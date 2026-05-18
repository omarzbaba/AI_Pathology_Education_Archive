---
title: Rotation orientation one-pager
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: orientation, onepager, day-one
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates a one-page rotation orientation that removes day-1 confusion. Ruthlessly prioritized — the one-page constraint is the value, forcing cuts to anything that's not essential.

## When to use it

Send to incoming residents the week before they start a rotation. Update at least annually as contacts and workflows change.

## The prompt

```
You are generating a one-page rotation orientation document. The one-page constraint is the entire value — be ruthless about what gets cut.

## What I'm providing

- **Rotation name:** [name]
- **Duration:** [N weeks]
- **Audience:** [PGY level + relevant context]
- **Service environment:** [institution + service]
- **Day-1 logistics:** [arrival time, location, person to find]
- **Daily schedule shape:** [sign-out times, didactics, conferences]
- **Key contacts:** [3-5 names, roles, contact methods]
- **Required day-1 reading:** [1-3 items max with rationale]

## Sections (one page, ~400 words)

1. **Welcome + day-1 logistics** (3-4 sentences) — when, where, who to find, what to bring
2. **Daily schedule template** — typical Mon-Fri with sign-out, didactics, conferences
3. **Key contacts (3-5 people)** — name, role, how to reach (email or phone)
4. **Reading for day 1** — 1-3 items max with one-sentence rationale per item
5. **What success looks like by end of week 1** — 3-4 observable indicators
6. **What to do if things aren't clear** — explicit escalation path (who to ask, when to escalate to the PD)

## Tone

Welcoming, concrete, no jargon you wouldn't explain. Resident-friendly.

## Hard rules

- **One page maximum.** If you can't fit something, cut it.
- **Day-1 reading is 1-3 items MAX.** Aspirational reading lists go unread.
- **Key contacts include actual ways to reach them.**
- **Success indicators are observable**, not "demonstrates engagement."

## What I will NOT accept

- A two-page document called "one-pager"
- Reading list with more than 3 items
- Vague success indicators
- Missing escalation path
```

## Expected output

A one-page printable orientation document.

## Required human verification

- Pilot with a recent rotator — would they have wanted this document?
- Verify contact info is current.
- Update annually.

## Best model and why

**Claude Sonnet 4.6** — one-page format with constraint discipline.
