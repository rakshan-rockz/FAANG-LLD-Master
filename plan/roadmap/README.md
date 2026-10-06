# Roadmap: Discovery-First, Mastery-Gated, Two Tracks

**Principle:** you advance by what you can *design, build, run and defend*, not by how many patterns
you have read about. Nothing is cut or skimmed from the depth track. The 🎯 switch track
(`TRACK-switch.md`) is an **ordering and scoping** of the same rows for the job switch. Nothing is
deleted, and the depth pass later picks up everything it deferred.

> **Motto:** *Don't memorise patterns. Feel the pain they remove, then invent them.*
> A pattern is not "learned" when you can draw its UML. It is learned when you can see the requirement
> change that calls for it in unfamiliar code, build it from a blank file, and say when it would be
> over-engineering.

---

## 1. Structure

```text
Phase  →  Cycles  →  Sessions  →  Gate
```

- **Phase** (0–11): a block in prerequisite order (OOP → principles → patterns → clean code & testing →
  concurrency → machine coding → interview mastery).
- **Cycle**: 3–9 sessions on one theme, closed by a review (`R`).
- **Session**: one sitting (see §3 for durations). Unfinished sessions **continue** at the next sitting.
- **Gate**: the end-of-phase exit test, run cold. Pass = every criterion met. Fail = a remediation
  cycle, then retry the failed criteria. Attempts are unlimited and carry no penalty.

## 2. Session IDs and row format

`<phase>.<cycle>.<n>`: e.g. `4.1.3` = Phase 4, Cycle 1, session 3. `progress/STATUS.md` holds the next ID.
`/today` resumes from it. Every phase file uses exactly this table shape (parsed by `tools/gen_tracker.py`):

```markdown
| ID | Type | Session |
|---|---|---|
| 4.1.3 | L | **State** — Hook: … · Derive: … · Covers: … · Build: … · Adapt: … · Anchors: … · When-NOT: … · 📖 HFDP ch10 · File: `lessons/phase-04/4.1.3-State.md` |
```

Fields (all required for `L` / `DD` / `C` rows, in this order; `MC` / `LD` rows reuse them with the
meanings in the right-hand column):

| Field | In a lesson row (`L` `DD` `C` `WE`) | In a case-study row (`MC` `LD`) |
|---|---|---|
| **bold title** | The principle / pattern / primitive | The system |
| **Hook** | A concrete design problem or requirement, stated *without naming the principle or pattern*. The learner designs (and often codes) a first version before anything is taught | The prompt exactly as the interviewer states it: short and deliberately under-specified |
| **Derive** | The chain the learner should reach: naive design → the requirement change that breaks it (what has to be edited, retested, duplicated) → the force behind the pain → the principle/pattern. The hint ladder steers toward it | The mentor's private map of the expected discovery: the entities, the core abstraction, the hard part, and the naive design that fails. **Never shown before the attempt** |
| **Covers** | Every sub-point that must be taught. None may be dropped | Must-have features + the concepts the build must exercise |
| **Build** | The runnable artefact the learner writes this session (C++, Java where noted), under `designs/phase-NN/<slug>/` | (in `File`) |
| **Adapt** | 2–4 **curveball requirement changes** that test Level 4: "now add X — what breaks, and how many files change?" | The curveballs. One is fired at ~minute 60 of the build, one in review |
| **Anchors** | Canonical exercises for this topic (katas, textbook examples, interview questions) | Where it's asked / known variants / company style |
| **When-NOT** | Overuse and anti-patterns: when this principle/pattern is over-engineering, and the simpler alternative | Over-engineering traps specific to this problem |
| **📖** | Reading assigned **after** the session (never before: attempt first) | — |
| **File** | The lesson note path | The design directory (code + `REVIEW.md`) |

Other rows: `K` rows give target time, spec and pass checks; `CR` rows list the planted flaws
(private to the mentor); `CL` rows give Build / Break / Stress; `R`, `M`, `Gate` rows are plain.

## 3. Session types

