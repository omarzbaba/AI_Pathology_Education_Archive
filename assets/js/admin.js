/*
 * Admin dashboard — Firebase Auth sign-in + Firestore reads.
 *
 * Two views:
 * 1. Access log (append-only contact-capture submissions)
 * 2. Prompt submissions queue (community contributions for review)
 *
 * Security model:
 *   - Firebase Auth (email/password); admin UID gated at Firestore rule level.
 *   - Non-admin authenticated users are force-signed-out.
 *   - 30-min idle auto sign-out.
 */

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-app.js";
import {
  initializeAppCheck,
  ReCaptchaV3Provider
} from "https://www.gstatic.com/firebasejs/10.12.5/firebase-app-check.js";
import {
  getAuth,
  signInWithEmailAndPassword,
  onAuthStateChanged,
  signOut
} from "https://www.gstatic.com/firebasejs/10.12.5/firebase-auth.js";
import {
  getFirestore,
  collection,
  query,
  orderBy,
  getDocs,
  doc,
  updateDoc,
  deleteDoc
} from "https://www.gstatic.com/firebasejs/10.12.5/firebase-firestore.js";

import {
  firebaseConfig,
  appCheckSiteKey,
  adminUid
} from "./firebase-config.js";

// ---------------------------------------------------------------------------
// Firebase init
// ---------------------------------------------------------------------------

let auth, db;
let initError = null;

try {
  const app = initializeApp(firebaseConfig);
  initializeAppCheck(app, {
    provider: new ReCaptchaV3Provider(appCheckSiteKey),
    isTokenAutoRefreshEnabled: true
  });
  auth = getAuth(app);
  db = getFirestore(app);
} catch (err) {
  initError = err;
  console.warn("Firebase init failed:", err);
}

// ---------------------------------------------------------------------------
// DOM
// ---------------------------------------------------------------------------

const signinPanel    = document.getElementById("signin-panel");
const dashboardPanel = document.getElementById("dashboard-panel");
const dashboardEl    = document.getElementById("dashboard-content");
const submissionsEl  = document.getElementById("submissions-content");
const signinForm     = document.getElementById("signin-form");
const signinStatus   = document.getElementById("signin-status");
const emailInput     = document.getElementById("admin-email");
const passwordInput  = document.getElementById("admin-password");

const tabAccessLog   = document.getElementById("tab-access-log");
const tabSubmissions = document.getElementById("tab-submissions");
const tabComments    = document.getElementById("tab-comments");
const submissionsBadge = document.getElementById("submissions-badge");
const commentsBadge    = document.getElementById("comments-badge");
const accessLogSection   = document.getElementById("access-log-section");
const submissionsSection = document.getElementById("submissions-section");
const commentsSection    = document.getElementById("comments-section");
const commentsEl     = document.getElementById("comments-content");
const signoutLink    = document.getElementById("admin-signout-link");

function setSigninStatus(msg, kind) {
  signinStatus.className = "form-status form-status--" + kind;
  signinStatus.textContent = msg;
}

function escapeHtml(s) {
  return String(s == null ? "" : s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

// ---------------------------------------------------------------------------
// Tabs
// ---------------------------------------------------------------------------

function showTab(which) {
  const sections = {
    "access-log": accessLogSection,
    "submissions": submissionsSection,
    "comments": commentsSection
  };
  const tabs = {
    "access-log": tabAccessLog,
    "submissions": tabSubmissions,
    "comments": tabComments
  };
  for (const key of Object.keys(sections)) {
    sections[key].hidden = (key !== which);
    if (key === which) tabs[key].classList.add("admin-tab--active");
    else tabs[key].classList.remove("admin-tab--active");
  }
}

tabAccessLog.addEventListener("click", (e) => { e.preventDefault(); showTab("access-log"); });
tabSubmissions.addEventListener("click", (e) => { e.preventDefault(); showTab("submissions"); renderSubmissions(); });
tabComments.addEventListener("click", (e) => { e.preventDefault(); showTab("comments"); renderCommentsModeration(); });
signoutLink.addEventListener("click", (e) => { e.preventDefault(); signOut(auth); });

// ---------------------------------------------------------------------------
// Idle timeout — 30 minutes
// ---------------------------------------------------------------------------

const IDLE_MS = 30 * 60 * 1000;
let idleTimer = null;

function armIdleTimer() {
  clearTimeout(idleTimer);
  idleTimer = setTimeout(() => {
    if (auth && auth.currentUser) signOut(auth);
  }, IDLE_MS);
}

["click", "keydown", "scroll", "mousemove"].forEach((ev) =>
  document.addEventListener(ev, armIdleTimer, { passive: true })
);

// ---------------------------------------------------------------------------
// Sign-in
// ---------------------------------------------------------------------------

signinForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  setSigninStatus("", "");
  signinStatus.textContent = "";

  if (initError || !auth) {
    setSigninStatus("Firebase not configured. Complete setup first.", "error");
    return;
  }

  try {
    await signInWithEmailAndPassword(auth, emailInput.value.trim(), passwordInput.value);
    passwordInput.value = "";
  } catch (err) {
    setSigninStatus("Sign-in failed (" + (err.code || "unknown error") + ").", "error");
  }
});

