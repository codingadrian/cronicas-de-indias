// Etiqueta menciones de personas/lugares/años dentro de un capítulo con enlaces
// clicables, y resuelve el salto "Leer en contexto" (#leer-<id>-<occ>) que
// llega desde una página de persona/lugar. Adaptado de tagChapterHtml/
// buildEntityIndex del MVP original — mismo patrón de límite de palabra con
// \p{L}\p{N} (no \b, que no trata las tildes como letras).
(function () {
  "use strict";

  function escapeReg(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function buildIndex(entities) {
    const aliasMap = new Map();
    entities.forEach((e) => {
      const cands = new Set();
      const base = e.canonical_name.replace(/\s*\([^)]*\)\s*/g, " ").trim();
      if (base) cands.add(base);
      (e.aliases || []).forEach((a) => {
        if (a) cands.add(a.trim());
      });
      cands.forEach((c) => {
        if (c && c.length >= 3 && !aliasMap.has(c)) aliasMap.set(c, e);
      });
    });
    const list = Array.from(aliasMap.keys()).sort((a, b) => b.length - a.length);
    const regex = list.length
      ? new RegExp("(?<![\\p{L}\\p{N}])(?:" + list.map(escapeReg).join("|") + ")(?![\\p{L}\\p{N}])", "gu")
      : null;
    return { aliasMap, regex };
  }

  const YEAR_RE = /(?<![\p{L}\p{N}])(1[2-5]\d{2})(?![\p{L}\p{N}])/gu;

  function tagTextNode(node, idx, occCounters, baseurl) {
    const text = node.nodeValue;
    const matches = [];
    let m;
    YEAR_RE.lastIndex = 0;
    while ((m = YEAR_RE.exec(text))) {
      matches.push({ start: m.index, end: m.index + m[0].length, type: "fecha", text: m[0] });
    }
    if (idx.regex) {
      idx.regex.lastIndex = 0;
      while ((m = idx.regex.exec(text))) {
        matches.push({ start: m.index, end: m.index + m[0].length, type: "entity", text: m[0], info: idx.aliasMap.get(m[0]) });
      }
    }
    if (!matches.length) return;
    matches.sort((a, b) => a.start - b.start);
    const clean = [];
    let lastEnd = -1;
    matches.forEach((mt) => {
      if (mt.start >= lastEnd) {
        clean.push(mt);
        lastEnd = mt.end;
      }
    });

    const frag = document.createDocumentFragment();
    let cursor = 0;
    clean.forEach((mt) => {
      if (mt.start > cursor) frag.appendChild(document.createTextNode(text.slice(cursor, mt.start)));
      if (mt.type === "fecha") {
        const span = document.createElement("span");
        span.className = "ent ent-fecha";
        span.dataset.year = mt.text;
        span.textContent = mt.text;
        frag.appendChild(span);
      } else {
        const n = occCounters.get(mt.info.id) || 0;
        occCounters.set(mt.info.id, n + 1);
        const a = document.createElement("a");
        a.className = "ent ent-" + mt.info.tipo;
        a.href = baseurl + mt.info.url;
        a.dataset.id = mt.info.id;
        a.dataset.occ = String(n);
        a.textContent = mt.text;
        frag.appendChild(a);
      }
      cursor = mt.end;
    });
    if (cursor < text.length) frag.appendChild(document.createTextNode(text.slice(cursor)));
    node.parentNode.replaceChild(frag, node);
  }

  function jumpToHash(body) {
    const m = /^#leer-(.+)-(\d+)$/.exec(location.hash);
    if (!m) return;
    const entId = m[1];
    const occ = m[2];
    const target = Array.from(body.querySelectorAll(".ent[data-id]")).find(
      (el) => el.dataset.id === entId && el.dataset.occ === occ
    );
    if (target) {
      target.classList.add("flash");
      if (target.scrollIntoView) target.scrollIntoView({ block: "center", behavior: "smooth" });
      setTimeout(() => target.classList.remove("flash"), 1800);
    }
  }

  function run() {
    const readerEl = document.querySelector(".doc-reader[data-entity-data]");
    const body = document.getElementById("dr-body");
    if (!readerEl || !body) return;
    const baseurl = readerEl.dataset.baseurl || "";
    fetch(readerEl.dataset.entityData)
      .then((r) => r.json())
      .then((entities) => {
        const idx = buildIndex(entities);
        const occCounters = new Map();
        const walker = document.createTreeWalker(body, NodeFilter.SHOW_TEXT, null);
        const nodes = [];
        let n;
        while ((n = walker.nextNode())) nodes.push(n);
        nodes.forEach((node) => tagTextNode(node, idx, occCounters, baseurl));
        jumpToHash(body);
      })
      .catch(() => {});
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
  else run();
})();
