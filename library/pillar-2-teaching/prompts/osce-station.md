---
title: OSCE station drafting
pillar: teaching
event_type: n/a
audience: faculty
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: osce, assessment
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Draft an OSCE station with patient script, stem, expected examinee actions, and a scoring rubric.

## When to use it

When designing summative or formative OSCE assessment, especially for stations that test communication or reasoning rather than knowledge.

## The prompt

```
Draft an OSCE station for [target audience — e.g., 'CP residents at end-of-year assessment'] on [scenario type — e.g., 'critical value notification', 'frozen section consultation', 'handover to inpatient team'].

The station should include:

1. **Station instructions for the examinee** (what they're walking into, what they're expected to do, time limit).
2. **Patient/clinician script** for the simulated other party — what they say in response to common openers, what they hold back unless asked, how they respond to the examinee's communication style.
3. **The expected examinee actions** organized as: must do, should do, optional.
4. **A scoring rubric** with weighted line items — communication, content accuracy, prioritization, professionalism. Each item with behavioral anchors for novice/competent/proficient.
5. **A 'red flag' list** — actions that, if performed, indicate the examinee should be flagged for remediation.

Length: realistic for a 7-10 minute station.
```

## Expected output

A complete station packet ready for use: examinee instructions, script, action checklist, rubric, and red flag criteria.

## Common failure modes

- The script is too rigid and breaks if the examinee asks unexpected questions.
- The rubric items are vague and can't actually be scored reliably by two raters.
- Red flag list confuses 'made a mistake' with 'is unsafe to practice'.

## Required human verification

- Pilot the station with a faculty member playing the examinee role before using it in formal assessment.
- Have a second rater score a video of the pilot independently — if you don't get agreement, the rubric needs more behavioral anchoring.
- Verify the clinical content (any lab values, drug names, dose adjustments) against current practice.
