#!/usr/bin/env python3
"""R2 결정적 검사 (PLAN v2 §3). 구조·근거 실재·인용 일치·축 모순만 — 의미 타당성은 적대 검증 몫.
사용: python3 check_r2.py <jsonl>... [--expect-ids ids.txt]"""
import glob, hashlib, json, os, sys
from pathlib import Path
R = Path(__file__).resolve().parent
ROOT = R.parents[5]
AX = {"body_status": {"readable", "absent_at_caption", "present_unreadable", "association_unresolved"},
      "document_role": {"model_relation", "definition_or_assumption", "derivation_or_validation", "unknown", None},
      "implementation_relation": {"mapped", "mapped_with_differences", "document_only", "not_applicable", "unresolved"},
      "closure_status": {"resolved", "documented_limit", "unresolved"}}
ORIG = {"existing_contract", "existing_judgment", "new_comparison"}
packets = {}
for f in glob.glob(str(R / "packets/*.json")):
    p = json.load(open(f)); packets[p["caption"]["id"]] = p
_c = {}
def text(path):
    if path not in _c: _c[path] = (ROOT / path).read_text(errors="replace").splitlines()
    return _c[path]
def sha(path): return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
errs, seen = [], {}
args = [a for a in sys.argv[1:] if not a.startswith("--")]
expect = None
if "--expect-ids" in sys.argv:
    ef = sys.argv[sys.argv.index("--expect-ids") + 1]; expect = set(open(ef).read().split()); args = [a for a in args if a != ef]
for f in args:
    for n, l in enumerate(open(f), 1):
        try: r = json.loads(l)
        except Exception as e: errs.append(f"{f}:{n}: JSON {e}"); continue
        i = r.get("id"); w = f"{f}:{n}:{i}"
        if i not in packets: errs.append(f"{w}: 캡션 id 아님"); continue
        seen[i] = seen.get(i, 0) + 1
        for k, vals in AX.items():
            if r.get(k) not in vals: errs.append(f"{w}: {k}='{r.get(k)}'")
        a = r.get("association") or {}
        pa = packets[i]["association"]
        if a.get("status") != pa.get("status"): errs.append(f"{w}: association.status 가 어댑터({pa.get('status')})와 다름 — 바꾸려면 note 에 근거")
        pobj = {o.get("member") for o in pa.get("objects", [])}
        for o in a.get("objects", []):
            if o.get("member") not in pobj: errs.append(f"{w}: 어댑터에 없는 객체 {o.get('member')}")
        eq = r.get("equation_content")
        if r.get("body_status") == "readable":
            if not eq or not eq.get("images_used") or not eq.get("transcription"): errs.append(f"{w}: readable 인데 판독 근거(images_used·transcription) 없음")
        if eq:
            for im in eq.get("images_used", []):
                p = im.get("path", "")
                if not (ROOT / p).exists(): errs.append(f"{w}: images_used 경로 없음 {p}")
                elif im.get("sha256") and im["sha256"] != sha(p): errs.append(f"{w}: images_used sha256 불일치 {p}")
        if r.get("body_status") in ("absent_at_caption",) and eq and eq.get("transcription"): errs.append(f"{w}: absent_at_caption 인데 transcription 있음")
        og = r.get("evidence_origin") or []
        if not og or any(x.get("origin") not in ORIG for x in og): errs.append(f"{w}: evidence_origin 누락/무효")
        for x in og:
            if x.get("origin") != "new_comparison" and not (x.get("ref") and "claims_resolved" in x and "gaps_left" in x):
                errs.append(f"{w}: 재사용 근거에 ref·claims_resolved·gaps_left 필요")
        ir = r.get("implementation_relation")
        ev = r.get("evidence") or []
        if ir in ("mapped", "mapped_with_differences") and not any(e.get("role") == "source_code" for e in ev):
            errs.append(f"{w}: {ir} 인데 source_code 근거 없음")
        if ir == "document_only" and not r.get("search_scope"): errs.append(f"{w}: document_only 인데 search_scope 없음")
        if r.get("closure_status") == "resolved" and (ir == "unresolved" or r.get("body_status") in ("association_unresolved",)):
            errs.append(f"{w}: resolved 인데 미해결 축 존재")
        for e in ev:
            p = e.get("path", "")
            if not p or not (ROOT / p).exists(): errs.append(f"{w}: evidence path 없음 {p}"); continue
            if p.endswith((".png", ".pdf", ".docx", ".doc", ".bin")): continue
            L = text(p); a0, b0 = e.get("line_start", 0), e.get("line_end", e.get("line_start", 0))
            if not (1 <= a0 <= b0 <= len(L)): errs.append(f"{w}: 행 범위 {p}:{a0}-{b0}"); continue
            q = " ".join((e.get("quote") or "").split())
            if q and q not in " ".join(" ".join(L[a0-1:b0]).split()): errs.append(f"{w}: quote 불일치 {p}:{a0}-{b0}")
dups = [i for i, c in seen.items() if c > 1]
if dups: errs.append(f"중복 {len(dups)}: {dups[:5]}")
if expect is not None:
    m = expect - set(seen)
    if m: errs.append(f"누락 {len(m)}: {sorted(m)[:5]}")
print(f"records={sum(seen.values())} unique={len(seen)} errors={len(errs)}")
for e in errs[:200]: print(e)
sys.exit(1 if errs else 0)
