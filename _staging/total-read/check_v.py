#!/usr/bin/env python3
"""Gate V verdicts: coverage vs input + independent verbatim re-check of every neutralizer quote."""
import json,re,os,sys,collections
SH=sys.argv[1]
SRC="/home/firesinger/coastal-wiki/models/XBeach/raw/source_code"
V=f"/home/firesinger/coastal-wiki/_staging/total-read/model-audit/XBeach/cw/v"
inp={x["vid"]:x for x in json.load(open(f"{V}/{SH}.v-input.json"))}
if not os.path.exists(f"{V}/{SH}.v-verdicts.json"): print(f"{SH}: MISSING v-verdicts.json"); sys.exit(1)
vd=json.load(open(f"{V}/{SH}.v-verdicts.json"))["verdicts"]
def norm(s): return re.sub(r'\s+',' ',s).strip()
c=collections.Counter(); qok=qbad=0; bad=[]
seen=set()
for v in vd:
    c[v.get("verdict")]+=1; seen.add(v.get("vid"))
    if v.get("verdict") not in ("REFUTED","STANDS","NARROWED"): bad.append(f"invalid verdict {v.get('vid')}")
    nz=v.get("neutralizer")
    if v.get("verdict")=="REFUTED":
        if not nz or not nz.get("quote"): qbad+=1; bad.append(f"{v['vid']}: REFUTED without neutralizer quote"); continue
        path=nz["where"].split(":")[0].replace("models/XBeach/raw/source_code/","").lstrip("/")
        p=os.path.join(SRC,path)
        if not os.path.exists(p): qbad+=1; bad.append(f"{v['vid']}: neutralizer path not found {path}"); continue
        body=[norm(x) for x in open(p,errors="replace").read().splitlines()]
        q=[norm(x) for x in nz["quote"].splitlines() if norm(x)]
        if q and any(body[i:i+len(q)]==q for i in range(len(body)-len(q)+1)): qok+=1
        else: qbad+=1; bad.append(f"{v['vid']}: neutralizer quote not verbatim in {path}")
miss=set(inp)-seen; extra=seen-set(inp)
print(f"{SH}: verdicts {len(vd)}/{len(inp)} {dict(c)} | neutralizer quotes ok={qok} fail={qbad}")
if miss: bad.append(f"missing verdicts {len(miss)}: {sorted(miss)[:4]}")
if extra: bad.append(f"unknown vids {len(extra)}: {sorted(extra)[:4]}")
print("RESULT: PASS" if not bad else "RESULT: FAIL")
[print("  -",x) for x in bad[:12]]
sys.exit(1 if bad else 0)
