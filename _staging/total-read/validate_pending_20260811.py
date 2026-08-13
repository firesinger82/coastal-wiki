#!/usr/bin/env python3
"""pending semantic 레코드 기계검증 (WO-20260728 §5.1 부분집합, 오케스트레이터/validator 역할).

게이트의 submit 내장 검사(앵커 실재 probe)가 통과시키는 다음 결함을 잡는다:
  E1 bytes/lines_or_pages/sha256 실측 불일치
  E2 constants/params_defined 의 name 이 앵커 줄에 토큰으로 실재하지 않음(창작 라벨)
  E3 필수 필드 결측 / 금지 판단필드 존재 / read_status·comprehension_status 비 complete
  E4 reader·producer 가 실측 런타임 model-id 와 불일치(허용목록 인자로 전달)

content 를 생성·보정하지 않는다. 검출·보고만 한다.

사용: python3 validate_pending_20260811.py [run_id-glob] [--expect-reader openai/gpt-5.6-sol]
"""
import sys, os, json, glob, hashlib, re

# v5: 게이트 reread_gate_20260728.py 의 NUMLIT_RE 와 동일해야 한다 (두 곳이 갈리면 안 됨)
NUMLIT_RE = re.compile(r"^[-+]?(\d+\.?\d*|\.\d+)([eEdD][-+]?\d+)?(_\w+)?$")

TR = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/firesinger/coastal-wiki/models"
BANNED = ("note_worthy", "importance", "tier", "core")
REQUIRED = ("axis", "model", "path", "sha256", "bytes", "lines_or_pages", "read_status",
            "read_range", "reader", "read_at", "artifact_class", "producer", "read_method",
            "comprehension_status", "source_sha256", "chunk_manifest_sha256", "prompt_sha256",
            "run_id", "auditor", "audit_seed", "audit_status", "content")
CONTENT8 = ("what_it_is", "entities", "constants", "params_defined", "equations", "io",
            "calls", "verbatim_spans", "unresolved")


def banned_keys(o, hits):
    if isinstance(o, dict):
        for k, v in o.items():
            if k.lower() in BANNED: hits.append(k)
            banned_keys(v, hits)
    elif isinstance(o, list):
        for v in o: banned_keys(v, hits)


