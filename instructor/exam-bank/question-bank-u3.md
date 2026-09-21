# Question Bank — Unit U3: Planning the Work (L09–L14)

> **INSTRUCTOR ONLY — not published to the site.**
> This unit carries the course's quantitative core: every numerical item is
> fully worked and machine-verified. Bloom ladder: recall → computation →
> diagnosis → defense. Tag legend as in QB-U1. Formulas taught at L10
> (PERT: TE = (O+4M+P)/6; σ = (P−O)/6) and L11 (forward/backward pass).
> The L13 budget/quality formulas follow CS-17's convention (reserve on top
> of baseline), which is the version students are taught.

## MCQ items

### QB-U3-01 [L09 · CLO2 · Remember · F · MCQ] (1 mark)
The 100% rule of WBS decomposition states that:
A. Every package must fit one reporting period
B. Children must sum to 100% of the parent's scope (and effort)
C. The WBS must cover 100% of the organization
D. 100% of packages need dictionary entries

**Answer: B.**

### QB-U3-02 [L09 · CLO2 · Understand · F · MCQ] (1 mark)
A WBS decomposes work by **deliverable**, not by:
A. Phase
B. Organizational chart
C. Cost category
D. All of the above

**Answer: D.** (Org-chart WBS and phase WBS both hide scope.)

### QB-U3-03 [L10 · CLO2 · Apply · I · MCQ] (1 mark)
In PERT, a three-point estimate's expected value weights the most likely by:
A. 1/6
B. 1/3
C. 1/2
D. 4/6

**Answer: D.**

### QB-U3-04 [L11 · CLO2 · Apply · I · MCQ] (1 mark)
An activity's **free float** can exceed zero only if:
A. It is on the critical path
B. Its successor's earliest start is later than its earliest finish
C. It has no predecessors
D. The project ends early

**Answer: B.**

### QB-U3-05 [L12 · CLO2 · Understand · F · MCQ] (1 mark)
Resource levelling that extends the project end date is called:
A. Fast tracking
B. Time-constrained levelling
C. Resource-constrained levelling
D. Crashing

**Answer: C.** (Time-constrained levelling stays within float.)

### QB-U3-06 [L13 · CLO3 · Remember · F · MCQ] (1 mark)
Contingency reserve is distinguished from management reserve because it:
A. Is sponsor-controlled and covers unknown-unknowns
B. Is PM-controlled and covers identified known-unknowns
C. Sits outside the cost baseline
D. Requires CCB approval to spend

**Answer: B.** (A and D describe management reserve.)

### QB-U3-07 [L14 · CLO3 · Understand · I · MCQ] (1 mark)
Cost of quality's **appraisal costs** include:
A. Rework and scrap
B. Testing and inspection
C. Warranty claims
D. Training

**Answer: B.** (A/C are failure costs; D is prevention.)

### QB-U3-08 [L14 · CLO3 · Apply · I · MCQ] (1 mark)
For a data project, a data-quality rule such as "lab results must parse as
ISO 8601 timestamps" belongs to which rule class?
A. Validity
B. Completeness
C. Consistency
D. Uniqueness

**Answer: A.** (Format/regex conformance = validity; consistency would be
cross-field agreement.)

## Computation items (fully worked, machine-verified)

### QB-U3-09 [L09 · CLO2 · Apply · I · numeric] (6 marks)
**Case anchor: CS-12.** A deliverable has three packages: workflow 160 h,
notifications 60 h, admin-tools 50 h. A second, older estimate for workflow
says 140 h. Project roll-up must satisfy the 100% rule.

a) Which estimate enters the WBS if the rule is "newest estimate wins"? (1)
b) Compute the deliverable's roll-up. (2)
c) A colleague proposes adding a "project management" package under this
   deliverable. Why does the 100% rule reject *hiding* PM hours inside it,
   and where do PM hours belong? (3)

