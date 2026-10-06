# 🧩 FAANG LLD Master: Low-Level Design, Machine Coding & Concurrency

> **Goal:** given an unfamiliar problem and 90 minutes, clarify what matters, model the domain cleanly,
> build a *running, tested* program whose structure absorbs the interviewer's curveball with a local
> change, keep shared state correct under concurrency, and defend every decision, including why a
> pattern was *not* used.

**Targets:** SDE-2 LLD / machine-coding / concurrency rounds at Amazon, Microsoft, Uber, Atlassian, Google,
Flipkart, PhonePe, Razorpay, Swiggy, Walmart Global Tech, Adobe, Salesforce. Offers by ~June 2027.
**Language:** C++17/20 primary, with Java equivalents throughout (many Indian LLD rounds run in Java).
**Motto:** *Don't memorise patterns. Feel the pain they remove, then invent them.*

---

## 🚀 How to use this repo (with Claude Code)

Open Claude Code in this folder and type **`/today`**. It runs due reviews, then the next session on your
active track.

| When you want to… | Type |
|---|---|
| Do the next thing | `/today` |
| Get unstuck, one hint at a time (never the answer) | `/hint` |
| Compile, run, test and stress your code | `/check designs/…/<slug>` |
| A machine-coding case study / a whiteboard LLD round | `/mc <ID>` · `/lld-discuss <ID>` |
| A concurrency lab / a kata | `/conc <ID>` · `/kata <ID>` |
| A mock interview | `/mock flipkart machine-coding` · `/mock atlassian code-design` · `/mock amazon lld-discussion` |
| A 15-minute floor day | `/quiz 5` |
| End a session (saves everything) | `/wrap` |

**Build and run your code yourself:**

```bash
tools/run.sh designs/phase-08/parking-lot            # build + run the driver (all .cpp except tests)
tools/run.sh --test designs/phase-08/parking-lot     # build + run tests.cpp (all .cpp except main.cpp)
tools/stress.sh designs/phase-07/bbq 300 10          # 300 runs, 10 s timeout each: failures and hangs reported
tools/run.sh designs/phase-00/payroll-java           # Java: javac + java -ea (Main; --test → Tests)
NOCHECK=1 tools/run.sh designs/phase-06/atomics      # plain -O2 build for timing
python3 tools/gen_tracker.py --forecast              # course size by session type and hours
```

