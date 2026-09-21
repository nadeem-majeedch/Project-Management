---
title: "Lab 7 — Project Cost Baseline"
lab: 7
week: 7
lecture: 13
time: "2 hours in-lab + 1 hour refinement"
deliverable: "Bottom-up cost baseline + S-curve + contract-cap check"
submitted: "LMS, within one week"
---

# Lab 7 — Cost Baseline

## 1. Objectives
1. Build a bottom-up budget from WBS hours × rate card, with indirects and direct costs.
2. Add contingency (risk-derived, inside the baseline) and keep management reserve outside it.
3. Time-phase the baseline into an S-curve and verify the contract cap.

## 2. Background & scenario
The registrar's funding committee approves money by fiscal year, and the
vendor SOW is capped at PKR 1,950,000. Your budget must survive three
audiences: the sponsor (total), the vendor manager (cap), and week-13-you
(EVM needs the time-phased baseline to compute PV). Every number chains from
[data pack §B](data-pack.md) hours × §B rates — the checker verifies the chain.

## 3. Required tools
- [Cost baseline template](../templates/cost-baseline-template.md) + `campus-mend-budget.csv` as a format guide
- [Data pack §B (hours + rates), §C (format reference)](data-pack.md)
- Calculator or spreadsheet; Lab 6 levelled plan for time-phasing

## 4. Step-by-step instructions
1. **Labor build-up (30 min).** Per package: (dev h × 1,800) + (QA h × 1,200) + (DE h × 2,400) + (PM h × 2,200). Sum all eight packages. Checkpoint: labor subtotal = **PKR 3,225,600**.
2. **Indirects (10 min).** 25% of labor → **PKR 806,400**.
3. **Direct costs (15 min).** Monitoring tool PKR 40,000 + test data/GPU PKR 48,000 = **PKR 88,000**. Note in your sheet why vendor effort is *not* a baseline line (fixed-price SOW = seller's cost risk).
4. **Contingency (10 min).** 10% of (labor + indirects + direct) = 10% × 4,120,000 = **PKR 412,000**. Contingency belongs to *known risks* (Lab 9's register funds this) and sits INSIDE the baseline.
5. **Management reserve (5 min).** 5% of the baseline = PKR 226,600 — sponsor-held, OUTSIDE the baseline, inside the funding ask = **PKR 4,758,600**. Explain in one line why MR must not be spendable by the PM.
6. **Contract-cap check (10 min).** Vendor exposure inside your baseline must stay ≤ 1,950,000. Estimate the vendor-relevant work (LMS adapter F: 120 dev h internal? or vendor-executed? read §B note) and state your interpretation + arithmetic.
7. **S-curve (25 min).** Time-phase the labor from the Lab 6 levelled plan into periods P1–P5; add direct costs at their schedule points. Cumulative must end exactly at 4,532,000. Sketch the curve; mark the fiscal-year boundary (end of P2) and the cumulative at that point.
8. **Refine (out of lab, 1 h).** Fill the template; write the assumptions footer (rate card source, contingency derivation, MR justification).

## 5. Your tasks (checklist)
- [ ] Labor table per package with package-level costs
- [ ] Checkpoint matched: labor 3,225,600; indirects 806,400; direct 88,000
- [ ] Contingency 412,000 inside baseline; baseline = 4,532,000
- [ ] MR 226,600 outside baseline; funding ask 4,758,600
- [ ] Vendor cap analysis with stated interpretation
- [ ] S-curve table; cumulative ends exactly at baseline
- [ ] Assumptions footer complete

## 6. Expected outputs
`cost-baseline.md` + S-curve table. The arithmetic is machine-checkable
(the course answer checker runs at validation and grades the chain);
the cap interpretation is graded on reasoning. Submit via LMS.

## 7. Reflection questions
1. Why does contingency live inside the baseline but management reserve outside it? What behavioral problem does this split prevent?
2. If the fiscal-year cap at end of P2 is PKR 2,600,000 and your cumulative there is 2,795,700, what are two legitimate responses? Which is a *plan* change vs a *funding* change?
3. Your EVM story in Lab 13 depends on this S-curve. What breaks in EVM if the S-curve is a straight line?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Labor chain | per-package arithmetic visible | totals only |
| Baseline assembly | contingency vs MR correctly placed | MR inside baseline |
| S-curve | period profile follows schedule; cumulative exact | straight line |
| Cap check | interpretation stated + arithmetic | silent |
| Assumptions | rate card + contingency sourced | invented precision |

## 9. Related material
[Lecture 13 — Cost & budget](../lectures/L13-13-cost-budget.md) ·
[Case CS-17](../cases/CS-17.md) ·
[Lab 13 reads this baseline as PV](lab-13-evm-recovery.md)
