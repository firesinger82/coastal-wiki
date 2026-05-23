#!/usr/bin/env python3
"""OISST v2.1 + HadISST 다중 시간 윈도우 linear regression 분석.

윈도우:
- 2017-2025  (9년)  — KHOA 백서 본 분석과 직접 비교
- 1982-2025  (44년) — OISST 전체 (가장 긴 satellite 시계열)
- 1968-2022  (55년) — NIFS published reference 와 비교 (Fish Aquat Sci 2023)
- 1968-2012  (45년) — KHOA Annual Report 2012 vol.2 §3.1 표 3-1 와 비교
- 1870-2025  (156년) — HadISST 가능한 최장 (장기 climate)

산출:
- data/sst-global/trends_oisst_<window>.json
- data/sst-global/trends_hadisst_<window>.json
- data/sst-global/comparison_summary.json (모든 윈도우 + 해역별)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

WIKI_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = WIKI_ROOT / "data" / "sst-global"

# 분석 윈도우 (start_year, end_year) inclusive
WINDOWS = [
    ("2017-2025", 2017, 2025),  # KHOA 본 분석
    ("1982-2025", 1982, 2025),  # OISST 전체
    ("1968-2022", 1968, 2022),  # NIFS published
    ("1968-2012", 1968, 2012),  # KHOA 1968-2012 ref
    ("1870-2025", 1870, 2025),  # HadISST 최장
    ("1850-2025", 1850, 2025),  # COBE-SST2 최장 (176년)
]


def annualize(df: pd.DataFrame) -> pd.DataFrame:
    """monthly long-form → 정점·년도별 평균."""
    df = df.copy()
    df["year"] = pd.to_datetime(df["date"]).dt.year
    g = (df.dropna(subset=["sst_c"])
           .groupby(["station", "region", "year"], as_index=False)["sst_c"]
           .agg(["mean", "count"]))
    g.columns = ["station", "region", "year", "sst_mean", "n_months"]
    # 결측 많은 해 제외 (최소 9 months 이상)
    g = g[g["n_months"] >= 9].reset_index(drop=True)
    return g


def regress(years: np.ndarray, vals: np.ndarray) -> dict:
    n = len(years)
    if n < 3:
        return {"slope_per_year": None, "slope_per_decade": None, "r2": None,
                "intercept": None, "n": n, "delta_first_last": None}
    x_mean = years.mean()
    y_mean = vals.mean()
    ss_xy = ((years - x_mean) * (vals - y_mean)).sum()
    ss_xx = ((years - x_mean) ** 2).sum()
    slope = ss_xy / ss_xx
    intercept = y_mean - slope * x_mean
    pred = slope * years + intercept
    ss_res = ((vals - pred) ** 2).sum()
    ss_tot = ((vals - y_mean) ** 2).sum()
    r2 = float(1 - ss_res / ss_tot) if ss_tot > 0 else float("nan")
    return {
        "slope_per_year": float(slope),
        "slope_per_decade": float(slope * 10),
        "r2": r2,
        "intercept": float(intercept),
        "n": int(n),
        "delta_first_last": float(vals[-1] - vals[0]),
    }


def analyze(annual_df: pd.DataFrame, label: str, win_start: int, win_end: int) -> dict:
    win = annual_df[(annual_df["year"] >= win_start) & (annual_df["year"] <= win_end)]
    if win.empty:
        return {}
    out = {"dataset": label, "window": f"{win_start}-{win_end}", "stations": {}}
    for st in win["station"].unique():
        sub = win[win["station"] == st].sort_values("year")
        years = sub["year"].values
        vals = sub["sst_mean"].values
        res = regress(years, vals)
        res["region"] = sub["region"].iloc[0]
        res["year_first"] = int(years[0])
        res["year_last"] = int(years[-1])
        out["stations"][st] = res

    # 해역별 평균
    region_means = {}
    for region in ["서해", "남해", "동해"]:
        slopes = [out["stations"][s]["slope_per_decade"]
                  for s in out["stations"]
                  if out["stations"][s].get("region") == region
                  and out["stations"][s].get("slope_per_decade") is not None]
        if slopes:
            region_means[region] = {
                "mean_slope_per_decade": float(np.mean(slopes)),
                "n_stations": len(slopes),
            }
    out["region_means"] = region_means

    all_slopes = [out["stations"][s]["slope_per_decade"]
                  for s in out["stations"]
                  if out["stations"][s].get("slope_per_decade") is not None]
    out["national_mean_slope_per_decade"] = float(np.mean(all_slopes)) if all_slopes else None
    out["n_stations_used"] = len(all_slopes)
    return out


def main() -> int:
    oisst = pd.read_csv(DATA_DIR / "oisst_v21_13stations_monthly.csv")
    hadisst = pd.read_csv(DATA_DIR / "hadisst_13stations_monthly.csv")
    cobe2_path = DATA_DIR / "cobe2_13stations_monthly.csv"
    cobe2 = pd.read_csv(cobe2_path) if cobe2_path.exists() else None

    oisst_annual = annualize(oisst)
    hadisst_annual = annualize(hadisst)
    cobe2_annual = annualize(cobe2) if cobe2 is not None else None

    print(f"OISST annual rows: {len(oisst_annual)}, year range {oisst_annual['year'].min()}~{oisst_annual['year'].max()}")
    print(f"HadISST annual rows: {len(hadisst_annual)}, year range {hadisst_annual['year'].min()}~{hadisst_annual['year'].max()}")
    if cobe2_annual is not None:
        print(f"COBE2 annual rows: {len(cobe2_annual)}, year range {cobe2_annual['year'].min()}~{cobe2_annual['year'].max()}")

    summary = {"oisst": {}, "hadisst": {}, "cobe2": {}}
    for label, ys, ye in WINDOWS:
        # OISST 는 1982+ 데이터만
        if ye >= 1982:
            r = analyze(oisst_annual, "oisst", ys, ye)
            if r:
                summary["oisst"][label] = r
                print(f"\n[OISST {label}] n_stations={r.get('n_stations_used')}, "
                      f"national mean = {r.get('national_mean_slope_per_decade'):.3f} °C/decade")
        # HadISST 전 기간
        r = analyze(hadisst_annual, "hadisst", ys, ye)
        if r:
            summary["hadisst"][label] = r
            print(f"\n[HadISST {label}] n_stations={r.get('n_stations_used')}, "
                  f"national mean = {r.get('national_mean_slope_per_decade'):.3f} °C/decade")
        # COBE-SST2
        if cobe2_annual is not None:
            r = analyze(cobe2_annual, "cobe2", ys, ye)
            if r:
                summary["cobe2"][label] = r
                print(f"[COBE2  {label}] n_stations={r.get('n_stations_used')}, "
                      f"national mean = {r.get('national_mean_slope_per_decade'):.3f} °C/decade")

    # 요약 저장
    out_path = DATA_DIR / "trends_global_summary.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\n[saved] {out_path}")

    # comparison table (정점별 OISST vs HadISST vs KHOA 본 분석)
    return 0


if __name__ == "__main__":
    sys.exit(main())
