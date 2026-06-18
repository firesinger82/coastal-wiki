---
title: "표사이동 — 01 개념"
topic: sediment-transport
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference: textbook/md/590329085-Dynamics-of-Marine-Sands... (Soulsby 1997, 360 KB extracted with bedload/suspended/Shields/Rouse/ripple/dune/settling 항목 다수) + KHOA·PORTCALS glossary 113 표사·퇴적 용어."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 표사이동 — 01 개념

## 1. 정의

> **표사이동 (*sediment transport*)**: 흐름·파·중력 등에 의해 해저·하상·해변의 입자(모래·실트·점토)가 운반되는 현상. 침식·운반·퇴적 3 단계 포함.

영문: *sediment transport*, *sand transport*, *sediment dynamics*.

## 2. 운반 방식 — Bedload vs Suspended (Soulsby 1997)

### 2.1 두 방식 정의

| 한국어 | 영문 | 입자 운동 | 발생 조건 |
|---|---|---|---|
| **소류** | bedload | bed 인근 (≤ a few grain diameters) — saltation·rolling·sliding | 흐름 약함 ~ 중간 |
| **부유** | suspended load | 수괴 내부 (turbulence가 무게 균형) | 흐름 강함 |
| Wash load | wash load | 매우 미세 (turbulence가 항상 균형) | 미사·점토 |

→ 한국 KHOA: **소류사** (bedload sediment) / **부유사** (suspended sediment) / **연안표사** (littoral drift).

### 2.2 전이 — Suspension Threshold

부유 시작 조건: u_*/w_s > 1 (대략)
- u_* = friction velocity = √(τ_b/ρ)
- w_s = settling velocity

상세는 [`02-theory.md` §3](02-theory.md) Rouse profile.

## 3. 입자 분류 — 입도

### 3.1 Wentworth scale (광범위 통용)

| 분류 | 입경 (mm) | 분류 (한국) |
|---|---|---|
| Boulder | > 256 | 호박돌 |
| Cobble | 64-256 | 자갈 |
| Pebble | 4-64 | 자갈 |
| Granule | 2-4 | 잔자갈 |
| **Sand** | 0.0625-2 | **모래** (한국 연안 주류) |
| Silt | 0.0039-0.0625 | 실트 |
| Clay | < 0.0039 | 점토 |

### 3.2 Sand sub-classification

| 분류 | 입경 (mm) |
|---|---|
| Very coarse | 1-2 |
| Coarse | 0.5-1 |
| Medium | 0.25-0.5 |
| Fine | 0.125-0.25 |
| Very fine | 0.0625-0.125 |

### 3.3 KHOA 용어

| 한국어 | 영문 |
|---|---|
| 입도 | grain size |
| 입도분포 | grain size distribution |
| 입도분석 | grain size analysis |
| 입도곡선 | grain size curve (cumulative) |
| 저질 | sea-bed sediment / substrate |
| 저질조사 | sea-bed sediment survey |

→ 분석 방법은 [`03-analysis-methods.md` §1](03-analysis-methods.md).

## 4. Bed Forms (저면 형태) — Soulsby Ch.7 (Marine Sands)

흐름·파 강도에 따라 발달:

| 형태 | 한국어 | 영문 | 발생 조건 |
|---|---|---|---|
| Flat bed (no transport) | 평탄 (운동 없음) | flat bed (no motion) | θ < θ_cr |
| **Ripples** | 연흔 / 리플 | ripples | 약한 흐름, θ_cr < θ < ~0.5 |
| Megaripples | 대형 연흔 | megaripples | 중간 |
| **Dunes / Sandwaves** | 듄·모래파 | dunes / sandwaves | 강한 흐름 |
| Flat bed (sheet flow) | 평탄 (sheet flow) | upper-stage plane bed | 매우 강한 흐름, θ > 0.8 |
| Antidunes | 역사구 | antidunes | 임계 Froude 이상 (드뭄) |

### 4.1 Wave ripples (파 유발 연흔, Soulsby Ch.7 p.130)

- **대칭** (crest sharp, viewed from above 평행)
- 파장 λ_r ≈ 1-2 · A (A = orbital amplitude = U_w T/(2π))
- 높이 Δ_r ≈ 0.1-0.2 · λ_r
- Wash-out 조건: θ_ws > 0.8 또는 mobility ψ > 150
- 공식: Grant & Madsen (1982), Nielsen (1992), Mogridge et al. (1994) — Soulsby SC §7.3 (eq. 88-89)

### 4.2 Current ripples (흐름 유발 연흔)

- **비대칭** (gentle stoss + steep lee)
- 파장 λ ≈ 100-300 · d_50
- 높이 Δ ≈ λ/10-20

### 4.3 Sandwaves (모래파)

- 큰 규모: 파장 100-1000 m, 높이 1-10 m
- 한국 서해·신안 군도에 발달. 조류와 평행 (creast 직교)
- KHOA "모래파", Soulsby SC §7.2

## 5. 한국 연안 표사 패턴

### 5.1 해역별

