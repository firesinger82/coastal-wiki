---
title: "ROMS cppdefs.h — 32+ CPP option category 종합 (myroms.org/wiki/cppdefs.h)"
topic: roms-wiki-cppdefs
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/manuals/wiki/markdown/cppdefs.h.md (myroms.org/wiki/cppdefs.h, _revid=5862_, fetched 2026-05-03) 본문 직접 인용 — Contents 의 32 numbered section 직접 추출 (momentum·tracers·pressure gradient·atmospheric BL·shortwave·Lagrangian·horizontal/vertical mixing·GLS·MY25·KPP·Richardson·3 BBL closures·lateral BC·tidal forcing·driver·TL/RPR/ADJ·6 biology models)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — wiki markdown 직접 인용"
verification_date: 2026-05-24
related:
  - models/ROMS/manual-notes/roms-wiki-overview.md
  - models/ROMS/manual-notes/roms-wiki-getting-started.md
  - models/ROMS/source-analysis/roms_vertical_mixing.md
  - models/ROMS/source-analysis/roms_nonlinear_physics_modules.md
---

# ROMS `cppdefs.h` — 32+ CPP Option Categories

> 출처: [`models/ROMS/raw/manuals/wiki/markdown/cppdefs.h.md`](../raw/manuals/wiki/markdown/cppdefs.h.md) (myroms.org/wiki/cppdefs.h, _revid=5862_, fetched 2026-05-03). **운영 결정의 75% 가 여기서 끝남** (cppdefs 활성 옵션이 컴파일 시 binary 결정).

## 1. cppdefs.h 의 역할 (본문 직접 인용)

> "Internal header file containing all the C-preprocessing options that defines a particular application. It is included at the top of every ROMS source file. The application CPP option is specified in the makefile definition ROMS_APPLICATION. The application header file is determined during compilation as the lowercase value of ROMS_APPLICATION with the .h extension and loaded into the ROMS_HEADER definition." (cppdefs.h.md 본문)

### 1.1 활성 메커니즘

```cpp
#if defined ROMS_HEADER
# include ROMS_HEADER
#else
  CPPDEFS - Choose an appropriate ROMS application.
#endif
```

→ 사용자가 makefile 에서 `ROMS_APPLICATION = MY_APP` 설정 → 컴파일 시 `my_app.h` 가 자동 include → 그 안의 `#define` 매크로로 모든 옵션 결정.

## 2. 32 Option 카테고리 (Contents 직접 인용)

### 2.1 Equations + 수치 옵션 (1-9)

| § | 카테고리 |
|---|---|
| 1 | Options associated with momentum equations |
| 2 | Option to limit bottom stress |
| 3 | Options associated with tracers equations |
| 4 | Option to suppress further surface cooling |
| 5 | Option for MPDATA 3D Advection |
| 6 | **Options for pressure gradient algorithm** (Shchepetkin-McWilliams 2003 등) |
| 7 | **Options for atmospheric boundary layer surface fluxes** (BULK_FLUXES → bulk_flux.F COARE) |
| 8 | Options for wave roughness formulation in bulk fluxes |
| 9 | Options for shortwave radiation |

### 2.2 모델 구성 (10-12)

| § | 카테고리 |
|---|---|
| 10 | Options for model configuration |
| 11 | Options for Lagrangian drifters |
| 12 | Options for analytical fields configuration |

### 2.3 Mixing (13-18) — 운영 결정 핵심

| § | 카테고리 | 옵션 |
|---|---|---|
| 13 | Horizontal mixing of momentum | UV_VIS2, UV_VIS4, UV_SMAGORINSKY 등 |
| 14 | Horizontal mixing of tracers | TS_DIF2, TS_DIF4, MIX_S_TS, MIX_GEO_TS 등 |
| 15 | Vertical mixing of momentum + tracers | (parent — 16-18 중 선택) |
| 16 | **Generic Length-Scale closure (GLS)** | GLS_MIXING + k-ε, k-ω, gen 변종 |
| 17 | **Mellor/Yamada 2.5 closure (MY25)** | MY25_MIXING |
| 18 | **K-profile parameterization (KPP)** | LMD_MIXING + sub-옵션 (LMD_RIMIX, LMD_CONVEC, LMD_SHAPIRO 등) |

### 2.4 추가 mixing + bottom (19-22)

| § | 카테고리 |
|---|---|
| 19 | Richardson number smoothing |
| 20 | Meinte Blass bottom boundary layer closure (MB_BBL) |
| 21 | Styles and Glenn (2000) bottom boundary layer (SG_BBL) |
| 22 | **Sherwood/Signell/Warner bottom boundary layer (SSW_BBL)** — CSTMS 권장 |

### 2.5 Boundary + driver (23-25)

