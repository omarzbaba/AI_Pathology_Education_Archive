#!/usr/bin/env python3
"""
Deep refinement of Pillar 1 prompts — batch 1.

Includes:
- 6 NEW Pillar 1 prompts created from scratch
- 5 existing Pillar 1 prompts re-written to exemplar depth

Run:
  python3 scripts/deep-refine-p1-batch1.py
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Helper: build a complete file (frontmatter + body)
# ---------------------------------------------------------------------------

def write_prompt(path, frontmatter, body):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fm = "---\n" + "\n".join(f"{k}: {v}" for k, v in frontmatter.items()) + "\n---\n\n"
    p.write_text(fm + body)

# ---------------------------------------------------------------------------
# NEW PROMPT 1: IHC stain interpretation walkthrough
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/ihc-stain-interpretation.md",
    {
        "title": "IHC stain interpretation walkthrough",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "advanced",
        "time_to_use": "2-10min",
        "visual": "multimodal",
        "tags": "ihc, immunohistochemistry, stain-interpretation",
        "verified_models": "TODO",
        "best_model": "Claude Sonnet 4.6",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

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
""",
)

# ---------------------------------------------------------------------------
# NEW PROMPT 2: Molecular result interpretation drill
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/molecular-result-interpretation.md",
    {
        "title": "Molecular result interpretation drill",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "advanced",
        "time_to_use": "2-10min",
        "visual": "text-only",
        "tags": "molecular, ngs, variant-interpretation, classification",
        "verified_models": "TODO",
        "best_model": "Claude Opus 4.7",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

Walks through interpretation of a molecular result (single variant, fusion, copy number alteration, MSI/TMB result, or NGS panel) by drilling the four-step reasoning framework: *what is the alteration → what is its functional significance → what is its clinical significance in this disease context → what is the appropriate report language*. The model is your structured thinking partner, not your variant database.

## When to use it

When you're learning to integrate molecular results into final reports, especially during a molecular pathology rotation or while preparing for boards. Also useful when you've seen a result you'd like to think through more carefully before sign-out.

**Not for:** real patient variant classification (use your institutional pipeline and the appropriate authoritative databases — ClinVar, COSMIC, OncoKB, etc.), settled questions (look those up), or as a substitute for genetic counseling.

## The prompt

```
You are my molecular pathology interpretation drill partner. I'm going to give you a molecular finding (or a panel). Walk me through interpretation using a strict four-step framework, before I commit my own interpretation.

## What I'm pasting

- **Disease context:** [e.g., "70-year-old with new diagnosis of MDS, planning treatment"]
- **The molecular result:** [paste — single variant in standardized nomenclature (HGVS), fusion description, CNV finding, MSI/TMB result, or full panel — DE-IDENTIFIED, no patient identifiers]
- **Test type:** [e.g., "myeloid NGS panel, 50 genes, somatic"]
- **What I'm trying to decide:** [e.g., "should this go in the report as actionable? as VUS? not reported?"]

**Provenance check:** Confirm this is a teaching/published case or sufficiently de-identified material. If anything looks identifiable (rare combination of variant + age + diagnosis), stop and tell me before proceeding.

## The four-step framework

### Step 1: What is the alteration?

Plain-language version of the molecular finding. Include:
- Gene name and what the protein does (one sentence)
- Type of alteration (missense, nonsense, frameshift, splice, fusion, CNV)
- Predicted functional consequence at the protein level

If specific functional data exists for this variant (loss-of-function, gain-of-function, dominant negative), name it — and source it: `[ClinVar 2024]`, `[COSMIC]`, `[functional study: Author 2022]`. If you don't have specific functional data, say so — do not invent.

### Step 2: What is its general functional significance?

Walk through what's known about this gene's role in disease:
- Pathway it sits in
- Other diseases or contexts where this gene is altered
- Typical mechanism (TSG vs oncogene; LOF vs GOF expected)

### Step 3: What is its significance IN THIS DISEASE CONTEXT?

This is the most important step and the one most easily collapsed into Step 2. Specifically:
- Is this gene recurrently altered in this disease?
- What does its presence/absence change about diagnosis, prognosis, or therapy?
- Is it a class-defining alteration (e.g., BCR::ABL1 in CML), an enriching alteration, an actionable alteration with therapeutic implications, a prognostic marker, or incidental?
- Are there published classification or treatment guidelines that incorporate this finding? Cite the version: `[NCCN AML v2.2024]`, `[ELN 2022]`, `[WHO HAEM5]`.

### Step 4: What's the appropriate report language?

Suggest 2-3 sentences that could go into the molecular section of the final report, calibrated to the institutional conventions you'd typically follow.

## Then ask me ONE check question

Before I commit my own interpretation, ask me: "Given the context [disease + intent], how would you classify this — pathogenic/likely pathogenic/VUS/benign — and what's the single piece of additional information that would change your answer?" Wait for me to respond before discussing further.

## Hard rules

- **Source classification claims** — guideline version, database version, year.
- **Do NOT invent published functional data.** If you don't have specific data on this variant, say "no specific functional data available; reasoning by inference from gene class."
- **Distinguish gene-level from variant-level claims.** "TP53 mutations are associated with poor prognosis in AML" is gene-level; whether a SPECIFIC variant is pathogenic requires variant-level evidence.
- **Acknowledge uncertainty.** VUS classifications exist for good reason; do not collapse them prematurely.
```

## Expected output

Four steps in order, each with sourced claims where applicable, ending with a check question for you. The Step 4 report language should be usable as a starting point, not a finished report.

## Common failure modes

- **Collapsing Step 3 into Step 2.** The model talks about the gene in general rather than its meaning in *this disease*. Push back: "What does this mean specifically in the context of [disease]?"
- **Fabricated functional data.** The model invents a "published functional study" that doesn't exist. Catch this in verification.
- **Over-confident classification.** Calling something pathogenic when the evidence supports VUS. Push back: "Walk me through the ACMG criteria that support that classification."
- **Outdated guideline references.** Molecular classification evolves fast — verify the cited version is current.

## Required human verification

- **Cross-check against your institutional variant interpretation pipeline.** This prompt is a thinking tool, not a classification authority.
- **Verify every cited database or guideline version.** ClinVar, OncoKB, COSMIC, WHO HAEM5, NCCN — confirm the version is current.
- **For any clinically actionable interpretation, double-check with the molecular director or genetic counselor at your institution.** This prompt does not replace clinical molecular review.

## Best model and why

**Claude Opus 4.7** — variant interpretation requires depth and discipline about evidence quality. Opus is more careful about the gene-level vs variant-level distinction and more honest about uncertainty. Sonnet 4.6 works but more easily falls into confident classifications without sufficient evidence. **Never trust any model alone for clinical molecular interpretation** — this is a teaching tool only.
""",
)

# ---------------------------------------------------------------------------
# NEW PROMPT 3: Differential by histologic pattern
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/differential-by-histologic-pattern.md",
    {
        "title": "Differential by histologic pattern",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "intermediate",
        "time_to_use": "2-10min",
        "visual": "text-only",
        "tags": "differential, morphology, pattern-recognition",
        "verified_models": "TODO",
        "best_model": "Claude Opus 4.7",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

You describe a histologic pattern (small round blue cells in a child, spindle cell tumor of the dermis, granulomatous inflammation in lung), and the model generates a complete pattern-based differential, ranked by likelihood given any context you provide, with discriminating features for each entity. This builds the pattern-to-DDx reflex that distinguishes experienced pathologists.

## When to use it

When you've seen a pattern you can describe but can't yet generate a complete differential for. Especially useful early in subspecialty rotations or while studying for boards — the pattern-DDx mapping is one of the most heavily tested cognitive skills.

**Not for:** lookups of textbook tables (more efficient to just look at the table), single-entity learning (use the concept explanation prompt), or initial encounter with morphology you can't yet describe (use the photomicrograph practice prompt first).

## The prompt

```
You are my pattern-to-differential drill partner. I'll describe a histologic pattern. You generate a complete, ranked differential — not just an enumeration, but with the specific discriminating features and the cognitive shortcuts I should remember.

## What I'm describing

- **The pattern (in morphologic terms):** [e.g., "monomorphic small round blue cells in nests with delicate fibrovascular stroma, in a 14-year-old's chest wall mass"]
- **Clinical context (if known):** [demographics, location, presentation, any prior imaging — de-identified or fictional]
- **My current best guess (if any):** [optional — including this calibrates the differential and helps you tell me what I might be missing]

## What to produce

### Section 1: The pattern-based differential

List **all entities I should consider** based on the pattern, organized as:

| Rank | Entity | Discriminating feature(s) | Confirmatory test |
|---|---|---|---|

Rank by likelihood given the context provided. Be comprehensive — include the unusual entities I might miss, not just the top 3.

### Section 2: The "must not miss" diagnoses

Even if low probability, name the entities that I MUST NOT MISS because the consequences of missing them are high (aggressive malignancy, treatable infection, etc.). Mark these explicitly.

### Section 3: Why the top of the differential is at the top

For the 2-3 highest-likelihood entities, explain in 1-2 sentences each *why* they're at the top given the context. What about the pattern + context shifts the priors?

### Section 4: The single most discriminating workup step

If I could do only ONE thing next — one stain, one molecular test, one additional level, one clinical question — what would it be? Justify.

### Section 5: Cognitive shortcuts

Name 2-3 mental shortcuts that distinguish experienced pathologists' approach to this pattern from textbook reasoning. These should be the kind of intuition that comes from seeing many cases (e.g., "in a peripheral lymph node with [pattern], always check for [feature] before signing out — it's the single most common reason this entity gets called wrong").

## Hard rules

- **Be comprehensive in the differential.** Missing entities is the failure mode I'm trying to address with this prompt.
- **Discriminating features must be specific.** "Architecture" is not a feature; "tumor cells in well-formed glands lined by columnar epithelium" is.
- **Source any specific cutoff or criterion** — WHO edition, classification scheme, named criterion.
- **Do NOT rank entities by pure prevalence.** Pretest probability matters: adjust for the demographic and location context I gave you.

## What I will NOT accept

- A differential of 3 entities when 8 are reasonable
- Vague discriminating features
- A "must not miss" section that's just a restatement of the top of the differential
- Cognitive shortcuts that are obvious or platitudinous
```

## Expected output

A complete pattern-based DDx table, a must-not-miss list, ranked rationale for the top entities, a single discriminating next step, and 2-3 expert-level cognitive shortcuts.

## Common failure modes

- **Differential too narrow.** Push back: "What am I missing? Generate the full list including unusual entities."
- **Discriminating features are vague.** Push back: "What specifically about [feature] discriminates [entity A] from [entity B]?"
- **Pretest probability ignored.** Push back if a high-base-rate entity is buried below an exotic one without justification.
- **Shortcuts are platitudes.** Push back: "Give me shortcuts that someone who has signed out hundreds of these would know."

## Required human verification

- **Verify the differential against a subspecialty reference** (the relevant WHO blue book, your subspecialty atlas, or a recent review). Models can miss entities, especially less common ones.
- **Pressure-test the cognitive shortcuts** with an attending or fellow in the subspecialty. The shortcuts that survive expert scrutiny are the ones worth internalizing.
- **For any specific cutoff cited,** verify against the source.

## Best model and why

**Claude Opus 4.7** — generating a comprehensive, ranked differential with discriminating features rewards depth. Opus produces more complete lists and more specific features than Sonnet. Use Sonnet for quick pattern-DDx review when comprehensiveness is less critical.
""",
)

