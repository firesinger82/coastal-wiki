---
title: "Delft3D 공유 지원 라이브러리 (utils_gpl / utils_lgpl) S-tier 개요"
model: Delft3D
component: utils_gpl, utils_lgpl
canonical_source: self
citation_status: verified
verification_method: "src/utils_gpl·utils_lgpl 트리를 find/wc/grep 로 전수 스캔(파일 수·라인 수 집계), 각 라이브러리 대표 파일을 직접 read — flow1d_implicit/SOFLOW.f90·FLINI.f90 헤더, morphology/bedcomposition_module.f90, flow1d/CrossSections.f90 (디렉토리), deltares_common/{properties,geometry_module,time_module,MessageHandling.F90}, delftio/dio-plt-rw.F90, io_netcdf/{io_ugrid,io_netcdf}.f90, ec_module/{ec_module,ec_converter}, nefis/{gp.c,README,doc/NEFIS5_structure_definition.txt}, io_hyd/read_hyd.f90, esmfsm/fortapi.f90 의 module 선언·주석·public 목록·라인번호 직접 확인. 인용 file:line 은 모두 read 결과에 근거."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/Delft3D/README.md
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/source-analysis/delft3d_sediment_morphology.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_data_io.md
---

# Delft3D 공유 지원 라이브러리 (utils_gpl / utils_lgpl) S-tier 개요

> Delft3D 소스 트리(`src/`)에서 개별 엔진(D-Flow FM·FLOW2D3D·WAQ·WAVE 등)이 공유하는 **지원 라이브러리** 군. `utils_gpl/`(GPL: 도메인 기능 라이브러리)와 `utils_lgpl/`(LGPL: 범용 유틸·IO·커플링 인프라)로 양분. 본 노트는 라이브러리별 **목적 + 대표 파일(file:line)** 의 S-tier 개요로, 전수 전사가 아니라 "어디에 무엇이 있는가"의 맵이다. 모듈 내부 알고리즘 deep-dive 는 해당 전용 노트로 링크.

## 0. 스코프와 집계

`find ... | wc -l` 로 측정한 라이브러리별 소스 파일 수(*.f90/*.F90, nefis/esmfsm 은 *.c 포함):

| 그룹 | 라이브러리 | 파일 수 | 역할 한 줄 |
|---|---|---:|---|
| utils_gpl | `flow1d_implicit/` | 623 | 1D 암시적 채널흐름 — SOBEK-RE 계열 엔진 |
| utils_gpl | `morphology/` | 79 | 형태변화(bed composition·표사·dredge) 커널·IO |
| utils_gpl | `flow1d/` | 35 | 1D 네트워크·단면·구조물 자료형 (현대 D-Flow 1D core) |
| utils_lgpl | `deltares_common/` | 113 | 공용 유틸 — 시간·기하·문자열·메시지·INI tree |
| utils_lgpl | `delftio/` | 87 | IO 추상화 — HIS/PLT·2D field·SOBEK 동기화 스트림 |
| utils_lgpl | `delftio` 외 `io_netcdf/` | 25 | NetCDF + UGRID 비정형격자 IO |
| utils_lgpl | `io_hyd/` | 40 | WAQ용 hydrodynamic(`.hyd`) coupling 파일 IO |
| utils_lgpl | `nefis/` | 35 | Deltares 자체 바이너리 포맷(NEFIS) C 라이브러리 |
| utils_lgpl | `ec_module/` | 36 | External forcings Coupling — 시·공간 보간 |
| utils_lgpl | `esmfsm/` | 16 | FSM — Fortran/C 공유메모리 포인터 관리 |

라이선스는 파일 헤더로 확인: `utils_lgpl/*` 는 모두 `LGPL ... version 2.1`(예: `delftio/.../dio-plt-rw.F90:6-7`, `deltares_common/.../properties.f90:7-8`), GPL 그룹은 `utils_gpl/`.

---

## 1. utils_gpl — 도메인 기능 라이브러리

### 1.1 flow1d_implicit (623) — SOBEK-RE 1D 암시적 채널흐름

최대 라이브러리. 헤더 주석이 출자를 명시: *"Rijkswaterstaat/RIZA and DELFT HYDRAULICS / One Dimensional Modelling System / S O B E K"* (`flow1d_implicit/src/SOFLOW.f90:34-36`). 즉 De Saint-Venant 방정식의 **암시적(implicit)** 1D 솔버 계열(SOBEK-RE) 이식.

| 파일 | 라인 | 내용 (verbatim 주석 근거) |
|---|---:|---|
| `flow1d_implicit/src/SOFLOW.f90` | 1152 | `SOFLOW (SObek FLOW main routine)` — "computes the waterlevels and discharges for the next time level", 수렴까지 flow module 반복 (`:39-49`) |
| `flow1d_implicit/src/FLINI.f90` | 860 | `FLINI (FLow INItialisation)` — 초기 수류 할당, restart/user/computed 3 옵션 (`:30-45`) |
| `flow1d_implicit/src/DLAPACK.f90` | 6463 | 번들 LAPACK (선형대수 — 암시적 행렬 풀이) |
| `flow1d_implicit/src/DBLASK.f90` | 2990 | 번들 BLAS |
| `flow1d_implicit/src/FLQLAT.f90` | 973 | lateral discharge 처리 |
| `sobeksim/src/SOINIT.f90` | 987 | 시뮬레이션 초기화 (sobeksim 하위 패키지) |
| `sobekre_dll/src/SobekREOpenMI.f90` | 1469 | OpenMI 커플링 DLL 진입점 |

서브패키지: `flow1d_implicit/`(코어 FL*/SO* 루틴 + 번들 LAPACK/BLAS), `sobeksim/`(드라이버), `sobekre_dll/`(OpenMI 래퍼). 변수명 관례: `FL*`=Flow 모듈, `SO*`=SObek 메인. 인터페이스에 `fm1dimp` 인자(`SOFLOW.f90:21`)가 있어 D-Flow FM 1D 와의 연결 지점 존재.

