---
title: Grand rounds speaker prep
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: grand-rounds, speaker-prep, audience-reading
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## The prompt

```
You are helping me prep for grand rounds. Read the host institution's culture if I describe it; ask if you don't know it.

## What I'm preparing

- **Topic:** [be specific]
- **Institution:** [name + general culture if I know it]
- **Date:** [when]
- **Duration:** [talk + Q&A]
- **Audience composition:** [mix]

## What to produce

1. **Audience profile** — who's likely there, what they know, what they want
2. **Talk structure** — opening hook approach + 3-4 content beats + synthesis (with timing)
3. **Recommended visuals** — 2-3 specific visuals that will land
4. **5 Q&A questions to prep for**:
   - 2 from a content expert
   - 2 from a generalist
   - 1 from a trainee
5. **What NOT to do** — 2-3 framings that will misfire at this institution. ASK ME about institutional culture before drafting this if you don't know.
6. **The "walking away" line** — one sentence the audience will remember 24 hours later

## Hard rules

- Ask about institutional culture before guessing
- Specific visuals, not generic
- Walking-away line testable in 24 hours

## What I will NOT accept

- Generic audience profile
- "What not to do" guessed at without knowing the institution
- Walking-away line that's too long or vague
```

## Required human verification

- Validate audience profile with someone at the host institution.
- Walking-away line should be repeatable from memory tomorrow.

## Best model and why

**Claude Opus 4.7** — audience reading and anticipating sophisticated questions requires depth.