# ---------------------------------------------------------------------------
# NEW PROMPT 4: Critical value workflow drill
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/critical-value-workflow.md",
    {
        "title": "Critical value workflow drill",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "intermediate",
        "time_to_use": "2-10min",
        "visual": "text-only",
        "tags": "critical-values, lab-workflow, cp, notification",
        "verified_models": "TODO",
        "best_model": "Claude Sonnet 4.6",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

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
""",
)

# ---------------------------------------------------------------------------
# NEW PROMPT 5: Blood smear systematic review
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/blood-smear-systematic-review.md",
    {
        "title": "Blood smear systematic review walkthrough",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "intermediate",
        "time_to_use": "2-10min",
        "visual": "multimodal",
        "tags": "blood-smear, hematology, systematic-review, multimodal",
        "verified_models": "TODO",
        "best_model": "Claude Sonnet 4.6",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

Builds the habit of reading a peripheral blood smear systematically — RBCs, WBCs, platelets, in that order, with specific observations at each magnification — rather than pattern-matching to the most likely diagnosis. This discipline distinguishes pathologists who catch the second finding from those who anchor on the first.

## When to use it

During your first weeks of clinical hematology or when you're trying to break the habit of going straight to "what is this" rather than "what do I see." Pairs well with a teaching atlas of smears.

**Not for:** real patient smears (use your scope), settled diagnoses (look those up), or quick pattern matching when speed matters (different drill).

## Safety

Published teaching images or public-domain only. No real patient smears. See [Guardrails](library.html#/docs/guardrails).

## The prompt

```
You are my blood smear reading discipline coach. I'll upload a peripheral blood smear image (teaching case, confirmed). Walk me through the systematic review I should perform every single time.

## What I'm uploading

- **Stain and magnification:** [e.g., "Wright-Giemsa at 1000x oil immersion"]
- **Clinical context (if known):** [optional — including this changes the discipline test]
- **Source:** [confirm: teaching atlas / public domain / cleared collection]

## The systematic review you'll walk through

### Pass 1: Low power (10-20x)

Before any cellular detail, describe:
- Smear quality (well-spread vs thick/thin, monolayer adequacy, distribution)
- General cellularity (hypo/normo/hypercellular vs the white count)
- Distribution patterns (clumping, rouleaux, agglutination)
- Anything immediately unusual at low power (large cell aggregates, parasites, schistocytes obvious at low power)

### Pass 2: RBC review (40-100x)

In ORDER, comment on:
- **Size** (anisocytosis, micro vs macro vs normocytic; compare to small lymphocyte nucleus)
- **Shape** (poikilocytosis: sickle, target, spherocytes, schistocytes, teardrops, burr cells, acanthocytes, ovalocytes, stomatocytes)
- **Color** (hypochromasia, polychromasia)
- **Inclusions** (Howell-Jolly, basophilic stippling, Pappenheimer, Heinz, Cabot rings, parasites)
- **Distribution** (rouleaux, agglutination, autoagglutination)

### Pass 3: WBC review (100x oil)

In ORDER:
- **Estimated count vs reported count** (rough estimate × 1500 per HPF for 100x oil)
- **Differential** (neutrophils, bands, lymphs, monos, eos, basos)
- **Neutrophil abnormalities** (hypogranulation, hypersegmentation, toxic changes, Döhle bodies, Auer rods, dysplastic features)
- **Lymphocyte abnormalities** (reactive vs atypical lymphs, blasts, hairy cells, Sézary cells, smudge cells)
- **Monocytes** (atypical, dysplastic)
- **Blasts** (count per area, morphology if present)

### Pass 4: Platelet review (100x oil)

- **Estimated count** (per HPF × 15-20K for 100x oil; flag if discordant with reported count)
- **Size** (giant platelets, normal size variation)
- **Clumping** (genuine vs EDTA-induced)
- **Morphology** (granulation, fragmented platelets)

### Pass 5: Anything I should NOT miss

Even if low probability, what should I make sure I looked for given the context provided? Examples: parasites in fever of unknown origin, schistocytes in suspected TTP, blasts in cytopenia.

### Then ask me ONE check question

Before revealing your impression, ask me about ONE specific observation from one of the passes. Wait for my answer.

## Hard rules

- **Walk through every pass, in order.** Don't skip Pass 1 because it seems too basic — that's where smear quality issues that confound everything else are caught.
- **Estimated counts must be physiologic.** A patient with reported WBC of 100K should have proportionally more cells per HPF; if the smear doesn't match, name the discrepancy.
- **Do NOT skip to a diagnosis until I commit.**
- **If a finding is borderline or ambiguous, say so.** Do not commit to "schistocytes present" if you're seeing 1-2 per HPF that are equivocal.
```

## Expected output

Five passes in order with specific observations at each, then a check question waiting for your answer. The five-pass structure is the entire point — repeating it builds the reflex.

## Common failure modes

- **Skipping the low-power pass.** This is where smear quality issues hide. Push back if Pass 1 is perfunctory.
- **Confident overcalls** of subtle findings. Schistocytes are over-called constantly; the model should reflect that calibration.
- **Estimated counts disconnected from the reported CBC.** Push back when math doesn't add up.
- **Premature diagnostic commitment.** Same fix as the other multimodal prompts.

## Required human verification

- **Compare against the published key** for the teaching case. The five passes are the discipline; the specific findings are where you check the model.
- **For schistocytes, blasts, parasites, or other high-stakes findings the model identifies,** verify against the published key — these are the findings where AI false-positives can mislead.

## Best model and why

**Claude Sonnet 4.6** for the systematic structure and most multimodal pattern recognition. **Gemini 2.5 Pro** if you want maximum fine-detail visual analysis. The discipline of the five passes matters more than model choice.
""",
)

