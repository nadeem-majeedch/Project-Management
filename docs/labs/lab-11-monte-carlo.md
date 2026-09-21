---
title: "Lab 11 — Monte Carlo Schedule Simulation"
lab: 11
week: 9
lecture: 16
time: "2 hours in-lab + 1 hour refinement"
deliverable: "Simulation run + percentile forecast + deadline memo to the sponsor"
submitted: "LMS, within one week"
---

# Lab 11 — Monte Carlo Schedule Simulation

## 1. Objectives
1. Run a deterministic Monte Carlo simulation of the §A network with uncertain A, B, D.
2. Read the finish distribution: P50/P80/P90/P95 and probability of meeting week 17.
3. Write a sponsor memo that replaces "we're fine" with a defensible confidence statement.

## 2. Background & scenario
Lab 4 told the sponsor "CPM = 17 weeks, zero float." The sponsor's confidence
was premature: three packages are genuinely uncertain (A sign-off drift, B
legacy surprises, D discovery growth), and point estimates hide it. The
simulation quantifies what the sponsor *should* have been told. The script is
provided and deterministic — every student gets identical numbers, and the
checker verifies the summary against the reference.

## 3. Required tools
- Simulation script `tools/campus_mend_sim.py` from the course repository — run:
  `python tools/campus_mend_sim.py` (deterministic: seed 42, 20,000 trials)
- [Schedule CSV](../templates/data/campus-mend-schedule.csv) (input the script reads)
- Lab 4 network (to reason about *which* path the risk lands on)

## 4. Step-by-step instructions
1. **Baseline run (15 min).** Run the script. Record: P50, P80, P90, P95, Prob(finish ≤ 17 wks), mean, stdev, range.
2. **Why the P50 moved (20 min).** The deterministic finish is 17.0 but P50 ≈ 17.9. Explain using the network: A, B, D sit on the critical path; triangular distributions with upward tails push the path longer more often than shorter (check the factors in the script header). Write the two-sentence explanation a sponsor would understand.
3. **Deadline memo (30 min).** One page to the registrar: current confidence, what P80 means for the January calendar, and your recommended decision window. Use numbers from the run — no adjectives without numbers.
4. **Sensitivity check (20 min).** Which package drives the tail? Reason from the network (B feeds C, D, F — the hub) and confirm by editing your *own copy* of the CSV: set B's duration to 4 and re-run. Record the change in P50 and P(on-time). Revert your copy afterwards.
5. **Mitigation tie-in (15 min).** Which Lab 9 risk, if mitigated, would flatten which tail? Name the risk and the mechanism.
6. **Refine (out of lab, 1 h).** Memo polished; run table + memo submitted.

## 5. Your tasks (checklist)
- [ ] Baseline run recorded (all seven summary numbers)
- [ ] P50-vs-CPM explanation written
- [ ] One-page sponsor memo with numbers
- [ ] Sensitivity run documented (before/after P50, P(on-time))
- [ ] Mitigation tie-in to the register

## 6. Expected outputs
`monte-carlo.md` (run table + memo + sensitivity note). The checker verifies
your summary numbers against the reference JSON. Submit via LMS.

## 7. Reflection questions
1. P(on-time) ≈ 8% is a *planning* fact, not a pessimism contest. What three decisions does it legitimately trigger?
2. Why is a single-point promise ("we'll finish in week 17") an integrity problem for a PM, independent of effort?
3. If the sponsor asks for "99% confidence," what does the distribution say that would cost — and is there a cheaper honest answer?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Run | summary table complete & correct | numbers invented |
| Interpretation | P50-vs-CPM explained via network | "simulations vary" |
| Memo | numbers + decision window | adjectives |
| Sensitivity | real re-run with before/after | hypothetical |
| Tie-in | register risk ↔ tail mechanism | generic |

## 9. Related material
[Lecture 16 — Quantitative risk](../lectures/L16-16-quant-risk-simulation.md) ·
[Case CS-22](../cases/CS-22.md) ·
[Lab 15's recovery plan consumes this forecast](lab-15-change-recovery.md)
