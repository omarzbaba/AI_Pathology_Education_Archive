/*
 * Search widget — site-wide search across prompts, tutorials, examples, docs.
 *
 * Lazy-loads library/search-index.json on first focus. Pure client-side
 * substring + tag matching with simple relevance scoring. No external
 * libraries, no network calls beyond the one-time index load.
 *
 * Mount: pages include this script and a <div id="search-mount"></div> in
 * the nav. The widget injects an input + dropdown into the mount.
 */

(function () {
  const MOUNT_ID = "search-mount";
  let index = null;       // loaded on first focus
  let indexLoading = null; // a Promise
  let currentResults = [];
  let activeIndex = -1;

  function injectStyles() {
    if (document.getElementById("search-widget-styles")) return;
    const css = `
      .swx {
        position: relative;
        font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
      }
      .swx__input {
        width: 260px;
        max-width: 100%;
        padding: 0.45rem 0.7rem 0.45rem 2rem;
        border: 1px solid var(--color-rule, #E4E2DC);
        border-radius: 4px;
        font-size: 0.92rem;
        font-family: inherit;
        background: #fff url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%237A1C28' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'><circle cx='11' cy='11' r='8'/><line x1='21' y1='21' x2='16.65' y2='16.65'/></svg>") 0.55rem center / 14px no-repeat;
        color: var(--color-navy, #14213D);
      }
      .swx__input:focus {
        outline: 2px solid var(--color-burgundy, #7A1C28);
        outline-offset: -1px;
        border-color: var(--color-burgundy, #7A1C28);
      }
      .swx__panel {
        position: absolute;
        top: calc(100% + 6px);
        right: 0;
        width: min(580px, 90vw);
        max-height: 70vh;
        overflow-y: auto;
        background: #fff;
        border: 1px solid var(--color-rule, #E4E2DC);
        border-radius: 4px;
        box-shadow: 0 12px 36px rgba(20,33,61,0.18);
        z-index: 1000;
        padding: 8px 0;
      }
      .swx__hint {
        padding: 0.6rem 1rem;
        color: var(--color-muted, #6B6F7A);
        font-size: 0.88rem;
      }
      .swx__group {
        padding: 0.4rem 1rem 0.2rem;
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--color-burgundy, #7A1C28);
        font-weight: 600;
      }
      .swx__item {
        display: block;
        padding: 0.55rem 1rem;
        text-decoration: none;
        color: var(--color-navy, #14213D);
        border-left: 3px solid transparent;
        cursor: pointer;
      }
      .swx__item:hover,
      .swx__item--active {
        background: var(--color-paper, #FAFAF7);
        border-left-color: var(--color-burgundy, #7A1C28);
      }
      .swx__title {
        font-size: 0.95rem;
        font-weight: 500;
        margin: 0 0 2px 0;
        line-height: 1.3;
      }
      .swx__snippet {
        font-size: 0.82rem;
        color: var(--color-muted, #6B6F7A);
        line-height: 1.4;
        margin: 0;
      }
      .swx__meta {
        font-size: 0.72rem;
        color: var(--color-muted, #6B6F7A);
        margin-top: 3px;
        display: flex;
        gap: 0.6rem;
        flex-wrap: wrap;
      }
      .swx__badge {
        display: inline-block;
        font-size: 0.7rem;
        padding: 1px 6px;
        border-radius: 3px;
        background: var(--color-rule, #E4E2DC);
        color: var(--color-navy, #14213D);
        text-transform: uppercase;
        letter-spacing: 0.04em;
        font-weight: 500;
      }
      .swx__badge--beginner { background: #E8F1EC; color: #1F5C3B; }
      .swx__badge--intermediate { background: #FFF4DA; color: #8B5E00; }
      .swx__badge--advanced { background: #FBECEE; color: #8B1A2B; }
      .swx__empty {
        padding: 1rem;
        color: var(--color-muted, #6B6F7A);
        text-align: center;
        font-style: italic;
        font-size: 0.9rem;
      }
      mark.swx__mark {
        background: #fff4da;
        color: inherit;
        padding: 0 1px;
        border-radius: 2px;
      }
      @media (max-width: 700px) {
        .swx__input { width: 100%; }
        .swx__panel { width: 96vw; right: -10px; }
      }
    `;
    const style = document.createElement("style");
    style.id = "search-widget-styles";
    style.textContent = css;
    document.head.appendChild(style);
  }

  function mount() {
    const target = document.getElementById(MOUNT_ID);
    if (!target || target.dataset.swxMounted) return;
    target.dataset.swxMounted = "1";

    target.innerHTML =
      '<div class="swx">' +
        '<input type="search" class="swx__input" id="swx-input" placeholder="Search prompts, tutorials…" autocomplete="off" spellcheck="false">' +
      '</div>';

    const input = target.querySelector("#swx-input");
    let panel = null;

    input.addEventListener("focus", async () => {
      if (!index) await loadIndex();
      openPanel();
      if (input.value.trim()) runSearch(input.value);
    });

    input.addEventListener("input", () => {
      if (!index) return;
      runSearch(input.value);
    });

    input.addEventListener("keydown", (e) => {
      if (!panel) return;
      if (e.key === "ArrowDown") { e.preventDefault(); moveActive(1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); moveActive(-1); }
      else if (e.key === "Enter")    { e.preventDefault(); openActive(); }
      else if (e.key === "Escape")   { closePanel(); input.blur(); }
    });

    document.addEventListener("click", (e) => {
      if (!panel) return;
      if (e.target === input || target.contains(e.target)) return;
      closePanel();
    });

    function openPanel() {
      if (panel) return;
      panel = document.createElement("div");
      panel.className = "swx__panel";
      panel.innerHTML = '<p class="swx__hint">Type to search prompts, tutorials, examples, docs…</p>';
      target.querySelector(".swx").appendChild(panel);
    }
    function closePanel() {
      if (panel) panel.remove();
      panel = null;
      activeIndex = -1;
    }
    function moveActive(delta) {
      if (!currentResults.length) return;
      activeIndex = (activeIndex + delta + currentResults.length) % currentResults.length;
      renderResults();
    }
    function openActive() {
      const r = currentResults[activeIndex >= 0 ? activeIndex : 0];
      if (r) window.location.href = toHref(r);
    }

    window._swx = { runSearch, openPanel };

    function runSearch(rawQuery) {
      const q = (rawQuery || "").trim();
      if (!panel) openPanel();
      if (!q) {
        panel.innerHTML = '<p class="swx__hint">Type to search prompts, tutorials, examples, docs…</p>';
        currentResults = [];
        return;
      }
      currentResults = scoreAndRank(q, index);
      activeIndex = currentResults.length ? 0 : -1;
      renderResults(q);
    }

    function renderResults(query) {
      if (!panel) return;
      if (!currentResults.length) {
        panel.innerHTML = '<p class="swx__empty">No matches. Try a different word.</p>';
        return;
      }
      const groups = groupByType(currentResults.slice(0, 30));
      let html = "";
      const groupOrder = ["prompt", "tutorial", "example", "doc", "how-to-landing"];
      const groupLabels = {
        prompt: "Prompts",
        tutorial: "Tutorials",
        example: "Worked examples",
        doc: "Documents",
        "how-to-landing": "Landing pages"
      };
      let globalIdx = 0;
      for (const type of groupOrder) {
        if (!groups[type]) continue;
        html += '<div class="swx__group">' + groupLabels[type] + ' (' + groups[type].length + ')</div>';
        for (const r of groups[type]) {
          const isActive = (globalIdx === activeIndex);
          html += renderItem(r, isActive, query);
          globalIdx++;
        }
      }
      panel.innerHTML = html;
      // Re-wire click handlers
      panel.querySelectorAll(".swx__item").forEach((el, idx) => {
        el.addEventListener("mouseenter", () => {
          activeIndex = idx;
          panel.querySelectorAll(".swx__item").forEach((e2, i2) => {
            e2.classList.toggle("swx__item--active", i2 === idx);
          });
        });
        el.addEventListener("click", (e) => {
          e.preventDefault();
          window.location.href = el.getAttribute("href");
        });
      });
    }

    function renderItem(r, isActive, query) {
      const href = toHref(r);
      const badges = [];
      if (r.difficulty) {
        const cls = "swx__badge--" + r.difficulty.replace(/[^a-z]/g, "");
        badges.push('<span class="swx__badge ' + cls + '">' + escapeHtml(r.difficulty) + '</span>');
      }
      if (r.pillar) {
        const p = r.pillar.replace(/pillar-\d+-/, "").replace(/-/g, " ");
        badges.push('<span class="swx__badge">' + escapeHtml(p) + '</span>');
      }
      if (r.section) {
        badges.push('<span class="swx__badge">' + escapeHtml(r.section) + '</span>');
      }
      const title = highlight(r.title || "", query);
      const snippet = highlight(r.snippet || "", query);
      return (
        '<a class="swx__item' + (isActive ? ' swx__item--active' : '') + '" href="' + escapeAttr(href) + '">' +
          '<p class="swx__title">' + title + '</p>' +
          (snippet ? '<p class="swx__snippet">' + snippet + '</p>' : '') +
          (badges.length ? '<div class="swx__meta">' + badges.join("") + '</div>' : '') +
        '</a>'
      );
    }
  }

  // -------- Index loading --------

  function loadIndex() {
    if (index) return Promise.resolve(index);
    if (indexLoading) return indexLoading;
    // Determine the right path for search-index.json (relative to root)
    indexLoading = fetch("library/search-index.json", { cache: "no-store" })
      .then(r => r.ok ? r.json() : [])
      .then(j => { index = j; return j; })
      .catch(_ => { index = []; return []; });
    return indexLoading;
  }

  // -------- Scoring --------

  function scoreAndRank(query, entries) {
    if (!entries || !entries.length) return [];
    const words = query.toLowerCase().split(/\s+/).filter(Boolean);
    const scored = [];
    for (const e of entries) {
      let score = 0;
      const titleLc = (e.title || "").toLowerCase();
      const snippetLc = (e.snippet || "").toLowerCase();
      const tagsLc = (e.tags || "").toLowerCase();
      const sectionLc = (e.section || "").toLowerCase();
      for (const w of words) {
        if (titleLc.includes(w))   score += 8;
        if (titleLc.startsWith(w)) score += 4;
        if (snippetLc.includes(w)) score += 2;
        if (tagsLc.includes(w))    score += 3;
        if (sectionLc.includes(w)) score += 2;
      }
      // Type bias: prompts and tutorials are usually what people want
      if (e.type === "prompt") score *= 1.05;
      if (e.type === "tutorial") score *= 1.05;
      if (score > 0) scored.push({ entry: e, score });
    }
    scored.sort((a, b) => b.score - a.score);
    return scored.map(s => s.entry);
  }

  function groupByType(results) {
    const g = {};
    for (const r of results) {
      const t = r.type || "doc";
      if (!g[t]) g[t] = [];
      g[t].push(r);
    }
    return g;
  }

  // -------- Helpers --------

  function toHref(r) {
    return "library.html#/" + r.path;
  }
  function escapeHtml(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }
  function escapeAttr(s) { return escapeHtml(s); }
  function highlight(text, query) {
    const safe = escapeHtml(text);
    if (!query) return safe;
    const words = query.toLowerCase().split(/\s+/).filter(w => w.length > 1);
    if (!words.length) return safe;
    const re = new RegExp("(" + words.map(escapeRegex).join("|") + ")", "gi");
    return safe.replace(re, '<mark class="swx__mark">$1</mark>');
  }
  function escapeRegex(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }

  // -------- Boot --------

  function boot() {
    injectStyles();
    mount();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
