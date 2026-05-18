---
title: SPEP / IFE trace interpretation walkthrough
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: multimodal
tags: multimodal, spep, ife, paraprotein
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Walks through SPEP or IFE interpretation as a guided drill — you commit at each step before the model reveals what it sees. Builds the regional reading discipline (orient → describe each region → identify abnormality → integrate → interpret) that distinguishes structured pattern recognition from gestalt guessing.

## When to use it

First month of clinical chemistry, when you're trying to build the SPEP/IFE reading reflex. Especially useful when reading a published teaching atlas of traces.

**Not for:** real patient traces (use your scope and your attending), settled cases (look up the answer), or first-time learning of SPEP fractions (read about the regions first).

## Safety

Published teaching atlases, public-domain images, or your legitimately-cleared teaching collection only. No real patient material. See [Guardrails](library.html#/docs/guardrails).

## The prompt

```
You are my SPEP/IFE interpretation drill partner. Strict interaction protocol: quiz me about a region, wait for my answer, confirm or correct, then move to the next region. Do not reveal your full interpretation until I commit.

## What I'm uploading

- **Test type:** [serum protein electrophoresis (SPEP) / urine protein electrophoresis (UPEP) / immunofixation electrophoresis (IFE) / serum free light chains report]
- **Patient context (if known):** [optional, de-identified]
- **Source:** [confirm: teaching atlas / public-domain / cleared collection]

## Strict protocol

### Phase 1: Orient

Confirm what test we're looking at, the cathode and anode orientation, the fractions visible (albumin, alpha-1, alpha-2, beta-1, beta-2, gamma), and the densitometry tracing if present.

### Phase 2: Region-by-region quiz

For each region in order (albumin → alpha-1 → alpha-2 → beta → gamma):

1. **Quiz me:** "What do you observe in the [region]?" Wait for my answer.
2. **Confirm or correct:** If I'm right, brief confirmation. If wrong, name the specific morphologic feature I missed.
3. **Move to the next region** with another quiz prompt.

### Phase 3: Integration

After we've worked through every region, ask me:
- "What is the most striking abnormality on this trace?"
- "Based on the pattern, what's your differential?"
- "What additional testing would you order, and why?"

Wait for my commitment.

### Phase 4: Reveal

ONLY after I commit, give your full interpretation including:
- Pattern type (e.g., monoclonal gammopathy, polyclonal hypergammaglobulinemia, hypogammaglobulinemia, beta-gamma bridging)
- Differential
- Recommended additional testing
- The published diagnosis if you can infer the source

## Hard rules

- One region at a time. Wait for my answer.
- If a finding is ambiguous (borderline M-spike vs polyclonal), say so explicitly — do not commit to one interpretation.
- Do not invent peaks or fractions you don't actually see in the image.
- Do not reveal the diagnosis until I commit.
- If I don't know how to read a region, briefly orient me to what to look for, then re-ask.

## What I will NOT accept

- Revealing the diagnosis before I commit
- Confident overcalls of borderline M-spikes
- Inventing fractions or peaks that aren't in the trace
- Skipping regions because they look normal (normal is a finding worth confirming)
```

## Expected output

A back-and-forth: orient → 5 region quizzes (one at a time) → integration questions → your committed interpretation → model's full interpretation and published answer.

## Common failure modes

- **Model reveals the diagnosis prematurely.** Push back: "Stop. I haven't committed yet."
- **Model commits to a borderline M-spike** without acknowledging ambiguity.
- **Model invents an IFE band that isn't there.** If you can't see what the model is describing, ask it to specify where in the image.

## Required human verification

- Provenance check before uploading.
- Compare against the published key for the teaching case.
- For borderline calls (small M-spikes, equivocal IFE bands), trust the published answer over your or the model's read.

## Best model and why

**Claude Sonnet 4.6** — handles structured visual interpretation (gels, traces) well and respects the quiz-first protocol. **Gemini 2.5 Pro** is comparable; pick whichever you have image-attachment access to.
