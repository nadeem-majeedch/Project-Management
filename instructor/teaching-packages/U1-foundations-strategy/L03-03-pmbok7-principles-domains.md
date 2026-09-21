# Lecture 03 — PMBOK Guide 7: Principles & Performance Domains

> **Package for:** L03 · Week 2 · Unit U1 · CLO1 · Bloom: Understand
> **Case anchor:** CS-04 (sorting 20 artifacts into the 8 domains)
> Companion: [`L03` skeleton](../../../docs/lectures/L03-03-pmbok7-principles-domains.md) · [CS-04 brief](../../../docs/cases/CS-04.md)

## Learning objectives

1. Name the twelve principles and eight performance domains of PMBOK 7.
2. Classify real project artifacts into the correct performance domain.
3. Explain why PMI moved from 49 processes (6th ed.) to principles + domains (7th ed.).
4. Use PMBOK 6 process vocabulary alongside PMBOK 7 domains when needed.

## Required prior knowledge

- L01–L02 vocabulary (project, portfolio, life cycle).
- Awareness that standards exist and differ in framing (today deepens it).

## Teaching notes

This is the course's **vocabulary backbone** — but teaching 20 framework items
as a list would be dead on arrival. Teach it as a *map for navigation*: the
domains answer "what am I responsible for?" and the principles answer "how do
I act when the standard doesn't cover my case?"

Sequence: (1) the story of the change — 6th edition's 49 processes were
tunable but prescriptive; 7th edition hands practitioners principles and says
"tailor" (this sets up L08); (2) the eight domains as a walk around a project
in time; (3) principles as lenses with a fast matching drill; (4) CS-04 as the
consolidation activity. Reassure students they will *not* memorize this list —
they will use it, and the midterm tests usage, not recitation.

Keep the 6th-edition bridge honest: recruiters, certification exams, and most
job descriptions still speak process language (stakeholder management,
procurement management...). The course uses 7th-edition structure with 6th-ed
vocabulary where useful — the [detailed syllabus](../../../docs/syllabus/detailed-syllabus.md)
knowledge areas do exactly this.

## Definitions & concepts

**Twelve principles (PMBOK 7, PMI, 2021)** — stewardship; team;
stakeholders; value; systems thinking; leadership; tailoring; quality;
complexity; risk; adaptability & resilience; change.

**Eight performance domains:**

| Domain | Answers the question |
|---|---|
| Stakeholders | Who matters, and how do we keep them engaged? |
| Team | How does the team perform? |
| Development approach & life cycle | How do we build this — predictive, adaptive, hybrid? |
| Planning | How are the pieces organized in time and logic? |
| Project work | How does the work get done and kept on track? |
| Delivery | How do requirements and scope become accepted value? |
| Measurement | How do we know how we're doing? |
| Uncertainty | How do we handle risk, ambiguity, volatility? |

- **Model / method / artifact** — PMBOK 7's three tool shelves: mental models
  (e.g., systems thinking), methods (e.g., estimation techniques), artifacts
  (e.g., risk register). Domains *use* artifacts; they are not artifacts.

## Practical examples

**CS:** a registration-system rewrite — charter (stakeholders domain), sprint
board (project work), test plan (delivery), burn-down (measurement), risk
register (uncertainty). Ask where the *WBS dictionary* lives: planning —
but the acceptance criteria inside it are delivery. Artifacts serve domains,
and a large artifact serves several.

**DS:** churn-model project — data-quality rules (delivery), model-risk gate
(uncertainty + delivery), experiment log (project work), fairness report
(delivery + measurement). Point out data projects lean hard on *uncertainty*
and *measurement* domains — foreshadowing the DS spine.

## Worked example

**Artifact-to-domain sorting (board demonstration with five items):**

1. *Stakeholder engagement assessment matrix* → Stakeholders.
2. *Monte Carlo S-curve of schedule outcomes* → Uncertainty (and Measurement
   when used for forecasts). The honest answer is "primary + secondary":
   force the class to argue primary purpose.
3. *Definition of Done poster* → Delivery? Project work? Better: Team (it is
   a shared team commitment governing how work completes) — a deliberate
   judgment call to show the map is a tool, not a cage.
4. *Procurement SOW* → Project work (and Delivery at acceptance).
5. *Model card* → Delivery + Measurement; also *Uncertainty* (known
   limitations). A data artifact straddling three domains is normal.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "PMBOK 7 replaced PMBOK 6, so processes are dead." | PMI retired the *standard*, not the vocabulary; 6th-ed process names remain the profession's lingua franca. |
| "Principles are just decoration; I need templates." | Principles are what you fall back on when templates don't fit — which is most novel projects. |
| "Each artifact belongs to exactly one domain." | Artifacts serve multiple domains; the map aids thinking, it is not a filing system. |
| "The domains run in sequence like phases." | They are *concurrent* areas of focus, not stages. |

## Classroom activities

1. **CS-04 sorting sprint (30 min):** 20 artifact cards, teams place them in
   the 8 domains and must *defend two judgment calls in writing*.
2. **Principle matching drill (15 min):** twelve one-line situations, teams
   name the governing principle — fast, loud, competitive.
3. **6th/7th bridge (10 min):** give ten process names ("plan risk
   management", "control procurements"); teams place each in a domain.

## Discussion questions

1. Which domain do data projects lean on hardest, and why?
2. If you could only instrument one domain with metrics, which and why?
3. Where does the principle of *stewardship* collide with a sponsor's instruction? (Seeds L28.)

## Practical exercise

**Take home (30 min):** map **five artifacts from your own past project** to
domains, marking primary + secondary, with a one-line defense each. Portfolio-
eligible concept practice (not a submission).

## Formative assessment (exit ticket)

1. Name any four of the eight domains.
2. Which domain does a *risk register* primarily serve?
3. Why did PMI shift from processes to principles?

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Sections 2–3 (principles) and the
  performance-domain chapters; skim, do not memorize.
- PMI. (2017). *PMBOK Guide* (6th ed.) — Table of Contents only, to see the
  49-process structure being bridged.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:08 | Hook: "your new job hands you 49 process templates..." | — |
| 0:08–0:30 | Story of the change; principles as lenses | principle cards |
| 0:30–0:50 | Eight domains walked around a project in time | domain wall chart |
| 0:50–1:00 | Break | |
| 1:00–1:30 | CS-04 sorting sprint | CS-04 card deck |
| 1:30–1:45 | Debrief: contested placements argued out | team answer sheets |
| 1:45–1:55 | Principle drill + 6th/7th bridge | drill slides |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Print the artifact card deck (20 cards, one per item from CS-04's YAML
  definition) or run it digitally if the room has boards.
- Rehearse the contested placements (DoD, model card) — students will argue;
  the goal is reasoning quality, not your answer.
- Midterm blueprint note: 3–4 items test domain usage via vignettes.

## Linked resources

- Lecture skeleton: [`docs/lectures/L03`](../../../docs/lectures/L03-03-pmbok7-principles-domains.md)
- Case: [CS-04](../../../docs/cases/CS-04.md)
- Vocabulary: [glossary](../../../docs/resources/glossary.md) ·
  [standards library](../../../docs/resources/standards-library.md)
- Forward: [tailoring L08](../../../docs/lectures/L08-08-tailoring.md) — where
  principles get applied to a real template cut.
