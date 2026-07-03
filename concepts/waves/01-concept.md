---
title: "파랑 — 01 개념"
topic: waves
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "AI cross-reference: textbook/md/Waves-Holthuijsen2007.md (Ch.1-3 TOC + key concepts) + KHOA·PORTCALS glossary (284 wave-related terms) + 해양수산부(MOF)/KHOA 공식 관측망 MPT station structure (source-needed)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 파랑 — 01 개념

## 1. 정의

> **파랑 (波浪, *waves*)**: 바람·중력·천체 인력 등에 의해 해수면이 일으키는 진동성 운동. 광범위한 시간 척도와 메커니즘 포함. ([KHOA] 파랑 — 별도 cross-check 필요)

영문: *waves* (일반), *ocean waves* / *sea waves* / *water waves*.

본 토픽은 **풍파(wind-generated) + 너울(swell) 중심**. 조석파(`concepts/tides/`)·쓰나미·내부파 등은 별도.

## 2. 시간 척도별 분류 (Holthuijsen 2007 §1.3 — 일반 통설)

`tides-lubbad2009-overview.md` §1과 호환:

| 주기 | 종류 | 메커니즘 |
|---|---|---|
| ~0.1 s | 표면 장력파 (capillary) | 표면 장력 (Holthuijsen §5.4.4) |
| 0.1 ~ 1 s | 단주기 중력파 | 중력 (gravity-dominant 천이) |
| **1 ~ 30 s** | **풍파·너울 (wind sea, swell)** | 바람 → 중력 회복 (본 토픽 중심) |
| 수십 ~ 수백 s | 인프라그라비티파 (long waves) | 풍파의 비선형 상호작용 + 천해 변형 |
| ~분 ~ 시간 | 쓰나미·seiche | 충격성 변위 (지진·해저 산사태·기상) |
| 12-24 h | 조석 | 천체 인력 (`concepts/tides/`) |

## 3. 풍파의 발달 단계

(Holthuijsen Ch.6 §6.3-6.4)

1. **풍파 생성** (S_in): 바람이 해면에 운동량 전달 (Phillips 1957 mechanism + Miles 1957 shear instability)
2. **분산·전파**: 긴 파장 성분이 더 빠르게 전파 → 풍역 밖에서 너울로 분리
3. **비선형 상호작용** (S_nl4): quadruplet wave–wave interaction → 에너지 재분포
4. **쇄파 소산** (S_ds): white-capping (deep water) + bottom friction + depth-induced surf-breaking (천해)

## 4. 풍파 vs 너울 (KHOA 통설)

| 항목 | 풍파 (wind sea) | 너울 (swell) |
|---|---|---|
| 발생 | 풍역 내, 진행 중인 바람 | 풍역 밖, 바람과 분리 |
| 주기 | 짧음 (3-12 s) | 길음 (8-20 s) |
| 파형 | 불규칙, 가파름 | 규칙적, 부드러움 |
| 분산 | 광대역 | 협대역 (저주파 우세) |
| 출처 | 현지 바람 | 원거리 바람 (수천 km) |

연안에서는 두 성분이 공존 → 스펙트럼이 multi-peak 형태일 수 있음 ([Holthuijsen §3.5.7](../../textbook/notes/waves-holthuijsen-toc.md)).

## 5. 파라미터 (단일 파)

### 5.1 기본 (Holthuijsen Ch.3 §3.3, KHOA)

| 기호 | 한국어 | 영문 | 정의 |
|---|---|---|---|
| H | 파고 | wave height | crest와 직전 trough 사이 수직 거리 |
| **T** | 주기 | wave period | 두 zero-up-crossing 사이 시간 |
| L (λ) | 파장 | wavelength | 두 인접 crest 사이 수평 거리 |
| a | 진폭 | amplitude | 평균 해면에서 crest까지 (H/2 for sinusoidal) |
| f = 1/T | 주파수 | frequency | Hz |
| ω = 2π/T | 각주파수 | angular frequency | rad/s |
| k = 2π/L | 파수 | wavenumber | rad/m |
| H/L | 파형도 | steepness | 무차원 |
| h | 수심 | water depth | m |

### 5.2 심해 vs 천해 구분 (Holthuijsen §5.4.3)

분산 관계 `ω² = gk·tanh(kh)`로부터:

| 영역 | 조건 | 분산 식 |
|---|---|---|
| **심해파 (deep water)** | h/L > 1/2 (kh > π) | ω² = gk (즉 L = gT²/2π) |
| **천이파 (transitional)** | 1/20 < h/L < 1/2 | full ω² = gk·tanh(kh) |
| **천해파 (shallow water)** | h/L < 1/20 (kh < π/10) | ω² = ghk² (즉 c = √(gh)) |

→ 한국 서해 (수심 30-100 m, 풍파 T ≈ 5-10 s, L ≈ 40-160 m): 대부분 천이~천해 영역.

## 6. 통계 파라미터 (불규칙 파)

### 6.1 H 계열 (Holthuijsen §4.2, KHOA glossary)

| 한국어 | 영문 | 정의 |
|---|---|---|
| **유의파고** | **significant wave height** (H_s, H_{1/3}) | 1/3 highest waves의 평균 파고 — 인지값과 가장 가까움 |
| 최대파고 | max wave height (H_max) | 관측 기간 최대 |
| 평균파고 | mean wave height (H_mean) | 산술 평균 |
| 십분의일 최대파 | one-tenth highest wave (H_{1/10}) | 1/10 highest waves의 평균 |
| 1/100 최대파 | one-hundredth highest (H_{1/100}) | 1/100 highest |
| H_rms | RMS wave height | √(평균 H²) |

