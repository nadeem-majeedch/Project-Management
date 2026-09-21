#!/usr/bin/env python3
"""
check_cases.py — machine validation for the 105-case collection.

What it checks
  A. Structure   band files merge to exactly CS-01..CS-105, band ranges match
                 meta, schema keys complete, difficulty matches band,
                 numerical flag consistent, substantive solution text.
  B. Numbers     every numeric block is recomputed from its own data block:
                 - `arith`/`steps` blocks: each step expression is evaluated
                   (previous steps available by name) and compared to
                   `expect` within `tol`.
                 - structured blocks (portfolio_score, wbs_rollup,
                   pert_calibration, cpm, budget, pxi, histogram_stats,
                   contract_fpif, evm, crash, leveling): every value in
                   `expected` is recomputed and compared.

Usage: python tools/check_cases.py     → exit 0 = all pass; exit 1 = failures
"""
from __future__ import annotations

import glob
import itertools
import math
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "planning" / "cases"
META_FILE = ROOT / "planning" / "case-catalog.yaml"

failures: list[str] = []
stats = {"cases": 0, "numeric": 0, "checks": 0}

SCHEMA_KEYS = {
    "id", "title", "domain", "level", "use", "lecture", "seed", "difficulty",
    "numerical", "tags", "concepts", "summary", "context", "problem",
    "constraints", "tasks", "deliverables", "discussion", "objectives",
    "rubric", "solution",
}
BANDS = {
    "band-1-beginner.yaml": ("beginner", 1, 20),
    "band-2-intermediate.yaml": ("intermediate", 21, 45),
    "band-3-advanced.yaml": ("advanced", 46, 75),
    "band-4-expert.yaml": ("expert", 76, 105),
}


def fail(msg: str) -> None:
    failures.append(msg)


def close(computed, expect, tol) -> bool:
    try:
        return abs(float(computed) - float(expect)) <= float(tol) + 1e-9
    except (TypeError, ValueError):
        return computed == expect


def fmt(v) -> str:
    return str(v)


# ── namespace wrapper so dotted paths (P1.bac, good.p) evaluate ─────────────
class NS:
    def __init__(self, d: dict):
        for k, v in d.items():
            setattr(self, k, NS(v) if isinstance(v, dict) else v)


SAFE_GLOBALS = {
    "__builtins__": {},
    "max": max, "min": min, "abs": abs, "round": round, "sum": sum,
    "len": len, "int": int, "float": float,
    "sqrt": math.sqrt, "exp": math.exp, "log": math.log, "pow": pow,
}


def eval_steps(case_id: str, block: dict) -> None:
    # expose top-level data keys as bare names; nested dicts stay attribute-accessible
    names: dict = {}
    for k, v in block["data"].items():
        names[k] = NS(v) if isinstance(v, dict) else v
    results: dict = {}
    for step in block["steps"]:
        name = step["name"]
        try:
            val = eval(step["expr"], dict(SAFE_GLOBALS), {**names, **results})  # noqa: S307
        except Exception as exc:  # noqa: BLE001
            fail(f"{case_id}: step {name!r} crashed: {exc}")
            continue
        results[name] = val
        stats["checks"] += 1
        if not close(val, step["expect"], step["tol"]):
            fail(
                f"{case_id}: step {name!r} = {fmt(val)} but key says {fmt(step['expect'])}"
                f" (tol {step['tol']})"
            )


# ── structured evaluators ───────────────────────────────────────────────────
def check_expected(case_id: str, expected: dict, computed: dict) -> None:
    for key, exp in expected.items():
        stats["checks"] += 1
        got = computed.get(key, "<missing>")
        if isinstance(exp, dict):
            for k2, v2 in exp.items():
                stats["checks"] += 1
                g2 = got.get(k2, "<missing>") if isinstance(got, dict) else "<missing>"
                if not close(g2, v2, max(abs(float(v2)) * 1e-4, 0.001) if isinstance(v2, (int, float)) else 0):
                    fail(f"{case_id}: {key}.{k2} = {fmt(g2)} but key says {fmt(v2)}")
        elif isinstance(exp, list):
            if sorted(map(str, got)) != sorted(map(str, exp)):
                fail(f"{case_id}: {key} = {got} but key says {exp}")
        else:
            tol = max(abs(float(exp)) * 1e-4, 0.001) if isinstance(exp, (int, float)) else 0
            if not close(got, exp, tol):
                fail(f"{case_id}: {key} = {fmt(got)} but key says {fmt(exp)}")


