---
title: Working with images — multimodal AI for pathology
last_updated: 2026-05-18
---

Pathology is a visual specialty. We work in photomicrographs, gross images, gel images, immunofluorescence patterns, electrophoresis traces, flow plots, gating diagrams. The current generation of AI tools can ingest images directly — you upload a JPG or PNG, the model "sees" it and responds in words.

This is genuinely useful for education. It is also more error-prone than text-only AI, more variable across models, and surrounded by ethical guardrails that most pathologists haven't fully thought through. This guide is the practical onboarding.

---

## Part 1 — The non-negotiable rule first

**Do not upload real patient material to any AI tool. Ever.**

Not photomicrographs from your sign-out. Not de-identified gross images. Not anonymized service material. Not screenshots from the LIS. Not the photo you took at the multi-headed scope last week. Not the image from your teaching file unless you can prove its provenance and consent status.

The risks compound:

- **De-identification is not a guarantee.** A rare entity + age + institutional context can re-identify a patient even with all overt identifiers stripped.
- **Vendor data policies vary and change.** What the vendor does with uploaded images today may not be what they do in six months.
- **Models may be retrained on uploads.** Even when a vendor says "no training on user data," the policy can be incomplete (e.g., "no training unless flagged for review," and your image gets flagged).
- **Institutional liability is real.** Even if no patient is identified, uploading institutional case material may violate your institution's data policies, your subspecialty society's policies, or applicable HIPAA business-associate constraints.

**Use published teaching material instead.** Pathology Outlines, the WHO classification image collections, AFIP/ASIP teaching sets, society teaching collections, atlas chapters from textbooks you own. These are designed for exactly this use; the consent and copyright questions are settled.

If you cannot demonstrate on demand that an image is consented and de-identified for AI use, do not upload it. The educational value is not worth the risk.

The rest of this guide assumes you're working with published or public-domain teaching cases.

---

## Part 2 — Technical quality of the upload

The model's interpretation is bounded by what it can actually see. A bad upload guarantees a bad response. Five rules for upload quality:

### 1. Resolution

Aim for at least 1024×1024 pixels. Below that, fine morphologic detail is lost in the upload itself before the model sees it. Above 2048×2048 is rarely useful — most models downsample to ~2K anyway.

For a photomicrograph: original full-resolution scope photo is ideal. A phone snap of a slide from the eyepiece is usable if the focus is reasonable. A blurry zoomed-in JPG from a textbook chapter is much worse than the same image at original publication resolution.

### 2. Crop

Crop tightly to the region of interest. If you ask "what's the diagnosis?" on a low-power tissue image with five distinct regions, the model has to guess which region matters. If you crop to the one region you want analyzed, the answer improves measurably.

If multiple regions matter, upload them as separate images with text labels: "Image 1: H&E ×40. Image 2: cytokeratin IHC ×40 of the same region. Image 3: ki-67 ×20."

### 3. Aspect ratio

Square or near-square crops are processed most cleanly. Very wide or very tall images can lose detail during the model's internal preprocessing. If you have a tall image, consider splitting it into two square crops.

### 4. Magnification labels

Models cannot reliably infer magnification from morphology alone. Always state the magnification in your text prompt: *"This is an H&E section at 200×."* Without this, the model will sometimes mis-interpret cells as smaller or larger than they actually are.

### 5. Stain identification

State the stain explicitly. "*This is an H&E*" or "*This is a Wright-Giemsa of a peripheral blood smear*" or "*This is a Congo red under polarized light*." Models can sometimes infer stain from color and morphology, but unreliably. Always provide.

---

## Part 3 — Context to add in the prompt

The image alone is not a prompt. What you wrap it in matters as much as the image.

Always include:

- **What the image is** (modality, stain, magnification, organ)
- **What level you're working at** (PGY-2 in heme, fellow in cyto, attending wanting a second look)
- **What you've already considered** (your differential so far, your favored interpretation)
- **What you want from the model** (interpret? confirm your read? generate a teaching point? ask me a question to drill my reasoning?)

Compare two prompts for the same image:

**Weak:**
> What is this?

**Strong:**
> This is an H&E section of bone marrow at ×400 from a published teaching case (Pathology Outlines, MGUS chapter). I'm a PGY-2 trying to develop my interpretive reflex for plasma cell morphology. Without telling me the diagnosis yet: ask me three specific morphologic features I should be commenting on, then wait for my answer before revealing the case.

The weak prompt invites a generic textbook-style answer. The strong prompt establishes a learning interaction and constrains the model to behave the way you'd want a senior colleague to behave.

---

## Part 4 — Which models for which image types

As of 2026, the field is still genuinely variable. Recommendations below should be re-checked quarterly; what's true today may not hold next quarter.

| Image type | Recommended first try | Backup / second opinion |
|---|---|---|
| H&E photomicrograph | GPT-4o or Claude Sonnet 4.6 | Try the other; cross-check matters |
| IHC photomicrograph | GPT-4o | Claude Sonnet 4.6 (improving fast) |
| Peripheral blood smear | Claude Sonnet 4.6 | GPT-4o |
| Bone marrow aspirate | GPT-4o | Claude Sonnet 4.6 |
| SPEP / IFE trace | Claude Sonnet 4.6 | GPT-4o |
| Flow cytometry plot | Claude Opus 4.7 | GPT-4o (challenging for both) |
| Karyotype | Claude Opus 4.7 | GPT-4o (challenging for both) |
| Electron microscopy | Try both; expect mediocre results |
| Gross photograph | GPT-4o | Claude Sonnet 4.6 |
| Gel image (Western, agarose) | GPT-4o | Claude Sonnet 4.6 |
| Radiograph or CT slice | GPT-4o | Specialized radiology models exist; out of scope here |

