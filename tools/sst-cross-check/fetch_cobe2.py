#!/usr/bin/env python3
"""COBE-SST2 (JMA) NetCDF 다운로드 + 13 KHOA 정점 좌표 시계열 추출.

데이터: JMA COBE-SST2 (Japan Meteorological Agency)
배포: NOAA PSL 미러 (https://downloads.psl.noaa.gov/Datasets/COBE2/sst.mon.mean.nc)
해상도: 1° × 1° monthly
기간: 1850.01 ~ 현재 (175+ 년 — HadISST 보다 20년 더 길음)
size: ~523 MB

산출: data/sst-global/cobe2_13stations_monthly.csv
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import xarray as xr

WIKI_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = WIKI_ROOT / "data" / "sst-global"
DATA_DIR.mkdir(parents=True, exist_ok=True)

COBE2_URL = "https://downloads.psl.noaa.gov/Datasets/COBE2/sst.mon.mean.nc"
COBE2_LOCAL = DATA_DIR / "cobe2_sst_mon_mean.nc"

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


def download() -> Path:
    if COBE2_LOCAL.exists():
        sz = COBE2_LOCAL.stat().st_size / 1024 / 1024
        print(f"[skip] COBE2 파일 존재: {COBE2_LOCAL} ({sz:.1f} MB)")
        return COBE2_LOCAL
    print(f"[download] {COBE2_URL}")
    r = requests.get(COBE2_URL, stream=True, timeout=900)
    r.raise_for_status()
    total = 0
    with open(COBE2_LOCAL, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)
            total += len(chunk)
            print(f"  ... {total/1024/1024:.1f} MB", end="\r")
    print()
    print(f"[done] saved {COBE2_LOCAL} ({total/1024/1024:.1f} MB)")
    return COBE2_LOCAL


def find_nearest_ocean(ds: xr.Dataset, lat: float, lon: float,
                       max_radius: int = 4) -> tuple[float, float, np.ndarray]:
    """COBE2 1° grid 에서 ocean pixel 찾기."""
    lats = ds.lat.values
    lons = ds.lon.values
    i0 = int(np.argmin(np.abs(lats - lat)))
    j0 = int(np.argmin(np.abs(lons - lon)))

    sst0 = ds.sst.isel(time=0).values
    if not np.isnan(sst0[i0, j0]):
        ts = ds.sst.isel(lat=i0, lon=j0).values
        return float(lats[i0]), float(lons[j0]), ts

    for r in range(1, max_radius + 1):
        candidates = []
        for di in range(-r, r + 1):
            for dj in range(-r, r + 1):
                if max(abs(di), abs(dj)) != r:
                    continue
                i = i0 + di
                j = j0 + dj
                if not (0 <= i < len(lats) and 0 <= j < len(lons)):
                    continue
                if not np.isnan(sst0[i, j]):
                    d = np.hypot(lats[i] - lat, lons[j] - lon)
                    candidates.append((d, i, j))
        if candidates:
            candidates.sort()
            _, i, j = candidates[0]
            ts = ds.sst.isel(lat=i, lon=j).values
            return float(lats[i]), float(lons[j]), ts

    raise RuntimeError(f"No ocean pixel within radius {max_radius} for ({lat}, {lon})")


def extract_stations(nc_path: Path) -> pd.DataFrame:
    print(f"[open] {nc_path}")
    ds = xr.open_dataset(nc_path)
    print(f"  dims: {dict(ds.sizes)}")
    print(f"  time range: {pd.to_datetime(ds.time.min().values)} ~ {pd.to_datetime(ds.time.max().values)}")

    lon_max = float(ds.lon.max())
    times = ds.time.values
    rows = []
    for name, region, lat, lon in STATIONS:
        lon_q = lon + 360 if (lon_max > 180 and lon < 0) else lon
        # COBE2 lon 은 0-360 (PSL 컨벤션)
        if lon_max > 180:
            lon_q = lon
        actual_lat, actual_lon, values = find_nearest_ocean(ds, lat, lon_q)
        n_valid = int(np.sum(~np.isnan(values)))
        d = np.hypot(actual_lat - lat, actual_lon - lon_q)
        tag = "  [LAND→sea fallback]" if d > 0.6 else ""
        print(f"  {name} ({region}) {lat:.3f},{lon:.3f} → grid ({actual_lat:.3f},{actual_lon:.3f}) "
              f"n={len(values)} valid={n_valid}{tag}")
        for t, v in zip(times, values):
            rows.append({
                "station": name,
                "region": region,
                "lat_req": lat,
                "lon_req": lon,
                "lat_actual": actual_lat,
                "lon_actual": actual_lon,
                "date": pd.to_datetime(t),
                "sst_c": float(v) if not np.isnan(v) else np.nan,
            })

    return pd.DataFrame(rows)


def main() -> int:
    path = download()
    df = extract_stations(path)
    out_csv = DATA_DIR / "cobe2_13stations_monthly.csv"
    df.to_csv(out_csv, index=False, float_format="%.4f")
    print(f"[saved] {out_csv}  ({len(df)} rows)")

    print()
    print("=== 요약 (정점별 first/last + 결측) ===")
    for name in df["station"].unique():
        sub = df[df["station"] == name].dropna(subset=["sst_c"])
        total = (df["station"] == name).sum()
        if not sub.empty:
            print(f"  {name}: {sub['date'].min().strftime('%Y-%m')} ~ {sub['date'].max().strftime('%Y-%m')} "
                  f"n={len(sub)} (missing {total - len(sub)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
