---
title: "ROMS 전역 상태 모듈 — mod_* global state (param/grid/ocean/mixing/forces/boundary/scalars/stepping/iounits)"
model: ROMS
component: ROMS/Modules
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Modules/). mod_param.F(차원·T_BOUNDS·T_DOMAIN), mod_ocean.F(T_OCEAN 상태변수 allocate/initialize), mod_grid.F(T_GRID metric), mod_stepping.F(시간 인덱스), mod_scalars.F(time/dt/g/rho0), mod_mixing/forces/boundary/iounits.F(파생타입), mod_arrays.F(allocate orchestrator) 를 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_support_modules.md
  - models/ROMS/README.md
---

# ROMS 전역 상태 모듈 — mod_* global state

> ROMS 의 모든 격자·상태변수·구성 스칼라를 담는 Fortran MODULE 집합 (경로: roms/ROMS/Modules/). 각 모듈은 nested grid 배열 `(ng)` 로 인덱싱되는 파생타입(derived type)을 정의하고, `allocate_*`/`initialize_*`/`deallocate_*` 3종 루틴을 export 한다.

이 노트는 **전역 상태 자료구조(차원·격자·상태변수·스칼라·시간인덱스)** 에 집중한다. 지원·유틸리티 성격 모듈(`mod_kinds`, `mod_parallel`, `mod_strings` 등)은 기존 [[roms_support_modules]] 참조. NetCDF I/O 메타(`mod_ncparam`, `mod_netcdf`) 와 물리 패키지별 상태(`mod_biology`, `mod_sediment`, `mod_bbl`, `mod_tides`)는 각 도메인 노트로 분리.

## 0. 공통 설계 패턴

Modules/ 에 38 개 `mod_*.F` 존재 (`ls Modules/*.F | wc -l` → 38). 핵심 상태 모듈의 공통 관용:

1. `#include "cppdefs.h"` 로 시작, 모든 라이선스 헤더는 `!=== Hernan G. Arango ===` 블록 (예: `mod_param.F:5`, `mod_ocean.F:5`).
2. 파생타입 `T_XXX` 를 정의하고, **nested grid 차원** allocatable 배열 `TYPE(T_XXX), allocatable :: XXX(:)` 를 모듈 전역에 선언 — 예: `OCEAN(:)` (`mod_ocean.F:363`), `GRID(:)` (`mod_grid.F:365`), `MIXING(:)` (`mod_mixing.F:399`), `FORCES(:)` (`mod_forces.F:563`), `BOUNDARY(:)` (`mod_boundary.F:763`).
3. 멤버는 거의 전부 `real(r8), pointer :: var(:,:,...)` — allocatable 이 아니라 **pointer** (nesting/contact point 에서 재지정·공유 필요).
4. 3 루틴 PUBLIC: `allocate_*`/`deallocate_*`/`initialize_*` (예: `mod_ocean.F:76-78`).
5. `initialize_*` 는 **first-touch 정책** 으로 0 초기화 — shared-memory 에서 thread 별 메모리 지역성(NUMA) 확보 (`mod_ocean.F:1566-1570` "using first touch distribution policy ... performs propagation of the shared arrays across the cluster").

전체 할당은 `mod_arrays.F` 의 `ROMS_allocate_arrays` 가 grid 루프에서 각 모듈 `allocate_*` 를 순차 호출하는 방식으로 오케스트레이션된다 (`mod_arrays.F:123`, 호출 본문 `:180-224`).

## 1. mod_param — 차원·파티션·파생타입 부모

`mod_param.F` 는 모든 차원 파라미터를 정의. `USE mod_kinds` 만 의존 (`mod_param.F:99`).

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

`NAT`(능동, 보통 2=θ,S; `mod_param.F:499`, 정의 `:63-64`), `NT(:)`(총 추적자, `mod_param.F:489`), `MT`(최대 추적자, `mod_param.F:490`). 정의 주석 `mod_param.F:61-76` — `NST=NCS+NNS`(퇴적), `NPT`(passive), `NBT`(생물). 추적자 **이름 인덱스**(`itemp`,`isalt`)는 여기가 아니라 `mod_ncparam.F` 에 있다 (`idTvar(:)` 등 `mod_ncparam.F:586`).

### 1.3 타일 경계 파생타입 — T_BOUNDS / T_IOBOUNDS / T_DOMAIN

`mod_param.F` 는 병렬 타일링의 핵심 인덱스 컨테이너를 정의:

- `T_BOUNDS` (`mod_param.F:162-230`): 타일별 하한/상한 `LBi/UBi/LBj/UBj` (`:165-168`), 계산 루프 시작/끝 `Istr/Iend/Jstr/Jend` (`:175-178`), RHO/U/V 변형 `IstrR/IstrU/JstrV` (`:180-186`), open-boundary(`B`/`M`) 및 nesting(`P`/`T`) 인덱스 (`:188-204`), halo 인덱스 `Istrm3..Iendp3` (`:206-214`). 전역 인스턴스 `BOUNDS(:)` (`mod_param.F:232`). 인덱스 산출 루틴은 `Utility/get_bounds.F` 의 `var_bounds` (`mod_param.F:150-151` 주석 참조).
- `T_IOBOUNDS` (`mod_param.F:241-280`): NetCDF I/O 용 PSI/RHO/U/V 별 lower/upper bound + 점 수 (`xi_rho`,`eta_rho` 등). 인스턴스 `IOBOUNDS(:)` (`:282`).
- `T_DOMAIN` (`mod_param.F:292-327`): 타일이 도메인 가장자리에 접하는지 논리 스위치 `Eastern_Edge`/`Western_Edge`/.../ 코너 `NorthEast_Corner` (`:293-301`) + 타일 분수좌표 min/max. 인스턴스 `DOMAIN(:)` (`:329`).

### 1.4 메모리 추정

`Dmem(:)`(동적 메모리 요구, 배열 원소 수; `mod_param.F:137`)와 `BmemMax(:)`(분산메모리 버퍼 최대, bytes; `:132`). 각 `allocate_*` 가 할당 시 `Dmem(ng)=Dmem(ng)+...` 로 누적 (예: `mod_ocean.F:459`).

## 2. mod_ocean — 예후(prognostic) 상태변수 T_OCEAN

ROMS 의 **핵심 상태벡터**. `T_OCEAN` 구조체 (`mod_ocean.F:84-361`), 전역 `OCEAN(:)` (`mod_ocean.F:363`).

### 2.1 비선형(NLM) 상태변수

| 멤버 | 의미 | 단위 | 차원 | file:line |
|---|---|---|---|---|
| `zeta(:,:,3)` | 자유표면 | m | 2D×3 시간레벨 | 선언 `mod_ocean.F:93`, alloc `:413` |
| `ubar/vbar(:,:,3)` | 연직적분 2D 운동량 | m/s | 2D×3 | 선언 `:91-92`, alloc `ubar :407` |
| `u/v(:,:,N,2)` | 3D 운동량 성분 | m/s | 3D×2 시간레벨 | 선언 `:113,115`, alloc `u :461`, `v :467` |
| `t(:,:,N,3,NT)` | 추적자(능동+수동) | — | 3D×3×NT | 선언 `:112`, alloc `:458` |
| `rho/pden(:,:,N)` | 밀도/위치밀도 anomaly | kg/m³ | 3D | 선언 `:108-109`, alloc `pden :446`,`rho :449` |
| `W(:,:,0:N)` | S좌표 연직속도 ω·Hz/(mn) | m³/s | 3D(0:N) | 선언 `:117`, 주석 `:34` |
| `ru/rv(:,:,0:N,2)` | 3D 운동량 RHS | m⁴/s² | alloc `:452,455` |
| `rubar/rvbar/rzeta(:,:,2)` | 2D RHS | — | 선언 `:88-90` |

핵심 차원 규약: **2D 변수는 시간레벨 3개**(barotropic 예측자-수정자 + krhs/kstp/knew), **3D 운동량은 2개**(nstp/nnew), **추적자 t 는 3개**(`mod_ocean.F:458` 의 `,3,NT(ng)`). RHS 배열 ru/rv 는 `0:N(ng)` 로 연직 face 포함 (`:452`).

상태변수 정의 주석은 `mod_ocean.F:11-34` 에 단위까지 명시 — 예: `zeta` = "Free surface (m)" (`:18`), `W` = "S-coordinate (omega*Hz/mn) vertical velocity (m3/s)" (`:34`).

### 2.2 데이터동화 다중 상태 (TL/AD/representer)

