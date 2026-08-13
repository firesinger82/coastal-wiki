#!/usr/bin/env python3
"""WO-20260728-reread §4 파일별 완료 프로토콜 집행 게이트.

역할(스크립트 허용 범위만): chunk manifest 실측 생성, chunk 순차 전달,
receipt 검증, EMIT_ALLOWED 토큰 발급, pending 수납. semantic content 는 만들지 않는다.

사용 (1차 판독자 에이전트가 호출):
  init  <axis> <MODEL> <NNN> <producer-slug>   → run_id 생성 + 전 파일 chunk manifest
  next  <run_id>                               → 현재 파일의 다음 chunk 본문 출력(직전 receipt 검증시에만)
  ack   <run_id> <json-receipt-한줄>           → receipt 검증·기록
  token <run_id>                               → 현재 파일 전 chunk ACK+eof 시 EMIT_ALLOWED 토큰 발급
  submit <run_id> <record-json-파일>           → pending/<run_id>/ 수납(토큰 발급된 파일만)
  status <run_id>
"""
import sys, os, json, hashlib, secrets, datetime

TR = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/firesinger/coastal-wiki/models"
CHUNK_LINES = 200

def sha(b): return hashlib.sha256(b).hexdigest()
def path_id(model, npath, src_sha): return sha(f"{model}\0{npath}\0{src_sha}".encode())

def load_state(run_id):
    p = f"{TR}/state/reread-20260728/{run_id}.json"
    return json.load(open(p)), p

def save_state(st, p): json.dump(st, open(p, "w"), ensure_ascii=False, indent=1)

def build_manifest(model, npath, run_id):
    full = os.path.join(ROOT, npath)
    raw = open(full, "rb").read()
    src = sha(raw)
    lines = raw.split(b"\n")
    final_nl = raw.endswith(b"\n") and len(raw) > 0
    wc_lf = raw.count(b"\n")
    logical = wc_lf + (1 if (len(raw) > 0 and not final_nl) else 0)
    body = lines[:-1] if final_nl else lines
    if len(raw) == 0: body = []
    chunks = []
    for i in range(0, len(body), CHUNK_LINES):
        seg = body[i:i+CHUNK_LINES]
        last_in_file = (i + CHUNK_LINES) >= len(body)
        seg_bytes = b"\n".join(seg) + (b"\n" if (not last_in_file or final_nl) else b"")
        chunks.append({"chunk_index": len(chunks), "first_line": i+1,
                       "last_line": min(i+CHUNK_LINES, len(body)),
                       "bytes": len(seg_bytes), "chunk_sha256": sha(seg_bytes)})
    m = {"model": model, "path": npath, "source_sha256": src, "source_bytes": len(raw),
         "total_chunks": len(chunks), "logical_lines": logical, "wc_lf_count": wc_lf,
         "final_newline": final_nl, "chunk_lines": CHUNK_LINES, "chunks": chunks}
    pid = path_id(model, npath, src)
    d = f"{TR}/chunk-manifests/reread-20260728/{run_id}"
    os.makedirs(d, exist_ok=True)
    mp = f"{d}/{pid}.json"
    with open(mp, "w") as f: json.dump(m, f, ensure_ascii=False, indent=1)
    m["_manifest_sha256"] = sha(open(mp, "rb").read())
    m["_path_id"] = pid
    return m

def chunk_bytes(npath, man, i):
    raw = open(os.path.join(ROOT, npath), "rb").read()
    lines = raw.split(b"\n")
    body = lines[:-1] if man["final_newline"] else lines
    if man["source_bytes"] == 0: body = []
    c = man["chunks"][i]
    seg = body[c["first_line"]-1:c["last_line"]]
    last_in_file = c["last_line"] >= len(body)
    return b"\n".join(seg) + (b"\n" if (not last_in_file or man["final_newline"]) else b"")

