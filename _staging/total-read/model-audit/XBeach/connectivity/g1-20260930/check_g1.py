#!/usr/bin/env python3
"""G1 결정적 검사 (PLAN v2 §3.1). 인용 일치·참조 무결성만 — 결속 타당성은 검사하지 않는다.
사용: python3 check_g1.py <jsonl>... [--expect-ids ids.txt]"""
import hashlib, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
G = Path(__file__).resolve().parent
C = G.parent
RES = {"direct_edge": {"call_site", "visibility", "definition", "compatibility"},
       "generic_edge": {"call_site", "visibility", "generic_interface", "specific_signature", "compatibility"},
       "indirect_interface": {"call_site", "pointer_or_binding_decl", "abstract_interface", "registration"},
       "intrinsic": {"call_site", "shadowing_check"},
       "external_interface": {"call_site", "external_decl", "link_evidence"},
       "not_a_call": {"call_site", "scope_declaration"},
       "unresolved": {"call_site"}}
STATUS = {"confirmed", "excluded", "undetermined"}
inputs = json.load(open(G / "inputs.json"))["files"]
cands = {json.loads(l)["id"]: json.loads(l) for l in open(C / "runtime-20260912/call-candidates.jsonl")}
procs = {json.loads(l)["id"] for l in open(C / "runtime-20260912/procedures.jsonl")}
gen = json.load(open(C / "runtime-20260912/generated-links.json"))["records"]
gen_names = {(r["name"], r["sha256"][:12], d["line"], d["name"]) for r in gen for d in r["definitions"]}
gen_names |= {(r["name"], r["sha256"][:12], s["line"], s["specific"]) for r in gen for s in r["generic_specifics"]}
_lines = {}
def lines(path):
    if path not in _lines:
        _lines[path] = (ROOT / path).read_text(errors="replace").splitlines()
    return _lines[path]
errs, seen = [], {}
args = [a for a in sys.argv[1:] if not a.startswith("--")]
expect = None
if "--expect-ids" in sys.argv:
    expect = set(Path(sys.argv[sys.argv.index("--expect-ids") + 1]).read_text().split())
    args = [a for a in args if a != sys.argv[sys.argv.index("--expect-ids") + 1]]
for f in args:
    for n, l in enumerate(open(f), 1):
        try: r = json.loads(l)
        except Exception as e: errs.append(f"{f}:{n}: JSON {e}"); continue
        i = r.get("id"); where = f"{f}:{n}:{i}"
        if i not in cands: errs.append(f"{where}: 동결 후보에 없는 id"); continue
        seen[i] = seen.get(i, 0) + 1
        res = r.get("resolution")
        if res not in RES: errs.append(f"{where}: resolution '{res}'"); continue
        roles = {e.get("role") for e in r.get("evidence", [])}
        miss = RES[res] - roles
        if miss: errs.append(f"{where}: 필수 role 누락 {sorted(miss)}")
        if res == "unresolved" and not all(r.get(k) for k in ("reason", "missing_evidence", "impact")):
            errs.append(f"{where}: unresolved 는 reason·missing_evidence·impact 필수")
        for e in r.get("evidence", []):
            p = e.get("path", "")
            if p not in inputs: errs.append(f"{where}: evidence path 가 inputs.json 에 없음 {p}"); continue
            if e.get("sha256") and e["sha256"] != inputs[p]: errs.append(f"{where}: sha256 불일치 {p}")
            L = lines(p); a, b = e.get("line_start", 0), e.get("line_end", e.get("line_start", 0))
            if not (1 <= a <= b <= len(L)): errs.append(f"{where}: 행 범위 {p}:{a}-{b}"); continue
            q = " ".join(e.get("quote", "").split())
            if q and q not in " ".join(" ".join(L[a-1:b]).split()): errs.append(f"{where}: quote 불일치 {p}:{a}-{b}")
            if e.get("role") == "call_site" and not (a <= cands[i]["line_start"] <= b):
                errs.append(f"{where}: call_site 행이 후보 line_start({cands[i]['line_start']})를 포함하지 않음")
        bs = r.get("bindings", [])
        if res in ("direct_edge", "generic_edge") and not bs: errs.append(f"{where}: bindings 없음")
        for b in bs:
            t = b.get("target", "")
            if t.startswith("gen:"):
                try:
                    out, rest = t[4:].split("@", 1); sha12, ln, name = rest.split(":", 2)
                    if (out, sha12, int(ln), name) not in gen_names: errs.append(f"{where}: 생성 대상 레지스트리에 없음 {t}")
                except ValueError: errs.append(f"{where}: gen 대상 형식 {t}")
            elif t.startswith(("ext:", "intrinsic:")) or t == "unknown": pass
            elif t not in procs: errs.append(f"{where}: target 이 procedures.jsonl 에 없음 {t}")
            st = (b.get("applicability") or {}).get("status")
            if st not in STATUS: errs.append(f"{where}: applicability.status '{st}'")
dups = [i for i, c in seen.items() if c > 1]
if dups: errs.append(f"중복 id {len(dups)}: {dups[:5]}")
if expect is not None:
    missing = expect - set(seen)
    if missing: errs.append(f"누락 id {len(missing)}: {sorted(missing)[:5]}")
print(f"records={sum(seen.values())} unique={len(seen)} errors={len(errs)}")
for e in errs[:200]: print(e)
sys.exit(1 if errs else 0)
