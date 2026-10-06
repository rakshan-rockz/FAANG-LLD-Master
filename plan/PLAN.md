# Mentor's Plan — LLD, Machine Coding & Concurrency

> `CLAUDE.md` = the mentorship contract + how sessions run. This file = the strategy: why the course is
> shaped this way, how the target companies' rounds work, what to read, the traps, the risks, the scale.
> `plan/roadmap/` = every session in order; `TRACK-switch.md` = the 🎯 job-switch order.

**Guiding decisions:** (1) *progress over timeline*: advance by passing gates; (2) *pain before
pattern*: every principle and pattern is derived from a requirement change that hurts; (3) *running,
tested code in almost every session*; (4) *two tracks, nothing deleted*: a ~150 h switch track for
offers by ~June 2027, then the depth pass.

---

## 1. The problem this course solves

Most LLD preparation fails in one of four ways, and interviewers see all four every week:

| Failure mode | What it looks like in a round | What this course does instead |
|---|---|---|
| **Catalogue learning** | Names 6 patterns in minute 3; applies Singleton, Factory, Observer to a problem that needs none; can't say when *not* to | Pain before pattern: every pattern is derived after a requirement change makes the naive design hurt; every lesson ends with When-NOT and a simpler alternative; critiques full of over-engineering |
| **Diagram without code** | A beautiful class diagram at minute 30, nothing compiling at minute 75 | The 90-minute method with artefacts per phase; "running by minute 60" as a hard rule; builds in almost every session from Phase 0 |
| **Code without design** | A 600-line `main` or a `Manager` god class that works for the demo and collapses at the first curveball | Modelling (Phase 0), principles (Phase 1), and a curveball in every build, scored on *how local the change is* |
| **Concurrency by hope** | "I'll add `synchronized`" / a global mutex; double booking and double spend on follow-up | Two phases of concurrency built from the hazard up, labs that *break* code and demand the interleaving, and a dedicated session on domain-level races (7.3.5) before the booking/money case studies |

## 2. Why each phase is where it is

| Phase | Why here (and what would go wrong elsewhere) |
|---|---|
| 0 OOP foundations (C++ & Java) | Everything is expressed in objects and ownership. Without RAII, smart-pointer ownership, value objects and correct polymorphism, C++ LLD code leaks, slices and uses `double` for money: all visible to an evaluator in seconds. Modelling (nouns → entities, UML) is the first 20 minutes of every round |
| 1 Principles | Principles are the *reasons*. Taught before patterns so that each pattern arrives as "the structure that keeps this change local", which is how you justify it in an interview. Patterns first produce catalogue learners |
| 2 Creational | Creation is the first place coupling hides; needs DIP/OCP. Singleton is taught with its anti-pattern critique straight away |
| 3 Structural | Needs interfaces and composition over inheritance. Four patterns share one shape, so the compare session (3.1.5) is the key skill |
| 4 Behavioral + modern | The patterns machine coding uses most (Strategy, State, Observer, Command, CoR) plus what product code uses (repository, specification, event bus, rules engine). Needs Phases 1–3 |
| 5 Clean code & testing | The rubric grades tests and quality; evaluators read the code. The learner writes the test framework used in every later build. Testable design (injected clocks) is a prerequisite for testing concurrent code |
| 6 Concurrency I | Primitives built from hazards: race → mutex; busy-wait → condition variable; deadlock produced on purpose → lock ordering. Needs RAII and testable design |
| 7 Concurrency II | The components interviews name (BBQ, pool, futures, RW lock, concurrent LRU, rate limiter, scheduler) and domain-level races (double booking, lost update, double spend) with pessimistic/optimistic/hold strategies |
| 8 Method + case studies I | Only now is everything available to build a system under a clock. Method first (8.1), then games, state machines and the classic systems |
| 9 Case studies II | The target companies' domains (booking, money, commerce, mobility) where concurrency and money correctness decide the score |
| 10 Case studies III | Libraries (logger, cache, limiter, scheduler, pub-sub, KV store, FS, editor, workflow engine) where extensibility and thread safety *are* the problem; plus discussion-style rounds |
| 11 Interview mastery | Company formats, evaluation-discussion defence, curveball gym, LLD discussion gym, sealed baseline redo, final gate |

