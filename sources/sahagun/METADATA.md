---
titulo: "Historia general de las cosas de Nueva España (Códice Florentino)"
autor: "Fray Bernardino de Sahagún"
escrito: "c. 1540-1585"
teatro: "Cultura, religión, lengua e historia nahua"
estado_licencia: "dominio público"
estado_texto: "parcial — Tomo B (Libros VII-XII de 12), 142 secciones (6 prólogos + 136 capítulos), ~170 000 palabras, limpio y dividido en texto-limpio/; falta el Tomo A (Libros I-VI) para tener la obra completa"
---

# Historia general de las cosas de Nueva España (Códice Florentino)

## Texto listo (Fase 1, parcial)

`texto-limpio/historia-general-cosas-nueva-espana-tomo-b.md` — Libro
Séptimo al Libro Duodécimo (de los 12 libros originales), cada uno con su
propio Prólogo + capítulos numerados: Libro VII (12 cap.), Libro VIII (21
cap.), Libro IX (21 cap.), Libro X (28 cap.), Libro XI (13 cap.), Libro
XII (41 cap.) — 136 capítulos + 6 prólogos = 142 secciones, ~170 000
palabras. Termina donde termina el propio Tomo B (Libro XII, Capítulo 41,
"...todo el oro venía a su poder") — no es un corte de esta limpieza, es
el final real del volumen conseguido.

Fuente: escaneo OCR de una edición crítica de 1990 ("Crónicas de América"
/ Historia 10, dirigida por Manuel Ballesteros Gaibrois — el mismo
director que la edición de Cieza de León —, edición/introducción/notas de
Juan Carlos Temprano),
https://archive.org/details/sahagun-bernardino-de.-historia-general-de-las-cosas-de-nueva-espana-tomo-b-ocr-1990.
Se excluyó por completo el aparato editorial moderno de Temprano (nota de
colección, la sección "NOTAS" agrupada por libro al final del volumen con
sus ~90 marcadores `(N)` dentro del cuerpo, el glosario náhuatl, y el
índice/catálogo editorial final) — solo se conservó la prosa de Sahagún.

**Advertencia importante — este es el peor caso de OCR de todo el
proyecto, peor incluso que el de Zárate (tipografía del s. XVI):** el
motor de OCR confundió sistemáticamente letras con dígitos (6→é,
0/1/3→l/í/á según posición, k→é) y, en varios cientos de casos, con
ideogramas CJK sueltos (人, 和, 上, 了, etc.) — estos últimos NO se
intentaron adivinar letra por letra, para no inventar contenido; se
dejaron tal como los leyó el OCR. Se aplicó una limpieza sistemática de
los patrones más frecuentes (puntuación de ancho completo, sustituciones
dígito-por-vocal-acentuada, y un diccionario de más de 100 formas de
palabra corregidas a mano tras un análisis de frecuencia), que redujo el
ruido de miles de instancias a unos ~900 tokens con dígitos residuales y
~900 ideogramas CJK residuales sobre las ~170 000 palabras totales —
concentrados sobre todo en vocabulario náhuatl (nombres propios, términos
culturales) y en pasajes puntuales que el diccionario no cubrió. También
se corrigieron a mano tres números de capítulo mal leídos por el OCR,
detectados por comparar contra la secuencia esperada (Libro VIII: un "13"
duplicado era en realidad el 15; Libro X: un "20" era en realidad el 26;
Libro XII: un "30" era en realidad el 36) — la numeración de capítulos en
`texto-limpio/` ya está corregida.

**Esta es la obra que más necesita una relectura humana completa contra
el escaneo original antes de tratarse como citation-exact — no usar para
Fase 2 sin esa revisión, en especial para vocabulario y nombres propios
náhuatl.** No se hizo una relectura palabra por palabra de las 170 000
palabras finales — la limpieza fue sistemática (diccionario de frecuencia
+ verificación dirigida), no exhaustiva línea por línea.

## Pendiente

- **Fase 1 del Tomo A** (Libros I-VI): no conseguido todavía — buscarlo es
  trabajo pendiente para tener la obra completa.
- **Relectura manual de este Tomo B** contra el escaneo original antes de
  Fase 2 (ver advertencia arriba) — prioridad alta dado lo severo del OCR.
- Fase 2: no empezó.

## Fuente original

`raw/historia-general-cosas-nueva-espana-tomo-b-archive-org.txt` — **solo "tomo B" de la edición consultada, no la obra completa**.
