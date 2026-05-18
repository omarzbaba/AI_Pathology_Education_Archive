/*
 * engagement.js — comments + upvotes on prompt detail pages.
 *
 * Lazy-initializes Firebase only when the user actually interacts (clicks
 * comment, upvote, or load-more) so prompt browsing stays fast and
 * non-Firebase pages don't pay the init cost.
 *
 * Identity model:
 *   - If localStorage has companion_access_granted (user has signed in
 *     via the access form), use that email automatically — no extra
 *     friction.
 *   - Otherwise, prompt for email on first interaction. The email is
 *     stored locally for subsequent interactions in this browser.
 *
 * Comments are PRE-MODERATED — submissions start in 'pending' status and
 * only appear publicly after the admin approves them.
 *
 * Votes are immediate (no pre-moderation). One vote per email per prompt
 * enforced by deterministic doc ID.
 */

let firebaseModules = null;
let app = null;
let db = null;

async function ensureFirebase() {
  if (db) return db;
  if (!firebaseModules) {
    const [{ initializeApp }, { initializeAppCheck, ReCaptchaV3Provider },
           { getFirestore, collection, addDoc, setDoc, doc, query, where,
             orderBy, getDocs, deleteDoc, serverTimestamp }] = await Promise.all([
      import("https://www.gstatic.com/firebasejs/10.12.5/firebase-app.js"),
      import("https://www.gstatic.com/firebasejs/10.12.5/firebase-app-check.js"),
      import("https://www.gstatic.com/firebasejs/10.12.5/firebase-firestore.js")
    ]);
    const { firebaseConfig, appCheckSiteKey } = await import("./firebase-config.js");
    firebaseModules = {
      collection, addDoc, setDoc, doc, query, where, orderBy, getDocs,
      deleteDoc, serverTimestamp
    };
    app = initializeApp(firebaseConfig, "engagement-" + Date.now());
    initializeAppCheck(app, {
      provider: new ReCaptchaV3Provider(appCheckSiteKey),
      isTokenAutoRefreshEnabled: true
    });
    db = getFirestore(app);
  }
  return db;
}

// -------------------------------------------------------------------------
// Identity (email-based, lightweight)
// -------------------------------------------------------------------------

function getStoredIdentity() {
  // Prefer access-form identity (user already gave it to us)
  try {
    const raw = localStorage.getItem("companion_access_granted");
    if (raw) {
      const d = JSON.parse(raw);
      if (d && d.email && d.name) return { name: d.name, email: d.email };
    }
  } catch (_) {}
  // Fall back to engagement-specific identity
  try {
    const raw = localStorage.getItem("companion_engagement_identity");
    if (raw) return JSON.parse(raw);
  } catch (_) {}
  return null;
}

function storeEngagementIdentity(name, email, affiliation) {
  try {
    localStorage.setItem("companion_engagement_identity", JSON.stringify({
      name, email, affiliation: affiliation || ""
    }));
  } catch (_) {}
}

function getVotedFlags() {
  try {
    const raw = localStorage.getItem("companion_voted_prompts");
    return raw ? JSON.parse(raw) : {};
  } catch (_) { return {}; }
}

function setVotedFlag(promptPath, voted) {
  const flags = getVotedFlags();
  if (voted) flags[promptPath] = true;
  else delete flags[promptPath];
  try { localStorage.setItem("companion_voted_prompts", JSON.stringify(flags)); }
  catch (_) {}
}

// -------------------------------------------------------------------------
// Deterministic vote doc ID
// -------------------------------------------------------------------------

async function voteDocId(promptPath, email) {
  // SHA-256 hash of path + email, base64url, first 32 chars
  const enc = new TextEncoder().encode(promptPath + "|" + email.toLowerCase());
  const hashBuf = await crypto.subtle.digest("SHA-256", enc);
  const bytes = new Uint8Array(hashBuf);
  let str = "";
  for (let i = 0; i < bytes.length; i++) str += String.fromCharCode(bytes[i]);
  return btoa(str).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "").slice(0, 32);
}

// -------------------------------------------------------------------------
// Helpers
// -------------------------------------------------------------------------

