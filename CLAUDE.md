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
historiadores y escritores, publicado como sitio Jekyll de código abierto —
cada capítulo/persona/lugar es una página Markdown editable a mano, para que
alguien sin experiencia de programación pueda proponer correcciones vía
Pull Request. Idioma: español neutro latinoamericano en todo el contenido
dirigido al usuario (sitio, READMEs, METADATA).

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
- **Migración a sitio Jekyll completada (2026-08-28)**: el MVP de un
  solo archivo HTML (`mvp/archivo-final.html`) se reemplazó por un sitio
  Jekyll real — 419 páginas de capítulo, 92 de persona y 83 de lugar,
  generadas una sola vez por `scripts/generar_sitio.py` y versionadas como
  Markdown editable. Se sacó la pestaña "Red de relaciones" (el grafo de
  fuerza no se migró) y las pestañas restantes pasaron a ser la barra de
  navegación real del sitio (`Documentos`/`Personas`/`Lugares`/
  `Cronología`), no un selector de una sola página. `mvp/` se borró del
  todo (queda en el historial de git). Ver "El sitio Jekyll" más abajo
  para la arquitectura completa.
- **Cortés salió de pausa** el 2026-08-28 al conseguirse una edición
  digital (no escaneada) de las *Cartas de relación* — ver "Decisiones de
  alcance" más abajo, esto reabre una decisión previa.
- **Catálogo completo de 20 cronistas (`sources/CATALOGO.md`)**: el
  2026-08-28 el usuario dio una lista priorizada de 20 crónicas y pidió
  conseguirlas todas. Las 20 tienen ahora al menos Fase 0 (fuente
  descargada) — 17 obras nuevas quedaron en estado **"por procesar"**
  (`raw/` conseguido, Fase 1 sin empezar, sin revisión manual de calidad
  de OCR). Ninguna de las 17 está todavía en el sitio. Ver el catálogo para
  qué se consiguió de cada una, de dónde, y qué huecos quedan (obras
  parciales o ediciones distintas a la pedida).
- **Repo en GitHub y Pages publicado**: el proyecto vive en
  https://github.com/codingadrian/cronicas-de-indias (público) y el sitio se
  sirve en https://codingadrian.github.io/cronicas-de-indias/. Ver
  "GitHub / GitHub Pages" más abajo para cómo está armado el deploy.

## Estructura de carpetas

