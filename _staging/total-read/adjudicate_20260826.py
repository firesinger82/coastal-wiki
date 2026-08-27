#!/usr/bin/env python3
"""맹검 감사 판정 보조 (WO §6, 읽기 전용). Codex 독립 레코드 ↔ Claude 1차 레코드를 원문 대비 비교.

객관 대조만 한다: (a) Codex 레코드 앵커가 원문에 실재하는가(게이트 v5),
(b) entity/constants/params/io/calls 커버리지 차 — 한쪽만 잡은 식별자,
(c) Codex 가 unresolved 에 올린 결함(= Claude 가 놓쳤을 후보) 덤프.
의미 판정(모순·거짓주장·교차라인 누락)은 사람/조정자가 원문으로 최종 확정. content 미생성.

사용: python3 adjudicate_20260826.py <primary_run_id> <audit_run_id>
"""
import sys, os, json, glob, re, hashlib, importlib.util
TR=os.path.dirname(os.path.abspath(__file__)); ROOT="/home/firesinger/coastal-wiki/models"
spec=importlib.util.spec_from_file_location("gate",f"{TR}/reread_gate_20260728.py")
g=importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

def recs(run):
    d={}
    for f in glob.glob(f"{TR}/pending/reread-20260728/{run}/*.json"):
        r=json.load(open(f)); d[r["path"]]=r
    return d

def toks(items, keys=("name",)):
    s=set()
    for it in items or []:
        if isinstance(it,dict):
            for k in keys:
                v=str(it.get(k,""))
                for t in re.findall(r"[A-Za-z_][A-Za-z0-9_]{1,}", v): s.add(t)
        else:
            for t in re.findall(r"[A-Za-z_][A-Za-z0-9_]{1,}", str(it)): s.add(t)
    return s

def main():
    P=recs(sys.argv[1]); A=recs(sys.argv[2])
    common=sorted(set(P)&set(A))
    print(f"1차 {len(P)} · 감사 {len(A)} · 공통 {len(common)}")
    only_p=set(P)-set(A); only_a=set(A)-set(P)
    if only_p: print(f"★감사 누락 파일({len(only_p)}): 감사자가 이 파일을 안 읽음 — 감사 미완")
    if only_a: print(f"★1차에 없는 감사 파일({len(only_a)})")
    flagged=0
    for p in common:
        pr,ar=P[p],A[p]
        raw=open(os.path.join(ROOT,p),"rb").read()
        n=raw.count(b"\n")+(1 if raw and not raw.endswith(b"\n") else 0)
        abad=g.anchor_check(ar,p,n)  # 감사 레코드 앵커 실재
        pc,ac=pr["content"],ar["content"]
        # 커버리지: 식별자 집합 차
        pe=toks(pc.get("entities")); ae=toks(ac.get("entities"))
        pcst=toks(pc.get("constants"))|toks(pc.get("params_defined"))
        acst=toks(ac.get("constants"))|toks(ac.get("params_defined"))
        # 감사자만 잡은 선언/상수(= 1차 누락 후보)
        ent_miss=ae-pe; cst_miss=acst-pcst
        # 결함 신호: 감사자 unresolved 건수
        aun=ac.get("unresolved") or []
        pun=pc.get("unresolved") or []
        signal = bool(abad) or len(ent_miss)>=8 or len(cst_miss)>=3 or (len(aun)>len(pun)+2)
        if signal:
            flagged+=1
            print(f"\n[FLAG] {p}")
            if abad: print(f"   ✗ 감사 레코드 앵커 실재 실패 {len(abad)}건: {abad[:2]}")
            if ent_miss: print(f"   entity 1차미포함(감사만) {len(ent_miss)}: {sorted(ent_miss)[:10]}")
            if cst_miss: print(f"   const/param 1차미포함(감사만) {len(cst_miss)}: {sorted(cst_miss)[:10]}")
            print(f"   unresolved: 1차 {len(pun)} vs 감사 {len(aun)}")
            for u in aun[:4]: print(f"     감사발견: {str(u)[:100]}")
    print(f"\n=== 판정 후보 {flagged}/{len(common)} (사람 최종확정 대상) · 신호無 {len(common)-flagged} ===")

main()
