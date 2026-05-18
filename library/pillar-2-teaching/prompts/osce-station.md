---
title: OSCE station drafting
pillar: teaching
event_type: n/a
audience: faculty
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: osce, assessment, simulation
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Drafts a complete OSCE station: examinee instructions, simulated-other-party script that handles real conversational variation, expected examinee actions ranked by importance, a behaviorally-anchored scoring rubric, and a "red flag" list of actions that should trigger remediation review.

OSCEs are easy to design badly. The two failure modes: (1) the script is rigid and breaks when the examinee asks an unexpected question, (2) the rubric is too vague for two raters to score the same examinee the same way.

## When to use it

Designing summative or formative OSCE assessment, especially for stations that test communication or reasoning rather than knowledge. Also useful as a teaching tool — running a formative OSCE with a coaching debrief.

**Not for:** assessment without pilot testing (OSCEs need calibration), high-stakes credentialing stations without psychometric review, or replacing your program's standard OSCE design process.

## The prompt

```
You are drafting a complete OSCE station. The script must handle conversational variation; the rubric must enable two raters to score the same examinee the same way.

## What I'm building

- **Target audience:** [e.g., "CP residents at end-of-year assessment", "first-year fellows"]
- **Scenario:** [e.g., "critical value notification to a covering physician at 2am", "frozen section consultation with a surgeon in the OR", "handover to inpatient team after a complex case"]
- **Station length:** [in minutes — typically 7-10]
- **Number of raters:** [single rater / two raters scoring independently]
- **Pass / fail or graded:** [which]

## What to produce — 5 parts

### Part 1: Examinee instructions

What the examinee reads/hears before walking in. Should include:
- The scenario context (1-2 sentences)
- What they're expected to do
- Time limit
- Any props or materials available
- A clear stopping condition (when do they know they're done?)

### Part 2: Simulated other party script

The simulated patient, clinician, or other party. Should include:
- Opening line (what they say first)
- Responses to the 4-5 most likely examinee openers — each with the words they'd actually say
- Information they hold back unless directly asked
- How they respond to a non-empathetic examinee vs an empathetic one
- A "if asked about X" reference for tangential topics
- A wind-down trigger that helps end the station gracefully

### Part 3: Expected examinee actions

Organized as:
- **MUST DO** (failure to do these = critical fail)
- **SHOULD DO** (full credit)
- **OPTIONAL** (above-and-beyond)

For each action, name the specific behavior. Not "communicate effectively" — "explicitly state the patient identifier and the critical value within the first 30 seconds of the call."

### Part 4: Scoring rubric

5-7 dimensions, each with:
- Dimension name
- **Behavioral anchors at 4 levels:** Novice / Developing / Competent / Proficient
- The specific observable behavior at each level

Dimensions should cover: communication, content accuracy, prioritization, professionalism. Each dimension should be independently rateable.

### Part 5: Red flag list

Actions that, if performed, should trigger remediation review:
- Patient safety issues
- Professionalism violations
- Egregious communication failures

Be specific — these are the actions that get reported up, so they need to be unambiguous.

## Hard rules

- **The script must handle conversational variation.** A rigid script that only works if the examinee asks specific questions is broken.
- **Rubric anchors must be behaviorally specific.** "Demonstrates good communication" is not an anchor; "explicitly summarizes the situation, asks for read-back, and confirms next steps before ending the call" is.
- **Inter-rater reliability is the test.** If two raters can read the rubric and rate the same examinee differently, the anchors aren't specific enough.
- **The red flag list is for unambiguous actions only.** "Behaved unprofessionally" is not a red flag; "made a comment about the patient's appearance" might be.

## What I will NOT accept

- A rigid script that breaks under conversational variation
- Vague rubric anchors ("shows competence")
- Red flag items that require subjective judgment
- Expected actions that aren't observable
```

## Expected output

5 parts: examinee instructions, simulated party script with conversational variation, ranked expected actions, behaviorally-anchored 5-7 dimension rubric, red flag list. Length 800-1500 words for a typical 7-10 minute station.

## Common failure modes

- **Script too rigid.** Push back: "Add responses for [common variations]."
- **Vague rubric anchors.** Push back: "Name the specific observable behavior at each level."
- **Red flag list with subjective items.** Push back: "These need to be unambiguous."

## Required human verification

- **Pilot the station** with a faculty member playing the examinee role before formal use.
- **Have a second rater score a video of the pilot independently.** If inter-rater agreement is low, the rubric needs more anchoring.
- **Verify clinical content** (drug doses, lab cutoffs, procedural steps) against current practice.
- **For high-stakes use,** consider psychometric review of the station before deployment.

## Best model and why

**Claude Opus 4.7** — multi-part OSCE artifacts (script, rubric, red-flag list) need internal consistency that Opus holds together better than Sonnet. The conversational-variation handling in the script also benefits from Opus's depth.
