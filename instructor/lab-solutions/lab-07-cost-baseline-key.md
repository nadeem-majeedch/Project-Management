# Lab 7 Answer Key — Cost Baseline

## Model labor build-up (per package; checker-verified totals)

| Pkg | Dev h × 1,800 | QA h × 1,200 | DE h × 2,400 | PM h × 2,200 | Pkg cost |
|---|---|---|---|---|---|
| A | 72,000 | 24,000 | 0 | 17,600 | 113,600 |
| B | 144,000 | 24,000 | 96,000 | 17,600 | 281,600 |
| C | 576,000 | 96,000 | 0 | 52,800 | 724,800 |
| D | 216,000 | 24,000 | 480,000 | 26,400 | 746,400 |
| E | 216,000 | 24,000 | 288,000 | 26,400 | 554,400 |
| F | 216,000 | 48,000 | 0 | 35,200 | 299,200 |
| G | 72,000 | 288,000 | 0 | 17,600 | 377,600 |
| H | 43,200 | 48,000 | 19,200 | 17,600 | 128,000 |
| **Σ** | **1,555,200** | **576,000** | **883,200** | **211,200** | **3,225,600** |

## Baseline assembly (checker-verified)

| Line | Amount (PKR) |
|---|---|
| Labor | 3,225,600 |
| Indirects (25%) | 806,400 |
| Direct (monitoring 40,000 + test-data/GPU 48,000) | 88,000 |
| **Subtotal** | **4,120,000** |
| Contingency (10% of subtotal — Lab 9 register funds it) | 412,000 |
| **Cost baseline (= BAC)** | **4,532,000** |
| Management reserve (5% of baseline; sponsor-held) | 226,600 |
| **Funding ask** | **4,758,600** |

## S-curve (model time-phasing; cumulative must end at 4,532,000)

| Period | Weeks | Labor+PM+indirect spread | Direct at point | Period total | Cumulative |
|---|---|---|---|---|---|
| P1 | 1–4 | ≈ 560,000 | monitoring 40,000 | 600,000 | 600,000 |
| P2 | 5–8 | ≈ 1,350,000 | — | 1,350,000 | 1,950,000 |
| P3 | 9–12 | ≈ 1,290,000 | GPU/test-data 48,000 | 1,338,000 | 3,288,000 |
| P4 | 13–16 | ≈ 1,000,000 | — | 1,000,000 | 4,288,000 |
| P5 | 17 | ≈ 244,000 | — | 244,000 | **4,532,000** ✓ |

*(spread = package cost × share of its weeks inside the period; students'
numbers may differ ±10% provided the cumulative closes exactly at baseline
and follows the levelled plan — S-shape, not a line.)*

## Contract-cap check (model)

Vendor-relevant exposure: F executed as vendor work (120 dev h equivalent at
2,500 = 300,000) + integration support ≈ 500,000–700,000 total inside the
SOW — interpretation must be stated. Either reading stays ≤ 1,950,000 ✓.
Pass requires the interpretation + arithmetic, not the specific number.

## Common wrong answers

| Error | Correction |
|---|---|
| DE hours at dev rate | 2,400 vs 1,800 — D and E costs understate by 20k+ |
| Contingency applied to labor only | 10% of subtotal (labor + indirects + direct) |
| MR inside baseline | MR is sponsor-held insurance above the baseline; PM cannot spend it |
| S-curve cumulative ≠ baseline | chain-of-custody broken; usually a period mis-assignment |
| Vendor SOW ignored | fixed-price ≠ free: exposure must be estimated and checked vs cap |

## Reflection guidance

1. Contingency in-baseline = PM-controlled, risk-derived (visible in EVM);
   MR out = sponsor-gated for unknown-unknowns — the split prevents PM
   quietly spending insurance and prevents sponsor nickel-and-diming risk
   responses.
2. Legitimate responses: re-phase non-fiscal-year-crossing work earlier
   (plan change), or request forward funding (funding change); hiding the
   crossing is neither.
3. Straight-line S-curve → PV is fiction; EVM indices (Lab 13) then measure
   distance from a fantasy, not from plan.

## Preparation notes

Run the checker's budget gate before class; arithmetic errors are cheap to
fix here and fatal to Lab 13's PV chain. Students confusing MR/contingency
need redirection to L13's worked example before proceeding.
