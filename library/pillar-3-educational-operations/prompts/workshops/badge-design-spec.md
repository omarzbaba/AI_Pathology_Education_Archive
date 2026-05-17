---
title: Badge design specifications
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: design, badges
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-17
---

## What this prompt does

Draft a specification for printable workshop badges — fields, dimensions, color, accessibility, and print-shop-ready dimensions.

## When to use it

3-4 weeks before the workshop, when you're ordering supplies and need a spec to send to the print shop or graphic designer.

## The prompt

```
Draft a print specification for workshop attendee badges. Workshop: [name and date].

The spec should include:

- **Dimensions:** physical size of the badge (mm or inches), orientation (portrait/landscape), bleed area if printed professionally.
- **Required fields:** what appears on the badge (name in large type, institution in smaller type, role, date or event name, etc.) with the relative font size and position of each.
- **Optional fields:** any conditional content (faculty/attendee/staff color coding, table assignment, dietary marker if used).
- **Color palette:** specific colors with hex codes; reasonable defaults if I don't specify.
- **Font:** legible at distance, with size minimums for accessibility (e.g., name in 24-32pt).
- **Lanyard / holder type:** clip vs lanyard, hole position, paper weight or material.
- **Quantity to order** with at least 10% buffer for last-minute attendees and reprints.

End with a print-shop-ready summary I can paste into an order form.

**Important — refinement:** Verify font size meets accessibility minimums: name in ≥24pt for in-person events (legible from across a room). If institutional branding requirements conflict with accessibility, name the conflict explicitly.
```

## Expected output

A spec document plus a print-shop summary. Should be unambiguous enough that two designers would produce identical badges.

## Common failure modes

- Font sizes too small to read from across a room.
- No buffer quantity, so you run out at registration.
- Color choices that don't meet WCAG contrast for the text-on-background.

## Required human verification

- Print one prototype and test legibility from 6 feet.
- Verify the lanyard/holder type matches the badges you're ordering.

## Best model and why

**Claude Haiku 4.5** — Print specification is fast and structured. Haiku is sufficient and cheap.