### 1.2 morphology (79) — 형태변화 커널·IO

bed level update + bed stratigraphy 관리. 4 서브패키지: `morphology_kernel/`(계산), `morphology_io/`(입력 파서), `morphology_data/`(자료형), `morphology_plugins_c/`(C 플러그인). 대표:

| 파일 | 라인 | 내용 |
|---|---:|---|
| `morphology_kernel/src/bedcomposition_module.f90` | 3853 | bed composition 추적 — "keeps track of the bed composition at one or more locations ... schematized using one or more layers" (`:32-35`); Lagrangian/Eulerian underlayer thickness (`:125-126`) |
| `morphology_kernel/src/eqtran.f90` | 834 | 평형 표사이송 공식 dispatcher |
| `morphology_kernel/src/dredge.f90` | 1665 | 준설/투기 커널 |
| `morphology_kernel/src/santoss.f90` | 492 | SANTOSS 파랑하 표사 공식 |
| `morphology_io/src/rdmor.f90` | 2374 | `.mor` morphology 입력 |
| `morphology_io/src/rdsed.f90` | 2315 | `.sed` sediment 입력 |
| `morphology_io/src/rdmorlyr.f90` | 2171 | layered bed 입력 |

> 커널 알고리즘(compute_sediment·erosilt·eqtran·compbsskin)·dredge 메커닉의 deep-dive 는 본 노트가 아니라 [`delft3d_sediment_morphology.md`](delft3d_sediment_morphology.md)·[`delft3d_sediment_transport_formulae.md`](delft3d_sediment_transport_formulae.md)·[`delft3d_dredge_dump.md`](delft3d_dredge_dump.md) 가 canonical. 여기서는 "라이브러리 위치 + 파일 맵" 만.

### 1.3 flow1d (35) — 현대 1D 네트워크 자료형

flow1d_implicit(SOBEK-RE 레거시)와 별개의 **현대 D-Flow 1D core**. 네트워크 위상·단면·구조물 객체 정의. 3 서브패키지: `flow1d_core/`·`flow1d_io/`·`flow1d/`.

| 파일 | 라인 | 내용 |
|---|---:|---|
| `flow1d_core/src/CrossSections.f90` | 3434 | 단면 자료형(tabulated/yz/circle 등) |
| `flow1d_core/src/Network.f90` | 1122 | 1D 네트워크(branch·node) 구조 |
| `flow1d_core/src/structures.f90` | 1045 | 구조물 기반 자료형 |
| `flow1d_core/src/general_structure.f90` | 1085 | general structure (weir/gate 일반화) |
| `flow1d_io/src/Readstructures.f90` | 1532 | 구조물 입력 파서 |
| `flow1d_io/src/readCrossSections.f90` | 981 | 단면 입력 파서 |

---

## 2. utils_lgpl — 범용 유틸·IO·커플링 인프라

### 2.1 deltares_common (113) — 공용 유틸 토대

거의 모든 엔진이 의존하는 기반. 단일 패키지 `deltares_common/src/`. 대표 모듈:

| 모듈 (`.../src/`) | 라인 | 역할 (public/주석 근거) |
|---|---:|---|
| `properties.f90` | 3294 | INI 형식 property 트리 read/write (`module properties` `:1`) — MDU/설정 파일 파싱 백본 |
| `tree_struct.f90` | 897 | 일반 트리 자료구조 (properties 의 하부) |
| `geometry_module.f90` | 2752 | 기하 연산 — `clockwise_sp`(`:166`), `pinpok`/point-in-polygon(`:256`,`:278`), `dbdistance`(`:479`), 구면(`jsferic`) 지원 |
| `time_module.f90` | 1447 | 날짜·시간 변환 — `ymd2modified_jul`·`mjd2date`·`parse_time`·`datetime2sec` 등 public(`:43-59`) |
| `string_module.f90` | 1248 | 문자열 유틸 |
| `MessageHandling.F90` | 1014 | 통합 로깅/에러 — 6 레벨 `LEVEL_DEBUG..LEVEL_FATAL`(`:132-138`), prefix `** WARNING:`/`** ERROR:` 등(`:141-145`), C 콜백 인터페이스(`:42`) |
| `tables.f90` / `m_tables.f90` / `table_handles.f90` | 1885/759/741 | 시계열·look-up 테이블 |
| `stdlib/stdlib_sorting_*.f90` | 4922 등 | Fortran stdlib 정렬 번들 |

### 2.2 delftio (87) — IO 추상화 (HIS/PLT, 동기 스트림)

Deltares "DelftIO" 추상 IO. 3 서브패키지: `diof90/`(Fortran 90 API), `diof90Nefis/`(NEFIS 백엔드), `delftio_sync/`(D3D↔SOBEK 동기화). 핵심 추상은 **PLT**(Parameter–Location–Time) 자료형 = HIS 시계열 출력의 모델:

| 파일 | 라인 | 내용 |
|---|---:|---|
| `diof90/dio-plt-rw.F90` | 5014 | `module Dio_plt_rw`(`:60`) — PLT 헤더 정의/조회, HIS/HIA/ASCII/BIN read·write (`:48-58` 주석 목록) |
| `diof90/dio-2dfield-rw.F90` | 1129 | `module Dio_2dfield_rw`(`:40`) — 2D field IO |
| `diof90/dio-streams.F90` | 958 | `module dio_streams`(`:39`) — 저수준 스트림 |
| `delftio_sync/d3d_sobek.f90` | 966 | D3D–SOBEK online 커플링 동기화 |
| `delftio_sync/d3d_sobek_conf.f90` | 1118 | 동 커플링 설정 |

### 2.3 io_netcdf (25) — NetCDF + UGRID 비정형격자 IO

D-Flow FM 출력의 표준 IO. 단일 패키지 + `io_netcdf_api/`. CF/UGRID 컨벤션 준수가 명문화:

| 파일 | 라인 | 내용 |
|---|---:|---|
| `io_netcdf/src/io_ugrid.F90` | 5893 | `module io_ugrid`(`:40`) — "reading and writing NetCDF files with UGRID-compliant data on unstructured grids" (`:34`); `CF-1.8`(`:60`)·`UGRID-1.0`(`:61`) 채택; netcell `t_face`(`:119`) |
| `io_netcdf/src/io_netcdf.f90` | 2310 | `module io_netcdf`(`:33`) — 컨벤션 선택형 상위 API, `ionc_*` 인터페이스, `IONC_CONV_{UGRID,CF,SGRID}`(`:46-50`) |
| `io_netcdf/src/coordinate_reference_system.F90` | 309 | CRS 처리 |

> D-Flow FM 측 IO 사용은 [`delft3d_dflowfm_data_io.md`](delft3d_dflowfm_data_io.md) 참조. 본 노트는 라이브러리 정체만.

### 2.4 io_hyd (40) — WAQ hydrodynamic coupling 파일

FLOW/FM → WAQ 로 흐름장을 넘기는 `.hyd` 기반 coupling IO. 비정형 격자 → WAQ aggregation 지원.

| 파일 | 라인 | 내용 |
|---|---:|---|
| `io_hyd/src/read_hyd.f90` | 622 | `subroutine read_hyd(hyd)` — "read a hydrodynamic description file"(`:30-31`), `t_hydrodynamics` 채움(`:46`) |
| `io_hyd/src/merge_domains.f90` | 1200 | 도메인 분할(병렬) 결과 병합 |
| `io_hyd/src/aggregate_waqgeom.f90` | 435 | WAQ 격자 aggregation |
| `io_hyd/src/hyd_waqgeom_mod_old.f90` | 1934 | WAQ geom (구버전) |

### 2.5 nefis (35) — Deltares 바이너리 포맷 (C 라이브러리)

NEFIS = Deltares 자체 self-describing 바이너리 파일 포맷(정의 파일 + 데이터 파일). 주로 **C** 구현이며 Fortran/C 양쪽 바인딩 제공. FLOW2D3D 의 `trim-`/`trih-`(map/history) 출력이 NEFIS.