// ---------------------------------------------------------------------------
// Auth state
// ---------------------------------------------------------------------------

if (auth) {
  onAuthStateChanged(auth, async (user) => {
    if (user && user.uid === adminUid) {
      signinPanel.hidden = true;
      dashboardPanel.hidden = false;
      armIdleTimer();
      await renderAccessLog();
      await checkSubmissionCount();
      await checkCommentsCount();
    } else {
      if (user) {
        await signOut(auth);
        setSigninStatus("That account is not authorized for the admin dashboard.", "error");
      }
      signinPanel.hidden = false;
      dashboardPanel.hidden = true;
      clearTimeout(idleTimer);
    }
  });
}

// ---------------------------------------------------------------------------
// Access log
// ---------------------------------------------------------------------------

let accessLogRows = [];

async function renderAccessLog() {
  dashboardEl.innerHTML = '<p>Loading access log&hellip;</p>';
  try {
    const q = query(collection(db, "access_log"), orderBy("timestamp", "desc"));
    const snap = await getDocs(q);
    accessLogRows = [];
    snap.forEach((doc) => {
      const d = doc.data();
      accessLogRows.push({
        id:          doc.id,
        timestamp:   d.timestamp,
        name:        d.name        || "",
        email:       d.email       || "",
        role:        d.role        || "",
        institution: d.institution || "",
      });
    });
    drawAccessLogTable(accessLogRows);
  } catch (err) {
    dashboardEl.innerHTML =
      '<p class="form-status form-status--error">Failed to load: ' +
      escapeHtml(err.message) + '</p>';
  }
}

function fmtTimestamp(ts) {
  if (!ts) return "";
  if (typeof ts.toDate === "function") return ts.toDate().toLocaleString();
  return String(ts);
}

function drawAccessLogTable(rows) {
  const total = accessLogRows.length;
  const showing = rows.length;
  dashboardEl.innerHTML =
    '<div class="admin-controls" style="display:flex;gap:1rem;flex-wrap:wrap;align-items:center;margin-bottom:1rem;">' +
      '<input type="search" id="admin-search" placeholder="Search name, email, institution&hellip;" style="flex:1;min-width:240px;padding:0.5rem;border:1px solid var(--color-rule);border-radius:2px;">' +
      '<select id="admin-role-filter" style="padding:0.5rem;border:1px solid var(--color-rule);border-radius:2px;">' +
        '<option value="">All roles</option>' +
        '<option value="resident">Resident</option>' +
        '<option value="fellow">Fellow</option>' +
        '<option value="faculty">Faculty</option>' +
        '<option value="program_director">Program Director</option>' +
        '<option value="other">Other</option>' +
      '</select>' +
      '<button class="btn" id="admin-export">Export CSV</button>' +
    '</div>' +
    '<p style="font-size:var(--fs-sm);color:var(--color-muted);margin:0 0 1rem;">Showing ' + showing + ' of ' + total + ' entries.</p>' +
    '<div style="overflow-x:auto;border:1px solid var(--color-rule);">' +
      '<table style="width:100%;border-collapse:collapse;font-size:var(--fs-sm);">' +
        '<thead style="background:var(--color-paper);"><tr>' +
          '<th style="text-align:left;padding:0.5rem;border-bottom:1px solid var(--color-rule);">Timestamp</th>' +
          '<th style="text-align:left;padding:0.5rem;border-bottom:1px solid var(--color-rule);">Name</th>' +
          '<th style="text-align:left;padding:0.5rem;border-bottom:1px solid var(--color-rule);">Email</th>' +
          '<th style="text-align:left;padding:0.5rem;border-bottom:1px solid var(--color-rule);">Role</th>' +
          '<th style="text-align:left;padding:0.5rem;border-bottom:1px solid var(--color-rule);">Institution</th>' +
        '</tr></thead><tbody>' +
          rows.map((r) =>
            '<tr>' +
              '<td style="padding:0.5rem;border-bottom:1px solid var(--color-rule);white-space:nowrap;">' + escapeHtml(fmtTimestamp(r.timestamp)) + '</td>' +
              '<td style="padding:0.5rem;border-bottom:1px solid var(--color-rule);">' + escapeHtml(r.name) + '</td>' +
              '<td style="padding:0.5rem;border-bottom:1px solid var(--color-rule);">' + escapeHtml(r.email) + '</td>' +
              '<td style="padding:0.5rem;border-bottom:1px solid var(--color-rule);">' + escapeHtml(r.role) + '</td>' +
              '<td style="padding:0.5rem;border-bottom:1px solid var(--color-rule);">' + escapeHtml(r.institution) + '</td>' +
            '</tr>'
          ).join("") +
        '</tbody></table></div>';
  document.getElementById("admin-search").addEventListener("input", applyAccessLogFilters);
  document.getElementById("admin-role-filter").addEventListener("change", applyAccessLogFilters);
  document.getElementById("admin-export").addEventListener("click", exportAccessLogCsv);
}

