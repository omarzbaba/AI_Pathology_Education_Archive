---
title: Verify your AI notebook is actually grounded
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: source-grounded, verification, grounding-drift
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Source-grounded AI tools claim to answer "only from your uploaded sources." In practice, they drift — pulling from the model's general training data when retrieval is weak, paraphrasing in ways that change meaning, citing sources that don't actually contain the claim. This guide gives you a 5-test protocol to verify grounding before trusting your notebook for high-stakes use.

## When to use it

The first time you set up a notebook. Then monthly thereafter. Also any time the notebook's response surprises you in a "this is suspiciously confident" way.

## The protocol — 5 tests

```
GROUNDING VERIFICATION PROTOCOL

Run all 5 tests at notebook setup and monthly thereafter. If any test
fails, the notebook's grounding is weak and you should not rely on it for
high-stakes use until you understand why.

## Test 1: Known-answer probe

Ask a question you KNOW the answer to from a specific source you uploaded.

Example: "Based on the uploaded sources, what is the diagnostic threshold
for [specific entity] per the [specific guideline]?"

The response should:
- Cite the actual uploaded source (NotebookLM shows citations explicitly;
  ask Claude Projects: "Which uploaded source does this come from?")
- Give the answer that's actually in the source
- Not add information from elsewhere

If it confabulates or pulls from outside the source, grounding is weak.

## Test 2: Negative probe — out-of-corpus question

Ask a question that is NOT addressed in any of your uploaded sources.

Example: "Based on the uploaded sources, what does the 2030 guideline
say about [topic]?" (assuming you uploaded only 2024 sources)

The response should:
- Acknowledge that the uploaded sources don't address this
- Refuse to answer or clearly mark its response as drawing from general
  knowledge rather than your corpus

If the model invents a 2030 guideline answer, grounding is weak. This
is the most important test.

## Test 3: Citation verification

For a response that cites a specific source, open that source and check:
- Is the claim actually in the source as described?
- Is the wording paraphrased in a way that changes meaning?
- Is the page/section reference accurate (if cited)?

If the cited claim doesn't match the source, grounding is decorative
rather than real.

## Test 4: Cross-source disagreement detection

Upload two sources that you know disagree on a specific point. Ask:
"How do the uploaded sources differ on [topic]?"

The response should:
- Identify the disagreement
- Cite each source's position accurately
- Not artificially smooth over the conflict

If it pretends the sources agree or makes up a synthetic consensus,
grounding is weak.

## Test 5: Consistency probe — same question, different framings

Ask the same substantive question two different ways, separated by other
queries.

Example:
- Q1: "What's the diagnostic criterion for X per the uploaded sources?"
- (do other questions)
- Q2: "How would I diagnose X using only the uploaded sources?"

The two answers should be substantively the same. If they materially
differ, the model is generating fresh content each time rather than
retrieving from a stable source — that's a grounding failure.

## What to do if a test fails

1. Reduce corpus size — too many sources dilutes retrieval.
2. Check source quality — low-quality PDFs (scanned, OCR errors) degrade
   retrieval.
3. Switch tools — if NotebookLM fails and you have access to Claude
   Projects (or vice versa), try the other.
4. Don't rely on the notebook for high-stakes use until you understand
   the failure mode.

## Frequency

- **At setup:** all 5 tests
- **Monthly:** Tests 1, 2, 3
- **After major corpus changes:** all 5 tests
- **Before any high-stakes use** (board prep, journal club presentation):
  Tests 1 and 3 at minimum
```

## Expected output

A clear assessment of whether your notebook is grounded enough to trust. Often the answer is "mostly, but verify citations before relying on any specific answer."

## Common failure modes

- **Trusting the notebook without verification** because it sounds confident.
- **Skipping Test 2** (negative probe) — this is the most diagnostic test and the most often skipped.
- **Treating one passing test as proof the notebook is grounded.** Run all 5.

## Required human verification

- Verification IS the use. There's no shortcut. The notebook is a thinking partner whose work you check, not a database.

## Best model and why

This is a verification protocol, not a prompt. **Use whichever tool you're verifying.** The tests work the same way across NotebookLM, Claude Projects, and ChatGPT Custom GPTs.
