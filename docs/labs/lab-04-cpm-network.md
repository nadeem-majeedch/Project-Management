---
title: "Lab 4 — Dependency Network & Critical Path"
lab: 4
week: 6
lecture: 11
time: "2 hours in-lab + 1 hour refinement"
deliverable: "AON network + full forward/backward pass + float table + compression memo"
submitted: "LMS, within one week"
---

# Lab 4 — Dependency Network & Critical Path

## 1. Objectives
1. Build an AON network from the §A schedule with justified dependency types.
2. Execute a complete, checkable forward and backward pass (ES/EF/LS/LF).
3. Compute total and free float, identify the critical path and the near-critical path, and write a numbers-based compression memo.

## 2. Background & scenario
The registrar's 17-week window is fixed (constraint R4). The §A schedule's
CPM finish is exactly 17 weeks — zero float on the whole project — which the
sponsor finds "reassuring." Your job this lab is to show why that comfort is
false: the *near-critical* paths and the float arithmetic tell the real risk
story. All calculations have independently checkable answers (the answer
checker verifies your float table).

## 3. Required tools
- [Activity & dependency template](../templates/activity-dependency-template.md)
- [CPM worksheet template](../templates/cpm-worksheet-template.md) + [pass worksheet CSV](../templates/data/cpm-pass-worksheet.csv)
- [Data pack §A](data-pack.md)

## 4. Step-by-step instructions
1. **Activity table (15 min).** Copy §A into the template; add owner per activity.
2. **Dependency audit (20 min).** F→G is listed as FS from C, E, F. For each dependency, label it mandatory (physical/contractual) or discretionary, and justify one lead or lag you propose (e.g., could F start SS+2 after B? What breaks if you're wrong?). Default = FS with no lead/lag.
3. **Forward pass (20 min).** ES/EF for all eight activities. Checkpoints: EF(D) = 10, EF(E) = 14. Project EF = 17.
4. **Backward pass (20 min).** LF/LS from the finish. Checkpoints: LS(D) = 5, LS(C) = 7.
5. **Float table (15 min).** Total float = LS − ES per activity; free float = min(ES of successors) − EF. Fill the CSV (`critical` column TRUE/FALSE). Verify: exactly two activities have TF = 2 (C and F — they share the same near-critical path), all others TF = 0.
6. **Near-critical analysis (15 min).** The path A→B→C→F→G→H runs 15 of 17 weeks (float 2). Write the two-sentence warning for the sponsor: two one-week slips (one on C, one on F) move the critical path — and C sits *before* both F and G, so it hides in the middle of the network.
7. **Compression memo (20 min).** Deadline moves to 15 weeks. Crash candidates from the lab sheet: D can crash 5→4 wk at PKR 60,000/wk; E can crash 4→3 wk at PKR 75,000/wk. Compute the cheapest 2-week compression; name what you would NOT do and why (two traps: crashing C — check its float first; fast-tracking E over D — check the rework risk).
8. **Refine (out of lab, 1 h).** Redraw the network cleanly; re-check the CSV against your paper pass.

## 5. Your tasks (checklist)
- [ ] Activity table with owners and labeled dependency types
- [ ] Full pass: ES/EF/LS/LF all filled, checkpoints match
- [ ] Float table complete; TF and FF computed for all 8 activities
- [ ] CSV filled with `critical` column; checker passes
- [ ] Critical path + near-critical path named with floats
- [ ] Compression memo with cost arithmetic and a rejected option

## 6. Expected outputs
`network.md` (activity table + diagram + memo) and `cpm-pass-worksheet.csv`
(filled). The CSV is machine-checked; the memo is human-graded. Submit both.

## 7. Reflection questions
1. E has total float 0 but G is where both paths meet. Why doesn't E's zero float make *G* critical by itself?
2. Your proposed lag/lead from step 2: if it slips by one week, which float numbers change? Recompute one.
3. C has total float 2 but sits upstream of both F and G. Why is shared path float (A→B→C→F→G→H) more dangerous than two independent float pockets?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Pass arithmetic | all 8 rows correct and checkable | errors or missing pass |
| Float | TF and FF distinguished correctly | one number for both |
| Critical analysis | CP + near-critical named with floats | CP only |
| Compression | arithmetic + rejected option | "add people" |
| Dependencies | types labeled, leads/lags justified | all FS, unexamined |

## 9. Related material
[Lecture 11 — CPM & PERT](../lectures/L11-11-cpm-pert.md) ·
[Case CS-15](../cases/CS-15.md) ·
[Lab 11 re-uses this network with uncertainty](lab-11-monte-carlo.md)
