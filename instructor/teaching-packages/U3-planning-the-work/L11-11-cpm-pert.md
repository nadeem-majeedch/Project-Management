# Lecture 11 — Network Logic, CPM & PERT

> **Package for:** L11 · Week 6 · Unit U3 · CLO2 · Bloom: Apply
> **Case anchor:** CS-15 (hand-solved 14-activity network) · **Quiz 2 next lecture**
> Companion: [`L11` skeleton](../../../docs/lectures/L11-11-cpm-pert.md) · [CS-15 brief](../../../docs/cases/CS-15.md)

## Learning objectives

1. Model activity dependencies with FS/SS/FF/SF links, leads, and lags.
2. Execute the forward and backward pass to compute ES/EF/LS/LF for every activity.
3. Identify the critical path and compute total and free float.
4. Evaluate crashing vs fast-tracking with explicit cost and risk arithmetic.

## Required prior knowledge

- L09 work packages; L10 three-point estimates (the durations being networked).
- Comfort with quick arithmetic — this is the course's most computational
  lecture alongside L19.

## Teaching notes

CPM is the lecture where the course's promise ("quantitative backbone") is
kept or broken. The failure mode is teaching it as a table-filling ritual.
Instead teach the *two questions the network exists to answer*: **what
controls the end date?** (critical path) and **where can we absorb trouble?**
(float). Every mechanic — forward pass, backward pass, float arithmetic —
serves those questions.

