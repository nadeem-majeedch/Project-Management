# Question Bank — Unit U4: Risk, Uncertainty & Control (L15–L20)

> **INSTRUCTOR ONLY — not published to the site.**
> Quantitative core of the second half: P×I/EMV (L15–16), full EVM set
> (L19 — CV/SV/CPI/SPI, four EAC variants, TCPI), monitoring signals (L20).
> Tag legend as in QB-U1. EVM formulas as taught at L19.

## MCQ items

### QB-U4-01 [L15 · CLO4 · Remember · F · MCQ] (1 mark)
A risk is best defined as:
A. Any problem that has occurred
B. An uncertain event that, if it occurs, affects objectives
C. A cost overrun already booked
D. A defect found in testing

**Answer: B.** (A/C/D are issues/realized risks.)

### QB-U4-02 [L15 · CLO4 · Understand · F · MCQ] (1 mark)
In a normalized risk statement "cause → risk → effect," the risk element is:
A. The root cause
B. The uncertain event itself
C. The impact on objectives
D. The response plan

**Answer: B.**

### QB-U4-03 [L16 · CLO4 · Apply · I · MCQ] (1 mark)
Expected monetary value (EMV) of a risk equals:
A. Impact × detectability
B. Probability × impact
C. Impact − mitigation cost
D. Probability + severity

**Answer: B.** (A is the detection-ratio trap; C is mitigation ROI logic.)

### QB-U4-04 [L17 · CLO4 · Apply · I · MCQ] (1 mark)
Buying insurance against a data-breach fine is which response strategy?
A. Avoid
B. Mitigate
C. Transfer
D. Accept

**Answer: C.**

### QB-U4-05 [L18 · CLO4 · Understand · F · MCQ] (1 mark)
The point of total assumption (POTA) in an FPIF contract is the cost at which:
A. The buyer cancels the contract
B. The seller absorbs all further overrun
C. The fee reaches its maximum
D. The buyer pays the target price

**Answer: B.**

### QB-U4-06 [L19 · CLO4 · Remember · F · MCQ] (1 mark)
Earned value (EV) is:
A. Budgeted cost of work scheduled
B. Budgeted value of work actually performed
C. Actual cost of work performed
D. Total budget at completion

**Answer: B.** (A = PV, C = AC, D = BAC.)

### QB-U4-07 [L19 · CLO4 · Apply · I · MCQ] (1 mark)
CPI = 0.85 means:
A. The project is 15% ahead of schedule
B. Every rupee spent earns 0.85 rupees of value
C. The budget was cut 15%
D. 15% of scope is done

**Answer: B.**

### QB-U4-08 [L20 · CLO4 · Analyze · A · MCQ] (1 mark)
SPI = 1.0 while CPI = 0.8 most likely indicates:
A. Schedule pressure consuming money (e.g., overtime, expediting)
B. Perfect schedule performance
C. Underestimated durations
D. Gold plating

**Answer: A.** (Buying schedule with money — a classic diagnosis pattern.)

## Computation items (fully worked, machine-verified)

### QB-U4-09 [L15 · CLO4 · Apply · I · numeric] (6 marks)
**Case anchor: CS-21.** Risks: R1 P×I 3×4 prob 0.30 money 1,200,000;
R2 4×4 prob 0.40 money 2,500,000; R5 1×5 prob 0.05 money 2,000,000.
Bands: low ≤ 6, medium ≤ 12, high > 12.

a) Score and band each risk. (3)
b) EMV of each. (2)
c) Which risk ranks first by score but not by EMV — and what does the gap teach? (1)

**Answers (machine-verified):** a) R1 12 medium; R2 16 high; R5 5 low.
b) R1 360,000; R2 1,000,000; R5 100,000. c) Same ranking here — accept
any risk where score and EMV orders diverge with the lesson: ordinal P×I
hides magnitude; EMV re-ranks by exposure, so funding decisions must use
EMV, not heat-map color.

