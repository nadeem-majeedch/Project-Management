# 07 — Teaching-Material Inventory

Status legend: ✅ generated this pass · 🔶 shell created, content authored during delivery · ⬜ planned

## 1. Student-facing (published via docs/)

| Artifact | Location | Count | Status | Source of truth |
|---|---|---|---|---|
| Landing page | `docs/index.md` | 1 | ✅ hand-authored | — |
| Course description | `docs/syllabus/course-description.md` | 1 | ✅ hand-authored | — |
| Detailed syllabus (KA map, units, CLO chains) | `docs/syllabus/detailed-syllabus.md` | 1 | ✅ generated | course-data.yaml |
| Textbooks & references | `docs/syllabus/textbooks.md` | 1 | ✅ hand-authored | planning/11 §6 |
| Course policies & expectations | `docs/syllabus/course-policies.md` | 1 | ✅ hand-authored | — |
| Delivery methodology | `docs/syllabus/delivery-methodology.md` | 1 | ✅ hand-authored | — |
| Weekly schedule (dates + assessment) | `docs/syllabus/weekly-schedule.md` | 1 | ✅ generated | course-data.yaml |
| Policies page | `docs/assessments/policies.md` | 1 | ✅ hand-authored | 05-framework §4 |
| Assessment strategy | `docs/assessments/assessment-strategy.md` | 1 | ✅ hand-authored | 05-framework |
| Academic integrity & responsible AI | `docs/assessments/academic-integrity.md` | 1 | ✅ hand-authored | planning/11 |
| Grading page | `docs/assessments/grading.md` | 1 | ✅ hand-authored (mirrors 05 + YAML) | course-data.yaml |
| Curriculum map | `docs/lectures/index.md` | 1 | ✅ generated | course-data.yaml |
| Lecture pages | `docs/lectures/L01..L32-*.md` | 32 | ✅ generated skeletons | course-data.yaml |
| Case briefs (all 105 published) | `docs/cases/CS-01..CS-105.md` | 105 | ✅ generated full briefs | planning/cases/band-*.yaml |
| Case directory (band-organized + tag filter) | `docs/cases/index.md` | 1 | ✅ generated | case-catalog.yaml + bands |
| Case answer keys (instructor-only) | `instructor/answer-keys/cases/CS-01..CS-105.md` | 105 | ✅ generated keys | band solution blocks |
| Case numeric checker | `tools/check_cases.py` | 1 | ✅ recomputes 30+ numeric blocks | band numeric blocks |
| Lab briefs (CAMPUS-MEND scenario, full briefs) | `docs/labs/` | 16 | ✅ hand-authored | labs data-pack + templates |
| Assignment briefs (rubric-aligned) | `docs/assignments/` | 3 | ✅ hand-authored | assessment_plan |
| Capstone pack (spec, milestones, rubrics, peer review) | `docs/capstone/` | 8 | ✅ hand-authored | capstone milestones L08/L12/L27/L32 |
| Glossary (46 terms incl. governance/AI) | `docs/resources/glossary.md` | 1 | ✅ hand-authored | — |
| Templates + standards | `docs/templates/` (15 md + 12 csv), `docs/resources/` | 2 + 27 | ✅ hand-authored | — |

## 2. Instructor-only (never published; validator-enforced)

| Artifact | Location | Count | Status |
|---|---|---|---|
| **Full teaching packages** (16-section packages by module U1–U7: objectives, prior knowledge, teaching notes, definitions, CS/DS examples, worked examples — WBS, dependencies, CPM/float, cost, budget variance, EVM, P×I, agile estimation & forecasting — misconceptions, activities, discussion, exercise, exit tickets, attributable references, 2-hour plans, prep notes, resource links) | `instructor/teaching-packages/U*/L*.md` | 32 | ✅ hand-authored; gate-10 validated |
| **Lab answer keys** (model answers, common errors, reflection guidance, prep notes) + `data/` machine-readable answers (CPM, risk scores, EVM, sprint capacity, Monte Carlo reference JSON) | `instructor/lab-solutions/` | 16 + 5 | ✅ hand-authored; recomputed by `tools/check_answers.py` (gate 11) |
| **Lecture slide decks** (Marp Markdown → self-contained HTML via `tools/build_slides.py`: objectives, Mermaid diagrams, CS/DS examples, checker-verified calculations, case-activity slides, discussion, summary/exit ticket, references, embedded speaker notes, WCAG-AA theme) | `instructor/slides/L01..L32-slides.md` + `build/` | 32 | ✅ hand-authored; `tools/check_slides.py` + gate 14 |
| Lesson plans (2-h timing, facilitation) | `instructor/lesson-plans/L01..L32.md` | 32 | ✅ generated |
| Case index (full summaries) | `instructor/answer-keys/case-index.md` | 1 | ✅ generated |
| Case facilitation notes | `instructor/answer-keys/` | per-case | ⬜ authored progressively |
| Quiz items (Q1–Q3) | `instructor/exam-bank/` | 3 sets (A+B versions, keys, marking guides) | ✅ hand-authored; gate 13 |
| Midterm + final exams | `instructor/exam-bank/` | 2 (full keys + marking guides) | ✅ hand-authored; gate 13 |
| Question banks (all 32 lectures) | `instructor/exam-bank/question-bank-u1..u7.md` | 128 tagged items | ✅ hand-authored; gate 13 |
| Capstone + portfolio rubrics | `instructor/rubrics/` | 4 + assignment marking guides | ✅ lab rubric refreshed to 16 labs; gate 13 |
| Full case texts (62 extension cases) | instructor + LMS | 62 | ⬜ authored progressively |

## 3. Data & tooling

| Artifact | Location | Status |
|---|---|---|
| Course data (lectures, CLOs, units, assessment) | `planning/course-data.yaml` | ✅ |
| Case catalog (105 cases) | `planning/case-catalog.yaml` | ✅ |
| Generator | `tools/scaffold.py` | ✅ |
| Validator | `tools/validate.py` | ✅ |
| Site config | `mkdocs.yml` | ✅ |
| CI workflows | `.github/workflows/ci.yml`, `pages.yml` | ✅ |
| Stylesheet | `docs/stylesheets/custom.css` | ✅ |
| Requirements | `requirements.txt` | ✅ |

## 4. Architecture dossier (planning/)

01 inspection · 02 architecture · 03 curriculum map · **04 CLO mapping (generated)**
· 05 assessment framework · **06 case matrix (generated)** · 07 this inventory
· 08 case-study architecture · 09 website information architecture
· 10 generation & validation plan · 11 academic-foundation extension (Prompt 1:
measurable CLOs, knowledge-area map, gate 9, instructor decisions, sources)

## 5. Content-depth policy

Generated lecture pages are **skeletons**: topic structure, objectives, case
links, activities, and assessment anchors. Narrative depth (slides, worked
examples, readings) is authored per lecture during delivery; the skeleton
format keeps those additions additive so regeneration never overwrites
hand-written sections — new prose belongs below the generated "Core content"
block or in slide decks stored outside `docs/lectures/`.
