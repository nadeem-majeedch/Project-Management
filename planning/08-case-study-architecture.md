# 08 — Case-Study Architecture (105 Progressive Cases)

> Canonical data: `planning/case-catalog.yaml` + `planning/cases/band-{1..4}-*.yaml` (definitions) ·
> machine rendering: `planning/06-case-matrix.md` · numeric checker: `tools/check_cases.py`
> Student-facing briefs: `docs/cases/` (all 105 published; 100 lecture-anchored)
> Instructor keys: `instructor/answer-keys/cases/` (generated from solution blocks; never published)

## 1. Why cases, and why 105

Project management is a judgment discipline; lectures transfer vocabulary,
cases transfer judgment. Five cases per lecture-week pair (105 ÷ 32 ≈ 3.3,
front-loaded into planning weeks) gives every concept at least one applied
encounter plus enough unspent cases to power homework, exams, and the capstone
without reuse — reuse is the death of case credibility.

## 2. Five progression levels

| Level | Name | Cognitive demand | Typical use |
|---|---|---|---|
| L1 | Single-concept drill | recognize/apply one tool to one situation | in-class warm-up |
| L2 | Two-concept applied | combine two tools; first trade-offs | in-class, homework |
| L3 | Multi-concept analysis | integrate a toolchain; analyze causes | in-class, homework, exam |
| L4 | Cross-domain integration | quantitative synthesis under constraints; conflicting objectives | homework, exam |
| L5 | Open-ended strategic | ill-posed, strategic, capstone-grade | capstone feeders |

**Distribution achieved:** L1 × 9, L2 × 18, L3 × 31, L4 × 42, L5 × 5 —
deliberately mid-heavy because 7th-semester students enter with strong
analysis skills and weak integration discipline; the L4 band is where this
course adds the most value.

## 3. Ten domains

| Domain | Theme | Cases | Sample anchors |
|---|---|---|---|
| D1 | Foundations, portfolio, integration | 9 | CS-01 iron-triangle autopsy, CS-95 rebalancing |
| D2 | Life cycles & initiating | 7 | CS-07 hybrid regulatory gates, CS-45 startup MVP |
| D3 | Scope & schedule | 10 | CS-15 CPM network, CS-53 fast-tracking gone wrong |
| D4 | Cost | 6 | CS-57 cloud overrun, CS-58 build-vs-subscribe TCO |
| D5 | Risk & uncertainty | 12 | CS-22 Monte Carlo, CS-70 AI risk-mining pilot |
| D6 | Quality & data quality | 9 | CS-19 data-quality rules, CS-74 fairness metrics |
| D7 | Procurement | 7 | CS-25 ML-API SLA, CS-79 exit clauses |
| D8 | Adaptive delivery & scaling | 11 | CS-31 hypothesis backlog, CS-87 phase-gated agile |
| D9 | Teams & stakeholders | 8 | CS-35 conflict role cards, CS-93 BATNA prep |
| D10 | Ethics, sustainability, closure | 7 | CS-99 padding dilemma, CS-104 benefits shortfall |

## 4. Seed projects (recurring fictional settings)

| Seed | Setting | Serves |
|---|---|---|
| MEDSYNC | Hospital medication-reconciliation platform, regulated health data | compliance, stakeholder, quality cases |
| TELCOCARE | Telecom customer-churn ML product, quarterly commercial targets | data/ML delivery, fairness, vendor cases |
| CAMPUSHUB | University student-services portal, fixed semester budget | familiar ground for first cases |
| GRIDSENSE | Smart-grid streaming analytics, real-time telemetry | scale, cost, risk-quantification cases |
| VOLTPAY | Fintech payments migration, hard cutover dates, vendor-heavy | crisis, runway, vendor-exit cases |
| AGROSENSE | Agricultural IoT + yield prediction, seasonal deadlines | hardware/data-pipeline, sustainability cases |

Cases build on each other within a seed: CS-09 stakeholder register (MEDSYNC)
is reused in CS-10 grid, CS-36 negotiation, CS-92 sponsor reset, CS-100
privacy dilemma — students watch one project evolve across a semester, which
mirrors how real projects feel.

## 5. Usage lanes

| Lane | Cases | Mechanism |
|---|---|---|
| In-class anchor | 43 (one+ per lecture) | published brief in `docs/cases/` |
| Homework | 53 | released via LMS, per-unit |
| Exam items | 17 | modified versions in instructor/exam-bank |
| Portfolio-eligible | homework lane | 12 analyses required (see 05-framework) |
| Capstone feeders | CS-43, CS-76, CS-88, CS-105 | L5 integration |

## 6. Case-page anatomy (student view)

Every published brief contains: case card (difficulty band, level, domain,
seed), learning objectives, project context, problem statement, constraints,
student tasks, expected deliverables, discussion questions, and the grading
rubric — the full 15-element structure. Answer keys (model answer, reasoning,
alternatives, machine-checked values) are generated to
`instructor/answer-keys/cases/` only; the student brief ends before any
solution content, and the validator gates the separation.

## 7. Portfolio mechanics

Students submit 12 case analyses across the semester (≥ 3 per unit boundary:
L08, L14, L20, L26), each 300–500 words, choosing any case from the homework
lane marked for that unit. The portfolio (A6, 10%) rewards breadth: no two
analyses from the same domain. This converts the 105-case catalog from a
teaching prop into an individualized assessment instrument — 105 choose-12 ×
domain constraints means answer-sharing is structurally hard.

## 8. Provenance rule

All 105 cases are fictional composites written for this course. Where a case
echoes a publicly known project, the echo is illustrative only; cases never
assert facts about real organizations, real people, or real outcomes. Real
projects enter only through lecture discussions of published, citable
material — and such claims must carry citations per the no-fabrication rule.
