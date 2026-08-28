#!/usr/bin/env python3
"""Genera el sitio Jekyll a partir de las fuentes de investigación del
proyecto:

  sources/<obra>/texto-limpio/*.md   -> _documentos/<obra>/NNN.md
  entidades/<obra>/personas.json     -> _personas/<obra>/<slug>.md
  entidades/<obra>/lugares.json      -> _lugares/<obra>/<slug>.md
  entidades/<obra>/relaciones-muestra.json (eventos) -> cronologia/index.md

  también escribe assets/data/<obra>.json (para assets/js/tag-entities.js)
  y assets/data/search-index.json (para assets/js/search.js).

Corrida única: no es parte del build de Jekyll. Las páginas que genera
quedan versionadas y son editables a mano después — volver a correr este
script sobre una obra ya editada a mano pisaría esas ediciones, así que no
se debe correr a ciegas sobre todo el sitio una vez que haya contenido
corregido a mano.
"""
import html
import json
import re
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

OBRAS = [
    {"clave": "bernal-diaz", "archivo": "sources/bernal-diaz/texto-limpio/historia-verdadera-tomo1.md"},
    {"clave": "las-casas", "archivo": "sources/las-casas/texto-limpio/historia-de-las-indias-tomo2.md"},
    {"clave": "colon-cartas", "archivo": "sources/colon-cartas/texto-limpio/relaciones-cartas-colon.md"},
    {"clave": "cortes", "archivo": "sources/cortes/texto-limpio/cartas-de-relacion.md"},
    {"clave": "cristobal-colon", "archivo": "sources/cristobal-colon/texto-limpio/diario-primer-viaje-colon.md"},
]

CAP_BLURBS = 20
VENTANA_SNIPPET = 140
YEAR_RE = re.compile(r"\b(1[2-5]\d{2})\b")


def slugify(texto):
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9]+", "-", texto).strip("-")
    return texto


def escribir(ruta, front_matter, cuerpo):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    fm = yaml.safe_dump(front_matter, allow_unicode=True, sort_keys=False, default_flow_style=False, width=100000)
    ruta.write_text(f"---\n{fm}---\n{cuerpo.strip()}\n", encoding="utf-8")


def leer_obra(ruta_rel):
    raw = (ROOT / ruta_rel).read_text(encoding="utf-8")
    fin = raw.index("\n---\n", 4)
    meta = yaml.safe_load(raw[4:fin]) or {}
    body = raw[fin + 5:]
    return meta, body


def partir_capitulos(body):
    partes = re.split(r"(?m)^## (.+)$", body)
    capitulos = []
    for i in range(1, len(partes), 2):
        heading = partes[i].strip()
        texto = partes[i + 1] if i + 1 < len(partes) else ""
        capitulos.append({"heading": heading, "texto": texto})
    return capitulos


def normalizar_parrafos(texto):
    bloques = re.split(r"\n\s*\n", texto.strip())
    parrafos = []
    for b in bloques:
        linea = " ".join(l.strip() for l in b.splitlines() if l.strip())
        if linea:
            parrafos.append(linea)
    return parrafos


def cargar_entidades(clave):
    base = ROOT / "entidades" / clave
    personas = json.loads((base / "personas.json").read_text(encoding="utf-8"))
    lugares = json.loads((base / "lugares.json").read_text(encoding="utf-8"))
    rel_path = base / "relaciones-muestra.json"
    relaciones = json.loads(rel_path.read_text(encoding="utf-8")) if rel_path.exists() else {}
    return personas, lugares, relaciones


def candidatos_de(entidad):
    cands = set()
    base = re.sub(r"\s*\([^)]*\)\s*", " ", entidad["canonical_name"]).strip()
    if base:
        cands.add(base)
    for a in entidad.get("aliases", []):
        if a and a.strip():
            cands.add(a.strip())
    return {c for c in cands if len(c) >= 3}


def construir_indice(entidades):
    alias_map = {}
    for e in entidades:
        for c in candidatos_de(e):
            if c not in alias_map:
                alias_map[c] = e
    lista = sorted(alias_map.keys(), key=len, reverse=True)
    if not lista:
        return alias_map, None
    patron = "|".join(re.escape(c) for c in lista)
    return alias_map, re.compile(r"\b(?:" + patron + r")\b")


def hacer_snippet(texto, inicio, fin):
    ini = max(0, inicio - VENTANA_SNIPPET)
    tope = min(len(texto), fin + VENTANA_SNIPPET)
    pre = html.escape(texto[ini:inicio])
    mid = html.escape(texto[inicio:fin])
    post = html.escape(texto[fin:tope])
    prefijo = "…" if ini > 0 else ""
    sufijo = "…" if tope < len(texto) else ""
    return f"{prefijo}{pre}<mark>{mid}</mark>{post}{sufijo}"


