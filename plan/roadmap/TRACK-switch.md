# 🎯 Switch Track — LLD, Machine Coding & Concurrency

**Goal:** pass SDE-2 LLD, machine-coding and concurrency rounds at Amazon, Microsoft, Uber, Atlassian, Google, Flipkart, PhonePe, Razorpay, Swiggy, Walmart Global Tech, Adobe and Salesforce by ~April–May 2027 (offers by ~June 2027) · **Budget:** 150 h · **Track total (est.):** 151 h

Sessions 124.00 h + reading 2 h (1 chapter) + 20% overhead = **151.2 h** over 83 sessions. At ~5–6 h/week from 2026-09-28 this ends around late March–April 2027, leaving time for real interviews. `Est h` uses the roadmap durations, adjusted where the scope is reduced (gates at switch scope 1–1.5 h; LD-scope case studies 1.5 h).

**Rules.** `/today` and `/wrap` follow this order while `progress/STATUS.md` says `**Active track:** switch`. A `switch:` scope covers what it names now; everything else in that row, and every row in the deferred table, is taught in the **depth pass**, which runs the remaining roadmap rows in roadmap order after the track ends (or whenever the learner switches track). Gates here test only the criteria of included sessions; the others are marked *(switch: deferred)* in the phase files. Nothing is deleted.

## Order

