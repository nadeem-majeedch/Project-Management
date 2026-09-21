---
title: "Lab 14 — Agile Product Backlog & Sprint Planning"
lab: 14
week: 11
lecture: 21
time: "2 hours in-lab + 1 hour refinement"
deliverable: "Ordered backlog + sprint goal + capacity-based selection + DoD + sprint risks"
submitted: "LMS, within one week"
---

# Lab 14 — Agile Product Backlog & Sprint Planning

## 1. Objectives
1. Order the §F backlog by value and goal contribution, not by story size.
2. Run the full capacity arithmetic from gross hours to point capacity.
3. Select a sprint whose items fit capacity *and* serve a written goal; write a testable DoD.

## 2. Background & scenario
Mid-recovery (Lab 13's diagnosis accepted), the team switches the build to
2-week sprints to restore cadence and transparency. The §F backlog (10 items,
66 points) is real scope from the recovery re-plan. Team: 3 devs + 1 QA,
10 productive h/person/week. The registrar needs the result-publishing
rehearsal (B6) *and* the deadlock fix (B1) — but the arithmetic decides what
fits, and the goal decides what matters.

## 3. Required tools
- [Sprint planning template](../templates/sprint-planning-template.md) + [selection worksheet CSV](../templates/data/sprint-plan-worksheet.csv)
- [Data pack §F (backlog)](data-pack.md)
- Lecture 21 worked example (capacity chain)

## 4. Step-by-step instructions
1. **Capacity chain (25 min).** Gross: 4 × 2 wk × 10 h = 80 h. One member has exam week 1 (−6 h). Focus factor 0.7. Ceremonies: planning 2 h, review 1 h, retro 1 h, dailies 10 min × 10 d ≈ 1.7 h. Build capacity = ? h. With the team's measured rate ≈ 1.4 h/pt → point capacity = ? (Show every step; checker verifies the chain.)
2. **Sprint goal (15 min).** Write the outcome sentence first — the registrar's two priorities (B1, B6) plus SLA readiness should shape it. Items must justify themselves against the goal.
3. **Ordering (20 min).** Rank the backlog: value × goal-fit, dependencies respected (B6 rehearsal needs B5's retry handling? state your dependency calls). Mark goal-fit 1–5 per item in the CSV.
4. **Selection (25 min).** Fill items until point capacity is reached. There is more than one defensible cut — you will be graded on the *reasoning*, and the checker verifies only that committed points ≤ capacity and arithmetic is consistent.
5. **DoD (15 min).** ≥ 5 testable items; QA writes at least two (they own verification); include at least one data/SLA-evidence item for B6-type work.
6. **Sprint risks (15 min).** Top 3 risks to the goal, each with trigger + fallback.
7. **Refine (out of lab, 1 h).** Complete template; goal-fit column consistent with your ordering.

## 5. Your tasks (checklist)
- [ ] Capacity chain shown, every step; build h and points computed
- [ ] Sprint goal written before selection
- [ ] Backlog ordered; goal-fit scored in CSV
- [ ] Committed points ≤ capacity (checker-verified); stretch marked
- [ ] DoD ≥ 5 testable items incl. QA-owned + SLA-evidence item
- [ ] 3 sprint risks with triggers + fallbacks

## 6. Expected outputs
`sprint-plan.md` + filled `sprint-plan-worksheet.csv`. Submit both.

## 7. Reflection questions
1. If your point capacity is floor(46.1 / 1.4) but the two registrar-priority items total 26, what does that force you to tell her — and how does the goal sentence carry that conversation?
2. Where would Kanban's WIP limits help this team *inside* the sprint, and where would they fight the sprint container?
3. Which DoD item will be first to erode under deadline pressure — and what pre-commitment protects it?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Capacity | every step visible and checkable | single final number |
| Goal | outcome sentence before items | feature list |
| Selection | fits capacity, goal-justified | knapsack without reasoning |
| DoD | testable, QA-owned items | "done means done" |
| Risks | triggers + fallbacks | named only |

## 9. Related material
[Lecture 21 — Scrum](../lectures/L21-21-scrum.md) ·
[Case CS-28](../cases/CS-28.md) ·
[Lecture 22 — Kanban & flow](../lectures/L22-22-kanban-flow.md) for the WIP question
