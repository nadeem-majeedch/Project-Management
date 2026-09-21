# Lab 4 Answer Key — Dependency Network & Critical Path

## Reference pass (checker-verified; students' tables must match)

| ID | Dur | Pred | ES | EF | LS | LF | TF | FF | Critical |
|---|---|---|---|---|---|---|---|---|---|
| A | 2 | — | 0 | 2 | 0 | 2 | 0 | 0 | YES |
| B | 3 | A | 2 | 5 | 2 | 5 | 0 | 0 | YES |
| C | 4 | B | 5 | 9 | 7 | 11 | 2 | 2 | no |
| D | 5 | B | 5 | 10 | 5 | 10 | 0 | 0 | YES |
| E | 4 | D | 10 | 14 | 10 | 14 | 0 | 0 | YES |
| F | 3 | B, C | 9 | 12 | 11 | 14 | 2 | 2 | no |
| G | 2 | C, E, F | 14 | 16 | 14 | 16 | 0 | 0 | YES |
| H | 1 | G | 16 | 17 | 16 | 17 | 0 | 0 | YES |

- **Critical path:** A → B → D → E → G → H = **17 weeks**.
- **Near-critical:** A → B → C → F → G → H = 15 weeks (TF 2 on C and F —
  shared path float, not independent pockets).
- **Free float:** C: min(ES F=9) − EF C(9) = 0? — careful: F cannot start
  before C finishes (FS), so FF(C) = 9 − 9 = 0; FF(F) = 14 − 12 = 2.
  **Total float: C = 2, F = 2; all others 0.**
- Pass on the CSV `critical` column: exactly A, B, D, E, G, H = TRUE.

## Dependency audit (model)

- C←B, D←B, F←C mandatory (build order); F←B discretionary (F's dev leads
  can start schema-consumption before C's UI completes — SS+1 candidate).
- G←C,E,F mandatory (test needs all three); H←G mandatory (SLA evidence).
- External: LMS vendor schema (constraint on F start); academic calendar
  (constraint on H).

## Compression memo (model answer)

Deadline 15 weeks → need 2 weeks off A→B→D→E→G→H.
- D crash 5→4: 60,000/wk (critical, safe).
- E crash 4→3: 75,000/wk (critical, safe).
- **Cheapest 2 weeks: crash D (60,000) + crash E (75,000) = 135,000.**
- Crash C? Irrelevant — C has float 2; shortening it moves nothing (float
  trap).
- Fast-track E over D (SS+2): saves ≈2 weeks of calendar but rework risk on
  streaming features; with rework probability ≈30% the expected cost
  (≈1.2 wk of DE + dev rework ≈ 110k+) exceeds the certain 135,000 only
  marginally — accept the certain spend unless schedule risk is extreme.

## Common wrong answers

| Error | Correction |
|---|---|
| Backward pass started LF at H's EF + 1 | LF(last) = project EF = 17, not 18 |
| FF(C) = 2 | FF is successor-gap based: F starts when C finishes (FS), FF(C)=0; the 2 is *total* float shared with F |
| "Critical path = all activities with any float" | critical = TF 0 path; C/F are near-critical |
| Crashed C to save 2 weeks | C's float absorbs nothing — crashing off-path work wastes money |
| Fast-track without rework number | rework probability × cost must be stated vs certain crash cost |

## Reflection guidance

1. E's TF 0 comes from D→E; G is critical because it's the merge point of
   three paths — its zero float is structural (merge), E's is inherited.
2. Lag on F←B (SS+1) slipping: F's start moves, EF F = 13 → TF F = 1, and C's
   float also shrinks — shared path.
3. Probabilistic option right when sponsor's schedule penalty dwarfs cost
   certainty and rework is recoverable within remaining float.

## Preparation notes

Run the checker on `cpm-pass-worksheet.csv` live in the lab — students see
row-level correctness immediately. The C/F float subtlety is the exam-level
discriminator; rehearse it on the board.