# ---------------------------------------------------------------------------
# NEW PROMPT 6: Frozen section thinking-out-loud drill
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/frozen-section-thinking-aloud.md",
    {
        "title": "Frozen section thinking-out-loud drill",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "advanced",
        "time_to_use": "2-10min",
        "visual": "text-only",
        "tags": "frozen-section, time-pressure, decision-making",
        "verified_models": "TODO",
        "best_model": "Claude Opus 4.7",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

Simulates frozen section decision-making under time pressure, including the meta-cognitive challenge: what to say to the surgeon when you're uncertain, when to defer to permanent, and how to communicate the implications of each option. The drill is your reasoning under cognitive load, not pattern-matching the answer.

## When to use it

During AP rotations where you'll be doing frozens, or as a board-prep exercise. Pairs well with cases from a frozen section atlas.

**Not for:** real frozens (use your scope and your attending), pattern lookup (different drill), or initial encounter with a tumor type (read about it first).

## The prompt

```
You are simulating a frozen section consult with me. The setup: I am the pathologist on call, you are the surgeon in the OR. I will describe what I see; you will play the surgeon and ask the questions a real surgeon would ask. Then you'll critique my responses, framing what I did well and what I missed.

## The case

- **Specimen type and procedure context:** [e.g., "intraoperative consultation, breast lump, planned partial mastectomy, surgeon wants to know if margins are clear and if there's invasion"]
- **What I see grossly:** [my description]
- **What I see on the frozen slide:** [my description, including any concerning features]
- **My current interpretation:** [my draft answer]

## Your role

### As the surgeon (Phase 1)

Respond as the surgeon would — asking the question that drives the next surgical decision, not a textbook question. Real frozen-section conversations sound like:

- "Is it cancer?"
- "Is the margin clear?"
- "Should I take more?"
- "Can I close, or am I waiting for permanent?"
- "What's your level of confidence?"
- "What does this mean for the lymph nodes?"

Ask ONE question at a time. Wait for my answer. Then ask the next.

After 3-5 surgeon questions, switch to Phase 2.

### As the consultant pathologist coach (Phase 2)

Critique my responses to the surgeon, framed around three dimensions:

1. **Accuracy.** Was my interpretation defensible given what I described seeing? Where might I have been wrong, and what should I have looked at more carefully?
2. **Communication.** Did I express uncertainty appropriately when it was present? Did I avoid hedging when I shouldn't have? Did I give the surgeon what they needed to make their next decision?
3. **Defer-to-permanent calibration.** When SHOULD I have deferred? When was deferring the wrong call? What's the rule of thumb for this scenario?

End with: the single most important thing I should do differently next time, and why.

## Hard rules

- **The surgeon questions must be realistic.** No textbook framings. Real surgeons want decisions, not differentials.
- **The critique must be honest.** If I over-committed when I should have deferred, say so. If I deferred when I should have committed, also say so. Sycophantic critique is useless.
- **Acknowledge the time pressure.** A frozen-section answer at 3 am in the OR is not the same as a sign-out the next morning. The model must reflect this.

## What I will NOT accept

- Surgeon questions that no surgeon would actually ask
- Critique that's all positive or all negative
- A "defer to permanent" recommendation in every case (real practice has a more nuanced calibration)
```

## Expected output

A short dialogue (3-5 surgeon Q&A exchanges) then a structured critique across accuracy / communication / deferral calibration, ending with a single most-important takeaway.

## Common failure modes

- **Textbook-y surgeon questions** that don't reflect real OR conversations. Push back: "A surgeon wouldn't ask that mid-case. Ask the question they'd actually ask."
- **Sycophantic critique** ("great job, just keep doing what you're doing"). Push back: "Be more critical — name a specific gap."
- **Always-defer recommendation.** Push back: "When SHOULD I commit on frozen? Give me the rule of thumb."

## Required human verification

- **Discuss the simulation with your attending after.** Real frozen-section calibration is institution-specific and attending-specific; the model's defaults may differ from how your service operates.
- **For the specific morphology described, verify against your subspecialty atlas** — frozen artifact can mimic features that aren't really there, and the inverse.
- **Practice the spoken communication aloud.** Frozen-section communication is verbal; reading is not the same as speaking under time pressure.

## Best model and why

**Claude Opus 4.7** — the simulation requires both clinical reasoning depth and convincing surgeon role-play. Opus pulls away from Sonnet on multi-role simulations. The critique phase also benefits from Opus's willingness to be specific rather than hedging.
""",
)

# ---------------------------------------------------------------------------
# REFINED EXISTING PROMPT: MCQ generation with rationales
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/mcq-generation-with-rationales.md",
    {
        "title": "MCQ generation with rationales",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "intermediate",
        "time_to_use": "2-10min",
        "visual": "text-only",
        "tags": "mcq, board-prep, question-writing",
        "verified_models": "TODO",
        "best_model": "Claude Opus 4.7",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

Generates board-style MCQs with detailed rationales for **every** answer choice — not just the correct one. The rationales for incorrect choices are the highest-yield learning, because they teach the cognitive moves that distinguish strong test-takers from weak ones.

The prompt is designed to produce questions that test *application and analysis*, not memorization, and that have *plausible* distractors rather than throwaways.

## When to use it

After studying a topic, to actively retrieve and stress-test what you've learned. Also useful for building a personal review bank organized by topic. Best with the [Question bank gap analysis](library.html#/library/pillar-1-self-education/prompts/question-bank-gap-analysis) prompt — generate questions on your weak topics, then track which ones you miss.

**Not for:** replacing a real qbank for board prep (real qbanks have psychometric validation; AI-generated questions don't), questions for formal assessment (use validated items), or topics where you don't yet have foundational knowledge (read first, then drill).

## The prompt

```
You are a board-style MCQ writer for pathology residents. Generate questions that test reasoning, not retrieval. The rationales for incorrect answers are the highest-yield part of your output — write them like a teacher explaining the cognitive trap each distractor represents.

## What I'm requesting

- **Topic:** [be specific — e.g., "interpretation of the indirect antiglobulin test (IAT) in blood bank crossmatch", not just "blood bank"]
- **Number of questions:** [e.g., 5]
- **Target level:** [e.g., "PGY-2 in their first month of blood bank", or "RISE exam", "AP/CP boards", "ABPath in-service"]
- **Question style:** [e.g., "USMLE-style clinical vignette" or "compressed stem with lab values only"]

## Format for each question

```
Question N:
[Vignette of 2-5 sentences — clinical or laboratory context, ending in a clear question]

A. [Choice]
B. [Choice]
C. [Choice]
D. [Choice]
E. [Choice]

---

ANSWER: [Letter]

RATIONALE FOR EACH CHOICE:

A. [Why this is correct OR what specific misunderstanding makes a resident pick this incorrectly. Be specific about the cognitive error.]
B. [Same.]
C. [Same.]
D. [Same.]
E. [Same.]

TEACHING POINT (1-2 sentences): The single most important concept this question tests.
```

## Hard rules

- **Vignettes must include enough clinical context to reason from.** A bare question is not a board-style MCQ.
- **Distractors must be plausible to someone with partial knowledge.** "Obviously wrong" distractors are throwaways. Each distractor should represent a specific cognitive error a real resident would make.
- **Distractor rationales must be SUBSTANTIVE.** "This is incorrect because A is correct" is not a rationale. Say WHAT misunderstanding leads to picking that answer.
- **Calibrate to the stated level.** PGY-2 questions should not require fellowship-level knowledge; board questions should not be trivially easy.
- **DO NOT reproduce or closely paraphrase real published board questions.** If the topic is so narrow that you can't generate original questions safely, tell me — do not invent.
- **One unambiguous best answer.** If two answers could be defensible, the question is broken.

## What I will NOT accept

- Distractors that are clearly wrong on inspection
- "This is incorrect because the correct answer is A" non-rationales
- Vignettes that are decorative (clinical context that doesn't actually inform the question)
- Questions where the correct answer is in the longest choice (a classic test-writing tell)
- Questions that test memorization of a single fact dressed up as a vignette
```

## Expected output

The requested number of questions in the format above, each with five plausible answer choices, full per-choice rationales, and a one-line teaching point. Total length scales with number of questions — usually ~250-350 words per question.

## Common failure modes

- **Obvious throwaway distractors.** Push back: "Distractor C is obviously wrong. Replace it with something that represents an actual misconception."
- **Pseudo-rationales.** Push back: "Your rationale for choice B doesn't say WHY someone would pick it. Explain the cognitive error."
- **Application questions that actually test recall.** Push back: "Could a resident who memorized facts answer this without reasoning? If yes, it's not application."
- **Vignettes that don't add value.** Push back: "Strip the vignette — does the question still make sense? If yes, your vignette is decorative."

## Required human verification

- **Verify the correct answer against an authoritative source** every single time. AI-generated MCQs frequently have plausible-looking-but-wrong correct answers, especially for nuanced topics. The rationales sound convincing for both the right and the wrong answer, which is the failure mode that matters most.
- **Verify the distractor rationales.** A confidently-wrong distractor rationale teaches the wrong concept.
- **For any specific value cited** (cutoff, threshold, dose), verify against current guideline.
- **Show one question to a colleague who knows the topic** — if they spot a flaw you missed, the question needs more work.

## Best model and why

**Claude Opus 4.7** — generating plausible distractors and substantive wrong-answer rationales is where Opus materially outperforms Sonnet. Sonnet rationales tend toward formulaic; Opus produces rationales that read like a teacher explaining the trap. For high-stakes use (formal assessment, board prep banks), use Opus. For quick review questions during a study session, Sonnet is sufficient.
""",
)

