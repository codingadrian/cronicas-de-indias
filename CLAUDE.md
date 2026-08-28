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

- **Fase 0-1 completas para cinco obras**: descarga, limpieza de texto,
  separación de aparato editorial. Bernal Díaz y Las Casas vienen de
  Project Gutenberg; el Diario de Colón, de Wikisource (funcionó desde
  Claude Code local, a diferencia del entorno de nube original — ver nota
  más abajo); Cortés y las Cartas de Colón, de Archive.org.
- **Fase 2 (entidades y relaciones): las cinco obras activas tienen ahora
  al menos una primera pasada** (2026-08-28, hecho en paralelo con 5 forks,
  uno por obra, después fusionado y verificado a mano — ver "Pendientes"
  para cómo seguir cada una):
  - **Bernal Díaz**: Capítulos 1-18 de 111 (93 quedan). 41 personas, 31
    lugares, 10 eventos, 80 relaciones.
  - **Las Casas**: Capítulos 1-11 de 97 (86 quedan). 26 personas, 22
    lugares, 10 eventos, 40 relaciones.
  - **Diario de Colón**: Proemio + días 1-20 de 191 (~11%). 5 personas, 11
    lugares, 2 eventos, 13 relaciones. Colón se modeló como
    `person:cristobal-colon` (narrador/sujeto, con nota sobre la voz de
    Las Casas), mismo patrón que `person:bernal-diaz-del-castillo`.
  - **Cortés**: solo la Primera carta-relación de 5. 11 personas, 9
    lugares, 7 eventos, 29 relaciones.
  - **Colón — Cartas**: los primeros 3 documentos de 10 (Carta a
    Santángel + Rafael Sánchez + Memorial a Torres bajo un mismo
    capítulo, Instrucción a Margarite, Carta a los Reyes del 2º viaje).
    9 personas, 10 lugares, 4 eventos, 21 relaciones.

  **Bugs de integridad encontrados y corregidos en esta tanda** (vale la
  pena recordarlos si se retoma manualmente): (1) las entidades nuevas del
  Capítulo 1 de Bernal Díaz y de Las Casas se habían quedado solo en el
  log `entidades_nuevas` de `relaciones-muestra.json` sin copiarse nunca a
  `personas.json`/`lugares.json` — las relaciones citaban ids que no
  existían en el registro real (invisibles en el MVP). Ya están
  promovidas en ambas obras. (2) Un fork usó una relación `citado_en`
  persona→fuente en Las Casas, que no es como está pensado el esquema
  (`cited_in` es relación→fuente, y cada relación ya cita su fuente en su
  propio campo `source`) y apuntaba a un id sin registrar — se corrigió a
  `estuvo_presente_en` contra el evento correspondiente. Antes de dar por
  buena una tanda nueva, correr un chequeo de integridad referencial
  (todo `from`/`to` de `relaciones` debe resolver contra `personas` +
  `lugares` + `eventos` de esa misma obra) — quedó como buena práctica a
  repetir.
- **MVP publicado** (`mvp/archivo-final.html`, también como Artifact —
  ver más abajo) con las cinco obras completas (415 capítulos/entradas)
  navegables y buscables, y ahora **las cinco con al menos algunas
  entidades enlazadas en el texto** (antes solo Bernal Díaz/Las Casas
  tenían esto).
- **Cortés salió de pausa** el 2026-08-28 al conseguirse una edición
  digital (no escaneada) de las *Cartas de relación* — ver "Decisiones de
  alcance" más abajo, esto reabre una decisión previa.
