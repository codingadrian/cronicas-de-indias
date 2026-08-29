---
layout: default
title: Inicio
permalink: /
---
<section class="home-hero">
  <span class="eyebrow">Archivo abierto · dominio público</span>
  <h1>Un archivo vivo de las crónicas de Indias</h1>
  <p class="home-lede">Crónicas de Indias reúne el texto completo de las crónicas
  españolas sobre la conquista de América —de dominio público— junto con las
  personas, los lugares y los eventos que nombran, cada uno enlazado de vuelta
  al pasaje exacto de donde salió. No es un resumen ni una enciclopedia: es la
  fuente primaria misma, hecha más fácil de recorrer, citar y corregir.</p>
  <div class="home-ctas">
    <a class="home-cta primary" href="{{ '/documentos/' | relative_url }}">Explorar las crónicas →</a>
    <a class="home-cta secondary" href="https://github.com/codingadrian/cronicas-de-indias">Ver el repositorio en GitHub</a>
  </div>
</section>

<div class="home-sections">
  <div class="home-section">
    <h2>Cómo usarlo</h2>
    <p><b>Documentos</b> tiene el texto completo de cada crónica, capítulo por
    capítulo. Los nombres de persona, de lugar y los años que aparecen
    resaltados en el texto son enlaces: llevan a una página con todas las
    veces que esa persona o ese lugar se menciona a lo largo de la obra, con
    un botón para volver al pasaje exacto ("Leer en contexto").</p>
    <p><b>Personas</b> y <b>Lugares</b> son índices de todo lo catalogado
    hasta ahora, obra por obra. <b>Cronología</b> ordena los eventos
    identificados por fecha. El buscador de arriba busca por nombre o por
    cualquier palabra del texto, en todas las crónicas a la vez.</p>
  </div>
  <div class="home-section lugar-accent">
    <h2>Cómo colaborar</h2>
    <p>No hace falta saber programar. Cada capítulo, cada persona y cada
    lugar es un archivo de texto simple. Para corregir una errata o mejorar
    una transcripción: abrí el archivo en GitHub (el botón de lápiz ✏️
    "Edit this file"), hacé el cambio, y proponé un Pull Request.</p>
    <p>También es útil avisar de un dato dudoso, una identidad ambigua, o una
    crónica que falta —el
    <a href="https://github.com/codingadrian/cronicas-de-indias/blob/main/sources/CATALOGO.md">catálogo de fuentes</a>
    lleva el registro de qué se consiguió, de dónde, y qué huecos quedan.</p>
  </div>
  <div class="home-section evento-accent">
    <h2>Qué vas a encontrar</h2>
    <p>{{ site.data.stats.obras }} obras completas, {{ site.data.stats.personas }}
    personas y {{ site.data.stats.lugares }} lugares catalogados,
    {{ site.data.stats.eventos }} eventos y {{ site.data.stats.relaciones }}
    relaciones entre ellos — cada una citando el capítulo exacto de donde sale.
    Varias decenas de crónicas más están en distintas etapas de limpieza y
    catalogación, camino a sumarse al archivo.</p>
    <p>Todo el trabajo de catalogación queda marcado como <em>candidato</em>
    hasta que pasa una segunda revisión — es un punto de partida para
    investigar, no una autoridad final.</p>
  </div>
</div>

<div class="home-vision">
  <h2>Nuestra visión</h2>
  <ul class="home-pillars">
    <li><b>Convertirnos en una referencia de alta calidad</b> para
    historiadores, escritores, y cualquiera que quiera acercarse a estas
    fuentes de primera mano.</li>
    <li><b>Permanecer en dominio público</b>, siempre — el texto, los datos,
    y el código de este sitio son libres de usar, copiar y redistribuir.</li>
    <li><b>Mejorar la digitalización</b> de estas crónicas: menos ruido de
    escaneo, aparato editorial moderno separado del texto original, y una
    transcripción cada vez más fiel a la fuente.</li>
  </ul>
  <p class="home-signature">— El Editor</p>
</div>
