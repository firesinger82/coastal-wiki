#!/usr/bin/env python3
"""verify_crosswalk.py — external check for crosswalk artifacts (MERGE-PLAN §6.1).
Guarantees: (1) zero original-finding loss, (2) every finding gets exactly one
disposition, (3) disposition-shape invariants, (4) provenance integrity
(recompute parent record hashes; source sha agreement). Read-only.
Usage: verify_crosswalk.py <crosswalk_dir> <base_record_dir> <audit_record_dir>
Exit 0 = PASS, 1 = FAIL."""
import json, os, sys, hashlib

VALID={"equivalent","confirmed_delta","distinct_unconfirmed","rejected","conflict","base_only"}

def sha_bytes(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()

def load_records(dirp):
    out={}
    for f in os.listdir(dirp):
        if f.endswith(".json"):
            r=json.load(open(os.path.join(dirp,f)))
            out[f]={"rec":r,"path":os.path.join(dirp,f),"file":f}  # key by record filename (source_sha256 can collide across duplicate-content paths)
    return out

def main():
    cwdir, basedir, auddir = sys.argv[1], sys.argv[2], sys.argv[3]
    base=load_records(basedir); aud=load_records(auddir)
    fails=[]; nfiles=0; ndisp=0; deltas=0
    for f in sorted(os.listdir(cwdir)):
        if not f.endswith(".crosswalk.json"): continue
        nfiles+=1
        cw=json.load(open(os.path.join(cwdir,f)))
        sha=cw["source_sha256"]; tag=f
        bf=cw.get("base_record_file"); af=cw.get("audit_record_file")
        if bf not in base: fails.append(f"{tag}: base record file '{bf}' not found"); continue
        if af not in aud:  fails.append(f"{tag}: audit record file '{af}' not found"); continue
        b=base[bf]; a=aud[af]
        # (4) integrity: recompute parent record hashes, do NOT trust stored field
        if sha_bytes(b["path"])!=cw["base_record_sha256_bytes"]:
            fails.append(f"{tag}: base record bytes hash mismatch (record changed since crosswalk)")
        if sha_bytes(a["path"])!=cw["audit_record_sha256_bytes"]:
            fails.append(f"{tag}: audit record bytes hash mismatch")
        if not (b["rec"]["source_sha256"]==a["rec"]["source_sha256"]==sha):
            fails.append(f"{tag}: source sha disagreement across layers")
        bu=b["rec"]["content"]["unresolved"]; au=a["rec"]["content"]["unresolved"]
        if cw["base_finding_count"]!=len(bu):  fails.append(f"{tag}: base_finding_count != len(base.unresolved)")
        if cw["audit_finding_count"]!=len(au): fails.append(f"{tag}: audit_finding_count != len(audit.unresolved)")
        exp_b={f"A{i}" for i in range(len(bu))}
        exp_a={f"B{i}" for i in range(len(au))}
        seen_b=[]; seen_a=[]
        for d in cw["dispositions"]:
            ndisp+=1
            disp=d["disposition"]
            if disp not in VALID: fails.append(f"{tag}: invalid disposition '{disp}'")
            bids=d["base_ids"]; aids=d["audit_ids"]
            seen_b+=bids; seen_a+=aids
            # shape invariants
            if disp=="confirmed_delta":
                deltas+=1
                if bids: fails.append(f"{tag}: confirmed_delta must have empty base_ids ({bids})")
                if len(aids)!=1: fails.append(f"{tag}: confirmed_delta must cite exactly one audit id ({aids})")
                sp=d.get("evidence_span")
                if not sp or not sp.get("quote"): fails.append(f"{tag}: confirmed_delta {aids} missing evidence_span.quote")
            elif disp=="base_only":
                if aids: fails.append(f"{tag}: base_only must have empty audit_ids ({aids})")
                if not bids: fails.append(f"{tag}: base_only must have >=1 base id")
            elif disp in ("distinct_unconfirmed","rejected"):
                if bids: fails.append(f"{tag}: {disp} must have empty base_ids ({bids})")
                if not aids: fails.append(f"{tag}: {disp} must have >=1 audit id")
            elif disp in ("equivalent","conflict"):
                if not bids or not aids: fails.append(f"{tag}: {disp} needs both base and audit ids ({bids}/{aids})")
        # (1)(2) exact-once coverage, no loss, no dup
        db=[x for x in seen_b if seen_b.count(x)>1]
        da=[x for x in seen_a if seen_a.count(x)>1]
        if db: fails.append(f"{tag}: base ids assigned more than once: {sorted(set(db))}")
        if da: fails.append(f"{tag}: audit ids assigned more than once: {sorted(set(da))}")
        miss_b=exp_b-set(seen_b); miss_a=exp_a-set(seen_a)
        if miss_b: fails.append(f"{tag}: LOST base findings (no disposition): {sorted(miss_b)}")
        if miss_a: fails.append(f"{tag}: LOST audit findings (no disposition): {sorted(miss_a)}")
        extra_b=set(seen_b)-exp_b; extra_a=set(seen_a)-exp_a
        if extra_b: fails.append(f"{tag}: base ids out of range: {sorted(extra_b)}")
        if extra_a: fails.append(f"{tag}: audit ids out of range: {sorted(extra_a)}")
    print(f"files={nfiles} dispositions={ndisp} confirmed_delta={deltas}")
    if nfiles==0: fails.append("no *.crosswalk.json found in crosswalk dir")
    if fails:
        print("RESULT: FAIL"); [print("  -",x) for x in fails]; sys.exit(1)
    print("RESULT: PASS — zero finding loss, all dispositions valid, provenance intact")
    sys.exit(0)

if __name__=="__main__":
    main()
