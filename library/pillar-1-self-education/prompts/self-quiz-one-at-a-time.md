---
title: Self-quiz one at a time
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: self-assessment, drilling
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Drill yourself with one question at a time, with the model adapting follow-up questions based on what you got wrong. The interaction structure matters as much as the content.

## When to use it

When you have 10-30 minutes and want to actively rehearse rather than passively read. Especially valuable the week before an exam, or during a rotation where you want to test your retention of last week's material.

## The prompt

```
I'm a [PGY level] resident studying [topic]. I want you to quiz me on this topic.

Ground rules — these are critical:

1. Ask me ONE question at a time. Wait for my answer.
2. After each answer, tell me if I'm right or wrong and explain briefly. If I was partially right, name what I missed.
3. Use my answer to calibrate the next question. If I got it cold, escalate the difficulty. If I struggled, ask a related but slightly easier question that addresses my gap.
4. After 5 questions, give me a one-paragraph synthesis of where I'm strong and where I have a gap.
5. Do NOT lecture between questions. Keep the rhythm tight.

Start with a calibration question that helps you figure out my level on this topic.
```

## Expected output

A back-and-forth conversation. Each model turn = one question + brief feedback on the prior answer (if any). At question 5, a synthesis paragraph identifying your strongest area and biggest gap.

## Common failure modes

- The model violates the one-question rule and dumps three questions at once. Push back hard: 'One at a time. Wait for my answer before the next question.'
- The model lectures between questions, undermining the drill rhythm. Push back: 'Less explanation, more questions.'
- The synthesis at the end is generic ('keep studying!') rather than specific. Ask: 'Be more specific about my gap — what should I read tonight?'

## Required human verification

- The model's feedback on whether you got it right or wrong is itself fallible. If a question's correct answer surprises you, verify against an authoritative source before incorporating it into your mental model.
- Watch for the model marking you 'partially correct' when you're actually wrong, which builds false confidence.
