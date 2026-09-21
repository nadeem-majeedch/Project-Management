---
title: "Lab 8 — Quality Management Plan"
lab: 8
week: 8
lecture: 14
time: "2 hours in-lab + 1 hour refinement"
deliverable: "Quality management plan with objectives from §G, verification matrix, CoQ split"
submitted: "LMS, within one week"
---

# Lab 8 — Quality Management Plan

## 1. Objectives
1. Turn the §G targets into measurable quality objectives with tolerances.
2. Distinguish QA (process audits) from QC (product verification) in a funded plan.
3. Budget the 480 QA hours across prevention–appraisal–failure and defend the split.

## 2. Background & scenario
The 2018 portal's reputation damage came from *escaped* defects: peak-load
crashes and result-day failures nobody load-tested. The registrar now asks a
single question in every steering meeting: "what tells us quality before
students tell us?" Your quality plan is the answer — and week 9's crisis
(Lab 13) will test whether your verification matrix would actually have
caught the E-claim.

## 3. Required tools
- [Quality plan template](../templates/quality-plan-template.md)
- [Data pack §G (targets), §B (QA hours)](data-pack.md)
- Lab 5 dictionary (acceptance criteria feed the verification matrix)

## 4. Step-by-step instructions
1. **Objectives (20 min).** Restate §G as QO1–QO4 with measure/target/source (the template pre-fills these — verify you understand each).
2. **QA vs QC mapping (25 min).** Place at least six activities into QA vs QC. QA examples: gate audits, test-evidence reviews, escape analysis. QC examples: load test, data-contract test in CI, ticket sampling. Every activity must name its evidence.
3. **Verification matrix (30 min).** One row per QO: method, sample size, tolerance, owner. The E-audit rule belongs here: E's percent claims verified by QA ticket sampling against the 20 QA h.
4. **Root-cause palette (15 min).** Pick ≥ 2 tools with concrete triggers (e.g., control chart on the result-publishing job; 5-Why after any escape).
5. **CoQ split (20 min).** Distribute the 480 QA h across prevention / appraisal / internal failure / external failure (target ≈ 0). Justify: why does CAMPUS-MEND deserve a heavier prevention share than the 2018 project would have chosen?
6. **Sign-off block (10 min).** Sponsor confirms tolerances; QA lead confirms the matrix is executable within budget.
7. **Refine (out of lab, 1 h).** Cross-check: every QO traceable to a dictionary acceptance criterion (Lab 5).

## 5. Your tasks (checklist)
- [ ] QO1–QO4 with measures, targets, sources
- [ ] ≥ 6 activities mapped QA vs QC with evidence named
- [ ] Verification matrix complete incl. E-audit rule
- [ ] ≥ 2 root-cause tools with triggers
- [ ] CoQ split totals 480 h with justification
- [ ] Sign-off block filled

## 6. Expected outputs
`quality-plan.md`. Submit via LMS.

## 7. Reflection questions
1. The registrar asks "how do we know quality before students do?" — which single row of your verification matrix is your answer, and why that one?
2. G's 240 QA hours dominate the budget. What failure cost is this appraisal spend buying down — estimate it in one sentence using the 2018 story.
3. Which QO is most at risk *because of* the week-9 E-claim problem (preview: quality evidence is also progress evidence)?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Objectives | measurable, sourced to §G | restated adjectives |
| QA/QC split | correct mapping with evidence | labels swapped |
| Verification matrix | executable rows incl. E-audit | method without tolerance |
| CoQ | totals 480 h, justified split | equal split without thought |
| Traceability | QOs ↔ dictionary criteria | orphaned objectives |

## 9. Related material
[Lecture 14 — Quality & data quality](../lectures/L14-14-quality-data-quality.md) ·
[Case CS-18](../cases/CS-18.md) ·
[Lab 13's audit is your matrix in action](lab-13-evm-recovery.md)
