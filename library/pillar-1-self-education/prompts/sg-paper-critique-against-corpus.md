---
title: Source-grounded paper critique against your corpus
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: source-grounded, paper-critique, cross-source-comparison
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-18
---

## What this prompt does

Critiques a paper against the broader literature in your notebook — not against the model's general training. Surfaces where this paper agrees with, extends, or contradicts the other sources you've uploaded. Useful for journal club prep and for deciding whether to incorporate a paper into your practice.

## When to use it

Inside a journal club or topic-specific notebook that contains the primary paper plus 5-10 related sources.

## The prompt

```
You are critiquing this paper against the broader literature in the uploaded
notebook. Your job is to surface where this paper agrees with, extends,
or contradicts the other sources — based ONLY on what's in the notebook,
not your general knowledge.

## What I'm asking

- **Primary paper to critique:** [filename or title — must be in the notebook]
- **My focus:** [e.g., "Is the headline result consistent with prior trials?",
  "What's the strongest critique of the methods based on the related literature?"]

## What to produce — 5 parts

### 1. Where this paper AGREES with the broader corpus

Specific points where the primary paper aligns with conclusions in other
uploaded sources. Cite each agreement: `[primary paper claim] aligns with
[other source X, finding Y]`.

### 2. Where this paper EXTENDS the broader corpus

Novel contributions — claims or findings that go beyond what other uploaded
sources address. Be honest about whether this is genuinely new vs incremental.

### 3. Where this paper CONTRADICTS the broader corpus

Specific points where the primary paper disagrees with conclusions in other
uploaded sources. Cite both sides: `[primary paper claim X] contradicts
[other source Y conclusion Z]`. Acknowledge if you can tell from the
sources WHY they disagree (different methods, different populations,
publication date difference).

### 4. The single strongest critique from the corpus

If you had to pick ONE point from the other uploaded sources that most
challenges this paper's conclusions, what is it? Why is it the strongest?

### 5. Open questions the corpus doesn't resolve

What questions does this critique surface that no source in the notebook
can answer? These are the questions for journal club discussion.

## Source-grounding rules

- **Every comparative claim must cite both sides** (the primary paper and
  the other source).
- **If the corpus doesn't contain a relevant comparison source, say so.**
  Do not fill in from general literature you weren't shown.
- **If you're uncertain whether two sources actually disagree** (vs use
  different language for similar concepts), say so.

## What I will NOT accept

- Unsourced claims about "the literature" generally
- Vague "this paper extends our understanding" without specifics
- Synthesized contradictions that aren't actually in the sources
```

## Expected output

A 5-part critique grounded in actual cross-source comparison from your notebook, with verifiable citations on both sides of every comparison.

## Common failure modes

- **Synthetic contradictions.** The model invents disagreements that aren't actually in the sources.
- **Smoothed-over disagreements.** Push back: "Source X clearly disagrees with this paper on [Y]; address that."
- **Citation slippage.** A claim attributed to Smith 2021 isn't actually in that paper. Verify.

## Required human verification

- **Open every cited source and verify the comparison.** Both the primary paper's claim and the related source's position.
- **For journal club use, every contradiction you'll mention must be verified.** The cost of mis-citing a paper in front of colleagues is high.

## Best model and why

**Claude Opus 4.7 via Claude Projects with PDFs attached** for substantive cross-source reasoning. **NotebookLM** for tighter grounding but less reasoning depth.
