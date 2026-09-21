---
title: "Lab 13 — EVM & Recovery Diagnosis"
lab: 13
week: 10
lecture: 19
time: "2 hours in-lab + 1.5 hours refinement"
deliverable: "Full EVM computation set + measurement-integrity audit + written diagnosis"
submitted: "LMS, within one week"
---

# Lab 13 — EVM & Recovery Diagnosis

## 1. Objectives
1. Compute the complete EVM set for the week-9 status: CV, SV, CPI, SPI, EAC variants, ETC, TCPI.
2. Audit the *measurement* behind EV — indices are only as honest as the completion claims feeding them.
3. Write a diagnosis that separates what the indices say from what they hide.

## 2. Background & scenario
End of week 9 (data-pack §D): PV 2,026,000 · EV 1,762,000 · AC 2,041,000.
The team says package E is 55% done; the QA ticket-sampling audit verifies
40%; F is "complete" with an open integration ticket. Your Lab 5 dictionary
EV rules and Lab 8 verification matrix are the instruments — this lab runs
them. All arithmetic is checker-verified; the diagnosis is graded on
reasoning.

## 3. Required tools
- [EVM worksheet CSV](../templates/data/evm-status-wk9.csv) + [status data](../templates/data/campus-mend-status-wk9.csv)
- [Monitoring dashboard template](../templates/monitoring-dashboard-template.md)
- [Data pack §C (baseline = BAC 4,532,000) and §D](data-pack.md)
- Calculator; Lab 5 dictionary (your EV rules)

## 4. Step-by-step instructions
1. **Core indices (20 min).** CV = EV − AC; SV = EV − PV; CPI = EV/AC; SPI = EV/PV. Record unrounded ratios to 4 decimals. Checkpoints: CPI ≈ 0.8633, SPI ≈ 0.8697.
2. **Forecast family (25 min).** BAC = 4,532,000. Compute EAC₁ = BAC/CPI (inefficiency persists); EAC₂ = AC + (BAC − EV) (one-off); ETC = EAC₁ − AC; TCPI = (BAC − EV)/(BAC − AC). Checkpoints: EAC₁ ≈ 5,250,000; EAC₂ = 4,811,000; TCPI ≈ 1.11.
3. **Variant selection (15 min).** Given §D's physical evidence (E claim inflated; F ticket open), which EAC variant is *defensible*? Write the one-line assumption each variant encodes and pick one.
4. **Measurement audit (30 min).** Re-derive EV with corrected claims: E at 40% verified (not 55%), F held at 90% weighted-milestone credit per dictionary rules. Estimate corrected EV (state your F credit assumption), recompute CPI/SPI/EAC₁. What changed?
5. **Diagnosis (30 min).** ≤ 1 page: (a) what the indices say; (b) what they hide (≥ 2 measurement traps: stale EV claims, the 55% myth, F's open ticket); (c) TCPI credibility — can a team at CPI 0.863 run the rest at 1.09+? (d) recommendation with numbers.
6. **Dashboard rows (10 min).** Fill View 1 and View 2 of the monitoring template with thresholds — this feeds Lab 15.
7. **Refine (out of lab, 1.5 h).**

## 5. Your tasks (checklist)
- [ ] Core indices computed to 4 decimals (checker-verified)
- [ ] EAC family + ETC + TCPI computed (checker-verified)
- [ ] Variant chosen with stated assumption
- [ ] Corrected-EV re-derivation with explicit assumptions
- [ ] Diagnosis page with traps named and TCPI credibility argued
- [ ] Dashboard Views 1–2 filled with thresholds

## 6. Expected outputs
`evm-recovery.md` + filled `evm-status-wk9.csv`. Submit both.

## 7. Reflection questions
1. The 55% claim moved CPI by how much between the reported and corrected EV? What does that tell you about EV-rule design (back to Lab 5)?
2. SPI ≈ 0.87 — "17% late"? Explain what SPI does and does not measure for a project with a fixed 48-hour rule.
3. Your TCPI credibility verdict: if you refuse to promise BAC, what are the two honest alternatives left to the sponsor?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Arithmetic | full set correct to 4 dp | errors or rounding drift |
| Variant | assumption named, choice defended | formula picking |
| Measurement audit | corrected EV with explicit rules | accepts claims |
| Diagnosis | says + hides + credibility | index restatement |
| Dashboard | thresholds explicit | colors without numbers |

## 9. Related material
[Lecture 19 — EVM](../lectures/L19-19-evm.md) ·
[Assignment A4](../assignments/a3-evm-analysis.md) is the formal graded version ·
[Lab 15 turns this diagnosis into a recovery decision](lab-15-change-recovery.md)