# ---------------------------------------------------------------------------
# REFINED EXISTING PROMPT: Reverse case drill
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/reverse-case-drill.md",
    {
        "title": "Reverse case drill — findings to diagnosis",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "advanced",
        "time_to_use": "2-10min",
        "visual": "text-only",
        "tags": "case-based, drilling, reasoning",
        "verified_models": "TODO",
        "best_model": "Claude Opus 4.7",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

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
""",
)

# ---------------------------------------------------------------------------
# REFINED EXISTING PROMPT: Paper summarization
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/paper-summarization.md",
    {
        "title": "Paper summarization",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "quick-win",
        "time_to_use": "<2min",
        "visual": "text-only",
        "tags": "literature, summarization, triage",
        "verified_models": "TODO",
        "best_model": "Gemini 2.5 Pro",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

Generates a structured paper summary covering question / design / headline finding / most important limitation / would-this-change-practice / attending Q&A prep — in that order, no skipping. The output is a triage tool: read the full paper, scan it, or skip it.

The dominant failure mode is **summarizing from the title and abstract alone** when the model doesn't actually have the paper. This prompt makes that failure mode hard to commit by requiring an explicit honesty check at the top.

## When to use it

When a paper lands in your inbox or shows up in a journal club packet and you have 10 minutes to decide whether to read it. Also useful as the *first* step before journal club presentation: generate the summary, identify what you can't answer, then go read those specific sections of the paper.

**Not for:** in-depth methodology critique (use the [Paper methods critique](library.html#/library/pillar-1-self-education/prompts/paper-methods-critique) prompt), generating discussion questions (use the [Journal club discussion questions](library.html#/library/pillar-2-teaching/prompts/journal-club-discussion-q) prompt), or as a substitute for actually reading the paper before citing it.

## The prompt

```
You are summarizing a paper for me. Before you produce anything, you must honestly answer a question about what you actually have access to.

## Honesty check — answer first

Do you have access to the full text of this paper, or only the title and abstract (or only the title)? Say so explicitly. If you only have the title or abstract, STOP and tell me — do not summarize. A hallucinated summary is more damaging than no summary.

If I've attached a PDF or pasted the full text, confirm you can read it. If I've given you only a citation, ask whether I want you to proceed with title/abstract only or to wait for me to provide the text.

## What I'm requesting

- **Paper:** [DOI, citation, attached PDF, or pasted full text]
- **My background on this topic:** [e.g., "PGY-3, this is for journal club next week; I've read the related guideline but not other papers in this area"]
- **My time budget:** [e.g., "I have 10 minutes; will read more only if your summary makes the case"]

## The six-part summary (in this order, no skipping)

### 1. The question (1 sentence)

What gap in the literature does this paper address? Not "what did they study" — what was the open question this paper was designed to answer?

### 2. The design (2-3 sentences)

Study type, population, comparison or control, key methods. Be specific enough that I could critique the design without reading the paper. Name the study type with the standard terminology (RCT, retrospective cohort, prospective cohort, case-control, diagnostic accuracy, systematic review, meta-analysis, prediction model, etc.).

### 3. The headline finding (1-2 sentences)

The main result. Include the effect size and statistical precision (95% CI or p-value), not just direction. If the result is a difference, give absolute numbers — not just relative risk reduction.

### 4. The most important limitation (1-2 sentences)

The single limitation that most constrains the generalizability or interpretation of the finding. Not a list of limitations — the most important one. Be specific about HOW it constrains interpretation, not just that it exists.

### 5. Would this change practice? (1-2 sentences)

A specific answer:
- **Yes, in [specific setting]:** [what changes and for which patients]
- **No, because:** [the specific gap that would need to be filled first]
- **Not yet, but if [X] confirms:** [what would tip it over]

Avoid "more research is needed" — that's true of everything.

### 6. Three questions I should be prepared to answer

If my attending asks me about this paper, what are the three questions most likely to come up? For each, give me 1-2 sentences of prepared answer.

## Hard rules

- **The honesty check is non-negotiable.** Do not summarize a paper you don't have.
- **Effect sizes must be specific.** "Significant reduction" is not enough; give the number.
- **The limitation must be the MOST important one, not the easiest to name.** Small sample size is easy to name and often not the most important.
- **The "would this change practice" answer must commit.** "It might, depending on circumstances" is a non-answer.
- **The three attending questions must be specific to THIS paper, not generic.** "What were the limitations?" is generic. "Why did the authors choose a 30-day mortality endpoint when the disease usually progresses over years?" is specific.

## What I will NOT accept

- A summary built from the title or abstract alone, dressed up as if you read the full paper
- Vague effect sizes ("significant")
- A list of limitations instead of the most important one
- Generic attending questions
- Citation that doesn't exactly match the paper (verify before producing the summary)
```

## Expected output

The six-part summary in the order above. Total length scales with the paper's substance — usually 300-450 words. Should be readable in 90 seconds.

## Common failure modes

- **Summary fabricated from the title.** This is the dominant failure mode and the most damaging. The honesty check at the top is designed to make this hard to commit; verify the model actually has the paper before trusting the summary.
- **Effect sizes given as direction only ("improved", "reduced") without numbers.** Push back for the number.
- **"More research is needed" non-answers in Step 5.** Push for a commit.
- **Generic limitation** like "small sample size" when N is 5,000. Push for the specific constraint.

## Required human verification

- **Verify the headline finding** against the actual paper. The model frequently misremembers numbers from papers it has "seen."
- **Verify the limitation is real and is actually the most important one.** A junior reviewer would catch obvious limitations; the model's value is in surfacing the subtle one, but it's also where the model is most likely to be wrong.
- **Verify the three attending questions are answerable** from the paper before relying on them in journal club.
- **If the honesty check answer is "I only have the abstract", DISCARD the summary entirely and provide the paper text.**

## Best model and why

**Gemini 2.5 Pro** with the PDF attached — best long-context handling of full-text PDFs as of mid-2026, which is the entire ball game for paper summarization. **Claude Opus 4.7** with PDF attached is a comparable alternative. Without the paper text, every model fabricates — model choice doesn't save you. Always confirm the model has the text before trusting the summary.
""",
)

