# <ID> — <Principle / Pattern / Primitive>

**Date:** YYYY-MM-DD · **Type:** L | DD | C | WE | CL | K | CR · **Track scope:** full | switch (<what was covered>)
**Prerequisites:** <IDs> · **Build:** `designs/phase-NN/<slug>/` · **Confidence after:** _/5

## In one sentence
<The force it resolves, in the learner's words: "when X varies independently of Y, …">

## The Hook and the first design
<The requirement as posed; the learner's naive design (diagram or code excerpt, by path).>

## What broke when the requirement changed
<The change fired; files/classes that had to change; what was duplicated; what unrelated thing could break.>

## The force → the principle / pattern
<Derivation in steps. Then: name, GoF/literature intent, participants, other names.>

## Structure
```text
(ASCII class diagram; + sequence diagram of the core flow if useful)
```

## C++ (the learner's build)
<Key excerpts by path, with the design decisions: ownership, const, virtual destructor, `std::function` vs interface…>

## Java equivalent
<Key differences: interfaces/lambdas/records/sealed, GC ownership, standard-library examples.>

## Curveballs (Adapt) and how local each change was
| Curveball | Files changed | New classes | Tests changed | Verdict |
|---|---|---|---|---|

## When NOT to use it
<Each item with the counter-requirement or context that makes it over-engineering, and the simpler alternative.>

## Comparison vs the nearest alternative
| Dimension | This | Nearest alternative |
|---|---|---|

## Common mistakes
1. <mistake — why it happens — the requirement/input/interleaving that exposes it>

## Real-world uses
<STL / JDK / frameworks / production systems.>

## Interview follow-ups (12–15, with the reasoning)
1. **Q:** … **A:** …

## My Discovery Path
- **First design I proposed:**
- **Where it broke / where I got stuck:**
- **Hints used (rungs H0–H4 and what each said):**
- **Wrong turns and the counter-requirements that broke them:**
- **The observation that unlocked it:**
- **My 2-minute explanation:** <verbatim-ish; grade: precise / missing / wrong>
- **Five-question reflection:** what problem · why it works · when · when NOT · vs the naive design

## Carry forward
<One no-code thought exercise that seeds the next session's force.>

## Reference entry
- [ ] Learner wrote/updated `reference/<patterns|principles|concurrency-primitives>.md` (verified by mentor)