def bio_persona(e):
    partes = []
    if e.get("role"):
        partes.append(f"Aparece en el texto como {e['role']}.")
    else:
        partes.append("Aparece mencionada en el texto.")
    if e.get("mention_count_aprox"):
        partes.append(f"Se la menciona aproximadamente {e['mention_count_aprox']} veces a lo largo de la obra.")
    if e.get("aliases"):
        partes.append("También aparece nombrada como: " + ", ".join(e["aliases"]) + ".")
    return " ".join(partes)


def bio_lugar(e):
    partes = []
    if e.get("modern_equivalent"):
        partes.append(f"Corresponde aproximadamente a {e['modern_equivalent']} en la geografía actual.")
    else:
        partes.append("Lugar mencionado en el texto.")
    if e.get("mention_count_aprox"):
        partes.append(f"Se lo menciona aproximadamente {e['mention_count_aprox']} veces a lo largo de la obra.")
    if e.get("aliases"):
        partes.append("También aparece nombrado como: " + ", ".join(e["aliases"]) + ".")
    return " ".join(partes)


def muestrear_parejo(lista, tope):
    if len(lista) <= tope:
        return lista
    paso = len(lista) / tope
    return [lista[int(i * paso)] for i in range(tope)]


def main():
    todos_los_eventos = []  # para cronologia/index.md
    indice_busqueda = []  # para assets/data/search-index.json

    for obra in OBRAS:
        clave = obra["clave"]
        meta, body = leer_obra(obra["archivo"])
        capitulos = partir_capitulos(body)
        total = len(capitulos)
        obra_titulo = meta.get("titulo", clave)
        autor = meta.get("autor", "")

        personas, lugares, relaciones = cargar_entidades(clave)
        entidades = []
        for p in personas:
            slug = p["id"].split(":", 1)[1]
            entidades.append({**p, "tipo": "persona", "slug": slug, "url": f"/personas/{clave}/{slug}/"})
        for l in lugares:
            slug = l["id"].split(":", 1)[1]
            entidades.append({**l, "tipo": "lugar", "slug": slug, "url": f"/lugares/{clave}/{slug}/"})

        alias_map, regex = construir_indice(entidades)

        # menciones[entity_id] = lista de {heading, url, occ, html}
        menciones = {e["id"]: [] for e in entidades}

        capitulo_urls = []
        for i, cap in enumerate(capitulos):
            parrafos = normalizar_parrafos(cap["texto"])
            url_cap = f"/documentos/{clave}/{i:03d}/"
            capitulo_urls.append(url_cap)

            escribir(
                ROOT / "_documentos" / clave / f"{i:03d}.md",
                {
                    "obra": clave,
                    "obra_titulo": obra_titulo,
                    "autor": autor,
                    "heading": cap["heading"],
                    "chapter_index": i,
                    "total_capitulos": total,
                },
                "\n\n".join(parrafos),
            )

            if regex is not None:
                occ_por_entidad = {}
                for parrafo in parrafos:
                    for m in regex.finditer(parrafo):
                        ent = alias_map[m.group(0)]
                        n = occ_por_entidad.get(ent["id"], 0)
                        occ_por_entidad[ent["id"]] = n + 1
                        menciones[ent["id"]].append(
                            {
                                "heading": cap["heading"],
                                "url": url_cap,
                                "occ": n,
                                "html": hacer_snippet(parrafo, m.start(), m.end()),
                            }
                        )

            indice_busqueda.append(
                {"heading": cap["heading"], "obra_titulo": obra_titulo, "url": url_cap, "texto": " ".join(parrafos)}
            )

        # páginas de personas y lugares
        for p in personas:
            slug = p["id"].split(":", 1)[1]
            total_menciones = menciones.get(p["id"], [])
            muestra = muestrear_parejo(total_menciones, CAP_BLURBS)
            if len(muestra) < len(total_menciones):
                hint = f"Se muestran {len(muestra)} de {len(total_menciones)} menciones a lo largo de la obra."
            elif total_menciones:
                hint = f"Las {len(total_menciones)} menciones de esta persona en el texto."
            else:
                hint = "No se encontraron menciones etiquetadas en el texto."
            escribir(
                ROOT / "_personas" / clave / f"{slug}.md",
                {
                    "obra": clave,
                    "obra_titulo": obra_titulo,
                    "entity_id": p["id"],
                    "canonical_name": p["canonical_name"],
                    "aliases": p.get("aliases", []),
                    "role": p.get("role", ""),
                    "mention_count_aprox": p.get("mention_count_aprox"),
                    "status": p.get("status", "candidata"),
                    "notas": p.get("notas", ""),
                    "mentions_hint": hint,
                    "blurbs": muestra,
                },
                bio_persona(p),
            )

        for l in lugares:
            slug = l["id"].split(":", 1)[1]
            total_menciones = menciones.get(l["id"], [])
            muestra = muestrear_parejo(total_menciones, CAP_BLURBS)
            if len(muestra) < len(total_menciones):
                hint = f"Se muestran {len(muestra)} de {len(total_menciones)} menciones a lo largo de la obra."
            elif total_menciones:
                hint = f"Las {len(total_menciones)} menciones de este lugar en el texto."
            else:
                hint = "No se encontraron menciones etiquetadas en el texto."
            escribir(
                ROOT / "_lugares" / clave / f"{slug}.md",
                {
                    "obra": clave,
                    "obra_titulo": obra_titulo,
                    "entity_id": l["id"],
                    "canonical_name": l["canonical_name"],
                    "aliases": l.get("aliases", []),
                    "modern_equivalent": l.get("modern_equivalent", ""),
                    "mention_count_aprox": l.get("mention_count_aprox"),
                    "status": l.get("status", "candidata"),
                    "notas": l.get("notas", ""),
                    "mentions_hint": hint,
                    "blurbs": muestra,
                },
                bio_lugar(l),
            )

        # assets/data/<obra>.json para tag-entities.js
        datos_obra = [
            {"id": e["id"], "canonical_name": e["canonical_name"], "aliases": e.get("aliases", []), "tipo": e["tipo"], "url": e["url"]}
            for e in entidades
        ]
        (ROOT / "assets" / "data").mkdir(parents=True, exist_ok=True)
        (ROOT / "assets" / "data" / f"{clave}.json").write_text(
            json.dumps(datos_obra, ensure_ascii=False, indent=0), encoding="utf-8"
        )

        # eventos para cronología
        lugares_por_id = {l["id"]: l for l in lugares}
        for ev in relaciones.get("eventos", []):
            lugar = lugares_por_id.get(ev.get("place_id"))
            if lugar:
                lugar_slug = lugar["id"].split(":", 1)[1]
                lugar_nombre = lugar["canonical_name"]
                lugar_url = f"/lugares/{clave}/{lugar_slug}/"
            else:
                lugar_nombre = ev.get("place_id", "")
                lugar_url = None
            date_normalized = ev.get("date_normalized")
            if date_normalized:
                clave_orden = date_normalized
            else:
                m = YEAR_RE.search(ev.get("date_text", ""))
                clave_orden = f"{m.group(1)}-99-99" if m else "9999-99-99"
            todos_los_eventos.append(
                {
                    "clave_orden": clave_orden,
                    "nombre": ev.get("name", ""),
                    "fecha_texto": ev.get("date_text", ""),
                    "obra_titulo": obra_titulo,
                    "lugar_nombre": lugar_nombre,
                    "lugar_url": lugar_url,
                }
            )

    (ROOT / "assets" / "data" / "search-index.json").write_text(
        json.dumps(indice_busqueda, ensure_ascii=False, indent=0), encoding="utf-8"
    )

    # cronologia/index.md — página estática (los datos ya quedan
    # embebidos en el HTML, no hace falta Liquid para esto)
    todos_los_eventos.sort(key=lambda e: e["clave_orden"])
    filas = []
    for ev in todos_los_eventos:
        if ev["lugar_url"]:
            lugar_html = f'<a href="{ev["lugar_url"]}">{html.escape(ev["lugar_nombre"])}</a>'
        else:
            lugar_html = html.escape(ev["lugar_nombre"]) if ev["lugar_nombre"] else ""
        fecha = html.escape(ev["fecha_texto"]) if ev["fecha_texto"] else "sin fecha precisa"
        filas.append(
            f'  <div class="tl-item">\n'
            f'    <div class="tl-date mono">{fecha}</div>\n'
            f'    <div class="tl-name">{html.escape(ev["nombre"])}<div class="tl-obra">{html.escape(ev["obra_titulo"])}</div></div>\n'
            f'    <div class="tl-place">{lugar_html}</div>\n'
            f"  </div>"
        )
    cuerpo_cronologia = (
        '<p class="hint">Eventos identificados en la primera pasada de extracción de relaciones '
        "(todavía cubre solo una parte de cada obra — ver CLAUDE.md, sección Pendientes).</p>\n"
        '<div class="timeline-list">\n' + "\n".join(filas) + "\n</div>\n"
    )
    escribir(ROOT / "cronologia" / "index.md", {"layout": "default", "title": "Cronología", "permalink": "/cronologia/"}, cuerpo_cronologia)

    print(f"Listo: {sum(1 for _ in (ROOT / '_documentos').rglob('*.md'))} documentos, "
          f"{sum(1 for _ in (ROOT / '_personas').rglob('*.md'))} personas, "
          f"{sum(1 for _ in (ROOT / '_lugares').rglob('*.md'))} lugares, "
          f"{len(todos_los_eventos)} eventos.")


if __name__ == "__main__":
    main()
