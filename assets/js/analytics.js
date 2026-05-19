/*
 * First-party analytics.
 *
 * Logs three event types to the Firestore `page_events` collection:
 *   - view   — page or hash-route loaded (auto-fired)
 *   - copy   — "Copy prompt" button clicked on a prompt detail page
 *   - search — user runs a search via the search widget
 *
 * No third parties; data lives entirely in your Firestore. Admin-only read.
 *
 * Lazy-loads Firebase on first event. Skip via body.analytics-suppress.
 */

(function () {
  const STORAGE_KEY_ACCESS = "companion_access_granted";
  const STORAGE_KEY_SESSION = "companion_session_id";

  let firebaseReady = null;
  let queue = [];
  let lastViewPath = null;

  // ---------- Helpers ----------

  function uuid4() {
    // Reasonable randomness; not cryptographic. Good enough for session IDs.
    const r = () => Math.floor(Math.random() * 0x100000000).toString(16).padStart(8, "0");
    return r() + "-" + r() + "-" + r() + "-" + r();
  }

  function getOrCreateSessionId() {
    try {
      let id = localStorage.getItem(STORAGE_KEY_SESSION);
      if (!id) {
        id = uuid4();
        localStorage.setItem(STORAGE_KEY_SESSION, id);
      }
      return id;
    } catch (_) {
      return uuid4(); // fall back to ephemeral if storage is blocked
    }
  }

  function getEmail() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY_ACCESS);
      if (!raw) return "";
      const parsed = JSON.parse(raw);
      return (parsed && parsed.email) ? String(parsed.email).slice(0, 254) : "";
    } catch (_) { return ""; }
  }

  function trunc(s, n) { return String(s == null ? "" : s).slice(0, n); }

  function currentPath() {
    // For SPA hash routes (library.html#/foo), include the hash.
    // For other pages, just the pathname.
    const path = window.location.pathname + window.location.hash;
    return trunc(path, 500);
  }

  // ---------- Firebase lazy-load ----------

  async function loadFirebase() {
    const [{ initializeApp, getApps }, { initializeAppCheck, ReCaptchaV3Provider }, fs, cfg] = await Promise.all([
      import("https://www.gstatic.com/firebasejs/10.12.5/firebase-app.js"),
      import("https://www.gstatic.com/firebasejs/10.12.5/firebase-app-check.js"),
      import("https://www.gstatic.com/firebasejs/10.12.5/firebase-firestore.js"),
      import("./firebase-config.js")
    ]);

    let app = getApps().find((a) => a.name === "analytics");
    if (!app) {
      app = initializeApp(cfg.firebaseConfig, "analytics");
      try {
        initializeAppCheck(app, {
          provider: new ReCaptchaV3Provider(cfg.appCheckSiteKey),
          isTokenAutoRefreshEnabled: true
        });
      } catch (_) { /* token may already be init on default app — non-fatal */ }
    }
    const db = fs.getFirestore(app);
    return { db, fs };
  }

  // ---------- Track ----------

  async function track(type, payload) {
    if (document.body && document.body.classList.contains("analytics-suppress")) return;
    if (!type) return;

    const event = {
      type: type,
      session_id: getOrCreateSessionId(),
      path: currentPath(),
      email: getEmail(),
      referrer: trunc(document.referrer || "", 500),
      query: trunc((payload && payload.query) || "", 200).replace(/[\r\n\t]+/g, " "),
      prompt_path: trunc((payload && payload.prompt_path) || "", 300)
    };

    queue.push(event);

    if (!firebaseReady) firebaseReady = loadFirebase();
    try {
      const { db, fs } = await firebaseReady;
      while (queue.length > 0) {
        const e = queue.shift();
        try {
          await fs.addDoc(fs.collection(db, "page_events"), {
            timestamp: fs.serverTimestamp(),
            ...e
          });
        } catch (err) {
          // Silently swallow — analytics must not break the site
          console.warn("analytics write failed:", err && err.code);
          break; // stop draining queue on error to avoid hammering
        }
      }
    } catch (_) { /* Firebase init failed; ignore */ }
  }

  // ---------- Auto-fire page view ----------

  function autoTrackView() {
    const p = currentPath();
    if (p === lastViewPath) return; // dedupe rapid double-fires
    lastViewPath = p;
    track("view");
  }

  function boot() {
    autoTrackView();
    // For SPA hash routing, also track on hashchange
    window.addEventListener("hashchange", autoTrackView);
  }

  // ---------- Expose API ----------

  window.analytics = {
    track: track,
    view: autoTrackView
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
