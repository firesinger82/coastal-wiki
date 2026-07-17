#!/usr/bin/env python3
"""count-notes.py — 노트 개수 실측 + 원장 대조 (F-1, 2026-07-12 Codex 검토 반영).

문서(원장·INDEX)에 하드코딩된 노트 개수의 드리프트를 차단한다.
  기본:      모델별 source-analysis/manual-notes + theory 노트 실측 출력
  --check:   AUDIT-LEDGER 대시보드의 "✅ N 노트" 와 실측 SA 를 대조, 불일치 시 exit 1
  --json:    기계가독 출력

제외 규칙: README.md 미계수. raw/·_archive/ 밖의 .md 만.
"""
import json
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()

MODELS = ["SWASH", "Delft3D", "ROMS", "FUNWAVE", "ADCIRC", "EFDC", "XBeach",
          "SWAN", "Celeris", "SFINCS", "LISFLOOD-FP", "CADMAS-SURF"]


def count(subdir):
    base = os.path.join(ROOT, subdir)
    if not os.path.isdir(base):
        return None
    n = 0
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in ("raw", "_archive")]
        n += sum(1 for f in filenames if f.endswith(".md") and f != "README.md")
    return n


def measure():
    out = {}
    for m in MODELS:
        out[m] = {
            "SA": count(f"models/{m}/source-analysis"),
            "MN": count(f"models/{m}/manual-notes"),
        }
    theory = 0
    notes_dir = os.path.join(ROOT, "textbook/notes")
    for f in os.listdir(notes_dir):
        if f.startswith("theory-") and f.endswith(".md"):
            theory += 1
    out["_theory_notes"] = theory
    return out


def check(data):
    ledger = open(os.path.join(ROOT, "models/AUDIT-LEDGER.md"), encoding="utf-8").read()
    fails = []
    for m in MODELS:
        row = re.search(
            rf"^\|\s*\*\*{re.escape(m)}\*\*[^\n]*?✅\s*(\d+)\s*노트", ledger, re.M
        )
        if not row:
            print(f"  ? {m}: 대시보드 행에서 '✅ N 노트' 패턴 미발견 — 수동 확인")
            continue
        claimed = int(row.group(1))
        actual = data[m]["SA"]
        mark = "OK" if claimed == actual else "MISMATCH"
        if claimed != actual:
            fails.append(f"{m}: 대시보드 {claimed} vs 실측 {actual}")
        print(f"  [{mark}] {m}: 대시보드 {claimed} / 실측 SA {actual}")
    # theory parity (R1 I-1e, Codex 20회차): THEORY-LEDGER 대시보드의 노트 링크 수 vs 실측
    tl = open(os.path.join(ROOT, "textbook/THEORY-LEDGER.md"), encoding="utf-8").read()
    dash = tl.split("## 게이트 기록")[0]
    ledger_theory = len(set(re.findall(r"\]\((notes/theory-[^)]+\.md)\)", dash)))
    actual_theory = data["_theory_notes"]
    mark = "OK" if ledger_theory == actual_theory else "MISMATCH"
    if ledger_theory != actual_theory:
        fails.append(f"theory: THEORY-LEDGER 링크 {ledger_theory} vs 실측 {actual_theory}")
    print(f"  [{mark}] theory: THEORY-LEDGER 대시보드 링크 {ledger_theory} / 실측 {actual_theory}")
    if fails:
        print(f"[count-notes] --check FAIL {len(fails)}건:")
        for f in fails:
            print(f"  ✗ {f}")
        return 1
    print("[count-notes] --check OK: 대시보드 SA + theory 카운트 전부 실측 일치.")
    return 0


def main():
    data = measure()
    if "--json" in sys.argv:
        print(json.dumps(data, ensure_ascii=False, indent=1))
        return 0
    if "--check" in sys.argv:
        return check(data)
    for m in MODELS:
        print(f"{m}: SA {data[m]['SA']} / MN {data[m]['MN']}")
    print(f"theory 노트(textbook/notes/theory-*): {data['_theory_notes']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
