---
title: "Lab 10 — Probability–Impact Matrix"
lab: 10
week: 8
lecture: 15
time: "2 hours in-lab + 1 hour refinement"
deliverable: "Plotted matrix + defended band→action table + equal-score test + data-quality audit"
submitted: "LMS, within one week"
---

# Lab 10 — Probability–Impact Matrix

## 1. Objectives
1. Plot the full register on the 5×5 P×I grid — every risk exactly once.
2. Defend a band→action table (thresholds, funding, cadence, closing authority).
3. Run the equal-score test and the data-quality audit of your own scores.

## 2. Background & scenario
The committee likes colors; auditors like tables. The matrix is for the
committee; the band→action table is for the auditors. Two risks in your
register share score 12 with *different* dominant impacts — the committee
will see "two orange dots" until your equal-score paragraph shows them why
one buys schedule insurance and the other buys a data fix.

## 3. Required tools
- [P×I matrix template](../templates/probability-impact-template.md) + [score worksheet CSV](../templates/data/risk-score-worksheet.csv)
- Lab 9 register (completed)
- [Data pack §E (scale definitions)](data-pack.md)

## 4. Step-by-step instructions
1. **Score grid (20 min).** Fill the worksheet CSV for all risks (seed + own); checker verifies score = max(S,C,Q) × P and the band assignment.
2. **Plot (15 min).** Place every risk ID in the grid exactly once; annotate cells with L/M/H/C.
3. **Band→action table (25 min).** One row per band: required response, funding source, review cadence, who may close a risk. Defend the cut-offs: why does 12 mean "fund now" while 10 means "watch"?
4. **Equal-score test (15 min).** The two 12s (R1: schedule-dominant; R3: quality-dominant): one paragraph on why their responses differ despite identical scores.
5. **Data-quality audit (20 min).** For each risk: is P evidence-based, interview-based, or folklore? Weakest input marked; schedule the interview/measurement that upgrades the weakest one.
6. **Committee view (10 min).** Produce the one-glance version: grid + top-3 list + the ask. This is what actually gets presented.
7. **Refine (out of lab, 1 h).**

## 5. Your tasks (checklist)
- [ ] Worksheet CSV complete; checker passes (scores + bands)
- [ ] Grid: every risk exactly once, bands annotated
- [ ] Band→action table with defensible cut-offs
- [ ] Equal-score paragraph on the two 12s
- [ ] Data-quality audit for every risk; weakest input scheduled for upgrade
- [ ] Committee one-glance version produced

## 6. Expected outputs
`pxi-matrix.md` + `risk-score-worksheet.csv` (complete). Submit both.

## 7. Reflection questions
1. If the committee insists on moving the High/Critical boundary from 12 to 10, what concrete behavior changes in project spending — and who funds it?
2. R3's P = 3 rests on a label-era audit; your weakest P rests on folklore. Which register is more *defensible* at a gate, and why does evidence quality matter more than the score itself?
3. Name a risk whose true management lever doesn't appear anywhere on the P×I grid.

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Plot | complete, correct, annotated | missing IDs |
| Band table | cut-offs defended with consequences | colors copied |
| Equal-score test | shows response divergence | ignores it |
| Data-quality audit | honest folklore marking + upgrade plan | all "evidence-based" |
| Committee view | one glance communicates | committee reads register |

## 9. Related material
[Lecture 15 — Risk foundations](../lectures/L15-15-risk-foundations.md) ·
[Case CS-21](../cases/CS-21.md) ·
[Lab 11 replaces these point estimates with distributions](lab-11-monte-carlo.md)
