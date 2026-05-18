# Privacy Notice

**Last updated:** 2026-05-17

This notice describes what information the AI in Pathology Education Companion Library collects when you sign in for access, why it is collected, where it is stored, who can read it, and what your rights are.

## What we collect

The site collects information in **two distinct contexts**, each with its own purpose and rules:

### Context 1 — Access form submissions

When you submit the access form on the companion site, the following information is recorded:

- **Name** (the value you enter)
- **Email address** (the value you enter)
- **Institution** (optional — only if you provide it)
- **Role** (resident / fellow / faculty / program director / other — the value you select)
- **Referrer URL** (where you came from, if your browser provides it)
- **User agent string** (your browser identifier, automatically sent by your browser)
- **Server timestamp** (set by the database, not by your browser)

### Context 2 — Prompt submissions

When you submit a prompt via the [Submit a prompt](/submit.html) form, the following information is recorded:

- **Your name and email address** (required, so we can attribute and follow up)
- **Your institution / affiliation** (optional)
- **The prompt content itself** (title, intent, when to use it, the prompt text, expected output, failure modes, verification, suggested model, audience, difficulty, time)
- **Status** (initially "pending", updated by the admin to approved / rejected / needs revision)
- **Referrer URL and user agent** (same as access form)
- **Server timestamp**

Submitted prompt content is stored even if rejected — we keep the audit trail so that contributors can ask why their submission was declined, but rejected submissions are NOT made public.

### Context 3 — Comments on prompts

When you post a comment on a prompt detail page, the following is recorded:

- **Your name** (displayed publicly with the comment after approval)
- **Your email address** (stored privately; not displayed publicly)
- **Your institution / affiliation** (optional, displayed publicly if provided)
- **Your comment text** (displayed publicly after approval)
- **Status** (initially "pending"; admin reviews and sets to "visible" or "hidden")
- **Referrer URL and user agent**
- **Server timestamp**

Comments are **pre-moderated** — they do not appear publicly until the author has reviewed and approved them. Once visible, comments can be set back to "hidden" by the author (the content remains stored for audit purposes but is not displayed). The author cannot delete comments outright; the audit trail is preserved.

### Context 4 — Feedback messages

When you click the floating **Feedback** button on any page and send a message:

- **Your name and email** if you've already provided them via the access form, or what you type into the optional fields if you haven't (both fields are optional; anonymous feedback is allowed)
- **Your message text**
- **The page URL you were on** when you sent the message (helps the author triage bug reports)
- **Status** (initially "new"; the author marks it "triaged" or "resolved" as they work through the queue)
- **Referrer URL and user agent**
- **Server timestamp**

Feedback messages are admin-only; they are never displayed publicly. If you provide an email, the author may reply directly.

### Context 5 — Votes on prompts

When you upvote a prompt:

- **Your email address** is stored as part of a vote record (one vote per email per prompt, enforced by deterministic record ID)
- **The prompt voted on**
- **Server timestamp**
- **Referrer URL and user agent**

The email is used to prevent duplicate voting; it is not displayed publicly. Vote counts are public; individual votes are not attributed in any public display.

If you provided your email via the access form or a comment, it is reused for voting so you don't need to enter it again.

### What's the same across both contexts

No other information is collected. The site does not load analytics scripts, tracking pixels, third-party tags, or social-media widgets. The site does not write tracking cookies. The only browser storage used is a single localStorage entry that holds your first name (for personalized greeting) and a flag that you've already signed in.

## Why we collect it

The information is collected so the author can study how the library is used and cite that usage in a forthcoming manuscript on structured AI literacy in pathology training. The aggregate usage data is part of the manuscript's evidence base.

The information will not be used for marketing, will not be sold or transferred, and will not be shared with third parties.

## Where it is stored

The information is stored in Google Firebase Firestore, hosted in a Google Cloud data center in the United States. Google's data processing terms apply to Firestore. Google does not have a contractual research-use of your information; they store it on the author's behalf.

The database is configured so that:

- Only the author can read the data (enforced by Firebase Authentication and Firestore security rules)
- **Access form entries** cannot be edited or deleted by anyone after submission (append-only, enforced at the database rule layer)
- **Prompt submissions and comments** are immutable in their content fields (only the status field can be updated). The admin can permanently delete a row to remove spam, off-topic noise, or test entries; deletion is logged in the admin's own activity but the deleted row is gone from Firestore.
- Submissions require a valid App Check token (reCAPTCHA v3), which prevents automated bots from filling either collection

### Sub-processors

When email notifications are enabled (optional; see `firebase/SETUP-EMAIL.md`):

- **Resend** (https://resend.com) is used to deliver transactional emails: new-comment notices and new-submission notices to the author, and submission-status updates to contributors. The recipient address, the name you submitted, the prompt content (for submissions), and your comment text (for comments) are transmitted to Resend's servers (US-based) for delivery. Resend retains delivery logs per their privacy policy.

If email notifications are disabled, no sub-processor receives your information; everything stays inside Google Firebase.

## How long we keep it

The data is retained for:

- The active period of the manuscript project, **plus**
- Five years after the manuscript is published or formally abandoned

After that, the database will be deleted. Periodic CSV exports may be retained for the author's archival purposes per the same five-year retention schedule.

## Who can read it

- **The author (Omar Z. Baba, MD)** can read all entries through an authenticated admin dashboard.
- **No one else** — not co-authors, not the author's institution, not Google personnel in the ordinary course of business — can read individual entries.
- **Anonymized aggregate counts** (e.g., "237 residents, 84 faculty, 19 program directors, representing 96 distinct institutions") may appear in the manuscript or in derivative scholarly work. Individual rows will not.

## Your rights

You can ask the author at any time to:

- Receive a copy of the information collected about you
- Correct any inaccuracy in the information you submitted (since the log is append-only, this is handled by adding a corrected entry and noting the prior as superseded)
- Delete the information collected about you

To exercise any of these rights, email the author. Identify yourself with the email address you used to sign in (so we can locate the right entry). Requests will be honored within 30 days.

If you are in the European Union or the United Kingdom, the General Data Protection Regulation (GDPR) and UK Data Protection Act apply. The rights described above (access, rectification, erasure) correspond to your GDPR rights of access (Article 15), rectification (Article 16), and erasure (Article 17). The lawful basis for processing is your consent, which you give by submitting the form, and which you can withdraw at any time by requesting deletion.

If you have a complaint about how your data has been handled and you are in the EU/UK, you have the right to lodge a complaint with your supervisory authority (e.g., the UK ICO).

## What we do not do

- We do not require the form to read library content. The library is publicly available on GitHub. The form is a courtesy gate for tracking and personalization, not real access control. You can browse the underlying repository directly without ever submitting the form.
- We do not run advertising. There are no ads on this site and will not be.
- We do not place affiliate links. Any external links are editorial.
- We do not sell, license, lease, transfer, or otherwise commercialize your information.
- We do not aggregate your information with third-party data sets.

## Contact

Omar Z. Baba, MD
Clinical Pathology & Informatics

You can reach the author via the GitHub repository for this library (https://github.com/omarzbaba/AI_Pathology_Education) or through the floating **Feedback** button on any page of the companion site.

## Updates to this notice

If this notice changes materially (new data collected, different retention period, different access policy), the change will be reflected here with an updated "Last updated" date at the top of the page, and a brief change log will be appended below.

## Change log

- **2026-05-17:** Initial notice.
- **2026-05-18:** Added sub-processor section noting Resend (optional, only when email notifications are enabled).
- **2026-05-18:** Admin can now permanently delete prompt submissions and comments (previously only status-change was possible). Used for spam, off-topic noise, and test entries. Access-form entries remain strictly append-only.
- **2026-05-18:** Added the **feedback** collection (Context 4 above) — a floating Feedback button on every page collects bug reports, suggestions, and questions for the author. Anonymous submissions allowed; if you include an email the author may reply. Admin-only read.
- **2026-05-18:** Added a **returning-visitor email lookup**. If you've already signed in once and later clear your browser or switch devices, you can re-enter just your email and a server-side Cloud Function (running in our Firebase project, no third-party sub-processor) looks up the existing access_log entry and restores access. The function only echoes back the name, role, and institution you previously provided; it never returns referrer, user agent, or timestamps. The function requires a valid App Check token to prevent automated email enumeration.
