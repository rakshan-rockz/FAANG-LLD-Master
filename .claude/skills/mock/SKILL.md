---
name: mock
description: Run a company-styled LLD mock interview — formats machine-coding (Flipkart/PhonePe/Razorpay/Swiggy 90 min + evaluation), code-design (Atlassian 60 min with mid-round extensions), lld-discussion (Amazon/Microsoft), concurrency (Uber-style), fundamentals (Adobe/Microsoft C++/Java), or a full loop; then debrief, /100 score and a mocks/ file. Also runs the sealed baseline (0.0.2) and its redo (11.3.1).
argument-hint: [session ID | company] [format] [baseline]
---

# Mock interview: $ARGUMENTS

Defaults: the `M` row's format and company; otherwise rotate companies from `progress/profile.md`.
Problems are **unseen**: never a case study from the roadmap, never a repeat (check `mocks/`), stated
in your own words, with no pattern-revealing wording. Interview conditions: cold, hints only when stuck
2+ turns and they cost points. Language: the learner's MC language (or the company's if the profile says so).

## `baseline` (0.0.2) and its redo (11.3.1)

**Vehicle Rental Service**, Flipkart-style, 90-min build + 15-min curveball + evaluation, zero hints,
strict. At 0.0.2: compose the full problem document at the start of the session (a realistic
Flipkart-style rental prompt: 5–6 must-haves + 2 bonus items) and choose one curveball that a good
design absorbs locally; write both into `mocks/YYYY-MM-DD-0.0.2-baseline.md` under "Sealed problem" and
**don't write them anywhere else** (not in this skill, the roadmap or the lesson notes). Debrief
= score + top 3 gaps only; **no model design shown**, so the redo stays fair. At 11.3.1: copy the sealed
problem and curveball exactly; same conditions; then a full debrief and a per-category comparison.

## Formats

- **machine-coding** (Flipkart / PhonePe / Razorpay / Swiggy / Walmart): a 1-page problem document
  with must-haves and bonus items; 90 min; the `/mc` Phase A flow in interviewer mode; curveball at ~70;
  then a 20–30 min evaluation discussion in character (walkthrough, "add X", concurrency, smells).
- **code-design** (Atlassian): start with a small core requirement; working, tested code expected;
  **extension 1 at ~25 min, extension 2 at ~45 min** (each changes requirements in a way a good design
  absorbs locally); readability and tests graded explicitly; 60 min.
- **lld-discussion** (Amazon / Microsoft / Salesforce): the `/lld-discuss` Phase A flow; Amazon adds a
  short Leadership-Principles-flavoured question about a real design decision the learner made.
- **concurrency** (Uber / Walmart / Microsoft): an LLD with a concurrency core + a 15-min concurrency
  coding question (ordering puzzle, blocking queue variant, rate limiter); "two requests at once: walk
  me through it" until the atomic unit and mechanism are stated.
- **fundamentals** (Adobe / Microsoft): 45-min OOD with code for the core + 15 min of language
  fundamentals (C++: virtual destructors, slicing, smart pointers, Rule of 5, move, const, atomics vs
  `volatile`; Java: `equals/hashCode`, `HashMap`/`ConcurrentHashMap` internals, `synchronized` vs
  `ReentrantLock`, `volatile`).
- **loop**: 2–3 back-to-back rounds of different formats/companies, one combined debrief.

Throughout: `date +%H:%M` at start and every phase boundary; per-phase timings recorded; one open weak
area woven into a follow-up.

## Debrief ("Interview over. Mentor hat on.")

1. Run the code and tests yourself (formats with code). 2. Strong / weak / missed, each with the
exposing requirement, input or interleaving. 3. The model design (except baseline) and how it could
have been discovered from where they were. 4. Score on the roadmap §9 rubric (LD weighting for
discussion formats), one line per category, strict; band. 5. 3 things to practise, each mapped to a
session type.

## Finish

Write `mocks/YYYY-MM-DD-<ID>-<company>-<format>.md` from `templates/mock-review.md` (problem statement in
full, timings, what happened, debrief, score, actions); the learner's code in `designs/mocks/<ID>-<slug>/`.
Tracker Mocks row (score, date); weak areas; resolve queue if < 65; STATUS; wrap-up protocol.
