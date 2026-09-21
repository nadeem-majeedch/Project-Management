# Lecture 07 — Stakeholder Identification & Analysis

> **Package for:** L07 · Week 4 · Unit U2 · CLO5 · Bloom: Apply
> **Case anchors:** CS-09 (stakeholder hunt), CS-10 (grid + hostile engagement)
> Companion: [`L07` skeleton](../../../docs/lectures/L07-07-stakeholders.md) · [CS-09](../../../docs/cases/CS-09.md) · [CS-10](../../../docs/cases/CS-10.md)

## Learning objectives

1. Identify ≥ 15 stakeholders for a technical project, including hidden ones.
2. Place stakeholders on a power/interest grid and derive engagement strategies per quadrant.
3. Use the engagement assessment matrix (unaware → leading) to plan movement.
4. Justify engagement effort allocation under finite PM time.

## Required prior knowledge

- L04 roles (sponsor/PO/steward distinctions).
- L06 charter (stakeholders shape success criteria).

## Teaching notes

The dangerous myth this lecture kills: *stakeholder analysis is a list.* A
register nobody uses is filing. Teach it as a **risk instrument with a plan
attached**: identification → prioritization → engagement *movement* — where is
each stakeholder now, where do they need to be, what is the smallest action
that moves them?

The hidden-stakeholder hunt is the session's engine, especially for data
projects: auditors, data owners, nurses' unions, clinical governance,
legal-privacy, *and the silent users of the current spreadsheet workaround*.
Teams that find only the org-chart people fail the exercise; say so up front.

Facilitation: run CS-09 as a competitive hunt (leader = most *non-obvious*
stakeholders, not most total), then CS-10 for the strategy work. The hostile
engagement plans are the debrief's gold — most teams first propose "communicate
more"; push them to what power is actually being exercised and what trade
would change incentives.

## Definitions & concepts

- **Stakeholder** — anyone who can affect, is affected by, or perceives
  themselves affected by the project (the *perceives* clause matters).
- **Power/interest grid** — quadrants: manage closely (high/high), keep
  satisfied (high power/low interest), keep informed (low/high), monitor
  (low/low).
- **Engagement assessment matrix** — current vs desired engagement:
  unaware → resistant → neutral → supportive → leading.
- **Salience** — power × legitimacy × urgency; explains why "low interest"
  stakeholders suddenly dominate agendas.
- **Stakeholder register** — name, role, interest, power, current/desired
  engagement, engagement action, owner (refresh cadence: monthly or on
  change).

## Practical examples

**CS:** CampusHub registration rewrite — obvious: registrar, students,
advisors, help desk. Hidden: the exam-office script that scrapes the old
system (will break), the marketing team sending email campaigns keyed to old
data fields, the disability-services office (accessibility requirements with
legal weight), IT security review board.

**DS:** churn model — obvious: VP marketing, retention team. Hidden: the CRM
data steward (access approvals — L04 role), legal-privacy (record-level data
rules, CS-100's collision), call-center team leads (their scripts absorb the
model's output; skip them and the intervention dies), the pricing team (whose
offers interact with retention offers), and the customers' union/advocates if
retention offers differ systematically across groups.

## Worked example

**Grid → strategy derivation (board, then small groups):**

| Stakeholder | Power | Interest | Quadrant | Current→Desired | Smallest move |
|---|---|---|---|---|---|
| Data steward | High | Low (today) | Keep satisfied | Neutral→Supportive | 20-min access-rules briefing; invite to gate |
| Call-center leads | Medium | High | Keep informed | Resistant→Neutral | Shadow one shift; show triage benefit |
| Regulator/audit | High | Low–var | Keep satisfied | Unaware→Supportive | Early documentation-gate walkthrough |
| VP marketing | High | High | Manage closely | Supportive→Leading | Co-own one success metric |

Teach the reading: *keep satisfied* is about **surprise prevention** — the
steward who blocks ingestion in week 12 was never engaged in week 1. Movement
costs money and time; that is why the *smallest* move column exists.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "We identified stakeholders once — done." | Engagement states drift; the register refreshes on change, at minimum monthly. |
| "High power + low interest can be ignored until needed." | They are your ambush risk; satisfaction costs less than surprise. |
| "More communication = better engagement." | Targeted movement beats volume; resistant stakeholders get dialogue, not newsletters. |
| "Users are one stakeholder." | Segments differ (students vs advisors vs help desk); aggregate registers produce useless strategies. |

## Classroom activities

1. **CS-09 hunt (30 min):** competitive hidden-stakeholder hunt; scoring
   rewards non-obvious finds with a one-line "why they matter."
2. **CS-10 grid + hostile plan (30 min):** place 15 on the grid; write
   engagement plans for the three most hostile, each naming the *trade* that
   changes their incentive.
3. **Register autopsy (10 min):** hand out a real-world register that lists
   names but no actions; teams fix it in four minutes.

## Discussion questions

1. Who are the hidden stakeholders of *your capstone idea* — and which one would you fear most at the defense?
2. A hostile stakeholder has a legitimate point. How does the plan change when resistance is justified rather than political?
3. When does stakeholder engagement itself become scope creep? (Seeds L09/L20.)

## Practical exercise

**In class:** CS-09 + CS-10 deliverables (register + grid + hostile plans).
**Take home (20 min):** run the hidden-stakeholder hunt on your own capstone
idea (≥ 8 stakeholders, ≥ 3 hidden), bring to L08 team formation — teams merge
individual hunts into the team register.

## Formative assessment (exit ticket)

1. Name two quadrants of the power/interest grid and the strategy for one.
2. Why does the register need a refresh cadence?
3. One hidden stakeholder from the CS-09 hunt you would never have found alone.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Stakeholders Performance Domain.
- [Templates](../../../docs/resources/templates.md): stakeholder register +
  grid skeleton (Lab 2 material).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the stakeholder who killed the project in week 12 | — |
| 0:10–0:30 | Identification techniques; hidden-stakeholder doctrine | hunt rules |
| 0:30–0:50 | Grid + engagement matrix; movement logic | grid handout |
| 0:50–1:00 | Break | |
| 1:00–1:30 | CS-09 competitive hunt | CS-09 brief |
| 1:30–1:55 | CS-10 grid + hostile engagement plans | CS-10 brief |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Score the hunt on *distinct non-obvious* finds to prevent list inflation.
- Pre-mark your own 15-stakeholder answer including 5 hidden ones; keep the
  reveal for the debrief.
- Lab 2 runs this week on the same material — lab = students' own project,
  lecture = MEDSYNC.

## Linked resources

- Lecture skeleton: [`docs/lectures/L07`](../../../docs/lectures/L07-07-stakeholders.md)
- Cases: [CS-09](../../../docs/cases/CS-09.md) · [CS-10](../../../docs/cases/CS-10.md)
- Template: [register + grid](../../../docs/resources/templates.md) ·
  Lab 2: [labs index](../../../docs/labs/index.md)
- Forward: [communication L26](../../../docs/lectures/L26-26-communication-negotiation.md)
  turns the register into a cadence plan.
