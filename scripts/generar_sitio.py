#!/usr/bin/env python3
"""Genera el sitio Jekyll a partir de las fuentes de investigación del
proyecto:

  sources/<obra>/texto-limpio/*.md   -> _documentos/<obra>/NNN.md
  entidades/<obra>/personas.json     -> _personas/<obra>/<slug>.md
  entidades/<obra>/lugares.json      -> _lugares/<obra>/<slug>.md

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
    {"clave": "xerez", "archivo": "sources/xerez/texto-limpio/verdadera-relacion.md"},
    {"clave": "cabeza-de-vaca", "archivo": "sources/cabeza-de-vaca/texto-limpio/naufragios.md"},
    {"clave": "munoz-camargo", "archivo": "sources/munoz-camargo/texto-limpio/historia-de-tlaxcala.md"},
    {"clave": "pedro-pizarro", "archivo": "sources/pedro-pizarro/texto-limpio/relacion-descubrimiento-conquista.md"},
    {"clave": "ixtlilxochitl", "archivo": "sources/ixtlilxochitl/texto-limpio/historia-nacion-chichimeca.md"},
    {"clave": "cieza-de-leon", "archivo": "sources/cieza-de-leon/texto-limpio/cronica-del-peru.md"},
    {"clave": "tezozomoc", "archivo": "sources/tezozomoc/texto-limpio/cronica-mexicana.md"},
    {"clave": "motolinia", "archivo": "sources/motolinia/texto-limpio/historia-de-los-indios.md"},
    {"clave": "pedro-martir", "archivo": "sources/pedro-martir/texto-limpio/decadas-del-nuevo-mundo.md"},
    {"clave": "acosta", "archivo": "sources/acosta/texto-limpio/historia-natural-moral-indias.md"},
]

CAP_BLURBS = 20
VENTANA_SNIPPET = 140


def cargar_editores():
    ruta = ROOT / "_data" / "editores.yml"
    if not ruta.exists():
        return {}
    return yaml.safe_load(ruta.read_text(encoding="utf-8")) or {}


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


COLOR_ORIGINAL = "#c9a227"
VENTANA_NOTA_VIEJA = 10  # párrafos hacia adelante a buscar la definición de una nota vieja
COLOR_EDITOR_SIN_REGISTRAR = "#8a8570"

MARCADOR_RE = re.compile(r"\s?\((\d+)\)")
DEF_EDITOR_RE = re.compile(r"\((\d+),([^,()]+)(?:,([^,()]+))?\)")
AUTOR_NOTA_VIEJA_RE = re.compile(r"[—\-]\s*([A-ZÁÉÍÓÚÑ][^.]{2,40})\.?\s*$")


def ultimas_n_palabras(texto, n):
    palabras = texto.strip().split()
    return " ".join(palabras[-n:]) if palabras else ""


def autor_de_nota_vieja(texto):
    m = AUTOR_NOTA_VIEJA_RE.search(texto)
    return m.group(1).strip() if m else None


def procesar_comentarios(parrafos, editores):
    """Parsea comentarios al margen dentro de los párrafos de un capítulo,
    con dos sintaxis (ver CLAUDE.md, sección de comentarios):

    - Nota vieja (aparato editorial ya presente en la fuente, sin coma):
      `palabra (N)` en un párrafo, con la definición en el párrafo
      siguiente empezando `(N) texto...` — se anota como origen
      "original", color fijo amarillo, autor extraído de un "— Nombre."
      al final del texto si lo hay.
    - Comentario de editor (nuevo, con coma): `palabra(N)` seguido, más
      adelante en el MISMO párrafo, de `(N,Autor)texto...` o
      `(N,ancho,Autor)texto...` (ancho = cuántas palabras antes del
      marcador subrayar, default 1) — origen "editor", color del
      registro de editores si el alias matchea, gris si no.

    Devuelve (parrafos_sin_marcadores_ni_definiciones, lista_de_comentarios).
    Cada comentario incluye `ocurrencia`: cuántas veces ya apareció ese
    mismo texto de ancla en el cuerpo final ANTES de este punto — hace
    falta porque el mismo texto puede repetirse, y el navegador tiene que
    saber a cuál instancia exacta apuntar (ver assets/js/comments.js).
    """
    resultado = list(parrafos)
    consumidos = set()
    comentarios = []

    def texto_final_hasta(i, prefijo):
        return "\n\n".join(p for idx, p in enumerate(resultado[:i]) if idx not in consumidos) + "\n\n" + prefijo

    i = 0
    while i < len(resultado):
        if i in consumidos:
            i += 1
            continue
        cambiado = True
        while cambiado:
            cambiado = False
            parrafo = resultado[i]

            # --- estilo editor: marcador y definición (con coma) en el mismo párrafo ---
            encontrado = False
            for m in DEF_EDITOR_RE.finditer(parrafo):
                ref = m.group(1)
                marcador_m = None
                for mm in re.finditer(r"\(" + re.escape(ref) + r"\)", parrafo[: m.start()]):
                    marcador_m = mm
                if not marcador_m:
                    continue
                if m.group(3) is not None:
                    ancho, autor_alias = int(m.group(2)), m.group(3).strip()
                else:
                    ancho, autor_alias = 1, m.group(2).strip()
                # El texto del comentario termina al final del párrafo, O antes
                # si hay otra definición (N,Autor) más adelante en el mismo
                # párrafo — pasa si dos párrafos de comentario quedaron
                # pegados por faltar una línea en blanco entre ellos en la
                # fuente; sin este corte, el primer comentario se comería el
                # texto real y la segunda definición entera.
                siguiente_def = DEF_EDITOR_RE.search(parrafo, m.end())
                fin_texto = siguiente_def.start() if siguiente_def else len(parrafo)
                texto_comentario = parrafo[m.end(): fin_texto].strip()
                antes = parrafo[: marcador_m.start()]
                anchor = ultimas_n_palabras(antes, ancho)
                # -1 porque `antes` termina justo en `anchor` por construcción
                # (ultimas_n_palabras), así que el conteo siempre incluye esa
                # propia aparición — sin restarla, toda ocurrencia quedaría
                # corrida en +1 (un verdadero primer uso saldría "1", no "0").
                ocurrencia = (texto_final_hasta(i, antes).count(anchor) - 1) if anchor else 0
                if autor_alias.strip().lower() == "original":
                    # Palabra reservada: no es un editor, es una nota vieja
                    # de la propia edición que se está convirtiendo a mano en
                    # vez de dejar que la detección automática la encuentre
                    # (ver "estilo viejo" más abajo) — mismo criterio de
                    # color/autor que esa detección automática.
                    comentarios.append({
                        "anchor": anchor,
                        "ocurrencia": ocurrencia,
                        "origen": "original",
                        "autor": autor_de_nota_vieja(texto_comentario) or "Nota del editor",
                        "color": COLOR_ORIGINAL,
                        "texto": texto_comentario,
                    })
                else:
                    info = editores.get(autor_alias)
                    comentarios.append({
                        "anchor": anchor,
                        "ocurrencia": ocurrencia,
                        "origen": "editor",
                        "autor": info["nombre"] if info else autor_alias,
                        "color": info["color"] if info else COLOR_EDITOR_SIN_REGISTRAR,
                        "texto": texto_comentario,
                    })
                resultado[i] = (
                    parrafo[: marcador_m.start()]
                    + parrafo[marcador_m.end(): m.start()]
                    + parrafo[fin_texto:]
                ).rstrip()
                cambiado = True
                encontrado = True
                break
            if encontrado:
                continue

            # --- estilo viejo: marcador con definición en un párrafo
            # cercano más adelante (no necesariamente el inmediato
            # siguiente — a veces varios párrafos de título/fecha se
            # interponen entre el marcador y el bloque de notas real,
            # sobre todo en los encabezados de carta) ---
            for mm in MARCADOR_RE.finditer(parrafo):
                ref = mm.group(1)
                m_def = None
                sig = None
                for cand in range(i + 1, min(i + 1 + VENTANA_NOTA_VIEJA, len(resultado))):
                    if cand in consumidos:
                        continue
                    cand_m = re.match(r"^\(" + re.escape(ref) + r"\)\s*(.*)$", resultado[cand], re.S)
                    if cand_m:
                        m_def, sig = cand_m, cand
                        break
                if not m_def:
                    continue
                texto_nota = m_def.group(1).strip()
                autor = autor_de_nota_vieja(texto_nota)
                antes = parrafo[: mm.start()]
                anchor = ultimas_n_palabras(antes, 1)
                # -1 porque `antes` termina justo en `anchor` por construcción
                # (ultimas_n_palabras), así que el conteo siempre incluye esa
                # propia aparición — sin restarla, toda ocurrencia quedaría
                # corrida en +1 (un verdadero primer uso saldría "1", no "0").
                ocurrencia = (texto_final_hasta(i, antes).count(anchor) - 1) if anchor else 0
                comentarios.append({
                    "anchor": anchor,
                    "ocurrencia": ocurrencia,
                    "origen": "original",
                    "autor": autor or "Nota del editor",
                    "color": COLOR_ORIGINAL,
                    "texto": texto_nota,
                })
                consumidos.add(sig)
                resultado[i] = (parrafo[: mm.start()] + parrafo[mm.end():]).rstrip()
                cambiado = True
                break
        i += 1

    parrafos_finales = [p for idx, p in enumerate(resultado) if idx not in consumidos]
    return parrafos_finales, comentarios


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
    indice_busqueda = []  # para assets/data/search-index.json
    editores = cargar_editores()

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
            parrafos, comentarios = procesar_comentarios(parrafos, editores)
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
                    "chapter_index_padded": f"{i:03d}",
                    "total_capitulos": total,
                    "tiene_comentarios": bool(comentarios),
                },
                "\n\n".join(parrafos),
            )

            if comentarios:
                (ROOT / "assets" / "data" / "comentarios").mkdir(parents=True, exist_ok=True)
                (ROOT / "assets" / "data" / "comentarios" / f"{clave}-{i:03d}.json").write_text(
                    json.dumps(comentarios, ensure_ascii=False, indent=0), encoding="utf-8"
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

    (ROOT / "assets" / "data" / "search-index.json").write_text(
        json.dumps(indice_busqueda, ensure_ascii=False, indent=0), encoding="utf-8"
    )

    print(f"Listo: {sum(1 for _ in (ROOT / '_documentos').rglob('*.md'))} documentos, "
          f"{sum(1 for _ in (ROOT / '_personas').rglob('*.md'))} personas, "
          f"{sum(1 for _ in (ROOT / '_lugares').rglob('*.md'))} lugares.")


if __name__ == "__main__":
    main()
