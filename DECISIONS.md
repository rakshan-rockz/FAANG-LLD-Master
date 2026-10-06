# Programme Decisions Log

Everything decided about this programme and its Claude setup, in one place: what was built, why, what
was rejected, and what's still open. Updated whenever the roadmap, the track or the setup changes.

**State as of 2026-09-25:** setup complete, programme **not started**. Active track: **switch**. Next
session: `0.0.1 Intake`.

---

## 1. How the system works (one picture)

```text
  CLAUDE.md (mentorship contract + operating manual)
        │
        ▼
  plan/PLAN.md (strategy)     plan/roadmap/ (12 phases, 227 sessions, gates)  +  TRACK-switch.md (🎯 83 rows)
        │                       README.md: Design Discovery · MC · LD · CL protocols · hint ladder · mastery · rubric
        └──────────────┬──────────────────┘
                       ▼
  SessionStart hook ──► date · concept rows ✅/🟨 · case studies · mocks · gates · switch-track position ·
                        due reviews / redos / weak areas · STATUS
                       │
                       ▼
        /today ─► due reviews + a redo ─► next ID on the active track ─► right skill:
                   /lesson  /mc  /lld-discuss  /conc  /kata  /critique  /mock  /quiz  /weekly-review  /gate  /intake
                   (+ /hint and /check at any time)
                       │
                       ▼
        /wrap ─► lesson note / REVIEW.md / mock file · tracker · queues · weak areas · STATUS (next on track) ·
                 README dashboard · learner's reference entries verified
```

## 2. Version history

| Ver | Date | What happened | Status |
|---|---|---|---|
| v1 | 2026-09-25 | Repository built, modelled on `FAANG-System-Design-Master` (mastery-gated roadmap, `phase.cycle.n` IDs, gates, generated tracker, role-play skills) and `FAANG-DSA-Master` (discovery protocol, hint ladder H0–H4, row fields, katas, critiques, checked builds, two review queues); two-track convention (switch + depth) | Current |

## 3. Key decisions (with rationale)

