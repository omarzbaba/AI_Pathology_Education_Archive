---
title: Rotation orientation one-pager
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: orientation, onepager
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generate a one-page rotation orientation covering schedule, expectations, key contacts, and what success looks like by day 5.

## When to use it

Send to incoming residents the week before they start a rotation. The goal is to remove the 'I don't know what I don't know' fog of the first day.

## The prompt

```
Generate a one-page orientation document for the [rotation name] rotation. Audience: [PGY level] residents starting the rotation.

The page should fit on one printed page (so be ruthless about what to include). Sections:

1. **Welcome and orientation logistics** (3-4 sentences): when and where to arrive on day 1, who to find, what to bring.
2. **Daily schedule template**: typical Monday-Friday, with sign-out times, didactics, conferences.
3. **Key contacts**: 3-5 people the resident should know (lab director, attending of the week, fellow, charge tech, scheduler). Name, role, how to reach.
4. **Reading for day 1**: 1-3 items, with rationale. Don't pad.
5. **What success looks like by end of week 1**: 3-4 observable indicators that the resident is on track.
6. **What to do if things aren't clear**: explicit escalation path.

Tone: welcoming, concrete, no jargon you wouldn't explain.

**Important — refinement:** If you can't fit something on one page, cut it. The one-page constraint is the value — it forces ruthless prioritization of what a day-1 resident actually needs.
```

## Expected output

A one-page document, printable and skimmable, that removes day-1 confusion.

## Common failure modes

- Tries to fit too much, defeats the one-page constraint.
- 'Key contacts' don't include the people who actually answer questions on day 1.
- Reading list is aspirational rather than essential.

## Required human verification

- Pilot with a recent rotator: would they have wanted this document?
- Verify contact info is current.
- Update each rotation block (don't recycle stale info).

## Best model and why

**Claude Sonnet 4.6** — One-page format with ruthless prioritization — Sonnet handles the constraint well. Haiku can work but tends to omit useful detail.