function applyAccessLogFilters() {
  const term = document.getElementById("admin-search").value.trim().toLowerCase();
  const role = document.getElementById("admin-role-filter").value;
  const filtered = accessLogRows.filter((r) => {
    if (role && r.role !== role) return false;
    if (term) {
      const hay = (r.name + " " + r.email + " " + r.institution).toLowerCase();
      if (!hay.includes(term)) return false;
    }
    return true;
  });
  drawAccessLogTable(filtered);
}

function exportAccessLogCsv() {
  const term = document.getElementById("admin-search").value.trim().toLowerCase();
  const role = document.getElementById("admin-role-filter").value;
  const rows = accessLogRows.filter((r) => {
    if (role && r.role !== role) return false;
    if (term) {
      const hay = (r.name + " " + r.email + " " + r.institution).toLowerCase();
      if (!hay.includes(term)) return false;
    }
    return true;
  });
  const header = ["timestamp", "name", "email", "role", "institution"];
  const csvRows = [header.join(",")];
  for (const r of rows) {
    csvRows.push(header.map((k) => csvCell(k === "timestamp" ? fmtTimestamp(r.timestamp) : r[k])).join(","));
  }
  downloadFile(csvRows.join("\n"), "access_log_" + new Date().toISOString().slice(0, 10) + ".csv", "text/csv");
}

