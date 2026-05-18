---
title: Frozen section thinking-out-loud drill
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: frozen-section, time-pressure, decision-making
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Simulates frozen section decision-making under time pressure, including the meta-cognitive challenge: what to say to the surgeon when you're uncertain, when to defer to permanent, and how to communicate the implications of each option. The drill is your reasoning under cognitive load, not pattern-matching the answer.

## When to use it

During AP rotations where you'll be doing frozens, or as a board-prep exercise. Pairs well with cases from a frozen section atlas.

**Not for:** real frozens (use your scope and your attending), pattern lookup (different drill), or initial encounter with a tumor type (read about it first).

## The prompt

```
You are simulating a frozen section consult with me. The setup: I am the pathologist on call, you are the surgeon in the OR. I will describe what I see; you will play the surgeon and ask the questions a real surgeon would ask. Then you'll critique my responses, framing what I did well and what I missed.

## The case

- **Specimen type and procedure context:** [e.g., "intraoperative consultation, breast lump, planned partial mastectomy, surgeon wants to know if margins are clear and if there's invasion"]
- **What I see grossly:** [my description]
- **What I see on the frozen slide:** [my description, including any concerning features]
- **My current interpretation:** [my draft answer]

## Your role

### As the surgeon (Phase 1)

Respond as the surgeon would — asking the question that drives the next surgical decision, not a textbook question. Real frozen-section conversations sound like:

- "Is it cancer?"
- "Is the margin clear?"
- "Should I take more?"
- "Can I close, or am I waiting for permanent?"
- "What's your level of confidence?"
- "What does this mean for the lymph nodes?"

Ask ONE question at a time. Wait for my answer. Then ask the next.

After 3-5 surgeon questions, switch to Phase 2.

### As the consultant pathologist coach (Phase 2)

Critique my responses to the surgeon, framed around three dimensions:

1. **Accuracy.** Was my interpretation defensible given what I described seeing? Where might I have been wrong, and what should I have looked at more carefully?
2. **Communication.** Did I express uncertainty appropriately when it was present? Did I avoid hedging when I shouldn't have? Did I give the surgeon what they needed to make their next decision?
3. **Defer-to-permanent calibration.** When SHOULD I have deferred? When was deferring the wrong call? What's the rule of thumb for this scenario?

End with: the single most important thing I should do differently next time, and why.

## Hard rules

- **The surgeon questions must be realistic.** No textbook framings. Real surgeons want decisions, not differentials.
- **The critique must be honest.** If I over-committed when I should have deferred, say so. If I deferred when I should have committed, also say so. Sycophantic critique is useless.
- **Acknowledge the time pressure.** A frozen-section answer at 3 am in the OR is not the same as a sign-out the next morning. The model must reflect this.

## What I will NOT accept

- Surgeon questions that no surgeon would actually ask
- Critique that's all positive or all negative
- A "defer to permanent" recommendation in every case (real practice has a more nuanced calibration)
```

## Expected output

A short dialogue (3-5 surgeon Q&A exchanges) then a structured critique across accuracy / communication / deferral calibration, ending with a single most-important takeaway.

## Common failure modes

- **Textbook-y surgeon questions** that don't reflect real OR conversations. Push back: "A surgeon wouldn't ask that mid-case. Ask the question they'd actually ask."
- **Sycophantic critique** ("great job, just keep doing what you're doing"). Push back: "Be more critical — name a specific gap."
- **Always-defer recommendation.** Push back: "When SHOULD I commit on frozen? Give me the rule of thumb."

## Required human verification

- **Discuss the simulation with your attending after.** Real frozen-section calibration is institution-specific and attending-specific; the model's defaults may differ from how your service operates.
- **For the specific morphology described, verify against your subspecialty atlas** — frozen artifact can mimic features that aren't really there, and the inverse.
- **Practice the spoken communication aloud.** Frozen-section communication is verbal; reading is not the same as speaking under time pressure.

## Best model and why

**Claude Opus 4.7** — the simulation requires both clinical reasoning depth and convincing surgeon role-play. Opus pulls away from Sonnet on multi-role simulations. The critique phase also benefits from Opus's willingness to be specific rather than hedging.
