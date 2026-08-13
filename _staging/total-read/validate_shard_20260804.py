#!/usr/bin/env python3
"""shard 단위 §5.1 기계검증 (WO-20260728). usage: validate_shard_20260804.py <run_id> <axis> <model> <prompt_sha_file>"""
import json, os, hashlib, re, sys

TR = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/firesinger/coastal-wiki/models"
def sha(b): return hashlib.sha256(b).hexdigest()
FORBID = {"note_worthy", "importance", "tier", "core"}
def fscan(o):
    if isinstance(o, dict): return any(k in FORBID or fscan(v) for k, v in o.items())
    if isinstance(o, list): return any(fscan(v) for v in o)
    return False
def toks(s): return re.findall(r"[A-Za-z_][A-Za-z0-9_]{1,}", str(s))

def validate(RID, axis, model, prompt_sha_file):
    st = json.load(open(f"{TR}/state/reread-20260728/{RID}.json"))
    prompt_sha = open(os.path.join(TR, prompt_sha_file)).read().strip()
    grand = 0; a_tot = 0; a_bad = 0; n_sem = 0; n_mech = 0; fails = []
    for f in st["files"]:
        if f.get("mechanical_exception"): n_mech += 1; continue
        n_sem += 1; errs = []
        rec = json.load(open(f"{TR}/pending/reread-20260728/{RID}/{f['path_id']}.json"))
        raw = open(os.path.join(ROOT, f["path"]), "rb").read()
        man_file = f"{TR}/chunk-manifests/reread-20260728/{RID}/{f['path_id']}.json"
        man = json.load(open(man_file))
        for k, v in [("artifact_class","semantic_read"),("read_method","llm_full_read"),
                     ("read_status","complete"),("comprehension_status","complete"),
                     ("axis",axis),("model",model),("path",f["path"]),
                     ("run_id",RID),("audit_status","pending")]:
            if rec.get(k) != v: errs.append(k)
        if not str(rec.get("producer","")).startswith("llm:"): errs.append("producer")
        if rec.get("sha256") != sha(raw) or rec.get("source_sha256") != sha(raw): errs.append("sha")
        if rec.get("bytes") != len(raw): errs.append("bytes")
        logical = raw.count(b"\n") + (1 if raw and not raw.endswith(b"\n") else 0)
        if rec.get("lines_or_pages") != logical: errs.append("lines")
        if rec.get("read_range") != f"1-{logical}": errs.append("range")
        if rec.get("chunk_manifest_sha256") != sha(open(man_file,'rb').read()): errs.append("man_sha")
        if rec.get("prompt_sha256") != prompt_sha: errs.append("prompt_sha")
        rcpts = [json.loads(l) for l in open(f"{TR}/chunk-receipts/reread-20260728/{RID}/{f['path_id']}.jsonl")]
        if len(rcpts) != man["total_chunks"]: errs.append("rcpt_n")
        for i, (r, c) in enumerate(zip(rcpts, man["chunks"])):
            if r["chunk_index"] != i or r["chunk_sha256"] != c["chunk_sha256"]: errs.append(f"rcpt{i}"); break
        if rcpts and not rcpts[-1].get("eof"): errs.append("eof")
        if fscan(rec): errs.append("금지필드")
        c8 = rec.get("content", {})
        if [k for k in ("what_it_is","entities","constants","params_defined","equations","io","calls","verbatim_spans","unresolved") if k not in c8]:
            errs.append("content")
        body = raw.split(b"\n"); bad = []
        for fld, keys in [("constants",("name","value")),("params_defined",("name","default")),("equations",("expr","ref"))]:
            for it in c8.get(fld, []) or []:
                loc = it.get("line") or it.get("loc"); a_tot += 1
                if not isinstance(loc, int) or not (1 <= loc <= logical): bad.append((fld, loc)); continue
                tt = toks(it.get(keys[0],"")) + toks(it.get(keys[1],""))
                nums = (re.findall(r"\d+\.?\d*", str(it.get(keys[0],""))) + re.findall(r"\d+\.?\d*", str(it.get(keys[1],""))))[:5]
                if not tt and not nums: continue
                line = body[loc-1].decode("utf-8","replace").lower()
                if not any(x.lower() in line for x in tt) and not any(v in line for v in nums):
                    bad.append((fld, str(it.get(keys[0]))[:25], loc))
        a_bad += len(bad)
        if errs or bad: grand += len(errs) + len(bad); fails.append((f["path"].split("/")[-1], errs, bad[:4]))
    tag = "-".join(RID.split("-")[1:4])
    print(f"{tag}: semantic {n_sem}+mech {n_mech}, 앵커 {a_tot-a_bad}/{a_tot}",
          "→ 전건 통과" if grand == 0 else f"→ 오류 {grand}건")
    for x in fails: print("  FAIL", x)
    return 0 if grand == 0 else 1

if __name__ == "__main__":
    sys.exit(validate(*sys.argv[1:5]))