function csvCell(v) {
  const s = String(v == null ? "" : v);
  if (/[",\n\r]/.test(s)) return '"' + s.replace(/"/g, '""') + '"';
  return s;
}

function downloadFile(content, filename, mimeType) {
  const blob = new Blob([content], { type: mimeType + ";charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// ---------------------------------------------------------------------------
// Submissions queue
// ---------------------------------------------------------------------------

let submissionRows = [];

async function checkSubmissionCount() {
  try {
    const q = query(collection(db, "prompt_submissions"), orderBy("timestamp", "desc"));
    const snap = await getDocs(q);
    let pending = 0;
    snap.forEach((doc) => {
      if (doc.data().status === "pending") pending++;
    });
    if (pending > 0) {
      submissionsBadge.textContent = pending;
      submissionsBadge.style.display = "inline-block";
    } else {
      submissionsBadge.style.display = "none";
    }
  } catch (_) { /* ignore — will show when tab is opened */ }
}

async function renderSubmissions() {
  submissionsEl.innerHTML = '<p>Loading submissions&hellip;</p>';
  try {
    const q = query(collection(db, "prompt_submissions"), orderBy("timestamp", "desc"));
    const snap = await getDocs(q);
    submissionRows = [];
    snap.forEach((doc) => {
      submissionRows.push({ id: doc.id, ...doc.data() });
    });
    drawSubmissionsTable(submissionRows);
  } catch (err) {
    submissionsEl.innerHTML =
      '<p class="form-status form-status--error">Failed to load: ' +
      escapeHtml(err.message) + '</p>';
  }
}

function statusPill(status) {
  const map = {
    pending:         { cls: "pill pill--mid", label: "Pending" },
    approved:        { cls: "pill pill--easy", label: "Approved" },
    rejected:        { cls: "pill pill--hard", label: "Rejected" },
    needs_revision:  { cls: "pill pill--neutral", label: "Needs revision" }
  };
  const m = map[status] || { cls: "pill pill--neutral", label: status || "?" };
  return '<span class="' + m.cls + '">' + escapeHtml(m.label) + '</span>';
}

function drawSubmissionsTable(rows) {
  const counts = {
    pending: rows.filter(r => r.status === "pending").length,
    approved: rows.filter(r => r.status === "approved").length,
    rejected: rows.filter(r => r.status === "rejected").length,
    needs_revision: rows.filter(r => r.status === "needs_revision").length,
  };

  submissionsEl.innerHTML =
    '<div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:1rem;">' +
      '<button class="btn" data-filter="all" style="background:var(--color-navy);">All (' + rows.length + ')</button>' +
      '<button class="btn" data-filter="pending">Pending (' + counts.pending + ')</button>' +
      '<button class="btn" data-filter="approved" style="background:var(--color-success);">Approved (' + counts.approved + ')</button>' +
      '<button class="btn" data-filter="needs_revision" style="background:var(--color-muted);">Needs revision (' + counts.needs_revision + ')</button>' +
      '<button class="btn" data-filter="rejected" style="background:var(--color-burgundy);">Rejected (' + counts.rejected + ')</button>' +
    '</div>' +
    '<div id="submissions-list">' +
      rows.map(submissionCardHtml).join("") +
    '</div>';

  // Wire filter buttons
  submissionsEl.querySelectorAll("button[data-filter]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const f = btn.getAttribute("data-filter");
      const filtered = f === "all" ? submissionRows : submissionRows.filter(r => r.status === f);
      document.getElementById("submissions-list").innerHTML = filtered.map(submissionCardHtml).join("");
      wireSubmissionActions();
    });
  });

  wireSubmissionActions();
}

function submissionCardHtml(r) {
  const id = "sub-" + r.id;
  return (
    '<article style="border:1px solid var(--color-rule);border-radius:3px;margin-bottom:1rem;padding:1rem;background:var(--color-white);">' +
      '<div style="display:flex;justify-content:space-between;align-items:start;gap:1rem;margin-bottom:0.5rem;">' +
        '<div>' +
          '<h3 style="font-family:var(--font-serif);margin:0 0 0.25rem;font-size:1.125rem;">' + escapeHtml(r.prompt_title) + '</h3>' +
          '<p style="font-size:var(--fs-sm);color:var(--color-muted);margin:0;">' +
            'From <strong>' + escapeHtml(r.submitter_name) + '</strong>' +
            (r.submitter_affiliation ? ' (' + escapeHtml(r.submitter_affiliation) + ')' : '') +
            ' &middot; ' + escapeHtml(r.submitter_email) +
            ' &middot; ' + escapeHtml(fmtTimestamp(r.timestamp)) +
          '</p>' +
        '</div>' +
        '<div>' + statusPill(r.status) + '</div>' +
      '</div>' +
      '<div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-bottom:0.75rem;font-size:var(--fs-xs);">' +
        '<span class="pill">' + escapeHtml(r.prompt_pillar) + '</span>' +
        (r.prompt_audience ? '<span class="pill">' + escapeHtml(r.prompt_audience) + '</span>' : '') +
        (r.prompt_difficulty ? '<span class="pill">' + escapeHtml(r.prompt_difficulty) + '</span>' : '') +
        (r.prompt_time ? '<span class="pill">' + escapeHtml(r.prompt_time) + '</span>' : '') +
        (r.prompt_best_model ? '<span class="pill pill--model">' + escapeHtml(r.prompt_best_model) + '</span>' : '') +
      '</div>' +
      '<details style="margin-bottom:0.75rem;">' +
        '<summary style="cursor:pointer;font-weight:500;font-size:var(--fs-sm);">View submission</summary>' +
        '<div style="margin-top:0.75rem;padding-top:0.75rem;border-top:1px solid var(--color-rule);font-size:var(--fs-sm);">' +
          '<p><strong>What it does:</strong> ' + escapeHtml(r.prompt_intent) + '</p>' +
          (r.prompt_when ? '<p><strong>When to use:</strong> ' + escapeHtml(r.prompt_when) + '</p>' : '') +
          '<p><strong>The prompt:</strong></p>' +
          '<pre style="background:var(--color-paper);border:1px solid var(--color-rule);padding:0.75rem;overflow-x:auto;white-space:pre-wrap;font-size:0.85em;">' + escapeHtml(r.prompt_text) + '</pre>' +
          (r.prompt_expected_output ? '<p><strong>Expected output:</strong> ' + escapeHtml(r.prompt_expected_output) + '</p>' : '') +
          (r.prompt_failure_modes ? '<p><strong>Failure modes:</strong> ' + escapeHtml(r.prompt_failure_modes) + '</p>' : '') +
          (r.prompt_verification ? '<p><strong>Verification:</strong> ' + escapeHtml(r.prompt_verification) + '</p>' : '') +
        '</div>' +
      '</details>' +
      '<div style="display:flex;gap:0.5rem;flex-wrap:wrap;">' +
        '<button class="btn" data-sub-id="' + escapeHtml(r.id) + '" data-action="approve" style="background:var(--color-success);font-size:0.85em;padding:0.4rem 0.8rem;">Approve</button>' +
        '<button class="btn" data-sub-id="' + escapeHtml(r.id) + '" data-action="needs_revision" style="background:var(--color-muted);font-size:0.85em;padding:0.4rem 0.8rem;">Needs revision</button>' +
        '<button class="btn" data-sub-id="' + escapeHtml(r.id) + '" data-action="reject" style="background:var(--color-burgundy);font-size:0.85em;padding:0.4rem 0.8rem;">Reject</button>' +
        '<button class="btn" data-sub-id="' + escapeHtml(r.id) + '" data-action="export" style="background:var(--color-navy);font-size:0.85em;padding:0.4rem 0.8rem;">Export as markdown</button>' +
        '<button class="btn" data-sub-id="' + escapeHtml(r.id) + '" data-action="delete" style="background:#7a1c28;border:1px solid #4a0f17;font-size:0.85em;padding:0.4rem 0.8rem;" title="Permanently delete this submission">Delete…</button>' +
      '</div>' +
    '</article>'
  );
}

function wireSubmissionActions() {
  submissionsEl.querySelectorAll("button[data-action]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const id = btn.getAttribute("data-sub-id");
      const action = btn.getAttribute("data-action");
      const sub = submissionRows.find(r => r.id === id);
      if (!sub) return;

      if (action === "export") {
        exportSubmissionAsMarkdown(sub);
        return;
      }

      if (action === "delete") {
        const label = (sub.prompt_title || "untitled").slice(0, 60);
        if (!confirm("Permanently delete the submission \"" + label + "\"?\n\nThis CANNOT be undone — the row is removed from Firestore.")) return;
        btn.disabled = true;
        const orig = btn.textContent;
        btn.textContent = "Deleting…";
        try {
          await deleteDoc(doc(db, "prompt_submissions", id));
          await renderSubmissions();
          await checkSubmissionCount();
        } catch (err) {
          alert("Delete failed: " + (err.message || "unknown error"));
          btn.disabled = false;
          btn.textContent = orig;
        }
        return;
      }

      const newStatus =
        action === "approve" ? "approved" :
        action === "needs_revision" ? "needs_revision" :
        action === "reject" ? "rejected" : null;
      if (!newStatus) return;

      if (!confirm("Set this submission to '" + newStatus + "'?")) return;

      btn.disabled = true;
      const orig = btn.textContent;
      btn.textContent = "Updating…";
      try {
        await updateDoc(doc(db, "prompt_submissions", id), { status: newStatus });
        // Re-render
        await renderSubmissions();
        await checkSubmissionCount();
      } catch (err) {
        alert("Update failed: " + (err.message || "unknown error"));
        btn.disabled = false;
        btn.textContent = orig;
      }
    });
  });
}