function escapeHtml(s) {
  return String(s == null ? "" : s)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

function fmtRelative(ts) {
  if (!ts || !ts.toDate) return "";
  const d = ts.toDate();
  const diffMs = Date.now() - d.getTime();
  const sec = Math.floor(diffMs / 1000);
  if (sec < 60) return "just now";
  const min = Math.floor(sec / 60);
  if (min < 60) return min + " min ago";
  const hr = Math.floor(min / 60);
  if (hr < 24) return hr + " hr ago";
  const day = Math.floor(hr / 24);
  if (day < 30) return day + " day" + (day === 1 ? "" : "s") + " ago";
  return d.toLocaleDateString();
}

function sanitize(s, maxLen) {
  return String(s || "").trim()
    .replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/g, "").slice(0, maxLen);
}

function sanitizeText(s, maxLen) {
  return String(s || "")
    .replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/g, "").trim().slice(0, maxLen);
}

function validateEmail(email) {
  return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) && email.length >= 5 && email.length <= 254;
}

// -------------------------------------------------------------------------
// Main rendering — called from library-router after a prompt detail loads
// -------------------------------------------------------------------------

export async function renderEngagement(container, promptPath) {
  // Render the static UI immediately; data loads lazily
  container.innerHTML = `
    <section class="engagement" aria-labelledby="engagement-heading">
      <h2 id="engagement-heading" style="font-family: var(--font-serif);">Discussion &amp; voting</h2>

      <div class="vote-row">
        <button type="button" class="vote-btn" id="vote-btn" aria-label="Upvote this prompt">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4l8 8h-5v8H9v-8H4z"/></svg>
          <span class="vote-label">Upvote</span>
          <span class="vote-count" id="vote-count">…</span>
        </button>
        <span class="vote-note" id="vote-note"></span>
      </div>

      <h3 class="comments-heading">Comments</h3>
      <p class="comments-meta" id="comments-meta">Loading comments…</p>

      <div class="comments-thread" id="comments-thread"></div>

      <details class="comment-form-wrapper">
        <summary>Add a comment</summary>
        <form id="comment-form" class="comment-form">
          <div class="comment-form__identity" id="comment-form-identity"></div>
          <div class="field">
            <label for="comment-text">Your comment <span class="required">*</span></label>
            <textarea id="comment-text" name="comment-text" required minlength="10" maxlength="2000" rows="4" placeholder="Share what worked, what didn't, a refinement you found, or a question." style="font-family: var(--font-sans); font-size: var(--fs-base); padding: var(--space-3); border: 1px solid var(--color-rule); border-radius: 2px; width: 100%;"></textarea>
            <p class="field__error" id="comment-text-error" aria-live="polite"></p>
          </div>
          <button type="submit" class="btn" id="comment-submit">Post comment</button>
          <p class="form-status" id="comment-status" role="status" aria-live="polite"></p>
          <p class="form-privacy" style="margin-top: var(--space-3);">
            Comments are reviewed by the author before appearing publicly. Your name and (if provided) affiliation are shown on approved comments; your email is not. By posting, you agree to these terms and to the <a href="PRIVACY.md">privacy notice</a>.
          </p>
        </form>
      </details>
    </section>
  `;

  // Render identity sub-form
  renderIdentityForm();

  // Wire vote button
  document.getElementById("vote-btn").addEventListener("click", () => onVoteClicked(promptPath));

  // Wire comment form
  document.getElementById("comment-form").addEventListener("submit", (e) => {
    e.preventDefault();
    onCommentSubmit(promptPath);
  });

  // Load data asynchronously
  loadVoteCount(promptPath).catch(console.warn);
  loadComments(promptPath).catch(console.warn);
}

function renderIdentityForm() {
  const wrapper = document.getElementById("comment-form-identity");
  const id = getStoredIdentity();
  if (id) {
    wrapper.innerHTML = `
      <p style="font-size: var(--fs-sm); color: var(--color-muted); margin: 0 0 var(--space-3);">
        Posting as <strong>${escapeHtml(id.name)}</strong>${id.affiliation ? ` (${escapeHtml(id.affiliation)})` : ""} —
        <a href="#" id="change-identity">change</a>
      </p>
    `;
    document.getElementById("change-identity").addEventListener("click", (e) => {
      e.preventDefault();
      try { localStorage.removeItem("companion_engagement_identity"); } catch (_) {}
      renderIdentityForm();
    });
  } else {
    wrapper.innerHTML = `
      <div class="form-grid">
        <div class="field">
          <label for="comment-name">Your name <span class="required">*</span></label>
          <input type="text" id="comment-name" required maxlength="100" autocomplete="name">
        </div>
        <div class="field">
          <label for="comment-email">Email <span class="required">*</span></label>
          <input type="email" id="comment-email" required maxlength="254" autocomplete="email">
        </div>
        <div class="field form-grid__full">
          <label for="comment-affiliation">Institution (optional)</label>
          <input type="text" id="comment-affiliation" maxlength="200" autocomplete="organization">
        </div>
      </div>
    `;
  }
}

