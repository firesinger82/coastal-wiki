---
title: "ROMS 전역 상태 모듈 — mod_* global state (param/grid/ocean/mixing/forces/boundary/scalars/stepping/iounits)"
model: ROMS
component: ROMS/Modules
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Modules/). mod_param.F(차원·T_BOUNDS·T_DOMAIN), mod_ocean.F(T_OCEAN 상태변수 allocate/initialize), mod_grid.F(T_GRID metric), mod_stepping.F(시간 인덱스), mod_scalars.F(time/dt/g/rho0), mod_mixing/forces/boundary/iounits.F(파생타입), mod_arrays.F(allocate orchestrator) 를 file:line 인용. 2026-10-14 ROMS recovery 대조 보고서 반영"
last_source_check: 2026-10-14 (recovery 대조 반영)
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_support_modules.md
  - models/ROMS/README.md
---

# ROMS 전역 상태 모듈 — mod_* global state

> ROMS 의 모든 격자·상태변수·구성 스칼라를 담는 Fortran MODULE 집합 (경로: roms/ROMS/Modules/). 각 모듈은 nested grid 배열 `(ng)` 로 인덱싱되는 파생타입(derived type)을 정의하고, `allocate_*`/`initialize_*`/`deallocate_*` 3종 루틴을 export 한다.

이 노트는 **전역 상태 자료구조(차원·격자·상태변수·스칼라·시간인덱스)** 에 집중한다. 지원·유틸리티 성격 모듈(`mod_kinds`, `mod_parallel`, `mod_strings` 등)은 기존 [roms_support_modules](roms_support_modules.md) 참조. NetCDF I/O 메타(`mod_ncparam`, `mod_netcdf`) 와 물리 패키지별 상태(`mod_biology`, `mod_sediment`, `mod_bbl`, `mod_tides`)는 각 도메인 노트로 분리.

## 0. 공통 설계 패턴

현재 `ROMS/Modules`의 `.F` 파일은 38개이다 ([build-options-history:RBH-3506](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md)).
수량은 HEAD `57aecf58`의 `*.F` 파일 목록에서 센 값이다 ([build-options-history:RBH-3506](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md)).
핵심 상태 모듈의 공통 관용:

1. `#include "cppdefs.h"` 로 시작, 모든 라이선스 헤더는 `!=== Hernan G. Arango ===` 블록 (예: `mod_param.F:5`, `mod_ocean.F:5`).
2. 파생타입 `T_XXX` 를 정의하고, **nested grid 차원** allocatable 배열 `TYPE(T_XXX), allocatable :: XXX(:)` 를 모듈 전역에 선언 — 예: `OCEAN(:)` (`mod_ocean.F:364`), `GRID(:)` (`mod_grid.F:365`), `MIXING(:)` (`mod_mixing.F:399`), `FORCES(:)` (`mod_forces.F:563`), `BOUNDARY(:)` (`mod_boundary.F:763`).
3. 멤버는 거의 전부 `real(r8), pointer :: var(:,:,...)` — allocatable 이 아니라 **pointer** (nesting/contact point 에서 재지정·공유 필요).
4. 3 루틴 PUBLIC: `allocate_*`/`deallocate_*`/`initialize_*` (예: `mod_ocean.F:76-78`).
5. `initialize_*` 는 **first-touch 정책** 으로 0 초기화 — shared-memory 에서 thread 별 메모리 지역성(NUMA) 확보 (`mod_ocean.F:1567-1571` "using first touch distribution policy ... performs propagation of the shared arrays across the cluster").

전체 할당은 `mod_arrays.F` 의 `ROMS_allocate_arrays` 가 grid 루프에서 각 모듈 `allocate_*` 를 순차 호출하는 방식으로 오케스트레이션된다 (`mod_arrays.F:127`, 호출 본문 `:180-224`).

## 1. mod_param — 차원·파티션·파생타입 부모