| # | Decision | Why | Rejected alternative |
|---|---|---|---|
| D1 | **Design Discovery Protocol**: Hook → learner's first design → a requirement change that hurts → the force → the principle/pattern, named only then | The learner wants to *discover* designs; catalogue learning produces over-engineering in rounds | Teaching patterns by UML + example |
| D2 | **Row fields** Hook · Derive · Covers · Build · Adapt · Anchors · When-NOT · 📖 · File (MC/LD rows reuse them; `Derive` is private for case studies) | Same contract style as the DSA stage rows; `Build` enforces running code; `When-NOT` enforces restraint | Free-form session descriptions |
| D3 | **12 phases** in prerequisite order: OOP → principles → creational → structural → behavioral+modern → clean code & testing → concurrency I → concurrency II → method + case studies I → II → III → interview mastery | Principles before patterns (patterns become derivations); testing before concurrency (fake clocks, invariant tests); all tools before timed builds | Patterns first; concurrency as an appendix |
| D4 | **Session types** Intake · Baseline · L · DD · C · WE · K · MC · CR · CL · M · R · Gate, **plus `LD`** (LLD discussion round, 1.5 h) | Amazon/Microsoft/Adobe/Salesforce run whiteboard LLD rounds without full code; a distinct type keeps them tracked and scored with their own weighting | Folding discussion rounds into `M` only |
| D5 | **/100 LLD rubric** (requirements 10, modelling 15, classes & relationships 15, principles/patterns *not over-applied* 10, working code 15, extensibility 10, concurrency 5, testing 10, quality 5, communication 5); DSA bands; LD weighting swaps code/testing for interface precision/walkthrough | The brief's rubric; strict caps (no running code by minute 60 → Working code ≤ 8) make the method's rules bite | Unscored reviews |
| D6 | **Hint ladder H0–H4** adapted to design (process → principle → observation → structure → walkthrough); rungs recorded; in timed rounds hints cost points | Guided discovery with honest measurement (as DSA) | Free-form help |
| D7 | **Counter-requirements instead of corrections** | The design analogue of DSA counterexamples: a wrong design is disproved by the change that breaks it | Telling the learner the fix |
| D8 | **Learner writes all code; Claude compiles, tests, stresses, reviews** (`tools/run.sh`, `stress.sh`, `/check`) | "Working code" is 15/100 and can't be learned by reading | Claude-written reference solutions |
| D9 | **Learner-built test framework** (`designs/lib/minitest.hpp`, kata 5.2.2) used in every later build; plain `assert` before | Generation effect; no dependency on gtest/JUnit installs; fast in 90-min rounds | Installing gtest/JUnit |
| D10 | **Concurrency labs break code on purpose** and demand the exact interleaving before any fix | Interviews test reasoning about interleavings; TSan is unavailable here anyway | "Add a mutex and move on" |
| D11 | **Checked builds**: `-std=c++20 -Wall -Wextra -Wshadow -pthread` + `_GLIBCXX_DEBUG` always; ASan/UBSan and (with `TSAN=1`, default in `stress.sh`) TSan **only if a probe links** | This machine (GCC 11.5) lacks libasan/libubsan/libtsan: all three probes fail; debug STL still catches bounds errors; the tools upgrade automatically if the libraries are installed | Requiring sanitizers |
| D12 | **`stress.sh` as a concurrency repeat runner** (N runs, timeout → "HANG", every 4th run pinned to one core) instead of DSA's brute-force diff | LLD concurrency bugs are schedule-dependent, not input-dependent; hangs = deadlock/lost wakeup | Porting the brute-force stress script unchanged |
| D13 | **Java supported by `run.sh`** (`javac -Xlint:all`, `java -ea`, `Main`/`Tests` entry classes); JDK 23 is installed | Many Indian LLD rounds are run in Java; Java equivalents in every lesson | C++ only |
| D14 | **Sealed baseline**: Vehicle Rental Service (not one of the 27 case studies), 90-min machine coding, problem and curveball composed at the session and written only into the mock file; redone identically at 11.3.1 | Objective growth measure; not a later case study so the redo stays fair; not written in skills/roadmap so the learner can't pre-read it | Parking Lot as baseline |
| D15 | **Two tracks, one convention across all three repos**: `TRACK-switch.md` (order table with `Scope` + deferred table), `**Active track:**` in STATUS, next session = next track row; depth pass continues with the remaining rows; gates test only included criteria; nothing deleted | Offers by ~June 2027 need a bounded path; the learner still wants the depth later | A separate "lite" roadmap; cutting rows |
| D16 | **Switch track = 83 rows, ≈151 h** (124 h sessions + 2 h reading, +20%); folded rows name exactly what they include; Gates 2–3 fold into Gate 4, Gate 10 into Gate 11; switch-scope gates 1–1.5 h | Fits ~5–6 h/week to ~April 2027; prioritises the MC method, the 10 most-asked systems, the concurrency core, and 5 company-format mocks | Including all 27 case studies (≈ 100 h of MCs alone) |
| D17 | **Retention**: concept reviews +2/+7/+21/+60; cold redos (katas, case studies < 65) +3/+14/+45 | Same machinery as DSA, adapted: a case-study "redo" is a 30-min model + core flow unless it scored < 50 | Weekly revision only |
| D18 | **Learner-built references**: `patterns.md` (with *When NOT* and *Confused with* columns), `principles.md`, `concurrency-primitives.md` (with *classic bug*), `case-study-index.md` (decisions, not code) | Generation effect; the pre-onsite revision set | Claude-written cheat sheets |
| D19 | **Tracker generated** from the phase files + track by `tools/gen_tracker.py` (progress preserved; `--summary` for the hook, `--forecast` for §Scale numbers, `--check` for track coverage) | Roadmap, track and tracker can't drift; the forecast numbers in PLAN are reproducible | Hand-maintained tracker |
| D20 | **Company calibration stated as tendencies** to verify with recruiters and recent write-ups | Formats vary by team/year; overclaiming would mislead preparation | A fixed "company X asks Y" list |
| D21 | **Scope boundaries with the sibling repos**: DSA owns design-a-data-structure internals (LRU/LFU); HLD owns the distributed halves (Kafka, distributed limiters, URL shortener at scale); LLD case studies state the distributed follow-up and stop | Avoid triple-teaching; interleave instead | Re-teaching everything here |
| D22 | **No git init** (per instruction) | — | — |

## 4. Inventory: everything that exists

### 4.1 Skills (slash commands) in `.claude/skills/`

