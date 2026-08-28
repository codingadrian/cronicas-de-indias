---
layout: default
title: Lugares
permalink: /lugares/
---
{% assign obras = site.lugares | group_by: "obra" %}
{% for grupo in obras %}
<h3 style="margin:1.4rem 0 0.6rem;">{{ grupo.items.first.obra_titulo }}</h3>
<div class="grid">
  {% assign items = grupo.items | sort: "canonical_name" %}
  {% for l in items %}
  <a class="card" href="{{ l.url | relative_url }}">
    <div class="chead"><span class="cname">{{ l.canonical_name }}</span></div>
    <p class="crole">{{ l.modern_equivalent }}</p>
    <div class="cfoot">
      <span><span class="status-dot {{ l.status }}"></span>{{ l.status }}</span>
    </div>
  </a>
  {% endfor %}
</div>
{% endfor %}
