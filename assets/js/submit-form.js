/*
 * Submit-a-prompt form handler.
 *
 * Mirrors the access-gate.js pattern: App Check + Firestore write +
 * client-side validation as defense-in-depth (Firestore rules are the
 * real gate).
 *
 * Writes to the prompt_submissions collection. Submissions are reviewed
 * by the admin via the admin.html dashboard before being added to the
 * library.
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
  const app = initializeApp(firebaseConfig, "submit-form");
  initializeAppCheck(app, {
    provider: new ReCaptchaV3Provider(appCheckSiteKey),
    isTokenAutoRefreshEnabled: true
  });
  db = getFirestore(app);
} catch (err) {
  initError = err;
  console.warn("Firebase init failed (expected during setup):", err);
}

// ---------------------------------------------------------------------------
// Validation & sanitization
// ---------------------------------------------------------------------------

const ALLOWED_PILLARS = ["self-education", "teaching", "educational-operations"];
const ALLOWED_AUDIENCES = ["resident", "fellow", "faculty", "program-director", "learner", "mixed", ""];
const ALLOWED_DIFFICULTIES = ["quick-win", "intermediate", "advanced", ""];
const ALLOWED_TIMES = ["<2min", "2-10min", ">10min", ""];
const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

function sanitizeString(value, maxLen) {
  return String(value || "")
    .trim()
    .replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/g, "")
    .slice(0, maxLen);
}

function sanitizeText(value, maxLen) {
  // Allows newlines and tabs but strips other control characters
  return String(value || "")
    .replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/g, "")
    .trim()
    .slice(0, maxLen);
}

function validateEmail(email) {
  return EMAIL_RE.test(email) && email.length >= 5 && email.length <= 254;
}

// ---------------------------------------------------------------------------
// DOM wiring
// ---------------------------------------------------------------------------

const form = document.getElementById("submit-form");
const submitBtn = document.getElementById("submit-button");
const formStatus = document.getElementById("form-status");

const REQUIRED_FIELDS = [
  "submitter_name", "submitter_email", "prompt_title", "prompt_pillar",
  "prompt_intent", "prompt_text"
];

function getField(name) {
  return document.getElementById(name);
}

function getError(name) {
  return document.getElementById(name + "-error");
}

function clearErrors() {
  REQUIRED_FIELDS.forEach((name) => {
    const err = getError(name);
    if (err) err.textContent = "";
    const input = getField(name);
    if (input && input.parentElement) input.parentElement.classList.remove("field--error");
  });
  formStatus.className = "form-status";
  formStatus.textContent = "";
}

function setFieldError(name, msg) {
  const err = getError(name);
  if (err) err.textContent = msg;
  const input = getField(name);
  if (input && input.parentElement) input.parentElement.classList.add("field--error");
}

function setFormStatus(msg, kind) {
  formStatus.className = "form-status form-status--" + kind;
  formStatus.textContent = msg;
}

// ---------------------------------------------------------------------------
// Submission
// ---------------------------------------------------------------------------

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  clearErrors();

  // Read + sanitize
  const data = {
    submitter_name:        sanitizeString(getField("submitter_name").value, 120),
    submitter_email:       sanitizeString(getField("submitter_email").value, 254).toLowerCase(),
    submitter_affiliation: sanitizeString(getField("submitter_affiliation").value, 200),
    prompt_title:          sanitizeString(getField("prompt_title").value, 200),
    prompt_pillar:         String(getField("prompt_pillar").value || ""),
    prompt_audience:       String(getField("prompt_audience").value || ""),
    prompt_difficulty:     String(getField("prompt_difficulty").value || ""),
    prompt_time:           String(getField("prompt_time").value || ""),
    prompt_intent:         sanitizeText(getField("prompt_intent").value, 800),
    prompt_when:           sanitizeText(getField("prompt_when").value, 800),
    prompt_text:           sanitizeText(getField("prompt_text").value, 8000),
    prompt_expected_output: sanitizeText(getField("prompt_expected_output").value, 800),
    prompt_failure_modes:  sanitizeText(getField("prompt_failure_modes").value, 1500),
    prompt_verification:   sanitizeText(getField("prompt_verification").value, 1500),
    prompt_best_model:     sanitizeString(getField("prompt_best_model").value, 100),
  };

  // Validate required fields
  let valid = true;
  if (!data.submitter_name) {
    setFieldError("submitter_name", "Name is required."); valid = false;
  }
  if (!validateEmail(data.submitter_email)) {
    setFieldError("submitter_email", "Please enter a valid email address."); valid = false;
  }
  if (!data.prompt_title) {
    setFieldError("prompt_title", "Title is required."); valid = false;
  }
  if (!ALLOWED_PILLARS.includes(data.prompt_pillar)) {
    setFieldError("prompt_pillar", "Please select a pillar."); valid = false;
  }
  if (!data.prompt_intent || data.prompt_intent.length < 20) {
    setFieldError("prompt_intent", "Please describe what the prompt does (at least 20 characters)."); valid = false;
  }
  if (!data.prompt_text || data.prompt_text.length < 50) {
    setFieldError("prompt_text", "Please paste the prompt text (at least 50 characters)."); valid = false;
  }

  // Validate optional enums (only if non-empty)
  if (data.prompt_audience && !ALLOWED_AUDIENCES.includes(data.prompt_audience)) valid = false;
  if (data.prompt_difficulty && !ALLOWED_DIFFICULTIES.includes(data.prompt_difficulty)) valid = false;
  if (data.prompt_time && !ALLOWED_TIMES.includes(data.prompt_time)) valid = false;

  if (!valid) {
    setFormStatus("Please fix the errors above.", "error");
    return;
  }

  if (initError || !db) {
    setFormStatus(
      "The submission form isn't configured yet. Please email Dr. Baba directly to share your prompt.",
      "error"
    );
    return;
  }

  submitBtn.disabled = true;
  const originalLabel = submitBtn.textContent;
  submitBtn.textContent = "Submitting…";

  try {
    await addDoc(collection(db, "prompt_submissions"), {
      timestamp: serverTimestamp(),
      status: "pending",
      ...data,
      referrer:   sanitizeString(document.referrer, 500),
      user_agent: sanitizeString(navigator.userAgent, 500)
    });

    // Replace the form with a thank-you panel
    document.getElementById("submit-form").innerHTML =
      '<div style="padding: var(--space-6); text-align: center;">' +
        '<h3 style="margin-top: 0; color: var(--color-success); font-family: var(--font-serif);">Thank you</h3>' +
        '<p>Your submission was received and is in the review queue. Dr. Baba reviews submissions personally; you should hear back within 2-3 weeks.</p>' +
        '<p>Accepted contributions are added to the library with your name on the <a href="library.html#/docs/contributors">Contributors</a> page.</p>' +
        '<p style="margin-top: var(--space-5);"><a href="thank-you.html">Return to the library</a> &middot; <a href="submit.html">Submit another</a></p>' +
      '</div>';
  } catch (err) {
    console.error("Submission failed:", err);
    setFormStatus(
      "Submission failed. Please try again, or email Dr. Baba directly with your prompt.",
      "error"
    );
    submitBtn.disabled = false;
    submitBtn.textContent = originalLabel;
  }
});
