---
title: Resident feedback note drafting
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: feedback, narrative, evidence-based
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Converts your bullet observations from a rotation into a polished feedback note that residents will actually read and remember. Strict discipline: every claim in the note must trace to an observation you provided. No extrapolation, no padding, no manufactured praise.

## When to use it

End of rotation, when you've taken notes during the block and want to convert them into a readable feedback document. Best within a week of the rotation end while details are fresh.

**Not for:** CCC narratives (use [CCC narrative comment drafting](library.html#/library/pillar-2-teaching/prompts/ccc-narrative-comment) — different audience), high-stakes professionalism conversations (use [Difficult feedback conversation prep](library.html#/library/pillar-2-teaching/prompts/difficult-feedback-conversation-prep)), or feedback you don't actually have observations for.

## The prompt

```
You are drafting a feedback note for a resident. Every claim in the note must trace to an observation I gave you. Do not extrapolate, manufacture praise, or pad to reach a length.

## What I'm providing

- **Resident initial and PGY:** [e.g., "Resident DA, PGY-2"]
- **Rotation and duration:** [e.g., "blood bank, 4 weeks"]
- **Service context:** [the rotation environment, my role, frequency of interaction]
- **My observations (bullets):**
  [paste — mix of strengths, growth areas, specific incidents]
- **My intended outcome for this feedback:** [what I want the resident to do differently or keep doing]

## Note structure (5 sections, ~250-350 words total)

1. **Opening orientation (1-2 sentences)** — the rotation, level of trust the resident operates at, the overall arc
2. **Strengths section (2-4 specific strengths)** — each tied to a behavior or incident I noted. Avoid generic praise like "great communicator."
3. **Growth section (2-3 specific growth areas)** — each tied to a behavior or incident. Use actionable language — what would "better" look like specifically?
4. **One behavioral commitment** — framed as a question the resident should ask themselves at each sign-out (e.g., "Before I commit to this interpretation, what would I want to see that I haven't?")
5. **Closing (1 sentence)** — forward-looking, not a hollow compliment

## Tone

- Warm but honest
- Specific over generic
- Behavioral over personality-based
- Direct without being harsh

## Hard rules

- **Every claim must trace to an observation I provided.** If you find yourself padding to reach the target length, leave it short.
- **Do NOT add praise or critique I didn't write.** Watch for this — it dilutes credibility.
- **Growth areas framed as behaviors, not personality traits.** "Be more confident" is bad; "When you commit to an interpretation at sign-out, lead with the diagnosis rather than the differential" is good.
- **The behavioral commitment is non-optional.** Without it, the feedback is reflective, not actionable.

## What I will NOT accept

- Claims I can't trace to my observations
- Generic praise or growth areas
- Personality-trait framing
- A hollow closing ("great work, keep it up!")
```

## Expected output

A 5-section feedback note (~250-350 words) tightly grounded in your observations.

## Common failure modes

- **Manufactured observations.** Push back: "I didn't write that. Where did you get it?"
- **Personality-trait framing.** Push back: "What's the behavior?"
- **Hollow closing.** Push back.

## Required human verification

- Re-read against your original observations. Anything in the note that's not in your bullets is the model speaking, not you. Delete or rewrite.
- Sanity-check the tone with how you'd actually talk to this resident.

## Best model and why

**Claude Opus 4.7** — voice and nuance matter here. Opus produces feedback that reads more like a thoughtful attending; Sonnet tends toward template phrasing.
