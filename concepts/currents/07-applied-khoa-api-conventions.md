---
title: "KHOA 조류 자료의 명세에 없는 규약 — 성분·시각·유향·16방위 (실측 대조로 정한 사용 계약)"
topic: currents
layer: 4
depends_on:
  - concepts/currents/03-analysis-methods.md
  - concepts/currents/04-code-and-tools.md
  - experience/khoa-tidal-current-phase-reference-2026.md
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "④ 응용 노트(CONVENTIONS §8.1). KHOA 조류 자료(수치조류도 조화상수 CSV·바다누리 tidalCurrentArea·data.go.kr 조류예보 API)의 공식 명세에 적혀 있지 않은 규약을 실측 대조로 정한 결과를 사용 계약으로 정리한다. 근거는 ③[[03-analysis-methods]](KHOA 위상 표준 g=동경135°)·③[[04-code-and-tools]](자료 목록·명세 인용)와 experience 커밋고정 링크 1종이며, **대조 수치는 experience 노트에 두고 본문에 복제하지 않는다**. 인용 고정점 = `experience/khoa-tidal-current-phase-reference-2026.md` @ `20bc544`. 수치 자체의 검증 책임은 그 노트(3조건 통과·verified)에 있다. **한계**: 공식 명세가 아니라 특정 시기·지점의 대조 결과다. KHOA 가 명세를 공개하거나 제품을 바꾸면 이 계약은 다시 확인해야 한다(§5)."
note_author: "Claude Opus 5.5"
note_date: 2026-09-30
related:
  - concepts/currents/04-code-and-tools.md
  - concepts/currents/05-examples.md
  - concepts/tides/07-applied-record-length.md
---

# KHOA 조류 자료의 명세에 없는 규약

> [[04-code-and-tools]] 는 KHOA 조류 자료를 명세대로 소개한다. 그런데 명세는 **어느 성분인지, 시각이 어느 시간대인지,
> 유향이 흐르는 방향인지 오는 방향인지, 16방위를 어떻게 도로 바꾸는지** 적지 않는다. 틀리게 가정하면 모델 검증에서
> 위상이 반 주기 어긋나거나 벡터가 뒤집혀도 겉으로는 드러나지 않는다.
> 이 노트는 실측 대조로 정한 규약을 **사용 계약**으로 적는다. 대조 방법과 수치는 아래 experience 노트에 있다.

## 0. 근거의 위치

- 대조 방법·수치·재현 절차: [`experience/khoa-tidal-current-phase-reference-2026.md`](../../experience/khoa-tidal-current-phase-reference-2026.md) @ `20bc544`
- 명세 인용과 자료 목록: [[04-code-and-tools]] §2·§3
- KHOA 위상 표준(지각 g = 동경 135° 기준): [[03-analysis-methods]] §1.3

## 1. 수치조류도 조화상수 CSV 는 남북(v) 성분 하나다

- **명세**: CSV 헤더는 `m2_진폭`·`m2_지각` 뿐이고, data.go.kr 컬럼 설명은 "조화상수의 진폭정보" 라고만 한다.
- **계약**: (진폭, 지각) 쌍은 **남북(v) 유속 성분**이다. 동서 성분은 공개 CSV 에 없다. 근거: experience §3b (같은 격자의 KHOA 예측 유속 아카이브와 분산·시계열 대조).
- **따라서**: 이 CSV 로 조류 벡터·타원을 재구성할 수 없고, 모델 검증은 모델의 v 성분과만 비교한다.
- **단위**: 포털 메타데이터에 없다. 예측 유속과의 대조로 cm/s 와 정합한다(experience §3b).

## 2. 위상은 g(동경 135°), API 시각은 KST, 유향은 흐르는 방향

- **위상 기준**: CSV·포털 모두 미기재. KHOA 공식 표준([[03-analysis-methods]] §1.3)대로 **g(135°E)** 로 읽는다. 조위 위상과의 교차 대역 대조가 이를 뒷받침한다(experience §3).
- **API 시각**: 바다누리 `tidalCurrentArea` 의 `Date`·`Hour` 는 **KST** 다(experience §3c — CSV 합성값과 시각 지정 대조).
- **유향**: **흐르는 방향, 진북 기준 시계방향**이다(experience §3c). 반대 규약이면 대조 상관의 부호가 뒤집힌다. 백서 2025 도 "유향은 진북을 기준으로" 라고만 적는다.
- 두 대조는 서로 묶여 있다: 시각 검정만으로는 "CSV=g·API=KST" 와 "CSV=G·API=UTC" 를 가를 수 없고, 조위 대조가 CSV=g 를 정해 API=KST 가 따라 나온다(experience §3c).

## 3. 조류예보 API 의 16방위 유향

- **명세**: data.go.kr `crntFcstTime`(15156024)은 유향을 16방위 문자로 준다. 도 변환 규칙은 적지 않는다.
- **계약**: 한국식 이름(동·서가 앞: `동북동`·`동남동`·`서남서`·`서북서`)의 16방위이며, **가장 가까운 22.5° 구간으로 반올림한 흐르는 방향**이다(`북` = 0°, 시계방향). 변환표는 [[04-code-and-tools]] §3. 근거: experience §3d (숫자 유향을 주는 최강창낙조 API 와 같은 시각 대조, 규약이 확인된 수치조류도 API 와 대조).
- **따라서**: 변환 뒤 유향에는 구간 폭만큼의 양자화 오차가 남는다. 모델 유향과 비교할 때 이보다 작은 차이는 판별할 수 없고, 유속과 함께 벡터로 바꾸면 그 오차가 성분에 들어간다. 크기는 experience §3d.

## 4. 인용 계약

KHOA 조류 자료를 모델 검증에 쓸 때 다음을 함께 적는다.

1. 어떤 제품인가 — 수치조류도 조화상수 CSV / 바다누리 API / 조류예보 API (예보지점 기반, 수치조류도 격자 아님).
2. 성분 — CSV 는 v 만.
3. 위상 기준(g)과 시각대(KST) — 모델 쪽 UTC·G 와 변환했는지.
4. 유향 규약(흐르는 방향)과 16방위 양자화 여부.
5. 이 노트의 근거 커밋(`20bc544`) — 명세가 공개되거나 바뀌면 다시 확인한다.

## 5. 한계

- 공식 명세가 아니다. 대조는 특정 시기·지점·표본 간격에서 했다(규모는 experience §2·§3b–3d).
- 동해 연안은 수치조류도 격자 밖이라 §1–2 대조에 들어가지 않았다(experience §5).
- KHOA 문서에서 성분·시각대·유향 규약을 명시한 원문이 나오면 그것으로 대체한다 (source-needed).
