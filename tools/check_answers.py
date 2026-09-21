#!/usr/bin/env python3
"""
check_answers.py — independently verify every CAMPUS-MEND calculation.

Recomputes each number from the raw inputs in docs/labs/data-pack.md (via
the machine-readable CSVs) and compares against the instructor answer keys.
Nothing is trusted: totals are summed from rows, indices re-derived, the
CPM pass re-executed from the schedule, and the Monte Carlo re-run against
its pinned reference.

Checks:
  A  Budget chain       labor from hours x rates -> baseline (5 internal tests)
  B  Labor hours        role totals + grand total
  C  CPM pass           full forward/backward re-execution vs answer key
  D  Risk scores        score = max(S,C,Q)*P and bands vs answer key
  E  EVM set            CV/SV/CPI/SPI/EAC1/EAC2/ETC/TCPI vs answer key
  F  Sprint capacity    chain + committed <= point capacity
  G  Monte Carlo        re-run sim, compare to pinned reference JSON
  H  Reference hygiene  no answer-key data in student templates

Usage:  python tools/check_answers.py
Exit 0 = all checks pass; exit 1 = failures listed.
"""
from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "templates" / "data"
KEYS = ROOT / "instructor" / "lab-solutions" / "data"

failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def read_rows(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as fh:
        rows = [r for r in csv.reader(fh) if r and not r[0].lstrip().startswith("#")]
    header = [h.strip() for h in rows[0]]
    return [dict(zip(header, [c.strip() for c in row])) for row in rows[1:]]


def close(a: float, b: float, tol: float = 0.01) -> bool:
    return abs(a - b) <= tol


def get(rows: list[dict], key_col: str, key_val: str, val_col: str) -> str:
    for r in rows:
        if r[key_col] == key_val:
            return r[val_col]
    return ""


# ── A. Budget chain ─────────────────────────────────────────────────────────
def check_budget() -> None:
    hours = read_rows(DATA / "campus-mend-hours.csv")
    total_row = next(r for r in hours if r["package_id"] == "TOTAL")
    dev, qa, de, pm = (float(total_row[c]) for c in
                       ("dev_hours", "qa_hours", "de_hours", "pm_hours"))
    if dev != 864 or qa != 480 or de != 368 or pm != 96:
        fail(f"A hours-sheet totals dev={dev} qa={qa} de={de} pm={pm} — "
             "must be 864/480/368/96")
    sum_dev = sum(float(r["dev_hours"]) for r in hours if r["package_id"] != "TOTAL")
    sum_qa = sum(float(r["qa_hours"]) for r in hours if r["package_id"] != "TOTAL")
    sum_de = sum(float(r["de_hours"]) for r in hours if r["package_id"] != "TOTAL")
    sum_pm = sum(float(r["pm_hours"]) for r in hours if r["package_id"] != "TOTAL")
    if (sum_dev, sum_qa, sum_de, sum_pm) != (dev, qa, de, pm):
        fail(f"A package rows sum to {sum_dev}/{sum_qa}/{sum_de}/{sum_pm} "
             f"but TOTAL row says {dev}/{qa}/{de}/{pm}")

    labor = dev * 1800 + qa * 1200 + de * 2400 + pm * 2200
    indirect = 0.25 * labor
    direct = 40_000 + 48_000
    subtotal = labor + indirect + direct
    contingency = 0.10 * subtotal
    baseline = subtotal + contingency
    mr = 0.05 * baseline
    ask = baseline + mr

    budget = read_rows(DATA / "campus-mend-budget.csv")
    expect = {
        "Labor": labor,
        "Indirects (25% of labor)": indirect,
        "Direct costs (licenses + GPU)": direct,
        "Subtotal": subtotal,
        "Contingency (10% of subtotal)": contingency,
        "Cost baseline": baseline,
    }
    for line, want in expect.items():
        got = float(get(budget, "line", line, "amount_pkr"))
        if not close(got, want, tol=1.0):
            fail(f"A budget '{line}': sheet {got:,.0f} vs computed {want:,.0f}")
    if not close(mr, 226_600, tol=1) or not close(ask, 4_758_600, tol=1):
        fail(f"A MR/ask: computed {mr:,.0f}/{ask:,.0f} — data pack says "
             "226,600 / 4,758,600")


# ── B. Labor hours per role (redundant-independence check) ──────────────────
def check_labor_key() -> None:
    # per-package cost table printed in lab-07 key must re-derive exactly
    per_pkg = {"A": 113_600, "B": 281_600, "C": 724_800, "D": 746_400,
               "E": 554_400, "F": 299_200, "G": 377_600, "H": 128_000}
    hours = read_rows(DATA / "campus-mend-hours.csv")
    for r in hours:
        pid = r["package_id"]
        if pid == "TOTAL":
            continue
        cost = (float(r["dev_hours"]) * 1800 + float(r["qa_hours"]) * 1200 +
                float(r["de_hours"]) * 2400 + float(r["pm_hours"]) * 2200)
        if not close(cost, per_pkg[pid], tol=1):
            fail(f"B package {pid} cost {cost:,.0f} vs key {per_pkg[pid]:,}")


# ── C. CPM pass re-execution ────────────────────────────────────────────────
def check_cpm() -> None:
    sched = read_rows(DATA / "campus-mend-schedule.csv")
    tasks = {}
    for r in sched:
        preds = [p.strip() for p in r["predecessors"].split(",") if p.strip()]
        tasks[r["id"]] = {"preds": preds, "dur": float(r["duration_weeks"])}
    order, perm = [], set()

    def visit(t):
        if t in perm:
            return
        for p in tasks[t]["preds"]:
            visit(p)
        perm.add(t)
        order.append(t)

    for t in tasks:
        visit(t)

    es, ef = {}, {}
    for t in order:
        es[t] = max((ef[p] for p in tasks[t]["preds"]), default=0.0)
        ef[t] = es[t] + tasks[t]["dur"]
    finish = max(ef.values())
    succs = {t: [] for t in tasks}
    for t in tasks:
        for p in tasks[t]["preds"]:
            succs[p].append(t)
    ls, lf = {}, {}
    for t in reversed(order):
        lf[t] = min((ls[s] for s in succs[t]), default=finish)
        ls[t] = lf[t] - tasks[t]["dur"]

    key = read_rows(KEYS / "campus-mend-cpm-answers.csv")
    if len(key) != len(sched):
        fail(f"C answer-key rows {len(key)} != schedule rows {len(sched)}")
        return
    for k in key:
        t = k["id"]
        if not close(float(k["es"]), es[t], 0.01):
            fail(f"C {t} ES key {k['es']} vs computed {es[t]}")
        if not close(float(k["ef"]), ef[t], 0.01):
            fail(f"C {t} EF key {k['ef']} vs computed {ef[t]}")
        if not close(float(k["ls"]), ls[t], 0.01):
            fail(f"C {t} LS key {k['ls']} vs computed {ls[t]}")
        if not close(float(k["lf"]), lf[t], 0.01):
            fail(f"C {t} LF key {k['lf']} vs computed {lf[t]}")
        tf = ls[t] - es[t]
        if not close(float(k["total_float"]), tf, 0.01):
            fail(f"C {t} TF key {k['total_float']} vs computed {tf}")
        ff = min((es[s] for s in succs[t]), default=finish) - ef[t]
        if not close(float(k["free_float"]), ff, 0.01):
            fail(f"C {t} FF key {k['free_float']} vs computed {ff}")
        crit = "TRUE" if abs(tf) < 1e-9 else "FALSE"
        if k["critical"].upper() != crit:
            fail(f"C {t} critical key {k['critical']} vs computed {crit}")
    if not close(finish, 17.0, 0.01):
        fail(f"C project finish {finish} != 17 weeks")


# ── D. Risk scores ──────────────────────────────────────────────────────────
def check_risks() -> None:
    key = read_rows(KEYS / "campus-mend-risk-answers.csv")
    bands = {"Low": (0, 5), "Medium": (6, 11), "High": (12, 15),
             "Critical": (16, 25)}
    for r in key:
        p, s, c, q = (float(r[k]) for k in
                      ("P", "S_impact", "C_impact", "Q_impact"))
        score = max(s, c, q) * p
        if not close(score, float(r["score"])):
            fail(f"D {r['risk_id']} score key {r['score']} vs computed {score}")
        band = next(b for b, (lo, hi) in bands.items() if lo <= score <= hi)
        if r["band"] != band:
            fail(f"D {r['risk_id']} band key {r['band']} vs computed {band}")
    seed = read_rows(DATA / "campus-mend-risks.csv")
    seed_map = {r["risk_id"]: r for r in seed if r.get("P")}
    for r in key:
        s = seed_map.get(r["risk_id"])
        if not s:
            fail(f"D key row {r['risk_id']} missing from student seed CSV")
            continue
        for col in ("P", "S_impact", "C_impact", "Q_impact"):
            if s[col] != r[col]:
                fail(f"D {r['risk_id']} {col} seed {s[col]} vs key {r[col]}")


# ── E. EVM set ──────────────────────────────────────────────────────────────
def check_evm() -> None:
    status = read_rows(DATA / "campus-mend-status-wk9.csv")
    pv = float(get(status, "metric", "PV", "value_pkr"))
    ev = float(get(status, "metric", "EV", "value_pkr"))
    ac = float(get(status, "metric", "AC", "value_pkr"))
    bac = 4_532_000.0

    want = {
        "CV": ev - ac,
        "SV": ev - pv,
        "CPI": round(ev / ac, 4),
        "SPI": round(ev / pv, 4),
        "EAC1": round(bac / (ev / ac)),
        "EAC2": ac + (bac - ev),
        "ETC1": round(bac / (ev / ac)) - ac,
        "TCPI_to_BAC": round((bac - ev) / (bac - ac), 4),
    }
    key = read_rows(KEYS / "campus-mend-evm-answers.csv")
    for metric, w in want.items():
        g = get(key, "metric", metric, "value")
        if not g:
            fail(f"E answer key missing {metric}")
            continue
        tol = 0.0005 if metric in ("CPI", "SPI", "TCPI_to_BAC") else 1.0
        if not close(float(g), float(w), tol):
            fail(f"E {metric}: key {g} vs computed {w}")


# ── F. Sprint capacity ──────────────────────────────────────────────────────
def check_sprint() -> None:
    backlog = read_rows(DATA / "campus-mend-backlog.csv")
    total_pts = sum(float(r["points"]) for r in backlog
                    if not r["item_id"].startswith("#"))
    if total_pts != 66:
        fail(f"F backlog totals {total_pts} pts, expected 66")

    gross = 4 * 2 * 10
    after_abs = gross - 6
    after_focus = after_abs * 0.7
    build = after_focus - 5.7
    pts_cap = int(build / 1.4)

    key = read_rows(KEYS / "campus-mend-sprint-answers.csv")
    expect = {"gross_hours": gross, "hours_after_absence": after_abs,
              "hours_after_focus": after_focus, "ceremony_hours": 5.7,
              "build_capacity_hours": build, "point_capacity": pts_cap}
    for metric, w in expect.items():
        g = get(key, "metric", metric, "value")
        if not g or not close(float(g), float(w), 0.01):
            fail(f"F {metric}: key {g} vs computed {w}")

    committed = [r for r in read_rows(KEYS / "campus-mend-sprint-answers.csv")
                 if False]  # placeholder no-op
    # committed points must be <= capacity (model answer row)
    model = get(key, "metric", "committed_points", "value")
    if not model or float(model) > pts_cap:
        fail(f"F committed_points {model} exceeds capacity {pts_cap}")


# ── G. Monte Carlo vs pinned reference ─────────────────────────────────────
def check_simulation() -> None:
    ref_path = KEYS / "campus-mend-sim-reference.json"
    ref = json.loads(ref_path.read_text(encoding="utf-8"))
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "campus_mend_sim.py")],
        capture_output=True, text=True, cwd=ROOT,
    )
    if proc.returncode != 0:
        fail(f"G simulation re-run failed: {proc.stderr.strip()[:200]}")
        return
    fresh = json.loads(ref_path.read_text(encoding="utf-8"))
    for field in ("mean_weeks", "p50_weeks", "p80_weeks", "p90_weeks",
                  "p95_weeks", "prob_on_time", "stdev_weeks"):
        if fresh[field] != ref[field]:
            fail(f"G simulation drift: {field} {fresh[field]} vs pinned {ref[field]}")
    if fresh != ref:
        fail("G reference JSON rewritten with different content")
    # restore: ensure the pinned file is unchanged on disk
    ref_path.write_text(json.dumps(ref, indent=2) + "\n", encoding="utf-8")


# ── H. Student templates must not leak answer data ─────────────────────────
def check_no_leak() -> None:
    banned = [
        ("docs/templates/data/cpm-pass-worksheet.csv",
         [str(v) for v in (7, 11, 14, 16, 9, 12)]),
        ("docs/templates/data/evm-status-wk9.csv",
         ["0.8633", "0.8697", "5250000", "4811000", "1.1118", "-279000"]),
        ("docs/templates/data/sprint-plan-worksheet.csv",
         ["32", "IN\nB6", "OUT\nB10"]),
    ]
    for rel, needles in banned:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for needle in needles:
            if needle in text:
                fail(f"H possible answer leak in {rel}: '{needle}'")


def main() -> int:
    check_budget()
    check_labor_key()
    check_cpm()
    check_risks()
    check_evm()
    check_sprint()
    check_simulation()
    check_no_leak()
    print(f"CHECK FAIL ({len(failures)}):" if failures else
          "CHECK PASS — all calculation chains verified")
    for f in failures:
        print("  " + f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
