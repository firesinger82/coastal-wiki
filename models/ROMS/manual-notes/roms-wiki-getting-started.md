---
title: "ROMS Getting Started — myroms.org wiki 본문 직접 인용 + 디렉토리 구조"
topic: roms-wiki-getting-started
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/manuals/wiki/markdown/Getting_Started.md (77 줄, _revid=6667_, fetched 2026-05-03 from myroms.org/wiki/Getting_Started) 본문 직접 인용. ROMS 디렉토리 구조 (Compilers·Data·Master·ROMS/Adjoint·Bin·Drivers·External·Functionals·Include·Modules·Nonlinear·Obsolete·Programs·Representer·Tangent·Utility·User) 직접 추출."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — wiki markdown 직접 인용"
verification_date: 2026-05-24
related:
  - models/ROMS/manual-notes/roms-wiki-overview.md
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_nonlinear_physics_modules.md
---

# ROMS Getting Started

> 출처: [`models/ROMS/raw/manuals/wiki/markdown/Getting_Started.md`](../raw/manuals/wiki/markdown/Getting_Started.md) (myroms.org/wiki/Getting_Started, _revid=6667_, fetched 2026-05-03).

## 1. ROMS 본문 (직접 인용)

> "ROMS is a very complex model with many options and capabilities. ROMS is composed of many Fortran files (.F), a few header files (.h), various input script files (.in), a metadata variable definition file ([varinfo.yaml](/wiki/varinfo.yaml)), and a single [makefile](/wiki/makefile)."
>
> "The ROMS algorithms are distributed with the following directory structure:"
> (이하 §2)
>
> "ROMS uses [C-preprocessing](/wiki/C-preprocessing) extensively to activate and/or deactivate ..."

## 2. 디렉토리 구조 (Getting_Started.md 본문)

```
Compilers/                     make configuration files
Data/                          Input data root directory
    /ROMS/                     ROMS data root directory
         /CDL                  ROMS NetCDF metadata design
Master/                        Main standalone and coupling programs
ROMS/                          ROMS root directory
    /Adjoint/                  Adjoint model
            /Biology           Adjoint biology/ecosystem models
    /Bin                       Executable scripts
    /Drivers                   Computational drivers
    /External                  Standard input scripts
    /Functionals               Analytical expression header files
    /Include                   Test cases configuration header files
    /Modules                   Declaration modules
    /Nonlinear/                Nonlinear model
              /BBL             Bottom Boundary Layer formulation
              /Biology         Nonlinear biology/ecosystem models
              /SeaIce          SeaIce model
              /Sediment        Nonlinear sediment transport model
    /Obsolete                  Discontinued files
    /Programs                  Support programs
    /Representer/              Representer model
                /Biology       Representer biology/ecosystem models
    /Tangent/                  Tangent linear model
            /Biology           Tangent linear biology/ecosystem models
    /Utility                   Generic utility files
User/                          ROMS User interface root directory
    /External                  User standard input scripts
    /Functionals               User analytical expressions templates
    /Include                   User application header files
```

→ 본 위키 [`models/ROMS/raw/source_code/roms/`](../raw/source_code/roms/) 와 1:1 일치.

## 3. 디렉토리 구조 의미별 분류

### 3.1 Build 인프라

| 디렉토리 | 역할 |
|---|---|
| `Compilers/` | Linux GFortran·Intel·Cray·etc. 별 make configuration |
| `Bin` | 실행 스크립트 (build_roms.sh·copyright.sh 등) |
| `Programs` | 보조 Programs |
| (root) `makefile` | 단일 makefile |

### 3.2 Coupling 인프라

| 디렉토리 | 역할 |
|---|---|
| `Master/` | Standalone main + ESMF coupler ([[../source-analysis/roms_main_driver_dispatch]] §3) |

### 3.3 ROMS 모델 변종 (model variants)

| 디렉토리 | 모델 변종 | 활용 |
|---|---|---|
| `Nonlinear/` | **Forward (Nonlinear)** | 일반 hindcast/forecast — [[../source-analysis/roms_nonlinear_physics_modules]] |
| `Adjoint/` | **Adjoint model** | sensitivity analysis |
| `Tangent/` | Tangent linear model | linearized perturbation |
| `Representer/` | Representer model | 4DVar 변종 |

각 모델 변종은 `/Biology` subdir 가지며, 4-model 모두 biology coupling 지원.

### 3.4 Driver 인프라

