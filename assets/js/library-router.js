/*
 * Library router — loads + renders content into library.html.
 *
 * Two view modes:
 *
 * 1. PILLAR INDEX view: when the hash points to a pillar index page
 *    (e.g., #/library/pillar-1-self-education/index), renders a card
 *    grid from library/manifest.json instead of rendering the index.md.
 *    Cards show category icon, title, brief intent, difficulty pill,
 *    time pill, and best-model badge.
 *
 * 2. DETAIL view: when the hash points to any other .md file, renders
 *    the markdown content (frontmatter → metadata card, body → prose).
 *    Prompt detail pages get a prominent "Copy prompt" button at the
 *    top of the page (above the body, in addition to the per-code-block
 *    copy buttons added by addCopyButtons()).
 *
 * Security: marked.js parses Markdown to HTML; DOMPurify sanitizes
 * before injection. Both vendored under /assets/vendor/ with SRI.
 */

(function () {
  "use strict";

  const contentEl = document.getElementById("library-content");
  let manifest = null;

  // -------------------------------------------------------------------------
  // Routing
  // -------------------------------------------------------------------------

  function parseHash() {
    let h = window.location.hash || "";
    if (h.startsWith("#")) h = h.slice(1);
    if (h.startsWith("/")) h = h.slice(1);
    const parts = [];
    for (const seg of h.split("/")) {
      if (!seg || seg === ".") continue;
      if (seg === "..") { if (parts.length) parts.pop(); continue; }
      if (!/^[A-Za-z0-9_\-]+$/.test(seg)) return null;
      parts.push(seg);
    }
    if (parts.length === 0) return null;
    return parts.join("/") + ".md";
  }

  function isPillarIndexPath(path) {
    // Match library/pillar-X-Y/index.md
    return /^library\/pillar-[^\/]+\/index\.md$/.test(path);
  }

  function pillarSlugFromPath(path) {
    const m = path.match(/^library\/(pillar-[^\/]+)\/index\.md$/);
    return m ? m[1] : null;
  }

  async function load() {
    const path = parseHash();
    if (!path) {
      renderError("No document selected. Pick a section from the navigation.");
      return;
    }

    // Lazy-load manifest the first time we need it
    if (!manifest) {
      try {
        const res = await fetch("library/manifest.json", { cache: "no-store" });
        if (res.ok) manifest = await res.json();
      } catch (_) { /* fall through to detail render */ }
    }

    if (isPillarIndexPath(path) && manifest) {
      const slug = pillarSlugFromPath(path);
      const pillar = manifest.pillars.find((p) => p.slug === slug);
      if (pillar) {
        renderPillarCards(pillar);
        return;
      }
    }

    // Fall back to markdown detail view
    try {
      const res = await fetch(path, { cache: "no-store" });
      if (!res.ok) {
        renderError("That document could not be found (" + res.status + ").");
        return;
      }
      const text = await res.text();
      renderDetail(text, path);
    } catch (err) {
      renderError("Failed to load: " + (err && err.message ? err.message : "unknown error"));
    }
  }

  // -------------------------------------------------------------------------
  // Frontmatter parsing
  // -------------------------------------------------------------------------

  function parseFrontmatter(src) {
    if (!src.startsWith("---\n") && !src.startsWith("---\r\n")) {
      return { data: {}, body: src };
    }
    const end = src.indexOf("\n---", 4);
    if (end < 0) return { data: {}, body: src };
    const block = src.slice(4, end);
    const after = src.slice(end + 4).replace(/^\r?\n/, "");
    const data = {};
    for (const raw of block.split(/\r?\n/)) {
      const line = raw.trim();
      if (!line || line.startsWith("#")) continue;
      const m = line.match(/^([A-Za-z0-9_\-]+)\s*:\s*(.*)$/);
      if (!m) continue;
      let v = m[2].trim();
      if ((v.startsWith('"') && v.endsWith('"')) ||
          (v.startsWith("'") && v.endsWith("'"))) {
        v = v.slice(1, -1);
      }
      if (v.startsWith("[") && v.endsWith("]")) v = v.slice(1, -1).trim();
      data[m[1]] = v;
    }
    return { data, body: after };
  }

  function escapeHtml(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }

  function setPageTitle(title) {
    if (title) document.title = title + " — AI in Pathology Education";
  }

  // -------------------------------------------------------------------------
  // Category icons (inline SVG, stroke-based, monochrome — inherit color)
  // -------------------------------------------------------------------------

  const ICONS = {
    learn:    '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5h7a3 3 0 0 1 3 3v12a2 2 0 0 0-2-2H4z"/><path d="M20 5h-7a3 3 0 0 0-3 3v12a2 2 0 0 1 2-2h8z"/></svg>',
    drill:    '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/></svg>',
    read:     '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 4h9l5 5v11a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1z"/><path d="M14 4v6h6"/><path d="M8 14h8M8 18h8"/></svg>',
    image:    '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="10" r="6"/><circle cx="12" cy="10" r="2.5"/><path d="M9 19v2M15 19v2M7 21h10"/></svg>',
    teach:    '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="13" rx="1"/><path d="M8 21h8M12 17v4"/><path d="M7 8h10M7 12h7"/></svg>',
    assess:   '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="1"/><path d="M8 9l2 2 4-4M8 15l2 2 4-4"/></svg>',
    write:    '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h16"/><path d="M14 4l4 4-9 9H5v-4z"/></svg>',
    discuss:  '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 5h12a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2H9l-4 4z"/></svg>',
    plan:     '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="5" width="16" height="16" rx="1"/><path d="M4 10h16M9 3v4M15 3v4"/><circle cx="9" cy="15" r="1" fill="currentColor"/><circle cx="14" cy="15" r="1" fill="currentColor"/></svg>',
    template: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h9l4 4v14a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/><path d="M14 3v5h5"/><path d="M8 13h8M8 17h5"/></svg>',
    comms:    '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 6l9 7 9-7"/></svg>',
    debrief:  '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="4" width="12" height="17" rx="1"/><path d="M9 3h6v3H9z"/><path d="M9 11h6M9 15h6"/></svg>',
    notebook: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h11a2 2 0 0 1 2 2v14a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1z"/><path d="M14 4v6l-2-1.5L10 10V4"/><path d="M5 8H4M5 12H4M5 16H4"/></svg>',
  };

  // -------------------------------------------------------------------------
  // Pillar index — card grid view
  // -------------------------------------------------------------------------

  function difficultyClass(d) {
    return "pill pill--" + (
      d === "quick-win" ? "easy" :
      d === "intermediate" ? "mid" :
      d === "advanced" ? "hard" : "neutral"
    );
  }

  function modelShort(m) {
    if (!m) return "";
    // Strip "with paper attached" suffix for badge brevity (still in detail)
    return m.replace(/ with paper attached$/i, "");
  }

  function promptCardHtml(p) {
    const icon = ICONS[p.category] || ICONS.template;
    const href = "library.html#/" + p.path.replace(/\.md$/, "");
    return (
      '<a class="prompt-card" href="' + escapeHtml(href) + '">' +
        '<div class="prompt-card__icon" aria-hidden="true">' + icon + '</div>' +
        '<div class="prompt-card__body">' +
          '<h4 class="prompt-card__title">' + escapeHtml(p.title) + '</h4>' +
          '<p class="prompt-card__intent">' + escapeHtml(p.intent) + '</p>' +
          '<div class="prompt-card__meta">' +
            (p.difficulty ? '<span class="' + difficultyClass(p.difficulty) + '">' + escapeHtml(p.difficulty) + '</span>' : '') +
            (p.time_to_use ? '<span class="pill pill--time">' + escapeHtml(p.time_to_use) + '</span>' : '') +
            (p.visual === "multimodal" ? '<span class="pill pill--multimodal">multimodal</span>' : '') +
            (p.best_model ? '<span class="pill pill--model">' + escapeHtml(modelShort(p.best_model)) + '</span>' : '') +
          '</div>' +
        '</div>' +
      '</a>'
    );
  }

  function flagshipHtml(f) {
    if (!f) return "";
    const href = "library.html#/" + String(f.path || "").replace(/\.md$/, "");
    const meta = (f.meta || []).map(function (m) {
      return '<li>' + escapeHtml(m) + '</li>';
    }).join("");
    const arc = (f.arc || []).map(function (a) {
      return '<li>' + escapeHtml(a) + '</li>';
    }).join("");
    return (
      '<div class="flagship">' +
        '<p class="flagship__eyebrow">' + escapeHtml(f.eyebrow || "Start here \u00b7 Flagship worked example") + '</p>' +
        '<h2 class="flagship__title">' + escapeHtml(f.title || "") + '</h2>' +
        '<p class="flagship__premise">' + escapeHtml(f.premise || "") + '</p>' +
        (meta ? '<ul class="flagship__meta">' + meta + '</ul>' : '') +
        (arc ? '<ol class="arc">' + arc + '</ol>' : '') +
        '<p><a class="btn" href="' + escapeHtml(href) + '">' +
          escapeHtml(f.cta || "Walk through the example") + ' \u2192</a></p>' +
      '</div>'
    );
  }

  function renderPillarCards(pillar) {
    setPageTitle(pillar.title);
    const sectionsHtml = pillar.sections.map((s) =>
      '<section class="card-section">' +
        '<h3 class="card-section__title">' + escapeHtml(s.title) + '</h3>' +
        '<div class="prompt-card-grid">' +
          s.prompts.map(promptCardHtml).join("") +
        '</div>' +
      '</section>'
    ).join("");
    contentEl.innerHTML =
      '<h1>' + escapeHtml(pillar.title) + '</h1>' +
      '<p class="lead">' + escapeHtml(pillar.description) + '</p>' +
      flagshipHtml(pillar.flagship) +
      sectionsHtml;
    window.scrollTo({ top: 0, behavior: "instant" });
  }

  // -------------------------------------------------------------------------
  // Detail view — markdown render
  // -------------------------------------------------------------------------

  const META_LABELS = {
    pillar:          "Pillar",
    event_type:      "Event type",
    audience:        "Audience",
    difficulty:      "Difficulty",
    time_to_use:     "Time to use",
    visual:          "Format",
    tags:            "Tags",
    best_model:      "Best model",
    verified_models: "Verified on",
    last_updated:    "Updated"
  };

  function buildMetaCard(data) {
    const entries = [];
    for (const key of Object.keys(META_LABELS)) {
      if (data[key]) entries.push([META_LABELS[key], data[key]]);
    }
    if (!entries.length) return "";
    return '<dl class="meta-card">' +
      entries.map(([k, v]) =>
        "<dt>" + escapeHtml(k) + "</dt><dd>" + escapeHtml(v) + "</dd>"
      ).join("") +
    "</dl>";
  }

  function extractPromptText(body) {
    // Find the first code block under "## The prompt"
    const m = body.match(/## The prompt\s*\n+```\n([\s\S]*?)\n```/);
    return m ? m[1] : null;
  }

  function copyButtonHtml(text) {
    // The copy button is rendered as a separate top-of-page action.
    // The actual copying is wired up in addPromptCopyAction() to avoid
    // putting the prompt text in attribute strings.
    return (
      '<div class="prompt-actions">' +
        '<button type="button" class="btn-copy-prompt" id="copy-prompt-top">' +
          '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="11" height="11" rx="1"/><path d="M5 15V5a1 1 0 0 1 1-1h10"/></svg>' +
          '<span>Copy prompt</span>' +
        '</button>' +
      '</div>'
    );
  }

  function isPromptDetailPath(path) {
    return /^library\/pillar-[^\/]+\/prompts\/[^\/]+\.md$/.test(path)
        || /^library\/pillar-[^\/]+\/prompts\/[^\/]+\/[^\/]+\.md$/.test(path);
  }

  function renderDetail(text, path) {
    const { data, body } = parseFrontmatter(text);
    setPageTitle(data.title || path);

    if (!window.marked || !window.DOMPurify) {
      renderError("Renderer not loaded.");
      return;
    }

    const rawHtml = window.marked.parse(body, { headerIds: true, mangle: false });
    const cleanHtml = window.DOMPurify.sanitize(rawHtml, {
      USE_PROFILES: { html: true },
      ADD_ATTR: ["target", "rel"]
    });

    const heading = data.title ? '<h1>' + escapeHtml(data.title) + '</h1>' : '';
    const promptText = extractPromptText(body);
    const promptActions = promptText ? copyButtonHtml(promptText) : '';
    const engagementSlot = isPromptDetailPath(path)
      ? '<div id="engagement-slot"></div>'
      : '';

    contentEl.innerHTML =
      heading +
      buildMetaCard(data) +
      promptActions +
      cleanHtml +
      engagementSlot;

    if (promptText) wirePromptCopyAction(promptText);

    contentEl.querySelectorAll("a[href]").forEach((a) => {
      const href = a.getAttribute("href") || "";
      if (/^https?:\/\//i.test(href)) {
        a.setAttribute("target", "_blank");
        a.setAttribute("rel", "noopener noreferrer");
      }
    });

    addCopyButtons();

    // Lazy-load engagement (comments + votes) only for prompt detail pages
    if (isPromptDetailPath(path)) {
      // Strip the .md extension for the canonical prompt_path identifier
      const promptPath = path.replace(/\.md$/, "");
      import("./engagement.js")
        .then(({ renderEngagement }) =>
          renderEngagement(document.getElementById("engagement-slot"), promptPath))
        .catch((err) => console.warn("Engagement load failed:", err));
    }

    window.scrollTo({ top: 0, behavior: "instant" });
  }

  function wirePromptCopyAction(promptText) {
    const btn = document.getElementById("copy-prompt-top");
    if (!btn) return;
    btn.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(promptText);
        const label = btn.querySelector("span");
        const orig = label.textContent;
        label.textContent = "Copied";
        btn.classList.add("btn-copy-prompt--copied");
        // Analytics: copy event
        if (window.analytics) {
          const promptPath = (window.location.hash || "").replace(/^#\//, "");
          window.analytics.track("copy", { prompt_path: promptPath });
        }
        setTimeout(() => {
          label.textContent = orig;
          btn.classList.remove("btn-copy-prompt--copied");
        }, 2000);
      } catch (_) {
        btn.querySelector("span").textContent = "Copy failed";
      }
    });
  }

  function renderError(msg) {
    contentEl.innerHTML =
      '<p class="form-status form-status--error">' + escapeHtml(msg) + "</p>" +
      '<p>Return to the <a href="thank-you.html">library home</a>.</p>';
  }

  // -------------------------------------------------------------------------
  // Copy-to-clipboard buttons on inline code blocks
  // -------------------------------------------------------------------------

  function addCopyButtons() {
    contentEl.querySelectorAll("pre").forEach((pre) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.textContent = "Copy";
      btn.className = "copy-btn";
      btn.setAttribute("aria-label", "Copy code to clipboard");
      pre.style.position = "relative";
      btn.addEventListener("click", async () => {
        try {
          await navigator.clipboard.writeText(pre.innerText);
          btn.textContent = "Copied";
          setTimeout(() => (btn.textContent = "Copy"), 1500);
        } catch (_) {
          btn.textContent = "Failed";
        }
      });
      pre.appendChild(btn);
    });
  }

  // -------------------------------------------------------------------------
  // Boot
  // -------------------------------------------------------------------------

  window.addEventListener("hashchange", load);
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", load);
  } else {
    load();
  }
})();