| Type | Name | Skill | Est. h | What happens |
|---|---|---|---:|---|
| `Intake` | Intake | `/intake` | 1.5 | Profile: level (SDE-2 confirmed), companies, MC language, C++/Java fluency, availability |
| `Baseline` | Baseline machine-coding mock | `/mock baseline` | 1.5 | Cold 90-min machine-coding round, sealed score. Redone identically at 11.3.1 |
| `L` | Discovery lesson | `/lesson` (learn) | 1.25 | The **Design Discovery Protocol** (§5) |
| `DD` | Deep dive | `/lesson` (deep-dive) | 1.5 | Beneath the surface: internals, costs, edge semantics, the literature |
| `C` | Compare | `/lesson` (compare) | 1.25 | Two or more alternatives that get confused (Strategy vs State, inheritance vs composition). Comparison table built with the learner, then "which would you pick?" scenarios |
| `WE` | Worked example | `/lesson` (we) | 1.25 | Mentor designs and codes out loud, narrating every decision and one dead end; learner annotates, then does a sibling problem alone. Cognitive apprenticeship: *model* |
| `K` | Kata | `/kata` | 0.75 | Implement a pattern / primitive / skeleton from a blank file, timed, compiled, tested (stress-tested if concurrent) |
| `MC` | Machine-coding case study | `/mc` | 3 | Timed build in interviewer mode (clarify → model → code → run → test) → curveball → mentor review → /100 score (§6) |
| `LD` | LLD discussion round | `/lld-discuss` | 1.5 | Whiteboard round, no full code: requirements, class diagram, key interfaces, core flow as a sequence diagram, trade-offs, extensibility and concurrency questions. Amazon/Microsoft OOD style |
| `CR` | Critique | `/critique` | 1 | Claude presents a confident but flawed design or code (god class, LSP violation, race condition, over-engineering…); the learner finds the flaws. Bloom's *evaluate* |
| `CL` | Concurrency lab | `/conc` | 2 | Write the concurrent code, then **break it** with stress runs and forced interleavings, fix it, and argue the invariant (§7) |
| `M` | Mock interview | `/mock` | 1.5 | Company-styled: machine coding, code design, LLD discussion, or concurrency round. Scored /100 |
| `R` | Review | `/weekly-review` | 1 | Explain-back and rebuild-back without notes, weak areas, learner references, repeat sessions if needed |
| `Gate` | Phase gate | `/gate` | 3 | Calibration → concept map → cold test of every criterion → pass or remediation |

