---
title: Companion App Builder — a standalone Claude Code prompt
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: advanced
time_to_use: ">10min"
visual: text-only
tags: companion-app, builder, workshop, standalone-prompt
verified_models: Claude Code (Opus 4.7), Claude Sonnet 4.5
last_updated: 2026-05-17
---

## What this is

This file is a **standalone, self-contained prompt** that you can paste into Claude Code (or any sufficiently capable agentic coding tool) to build a workshop companion website similar to the one you are reading this on.

It is the single most reusable artifact in the entire library. Every other prompt here helps you generate *content*. This one helps you generate a working *site*.

The output is a deployable companion app suitable for any single-day or multi-day educational event in pathology — workshops, courses, conference tracks. It is opinionated about the architecture (static site on GitHub Pages, backend on Firebase, no marketing analytics, append-only access log) because those choices have been load-tested on a live event already.

## Who this is for

A pathology educator (resident, fellow, faculty, or program director) who:

- Is running a discrete educational event with 10–200 attendees
- Wants a professional companion site rather than a Google Drive folder full of PDFs
- Is comfortable creating accounts on GitHub and Firebase but has not written a website from scratch
- Has a few hours to invest in the initial setup, in exchange for an asset that can be reused for future events

You do not need to be a programmer. Claude Code will do the coding; you will do the choosing.

## What you get

A working website with:

- A landing page describing the event
- A gated access form (name, email, role, institution) that writes to a private Firestore log
- A library of event-related materials organized by topic
- An attendee dashboard during the event with personalized session schedule, materials, and contact card
- Optional features depending on what you ask for during the intake interview: in-event chat, real-time roster, pulse-checks with word cloud, exit survey with auto-generated PDF report, printable badges/certificates/access cards/roster, post-event mode with email feedback routing

The site is deployed on GitHub Pages (free) with Firebase Firestore (free tier) as the backend. Total monthly cost: **$0** for any event under a few thousand submissions.

## How to use this prompt

