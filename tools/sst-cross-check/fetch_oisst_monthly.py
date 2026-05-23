#!/usr/bin/env python3
"""OISST v2.1 monthly mean NetCDF 다운로드 + 13 KHOA 정점 좌표 시계열 추출.

데이터: NOAA OISST v2.1 (0.25° daily → monthly mean)
소스: NOAA PSL ftp/https
범위: 1981-12 ~ 현재 (현 시점 직전월까지)
size: ~30-50 MB

산출: data/sst-global/oisst_v21_13stations_monthly.csv
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

# OISST v2.1 monthly mean (sst.mnmean.nc on PSL)
OISST_URL = "https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc"
OISST_LOCAL = DATA_DIR / "oisst_v21_sst_mon_mean.nc"

# 13 KHOA 정점 + 위경도 (KHOA Annual Report 2025 정점 list)
# experience/khoa-sst-warming-trend.md 의 정점과 일치
STATIONS = [
    # name, region, lat, lon
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


def download_oisst() -> Path:
    if OISST_LOCAL.exists():
        sz = OISST_LOCAL.stat().st_size / 1024 / 1024
        print(f"[skip] OISST 파일 존재: {OISST_LOCAL} ({sz:.1f} MB)")
        return OISST_LOCAL
    print(f"[download] {OISST_URL}")
    r = requests.get(OISST_URL, stream=True, timeout=300)
    r.raise_for_status()
    total = 0
    with open(OISST_LOCAL, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)
            total += len(chunk)
            print(f"  ... {total/1024/1024:.1f} MB", end="\r")
    print()
    print(f"[done] saved {OISST_LOCAL} ({total/1024/1024:.1f} MB)")
    return OISST_LOCAL


def find_nearest_ocean(ds: xr.Dataset, lat: float, lon: float,
                       max_radius: int = 8) -> tuple[float, float, np.ndarray]:
    """직접 nearest pixel 이 육지(NaN) 이면 주변 neighborhood 에서 ocean pixel 검색.

    OISST 0.25° 격자 → max_radius=8 은 약 2° (~220 km) 까지 검색.
    """
    lats = ds.lat.values
    lons = ds.lon.values
    # 직접 nearest grid idx
    i0 = int(np.argmin(np.abs(lats - lat)))
    j0 = int(np.argmin(np.abs(lons - lon)))

    # 첫 시각 sst 으로 land mask 판단 (NaN = land/ice)
    sst0_vals = ds.sst.isel(time=0).values

    # 직접 픽셀이 ocean 인가
    if not np.isnan(sst0_vals[i0, j0]):
        ts = ds.sst.isel(lat=i0, lon=j0).values
        return float(lats[i0]), float(lons[j0]), ts

    # 육지 — neighborhood expanding spiral
    for r in range(1, max_radius + 1):
        candidates = []
        for di in range(-r, r + 1):
            for dj in range(-r, r + 1):
                if max(abs(di), abs(dj)) != r:  # only ring
                    continue
                i = i0 + di
                j = j0 + dj
                if not (0 <= i < len(lats) and 0 <= j < len(lons)):
                    continue
                if not np.isnan(sst0_vals[i, j]):
                    d = np.hypot(lats[i] - lat, lons[j] - lon)
                    candidates.append((d, i, j))
        if candidates:
            candidates.sort()
            _, i, j = candidates[0]
            ts = ds.sst.isel(lat=i, lon=j).values
            return float(lats[i]), float(lons[j]), ts

    raise RuntimeError(f"No ocean pixel within radius {max_radius} for ({lat}, {lon})")


def extract_stations(nc_path: Path) -> pd.DataFrame:
    """OISST NetCDF 에서 13정점 좌표 추출 → long-format DataFrame."""
    print(f"[open] {nc_path}")
    ds = xr.open_dataset(nc_path)
    print(f"  dims: {dict(ds.sizes)}")
    print(f"  time range: {pd.to_datetime(ds.time.min().values)} ~ {pd.to_datetime(ds.time.max().values)}")

    lon_max = float(ds.lon.max())
    times = ds.time.values

    rows = []
    for name, region, lat, lon in STATIONS:
        lon_query = lon + 360 if (lon_max > 180 and lon < 0) else lon
        actual_lat, actual_lon, values = find_nearest_ocean(ds, lat, lon_query)
        landfix = (abs(actual_lat - lat) > 0.13) or (abs(actual_lon - lon_query) > 0.13)
        # OISST 0.25°: nearest 는 ~0.125° 차이가 정상. 그보다 크면 fallback 작동
        n_valid = int(np.sum(~np.isnan(values)))
        tag = "  [LAND→sea fallback]" if landfix else ""
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

    df = pd.DataFrame(rows)
    return df


def main() -> int:
    path = download_oisst()
    df = extract_stations(path)
    out_csv = DATA_DIR / "oisst_v21_13stations_monthly.csv"
    df.to_csv(out_csv, index=False, float_format="%.4f")
    print(f"[saved] {out_csv}  ({len(df)} rows)")

    # 요약
    print()
    print("=== 요약 (정점별 first/last + 결측 ===")
    for name in df["station"].unique():
        sub = df[df["station"] == name].dropna(subset=["sst_c"])
        if not sub.empty:
            print(f"  {name}: {sub['date'].min().strftime('%Y-%m')} ~ {sub['date'].max().strftime('%Y-%m')} "
                  f"n={len(sub)} (missing {(df['station']==name).sum() - len(sub)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