**Answers:** a) 160 h (newest). b) 160+60+50 = **270 h**. c) The 100% rule
makes the WBS an additive scope contract — embedding PM hours in a
deliverable double-counts them across deliverables and corrupts roll-ups;
PM effort belongs in a project-level element (e.g., WBS 1.x PM) so it is
counted exactly once. Award: rule-consequence (2), placement (1).

### QB-U3-10 [L10 · CLO2 · Apply · I · numeric] (6 marks)
An ML feature-extraction task has O = 2 days, M = 4 days, P = 12 days.

a) PERT expected value. (2)
b) Standard deviation. (2)
c) The team currently estimates at M = 4 only. State the systematic bias
   this introduces and the correction the course recommends. (2)

**Answers:** a) TE = (2 + 16 + 12)/6 = **30/6 = 5.0 days**. b) σ = (12−2)/6 =
**1.67 days**. c) M-only estimation ignores the right tail; historical
calibration (QB analog: CS-14's bias ratio) shows actuals exceed M — apply a
calibration factor from past estimate-vs-actual data and keep ranges, not
point values.

### QB-U3-11 [L11 · CLO2 · Apply · I · numeric] (8 marks)
**Case anchor: CS-15.** Activities: A(3) → B(5) → D(6) → G(4) → I(2) → K(4)
→ M(3) → N(1); C(2) after A; E(4) after B; F(3) after C; H(5) after E and F;
J(3) after H; L(2) after K; N after L and M.

a) Compute ES/EF for K. (2)
b) Compute the project duration. (3)
c) State total float of E and interpret it in one sentence. (3)

**Answers (machine-verified, tools/check_cases.py):**
a) ES(K) = max(EF(I), EF(J)) = max(20, 20) = **20**; EF(K) = 24.
b) **28 weeks** — two jointly critical routes (…K–L–N and …K–M–N) plus a
third via E–H–J; accept duration from a correct pass.
c) TF(E) = **0** — E is on a critical route; zero slip available before the
project end moves.

### QB-U3-12 [L11 · CLO2 · Analyze · A · numeric] (6 marks)
**Case anchor: CS-46.** Crashing data: A slope 15k/wk (1 wk available),
B slope 15k/wk (1 wk available), C slope 20k/wk, D slope 20k/wk. Critical
path A–B–D = 13 wk; target 11 wk; indirects 8k/wk.

a) Cheapest two-week crash plan and its direct cost. (3)
b) Net cost after indirect savings. (2)
c) Why must the plan check a second near-critical path before committing? (1)

**Answers:** a) Crash A and B one week each: 15k + 15k = **30k**. b) Savings
16k − 30k = **net +14k cost**; the crash buys time, not money. c) Compressing
one path can promote a parallel path to critical, so the second week of
crashing may require crashing two activities — plan cost doubles.

### QB-U3-13 [L12 · CLO2 · Analyze · A · case] (6 marks)
**Case anchor: CS-16.** Two activities compete for one database specialist;
one holds 4 days of float, the other is critical. Level the conflict.

**Marking criteria:** move floated activity into its float window (2);
explicitly state the float consumed and the new zero-float exposure (2);
name when a second specialist beats levelling (float nearly exhausted
elsewhere / context-switching cost) (2). End date unchanged is required.

### QB-U3-14 [L13 · CLO3 · Apply · I · numeric] (8 marks)
**Case anchor: CS-17.** Labor: Data engineer 420 h × 2,600; Backend 300 h ×
2,400; QA 160 h × 1,800 (PKR). Indirects 25% of labor; direct costs 180,000;
contingency 10% of subtotal; management reserve 5% on top of the baseline;
funding cap 3,000,000.

a) Labor total. (2)
b) Contingency amount and cost baseline. (3)
c) Headroom against the cap after reserve. (2)
d) Who releases the management reserve and why is it outside the baseline? (1)

