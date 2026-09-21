#!/usr/bin/env python3
"""
campus_mend_sim.py — deterministic Monte Carlo schedule simulation (Lab 11).

Reads docs/templates/data/campus-mend-schedule.csv, perturbs three packages
with triangular distributions, and computes the project-finish distribution
via full topological forward passes.

Deterministic: fixed seed (42) and fixed trial count -> identical output on
every machine. The summary is stored as the Lab 11 reference answer in
instructor/lab-solutions/data/campus-mend-sim-reference.json and is re-checked
by tools/check_answers.py.

Usage:
    python tools/campus_mend_sim.py                 # print summary table
    python tools/campus_mend_sim.py --csv OUT.csv   # also write per-percentile CSV
"""
from __future__ import annotations

import argparse
import csv
import random
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEDULE = ROOT / "docs" / "templates" / "data" / "campus-mend-schedule.csv"

SEED = 42
TRIALS = 20_000
# Packages with uncertainty: (optimistic factor, most-likely factor, pessimistic factor)
# applied to the baseline duration; all other packages are deterministic.
PERTURBED = {
    "A": (0.90, 1.00, 1.40),  # sign-off can slip when legacy surprises appear
    "B": (0.85, 1.00, 1.50),  # schema work depends on how messy the legacy DB is
    "D": (0.90, 1.00, 1.30),  # analytics repo grows with data-discovery findings
}
DEADLINE_WEEKS = 17.0


def load_schedule(path: Path) -> dict[str, dict]:
    tasks: dict[str, dict] = {}
    with open(path, encoding="utf-8") as fh:
        rows = [r for r in csv.reader(fh) if r and not r[0].startswith("#")]
    header = rows[0]
    for row in rows[1:]:
        rec = dict(zip(header, row))
        preds = [p.strip() for p in rec["predecessors"].split(",") if p.strip()]
        tasks[rec["id"]] = {"name": rec["name"], "preds": preds,
                            "dur": float(rec["duration_weeks"])}
    return tasks


def toposort(tasks: dict[str, dict]) -> list[str]:
    order, temp, perm = [], set(), set()

    def visit(tid: str) -> None:
        if tid in perm:
            return
        if tid in temp:
            sys.exit(f"cycle detected involving {tid}")
        temp.add(tid)
        for p in tasks[tid]["preds"]:
            visit(p)
        temp.discard(tid)
        perm.add(tid)
        order.append(tid)

    for tid in tasks:
        visit(tid)
    return order


def finish_time(tasks: dict[str, dict], order: list[str], durations: dict[str, float]) -> float:
    finish: dict[str, float] = {}
    for tid in order:
        start = max((finish[p] for p in tasks[tid]["preds"]), default=0.0)
        finish[tid] = start + durations[tid]
    return max(finish.values())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="optional output CSV path for percentiles")
    args = parser.parse_args()

    tasks = load_schedule(SCHEDULE)
    order = toposort(tasks)

    rng = random.Random(SEED)
    results = []
    for _ in range(TRIALS):
        durations = {}
        for tid, t in tasks.items():
            base = t["dur"]
            if tid in PERTURBED:
                lo, ml, hi = PERTURBED[tid]
                durations[tid] = base * rng.triangular(lo, hi, ml)
            else:
                durations[tid] = base
        results.append(finish_time(tasks, order, durations))

    results.sort()

    def pct(p: float) -> float:
        k = (len(results) - 1) * p
        f, c = int(k), min(int(k) + 1, len(results) - 1)
        return results[f] + (results[c] - results[f]) * (k - f)

    mean = statistics.fmean(results)
    stdev = statistics.pstdev(results)
    on_time = sum(1 for r in results if r <= DEADLINE_WEEKS) / TRIALS

    summary = {
        "trials": TRIALS,
        "seed": SEED,
        "deadline_weeks": DEADLINE_WEEKS,
        "perturbed_packages": PERTURBED,
        "mean_weeks": round(mean, 2),
        "stdev_weeks": round(stdev, 2),
        "min_weeks": round(results[0], 2),
        "max_weeks": round(results[-1], 2),
        "p50_weeks": round(pct(0.50), 2),
        "p80_weeks": round(pct(0.80), 2),
        "p90_weeks": round(pct(0.90), 2),
        "p95_weeks": round(pct(0.95), 2),
        "prob_on_time": round(on_time, 4),
    }

    print("CAMPUS-MEND Monte Carlo — deterministic (seed 42, 20,000 trials)")
    print(f"Perturbed: A, B, D (triangular); deadline = {DEADLINE_WEEKS:.0f} weeks")
    print(f"mean = {summary['mean_weeks']} wk  stdev = {summary['stdev_weeks']} wk")
    print(f"P50 = {summary['p50_weeks']}  P80 = {summary['p80_weeks']}  "
          f"P90 = {summary['p90_weeks']}  P95 = {summary['p95_weeks']}")
    print(f"Prob(finish <= 17 weeks) = {summary['prob_on_time']:.4f}")
    print(f"range = {summary['min_weeks']} .. {summary['max_weeks']} weeks")

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["statistic", "weeks"])
            for k, v in summary.items():
                if k not in ("perturbed_packages",):
                    w.writerow([k, v])
        print(f"wrote {args.csv}")

    ref = ROOT / "instructor" / "lab-solutions" / "data" / "campus-mend-sim-reference.json"
    if ref.parent.exists():
        import json
        ref.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        print(f"reference written: {ref.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
