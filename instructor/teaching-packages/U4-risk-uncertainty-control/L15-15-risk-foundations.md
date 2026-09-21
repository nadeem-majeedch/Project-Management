# Lecture 15 — Risk Management Foundations (ISO 31000 Alignment)

> **Package for:** L15 · Week 8 · Unit U4 · CLO4 · Bloom: Analyze
> **Case anchors:** CS-20 (twenty risks), CS-21 (heat-map thresholds)
> Companion: [`L15` skeleton](../../../docs/lectures/L15-15-risk-foundations.md) · [CS-20](../../../docs/cases/CS-20.md) · [CS-21](../../../docs/cases/CS-21.md)

## Learning objectives

1. Structure risk management per ISO 31000 (scope/context/criteria → assessment → treatment → monitoring).
2. Write normalized cause-risk-effect risk statements (≥ 18 for a given scenario).
3. Score risks on a 5×5 probability × impact scale and defend scale thresholds.
4. Assess risk-data quality and adjust scores when sources conflict.

## Required prior knowledge

- L06 assumptions (charters produce risks); L14 (a failed gate is a risk).
- L15 opens the Risk unit — the course's analytic core alongside L11.

## Teaching notes

Risk teaching usually dies in heat-map coloring. Ground it in **decisions**:
the register exists to drive *responses* (L17) and *contingency sizing*
(L16/L13). Two disciplines get drilled today: **normalization** (a risk
statement names cause → uncertain event → effect; "data quality is a risk" is
not a risk) and **scale honesty** (5×5 scores are arguments about evidence —
the thresholds defend or bury the whole analysis).

ISO 31000 gives the process skeleton; teach it as a loop, not a ceremony:
establish context → assess (identify/analyze/evaluate) → treat → monitor, with
communication throughout. The vocabulary pays off in L16 (quantify the top
risks) and L17 (respond to them) — today only builds the *foundations*.

DS emphasis: data projects carry risk families CS projects barely have — data
availability (access approved? in time?), label quality, drift, privacy
processing, model misuse. Seed CS-20's list so at least six of twenty are
data-family risks.

## Definitions & concepts

- **Individual vs overall project risk** — a single uncertain event vs the
  total uncertainty exposure of outcomes (distributions vs items).
- **Threat / opportunity** — uncertain events that hurt / help objectives;
  opportunities get equal process respect (CS-66 deepens).
- **Cause-risk-effect statement** — "Because ⟨cause⟩, ⟨uncertain event⟩ may
  occur, resulting in ⟨effect on objective⟩."
- **5×5 scoring** — probability (1 rare … 5 near-certain) × impact (1 minor …
  5 severe) on named objectives (schedule/cost/quality separately or a
  declared composite); thresholds define the heat map's colors.
- **Risk data quality** — the reliability of the P&I inputs themselves
  (source, age, agreement) — CS-63's homework case.
- **Issue vs risk** — occurred vs uncertain; issues go to the issue log, not
  the register.

## Practical examples

**CS (GRIDSENSE-adjacent):** "Because the vendor's connector API rate-limits
bulk pulls (cause), ingestion may fall behind the 4-hour freshness window
(event), delaying every downstream alert SLA (effect)." — normalized. The
un-normalized version everyone writes first: "API risk."

**DS (TelcoCare):** "Because label sources span two billing eras (cause),
churn labels may be inconsistent for accounts migrated mid-period (event),
biasing the model against migrated customers (effect: fairness + revenue)."
Also: privacy processing risk (record-level access request pending — the
CS-100 collision in seed), drift risk (segment migration changes the
population).

## Worked example

**Full P×I scoring on a register slice (board):**

Scale: P (1 <10% … 5 >70% in project horizon); I (1 <5% budget/1 wk … 5
failure of objective). Declared composite = max of schedule/cost impacts.

| # | Cause–event–effect (short) | P | I (S/C/Q) | Score | Band |
|---|---|---|---|---|---|
| R1 | Vendor rate-limit → ingestion misses freshness SLA | 3 | 4 (S4/C2/Q3) | 12 | High |
| R2 | Key DS resignation mid-discovery | 2 | 4 (S5/C3/Q2) | 8 | Medium |
| R3 | Label eras inconsistent → biased model | 3 | 5 (Q5) | 15 | Critical |
| R4 | GPU price +25% over plan | 2 | 2 (C2) | 4 | Low |
| R5 | Governance gate demands extra evidence | 4 | 3 (S3) | 12 | High |

