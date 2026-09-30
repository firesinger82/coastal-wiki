#!/usr/bin/env python3
"""B1 결정적 대조: 레코드의 bindings[].applicability.build 를 build-map.json 에서 계산한 파일 포함 상태와 비교."""
import json, collections, sys
from pathlib import Path
C = Path(__file__).resolve().parents[2]
b = json.load(open(C / "build-mode-20260912/build-map.json"))
def norm(p): return p.replace("\\", "/").lower()
exp = collections.defaultdict(dict)   # caller file -> family -> set(states)
auto = {norm(x) for k in ("library_sources", "executable_sources") for x in b["autotools"][k]}
for pr in b["projects"]:
    ncfg = len(pr["configs"])
    listed = {}
    for f in pr["files"]:
        rp = norm(f.get("resolved_path") or "")
        exc = sum(1 for o in f.get("overrides", []) if o.get("ExcludedFromBuild") == "true")
        listed[rp] = "excluded" if exc >= ncfg else ("included" if exc == 0 else "mixed")
    exp[pr["path"]] = listed
R = [json.loads(l) for l in open(sys.argv[1])]
bad = collections.Counter(); ex = []
for r in R:
    caller = norm(r["id"].split(":")[0])
    base = caller.split("/")[-1]
    for bd in r.get("bindings", []):
        got = {x.get("family"): x.get("state") for x in bd["applicability"].get("build", [])}
        # autotools
        a = "included" if base in auto else "excluded"
        if got.get("autotools") not in (a, "unknown"):
            bad["autotools"] += 1; ex.append((r["id"], "autotools", got.get("autotools"), a))
        for proj, listed in exp.items():
            want = listed.get(caller, "excluded")
            g = got.get(proj)
            if g is None: bad["missing:" + proj] += 1; ex.append((r["id"], proj, None, want)); continue
            if want == "mixed": continue
            if g not in (want, "unknown"): bad["mismatch:" + proj] += 1; ex.append((r["id"], proj, g, want))
print(len(R), dict(bad))
for e in ex[:15]: print(e)
