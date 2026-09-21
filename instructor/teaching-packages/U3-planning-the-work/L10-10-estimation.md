# Lecture 10 — Estimation: Size, Effort, Duration

> **Package for:** L10 · Week 5 · Unit U3 · CLO2 · Bloom: Apply
> **Case anchor:** CS-14 (planning-poker calibration)
> Companion: [`L10` skeleton](../../../docs/lectures/L10-10-estimation.md) · [CS-14 brief](../../../docs/cases/CS-14.md)

## Learning objectives

1. Apply analogous, parametric, bottom-up, and three-point estimation appropriately.
2. Compute PERT expected values and standard deviations and explain the weighting.
3. Run planning-poker calibration and connect relative estimates to forecasts.
4. Distinguish estimate, target, and commitment — and defend ranges to authority.

## Required prior knowledge

- L09 WBS (the package list being estimated) and basic statistics
  (mean, variance) from program prerequisites.

## Teaching notes

Estimation teaching fails when it becomes tip-lists. Teach the *shape* of
uncertainty instead: estimates are **distributions, not numbers**; the course's
technical spine (PERT here, Monte Carlo in L16, velocity forecasting in L22)
is one idea applied at three tool levels. Say that out loud — it converts
three lectures into one coherent skill.

The second spine is **behavioral**: padding, anchoring, planning fallacy.
The PERT weighting (O+4M+P)/6 exists to dampen the anchoring effect of the
most extreme value; students should see the formula as *psychology with
arithmetic*, which is also why the distribution's shape matters (PERT assumes
beta-like behavior; the sd formula is a usable approximation, not gospel).

Run planning poker live (CS-14) — the convergence behavior is the lesson:
first-round spreads of 3× are normal, not evidence of incompetence. End on the
estimate/target/commitment distinction; capstone teams will misuse these words
in L27 otherwise.

## Definitions & concepts

- **Analogous** — scale from a similar past project (fast, coarse).
- **Parametric** — quantity × rate (e.g., 12 interfaces × 6 h; DS: 40
  pipelines × historical h/run).
- **Bottom-up** — estimate each work package, aggregate (accurate, slow).
- **Three-point / PERT** — t_E = (O + 4M + P)/6; sd ≈ (P − O)/6; the 4M
  weighting dampens extremes.
- **Story points** — relative size units (complexity + effort + uncertainty);
  velocity = points completed per sprint; forecasts use *ranges* from history.
- **Estimate vs target vs commitment** — most likely outcome vs desired date
  vs promise made. Conflating them is how projects lie to themselves.

## Practical examples

**CS:** registration engine — analogous: "the alumni-portal API took 6 dev-
weeks; this is similar but 1.5× scope"; parametric: 9 interfaces × 6 h;
bottom-up: sum the L09 package estimates (310 h total).

