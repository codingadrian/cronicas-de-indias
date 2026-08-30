// Comentarios al margen: anclados a una frase exacta del texto, con una
// línea punteada del color del autor/origen. Se reparten en dos rieles,
// uno a cada lado del texto (1º comentario a la derecha, 2º a la
// izquierda, 3º a la derecha...) para no apilar todos del mismo lado en
// capítulos con muchos comentarios juntos. Corre en cualquier página que
// declare <aside class="comments-rail comments-rail-right"
// data-comments-url="..."> (y opcionalmente su par
// "comments-rail-left" sin data-url, para el lado izquierdo), puesto ahí
// por _layouts/capitulo.html cuando `page.tiene_comentarios` es true — ese
// campo lo pone scripts/generar_sitio.py, que también genera el JSON de
// comentarios de cada capítulo parseando la sintaxis en
// sources/<obra>/texto-limpio/*.md (ver la función procesar_comentarios ahí,
// y la nota de sintaxis en CLAUDE.md).
//
// Cada entrada del JSON tiene: anchor (frase a buscar), ocurrencia (qué
// aparición de esa frase en el texto final es esta — la misma frase puede
// repetirse, así que no alcanza con "la primera que aparezca"), origen
// ("original" | "editor"), autor, color (hex), texto.
(function () {
  "use strict";

  function escapeReg(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  // Busca la aparición número `ocurrencia` (0-based) de `anchorText` entre
  // TODOS los nodos de texto de `body`, contando en orden de documento, y la
  // envuelve en un <mark class="comment-anchor">. Contar de cero en cada
  // llamada (en vez de arrancar donde quedó la anterior) es a propósito:
  // envolver una coincidencia previa no cambia el contenido de texto, solo
  // lo envuelve en una etiqueta, así que recontar siempre da la posición
  // correcta sin importar qué otros comentarios ya se procesaron. No
  // reprocesa el HTML como string (mismo criterio que tag-entities.js) para
  // no romper el markup que ya generó kramdown.
  function wrapAnchor(body, anchorText, color, idx, ocurrencia) {
    if (!anchorText) return null;
    const walker = document.createTreeWalker(body, NodeFilter.SHOW_TEXT, null);
    const re = new RegExp(escapeReg(anchorText), "g");
    let node;
    let contador = 0;
    while ((node = walker.nextNode())) {
      const text = node.nodeValue;
      re.lastIndex = 0;
      let m;
      while ((m = re.exec(text))) {
        if (contador === ocurrencia) {
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
        contador++;
      }
    }
    return null;
  }

  // Llena UN riel con sus cajas/conectores y evita que se superpongan
  // empujando hacia abajo (los conectores se quedan apuntando a la altura
  // real del ancla en el texto, así que si una caja se empuja, el punteado
  // deja de ser perfectamente horizontal — simplificación aceptada, no es
  // un leader-line completo).
  function layoutRail(rail, items) {
    rail.innerHTML = "";
    const railRect = rail.getBoundingClientRect();
    const boxes = [];
    items.forEach(({ anchorEl, comment }) => {
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

  // Reparte los comentarios alternando de lado (1º derecha, 2º izquierda,
  // 3º derecha...) para no apilar todos del mismo lado en capítulos con
  // muchos comentarios seguidos — cada lado evita superposición solo
  // contra sí mismo, son columnas independientes. Si el riel izquierdo
  // existe en el DOM pero está oculto por CSS (pantalla angosta, ver
  // main.css), NO hay que seguir mandándole la mitad de los comentarios
  // — desaparecerían en silencio. En ese caso todo va al derecho.
  function layout(railLeft, railRight, anchors, comments) {
    const izquierdaVisible = !!railLeft && getComputedStyle(railLeft).display !== "none";
    const izquierda = [];
    const derecha = [];
    anchors.forEach((anchorEl, i) => {
      if (!anchorEl) return;
      const item = { anchorEl: anchorEl, comment: comments[i] };
      if (izquierdaVisible && i % 2 !== 0) izquierda.push(item);
      else derecha.push(item);
    });
    if (railRight) layoutRail(railRight, derecha);
    if (railLeft) layoutRail(railLeft, izquierda);
  }

  function run() {
    const railRight = document.querySelector(".comments-rail-right[data-comments-url]");
    const railLeft = document.querySelector(".comments-rail-left");
    const body = document.getElementById("dr-body");
    if (!railRight || !body) return;
    fetch(railRight.dataset.commentsUrl)
      .then((r) => r.json())
      .then((comments) => {
        const anchors = comments.map((c, idx) => wrapAnchor(body, c.anchor, c.color, idx, c.ocurrencia || 0));
        const relayout = () => layout(railLeft, railRight, anchors, comments);
        relayout();
        window.addEventListener("resize", relayout);
        if (document.fonts && document.fonts.ready) document.fonts.ready.then(relayout);
      })
      .catch(() => {});
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
  else run();
})();
