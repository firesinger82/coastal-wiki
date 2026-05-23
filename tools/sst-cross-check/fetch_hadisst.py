#!/usr/bin/env python3
"""HadISST NetCDF 다운로드 + 13 KHOA 정점 좌표 시계열 추출.

데이터: HadISST v1.1 (UK Met Office Hadley Centre)
해상도: 1°x1° monthly
기간: 1870-01 ~ 현재
size: ~50 MB (.nc.gz)

산출: data/sst-global/hadisst_13stations_monthly.csv
"""
from __future__ import annotations

import gzip
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import xarray as xr

WIKI_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = WIKI_ROOT / "data" / "sst-global"
DATA_DIR.mkdir(parents=True, exist_ok=True)

HADISST_URL = "https://www.metoffice.gov.uk/hadobs/hadisst/data/HadISST_sst.nc.gz"
HADISST_GZ = DATA_DIR / "HadISST_sst.nc.gz"
HADISST_LOCAL = DATA_DIR / "HadISST_sst.nc"

# 동일한 13 KHOA 정점 (fetch_oisst_monthly.py 와 일치)
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


def download_and_unpack() -> Path:
    if HADISST_LOCAL.exists():
        sz = HADISST_LOCAL.stat().st_size / 1024 / 1024
        print(f"[skip] HadISST 압축 해제 파일 존재: {HADISST_LOCAL} ({sz:.1f} MB)")
        return HADISST_LOCAL
    if not HADISST_GZ.exists():
        print(f"[download] {HADISST_URL}")
        r = requests.get(HADISST_URL, stream=True, timeout=600)
        r.raise_for_status()
        total = 0
        with open(HADISST_GZ, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                f.write(chunk)
                total += len(chunk)
                print(f"  ... {total/1024/1024:.1f} MB", end="\r")
        print()
        print(f"[done] saved {HADISST_GZ} ({total/1024/1024:.1f} MB compressed)")
    print(f"[gunzip] {HADISST_GZ} → {HADISST_LOCAL}")
    with gzip.open(HADISST_GZ, "rb") as fin, open(HADISST_LOCAL, "wb") as fout:
        shutil.copyfileobj(fin, fout)
    sz = HADISST_LOCAL.stat().st_size / 1024 / 1024
    print(f"[done] unpacked ({sz:.1f} MB)")
    return HADISST_LOCAL


def find_nearest_ocean(ds: xr.Dataset, lat: float, lon: float,
                       max_radius: int = 4) -> tuple[float, float, np.ndarray]:
    """HadISST 1° grid 에서 ocean pixel 찾기. max_radius=4 ≈ 4° (~440 km)."""
    lats = ds.latitude.values
    lons = ds.longitude.values
    i0 = int(np.argmin(np.abs(lats - lat)))
    j0 = int(np.argmin(np.abs(lons - lon)))

    # HadISST 의 land/ice 는 -1000 또는 매우 음수로 채워질 수 있음. NaN 대신 mask 사용 권장.
    sst0 = ds.sst.isel(time=0).values
    # 1.0e+20 또는 비현실 값 NaN 처리
    sst0 = np.where(sst0 < -100, np.nan, sst0)

    if not np.isnan(sst0[i0, j0]):
        ts = ds.sst.isel(latitude=i0, longitude=j0).values
        ts = np.where(ts < -100, np.nan, ts)
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
            ts = ds.sst.isel(latitude=i, longitude=j).values
            ts = np.where(ts < -100, np.nan, ts)
            return float(lats[i]), float(lons[j]), ts

    raise RuntimeError(f"No ocean pixel within radius {max_radius} for ({lat}, {lon})")


def extract_stations(nc_path: Path) -> pd.DataFrame:
    print(f"[open] {nc_path}")
    ds = xr.open_dataset(nc_path)
    print(f"  dims: {dict(ds.sizes)}")
    print(f"  time range: {pd.to_datetime(ds.time.min().values)} ~ {pd.to_datetime(ds.time.max().values)}")
    print(f"  variables: {list(ds.data_vars)}")

    times = ds.time.values
    rows = []
    for name, region, lat, lon in STATIONS:
        # HadISST 의 longitude 가 -179.5 ~ 179.5 라면 동일, 0-360 면 변환
        lon_max = float(ds.longitude.max())
        lon_q = lon + 360 if (lon_max > 180 and lon < 0) else lon
        actual_lat, actual_lon, values = find_nearest_ocean(ds, lat, lon_q)
        n_valid = int(np.sum(~np.isnan(values)))
        # HadISST 1° fallback 검출: 거리 > 0.6° 이면 fallback
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
    path = download_and_unpack()
    df = extract_stations(path)
    out_csv = DATA_DIR / "hadisst_13stations_monthly.csv"
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