1. Install Claude Code (https://claude.com/claude-code) and open a terminal.
2. Make an empty directory for your project: `mkdir my-event-companion && cd my-event-companion`
3. Start Claude Code in that directory.
4. Paste the **entire prompt below** as your first message.
5. Claude Code will run a 7-phase orchestration. It will ask you intake questions, scaffold the site, walk you through Firebase, write the content, and deploy. Expect 2–4 hours of your time over 1–2 sessions.

---

## THE PROMPT TO PASTE

```
You are building a workshop companion website for an educational event in pathology.
You will run a seven-phase orchestration. Confirm each phase complete before moving
to the next. Assume I am semi-technical, have a GitHub account, and have never used
Firebase.

ARCHITECTURE — non-negotiable defaults:
- Static site hosted on GitHub Pages
- Firebase Firestore for the access log and any real-time features
- Firebase Auth (email/password) for an admin dashboard, single admin user
- Firebase App Check (reCAPTCHA v3) protecting Firestore writes from bots
- No marketing analytics, no tracking pixels, no third-party tags
- All fonts self-hosted
- Markdown content rendered client-side via marked.js + DOMPurify, vendored
  locally with SRI hashes (no runtime CDN dependency)
- CC-BY-4.0 license

PHASE 1 — INTAKE INTERVIEW
Run a structured intake interview. Ask these question batches one batch at a time,
wait for answers, then ask the next batch. Do not start building until intake is
complete.

Batch 1 — Event basics
- Event title (full and short form)
- Event subtitle / tagline
- Event date(s) and venue (city, institution)
- Lead organizer name, institution, professional email
- Co-organizers (name, institution, role) — list as many as relevant
- One-paragraph event description

Batch 2 — Attendees
- Expected attendee count
- Primary audience (resident / fellow / faculty / program director / mixed)
- How will attendees register beforehand (existing platform, this site's form, both)
- Will you collect any pre-event data beyond name/email/institution/role
- Will the site need to handle GDPR-style EU attendees (yes/no/unknown)

Batch 3 — Schedule structure
- Single-day / multi-day
- Single track / multi-track / station-based
- Approximate number of sessions, stations, or modules
- Will sessions have assigned facilitators (yes/no)
- Will attendees be assigned to specific stations or rotations (yes/no — if yes,
  ask how the assignment is made)

Batch 4 — Features (pick all that apply)
- Pre-event access materials gated behind a sign-in form
- Day-of personalized dashboard for each attendee
- In-event chat / Q&A
- Real-time roster ("who is here today")
- Pulse-checks with optional word cloud
- Exit survey with auto-generated PDF report
- Printable assets: badges, certificates of attendance, access cards, roster
- Post-event mode: materials remain available, feedback routes to the
  organizer's email, the access log freezes to read-only

Batch 5 — Branding
- Primary color (or pick from: deep navy, charcoal, deep teal)
- Accent color (or pick from: burgundy, terracotta, muted gold)
- Background (white / cream / off-white)
- Headline font (serif preferred for editorial feel — Cormorant Garamond,
  Playfair, EB Garamond)
- Body font (Inter, IBM Plex Sans, Source Sans 3)
- Will you provide a logo (yes/no — if yes, ask for dimensions and ratio
  preference)
- Will you provide a headshot for the lead organizer (yes/no)

Batch 6 — Communications
- What email do post-event feedback messages route to
- What is the preferred suggested-citation format for any materials downloaded
  from the site
- Do you want a printable QR code on the final slide of the workshop (yes/no —
  if yes, generate one in Phase 6)

PHASE 2 — CONFIGURATION ASSEMBLY
Assemble the intake answers into a single config object. Echo it back to me for
confirmation before scaffolding.

PHASE 3 — DASHBOARD GENERATION
Generate the file structure for the site:

  /index.html           — landing page with access form
  /thank-you.html       — post-form library home with personalized greeting
  /library.html         — markdown viewer (renders any .md file in the repo)
  /dashboard.html       — day-of attendee dashboard (only built if Phase 1
                          Batch 4 includes the dashboard feature)
  /admin.html           — Firebase-Auth-gated admin dashboard
  /404.html             — styled not-found page
  /assets/css/styles.css
  /assets/js/firebase-config.js
  /assets/js/access-gate.js
  /assets/js/library-router.js
  /assets/js/admin.js
  /assets/js/dashboard.js          (if dashboard feature requested)
  /assets/vendor/marked.min.js     (with SRI hash)
  /assets/vendor/dompurify.min.js  (with SRI hash)
  /assets/fonts/                   (with download-fonts.sh and a README)
  /content/                        (markdown files for the library)
  /firebase/firestore.rules
  /firebase/SETUP.md               (the console walkthrough I will use)
  /docs/about.md, /docs/citation.md, /docs/guardrails.md
  /docs/how-to/index.md, /docs/how-to/use-this-library.md (+ further tutorials)
  /PRIVACY.md
  /README.md
  /LICENSE                         (CC-BY-4.0)
  /.gitignore

Build the CSS with the colors and fonts from intake. Wire all five HTML pages
with the masthead, footer, and navigation appropriate to the event.

PHASE 4 — CLOUD SETUP WALKTHROUGH
Write firebase/SETUP.md as a 9-step console walkthrough covering:
  1. Create Firebase project (3 min)
  2. Register web app (2 min)
  3. Enable Firestore (3 min)
  4. Enable Auth, create admin user, copy admin UID (3 min)
  5. Enable App Check + reCAPTCHA v3, enforce on Firestore (5 min)
  6. Lock authorized domains (1 min)
  7. Paste config into firebase-config.js (2 min)
  8. Paste admin UID into firestore.rules and deploy (3 min)
  9. Five smoke tests: happy-path write, direct-write rejection, admin read
     while signed out, append-only enforcement, admin sign-in flow (5 min)

The Firestore rules MUST enforce: shape validation on create (required fields,
length caps, role enum, server-set timestamp); admin-UID-only on read/list;
update and delete denied for everyone (append-only).

Walk me through the steps in sequence. Pause for me to complete each one.

PHASE 5 — CONTENT CUSTOMIZATION
Populate the /content/ directory with the event-specific material:
- Session descriptions (one .md file per session, with frontmatter)
- Speaker bios
- Reading list with rationale
- Pre-event prep materials
- Day-of agenda
- Post-event feedback routing
For each content type, ask me what raw material I have and either ingest it
(if I paste it) or generate placeholders for me to fill in. Do NOT fabricate
educational content — placeholders only for anything I cannot supply.

PHASE 6 — PRE-EVENT REHEARSAL
Run a pre-event rehearsal:
- Open the live site in a fresh browser
- Submit the access form as a test attendee
- Verify the Firestore document appears with a server timestamp
- Sign into the admin dashboard, see the test entry, export CSV
- Verify the personalized dashboard greets the test attendee correctly
- Verify mobile responsiveness on a phone
- Generate a high-resolution QR code (1000×1000+, error correction level H)
  pointing to the live URL, suitable for the final slide of the workshop
- Print one test badge, one test certificate, one test access card (if those
  features were requested)
- Verify CSP, SRI, and the security checklist (below) are all green

Security checklist:
[ ] No service account keys or .env files in the repo
[ ] Firestore rules tested with a malformed payload (should reject)
[ ] App Check enforcement ON for Firestore
[ ] Append-only verified: update/delete denied even as admin
[ ] Admin dashboard requires Firebase Auth sign-in (no client passphrase)
[ ] CSP meta tag on all HTML pages
[ ] SRI hashes on all vendored JS
[ ] All fonts self-hosted
[ ] No analytics or tracking
[ ] DOMPurify sanitizes all rendered markdown
[ ] PRIVACY.md linked from access form and footer
[ ] GitHub branch protection on main

PHASE 7 — DAY-OF & POST-EVENT PLAYBOOK
Generate a one-page playbook covering:
- 30-minute pre-event check (live site, Firestore is accepting writes, admin
  dashboard works)
- During-event monitoring (admin tab open, CSV export schedule if needed)
- End-of-event tasks (lock the access log to read-only via a rules update,
  enable post-event mode, send the thank-you email, archive the access log
  to Cloud Storage)
- Post-event maintenance (when to take the site down, how to repurpose for
  the next event, how to delete attendee data on request per the privacy
  notice)

GUARDRAILS — apply to everything you generate:
- No patient data, no identifiable cases, no institutional exam content
- No fabricated quotes, biographies, citations, or images
- No emoji decoration
- No "powered by AI" footer credit — this is the organizer's professional work
- All content stays in the organizer's voice; you scaffold but do not author

DELIVERABLES:
At the end of Phase 7, summarize: the live URL, the GitHub repo URL, the
Firebase project ID, the admin email, the QR code file location, and any
TODO items for the organizer to complete before launch.

Begin with Phase 1. Ask Batch 1 of the intake interview now.
```

---

## Where this came from

This prompt was originally derived from the work that built the AI in Pathology Education Companion Library you are currently using (built for the API Summit 2026 workshop). The 7-phase structure, the security model, the Firestore append-only design, and the intake interview format have been tested on at least one live event and refined accordingly.

## Attribution

If you build a site with this prompt and publish, share, or write about the work, please cite:

> Baba, O. Z. (2026). *AI in Pathology Education — Companion Library: Companion App Builder*. API Summit 2026. Licensed under CC BY 4.0.

If you use this prompt at your institution and would like to share what you built, contact the author — collected feedback is informing a manuscript on AI-assisted educational infrastructure.

## What this prompt does NOT do

- It does not write your event's substantive content. You bring the session descriptions, the speaker list, the reading materials.
- It does not handle payment processing, complex registration logic (waitlists, tiered pricing), or CME credit awarding. Those need real registration platforms.
- It does not replace IRB review or institutional approvals for educational research.
- It does not provide HIPAA-grade infrastructure. The site is appropriate for educational event coordination, not for any workflow that touches protected health information.

## Getting help

- Firebase: https://firebase.google.com/docs
- GitHub Pages: https://docs.github.com/pages
- reCAPTCHA v3: https://developers.google.com/recaptcha/docs/v3
- Claude Code: https://claude.com/claude-code
