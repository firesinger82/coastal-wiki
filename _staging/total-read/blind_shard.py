#!/usr/bin/env python3
"""Blinded crosswalk input builder (MERGE-PLAN §2). Produces a vendor-blind,
A/B-randomized adjudication packet for a fresh subagent, plus a PRIVATE keymap
for post-hoc un-blinding. Deterministic (seeded) for reproducibility.
Prints only counts — never finding text — to keep the caller blind at the
equivalence-judgment stage. Reads frozen records (read-only). stdlib only.

Usage: blind_shard.py <base_run_dir> <audit_run_dir> <shard_tag> <out_dir>
Emits <out_dir>/blinded_input.json  (subagent sees this)
      <out_dir>/keymap.json         (caller-only; subagent MUST NOT see)"""
import json, os, re, sys, random, hashlib

def lines(t): return set(int(x) for x in re.findall(r'L(\d{1,6})', t))
def toks(t):  return set(re.findall(r'[A-Za-z_][A-Za-z0-9_]{2,}', t.upper()))

def load(d):
    o={}
    for f in os.listdir(d):
        if f.endswith(".json"):
            r=json.load(open(os.path.join(d,f)))
            o[f]=r
    return o

def candidate(x,y):
    lx,ly=lines(x),lines(y); tx,ty=toks(x),toks(y)
    close = bool(lx&ly) or (min(([abs(p-q) for p in lx for q in ly] or [999]))<=6)
    jac = len(tx&ty)/max(1,len(tx|ty))
    return close or jac>=0.18

def main():
    base_dir,aud_dir,tag,out=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    os.makedirs(out,exist_ok=True)
    b=load(base_dir); a=load(aud_dir)
    common=sorted(set(b)&set(a))
    files_out=[]; keymap={"shard":tag,"files":{}}
    seed=int(hashlib.sha256(tag.encode()).hexdigest(),16)&0xffffffff
    rng=random.Random(seed)
    for fi,f in enumerate(common):
        assert b[f]["source_sha256"]==a[f]["source_sha256"], "sha mismatch "+f
        assert b[f]["path"]==a[f]["path"], "path mismatch "+f
        bu=b[f]["content"].get("unresolved",[]); au=a[f]["content"].get("unresolved",[])
        flip=rng.random()<0.5   # True -> X=audit,Y=base ; False -> X=base,Y=audit
        if flip:
            Xsrc,Ysrc=("audit",au),("base",bu)
        else:
            Xsrc,Ysrc=("base",bu),("audit",au)
        (xrole,xlist),(yrole,ylist)=Xsrc,Ysrc
        # neutral file token (no vendor / no source name)
        ftok=f"F{fi:02d}"
        Xitems=[{"id":f"{ftok}-X{i}","text":t} for i,t in enumerate(xlist)]
        Yitems=[{"id":f"{ftok}-Y{i}","text":t} for i,t in enumerate(ylist)]
        # candidate pairs on original text
        cands=[]
        for i,xt in enumerate(xlist):
            for j,yt in enumerate(ylist):
                if candidate(xt,yt):
                    cands.append([f"{ftok}-X{i}",f"{ftok}-Y{j}"])
        files_out.append({"file_token":ftok,"lang":os.path.splitext(b[f]["path"])[1],
                          "listX":Xitems,"listY":Yitems,"candidate_pairs":cands})
        # keymap: neutral id -> (role, original index); role in {base,audit}
        km={"record_file":f,"source_path":b[f]["path"],"source_sha256":b[f]["source_sha256"],
            "X_role":xrole,"Y_role":yrole,
            "X":{f"{ftok}-X{i}":i for i in range(len(xlist))},
            "Y":{f"{ftok}-Y{j}":j for j in range(len(ylist))}}
        keymap["files"][ftok]=km
    blinded={"shard":tag,"instructions_ref":"see subagent prompt","files":files_out}
    json.dump(blinded,open(os.path.join(out,"blinded_input.json"),"w"),ensure_ascii=False,indent=1)
    json.dump(keymap,open(os.path.join(out,"keymap.json"),"w"),ensure_ascii=False,indent=1)
    nX=sum(len(x["listX"]) for x in files_out); nY=sum(len(x["listY"]) for x in files_out)
    nc=sum(len(x["candidate_pairs"]) for x in files_out)
    print(f"shard={tag} files={len(files_out)} listX={nX} listY={nY} candidate_pairs={nc}")
    print("wrote blinded_input.json + keymap.json to", out)

if __name__=="__main__": main()
