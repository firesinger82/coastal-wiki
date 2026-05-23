#!/usr/bin/env python3
"""NIFS KODC surface_annual.csv → 해역별·정선별 trend.

방법:
1. 각 정선의 연평균 (이미 surface_annual.csv 에 계산됨, dpwt<=10m)
2. 해역별 = 해역 내 모든 정선 같은 연도 평균 (정선 동등 가중)
3. 전국 = 모든 해역 같은 연도 평균
4. 5 윈도우 (2017-2025, 1982-2025, 1968-2022, 1968-2012, 1968-2025) 선형회귀

산출:
- data/sst-global/nifs-kodc/trends_nifs.json (윈도우 × 해역·전국 × 정선별)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

WIKI = Path(__file__).resolve().parent.parent.parent
DATA = WIKI / "data" / "sst-global" / "nifs-kodc"

WINDOWS = [
    ("2017-2025", 2017, 2025),
    ("1982-2025", 1982, 2025),
    ("1968-2022", 1968, 2022),  # NIFS published reference
    ("1968-2012", 1968, 2012),
    ("1968-2025", 1968, 2025),
]


def regress(years: np.ndarray, vals: np.ndarray) -> dict:
    n = len(years)
    if n < 3:
        return {"slope_per_year": None, "slope_per_decade": None, "r2": None, "n": n}
    x_mean = years.mean()
    y_mean = vals.mean()
    ss_xy = ((years - x_mean) * (vals - y_mean)).sum()
    ss_xx = ((years - x_mean) ** 2).sum()
    slope = ss_xy / ss_xx
    intercept = y_mean - slope * x_mean
    pred = slope * years + intercept
    ss_res = ((vals - pred) ** 2).sum()
    ss_tot = ((vals - y_mean) ** 2).sum()
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return {
        "slope_per_year": float(slope),
        "slope_per_decade": float(slope * 10),
        "r2": float(r2),
        "n": int(n),
        "delta_first_last": float(vals[-1] - vals[0]),
    }


def analyze_window(df: pd.DataFrame, ys: int, ye: int) -> dict:
    win = df[(df["year"] >= ys) & (df["year"] <= ye)].copy()
    if win.empty:
        return {}

    out = {"window": f"{ys}-{ye}", "by_line": {}, "by_sea": {}, "national": None}

    # 정선별
    for (sea, line), grp in win.groupby(["_sea", "_line"]):
        grp = grp.sort_values("year")
        res = regress(grp["year"].values, grp["sst_mean"].values)
        res["sea"] = sea
        res["year_first"] = int(grp["year"].min())
        res["year_last"] = int(grp["year"].max())
        out["by_line"][f"{sea}-{line}"] = res

    # 해역별 — 해역 내 정선 동등 가중 평균
    for sea, grp in win.groupby("_sea"):
        # 각 연도의 정선 평균
        yearly = grp.groupby("year")["sst_mean"].mean().reset_index().sort_values("year")
        res = regress(yearly["year"].values, yearly["sst_mean"].values)
        res["n_lines"] = grp["_line"].nunique()
        out["by_sea"][sea] = res

    # 전국 = 모든 해역의 정선 동등 가중
    yearly = win.groupby("year")["sst_mean"].mean().reset_index().sort_values("year")
    out["national"] = regress(yearly["year"].values, yearly["sst_mean"].values)
    out["national"]["n_lines"] = win["_line"].nunique()

    return out


def main() -> int:
    df = pd.read_csv(DATA / "surface_annual.csv")
    print(f"NIFS surface annual rows: {len(df)}, "
          f"years {df['year'].min()}-{df['year'].max()}, "
          f"{df['_line'].nunique()} 정선")

    # n_months >= 6 필터 (반년 이상 관측한 연도만 신뢰)
    df = df[df["n_months"] >= 6].copy()
    print(f"  after n_months>=6 filter: {len(df)} rows")

    all_windows = {}
    for label, ys, ye in WINDOWS:
        r = analyze_window(df, ys, ye)
        if not r:
            continue
        all_windows[label] = r
        nat = r['national']
        if nat['slope_per_decade'] is not None:
            print(f"\n[{label}] national = {nat['slope_per_decade']:+.3f} °C/dec  R²={nat['r2']:.3f}  n_lines={nat['n_lines']}")
        else:
            print(f"\n[{label}] national = n/a (n_years<3)")
        for sea, sd in r["by_sea"].items():
            if sd['slope_per_decade'] is not None:
                print(f"  {sea:6s}: {sd['slope_per_decade']:+.3f} °C/dec  R²={sd['r2']:.3f}  n_lines={sd.get('n_lines')}")
            else:
                print(f"  {sea:6s}: n/a (n={sd['n']})")

    out_path = DATA / "trends_nifs.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_windows, f, ensure_ascii=False, indent=2)
    print(f"\n[saved] {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
