---
title: "Catálogo de cronistas de Indias — pistas de trabajo"
---

# Catálogo de cronistas de Indias

Lista de referencia de las 20 crónicas priorizadas por el usuario
(2026-08-28), con el estado real de cada una en este repositorio.
`sources/<obra>/METADATA.md` tiene el detalle de cada obra; acá se
resume el panorama completo.

**Resultado de la tanda de adquisición del 2026-08-28: las 20 crónicas
de la lista tienen ahora al menos Fase 0 (fuente descargada) en este
repo.** Cinco ya estaban o quedaron en Fase 1 completa (activas en el
MVP); las otras 15 tienen `raw/` conseguido pero **todavía no pasaron
por Fase 1** (limpieza, separación de aparato editorial, división en
capítulos) ni por Fase 2 (entidades/relaciones).

Estados usados: **activa** (Fase 1 completa, en `texto-limpio/` y en el
MVP) · **por procesar** (raw/ descargado, Fase 1 pendiente) · **parcial**
(se consiguió una parte de la obra, no toda, o una edición/versión
distinta a la pedida).

| # | Cronista | Obra pedida | Estado | Carpeta | Fuente |
|---|----------|-------------|--------|---------|--------|
| 1 | Cristóbal Colón | Diario del primer viaje | ✅ activa | `cristobal-colon/` | Wikisource |
| 1 | Cristóbal Colón | Cartas | ✅ activa (parcial: 10 bloques, no ~30; OCR sin corregir) | `colon-cartas/` | Archive.org (ed. 1892) |
| 2 | Hernán Cortés | Cartas de relación | ✅ activa | `cortes/` | Archive.org (ePubLibre 2013) |
| 3 | Bernal Díaz del Castillo | Historia verdadera de la conquista de la Nueva España | ✅ activa (parcial: tomo 1 de 3) | `bernal-diaz/` | Project Gutenberg |
| 4 | Francisco López de Gómara | Historia general de las Indias / Conquista de México | 🟡 por procesar | `lopez-de-gomara/` | Archive.org (Biblioteca Ayacucho 1979) |
| 5 | Gonzalo Fernández de Oviedo | Historia general y natural de las Indias | 🟡 por procesar (4 tomos, ~1.77M palabras) | `oviedo/` | Archive.org (ed. Real Academia de la Historia) |
| 6 | Bartolomé de las Casas | Historia de las Indias | ✅ activa | `las-casas/` | Project Gutenberg |
| 6 | Bartolomé de las Casas | Brevísima relación de la destrucción de las Indias | 🟡 por procesar | `las-casas/` (raw/brevisima-*) | Archive.org (ed. 1991) |
| 7 | Pedro Mártir de Anglería | Décadas del Nuevo Mundo (De Orbe Novo) | 🟡 por procesar | `pedro-martir/` | Archive.org (trad. Torres Asensio 1892) |
| 8 | Álvar Núñez Cabeza de Vaca | Naufragios | 🟡 por procesar (wikitexto ya limpiado) | `cabeza-de-vaca/` | Wikisource |
| 9 | Fray Toribio de Benavente "Motolinía" | Historia de los indios de la Nueva España | 🟡 por procesar | `motolinia/` | Archive.org |
| 10 | Fray Bernardino de Sahagún | Historia general de las cosas de Nueva España | 🟡 por procesar — **parcial: solo tomo B, faltan los demás tomos** | `sahagun/` | Archive.org (ed. 1990) |
| 11 | Fray Diego Durán | Historia de las Indias de Nueva España e islas de Tierra Firme | 🟡 por procesar (2 tomos) | `duran/` | Archive.org (escaneo s. XIX) |
| 12 | José de Acosta | Historia natural y moral de las Indias | 🟡 por procesar | `acosta/` | Archive.org (ed. 1986) |
| 13 | Pedro Cieza de León | Crónica del Perú | 🟡 por procesar | `cieza-de-leon/` | Archive.org (ed. 1985) |
| 14 | Agustín de Zárate | Historia del descubrimiento y conquista del Perú | 🟡 por procesar | `zarate/` | Archive.org (BNE, ed. Amberes 1555) |
| 15 | Francisco de Xerez | Verdadera relación de la conquista del Perú | 🟡 por procesar | `xerez/` | Archive.org (ed. 1985) |
| 16 | Pedro Pizarro | Relación del descubrimiento y conquista de los reinos del Perú | 🟡 por procesar (OCR ruidoso en portada) | `pedro-pizarro/` | Archive.org (ed. PUCP) |
| 17 | Inca Garcilaso de la Vega | Comentarios reales de los Incas; Historia general del Perú | 🟡 por procesar — **falta Historia general del Perú (2ª parte)** | `inca-garcilaso/` | Archive.org (Biblioteca Ayacucho 1985) |
| 18 | Felipe Guamán Poma de Ayala | Nueva corónica y buen gobierno | 🟡 por procesar (2 tomos) | `guaman-poma/` | Archive.org (Biblioteca Ayacucho 1980) |
| 19 | Fernando de Alva Ixtlilxóchitl | Historia de la nación chichimeca | 🟡 por procesar | `ixtlilxochitl/` | Archive.org (ed. 1985) |
| 20 | Hernando Alvarado Tezozómoc | Crónica mexicana / Crónica mexicáyotl | 🟡 por procesar — **solo Crónica mexicana; falta Crónica mexicáyotl (obra distinta)** | `tezozomoc/` | Archive.org (ed. 1997) |
| 21 | Diego Muñoz Camargo | Historia de Tlaxcala | 🟡 por procesar | `munoz-camargo/` | Archive.org (ed. 1986) |