def check(rec_path, expect_reader):
    r = json.load(open(rec_path))
    errs = []
    for k in REQUIRED:
        if k not in r: errs.append(("E3", f"필드 결측 {k}", None))
    c = r.get("content", {})
    for k in CONTENT8:
        if k not in c: errs.append(("E3", f"content 필드 결측 {k}", None))
    if r.get("read_status") != "complete" or r.get("comprehension_status") != "complete":
        errs.append(("E3", f"complete 아님 {r.get('read_status')}/{r.get('comprehension_status')}", None))
    hits = []; banned_keys(r, hits)
    if hits: errs.append(("E3", f"금지 판단필드 {sorted(set(hits))}", None))

    src = os.path.join(ROOT, r.get("path", ""))
    if not os.path.exists(src):
        errs.append(("E1", "원문 부재", r.get("path")))
        return r, errs
    raw = open(src, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    lf = raw.count(b"\n")
    logical = lf + (1 if (raw and not raw.endswith(b"\n")) else 0)
    if r.get("sha256") != sha: errs.append(("E1", f"sha256 불일치 rec={r.get('sha256','')[:12]} 실측={sha[:12]}", None))
    if r.get("source_sha256") != sha: errs.append(("E1", "source_sha256 불일치", None))
    if r.get("bytes") != len(raw): errs.append(("E1", f"bytes rec={r.get('bytes')} 실측={len(raw)}", None))
    if r.get("lines_or_pages") != logical: errs.append(("E1", f"lines rec={r.get('lines_or_pages')} 실측={logical}", None))
    if r.get("read_range") != f"1-{logical}": errs.append(("E1", f"read_range={r.get('read_range')} 기대=1-{logical}", None))

    if expect_reader:
        if r.get("reader") != expect_reader: errs.append(("E4", f"reader={r.get('reader')}", None))
        if r.get("producer") != "llm:" + expect_reader: errs.append(("E4", f"producer={r.get('producer')}", None))

    lines = raw.split(b"\n")
    for fld in ("constants", "params_defined"):
        for it in (c.get(fld) or []):
            name = str(it.get("name", "")).strip()
            loc = it.get("line") if it.get("line") is not None else it.get("loc")
            if not isinstance(loc, int) or not (1 <= loc <= max(logical, 1)):
                errs.append(("E2", f"{fld} '{name[:28]}' loc 범위밖 {loc}", None)); continue
            txt = lines[loc - 1].decode("utf-8", "replace")
            # v5 (2026-08-13): 게이트 anchor_check 와 동일 규칙.
            #   N1 name 전체가 앵커 줄에 경계 포함 실재 / N2 순수 수치 리터럴 금지.
            # v4 의 'ASCII bare 식별자 강제'는 폐기 — `ε`·`%%BoundingBox` 처럼 원문에 실재하는
            # 비ASCII·비식별자 토큰을 거짓 적발했다(파일럿 note-000 에서 적발). 판단 기준은
            # 식별자 문법이 아니라 원문 실재다.
            if not name:
                errs.append(("E2", f"{fld} name 비어 있음 @L{loc}", None)); continue
            if NUMLIT_RE.match(name):
                errs.append(("E2", f"{fld} 순수 수치 리터럴 name(v5): {name[:40]!r} @L{loc}", None)); continue
            if not re.search(r"(?<![A-Za-z0-9_])" + re.escape(name) + r"(?![A-Za-z0-9_])", txt, re.I):
                errs.append(("E2", f"{fld} '{name[:28]}' @L{loc} 전체 미실재(v5): {txt.strip()[:60]!r}", None))
    # A-2 남용 방지: 내용이 있는 파일에서 세 필드가 모두 빈 배열이면 부실 판독.
    # '내용 있음' 판정은 행 수가 아니라 **공백 아닌 문자의 존재**로 한다 — cpp 전처리 잔해처럼
    # 개행만 남은 파일(예: build/pre/mod_foam.f90 = 11바이트 전부 개행)은 기록할 항목이 실제로
    # 없으므로 세 필드가 비는 것이 정직한 기록이다(2026-08-13 파일럿 후속에서 거짓 적발로 확인).
    if raw.strip() and not (c.get("constants") or c.get("params_defined") or c.get("verbatim_spans")):
        errs.append(("E5", "constants·params_defined·verbatim_spans 가 모두 빈 배열 (부속서01 A-2 위반)", None))
    return r, errs


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    expect = None
    if "--expect-reader" in sys.argv:
        expect = sys.argv[sys.argv.index("--expect-reader") + 1]
        args = [a for a in args if a != expect]
    pat = args[0] if args else "*"
    files = sorted(glob.glob(f"{TR}/pending/reread-20260728/{pat}/*.json"))
    bad = 0
    per_run = {}
    for f in files:
        run = os.path.basename(os.path.dirname(f))
        r, errs = check(f, expect)
        per_run.setdefault(run, [0, 0])
        per_run[run][0] += 1
        if errs:
            bad += 1
            per_run[run][1] += 1
            print(f"\n[FAIL] {r.get('path')}")
            print(f"       {os.path.basename(f)}")
            for code, msg, _ in errs[:6]:
                print(f"       {code} {msg}")
            if len(errs) > 6: print(f"       … 외 {len(errs)-6}건")
    print(f"\n=== 검사 {len(files)}건 / 결함 {bad}건 ===")
    for run, (n, b) in sorted(per_run.items()):
        print(f"  {run.split('-')[1]}-{run.split('-')[3]} {run[-8:]}: {n}건 중 결함 {b}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
