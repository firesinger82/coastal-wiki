#!/usr/bin/env python3
"""2026-08-13 처분: code·note 269 + doc-FUNWAVE-002 41 을 pending-superseded 로 격리.

선례(20260811-modelid·20260811-anchorrule)와 동일 절차:
  ① 이동 전 파일별 sha256 실측  ② 이동  ③ 이동 후 sha256 재실측·대조  ④ manifest.json 기록
삭제하지 않는다. canonical records/ 는 접촉하지 않는다.
"""
import os, sys, json, glob, shutil, hashlib, datetime

TR = os.path.dirname(os.path.abspath(__file__))
SRC = f"{TR}/pending/reread-20260728"
DST = f"{TR}/pending-superseded/20260813-namerule"

TARGET_DOC_SHARD = "reread20260728-doc-FUNWAVE-002-codex-20260811T012259Z-e0440617"

def sha256f(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def main():
    dry = "--apply" not in sys.argv
    runs = []
    for d in sorted(os.listdir(SRC)):
        if "-code-" in d or "-note-" in d or d == TARGET_DOC_SHARD:
            runs.append(d)
    if not runs:
        sys.exit("대상 run 없음")

    manifest = {
        "superseded_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "reason": ("프롬프트 code-v3 자기모순(29행 bare 식별자 vs 31행 첫 토큰) 으로 생산된 "
                   "수치 리터럴 name 결함 + 게이트 v4 의 부분문자열·다토큰 통과 구멍으로 살아남은 "
                   "off-by-1 앵커. 사용자 처분 2026-08-13(§5.2 무관용): 결함 shard 전체 재판독 + "
                   "게이트 v5 + 프롬프트 code-v4(부속서01-code). 원인 분류상 창작 라벨은 0건."),
        "gate": "reread_gate_20260728.py v5 (anchor_check N1 name 전체 실재 + N2 수치 리터럴 금지)",
        "prompt_code_v4_sha256": "13b91717e70bf4f9a21debb94a80bf6e91de480e419fc04e843d050086574153",
        "annex01_code_sha256": "c0b4fe5591c081fbe3cb540c0317898b037bb9509f3993005663fcc1e58858e2",
        "workorder": "WO-20260728-amendment-03.md",
        "runs": {},
    }

    total = 0
    for run in runs:
        files = sorted(glob.glob(f"{SRC}/{run}/*.json"))
        entries = []
        for f in files:
            r = json.load(open(f))
            entries.append({
                "file": os.path.basename(f),
                "sha256": sha256f(f),
                "path": r.get("path"),
                "reader": r.get("reader"),
                "run_id": r.get("run_id"),
            })
        manifest["runs"][run] = {"records": len(entries), "entries": entries}
        total += len(entries)
        axis = run.split("-")[1]
        print(f"  {axis:5s} {run[-8:]}  {len(entries):3d}건  {run}")

    print(f"\n격리 대상 합계: {total}건 / {len(runs)} run")
    if dry:
        print("\n[DRY RUN] --apply 를 붙이면 실제 이동한다.")
        return

    os.makedirs(DST, exist_ok=True)
    moved, verified = 0, 0
    for run in runs:
        shutil.move(f"{SRC}/{run}", f"{DST}/{run}")
        moved += 1
        for e in manifest["runs"][run]["entries"]:
            p = f"{DST}/{run}/{e['file']}"
            if not os.path.exists(p):
                sys.exit(f"★이동 후 파일 부재: {p}")
            if sha256f(p) != e["sha256"]:
                sys.exit(f"★이동 후 sha256 불일치: {p}")
            verified += 1
    json.dump(manifest, open(f"{DST}/manifest.json", "w"), ensure_ascii=False, indent=1)
    print(f"\n이동 {moved} run / sha256 재검증 {verified}건 전건 일치")
    print(f"manifest: {DST}/manifest.json")

main()
