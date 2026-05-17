---
title: Certificate of completion template
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: design, certificates
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-17
---

## What this prompt does

Draft a certificate of completion template with attestation language, signature blocks, and a layout brief.

## When to use it

The week before the workshop, so certificates can be printed (or set up for digital delivery) ahead of the closing session.

## The prompt

```
Draft a certificate of completion template for [workshop name] on [date], held at [location].

The certificate should include:

1. Standard certificate header: 'Certificate of Completion' or equivalent.
2. **Attestation language**: 'This certifies that [Name] has successfully completed [workshop title] on [date] in [city]', with the workshop's hour count if applicable.
3. **Learning outcomes**: list the workshop's stated objectives (so the certificate documents what the attendee was certified to have completed).
4. **Issuing organization** with logo placeholder.
5. **Signature blocks**: typically 1-2 signers (workshop director, institutional sponsor). Include printed name, title, and signature line.
6. **Authentication elements**: certificate number, QR code linking to a verification page (optional), date of issue.

Layout brief:
- Orientation (landscape recommended for certificates).
- Suggested font (a serif display face for traditional feel; a clean sans-serif for modern).
- Color palette (institutional colors or neutral palette).
- Border style (none, simple line, classical ornament).

Produce both:
1. The plain-text content with placeholders for name and date.
2. A layout brief that a designer could use to produce the visual template.

Avoid CME claims unless I've specified the workshop is CME-accredited.

**Important — refinement:** Do NOT include CME, MOC, or any continuing education credit language unless I have explicitly confirmed the workshop is accredited for that credit. False credit claims are a regulatory issue.
```

## Expected output

The text content + the visual layout brief. Together they enable production of the certificate.

## Common failure modes

- Includes CME credit claims without verifying accreditation.
- Attestation language is so generic the certificate is meaningless.
- Learning outcomes section is omitted, reducing the certificate's documentary value.

## Required human verification

- If claiming CME or any continuing education credit, verify accreditation status before including.
- Confirm signers' titles are current.
- Have one printed prototype reviewed for any layout issues at full size.

## Best model and why

**Claude Haiku 4.5** — Template generation suits Haiku. Verify CME/accreditation language regardless of model — false credit claims are a regulatory issue, not a model issue.
