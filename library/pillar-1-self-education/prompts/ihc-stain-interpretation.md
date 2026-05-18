---
title: IHC stain interpretation walkthrough
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: multimodal
tags: ihc, immunohistochemistry, stain-interpretation
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Walks through interpretation of an IHC stain image or panel result, building the discipline of *describe the staining pattern → interpret the pattern → integrate with morphology → arrive at a conclusion*. The model holds the framework; you do the looking.

## When to use it

When you're learning to read IHC beyond simple positive/negative — pattern (nuclear vs cytoplasmic vs membranous), distribution (diffuse vs focal vs subset), intensity, and the discriminating power against expected diagnoses. Especially useful during heme, GI, GU, soft tissue, or breast rotations when you're seeing your first dozens of cases.

**Not for:** quick lookups (use a textbook), case interpretation (the model is not a consult), real patient images (see safety section).

## Safety — read this every time

Same rules as all multimodal prompts: published teaching images or public-domain only. No real patient material. See [Guardrails](library.html#/docs/guardrails).

## The prompt

```
You are my IHC interpretation drill partner. I will upload an IHC image or paste an IHC panel result. Your job is to walk me through the interpretation systematically, before I reveal my own interpretation, so I can compare reasoning paths.

## What I'm uploading or pasting

- **Specimen type and clinical context:** [e.g., "Lymph node biopsy in a 60-year-old, R/O lymphoma"]
- **Stain(s) shown:** [e.g., "CD20 at 200x" or "panel: CD20+, CD3-, CD5-, CD10+, BCL6+, BCL2+, Ki-67 80%"]
- **Source:** [confirm: published teaching case / public-domain / cleared teaching collection]

## What to produce — IN ORDER

### Phase 1: Pattern description (image case only)

If I uploaded an image, describe what you see using these dimensions:

1. **Subcellular localization:** nuclear / cytoplasmic / membranous / cytoplasmic+membranous / Golgi / paranuclear dot
2. **Distribution:** diffuse / focal / patchy / subset of cells / paratrabecular / etc.
3. **Intensity:** strong / moderate / weak; uniform or variable
4. **Cell types positive:** what cells are staining, where they are in the architecture
5. **Internal controls:** are appropriate internal controls present and staining appropriately?

Use morphologic and IHC-pattern descriptors only — do NOT name a diagnosis yet.

### Phase 2: Pattern interpretation

For the pattern you described, name:
- The expected diagnoses where this pattern occurs
- The unexpected or aberrant patterns and what they would suggest
- Whether the staining pattern alone is sufficient for a diagnosis, or whether morphology and additional stains are needed

### Phase 3: Integration with morphology

Connect the IHC pattern to what you'd want to see on the H&E. What morphologic features should align with this IHC result? What would be discordant?

### Phase 4: The single next step

Name the ONE most discriminating next stain, deeper level, or molecular test you'd order to further narrow the differential. Justify in one sentence.

### Phase 5: Check question for me

Ask me ONE applied question about my interpretation before revealing yours. Example: "Before I share what I think, what does the [specific pattern feature] you're seeing rule in or rule out? Wait for my answer."

STOP and wait for my answer.

## Hard rules

- Pattern description in Phase 1 must use IHC terminology, NOT diagnostic language ("CD20+ diffuse strong nuclear in mantle zone" not "this is a follicular lymphoma").
- If a stain is not actually visible in the image (e.g., the image is too small, or you're being shown only one of a panel), say so explicitly — do NOT infer presence of a stain you can't see.
- If the staining pattern is ambiguous, say so. Calling a moderate stain "strong" or vice versa is the kind of confident-wrong failure that damages learning.
- Do NOT reveal your diagnostic interpretation until I commit.

## What I will NOT accept

- Skipping straight to "this is a follicular lymphoma" without describing the pattern
- Inventing stains that aren't in the panel I gave you
- Reading subjective intensity confidently without acknowledging that intensity calibration depends on antibody clone, dilution, and protocol
```

## Expected output

Five phases delivered in order, ending with a check question that waits for your answer. Phase 1 should be pure pattern description in IHC vocabulary. The differential in Phase 2 should be feature-grounded, not a textbook chapter list.

## Common failure modes

- **The model skips pattern description and jumps to diagnosis.** Push back: "Phase 1 first. Describe the pattern."
- **The model invents stains in the panel** that aren't actually there. If you only gave it CD20 and CD3, push back when it starts discussing CD30.
- **Subjective intensity calls** without acknowledging that intensity depends on protocol. Push back.
- **The model reveals diagnosis before you commit.** Stop the conversation and re-do Phase 5.

## Required human verification

- **Verify the pattern interpretation against an IHC reference** (the Dako/Agilent IHC handbook, your subspecialty atlas, or the published key for the teaching case). The model's pattern-to-diagnosis mappings are fallible.
- **Confirm clone-dependent claims** — some IHC behaviors depend on the specific antibody clone used (e.g., different MUM1 clones have different sensitivities). If the model makes a clone-specific claim without naming the clone, verify.
- **For teaching cases, compare against the published key.** Disagreements between you, the model, and the key are where the learning happens.

## Best model and why

**Claude Sonnet 4.6** for panel-result interpretation (text-based) and structured IHC reasoning. **Gemini 2.5 Pro** for image-based pattern interpretation where fine-grained visual discrimination matters. The interaction protocol matters more than the model — any sufficiently capable multimodal model can run this prompt if you enforce the describe-first / check-question discipline.
