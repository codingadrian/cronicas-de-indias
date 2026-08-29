---
titulo: "Décadas del Nuevo Mundo (De Orbe Novo)"
autor: "Pedro Mártir de Anglería"
escrito: "1494-1526 (escrito en latín; trad. española de Joaquín Torres Asensio, 1892)"
teatro: "Primeras exploraciones y conquista"
estado_licencia: "dominio público"
estado_texto: "completa — Fase 1 hecha, texto-limpio/ armado (2026-08-29)"
---

# Décadas del Nuevo Mundo (De Orbe Novo)

## Texto listo (Fase 1)

`texto-limpio/decadas-del-nuevo-mundo.md` — Prólogo (1892) + Dedicatoria de
Anglería al rey Carlos (1516) + las 8 décadas completas (79 "Libros": 10
por década salvo la Década sexta, que tiene 9) + Advertencias finales del
traductor (1892). ~238 000 palabras — la obra más larga del proyecto hasta
ahora.

Es la traducción española de Joaquín Torres Asensio (Madrid, 1892), no el
latín original de Anglería. Se mantuvieron el Prólogo y las Advertencias
del traductor en sus propias secciones (son de 1892, misma edición
histórica, no aparato crítico moderno) — salvo 4 notas puntuales marcadas
explícitamente "(Nota del editor digital.)" en la digitalización de
Archive.org, que sí se excluyeron por ser modernas (de quien preparó este
escaneo concreto, no de Torres Asensio).

Se quitaron del cuerpo del texto unas 82 notas al pie numeradas del propio
Torres Asensio (aclaraciones de traducción, referencias bibliográficas,
comentario histórico suyo, y en un par de casos citas largas como el
testamento del propio Anglería o una cita del Diario de Colón vía Las
Casas) para dar continuidad de lectura a la narración — no se resumen ni
reproducen en texto-limpio. Esto es distinto del resto de notas al pie que
se han excluido en otras obras del catálogo: aquí no es una cuestión de
derechos de autor (Torres Asensio murió hace más de un siglo), es solo
para mantener el mismo formato de lectura continua que las demás obras del
sitio.

Cada "Libro" dentro de una década es en sí una carta de Anglería a un
destinatario distinto (cardenal, papa, rey) — se mantuvo esa línea de
dedicatoria propia de cada libro como parte del texto, no se trató como
aparato editorial (es de Anglería mismo, no de Torres Asensio). Dentro de
cada Libro, Torres Asensio añadió su propia subdivisión en "capítulos"
numerados con un resumen de una línea (él mismo lo explica en el Prólogo:
"he creído muy conveniente dividir los libros en capítulos... y poner los
sumarios") — se conservaron esos resúmenes numerados como texto corrido
dentro del Libro en vez de promoverlos a encabezados `##` propios, para no
multiplicar la granularidad de capítulos del sitio; quedan visibles en el
texto como líneas que empiezan con "1.", "2.", etc.

La Década sexta no usa la palabra "Libro" para encabezar sus subdivisiones
en el original (solo numerales sueltos) y salta del número 1 al 3 en el
texto fuente — son 9 subdivisiones en vez de 10; se preservó el salto tal
cual está en la fuente, no se inventó contenido para rellenarlo.

**Método de verificación** (dado lo largo del texto — 26 168 líneas del
raw): se usó la "Tabla"/estructura de encabezados DÉCADA/LIBRO del propio
texto como referencia (confirmados por conteo exacto: 79 encabezados de
Libro + 8 de Década), un script de limpieza que separa por bloques
delimitados por líneas en blanco y clasifica cada bloque (nota al pie /
número de página suelto / texto real), y una verificación posterior
buscando que no quedara ningún bloque residual con forma de nota al pie ni
ninguna mención de "editor digital" fuera de esta misma nota. Un primer
intento del script trató por error dos subtítulos numerados propios del
Prólogo (los números "1." y "4." que introducen sus subsecciones, ej. "4.
Patria y primeros años del autor...") como si fueran notas al pie —se
detectó al revisar el log de bloques removidos y se corrigió el criterio
antes de finalizar (ahora exige que haya texto en la misma línea que el
número para tratarlo como nota al pie). No se hizo una lectura manual
completa palabra por palabra de las 238 000 palabras — se verificó por
script más revisión puntual de los límites de Libro y de varias notas
removidas, no por lectura corrida como en otras obras más cortas del
catálogo. Queda como candidato razonable a una relectura humana antes de
tratarlo como citación exacta, sobre todo por el volumen.

Ruido de OCR menor conocido y no corregido: alguna comilla suelta residual
(ej. un carácter de cierre de comilla `"` colgado al final de la línea de
dedicatoria de un Libro), y posibles erratas puntuales típicas de OCR de
un escaneo de 1892 no revisadas palabra por palabra dado el volumen.

## Fuente original

`raw/decadas-del-nuevo-mundo-archive-org.txt` — vía Archive.org (edición Torres Asensio 1892, las 8 décadas completas): https://archive.org/details/525-pedro-martir-de-angleria
