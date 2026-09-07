#!/usr/bin/env python3
"""Supplement manifest builder v2 (MERGE-PLAN §3-4, hardened per Codex review).
Promotes crosswalk confirmed_delta into a keyed supplement manifest, binding each
supplement to (a) its crosswalk (path+hash), (b) the audit record (hash + parsed
source_sha256 + audit_id/finding_text membership), (c) every cited evidence source
(exact path + hash). Re-derives all evidence from live source. stdlib only.

Usage: build_supplement_manifest.py <crosswalk_root> <records_root> <models_root> <out.json>
"""
import json, os, re, sys, hashlib, glob

def sha_bytes(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
def sha_text(t):  return hashlib.sha256(t.encode()).hexdigest()
def parse_lines(spec):
    out=[]
    for part in str(spec).split(","):
        part=part.strip()
        if "-" in part: a,b=part.split("-"); out.append((int(a),int(b)))
        elif part: out.append((int(part),int(part)))
    return out
def extract(path,ranges,nlines):
    lines=open(path,encoding="utf-8",errors="replace").read().splitlines()
    segs=[]
    for a,b in ranges:
        assert 1<=a<=b<=nlines, f"range {a}-{b} out of bounds (1..{nlines})"
        segs.append("\n".join(lines[a-1:b]))
    q="\n…\n".join(segs)
    assert q.strip(), "empty quote"
    return q
def linecount(path): return len(open(path,encoding="utf-8",errors="replace").read().splitlines())
AUDIT_ID=re.compile(r"B(0|[1-9]\d*)$")
def resolve_contained(models_root, src_path):
    real=os.path.realpath(models_root); p=os.path.realpath(os.path.join(models_root, src_path))
    return p if p.startswith(real+os.sep) and os.path.exists(p) else None

def main():
    cwroot,recroot,models,out=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    entries=[]; problems=[]; seen=set()
    for cw in sorted(glob.glob(os.path.join(cwroot,"*","*.crosswalk.json"))):
        j=json.load(open(cw)); shard=os.path.basename(os.path.dirname(cw))
        # validate ALL crosswalk audit_ids: grammar + no contradiction with confirmed_delta
        aid_kinds={}
        for dd in j["dispositions"]:
            for aid in dd.get("audit_ids",[]):
                if not AUDIT_ID.fullmatch(aid): problems.append(f"{shard}: malformed crosswalk audit_id {aid}")
                aid_kinds.setdefault(aid,set()).add(dd["disposition"])
        for aid,kinds in aid_kinds.items():
            if "confirmed_delta" in kinds and kinds-{"confirmed_delta"}:
                problems.append(f"{shard}: {aid} contradictory dispositions {kinds}")
        deltas=[d for d in j["dispositions"] if d["disposition"]=="confirmed_delta"]
        if not deltas: continue
        def find_rec(run_id, rec_file):
            p=os.path.join(recroot, run_id, rec_file)
            return p if os.path.exists(p) else None
        base_p=find_rec(j["base_run_id"], j["base_record_file"])
        aud_p =find_rec(j["audit_run_id"], j["audit_record_file"])
        if not base_p or not aud_p: problems.append(f"{shard} {j['source_path']}: record not found"); continue
        brec=json.load(open(base_p)); arec=json.load(open(aud_p))
        cw_h=sha_bytes(cw); base_h=sha_bytes(base_p); aud_h=sha_bytes(aud_p)
        # §4 integrity vs crosswalk-stored
        if base_h!=j["base_record_sha256_bytes"]: problems.append(f"{shard}: base record hash drift")
        if aud_h !=j["audit_record_sha256_bytes"]: problems.append(f"{shard}: audit record hash drift")
        ckey_sha=j["source_sha256"]
        au=arec["content"]["unresolved"]
        supplements=[]
        for d in deltas:
            sp=d["evidence_span"]; ranges=parse_lines(sp["lines"])
            # audit_id membership + per-member finding_text (grammar-checked)
            member_texts={}
            for aid in d["audit_ids"]:
                if not re.fullmatch(r"B(0|[1-9]\d*)", aid): problems.append(f"{shard}: bad audit_id grammar {aid}"); continue
                idx=int(aid[1:])
                if not (0<=idx<len(au)): problems.append(f"{shard}: {aid} out of audit range"); continue
                member_texts[aid]=au[idx]
            # dedup
            for aid in d["audit_ids"]:
                key=(ckey_sha,aid)
                if key in seen: problems.append(f"{shard}: duplicate promotion {aid}")
                seen.add(key)
            # evidence sources = the span path (+ could be many); build exact hash
            srcf=resolve_contained(models, sp["path"])
            if not srcf: problems.append(f"{shard}: evidence source not found {sp['path']}"); continue
            nlines=linecount(srcf)
            try: authoritative=extract(srcf, ranges, nlines)
            except AssertionError as e: problems.append(f"{shard}: {sp['path']} {e}"); continue
            ev_sha=sha_bytes(srcf)
            supplements.append({
                "member_input_ids": d["audit_ids"],
                "finding_texts": member_texts,   # {audit_id: exact unresolved text}
                "audit_record": {"run_id": j["audit_run_id"],
                    "record_path": aud_p.split("_staging/")[-1],
                    "record_sha256_bytes": aud_h,
                    "record_source_sha256": arec.get("source_sha256")},
                "evidence_sources": [{"path": sp["path"], "sha256": ev_sha}],
                "source_span": {"path": sp["path"], "lines": sp["lines"]},
                "authoritative_quote": authoritative,
                "source_span_hash": sha_text(authoritative),
                "decision": "confirmed_delta",
                "decided_by": d.get("decided_by"), "decided_at": d.get("decided_at"),
                "rationale": d.get("rationale"), "reconfirmed_at": "2026-09-07",
                "reconfirm_method": "span re-extracted (bounds-checked) from exact live source; audit_id/finding_text membership + crosswalk + record hashes verified by verify_supplement.py",
            })
        entries.append({
            "canonical_key": {"model": j["model"], "normalized_path": j["source_path"], "source_sha256": ckey_sha},
            "shard": shard,
            "selected_record": {"layer":"base_1차","reader": brec.get("reader"),
                "run_id": j["base_run_id"], "record_file": j["base_record_file"],
                "record_path": base_p.split("_staging/")[-1],
                "record_sha256_bytes": base_h, "record_source_sha256": brec.get("source_sha256")},
            "crosswalk": {"path": cw.split("_staging/")[-1], "sha256_bytes": cw_h},
            "supplements": supplements,
        })
    manifest={"schema":"supplement-manifest/v2","corpus":"model-audit-20260831",
              "design_ref":"MERGE-PLAN-20260827.md §3-4; hardened per Codex adversarial review 2026-08-27",
              "generated_by":"llm:claude-opus-5 (supplement gate; span-reconfirm only — NOT completion authority)",
              "generated_at":"2026-09-07",
              "note":"selected_record=base(Claude 1차, unchanged). supplements=span-reconfirmed audit confirmed_delta, bound to crosswalk+audit-record+evidence-source hashes. Canonical validity requires verify_supplement.py PASS AND an approved human decision receipt (supplement-decisions.json). Supplements are neither necessary nor sufficient for the completion gate.",
              "entry_count":len(entries),
              "supplement_count":sum(len(e["supplements"]) for e in entries),
              "entries":entries}
    if problems:
        print(f"BUILD FAILED — {len(problems)} problem(s); manifest NOT written:")
        for p in problems: print("  -",p)
        sys.exit(1)
    json.dump(manifest,open(out,"w"),ensure_ascii=False,indent=1)
    print(f"entries={len(entries)} supplements={manifest['supplement_count']} — written")

if __name__=="__main__": main()
