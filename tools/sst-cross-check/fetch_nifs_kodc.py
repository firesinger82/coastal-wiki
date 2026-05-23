#!/usr/bin/env python3
"""NIFS KODC 정선해양조사자료 JSON API 직접 호출 → SST 시계열 추출.

API: https://www.nifs.go.kr/kodc/api/observe/line/data/list
   params: sea, line, startDate, endDate, page, size
   response: JSON {total, size, page, list:[{lsta, staCd, lot, lat, msrmtDt(epoch ms), dpwt, wtem, slnty, ...}]}

제약:
- 최대 조회기간 5년/요청 → 1968-2025 (58년) 을 12 chunk
- size 무제한 (확인: 2737 records OK with size=10000)

산출:
- data/sst-global/nifs-kodc/raw_<sea>_<line>.json (각 정선 모든 chunk 합본)
- data/sst-global/nifs-kodc/all_raw.csv (전체 records normalize)
- data/sst-global/nifs-kodc/surface_annual.csv (dpwt<=10m, 정선·연도별 평균)
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests

WIKI = Path(__file__).resolve().parent.parent.parent
OUT = WIKI / "data" / "sst-global" / "nifs-kodc"
OUT.mkdir(parents=True, exist_ok=True)

BASE = "https://www.nifs.go.kr/kodc/api/observe/line/data"
HDR = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) coastal-wiki/0.1"}

# 5년 chunk 12개 (1968-01-01 ~ 2027-12-31; 마지막은 짧음)
CHUNKS = [
    ("1968-01-01", "1972-12-31"),
    ("1973-01-01", "1977-12-31"),
    ("1978-01-01", "1982-12-31"),
    ("1983-01-01", "1987-12-31"),
    ("1988-01-01", "1992-12-31"),
    ("1993-01-01", "1997-12-31"),
    ("1998-01-01", "2002-12-31"),
    ("2003-01-01", "2007-12-31"),
    ("2008-01-01", "2012-12-31"),
    ("2013-01-01", "2017-12-31"),
    ("2018-01-01", "2022-12-31"),
    ("2023-01-01", "2026-12-31"),
]

SEAS = ["동해", "서해", "남해", "동중국해"]


def get_lines(sea: str) -> list[str]:
    r = requests.get(f"{BASE}/lsta", params={"sea": sea}, headers=HDR, timeout=20)
    r.raise_for_status()
    return r.json().get("list", [])


def fetch_chunk(sea: str, line: str, start: str, end: str) -> list[dict]:
    params = {"sea": sea, "line": line, "startDate": start, "endDate": end,
              "page": 1, "size": 100000}
    r = requests.get(f"{BASE}/list", params=params, headers=HDR, timeout=120)
    r.raise_for_status()
    j = r.json()
    if j.get("total", 0) != len(j.get("list", [])):
        print(f"    WARN: total={j.get('total')}, returned={len(j.get('list', []))}")
    return j.get("list", [])


def main() -> int:
    log = OUT / "fetch.log"
    summary = []
    all_records = []
    for sea in SEAS:
        lines = get_lines(sea)
        print(f"\n[{sea}] {len(lines)} lines: {','.join(lines)}")
        for line in lines:
            line_records = []
            t0 = time.time()
            for start, end in CHUNKS:
                try:
                    recs = fetch_chunk(sea, line, start, end)
                    if recs:
                        line_records.extend(recs)
                    print(f"  {sea}-{line} [{start}~{end[:7]}] n={len(recs)}")
                    time.sleep(0.2)  # rate limit
                except Exception as e:
                    print(f"  ERR {sea}-{line} [{start}~{end}]: {e}")
            elapsed = time.time() - t0
            print(f"  {sea}-{line} total={len(line_records)} ({elapsed:.1f}s)")
            # 정선별 raw json 저장
            with open(OUT / f"raw_{sea}_{line}.json", "w", encoding="utf-8") as f:
                json.dump(line_records, f, ensure_ascii=False)
            # 전체 records 에도 추가
            for r in line_records:
                r["_sea"] = sea
                r["_line"] = line
            all_records.extend(line_records)
            summary.append({"sea": sea, "line": line, "n": len(line_records),
                            "elapsed_s": round(elapsed, 1)})

    # 전체 normalize → CSV
    df = pd.DataFrame(all_records)
    # 시각 변환: msrmtDt (epoch ms, KST 또는 UTC?)
    df["msrmtDt_iso"] = pd.to_datetime(df["msrmtDt"], unit="ms")
    df["year"] = df["msrmtDt_iso"].dt.year
    df["month"] = df["msrmtDt_iso"].dt.month

    out_csv = OUT / "all_raw.csv"
    df.to_csv(out_csv, index=False, float_format="%.4f")
    print(f"\n[saved] {out_csv}  ({len(df)} rows, {len(df.columns)} cols)")

    # 표층 (dpwt<=10) 정선·연도별 평균 SST
    surf = df[df["dpwt"] <= 10].copy()
    annual = (surf.dropna(subset=["wtem"])
                  .groupby(["_sea", "_line", "year"], as_index=False)
                  .agg(sst_mean=("wtem", "mean"),
                       n=("wtem", "count"),
                       n_months=("month", "nunique")))
    annual_csv = OUT / "surface_annual.csv"
    annual.to_csv(annual_csv, index=False, float_format="%.4f")
    print(f"[saved] {annual_csv}  ({len(annual)} rows)")

    # summary
    pd.DataFrame(summary).to_csv(OUT / "fetch_summary.csv", index=False)
    print(f"[saved] {OUT}/fetch_summary.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