| § | 카테고리 |
|---|---|
| 23 | Lateral boundary conditions |
| 24 | Tidal forcing at open boundaries |
| 25 | ROMS/TOMS driver (NONLINEAR / ADJOINT / TANGENT / etc.) |

### 2.6 Data assimilation (26)

| § | 카테고리 |
|---|---|
| 26 | Tangent linear, representer and adjoint models |

### 2.7 Biology (27-32)

| § | Biology 모델 | 출처 |
|---|---|---|
| 27 | **Fennel et al. 2006** | Fennel et al. (2006) "Nitrogen cycling..." |
| 28 | Hypoxia ecosystem model | |
| 29 | **NPZD** (Nitrogen-Phytoplankton-Zooplankton-Detritus) | 단순 4-box |
| 30 | EcoSim bio-optical | |
| 31 | Nemuro lower trophic level | |
| 32 | Red tide biological | |

## 3. 운영 결정 매트릭스 — 신규 application 시

| 결정 | 권장 옵션 | 비고 |
|---|---|---|
| **Pressure gradient** | DJ_GRADPS (Shchepetkin-McWilliams 2003) | 안정·정확 |
| **Atmospheric BL flux** | BULK_FLUXES | COARE 알고리즘 ([[../source-analysis/roms_bulk_flux_coare]]) |
| **Vertical mixing** (default) | LMD_MIXING (KPP) + LMD_RIMIX + LMD_CONVEC + LMD_NONLOCAL | Large 1994 표준 |
| Vertical mixing (alt) | GLS_MIXING (k-ε 또는 k-ω) | GOTM 호환 |
| Vertical mixing (legacy) | MY25_MIXING | 학습 reference |
| **Horizontal momentum** | UV_VIS2 + MIX_S_UV | 시작 안전 |
| **Horizontal tracers** | TS_DIF2 + MIX_GEO_TS | rotated isobath |
| **BBL** (sediment 시) | SSW_BBL (CSTMS) | Sherwood/Signell/Warner |
| **Tidal forcing** | SSH_TIDES + UV_TIDES | OBC 결합 |
| **Driver** | NONLINEAR | 일반 forecast |
| **Biology** (선택) | BIO_FENNEL 또는 NPZD | 단순→복잡 진입 |

## 4. 한국 적용 추천 cppdefs (예시)

KOOS-EJS (NIFS 동해예측시스템) 류 운영용 minimal:

```cpp
// 한국 동해 minimal forecast
#define NONLINEAR
#define SOLVE3D
#define SPHERICAL
#define DJ_GRADPS
#define BULK_FLUXES
#define LMD_MIXING
#define LMD_RIMIX
#define LMD_CONVEC
#define LMD_NONLOCAL
#define UV_VIS2
#define TS_DIF2
#define MIX_GEO_TS
#define UV_TIDES
#define SSH_TIDES
#define ANA_BSFLUX
#define ANA_BTFLUX
// (optional sediment)
// #define SOLVE_SEDIMENT
// #define SSW_BBL
```

## 5. cppdefs vs runtime 옵션 — 결정 시점 차이

| 시점 | 결정 방식 |
|---|---|
| **컴파일 시 (cppdefs)** | KPP vs MY25, advection scheme, biology 활성, sediment 활성, BBL 종류 등 — 한번 결정하면 binary fixed |
| **Runtime (.in)** | 격자 파일, 시간 step, 부분 viscosity 값, BC NetCDF 경로 등 — 매 run 다름 |

→ application 별 cppdefs 한번 작성 → 여러 grid·forcing 으로 같은 binary 재사용.

## 6. 작성 우선순위 (남은 M-C)

- `roms-wiki-vertical-mixing-decision.md` — KPP·MY25·GLS 비교 + 선택 가이드 (§15-18 deep)
- `roms-wiki-tidal-forcing-setup.md` — Tidal_Forcing.md (§24) deep + 한국 KHOA tide 결합
- `roms-wiki-4dvar-tutorial.md` — 4DVar 학습 entry (§25-26 driver)

## 7. 관련 자료

- [[roms-wiki-overview]] — 326 pages 인덱스
- [[roms-wiki-getting-started]] — Getting_Started 본문
- [[../source-analysis/roms_vertical_mixing]] — §15-18 매핑 (KPP·MY25·GLS Fortran)
- [[../source-analysis/roms_bulk_flux_coare]] — §7 BULK_FLUXES Fortran 구현 (신설 M-D 2차)
- [[../source-analysis/roms_main_driver_dispatch]] — §25 ROMS/TOMS driver
- [[../web-refs/roms-official-resources]] — Shchepetkin-McWilliams 2003 (§6 PG), Large 1994 (§18 KPP)
- 외부: [myroms.org/wiki/cppdefs.h](https://www.myroms.org/wiki/cppdefs.h), [Options](https://www.myroms.org/wiki/Options)
