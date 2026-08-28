---
layout: default
title: Personas
permalink: /personas/
---
{% assign obras = site.personas | group_by: "obra" %}
{% for grupo in obras %}
<h3 style="margin:1.4rem 0 0.6rem;">{{ grupo.items.first.obra_titulo }}</h3>
<div class="grid">
  {% assign items = grupo.items | sort: "canonical_name" %}
  {% for p in items %}
  <a class="card" href="{{ p.url | relative_url }}">
    <div class="chead"><span class="cname">{{ p.canonical_name }}</span></div>
    <p class="crole">{{ p.role }}</p>
    {% if p.aliases and p.aliases.size > 0 %}
    <div class="caliases">{% for a in p.aliases %}<span class="alias">{{ a }}</span>{% endfor %}</div>
    {% endif %}
    <div class="cfoot">
      <span><span class="status-dot {{ p.status }}"></span>{{ p.status }}</span>
      <span>{% if p.mention_count_aprox %}~{{ p.mention_count_aprox }} menciones{% endif %}</span>
    </div>
  </a>
  {% endfor %}
</div>
{% endfor %}
