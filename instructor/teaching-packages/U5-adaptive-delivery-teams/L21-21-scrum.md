# Lecture 21 — Scrum in Practice

> **Package for:** L21 · Week 11 · Unit U5 · CLO5 · Bloom: Apply
> **Case anchors:** CS-28 (sprint planning), CS-29 (Definition of Done)
> Companion: [`L21` skeleton](../../../docs/lectures/L21-21-scrum.md) · [CS-28](../../../docs/cases/CS-28.md) · [CS-29](../../../docs/cases/CS-29.md)

## Learning objectives

1. Run the five Scrum events with their Scrum Guide 2020 purposes and timeboxes.
2. Plan a sprint from a product goal: capacity arithmetic, sprint goal, sprint backlog.
3. Write a testable Definition of Done for a team's specific context.
4. Name the classic Scrum failure modes (Scrum-but, velocity weaponization, PO-as-proxy) and their repairs.

## Required prior knowledge

- L05 (adaptive life cycle — why Scrum exists on the spectrum), L10 (story
  points and velocity as *forecast* inputs).
- Teams bring their capstone backlog seed (from L08–L09 work).

## Teaching notes

Students "know Scrum" from the internet — the teaching challenge is replacing
cargo-cult familiarity with **the Guide's actual mechanics plus the reasons
behind each event**. Teach each event by its *purpose question*: sprint
planning — "why is this sprint valuable and how will we get it done?";
daily scrum — "are we on track for the sprint goal, what's blocking?";
review — "did the increment deliver value?"; retro — "how does the team
improve?". The 2020 Guide's commitments (product goal, sprint goal,
definition of done) anchor all of it.

Capacity planning is the arithmetic core: available hours ≠ commitment.
The worked example walks focus factor, absence, ceremony load — and lands on
the sprint goal *before* the item list (goal-first planning is the anti-
"feature laundry list" discipline).

