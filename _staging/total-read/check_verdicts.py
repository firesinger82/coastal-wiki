#!/usr/bin/env python3
"""Gate a CW verdicts.json against its blinded_input.json before finalize.
Usage: check_verdicts.py <shard>"""
import json,sys,os,re
SH=sys.argv[1]
B=f"/home/firesinger/coastal-wiki/_staging/total-read/model-audit/XBeach/cw/blind/{SH}"
bi=json.load(open(f"{B}/blinded_input.json"))
if not os.path.exists(f"{B}/verdicts.json"): print("MISSING verdicts.json"); sys.exit(1)
vd=json.load(open(f"{B}/verdicts.json"))
want_pairs=set(); want_ids=set()
for f in bi["files"]:
    for p in f["candidate_pairs"]: want_pairs.add(tuple(p))
    for it in f["listX"]+f["listY"]: want_ids.add(it["id"])
got=[tuple(p["pair"]) for p in vd.get("pairs",[])]
gots=set(got); dup=[p for p in gots if got.count(p)>1]
mat=vd.get("materiality",{})
V={"SAME","CONFLICT","DIFFERENT"}
badv=[p for p in vd.get("pairs",[]) if p.get("verdict") not in V]
badm=[k for k,v in mat.items() if v not in {"HIGH","MED","LOW"}]
miss_p=want_pairs-gots; extra_p=gots-want_pairs
miss_m=want_ids-set(mat); extra_m=set(mat)-want_ids
c={}
for p in vd.get("pairs",[]): c[p.get("verdict")]=c.get(p.get("verdict"),0)+1
mc={}
for v in mat.values(): mc[v]=mc.get(v,0)+1
print(f"{SH}: pairs {len(gots)}/{len(want_pairs)} {c} | materiality {len(mat)}/{len(want_ids)} {mc}")
fails=[]
if miss_p: fails.append(f"missing pairs {len(miss_p)}: {sorted(miss_p)[:5]}")
if extra_p: fails.append(f"unknown pairs {len(extra_p)}: {sorted(extra_p)[:5]}")
if dup: fails.append(f"duplicate pairs {len(dup)}")
if badv: fails.append(f"invalid verdicts {len(badv)}")
if miss_m: fails.append(f"missing materiality {len(miss_m)}: {sorted(miss_m)[:5]}")
if extra_m: fails.append(f"unknown materiality keys {len(extra_m)}: {sorted(extra_m)[:5]}")
if badm: fails.append(f"invalid materiality values {len(badm)}")
print("RESULT: PASS" if not fails else "RESULT: FAIL")
[print("  -",x) for x in fails]
sys.exit(1 if fails else 0)
