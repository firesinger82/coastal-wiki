# 감사 반영 설계 — 오버레이 + delta 승격 (2026-08-27, 확정)

> santa-method: 설계 → Codex 적대검증(HIGH 1·MED 3, '전량 union→canonical 은 정밀도 저하') → 반영.
> 사용자 결정(2026-08-27): 전량 union 폐기, **오버레이+delta 승격** 채택. canonical 무결성 우선.
> 원본 2층(1차 `*-fable5-*` · 감사 `*-codexaudit-*` pending)은 **불가침**.

## 0. 결정 요지
전량 union 을 canonical 에 물리면 확정 delta 1건(DETTMP) 대비 미판정 findings 2,600건이 유입돼
precision 이 떨어지고 소비자가 "2벤더 검증"으로 오해한다(적대검증 메타 지적). 대신:

```
canonical      = Claude 1차 유지 (정밀·불변, 현 canonical 후보)
감사층         = Codex 레코드 병존 (불변)
crosswalk      = finding 별 처분 기록
canonical 보강 = 원문 확인된 delta 만 supplement 로 승격
union view     = 검색용 동적 오버레이 (canonical truth 아님)
구조필드       = 병합 안 함 (식별자 정규화·앵커≠정확성 문제, 적대검증 HIGH)
```

## 1. crosswalk (핵심 산물)
파일별로 1차 unresolved ↔ 감사 unresolved 를 대조해 각 finding 에 처분 부여:
- `equivalent` — 두 벤더가 같은 결함(다른 표현 포함). 대표 1건 + member id.
- `confirmed_delta` — 감사가 찾고 1차가 놓친 **원문 검증된 material 결함**(예: DETTMP).
- `distinct_unconfirmed` — 감사 신규이나 material 미확정(사장코드·방어경고 등). 오버레이에만.
- `rejected` — 감사 finding 이 실 결함 아님/환각. 근거 기록.
- `conflict` — 두 서술이 상충. 사람 확정 대상.

출력: `records-crosswalk/reread-20260728/<file>.json` — 원본 finding id, 처분, 근거 span.

## 2. 실행자·편향 방지 (적대검증 MED 반영)
- crosswalk 판정 = Claude 에이전트, 단 **벤더명·base 라벨 제거 + A/B 순서 무작위화**.
- 에이전트는 `equivalent/distinct/conflict` 제안 + 근거 span 만. **many-to-one 병합·confirmed_delta 는
  원문 span 대조로만 확정**(제안≠확정).
- 비용 절감: 전량이 아니라 **라인앵커·텍스트 유사도로 후보쌍만** 판정 투입.

## 3. delta 승격 (canonical 보강)
- `confirmed_delta` 만 canonical supplement 로. supplement 는 hash 고정, 원본 미변경.
- manifest: canonical key → `selected_record`(Claude) + `supplements[]`(확정 delta, 원본 감사 locator+span).
- WO §7 canonical 선택·§5.3 완결게이트를 supplement 허용하도록 **좁게 개정**(별도 amendment).

## 4. provenance (적대검증 MED 반영)
- crosswalk·supplement 항목마다: `member_input_ids`(원본 finding), `src_run_id`, `src_record_path`,
  `record_sha256_bytes`(+ 필요시 `_jcs`), `source_span_hash`, `decision`, `decided_by`, `decided_at`.
- 원본 불변성: canonical 승격 시 부모 hash **전건 재계산** 대조(해시 필드 신뢰 금지 — 적대검증 지적).

## 5. union view (검색 보조, canonical 아님)
- `base(Claude) + audit overlay` 동적 뷰. wiki_search 등 소비자에 "전 findings" 제공.
- ★canonical truth 와 명확히 구분 표기. 미확정 findings 를 결함으로 오인 못 하게.

## 6. 실행 순서 (미실행)
1. crosswalk 스키마·검증기(`verify_crosswalk.py`: 원본 finding 유실 0·처분 전건 부여) 신설.
2. **파일럿 = EFDC-000**(DETTMP 가 confirmed_delta 로, 나머지 겹침이 equivalent 로 분류되는지 검증).
3. shard별 crosswalk 에이전트(A/B 무작위·라벨제거).
4. confirmed_delta 원문 span 재확인 → supplement 승격.
5. WO amendment(supplement 게이트) → canonical 선택.
6. santa-method `/codex:review` 최종.

## 7. 폐기된 안
- 전량 union materialize(구 MERGE-PLAN) — precision 저하로 폐기.
- 구조필드 병합 — 정의 부족으로 폐기(필요시 `structural_delta_candidate` 로 별도).
