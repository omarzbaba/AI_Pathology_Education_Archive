---
title: Certificate of completion template
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: design, certificates, accreditation
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-18
---

## What this prompt does

Drafts a certificate of completion template with attestation language, signature blocks, optional authentication elements (certificate number, QR code), and a designer-ready layout brief. Strict rule: NO CME, MOC, or continuing education credit language unless accreditation is confirmed.

## When to use it

The week before the workshop, so certificates can be printed or set up for digital delivery ahead of the closing session.

## The prompt

```
You are drafting a certificate of completion template. Do NOT include CME, MOC, or continuing education credit claims unless I have confirmed accreditation. False credit claims are a regulatory issue.

## What I'm producing

- **Workshop name + date + location:** [name + date + city]
- **Accreditation status:** [CME-accredited / not accredited / pending — be specific]
- **Hour count (if applicable):** [N hours]
- **Issuing organization:** [name + logo availability]
- **Signers (typically 1-2):** [names + titles]
- **Workshop learning outcomes:** [from the announcement — to be listed on certificate]
- **Format:** [printable / digital / both]

## What to produce

### The certificate content (plain text with placeholders)

1. **Header:** "Certificate of Completion" or equivalent
2. **Attestation language:** "This certifies that [Name] has successfully completed [workshop title] on [date] in [city]" with hour count if applicable
3. **Learning outcomes:** the workshop's stated objectives (so the cert documents what was completed)
4. **Issuing organization:** name + logo placeholder
5. **Signature blocks:** for each signer — printed name, title, signature line
6. **Authentication elements (optional):**
   - Certificate number (if generating unique IDs)
   - QR code linking to verification page (if you have one)
   - Date of issue

### Layout brief (for a designer or for you to lay out)

- Orientation (landscape recommended)
- Suggested font (serif display for traditional; clean sans-serif for modern)
- Color palette (institutional colors or neutral)
- Border style (none / simple line / classical ornament)
- Paper recommendation if printed

## Hard rules

- **Do NOT include CME, MOC, or any continuing education credit language unless explicitly confirmed accredited.** False credit claims are a regulatory matter.
- **Hour count only if accurate and documented.**
- **Signers' titles current and accurate.**
- **Authentication elements optional — but if used, the verification page must actually exist before going live.**

## What I will NOT accept

- Implied or false credit claims
- Inaccurate hour count
- Authentication elements without a working verification page
```

## Expected output

Plain-text content + layout brief.

## Required human verification

- Verify accreditation status with your CME/CE office before including any credit language.
- Confirm signers' titles are current.
- Print one prototype at full size and review.

## Best model and why

**Claude Haiku 4.5** — template generation.
