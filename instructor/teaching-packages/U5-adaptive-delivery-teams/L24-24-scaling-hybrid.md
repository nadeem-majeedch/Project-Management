# Lecture 24 — Scaling Frameworks & Hybrid Delivery

> **Package for:** L24 · Week 12 · Unit U5 · CLO5 · Bloom: Understand
> **Case anchor:** CS-33 (40-person program onto Scrum-of-Scrums)
> Companion: [`L24` skeleton](../../../docs/lectures/L24-24-scaling-hybrid.md) · [CS-33 brief](../../../docs/cases/CS-33.md)

## Learning objectives

1. Explain why coordination costs explode as teams multiply (dependency, integration, decision latency).
2. Apply Scrum-of-Scrums mechanics: cadence, dependency board, escalation paths.
3. Summarize SAFe's program-level structure *and* the standard critiques of framework-heavy scaling.
4. Design a hybrid delivery model for a regulated data product, choosing where gates and sprints live.

## Required prior knowledge

- L21–L23 (single-team mechanics being scaled), L20 (CCB — a scaling
  governance instrument).

## Teaching notes

Keep this lecture *Bloom: Understand* honest — it is a survey with judgment
attached, not a SAFe certification week. The teaching frame: **scaling is a
tax on communication paths.** The arithmetic hook (Metcalfe-flavored):
communication channels ≈ n(n−1)/2; two teams have 1 inter-team channel, five
teams have 10 — scaling frameworks exist to *channelize* those paths
deliberately instead of letting them happen in hallways.

