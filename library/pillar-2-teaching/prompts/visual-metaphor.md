---
title: Visual metaphor brainstorming
pillar: teaching
event_type: n/a
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: lecture, metaphor
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generate visual metaphors for an abstract concept, ranked by precision vs accessibility. The point is not to pick the metaphor for you but to surface options you wouldn't have generated alone.

## When to use it

When you're explaining an abstract concept (gating in flow cytometry, antibody-antigen interactions, deconvolution) and your usual go-to metaphor isn't landing. Brainstorming fuel, not final answer.

## The prompt

```
Generate 5-7 visual metaphors for explaining [abstract concept] to [audience].

For each metaphor:

1. The metaphor in one sentence.
2. **What it captures well** — which features of the concept does this metaphor faithfully represent?
3. **Where it breaks down** — the feature of the concept the metaphor distorts or misses.
4. **Precision score** (1-5): how technically accurate is the metaphor when pushed?
5. **Accessibility score** (1-5): how immediately graspable is it for the target audience?

Rank the list by (precision × accessibility), but acknowledge the trade-off — the most accessible metaphors are often the least precise.

End with: which metaphor would you pick if I'm teaching to medical students vs. attendings, and why?

**Important — refinement:** Be honest about precision: do not inflate precision scores. A metaphor that breaks down when pushed against an expert deserves a precision of 2, not 4. The trade-off is the point.
```

## Expected output

5-7 ranked metaphors with strengths, weaknesses, and scores. Plus the differentiated recommendation for different audiences.

## Common failure modes

- All metaphors are variants of one ('it's like a key in a lock' / 'it's like a key fitting a door').
- Precision scores are inflated — every metaphor is rated 4-5 on precision.
- The 'breaks down' analysis is superficial.

## Required human verification

- Push each metaphor to its breaking point with an expert in your subspecialty. The metaphors that survive expert pushback are the ones to use; those that don't will mislead learners.
- Trust audience feedback over your own assessment — if the metaphor doesn't land in the room, the precision score doesn't matter.

## Best model and why

**Claude Opus 4.7** — Generating *diverse* metaphors (not variations of one) is a creativity task where Opus pulls away. Sonnet tends to converge on similar metaphors.