The failure-mode segment is where judgment lives: Scrum-but (mechanics kept,
commitments dropped), velocity-as-target (L10's warning returns), PO-as-proxy
(stakeholders never meet the team). Each gets a *repair*, not just a name.

## Definitions & concepts

- **Accountabilities** — Product Owner (maximize product value, owns backlog),
  Scrum Master (process health, removes impediments — *not* people manager),
  Developers (build the increment).
- **Events** — sprint (container, ≤ 1 month), planning (≤ 8 h for a month-
  sprint), daily scrum (15 min, not a status report), review (working
  increment, stakeholders present), retrospective (team process).
- **Artifacts + commitments** — product backlog → product goal; sprint
  backlog → sprint goal; increment → definition of done.
- **Capacity arithmetic** — focus factor (typ. 0.6–0.7 after meetings/
  interrupts) × available hours; absence and support duty subtract first.
- **Velocity** — historical completed points; a *forecast* input, never a
  target (L10's rule, now in team context).

## Practical examples

**CS:** capstone team (4 students, 2-week sprint): each 10 h/wk on-course →
80 person-hours × focus 0.7 ≈ 56 h; ceremony load (planning 2 h, review 1 h,
retro 1 h, dailies 5×15min ≈ 1.25 h) ≈ 5.25 h → ~50 h build capacity. Sprint
goal: "registration API passes its acceptance suite behind a flag." Items
sized from CS-14's poker results.

**DS:** churn-model sprint — the increment is *not* "a model"; it is "an
end-to-end scoring path on last month's data with gate-quality checks
passing." Discovery spikes sized as *budgeted experiments* (L10's insight);
the DoD must include the model gate items (metrics + fairness + monitoring
hook) or sprints will "complete" ungated models — the classic DS Scrum failure.

## Worked example

**Sprint planning arithmetic (board, full walk):**

| Step | Computation | Result |
|---|---|---|
| Available hours | 4 devs × 2 wk × 10 h/wk | 80 h |
| Absence (1 exam week) | −6 h | 74 h |
| Focus factor 0.7 | 74 × 0.7 | ≈ 52 h |
| Ceremony load | planning 2 + review 1 + retro 1 + dailies 1.25 | −5.25 h |
| **Build capacity** | | **≈ 46–47 h** |
| Backlog items (CS-14 points) | item set: 5+8+3+5+8+3 pts | 32 pts |
| Historical conversion | ~1.4 h/pt (team's own data) | 32 × 1.4 ≈ **45 h ✓ fits** |

Checks taught: the *goal* is written before items; the spike item (8 pts)
carries an explicit exit criterion ("auth latency measured on 1k sessions —
go/no-go for the flag rollout"); stretch item exists but is *not* committed.
The h/pt conversion is the team's own measured rate — borrowing industry
numbers (8–12 h/pt folklore) defeats the point of points.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Daily scrum = status meeting to the SM." | It is the developers' re-planning huddle around the sprint goal; status reporting is a by-product, not the purpose. |
| "Sprint review = demo to the boss." | It is a working-session inspection of the increment with stakeholders *adapting the backlog* — not applause hour. |
| "Retros are optional when busy." | The retro is the improvement engine; cutting it first guarantees the same blockers next sprint. |
| "The SM assigns tasks." | Developers self-manage; the SM owns process health, not task assignment. |
| "Scrum = no planning." | Planning concentrates *inside* the container: goal-first sprint planning, rolling backlog refinement. |

## Classroom activities

1. **CS-28 sprint planning (35 min):** goal-first planning with the capacity
   arithmetic on their own backlog; board photo = artifact.
2. **CS-29 DoD workshop (25 min):** testable DoD (≥ 5 items) for their
   context; DS teams must include gate items; trade test: "would you ship
   this to *your* users?"
3. **Failure-mode triage (15 min):** three team scenarios (Scrum-but,
   velocity-target, PO-proxy); teams diagnose + repair.

## Discussion questions

1. Your sprint goal failed mid-sprint (a spike killed the approach). What does the Guide's logic say happens — and what does cargo-cult Scrum do instead?
2. Who outside the team must attend your review for the increment to be *inspected* rather than *shown* — and what does each contribute?
3. Which DoD item will your team be tempted to skip in week 15 — and what pre-commitment prevents it?

## Practical exercise

**In class:** CS-28 + CS-29 deliverables (sprint plan + DoD poster) — both go
into the capstone process-evidence pack. **Take home (20 min):** run the two-
week sprint *for real* on the capstone (Labs 9 supports); record daily-scrum
notes twice; the review happens at L24's scaling session.

## Formative assessment (exit ticket)

1. Name the three accountabilities and one sentence each on what they own.
2. Where does capacity arithmetic start — available hours or focus factor?
3. Which commitment makes an increment "done" beyond tests passing?

## Reading & references

- Schwaber & Sutherland. (2020). *The Scrum Guide* — the whole thing; it is
  short and free (scrum.org). Required reading before class.
- PMI. (2021). *PMBOK Guide* (7th ed.) — Team domain (adaptive team
  practices).
- [Lab 9 brief](../../../docs/labs/index.md) — Scrum simulation artifact.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: "we do standups, we're agile" — the Scrum-but autopsy | — |
| 0:10–0:30 | Guide mechanics: events by purpose; commitments | guide excerpt |
| 0:30–0:50 | Worked example: capacity arithmetic, goal-first planning | board |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-28 planning + CS-29 DoD | case briefs |
| 1:35–1:50 | Failure-mode triage | scenario cards |
| 1:50–1:57 | Capstone sprint kickoff logistics | — |
| 1:57–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Require the Scrum Guide pre-reading (LMS check-quiz of 3 items opens the
  session); students without it join a parallel reading group for 15 min.
- Pre-compute the worked example for *their* team size (4) and their CS-14
  point data if available — the arithmetic should be *their* numbers.
- Process-evidence logistics: board tool access confirmed for all teams today.

## Linked resources

- Lecture skeleton: [`docs/lectures/L21`](../../../docs/lectures/L21-21-scrum.md)
- Cases: [CS-28](../../../docs/cases/CS-28.md) · [CS-29](../../../docs/cases/CS-29.md)
- Lab 9: [labs index](../../../docs/labs/index.md)
- Forward: [Kanban L22](../../../docs/lectures/L22-22-kanban-flow.md)
  (the flow alternative) · [ML sprint design CS-84 (homework lane)](../../../docs/cases/index.md).
