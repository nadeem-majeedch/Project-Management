# Lab 11 Answer Key — Monte Carlo Schedule Simulation

## Reference run (deterministic: seed 42, 20,000 trials — verified against
`data/campus-mend-sim-reference.json` by the checker)

| Statistic | Value |
|---|---|
| Mean | 17.88 wk |
| Stdev | 0.63 wk |
| Min / Max | 16.15 / 20.31 wk |
| P50 | 17.85 wk |
| P80 | 18.43 wk |
| P90 | 18.72 wk |
| P95 | 18.98 wk |
| **P(finish ≤ 17)** | **7.55%** |

## Model interpretation (the P50-vs-CPM explanation)

CPM's 17.0 weeks uses most-likely durations; A, B, D carry upward tails
(triangular 0.9–1.4 / 0.85–1.5 / 0.9–1.3 × baseline) and all three sit on the
critical path. Upside tails are fatter and longer than the downside (0.85–0.9
floors are shallow; ceilings reach +40–50%), so finish lands right of 17.0 in
most trials — P50 = 17.85. Sponsor version: "Our best-case plan says week 17,
but on current evidence, half of comparable outcomes finish after week 17.85,
and there is about a 1-in-13 chance we make the calendar at all. That is a
planning fact, not pessimism — it says we must decide how to buy probability:
scope, buffer, or early vendor actions."

## Sensitivity check (model)

Setting B = 4 wk (from 3) in a student's copy shifts P50 to ≈ 18.9 and
P(on-time) toward 0 — B is the hub feeding C, D, F simultaneously; a B slip
re-prices everything downstream. (Exact deltas depend on the copy; require
before/after numbers, not prose.) Revert afterwards — the deterministic
reference must stay reproducible.

## Mitigation tie-in (model)

R8 (legacy dates, Critical 16) mitigation in package A flattens A's tail →
P50 drops and the on-time probability rises most per rupee spent, because A
sits at the head of *both* paths. R1's mitigation (vendor SLA) protects F,
which has float — cheaper but smaller distribution effect. Register actions
and simulation tails must connect: the register's Critical risks should
appear as the dominant simulation drivers.

## Memo grading checklist

- [ ] Confidence stated as a probability range, not adjectives
- [ ] P80 (and ideally P95) translated into calendar dates
- [ ] Decision window named (what must be decided by which week)
- [ ] Options priced: scope cut vs buffer vs early vendor work
- [ ] No "we will try harder" — probability is not a motivational variable

## Common wrong answers

| Error | Correction |
|---|---|
| "Simulation says we're late" | it says most outcomes exceed wk 17 *given current duration estimates* — change estimates or plan |
| P80 read as "80% of the work" | P80 = date by which 80% of *trials* finish |
| Sensitivity run invented | require the actual re-run with before/after numbers |
| Treating mean as the promise | promise from P-levels; the mean is not a commitment |
| Editing the shared CSV without reverting | the reference must stay deterministic; copies only |

## Reflection guidance

1. Three legitimate decisions: re-baseline the promise (P80 date), buy
   probability (crash/early-start actions), or pre-negotiate scope
   contingencies — all three are honest; "ignore it" is not.
2. Single-point promises with an 8% underlying probability mislead the
   sponsor regardless of effort — the distribution exists whether or not
   you state it.
3. P99 from the run ≈ 19.5+ wk → ≈ 2.5 weeks of schedule → ~ weeks of team
   cost (order of 200k+); the cheaper honest answer is the P80 promise plus
   a pre-agreed scope lever.

## Preparation notes

The script is deterministic — run it once before class and pin the numbers
on the board; the lab's value is interpretation, not execution. Collect the
memos: they are the pre-work for Lab 15's recovery decision.
