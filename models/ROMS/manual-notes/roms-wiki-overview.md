---
title: "ROMS myroms.org wiki 종합 인덱스 — 326 페이지 + 토픽 클러스터링"
topic: roms-wiki-overview
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/manuals/wiki/manifest.json 직접 인용 (page_count: 326, fetched_at: 2026-05-03T14:20:20Z, site: myroms.org/wiki) + markdown/ 321 .md files 직접 ls — Getting_Started·build_roms·cppdefs.h·Vertical_Mixing_Parameterizations·Horizontal_Mixing·GLS_MIXING·Tidal_Forcing·Input_Parameter_Files·Standard_Output·Grid_Generation·Nested_Grids·sediment_cppdefs.h 등 핵심 토픽 directory 직접 확인."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — manifest.json + markdown/ ls 직접 확인"
verification_date: 2026-05-24
related:
  - models/ROMS/manual-notes/roms-wiki-getting-started.md
  - models/ROMS/README.md
  - models/ROMS/web-refs/roms-official-resources.md
---

# ROMS myroms.org wiki 종합 인덱스

> 출처: [`models/ROMS/raw/manuals/wiki/`](../raw/manuals/wiki/) — myroms.org wiki mirror (326 pages, fetched 2026-05-03). `manifest.json` 직접 인용.

## 1. 자료 식별

| 항목 | 값 |
|---|---|
| 사이트 | myroms.org/wiki |
| 페이지 수 | **326** (manifest.json) |
| Fetched | 2026-05-03 T14:20:20Z |
| 본 위키 mirror | `raw/manuals/wiki/markdown/` (321 .md files) + `wikitext/` + `html/` |
| 인용 형식 | "ROMS wiki: [Page_Name] (myroms.org/wiki/Page_Name, fetched 2026-05-03)" |

## 2. 토픽 클러스터 (321 markdown 페이지)

### 2.1 Getting Started + Build

| 핵심 페이지 | 내용 |
|---|---|
| `Getting_Started.md` | ROMS 개관 + 디렉토리 구조 + C-preprocessing intro ([[roms-wiki-getting-started]]) |
| `build_roms.md` | build_roms.sh 빌드 스크립트 |
| `build_Script.md` | 빌드 스크립트 일반 |
| `my_build_paths.md` | 사용자 build path 설정 |
| `cppdefs.h.md` | CPP options (가장 중요한 운영 결정) |
| `sediment_cppdefs.h.md` | sediment CPP 옵션 |

### 2.2 4DVar (데이터 동화) — 대량 페이지

ROMS wiki 의 가장 큰 부분 — 4DVar tutorial + driver 별 페이지:
- `4DVar_Normalization_Tutorial.md` + `_2010.md`
- `4DVar_Tutorial_Introduction.md` + `_2010.md`
- `A4DVAR_TOY.md` + `_CASE.md`
- `I4DVAR.md`, `R4DVAR.md` (Incremental, Representer)
- `ADJOINT.md`, `ADM_DRIVER.md`, `AD_SENSITIVITY.md`
- `AFT_EIGENMODES.md`, `FT_EIGENMODES.md`, `FSV_DRIVER.md`
- `BG_NORMALIZATION.md`, `CORRELATION.md`
- (수십 페이지)

### 2.3 격자 + 입출력

| 페이지 | 내용 |
|---|---|
| `Grid_Generation.md` | 격자 생성 일반 |
| `Grid_Processing_Scripts.md` | 격자 후처리 스크립트 |
| `Nested_Grids.md` | nested (multi-grid) |
| `seagrid.md` | seagrid MATLAB 도구 |
| `easygrid.md` | easygrid Python 도구 |
| `Input_Parameter_Files.md` | input file (.in) family |
| `Standard_Output.md` + `_File.md` + `_Files.md` | NetCDF 출력 표준 |

### 2.4 Mixing (vertical + horizontal)

| 페이지 | 내용 |
|---|---|
| `Vertical_Mixing_Parameterizations.md` | KPP·MY25 등 vertical mixing |
| `GLS_MIXING.md` | Generic Length Scale mixing |
| `Horizontal_Mixing.md` | UV·TS horizontal mixing scheme |

### 2.5 Boundary + Forcing

