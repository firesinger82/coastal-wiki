---
title: "ADCIRC 공식 자료 — 사이트·GitHub·핵심 논문·커뮤니티 큐레이션"
topic: adcirc-web-refs
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "공식 도메인 (adcirc.org, adcirc.github.io) WebFetch sampling 2026-05-24 — theory/index.html + parameter_definitions/index.html 본 위키 [[../manual-notes/03-theory-and-formulation]] + [[../manual-notes/06-parameter-definitions]] 작성 시 검증 완료. GitHub URL 은 공개 repo (github.com/adcirc/adcirc, adcirc-testsuite, adcircpy 등). 논문 인용은 publicly-known canonical works."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — URL audit + 공인 논문 인용"
verification_date: 2026-05-24
related:
  - models/ADCIRC/README.md
---

# ADCIRC 공식 자료 큐레이션

> [`models/ADCIRC/README.md`](../README.md) 의 정체 카드 외부 references 확장.

## 1. 공식 사이트

| 자원 | URL | 활용 |
|---|---|---|
| **adcirc.org** | [https://adcirc.org/](https://adcirc.org/) | 공식 홈, 운영 안내, FAQ |
| **adcirc.github.io 공식 docs** | [https://adcirc.github.io/adcirc/](https://adcirc.github.io/adcirc/) | 최신 docs hub (Theory·Input·Examples·Tools) |
| Documentation hub | [adcirc.github.io/adcirc/](https://adcirc.github.io/adcirc/) | [[../manual-notes/01-docs-hub]] |
| FAQ | [adcirc.org/home/adcirc-faq](https://adcirc.org/home/adcirc-faq/) | [[../manual-notes/09-support-and-faq]] |

## 2. Code repositories (GitHub)

| Repo | 역할 |
|---|---|
| [adcirc/adcirc](https://github.com/adcirc/adcirc) | Fortran core (메인) |
| [adcirc/adcirc-testsuite](https://github.com/adcirc/adcirc-testsuite) | 표준 테스트 케이스 (Katrina·Shinnecock 등) |
| [adcirc/adcircpy](https://github.com/**oceanmodeling**/adcircpy (★구 adcirc/adcircpy 는 404, 2026-07-19 확인)) (or [oceanmodeling/adcircpy](https://github.com/oceanmodeling/adcircpy)) | Python wrapper |
| [adcirc/gahm](https://github.com/adcirc/gahm) | Generalized Asymmetric Holland Model (vortex) |
| [StormSurgeLive/asgs](https://github.com/StormSurgeLive/asgs) | ADCIRC Surge Guidance System (운영 forecast) |
| [CHLNDDEV/OceanMesh2D](https://github.com/CHLNDDEV/OceanMesh2D) | MATLAB mesh generator ([[../manual-notes/27-github-oceanmesh2d-repo-review]]) |
| [CHLNDDEV/oceanmesh](https://github.com/CHLNDDEV/oceanmesh) | Python mesh generator ([[../manual-notes/28-github-oceanmesh-python-repo-review]]) |
| [noaa-ocs-modeling/OCSMesh](https://github.com/noaa-ocs-modeling/OCSMesh) | NOAA OCS Mesh tool ([[../manual-notes/29-github-ocsmesh-repo-review]]) |

## 3. 핵심 논문 — 시초부터 현재까지

### 3.1 Foundation (1991-1994)

- **Luettich, R.A., Westerink, J.J., Scheffner, N.W. (1992)** "ADCIRC: an advanced three-dimensional circulation model for shelves, coasts, and estuaries; report 1: theory and methodology of ADCIRC-2DDI and ADCIRC-3DL" *U.S. Army Corps of Engineers Tech Report DRP-92-6, Vicksburg MS*
- **Luettich, R.A., Westerink, J.J. (1991)** "A solution for the vertical variation of stress, rather than velocity, in a three-dimensional circulation model" *Int. J. Numer. Methods Fluids* 12:911-928 — 3DVS 형성
- **Westerink, J.J., Luettich, R.A., Baptists, A.M., Scheffner, N.W., Farrar, P. (1992)** "Tide and Storm Surge Predictions Using Finite Element Model" *J. Hydraulic Engineering* 118(10):1373-1390

### 3.2 Theory PDF (operational reference)

- **Luettich & Westerink (2004)** "Formulation and Numerical Implementation of the 2D/3D ADCIRC Finite Element Model Version 44.XX" — [adcirc.org PDF](https://adcirc.org/wp-content/uploads/sites/2255/2018/11/adcirc_theory_2004_12_08.pdf)
- 본 위키 — [[../manual-notes/04-theory-pdf-v44xx]]

### 3.3 Storm surge applications

- **Westerink, J.J. et al. (2008)** "A basin- to channel-scale unstructured grid hurricane storm surge model applied to southern Louisiana" *Monthly Weather Review* 136:833-864 — Katrina application
- **Dietrich, J.C. et al. (2010)** "A High-Resolution Coupled Riverine Flow, Tide, Wind, Wind Wave, and Storm Surge Model for Southern Louisiana and Mississippi. Part II: Synoptic Description and Analysis of Hurricanes Katrina and Rita" *Monthly Weather Review* 138:378-404
- **Dietrich, J.C. et al. (2011)** "Hurricane Gustav (2008) Waves and Storm Surge: Hindcast, Synoptic Analysis, and Validation in Southern Louisiana" *Monthly Weather Review* 139:2488-2522 — ADCIRC + SWAN coupling

### 3.4 Vortex / hurricane forcing (NWS modes)

- **Holland, G.J. (1980)** "An Analytic Model of the Wind and Pressure Profiles in Hurricanes" *Monthly Weather Review* 108:1212-1218 — Holland B (ADCIRC NWS=19 AHM)
- **Gao, J. et al. (2014)** GAHM (Generalized AHM) — quadrant-dependent B + BL Vmax, ADCIRC NWS=20

## 4. 한국 적용 (참고)

- KHOA Annual Report 2024 §3.1 (source_id: khoa-annual-reports) — 한국 이상조위 분석
- 한국 적용 ADCIRC 운영 — [`concepts/storm-surge/04-code-and-tools.md`](../../../concepts/storm-surge/04-code-and-tools.md) 의 NWS=13 (JMA-MSM) 한국 hindcast 워크플로
- (개별 한국 hindcast 논문은 별도 큐레이션 필요)

## 5. 운영 자원

| 자원 | 비고 |
|---|---|
| Official examples | [adcirc.org/home/documentation/example-problems/](https://adcirc.org/home/documentation/example-problems/) ([[../manual-notes/08-official-example-problems]]) |
| GitHub Issues | [github.com/adcirc/adcirc/issues](https://github.com/adcirc/adcirc/issues) |
| Users forum (메일링 리스트) | adcirc.org → Community |

## 6. 본 위키 내 cross-ref

- [`concepts/storm-surge/01-concept.md`](../../../concepts/storm-surge/01-concept.md) — Pugh §6 storm surge + ADCIRC 5 인자
- [`concepts/storm-surge/02-theory.md`](../../../concepts/storm-surge/02-theory.md) — Pugh + ADCIRC GWCE
- [`concepts/storm-surge/03-analysis-methods.md`](../../../concepts/storm-surge/03-analysis-methods.md) — separation·MK trend·return period
- [`concepts/storm-surge/04-code-and-tools.md`](../../../concepts/storm-surge/04-code-and-tools.md) — NWS modes·KHOA observation·운영 운영
- [`concepts/tides/06-model-application.md`](../../../concepts/tides/06-model-application.md) — 조석 forcing
- [`models/ADCIRC/source-analysis/`](../source-analysis/) — 38 source-analysis 노트 (README 제외 실측, AUDIT-LEDGER 관례)
- [`models/ADCIRC/manual-notes/`](../manual-notes/) — 21 verified
