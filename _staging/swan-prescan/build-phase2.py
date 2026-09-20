#!/usr/bin/env python3
"""SWAN Phase 2 입력 — line-ref-map + excluded-refs ledger.

DESIGN v2.0 §AUTOMATION BOUNDARY 4: 범위 내부가 바뀐 참조는
Phase 1 에서 판정된 지점만 자동 치환하고, 나머지는 NEEDS_CLAUDE_REVIEW.
"""
import csv, difflib, subprocess, sys
from pathlib import Path
from collections import Counter

W = Path.home()/"coastal-wiki"; OUT = W/"_staging/swan-prescan"
STG = Path.home()/".cache/coastal-snapshots/swan-43e9bbb"
OLD, NEW = "55441526ec4330338f05d148759fc66f6fc7fb9d", "43e9bbba393f2cf9eaff78bc92eaed118a3a5c8e"
sys.path.insert(0, str(W/"_staging/model-migration-framework")); import refparser as rp

def git(*a): return subprocess.run(["git","-c","safe.directory=*","-C",str(STG),*a],
                                   capture_output=True, text=True).stdout

changed = {}
for line in git("diff","--name-status",OLD,NEW).splitlines():
    p = line.split("\t"); changed[p[-1]] = p[0][0]
deleted_base = {Path(p).name for p,s in changed.items() if s == "D"}

# Phase 1 에서 판정된 (note, line) — 좌표 치환 허용 근거
adjudicated = {(r["note"], str(r["note_line"]))
               for r in csv.DictReader(open(OUT/"phase1-codex.csv"))}

linemap, hunks, content = {}, {}, {}
for p, s in changed.items():
    if s == "D": continue
    o = git("show", f"{OLD}:{p}").splitlines(); n = git("show", f"{NEW}:{p}").splitlines()
    m, hs = {}, []
    for tag,i1,i2,j1,j2 in difflib.SequenceMatcher(None,o,n,autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2-i1): m[i1+k+1] = j1+k+1
        else: hs.append((i1+1, max(i2, i1+1)))
    linemap[p], hunks[p], content[p] = m, hs, (o, n)

by_base = {}
for p in linemap: by_base.setdefault(Path(p).name, []).append(p)

def fmt(rs): return ",".join(f"{a}-{b}" if a != b else str(a) for a,b in rs)

rows, excl = [], []
for md in sorted(p for p in (W/"models/SWAN").rglob("*.md") if "/raw/" not in str(p)):
    rel = str(md.relative_to(W))
    for x in rp.parse_note(md.read_text(errors="replace")):
        if x["kind"] != "file-line" or not x["ranges"]: continue
        if x.get("anomaly"): continue
        base = Path(x["path"]).name
        if base in deleted_base:
            rows.append(dict(note=rel, note_line=x["line"], ref=x["raw"], source=base,
                             old=fmt(x["ranges"]), new="", status="UNRESOLVED_SOURCE_REFERENCE",
                             basis="파일이 새 snapshot 에 없음(삭제)"))
            continue
        if base not in by_base: continue
        if x["excluded"]:
            excl.append(dict(note=rel, line=x["line"], ref=x["raw"], source=base,
                             ranges=fmt(x["ranges"]), region="code-block",
                             disposition="STALE_AFTER_BUMP",
                             reason="코드블록 내 인용 — 자동 수정 제외 영역"))
            continue
        if len(by_base[base]) > 1:
            rows.append(dict(note=rel, note_line=x["line"], ref=x["raw"], source=base,
                             old=fmt(x["ranges"]), new="", status="AMBIGUOUS", basis="동명 파일 다중"))
            continue
        p = by_base[base][0]; m = linemap[p]; o, n = content[p]
        mapped, flags = [], []
        keys = sorted(m)
        def anchor(v, d):
            c = [k for k in keys if k <= v] if d < 0 else [k for k in keys if k >= v]
            return m[c[-1] if d < 0 else c[0]] if c else None
        interior = False
        for a, b in x["ranges"]:
            ma, mb = m.get(a), m.get(b)
            if ma is None or mb is None:
                flags.append("REANCHOR"); ca, cb = ma or anchor(a,-1), mb or anchor(b,1)
                mapped.append((ca or a, cb or b)); continue
            if o[a-1:b] != n[ma-1:mb]: interior = True
            flags.append("IDENTICAL" if (ma,mb) == (a,b) else "MOVED")
            mapped.append((ma, mb))
        if "REANCHOR" in flags: st = "REANCHOR_REQUIRED"
        elif set(flags) == {"IDENTICAL"}: st = "IDENTICAL"
        else: st = "MOVED"
        basis = ""
        if interior and st in ("MOVED","IDENTICAL"):
            if (rel, str(x["line"])) in adjudicated:
                basis = "내부 변경 있으나 Phase 1 판정 완료(REVIEW_ONLY)"
            else:
                st, basis = "NEEDS_CLAUDE_REVIEW", "내부 변경 + Phase 1 판정 이력 없음"
        rows.append(dict(note=rel, note_line=x["line"], ref=x["raw"], source=p,
                         old=fmt(x["ranges"]), new=fmt(mapped), status=st, basis=basis))

with open(OUT/"line-ref-map.csv","w",newline="") as f:
    w=csv.DictWriter(f,["note","note_line","ref","source","old","new","status","basis"]); w.writeheader(); w.writerows(rows)
with open(OUT/"excluded-refs.csv","w",newline="") as f:
    w=csv.DictWriter(f,["note","line","ref","source","ranges","region","disposition","reason"]); w.writeheader(); w.writerows(excl)

print("line-ref-map:", Counter(r["status"] for r in rows), "총", len(rows))
print("excluded-refs:", len(excl))
for r in rows:
    if r["status"] in ("NEEDS_CLAUDE_REVIEW","REANCHOR_REQUIRED","UNRESOLVED_SOURCE_REFERENCE","AMBIGUOUS"):
        print(f"  {r['status']:28} {r['note'].split('/')[-1]:40}:{r['note_line']:>4} {r['ref'][:34]} {r['basis']}")