Walk the discipline: R1 vs R5 both score 12 but have *different* responses
(mitigate vs prepare evidence) — score drives attention; **response choice
needs the cause** (L17's job). Threshold defense: why is 12 "high"? Because at
12 the response must be funded *now* vs watched — the band ↔ action table is
the deliverable, not the colors. Data-quality note: R3's P=3 comes from a
documented era-boundary audit (source cited); R2's P=2 is team lore —
weakest input, marked for interview evidence.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Risk = bad things; register = complaint list." | Risks are *uncertain events affecting objectives* — including opportunities; statements must be normalized to be actionable. |
| "High score = worst risk, always." | Scores drive attention; response design needs cause + owner + trigger. Two 12s can deserve opposite treatments. |
| "The heat map is the analysis." | It is a communication view; thresholds and data quality are where the rigor lives. |
| "Known issues belong in the register." | Occurred events are issues (management now); risks are uncertain (response now). |
| "Data risks are technical details." | Availability, privacy, drift risks are project-level exposures with sponsor-visible effects. |

## Classroom activities

1. **CS-20 identification sprint (35 min):** 20 normalized risks across
   technical/vendor/people/data families; teams swap and critique two
   statements each for cause-effect completeness.
2. **CS-21 heat-map trial (25 min):** place 12 scored risks; then the
   threshold defense: each team writes the band→action table justifying their
   color cut-offs.
3. **Normalize the lazy (10 min):** ten real-world one-word "risks" ("scope",
   "vendor", "AI", "security"...) rewritten as statements under time pressure.

## Discussion questions

1. Which band→action threshold in your table is most vulnerable to challenge — by whom, and with what evidence?
2. Name an *opportunity* for your capstone with the same P×I discipline. What would "exploit" (L17) look like?
3. Where does your risk-data quality come from — audits, interviews, folklore? What upgrade is affordable this semester?

## Practical exercise

**In class:** CS-20 + CS-21 deliverables. **Take home (feeds A3):** identify
≥ 18 normalized risks for your A2 project (≥ 2 opportunities, ≥ 2 data-family
if applicable), score on the declared 5×5 with a threshold table. A3's brief
releases after L17 (register + responses); today's output is its first half.

## Formative assessment (exit ticket)

1. Rewrite as a normalized statement: "testing risk."
2. P=4, I=3 — band if thresholds are high ≥ 12? How do you know?
3. Issue vs risk — one sentence.

## Reading & references

- ISO 31000:2018, *Risk management — Guidelines* — process vocabulary
  (required backbone).
- PMI. (2021). *PMBOK Guide* (7th ed.) — Uncertainty domain.
- [Templates](../../../docs/resources/templates.md): risk register skeleton ·
  [Lab 7 brief](../../../docs/labs/index.md).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the risk that was "fine" until it wasn't (a real normalized statement) | — |
| 0:10–0:28 | ISO 31000 loop; vocabulary; normalization doctrine | board |
| 0:28–0:50 | Worked example: 5×5 scoring + thresholds + data quality | board table |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-20 sprint + swap critique | CS-20 brief |
| 1:35–1:55 | CS-21 heat map + threshold defense | CS-21 brief |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Prepare the 12-risk scored list for CS-21 with two deliberately contested
  scores; the threshold defense needs friction.
- A3 release timing confirmed: brief out after L17; mention today so students
  collect candidate risks from L15/L16 sessions.
- Answer-key note: record the normalization failures you see most often
  (they recur in the midterm's risk items).

## Linked resources

- Lecture skeleton: [`docs/lectures/L15`](../../../docs/lectures/L15-15-risk-foundations.md)
- Cases: [CS-20](../../../docs/cases/CS-20.md) · [CS-21](../../../docs/cases/CS-21.md)
- Assignment: [A3 brief](../../../docs/assignments/a2-risk-register.md)
- Forward: [Monte Carlo L16](../../../docs/lectures/L16-16-quant-risk-simulation.md) ·
  [responses L17](../../../docs/lectures/L17-17-risk-response.md) ·
  [privacy collision CS-100 (homework lane)](../../../docs/cases/index.md).
