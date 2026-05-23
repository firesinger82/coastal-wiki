#!/usr/bin/env python3
"""Marine Heatwave (MHW) 식별 — Hobday 2016 algorithm.

데이터: NOAA OISST v2.1 daily SST via ERDDAP point query.
대상: 한국 13정점 중 R² 강한 정점 우선 (서귀포·제주·거제도).
기간: 1991-01-01 ~ 2025-12-31 (climatology base 1991-2020).

산출:
- data/sst-global/mhw/<station>_daily.csv (raw daily SST)
- data/sst-global/mhw/<station>_climatology.csv (day-of-year 별 mean + p90)
- data/sst-global/mhw/<station>_events.csv (MHW events: start/end/duration/max_anom/category)
- data/sst-global/mhw/summary.json (전체 결과)
"""
from __future__ import annotations

import json
import sys
from io import StringIO
from pathlib import Path

import numpy as np
import pandas as pd
import requests

WIKI = Path(__file__).resolve().parent.parent.parent
OUT = WIKI / "data" / "sst-global" / "mhw"
OUT.mkdir(parents=True, exist_ok=True)

# OISST v2.1 ERDDAP — NOAA CoastWatch
ERDDAP = "https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg_LonPM180.csv"

# 13정점 중 R² 강했던 정점 우선
STATIONS = [
    ("서귀포", 33.24, 126.5614),
    ("제주", 33.5269, 126.5436),
    ("거제도", 34.8094, 128.6997),
    ("부산", 35.0961, 129.0356),
    ("포항", 36.0431, 129.3786),
]

BASELINE = ("1991-01-01", "2020-12-31")
ANALYSIS = ("1991-01-01", "2025-12-31")


def fetch_daily(name: str, lat: float, lon: float) -> pd.DataFrame:
    """OISST daily SST 한 격자점 1991-2025."""
    out_csv = OUT / f"{name}_daily.csv"
    if out_csv.exists():
        print(f"  [skip] {out_csv} 존재")
        return pd.read_csv(out_csv, parse_dates=["time"])

    # ERDDAP nearest grid lookup. OISST 0.25° → 격자 round
    lat_g = round(lat * 4) / 4
    lon_g = round(lon * 4) / 4
    # ERDDAP query (CSV with header)
    url = (f"{ERDDAP}?sst[({ANALYSIS[0]}T12:00:00Z):1:({ANALYSIS[1]}T12:00:00Z)]"
           f"[(0.0):1:(0.0)]"
           f"[({lat_g}):1:({lat_g})]"
           f"[({lon_g}):1:({lon_g})]")
    print(f"  [fetch] {name} (lat={lat_g}, lon={lon_g})")
    r = requests.get(url, timeout=600, headers={"User-Agent": "coastal-wiki/0.1"})
    r.raise_for_status()
    # ERDDAP CSV: 2 header rows (col name, units), then data
    text = r.text
    # parse — skip second row (units)
    lines = text.split("\n")
    if len(lines) < 3:
        raise RuntimeError(f"Empty ERDDAP response: {text[:200]}")
    header = lines[0]
    data_text = "\n".join([header] + lines[2:])
    df = pd.read_csv(StringIO(data_text))
    df.columns = [c.strip() for c in df.columns]
    df = df.rename(columns={"time": "time", "sst": "sst_c"})
    df["time"] = pd.to_datetime(df["time"], utc=True).dt.tz_localize(None)
    df = df[["time", "sst_c"]].dropna(subset=["sst_c"]).copy()
    df.to_csv(out_csv, index=False, float_format="%.4f")
    print(f"    {len(df)} days, range {df['time'].min().date()}~{df['time'].max().date()}")
    return df


