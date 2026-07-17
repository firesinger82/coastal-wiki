#!/usr/bin/env python3
"""test_scan_runs_feedback.py — scan-runs-feedback.py 회귀 (RUNS-CHANNEL §3.3).

검증: ① 관찰노트 id 추출(블록 경계 — 다음 최상위 키 오염 없음) ② 원장 ack
대조(2건 중 1건 ack → unacked 1건) ③ runs-root 부재 exit 2 ④ 전건 ack → 0건.
"""
import importlib.util
import os
import sys
import tempfile
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "srf", os.path.join(HERE, "scan-runs-feedback.py"))
srf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(srf)

OBS = """---
model: ADCIRC
host: TESTHOST
wiki_feedback:
  - id: TESTHOST-20260717-tidal-gap-001
    type: gap
    destination: canonical
    target_ref: "unresolved"
    evidence: [runs/TESTHOST/x/metrics/a.csv]
    note: "one"
  - id: TESTHOST-20260717-tidal-gap-002
    type: promote-candidate
    destination: experience
    target_ref: "coastal-wiki@abc concepts/tide/01-concept.md §2"
    evidence: [runs/TESTHOST/x/metrics/b.csv]
    note: "two"
gate:
  reviewer: ""
---

## 관찰
본문.
"""

OBS_NO_FEEDBACK = """---
model: SWAN
host: TESTHOST
---

## 관찰
피드백 없음.
"""

failures = []


def check(name, cond, detail=""):
    if cond:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        failures.append(name)


def main():
    with tempfile.TemporaryDirectory() as td:
        runs = Path(td) / "coastal-runs"
        (runs / "observations" / "TESTHOST").mkdir(parents=True)
        (runs / "observations" / "TESTHOST" / "a.md").write_text(OBS, encoding="utf-8")
        (runs / "observations" / "TESTHOST" / "b.md").write_text(
            OBS_NO_FEEDBACK, encoding="utf-8")

        # ① id 추출 — 정확히 2건, gate 블록 미오염
        ids = srf.observation_ids(runs)
        check("extracts exactly the 2 feedback ids",
              [i for i, _ in ids] == ["TESTHOST-20260717-tidal-gap-001",
                                      "TESTHOST-20260717-tidal-gap-002"],
              f"got {ids}")

        # ② 원장 1건 ack → unacked 1건
        ledger = Path(td) / "ledger.yml"
        ledger.write_text(
            "entries:\n"
            "  - feedback_id: TESTHOST-20260717-tidal-gap-001\n"
            "    verdict: accepted\n", encoding="utf-8")
        orig = srf.LEDGER
        srf.LEDGER = ledger
        try:
            acked = srf.ledger_ids()
            check("ledger parse", acked == {"TESTHOST-20260717-tidal-gap-001"},
                  f"got {acked}")
            pending = [(f, p) for f, p in srf.observation_ids(runs) if f not in acked]
            check("1 unacked detected",
                  [f for f, _ in pending] == ["TESTHOST-20260717-tidal-gap-002"],
                  f"got {pending}")

            # ④ 전건 ack → 0건
            ledger.write_text(
                "entries:\n"
                "  - feedback_id: TESTHOST-20260717-tidal-gap-001\n"
                "  - feedback_id: TESTHOST-20260717-tidal-gap-002\n",
                encoding="utf-8")
            pending = [(f, p) for f, p in srf.observation_ids(runs)
                       if f not in srf.ledger_ids()]
            check("all acked → 0 pending", pending == [], f"got {pending}")
        finally:
            srf.LEDGER = orig

        # ③ runs-root 부재 → exit 2
        rc = srf.main(["--runs-root", str(Path(td) / "no-such-dir")])
        check("missing runs-root → exit 2", rc == 2, f"rc={rc}")

    print()
    if failures:
        print(f"FAIL: {len(failures)} case(s): {', '.join(failures)}")
        return 1
    print("OK: scan-runs-feedback 회귀 전부 통과")
    return 0


if __name__ == "__main__":
    sys.exit(main())
