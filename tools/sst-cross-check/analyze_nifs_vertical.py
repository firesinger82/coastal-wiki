#!/usr/bin/env python3
"""NIFS KODC 다층 수온 trend 분석 — 표층 vs 50m/100m/200m/500m.

입력: data/sst-global/nifs-kodc/all_raw.csv (523k records, .gitignore)
산출:
- data/sst-global/nifs-kodc/depth_annual.csv (해역·정선·연도·표준 깊이별 평균)
- data/sst-global/nifs-kodc/trends_by_depth.json (windows × 깊이 × 해역)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

WIKI = Path(__file__).resolve().parent.parent.parent
DATA = WIKI / "data" / "sst-global" / "nifs-kodc"

# 표준 깊이 (NIFS KODC 정선 측정 표준 layer)
DEPTH_BINS = [
    ("surface", 0, 5),     # 0-5m 표층
    ("upper", 6, 30),       # mixed layer 일부
    ("50m", 31, 75),
    ("100m", 76, 150),
    ("200m", 151, 300),
    ("500m", 301, 750),
]

WINDOWS = [
    ("2017-2025", 2017, 2025),
    ("1982-2025", 1982, 2025),
    ("1968-2022", 1968, 2022),
    ("1968-2012", 1968, 2012),
    ("1968-2025", 1968, 2025),
]


def regress(years, vals):
    n = len(years)
    if n < 3:
        return None
    x_mean = years.mean(); y_mean = vals.mean()
    ss_xy = ((years - x_mean) * (vals - y_mean)).sum()
    ss_xx = ((years - x_mean) ** 2).sum()
    slope = ss_xy / ss_xx
    intercept = y_mean - slope * x_mean
    pred = slope * years + intercept
    ss_res = ((vals - pred) ** 2).sum()
    ss_tot = ((vals - y_mean) ** 2).sum()
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return {"slope_per_decade": float(slope * 10), "r2": float(r2), "n": int(n)}


def main() -> int:
    print("[load] all_raw.csv …")
    df = pd.read_csv(DATA / "all_raw.csv", low_memory=False)
    print(f"  rows: {len(df):,}")
    df = df.dropna(subset=["wtem", "dpwt"]).copy()
    df["msrmtDt_iso"] = pd.to_datetime(df["msrmtDt"], unit="ms")
    df["year"] = df["msrmtDt_iso"].dt.year
    df["month"] = df["msrmtDt_iso"].dt.month
    print(f"  after wtem/dpwt dropna: {len(df):,}")

    # 깊이 bin
    def bin_depth(d):
        for label, lo, hi in DEPTH_BINS:
            if lo <= d <= hi:
                return label
        return None
    df["depth_bin"] = df["dpwt"].apply(bin_depth)
    df = df.dropna(subset=["depth_bin"])

    # 해역·정선·연도·깊이 평균
    annual = (df.groupby(["_sea", "_line", "year", "depth_bin"], as_index=False)
                .agg(t_mean=("wtem", "mean"),
                     n=("wtem", "count"),
                     n_months=("month", "nunique")))
    # n_months >= 4 (4계절 중 일부) 필터
    annual = annual[annual["n_months"] >= 4]
    annual.to_csv(DATA / "depth_annual.csv", index=False, float_format="%.4f")
    print(f"  depth_annual.csv: {len(annual)} rows")

    # 윈도우 × 깊이 × 해역 trend
    summary = {}
    for label, ys, ye in WINDOWS:
        win = annual[(annual["year"] >= ys) & (annual["year"] <= ye)]
        win_out = {}
        for depth in [d[0] for d in DEPTH_BINS]:
            ddf = win[win["depth_bin"] == depth]
            if ddf.empty:
                continue
            by_sea = {}
            for sea, grp in ddf.groupby("_sea"):
                yearly = grp.groupby("year")["t_mean"].mean().reset_index().sort_values("year")
                res = regress(yearly["year"].values, yearly["t_mean"].values)
                if res:
                    res["n_lines"] = grp["_line"].nunique()
                    by_sea[sea] = res
            # 전국
            yearly_nat = ddf.groupby("year")["t_mean"].mean().reset_index().sort_values("year")
            nat = regress(yearly_nat["year"].values, yearly_nat["t_mean"].values)
            win_out[depth] = {"by_sea": by_sea, "national": nat}
        summary[label] = win_out

    with open(DATA / "trends_by_depth.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"  trends_by_depth.json saved")

    # 출력: 한 윈도우 (1968-2022) 의 깊이별 trend 표
    print("\n=== 1968-2022 한국 전국·해역별·깊이별 trend (°C/decade) ===")
    fmt = "{:8s} | {:>9s} {:>9s} {:>9s} {:>9s}"
    print(fmt.format("depth", "전국", "서해", "남해", "동해"))
    print("-" * 60)
    win = summary.get("1968-2022", {})
    for depth in [d[0] for d in DEPTH_BINS]:
        d = win.get(depth, {})
        n = d.get("national") or {}
        by = d.get("by_sea", {})
        def f(v): return f"{v.get('slope_per_decade'):+.3f}" if v else "  n/a"
        print(fmt.format(depth, f(n), f(by.get("서해", {})), f(by.get("남해", {})), f(by.get("동해", {}))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
