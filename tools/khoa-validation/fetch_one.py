#!/usr/bin/env python3
"""Single-station fetch — designed to run multiple instances in parallel."""
import os, sys, urllib.request, json, csv, time
from datetime import datetime, timedelta
from pathlib import Path

KEY = os.environ.get('KHOA_API_KEY')
if not KEY:
    sys.stderr.write("ERROR: KHOA_API_KEY env var not set. Get one from data.go.kr → tideObsRecent.\n")
    sys.exit(1)
ROOT = Path(__file__).parent
OUT_DIR = ROOT / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

YEAR = 2025
SLEEP = 0.3   # 병렬화 시 작게 (3 workers × 0.3s ≈ 한 IP에서 ~1 req/s)

def main(obs_code, obs_name):
    out_csv = OUT_DIR / f"{obs_code}_{YEAR}.csv"
    log_path = ROOT / "logs" / f"fetch_{obs_code}.log"

    # resume mode: if file exists with content, skip
    if out_csv.exists():
        with open(out_csv) as f:
            n = sum(1 for _ in f) - 1
        if n >= 8000:
            with open(log_path, 'a') as lf:
                print(f"[SKIP] {obs_code} {obs_name}: {n} rows already", file=lf, flush=True)
            return

    with open(log_path, 'a') as lf, open(out_csv, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["obs_code","obs_name","lat","lon","t_kst","bscTdlvHgt_cm","tdlvHgt_cm"])
        d = datetime(YEAR,1,1)
        end = datetime(YEAR,12,31)
        total = 0
        fails = 0
        print(f"=== START {obs_code} {obs_name} {datetime.now().isoformat()} ===", file=lf, flush=True)
        while d <= end:
            ymd = d.strftime("%Y%m%d")
            url = (f"https://apis.data.go.kr/1192136/surveyTideLevel/GetSurveyTideLevelApiService"
                   f"?serviceKey={KEY}&type=json&obsCode={obs_code}&reqDate={ymd}&min=60&numOfRows=24")
            try:
                req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=30) as r:
                    j = json.loads(r.read())
                if j.get('header',{}).get('resultCode') == '00':
                    items = j.get('body',{}).get('items',{}).get('item',[])
                    if not isinstance(items, list): items = [items]
                    for it in items:
                        w.writerow([obs_code, obs_name,
                                    it.get('lat',''), it.get('lot',''),
                                    it.get('obsrvnDt',''),
                                    it.get('bscTdlvHgt',''),
                                    it.get('tdlvHgt','')])
                    total += len(items)
                else:
                    fails += 1
            except Exception as e:
                fails += 1
                if fails <= 5:
                    print(f"  [ERR] {ymd}: {e}", file=lf, flush=True)
            d += timedelta(days=1)
            time.sleep(SLEEP)
            if d.day == 1:
                print(f"  [PROG] {ymd} → {total} rows, {fails} fails", file=lf, flush=True)
        print(f"=== DONE {obs_code}: {total} rows, {fails} fails {datetime.now().isoformat()} ===", file=lf, flush=True)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
