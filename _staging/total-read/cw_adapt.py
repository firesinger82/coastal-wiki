#!/usr/bin/env python3
"""Adapt XBeach R1/R2 shard jsonl -> per-file record dirs consumable by
blind_shard.py / finalize_shard.py / verify_crosswalk.py.
Record schema (subset the tools use): path, source_sha256, run_id, content.unresolved[str]
Finding dict -> string rendered with L-prefixed line anchors so candidate() line matching works."""
import json,os,re,hashlib,sys
W="/home/firesinger/coastal-wiki"; SRC=f"{W}/models/XBeach/raw/source_code"
D=f"{W}/_staging/total-read/model-audit/XBeach"; OUT=f"{D}/cw"
RUN={("R1","XBeach-000"):"01a05a52-c773-7170-b126-7a88b545d9e6",
     ("R1","XBeach-001"):"01a05a5b-a17d-7cd0-8b9b-49a161c8810c",
     ("R1","XBeach-002"):"01a05a67-e2d6-7e11-b2eb-ed7a4a8bc0af",
     ("R1","XBeach-003"):"01a05a73-c44f-73d1-9740-9462379b36f1",
     ("R1","XBeach-004"):"01a05a7d-6f0e-70e0-856c-72e0db530fda",
     ("R1","XBeach-005"):"01a05a82-9b09-7e13-97be-a61dffd0da0d",
     ("R2","XBeach-000"):"01a05a9c-78d9-7eb0-9d9e-e5e019072cda",
     ("R2","XBeach-001"):"01a05aa6-f6db-7991-802e-4d57ae64a826",
     ("R2","XBeach-002"):"01a05ab3-8036-7660-84fb-58c476606a27",
     ("R2","XBeach-003"):"01a05ac0-7e92-7031-ae47-79d30eab7b40",
     ("R2","XBeach-004"):"01a05acc-9545-75d1-9790-69ad91b9aa3a",
     ("R2","XBeach-005"):"01a05ada-6ee0-72f3-abb0-11672883260c"}
PARTIAL_RUN="01a056f9-9d41-7cf1-972b-2992f7eaf5c6"   # R1-000 first 6 files (earlier partial run)
PARTIAL={"trunk/src/xbeach/input.F90","trunk/src/xbeach/xbeach.F90",
         "trunk/src/xbeachlibrary/constants.F90","trunk/src/xbeachlibrary/typesandkinds.F90",
         "trunk/src/xbeachlibrary/loopcounters.F90","trunk/src/xbeachlibrary/sleeper.F90"}

def anchor(s):
    """'629-630' / '409-416, 426-434' / '19' -> 'L629-L630', ... (line tokens the matcher reads)"""
    return re.sub(r'(?<![\w.])(\d{1,6})(?![\w.])', r'L\1', str(s))

def render(u):
    return f"[{anchor(u.get('lines',''))}] ({u.get('severity','?')}/{u.get('class','?')}) {u.get('finding','')}"

def sha_file(p):
    return hashlib.sha256(open(p,'rb').read()).hexdigest()

def main():
    tot={}
    for shard in [f"XBeach-00{i}" for i in range(6)]:
        for round_,suffix in (("R1",".jsonl"),("R2","-R2.jsonl")):
            src=f"{D}/{shard}{suffix}"
            od=f"{OUT}/records-{round_.lower()}/{shard}"; os.makedirs(od,exist_ok=True)
            n=0
            for line in open(src):
                d=json.loads(line); p=d["path"]
                ssha=sha_file(f"{SRC}/{p}")
                rid=PARTIAL_RUN if (round_=="R1" and shard=="XBeach-000" and p in PARTIAL) else RUN[(round_,shard)]
                rec={"axis":"code","model":"XBeach","path":p,"source_sha256":ssha,
                     "lines_or_pages":d["lines_read"],"read_status":"complete",
                     "reader":d["reader"],"producer":"llm:openai/codex",
                     "read_method":"llm_full_read","artifact_class":"semantic_read",
                     "run_id":f"xbeach-{round_.lower()}-{shard}-codex-{rid}",
                     "shard":shard,"round":round_,
                     "content":{"unresolved":[render(u) for u in d["unresolved"]]}}
                fn=hashlib.sha256(p.encode()).hexdigest()+".json"
                json.dump(rec,open(f"{od}/{fn}","w"),ensure_ascii=False,indent=1)
                n+=1
            tot[(shard,round_)]=n
    for k in sorted(tot): print(k, tot[k])

if __name__=="__main__": main()