**Answers (machine-verified):** a) 1,092,000 + 720,000 + 288,000 =
**2,100,000**. b) Subtotal = 2,100,000×1.25 + 180,000 = **2,805,000**;
contingency = **280,500**; baseline = **3,085,500**. c) Reserve = 154,275;
total 3,239,775; headroom = **−239,775** (cap breached — descope or
renegotiate). d) Sponsor/management — unknown-unknowns are governance risk,
not plan risk; releasing it changes the baseline itself.

### QB-U3-15 [L13 · CLO3 · Analyze · A · case] (6 marks)
**Case anchor: CS-73.** Contingency is 45% drawn at 60% schedule progress.
Diagnose the two readings a reviewer must distinguish before alarming the
sponsor.

**Marking criteria:** rate-vs-pattern reading — proportional draw with
schedule can be healthy; front-loaded draw signals mis-estimation or
unrecorded scope changes (3); recommendation depends on which pattern the
draw-log shows, plus where the reserve sits vs remaining risk exposure (3).

### QB-U3-16 [L14 · CLO3 · Apply · I · short] (5 marks)
A hospital analytics pipeline defines four data-quality rules. Classify each:
(1) every admission has a patient_id; (2) discharge date ≥ admission date;
(3) lab codes match the reference table; (4) no duplicate episode rows.

**Answer:** 1 completeness; 2 consistency; 3 validity; 4 uniqueness.
1¼ marks each (round to nearest half-mark; 5 total).

### QB-U3-17 [L14 · CLO3 · Evaluate · A · case] (6 marks)
**Case anchor: CS-18.** A dashboard proposes these quality metrics: lines of
code, test pass rate, defect count, escaped defects per release. Select the
two you would keep and justify; name the failure mode of each rejected one.

**Marking criteria:** keep escaped defects (outcome-linked) and defect count
(with coverage caveat) or test pass rate **only with** coverage context (3);
rejections name real failure modes — LOC rewards verbosity; test pass rate
without coverage measures the tests, not the quality (3). Provenance of
targets expected for full marks.

### QB-U3-18 [L09 · CLO2 · Evaluate · A · case] (6 marks)
**Case anchor: CS-13.** From a change log, identify which entries are scope
creep versus legitimate change, and state the governance step each requires.

**Marking criteria:** creep = undocumented/unapproved additions accepted
socially; legitimate change = documented, impact-assessed, CCB-approved (3);
required steps — refuse-and-log for creep proposals, CR workflow for real
change, re-baseline only via CCB (3).

### QB-U3-19 [L12 · CLO2 · Apply · I · numeric] (4 marks)
A sprint-capacity computation: 5 devs × 10 days × 8 h = 400 nominal; focus
factor 0.7; 20 h support duty; 14 h per story point.

a) Effective focused hours. (2)
b) Point capacity to one decimal. (2)

**Answers (machine-verified, CS-28 chain):** a) 400×0.7 − 20 = **260 h**.
b) 260/14 = **18.6 points**.

### QB-U3-20 [L13 · CLO3 · Analyze · A · numeric] (6 marks)
**Case anchor: CS-57.** Cloud project: BAC 1,800,000; actuals to date
1,650,000 at month 4 of 6; planned to date 1,200,000; a fix recovers 120,000
per month from month 5.

a) Variance to plan and overrun percentage. (2)
b) EAC at current monthly rate. (2)
c) EAC with the fix. (2)

**Answers (machine-verified):** a) +450,000; **37.5%** over plan. b) Rate =
412,500/mo → EAC = 1,650,000 + 2×412,500 = **2,475,000** (VAC −675,000).
c) Fixed rate 292,500 → EAC = 1,650,000 + 585,000 = **2,235,000** (VAC
−435,000).

## Quiz-extraction note

Quiz 2 (L12) draws: QB-U3-03/04/05 MCQs + QB-U3-11 network problem
(renumbered) + one short from QB-U3-01/02. Version B uses QB-U3-19's
capacity chain as the computational item instead.
