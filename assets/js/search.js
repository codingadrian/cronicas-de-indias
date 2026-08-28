// Buscador liviano: filtra un índice JSON generado (título/teaser/URL de
// cada capítulo) contra lo que se escribe en el input de la nav.
(function () {
  "use strict";
  const input = document.getElementById("global-search");
  const resultsEl = document.getElementById("search-results");
  if (!input || !resultsEl) return;

  let index = null;
  function ensureIndex(cb) {
    if (index) return cb();
    fetch(input.dataset.indexUrl)
      .then((r) => r.json())
      .then((data) => {
        index = data;
        cb();
      })
      .catch(() => {
        index = [];
        cb();
      });
  }

  function escapeHtml(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  const VENTANA = 90;
  function snippetPara(texto, qLower) {
    const textoLower = texto.toLowerCase();
    const pos = textoLower.indexOf(qLower);
    if (pos === -1) return escapeHtml(texto.slice(0, 160)) + "…";
    const ini = Math.max(0, pos - VENTANA);
    const fin = Math.min(texto.length, pos + qLower.length + VENTANA);
    const pre = escapeHtml(texto.slice(ini, pos));
    const mid = escapeHtml(texto.slice(pos, pos + qLower.length));
    const post = escapeHtml(texto.slice(pos + qLower.length, fin));
    return (ini > 0 ? "…" : "") + pre + "<mark>" + mid + "</mark>" + post + (fin < texto.length ? "…" : "");
  }

  function render(q) {
    const qLower = q.toLowerCase();
    const matches = index
      .filter((it) => it.heading.toLowerCase().includes(qLower) || it.texto.toLowerCase().includes(qLower))
      .slice(0, 30);
    if (!matches.length) {
      resultsEl.innerHTML = '<div class="empty">Sin resultados.</div>';
      resultsEl.style.display = "block";
      return;
    }
    resultsEl.innerHTML = matches
      .map(
        (m) => `
      <a class="result" href="${m.url}">
        <div class="rhead"><span class="rtitle">${escapeHtml(m.heading)}</span><span class="robra mono">${escapeHtml(m.obra_titulo)}</span></div>
        <div class="snippet">${snippetPara(m.texto, qLower)}</div>
      </a>`
      )
      .join("");
    resultsEl.style.display = "block";
  }

  input.addEventListener("input", () => {
    const q = input.value.trim();
    if (!q) {
      resultsEl.style.display = "none";
      resultsEl.innerHTML = "";
      return;
    }
    ensureIndex(() => render(q));
  });

  document.addEventListener("click", (e) => {
    if (e.target !== input && !resultsEl.contains(e.target)) resultsEl.style.display = "none";
  });
})();
