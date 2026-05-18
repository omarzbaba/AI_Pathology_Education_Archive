/*
 * Access gate — handles the contact-capture form on index.html.
 *
 * Security model:
 *   - Firebase App Check (reCAPTCHA v3) attaches a token to every request.
 *     With App Check enforced for Firestore, bots and direct API calls
 *     without a valid token are rejected before rules even run.
 *   - Firestore rules (firebase/firestore.rules) validate shape,
 *     length caps, role enum, and require the timestamp to be the
 *     server time. Client validation here is defense-in-depth only.
 *   - The form is a courtesy gate for tracking and personalization,
 *     not real access control. Library content is public on GitHub.
 */

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-app.js";
import {
  initializeAppCheck,
  ReCaptchaV3Provider
} from "https://www.gstatic.com/firebasejs/10.12.5/firebase-app-check.js";
import {
  getFirestore,
  collection,
  addDoc,
  serverTimestamp
} from "https://www.gstatic.com/firebasejs/10.12.5/firebase-firestore.js";
import {
  getFunctions,
  httpsCallable
} from "https://www.gstatic.com/firebasejs/10.12.5/firebase-functions.js";

import { firebaseConfig, appCheckSiteKey } from "./firebase-config.js";

// ---------------------------------------------------------------------------
// Returning-visitor short-circuit
// ---------------------------------------------------------------------------
// If this browser already has an access-granted flag, skip the form and show
// a "Welcome back" panel instead. The library is just a click away, no
// re-submission needed. Clearing localStorage (e.g. private window) brings
// the form back.

(function maybeShowWelcomeBack() {
  let granted = null;
  try {
    const raw = localStorage.getItem("companion_access_granted");
    if (raw) granted = JSON.parse(raw);
  } catch (_) { /* malformed JSON — ignore, show form */ }

  if (!granted || !granted.name) return;

  const section = document.querySelector(".form-section");
  if (!section) return;

  const safeName = String(granted.name).replace(/[<>&"']/g, "");
  const firstName = safeName.split(/\s+/)[0] || safeName;

  section.innerHTML =
    '<h2>Welcome back, ' + firstName + '</h2>' +
    '<p class="form-section__intro">' +
      'You already have access on this browser. Jump straight in.' +
    '</p>' +
    '<p style="margin-top: 1.5rem;">' +
      '<a href="thank-you.html" class="btn" style="display:inline-block; text-decoration:none;">Enter the library</a>' +
    '</p>' +
    '<p class="form-section__intro" style="font-size: 0.9rem; margin-top: 1.5rem;">' +
      'Not you, or want to use a different email? ' +
      '<a href="#" id="reset-identity">Clear and start over</a>.' +
    '</p>';

  const reset = document.getElementById("reset-identity");
  if (reset) {
    reset.addEventListener("click", (e) => {
      e.preventDefault();
      try { localStorage.removeItem("companion_access_granted"); } catch (_) {}
      window.location.reload();
    });
  }
})();

// ---------------------------------------------------------------------------
// Firebase init
// ---------------------------------------------------------------------------

let db;
let functions;
let initError = null;

try {
  const app = initializeApp(firebaseConfig);
  initializeAppCheck(app, {
    provider: new ReCaptchaV3Provider(appCheckSiteKey),
    isTokenAutoRefreshEnabled: true
  });
  db = getFirestore(app);
  functions = getFunctions(app);
} catch (err) {
  initError = err;
  // Don't throw — let the form render and show a sensible error on submit.
  // This keeps the page usable during local development before Firebase is set up.
  console.warn("Firebase init failed (expected during Phase 3 setup):", err);
}

// ---------------------------------------------------------------------------
// Returning-visitor mini-form (email shortcut)
// ---------------------------------------------------------------------------

(function wireReturningForm() {
  const form = document.getElementById("returning-form");
  if (!form) return; // not rendered (already-granted branch above ran)

  const emailEl = document.getElementById("returning-email");
  const btn = document.getElementById("returning-submit");
  const statusEl = document.getElementById("returning-status");

  function setStatus(msg, kind) {
    statusEl.style.color = kind === "error" ? "var(--color-error, #8B1A2B)"
                          : kind === "success" ? "var(--color-success, #1F5C3B)"
                          : "var(--color-muted, #6B6F7A)";
    statusEl.textContent = msg;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = (emailEl.value || "").trim().toLowerCase();
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      setStatus("Please enter a valid email address.", "error");
      return;
    }

    if (initError || !functions) {
      setStatus("Lookup not configured yet — please use the form below.", "error");
      return;
    }

    btn.disabled = true;
    const origLabel = btn.textContent;
    btn.textContent = "Looking up…";
    setStatus("", "");

    try {
      const verify = httpsCallable(functions, "verifyReturningVisitor");
      const res = await verify({ email });
      const r = (res && res.data) || {};
      if (!r.found) {
        setStatus("We don't have an entry for that email. Please fill the full form below.", "error");
        btn.disabled = false;
        btn.textContent = origLabel;
        return;
      }
      // Restore localStorage and forward into the library
      try {
        localStorage.setItem("companion_access_granted", JSON.stringify({
          name: r.name || "",
          email: email,
          grantedAt: new Date().toISOString()
        }));
      } catch (_) { /* private mode — proceed anyway */ }
      setStatus("Welcome back. Taking you to the library…", "success");
      window.location.href = "thank-you.html";
    } catch (err) {
      console.error("Returning-visitor lookup failed:", err);
      const msg = err && err.code === "functions/unavailable"
        ? "Lookup service is offline. Please use the form below."
        : "Couldn't verify right now. Please use the form below.";
      setStatus(msg, "error");
      btn.disabled = false;
      btn.textContent = origLabel;
    }
  });
})();

