---
title: Letter of recommendation starting draft
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: lor, narrative
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate a starting draft for a letter of recommendation. **Heavy editing required** — the model produces structurally plausible but generic prose; the specific anecdotes and judgments must come from you.

## When to use it

When you've agreed to write a LOR and need to break the blank-page paralysis. Treat the output as scaffolding, not as a letter you'd sign.

## The prompt

```
Draft a letter of recommendation for [applicant name and degree(s)] applying to [program type / specific program] starting in [year].

Context I'll provide:
- My relationship to the applicant: [how long you've known them, in what capacity, frequency of interaction]
- My role: [your title, why your voice carries weight for this application]
- Their strengths I want to highlight: [specific traits + the specific anecdotes that demonstrate each]
- What I want the reader to know that's not on the CV: [the differentiator]
- Their areas for growth I want to acknowledge honestly: [optional but recommended for credibility]

Letter structure:

1. Opening: relationship, capacity, and a one-sentence headline of who this person is.
2. Body paragraph(s) — one per strength, each with the specific anecdote that demonstrates it. Replace any placeholders with specifics; do not leave generic.
3. A paragraph that says what distinguishes this applicant from others at their level.
4. Closing: explicit recommendation with appropriate strength, and an offer to discuss further.

**Critical:** the letter MUST be heavily edited by me before sending. The model will produce structurally plausible prose that reads as generic to experienced LOR readers (program directors read hundreds and recognize template language). My job is to inject specificity, my actual voice, and the anecdotes only I would know.
```

## Expected output

A draft letter with placeholders where you'll need to insert specifics. The draft is the skeleton; you supply the flesh.

## Common failure modes

- The model produces generic praise that sounds like every other LOR.
- The 'distinguishing' paragraph is platitudinous.
- Quoted anecdotes get distorted in translation.

## Required human verification

- **Read every sentence and ask: would I write this exact sentence?** Rewrite the ones where the answer is no — that's most of them.
- Verify the applicant's accomplishments, dates, and dosing of praise.
- LOR readers detect AI-template language. The differentiator is your specific voice and your specific knowledge — that has to come from you, not the model.
- See [Guardrails](library.html#/docs/guardrails) on the structural plausibility failure mode.
