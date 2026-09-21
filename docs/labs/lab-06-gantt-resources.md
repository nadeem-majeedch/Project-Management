---
title: "Lab 6 — Gantt Chart & Resource Allocation"
lab: 6
week: 7
lecture: 12
time: "2 hours in-lab + 1 hour refinement"
deliverable: "Baselined Gantt + period resource-load table + levelling decisions"
submitted: "LMS, within one week"
---

# Lab 6 — Gantt Chart & Resource Allocation

## 1. Objectives
1. Turn the CPM schedule into a baselined Gantt with milestones and the deadline line.
2. Compute period resource loads from activity hours and capacity.
3. Level overloads with justified, path-aware decisions (never silently move critical work).

## 2. Background & scenario
The CPM pass says the §A network finishes in 17 weeks — but CPM assumes
infinite resources. The real team is 3 devs + 1 QA + 1 DE + half-time PM,
with two contract testers joining for G. This lab converts the network into
a *staffed* plan: where the §B hours land on the calendar, which periods
overload, and what levelling costs you. The package hours in
[data pack §B](data-pack.md) are the load; the capacity model below is
your constraint.

## 3. Required tools
- [Gantt & resource template](../templates/gantt-resource-template.md)
- [Data pack §A (schedule) and §B (hours)](data-pack.md)
- Lab 4 float table (you need float to know what may move)

## 4. Capacity model (given — use as stated)
| Role | Availability | Notes |
|---|---|---|
| Developers (3) | 80 h/wk pooled | after ceremonies; product work |
| QA (1) | 40 h/wk | independent of dev |
| Data engineer (1) | 40 h/wk | dedicated to this project |
| PM (0.5) | 20 h/wk | everything PM-typed |
| Contract testers (2) | +80 h/wk QA-pooled | weeks 13–17 only (G's 240 h) |

Periods: **P1 wk 1–4, P2 wk 5–8, P3 wk 9–12, P4 wk 13–16, P5 wk 17.**
Capacity per 4-week period: Dev 320 h · QA 160 h (P4: 160 + 320 with testers) ·
DE 160 h · PM 80 h; P5 is one week (Dev 80 · QA 40 + testers 80 · DE 40 · PM 20).
*(Overloads still appear — the deadline forces compression, and G's 240 QA h
would need 6 weeks of internal-QA capacity if the testers were not added.)*

## 5. Step-by-step instructions
1. **Baseline Gantt (30 min).** Draw the §A schedule as week bars using ES/duration from Lab 4. Mark milestones (end A, end B, end D, end E, end F, end G, rollout) and the deadline line at week 17.
2. **Map hours to periods (30 min).** Each activity's hours land in its scheduled weeks (split evenly across duration). Example: C (wk 3–6) puts its 320 dev h as 160 h into P1 (wks 3–4) and 160 h into P2 (wks 5–6); compute the rest.
3. **Load vs capacity table (20 min).** Fill the template's Part B for Dev/QA/DE/PM per period. Overloads are expected — find them.
4. **Levelling (30 min).** For each overload: delay non-critical work into float (cite float), split, or re-sequence. Rule: critical activities may not move silently — if a critical activity must move, that is a baseline change, flag it.
5. **Cost of levelling (10 min).** State the before/after finish. If levelling pushes finish beyond 17 weeks, you have found the real constraint — document it instead of hiding it.
6. **Refine (out of lab, 1 h).** Final chart with legend, milestones, deadline, and the levelling log.

## 6. Your tasks (checklist)
- [ ] Gantt with all 8 activities, milestones, deadline line
- [ ] Load-vs-capacity table, all 4 roles × 5 periods
- [ ] Overloads identified with evidence (numbers)
- [ ] Levelling decisions path-aware and cited to float
- [ ] Before/after finish dates recorded
- [ ] Any critical-path movement flagged as baseline change

## 7. Expected outputs
`gantt-resources.md` (+ the worksheet section of the template). Submit via LMS.

## 8. Reflection questions
1. Which overload is *structural* (capacity genuinely below demand) vs *scheduling* (work placed badly)? Name one of each.
2. G's 240 QA hours need the two contract testers. What happens to P4's QA load if G starts one week late — and which calendar constraint do the testers' contracts collide with?
3. D + E need 320 DE h but E (120 h) cannot start until D (200 h) finishes — what does this imply about the DE's utilization curve that the CPM network alone cannot show?

## 9. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Gantt | accurate bars, milestones, deadline | bars from memory |
| Load table | arithmetic traceable to §B | invented numbers |
| Levelling | float-cited, path-aware | moves critical work silently |
| Honesty | documents capacity limits found | hides overloads |

## 10. Related material
[Lecture 12 — Schedule tools](../lectures/L12-12-schedule-tools.md) ·
[Case CS-16](../cases/CS-16.md) ·
[Lab 7's budget (next) consumes the levelled plan](lab-07-cost-baseline.md)
