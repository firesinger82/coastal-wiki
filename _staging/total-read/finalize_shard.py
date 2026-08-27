#!/usr/bin/env python3
"""Un-blind + merge blinded verdicts into crosswalk/v1 JSONs (MERGE-PLAN §2-3).
Reads keymap.json (neutral->role/idx), verdicts.json (subagent SAME/CONFLICT +
materiality), and the frozen records (for text/provenance). Partitions each
file's findings into a clean disposition set and emits crosswalk JSONs.
Unmatched-audit HIGH-materiality findings are emitted as distinct_unconfirmed
AND listed in delta_candidates.json for caller span-review -> confirmed_delta.
stdlib only. Usage: finalize_shard.py <blind_dir> <base_run_dir> <audit_run_dir> <out_dir>"""
import json, os, sys, hashlib

def sha_bytes(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()

def load_recs(d):
    o={}
    for f in os.listdir(d):
        if f.endswith(".json"):
            r=json.load(open(os.path.join(d,f))); o[f]=r
    return o

class UF:
    def __init__(s): s.p={}
    def find(s,x):
        s.p.setdefault(x,x)
        while s.p[x]!=x: s.p[x]=s.p[s.p[x]]; x=s.p[x]
        return x
    def union(s,a,b): s.p[s.find(a)]=s.find(b)

def main():
    blind,base_dir,aud_dir,out=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    os.makedirs(out,exist_ok=True)
    km=json.load(open(os.path.join(blind,"keymap.json")))
    vd=json.load(open(os.path.join(blind,"verdicts.json")))
    brecs=load_recs(base_dir); arecs=load_recs(aud_dir)
    mat=vd["materiality"]
    # index pairs by file token
    pairs_by=lambda ft:[p for p in vd["pairs"] if p["pair"][0].startswith(ft+"-")]
    DECIDED_BY="llm:blinded-subagent (general-purpose, vendor-blind, A/B-randomized) + caller span-confirm"
    DECIDED_AT="2026-08-27"
    delta_cands=[]
    summary={"equivalent":0,"conflict":0,"base_only":0,"distinct_unconfirmed":0,"confirmed_delta":0}
    for ft,info in sorted(km["files"].items()):
        f=info["record_file"]; brec=brecs[f]; arec=arecs[f]
        bu=brec["content"]["unresolved"]; au=arec["content"]["unresolved"]
        # map neutral id -> ("A",idx) or ("B",idx) using role
        def canon(nid):
            side="X" if "-X" in nid else "Y"
            role=info[side+"_role"]; idx=info[side][nid]
            return ("A",idx) if role=="base" else ("B",idx)
        # SAME graph
        uf=UF(); same_ids=set(); conflict_pairs=[]
        for p in pairs_by(ft):
            a,b=p["pair"]; v=p["verdict"]
            if v=="SAME":
                uf.union(a,b); same_ids.add(a); same_ids.add(b)
            elif v=="CONFLICT":
                conflict_pairs.append((a,b,p.get("reason","")))
        # equivalence components
        comps={}
        for nid in same_ids:
            comps.setdefault(uf.find(nid),[]).append(nid)
        consumed=set()
        disp=[]
        def rec_disp(d,bids,aids,note,members_txt_b,members_txt_a,span=None):
            item={"disposition":d,"base_ids":[f"A{i}" for i in bids],
                  "audit_ids":[f"B{i}" for i in aids],
                  "base_member_text":members_txt_b,"audit_member_text":members_txt_a,
                  "representative":"audit" if aids else "base","rationale":note,
                  "decided_by":DECIDED_BY,"decided_at":DECIDED_AT}
            if span: item["evidence_span"]=span
            return item
        for comp in comps.values():
            bids=[]; aids=[]
            for nid in comp:
                side,idx=canon(nid); consumed.add(nid)
                (bids if side=="A" else aids).append(idx)
            bids=sorted(set(bids)); aids=sorted(set(aids))
            disp.append(rec_disp("equivalent",bids,aids,
                "blinded SAME"+(" (many-to-one)" if len(bids)+len(aids)>2 else ""),
                [bu[i] for i in bids],[au[i] for i in aids]))
            summary["equivalent"]+=1
        conflict_notes=[]  # (surviving_nid, reason) where one endpoint already matched
        for a,b,reason in conflict_pairs:
            if a in consumed or b in consumed:
                # one endpoint already in an equivalent class; keep the free endpoint's
                # normal disposition but annotate the conflict for human review (exact-once safe)
                free = b if a in consumed else a
                conflict_notes.append((free, "CONFLICT vs a matched finding: "+reason))
                continue
            bids=[];aids=[]
            for nid in (a,b):
                side,idx=canon(nid); consumed.add(nid)
                (bids if side=="A" else aids).append(idx)
            disp.append(rec_disp("conflict",sorted(set(bids)),sorted(set(aids)),
                "blinded CONFLICT: "+reason,[bu[i] for i in sorted(set(bids))],[au[i] for i in sorted(set(aids))]))
            summary["conflict"]+=1
        cnote={nid:msg for nid,msg in conflict_notes}
        # unmatched
        for i in range(len(bu)):
            nid=f"{ft}-X{i}" if info["X_role"]=="base" else f"{ft}-Y{i}"
            if nid in consumed: continue
            note="unmatched base finding (mat="+mat.get(nid,"?")+")"
            if nid in cnote: note+=" | "+cnote[nid]
            disp.append(rec_disp("base_only",[i],[],note,[bu[i]],[]))
            summary["base_only"]+=1
        for j in range(len(au)):
            nid=f"{ft}-X{j}" if info["X_role"]=="audit" else f"{ft}-Y{j}"
            if nid in consumed: continue
            m=mat.get(nid,"?")
            note="unmatched audit finding (mat="+m+")"
            if nid in cnote: note+=" | "+cnote[nid]
            disp.append(rec_disp("distinct_unconfirmed",[],[j],note,[],[au[j]]))
            summary["distinct_unconfirmed"]+=1
            if m=="HIGH":
                delta_cands.append({"source_path":info["source_path"],"record_file":f,
                    "audit_id":f"B{j}","text":au[j]})
        cw={"schema":"crosswalk/v1","model":km["shard"].split("-")[0],"shard":km["shard"],
            "source_path":info["source_path"],"source_sha256":info["source_sha256"],
            "base_run_id":brec["run_id"],"audit_run_id":arec["run_id"],
            "base_record_file":f,"audit_record_file":f,
            "base_record_sha256_bytes":sha_bytes(os.path.join(base_dir,f)),
            "audit_record_sha256_bytes":sha_bytes(os.path.join(aud_dir,f)),
            "base_finding_count":len(bu),"audit_finding_count":len(au),
            "provenance":{"pilot":False,"blinded":True,
              "note":"Blinded single-subagent adjudication (MERGE-PLAN §2): vendor labels stripped, A/B randomized per file, candidate-pair focus. confirmed_delta promoted only after caller original-span confirmation.",
              "decided_by":DECIDED_BY,"decided_at":DECIDED_AT},
            "dispositions":disp}
        flat=info["source_path"].strip("/").replace("/","__")  # full path -> unique filename
        json.dump(cw,open(os.path.join(out,flat+".crosswalk.json"),"w"),ensure_ascii=False,indent=1)
    json.dump(delta_cands,open(os.path.join(out,"..","delta_candidates.json"),"w"),ensure_ascii=False,indent=1)
    print("summary:",json.dumps(summary))
    print("delta_candidates (HIGH unmatched-audit):",len(delta_cands))
    print("wrote crosswalk JSONs to",out)

if __name__=="__main__": main()
