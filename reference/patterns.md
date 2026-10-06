# My Pattern Catalogue

**You write each entry after you've derived and built the pattern**, in your own words. Claude verifies
and corrects, never fills in a blank. Leave a row empty until you've built it. The **When NOT** column matters as much as
the others: most interview over-engineering is a pattern used where its force is absent.

Columns: *Force* = the requirement change or pain that calls for it · *Structure* = one line (participants + relationships) ·
*Cost* = what it adds (indirection, classes, runtime) · *When NOT* = the context where the simpler thing wins, and what that is ·
*Confused with* = the nearest pattern and the difference · *Used in* = your builds/case studies (paths).

## Creational (Phase 2)

| Pattern | Force (the pain it removes) | Structure (1 line) | Cost | When NOT (→ instead) | Confused with | Used in |
|---|---|---|---|---|---|---|
| Simple factory / static factory method | | | | | | |
| Factory Method | | | | | | |
| Abstract Factory | | | | | | |
| Registry factory | | | | | | |
| Builder | | | | | | |
| Prototype | | | | | | |
| Singleton | | | | | | |
| Object Pool | | | | | | |
| DI container / composition root | | | | | | |

## Structural (Phase 3)

| Pattern | Force (the pain it removes) | Structure (1 line) | Cost | When NOT (→ instead) | Confused with | Used in |
|---|---|---|---|---|---|---|
| Adapter | | | | | | |
| Facade | | | | | | |
| Decorator | | | | | | |
| Proxy | | | | | | |
| Composite | | | | | | |
| Bridge (+ pimpl) | | | | | | |
| Flyweight | | | | | | |

## Behavioral (Phase 4)

| Pattern | Force (the pain it removes) | Structure (1 line) | Cost | When NOT (→ instead) | Confused with | Used in |
|---|---|---|---|---|---|---|
| Strategy | | | | | | |
| Template Method (+ NVI) | | | | | | |
| State | | | | | | |
| Chain of Responsibility | | | | | | |
| Command | | | | | | |
| Memento | | | | | | |
| Observer | | | | | | |
| Mediator | | | | | | |
| Iterator | | | | | | |
| Visitor (/ std::variant + visit) | | | | | | |
| Interpreter | | | | | | |

## Modern / product-code (Phase 4)

| Pattern | Force (the pain it removes) | Structure (1 line) | Cost | When NOT (→ instead) | Confused with | Used in |
|---|---|---|---|---|---|---|
| Repository & Unit of Work | | | | | | |
| Specification | | | | | | |
| Null Object | | | | | | |
| Event bus / in-process pub-sub | | | | | | |
| Plugin | | | | | | |
| Pipeline / middleware | | | | | | |
| Rules engine | | | | | | |

## Concurrency patterns (Phases 6–7)

| Pattern | Force (the pain it removes) | Structure (1 line) | Cost | When NOT (→ instead) | Confused with | Used in |
|---|---|---|---|---|---|---|
| Monitor (mutex + cv + state) | | | | | | |
| Producer–consumer / bounded queue | | | | | | |
| Thread pool | | | | | | |
| Future / promise | | | | | | |
| Readers–writers / copy-on-write | | | | | | |
| Lock striping / sharding | | | | | | |
| Actor / single-writer | | | | | | |
| Reservation (hold with expiry) | | | | | | |
| Optimistic concurrency (versioning) | | | | | | |
| Idempotency key | | | | | | |

## Traps I've caught myself in

| Date | Trap | Where | What I do now |
|---|---|---|---|
