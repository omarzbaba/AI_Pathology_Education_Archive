---
title: Diagnostic algorithm walkthrough
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: algorithm, diagnostic-workup
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Walk through a published diagnostic algorithm step by step, with the model explaining each decision point and the consequences of choosing each branch.

## When to use it

When you're encountering a clinical algorithm for the first time, or when you've used one mechanically without really understanding why each branch exists. Good for the night before a sign-out where you know an algorithm will come up.

## The prompt

```
Walk me through the [name of algorithm — e.g., 'BSH guideline for warfarin reversal', 'ISTH overt DIC scoring', '2022 ELN AML response criteria'] step by step.

For each decision point in the algorithm:

1. State the question or test being asked at this node.
2. Explain *why* this question is being asked here — what does the answer rule in or rule out?
3. Walk through what happens if the answer is yes/positive and what happens if it's no/negative.
4. Name one common pitfall at this decision point — a way residents typically mis-apply this step.

After walking through the full algorithm, end with: the single decision point where errors are most clinically consequential, and how to avoid those errors.

Be specific to the published version of the algorithm; do not generalize to 'similar' protocols.

**Important — refinement:** State which version of the algorithm you're walking through (year, society, edition). If the algorithm has been substantially revised in the last 5 years, note both the version you're describing and what changed.
```

## Expected output

A linear walk-through, one node at a time, with rationale and pitfalls at each. A final synthesis identifying the most consequential decision point. Length: ~400-700 words for a typical 5-7 step algorithm.

## Common failure modes

- The model conflates two similar algorithms (e.g., ISTH overt vs non-overt DIC criteria) without flagging which it's using.
- The 'common pitfall' is generic ('don't forget to check the value') rather than specific.
- The model substitutes its own simplified logic for the actual published algorithm.

## Required human verification

- **Critical:** verify the algorithm against the actual published source (society guideline, original paper, institutional protocol). The model frequently mis-remembers cutoffs, the order of decision nodes, or which version of an algorithm it's describing.
- If the algorithm has multiple versions (e.g., updated in 2020 and 2024), confirm which version the model is walking through.

## Best model and why

**Claude Opus 4.7** — Multi-step algorithm walkthroughs with specific guideline versions reward Opus's depth. Sonnet works but is more likely to conflate similar protocols.
