# Crónicas de Indias — archivo del proyecto

Este directorio reúne el trabajo del proyecto **Crónicas de Indias**: un archivo relacional y consultable de las crónicas españolas de la conquista de América, pensado para historiadores y publicado en dominio público.

> Si vas a seguir trabajando con Claude Code en esta carpeta, leé también
> `CLAUDE.md` — tiene el contexto técnico completo (decisiones de alcance,
> modelo de datos, arquitectura del MVP, pendientes) para retomar el
> trabajo sin tener que reexplicarlo todo de nuevo.

## Estado

**MVP piloto publicado** (ver `mvp/README.md`), construido sobre la primera pasada de Fase 2 (entidades y relaciones) de las dos obras activas. La extracción de relaciones sigue pendiente para el resto de los capítulos.

Repo: https://github.com/codingadrian/cronicas-de-indias — sitio publicado en https://codingadrian.github.io/cronicas-de-indias/

- ✅ Bernal Díaz del Castillo — *Historia verdadera* (tomo 1): 31 personas y 18 lugares registrados, relaciones de los Capítulos 1-8.
- ✅ Bartolomé de las Casas — *Historia de las Indias* (tomo II): 16 personas y 13 lugares registrados, relaciones del Capítulo 1.
- ✅ Cristóbal Colón — *Diario de a bordo del primer viaje*: texto completo y navegable (proemio + 191 entradas por día); todavía sin personas/lugares/relaciones curados.
- ✅ Cristóbal Colón — *Relaciones y cartas*: 10 cartas y documentos navegables (edición de 1892, con ruido de OCR sin corregir); todavía sin personas/lugares/relaciones curados.
- ✅ Hernán Cortés — *Cartas de relación*: las 5 cartas completas y navegables; recién salió de pausa al conseguirse una edición digital; todavía sin personas/lugares/relaciones curados.
- ⏸️ Hernando Colón — en pausa.

**Catálogo completo de 20 cronistas** (`sources/CATALOGO.md`): a pedido
del usuario se buscaron y descargaron las 20 crónicas de una lista
priorizada. Las 5 de arriba ya están activas en el MVP; las otras 15
obras (Gómara, Oviedo, Mártir de Anglería, Cabeza de Vaca, Motolinía,
Sahagún, Durán, Acosta, Cieza de León, Zárate, Xerez, Pedro Pizarro,
Inca Garcilaso, Guamán Poma, Ixtlilxóchitl, Tezozómoc, Muñoz Camargo, y
la Brevísima relación de Las Casas) tienen el texto descargado en
`sources/<obra>/raw/` pero todavía no pasaron por limpieza ni están en
el MVP — ver el catálogo para el detalle de cada una y qué falta.

## Estructura

```
/historia
├── README.md
├── CLAUDE.md               contexto técnico para retomar el trabajo con Claude Code
├── plan/
├── schema/                 esquema de entidades y relaciones
├── sources/                textos originales y limpios, por obra
├── entidades/
│   ├── bernal-diaz/
│   │   ├── personas.json           registro canónico (nombre, alias, rol)
│   │   ├── lugares.json            registro canónico
│   │   ├── candidatos-frecuencia.json   salida cruda del primer paso automático (conteo de menciones)
│   │   └── relaciones-muestra.json      relaciones extraídas a mano del Capítulo 1, con cita a la fuente
│   └── las-casas/           (misma estructura)
└── mvp/                     ver mvp/README.md para el detalle
    ├── README.md
    └── archivo-final.html   MVP autocontenido (también publicado como artefacto)
```

## Cómo se hizo esta primera pasada

1. **Etiquetado asistido**: un script de conteo de frecuencia (nombres propios de dos o más palabras) escaneó el texto completo de cada obra — sin necesidad de leerla entera a mano — para encontrar los candidatos más mencionados.
2. **Canonización**: los candidatos más frecuentes y reconocibles se convirtieron en registros de `personas.json`/`lugares.json`, resolviendo variantes ortográficas (ej. "Velazquez"/"Velázquez") en un solo id.
3. **Muestra de relaciones**: se leyó a mano el Capítulo 1 de cada obra para extraer relaciones completas (persona↔evento↔lugar↔fecha), cada una citando el capítulo de origen.
4. **MVP**: se combinaron los registros de entidades, la muestra de relaciones y los capítulos completos de las obras en una sola página consultable (`mvp/archivo-final.html`), con navegación por documento y páginas de persona, para validar el modelo antes de seguir extrayendo relaciones.

## Lo que falta (todavía no está hecho)

- Las relaciones están hechas para los Capítulos 1-8 de Bernal Díaz y el Capítulo 1 de Las Casas — quedan 103 capítulos de Bernal Díaz y 96 de Las Casas sin relaciones extraídas (esto limita lo que se ve en la Cronología y la Red de relaciones del MVP).
- Varias entradas quedaron con `"status": "candidata"` (pendientes de una segunda revisión) o con notas de ambigüedad (ej. "D Diego" en Las Casas podría confundirse entre dos personas distintas).
- El registro de personas/lugares se armó a partir de los candidatos más *frecuentes*; nombres mencionados pocas veces no están todavía en el registro general.

## Próximo paso

Con el MVP validado, seguir extrayendo relaciones capítulo por capítulo (por tandas), priorizando los capítulos de mayor interés si hay alguno en particular.
