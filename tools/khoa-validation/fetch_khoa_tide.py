#!/usr/bin/env python3
"""KHOA 조위 시계열 다운로드 — 15정점 2025년 1년치 (시간별)

출력: data/<obs_code>_2025.csv (시각 KST, bscTdlvHgt 예측, tdlvHgt 실측, cm)
재실행 시 이미 받은 정점은 skip.
"""
import urllib.request
import json
import csv
import time
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

KEY = os.environ.get('KHOA_API_KEY')
if not KEY:
    sys.stderr.write("ERROR: KHOA_API_KEY env var not set. Get one from data.go.kr → tideObsRecent.\n")
    sys.exit(1)
OUT_DIR = Path(__file__).parent / "data"
LOG_DIR = Path(__file__).parent / "logs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# 15 정점: 해역별 골고루
STATIONS = [
    # 서해 5
    ("DT_0001", "인천",       "west"),
    ("DT_0018", "군산",       "west"),
    ("DT_0007", "목포",       "west"),
    ("DT_0025", "보령",       "west"),
    ("DT_0067", "안흥",       "west"),
    # 남해 5
    ("DT_0005", "부산",       "south"),
    ("DT_0020", "울산",       "south"),
    ("DT_0014", "통영",       "south"),
    ("DT_0016", "여수",       "south"),
    ("DT_0049", "광양",       "south"),
    # 동해 3
    ("DT_0006", "묵호",       "east"),
    ("DT_0091", "포항",       "east"),
    ("DT_0012", "속초",       "east"),
    # 제주 2
    ("DT_0004", "제주",       "jeju"),
    ("DT_0010", "서귀포",     "jeju"),
]

YEAR = 2025
SLEEP = 0.6  # API rate limit (1초 미만이면 다소 빠름, 너무 빠르면 차단)

def fetch_day(obs_code, ymd):
    """한 정점 하루치 hourly 데이터 반환 (24 records)."""
    url = (f"https://apis.data.go.kr/1192136/surveyTideLevel/GetSurveyTideLevelApiService"
           f"?serviceKey={KEY}&type=json&obsCode={obs_code}&reqDate={ymd}&min=60&numOfRows=24")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        j = json.loads(r.read())
    if j.get('header', {}).get('resultCode') != '00':
        return None, j.get('header', {}).get('resultMsg', '?')
    items = j.get('body', {}).get('items', {}).get('item', [])
    if not isinstance(items, list):
        items = [items]
    return items, None

def fetch_station(obs_code, obs_name, region, log_f):
    out_csv = OUT_DIR / f"{obs_code}_{YEAR}.csv"
    if out_csv.exists():
        with open(out_csv) as f:
            n = sum(1 for _ in f) - 1
        print(f"[SKIP] {obs_code} {obs_name}: 이미 다운로드됨 ({n} rows)", file=log_f, flush=True)
        return n

    print(f"[START] {obs_code} {obs_name} ({region}) {YEAR}년 다운로드 시작 — {datetime.now().isoformat()}", file=log_f, flush=True)
    start = datetime(YEAR, 1, 1)
    end = datetime(YEAR, 12, 31)
    total_rows = 0
    fail_days = 0

    with open(out_csv, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["obs_code", "obs_name", "lat", "lon", "t_kst", "bscTdlvHgt_cm", "tdlvHgt_cm"])
        d = start
        while d <= end:
            ymd = d.strftime("%Y%m%d")
            try:
                items, err = fetch_day(obs_code, ymd)
                if items is None:
                    fail_days += 1
                    if fail_days <= 3:
                        print(f"  [FAIL] {obs_code} {ymd}: {err}", file=log_f, flush=True)
                else:
                    for it in items:
                        w.writerow([obs_code, obs_name,
                                    it.get('lat',''), it.get('lot',''),
                                    it.get('obsrvnDt',''),
                                    it.get('bscTdlvHgt',''),
                                    it.get('tdlvHgt','')])
                    total_rows += len(items)
            except Exception as e:
                fail_days += 1
                if fail_days <= 3:
                    print(f"  [ERR] {obs_code} {ymd}: {e}", file=log_f, flush=True)
            d += timedelta(days=1)
            time.sleep(SLEEP)
            # progress every 30 days
            if d.day == 1:
                print(f"  [PROG] {obs_code} {obs_name}: {ymd} 완료, {total_rows} rows", file=log_f, flush=True)

    print(f"[DONE] {obs_code} {obs_name}: {total_rows} rows, {fail_days} fail days — {datetime.now().isoformat()}", file=log_f, flush=True)
    return total_rows

if __name__ == "__main__":
    log_path = LOG_DIR / f"fetch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    with open(log_path, 'w') as log_f:
        print(f"=== Fetch start {datetime.now().isoformat()} ===", file=log_f, flush=True)
        print(f"Stations: {len(STATIONS)}, Year: {YEAR}, Sleep: {SLEEP}s", file=log_f, flush=True)
        grand_total = 0
        for obs_code, obs_name, region in STATIONS:
            n = fetch_station(obs_code, obs_name, region, log_f)
            grand_total += n
        print(f"=== Fetch complete: {grand_total} total rows — {datetime.now().isoformat()} ===", file=log_f, flush=True)
    print(f"Log: {log_path}")
