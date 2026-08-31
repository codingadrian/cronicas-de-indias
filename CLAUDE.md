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

## Estado actual (snapshot, actualizado 2026-08-31)

- **Fase 1 (texto limpio y dividido en capítulos) completa para 16 de
  las 17 obras del catálogo** (`sources/CATALOGO.md`), hecha en una
  tanda grande de forks paralelos el 2026-08-29. Solo **Oviedo** (4
  tomos) sigue sin Fase 1 — ver más abajo, es la obra más difícil de
  todo el catálogo. Detalle por obra (13 sin reservas relevantes, 2 con
  reservas serias de fidelidad OCR, y las obras que quedaron
  documentadamente parciales):
  - **Sin reservas — completas y confiables**: Durán (~455 000
    palabras, la más grande del proyecto — incluye un Apéndice que
    **no es de Durán**, identificado y separado, ver "Decisiones de
    alcance"), Pedro Mártir (~238 000, la traducción de Torres Asensio
    de 1892), Acosta (~171 000), López de Gómara (~170 000 —
    ~25 de 224 capítulos quedaron sin dividir por corrupción OCR
    irrecuperable; ver nota sobre la autoría de la "Vida de Hernán
    Cortés" incluida en la misma edición), Tezozómoc (~168 000),
    Cieza de León (~124 000, solo la Primera Parte, que es lo que cubre
    esta edición), Pedro Pizarro (~66 000), Ixtlilxóchitl (~101 000 —
    termina incompleta en la propia fuente, se corta a mitad de la
    entrada a Tenochtitlan), Muñoz Camargo (~63 000), Motolinía
    (~107 000), Cabeza de Vaca (~37 000), Xerez (~33 000).
  - **Parciales por huecos de fuente, documentados en cada
    `METADATA.md`**: Inca Garcilaso (~275 000 — solo la Primera Parte,
    falta la *Historia general del Perú*, que no está en esta edición),
    Sahagún (~170 000 — solo Tomo B, Libros VII-XII de 12; falta el
    Tomo A completo).
  - **Con reservas serias de fidelidad OCR — no recomendadas para Fase 2
    sin una revisión manual previa**: Zárate (~120 000 — escaneo de la
    edición original de 1555, ~25 de 130 capítulos sin separar, mucho
    texto sin reconstruir letra por letra), Guamán Poma (~154 000 — el
    peor OCR del proyecto, y **falta toda la primera mitad de la obra**:
    el "tomo1" adquirido resultó ser 100% aparato editorial moderno de
    1980, cero palabras de Guamán Poma; el "tomo2" empieza en el folio
    560 de ~1200, así que folios 1-559 —mito de creación, genealogía
    inca, la conquista, inicio del "Buen gobierno"— nunca se consiguieron).
  - **Sin empezar**: **Oviedo** (4 tomos, ~1.77M de palabras) — el peor
    OCR de todo el catálogo (peor que Guamán Poma), dos intentos de
    arrancar Fase 1 se cortaron sin escribir nada por límite de sesión.
- **Fase 2 (entidades y relaciones) completa para 15 obras** (las 5
  originales + Xerez, Cabeza de Vaca, Muñoz Camargo, Pedro Pizarro,
  Ixtlilxóchitl, Cieza de León, Tezozómoc, Motolinía, Pedro Mártir,
  Acosta) — total combinado: **566 personas, 408 lugares, 260 eventos,
  1254 relaciones** (Colón — Cartas subió de 65 a 73 relaciones y sumó
  2 lugares el 2026-08-31, ver más abajo). La cobertura por obra varía
  y está documentada
  honestamente en la `nota` de cada `relaciones-muestra.json`: algunas
  son de libro completo (Motolinía, Xerez, Cabeza de Vaca, Acosta), la
  mayoría cubre en profundidad los capítulos históricamente centrales y
  solo por título/resumen los tramos largos descriptivos o genealógicos
  (documentado por obra) — **Pedro Mártir en particular quedó con
  cobertura baja relativa a su tamaño**: de sus 80 libros en 8 décadas,
  solo un puñado se leyeron a fondo (los viajes de Colón, el cruce de
  Balboa, la caída de Tenochtitlan, la persecución de Cristóbal de Olid)
  y el resto no tiene entidades extraídas todavía.
  Quedan 4 obras del catálogo sin Fase 2 (López de Gómara, Sahagún,
  Inca Garcilaso, Durán), más Zárate y Guamán Poma (bloqueadas por
  fidelidad OCR) y Oviedo (bloqueada por Fase 1).
- **Sitio activo: 15 obras** (las 5 originales + los 8 sumados el
  2026-08-29 + Pedro Mártir y Acosta, sumados el 2026-08-31 — ver más
  abajo). KPIs reales del sitio activo (`_data/stats.yml`, mostrados en
  la barra de navegación): **15 obras, 566 personas, 408 lugares, 260
  eventos, 1254 relaciones**.
  **Bugs de integridad encontrados y corregidos en este trabajo** (vale
  la pena recordarlos si se retoma manualmente): (1) las entidades
  nuevas del Capítulo 1 de Bernal Díaz y de Las Casas se habían quedado
  solo en el log `entidades_nuevas` de `relaciones-muestra.json` sin
  copiarse nunca a `personas.json`/`lugares.json` — las relaciones
  citaban ids que no existían en el registro real. Ya están promovidas
  en ambas obras. (2) Un fork usó una relación `citado_en` persona→fuente
  en Las Casas, que no es como está pensado el esquema (`cited_in` es
  relación→fuente, y cada relación ya cita su fuente en su propio campo
  `source`) — se corrigió a `estuvo_presente_en` contra el evento
  correspondiente; el mismo error casi se repitió en la tanda de Fase 2
  de Motolinía, pero el propio fork lo detectó y lo corrigió antes de
  terminar. (3) En tandas paralelas, varios forks se cortaron a mitad de
  trabajo por límite de sesión — a veces sin escribir nada, a veces con
  los archivos ya escritos pero sin reportar (hay que revisar el estado
  real de los archivos antes de asumir que un fork "fallido" no produjo
  nada). **Antes de dar por buena una tanda nueva, correr un chequeo de
  integridad referencial** (todo `from`/`to` de `relaciones` y todo
  `place_id` de `eventos` debe resolver contra `personas` + `lugares` +
  `eventos` de esa misma obra — la única excepción es la relación
  `ocurrió_el`, cuyo `to` es un literal `Date:YYYY`, no un id de
  entidad) **y comparar el rango real de `source:...:cap-N` citado en
  `relaciones` contra lo que dice el campo `nota`**. (4) Un fork de Fase
  2 (Cieza de León) encontró que un primer filtro mecánico de notas al
  pie había borrado en silencio ~1500 palabras de narrativa real de
  Cieza (sobre la fundación de Popayán) — el filtro fusionaba una nota
  descartada con el texto real que la seguía. Otro (Pedro Pizarro) casi
  borró un pasaje históricamente importante (Valverde ante Atahualpa)
  porque contenía la frase común "en lugar de hermano", parecida a una
  fórmula editorial. **Verificar en ambas direcciones**: no solo que no
  sobrevivió contaminación editorial, sino que no se borró contenido real
  — imprimir cada eliminación no trivial antes de aceptarla.
  (5) **Ojo con ediciones críticas modernas (colección "Crónicas de
  América"/Historia 16, Biblioteca Ayacucho, etc.)**: su introducción,
  notas al pie y aparato crítico son de un editor moderno (con copyright
  propio, distinto al de la crónica original de dominio público) y deben
  excluirse por completo, no solo "separarse" como se hace con el
  aparato editorial viejo (pre-1900, ya seguro de dominio público, como
  el prólogo de 1862 de Bernal Díaz). Las notas al pie de estas
  ediciones suelen estar intercaladas página por página con el texto
  original sin repetir su número al continuar en la página siguiente —
  eso es lo que causó los bugs (3) y (4) de arriba; un filtro mecánico
  simple no alcanza, hace falta una pasada de verificación completa.
- **Migración a sitio Jekyll completada (2026-08-28)**: el MVP de un
  solo archivo HTML (`mvp/archivo-final.html`) se reemplazó por un sitio
  Jekyll real, generado una sola vez por `scripts/generar_sitio.py` y
  versionado como Markdown editable. Se sacó la pestaña "Red de
  relaciones" (el grafo de fuerza no se migró) y las pestañas restantes
  pasaron a ser la barra de navegación real del sitio (`Documentos`/
  `Personas`/`Lugares`/`Cronología`), no un selector de una sola página.
  `mvp/` se borró del todo (queda en el historial de git). Ver "El sitio
  Jekyll" más abajo para la arquitectura completa.
- **Cortés salió de pausa** el 2026-08-28 al conseguirse una edición
  digital (no escaneada) de las *Cartas de relación* — ver "Decisiones de
  alcance" más abajo, esto reabre una decisión previa.
- **Catálogo completo de 20 cronistas (`sources/CATALOGO.md`)**: el
  2026-08-28 el usuario dio una lista priorizada de 20 crónicas y pidió
  conseguirlas todas. `sources/CATALOGO.md` tiene su tabla de estado
  actualizada al 2026-08-29 (misma información que la sección de
  arriba, en formato de tabla por obra).
- **Repo en GitHub y Pages publicado**: el proyecto vive en
  https://github.com/codingadrian/cronicas-de-indias (público) y el sitio se
  sirve en https://codingadrian.github.io/cronicas-de-indias/. Ver
  "GitHub / GitHub Pages" más abajo para cómo está armado el deploy.
- **Diseño visual: fondo más claro y letra ~12.5% más grande (2026-08-29)**.
  En `assets/css/main.css`: se aclararon las paletas de `--bg`/`--surface`/
  `--surface-2`/`--surface-3` en los dos temas (claro y oscuro, ya que el
  sitio sigue la preferencia del sistema operativo sin selector manual), y
  se agregó `html{ font-size: 18px; }` (era el default de 16px del
  navegador) con `body` pasado a `font-size: 1rem` para que herede — como
  casi todo el resto del CSS ya usaba `rem`, esto escaló toda la
  tipografía del sitio junto, no solo el cuerpo del texto.
- **Bug de integridad encontrado en Colón — Cartas (2026-08-29), ver
  regla nueva en "Convenciones a mantener"**: se descubrió que
  `sources/colon-cartas/texto-limpio/relaciones-cartas-colon.md` se
  había editado repetidas veces **directamente en los archivos
  generados** (`_documentos/colon-cartas/000.md` y `_documentos/cortes/
  *.md`) en vez de en el `texto-limpio/` de origen — probablemente por
  una sesión concurrente de Claude Code trabajando en el mismo repo
  (se vio como peer session activa, `migrate-mvp-jekyll-multipage`,
  vía `ListAgents`). Esto dejó el sitio publicado con más limpieza de
  la que tenía el `texto-limpio/` real, y en un caso concreto un editor
  (humano o agente) promovió por error dos títulos de sub-documento de
  texto plano ("CARTA DEL ALMIRANTE... RAFAEL SÁNCHEZ" y "MEMORIAL")
  a encabezados `## ` reales dentro de `sources/colon-cartas/`,
  duplicando el título y subiendo el conteo de "capítulos" de 10 a 12
  — desalineando en silencio la numeración `cap-N` que ya citan las 65
  relaciones de `entidades/colon-cartas/relaciones-muestra.json`. Se
  corrigió (encabezados vueltos a texto plano, contenido regenerado
  solo para `colon-cartas` con un script puntual que reusa la lógica de
  `scripts/generar_sitio.py` sin tocar las otras 12 obras del sitio) —
  ver el historial de commits del 2026-08-29 para el detalle completo.
  **La causa raíz era editar el archivo generado en vez del de origen —
  ahora hay una regla explícita contra esto, ver "Convenciones a
  mantener".**
- **Colón — Cartas: segunda tanda de limpieza de OCR (2026-08-31,
  líneas 1-681 de `sources/colon-cartas/texto-limpio/
  relaciones-cartas-colon.md`) y remapeo completo de Fase 2.** El
  usuario limpió a mano varios títulos de sub-documento que en el OCR
  quedaban repartidos en líneas verticales sueltas (ej. "CARTA / DE /
  D. CRISTÓBAL COLON / A LOS REYES..."), lo que reveló que estaban
  fusionados con el cuerpo del capítulo anterior en vez de ser su
  propio encabezado — esto subió el conteo real de capítulos de 12 a
  **16** (`_documentos/colon-cartas/000.md`-`015.md`). Se regeneró
  acotado a esta obra (mismo patrón que el bug anterior) y se reescribió
  `entidades/colon-cartas/relaciones-muestra.json` entero: las 65
  relaciones viejas citaban `cap-0` a `cap-9` bajo la numeración de 10
  documentos que ya no existía (bug de arrastre desde la restructuración
  a 12 capítulos del 2026-08-29, nunca corregido — ver el commit
  `70dcdc4`, que ya dejó anotado este pendiente). Se remapearon a la
  numeración de 16 y se **re-verificaron contra el texto real** los
  capítulos 0-13 y el tramo ya limpio de cap-14 (hasta la línea 681):
  esto recuperó hechos que estaban escondidos en comentarios al margen
  (nota vieja de Navarrete/Las Casas) y no en el cuerpo visible, como
  que Roldán cercaba al Adelantado en la fortaleza de la Concepción
  (cap-7) o que los Reyes mandaron a Bobadilla por las quejas contra
  Colón (cap-6) — ninguno de los dos hechos estaba en las relaciones
  viejas. Se sumaron 2 lugares nuevos (`place:isla-de-la-madera`,
  `place:islas-de-cabo-verde`, escalas del tercer viaje). El tramo de
  cap-14 posterior a la línea 681 (prisión por Bobadilla, naufragio en
  Jamaica) y todo cap-15 (Testamento) se remapearon de número pero
  **no se re-verificaron contra texto** porque esa parte de la fuente
  todavía no se limpió a mano — queda marcado explícitamente en la
  `nota` del archivo y en cada relación afectada (`notas: "sin
  re-verificar..."`), pendiente para cuando se limpie el resto (ver
  "Pendientes"). Total de la obra: 65 → 73 relaciones.
- **Pedro Mártir y Acosta sumados al sitio (2026-08-31)** — resolvía el
  punto 1 de "Pendientes": se agregaron a `OBRAS` en
  `scripts/generar_sitio.py` y se corrió el generador completo. Al
  correrlo sobre las 15 obras (no solo las 2 nuevas) salieron dos
  efectos secundarios, ambos ya resueltos: (1) las 12 obras activas
  anteriores a la feature de comentarios al margen (commit `70dcdc4`)
  nunca se habían regenerado con ella, así que les faltaban los campos
  `chapter_index_padded`/`tiene_comentarios` en el front matter —
  el generador los agregó (cambio puramente aditivo, sin tocar el
  cuerpo de ningún capítulo, verificado línea por línea antes de
  commitear). (2) **`_documentos/cortes/*.md` volvió a caer en la
  misma trampa que Colón — Cartas** (ver el bug de más arriba): tiene
  limpieza de OCR aplicada directamente en los archivos generados que
  nunca se trasladó a `sources/cortes/texto-limpio/cartas-de-relacion.md`
  — correr el generador completo lo revirtió a la versión sucia sin
  querer. Se restauró con `git checkout -- _documentos/cortes` y se
  reconstruyeron a mano las 5 entradas de Cortés en
  `assets/data/search-index.json` a partir de la versión previa del
  archivo (`git show HEAD:...`), en vez de dejar que el generador las
  pisara. **Sigue pendiente pasar esa limpieza de `_documentos/cortes/`
  al `texto-limpio/` de origen** — hasta que no se haga, cualquier
  regeneración completa del sitio va a tener que repetir este mismo
  restore. `_data/stats.yml` y `README.md` actualizados a los totales
  nuevos (15 obras, 566/408/260/1254).

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
│   ├── colon-cartas/    activa  — texto-limpio/relaciones-cartas-colon.md (16 documentos, ~74k
│   │                    palabras, OCR limpiado a mano hasta la línea 681 el 2026-08-31; el resto
│   │                    sigue sin corregir palabra por palabra — ver "Estado actual")
│   ├── cortes/          activa  — texto-limpio/cartas-de-relacion.md (5 cartas, ~172k palabras) —
│   │                    OJO: `_documentos/cortes/` tiene limpieza de OCR que nunca se trasladó
│   │                    acá (ver "Estado actual", 2026-08-31)
│   ├── xerez/, cabeza-de-vaca/, munoz-camargo/, pedro-pizarro/,
│   │   ixtlilxochitl/, cieza-de-leon/, tezozomoc/, motolinia/,
│   │   pedro-martir/, acosta/
│   │                    activas — Fase 1+2 completas y sumadas al sitio (los 8 primeros el
│   │                    2026-08-29, pedro-martir y acosta el 2026-08-31)
│   ├── lopez-de-gomara/, sahagun/, inca-garcilaso/, duran/
│   │                    Fase 1 completa, Fase 2 pendiente — sahagun e inca-garcilaso
│   │                    quedaron parciales por huecos de fuente (ver "Estado actual")
│   ├── zarate/, guaman-poma/
│   │                    Fase 1 hecha pero con reservas serias de fidelidad OCR —
│   │                    no arrancar Fase 2 sin una revisión manual previa
│   ├── oviedo/          Fase 1 sin empezar — el peor OCR del catálogo, 4 tomos
│   ├── hernando-colon/  en pausa — solo raw/, sin texto-limpio/
│   └── (ver CATALOGO.md para el detalle original de cada una, con su
│        tabla de estado actualizada al 2026-08-29)
├── entidades/                         dato de investigación, NO se sirve (ver _config.yml exclude)
│   ├── bernal-diaz/personas.json, lugares.json, candidatos-frecuencia.json, relaciones-muestra.json
│   ├── las-casas/, colon-cartas/, cortes/, cristobal-colon/,
│   │   xerez/, cabeza-de-vaca/, munoz-camargo/, pedro-pizarro/,
│   │   ixtlilxochitl/, cieza-de-leon/, tezozomoc/, motolinia/,
│   │   pedro-martir/, acosta/                                (misma estructura, sin candidatos-frecuencia.json en las nuevas)
├── scripts/
│   └── generar_sitio.py               genera todo lo de abajo a partir de sources/ + entidades/ (ver "El sitio Jekyll")
├── _documentos/<obra>/NNN.md          contenido del sitio — un capítulo por archivo, editable a mano
├── _personas/<obra>/<slug>.md         una persona por archivo
├── _lugares/<obra>/<slug>.md          un lugar por archivo
├── documentos/index.md, personas/index.md, lugares/index.md   páginas índice
├── index.md                           portada — introducción al proyecto, cómo usarlo,
│                                       cómo colaborar, visión (no la biblioteca; esa vive en documentos/)
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
  palabra en su mayor parte (a diferencia de las otras cuatro obras),
  salvo las líneas 1-681 ya limpiadas a mano el 2026-08-31 — ver
  "Estado actual". Dividido más grueso que el índice original del libro
  (16 bloques, tras dos rondas de restructuración el 2026-08-29 y
  2026-08-31, en vez de ~30 cartas/fragmentos) — ver
  `sources/colon-cartas/METADATA.md` para el detalle y qué falta si se
  quiere más granularidad.
- **Durán — Apéndice: se mantuvo aunque no es de Durán.** El
  `texto-limpio/` incluye un apéndice de 9 capítulos que el propio texto
  dice que iba a escribir el editor Ramírez pero terminó encargándole a
  otra persona sin firmar — es un ensayo interpretativo sobre un códice
  jeroglífico distinto, no la crónica de Durán. Se conservó (es de 1880,
  dominio público) pero separado y rotulado como ajeno a Durán, para que
  Fase 2 no le atribuya entidades a él por error.
- **López de Gómara — autoría de la "Vida de Hernán Cortés" en duda.**
  La misma edición (Biblioteca Ayacucho 1979) trae, junto a la *Historia
  general de las Indias*, la *Vida de Hernán Cortés* que tradicionalmente
  se le atribuye a Gómara — pero una nota de archivo del propio traductor
  (excluida del cuerpo por ser aparato editorial moderno, pero conservada
  en `sources/lopez-de-gomara/METADATA.md`) sugiere que podría ser un
  manuscrito anónimo o de otro autor (posiblemente Calvet de Estrella)
  que un editor del siglo XIX encontró incompleto en el Archivo de
  Simancas. Sin resolver — importa para cómo se atribuyan las entidades
  de esa sección en Fase 2.
- **Sahagún: solo Tomo B (Libros VII-XII de 12), Fase 1 hecha con el peor
  nivel de corrupción de OCR del proyecto hasta antes de Oviedo/Zárate**
  (sustitución aleatoria de caracteres CJK por letras latinas). Falta
  conseguir el Tomo A para tener la obra completa — ver
  `sources/sahagun/METADATA.md`.
- **Inca Garcilaso: solo la Primera Parte de los *Comentarios Reales*
  (9 libros, 246 capítulos), Fase 1 completa.** Falta la *Historia
  general del Perú* (2ª parte), que no está en la edición conseguida —
  ver `sources/inca-garcilaso/METADATA.md`. Ojo: los archivos raw
  descargados como "tomo1"/"tomo2" están **al revés** respecto al tomo
  real de la edición (el archivo "tomo1" contiene el Tomo II de la
  edición, y viceversa) — ya documentado en el `texto-limpio/`, no
  volver a confundirlo.
- **Zárate: Fase 1 hecha pero NO recomendada para Fase 2 sin revisión
  manual previa.** Es un escaneo de la edición original de Amberes,
  1555 — el peor caso de fidelidad de OCR encontrado hasta Guamán
  Poma/Oviedo. ~25 de 130 capítulos (según la Tabla de Capítulos impresa
  del propio libro) no se pudieron separar de forma confiable y quedaron
  fusionados con el capítulo anterior; mucho texto no se reconstruyó
  letra por letra. Ver `sources/zarate/METADATA.md`.
- **Guamán Poma: Fase 1 hecha pero con el hueco de fuente más grave del
  catálogo, NO recomendada para Fase 2 sin resolver el hueco primero.**
  El "tomo1" adquirido resultó ser 100% aparato editorial moderno de
  1980 (cero palabras de Guamán Poma); el "tomo2" empieza en el folio
  560 de ~1200 — falta toda la primera mitad de la obra (mito de
  creación, genealogía inca, la conquista, inicio del "Buen gobierno").
  Además, el peor OCR del proyecto entre las obras que sí se pudieron
  procesar. Ver `sources/guaman-poma/METADATA.md` para los próximos
  pasos sugeridos (buscar el facsímil completo en kb.dk, o una edición
  impresa distinta que cubra la primera mitad).
- **Oviedo: todavía sin Fase 1.** 4 tomos, ~1.77M de palabras, el peor
  OCR de todo el catálogo (peor que Guamán Poma) — dos intentos de
  arrancar la limpieza se cortaron por límite de sesión sin llegar a
  escribir nada. Pendiente, ver "Pendientes" más abajo para el enfoque
  sugerido (un fork por tomo, dado el volumen).

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

`relaciones-muestra.json` sigue siendo una extracción parcial en varias
obras, no completa — ver "Estado actual" para la cobertura real de cada
una (varía mucho: de libro completo a solo los capítulos históricamente
centrales). El campo `entidades_nuevas` dentro de cada archivo lleva un
`capitulo` (o equivalente, según cómo esté dividida la obra: década/libro,
sección, etc.) por entrada para saber dónde apareció cada una por primera
vez.

## El sitio Jekyll

Sitio Jekyll multi-página (no ya un solo archivo HTML). Tres pestañas en
la barra de navegación real (`_includes/nav.html`): **Documentos**,
**Personas**, **Lugares** — no hay "Red de relaciones" (grafo de fuerza
del viejo MVP, nunca migrado) ni "Cronología" (pestaña + página
`cronologia/index.md` que sí se migró en su momento, pero se sacó del
sitio del todo el 2026-08-29 a pedido del usuario — `scripts/
generar_sitio.py` ya no la genera; los eventos siguen existiendo en
`entidades/<obra>/relaciones-muestra.json`, solo que ya no tienen una
vista propia en el sitio).

**Contenido generado, no a mano**: `scripts/generar_sitio.py` lee
`sources/<obra>/texto-limpio/*.md` y `entidades/<obra>/*.json` y escribe
`_documentos/`, `_personas/`, `_lugares/` y
`assets/data/*.json` — es una corrida de una sola vez (no forma parte del
build de Jekyll). **Después de correrlo, el contenido generado queda
versionado y es la fuente de verdad editable** — volver a correr el script
sobre una obra que ya tiene ediciones manuales en sus páginas las pisaría,
así que no correrlo a ciegas sobre todo el sitio una vez que haya contenido
corregido a mano.

**Esto último es para una corrección puntual de un colaborador externo
vía Pull Request** (ver README.md), que en la práctica no va a volver a
correr el generador para esa obra. **Para trabajo de Claude Code/un
agente arreglando texto de una crónica, la regla es la contraria: editar
siempre `sources/<obra>/texto-limpio/*.md`, nunca `_documentos/`
directamente** — ver la regla dura en "Convenciones a mantener" y el bug
real de Colón — Cartas en "Estado actual" que salió de romper esta
distinción (una corrección se hizo directo en `_documentos/`, no en el
`texto-limpio/` de origen, y quedó desincronizada).

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
  (algunas obras sí lo tienen, otras solo `date_text` libre) — sigue
  siendo un campo del esquema de eventos aunque el sitio ya no tiene una
  vista de cronología que lo consuma (ver "El sitio Jekyll" más arriba,
  pestaña Cronología sacada del sitio el 2026-08-29).

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

1. **Trasladar a `sources/cortes/texto-limpio/cartas-de-relacion.md` la
   limpieza de OCR que hoy solo vive en `_documentos/cortes/*.md`** —
   ver "Estado actual" (2026-08-31). Mientras no se haga, cualquier
   regeneración completa del sitio (`python3 scripts/generar_sitio.py`
   sin acotar a una obra) va a revertir esas páginas a la versión sucia
   y hay que acordarse de restaurarlas con `git checkout --
   _documentos/cortes` y reconstruir a mano sus 5 entradas en
   `assets/data/search-index.json` después de correrlo. **Antes de
   correr el generador completo en general**: `git status` para ver si
   alguna obra activa tiene `_documentos/` editado a mano por fuera de
   su `texto-limpio/` (mismo patrón que ya pasó con Colón — Cartas el
   2026-08-29, y con Cortés dos veces — el 2026-08-29 y de nuevo el
   2026-08-31, porque la primera vez nunca se trasladó la limpieza al
   `texto-limpio/`); si las hay y no coinciden, restaurarlas después con
   `git checkout -- <archivos>`.
2. **Re-verificar el resto de Colón — Cartas contra texto limpio**:
   el tramo de cap-14 posterior a la línea 681 (prisión de Colón por
   Bobadilla, naufragio en Jamaica) y todo cap-15 (Testamento) todavía
   citan hechos extraídos antes de esta última limpieza, sin
   confirmarlos contra el texto ya corregido — están marcados
   explícitamente en `entidades/colon-cartas/relaciones-muestra.json`
   (campo `notas: "sin re-verificar..."` en cada relación afectada, y
   en la `nota` general del archivo). Hacerlo en cuanto se limpie más
   OCR de esa obra (ver punto 8 de abajo).
3. **Fase 2 de las 4 obras que ya tienen Fase 1 limpia y sin reservas**:
   López de Gómara, Sahagún (parcial, Tomo B), Inca Garcilaso (parcial,
   Primera Parte), Durán. Mismo patrón que las 10 obras ya hechas: crear
   `entidades/<obra>/personas.json`+`lugares.json`+
   `relaciones-muestra.json` siguiendo el esquema, citando
   `source:<obra>:<lo que corresponda>` (capítulo, o década/libro, o
   sección según cómo esté dividida cada obra — ver el `nota` de cada
   `texto-limpio/*.md` para la convención usada), **correr el chequeo de
   integridad referencial** de siempre, y evitar los dos bugs ya
   encontrados: (a) nunca `citada_en` persona→fuente (ver "Estado
   actual"), (b) verificar en ambas direcciones que un filtro no haya
   borrado contenido real, no solo que no sobrevivió aparato editorial.
   Dado el volumen de Durán (~455 000 palabras) y Pedro Mártir ya mostró
   que la cobertura puede quedar muy desigual en obras enormes, conviene
   pedir explícitamente cobertura completa si importa, o aceptar de
   entrada que quedará parcial y documentarlo bien en la `nota`.
4. **Revisión manual de Zárate y Guamán Poma antes de su Fase 2** — ambas
   tienen reservas serias de fidelidad OCR (ver "Decisiones de alcance"
   y "Estado actual"). Arrancar Fase 2 sobre texto con tanto ruido
   produciría entidades erróneas o duplicadas por nombres propios mal
   reconstruidos. Guamán Poma además tiene un hueco de fuente que
   conviene resolver antes (falta la primera mitad de la obra — ver
   `sources/guaman-poma/METADATA.md` para dónde buscarla).
5. **Fase 1 de Oviedo** (4 tomos, ~1.77M de palabras) — la obra más
   difícil del catálogo: el peor OCR encontrado (peor que Guamán Poma),
   y el volumen es mayor que todo lo demás procesado junto. Encarar un
   fork por tomo en paralelo, no de a uno (dos intentos anteriores se
   cortaron por límite de sesión sin escribir nada); dar instrucciones
   explícitas de no inventar texto donde el OCR sea irreconstruible
   (documentar como incierto en vez de adivinar, mismo criterio que se
   usó en Zárate).
6. Segunda revisión de las entradas marcadas `"status": "candidata"` en
   los registros de personas/lugares — ahora son prácticamente todas, en
   las 15 obras con Fase 2. Casos de ambigüedad de nombre ya detectados
   y con `notas` cruzadas a resolver: "Diego Colón" en Las Casas
   (`person:diego-colon-hermano`/`diego-colon-hijo`/
   `diego-colon-indio-guanahani`, el sitio no desambigua homónimos al
   etiquetar texto), "Huitzilihuitzin" en Ixtlilxóchitl (un tlatoani y,
   por separado, el tutor de Nezahualcóyotl), y "Manco Cápac"/"Manco Inca
   Yupanqui" en Acosta. También la discrepancia de a quién nombra
   "Champotón" entre Bernal Díaz y la Primera carta de Cortés en
   `entidades/cortes/lugares.json`. Cotejar contra
   historia-hispanica.rah.es o Wikipedia (ver "Fuentes de referencia
   para comparar/inspirar biografías y lugares" en "El sitio Jekyll")
   cuando haga falta resolver una ambigüedad de fechas o identidad.
7. **Diario de Colón, Bernal Díaz, y Las Casas siguen con Fase 2
   incompleta** desde antes de esta tanda — quedan 76 capítulos de
   Bernal Díaz (de 111), 69 de Las Casas (de 97), y 151 días del Diario
   de Colón (de 191) sin procesar. Mismo patrón de siempre para sumar
   una tanda (ver el punto 3 de arriba).
8. **Colón — Relaciones y cartas: seguir limpiando el OCR más allá de la
   línea 681** de `sources/colon-cartas/texto-limpio/
   relaciones-cartas-colon.md` (el resto de cap-14 — prisión por
   Bobadilla, naufragio en Jamaica — y todo cap-15, Testamento) y, una
   vez limpio, re-verificar sus relaciones (ver el punto 2 de arriba).
   También dividido más grueso que el índice original del libro (16
   bloques en vez de ~30 cartas/fragmentos) — ver
   `sources/colon-cartas/METADATA.md`. Si hace falta más granularidad,
   es trabajo pendiente aparte.
9. Retomar Hernando Colón (limpieza manual o edición alternativa) cuando
   haya tiempo — no es bloqueante para lo demás.
10. Cerrar los huecos de fuente que quedaron documentados en el catálogo:
   Tomo A de Sahagún, primera mitad de Guamán Poma, la segunda parte de
   los Comentarios reales de Inca Garcilaso (*Historia general del
   Perú*), y la *Crónica mexicáyotl* de Tezozómoc (distinta de la
   *Crónica mexicana* ya conseguida).

## Convenciones a mantener

- Español neutro latinoamericano en todo contenido dirigido al usuario.
- Ids con prefijo por tipo (`person:`, `place:`, `event:`, `source:`),
  slug en minúsculas con guiones, **scoped por obra** (ver nota en "Modelo
  de datos").
- Toda relación cita su `Source` exacta (obra + capítulo).
- **Regla dura: el texto de una crónica solo se corrige dentro de
  `sources/<obra>/texto-limpio/*.md`. Nunca editar directamente
  `_documentos/`, `_personas/`, `_lugares/`, ni `assets/data/*.json`.**
  Esos son contenido *generado* por `scripts/generar_sitio.py` a partir
  de `sources/` + `entidades/` — una corrección hecha ahí directamente
  queda desincronizada del origen y se pierde (silenciosamente, sin
  error) la próxima vez que alguien regenere esa obra, porque el
  generador sobreescribe esos archivos sin mirar si tienen ediciones
  manuales encima. Esto ya pasó de verdad — ver "Estado actual", el bug
  de integridad de Colón — Cartas del 2026-08-29, causado exactamente
  por esto. Si hace falta corregir una errata que ya está publicada:
  corregir `sources/<obra>/texto-limpio/*.md` y volver a generar (para
  una sola obra sin tocar las demás, ver "El sitio Jekyll"/"Pendientes"
  para el patrón de regeneración acotada por obra). **Esta regla es solo
  para el texto de la crónica** — `entidades/<obra>/*.json` sí se edita
  directamente a mano o por agente, ese es su diseño (es dato de
  investigación fuente, igual que `sources/`, no contenido generado).
- **Aparato editorial: el criterio es la fecha del editor, no si "molesta".**
  Aparato editorial viejo (pre-1900, ya seguro de dominio público — un
  prólogo de 1862, una introducción de 1875) se conserva, separado en su
  propia sección, igual que el texto de la crónica misma. Aparato
  editorial moderno (siglo XX/XXI, con copyright propio distinto al de la
  crónica — introducciones, notas al pie y bibliografías de ediciones
  críticas como "Crónicas de América"/Historia 16 o Biblioteca Ayacucho)
  se **excluye por completo** de `texto-limpio/`, no se resume ni se
  conserva de ninguna forma. Ver "Estado actual" para los bugs de
  integridad que salieron de aplicar mal este criterio (notas al pie
  intercaladas sin repetir número de página en página, que un filtro
  mecánico simple no detecta).
- No sacar Hernando Colón de pausa, ni reabrir la decisión de usar
  *Historia de las Indias* en vez de la *Brevísima relación*, sin que el
  usuario lo pida explícitamente — son decisiones de alcance ya tomadas con
  él, con motivo documentado arriba. (Cortés ya no está en esta lista —
  salió de pausa el 2026-08-28, ver "Decisiones de alcance".)
