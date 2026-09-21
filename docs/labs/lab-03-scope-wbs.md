---
title: "Lab 3 — Requirements & Scope Statement + WBS"
lab: 3
week: 5
lecture: 9
time: "2 hours in-lab + 2 hours refinement"
deliverable: "Scope statement + 3-level WBS with hours roll-up (100% rule)"
submitted: "LMS, within one week"
---

# Lab 3 — Scope & WBS

## 1. Objectives
1. Write testable requirements with MoSCoW priorities and explicit exclusions.
2. Decompose the eight-package spine into a 3-level, deliverable-oriented WBS.
3. Enforce the 100% rule numerically: child hours sum to parent, tree total = 1,808 h (from data pack §B).

## 2. Background & scenario
The registrar signed a charter promising "the same student-facing features,
rebuilt properly." Scope failure is now the biggest threat: every stakeholder
who ever mentioned a wish considers it in scope. Your defense is a scope
statement with testable requirements and a WBS whose arithmetic closes.
The [data pack §B](data-pack.md) gives authoritative hours per package —
your WBS decomposition must sum to exactly those hours.

## 3. Required tools
- [Scope statement template](../templates/scope-statement-template.md)
- [WBS template](../templates/wbs-template.md) + [hours worksheet CSV](../templates/data/wbs-hours-worksheet.csv)
- [Data pack §A (schedule spine) and §B (hours)](data-pack.md)

## 4. Step-by-step instructions
1. **Requirements (30 min).** From the story, extract 8–12 requirements as testable sentences ("Result publishing completes within 48 h of ceremony end" — verifiable; "fast results" — not). Prioritize MoSCoW; map each to a deliverable.
2. **Exclusions (15 min).** ≥ 3 explicit exclusions with destination (parking lot / other project / never). Think: mobile app? fee payment itself? the *legacy* archive?
3. **WBS decomposition (40 min).** Level 1 = CAMPUS-MEND. Level 2 = the eight §A packages + a sized PM package. Level 3 = 2–4 work packages inside each level-2, using the §B hour totals. Deliverable-oriented nouns; no "do testing" — "performance test suite (evidence for QO1)".
4. **100%-rule audit (20 min).** Sum level-3 hours per level-2; compare against §B. Fill the worksheet CSV. Any mismatch = a missing or overlapping package.
5. **Rolling-wave note (10 min).** Which branches are fully decomposed now, which wait, and why (hint: E and F depend on discovery findings).
6. **Refine (out of lab, 2 h).** Dictionary preview: pick two work packages and write acceptance criteria + EV rule (full dictionary is Lab 5).

## 5. Your tasks (checklist)
- [ ] 8–12 testable requirements, MoSCoW-prioritized, deliverable-mapped
- [ ] ≥ 3 exclusions with destinations
- [ ] 3-level WBS, deliverable-oriented, PM package explicitly sized (96 h)
- [ ] Level-3 sums = §B package hours exactly (total 1,808 h)
- [ ] Worksheet CSV filled and consistent
- [ ] Rolling-wave decisions justified
- [ ] 2 acceptance criteria + EV rules drafted

## 6. Expected outputs
`scope-statement.md` + `wbs.md` (+ filled `wbs-hours-worksheet.csv`). Submit all three via LMS.

## 7. Reflection questions
1. Which requirement was hardest to make testable, and what measure did you attach?
2. If a level-2 package's children sum to 130% of its §B hours, what are the two most likely causes — and which fix is a scope fix vs an estimating fix?
3. Why does the 100% rule make percent-complete claims *auditable* later in the project?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Requirements | testable sentences, MoSCoW, mapped | vague wishes |
| Exclusions | explicit with destinations | absent |
| WBS structure | 3 levels, deliverable nouns, no misc nodes | activity-verb soup |
| 100% rule | sums exact at every parent | arithmetic gaps |
| PM sizing | 96 h explicitly placed | PM invisible |

## 9. Related material
[Lecture 9 — Scope & WBS](../lectures/L09-09-scope-wbs.md) ·
[Assignment A1](../assignments/a1-scope-schedule.md) (this WBS is the A1 draft) ·
[Case CS-11](../cases/CS-11.md)
