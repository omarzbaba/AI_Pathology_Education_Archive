---
title: Question bank gap analysis
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: board-prep, gap-analysis, metacognition
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Takes a list of qbank questions you've missed and identifies the underlying *concept gaps* — not the surface-level facts you didn't know, but the recurring patterns of misunderstanding that explain why those specific questions fooled you. Then ranks the gaps by impact and produces a targeted review plan for the top gap.

The key discipline this prompt enforces: distinguishing a *concept gap* (you don't understand the underlying mechanism) from a *recall failure* (you knew the fact but couldn't retrieve it under time pressure). The interventions for each are different.

## When to use it

After a substantial block of qbank questions (50+) where you've underperformed, especially if you can't immediately see why. Also useful as a periodic check during board prep — gap analysis every 100 questions is more useful than gap analysis at the end.

**Not for:** small samples (5-10 missed questions is noise), questions you missed for non-knowledge reasons (timing, misreading), or as a substitute for talking through specific cases with an attending.

## The prompt

```
You are doing a gap analysis on questions I missed. Your job is to find the UNDERLYING patterns, not just enumerate the facts I didn't know. Distinguish concept gaps from recall failures — the interventions are different.

## What I'm pasting

For each missed question:
`topic — what the question tested — why I missed it (my honest assessment)`

Example:
- `Plasma cell neoplasms — distinguishing MGUS from smoldering MM — I knew the criteria but defaulted to the wrong threshold`
- `Hemostasis — interpreting mixing studies — I didn't understand what the mixing study actually shows mechanistically`

[paste your list, 10-50 entries]

## What to produce

### 1. Cluster the misses into 2-5 concept clusters

A cluster is a recurring *kind* of misunderstanding, not just a topic area. Examples of good cluster names:
- "Confusing inherited vs acquired in coagulation disorders"
- "Cutoff thresholds in plasma cell neoplasms"
- "Mechanism-to-finding inferences in lab medicine"

For each cluster:
- List the missed questions that belong in it
- State the underlying gap in 1-2 sentences
- **Mark whether this cluster is a concept gap or a recall failure** (or mixed)

### 2. Rank the clusters by impact

Which gap, if filled, would resolve the most other questions? Justify the ranking — don't just list.

### 3. Targeted review plan for the TOP cluster

For the highest-priority gap:
- **Specific resources:** which chapter, paper, or video addresses this cluster directly
- **Targeted qbank topic to drill next:** name the qbank subtopic
- **Estimated hours needed:** be honest, not aspirational
- **A check question:** how will I know I've actually closed this gap?

### 4. The "don't worry about it" list

Anything in my misses that's low-yield for the exam and not worth fixing in the time I have. Be specific — name the questions.

### 5. Meta-pattern

After the cluster analysis: is there a single META-pattern across all my misses? (e.g., "I'm faster than I should be on multi-step questions and miss the second step", "I anchor on the first plausible answer", "I'm strong on facts but weak on integration")

## Hard rules

- **Distinguish concept gaps from recall failures explicitly** — different interventions.
- **Cluster names must describe the gap, not just the topic.**
- **The "don't worry about it" list cannot be empty.** Real qbank data always includes some questions not worth re-studying.
- **The targeted review plan must be specific.** "Read more" is not a plan; "Read Henry chapter 38, then drill the qbank 'PCN cutoffs' subtopic for 90 min" is.

## What I will NOT accept

- Topic-name clusters dressed up as concept clusters
- All clusters labeled "high priority"
- Empty "don't worry about it" list
- Aspirational hours that ignore my actual time budget
```

## Expected output

Clusters with concept-vs-recall labels, ranked by impact, with a specific review plan for the top cluster, an honest "don't worry about it" list, and a meta-pattern observation.

## Common failure modes

- **Model treats every miss as equally important.** Push back: "Rank by impact."
- **Cluster names are just topic names.** Push back: "Name the gap, not the topic."
- **Review plan is vague.** Push back for specific resources and hours.
- **No "don't worry about it" list.** Push back: "Be honest — what's low-yield?"

## Required human verification

- Validate cluster boundaries — does the cluster naming match how YOU think about your gaps?
- The "don't worry about it" list should be validated against your program's emphasis and your exam's blueprint.
- Talk through the meta-pattern with a colleague — sometimes the model sees a pattern that's actually noise, or misses a real pattern.

## Best model and why

**Claude Opus 4.7** — pattern recognition across many missed questions is exactly where Opus pulls away from Sonnet. The cluster-naming discipline and the concept-vs-recall distinction reward depth. **Sonnet** works for shorter lists (≤15 questions) where the clustering is more obvious.
