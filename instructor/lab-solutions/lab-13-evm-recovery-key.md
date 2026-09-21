# Lab 13 Answer Key — EVM & Recovery Diagnosis

## Reference computation (checker-verified against `data/campus-mend-evm-answers.csv`)

Given: PV = 2,026,000 · EV = 1,762,000 · AC = 2,041,000 · BAC = 4,532,000.

| Metric | Computation | Value |
|---|---|---|
| CV | 1,762,000 − 2,041,000 | **−279,000** |
| SV | 1,762,000 − 2,026,000 | **−264,000** |
| CPI | 1,762,000 / 2,041,000 | **0.8633** |
| SPI | 1,762,000 / 2,026,000 | **0.8697** |
| EAC₁ | 4,532,000 / CPI (unrounded) | **≈ 5,249,611** |
| EAC₂ | 2,041,000 + (4,532,000 − 1,762,000) | **4,811,000** |
| ETC₁ | 5,249,611 − 2,041,000 | **≈ 3,208,611** |
| TCPI | (4,532,000 − 1,762,000) / (4,532,000 − 2,041,000) | **1.1118** |

*(If students' corrected-EV CPI rounds differently, accept any consistent
arithmetic; the checkpoints above are the audit-verified-EV reading.)*

## EAC variant selection (model)

Physical evidence: E's claim inflated (55% claimed, 40% verified), F hides an
open integration ticket → inefficiency is *embedded*, not one-off. EAC₂'s
"it won't happen again" assumption is the denial variant. **Defensible
choice: EAC₁ (5.25M), refined by the corrected-EV computation in step 4.**
A student choosing EAC₂ must show why the embedded-inefficiency reading is
wrong — rare and hard.

## Measurement audit (model)

- E: claimed 55% vs QA ticket-sampling verified 40% → EV credit corrected
  from 55% to 40% of E's budget.
- F: "complete" per team, but dictionary criterion (integration ticket
  closed) unmet → F at 50/50 means credit only if start-evidence exists;
  finish credit withheld → F at 50%.
- Re-derived EV (model): 1,762,000 − 0.15 × E-budget − 0.5 × F-budget-credit
  ≈ 1,640,000 (students state their F assumption explicitly; accept a range
  with shown arithmetic) → corrected CPI ≈ 0.803, corrected EAC₁ ≈ 5.64M.
  **The claims were costing ≈ 400k of false comfort.**

## Diagnosis (model structure, ≤ 1 page)

1. **Indices say:** both dimensions adverse, moderate (CPI/SPI ≈ 0.86–0.87);
   EAC₁ ≈ +718k over baseline; TCPI 1.11.
2. **Indices hide:** (a) the 55% myth — EV inflated by stale claims;
   (b) F's open ticket — SV overstates *both* plan and delivery honesty;
   (c) SPI says 13% behind at the *value* level; with C, D complete and E
   mid-flight, the critical path's remaining float is zero, so calendar
   slippage is likely worse than SPI implies.
3. **TCPI credibility:** sustaining 1.11 after running at 0.863 is a ~29%
   efficiency jump — historically implausible without structural change;
   conclude: BAC is not recoverable by hustle → choose scope/date options
   (Lab 15's job).
4. **Recommendation:** adopt EAC₁ as the working forecast, fix the EV rules
   (E audit cadence, F ticket evidence), and take the recovery decision to
   CCB with options priced.

## Common wrong answers

| Error | Correction |
|---|---|
| Indices computed from claimed (not corrected) EV and presented as clean | the audit comes *before* the diagnosis; otherwise you diagnose fiction |
| EAC₂ chosen "to be optimistic" | variants encode assumptions; optimism is not one |
| TCPI 1.11 accepted as fine | > 1.10 triggers the credibility test; a 0.863 team at 1.11 needs structural change |
| "SPI 0.87 = we finish 13% late" | SPI is value-rate, not calendar; with zero path float the calendar risk is worse |
| Rounding CPI to 0.86 everywhere then compounding | carry 4 decimals through forecasts; drift compounds |

## Reflection guidance

1. Reported → corrected CPI swing ≈ 0.863 → 0.803: ≈ 400k of false comfort —
   EV-rule design (Lab 5) is the control; percent-complete rules created it.
2. SPI misreads here because the 48-h rule fixes the calendar: the honest
   statement is "value pace is 87% of plan; the remaining path has zero
   float; the SLA is at risk unless recovery adds capacity or cuts scope."
3. Refusing BAC leaves: re-baseline (new ask with justification) or
   scope-cut to a fundable+deliverable core — both are Lab 15 options.

## Preparation notes

The corrected-EV step is the discriminator between computing and diagnosing;
push students past formula recall. Collect dashboards (Views 1–2) — Lab 15
opens with them. Assignment A4 is the graded, individual version of this lab.