def cmd_init(axis, model, nnn, slug):
    shard = f"{TR}/shards/reread-20260728/{axis}-{model}-reread20260728-{nnn}.txt"
    paths = [l.rstrip("\n") for l in open(shard)]
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"reread20260728-{axis}-{model}-{nnn}-{slug}-{ts}-{secrets.token_hex(4)}"
    os.makedirs(f"{TR}/state/reread-20260728", exist_ok=True)
    os.makedirs(f"{TR}/chunk-receipts/reread-20260728/{run_id}", exist_ok=True)
    os.makedirs(f"{TR}/pending/reread-20260728/{run_id}", exist_ok=True)
    # 부속서01 §2: 수치격자 예외 path 는 mechanical 레코드로 충족 — 서빙 없이 skip 마킹
    exc = set()
    for exc_file in (f"{TR}/reread-queue/numeric-grid-exceptions-20260728.txt",
                     f"{TR}/reread-queue/numeric-bulk-exceptions-20260804.txt"):
        if os.path.exists(exc_file):
            for line in open(exc_file):
                if line.startswith("#"): continue
                parts = line.rstrip("\n").split("\t")
                if len(parts) == 4: exc.add(parts[3])
    files = []
    for p in paths:
        if p in exc:
            files.append({"path": p, "path_id": None, "source_sha256": None,
                          "manifest_sha256": None, "total_chunks": 0, "logical_lines": 0,
                          "acked": 0, "eof": True, "token_issued_at": None,
                          "submitted": True, "mechanical_exception": "numeric_grid"})
            continue
        m = build_manifest(model, p, run_id)
        files.append({"path": p, "path_id": m["_path_id"], "source_sha256": m["source_sha256"],
                      "manifest_sha256": m["_manifest_sha256"], "total_chunks": m["total_chunks"],
                      "logical_lines": m["logical_lines"], "acked": 0, "eof": False,
                      "token_issued_at": None, "submitted": False})
    st = {"run_id": run_id, "axis": axis, "model": model, "shard": os.path.basename(shard),
          "shard_sha256": sha(open(shard, "rb").read()), "producer_slug": slug,
          "cur_file": 0, "files": files}
    save_state(st, f"{TR}/state/reread-20260728/{run_id}.json")
    print(run_id)

def cur(st):
    while st["cur_file"] < len(st["files"]) and st["files"][st["cur_file"]]["submitted"]:
        st["cur_file"] += 1
    if st["cur_file"] >= len(st["files"]): return None
    return st["files"][st["cur_file"]]

def cmd_next(run_id):
    st, sp = load_state(run_id)
    f = cur(st)
    if f is None: sys.exit("run 종료: 모든 파일 완료")
    if f["eof"]: sys.exit(f"파일 {f['path']} 은 eof — token/submit 단계. (next 아님)")
    i = f["acked"]
    man = json.load(open(f"{TR}/chunk-manifests/reread-20260728/{run_id}/{f['path_id']}.json"))
    if i >= man["total_chunks"]: sys.exit("내부 오류: acked>=total 인데 eof 아님")
    c = man["chunks"][i]
    hdr = {"run_id": run_id, "path": f["path"], "source_sha256": f["source_sha256"],
           "chunk_index": i, "total_chunks": man["total_chunks"],
           "first_line": c["first_line"], "last_line": c["last_line"],
           "chunk_sha256": c["chunk_sha256"], "logical_lines": man["logical_lines"],
           "source_bytes": man["source_bytes"], "chunk_manifest_sha256": f["manifest_sha256"]}
    sys.stdout.write("CHUNK-HEADER\t" + json.dumps(hdr) + "\n")
    sys.stdout.flush()
    sys.stdout.buffer.write(chunk_bytes(f["path"], man, i))
    sys.stdout.buffer.write(b"\n===END-CHUNK===\n")

