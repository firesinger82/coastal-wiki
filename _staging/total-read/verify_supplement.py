#!/usr/bin/env python3
"""verify_supplement.py — external gate for the supplement manifest (MERGE-PLAN §3-4).
Re-derives every claim from source; trusts no stored field. Read-only.
Checks:
  (1) canonical keys unique (supplements add no new keys)
  (2) selected_record bytes hash recomputed == stored
  (3) each supplement src (audit) record bytes hash recomputed == stored
  (4) live source file sha256 == record source_sha256 == supplement.source_file_sha256
      (source unchanged since the read)
  (5) authoritative_quote re-extracted from live source at cited lines == stored;
      source_span_hash == sha256(quote)   (§6.4 span 재확인, mechanized)
  (6) every supplement.decision == confirmed_delta
  (7) each supplement traces to a confirmed_delta disposition in the crosswalk
Usage: verify_supplement.py <manifest.json> <records_root> <models_root> <crosswalk_root>
Exit 0 PASS / 1 FAIL."""
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
def extract(path,ranges):
    lines=open(path,encoding="utf-8",errors="replace").read().splitlines()
    return "\n…\n".join("\n".join(lines[a-1:b]) for a,b in ranges)
def resolve_source(models,src):
    c=os.path.join(models,src)
    if os.path.exists(c): return c
    base=os.path.basename(src)
    for r in glob.glob(os.path.join(models,"**",base),recursive=True):
        if r.endswith(src.split("/",1)[-1]) or r.endswith("/"+base): return r
    return None

def crosswalk_deltas(cwroot):
    """(source_sha256, audit_id) set of confirmed_delta across all crosswalks."""
    s=set()
    for cw in glob.glob(os.path.join(cwroot,"*","*.crosswalk.json")):
        j=json.load(open(cw))
        for d in j["dispositions"]:
            if d["disposition"]=="confirmed_delta":
                for aid in d["audit_ids"]: s.add((j["source_sha256"],aid))
    return s

def main():
    man,recroot,models,cwroot=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    M=json.load(open(man)); fails=[]
    xdeltas=crosswalk_deltas(cwroot)
    keys=[]; nsup=0
    def find_under(root, relpath):
        # relpath stored relative to _staging/ ; root is repo root containing _staging
        p=os.path.join(root, relpath)
        return p if os.path.exists(p) else None
    repo_root=recroot.split("_staging/")[0]  # e.g. /home/.../coastal-wiki/
    for e in M["entries"]:
        key=tuple(e["canonical_key"][k] for k in ("model","normalized_path","source_sha256"))
        keys.append(key)
        src_sha=e["canonical_key"]["source_sha256"]
        # (2) selected_record hash
        selp=find_under(os.path.join(repo_root,"_staging"), e["selected_record"]["record_path"])
        if not selp: fails.append(f"{key[1]}: selected_record path missing"); continue
        if sha_bytes(selp)!=e["selected_record"]["record_sha256_bytes"]:
            fails.append(f"{key[1]}: selected_record bytes hash mismatch")
        for sp in e["supplements"]:
            nsup+=1
            # (6) decision
            if sp["decision"]!="confirmed_delta": fails.append(f"{key[1]}: non-delta supplement")
            # (3) audit record hash
            arp=find_under(os.path.join(repo_root,"_staging"), sp["src_record_path"])
            if not arp: fails.append(f"{key[1]}: src record path missing"); continue
            if sha_bytes(arp)!=sp["src_record_sha256_bytes"]:
                fails.append(f"{key[1]}: src(audit) record bytes hash mismatch")
            # (7) crosswalk traceability
            for aid in sp["member_input_ids"]:
                if (src_sha,aid) not in xdeltas:
                    fails.append(f"{key[1]}: supplement {aid} has no confirmed_delta in crosswalk")
            # (4)+(5) source span re-derivation
            srcf=resolve_source(models, sp["source_span"]["path"])
            if not srcf: fails.append(f"{key[1]}: source file missing {sp['source_span']['path']}"); continue
            live_sha=sha_bytes(srcf)
            if live_sha!=sp["source_file_sha256"]:
                fails.append(f"{key[1]}: live source sha != supplement.source_file_sha256 (source changed)")
            # note: span source file may differ from canonical source (doc-vs-code delta); only enforce
            # source_sha256==canonical when the span path IS the canonical file
            if sp["source_span"]["path"]==e["canonical_key"]["normalized_path"] and live_sha!=src_sha:
                fails.append(f"{key[1]}: canonical source sha drift")
            q=extract(srcf, parse_lines(sp["source_span"]["lines"]))
            if q!=sp["authoritative_quote"]:
                fails.append(f"{key[1]}: authoritative_quote does not match live source at cited lines")
            if sha_text(sp["authoritative_quote"])!=sp["source_span_hash"]:
                fails.append(f"{key[1]}: source_span_hash != sha256(quote)")
    # (1) unique keys
    if len(keys)!=len(set(keys)): fails.append("duplicate canonical_key in manifest")
    print(f"entries={len(M['entries'])} supplements={nsup} (manifest says {M.get('supplement_count')})")
    if nsup!=M.get("supplement_count"): fails.append("supplement_count mismatch")
    if fails:
        print("RESULT: FAIL"); [print("  -",x) for x in fails]; sys.exit(1)
    print("RESULT: PASS — supplements span-reconfirmed from live source, hashes re-derived, keys unique, crosswalk-traceable")
    sys.exit(0)

if __name__=="__main__": main()
