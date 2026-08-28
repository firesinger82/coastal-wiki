# supplement-manifest/v2 — canonical 보강 (confirmed_delta 승격, Codex-hardened)

> MERGE-PLAN §3-4 구현. 빌더 `build_supplement_manifest.py`, 검증기 `verify_supplement.py`(v4, 4-round 하드닝).
> 적대검증 경위 [SUPPLEMENT-CODEX-REVIEW.md](SUPPLEMENT-CODEX-REVIEW.md). SPEC 반영 §80 "item 2 보강 + canonical supplement".
> canonical = base(Claude 1차) 불변. supplement = span-재확인 + 사람 승인된 audit confirmed_delta. **새 canonical key/ selected_record 생성 안 함**.

## 파일
- `supplement-manifest.json` (supplement-manifest/v2) — canonical key 당 1 entry.
- `supplement-decisions.json` (supplement-decisions/v2) — 사람 승인 receipt (미승인은 status=pending).

## manifest 구조
```
schema, corpus, generated_by(producer), entry_count, supplement_count
entries[]:
  canonical_key {model, normalized_path, source_sha256}
  crosswalk {path, sha256_bytes}                 # 이 key 를 판정한 crosswalk (해시 핀)
  selected_record {reader, run_id, record_file, record_path, record_sha256_bytes, record_source_sha256}
                                                 # crosswalk base 와 정확히 일치(검증기 강제) — 제2 selector 아님
  supplements[]:
    member_input_ids [audit_id...]               # 비어있지 않음, 문법 ^B(0|[1-9]\d*)$
    finding_texts {audit_id: text}               # 각 == 감사레코드 unresolved[idx]
    audit_record {run_id, record_path, record_sha256_bytes, record_source_sha256}  # crosswalk audit 에 핀
    evidence_sources [{path, sha256}]            # 인용 소스 (doc-vs-code 는 canonical 과 다른 파일 가능)
    source_span {path, lines} · authoritative_quote · source_span_hash
    decision: confirmed_delta · decided_by · decided_at · rationale · reconfirmed_at
```

## decisions receipt (사람 게이트)
```
{canonical_source_sha256, canonical_path, audit_id,
 crosswalk_sha256_bytes, source_span_hash, audit_record_sha256_bytes, evidence_sha256[],  # 4-해시 바인딩
 status: pending|approved|rejected, approver(사람), approved_at, note}
```

## verify_supplement.py 이중 게이트 (저장필드 신뢰 금지 — 전부 소스 재도출)
**기계 (M)**: 레코드/crosswalk/evidence bytes 해시 재계산; 각 레코드 source_sha256==key; canonical model/path·
selected_record·audit_record 를 crosswalk 에 핀; **crosswalk 전량 열거해 manifest 가 confirmed_delta 집합과
exact+complete**(누락·초과 0); 전 crosswalk audit_id 문법·모순 disposition 거부; span bounds+quote 재추출+
source_span_hash; evidence realpath containment(abs·`..` 거부); schema/corpus/decision_count/dedup.
**사람 (H)**: 승인 receipt 4-해시 바인딩 일치·status=approved·approver 사람(모델 identity·producer 거부)·
approved_at 필수. **우회 플래그 없음.**

canonical 유효 = M PASS AND H approved. pending·미승인은 항상 FAIL.

## Phase A/B 결과 (23 supplements, pending)
| shard | confirmed_delta |
|---|---|
| EFDC-000 | 1 (DETTMP) |
| FUNWAVE-000 | 3 (convert.f OOB·breaker.F/breaker_gpu.F UBA) |
| FUNWAVE-001 | 8 (breaker.f90·dispersion·wavemaker×4·mod_global·io) |
| FUNWAVE-004 | 10 (breaker.F·wavemaker×4·sediment×2·io·vessel·tracer) |
| FUNWAVE-note-000 | 1 (manual STATIONS_FILE) |

전 supplement mechanical PASS, 사람 승인 0/23(전부 pending). 사용자가 `supplement-decisions.json` 승인 시 canonical 유효.
Phase B 기각 12·MED 11·심층보류 6 은 각 shard `_provenance/delta_candidates.json`.
