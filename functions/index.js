/*
 * Email notification Cloud Functions for the companion library.
 *
 * Three triggers:
 *   1. onCommentCreated   — emails admin when a new comment is submitted
 *   2. onSubmissionCreated — emails admin when a new prompt is submitted
 *   3. onSubmissionStatusChanged — emails the submitter when status changes
 *
 * Requirements:
 *   - Firebase Blaze plan (Cloud Functions require it; cost ~$0 at our scale)
 *   - Resend account with API key (free tier: 100 emails/day, 3K/month)
 *   - Verified sender domain on Resend (or use Resend's default for testing)
 *
 * Configuration:
 *   Set these via:
 *     firebase functions:config:set resend.key="re_xxx" \
 *       resend.from="notifications@yourdomain.com" \
 *       admin.email="omar@yourdomain.com" \
 *       site.url="https://omarzbaba.github.io/AI_Pathology_Education"
 *
 * Or use environment variables (v2 functions):
 *   See firebase/SETUP-EMAIL.md for the full walkthrough.
 */

const { onDocumentCreated, onDocumentUpdated } = require("firebase-functions/v2/firestore");
const { logger } = require("firebase-functions/v2");
const { defineSecret } = require("firebase-functions/params");
const { Resend } = require("resend");

const resendKey = defineSecret("RESEND_API_KEY");

// Configurable via environment params; safe defaults below
const RESEND_FROM = process.env.RESEND_FROM || "notifications@onresend.dev";
const ADMIN_EMAIL = process.env.ADMIN_EMAIL || "admin@example.com";
const SITE_URL = process.env.SITE_URL || "https://omarzbaba.github.io/AI_Pathology_Education";

function getResend() {
  return new Resend(resendKey.value());
}

function escapeHtml(s) {
  return String(s == null ? "" : s)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

// ---------------------------------------------------------------------------
// 1. New comment → email admin
// ---------------------------------------------------------------------------

exports.onCommentCreated = onDocumentCreated(
  { document: "comments/{commentId}", secrets: [resendKey] },
  async (event) => {
    const c = event.data.data();
    // Only notify on public (pending) submissions, not admin replies
    if (c.is_admin === true) return;

    try {
      const resend = getResend();
      const promptUrl = SITE_URL + "/library.html#/" + c.prompt_path;
      const adminUrl = SITE_URL + "/admin.html";

      await resend.emails.send({
        from: RESEND_FROM,
        to: ADMIN_EMAIL,
        subject: "[Companion] New comment from " + (c.commenter_name || "unknown"),
        html: `
          <h2>New comment awaiting moderation</h2>
          <p><strong>From:</strong> ${escapeHtml(c.commenter_name)}${c.commenter_affiliation ? " (" + escapeHtml(c.commenter_affiliation) + ")" : ""}</p>
          <p><strong>Email:</strong> ${escapeHtml(c.commenter_email)}</p>
          <p><strong>On prompt:</strong> <a href="${escapeHtml(promptUrl)}">${escapeHtml(c.prompt_path)}</a></p>
          <hr>
          <blockquote style="border-left: 3px solid #7A1C28; padding-left: 1rem; margin: 1rem 0;">
            ${escapeHtml(c.comment_text).replace(/\n/g, "<br>")}
          </blockquote>
          <p><a href="${escapeHtml(adminUrl)}">Open admin dashboard &rarr;</a></p>
        `
      });
      logger.info("Comment notification sent for", event.params.commentId);
    } catch (err) {
      logger.error("Failed to send comment notification:", err);
    }
  }
);

// ---------------------------------------------------------------------------
// 2. New prompt submission → email admin
// ---------------------------------------------------------------------------

exports.onSubmissionCreated = onDocumentCreated(
  { document: "prompt_submissions/{subId}", secrets: [resendKey] },
  async (event) => {
    const s = event.data.data();
    try {
      const resend = getResend();
      const adminUrl = SITE_URL + "/admin.html";

      await resend.emails.send({
        from: RESEND_FROM,
        to: ADMIN_EMAIL,
        subject: "[Companion] New prompt submission: " + (s.prompt_title || "untitled"),
        html: `
          <h2>New prompt submission</h2>
          <p><strong>Title:</strong> ${escapeHtml(s.prompt_title)}</p>
          <p><strong>From:</strong> ${escapeHtml(s.submitter_name)}${s.submitter_affiliation ? " (" + escapeHtml(s.submitter_affiliation) + ")" : ""} &lt;${escapeHtml(s.submitter_email)}&gt;</p>
          <p><strong>Pillar:</strong> ${escapeHtml(s.prompt_pillar)}</p>
          <h3>What it does</h3>
          <p>${escapeHtml(s.prompt_intent).replace(/\n/g, "<br>")}</p>
          <h3>The prompt</h3>
          <pre style="background: #f5f5f0; padding: 1rem; overflow-x: auto;">${escapeHtml(s.prompt_text)}</pre>
          <p><a href="${escapeHtml(adminUrl)}">Open admin dashboard to review &rarr;</a></p>
        `
      });
      logger.info("Submission notification sent for", event.params.subId);
    } catch (err) {
      logger.error("Failed to send submission notification:", err);
    }
  }
);

// ---------------------------------------------------------------------------
// 3. Submission status changed → email submitter
// ---------------------------------------------------------------------------

exports.onSubmissionStatusChanged = onDocumentUpdated(
  { document: "prompt_submissions/{subId}", secrets: [resendKey] },
  async (event) => {
    const before = event.data.before.data();
    const after = event.data.after.data();
    if (before.status === after.status) return; // No status change
    if (!after.submitter_email) return;

    const statusMessages = {
      approved: {
        subject: "Your prompt has been approved",
        body: "Good news — your submission has been approved and will appear in the library shortly with attribution to you."
      },
      rejected: {
        subject: "Update on your prompt submission",
        body: "After review, your submission won't be added to the library at this time. This often happens when the prompt is too generic, overlaps significantly with existing content, or falls outside the library's scope. You're welcome to revise and resubmit if you'd like."
      },
      needs_revision: {
        subject: "Your prompt submission needs revision",
        body: "Your submission shows promise but needs some revision before it can be approved. Dr. Baba will follow up directly with specific feedback within a few days."
      },
      pending: null // No need to email "back to pending"
    };

    const msg = statusMessages[after.status];
    if (!msg) return;

    try {
      const resend = getResend();
      await resend.emails.send({
        from: RESEND_FROM,
        to: after.submitter_email,
        subject: msg.subject + ": " + (after.prompt_title || "your submission"),
        html: `
          <p>Hi ${escapeHtml(after.submitter_name)},</p>
          <p>Thank you for submitting "<strong>${escapeHtml(after.prompt_title)}</strong>" to the AI in Pathology Education Companion Library.</p>
          <p>${escapeHtml(msg.body)}</p>
          <p>If you have questions, feel free to reply to this email directly.</p>
          <p>— The AI in Pathology Education team</p>
        `
      });
      logger.info("Status notification sent to submitter:", after.submitter_email, "status:", after.status);
    } catch (err) {
      logger.error("Failed to send status notification:", err);
    }
  }
);