function exportSubmissionAsMarkdown(sub) {
  // Generate a ready-to-paste .md file in the prompt format
  const slug = (sub.prompt_title || "untitled")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80);

  const today = new Date().toISOString().slice(0, 10);

  const fm = [
    "---",
    "title: " + sub.prompt_title,
    "pillar: " + sub.prompt_pillar,
    "event_type: " + "n/a",
    "audience: " + (sub.prompt_audience || "mixed"),
    "difficulty: " + (sub.prompt_difficulty || "intermediate"),
    "time_to_use: " + (sub.prompt_time || "2-10min"),
    "visual: " + "text-only",
    "tags: " + "community-contributed",
    "verified_models: TODO",
    "best_model: " + (sub.prompt_best_model || "Claude Sonnet 4.6"),
    "contributor: " + sub.submitter_name + (sub.submitter_affiliation ? " (" + sub.submitter_affiliation + ")" : ""),
    "last_updated: " + today,
    "---",
    "",
    "## What this prompt does",
    "",
    sub.prompt_intent,
    "",
    "## When to use it",
    "",
    sub.prompt_when || "TODO",
    "",
    "## The prompt",
    "",
    "```",
    sub.prompt_text,
    "```",
    "",
    "## Expected output",
    "",
    sub.prompt_expected_output || "TODO",
    "",
    "## Common failure modes",
    "",
    sub.prompt_failure_modes || "TODO",
    "",
    "## Required human verification",
    "",
    sub.prompt_verification || "TODO",
    "",
    "## Best model and why",
    "",
    "**" + (sub.prompt_best_model || "Claude Sonnet 4.6") + "** — TODO add rationale.",
    "",
    "## Contributed by",
    "",
    sub.submitter_name + (sub.submitter_affiliation ? ", " + sub.submitter_affiliation : "") + ". Submitted " + fmtTimestamp(sub.timestamp) + ".",
    ""
  ].join("\n");

  downloadFile(fm, slug + ".md", "text/markdown");
}

