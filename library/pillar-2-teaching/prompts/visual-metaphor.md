---
title: Visual metaphor brainstorming
pillar: teaching
event_type: n/a
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: teaching, metaphor, abstract-concepts
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generates 5-7 candidate visual metaphors for an abstract concept, with explicit precision-vs-accessibility tradeoffs scored for each. The point isn't to pick the metaphor for you but to surface options you wouldn't have generated alone, with honest acknowledgment of where each one breaks down.

## When to use it

When you're explaining an abstract concept (clonality, gating in flow cytometry, antibody-antigen interactions, deconvolution) and your usual go-to metaphor isn't landing. Brainstorming fuel, not the final answer.

**Not for:** lookups (just look up the standard metaphor), highly technical audiences where metaphors do more harm than good, or contexts where precision-over-accessibility is required.

## The prompt

```
You are generating visual metaphor options for me. Be honest about each metaphor's precision tradeoffs. A metaphor that sounds clever but distorts the concept is worse than no metaphor.

## What I'm explaining

- **Abstract concept:** [be specific — e.g., "clonality in lymphoid populations" not just "clonality"]
- **Target audience:** [medical students / residents / attendings / patients — calibrates the precision-accessibility tradeoff]
- **What I want them to understand specifically:** [the key insight the metaphor should land]
- **Metaphors I've already tried:** [optional — so you don't repeat them]

## Produce 5-7 candidate metaphors

For each:

1. **The metaphor** (1 sentence)
2. **What it captures well** — which features of the concept does this metaphor faithfully represent?
3. **Where it breaks down** — the feature of the concept that this metaphor distorts or misses. Be honest here; this is the most important field.
4. **Precision score (1-5):** how technically accurate is the metaphor when pushed?
5. **Accessibility score (1-5):** how immediately graspable is it for the target audience?

## Ranking

Rank by (precision × accessibility). Acknowledge the trade-off: the most accessible metaphors are often the least precise.

## Recommendation by audience

End with:
- "If you're teaching medical students, use [metaphor X] because [reason]"
- "If you're teaching attendings, use [metaphor Y] because [reason]"

## Hard rules

- **Be honest about precision.** Inflated precision scores defeat the entire prompt.
- **The "where it breaks down" field is the most important.** If a metaphor breaks at a critical point and you don't say so, you've mis-served the teacher.
- **Diverse metaphors, not variants of one.** "Like a key in a lock" and "like a key fitting a door" are the same metaphor.
- **Acknowledge if a metaphor is technically inaccurate.** A precision score of 2 means "breaks down when an expert pushes" — that's important to know.

## What I will NOT accept

- All metaphors are variants of one
- Inflated precision scores (everything 4-5)
- Superficial "breaks down" analysis
- No audience-differentiated recommendation
```

## Expected output

5-7 ranked metaphors with strengths, weaknesses, scores. Plus the audience-differentiated recommendation.

## Common failure modes

- **Convergent metaphors** (all variations on one theme). Push back: "Generate genuinely different metaphors."
- **Score inflation.** Push back: "Be honest — what's the precision score if an expert pushes?"
- **Superficial 'breaks down' analysis.** Push back: "Where specifically does it fail?"

## Required human verification

- Push each metaphor to its breaking point with a colleague in your subspecialty. Metaphors that survive expert pushback are the ones to use.
- Trust audience feedback over your own assessment — if the metaphor doesn't land, the precision score doesn't matter.

## Best model and why

**Claude Opus 4.7** — generating *diverse* metaphors (not variations of one) is a creativity task where Opus pulls away. Sonnet tends to converge.
