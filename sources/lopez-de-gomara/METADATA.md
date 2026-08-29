---
titulo: "Historia general de las Indias y vida de Hernán Cortés"
autor: "Francisco López de Gómara"
escrito: "1552"
teatro: "Conquista de las Indias y de México (basada en testimonios de Cortés)"
estado_licencia: "dominio público"
estado_texto: "completa (con reservas — ver nota) — Preámbulo + 199 capítulos de la Historia general + Vida de Hernán Cortés en 6 secciones, ~170 000 palabras, limpio y dividido en texto-limpio/"
---

# Historia general de las Indias y vida de Hernán Cortés

## Texto listo (Fase 1)

`texto-limpio/historia-general-vida-cortes.md` — dos obras de Francisco
López de Gómara publicadas juntas en esta edición:

**Historia general de las Indias** (1552, completa): "A los leyentes",
"A los trasladores", la dedicatoria a Don Carlos, un Preámbulo sin título
("Es el mundo tan grande...") y 199 capítulos, ~158 500 palabras. El
índice impreso de esta misma edición (recuperado al final del escaneo,
antes del aparato moderno) confirma que la obra completa tiene 224
capítulos (I a CCXXIV) — de esos, 199 se detectaron y dividieron de forma
fiable en el cuerpo del texto; los ~25 restantes no se perdieron, sino que
quedaron fusionados dentro del capítulo detectado inmediatamente anterior,
porque el marcador de capítulo (un numeral romano solo en su propia línea)
salió del OCR demasiado corrompido para reconocerlo con confianza como
límite real (mismo tipo de problema, y mismo criterio de "no adivinar",
que en `sources/zarate/METADATA.md`). La numeración de capítulos en
`texto-limpio/` es por posición real (Capítulo 1, 2, 3...), no el numeral
romano original — cada encabezado anota entre paréntesis el numeral tal
como lo leyó el OCR en ese punto (a veces también corrompido, p. ej.
"TM" en vez de "III", "CCXXIIT" en vez de "CCXXIII" — se dejaron tal
cual, sin intentar reconstruirlos, siguiendo el mismo criterio que Acosta).

**Vida de Hernán Cortés** (traducción al español de Joaquín García
Icazbalceta, publicada en el siglo XIX): 6 secciones temáticas (esta
edición no trae división en capítulos), ~11 150 palabras. **Nota
importante sobre autoría**: una nota archivística del propio traductor,
fechada en Simancas y firmada "Juan Baut. Muñoz", que aparece al final del
texto en esta edición (excluida de `texto-limpio/` por ser aparato
editorial, pero preservada aquí por su relevancia), dice haber hallado el
original de esta obra en el Archivo de Simancas como parte de un
manuscrito titulado *De rebus gestis Ferd. Cortessii*, y conjetura que
podría no ser de Gómara sino de Cristóbal de Calvet de Estrella u otro
cronista — la atribución a López de Gómara que lleva esta edición (y que
seguimos aquí por convención bibliográfica, ya que así se cataloga y así
se publicó) **no es del todo segura**. Tenerlo en cuenta en Fase 2 al
etiquetar la fuente de las relaciones extraídas de esta sección
específicamente (`source:lopez-de-gomara:cap-XXX` donde XXX cae dentro de
las 6 secciones de Vida de Hernán Cortés). Además, el texto tal como
aparece en esta edición no cubre la vida completa de Cortés: termina
justo cuando la armada zarpa hacia la Nueva España en 1519 (con un cierre
retórico, no un corte a media frase), consistente con la nota del
traductor de que el manuscrito original es un fragmento incompleto.

Fuente: escaneo OCR de la edición Biblioteca Ayacucho (Caracas, 1979,
prólogo y edición de Jorge Gurría Lacroix),
https://archive.org/details/lopez-de-gomara-francisco.-historia-general-de-las-indias.-vida-de-hernan-cortes-ocr-1979.

Se excluyó por completo el aparato editorial moderno de 1979: el prólogo
biográfico-crítico de Jorge Gurría Lacroix ("Gómara, vida y obra", ~1350
palabras), la sección "Criterio de esta edición", y el índice impreso
final. En la Vida de Hernán Cortés se excluyeron además las notas al pie
de Icazbalceta (unas 17 notas numeradas, con citas a Oviedo, Pedro Mártir,
Herrera, Robertson y manuscritos del Archivo de Simancas) — a diferencia
del aparato de 1979, estas notas del siglo XIX son en sí mismas dominio
público (Icazbalceta murió en 1894), así que se quitaron por consistencia
de formato de lectura con el resto del sitio (mismo criterio aplicado en
`sources/pedro-martir/METADATA.md`), no por derechos de autor.

Verificación de contaminación en ambas direcciones, aplicando la lección
de Cieza de León/Pedro Pizarro/Acosta (un filtro mecánico de notas al pie
puede borrar narrativa real en silencio): un primer filtro automático por
patrón (párrafo que empieza con un dígito u OCR de dígito pegado a
mayúscula) detectó 9 de las notas de Icazbalceta pero dejó pasar otras 12
notas/fragmentos editoriales largos que no seguían ese patrón exacto —
se encontraron con una segunda pasada dirigida (búsqueda de nombres de
historiadores citados en tercera persona, fórmulas como "según el autor
citado", fechas de archivo) y se revisó cada una a mano antes de
quitarla, confirmando que dos párrafos que parecían sospechosos por
mencionar cronistas antiguos (Oviedo, Pedro Mártir) eran en realidad
narrativa genuina de Gómara/Icazbalceta citando a otros cronistas dentro
de su propio relato, no notas — se conservaron. Un caso de frase cortada
a la mitad por una nota intercalada ("...Las familias de" seguido de la
nota, seguido de "Cortés, Monroy, Pizarro..." como si fuera un párrafo
nuevo) se detectó y se volvió a unir en una sola oración.

**No se hizo una relectura palabra por palabra de las ~170 000 palabras
finales** — la verificación fue sistemática y dirigida, no exhaustiva
línea por línea. La Historia general en particular retiene ruido de OCR
disperso sin corregir a nivel de palabra (aparte de un puñado de
confusiones sistemáticas b/h corregidas: "bistoria"→"historia",
"bombres"→"hombres", "bizo"→"hizo", etc.) — valdría la pena una
relectura manual completa antes de tratar este texto como citation-exact
para Fase 2, mismo caveat que en `sources/zarate/METADATA.md` y
`sources/pedro-martir/METADATA.md`.

## Fuente original

`raw/historia-general-indias-vida-cortes-archive-org.txt`