| 페이지 | 내용 |
|---|---|
| `Tidal_Forcing.md` | 조석 forcing input |
| `ADD_FSOBC.md`, `ADD_M2OBC.md` | open boundary modifiers |
| `ANA_*` 다수 | analytical forcing functions (대기·BC·initial·grid 등) |

ANA_* 페이지 다수:
- `ANA_BIOLOGY.md`, `ANA_BPFLUX/BSFLUX/BTFLUX.md` (biology fluxes)
- `ANA_CLOUD.md`, `ANA_DIAG.md`
- `ANA_GRID.md` (analytical grid setup)
- (수십 더)

### 2.6 Vertical coordinate

| 페이지 | 내용 |
|---|---|
| `Vertical_S-coordinate.md` | S-coordinate (terrain-following) — ROMS 의 핵심 vertical 방식 |

### 2.7 격자 + bottom

| 페이지 | 내용 |
|---|---|
| `CURVGRID.md` | curvilinear grid |
| `BBL` 관련 | Bottom Boundary Layer (source-analysis 와 cross-ref) |

## 3. 운영 cheat-sheet — Wiki 페이지 선택 가이드

| 작업 | 권장 wiki page |
|---|---|
| **신규 ROMS 첫 설치** | Getting_Started → build_roms |
| **CPP 옵션 결정** | cppdefs.h + Vertical_Mixing_Parameterizations + sediment_cppdefs.h |
| **격자 생성** | Grid_Generation + seagrid/easygrid + CURVGRID |
| **Nesting setup** | Nested_Grids + Grid_Processing_Scripts |
| **Boundary 설정** | Input_Parameter_Files + Tidal_Forcing + ADD_FSOBC/M2OBC + ANA_* |
| **출력 NetCDF** | Standard_Output_Files |
| **데이터 동화** | 4DVar_Tutorial_Introduction + I4DVAR + R4DVAR + Normalization |
| **민감도 분석** | ADJOINT + AD_SENSITIVITY + FT_EIGENMODES |

## 4. 본 위키 verified manual-notes (M-C 2차 시작)

| 노트 | 상태 | 비고 |
|---|---|---|
| [[roms-wiki-overview]] (본 노트) | verified | 326 pages 인덱스 |
| [[roms-wiki-getting-started]] | verified | Getting_Started.md 본문 (디렉토리 구조 + C-pp intro) |
| `roms-wiki-cppdefs.md` | (M-C 후속) | cppdefs.h CPP 옵션 운영 결정 |
| `roms-wiki-vertical-mixing.md` | (M-C 후속) | KPP·MY25·GLS 선택 가이드 |
| `roms-wiki-4dvar-tutorial.md` | (M-C 후속) | 4DVar 학습 entry |

## 5. ROMS Fortran source 매핑 (source-analysis 와 cross-ref)

| Wiki 페이지 | Fortran 모듈 |
|---|---|
| Getting_Started 디렉토리 구조 | [[../source-analysis/roms_main_driver_dispatch]] (Drivers/) |
| cppdefs.h | (모든 Nonlinear/ + Drivers/ 코드의 활성화 매크로) |
| Vertical_Mixing_Parameterizations | [[../source-analysis/roms_vertical_mixing]] |
| Tidal_Forcing | [[../source-analysis/roms_open_boundaries]] |
| Grid_Generation + CURVGRID | [[../source-analysis/roms_grid_metrics]] |
| 4DVar tutorials | [[../source-analysis/roms_4dvar]] + i4dvar.F driver |
| Nested_Grids | [[../source-analysis/roms_nesting]] |
| ANA_* analytical | Functionals/ + Include/ |
| sediment_cppdefs | [[../source-analysis/sediment/roms_sediment]] subdir + Nonlinear/Sediment/ |

## 6. 관련 자료

- [[../README]] — ROMS 모델 정체 카드
- [[../web-refs/roms-official-resources]] — Shchepetkin-McWilliams 2005 + Haidvogel 2008 + Warner 2008 CSTMS 인용
- [[../source-analysis/roms_main_driver_dispatch]] — Drivers/ + Master/ ESMF
- [[../source-analysis/roms_nonlinear_physics_modules]] — Nonlinear/ 6 subdirs
- [[roms-wiki-getting-started]] — Getting_Started 본문 verified
- 외부: [myroms.org wiki](https://www.myroms.org/wiki/), [myroms forum](https://www.myroms.org/forum/)