같은 구조체 안에 4D-Var 용 접선선형(`tl_`)·수반(`ad_`)·forcing(`f_`) 사본을 보유: `tl_zeta`(`:157`), `tl_t/tl_u`(`:176-177`), `ad_t/ad_u`(`:227-228`), `f_t`(`:312`). 할당 예 `tl_zeta :559`, `tl_t :606`. → 메커닉은 [[roms_adjoint_framework]]·[[roms_4dvar]] 참조; 여기서는 **상태 컨테이너가 NLM/TLM/ADM 을 단일 OCEAN 구조체에 동거**시킨다는 점만 기록.

### 2.3 WEC·생물·기타 조건부 멤버

`#ifdef WEC` Stokes 속도 `ubar_stokes`/`u_stokes`/`W_stokes` (`mod_ocean.F:104-105,123-125`, 정의 주석 `:60-67`) → [[roms_wec]]. `#ifdef WEC_VF` quasi-static `zetat/zetaw/qsp/bh` (`:98-101`). `TIDE_GENERATING_FORCES` 시 `eq_tide` (`:95`).

### 2.4 초기화 (first-touch)

`initialize_ocean(ng,tile,model)` (`mod_ocean.F:1562`): `IniVal=0.0_r8` (`:1588`) 로 타일 범위 전체를 0 대입 (`:1631-1639` ...). `#include "set_bounds.h"` 로 타일 인덱스 설정 (`:1590`), `#ifdef DISTRIBUTE` 분기로 분산메모리 시 전체 LBi:UBi 범위 사용 (`:1594-1596`).

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

이 인덱스들이 leapfrog/predictor-corrector 시간적분에서 회전(roll)된다 → 적분 메커닉은 [[roms_baroclinic_3d]]·[[roms_barotropic_2d]] 참조.

## 5. mod_scalars — 구성 스칼라·물리상수

가장 큰 스칼라 컨테이너 (`mod_scalars.F`, 165 KB). 핵심:

### 5.1 시간 제어

`time(:)`(초)·`tdays(:)`(일) (`mod_scalars.F:265-266`, THREADPRIVATE `:267`), 시간스텝 `dt(:)`·`dtfast(:)` (`:273-274`), 스텝 카운터 `iic(:)`(NLM 시간스텝 인덱스, `:253`)·`iif(:)`(barotropic, `:254`), `ndtfast(:)`/`nfast(:)`(`:262-263`), `ntimes(:)`(총 스텝, `:340`), `ntstart(:)`/`ntend(:)`(`:382-383`), 재시작 레코드 `nrrec(:)` (`:1192`).

### 5.2 물리 상수

| 상수 | 값 | file:line |
|---|---|---|
| `g` | 9.81 m/s² (`#ifdef SOLITON` 시 비차원 1.0) | `mod_scalars.F:470` (SOLITON 분기 `:468`) |
| `rho0` | 1025.0 kg/m³ (기준밀도) | `:798` |
| `Eradius` | 6371315.0 m | `:463` |
| `pi` | 3.14159265358979… (parameter) | `:834` |
| `deg2rad` | pi/180 | `:835` |

복합항 `gorho0=g/rho0` 는 런타임 계산 (`mod_scalars.F:4457`).

### 5.3 종료 코드

`exit_flag`(초기 0, `mod_scalars.F:570`) 와 코드표 주석 `:559-568`: 1=Blows up, 2=Input error, 3=Output error, 7=Illegal input parameter, 8=Fatal algorithm result 등. NaN/blow-up 검출 시 드라이버가 이 값으로 종료를 결정 → [[roms_main_driver_dispatch]].

## 6. mod_mixing / mod_forces / mod_boundary

### 6.1 mod_mixing — 혼합계수 T_MIXING

`T_MIXING` (`mod_mixing.F:153-397`), `MIXING(:)` (`:399`). 연직 혼합계수 `Akv(:,:,0:N)`(운동량, `:237`)·`Akt(:,:,0:N,NAT)`(추적자, `:238`). 난류 닫힘(GLS/MY2.5)·수평혼합 변수도 다수 보유. 알고리즘은 [[roms_vertical_mixing]]·[[roms_horizontal_mixing]] 참조.

### 6.2 mod_forces — 표면/바닥 강제력 T_FORCES

`T_FORCES` (`mod_forces.F:210-561`), `FORCES(:)` (`:563`). 표면 운동량 응력 `sustr/svstr(:,:)` (`:214-215`), 바닥 응력 `bustr` (`:225`), 표면 추적자 flux `stflx(:,:,NT)` (`:430`). 대기강제·bulk flux 메커닉은 [[roms_atmospheric_forcing]]·[[roms_bulk_flux_coare]] 참조.

