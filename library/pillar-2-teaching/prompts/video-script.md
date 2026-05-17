---
title: Video script and storyboard
pillar: teaching
event_type: n/a
audience: faculty
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: video, scripting
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Draft a video script and storyboard for a short educational explainer, with shot suggestions and on-screen text cues.

## When to use it

When you're producing short educational content (2-5 min explainers, social media clips, asynchronous training) and need a script that thinks about visuals, not just dialogue.

## The prompt

```
Draft a script for a [duration]-minute educational video on [topic] for [audience].

Format:

- **Two columns:** left = narration; right = visuals/on-screen text/cuts.
- **One row per beat**, with each beat being 5-15 seconds of video.
- **Total length:** target the duration above; flag if the script will overrun.
- **Hook:** the first 5 seconds must give the viewer a reason to keep watching. Stating the topic isn't a hook.
- **Visuals:** 'cut to photomicrograph', 'animated diagram of antibody binding', 'on-screen text: NORMAL RANGE 4.0-11.0 K/uL'. Be specific about what's on screen at each beat.
- **End with a single takeaway** that fits in 5 seconds.

After the script, list:
- The 2-3 shots/assets I'll need to produce or source.
- The 1 sentence the viewer will remember 24 hours later.

**Important — refinement:** Read the script aloud at conversational pace (~150 words/minute). If it overruns the target duration, cut narration first; do not cut visuals or beats.
```

## Expected output

Two-column script with timed beats, opening hook, specific visuals, and a final takeaway. Plus an asset list and a stated 24-hour-takeaway.

## Common failure modes

- The 'hook' is just the topic stated declaratively.
- Visuals are placeholders ('relevant image') rather than specific.
- The script is too dense to fit in the stated duration when read at natural pace.

## Required human verification

- Read the script aloud at natural pace and time it. AI-generated scripts almost always overrun.
- Verify any specific clinical content.
- Source visuals from properly licensed material; do not use images without clear permission.

## Best model and why

**Claude Sonnet 4.6** — Two-column script with timed beats is a structured creative task — Sonnet handles it well. Aloud-test the script for natural pacing regardless of which model you use.