**Spirals** (the same idea at increasing depth): composition over inheritance (0.1.5 → 1.2.3 → every
MC) · Observer → event bus → pub-sub broker (4.2.1 → 4.3.3 → 10.2.1) · Command undo → text editor
(4.1.6 → 10.3.1) · LRU → concurrent LRU → pluggable cache (DSA → 7.2.3 → 10.1.2) · token bucket →
limiter library (7.3.1 → 10.1.3) · scheduler → cron (7.3.2 → 10.1.4) · seat holds → BookMyShow
(7.3.5 → 9.1.1) · Money value object → wallet ledger (0.2.5 → 9.2.2) · specification → coupon engine
(4.3.2 → 9.3.1).

**Relation to the sibling repos.** `FAANG-DSA-Master` Stage 24 covers design-a-data-structure rounds
(LRU/LFU, randomised set) and a light "design-style coding round" lesson; this course owns OOD, machine
coding and concurrency, and reuses those structures inside case studies without re-teaching them.
`FAANG-System-Design-Master` owns the distributed half (URL shortener at scale, Kafka, distributed rate
limiting, notification platforms). Case studies here state the distributed follow-up and stop.

## 3. What is added beyond a standard LLD list (and why)

| Addition | Where | Why |
|---|---|---|
| C++ ownership & value semantics as design tools | 0.2 | Ownership arrows decide member types; evaluators judge C++ code on this first |
| Relationships in code (IDs vs pointers) | 0.3.2 | Machine-coding designs with repositories hold IDs; mixing the two is a common bug source |
| Requirements → entities with GRASP/CRC | 0.3.3 | The 10-minute modelling phase is trainable, not a talent |
| Design by contract, immutability, layering/ports-adapters | 1.2 | The reasons behind validation placement, snapshots and folder layout in MCs |
| Object pool, DI container built by hand | 2.2 | Demystify Spring/Guice; justify manual DI in rounds |
| Repository, specification, null object, event bus, plugin, pipeline, rules engine | 4.3 | Used constantly in product code and in coupon/offer/notification rounds; missing from GoF |
| A learner-written test framework, fakes and fake clocks | 5.2 | Makes testing in 90 minutes fast; makes time-based rules testable |
| Memory model, lock-free basics, work stealing, actors | 6.2, 7.1–7.3 | Depth-track answers to Uber/Microsoft/Adobe follow-ups; say "mutex first" with authority |
| Domain concurrency (double booking, write skew, double spend, idempotency) | 7.3.5 | The follow-up in every booking/payment round |
| Payment gateway routing, order matching, workflow engine, Cricbuzz | 9–10 | Fintech and Indian-company favourites |
| Evaluation-discussion defence, curveball gym, evaluator's-seat critique | 11.2 | The 30 minutes after the build often decide the outcome |

## 4. Scale

Counted by `python3 tools/gen_tracker.py --forecast` from the phase files (durations: L 1.25 h, DD 1.5,
C 1.25, WE 1.25, K 0.75, CR 1, CL 2, MC 3 incl. review, **LD 1.5** (a type added for discussion rounds),
M 1.5, R 1, Gate 3, Intake/Baseline 1.5; reading ≈ 2 h per scheduled chapter; +20% overhead).

| Type | Sessions | Hours |
|---|---:|---:|
| Intake | 1 | 1.5 |
| Baseline (0.0.2 + redo 11.3.1) | 2 | 3.0 |
| L learn | 78 | 97.5 |
| DD deep dive | 13 | 19.5 |
| C compare | 7 | 8.75 |
| WE worked example | 5 | 6.25 |
| K kata | 13 | 9.75 |
| CR critique | 13 | 13.0 |
| CL concurrency lab | 8 | 16.0 |
| MC machine-coding case study | 27 | 81.0 |
| LD LLD discussion | 6 | 9.0 |
| M mock | 10 | 15.0 |
| R review | 32 | 32.0 |
| Gate | 12 | 36.0 |
| **All sessions** | **227** | **348.25** |
| Reading: 40 chapters (HFDP 13, GoF 4, Clean Code 6, Refactoring 4, CCiA 7, JCIP 6) | | 80.0 |
| **Full course (depth track): (348.25 + 80) × 1.2** | | **≈ 514 h** |
| **🎯 Switch track: 83 sessions, (124.0 + 2 h reading) × 1.2** | | **≈ 151 h** |