def ev_portfolio_score(d: dict) -> dict:
    w, projs = d["weights"], d["projects"]
    scores = {p["id"]: round(w["alignment"] * p["alignment"] + w["impact"] * p["impact"]
                             + w["feasibility"] * p["feasibility"], 1) for p in projs}
    best, best_score = None, -1.0
    for r in range(1, len(projs) + 1):
        for combo in itertools.combinations(projs, r):
            cost = sum(p["cost_m"] for p in combo)
            if cost <= d["budget_m"] + 1e-9:
                sc = sum(scores[p["id"]] for p in combo)
                if sc > best_score + 1e-9 or (abs(sc - best_score) <= 1e-9 and cost < (best[1] if best else 1e9)):
                    best, best_score = (combo, cost), sc
    vpm = {p["id"]: round(scores[p["id"]] / p["cost_m"], 4) for p in projs}
    return {"scores": scores,
            "optimal_bundle": sorted(p["id"] for p in best[0]),
            "optimal_total_score": round(best_score, 1),
            "optimal_total_cost_m": round(best[1], 1),
            "value_per_m": vpm}


def ev_wbs_rollup(d: dict) -> dict:
    dh = {dl["name"]: sum(dl["packages"].values()) for dl in d["deliverables"]}
    return {"deliverable_hours": dh,
            "project_total_hours": sum(dh.values()),
            "duplicate_resolutions": {x["package"]: x["newest"] for x in d["duplicate_estimates"]}}


def ev_pert_calibration(d: dict) -> dict:
    means = {it["id"]: round((it["O"] + 4 * it["M"] + it["L"]) / 6, 2) for it in d["items"]}
    te = round(sum(means.values()), 2)
    ta = round(sum(it["actual"] for it in d["items"]), 2)
    bias = ta / te
    return {"pert_means": means, "total_estimate": te, "total_actual": ta,
            "bias_ratio": round(bias, 3),
            "recommended_correction": round(round(bias * 20) / 20, 2)}  # practical 0.05 steps


def ev_cpm(d: dict) -> dict:
    acts = {a["id"]: a for a in d["activities"]}
    lag_of = lambda a, p: a.get("lags", {}).get(p, 0)  # noqa: E731
    es, ef = {}, {}
    for a in d["activities"]:  # band files list predecessors before successors
        es[a["id"]] = max((ef[p] + lag_of(a, p) for p in a["preds"]), default=0)
        ef[a["id"]] = es[a["id"]] + a["dur"]
    dur = max(ef.values())
    succs = {i: [] for i in acts}
    for a in d["activities"]:
        for p in a["preds"]:
            succs[p].append(a["id"])
    lf, ls = {}, {}
    for a in reversed(d["activities"]):
        # terminal activities finish at project end; else min over lag-adjusted successor LS
        lf[a["id"]] = min((ls[s] - lag_of(acts[s], a["id"]) for s in succs[a["id"]]),
                          default=dur)
        ls[a["id"]] = lf[a["id"]] - a["dur"]
    tf = {i: ls[i] - es[i] for i in acts}
    ff = {i: (min((es[s] - lag_of(acts[s], i) for s in succs[i]), default=dur) - ef[i])
          for i in acts}

    # all tight zero-total-float source→sink paths (edge must be binding)
    zero = [i for i in acts if tf[i] == 0]
    starts = [i for i in zero if all(tf[p] > 0 for p in acts[i]["preds"])]
    sinks = [i for i in zero if all(tf[s] > 0 for s in succs[i])]
    paths = []
    def walk(node, acc):
        if node in sinks:
            paths.append(acc)
            return
        for s in [x for x in succs[node]
                  if tf[x] == 0 and lf[node] == ls[x] - lag_of(acts[x], node)]:
            walk(s, acc + [s])
    for s in starts:
        walk(s, [s])
    return {"es": es, "ef": ef, "ls": ls, "lf": lf, "total_float": tf, "free_float": ff,
            "critical_path": paths[0] if paths else [],
            "_all_cp_paths": paths, "project_duration": dur}


def ev_budget(d: dict) -> dict:
    labor = sum(r["hours"] * r["rate_pkr"] for r in d["roles"])
    indirects = labor * d["indirect_rate"]
    subtotal = labor + indirects + d["direct_costs_pkr"]
    contingency = subtotal * d["contingency_rate"]
    baseline = subtotal + contingency
    reserve = baseline * d["mgmt_reserve_rate"]
    total = baseline + reserve
    return {"labor_pkr": labor, "indirects_pkr": indirects, "subtotal_pkr": subtotal,
            "contingency_pkr": contingency, "baseline_pkr": baseline,
            "mgmt_reserve_pkr": reserve, "total_with_reserve_pkr": total,
            "cap_headroom_pkr": d["funding_cap_pkr"] - total}


