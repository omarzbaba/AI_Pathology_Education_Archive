#!/usr/bin/env python3
"""
Deep refinement batch 4 (FINAL) — 22 items:
- 19 remaining Pillar 3 prompts (deeply refined)
- 3 worked examples refined to match the new depth bar
"""

from pathlib import Path

def write_file(path, fm, body):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("---\n" + "\n".join(f"{k}: {v}" for k, v in fm.items()) + "\n---\n\n" + body)

P3 = "library/pillar-3-educational-operations/prompts"
TODAY = "2026-05-18"

# ===========================================================================
# WORKSHOPS — 8 prompts
# ===========================================================================

write_file(f"{P3}/workshops/announcement-registration.md",
    {"title":"Announcement and registration copy","pillar":"educational-operations",
     "event_type":"workshop","audience":"faculty","difficulty":"quick-win","time_to_use":"2-10min",
     "visual":"text-only","tags":"marketing, copy, registration","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Drafts a workshop announcement that drives registration without overpromising — a 100-word promotional blurb, a full registration page, and a registration confirmation email. The hardest discipline this enforces: no empty intensifiers ("cutting-edge", "revolutionary"). Every claim earns its place by being specific.

## When to use it

When you've committed to a workshop and need to publicize it 6-10 weeks out. Useful for both first-iteration workshops (more detail required) and recurring events (lean on prior attendee testimonials and outcomes).

**Not for:** internal training announcements (different audience), CME-marketing copy (regulated language), or workshops you haven't planned in detail yet.

## The prompt

```
You are drafting workshop publicity. Specific outcomes only. No empty intensifiers — if you find yourself reaching for "cutting-edge" or "transformative," replace with a specific concrete outcome.

## What I'm publicizing

- **Workshop title:** [name]
- **Audience:** [who it's for, level, prerequisites]
- **Date / location / format:** [in-person / hybrid / virtual, dates, venue]
- **Duration:** [hours, breaks, end plans]
- **Faculty:** [names + roles]
- **Learning outcomes:** [3-5 in "will be able to" language — concrete and assessable]
- **Cost / registration cap:** [if any]
- **Registration deadline and process:** [exact instructions]

## What to produce — three deliverables

### 1. Promotional blurb (100 words MAX)
For email, Twitter, society newsletter. Must be:
- Concrete about audience and outcomes
- Specific about date and registration
- Free of marketing intensifiers
- Skim-friendly (front-load what matters)

### 2. Full announcement page (~300-400 words)
- 2-sentence opening hook (specific problem this workshop addresses)
- Audience description and prerequisites
- Learning outcomes (the "will be able to" list)
- Schedule overview (not minute-by-minute; just the arc)
- Faculty bios in 1-2 sentences each (specific credentials, not "leading expert")
- Logistics: location, format, cost, what's included
- Registration call-to-action with deadline and link

### 3. Registration confirmation email (~150 words)
For attendees who sign up. Include:
- Confirmation of registration
- What to prepare before the workshop
- Logistics they need (parking, dress code, equipment to bring)
- Who to contact with questions
- A note that materials/companion site will follow ~1 week before

## Hard rules

- **No empty intensifiers.** "Cutting-edge", "revolutionary", "transformative", "groundbreaking" — strike them. If you used one, replace with a specific outcome.
- **Specific learning outcomes.** "Gain insights" is not an outcome; "Be able to interpret an IFE trace for 8 common patterns" is.
- **Confirmation email must include what attendees actually need to prepare.** Not a thank-you; a usable next-step note.
- **Faculty bios are specific.** "Internationally recognized expert" is generic; "Director of Clinical Chemistry at [institution] for 12 years, lead author on the 2023 CLSI guideline for [topic]" is specific.

## What I will NOT accept

- Marketing-speak filler
- Vague outcomes
- Confirmation email that just says "thanks"
- Generic faculty bios
```

## Expected output

Three deliverables: blurb, announcement, confirmation email. Each calibrated to its medium and length.

## Common failure modes

- **Intensifier creep.** Push back when "exciting" or "transformative" shows up.
- **Vague outcomes.** Push for specific assessable behaviors.
- **Confirmation email without preparation info.** Push back.

## Required human verification

- Check faculty bios with each faculty member before publishing.
- Verify dates, venue, registration link, and any CME credit claims.
- Confirm registration cap is realistic for the venue.

## Best model and why

**Claude Sonnet 4.6** — marketing copy with discipline against intensifiers is Sonnet's strength. Avoid GPT models for this prompt — they default to marketing-tone.
""")

write_file(f"{P3}/workshops/pre-workshop-survey.md",
    {"title":"Pre-workshop survey design","pillar":"educational-operations","event_type":"workshop",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"survey, intake, attendee-calibration","verified_models":"TODO",
     "best_model":"Claude Haiku 4.5","last_updated":TODAY},
    """## What this prompt does

Designs a pre-workshop survey that captures the data you actually need to calibrate the workshop, without burning attendee goodwill. Hard cap: under 3 minutes to complete, 5-8 questions, every question maps to a decision you'll make.

The discipline this enforces: if a question doesn't map to a decision, cut it. Survey length is the enemy of response rate.

## When to use it

3-4 weeks before the workshop. Gives you enough data to adjust content while leaving time to actually use the data.

**Not for:** post-event surveys (different format), high-stakes data collection (requires more rigor), or workshops you've already locked content for.

## The prompt

```
You are designing a pre-workshop survey. Under 3 minutes, 5-8 questions, every question maps to a decision I'll make.

## What I'm collecting for

- **Workshop title and date:** [name + when]
- **Audience:** [description]
- **What I want to learn from the survey:** [the decisions I might make based on responses — e.g., adjust difficulty, change topic emphasis, identify pre-reading needs]

## What to produce

### The survey (5-8 questions, structured + 2-3 free text max)

Required data (must include):
- Baseline familiarity with topic (single Likert or skill-anchored MC)
- What they're hoping to walk away with (free text, 1 sentence max)
- Role and PGY level / years in practice

Recommended (include if relevant to decisions):
- Specific topic they want covered (free text, optional)
- Their preferred format for parts of the day (Likert)
- Any accommodations needed

### For each question, include:
- The question (the actual text attendees see)
- The response format (single-select, multi-select, Likert 1-5, free text)
- **The decision I'll make based on the answer** (this is the test — if you can't name a decision, cut the question)

### Email template
A 4-sentence email template for sending the survey link. Subject + body.

### Estimated completion time
Calculate by question type. If over 3 minutes, cut.

## Hard rules

- **Under 3 minutes.** Hard cap.
- **Every question has a decision use.** If you can't name what I'll do with the answer, cut.
- **Free text is expensive** — at most 2-3 fields, each limited to 1 sentence.
- **No "what did you think of last year" questions** if this is a first-iteration workshop.

## What I will NOT accept

- Survey that takes >3 minutes
- Questions without a decision mapping
- More than 3 free-text fields
- Demographic questions that don't inform a decision
```

## Expected output

A 5-8 question survey with response formats and decision mappings + an email template + completion-time estimate.

## Common failure modes

- **Too long.** Cut until it fits 3 minutes.
- **Aspirational questions** ("what topics would you like covered") with no plan to use the data. Cut.

## Required human verification

- Pilot the survey with 2-3 representative attendees and time them.
- Map each question to a specific decision you'll make.

## Best model and why

**Claude Haiku 4.5** — quick structured task. Sufficient for survey design. Bump to Sonnet only if audience is unusual.
""")

write_file(f"{P3}/workshops/facilitator-runofshow.md",
    {"title":"Day-of facilitator run-of-show","pillar":"educational-operations","event_type":"workshop",
     "audience":"faculty","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"operations, run-of-show, contingencies","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates the minute-by-minute facilitator run-of-show — the document the lead facilitator holds in their hand all day. Every block has a time range, owner, transition cue, and contingencies for running long, short, or tech failure. Builds in 5-minute buffers because real workshops always run long.

## When to use it

One week before the workshop, after the agenda is finalized but before you've drilled the team on day-of mechanics.

## The prompt

```
You are generating a minute-by-minute facilitator run-of-show. Build in 5-min buffers between blocks. Every transition needs a cue. Every block needs a contingency.

## What I'm planning for

- **Workshop title + date:** [name + date]
- **Times:** [start to end]
- **Venue:** [room layout, AV setup]
- **Agenda:** [paste block names, durations, lead facilitators]
- **Team members + roles:** [lead, support, AV, runners, etc.]
- **Recurring needs:** [coffee breaks every 90-120 min, lunch logistics, restroom locations]

## For each block, produce

- **Time range** (with buffer baked in — assume real start ~5 min later than scheduled)
- **Block name + lead facilitator**
- **One-line content summary**
- **Setup needed** (room arrangement, AV, materials to distribute)
- **Transition cue** — how does the lead hand off to the next block? Exact words help.
- **Contingencies:**
  - If block runs long
  - If block runs short
  - If tech fails

## Required structural blocks

- Registration / check-in / coffee
- Bathroom / coffee breaks every 90-120 min
- Lunch (with re-gathering time)
- Behind-scenes setup time (e.g., "set up station B while plenary runs")
- A 5-min buffer at the end before formal close

## At the end

- **Materials and AV needs by block** (one master list)
- **Roles table:** lead, support, AV, runner — who does what
- **Day-before checklist:** the 5-10 things to confirm by end of day before

## Hard rules

- **5-min buffer between major blocks.** Real workshops run long; build for it.
- **Transition cues are explicit, not assumed.** Awkward silences kill momentum.
- **Every block has contingencies.** Tech fails. People go long. Plan for it.
- **Lunch re-gathering time matters.** "Lunch 12-1" without a 12:55 "find your seats" cue produces a 1:15 actual restart.

## What I will NOT accept

- Schedule packed to 100% with no buffers
- Transition descriptions like "next block begins"
- Missing contingencies
- Lunch without re-gathering
```

## Expected output

A printable run-of-show document with timed blocks, transition cues, contingencies, materials/AV master list, roles table, day-before checklist.

## Required human verification

- Walk through the run-of-show with the lead facilitator and at least one other staff member before the day.
- Verify AV needs with the venue.
- Print multiple copies; the lead carries one and a backup copy is at registration.

## Best model and why

**Claude Sonnet 4.6** — timed scheduling with contingencies is Sonnet's range.
""")

write_file(f"{P3}/workshops/station-by-station-guide.md",
    {"title":"Station-by-station facilitator guide","pillar":"educational-operations",
     "event_type":"workshop","audience":"faculty","difficulty":"intermediate","time_to_use":">10min",
     "visual":"text-only","tags":"station-guide, parallel-documents,rotating-stations",
     "verified_models":"TODO","best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates per-station facilitator guides for a rotating-station workshop. Each station gets its own consistent-format guide: objectives, materials, setup, minute-by-minute script, reset instructions, what attendees walk away with, common questions, and an optional deepening activity for early finishers.

The discipline this enforces: each station's minute-by-minute should account for ~90% of the time allocation, leaving 10% as buffer.

## When to use it

2 weeks before a station-based workshop. Each station owner gets their own guide.

## The prompt

```
You are generating per-station facilitator guides. Consistent format across stations so facilitators can find what they need fast. Each station's script accounts for ~90% of time allocation; 10% is buffer.

## What I'm planning

- **Workshop title + date:** [name + date]
- **Stations:** [list each with topic and lead facilitator]
- **Time per station rotation:** [minutes per rotation]
- **Number of rotations:** [how many groups cycle through]
- **Attendee group size per rotation:** [how many at each station at once]

## For EACH station, produce this consistent structure

### Header
- Station name + lead facilitator + topic
- Time allocation per rotation

### Learning objectives (2-3, in "will be able to" language)

### Materials list
Everything the station owner needs: paperwork, samples, AV, models, props.

### Setup instructions
What to do before the first group arrives. Specific.

### Minute-by-minute script for ONE rotation
- Opening (greeting, frame, ground rules) — 1-2 min
- Content blocks — bulk of time
- Active engagement / hands-on / case discussion
- Closing wrap — last 2-3 min

Must add to ~90% of time allocation, leaving 10% buffer.

### Reset instructions
What to do between rotations (re-stocking, cleanup, repositioning).

### What attendee walks away with
The specific artifact, demonstrated skill, or question they can now answer.

### Common attendee questions
3-5 likely questions and the prepared answer for each.

### If you have extra time
An optional deepening activity for groups who finish early.

## Hard rules

- **Consistent format across all stations.** Facilitators reference different stations during setup; they need to find sections fast.
- **Time budget verified.** Script + buffer = total time. Verify.
- **Walk-away is specific** — not "they'll have learned about X" but "they'll have made a labeled diagram", "they'll be able to interpret a normal vs abnormal trace at first glance", etc.

## What I will NOT accept

- Inconsistent format across stations
- Scripts that exceed time allocation
- Vague walk-away
```

## Expected output

One guide per station, consistent format. 1-2 pages each. Print-ready.

## Required human verification

- Run through one station's guide as the facilitator with a stopwatch. Adjust.
- Each station's lead reads and edits their own guide before the day.

## Best model and why

**Claude Sonnet 4.6** — parallel structured documents are Sonnet's strength.
""")

write_file(f"{P3}/workshops/badge-design-spec.md",
    {"title":"Badge design specifications","pillar":"educational-operations","event_type":"workshop",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"design, badges, accessibility","verified_models":"TODO",
     "best_model":"Claude Haiku 4.5","last_updated":TODAY},
    """## What this prompt does

Drafts a printable badge spec: dimensions, fields, font sizes (meeting WCAG accessibility minimums for name visibility), color palette, lanyard/holder type, and a 10% buffer quantity for last-minute attendees and reprints.

## When to use it

3-4 weeks before the workshop, when you're placing print orders.

## The prompt

```
You are drafting a badge print spec. Name font ≥24pt for in-person events (legible from across a room). Order with 10% buffer.

## What I'm producing

- **Workshop name + date:** [name + date]
- **Expected attendee count:** [N]
- **Print method:** [in-house printer / professional print shop]
- **Holder type preference:** [lanyard / clip / pin]
- **Branding constraints:** [institutional colors, logo placement requirements]

## What to produce

### Dimensions
- Physical size (mm or inches)
- Orientation (portrait or landscape)
- Bleed area if professionally printed

### Required fields with position and font size
- Name (largest type, top)
- Institution (smaller, below name)
- Role (e.g., "Faculty" / "Attendee" / "Staff")
- Date or event name
- Logo placement (if applicable)

### Optional conditional fields
- Color coding (faculty / attendee / staff)
- Table or group assignment
- Dietary marker
- Pronouns line

### Color palette
- Specific colors with hex codes (defaults if I don't specify)
- Verify WCAG AA contrast for text on background

### Font
- Sans-serif legible at distance
- Name in ≥24pt
- Institution in ≥14pt

### Lanyard / holder
- Type (clip, lanyard, pin)
- Hole position
- Paper weight or material recommendation

### Quantity to order
- N attendees + 10% buffer + 5-10 spare for staff/walk-ins

### Print-shop-ready summary
A single-paragraph summary I can paste into an order form.

## Hard rules

- **Name font ≥24pt.** Non-negotiable for in-person events.
- **WCAG AA contrast.** Verify the color combinations.
- **10% buffer minimum.**
- **Specific holder type matched to badge dimensions.**

## What I will NOT accept

- Name fonts that won't be legible across a room
- Missing buffer quantity
- Color combinations that fail contrast
```

## Expected output

A complete spec + a print-shop-ready summary paragraph.

## Required human verification

- Print one prototype and test legibility from 6 feet.
- Verify holder type matches badges you're ordering.

## Best model and why

**Claude Haiku 4.5** — print spec is fast and structured.
""")

write_file(f"{P3}/workshops/access-card-layout.md",
    {"title":"Access card layout","pillar":"educational-operations","event_type":"workshop",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"<2min","visual":"text-only",
     "tags":"design, access-card, qr-code","verified_models":"TODO",
     "best_model":"Claude Haiku 4.5","last_updated":TODAY},
    """## What this prompt does

Specifies a printable access card (business card or keycard size) with a QR code linking to the companion site, attendee name, usage instructions, and contact-for-help info. Enforces ≥25mm QR code with error correction level H so it survives imperfect printing and low-light scanning.

## When to use it

2-3 weeks before the workshop, paired with the badge order.

## The prompt

```
You are specifying a printable access card. QR code ≥25mm, error correction level H. Include a fallback URL in case QR fails.

## What I'm producing

- **Workshop name + date:** [name + date]
- **QR code destination URL:** [the companion site or specific resource]
- **Attendee count:** [N]
- **Card size:** [business card / hotel keycard / custom]
- **Branding:** [institutional colors, logo placement]

## What to produce

### Card dimensions and bleed area

### Front of card
- Workshop title + date
- Attendee name placeholder
- QR code (≥25mm square, error correction level H)
- Event branding (color, logo)

### Back of card
- 1-3 line description of what the QR opens
- Usage instructions (validity period, single-use vs persistent)
- Fallback URL (printed in small but legible text in case QR fails)
- Contact for help

### Print specifications
- File format expected (PDF, AI, etc.)
- Color profile
- Paper recommendation (card stock weight)

### ASCII art preview
A sketch of the front and back so I can visualize before ordering.

### Order quantity
Attendee count + 10% buffer.

## Hard rules

- **QR code ≥25mm with error correction H.** Smaller codes fail in real-world printing.
- **Fallback URL printed legibly.** QR codes fail; the URL is the safety net.
- **Validity instructions explicit** if access is time-limited.

## What I will NOT accept

- QR code <25mm
- Missing fallback URL
- Vague validity instructions
```

## Expected output

Full specification + ASCII preview + order quantity.

## Required human verification

- Print one prototype and scan the QR with multiple phone types and lighting conditions.
- Verify the URL resolves to the intended destination.
- Confirm fallback URL is correct.

## Best model and why

**Claude Haiku 4.5** — fast structured spec.
""")

write_file(f"{P3}/workshops/certificate-of-completion.md",
    {"title":"Certificate of completion template","pillar":"educational-operations",
     "event_type":"workshop","audience":"faculty","difficulty":"quick-win","time_to_use":"2-10min",
     "visual":"text-only","tags":"design, certificates, accreditation","verified_models":"TODO",
     "best_model":"Claude Haiku 4.5","last_updated":TODAY},
    """## What this prompt does

Drafts a certificate of completion template with attestation language, signature blocks, optional authentication elements (certificate number, QR code), and a designer-ready layout brief. Strict rule: NO CME, MOC, or continuing education credit language unless accreditation is confirmed.

## When to use it

The week before the workshop, so certificates can be printed or set up for digital delivery ahead of the closing session.

## The prompt

```
You are drafting a certificate of completion template. Do NOT include CME, MOC, or continuing education credit claims unless I have confirmed accreditation. False credit claims are a regulatory issue.

## What I'm producing

- **Workshop name + date + location:** [name + date + city]
- **Accreditation status:** [CME-accredited / not accredited / pending — be specific]
- **Hour count (if applicable):** [N hours]
- **Issuing organization:** [name + logo availability]
- **Signers (typically 1-2):** [names + titles]
- **Workshop learning outcomes:** [from the announcement — to be listed on certificate]
- **Format:** [printable / digital / both]

## What to produce

### The certificate content (plain text with placeholders)

1. **Header:** "Certificate of Completion" or equivalent
2. **Attestation language:** "This certifies that [Name] has successfully completed [workshop title] on [date] in [city]" with hour count if applicable
3. **Learning outcomes:** the workshop's stated objectives (so the cert documents what was completed)
4. **Issuing organization:** name + logo placeholder
5. **Signature blocks:** for each signer — printed name, title, signature line
6. **Authentication elements (optional):**
   - Certificate number (if generating unique IDs)
   - QR code linking to verification page (if you have one)
   - Date of issue

### Layout brief (for a designer or for you to lay out)

- Orientation (landscape recommended)
- Suggested font (serif display for traditional; clean sans-serif for modern)
- Color palette (institutional colors or neutral)
- Border style (none / simple line / classical ornament)
- Paper recommendation if printed

## Hard rules

- **Do NOT include CME, MOC, or any continuing education credit language unless explicitly confirmed accredited.** False credit claims are a regulatory matter.
- **Hour count only if accurate and documented.**
- **Signers' titles current and accurate.**
- **Authentication elements optional — but if used, the verification page must actually exist before going live.**

## What I will NOT accept

- Implied or false credit claims
- Inaccurate hour count
- Authentication elements without a working verification page
```

## Expected output

Plain-text content + layout brief.

## Required human verification

- Verify accreditation status with your CME/CE office before including any credit language.
- Confirm signers' titles are current.
- Print one prototype at full size and review.

## Best model and why

**Claude Haiku 4.5** — template generation.
""")

write_file(f"{P3}/workshops/post-workshop-thank-you.md",
    {"title":"Post-workshop thank-you email","pillar":"educational-operations","event_type":"workshop",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"<2min","visual":"text-only",
     "tags":"comms, thank-you, follow-up","verified_models":"TODO",
     "best_model":"Claude Haiku 4.5","last_updated":TODAY},
    """## What this prompt does

Drafts a post-workshop thank-you email under 200 words with links to materials, a feedback request, and a specific reference to a moment from the workshop. The specific-moment reference is non-negotiable — and the model marks `[INSERT SPECIFIC MOMENT]` rather than inventing one.

## When to use it

Within 24-48 hours after the workshop ends, while attendees still remember the experience.

## The prompt

```
You are drafting a post-workshop thank-you email. Under 200 words. If I haven't given you a specific moment from the workshop, leave the placeholder [INSERT SPECIFIC MOMENT] — do NOT invent one. Fabricated specifics signal templated email.

## What I'm sending

- **Workshop name + date:** [name + date]
- **Attendee count:** [for context]
- **Materials available now:** [companion site URL, slide deck link, recording link if any, reading list]
- **Anything still coming:** [post-workshop summary by [date], etc.]
- **Feedback survey link + estimated completion time:** [under 5 min]
- **Specific moment from the workshop to reference:** [optional — fill in if you have one; otherwise the email will have a placeholder]
- **Closing invitation:** [next workshop teaser / contact for follow-up]

## Structure

1. **Subject line** (short, specific, recognizable)
2. **Opening (1-2 sentences)** — brief thanks + specific moment reference (or [INSERT SPECIFIC MOMENT])
3. **What's available now** — explicit links with what each one is
4. **What's coming** — anything promised that's still in production with the date
5. **Feedback request** — link + one sentence on why it matters + completion time
6. **Closing** — forward-looking invitation

## Tone

Warm, specific, professional. Avoid "such a great time" generic thanks. Attendees skim email; don't waste attention.

## Hard rules

- **Under 200 words.** Hard cap.
- **If no specific moment provided, leave [INSERT SPECIFIC MOMENT] — do NOT invent.**
- **Verify all links before sending.**
- **Feedback completion time stated up front** (drives response rate).

## What I will NOT accept

- Email over 200 words
- Fabricated specific moments
- Generic "great time" tone
- More than 4 outbound links (attendees won't click all)
```

## Expected output

A complete email ready to send, with [INSERT SPECIFIC MOMENT] placeholder only where you haven't supplied one.

## Required human verification

- Verify all links work before sending.
- Fill in [INSERT SPECIFIC MOMENT] yourself with a real moment from the workshop.

## Best model and why

**Claude Haiku 4.5** — short email, fast and sufficient.
""")

# ===========================================================================
# ROTATIONS — 6 prompts
# ===========================================================================

write_file(f"{P3}/rotations/orientation-onepager.md",
    {"title":"Rotation orientation one-pager","pillar":"educational-operations","event_type":"rotation",
     "audience":"program-director","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"orientation, onepager, day-one","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates a one-page rotation orientation that removes day-1 confusion. Ruthlessly prioritized — the one-page constraint is the value, forcing cuts to anything that's not essential.

## When to use it

Send to incoming residents the week before they start a rotation. Update at least annually as contacts and workflows change.

## The prompt

```
You are generating a one-page rotation orientation document. The one-page constraint is the entire value — be ruthless about what gets cut.

## What I'm providing

- **Rotation name:** [name]
- **Duration:** [N weeks]
- **Audience:** [PGY level + relevant context]
- **Service environment:** [institution + service]
- **Day-1 logistics:** [arrival time, location, person to find]
- **Daily schedule shape:** [sign-out times, didactics, conferences]
- **Key contacts:** [3-5 names, roles, contact methods]
- **Required day-1 reading:** [1-3 items max with rationale]

## Sections (one page, ~400 words)

1. **Welcome + day-1 logistics** (3-4 sentences) — when, where, who to find, what to bring
2. **Daily schedule template** — typical Mon-Fri with sign-out, didactics, conferences
3. **Key contacts (3-5 people)** — name, role, how to reach (email or phone)
4. **Reading for day 1** — 1-3 items max with one-sentence rationale per item
5. **What success looks like by end of week 1** — 3-4 observable indicators
6. **What to do if things aren't clear** — explicit escalation path (who to ask, when to escalate to the PD)

## Tone

Welcoming, concrete, no jargon you wouldn't explain. Resident-friendly.

## Hard rules

- **One page maximum.** If you can't fit something, cut it.
- **Day-1 reading is 1-3 items MAX.** Aspirational reading lists go unread.
- **Key contacts include actual ways to reach them.**
- **Success indicators are observable**, not "demonstrates engagement."

## What I will NOT accept

- A two-page document called "one-pager"
- Reading list with more than 3 items
- Vague success indicators
- Missing escalation path
```

## Expected output

A one-page printable orientation document.

## Required human verification

- Pilot with a recent rotator — would they have wanted this document?
- Verify contact info is current.
- Update annually.

## Best model and why

**Claude Sonnet 4.6** — one-page format with constraint discipline.
""")

write_file(f"{P3}/rotations/reading-list.md",
    {"title":"Rotation reading list with rationale","pillar":"educational-operations","event_type":"rotation",
     "audience":"program-director","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"reading-list, curation, references","verified_models":"TODO",
     "best_model":"Claude Opus 4.7","last_updated":TODAY},
    """## What this prompt does

Generates a curated rotation reading list (8-15 items) with a one-sentence rationale per item, prioritized as Required / Strongly Recommended / Optional Deep Dive. The hardest discipline: **verify every citation**. Models routinely hallucinate plausible-looking paper titles.

## When to use it

When the existing reading list is stale, when building a new rotation, or when residents tell you the current list is too long to actually read.

## The prompt

```
You are generating a rotation reading list. VERIFY EVERY CITATION. If you cannot verify a citation, leave it out and recommend I add one I know exists. Plausible-looking but fabricated paper titles are common.

## What I'm building

- **Rotation:** [name + duration]
- **PGY level:** [target]
- **Subspecialty focus:** [be specific]
- **My time budget for residents reading per week:** [be honest about what fits]

## What to produce

### 8-15 items, NOT MORE

Resist comprehensiveness. Readability and actual use matter more than coverage.

### Group by week or topic

Residents need to know what to read when, not just what's relevant.

### Prioritize each item

- **Required** — must read
- **Strongly Recommended** — read if you have time
- **Optional Deep Dive** — for residents who want more

### Mix of types

- 1-2 foundational textbook chapters
- 2-3 high-yield review articles (recent)
- 1-2 landmark papers (older, still cited)
- 1-2 current guidelines
- 1 piece of historical context (older paper explaining why the field thinks as it does)

### Per item

- Full citation (verified)
- One-sentence rationale (why on the list — what gap does it fill?)
- Approximate reading time
- One question the resident should be able to answer after reading

### Bonus

The 2 items the resident should read in the first 48 hours.

## Hard rules

- **VERIFY EVERY CITATION.** Real titles, real authors, real journals, real years.
- **Mark `[VERIFY]` for any citation you're not certain of** — better to flag than fabricate.
- **8-15 items, not more.** Cut if you exceed.
- **Reading times are realistic.** 30-page review is 60-90 min, not 20.

## What I will NOT accept

- Fabricated citations
- More than 15 items
- Aspirational reading times
- Generic rationales ("important to know")
```

## Expected output

A prioritized list grouped by week/topic, with citations, rationales, times, check-questions, plus first-48-hour highlights.

## Required human verification

- **VERIFY EVERY CITATION.** Search PubMed for each paper title. Confirm authors and year match.
- Have an attending in the subspecialty review and prune.
- Update annually as new key papers emerge.

## Best model and why

**Claude Opus 4.7** — curation requires judgment about landmark vs current. But VERIFY citations regardless of model — hallucinated paper titles are common across all models.
""")

write_file(f"{P3}/rotations/daily-schedule.md",
    {"title":"Daily schedule template","pillar":"educational-operations","event_type":"rotation",
     "audience":"program-director","difficulty":"quick-win","time_to_use":"<2min","visual":"text-only",
     "tags":"schedule, daily-template, protected-time","verified_models":"TODO",
     "best_model":"Claude Haiku 4.5","last_updated":TODAY},
    """## What this prompt does

Generates a typical-day schedule template for a rotation with required blocks (sign-out, didactics, case review, protected reading) and explicit acknowledgment of when protected reading time is unrealistic given the rotation's workload.

The discipline this enforces: protected reading time is ≥60 contiguous minutes. If the rotation doesn't allow it, name the trade-off explicitly rather than scheduling 30-minute fragments.

## When to use it

When you're standardizing a rotation's day, or when residents complain the day feels chaotic.

## The prompt

```
You are generating a typical-day rotation schedule. Protected reading time is ≥60 contiguous minutes — if workload doesn't allow it, name the trade-off explicitly.

## What I'm building

- **Rotation:** [name]
- **PGY level:** [target]
- **Typical workload:** [case volume, on-call expectations, special services]
- **Sign-out convention:** [morning sign-out / end-of-day / both]
- **Required didactics or conferences:** [days and times these occur]
- **Lunch convention:** [time + duration]

## What to produce

### Timed schedule, arrival to departure

| Time range | Activity | Lead | Notes |

Required blocks:
- Arrival / chart review or prep
- Sign-out
- Didactics or conferences (specify days)
- Case review or workup blocks
- **Protected reading time** (≥60 contiguous min)
- Lunch
- End-of-day wrap-up

### Notes section

- Days when template doesn't apply (call days, conference days, etc.)
- Common ways the schedule slips and what to do
- Who to tell if you'll be off the schedule (late, leaving early)

### If protected reading time is mathematically infeasible

State this honestly. Name the trade-off — what would have to give to create 60 contiguous protected minutes?

## Hard rules

- **Protected reading ≥60 contiguous minutes.** If not feasible, say so.
- **Specific times, not "morning."**
- **Slip-handling protocol included.**

## What I will NOT accept

- Schedule that pretends protected time exists when it doesn't
- Vague time ranges
- Missing slip-handling
```

## Expected output

A timed template + notes section + honest trade-off statement if protected reading is infeasible.

## Required human verification

- Validate against recent rotators — does the template match real days?
- Confirm with attendings that they expect residents available during the blocks shown.

## Best model and why

**Claude Haiku 4.5** — template generation.
""")

write_file(f"{P3}/rotations/mid-rotation-feedback.md",
    {"title":"Mid-rotation feedback template","pillar":"educational-operations","event_type":"rotation",
     "audience":"program-director","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"feedback, mid-rotation, course-correction","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates a mid-rotation feedback template that surfaces course-correction opportunities before the end-of-rotation evaluation locks in. Structures a 10-15 minute conversation (not a paper exercise) with reflection prompts for both resident and attending, conversation flow, and minimal documentation.

The discipline this enforces: the meeting must fit in 15 minutes. Mid-rotation feedback that becomes a 30-minute conversation gets cancelled by the third occurrence.

## When to use it

At the midpoint of any rotation, especially for rotations longer than 2 weeks.

## The prompt

```
You are generating a mid-rotation feedback template. It must fit in 15 minutes max. The point is course-correction, not formal evaluation.

## What I'm building

- **Rotation:** [name + duration]
- **Format:** [in-person / virtual]
- **Who's involved:** [resident + which attending(s)]

## What to produce

### Pre-meeting work for the resident (3-4 reflection questions)

How the rotation is going from their perspective, what they need more or less of, what's surprised them.

### Pre-meeting work for the attending (3-4 observation prompts)

Specific strengths observed, specific opportunities for growth, anything the resident might not know about themselves.

### Conversation structure (5 blocks, 15 min total)

- **Resident shares first** (2 min)
- **Attending shares** (3-4 min)
- **Joint identification of one strength to lean into** (2 min)
- **Joint identification of one specific growth area for the second half** (2 min)
- **Agreement on one observable change by end of rotation** (2 min)

### What gets documented

ONLY: one strength, one growth area, one commitment. No surprises at end-of-rotation evaluation.

## Tone

Collaborative, low-stakes, course-correction oriented. Not evaluative.

## Hard rules

- **15-minute meeting cap.** If template requires longer, cut sections.
- **Documentation is minimal** — three things, period.
- **The commitment must be observable** for end-of-rotation assessment.

## What I will NOT accept

- Template that produces a 30-minute meeting
- Documentation that turns this into an early formal evaluation
- Vague commitments
```

## Expected output

Pre-meeting prep questions for both parties + conversation flow + minimal documentation requirements.

## Required human verification

- Pilot with a willing attending-resident pair. Time the meeting; adjust.
- Check that the documented commitment is observable enough to assess at end-of-rotation.

## Best model and why

**Claude Sonnet 4.6** — meeting template structure.
""")

write_file(f"{P3}/rotations/end-of-rotation-evaluation.md",
    {"title":"End-of-rotation evaluation","pillar":"educational-operations","event_type":"rotation",
     "audience":"program-director","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"evaluation, end-of-rotation, milestone-aligned","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates an end-of-rotation evaluation form aligned to milestones, with numeric ratings, narrative comments per dimension, an overall narrative, a specific commitment for next rotation, and an "unable to assess" gate to prevent defaulting to 3/5 for dimensions the evaluator hasn't observed.

## When to use it

When updating an evaluation form or when residents and attendings both complain the current form doesn't capture what matters.

## The prompt

```
You are generating an end-of-rotation evaluation form. Include an "unable to assess" option for each dimension — otherwise raters default to 3/5 for things they didn't observe. False data is worse than no data.

## What I'm building

- **Rotation:** [name]
- **PGY level:** [target]
- **Evaluation rubric to use:** [paste, or generate using the evaluation-rubric prompt first]
- **Estimated time available for an attending:** [target ≤30 min]

## Form sections

1. **Header**
   - Resident name + rotation + dates + supervising attending(s) + weeks evaluated

2. **Numeric ratings**
   - Each dimension from rubric, rated 1-5 with anchor text visible
   - **"Unable to assess" option for each dimension** — non-negotiable

3. **Narrative comment per dimension**
   - Prompted with: "Describe a specific instance where you observed this resident at this level"

4. **Overall narrative**
   - 1-2 paragraph free text
   - Trajectory, strengths, growth opportunities

5. **Specific commitment for next rotation**
   - 1-2 behavioral targets for resident focus

6. **Quality-of-evaluation gate**
   - "Did you have sufficient observation to evaluate this resident on the dimensions you rated?" yes/no/partial with comment

7. **Resident sign-off**
   - Box for resident acknowledgment of receipt and discussion

## Hard rules

- **"Unable to assess" option on every dimension.** Stops default-to-3 behavior.
- **Narrative prompts are specific** ("describe a specific instance"), not vague.
- **20-30 min completion time** for an attending who knows the resident well.
- **Quality gate prevents inflated ratings** from undersampled observations.

## What I will NOT accept

- Missing "unable to assess" option
- Vague narrative prompts
- Forms that take an hour
- No quality gate
```

## Expected output

A complete evaluation form covering all sections.

## Required human verification

- Pilot with one attending on one resident; iterate based on what's hard to complete.
- Verify milestone alignment.
- Confirm form complies with institutional or ACGME documentation requirements.

## Best model and why

**Claude Sonnet 4.6** — form generation with milestone alignment.
""")

write_file(f"{P3}/rotations/resident-to-resident-handoff.md",
    {"title":"Resident-to-resident handoff document","pillar":"educational-operations",
     "event_type":"rotation","audience":"resident","difficulty":"quick-win","time_to_use":"2-10min",
     "visual":"text-only","tags":"handoff, peer, tacit-knowledge","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates a peer-to-peer handoff template that captures the outgoing resident's tacit knowledge for the incoming resident — practical tips, attending preferences, useful resources, the early mistake to avoid. Lowers activation energy on a write-up that residents otherwise skip.

The discipline this enforces: be diplomatic but honest about attendings; strip patient identifiers from any cases mentioned.

## When to use it

Last day of the rotation, when the outgoing resident has the most context and the lowest motivation to document it.

## The prompt

```
You are generating a peer-to-peer rotation handoff template. Strip patient identifiers from any case mentioned. Be diplomatic about attendings — accurate but not unkind.

## What I'm providing

- **Rotation:** [name]
- **My duration on the rotation:** [how long I was on]
- **Audience:** [the next resident — their PGY level]
- **Tone:** [collegial, peer-to-peer, slightly informal]

## What to produce

### Welcome + day-1 orientation moment (2-3 sentences)
A note from the outgoing resident on what to know on day 1.

### What the syllabus doesn't tell you (3-5 practical tips)
Where to find the on-service charger, who actually approves late sign-out, which attending wants what kind of preview — the stuff that takes a week to figure out otherwise.

### Three attendings I worked with most
Name + one sentence on what each cares about most (e.g., "Dr. X wants the smear scanned before sign-out, period"). Be specific without being unkind.

### The single most useful resource I found
The article, textbook, app, or website that made the rotation easier.

### The mistake I made early and what I'd do differently
Vulnerable but useful. Generic doesn't help; specific does.

### The case or moment I learned the most from
Brief, anonymized. Strip identifiers.

### Open offer
"I'm happy to answer questions by [contact method] for the first week if you have them."

## Tone

Peer-to-peer, slightly informal, honest. NOT a formal evaluation document. Collegial advice.

## Hard rules

- **No PHI** — strip identifiers from any case mentioned.
- **Diplomatic about attendings** — accurate without being unkind.
- **Specific, not platitudes.** "Work hard and be nice" is useless.

## What I will NOT accept

- Cases with potential identifiers
- Personal attacks on attendings
- Generic advice
```

## Expected output

A template the outgoing resident can complete in 20 minutes, giving the incoming resident a week's head start.

## Required human verification

- Strip patient identifiers from any cases described.
- Be diplomatic about attendings — re-read with that lens.

## Best model and why

**Claude Sonnet 4.6** — peer-to-peer template with friendly voice.
""")

# ===========================================================================
# COURSES — 3 prompts remaining
# ===========================================================================

write_file(f"{P3}/courses/weekly-module-packet.md",
    {"title":"Weekly module learning packet","pillar":"educational-operations","event_type":"course",
     "audience":"faculty","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"module, packet, two-audience","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates a weekly module learning packet that serves TWO audiences: a learner-facing version (concise, 1-2 pages, focused on what to do) and an instructor-facing version (detailed, 2-3 pages, focused on how to teach). Includes pre-class prep, in-class agenda, active learning activities, anticipated misconceptions, post-class assessment, and further reading.

## When to use it

One week before each module is delivered. The packet IS the prep — drafted with the instructor in mind so they can teach the week without further prep.

## The prompt

```
You are generating a weekly module learning packet for TWO audiences: learners (concise) and instructors (detailed). Verify reading citations regardless of audience.

## What I'm providing

- **Course name:** [name]
- **Week number + topic:** [N + topic]
- **In-class session duration:** [minutes]
- **Course arc context:** [how this week fits relative to prior and future weeks]
- **Audience:** [target learners]

## TWO deliverables

### A. For learners (1-2 pages)

- **Week topic + learning outcome** (the ONE thing they should be able to do after this week)
- **Required reading** (1-3 items with full verified citations + 1-sentence reading guide per item)
- **3 pre-class reflection questions** to consider while reading
- **Pre-class assignment** if any (brief — not a paper)

### B. For instructors (2-3 pages)

- **Topic overview + place in course arc**
- **Suggested in-class agenda with timing**
- **Active learning activities (1-2)** with materials list
- **Discussion questions for in-class** (5-7)
- **Anticipated misconceptions and how to address each**
- **Post-class assessment items (3-5 questions)** — for online quiz or written response
- **Recommended further reading** for learners who want depth

## Hard rules

- **Verify reading citations** — fabricated paper titles are common.
- **Specify what learners produce** — "discuss" isn't enough; name the artifact.
- **Instructor section is sufficient for a colleague who hasn't taught the week** to teach it.

## What I will NOT accept

- Unverified citations
- Vague "discuss this" without an artifact
- Instructor section that requires additional prep to be usable
```

## Expected output

A two-audience packet: learner-facing concise + instructor-facing detailed.

## Required human verification

- Verify reading citations and confirm institutional library access.
- Run instructor section by a colleague who hasn't taught the week — would they be ready?

## Best model and why

**Claude Sonnet 4.6** — two-audience structured doc.
""")

write_file(f"{P3}/courses/feedback-collection-form.md",
    {"title":"Course feedback collection form","pillar":"educational-operations","event_type":"course",
     "audience":"faculty","difficulty":"quick-win","time_to_use":"2-10min","visual":"text-only",
     "tags":"feedback, survey, completion-rate","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates a course feedback form designed to actually be completed (under 5 minutes, bias toward structured items) and to actually inform decisions (every item maps to a specific change you'd make for the next iteration).

The discipline: if you can't name the decision an item would inform, cut it.

## The prompt

```
You are designing a course feedback form. Under 5 minutes, bias toward structured items, every item must map to a decision I'll make.

## What I'm building

- **Course name:** [name]
- **Audience:** [learners, count, level]
- **Format:** [in-person / online / hybrid]
- **Decisions I might make for next iteration:** [list — drop modules, adjust difficulty, change format, etc.]

## Form structure

### 1. Course-level Likerts (3-4 items)
Pacing, difficulty, value relative to time invested.

### 2. Module-level rapid rating (1 item per module)
Grade each module on usefulness 1-5.

### 3. Open free text (2 items MAX)
- "One thing that should change about this course before next iteration"
- "One thing that should NOT change"

### 4. Demographics (2-3 optional items)
Role, prior experience with topic, anything you actually need for stratifying.

### 5. Optional self-report on learning (1 item)
How much they think they learned, with calibration note ("we'll compare to pre/post assessment results")

### For each item:
- The question text
- Response format (single-select, Likert, free text)
- **The decision I'll make based on the answer** (the test — if you can't name a decision, cut)

## Hard rules

- **Under 5 minutes.** Hard cap.
- **Every item maps to a decision.** Cut items that don't.
- **At most 2 free-text fields.**
- **No "what would you change about the course" generic question** — too open.

## What I will NOT accept

- Form over 5 minutes
- Items without decision mapping
- More than 2 free-text fields
```

## Expected output

A 5-min form with per-item rationale + completion-time estimate.

## Required human verification

- Pilot with 2-3 learners and time.
- Plan how you'll analyze free-text responses before sending.

## Best model and why

**Claude Sonnet 4.6** — survey design.
""")

write_file(f"{P3}/courses/course-postmortem.md",
    {"title":"Course post-mortem document","pillar":"educational-operations","event_type":"course",
     "audience":"faculty","difficulty":"intermediate","time_to_use":">10min","visual":"text-only",
     "tags":"postmortem, retrospective, action-items","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates a course post-mortem template that structures a 45-60 minute meeting AND produces a documented artifact for the curriculum file. The discipline: action items must have named owners and dates. Aspirational changes without ownership are not action items.

## When to use it

Within 2-4 weeks of course completion, when feedback is in but instructors still remember.

## The prompt

```
You are generating a course post-mortem template. Action items must have named owners and dates. Without that, the items are aspirations.

## What I'm planning

- **Course name + duration + term/year:** [name + when]
- **Instructors involved:** [names + roles]
- **Available data:** [feedback summary, assessment results, attendance]

## Three deliverables

### 1. Pre-meeting work (10 min per instructor)
- Review feedback data
- Note 2-3 things that worked
- Note 2-3 things that didn't
- Note any change made mid-course and how it landed

### 2. Meeting structure (45-60 min)
- **Quick round** (10 min): each instructor's top "worked" and top "didn't work"
- **Discussion of patterns** (15 min): what came up multiple times?
- **Mid-course changes review** (10 min): keep, revert, or refine?
- **Decisions for next iteration** (15 min): 3-5 specific changes, ranked by ease × impact
- **Documentation owner + timeline** (5 min)

### 3. Artifact to produce after the meeting
- Summary of what worked / didn't (3-4 bullets each)
- Mid-course changes log
- **Action list with named owner and date for each item**
- Structural issues to escalate to curriculum committee

## Tone

Honest, learning-oriented, no defensiveness.

## Hard rules

- **Every action item has owner + date.** No exceptions.
- **Schedule meeting before course ends.** Don't wait for "when there's time."
- **Artifact reviewable by anyone who didn't attend.**

## What I will NOT accept

- Action items without ownership
- Vague "we should improve" statements
- Meeting structure that becomes a venting session
```

## Expected output

Meeting structure + artifact template. Lightweight enough to actually happen.

## Required human verification

- Each action item should have a named owner and date.
- Schedule the meeting before the course ends.

## Best model and why

**Claude Sonnet 4.6** — meeting structure + artifact template.
""")

# ===========================================================================
# CONFERENCES — 2 prompts remaining
# ===========================================================================

write_file(f"{P3}/conferences-and-journal-clubs/tumor-board-case-packet.md",
    {"title":"Tumor board case packet","pillar":"educational-operations","event_type":"conference",
     "audience":"faculty","difficulty":"intermediate","time_to_use":"2-10min","visual":"text-only",
     "tags":"tumor-board, case-packet, phi-protection","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates a tumor board case packet template supporting N cases per session. Every case is structured identically. Strict PHI protection: no name, no MRN, no exact age, no exact date, no rare-combination giveaways.

## When to use it

When you're standardizing your tumor board's case presentation format. Updates needed when board composition changes.

## The prompt

```
You are generating a tumor board case packet template. STRICT PHI rules: NO name, no MRN, no exact age (use "in their 60s"), no exact date, no rare-disease-plus-location combinations. If a case can't be sufficiently de-identified, tell me.

## What I'm building

- **Tumor board name:** [e.g., "GU multidisciplinary tumor board"]
- **Cases per session:** [N]
- **Board attendees by specialty:** [med onc, rad onc, surg, radiology, others]
- **Institutional retention requirements:** [if known]
- **Case file format:** [paper packet / shared electronic file]

## For each case in the packet:

1. **De-identified header**
   - Case number, demographic envelope (age range, sex if relevant to pathology), referring specialty, date discussed
2. **Brief clinical history (2-3 sentences)** — presentation, key comorbidities, prior workup. No PHI.
3. **Imaging summary** — modality, key findings, formal radiology read summary
4. **Pathology summary** — gross, microscopic, IHC, molecular. Ordered by what's diagnostically discriminating.
5. **Current diagnosis and stage** (if applicable)
6. **The question for the board** — explicit single decision being asked
7. **Treatment options under consideration** — 2-3 alternatives with rationale
8. **Anticipated discussion points** — 2-3 things you expect the board to weigh in on
9. **Outcome decision** (filled in after the discussion)

## Packet header

- Date, attendees, standing references (e.g., institutional treatment protocols)

## Hard rules

- **NO PHI in any case packet.**
- **Outcome field filled in for every case** — administrative discipline matters.
- **Decision question explicit** — boards stall when this is unclear.
- **Format matches institutional retention requirements.**

## What I will NOT accept

- Templates that allow PHI to creep in
- Missing outcome field
- Vague decision questions
```

## Expected output

Packet header template + per-case template, consistent format.

## Required human verification

- **Verify no PHI** in any case before circulating.
- Confirm outcome field is filled for every case (admin discipline).
- Match retention requirements.

## Best model and why

**Claude Sonnet 4.6** — template generation. PHI discipline matters more than model choice.
""")

write_file(f"{P3}/conferences-and-journal-clubs/conference-schedule.md",
    {"title":"Conference schedule and topic rotation","pillar":"educational-operations",
     "event_type":"conference","audience":"faculty","difficulty":"quick-win","time_to_use":"2-10min",
     "visual":"text-only","tags":"schedule, topic-rotation, presenter-balance","verified_models":"TODO",
     "best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this prompt does

Generates a quarterly or annual conference schedule with topic rotation across subspecialties, balanced presenter loads, required-topic coverage, and buffer sessions. Includes a draft invitation email template.

## When to use it

Annually when planning the academic year's conference series, or quarterly for shorter cycles.

## The prompt

```
You are generating a conference schedule. Balance topics across subspecialties, balance presenter loads, include buffer sessions, and confirm with each presenter before publishing.

## What I'm building

- **Conference series name:** [e.g., "Tuesday morning CP didactics"]
- **Audience:** [target + level]
- **Frequency:** [weekly / biweekly]
- **Number of sessions to fill:** [N]
- **Available presenters:** [list with subspecialties and rotation availability]
- **Required topic coverage:** [subspecialties or specific topics that must be covered, e.g., RISE prep blocks]
- **Standing items:** [recurring slots — journal club every Nth week, in-service review, etc.]

## What to produce

### Full schedule
Date, topic, presenter, any pre-reading.

### Balance check
- Distribution of topics across subspecialties
- Flag if some subspecialties are over- or under-represented; suggest adjustments

### Presenter load check
- Distribution of sessions per presenter
- Flag if any presenter is overloaded (>X sessions in Y weeks)

### Buffer sessions
- 1-2 unscheduled or flexible sessions per quarter for guest speakers, schedule slips, or topic substitutions

### Logistics
- Room, AV needs, recording status, attendance tracking

### Invitation email template
Draft email I can use to invite each presenter with their assigned date and topic.

## Hard rules

- **Verify presenter availability before publishing.** Model can suggest; you must confirm.
- **Buffer sessions are non-optional.**
- **Sequencing constraints respected** (e.g., RISE prep BEFORE the exam, not after).

## What I will NOT accept

- Schedule that assumes presenters are available without verification
- No buffer sessions
- Required-coverage topics scheduled at suboptimal times
```

## Expected output

Schedule + balance check + presenter load check + buffer + logistics + invitation template.

## Required human verification

- **Verify each presenter's availability before publishing.**
- Confirm room and AV bookings.
- Validate sequencing against constraints.

## Best model and why

**Claude Sonnet 4.6** — schedule planning with constraints.
""")

# ===========================================================================
# WORKED EXAMPLES — refine 3
# ===========================================================================

write_file("library/pillar-1-self-education/examples/spep-self-quiz.md",
    {"title":"Worked example — Self-quizzing through SPEP interpretation","pillar":"self-education",
     "event_type":"n/a","audience":"resident","difficulty":"intermediate","time_to_use":">10min",
     "visual":"multimodal","tags":"spep, ife, self-quiz, paraprotein, worked-example, multimodal",
     "verified_models":"Claude Sonnet 4.5, GPT-4o","best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this example shows

A 22-minute self-quizzing session through SPEP and follow-up IFE interpretation. The user is a PGY-2 in their first week of clinical chemistry. **The goal is not to get the diagnosis** — it is to drill the interpretive reflex: see a pattern → generate a differential → narrow systematically → critique the reasoning.

The session uses three prompts in sequence — **calibrate** → **deepen** → **drill** — chained in a single conversation so the model maintains its mental model of the user across turns. Every model exchange is shown verbatim. Annotations in *italics* show what the user did well, what they corrected, and where they had to push back.

This is the most useful structure of any Pillar 1 example because it demonstrates the *chaining* pattern that distinguishes effective AI study from one-shot queries.

## Setup

- **User:** PGY-2 resident, week 1 of CP/clinical chemistry rotation
- **Source material:** A SPEP gel and densitometry trace from a published teaching case (de-identified, public-domain — provenance confirmed before upload)
- **Tools:** Claude Sonnet 4.6 with image attachment; single conversation thread
- **Time invested:** 22 minutes
- **Outcome:** correctly identified IgG-kappa monoclonal gammopathy of undetermined significance vs early myeloma; one model correction caught; one model hedge pushed back on

## Turn 1 — Calibrate

> **User:** I'm a PGY-2 in my first week of clinical chemistry. I've read the chapter on serum protein electrophoresis once. I can identify the five major regions on a normal trace but I have not yet practiced interpreting abnormal patterns.
>
> I'm going to show you a SPEP and I want you to **quiz me before you tell me anything**. Ask me one question at a time, starting from the broadest observation and narrowing. Wait for my answer each time. Do not give me the answer until I tell you I'm stuck.

*Annotation: the calibration is doing three things simultaneously — declaring level (PGY-2, week 1), declaring goal (drill, not lecture), and setting the interaction protocol (one question at a time, wait for answer). Without the explicit protocol declaration, the model defaults to dumping the full interpretation at once. The protocol is the entire point of the chained approach.*

> **Model:** Got it. Looking at the trace you've attached, here's my first question:
>
> Before we get into the diagnostic interpretation, can you describe what you observe in the **gamma region** compared to a normal trace? Just describe the shape, not the diagnosis.

## Turn 2 — User answer + deepen

> **User:** The gamma region has a tall, narrow spike that is much sharper than a normal polyclonal gamma hump. The base of the spike is narrow — it looks like a single column rather than a broad mound.

> **Model:** Good — that's the key observation. The narrow base is what separates this from a polyclonal increase. Next question:
>
> Given that morphology, what are the **two broad categories** of paraprotein you should be thinking about, and how do they differ in clinical implication?

*Annotation: the model correctly named the next layer without skipping ahead. It also reinforced the discriminating feature ("narrow base") — exactly the kind of repetition that builds the interpretive reflex.*

> **User:** The two broad categories are monoclonal gammopathy of undetermined significance (MGUS) and a malignant plasma cell disorder, most commonly multiple myeloma. MGUS has a lower paraprotein level (usually under 3 g/dL), no end-organ damage, and bone marrow plasma cells under 10%. Multiple myeloma has higher paraprotein, end-organ damage (CRAB), and ≥10% plasma cells on marrow.

> **Model:** Correct on the discriminators. One small refinement: you should also be thinking about **smoldering multiple myeloma** as the intermediate category between MGUS and overt myeloma — same higher paraprotein and marrow plasma cells as myeloma but without end-organ damage. Worth knowing because the management is different.
>
> Next question:
>
> What is the next test you would order to characterize this spike, and what specifically would it tell you?

## Turn 3 — Drill

> **User:** I would order an immunofixation electrophoresis (IFE). It would tell me the heavy chain class (IgG, IgA, IgM, IgD, IgE) and the light chain type (kappa or lambda) of the paraprotein.

> **Model:** Right. I'm attaching the IFE result for this same patient now. Tell me what you see — and again, describe before diagnosing.

*Annotation: the user uploaded the IFE; the model's next response described the band positions and asked the user to interpret. The full session continued for another 14 turns through bone marrow biopsy interpretation, free light chain ratio, and a discussion of when to refer to hematology. Truncated here for length — the pattern is the lesson.*

## Two correction moments

### Correction #1 — model overstated MGUS safety

In turn 6 (not shown), the model wrote: "**MGUS is benign**." The user pushed back:

> **User:** MGUS isn't benign — it carries a ~1%/year risk of progression to myeloma. "Benign" is the wrong frame.

> **Model:** You're right, my apologies — that was imprecise. MGUS is **clinically asymptomatic** but is not biologically benign — it carries roughly 1% per year progression risk to overt plasma cell neoplasm, with cumulative risk that becomes meaningful over decades. The phrase I should have used was "asymptomatic" or "premalignant," not benign.

*Annotation: this is the most important moment in the transcript. Self-education with AI requires the user to catch the model's confident errors. The model's correction was graceful; the user's catch was correct. Both matter.*

### Correction #2 — model tried to skip ahead

In turn 10 (not shown), after the user had committed to "IgG kappa monoclonal gammopathy", the model started a paragraph on **treatment** for symptomatic myeloma. The user redirected:

> **User:** I'm not at treatment yet — I want to stay on interpretation. What does the marrow biopsy report add that I haven't already integrated?

> **Model:** Fair pull-back — let me stay on interpretation. Looking at the marrow report you described...

*Annotation: the model's instinct to "complete" the case (move forward to clinical management) competed with the user's drill goal. The user enforced the boundary. This is normal — the model doesn't know the user's specific learning goal unless reminded.*

## What the user did well

1. **Set the interaction protocol up front.** "Ask me one question at a time, wait for my answer" prevents the model from defaulting to a complete answer dump.
2. **Described before diagnosing.** Even when the diagnosis was obvious, forcing morphologic description first mimics the reading rhythm of an experienced pathologist.
3. **Pushed back on model overstatement** ("benign") and on model scope creep (moving to treatment). Both pushes preserved the drill.
4. **Used a single conversation thread** so the model maintained context. Re-starting fresh between turns would have lost the calibration.

## What this example does NOT show

- This is a **study transcript**, not a clinical workflow. The trace was a published teaching case. **No real patient was involved.**
- The model's interpretations were correct in this case — but they could have been wrong, and the user was responsible for verification against the published answer key.
- This pattern (calibrate → deepen → drill) is not the right shape for every learning task. Use it for *interpretive* skill-building; for *recall* tasks, use the MCQ generation or Anki prompts instead.

## How to use this example

If you're a CP resident in your first month, use this transcript as a template:

1. **Find a published SPEP teaching case** (atlas, society teaching set, public-domain case repository).
2. **Open a fresh conversation** with your preferred model (Claude Sonnet 4.6 or comparable).
3. **Paste the calibration prompt** (Turn 1 above), substituting your level and the specific image.
4. **Drill through 5-10 turns**, enforcing the one-at-a-time protocol.
5. **End with a check question** like: "Based on this session, what's the one concept I'm still weakest on?"

If you're a faculty member, this transcript is a useful model for what to encourage residents toward. The transcript can also be used as a teaching artifact in a "how to study with AI" session.

## Related prompts

- [SPEP / IFE trace interpretation walkthrough](library.html#/library/pillar-1-self-education/prompts/multimodal-spep-ife)
- [Self-quiz one at a time](library.html#/library/pillar-1-self-education/prompts/self-quiz-one-at-a-time)
- [Concept explanation at level](library.html#/library/pillar-1-self-education/prompts/concept-explanation-at-level)
- [Guardrails](library.html#/docs/guardrails)
""")

write_file("library/pillar-2-teaching/examples/pgy2-transfusion-reaction.md",
    {"title":"Worked example — Designing a PGY-2 transfusion reaction teaching session","pillar":"teaching",
     "event_type":"n/a","audience":"faculty","difficulty":"intermediate","time_to_use":">10min",
     "visual":"text-only","tags":"transfusion, vignette, mcq, teaching-session, worked-example",
     "verified_models":"Claude Sonnet 4.5, GPT-4o","best_model":"Claude Opus 4.7","last_updated":TODAY},
    """## What this example shows

A 35-minute design session where a CP faculty member built a 50-minute small-group teaching session on transfusion reactions for PGY-2 residents in their first month of blood bank. The session uses one ambiguous case vignette and three matched MCQs.

The example shows three things side by side:

1. **The input prompt** — what the faculty member asked for
2. **The AI-generated draft** — what came back
3. **The faculty edits** — what changed, and why each change matters

**The point of showing the edits is that the model's first draft is structurally plausible but pedagogically generic.** The discriminating features that make a vignette *teachable* — the deliberately ambiguous fever onset, the wrong distractor that resembles a common misconception, the matched-pair logic — are judgment calls a human teacher has to make.

This is the most important example in Pillar 2 because it shows the **edit-as-discipline** pattern: AI gives you the scaffold; you supply what makes the session land.

## Setup

- **Faculty member:** CP faculty, ~10 years on blood bank service
- **Audience:** 4 PGY-2 residents in their first month of blood bank
- **Format:** 50-minute small group; 1 vignette + 3 MCQs + discussion
- **Tool:** Claude Opus 4.7 (chosen for nuanced vignette generation)
- **Time invested:** 35 minutes (8 min prompt drafting + 2 min generation + 20 min editing + 5 min final review)
- **Outcome:** A vignette that residents reliably get wrong in instructive ways; 3 MCQs that produce discussion rather than rapid agreement

## Input prompt

> I'm a CP faculty member designing a 50-minute small-group session for PGY-2 residents in their first month of blood bank. The learning objective is: "Given a transfusion reaction scenario, the resident will distinguish between febrile non-hemolytic, acute hemolytic, and TRALI reactions based on the temporal pattern and clinical findings, and will name the immediate management steps for each."
>
> Generate **one case vignette** where the reaction type is intentionally ambiguous between febrile non-hemolytic and acute hemolytic. The vignette should be 4-6 sentences. Then generate **three MCQs** based on the vignette. The first MCQ should test recognition of the reaction type, the second should test the next best management step, and the third should test the underlying mechanism. For each MCQ, provide all 4 answer choices and a rationale for each choice.
>
> Calibrate to a PGY-2 — appropriate complexity, no esoteric distractors. Use SI units. Do not use any patient names or institutional identifiers.

*Annotation: the prompt is doing several things right — naming the level explicitly, naming the cognitive challenge (ambiguity), specifying length, specifying calibration. What it's NOT doing well: it doesn't ask the model to identify the discriminating feature that makes the case ambiguous, or to suggest a teaching beat for the discussion. The faculty member learned to add these in subsequent uses.*

## AI-generated draft (Claude Opus 4.7)

### Vignette

> A 58-year-old patient receiving the second unit of packed red blood cells for symptomatic anemia develops a temperature rise from 37.0°C to 38.5°C approximately 45 minutes into the transfusion. The patient reports mild chills but no back pain. Blood pressure is 118/76 mmHg, heart rate is 92 bpm, oxygen saturation is 98% on room air. The transfusion is paused.

### MCQ 1 — Most likely reaction type

> A. Febrile non-hemolytic transfusion reaction *(correct)*
> B. Acute hemolytic transfusion reaction
> C. TRALI
> D. Allergic reaction
>
> Rationale A: Fever ≥1°C above baseline without hemodynamic instability, hypoxia, or back pain is most consistent with FNHTR.
> Rationale B: Acute hemolytic reactions classically present with fever AND hypotension, back pain, hemoglobinuria.
> Rationale C: TRALI presents within 6 hours of transfusion with hypoxia and bilateral pulmonary infiltrates.
> Rationale D: Allergic reactions present with urticaria, pruritus, and in severe cases bronchospasm.

### MCQ 2 — Next best step

> A. Restart transfusion at slower rate
> B. Administer epinephrine
> C. Send patient and unit samples to blood bank for workup *(correct)*
> D. Premedicate with diphenhydramine and restart
>
> *[rationales follow]*

### MCQ 3 — Mechanism

> A. Recipient antibodies against donor leukocyte HLA antigens *(correct)*
> B. ABO incompatibility with intravascular hemolysis
> C. Donor antibodies against recipient HLA antigens in the lung
> D. IgE-mediated mast cell degranulation
>
> *[rationales follow]*

## Faculty edits — annotated

### Vignette edits

The faculty member made three substantive changes:

1. *Original: "approximately 45 minutes into the transfusion."*
   **Edited to: "approximately 25 minutes into the transfusion."**
   *Reason: 45 minutes makes the case too easy — it sits comfortably in FNHTR territory. 25 minutes is in the overlap window where both FNHTR and an early acute hemolytic reaction are reasonable. The point of the case is to BE ambiguous; the model produced an unambiguous case.*

2. *Original: "but no back pain."*
   **Edited to: "no back pain reported. Patient is sedated for end-stage liver disease and unable to give a reliable subjective history."**
   *Reason: removing the patient's ability to self-report ambiguates the case appropriately. This forces the resident to rely on the objective findings — which is the actual clinical situation residents face. The model's case was too clean.*

3. *Original: "blood pressure is 118/76 mmHg"*
   **Edited to: "blood pressure is 102/68 mmHg (was 124/76 mmHg pre-transfusion)."**
   *Reason: a borderline drop is exactly the kind of finding that distinguishes a teachable vignette from a giveaway. The resident has to decide whether a 14-point drop matters in this context.*

### MCQ 1 edits

After the vignette edits, the faculty member **flipped the correct answer** to "acute hemolytic transfusion reaction" and rewrote the rationales to emphasize:

- The "1°C above baseline" criterion alone is **necessary but not sufficient** for FNHTR
- A blood pressure drop, even a small one, in a patient who can't self-report **forces the workup**
- The discriminating principle: *when in doubt, treat as the worse possibility until disproven*

*Annotation: this is the highest-value edit in the entire example. The model's vignette and MCQ were internally consistent (FNHTR) but pedagogically wrong (too easy). The faculty member changed both together to preserve internal consistency while shifting the cognitive challenge.*

### MCQ 2 edits

The faculty member kept the MCQ structure but added a discussion note for the facilitator:

> Even residents who correctly pick C ("send to blood bank") often skip the **most time-sensitive step BEFORE that**: maintain IV access with normal saline (NOT the blood bag's tubing — change it) and send a urinalysis for free hemoglobin. Use this as a teaching moment about prioritization, not just identification.

*Annotation: the model produced a question with one correct answer. The faculty member added a layer the model didn't think to add — what experienced clinicians do before sending the workup. This is the kind of judgment-derived content the model cannot generate.*

### MCQ 3 — distractor revision

The faculty member kept this MCQ largely as drafted but revised one distractor:

> Replace D ("IgE-mediated mast cell degranulation") with "**Cytokine release from donor leukocytes accumulated during storage**".
>
> This is a much more dangerous distractor because it's actually a *contributing mechanism* to FNHTR — it lets you ask a follow-up question about why leukoreduction reduces FNHTR risk, even though the primary mechanism in the chosen scenario is now acute hemolytic.

*Annotation: an obvious throwaway distractor (D-original) gives residents a free elimination. A plausibly-related distractor (D-revised) requires thought and opens a path to a deeper teaching moment.*

## Final teaching-ready output

After ~20 minutes of editing, the faculty member had:

- A vignette that requires the resident to integrate three pieces of evidence (timing, BP drop, inability to self-report)
- Three MCQs that progress from recognition → action → mechanism
- A facilitator note that surfaces a common cognitive shortcut (jumping to workup without IV access and free-hemoglobin urinalysis)
- One distractor revision that opens a path to a follow-up question on leukoreduction

**Time saved vs starting from scratch: ~30 minutes.** Time spent editing: ~20 minutes. **Net: ~10 minutes saved, plus a more pedagogically deliberate session** than the faculty member would have built under time pressure.

## What this example does NOT show

- This is not a session designed for a board exam. The MCQs are pedagogical; they would not necessarily pass psychometric review.
- The model did not generate the *teaching judgment* — when to make a case ambiguous, when to keep a distractor mild, when to add a facilitator note. That came from the faculty member.
- A separate review pass for **demographic representation** (age, sex, race) across a series of cases is needed at the course level, not the single-case level. See [Guardrails](library.html#/docs/guardrails).
- The faculty member knew transfusion reactions cold. **If you don't know the topic deeply, the model's first draft will fool you.** This pattern is most useful for topics within your active expertise.

## How to use this pattern

For your own teaching session design:

1. **Draft the prompt** using the [Case vignette at PGY level](library.html#/library/pillar-2-teaching/prompts/case-vignette-pgy) prompt as a template
2. **Generate** — but read the output as a STARTING SCAFFOLD, not a finished session
3. **Pressure-test for ambiguity** — is the case too easy? Too hard? Right shape?
4. **Edit the vignette FIRST**, then re-align the MCQs to match
5. **Add facilitator notes** that capture judgment the model can't generate
6. **Pressure-test with a co-faculty** colleague before delivery

## Related prompts

- [Case vignette at PGY level](library.html#/library/pillar-2-teaching/prompts/case-vignette-pgy)
- [Matched case pair — reactive vs neoplastic](library.html#/library/pillar-2-teaching/prompts/matched-case-pair)
- [Bloom's taxonomy MCQ generation](library.html#/library/pillar-2-teaching/prompts/blooms-mcq)
- [Guardrails](library.html#/docs/guardrails)
""")

write_file("library/pillar-3-educational-operations/examples/coag-rotation-orientation.md",
    {"title":"Worked example — Coagulation rotation orientation packet","pillar":"educational-operations",
     "event_type":"rotation","audience":"program-director","difficulty":"intermediate",
     "time_to_use":">10min","visual":"text-only",
     "tags":"rotation, orientation, coagulation, packet, worked-example",
     "verified_models":"Claude Sonnet 4.5, GPT-4o","best_model":"Claude Sonnet 4.6","last_updated":TODAY},
    """## What this example shows

A program director used AI to draft a coagulation rotation orientation packet for a 4-week PGY-3 rotation. Total work: ~25 minutes — 8 minutes to write the input prompt, 2 minutes for the model to generate the draft, 15 minutes of editing.

The example shows the **input → draft → final** progression with side-by-side commentary on what was kept, what was rewritten, and what was deleted entirely. The most important pattern: **institutional vocabulary, judgment-derived pitfalls, and named contacts** are content the model fundamentally cannot generate — only humans with operational knowledge of the rotation can supply them.

This is the most useful example in Pillar 3 because it demonstrates the **scaffold-and-replace** pattern that's the right model for educational operations work: AI builds the structure; you replace the placeholder content with the substance that makes it usable.

## Setup

- **PD:** CP program director, ~5 years in role
- **Rotation:** 4-week PGY-3 coagulation rotation at an academic medical center
- **Audience:** Incoming PGY-3 residents (4-6 per year)
- **Tool:** Claude Sonnet 4.6
- **Time invested:** 25 minutes total
- **From-scratch comparison:** ~90-120 minutes for the same packet
- **Net savings:** ~70-95 minutes, plus better structure than under-time-pressure first drafts

## Input prompt

> I'm a CP program director. Generate a 4-page rotation orientation packet for a 4-week PGY-3 coagulation rotation at an academic medical center with a high-volume special coagulation lab. The packet should include:
>
> 1. A welcome paragraph (3-4 sentences, professional but human)
> 2. Rotation goals (5 bullets, milestone-aligned)
> 3. Weekly schedule template (typical Monday-Friday — sign-out at 8 am, didactics, case review, protected reading time, end-of-day wrap-up)
> 4. Key contacts (lab director, attending, fellow, charge tech, scheduler) — use placeholders for names
> 5. Required reading for week 1 (5 references) with one-sentence rationale per reference
> 6. Common pitfalls (3 specific to PGY-3s starting coag)
> 7. What success looks like by the end of week 1, week 2, week 4
>
> Use SI units. Use the phrase "the resident will" for objectives. Do not use any patient names or institutional identifiers.

*Annotation: the prompt is doing the prompt-engineering work well — specifying length, structure, level, formatting conventions, and what NOT to include. What it doesn't do (and what the PD added in subsequent uses): ask the model to explicitly flag which sections will need institutional substitution.*

## AI-generated draft (excerpted)

### Welcome to the Coagulation Rotation

> Welcome to your four weeks on the coagulation service. This rotation will give you hands-on experience interpreting routine and special coagulation testing, participating in patient management discussions with hematology and surgery teams, and developing the diagnostic reasoning skills needed for an independent CP practice. We are excited to have you, and we expect a lot of you — both are true.

### Rotation goals

> By the end of the rotation, the resident will:
>
> - Interpret routine coagulation testing (PT, aPTT, fibrinogen, D-dimer) and identify patterns suggestive of common acquired and inherited bleeding disorders.
> - Order and interpret a focused workup for a patient with isolated prolonged aPTT, including mixing studies and factor assays.
> - Distinguish DIC from other consumptive coagulopathies using laboratory and clinical findings.
> - Recognize and triage critical coag values, including appropriate communication with the clinical team.
> - Participate in at least three coag consults per week with progressive autonomy.

*[Rest of the draft followed the requested sections.]*

## Faculty edits — what changed and why

### Welcome paragraph: KEPT verbatim

The draft welcome paragraph was kept exactly as written. "We are excited to have you, and we expect a lot of you — both are true" was the one line the PD wanted to keep. *The model's; not the PD's.*

*Annotation: this is unusual — most AI-generated openings get rewritten. The model's phrasing of "both are true" struck the PD as exactly right for the tone he wanted. Worth keeping when it lands.*

### Rotation goals: 3 of 5 kept, 2 substantively rewritten

**Kept:**
- PT/aPTT/fibrinogen/D-dimer interpretation goal
- Isolated prolonged aPTT workup goal
- DIC distinction goal

**Rewrote goal 4** (critical values):

> Original: "Recognize and triage critical coag values, including appropriate communication with the clinical team."
>
> **Edited to: "Manage the panic-value workflow for critical INR and fibrinogen results, including triggering the institutional reversal protocol where appropriate, documenting the call in the LIS, and following up on disposition by end of shift."**

*Annotation: "appropriate communication" is the kind of vague language the model defaults to. The PD replaced it with the specific institutional workflow — the panic value, the reversal protocol, the LIS documentation, the end-of-shift follow-up. **This is content the model fundamentally cannot generate** because it depends on knowing the institution.*

**Rewrote goal 5** (autonomy gradient):

> Original: "Participate in at least three coag consults per week with progressive autonomy."
>
> **Edited to: "By week 4, the resident will independently formulate the workup plan and recommendation for routine consults, with attending review only at the final sign-out step."**

*Annotation: "progressive autonomy" is empty. The edited version specifies the endpoint — independent workup formulation by week 4 — which is assessable.*

### Required reading: 4 of 5 kept, 1 swapped

The model drafted a reasonable reading list:
- 2 current textbook chapters
- 2 ISTH guideline summaries
- 1 recent review article on lupus anticoagulant testing

The PD swapped one of the items:

> **Removed:** The recent review article on lupus anticoagulant testing (good, but not the most important on day 1)
>
> **Replaced with:** The institutional massive transfusion protocol document — not findable to the model, and the most important single document for a resident on this rotation.

*Annotation: this swap is the most common pattern in operations editing. The model defaults to publicly available references; the most important documents for a real rotation are often institutional.*

### Common pitfalls: REWROTE ENTIRELY

The model's drafted pitfalls were generic:
- "Don't rely on a single value"
- "Remember to consider pre-analytical factors"
- "Always think about the clinical context"

The PD replaced them with three specific failure modes she had seen in residents:

> 1. **Reflexive mixing study on every prolonged aPTT.** A prolonged aPTT in a patient on heparin doesn't need a mixing study — confirm heparin contamination first.
> 2. **Calling a panic INR without checking the medication list.** The PD wants to know about the warfarin dose change before being woken up at 2 am about an INR of 5 on a stable outpatient.
> 3. **Treating D-dimer as a diagnostic test.** D-dimer is a screening test with a high negative predictive value, not a positive predictive one. Residents in their first week routinely overstate the meaning of a positive D-dimer.

*Annotation: these pitfalls are **judgment-derived** — they come from watching residents make the same mistakes over years. **The model cannot generate them.** This is the most reliable rule of thumb: anything that requires longitudinal observation of trainees is content you supply, not content AI generates.*

### "What success looks like" section: structure kept, milestones customized

The model drafted reasonable week 1 / week 2 / week 4 milestones. The PD kept the structure but tightened the week 4 milestone to align with her program's milestone sub-competency language for CP-3 (Laboratory Operations and Quality Assurance).

## Time accounting

| Step | Time |
|------|------|
| Writing the input prompt | 8 min |
| Model generation | 2 min |
| Reading + first edit pass | 8 min |
| Inserting institution-specific content | 5 min |
| Final polish | 2 min |
| **Total** | **25 min** |

Estimated time from-scratch: 90-120 minutes.
**Net savings:** ~70-95 minutes.

## What this example does NOT show

- The model cannot generate **institutional vocabulary** — protocol names, contact roles, specific LIS workflows. Every PD needs to bring these.
- The model cannot generate **judgment-derived pitfalls** that come from watching residents make the same mistakes for years.
- The packet still needs to be **reviewed by the lab director and the chief technologist** before distribution — for accuracy and for buy-in. AI does not change the institutional review process; it only changes the time to first draft.
- This was a relatively well-scoped rotation. A more complex rotation (multi-service, longer duration, more attendings) would require more editing.

## How to use this pattern for other rotations

The same input-prompt structure works for any rotation. Replace "coagulation" with "blood bank", "microbiology", "chemistry", "hematopathology" — the model will produce a structurally similar draft. **The judgment-derived sections (pitfalls, institutional specifics, autonomy gradient) are what you bring.**

Rule of thumb: **expect to rewrite the "common pitfalls" section entirely**, swap 1-2 reading list items, and customize the autonomy gradient. The welcome paragraph, schedule template, and overall structure are usually fine as drafted.

## Related prompts

- [Rotation orientation one-pager](library.html#/library/pillar-3-educational-operations/prompts/rotations/orientation-onepager) — for the shorter one-page version
- [Rotation expectations document](library.html#/library/pillar-3-educational-operations/prompts/rotations/expectations-doc) — for the formal handbook version
- [Rotation reading list with rationale](library.html#/library/pillar-3-educational-operations/prompts/rotations/reading-list)
- [Daily schedule template](library.html#/library/pillar-3-educational-operations/prompts/rotations/daily-schedule)
""")

# ===========================================================================
# Done
# ===========================================================================

print("Batch 4 (FINAL) done — 22 items:")
print("  Workshops (8): announcement-registration, pre-workshop-survey,")
print("    facilitator-runofshow, station-by-station-guide, badge-design-spec,")
print("    access-card-layout, certificate-of-completion, post-workshop-thank-you")
print("  Rotations (6): orientation-onepager, reading-list, daily-schedule,")
print("    mid-rotation-feedback, end-of-rotation-evaluation,")
print("    resident-to-resident-handoff")
print("  Courses (3): weekly-module-packet, feedback-collection-form,")
print("    course-postmortem")
print("  Conferences (2): tumor-board-case-packet, conference-schedule")
print("  Worked examples (3): spep-self-quiz, pgy2-transfusion-reaction,")
print("    coag-rotation-orientation")
