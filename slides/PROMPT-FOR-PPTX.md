# Prompt: Generate a 5-slide PowerPoint deck for the API Summit 2026 workshop

Paste everything below this line into the Claude chat that already has the
workshop slide-deck template / theme. The deliverable is a `.pptx` file that
matches that template exactly.

---

I need you to add **5 new slides** to the workshop deck for the API Summit 2026
talk *"AI in Pathology Education: A Practical Framework Across Learning,
Teaching, and Educational Operations."* Use the **exact same template, layout,
typography, and color palette** as the rest of the deck — the slides below
should drop in seamlessly.

Output format: a `.pptx` file containing only these 5 slides (I'll merge them
into the main deck myself). Slide size: 16:9 widescreen.

## Visual style (in case you need a refresher on the theme)

- **Palette**
  - Deep navy `#14213D` — primary text, structure, Pillar I accent
  - Burgundy `#7A1C28` — accent, eyebrow text, dividers, CTAs, Pillar II accent
  - Soft navy `#2C3E5C` — secondary text, Pillar III accent
  - Paper `#FAFAF7` — card backgrounds
  - Hairline rule `#E4E2DC` — borders
  - Muted text `#6B6F7A` — captions, meta
- **Type**
  - Headlines: Cormorant Garamond (serif), 80–100pt, semibold, tight leading
  - Subtitles: Cormorant Garamond italic, ~32pt
  - Eyebrow: Inter (sans), 18–22pt, uppercase, letterspaced, burgundy
  - Body / cards: Inter, 18–22pt
  - Example code: JetBrains Mono, 14–16pt
- **Layout discipline**
  - Generous left margin (~120px on a 1920×1080 frame)
  - 2-px burgundy horizontal rule (120px wide) under the subtitle
  - Card stacks with 1px hairline borders + 6px left-or-top accent stripe
  - Footer at the bottom of every slide: `Omar Z. Baba, MD · Henry Ford Health · API Summit 2026` (left) and page number `N / 5` (right), 1px top border

---

## Slide 1 — *The Digital Companion* (QR code + features)

**Eyebrow:** YOUR WORKSHOP COMPANION
**Title:** The Digital Companion
**Subtitle (italic):** A curated prompt library you can keep using long after the session ends

**Layout:** Two columns. Left = lead paragraph + 8 features in a 2×4 grid. Right = a "QR card" with a paper-colored background, 6px burgundy left border.

**Lead paragraph (italic serif, ~30pt, navy-soft):**

> Every prompt I'll demo today — plus 80 more — lives in this companion site. Scan the QR, sign in once, and return to the library whenever you need it.

**Features grid** (2 columns × 4 rows). Each feature has a burgundy filled circle with a white number (1–8), then a bold line, then a single muted-grey caption underneath:

1. **88 curated prompts** across three pillars
   *Each with intent, expected output, failure modes, and human verification step*
2. **How-to tutorials**
   *Including a comprehensive guide on writing good prompts — usable as a teaching session*
3. **Worked examples**
   *Full transcripts of real chains in practice — not just the prompt, but the whole session*
4. **Source-grounded AI guides**
   *NotebookLM vs. Claude Projects, privacy, copyright, grounding verification*
5. **Submit your own prompt**
   *Community contributions reviewed and credited — library grows with use*
6. **Comments & upvotes**
   *See what other pathology educators have found valuable; share your own variants*
7. **Floating feedback button**
   *Spotted a bug or want to suggest something? One click sends it straight to me*
8. **Privacy-first design**
   *Append-only access log, no tracking pixels, no third-party analytics*

**QR card (right column):**

