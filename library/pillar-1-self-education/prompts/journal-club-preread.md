---
title: Journal club pre-read prep
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: journal-club, preparation
verified_models: TODO
best_model: Claude Opus 4.7 with paper attached
last_updated: 2026-05-17
---

## What this prompt does

Generate a one-page pre-read for a journal club paper covering background, key results, and 5 discussion questions. Designed to be sent to attendees the day before.

## When to use it

When you're hosting journal club and want attendees to arrive prepared rather than reading the paper for the first time during the discussion.

## The prompt

```
Create a one-page pre-read for a journal club discussion of this paper. Target audience: [PGY level] pathology residents and faculty.

Structure:

1. **The clinical or scientific context** (3-4 sentences): why this question was worth asking, the state of the field before this paper.
2. **The study in one paragraph** (5-7 sentences): population, methods, key results with numbers. No interpretation yet.
3. **What this paper is good at**: 1-2 specific strengths of the design or analysis.
4. **What this paper is not good at**: 1-2 specific limitations that constrain interpretation.
5. **Five discussion questions**, ordered from concrete (methods, numbers) → abstract (implications, what would change practice). The fifth question should be one where reasonable people disagree.

Keep it to one page. Use specific numbers from the paper, not vague characterizations.

Paper: [paste DOI, citation, or full text]

**Important — refinement:** If you don't have the full paper text, say so and refuse to fabricate specific results, sample sizes, p-values, or quotes. A pre-read with invented numbers is worse than no pre-read.
```

## Expected output

A one-page document (~400-500 words) with the five sections above. The five discussion questions should escalate in abstractness and end with a contested one.

## Common failure modes

- The model fabricates specific numbers or quotes. If the model doesn't have the paper, it will sometimes guess.
- Discussion questions are leading ('don't you think...?') rather than open.
- The strengths and limitations are generic.

## Required human verification

- Verify all specific numbers (sample sizes, p-values, effect sizes) against the paper.
- Check that the discussion questions are actually answerable from the paper or from background knowledge the attendees should have.
- If the model couldn't access the paper, the pre-read is partly fabricated — discard and try with the paper text pasted in.

## Best model and why

**Claude Opus 4.7 with paper attached** — Pre-read quality depends on actually reading the paper. Use Opus 4.7 with the PDF attached, or Gemini 2.5 Pro for very long papers. Without the paper text, every model fabricates; with it, Opus produces the most defensible pre-read.
