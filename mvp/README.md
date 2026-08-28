# Crónicas de Indias — archivo del proyecto

Este directorio reúne el trabajo del proyecto **Crónicas de Indias**: un archivo relacional y consultable de las crónicas españolas de la conquista de América, pensado para historiadores y publicado en dominio público.

## Estado

**MVP piloto publicado** — construido sobre la primera pasada de Fase 2 (entidades y relaciones) de las dos obras activas, para validar el modelo y la experiencia de uso antes de seguir capítulo por capítulo.

- ✅ Bernal Díaz del Castillo — *Historia verdadera* (tomo 1): 24 personas y 10 lugares registrados, muestra completa de relaciones del Capítulo 1.
- ✅ Bartolomé de las Casas — *Historia de las Indias* (tomo II): 16 personas y 13 lugares registrados, muestra completa de relaciones del Capítulo 1.
- ⏸️ Hernando Colón — en pausa.
- ⏸️ Hernán Cortés — en pausa.

## MVP

`mvp/archivo-final.html` — una sola página autocontenida (sin dependencias externas) publicada como artefacto:
https://claude.ai/code/artifact/1f4b9b79-bc9d-42c8-aa56-b4bdfd7c3dfd

Cinco vistas:
- **Documentos** — las dos obras completas, capítulo a capítulo, en su texto limpio y sin alterar. Dentro del texto, los nombres de personas, los lugares y los años están resaltados como enlaces:
  - Clic en una **persona** → abre su página: retrato breve construido a partir de cómo la crónica la presenta (rol, cuántas veces se la menciona), y una lista de menciones a lo largo del texto (muestreadas de forma pareja cuando son muchas, ej. Cortés con ~834), cada una con un enlace "Leer en contexto →" que vuelve al texto principal, en el capítulo exacto, con esa mención resaltada — así se puede seguir leyendo desde ahí.
  - Clic en un **lugar** → salta a su ficha en la pestaña Lugares.
  - Clic en un **año** → salta a Cronología si hay un evento registrado para ese año.
  - La búsqueda de texto libre (barra superior) sigue funcionando igual que antes, ahora dentro de esta misma pestaña.
- **Personas** — 40 fichas (registro canónico + alias + rol), filtrables por obra; cada ficha también abre la página de la persona.
- **Lugares** — mapa (proyección equirectangular propia, sin dependencias externas) con los lugares con coordenadas conocidas.
- **Cronología** — línea de tiempo de los eventos con fecha, más una lista aparte de eventos sin fecha exacta.
- **Red de relaciones** — grafo de fuerza (nodos arrastrables) sobre la muestra de relaciones del Capítulo 1 de cada obra.

**Qué valida:** que el modelo de datos (personas/lugares/eventos/fuentes + relaciones) funciona de punta a punta —desde el texto limpio hasta una interfaz consultable, visual y navegable por entidades— con datos reales, aunque parciales.

**Qué NO cubre todavía:** el mapa, la cronología y el grafo solo tienen datos del Capítulo 1 de cada obra (la única muestra de relaciones hecha hasta ahora); el texto completo, la búsqueda y las fichas de personas/lugares sí cubren los 208 capítulos. El etiquetado de personas/lugares/años dentro del texto es por coincidencia de nombre y alias (no desambigua homónimos), y los "retratos" de las páginas de persona se arman solo con lo que hay en el registro de esa obra — no son biografías históricas externas, están señalados como tales en la página.

### Revisión de código

Antes de publicar la primera versión se revisó el JavaScript de las cinco vistas y se corrigió un error real: el grafo de "Red de relaciones" volvía a registrar los mismos escuchadores de eventos de arrastre (`pointermove`/`pointerup`/`pointerleave`) en cada redibujado, lo que iba acumulando escuchadores duplicados en cada movimiento durante un arrastre y degradaba el rendimiento cuanto más se arrastraba un nodo. Se corrigió registrando esos escuchadores una sola vez al inicializar el grafo.

Para la vista Documentos y las páginas de persona se armó una batería de pruebas automatizadas (jsdom, fuera del navegador) que ejercita clics reales sobre la página publicada: abrir una obra, entrar a un capítulo, verificar que personas/lugares/años quedan etiquetados y numerados correctamente, abrir la página de una persona de alta frecuencia (Cortés, ~834 menciones) y confirmar que el muestreo de menciones se arma rápido y sin errores, saltar a "Leer en contexto" y confirmar que resalta la mención correcta, saltar a un lugar compartido entre las dos obras (Cuba) y confirmar que resuelve a la ficha de la obra correcta, y volver con el botón "Volver". Las 33 verificaciones pasaron; además se revisó visualmente en el navegador.

## Estructura

```
/historia
├── README.md
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
└── mvp/                     ← nuevo
    ├── README.md
    └── archivo-final.html   MVP autocontenido (también publicado como artefacto)
```

## Cómo se hizo esta primera pasada

1. **Etiquetado asistido**: un script de conteo de frecuencia (nombres propios de dos o más palabras) escaneó el texto completo de cada obra — sin necesidad de leerla entera a mano — para encontrar los candidatos más mencionados.
2. **Canonización**: los candidatos más frecuentes y reconocibles se convirtieron en registros de `personas.json`/`lugares.json`, resolviendo variantes ortográficas (ej. "Velazquez"/"Velázquez") en un solo id.
3. **Muestra de relaciones**: se leyó a mano el Capítulo 1 de cada obra para extraer relaciones completas (persona↔evento↔lugar↔fecha), cada una citando el capítulo de origen.
4. **MVP**: se combinaron los registros de entidades, la muestra de relaciones y los 208 capítulos completos en una sola página consultable, para validar el modelo antes de seguir extrayendo relaciones.

## Lo que falta (todavía no está hecho)

- Las relaciones solo están hechas para el Capítulo 1 de cada obra — quedan 110 capítulos de Bernal Díaz y 96 de Las Casas sin relaciones extraídas (esto limita lo que se ve en Cronología y Red de relaciones).
- Varias entradas quedaron con `"status": "candidata"` (pendientes de una segunda revisión) o con notas de ambigüedad (ej. "D Diego" en Las Casas podría confundirse entre dos personas distintas).
- El registro de personas/lugares se armó a partir de los candidatos más *frecuentes*; nombres mencionados pocas veces no están todavía en el registro general.
- Varias coordenadas de lugares son aproximadas (marcadas como tal en el mapa con borde punteado).

## Próximo paso

Con el MVP validado, seguir extrayendo relaciones capítulo por capítulo (por tandas), priorizando los capítulos de mayor interés si hay alguno en particular — cada tanda nueva se refleja directamente en el mapa, la cronología y el grafo del MVP.
