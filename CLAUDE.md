# Crónicas de Indias — contexto del proyecto

Este archivo se lee automáticamente al abrir Claude Code en esta carpeta. Da el
contexto completo para seguir el trabajo sin tener que volver a explicarlo.
El `README.md` de esta misma carpeta es la versión corta pensada para una
persona; este documento es más largo y técnico, pensado para retomar el
trabajo con un agente.

## Qué es esto

Un archivo relacional y consultable de crónicas españolas (dominio público)
sobre la conquista de América: texto completo + entidades (personas, lugares,
eventos) + relaciones entre ellas, con cita a la fuente exacta. Pensado para
historiadores y escritores, para publicarse como sitio web. Idioma: español
neutro latinoamericano en todo el contenido dirigido al usuario (UI del MVP,
READMEs, METADATA).

## Estado actual (snapshot)

- **Fase 0-1 completas** para dos obras: descarga, limpieza de texto,
  separación de aparato editorial.
- **Fase 2 (entidades y relaciones): primera pasada solo sobre el Capítulo 1**
  de cada una de las dos obras activas — el resto de los capítulos (110 de
  Bernal Díaz, 96 de Las Casas) todavía no tiene relaciones extraídas. Ver
  "Pendientes" más abajo.
- **MVP publicado** (`mvp/archivo-final.html`, también como Artifact —
  ver más abajo) con las dos obras completas (208 capítulos) navegables,
  entidades enlazadas dentro del texto y página de detalle por persona.
- **Repo en GitHub y Pages publicado**: el proyecto vive en
  https://github.com/codingadrian/cronicas-de-indias (público) y el MVP se
  sirve en https://codingadrian.github.io/cronicas-de-indias/. Ver
  "GitHub / GitHub Pages" más abajo para cómo está armado el deploy.

## Estructura de carpetas

```
/historia
├── README.md                          resumen del proyecto para una persona
├── CLAUDE.md                          este archivo
├── .gitignore                         excluye sources/cortes/raw/*.pdf (supera 100 MB de GitHub)
├── .github/workflows/pages.yml        deploy de mvp/archivo-final.html a GitHub Pages
├── plan/
│   ├── plan.html                      plan del proyecto, copia local
│   └── README.md                      apunta al Artifact publicado del plan
├── schema/
│   └── entidades-relaciones.schema.json   modelo de datos (ver abajo)
├── sources/                           por obra: raw/ (fuente sin tocar) + texto-limpio/ (Fase 1)
│   ├── bernal-diaz/    activa  — texto-limpio/historia-verdadera-tomo1.md (111 cap., ~126k palabras)
│   ├── las-casas/      activa  — texto-limpio/historia-de-las-indias-tomo2.md (97 cap., ~178k palabras)
│   ├── hernando-colon/ en pausa — solo raw/, sin texto-limpio/
│   └── cortes/         en pausa — solo raw/ (PDF escaneado, 344 MB, sin OCR)
├── entidades/
│   ├── bernal-diaz/personas.json, lugares.json, candidatos-frecuencia.json, relaciones-muestra.json
│   └── las-casas/          (misma estructura)
└── mvp/
    ├── README.md                      detalle del MVP, qué valida y qué no
    └── archivo-final.html             el MVP: HTML autocontenido, ~1.8 MB
```

Cada `METADATA.md` en `sources/<obra>/` tiene front-matter YAML (título,
autor, edición, estado) y una nota de por qué esa obra está activa o en
pausa — léelos antes de retomar Hernando Colón o Cortés, tienen el motivo
exacto documentado.

## Decisiones de alcance ya tomadas (no las reabras sin pedir)

- **Cortés — Cartas de relación: en pausa.** La única fuente conseguida es un
  PDF escaneado de 344 MB sin OCR (`sources/cortes/raw/`). Se decidió no
  hacer OCR todavía para no bloquear el resto del piloto. Wikisource (mejor
  calidad) no es alcanzable desde este entorno de nube — habría que
  descargarlo a mano como se hizo con las otras obras, o hacer OCR del PDF
  por rangos de páginas.
- **Hernando Colón — Historia del Almirante: en pausa.** El único texto
  disponible (Internet Archive, edición Arranz) mezcla notas editoriales
  modernas dentro de los capítulos por un problema de orden en el volcado
  OCR; no se pudo separar de forma confiable el texto de 1571 del aparato
  moderno. Nota positiva para cuando se retome: entre los capítulos LXI-LXIII
  está completa la "Relación acerca de las antigüedades de los indios" de
  fray Ramón Pané, que vale la pena tratar como fuente independiente.
