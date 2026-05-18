---
title: Badge design specifications
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: design, badges, accessibility
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-18
---

## What this prompt does

Drafts a printable badge spec: dimensions, fields, font sizes (meeting WCAG accessibility minimums for name visibility), color palette, lanyard/holder type, and a 10% buffer quantity for last-minute attendees and reprints.

## When to use it

3-4 weeks before the workshop, when you're placing print orders.

## The prompt

```
You are drafting a badge print spec. Name font ≥24pt for in-person events (legible from across a room). Order with 10% buffer.

## What I'm producing

- **Workshop name + date:** [name + date]
- **Expected attendee count:** [N]
- **Print method:** [in-house printer / professional print shop]
- **Holder type preference:** [lanyard / clip / pin]
- **Branding constraints:** [institutional colors, logo placement requirements]

## What to produce

### Dimensions
- Physical size (mm or inches)
- Orientation (portrait or landscape)
- Bleed area if professionally printed

### Required fields with position and font size
- Name (largest type, top)
- Institution (smaller, below name)
- Role (e.g., "Faculty" / "Attendee" / "Staff")
- Date or event name
- Logo placement (if applicable)

### Optional conditional fields
- Color coding (faculty / attendee / staff)
- Table or group assignment
- Dietary marker
- Pronouns line

### Color palette
- Specific colors with hex codes (defaults if I don't specify)
- Verify WCAG AA contrast for text on background

### Font
- Sans-serif legible at distance
- Name in ≥24pt
- Institution in ≥14pt

### Lanyard / holder
- Type (clip, lanyard, pin)
- Hole position
- Paper weight or material recommendation

### Quantity to order
- N attendees + 10% buffer + 5-10 spare for staff/walk-ins

### Print-shop-ready summary
A single-paragraph summary I can paste into an order form.

## Hard rules

- **Name font ≥24pt.** Non-negotiable for in-person events.
- **WCAG AA contrast.** Verify the color combinations.
- **10% buffer minimum.**
- **Specific holder type matched to badge dimensions.**

## What I will NOT accept

- Name fonts that won't be legible across a room
- Missing buffer quantity
- Color combinations that fail contrast
```

## Expected output

A complete spec + a print-shop-ready summary paragraph.

## Required human verification

- Print one prototype and test legibility from 6 feet.
- Verify holder type matches badges you're ordering.

## Best model and why

**Claude Haiku 4.5** — print spec is fast and structured.