`/check` (compile, run, test, stress, review the learner's code) and `/hint` (one rung) are used inside
any session. `/quiz` is the 15-minute floor day.

## 4. The mastery bar

A concept row becomes ✅ in `progress/tracker.md` only when **all five** hold. Until then it is 🟨.

| Level | Test | Where it's tested |
|---|---|---|
| 1. **Recognition** | In unfamiliar code or requirements, spots the smell / force / hazard that calls for it, and says why the nearest alternative is worse *here* | `CR`, `MC` reviews, gates |
| 2. **Understanding** | 2-minute explain-back: the problem it removes, how it works, its cost, **when NOT to use it** | end of `L`, `R` |
| 3. **Construction** | Builds it from a blank file, compiled and tested, without reference code | `Build` in `L`, `K`, gates |
| 4. **Adaptation** | Absorbs a curveball requirement with a *local* change (states which files change and why), or correctly decides the pattern is not worth it | `Adapt`, `MC`, `M` |
| + **Retention** | Passes the +21-day spaced review | review queue |

Case studies are ✅ when scored ≥ 80 (Hire band) cold. Confidence 1–5 is tracked separately.

## 5. The Design Discovery Protocol (how every `L` / `DD` / `C` session runs)

One step per turn. The learner acts first at every step that can be reasoned out.

1. **Retrieval warm-up**: due reviews; one question linking to the previous session.
2. **Hook**: state the concrete problem. **Do not name the principle or pattern.**
3. **First design**: the learner models it (entities, a sketch of classes) and writes or describes the
   first version. The naive design is welcome; it is what the lesson is built from.
4. **Requirement change**: the mentor fires the change from the row's **Derive** chain ("now add UPI
   and wallet payments"). The learner answers: *which classes change? what gets retested? what gets
   duplicated? what could now break that has nothing to do with the change?*
5. **Find the force**: what varies, what stays fixed, who depends on whom, which knowledge is
   duplicated. The hint ladder (§8) is used only if the learner is stuck.
6. **Construct**: the learner proposes the restructuring. If it's wrong or over-built, Claude gives a
   **counter-requirement** ("fine, now add X; how many files did that touch?"), not a correction.
7. **Name it**: only now: the principle/pattern name, GoF intent, participants, lineage, and the
   other names it goes by.
8. **Structure**: the learner draws the ASCII class diagram (and a sequence diagram for the core flow);
   Claude tightens it.
9. **Build**: the learner writes it in C++ (Java where the row says so) under `designs/phase-NN/<slug>/`,
   with tests (plain `assert` before 5.2.2; `designs/lib/minitest.hpp` after). `/check` compiles and runs
   it. Claude reviews, pointing at lines, and never rewrites the learner's code.
10. **Adapt**: the row's curveballs, one at a time. The measure is *how local the change is*.
11. **When NOT**: the learner states the costs (indirection, class count, harder debugging) and
    names the simpler alternative (a lambda, an enum + switch over a closed set, a plain function).
    Then build the **comparison table vs the nearest alternative** together; the learner fills it in first.
12. **Language bridge**: C++ idioms (RAII, `std::function`, `std::variant`, templates) vs the Java
    equivalent (interfaces, lambdas, records, `sealed`), because many Indian LLD rounds are run in Java.
13. **Explain-back**: the learner's 2-minute explanation, graded precise / missing / wrong.
14. **Record**: Claude writes the lesson note (`templates/lesson-note.md`) including the learner's own
    **Discovery Path**. The learner adds or updates their entry in `reference/patterns.md` or
    `reference/principles.md`; Claude verifies it.

`WE` sessions invert steps 3–9: the mentor does them aloud first (with one deliberate dead end), the
learner annotates *what was done and why at that moment*, then solves a sibling problem alone.

## 6. The machine-coding protocol (`MC`) and discussion protocol (`LD`)

**MC: 90-minute build + review (the Flipkart / PhonePe / Swiggy / Razorpay format).**

| Minute | Phase | The learner must produce |
|---|---|---|
| 0–10 | Clarify | Written requirement list: must-have vs nice-to-have, assumptions stated, scale/concurrency asked about |
| 10–20 | Model | Entities + relationships (ASCII class diagram), the 3–5 public APIs, the core flow |
| 20–30 | Skeleton | Compiling skeleton: models, interfaces, in-memory repositories, driver `main` |
| 30–75 | Implement | Core flows first, **running by minute 60** (demo via the driver), then the rest |
| 75–85 | Test | Tests for core flows and edge cases (minitest), run green |
| 85–90 | Wrap | Self-review: what's missing, what they'd extend |
| +15–30 | Curveball & defence | The row's curveball: learner states the change plan, then implements it if time allows; code walkthrough |

Interviewer mode during the build: answers clarifications briefly, doesn't rescue, announces time
(`date +%H:%M`) at each phase boundary, and calls out "no running code at minute 60" by name. Then
**"Build over. Mentor hat on."**: strengths → problems (with the requirement change that exposes each)
→ what the mentor's design would change and why (only after the attempt) → rubric score (§9) →
3 practice actions. The code stays the learner's; the review goes in `designs/phase-NN/<slug>/REVIEW.md`.

**LD: 45–60 min whiteboard round, no full code (Amazon / Microsoft / Adobe / Salesforce style).**
Requirements → use cases → class diagram with relationships and multiplicity → key interfaces with
signatures → sequence diagram of the hardest flow → extensibility questions ("add a new vehicle type")
→ concurrency questions ("two users book the last seat") → trade-offs. The learner may write the 20–40
lines that matter most (a state transition, a locking section). Scored on the same rubric, with
*working code* and *testing* re-weighted to *interfaces precision* and *walkthrough* (skill file).

## 7. The concurrency lab protocol (`CL`)

1. **Predict**: before coding, the learner states the invariant ("every item produced is consumed
   exactly once; `size ≤ capacity` at all times") and the hazards they expect.
2. **Build**: C++ (`std::thread`/`jthread`, `mutex`, `condition_variable`, atomics); Java equivalent
   where the row says so.
3. **Break**: stress it with `tools/stress.sh` (hundreds of runs, a timeout to catch deadlocks, some
   runs pinned to one core to change schedules), add `sleep`/`yield` injection at the suspicious point,
   and run the deliberately wrong variant to *watch it fail*. TSan is used automatically if it links;
   on this machine it doesn't, so repetition + invariant assertions + reasoning are the tools.
4. **Explain the interleaving**: for every failure, the learner writes the exact interleaving (thread
   A does x, B does y…) that produced it. No fix is accepted without that.
5. **Fix and argue**: fix, re-stress, and state why the fix is correct (lock covers the invariant;
   predicate re-checked after wake; lock order is global).
6. **Cost**: measure (a `NOCHECK=1` build) the throughput of the coarse vs fine-grained versions when relevant.

## 8. The hint ladder

"I'm stuck" never gets the answer. It gets the **next rung**, and the rung is recorded.

| Rung | Gives | Example (a payment `if/else` chain; adding a payment method edits 6 places) |
|---|---|---|
| **H0** Process nudge | a question about the *process* | "List what changed between the old and new requirement. Which of your classes had to be edited?" |
| **H1** Principle pointer | a principle or heuristic by name, as a question | "Which principle is violated when adding a *type* forces you to edit existing *logic*?" |
| **H2** Observation | a specific fact about this design | "The checkout flow is identical for every method; only 'how to charge' varies." |
| **H3** Structure | the abstraction / relationship to introduce | "One interface for 'charge'; one implementation per method; chosen once, at construction." |
| **H4** Walkthrough | the full design and why (the learner still writes the code) | The Strategy structure + selection via a registry |

**Scoring by the highest rung used:** H0–H1 = independent · H2–H3 = with hints → the kata or design
goes into `progress/resolve-queue.md` for a cold redo · H4 = ♻️ Revisit, redo required. In `MC`/`M`, hints
cost rubric points (the category where the hint was needed). "Just tell me" = one rung up, and the full
answer only if asked again.

## 9. LLD rubric (/100): used for `MC`, `LD`, `M`, `Baseline`

| Category | /pts | What earns full marks |
|---|---:|---|
| Requirements & clarification | 10 | Asks the questions that change the design (scale, concurrency, extensibility axes, money, time); writes must-have vs nice-to-have; states assumptions |
| Entity modelling | 15 | Right nouns as entities vs value objects vs attributes; no god class; responsibilities placed where the data is |
| Class design & relationships | 15 | Correct association/aggregation/composition/dependency, multiplicity, ownership (who creates, who deletes); clean interfaces; encapsulated state |
| Principles & patterns (applied appropriately, *not over-applied*) | 10 | Each pattern justified by a stated axis of change; nothing speculative; SOLID violations absent where they'd hurt |
| Working code | 15 | Compiles, runs the core flows via a driver by minute 60, all must-haves by the end; no crashes on edge inputs |
| Extensibility (curveball) | 10 | The curveball lands as a local change; the learner predicts the touched files correctly |
| Concurrency safety | 5 | Identifies shared mutable state; correct locking/atomicity where needed (or a justified "single-threaded by requirement") |
| Testing | 10 | Tests for the core flows and the nasty edge cases, run green; tests written by the learner |
| Code quality | 5 | Naming, small functions, const-correctness, no leaks/UB, error handling that fits the domain |
| Communication | 5 | Thinks aloud, signposts, explains trade-offs, takes feedback without defensiveness |

Bands: **< 50** No hire · **50–64** Lean no · **65–79** Lean hire · **80–89** Hire · **90+** Strong hire.
Strict: no running code by minute 60 caps *Working code* at 8; untested code scores ≤ 3 in *Testing*; a
pattern with no stated axis of change costs *Principles* points even if it's "correct".

## 10. Retention machinery

- **Concept review queue** (`progress/review-queue.md`): a row reaching 🟨 gets reviews at **+2 / +7 /
  +21 / +60 days**. A review = explain it in 2 min + a curveball + (for patterns) sketch the structure
  from memory in ≤ 3 min. A failure resets to +2 and opens a weak area.
- **Cold redo queue** (`progress/resolve-queue.md`): failed or H2+ katas and case studies scored < 65
  get cold redos at **+3 / +14 / +45 days** (kata: full redo; case study: 30-min model + core-flow
  redo; full rebuild if it scored < 50).
- **Interleaving**: from Phase 3, every `CR` and `M` mixes material from all earlier phases; case
  studies deliberately need patterns from several phases, *unlabeled*.
- **Learner-built references**: `reference/patterns.md` (the learner's catalogue: intent, forces,
  structure, when / when-NOT, used-in), `reference/principles.md`, `reference/concurrency-primitives.md`,
  `reference/case-study-index.md` (every case study: core abstraction, hard part, score, lessons).
  The learner writes them; Claude verifies and corrects.

## 11. The route (all phases, in order)

| Phase | Title | Why here |
|---:|---|---|
| 0 | Kickoff + OOP foundations (C++ & Java) | Every later design is expressed in objects, ownership and relationships. C++ LLD code is only credible with RAII, smart-pointer ownership, value semantics and correct polymorphism. Modelling (nouns → entities, UML) is the first 20 minutes of every round |
| 1 | Design principles | Principles are the *reasons* behind patterns. Taught first so that every pattern later is derived as "the structure that satisfies OCP/DIP here", not recalled |
| 2 | Creational patterns | Object creation is the first place coupling hides (`new ConcreteX` everywhere). Needs DIP/OCP |
| 3 | Structural patterns | Composing objects: wrapping, adapting, trees. Needs interfaces and composition over inheritance |
| 4 | Behavioral + modern patterns | Varying behaviour and communication; the patterns machine coding uses most (Strategy, State, Observer, Command, CoR) plus repository, specification, event bus, rules engine |
| 5 | Clean code, testing & refactoring | The rubric grades tests and code quality; the learner-built test framework is used in every later build. Refactoring is how patterns are *reached* in real code |
| 6 | Concurrency I (coding) | Threads, races, locks, condition variables, atomics, the memory model, liveness, the LeetCode concurrency set. Needs RAII (0.2) and testable design (5.2) |
| 7 | Concurrency II (structures & systems) | Blocking queues, pools, futures, readers–writers, lock-free basics, concurrent maps/LRU, rate limiters, schedulers, and designing LLD systems against double booking and lost updates |
| 8 | Machine-coding method + case studies I | The 90-minute method, then games, state machines and the classic systems. Needs everything above |
| 9 | Case studies II: booking, commerce, finance | Concurrency-critical domains (seats, money, inventory, matching) at the target companies |
| 10 | Case studies III: infra-flavoured | Libraries and frameworks (logger, cache, rate limiter, scheduler, pub-sub, KV store, FS, editor, workflow engine) where extensibility and thread safety are the whole point |
| 11 | Interview mastery | Company-format mocks, LLD discussion rounds, curveball gym, code-walkthrough defence, baseline redo, final gate |

## 12. Tracks

- **🎯 Switch track** (`TRACK-switch.md`): the subset in teaching order needed to pass SDE-2 LLD /
  machine-coding / concurrency rounds at the targets by ~April–May 2027, budget ~150 h. Each row has a
  `Scope`: `full`, or `switch: <what is covered now; what waits>`. Gates in the switch track test only
  the criteria for included sessions; the rest are marked *deferred*.
- **Depth track**: every row of every phase file, in order. After the switch track is done (or when the
  learner switches), `/today` continues with the remaining rows in roadmap order, *including* the
  deferred parts of rows that were covered at switch scope.
- `progress/STATUS.md` holds `**Active track:** switch | depth`. `/today` and `/wrap` pick the next
  session from the active track. Nothing is ever deleted.

## 13. Pedagogical design (why the roadmap is shaped this way)

| Principle | Evidence base | Where it shows up |
|---|---|---|
| **Productive failure** | Kapur: attempting before instruction improves transfer | Every lesson opens with a Hook the learner designs *before* the principle/pattern is named; every MC before the model design |
| **Guided, not pure, discovery** | Mayer (2004): unguided discovery fails | The hint ladder: the smallest nudge that unblocks |
| **Variation theory / contrast** | Marton: discrimination needs contrasting cases | `C` sessions (Strategy vs State, Adapter vs Decorator vs Proxy), "vs nearest alternative" tables, When-NOT in every row |
| **Worked examples → faded scaffolds** | Sweller; expertise-reversal effect | `WE` at the start of each heavy block; scaffolding fades by phase (§14) |
| **Retrieval practice** | Roediger & Karpicke | Explain-back, rebuild-back, `/quiz`, katas from blank files, gates |
| **Spaced repetition** | Ebbinghaus; Cepeda et al. | +2/+7/+21/+60 concept reviews; +3/+14/+45 cold redos |
| **Interleaving** | Rohrer & Taylor | Unlabeled case studies needing patterns from several phases; mixed critiques and mocks |
| **Elaborative interrogation** | Dunlosky et al. | "What breaks when the requirement changes?" and "why not the simpler thing?" at every step |
| **Mastery learning** | Bloom | ✅ = recognition + understanding + construction + adaptation + retention; gates with remediation |
| **Spiral curriculum** | Bruner | Composition over inheritance (0.1.5 → 1.2.3 → every MC), Observer (4.2.1 → event bus 4.3.3 → pub-sub 10.2.1), undo (4.1.6 → 10.3.1), LRU (7.2.3 → 10.1.2), rate limiting (7.3.1 → 10.1.3), seat locking (7.3.5 → 9.1.1) |
| **Critique / error detection** | Bloom's *evaluate* | `CR` sessions each phase: find the flaws in a confident design |
| **Deliberate practice** | Ericsson | Remediation and redo queues target the weakest rubric categories specifically |
| **Metacognitive calibration** | Self-assessment accuracy predicts learning | Predict each gate criterion before testing |
| **Generation effect** | Slamecka & Graf | The learner writes the pattern catalogue, principles, primitives sheet, case-study index, and the test framework itself |
| **Desirable difficulties** | Bjork | Timed builds, mid-build curveballs, cold baselines, forced interleavings in labs |
| **Cognitive apprenticeship** | Collins, Brown & Newman | Model (`WE`) → coach (`L`, `MC` review) → fade (cold `M`) |

## 14. Scaffolding fades by phase

| Phases | During builds | Case studies / mocks |
|---|---|---|
| 0–2 | Hints on request at any rung; Claude offers H0 after ~5 min of silence | (none yet) |
| 3–5 | Hints on request only, after an honest attempt | Critiques coached |
| 6–7 | Max H2 before the time box ends; H3+ only after | Labs: learner explains every interleaving |
| 8 | MC: hints on request, each one costs points; Claude calls out the time | Coached debrief |
| 9–11 | Interview conditions: cold, company-styled, hints cost points everywhere | Strict |

## 15. Rules that never bend

- No pattern or principle is named before the learner has attacked the Hook.
- No mentor model design is shown before the learner's full attempt at an `MC` / `LD`.
- The learner writes the code. Claude compiles, runs, stresses and reviews it.
- No concurrency fix is accepted without the interleaving that broke the old version.
- Due reviews and due redos run before new material, every session.
- "I already know this" → prove it cold (explain + build from blank + one curveball). Pass → the
  session becomes a harder deep dive on the same topic, not a skip.
- Every phase ends with a critique, a review with a concept map, and a gate.

## 16. Phase files

`phase-00.md` … `phase-11.md` in this folder: an intro (why here, scaffolding, reading), the cycles and
their session tables, and a **Gate** checklist at the bottom. `TRACK-switch.md`: the 🎯 switch order.
