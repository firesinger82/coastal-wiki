#!/usr/bin/env python3
"""verify_supplement.py v4 — external gate for the supplement manifest
(MERGE-PLAN §3-4, hardened over three Codex adversarial rounds). Read-only.
Re-derives EVERY claim from source; trusts no stored field. NO release bypass.

A supplement is canonical iff: mechanical checks pass AND it carries an approved,
hash-bound, human (non-model) decision receipt. The manifest must ALSO be complete
and exact w.r.t. the crosswalk corpus: exactly the set of crosswalk confirmed_delta
findings, no more (dedup) and no fewer (completeness). cwroot is the delta authority.

Usage: verify_supplement.py <manifest> <records_root> <models_root> <crosswalk_root> <decisions>
Exit 0 = PASS. Exit 1 = FAIL (any mechanical failure OR any unapproved/omitted supplement).
"""
import json, os, re, sys, hashlib, glob

EXPECT_MANIFEST_SCHEMA="supplement-manifest/v2"
EXPECT_DECISIONS_SCHEMA="supplement-decisions/v2"
EXPECT_CORPUS="model-audit-20260831"
AUDIT_ID=re.compile(r"B(0|[1-9]\d*)$")
MODEL_TOKENS={"llm","ai","bot","model","assistant","claude","gpt","gpt-5","chatgpt",
              "codex","grok","gemini","opus","sonnet","haiku","fable","anthropic","openai"}

