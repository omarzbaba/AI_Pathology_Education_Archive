---
title: Tumor board prep coaching
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: tumor-board, coaching, presentation-skills
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Coaches a resident who will present at tumor board. The model interviews them on the case, identifies where their presentation is weakest, and gives them specific drilling on the 2-3 highest-stakes questions board members will ask. This is meta-prompt — the PRESENTER uses it, not the audience.

## When to use it

When you're coaching a resident who will present at tumor board for the first time, or when a senior resident is presenting a complex case where the consequences of a poor presentation are high.

**Not for:** preparing your own tumor board presentation (you should know your own gaps), generating the case packet itself (different prompt), or replacing real practice runs with your team.

## The prompt

```
You are coaching me through preparing to present a case at tumor board. Interview me, find the weak spots in my presentation, and drill the 2-3 highest-stakes questions board members will ask.

## What I'm presenting

- **Case (de-identified):** [paste your case summary — pathology, imaging, history, current question for the board]
- **Tumor board specialty:** [GU MDTB, GI MDTB, breast MDTB, lung MDTB, etc.]
- **Anticipated attendees:** [med onc, rad onc, surgery, radiology, others]
- **The decision the board needs to make:** [the explicit question I'm bringing]
- **My role on the team:** [my level + how long I've been on this service]
- **What I'm nervous about:** [optional — but useful]

## How to coach me — 4 phases

### Phase 1: Walk-through

I'll talk you through my draft presentation. You listen. Don't interrupt unless I ask. Just take note of:
- Where my framing is weakest
- Where I'm using imprecise language
- Where the decision question is unclear or buried
- Where I'm under-prepared for likely follow-up

Ask me to walk through it first before any feedback.

### Phase 2: Targeted feedback

After my walkthrough, give me feedback in this order:
1. **The single most important fix.** What's the one change that would most improve my presentation?
2. **Second and third priorities.** Two more specific improvements, ranked by impact.
3. **What's working well.** Specific strengths, not "great job."

### Phase 3: The 2-3 highest-stakes questions

For my case, anticipate the 2-3 most likely follow-up questions from board members and walk me through how to answer each:
- The question (phrased as the actual board member would ask it)
- The 2-3 sentence response with the supporting data
- The follow-up question that would likely come next
- Any pre-prepared slide or data point I should have queued up

Cover at minimum: one question from the med onc, one from radiology or surgery (whichever is more relevant), and one from a generalist (medical director, board chair).

### Phase 4: The simulation

Now play the role of the most likely tough questioner at MY institution's board (you may need to ask me what they're like). Ask me one question. I'll respond. You'll give me feedback.

Do 2-3 rounds.

## Hard rules

- **Don't lecture me about the case.** This is about the presentation, not the medicine.
- **Be specific in feedback.** "Be more confident" is useless; "When you said 'I think this is high-grade,' say 'this is high-grade' instead" is useful.
- **The simulation is for practice, not assessment.** Push me, but don't grade me.

## What I will NOT accept

- Generic presentation tips
- Feedback that's all positive or all negative
- Anticipated questions that softball the case
- Skipping the simulation
```

## Expected output

A 4-phase coaching conversation: walkthrough → targeted feedback → 2-3 highest-stakes questions with response framing → 2-3 rounds of simulated tough questions.

## Common failure modes

- **Generic feedback** ("be clear, be confident"). Push for specific.
- **Softball anticipated questions.** Push back: "What's the question they'd ask if they wanted to challenge me?"
- **Skipping the simulation.** Make sure you actually do the practice rounds.

## Required human verification

- The model doesn't know your institution's specific board dynamics. Validate the anticipated questions with someone who attends regularly.
- Practice the simulation aloud — speaking is different from reading.
- After the actual board, write down what was asked vs what the model predicted. Use it to calibrate next time.

## Best model and why

**Claude Opus 4.7** — anticipating sophisticated medical questions and providing substantive coaching requires depth. Opus is better at playing the role of a tough questioner than Sonnet.
