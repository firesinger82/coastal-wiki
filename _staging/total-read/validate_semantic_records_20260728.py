#!/usr/bin/env python3
"""semantic 레코드 기계 검증기 (SPEC.md 스키마 v2, 2026-07-28)

용도: 재판독 shard 의 JSONL 을 완결 게이트 5항(라인/해시/chunk 검증) 기준으로 검사.
스크립트 허용 범위(SPEC v2 '스크립트 허용/금지')만 수행 — 레코드 수정·생성 없음, 판정 보고만.

usage: python3 validate_semantic_records_20260728.py <records.jsonl> <chunk-manifest.jsonl>
exit 0 = 전건 통과, 1 = 결함 있음(불합격 shard → records-rejected/ 대상), 2 = 사용 오류
"""
import json, sys, os, hashlib

MODELS_ROOT = "/home/firesinger/coastal-wiki/models"
REQUIRED_TOP = ["axis", "model", "path", "sha256", "bytes", "lines_or_pages",
                "read_range", "read_at", "content",
                "artifact_class", "producer", "read_method", "comprehension_status",
                "source_sha256", "chunk_manifest_sha256", "prompt_sha256", "run_id"]
FORBIDDEN = ["note_worthy", "importance", "tier", "core", "reader"]  # reader 는 v2 에서 producer 로 대체
VALID = {"artifact_class": {"semantic_read"},
         "read_method": {"llm_full_read"},
         "comprehension_status": {"complete", "partial", "failed"}}

def norm(p):
    p = p.replace('/home/firesinger/coastal-wiki/', '')
    return p[7:] if p.startswith('models/') else p

def main(rec_path, manifest_path):
    manifest = {}
    for l in open(manifest_path):
        m = json.loads(l)
        manifest[m["path"]] = m
    man_sha = hashlib.sha256(open(manifest_path, 'rb').read()).hexdigest()

    errors, seen = [], {}
    n = 0
    for i, l in enumerate(open(rec_path), 1):
        n += 1
        def err(msg): errors.append(f"line {i}: {msg}")
        try:
            r = json.loads(l)
        except Exception as e:
            err(f"JSON 오류: {e}"); continue
        for k in REQUIRED_TOP:
            if k not in r: err(f"필수 필드 결측: {k}")
        for k in FORBIDDEN:
            if k in r: err(f"금지 필드 존재: {k}")
        for k, vals in VALID.items():
            if r.get(k) and r[k] not in vals: err(f"{k} 값 위반: {r[k]}")
        if not str(r.get("producer", "")).startswith("llm:"):
            err(f"producer 는 llm:<vendor/model> 이어야 함: {r.get('producer')}")
        p = norm(r.get("path", ""))
        key = (r.get("model", ""), p)
        if key in seen: err(f"중복 key (첫 등장 line {seen[key]}): {key}")
        seen[key] = i
        m = manifest.get(p)
        if m is None:
            err(f"chunk manifest 에 없는 path: {p}"); continue
        if r.get("sha256") != m["source_sha256"] or r.get("source_sha256") != m["source_sha256"]:
            err(f"sha256 불일치 (manifest={m['source_sha256'][:12]}…)")
        if r.get("chunk_manifest_sha256") != man_sha:
            err("chunk_manifest_sha256 불일치")
        if r.get("bytes") != m["bytes"]: err(f"bytes 불일치 {r.get('bytes')} != {m['bytes']}")
        if r.get("lines_or_pages") != m["lines"]: err(f"행수 불일치 {r.get('lines_or_pages')} != {m['lines']}")
        # chunk 수신확인: content.chunks_read = [chunk index 전부] 요구
        acks = r.get("content", {}).get("chunks_read") or r.get("chunks_read")
        if r.get("comprehension_status") == "complete":
            if acks != list(range(1, m["n_chunks"] + 1)):
                err(f"chunk 수신확인 불완전: {acks} != 1..{m['n_chunks']}")
        # 앵커 실재 검사: 라인번호 필드가 실제 파일 범위 안이고, 이름이 그 줄에 실재하는가
        full = os.path.join(MODELS_ROOT, p)
        try:
            raw = open(full, 'rb').read().split(b"\n")
        except Exception as e:
            err(f"원본 열기 실패: {e}"); continue
        c = r.get("content", {})
        for fld in ("constants", "params_defined", "equations"):
            for item in c.get(fld, []) or []:
                loc = item.get("line") or item.get("loc")
                if not isinstance(loc, int) or not (1 <= loc <= max(m["lines"], 1)):
                    err(f"{fld} 앵커 범위 밖: {item}"); continue
                name = str(item.get("name") or item.get("expr") or "")[:40]
                probe = name.split("(")[0].split("=")[0].strip()
                if probe:
                    line_txt = raw[loc - 1].decode("utf-8", errors="replace") if loc - 1 < len(raw) else ""
                    if probe.lower() not in line_txt.lower():
                        err(f"{fld} 앵커 미실재 line {loc}: {probe!r}")
    # manifest 대비 누락 (shard 범위 파일 목록은 호출측이 판단 — 여기선 레코드가 가리키는 파일만 검사)
    print(f"{rec_path}: {n}행, key {len(seen)}, 오류 {len(errors)}")
    for e in errors[:50]:
        print("  ✗", e)
    if len(errors) > 50: print(f"  … 외 {len(errors)-50}건")
    return 1 if errors else 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
