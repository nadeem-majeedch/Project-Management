# Exam Bank — PM-401 assessment package

**Status: populated.** Every component below is authored, keyed, and aligned
to the approved framework (`planning/05-assessment-framework.md`,
`planning/course-data.yaml` assessment_plan, `docs/assessments/grading.md`).
Weights are fixed by the YAML — never adjust a paper's stated weight without
changing the framework in all three places.

## Question banks (per unit; all items tagged lecture · CLO · Bloom · difficulty · type)

| File | Unit | Lectures | CLO focus | Items |
|---|---|---|---|---|
| `question-bank-u1.md` | U1 Foundations & Strategy | L01–L04 | CLO1 | 18 |
| `question-bank-u2.md` | U2 Life-cycles & Initiating | L05–L08 | CLO1, CLO5 | 18 |
| `question-bank-u3.md` | U3 Planning the Work | L09–L14 | CLO2, CLO3 | 20 (7 numeric, machine-verified) |
| `question-bank-u4.md` | U4 Risk, Uncertainty & Control | L15–L20 | CLO4 | 20 (7 numeric, machine-verified) |
| `question-bank-u5.md` | U5 Adaptive Delivery & Teams | L21–L26 | CLO5 | 20 |
| `question-bank-u6.md` | U6 Integration, Ethics & Closing | L27–L30 | CLO6 | 18 (1 numeric; one variant flagged for hand-verification) |
| `question-bank-u7.md` | U7 Synthesis & Capstone | L31–L32 | CLO6 | 14 |

Numeric chains reuse the case collection's verified arithmetic
(`tools/check_cases.py`): CS-15/17/21/22/23/24/26/28/57/63/82/104. When
modifying any numeric item, re-derive it through the checker pattern — never
hand-adjust a network, budget, or EVM chain.

## Ready-to-print papers (A/B versions, keys, marking guides)

| File | Assessment | Coverage | Marks | When |
|---|---|---|---|---|
| `quiz1.md` | A1/Q1 (10% pooled) | L01–L04 · CLO1 | 7 | L04 |
| `quiz2.md` | A1/Q2 | L09–L12 · CLO2 | 8 | L12 |
| `quiz3.md` | A1/Q3 | L21–L26 · CLO5 | 8 | L26 |
| `midterm.md` | A5 (20%) | L01–L20 · CLO1–CLO4 | 40 | weeks 10–11 |
| `final.md` | A8 (5%) | comprehensive, emphasis L21–L32 | 20 | exam week |

Midterm pass rule: ≥ 40% (16/40) — from the grading page; scripts under
threshold are reviewed, not auto-failed.

## Marking guides for coursework

| File | Covers |
|---|---|
| `../rubrics/assignment-marking-guides.md` | A2 scope & schedule · A3 risk register · A4 EVM analysis (0–3 anchors per artifact) |
| `../rubrics/lab-reports.md` | 16 labs, pass/refine, per-lab checklists |
| `../rubrics/case-portfolio.md` | A6 portfolio (unchanged; already aligned) |
| `../rubrics/capstone-plan.md` + `capstone-defense.md` | A7 plan + defense |
| Student-facing rubric: `docs/capstone/presentation-rubric.md` · peer instruments: `docs/capstone/peer-review.md` | A7 presentation layer |

## Integrity and reuse rules

- Papers are single-semester; regenerate numeric variants through the
  checker before each delivery.
- Exam-use cases (23 marked `exam` in the band files) may be adapted:
  modify numbers, keep the concept target, never reuse unchanged.
- Student/instructor separation is enforced by validator gate 7 (site leak
  check) — nothing from this folder is published.