### QB-U4-10 [L16 · CLO4 · Analyze · A · numeric] (6 marks)
**Case anchor: CS-22.** Monte Carlo histogram (10,000 trials, deadline 16 wk):
14 wk ×1,200; 15 ×2,300; 16 ×2,900; 17 ×2,100; 18 ×1,000; 19 ×400; 20 ×100.

a) P(on-time). (2)
b) Median and P70 completion brackets. (2)
c) Mean overrun if late (late trials only), to 2 dp. (2)

**Answers (machine-verified):** a) 6,400/10,000 = **64%**. b) Median **16 wk**
(cumulative 6,400 ≥ 5,000 at 16); P70 also **17 wk** (cumulative 8,500 ≥ 7,000
at 17). c) Late trials 3,600; weighted overrun 5,700 → **1.58 wk**.

### QB-U4-11 [L16 · CLO4 · Evaluate · A · numeric] (6 marks)
**Case anchor: CS-63.** Custom build: cost 400k, success p = 0.6, benefit
1,200k on success, 0 otherwise. Vendor: certain 700k benefit, cost 300k.
A perfect PoC costs 80k.

a) EMV of each option without information. (2)
b) EV with perfect information, gross of PoC cost. (2)
c) EVPI and the decision. (2)

**Answers (machine-verified):** a) Custom **320k** (0.6×1,200k − 400k);
vendor **400k** — vendor wins now. b) 0.6×800k + 0.4×400k = **640k**.
c) EVPI = 240k > PoC 80k → **buy the PoC**; net value after PoC 560k vs 400k.
The PoC's worth lives entirely in the 40% failure branch.

### QB-U4-12 [L18 · CLO4 · Apply · I · numeric] (8 marks)
**Case anchor: CS-24.** FPIF: target cost 800,000; target fee 80,000;
ceiling price 950,000; share 80/20 (buyer/seller).

a) Target price and POTA. (3)
b) Fee and price at actual cost 1,200,000. (3)
c) One behavioral consequence for the seller above POTA. (2)

**Answers:** a) Target price = **880,000**; POTA = 800,000 + (950,000 −
880,000)/0.8 = **887,500** (buyer's share in the denominator — the exam
trap). b) 1,200,000 > POTA → price capped at **950,000**; fee = price −
cost = **−250,000**. c) Cost-control incentive collapses past POTA —
sellers stop investing and re-price the tail into future targets.

### QB-U4-13 [L19 · CLO4 · Apply · I · numeric] (8 marks)
**Case anchor: CS-26.** BAC 4,000,000; PV 2,000,000; EV 1,700,000; AC
1,900,000. Compute the full indicator set and both EAC models, with TCPI.

a) CV, SV. (2)
b) CPI, SPI. (2)
c) EAC₁ (typical) and EAC₂ (atypical). (2)
d) TCPI based on BAC and its credibility reading. (2)

**Answers (machine-verified):** a) CV = **−200,000**; SV = **−300,000**.
b) CPI = **0.895** (0.8947); SPI = **0.85**. c) EAC₁ = 4,000,000/0.8947 =
**4,470,588**; EAC₂ = 1,900,000 + (4,000,000 − 1,700,000) = **4,200,000**.
d) TCPI = (4,000,000 − 1,700,000)/(4,000,000 − 1,900,000) = 2,300,000/
2,100,000 = **1.095** — the remaining work must run ~10% more efficient than
all work to date; below ~1.10 is credible, ≥1.20 is fantasy (L19 threshold).

### QB-U4-14 [L19 · CLO4 · Analyze · A · numeric] (6 marks)
**Case anchor: CS-61.** BAC 5,000,000; EV 2,600,000; AC 3,000,000; PV
2,900,000.

a) CPI and TCPI(BAC). (2)
b) TCPI against EAC₁ instead of BAC. (2)
c) Interpret the pair for a sponsor who wants to believe the original BAC. (2)

