#!/usr/bin/env python3
"""
Deep refinement batch 3 (25 prompts):
- 10 remaining Pillar 2 prompts (deeply refined)
- 7 new Pillar 3 prompts (created at exemplar depth)
- 8 highest-value existing Pillar 3 prompts (deeply refined)
"""

from pathlib import Path

def write_prompt(path, fm, body):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("---\n" + "\n".join(f"{k}: {v}" for k, v in fm.items()) + "\n---\n\n" + body)

P2 = "library/pillar-2-teaching/prompts"
P3 = "library/pillar-3-educational-operations/prompts"

# ===========================================================================
# PILLAR 2 — REMAINING 10 PROMPTS (deeply refined)
# ===========================================================================

write_prompt(f"{P2}/matched-case-pair.md",
    {"title":"Matched case pair — reactive vs neoplastic","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"advanced","time_to_use":"2-10min","visual":"text-only",
     "tags":"vignette, differential, paired-cases","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Generates two case vignettes that share superficial features but diverge on a specific discriminating feature — the one you want to teach. The pair structure forces residents to NOTICE the discriminator rather than pattern-match to a likely diagnosis. The hardest discipline this enforces: the cases must be parallel in every dimension EXCEPT the intended discriminator.

## When to use it

When teaching a differential where two entities are commonly confused, especially when the discrimination is taught in a textbook but rarely drilled in cases. Pairs well with sign-out teaching or journal club discussion.

**Not for:** generic case generation (use [Case vignette at PGY level](library.html#/library/pillar-2-teaching/prompts/case-vignette-pgy)), broader pattern discrimination (use [Differential by histologic pattern](library.html#/library/pillar-1-self-education/prompts/differential-by-histologic-pattern)), or pairs where you don't yet know what the discriminating feature should be.

## The prompt

```
You are generating a matched case pair for teaching a specific discrimination. The pair must be parallel in every dimension EXCEPT the intended discriminator.

## What I'm requesting

- **Entity A and Entity B to discriminate:** [be specific — e.g., "reactive follicular hyperplasia (Entity A) vs grade 1-2 follicular lymphoma (Entity B)"]
- **The discriminating feature(s) I want to teach:** [name the specific feature — e.g., "bcl-2 positivity in follicles, absent in reactive and present in FL"]
- **Audience level:** [PGY level + rotation context]
- **Cognitive trap to avoid:** [optional — e.g., "residents tend to anchor on architecture and miss the IHC"]

## What to produce

### Case A

- **Vignette (4-6 sentences):** clinical context, presentation, initial findings
- **Histology description:** what's on the slide at low → high power
- **Workup results:** IHC, molecular as relevant
- **The discriminating feature as it appears in THIS case** (positive or negative)
- **Intended diagnosis:** stated explicitly

### Case B

Same structure. **Parallel to Case A in every dimension** (similar age range, similar location, similar presenting complaint, similar initial workup architecture) EXCEPT for the discriminating feature.

### Side-by-side comparison table

| Feature | Case A | Case B |
|---|---|---|

Include the features that are SAME (so residents notice that the difference is NOT in those features) and the discriminating feature(s).

### The 'aha' question

When residents see both side by side, what specific question crystallizes the discrimination? Phrase the exact question — not "ask them to compare," the question itself.

## Hard rules

- **Parallelism is the entire point.** If the cases differ in age, sex, location, presenting complaint, etc., the discrimination becomes confounded.
- **The discriminating feature must be the SAME feature in both cases** — present in one, absent in the other (or different in a specific way). Not "Case A has X, Case B has Y."
- **The 'aha' question is non-negotiable.** Without it, the pair is just two cases.
- **No PHI.** Both vignettes are fictional or sufficiently genericized.

## What I will NOT accept

- Pairs that differ in confounding features
- Discriminators that depend on tests I can't get in real practice
- 'Aha' questions that are leading rather than illuminating
- Vignettes of very different lengths or detail levels (signals the difference)
```

## Expected output

Two parallel cases + side-by-side table + 'aha' question. Length ~500-700 words.

## Common failure modes

- **Confounded cases.** Push back: "Cases differ in [feature]. Make them parallel."
- **'Aha' question is leading.** Push back: "Make it open-ended."

## Required human verification

- Verify the discriminator is what current practice actually uses (not an outdated criterion).
- Pressure-test with a resident who hasn't been taught the discrimination — do they notice it, or does the pair feel like "two cases"?

## Best model and why

**Claude Opus 4.7** — parallel construction with a single deliberate difference is harder than it looks. Opus is more disciplined about NOT varying confounding features.
""")

write_prompt(f"{P2}/slide-outline-1hr.md",
    {"title":"Slide outline for a 1-hour lecture","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"lecture, slides, timing","verified_months":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Generates a slide outline for a 1-hour lecture: 35-45 slides, beat structure (hook → roadmap → 3-4 content beats → synthesis → Q&A), per-slide visuals, audience interaction moments, anchor slides, and a contingency cut list for when you run out of time.

Breaks the staring-at-empty-PowerPoint paralysis.

## When to use it

When you've agreed to give a lecture and need a starting structure. Best done 2-3 weeks before, leaving time to slot in your actual content and refine.

**Not for:** short talks (different format), workshops (different design), or generating the actual slides (this is outline only).

## The prompt

```
You are generating a slide outline for a 1-hour lecture. Stay disciplined about timing and visual diversity. Resist the urge to cram more slides.

## What I'm building

- **Topic:** [be specific]
- **Audience:** [PGY level / faculty / mixed — describe]
- **Lecture context:** [grand rounds / didactic conference / society talk / industry CME — affects tone]
- **My existing materials:** [any slides, papers, prior talks I can draw from]
- **The ONE thing I want the audience to walk away with:** [stated explicitly]

## What to produce

### Beat structure (timed)

- **Opening hook** (1 slide, 2-3 min) — what's the specific hook? A case? A statistic? A contrarian framing?
- **Roadmap** (1 slide, 1 min) — preview the 3-4 content beats
- **Content beats** (3-4 beats, 8-12 slides each, ~12-15 min each)
- **Synthesis** (2-3 slides, 3-5 min)
- **Q&A buffer** (1 slide, 5-10 min)

Total slides: 35-45. Roughly 1 slide per 80-100 seconds of speaking time.

### Per-slide outline

For each slide:
- **Title** (the actual title, not a placeholder)
- **2-3 content bullets** (what's on the slide — bullets, not full sentences)
- **Recommended visual** (one line: 'photomicrograph of X', 'algorithm flowchart', 'table comparing A and B', 'text only')
- **Speaking time** (typically 60-120 sec)

### Audience interaction beats

Mark 2-4 moments where you'd interrupt the lecture with:
- A poll question
- A case to think about
- A question to the room
- A "raise your hand if..." check-in

These usually go at transitions between beats.

### Anchor slides

Identify the 2-3 slides that, if you only had 30 seconds, you'd use. These anchor the lecture.

### Contingency cut list

Identify the 3-5 slides you'd cut FIRST if you run out of time, and why those specifically (not anchor slides, not central to the argument).

### Time-budget check

After producing the outline, sum the speaking time per slide. Confirm it fits 60 minutes including Q&A. Flag if it doesn't and recommend specific compressions.

## Hard rules

- **35-45 slides total.** Resist the urge to add more.
- **Visual diversity.** Not every slide can be bullet points.
- **Audience interaction beats are non-negotiable.**
- **Timing math must add up to 60 minutes.**

## What I will NOT accept

- An outline with 80 slides
- All slides marked "text only"
- No anchor slides identified
- Timing that exceeds 60 minutes without compression recommendations
```

## Expected output

35-45 slide outline with titles, bullets, visuals, timing, interaction beats, anchors, cut list. Length 800-1500 words.

## Common failure modes

- **Over-slided.** Push back: "Cut to 40."
- **No visual diversity.** Push back: "Vary the visuals."
- **Timing math wrong.** Push back: "Add it up. Does it fit?"

## Required human verification

- Walk through the outline at presentation pace (~80 sec/slide) and check timing.
- Verify substantive content for each beat against your subspecialty's reference.
- Source the visuals from properly licensed material.

## Best model and why

**Claude Sonnet 4.6** — structured planning with timing is Sonnet's strength. Opus only if the topic is unusually complex.
""")

write_prompt(f"{P2}/speaker-notes.md",
    {"title":"Speaker notes for existing slides","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"lecture, speaker-notes, spoken-voice","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Generates speaker notes for your existing slide deck: paste your slide titles + bullets, get back per-slide notes that expand bullets into spoken prose, include the specific example to use, mark interaction beats, and bridge to the next slide. Notes are in SPOKEN voice — short sentences, no jargon you wouldn't actually say.

## When to use it

When you've built slides but haven't yet rehearsed, or when you'll be delivering the same talk multiple times and want a script to anchor your first pass. The notes get refined each iteration.

**Not for:** writing the slides themselves (use the slide outline prompt), generating substantive new content (the model fills in connective tissue — your bullets supply the substance), or any context where written-voice formality is expected (different format).

## The prompt

```
You are generating speaker notes for an existing slide deck. Notes must be in SPOKEN voice. Aloud-test as you write — if a sentence reads like written prose, rewrite for the ear.

## What I'm providing

- **Talk title and duration:** [e.g., "Approach to monoclonal gammopathy, 45 min + 15 min Q&A"]
- **Audience:** [PGY level / faculty / mixed]
- **Slide content:** [paste slide titles + bullet content, one slide per block]
- **My specific examples / anecdotes / cases:** [paste the ones I want to use]
- **My delivery style:** [conversational / formal / Socratic — pick]

## For each slide, produce

1. **Transition sentence from the previous slide** (1 sentence — the bridge that makes the lecture feel continuous)
2. **Expansion of each bullet into 2-3 spoken sentences** (more than the slide says, less than a paragraph)
3. **The specific example, anecdote, or analogy I should use here** — drawn from what I gave you. If I didn't provide one for a slide that needs it, mark `[INSERT EXAMPLE]`.
4. **Bridge sentence to the next slide** (1 sentence)
5. **Interaction marker** if this slide has a poll, audience question, or case to think about — bracketed `[PAUSE FOR POLL]` or similar

## For visual/diagram slides with minimal text

Speaker notes should be LONGER, not shorter. The visual is your prompt; the notes are where you explain what the audience sees. Walk through the visual systematically: "On the left, you'll see... in the middle... on the right..."

## Tone and voice

- **Short sentences.** Speakers can hold ~15 words at a time, not 40.
- **Conversational vocabulary.** If a word feels like reading-vocab, replace it.
- **First person plural** where appropriate ("we know", "we've seen") rather than passive voice.
- **One thought per sentence.** Embedded clauses lose listeners.

## Hard rules

- **Notes are spoken voice, not written voice.** If a sentence reads like a journal article, rewrite for the ear.
- **Do not invent clinical content** I didn't provide on the slides. Connective tissue only.
- **Mark `[INSERT EXAMPLE]`** rather than making up an anecdote.
- **Transition sentences are non-optional.** They make the lecture feel continuous.

## What I will NOT accept

- Notes that sound like written prose ("It is important to recognize that...")
- Generic examples ("a recent case")
- Slide notes that fabricate content not on the slide
- Missing transitions
```

## Expected output

Per-slide notes with transitions, expansions, specific examples, bridges, and interaction markers. Length scales with number of slides.

## Common failure modes

- **Written voice slipping in.** Push back: "Read aloud. Does it sound like you?"
- **Fabricated examples** when you didn't supply one. Push back: "Mark [INSERT EXAMPLE]; don't invent."
- **Generic clinical content added** beyond what's on the slide. Push back.

## Required human verification

- Verify any clinical content the model added beyond what was on the slide. The model fills gaps and sometimes fills them wrong.
- Rehearse the notes aloud. Spoken language reveals problems written language hides.

## Best model and why

**Claude Sonnet 4.6** — expanding bullets into natural spoken voice is a workhorse task. Sonnet's voice is more natural for spoken delivery than GPT-4o (tends toward written register).
""")

write_prompt(f"{P2}/visual-metaphor.md",
    {"title":"Visual metaphor brainstorming","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"<2min","visual":"text-only",
     "tags":"teaching, metaphor, abstract-concepts","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Generates 5-7 candidate visual metaphors for an abstract concept, with explicit precision-vs-accessibility tradeoffs scored for each. The point isn't to pick the metaphor for you but to surface options you wouldn't have generated alone, with honest acknowledgment of where each one breaks down.

## When to use it

When you're explaining an abstract concept (clonality, gating in flow cytometry, antibody-antigen interactions, deconvolution) and your usual go-to metaphor isn't landing. Brainstorming fuel, not the final answer.

**Not for:** lookups (just look up the standard metaphor), highly technical audiences where metaphors do more harm than good, or contexts where precision-over-accessibility is required.

## The prompt

```
You are generating visual metaphor options for me. Be honest about each metaphor's precision tradeoffs. A metaphor that sounds clever but distorts the concept is worse than no metaphor.

## What I'm explaining

- **Abstract concept:** [be specific — e.g., "clonality in lymphoid populations" not just "clonality"]
- **Target audience:** [medical students / residents / attendings / patients — calibrates the precision-accessibility tradeoff]
- **What I want them to understand specifically:** [the key insight the metaphor should land]
- **Metaphors I've already tried:** [optional — so you don't repeat them]

## Produce 5-7 candidate metaphors

For each:

1. **The metaphor** (1 sentence)
2. **What it captures well** — which features of the concept does this metaphor faithfully represent?
3. **Where it breaks down** — the feature of the concept that this metaphor distorts or misses. Be honest here; this is the most important field.
4. **Precision score (1-5):** how technically accurate is the metaphor when pushed?
5. **Accessibility score (1-5):** how immediately graspable is it for the target audience?

## Ranking

Rank by (precision × accessibility). Acknowledge the trade-off: the most accessible metaphors are often the least precise.

## Recommendation by audience

End with:
- "If you're teaching medical students, use [metaphor X] because [reason]"
- "If you're teaching attendings, use [metaphor Y] because [reason]"

## Hard rules

- **Be honest about precision.** Inflated precision scores defeat the entire prompt.
- **The "where it breaks down" field is the most important.** If a metaphor breaks at a critical point and you don't say so, you've mis-served the teacher.
- **Diverse metaphors, not variants of one.** "Like a key in a lock" and "like a key fitting a door" are the same metaphor.
- **Acknowledge if a metaphor is technically inaccurate.** A precision score of 2 means "breaks down when an expert pushes" — that's important to know.

## What I will NOT accept

- All metaphors are variants of one
- Inflated precision scores (everything 4-5)
- Superficial "breaks down" analysis
- No audience-differentiated recommendation
```

## Expected output

5-7 ranked metaphors with strengths, weaknesses, scores. Plus the audience-differentiated recommendation.

## Common failure modes

- **Convergent metaphors** (all variations on one theme). Push back: "Generate genuinely different metaphors."
- **Score inflation.** Push back: "Be honest — what's the precision score if an expert pushes?"
- **Superficial 'breaks down' analysis.** Push back: "Where specifically does it fail?"

## Required human verification

- Push each metaphor to its breaking point with a colleague in your subspecialty. Metaphors that survive expert pushback are the ones to use.
- Trust audience feedback over your own assessment — if the metaphor doesn't land, the precision score doesn't matter.

## Best model and why

**Claude Opus 4.7** — generating *diverse* metaphors (not variations of one) is a creativity task where Opus pulls away. Sonnet tends to converge.
""")

write_prompt(f"{P2}/audience-polls.md",
    {"title":"Audience poll question generation","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"<2min","visual":"text-only",
     "tags":"polls, audience-engagement, live-teaching","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Generates audience poll questions for a live talk — designed for engagement and misconception-surfacing, not assessment. Each poll has a "wrong" answer that most of the audience will pick (by design — that's where the teaching beat is), with notes on what to say at each likely audience distribution.

The discipline this enforces: a poll where everyone gets it right immediately is a failed poll.

## When to use it

When you're delivering a 30-60 minute talk and want 2-3 polling moments to break the lecture rhythm and surface misconceptions. Pairs well with the slide outline prompt.

**Not for:** assessment questions (use MCQ generator), polls in workshops (different format and audience dynamics), or audiences who won't engage with polls (read the room first).

## The prompt

```
You are generating audience poll questions for a live talk. These are teaching moments, not assessments. A poll where everyone gets it right immediately is a failed poll — the wrong answer must be plausibly attractive.

## What I'm building

- **Talk topic and duration:** [e.g., "approach to monoclonal gammopathy, 45 min"]
- **Audience:** [PGY level / faculty / mixed — calibrates difficulty]
- **Number of polls:** [usually 2-3]
- **Where in the talk you want them:** [optional — e.g., "after the diagnosis section, before treatment"]

## For each poll, produce

1. **The question** — short stem, ideally 3 answer choices (not 5). Should be answerable in 30-60 seconds.
2. **Answer choices** with the correct answer marked
3. **The "intended wrong answer"** — the answer most of the audience will pick. This is the teaching opportunity.
4. **Why residents pick the wrong answer** — the specific misconception or cognitive shortcut.
5. **Predicted audience distribution** (e.g., "30% correct, 50% intended wrong, 20% other")
6. **Suggested placement in the talk** — where it serves as a transition or misconception-surfacing moment
7. **What to say at each likely result:**
   - "If 60% pick the intended wrong answer..." → your teaching response
   - "If they all get it right..." → your pivot (still useful, just shorter)
   - "If they split..." → your acknowledgment

## Hard rules

- **Each poll must have a "wrong" answer that's plausibly attractive.** No obvious throwaways.
- **The teaching response — what to say after the poll — is non-negotiable.** Without it, the poll lands flat.
- **Don't over-poll.** 2-3 polls in a 45-min talk is right; more becomes a quiz show.
- **Specific placement.** "Use this poll somewhere in the talk" is not specific.

## What I will NOT accept

- Polls with obvious right answers
- "Suggested wrong" that no one would actually pick
- No teaching response for the most likely audience distribution
```

## Expected output

N polls with all 7 elements. Total ~500-800 words for 3 polls.

## Common failure modes

- **Obvious right answer.** Push back: "Make the wrong answer more attractive."
- **Generic teaching responses.** Push back for specific.

## Required human verification

- Pre-test the poll with a colleague at the target audience level — if they get the intended-wrong answer right cold, the poll won't work.
- Verify the correct answer.

## Best model and why

**Claude Sonnet 4.6** — poll generation with predicted distributions is well within Sonnet's range. The discipline (plausibly-wrong answer) matters more than model depth.
""")

write_prompt(f"{P2}/video-script.md",
    {"title":"Video script and storyboard","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"advanced","time_to_use":">10min","visual":"text-only",
     "tags":"video, scripting, storyboard","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Drafts a 2-column video script (narration / visuals) for a short educational explainer, with timed beats, specific visual cues, opening hook, and a single takeaway. Built for short asynchronous content (2-5 min) where pacing and visual design matter more than depth.

## When to use it

When you're producing educational video content for asynchronous viewing — onboarding clips, social media explainers, training modules. Especially useful as a starting structure before you record.

**Not for:** long lectures (different format), live demos, or contexts where you're not actually planning to produce video.

## The prompt

```
You are drafting a script for a short educational video. The script must work as video, not as a talking-head reading lecture notes. Hook in 5 seconds, takeaway in the last 5 seconds.

## What I'm producing

- **Topic:** [be specific]
- **Target duration:** [in minutes — be honest about what fits]
- **Audience:** [target — students, residents, patients, etc.]
- **Production capacity:** [I'm shooting myself with a phone / professional setup / animation only — calibrates visual complexity]
- **Distribution:** [internal training / public / specific platform]

## Format — two columns, timed beats

| Time | Narration | Visual |
|------|-----------|--------|
| 0:00-0:05 | [opening hook] | [shot description] |
| 0:05-0:15 | [next beat] | [shot or on-screen text] |

Each row = 5-15 seconds of video. Be specific about visuals.

## Required elements

### Opening hook (0:00-0:05)
The first 5 seconds must give viewer a reason to keep watching. Stating the topic is NOT a hook. Hooks that work:
- A specific question or statistic
- A surprising claim
- A case scenario in one sentence
- A contrarian framing

### Body (most of the duration)
Build the argument in beats. Each beat advances the explanation. Maximum 4-5 beats for a 3-minute video.

### Visuals
For each beat: 'cut to photomicrograph', 'animated diagram of antibody binding', 'on-screen text: NORMAL RANGE 4.0-11.0 K/uL', 'B-roll of lab', etc. Be specific.

### Single takeaway (last 5 seconds)
The one sentence viewers will remember 24 hours later. State it on-screen as text AND say it in narration.

## After the script

List:
- **Assets I'll need to produce or source** (2-3 most important)
- **Estimated word count of narration** (compare against speaking-pace target of 150 wpm — flag if script will overrun)

## Hard rules

- **Hook in 5 seconds.** Not "introduction" — hook.
- **Visuals are specific, not placeholder.** "Relevant image" is not specific.
- **Total narration word count must fit the duration at 150 wpm.** Sum it and check.
- **One takeaway, not five.** A 3-minute video with 5 takeaways has zero takeaways.

## What I will NOT accept

- Hook that's "Hi, today we're going to talk about X"
- Generic visuals
- Script that overruns the target duration when read aloud at 150 wpm
- More than one takeaway
```

## Expected output

A 2-column timed script + asset list + word-count check. Length depends on target duration.

## Common failure modes

- **Weak hook.** Push back: "Make the first 5 seconds make me want to keep watching."
- **Vague visuals.** Push back: "What's actually on screen?"
- **Script too long.** Verify word count.

## Required human verification

- Read the script aloud at natural pace and time it. AI scripts almost always overrun.
- Verify any specific clinical content.
- Source visuals from properly licensed material.

## Best model and why

**Claude Sonnet 4.6** — structured creative writing with timing is Sonnet's strength.
""")

write_prompt(f"{P2}/resident-feedback-note.md",
    {"title":"Resident feedback note drafting","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"feedback, narrative, evidence-based","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Converts your bullet observations from a rotation into a polished feedback note that residents will actually read and remember. Strict discipline: every claim in the note must trace to an observation you provided. No extrapolation, no padding, no manufactured praise.

## When to use it

End of rotation, when you've taken notes during the block and want to convert them into a readable feedback document. Best within a week of the rotation end while details are fresh.

**Not for:** CCC narratives (use [CCC narrative comment drafting](library.html#/library/pillar-2-teaching/prompts/ccc-narrative-comment) — different audience), high-stakes professionalism conversations (use [Difficult feedback conversation prep](library.html#/library/pillar-2-teaching/prompts/difficult-feedback-conversation-prep)), or feedback you don't actually have observations for.

## The prompt

```
You are drafting a feedback note for a resident. Every claim in the note must trace to an observation I gave you. Do not extrapolate, manufacture praise, or pad to reach a length.

## What I'm providing

- **Resident initial and PGY:** [e.g., "Resident DA, PGY-2"]
- **Rotation and duration:** [e.g., "blood bank, 4 weeks"]
- **Service context:** [the rotation environment, my role, frequency of interaction]
- **My observations (bullets):**
  [paste — mix of strengths, growth areas, specific incidents]
- **My intended outcome for this feedback:** [what I want the resident to do differently or keep doing]

## Note structure (5 sections, ~250-350 words total)

1. **Opening orientation (1-2 sentences)** — the rotation, level of trust the resident operates at, the overall arc
2. **Strengths section (2-4 specific strengths)** — each tied to a behavior or incident I noted. Avoid generic praise like "great communicator."
3. **Growth section (2-3 specific growth areas)** — each tied to a behavior or incident. Use actionable language — what would "better" look like specifically?
4. **One behavioral commitment** — framed as a question the resident should ask themselves at each sign-out (e.g., "Before I commit to this interpretation, what would I want to see that I haven't?")
5. **Closing (1 sentence)** — forward-looking, not a hollow compliment

## Tone

- Warm but honest
- Specific over generic
- Behavioral over personality-based
- Direct without being harsh

## Hard rules

- **Every claim must trace to an observation I provided.** If you find yourself padding to reach the target length, leave it short.
- **Do NOT add praise or critique I didn't write.** Watch for this — it dilutes credibility.
- **Growth areas framed as behaviors, not personality traits.** "Be more confident" is bad; "When you commit to an interpretation at sign-out, lead with the diagnosis rather than the differential" is good.
- **The behavioral commitment is non-optional.** Without it, the feedback is reflective, not actionable.

## What I will NOT accept

- Claims I can't trace to my observations
- Generic praise or growth areas
- Personality-trait framing
- A hollow closing ("great work, keep it up!")
```

## Expected output

A 5-section feedback note (~250-350 words) tightly grounded in your observations.

## Common failure modes

- **Manufactured observations.** Push back: "I didn't write that. Where did you get it?"
- **Personality-trait framing.** Push back: "What's the behavior?"
- **Hollow closing.** Push back.

## Required human verification

- Re-read against your original observations. Anything in the note that's not in your bullets is the model speaking, not you. Delete or rewrite.
- Sanity-check the tone with how you'd actually talk to this resident.

## Best model and why

**Claude Opus 4.7** — voice and nuance matter here. Opus produces feedback that reads more like a thoughtful attending; Sonnet tends toward template phrasing.
""")

write_prompt(f"{P2}/journal-club-discussion-q.md",
    {"title":"Journal club discussion questions","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"<2min","visual":"text-only",
     "tags":"journal-club, discussion, escalating-questions","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Generates 5 discussion questions for journal club, ordered from concrete (methods, numbers) to abstract (implications, practice-change) and ending with one genuinely contested question that reasonable experts disagree about.

## When to use it

When you're leading journal club and want a question set that escalates rather than stays at one level. Especially valuable for stalling-out discussions ("any questions?" → silence).

**Not for:** generating the pre-read packet (use [Journal club packet generation](library.html#/library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/journal-club-packet)), discussion of methods alone (use [Paper methods critique](library.html#/library/pillar-1-self-education/prompts/paper-methods-critique)), or contexts where you can't ground questions in the actual paper.

## The prompt

```
You are generating 5 discussion questions for journal club. They must escalate from concrete to contested. The fifth question is the test — if it has an obvious right answer in current literature, it's not actually contested.

## What I'm requesting

- **Paper:** [citation or attached PDF]
- **Audience:** [PGY level + faculty mix]
- **Discussion length:** [usually 30-45 min for questions]
- **My role:** [discussion leader / participant prepping]

## Honesty check first

Do you have access to the actual paper text? If not, say so. Questions generated from title alone fabricate methods and findings.

## Generate 5 questions, ordered

### Question 1: Concrete methods question
A specific design choice or analytic approach to scrutinize. Answer should be in the paper.

### Question 2: Finding-level question
How confident should we be in the headline result given the design? Requires interpretation, not just recall.

### Question 3: Generalizability question
Does this apply to our patient population? What specifically about ours would limit applicability?

### Question 4: Practice-change question
Should this change what we do, and if so, in what specific setting for which patients?

### Question 5: Contested question
One that reasonable experts would genuinely disagree on. Should provoke real debate.

## For each question, also provide

- **Question text** (the actual question)
- **What this question opens up** — what discussion thread does it start?
- **The "wrong" or shallow response** likely to come up early and how to redirect

## Hard rules

- **Questions must escalate.** Q1 should be answerable from the paper; Q5 should not have a single right answer.
- **Q5 must be genuinely contested.** Pressure-test: if the answer is obvious to literate experts, it's not Q5.
- **No leading questions** ("Don't you think...?").
- **Each question should be answerable in 5-8 minutes of discussion** — not a thesis topic.

## What I will NOT accept

- All questions at the same abstraction level
- Q5 that has an obvious settled answer
- Leading questions
- Generic questions that could apply to any paper
```

## Expected output

5 questions with productivity notes and predicted-shallow-response handling. Length ~400-600 words.

## Common failure modes

- **All questions at the same level.** Push back: "Question 5 should be more abstract than Question 1."
- **Q5 has an obvious answer.** Push back: "What's something experts disagree on?"

## Required human verification

- Pre-test Q5 with a colleague — if they immediately agree with you, not contested.
- Verify questions are answerable from the actual paper.

## Best model and why

**Claude Sonnet 4.6** — question escalation across abstraction levels is well within Sonnet's range.
""")

write_prompt(f"{P2}/tumor-board-presentation.md",
    {"title":"Tumor board case presentation template","pillar":"teaching","event_type":"n/a",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"tumor-board, presentation, structured-format","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Generates a tumor board case presentation outline that walks through history → imaging → pathology in the order the audience needs it, ends with an explicit decision question for the board, and anticipates the 2-3 most likely follow-up questions.

The hardest discipline: strip ALL patient identifiers before generating the outline. The model cannot un-see identifiers once they're in the conversation.

## When to use it

When you're presenting a case at tumor board and need a structured outline. Also useful as a teaching tool for junior residents who need to learn the structure.

**Not for:** real-time presentation prep (use the tumor board prep coaching prompt instead), generating the packet (use [Tumor board case packet](library.html#/library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/tumor-board-case-packet)), or cases that can't be sufficiently de-identified.

## The prompt

```
You are generating a tumor board case presentation outline. STRIP ALL PATIENT IDENTIFIERS before generating. No name, no MRN, no exact age, no exact date, no rare-combination giveaways.

## Provenance check first

Confirm the case I'm pasting is sufficiently de-identified. If anything looks identifiable, STOP and tell me before generating the outline.

## What I'm presenting

- **Clinical history (de-identified):** [paste — age range, sex if relevant, brief presentation, comorbidities, prior workup]
- **Imaging findings:** [paste summary]
- **Pathology findings:** [paste — gross, microscopic, IHC, molecular as available]
- **Question for the board:** [the explicit decision being asked — staging, treatment, second opinion, etc.]
- **Tumor board type:** [GU MDTB, GI MDTB, etc.]

## Outline structure (3-4 minutes of presentation)

1. **One-sentence patient summary** (anonymized): age range, key comorbidity if relevant, presentation
2. **Imaging summary** in radiologist-friendly framing — what they need to know to interpret the pathology
3. **Pathology in order:** gross → microscopic → IHC → molecular. Lead with diagnostic features, not workup history.
4. **Diagnosis and stage** (if applicable)
5. **The decision point** — what the board is being asked to advise on, stated explicitly
6. **2-3 most likely questions from the board** — from med onc, rad onc, surg, radiology — and the data points to have ready

Length: 3-4 minutes of presentation time. No PHI.

## Hard rules

- **No PHI ever** — strip identifiers before generating.
- **Decision point explicit, not buried.** The board should know what you're asking by minute 1.
- **Anticipated questions from each relevant specialty** present at YOUR institution's board.
- **Pathology presented in DIAGNOSTIC order** (what tells you the diagnosis first) not workup chronological order.

## What I will NOT accept

- Any identifiable patient information
- Decision question buried at the end
- Generic anticipated questions that don't match the case
- Pathology in workup-chronological order (boring) rather than diagnostic-priority order
```

## Expected output

A structured outline ready to present (~400-600 words) plus anticipated questions and data points.

## Common failure modes

- **Identifiable info slipping through.** Strip BEFORE pasting.
- **Decision question buried.** Push back.

## Required human verification

- **No PHI ever** — verify de-identification.
- Verify pathology summary against your sign-out.
- Run anticipated questions by a colleague who attends your tumor board regularly.

## Best model and why

**Claude Sonnet 4.6** — structured case outlines are Sonnet's wheelhouse. PHI discipline is more important than model choice.
""")

write_prompt(f"{P2}/resident-as-teacher.md",
    {"title":"Resident-as-teacher scaffolding","pillar":"teaching","event_type":"n/a",
     "audience":"resident","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"resident-as-teacher, scaffolding, teaching-skills","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_invariant":"2026-05-17"},
    """## What this prompt does

Scaffolds a teaching session for a resident who has been asked to teach — typically for the first time. Forces the resident to think about teaching as a deliberate practice (one concept, one slide, one exercise) rather than content delivery.

The single most useful question: "what is the ONE concept you most want them to walk away with?" If it doesn't fit in one sentence, it's too broad.

## When to use it

When you're a senior resident asked to give a teaching session, or when you're an attending coaching a resident through their first teaching attempt. Useful both as preparation and as a coaching conversation guide.

**Not for:** experienced teachers (different scope), prep for high-stakes formal lectures (use the slide outline prompt), or contexts where you're being assessed on teaching skill (different framing).

## The prompt

```
You are scaffolding my preparation for a teaching session. Push me to think about teaching as a deliberate practice, not content delivery. If my answers are vague, push back.

## My context

- **My level:** [PGY level]
- **Session topic:** [what I'm teaching]
- **Audience:** [who and how many — be specific, e.g., "the three incoming PGY-1s in their first week of CP, plus the senior resident who's been with us a year"]
- **Session duration:** [in minutes]
- **Format:** [didactic / case-based / hands-on / interactive — what I have in mind]
- **My teaching experience:** [first time / a few times / regular]

## Walk me through these 6 questions, one at a time

### 1. What is the ONE concept you most want them to walk away with?

State it in one sentence. If you can't fit it in one sentence, it's too broad — push you to narrow.

Pressure-test: can a learner reasonably restate it in 30 seconds at the end of the session? If not, still too broad.

### 2. What are the 2-3 common misconceptions about this topic you should anticipate?

These are the misconceptions that experienced teachers know but you might miss. If your answers are generic ("they might think it's easy"), push for specific cognitive shortcuts learners use.

### 3. If you had only ONE slide, what would it show?

Describe the visual or text in detail. This is the anchor slide — if you had 30 seconds with this audience, what would you put up?

### 4. What is the simplest exercise you could do that would let you see whether they understood the one concept?

Active retrieval or application. Not "ask if they have questions" — an exercise that produces an artifact (a written answer, a verbal commitment, a marked-up image).

### 5. What's the question you should NOT try to answer in this session?

The related topic that would be a different talk. Naming it explicitly prevents scope creep.

### 6. How will you know if the session went well?

Give 2-3 observable indicators during or right after — not "they seemed engaged" but specific behaviors.

## After my answers, give me

- **Your one specific suggestion** for how to make the session land better
- **The one risk** I should anticipate

## Hard rules

- **Walk through questions ONE AT A TIME.** Wait for my answer.
- **Push back if my answer is vague.** Generic answers produce generic sessions.
- **The 'one concept' must fit in 30 seconds.** If not, narrow.
- **Observable indicators must be observable.** "Engagement" is not observable.

## What I will NOT accept

- Walking through all 6 questions at once
- Accepting vague answers without pushback
- Recommendations that aren't specific to my context
```

## Expected output

A back-and-forth scaffolding conversation across 6 questions, ending with the model's specific suggestion and risk callout.

## Common failure modes

- **Model dumps all 6 questions at once.** Push back: "One at a time."
- **Accepting vague answers.** Push back yourself: "I gave a vague answer — push me to be more specific."
- **Generic suggestions at the end.** Push back.

## Required human verification

- Run the 'one concept' by a colleague at the target audience level — does it land?
- Validate the observable indicators are actually observable.

## Best model and why

**Claude Sonnet 4.6** — reflective scaffolding suits Sonnet's pattern of clear, structured outputs.
""")

# ===========================================================================
# PILLAR 3 — 7 NEW PROMPTS + 8 REFINED EXISTING
# ===========================================================================

# --- NEW P3 #1: Call schedule generator ---
write_prompt(f"{P3}/rotations/call-schedule-generator.md",
    {"title":"Call schedule generator with constraints","pillar":"educational-operations",
     "event_type":"rotation","audience":"program-director","difficulty":"intermediate",
     "time_to_use":">10min","visual":"text-only",
     "tags":"call-schedule, planning, constraints","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Generates a fair call schedule respecting constraints (vacations, time-off requests, ACGME work-hour rules, fairness across residents, weekend equity). This is the chief resident task that consumes hours and produces resentment when done poorly.

## When to use it

When you're building the next call cycle — typically a quarterly or semi-annual task. Best done with all constraint information collected upfront.

**Not for:** ad hoc swap requests (use a swap tool), schedules without explicit constraints (the prompt requires them), or replacing your program's institutional scheduling system.

## The prompt

```
You are generating a call schedule that must be fair and constraint-respecting. Show your work — explain the trade-offs you made and where the schedule is tight.

## What I'm providing

- **Time period:** [start date to end date, e.g., "January 1 to March 31, 2027"]
- **Call type:** [pathology call / CP-only call / weekend call / etc.]
- **Residents available:** [list with PGY level for each]
- **Per-resident constraints:**
  - Vacation requests (specific dates)
  - Conference / educational leave
  - Hard "no" dates (interviews, life events)
  - Soft preferences (avoid weekends, prefer back-to-back, etc.)
- **Institutional rules:**
  - ACGME work hour limits applicable
  - Maximum consecutive call days
  - Mandatory rest days
  - Weekend frequency caps
- **Total slots to fill:** [calculate from time period × shifts per day]

## What to produce

### The schedule

A day-by-day table:
| Date | Day | Resident | Notes |

### Fairness check

- Total call days per resident
- Weekend days per resident
- Holiday days per resident (if applicable)
- Variance flag: which residents are over- or under-allocated and by how much

### Constraint compliance check

For each resident, confirm:
- All hard "no" dates respected
- Vacation dates respected
- Work-hour rules not violated
- Maximum consecutive days not exceeded

### Tradeoffs I should know about

- **Where the schedule is tight** (any constraint I came close to violating)
- **Where I had to compromise** (soft preferences I couldn't accommodate, and why)
- **What additional flexibility from a resident would most improve the schedule**

### Swap-friendly notes

For each resident, identify the dates that would be easiest for them to swap with someone if a swap request comes in later.

## Hard rules

- **All hard constraints respected.** No exceptions, no "almost."
- **Work-hour rules not violated.** Flag if my stated constraints are inconsistent with ACGME rules.
- **Fairness calculation must be honest.** If the schedule is unfair to one resident, say so directly.
- **Do not silently relax constraints to make the math work.** Tell me what's blocking and ask for adjustment.

## What I will NOT accept

- A schedule that violates a hard constraint (even one)
- Hidden compromises ("almost equal weekends")
- A schedule generated without flagging the tradeoffs
```

## Expected output

A complete schedule + fairness check + constraint compliance check + tradeoffs + swap-friendly notes.

## Common failure modes

- **Hard constraint violated silently.** Verify every constraint manually before publishing.
- **Fairness math hidden.** Push for explicit per-resident totals.
- **Schedule that "works on average" but is unfair to one resident.** Push back.

## Required human verification

- **Verify every hard constraint against the schedule.** The model can miss things.
- **Verify ACGME work-hour rules** for your specialty and PGY level.
- **Share the draft with affected residents** before finalizing. They will spot issues you and the model missed.
- **Document your fairness methodology** so you can defend the schedule.

## Best model and why

**Claude Opus 4.7** — multi-constraint scheduling with fairness reasoning is hard. Opus produces more honest tradeoff analysis than Sonnet, which tends to silently relax constraints.
""")

# --- NEW P3 #2: Lab incident debrief ---
write_prompt(f"{P3}/workshops/lab-incident-debrief.md",
    {"title":"Lab incident debrief template","pillar":"educational-operations","event_type":"workshop",
     "audience":"faculty","difficulty":"advanced","time_to_use":">10min","visual":"text-only",
     "tags":"incident, debrief, just-culture, quality","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

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
""")

# --- NEW P3 #3: Visiting professor invitation ---
write_prompt(f"{P3}/conferences-and-journal-clubs/visiting-professor-invitation.md",
    {"title":"Visiting professor invitation letter","pillar":"educational-operations","event_type":"conference",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"visiting-professor, invitation, hospitality","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Drafts the formal invitation letter to a visiting professor for a grand rounds talk or visiting professorship. Substantive enough that the invitee takes it seriously, gracious enough that the relationship starts well, specific enough that they understand exactly what's being asked.

## When to use it

When you're hosting a visiting professor or grand rounds speaker and need to send the formal invitation 3-6 months ahead. Useful both for first-time invitations and for invitations to people you know well (different tone for each).

**Not for:** casual speaker requests (use a short email), CME-accredited industry-funded events (those have specific compliance requirements), or follow-up communications.

## The prompt

```
You are drafting an invitation letter to a visiting professor. Substantive but not effusive. Specific enough that they know exactly what's being asked.

## What I'm inviting

- **Speaker:** [name, current title and institution]
- **Relationship to invitee:** [I don't know them / met at a conference / mentor relationship / longstanding colleague]
- **Event:** [grand rounds / visiting professorship / named lecture / conference keynote]
- **Date and location:** [specific date, my institution]
- **Honorarium and travel:** [what's offered]
- **Format:** [1-hour grand rounds / half-day visit / full-day visit with multiple activities]
- **Why this speaker specifically:** [their expertise that matches our need — be specific]
- **What I want them to talk about:** [topic + level of audience]
- **The signer of the letter:** [me / department chair / program director]

## Letter structure (one page, ~300-400 words)

### Paragraph 1: Opening + invitation
- Formal address (Dr. [Last Name])
- The invitation, stated clearly in the first 1-2 sentences (event, date)
- A specific reason WHY this person — referencing their work, not generic praise

### Paragraph 2: What's being asked
- The talk topic with specificity (not just "anything in your area of expertise")
- Audience description (how many, what level)
- Logistics: location, format, audience composition

### Paragraph 3: What's offered
- Honorarium (named, even if "we'll provide an honorarium" with details to follow)
- Travel and accommodation logistics
- Any additional activities (sign-out visit, meeting with residents, dinner with faculty)

### Paragraph 4: Practical next steps
- What I'm asking them to confirm
- Date by which I'd appreciate a response
- Who they'll work with on logistics
- An offer to chat by phone if they have questions

### Closing
- Warm but professional
- Signature with full title and institution

## Tone

- Substantive — they should believe we've thought about why we're inviting them
- Not effusive — no "honored," "thrilled," "exceptional"
- Specific — generic invitations get declined
- Respectful of their time

## Hard rules

- **One page maximum.** Long letters signal you're padding.
- **Specific 'why this speaker'** in paragraph 1 — referencing their work, not generic praise.
- **Honorarium and travel offer mentioned even if details follow.** Avoiding it implies stinginess.
- **Specific topic suggestion.** "Anything in your area" is lazy; "we'd love your take on [specific question we're wrestling with]" is generous.

## What I will NOT accept

- A letter that could have been sent to any speaker
- Effusive language ("honored," "thrilled," "tremendously excited")
- Vague topic suggestion
- Missing logistics
```

## Expected output

A one-page formal invitation letter (~300-400 words) ready to send.

## Common failure modes

- **Generic.** Push back: "What specifically about this person?"
- **Effusive.** Push back: "Less 'honored,' more substance."
- **Vague topic.** Push back.

## Required human verification

- Verify the speaker's current title, institution, and preferred form of address.
- If institutional honorarium policies apply, confirm the offered amount complies.
- For CME-accredited events, additional disclosure language may be required.

## Best model and why

**Claude Sonnet 4.6** — formal correspondence with specific calibration is Sonnet's strength.
""")

# --- NEW P3 #4: IRB protocol for QI / educational research ---
write_prompt(f"{P3}/courses/irb-qi-protocol.md",
    {"title":"IRB protocol for QI or educational research","pillar":"educational-operations",
     "event_type":"course","audience":"faculty","difficulty":"advanced","time_to_use":">10min","visual":"text-only",
     "tags":"irb, qi, educational-research, regulatory","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Drafts a starting IRB protocol for an educational intervention or quality improvement study — the type most pathology educators do. Walks through whether it's QI or research, the appropriate level of IRB review (exempt / expedited / full board), the required protocol elements, and the data/consent language.

The hardest decision this prompt clarifies: **is your project QI or research?** The classification determines everything else.

## When to use it

When planning an educational study (e.g., effectiveness of a new curriculum), a QI project (e.g., reducing critical-value response time), or a scholarship project that will be published. Best done early in project design, before data collection starts.

**Not for:** clinical research with patient subjects (different category — work with your IRB directly), studies involving identifiable patient data (different framework), or as a substitute for actual IRB review (this generates a starting protocol, not a finished submission).

## The prompt

```
You are helping me draft a starting IRB protocol for an educational or QI project. The first thing to settle is whether this is QI or research. The classification changes everything that follows.

## What I'm planning

- **Project name:** [brief]
- **Project description:** [what I'm doing and why]
- **Setting:** [pathology residency / fellowship / faculty development / multi-institutional]
- **Subjects:** [residents / faculty / patients / specimens / records]
- **Data I'll collect:** [pre/post test scores, survey responses, observed behaviors, retrospective chart review, etc.]
- **Will results be published or presented externally?** [yes / no / unsure]
- **Institutional IRB:** [name + general framework — whether they use OHRP Common Rule]

## STEP 1: QI vs Research classification

Walk me through this decision explicitly. Key questions per OHRP guidance:

1. Is the intent to develop or contribute to **generalizable knowledge** (research) vs improve a specific local process (QI)?
2. Will findings be **published or presented externally** in a way intended to inform practice beyond this institution?
3. Is there **randomization or control** that wouldn't otherwise occur?
4. Is there **deviation from accepted practice** to test a hypothesis?

Based on my answers, classify as:
- **QI only** — may not require IRB review at all, but often requires departmental QI committee review
- **QI with planned dissemination** — may require IRB review; some institutions have a "QI with publication intent" pathway
- **Research** — requires IRB review

If you're uncertain, recommend I consult my institutional IRB before designing the rest.

## STEP 2: If research — IRB review level

Walk through likely classification:
- **Exempt** — most educational research with no/minimal risk: surveys, educational tests, observational of normal educational practices
- **Expedited** — research involving minor risk: retrospective record review with PHI, prospective educational intervention
- **Full board** — vulnerable populations, more than minimal risk

For my project specifically, recommend a likely level with rationale.

## STEP 3: Protocol elements

For the appropriate review level, draft each required section:

1. **Specific aims** (1-2 sentences each, measurable)
2. **Background and significance** (~1 paragraph)
3. **Study design and methods** (specific to my project)
4. **Subjects** (inclusion/exclusion, recruitment, sample size with justification)
5. **Data collection** (what, how, by whom)
6. **Data security and confidentiality** (where data lives, who has access, retention plan)
7. **Risks** (specific to subject type — residents have different risks than patients)
8. **Benefits** (to subjects, to the field — be honest)
9. **Consent** (consent form text OR rationale for waiver of consent)
10. **Dissemination plan** (publication, presentation, internal report)

## STEP 4: Common pitfalls for educational research

Flag the 2-3 most common reasons educational research protocols get returned for revision at your IRB.

## Hard rules

- **Be honest about classification.** If a project crosses into research, say so.
- **Recommend consultation with the institutional IRB early** for ambiguous cases.
- **Do NOT generate fake IRB-approved language.** This is a STARTING draft for me to review with my IRB.
- **Acknowledge that institutional policies vary.** What's exempt at one institution may require expedited review at another.

## What I will NOT accept

- A protocol that confidently states the review level without acknowledging institutional variation
- Generic protocol language that doesn't engage with my specific project
- Skipping the QI vs research decision step
- Claims about IRB approval pathways without sourcing
```

## Expected output

A QI/research classification recommendation + IRB review level recommendation + 10-section starting protocol + common pitfalls. Length 1000-1500 words.

## Common failure modes

- **Confidently mis-classifies QI as research** or vice versa. Push back: "Walk through the criteria explicitly."
- **Generic protocol language.** Push for specificity to your project.
- **Skips institutional variation acknowledgment.** Push back.

## Required human verification

- **Consult your IRB.** This prompt generates a starting draft, not an approval. Your IRB's specific requirements may differ.
- **For research that might involve protected health information, consult your privacy officer.** HIPAA implications are project-specific.
- **For multi-institutional projects, all involved IRBs may need to approve.** Don't assume reciprocity.

## Best model and why

**Claude Opus 4.7** — IRB protocol drafting requires depth and regulatory awareness. Opus is more careful about acknowledging uncertainty and institutional variation than Sonnet.
""")

# --- NEW P3 #5: Promotion / portfolio narrative ---
write_prompt(f"{P3}/courses/promotion-portfolio-narrative.md",
    {"title":"Promotion / portfolio teaching narrative","pillar":"educational-operations","event_type":"course",
     "audience":"faculty","difficulty":"advanced","time_to_use":">10min","visual":"text-only",
     "tags":"promotion, portfolio, teaching-narrative, high-stakes","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Drafts the "teaching and education" narrative section of a faculty promotion portfolio. This is the high-stakes annual writing that committee members read to evaluate teaching contributions for promotion to associate or full professor.

The hardest discipline: this is a NARRATIVE, not a list. The narrative connects teaching activities to a coherent identity as an educator — the committee is evaluating whether you ARE an educator, not whether you've done teaching activities.

## When to use it

When preparing your promotion portfolio (annual update or formal promotion year). Best done with your CV in hand, your teaching evaluations available, and ideally with a mentor reviewing the draft.

**Not for:** writing your CV (different format), short bios (different scope), or as a substitute for working with your institution's faculty affairs office on portfolio requirements.

## The prompt

```
You are drafting the "teaching and education" narrative for my promotion portfolio. This is a high-stakes narrative — the committee reads it to evaluate whether I am an EDUCATOR, not whether I've done teaching activities.

## Critical first step

Before drafting, ask me at least 4 questions to elicit specific anecdotes and a coherent educator identity. Do NOT start writing the narrative until you have substantive answers. Generic teaching prose without specific anecdotes is the most common failure mode for promotion narratives.

## What I'll provide

- **Promotion target:** [associate professor / full professor / clinician-educator track / other]
- **My institution's framework:** [educator portfolio required / narrative only / mixed]
- **Time period covered:** [years]
- **Teaching activities to draw from:**
  - **Formal courses or rotations taught:** [list with role and dates]
  - **Mentorship:** [residents, fellows, faculty I've mentored]
  - **Curriculum development:** [what I created or substantially revised]
  - **Educational scholarship:** [publications, presentations, grants]
  - **Educational leadership:** [course director, program director, education committee roles]
- **Teaching evaluations / outcomes data:** [what's available]
- **My institution's word limit:** [if specified]

## The 4+ questions you must ask before drafting

1. **The identity question:** "If a committee member could describe your contribution as an educator in one sentence after reading the narrative, what would that sentence be? Don't tell me what you DO — tell me what you ARE in this domain."

2. **The anecdote question:** "Give me one specific moment in the past 3 years that captures what you bring to teaching. A specific learner, a specific course design decision, a specific moment of impact. Details I can use to ground a paragraph."

3. **The evolution question:** "How have you grown as an educator since your last review? What can you do now that you couldn't 3 years ago?"

4. **The differentiation question:** "What distinguishes your teaching contribution from a colleague at your rank who is also doing teaching? Be honest — committees read many portfolios."

If my answers are generic, push back for specifics before drafting.

## Narrative structure (typically 800-1500 words depending on institutional norms)

### Opening (1 paragraph)
The identity statement — what kind of educator you are. Anchored in a specific scope (e.g., "I have built my educational contribution around teaching diagnostic reasoning to early-stage CP residents through structured case-based instruction"). Not a list of activities; an identity claim.

### Teaching practice (2-3 paragraphs)
- What you teach, to whom, in what formats
- Anchored in one or two SPECIFIC examples from the anecdotes I gave
- Tie to outcomes (learner feedback, performance data) where available

### Curriculum and innovation (1-2 paragraphs)
- What you've built or substantially redesigned
- The specific need it addressed
- Evidence it worked

### Mentorship (1 paragraph)
- Specific mentees and where they are now (de-identified if appropriate)
- Your approach to mentoring as a deliberate practice, not just an activity

### Educational scholarship (1 paragraph if applicable)
- Publications, presentations, grants
- The thread connecting them — what's the educational question you're pursuing?

### Leadership and field contribution (1 paragraph if applicable)
- Roles within the institution and externally
- How your work influences practice beyond your institution

### Forward statement (1 paragraph)
- Where you're going in the next 3-5 years
- Specific, not aspirational

## Hard rules

- **Identity first, activities second.** A list of activities without identity reads as a CV.
- **Specific anecdotes ground every claim.** Generic competence statements are the failure mode.
- **Outcomes where available.** Evaluations, learner performance, dissemination — quantify where you can.
- **Honest about scope.** Promotion committees recognize inflated claims. Stay honest about your level of contribution.
- **Forward statement is specific.** "I plan to continue contributing to medical education" is the worst version; "I plan to develop and validate a structured assessment tool for diagnostic reasoning in CP, partnering with [colleague/group]" is the right version.

## What I will NOT accept

- A list of activities masquerading as a narrative
- Generic anecdotes ("I work hard with my residents")
- Outcomes claimed without evidence
- A forward statement that's actually a wish list
```

## Expected output

The 4+ questions in the first response; the structured narrative (~800-1500 words depending on institutional norms) in the second response after you provide answers.

## Common failure modes

- **Activity-list instead of identity.** Push back: "What's the identity?"
- **Generic anecdotes.** Push back for specific learners, specific moments.
- **Quantified outcomes claimed without evidence.** Verify.

## Required human verification

- **Run by a mentor at your institution** — they know what your specific promotion committee weighs.
- **Verify all dates, titles, and outcomes** against your CV before submitting.
- **Check institutional word limit and format requirements** — these vary considerably.
- **If you're being considered for a track requiring specific evidence (clinician-educator track, etc.), confirm the narrative addresses the required dimensions.**

## Best model and why

**Claude Opus 4.7** — high-stakes narrative writing with identity-level claims requires depth. Sonnet produces more generic prose; Opus is materially better at the identity-vs-activity distinction.
""")

# --- NEW P3 #6: Conference abstract for medical education ---
write_prompt(f"{P3}/conferences-and-journal-clubs/medical-education-abstract.md",
    {"title":"Conference abstract for medical education research","pillar":"educational-operations",
     "event_type":"conference","audience":"faculty","difficulty":"intermediate","time_to_use":">10min",
     "visual":"text-only","tags":"abstract, medical-education-research, scholarship",
     "verified_models":"TODO","best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Drafts a conference abstract for medical education research (AAMC, AMEE, society educational sections). Medical education abstracts follow different conventions than clinical research abstracts — different sections, different evidence standards, different ways of framing innovation.

## When to use it

When submitting to a medical education conference. Best done with your project data in hand and a clear sense of which conference's conventions apply.

**Not for:** clinical research abstracts (different conventions), QI abstracts (different framework), or as a substitute for your IRB-approval status (verify before submitting).

## The prompt

```
You are drafting a medical education conference abstract. Med-ed abstracts have different conventions than clinical research — the framing and evidence standards are specific.

## What I'm submitting

- **Conference:** [name + abstract category if applicable]
- **Word limit:** [check the conference guidelines]
- **Abstract type:** [original research / innovation report / curriculum description / scholarly perspective]
- **Conference's preferred structure:** [check guidelines — usually structured with named sections]

## My project

- **Background / problem:** [the educational gap your project addresses]
- **Setting:** [where this happened — institution, level of learners, scale]
- **Intervention or innovation:** [what you did]
- **Evaluation approach:** [how you measured impact]
- **Results:** [what you found — quantitative + qualitative]
- **Discussion / implications:** [what others can take from this]
- **IRB / ethics status:** [exempt / expedited / approved / not applicable]

## What to produce

### The abstract

In the conference's required structure. Common med-ed structures:

**Research abstract (200-350 words):**
- **Background / Problem**
- **Educational Context** (setting + learners)
- **Innovation / Intervention**
- **Evaluation Methods**
- **Results**
- **Discussion / Significance**

**Innovation report (200-350 words):**
- **Statement of Problem**
- **Approach** (what you did, how it was novel)
- **Outcomes** (what evidence you have it worked)
- **Practical Lessons / Implications**

### Title

3-5 candidate titles. Med-ed titles tend to be longer and more descriptive than clinical research titles. Avoid clever titles that obscure content.

### Keywords

5-7 keywords for indexing.

### A note on what's missing

If your project has gaps (small sample, no comparison group, limited follow-up), name them explicitly and suggest framing that's honest without being self-defeating. Reviewers respect acknowledged limitations.

## Hard rules

- **Match the conference's required structure exactly.** Submissions get rejected for format issues.
- **Word count within limit.** Count it.
- **Specific outcomes, not vague claims.** "Improved learning" is not an outcome; "30% improvement in post-test scores (p<0.05)" is.
- **Honest about limitations.** Don't oversell.
- **IRB status mentioned where applicable** (some conferences require it in the abstract).

## What I will NOT accept

- Abstracts that overrun word limits
- Vague outcomes
- Oversold conclusions
- Generic discussion section that could apply to any project
```

## Expected output

The structured abstract + 3-5 candidate titles + keywords + limitation framing. Total length depends on word limit.

## Common failure modes

- **Word count overrun.** Verify.
- **Vague outcomes.** Push for specific numbers.
- **Conclusion overreach.** Pull back to what the evidence supports.

## Required human verification

- Verify all reported numbers against your actual data.
- Confirm conference's required structure and word limit haven't changed.
- Have a colleague who's served as a med-ed conference reviewer read the draft.
- Verify IRB status language matches your actual approval.

## Best model and why

**Claude Sonnet 4.6** — structured short-form writing with specific conventions is Sonnet's strength.
""")

# --- NEW P3 #7: Rotation block scheduling ---
write_prompt(f"{P3}/rotations/rotation-block-scheduling.md",
    {"title":"Rotation block scheduling across an academic year","pillar":"educational-operations",
     "event_type":"rotation","audience":"program-director","difficulty":"advanced","time_to_use":">10min",
     "visual":"text-only","tags":"rotation-schedule, annual-planning, constraints",
     "verified_models":"TODO","best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Generates a year-long rotation block schedule respecting required experiences, board prep timing, elective preferences, and constraints (vacation, conference, life events). Different from call scheduling — this is the "which resident is on which rotation each block" annual puzzle.

## When to use it

Annually when planning the next academic year's rotation assignments. Best done after collecting resident preferences and constraints but before the year begins.

**Not for:** call scheduling (different prompt), ad hoc rotation swaps (different process), or programs where rotation assignments follow a strict algorithm without flexibility.

## The prompt

```
You are generating a year-long rotation block schedule. Respect required experiences, board prep timing, and resident constraints. Be honest about tradeoffs.

## What I'm providing

- **Academic year:** [July 2027 - June 2028]
- **Block structure:** [number of blocks, length of each — usually 13 four-week or 12 four-week blocks]
- **Residents:** [list with PGY level for next year]
- **Required rotations per PGY level:**
  - PGY-1: [list with minimum blocks each]
  - PGY-2: [list]
  - PGY-3: [list]
  - PGY-4: [list]
- **Resource constraints:** [maximum residents per rotation per block, e.g., "max 2 on autopsy", "max 1 on molecular"]
- **Resident preferences:**
  - Elective preferences (ranked)
  - Board prep block requests (if applicable)
  - Vacation block requests
  - Hard conflicts (interviews, life events, conferences)
- **Program priorities:** [graduating resident board prep, fellowship interview accommodation, etc.]

## What to produce

### The grid

Block-by-block, resident-by-resident schedule:

| Block | Dates | Resident 1 | Resident 2 | Resident 3 | ... |

### Required-experience compliance check

For each resident, confirm:
- All required rotations completed by end of year (or PGY level)
- Minimum blocks met for each
- Sequencing makes sense (e.g., autopsy before sign-out independence)

### Resource compliance check

For each block, confirm:
- Resource caps not exceeded (max residents per rotation)
- No critical rotations unstaffed

### Preference accommodation summary

Per resident:
- Electives received vs requested
- Vacation blocks granted vs requested
- Board prep timing
- Hard conflicts respected

### Tradeoffs I should know about

- Which residents got less of their preferences and why
- Where I had to make compromises on sequencing
- What additional flexibility would most improve the schedule
- Which residents I'd talk to first about adjustments

### Comparison to fairness baseline

How does this schedule compare to a baseline where preferences were ignored and rotations were assigned alphabetically? Useful to show your CCC the schedule isn't arbitrary.

## Hard rules

- **Required rotations met for every resident.** No exceptions.
- **Resource caps respected.** No exceptions.
- **Hard conflicts respected.** No exceptions.
- **Be honest about preference accommodation.** Don't claim "preferences met" when they weren't.
- **Flag if my stated constraints are mathematically impossible to satisfy** rather than silently relaxing them.

## What I will NOT accept

- A schedule that misses a required rotation for any resident
- A schedule that exceeds resource caps
- Hidden preference compromises
- Schedule generated without flagging tradeoffs
```

## Expected output

Schedule grid + required-experience check + resource check + preference summary + tradeoffs + fairness comparison.

## Common failure modes

- **Required rotation missed silently.** Verify manually.
- **Resource cap exceeded.** Verify.
- **Hidden preference compromises.** Push for explicit comparison.

## Required human verification

- **Verify every required rotation count manually.** The model can miscount.
- **Share the draft with residents** before publishing — they'll spot issues.
- **Verify against ACGME and your program's specific requirements.**
- **Document fairness methodology** for the CCC.

## Best model and why

**Claude Opus 4.7** — multi-constraint annual scheduling with fairness reasoning rewards Opus's depth.
""")

# ===========================================================================
# REFINED EXISTING P3 PROMPTS (8 highest-value)
# ===========================================================================

# --- Refined: faculty-feedback-summary ---
write_prompt(f"{P3}/workshops/faculty-feedback-summary.md",
    {"title":"Faculty feedback summary email","pillar":"educational-operations","event_type":"workshop",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"feedback, debrief, themes","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Converts raw attendee feedback into a faculty debrief email organized by theme, ordered by frequency, with honest separation of signal vs noise and ranked suggested actions.

## When to use it

1-2 weeks after the event, when feedback has come in but faculty are still engaged enough to act on it.

**Not for:** real-time feedback during the event, individual feedback to a specific faculty member (different conversation), or contexts where faculty don't want the unvarnished read.

## The prompt

```
You are converting raw attendee feedback into a faculty debrief email. Be honest about negative themes; don't minimize. Anonymize quotes.

## What I'm providing

- **Event and date:** [name + when]
- **Raw feedback:** [paste survey responses, exit tickets, post-event comments]
- **Response rate:** [N respondents out of M attendees]
- **Audience to send debrief to:** [all faculty involved / leadership only / etc.]

## Structure

### 1. One-paragraph summary
Overall reception, response rate, top-level themes (positive AND negative).

### 2. What worked (themes, ordered by frequency)
Paraphrased example quotes (preserving anonymity).

### 3. What didn't work (themes, ordered by frequency)
Same structure as #2. Do NOT minimize.

### 4. Signal vs noise
Which comments represent systemic issues vs one-off complaints. Be honest about both — but don't dismiss minority voices that point to real issues.

### 5. Suggested actions for next iteration
3-5 specific changes, ranked by ease × impact.

### 6. Response rate and selection bias note
Who responded, who didn't, what that means for interpretation.

## Hard rules

- **Quote anonymity.** If a quote could identify the respondent (small group, distinctive phrasing), paraphrase further.
- **Do NOT embellish quotes.** That erodes faculty trust.
- **Do NOT minimize negative themes.** Selective reporting is detected.
- **Actions must be specific.** Generic "improve communication" is not actionable.

## What I will NOT accept

- Selective reporting favoring positive feedback
- Embellished or smoothed quotes
- Actions without owners or specifics
- Quotes that could identify respondents
```

## Expected output

A debrief email with 6 sections, paraphrased quotes preserving anonymity, ranked actions.

## Common failure modes

- **Positive bias.** Push back: "Did I miss negative themes?"
- **Quote embellishment.** Verify against raw text.
- **Aspirational actions.** Push for specifics.

## Required human verification

- Re-read against raw feedback — confirm negative themes preserved.
- Anonymize ALL quotes — including paraphrased versions.
- Run by one trusted faculty member before sending widely.

## Best model and why

**Claude Opus 4.7** — theme synthesis from raw feedback rewards depth. Opus is better at signal-vs-noise distinction.
""")

# --- Refined: evaluation-rubric (rotations) ---
write_prompt(f"{P3}/rotations/evaluation-rubric.md",
    {"title":"Rotation evaluation rubric","pillar":"educational-operations","event_type":"rotation",
     "audience":"program-director","difficulty":"advanced","time_to_use":">10min","visual":"text-only",
     "tags":"evaluation, rubric, milestone-alignment","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## What this prompt does

Generates a milestone-aligned evaluation rubric with behaviorally-anchored level descriptors. The key discipline: anchors describe OBSERVABLE BEHAVIORS, not personality traits, and they GENUINELY DISCRIMINATE between levels (not just sound positive at every level).

## When to use it

When piloting milestone-anchored evaluations or replacing a generic form. Should be reviewed by your CCC before deployment.

## The prompt

```
You are generating a rotation evaluation rubric. Anchors must be observable behaviors and must genuinely discriminate between levels. "Demonstrates competence" at every level is the failure mode.

## What I'm building

- **Rotation:** [name + duration]
- **PGY level:** [target level]
- **Milestone document version:** [your program's current version]
- **Number of dimensions:** [usually 5-7]
- **Rater time budget:** [target — usually 15 min]

## What to produce

### 5-7 dimensions

Each mapped to a milestone sub-competency this rotation is positioned to assess. Mix of knowledge/technical and professional/interpersonal.

### Per-dimension structure

For each dimension:
- Name
- Milestone sub-competency mapping
- **5 levels with behavioral anchors:**

Each anchor must describe an OBSERVABLE BEHAVIOR. Examples:
- BAD: "Demonstrates competence in interpreting routine cases"
- GOOD: "Independently formulates a workup plan for routine cases and seeks supervision appropriately for complex ones; escalation decisions match attending expectations >80% of the time"

- **Narrative comment prompt** to help raters write specific feedback ("Cite one specific case or moment where you observed this dimension")

### Quality controls

- Each dimension independently rateable (no overlap)
- 5 levels genuinely differentiate
- Behavioral anchors, not personality traits
- "Unable to assess" option for each dimension

### Time and observation requirements

- Estimated rater time
- Minimum observations needed to assign each dimension fairly

## Hard rules

- **Observable behaviors only.** "Shows enthusiasm" is not an anchor.
- **Genuine differentiation.** If levels 3, 4, 5 all sound positive in different ways without distinction, the anchors are too soft.
- **Independent dimensions.** "Writing quality" and "organization" overlap; merge or rewrite.
- **"Unable to assess" option non-negotiable.** Otherwise raters default to 3/5 for things they didn't observe.

## What I will NOT accept

- Personality-trait anchors
- Anchors that all sound positive
- Overlapping dimensions
- Missing "unable to assess" option
```

## Expected output

5-7 dimensions, each with 5-level behaviorally-anchored descriptors, narrative prompts, quality controls.

## Common failure modes

- **Anchors that all sound positive.** Push back: "Differentiate."
- **Personality traits.** Push back.
- **Overlapping dimensions.** Push to merge or rewrite.

## Required human verification

- Run by CCC chair before use.
- Pilot with two raters scoring the same resident — check inter-rater agreement.
- Verify milestone mapping is current.

## Best model and why

**Claude Opus 4.7** — behavioral anchors that genuinely discriminate require care. Sonnet anchors tend toward all-positive.
""")

# --- Refined: expectations-doc ---
write_prompt(f"{P3}/rotations/expectations-doc.md",
    {"title":"Rotation expectations document","pillar":"educational-operations","event_type":"rotation",
     "audience":"program-director","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"expectations, syllabus, milestones","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Generates a rotation expectations document mapping objectives to milestones, specifying daily/weekly responsibilities, defining the supervision model, and naming the evaluation criteria. Lives in the rotation handbook.

## The prompt

```
You are generating a rotation expectations document. Every objective must map to a specific milestone sub-competency code. Generic "will demonstrate competence" doesn't help the CCC.

## What I'm providing

- **Rotation:** [name + duration]
- **PGY level:** [target]
- **Service context:** [your institution's service]
- **Milestone document version:** [current]
- **Supervision model:** [autonomy gradient — how it changes start to end of rotation]
- **Evaluation framework:** [rubric or form name]

## What to produce

7 sections:

1. **Rotation overview** (2-3 sentences) — place in curriculum, prerequisites, what it builds toward
2. **Learning objectives** (5-8) — milestone-aligned, "will be able to" language with measurable verbs
3. **Daily responsibilities** — typical day's required activities
4. **Weekly responsibilities** — recurring less than daily
5. **End-of-rotation requirements** — deliverables, assessments
6. **Supervision model** — autonomy level at start, at end, triggers for attending involvement
7. **Evaluation criteria** — framework named, when evaluated

Specify any institutional-specific terms and define on first use.

## Hard rules

- **Every objective maps to a specific milestone sub-competency code.**
- **Measurable verbs only** (no "understand," "know").
- **Supervision gradient explicit.**
- **Verify milestone codes against the current version.**

## What I will NOT accept

- Vague objectives ("will demonstrate competence")
- Missing milestone mapping
- Vague supervision model
```

## Expected output

A 7-section document for the rotation handbook.

## Required human verification

- Verify milestone codes against current document.
- Run by rotation director and a recent rotator.
- Confirm supervision model matches institutional policy.

## Best model and why

**Claude Sonnet 4.6** — structured doc with milestone mapping is Sonnet's range.
""")

# --- Refined: syllabus ---
write_prompt(f"{P3}/courses/syllabus.md",
    {"title":"Course syllabus","pillar":"educational-operations","event_type":"course",
     "audience":"faculty","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"syllabus, course, policies","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":"2026-05-17"},
    """## What this prompt does

Generates a complete course syllabus with weekly schedule, objectives, assessment plan, resources, policies (including an EXPLICIT AI use policy — not silence), and communication norms.

## The prompt

```
You are generating a course syllabus. Every week must have a topic + outcome. AI use policy must be explicit — silence is not a policy.

## What I'm providing

- **Course name:** [name]
- **Duration:** [N weeks]
- **Audience:** [target learners]
- **Meeting time/location:** [if applicable]
- **Format:** [in-person / hybrid / async]
- **Prerequisites:** [if any]
- **My institution's specific requirements:** [CME accreditation, etc.]

## What to produce

8 sections:

1. **Course title, instructor(s), meeting info**
2. **Course description** (3-5 sentences) — scope, prerequisites, place in curriculum
3. **Learning objectives** (4-7) — course-level, "will be able to" with measurable verbs
4. **Weekly schedule** — each week with topic, readings, in-class activity, post-class assignment, outcome
5. **Assessment plan** — formative + summative, weighting if graded
6. **Resources** — required and recommended with full citations
7. **Policies**:
   - Attendance
   - Makeup work
   - Accommodations
   - **AI use policy — explicit, not silence**
   - Academic integrity
8. **Communication norms** — how to reach instructors, response times

For each weekly topic, name ONE outcome demonstrating mastery.

## Hard rules

- **AI use policy explicit.** Specify what's encouraged, what requires disclosure, what's prohibited.
- **Every week has a measurable outcome.**
- **All resources verified.**
- **Match institutional formality** (CME = more formal; didactic series = less).

## What I will NOT accept

- Silent or boilerplate AI use policy
- Weekly topics without outcomes
- Assessment plan disconnected from objectives
```

## Expected output

Complete syllabus, 5-8 pages, ready for curriculum committee review.

## Required human verification

- Verify all resource citations.
- Check institutional policies for AI use match your statement.
- Confirm assessment plan aligns to objectives.

## Best model and why

**Claude Sonnet 4.6** — structured doc with explicit policies. The AI policy is the genuinely new part; spend time refining it.
""")

# --- Refined: assignment-grading-rubric ---
write_prompt(f"{P3}/courses/assignment-grading-rubric.md",
    {"title":"Assignment grading rubric","pillar":"educational-operations","event_type":"course",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"rubric, grading, assessment","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## The prompt

```
You are generating a grading rubric. Dimensions must be independently assessable. If two dimensions could be confused, merge or rewrite.

## What I'm providing

- **Assignment:** [name + brief description]
- **Course:** [name + audience]
- **Expected length/format:** [pages/slides/video min]
- **Learning objectives assessed:** [from syllabus]
- **Point total:** [if graded numerically]

## What to produce

### 4-6 dimensions

Each capturing what "good" looks like. Independently assessable (don't combine content quality and writing).

### 4 levels per dimension

Exemplary / Proficient / Developing / Needs Substantial Work — each with a behavioral or product descriptor (what would I observe in the artifact?).

### Point weighting

Per dimension, weighted by impact on objectives.

### Feedback prompts

Per dimension, prompts to help graders write specific narrative feedback ("Cite one moment where the student demonstrated X").

### Common pitfalls

Type-specific failure modes the rubric captures.

### Estimated grading time

Per submission, in minutes.

## Hard rules

- **Independently assessable dimensions.**
- **4 levels that genuinely differentiate** — not all positive.
- **Weighting reflects actual importance.**
- **Pitfalls specific to assignment type.**

## What I will NOT accept

- Overlapping dimensions
- All-positive level descriptors
- Generic feedback prompts
```

## Expected output

4-6 dimensions × 4 levels with prompts, pitfalls, time estimate.

## Required human verification

- Grade one sample submission with the rubric, then have a colleague grade independently. Refine where you disagree.
- Verify rubric assesses stated objectives.

## Best model and why

**Claude Opus 4.7** — sharp distinctions between levels reward depth.
""")

# --- Refined: journal-club-packet ---
write_prompt(f"{P3}/conferences-and-journal-clubs/journal-club-packet.md",
    {"title":"Journal club packet generation","pillar":"educational-operations","event_type":"conference",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"journal-club, packet, paper-engagement","verified_models":"TODO",
     "best_model":"Claude Opus 4.7 with paper attached","last_updated":"2026-05-17"},
    """## The prompt

```
You are generating a journal club packet. Quality depends entirely on having the paper text. Refuse if you don't have it.

## Honesty check FIRST

Do you have the full paper text? If not, STOP. Fabricated packets are worse than no packet.

## What I'm providing

- **Paper:** [citation or attached PDF]
- **Audience:** [PGY level + faculty mix]
- **Discussion format:** [traditional / debate / structured critique]

## Packet structure (2-3 pages)

1. **Background paragraph** — state of the field before this paper
2. **Study summary** — design, population, key results with specific numbers (neutral framing)
3. **Methodologic critique** — 2 specific strengths + 2-3 specific limitations using the appropriate reporting guideline framework
4. **"So what"** — what could this change about practice + barriers to that change
5. **5 discussion questions** ordered from concrete to contested:
   - Methods/numbers
   - Generalizability
   - Comparison to prior literature
   - Practice change
   - Genuinely contested
6. **Attendee prep note** — what to think about before arriving

## Hard rules

- Refuse if no paper text
- Specific numbers from paper
- Contested question must be genuinely contested
- No PHI

## What I will NOT accept

- Packet from title alone
- Fabricated numbers
- Contested question with obvious answer
```

## Required human verification

- Verify all numbers against paper.
- Pre-test contested question with colleague.

## Best model and why

**Claude Opus 4.7 with paper attached** for substantive engagement. **Gemini 2.5 Pro** for very long papers.
""")

# --- Refined: grand-rounds-speaker-prep ---
write_prompt(f"{P3}/conferences-and-journal-clubs/grand-rounds-speaker-prep.md",
    {"title":"Grand rounds speaker prep","pillar":"educational-operations","event_type":"conference",
     "audience":"faculty","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"grand-rounds, speaker-prep, audience-reading","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## The prompt

```
You are helping me prep for grand rounds. Read the host institution's culture if I describe it; ask if you don't know it.

## What I'm preparing

- **Topic:** [be specific]
- **Institution:** [name + general culture if I know it]
- **Date:** [when]
- **Duration:** [talk + Q&A]
- **Audience composition:** [mix]

## What to produce

1. **Audience profile** — who's likely there, what they know, what they want
2. **Talk structure** — opening hook approach + 3-4 content beats + synthesis (with timing)
3. **Recommended visuals** — 2-3 specific visuals that will land
4. **5 Q&A questions to prep for**:
   - 2 from a content expert
   - 2 from a generalist
   - 1 from a trainee
5. **What NOT to do** — 2-3 framings that will misfire at this institution. ASK ME about institutional culture before drafting this if you don't know.
6. **The "walking away" line** — one sentence the audience will remember 24 hours later

## Hard rules

- Ask about institutional culture before guessing
- Specific visuals, not generic
- Walking-away line testable in 24 hours

## What I will NOT accept

- Generic audience profile
- "What not to do" guessed at without knowing the institution
- Walking-away line that's too long or vague
```

## Required human verification

- Validate audience profile with someone at the host institution.
- Walking-away line should be repeatable from memory tomorrow.

## Best model and why

**Claude Opus 4.7** — audience reading and anticipating sophisticated questions requires depth.
""")

# --- Refined: qa-prep-doc ---
write_prompt(f"{P3}/conferences-and-journal-clubs/qa-prep-doc.md",
    {"title":"Q&A preparation document","pillar":"educational-operations","event_type":"conference",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"qa-prep, presentation, anticipation","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":"2026-05-17"},
    """## The prompt

```
You are preparing me for a Q&A. The hardest questions section is the most valuable. Don't softball.

## What I'm preparing for

- **Presentation:** [title + when]
- **Audience:** [description]

## What to produce

### 1. The 5-10 likeliest questions, ranked

For each:
- Question (phrased as I'd hear it)
- Questioner's angle (technical objection / clinical concern / scope question)
- 2-3 sentence response, evidence-backed
- Anticipated follow-up
- Pre-prepared data/slide/citation to have ready

### 2. The 2 HARDEST questions

The ones I'd dread. Be honest if I don't have a great answer; suggest how to respond honestly while preserving credibility.

### 3. The 1 question I CANNOT answer

If there's a gap, draft a response that acknowledges rather than dodges.

### 4. Time management

How long per answer for the available Q&A time.

### 5. Body language and voice

Where to look, how to handle hostile questioners, how to redirect off-topic.

### 6. The question I HOPE someone asks

Because it lets me make my strongest point.

## Hard rules

- Hardest questions must be genuinely hard, not softballs.
- Honest acknowledgments of gaps.
- The "hope someone asks" question should be one someone might actually ask.

## What I will NOT accept

- Softball "hardest" questions
- Dodging responses to the question I cannot answer
- Generic time management
```

## Required human verification

- Have a colleague pose the questions to you and rate your responses.
- Verify any data/citations referenced.

## Best model and why

**Claude Opus 4.7** — anticipating sophisticated hostile questions requires mental adversarialism.
""")

print("Batch 3 done — 25 prompts:")
print("  P2 remaining (10): matched-case-pair, slide-outline-1hr, speaker-notes,")
print("    visual-metaphor, audience-polls, video-script, resident-feedback-note,")
print("    journal-club-discussion-q, tumor-board-presentation, resident-as-teacher")
print("  P3 new (7): call-schedule-generator, lab-incident-debrief,")
print("    visiting-professor-invitation, irb-qi-protocol, promotion-portfolio-narrative,")
print("    medical-education-abstract, rotation-block-scheduling")
print("  P3 refined (8): faculty-feedback-summary, evaluation-rubric (rotations),")
print("    expectations-doc, syllabus, assignment-grading-rubric, journal-club-packet,")
print("    grand-rounds-speaker-prep, qa-prep-doc")
