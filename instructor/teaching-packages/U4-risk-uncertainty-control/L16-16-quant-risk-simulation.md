# Lecture 16 — Quantitative Risk: PERT, Trees & Simulation

> **Package for:** L16 · Week 8 · Unit U4 · CLO4 · Bloom: Analyze
> **Case anchor:** CS-22 (Monte Carlo on a class schedule) · **A2 due after this lecture**
> Companion: [`L16` skeleton](../../../docs/lectures/L16-16-quant-risk-simulation.md) · [CS-22 brief](../../../docs/cases/CS-22.md)

## Learning objectives

1. Build a decision tree with probabilities and payoffs; compute EMV and choose.
2. Explain what Monte Carlo simulation adds over PERT arithmetic (correlation, path interactions).
3. Run a 1,000-trial schedule simulation and read the S-curve and tornado chart.
4. Derive contingency from a P80 confidence target and defend it to a sponsor.

## Required prior knowledge

- L10 (PERT: the single-path arithmetic), L11 (paths and floats), L13
  (contingency as a budget line), L15 (normalized risks with P scales).

## Teaching notes

This lecture completes the course's uncertainty arc: L10 estimated *one* path
analytically; today we admit **correlation and path interaction** — the
reasons naive summation lies — and let the machine sample instead.

Sequence: (1) EMV as the *simplest* quantification (one decision, few states)
— do the tree arithmetic by hand so the logic is transparent; (2) the Monte
Carlo mechanics — what gets sampled (durations/costs from the three-point
distributions), what gets recorded (project finish / total cost per trial),
what comes out (S-curve, confidence targets, tornado); (3) the live notebook
run on the class schedule (CS-22); (4) contingency derivation from P80.

