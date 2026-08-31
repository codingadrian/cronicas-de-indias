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

## Estado (actualizado 2026-08-31)

**Sitio Jekyll publicado, 15 obras activas.** KPIs actuales: 15 obras,
566 personas, 408 lugares, 260 eventos, 1254 relaciones.

Repo: https://github.com/codingadrian/cronicas-de-indias — sitio publicado en https://codingadrian.github.io/cronicas-de-indias/

- ✅ Bernal Díaz del Castillo — *Historia verdadera* (tomo 1): relaciones de los Capítulos 1-35 (de 111).
- ✅ Bartolomé de las Casas — *Historia de las Indias* (tomo II): relaciones de los Capítulos 1-28 (de 97).
- ✅ Cristóbal Colón — *Diario de a bordo del primer viaje*: relaciones del proemio + días 1-40 (de 191).
- ✅ Cristóbal Colón — *Relaciones y cartas*: relaciones de los Capítulos 0-15 (de 16, el último con relaciones pendientes de re-verificar).
- ✅ Hernán Cortés — *Cartas de relación*: **completa**.
- ✅ Francisco de Xerez, Álvar Núñez Cabeza de Vaca, Diego Muñoz Camargo, Pedro Pizarro, Fernando de Alva Ixtlilxóchitl, Pedro Cieza de León (Primera Parte), Hernando Alvarado Tezozómoc, Fray Toribio de Benavente "Motolinía" — sumadas al sitio el 2026-08-29, todas **completas** salvo donde su propia fuente está incompleta (Ixtlilxóchitl se corta a mitad de la conquista; Cieza de León es solo su Primera Parte).
- ✅ Pedro Mártir de Anglería y José de Acosta — sumadas al sitio el 2026-08-31.
- ⏸️ Hernando Colón — en pausa.

**Catálogo completo de 20 cronistas** (`sources/CATALOGO.md`): a pedido
del usuario se buscaron y descargaron las 20 crónicas de una lista
priorizada. De las 17 obras nuevas, **16 ya tienen su texto limpio y
dividido en capítulos** (Fase 1) — solo Oviedo (4 tomos, ~1.77M
palabras, el peor caso de OCR del catálogo) sigue sin empezar. Dos de
las 16 (Zárate y Guamán Poma) quedaron con reservas serias de fidelidad
de OCR y no se recomienda avanzarlas a Fase 2 sin una revisión manual
antes — ver el catálogo y `CLAUDE.md` para el detalle de cada una,
incluidos los huecos de fuente que quedan (falta un tomo de Sahagún, la
primera mitad de Guamán Poma, la segunda parte de los Comentarios
reales de Inca Garcilaso, y la *Crónica mexicáyotl* de Tezozómoc).

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
│   └── generar_sitio.py    genera _documentos/_personas/_lugares a partir de sources/ y entidades/
├── _documentos/<obra>/NNN.md   un capítulo por archivo — contenido del sitio, editable a mano
├── _personas/<obra>/<slug>.md  una persona por archivo
├── _lugares/<obra>/<slug>.md   un lugar por archivo
├── documentos/, personas/, lugares/   páginas índice del sitio
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

- Las relaciones siguen incompletas en Bernal Díaz (76 de 111 capítulos), Las Casas (69 de 97), y el Diario de Colón (151 de 191 días) — trabajo de antes de esta tanda. Varias de las obras nuevas también quedaron con cobertura parcial en obras muy largas (ver `CLAUDE.md`, especialmente Pedro Mártir).
- Pedro Mártir y Acosta tienen Fase 2 completa pero todavía no están sumados al sitio.
- Zárate, Guamán Poma, y Oviedo necesitan trabajo antes de poder avanzar a Fase 2 (ver arriba).
- Casi todas las entradas siguen con `"status": "candidata"` (pendientes de una segunda revisión), y hay varias notas de ambigüedad de nombre sin resolver (ver `CLAUDE.md`, sección "Pendientes").

## Próximo paso

Ver `CLAUDE.md`, sección "Pendientes", para el orden sugerido completo.
