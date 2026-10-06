---
name: gate
description: Run a phase exit gate from the roadmap — calibration predictions, concept map, then a cold test of every criterion with fresh prompts, builds and snippets; on the switch track only the non-deferred criteria plus any folded gates. Pass unlocks the next phase; any failure creates a targeted remediation cycle and a retry.
argument-hint: [phase number]
---

# Phase gate: $ARGUMENTS

Phase = argument, or the current phase in `progress/STATUS.md`. Read the **Gate** section at the bottom
of `plan/roadmap/phase-NN.md`, `progress/tracker.md`, the phase's lesson notes / `REVIEW.md` files and
`progress/weak-areas.md`.

**Track scope:** on the switch track, skip criteria marked *(switch: deferred)*, test those marked
*(switch: …)* at the stated scope, and add the criteria of any gate folded into this one (Gate 4 includes
Gates 2–3; Gate 11 includes Gate 10). Record which criteria were deferred so the depth pass tests them.

## Rules

- Interviewer mode. Cold: no notes, no hints (unless a criterion allows them), no teaching during the gate.
- Every criterion is tested with **fresh** prompts, snippets and builds not seen in lessons, critiques
  or case studies. Build criteria are compiled and run (`tools/run.sh`, `--test`, `stress.sh`).
- Score criteria (≥ 65, ≥ 70 …) use a fresh timed build or mock inside the gate, not old scores.
- May span several sittings. Record per-criterion progress in STATUS between sittings.

## Flow

1. Announce the gate and its criteria. **Calibration:** the learner predicts pass/fail and confidence
   1–5 per criterion. Record the predictions.
2. **Concept map** of the phase (required): critique missing or wrong links.
3. Test each criterion. Mark ✅ / ❌ with a 1-line reason.
4. Compare predictions with results; note systematic over- or under-confidence in `progress/profile.md`.
5. Result:
   - **All ✅** → gate passed: tracker Gates table (status, attempts, date); rows meeting the full
     mastery bar → ✅; next session = the next row on the active track; 2-min profile refresh.
   - **Any ❌** → write a **remediation cycle** into STATUS: for each failed criterion, the specific rows
     to redo (as harder variants, not replays), a fresh build or critique, and the weak area it maps to.
     Next session = the first remediation item. Retry = the failed criteria + one spot-check of a passed one.
6. Tell the learner plainly what passed, what didn't, and why. No softening, no discouragement.
   Attempts are unlimited.

## Finish

Wrap-up protocol in `CLAUDE.md`.
