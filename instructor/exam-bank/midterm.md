# Midterm Examination — PM-401 (L01–L20)

> **INSTRUCTOR ONLY — not published to the site.**
> 90 minutes · 40 marks · 20% of course grade (A5) · CLO1–CLO4.
> **Pass rule: ≥ 40% (16/40) required to pass the course** (grading page).
> All numeric chains below are machine-verified (tools/check_cases.py);
> IDs reference the question bank and published case briefs. Formula sheet:
> a one-page sheet with PERT, forward/backward pass definitions, the EVM
> indicator table, and the budget build-up is supplied with the paper —
> students are tested on application, not recall of constants.

## Section A — Concepts (6 × 1 mark; CLO1, Bloom Remember/Understand)

1. A temporary endeavor with a unique output is a: (A) program · (B) project
   · (C) operation · (D) portfolio
2. PMBOK 7's structure: (A) 49 processes · (B) 12 principles, 8 domains ·
   (C) 10 knowledge areas · (D) 4 maturity levels
3. The charter formally gives the PM: (A) technical authority · (B) authority
   to apply organizational resources · (C) budget ownership · (D) HR rights
4. A stakeholder with high power and low interest is: (A) monitored ·
   (B) kept satisfied · (C) managed closely · (D) ignored
5. Total float is: (A) LS − ES · (B) EF − ES · (C) LF − EF at completion ·
   (D) project end − EF, always
6. CPI < 1 means: (A) ahead of schedule · (B) over cost — value per rupee
   below 1 · (C) under budget · (D) scope creep

**Key:** 1 B · 2 B · 3 B · 4 B · 5 A · 6 B.

## Section B — Planning mathematics (16 marks; CLO2, CLO3; Apply)

### Q7 — Network and critical path (10 marks) *[QB-U3-11 / CS-15 network]*

Activities (weeks, FS with zero lag):
A(3) · B(5, after A) · C(2, after A) · D(6, after B) · E(4, after B) ·
F(3, after C) · G(4, after D) · H(5, after E and F) · I(2, after G) ·
J(3, after H) · K(4, after I and J) · L(2, after K) · M(3, after K) ·
N(1, after L and M)

a) Forward pass: EF of H, I, and J. **(3)**
b) ES and EF of K. **(2)**
c) Project duration. **(2)**
d) Total float of E and of C. **(2)**
e) Name one zero-float path in full. **(1)**

### Q8 — Bottom-up budget (6 marks) *[QB-U3-14 / CS-17]*

Labor: Data engineer 420 h × 2,600 PKR/h; Backend 300 h × 2,400; QA 160 h ×
1,800. Indirects 25% of labor. Direct costs 180,000 PKR. Contingency 10% of
subtotal. Management reserve 5% on top of the baseline. Funding cap 3,000,000.

a) Labor total. **(1)**
b) Subtotal (labor + indirects + direct). **(1)**
c) Contingency and cost baseline. **(2)**
d) Total with reserve, and headroom vs the cap. **(2)**

## Section C — Control (10 marks; CLO3, CLO4; Analyze)

### Q9 — EVM diagnosis (10 marks) *[QB-U4-13 / CS-26]*

Status at month 5 of 10: BAC 4,000,000 PKR; PV 2,000,000; EV 1,700,000;
AC 1,900,000.

a) CV and SV, in rupees. **(2)**
b) CPI and SPI, to 3 dp. **(2)**
c) EAC₁ (cost inefficiency continues). **(2)**
d) EAC₂ (the overrun was one-off). **(2)**
e) TCPI (against BAC) and one sentence on its credibility. **(2)**

## Section D — Judgment under published constraints (8 marks; CLO4; Evaluate)

### Q10 — Resource levelling (4 marks) *[CS-16]*

Two activities need the same database specialist in the same fortnight;
one has 4 days of float, the other is critical. Level the conflict without
extending the end date: state the move, what it consumes, and the new
exposure. **(4)**

### Q11 — Risk prioritization (4 marks) *[CS-21 values]*

Risk register extract (probabilities × money impact): R1 p 0.3, 1,200,000;
R2 p 0.4, 2,500,000; R5 p 0.05, 2,000,000. A sponsor proposes funding the
response for R5 because "a 2M hit would be devastating."

