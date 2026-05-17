---
title: Slide outline for a 1-hour lecture
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: lecture, slides
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate a slide outline for a 1-hour lecture, including timing, beat structure, and recommended visuals for each slide.

## When to use it

When you've agreed to give a lecture and need a starting structure before you put a single slide in PowerPoint. Saves the 'staring at empty slides' phase.

## The prompt

```
Generate a slide outline for a 1-hour lecture on [topic] for [audience].

Structure:

- **Total slides: 35-45.** Roughly 1 slide per 80-100 seconds. Resist the urge to cram more.
- **Beat structure:** opening hook (1 slide, 2-3 min) → roadmap (1 slide) → 3-4 content beats (8-12 slides each, ~12-15 min each) → synthesis (2-3 slides) → questions (1 slide, 5-10 min).
- **For each slide:** title, 2-3 bullet points of content (not full sentences), and a one-line recommended visual ('photomicrograph of X', 'algorithm flowchart', 'table comparing A and B', 'text only').
- **Mark moments of audience interaction** (poll, question, case to think about) at the transitions between beats.
- **Identify the 2 slides that, if you only had 30 seconds, you'd use.** Those are the slides that anchor the lecture.

After the outline, name the most likely point in the lecture where you'll run out of time, and the 2-3 slides you'd cut to recover.
```

## Expected output

A 35-45 slide outline with titles, brief content, visuals, and interaction beats. Plus the anchor slides and a contingency cut list.

## Common failure modes

- The outline is text-heavy with no visual diversity — every slide is 'bullet points'.
- The interaction beats are filler rather than substantive.
- The 'anchor slides' aren't actually the most important; they're the ones that came first in the outline.

## Required human verification

- Walk through the outline at presentation pace (~80 seconds per slide). Does the timing work?
- Verify the substantive content for each beat against your subspecialty's reference. The model may sketch beats that turn out to be technically wrong.
- The recommended visuals are starting points; you supply the actual images and verify they're properly licensed.
