---
titulo: "Crónica del Perú"
autor: "Pedro Cieza de León"
escrito: "1553"
teatro: "Conquista, geografía e historia andina"
estado_licencia: "dominio público"
estado_texto: "completa — texto limpio y dividido en capítulos en texto-limpio/ (solo la Primera Parte, que es lo que cubre esta edición)"
---

# Crónica del Perú

## Texto listo (Fase 1)

`texto-limpio/cronica-del-peru.md` — Dedicatoria + Proemio del autor +
121 capítulos (la Primera Parte completa), ~123 800 palabras. Fuente del
escaneo: edición Crónicas de América 4 (Historia 16, Madrid, 1984, ed.
Manuel Ballesteros Gaibrois), vía Archive.org.

Se excluyó por completo la introducción/estudio biográfico, la
bibliografía y las más de 400 notas a pie de página de esa edición de
1984 — es aparato editorial moderno, no de dominio público (solo se
conservó el texto de Cieza de León mismo). El escaneo tenía las notas al
pie intercaladas físicamente entre los párrafos del propio Cieza
(maquetación de página con notas separadas del cuerpo por saltos de
página, a veces con dos columnas de notas mezcladas por el OCR); se
separaron con un pipeline que sigue el flujo página a página (marcador
de nota vs. número de página vs. texto narrativo) y se verificó con una
revisión automatizada de todo el documento en busca de rastros de
aparato editorial filtrado (menciones de Cieza en tercera persona,
"véase", nombres de editores/bibliógrafos, números de página impresos),
seguida de una revisión manual dirigida a cada resultado sospechoso —
no una lectura línea por línea de las ~123 000 palabras. Se corrigieron
artefactos de OCR (palabras cortadas al final de renglón o página,
algunos guiones de corte de palabra mal leídos como puntos, apóstrofos
espurios insertados en medio de una palabra) sin modernizar la
ortografía original de Cieza.

Un pasaje (dentro del proemio, sobre la fundación de Popayán) tenía el
número de una nota tan deteriorado por el OCR que no pudo identificarse
con certeza — no se descarta algún artefacto menor residual en el resto
del texto.

## Pendiente

- Esta edición solo cubre la **Primera Parte** de la obra de Cieza (las
  partes segunda, tercera y cuarta, mencionadas por el propio autor en
  su proemio, no están en esta fuente — quedarían como una adquisición
  separada si se quieren agregar más adelante).
- Fase 2: no empezó.

## Fuente original

`raw/cronica-del-peru-archive-org.txt` — vía Archive.org (edición
Crónicas de América 4, Historia 16, 1984, ed. Manuel Ballesteros
Gaibrois): https://archive.org/details/cieza-de-leon-pedro-de.-la-cronica-del-peru-ocr-1985
