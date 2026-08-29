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
repo.** El 2026-08-29 se completó Fase 1 (limpieza) para 16 de las 17
obras nuevas, y Fase 2 (entidades/relaciones) para 10 de ellas —
ver `CLAUDE.md`, sección "Estado actual", para el detalle preciso de
cobertura, reservas y huecos de cada una (esta tabla solo resume qué
fase alcanzó cada obra, no cuánto de cada una está realmente cubierto).

Estados usados: **activa** (Fase 1+2 completas y sumada al sitio) ·
**Fase 1+2** (completas pero todavía sin sumar al sitio) · **Fase 1**
(texto limpio, Fase 2 pendiente) · **Fase 1 (reservas)** (texto limpio
pero con problemas serios de fidelidad OCR, no recomendada para Fase 2
sin revisión manual) · **por procesar** (raw/ descargado, Fase 1
pendiente) · **parcial** (se consiguió una parte de la obra, no toda, o
una edición/versión distinta a la pedida — puede combinarse con
cualquier estado de arriba).

| # | Cronista | Obra pedida | Estado | Carpeta | Fuente |
|---|----------|-------------|--------|---------|--------|
| 1 | Cristóbal Colón | Diario del primer viaje | ✅ activa | `cristobal-colon/` | Wikisource |
| 1 | Cristóbal Colón | Cartas | ✅ activa (parcial: 10 bloques, no ~30; OCR sin corregir) | `colon-cartas/` | Archive.org (ed. 1892) |
| 2 | Hernán Cortés | Cartas de relación | ✅ activa | `cortes/` | Archive.org (ePubLibre 2013) |
| 3 | Bernal Díaz del Castillo | Historia verdadera de la conquista de la Nueva España | ✅ activa (parcial: tomo 1 de 3) | `bernal-diaz/` | Project Gutenberg |
| 4 | Francisco López de Gómara | Historia general de las Indias / Conquista de México | 🔵 Fase 1 (parcial: ~25/224 cap. sin dividir por OCR) | `lopez-de-gomara/` | Archive.org (Biblioteca Ayacucho 1979) |
| 5 | Gonzalo Fernández de Oviedo | Historia general y natural de las Indias | 🟡 por procesar (4 tomos, ~1.77M palabras, peor OCR del catálogo) | `oviedo/` | Archive.org (ed. Real Academia de la Historia) |
| 6 | Bartolomé de las Casas | Historia de las Indias | ✅ activa | `las-casas/` | Project Gutenberg |
| 6 | Bartolomé de las Casas | Brevísima relación de la destrucción de las Indias | 🟡 por procesar | `las-casas/` (raw/brevisima-*) | Archive.org (ed. 1991) |
| 7 | Pedro Mártir de Anglería | Décadas del Nuevo Mundo (De Orbe Novo) | 🟢 Fase 1+2 (sin sumar al sitio aún) | `pedro-martir/` | Archive.org (trad. Torres Asensio 1892) |
| 8 | Álvar Núñez Cabeza de Vaca | Naufragios | ✅ activa | `cabeza-de-vaca/` | Wikisource |
| 9 | Fray Toribio de Benavente "Motolinía" | Historia de los indios de la Nueva España | ✅ activa | `motolinia/` | Archive.org |
| 10 | Fray Bernardino de Sahagún | Historia general de las cosas de Nueva España | 🔵 Fase 1 (parcial: solo tomo B, faltan los demás tomos) | `sahagun/` | Archive.org (ed. 1990) |
| 11 | Fray Diego Durán | Historia de las Indias de Nueva España e islas de Tierra Firme | 🔵 Fase 1 (incluye un Apéndice que no es de Durán, separado) | `duran/` | Archive.org (escaneo s. XIX) |
| 12 | José de Acosta | Historia natural y moral de las Indias | 🟢 Fase 1+2 (sin sumar al sitio aún) | `acosta/` | Archive.org (ed. 1986) |
| 13 | Pedro Cieza de León | Crónica del Perú | ✅ activa (parcial: solo Primera Parte) | `cieza-de-leon/` | Archive.org (ed. 1985) |
| 14 | Agustín de Zárate | Historia del descubrimiento y conquista del Perú | 🟠 Fase 1 (reservas — OCR severo, ~25/130 cap. sin separar) | `zarate/` | Archive.org (BNE, ed. Amberes 1555) |
| 15 | Francisco de Xerez | Verdadera relación de la conquista del Perú | ✅ activa | `xerez/` | Archive.org (ed. 1985) |
| 16 | Pedro Pizarro | Relación del descubrimiento y conquista de los reinos del Perú | ✅ activa | `pedro-pizarro/` | Archive.org (ed. PUCP) |
| 17 | Inca Garcilaso de la Vega | Comentarios reales de los Incas; Historia general del Perú | 🔵 Fase 1 (parcial: falta Historia general del Perú, 2ª parte) | `inca-garcilaso/` | Archive.org (Biblioteca Ayacucho 1985) |
| 18 | Felipe Guamán Poma de Ayala | Nueva corónica y buen gobierno | 🟠 Fase 1 (reservas graves — falta la primera mitad de la obra, folios 1-559; peor OCR del catálogo entre las procesadas) | `guaman-poma/` | Archive.org (Biblioteca Ayacucho 1980) |
| 19 | Fernando de Alva Ixtlilxóchitl | Historia de la nación chichimeca | ✅ activa (obra incompleta en su propia fuente) | `ixtlilxochitl/` | Archive.org (ed. 1985) |
| 20 | Hernando Alvarado Tezozómoc | Crónica mexicana / Crónica mexicáyotl | ✅ activa — **solo Crónica mexicana; falta Crónica mexicáyotl (obra distinta)** | `tezozomoc/` | Archive.org (ed. 1997) |
| 21 | Diego Muñoz Camargo | Historia de Tlaxcala | ✅ activa | `munoz-camargo/` | Archive.org (ed. 1986) |

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

