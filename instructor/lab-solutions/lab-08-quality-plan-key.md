# Lab 8 Answer Key — Quality Management Plan

## Model QA vs QC mapping (≥ 6 activities required)

| Activity | Type | Evidence |
|---|---|---|
| Gate process audits (end B, end D, end G) | QA | audit report vs checklist |
| Test-evidence reviews (G's artifacts quality) | QA | review record |
| Escape analysis at closure | QA | escape log + root cause |
| Load test (QO1: p95 ≤ 2.0 s, 3 runs) | QC | load-test report |
| Data-contract test in CI (schema drift, D/E) | QC | CI report |
| QA ticket sampling on E's % claims | QC | sampling memo |
| 48h SLA staging rehearsal (QO2) | QC | rehearsal timing log |
| Regression timer (QO4 ≤ 25 min) | QC | CI timer |

**Verification matrix (model):** QO1 load test, 3 runs, p95 ≤ 2.0 s, QA lead;
QO2 rehearsal ×2, finish + ≥ 2 h margin; QO3 escape analysis per release,
≤ 2; QO4 CI timer every run, ≤ 25 min; plus E-audit row — E % claims verified
by ticket sampling against E's 20 QA h.

**Root-cause palette (pass = 2 tools with triggers):** control chart on
result-publishing job duration (fires when 2 consecutive runs exceed the
46-h point); 5-Why within 48 h of any escape; Pareto monthly on defect
backlog.

## CoQ split (model; students must total 480 and justify)

| Category | h | Rationale |
|---|---|---|
| Prevention | 100 | data-contract tests, review templates, DoD discipline — the 2018 project had none |
| Appraisal | 260 | load tests, rehearsals, sampling, audits — this is where CAMPUS-MEND's money goes |
| Internal failure | 120 | rework from gate defects (expected, funded) |
| External failure | 0 (target) | anything escaping = QO3 breach + incident process |
| **Total** | **480** | |

Accept other splits that (a) total 480, (b) push the failure share down vs
the 2018 pattern, (c) justify prevention > 0 explicitly.

## Common wrong answers

| Error | Correction |
|---|---|
| QA/QC labels swapped (audit called QC) | QA = process ("are we doing it right?"); QC = product ("did we build it right?") |
| Verification without tolerance | "tested for performance" ≠ p95 ≤ 2.0 s, 3 runs |
| CoQ = equal quarters without argument | the split IS the plan's philosophy; unequal on purpose |
| E-audit rule missing | Lab 13's audit depends on this row existing now |
| Objectives without sources | every QO cites §G |

## Reflection guidance

1. Best single row: QO2 (staged rehearsal with ≥ 2 h margin) — it simulates
   the exact 2018 failure (result-day publishing) before students see it.
2. G's 240 appraisal h buy down external-failure cost: one result-day outage
   in 2018 cost a student-union complaint, a fixed delay policy, and the
   whole rebuild — the 240 h are the cheapest insurance on the books.
3. QO1: quality evidence doubles as progress evidence (load test pass = G
   milestone) — when quality evidence is late, progress claims (E!) become
   unverifiable, which is precisely week 9's story.

## Preparation notes

Cross-reference Lab 5 acceptance criteria during grading; orphaned QOs
(objective with no dictionary criterion) predict capstone integration
failures. This plan is short on purpose — the E-audit row is the part worth
reading closely.