**Answers (machine-verified):** a) CPI = 0.8667; TCPI(BAC) = 2,400,000/
2,000,000 = **1.20**. b) EAC₁ = 5,769,231; TCPI(EAC) = 2,400,000/2,769,231 =
**0.867** (equals CPI, as the algebra guarantees). c) Against the original
BAC the team must run at 1.20 — above the credibility ceiling; against the
honest forecast it only sustains current performance (0.867). The gap IS the
message: the BAC is no longer the plan.

### QB-U4-15 [L20 · CLO4 · Analyze · A · case] (6 marks)
**Case anchor: CS-82.** Month 8 of 14: BAC 4.0M, EV 1.8M, AC 2.2M, PV 2.2M.
Recovery proposal: descope 300k, assume efficiency 0.95 for remaining work.

a) EAC₁ on the original baseline. (2)
b) Re-based EAC under the proposal. (2)
c) The proposal's forecast rests on one fragile number — name it and the
evidence test. (2)

**Answers (machine-verified):** a) CPI 0.818 → EAC₁ = **4,888,889**.
b) BAC′ = 3.7M; EAC = 2,200,000 + 1,900,000/0.95 = **4,200,000**. c) The
0.95 efficiency assumption — worth ~323k of forecast. Evidence test: the last
three completed packages' realized efficiency, the *named* cause of the 0.818
and whether it is fixed, and what changes in month 9 that did not in months
5–8 (CS-82 key). Conditional acceptance: re-check at month 10; revert if
realized efficiency < 0.88.

### QB-U4-16 [L17 · CLO4 · Evaluate · A · case] (6 marks)
**Case anchor: CS-23.** A response plan proposes mitigating sensor drift by
adding a redundant feed. Identify the baseline impact, the secondary risk,
and who owns each.

**Marking criteria:** baseline impact = new scope/cost task → CCB approval
not quiet absorption (2); secondary risk = false alarms/complexity eroding
trust in alerts (2); ownership = the response owner owns the secondary risk
entry on the same register (2).

### QB-U4-17 [L15 · CLO4 · Apply · I · short] (4 marks)
Distinguish an issue from a risk, and state which register each enters.

**Answer:** issue = realized, certain (issue log; assign owner and action
now); risk = uncertain, potential (risk register with probability, impact,
response). 2 + 2.

### QB-U4-18 [L18 · CLO4 · Evaluate · A · case] (6 marks)
**Case anchor: CS-79.** Draft the two contractual clauses that make a
proprietary-vendor dependency survivable, and state what each is worth at
the next renewal.

**Marking criteria:** data-egress clause (format, completeness, timeline,
capped cost) — converts dependency into migration option (2); exit/termination
triggers with cure windows — converts dependency into leverage (2); renewal
value: pricing posture and the BATNA they create (2). CS-93's leverage logic
accepted.

### QB-U4-19 [L20 · CLO4 · Understand · F · short] (3 marks)
Name the three baseline signals a weekly control report must carry and what
each answers.

**Answer:** SPI — are we ahead/behind?; CPI — are we efficient?; variance
trend (2–3 periods) — is the situation improving or deteriorating? Accept
buffer burn in place of trend for CCPM answers. 1 each.

### QB-U4-20 [L16 · CLO4 · Analyze · A · case] (6 marks)
**Case anchor: CS-51.** A change order was agreed verbally and the committed
costs were never re-forecast. The overrun surfaces at month 9. Diagnose the
control failure and prescribe the two mechanics that prevent it.

**Marking criteria:** diagnosis — commitment without re-baseline breaks
EVM's premise (EV/AC compare the same scope) and cost management's
contemporaneous-record rule (2); mechanics: written change orders with
cost/schedule impact before commitment (2); committed-cost register reviewed
weekly against AC (2).

## Quiz-extraction note

Quiz 3 (L26) covers U5 per the exam-bank README — this unit feeds the
**midterm** (QB-U4-09/13 as the risk/EVM problems) and the final's case
sections. Version B swaps QB-U4-14 for QB-U4-13 as the EVM item.
