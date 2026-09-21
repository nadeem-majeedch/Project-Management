<!--
Template: Gantt chart + resource allocation (Lab 5)
Part A baselines the schedule; Part B checks the plan against real capacity
and levels the overloads. A Gantt is only as honest as its resource load.
-->

# Gantt & Resource Plan — [Project name]

## Part A — Baseline Gantt (from the CPM schedule)

| Activity | Dur | ES | Weeks → (1 … 17) |
|---|---|---|---|
| A Legacy audit | 2 | 0 | ██ |
| B Schema design | 3 | 2 | ███ |
*(one █ block per week; extend to your full activity set)*

**Milestones:** | M# | name | end of week | evidence gate |
**Deadline line:** mark week [17] on the chart; note any path ending beyond it.

## Part B — Resource allocation check

Capacity per period (periods = 4-week blocks + final 1-week block, or your own):

| Period | Weeks | Dev h avail | QA h avail | DE h avail | PM h avail |
|---|---|---|---|---|---|
| P1 | 1–4 | | | | |
| P2 | 5–8 | | | | |
| P3 | 9–12 | | | | |
| P4 | 13–16 | | | | |
| P5 | 17 | | | | |

Load per period (sum activity hours landing in that period from §B of the
data pack, allocated by each activity's schedule):

| Period | Dev h needed | QA h needed | DE h needed | PM h needed | Over? |
|---|---|---|---|---|---|

## Part C — Levelling decisions
| Overload | Choice (delay non-critical work / split / re-sequence / add capacity) | Effect on critical path & finish | Approved? |
|---|---|---|---|

**Rules:** levelling may *not* silently move critical activities; every change
re-checks the CPM pass; record before/after finish dates.
