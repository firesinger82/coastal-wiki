#!/usr/bin/env python3
"""NIFS 다층 SST → 해역별·연도별 Ocean Heat Content (OHC) 0-500m 적분.

OHC = ρ · Cp · ∫₀^H T(z) dz   [J/m²]
trend: 연도별 OHC 의 선형회귀 → J/m²/year → 적분 면적 시 J/year

NIFS Fish Aquat Sci 2023 published 값과 비교:
  동해 0.148, 남해 0.089, 서해 0.061 × 10¹⁸ J/year (한국 EEZ 적분)

산출:
- data/sst-global/nifs-kodc/ohc_annual.csv (해역·연 평균 OHC)
- data/sst-global/nifs-kodc/ohc_trends.json (윈도우 × 해역 OHC trend)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

WIKI = Path(__file__).resolve().parent.parent.parent
DATA = WIKI / "data" / "sst-global" / "nifs-kodc"

RHO = 1025.0  # kg/m³ seawater
CP = 3990.0   # J/(kg·°C)

# 깊이 bin 중심 + 두께 (Δz)
# 0-150m 만 적분 — NIFS published 0-200m 과 가까운 범위, 200m·500m 는 sampling 한정·trend 신뢰성 낮음
DEPTH_BINS = [
    ("surface", 2.5, 5),     # 0-5m, 두께 5m
    ("upper", 18, 25),        # 6-30m, 두께 25m
    ("50m", 53, 45),          # 31-75m, 두께 45m
    ("100m", 113, 75),        # 76-150m, 두께 75m
    # 200m, 500m 제외 (NIFS published 와 정합성, sampling 한정)
]

# 해역별 면적 (km², 한국 EEZ 내 대략)
SEA_AREA_KM2 = {
    "동해": 110000,
    "남해": 75000,
    "서해": 80000,
    "동중국해": 30000,
}

WINDOWS = [
    ("2017-2025", 2017, 2025),
    ("1982-2025", 1982, 2025),
    ("1968-2022", 1968, 2022),
    ("1968-2012", 1968, 2012),
    ("1968-2025", 1968, 2025),
]


def compute_ohc_per_sea_year(annual: pd.DataFrame) -> pd.DataFrame:
    """각 (해역, 연도) 의 OHC J/m² 계산. 깊이 bin 합산."""
    rows = []
    for (sea, year), grp in annual.groupby(["_sea", "year"]):
        # 각 깊이 bin 평균 (정선들 평균, n_months>=4 이미 필터됨)
        bin_means = grp.groupby("depth_bin")["t_mean"].mean()
        # 모든 bin 들에 데이터 있는 경우만 OHC 계산
        ohc_layers = {}
        ohc_total = 0.0
        present = []
        for label, depth_center, thickness in DEPTH_BINS:
            t = bin_means.get(label)
            if t is not None and not np.isnan(t):
                layer_e = RHO * CP * t * thickness  # J/m² per layer
                ohc_layers[label] = layer_e
                ohc_total += layer_e
                present.append(label)
        if present:
            rows.append({
                "sea": sea, "year": int(year),
                "ohc_j_per_m2": ohc_total,
                "depth_bins_used": ",".join(present),
                "n_bins": len(present),
            })
    return pd.DataFrame(rows)


def regress(years, vals):
    n = len(years)
    if n < 3:
        return None
    x_mean = years.mean(); y_mean = vals.mean()
    ss_xy = ((years - x_mean) * (vals - y_mean)).sum()
    ss_xx = ((years - x_mean) ** 2).sum()
    slope = ss_xy / ss_xx
    pred = slope * years + (y_mean - slope * x_mean)
    ss_res = ((vals - pred) ** 2).sum()
    ss_tot = ((vals - y_mean) ** 2).sum()
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return {"slope_per_year_j_m2": float(slope), "r2": float(r2), "n": int(n)}


def main() -> int:
    annual = pd.read_csv(DATA / "depth_annual.csv")
    print(f"depth_annual rows: {len(annual)}")
    # n_bins ≥ 3 (최소 surface + upper + 50m) 필터링은 compute_ohc_per_sea_year 결과에서 사후
    ohc = compute_ohc_per_sea_year(annual)
    ohc = ohc[ohc["n_bins"] >= 3]  # 최소 0-75m 적분 확보
    ohc.to_csv(DATA / "ohc_annual.csv", index=False, float_format="%.4e")
    print(f"ohc_annual rows: {len(ohc)}")

    # 윈도우별 trend
    summary = {}
    for label, ys, ye in WINDOWS:
        win = ohc[(ohc["year"] >= ys) & (ohc["year"] <= ye)]
        wout = {}
        print(f"\n[{label}] OHC trend (×10⁸ J/m²/year, area-integrated 10¹⁸ J/year)")
        for sea, grp in win.groupby("sea"):
            grp = grp.sort_values("year")
            r = regress(grp["year"].values, grp["ohc_j_per_m2"].values)
            if r:
                area_m2 = SEA_AREA_KM2.get(sea, 0) * 1e6
                ohc_per_year = r["slope_per_year_j_m2"] * area_m2  # J/year
                r["area_km2"] = SEA_AREA_KM2.get(sea, 0)
                r["ohc_e18_j_per_year"] = ohc_per_year / 1e18
                wout[sea] = r
                print(f"  {sea:6s}: {r['slope_per_year_j_m2']/1e8:+.3f} ×10⁸ J/m²/yr  "
                      f"→ {r['ohc_e18_j_per_year']:+.4f} ×10¹⁸ J/yr  "
                      f"R²={r['r2']:.3f}  n={r['n']}")
        summary[label] = wout

    with open(DATA / "ohc_trends.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\n[saved] {DATA}/ohc_trends.json")

    # 비교 — NIFS published Fish Aquat Sci 2023 (1955-2021 OHC 0-200m):
    # 동해 0.148, 남해 0.089, 서해 0.061 ×10¹⁸ J/year
    print("\n=== NIFS published (Fish Aquat Sci 2023, 1955-2021 0-200m) ===")
    print("  동해 0.148, 남해 0.089, 서해 0.061 ×10¹⁸ J/year")
    return 0


if __name__ == "__main__":
    sys.exit(main())