| # | ID | Type | Topic | Scope | Est h |
|---|---|---|---|---|---|
| 1 | 0.0.1 | Intake | Intake | full | 1.5 |
| 2 | 0.0.2 | Baseline | Vehicle Rental Service | full | 1.5 |
| 3 | 0.0.3 | K | Kata: the toolchain | full | 0.75 |
| 4 | 0.1.1 | L | Encapsulation & Class Invariants | switch: + 0.1.2's interfaces vs abstract classes (C++ idiom, Java `interface` vs `abstract class`) in 15 min; the rest of 0.1.2 waits | 1.25 |
| 5 | 0.1.3 | L | Inheritance & Polymorphism (static and dynamic) | switch: full content; vtable internals (0.1.4) and the composition first look (0.1.5, folded into 1.2.3) wait | 1.25 |
| 6 | 0.2.2 | L | Smart Pointers & Ownership Modelling | switch: + RAII essentials from 0.2.1 (destructor-released resources, `lock_guard`, try-with-resources) and the Rule of Zero; exception-safety guarantees and Rule of 3/5 (0.2.3) wait | 1.25 |
| 7 | 0.2.5 | L | Enums, Value Objects & Strong Types | full | 1.25 |
| 8 | 0.3.1 | L | UML Class Diagrams in ASCII | switch: + the relationships-in-code table from 0.3.2 (value / `unique_ptr` / raw / ID per relationship kind); association classes and bidirectional consistency wait | 1.25 |
| 9 | 0.3.3 | L | From Requirements to Entities (nouns, verbs, responsibilities) | switch: + sequence-diagram basics from 0.3.4 (one core flow per design); state diagrams and use cases wait | 1.25 |
| 10 | 0.3.5 | WE | Worked example: modelling out loud | full | 1.25 |
| 11 | 0.3.8 | Gate | Gate 0 | switch: criteria for the rows above only; vtable, Rule of 5 and critique criteria deferred | 1 |
| 12 | 1.1.2 | L | Single Responsibility Principle | switch: opens with the cohesion/coupling framing of 1.1.1 (10 min); connascence and deep modules wait | 1.25 |
| 13 | 1.1.3 | L | Open/Closed Principle | full | 1.25 |
| 14 | 1.1.4 | L | Liskov Substitution Principle | full | 1.25 |
| 15 | 1.1.5 | L | Interface Segregation Principle | full | 1.25 |
| 16 | 1.1.6 | L | Dependency Inversion Principle | switch: + constructor injection, composition root and the fake-clock test from 1.2.6; injection styles and DI frameworks wait | 1.25 |
| 17 | 1.1.7 | CR | Critique: SOLID violations and SOLID over-application | full | 1 |
| 18 | 1.2.3 | C | Composition over Inheritance (deep) | switch: + 0.1.5's first-look content (class explosion, `Stack extends Vector`); policy-based design in brief | 1.25 |
| 19 | 1.2.8 | WE | Worked example: refactoring a god function out loud | full | 1.25 |
| 20 | 1.2.11 | Gate | Gate 1 | switch: criteria for included rows; DRY, Law of Demeter and kata criteria deferred | 1 |
| 21 | 2.1.2 | L | Factory Method (and static factory methods) | switch: + the pattern-first trap from 2.1.1 (10 min); GoF ch 1 reading waits | 1.25 |
| 22 | 2.1.4 | C | Simple Factory vs Factory Method vs Abstract Factory vs Registry | switch: Abstract Factory (2.1.3) at intent level only; registry with explicit registration in `main` | 1.25 |
| 23 | 2.1.5 | L | Builder | full | 1.25 |
| 24 | 2.2.1 | L | Singleton (and its thread-safe implementations) | switch: + the anti-pattern headline and 'inject a single instance' alternative from 2.2.2; the refactor build waits | 1.25 |
| 25 | 3.1.1 | L | Adapter | full | 1.25 |
| 26 | 3.1.3 | L | Decorator | full | 1.25 |
| 27 | 3.1.5 | C | Adapter vs Decorator vs Proxy vs Facade | switch: Facade (3.1.2) and Proxy (3.1.4) taught here at intent + structure level; their builds wait | 1.25 |
| 28 | 3.2.1 | L | Composite | full | 1.25 |
| 29 | 4.1.1 | L | Strategy | full | 1.25 |
| 30 | 4.1.3 | L | State | full | 1.25 |
| 31 | 4.1.4 | C | Strategy vs State vs Template Method vs enum + switch | switch: Template Method (4.1.2) taught here at intent level with NVI; the importer build waits | 1.25 |
| 32 | 4.1.5 | L | Chain of Responsibility | full | 1.25 |
| 33 | 4.1.6 | L | Command (undo/redo, queues, macros) | switch: + the snapshot-undo contrast from Memento (4.1.7); the Memento build waits | 1.25 |
| 34 | 4.2.1 | L | Observer | switch: + in-process event-bus basics from 4.3.3 (typed subscribe, RAII tokens, error isolation) | 1.25 |
| 35 | 4.3.7 | CR | Critique: pattern soup (and one missing pattern) | full | 1 |
| 36 | 4.3.10 | Gate | Gate 4 | switch: + the switch criteria of Gates 2 and 3 (listed in Gate 4); Visitor, specification and rules-engine criteria deferred | 1.5 |
| 37 | 5.1.2 | L | Error Handling: exceptions vs error codes vs `optional` vs `Result` | full | 1.25 |
| 38 | 5.2.1 | L | Unit Testing Fundamentals | switch: + test doubles and the fake clock (5.2.4) and the testable-design headline (5.2.5); TDD (5.2.3) waits | 1.25 |
| 39 | 5.2.2 | K | Kata: write your own test framework (`minitest.hpp`) | full | 0.75 |
| 40 | 5.2.9 | Gate | Gate 5 | switch: criteria for included rows; smells, refactoring, TDD and critique criteria deferred | 1 |
| 41 | 6.1.2 | L | Data Races & Race Conditions | switch: + thread basics from 6.1.1 (`jthread`, join, capture-by-reference pitfalls) | 1.25 |
| 42 | 6.1.3 | L | Mutexes & Lock Types | full | 1.25 |
| 43 | 6.1.5 | L | Condition Variables | full | 1.25 |
| 44 | 6.1.6 | CL | LeetCode concurrency I: ordering threads | full | 2 |
| 45 | 6.2.1 | L | Atomics | switch: + seq_cst vs release/acquire message passing from 6.2.2; the formal model and JMM depth wait | 1.25 |
| 46 | 6.3.1 | L | Deadlock | switch: + the livelock/starvation headline from 6.3.2 | 1.25 |
| 47 | 6.3.4 | CL | LeetCode concurrency II: the classic puzzles | switch: semaphores, latches and barriers (6.3.3) taught in-lab with the standard types | 2 |
| 48 | 6.3.6 | CR | Critique: a "thread-safe" class that isn't | full | 1 |
| 49 | 6.3.8 | Gate | Gate 6 | switch: criteria for included rows; formal memory model, liveness depth and the primitives kata deferred | 1 |
| 50 | 7.1.1 | L | Producer–Consumer & the Bounded Blocking Queue | full | 1.25 |
| 51 | 7.1.2 | CL | Bounded blocking queue lab (LeetCode 1188 and beyond) | full | 2 |
| 52 | 7.1.5 | CL | Thread-pool lab: submit() returning futures | switch: thread-pool (7.1.3) and futures (7.1.4) essentials taught in-lab; `CompletableFuture` composition depth waits | 2 |
| 53 | 7.2.3 | DD | Concurrent Hash Map & Concurrent LRU | switch: + `shared_mutex` / readers–writers basics from 7.2.1 | 1.5 |
| 54 | 7.3.1 | L | Rate Limiters (token bucket, leaky bucket, windows) | full | 1.25 |
| 55 | 7.3.5 | DD | Concurrency Bugs in LLD Systems (and how to design against them) | full | 1.5 |
| 56 | 7.3.6 | CR | Critique: a "concurrent" seat-booking service | full | 1 |
| 57 | 7.3.9 | Gate | Gate 7 | switch: criteria for included rows; ABA and scheduler criteria deferred | 1 |
| 58 | 8.1.1 | L | The Machine-Coding Round & the Method | switch: + the company-format overview from 11.1.1 | 1.25 |
| 59 | 8.1.2 | WE | Worked example: Tic-Tac-Toe (N×N, k players), out loud and timed | full | 1.25 |
| 60 | 8.1.3 | K | Kata: the machine-coding skeleton | full | 0.75 |
| 61 | 8.3.1 | MC | Vending Machine | full | 3 |
| 62 | 8.4.1 | MC | Parking Lot | full | 3 |
| 63 | 8.4.2 | MC | Elevator System | full | 3 |
| 64 | 8.4.4 | LD | LLD discussion: Amazon Locker | full | 1.5 |
| 65 | 8.4.7 | Gate | Gate 8 | switch: criteria for included rows; evaluator-scoring criterion deferred | 1 |
| 66 | 9.1.1 | MC | BookMyShow (movie ticket booking) | full | 3 |
| 67 | 9.2.1 | MC | Splitwise | full | 3 |
| 68 | 9.2.2 | MC | Payment Wallet (PhonePe/Paytm-style) | switch: + provider adapters, the payment state machine and timeout-with-unknown-outcome from 9.2.3 | 3 |
| 69 | 9.3.1 | MC | Shopping Cart, Checkout & Coupon/Discount Engine (Amazon/Flipkart-style) | switch: the specification pattern (4.3.2) is taught in the review | 3 |
| 70 | 9.3.4 | MC | Ride Sharing (Uber/Ola-style) | switch: LD scope: class design + the matching/assignment core with its concurrency (~40 lines of code); the full build waits | 1.5 |
| 71 | 9.3.6 | M | Mock: payments/commerce machine coding (PhonePe / Razorpay / Swiggy style) | full | 1.5 |
| 72 | 9.3.8 | Gate | Gate 9 | switch: criteria for included rows; order matching and critique criteria deferred | 1 |
| 73 | 10.1.1 | MC | Logger Framework | switch: LD scope: design + the async sink path in code; the full build waits | 1.5 |
| 74 | 10.1.2 | MC | Pluggable Cache (LRU/LFU/TTL) | full | 3 |
| 75 | 10.1.3 | MC | Rate Limiter Library | full | 3 |
| 76 | 10.2.1 | MC | Pub-Sub / In-Memory Message Queue | full | 3 |
| 77 | 11.1.2 | M | Mock: Flipkart-style machine coding (90 + 30) | full | 1.5 |
| 78 | 11.1.3 | M | Mock: Atlassian-style code design (60 min) | full | 1.5 |
| 79 | 11.1.4 | M | Mock: Amazon-style LLD round (45–60 min discussion) | full | 1.5 |
| 80 | 11.1.5 | M | Mock: Uber-style LLD + concurrency | full | 1.5 |
| 81 | 11.2.2 | DD | Code-Walkthrough Defence | full | 1.5 |
| 82 | 11.3.1 | Baseline | Baseline redo | full | 1.5 |
| 83 | 11.3.4 | Gate | Gate 11 (final) | switch: + Gate 10's switch criteria; curveball-gym and evaluator-seat criteria deferred | 1.5 |