| 디렉토리 | 역할 |
|---|---|
| `Drivers/` | 46 driver headers (nl_roms·ad_roms·i4dvar 등) — [[../source-analysis/roms_main_driver_dispatch]] |
| `Modules/` | Global declaration modules |
| `External/` | Standard input scripts (.in files) |
| `Functionals/` | Analytical expression header files (ANA_* family) |
| `Include/` | Test cases configuration header files |

### 3.5 보조

| 디렉토리 | 역할 |
|---|---|
| `Utility/` | Generic utility (NetCDF I/O·math·시간 처리·etc.) |
| `Obsolete/` | Discontinued files |

### 3.6 User 인터페이스

| 디렉토리 | 역할 |
|---|---|
| `User/` | 사용자 정의 입력·해석 함수 |
| `User/External` | 사용자 .in scripts |
| `User/Functionals` | 사용자 ANA_* 템플릿 |
| `User/Include` | 사용자 cppdefs.h |

### 3.7 Data

| 디렉토리 | 역할 |
|---|---|
| `Data/` | Input data root |
| `Data/ROMS/CDL` | NetCDF metadata design (Common Data Language) |

## 4. 단일 makefile 모델

ROMS 의 빌드 흐름:

1. **사용자 cppdefs.h** (`User/Include/`) 작성 — application 별 macro
2. `build_roms.sh` 실행 (`Bin/`)
3. `makefile` 가 `Compilers/<arch>.mk` 참조해 빌드
4. 실행 binary 산출 (oceanS·oceanM·oceanG 등 cppdefs 옵션에 따라)

상세 — myroms.org wiki `build_roms.md` ([[roms-wiki-overview]] §2.1).

## 5. C-preprocessing 의 역할 — 운영 핵심

ROMS 의 가장 큰 특징:

> "ROMS uses C-preprocessing extensively to activate and/or deactivate ..." (Getting_Started.md 본문)

- 모든 옵션 (KPP vs MY25 vs GLS, advection scheme, sediment, biology 등) 은 **CPP 매크로** 로 활성/비활성
- 사용자 application 별 `cppdefs.h` 작성 → 컴파일 시 결정 → runtime 가변 X
- → **운영 결정의 75% 가 cppdefs.h 단계** 에서 끝남

상세 cppdefs 운영 가이드는 `roms-wiki-cppdefs.md` (예정 — M-C 후속).

## 6. 변수 메타데이터 — varinfo.yaml

> "a metadata variable definition file ([varinfo.yaml](/wiki/varinfo.yaml))" (Getting_Started.md)

ROMS 의 모든 NetCDF 변수 정의가 YAML 파일 한 곳에 모임. 출력 단위·long_name·standard_name 일관성.

## 7. 학습 권장 시퀀스

| 단계 | 자료 |
|---|---|
| 1. ROMS 개념 + 구조 | 본 노트 + Getting_Started.md |
| 2. Build 환경 | `build_roms.md` + `my_build_paths.md` |
| 3. CPP 옵션 결정 | `cppdefs.h.md` + `sediment_cppdefs.h.md` |
| 4. 입력 파일 (`.in`) | `Input_Parameter_Files.md` |
| 5. 격자 + bathymetry | `Grid_Generation.md` + `seagrid/easygrid` |
| 6. Vertical coord (S-coord) | `Vertical_S-coordinate.md` |
| 7. Vertical mixing 선택 | `Vertical_Mixing_Parameterizations.md` |
| 8. Boundary forcing | `Tidal_Forcing.md` + `Input_Parameter_Files.md` |
| 9. 첫 실행 → NetCDF 출력 | `Standard_Output_Files.md` |
| 10. (필요 시) 4DVar 동화 | `4DVar_Tutorial_Introduction.md` |
| 11. (필요 시) Nested grids | `Nested_Grids.md` |
| 12. (필요 시) Sediment | `sediment_cppdefs.h.md` + CSTMS 노트 |

## 8. 한국 적용

- **NIFS KOOS-EJS** — 한국 국립수산과학원 동해예측시스템 (ROMS 기반)
- 본 위키 — [[../../experience/nifs-vertical-sst-trends]] (NIFS 다층 수온 trend, ROMS forcing source)

## 9. 관련 자료

- [[roms-wiki-overview]] — 326 페이지 인덱스
- [[../source-analysis/roms_main_driver_dispatch]] — Drivers/ + Master/ 코드 매핑
- [[../source-analysis/roms_nonlinear_physics_modules]] — Nonlinear/ 6 subdirs
- [[../web-refs/roms-official-resources]] — Shchepetkin-McWilliams 2005·Haidvogel 2008
- 외부: [myroms.org/wiki/Getting_Started](https://www.myroms.org/wiki/Getting_Started)