| 파일 (`packages/nefis/src/`) | 라인 | 내용 |
|---|---:|---|
| `gp.c` | 1947 | "Read and write items to NEFIS data and definiton file" (`:30`) — element/cell/group 단위 get·put |
| `f2c.c` | 2621 | Fortran→C 바인딩 레이어 |
| `c2c.c` | 2498 | C 내부 레이어 |
| `oc.c` | 1459 | open/close 파일 관리 |
| `df.c` | 1310 | definition file 처리 |
| `doc/NEFIS5_structure_definition.txt` | — | 바이너리 레이아웃 명세(element/cell 버퍼 바이트 오프셋, `:1-30`) |

`packages/nefis_version_number/` 도 존재. README 빌드 노트 저자: *Jan Mooiman* (`nefis/README:7`).

### 2.6 ec_module (36) — External forcings Coupling (시·공간 보간)

경계조건·기상강제(wind/pressure/meteo)·시계열을 모델 격자/시각으로 **보간**해 공급하는 커플링 엔진. 단일 진입점 `tEcInstance` 패턴:

| 파일 (`ec_module/src/`) | 라인 | 내용 |
|---|---:|---|
| `ec_module.f90` | 774 | `module m_ec_module`(`:38`) — "main access point to the EC-module", 모든 상호작용은 `tEcInstance` 포인터 경유(`:29-32`); create 제네릭(FileReader/BCBlock/NetCDF/Quantity, `:67-89`) |
| `ec_converter.f90` | 3733 | Converter — interpolation type 관리(`ecConverterSetInterpolation` `:267`), spacetimeSaveWeightFactors·nearest_neighbour·triinterp2 (`:318`,`:382-431`) |
| `ec_filereader_read.F90` | 2345 | 강제 파일 reader |
| `ec_basic_interpolation.F90` | 1911 | 저수준 보간(triinterp2·nearest_neighbour) |
| `meteo/meteo.f90` | 1708 | 기상 강제 전용 |
| `ec_provider.F90` | 3896 | provider(source)–item–connection 그래프 |

구조: **provider/source → item → connection → converter(보간) → target(모델 quantity)**.

### 2.7 esmfsm (16) — FSM 공유메모리 포인터 관리

가장 작은 라이브러리. *"Delft-FSM (Fortran Shared Memory) / Interface between Fortran (the users of FSM) and C (the implementation)"* (`esmfsm/src/fsm/fortapi.f90:30-31`). 동적 메모리 풀에 이름 붙인 포인터 할당:

| Fortran API | → C | 역할 |
|---|---|---|
| `FSMINI` | `FSM_Init` | 초기화 (`fortapi.f90:34`,`:52`) |
| `MAKPTR` | `FSM_MakePointer` | named pointer 생성 (`:35`,`:68`) |
| `GETPTR` | `FSM_GetPointer` | 조회 (`:36`) |
| `RELPTR` | `FSM_ReleasePointer` | 해제 (`:37`) |
| `PRTKEY`/`FSMERR` | `FSM_PrintKeys`/`FSM_Err` | 디버그·에러 (`:38-39`) |

`esmfsm_version_number/` 패키지에 C 버전 헬퍼(f2c.c/c2c.c) 포함.

---

## 3. 의존 관계 요지

- **deltares_common** 은 거의 전 라이브러리·엔진의 토대(시간·기하·메시지·property tree).
- **io_netcdf(UGRID)** 는 D-Flow FM 출력, **nefis+delftio(PLT/HIS)** 는 FLOW2D3D(4) 출력의 IO 백엔드 — 즉 4세대(structured) vs FM(unstructured) IO 스택이 갈림.
- **ec_module** 은 모든 엔진의 강제/경계 보간 공통 게이트. **esmfsm** 은 레거시(FLOW2D3D) 공유메모리.
- **io_hyd** 는 hydrodynamics→WAQ 브릿지, **flow1d/flow1d_implicit** 은 1D 채널흐름(현대 vs SOBEK-RE) 코어.

## 4. 한계 / 미확인

- ⚠ 각 라이브러리의 내부 알고리즘(예: ec_module 보간 가중치 계산 세부, nefis 해시 인덱싱) deep-dive 는 본 개요 범위 밖 — 필요 시 별도 source-analysis 노트로 분리.
- 파일 수는 *.f90/*.F90/*.c 기준 `find` 집계값으로, 빌드 스크립트·헤더(.inc/.h)·테스트는 포함/제외가 라이브러리마다 다를 수 있음(nefis/esmfsm 은 C·테스트 포함 집계).