General pattern: GPT-4o has historically been the strongest at image-based pathology questions, with Claude Sonnet 4.6 closing the gap rapidly and sometimes better on calibrated educational framing. Both struggle with fine morphologic detail at high power and with subtle pattern recognition where humans rely on context the model can't access.

**Always cross-check with a different model when the answer matters.** Don't accept a single-model image read for a high-stakes question without a second opinion.

---

## Part 5 — The framing trap

The single most common mistake with multimodal AI in education is asking the wrong question shape.

**The trap:** *"Tell me what this is."*

This framing positions the model as oracle, you as recipient. You get a textbook-style answer that may or may not be right, and you've done none of the cognitive work that the case was supposed to teach you.

**The right framing:** *"I'm using this image to drill my interpretive reflex. Without telling me the diagnosis: ask me what I'm looking at, what features matter, what differential I should be considering."*

This framing positions the model as a tutor and you as the trainee doing the work. You get to attempt your own interpretation; the model checks your reasoning; you learn.

The difference is not subtle. Pathologists who use multimodal AI as oracle ("what is it?") get bored and stop because the answers feel hollow. Pathologists who use it as drill partner ("ask me what I see") build skill measurably faster.

See the [SPEP self-quiz worked example](library.html#/library/pillar-1-self-education/examples/spep-self-quiz) in the library for the right framing shape applied to a real case.

---

## Part 6 — Comparing outputs across models

When you ask the same image question to two different models, the comparison is itself informative.

**Three patterns to watch for:**

**1. Both models converge on the same answer.** Strong signal you're probably right (if you'd also concluded the same), or worth taking seriously (if their answer surprises you). Verify against the known answer of the published case.

**2. The models disagree.** Genuinely interesting. Sometimes one model has spotted a subtle feature the other missed; sometimes one is confabulating. The disagreement is a flag to slow down and look at the image more carefully yourself.

**3. Both models give different vague, hedged answers.** The image is at the edge of what current AI can interpret. Trust neither answer; treat the case as one where AI is not yet a reliable tutor.

The cost of running the same image past two models is one extra upload. The information gain is large. Do this routinely for any case that matters educationally.

---

## Part 7 — Multimodal limitations you must know

A short list of known weaknesses across current models. These will improve over time; check this list periodically.

- **Counting is unreliable.** "How many cells?" "How many mitoses per 10 HPF?" Models routinely miscount. Use the model for interpretation, not for quantification.
- **Spatial reasoning is weak.** "What's in the lower-right quadrant?" "Compare the upper region to the lower region." Models often confuse spatial relationships. Crop to one region at a time.
- **Subtle color discrimination is unreliable.** Faint blush of IHC positivity, subtle nuclear pleomorphism, mild dysplasia — all are at the edge of what models reliably distinguish. Don't rely on AI for "is this just barely positive or just barely negative" calls.
- **Out-of-distribution images fail silently.** Rare entities, unusual stains, lab-specific artifacts the model has never seen will produce confident-wrong answers with no signal that the model is out of its depth.
- **Multi-image comparison is poor.** "Compare image A to image B" is harder for current models than handling images independently. Better to ask one at a time and synthesize the results in your own head.

---

## Part 8 — Practical workflow for image-based study

A 30-minute multimodal study session, applied to a published photomicrograph series (e.g., the chapter on plasma cell neoplasms in your atlas):

1. Pick one teaching image from the chapter you've been meaning to study.
2. Crop tightly to the region of interest. Save at ≥1024 px.
3. In a fresh Claude or ChatGPT conversation, upload the image with this prompt:
   > This is an H&E photomicrograph at [magnification] from [source]. I'm a PGY-[X] trying to develop my interpretive reflex for [entity family]. Without telling me the diagnosis: ask me three specific morphologic features I should be commenting on. Wait for my answer.
4. Answer the questions the model asks you.
5. After your answer, ask: *"What did I get right? What did I miss? What features would I have needed to call to make the definitive diagnosis?"*
6. Reveal the actual answer to yourself (since you picked the case from a labeled atlas, you know it). Ask the model: *"The actual diagnosis is [X]. Did your line of questioning point me toward that, or away from it? What should I do differently next time?"*
7. Pick the next image. Repeat.

Six or seven images in 30 minutes. Each image generates a self-quiz, a critique of your reasoning, and a meta-reflection on your interpretive habits. This is dramatically more effective than passive review of the same chapter.

---

## Part 9 — A few things to NEVER do

- **Don't upload an image and ask "is this cancer?"** — both ethically and technically wrong. The model is not a diagnostic device.
- **Don't paste a screenshot of your sign-out screen.** EHR snippets identify institutions; the case may be patient-identifying even if "obvious" identifiers are out of frame.
- **Don't use AI image interpretation for any clinical decision on a real patient.** Education only.
- **Don't trust counts.** Use AI for interpretation, not quantification.
- **Don't cite the AI's image read in a manuscript or presentation.** Cite the published case + your own interpretation; the AI is a tutor, not a co-author.

---

## Part 10 — Where this is going

Multimodal pathology AI is improving fast. The capabilities described here are likely to be obsolete within 12–18 months — for the better. Cropping requirements will relax; quantification will improve; subtle interpretation will sharpen.

What will not change:

- The ethical constraints on patient material
- The verification discipline
- The framing trap (oracle vs tutor)
- The value of cross-model comparison

Build habits around those four and you'll stay competent through whatever the next generation of models brings.
