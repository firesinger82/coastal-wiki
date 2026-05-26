---
title: "ROMS 공식 자료 — myroms.org·GitHub·핵심 논문 (Shchepetkin & McWilliams 2005 등) 큐레이션"
topic: roms-web-refs
canonical_source: self
citation_status: verified
verification_method: "myroms.org 공식 도메인 + GitHub 공개 repo (myroms/roms, myroms/roms-jedi). License_ROMS.md (MIT) 본 위키 raw/source_code/roms/. 핵심 논문 인용은 publicly-known canonical works (Shchepetkin & McWilliams 2005, Haidvogel 2008, Warner 2008 CSTMS)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — URL + 공인 논문 인용"
verification_date: 2026-05-24
related:
  - models/ROMS/README.md
---

# ROMS 공식 자료 큐레이션

> [`models/ROMS/README.md`](../README.md) 의 정체 카드 외부 references 확장.

## 1. 공식 사이트

| 자원 | URL | 활용 |
|---|---|---|
| **myroms.org** | [https://www.myroms.org/](https://www.myroms.org/) | 공식 홈 — Rutgers + UCLA |
| **myroms Wiki** | [www.myroms.org/wiki/](https://www.myroms.org/wiki/) | 공식 documentation hub |
| **myroms Forum** | [www.myroms.org/forum/](https://www.myroms.org/forum/) | 사용자 커뮤니티 (가장 활발) |

본 위키 — `raw/manuals/wiki/` 에 1161 wiki HTML mirror.

## 2. Code repository

| Repo | 역할 |
|---|---|
| **myroms/roms** | [github.com/myroms/roms](https://github.com/myroms/roms) | Fortran core (Rutgers ROMS) |
| **myroms/roms-jedi** | [github.com/myroms/roms-jedi](https://github.com/myroms/roms-jedi) | JEDI 데이터 동화 통합 |
| **ECCO-style ROMS** | 본 위키 `raw/source_code/roms_eccofs/` | ECCO 동화 |
| **ROMS libs** | `raw/source_code/roms_libs/` | 공통 라이브러리 |
| **ROMS MATLAB toolbox** | `raw/source_code/roms_matlab/` | 후처리 (Rutgers Hernan Arango) |
| **ROMS Test Cases** | `raw/source_code/roms_test/` | 표준 테스트 케이스 |

## 3. 핵심 논문 — 시초부터 현재까지

### 3.1 Foundation (1990s-2005) — Rutgers + UCLA

- **Shchepetkin, A.F., McWilliams, J.C. (2005)** "The regional oceanic modeling system (ROMS): a split-explicit, free-surface, topography-following-coordinate oceanic model" *Ocean Modelling* 9(4):347-404 — **ROMS 시초 시스템 paper**
- **Shchepetkin, A.F., McWilliams, J.C. (2003)** "A method for computing horizontal pressure-gradient force in an oceanic model with a nonaligned vertical coordinate" *J. Geophys. Res. Oceans* 108(C3):3090 — pressure gradient
- **Shchepetkin, A.F., McWilliams, J.C. (1998)** "Quasi-monotone advection schemes based on explicit locally adaptive dissipation" *Monthly Weather Review* 126:1541-1580 — advection scheme

### 3.2 Skill assessment

- **Haidvogel, D.B., Arango, H., Budgell, W.P., Cornuelle, B.D., Curchitser, E., Di Lorenzo, E., et al. (2008)** "Ocean forecasting in terrain-following coordinates: Formulation and skill assessment of the Regional Ocean Modeling System" *J. Comput. Phys.* 227(7):3595-3624 — operational forecasting

### 3.3 Sediment — CSTMS

- **Warner, J.C., Sherwood, C.R., Signell, R.P., Harris, C.K., Arango, H.G. (2008)** "Development of a three-dimensional, regional, coupled wave, current, and sediment-transport model" *Computers & Geosciences* 34(10):1284-1306 — **CSTMS 통합 시초**

### 3.4 Vertical mixing

- **Large, W.G., McWilliams, J.C., Doney, S.C. (1994)** "Oceanic vertical mixing: A review and a model with a nonlocal boundary layer parameterization" *Reviews of Geophysics* 32(4):363-403 — KPP scheme
- **Mellor, G.L., Yamada, T. (1982)** "Development of a turbulence closure model for geophysical fluid problems" *Reviews of Geophysics* 20(4):851-875 — MY2.5

### 3.5 Coupled / 한국 동해

- **WRF + ROMS coupling** — 본 위키 `raw/source_code/WRF/` 참조
- **KOOS-EJS (NIFS 동해예측시스템)** — 한국 국립수산과학원 동해 ROMS 운영 시스템 (별도 한국 paper 큐레이션 필요)

## 4. 핵심 모듈

| 모듈 | 활용 | 본 위키 cross-ref |
|---|---|---|
| **split-explicit time-stepping** | 2D barotropic + 3D baroclinic 분리 | (예정) source-analysis 보강 |
| **K-profile (KPP)** | vertical mixing | Large 1994 |
| **Mellor-Yamada 2.5** | vertical mixing | Mellor & Yamada 1982 |
| **4DVAR / ROMS-JEDI** | 데이터 동화 | `raw/source_code/roms-jedi/` |
| **CSTMS** | sediment-wave-current coupling | Warner 2008 |
| **Biogeochemistry** | nutrient·plankton·oxygen | NPZD·BEC 등 옵션 |

## 5. 한국 적용

- **NIFS KOOS-EJS** — 국립수산과학원 동해예측시스템 (ROMS 기반)
- 본 위키 — [[../../../experience/nifs-vertical-sst-trends]] (NIFS 다층 수온 trend 활용, ROMS forcing source)
- [`concepts/sst/06-model-application.md`](../../../concepts/sst/06-model-application.md) — ROMS 해수온 모듈 + 한국 동해 적용

## 6. 운영 자원

| 자원 | 비고 |
|---|---|
| **myroms Forum** | 가장 활발한 사용자 Q&A (Arango 직접 응답) |
| **WikiROMS** | 공식 wiki — Getting Started, CPP options, Vertical Mixing 등 |
| **MyROMS Tutorial** | 표준 테스트 케이스 walkthrough |
| **ESMF coupling** | Earth System Modeling Framework — WRF coupling 표준 |
| **PyROMS / ROMSTOOLS** | Python·MATLAB 전·후처리 도구 (커뮤니티) |

## 7. 본 위키 내 cross-ref

- [`concepts/sst/06-model-application.md`](../../../concepts/sst/06-model-application.md) — ROMS SST module
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — ROMS-CSTMS sediment
- [`concepts/currents/`](../../../concepts/currents/) — baroclinic regional current modeling
- [[../../../experience/nifs-vertical-sst-trends]] — NIFS 다층 수온 + ROMS forcing 정합성
- [`models/ROMS/source-analysis/`](../source-analysis/) — 11 verified 노트 (sparse, M-D 보강 후보)
- [`models/ROMS/source-analysis/roms_atmospheric_forcing.md`](../source-analysis/roms_atmospheric_forcing.md) — 대기 forcing 일반론 (a9618df promote)

## 8. Recent updates (citation_status: source-needed)

W22 Hermes ingest (2026-05-25) 발견 항목 — promote 시 PR/issue 본문 발췌 그대로 인용. 본 §의 verified 승격은 코드 변경 직접 확인 후.

### 8.1 PR #75 — MULTI_SCALE_B 4D-Var background error operator (2026-05-22)

- 출처: [github.com/myroms/roms/pull/75](https://github.com/myroms/roms/pull/75) (github PR)
- 요약 (PR description 발췌): "This PR implements a multi-scale background error covariance (**B**) operator into **ROMS 4D-Var**. It is based on the formulation of Weaver et al. (2013, 2016, 2018). It is activated with the **`MULTI_SCALE_B`** option. The new formulation uses a normalized implicit diffusion ope[rator...]"
- 새 CPP option: `MULTI_SCALE_B` (4D-Var background error covariance 다중 스케일 분해).
- 이론 출처: Weaver et al. (2013, 2016, 2018) — multi-scale B 의 분해 공식. ROMS 4D-Var (Moore et al. 2011 IS4DVAR) 의 standard B 를 다중 스케일 분해로 확장.
- **인용 검증 TODO**: Weaver 2013/2016/2018 인용 정확화 (저널·DOI) + PR 의 변경 파일 (4dvar driver, B operator routine) 직접 확인 후 source-analysis/4dvar/ 노트에 cross-ref 추가. 다중 스케일 B 의 한국 동해 NIFS KOOS-EJS (`../../../experience/nifs-vertical-sst-trends`) 적용 가능성 평가.
