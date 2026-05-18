---
title: Cross-source comparison drill
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: source-grounded, comparison, discrepancy-detection
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-18
---

## What this prompt does

Asks the notebook to compare how multiple uploaded sources address the same topic — surfacing discrepancies, definitional differences, and version drift between editions. Especially valuable when your corpus spans multiple guidelines or editions.

## When to use it

When studying a topic where you suspect (or know) the sources you've uploaded don't agree — different WHO editions, different society guidelines, different country conventions, foundational textbook vs current review.

## The prompt

```
You are surfacing discrepancies between the uploaded sources on a specific
topic. Your job is to identify where the sources disagree, not to synthesize
a consensus — disagreement IS the finding.

## What I'm asking about

- **Topic:** [be specific — e.g., "diagnostic criteria for MGUS"]
- **Which sources to compare:** [optional — name specific filenames if you
  want a focused comparison; otherwise compare across the full corpus]

## What to produce — 4 sections

### 1. Side-by-side comparison

| Aspect | Source A | Source B | Source C |
|---|---|---|---|

Rows: the specific aspects where the sources differ (definitions, cutoffs,
recommendations, terminology).

### 2. Categorize each discrepancy

For each row, label it:
- **Substantive disagreement** — sources genuinely contradict
- **Version drift** — sources agree but use different editions/years
- **Definitional difference** — sources use different terms for similar
  concepts
- **Scope difference** — sources address slightly different populations
  or use cases

### 3. The most consequential discrepancy

Which discrepancy would most change practice or interpretation if you
chose the wrong source? Why?

### 4. Recommended source for clinical use

If a learner had to pick ONE source from the uploaded corpus to use
clinically right now, which would you recommend and why? Acknowledge
tradeoffs.

## Source-grounding rules

- **Cite specific source passages** for each comparison row.
- **If you're uncertain whether two sources actually disagree** (vs
  using different language for similar concepts), say so.
- **If one source addresses a row and others don't,** mark the empty
  cells as "[not addressed]" rather than inventing a position.
- **For 'recommended source for clinical use,' acknowledge the limits
  of your information.** You're recommending based on what's in the
  notebook, not based on real-world institutional practice.

## What I will NOT accept

- A synthesized "consensus" that smooths over real disagreement
- Claims of agreement that aren't actually verified
- Recommendations beyond what the sources support
```

## Expected output

A 4-section comparison: side-by-side table, categorized discrepancies, most consequential one named, recommended source with tradeoffs.

## Common failure modes

- **Synthetic consensus.** Push back: "Source X says different. Don't smooth that over."
- **Confabulated positions** for sources that don't actually address a row.
- **Recommendation that ignores institutional context.** Your institution may use a different source for reasons you didn't share with the notebook.

## Required human verification

- **Verify each comparison row against both sources.** Cross-source comparison is where the model is most likely to invent.
- **For clinical decisions, check with the attending which source your service uses.**

## Best model and why

**Claude Opus 4.7 via Claude Projects** — substantive comparison across multiple sources rewards depth. **NotebookLM** if you want stricter citation linking but expect less synthesis.
