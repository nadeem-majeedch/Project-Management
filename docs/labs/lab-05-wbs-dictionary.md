---
title: "Lab 5 — WBS Dictionary"
lab: 5
week: 6
lecture: 12
time: "2 hours in-lab + 1 hour refinement"
deliverable: "Complete dictionary rows for all eight packages (owners, estimates, acceptance, EV rules)"
submitted: "LMS, within one week"
---

# Lab 5 — WBS Dictionary

## 1. Objectives
1. Complete dictionary rows for all eight packages: owner, description, predecessors, estimates, acceptance criteria, EV rules, QA budget.
2. Choose EV rules that resist completion-claim inflation.
3. State the E-audit rule that Lab 13 will enforce.

## 2. Background & scenario
Lab 3's WBS gives the tree; the dictionary makes it executable. In week 9
([Lab 13](lab-13-evm-recovery.md)) a team member will claim package E is
55% done. Whether that claim survives an audit depends on what you write
into the dictionary *now*: acceptance criteria and EV rules are the audit
rails. This lab is deliberately quiet — filling 8 rows properly is the work.

## 3. Required tools
- [WBS dictionary template](../templates/wbs-dictionary-template.md)
- [Data pack §B (hours → estimates) and §G (quality targets)](data-pack.md)
- Your Lab 3 WBS output

## 4. Step-by-step instructions
1. **Row per package (50 min).** For each of A–H: owner (role, not person), 2–3-line description, predecessors, estimates (O/M/P → PERT), acceptance criterion (observable evidence), EV rule, QA budget.
2. **EV rule selection (20 min).** Apply the palette: H = 0/100 (binary SLA evidence); G = weighted milestones 30/30/40 (design pass → evidence pass → load-test pass). Justify each choice in one line.
3. **QA budget split (15 min).** Distribute the 480 QA hours across A–H per data-pack §B. Then write the E-audit rule: any percent claim on E requires tickets against E's 20 QA hours.
4. **PERT skew note (10 min).** For two packages, write O/M/P where the distribution is right-skewed (e.g., E: O = 3, M = 4, P = 8 — integration surprises add work). Recompute PERT = (O + 4M + P)/6 and note the skew direction.
5. **Refine (out of lab, 1 h).** Add the change-discipline footer: post-signature dictionary edits need a CR reference.

## 5. Your tasks (checklist)
- [ ] All 8 rows complete, all columns filled
- [ ] EV rules justified per package
- [ ] QA split totals 480 h; E-audit rule stated
- [ ] PERT skew noted for 2 packages
- [ ] Change-discipline footer added

## 6. Expected outputs
`wbs-dictionary.md` with 8 complete rows + footer. Keep
[wbs-hours-worksheet.csv](../templates/data/wbs-hours-worksheet.csv) current —
Lab 6 and Lab 13 read it. Submit via LMS.

## 7. Reflection questions
1. Why does a 0/100 rule on H (rollout) produce honest reporting while raw percent-complete on E invites inflation? (Two sentences.)
2. Your acceptance criterion for F must catch the week-9 failure the data pack foreshadows. What must it require? (Hint: integration ticket closed.)
3. Which of your EV rules is most likely to *understate* progress — and is that bias safe for CAMPUS-MEND's SLA? Why?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Rows complete | all 8 rows, all columns | gaps |
| EV rules | justified per package | defaults without reason |
| QA split | 480 h accounted; E rule stated | totals off or rule missing |
| Acceptance criteria | observable evidence named | "works well" |
| Change discipline | CR footer present | none |

## 9. Related material
[Lecture 12 — Schedule tools](../lectures/L12-12-schedule-tools.md) ·
[Case CS-16](../cases/CS-16.md) ·
[Lab 13 audit uses these EV rules](lab-13-evm-recovery.md)
