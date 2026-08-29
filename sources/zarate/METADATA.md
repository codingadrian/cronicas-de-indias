---
titulo: "Historia del descubrimiento y conquista del Perú"
autor: "Agustín de Zárate"
escrito: "1555"
teatro: "Conquista del Perú"
estado_licencia: "dominio público"
estado_texto: "parcial — Fase 1 hecha con reservas importantes de fidelidad OCR (ver nota abajo); no recomendado para Fase 2 sin una revisión manual previa"
---

# Historia del descubrimiento y conquista del Perú

## Texto listo (Fase 1, con reservas)

`texto-limpio/historia-descubrimiento-conquista-peru.md` — 7 libros,
111 capítulos (más una sección inicial de portada/privilegio real/
epístola dedicatoria), ~119 300 palabras. Edición: la **original de
Amberes, 1555** (Martín Nucio), vía un escaneo de la Biblioteca
Nacional de España en Archive.org — no es una edición crítica moderna,
así que no hay aparato editorial del siglo XX que excluir.

**Este es el caso de OCR más degradado de todo el proyecto hasta
ahora**, muy por encima de bernal-diaz/las-casas/xerez/muñoz-camargo/
motolinia/cabeza-de-vaca (todas Fase 1 ya completas). Al ser tipografía
del siglo XVI (letra ſ larga confundida con f, ligaduras, abreviaturas,
u/v e i/j intercambiados según convención de época), el texto OCR
tiene una tasa de error mucho más alta que un escaneo moderno mal
hecho:

- **Estructura (libros y capítulos): reconstruida con confianza
  razonable pero incompleta.** Se usó la "Tabla de los Capítulos" que
  el propio impreso trae al final (cerca de la línea 21258 del raw) como
  referencia — según esa tabla la obra tiene 130 capítulos repartidos en
  7 libros (15/13/13/22/35/19/13). De esos 130 encabezados, se
  localizaron con confianza 105 en el cuerpo del texto mediante un
  patrón "CAP." + numeral romano con un límite de párrafo en blanco
  inmediatamente antes (para no confundirlos con menciones de
  "capitán"/"capitulación" en medio de una frase). Los ~25 restantes
  — concentrados sobre todo en el Libro I (solo 9 de 15 capítulos
  localizados) y el Libro VI (14 de 19) — no se intentaron adivinar:
  su contenido quedó fusionado dentro del capítulo detectado
  inmediatamente anterior, así que el texto sigue completo, solo que
  con menos granularidad de la ideal en esos dos libros. La numeración
  de capítulos en `texto-limpio/` es secuencial por libro (Capítulo 1,
  2, 3...), no un intento de reproducir los numerales romanos
  originales (que además están frecuentemente ilegibles en el OCR).
- **Limpieza mecánica hecha**: se removió el boilerplate de escaneo
  ("© Biblioteca Nacional de España", repetido cientos de veces), los
  encabezados de página corridos ("LIBRO I. DE LA...", "HISTORIA DEL
  PERV" alternando por página), líneas de solo número de folio, y se
  deshifenaron/rejuntaron las palabras partidas a fin de línea en
  párrafos continuos.
- **NO se hizo reconstrucción palabra por palabra del OCR.** A
  diferencia de xerez/muñoz-camargo (donde el problema era aparato
  editorial moderno interleaved, resuelto con una lectura manual
  completa), acá el problema es la fidelidad del OCR de la letra
  antigua en sí — reconstruir correctamente ~119 000 palabras con esa
  tasa de error habría requerido comparar contra las imágenes de
  página originales, no solo el texto ya extraído, lo cual excede el
  alcance de esta pasada. El texto tal como quedó conserva muchas
  palabras deformadas por el OCR (ej. "efcriuia" en vez de "escribía",
  "fusiten tallen" en vez de "sustentasen") — es legible con esfuerzo
  y perfectamente utilizable para lectura humana en el sitio, pero
  **no es una transcripción palabra-exacta** todavía.

## Pendiente

- **Antes de correr Fase 2 (extracción de entidades/relaciones) sobre
  esta obra**, se recomienda una pasada de revisión/corrección manual
  del texto — idealmente cotejando contra las imágenes de página
  originales de Archive.org, o consiguiendo una transcripción
  alternativa de mejor calidad — porque nombres propios mal
  reconocidos por el OCR (personas, lugares) producirían entidades
  erróneas o duplicadas en el registro.
- Localizar a mano los ~25 capítulos cuyo encabezado no se detectó
  automáticamente (concentrados en Libro I y Libro VI) si se quiere
  granularidad completa de 130 capítulos.

## Fuente original

`raw/historia-descubrimiento-conquista-peru-archive-org.txt`
