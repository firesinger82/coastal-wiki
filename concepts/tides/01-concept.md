---
title: "조석 — 01 개념"
topic: tides
canonical_source: self
citation_status: draft-unsourced
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: ""
verification_date: ""
---

# 조석 — 01 개념

## 정의

조석(tide)은 **달의 만유인력(주효과)과 태양의 인력(부효과)에 의한 해양·대형 수괴 해수면의 규칙적·교대적 상승과 하강**.

> "Alternate and regular rise and fall of sea level in oceans and other large bodies of water. These changes are caused by the gravitational attraction of the moon and, to a lesser extent, of the sun on the earth." — (lubbad2009-tides-slides, p.8)

핵심 속성:
- **규칙적 (regular)**: 천체 운동에 종속되어 예측 가능한 주기 구조
- **교대적 (alternate)**: 상승(flood)과 하강(ebb)이 반복
- **천문 기원**: 달이 주효과, 태양은 부효과 (질량 차이는 크지만 거리가 훨씬 가까운 달이 우세)

## 맥락

### 더 큰 도메인 — 해수면 변동의 분류

조석은 [수위 변동(water level fluctuation)](../../textbook/notes/tides-lubbad2009-overview.md#슬라이드-구조)의 한 종류. 시간 척도별 분류 (lubbad2009-tides-slides, p.6):

| 척도 | 종류 |
|---|---|
| 단기 (Short term) | **조석**, 기압 변동, 폭풍해일(storm surge), seiche |
| 계절 (Seasonal) | 계절적 기후 변동 |
| 장기 (Long term) | Isostatic, 지구 기후 변화 (해수면 상승) |

조석은 단기 척도이며 **천문 기원**이라는 점에서 다른 단기 변동(기상 기원: 폭풍해일, seiche)과 구별.

### 왜 중요한가

- **해안 구조물 설계**: 만조 시 파랑 + 월파 + 침수 평가의 기준
- **해안 침식**: 사빈에서 조위에 따라 작은 파에서도 침식이 진행
- **항만 운영**: 흘수 제약, 갑문 운용
- **수치모델 forcing**: 연안·하구 모델(EFDC, ADCIRC 등)의 경계 조건

(객관적 사례·메커니즘은 출처 인용 보강 후 추가)

## 핵심 용어

(lubbad2009-tides-slides, p.9-12)

| 용어 (한) | 영문 | 정의 |
|---|---|---|
| 기준면 | Datum | 조위 측정의 기준 평면. 통상 거의 모든 조위가 그 이상이 되도록 설정 |
| 만조 상승 | Rise | 채택 척도에서 만조의 높이 (기준면 기준) |
| 조차 | Range | 만조와 이어지는 (또는 직전) 간조 사이의 수위 차 |
| 조류 | Tidal currents | 조석에 의한 수평 흐름 |
| 창조류 | Flood current | 상승 수위에 동반되는 조류 |
| 낙조류 | Ebb current | 하강 수위에 동반되는 조류 |
| 조석파 | Tidal wave | 가장 긴 해양파. 수시간 주기의 수위 진동 |

**주의**: 창조류 ≠ 낙조류 (방향·세기 비대칭이 일반적). 비대칭은 표사 이동과 직접 연결됨 — `concepts/sediment-transport/` 작성 시 연결.

### 추가 용어 (개념 단계에 필요한 최소)

- **태양일 (solar day)**: 24 h — 태양이 동일 자오선에 두 번 올 때까지
- **태음일 (lunar day)**: **24 h 50 min** — 달이 동일 자오선에 두 번 올 때까지. 만조 시각이 매일 약 50분씩 늦어지는 직접 원인 (lubbad2009-tides-slides, p.19-20)
- **반일주조 (semidiurnal)**: 하루에 만조·간조가 두 번씩 발생하는 조석 형태 (주성분 주기 약 12.42 h)
- **일주조 (diurnal)**: 하루에 만조·간조가 한 번씩
- **혼합조 (mixed)**: 반일주조 + 일주조 성분이 비슷한 크기로 공존

## 전형 조차

(lubbad2009-tides-slides, p.13)

| 위치 유형 | 조차 |
|---|---|
| 외해 (open ocean) | 약 0.6 m |
| 연안 | 2 – 3 m |
| 최대 (Bay of Fundy, Canada) | 12 m |

> **검증 노트**: 12 m는 슬라이드의 명시값. 실제 Bay of Fundy 최대 조차는 약 16 m 보고도 있음 (Burntcoat Head). 슬라이드 값 인용 시 위 표 그대로 사용하되, 정밀 인용 필요 시 별도 출처(예: 캐나다 해양수산부 자료) 확보 필요. → **사용자 verify 시 확인 항목**

## 한국 연안 맥락

(한국 동·서·남해의 조차 차이 등 객관 자료는 보강 필요 — 현재 source-needed)

## 미해결·보강 예정

- `02-theory.md`로 이전될 항목: 조석 생성력, 평형조석, Laplace 방정식
- 진폭·위상의 amphidromic system 형성 메커니즘 (해저지형·코리올리·마찰)
- 분조(harmonic constituents) 상세는 `03-analysis-methods.md`
- 한국 연안 조차 분포 (서해 ≈ 6-9 m, 남해 ≈ 1-3 m, 동해 ≈ 0.2-0.4 m) — 출처 확보 후 추가

## 연결

- **다음 단계 문서** (미작성):
  - `02-theory.md` — 생성력·평형조석 (`stewart-physical-ocean` 보강 시)
  - `03-analysis-methods.md` — 조화 분해 (`tidal-heights-manual` 활용)
- **소스 노트**:
  - [`textbook/notes/tides-lubbad2009-overview.md`](../../textbook/notes/tides-lubbad2009-overview.md) — 전체 슬라이드 발췌 개관
- **상위 정책**:
  - [`CONVENTIONS.md`](../../CONVENTIONS.md) — frontmatter, citation_status
  - [`textbook/POLICY.md`](../../textbook/POLICY.md) — 출처 인용 규칙

## verified 승격 체크리스트 (사용자 작업)

이 문서가 `verified`로 가려면:
- [ ] §정의의 인용문 페이지(p.8) 원문 대조
- [ ] §핵심 용어 표의 7개 정의 페이지 대조 (p.9-12)
- [ ] §전형 조차 12 m 값 검증 (필요시 추가 출처)
- [ ] §추가 용어 중 슬라이드에 없는 항목(반일주조/일주조/혼합조)에 별도 출처 부착
- [ ] frontmatter `citation_status: verified`, `verification_by`, `verification_date` 갱신
