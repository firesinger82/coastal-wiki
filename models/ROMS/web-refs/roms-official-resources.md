---
title: "ROMS 공식 자료 — myroms.org·GitHub·핵심 논문 (Shchepetkin & McWilliams 2005 등) 큐레이션"
topic: roms-web-refs
canonical_source: self
citation_status: verified
verification_method: "myroms.org 공식 도메인 + GitHub 공개 repo (myroms/roms, myroms/roms-jedi). License_ROMS.md (MIT) 본 위키 raw/source_code/roms/. 핵심 논문 인용은 publicly-known canonical works (Shchepetkin & McWilliams 2005, Haidvogel 2008, Warner 2008 CSTMS). §8 추가 (2026-05-26): GitHub API `gh pr view 75 -R myroms/roms` 직접 fetch — PR description verbatim + Weaver et al. 2013 (doi:10.1002/qj.1955) / 2016 (doi:10.1002/qj.2664) / 2018 (doi:10.1002/qj.3302) 정확 인용 + 93 changed files + multi_scale_B_v1.pdf attachment 명시 + 핵심 신규 multiscale_* 파일 7개 (Klaplacian/Vdiff/CIsolver/eigen/CGsolver/driver/sum_B) 직접 확인."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-26
verification_by: "Claude Opus 4.7 (1M context) — URL + 공인 논문 인용 + §8 GitHub API + Weaver et al. DOI 정확화"
verification_date: 2026-05-26
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

### 3.6 Regional review — COAWST 적용 (abstract-level, source-needed)

- **Carniel, Russo, Benetazzo 2013** (arxiv:1309.7600) — Adriatic Sea 에서 ROMS(순수 hydrodynamic)→**COAWST**(Coupled Ocean-Atmosphere-Wave-Sediment Transport) 적용 진화 review. Gulf of Venice 일일 운영, ICZM/MSP 지원 다중 시공간 규모. COAWST 결합 체계(§3.5)의 실제 지역 적용 사례 큐레이션. `citation_status: source-needed` (abstract-level; full read 후 §3.3 sediment/§3.4 mixing 와 cross-link 가능).

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

## 8. Recent updates

GitHub API 직접 fetch (`gh pr view 75 -R myroms/roms`, 2026-05-26).

### 8.1 PR #75 — Multi-scale background error covariance matrix (OPEN, feature/multiscale)

