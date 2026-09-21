# Lab 14 Answer Key — Agile Product Backlog & Sprint Planning

## Reference capacity chain (checker-verified against `data/campus-mend-sprint-answers.csv`)

| Step | Computation | Result |
|---|---|---|
| Gross | 4 × 2 wk × 10 h | 80 h |
| Absence | exam week | −6 h |
| After absence | | 74 h |
| Focus ×0.7 | 74 × 0.7 | 51.8 h |
| Ceremonies | 2 + 1 + 1 + 10×10min | −5.7 h |
| **Build capacity** | | **46.1 h** |
| Rate | team's measured | ≈ 1.4 h/pt |
| **Point capacity** | floor(46.1 / 1.4) | **32 pts** |

## Model ordering + selection (checker-verified: committed ≤ capacity)

**Sprint goal (model):** "Restore confidence in the two student-critical
flows — registration under peak load and result publishing inside 48 h —
with rehearsed, observed evidence."

| Order | Item | Pts | Value | Goal-fit | In sprint? |
|---|---|---|---|---|---|
| 1 | B1 deadlock fix + load test | 13 | 10 | 5 | **IN** |
| 2 | B6 result-publishing rehearsal | 13 | 9 | 5 | **IN** |
| 3 | B9 rollback drill | 5 | 8 | 4 | **IN** (31 pts) |
| 4 | B3 caching layer | 8 | 9 | 3 | stretch — **not committed** |

Committed = 31 pts ≤ 32 ✓. Rationale: B1+B6 are the registrar's named
priorities; B9 (rollback drill) is the SLA safety net B6's rehearsal needs;
B3 is the highest-value remaining item but its 8 pts would breach capacity —
declaring it stretch, not committed, is the honest cut. Alternative defensible
cuts: B5 over B9 (if the student argues retry-handling is a B6 dependency —
accept if the dependency claim is explicit and consistent with their
ordering).

## DoD (model; ≥ 5 testable, QA-owned ≥ 2, SLA-evidence item included)

1. Peak-replay load test executed; p95 ≤ 2.0 s (QA-owned).
2. Registration peak replay shows zero deadlocks across 3 runs (QA-owned).
3. Result-publishing rehearsal timed with ≥ 2 h margin, log attached
   (SLA-evidence item).
4. Rollback drill completed ≤ 30 min with evidence.
5. All code peer-reviewed (2 approvers) and CI green incl. data-contract
   tests.
6. Ticket log reconciles claimed vs verified completion (Lab 5/13 audit
   rule).

## Sprint risks (model top 3)

| Risk | Trigger | Fallback |
|---|---|---|
| B6 rehearsal exposes pipeline defect | first rehearsal misses margin | de-scope rehearsal variance runs; fixed scope re-run by sprint end |
| B1 fix regresses under mixed load | CI load step fails post-fix | revert + feature-flag the fix path; escalate to next sprint with sponsor note |
| QA absence in exam week | QA unavailable for DoD items 1–2 | pre-book contract tester day 1; swap DoD ownership to PM-verified checklist |

## Common wrong answers

| Error | Correction |
|---|---|
| Capacity = 80 h × 1.4 h/pt inverted | points capacity = build h ÷ h/pt; show the chain |
| Selecting 40+ pts "because velocity will improve" | forecast with the team's own measured rate; improvement is measured, not hoped |
| Goal = item list | outcome sentence first; items serve it |
| Stretch marked committed | stretch exists because capacity is a ceiling, not a target |
| DoD = "done means done" | testable, verifiable items; QA owns ≥ 2 |

## Reflection guidance

1. 32 pts capacity vs 26 pts of registrar priorities: tell her the two fit
   with 5 pts of safety net (B9), the next item (B3) is stretch, and the
   goal sentence carries that as "the two student-critical flows get
   rehearsed evidence this sprint" — she hears scope honesty, not a no.
2. WIP limits help *inside* the sprint (QA column limit prevents B1/B6
   finishing untested) but fight the sprint container if pull-based work
   replaces the committed scope — limit columns, keep the goal.
3. Erosion candidate: peer-review count (2 approvers) under deadline —
   protect via CI-blocked merges (pre-commitment), not goodwill.

## Preparation notes

Run the checker on the selection CSV before grading prose — arithmetic is
free to verify; spend your reading time on goal-fit arguments and DoD
testability. This lab is the week the agile track's numbers connect to the
predictive track's audit discipline (Lab 5/13).