// ---------------------------------------------------------------------------
// Comments moderation
// ---------------------------------------------------------------------------

let commentRows = [];

async function checkCommentsCount() {
  try {
    const q = query(collection(db, "comments"), orderBy("timestamp", "desc"));
    const snap = await getDocs(q);
    let pending = 0;
    snap.forEach((doc) => {
      if (doc.data().status === "pending") pending++;
    });
    if (pending > 0) {
      commentsBadge.textContent = pending;
      commentsBadge.style.display = "inline-block";
    } else {
      commentsBadge.style.display = "none";
    }
  } catch (_) { /* ignore */ }
}

async function renderCommentsModeration() {
  commentsEl.innerHTML = '<p>Loading comments&hellip;</p>';
  try {
    const q = query(collection(db, "comments"), orderBy("timestamp", "desc"));
    const snap = await getDocs(q);
    commentRows = [];
    snap.forEach((doc) => commentRows.push({ id: doc.id, ...doc.data() }));
    drawCommentsTable(commentRows);
  } catch (err) {
    commentsEl.innerHTML =
      '<p class="form-status form-status--error">Failed to load: ' +
      escapeHtml(err.message) + '</p>';
  }
}

function commentStatusPill(status) {
  const map = {
    pending: { cls: "pill pill--mid",    label: "Pending" },
    visible: { cls: "pill pill--easy",   label: "Visible" },
    hidden:  { cls: "pill pill--hard",   label: "Hidden" }
  };
  const m = map[status] || { cls: "pill pill--neutral", label: status || "?" };
  return '<span class="' + m.cls + '">' + escapeHtml(m.label) + '</span>';
}

