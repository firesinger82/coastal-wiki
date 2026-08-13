#!/usr/bin/env python3
"""오케스트레이터 전용 — 현재 파일의 ack 상태를 '시작 전'으로 되돌린다.

용도: 판독자가 chunk 를 ack 한 뒤 레코드 제출 전에 중단하면, 그 판독 내용은 컨텍스트와
함께 소실된다. 게이트는 eof 상태라 next 를 재서빙하지 않고 token 만 발급 가능하므로,
새 판독자는 원문을 모르는 채 레코드를 써야 하는 상황에 몰린다(= 날조 유인).
WO §4 '부분판독 승계 금지' 선례(2026-07-28 code-FUNWAVE-003 tide_frf plot_time_series.m)대로
acked=0·eof=False·token 회수 + 해당 파일 receipt 삭제로 chunk 0 부터 재서빙시킨다.

★submitted=True 인 파일은 절대 건드리지 않는다. content 를 만들지도 읽지도 않는다.
"""
import sys, os, json, shutil, datetime

TR = os.path.dirname(os.path.abspath(__file__))

def main():
    run_id = sys.argv[1]
    apply = "--apply" in sys.argv
    sp = f"{TR}/state/reread-20260728/{run_id}.json"
    st = json.load(open(sp))

    i = st["cur_file"]
    while i < len(st["files"]) and st["files"][i]["submitted"]:
        i += 1
    if i >= len(st["files"]):
        sys.exit("초기화 대상 없음 — shard 전 파일 수납 완료")
    f = st["files"][i]

    print(f"run_id : {run_id}")
    print(f"대상   : {f['path']}")
    print(f"현재   : acked {f['acked']}/{f['total_chunks']}  eof={f['eof']}  token={'발급' if f['token_issued_at'] else '미발급'}")
    if f["submitted"]:
        sys.exit("★대상이 이미 submitted — 중단(수납분 불가침)")

    rc = f"{TR}/chunk-receipts/reread-20260728/{run_id}/{f['path_id']}.jsonl"
    n_rc = sum(1 for _ in open(rc)) if os.path.exists(rc) else 0
    print(f"receipt: {n_rc}행 ({'있음' if n_rc else '없음'})")
    print(f"초기화 후: acked 0/{f['total_chunks']}  eof=False  token 회수  receipt 삭제")

    if not apply:
        print("\n[DRY RUN] --apply 로 실행")
        return

    if os.path.exists(rc):
        bak = f"{TR}/chunk-receipts/reread-20260728/{run_id}/{f['path_id']}.jsonl.reset-{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
        shutil.move(rc, bak)          # 삭제가 아니라 보존 이동 (감사 추적)
        print(f"receipt 보존 이동 → {os.path.basename(bak)}")

    f["acked"] = 0
    f["eof"] = False
    f["token_issued_at"] = None
    st.setdefault("_resets", []).append({
        "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "path": f["path"],
        "reason": "판독자 중단으로 판독 내용 소실 — 부분판독 승계 금지(WO §4), chunk 0 재서빙",
        "receipts_moved": n_rc,
    })
    json.dump(st, open(sp, "w"), ensure_ascii=False, indent=1)
    print("상태 초기화 완료 — GATE next 가 chunk 0 부터 재서빙한다")

main()