스펙트럼 기반:
- **H_{m0}**: 4√m₀ (m₀ = 스펙트럼 0차 모먼트). 협대역 풍파에선 H_s ≈ H_{m0}
- T_{m02}: √(m₀/m₂) zero-crossing 평균 주기
- T_p: peak period (스펙트럼 최대값의 주기)
- T_{m01}: m₀/m₁

### 6.2 H 분포

해상에서 파고는 Rayleigh 분포 근사 (협대역, deep water 가정):
```
P(H > h) = exp(-2h²/H_s²)
```
극단치는 Weibull / Forristall 보정 (Holthuijsen §4.2.4).

## 7. 관측 기법 (Holthuijsen Ch.2 + KHOA)

### 7.1 In-situ (Ch.2 §2.3)

| 기법 | KHOA 명칭 | 출력 |
|---|---|---|
| Wave buoy | **부이식 파고계** | (η(t), u, v) 시계열 → 1D/2D spectrum |
| Wave pole | **수압식·기계식 파고계** | η(t) 시계열 |
| Pressure transducer | 수압식 | 압력 → 수심 보정 → η |
| ADCP (waves mode) | ADCP 파랑 모드 | 표면 부근 orbital velocity → 파라미터 |

### 7.2 Remote sensing (Ch.2 §2.4)

- **Stereo-photography**
- **Imaging radar** (X-band, marine radar)
- **Altimetry** (laser·acoustic·radar) — H_s 직접 추정

### 7.3 한국 MPT 정점 (해양수산부 MOF·KHOA 공식 관측망 / mof_data 74 정점, source-needed)

| 기관 | 정점 수 | 비고 |
|---|---|---|
| 해양수산부 (MOF) | 34 | MPT2xx 코드 |
| 기상청 (KMA) | 29 | MPT1xx 코드 |
| 국립해양조사원 (KHOA) | 11 | MPT 추가 + 외해 buoy |

해역 분포: 서해 19, 남해 23, 동해 32 (총 74).

→ 정점별 데이터·예제는 `05-examples.md`.

## 8. 한국 KHOA 용어 (284 wave terms 중 핵심)

| 한국어 | 한자/영문 | 의미 |
|---|---|---|
| **유의파** | (significant wave) | H_s = H_{1/3} |
| **설계파** | design wave | 구조물 설계 기준 (재현기간 50/100년 등) |
| **설계파고** | design wave height | 위와 동일 의미 |
| **불규칙파** | irregular wave | 실해상 파 |
| **규칙파** | regular / monochromatic / periodic wave | 단일 주기 정현파 |
| **선형파** | linear wave | 미소진폭 가정 |
| **비선형파** | nonlinear wave | Stokes·cnoidal·solitary 등 |
| **굴절** | refraction | 수심 변화에 따른 진행방향 변화 |
| **회절** | diffraction | 장애물 우회 |
| **반사** | reflection | 구조물·해벽 반사 |
| **천수** | shoaling | 수심 감소 시 진폭 증가 |
| **쇄파** | breaker / breaking wave | 파의 무너짐 |
| **쇄파대** | breaker zone / surf zone | 쇄파 발생 영역 |
| **권파/붕파/쇄기파** | plunging / spilling / collapsing breaker | 쇄파 type (별도 detail) |
| **방파제** | breakwater | (구조물, `concepts/coastal-structures/`) |
| **소파공/소파블록/소파호안** | wave-dissipating structure | 쇄파 유도 구조물 |
| **고립파** | solitary wave | 단일 비분산파 (tidal bore·tsunami) |
| **스톡스파** | Stokes wave | 유한 진폭 비선형 정상파 |
| **내부파** | internal wave | 밀도 성층 매질 내부 (≠ surface wave) |
| **월파** | wave overtopping | 파가 구조물 마루를 넘어 침입 |
| **월파량** | overtopping discharge | (m³/m/s) |

상세는 `02-theory.md` 이후 인용 시 (KHOA) 표시.

## 9. 보강·미해결

- 천이파의 분산 관계 수치 풀이 알고리즘 (Newton-Raphson)
- H_{m0} ≈ H_{1/3} 정합 조건 (협대역·풍파 한정)
- 비선형 파 (Stokes 2-5차)의 적용 범위
- 한국 서해·남해·동해 typical 풍파 통계 (DASHBOARD MPT 데이터로 정량)
- Hudspeth 2005 *Waves and Wave Forces* — 구조물 적용 별도 정리

## 10. 연결

- `02-theory.md` — linear wave theory·분산 관계·energy
- `03-analysis-methods.md` — 스펙트럼·통계 분석
- `04-code-and-tools.md` — SWAN·WAVEWATCH III·XBeach
- `05-examples.md` — 한국 MPT 정점 실제 데이터
- `06-model-application.md` — SWAN canonical (`models/SWAN/`)
- 소스 노트:
  - [`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md) — Holthuijsen 2007 TOC (verified)
  - `khoa-portcals-glossary` — 284 파랑 용어
  - 해양수산부(MOF)·KHOA 공식 관측망 — MPT 74 정점 메타데이터 (source-needed)