- **Catálogo completo de 20 cronistas (`sources/CATALOGO.md`)**: el
  2026-08-28 el usuario dio una lista priorizada de 20 crónicas y pidió
  conseguirlas todas. Las 20 tienen ahora al menos Fase 0 (fuente
  descargada) — 17 obras nuevas quedaron en estado **"por procesar"**
  (`raw/` conseguido, Fase 1 sin empezar, sin revisión manual de calidad
  de OCR). Ninguna de las 17 está todavía en el MVP. Ver el catálogo para
  qué se consiguió de cada una, de dónde, y qué huecos quedan (obras
  parciales o ediciones distintas a la pedida).
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
│   ├── CATALOGO.md      catálogo completo de las 20 crónicas priorizadas por el usuario
│   │                    (2026-08-28) — qué se consiguió, de dónde, y qué falta por obra
│   ├── bernal-diaz/     activa  — texto-limpio/historia-verdadera-tomo1.md (111 cap., ~126k palabras)
│   ├── las-casas/       activa  — texto-limpio/historia-de-las-indias-tomo2.md (97 cap., ~178k palabras);
│   │                    también tiene la Brevísima relación por procesar (raw/ nada más)
│   ├── cristobal-colon/ activa  — texto-limpio/diario-primer-viaje-colon.md (191 entradas + proemio, ~54k palabras)
│   ├── colon-cartas/    activa  — texto-limpio/relaciones-cartas-colon.md (10 documentos, ~74k palabras, OCR sin corregir)
│   ├── cortes/          activa  — texto-limpio/cartas-de-relacion.md (5 cartas, ~172k palabras) — recién salió de pausa
│   ├── hernando-colon/  en pausa — solo raw/, sin texto-limpio/
│   └── (17 carpetas más, todas "por procesar" — raw/ conseguido el 2026-08-28,
│        Fase 1 pendiente: lopez-de-gomara, oviedo, pedro-martir, cabeza-de-vaca,
│        motolinia, sahagun, duran, acosta, cieza-de-leon, zarate, xerez,
│        pedro-pizarro, inca-garcilaso, guaman-poma, ixtlilxochitl, tezozomoc,
│        munoz-camargo — ver CATALOGO.md para el detalle de cada una)
├── entidades/
│   ├── bernal-diaz/personas.json, lugares.json, candidatos-frecuencia.json, relaciones-muestra.json
│   └── las-casas/          (misma estructura — las otras tres obras activas todavía no tienen carpeta acá, ver Pendientes)
└── mvp/
    ├── README.md                      detalle del MVP, qué valida y qué no
    └── archivo-final.html             el MVP: HTML autocontenido, ~1.8 MB
```

Cada `METADATA.md` en `sources/<obra>/` tiene front-matter YAML (título,
autor, edición, estado) y una nota de por qué esa obra está activa o en
pausa — léelos antes de retomar Hernando Colón, tienen el motivo exacto
documentado.

## Decisiones de alcance ya tomadas (no las reabras sin pedir)

- **Cortés — Cartas de relación: reactivada el 2026-08-28** (ya no está en
  pausa — esto reemplaza la decisión anterior de dejarla pausada). La
  pausa original era porque la única fuente conseguida era un PDF
  escaneado de 344 MB sin OCR; se consiguió una edición digital nacida
  digital (ePubLibre, 2013, vía Archive.org, no un escaneo) que no
  necesitó OCR, así que se sacó de pausa directamente. El PDF escaneado
  se conserva en `sources/cortes/raw/` pero ya no es la fuente activa —
  ver `sources/cortes/METADATA.md`.
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
- **Fuente de los textos: Project Gutenberg** para Bernal Díaz y Las Casas,
  no Wikisource — WebFetch no puede alcanzar `es.wikisource.org` desde el
  entorno de nube original ("cache-only domain"). **Confirmado que sí
  funciona desde Claude Code local**: el Diario de Colón se consiguió así
  (`sources/cristobal-colon/`) — Wikisource es una fuente a considerar de
  nuevo para completar Bernal Díaz (tomos 2-3) u otras obras, si se sigue
  trabajando localmente.
- **Cristóbal Colón — Diario de a bordo: activa, solo Fase 0-1.** Se agregó
  el 2026-08-28. El diario autógrafo original se perdió; el texto es la
  transcripción atribuida a fray Bartolomé de las Casas (ver
  `sources/cristobal-colon/METADATA.md`). Carpeta nombrada
  `cristobal-colon` (no `colon`) para no confundir con `hernando-colon/`
  (su hijo, obra distinta, en pausa). Está en el MVP como texto navegable
  y buscable, pero **sin entidades/relaciones curadas todavía** — no tiene
  carpeta en `entidades/`. Ver "Pendientes".
- **Cristóbal Colón — Relaciones y cartas: activa, solo Fase 0-1.** Se
  agregó el 2026-08-28 (edición de 1892, Archive.org). Carpeta separada
  `sources/colon-cartas/` (no dentro de `cristobal-colon/`) porque es otra
  obra del mismo autor. **Esta edición de 1892 incluye también la
  Relación del primer viaje (el mismo Diario)** — se excluyó esa parte de
  `texto-limpio/` para no duplicar contenido ya cubierto por
  `cristobal-colon/`. Texto con ruido de OCR sin corregir palabra por
  palabra (a diferencia de las otras cuatro obras) y dividido más grueso
  que el índice original del libro (10 bloques en vez de ~30 cartas/
  fragmentos) — ver `sources/colon-cartas/METADATA.md` para el detalle y
  qué falta si se quiere más granularidad.

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

`relaciones-muestra.json` sigue siendo una extracción parcial, no
completa, de cada obra — cubre los Capítulos 1-8 de Bernal Díaz y solo
el Capítulo 1 de Las Casas. El campo `entidades_nuevas` dentro de cada
archivo lleva un `capitulo` por entrada para saber en qué capítulo
apareció cada una por primera vez.

## El MVP (`mvp/archivo-final.html`)

Publicado como Artifact:
https://claude.ai/code/artifact/1f4b9b79-bc9d-42c8-aa56-b4bdfd7c3dfd

Un solo archivo HTML autocontenido (sin build, sin dependencias salvo un
`<link>` a Google Fonts) con los datos embebidos en
`<script id="data-corpus" type="application/json">` (obras completas +
personas + lugares + eventos + relaciones). El JS principal está en el
segundo `<script>` del archivo, vanilla, dentro de un único IIFE.

Cinco pestañas: **Documentos**, **Personas**, **Lugares**, **Cronología**,
**Red de relaciones** (grafo de fuerza). Personas/Lugares solo tienen datos
de Bernal Díaz y Las Casas — las otras tres obras todavía no tienen
entidades curadas (ver "Pendientes").

**Documentos** (2026-08-28: cambio de navegación) — un clic en una obra de
la biblioteca va directo al Capítulo 1 (ya no pasa por una pantalla de
tabla de contenidos aparte). El índice de capítulos vive *dentro* del lector
(`#doc-toc-toggle` + `#doc-toc-inline`, colapsado por defecto, con el
capítulo actual marcado `.current`) — clic en un capítulo salta ahí y
cierra el panel. Ver `renderInlineToc`/`openDocChapter` en el JS. **Ojo
si se vuelve a tocar este panel**: el div tiene doble clase
(`class="doc-toc doc-toc-inline"`) para reusar el estilo de botones de
`.doc-toc`, así que el atributo `hidden` nativo necesita la regla explícita
`.doc-toc-inline[hidden]{ display:none; }` — si no, la regla de autor
`.doc-toc{ display:flex }` gana y `hidden` deja de esconder el panel.

