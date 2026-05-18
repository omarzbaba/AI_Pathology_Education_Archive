---
title: Privacy and copyright for source-grounded AI
last_updated: 2026-05-18
difficulty: intermediate
category: source-grounded
---

A walk-through of the privacy, copyright, and institutional-policy considerations BEFORE you upload anything to an AI notebook. Source-grounded AI is genuinely useful for education, but it sits on top of a complicated web of copyright, vendor terms of service, and institutional data policies — most of which are unsettled, and most of which can bite you in unexpected ways.

## When to read this

The first time you're considering setting up an AI notebook with educational materials. Re-read whenever you're adding new source types you haven't uploaded before.

## The six categories

### 1. Patient material — never, under any circumstances

Do not upload to any AI notebook:

- Patient images (photomicrographs, gel images, gross photos, radiology images) from real cases — even "de-identified" ones
- Patient reports, lab results, or chart data
- Institutional case material from your sign-out, your tumor board, your resident teaching files

**Why:** vendor terms of service vary, models retrain on unknown schedules, and combinations of "de-identified" data are often re-identifiable in ways you cannot predict. The educational value of using your own case material is not worth the risk.

**Use instead:** published teaching cases, public-domain images, legitimately-cleared teaching collections. Pathology Outlines, the WHO classification image collections, society teaching sets, atlas chapters — these are designed for exactly this use.

### 2. Copyrighted textbook material — depends on access route

Textbook chapters you have legitimate access to (institutional subscription or personal purchase) sit in a gray zone:

**Probably OK:**

- Uploading a chapter you legitimately purchased, for your own personal study, to a notebook only you can access
- Fair use for personal educational purposes is generally defensible

**Probably not OK:**

- Sharing the notebook with co-residents (no longer personal use)
- Uploading material from institutional subscriptions to a personal AI account (terms of service violation for the subscription)
- Uploading scanned/pirated copies of textbooks you don't have access to

**Consult your library:** your institutional librarian can tell you which of your subscriptions explicitly address AI tools. Some publishers now have specific AI-use policies; some prohibit AI training/use entirely.

### 3. Institutional protocols and unpublished material

Do not upload without explicit permission:

- Your institution's specific clinical protocols (laboratory procedures, reversal protocols, sign-out workflows)
- Unpublished case material from your service
- Internal QI documents
- Resident or faculty unpublished notes without their permission
- Drafts of manuscripts under peer review (yours or others')

**Consult your compliance office:** institutional documents may be confidential even if they don't carry an explicit "confidential" label. The default should be "ask, don't assume."

### 4. Published guidelines and society documents

**Generally OK** to upload guidelines that are publicly available:

- NCCN guidelines (verify your subscription terms)
- ASH, ASCP, CAP guideline statements when publicly accessible
- WHO classification when accessed through legitimate channels
- Open-access journal content under CC-BY licenses

**Watch out for:**

- Subscription-only versions you're accessing through your institution
- Drafts or preprints not yet formally released
- Older versions when newer ones exist (use the current one)

### 5. Your own notes — generally OK

Your own typed notes, rotation observations (de-identified), study summaries, and similar personal material:

**Generally OK** to upload, but:

- If your notes contain attending preferences or institutional specifics, treat them as institutional material (Category 3)
- If your notes contain patient details (even de-identified), treat them as patient material (Category 1) — strip them first
- If your notes contain content you'd be embarrassed to share publicly, remember that the notebook is one data leak away from public

### 6. Vendor terms of service vary — check them

Different AI vendors have different policies:

- **NotebookLM (Google):** check current terms re: data use for training
- **Claude Projects (Anthropic):** Anthropic's policies on Project data are generally favorable for educational use but read current ToS
- **OpenAI Custom GPTs:** OpenAI's training data policies have evolved — verify what's current

**The question to ask for any vendor:**

- Does my uploaded content become training data?
- Is there a way to opt out of training?
- What happens to my content if I delete the notebook?
- Are there enterprise/business tier options with stricter data segregation?

Read the terms before uploading anything sensitive.

## Bottom-line decision rubric

Before uploading any source, ask:

1. **Is this patient material in any form?** → STOP. Do not upload.
2. **Is this institutional/confidential material?** → Get permission first.
3. **Is this copyrighted material I have legitimate access to?** → Probably OK for personal use; not for sharing.
4. **Is this material I created or that's public-domain?** → Generally OK.
5. **Have I checked the vendor's current terms of service?** → Required for sensitive material.

## Common failure modes

- **"Everyone does it" reasoning.** Other residents may be uploading patient material to AI tools. Don't follow them off the cliff.
- **Treating "de-identification" as a safety guarantee.** It isn't, especially for combinations of features (rare diagnosis + age + location can re-identify).
- **Assuming institutional subscriptions cover AI use.** Most don't explicitly; many publishers have new AI-use restrictions.
- **Treating vendor ToS as static.** Policies evolve; check periodically.

## Who to ask

- **For any sensitive upload, consult your institutional librarian or compliance office.** They have specific knowledge of your institution's policies and subscriptions.
- **For copyright questions, your institutional library is the right resource.** Not the AI vendor, not your co-residents, not online forums.
- **For patient material, the answer is always no.** No verification needed.