function drawCommentsTable(rows) {
  const counts = {
    pending: rows.filter(r => r.status === "pending").length,
    visible: rows.filter(r => r.status === "visible").length,
    hidden:  rows.filter(r => r.status === "hidden").length,
  };

  commentsEl.innerHTML =
    '<div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:1rem;align-items:center;">' +
      '<button class="btn" data-cfilter="all" style="background:var(--color-navy);">All (' + rows.length + ')</button>' +
      '<button class="btn" data-cfilter="pending">Pending (' + counts.pending + ')</button>' +
      '<button class="btn" data-cfilter="visible" style="background:var(--color-success);">Visible (' + counts.visible + ')</button>' +
      '<button class="btn" data-cfilter="hidden" style="background:var(--color-burgundy);">Hidden (' + counts.hidden + ')</button>' +
      '<input type="search" id="comments-search" placeholder="Search name, email, text&hellip;" style="flex:1;min-width:200px;padding:0.5rem;border:1px solid var(--color-rule);border-radius:2px;">' +
    '</div>' +
    '<div id="bulk-actions" style="display:none;background:var(--color-paper);border:1px solid var(--color-rule);padding:0.75rem;margin-bottom:1rem;border-radius:3px;align-items:center;gap:0.75rem;flex-wrap:wrap;">' +
      '<strong id="bulk-count" style="font-size:var(--fs-sm);">0 selected</strong>' +
      '<button class="btn" id="bulk-approve" style="background:var(--color-success);font-size:0.85em;padding:0.4rem 0.8rem;">Approve selected</button>' +
      '<button class="btn" id="bulk-hide" style="background:var(--color-burgundy);font-size:0.85em;padding:0.4rem 0.8rem;">Hide selected</button>' +
      '<button class="btn" id="bulk-clear" style="background:var(--color-muted);font-size:0.85em;padding:0.4rem 0.8rem;">Clear selection</button>' +
    '</div>' +
    '<div id="comments-list">' +
      rows.map(commentModerationCardHtml).join("") +
    '</div>';

  commentsEl.querySelectorAll("button[data-cfilter]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const f = btn.getAttribute("data-cfilter");
      const filtered = f === "all" ? commentRows : commentRows.filter(r => r.status === f);
      const searchTerm = document.getElementById("comments-search").value.trim().toLowerCase();
      const finalFiltered = searchTerm
        ? filtered.filter(r => commentMatchesSearch(r, searchTerm))
        : filtered;
      document.getElementById("comments-list").innerHTML = finalFiltered.map(commentModerationCardHtml).join("");
      wireCommentModerationActions();
      wireBulkActions();
    });
  });

  document.getElementById("comments-search").addEventListener("input", (e) => {
    const term = e.target.value.trim().toLowerCase();
    const filtered = term ? commentRows.filter(r => commentMatchesSearch(r, term)) : commentRows;
    document.getElementById("comments-list").innerHTML = filtered.map(commentModerationCardHtml).join("");
    wireCommentModerationActions();
    wireBulkActions();
  });

  wireCommentModerationActions();
  wireBulkActions();
}

function commentMatchesSearch(c, term) {
  const hay = (
    (c.commenter_name || "") + " " +
    (c.commenter_email || "") + " " +
    (c.commenter_affiliation || "") + " " +
    (c.comment_text || "") + " " +
    (c.prompt_path || "")
  ).toLowerCase();
  return hay.includes(term);
}

function wireBulkActions() {
  const bulkActions = document.getElementById("bulk-actions");
  const bulkCount = document.getElementById("bulk-count");

  function updateBulkVisibility() {
    const checked = commentsEl.querySelectorAll("input.comment-checkbox:checked");
    if (checked.length > 0) {
      bulkActions.style.display = "flex";
      bulkCount.textContent = checked.length + " selected";
    } else {
      bulkActions.style.display = "none";
    }
  }

  commentsEl.querySelectorAll("input.comment-checkbox").forEach((cb) => {
    cb.addEventListener("change", updateBulkVisibility);
  });

  async function bulkUpdate(newStatus) {
    const checked = Array.from(commentsEl.querySelectorAll("input.comment-checkbox:checked"));
    if (checked.length === 0) return;
    if (!confirm("Set " + checked.length + " comment(s) to '" + newStatus + "'?")) return;

    const ids = checked.map(cb => cb.getAttribute("data-cid"));
    try {
      // Update sequentially to avoid hammering
      for (const id of ids) {
        await updateDoc(doc(db, "comments", id), { status: newStatus });
      }
      await renderCommentsModeration();
      await checkCommentsCount();
    } catch (err) {
      alert("Bulk update failed: " + (err.message || "unknown error"));
    }
  }

  document.getElementById("bulk-approve").addEventListener("click", () => bulkUpdate("visible"));
  document.getElementById("bulk-hide").addEventListener("click", () => bulkUpdate("hidden"));
  document.getElementById("bulk-clear").addEventListener("click", () => {
    commentsEl.querySelectorAll("input.comment-checkbox").forEach(cb => cb.checked = false);
    updateBulkVisibility();
  });
}

