#!/usr/bin/env python3
"""Codex 발주 입력 생성: final-classification.csv + line-ref-map.csv

좌표 매핑은 difflib opcode 기반 old→new 라인 맵으로 결정론적으로 산출한다.
Codex 가 줄 번호를 추정하지 않게 하는 것이 목적이다.
"""
import csv, difflib, re, sys
from pathlib import Path

WIKI = Path.home() / "coastal-wiki"
PRE = WIKI / "_staging/efdc-prescan"
OUT = WIKI / "_staging/efdc-migration"
OLD_ROOT = WIKI / "models/EFDC/raw/source_code/EFDCPlus_Stable"
sys.path.insert(0, str(WIKI / "_staging/model-migration-framework"))
import refparser as rp

# ---------- 1. 최종 분류 ----------
# Claude 최종 판정 = Codex 제안, 단 codex-16 은 RO→UR 승격 (transport_scheme 제목·요약)
UPGRADES = {("phase1", "16"): "UPDATE_REQUIRED"}
BATCH_FILES = [("phase1", "phase1-codex-review.csv"), ("B1", "phase2-B1-codex.csv"),
               ("B2", "phase2-B2-codex.csv"), ("C1", "phase2-C1-codex.csv"),
               ("C2", "phase2-C2-codex.csv")]
items = []
for batch, fn in BATCH_FILES:
    rd = csv.DictReader(open(PRE / fn))
    idk, linek = rd.fieldnames[0], rd.fieldnames[2]
    for r in rd:
        iid = r[idk].strip()
        cx = (r.get("proposed_classification") or "").strip()
        # B1 의 3번째 컬럼은 섹션 경로 문자열("… / claim L104") 이라 실제 줄번호를 추출한다
        raw_line = r[linek].strip()
        m = re.search(r"claim\s+L(\d+)", raw_line)
        nl = m.group(1) if m else raw_line
        items.append(dict(batch=batch, id=iid, note=r["note"].strip(),
                          note_line=nl, codex=cx,
                          final=UPGRADES.get((batch, iid), cx),
                          old_evidence=(r.get("old_source_evidence") or "").strip()))
with open(OUT / "final-classification.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["batch", "id", "note", "note_line", "codex", "final", "old_evidence"])
    w.writeheader(); w.writerows(items)
from collections import Counter
print("최종 분류:", Counter(i["final"] for i in items), "총", len(items))

# ---------- 2. old→new 라인 맵 ----------
def mangle(p): return "EFDC__" + p[len("EFDC/"):].replace("/", "__") if p.startswith("EFDC/") else p.replace("/", "__")

changed = {}
for r in csv.reader(open(PRE / "changed-files.csv")):
    if len(r) < 4 or r[1] == "status": continue
    status, old_p, new_p = r[1], r[2], r[3]
    changed[old_p] = (status, new_p)

linemaps, newlines_cache, missing = {}, {}, []
for old_p, (status, new_p) in changed.items():
    of, nf = OLD_ROOT / old_p, PRE / "new" / mangle(new_p)
    if not of.exists() or not nf.exists():
        missing.append((old_p, of.exists(), nf.exists())); continue
    o = of.read_text(errors="replace").splitlines()
    n = nf.read_text(errors="replace").splitlines()
    m = {}
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, o, n, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): m[i1 + k + 1] = j1 + k + 1
    linemaps[old_p] = m
    newlines_cache[old_p] = (o, n)
print(f"라인맵 생성 {len(linemaps)}개 파일, 소스 없음 {len(missing)}")
for x in missing: print("   MISSING:", x)

by_base = {}
for old_p in linemaps: by_base.setdefault(Path(old_p).name, []).append(old_p)

# ---------- 3. 노트 참조 스캔 ----------
NOTE_DIRS = [WIKI / "models/EFDC", WIKI / "concepts"]
cls_by_note = {}
for i in items:
    cls_by_note.setdefault(Path(i["note"]).name, set()).add(i["final"])

rows = []
for d in NOTE_DIRS:
    for md in sorted(d.rglob("*.md")):
        if "/raw/" in str(md) or "/_archive/" in str(md): continue
        try: refs = rp.parse_note(md.read_text(errors="replace"))
        except Exception: continue
        for r in refs:
            if r["kind"] != "file-line" or r["excluded"] or not r["ranges"]: continue
            base = Path(r["path"]).name
            if base not in by_base: continue
            cands = by_base[base]
            if len(cands) > 1:
                rows.append(dict(note=str(md.relative_to(WIKI)), note_line=r["line"], ref=r["raw"],
                                 source=base, old="|".join(cands), new="", status="AMBIGUOUS_SOURCE",
                                 note_class="/".join(sorted(cls_by_note.get(md.name, {"-"}))))); continue
            old_p = cands[0]; m = linemaps[old_p]; o, n = newlines_cache[old_p]
            mapped, flags = [], []
            keys = sorted(m)
            def anchor(x, direction):
                """매핑 불가 끝점 → 가장 가까운 매핑 가능 줄로 재앵커 후보 산출"""
                cand = [k for k in keys if k <= x] if direction < 0 else [k for k in keys if k >= x]
                return m[cand[-1] if direction < 0 else cand[0]] if cand else None
            for a, b in r["ranges"]:
                ma, mb = m.get(a), m.get(b)
                if ma is None or mb is None:
                    flags.append("REANCHOR_REQUIRED")
                    ca, cb = (ma or anchor(a, -1)), (mb or anchor(b, +1))
                    mapped.append((ca if ca else a, cb if cb else b)); continue
                ok = (o[a-1] == n[ma-1]) and (o[b-1] == n[mb-1])
                flags.append("IDENTICAL" if (ma, mb) == (a, b) else ("MOVED" if ok else "CONTENT_DIFF"))
                mapped.append((ma, mb))
            st = "REANCHOR_REQUIRED" if "REANCHOR_REQUIRED" in flags else \
                 "CONTENT_DIFF" if "CONTENT_DIFF" in flags else \
                 "IDENTICAL" if set(flags) == {"IDENTICAL"} else "MOVED"
            fmt = lambda rs: ",".join(f"{a}-{b}" if a != b else str(a) for a, b in rs)
            rows.append(dict(note=str(md.relative_to(WIKI)), note_line=r["line"], ref=r["raw"],
                             source=old_p, old=fmt(r["ranges"]), new=fmt(mapped), status=st,
                             note_class="/".join(sorted(cls_by_note.get(md.name, {"-"})))))

with open(OUT / "line-ref-map.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["note", "note_line", "ref", "source", "old", "new", "status", "note_class"])
    w.writeheader(); w.writerows(rows)
print("참조 매핑:", Counter(r["status"] for r in rows), "총", len(rows))
print("치환 대상(MOVED):", sum(1 for r in rows if r["status"] == "MOVED"),
      "| 노트 수:", len({r["note"] for r in rows if r["status"] == "MOVED"}))
