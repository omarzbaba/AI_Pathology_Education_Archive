---
title: Microscopy teaching session design
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: teaching, microscopy, image-based, session-design
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Designs a microscopy-anchored teaching session built around 6-10 images rather than slides of text. Generates per-image talking points, discussion questions, and the teaching arc that holds the images together — not just a parade of cases.

The key discipline this prompt enforces: the SESSION has a teaching argument, and each image is selected to advance that argument. Image-based teaching is not "here are some cases" — it's a structured progression.

## When to use it

When you've been asked to give an unknown-cases conference, run a multi-headed microscopy session, or build a self-paced image-based learning module. Especially useful when you have an image collection and need to organize it into teaching.

**Not for:** designing a lecture with slides of text (use [Slide outline for a 1-hour lecture](library.html#/library/pillar-2-teaching/prompts/slide-outline-1hr)), generating images (different problem), or teaching that doesn't have microscopy at the center.

## The prompt

```
You are designing an image-anchored microscopy teaching session. The session must have a teaching argument — a thread that connects the images. Don't give me a parade of cases.

## What I'm building

- **Session topic:** [be specific — e.g., "subtypes of follicular lymphoma and their mimics", not just "lymphoma"]
- **Audience:** [PGY level + subspecialty rotation context]
- **Session duration:** [in minutes]
- **Format:** [multi-headed scope / unknown slide quiz / projected images / web-based teaching set]
- **Image collection I have available:** [describe — e.g., "12 cases including 3 FLG1-2, 2 FLG3A, 2 follicular hyperplasia, 1 marginal zone, 4 other lymphomas"]
- **What learners should walk away with:** [the one thing they should be able to DO after — be specific]

## What to produce

### 1. The teaching argument (1 sentence)

What is the THESIS of this session? Not the topic — the argument. Example: "By the end of this session, residents will be able to distinguish FL from its mimics by attending to architectural patterns at low power, not just immunoprofile."

### 2. Image sequence (6-10 images)

For each image:
- **Position in the session** (with timing)
- **What it shows** (one sentence)
- **Why it's in this position** — how does it advance the teaching argument?
- **The teaching beat:** what you'll say or ask at this image (NOT a textbook description — the specific point this image makes in the session)
- **One question to ask the audience** at this image
- **Anticipated wrong answer** and how to use it as a teaching moment

### 3. Image-to-image transitions

Between images, what's the bridge? "This case showed X; the next case shows what happens when X is absent." Transitions are where learning consolidates.

### 4. The reveal moment

Most image-based sessions have a "reveal" — the unexpected case, the trick, the point where the audience's pattern breaks. Identify where it is in your session and what makes it work.

### 5. Closing synthesis

How do you tie the session together at the end? Not "any questions" — the explicit reinforcement of the teaching argument with the specific evidence the images supplied.

## Hard rules

- The session has a teaching argument, stated explicitly
- Each image advances the argument
- Transitions are explicit, not assumed
- The reveal is identified
- Closing synthesis ties back to the opening thesis

## What I will NOT accept

- "Here are some cases" structure without an argument
- Images that are interesting but don't connect
- A closing that's "questions?" rather than synthesis
- Anticipated audience answers that are softball
```

## Expected output

A session plan with explicit argument, 6-10 images with positioning and teaching beats, transitions, reveal, and closing synthesis. Length 600-1000 words.

## Common failure modes

- **No teaching argument** — just a list of cases. Push back: "What's the thesis?"
- **Generic teaching beats** — "describe what you see" repeated 10 times. Push for the specific point each image makes.
- **Reveal feels arbitrary** — happens because the model didn't plan it. Push for a deliberate reveal.

## Required human verification

- Pilot the session structure with a colleague who teaches the same topic. Their feedback on what the audience actually learns matters more than the plan looks.
- Verify image diagnoses against the published key for each case.
- After the first delivery, write down what worked and what didn't. Image-based sessions improve with iteration.

## Best model and why

**Claude Opus 4.7** — structuring a multi-image teaching argument across 6-10 cases requires substantive synthesis. Opus produces tighter teaching arcs than Sonnet. The reveal-moment design also benefits from Opus's narrative judgment.
