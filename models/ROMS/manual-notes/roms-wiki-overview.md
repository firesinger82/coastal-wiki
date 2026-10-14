---
title: "ROMS myroms.org wiki 종합 인덱스 — 326 페이지 + 토픽 클러스터링"
topic: roms-wiki-overview
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/manuals/wiki/manifest.json 직접 인용 (page_count: 326, fetched_at: 2026-05-03T14:20:20Z, site: myroms.org/wiki) + markdown/ 321 .md files 직접 ls — Getting_Started·build_roms·cppdefs.h·Vertical_Mixing_Parameterizations·Horizontal_Mixing·GLS_MIXING·Tidal_Forcing·Input_Parameter_Files·Standard_Output·Grid_Generation·Nested_Grids·sediment_cppdefs.h 등 핵심 토픽 directory 직접 확인. 2026-10-14 ROMS recovery 대조 보고서 반영."
note_author: "Claude Opus 4.7 (1M context)"
last_source_check: "2026-10-14 (recovery 대조 반영)"
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

mirror 수집 날짜와 코드 커밋은 서로 다른 판본 식별 정보이다. ([RMF1-968](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#4-노트-대조와-수정안))
위키 수집 날짜는 모든 쪽의 작성 시점을 보증하지 않는다. ([RMF1-968](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#4-노트-대조와-수정안))

## 2. 토픽 클러스터 (321 markdown 페이지)

### 2.1 Getting Started + Build

| 핵심 페이지 | 내용 |
|---|---|
| `Getting_Started.md` | ROMS 개관 + 디렉토리 구조 + C-preprocessing intro ([roms-wiki-getting-started](roms-wiki-getting-started.md)) |
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
- [I4DVAR](../raw/manuals/wiki/wikitext/I4DVAR.wiki)는 Incremental 4D-Var 설명 문서이다 (`I4DVAR.wiki:1`). 두 동화 옵션의 Options 원 절은 [I4DVAR](../raw/manuals/wiki/wikitext/Options.wiki#I4DVAR)와 [R4DVAR](../raw/manuals/wiki/wikitext/Options.wiki#R4DVAR)이다. [10-14 전수 검증 정정]
- `ADJOINT.md`, `ADM_DRIVER.md`, `AD_SENSITIVITY.md`. Options 원 절: [ADJOINT](../raw/manuals/wiki/wikitext/Options.wiki#ADJOINT), [ADM_DRIVER](../raw/manuals/wiki/wikitext/Options.wiki#ADM_DRIVER), [AD_SENSITIVITY](../raw/manuals/wiki/wikitext/Options.wiki#AD_SENSITIVITY).
- 고유모드와 강제 특이벡터 옵션은 Options의 [AFT_EIGENMODES](../raw/manuals/wiki/wikitext/Options.wiki#AFT_EIGENMODES)·[FT_EIGENMODES](../raw/manuals/wiki/wikitext/Options.wiki#FT_EIGENMODES)·[FORCING_SV](../raw/manuals/wiki/wikitext/Options.wiki#FORCING_SV)를 참조한다. [10-14 전수 검증 정정]
- 정규화는 [4DVar Normalization Tutorial](../raw/manuals/wiki/wikitext/4DVar_Normalization_Tutorial.wiki)을 참조한다. 상관 드라이버 옵션은 [CORRELATION](../raw/manuals/wiki/wikitext/Options.wiki#CORRELATION)을 참조한다. [10-14 전수 검증 정정]
- [RBL4D-Var Tutorial](../raw/manuals/wiki/wikitext/RBL4D-Var_Tutorial.wiki).
- [RBL4D-Var Analysis Observation Impact Tutorial](../raw/manuals/wiki/wikitext/RBL4D-Var_Analysis_Observation_Impact_Tutorial.wiki).
- [RBL4D-Var Analysis Observation Sensitivity Tutorial](../raw/manuals/wiki/wikitext/RBL4D-Var_Analysis_Observation_Sensitivity_Tutorial.wiki).
- [RBL4D-Var Forecast Observation Impact Tutorial](../raw/manuals/wiki/wikitext/RBL4D-Var_Forecast_Observation_Impact_Tutorial.wiki).
- [RBL4D-Var Forecast Observation Sensitivity Tutorial](../raw/manuals/wiki/wikitext/RBL4D-Var_Forecast_Observation_Sensitivity_Tutorial.wiki).

`IS4DVAR`는 [Variational Data Assimilation](../raw/manuals/wiki/wikitext/Variational_Data_Assimilation.wiki)로 리다이렉트한다. (`IS4DVAR.wiki:1`; [DA1-016·DA1-820](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md))
색인에 수록되었다는 사실을 수학식 검증 근거로 사용하지 않는다. ([DA1-820](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md#4-노트-대조와-수정안))

### 2.3 격자 + 입출력

| 페이지 | 내용 |
|---|---|
| `Grid_Generation.md` | 격자 생성 일반 |
| `Grid_Processing_Scripts.md` | 격자 후처리 스크립트 |
| `Nested_Grids.md` | nested (multi-grid) |
| `seagrid.md` | seagrid MATLAB 도구 |
| `easygrid.md` | ROMS 격자와 초기조건 파일을 만드는 Matlab 스크립트 |
| `Input_Parameter_Files.md` | input file (.in) family |
| `Standard_Output.md` | 표준 출력 로그의 예제 설명 |
| `Standard_Output_Files.md` | 관련 출력 문서의 색인 |
| `Standard_Output_File.md` | `Standard_Output_Files` 색인으로의 redirect |

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
- `ANA_BIOLOGY.md` (초기 상태 입력).
- `ANA_BPFLUX/BSFLUX/BTFLUX.md` (biology fluxes).

초기 상태 입력과 reaction 매개변수를 구분한다. ([NT-021](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안))
- `ANA_CLOUD.md`, `ANA_DIAG.md`
- `ANA_GRID.md` (analytical grid setup)
- (수십 더)

### 2.6 Vertical coordinate

| 페이지 | 내용 |
|---|---|
| `Vertical_S-coordinate.md` | S-coordinate (terrain-following) — ROMS 의 핵심 vertical 방식 |

지배식·좌표·수치 해법 원문은 [이론·수치 대조 보고서](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md)의 판·인용 위치와 함께 연결한다. ([RTN-404](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#4-노트-대조와-수정안))

- [Equations_of_Motion](../raw/manuals/wiki/wikitext/Equations_of_Motion.wiki).
- [Terrain-Following_Coordinate_Transformation](../raw/manuals/wiki/wikitext/Terrain-Following_Coordinate_Transformation.wiki).
- [Numerical_Solution_Technique](../raw/manuals/wiki/wikitext/Numerical_Solution_Technique.wiki).
- [Time-stepping_Schemes_Review](../raw/manuals/wiki/wikitext/Time-stepping_Schemes_Review.wiki).

### 2.7 격자 + bottom

| 페이지 | 내용 |
|---|---|
| `CURVGRID.md` | curvilinear grid |
| `BBL` 관련 | Bottom Boundary Layer (source-analysis 와 cross-ref) |

곡선좌표 변환 원문은 [Curvilinear_Coordinates_Transformation](../raw/manuals/wiki/wikitext/Curvilinear_Coordinates_Transformation.wiki)을 참조한다. ([RTN-404](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#4-노트-대조와-수정안))

## 3. 운영 cheat-sheet — Wiki 페이지 선택 가이드

| 작업 | 권장 wiki page |
|---|---|
| **신규 ROMS 첫 설치** | Getting_Started → build_roms |
| **CPP 옵션 결정** | cppdefs.h + Vertical_Mixing_Parameterizations + sediment_cppdefs.h |
| **격자 생성** | Grid_Generation + seagrid/easygrid + CURVGRID |
| **Nesting setup** | Nested_Grids + Grid_Processing_Scripts |
| **Boundary 설정** | Input_Parameter_Files + Tidal_Forcing + ADD_FSOBC/M2OBC + ANA_* |
| **출력 문서 탐색** | [Standard_Output_Files](../raw/manuals/wiki/wikitext/Standard_Output_Files.wiki) |
| **데이터 동화** | 4DVar_Tutorial_Introduction + I4DVAR + R4DVAR + Normalization + [RBL4D-Var Tutorial](../raw/manuals/wiki/wikitext/RBL4D-Var_Tutorial.wiki) + 위 §2.2의 분석·예보 영향·감도 쪽 |
| **민감도 분석** | ADJOINT + AD_SENSITIVITY + FT_EIGENMODES + [R4DVAR_ANA_SENSITIVITY](../raw/manuals/wiki/wikitext/Options.wiki#R4DVAR_ANA_SENSITIVITY) + [RBL4DVAR_ANA_SENSITIVITY](../raw/manuals/wiki/wikitext/Options.wiki#RBL4DVAR_ANA_SENSITIVITY) + [RBL4DVAR_FCT_SENSITIVITY](../raw/manuals/wiki/wikitext/Options.wiki#RBL4DVAR_FCT_SENSITIVITY) |

`Standard_Output_Files`에 표준 출력·평균·진단·이력·재시작 링크가 있다. ([OMD-N041](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#4-노트-대조와-수정안))
일반 수반 감도와 동화 관측 감도는 다른 드라이버다. ([RT2-405](../../../_staging/recovery/compare/roms-da-representer-vs-code.md#4-노트-대조와-수정안))
`Nested_Grids`의 이전 `Hweight` 예제와 현재 `nLweights`/`Lweight` 계약을 구분한다. ([RCN-1961](../../../_staging/recovery/compare/roms-coupling-nesting-parallel-vs-code.md#4-노트-대조와-수정안))

## 4. 본 위키 노트와 대조 보고서

| 노트·보고서 | 내용 |
|---|---|
| [roms-wiki-overview](roms-wiki-overview.md) (본 노트) | 326 pages 인덱스 |
| [roms-wiki-getting-started](roms-wiki-getting-started.md) | Getting_Started.md 본문 (디렉토리 구조 + C-pp intro) |
| [빌드·옵션·이력 대조](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md) | cppdefs.h CPP 옵션 대조 |
| [혼합·경계·강제 대조](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md) | KPP·MY25·GLS 대조 |
| [4D-Var 대조](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md) | 4D-Var 위키·코드 대조 |

## 5. ROMS Fortran source 매핑 (source-analysis 와 cross-ref)

| Wiki 페이지 | Fortran 모듈 |
|---|---|
| Getting_Started 디렉토리 구조 | [roms_main_driver_dispatch](../source-analysis/roms_main_driver_dispatch.md) (Drivers/) |
| cppdefs.h | (모든 Nonlinear/ + Drivers/ 코드의 활성화 매크로) |
| Vertical_Mixing_Parameterizations | [roms_vertical_mixing](../source-analysis/roms_vertical_mixing.md) |
| Tidal_Forcing | [roms_open_boundaries](../source-analysis/roms_open_boundaries.md) |
| Grid_Generation + CURVGRID | [roms_grid_metrics](../source-analysis/roms_grid_metrics.md) |
| 4DVar tutorials | [roms_4dvar](../source-analysis/roms_4dvar.md) + [동화 계산 흐름](../../../_staging/recovery/flow/ROMS-callflow-da.md#4-계산-흐름도) |
| Nested_Grids | [roms_nesting](../source-analysis/roms_nesting.md) + [Hweight·nLweights/Lweight 대조](../../../_staging/recovery/compare/roms-coupling-nesting-parallel-vs-code.md#4-노트-대조와-수정안) |
| ANA_* analytical | Functionals/ + Include/ |
| sediment_cppdefs | [roms_sediment](../source-analysis/sediment/roms_sediment.md) subdir + Nonlinear/Sediment/ |

I4는 매 외부 반복의 background·increment·analysis를 호출한다. (`ROMS/Drivers/i4dvar_roms.h:292-314`)
R4와 RBL은 `outer=0`의 background 뒤 외부 반복을 시작한다. (`ROMS/Drivers/r4dvar_roms.h:293-323`, `ROMS/Drivers/rbl4dvar_roms.h:295-325`; [RF2-032 수정안](../../../_staging/recovery/flow/ROMS-callflow-da.md#6-기존-노트-대조와-수정안))
최소화기 호출과 `zgrad0`·`cg_beta`·`px`의 생산·소비 위치는 [동화 계산 흐름 보고서 §8](../../../_staging/recovery/flow/ROMS-callflow-da.md#8-차이-결론)을 참조한다.

## 6. 관련 자료

- [ROMS 모델 정체 카드](../README.md).
- [roms-official-resources](../web-refs/roms-official-resources.md) — Shchepetkin-McWilliams 2005 + Haidvogel 2008 + Warner 2008 CSTMS 인용.
- [roms_main_driver_dispatch](../source-analysis/roms_main_driver_dispatch.md) — Drivers/ + Master/ ESMF.
- [roms_nonlinear_physics_modules](../source-analysis/roms_nonlinear_physics_modules.md) — Nonlinear/ 6 subdirs.
- [roms-wiki-getting-started](roms-wiki-getting-started.md) — Getting_Started 본문 verified.
- [위키 수집 manifest](../raw/manuals/wiki/manifest.json).

현재 판의 퇴적물·해빙·식생·굴 유생 대조는 [퇴적물·해빙·식생 보고서](../../../_staging/recovery/compare/roms-sediment-ice-vegetation-vs-code.md)를 참조한다. ([RN1-046](../../../_staging/recovery/compare/roms-sediment-ice-vegetation-vs-code.md#4-노트-대조와-수정안))
입력 자료의 근거 파일과 판독 범위는 [입력 대조 보고서](../../../_staging/recovery/compare/roms-inputs-vs-code.md#1-요약)를 참조한다. ([RI1-1058](../../../_staging/recovery/compare/roms-inputs-vs-code.md#4-노트-대조와-수정안))

## 문서와 코드 차이 (10-14 대조)

근거: [Representer 동화](../../../_staging/recovery/compare/roms-da-representer-vs-code.md#5-차이-결론), [출력·메타데이터](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#5-차이-결론), [이론·수치](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#5-차이-결론), [도구·가이드](../../../_staging/recovery/compare/roms-tools-guides-vs-code.md#5-차이-결론).

문서 판: ROMS 위키 wikitext, 2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json). 코드 판: 원본 저장소 HEAD `57aecf58`, 2026-09-18, roms-4.2 이후 4.3 개발.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| da-representer:RT2-404 | 동화 위키 선택 가이드 | `models/ROMS/manual-notes/roms-wiki-overview.md:113` ` \| **데이터 동화** \| 4DVar_Tutorial_Introduction + I4DVAR + R4DVAR + Normalization \| ` | `Master/roms_kernel.F:159` ` #elif defined RBL4DVAR && !defined SPLIT_RBL4DVAR `<br>`Master/roms_kernel.F:160` ` # include "rbl4dvar_roms.h" ` | C 문서 누락 | 데이터 동화 가이드에 RBL4D-Var Tutorial과 RBL4D-Var 분석·예보 영향·감도 쪽을 추가한다. |
| da-representer:RT2-405 | 감도 위키 선택 가이드 | `models/ROMS/manual-notes/roms-wiki-overview.md:114` ` \| **민감도 분석** \| ADJOINT + AD_SENSITIVITY + FT_EIGENMODES \| ` | `Master/roms_kernel.F:161` ` #elif defined RBL4DVAR_ANA_SENSITIVITY `<br>`Master/roms_kernel.F:162` ` # include "obs_sen_rbl4dvar_analysis.h" ` | C 문서 누락 | 동화 관측 감도의 분석·예보 드라이버를 일반 AD_SENSITIVITY와 구분해서 안내한다. |
| outputs-metadata:OMD-N040 | roms-wiki-overview.md:66 | `manual-notes/roms-wiki-overview.md:66` `\| &#96;Standard_Output.md&#96; + &#96;_File.md&#96; + &#96;_Files.md&#96; \| NetCDF 출력 표준 \|`<br>`Standard_Output.wiki:1` `<div class="title">ROMS Standard Output</div>`<br>`Standard_Output.wiki:2` `ROMS writes to the standard output, unit 6 by default. It writes a very complete set of diagnostics on startup so that you can check to make sure everything is in order. An example of this output for the BENCHMARK option is below. I will attempt to describe each section here, but it's a wiki, so fix what's wrong:`<br>`Standard_Output_Files.wiki:1` `<div class="title">Standard Output Files</div>`<br>`Standard_Output_Files.wiki:2` `*&#91;&#91;Standard Output&#93;&#93;`<br>`Standard_Output_Files.wiki:3` `*&#91;&#91;Averages&#93;&#93;`<br>`Standard_Output_Files.wiki:4` `**&#91;&#91;LSF Tides\|Least Squares Fit for ROMS Tides&#93;&#93;`<br>`Standard_Output_Files.wiki:5` `*&#91;&#91;Diagnostics&#93;&#93;`<br>`Standard_Output_Files.wiki:6` `*&#91;&#91;History&#93;&#93;`<br>`Standard_Output_Files.wiki:7` `*&#91;&#91;Restart&#93;&#93;`<br>`Standard_Output_File.wiki:1` `#REDIRECT &#91;&#91;Standard Output Files&#93;&#93;` | — | B 문서 오기 | Standard_Output은 표준 출력 로그의 예제 설명이다. Standard_Output_Files는 관련 출력 문서의 색인이며 Standard_Output_File은 그 색인으로의 redirect다. NetCDF 출력 표준이라는 설명을 표준 출력 로그 설명과 출력 문서 색인으로 고친다. |
| theory-numerics:RTN-404 | 위키 overview의 수치 원문 색인 | `models/ROMS/manual-notes/roms-wiki-overview.md:94` ``\| `Vertical_S-coordinate.md` \| S-coordinate (terrain-following) — ROMS 의 핵심 vertical 방식 \|`` | `ROMS/Nonlinear/set_depth.F:222` `              Hz(i,j,k)=z_w(i,j,k)-z_w(i,j,k-1)` | C 문서 누락 | 위키 overview에 이번 지배식·좌표·수치 해법 원문과 대조 보고서의 연결을 추가한다. |
| tools-guides:RTG-1982 | EASYGRID를 Python 도구로 쓴 노트 | `models/ROMS/manual-notes/roms-wiki-overview.md:64` ``\| `easygrid.md` \| easygrid Python 도구 \|``<br>`easygrid.wiki:3` `EASYGRID is a simple matlab script` | — | B 문서 오기 | EASYGRID는 ROMS 격자와 초기조건 파일을 만드는 Matlab 스크립트이다. |
