---
title: Lab incident debrief template
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: incident, debrief, just-culture, quality
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generates a structured debrief template for when something has gone wrong in the lab — specimen lost, critical value missed, mis-identification, wrong-patient result, near-miss. The template follows just-culture principles: structured to find systemic causes rather than assign individual blame, while preserving accountability where individual choice is relevant.

## When to use it

After a lab incident or near-miss that warrants formal review. Especially valuable when residents or trainees were involved — the debrief framing dramatically affects whether they speak up about future near-misses.

**Not for:** routine quality review (different process), incidents involving patient safety issues that require institutional reporting (those follow specific protocols — escalate first), or contexts where you don't have buy-in for a just-culture approach.

## The prompt

```
You are generating a structured debrief template for a lab incident. Use just-culture framing: structured to find systemic causes, not assign blame, while preserving accountability where individual choice mattered.

## What I'm preparing for

- **Incident type:** [specimen lost / critical value not called / wrong-patient result / mis-identification / near-miss / other]
- **Brief description (de-identified):** [what happened, when, who was involved by role]
- **Severity:** [actual patient impact / no impact / near-miss]
- **People involved (by role, not name):** [e.g., "PGY-2 resident, charge tech, attending"]
- **My role in the debrief:** [facilitator / participant / observer]
- **Institutional reporting status:** [has this been reported up? to whom?]

## CRITICAL FIRST STEP

If this incident involves potential patient harm, specific reporting obligations may apply (institutional QI/safety reporting, regulatory reporting, peer review processes). Confirm with the appropriate institutional office BEFORE running an informal debrief, since debrief content may have different protections depending on the framework used.

## Debrief structure (60-75 minutes)

### Phase 1: Set the frame (5 min)
What to say to open the debrief that establishes psychological safety. Verbatim suggestion for the opening 3-4 sentences.

### Phase 2: Walk-through of what happened (15-20 min)
Each person involved walks through the event from their perspective in chronological order. Rules:
- No interruptions during walk-through
- Facts only — not interpretations
- "I" statements, not "we" or "you"
- Time-stamped where possible

Script for what the facilitator says between walk-throughs.

### Phase 3: Identify the contributing factors (20 min)
Use a structured framework:
- **Systemic factors:** workflow design, staffing, time pressure, training adequacy, tool/IT support, environment
- **Communication factors:** handoffs, escalation paths, documentation
- **Individual factors:** knowledge gaps, attentional issues, decision-making — but ONLY when these are factors that are reasonable to expect of someone with this training
- **What was DIFFERENT this time** compared to when this work usually goes right

For each factor identified, ask: "If we fixed this, would it prevent this incident from happening again? Would it prevent OTHER incidents?"

### Phase 4: Distinguish system vs individual contribution (10 min)
Apply just-culture framework:
- **Human error:** an inadvertent action; slip; lapse; mistake. System fix needed.
- **At-risk behavior:** a choice where risk wasn't recognized or was mistakenly believed justified. Coaching needed.
- **Reckless behavior:** conscious disregard of substantial and unjustifiable risk. Accountability needed.

Be careful: most incidents involve some of each. Don't force a single category.

### Phase 5: Actions (15 min)
For each contributing factor:
- **What's the change?** Specific, observable.
- **Who owns it?** Named individual.
- **By when?** Specific date.
- **How will we know it worked?** Observable indicator.

### Phase 6: Close (5 min)
- Summarize commitments
- Acknowledge the people involved
- Set follow-up date

## Hard rules

- **Just culture framing throughout.** Do not slip into blame language.
- **Distinguish system vs individual contribution.** Don't lump them.
- **Actions must have owners and dates.** Otherwise they don't happen.
- **Acknowledge regulatory and reporting obligations.** Do not run an informal debrief in place of required institutional process.

## What I will NOT accept

- Blame-oriented framing
- Actions without owners
- Skipping just-culture framework on the assumption "it was just human error"
- Treating this as a substitute for required institutional reporting
```

## Expected output

A 6-phase debrief template with verbatim suggestions for opening, walk-through framing, and contributing factor analysis. Length 800-1200 words.

## Common failure modes

- **Blame framing slipping in.** Push back: "Reframe in just-culture terms."
- **Forcing single categorization** (all "human error" or all "system"). Push for nuance.
- **Vague actions.** Push for specific owners and dates.

## Required human verification

- **Confirm institutional reporting and protection frameworks** before running the debrief. Some incidents must go through specific QI/peer-review processes that have legal protections.
- **Run by your quality and safety leadership** before using this template for the first time.
- **Document outcomes per your institution's process** — informal notes may not have the protections of formal QI documentation.

## Best model and why

**Claude Opus 4.7** — high-stakes facilitation with multiple stakeholder dynamics requires depth and judgment. Opus is better at the just-culture distinction than Sonnet.
