---
title: Negative drill — what would change the diagnosis
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: disconfirmation, counterfactual-reasoning
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Trains the habit of *disconfirmation*: take a working diagnosis you're confident in and ask the model to enumerate the findings or test results that would force you to reconsider, ranked by **clinical likelihood** rather than exoticism. The output should surface the boring, common ways you could be wrong — not the zebra alternatives.

This counters the well-documented confirmation bias in diagnostic reasoning: once we have a working diagnosis, we look for evidence that supports it and discount evidence that doesn't.

## When to use it

When you have a working diagnosis you're confident in, especially:
- Before sign-out, when the consequences of being wrong are high
- For diagnoses you've seen rarely and want to stress-test
- During study of a topic where you've gotten over-confident
- Before a tumor board where you'll defend your diagnosis

**Not for:** real-time clinical interpretation (different stakes), academic devil's advocate exercises (this is calibrated to clinical decision-making), or when you don't actually have a working diagnosis yet.

## The prompt

```
I have a working diagnosis. Your job is to stress-test it by enumerating what would force me to reconsider. Rank by CLINICAL LIKELIHOOD — the most likely way I'm wrong is usually a common condition presenting atypically, not a rare zebra.

## The case

- **My working diagnosis:** [exact entity]
- **Clinical context (de-identified):** [age range, sex if relevant, brief presentation, key positive findings — no PHI]
- **My confidence level:** [low / moderate / high — be honest]
- **What I want stress-tested:** [optional — e.g., "I'm worried I anchored on this", "I want to make sure I'm not missing something common"]

## What to produce — 3 tiers + alternative + discriminating test

### Tier 1: Findings that would force COMPLETE RECONSIDERATION

Rule out the working diagnosis entirely. For each:
- The finding
- One sentence: why does this finding contradict the working diagnosis?
- One sentence: what does it suggest instead?

### Tier 2: Findings that would EXPAND the differential

Don't rule out, but suggest a different category of disease is also in play. For each, same structure.

### Tier 3: Findings that are INCONSISTENT BUT DON'T NECESSARILY CHANGE the diagnosis

Worth noting in the report or follow-up, may indicate complication or atypical presentation.

### The single most likely alternative diagnosis

If you're wrong, what is the SINGLE MOST LIKELY alternative — not the most interesting alternative, the most likely? Justify by saying what makes this alternative compete with the working diagnosis on this case's specific features.

### The ONE test to discriminate

If you could order one test to distinguish your working diagnosis from the most likely alternative, what is it? Justify in one sentence.

## Hard rules

- **Rank by clinical likelihood, not by exoticism.** The most likely way I'm wrong is rarely a rare zebra.
- **Don't pad with implausible alternatives** to look comprehensive.
- **The "one test to discriminate" must have meaningful discriminating power** for THIS pair of differentials. Don't suggest a test that's already negative.
- **Acknowledge if the working diagnosis is genuinely well-supported.** If the case is unambiguous, say so — don't manufacture doubt.

## What I will NOT accept

- A list of rare alternatives without a common one
- An "alternative" that's been excluded by basic workup
- A "discriminating test" with low specificity for the pair
- Pretending the case is more ambiguous than it is
```

## Expected output

3 tiers of disconfirming findings + the single most likely alternative + the one discriminating test. Length 400-600 words.

## Common failure modes

- **Exotic alternatives ranked above common ones.** Push back: "What's the COMMON way I could be wrong?"
- **Discriminating test that's not actually discriminating** for this pair.
- **Manufactured doubt** about a well-supported case. Push back if doubt feels strained.

## Required human verification

- This is a thinking exercise; the model's specific suggestions are starting points.
- If a specific test is recommended, verify it's the right test for the discrimination you actually need.
- Talk through the alternative with an attending if the case is genuinely high-stakes.

## Best model and why

**Claude Opus 4.7** — counterfactual reasoning and ranking by clinical likelihood require both medical knowledge depth and judgment about pretest probability. Sonnet tends to surface rarer alternatives first; Opus is better calibrated to common-things-common.
