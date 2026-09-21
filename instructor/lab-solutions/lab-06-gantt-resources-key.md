# Lab 6 Answer Key — Gantt & Resource Allocation

## Model baseline Gantt (from Lab 4 ES/durations)

| Activity | Wks | Bar (weeks 1–17) |
|---|---|---|
| A | 1–2 | ██ |
| B | 3–5 | ███ |
| C | 6–9 | ████ |
| D | 6–10 | █████ |
| E | 11–14 | ████ |
| F | 10–12 | ███ |
| G | 15–16 | ██ |
| H | 17 | █ |

Milestones: end A (wk2), end B (wk5), end D (wk10), end E (wk14), end F
(wk12), test pass (wk16), rollout (wk17). Deadline line: wk17.

## Load vs capacity (model numbers; package cost spread evenly per activity-week)

| Period | Dev need | Dev cap (320) | QA need | QA cap (160; P4/P5 +80/wk testers) | DE need (160) | PM need (80) |
|---|---|---|---|---|---|---|
| P1 (1–4) | 94 | ✓ | 33 | ✓ | 27 | 13 |
| P2 (5–8) | **339** | **overload +19** | 79 | ✓ | 133 | 28 |
| P3 (9–12) | 308 | ✓ (tight) | 78 | ✓ | 140 | 33 |
| P4 (13–16) | 100 | ✓ | 250 | ✓ with testers (480 cap) | 60 | 14 |
| P5 (17) | 24 | ✓ | 40 | ✓ | 8 | 8 |

*(values rounded to whole hours; totals reconcile to §B: dev 864, QA 480,
DE 368, PM 96.)*

## Findings (the graded core)

1. **QA P4 is the structural overload:** G's 240 QA h land in wks 15–16
   against 160 h of internal QA capacity → the two contract testers (wks
   13–17) are not optional, they are *required by the schedule* — their
   contract window must match G's slot, which collides with any slip.
2. **Dev P2 overload (+19 h):** all three activities loading P2 (B tail, C,
   D head) are critical — no float to level with. Options: ≈19 h contract
   dev capacity (cheapest honest fix), or split C's non-critical internals,
   or the finish slips ~1 week → deadline breach → escalate to sponsor.
   Accept answers that quantify; reject "people will work harder."
3. **DE utilization curve:** DE is idle-ish P1 (27 h), saturated P2–P3
   (133–140 h of 160), idle P4 tail — D (200 h) then E (120 h) is a
   sequential 320-h block the network shows but only the resource chart makes
   visible; any B slip starves D's start immediately (DE is the bottleneck
   resource for the DS track).
4. **Before/after finish:** with testers + 19 dev h resolved → finish holds
   17. Without dev fix → 18 → violates calendar rule → the honest output of
   this lab is an escalation memo, not a tidy plan.

## Common wrong answers

| Error | Correction |
|---|---|
| Bars drawn from duration alone (ignoring ES) | Gantt comes from the CPM pass, not memory |
| Loads computed per activity-period guesswork | hours spread evenly per activity-week; show one example calculation |
| Critical activity silently delayed to fix overload | levelling moves float-carrying work only; critical moves = baseline change + flag |
| "Add overtime" without numbers | quantify the gap (+19 dev h; 90 QA h before testers) and cost it |
| Tester dependency missed | P4 QA is infeasible without the testers' calendar window |

## Reflection guidance

1. Structural: QA P4 (capacity genuinely below G's demand). Scheduling:
   none major — P3 dev is tight but legal; if a student levels B's tail into
   wk 6 they moved critical work (flag it).
2. G one week late → G's 240 h push into wk 16–17: testers' contract window
   (wk 13–17) still covers it but P5 QA = 120+40 vs H also needing QA — H's
   SLA validation then collides with the calendar rule: the testers' window
   is the hidden single point of failure.
3. D/E sequential 320 h on one DE → D's start is the control point for the
   whole DS track; the network shows the sequence, only the histogram shows
   the starvation risk if B slips.

## Preparation notes

Bring Lab 4 float tables — levelling without float is guessing. The +19 h
dev overload is deliberate: students should discover that the deadline, not
their plan, creates it, and practice escalating with numbers.
