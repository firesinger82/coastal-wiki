#!/usr/bin/env python3
"""WO-20260728 §6.2 맹검 감사 층화표본 selector (결정론적, 읽기 전용)."""
import sys, os, json, glob, hashlib, math, argparse
from collections import defaultdict, Counter

TR = os.path.dirname(os.path.abspath(__file__))
SEED = "6465d0b8bd3f7acb9a2a437da66cfb37e1a0f0a8033b44214f49f1907e393ae6"

def size_band(b):
    if b <= 4096: return "small"
    if b <= 65536: return "medium"
    return "large"

def rankkey(model, axis, npath, ssha):
    return hashlib.sha256(f"{SEED}\0{model}\0{axis}\0{npath}\0{ssha}".encode()).hexdigest()

def load(axes):
    pop=[]
    for f in sorted(glob.glob(f"{TR}/pending/reread-20260728/*/*.json")):
        r=json.load(open(f))
        if r.get("axis") not in axes: continue
        run=os.path.basename(os.path.dirname(f))
        shard="-".join(run.split("-")[1:4])
        unres = "nonempty" if (r.get("content",{}).get("unresolved") or []) else "empty"
        pop.append({"record_file": os.path.relpath(f, TR),"model": r["model"],"axis": r["axis"],
            "path": r["path"],"source_sha256": r["source_sha256"],"bytes": r["bytes"],
            "size_band": size_band(r["bytes"]),"unresolved_band": unres,"shard": shard,
            "stratum": (r["model"], r["axis"], size_band(r["bytes"]), unres),
            "rank": rankkey(r["model"], r["axis"], r["path"], r["source_sha256"])})
    return pop

def select(pop, N):
    by_str=defaultdict(list); by_shd=defaultdict(list)
    for x in pop:
        by_str[x["stratum"]].append(x); by_shd[x["shard"]].append(x)
    for k in by_str: by_str[k].sort(key=lambda z:z["rank"])
    for k in by_shd: by_shd[k].sort(key=lambda z:z["rank"])
    chosen={}
    for k,v in by_str.items():
        if k[3]=="nonempty": chosen[v[0]["record_file"]]=v[0]
    for k,v in by_shd.items(): chosen[v[0]["record_file"]]=v[0]
    if len(chosen) > N: return list(chosen.values()), True
    budget = N - len(chosen)
    unsel=defaultdict(list)
    for x in pop:
        if x["record_file"] not in chosen: unsel[x["stratum"]].append(x)
    for k in unsel: unsel[k].sort(key=lambda z:z["rank"])
    total_un=sum(len(v) for v in unsel.values())
    if budget>0 and total_un>0:
        quota={}; rema={}
        for k,v in unsel.items():
            q=len(v)/total_un*budget; quota[k]=int(q); rema[k]=q-int(q)
        left=budget-sum(quota.values())
        order=sorted(unsel.keys(), key=lambda k:(-rema[k], str(k).encode()))
        for k in order[:left]: quota[k]+=1
        for k,v in unsel.items():
            for x in v[:quota[k]]: chosen[x["record_file"]]=x
    return list(chosen.values()), False

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--axes", default="code,note")
    ap.add_argument("--frac", type=float, default=0.10)
    ap.add_argument("--out", default=None)
    a=ap.parse_args()
    axes=set(a.axes.split(","))
    pop=load(axes)
    N=math.ceil(len(pop)*a.frac)
    sel,capped=select(pop,N)
    sel.sort(key=lambda z:z["rank"])
    print(f"모집단 {len(pop)} · 목표 N=ceil({len(pop)}×{a.frac})={N} · 선택 {len(sel)}"+(" (강제분이 N초과)" if capped else ""))
    shd=Counter(x["shard"] for x in sel)
    print("shard 커버:")
    for k in sorted(shd): print(f"  {k:20s} {shd[k]}")
    strc=Counter(x["stratum"] for x in sel)
    print(f"전체 층 {len(set(x['stratum'] for x in pop))} 중 표본 {len(strc)}층")
    if a.out:
        man={"seed":SEED,"seed_string":"WO-20260728-reread|blind-audit|v1","axes":sorted(axes),
             "frac":a.frac,"population":len(pop),"N":N,"generated_over":"pending/reread-20260728",
             "selected":[{kk:x[kk] for kk in ("record_file","model","axis","path","source_sha256","bytes","size_band","unresolved_band","shard","rank")} for x in sel]}
        blob=json.dumps(man,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
        open(a.out,"w").write(json.dumps(man,ensure_ascii=False,indent=1))
        print(f"\nmanifest → {a.out}\nmanifest sha256: {hashlib.sha256(blob).hexdigest()}")

main()
