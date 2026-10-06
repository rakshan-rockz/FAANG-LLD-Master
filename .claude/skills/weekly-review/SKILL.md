---
name: weekly-review
description: End-of-cycle or end-of-phase review (R sessions) — explain-back and rebuild-back without notes, re-test weak areas, verify the learner-built references, compare case-study scores by rubric category, insert repeat sessions for anything not owned; monthly mode runs a cumulative checkpoint. Writes to reviews/.
argument-hint: [monthly]
---

# Review: $ARGUMENTS

1. Identify the cycle (or phase) from `progress/STATUS.md`. Read its rows in `plan/roadmap/phase-NN.md`,
   its lesson notes, `REVIEW.md` files and mock files since the last review, and `progress/weak-areas.md`.
   (On the switch track, R rows are deferred; run this skill anyway every ~2 weeks, or when the learner
   asks, over the switch rows done since the last review.)
2. Run it interactively. Ask, don't tell:
   - **Understanding**: for each concept in the cycle, a 1–2 min explain-back without notes, including
     when NOT to use it. Grade.
   - **Construction**: the 2 lowest-confidence items: rebuild-back from a blank file (a pattern's core
     in ≤ 10 min, or a case study's class diagram + core interface in ≤ 10 min).
   - **Recognition**: 5 unlabeled scenarios / snippets mixing this cycle with older phases.
   - **Scores** (Phase 8+): case-study and mock scores by rubric category: which category is weakest,
     and what habit fixes it?
   - **References**: the learner's entries in `reference/patterns.md` / `principles.md` /
     `concurrency-primitives.md` / `case-study-index.md` for this cycle: check them for accuracy and
     completeness (When-NOT filled? used-in filled?). Correct errors, don't fill blanks for them.
3. Re-test each open weak area briefly; resolve those answered correctly (second time).
4. Decide: anything that failed explain-back or rebuild-back gets a **repeat session** inserted before
   moving on (note it in STATUS as a remediation item). Nothing is carried forward half-learned.
5. If this closes the phase → the next session is the phase **Gate** (`/gate`); the learner draws the
   phase **concept map** (ASCII: concepts + labelled links such as "motivates", "is confused with",
   "prevents", "is built from").

## Monthly mode (every ~4–6 weeks, cumulative)

60–90 min over **everything** covered: 8 unlabeled recognition items, 2 rapid class-diagram rounds
(15 min each, one old domain, one recent), 2 cold explain-backs from the oldest ✅ rows, 1 kata redo,
1 "is this thread-safe?" snippet (from Phase 6 on). Compare with the previous checkpoint.

## Finish

Write `reviews/<phase>.<cycle>-review.md` (monthly: `reviews/YYYY-MM-monthly.md`) from
`templates/weekly-review.md`, then the wrap-up protocol in `CLAUDE.md`.