## Calidad de las fuentes conseguidas — lo que se encontró en Fase 1

16 de las 17 obras nuevas ya pasaron Fase 1 (2026-08-29) — el ruido de
OCR y el aparato editorial que esta sección advertía sí aparecieron, en
distinto grado según la fuente:

- **Ediciones críticas modernas** (colección "Crónicas de América"/
  Historia 16 — Xerez, Muñoz Camargo, Ixtlilxóchitl, Cieza de León,
  Sahagún, Tezozómoc; Biblioteca Ayacucho — López de Gómara, Inca
  Garcilaso, Guamán Poma; PUCP — Pedro Pizarro): todas traían
  introducción y notas al pie de un editor del siglo XX, con copyright
  propio y distinto al de la crónica original — se excluyeron por
  completo (no solo se separaron), y en varias el filtrado mecánico casi
  o efectivamente borró contenido real por notas intercaladas sin
  repetir su número de página en página — ver CLAUDE.md, "Estado
  actual", punto (4)/(5).
- **Escaneos de ediciones viejas, sin aparato moderno que excluir**
  (Zárate: original de 1555; Durán: escaneo del s. XIX; Oviedo: edición
  RAH de 1851): el problema ahí es solo fidelidad del OCR sobre
  tipografía antigua, no aparato editorial — y resultó **mucho más
  grave** de lo esperado: Zárate y Oviedo quedaron con reservas serias
  o sin poder ni empezar.
- **Peor caso encontrado: Guamán Poma** — el "tomo1" adquirido resultó
  ser 100% aparato editorial moderno (cero palabras de Guamán Poma), y
  el "tomo2" empieza a mitad de la obra (folio 560 de ~1200) — un hueco
  de fuente mucho más grave que "ruido de OCR", ver más abajo.

## Huecos que quedan (no se consiguió la obra completa pedida)

- **Sahagún**: solo un tomo (B, Libros VII-XII de 12) de una edición de
  varios volúmenes — confirmado tras Fase 1.
- **Inca Garcilaso**: falta *Historia general del Perú* (2ª parte); la
  Primera Parte (9 libros, 246 capítulos) sí está completa.
- **Tezozómoc**: falta *Crónica mexicáyotl* (obra distinta de *Crónica
  mexicana*, que sí se consiguió completa).
- **Guamán Poma — el hueco más grave del catálogo**: falta toda la
  primera mitad de la obra (folios 1-559 de ~1200: mito de creación,
  genealogía inca, la conquista, inicio del "Buen gobierno"). Lo
  conseguido (folios 560-1167) también carece de las ~400 ilustraciones
  del manuscrito autógrafo, que solo están en el sitio de la Biblioteca
  Real de Dinamarca (kb.dk) — pendiente: buscar ahí el facsímil completo
  o una edición impresa distinta que sí cubra la primera mitad.

## Pendiente general

Ver CLAUDE.md, sección "Pendientes", para el orden sugerido actual
(Fase 2 de las 4 obras que ya tienen Fase 1 limpia, revisión manual de
Zárate/Guamán Poma antes de su Fase 2, Fase 1 de Oviedo, y cierre de los
huecos de fuente de arriba).
