#!/usr/bin/env python3
"""Promote span-confirmed delta candidates in the crosswalk JSONs.
CONFIRM (+ independently re-verified verbatim quote) -> confirmed_delta with evidence_span
REFUTE   -> rejected ; UNCERTAIN -> left as distinct_unconfirmed
The quote is checked against the real source BEFORE promotion (never trust the reporter).
Usage: promote_deltas.py <shard> [--apply]"""
import json,os,re,sys,glob,hashlib
W="/home/firesinger/coastal-wiki"; SRC=f"{W}/models/XBeach/raw/source_code"
CW=f"{W}/_staging/total-read/model-audit/XBeach/cw/crosswalk"
SH=sys.argv[1]; APPLY="--apply" in sys.argv

def norm(s): return re.sub(r'\s+',' ',s).strip()

def quote_ok(path,span):
    """quote must appear verbatim (whitespace-normalised) in the file, and within the cited lines if given"""
    if not span or not span.get("quote"): return False,"no quote"
    body=open(f"{SRC}/{path}",errors="replace").read().splitlines()
    q=[norm(x) for x in span["quote"].splitlines() if norm(x)]
    if not q: return False,"empty quote"
    hay=[norm(x) for x in body]
    # find contiguous run of quote lines anywhere
    for i in range(len(hay)-len(q)+1):
        if hay[i:i+len(q)]==q:
            found=(i+1,i+len(q))
            nums=[int(x) for x in re.findall(r'(\d{1,6})',span.get("lines",""))]
            if nums and not (min(nums)-8 <= found[0] <= max(nums)+8):
                return False,f"quote found at L{found[0]}-L{found[1]} outside cited {span.get('lines')}"
            return True,f"L{found[0]}-L{found[1]}"
    return False,"quote not found verbatim in source"

vd=json.load(open(f"{CW}/{SH}.span-verdicts.json"))["verdicts"]
cand=json.load(open(f"{CW}/{SH}.delta_candidates.json"))
key=lambda p,a:(p,a)
vmap={key(v["source_path"],v["audit_id"]):v for v in vd}
missing=[c for c in cand if key(c["source_path"],c["audit_id"]) not in vmap]
stats={"CONFIRM":0,"REFUTE":0,"UNCERTAIN":0,"QUOTE_FAIL":0,"promoted":0,"rejected":0}
detail=[]
edits={}   # crosswalk file -> list of (audit_id, new_disposition, evidence_span, rationale)
for c in cand:
    v=vmap.get(key(c["source_path"],c["audit_id"]))
    if not v: continue
    verd=v["verdict"]; stats[verd]=stats.get(verd,0)+1
    flat=c["source_path"].strip("/").replace("/","__")+".crosswalk.json"
    if verd=="CONFIRM":
        ok,why=quote_ok(c["source_path"],v.get("evidence_span"))
        if not ok:
            stats["QUOTE_FAIL"]+=1; stats["CONFIRM"]-=1
            detail.append(("QUOTE_FAIL",c["source_path"],c["audit_id"],why))
            continue
        sp=dict(v["evidence_span"]); sp["verified_at_lines"]=why
        sp["source_sha256"]=hashlib.sha256(open(f"{SRC}/{c['source_path']}","rb").read()).hexdigest()
        edits.setdefault(flat,[]).append((c["audit_id"],"confirmed_delta",sp,v.get("rationale","")))
        stats["promoted"]+=1
        detail.append(("CONFIRM",c["source_path"],c["audit_id"],why))
    elif verd=="REFUTE":
        edits.setdefault(flat,[]).append((c["audit_id"],"rejected",None,v.get("rationale","")))
        stats["rejected"]+=1
print(f"{SH}: candidates={len(cand)} verdicts={len(vd)} missing={len(missing)} {stats}")
for d in detail:
    if d[0]!="CONFIRM": print("  !",d[0],d[1].split('/')[-1],d[2],"|",d[3])
if not APPLY:
    print("(dry-run; pass --apply to write)"); sys.exit(0)
n=0
for flat,items in edits.items():
    p=f"{CW}/{SH}/{flat}"
    cw=json.load(open(p)); hit=0
    for aid,newd,sp,rat in items:
        for d in cw["dispositions"]:
            if d["disposition"]=="distinct_unconfirmed" and d["audit_ids"]==[aid]:
                d["disposition"]=newd
                d["rationale"]=(("span-confirmed: " if newd=="confirmed_delta" else "span-refuted: ")+rat)[:600]
                d["decided_by"]="llm:codex span-confirmation + caller verbatim-quote re-verification"
                d["decided_at"]="2026-09-06"
                if sp: d["evidence_span"]=sp
                hit+=1
    json.dump(cw,open(p,"w"),ensure_ascii=False,indent=1); n+=hit
print(f"applied {n} disposition changes across {len(edits)} crosswalk files")