a) Compute each risk's EMV. **(2)**
b) Advise the sponsor with the exposure-ordering argument. **(2)**

---

# Answer key and marking guide

## Q7 (machine-verified — identical chain to CS-15 in tools/check_cases.py)

| Part | Answer | Marks |
|---|---|---|
| a | EF(H) = 8+5 = **13**… forward pass: EF(I) = 14+4+2 = **20**; EF(J) = EF(H)+3 = **20**; EF(H) = max(EF E 12, EF F 8) + 5 = **17** | 3 (1 each) |
| b | ES(K) = max(EF I, EF J) = **20**; EF(K) = **24** | 2 |
| c | Duration = **28 weeks** (two jointly critical routes K–L–N and K–M–N; a third via E–H–J) | 2 |
| d | TF(E) = **0** (E sits on a zero-float route via H–J–K); TF(C) = **4** | 2 (1 each) |
| e | e.g. A–B–D–G–I–K–M–N (or …L–N, or the E–H–J route) | 1 |

**Method marks:** full-credit forward pass requires showing EF computations,
not answers. Arithmetic slips with correct method: −1 per occurrence capped
at −3. Method failure on the backward logic: cap Section B at 6/10.
**Version B:** swap durations of E and F and re-verify (use the checker's
ev_cpm before printing — never hand-adjust a network).

## Q8 (machine-verified — CS-17 chain)

| Part | Answer | Marks |
|---|---|---|
| a | 420×2,600 + 300×2,400 + 160×1,800 = **2,100,000** | 1 |
| b | 2,100,000×1.25 = 2,625,000 + 180,000 = **2,805,000** | 1 |
| c | Contingency **280,500**; baseline **3,085,500** | 2 |
| d | Reserve 154,275 → total **3,239,775**; headroom **−239,775** — the cap is breached: descope or renegotiate | 2 |

The cap breach is the point: full marks on (d) require stating the
consequence, not just the negative number.

## Q9 (machine-verified — CS-26 chain)

| Part | Answer | Marks |
|---|---|---|
| a | CV = 1,700,000−1,900,000 = **−200,000**; SV = 1,700,000−2,000,000 = **−300,000** | 2 |
| b | CPI = **0.895**; SPI = **0.85** | 2 |
| c | EAC₁ = 4,000,000/0.8947 = **4,470,588** | 2 |
| d | EAC₂ = 1,900,000 + 2,300,000 = **4,200,000** | 2 |
| e | TCPI = 2,300,000/2,100,000 = **1.095**; credible only with a named, evidenced recovery — otherwise the forecast is hope | 2 |

Accept EAC range ±5,000 for rounding conventions taught at L19.

## Q10 (marking criteria — CS-16 key)

Move the floated activity into its 4-day float window (2); float consumed →
moved activity now has zero float, any further slip makes it critical (1);
hiring/loaning a second specialist when float is nearly exhausted elsewhere
or context-switching cost is high (1). End date unchanged is a precondition,
not a scoring item.

## Q11 (machine-verified — CS-21 chain)

| Part | Answer | Marks |
|---|---|---|
| a | EMV: R1 **360,000**; R2 **1,000,000**; R5 **100,000** | 2 |
| b | Fund R2 first — 10× R5's exposure; the sponsor's impact-anchoring ignores probability; severity and exposure are different orderings | 2 |

## Administration

- **Bloom ladder within the paper:** A recall/understand (6) → B apply (16)
  → C analyze (10) → D evaluate (8).
- **Pass-rule handling:** scripts below 16/40 are flagged to the instructor
  for the pass-rule review recorded on the grading page.
- **Timing guidance (per section on the board):** A 10 min · B 40 · C 20 ·
  D 15 · review 5.
- **Formula sheet contents:** PERT (TE, σ), CPM definitions (EF, ES, LF, LS,
  TF = LS−ES, FF), EVM table (PV/EV/AC, CV/SV, CPI/SPI, 4 EAC variants,
  TCPI), budget build-up order (labor → indirects → direct → subtotal →
  contingency → baseline → reserve).
- **Integrity:** single seating; the network and budget numbers are unique to
  this paper — versions B differs numerically, not structurally.
