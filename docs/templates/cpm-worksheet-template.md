<!--
Template: CPM worksheet (Lab 4; graded on the pass, not the answer)
Fill the table with the full forward and backward pass, then answer the
reading questions. Show work: a wrong answer with a visible pass earns more
than a right answer with none.
-->

# CPM Worksheet — [Project name]

## 1. Pass table
| ID | Dur | Pred | ES | EF | LS | LF | Total float | Free float | Critical? |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

**Formulas:** ES = max(EF of preds) · EF = ES + Dur · LF = min(LS of succs)
(LF of last = project finish) · LS = LF − Dur · TF = LS − ES ·
FF = min(ES of succs) − EF.

## 2. Results
- **Critical path(s):** [A → … → H] · **Project duration:** [n weeks]
- **Near-critical path & float:** [path, float] — what single slip moves it?
- **Negative-float check (deadline applied):** if the sponsor deadline is
  [d] weeks, which paths go negative and by how much?

## 3. Reading questions (answer before the debrief)
1. Which float belongs to the *project* (paths sharing it)? Name the chain.
2. One activity gained a +1-week lag on a discretionary dependency. Which
   float numbers change and why?
3. Your sponsor proposes cutting 2 weeks by starting [activity] before its
   predecessor finishes. From the table, what must be true for that to work?

## 4. Compression memo (≤ 10 lines)
If the deadline is [X] weeks shorter: crash candidates (activity, slope =
Δcost/Δweek, max weeks) vs fast-track candidates (what overlaps, what rework
risk). Recommendation + the number that justifies it.