Draw the network *large* and do the passes in public, narrating the logic
("the forward pass asks: what's the earliest I could finish if everyone
hustled? the backward pass asks: how late could each task be if the project
still lands?"). Then hand them a network of their own (CS-15) and walk away.

The compression segment must stay arithmetic-honest: crashing has a price per
week, fast-tracking has a rework probability. Making those numbers explicit is
what separates defensible schedule decisions from vibes (and seeds the
cost/schedule trade analysis the midterm probes).

## Definitions & concepts

- **Dependencies** — FS (finish-to-start, the default), SS, FF, SF; **lead**
  (overlap, negative lag), **lag** (waiting time, e.g., cure/dry/holdout
  periods). DS example: training must lag data-validation by the pipeline run
  time (FS + lag).
- **Forward pass** — ES = max(EF of predecessors); EF = ES + duration.
- **Backward pass** — LF = min(LS of successors); LS = LF − duration.
- **Total float** — LS − ES: how long an activity can slip *without moving the
  project end*. **Free float** — ES of successor − EF: slip without touching
  the successor's start.
- **Critical path** — longest path; total float = 0; drives the end date.
  Near-critical paths (float ≤ 1–2) deserve respect too.
- **Crashing** — shorten duration with money (overtime, extra hands); cost
  slope = Δcost / Δweeks. **Fast-tracking** — overlap sequential work;
  pays in rework risk, not money.

## Practical examples

**CS:** registration engine path: rule format → rule service → integration
tests → deployment. A compliance-report task (fixed external date) sits
off-path with float — the place to safely park a delayed hire.

**DS:** churn model path: data audit → feature store → training → gate →
rollout. Streaming-features work sits parallel to batch features (SS + 2-week
lag) with float — *until* the drift-monitoring design pulls it onto the path:
critical paths move, and networks must be re-run when reality changes (that is
L20's re-baselining hook).

## Worked example

**Hand-solved 8-activity network (board, full pass):** weeks; all FS.

| Activity | Predecessor | Dur |
|---|---|---|
| A Data audit | — | 2 |
| B Schema design | A | 3 |
| C Ingestion build | B | 4 |
| D Feature store | B | 5 |
| E Streaming features | D | 4 |
| F Model training | C, D | 3 |
| G Gate evidence | E, F | 2 |
| H Rollout | G | 1 |

**Forward pass:** A: ES0 EF2 · B: 2–5 · C: 5–9 · D: 5–10 · E: 10–14 ·
F: max(EF C=9, EF D=10) = 10 → 13 · G: max(EF E=14, EF F=13) = 14 → 16 ·
H: 16 → **17 = project EF**.

**Backward pass** (LF start = 17): H: LS16 · G: LF16 → LS14 · F: LF14 →
LS11 · E: LF14 → LS10 · D: LF = min(LS E=10, LS F=11) = 10 → LS5 ·
C: LF = LS F = 11 → LS7 · B: LF = min(LS C=7, LS D=5) = 5 → LS2 ·
A: LF = LS B = 2 → LS0.

**Floats:** C: LS7−ES5 = **2** · E: 10−10 = **0** · F: 11−10 = **1** ·
A, B, D, G, H: **0**.

**Critical path: A→B→D→E→G→H = 17 weeks.** Near-critical: F (float 1) — one
bad week in training and the path shifts; name that explicitly.

**Free float:** C: ES F (10) − EF C (9) = 1; E: ES G (14) − EF E (14) = 0.

**Compression decision (numbers):** D (feature store) can crash 5→4 weeks at
k$8k; E can crash 4→3 at k$5k. Both are on the path; total-savings logic:
crash E first (cheaper slope). Fast-tracking candidate: overlap E with D
(SS+2 lag): saves ~2 weeks but rework probability ~30% on streaming features
(expected rework ≈ 0.3 × 2 wks of E's team ≈ 1.2 wk × k$6k ≈ k$7.2k) — compare
against crashing: E-crash k$5k certain vs fast-track ~k$7.2k *expected* + a
risk of schedule slip on the critical path. Decision discipline: choose the
**certain k$5k** unless the k$2k difference buys something else. (This exact
reasoning reappears in L16 with Monte Carlo; note the bridge.)

## Common misconceptions

| Misconception | Correction |
|---|---|
| "The critical path is the longest *to-do* chain." | It is the longest *timewise dependent* chain; duration, not headcount or importance. |
| "Float is slack to waste." | Float is a *shared, finite* risk buffer; consuming it silently converts flexible tasks into critical ones. |
| "Zero float = most important work." | Criticality ≠ priority of value; a critical 1-day task isn't more valuable than a floating 3-week one. |
| "Crashing always helps." | Crashing non-critical activities buys nothing; crashing has diminishing returns and can add cost past benefit. |
| "The critical path never changes." | It moves when reality moves; networks are re-run at each review (CS-56's whole point). |

## Classroom activities

1. **CS-15 full solve (40 min):** 14 activities, teams complete both passes +
   float table + critical path; instructor circulates checking *arithmetic
   discipline* (ES from max-EF is the recurring error).
2. **Compression trade (15 min):** given cost slopes, teams must cut 3 weeks
   under a k$12k budget — write the decision memo in three lines.
3. **Find-the-dependency (10 min):** six SS/FF/SF/lag scenarios; teams name the
   link type — quick fluency drill.

## Discussion questions

1. Your team's network has two paths within 1 week of each other. What does that imply about monitoring and about crashing decisions?
2. Where in a *data* network does a lag belong (name the real waiting), and what happens when teams ignore lags?
3. Fast-tracking shows a favorable expected value. Why might you still not do it? (Think: variance, blame, rework on the critical path.)

## Practical exercise

**In class:** CS-15 deliverable (complete network). **Take home (feeds A2):**
build and solve the network for your own A2 packages (≥ 20 activities, hand
pass shown); identify critical path, total float table, and the two cheapest
compression candidates with slopes.

## Formative assessment (exit ticket)

1. Forward pass: what is ES of an activity whose predecessors finish at day 8 and day 12? (12.)
2. Total float formula.
3. Why does crashing a non-critical task buy you nothing?

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Planning domain (network analysis,
  critical path, compression).
- PMI. (2017). *PMBOK Guide* (6th ed.) — "Sequence Activities" / "Develop
  Schedule" processes (ITTO vocabulary; leads/lags taxonomy).
- [Lab 4 brief](../../../docs/labs/index.md) — hand-solved network artifact.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:08 | Hook: "everything is urgent" vs the path | — |
| 0:08–0:22 | Dependency types, leads/lags | scenario cards |
| 0:22–0:50 | Worked example: full passes + floats + compression math | board network |
| 0:50–1:00 | Break | |
| 1:00–1:40 | CS-15 team solve | network handout |
| 1:40–1:55 | Compression trade memo | slope table |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Draw the worked network on the board *before* class if the room allows;
  public arithmetic takes the full 28 minutes otherwise.
- CS-15 answer key: complete both passes recorded in the
  [answer keys](../../answer-keys/README.md) area before delivery; verify the
  intentional near-critical path (float 1) — the debrief depends on it.
- Quiz 2 (next lecture) blueprint: 1 small network (4–6 nodes) + estimation
  concept items.

## Linked resources

- Lecture skeleton: [`docs/lectures/L11`](../../../docs/lectures/L11-11-cpm-pert.md)
- Case: [CS-15](../../../docs/cases/CS-15.md) · Lab 4: [labs index](../../../docs/labs/index.md)
- Assignment: [A2 brief](../../../docs/assignments/a1-scope-schedule.md)
- Forward: [Gantt/levelling L12](../../../docs/lectures/L12-12-schedule-tools.md) ·
  [Monte Carlo L16](../../../docs/lectures/L16-16-quant-risk-simulation.md) ·
  [critical-path shift CS-56 (exam lane)](../../../docs/cases/index.md)