def cmd_ack(run_id, receipt_json):
    st, sp = load_state(run_id)
    f = cur(st)
    if f is None or f["eof"]: sys.exit("ack 불가 상태")
    i = f["acked"]
    man = json.load(open(f"{TR}/chunk-manifests/reread-20260728/{run_id}/{f['path_id']}.json"))
    c = man["chunks"][i]
    r = json.loads(receipt_json)
    exp_ack = f"ACK {i}/{man['total_chunks']} {c['last_line']} {c['chunk_sha256']}"
    checks = [r.get("run_id") == run_id, r.get("path") == f["path"],
              r.get("source_sha256") == f["source_sha256"], r.get("chunk_index") == i,
              r.get("first_line") == c["first_line"], r.get("last_line") == c["last_line"],
              r.get("chunk_sha256") == c["chunk_sha256"],
              r.get("last_line_seen") == c["last_line"], r.get("ack") == exp_ack,
              r.get("eof") == (i == man["total_chunks"] - 1)]
    if not all(checks):
        sys.exit(f"RECEIPT 불일치 (chunk {i}): 검사 {['OK' if x else 'FAIL' for x in checks]} — shard 실패 규정 §4.2.2")
    with open(f"{TR}/chunk-receipts/reread-20260728/{run_id}/{f['path_id']}.jsonl", "a") as fp:
        r["_gate_validated_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        fp.write(json.dumps(r, ensure_ascii=False) + "\n")
    f["acked"] = i + 1
    if f["acked"] == man["total_chunks"]: f["eof"] = True
    save_state(st, sp)
    print(f"ACK OK {i+1}/{man['total_chunks']}" + (" — eof, token 요청 가능" if f["eof"] else ""))

def cmd_token(run_id):
    st, sp = load_state(run_id)
    f = cur(st)
    if f is None or not f["eof"]: sys.exit("token 불가: eof 아님")
    tok = sha(f"EMIT_ALLOWED\0{run_id}\0{f['source_sha256']}\0{f['manifest_sha256']}".encode())
    f["token_issued_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    save_state(st, sp)
    print(tok)

import re as _re
# v5: 순수 수치 리터럴 name 판정 (Fortran kind 접미 `_SP`·지수표기 `E-06`·`D0` 포함)
NUMLIT_RE = _re.compile(r"^[-+]?(\d+\.?\d*|\.\d+)([eEdD][-+]?\d+)?(_\w+)?$")

def anchor_check(rec, npath, logical):
    """validator 동일 로직의 앵커 실재 검사 (스크립트 허용 범위: 앵커 검증만, content 는 만들지 않음).
    반환: 실패 항목 목록 [(field, name, loc, 사유)]

    ★집행 범위: constants·params_defined·equations 만 검사한다.
      entities·io·calls·verbatim_spans 는 이 함수가 검사하지 않는다(자가대조·맹검 소관).
      부속서01-code B-1 을 게이트가 전 필드에 강제한다고 오해하지 말 것.

    v4 (2026-08-11, 사용자 승인): name 에 식별자 토큰이 1개 이상 있고 그 토큰이 앵커 줄에
      실재할 것. 수치 부분일치로 통과시키던 v3 구멍을 막았다.
    v5 (2026-08-13, 사용자 승인 — Codex 적대검증 HIGH-1·HIGH-2 반영): v4 는 여전히
      (a) **부분문자열** 일치(`DT` 가 `DTMAX = 1.0` 을 통과)와
      (b) **다토큰 중 하나만** 일치(`DATA column_1` 이 `DATA(1) = 0.53` 을 통과 — 창작 라벨 동승)를
      허용했다. 실제로 doc-FUNWAVE-002 의 input.txt 에서 `SLP @L32`(실제 L31, L32 는 `Xslp`)·
      `PLOT_INTV @L49`(실제 L48, L49 는 `PLOT_INTV_STATION`) 계통 off-by-1 이 v4 를 통과했다.
      v5 규칙:
        N1 name **전체 문자열**이 앵커 줄에 문자 그대로(식별자 경계 포함) 실재해야 한다.
        N2 순수 수치 리터럴 name 금지 — 부속서01-code A-2(verbatim_spans) 로 처리한다.
      v4 의 '서술형 3토막' 제한은 폐기한다. N1 이 창작 라벨을 이미 차단하므로, 그 제한은
      `HOT START`·`!_TAG_FILE_FORMAT` 처럼 원문에 실재하는 정당한 토큰만 거짓 거부했다.
      1자 식별자(`g = 9.81`)는 정상 통과한다(v4 정규식과 동일).
    """
    import re
    raw = open(os.path.join(ROOT, npath), "rb").read().split(b"\n")
    def toks(s): return re.findall(r"[A-Za-z_][A-Za-z0-9_]{1,}", str(s))
    bad = []
    c8 = rec.get("content", {})
    for fld, keys in [("constants",("name","value")),("params_defined",("name","default")),("equations",("expr","ref"))]:
        for it in c8.get(fld, []) or []:
            loc = it.get("line") or it.get("loc")
            if not isinstance(loc, int) or not (1 <= loc <= max(logical,1)):
                bad.append((fld, str(it.get(keys[0]))[:30], loc, "범위밖")); continue
            rawline = raw[loc-1].decode("utf-8","replace") if loc-1 < len(raw) else ""
            line = rawline.lower()
            if fld in ("constants", "params_defined"):
                name = str(it.get("name", "")).strip()
                if not name:
                    bad.append((fld, "", loc, "name 비어 있음(v5)")); continue
                if NUMLIT_RE.match(name):
                    bad.append((fld, name[:40], loc,
                                "순수 수치 리터럴 name 금지(v5) — 부속서01-code A-2 로 처리")); continue
                if not re.search(r"(?<![A-Za-z0-9_])" + re.escape(name) + r"(?![A-Za-z0-9_])",
                                 rawline, re.I):
                    bad.append((fld, name[:40], loc,
                                f"name 전체 미실재(v5): {rawline.strip()[:60]!r}"))
                continue
            tt = toks(it.get(keys[0],"")) + toks(it.get(keys[1],""))
            nums = (re.findall(r"\d+\.?\d*", str(it.get(keys[0],""))) +
                    re.findall(r"\d+\.?\d*", str(it.get(keys[1],""))))[:5]
            if not tt and not nums: continue  # probe 불가 항목은 맹검 감사 소관
            if not any(t.lower() in line for t in tt) and not any(v in line for v in nums):
                bad.append((fld, str(it.get(keys[0]))[:30], loc, f"미실재: {line.strip()[:60]!r}"))
    return bad

def cmd_verify(run_id, rec_file):
    st, _ = load_state(run_id)
    f = cur(st)
    if f is None: sys.exit("run 종료 상태")
    rec = json.load(open(rec_file))
    man = json.load(open(f"{TR}/chunk-manifests/reread-20260728/{run_id}/{f['path_id']}.json"))
    bad = anchor_check(rec, f["path"], man["logical_lines"])
    if bad:
        print(f"VERIFY FAIL {len(bad)}건:")
        for b in bad: print("  ", b)
        sys.exit(1)
    print("VERIFY PASS — 전 앵커 실재 확인")

def cmd_submit(run_id, rec_file):
    st, sp = load_state(run_id)
    f = cur(st)
    if f is None or not f["eof"] or not f["token_issued_at"]: sys.exit("submit 불가: 토큰 미발급")
    rec = json.load(open(rec_file))
    if rec.get("path") != f["path"] or rec.get("source_sha256") != f["source_sha256"]:
        sys.exit("submit 거부: path/sha 불일치")
    man = json.load(open(f"{TR}/chunk-manifests/reread-20260728/{run_id}/{f['path_id']}.json"))
    # v4: 실측 필드 대조(§5.1) — bytes/lines/read_range 전사 실수 차단
    fld_bad = []
    if rec.get("bytes") != man["source_bytes"]:
        fld_bad.append(f"bytes={rec.get('bytes')} 실측={man['source_bytes']}")
    if rec.get("lines_or_pages") != man["logical_lines"]:
        fld_bad.append(f"lines_or_pages={rec.get('lines_or_pages')} 실측={man['logical_lines']}")
    if rec.get("read_range") != f"1-{man['logical_lines']}":
        fld_bad.append(f"read_range={rec.get('read_range')} 기대=1-{man['logical_lines']}")
    if rec.get("chunk_manifest_sha256") != f["manifest_sha256"]:
        fld_bad.append("chunk_manifest_sha256 불일치")
    if fld_bad:
        print("submit 거부 — 실측 필드 불일치(v4):")
        for b in fld_bad: print("  ", b)
        sys.exit(1)
    bad = anchor_check(rec, f["path"], man["logical_lines"])
    if bad:
        print(f"submit 거부 — 앵커 검사 실패 {len(bad)}건 (verify 로 확인·정정 후 재시도):")
        for b in bad[:10]: print("  ", b)
        sys.exit(1)
    dst = f"{TR}/pending/reread-20260728/{run_id}/{f['path_id']}.json"
    if os.path.exists(dst): sys.exit("submit 거부: 이미 존재(덮어쓰기 금지)")
    json.dump(rec, open(dst, "w"), ensure_ascii=False)
    f["submitted"] = True
    st["cur_file"] += 1
    save_state(st, sp)
    nxt = cur(st)
    print(f"수납 완료: {f['path']} → pending. " + (f"다음 파일: {nxt['path']}" if nxt else "shard 전 파일 완료"))

def cmd_status(run_id):
    st, _ = load_state(run_id)
    done = sum(1 for x in st["files"] if x["submitted"])
    print(f"{run_id}: {done}/{len(st['files'])} 파일 수납")
    f = cur(st)
    if f: print(f"현재: {f['path']} acked {f['acked']}/{f['total_chunks']} eof={f['eof']}")

if __name__ == "__main__":
    a = sys.argv[1:]
    try:
        {"init": lambda: cmd_init(*a[1:5]), "next": lambda: cmd_next(a[1]),
         "ack": lambda: cmd_ack(a[1], a[2]), "token": lambda: cmd_token(a[1]),
         "verify": lambda: cmd_verify(a[1], a[2]),
         "submit": lambda: cmd_submit(a[1], a[2]), "status": lambda: cmd_status(a[1])}[a[0]]()
    except (KeyError, IndexError):
        print(__doc__); sys.exit(2)