# ---------------------------------------------------------------------------
# REFINED EXISTING PROMPT: Paper methods critique
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/paper-methods-critique.md",
    {
        "title": "Paper methods critique",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "advanced",
        "time_to_use": "2-10min",
        "visual": "text-only",
        "tags": "literature, critical-appraisal, methods",
        "verified_models": "TODO",
        "best_model": "Claude Opus 4.7",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

Generates a structured methodology critique using the appropriate reporting guideline as the framework (CONSORT for RCTs, STROBE for observational, STARD for diagnostic accuracy, PRISMA for systematic reviews, TRIPOD for prediction models). The output is checklist-style and item-by-item, not impressionistic — which is exactly what reviewers and journal club discussants need.

## When to use it

Preparing for journal club presentation, peer-reviewing a manuscript, writing a critical letter, or studying critical appraisal skills. The structured framework forces engagement with the *design* choices rather than the *result*.

**Not for:** paper summarization (use the dedicated prompt), questions about clinical significance (separate skill), or analyzing your own work without a colleague's review (the model isn't an independent reviewer).

## The prompt

```
You are critiquing the methods section of a paper, item-by-item against the appropriate reporting guideline. Be specific, be honest, and source your critique points to the actual paper text. A vague critique that could apply to any paper is useless.

## Honesty check first

Do you have access to the full methods section of this paper? Confirm explicitly. If you don't have the methods section (or only have the abstract), STOP and tell me — do not critique what you cannot read.

## What I'm requesting

- **Paper:** [DOI, citation, attached PDF, or pasted methods section]
- **Study type:** [one of: RCT, retrospective cohort, prospective cohort, case-control, diagnostic accuracy, systematic review, meta-analysis, prediction model, qualitative study, other (name it)]
- **Reporting guideline framework I want you to use:**
  - RCT → CONSORT 2010 (+ relevant extensions)
  - Observational study → STROBE
  - Diagnostic accuracy → STARD 2015
  - Systematic review/meta-analysis → PRISMA 2020
  - Prediction model → TRIPOD 2024
  - Qualitative → COREQ or SRQR
  - Other → [name the guideline you want me to use]
- **My critique purpose:** [journal club presentation / peer review / personal study / writing a letter]

## What to produce — item-by-item

### Part 1: The checklist

For each major reporting guideline item, mark:
- **Adequate** — the paper addresses this item clearly and completely
- **Partial** — the paper addresses it but with gaps
- **Not addressed** — the paper is silent on this item
- **Not applicable** — the item doesn't apply to this study design (justify)

For each item, quote or paraphrase the relevant text from the paper where applicable. If the paper doesn't address an item, say what would have been needed.

### Part 2: The three most consequential gaps

Beyond the checklist, identify the **3 gaps a peer reviewer would flag**. For each:
- What the gap is
- Why it matters (how it constrains the paper's interpretability)
- What the authors should have done

### Part 3: The single most constraining design choice

Of all the design choices the authors made, identify the ONE that most constrains the paper's interpretability. This is different from "the most criticizable" — it's the choice that, if it had been different, would most have improved the paper. Suggest the specific alternative.

### Part 4: What the authors got right

Critique should not be uniformly negative. Identify 1-2 design choices the authors made that demonstrate methodological care or thoughtfulness. Specific, not generic.

### Part 5: Calibration disclosure

Acknowledge any uncertainty about whether the guideline version you used is current. Reporting guidelines update; if you're not sure whether you're using the latest version (e.g., CONSORT 2025 if released), say so explicitly so I can verify against the current source.

## Hard rules

- **Critique must be specific.** "Sample size could be larger" is not a critique. "Sample size of 47 yields 0.6 power to detect the pre-specified effect size, which the authors do not address" is.
- **Quote or paraphrase from the actual paper** rather than imagining what the methods might have said.
- **Do not invent guideline items.** If you're not sure what the current CONSORT items are, say so.
- **The constraining design choice in Part 3 must be feasible to have done differently.** "They should have done an RCT" is not a useful critique if the topic doesn't permit one.
- **Do not pad with peripheral critique** if the methods are largely sound. A paper with strong methods deserves a critique that says so.

## What I will NOT accept

- Vague critique that could apply to any paper
- Critique fabricated for a paper you don't actually have
- "More research is needed" as a critique
- Critique that ignores Part 4 (what they got right)
```