// ---------------------------------------------------------------------------
// Validation & sanitization
// ---------------------------------------------------------------------------

const ALLOWED_ROLES = [
  "resident", "fellow", "faculty", "program_director", "other"
];

const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

function sanitizeString(value, maxLen) {
  // Trim, strip control characters (incl. null, line breaks for non-textarea),
  // and cap length. Defense in depth — the Firestore rule also enforces caps.
  return String(value || "")
    .trim()
    .replace(/[\x00-\x1F\x7F]/g, "")
    .slice(0, maxLen);
}

function validateEmail(email) {
  return EMAIL_RE.test(email) && email.length >= 5 && email.length <= 254;
}

// ---------------------------------------------------------------------------
// DOM wiring
// ---------------------------------------------------------------------------

const form = document.getElementById("access-form");
const submitBtn = document.getElementById("access-submit");
const formStatus = document.getElementById("form-status");

const fields = {
  name:        { input: document.getElementById("name"),        error: document.getElementById("name-error") },
  email:       { input: document.getElementById("email"),       error: document.getElementById("email-error") },
  role:        { input: document.getElementById("role"),        error: document.getElementById("role-error") },
  institution: { input: document.getElementById("institution"), error: document.getElementById("institution-error") }
};

function clearErrors() {
  for (const key of Object.keys(fields)) {
    fields[key].error.textContent = "";
    fields[key].input.parentElement.classList.remove("field--error");
  }
  formStatus.className = "form-status";
  formStatus.textContent = "";
}

function setFieldError(key, msg) {
  fields[key].error.textContent = msg;
  fields[key].input.parentElement.classList.add("field--error");
}

function setFormStatus(msg, kind /* 'error' | 'success' */) {
  formStatus.className = "form-status form-status--" + kind;
  formStatus.textContent = msg;
}

// ---------------------------------------------------------------------------
// Submission
// ---------------------------------------------------------------------------

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  clearErrors();

  const name        = sanitizeString(fields.name.input.value, 120);
  const email       = sanitizeString(fields.email.input.value, 254).toLowerCase();
  const role        = String(fields.role.input.value || "");
  const institution = sanitizeString(fields.institution.input.value, 200);

  // Client-side validation (the Firestore rule is the real gate)
  let valid = true;
  if (!name) { setFieldError("name", "Name is required."); valid = false; }
  if (!validateEmail(email)) { setFieldError("email", "Please enter a valid email address."); valid = false; }
  if (!ALLOWED_ROLES.includes(role)) { setFieldError("role", "Please select your role."); valid = false; }
  if (!valid) return;

  if (initError || !db) {
    setFormStatus(
      "The access form isn't configured yet. Please email the author directly to request access.",
      "error"
    );
    return;
  }

  submitBtn.disabled = true;
  const originalLabel = submitBtn.textContent;
  submitBtn.textContent = "Submitting…";

  try {
    await addDoc(collection(db, "access_log"), {
      timestamp: serverTimestamp(),
      name,
      email,
      role,
      institution,
      referrer:   sanitizeString(document.referrer, 500),
      user_agent: sanitizeString(navigator.userAgent, 500)
    });

    // Store minimal data for personalization on the library home.
    // Never store anything sensitive here.
    try {
      localStorage.setItem("companion_access_granted", JSON.stringify({
        name,
        email,
        grantedAt: new Date().toISOString()
      }));
    } catch (_) { /* private mode etc. — ignore */ }

    window.location.href = "thank-you.html";
  } catch (err) {
    console.error("Access log submission failed:", err);
    setFormStatus(
      "Submission failed. Please try again, or email the author directly so we can grant you access.",
      "error"
    );
    submitBtn.disabled = false;
    submitBtn.textContent = originalLabel;
  }
});