### 6.3 mod_boundary — 개방경계 강제 T_BOUNDARY + LBC_apply

두 파생타입:
- `T_APPLY` (`mod_boundary.F:387-392`): 경계점별 적용 스위치 `west/east/south/north` 논리배열. 인스턴스 `LBC_apply(:)` (`:394`). nesting composite grid 에서 nesting 처리 점은 FALSE 로 mixed BC 허용 (`:381-385` 주석).
- `T_BOUNDARY` (`mod_boundary.F:400-761`), `BOUNDARY(:)` (`:763`): 경계별 강제값 `zeta_west(:)`(`:404`), `u_west(:,:)`(`:515`), `t_west(:,:,NT)`(`:585`) 등 4 방향×변수. `CELERITY_*` 시 Orlanski 위상속도 사본 `zeta_west_Cx` 등 (`:406-408`). LBC 적용 메커닉은 [[roms_open_boundaries]] 참조.

## 7. mod_iounits — I/O 파일 구조 T_IO

`T_IO` (`mod_iounits.F:167-189`): 단일 출력 파일의 모든 메타를 압축 보관 — `IOtype`/`Nfiles`/`Fcount`(multi-file 카운터, `:168-170`), `Rindex`(NetCDF 레코드, `:172`), `ncid`(`:173`), 변수ID 포인터 `Vid/Tid`(`:175-176`), 시간범위 `time_min/time_max`(`:177-178`), 파일명 `base/name/files`(`:181-183`). `PIO_LIB` 시 PIO descriptor `pioFile/pioVar` (`:184-188`). HIS/AVG/RST 등 출력 종류마다 `TYPE(T_IO) :: HIS(Ngrids)` 형태로 인스턴스화 (`:160-165` 주석).

## 8. mod_arrays — 할당 오케스트레이터

`ROMS_allocate_arrays(allocate_vars)` (`mod_arrays.F:123`): 모든 상태 모듈의 `allocate_*` 를 `ONLY` import (`:24-104`) 한 뒤, grid 루프 `DO ng=1,Ngrids` (`:168`) 안에서 타일 경계 `LBi..UBij` 를 `BOUNDS(ng)` 에서 추출(`:170-175`)하고 순차 호출 — `allocate_boundary`(`:182`)→`allocate_forces`(`:202`)→`allocate_grid`(`:203`)→`allocate_mixing`(`:208`)→`allocate_ocean`(`:209`) ... `$OMP MASTER`/`$OMP BARRIER` 로 마스터 스레드만 할당 (`:169,225-226`). 완료 시 `LallocatedMemory=.TRUE.` (`:252`). `NESTING` 시 contact point 구조는 `LBC_apply` 할당 후로 지연 (`:229-236`). 짝 루틴 `ROMS_deallocate_arrays`(`:273`)·`ROMS_initialize_arrays`(`mod_arrays.F:111` PUBLIC).

## 9. 요약 — 상태 흐름

```
mod_param (차원 Lm/Mm/N/NT, BOUNDS 타일 인덱스)
   │ ROMS_allocate_arrays (mod_arrays.F:123)
   ▼
OCEAN(ng)%{zeta,ubar,u,v,t,rho,W}   ← 예후 상태 (mod_ocean)
GRID(ng)%{h,f,pm,pn,Hz,z_r,*mask}   ← 격자 metric (mod_grid)
MIXING/FORCES/BOUNDARY(ng)          ← 혼합·강제·경계
   │ 시간레벨 회전: kstp/krhs/knew (2D), nstp/nnew (3D)  (mod_stepping)
   │ 스칼라: time/dt/g/rho0/exit_flag                    (mod_scalars)
   ▼
시간적분 (Nonlinear/main3d) — 메커닉은 [[roms_baroclinic_3d]] 등
```

## ⚠ 범위 밖 (다른 노트)

- 추적자 이름 인덱스 `itemp/isalt`·NetCDF 변수 ID 매핑 → `mod_ncparam.F`(별도, source-needed).
- `mod_average`(시간평균 누산기)·`mod_diags`(진단)·`mod_coupling`(2D↔3D 결합항) → 미작성, source-needed.
- 병렬 `mod_parallel`·종류 `mod_kinds`(r8/dp 정의)·`mod_storage` → [[roms_support_modules]].
