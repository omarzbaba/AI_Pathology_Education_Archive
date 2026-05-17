/*
 * Personalized greeting on thank-you.html.
 * Reads the user's first name from localStorage (set by access-gate.js
 * after a successful form submission) and updates the greeting element.
 *
 * Defensive: caps length, strips anything that isn't a letter, space,
 * hyphen, or apostrophe. Fails silently in private-browsing mode.
 */

(function () {
  try {
    const raw = localStorage.getItem("companion_access_granted");
    if (!raw) return;
    const data = JSON.parse(raw);
    if (!data || !data.name) return;
    let first = String(data.name).trim().split(/\s+/)[0];
    first = first.slice(0, 40).replace(/[^A-Za-z\-' ]/g, "");
    if (!first) return;
    const el = document.getElementById("greeting");
    if (el) el.textContent = "Welcome, " + first + ".";
  } catch (e) {
    /* silently ignore */
  }
})();