## Expected output

A checklist with adequacy ratings + the three consequential gaps + the most constraining design choice with alternative + 1-2 strengths + a calibration note about the guideline version. Length: 500-800 words for a typical paper.

## Common failure modes

- **Generic critique** that could apply to any paper. Push back: "Be more specific. What specifically in this paper's methods?"
- **Critique fabricated for a paper the model doesn't have.** The honesty check at top is designed to prevent this, but verify before trusting.
- **Guideline version uncertainty hidden.** If the model isn't sure whether it's using CONSORT 2010 or 2025, push for explicit acknowledgment.
- **All-negative critique** that ignores what the authors did well. Push for Part 4.

## Required human verification

- **Verify the critique against the actual methods section.** Quotes the model attributes to the paper need to be checked.
- **Verify the reporting guideline version is current.** Guidelines update; the model may reference an older version.
- **For a critique you'll present publicly** (journal club, peer review, letter), have a methodologist colleague pressure-test the critique before relying on it. There's no substitute for human review on methodologic critique.

## Best model and why

**Claude Opus 4.7** — methods critique requires applying named reporting guidelines with precision and resisting the temptation to be vaguely negative. Opus is materially more disciplined about specificity and about acknowledging what's done well. **Avoid Sonnet** for high-stakes critique (peer review, public presentation) — it produces critique that sounds plausible but is often generic.
""",
)

# ---------------------------------------------------------------------------
# REFINED EXISTING PROMPT: Self-quiz one at a time
# ---------------------------------------------------------------------------

write_prompt(
    "library/pillar-1-self-education/prompts/self-quiz-one-at-a-time.md",
    {
        "title": "Self-quiz one at a time",
        "pillar": "self-education",
        "event_type": "n/a",
        "audience": "resident",
        "difficulty": "quick-win",
        "time_to_use": "2-10min",
        "visual": "text-only",
        "tags": "self-assessment, drilling, interactive",
        "verified_models": "TODO",
        "best_model": "Claude Sonnet 4.6",
        "last_updated": "2026-05-17",
    },
    """## What this prompt does

