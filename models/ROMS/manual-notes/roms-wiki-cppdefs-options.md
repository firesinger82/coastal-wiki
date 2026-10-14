---
title: "ROMS cppdefs.h — 대표 CPP 범주 (myroms.org/wiki/cppdefs.h)"
topic: roms-wiki-cppdefs
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/manuals/wiki/markdown/cppdefs.h.md (myroms.org/wiki/cppdefs.h, _revid=5862_, fetched 2026-05-03) 본문 직접 인용 — Contents 의 32 numbered section 직접 추출 (momentum·tracers·pressure gradient·atmospheric BL·shortwave·Lagrangian·horizontal/vertical mixing·GLS·MY25·KPP·Richardson·3 BBL closures·lateral BC·tidal forcing·driver·TL/RPR/ADJ·6 biology models). 2026-10-14 ROMS recovery 대조 보고서 반영"
last_source_check: "2026-10-14 (recovery 대조 반영)"
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

# ROMS `cppdefs.h` — 대표 CPP 범주

> 출처: [`models/ROMS/raw/manuals/wiki/markdown/cppdefs.h.md`](../raw/manuals/wiki/markdown/cppdefs.h.md) (myroms.org/wiki/cppdefs.h, _revid=5862_, fetched 2026-05-03).

## 1. cppdefs.h 의 역할 (본문 직접 인용)

> "Internal header file containing all the C-preprocessing options that defines a particular application." (cppdefs.h.md 본문)

> "The application CPP option is specified in the makefile definition ROMS_APPLICATION. The application header file is determined during compilation as the lowercase value of ROMS_APPLICATION with the .h extension and loaded into the ROMS_HEADER definition." (cppdefs.h.md 본문)