def ev_pxi(d: dict) -> dict:
    scores, bands, emv = {}, {}, {}
    lo, med = d["bands"]["low_max"], d["bands"]["medium_max"]
    for r in d["risks"]:
        s = r["p"] * r["i"]
        scores[r["id"]] = s
        bands[r["id"]] = "low" if s <= lo else ("medium" if s <= med else "high")
        emv[r["id"]] = r["prob"] * r["money_pkr"]
    top = max(emv, key=emv.get)
    return {"scores": scores, "bands": bands, "emv_pkr": emv,
            "total_emv_pkr": sum(emv.values()), "top_emv": top}


def ev_histogram_stats(d: dict) -> dict:
    dl = d["deadline_weeks"]
    on_time = sum(h["count"] for h in d["histogram"] if h["completion_weeks"] <= dl)
    total = d["trials"]
    late = [(h["completion_weeks"] - dl) * h["count"] for h in d["histogram"]
            if h["completion_weeks"] > dl]
    late_trials = sum(h["count"] for h in d["histogram"] if h["completion_weeks"] > dl)
    cum, median, p70 = 0, None, None
    for h in d["histogram"]:
        cum += h["count"]
        if median is None and cum >= total / 2:
            median = h["completion_weeks"]
        if p70 is None and cum >= 0.7 * total:
            p70 = h["completion_weeks"]
    return {"on_time_trials": on_time, "p_on_time": round(on_time / total, 4),
            "median_week": median, "late_trials": late_trials,
            "mean_overrun_late_weeks": round(sum(late) / late_trials, 3),
            "mean_overrun_all_weeks": round(sum(late) / total, 2),
            "p70_bracket_weeks": p70}


def ev_contract_fpif(d: dict) -> dict:
    tp = d["target_cost_pkr"] + d["target_fee_pkr"]
    pota = d["target_cost_pkr"] + (d["ceiling_price_pkr"] - tp) / (1 - d["seller_share"])
    out = {"target_price_pkr": tp, "pota_pkr": round(pota, 1)}
    for c in d["check_costs_pkr"]:
        if c <= pota:
            fee = d["target_fee_pkr"] + (d["target_cost_pkr"] - c) * d["seller_share"]
            price = min(c + fee, d["ceiling_price_pkr"])
        else:
            price = d["ceiling_price_pkr"]
        fee = round(price - c, 1)
        out[f"fee_at_{c}"] = fee
        out[f"price_at_{c}"] = price
    return out


def ev_evm(d: dict) -> dict:
    cv = d["ev_pkr"] - d["ac_pkr"]
    sv = d["ev_pkr"] - d["pv_pkr"]
    cpi = d["ev_pkr"] / d["ac_pkr"]
    spi = d["ev_pkr"] / d["pv_pkr"]
    eac1 = d["bac_pkr"] / cpi
    return {"cv_pkr": cv, "sv_pkr": sv, "cpi": round(cpi, 4), "spi": round(spi, 4),
            "eac1_typical_pkr": round(eac1), "eac2_atypical_pkr": d["ac_pkr"] + (d["bac_pkr"] - d["ev_pkr"]),
            "vac_pkr": round(d["bac_pkr"] - eac1), "tcpi": round((d["bac_pkr"] - d["ev_pkr"]) / (d["bac_pkr"] - d["ac_pkr"]), 4)}


def ev_crash(d: dict) -> dict:
    slope = lambda k: (d[k]["crash_cost"] - d[k]["cost"]) / (d[k]["dur"] - d[k]["crash_dur"])  # noqa: E731
    return {"slope_A_pkr": slope("A"), "slope_B_pkr": slope("B"),
            "slope_C_pkr": slope("C"), "slope_D_pkr": slope("D"),
            "cp_before_weeks": d["A"]["dur"] + d["B"]["dur"] + d["D"]["dur"],
            "total_crash_cost_pkr": slope("B") * 1 + slope("A") * 1,
            "duration_after_weeks": d["A"]["crash_dur"] + d["B"]["crash_dur"] + d["D"]["dur"],
            "indirect_saving_pkr": d["indirect_per_week_pkr"] * 2}


def ev_leveling(d: dict) -> dict:
    after = d["weekly_loads_after"]
    return {"overload_w3_before": d["weekly_loads_before"]["w3"] - d["capacity_h_per_week"],
            "max_load_after": max(after.values()),
            "total_hours_preserved": sum(after.values())}


