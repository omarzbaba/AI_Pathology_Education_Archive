---
title: Source-grounded concept explanation
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: <2min
visual: text-only
tags: source-grounded, concept, citation-required
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

The source-grounded version of [Concept explanation at level](library.html#/library/pillar-1-self-education/prompts/concept-explanation-at-level). Anchors every substantive claim to a specific uploaded source — not just "this is how it works" but "as described in [source X]". Designed for use in NotebookLM or Claude Projects with curated sources.

## When to use it

Inside a board prep, sign-out, or journal club notebook when you want an explanation anchored to YOUR specific source material, not the model's general knowledge.

## The prompt (paste into your notebook chat after sources are uploaded)

```
You are my study partner working ONLY from the sources I've uploaded to this
notebook. Do not draw from your general knowledge. If something is not in the
uploaded sources, say so explicitly rather than inventing.

## My context

- **PGY level:** [e.g., PGY-2]
- **Why I'm asking:** [e.g., "preparing for tomorrow's bone marrow sign-out"]
- **Target concept:** [the specific thing you're trying to understand]

## Explain the target concept in three layers, ALL grounded in uploaded sources

1. **First-year medical student version (1 sentence).** Plain language.
2. **My-level version (1 paragraph).** Mechanistic explanation at my level.
3. **The "thought hard about this" layer (1 paragraph).** Nuance that
   distinguishes someone who has internalized the concept from someone who
   has memorized.

## Source-grounding rules — non-negotiable

- **Every substantive claim must cite an uploaded source.** Format:
  `[Source filename or title, section if applicable]` inline.
- **If a claim is in multiple sources, cite the strongest one** (most current,
  most authoritative for this topic).
- **If a claim is NOT in any uploaded source, mark it `[NOT IN SOURCES]`** —
  do not fill in from general knowledge.
- **If sources disagree on a point, acknowledge the disagreement** with
  both citations.

## After your explanation

Ask me ONE application question that tests the most likely misunderstanding
for my level. Wait for my answer. If I'm wrong, name the specific gap with
a citation to the source that addresses it before re-explaining.

## What I will NOT accept

- Claims without source citations
- Claims that fill in gaps with general knowledge
- Citations to sources that don't actually contain the claim (I will verify)
- "In general..." statements that bypass the source-grounding rule
```

## Expected output

A 3-layer explanation where every substantive claim is followed by an inline source citation, with `[NOT IN SOURCES]` marks where the uploaded corpus doesn't address something.

## Common failure modes

- **Citations that don't match the source content.** The model paraphrases and confabulates citations. Verify.
- **General knowledge slipping in** without `[NOT IN SOURCES]` flag. The hardest failure mode to catch because the content sounds right.
- **Smoothing over source disagreements.** Push back if you know two sources disagree.

## Required human verification

- **Open every cited source and verify the claim is there.** Source-grounded does not mean truth-grounded — it means the model claims to be drawing from your sources, and you have to verify.
- For high-stakes use (e.g., before a board exam), spot-check at least 30% of citations.

## Best model and why

**Claude Sonnet 4.6 via Claude Projects** or **NotebookLM**. Both handle source citation well. NotebookLM is more reliable about staying in-corpus; Claude Projects is more flexible if you want to switch to general knowledge mid-conversation when needed.
