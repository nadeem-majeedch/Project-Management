# Lecture 01 — Why Projects Fail: The Case for Project Management

> **Package for:** L01 · Week 1 · Unit U1 · CLO1 · Bloom: Understand
> **Case anchors:** CS-01 (iron-triangle autopsy), CS-02 (success/failure twins)
> Companion: [`L01` skeleton](../../../docs/lectures/L01-01-why-projects-fail.md) · [CS-01 brief](../../../docs/cases/CS-01.md) · [CS-02 brief](../../../docs/cases/CS-02.md)

## Learning objectives

By the end of this session students can:

1. Distinguish a project from ongoing operations using concrete criteria.
2. Name the iron-triangle constraints and explain why the triangle alone does not explain failure.
3. Map a well-known project outcome onto scope, time, cost, and quality decisions.
4. Argue what disciplined management would have changed first — with reasons.

## Required prior knowledge

- Course prerequisites only: one team-built software or data project, Git basics.
- No PM vocabulary assumed — this lecture *creates* the need for it.

## Teaching notes

This is an attitude-setting lecture, not a definitions lecture. Students arrive
believing failure is a coding problem. The session's job is to relocate the
locus of failure to decisions: unclear scope, unmanaged expectations, absent
risk work, silence about bad news.

Structure the 120 minutes around three moves:

1. **Hook (failure autopsy):** open with a large, well-documented project
   failure the class can research later. Keep the story concrete and let
   students propose causes before you impose any framework; write their causes
   on the board and hold them for later mapping onto the triangle.
2. **Definitions with contrast:** introduce *project vs operations* by sorting
   examples from both CS and DS contexts (see Practical examples below).
3. **Case work:** hand the class CS-01 and CS-02 and let them do the diagnosis;
   you facilitate rather than lecture. The debrief is where the "judgment, not
   ceremony" message lands.

Course-mechanics to announce today (first-session duty): case-portfolio rules,
quiz schedule, AI-disclosure policy pointer, and that teams rotate per unit.
Point students to [course policies](../../../docs/syllabus/course-policies.md)
and [assessment strategy](../../../docs/assessments/assessment-strategy.md).

## Definitions & concepts

- **Project** — a temporary endeavor undertaken to create a unique result
  (PMBOK 7, PMI, 2021). Temporary ≠ short; unique ≠ never done before.
- **Operations** — ongoing, repetitive work that sustains the business.
- **Iron triangle** — scope, time, cost as competing constraints, with quality
  as an output of squeezing them. Useful as a checklist, misleading as an
  explanation: most failures are *stakeholder* and *risk* failures that then
  show up as triangle symptoms.
- **Critical success factors** — the small set of conditions that reliably
  separate successful projects from failed ones (clear objectives, sponsor
  engagement, honest measurement, controlled change).

## Practical examples

**CS flavor:** a university replaces its legacy course-registration system.
Operations = running registration week each semester. Project = building and
migrating to the new system. Ask: where does "fixing a bug found during
registration week" belong? (Trick — it depends: one-off fix = operations;
a two-month rework program = project.)

**DS flavor:** a churn-model product at TelcoCare. Operations = scoring
customers nightly. Project = building the model and its pipeline. Ask: where
does quarterly retraining belong? (Boundary case — recurring work with
project-like planning needs; foreshadows L23 and MLOps.)

## Worked example

Run the **constraint coupling** demonstration on the board with hypothetical
but realistic numbers — the point is the *shape* of the argument:

> A 6-person team must deliver 30 features in 20 weeks. Marketing cuts the
> deadline to 16 weeks. Walk the triangle: cut scope to ~24 features, add
> cost (~2 people ≈ +33% payroll for those weeks), or accept quality erosion
> (compressed testing → escaped defects). Now the deeper question the triangle
> cannot answer: *which features actually carry the benefit?* That question —
> value, stakeholders, risk — is where project management actually lives, and
> the failure modes of Lecture 1 come from ignoring it.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Projects fail because developers are bad." | Failure is usually traceable to early decisions: vague objectives, unowned assumptions, suppressed bad news — before code exists. |
| "More process would have saved it." | Process is a tool; the *right amount* of process is a judgment (this course calls it tailoring, L08). |
| "Agile means no management." | Agile *changes* the management work — it does not remove scope, risk, or stakeholder decisions. |
| "Success = on time, on budget." | A delivered-on-time system nobody uses is a failure; benefits matter (L29). |

## Classroom activities

1. **Failure autopsy (25 min, teams of 4):** assign CS-01. Each team maps the
   failure onto the triangle and writes a one-paragraph root-cause hypothesis.
2. **Twin-projects contrast (20 min):** CS-02. Teams find five diverging early
   decisions between the successful and failed sibling projects.
3. **Sort line (10 min, plenary):** rapid project/operations/boundary sorting
   of ten one-line work items from CS and DS contexts.

## Discussion questions

1. Which iron-triangle constraint was *binding* in CS-01 — and who decided that?
2. Could the failed twin in CS-02 have succeeded with the same team and more process? What is the minimum change that flips the outcome?
3. Name a project you have personally watched fail. Which failure mode from today does it match? What did nobody want to say out loud?

## Practical exercise

**Take home (30–40 min):** pick any app or system you use daily. Write a
half-page "failure pre-mortem": if this system's next release fails, what will
be the binding constraint, what early decision caused it, and what would you
monitor to see it coming? Bring one sentence from it to L02.

## Formative assessment (exit ticket)

Three questions, 3 minutes, anonymous:

1. One difference between a project and operations.
2. Which triangle constraint did CS-01's autopsy reveal as binding?
3. One question about this course you still have.

Expected: students can (1) without notes; (2) with specific evidence;
(3) answers mostly about mechanics — answer them in LMS announcements.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — skim the Introduction and the
  *Foundational Elements* section: project/program/portfolio definitions.
- [Textbooks & references page](../../../docs/syllabus/textbooks.md) — the
  course reading list with access notes.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: failure story; students propose causes | board for cause list |
| 0:10–0:25 | Project vs operations; iron triangle introduced | sort-line examples |
| 0:25–0:50 | Content: constraint coupling worked example | board math |
| 0:50–1:00 | Break | |
| 1:00–1:25 | Activity 1: CS-01 autopsy in teams | CS-01 briefs |
| 1:25–1:45 | Activity 2: CS-02 twins contrast | CS-02 briefs |
| 1:45–1:55 | Debrief: judgment vs ceremony; course mechanics | syllabus pointers |
| 1:55–2:00 | Exit ticket | slips or poll |

## Instructor preparation notes

- Choose the hook failure **before** the session and check current public
  reporting on it; do not improvise statistics from memory.
- Print or link CS-01/CS-02 briefs; review facilitation notes in
  [answer keys](../../answer-keys/README.md) after first authoring.
- Prepare the course-mechanics announcements (portfolio cadence, quiz dates).
- Decide team assignments for Unit 1 case teams (rotation explained today).

## Linked resources

- Lecture skeleton: [`docs/lectures/L01`](../../../docs/lectures/L01-01-why-projects-fail.md)
- Cases: [CS-01](../../../docs/cases/CS-01.md) · [CS-02](../../../docs/cases/CS-02.md) · [directory](../../../docs/cases/index.md)
- Policies: [course policies](../../../docs/syllabus/course-policies.md) · [integrity & AI](../../../docs/assessments/academic-integrity.md)
- Grading context: [assessment strategy](../../../docs/assessments/assessment-strategy.md)
- Lab link: none this week; first lab (charter drafting) is Lab 1 in week 3.
