---
title: Reverse case drill — findings to diagnosis
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: case-based, drilling, reasoning
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

You provide a set of findings from a case (anonymized, no PHI). The model works the case in reverse — from findings alone, walking through the differential, narrowing systematically, reaching a diagnosis, and naming the piece of evidence it most wanted. Then you compare your reasoning path against the model's, not to find out who's "right" but to surface where your reasoning shortcuts diverged.

The drill is in your interpretation, not in receiving the answer.

## When to use it

After you've signed out a case where the diagnosis was non-obvious or required extensive workup, when you want to test whether you'd reach the same conclusion working from the findings alone. Especially valuable for cases where you anchored on a wrong diagnosis early and want to understand why.

**Not for:** real-time clinical case interpretation (the model is not a consult), simple cases where the diagnosis was obvious (no learning to extract), or cases you can't anonymize (see safety section).

## Safety — critical PHI guard

**Read every time, no exceptions:** the findings you paste must be **de-identified** with no patient identifiers — no name, MRN, accession number, exact date of service, exact age (use age range), institutional identifiers, or rare-finding combinations sufficient for re-identification.

If you cannot adequately de-identify a case, **do not use this prompt**. Use a published teaching case instead. See [Guardrails](library.html#/docs/guardrails).

## The prompt

```
You are my case-reasoning drill partner. I will give you findings from a case I just worked. Work the case in reverse, starting from the findings alone — do not skip steps even if the answer seems obvious. After your walkthrough, I'll share what I actually concluded and we'll compare reasoning paths.

## Provenance check

Before responding, confirm: the findings I paste contain no patient identifiers (name, MRN, accession, exact age, exact date of service, institutional ID, or rare-finding combinations that enable re-identification). If anything in what I paste looks identifiable, STOP and tell me before proceeding — do not work the case until I confirm de-identification.

## What I'm pasting

- **Clinical context (de-identified):** [age range, sex if relevant to differential, brief presentation — no specifics]
- **Findings:** [labs, imaging summary, morphology description, IHC, molecular — whatever was available, in the order you encountered them]
- **What I want from the drill:** [optional — e.g., "stress test my anchoring", "I think I missed something subtle", "I want to see if a fresh look reaches the same place"]

## How to work the case — show the work

### Step 1: Initial framing (1 paragraph)

Given the clinical context and the first few findings, what is the broad diagnostic category in play? What is the pretest probability landscape (common things common, but adjust for the specific demographic and context)?

### Step 2: Differential at first pass (3-6 entities)

Generate a broad differential based on the findings. For each entity, name:
- The specific finding(s) putting it on the differential
- The specific finding(s) that would push it OFF the differential

### Step 3: Narrowing (walk it down, in stages)

Take the findings in order. At each new finding, name how it shifts the differential — which entities move up, which move down, which drop off. Show the reasoning, not just the conclusion.

### Step 4: Final diagnosis

State the diagnosis. Acknowledge your confidence level explicitly (e.g., "high confidence", "consistent with but other entities not fully excluded").

### Step 5: The piece of evidence you most wanted that you didn't have

Name the single test, finding, or clinical detail that would have most increased your diagnostic confidence. What would it have ruled in or out?

### Step 6: Where this case could go wrong

Name the 1-2 alternative diagnoses that a reasonable pathologist could have landed on instead, and what would distinguish them.

## Hard rules

- **Do not skip Steps 1-3.** The drill is in the reasoning, not in arriving at the diagnosis. If you jump from findings to diagnosis, you've defeated the prompt.
- **Use only the findings I gave you.** Do not invent findings that weren't there.
- **Acknowledge uncertainty.** If the findings genuinely don't support a confident diagnosis, say so.
- **Do not soften the differential to flatter my expected answer.** If a less likely entity belongs on the differential, include it.
```

## Expected output

Six steps in order, with the reasoning shown explicitly at each. The "piece of evidence I most wanted" is often the most valuable part — it surfaces what the model would have done differently if you'd ordered different workup. After you share your actual conclusion, the comparison conversation is where the learning happens.

## Common failure modes

- **Skipping steps to reach the diagnosis fast.** Push back: "Slow down. Walk through Step 2 — what's the full differential?"
- **Inventing findings that weren't in your paste.** Push back: "I didn't tell you about [feature]. Where did you get that?"
- **Anchoring on the first plausible diagnosis** without working through alternatives. Push back: "Walk through what would shift you to [other entity]."
- **The model softens its differential to match what it thinks you concluded.** Push back: "What's YOUR reading independent of my opinion?"

## Required human verification

- **PHI strip is the most important step.** Verify before pasting. The model cannot un-see information once you've shown it to it.
- **Treat the model's final diagnosis as fallible.** This is a structured comparison of reasoning paths, not a second opinion.
- **The "piece of evidence I most wanted" insight is often the most useful — pay attention to it.** It often surfaces workup decisions you could revise for future cases.

## Best model and why

**Claude Opus 4.7** — explicit reasoning chains under diagnostic uncertainty are Opus's strongest use case. Sonnet skips steps in case reasoning; Opus shows the work, which is the point of the drill. For pure pattern-recognition tasks, Sonnet is fine — but reverse case reasoning is what makes Opus worth the extra cost.