- **Las Casas: el archivo que se bajó como "Brevísima relación" en realidad
  es *Historia de las Indias* (tomo II).** Se descubrió al leer la
  transcripción de portada y la numeración de capítulos (LXXXIII-CLXXXIII).
  Se decidió usarlo tal cual en el piloto en vez de conseguir la Brevísima
  relación aparte — es la obra activa del piloto hoy.
- **Fuente de los textos: Project Gutenberg**, no Wikisource — WebFetch no
  puede alcanzar `es.wikisource.org` desde este entorno de nube ("cache-only
  domain"). Si se sigue trabajando desde un entorno con red distinta (como
  Claude Code local), Wikisource podría ser una fuente mejor a probar de
  nuevo para los textos que faltan.

## Modelo de datos

`schema/entidades-relaciones.schema.json` define 4 tipos de entidad (Person,
Place, Event, Source) y 7 tipos de relación tipada (`present_at`,
`allied_with`, `fought_against`, `occurred_in`, `occurred_on`, `traveled_to`,
`cited_in`), cada relación citando su `Source` exacta (obra + capítulo).
Estado de revisión por entrada: `candidata` → `revisada` → `publicada` /
`descartada`.

Los `personas.json`/`lugares.json` reales (`entidades/<obra>/`) tienen ids
con prefijo (`person:...`, `place:...`), `canonical_name`, `aliases`, `role`
o `modern_equivalent`, `mention_count_aprox`, `status`, y a veces `notas`
(ambigüedades a resolver). **Los ids están scoped por obra, no son globales**:
las dos obras generaron sus registros por separado, así que un mismo lugar
real puede tener el mismo id en ambas (ej. `place:cuba` aparece en
`bernal-diaz/lugares.json` y en `las-casas/lugares.json` como dos entradas
distintas con el mismo id) — cualquier código que use estos ids como clave
única global tiene que combinarlos con `obra`, no con el id solo. El MVP ya
maneja esto (ver más abajo); tenlo en cuenta si se arma un merge global de
entidades para fases futuras.

`candidatos-frecuencia.json` es la salida cruda del primer paso automático
(conteo de nombres propios de 2+ palabras) — sirve de referencia para seguir
canonizando entidades, no está pensado para mostrarse tal cual.

`relaciones-muestra.json` solo cubre el Capítulo 1 de cada obra — es la
"prueba de que el modelo funciona sobre texto real", no una extracción
completa.

## El MVP (`mvp/archivo-final.html`)

Publicado como Artifact:
https://claude.ai/code/artifact/1f4b9b79-bc9d-42c8-aa56-b4bdfd7c3dfd

Un solo archivo HTML autocontenido (sin build, sin dependencias salvo un
`<link>` a Google Fonts) con los datos embebidos en
`<script id="data-corpus" type="application/json">` (obras completas +
personas + lugares + eventos + relaciones). El JS principal está en el
segundo `<script>` del archivo, vanilla, dentro de un único IIFE.

Cinco pestañas: **Documentos** (biblioteca de las 2 obras → tabla de
contenidos → lector de capítulo con navegación anterior/siguiente),
**Personas**, **Lugares** (con mapa propio), **Cronología**, **Red de
relaciones** (grafo de fuerza).

### Etiquetado de entidades dentro del texto (Documentos)

`tagChapterHtml(obraKey, rawText)` envuelve menciones de personas, lugares y
años en `<span class="ent ...">` clicables, directamente sobre el texto
limpio (sin alterarlo). Puntos a tener en cuenta si se toca este código:

- El regex de cada entidad usa lookaround de límite de palabra con
  `\p{L}\p{N}` (flags `gu`), **no `\b`** — `\b` de JS no trata las letras
  acentuadas como caracteres de palabra, así que falla en nombres como
  "Ávila" o "Núñez". Cualquier regex nuevo sobre este texto tiene que usar
  el mismo patrón de lookaround.
- Orden de las pasadas: primero años (`YEAR_RE`, 4 dígitos 1200-1599), después
  personas/lugares — en ese orden, para que los dígitos de `data-occ="N"`
  que se insertan después nunca puedan confundirse con un año de 4 cifras.
- `data-occ` numera las apariciones de una misma entidad dentro de un mismo
  capítulo (0-based) — es lo que permite saltar a la mención exacta desde la
  página de una persona ("Leer en contexto →").
- El etiquetado es por coincidencia de texto (nombre/alias), no desambigua
  homónimos reales.

### Página de persona

