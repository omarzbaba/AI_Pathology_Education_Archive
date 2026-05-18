---
title: Critical value workflow drill
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: critical-values, lab-workflow, cp, notification
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Drill the complete critical value workflow for a given result: confirm the value is real, identify and notify the right provider, document the call, follow up on disposition, and recognize when a value crosses from critical to call-the-rapid-response. This is a practical CP skill that is rarely formally taught and frequently mishandled.

## When to use it

During your first month of CP call or as a resident-as-teacher session for a junior. Especially valuable when you want to practice the harder version: a critical value where the call isn't obvious (chronic dialysis patient with chronically critical K+, the panic value that's a known previous trend, the value that's critical at one institution but not another).

## The prompt

```
You are my critical value workflow drill partner. Walk me through a single case end-to-end, including the parts that residents typically skip.

## The case I'm working

- **The result:** [e.g., "potassium 7.2 mmol/L on a chemistry panel"]
- **Patient context (de-identified):** [e.g., "outpatient on chronic hemodialysis", "ICU patient post-op", "young adult in the ED"]
- **What I would do (my draft plan):** [briefly state what you'd do — this is the calibration step]

## What to produce — IN ORDER

### Step 1: Is the value real?

Walk through the pre-analytical considerations:
- Pseudohyperkalemia / hemolysis / sample handling issues for the specific value
- Whether to repeat, draw a verification sample, or accept the value
- The specific evidence in the result that would push you one way or the other (e.g., HI index, sample status flags)
- What a "real" result looks like vs an artifact

### Step 2: Is this a critical value at THIS institution and for THIS patient?

- The institutional critical value threshold for this analyte (acknowledge that thresholds vary; ask me what mine is if relevant)
- Whether patient context changes the urgency (chronic vs acute, expected vs unexpected, ICU vs outpatient)
- When a critical value is NOT critical at the patient level (e.g., chronic dialysis pt with chronically elevated K+) and how to document that judgment

### Step 3: Notification

- Who is the right person to call (ordering provider vs covering vs nurse — institutional variation acknowledged)
- The actual notification script (concise, structured: "this is [name] from the lab calling with a critical value for patient [identifier]: [result] at [time], the value is [interpretation], please acknowledge")
- Read-back: what's required and how to obtain it
- What to do if you can't reach the ordering provider

### Step 4: Documentation

- What MUST be documented in the LIS (or your institutional system)
- Format: who called, when called, who acknowledged (name, role), read-back confirmation, any patient-care implications discussed
- Common documentation failures (vague "RN notified", no time stamp, no read-back, no follow-up note)

### Step 5: Follow-up

- What follow-up the lab should do (recheck plan, additional testing, related results to flag)
- When to escalate (no acknowledgment, no read-back, repeat critical value, value rising)
- The boundary between "critical value notified" and "this needs rapid response NOW" — and who decides

### Then critique my draft plan

After all five steps, review my draft plan against your walkthrough. Tell me:
- What I did well
- What I missed
- The single most important thing I should change

## Hard rules

- **Acknowledge institutional variation.** Critical value thresholds, notification policies, and documentation requirements differ by institution. State this and tell me to verify against my institutional policy.
- **Do NOT invent specific institutional policies.** "This institution requires X" without knowing my institution is wrong.
- **Be specific about the script.** Vague "call the provider" is useless; an actual phone script is the deliverable.
```

## Expected output

Five steps walked through systematically, then a critique of your draft plan. Should feel like a structured simulation, not a textbook chapter.

## Common failure modes

- **The model skips Step 1.** Pseudo-results are common and a residents-skip-this trap. Push back if Step 1 is perfunctory.
- **Specific institutional policies invented.** The model says "your institution requires X" without knowing. Push back: "How would I find out what MY institution requires?"
- **Notification script is generic.** Push for the exact words.
- **Documentation step is hand-waved.** Push for the specific elements.

## Required human verification

- **Verify the threshold and policy against your institution.** Critical value thresholds and notification policies are institution-specific; the model's defaults may not match yours.
- **Confirm the read-back requirement** under CLIA / The Joint Commission / your accreditation framework — these have specific language.
- **Practice the script aloud once.** Talking through the script is different from reading it.

## Best model and why

**Claude Sonnet 4.6** — structured procedural walkthroughs are Sonnet's strength. **Avoid Opus** for this prompt; it tends to over-elaborate the pre-analytical step. The value is in the systematic discipline, not depth.
