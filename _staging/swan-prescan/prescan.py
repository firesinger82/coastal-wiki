#!/usr/bin/env python3
"""SWAN 3차 파일럿 사전 스캔 — DESIGN v2.0 §PILOT ROLLOUT ORDER 5지표.

⑴ 변경 파일 ⑵ 인용 교집합 ⑶ 줄 이동 수 ⑷ 의미 변경 후보 ⑸ broad·unresolved 수
"""
import csv, difflib, json, subprocess, sys
from pathlib import Path
from collections import Counter

W = Path.home()/"coastal-wiki"
OUT = W/"_staging/swan-prescan"
INS = W/"models/SWAN/raw/source_code/swan"
STG = Path.home()/".cache/coastal-snapshots/swan-43e9bbb"
OLD, NEW = "55441526ec4330338f05d148759fc66f6fc7fb9d", "43e9bbba393f2cf9eaff78bc92eaed118a3a5c8e"
sys.path.insert(0, str(W/"_staging/model-migration-framework")); import refparser as rp

def git(*a, cwd=STG):
    return subprocess.run(["git","-c","safe.directory=*","-C",str(cwd),*a],
                          capture_output=True, text=True).stdout

# ---------- 변경 집합 ----------
changed = {}
for line in git("diff","--name-status",OLD,NEW).splitlines():
    p = line.split("\t")
    changed[p[-1]] = p[0][0]
deleted = {p for p,s in changed.items() if s=="D"}
with open(OUT/"changed-files.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["status","path"])
    for p,s in sorted(changed.items()): w.writerow([s,p])

# ---------- 참조 스캔 (coverage ledger) ----------
src_index = {}
for p in INS.rglob("*"):
    if p.is_file(): src_index.setdefault(p.name, []).append(str(p.relative_to(INS)))
changed_base = {}
for p in changed: changed_base.setdefault(Path(p).name, []).append(p)

notes = [p for p in (W/"models/SWAN").rglob("*.md") if "/raw/" not in str(p)]
led = Counter(); refs_rows = []
for md in sorted(notes):
    rel = str(md.relative_to(W))
    for x in rp.parse_note(md.read_text(errors="replace")):
        k = x["kind"]
        led["total"] += 1
        if x["excluded"]: led["excluded"] += 1
        if k == "symbol": led["symbol_only"] += 1; continue
        if k == "bare":   led["bare"] += 1; continue
        base = Path(x["path"]).name
        if x.get("anomaly") == "NUMERIC_STEM":
            led["abbreviation"] += 1; state = "AMBIGUOUS_ABBREVIATION"
            refs_rows.append(dict(note=rel, line=x["line"], ref=x["raw"], base=base, ranges="",
                                  span=0, state=state, excluded=x["excluded"], changed=False, deleted=False))
            continue
        cands = src_index.get(base, [])
        if not cands: led["unresolved_file"] += 1; state = "UNRESOLVED_SOURCE_REFERENCE"
        elif len(cands) > 1: led["ambiguous"] += 1; state = "AMBIGUOUS"
        else: led["resolved"] += 1; state = "RESOLVED"
        if x["ranges"]:
            led["file_line"] += 1
            span = sum(b-a+1 for a,b in x["ranges"])
            if span > 60: led["broad"] += 1
        else:
            led["file_only"] += 1; span = 0
        refs_rows.append(dict(note=rel, line=x["line"], ref=x["raw"], base=base,
                              ranges=";".join(f"{a}-{b}" for a,b in (x["ranges"] or [])),
                              span=span, state=state, excluded=x["excluded"],
                              changed=base in changed_base, deleted=base in {Path(d).name for d in deleted}))
with open(OUT/"REFERENCES.csv","w",newline="") as f:
    w=csv.DictWriter(f, list(refs_rows[0])); w.writeheader(); w.writerows(refs_rows)

# ---------- 교집합 + 줄 이동 + 의미 후보 ----------
linemap, hunks, content = {}, {}, {}
for p,s in changed.items():
    if s == "D": continue
    o = git("show",f"{OLD}:{p}").splitlines(); n = git("show",f"{NEW}:{p}").splitlines()
    m = {}; hs = []
    for tag,i1,i2,j1,j2 in difflib.SequenceMatcher(None,o,n,autojunk=False).get_opcodes():
        if tag=="equal":
            for k in range(i2-i1): m[i1+k+1] = j1+k+1
        else: hs.append((i1+1, max(i2, i1+1)))
    linemap[p]=m; hunks[p]=hs; content[p]=(o,n)

inter, moved, semantic, unres = [], 0, [], []
for r in refs_rows:
    if not r["changed"]: continue
    if r["deleted"]:
        unres.append(r); continue
    paths = changed_base[r["base"]]
    if len(paths) != 1: continue
    p = paths[0]
    inter.append(r)
    if not r["ranges"]: continue
    rngs = [tuple(int(v) for v in s.split("-")) for s in r["ranges"].split(";")]
    o,n = content[p]; m = linemap[p]
    hit = any(not (b < h0 or a > h1) for (a,b) in rngs for (h0,h1) in hunks[p])
    if hit: semantic.append({**r, "source": p})
    else:
        if any(m.get(a) != a or m.get(b) != b for a,b in rngs): moved += 1

json.dump({"old":OLD,"new":NEW,"changed":len(changed),"deleted":sorted(deleted)},
          open(OUT/"snapshot.json","w"), indent=1)
with open(OUT/"semantic-candidates.csv","w",newline="") as f:
    if semantic:
        w=csv.DictWriter(f, list(semantic[0])); w.writeheader(); w.writerows(semantic)

print("=== SWAN 사전 스캔 ===")
print(f"⑴ 변경 파일       : {len(changed)} (수정 {sum(1 for v in changed.values() if v=='M')} / 삭제 {len(deleted)})")
print(f"⑵ 인용 교집합     : {len(inter)}건 / 노트 {len({r['note'] for r in inter})}개")
print(f"⑶ 줄 이동(의미무관): {moved}")
print(f"⑷ 의미 변경 후보  : {len(semantic)}건 / 노트 {len({r['note'] for r in semantic})}개")
print(f"⑸ broad {led['broad']} / unresolved_file {led['unresolved_file']} / ambiguous {led['ambiguous']} / 삭제파일 참조 {len(unres)}")
print()
print("--- coverage ledger ---")
for k in ("total","file_line","file_only","bare","symbol_only","resolved","ambiguous","abbreviation","unresolved_file","broad","excluded"):
    print(f"  {k:18} {led[k]}")