**Reading in the track:** 📖 HFDP ch1 (read after 4.1.1). Everything else is in the depth pass.

**Track composition:** Intake 1 · Baseline 2 · K 3 · L 32 · WE 3 · Gate 9 · CR 4 · C 4 · CL 4 · DD 3 · MC 12 · LD 1 · M 5.

## Deferred to the depth pass (not deleted)

| ID | Topic | Why deferred |
|---|---|---|
| 0.1.2 | Abstraction: Interfaces & Abstract Classes | Core covered at switch scope inside 0.1.1; full session in the depth pass |
| 0.1.4 | vtables & the C++ Object Model (+ Java dispatch) | Object-model internals: valuable for Adobe/Microsoft C++ fundamentals questions, rarely decisive in LLD rounds |
| 0.1.5 | Inheritance vs Composition (first look) | Core covered at switch scope inside 1.2.3; full session in the depth pass |
| 0.1.6 | Kata: a polymorphic hierarchy from blank | Kata practice beyond the minimum; the lesson builds cover it |
| 0.1.7 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 0.2.1 | RAII & Exception Safety | Core covered at switch scope inside 0.2.2; full session in the depth pass |
| 0.2.3 | Rule of 0/3/5 & Move Semantics | Rule of 3/5 and move semantics depth: LLD code uses Rule of Zero; covered in 11.1.7 fundamentals mock in the depth pass |
| 0.2.4 | Const-Correctness & Value vs Reference Semantics | Const-correctness is enforced in every `/check` review instead of a dedicated session |
| 0.2.6 | Kata: Money + an owning container | Kata practice beyond the minimum; the lesson builds cover it |
| 0.2.7 | Critique: a "clean" C++ class that isn't | Critique practice; later switch critiques mix Phase 0 flaws in |
| 0.2.8 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 0.3.2 | Relationships in Code: association, aggregation, composition, dependency | Core covered at switch scope inside 0.3.1; full session in the depth pass |
| 0.3.4 | Sequence Diagrams, State Diagrams & Use Cases | Core covered at switch scope inside 0.3.3; full session in the depth pass |
| 0.3.6 | Critique: a confident but flawed class diagram | Critique practice; later switch critiques mix modelling flaws in |
| 0.3.7 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 1.1.1 | Cohesion, Coupling & the Cost of Change | Core covered at switch scope inside 1.1.2; full session in the depth pass |
| 1.1.8 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 1.2.1 | DRY, KISS, YAGNI & the Wrong Abstraction | DRY/KISS/YAGNI are called out by name in every review; the dedicated session waits |
| 1.2.2 | Law of Demeter & Tell, Don't Ask | Law of Demeter is covered in the 1.2.8 worked example and reviews |
| 1.2.4 | Design by Contract & Defensive Programming | Contracts appear in 5.1.2 error handling; the dedicated session waits |
| 1.2.5 | Immutability | Immutability is applied in value objects (0.2.5) and order snapshots (9.3.1) |
| 1.2.6 | Dependency Injection & Inversion of Control | Core covered at switch scope inside 1.1.6; full session in the depth pass |
| 1.2.7 | Programming to Interfaces, Layering & Ports/Adapters | Layout/layering is installed by the 8.1.3 skeleton kata |
| 1.2.9 | Kata: Replace Conditional with Polymorphism | The OCP lesson build already practises replace-conditional-with-polymorphism |
| 1.2.10 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 2.1.1 | What a Design Pattern Is (and the pattern-first trap) | Core covered at switch scope inside 2.1.2; full session in the depth pass |
| 2.1.3 | Abstract Factory | Core covered at switch scope inside 2.1.4; full session in the depth pass |
| 2.1.6 | Prototype | Prototype is rarely needed in machine-coding rounds |
| 2.1.7 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 2.2.2 | Singleton as an Anti-Pattern, and the Alternatives | Core covered at switch scope inside 2.2.1; full session in the depth pass |
| 2.2.3 | Object Pool | Object pools are rare in LLD rounds; pools reappear as thread pools (7.1.5) |
| 2.2.4 | Build a Tiny DI Container | DI containers are not built in interviews; manual DI is what's expected |
| 2.2.5 | Kata: registry factory + builder | Kata practice beyond the minimum |
| 2.2.6 | Critique: over-engineered creational code | Over-engineering critique is covered by 4.3.7 pattern soup |
| 2.2.7 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 2.2.8 | Gate 2 | Core covered at switch scope inside 4.3.10; full session in the depth pass |
| 3.1.2 | Facade | Core covered at switch scope inside 3.1.5; full session in the depth pass |
| 3.1.4 | Proxy | Core covered at switch scope inside 3.1.5; full session in the depth pass |
| 3.1.6 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 3.2.2 | Bridge (+ pimpl) | Bridge is rare in rounds; Strategy covers most notification × channel variation |
| 3.2.3 | Flyweight | Flyweight is rare in LLD rounds |
| 3.2.4 | Worked example: restaurant menu & order builder, out loud | Worked example; case studies in Phase 8 model the same moves |
| 3.2.5 | Kata: decorator chain | Kata practice beyond the minimum |
| 3.2.6 | Critique: structural patterns misused | Critique practice; 4.3.7 covers misuse across patterns |
| 3.2.7 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 3.2.8 | Gate 3 | Core covered at switch scope inside 4.3.10; full session in the depth pass |
| 4.1.2 | Template Method (+ NVI) | Core covered at switch scope inside 4.1.4; full session in the depth pass |
| 4.1.7 | Memento | Core covered at switch scope inside 4.1.6; full session in the depth pass |
| 4.1.8 | Kata: undo/redo buffer | Undo/redo is built in the 4.1.6 lesson |
| 4.1.9 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 4.2.2 | Mediator | Mediator is uncommon in machine coding |
| 4.2.3 | Iterator | Iterator mechanics are familiar from DSA/STL; custom iterators rarely asked |
| 4.2.4 | Visitor (+ `std::variant`/`std::visit`, the expression problem) | Visitor is rarely needed in LLD rounds; `std::variant` alternative waits |
| 4.2.5 | Interpreter | Interpreter is rarely asked; the coupon engine uses specification instead |
| 4.2.6 | Observer vs Mediator vs Event Bus; Visitor vs variant/pattern-matching | Comparison session; the Observer lesson covers event-bus basics |
| 4.2.7 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 4.3.1 | Repository & Unit of Work | Repositories are installed by the 8.1.3 skeleton kata |
| 4.3.2 | Specification & Null Object | Core covered at switch scope inside 9.3.1; full session in the depth pass |
| 4.3.3 | Event Bus / In-Process Pub-Sub | Core covered at switch scope inside 4.2.1; full session in the depth pass |
| 4.3.4 | Plugin & Pipeline (pipes and filters, middleware) | Plugins/pipelines appear inside case studies (cart pricing pipeline) |
| 4.3.5 | Rules Engine | Rules engines are met in context in the coupon engine (9.3.1) |
| 4.3.6 | Worked example: order lifecycle, out loud | Worked example; Vending/Parking MCs practise the same combination |
| 4.3.8 | Kata: safe observer + strategy registry | Kata practice beyond the minimum |
| 4.3.9 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 5.1.1 | Naming & Functions | Naming/functions are graded in every review; the dedicated session waits |
| 5.1.3 | The Code-Smells Catalogue | Smells are named in critiques and MC reviews |
| 5.1.4 | Refactoring Moves (small steps, always green) | Refactoring mechanics: needed for the job, less for 90-min rounds |
| 5.1.5 | Legacy Code: characterisation tests & seams | Legacy-code techniques: job skill, not interview skill |
| 5.1.6 | Kata: Gilded Rose | Refactoring kata; waits with 5.1.4 |
| 5.1.7 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 5.2.3 | Test-Driven Development | TDD is a poor fit for 90-min rounds; test-after with minitest is taught instead |
| 5.2.4 | Test Doubles: dummies, stubs, spies, mocks, fakes | Core covered at switch scope inside 5.2.1; full session in the depth pass |
| 5.2.5 | Testable Design | Core covered at switch scope inside 5.2.1; full session in the depth pass |
| 5.2.6 | Logging & Diagnostics in LLD Code | Logging design is met in the logger case study (10.1.1) |
| 5.2.7 | Critique: tests that test nothing, and code that can't be tested | Test critique; testing is scored in every MC review |
| 5.2.8 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 6.1.1 | Threads | Core covered at switch scope inside 6.1.2; full session in the depth pass |
| 6.1.4 | Race lab: see it fail, explain it, fix it | Race lab; the same failures are reproduced inside 6.1.6 and 7.1.2 |
| 6.1.7 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 6.2.2 | The C++ Memory Model (and the Java Memory Model) | Core covered at switch scope inside 6.2.1; full session in the depth pass |
| 6.2.3 | Memory-ordering & spinlock lab | Spinlocks and SPSC ordering are rarely asked at SDE-2 |
| 6.2.4 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 6.3.2 | Livelock, Starvation, Fairness & Priority Inversion | Core covered at switch scope inside 6.3.1; full session in the depth pass |
| 6.3.3 | Semaphores, Latches & Barriers | Core covered at switch scope inside 6.3.4; full session in the depth pass |
| 6.3.5 | Kata: primitives from mutex + condition variable | Primitives-from-scratch kata; standard types are used in the switch |
| 6.3.7 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 7.1.3 | Thread Pools & Executors | Core covered at switch scope inside 7.1.5; full session in the depth pass |
| 7.1.4 | Futures, Promises & Async | Core covered at switch scope inside 7.1.5; full session in the depth pass |
| 7.1.6 | Work Stealing & Fork/Join | Work stealing is a deep-dive topic, rarely asked |
| 7.1.7 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 7.2.1 | Readers–Writers | Core covered at switch scope inside 7.2.3; full session in the depth pass |
| 7.2.2 | Lock-Free Basics: CAS, the Treiber Stack, ABA, Reclamation | Lock-free/ABA is rarely asked at SDE-2 LLD; say 'mutex first' |
| 7.2.4 | Thread-safe LRU lab | Concurrent LRU lab; the pluggable cache MC (10.1.2) builds the same thing |
| 7.2.5 | Thread-safe Singleton & Lazy Initialisation, compared | Lazy-init comparison; 2.2.1 covers the interview answer |
| 7.2.6 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 7.3.2 | Schedulers & Timers | Scheduler design waits with the scheduler MC (10.1.4) |
| 7.3.3 | Delayed-task scheduler lab | Scheduler lab waits with 7.3.2 |
| 7.3.4 | Actor & Event-Loop Models | Actor/event-loop models: useful framing, rarely required |
| 7.3.7 | Kata: bounded blocking queue from blank | The BBQ is built in 7.1.2; the timed kata is repeated in the depth pass |
| 7.3.8 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 8.2.1 | Snake & Ladder | Games: the Tic-Tac-Toe worked example covers the pattern; Snake & Ladder is a good extra mock |
| 8.2.2 | Chess (move validation) | Chess is long and less common in Indian MC rounds |
| 8.2.3 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 8.3.2 | ATM | ATM overlaps heavily with Vending (State + CoR) |
| 8.3.3 | Critique: a flawed vending machine | Critique practice; MC reviews do this on the learner's own code |
| 8.3.4 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 8.4.3 | Library Management System | Library overlaps with the 0.3.5 worked example |
| 8.4.5 | Mock: 90-min machine coding, Flipkart-style | Mock; the switch has 6 mocks elsewhere |
| 8.4.6 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 9.1.2 | Hotel Booking | Hotel booking overlaps with BookMyShow (holds, intervals) |
| 9.1.3 | Meeting-Room Scheduler / Calendar | Meeting scheduler: good extra practice; interval logic is DSA-familiar |
| 9.1.4 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 9.2.3 | LLD discussion: Payment Gateway Integration & Routing (Razorpay-style) | Core covered at switch scope inside 9.2.2; full session in the depth pass |
| 9.2.4 | Stock Broker Order Matching Engine | Order matching is specialist (fintech/exchanges) |
| 9.2.5 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 9.3.2 | Inventory Management | Inventory reservation concurrency is covered by 7.3.5 and BookMyShow |
| 9.3.3 | Food Delivery (Swiggy/Zomato-style) | Food delivery overlaps with ride sharing (state machine + assignment) |
| 9.3.5 | Critique: a flawed Splitwise and a flawed ride-matcher | Critique practice |
| 9.3.7 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 10.1.4 | Task Scheduler / Cron | Scheduler/cron waits with 7.3.2–7.3.3 |
| 10.1.5 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 10.2.2 | Notification Service | Notification overlaps with logger sinks + rate limiter |
| 10.2.3 | In-Memory Key-Value Store with TTL & Transactions | KV store with transactions: strong extra practice for Atlassian/Uber; first depth-pass priority |
| 10.2.4 | In-Memory File System | In-memory file system: Composite practice; depth pass |
| 10.2.5 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 10.3.1 | Text Editor with Undo/Redo | Text editor: Command practice; depth pass |
| 10.3.2 | Rule / Workflow Engine | Workflow engine: depth pass |
| 10.3.3 | LLD discussion: URL Shortener (the LLD half) | URL shortener LLD: short; good warm-up in the depth pass |
| 10.3.4 | LLD discussion: Stack Overflow | Stack Overflow discussion: depth pass |
| 10.3.5 | LLD discussion: Cricbuzz (live cricket scores) | Cricbuzz discussion: depth pass |
| 10.3.6 | Critique: a flawed pub-sub broker and a flawed KV store | Critique practice |
| 10.3.7 | Mock: Uber / Atlassian-style code design | Mock; Atlassian/Uber formats are mocked in 11.1.3 and 11.1.5 |
| 10.3.8 | Review: Phase review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 10.3.9 | Gate 10 | Core covered at switch scope inside 11.3.4; full session in the depth pass |
| 11.1.1 | Company Formats, Evaluation & Self-Review | Core covered at switch scope inside 8.1.1; full session in the depth pass |
| 11.1.6 | Mock: PhonePe / Razorpay-style payments machine coding | Payments mock; 9.3.6 covers the domain |
| 11.1.7 | Mock: Microsoft / Adobe-style OOD + C++ fundamentals | Fundamentals mock; waits with 0.1.4 and 0.2.3 |
| 11.1.8 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 11.2.1 | Extensibility Curveball Gym | Curveball gym; curveballs are fired in every MC |
| 11.2.3 | LLD Discussion Gym: 3 × 20-minute rounds | LD gym; 8.4.4, 9.3.4, 10.1.1 and 11.1.4 cover discussion rounds |
| 11.2.4 | Critique from the evaluator's seat | Evaluator-seat critique: depth pass |
| 11.2.5 | Review: Cycle review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
| 11.3.2 | Full loop | Full loop: run if time allows before onsites; otherwise depth pass |
| 11.3.3 | Review: Final review | Cycle/phase reviews: in the switch track, retention runs through due spaced reviews and the gates |
