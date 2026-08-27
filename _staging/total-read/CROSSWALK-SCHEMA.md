# crosswalk/v1 스키마 — 1차↔감사 처분 기록

> MERGE-PLAN-20260827 §1-4 구현. 파일럿(EFDC-000) 확정. 출력: `records-crosswalk/reread-20260728/<source_basename>.crosswalk.json`.
> 빌드 `build_crosswalk.py`, 검증 `verify_crosswalk.py`(외부 게이트 — 원본 finding 유실 0 보장).

## 파일당 1 crosswalk 문서

동일 소스파일에 대한 두 레코드층을 대조한다:
- **base** = 1차 판독(`*-fable5-*`, Claude) = 현 canonical 후보 (정밀·불변)
- **audit** = 감사(`*-codexaudit-*`, Codex gpt-5.6-sol) = 병존 감사층 (불변)

두 레코드의 `content.unresolved[]` 항목을 finding 으로 보고, 각각 `A{i}`(base)·`B{i}`(audit) id 부여.

## 처분(disposition) — 6종

plan §1 은 감사 finding 관점 5종을 열거. **`base_only` 추가(사용자 승인 2026-08-27)** — 1차-only finding 도 처분을 받아야 검증기의 양방향 zero-loss 보장이 성립.

| disposition | base_ids | audit_ids | 의미 |
|---|---|---|---|
| `equivalent` | ≥1 | ≥1 | 두 벤더가 같은 결함(표현 차이 포함). many-to-one 허용(원문 span 대조로 확정). |
| `confirmed_delta` | ∅ | =1 | 감사가 찾고 1차가 놓친 **원문 검증된 material 결함**. `evidence_span.quote` 필수. canonical supplement 승격 대상. |
| `distinct_unconfirmed` | ∅ | ≥1 | 감사 신규이나 material 미확정. 오버레이에만, 승격 안 함. |
| `rejected` | ∅ | ≥1 | 감사 finding 이 실 결함 아님/환각. |
| `conflict` | ≥1 | ≥1 | 두 서술이 상충. 사람 확정 대상. |
| `base_only` | ≥1 | ∅ | 1차-only. canonical(=1차)에 그대로 유지, 승격 없음. |

## 문서 필드

```
schema, model, shard, source_path, source_sha256
base_run_id, audit_run_id, base_record_file, audit_record_file
base_record_sha256_bytes, audit_record_sha256_bytes   # 검증기가 재계산 대조(§4: 필드 신뢰 금지)
base_finding_count, audit_finding_count
provenance { pilot, blinded, note, decided_by, decided_at }
dispositions[] {
  disposition, base_ids[], audit_ids[],
  base_member_text[], audit_member_text[],   # 원문 스냅샷(가독성·유실검출)
  representative, rationale, decided_by, decided_at,
  evidence_span? { path, lines, quote }      # confirmed_delta 필수
}
```

## verify_crosswalk.py 보장

1. **유실 0** — 모든 `A{i}`·`B{i}` 가 정확히 한 disposition 에 등장(중복·누락·범위초과 적발).
2. **처분 전건 부여** — 유효 disposition 값 + 종류별 shape 불변식.
3. **confirmed_delta 게이트** — base_ids 공집합·audit_ids 단일·`evidence_span.quote` 존재.
4. **provenance 무결성** — 부모 레코드 bytes 해시 **재계산** 대조, 소스 sha 3층 일치.
5. 빈 실행 실패(false PASS 방지).

tamper 4종(disposition 삭제·base id 중복·delta span 제거·해시 위조) 전건 FAIL 확인.

## 파일럿 결과 (EFDC-000, 6파일)

raw 153(base 69 / audit 84) → dispositions 130:
`distinct_unconfirmed` 62 · `base_only` 46 · `equivalent` 21 · `confirmed_delta` 1.

- **confirmed_delta = aaefdc.f90 L924-928 DETTMP** — 특이행렬 역수(`1./det`) 후 `== 0.0` 비교: 특이시 Inf 이지 0 아니므로 STOPP 가드가 사장코드. 1차 전건 미검출. 원문 span 검증 완료.
- 파일럿은 **UNBLINDED 자율판독**(스코핑에 라벨노출) — 파이프라인 mechanics 검증용. **운영 shard 는 blinded 단일 subagent(§2: 라벨제거·A/B 무작위)** 로 진행(사용자 승인).
