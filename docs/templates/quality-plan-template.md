<!--
Template: Quality management plan (Lab 7)
QA asks "are we using the right process?" (audits of process); QC asks "is
this deliverable within tolerance?" (inspection of product). Both are funded
in the QA hours budget — split them honestly.
-->

# Quality Management Plan — [Project name]

## 1. Quality objectives (measurable)
| Objective | Measure | Target | Source |
|---|---|---|---|
| QO1 Performance | p95 portal response | ≤ 2.0 s @ 3,000 users | data-pack §G |
| QO2 SLA margin | batch result job finish vs 48 h | ≥ 2 h margin | data-pack §G |
| QO3 Escapes | production defects per release | ≤ 2 | data-pack §G |
| QO4 Regression speed | full regression suite runtime | ≤ 25 min | data-pack §G |

## 2. Assurance vs control (keep the distinction)
| Question the activity answers | Activity | Type (QA/QC) |
|---|---|---|
| Are we using the right process? | process audit at gates | QA |
| Is this deliverable within tolerance? | load test, code review, data-contract test | QC |
| Did escapes reach production? | escape analysis at closure | QA |

## Root-cause palette — what will your team actually use?
| Tool | When we'd use it | Example from this project |
|---|---|---|
| Fishbone (Ishikawa) | gate retrospectives | (yours) |
| 5-Why | post-incident | (yours) |
| Pareto | defect backlog triage | (yours) |
| Control chart | result-publishing SLA monitoring | (yours) |
| Check sheet | QA ticket sampling (Lab 13 audit) | (yours) |
| Template-based review | test evidence quality | (yours) |

**Rule:** name at least 2 tools with concrete triggers; delete the rest.

## 3. Review & audit schedule (QA)
| Gate | Review type | Entry criteria | Exit criteria |
|---|---|---|---|
| end of B | schema review | B acceptance evidence | severity threshold met |
| end of D | data audit | D acceptance evidence | label-era audit passed |
| end of G | readiness review | G pass report + SLA margin evidence | go/no-go signed |

## 4. Verification matrix (QC)
| Quality objective | Verification method | Sample size | Tolerance | Who |
|---|---|---|---|---|
| QO1 | load test | 3 runs | p95 ≤ 2.0 s | QA |
| QO2 | staged rehearsal timing | 2 runs | finish + ≥ 2 h margin | QA |
| QO3 | escape analysis | every release | ≤ 2 | QA |
| QO4 | CI timer | every run | ≤ 25 min | QA |

## 5. Nonconformity handling
| Step | Owner | SLA |
|---|---|---|
| detect → log defect → triage severity → fix or waive (sponsor-visible waiver only) → re-verify | QA triages; dev fixes | fix per severity; waiver = sponsor decision |

## 6. Data/ML-specific quality controls (where applicable)
| Control | Applies to | Cadence | Evidence |
|---|---|---|---|
| data-contract test in CI | schema drift (packages D/E) | every build | CI report |
| label-era audit | historical bias (R3) | at D and E gates | audit memo |
| model/report review template | reporting deliverable | every publish | review record |

## 7. Cost of quality: prevention–appraisal–failure split of the QA budget (480 h)
| Category | QA hours | % of 480 h |
|---|---|---|
| Prevention | | |
| Appraisal | | |
| Internal failure | | |
| External failure (target ≈ 0) | | |
| **Total** | **480** | **100%** |

## 8. Sign-off
| Role | Confirms |
|---|---|
| Sponsor | objectives & tolerances acceptable |
| QA lead | verification matrix executable with the budget |
| PM | fits the plan; changes via CCB |