Switch-track composition: Intake 1 · Baseline 2 · L 32 · DD 3 · C 4 · WE 3 · K 3 · CR 4 · CL 4 · MC 12
(two at LD scope) · LD 1 · M 5 · Gate 9. At ~5–6 h/week from late September 2026 it ends around late
March–April 2027, in time for interviews in April–May and offers by ~June 2027. The full course at
~6 h/week is ~20 months; that's expected, and the depth pass runs after the switch.

## 5. Company calibration (tendencies reported by candidates; refined at intake and before each loop)

Formats change by team and year. Confirm with the recruiter and recent interview write-ups; these are
patterns to practise against, not guarantees.

| Company | LLD format (typical) | What wins | Practise with |
|---|---|---|---|
| **Flipkart** | Machine coding from a problem document, ~90–120 min, runnable in-memory program with a driver; then an evaluation discussion; separate design rounds at higher levels | Working code covering must-haves, modularity, extensibility on "add X", clean naming, handling edge cases; Java common but language usually free | `MC` in Phases 8–10, 11.1.2 |
| **PhonePe** | Machine coding (~90–120 min) + LLD/design discussion; payments-flavoured problems | Correctness (money, idempotency), concurrency on shared state, extensibility, tests | 9.2, 11.1.6 |
| **Razorpay** | Machine coding and LLD rounds; payments/merchant domains | State machines, idempotency, provider adapters, clean interfaces | 9.2.2–9.2.3, 11.1.6 |
| **Swiggy** | Machine coding (~90 min) + LLD; delivery/commerce domains | Working code, extensibility, assignment/state logic | 9.3, 9.3.6 |
| **Walmart Global Tech** | LLD round and/or machine coding in many teams; Java + multithreading questions common | OOD + Java concurrency fundamentals | Phase 6–7 (Java versions), 11.1.5 |
| **Uber** | LLD / machine coding with an extensible class design; concurrency follow-ups; sometimes concurrency coding | Clean abstractions, correct concurrency reasoning, extensions | 11.1.5, Phase 7 |
| **Atlassian** | "Code design" round (~60 min): working, tested code; requirements extended mid-round; readability/extensibility explicitly graded | Small steps, tests, designs that absorb extensions | 11.1.3, 10.1.3, 10.2.3 |
| **Amazon** | An OOD/LLD round in the SDE-2 loop: classes, interfaces, patterns, extensibility, some code; Leadership Principles woven in | Clear modelling, justified patterns, trade-offs, ownership stories | `LD` sessions, 11.1.4 |
| **Microsoft** | Design/OOD rounds with code in many loops; fundamentals and correctness | Correct, tested code; clean OOP | 11.1.7, Phase 0 |
| **Adobe / Salesforce** | LLD + OOP + language fundamentals (C++ virtuals/smart pointers; Java collections/concurrency) | Fundamentals + clean design | 0.1–0.2, 11.1.7 |
| **Google** | Rarely a separate LLD round at SDE-2/L4; coding rounds reward clean class design; system design at L5 | Clean code in coding rounds | (DSA repo) + Phase 5 |

## 6. Reading list (assigned *after* the session, never before: attempt first)

| Book | Role | Scheduled chapters |
|---|---|---|
| *Head First Design Patterns*, 2nd ed. (Freeman & Robson) (HFDP) | Intuition and motivation for the GoF patterns | 1 Strategy (4.1.1) · 2 Observer (4.2.1) · 3 Decorator (3.1.3) · 4 Factory (2.1.2) · 5 Singleton (2.2.1) · 6 Command (4.1.6) · 7 Adapter & Facade (3.1.1) · 8 Template Method (4.1.2) · 9 Iterator & Composite (3.2.1) · 10 State (4.1.3) · 11 Proxy (3.1.4) · 12 Compound patterns (4.3.6) · 13 Real world (4.3.9) |
| *Design Patterns* (Gamma, Helm, Johnson, Vlissides) (GoF) | The reference: intent, forces, consequences | 1 Introduction (2.1.1) · 3 Creational (2.2.7) · 4 Structural (3.2.7) · 5 Behavioral (4.3.9) |
| *Clean Code* (Martin) (CC) | Code-level quality evaluators notice | 2 Names · 3 Functions (5.1.1) · 7 Error handling (5.1.2) · 9 Unit tests (5.2.1) · 10 Classes (5.1.4) · 17 Smells (5.1.3) |
| *Refactoring*, 2nd ed. (Fowler) | How designs are reached in real code | 1 First example · 2 Principles (5.1.4) · 3 Bad smells (5.1.3) · 4 Building tests (5.2.1) |
| *C++ Concurrency in Action*, 2nd ed. (Williams) (CCiA) | C++ threads, locks, atomics, memory model, concurrent structures, pools | 2 (6.1.1) · 3 (6.1.3) · 4 (6.1.5) · 5 (6.2.2) · 6 (7.2.3) · 7 (7.2.2) · 9 (7.1.3) |
| *Java Concurrency in Practice* (Goetz et al.) (JCIP) | The Java side; the best text on thread-safety reasoning | 2 (6.1.2) · 3 (6.2.1) · 5 (6.3.3) · 6 (7.1.3) · 10 (6.3.1) · 16 (6.2.2) |

