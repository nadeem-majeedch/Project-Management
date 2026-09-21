---
title: "Lab 9 — Risk Register"
lab: 9
week: 8
lecture: 15
time: "2 hours in-lab + 1.5 hours refinement"
deliverable: "Complete register (8 seed + ≥ 8 own risks) with responses, triggers, residuals"
submitted: "LMS, within one week"
---

# Lab 9 — Risk Register

## 1. Objectives
1. Normalize risk statements to cause → event → effect discipline.
2. Complete the seed register (§E) with owners, responses, triggers, and residuals.
3. Extend with ≥ 8 own risks across required families, including one opportunity.

## 2. Background & scenario
The registrar's committee reads one page of your register before every gate.
R4 has already *realized* (the 48-hour calendar rule binds — it is now a
constraint, not a risk), and R8's ambiguous legacy dates are live. Your
register must show the committee you manage uncertainty deliberately:
every High/Critical risk carries a funded action and a trigger; every
mitigated risk carries a residual.

## 3. Required tools
- [Risk register template](../templates/risk-register-template.md) + [seed CSV](../templates/data/campus-mend-risks.csv)
- [Data pack §E (seed risks + scales + bands)](data-pack.md)
- Lecture 15 worked example (response-strategy selection)

## 4. Step-by-step instructions
1. **Seed completion (40 min).** For each of R1–R8 (skip R4 — realized): verify the statement discipline; add response strategy (avoid/mitigate/transfer/accept/escalate), a concrete action (what/who/when), a trigger (the observable event that fires the action), and residual P and I if mitigated.
2. **Extension (40 min).** ≥ 8 own risks, must cover: people (2+), vendor (1+), data quality (2+, beyond R3/R8), security/privacy (1+), governance (1+), **opportunity (1+)** with exploit/enhance action. No bare-noun statements.
3. **Score check (15 min).** Compute score = max(S,C,Q) × P and band (Low ≤ 5, Medium 6–11, High 12–15, Critical 16–25) for every own risk. Checker verifies your arithmetic.
4. **Trigger quality (15 min).** Every High/Critical trigger must be observable and dated ("R7: vendor misses week-9 checkpoint deliverable" — good; "if vendor seems slow" — not).
5. **Residual discipline (10 min).** For each mitigation: residual score must be strictly lower, and the cost of the action must be named (contingency line or effort).
6. **Refine (out of lab, 1.5 h).** Sort register by band; write the one-paragraph committee summary (top 3 risks + what you need from the committee).

## 5. Your tasks (checklist)
- [ ] R1–R8 completed (response, action, trigger, residual)
- [ ] R4 handled as realized constraint with escalation note
- [ ] ≥ 8 own risks across all required families + 1 opportunity
- [ ] Scores and bands arithmetically correct (checker-verified)
- [ ] Observable triggers on all High/Critical
- [ ] Committee summary written

## 6. Expected outputs
`risk-register.md` + updated `risk-score-worksheet.csv` with your added rows.
Submit both via LMS.

## 7. Reflection questions
1. R2 (DE resignation, P = 2) versus R8 (ambiguous dates, P = 4): which gets the funded action first, and what does the *cause* tell you that the score alone doesn't?
2. Write one mitigation for R1 whose *residual* is worse than the primary risk in a different dimension — explain the trade.
3. Your opportunity: what does exploiting it *cost*, and what would make you abandon the exploit action?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Statements | full cause-event-effect | nouns |
| Responses | strategy + funded action + owner | "monitor closely" |
| Triggers | observable, dated | vibes |
| Scoring | correct arithmetic incl. residual < primary | errors |
| Coverage | all families + opportunity | gaps |

## 9. Related material
[Lecture 15 — Risk foundations](../lectures/L15-15-risk-foundations.md) ·
[Assignment A3](../assignments/a2-risk-register.md) extends this register ·
[Lab 10 plots these on the P×I matrix](lab-10-probability-impact.md)
