#!/usr/bin/env python3
"""Monthly MHW 식별 — Hobday 2016 의 monthly variant.

이미 가지고 있는 OISST v2.1 monthly 자료 활용 (ERDDAP daily 가 timeout):
- 1991-2020 monthly climatology + 90 percentile per month
- 1981-2026 monthly anomaly
- monthly threshold cross + 연속 2+ months → monthly MHW event

표준 Hobday 2016 (5-day window) 보다 거친 정의이지만 monthly trend·event 식별엔 충분.
정확한 daily MHW (Hobday 5-day) 는 ERDDAP timeout 해결 후 별도 작업.

산출:
- data/sst-global/mhw/monthly_climatology.csv (정점·월별 mean + p90)
- data/sst-global/mhw/monthly_events.csv (MHW events)
- data/sst-global/mhw/monthly_summary.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

WIKI = Path(__file__).resolve().parent.parent.parent
OUT = WIKI / "data" / "sst-global" / "mhw"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> int:
    df = pd.read_csv(WIKI / "data" / "sst-global" / "oisst_v21_13stations_monthly.csv",
                     parse_dates=["date"])
    df = df.dropna(subset=["sst_c"]).copy()
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    print(f"OISST monthly rows: {len(df)}, stations: {df['station'].nunique()}")

    # Climatology baseline 1991-2020
    base = df[(df["year"] >= 1991) & (df["year"] <= 2020)].copy()
    clim = (base.groupby(["station", "month"])["sst_c"]
                 .agg(["mean", lambda s: s.quantile(0.9)])
                 .reset_index())
    clim.columns = ["station", "month", "clim_mean", "clim_p90"]
    clim.to_csv(OUT / "monthly_climatology.csv", index=False, float_format="%.4f")
    print(f"climatology saved: {len(clim)} (13 stations × 12 months)")

    # merge
    df = df.merge(clim, on=["station", "month"], how="left")
    df["anomaly"] = df["sst_c"] - df["clim_mean"]
    df["over"] = df["sst_c"] > df["clim_p90"]

    # Event detection: 연속 2+ months threshold 초과 → event
    summary = {"stations": {}}
    all_events = []
    for st in df["station"].unique():
        sub = df[df["station"] == st].sort_values("date").reset_index(drop=True)
        events = []
        in_evt = False
        start_idx = None
        for i, ov in enumerate(sub["over"].values):
            if ov and not in_evt:
                start_idx = i
                in_evt = True
            elif not ov and in_evt:
                if i - start_idx >= 2:  # 2 months minimum
                    seg = sub.iloc[start_idx:i]
                    events.append({
                        "station": st,
                        "start": seg["date"].iloc[0].strftime("%Y-%m"),
                        "end": seg["date"].iloc[-1].strftime("%Y-%m"),
                        "duration_months": int(i - start_idx),
                        "max_anomaly_c": float(seg["anomaly"].max()),
                        "mean_anomaly_c": float(seg["anomaly"].mean()),
                        "max_sst_c": float(seg["sst_c"].max()),
                    })
                in_evt = False
        # tail
        if in_evt and len(sub) - start_idx >= 2:
            seg = sub.iloc[start_idx:]
            events.append({
                "station": st,
                "start": seg["date"].iloc[0].strftime("%Y-%m"),
                "end": seg["date"].iloc[-1].strftime("%Y-%m"),
                "duration_months": int(len(sub) - start_idx),
                "max_anomaly_c": float(seg["anomaly"].max()),
                "mean_anomaly_c": float(seg["anomaly"].mean()),
                "max_sst_c": float(seg["sst_c"].max()),
            })
        all_events.extend(events)

        summary["stations"][st] = {
            "region": sub["region"].iloc[0],
            "n_events": len(events),
            "total_over_months": int(sub["over"].sum()),
            "n_months_data": len(sub),
            "max_anomaly_c": float(max([e["max_anomaly_c"] for e in events])) if events else 0.0,
            "longest_event_months": int(max([e["duration_months"] for e in events])) if events else 0,
        }
    pd.DataFrame(all_events).to_csv(OUT / "monthly_events.csv", index=False, float_format="%.3f")
    with open(OUT / "monthly_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"events saved: {len(all_events)}")

    # 출력: 정점별 최근 events
    print("\n=== 정점별 최근 5 events (2010+) ===")
    for st in df["station"].unique():
        sub_evts = [e for e in all_events if e["station"] == st]
        recent = sorted([e for e in sub_evts if e["start"] >= "2010"], key=lambda e: e["start"])
        if recent:
            print(f"\n[{st}] {summary['stations'][st]['region']}, total {len(sub_evts)} events")
            for e in recent[-5:]:
                print(f"  {e['start']}~{e['end']} ({e['duration_months']}mo) "
                      f"max_anom={e['max_anomaly_c']:+.2f}°C max_sst={e['max_sst_c']:.2f}°C")

    return 0


if __name__ == "__main__":
    sys.exit(main())