C++ builds use `-std=c++20 -Wall -Wextra -Wshadow -pthread` with the bounds-checked STL; ASan/UBSan/TSan are
switched on automatically if their libraries are installed (they aren't on this machine yet).

## How a session works

- **Lessons** start with a problem, not a pattern. You design a first version; a requirement change makes
  it hurt; you find the force and restructure; *then* the principle or pattern is named; you draw it, build
  it (C++ and Java), adapt it to curveballs, and say when it would be over-engineering.
- **Case studies** are timed 90-minute builds in interviewer mode: clarify → model → skeleton → running by
  minute 60 → tests → curveball → evaluation discussion → review → score /100.
- **Concurrency labs** make you write the code, break it with hundreds of stress runs, explain the exact
  interleaving of every failure, then fix and argue it.
- **Critiques** hand you a confident, flawed design; you find the flaws with evidence.
- **Gates** end each phase: a cold test of everything, with remediation if anything fails.

Details: [`plan/roadmap/README.md`](plan/roadmap/README.md) (protocols, hint ladder, mastery bar, rubric)
· strategy and company calibration: [`plan/PLAN.md`](plan/PLAN.md) · the switch track:
[`plan/roadmap/TRACK-switch.md`](plan/roadmap/TRACK-switch.md) · every setup decision:
[`DECISIONS.md`](DECISIONS.md) · how Claude behaves: [`CLAUDE.md`](CLAUDE.md).

**Source of truth:** `progress/STATUS.md` (what's next) and `progress/tracker.md` (generated). The block
below mirrors them.

---

## 📊 Dashboard

**Active track:** 🎯 switch · **Phase:** 0: Kickoff + OOP Foundations · **Next session:** `0.0.1` Intake →
`0.0.2` Baseline (90-min machine coding, sealed)

```text
🎯 Switch track (83 sessions, ~151 h)
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0%   row 1 of 83

Depth track (227 sessions, ~514 h incl. reading)
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0%

Gates 0 / 12 · Case studies scored 0 / 33 · Mocks 0 / 12 · Baseline: not yet
```

**Last scores:** (none yet)
**Up next:** Intake → sealed baseline → OOP foundations (encapsulation, polymorphism, ownership, value
objects, modelling) → SOLID → patterns → testing → concurrency → machine coding.

**Rhythm (switch track, ~5–6 h/week):** 2–3 weekday sessions (lessons, katas, labs, 45–120 min) + one
weekend slot for a 3-hour case study or mock. A gap just means `/today` opens with a short re-entry review.

---

## 🗺️ Curriculum

| # | Phase | Sessions | 🎯 in switch track | Status |
|---:|---|---:|---:|---|
| 0 | Kickoff + OOP foundations (C++ & Java): classes, encapsulation, abstraction, inheritance vs composition, polymorphism & vtables, RAII, smart pointers, Rule of 0/3/5, move semantics, const, value objects, UML (ASCII), modelling | 26 | 11 | 🔓 current |
| 1 | Design principles: cohesion/coupling, SRP, OCP, LSP, ISP, DIP, DRY/KISS/YAGNI, Law of Demeter, composition over inheritance, design by contract, immutability, DI & IoC, layering | 19 | 9 | 🔒 |
| 2 | Creational patterns: factory method, abstract factory, registry, builder, prototype, singleton (thread-safe, and why it's often an anti-pattern), object pool, DI container | 15 | 4 | 🔒 |
| 3 | Structural patterns: adapter, facade, decorator, proxy, composite, bridge (+ pimpl), flyweight | 14 | 4 | 🔒 |
| 4 | Behavioral + modern: strategy, template method, state, chain of responsibility, command, memento, observer, mediator, iterator, visitor, interpreter; repository, specification, null object, event bus, plugin, pipeline, rules engine | 26 | 8 | 🔒 |
| 5 | Clean code, testing & refactoring: naming, error handling (exceptions / `Result` / `optional`), smells, refactoring moves, legacy seams, unit testing, **your own test framework**, TDD, test doubles & fake clocks, testable design, logging | 16 | 4 | 🔒 |
| 6 | Concurrency I: threads, data races, mutexes, condition variables, atomics, the memory model, deadlock, livelock/starvation, semaphores/latches/barriers, the LeetCode concurrency set | 19 | 9 | 🔒 |
| 7 | Concurrency II: bounded blocking queue, thread pools, futures, work stealing, readers–writers, lock-free basics & ABA, concurrent map & LRU, lazy init, rate limiters, schedulers, actors, **double booking / lost updates by design** | 22 | 8 | 🔒 |
| 8 | Machine-coding method + case studies I: Tic-Tac-Toe (worked), Snake & Ladder, Chess, Vending Machine, ATM, Parking Lot, Elevator, Library, Amazon Locker (LD) | 17 | 8 | 🔒 |
| 9 | Case studies II: BookMyShow, Hotel, Meeting scheduler, Splitwise, Payment wallet, Payment gateway (LD), Order matching, Cart & coupon engine, Inventory, Food delivery, Ride sharing | 17 | 7 | 🔒 |
| 10 | Case studies III: Logger, Cache (LRU/LFU/TTL), Rate limiter, Task scheduler/cron, Pub-sub/MQ, Notification service, KV store with TTL & transactions, File system, Text editor, Workflow engine, URL shortener / Stack Overflow / Cricbuzz (LD) | 19 | 4 | 🔒 |
| 11 | Interview mastery: company formats, 6 company-style mocks, curveball gym, code-walkthrough defence, LD gym, evaluator's-seat critique, **baseline redo**, full loop, final gate | 17 | 7 | 🔒 |

---

## 🗂️ Repository map

| Path | Purpose |
|---|---|
| `plan/` | `PLAN.md` (strategy), `roadmap/` (protocols, 12 phase files with every session and gate, `TRACK-switch.md`) |
| `progress/` | `STATUS.md` (next session, active track), `tracker.md` (generated), review & redo queues, weak areas, profile |
| `reference/` | **Yours:** pattern catalogue (with *when NOT*), principles, concurrency primitives, case-study index |
| `designs/` | **Your code:** `phase-NN/<slug>/` builds and case studies (+ `REVIEW.md`), `kata/`, `mocks/`, `lib/minitest.hpp` (your test framework) |
| `lessons/` | Lesson notes, one per concept session, including your own Discovery Path |
| `mocks/` | Mock interview records (the baseline is sealed here) |
| `reviews/` | Cycle, phase and monthly reviews |
| `templates/` | Lesson note, case-study review (with the rubric), mock review, weekly review |
| `tools/` | `run.sh` (C++/Java build + run/test), `stress.sh` (concurrency repeat runner), `gen_tracker.py` |
| `.claude/` | Skills (slash commands), the SessionStart hook, permissions |

**Sibling repos:** `../FAANG-DSA-Master` (algorithms) and `../FAANG-System-Design-Master` (distributed
systems). Same conventions: session IDs, gates, hint ladder, `/today`, and a 🎯 switch track per repo.