많은 ROMS 커널은 `cppdefs.h`를 포함한다.
독립 유틸리티에는 예외가 있다 (`ROMS/Utility/yaml_parser.F:1`, `ROMS/Utility/get_env.F:1`; [빌드·옵션 대조 보고서의 RBH-3477](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

### 1.1 활성 메커니즘

```cpp
#if defined ROMS_HEADER
# include ROMS_HEADER
#else
  CPPDEFS - Choose an appropriate ROMS application.
#endif
```

→ 사용자가 makefile 에서 `ROMS_APPLICATION = MY_APP` 설정 → 컴파일 시 `my_app.h` 가 자동 include → 그 안의 `#define` 매크로로 application의 CPP 옵션을 지정한다(`cppdefs.h.md:7-10`); 별도 입력 스크립트도 있다(`Getting_Started.md:7`).

응용 헤더를 먼저 읽는다 (`ROMS/Include/cppdefs.h:753-754`).
이어서 `globaldefs.h`를 읽는다 (`ROMS/Include/cppdefs.h:763`; [비선형 계산 흐름 대조 보고서의 N-05](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md#6-기존-노트-대조와-수정안)).

## 2. 대표 CPP 범주 (Contents 직접 인용)

번호는 위키 Contents의 편집 범주 번호이다 ([빌드·옵션 대조 보고서의 RBH-3479](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

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
| 15 | Vertical mixing of momentum + tracers | GLS·MY25·LMD·BVF_MIXING·ANA_VMIX |
| 16 | **Generic Length-Scale closure (GLS)** | GLS_MIXING + k-ε, k-ω, gen 변종 |
| 17 | **Mellor/Yamada 2.5 closure (MY25)** | MY25_MIXING |
| 18 | **K-profile parameterization (KPP)** | LMD_MIXING + sub-옵션 (LMD_RIMIX, LMD_CONVEC, LMD_SHAPIRO 등) |

수직 혼합 목록에는 `BVF_MIXING`과 `ANA_VMIX`도 있다.
`NONLINEAR`·`SOLVE3D`의 `main3d`에서는 `ANA_VMIX`를 먼저 검사하고 다음으로 `LMD_MIXING`, `BVF_MIXING`을 검사한다 (`ROMS/Nonlinear/main3d.F:533-539`; [빌드·옵션 대조 보고서의 RBH-3480](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

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

노트의 생물 모델 묶음은 `roms-4.2`의 목록과 맞는다.
현재 `cppdefs.h`의 목록에는 `ECB`가 추가되어 있다 (`ROMS/Include/cppdefs.h:469-471`).
추가 커밋은 `d06fee85` (2025-06-27, Adding Estuarine Carbon Biogeochemical Model (ECB))이다 ([생지화학 대조 보고서의 NT-016](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안)).

## 3. 운영 결정 매트릭스 — 권장 구성

이 표의 기본안은 권장 구성의 기준값이다 ([수치 대조 보고서의 RTN-410](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#4-노트-대조와-수정안)).
`LMD_MIXING`은 선택 가능한 폐쇄이다.
application header가 선택한다 ([혼합·경계·강제 대조 보고서의 RMF1-963](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#4-노트-대조와-수정안)).
실제 CPP·runtime 선택은 사례별로 기록한다 ([시험 사례 대조 보고서의 RT1-1531](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안)).

| 결정 | 권장 옵션 | 비고 |
|---|---|---|
| **Pressure gradient** | DJ_GRADPS (Shchepetkin-McWilliams 2003) | 적용·성능 권고: 안정·정확 |
| **Atmospheric BL flux** | BULK_FLUXES | COARE 알고리즘 ([구현 노트](../source-analysis/roms_bulk_flux_coare.md)) |
| **Vertical mixing** (권고의 기본안) | LMD_MIXING (KPP) + LMD_RIMIX + LMD_CONVEC + LMD_NONLOCAL | Large 1994 표준 |
| Vertical mixing (alt) | GLS_MIXING (k-ε 또는 k-ω) | GOTM 호환 |
| Vertical mixing (legacy) | MY25_MIXING | 학습 reference |
| **Horizontal momentum** | UV_VIS2 + MIX_S_UV | 적용·성능 권고: 시작 안전 |
| **Horizontal tracers** | TS_DIF2 + MIX_GEO_TS | geopotential surface (일정 z) (`ROMS/Nonlinear/t3dmix2_geo.h:10-11`) |
| **BBL** (sediment 시) | SSW_BBL (CSTMS) | 퇴적물 응용의 선택 권고 |
| **Tidal forcing** | SSH_TIDES + UV_TIDES | OBC 결합 |
| **Driver** | NONLINEAR | 일반 forecast |
| **Biology** (선택) | BIO_FENNEL 또는 NPZD | 선택 진입 권고 ([생지화학 대조 보고서의 NT-017](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안)) |

`bulk_flux`의 현재 기본 경로는 COARE 3.5이다 (`ROMS/Nonlinear/bulk_flux.F:78-79`).
`COARE_30`은 이전 COARE 3.0 경로를 선택한다 (`ROMS/Nonlinear/bulk_flux.F:797-799`; [빌드·옵션 대조 보고서의 RBH-3482](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

`MIX_S_TS`는 지형 추종 방향의 선택이다 (`ROMS/Nonlinear/t3dmix2_s.h:10–11`). [10-14 전수 검증 보완]
`MIX_ISO_TS`는 isopycnal 방향의 선택이다 (`ROMS/Nonlinear/t3dmix.F:17–24`, `ROMS/Nonlinear/t3dmix2_iso.h:10–11`; [수치 대조 보고서의 RTN-400](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#4-노트-대조와-수정안)). [10-14 전수 검증 보완]

SSW_BBL은 퇴적물 응용의 선택 권고다.
실제 기본 마찰 옵션은 각 사례 헤더에서 확인한다 ([시험 사례 대조 보고서의 RT1-1530](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안)).

## 4. 한국 동해 사용자 적용 예시

이 블록은 한국 동해에 대한 사용자 적용 예시이다 ([빌드·옵션 대조 보고서의 RBH-3484](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

```cpp
// 한국 동해 사용자 적용 예시
#define NONLINEAR
#define SOLVE3D
#define SPHERICAL
#define DJ_GRADPS
#define UV_ADV
#define UV_COR
#define BULK_FLUXES
#define LMD_MIXING
#define LMD_RIMIX
#define LMD_CONVEC
#define LMD_NONLOCAL
#define UV_VIS2
#define MIX_S_UV
#define TS_DIF2
#define MIX_GEO_TS
#define UV_TIDES
#define SSH_TIDES
#define ANA_BSFLUX
#define ANA_BTFLUX
// (optional sediment)
// #define SEDIMENT
// #define SSW_BBL
```

`UV_VIS2`를 사용하는 `SOLVE3D` 예제에는 `MIX_S_UV` 또는 `MIX_GEO_UV`를 명시한다.
둘 다 없으면 `UV3DMIX: must define one of MIX_S_UV, MIX_GEO_UV` 오류 구문이 남는다 (`ROMS/Nonlinear/uv3dmix.F:19-24`; [수치 대조 보고서의 RTN-401](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#4-노트-대조와-수정안)).
퇴적물 옵션 이름은 `SEDIMENT`이다 (`ROMS/Include/cppdefs.h:523`, `ROMS/Nonlinear/Sediment/sediment.F:5`; [퇴적물 대조 보고서의 RN1-039](../../../_staging/recovery/compare/roms-sediment-ice-vegetation-vs-code.md#4-노트-대조와-수정안)).

## 5. cppdefs vs runtime 옵션 — 결정 시점 차이

| 시점 | 선택 항목 | 결정 방식 |
|---|---|---|
| **컴파일 시 (CPP)** | 물리 모듈과 지원 커널 | KPP·MY25·GLS, biology 활성, sediment 활성, BBL 종류 ([퇴적물 대조 보고서의 RN1-040](../../../_staging/recovery/compare/roms-sediment-ice-vegetation-vs-code.md#4-노트-대조와-수정안)) |
| **컴파일 시 (CPP)** | 운동량 이류 | `UV_*` 이류 옵션 (`ROMS/Include/cppdefs.h:35-38`) |
| **Runtime (.in)** | 추적자 이류 | `SOLVE3D`에서 `Hadvection`·`Vadvection`으로 추적자별로 지정한다 (`ROMS/Utility/read_phypar.F:418–442`). [10-14 전수 검증 정정] |
| **Runtime (.in)** | 수직 좌표 | `Vtransform`·`Vstretching` 정수 입력 ([수치 대조 보고서의 RTN-402](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#4-노트-대조와-수정안)) |
| **Runtime (.in)** | 입력 자료와 계산 매개변수 | 격자 파일, 시간 step, 점성계수, 경계 파일 경로를 입력한다 (`ROMS/Utility/read_phypar.F:593–594,839–842,4215–4218,4294–4295`). [10-14 전수 검증 보완] |

컴파일한 기능 범위 안에서 실행 시 입력을 바꿀 수 있다 ([빌드·옵션 대조 보고서의 RBH-3487](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).

## 6. 세부 대조 자료

- [혼합·경계·강제 대조 보고서](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md) — 수직 혼합과 조석 강제
- [4D-Var 대조 보고서](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md) — 4D-Var 학습 자료와 동화 드라이버
- [Representer 대조 보고서](../../../_staging/recovery/compare/roms-da-representer-vs-code.md) — Representer 동화

Representer는 I4DVAR의 primal 접선 모델과 구분한다 ([4D-Var 대조 보고서의 DA1-821](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md#4-노트-대조와-수정안)).

## 7. 관련 자료

- [roms-wiki-overview](roms-wiki-overview.md) — 326 pages 인덱스
- [roms-wiki-getting-started](roms-wiki-getting-started.md) — Getting_Started 본문
- [roms_vertical_mixing](../source-analysis/roms_vertical_mixing.md) — §15-18 매핑 (KPP·MY25·GLS Fortran)
- [roms_bulk_flux_coare](../source-analysis/roms_bulk_flux_coare.md) — §7 BULK_FLUXES Fortran 구현
- [roms_main_driver_dispatch](../source-analysis/roms_main_driver_dispatch.md) — §25 ROMS/TOMS driver
- [roms-official-resources](../web-refs/roms-official-resources.md) — Shchepetkin-McWilliams 2003 (§6 PG), Large 1994 (§18 KPP)
- 위키 원문: [cppdefs.h](../raw/manuals/wiki/markdown/cppdefs.h.md), [Options](../raw/manuals/wiki/markdown/Options.md)

## 문서와 코드 차이 (10-14 대조)

- [문서와 코드 차이 1](roms-wiki-cppdefs-options-differences-1.md)
- [문서와 코드 차이 2](roms-wiki-cppdefs-options-differences-2.md)
- [문서와 코드 차이 3](roms-wiki-cppdefs-options-differences-3.md)
- [문서와 코드 차이 4](roms-wiki-cppdefs-options-differences-4.md)

네 차이 노트에 배정한 행 수는 794개이다. 결론별 행 수는 A 판 차이 562개, B 문서 오기 126개, C 문서 누락 90개, D 문서에만 있음 8개, E 코드 결함 후보 2개, F 표기 차이 6개이다. 수량은 [note-job-5.tsv](../../../_staging/recovery/assign/note-job-5.tsv), [note-job-6.tsv](../../../_staging/recovery/assign/note-job-6.tsv), [note-job-7.tsv](../../../_staging/recovery/assign/note-job-7.tsv), [note-job-8.tsv](../../../_staging/recovery/assign/note-job-8.tsv)의 해당 차이 노트 배정 행을 합산한 값이다. [10-14 전수 검증 정정]
