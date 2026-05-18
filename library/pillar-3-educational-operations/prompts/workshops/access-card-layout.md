---
title: Access card layout
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: design, access-card, qr-code
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-18
---

## What this prompt does

Specifies a printable access card (business card or keycard size) with a QR code linking to the companion site, attendee name, usage instructions, and contact-for-help info. Enforces ≥25mm QR code with error correction level H so it survives imperfect printing and low-light scanning.

## When to use it

2-3 weeks before the workshop, paired with the badge order.

## The prompt

```
You are specifying a printable access card. QR code ≥25mm, error correction level H. Include a fallback URL in case QR fails.

## What I'm producing

- **Workshop name + date:** [name + date]
- **QR code destination URL:** [the companion site or specific resource]
- **Attendee count:** [N]
- **Card size:** [business card / hotel keycard / custom]
- **Branding:** [institutional colors, logo placement]

## What to produce

### Card dimensions and bleed area

### Front of card
- Workshop title + date
- Attendee name placeholder
- QR code (≥25mm square, error correction level H)
- Event branding (color, logo)

### Back of card
- 1-3 line description of what the QR opens
- Usage instructions (validity period, single-use vs persistent)
- Fallback URL (printed in small but legible text in case QR fails)
- Contact for help

### Print specifications
- File format expected (PDF, AI, etc.)
- Color profile
- Paper recommendation (card stock weight)

### ASCII art preview
A sketch of the front and back so I can visualize before ordering.

### Order quantity
Attendee count + 10% buffer.

## Hard rules

- **QR code ≥25mm with error correction H.** Smaller codes fail in real-world printing.
- **Fallback URL printed legibly.** QR codes fail; the URL is the safety net.
- **Validity instructions explicit** if access is time-limited.

## What I will NOT accept

- QR code <25mm
- Missing fallback URL
- Vague validity instructions
```

## Expected output

Full specification + ASCII preview + order quantity.

## Required human verification

- Print one prototype and scan the QR with multiple phone types and lighting conditions.
- Verify the URL resolves to the intended destination.
- Confirm fallback URL is correct.

## Best model and why

**Claude Haiku 4.5** — fast structured spec.
