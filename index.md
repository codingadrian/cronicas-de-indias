---
layout: default
title: Inicio
permalink: /
---
<p class="hint">Cinco crónicas completas — hacé clic para leerlas. Los nombres de personas, lugares y años que aparecen resaltados en el texto son enlaces.</p>
<div class="doc-library">
{% assign obras = site.documentos | group_by: "obra" %}
{% for grupo in obras %}
  {% assign primero = grupo.items | where: "chapter_index", 0 | first %}
  {% unless primero %}{% assign primero = grupo.items | sort: "chapter_index" | first %}{% endunless %}
  {% assign teaser = primero.content | strip_html | strip_newlines | truncate: 170 %}
  <a class="doc-card" href="{{ primero.url | relative_url }}">
    <h3>{{ primero.obra_titulo }}</h3>
    <div class="dauthor">{{ primero.autor }}</div>
    <div class="dmeta">{% if primero.obra_nota %}{{ primero.obra_nota }} · {% endif %}{{ grupo.items.size }} capítulos</div>
    <p class="dteaser">{{ teaser }}…</p>
    <span class="dgo">Leer →</span>
  </a>
{% endfor %}
</div>