| Skill | Session types | What it does | Writes |
|---|---|---|---|
| `/today` | any | Due reviews + a redo → next ID on the active track → right skill; build rule | via wrap |
| `/intake` | Intake | Profile, MC-language decision, calibration exercises | `progress/profile.md` |
| `/lesson` | L, DD, C, WE | Design Discovery Protocol (`learn` / `deep-dive` / `compare` / `we`) | lesson note |
| `/mc` | MC | Timed 90-min build in interviewer mode, curveball, evaluation discussion, review, /100 | `REVIEW.md` |
| `/lld-discuss` | LD, discussion mocks | Whiteboard LLD round, LD-weighted /100 | `REVIEW.md` / mock file |
| `/conc` | CL | Invariant → build → break → interleaving → fix → argue → measure | lesson note |
| `/kata` | K | From blank, timed, tested/stressed | tracker, redo queue |
| `/check` | any | Compile, run, test, stress, review the learner's code | — |
| `/hint` | any | Exactly one rung | Discovery Path / score |
| `/critique` | CR | Find the planted flaws in a confident design | weak areas |
| `/mock` | M, Baseline | Company formats (machine-coding, code-design, lld-discussion, concurrency, fundamentals, loop), sealed baseline | `mocks/` |
| `/quiz` | any / floor day | Rapid retrieval | tracker, queues |
| `/weekly-review` | R | Cycle/phase review; `monthly` checkpoint | `reviews/` |
| `/gate` | Gate | Calibration → concept map → cold, track-scoped test → pass / remediation | tracker Gates, STATUS |
| `/wrap` | end of every session | Wrap-up protocol; next row on the active track | all progress files |

### 4.2 Files

| Path | Purpose | Who writes it |
|---|---|---|
| `README.md` | Charter + dashboard + how to use | Claude (dashboard at wrap) |
| `CLAUDE.md` | Mentorship contract + operating manual | Claude |
| `DECISIONS.md` | This log | Claude |
| `plan/PLAN.md` | Strategy, company calibration, reading, traps, risks, scale | Claude |
| `plan/roadmap/README.md` | Protocols, hint ladder, mastery bar, rubric, route, pedagogy, tracks | Claude |
| `plan/roadmap/phase-00…11.md` | Every session + gate checklists (switch-deferred criteria marked) | Claude |
| `plan/roadmap/TRACK-switch.md` | 🎯 order with scopes and hours; deferred table with reasons | Claude |
| `progress/*` | STATUS, profile, tracker (generated), review/redo queues, weak areas | Claude (wrap), intake |
| `reference/*` | Pattern catalogue, principles, concurrency primitives, case-study index | **You** (Claude verifies) |
| `designs/`, `designs/lib/minitest.hpp` | Your code; your test framework | **You** |
| `lessons/`, `mocks/`, `reviews/` | Session records | Claude (from the session, with your words) |
| `templates/` | lesson-note, case-study-review, mock-review, weekly-review | — |
| `tools/` | `run.sh`, `stress.sh`, `_flags.sh`, `gen_tracker.py` | — |
| `.claude/settings.json`, `.claude/hooks/session-start.sh` | Permissions (progress/lessons/designs/mocks/reviews edits, tools); status at startup | — |

## 5. Open items / needs from you

| Item | Status |
|---|---|
| Intake answers: SDE-2 confirmation, company priority, known round formats, timeline, availability | Pending: session 0.0.1 |
| **Machine-coding language** (C++ everywhere vs Java for Java-first rounds) | Decide at intake (trade-off laid out in `/intake`) |
| Sanitizers | Optional: `sudo dnf install libasan libubsan libtsan` → the tools enable ASan/UBSan (and TSan with `TSAN=1`) automatically |
| Git repository | Not a git repo (as instructed). Recommend `git init` + a private remote for backup when you're ready |
| Books (HFDP, GoF, Clean Code, Refactoring, CCiA, JCIP) | Only HFDP ch 1 is needed for the switch track |
| Human mock partners | ≥ 4 from Phase 9 onward |
| Weekly split across the DSA / HLD / LLD repos | Suggest at intake; each switch track is sized to coexist |

## 6. Changing things later

Edit the relevant `plan/roadmap/phase-NN.md` (and `TRACK-switch.md`) → run `python3 tools/gen_tracker.py`
and `python3 tools/gen_tracker.py --check` → add a row to §2/§3 here. Asking Claude to "add X to the
roadmap" or "switch to the depth track" follows this procedure (CLAUDE.md).
