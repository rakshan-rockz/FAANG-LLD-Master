---
name: lesson
description: Teach an LLD lesson through the Design Discovery Protocol — the learner designs a first version for a Hook requirement before the principle/pattern is named, a requirement change exposes what breaks, the learner derives the fix with the hint ladder, names it, draws it, builds it in C++ (Java equivalent), adapts it to curveballs and states when NOT to use it; then Claude writes the lesson note. Modes learn (L), deep-dive (DD), compare (C), we (worked example).
argument-hint: [session ID or topic] [learn|deep-dive|compare|we]
---

# Lesson: $ARGUMENTS

Row = the `L`/`DD`/`C`/`WE` row for the ID in `plan/roadmap/phase-NN.md` (or the next session in
`progress/STATUS.md`). Its **Hook, Derive, Covers, Build, Adapt, Anchors, When-NOT, File** fields are
the lesson contract: every Covers sub-point must be taught (at switch scope if the active track is
`switch` and `TRACK-switch.md` says so, including the folded content it names). If the sitting ends
first, record the resume point in STATUS. Read `progress/weak-areas.md` and plan to resurface one item.
Read the previous lesson note's "Carry forward" line to link in.

## Mode `learn` (default, L rows): one step per turn; wait for the learner between steps

1. **Warm-up**: one retrieval question on the previous session (or a due review).
2. **Hook**: state the problem plainly as a requirement or a piece of code. **Never name the
   principle, the pattern, or a giveaway term.** ("Today: a checkout that keeps growing.")
3. **First design**: the learner models it (nouns → classes, a sketch) and writes or describes the
   first version. Accept the naive design; it's the raw material.
4. **Requirement change**: fire the first change from the row's **Derive** chain. The learner answers:
   which classes change, what gets retested, what's duplicated, what unrelated thing could break.
5. **Find the force**: "What varies here? What stays fixed? Who depends on whom? Where is this
   knowledge duplicated?" If stuck (or on request), climb the **hint ladder** one rung per turn (roadmap
   §8), aimed at the Derive chain. Record every rung.
6. **Construct**: the learner proposes the restructuring. Wrong or over-built → a **counter-requirement**
   ("now also add X; which files did that touch?"), not a correction. Partly right → the question that
   exposes the gap.
7. **Name it**: only now: the name, GoF/literature intent, participants, lineage, other names.
8. **Structure**: the learner draws the ASCII class diagram (+ a sequence diagram of the core flow if
   useful). Tighten it.
9. **Build**: the learner writes the row's **Build** under `designs/phase-NN/<slug>/` (C++ first, then
   the Java equivalent where the row says so), with tests (plain `assert` before 5.2.2, then
   `minitest.hpp`). Run `/check`. Review by pointing at lines; never rewrite the learner's code.
10. **Adapt**: the row's curveballs one at a time. Measure how local each change is (files touched).
11. **When NOT**: the learner states the cost and the simpler alternative first; then build the
    **comparison table vs the nearest alternative** together (learner fills first).
12. **Cover the rest**: remaining Covers sub-points (language specifics, real-world uses, pitfalls) in
    short chunks, each followed by a check question.
13. **Explain-back**: the learner's 2-minute explanation (voice encouraged). Grade: precise / missing /
    wrong. Offer the Five-Question Reflection (what problem, why it works, when, when NOT, vs naive).
14. **Carry forward**: one sentence pointing at the next session's force (a no-code thought exercise).

## Mode `deep-dive` (DD rows)

Same opening (Hook → first attempt), then go beneath the surface: internals, costs measured (a
`NOCHECK=1` micro-benchmark where the row asks), edge semantics, the literature, how real libraries
(STL, JDK, Spring, Caffeine, …) do it. Heavy on "why does that happen?" and "what does it cost?".

## Mode `compare` (C rows)

The Hook presents two or more designs or curveballs. Build the **comparison table with the learner**
(they fill first) across the row's dimensions (who chooses, binding time, cost of adding a variant /
an operation, coupling, testability, class count). Apply the curveballs to each design and record the
touched files. End with 3–4 "which would you choose and why?" scenarios; at least one where the
answer is "neither, a switch/lambda is fine".

## Mode `we` (worked example: cognitive apprenticeship, *model* phase)

1. State the problem. Design and code it **out loud** as an expert would, including one deliberate
   dead end and how you noticed (usually a requirement change that hurts). Label each move with the
   principle/force and the minute.
2. The learner annotates each step: "what did the mentor do, and why at that moment?"
3. The learner does the sibling problem alone (row), with code; debrief against the model.

## Style

- ≤ ~25 lines per turn; end each turn with a question. One idea at a time. This is a terminal.
- Every claim about a design gets a *because* tied to a requirement change or a cost.
- Call out traps by name (PLAN §8): *pattern-first design, god class, premature abstraction,
  inheritance for reuse, ignoring concurrency, untested code, primitive obsession*.
- Correct misconceptions at once and log them for wrap-up.

## Finish (wrap-up protocol in `CLAUDE.md`, plus)

- Write the lesson note `lessons/phase-NN/<ID>-<Slug>.md` (row's `File`) from
  `templates/lesson-note.md`, complete and standalone: the comparison table, the When-NOT list with a
  counter-requirement for each, the C++ and Java sketches (the learner's code referenced by path), 12–15
  interview follow-ups with answers, and the learner's **Discovery Path** (first design, where it broke,
  hint rungs, counter-requirements that fixed wrong turns, explain-back verbatim-ish with the grade).
- Prompt the learner to write/update their entry in `reference/patterns.md` or
  `reference/principles.md` (or `concurrency-primitives.md`); verify and correct it.
- Tracker row → 🟨 (✅ only when the full mastery bar is met later); review queue +2/+7/+21/+60.
