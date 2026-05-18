---
title: Photomicrograph description practice
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: multimodal
tags: multimodal, morphology, image-analysis, safety-critical
verified_models: TODO
best_model: Gemini 2.5 Pro
last_updated: 2026-05-17
---

## What this prompt does

Builds your morphologic description discipline using a published teaching image. You upload an image, the model describes what it sees and offers a differential **before you commit**, you commit your own interpretation, then you compare reasoning paths. The drill is *your description*, not the model's diagnosis.

The most important thing this prompt does is enforce the **describe-before-diagnose** habit that distinguishes pathologists who reason rigorously from those who pattern-match. The interaction protocol — image → model description → your description → comparison → published answer — is the entire point.

## When to use it

When you want **deliberate practice** on morphologic observation skills, especially:

- The first weeks of a new subspecialty rotation when your visual vocabulary is still being built
- Reviewing a teaching case you missed
- Studying a pattern you've read about but rarely seen
- Building a habit of structured visual reading before you sign out

**Not for:** clinical case interpretation (the model is not a consult), images of real patient material (see safety section below), or quick diagnoses (use a textbook).

## Safety — read this every time

**Three rules, no exceptions:**

1. **Only published teaching images, public-domain images, or legitimately-cleared teaching collection material.** No real patient images of any kind — not from your service, not from a colleague's case, not from a textbook you scanned without permission, not from your scope's snapshot folder.

2. **If you cannot demonstrate provenance,** do not upload. The fact that an image was "de-identified" by someone else is not enough.

3. **The model's diagnosis is fallible** — multimodal AI is improving fast but still routinely confidently wrong on subtle morphology. Use this prompt for *describing practice*, not for diagnosing your case.

See [Guardrails](library.html#/docs/guardrails) for the full set of multimodal rules.

## The prompt

```
You are my structured study partner for morphologic observation practice. Before we start, you must follow a strict interaction protocol: you describe first, I commit my interpretation, then we compare. Do not reveal what you think the diagnosis is until I commit.

## What I am uploading

[Briefly describe: specimen type, stain, magnification, source — e.g., "H&E-stained kidney biopsy at 200x, from a published teaching atlas case"]

**Confirm before responding:** I am affirming that this image is from a published teaching atlas, public-domain source, or a legitimately-cleared teaching collection — not real patient material. If anything I just said is unclear or the image looks like it might be a real clinical case, stop and ask me to confirm provenance before proceeding.

## What I want you to produce — IN ORDER, ONE PASS

### Phase 1: Your structured description

Describe what you see using morphologic language only — no diagnostic terms. Organize by:

1. **At low power (architecture / pattern):** what is the tissue-level architecture? Density, distribution, relationship to other structures.
2. **At mid power (cell populations):** what cell types or populations are present? Distribution? Polarity? Stromal context?
3. **At high power (cellular detail):** what nuclear features (size, shape, chromatin, nucleoli)? Cytoplasmic features? Mitoses? Specific inclusions or organelles?

**Use morphologic descriptors only.** Say "clusters of cells with hyperchromatic nuclei and a high N:C ratio" — NOT "atypical cells." Say "small lymphoid cells with mature chromatin" — NOT "benign lymphocytes." If you slip into diagnostic vocabulary, that's a failure.

### Phase 2: Cell or tissue identification

Identify the cell type or tissue type **if you can**. If you genuinely cannot identify with confidence, say so explicitly — don't bluff.

### Phase 3: Differential

Generate a differential of 3-5 entities based on the visible features. For each entity, name the **single morphologic feature** in the image that puts it on the differential.

### Phase 4: The single most discriminating next step

Name the one thing you would most want to see next to discriminate the differential — additional levels, a specific IHC stain, higher magnification, a specific molecular test. Justify in one sentence.

### Phase 5: A check question for me

Ask me ONE question about my own interpretation before you reveal what you think the diagnosis is. Example: "Before I tell you what I think this is, what did you see in the [specific region or feature]? What does that observation rule in or out?"

**STOP after the check question.** Wait for my answer before revealing your interpretation.

## Hard rules

- **Describe what is actually visible.** If a feature is not clearly in the image at the magnification provided, do NOT invent it. Multimodal AI confidently hallucinating features is the most dangerous failure mode here.
- **No diagnostic shortcuts.** Phase 1 must be pure description.
- **No premature reveal.** Do not tell me your diagnosis until I have committed mine.
- **Acknowledge uncertainty out loud.** If a feature is ambiguous in the image, say so explicitly rather than committing to one interpretation.
- **Differential must be plausible and ranked.** "5 random entities" is not a differential. Each must be defended with a specific feature you actually see.
```

## Expected output

Five phases delivered in order, ending with a check question that waits for your answer. Phase 1 should be 100-200 words of pure morphologic description (no diagnostic language). The differential in Phase 3 should be specific and feature-grounded, not a textbook chapter list. Phase 5 should be a question that makes you defend an observation, not just restate one.

The check question waiting is critical — if the model reveals its diagnosis before you commit, the entire exercise was wasted.

## Common failure modes

- **The model jumps to a diagnosis** in Phase 1, dressed up as description. Push back: "Phase 1 is description only. Re-do it without using any diagnostic terms."
- **The model uses diagnostic language disguised as description** ("atypical cells", "neoplastic glands"). Same fix.
- **The model "sees" features that aren't actually in the image** at the resolution provided. This is the most dangerous failure mode. If a described feature isn't visible to you in the image, name it back: "I don't see [feature] in this image — are you sure you're looking at the right area?"
- **The model reveals the diagnosis before you commit.** Stop the conversation: "Stop. I haven't committed yet. Go back to Phase 5."
- **The differential is too broad** (textbook list of "everything that could ever look like this") or **too narrow** (anchored on a likely answer). Push back accordingly.

## Required human verification

- **Provenance, every time.** Re-confirm to yourself that the image source is permissible before uploading. The model cannot verify provenance for you.
- **Compare against the published answer** for the teaching case. Note disagreements between the model's interpretation, your interpretation, and the published answer — all three are independent and the comparison is where the learning happens.
- **Treat the model's morphologic descriptions as fallible.** A feature confidently asserted by the model that you cannot find in the image is the failure mode. Trust the image, not the description.
- **If you find yourself using this prompt for an actual case** rather than a teaching case — stop and ask whether you should be consulting a colleague or a textbook instead.

## Best model and why

**Gemini 2.5 Pro** — currently has the strongest fine-grained image analysis for histopathology images, including accurate spatial relationship recognition at varying magnifications. **Claude Sonnet 4.6** multimodal is a comparable alternative if you prefer that ecosystem. **GPT-4o** can run this prompt but tends to be less specific about cellular-level detail. All multimodal models will confidently hallucinate features at the limits of resolution — this is the dominant failure mode regardless of model, so the verification step above is non-negotiable.
