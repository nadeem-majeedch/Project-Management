# Instructor Area — NOT PUBLISHED

Everything in `instructor/` is **instructor-only**. It sits outside `docs/`
so MkDocs never renders it, and `tools/validate.py` (gate 7) plus the CI
workflow fail the build if any of it leaks into `site/`.

| Folder | Contents | Status |
|---|---|---|
| `teaching-packages/` | **32 full teaching packages** (by module: U1–U7) — objectives, prior knowledge, teaching notes, definitions, CS/DS examples, worked examples (incl. WBS, CPM/float, cost, EVM, P×I, agile forecasting), misconceptions, activities, discussion, exercise, exit ticket, references, 2-hour plan, prep notes, resource links | hand-authored; validated by gate 10 (16 sections, no placeholders, titles/links) |
| `lesson-plans/` | 32 generated 2-hour timing plans (L01–L32) | generated — do not hand-edit |
| `lab-solutions/` | **16 lab answer keys** (model answers, common errors, reflection guidance, prep notes) + `data/` machine-readable answer files | hand-authored; verified by `tools/check_answers.py` (run inside validator gate 11) |
| `answer-keys/` | **105 generated case answer keys** (`cases/CS-01..105.md`: model answer, reasoning, alternatives, machine-checked values) + case index | generated from band solution blocks — do not hand-edit; verified by `tools/check_cases.py` |
| `exam-bank/` | **question banks U1–U7 (128 tagged items)**, quiz papers Q1–Q3 (A+B versions, keys, marking guides, debrief notes), midterm (L01–L20, ≥40% pass rule), final — integrity & reuse rules in its README | hand-authored; machine-checked by gate 13 |
| `slides/` | **32 lecture decks** (`L01..L32-slides.md`, Marp-flavored Markdown) + `assets/pm401.css` theme + `build/` HTML (self-contained; Mermaid diagrams; speaker notes embedded; WCAG-AA palette) | hand-authored; `tools/check_slides.py` + `tools/build_slides.py` (gate 14) — rebuild before class: `python tools/build_slides.py` |
| `rubrics/` | case-portfolio, capstone-plan, capstone-defense, lab-reports (16-lab refresh) + assignment marking guides (A2/A3/A4) | finalize wording before week 1 |

Rules:

1. Never move instructor content into `docs/` — publish only what students
   may see; student case briefs carry the task, not the answer.
2. Hand-written instructor files (facilitation notes, exam items) are
   yours to edit; generated files are regenerated from `planning/*.yaml`.
3. Distribute exam-bank material only through the LMS at assessment time.
4. Lab answer keys (`lab-solutions/`) never go to the LMS; the checker
   (`tools/check_answers.py`) gives students row-level correctness without
   revealing models. Re-run it after any edit to `docs/labs/data-pack.md` —
   the calculation chain must stay coherent end to end.
