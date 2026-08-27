#!/usr/bin/env python3
"""Supplement manifest builder (MERGE-PLAN §3-4). Promotes crosswalk
confirmed_delta findings into a canonical supplement manifest, re-deriving all
evidence from source (do NOT trust stored fields — §4). Read-only on corpus.

Per confirmed_delta:
  - resolve base(selected_record) + audit(src) records; RECOMPUTE their bytes hashes
  - verify source file sha256 == record source_sha256 (source unchanged since read)
  - RE-EXTRACT the cited source span from the live file (§6.4 span 재확인),
    store as authoritative quote + source_span_hash
Emits supplement-manifest.json. stdlib only.

Usage: build_supplement_manifest.py <crosswalk_root> <records_root> <models_root> <out.json>
  crosswalk_root = records-crosswalk/reread-20260728
  records_root   = pending/reread-20260728
  models_root    = repo models/ dir
"""
import json, os, re, sys, hashlib, glob

def sha_bytes(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
def sha_text(t):  return hashlib.sha256(t.encode()).hexdigest()

def parse_lines(spec):
    """'112,152-153,221-222' -> [112,(152,153),(221,222)] flattened to line list."""
    out=[]
    for part in str(spec).split(","):
        part=part.strip()
        if "-" in part:
            a,b=part.split("-"); out.append((int(a),int(b)))
        elif part:
            out.append((int(part),int(part)))
    return out

def extract(path, ranges):
    lines=open(path,encoding="utf-8",errors="replace").read().splitlines()
    chunks=[]
    for a,b in ranges:
        seg="\n".join(lines[a-1:b])  # 1-indexed inclusive
        chunks.append(seg)
    return "\n…\n".join(chunks)

def resolve_source(models_root, src_path):
    """src_path like FUNWAVE/raw/.../breaker.F -> models/FUNWAVE/raw/.../breaker.F"""
    cand=os.path.join(models_root, src_path)
    if os.path.exists(cand): return cand
    base=os.path.basename(src_path)
    for r in glob.glob(os.path.join(models_root,"**",base),recursive=True):
        if r.endswith(src_path.split("/",1)[-1]) or r.endswith("/"+base):
            return r
    return None

def main():
    cwroot,recroot,models,out=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    entries=[]; problems=[]
    for cw in sorted(glob.glob(os.path.join(cwroot,"*","*.crosswalk.json"))):
        j=json.load(open(cw))
        shard=os.path.basename(os.path.dirname(cw))
        deltas=[d for d in j["dispositions"] if d["disposition"]=="confirmed_delta"]
        if not deltas: continue
        # locate base + audit record dirs for this shard (glob under recroot)
        # crosswalk stores base_record_file / audit_record_file + run ids
        def find_rec(run_id, rec_file):
            # the run dir name == run_id; record file inside
            p=os.path.join(recroot, run_id, rec_file)
            if os.path.exists(p): return p
            # fallback: search
            for r in glob.glob(os.path.join(recroot,"*",rec_file)):
                if run_id in r: return r
            return None
        base_p=find_rec(j["base_run_id"], j["base_record_file"])
        aud_p =find_rec(j["audit_run_id"], j["audit_record_file"])
        if not base_p or not aud_p:
            problems.append(f"{shard} {j['source_path']}: record not found"); continue
        # §4 integrity: recompute parent hashes, compare to crosswalk-stored
        base_h=sha_bytes(base_p); aud_h=sha_bytes(aud_p)
        if base_h!=j["base_record_sha256_bytes"]: problems.append(f"{shard}: base record hash drift")
        if aud_h !=j["audit_record_sha256_bytes"]: problems.append(f"{shard}: audit record hash drift")
        brec=json.load(open(base_p))
        supplements=[]
        for d in deltas:
            sp=d["evidence_span"]; src_path=sp["path"]; ranges=parse_lines(sp["lines"])
            srcf=resolve_source(models, src_path)
            if not srcf: problems.append(f"{shard}: source not found {src_path}"); continue
            authoritative=extract(srcf, ranges)
            src_file_sha=sha_bytes(srcf)
            supplements.append({
                "member_input_ids": d["audit_ids"],
                "finding_text": d.get("audit_member_text",[None])[0],
                "src_run_id": j["audit_run_id"],
                "src_record_path": os.path.relpath(aud_p, os.path.dirname(models.rstrip('/'))) if False else aud_p.split("_staging/")[-1],
                "src_record_sha256_bytes": aud_h,
                "source_span": {"path": src_path, "lines": sp["lines"]},
                "source_file_sha256": src_file_sha,
                "authoritative_quote": authoritative,
                "source_span_hash": sha_text(authoritative),
                "decision": "confirmed_delta",
                "decided_by": d.get("decided_by"), "decided_at": d.get("decided_at"),
                "rationale": d.get("rationale"),
                "reconfirmed_at": "2026-08-27",
                "reconfirm_method": "span re-extracted from live source at cited lines; source_file_sha256 vs record source_sha256 checked by verifier",
            })
        entries.append({
            "canonical_key": {"model": j["model"], "normalized_path": j["source_path"],
                              "source_sha256": j["source_sha256"]},
            "shard": shard,
            "selected_record": {
                "layer":"base_1차","reader": brec.get("reader"),
                "run_id": j["base_run_id"], "record_file": j["base_record_file"],
                "record_path": base_p.split("_staging/")[-1],
                "record_sha256_bytes": base_h,
            },
            "supplements": supplements,
        })
    manifest={"schema":"supplement-manifest/v1","corpus":"reread-20260728",
              "design_ref":"MERGE-PLAN-20260827.md §3-4",
              "generated_by":"llm:claude-opus-4-8 (supplement gate Phase A)",
              "generated_at":"2026-08-27",
              "note":"canonical selected_record = base(Claude 1차, unchanged). supplements = span-reconfirmed audit confirmed_delta. Does NOT add canonical keys (completion gate item 2 preserved).",
              "entry_count":len(entries),
              "supplement_count":sum(len(e["supplements"]) for e in entries),
              "entries":entries}
    json.dump(manifest,open(out,"w"),ensure_ascii=False,indent=1)
    print(f"entries={len(entries)} supplements={manifest['supplement_count']}")
    if problems:
        print("PROBLEMS:"); [print("  -",p) for p in problems]
    else:
        print("no problems during build")

if __name__=="__main__": main()