- The QR code image itself (placeholder — I'll swap in the real one before printing). Size ~420×420 px, white background with 16px padding, thin grey border.
- Below the QR, italic serif "Scan to enter" (~28pt, navy-soft)
- Below that, monospace URL in burgundy: `omarzbaba.github.io/AI_Pathology_Education`
- Below the URL, in Inter ~24pt navy: **Sign in once with your name + email**
- One muted-grey sub-line: *Future visits restore automatically — even on new devices, with just your email.*

---

## Slide 2 — *What a good prompt looks like* (the 5-component framework)

**Eyebrow:** PRACTICAL FOUNDATIONS
**Title:** What a good prompt looks like
**Subtitle:** Five components — skip any one and the model fills the gap with guesses

**Layout:** A short italic lede across the full width, then 5 component cards in a 2×3 grid (the 6th cell is a wide navy banner spanning both columns at the bottom).

**Lede (italic serif, full width):**

> Most disappointing AI answers come from prompts missing one of these five. Add them all and you usually get a usable answer in one or two tries.

**Each of the 5 cards** has:
- A large faint serif number (1–5) in the top-right corner
- A small burgundy uppercase letterspaced eyebrow ("WHO IS THE MODEL", etc.)
- A serif name (Role / Context / Task / Format / Verification cue)
- A 1–2 sentence body in Inter
- A monospace example in a white box at the bottom

Cards alternate left-border color: cards 1, 3, 5 get a 6px navy left border; cards 2, 4 get a 6px burgundy left border.

**Card 1 — Role**
- Eyebrow: WHO IS THE MODEL
- Body: *Set the model's voice and frame of reference. Not decoration — it changes the texture of the output.*
- Example: `"Act as an experienced hematopathology attending teaching a PGY-2…"`

**Card 2 — Context**
- Eyebrow: WHAT IT CAN'T INFER
- Body: *Give what changes the answer — institution, learner level, specific scenario. Don't bloat with what's already known.*
- Example: `"PGY-2 in their first month of blood bank, two days of didactics…"`

**Card 3 — Task**
- Eyebrow: WHAT YOU WANT
- Body: *A verb plus a clear deliverable. Number multi-part tasks. "Explain MGUS" is a topic; "explain in three layers…" is a task.*
- Example: `"Explain in three layers: 1-sentence, mechanistic, nuanced."`

**Card 4 — Format**
- Eyebrow: SHAPE OF THE ANSWER
- Body: *Length, structure, named sections. Highest-leverage addition to a weak prompt — vague topic + specific format often works.*
- Example: `"Three paragraphs, layer name at the start of each, 3-5 sentences."`

**Card 5 — Verification cue**
- Eyebrow: HOW IT SIGNALS UNCERTAINTY
- Body: *Most-skipped, most-regretted component. Without it, models produce fluent confidence whether they know or not.*
- Example: `"Flag any numerical threshold I should verify against current IMWG criteria."`

**Bottom banner** (full width, navy background, white text, ~22pt):

> **Iterate in three rounds, not one.** Draft — observe — refine. The diagnosis step (round 2 → round 3) is where the learning happens. The third version is usually the one worth saving.

(The word "Iterate in three rounds, not one." should be in a warm gold/cream color like `#FFD8A8` to make it pop against the navy.)

---

## Slide 3 — *Pillar I: Self-Education*

**Eyebrow:** PILLAR I · 33 PROMPTS *(use a middle-dot, not pipe)*
**Title:** Self-Education *(in navy)*
**Tagline (italic serif under the title):** Using AI to learn pathology — concept work, drilling, paper critique, multimodal practice, source-grounded study.

**Layout:** 6 cards in a 3-column × 2-row grid. Each card has paper background, 1px grey border, **6px navy top border**, the card title in serif, a small burgundy uppercase count under it ("5 PROMPTS"), then a bulleted list with navy filled circles for bullets.

| Card | Count | Items |
|---|---|---|
| **Concept work** | 5 prompts | Concept explanation calibrated to your level · Compare & contrast adjacent entities · Guidelines in plain language · LIS / CP informatics review · Differential by histologic pattern |
| **Self-quizzing & drilling** | 7 prompts | One-at-a-time self-quiz (board-style) · MCQ generation with rationales · Anki flashcard generation · Board prep schedule · Question bank gap analysis · Reverse / forward / negative case drills · Diagnostic algorithm walkthrough |
| **Reading the literature** | 3 prompts | Paper summarization (calibrated) · Paper methods critique · Journal club pre-read |
| **Multimodal & lab** | 6 prompts | Photomicrograph self-quiz · SPEP / IFE interpretation drill · IHC stain interpretation · Blood smear systematic review · Frozen section "thinking aloud" · Molecular result interpretation |
| **CP workflow** | 1 prompt | Critical-value workflow drill |
| **Source-grounded AI** | 9 setup guides + variants | Build a board-prep notebook · Build a sign-out preview notebook · Build a journal club notebook · Source-grounded concept explanation · Source-grounded self-quiz / MCQs · Knowledge-gap discovery from sources · Cross-source comparison drill · Paper critique against your corpus |

---

## Slide 4 — *Pillar II: Teaching*

**Eyebrow:** PILLAR II · 21 PROMPTS
**Title:** Teaching *(in burgundy)*
**Tagline:** Using AI to teach pathology — objectives, vignettes, lectures, feedback, discussion design, resident-as-teacher.

**Layout:** Same 6-card grid (3×2), but card top-border accent is **burgundy** instead of navy. Bullet dots are burgundy. Subtitle rule under the title is also burgundy.

| Card | Count | Items |
|---|---|---|
| **Objectives & assessment** | 5 prompts | ACGME / EPA-aligned learning objectives · Bloom-leveled MCQs · OSCE station design · Resident feedback note drafting · CCC narrative comment drafting |
| **Cases & vignettes** | 2 prompts | PGY-calibrated case vignettes · Matched case-pair distractors |
| **Lectures & presentations** | 6 prompts | One-hour slide outline · Speaker notes for existing slides · Visual metaphor brainstorm · Audience polling questions · Short teaching video script · Microscopy teaching session structure |
| **Written feedback & narrative** | 2 prompts | Letter-of-recommendation starting draft · Subspecialty rotation goals letter |
| **Discussion-based formats** | 3 prompts | Journal club discussion questions · Tumor board presentation outline · Tumor board prep coaching |
| **Resident communication** | 3 prompts | Sign-out teaching turn · Resident-as-teacher framework · Difficult feedback conversation prep |

---

## Slide 5 — *Pillar III: Educational Operations*

**Eyebrow:** PILLAR III · 34 PROMPTS
**Title:** Educational Operations *(in navy)*
**Tagline:** Using AI to produce the artifacts around teaching events — workshops, rotations, courses, conferences, journal clubs.

**Layout:** 4 cards in a 2×2 grid (since each card has more items than the other pillars). Card top-border accent is **soft navy `#2C3E5C`**.

| Card | Count | Items |
|---|---|---|
| **Workshops** | 10 prompts | Announcement & registration page · Pre-workshop survey · Facilitator run-of-show · Station-by-station guide · Badge design spec · Access-card layout · Certificate of completion · Faculty feedback summary · Post-workshop thank-you · Lab incident debrief |
| **Rotations** | 10 prompts | Orientation one-pager · Expectations document · Reading list (PGY-calibrated) · Daily / call / block schedules · Evaluation rubric · Mid-rotation feedback template · End-of-rotation evaluation · Resident-to-resident handoff |
| **Courses** | 7 prompts | Syllabus draft · Weekly module packet · Assignment grading rubric · Feedback collection form · Course post-mortem · IRB / QI protocol skeleton · Promotion portfolio narrative |
| **Conferences & journal clubs** | 7 prompts | Conference schedule planner · Grand rounds speaker prep · Visiting professor invitation · Tumor board case packet · Journal club packet · Medical education abstract · Q&A prep doc |

---

## Footer (every slide)

Bottom strip, 1px top border:

- **Left:** `Omar Z. Baba, MD · Henry Ford Health · API Summit 2026` (Omar's name in semibold, rest in regular muted grey)
- **Right:** page number, e.g. `1 / 5` (tabular-nums)

---

## Deliverable

A single `.pptx` file with these 5 slides in this order. Use the deck's existing
master / theme so the slides drop into the larger deck without restyling. If
something here conflicts with the theme, **defer to the theme** — don't reinvent
typography or colors, just slot the content into the existing patterns.

If you can't render the QR code image, use a placeholder rectangle labeled
"QR CODE — link to companion site" and I'll swap in the real PNG.

Thanks.
