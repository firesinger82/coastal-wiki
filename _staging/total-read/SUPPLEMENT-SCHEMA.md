# supplement-manifest/v1 — canonical 보강 (confirmed_delta 승격)

> MERGE-PLAN §3-4 구현. supplement 게이트 Phase A. 빌더 `build_supplement_manifest.py`, 검증기 `verify_supplement.py`.
> canonical = base(Claude 1차) 불변 유지. supplement = span-재확인된 audit confirmed_delta. **새 canonical key 생성 안 함**(완결게이트 §80-2 "정확히 1회" 보존).

## 구조
`supplement-manifest.json` — canonical key 당 1 entry:
```
canonical_key: {model, normalized_path, source_sha256}
selected_record: base(Claude fable-5) — run_id·record_file·record_path·record_sha256_bytes(재계산)
supplements[]: 확정 delta
  member_input_ids          # 원본 audit finding id (crosswalk 추적)
  finding_text              # audit 원문
  src_run_id·src_record_path·src_record_sha256_bytes(재계산)
  source_span {path, lines} # 증거 위치 (doc-vs-code delta 는 canonical 과 다른 파일 가능)
  source_file_sha256        # 증거 소스파일 실측 sha
  authoritative_quote       # 인용 라인 실소스 재추출 (crosswalk 재구성본 아님)
  source_span_hash          # sha256(quote)
  decision: confirmed_delta·decided_by·decided_at·rationale
  reconfirmed_at·reconfirm_method  # §6.4 span 재확인
```

## verify_supplement.py 게이트 (모든 증거 소스 재도출 — §4 "필드 신뢰 금지")
1. canonical key 유일 (supplement 는 key 추가 안 함).
2. selected_record bytes 해시 재계산 == 저장값.
3. supplement src(audit) record bytes 해시 재계산 == 저장값.
4. **live 소스 sha256 == record source_sha256 == supplement.source_file_sha256** (판독 후 소스 불변).
5. authoritative_quote 를 live 소스 인용라인에서 재추출 == 저장값; source_span_hash == sha256(quote). (§6.4 span 재확인 기계화)
6. 전 supplement decision == confirmed_delta.
7. 각 supplement 가 crosswalk 의 confirmed_delta 처분으로 역추적됨.

## Phase A 결과 (5 supplements)
| shard | canonical | supplement | 결함 |
|---|---|---|---|
| EFDC-000 | aaefdc.f90 | B1 L924-928 | DETTMP 특이행렬 역수 후 ==0 비교, STOPP 가드 사장 |
| FUNWAVE-000 | convert.f | B3 L251-254 | 무경계 DO WHILE TIME() 탐색 OOB |
| FUNWAVE-001 | breaker.f90 | B1 L112,151-152,221-222 | DXg/DYg use-before-assign |
| FUNWAVE-004 | breaker.F | B1 L103,161-168,238-239 | DXg/DYg use-before-assign |
| FUNWAVE-note-000 | funwave-user-manual-full.md | B5 io.F L3361 | 본문 'STATION FILE' vs 파서 키 STATIONS_FILE |

verify PASS. 전 supplement live 소스 재추출·해시 재도출·crosswalk 추적.

## Phase B (예정) — pending in-scope HIGH 50건 span 재확인 → 확정분 편입
FUNWAVE-000 10·001 15·004 25. 직접 수행(검증 위임 금지). 확정분 crosswalk confirmed_delta 승격 후 manifest 재빌드.

## Phase C (예정·게이트) — WO(SPEC.md §80-2) amendment
완결게이트 "고유 canonical key 정확히 1회"에 optional `supplements[]` 수용 명문화. **santa-method Codex 적대검증 경유**(완결게이트 개정은 자기신고 불가, CLAUDE.md 작업규범 #4).
