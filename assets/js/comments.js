// Prototipo: comentarios al margen, anclados a una frase exacta del texto
// con una línea punteada del color del autor/origen. Solo corre en páginas
// que declaran <aside class="comments-rail" data-comments-url="..."> (por
// ahora, a mano en _layouts/capitulo.html solo para colon-cartas/000 — ver
// la nota ahí, es un test puntual, no un feature general del sitio todavía).
//
// Cada entrada del JSON de comentarios tiene: anchor (frase a buscar,
// primera coincidencia nada más), origen ("original" | "editor"), autor,
// color (hex), texto. Los de origen "original" son notas que ya estaban en
// la edición (ej. Navarrete, 1892); los de "editor" son de un colaborador
// de este proyecto, identificado por su firma.
(function () {
  "use strict";

  function escapeReg(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  // Busca la primera aparición de `anchorText` entre los nodos de texto de
  // `body` y la envuelve en un <mark class="comment-anchor">. No reprocesa
  // el HTML como string (mismo criterio que tag-entities.js) para no romper
  // el markup que ya generó kramdown ni el etiquetado de entidades.
  function wrapAnchor(body, anchorText, color, idx) {
    const walker = document.createTreeWalker(body, NodeFilter.SHOW_TEXT, null);
    const re = new RegExp(escapeReg(anchorText));
    let node;
    while ((node = walker.nextNode())) {
      const text = node.nodeValue;
      const m = re.exec(text);
      if (!m) continue;
      const frag = document.createDocumentFragment();
      if (m.index > 0) frag.appendChild(document.createTextNode(text.slice(0, m.index)));
      const mark = document.createElement("mark");
      mark.className = "comment-anchor";
      mark.style.setProperty("--comment-color", color);
      mark.dataset.commentIdx = String(idx);
      mark.textContent = m[0];
      frag.appendChild(mark);
      const rest = text.slice(m.index + m[0].length);
      if (rest) frag.appendChild(document.createTextNode(rest));
      node.parentNode.replaceChild(frag, node);
      return mark;
    }
    return null;
  }

  // Posiciona conectores y cajas de comentario en el margen. Las cajas se
  // empujan hacia abajo si se superponen con la anterior (los conectores
  // se quedan apuntando a la altura real del ancla en el texto, así que si
  // una caja se empuja, el punteado deja de ser perfectamente horizontal —
  // simplificación aceptada para este test, no un leader-line completo).
  function layout(rail, anchors, comments) {
    rail.innerHTML = "";
    const railRect = rail.getBoundingClientRect();
    const boxes = [];
    anchors.forEach((anchorEl, i) => {
      if (!anchorEl) return;
      const comment = comments[i];
      const rect = anchorEl.getBoundingClientRect();
      const anchorTop = rect.top - railRect.top + rect.height / 2;

      const connector = document.createElement("div");
      connector.className = "comment-connector";
      connector.style.setProperty("--comment-color", comment.color);
      connector.style.top = anchorTop + "px";
      rail.appendChild(connector);

      const box = document.createElement("div");
      box.className = "comment-box";
      box.style.setProperty("--comment-color", comment.color);
      const autor = document.createElement("span");
      autor.className = "cb-autor";
      autor.textContent = (comment.origen === "original" ? "Nota original · " : "Editor · ") + comment.autor;
      const texto = document.createElement("p");
      texto.textContent = comment.texto;
      box.appendChild(autor);
      box.appendChild(texto);
      rail.appendChild(box);
      boxes.push({ box: box, top: anchorTop });
    });

    // Segunda pasada: ahora que las cajas están en el DOM se puede medir su
    // altura real y evitar que se superpongan, empujando hacia abajo.
    let prevBottom = -Infinity;
    const gap = 14;
    boxes.forEach((b) => {
      let top = Math.max(b.top, prevBottom + gap);
      b.box.style.top = top + "px";
      prevBottom = top + b.box.getBoundingClientRect().height;
    });
  }

  function run() {
    const rail = document.querySelector(".comments-rail[data-comments-url]");
    const body = document.getElementById("dr-body");
    if (!rail || !body) return;
    fetch(rail.dataset.commentsUrl)
      .then((r) => r.json())
      .then((comments) => {
        const anchors = comments.map((c) => wrapAnchor(body, c.anchor, c.color));
        const relayout = () => layout(rail, anchors, comments);
        relayout();
        window.addEventListener("resize", relayout);
        if (document.fonts && document.fonts.ready) document.fonts.ready.then(relayout);
      })
      .catch(() => {});
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
  else run();
})();
