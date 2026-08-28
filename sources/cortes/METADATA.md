---
titulo: "Cartas de relación"
autor: "Hernán Cortés"
escritas: "1519–1526"
teatro: "Nueva España"
estado_licencia: "dominio público"
estado_texto: "activa — 5 cartas de relación limpias y en el MVP, vía edición digital ePubLibre (2013). Sin entidades/relaciones curadas todavía."
---

# Cartas de relación

Los cinco informes oficiales de Cortés a la corona.

## Historial

Se había dejado fuera del corpus piloto porque la única fuente conseguida
era un PDF escaneado de 344 MB sin OCR. El 2026-08-28 se consiguió una
edición digital (ePubLibre, 2013, vía Archive.org) con texto nacido
digital — no un escaneo — lo que permitió sacar la obra de pausa sin
necesidad de OCR.

## Texto listo (Fase 1)

`texto-limpio/cartas-de-relacion.md` — las 5 cartas completas
(~172 000 palabras), limpias de marcadores de página del OCR de
Archive.org. Se excluyó el aparato editorial moderno de esta edición
(introducción, bibliografía, notas y glosario) — no es texto de Cortés.

## Fuente original

`raw/cartas-de-relacion-epublibre.txt` — vía Archive.org:
https://archive.org/stream/cortes-hernan.-cartas-de-relacion-epl-fs-2013/

`raw/cartas-del-famoso-conquistador-hernan-cortes-al-emperador-carlos-quinto-975526.pdf`
— el escaneo de imágenes original (344 MB, sin OCR); se conserva pero ya
no es la fuente activa. Excluido de git (ver `.gitignore` en la raíz).

## Otras fuentes verificadas (referencia / cotejo)

- Wikisource (mejor calidad, no alcanzable desde el entorno de nube original —
  sí podría funcionar desde Claude Code local, ver `CLAUDE.md`):
  `https://es.wikisource.org/wiki/Cartas_del_famoso_conquistador_Hernán_Cortés/Carta_primera` (y siguientes)
- Internet Archive, edición de Pascual de Gayangos (1866):
  `https://archive.org/details/cartas-y-relaciones-hernan-cortes`

## Pendiente

Fase 2 (personas, lugares, relaciones) — todavía no empezó para esta obra.
