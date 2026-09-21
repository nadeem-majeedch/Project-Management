---
title: "Lab 15 — Change Control & Recovery Plan"
lab: 15
week: 12
lecture: 20
time: "2 hours in-lab + 1.5 hours refinement"
deliverable: "Recovery options analysis + CCB decision record + re-forecast plan"
submitted: "LMS, within one week"
---

# Lab 15 — Change Control & Recovery Plan

## 1. Objectives
1. Convert the Lab 13 diagnosis into recovery options, each with cost, finish forecast, and introduced risk.
2. Run a change-control board (CCB) simulation and produce a decision record with recorded dissent.
3. Produce the re-forecast plan: new baseline position, funding ask, and integrity checks.

## 2. Background & scenario
The corrected numbers (Lab 13): CPI ≈ 0.863, EAC₁ ≈ 5.25M against a 4.53M
baseline; the 48-hour rule makes the deadline immovable; contingency is
412,000 and unspent. Time is not negotiable — so the decision space is
scope and money. The CCB (registrar, vendor manager, PM, QA lead, students'
union observer) must choose. This is the course's decision lab: everything
you have built — network, register, baseline, dashboard, diagnosis — becomes
an input to one defensible recommendation.

## 3. Required tools
- [Monitoring & recovery template](../templates/monitoring-dashboard-template.md) (recovery section)
- Lab 13 outputs (indices, corrected EV, dashboard)
- [Data pack §D](data-pack.md); Lab 11 Monte Carlo memo (confidence context)

## 4. Step-by-step instructions
1. **Option generation (25 min).** Build ≥ 4 options: (O1) crash D and/or E — use Lab 4 slopes (D: 60,000/wk; E: 75,000/wk) and check they still shorten the *current* critical path; (O2) fast-track E over D-remnant work with rework probability stated; (O3) de-scope — defer B7/B10-class items from the re-plan; (O4) fund from contingency + MR request for the gap. For each: cost impact, finish forecast (method named: EAC variant or CPM re-pass), risk introduced.
2. **Constraint check (15 min).** Deadline fixed → any option that moves finish is invalid unless paired with scope change. Vendor SOW cap → options may not increase vendor payment. Calendar rule → rollout H cannot slip. Mark every option PASS/FAIL against the three.
3. **CCB simulation (40 min).** Assigned roles (registrar chairs; vendor manager protects the SOW; QA protects the 48h evidence; union observer asks the student question). PM presents options; CCB decides; record decision + dissent in the minutes format from Lab 12.
4. **Decision record (20 min).** What was decided, by whom, effective when; the CR number; what is re-baselined (scope/budget) vs held.
5. **Re-forecast (25 min).** New funding ask (baseline change + contingency redraw if used), new finish forecast with confidence language from Lab 11, TCPI re-check on the new baseline. Update Views 1–2 of the dashboard.
6. **Integrity check (10 min).** If any option requires the team to sustain CPI > 1.05 for the remainder, the plan must say why that is credible — or choose differently.
7. **Refine (out of lab, 1.5 h).**

## 5. Your tasks (checklist)
- [ ] ≥ 4 options with cost + forecast method + introduced risk
- [ ] Constraint check (deadline, SOW cap, SLA) on every option
- [ ] CCB simulation run; minutes with recorded dissent
- [ ] Decision record with CR number and re-baseline scope
- [ ] Re-forecast: new ask, new forecast, TCPI re-check
- [ ] Integrity check addressed explicitly

## 6. Expected outputs
`recovery-plan.md` + updated dashboard. Submit both.

## 7. Reflection questions
1. Which constraint killed your favorite option — and what does that tell you about constraints discovered *before* planning vs *during*?
2. The union observer asks: "what quality will students lose?" What does your de-scope list protect first, and why?
3. Your re-forecast asks the sponsor for money above the original baseline. What is the *honest* one-sentence framing of that request?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Options | ≥ 4, each with numbers + risk | list without analysis |
| Constraints | checked on every option | checked on the winner only |
| CCB | roles played, dissent recorded | consensus theater |
| Re-forecast | ask + forecast + TCPI re-check | new number, no method |
| Integrity | credibility argued or option changed | hustle promised |

## 9. Related material
[Lecture 20 — Monitoring & control](../lectures/L20-20-monitoring-control.md) ·
[Case CS-27](../cases/CS-27.md) ·
[Lecture 28 — Ethics & governance](../lectures/L28-28-ethics-governance.md) for the CCB authority question
