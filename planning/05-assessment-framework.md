# 05 — Assessment & Grading Framework

> Canonical data: `assessment_plan` in `planning/course-data.yaml` (weights validated to sum to 100).
> Published version: `docs/assessments/grading.md`.

## 1. Grade composition

| ID | Component | Weight | CLOs | Timing | Notes |
|---|---|---|---|---|---|
| A1 | Quizzes (best 2 of 3) | 10% | CLO1, CLO2, CLO5 | L04, L12, L26 | 15 min, start of lecture; lowest dropped |
| A2 | Assignment 1 — Scope & Schedule | 10% | CLO2 | Release L14, due L16 | WBS + estimates + network + Gantt |
| A3 | Assignment 2 — Risk Register & Responses | 10% | CLO4 | Release L17, due L19 | ISO 31000-aligned register |
| A4 | Assignment 3 — EVM Case Analysis | 10% | CLO4 | Release L19, due L21 | Compute + diagnose + recommend |
| A5 | Midterm Exam | 20% | CLO1–CLO4 | Week 10–11 window | L01–L20, quantitative emphasis |
| A6 | Case Portfolio | 10% | CLO1, CLO2, CLO4, CLO5 | Rolling, 3 per unit | 12 analyses of 300–500 words each |
| A7 | Capstone Project & Defense | 25% | CLO5, CLO6 | Team from L08; plan L27; defense L32 | Team charter, master plan, defense |
| A8 | Final Exam | 5% | CLO1, CLO6 | Exam week | Comprehensive, emphasis L21–L32 |

Design intent: 55% of the grade accrues before the capstone crunch (A1–A5 =
60% technically, but five of eight components land by week 11), keeping the
final three weeks focused on synthesis rather than new testing. The low
final-exam weight reflects the program's project-based assessment philosophy;
the midterm carries the individual quantitative gate.

## 2. Assessment ↔ CLO coverage check

| CLO | Components | Verdict |
|---|---|---|
| CLO1 | A1, A5, A6, A8 | ≥2 components ✓ |
| CLO2 | A1, A2, A5, A6 | ✓ |
| CLO3 | A5 | single-component ⚠ noted: CLO3 is also practiced in CS-17/CS-26 (in-class) and feeds CLO4 assignments; accepted for v1.0, revisit at first curriculum review |
| CLO4 | A1, A3, A4, A5, A6, capstone checkpoint | ✓ strongest coverage |
| CLO5 | A1, A6, A7 | ✓ |
| CLO6 | A7, A8 | ✓ |

## 3. Grading scale

| Letter | Range | | Letter | Range |
|---|---|---|---|---|
| A | ≥ 87 | | C+ | 67–69 |
| A− | 83–86 | | C | 63–66 |
| B+ | 79–82 | | C− | 60–62 |
| B | 75–78 | | D | 55–59 |
| B− | 70–74 | | F | < 55 |

Plus the standard constraints: ≥ 40% on the midterm to pass the course;
capstone defense is mandatory to earn A7 credit.

## 4. Policies (published verbatim in docs/assessments/policies.md)

- **Late work:** 5% per 24 h, 5-day ceiling; capstone plan draft is exempt from late acceptance (it feeds peer review).
- **Missed quiz:** best-2-of-3 absorbs one miss; a second miss needs documentation.
- **Collaboration:** assignments are individual unless marked team; the capstone is a team deliverable with an individual accountability memo.
- **AI use:** permitted for drafting and exploration with disclosure; fabrication of data, sources, or results is an integrity violation. Course norms co-written in L31.
- **Re-grade requests:** within one week of return, in writing, citing the rubric line.

## 5. Rubric architecture (instructor-only shells in `instructor/rubrics/`)

| Rubric | Dimensions | Levels |
|---|---|---|
| Case portfolio (per analysis) | concept accuracy, technique application, assumption honesty, communication | 4 × 4-point |
| Capstone master plan | completeness, internal consistency, tailoring justification, risk realism, communication | 5 × 4-point |
| Capstone defense | plan quality, defense Q&A, team process evidence, individual contribution | 4 × 4-point |
| Lab reports | task completion, correctness, reflection | 3 × 4-point |

Rubric files are created as structured shells with dimension tables and
point-guides; instructors finalize wording before week 1 (tracked in
`10-generation-and-validation-plan.md` § remaining work).

## 6. Academic integrity

Violations follow university policy; course-specific expectations: cite all
standards by edition and year; disclose AI assistance; individual work means
individual writing. The case portfolio is the integrity honeypot — templated
analyses are trivially detectable and heavily penalized.
