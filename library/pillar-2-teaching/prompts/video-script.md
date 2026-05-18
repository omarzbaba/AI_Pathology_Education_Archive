---
title: Video script and storyboard
pillar: teaching
event_type: n/a
audience: faculty
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: video, scripting, storyboard
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Drafts a 2-column video script (narration / visuals) for a short educational explainer, with timed beats, specific visual cues, opening hook, and a single takeaway. Built for short asynchronous content (2-5 min) where pacing and visual design matter more than depth.

## When to use it

When you're producing educational video content for asynchronous viewing — onboarding clips, social media explainers, training modules. Especially useful as a starting structure before you record.

**Not for:** long lectures (different format), live demos, or contexts where you're not actually planning to produce video.

## The prompt

```
You are drafting a script for a short educational video. The script must work as video, not as a talking-head reading lecture notes. Hook in 5 seconds, takeaway in the last 5 seconds.

## What I'm producing

- **Topic:** [be specific]
- **Target duration:** [in minutes — be honest about what fits]
- **Audience:** [target — students, residents, patients, etc.]
- **Production capacity:** [I'm shooting myself with a phone / professional setup / animation only — calibrates visual complexity]
- **Distribution:** [internal training / public / specific platform]

## Format — two columns, timed beats

| Time | Narration | Visual |
|------|-----------|--------|
| 0:00-0:05 | [opening hook] | [shot description] |
| 0:05-0:15 | [next beat] | [shot or on-screen text] |

Each row = 5-15 seconds of video. Be specific about visuals.

## Required elements

### Opening hook (0:00-0:05)
The first 5 seconds must give viewer a reason to keep watching. Stating the topic is NOT a hook. Hooks that work:
- A specific question or statistic
- A surprising claim
- A case scenario in one sentence
- A contrarian framing

### Body (most of the duration)
Build the argument in beats. Each beat advances the explanation. Maximum 4-5 beats for a 3-minute video.

### Visuals
For each beat: 'cut to photomicrograph', 'animated diagram of antibody binding', 'on-screen text: NORMAL RANGE 4.0-11.0 K/uL', 'B-roll of lab', etc. Be specific.

### Single takeaway (last 5 seconds)
The one sentence viewers will remember 24 hours later. State it on-screen as text AND say it in narration.

## After the script

List:
- **Assets I'll need to produce or source** (2-3 most important)
- **Estimated word count of narration** (compare against speaking-pace target of 150 wpm — flag if script will overrun)

## Hard rules

- **Hook in 5 seconds.** Not "introduction" — hook.
- **Visuals are specific, not placeholder.** "Relevant image" is not specific.
- **Total narration word count must fit the duration at 150 wpm.** Sum it and check.
- **One takeaway, not five.** A 3-minute video with 5 takeaways has zero takeaways.

## What I will NOT accept

- Hook that's "Hi, today we're going to talk about X"
- Generic visuals
- Script that overruns the target duration when read aloud at 150 wpm
- More than one takeaway
```

## Expected output

A 2-column timed script + asset list + word-count check. Length depends on target duration.

## Common failure modes

- **Weak hook.** Push back: "Make the first 5 seconds make me want to keep watching."
- **Vague visuals.** Push back: "What's actually on screen?"
- **Script too long.** Verify word count.

## Required human verification

- Read the script aloud at natural pace and time it. AI scripts almost always overrun.
- Verify any specific clinical content.
- Source visuals from properly licensed material.

## Best model and why

**Claude Sonnet 4.6** — structured creative writing with timing is Sonnet's strength.
