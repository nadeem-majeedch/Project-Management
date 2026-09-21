# Lecture 09 — Scope & Work Breakdown Structure

> **Package for:** L09 · Week 5 · Unit U3 · CLO2 · Bloom: Apply
> **Case anchors:** CS-12 (three-level WBS), CS-13 (scope-creep spotting)
> Companion: [`L09` skeleton](../../../docs/lectures/L09-09-scope-wbs.md) · [CS-12](../../../docs/cases/CS-12.md) · [CS-13](../../../docs/cases/CS-13.md)

## Learning objectives

1. Build a deliverable-oriented WBS to work-package level that passes the 100% rule.
2. Write WBS dictionary entries (owner, estimate, acceptance) for work packages.
3. Distinguish scope creep from gold plating from legitimate change.
4. Decompose a data-project WBS along pipeline stages rather than features.

## Required prior knowledge

- L06 charter (objectives the WBS must serve).
- L09 marks the Planning-unit turn: from here the course is artifact-heavy.

## Teaching notes

Two doctrine sentences carry the hour: **"if it's not in the WBS, it's not in
the project"** and **"the WBS is deliverable-oriented, not task-oriented."**
Students persistently build *to-do lists* ("install server", "write docs") —
the 100% rule plus the deliverable test fixes this in one iteration when you
show the failure concretely: a to-do WBS cannot be *handed over*, because it
has no deliverables to hand.

Second teaching spine: the 100% rule as the WBS's only hard law — every level
sums (comprehensively, with no overlaps) to the level above. Run one
intentionally broken WBS through the rule; let students find the missing and
the double-counted work.

DS adaptation matters here: data projects decompose along **pipeline stages
(ingestion → storage → features → model → serving → monitoring)** with a
horizontal "data operations" branch — feature-oriented decomposition produces
fragile data WBS's. Show both shapes side by side in the worked example.

## Definitions & concepts

- **Scope statement** — in/out lists, deliverables, acceptance criteria,
  constraints, assumptions.
- **WBS** — hierarchical, deliverable-oriented decomposition; the *lowest
  level = work packages* (owner, estimate, acceptance — controllable units).
- **100% rule** — each level captures 100% of the parent's scope: nothing
  missing, nothing double-counted.
- **WBS dictionary** — per-package definition: description, owner, estimate,
  acceptance criteria, dependencies.
- **Scope creep** — uncontrolled, unapproved growth. **Gold plating** —
  self-initiated extras nobody asked for. Both differ from **legitimate
  change** (approved through control, L20).

## Practical examples

**CS (CampusHub registration rewrite):** level-1 deliverables: *Registration
engine, Student portal UI, Advisor tools, Migration & cutover, Training &
documentation*. Note "Migration & cutover" — students forget non-code
deliverables; the 100% rule catches them.

**DS (TelcoCare churn):** level-1: *Data ingestion & validation, Feature
store, Model training & evaluation, Scoring service, Monitoring & drift
alerts, Analysis documentation*. The horizontal branch: *Data governance &
quality gates* touching all stages — a cross-cutting WBS element.

## Worked example

**Full WBS with arithmetic checks (board, 15 min):**

```
1.0 Registration Engine (deliverable)
  1.1 Registration services
      1.1.1 Enrollment API            [pkg: owner Sana, est 80h]
      1.1.2 Prereq-check service      [pkg: owner Sana, est 50h]
  1.2 Rules engine
      1.2.1 Policy rule format        [pkg: owner Bilal, est 30h]
      1.2.2 Rule evaluation service   [pkg: owner Bilal, est 70h]
  1.3 Engine integration tests        [pkg: owner Amina, est 40h]
```