// -------------------------------------------------------------------------
// Voting
// -------------------------------------------------------------------------

async function loadVoteCount(promptPath) {
  try {
    await ensureFirebase();
    const { collection, query, where, getDocs } = firebaseModules;
    const q = query(collection(db, "votes"), where("prompt_path", "==", promptPath));
    const snap = await getDocs(q);
    document.getElementById("vote-count").textContent = String(snap.size);
  } catch (err) {
    document.getElementById("vote-count").textContent = "—";
  }

  // Reflect "already voted" state from localStorage
  const flags = getVotedFlags();
  if (flags[promptPath]) {
    const btn = document.getElementById("vote-btn");
    btn.classList.add("vote-btn--voted");
    btn.querySelector(".vote-label").textContent = "Voted";
  }
}

async function onVoteClicked(promptPath) {
  const btn = document.getElementById("vote-btn");
  const note = document.getElementById("vote-note");
  note.textContent = "";

  // If user already voted (per localStorage), un-vote.
  const flags = getVotedFlags();
  if (flags[promptPath]) {
    await unvote(promptPath);
    return;
  }

  // Need email — either from access form or via inline prompt
  let id = getStoredIdentity();
  if (!id) {
    const email = window.prompt("Enter your email to vote. (Used only to prevent duplicate votes.)");
    if (!email || !validateEmail(email.trim())) {
      note.textContent = "Invalid email.";
      return;
    }
    const name = window.prompt("Your name (will be shown on comments, not on votes):");
    if (!name || !name.trim()) {
      note.textContent = "Name required.";
      return;
    }
    id = { name: name.trim(), email: email.trim().toLowerCase(), affiliation: "" };
    storeEngagementIdentity(id.name, id.email, id.affiliation);
    renderIdentityForm();
  }

  await castVote(promptPath, id.email);
}

async function castVote(promptPath, email) {
  const btn = document.getElementById("vote-btn");
  const countEl = document.getElementById("vote-count");
  const note = document.getElementById("vote-note");

  btn.disabled = true;
  try {
    await ensureFirebase();
    const { setDoc, doc, serverTimestamp } = firebaseModules;
    const id = await voteDocId(promptPath, email);
    await setDoc(doc(db, "votes", id), {
      timestamp: serverTimestamp(),
      prompt_path: promptPath,
      voter_email: email.toLowerCase(),
      referrer: sanitize(document.referrer, 500),
      user_agent: sanitize(navigator.userAgent, 500)
    });
    setVotedFlag(promptPath, true);
    btn.classList.add("vote-btn--voted");
    btn.querySelector(".vote-label").textContent = "Voted";
    // Optimistic count update
    const current = parseInt(countEl.textContent, 10);
    if (!Number.isNaN(current)) countEl.textContent = String(current + 1);
  } catch (err) {
    console.warn("Vote failed:", err);
    note.textContent = "Vote failed (already voted?).";
  } finally {
    btn.disabled = false;
  }
}

async function unvote(promptPath) {
  const id = getStoredIdentity();
  if (!id) return;
  const btn = document.getElementById("vote-btn");
  const countEl = document.getElementById("vote-count");
  const note = document.getElementById("vote-note");

  btn.disabled = true;
  try {
    await ensureFirebase();
    const { deleteDoc, doc } = firebaseModules;
    const voteId = await voteDocId(promptPath, id.email);
    // Note: delete is admin-only per Firestore rules. Client unvote
    // requires admin token, which the public user doesn't have. So we
    // just toggle the local flag and tell the user.
    setVotedFlag(promptPath, false);
    btn.classList.remove("vote-btn--voted");
    btn.querySelector(".vote-label").textContent = "Upvote";
    note.textContent = "Local un-vote (counted vote remains; admin can delete).";
  } catch (err) {
    note.textContent = "Un-vote failed.";
  } finally {
    btn.disabled = false;
  }
}