```
/historia
├── README.md                          resumen del proyecto para una persona
├── CLAUDE.md                          este archivo
├── .gitignore                         excluye sources/cortes/raw/*.pdf (supera 100 MB de GitHub)
├── .github/workflows/pages.yml        build de Jekyll + deploy a GitHub Pages
├── Gemfile                            jekyll + webrick
├── _config.yml                        config de Jekyll (collections, permalinks, defaults, exclude)
├── plan/
│   ├── plan.html                      plan del proyecto, copia local
│   └── README.md                      apunta al Artifact publicado del plan
├── schema/
│   └── entidades-relaciones.schema.json   modelo de datos (ver abajo)
├── sources/                           dato de investigación, NO se sirve (ver _config.yml exclude)
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
├── entidades/                         dato de investigación, NO se sirve (ver _config.yml exclude)
│   ├── bernal-diaz/personas.json, lugares.json, candidatos-frecuencia.json, relaciones-muestra.json
│   ├── las-casas/, colon-cartas/, cortes/, cristobal-colon/   (misma estructura)
├── scripts/
│   └── generar_sitio.py               genera todo lo de abajo a partir de sources/ + entidades/ (ver "El sitio Jekyll")
├── _documentos/<obra>/NNN.md          contenido del sitio — un capítulo por archivo, editable a mano
├── _personas/<obra>/<slug>.md         una persona por archivo
├── _lugares/<obra>/<slug>.md          un lugar por archivo
├── documentos/index.md, personas/index.md, lugares/index.md, cronologia/index.md   páginas índice
├── index.md                           portada (misma biblioteca que documentos/index.md)
├── _layouts/                          default.html, capitulo.html, persona.html, lugar.html
├── _includes/                         nav.html, footer.html
└── assets/
    ├── css/main.css
    ├── js/tag-entities.js, search.js
    └── data/<obra>.json, search-index.json   generados por scripts/generar_sitio.py
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
  (su hijo, obra distinta, en pausa). Está en el sitio como texto
  navegable y buscable.
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
única global tiene que combinarlos con `obra`, no con el id solo. El sitio
ya maneja esto (permalinks `/personas/<obra>/<slug>/`,
`/lugares/<obra>/<slug>/` — ver "El sitio Jekyll" más abajo); tenlo en
cuenta si se arma un merge global de entidades para fases futuras.

`candidatos-frecuencia.json` es la salida cruda del primer paso automático
(conteo de nombres propios de 2+ palabras) — sirve de referencia para seguir
canonizando entidades, no está pensado para mostrarse tal cual.

`relaciones-muestra.json` sigue siendo una extracción parcial, no
completa, de cada obra — cubre los Capítulos 1-8 de Bernal Díaz y solo
el Capítulo 1 de Las Casas. El campo `entidades_nuevas` dentro de cada
archivo lleva un `capitulo` por entrada para saber en qué capítulo
apareció cada una por primera vez.

## El sitio Jekyll

Sitio Jekyll multi-página (no ya un solo archivo HTML). Cuatro pestañas en
la barra de navegación real (`_includes/nav.html`): **Documentos**,
**Personas**, **Lugares**, **Cronología** — no hay "Red de relaciones", se
sacó del todo (no se migró el grafo de fuerza del viejo MVP).

**Contenido generado, no a mano**: `scripts/generar_sitio.py` lee
`sources/<obra>/texto-limpio/*.md` y `entidades/<obra>/*.json` y escribe
`_documentos/`, `_personas/`, `_lugares/`, `cronologia/index.md` y
`assets/data/*.json` — es una corrida de una sola vez (no forma parte del
build de Jekyll). **Después de correrlo, el contenido generado queda
versionado y es la fuente de verdad editable** — volver a correr el script
sobre una obra que ya tiene ediciones manuales en sus páginas las pisaría,
así que no correrlo a ciegas sobre todo el sitio una vez que haya contenido
corregido a mano.

- **División de capítulos**: cualquier línea `## Encabezado` en el
  `texto-limpio/*.md` de una obra es un límite de capítulo/página — no
  hace falta que diga "Capítulo N" (por eso "Prólogo", "Nota del
  transcriptor", "Carta a Luis de Santángel..." o "Viernes, 3 de agosto"
  son todos encabezados válidos, cada obra tiene su propia convención de
  títulos de sección).
- **Blurbs de persona/lugar pre-generados**: el script recorre los
  capítulos de la obra en orden y arma, por entidad, la lista completa de
  menciones (capítulo, `data-occ` dentro de ese capítulo, snippet con
  `<mark>` alrededor de la mención), y **muestrea parejo hasta 20** si hay
  más (`muestrear_parejo`/`CAP_BLURBS`) — no las primeras 20 nada más.
- **`date_normalized` no siempre existe** en `relaciones-muestra.json`
  (algunas obras sí lo tienen, otras solo `date_text` libre) — la
  cronología ordena por `date_normalized` cuando está, si no intenta
  sacar un año de 4 cifras de `date_text` con regex, y si tampoco eso
  aparece la entrada queda al final ("sin fecha precisa").

### Etiquetado de entidades dentro del texto (`assets/js/tag-entities.js`)

Cada página de capítulo (layout `_layouts/capitulo.html`) carga
`assets/js/tag-entities.js`, que hace `fetch('/assets/data/<obra>.json')`
(personas+lugares de esa obra, con `url` ya calculada) y etiqueta las
menciones **en el navegador**, recorriendo solo los nodos de texto del
`#dr-body` con un `TreeWalker` (no reprocesa el HTML como string, para no
romper el markup que ya generó kramdown).

- El regex usa `\b` de JavaScript normal — **no hace falta el lookaround
  `\p{L}\p{N}`** que sí llevaba el viejo MVP: acá el texto ya pasó por
  Python (`re` de Python SÍ trata las tildes como parte de `\w`/`\b` por
  default, a diferencia del `\b` de JS) para los blurbs pre-generados, y
  el JS del navegador confirmado igual de robusto con acentos en pruebas
  (`\bÁvila\b` matchea bien). Si se vuelve a tocar esta regex, probar con
  nombres acentuados antes de asumir que `\b` alcanza.
- `data-occ` numera las apariciones de una misma entidad **dentro de un
  mismo capítulo** (0-based, un contador nuevo por cada carga de página) —
  es lo que permite saltar a la mención exacta desde la página de una
  persona ("Leer en contexto →", hash `#leer-<entity_id>-<occ>`). El mismo
  número tiene que salir en el navegador y en el script de Python — están
  desacoplados pero usan la misma lógica (orden de recorrido, un contador
  por entidad que arranca en 0 en cada capítulo).
- **Los links generados necesitan el `baseurl` del sitio** (`/cronicas-de-indias`)
  — el JSON de `assets/data/<obra>.json` tiene URLs *sin* baseurl
  (`/personas/<obra>/<slug>/`), y `tag-entities.js` lo antepone leyendo
  `data-baseurl` (puesto por Liquid en `.doc-reader` en `capitulo.html`).
  Si se olvida este prefijo, los links de entidad navegan a una URL sin el
  path base del sitio y dan 404 — bug real que apareció y se corrigió
  durante la migración.
- Orden de las pasadas: primero años (`YEAR_RE`, 4 dígitos 1200-1599),
  después personas/lugares.
- El etiquetado es por coincidencia de texto (nombre/alias), no desambigua
  homónimos reales.

### Responsive (mobile-first)

Dos breakpoints (`max-width: 640px` y `max-width: 400px`) en
`assets/css/main.css` — grillas a una columna, la barra de búsqueda pasa a
su propia fila completa, tamaño de fuente de títulos. El input de búsqueda
usa `font-size:1rem` (16px) a propósito — por debajo de eso Safari en iOS
hace zoom automático al enfocar el campo.

**Cómo probar el responsive sin depender de que el entorno redimensione
la ventana de Chrome** (en este entorno de nube `resize_window` no
cambia el viewport real): inyectar un `<iframe>` con `style.width` fijo
(ej. 390px) apuntando a la misma página servida por HTTP.

### Búsqueda global (`assets/js/search.js`)

Filtra contra `assets/data/search-index.json` (generado por
`scripts/generar_sitio.py`, un objeto por capítulo con `heading`,
`obra_titulo`, `url` y **el texto completo del capítulo** en `texto`) —
importante que sea el texto completo y no solo un fragmento corto: una
versión anterior solo guardaba los primeros ~160 caracteres del capítulo
para "ahorrar espacio", y eso hacía que buscar una palabra mencionada más
adelante en el capítulo (ej. "Moctezuma"/"Montezuma") no encontrara casi
nada. El snippet mostrado en cada resultado se calcula en el momento de la
búsqueda, centrado en la posición del match dentro de `texto` (misma idea
de ventana que los blurbs de persona/lugar), no un snippet fijo.

### Página de persona/lugar

`_layouts/persona.html`/`lugar.html` arman una página con "retrato"/
"descripción" sintetizado solo a partir de los datos del registro (rol o
equivalente moderno + cuántas veces se la menciona — explícitamente
rotulado como no-biografía-externa, para no inventar datos históricos no
verificados por este corpus) y los blurbs pre-generados por
`scripts/generar_sitio.py` (ver arriba). El campo del front matter con el
id original (`person:...`/`place:...`) se llama **`entity_id`**, no `id`
— `id` es un campo reservado que Jekyll autogenera para todo documento de
colección, así que un front matter que use `id` para esto se pisa en
silencio con el valor autogenerado de Jekyll (bug real que apareció y se
corrigió en `persona.html` durante la migración).

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
**Las descripciones que se sintetizan (`bio_persona`/`bio_lugar` en
`scripts/generar_sitio.py`) tienen que seguir siendo chicas y basadas solo
en la crónica** — un
"retrato"/"descripción" de pocas líneas, no una biografía o nota
geográfica externa (por eso el disclaimer debajo de cada una); estas
fuentes externas informan campos de identificación como
`modern_equivalent`, `aliases` o `notas` en los JSON, no el texto
sintetizado que ve el usuario. Útil sobre todo al hacer la segunda
revisión de entradas `"candidata"` (ver Pendientes).

### Testing

No hay framework de pruebas automatizado en el repo. Para validar la
migración a Jekyll se corrió `jekyll build` local (revisar que no tire
warnings de Liquid — ojo, **no se puede indexar un array con un filtro
adentro de los corchetes**, `arr[idx | minus: 1]` tira "Expected
close_square but found pipe"; hay que precalcular el índice en un
`{% assign %}` aparte primero, como hace `_layouts/capitulo.html`) y
navegación real en Chrome (clic en entidad → página de persona/lugar →
"Leer en contexto →" → vuelta al capítulo con scroll+flash en la mención
exacta). **Al probar el flash de "Leer en contexto" a mano**: la clase
`.flash` se saca sola a los 1800ms (`setTimeout` en `jumpToHash` de
`tag-entities.js`) — si se revisa el DOM con una herramienta con latencia
(otro proceso, otra pestaña) es fácil llegar tarde y ver que "no
funcionó" cuando en realidad ya se sacó la clase; conviene revisar con el
timeout temporalmente alargado o mirar el resultado apenas carga la
página, no asumir que no anduvo solo porque no se ve al toque.

Si se agregan features nuevas al sitio conviene armar algo parecido a lo
anterior (jsdom, o navegación real) antes de publicar, en vez de confiar
solo en QA visual (la herramienta de captura de pantalla del navegador en
este entorno de nube es intermitente — falla y se recupera sin patrón
claro; usar JS embebido para verificar estado del DOM cuando la captura
falla).

## Cómo previsualizar el sitio fuera de este entorno

```
bundle install   # o: gem install jekyll (viene preinstalado en algunos entornos)
jekyll serve
```

Abrir `http://localhost:4000/cronicas-de-indias/`. En este entorno de nube
`bundle install` no tiene red para bajar gems — Jekyll 4.3.2 ya viene
instalado como gem del sistema, así que alcanza con `jekyll build`/
`jekyll serve` directo (sin `bundle exec`) si `bundle install` falla por
falta de red.

## GitHub / GitHub Pages (ejecutado)

Repo: https://github.com/codingadrian/cronicas-de-indias (público, rama
`main`). Pages publicado en https://codingadrian.github.io/cronicas-de-indias/.

- **`sources/cortes/raw/*.pdf` (344 MB) está en `.gitignore`** — supera el
  límite de 100 MB por archivo de GitHub. La fuente para volver a
  conseguirlo está documentada en `sources/cortes/METADATA.md`; no se perdió
  nada, solo no está versionado.
- **Deploy vía GitHub Actions** (`build_type: workflow` en la config de
  Pages del repo, no el modo Jekyll/branch por defecto), definido en
  `.github/workflows/pages.yml`: en cada push a `main` corre
  `bundle exec jekyll build` y publica `_site/`. Como sigue siendo
  `build_type: workflow` (no el Jekyll nativo/"safe mode" de Pages), no
  hay restricción de plugins si hiciera falta alguno más adelante.
- Para forzar un redeploy manual sin nuevo commit: `gh workflow run
  pages.yml --repo codingadrian/cronicas-de-indias` (el workflow tiene
  `workflow_dispatch`).

## Pendientes (en orden sugerido)

1. **Seguir la extracción de relaciones capítulo por capítulo** — es el
   trabajo de fondo que quedó pausado a pedido del usuario para primero
   validar la interfaz (primero el MVP, ahora la migración a Jekyll). Las
   cinco obras activas ya tienen una primera pasada (ver "Estado actual"
   para el detalle por obra); todas necesitan más capítulos/entradas/
   documentos — Bernal Díaz y Las Casas son las que más volumen tienen por
   delante (93 y 86 capítulos). El patrón para sumar una tanda: editar
   `entidades/<obra>/personas.json` y `lugares.json` (agregar entidades
   nuevas, `status: "candidata"`), sumar eventos/relaciones al final de
   `relaciones-muestra.json` citando `source:<obra>:cap-N`, **correr un
   chequeo de integridad referencial** (todo `from`/`to` de `relaciones`
   tiene que resolver contra `personas`+`lugares`+`eventos` de esa obra —
   ver el bug que se encontró y corrigió el 2026-08-28 en "Estado
   actual"). **Ahora que el sitio es Jekyll, hay dos formas de aplicar
   esos cambios a las páginas publicadas** (ya no hay un JSON embebido
   único que combinar): (a) si esa obra todavía no tiene páginas de
   persona/lugar editadas a mano, volver a correr
   `python3 scripts/generar_sitio.py` regenera todo desde cero (pisa
   `_documentos/`, `_personas/`, `_lugares/`, `cronologia/index.md` y
   `assets/data/*` — simple pero destructivo con ediciones manuales
   previas); (b) si ya hay contenido corregido a mano en esa obra, hay
   que aplicar el cambio a mano en las páginas afectadas (agregar el
   blurb/mención nueva, actualizar `assets/data/<obra>.json`) en vez de
   correr el script entero.
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
   "El sitio Jekyll") cuando haga falta resolver una ambigüedad de fechas
   o identidad.
6. **Fase 1 de las 17 obras nuevas del catálogo** (`sources/CATALOGO.md`)
   — cada una necesita el mismo tratamiento que ya se hizo para Bernal
   Díaz/Las Casas/Colón/Cortés: revisar el `raw/`, separar aparato
   editorial moderno, limpiar ruido de OCR donde haya, dividir en
   capítulos, y recién ahí armar `texto-limpio/`, sumar la obra a `OBRAS`
   en `scripts/generar_sitio.py`, y correr el script para sumarla al
   sitio. Dado
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