STRUCTURED = {
    "portfolio_score": ev_portfolio_score, "wbs_rollup": ev_wbs_rollup,
    "pert_calibration": ev_pert_calibration, "cpm": ev_cpm, "budget": ev_budget,
    "pxi": ev_pxi, "histogram_stats": ev_histogram_stats,
    "contract_fpif": ev_contract_fpif, "evm": ev_evm, "crash": ev_crash,
    "leveling": ev_leveling,
}


def check_numeric(cid: str, block: dict) -> None:
    stats["numeric"] += 1
    btype = block["type"]
    if "steps" in block:
        eval_steps(cid, block)
    elif btype in STRUCTURED:
        computed = STRUCTURED[btype](block["data"])
        if btype == "cpm":
            claimed = block["expected"]["critical_path"]
            all_paths = computed.pop("_all_cp_paths")
            stats["checks"] += 1
            if [str(x) for x in claimed] not in [[str(y) for y in p] for p in all_paths]:
                fail(f"{cid}: claimed critical path {claimed} is not a zero-float path of {computed['project_duration']}-week network")
            alt = block["expected"].get("critical_path_alt")
            if alt:
                stats["checks"] += 1
                if [str(x) for x in alt] not in [[str(y) for y in p] for p in all_paths]:
                    fail(f"{cid}: claimed alt critical path {alt} not found")
            check_expected(cid, {k: v for k, v in block["expected"].items()
                                 if k not in ("critical_path", "critical_path_alt")}, computed)
            return
        check_expected(cid, block["expected"], computed)
    else:
        fail(f"{cid}: numeric type {btype!r} has neither steps nor a known evaluator")


def run_all() -> list[str]:
    meta = yaml.safe_load(META_FILE.read_text(encoding="utf-8"))
    all_cases = []
    for fname, (difficulty, lo, hi) in sorted(BANDS.items()):
        path = CASES_DIR / fname
        if not path.exists():
            fail(f"missing band file {fname}")
            continue
        cases = yaml.safe_load(path.read_text(encoding="utf-8"))["cases"]
        want = [f"CS-{i:02d}" for i in range(lo, hi + 1)]
        got = [c["id"] for c in cases]
        if got != want:
            fail(f"{fname}: IDs {got[:3]}...{got[-3:]} do not match band range CS-{lo:02d}..CS-{hi:02d}")
        for c in cases:
            stats["cases"] += 1
            cid = c["id"]
            missing = SCHEMA_KEYS - set(c)
            if missing:
                fail(f"{cid}: missing keys {sorted(missing)}")
            if c.get("difficulty") != difficulty:
                fail(f"{cid}: difficulty {c.get('difficulty')} != band {difficulty}")
            n = c.get("numeric")
            if bool(n) != bool(c.get("numerical")):
                fail(f"{cid}: numerical flag ({c.get('numerical')}) inconsistent with numeric block presence ({bool(n)})")
            for listkey in ("tags", "concepts", "tasks", "deliverables", "discussion", "objectives"):
                if not c.get(listkey):
                    fail(f"{cid}: {listkey} empty")
            if len(c.get("solution", {}).get("reasoning", "")) < 200:
                fail(f"{cid}: solution.reasoning too thin (<200 chars)")
            if c.get("lecture") is not None and not 1 <= c["lecture"] <= 32:
                fail(f"{cid}: lecture anchor {c['lecture']} outside 1..32")
            if n:
                check_numeric(cid, n)
        all_cases += cases
    ids = [c["id"] for c in all_cases]
    if ids != [f"CS-{i:02d}" for i in range(1, len(ids) + 1)]:
        fail("merged IDs are not sequential CS-01..CS-nnn")
    if len(all_cases) != meta["meta"]["total_cases"]:
        fail(f"total cases {len(all_cases)} != meta.total_cases {meta['meta']['total_cases']}")
    if stats["numeric"] < meta["meta"]["numerical_target"]:
        fail(f"numeric cases {stats['numeric']} < meta.numerical_target {meta['meta']['numerical_target']}")
    return failures


def main() -> int:
    fails = run_all()
    print(f"CASE CHECK: {stats['cases']} cases, {stats['numeric']} numeric, "
          f"{stats['checks']} numeric assertions")
    if fails:
        print(f"FAIL ({len(fails)}):")
        for f in fails:
            print("  " + f)
        return 1
    print("PASS (0 failures)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
