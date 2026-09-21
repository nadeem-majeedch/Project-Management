# Question Bank — Unit U5: Adaptive Delivery & Teams (L21–L26)

> **INSTRUCTOR ONLY — not published to the site.**
> Judgment unit: no forced calculations (per the course design — leadership
> and communication are assessed with scenario and evaluation items; the
> unit's capacity/flow arithmetic lives in QB-U3-19 and CS-28/30). Tag
> legend as in QB-U1. Anchors: CS-28/30 (arithmetic already covered),
> CS-31 (hypothesis backlog), CS-33–35, CS-93 (BATNA).

## MCQ items

### QB-U5-01 [L21 · CLO5 · Remember · F · MCQ] (1 mark)
The three Scrum accountabilities are:
A. PM, sponsor, CCB
B. Product Owner, Scrum Master, Developers
C. Architect, tester, dev lead
D. Customer, vendor, integrator

**Answer: B.**

### QB-U5-02 [L21 · CLO5 · Understand · F · MCQ] (1 mark)
A sprint backlog differs from a product backlog because it:
A. Is owned by the Product Owner
B. Is the Developers' plan for one sprint, selected and decomposed by them
C. Contains only bugs
D. Is prioritized by business value alone

**Answer: B.**

### QB-U5-03 [L22 · CLO5 · Apply · I · MCQ] (1 mark)
In Kanban, the first corrective act when cycle time rises is usually:
A. Add capacity everywhere
B. Reduce WIP limits
C. Increase story sizes
D. Skip reviews

**Answer: B.** (WIP ↑ → cycle time ↑; Little's Law logic.)

### QB-U5-04 [L23 · CLO5 · Apply · I · MCQ] (1 mark)
For an ML product, a hypothesis backlog item is strongest when it:
A. Names a model architecture
B. States a measurable prediction the experiment will confirm or refute
C. Lists hyperparameters
D. Comes from the loudest stakeholder

**Answer: B.**

### QB-U5-05 [L24 · CLO5 · Understand · F · MCQ] (1 mark)
A Scrum-of-Scrums is primarily a mechanism for:
A. Status reporting upward
B. Cross-team dependency coordination
C. Replacing sprint planning
D. HR assessment

**Answer: B.**

### QB-U5-06 [L25 · CLO5 · Understand · F · MCQ] (1 mark)
A working agreement earns its keep primarily when:
A. HR requires one
B. The team co-authors it and revisits it after conflict
C. It is imported from another team
D. It is long and complete

**Answer: B.**

### QB-U5-07 [L26 · CLO5 · Apply · I · MCQ] (1 mark)
In negotiation, your BATNA is:
A. The outcome you publicly demand
B. Your best alternative if no agreement is reached — the source of leverage
C. The compromise midpoint
D. The other party's offer

**Answer: B.**

### QB-U5-08 [L26 · CLO5 · Analyze · A · MCQ] (1 mark)
A stakeholder says "just this one small exception" to the change process.
The response that preserves both the relationship and governance is:
A. Make the exception quietly
B. Refuse flatly and cite policy
C. Route it through the process at expedited priority
D. Escalate to the sponsor immediately

**Answer: C.** (A corrupts the baseline; B burns the relationship;
D is disproportionate.)

## Scenario and evaluation items

### QB-U5-09 [L21 · CLO5 · Apply · I · short] (6 marks)
**Case anchor: CS-28.** A team commits 21 points into a sprint whose capacity
arithmetic supports 18.6. Diagnose what will happen by day 7 and the two
corrections available at sprint planning.

**Marking guide:** predicts mid-sprint carryover erosion and scope-cut
pressure (3); corrections: move a story out now (protect the goal, not the
list) or split and re-order by goal contribution (3). Accept explicit
"never extend the sprint" for full marks.

### QB-U5-10 [L22 · CLO5 · Analyze · A · numeric-light] (6 marks)
**Case anchor: CS-30.** WIP 18, throughput 6/week → cycle time 3 weeks;
target is 2. State the two levers in Little's Law terms and which one the
team controls directly.

**Answer:** CT = WIP/throughput: reach 2 weeks by WIP 12 (at throughput 6)
or throughput 9 (at WIP 18). WIP is directly controllable — pull policy,
WIP limits; throughput is an outcome of flow health, not a dial. 2 per
lever + 2 for the control insight.

### QB-U5-11 [L23 · CLO5 · Evaluate · A · case] (6 marks)
**Case anchor: CS-31.** A data-science backlog contains "improve the model"
as its top item. Rewrite it as a hypothesis item and state what evidence
would kill it.

**Marking guide:** rewritten with measurable prediction + segment + metric
(e.g., "Adding tenure as a feature will raise prepaid-segment recall from
0.30 to ≥ 0.38 on the May holdout") (3); kill evidence: experiment result
below threshold or feature-availability cost exceeding value (3).

### QB-U5-12 [L24 · CLO5 · Apply · I · short] (5 marks)
Name the two program-level gates taught in L24's scaling design and the
entry evidence for each.

**Answer:** architecture review — interface contracts for cross-team
integrations + platform capacity allocation; integration readiness —
two weeks green on nightly cross-team integration + per-team rollback
evidence. 2.5 each (evidence completeness).

### QB-U5-13 [L25 · CLO5 · Evaluate · A · case] (6 marks)
**Case anchor: CS-34.** Two engineers relitigate the same design dispute in
every review. The manager wants to "resolve it." Diagnose why forcing a
winner is the wrong first move and design the working-agreement route.

**Marking criteria:** the dispute is structural (values/trade-offs), not
informational — forcing a winner produces compliance, not agreement, and
the loser relitigates (3); route: name the trade-off in the working
agreement with a decision rule (e.g., "defaults to X unless benchmarked
otherwise; benchmark owner rotates") + review date (3).

### QB-U5-14 [L25 · CLO5 · Analyze · I · short] (5 marks)
A high performer has become a single point of failure (bus factor 1).
State the two moves that reduce the risk without alienating them, and the
one move that predictably fails.

**Answer:** works — architect/teaching role reframing expertise as legacy
(CS-96), supervised succession with verifiable handover (CS-83's retrain
standard); fails — a documentation order (produces worthless PDFs, teaches
the expert that writing is punishment). 2 + 2 + 1.

### QB-U5-15 [L26 · CLO5 · Apply · I · short] (5 marks)
**Case anchor: CS-86.** A sponsor approves nothing in under three weeks and
the team has begun treating silence as consent. Deploy the mechanism taught
in L26 and state why it works.

**Answer:** default-with-notice: "unless I hear otherwise by Thursday, we
proceed with option B" in a one-page decision memo — silence becomes a
watched decision instead of assumed consent; it ends the pattern without
confrontation because the sponsor's load drops to veto-only (3); plus
decision triage so only true sponsor decisions reach them (2).

### QB-U5-16 [L26 · CLO5 · Evaluate · A · case] (6 marks)
**Case anchor: CS-93.** Before a renewal negotiation with a vendor who
raised prices 30%, list the four elements of negotiation preparation taught
in L26 and one sentence each on why the element moves the outcome.

**Marking guide:** your BATNA, costed and dated (leverage exists only if
exit is real) (1.5); their BATNA / loss analysis (their pricing reveals
their read of your dependence) (1.5); walk-away line with rationale and a
decision date (prevents salami-sweep in the room) (1.5); opening posture +
first concession plan (trades commitment for price, not dignity for
discount) (1.5).

### QB-U5-17 [L21 · CLO5 · Understand · F · short] (3 marks)
State theDefinition of Done's function and one way it differs from a
sprint goal.

**Answer:** DoD = the quality floor every item must clear before "done"
(applies to all work); sprint goal = the single outcome that arbitrates
scope choices within one sprint (applies to the sprint). 2 + 1.

### QB-U5-18 [L24 · CLO5 · Analyze · A · case] (6 marks)
**Case anchor: CS-87.** Six teams, one platform team, quarterly commitments.
Design the minimal cadence stack: what happens at team, SoS, and quarterly
levels, and the one artifact each produces.

**Marking criteria:** team sprints → sprint board/goal (1.5); SoS twice
weekly → dependency board with need-by dates and owners (1.5); quarterly PI
planning → committed increment plan with the two gates scheduled (1.5);
the discipline claim — every added artifact must name the decision it
enables or it does not enter (1.5).

### QB-U5-19 [L25 · CLO5 · Apply · I · short] (4 marks)
Name Tuckman's stages and the leadership posture each demands.

**Answer:** forming (direct/close guidance), storming (coach conflict into
working agreements), norming (support/delegate), performing (delegate and
protect). 1 per stage+posture pair.

### QB-U5-20 [L26 · CLO5 · Evaluate · A · case] (6 marks)
**Case anchor: CS-81.** Five conflicting status stories circulate after a
failed go-live. Design the communication freeze: cadence, voice, audience
map, and the one rule that kills the side-channel stories.

**Marking guide:** single status document updated twice daily at fixed times
(2); one voice — the PM — with audience-mapped depth (registrar operational,
VC risk, students service-level) (2); every inquiry answered with the
document's link; no verbal-only updates (2).

## Quiz-extraction note

Quiz 3 (L26) draws QB-U5-01/03/06/07 MCQs + QB-U5-09 and QB-U5-15 scenario
shorts. Version B substitutes QB-U5-10 and QB-U5-17.