- 출처: [github.com/myroms/roms/pull/75](https://github.com/myroms/roms/pull/75)
- status: **OPEN** (mergedAt: null)
- branch: `feature/multiscale` → `develop`
- changes: **62,338 additions / 27,341 deletions / 93 files** — major refactor + new feature
- 기술 문서 (PR attachment): [multi_scale_B_v1.pdf](https://github.com/user-attachments/files/25944393/multi_scale_B_v1.pdf)

#### 8.1.1 변경 설명 (PR description verbatim)

> "This PR implements a multi-scale background error covariance (**B**) operator into **ROMS 4D-Var**. It is based on the formulation of Weaver _et al._ (2013, 2016, 2018). It is activated with the **`MULTI_SCALE_B`** option. The new formulation uses a normalized implicit diffusion operator that represents Matérn-class correlation functions, which are solved using the Chebyshev iterations algorithm (Weaver _et al._, 2016, 2018)."

> "A secondary independent effect of this development is to enable spatially varying correlation scales in modeling the background-error covariance via convolutions of pseudo-diffusion operators, which also use the Chebyshev iteration solver. It allows correlation functions (Whittle–Matérn family) with more complex shapes. The implicit diffusion operator is more efficient for multiple correlation length scales. It is up to the user to determine such spatially varying horizontal correlation length scales. For example, they can be computed from the horizontal distribution of the first Rossby radius of deformation."

#### 8.1.2 기술 핵심

- **Matérn-class correlation functions** — SPDE (Stochastic Partial Differential Equation) approach 와 연관, isotropic + anisotropic 표현 가능. Smoothness ν · range ρ · variance σ² parameters 로 형태 조절
- **Normalized implicit diffusion operator** — diffusion equation 으로 correlation modeling. correlation = diffusion 의 Green function
- **Chebyshev iterations algorithm** — implicit diffusion solver (eigenvalue-bounded iteration scheme, Weaver et al. 2016/2018)
- **Whittle-Matérn family** — Matérn parameters 의 family. 일반적 correlation 의 표현
- **Spatially varying correlation scales** — 위치별 다른 length. 예: first Rossby radius of deformation (수심·층밀도 기반 자연 scale)
- 활성화: CPP option `MULTI_SCALE_B` (opt-in)

#### 8.1.3 Weaver et al. 인용 정확화 (PR References 직접 인용 verbatim)

| 연도 | 인용 |
|---|---|
| 2013 | **Weaver, A.T. and I. Mirouze**, 2013: "On the diffusion equation and its application to isotropic and anisotropic correlation modeling in variational assimilation", *Q. J. R. Meteorol. Soc.*, **139**, 242-260, [doi:10.1002/qj.1955](https://doi.org/10.1002/qj.1955) |
| 2016 | **Weaver, A.T., Tshimanga, J., and A. Piacentini**, 2016: "Correlation operators based on an implicitly formulated diffusion equation solved with the Chebyshev iteration", *Q. J. R. Meteorol. Soc.*, **142**, 455-471, [doi:10.1002/qj.2664](https://doi.org/10.1002/qj.2664) |
| 2018 | **Weaver, A.T., Gürol, S., Tshimanga, J., Chrust, M., and A. Piacentini**, 2018: "'Time'-parallel diffusion-based correlation operators", *Q. J. R. Meteorol. Soc.*, **144**, 2067-2088, [doi:10.1002/qj.3302](https://doi.org/10.1002/qj.3302) |

#### 8.1.4 핵심 변경 파일 (93 files 중 주요)

**새 multi-scale 코어 (`ROMS/Utility/multiscale_*`)**:

| 파일 | additions | 역할 |
|---|---:|---|
| `multiscale_Klaplacian.h` | +6,365 | K-Laplacian operator (Matérn correlation 표현) |
| `multiscale_Vdiff.h` | +3,173 | Vertical diffusion |
| `multiscale_CIsolver.h` | +2,741 | Chebyshev Iterations solver (Weaver 2016/2018) |
| `multiscale_eigen.F` | +2,310 | Eigenvalue 계산 (Chebyshev iteration bounding) |
| `multiscale_CGsolver.h` | +1,518 | Conjugate Gradient solver |
| `roms_multiscale.F` | +1,494 | Multi-scale driver |
| `sum_multi_B.F` | +778 | Sum operator (스케일 별 B 합산) |

**CPP option 추가**: `ROMS/Include/cppdefs.h` (+2 -0) — `MULTI_SCALE_B`.

**Convolution refactor (mono vs multi 분리)**:

- `ROMS/Adjoint/ad_convolution.F` (+98 -1607) → `ad_convolution_mono.h` (+1640) + `ad_convolution_multi.h` (+1576)
- `ROMS/Tangent/tl_convolution.F` (+98 -1611) → `tl_convolution_mono.h` (+1632) + `tl_convolution_multi.h` (+1578)
- `ROMS/Utility/convolve.F` (+94 -904) → `convolve_mono.h` (+927) + `convolve_multi.h` (+1028)
- `ROMS/Utility/normalization.F` (+68 -6332) → `normalization_mono.h` (+6859) + `normalization_multi.h` (+6805)

→ 기존 single-scale (`mono`) 와 새 multi-scale (`multi`) 양쪽 보존 (backward compat).

**get_state refactor**: `ROMS/Utility/get_state.F` (+461 -16105) → 16개 새 `get_state_<mode>_<backend>.h` 분리 (adm/frc/generic/nlm/nrm/std/tcs/tlm/tlm_forcing × nf90/pio I/O backend).

**4D-Var 입력 확장**:

- `ROMS/External/s4dvar.in` (+293 -86) — multi-scale parameters 추가
- `ROMS/External/varinfo.yaml` (+330 -3) — variable info 확장
- `ROMS/Utility/read_asspar.F` (+907 -75) — assimilation parameter reader

#### 8.1.5 한국 적용 — NIFS KOOS-EJS 가능성

ROMS 기반 NIFS 동해예측시스템 (KOOS-EJS) 에 multi-scale B 적용 가능성:

1. **동해 의 강한 mesoscale + sub-mesoscale 양쪽 length scale** — Rossby radius (~30-40 km) + sub-mesoscale (1-10 km) → spatially varying correlation 활용 적합
2. **NIFS 다층 수온 관측 활용** — [[../../../experience/nifs-vertical-sst-trends]] 의 vertical correlation 도 K-Laplacian 으로 modeling 가능 (smoothness ν 조절)
3. **후속 평가**: KOOS-EJS 의 현재 4D-Var 구성 (단일 스케일 B 사용 여부) 확인 후 multi-scale 적용 benefit 정량화 가능

#### 8.1.6 사용자 영향

- **빌드 영향**: 93 파일 변경 + 62k+ additions — 사용자가 develop branch 최신 동기화 + 빌드 검증 후 적용. release 까지 대기 권장
- **CPP option opt-in**: `MULTI_SCALE_B` 정의 안 하면 기존 (mono) 동작 그대로
- **4D-Var 입력 형식 변경**: `s4dvar.in` 의 +293 lines — 기존 input 후방호환 확인 필요
- **convolution / normalization API**: mono.h header 로 자동 fallback 가능성. 사용자 정의 4D-Var 모듈은 점검 권장

#### 8.1.7 검증 한계

- PR open 상태 (develop branch) — 최종 merge 형식 변경 가능. release tag 미확정
- `multi_scale_B_v1.pdf` (PR attachment) full read 후 implementation 의 정식 식 (예: $B^{1/2} = \sum_i \alpha_i (I - L_i^2 \nabla^2)^{-\nu_i/2}$ 같은 explicit form, $\nu$ smoothness · $L_i$ length scale) 보강 가능
- `models/ROMS/source-analysis/4dvar/` 노트 신설 또는 보강 후 본 §과 cross-ref 강화 후속
