---
titulo: "Relaciones y cartas de Cristóbal Colón (cartas y documentos)"
autor: "Cristóbal Colón"
escrito: "1493-1506"
teatro: "Castilla, primer al cuarto viaje"
estado_licencia: "dominio público"
estado_texto: "parcial — 10 documentos limpios de marcadores de página; texto todavía con ruido de OCR palabra por palabra (ver abajo)"
---

# Relaciones y cartas de Cristóbal Colón

Antología de cartas, instrucciones y documentos de Colón — distinto del
Diario de a bordo (ver `../cristobal-colon/`). Edición: *Biblioteca
Clásica*, tomo CLXIV (Madrid, 1892), preparada por Martín Fernández de
Navarrete.

## Por qué es una carpeta separada de `cristobal-colon/`

Es otra obra del mismo autor (cartas y documentos oficiales, no el
diario de a bordo). Se usa `colon-cartas` para no mezclarla con
`cristobal-colon/` (el Diario).

## Duplicado evitado: la Relación del primer viaje

Esta edición de 1892 **también incluye la Relación del primer viaje**
(el mismo Diario, con las notas de Navarrete) — es el mismo texto base
que ya está en `sources/cristobal-colon/` (vía Wikisource). Se excluyó
esa sección de `texto-limpio/` para no duplicar contenido en el MVP. El
`raw/` completo sí la conserva (está en el archivo descargado tal cual),
por si en el futuro interesa cotejar las notas de Navarrete.

## Texto listo (Fase 1) — calidad y alcance

`texto-limpio/relaciones-cartas-colon.md` — 10 documentos/cartas
(~74 500 palabras): Carta a Luis de Santángel, Instrucción a Pedro
Margarit, cartas a los Reyes y a su hermano Bartolomé, carta al obispo
de Badajoz, institución de mayorazgo, cartas y salvoconducto a
Francisco Roldán, la Relación del tercer viaje junto con los documentos
del cuarto viaje y años finales (agrupados en un solo bloque — ver
nota de alcance abajo), y el testamento/codicilo final.

**Dos limitaciones a tener en cuenta:**

1. **Ruido de OCR sin corregir.** A diferencia de Bernal Díaz/Las
   Casas (Project Gutenberg) y el Diario de Colón (Wikisource), esta es
   una fuente escaneada de 1892 sin transcripción manual — el archivo
   original tiene errores de OCR palabra por palabra (ej. "Hiimboldt"
   por "Humboldt", "dol" por "del") que **no se corrigieron uno por
   uno**. Se limpiaron solo los marcadores de página/encabezados
   repetidos, no cada palabra mal reconocida.
2. **División más gruesa que el índice original.** El libro real separa
   ~30 cartas y fragmentos distintos (ver el índice completo en
   `raw/`); acá se agruparon en 10 bloques para tener límites de
   sección verificables con confianza razonable en el tiempo
   disponible. El bloque **"Relación del tercer viaje y documentos
   posteriores (1498-1504)"** en particular junta de hecho ~15 cartas y
   fragmentos distintos del índice (profecías, carta a Su Santidad,
   cartas a Nicolao Oderigo, a fray Gaspar Gorricio, a Nicolás de
   Ovando, a su hijo Diego, etc.) sin subdividir. Separarlo más fino es
   trabajo pendiente si hace falta esa granularidad.

## Fuente original

`raw/relaciones-cartas-archive-org.txt` — vía Archive.org:
https://archive.org/stream/BRes140146/BRes140146_djvu.txt

## Pendiente

- Fase 2 (personas, lugares, relaciones) — todavía no empezó.
- Si hace falta, subdividir más fino el bloque grande del tercer/cuarto
  viaje usando el índice completo (está en las primeras ~180 líneas de
  `raw/`).
