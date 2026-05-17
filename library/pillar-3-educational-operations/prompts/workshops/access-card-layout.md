---
title: Access card layout
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: design, access-cards
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Specify a printable access card layout for workshop attendees with QR code, name, role, and event branding.

## When to use it

When attendees need a card that grants access to a companion site, a Slack channel, or other workshop resources. Pairs with the badge but is more durable and portable.

## The prompt

```
Specify a print layout for an attendee access card for [workshop name].

The card should be **the size of a business card or hotel keycard** (specify exactly) and include:

1. Front of card:
   - Workshop title and date.
   - Attendee name (placeholder for personalization).
   - A QR code linking to [specific URL — e.g., the companion site, a Slack invite, the workshop schedule].
   - Event branding (color, logo if applicable).
2. Back of card:
   - 1-3 line description of what scanning the QR gets the attendee.
   - Any usage instructions (e.g., 'access valid through [date]', 'one-time use').
   - Contact for help.

Include:

- Exact dimensions and bleed area.
- QR code size minimum to ensure scannability (typically 1 inch / 25mm minimum).
- Font sizes for name vs body text.
- File format expected by your print shop (PDF, AI, etc.).

End with a sample of the front and back as ASCII art so I can visualize the layout.
```

## Expected output

Full specification + visualized layout. Should be print-shop-ready.

## Common failure modes

- QR code too small to scan reliably.
- No fallback instruction if the QR doesn't work (e.g., 'or visit [URL]').
- Layout is busy and the QR is hard to find.

## Required human verification

- Print one prototype and scan the QR with multiple phone types and lighting conditions.
- Verify the URL is correct and resolves to the intended destination.
