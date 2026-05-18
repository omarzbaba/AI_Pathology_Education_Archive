---
title: Board prep schedule
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: >10min
visual: text-only
tags: planning, board-prep
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generates a personalized board prep schedule that adapts to your actual constraints (weeks remaining, daily hours available, strongest/weakest subspecialties, resources you'll use). Includes mandatory rest days, a rescue week near the exam, and explicit pre-exam-week guidance — features that distinguish a realistic schedule from a hypothetical one.

## When to use it

At the start of dedicated board prep, when re-allocating an existing plan that's not working, or when a life event (illness, rotation change, family) requires re-planning. Best done with honest self-assessment — the schedule is only as good as your input.

**Not for:** replacing experienced mentor advice (talk to recent graduates), schedules that don't account for clinical work continuing alongside prep (state explicitly), or first-time test-takers who need help calibrating ambitions (talk to a colleague first).

## The prompt

```
You are building me a board prep schedule. Be specific about resources, build in rest, and call out tradeoffs honestly. A schedule I can't sustain is worse than no schedule.

## My situation

- **Exam:** [name, date, format]
- **Weeks until exam:** [N]
- **Daily hours I can commit:** [weekdays X hours, weekends Y hours — be honest, not aspirational]
- **Clinical workload during prep:** [continuing rotations / dedicated study time / hybrid — describe]
- **Self-assessment by subspecialty:**
  - **Strong** (can pass at this moment): [list]
  - **Moderate** (would struggle on harder questions): [list]
  - **Weak** (would fail a focused section): [list]
- **Resources I have:** [qbank name, textbook, review course, study group, etc.]
- **Constraints I want you to respect:** [e.g., "I have a wedding week 8", "I can't study after 8pm", "I need at least one full day off per week"]

## Inconsistency check — do this FIRST

If my self-assessment looks internally inconsistent (a topic listed as "Strong" but also as something I want extra time on, or "Weak" topics that aren't in my resources), ASK me to clarify before generating the schedule.

## What to produce

### Week-by-week schedule

For each week:
- Topics covered (more time on weak areas, maintenance on strong areas)
- Daily breakdown: reading hours, qbank hours, review hours
- ONE rest day per week — not optional
- Specific resource mappings ("Tuesday: 2 hrs Robbins chapter 12 + 1 hr USMLE-style qbank on this topic")

### Required structural features

- **Rescue week** 2 weeks before the exam: re-attack the topics still weak after first pass
- **The week before the exam:** zero new material, focused review only
- **The last 48 hours:** explicit instructions (sleep schedule, light review, no caffeine experimentation, where to be the night before)

### Honest tradeoffs

If my hours and weak areas don't allow full coverage:
- Name which topics get less time and why
- Identify the topics that, if cut entirely, would most hurt me
- Suggest the lowest-cost compromise

### A daily/weekly check-in protocol

How will I know mid-week if the schedule is working or not, and what's my decision rule for adjusting?

## Hard rules

- **No 7-day weeks.** Rest is required.
- **No schedules that ignore my stated constraints.** If I said I can't study after 8pm, don't schedule 9pm review.
- **Resource use must be specific.** "Read about X" is not specific; "Read Robbins ch. 12 pp. 423-441" is.
- **Don't promise comprehensive coverage if hours don't support it.** Tradeoff honesty.
- **Last 48 hours guidance is non-negotiable.** Include it.

## What I will NOT accept

- All days look the same (no week-over-week rhythm)
- Resource use vague enough to be wishful
- Pretending I can study comprehensively when I can't
```

## Expected output

A week-by-week schedule with daily breakdown, named rest days, a rescue week, pre-exam-week and 48-hour guidance, honest tradeoffs section, and a mid-cycle check-in protocol. Length varies with weeks; usually 800-1500 words.

## Common failure modes

- **Aspirational hours that don't match what you said.** Push back.
- **Topics all weighted equally despite your gap profile.** Push back: "Give weak topics more time."
- **No rescue week.** Push back.
- **48-hour instructions missing.** Push back.

## Required human verification

- Run the schedule by a colleague who's recently taken the same exam. They'll spot infeasibilities you and the model both miss.
- Adjust at end of week 2 based on actual sustainability. The initial plan is a hypothesis.
- If clinical work continues during prep, talk to your program director about whether the schedule is compatible with your rotation responsibilities.

## Best model and why

**Claude Sonnet 4.6** — week-by-week structured planning with constraints is well within Sonnet's range. **Opus** is overkill unless the situation is unusual (re-take, very compressed time, complex life constraints).