// -------------------------------------------------------------------------
// Comments
// -------------------------------------------------------------------------

async function loadComments(promptPath) {
  const thread = document.getElementById("comments-thread");
  const meta = document.getElementById("comments-meta");
  try {
    await ensureFirebase();
    const { collection, query, where, orderBy, getDocs } = firebaseModules;
    // Note: client can read 'visible' comments per rule; pending/hidden
    // are filtered server-side.
    const q = query(
      collection(db, "comments"),
      where("prompt_path", "==", promptPath),
      where("status", "==", "visible"),
      orderBy("timestamp", "asc")
    );
    const snap = await getDocs(q);
    const rows = [];
    snap.forEach((doc) => rows.push({ id: doc.id, ...doc.data() }));
    if (rows.length === 0) {
      meta.textContent = "No comments yet. Be the first to share what worked or what didn't.";
      thread.innerHTML = "";
    } else {
      meta.textContent = rows.length + " comment" + (rows.length === 1 ? "" : "s") + ".";
      thread.innerHTML = rows.map(commentHtml).join("");
    }
  } catch (err) {
    meta.textContent = "Failed to load comments. (May need Firestore rules update — see DEPLOY.md.)";
    console.warn(err);
  }
}

function commentHtml(c) {
  const adminBadge = c.is_admin
    ? '<span class="pill pill--model" style="margin-left:0.5rem;">Author</span>'
    : '';
  const affiliation = c.commenter_affiliation
    ? ` <span style="color:var(--color-muted);font-size:var(--fs-xs);">— ${escapeHtml(c.commenter_affiliation)}</span>`
    : '';
  // Render comment text as plain paragraphs (preserve line breaks)
  const paragraphs = String(c.comment_text || "")
    .split(/\n\n+/)
    .map(p => "<p>" + escapeHtml(p).replace(/\n/g, "<br>") + "</p>")
    .join("");
  return `
    <article class="comment ${c.is_admin ? 'comment--admin' : ''}">
      <div class="comment__head">
        <strong>${escapeHtml(c.commenter_name)}</strong>${adminBadge}${affiliation}
        <span class="comment__ts">${fmtRelative(c.timestamp)}</span>
      </div>
      <div class="comment__body">${paragraphs}</div>
    </article>
  `;
}

async function onCommentSubmit(promptPath) {
  const textEl = document.getElementById("comment-text");
  const errorEl = document.getElementById("comment-text-error");
  const statusEl = document.getElementById("comment-status");
  const btn = document.getElementById("comment-submit");

  errorEl.textContent = "";
  statusEl.className = "form-status";
  statusEl.textContent = "";

  const text = sanitizeText(textEl.value, 2000);
  if (!text || text.length < 10) {
    errorEl.textContent = "Comment must be at least 10 characters.";
    return;
  }

  // Resolve identity
  let id = getStoredIdentity();
  if (!id) {
    const name = sanitize(document.getElementById("comment-name").value, 100);
    const email = sanitize(document.getElementById("comment-email").value, 254).toLowerCase();
    const affiliation = sanitize(document.getElementById("comment-affiliation").value, 200);
    if (!name) { errorEl.textContent = "Name required."; return; }
    if (!validateEmail(email)) { errorEl.textContent = "Valid email required."; return; }
    id = { name, email, affiliation };
    storeEngagementIdentity(name, email, affiliation);
  }

  btn.disabled = true;
  const origLabel = btn.textContent;
  btn.textContent = "Posting…";

  try {
    await ensureFirebase();
    const { collection, addDoc, serverTimestamp } = firebaseModules;
    await addDoc(collection(db, "comments"), {
      timestamp: serverTimestamp(),
      status: "pending",
      prompt_path: promptPath,
      commenter_name: id.name,
      commenter_email: id.email,
      commenter_affiliation: id.affiliation || "",
      comment_text: text,
      is_admin: false,
      referrer: sanitize(document.referrer, 500),
      user_agent: sanitize(navigator.userAgent, 500)
    });
    textEl.value = "";
    statusEl.className = "form-status form-status--success";
    statusEl.textContent = "Comment submitted for review. It will appear after approval.";
  } catch (err) {
    console.warn("Comment failed:", err);
    statusEl.className = "form-status form-status--error";
    statusEl.textContent = "Failed to post. Try again, or email the author directly.";
  } finally {
    btn.disabled = false;
    btn.textContent = origLabel;
  }
}