El lector (`.doc-reader`) está centrado (`margin:0 auto`), con
título/subtítulo centrados y el cuerpo (`.dr-body`) en `text-align:justify`.

### Etiquetado de entidades dentro del texto (Documentos)

`tagChapterHtml(obraKey, rawText)` envuelve menciones de personas, lugares y
años en `<span class="ent ...">` clicables, y arma el cuerpo en párrafos
(`<p>`) para que el lector se pueda justificar. Puntos a tener en cuenta si
se toca este código:

- El regex de cada entidad usa lookaround de límite de palabra con
  `\p{L}\p{N}` (flags `gu`), **no `\b`** — `\b` de JS no trata las letras
  acentuadas como caracteres de palabra, así que falla en nombres como
  "Ávila" o "Núñez". Cualquier regex nuevo sobre este texto tiene que usar
  el mismo patrón de lookaround.
- **El `.txt` fuente viene con saltos de línea duros cada ~70 caracteres**
  (formato típico de Gutenberg/Archive.org) — son artefactos de ancho fijo,
  no separadores de párrafo reales. `tagChapterHtml` primero marca los
  saltos de párrafo reales (2+ saltos de línea seguidos) con un separador
  temporal interno, colapsa el resto de los saltos de línea sueltos a un
  espacio, y recién ahí etiqueta y envuelve cada párrafo en `<p>`. Sin este
  paso, `text-align:justify` en `.dr-body` estiraría cada línea de ~70
  caracteres del original hasta el ancho completo de la columna, con
  espaciado carísimo entre palabras — el `white-space:pre-wrap` que tenía
  antes el `.dr-body` ya no hace falta ni está.
- Orden de las pasadas: primero años (`YEAR_RE`, 4 dígitos 1200-1599), después
  personas/lugares — en ese orden, para que los dígitos de `data-occ="N"`
  que se insertan después nunca puedan confundirse con un año de 4 cifras.
- `data-occ` numera las apariciones de una misma entidad dentro de un mismo
  capítulo (0-based) — es lo que permite saltar a la mención exacta desde la
  página de una persona ("Leer en contexto →").
- El etiquetado es por coincidencia de texto (nombre/alias), no desambigua
  homónimos reales.

