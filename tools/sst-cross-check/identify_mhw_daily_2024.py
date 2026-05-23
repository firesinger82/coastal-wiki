#!/usr/bin/env python3
"""Daily MHW (Hobday 2016) — 2024 한국 13정점.

데이터: NOAA OISST v2.1 daily NetCDF (sst.day.mean.2024.nc, ~449MB)
방법:
1. 한국 13정점 격자에서 2024 daily SST 추출
2. monthly climatology p90 (이미 계산됨) 을 day-of-year 로 linear interp
3. daily SST > p90 (interp) → MHW threshold cross
4. 연속 ≥5 days → MHW event (Hobday 2016)
5. Category I-IV (Hobday 2018) 분류

산출:
- data/sst-global/mhw/daily_2024_<station>.csv
- data/sst-global/mhw/daily_2024_events.csv
- data/sst-global/mhw/daily_2024_summary.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import xarray as xr

WIKI = Path(__file__).resolve().parent.parent.parent
DATA = WIKI / "data" / "sst-global"
OUT = DATA / "mhw"
OUT.mkdir(parents=True, exist_ok=True)

DAILY_URL = "https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.day.mean.2024.nc"
DAILY_LOCAL = DATA / "oisst_v21_sst_day_2024.nc"

# Stations (fetch_oisst_monthly.py 와 동일)
STATIONS = [
    ("인천", "서해", 37.4519, 126.5922),
    ("목포", "서해", 34.7794, 126.3756),
    ("진도", "서해", 34.3781, 126.3081),
    ("부산", "남해", 35.0961, 129.0356),
    ("여수", "남해", 34.7472, 127.7654),
    ("거제도", "남해", 34.8094, 128.6997),
    ("거문도", "남해", 34.0286, 127.3081),
    ("제주", "남해", 33.5269, 126.5436),
    ("서귀포", "남해", 33.2400, 126.5614),
    ("울산", "동해", 35.5022, 129.3878),
    ("포항", "동해", 36.0431, 129.3786),
    ("묵호", "동해", 37.5503, 129.1167),
    ("속초", "동해", 38.2069, 128.5942),
]


def download_daily():
    if DAILY_LOCAL.exists():
        sz = DAILY_LOCAL.stat().st_size / 1024 / 1024
        print(f"[skip] {DAILY_LOCAL} ({sz:.1f} MB)")
        return DAILY_LOCAL
    print(f"[download] {DAILY_URL}")
    r = requests.get(DAILY_URL, stream=True, timeout=900)
    r.raise_for_status()
    total = 0
    with open(DAILY_LOCAL, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)
            total += len(chunk)
            print(f"  ... {total/1024/1024:.1f} MB", end="\r")
    print()
    return DAILY_LOCAL


def find_nearest_ocean(sst0_vals, lats, lons, lat, lon, max_radius=8):
    i0 = int(np.argmin(np.abs(lats - lat)))
    j0 = int(np.argmin(np.abs(lons - lon)))
    if not np.isnan(sst0_vals[i0, j0]):
        return i0, j0
    for r in range(1, max_radius + 1):
        cands = []
        for di in range(-r, r + 1):
            for dj in range(-r, r + 1):
                if max(abs(di), abs(dj)) != r:
                    continue
                i, j = i0 + di, j0 + dj
                if not (0 <= i < len(lats) and 0 <= j < len(lons)):
                    continue
                if not np.isnan(sst0_vals[i, j]):
                    cands.append((np.hypot(lats[i]-lat, lons[j]-lon), i, j))
        if cands:
            cands.sort()
            return cands[0][1], cands[0][2]
    raise RuntimeError(f"no ocean near {lat},{lon}")


def extract_daily(nc_path):
    ds = xr.open_dataset(nc_path)
    print(f"  dims: {dict(ds.sizes)}")
    print(f"  time: {pd.to_datetime(ds.time.min().values)} ~ {pd.to_datetime(ds.time.max().values)}")
    lats = ds.lat.values
    lons = ds.lon.values
    sst0 = ds.sst.isel(time=0).values
    if sst0.ndim == 3:
        sst0 = sst0[0]  # zlev dim 있다면 squeeze

    out = {}
    for name, region, lat, lon in STATIONS:
        lon_q = lon if lons.max() <= 180 else lon
        i, j = find_nearest_ocean(sst0, lats, lons, lat, lon_q)
        ts = ds.sst.isel(lat=i, lon=j).values
        if ts.ndim == 2:
            ts = ts[:, 0]  # zlev squeeze
        time_vals = pd.to_datetime(ds.time.values)
        df_st = pd.DataFrame({"date": time_vals, "sst_c": ts}).dropna()
        df_st["station"] = name
        df_st["region"] = region
        df_st["lat_grid"] = float(lats[i])
        df_st["lon_grid"] = float(lons[j])
        df_st["doy"] = df_st["date"].dt.dayofyear
        out[name] = df_st
        print(f"  {name}: {len(df_st)} days, grid ({lats[i]:.3f}, {lons[j]:.3f})")
    return out


def interpolate_monthly_p90_to_doy(monthly_clim_df, station):
    """monthly clim 를 doy-grid 로 linear interp."""
    sub = monthly_clim_df[monthly_clim_df["station"] == station].sort_values("month")
    # 월 중간 doy (대략)
    month_mid_doy = {1: 15, 2: 45, 3: 75, 4: 105, 5: 136, 6: 166,
                     7: 197, 8: 228, 9: 258, 10: 289, 11: 319, 12: 350}
    months = sub["month"].values
    doys = np.array([month_mid_doy[m] for m in months])
    p90s = sub["clim_p90"].values
    means = sub["clim_mean"].values
    # cyclic extension for doy interp (Jan15=380, Dec350=14)
    doys_ext = np.concatenate([doys - 366, doys, doys + 366])
    p90s_ext = np.concatenate([p90s, p90s, p90s])
    means_ext = np.concatenate([means, means, means])
    target_doy = np.arange(1, 367)
    p90_interp = np.interp(target_doy, doys_ext, p90s_ext)
    mean_interp = np.interp(target_doy, doys_ext, means_ext)
    return pd.DataFrame({"doy": target_doy, "p90_interp": p90_interp,
                          "mean_interp": mean_interp})


def detect_daily_events(daily_df, clim_interp_df, min_duration=5):
    df = daily_df.merge(clim_interp_df, on="doy", how="left")
    df["anomaly"] = df["sst_c"] - df["mean_interp"]
    df["over"] = df["sst_c"] > df["p90_interp"]
    events = []
    in_evt = False
    start_i = None
    for i, ov in enumerate(df["over"].values):
        if ov and not in_evt:
            start_i = i
            in_evt = True
        elif not ov and in_evt:
            if i - start_i >= min_duration:
                seg = df.iloc[start_i:i]
                events.append({
                    "start": seg["date"].iloc[0].strftime("%Y-%m-%d"),
                    "end": seg["date"].iloc[-1].strftime("%Y-%m-%d"),
                    "duration_days": int(i - start_i),
                    "max_anomaly_c": float(seg["anomaly"].max()),
                    "mean_anomaly_c": float(seg["anomaly"].mean()),
                    "max_sst_c": float(seg["sst_c"].max()),
                    "category": categorize(seg["anomaly"].max(),
                                          (seg["p90_interp"] - seg["mean_interp"]).mean()),
                })
            in_evt = False
    if in_evt and len(df) - start_i >= min_duration:
        seg = df.iloc[start_i:]
        events.append({
            "start": seg["date"].iloc[0].strftime("%Y-%m-%d"),
            "end": seg["date"].iloc[-1].strftime("%Y-%m-%d"),
            "duration_days": int(len(df) - start_i),
            "max_anomaly_c": float(seg["anomaly"].max()),
            "mean_anomaly_c": float(seg["anomaly"].mean()),
            "max_sst_c": float(seg["sst_c"].max()),
            "category": categorize(seg["anomaly"].max(),
                                  (seg["p90_interp"] - seg["mean_interp"]).mean()),
        })
    return events


def categorize(max_anom, sigma_proxy):
    if sigma_proxy <= 0: return "I-moderate"
    r = max_anom / sigma_proxy
    if r < 2: return "I-moderate"
    if r < 3: return "II-strong"
    if r < 4: return "III-severe"
    return "IV-extreme"


def main():
    nc_path = download_daily()
    daily_data = extract_daily(nc_path)
    # save daily csv
    for name, dfs in daily_data.items():
        dfs.to_csv(OUT / f"daily_2024_{name}.csv", index=False, float_format="%.3f")

    # monthly climatology load
    monthly_clim = pd.read_csv(OUT / "monthly_climatology.csv")

    all_events = []
    summary = {}
    print()
    for name, dfs in daily_data.items():
        clim_interp = interpolate_monthly_p90_to_doy(monthly_clim, name)
        events = detect_daily_events(dfs, clim_interp)
        for e in events:
            e["station"] = name
        all_events.extend(events)
        if events:
            top = sorted(events, key=lambda e: -e["max_anomaly_c"])[0]
            print(f"  {name}: {len(events)} events, top: {top['start']}~{top['end']} "
                  f"{top['duration_days']}d max_anom={top['max_anomaly_c']:+.2f}°C ({top['category']})")
        summary[name] = {
            "region": dfs["region"].iloc[0],
            "n_events": len(events),
            "longest_days": max([e["duration_days"] for e in events]) if events else 0,
            "max_anomaly_c": max([e["max_anomaly_c"] for e in events]) if events else 0.0,
            "categories": {c: sum(1 for e in events if e["category"] == c)
                          for c in ["I-moderate", "II-strong", "III-severe", "IV-extreme"]},
        }

    pd.DataFrame(all_events).to_csv(OUT / "daily_2024_events.csv", index=False, float_format="%.3f")
    with open(OUT / "daily_2024_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\n[saved] daily_2024_events.csv ({len(all_events)} events), summary.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
