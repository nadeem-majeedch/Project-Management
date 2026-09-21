# Lecture 26 — Stakeholder Communication & Negotiation

> **Package for:** L26 · Week 13 · Unit U5 · CLO5 · Bloom: Apply/Evaluate · **Quiz 3 today (L21–L26)**
> **Case anchors:** CS-36 (scope-cut negotiation), CS-37 (bad-news delivery)
> Companion: [`L26` skeleton](../../../docs/lectures/L26-26-communication-negotiation.md) · [CS-36](../../../docs/cases/CS-36.md) · [CS-37](../../../docs/cases/CS-37.md)

## Learning objectives

1. Build a communication matrix (audience × channel × cadence × owner × purpose) for a project.
2. Apply negotiation fundamentals: interests vs positions, options, BATNA.
3. Deliver bad news early with structure: state, evidence, options, recommendation.
4. Handle the follow-up questions that follow bad news without over-promising.

## Required prior knowledge

- L07 (the register being operationalized into a communication plan), L25
  (conflict modes — negotiation is structured conflict).
- Quiz 3 runs first (L21–L26).

## Teaching notes

**Deliberately non-quantitative; rehearsal-based.** The lecture's spine:
*communication is a designed system, not a personality trait* — the matrix is
the design instrument; *negotiation is preparation, not charisma* — BATNA
analysis is the preparation instrument; *bad news is a format, not a talent* —
the four-part structure is the instrument.

Students' deepest failure mode here is silence: they discover bad news late
and deliver it late *because the conversation is scary*. The CS-37 exercise
makes the scary conversation safe to practice — twice — with observers
scoring structure, not personality. The instructor plays the steering
committee; the pushback script must be prepared (see prep notes) so the Q&A
segment generates the real experience: questions you cannot fully answer, and
the honest forms that still work ("I don't know yet; here's when you will").

The negotiation segment (CS-36) lands interests-vs-positions with the
scope-cut role-play: sponsor position "ship everything"; interests: board
credibility, specific regulatory feature, quarterly revenue narrative. The
option set that trades on interests beats positional haggling every time —
and BATNA is what lets you say no with confidence.

## Definitions & concepts

- **Communication matrix** — per audience: purpose, channel, cadence, owner,
  feedback loop; the L07 register's operational twin.
- **Interests vs positions** — the *why* behind the *what*; durable agreements
  trade on interests.
- **BATNA** — best alternative to a negotiated agreement: your walk-away
  reality; negotiated only in your head, deployed only if needed.
- **Option generation** — packages that satisfy interests asymmetrically
  (scope × schedule × money trades), presented as choices, not demands.
- **Bad-news structure** — headline → evidence → options with trade-offs →
  recommendation + decision request. No burying, no blame-first.
- **Async communication discipline** — written decisions, response-time
  norms, decision logs (distributed teams, CS-94's homework case).

## Practical examples

**CS:** portal delay communication — two weeks late on UAT entry: matrix
lines (sponsor: weekly written + immediate exception; users: milestone
bulletin), bad-news memo with three options (descope reports module / add
contractor at $X / shift date 2 weeks), recommendation: descope, because the
reports module carries the least registration benefit (evidence: benefit map
— L29 preview).

**DS:** churn-model fairness-gap breach — the bad-news conversation *upward*:
headline "we should not ship to segment B this quarter"; evidence: monitoring
trend + gate threshold; options: delay segment B / ship with narrower
audience + tighter monitoring / relax threshold (rejected — why);
recommendation: narrow ship. This is also a *governance* conversation — the
threshold was a governance decision (L23/L28), and honoring it upward is the
professional spine of the DS track.

## Worked example

**BATNA preparation sheet (board, then role-play):**

Scenario (CS-36): sponsor demands the full scope; your P80 says +6 weeks.

| Field | Content |
|---|---|
| My interests | credible delivery date; team sustainability; regulatory feature intact |
| Their likely interests | board narrative ("full scope"), a specific compliance module, quarterly revenue story |
| Options to propose | A) ship core + compliance module now, reports in +6 wks (matches board narrative + regulatory interest) · B) full scope +6 wks with weekly evidence pack · C) contractor surge (+$X, 3-wk recovery) |
| My BATNA | deliver per P80 with sponsor's written acceptance of the slip — unattractive but survivable; *their* BATNA (cancel) destroys their board narrative — they need this more than the 6 weeks |
| Reservation point | anything that sacrifices the compliance module or team sustainability |
| Opening | lead with option A framed on *their* interests |

