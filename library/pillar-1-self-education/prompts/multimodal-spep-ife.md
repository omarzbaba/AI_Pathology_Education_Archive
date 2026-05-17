---
title: SPEP / IFE trace interpretation walkthrough
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: multimodal
tags: multimodal, spep, ife
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Upload a SPEP or IFE trace and have the model walk through the interpretation, with you predicting each step before the model reveals it.

## When to use it

During your first month of clinical chemistry, when you've read the chapter but haven't yet built the pattern recognition. Use published teaching traces, not institutional cases.

## The prompt

```
I'm uploading a [serum protein electrophoresis / immunofixation electrophoresis] trace. This is a published teaching case.

I want to drill my interpretation, not just see the answer. Use this protocol:

1. **Quiz me first.** Ask me what I observe in [a specific region — e.g., 'the gamma region', 'between the beta-2 and gamma regions'] before you describe it.
2. **After I answer, confirm or correct my observation.** If I'm wrong, name the specific morphologic feature I missed.
3. **Move to the next region** with another question.
4. **After we've worked through the trace**, ask me what additional testing I'd order and why.
5. **Only after I've committed** to my interpretation, give me your full interpretation and the published diagnosis.

Start with the broadest observation: what stands out about this trace compared to a normal one?

**Important — refinement:** STOP before responding: confirm the trace is from a published teaching case or public-domain source, NOT institutional patient material. If unclear, ask. Describe only features visible in the trace; do not invent peaks or fractions you can't actually see.
```

## Expected output

A back-and-forth conversation, region by region, ending with your committed interpretation and then the model's. The interaction structure (quiz first, reveal later) is the point.

## Common failure modes

- The model reveals the diagnosis prematurely. Push back: 'don't tell me yet — quiz me first.'
- The model accepts a wrong observation without correcting it. Push back: 'be honest — was my observation correct?'
- The model fabricates features that aren't visible in the trace.

## Required human verification

- **Use published teaching traces or public-domain images only.** No institutional cases, no de-identified real patient material.
- Verify the model's morphologic descriptions and final interpretation against the published answer key for the teaching case.
- See [Guardrails](library.html#/docs/guardrails).

## Best model and why

**Claude Sonnet 4.6** — Sonnet handles structured visual interpretation (graphs, gel traces) well and respects the quiz-first protocol. Gemini 2.5 Pro is comparable; pick whichever you have access to with image attachment.
