/*
 * Admin dashboard — Firebase Auth sign-in + Firestore reads.
 *
 * Security model:
 *   - The page itself is publicly served. The Firestore rule
 *     (request.auth.uid == ADMIN_UID) is the actual gate; this script
 *     is just the UX.
 *   - Even if a non-admin signs in via the form, the dashboard query
 *     will be rejected by Firestore. We belt-and-brace by checking
 *     user.uid client-side and force-signing-out non-admins.
 *   - 30-minute idle auto-sign-out reduces window if the browser is
 *     left unlocked.
 *   - Append-only enforcement lives in the rules, not here.
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
  getDocs
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
const signinForm     = document.getElementById("signin-form");
const signinStatus   = document.getElementById("signin-status");
const emailInput     = document.getElementById("admin-email");
const passwordInput  = document.getElementById("admin-password");

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
// Sign-in form
// ---------------------------------------------------------------------------

signinForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  setSigninStatus("", "");
  signinStatus.textContent = "";

  if (initError || !auth) {
    setSigninStatus("Firebase not configured. Complete Phase 3 setup first.", "error");
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
// Auth state — show/hide panels, load data
// ---------------------------------------------------------------------------

if (auth) {
  onAuthStateChanged(auth, async (user) => {
    if (user && user.uid === adminUid) {
      signinPanel.hidden = true;
      dashboardPanel.hidden = false;
      armIdleTimer();
      await renderDashboard();
    } else {
      if (user) {
        // Authenticated but wrong UID — refuse and sign out.
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
// Dashboard rendering
// ---------------------------------------------------------------------------

let allRows = [];

async function renderDashboard() {
  dashboardEl.innerHTML = '<p>Loading access log&hellip;</p>';
  try {
    const q = query(collection(db, "access_log"), orderBy("timestamp", "desc"));
    const snap = await getDocs(q);
    allRows = [];
    snap.forEach((doc) => {
      const d = doc.data();
      allRows.push({
        id:          doc.id,
        timestamp:   d.timestamp,
        name:        d.name        || "",
        email:       d.email       || "",
        role:        d.role        || "",
        institution: d.institution || "",
        referrer:    d.referrer    || "",
        user_agent:  d.user_agent  || ""
      });
    });
    drawTable(allRows);
  } catch (err) {
    dashboardEl.innerHTML =
      '<p class="form-status form-status--error">Failed to load: ' +
      escapeHtml(err.message) + '</p>';
  }
}

function fmtTimestamp(ts) {
  if (!ts) return "";
  // Firestore Timestamp object has toDate()
  if (typeof ts.toDate === "function") return ts.toDate().toLocaleString();
  return String(ts);
}

function drawTable(rows) {
  const total = allRows.length;
  const showing = rows.length;

  dashboardEl.innerHTML =
    '<div class="admin-controls" style="display:flex;gap:1rem;flex-wrap:wrap;align-items:center;margin-bottom:1rem;">' +
      '<input type="search" id="admin-search" placeholder="Search name, email, institution&hellip;" ' +
        'style="flex:1;min-width:240px;padding:0.5rem;border:1px solid var(--color-rule);border-radius:2px;">' +
      '<select id="admin-role-filter" style="padding:0.5rem;border:1px solid var(--color-rule);border-radius:2px;">' +
        '<option value="">All roles</option>' +
        '<option value="resident">Resident</option>' +
        '<option value="fellow">Fellow</option>' +
        '<option value="faculty">Faculty</option>' +
        '<option value="program_director">Program Director</option>' +
        '<option value="other">Other</option>' +
      '</select>' +
      '<button class="btn" id="admin-export">Export CSV</button>' +
      '<button class="btn" id="admin-signout" style="background:var(--color-navy);">Sign out</button>' +
    '</div>' +
    '<p style="font-size:var(--fs-sm);color:var(--color-muted);margin:0 0 1rem;">' +
      'Showing ' + showing + ' of ' + total + ' entries.' +
    '</p>' +
    '<div style="overflow-x:auto;border:1px solid var(--color-rule);">' +
      '<table style="width:100%;border-collapse:collapse;font-size:var(--fs-sm);">' +
        '<thead style="background:var(--color-paper);">' +
          '<tr>' +
            '<th style="text-align:left;padding:0.5rem;border-bottom:1px solid var(--color-rule);">Timestamp</th>' +
            '<th style="text-align:left;padding:0.5rem;border-bottom:1px solid var(--color-rule);">Name</th>' +
            '<th style="text-align:left;padding:0.5rem;border-bottom:1px solid var(--color-rule);">Email</th>' +
            '<th style="text-align:left;padding:0.5rem;border-bottom:1px solid var(--color-rule);">Role</th>' +
            '<th style="text-align:left;padding:0.5rem;border-bottom:1px solid var(--color-rule);">Institution</th>' +
          '</tr>' +
        '</thead>' +
        '<tbody>' +
          rows.map((r) =>
            '<tr>' +
              '<td style="padding:0.5rem;border-bottom:1px solid var(--color-rule);white-space:nowrap;">' + escapeHtml(fmtTimestamp(r.timestamp)) + '</td>' +
              '<td style="padding:0.5rem;border-bottom:1px solid var(--color-rule);">' + escapeHtml(r.name) + '</td>' +
              '<td style="padding:0.5rem;border-bottom:1px solid var(--color-rule);">' + escapeHtml(r.email) + '</td>' +
              '<td style="padding:0.5rem;border-bottom:1px solid var(--color-rule);">' + escapeHtml(r.role) + '</td>' +
              '<td style="padding:0.5rem;border-bottom:1px solid var(--color-rule);">' + escapeHtml(r.institution) + '</td>' +
            '</tr>'
          ).join("") +
        '</tbody>' +
      '</table>' +
    '</div>';

  document.getElementById("admin-search").addEventListener("input", applyFilters);
  document.getElementById("admin-role-filter").addEventListener("change", applyFilters);
  document.getElementById("admin-export").addEventListener("click", exportCsv);
  document.getElementById("admin-signout").addEventListener("click", () => signOut(auth));
}

function applyFilters() {
  const term = document.getElementById("admin-search").value.trim().toLowerCase();
  const role = document.getElementById("admin-role-filter").value;
  const filtered = allRows.filter((r) => {
    if (role && r.role !== role) return false;
    if (term) {
      const hay = (r.name + " " + r.email + " " + r.institution).toLowerCase();
      if (!hay.includes(term)) return false;
    }
    return true;
  });
  drawTable(filtered);
}

function exportCsv() {
  const term = document.getElementById("admin-search").value.trim().toLowerCase();
  const role = document.getElementById("admin-role-filter").value;
  const rows = allRows.filter((r) => {
    if (role && r.role !== role) return false;
    if (term) {
      const hay = (r.name + " " + r.email + " " + r.institution).toLowerCase();
      if (!hay.includes(term)) return false;
    }
    return true;
  });

  const header = ["timestamp", "name", "email", "role", "institution", "referrer", "user_agent"];
  const csvRows = [header.join(",")];
  for (const r of rows) {
    csvRows.push(header.map((k) => csvCell(k === "timestamp" ? fmtTimestamp(r.timestamp) : r[k])).join(","));
  }
  const csv = csvRows.join("\n");

  const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "access_log_" + new Date().toISOString().slice(0, 10) + ".csv";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function csvCell(v) {
  const s = String(v == null ? "" : v);
  if (/[",\n\r]/.test(s)) return '"' + s.replace(/"/g, '""') + '"';
  return s;
}
