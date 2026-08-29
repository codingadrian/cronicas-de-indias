# Crónicas de Indias — archivo del proyecto

Este directorio reúne el trabajo del proyecto **Crónicas de Indias**: un archivo relacional y consultable de las crónicas españolas de la conquista de América, pensado para historiadores y escritores, de código abierto y publicado en dominio público.

> Si vas a seguir trabajando con Claude Code en esta carpeta, leé también
> `CLAUDE.md` — tiene el contexto técnico completo (decisiones de alcance,
> modelo de datos, arquitectura del sitio, pendientes) para retomar el
> trabajo sin tener que reexplicarlo todo de nuevo.

## Cómo colaborar sin saber programar

Cada capítulo de cada crónica es un archivo de texto simple (Markdown) en
`_documentos/<obra>/NNN.md`. Para corregir una errata o mejorar una
transcripción: abrí el archivo correspondiente en GitHub (botón de lápiz
✏️ "Edit this file"), hacé el cambio, y proponé un Pull Request — no hace
falta instalar nada. Las páginas de persona (`_personas/`) y de lugar
(`_lugares/`) también son archivos de texto editables de la misma manera.

## Estado

**Sitio Jekyll publicado**, construido sobre Fase 2 (entidades y
relaciones) — Cortés y Colón-cartas ya tienen sus obras completas; las
otras tres siguen en progreso capítulo por capítulo.

Repo: https://github.com/codingadrian/cronicas-de-indias — sitio publicado en https://codingadrian.github.io/cronicas-de-indias/

- ✅ Bernal Díaz del Castillo — *Historia verdadera* (tomo 1): 63 personas y 36 lugares registrados, relaciones de los Capítulos 1-35 (de 111).
- ✅ Bartolomé de las Casas — *Historia de las Indias* (tomo II): 45 personas y 43 lugares registrados, relaciones de los Capítulos 1-28 (de 97).
- ✅ Cristóbal Colón — *Diario de a bordo del primer viaje*: 5 personas y 14 lugares registrados, relaciones del proemio + días 1-40 (de 191).
- ✅ Cristóbal Colón — *Relaciones y cartas*: **completa** — 27 personas y 18 lugares registrados, relaciones de los 10 documentos/bloques (edición de 1892, con ruido de OCR sin corregir).
- ✅ Hernán Cortés — *Cartas de relación*: **completa** — 39 personas y 29 lugares registrados, relaciones de las 5 cartas.
- ⏸️ Hernando Colón — en pausa.

**Catálogo completo de 20 cronistas** (`sources/CATALOGO.md`): a pedido
del usuario se buscaron y descargaron las 20 crónicas de una lista
priorizada. Las 5 de arriba ya están activas en el sitio; las otras 15
obras (Gómara, Oviedo, Mártir de Anglería, Cabeza de Vaca, Motolinía,
Sahagún, Durán, Acosta, Cieza de León, Zárate, Xerez, Pedro Pizarro,
Inca Garcilaso, Guamán Poma, Ixtlilxóchitl, Tezozómoc, Muñoz Camargo, y
la Brevísima relación de Las Casas) tienen el texto descargado en
`sources/<obra>/raw/` pero todavía no pasaron por limpieza ni están en
el sitio — ver el catálogo para el detalle de cada una y qué falta.

## Estructura

```
/historia
├── README.md
├── CLAUDE.md               contexto técnico para retomar el trabajo con Claude Code
├── plan/
├── schema/                 esquema de entidades y relaciones
├── sources/                textos originales y limpios, por obra (dato de investigación, no se sirve)
├── entidades/              registros de personas/lugares/relaciones por obra (dato de investigación, no se sirve)
├── scripts/
│   └── generar_sitio.py    genera _documentos/_personas/_lugares/cronología a partir de sources/ y entidades/
├── _documentos/<obra>/NNN.md   un capítulo por archivo — contenido del sitio, editable a mano
├── _personas/<obra>/<slug>.md  una persona por archivo
├── _lugares/<obra>/<slug>.md   un lugar por archivo
├── documentos/, personas/, lugares/, cronologia/   páginas índice del sitio
├── assets/                 CSS, JS de etiquetado/búsqueda, y datos JSON generados
└── _layouts/, _includes/   plantillas Jekyll
```

## Cómo se hizo esta primera pasada

1. **Etiquetado asistido**: un script de conteo de frecuencia (nombres propios de dos o más palabras) escaneó el texto completo de cada obra — sin necesidad de leerla entera a mano — para encontrar los candidatos más mencionados.
2. **Canonización**: los candidatos más frecuentes y reconocibles se convirtieron en registros de `personas.json`/`lugares.json`, resolviendo variantes ortográficas (ej. "Velazquez"/"Velázquez") en un solo id.
3. **Muestra de relaciones**: se leyó a mano el Capítulo 1 de cada obra para extraer relaciones completas (persona↔evento↔lugar↔fecha), cada una citando el capítulo de origen.
4. **Sitio Jekyll**: `scripts/generar_sitio.py` combinó los registros de entidades, la muestra de relaciones y los capítulos completos de las obras en páginas Markdown individuales (una por capítulo/persona/lugar), con etiquetado de entidades en el cliente y páginas de persona/lugar con menciones muestreadas del texto real.

## Cómo verlo localmente

```
bundle install   # o: gem install jekyll (ya viene instalado en algunos entornos)
jekyll serve
```

Después abrí `http://localhost:4000/cronicas-de-indias/`.

## Lo que falta (todavía no está hecho)

- Las relaciones siguen incompletas en tres de las cinco obras (ver el detalle arriba) — quedan 76 capítulos de Bernal Díaz, 69 de Las Casas, y ~151 entradas del Diario de Colón sin procesar (esto limita lo que se ve en la Cronología). Cortés y Colón-cartas ya están completas.
- Varias entradas quedaron con `"status": "candidata"` (pendientes de una segunda revisión) o con notas de ambigüedad (ej. "D Diego" en Las Casas podría confundirse entre dos personas distintas).
- El registro de personas/lugares se armó a partir de los candidatos más *frecuentes*; nombres mencionados pocas veces no están todavía en el registro general.

## Próximo paso

Con el sitio migrado a Jekyll, seguir extrayendo relaciones capítulo por capítulo (por tandas), priorizando los capítulos de mayor interés si hay alguno en particular.
