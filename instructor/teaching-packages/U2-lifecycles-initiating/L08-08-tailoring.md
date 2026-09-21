# Lecture 08 — Tailoring for Software & Data Projects

> **Package for:** L08 · Week 4 · Unit U2 · CLO1, CLO5 · Bloom: Apply
> **Case anchor:** CS-11 (tailoring a heavyweight template down) · **Capstone team formation today**
> Companion: [`L08` skeleton](../../../docs/lectures/L08-08-tailoring.md) · [CS-11 brief](../../../docs/cases/CS-11.md)

## Learning objectives

1. Explain what tailoring is and why PMBOK 7 makes it a principle.
2. Cut a heavyweight 40-document template to a defensible 6-document set for a small project.
3. Decide what may be scaled down (documentation weight) vs never scaled down (risk and quality discipline).
4. Apply a tailoring worksheet to their own capstone project choice.

## Required prior knowledge

- L05 life cycles (tailoring follows the cycle choice).
- L03 principles (tailoring *is* one).

## Teaching notes

Tailoring is where beginners over-trim and professionals defend. The lesson's
hard core: **you may cut ceremony, never ownership.** A 6-week student project
can safely drop a formal change-control board — it cannot safely drop "someone
owns each risk with a trigger." The verb matters: documents carry *evidence*;
ownership carries *accountability*. Cut evidence volume; keep accountability.

Session mechanics today are special — this is also **capstone team formation
day** (3–5 members, project seed choice, CS-vs-DS track selection per the
[capstone charter](../../../docs/capstone/capstone-charter.md)). Sequence the
timing so formation happens *after* the tailoring content: teams pick a
project, then immediately tailor its management stack as their first team act
— the worksheet becomes the team's working agreement seed.

Common failure to pre-empt: students tailor by deleting everything that
sounds like work. The worksheet forces a *justification per cut*, and the
debrief exposes cuts that remove accountability — "we'll remember the risks"
is the tell.

## Definitions & concepts

- **Tailoring** — deliberate adaptation of method, artifacts, and governance
  to project context (PMBOK 7 principle; ISO 21502 likewise allows
  proportionate governance).
- **Scaling dimensions** — size, duration, team distribution, criticality,
  regulatory exposure, novelty.
- **Proportionality test** — for each artifact: what decision does it improve,
  what evidence does it carry, and what happens if it's absent?
- **Non-negotiables** — risk ownership, quality gates, decision rights,
  honest measurement. Ceremony varies; these persist.

## Practical examples

**CS:** a 6-person, 6-week CourseHub feature build — keep: one-page charter,
board + DoD, lightweight risk list (top 5), simple change log. Cut: formal
CCB, earned-value reporting, stakeholder register beyond one page. Never cut:
acceptance criteria per feature.

**DS:** a 9-week GRIDSENSE anomaly-alert prototype — keep: data access
agreement, data-quality rule sheet, model gate checklist, experiment log.
Cut: full procurement plan, formal QA plan. Never cut: the model release gate
and data steward sign-off — regulatory and trust exposure scale *up* in data
work even when team size scales down.

## Worked example

**Tailoring worksheet, fully worked (board):**

Context: 6-week, 4-student, campus data dashboard; internal only; one
stakeholder (department head); real student data with consent.

| Enterprise artifact | Decision | Defense |
|---|---|---|
| 40-page PM plan | **Cut** → 2-page plan | Decision value moves to the board + weekly metrics |
| Change control board | **Cut** → change log reviewed in weekly standup | One sponsor; latency must be < 1 week |
| Risk register (formal, scored) | **Keep, shrunk** → top-5 risks w/ owners+triggers | Ownership is non-negotiable; *scoring* ceremony scales |
| Quality/QA plan | **Keep, shrunk** → acceptance criteria + 3 data-quality rules | Quality discipline persists; document weight cut |
| Procurement plan | **Cut** | No external vendors |
| Communication plan | **Keep, 3 lines** | Weekly demo + exception email is a plan |
| Model release gate (if DS) | **Keep** | Trust evidence scales with data, not team size |

Net: 7 artifacts, each with a named decision it serves. The defense column is
the deliverable — a cut without a defense is a decision made by accident.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Agile projects don't need any of this." | Every project manages risk, quality, and stakeholders; tailoring changes the *form*, not the existence. |
| "Tailoring = deleting documents." | It is *redesigning evidence* to fit decisions; the justification column is the actual work. |
| "Small project = small risk." | Small teams carrying regulated data have concentrated, not reduced, exposure. |
| "One tailoring lasts the project." | Re-tailor at each phase gate or quarter; context drifts (that is gate work, L24/L28). |

## Classroom activities

1. **CS-11 tailoring gauntlet (35 min):** teams cut the 40-document template
   to 6 for a defined context; every cut needs a written defense.
2. **Accountability triage (15 min):** mixed cards (evidence vs ownership) —
   teams sort "may cut" vs "never cut" and defend two contested ones.
3. **Capstone formation + mini-tailoring (25 min):** teams form, pick seed +
   track, run the worksheet on their own project (5 artifacts minimum).

## Discussion questions

1. Which cut in your CS-11 worksheet would you reverse if the project doubled in length — and what changed?
2. A sponsor demands the full 40-document template for a 6-week project. Argue the case for tailoring *to them* — what do they actually fear?
3. In data projects, why does regulatory exposure often argue *against* the "small team, light process" instinct?

## Practical exercise

**In class:** team mini-tailoring worksheet (capstone deliverable #0, goes in
the team's evidence pack). **Take home (25 min):** individually write the
one-page *life-cycle + tailoring defense* for your team's project (merges your
L05 and L07 homework) — this feeds the charter due at L12.

## Formative assessment (exit ticket)

1. State the difference between cutting ceremony and cutting ownership.
2. Name two artifacts you may cut for a small internal project and one you may not.
3. Your team's chosen seed + track — written down, now, please.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Tailoring principle section and the
  Tailoring chapter.
- ISO 21502:2020 — proportionate governance language.
- [Capstone charter](../../../docs/capstone/capstone-charter.md) — track
  definitions teams choose between today.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the 200-page plan nobody opened | — |
| 0:10–0:30 | Tailoring principle; proportionality test; non-negotiables | worksheet handout |
| 0:30–0:50 | Worked example: full worksheet on student dashboard | board worksheet |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-11 gauntlet + accountability triage | CS-11 brief, cards |
| 1:35–1:55 | **Capstone team formation** + mini-tailoring | seed/track sheets |
| 1:55–2:00 | Exit ticket (incl. team registration) | slips + form |

## Instructor preparation notes

- Prepare the 40-document template inventory (one-line descriptions suffice —
  the exercise is cuts, not reading).
- Print accountability cards (15 evidence / 10 ownership items).
- Bring team-registration sheets; resolve track conflicts today, not later —
  the L27 red-team needs stable teams.
- Note for DS-track teams: data access constraints (synthetic/public only) are
  on the capstone charter page; repeat verbally today.

## Linked resources

- Lecture skeleton: [`docs/lectures/L08`](../../../docs/lectures/L08-08-tailoring.md)
- Case: [CS-11](../../../docs/cases/CS-11.md)
- Capstone: [charter & tracks](../../../docs/capstone/capstone-charter.md) ·
  [rubric](../../../docs/capstone/capstone-rubric.md)
- Forward: [master plan L27](../../../docs/lectures/L27-27-master-plan.md) —
  today's worksheet reappears as the tailoring-justification section.
