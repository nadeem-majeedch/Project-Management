# Quiz 2 — Planning the Work (L09–L12) · A1/Q2

> **INSTRUCTOR ONLY — not published to the site.**
> 15 minutes at the start of L12 · CLO2 · Best 2 of 3 quizzes count.
> 8 marks → reported as percentage. Includes one small computation.
> Items from question-bank-u3.md (IDs noted).

## Version A

**Section A — MCQ (3 × 1 mark).**

1. The 100% rule says: (A) one package per period · (B) children sum to
   100% of the parent's scope · (C) the WBS covers the whole organization ·
   (D) 100% of packages need dictionaries *(QB-U3-01)*
2. Free float > 0 requires: (A) the critical path · (B) a successor whose
   ES is later than this activity's EF · (C) no predecessors · (D) an early
   finish *(QB-U3-04)*
3. Resource-constrained levelling: (A) keeps the end date · (B) extends the
   end date · (C) removes the critical path · (D) adds resources
   *(QB-U3-05)*

**Section B — Computation (5 marks).**

4. Activities (weeks, FS): A(3) · B(5, after A) · C(2, after A) ·
   D(6, after B) · H(5, after C) · J(3, after H) · N(1, after D and J).

   a) Forward pass: EF of H and EF of J. (2)
   b) Project duration. (2)
   c) Total float of C. (1)

**Answers (hand-verified — two-path network):**
a) EF(H) = 3+2+5 = **10**; EF(J) = 10+3 = **13**.
b) Chain A–B–D–N = 3+5+6+1 = **15**; C-route = 14 → duration **15 weeks**.
c) LF(J) = LS(N) = 14; LS(J) = 11; LF(H) = 11; LS(H) = 6; LF(C) = 6;
   LS(C) = 4; ES(C) = 3 → TF(C) = **1 week** — the C–H–J route is
   near-critical, one week away: crashing decisions must check it.

## Version B

**Section A — MCQ (3 × 1 mark).**

1. PERT's expected value weights the most likely by: (A) 1/6 · (B) 1/3 ·
   (C) 1/2 · (D) 4/6 *(QB-U3-03)*
2. A WBS decomposes by deliverable rather than: (A) phase · (B) org chart ·
   (C) cost category · (D) all of the above *(QB-U3-02)*
3. Contingency reserve: (A) sponsor-controlled · (B) PM-controlled,
   known-unknowns · (C) outside the baseline · (D) needs CCB approval
   *(QB-U3-06)*

**Section B — Computation (5 marks).**

4. Sprint capacity: 5 devs × 10 days × 8 h; focus factor 0.7; 20 h support;
   14 h per point.

   a) Effective focused hours. (2)
   b) Point capacity to one decimal. (2)
   c) The team commits 21 points. Name the discipline problem. (1)

**Answers (machine-verified, CS-28 chain):** a) 400×0.7 − 20 = **260 h**.
b) **18.6 points**. c) Overcommitment by 2.4 points → guaranteed carryover;
   commit to the goal, move a story out at planning, never extend the sprint.

## Key — Version A
| 1 | 2 | 3 | 4a | 4b | 4c |
|---|---|---|---|---|---|
| B | B | B | 10; 13 | 15 wk | **1** (near-critical) |

## Key — Version B
| 1 | 2 | 3 | 4a | 4b | 4c |
|---|---|---|---|---|---|
| D | D | B | 260 h | 18.6 | overcommitment → carryover |

## Marking guide (both versions)

- Half-marks on 4a/4b for arithmetic slips with correct method; zero only
  for method failure.
- Debrief item A/3 (or B/1) immediately: levelling vs crashing vs fast
  tracking is the most conflated triple in the course.
- **Design note:** the network numbers here are hand-verified (two-path
  check: 15 vs 14); any future regeneration must re-verify both paths —
  near-critical routes are where hand-set quizzes go wrong.