### Responsive (mobile-first)

El sitio no tenía ningún media query hasta el 2026-08-28. Ahora hay dos
breakpoints (`max-width: 640px` y `max-width: 400px`) al final del
`<style>` que ajustan grillas a una columna, el header (la barra de
búsqueda pasa a su propia fila completa), el tamaño de fuente de
títulos, la altura del grafo/timeline, y ocultan la parte del título de
la obra en las migas de pan del lector (dejan solo "Documentos › Capítulo
N") para no saturar pantallas angostas. El input de búsqueda usa
`font-size:1rem` (16px) a propósito — por debajo de eso Safari en iOS
hace zoom automático al enfocar el campo.

**Cómo probar el responsive sin depender de que el entorno redimensione
la ventana de Chrome** (en este entorno de nube `resize_window` no
cambia el viewport real): inyectar un `<iframe>` con `style.width` fijo
(ej. 390px) apuntando al mismo archivo servido por HTTP — un iframe sí
tiene su propio viewport CSS independiente, así que los media queries
reales se disparan correctamente adentro, a diferencia de intentar
forzarlos editando el CSS del archivo (que da un resultado engañoso
porque el contenedor real sigue siendo ancho).

### Página de persona

Al hacer clic en un nombre se arma una página con "retrato" sintetizado solo
a partir de los datos del registro (rol + cuántas veces se la menciona —
explícitamente rotulado como no-biografía-externa, para no inventar datos
históricos no verificados por este corpus) y una lista de menciones
("blurbs") tomadas del texto real. Cuando una persona tiene muchas menciones
(Cortés: ~834) se muestrea parejo a lo largo de todo el texto hasta un tope
de 20 (`CAP = 20` en `buildBlurbs`), no solo las primeras — así la muestra
no queda toda en el primer capítulo.

#### Fuentes de referencia para comparar/inspirar biografías y lugares

**Personas** — https://historia-hispanica.rah.es/ — portal de la Real
Academia de la Historia que expone el *Diccionario Biográfico
electrónico* (DB-e, 2018) y el *Atlas Cronológico de la Historia de
España*: geoposiciona ~150 000 referencias, con biografías firmadas por
historiadores individuales (más de 5000 colaboradores). Cada ficha de
persona sigue la estructura Biografía → Obras → Bibliografía → Autor/es
→ Relación con otros personajes (mencionados en esta biografía /
biografías que citan a este personaje / personajes similares) → Eventos
y ubicaciones. Ejemplo consultado:
`historia-hispanica.rah.es/biografias/14401-bernal-diaz-del-castillo`
(es un SPA en Angular — el buscador en la barra superior lleva a la
ficha).

**Lugares** — Wikipedia en español (`es.wikipedia.org`) para identificar
el equivalente moderno de un topónimo (ubicación/coordenadas actuales,
municipio/estado, y a veces el origen del nombre o si se lo confunde con
otro lugar). Ejemplo ya aplicado: `place:potonchan`
(`entidades/bernal-diaz/lugares.json`) — Bernal Díaz usa "Potonchán" y
"Champotón" para el mismo sitio; el artículo
https://es.wikipedia.org/wiki/Champot%C3%B3n dio el equivalente moderno
preciso (Champotón, Campeche, con coordenadas) y explicó por qué se
confunde con una región de Tabasco también llamada Potonchán — se agregó
"Champotón"/"Champoton" como alias de la misma entrada (no una entidad
nueva) para que esas menciones también queden etiquetadas en el texto, y
la fuente y la explicación quedaron citadas en el campo `notas`.

**Cómo usarlo, en los dos casos:** como referencia para *comparar y
verificar* (cotejar fechas, alias, identidad, equivalente moderno,
ambigüedades al canonizar en `entidades/<obra>/personas.json` o
`lugares.json`) y, para personas, también como *modelo de estructura* de
una biografía completa — **nunca como fuente para copiar texto**. Es
contenido con su propia autoría (firma individual en el caso de
historia-hispanica.rah.es; licencia CC BY-SA en el caso de Wikipedia), a
diferencia de las crónicas de dominio público que arma este proyecto.
**Las descripciones que se muestran en el MVP (`synthBio`/`synthBioLugar`)
tienen que seguir siendo chicas y basadas solo en la crónica** — un
"retrato"/"descripción" de pocas líneas, no una biografía o nota
geográfica externa (por eso el disclaimer debajo de cada una); estas
fuentes externas informan campos de identificación como
`modern_equivalent`, `aliases` o `notas` en los JSON, no el texto
sintetizado que ve el usuario. Útil sobre todo al hacer la segunda
revisión de entradas `"candidata"` (ver Pendientes).

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
   validar primero la interfaz. Las cinco obras activas ya tienen una
   primera pasada (ver "Estado actual" para el detalle por obra); todas
   necesitan más capítulos/entradas/documentos — Bernal Díaz y Las Casas
   son las que más volumen tienen por delante (93 y 86 capítulos). El
   patrón para sumar una tanda: editar `entidades/<obra>/personas.json` y
   `lugares.json` (agregar entidades nuevas, `status: "candidata"`), sumar
   eventos/relaciones al final de `relaciones-muestra.json` citando
   `source:<obra>:cap-N`, **correr un chequeo de integridad referencial**
   (todo `from`/`to` de `relaciones` tiene que resolver contra
   `personas`+`lugares`+`eventos` de esa obra — ver el bug que se encontró
   y corrigió el 2026-08-28 en "Estado actual"), y volver a combinar esos
   tres archivos en el JSON embebido de `mvp/archivo-final.html`
   (reemplazando por completo las entradas con `obra: "<esa-obra>"` en
   `personas`/`lugares`/`eventos`/`relaciones`, no solo agregando, para no
   dejar entidades viejas duplicadas).
2. **Diario de Colón — decisión de narrador ya tomada**: se modeló a
   Cristóbal Colón como `person:cristobal-colon` (mismo patrón que
   `person:bernal-diaz-del-castillo`), con nota sobre la voz de Las Casas
   resumiendo. Aplicar el mismo criterio en `colon-cartas` si se retoma
   (ya se hizo ahí también, ver "Estado actual").
3. **Colón — Relaciones y cartas: dividido más grueso que el índice
   original** (10 bloques en vez de ~30 cartas/fragmentos), con ruido de
   OCR sin corregir — ver `sources/colon-cartas/METADATA.md`. Si hace
   falta más granularidad o texto más limpio, es trabajo pendiente.
4. Retomar Hernando Colón (limpieza manual o edición alternativa) cuando
   haya tiempo — no es bloqueante para lo demás.
5. Segunda revisión de las entradas marcadas `"status": "candidata"` en los
   registros de personas/lugares (ahora son la gran mayoría, en las cinco
   obras), y de las notas de ambigüedad (ej. "D Diego" en Las Casas, o la
   discrepancia de a quién nombra "Champotón" entre Bernal Díaz y la
   Primera carta de Cortés en `entidades/cortes/lugares.json`) — cotejar
   contra historia-hispanica.rah.es o Wikipedia (ver "Fuentes de
   referencia para comparar/inspirar biografías y lugares" en la sección
   del MVP) cuando haga falta resolver una ambigüedad de fechas o
   identidad.
6. **Fase 1 de las 17 obras nuevas del catálogo** (`sources/CATALOGO.md`)
   — cada una necesita el mismo tratamiento que ya se hizo para Bernal
   Díaz/Las Casas/Colón/Cortés: revisar el `raw/`, separar aparato
   editorial moderno, limpiar ruido de OCR donde haya, dividir en
   capítulos, y recién ahí armar `texto-limpio/` y sumarla al MVP. Dado
   el volumen (algunas enormes, como Oviedo con ~1.77M de palabras),
   conviene priorizar en vez de encarar todas juntas.
7. Cerrar los huecos de fuente que quedaron documentados en el catálogo:
   falta un tomo de Sahagún, la segunda parte de los Comentarios reales
   de Inca Garcilaso (*Historia general del Perú*), y la *Crónica
   mexicáyotl* de Tezozómoc (distinta de la *Crónica mexicana* ya
   conseguida).

## Convenciones a mantener

- Español neutro latinoamericano en todo contenido dirigido al usuario.
- Ids con prefijo por tipo (`person:`, `place:`, `event:`, `source:`),
  slug en minúsculas con guiones, **scoped por obra** (ver nota en "Modelo
  de datos").
- Toda relación cita su `Source` exacta (obra + capítulo).
- No sacar Hernando Colón de pausa, ni reabrir la decisión de usar
  *Historia de las Indias* en vez de la *Brevísima relación*, sin que el
  usuario lo pida explícitamente — son decisiones de alcance ya tomadas con
  él, con motivo documentado arriba. (Cortés ya no está en esta lista —
  salió de pausa el 2026-08-28, ver "Decisiones de alcance".)
