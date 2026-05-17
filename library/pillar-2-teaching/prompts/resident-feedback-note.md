---
title: Resident feedback note drafting
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: feedback, narrative
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Convert bullet-point observations from a rotation into a polished feedback note, preserving specificity while improving readability.

## When to use it

When you've taken notes during a rotation and need to convert them into a feedback document the resident will actually read and remember.

## The prompt

```
Convert these rotation observations into a feedback note for [resident name initial], a [PGY level] who just finished their [N]-week rotation on [service].

Observations (mix of strengths, areas for growth, specific instances):
[paste your bullet notes — specific incidents, recurring patterns, comparative observations]

Format:

1. **Opening orientation** (1-2 sentences): the rotation, the level of trust the resident operates at, the overall arc.
2. **Strengths section:** 2-4 specific strengths, each tied to a behavior or incident I noted. Avoid generic praise.
3. **Growth section:** 2-3 specific growth areas, each tied to a behavior or incident. Use language that's actionable — what would 'better' look like?
4. **One specific behavioral commitment** for the next rotation, framed as a question the resident should ask themselves at each sign-out.
5. **Closing** (1 sentence): a forward-looking statement, not a hollow compliment.

Tone: warm but honest. Specific over generic. Behavioral over personality-based.

Do NOT add observations that aren't in my notes. If something is missing, leave it out rather than padding.

**Important — refinement:** Every claim in the note must be traceable to an observation I gave you. Do not extrapolate to praise the resident didn't earn or growth areas I didn't flag. If you find yourself padding to reach the target length, leave it short.
```

## Expected output

A feedback note in five sections that reads like a real attending wrote it — specific, behavioral, actionable. The 'behavioral commitment' question is the most valuable line.

## Common failure modes

- The model adds praise or critique you didn't write. Watch for this — it dilutes credibility.
- Growth areas are framed as personality traits ('be more confident') rather than behaviors.
- The closing is hollow ('great work, keep it up!').

## Required human verification

- Re-read against your original observations. Anything in the note that's not in your notes is the model speaking, not you. Delete or rewrite.
- Sanity-check the tone with how you'd actually talk to this resident.
- Run formal feedback notes through your institution's required template format if one exists.

## Best model and why

**Claude Opus 4.7** — Voice and nuance matter here. Opus produces feedback that reads more like a thoughtful attending and less like a template, and is more disciplined about not adding observations you didn't provide.