def compute_climatology(df: pd.DataFrame, baseline=BASELINE, window: int = 11) -> pd.DataFrame:
    """day-of-year (1-366) 별 mean + 90 percentile, 11일 이동 평균."""
    base = df[(df["time"] >= baseline[0]) & (df["time"] <= baseline[1])].copy()
    base["doy"] = base["time"].dt.dayofyear
    clim_mean = base.groupby("doy")["sst_c"].mean()
    clim_p90 = base.groupby("doy")["sst_c"].quantile(0.9)
    # 11일 이동 평균 (cyclic; Hobday 2016)
    def smooth_cyclic(s, w=11):
        # 1-366 인덱스 cyclic
        ext = np.concatenate([s.values[-(w//2):], s.values, s.values[:w//2]])
        kernel = np.ones(w) / w
        smoothed = np.convolve(ext, kernel, mode="valid")
        return pd.Series(smoothed[:len(s)], index=s.index)
    clim_mean_s = smooth_cyclic(clim_mean, window)
    clim_p90_s = smooth_cyclic(clim_p90, window)
    clim = pd.DataFrame({"doy": clim_mean.index, "mean": clim_mean_s.values,
                         "p90": clim_p90_s.values})
    return clim


def detect_events(df: pd.DataFrame, clim: pd.DataFrame, min_duration: int = 5) -> list[dict]:
    """Hobday 2016 detection. 연속 ≥5일 SST > p90 → event."""
    df = df.copy().sort_values("time").reset_index(drop=True)
    df["doy"] = df["time"].dt.dayofyear
    df = df.merge(clim, on="doy", how="left")
    df["anomaly"] = df["sst_c"] - df["mean"]
    df["over"] = df["sst_c"] > df["p90"]
    df["over"] = df["over"].fillna(False)

    events = []
    in_evt = False
    start_idx = None
    for i, ov in enumerate(df["over"].values):
        if ov and not in_evt:
            start_idx = i
            in_evt = True
        elif not ov and in_evt:
            if i - start_idx >= min_duration:
                ev_anom = df["anomaly"].iloc[start_idx:i].values
                ev_p90 = df["p90"].iloc[start_idx:i].values
                ev_mean = df["mean"].iloc[start_idx:i].values
                events.append({
                    "start": df["time"].iloc[start_idx].date(),
                    "end": df["time"].iloc[i-1].date(),
                    "duration_days": int(i - start_idx),
                    "max_anomaly_c": float(np.max(ev_anom)),
                    "mean_anomaly_c": float(np.mean(ev_anom)),
                    "max_sst_c": float(df["sst_c"].iloc[start_idx:i].max()),
                    "category": categorize(ev_anom, ev_p90 - ev_mean),
                })
            in_evt = False
    # tail
    if in_evt and len(df) - start_idx >= min_duration:
        ev_anom = df["anomaly"].iloc[start_idx:].values
        ev_p90 = df["p90"].iloc[start_idx:].values
        ev_mean = df["mean"].iloc[start_idx:].values
        events.append({
            "start": df["time"].iloc[start_idx].date(),
            "end": df["time"].iloc[-1].date(),
            "duration_days": int(len(df) - start_idx),
            "max_anomaly_c": float(np.max(ev_anom)),
            "mean_anomaly_c": float(np.mean(ev_anom)),
            "max_sst_c": float(df["sst_c"].iloc[start_idx:].max()),
            "category": categorize(ev_anom, ev_p90 - ev_mean),
        })
    return events


def categorize(anomaly, threshold_diff) -> str:
    """Hobday 2018 Category I~IV.
    diff = p90 - mean (per-day stddev proxy)
    """
    # Use max anomaly relative to mean threshold_diff at that day
    sigma = np.mean(threshold_diff)
    if sigma <= 0:
        return "I-moderate"
    ratio = np.max(anomaly) / sigma
    if ratio < 2: return "I-moderate"
    if ratio < 3: return "II-strong"
    if ratio < 4: return "III-severe"
    return "IV-extreme"


def main() -> int:
    summary = {}
    for name, lat, lon in STATIONS:
        print(f"\n=== {name} (lat={lat}, lon={lon}) ===")
        try:
            df = fetch_daily(name, lat, lon)
        except Exception as e:
            print(f"  ERR: {e}")
            continue
        clim = compute_climatology(df)
        clim.to_csv(OUT / f"{name}_climatology.csv", index=False, float_format="%.4f")
        events = detect_events(df, clim)
        ev_df = pd.DataFrame(events)
        if not ev_df.empty:
            ev_df.to_csv(OUT / f"{name}_events.csv", index=False)
        print(f"  events: {len(events)}")
        if events:
            # 최근 5 events
            for ev in sorted(events, key=lambda e: e["start"])[-5:]:
                print(f"    {ev['start']}~{ev['end']} {ev['duration_days']}d "
                      f"max_anom={ev['max_anomaly_c']:+.2f}°C ({ev['category']})")
        summary[name] = {
            "lat": lat, "lon": lon,
            "n_days": len(df),
            "n_events": len(events),
            "max_duration_days": int(max([e["duration_days"] for e in events])) if events else 0,
            "max_anomaly_c": float(max([e["max_anomaly_c"] for e in events])) if events else 0.0,
        }

    with open(OUT / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\n[saved] {OUT}/summary.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
