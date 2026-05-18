---
title: Slide outline for a 1-hour lecture
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: lecture, slides, timing
verified_months: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generates a slide outline for a 1-hour lecture: 35-45 slides, beat structure (hook → roadmap → 3-4 content beats → synthesis → Q&A), per-slide visuals, audience interaction moments, anchor slides, and a contingency cut list for when you run out of time.

Breaks the staring-at-empty-PowerPoint paralysis.

## When to use it

When you've agreed to give a lecture and need a starting structure. Best done 2-3 weeks before, leaving time to slot in your actual content and refine.

**Not for:** short talks (different format), workshops (different design), or generating the actual slides (this is outline only).

## The prompt

```
You are generating a slide outline for a 1-hour lecture. Stay disciplined about timing and visual diversity. Resist the urge to cram more slides.

## What I'm building

- **Topic:** [be specific]
- **Audience:** [PGY level / faculty / mixed — describe]
- **Lecture context:** [grand rounds / didactic conference / society talk / industry CME — affects tone]
- **My existing materials:** [any slides, papers, prior talks I can draw from]
- **The ONE thing I want the audience to walk away with:** [stated explicitly]

## What to produce

### Beat structure (timed)

- **Opening hook** (1 slide, 2-3 min) — what's the specific hook? A case? A statistic? A contrarian framing?
- **Roadmap** (1 slide, 1 min) — preview the 3-4 content beats
- **Content beats** (3-4 beats, 8-12 slides each, ~12-15 min each)
- **Synthesis** (2-3 slides, 3-5 min)
- **Q&A buffer** (1 slide, 5-10 min)

Total slides: 35-45. Roughly 1 slide per 80-100 seconds of speaking time.

### Per-slide outline

For each slide:
- **Title** (the actual title, not a placeholder)
- **2-3 content bullets** (what's on the slide — bullets, not full sentences)
- **Recommended visual** (one line: 'photomicrograph of X', 'algorithm flowchart', 'table comparing A and B', 'text only')
- **Speaking time** (typically 60-120 sec)

### Audience interaction beats

Mark 2-4 moments where you'd interrupt the lecture with:
- A poll question
- A case to think about
- A question to the room
- A "raise your hand if..." check-in

These usually go at transitions between beats.

### Anchor slides

Identify the 2-3 slides that, if you only had 30 seconds, you'd use. These anchor the lecture.

### Contingency cut list

Identify the 3-5 slides you'd cut FIRST if you run out of time, and why those specifically (not anchor slides, not central to the argument).

### Time-budget check

After producing the outline, sum the speaking time per slide. Confirm it fits 60 minutes including Q&A. Flag if it doesn't and recommend specific compressions.

## Hard rules

- **35-45 slides total.** Resist the urge to add more.
- **Visual diversity.** Not every slide can be bullet points.
- **Audience interaction beats are non-negotiable.**
- **Timing math must add up to 60 minutes.**

## What I will NOT accept

- An outline with 80 slides
- All slides marked "text only"
- No anchor slides identified
- Timing that exceeds 60 minutes without compression recommendations
```

## Expected output

35-45 slide outline with titles, bullets, visuals, timing, interaction beats, anchors, cut list. Length 800-1500 words.

## Common failure modes

- **Over-slided.** Push back: "Cut to 40."
- **No visual diversity.** Push back: "Vary the visuals."
- **Timing math wrong.** Push back: "Add it up. Does it fit?"

## Required human verification

- Walk through the outline at presentation pace (~80 sec/slide) and check timing.
- Verify substantive content for each beat against your subspecialty's reference.
- Source the visuals from properly licensed material.

## Best model and why

**Claude Sonnet 4.6** — structured planning with timing is Sonnet's strength. Opus only if the topic is unusually complex.
