---
title: Journal club pre-read prep
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: journal-club, preparation, literature
verified_models: TODO
best_model: Claude Opus 4.7 with paper attached
last_updated: 2026-05-17
---

## What this prompt does

Generates a one-page pre-read for a journal club paper that attendees can actually use to arrive prepared. Includes background context, study summary with specific numbers, named strengths and limitations, and five discussion questions ordered from concrete to contested.

The most important guardrail: if the model doesn't have the actual paper text, it should refuse to produce the pre-read rather than fabricating content. A pre-read with invented numbers is worse than no pre-read.

## When to use it

When you're hosting journal club and want attendees to arrive prepared rather than reading the paper for the first time during the discussion. Also useful as a personal pre-read for any paper you'll be discussing.

**Not for:** generating the full presentation (different scope), as a substitute for actually reading the paper if you'll be presenting, or methods critique (use the [Paper methods critique](library.html#/library/pillar-1-self-education/prompts/paper-methods-critique) prompt for that depth).

## The prompt

```
You are creating a one-page pre-read for a journal club discussion. Quality depends entirely on whether you actually have the paper text. Honesty about that comes first.

## Honesty check — answer first

Do you have access to the full paper text (attached PDF, pasted full text, or otherwise)? Confirm explicitly. If you only have the title, abstract, or citation, STOP and tell me — do not generate a pre-read that invents numbers, methods, or quotes.

## What I'm requesting

- **Paper:** [DOI, citation, attached PDF, or pasted full text]
- **Audience:** [PGY level mix, plus faculty]
- **Discussion format:** [traditional walk-through / structured critique / debate / structured pro-con]
- **My role:** [presenter / discussant / attendee]

## Pre-read structure (one page, ~400-500 words)

### 1. Clinical or scientific context (3-4 sentences)

Why was this question worth asking? State of the field before this paper — what was open, what was contested, what was the gap.

### 2. The study in one paragraph (5-7 sentences)

Population, methods, key results with specific numbers. Neutral framing — not yet interpretive. Use the paper's own language for the design type (RCT, retrospective cohort, etc.).

### 3. What this paper is good at (1-2 specific strengths)

A specific design or analytic strength that strengthens the interpretation. Not "well-written" — something methodologic.

### 4. What this paper is not good at (1-2 specific limitations)

A specific limitation that constrains interpretation. Not "small sample size" if N=5000. Be specific about WHY the limitation matters.

### 5. Five discussion questions, ordered concrete → abstract → contested

- **Q1 (concrete, methods):** A question about a specific design choice or analytic decision. Answer should be in the paper.
- **Q2 (finding-level):** How confident should we be in the headline result given the design?
- **Q3 (generalizability):** Does this apply to our patient population? What about ours specifically would limit applicability?
- **Q4 (practice-change):** Should this change what we do? If yes, in what specific setting and for which patients?
- **Q5 (contested):** A question where reasonable people would genuinely disagree. Should provoke real debate.

### 6. Attendee preparation note (1 sentence)

What attendees should think about before arriving.

## Hard rules

- **Honesty check at the top.** If you don't have the paper, refuse.
- **Specific numbers from the paper, not vague characterizations.** "27% reduction (95% CI 18-35)" not "significant reduction".
- **The contested question must be genuinely contested,** not just dressed-up settled material.
- **Strengths and limitations must be specific** to this paper's design, not generic.
- **No PHI.**

## What I will NOT accept

- A pre-read generated from the title and abstract alone, dressed up as if the model read the paper
- Fabricated specific numbers or quotes
- Discussion questions that have obvious right answers (Q5 included)
- Generic strengths/limitations
```

## Expected output

A 6-section one-page pre-read (~400-500 words). Suitable for sending to attendees a week ahead.

## Common failure modes

- **Pre-read built from title alone.** Honesty check at top is designed to prevent this — verify the model actually has the paper.
- **Contested question that has an obvious answer.** Push back: "That's settled. Find a genuinely contested one."
- **Fabricated numbers.** Verify against the paper.

## Required human verification

- Verify all specific numbers against the paper.
- Pressure-test the contested question with a colleague — if they immediately agree with you, it's not actually contested.
- If the honesty check answer is "I only have the abstract," discard the pre-read and provide the paper text first.

## Best model and why

**Claude Opus 4.7 with PDF attached** for substantive engagement with the paper. **Gemini 2.5 Pro** if the paper is unusually long. Without the actual paper text, every model fabricates — the model choice doesn't save you.