Drills you with one question at a time, with the model adapting the next question based on what you got wrong. The *interaction structure* matters as much as the content — the rhythm of one-question-then-pause is what makes this work for active retrieval rather than passive reading.

## When to use it

When you have 10-30 minutes and want to rehearse rather than read. Especially effective:
- The week before an exam
- After a study block when you want to test retention
- During a rotation when you want to check your day's learning before sign-out tomorrow
- As a chained prompt after [Concept explanation at level](library.html#/library/pillar-1-self-education/prompts/concept-explanation-at-level) — the model already knows your level from that conversation

**Not for:** structured board prep (use real qbanks with psychometric validation), formal assessment, or when you don't have the focus to engage actively.

## The prompt

```
You are my quiz drill partner. The interaction structure is the entire point — one question at a time, with adaptive difficulty. Read all the rules before you start.

## My context

- **PGY level / role:** [e.g., PGY-3]
- **Topic:** [be specific — e.g., "interpretation of the indirect antiglobulin test (IAT) in blood bank crossmatch", not just "blood bank"]
- **How I want to use this:** [e.g., "I have 15 minutes, I want to test my retention", "I'm preparing for sign-out tomorrow", "I want to find my gaps"]

## Strict interaction rules

1. **Ask ONE question at a time.** Wait for my answer. Do not list multiple questions.
2. **After each answer, respond with:**
   - "Correct" / "Wrong" / "Partially correct" — call it explicitly
   - If wrong or partial: name the SPECIFIC concept I missed in one sentence, then give the right answer briefly
   - If right: a one-sentence confirmation, no lecture
3. **Adapt difficulty based on my answer:**
   - Got it cold → next question is harder, or shifts to a related concept
   - Struggled → next question is easier and targets the gap I just demonstrated
   - Genuinely wrong (not just imprecise) → next question loops back to the underlying concept
4. **After 5 questions, give me a synthesis paragraph:**
   - My strongest area (specific)
   - My biggest gap (specific)
   - One thing to read or drill next
5. **Do NOT lecture between questions.** Keep the rhythm tight. Brief responses, then the next question.

## Question quality bar

- **Mix question types.** Some recall, some application, some interpretation. Not all clinical vignettes; not all bare facts.
- **Specific enough to be assessable.** "Explain X" is not a question; "What's the specific finding that distinguishes X from Y?" is.
- **Connect to my level.** Don't ask PGY-1 questions of a PGY-3 or vice versa.

## Start now

Begin with a calibration question — something that helps you figure out where my level actually sits on this topic before you start drilling. Don't tell me it's a calibration question; just ask.

## If I correct you

If during the drill I correct you on a fact, STOP and acknowledge the correction explicitly. Do not continue as if it didn't happen. Update your model of the topic before the next question.
```

## Expected output

A back-and-forth conversation: model asks one question → you answer → model responds with calibration + next question → repeat. After 5 questions, a synthesis paragraph naming your strongest area, biggest gap, and next step.

The synthesis is the highest-value part — many residents skip it. The model should produce it without being asked.

## Common failure modes

- **Model dumps multiple questions at once.** Push back hard: "One at a time. Wait for my answer before the next."
- **Model lectures between questions.** Push back: "Less explanation, more questions. Keep the rhythm."
- **Model marks you "partially correct" when you're actually wrong** — builds false confidence. If you're not sure of your answer and the model is generous, ask: "Was that actually right? Be honest."
- **Synthesis at the end is generic** ("keep studying!"). Push back: "Be specific. What's my actual gap and what should I read tonight?"
- **Model fails to adapt** — keeps asking same-level questions regardless of how you're doing. Push back: "Adjust difficulty based on how I'm doing."

## Required human verification

- **The model's feedback on whether you got a question right is itself fallible.** If a "correct" answer surprises you, verify against an authoritative source before incorporating into your mental model.
- **The model can be generous about partial credit.** If your answer was vague or you guessed, downgrade the model's assessment to "wrong" yourself and add it to your gap list.
- **The synthesis is a hypothesis, not a verdict.** Your actual gap might be different from the one the model identified after only 5 questions.

## Best model and why

**Claude Sonnet 4.6** — interactive pacing and adaptive difficulty are well within Sonnet's range, and the back-and-forth conversational flow benefits from Sonnet's response speed. **Opus is overkill** for this prompt; the interaction structure matters more than reasoning depth. **Haiku** can work for quick recall drills but tends to lecture between questions.
""",
)

# ---------------------------------------------------------------------------
# Done — print summary
# ---------------------------------------------------------------------------

print("Wrote/updated 11 Pillar 1 prompts:")
print("  6 new: ihc-stain-interpretation, molecular-result-interpretation,")
print("         differential-by-histologic-pattern, critical-value-workflow,")
print("         blood-smear-systematic-review, frozen-section-thinking-aloud")
print("  5 refined: mcq-generation-with-rationales, reverse-case-drill,")
print("             paper-summarization, paper-methods-critique,")
print("             self-quiz-one-at-a-time")