Three positions to present fairly: (1) lightweight scaling (SoS + dependency
boards — most student projects' future reality), (2) framework-heavy scaling
(SAFe's program layer: PI planning, program board, release train — know the
vocabulary employers use), (3) the critique (process-for-process's-sake,
framework-first vs product-first adoption — teach students to recognize
*how* their future employers will over-adopt, and what lean questions to ask).

Hybrid design closes the arc: the L05 spectrum returns at scale — a regulated
data product with eight teams needs both gates *and* flow; CS-33's design
exercise is the synthesis.

## Definitions & concepts

- **Scrum-of-Scrums (SoS)** — team representatives meeting on cross-team
  impediments/dependencies at agreed cadence; scales to SoS-of-SoS.
- **Dependency board** — cross-team commitments made visible: who needs what
  from whom, by when; the scaling artifact that prevents hallway planning.
- **SAFe program layer (overview only)** — Agile Release Train, PI planning
  (8–12 weeks), program board with dependency strings; *the course takes no
  position on SAFe certification tracks*.
- **Critique lens** — framework adoption should start from the *problem*
  (which dependency hurts most?) not the framework diagram; ask "what decision
  does this ceremony speed up?"
- **Hybrid at scale** — predictive wrapper (fixed regulatory/release gates,
  architecture owners) + adaptive core (team sprints/flow) + explicit
  integration cadence.

## Practical examples

**CS:** a university IT program (portal + identity + CRM + help-desk): four
teams; SoS twice weekly; dependency board row: "identity team delivers SSO
test env → portal UAT blocked without it, by Apr 14". Escalation: unblocking
needs the CIO's budget decision → that is *governance*, not a standup topic
(L20/L28 echo).

**DS (GRIDSENSE, CS-33's case):** eight teams on the streaming platform:
ingestion, feature store, models ×3, dashboards, SRE, data governance.
Dependency strings concentrate around the feature-store contract (every model
team consumes it) — the program board's critical row; PI-style planning maps
to quarterly grid-compliance gates.

## Worked example

**Channel arithmetic + SoS design (board):**

- Teams: 8 → potential inter-team channels = 8×7/2 = **28**. With SoS
  (8 representatives, 1 channel each to the SoS) the *managed* path count
  drops to 8 — the framework's entire value is converting hallway chaos into
  8 governed channels.
- Dependency-board row anatomy (board): `Feature-store v2 contract → needed
  by models A/B/C → owner: FS lead → need-by: wk 34 → status: design freeze
  pending → escalation: program board, Thu`.
- Cadence budget: SoS 3×15 min/wk + program board review 1 h/wk + PI-style
  planning 2 days/quarter ≈ **< 4% of capacity** — scaling overhead is
  real but small *when ceremonies earn their keep*; the critique lens asks
  every new ceremony for its decision.

**Hybrid sketch (regulated data product):** quarterly compliance gate
(predictive: fixed evidence, external date) wrapping monthly program planning
(flow: dependency board, WIP-managed teams); architecture-runway work is
owned by named architects (predictive decision rights) inside team sprints
(adaptive execution). The hybrid tax (L05's honesty) at scale: evidence
preparation ≈ 10–15% of team capacity, planned explicitly.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Scaling = adding a framework diagram." | Scaling is managing dependencies and decisions; frameworks are one channelization strategy, adopted from problems, not posters. |
| "More teams = proportionally faster." | Coordination overhead grows quadratically; adding teams late often *slows* delivery (Brooks-flavored). |
| "SAFe is evil / SAFe is salvation." | Both are lazy; judge ceremonies by the decisions they speed up, and know the vocabulary either way — employers will use it. |
| "Hybrid at scale means some teams agile, some waterfall." | It means the *delivery system* deliberately assigns gates and flow where each fits; team-level methods stay coherent inside it. |
| "Dependency boards are PM theater." | They are the program's risk register for integration — the most common scaled-project failure is a dependency nobody owned. |

## Classroom activities

1. **CS-33 SoS design (35 min):** map the 8-team program: SoS cadence,
   dependency board rows (≥ 6 rows), escalation paths, capacity cost of
   ceremonies; gallery walk critique.
2. **Channel arithmetic speed-round (10 min):** channels for 2/5/8/12 teams;
   at what n do halls fail? (Students usually guess 5–6.)
3. **SAFe vocabulary match (10 min):** ten terms (ART, PI, program board...)
   matched to plain-language purposes — employability without evangelism.
4. **Critique lens drill (10 min):** given a real company's 12-ceremony
   adoption story, teams mark each ceremony "keeps/loses" with the decision
   it serves.

## Discussion questions

1. Which single dependency in CS-33 could sink the program — and what *governance* (not ceremony) fixes it?
2. Your employer adopts a heavy framework and team velocity drops 30%. What evidence would you bring to the framework review — and which L20/L22 instruments produce it?
3. Where do *ethics and data-governance decisions* live in a scaled program — which ceremony, which body? (Seeds L28: governance gates at scale.)

## Practical exercise

**In class:** CS-33 deliverable (coordination diagram + dependency rows +
escalation paths). **Take home (25 min):** scaling reflection memo (300
words): if your capstone doubled to 5 teams, what breaks first — pick one
artifact (dependency board, SoS, integration gate) and design it. Portfolio-
eligible analysis.

## Formative assessment (exit ticket)

1. Channel count for 5 teams? (10.)
2. What artifact makes cross-team commitments visible?
3. Name one SAFe program-level concept and its plain-language purpose.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Development approach & life cycle
  domain (scaling considerations); Team domain.
- Fowler, M. *The New Methodology* — method-scale context
  ([textbooks page](../../../docs/syllabus/textbooks.md); verify revision
  date when citing).
- Scrum Guide 2020 — the "Scrum but" prohibition, quoted when teams ask
  whether SoS "is Scrum".

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the 6-team hallway-coordination catastrophe | — |
| 0:10–0:28 | Channel arithmetic; SoS mechanics; dependency board | board |
| 0:28–0:45 | SAFe program layer overview + critique lens | vocabulary cards |
| 0:45–0:50 | Hybrid-at-scale sketch | — |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-33 design + gallery walk | CS-33 brief |
| 1:35–1:55 | Drills: arithmetic, vocabulary, critique | cards |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Keep SAFe coverage vocabulary-level; students who ask for depth get the
  pointer to public SAFe materials — the course's job is judgment, not
  certification prep.
- Pre-draw the CS-33 program-board skeleton with two pre-filled rows; teams
  complete ≥ 6.
- Sprint-review integration: capstone teams ran their L21 sprint — collect
  one learning per team today (feeds process evidence + L32 defense).

## Linked resources

- Lecture skeleton: [`docs/lectures/L24`](../../../docs/lectures/L24-24-scaling-hybrid.md)
- Case: [CS-33](../../../docs/cases/CS-33.md)
- Forward: [teams L25](../../../docs/lectures/L25-25-team-performance.md) —
  scaled systems still run on team health ·
  [governance L28](../../../docs/lectures/L28-28-ethics-governance.md).
