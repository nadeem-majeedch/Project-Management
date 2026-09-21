# Lecture 25 — Team Performance & Leadership

> **Package for:** L25 · Week 13 · Unit U5 · CLO5 · Bloom: Evaluate
> **Case anchors:** CS-34 (working agreement), CS-35 (conflict role cards)
> Companion: [`L25` skeleton](../../../docs/lectures/L25-25-team-performance.md) · [CS-34](../../../docs/cases/CS-34.md) · [CS-35](../../../docs/cases/CS-35.md)

## Learning objectives

1. Apply a team-development model (Tuckman) to diagnose where a real team is and what it needs next.
2. Draft a working agreement with observable, enforceable norms.
3. Distinguish five conflict-handling modes and select them by situation, not temperament.
4. Explain psychological safety's mechanism (learning from failure) and design one intervention.

## Required prior knowledge

- L21/L24 (the team structures being made healthy).
- Students' own (sometimes painful) group-project history — today's raw material.

## Teaching notes

**Deliberately non-quantitative.** The pedagogical challenge is the opposite
of L11/L19: students respect what they can compute and discount what they
cannot — so the session must make team dynamics *observable and arguable*,
using structured instruments (working agreement, conflict-mode cards,
safety diagnostics) rather than vibes.

Sequence: (1) Tuckman as a *diagnostic* (not destiny): what does a team need
in forming vs storming — structure vs conflict skills; (2) working agreements
as the forming-stage tool with enforceability test ("someone who never reads
this could still follow it"); (3) conflict modes as a situational repertoire
— the role-card exercise forces students out of their default mode; (4)
psychological safety as the *mechanism* behind learning-from-failure, with
the CS-90-style incident response.

The leadership content stays servant/situational and evidence-informed
without wading into pop-psychology typologies; the honest limitation
statement ("team science is contested; these instruments are practice
standards, not laws") models intellectual honesty.

## Definitions & concepts

- **Tuckman stages** — forming (orientation; needs clarity), storming
  (friction; needs conflict norms), norming (agreements emerge), performing
  (autonomy; needs challenge), adjourning (closure; needs recognition).
- **Working agreement** — the team's explicit operating norms: hours/core
  time, communication channels & response expectations, review etiquette,
  decision defaults, conflict protocol.
- **Conflict-handling modes** — compete (assert/uncooperative), collaborate
  (assert/cooperative), compromise (middle), avoid (unassert/uncoop),
  accommodate (unassert/cooperative) — *tools chosen by stakes and
  relationship*, not personality verdicts.
- **Psychological safety** — shared belief that interpersonal risk-taking
  (questions, errors, dissent) is safe here; the mechanism: error → surfacing
  → learning vs error → hiding → repetition.
- **Servant leadership** — success measured by team growth and outcomes, not
  control; situational leadership — direction/coaching style matched to
  member maturity on the task.

## Practical examples

**CS:** the capstone team two weeks in: one member silently merges unreviewed
code at midnight; another raises every concern in public channels. Diagnose:
storming + missing review norm + missing dissent norm. Working-agreement
lines: "PRs merge only after one review — no exceptions, including late
nights"; "design dissent goes to the issue thread first, meeting second."

**DS:** the churn-model team's analyst whose data-pipeline failure caused a
week's delay — publicly mocked in a review (the CS-90 scenario). The safety
mechanism analysis: next failure will be hidden → stale features → worse:
a silent quality regression. Intervention: leadership owns the "blame vs
learning" boundary explicitly; the retro runs on the *system* cause; the
incident response includes the mocked member in the fix design.

## Worked example

**Working agreement drafting with enforceability test (board):**

Vague version (fails test): "We communicate openly and respect deadlines."

Enforceable rewrite (passes):

| Norm | Observable form | Breach response |
|---|---|---|
| Core time | 10:00–14:00 overlapping; async allowed outside | Meeting-free core; exceptions announced day before |
| Review etiquette | PRs reviewed within 24 h; review comments reference criteria, not persons | Stale PR > 48 h → flagged in standup, pair-review at Friday block |
| Dissent protocol | Design objections: 1 paragraph in issue thread before the meeting | Meeting may proceed only after objection is minuted |
| Failure protocol | Deployment/data incidents: 24 h blame-free retro, system-cause focus | If blame appears, facilitator redirects to cause taxonomy |

Conflict-mode application (the second mini-example): deadline dispute where
the *stakes are low and the relationship matters* → accommodate is correct
(not weakness); architecture dispute where *stakes are high* → collaborate
with the dissent protocol above; the 2 a.m. production incident → compete
(direct command) is the *right* mode, temporarily. Choosing well = reading
stakes × relationship, then returning to the default collaborative norm.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Conflict is a sign of a bad team." | Zero conflict usually means suppressed dissent — the *unmanaged* conflict is the risk; storming is a stage to equip, not skip. |
| "Psychological safety = niceness/comfort." | It is *candor with accountability*; comfort that hides problems is the opposite. |
| "Leadership is for managers." | On student teams, leadership is who surfaces the goal, norms, and bad news first — any member. |
| "We're a small team; agreements are unnecessary." | Small teams break norms *silently* — the agreement makes the breach visible early. |
| "Personality tests tell you who should do what." | Team science is contested; use behavioral instruments (agreements, modes) over typologies. |

## Classroom activities

1. **CS-34 working agreement (30 min):** teams draft ≥ 6 norms in observable
   form + breach responses; enforceability test applied by a *different* team.
2. **CS-35 conflict role-play (35 min):** tech-debt dispute with five role
   cards (dev, tech lead, PM, sponsor voice, observer); run twice with
   different mode assignments; observers score mode-fit.
3. **Safety intervention design (15 min):** the CS-90 incident; teams write
   the leadership response: what is said publicly, what changes structurally,
   what is measured after.
4. **Tuckman diagnosis speed-round (5 min):** five team snapshots → stage +
   needed intervention.

## Discussion questions

1. Which norm in your working agreement will be tested first — and what does the breach response *actually* commit someone to do?
2. When is *competing* the right conflict mode on a student team, and how do you repair the relationship afterward?
3. What does your team's last failure reveal about its safety — did the failure surface fast, and what did it cost to surface?

## Practical exercise

**In class:** CS-34 deliverable (signed agreement — real signatures; it
governs the rest of the semester). **Take home (20 min):** one-page conflict
preparation sheet for a *real* upcoming team disagreement (stakes/interests/
BATNA seed — pre-loads L26's negotiation work).

## Formative assessment (exit ticket)

1. Name Tuckman's first two stages and the intervention each needs.
2. Which conflict mode fits: high stakes, long relationship, ongoing
   collaboration? (Collaborate — with the protocol to survive it.)
3. Complete: psychological safety converts individual errors into ___.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Team Performance Domain (the
  course's canonical treatment; Tuckman reference therein).
- Scrum Guide 2020 — the team-accountability framing.
- [Glossary](../../../docs/resources/glossary.md): psychological safety,
  decision rights; [Lab 9](../../../docs/labs/index.md) DoD artifact (the
  agreement extends it).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the midnight merge (silent norm breach) | — |
| 0:10–0:25 | Tuckman as diagnostic; leadership modes | board |
| 0:25–0:50 | Working agreement anatomy + enforceability test | board table |
| 0:50–1:00 | Break | |
| 1:00–1:30 | CS-34 drafting + cross-team test | CS-34 brief |
| 1:30–1:55 | CS-35 role-play rounds + observer scoring | role cards |
| 1:55–2:00 | Exit ticket + agreement signing | slips |

## Instructor preparation notes

- Print CS-35 role cards ×5 roles ×8 teams; brief observers with the
  mode-fit scoring sheet (they are the learning engine of the role-play).
- Enforceability test rule for cross-team review: "a member who missed the
  drafting session can follow this" — kill vague norms fast.
- Emotional-safety note for you as facilitator: conflict role-plays can sting;
  de-role explicitly at the end (30 seconds, named).

## Linked resources

- Lecture skeleton: [`docs/lectures/L25`](../../../docs/lectures/L25-25-team-performance.md)
- Cases: [CS-34](../../../docs/cases/CS-34.md) · [CS-35](../../../docs/cases/CS-35.md) ·
  CS-90 (homework lane — safety incident)
- Forward: [negotiation L26](../../../docs/lectures/L26-26-communication-negotiation.md)
  (conflict prep becomes BATNA prep) · [capstone rubric](../../../docs/capstone/capstone-rubric.md)
  (team process evidence).
