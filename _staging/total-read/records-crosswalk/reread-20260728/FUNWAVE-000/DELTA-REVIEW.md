# FUNWAVE-000 crosswalk — 첫 blinded shard (2026-08-27)

> MERGE-PLAN §2 준수 blinded 단일 subagent 판정. 49파일·438 dispositions·verify PASS.
> base=1차(fable5) / audit=감사(codexaudit). subagent 는 벤더라벨 제거·A/B 파일별 무작위로 판독(권한편향 차단).

## 파이프라인
1. `blind_shard.py` — 벤더라벨 제거·seeded A/B 무작위·후보쌍(라인앵커/토큰 유사도) 산출 → `blinded_input.json`(+ caller전용 `keymap.json`).
2. blinded subagent(general-purpose, fresh) — 후보쌍 208건 SAME/CONFLICT/DIFFERENT + findings 521건 재질 HIGH/MED/LOW 판정 → `verdicts.json`.
   - 결과: SAME 83 · CONFLICT 1 · DIFFERENT 124 / HIGH 76 · MED 220 · LOW 225.
3. `finalize_shard.py` — keymap 으로 un-blind, SAME→equivalent(union-find 병합), CONFLICT→conflict, 미매칭 base→base_only, 미매칭 audit→distinct_unconfirmed. HIGH 미매칭-audit → delta 후보 큐.
4. caller 원문 span 대조 → confirmed_delta 승격/기각(§2: 제안≠확정).

## dispositions (438)
| disposition | 수 |
|---|---|
| distinct_unconfirmed | 206 |
| base_only | 153 |
| equivalent | 78 (SAME 83 → 5 many-to-one 병합) |
| confirmed_delta | 1 |
| conflict | 0 (아래 주1) |

주1: subagent CONFLICT 1건(F27 [X4,Y5], 범례 라벨 상충)은 X4 가 SAME(X4↔Y1, no-op 복사루프)로 이미 소비돼 conflict 독립처분 불가 → 상대 finding 처분 rationale 에 교차주석으로 보존(exact-once 유지). 사람 확인 대상.

## delta 후보 23건 (HIGH 재질 미매칭-audit) — 원문 span 검토
- **confirmed 1**: `convert.f` B3 — `DO WHILE(TIME(Kstart)<time_cut); Kstart++` 무경계 탐색(L251-254). TIME 은 dim Ntotal=10000, Ndata=실측(ktime-1). time_cut 이 마지막 timestamp 초과 시 미초기화 원소→Ntotal 초과 시 할당 밖 OOB. base 미검출. → confirmed_delta 승격(evidence_span 기록).
- **refuted 1**: `sediment.F` B3 — `MIN(2.0,(1-n)/CH)*CH` (L152/L249). CH=0 이면 `(1-n)/0`=+Inf 이나 `MIN(2.0,·)`이 상한캡→`×0`=0. IEEE 무해, `-ffpe-trap` 빌드에서만 위험. material delta 아님 → distinct_unconfirmed 유지. **span-gate 가 후보를 기각 = §2 precision 보호 실증.**
- **pending 21**: 그 중 **11건은 .m 벤치마크/후처리 스크립트**(절대규칙 #8 canonical 범위 밖 — 확정돼도 supplement 목적지 없음, 최저 우선). **10건은 in-scope Fortran**(sediment.F B1/B2/B6, bc.f90 B0/B1, breaker.F B0, exchange_gpu0819.F B6, fluxes.F B0, breaker_gpu.F B0, convert.f B1) — supplement 게이트(§3, 누적 shard 대상)로 이월.

전체 목록·상태: `_provenance/delta_candidates.json` (review_status·canonical_scope 필드).

## 재현
`blind_shard.py`(seed=sha256(shard)&0xffffffff) → subagent(verdicts.json 보존) → `finalize_shard.py` → `verify_crosswalk.py`. blinded_input/keymap/verdicts 전량 `_provenance/` 에 동결.