Al hacer clic en un nombre se arma una página con "retrato" sintetizado solo
a partir de los datos del registro (rol + cuántas veces se la menciona —
explícitamente rotulado como no-biografía-externa, para no inventar datos
históricos no verificados por este corpus) y una lista de menciones
("blurbs") tomadas del texto real. Cuando una persona tiene muchas menciones
(Cortés: ~834) se muestrea parejo a lo largo de todo el texto hasta un tope
de 20 (`CAP = 20` en `buildBlurbs`), no solo las primeras — así la muestra
no queda toda en el primer capítulo.

### Testing

No hay framework de pruebas en el repo. Para validar el MVP se armó un
arnés de pruebas puntual con `jsdom` (`npm install jsdom`, cargar el HTML con
`runScripts: 'dangerously'`, disparar clics reales con
`dispatchEvent(new window.MouseEvent(...))` y verificar el DOM resultante) —
no quedó guardado como archivo en el repo, se armó y tiró en `/tmp` durante
la sesión. Si se agregan features nuevas al MVP conviene rearmar algo
parecido antes de publicar, en vez de confiar solo en QA visual (la
herramienta de captura de pantalla del navegador en este entorno de nube es
intermitente — falla y se recupera sin patrón claro).

## Cómo previsualizar el MVP fuera de este entorno

No hay herramienta de "Artifact" en Claude Code local. Para ver
`archivo-final.html` alcanza con abrirlo directo en el navegador
(`file://...`) — es autocontenido, no necesita servidor. Si hace falta un
servidor (por ejemplo para probar rutas relativas más adelante), un
`python3 -m http.server` en la carpeta `mvp/` alcanza.

## GitHub / GitHub Pages (ejecutado)

Repo: https://github.com/codingadrian/cronicas-de-indias (público, rama
`main`). Pages publicado en https://codingadrian.github.io/cronicas-de-indias/.

- **`sources/cortes/raw/*.pdf` (344 MB) está en `.gitignore`** — supera el
  límite de 100 MB por archivo de GitHub. La fuente para volver a
  conseguirlo está documentada en `sources/cortes/METADATA.md`; no se perdió
  nada, solo no está versionado.
- A `mvp/archivo-final.html` se le agregó el esqueleto HTML5 completo
  (`<!DOCTYPE html><html lang="es"><head>...</head><body>...</body></html>`)
  que antes le daba el visor de Artifacts — ya es una página standalone.
- **Deploy vía GitHub Actions** (`build_type: workflow` en la config de
  Pages del repo, no el modo Jekyll/branch por defecto), definido en
  `.github/workflows/pages.yml`: en cada push a `main` copia
  `mvp/archivo-final.html` → `index.html` y lo publica. `mvp/` sigue siendo
  la única fuente de verdad — no hay copia duplicada del archivo en el repo.
  Se descartó la opción de un sitio Jekyll más completo (portada, página
  "sobre el proyecto", etc.) por ahora — se puede retomar más adelante si
  hace falta más que la página única del MVP.
- Para forzar un redeploy manual sin nuevo commit: `gh workflow run
  pages.yml --repo codingadrian/cronicas-de-indias` (el workflow tiene
  `workflow_dispatch`).

## Pendientes (en orden sugerido)

1. **Seguir la extracción de relaciones capítulo por capítulo** — es el
   trabajo de fondo que el MVP dejó pausado a pedido del usuario para
   validar primero la interfaz. Cada tanda nueva de relaciones se refleja
   directamente en el mapa, la cronología y el grafo del MVP sin tocar
   código (los datos se combinan al armar `datos.json` → JSON embebido).
2. Retomar Cortés (OCR del PDF, por rangos de páginas) y Hernando Colón
   (limpieza manual o edición alternativa) cuando haya tiempo — no son
   bloqueantes para lo demás.
3. Segunda revisión de las entradas marcadas `"status": "candidata"` en los
   registros de personas/lugares, y de las notas de ambigüedad (ej. "D Diego"
   en Las Casas).

## Convenciones a mantener

- Español neutro latinoamericano en todo contenido dirigido al usuario.
- Ids con prefijo por tipo (`person:`, `place:`, `event:`, `source:`),
  slug en minúsculas con guiones, **scoped por obra** (ver nota en "Modelo
  de datos").
- Toda relación cita su `Source` exacta (obra + capítulo).
- No sacar Cortés/Hernando Colón de pausa, ni reabrir la decisión de usar
  *Historia de las Indias* en vez de la *Brevísima relación*, sin que el
  usuario lo pida explícitamente — son decisiones de alcance ya tomadas con
  él, con motivo documentado arriba.