## Cómo se buscó

1. **Wikisource primero** (confirmado reachable desde Claude Code local,
   a diferencia del entorno de nube original — ver `CLAUDE.md`). Solo
   tenía completos: *Naufragios* y el *Diario* de Colón (ya conocido).
   *Brevísima relación* y *Nueva corónica y buen gobierno* aparecen en
   Wikisource pero **incompletos/parafraseados** — se prefirió Archive.org.
2. **Archive.org**, vía su API de búsqueda (`advancedsearch.php`) y
   metadata (`/metadata/<id>`) para verificar que el ítem no fuera de
   préstamo restringido (`access-restricted-item`) antes de bajar el
   `_djvu.txt`. Todo lo marcado "por procesar" arriba salió de acá.
3. Un solo ítem bloqueado por préstamo controlado (Diego Durán,
   `bwb_S0-CAF-728_2`) — se encontró un ítem alternativo sin restricción
   (`historiadelasind01dur`/`02dur`, escaneo del siglo XIX).
4. Gómara también tiene PDFs sueltos (mercaba.es, CLACSO) encontrados
   por WebSearch, pero se usó la versión de Archive.org por ser más
   fácil de extraer como texto plano.

## Calidad de las fuentes conseguidas — importante para Fase 1

- **Ninguna de las 15 obras "por procesar" pasó revisión manual.** Son
  descargas directas (wikitexto limpiado programáticamente, o
  `_djvu.txt` de Archive.org tal cual) — pueden tener ruido de OCR,
  encabezados repetidos, marcadores de página, etc., como se vio y
  corrigió a mano en `cortes/` y `colon-cartas/` en la tanda anterior.
- Antes de armar `texto-limpio/` para cualquiera de estas, conviene
  inspeccionar el `raw/` primero (headers de Archive.org, prólogos
  editoriales modernos a separar, etc.), siguiendo el mismo patrón que
  `cortes/METADATA.md` y `colon-cartas/METADATA.md` documentan.

## Huecos que quedan (no se consiguió la obra completa pedida)

- **Sahagún**: solo un tomo (B) de una edición de varios volúmenes.
- **Inca Garcilaso**: falta *Historia general del Perú* (2ª parte);
  hay una pista en Wikisource sin confirmar completitud — ver
  `inca-garcilaso/METADATA.md`.
- **Tezozómoc**: falta *Crónica mexicáyotl* (obra distinta de *Crónica
  mexicana*, que sí se consiguió).
- **Guamán Poma**: el manuscrito autógrafo con los dibujos originales
  solo está en el sitio de la Biblioteca Real de Dinamarca (kb.dk); lo
  conseguido acá es una transcripción impresa sin las imágenes.

## Pendiente general

1. Para cada obra "por procesar": Fase 1 (limpieza, separar aparato
   editorial, dividir en capítulos) y después Fase 2 (entidades y
   relaciones) — mismo trabajo que ya se hizo para las 5 obras activas.
   Dado el volumen (15 obras, algunas enormes como Oviedo), conviene
   priorizar en vez de intentar procesar todo de una vez.
2. Cerrar los huecos de la sección anterior si hace falta la obra
   completa (Sahagún, Inca Garcilaso segunda parte, Tezozómoc).