`mod_param.F` 는 격자·구성·상태벡터 크기 파라미터를 정의한다(`mod_param.F:11-50`). `USE mod_kinds` 만 의존 (`mod_param.F:99`

### 1.1 격자 차원 (nested grid 배열)

| 변수 | 의미 | file:line |
|---|---|---|
| `Ngrids` | nested/connected grid 수 | `mod_param.F:113` |
| `Lm(:)` | XI 방향 내부 격자점 수 | `mod_param.F:455` |
| `Mm(:)` | ETA 방향 내부 격자점 수 | `mod_param.F:456` |
| `Im(:)`,`Jm(:)` | 전역 격자점 수 (XI/ETA) | `mod_param.F:465-466` |
| `N(:)` | 연직 레벨 수 | `mod_param.F:479` |
| `NtileI(:)`,`NtileJ(:)` | 도메인 분할 타일 수 | `mod_param.F:677-678` |

주석 정의: `Lm/Mm` = "Number of interior grid points" (`mod_param.F:17-19`), `N` = "Number of vertical levels for each nested grid" (`mod_param.F:21`).

### 1.2 추적자(tracer) 차원

`NAT`(능동, 보통 2=θ,S; `mod_param.F:499`, 정의 `:63-64`), `NT(:)`(총 추적자, `mod_param.F:489`), `MT`(최대 추적자, `mod_param.F:490`). 정의 주석 `mod_param.F:61-76` — `NST=NCS+NNS`(퇴적), `NPT`(passive), `NBT`(생물). 추적자 **이름 인덱스**(`itemp`,`isalt`)는 여기가 아니라 `mod_ncparam.F` 에 있다 (`idTvar(:)` 등 `mod_ncparam.F:635`).

현재 `NBT`는 선택한 생물 모듈이 설정하는 scalar integer다 (`ROMS/Modules/mod_param.F:509`; [biology:NT-024](../../../_staging/recovery/compare/roms-biology-vs-code.md)).
`NT(ng)`와 `NBT`를 같은 차원의 배열로 설명하지 않는다 ([biology:NT-024](../../../_staging/recovery/compare/roms-biology-vs-code.md)).
전체 추적자 수는 `NT(ng)=NAT+NBT+NST+NPT`로 계산한다 (`ROMS/Modules/mod_param.F:1642`).
현재 코드는 `MT=MAX(1,MAX(NAT,MAXVAL(NT)))`를 사용한다 (`ROMS/Modules/mod_param.F:1694`; [outputs-metadata:OMD-N032](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md)).

### 1.3 타일 경계 파생타입 — T_BOUNDS / T_IOBOUNDS / T_DOMAIN

`mod_param.F` 는 병렬 타일링의 핵심 인덱스 컨테이너를 정의:

- `T_BOUNDS` (`mod_param.F:162-230`): 타일별 하한/상한 `LBi/UBi/LBj/UBj` (`:165-168`), 계산 루프 시작/끝 `Istr/Iend/Jstr/Jend` (`:175-178`), RHO/U/V 변형 `IstrR/IstrU/JstrV` (`:180-186`), open-boundary(`B`/`M`) 및 nesting(`P`/`T`) 인덱스 (`:188-204`), halo 인덱스 `Istrm3..Iendp3` (`:206-214`). 전역 인스턴스 `BOUNDS(:)` (`mod_param.F:232`). 인덱스 산출 루틴은 `Utility/get_bounds.F` 의 `var_bounds` (`mod_param.F:150-151` 주석 참조).
- `T_IOBOUNDS` (`mod_param.F:241-280`): NetCDF I/O 용 PSI/RHO/U/V 별 lower/upper bound + 점 수 (`xi_rho`,`eta_rho` 등). 인스턴스 `IOBOUNDS(:)` (`:282`).
- `T_DOMAIN` (`mod_param.F:292-327`): 타일이 도메인 가장자리에 접하는지 논리 스위치 `Eastern_Edge`/`Western_Edge`/.../ 코너 `NorthEast_Corner` (`:293-301`) + 타일 분수좌표 min/max. 인스턴스 `DOMAIN(:)` (`:329`).

### 1.4 메모리 추정

`Dmem(:)`(동적 메모리 요구, 배열 원소 수; `mod_param.F:137`)와 `BmemMax(:)`(분산메모리 버퍼 최대, bytes; `:132`). 각 `allocate_*` 가 할당 시 `Dmem(ng)=Dmem(ng)+...` 로 누적 (예: `mod_ocean.F:460`).

## 2. mod_ocean — 예후(prognostic) 상태변수 T_OCEAN

ROMS 의 **핵심 상태벡터**. `T_OCEAN` 구조체 (`mod_ocean.F:84-362`), 전역 `OCEAN(:)` (`mod_ocean.F:364`).

### 2.1 비선형(NLM) 상태변수

| 멤버 | 의미 | 단위 | 차원 | file:line |
|---|---|---|---|---|
| `zeta(:,:,3)` | 자유표면 | m | 2D×3 시간레벨 | 선언 `mod_ocean.F:93`, alloc `:413` |
| `ubar/vbar(:,:,3)` | 수심 평균 속도 | m/s | 2D×3 | 선언 `:91-92`, alloc `ROMS/Modules/mod_ocean.F:408,411`; [theory-numerics:RTN-371](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md) [10-14 전수 검증 정정] |
| `u/v(:,:,N,2)` | 3D 운동량 성분 | m/s | 3D×2 시간레벨 | 선언 `:113,115`, alloc `ROMS/Modules/mod_ocean.F:462,468` |
| `t(:,:,N,3,NT)` | 추적자(능동+수동) | — | 3D×3×NT | 선언 `:112`, alloc `ROMS/Modules/mod_ocean.F:459` |
| `rho/pden(:,:,N)` | 1000 kg/m³ 기준 밀도·위치밀도 편차 | kg/m³ | 3D | 선언 `:108-109`, alloc `pden :447`,`rho :450`; [theory-numerics:RTN-391](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md) [10-14 전수 검증 정정] |
| `W(:,:,0:N)` | S좌표 연직속도 ω·Hz/(mn) | m³/s | 3D(0:N) | 선언 `:117`, 주석 `:34` |
| `ru/rv(:,:,0:N,2)` | `k=1..N`은 rho-level 운동량 RHS이다. `k=0`은 2D/3D 결합 forcing 이력을 저장한다. | m⁴/s² | `0:N×2` | alloc `ROMS/Modules/mod_ocean.F:453,456`; [theory-numerics:RTN-372](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md) |
| `rubar/rvbar/rzeta(:,:,2)` | 2D RHS | — | 2D×2 | 선언 `:88-90`, alloc `ROMS/Modules/mod_ocean.F:399,402,405` |

자유수면 `zeta`와 수심 평균 속도 `ubar`·`vbar`는 시간레벨 3개를 가진다 (`ROMS/Modules/mod_ocean.F:408,411,414`; [callflow-nonlinear:N-04](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md)). [10-14 전수 검증 정정]
3D 운동량은 시간레벨 2개를 가진다 (`ROMS/Modules/mod_ocean.F:462,468`).
추적자 `t`는 시간레벨 3개를 가진다 (`ROMS/Modules/mod_ocean.F:459`의 `,3,NT(ng)`).
`ru`와 `rv`는 `0:N` 범위를 할당한다 (`ROMS/Modules/mod_ocean.F:453,456`).
`SOLVE3D`의 Legacy 경로는 첫 짧은 예측 단계에서 깊이 적분 3D 우변과 2D 우변의 차이를 느린 강제력으로 만든다 (`ROMS/Nonlinear/step2d_LF_AM3.h:2306,2359–2362,2388–2391`).
0번 층은 이 강제력의 시간 이력을 저장하고 다음 큰 단계의 외삽에서 읽는다 ([callflow-nonlinear:RF1-032](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md)).
배열의 `0:N` 차원만으로 0번 층을 수직 face의 운동량 우변으로 해석할 수 없다 ([callflow-nonlinear:RF1-032](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md)).
FB AB3-AM4의 4슬롯 제어와 현재 3슬롯 2D 배열의 불일치는 [callflow-nonlinear:RF1-002](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md)를 참조한다 ([callflow-nonlinear:N-04](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md)).

상태변수 정의 주석은 `mod_ocean.F:11-34` 에 단위까지 명시 — 예: `zeta` = "Free surface (m)" (`:18`), `W` = "S-coordinate (omega*Hz/mn) vertical velocity (m3/s)" (`:34`).

선형 식에서 `R0`부터 시작한 값은 `-1000` 대입 전의 물리 밀도이다 (`ROMS/Nonlinear/rho_eos.F:699–703,716`).
최종 `rho`와 `pden`은 1000 kg/m³ 기준 편차이다 ([theory-numerics:RTN-391](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md)).

### 2.2 데이터동화 다중 상태 (TL/AD/representer)

`T_OCEAN`은 해당 전처리 조건에서 4D-Var용 접선선형(`tl_`)·수반(`ad_`)·forcing(`f_`) 사본을 함께 보유한다 (`ROMS/Modules/mod_ocean.F:157,176-177,227-228,313`). 할당 예는 `tl_zeta`의 560줄과 `tl_t`의 607줄이다. 관련 메커닉은 [roms_adjoint_framework](roms_adjoint_framework.md)·[roms_4dvar](roms_4dvar.md)를 참조한다. [10-14 전수 검증 정정]

4D-Var의 Lanczos 벡터는 이 상태 배열을 사용한다 ([da-4dvar:DA1-810](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md)).
최소화 좌표는 v-space로 변환한다 ([da-4dvar:DA1-810](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md)).

### 2.3 WEC·생물·기타 조건부 멤버

`#ifdef WEC` Stokes 속도 `ubar_stokes`/`u_stokes`/`W_stokes` (`mod_ocean.F:104-105,123-125`, 정의 주석 `:60-67`) → [roms_wec](roms_wec.md). `#ifdef WEC_VF` quasi-static `zetat/zetaw/qsp/bh` (`:98-101`). `TIDE_GENERATING_FORCES` 시 `eq_tide` (`:95`).

### 2.4 초기화 (first-touch)

`initialize_ocean(ng,tile,model)` (`mod_ocean.F:1563`): `IniVal=0.0_r8` (`:1588`) 로 타일 범위 전체를 0 대입 (`:1631-1639` ...). `#include "set_bounds.h"` 로 타일 인덱스 설정 (`:1590`), `#ifdef DISTRIBUTE` 분기로 분산메모리 시 전체 LBi:UBi 범위 사용 (`:1594-1596`).

## 3. mod_grid — 격자 metric T_GRID

`T_GRID` (`mod_grid.F:175-363`), 전역 `GRID(:)` (`mod_grid.F:365`).

### 3.1 수평 metric·좌표

| 멤버 | 의미 | file:line |
|---|---|---|
| `h(:,:)` | 바닥 수심 (m, RHO점) | 선언 `mod_grid.F:201`, 주석 `:44` |
| `f(:,:)` | Coriolis 파라미터 (1/s) | `:198`, 주석 `:40` |
| `pm/pn(:,:)` | 좌표변환 metric m,n (1/m) | `:220-221`, 주석 `:63-69` |
| `angler(:,:)` | XI축↔진북 각 (rad) | `:185`, 주석 `:28-29` |
| `lonr/latr(:,:)` | RHO점 경위도 | `:207,203` |

`dmde/dndx`(metric 미분, `mod_grid.F` 주석 `:36-39`), `om_*`/`on_*`(격자 간격), 복합항 `pmon_*`/`pnom_*`(주석 `:65-74`) 도 보유.

### 3.2 연직 좌표 (SOLVE3D)

`#ifdef SOLVE3D` (`mod_grid.F:246`): `Hz(:,:,N)`(RHO 셀 두께 m, `:247`, 주석 `:14`), `z_r/z_w(:,:,...)`(RHO/W점 깊이, `:255,257`), `Huon/Hvom`(전운동량 flux 항 Hz·u/pn, Hz·v/pm; `:251-252`, 주석 `:19-20`), `z0_r/z0_w`(`:253-254`). `ADJUST_BOUNDARY` 시 `Hz_bry` (`:249`).

### 3.3 마스킹 (MASKING)

`#ifdef MASKING` (`mod_grid.F:263`): `pmask/rmask/umask/vmask` (`:264-267`) — 0=Land,1=Sea (PSI 는 2=no-slip). 주석 정의 `mod_grid.F:75-80`. 시간평균/진단/wet-dry 변형 마스크(`rmask_avg`,`rmask_dia`,`rmask_wet`)도 조건부 (`:81-95`).

## 4. mod_stepping — 시간 인덱스

`mod_stepping.F` 는 **상태배열의 시간레벨 인덱스**를 grid 별로 보유 (모든 변수 allocatable `(:)`, `allocate_stepping(Ngrids)` `:115`).

- Barotropic(빠른) 2D 인덱스: `knew/krhs/kstp` (`mod_stepping.F:64-66`, 주석 `:25-31`). `OCEAN%zeta(:,:,1:3)` 의 1/2/3 슬롯을 가리킴.
- Baroclinic(느린) 3D 인덱스: `nnew/nrhs/nstp` (`:69-71`, 주석 `:39-45`). `OCEAN%u(:,:,:,1:2)`, `OCEAN%t(:,:,:,1:3,:)` 슬롯 선택.
- 모두 `!$OMP THREADPRIVATE` (`:67,72`) — 스레드별 사본.
- 데이터동화 인덱스 `Lnew/Lold`(`:106-107`), `Lbinp/Lbout`(`ADJUST_BOUNDARY`, `:96-97`), `Lfinp/Lfout`(`:102-103`). Float 인덱스 `nf/nfp1/nfm1..3`(`FLOATS`, `:76-80`). 조석 `NTC`(`:110`).

시간 슬롯의 회전과 적분식은 구분한다 ([theory-numerics:RTN-383](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md)).
2D 기본 경로는 LF-AM3이다 ([theory-numerics:RTN-383](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md)).
3D 운동량은 AB3의 n·n-1·n-2 기여를 조립한다 (`ROMS/Nonlinear/pre_step3d.F:16–19`; `ROMS/Nonlinear/step3d_uv.F:347–360`; [theory-numerics:RTN-383](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md)). [10-14 전수 검증 보완]
적분 메커닉은 [roms_baroclinic_3d](roms_baroclinic_3d.md)·[roms_barotropic_2d](roms_barotropic_2d.md)를 참조한다.

## 5. mod_scalars — 구성 스칼라·물리상수

가장 큰 스칼라 컨테이너 (`mod_scalars.F`, 165 KB). 핵심:

### 5.1 시간 제어

`time(:)`(초)·`tdays(:)`(일) (`mod_scalars.F:265-266`, THREADPRIVATE `:267`), 시간스텝 `dt(:)`·`dtfast(:)` (`:273-274`), 스텝 카운터 `iic(:)`(NLM 시간스텝 인덱스, `:253`)·`iif(:)`(barotropic, `:254`), `ndtfast(:)`/`nfast(:)`(`:262-263`), `ntimes(:)`(현재 실행의 길이, `:340`), `ntstart(:)`/`ntend(:)`(`:382-383`), 재시작 레코드 `nrrec(:)` (`ROMS/Modules/mod_scalars.F:1200`). [10-14 전수 검증 정정]

`ntimes`는 현재 실행의 길이를 나타낸다 ([inputs:RI1-1054](../../../_staging/recovery/compare/roms-inputs-vs-code.md)).
재시작의 시작 단계는 `ntstart(ng)=NINT((time(ng)-dstart*day2sec)/dt(ng))+1`로 계산한 뒤 `IF (ntstart(ng).lt.1) ntstart(ng)=1`을 적용한다 (`ROMS/Utility/get_state.F:436–437`; [inputs:RI1-1054](../../../_staging/recovery/compare/roms-inputs-vs-code.md)). [10-14 전수 검증 정정]
재시작에서도 종료 단계는 `ntend(ng)=ntstart(ng)+ntimes(ng)-1`로 계산한다 (`ROMS/Utility/get_state.F:438`).

### 5.2 물리 상수

| 상수 | 값 | file:line |
|---|---|---|
| `g` | 9.81 m/s² (`#ifdef SOLITON` 시 비차원 1.0) | `mod_scalars.F:470` (SOLITON 분기 `:468`) |
| `rho0` | 1025.0 kg/m³ (선언 초기값) | `ROMS/Modules/mod_scalars.F:806` |
| `Eradius` | 6371315.0 m | `:463` |
| `pi` | 3.14159265358979… (parameter) | `:834` |
| `deg2rad` | pi/180 | `:835` |

복합항 `gorho0=g/rho0` 는 런타임 계산 (`mod_scalars.F:4560`).

`RHO0` runtime 입력이 `rho0`의 선언 초기값을 바꾼다 (`ROMS/Utility/read_phypar.F:1015–1017`).
TEST_CHAN 입력 예는 998.0 kg/m³다 (`ROMS/External/roms_test_chan.in:427`; [testcases:RT1-1535](../../../_staging/recovery/compare/roms-testcases-vs-code.md)).

### 5.3 종료 코드

`exit_flag`(초기 0, `mod_scalars.F:570`) 와 코드표 주석 `:559-568`: 1=Blows up, 2=Input error, 3=Output error, 7=Illegal input parameter, 8=Fatal algorithm result 등. NaN/blow-up 검출 시 드라이버가 이 값으로 종료를 결정 → [roms_main_driver_dispatch](roms_main_driver_dispatch.md).

## 6. mod_mixing / mod_forces / mod_boundary

### 6.1 mod_mixing — 혼합계수 T_MIXING

`T_MIXING` (`mod_mixing.F:153-397`), `MIXING(:)` (`:399`). 연직 혼합계수 `Akv(:,:,0:N)`(운동량)·`Akt(:,:,0:N,NAT)`(추적자)의 할당은 `ROMS/Modules/mod_mixing.F:548,551`에 있다. 난류 닫힘(GLS/MY2.5)·수평혼합 변수도 다수 보유. 알고리즘은 [roms_vertical_mixing](roms_vertical_mixing.md)·[roms_horizontal_mixing](roms_horizontal_mixing.md) 참조. [10-14 전수 검증 보완]

### 6.2 mod_forces — 표면/바닥 강제력 T_FORCES

`T_FORCES` (`mod_forces.F:210-561`), `FORCES(:)` (`:563`). 표면 운동량 응력 `sustr/svstr(:,:)` (`:214-215`), 바닥 응력 `bustr` (`:225`), 표면 추적자 flux `stflx(:,:,NT)` (선언 `:430`, 할당 `ROMS/Modules/mod_forces.F:929`). 대기강제·bulk flux 메커닉은 [roms_atmospheric_forcing](roms_atmospheric_forcing.md)·[roms_bulk_flux_coare](roms_bulk_flux_coare.md) 참조. [10-14 전수 검증 보완]

### 6.3 mod_boundary — 개방경계 강제 T_BOUNDARY + LBC_apply

두 파생타입:
- `T_APPLY` (`mod_boundary.F:387-392`): 경계점별 적용 스위치 `west/east/south/north` 논리배열. 인스턴스 `LBC_apply(:)` (`:394`). nesting composite grid 에서 nesting 처리 점은 FALSE 로 mixed BC 허용 (`:381-385` 주석).
- `T_BOUNDARY` (`mod_boundary.F:400-761`), `BOUNDARY(:)` (`:763`): 경계별 강제값 `zeta_west(:)`(`:404`), `u_west(:,:)`(`:515`), `t_west(:,:,NT)`(선언 `:585`, 할당 `ROMS/Modules/mod_boundary.F:1462`) 등 4 방향×변수. `CELERITY_READ` 또는 `CELERITY_WRITE` 조건에서 위상속도 사본 `zeta_west_Cx` 등을 선언한다 (`ROMS/Modules/mod_boundary.F:405-408`). LBC 적용 메커닉은 [roms_open_boundaries](roms_open_boundaries.md) 참조. [10-14 전수 검증 정정]

## 7. mod_iounits — I/O 파일 구조 T_IO

`T_IO` (`mod_iounits.F:170-192`): 입출력 파일의 식별자·레코드·시간범위·파일명 등 관리 정보를 압축 보관(`mod_iounits.F:165-193`) — `IOtype`/`Nfiles`/`Fcount`(multi-file 카운터, `:168-170`), `Rindex`(NetCDF 레코드, `:172`), `ncid`(`:173`), 변수ID 포인터 `Vid/Tid`(`:175-176`), 시간범위 `time_min/time_max`(`:177-178`), 파일명 `base/name/files`(`:181-183`). `PIO_LIB` 시 PIO descriptor `pioFile/pioVar` (`:184-188`). HIS/AVG/RST 등 출력 종류마다 `TYPE(T_IO) :: HIS(Ngrids)` 형태로 인스턴스화 (`:160-165` 주석).

`HIS`·`AVG`·`RST`는 `Ngrids` 축을 가진다 ([outputs-metadata:OMD-N049](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md)).
`BRY`·`CLM`·`FRC`는 추가 `max_Ffiles` 축을 가진다 (`ROMS/Modules/mod_iounits.F:272,282,292`; 할당 `ROMS/Utility/read_phypar.F:4283,4321,4373`; [outputs-metadata:OMD-N049](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md)). [10-14 전수 검증 보완]

## 8. mod_arrays — 할당 오케스트레이터

`ROMS_allocate_arrays(allocate_vars)` (`mod_arrays.F:127`): 대상 상태 모듈의 `allocate_*` 를 CPP 조건에 따라 `ONLY` import (`mod_arrays.F:24-55`; `mod_fourdvar`는 이 구간에서 deallocate·initialize만 import) 한 뒤, grid 루프 `DO ng=1,Ngrids` (`:168`) 안에서 타일 경계 `LBi..UBij` 를 `BOUNDS(ng)` 에서 추출(`:170-175`)하고 순차 호출 — `allocate_boundary`(`:182`)→`allocate_forces`(`:202`)→`allocate_grid`(`:203`)→`allocate_mixing`(`:208`)→`allocate_ocean`(`:209`) ... `$OMP MASTER`/`$OMP BARRIER` 로 마스터 스레드만 할당 (`:169,225-226`). 완료 시 `LallocatedMemory=.TRUE.` (`:252`). `NESTING` 시 contact point 구조는 `LBC_apply` 할당 후로 지연 (`:229-236`). 짝 루틴 `ROMS_deallocate_arrays`(`:273`)·`ROMS_initialize_arrays`(`mod_arrays.F:115` PUBLIC).

## 9. 요약 — 상태 흐름

```
mod_param (차원 Lm/Mm/N/NT, BOUNDS 타일 인덱스)
   │ ROMS_allocate_arrays (mod_arrays.F:127)
   ▼
OCEAN(ng)%{zeta,ubar,u,v,t,rho,W}   ← 예후 상태 (mod_ocean)
GRID(ng)%{h,f,pm,pn,Hz,z_r,*mask}   ← 격자 metric (mod_grid)
MIXING/FORCES/BOUNDARY(ng)          ← 혼합·강제·경계
   │ 시간레벨 회전: kstp/krhs/knew (2D), nstp/nnew (3D)  (mod_stepping)
   │ 스칼라: time/dt/g/rho0/exit_flag                    (mod_scalars)
   ▼
시간적분 (Nonlinear/main3d) — 메커닉은 [roms_baroclinic_3d](roms_baroclinic_3d.md) 등
```

## ⚠ 범위 밖 (다른 노트)

- 일반 `load` 경로는 YAML 메타데이터를 `Vname`·`Iinfo`·`Fscale`에 연결한다 (`ROMS/Utility/get_metadata.F:972–981`, `ROMS/Modules/mod_ncparam.F:2646–2657`).
- `SEDIMENT` 또는 `BBL_MODEL`의 mud 클래스 생성은 `NCS.gt.0`에서 별도 처리한다 (`ROMS/Nonlinear/Sediment/sediment_var.h:135–156`, `ROMS/Modules/mod_ncparam.F:2633–2634`).
- 이 경로는 `load=.FALSE.`로 일반 복사를 건너뛴다 (`ROMS/Nonlinear/Sediment/sediment_var.h:136`).
- `Vname(6)` 생성 누락 후보는 OMD-K029의 출력 조건과 중간 강도 판정을 따른다 ([outputs-metadata:OMD-N033](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md)).
- `mod_average`(시간평균 누산기)·`mod_diags`(진단)·`mod_coupling`(2D↔3D 결합항) → 미작성, source-needed.
- 병렬 `mod_parallel`·종류 `mod_kinds`(r8/dp 정의)·`mod_storage` → [roms_support_modules](roms_support_modules.md).

## 문서와 코드 차이 (10-14 대조)

결론 출처: [biology](../../../_staging/recovery/compare/roms-biology-vs-code.md), [build-options-history](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md), [callflow-nonlinear](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md), [inputs](../../../_staging/recovery/compare/roms-inputs-vs-code.md), [outputs-metadata](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md), [testcases](../../../_staging/recovery/compare/roms-testcases-vs-code.md), [theory-numerics](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md), [tools-guides](../../../_staging/recovery/compare/roms-tools-guides-vs-code.md).

문서 판: ROMS 위키 wikitext, 2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json). 코드 판: 원본 저장소 HEAD `57aecf58`, 2026-09-18, roms-4.2 이후 4.3 개발.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| biology:NT-024 | NBT 및 전체 tracer 차원 | `N/roms_global_state_modules.md:53` `` `NAT`(능동, 보통 2=θ,S; `mod_param.F:499`, 정의 `:63-64`), `NT(:)`(총 추적자, `mod_param.F:489`), `MT`(최대 추적자, `mod_param.F:490`). 정의 주석 `mod_param.F:61-76` — `NST=NCS+NNS`(퇴적), `NPT`(passive), `NBT`(생물). 추적자 **이름 인덱스**(`itemp`,`isalt`)는 여기가 아니라 `mod_ncparam.F` 에 있다 (`idTvar(:)` 등 `mod_ncparam.F:635`). `` | `ROMS/Modules/mod_param.F:509` `      integer :: NBT = 0`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:184` `#ifdef CARBON`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:185` `# ifdef OXYGEN`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:186` `#  if defined PO4 && defined RIVER_DON`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:187` `      NBT=15`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:188` `#  elif defined RIVER_DON && !defined PO4`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:189` `      NBT=14`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:190` `#  elif defined PO4 && !defined RIVER_DON`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:191` `      NBT=13`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:192` `#  else`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:193` `      NBT=12`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:194` `#  endif`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:195` `# else`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:196` `#  if defined PO4 && defined RIVER_DON`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:197` `      NBT=14`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:198` `#  elif defined RIVER_DON && !defined PO4`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:199` `      NBT=13`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:200` `#  elif defined PO4 && !defined RIVER_DON`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:201` `      NBT=12`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:202` `#  else`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:203` `      NBT=11`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:204` `#  endif`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:205` `# endif`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:206` `#else`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:207` `# ifdef OXYGEN`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:208` `#  if defined PO4 && defined RIVER_DON`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:209` `      NBT=10`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:210` `#  elif defined PO4 \|\| defined RIVER_DON`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:211` `      NBT=9`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:212` `#  else`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:213` `      NBT=8`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:214` `#  endif`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:215` `# else`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:216` `#  if defined PO4 && defined RIVER_DON`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:217` `      NBT=9`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:218` `#  elif defined PO4 \|\| defined RIVER_DON`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:219` `      NBT=8`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:220` `#  else`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:221` `      NBT=7`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:222` `#  endif`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:223` `# endif`<br>`ROMS/Nonlinear/Biology/fennel_mod.h:224` `#endif`<br>`ROMS/Modules/mod_param.F:489` `      integer, allocatable :: NT(:)` | C 문서 누락 | 현재 NBT는 선택한 생물 모듈이 설정하는 scalar integer다. NT(ng)와 NBT를 같은 차원의 배열로 설명하지 않는다. [10-14 결론 검증 보완] |
| build-options-history:RBH-2144 | Modules 목록의 완전성 | `Modules.wiki:3` `Now that we are using Fortran 90, the method of choice for managing data structures are modules. The '''ROMS/Modules''' directory contains all of the ROMS modules that contain globally used variables. The complete list is:` | `ROMS/Modules/mod_behavior.F:29` `      MODULE mod_behavior`<br>`ROMS/Modules/mod_extract.F:2` `      MODULE mod_extract`<br>`ROMS/Modules/mod_ice.F:46` `      MODULE mod_ice`<br>`ROMS/Modules/mod_sedbed.F:26` `      MODULE mod_sedbed`<br>`ROMS/Modules/mod_sedflocs.F:2` `      MODULE mod_sedflocs`<br>`ROMS/Modules/mod_vegetation.F:2` `      MODULE mod_vegetation `<br>`ROMS/Modules/mod_pio_netcdf.F:2` `      MODULE mod_pio_netcdf`<br>`ROMS/Modules/mod_pio_netcdf.F:3` `#if defined PIO_LIB && defined DISTRIBUTE` | C 문서 누락 | Modules.wiki의 complete list는 현재 ROMS/Modules 파일 목록을 모두 포함하지 않는다. 현재 없는 mod_obs.F도 포함한다. [10-14 결론 검증 보완] |
| build-options-history:RBH-2145 | mod_arrays.F | `Modules.wiki:5` `<section begin=mod_arrays.F />;<span id="mod_arrays.F"></span>mod_arrays.F`<br>`Modules.wiki:6` `:This is actually a subroutine, not a module, but it calls the allocate and initialize routines for all the modules containing allocatable arrays.<section end=mod_arrays.F />` | `roms-3.9:ROMS/Modules/mod_arrays.F:2` `      SUBROUTINE mod_arrays (allocate_vars)`<br>`roms-3.9:ROMS/Modules/mod_arrays.F:132` `          CALL allocate_forces (ng, LBi, UBi, LBj, UBj)`<br>`roms-3.9:ROMS/Modules/mod_arrays.F:192` `          CALL initialize_forces (ng, tile, model)`<br>`cb4a69f3:ROMS/Modules/mod_arrays.F:2` `      MODULE mod_arrays`<br>`cb4a69f3:ROMS/Modules/mod_arrays.F:100` `      SUBROUTINE ROMS_allocate_arrays (allocate_vars)`<br>`57aecf58:ROMS/Modules/mod_arrays.F:2` `      MODULE mod_arrays`<br>`57aecf58:ROMS/Modules/mod_arrays.F:127` `      SUBROUTINE ROMS_allocate_arrays (allocate_vars)`<br>`57aecf58:ROMS/Modules/mod_arrays.F:277` `      SUBROUTINE ROMS_deallocate_arrays`<br>`57aecf58:ROMS/Modules/mod_arrays.F:379` `      SUBROUTINE ROMS_initialize_arrays` | A 판 차이 | mod_arrays.F는 ROMS 3.9에서 서브루틴이었다. 현재 파일은 mod_arrays 모듈이다. 현재 모듈은 배열 할당·해제·초기화 루틴을 제공한다. [10-14 결론 검증 보완] [10-14 git 이력 판정] git 판정: `cb4a69f3` (2021-09-28). |
| build-options-history:RBH-2150 | mod_clima.F | `Modules.wiki:20` `<section begin=mod_clima.F />;<span id="mod_clima.F"></span>mod_clima.F`<br>`Modules.wiki:21` `:If one of Options#CLIMATOLOGY \| CLIMATOLOGY, Options#AD_SENSITIVITY \| AD_SENSITIVITY, Options#OPT_OBSERVATIONS \| OPT_OBSERVATIONS, or Options#SO_SEMI \| SO_SEMI is '''#defined''', this will provide the storage for the climatological fields.<section end=mod_clima.F />` | `roms-3.6:ROMS/Modules/mod_clima.F:2` `      MODULE mod_clima`<br>`roms-3.6:ROMS/Modules/mod_clima.F:3` `#if defined AD_SENSITIVITY      \|\| defined CLIMATOLOGY      \|\| \`<br>`roms-3.6:ROMS/Modules/mod_clima.F:4` `    defined IS4DVAR_SENSITIVITY \|\| defined OPT_OBSERVATIONS \|\| \`<br>`roms-3.6:ROMS/Modules/mod_clima.F:5` `    defined SENSITIVITY_4DVAR   \|\| defined SO_SEMI`<br>`roms-3.6:ROMS/Modules/mod_clima.F:84` `# ifdef ZCLIMATOLOGY`<br>`46f20897:ROMS/Modules/mod_clima.F:2` `      MODULE mod_clima`<br>`46f20897:ROMS/Modules/mod_clima.F:3` `!`<br>`46f20897:ROMS/Modules/mod_clima.F:171` `      IF (LsshCLM(ng)) THEN`<br>`46f20897:ROMS/Modules/mod_clima.F:172` `        allocate ( CLIMA(ng) % ssh(LBi:UBi,LBj:UBj) )`<br>`57aecf58:ROMS/Modules/mod_clima.F:2` `      MODULE mod_clima`<br>`57aecf58:ROMS/Modules/mod_clima.F:189` `      IF (LsshCLM(ng)) THEN`<br>`57aecf58:ROMS/Modules/mod_clima.F:233` `      IF (ANY(LtracerCLM(:,ng)).or.ANY(LnudgeTCLM(:,ng))) THEN` | A 판 차이 | mod_clima.F의 옛 CPP 활성 조건은 ROMS 3.6과 맞는다. 현재 기후장 배열 할당은 LsshCLM 등 입력 스위치로 선택한다. [10-14 결론 검증 보완] [10-14 git 이력 판정] git 판정: `46f20897` (2014-03-13). |
| build-options-history:RBH-2172 | mod_sources.F | `Modules.wiki:86` `<section begin=mod_sources.F />;<span id="mod_sources.F"></span>mod_sources.F`<br>`Modules.wiki:87` `:If one of Options#UV_PSOURCE \| UV_PSOURCE, Options#TS_PSOURCE \| TS_PSOURCE or Options#Q_PSOURCE \| Q_PSOURCE is '''#defined''', this contains the variables used for point sources.<section end=mod_sources.F />` | `roms-3.6:ROMS/Modules/mod_sources.F:3` `#if defined UV_PSOURCE \|\| defined TS_PSOURCE \|\| defined Q_PSOURCE`<br>`roms-3.6:ROMS/Modules/mod_sources.F:59` `          real(r8), pointer :: Dsrc(:)`<br>`roms-3.6:ROMS/Modules/mod_sources.F:64` `          real(r8), pointer :: Tsrc(:,:,:)`<br>`fb1d4b49:ROMS/Modules/mod_sources.F:127` `          IF (LuvSrc(mg).or.LwSrc(mg).or.ANY(LtracerSrc(:,mg))) THEN`<br>`57aecf58:ROMS/Utility/read_phypar.F:7794` `        IF (LuvSrc(ng).or.LwSrc(ng).or.(ANY(LtracerSrc(:,ng)))) THEN`<br>`57aecf58:ROMS/Utility/checkdefs.F:3825` `        WRITE (stdout,240) uppercase('q_psource'), 'LwSrc'`<br>`57aecf58:ROMS/Utility/checkdefs.F:3838` `        WRITE (stdout,250) uppercase('ts_psource'), 'LtracerSrc'`<br>`57aecf58:ROMS/Utility/checkdefs.F:3851` `        WRITE (stdout,260) uppercase('uv_psource'), 'LuvSrc'`<br>`ROMS/Utility/checkdefs.F:3832` `#if defined TS_PSOURCE && defined SOLVE3D`<br>`ROMS/Utility/checkdefs.F:3838` `        WRITE (stdout,250) uppercase('ts_psource'), 'LtracerSrc'`<br>`ROMS/Utility/checkdefs.F:3842` `        exit_flag=5`<br>`ROMS/Utility/checkdefs.F:3845` `#ifdef UV_PSOURCE`<br>`ROMS/Utility/checkdefs.F:3851` `        WRITE (stdout,260) uppercase('uv_psource'), 'LuvSrc'`<br>`ROMS/Utility/checkdefs.F:3854` `     &          /,13x,'Edit header file or build script!')`<br>`ROMS/Utility/checkdefs.F:3819` `#ifdef Q_PSOURCE` | A 판 차이 | mod_sources.F의 옛 활성 조건은 UV_PSOURCE·TS_PSOURCE·Q_PSOURCE였다. 현재 점 소스 선택은 LuvSrc·LwSrc·LtracerSrc 입력이다. Q_PSOURCE와 UV_PSOURCE는 오류 처리 대상이다. TS_PSOURCE의 오류 검사는 SOLVE3D 조건에서 적용된다. [10-14 결론 검증 정정] [10-14 결론 검증 보완] [10-14 git 이력 판정] git 판정: `fb1d4b49` (2013-11-25). |
| callflow-nonlinear:RF1-032 | ru·rv의 0번 층을 vertical face로 해석 | `models/ROMS/source-analysis/roms_global_state_modules.md:84` ``핵심 차원 규약: **2D 변수는 시간레벨 3개**(barotropic 예측자-수정자 + krhs/kstp/knew), **3D 운동량은 2개**(nstp/nnew), **추적자 t 는 3개**(`mod_ocean.F:459` 의 `,3,NT(ng)`). RHS 배열 ru/rv 는 `0:N(ng)` 로 연직 face 포함 (`:452`).`` | `step2d_LF_AM3.h:2362` `ru(i,j,0,nstp)=rufrc(i,j)`<br>`mod_ocean.F:453` `allocate ( OCEAN(ng) % ru(LBi:UBi,LBj:UBj,0:N(ng),2) )`<br>`mod_ocean.F:456` `allocate ( OCEAN(ng) % rv(LBi:UBi,LBj:UBj,0:N(ng),2) )`<br>`step2d_LF_AM3.h:2269` `#ifdef SOLVE3D`<br>`step2d_LF_AM3.h:2306` `IF (FIRST_2D_STEP.and.PREDICTOR_2D_STEP(ng)) THEN`<br>`step2d_LF_AM3.h:2359` `rufrc(i,j)=rufrc(i,j)-rhs_ubar(i,j)`<br>`step2d_LF_AM3.h:2360` `rhs_ubar(i,j)=rhs_ubar(i,j)+                              &`<br>`step2d_LF_AM3.h:2361` `&                      1.5_r8*rufrc(i,j)-0.5_r8*ru(i,j,0,nnew)`<br>`step2d_LF_AM3.h:2388` `rvfrc(i,j)=rvfrc(i,j)-rhs_vbar(i,j)`<br>`step2d_LF_AM3.h:2389` `rhs_vbar(i,j)=rhs_vbar(i,j)+                              &`<br>`step2d_LF_AM3.h:2390` `&                      1.5_r8*rvfrc(i,j)-0.5_r8*rv(i,j,0,nnew)`<br>`step2d_LF_AM3.h:2391` `rv(i,j,0,nstp)=rvfrc(i,j)` | B 문서 오기 | ru와 rv는 0:N 범위를 할당한다. SOLVE3D의 Legacy 경로는 첫 짧은 예측 단계에서 깊이 적분 3D 우변과 2D 우변의 차이를 느린 강제력으로 만든다. 0번 층은 이 강제력의 시간 이력을 저장하고 다음 큰 단계의 외삽에서 읽는다. 배열의 0:N 차원만으로 0번 층을 수직 face의 운동량 우변으로 해석할 수 없다. [10-14 결론 검증 보완] |
| inputs:RI1-1008 | climatology tracer 저장 수 | — | `ROMS/Utility/inp_par.F:796` `#ifdef SOLVE3D`<br>`ROMS/Utility/inp_par.F:800` `IF (ANY(LtracerCLM(:,ng)).or.ANY(LnudgeTCLM(:,ng))) THEN`<br>`ROMS/Utility/inp_par.F:802` `DO itrc=1,NT(ng)`<br>`ROMS/Utility/inp_par.F:803` `IF (LtracerCLM(itrc,ng)) THEN`<br>`ROMS/Utility/inp_par.F:804` `ic=ic+1`<br>`ROMS/Utility/inp_par.F:807` `NTCLM(ng)=ic` | C 문서 누락 | SOLVE3D에서 NTCLM은 LtracerCLM가 TRUE인 NT 추적자의 수이다. LnudgeTCLM가 TRUE여도 LtracerCLM가 FALSE인 추적자는 이 수에 포함하지 않는다. |
| inputs:RI1-1021 | 격자·tracer 유효 범위 검사 | — | `ROMS/Utility/read_phypar.F:174` `IF (Ngrids.le.0) THEN`<br>`ROMS/Utility/read_phypar.F:208` `IF (NestLayers.lt.1) THEN`<br>`ROMS/Utility/read_phypar.F:257` `IF (Lm(ng).le.0) THEN`<br>`ROMS/Utility/read_phypar.F:267` `IF (Mm(ng).le.0) THEN`<br>`ROMS/Utility/read_phypar.F:277` `IF (N(ng).lt.0) THEN`<br>`ROMS/Utility/read_phypar.F:299` `IF ((NAT.lt.1).or.(NAT.gt.2)) THEN`<br>`ROMS/Utility/read_phypar.F:305` `# ifdef SALINITY`<br>`ROMS/Utility/read_phypar.F:306` `IF (NAT.ne.2) THEN`<br>`ROMS/Utility/read_phypar.F:318` `IF (NPT.le.0) THEN`<br>`ROMS/Utility/read_phypar.F:324` `# ifdef AGE_MEAN`<br>`ROMS/Utility/read_phypar.F:325` `IF (MOD(NPT,2).ne.0) THEN`<br>`ROMS/Utility/read_phypar.F:337` `IF (NCS.lt.0) THEN`<br>`ROMS/Utility/read_phypar.F:344` `IF (LreadNNS.and.((NCS+NNS).le.0)) THEN`<br>`ROMS/Utility/read_phypar.F:354` `IF (NNS.lt.0) THEN` | C 문서 누락 | Ngrids·Lm·Mm은 양수를 요구한다. NestLayers는 1 이상이다. N은 음수만 거부하므로 0은 이 검사에서 통과한다. SOLVE3D의 NAT는 1·2이다. SALINITY를 켜면 `NAT=2`이다. `T_PASSIVE&&SOLVE3D`의 NPT는 양수이다. AGE_MEAN은 짝수 NPT를 요구한다. `SEDIMENT&&SOLVE3D`는 NCS·NNS의 비음수와 양수 합계를 요구한다. |
| outputs-metadata:OMD-V025 | Variables BRY | `Variables.wiki:247` `;<span id="BRY"></span>BRY`<br>`Variables.wiki:248` `:Open boundary conditions input NetCDF file name. #Ngrids\|Ngrids values are expected.`<br>`Variables.wiki:249` `:'''dimension =''' '''BRY'''(#Ngrids\|Ngrids)`<br>`Variables.wiki:250` `:'''option =''' `<br>`Variables.wiki:251` `:'''routine =''' mod_iounits.F`<br>`Variables.wiki:252` `:'''keyword =''' BRYNAME`<br>`Variables.wiki:253` `:'''input =''' roms.in` | `ROMS/Modules/mod_iounits.F:272` `      TYPE(T_IO), allocatable :: BRY(:,:)`<br>`ROMS/Utility/read_phypar.F:4283` `              allocate ( BRY(max_Ffiles,Ngrids) )`<br>`ROMS/Utility/read_phypar.F:4294` `            CASE ('BRYNAME')`<br>`ROMS/Utility/read_phypar.F:4295` `              label='BRY - lateral open boundary conditions'`<br>`ROMS/Utility/metrics.F:1460` `                Text='West  bry Hconvolution, NHstepsB, DTsizeHB ='`<br>`ROMS/Utility/metrics.F:139` `#ifdef FOUR_DVAR`<br>`ROMS/Utility/metrics.F:1308` `# ifdef ADJUST_BOUNDARY`<br>`ROMS/Utility/metrics.F:1378` `#  ifndef MULTI_SCALE_B`<br>`roms-3.5:ROMS/Modules/mod_iounits.F:179` `      allocate ( BRY(Ngrids) )` | A 판 차이 | BRY(Ngrids)는 ROMS 3.5와 일치한다. ab8d6bc9(2020-04-29) 변경 뒤 BRY는 파일 목록과 격자에 대한 2차원 구조이며 BRY(max_Ffiles,Ngrids)로 할당한다. 원 보고서의 2011-03-25 전환 시점은 이 선언 변경과 달라 고친다. [10-14 git 이력 판정] [10-14 결론 검증 정정] [10-14 결론 검증 보완] |
| outputs-metadata:OMD-V028 | Variables CLM | `Variables.wiki:272` `;<span id="CLM"></span>CLM`<br>`Variables.wiki:273` `:Climatology input NetCDF file name. #Ngrids\|Ngrids values are expected.`<br>`Variables.wiki:274` `:'''dimension =''' '''CLM'''(#Ngrids\|Ngrids)`<br>`Variables.wiki:275` `:'''option =''' `<br>`Variables.wiki:276` `:'''routine =''' mod_iounits.F`<br>`Variables.wiki:277` `:'''keyword =''' CLMNAME`<br>`Variables.wiki:278` `:'''input =''' roms.in` | `ROMS/Modules/mod_iounits.F:282` `      TYPE(T_IO), allocatable :: CLM(:,:)`<br>`ROMS/Utility/read_phypar.F:4321` `              allocate ( CLM(max_Ffiles,Ngrids) )`<br>`ROMS/Utility/read_phypar.F:4332` `            CASE ('CLMNAME')`<br>`ROMS/Utility/read_phypar.F:4333` `              label='CLM - climatology fields'`<br>`ROMS/Utility/close_io.F:246` `            Fcount=CLM(i,ng)%Fcount`<br>`roms-3.5:ROMS/Modules/mod_iounits.F:180` `      allocate ( CLM(Ngrids) )` | A 판 차이 | CLM(Ngrids)는 ROMS 3.5와 일치한다. ab8d6bc9(2020-04-29) 변경 뒤 CLM는 파일 목록과 격자에 대한 2차원 구조이며 CLM(max_Ffiles,Ngrids)로 할당한다. 원 보고서의 2011-03-25 전환 시점은 이 선언 변경과 달라 고친다. [10-14 git 이력 판정] [10-14 결론 검증 정정] [10-14 결론 검증 보완] |
| outputs-metadata:OMD-V065 | Variables FRC | `Variables.wiki:558` `;<span id="FRC"></span>FRC`<br>`Variables.wiki:559` `:Input forcing fields file name(s). #Ngrids\|Ngrids values are expected.`<br>`Variables.wiki:560` `:'''dimension =''' '''FRC'''(#Ngrids\|Ngrids)`<br>`Variables.wiki:561` `:'''option =''' `<br>`Variables.wiki:562` `:'''routine =''' mod_iounits.F`<br>`Variables.wiki:563` `:'''keyword =''' FRCNAME`<br>`Variables.wiki:564` `:'''input =''' roms.in` | `ROMS/Modules/mod_iounits.F:292` `      TYPE(T_IO), allocatable :: FRC(:,:)`<br>`ROMS/Utility/read_phypar.F:4373` `              allocate ( FRC(max_Ffiles,Ngrids) )`<br>`ROMS/Utility/read_phypar.F:4384` `            CASE ('FRCNAME')`<br>`ROMS/Utility/read_phypar.F:4385` `              label='FRC - forcing fields'`<br>`ROMS/Utility/get_state.F:244` `        string='FRC: '                     ! impulse forcing`<br>`roms-3.3:ROMS/Modules/mod_iounits.F:109` `        character (len=80), allocatable :: FRCname(:,:)`<br>`63b208cc:ROMS/Modules/mod_iounits.F:126` `      TYPE(T_IO), allocatable :: FRC(:,:)` | B 문서 오기 | FRC(Ngrids)는 문서의 차원 오기다. ROMS 3.3의 FRCname은 2차원이다. 63b208cc(2011-04-22)가 도입한 FRC도 처음부터 2차원이다. 현재 FRC(max_Ffiles,Ngrids)는 파일 목록과 격자 축을 사용한다. [10-14 git 이력 판정] [10-14 결론 검증 정정] [10-14 결론 검증 보완] |
| outputs-metadata:OMD-V185 | Variables MT | `Variables.wiki:1431` `;<span id="MT"></span>MT`<br>`Variables.wiki:1432` `:The maximum number of tracers between all nested grids. Basically the sum of all Variables#NT\|NT.` | `ROMS/Modules/mod_param.F:490` `      integer :: MT`<br>`ROMS/Modules/mod_floats.F:220` `        allocate ( ifTvar(MT) )`<br>`ROMS/Modules/mod_floats.F:3` `#ifdef FLOATS`<br>`ROMS/Modules/mod_floats.F:112` `# ifdef SOLVE3D`<br>`ROMS/Utility/read_asspar.F:237` `              Npts=load_r(Nval, Rval, MT, Ngrids, Rtracer)`<br>`ROMS/Utility/read_asspar.F:2` `#if defined FOUR_DVAR \|\| defined VERIFICATION`<br>`ROMS/Utility/read_asspar.F:133` `# if defined FOUR_DVAR  \|\| defined VERIFICATION \|\| \`<br>`ROMS/Utility/read_asspar.F:134` `    (defined HESSIAN_SV && defined BNORM)`<br>`ROMS/Modules/mod_param.F:1694` `      MT=MAX(1,MAX(NAT,MAXVAL(NT)))`<br>`ROMS/Utility/inp_par.F:853` `        DO i=1,MT`<br>`ROMS/Utility/inp_par.F:43` `#ifdef SOLVE3D` | B 문서 오기 | 현재 코드는 `MT=MAX(1,MAX(NAT,MAXVAL(NT)))`를 사용한다. 문서의 sum of all NT는 최대값 정의와 다르다. |
| outputs-metadata:OMD-V305 | Variables tl_Tdiff | `Variables.wiki:2369` `;<span id="tl_Tdiff"></span>tl_Tdiff`<br>`Variables.wiki:2370` `:If weak constraint 4DVar and the Options#RPM_RELAXATION\|RPM_RELAXATION flag is activated, this coefficient is used to relax tracer type variables diffusion in the representer tangent linear solution to the previous outer loop linearized trajectory during the Picard iterations. The user may turn off relaxation by setting this to zero. #MT\|MT values are expected.`<br>`Variables.wiki:2371` `:'''dimension =''' '''tl_Tdiff'''(#NT\|NT,#Ngrids\|Ngrids)`<br>`Variables.wiki:2372` `:'''units =''' meters<sup>2</sup> second<sup>-1</sup>`<br>`Variables.wiki:2373` `:'''routine =''' ad_t3drelax.F, mod_scalars.F, read_asspar.F, rp_t3drelax.F, tl_t3drelax.F`<br>`Variables.wiki:2374` `:'''keyword =''' tl_Tdiff`<br>`Variables.wiki:2375` `:'''input =''' s4dvar.in` | `ROMS/Modules/mod_scalars.F:957` `        real(r8), allocatable :: tl_Tdiff(:,:)       ! tracers`<br>`ROMS/Modules/mod_scalars.F:2774` `        allocate ( tl_Tdiff(MT,Ngrids) )`<br>`ROMS/Utility/read_asspar.F:236` `            CASE ('tl_Tdiff')`<br>`ROMS/Utility/read_asspar.F:237` `              Npts=load_r(Nval, Rval, MT, Ngrids, Rtracer)`<br>`ROMS/Utility/read_asspar.F:2` `#if defined FOUR_DVAR \|\| defined VERIFICATION`<br>`ROMS/Utility/read_asspar.F:133` `# if defined FOUR_DVAR  \|\| defined VERIFICATION \|\| \`<br>`ROMS/Utility/read_asspar.F:134` `    (defined HESSIAN_SV && defined BNORM)`<br>`ROMS/Representer/rp_t3drelax.F:146` `                FX(i,j)=0.5_r8*tl_Tdiff(itrc,ng)*pmon_u(i,j)*           &`<br>`ROMS/Representer/rp_t3drelax.F:4` `#if defined TL_IOMS && defined RPM_RELAXATION && defined SOLVE3D` | B 문서 오기 | 실제 차원은 tl_Tdiff(MT,Ngrids)다. 문서의 NT는 그리드별 길이이고 MT는 전체 그리드의 최대 길이다. |
| outputs-metadata:OMD-Q003 | Variables의 전역 변수 전체 수록 주장 | `Variables.wiki:2` `This wikipage includes all ROMS global variables in alphabetic order. A single long page` | `ROMS/Modules/mod_ncparam.F:173` `      logical, allocatable :: Qout(:,:)     ! quicksave file switches`<br>`ROMS/Modules/mod_ncparam.F:852` `      IF (.not.allocated(Qout)) THEN`<br>`ROMS/Modules/mod_ncparam.F:853` `        allocate ( Qout(NV,Ngrids) )`<br>`ROMS/Modules/mod_ncparam.F:1462` `          Qout(i,ng)=.FALSE.`<br>`ROMS/Utility/read_phypar.F:2269` `            CASE ('Qout(idUvel)')`<br>`ROMS/Utility/read_phypar.F:2270` `              Npts=load_l(Nval, Cval, Ngrids, Lswitch)`<br>`ROMS/Utility/read_phypar.F:2271` `              Qout(idUvel,1:Ngrids)=Lswitch(1:Ngrids)` | C 문서 누락 | Variables.wiki는 일부 전역 변수 설명이며 현행 전역 변수의 완전한 목록으로 사용하지 않는다. |
| outputs-metadata:OMD-N033 | roms_global_state_modules.md:200 | `source-analysis/roms_global_state_modules.md:200` ``- 추적자 이름 인덱스 `itemp/isalt`·NetCDF 변수 ID 매핑 → `mod_ncparam.F`(별도, source-needed).`` | `ROMS/Utility/get_metadata.F:972` `          Vinfo(1)=Ystring1(Ientry)%value  ! 'variable'      key`<br>`ROMS/Utility/get_metadata.F:977` `          Vinfo(6)=Ystring6(Ientry)%value  ! 'standard_name' key`<br>`ROMS/Utility/get_metadata.F:978` `          Vinfo(7)=Ystring7(Ientry)%value  ! 'type'          key`<br>`ROMS/Utility/get_metadata.F:979` `          Vinfo(8)=Ystring8(Ientry)%value  ! 'index_code'    key`<br>`ROMS/Utility/get_metadata.F:981` `          scale   =Yreal2(Ientry)          ! 'scale'         key`<br>`ROMS/Modules/mod_ncparam.F:2646` `        IF (load) THEN`<br>`ROMS/Modules/mod_ncparam.F:2652` `          DO i=1,6`<br>`ROMS/Modules/mod_ncparam.F:2653` `            Vname(i,varid)=TRIM(ADJUSTL(Vinfo(i)))`<br>`ROMS/Modules/mod_ncparam.F:2656` `            Iinfo(1,varid,ng)=gtype`<br>`ROMS/Modules/mod_ncparam.F:2657` `            Fscale(varid,ng)=scale`<br>`ROMS/Nonlinear/Sediment/sediment_var.h:135` `          CASE ('idTvar(idmud(i))')`<br>`ROMS/Nonlinear/Sediment/sediment_var.h:136` `            load=.FALSE.`<br>`ROMS/Nonlinear/Sediment/sediment_var.h:146` `                WRITE (Vname(1,varid),'(a,i2.2)')                       &`<br>`ROMS/Nonlinear/Sediment/sediment_var.h:154` `                WRITE (Vname(5,varid),'(a)')                            &`<br>`ROMS/Nonlinear/Sediment/sediment_var.h:155` `     &                TRIM(ADJUSTL(Vinfo(5)))`<br>`ROMS/Nonlinear/Sediment/sediment_var.h:156` `              END DO`<br>`ROMS/Nonlinear/Sediment/sediment_var.h:137` `            IF (NCS.gt.0) THEN`<br>`ROMS/Nonlinear/Sediment/sediment_var.h:139` `              DO i=1,NCS`<br>`ROMS/Modules/mod_ncparam.F:2633` `#if defined SEDIMENT \|\| defined BBL_MODEL`<br>`ROMS/Modules/mod_ncparam.F:2634` `#  include <sediment_var.h>` | C 문서 누락 | 일반 load 경로는 YAML 메타데이터를 Vname·Iinfo·Fscale에 연결한다. SEDIMENT 또는 BBL_MODEL의 mud 클래스 생성은 `NCS.gt.0`에서 별도 처리하며 `load=.FALSE.`로 일반 복사를 건너뛴다. 이때 Vname(6) 생성 누락 후보는 OMD-K029의 출력 조건과 중간 강도 판정을 따른다. [10-14 결론 검증 보완] |
| testcases:RT1-667 | FJORD NTIMES와 3 days 주석 | `FJORD_TIDAL_CASE.wiki:314` `      NTIMES == <span class="green">1866241                 ! 3 days</span>`<br>`FJORD_TIDAL_CASE.wiki:315` `          DT == <span class="green">10</span>` | `ROMS/Utility/read_phypar.F:586` `              Npts=load_i(Nval, Rval, Ngrids, ntimes)`<br>`ROMS/Utility/read_phypar.F:594` `              Npts=load_r(Nval, Rval, Ngrids, dt)`<br>`Master/roms.h:122` `          run_time=MAX(run_time, dt(ng)*ntimes(ng))` | B 문서 오기 | FJORD 예제의 `NTIMES=1866241`과 `DT=10`은 3일 주석과 맞지 않는다. 목표 기간을 정한 뒤 단계 수를 다시 산정한다. |
| testcases:RT1-725 | UNSW stdout 격자 순서 K,J,I 표기 | `ROMS_UNSW2008.wiki:176` `::<div class="box">Operating system : Linux`<br>`CPU/hardware     : i686`<br>`Compiler system  : ifort `<br>`Compiler command : /usr/local/intel/fc/10.1.021/bin/ifort `<br>`Compiler flags   : -heap-arrays -ip -O3 -pc80 -xW -free`<br>``<br>`SVN Root URL  : <nowiki>https://www.myroms.org/svn/src/trunk</nowiki>`<br>`SVN Revision  : 333`<br>`Local Root    : /srv/ckpt/roms/shared/src`<br>`Header Dir    : /student/0/a0000020/srv/Projects/upwelling`<br>`Header file   : upwelling.h`<br>`Analytical Dir: /student/0/a0000020/srv/Projects/upwelling`<br>``<br>`Resolution, Grid 01: 0041x0080x016,  Parallel Threads:  1,  Tiling: 001x001</div>Check that these are what you intended. In last line above`<br>`ROMS_UNSW2008.wiki:178` `::* 0041x0080x016 shows the grid size is 41 x 80 x 16 grid points in the K,J,I directions` | `ROMS/Utility/inp_par.F:333` `          WRITE (stdout,50) ng, Lm(ng), Mm(ng), N(ng),                  &`<br>`ROMS/Utility/inp_par.F:334` `     &                      NtileI(ng), NtileJ(ng)`<br>`ROMS/Utility/inp_par.F:332` `#ifdef SOLVE3D` | B 문서 오기 | SOLVE3D 경로의 격자 크기 출력은 Lm×Mm×N 순이다. 문서의 41×80×16은 I×J×K 순으로 읽는다. [10-14 결론 검증 보완] |
| testcases:RT1-1001 | SED_TOY 중력 단위 9.81 ^2 | `CSTMS_SEDTOY.wiki:104` `Gravitational acceleration  <math>{\color{blue}{g}}~ =~ 9.81~ ^{2}</math>`<br>`` | `ROMS/Modules/mod_scalars.F:470` `        real(dp) :: g = 9.81_dp                 ! m/s2` | B 문서 오기 | 중력 가속도 `g=9.81` m/s2로 적는다. |
| testcases:RT1-1005 | SED_TOY steady state u·v XXX와단위 | `CSTMS_SEDTOY.wiki:91` `<math display="block">\begin{align}`<br>`CSTMS_SEDTOY.wiki:95` `Describe steady state sediment concentration and sediment bed`<br>`CSTMS_SEDTOY.wiki:92` `   \color{Blue}{u} &~= ~XXX ~m/s^{2} \\`<br>`CSTMS_SEDTOY.wiki:93` `   \color{Blue}{v} &~= ~XXX ~m/s^{2} \end{align}` | `ROMS/Functionals/ana_initial.h:449` `!  Initial conditions for 3D momentum components (m/s).` | B 문서 오기 | SED_TOY 정상상태 속도 u와 v의 단위는 m/s로 고친다. XXX는 미작성 결과 자리로 남긴다. [10-14 결론 검증 정정] [10-14 결론 검증 보완] |
| testcases:RT1-1070 | LAKE_SIGNELL 초기 u0의단위 m/s2 | `LAKE_SIGNELL_CASE.wiki:76` `<math>\color{blue}{u}\color{black}{ ~= ~0 ~m/s^{2}}</math>`<br>`` | `ROMS/Functionals/ana_initial.h:449` `!  Initial conditions for 3D momentum components (m/s).`<br>`ROMS/Functionals/ana_initial.h:518` `            u(i,j,k,1)=0.0_r8`<br>`ROMS/Functionals/ana_initial.h:523` `            v(i,j,k,1)=0.0_r8` | B 문서 오기 | LAKE_SIGNELL의 초기 속도 0은 m/s로 적는다. |
| testcases:RT1-1076 | LAKE_SIGNELL 중력 9.81의단위 | `LAKE_SIGNELL_CASE.wiki:90` `Gravitational acceleration  <math>\color{blue}{g}\color{black}{~ =~ 9.81~ ^{2}}</math>`<br>`` | `ROMS/Modules/mod_scalars.F:470` `        real(dp) :: g = 9.81_dp                 ! m/s2` | B 문서 오기 | 중력 가속도 `g=9.81` m/s2로 적는다. |
| testcases:RT1-1179 | TEST_HEAD 초기 u0의단위 m3 | `TEST_HEAD_CASE.wiki:72` `<math>\color{blue}{u}\color{black}{~ =~ 0~ m^{3}}</math>`<br>`` | `ROMS/Functionals/ana_initial.h:449` `!  Initial conditions for 3D momentum components (m/s).` | B 문서 오기 | TEST_HEAD 위키의 초기 속도 단위 m3는 m/s로 정정한다. 속도값 0은 위키의 외부 초기 자료 설정이다. [10-14 결론 검증 정정] |
| testcases:RT1-1211 | INLET_TEST의 NTIMES와 실행 기간 | `INLET_TEST_CASE.wiki:37` `\|simulation steps`<br>`INLET_TEST_CASE.wiki:39` `\|17280 steps (2 days)`<br>`INLET_TEST_CASE.wiki:35` `\|10 s` | `ROMS/External/roms_inlet_test.in:231` `      NTIMES == 34560`<br>`Master/roms.h:122` `          run_time=MAX(run_time, dt(ng)*ntimes(ng))`<br>`ROMS/External/roms_inlet_test.in:232` `          DT == 5.0d0` | F 표기 차이 | 위키의 `17280 step × 10 s`와 현재 입력의 `34560 step × 5 s`는 모두 172800 s, 즉 2일이다. [10-14 결론 검증 정정] [10-14 결론 검증 보완] |
| testcases:RT1-1535 | rho0 초기값의 인용 위치·runtime 대입 | `models/ROMS/source-analysis/roms_global_state_modules.md:148` ``\| `rho0` \| 1025.0 kg/m³ (기준밀도) \| `:798` \|`` | `ROMS/Modules/mod_scalars.F:806` `        real(dp) :: rho0 = 1025.0_dp`<br>`ROMS/Utility/read_phypar.F:1015` `            CASE ('RHO0')`<br>`ROMS/Utility/read_phypar.F:1017` `              rho0=Rvalue(1)`<br>`ROMS/External/roms_test_chan.in:427` `        RHO0 =  998.0d0                    ! kg/m3`<br>`ROMS/Modules/mod_scalars.F:798` `!`<br>`ROMS/Modules/mod_scalars.F:803` `!  Mean density (Kg/m3) used when the Boussinesq approximation is`<br>`ROMS/Modules/mod_scalars.F:804` `!  inferred.`<br>`ROMS/Utility/read_phypar.F:1016` `              Npts=load_r(Nval, Rval, 1, Rvalue)` | B 문서 오기 | rho0의 선언 초기값은 mod_scalars.F:806의 1025.0 kg/m³다. RHO0 runtime 입력이 이 값을 바꾼다. TEST_CHAN 입력 예는 998.0 kg/m³다. [10-14 결론 검증 보완] |
| theory-numerics:RTN-244 | NTIMES가 절대 종료 timestep이라는 설명 | `NTIMES.wiki:8` `'''Note that ntimes determines the timestep on which the run will ''end'''''.  Be aware that time step counting does not necessarily always start from 1. This could be so if ocean_time in the initial conditions file is not zero such as when:` | `ROMS/Utility/get_state.F:433` `        IF (msg.eq.1) THEN            ! processing initial conditions`<br>`ROMS/Utility/get_state.F:434` `          time(ng)=INPtime`<br>`ROMS/Nonlinear/initial.F:172` `        ntstart(ng)=INT((time(ng)-dstart*day2sec)/dt(ng))+1`<br>`ROMS/Nonlinear/initial.F:173` `        ntend(ng)=ntstart(ng)+ntimes(ng)-1`<br>`roms-3.6:ROMS/Nonlinear/initial.F:126` `      ntstart(ng)=INT((time(ng)-dstart*day2sec)/dt(ng))+1`<br>`roms-3.6:ROMS/Nonlinear/initial.F:127` `      ntend(ng)=ntimes(ng)`<br>`ROMS/Utility/get_state.F:438` `          ntend(ng)=ntstart(ng)+ntimes(ng)-1` | A 판 차이 | NTIMES를 절대 종료 단계로 사용한 설명은 ROMS 3.6과 일치한다. 2017-07-18 변경 뒤 종료 단계 식은 `ntend(ng)=ntstart(ng)+ntimes(ng)-1`이다. [10-14 결론 검증 보완] [10-14 git 이력 판정] git 판정: `e44e1f54` (2017-07-18). |
| theory-numerics:RTN-245 | 90 days·180 seconds·7776480 예제 | `NTIMES.wiki:12` `For example, if your forcing file data uses ocean_time = "seconds since 2006-01-01 00:00:00", but you wish only to model the period from 2006-04-01 onward, you would set ocean_time = 7776000 (90 days since 2006-01-01 multiplied by 86400 seconds per day) in the initial conditions netcdf file. For Variables#dt\|dt of 180 seconds (480 timesteps per day) '''ntimes''' = 7776480 would cause the run to conclude on 2006-04-02, i.e. it would only run for 1 day of simulated time.  If you set '''ntimes''' = 480 thinking this would be 1 day of simulation you will find ROMS will simply end immediately saying it is already done because the end time you requested predates the initial conditions. ` | `ROMS/Utility/get_state.F:436` `          ntstart(ng)=NINT((time(ng)-dstart*day2sec)/dt(ng))+1`<br>`ROMS/Utility/get_state.F:437` `          IF (ntstart(ng).lt.1) ntstart(ng)=1` | B 문서 오기 | 7776000초는 `dt=180`초에서 43200단계이다. 하루 적분은 480단계이다. |
| theory-numerics:RTN-284 | 모든 private·scratch array가 automatic이라는 설명 | `Old_Intro.wiki:23` `All private or scratch arrays are automatic; their size is determined when the procedure is entered.` | `ROMS/Nonlinear/step2d_LF_AM3.h:630` `      real(r8), dimension(IminS:ImaxS,JminS:JmaxS) :: zeta_new`<br>`ROMS/Nonlinear/step3d_t.F:323` `# endif`<br>`ROMS/Nonlinear/step3d_t.F:324` `      real(r8), allocatable :: Ta(:,:,:,:)` | C 문서 누락 | 일부 scratch는 automatic이다. MPDATA와 diagnostics의 큰 scratch는 allocatable이다. |
| theory-numerics:RTN-371 | ubar·vbar의 물리량 명칭 | `models/ROMS/source-analysis/roms_global_state_modules.md:76` ``\| `ubar/vbar(:,:,3)` \| 연직적분 2D 운동량 \| m/s \| 2D×3 \| 선언 `:91-92`, alloc `ubar :407` \|`` | `ROMS/Nonlinear/step3d_uv.F:1327` `        DO k=1,N(ng)`<br>`ROMS/Nonlinear/step3d_uv.F:1328` `          DO i=IstrP,IendT`<br>`ROMS/Nonlinear/step3d_uv.F:1346` `          DC(i,0)=1.0_r8/DC(i,0)                        ! recursive`<br>`ROMS/Nonlinear/step3d_uv.F:1347` `          CF(i,0)=DC(i,0)*(CF(i,0)-DU_avg1(i,j))        ! recursive` | B 문서 오기 | ubar·vbar는 수심 평균 속도이다. DU_avg·DV_avg와 Huon·Hvom은 수송량이다. |
| theory-numerics:RTN-372 | ru·rv의 k=0 용도 | `models/ROMS/source-analysis/roms_global_state_modules.md:84` ``핵심 차원 규약: **2D 변수는 시간레벨 3개**(barotropic 예측자-수정자 + krhs/kstp/knew), **3D 운동량은 2개**(nstp/nnew), **추적자 t 는 3개**(`mod_ocean.F:459` 의 `,3,NT(ng)`). RHS 배열 ru/rv 는 `0:N(ng)` 로 연직 face 포함 (`:452`).`` | `ROMS/Nonlinear/step2d_LF_AM3.h:2306` `      IF (FIRST_2D_STEP.and.PREDICTOR_2D_STEP(ng)) THEN`<br>`ROMS/Nonlinear/step2d_LF_AM3.h:2307` `        IF (iic(ng).eq.ntfirst(ng)) THEN` | B 문서 오기 | ru·rv의 `k=0`은 순압 결합 forcing 이력이다. |
| theory-numerics:RTN-383 | 전역 상태·TLM 노트의 leapfrog 명칭 | `models/ROMS/source-analysis/roms_global_state_modules.md:133` `이 인덱스들이 leapfrog/predictor-corrector 시간적분에서 회전(roll)된다 → 적분 메커닉은 roms_baroclinic_3d·roms_barotropic_2d 참조.` | `ROMS/Nonlinear/pre_step3d.F:16` `!  Both n-1 and n-2 time-step contributions of the  Adams/Bashforth    !`<br>`ROMS/Nonlinear/pre_step3d.F:17` `!  scheme are added here to u and v at time index "nnew", since the    !`<br>`ROMS/Nonlinear/step3d_uv.F:347` `        IF (iic(ng).eq.ntfirst(ng)) THEN`<br>`ROMS/Nonlinear/step3d_uv.F:348` `          cff=0.25_r8*dt(ng)` | C 문서 누락 | 3D 운동량의 AB3와 2D 기본 LF-AM3를 구분한다. |
| tools-guides:RTG-081 | 평균 변수 초기화 예제의 이름 | `Frequently_Asked_Questions.wiki:219` `real(r8), pointer :: avgu3d(:,:,:)`<br>`Frequently_Asked_Questions.wiki:219` `AVERAGE(ng) % avgv3d(i,j,k) = IniVal` | `ROMS/Modules/mod_average.F:1626` `              AVERAGE(ng) % avgu3d(i,j,k) = IniVal`<br>`ROMS/Modules/mod_average.F:1636` `              AVERAGE(ng) % avgv3d(i,j,k) = IniVal`<br>`ROMS/Modules/mod_average.F:1621` `# ifdef SOLVE3D`<br>`ROMS/Modules/mod_average.F:1622` `      IF (Aout(idUvel,ng)) THEN`<br>`ROMS/Modules/mod_average.F:1632` `      IF (Aout(idVvel,ng)) THEN` | B 문서 오기 | avgu3d를 정의·할당한 예제는 avgu3d를 초기화해야 한다. [10-14 결론 검증 보완] |
| tools-guides:RTG-1968 | 수동 추적자 수와 AGE_MEAN | `Frequently_Asked_Questions.wiki:108` `T_PASSIVE` | `ROMS/Utility/read_phypar.F:314` `#if defined T_PASSIVE && defined SOLVE3D`<br>`ROMS/Utility/read_phypar.F:318` `              IF (NPT.le.0) THEN`<br>`ROMS/Utility/read_phypar.F:324` `# ifdef AGE_MEAN`<br>`ROMS/Utility/read_phypar.F:325` `              IF (MOD(NPT,2).ne.0) THEN`<br>`ROMS/Modules/mod_ncparam.F:2668` `# ifdef AGE_MEAN`<br>`ROMS/Modules/mod_ncparam.F:2670` `                DO i=1,NPT,2`<br>`ROMS/Modules/mod_ncparam.F:2693` `                DO i=2,NPT,2`<br>`ROMS/Modules/mod_ncparam.F:2701` `                  WRITE (Vname(1,varid),'(a,i2.2,a)')                   &`<br>`ROMS/Modules/mod_ncparam.F:2702` `     &                  TRIM(ADJUSTL(Vinfo(1))), ic, '_age'` | C 문서 누락 | T_PASSIVE·SOLVE3D는 양의 NPT를 요구한다. 같은 경로에서 AGE_MEAN도 정의하면 NPT는 짝수여야 한다. [10-14 결론 검증 정정] [10-14 결론 검증 보완] |