Optional companions: *Effective Modern C++* (Meyers) items 18–25; *Effective Java* (Bloch) items 1–2, 17–20,
78–84; *A Philosophy of Software Design* (Ousterhout); *Clean Architecture* (Martin) ch 7–11;
*Working Effectively with Legacy Code* (Feathers); *Refactoring to Patterns* (Kerievsky). Interview-prep
LLD write-ups and videos: only **after** your own attempt at that case study is scored, to compare.

**Switch track reading:** HFDP ch 1 only (after 4.1.1). The rest is scheduled in the depth pass.

## 7. Retention and interview realism

- Every session opens with due reviews and redos (≤ 10–15 min) before new material.
- Explain-back (2 min, own words, graded) ends every lesson and is saved in the note.
- Cold redos for weak katas and case studies: +3 / +14 / +45 days.
- Interleaving: case studies never announce their patterns; critiques mix phases.
- Timed rounds with per-phase clock times; "running by minute 60".
- Talk aloud (voice if possible) in `LD` and mocks; score communication.
- **Human mocks**: ≥ 4 with peers or a mock platform from Phase 9 on; their feedback goes into weak areas.
  AI-only feedback has blind spots (no social pressure; tends to lead).

## 8. Traps I'll call out by name

- **Pattern-first design**: choosing patterns before the requirements show a force.
- **God class**: a `Manager`/`System`/`Service` that owns every rule.
- **Premature abstraction**: interfaces with one implementation and no test seam; factories for one type.
- **Inheritance for reuse**: subclassing to share code rather than to model a true subtype.
- **Ignoring concurrency**: "single-threaded" never stated, shared state never discussed.
- **Lock-and-pray / I/O under a lock**: one global mutex; payment calls while holding a lock.
- **No running code by minute 60.**
- **Untested code**: a demo is not a test.
- **Primitive obsession**: `double` for money, `int` for every ID, strings for states.
- **Anemic domain model**: data classes + one procedural service with all the logic.
- **Gold-plating the CLI**: 20 minutes on input parsing, 0 on the core.
- **Silent assumptions**: deciding a requirement without saying it aloud.
- **Rereading instead of rebuilding**: reading your old design feels productive and isn't.

## 9. Risks

| Risk | Mitigation |
|---|---|
| The switch track feels thin in places | Every folded row says exactly what it covers; the deferred list is explicit; the depth pass is scheduled, not optional |
| 3-hour MC sessions are hard to fit on weekdays | MCs on weekends; weekday lessons/katas; an MC can be split build (90 min) / review (next sitting) |
| C++ is slower to write under a clock than Java | Decide the MC language at intake per company; the skeleton kata (8.1.3) in both; two Phase 8 MCs in Java if needed |
| No ThreadSanitizer/ASan on this machine | Stress runs + invariant assertions + interleaving arguments; `sudo dnf install libtsan libasan libubsan` enables them automatically in the tools |
| Over-coaching by the AI mentor | Private `Derive` fields, hint ladder with recorded rungs, interviewer mode, human mocks |
| Momentum loss | Floor days (`/quiz 5`), visible track progress in the hook, re-entry reviews after gaps |
| Burnout from three parallel prep repos (DSA, HLD, LLD) | Interleave by week (e.g. 2 DSA : 1 LLD : 1 HLD days); the switch-track budgets are sized to coexist |