function commentModerationCardHtml(c) {
  const promptLink = c.prompt_path
    ? '<a href="library.html#/' + escapeHtml(c.prompt_path) + '" target="_blank" rel="noopener">' + escapeHtml(c.prompt_path.split("/").pop()) + ' &rarr;</a>'
    : '(no path)';
  return (
    '<article style="border:1px solid var(--color-rule);border-radius:3px;margin-bottom:1rem;padding:1rem;background:var(--color-white);">' +
      '<div style="display:flex;justify-content:space-between;align-items:start;gap:1rem;margin-bottom:0.5rem;">' +
        '<div style="display:flex;gap:0.75rem;align-items:start;flex:1;">' +
          '<input type="checkbox" class="comment-checkbox" data-cid="' + escapeHtml(c.id) + '" style="margin-top:0.25rem;">' +
          '<div>' +
          '<p style="font-size:var(--fs-sm);margin:0 0 0.25rem;"><strong>' + escapeHtml(c.commenter_name) + '</strong>' +
            (c.commenter_affiliation ? ' (' + escapeHtml(c.commenter_affiliation) + ')' : '') +
            ' &middot; ' + escapeHtml(c.commenter_email) +
            ' &middot; ' + escapeHtml(fmtTimestamp(c.timestamp)) +
            (c.is_admin ? ' <span class="pill pill--model">Author</span>' : '') +
          '</p>' +
          '<p style="font-size:var(--fs-xs);margin:0;color:var(--color-muted);">On: ' + promptLink + '</p>' +
          '</div>' +
        '</div>' +
        '<div>' + commentStatusPill(c.status) + '</div>' +
      '</div>' +
      '<blockquote style="margin:0.75rem 0;padding:0.5rem 0.75rem;border-left:3px solid var(--color-rule);background:var(--color-paper);font-size:var(--fs-sm);">' +
        escapeHtml(c.comment_text || "").split("\n").map(p => '<p style="margin:0.25rem 0;">' + p + '</p>').join("") +
      '</blockquote>' +
      '<div style="display:flex;gap:0.5rem;flex-wrap:wrap;">' +
        (c.status !== "visible"
          ? '<button class="btn" data-cid="' + escapeHtml(c.id) + '" data-caction="visible" style="background:var(--color-success);font-size:0.85em;padding:0.4rem 0.8rem;">Approve / Show</button>'
          : '') +
        (c.status !== "hidden"
          ? '<button class="btn" data-cid="' + escapeHtml(c.id) + '" data-caction="hidden" style="background:var(--color-burgundy);font-size:0.85em;padding:0.4rem 0.8rem;">Hide</button>'
          : '') +
        (c.status !== "pending"
          ? '<button class="btn" data-cid="' + escapeHtml(c.id) + '" data-caction="pending" style="background:var(--color-muted);font-size:0.85em;padding:0.4rem 0.8rem;">Reset to pending</button>'
          : '') +
        '<button class="btn" data-cid="' + escapeHtml(c.id) + '" data-caction="delete" style="background:#7a1c28;border:1px solid #4a0f17;font-size:0.85em;padding:0.4rem 0.8rem;" title="Permanently delete this comment">Delete…</button>' +
      '</div>' +
    '</article>'
  );
}

function wireCommentModerationActions() {
  commentsEl.querySelectorAll("button[data-caction]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const id = btn.getAttribute("data-cid");
      const action = btn.getAttribute("data-caction");

      if (action === "delete") {
        if (!confirm("Permanently delete this comment?\n\nThis CANNOT be undone — the row is removed from Firestore.")) return;
        btn.disabled = true;
        const orig = btn.textContent;
        btn.textContent = "Deleting…";
        try {
          await deleteDoc(doc(db, "comments", id));
          await renderCommentsModeration();
          await checkCommentsCount();
        } catch (err) {
          alert("Delete failed: " + (err.message || "unknown error"));
          btn.disabled = false;
          btn.textContent = orig;
        }
        return;
      }

      const newStatus = action;
      if (!confirm("Set this comment to '" + newStatus + "'?")) return;
      btn.disabled = true;
      const orig = btn.textContent;
      btn.textContent = "Updating…";
      try {
        await updateDoc(doc(db, "comments", id), { status: newStatus });
        await renderCommentsModeration();
        await checkCommentsCount();
      } catch (err) {
        alert("Update failed: " + (err.message || "unknown error"));
        btn.disabled = false;
        btn.textContent = orig;
      }
    });
  });
}
