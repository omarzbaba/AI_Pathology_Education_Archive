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

import { firebaseConfig, appCheckSiteKey } from "./firebase-config.js";

// ---------------------------------------------------------------------------
// Firebase init
// ---------------------------------------------------------------------------

let db;
let initError = null;

try {
  const app = initializeApp(firebaseConfig);
  initializeAppCheck(app, {
    provider: new ReCaptchaV3Provider(appCheckSiteKey),
    isTokenAutoRefreshEnabled: true
  });
  db = getFirestore(app);
} catch (err) {
  initError = err;
  // Don't throw — let the form render and show a sensible error on submit.
  // This keeps the page usable during local development before Firebase is set up.
  console.warn("Firebase init failed (expected during Phase 3 setup):", err);
}

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