Checks run live: (a) **100% rule** — do 1.1+1.2+1.3 fully define 1.0? Ask
what's missing; the answer that always emerges: *deployment* — add 1.4
"Engine deployment & config" (40 h). (b) **No overlaps** — 1.1.2 (prereq
checks) vs 1.2 (rules): is a prereq a policy rule? Deciding *either* move the
service under 1.2 *or* document the boundary in both dictionary entries;
unresolved overlap = double-counted estimate. (c) **Dictionary entry demo**
for 1.1.1: description, owner, 80 h estimate + basis, acceptance ("returns
enrollment decision ≤ 300 ms p95 for 5k concurrent users"), dependency on
rule format (1.2.1).

Totals: 80+50+30+70+40+40 = **310 h** — the WBS just produced the first
bottom-up estimate; point forward to L10 (estimation) and L13 (costing).

**DS variant (same mechanics, one branch shown):**

```
2.0 Feature Store (deliverable)
  2.1 Historical features batch      [pkg: owner Hira, est 60h]
  2.2 Streaming features             [pkg: owner Usman, est 90h]
  2.3 Feature validation suite       [pkg: owner Hira, est 35h]
      → 2.3 belongs to governance cross-branch too: boundary note in dictionary
```

## Common misconceptions

| Misconception | Correction |
|---|---|
| "The WBS is a task list / schedule." | It is deliverable decomposition; *schedule* comes later (L11–L12) by sequencing packages. |
| "Project management work isn't in the WBS." | PM effort is a work package (usually one per phase) — otherwise the 100% rule is violated. |
| "Fixed-level WBS (always 3 levels)." | Depth follows control need; 2–5 levels is typical, rule-of-thumb package size 8–80 h. |
| "Agile teams don't need WBS." | They decompose differently (epics → stories) but still owe deliverable scope definition — the release-plan level (L21/L24). |
| "Scope creep is the team's fault." | Usually a *missing control* fault — no baseline, no change log (CS-13 makes this visible). |

## Classroom activities

1. **CS-12 WBS build (35 min):** teams produce a 3-level WBS + two dictionary
   entries for the student portal; then a cross-team **100% rule audit swap** —
   each team finds another team's missing deliverable.
2. **CS-13 creep spotting (20 min):** 14-entry change log; classify each
   creep / gold plating / legitimate; agree dispositions.
3. **Boundary disputes (10 min):** deliberately overlapping packages on the
   board; teams write the dictionary boundary note that resolves each.

## Discussion questions

1. Where do *project management* activities sit in your CS-12 WBS, and what happens to the estimate if they're omitted?
2. Which is more dangerous for a data project: creep in features or creep in data (columns joined late)? What control fits each?
3. Your 100% audit found a missing deliverable in a peer WBS. Is that a WBS failure or a scope-statement failure? Who fixes what?

## Practical exercise

**In class:** CS-12 deliverable. **Take home (feeds A2):** complete the WBS
for your *own* assignment-1 project (20–30 packages, 100% rule checked by a
peer from another team), plus dictionary entries for two packages. This is the
first artifact of Assignment 1 — release its brief today.

## Formative assessment (exit ticket)

1. State the 100% rule.
2. Give one difference between creep and gold plating.
3. What three fields must a work-package dictionary entry contain at minimum?

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Planning domain; Delivery domain
  (acceptance criteria).
- PMI. (2017). *PMBOK Guide* (6th ed.) — "Create WBS" process section (the
  classic treatment; dictionary anatomy).
- [Templates](../../../docs/resources/templates.md): WBS + dictionary
  skeleton · [Assignment 1 brief](../../../docs/assignments/a1-scope-schedule.md).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the to-do WBS that couldn't be handed over | broken WBS slide |
| 0:10–0:30 | Scope statement; deliverable orientation; 100% rule | doctrine slides |
| 0:30–0:50 | Worked example: WBS + checks + dictionary | board tree |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-12 build + cross-team audit | CS-12 brief |
| 1:35–1:55 | CS-13 creep classification | change log handout |
| 1:55–2:00 | Exit ticket + A2 release | slips |

## Instructor preparation notes

- Draw the broken to-do WBS in advance; plant one missing *deployment* branch
  and one overlap (1.1.2 vs 1.2 style) for the audit reveal.
- Prepare the 14-entry change log for CS-13 with a defensible answer key
  (record in [answer keys](../../answer-keys/README.md) area).
- Verify every team has chosen seed + track before they leave (L08 follow-up);
  A2 project choice locks today.

## Linked resources

- Lecture skeleton: [`docs/lectures/L09`](../../../docs/lectures/L09-09-scope-wbs.md)
- Cases: [CS-12](../../../docs/cases/CS-12.md) · [CS-13](../../../docs/cases/CS-13.md)
- Assignment: [A2 scope & schedule brief](../../../docs/assignments/a1-scope-schedule.md)
- Forward: [estimation L10](../../../docs/lectures/L10-10-estimation.md) —
  the 310 h total becomes the estimation input.