Emphasize the honesty rules: simulation output is only as good as its input
distributions; correlated tasks (weather, vendor, the same reviewer) make
single-number "random" sampling optimistic — show the correlation-pitfall
contrast (CS-68's exam-lane setup) with two runs: independent vs correlated
(on the board as pre-computed output, not a second live run).

## Definitions & concepts

- **EMV** — probability-weighted monetary value: Σ pᵢ × payoffᵢ.
- **Decision tree** — decision nodes (squares) × chance nodes (circles);
  EMV folded backward from the leaves.
- **Monte Carlo simulation** — thousands of sampled scenario evaluations
  building outcome distributions for schedule/cost.
- **P80** — the value at 80% cumulative confidence (finish by … / cost under
  …); the standard commitment target in this course.
- **Tornado chart** — sensitivity ranking: which inputs swing the outcome
  most; tells you where estimation effort pays.
- **Correlation** — co-movement of estimates (shared vendor, shared reviewer,
  shared data pipeline); ignoring it narrows the distribution unrealistically.

## Practical examples

**CS:** platform decision tree — build in-house (success p=0.7: save $200k
net; failure p=0.3: overrun $350k) vs buy (subscription $120k certain, exit
clause costs $20k if regulator objects p=0.1). EMV walk: build = 0.7×200 −
0.3×350 = 140 − 105 = **+$35k**; buy = −120 − 0.1×20 = **−$122k** as cost →
build's EMV advantage ≈ $157k... then the sensitivity question: how bad can
failure cost get before the decision flips? (0.7·200 − 0.3·X > −122 → X <
$587k — the flip point; decisions need flip points, not just answers.)

**DS:** model retraining cadence — monthly retrain (compute $30k/qtr, drift
loss p=0.2 × $80k) vs weekly retrain ($60k/qtr, drift loss p=0.05 × $80k):
monthly EMV = 30 + 0.2×80 = **$46k/qtr**; weekly = 60 + 0.05×80 = **$64k/qtr**
— monthly wins *in expectation*; the tail (regulatory breach on drift) may
still choose weekly. EMV + tail judgment = the mature answer.

## Worked example

**Live Monte Carlo (CS-22, notebook):**

Input: 10 tasks, three-point distributions from L10 (O/M/P), the class's own
CS-15 network as dependency truth. Run 1,000 trials:

| Output | Value (illustrative run) |
|---|---|
| Deterministic sum of t_E | 17.0 wk |
| Mean finish (simulated) | 17.8 wk |
| P50 | 17.7 wk |
| P80 | **18.9 wk** |
| P95 | 20.1 wk |
| Critical path instability | path D→E→G leads in 61% of trials; path via C leads in 33% |

Read-outs taught explicitly: (1) the **mean exceeds the deterministic sum**
(systematic optimism of point estimates — merge events); (2) **P80 − P50 ≈
1.2 wk** = the honest contingency for an 80%-confidence commitment; (3) the
**critical path changes between trials** — the single-path assumption of L11
was a useful lie; (4) the **tornado** ranks tasks by swing: the feature-store
task (biggest sd) dominates → estimation effort and crashing attention go
*there*, not everywhere. Contingency line: +1.2 wk schedule buffer, and its
budget echo (1.2 wk × team-week cost ≈ $9.6k ≈ the L13 contingency's 10% —
the two methods now *agree*, which is the point).

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Monte Carlo is estimation theater." | Done right it is the only cheap way to expose path interaction and correlation; done lazily (independent, guessed distributions) it *is* theater. |
| "P80 means 80% chance of success." | It means 80% confidence in the *specific commitment* (date/cost) conditional on the model and the inputs. |
| "EMV chooses correctly." | EMV ignores risk appetite and tails; pair it with flip-point sensitivity and tail severity. |
| "Simulation removes the need for risk responses." | Quantification sizes buffers; it does not prevent anything — responses (L17) still own the causes. |

## Classroom activities

1. **EMV tree by hand (20 min):** the platform tree; each team computes EMVs
   *and* the flip point for their own varying parameter.
2. **CS-22 live simulation (35 min):** run the notebook; teams report P50/P80
   + tornado top driver; instructor varies one distribution live to show
   output sensitivity.
3. **Correlation contrast (10 min):** compare pre-computed independent vs
   correlated runs (CS-68 preview); find the word for what changed (spread,
   not mean).

## Discussion questions

1. Your P80 is 18.9 weeks; the sponsor commits 17. What are your three options, and what does each cost in confidence?
2. Which input distribution is *least* evidenced in your own A2 project — and what cheap evidence would upgrade it?
3. For a model-retraining cadence decision, when is EMV the wrong instrument despite being computable?

## Practical exercise

**In class:** CS-22 deliverable (S-curve + commitment recommendation).
**Take home (25 min):** run the notebook on your A2 network (template provided;
≥ 500 trials); record P80 − deterministic gap and the tornado's top driver;
**A2 due next lecture** — the simulation paragraph is its closing section.

## Formative assessment (exit ticket)

1. EMV: p=0.25 gain $40k, p=0.75 loss $8k → decide vs zero. (+$10k − $6k = +$4k → proceed.)
2. What does a tornado chart rank?
3. Why does the simulated mean exceed the deterministic sum?

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Uncertainty domain (quantitative
  analysis methods).
- [Lab 8 brief](../../../docs/labs/index.md) — Monte Carlo artifact
  (template notebook with seeded reproducibility).
- [Assignment 1 brief](../../../docs/assignments/a1-scope-schedule.md) —
  closing simulation section.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:08 | Hook: every past estimate was a single sample | — |
| 0:08–0:28 | EMV trees + flip points | board arithmetic |
| 0:28–0:50 | Monte Carlo mechanics; S-curve, P80, tornado | slides + notebook |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-22 live run + read-outs | notebook |
| 1:35–1:45 | Correlation contrast (independent vs correlated) | pre-computed runs |
| 1:45–1:57 | Contingency derivation + A2 closing briefing | — |
| 1:57–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Test the notebook **on the room's machines** before class (dependency
  versions); seed = 42 for reproducibility in the answer key.
- Pre-compute the correlated-runs contrast so the 10-minute segment cannot
  fail live.
- A2 collection logistics confirmed for next lecture; late-policy reminder in
  the LMS announcement today.

## Linked resources

- Lecture skeleton: [`docs/lectures/L16`](../../../docs/lectures/L16-16-quant-risk-simulation.md)
- Case: [CS-22](../../../docs/cases/CS-22.md) · Lab 8: [labs index](../../../docs/labs/index.md)
- Assignment: [A2 brief](../../../docs/assignments/a1-scope-schedule.md) (due after this lecture)
- Forward: [responses L17](../../../docs/lectures/L17-17-risk-response.md) ·
  [EVM L19](../../../docs/lectures/L19-19-evm.md) (does the plan hold?).
