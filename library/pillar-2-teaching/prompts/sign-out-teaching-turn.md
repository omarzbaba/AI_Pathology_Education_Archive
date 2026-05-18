---
title: Sign-out teaching turn
pillar: teaching
event_type: n/a
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: teaching, sign-out, capture-the-moment
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Converts a sign-out moment — a case that just came up, a finding that's worth pausing on, a question a resident asked — into a structured 3-5 minute teaching point you can deliver in the flow of the day. The model gives you the framing, the key question, the supporting points, and the wrap-up — calibrated to the seconds you have, not the hour you don't.

This captures what experienced attendings do instinctively but residents don't yet know how to do for themselves.

## When to use it

In the moment, at the scope or at sign-out, when you want to take 3-5 minutes to make a teaching point rather than just signing out the case. Also useful for senior residents who are being trained to teach in sign-out (resident-as-teacher).

**Not for:** designing formal teaching sessions (different scope), long-form explanations (use the concept explanation prompt instead), or replacing the diagnostic work of sign-out.

## The prompt

```
You are helping me turn a sign-out moment into a quick teaching point. Speed matters — I have 3-5 minutes inserted into a busy sign-out, not an hour to prepare a lecture.

## The moment

- **The case or finding I'm at:** [brief — e.g., "atypical mitosis in a parathyroid adenoma, on a resident's sign-out tray"]
- **The resident's level:** [PGY level + subspecialty rotation]
- **The question I want to teach to:** [the specific point this moment surfaces — e.g., "when does an atypical mitosis change the diagnosis vs when is it incidental?"]
- **Time I have:** [3 min / 5 min — be honest]

## What to produce — in this exact structure

### 1. The hook (1 sentence)

The opening line that makes the resident pause and pay attention. Not "let me teach you something" — the specific framing that turns this case into a question worth pursuing.

### 2. The question (1 sentence)

The exact question you'll ask the resident. They should be able to answer in 30-60 seconds.

### 3. The teaching points (2-3 bullets, MAX)

The substantive content. Each bullet:
- A specific point that follows from the question
- Why it matters clinically
- Tied to what you both can see in this case

### 4. The closing pivot (1 sentence)

How you wrap up and return to sign-out — making the teaching feel like a 30-second beat rather than an interruption.

### 5. The follow-up call-back (1 sentence)

A specific question you'll ask the same resident next week to check whether the teaching stuck.

## Hard rules

- **Calibrated to the time available.** A 3-minute teach is structured differently than a 5-minute teach.
- **Specific to THIS case.** Not generic teaching points that could apply to any version of the case.
- **The opening must hook the resident in.** "I want to make a teaching point" is not a hook.
- **The closing must return to sign-out** — don't leave the resident in teaching mode.
- **The follow-up call-back is non-negotiable.** Teaching that's not called back is teaching that's forgotten.

## What I will NOT accept

- A 5-bullet list when 3 is enough
- A generic opening
- Teaching points untethered from what's on the scope
- No follow-up call-back
```

## Expected output

Five lines: hook, question, 2-3 teaching points, closing pivot, follow-up call-back. Total content fits on a sticky note. Total speaking time matches what you said you had.

## Common failure modes

- **Too long.** A 5-minute teaching point becomes a 15-minute lecture. Push back: "Cut it. I have 3 minutes."
- **Generic hook.** Push back: "Make it specific to this case."
- **No follow-up call-back.** Push back: "What do I ask next week to check?"

## Required human verification

- Time yourself once on a real sign-out. The model's "3 minutes" may be optimistic for your speaking pace.
- After the teach, observe whether the resident actually picks up the concept. If they don't, the framing was wrong — adjust for next time.
- The follow-up call-back only works if you actually do it. Schedule a reminder.

## Best model and why

**Claude Sonnet 4.6** — fast, structured outputs at the right granularity. Opus would over-elaborate; Haiku might be too terse.
