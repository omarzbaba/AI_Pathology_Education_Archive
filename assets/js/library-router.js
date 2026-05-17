/*
 * Library router — loads + renders Markdown content into library.html.
 *
 * URL pattern:    library.html#/<path-relative-to-repo-root>
 * Examples:
 *   library.html#/library/pillar-1-self-education/index
 *   library.html#/library/pillar-2-teaching/prompts/case-vignette-pgy
 *   library.html#/docs/guardrails
 *
 * Security:
 *   - marked.js parses Markdown to HTML
 *   - DOMPurify sanitizes the HTML before we inject it into the page
 *     (NEVER inject raw marked output — Markdown can embed raw HTML)
 *   - Both libraries are vendored under /assets/vendor/ with SRI hashes
 *     on the <script> tags in library.html — no runtime CDN dependency
 *
 * Frontmatter:
 *   The first block delimited by `---` ... `---` is parsed as YAML-ish
 *   key/value pairs (simple, line-based, no nesting). Recognized keys
 *   surface as a metadata card above the rendered content.
 */

(function () {
  "use strict";

  const contentEl = document.getElementById("library-content");

  // -------------------------------------------------------------------------
  // Routing
  // -------------------------------------------------------------------------

  function parseHash() {
    let h = window.location.hash || "";
    if (h.startsWith("#")) h = h.slice(1);
    if (h.startsWith("/")) h = h.slice(1);
    // Resolve dot-segments and disallow escaping the site root
    const parts = [];
    for (const seg of h.split("/")) {
      if (!seg || seg === ".") continue;
      if (seg === "..") { if (parts.length) parts.pop(); continue; }
      // Allow only safe path characters
      if (!/^[A-Za-z0-9_\-]+$/.test(seg)) return null;
      parts.push(seg);
    }
    if (parts.length === 0) return null;
    return parts.join("/") + ".md";
  }

  async function load() {
    const path = parseHash();
    if (!path) {
      renderError("No document selected. Pick a section from the navigation.");
      return;
    }
    try {
      const res = await fetch(path, { cache: "no-store" });
      if (!res.ok) {
        renderError("That document could not be found (" + res.status + ").");
        return;
      }
      const text = await res.text();
      render(text, path);
    } catch (err) {
      renderError("Failed to load: " + (err && err.message ? err.message : "unknown error"));
    }
  }

  // -------------------------------------------------------------------------
  // Frontmatter parsing — minimal, line-based, no YAML library needed
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
      // Strip surrounding quotes if present
      if ((v.startsWith('"') && v.endsWith('"')) ||
          (v.startsWith("'") && v.endsWith("'"))) {
        v = v.slice(1, -1);
      }
      // Strip a bracketed list like [a, b, c] into comma-separated form
      if (v.startsWith("[") && v.endsWith("]")) {
        v = v.slice(1, -1).trim();
      }
      data[m[1]] = v;
    }
    return { data, body: after };
  }

  // -------------------------------------------------------------------------
  // Render
  // -------------------------------------------------------------------------

  function escapeHtml(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }

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

  function setPageTitle(data, fallback) {
    const title = data.title || fallback;
    if (title) document.title = title + " — AI in Pathology Education";
  }

  function render(text, path) {
    const { data, body } = parseFrontmatter(text);
    setPageTitle(data, path);

    if (!window.marked || !window.DOMPurify) {
      renderError("Renderer not loaded.");
      return;
    }

    const rawHtml = window.marked.parse(body, { headerIds: true, mangle: false });
    const cleanHtml = window.DOMPurify.sanitize(rawHtml, {
      USE_PROFILES: { html: true },
      ADD_ATTR: ["target", "rel"]
    });

    let heading = "";
    if (data.title) {
      heading = '<h1>' + escapeHtml(data.title) + '</h1>';
    }
    contentEl.innerHTML = heading + buildMetaCard(data) + cleanHtml;

    // External links open in a new tab with safe rel attributes
    contentEl.querySelectorAll("a[href]").forEach((a) => {
      const href = a.getAttribute("href") || "";
      if (/^https?:\/\//i.test(href)) {
        a.setAttribute("target", "_blank");
        a.setAttribute("rel", "noopener noreferrer");
      }
    });

    addCopyButtons();
    window.scrollTo({ top: 0, behavior: "instant" });
  }

  function renderError(msg) {
    contentEl.innerHTML =
      '<p class="form-status form-status--error">' + escapeHtml(msg) + "</p>" +
      '<p>Return to the <a href="thank-you.html">library home</a>.</p>';
  }

  // -------------------------------------------------------------------------
  // Copy-to-clipboard buttons on code blocks
  // -------------------------------------------------------------------------

  function addCopyButtons() {
    contentEl.querySelectorAll("pre").forEach((pre) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.textContent = "Copy";
      btn.className = "copy-btn";
      btn.setAttribute("aria-label", "Copy code to clipboard");
      btn.style.cssText =
        "position:absolute;top:0.5rem;right:0.5rem;" +
        "font-size:0.75rem;padding:0.25rem 0.5rem;" +
        "background:var(--color-navy);color:#fff;border:0;border-radius:2px;" +
        "cursor:pointer;font-family:var(--font-sans);";
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