def sha_bytes(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
def sha_text(t):  return hashlib.sha256(t.encode()).hexdigest()
def parse_lines(spec):
    out=[]
    for part in str(spec).split(","):
        part=part.strip()
        if "-" in part: a,b=part.split("-"); out.append((int(a),int(b)))
        elif part: out.append((int(part),int(part)))
    return out
def is_human(ap, producer):
    if not ap or not re.fullmatch(r"[A-Za-z][A-Za-z0-9 ._@-]{1,63}", ap): return False  # ASCII only (blocks homoglyphs)
    if set(re.split(r"[ ._@-]+", ap.lower())) & MODEL_TOKENS: return False
    return ap!=producer

def main():
    known={"--"}  # no optional flags accepted
    for x in sys.argv[1:]:
        if x.startswith("--") and x not in known:
            print(f"RESULT: FAIL — unknown option {x}"); sys.exit(1)
    a=[x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a)<5: print("usage: verify_supplement.py <manifest> <records_root> <models_root> <crosswalk_root> <decisions>"); sys.exit(1)
    man,recroot,models,cwroot,decf=a[:5]
    models_real=os.path.realpath(models); staging_real=os.path.realpath(recroot.split("_staging/")[0]+"_staging")
    cwroot_real=os.path.realpath(cwroot)
    M=json.load(open(man)); fails=[]; pending=[]
    def under(root_real, p):
        rp=os.path.realpath(p)
        return rp if rp.startswith(root_real+os.sep) and os.path.exists(rp) else None
    def under_staging(rel): return under(staging_real, os.path.join(staging_real, rel))
    def resolve_contained(src): return under(models_real, os.path.join(models, src))

    # schema/corpus
    if M.get("schema")!=EXPECT_MANIFEST_SCHEMA: fails.append(f"manifest schema != {EXPECT_MANIFEST_SCHEMA}")
    if M.get("corpus")!=EXPECT_CORPUS: fails.append(f"manifest corpus != {EXPECT_CORPUS}")
    producer=M.get("generated_by","")

    # decisions
    decisions={}
    if os.path.exists(decf):
        dj=json.load(open(decf))
        if dj.get("schema")!=EXPECT_DECISIONS_SCHEMA: fails.append(f"decisions schema != {EXPECT_DECISIONS_SCHEMA}")
        if dj.get("corpus")!=EXPECT_CORPUS: fails.append("decisions corpus mismatch")
        if dj.get("decision_count")!=len(dj.get("decisions",[])): fails.append("decisions decision_count missing/mismatch")
        for d in dj.get("decisions",[]):
            k=(d.get("canonical_source_sha256"), d.get("audit_id"))
            if k in decisions: fails.append(f"duplicate decision receipt {k}")
            decisions[k]=d
    else:
        fails.append("decisions file missing")

    # AUTHORITY: enumerate ALL crosswalk confirmed_delta across cwroot (completeness/exactness)
    authority={}   # (src_sha, aid) -> {"cw":path, "model":, "path":, "disp_kinds":set, "audit_run_id":, "audit_record_file":, "audit_record_sha256_bytes":, "base_*":}
    cw_bad=[]
    for cw in glob.glob(os.path.join(cwroot_real,"*","*.crosswalk.json")):
        j=json.load(open(cw)); ssha=j.get("source_sha256")
        aid_kinds={}
        for dd in j["dispositions"]:
            for aid in dd.get("audit_ids",[]):
                if not AUDIT_ID.fullmatch(aid): cw_bad.append(f"{os.path.basename(cw)}: malformed audit_id {aid}")
                aid_kinds.setdefault(aid,set()).add(dd["disposition"])
        for aid,kinds in aid_kinds.items():
            if "confirmed_delta" in kinds:
                if kinds-{"confirmed_delta"}: cw_bad.append(f"{os.path.basename(cw)}: {aid} contradictory {kinds}")
                authority[(ssha,aid)]={"cw":cw,"model":j["model"],"path":j["source_path"],
                    "audit_run_id":j["audit_run_id"],"audit_record_file":j["audit_record_file"],
                    "audit_record_sha256_bytes":j["audit_record_sha256_bytes"],
                    "base_run_id":j["base_run_id"],"base_record_file":j["base_record_file"],
                    "base_record_sha256_bytes":j["base_record_sha256_bytes"],
                    "cw_sha":sha_bytes(cw),"source_sha256":ssha}
    fails.extend(cw_bad)

    # manifest population
    if not M.get("entries"): fails.append("empty manifest")
    if M.get("entry_count")!=len(M.get("entries",[])): fails.append("entry_count mismatch")
    keys=[]; promo=set(); nsup=0; napproved=0
    for e in M["entries"]:
        ck=e["canonical_key"]; src_sha=ck["source_sha256"]; tag=ck["normalized_path"]
        keys.append((ck["model"],ck["normalized_path"],ck["source_sha256"]))  # canonical order, not values()-order
        cwp=under_staging(e["crosswalk"]["path"])
        if not cwp: fails.append(f"{tag}: crosswalk path missing/escapes"); continue
        if sha_bytes(cwp)!=e["crosswalk"]["sha256_bytes"]: fails.append(f"{tag}: crosswalk hash drift")
        cwj=json.load(open(cwp))
        # canonical identity bound to crosswalk (F1/F8)
        if cwj.get("source_sha256")!=src_sha: fails.append(f"{tag}: crosswalk source_sha256 != key")
        if cwj.get("model")!=ck["model"]: fails.append(f"{tag}: canonical model != crosswalk model")
        if cwj.get("source_path")!=ck["normalized_path"]: fails.append(f"{tag}: canonical path != crosswalk source_path")
        # selected_record pinned to crosswalk base (F3/F7)
        sr=e["selected_record"]
        if (sr["run_id"],sr["record_file"],sr["record_sha256_bytes"])!=(cwj.get("base_run_id"),cwj.get("base_record_file"),cwj.get("base_record_sha256_bytes")):
            fails.append(f"{tag}: selected_record not crosswalk-pinned base")
        selp=under_staging(sr["record_path"])
        if not selp: fails.append(f"{tag}: selected_record missing"); continue
        if sha_bytes(selp)!=sr["record_sha256_bytes"]: fails.append(f"{tag}: selected_record hash mismatch")
        if json.load(open(selp)).get("source_sha256")!=src_sha: fails.append(f"{tag}: selected_record.source_sha256 != key")
        for sp in e["supplements"]:
            nsup+=1
            if sp["decision"]!="confirmed_delta": fails.append(f"{tag}: non-delta supplement"); continue
            mids=sp["member_input_ids"]
            if not mids: fails.append(f"{tag}: empty member_input_ids"); continue
            # audit record PINNED to crosswalk audit (F3 — fixes substitution bypass)
            ar=sp["audit_record"]
            if (ar["run_id"], os.path.basename(ar["record_path"]), ar["record_sha256_bytes"])!=(cwj.get("audit_run_id"),cwj.get("audit_record_file"),cwj.get("audit_record_sha256_bytes")):
                fails.append(f"{tag}: audit_record not crosswalk-pinned audit"); continue
            arp=under_staging(ar["record_path"])
            if not arp: fails.append(f"{tag}: audit record missing"); continue
            if sha_bytes(arp)!=ar["record_sha256_bytes"]: fails.append(f"{tag}: audit record hash mismatch")
            arec=json.load(open(arp))
            if arec.get("source_sha256")!=src_sha: fails.append(f"{tag}: audit record.source_sha256 != key")
            au=arec["content"]["unresolved"]; ftexts=sp.get("finding_texts",{})
            for aid in mids:
                if not AUDIT_ID.fullmatch(aid): fails.append(f"{tag}: bad audit_id {aid}"); continue
                if (src_sha,aid) in promo: fails.append(f"{tag}: duplicate promotion {aid}")
                promo.add((src_sha,aid))
                if (src_sha,aid) not in authority: fails.append(f"{tag}: {aid} not a crosswalk confirmed_delta"); continue
                idx=int(aid[1:])
                if not (0<=idx<len(au)): fails.append(f"{tag}: {aid} out of audit range"); continue
                if ftexts.get(aid)!=au[idx]: fails.append(f"{tag}: {aid} finding_text != audit unresolved[{idx}]")
            # evidence + span
            ev_paths=set()
            for ev in sp["evidence_sources"]:
                ev_paths.add(ev["path"]); srcf=resolve_contained(ev["path"])
                if not srcf: fails.append(f"{tag}: evidence not found/escapes {ev['path']}"); continue
                live=sha_bytes(srcf)
                if live!=ev["sha256"]: fails.append(f"{tag}: evidence {ev['path']} sha != stored")
                if ev["path"]==ck["normalized_path"] and live!=src_sha: fails.append(f"{tag}: canonical evidence sha != key")
            spr=sp["source_span"]
            if spr["path"] not in ev_paths: fails.append(f"{tag}: span path not in evidence_sources")
            srcf=resolve_contained(spr["path"])
            if srcf:
                lines=open(srcf,encoding="utf-8",errors="replace").read().splitlines(); nl=len(lines); ok=True; segs=[]
                for x,y in parse_lines(spr["lines"]):
                    if not (1<=x<=y<=nl): fails.append(f"{tag}: span {x}-{y} OOB"); ok=False; break
                    segs.append("\n".join(lines[x-1:y]))
                if ok:
                    q="\n…\n".join(segs)
                    if not q.strip(): fails.append(f"{tag}: empty quote")
                    if q!=sp["authoritative_quote"]: fails.append(f"{tag}: quote != live source")
                    if sha_text(sp["authoritative_quote"])!=sp["source_span_hash"]: fails.append(f"{tag}: span hash mismatch")
            # human gate
            ev_hashes=sorted(ev["sha256"] for ev in sp["evidence_sources"])
            for aid in mids:
                rec=decisions.get((src_sha,aid))
                if not rec or rec.get("status")!="approved": pending.append(f"{tag} {aid}"); continue
                if rec.get("crosswalk_sha256_bytes")!=e["crosswalk"]["sha256_bytes"]: fails.append(f"{tag} {aid}: receipt crosswalk hash mismatch")
                if rec.get("source_span_hash")!=sp["source_span_hash"]: fails.append(f"{tag} {aid}: receipt span hash mismatch")
                if rec.get("audit_record_sha256_bytes")!=sp["audit_record"]["record_sha256_bytes"]: fails.append(f"{tag} {aid}: receipt audit-record hash mismatch")
                if sorted(rec.get("evidence_sha256",[]))!=ev_hashes: fails.append(f"{tag} {aid}: receipt evidence hash mismatch")
                if rec.get("canonical_path")!=ck["normalized_path"]: fails.append(f"{tag} {aid}: receipt canonical_path mismatch")
                if not rec.get("approved_at"): fails.append(f"{tag} {aid}: receipt missing approved_at")
                if not is_human(rec.get("approver",""), producer): fails.append(f"{tag} {aid}: approver '{rec.get('approver')}' not an independent human")
                else: napproved+=1
    # COMPLETENESS + EXACTNESS vs authority (fixes omission bypass; uses cwroot)
    missing=set(authority)-promo
    extra=promo-set(authority)
    if missing: fails.append(f"manifest omits {len(missing)} crosswalk confirmed_delta(s): "+", ".join(f"{p}:{a}" for p,a in sorted(missing))[:400])
    if extra:   fails.append(f"manifest promotes {len(extra)} non-authority delta(s)")
    if len(keys)!=len(set(keys)): fails.append("duplicate canonical_key")
    if nsup!=M.get("supplement_count"): fails.append("supplement_count mismatch")
    print(f"entries={len(M.get('entries',[]))} supplements={nsup} authority={len(authority)} approved={napproved} pending={len(pending)} mechanical_fails={len(fails)}")
    if pending: print("UNAPPROVED: "+", ".join(sorted(set(pending))))
    if fails: print("RESULT: FAIL"); [print("  -",x) for x in fails[:40]]; sys.exit(1)
    if pending: print("RESULT: FAIL — mechanical PASS but supplements lack approved human receipts (작업규범 #4). No bypass."); sys.exit(1)
    print("RESULT: PASS — evidence re-derived from source; manifest exact & complete vs crosswalk authority; every supplement human-approved with hash-bound receipts."); sys.exit(0)

if __name__=="__main__": main()