**DS:** feature-store build — parametric: 25 features × 4 h (batch) but
*streaming features break the rate* (3 h → 9 h when the source is
semi-structured) — parametric estimates need domain homogeneity, which is a
data problem more than a math problem. Model training itself is the
example of **non-homogeneous uncertainty**: one experiment ≈ hours of compute
but wildly variable *calendar* time (fail fast vs iterate long) — estimate
experiment *budgets*, not durations (this returns in L23's hypothesis backlogs).

## Worked example

**Full PERT computation (board):**

Work package 1.1.1 Enrollment API (from L09): O = 60 h, M = 80 h, P = 150 h
(the 150 comes from an unprompted "if the auth interface turns hostile…"
by the estimating engineer — write the source down; provenance is part of
the technique).

- t_E = (60 + 4·80 + 150)/6 = (60 + 320 + 150)/6 = 530/6 ≈ **88.3 h**
- sd = (150 − 60)/6 = **15 h**

Package 1.2.2 Rule evaluation service: O = 50, M = 70, P = 110:
t_E = (50 + 280 + 110)/6 = **73.3 h**; sd = 10 h.

Path of just these two (assume serial): E ≈ 161.7 h, sd = √(15² + 10²) =
√325 ≈ 18 h → **≈ 95% range of 161.7 ± 36 ≈ 126–198 h** (±2sd).

Lessons extracted live: (1) the range *is* the estimate; "88 h" alone is a
number wearing a costume; (2) the longest-package sd dominates — a 90-hour
spread swamps a 20-hour one, so precision effort belongs on the riskiest
package; (3) summing O's or P's naively gives 110 vs 260 — both wrong; only
the variance arithmetic is honest (full-path simulation arrives in L16).

**Agile forecast (10 minutes):** a team's last 4 sprints: 18, 21, 17, 20 pts
→ velocity ≈ 19, range ≈ 17–21. Backlog = 105 pts. Forecast: **5 sprints
(105/19) ± the range spread → plan 6 sprints** if the commitment matters.
Never forecast from *one* sprint; never average in the sprint where three
people were sick without saying why.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Give one number; ranges look indecisive." | Single numbers hide the distribution you actually believe; the range is the honest artifact. |
| "Add padding to be safe." | Padding is dishonest variance — untracked, unmanaged, repeated every level (and an ethics trap: CS-99). Manage contingency visibly instead (L13). |
| "Story points convert to hours." | Points are relative team velocity units; the moment you fix a conversion you reintroduce the problems points exist to escape. |
| "Velocity is a productivity target." | Weaponized velocity stops being a forecast input (teams inflate estimates) — the L22/L24 failure mode. |

## Classroom activities

1. **CS-14 planning poker (35 min):** 8 capstone-style items; 3 rounds;
   record first-round spread vs final; teams write what information closed
   each gap (the *conversation* is the product).
2. **PERT clinic (20 min):** each team PERTs three of their own L09 packages;
   identify the package whose sd dominates their project.
3. **Convert-the-boss (10 min):** given "t_E = 88 h", teams draft the two
   sentences they would say to a sponsor demanding "so it's 2 weeks?"

## Discussion questions

1. Where did the P = 150 h for the Enrollment API come from — and should one engineer's fear set your upper bound? What would improve provenance?
2. Your velocity range says 5–6 sprints; the roadmap promises 4. Walk the conversation — estimate, target, commitment.
3. Why do data-experiment estimates resist three-point treatment, and what do you do instead?

## Practical exercise

**In class:** PERT clinic on own packages (bring sd-ranked list to L11 — the
longest package feeds the CPM example). **Take home (feeds A2):** three-point
estimates for *all* A2 work packages + the estimating-basis note (one paragraph
per approach used: analogous/parametric/bottom-up mix).

## Formative assessment (exit ticket)

1. Compute t_E for O=10, M=20, P=60. (Answer: (10+80+60)/6 = 25 h.)
2. Why does the sd formula divide by 6?
3. Estimate, target, commitment — define one of them precisely.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Planning domain (estimation
  methods); Measurement domain (forecasting).
- [Templates](../../../docs/resources/templates.md): three-point estimate
  sheet · [Lab 4 materials](../../../docs/labs/index.md) (CPM network next
  week consumes today's estimates).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the death of the "2 weeks" estimate | — |
| 0:10–0:30 | Estimation families; distributions-not-numbers | family table |
| 0:30–0:50 | PERT worked example incl. 95% range | board computation |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-14 planning poker | item cards |
| 1:35–1:50 | Agile forecast: velocity ranges; sprint math | velocity slide |
| 1:50–1:57 | Convert-the-boss exercise | — |
| 1:57–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Pre-compute all board arithmetic (530/6, √325) to avoid dead air; have the
  95%-range follow-up ready as a second board column.
- Seed CS-14 items from real capstone-scale work; retire items that converge
  in round one (too easy) — spread is the fuel.
- Bridge check: every team leaves with ≥ 3 PERTed packages; Lab 4 assumes it.

## Linked resources

- Lecture skeleton: [`docs/lectures/L10`](../../../docs/lectures/L10-10-estimation.md)
- Case: [CS-14](../../../docs/cases/CS-14.md)
- Assignment: [A2 brief](../../../docs/assignments/a1-scope-schedule.md) —
  estimation section due after L16
- Forward: [CPM L11](../../../docs/lectures/L11-11-cpm-pert.md) ·
  [Monte Carlo L16](../../../docs/lectures/L16-16-quant-risk-simulation.md) ·
  [flow forecasting L22](../../../docs/lectures/L22-22-kanban-flow.md)