| 해역 | 표사 활동 | 우세 메커니즘 |
|---|---|---|
| 서해 (황해) | 매우 강함 | 강한 조류 (`concepts/currents/` 인천 M₂ 40 cm/s) + 파 |
| 남해 | 중간 | 파 + 약한 조류 + 강한 너울 |
| 동해 | 파 우세 | 약한 조류 (M₂ ≈ 3 cm/s) + 너울 침식 (NE 폭풍) |
| 제주 | 파 우세 | 너울 + 태풍 |

### 5.2 한국 KHOA 표사 관련 용어 (113 entries 중 핵심)

| 한국어 | 한자/영문 | 분류 |
|---|---|---|
| 표사 / 유사 | 漂砂 / sediment | 일반 |
| **소류** | 掃流 / bedload | 운반 방식 |
| **소류사** | bedload sediment | 운반 방식 |
| **부유사** / 부유표사 / 부유토사 | suspended sediment | 운반 방식 |
| **연안표사** | littoral drift | 해변 따라 운반 (별도 토픽) |
| **연안표사 이동** | littoral drift transport | 동상 |
| 유사량 | sediment discharge (m³/s) | 정량 |
| 유사이송 | sediment transport | 일반 |
| 유사침전 | sediment settling | 침강 |
| 응집침강 | flocculation settling | 점착성 미세 |
| **연안침식** | coastal erosion | 침식 |
| **연안침식관리구역** | coastal erosion management zone | 한국 법정 구역 |
| 세굴 | scour | 구조물 인근 침식 |
| **이동한계수심** | limit depth of motion | (`02-theory.md` §5) |
| 모래이동 한계수심 | limit depth of sand motion | 동상 |
| 수심변화 한계수심 | limit depth of bathymetric change | morphodynamic depth |
| 연흔 | ripple | bed form |
| 모래파 | sandwave | bed form |
| 입도·입도곡선·입도분석·입도분포 | grain size·curve·analysis·distribution | 분석 |
| 저질·저질조사 | sea-bed substrate·survey | 분석 |
| 사석투입 | rock dumping | 인공 |
| 인공해빈 | artificial beach | 양빈 |
| 동계형 해빈 | winter-profile beach | 계절 침식 |
| 준설·준설선 | dredging·dredger | 인공 운반 |

## 6. 점착성 vs 비점착성

| 항목 | 비점착성 (non-cohesive) | 점착성 (cohesive) |
|---|---|---|
| 입경 | > 0.0625 mm (모래·자갈) | < 0.0039 mm (점토) |
| 분류 | discrete grain | aggregated floc |
| 침강 | Stokes·Soulsby (단일 입자) | flocculation + settling 함수 |
| 한국 위치 | 외해·해변 | 하구·항만 안쪽 ([KHOA] 응집침강) |

→ 본 토픽은 **비점착성 모래** 중심. 점착성은 별도 (`concepts/cohesive-sediment/` 또는 본 토픽 확장).

## 7. 모르포다이나믹 (Morphodynamics)

표사 운반 + 시간 누적 → 지형 변화. 한국 사례:
- 해변 단면 (Dean equilibrium profile, winter/summer)
- 사구 (dunes) 발달·소멸
- 항만 어구 매몰 (siltation)
- 사주 (longshore bar) 이동
- 연안표사 평형 (longshore sediment transport, 별도 토픽 `concepts/littoral-drift/`)

EFDC·Delft3D·XBeach는 hydrodynamic + sediment + morpho 결합 시뮬 지원.

## 8. 보강·미해결

- Van Rijn (1993) 본문 OCR — formula 정밀화
- Mechanics of Sediment Transport 본문 발췌 (2 MB extracted, 구조 식별 필요)
- EFDC 표사이동 모듈 (`efdc-sed-trans-2003`) 발췌 → `models/EFDC/source-analysis/sediment.md`
- 응집침강 (cohesive) 별도 노트
- 한국 적용 사례는 바이블 검증(객관 데이터) 후 experience/ 에 카테고리화 — 본 canonical 미수록 (citation_status: source-needed)

## 9. 연결

- `02-theory.md` — Shields·Rouse·침강
- `03-analysis-methods.md` — 입도·관측·formula
- `04-code-and-tools.md` — EFDC SED 등 모델
- `05-examples.md` — 서해 사례 등 (객관 데이터 기반)
- `06-model-application.md` — 모델 적용 워크플로
- `concepts/waves/02-theory.md` §6.6 — radiation stress (longshore drift 원인)
- `concepts/currents/02-theory.md` — 조류 비대칭 (창·낙조류)
- `concepts/littoral-drift/` (미작성) — 연안표사 단독 토픽
- 외부:
  - **Soulsby (1997)** *Dynamics of Marine Sands* — 본 토픽 1차 reference
  - **Van Rijn (1993)** *Principles of Sediment Transport* — 클래식
  - Wentworth (1922) — 입도 분류
  - Shields (1936) — 임계 전단응력
  - Rouse (1937) — 부유 profile