Debrief point: BATNA strength is *analysis*, not confidence; the side with the
better-analyzed alternatives negotiates better *even with the same facts*.

**Bad-news memo skeleton (board):**

> "UAT entry slips two weeks. Evidence: integration-test trend vs plan
> (chart), root cause: schema-change rework (L11's fast-tracking cost —
> name it honestly). Options: A descope reports (recommended — least
> benefit lost, per benefit map), B surge, C date shift. Decision needed by
> Thursday to protect the release train."

Then the Q&A gauntlet: "who is accountable?", "why wasn't this seen two weeks
ago?", "what does this do to the board commitment?" — each answered with the
honest forms.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Bad news early panics stakeholders." | Late bad news removes *options*; early bad news invites help — the confidence question is about the presenter's preparation, not the news. |
| "Negotiation is about winning." | It is about durable agreements on interests; positional wins get re-litigated for months. |
| "BATNA is a threat you announce." | It is private analysis that steadies your no; announcing it turns negotiation into ultimatum. |
| "A communication plan is a distribution list." | The matrix ties every message to a purpose and a feedback loop; lists send, plans communicate. |
| "Over-promising in the crisis room is kind." | It converts one bad quarter into two; "I'll know by Friday" is the kind answer. |

## Classroom activities

1. **Quiz 3 (15 min):** L21–L26.
2. **Matrix build sprint (20 min):** communication matrix for the capstone —
   five audiences minimum, one feedback loop each.
3. **CS-36 negotiation role-play (30 min):** pairs, sponsor/PM roles, swap;
   observers score interests-usage and option packaging.
4. **CS-37 bad-news gauntlet (20 min):** memo → delivery → Q&A; instructor
   pushes twice; class scores structure adherence.

## Discussion questions

1. Whose interests in CS-36 were hardest to discover — and what question surfaced them?
2. Your BATNA is weak (you *need* this project). How do you negotiate from weakness — and what preparation replaces leverage?
3. In the DS bad-news case, what makes the "ship narrow" recommendation *governance-consistent* rather than merely cautious?

## Practical exercise

**In class:** CS-36 prep sheet + CS-37 memo (artifacts). **Take home (20
min):** write the bad-news memo you hope you'll never send for your capstone
(the most likely slip, evidence you'd cite, options) — filed with the team;
teams that *prepare* bad news deliver it faster.

## Formative assessment (exit ticket)

1. Position vs interest — one example pair from CS-36.
2. What are the four parts of the bad-news structure?
3. When do you deploy a BATNA — during, or only if talks fail?

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Stakeholders domain (communication
  dimensions); Team domain (power skills).
- PMI. (2017). *PMBOK Guide* (6th ed.) — "Plan Communications Management"
  (the matrix's canonical form).
- [Templates](../../../docs/resources/templates.md): communication matrix
  skeleton · [Lab 12 brief](../../../docs/labs/index.md) (dashboard + CCB —
  the communication plan's evidence engine).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:15 | **Quiz 3** (L21–L26) | quiz papers |
| 0:15–0:30 | Communication matrix; async discipline | matrix skeleton |
| 0:30–0:50 | Worked examples: BATNA sheet + bad-news structure | board |
| 0:50–1:00 | Break | |
| 1:00–1:30 | CS-36 role-play rounds | role cards |
| 1:30–1:50 | CS-37 gauntlet + Q&A practice | memo skeleton |
| 1:50–1:57 | Portfolio + capstone touchpoints | — |
| 1:57–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Write the sponsor pushback script (≥ 8 lines) — the gauntlet needs a
  *believable* committee; keep scoring on structure (headline → evidence →
  options → recommendation), never delivery charisma.
- Quiz 3 papers ready (blueprint in the [exam bank](../../exam-bank/README.md));
  peer-mark in session to protect activity time.
- Portfolio boundary reminder: unit-5 analyses due by L26 (3 per unit rule).

## Linked resources

- Lecture skeleton: [`docs/lectures/L26`](../../../docs/lectures/L26-26-communication-negotiation.md)
- Cases: [CS-36](../../../docs/cases/CS-36.md) · [CS-37](../../../docs/cases/CS-37.md) ·
  CS-93 (exam lane — BATNA), CS-94 (homework — remote ceremonies)
- Forward: [ethics L28](../../../docs/lectures/L28-28-ethics-governance.md)
  (honest reporting is the integrity spine) ·
  [master plan L27](../../../docs/lectures/L27-27-master-plan.md).
