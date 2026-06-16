---
title: "ROMS NetCDF I/O — def_·wrt_·get_·nf_ 계열 파일 구조와 병렬 I/O"
model: ROMS
component: ROMS/Utility
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Utility, roms/ROMS/Modules). mod_netcdf.F (INTERFACE 오버로딩·netcdf_create cmode), def_dim.F·def_var.F (nf90/PIO 듀얼 인터페이스·nf90_def_var·deflate), def_his.F (파일 생성·차원·변수 정의), wrt_his.F (Rindex 시간레코드 write·nf_fwrite), nf_fwrite2d.F·nf_fread2d.F (gather/scatter·water-point packing), get_2dfld.F·get_grid.F·get_state.F·read_phypar.F 헤더·핵심 로직 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_support_modules.md
  - models/ROMS/README.md
---

# ROMS NetCDF I/O — def_·wrt_·get_·nf_ 계열

> ROMS의 디스크 입출력 전체를 담당하는 Utility/ 의 NetCDF I/O 계층 분석. 파일/차원/변수 **정의**(`def_*`, 23개) → **출력**(`wrt_*`, 20개) → **입력**(`get_*` 18개, `read_*` 10개) → **저수준 병렬 read/write 래퍼**(`nf_f(re|w)rite*`, 12개) 의 4단 구조. (경로: roms/ROMS/Utility/, mod_netcdf 는 roms/ROMS/Modules/)

ROMS .F 파일은 모두 C-preprocessor 매크로(`#include "cppdefs.h"`)로 시작하며, NetCDF 표준 라이브러리와 NCAR **PIO(Parallel-IO)** 라이브러리를 동일 이름의 generic interface로 추상화한다.

---

## 1. 4단 I/O 계층 개요

| 계층 | 파일 prefix | 개수 | 역할 |
|---|---|---|---|
| 저수준 generic 래퍼 | `mod_netcdf` (Modules) | 1 모듈 | nf90 라이브러리 호출 단일 인터페이스화 (`netcdf_create/open/close/get_*/put_*`) |
| 파일·차원·변수 정의 | `def_*` | 23 | NetCDF 파일 생성, 차원/변수/속성 정의 (define mode) |
| 격자장 출력 | `wrt_*` | 20 | 시간 레코드별 모델 필드를 출력 파일에 write |
| 격자장 입력 | `get_*` (18), `read_*` (10) | 28 | 초기/경계/강제·격자 read, 표준입력 파라미터 read |
| 분산 2D/3D/4D read/write | `nf_fread*` / `nf_fwrite*` | 12 | MPI 타일 ↔ 전역 배열 gather/scatter + nf90_get/put_var |

`def_*`/`wrt_*` 이 **출력 파일별로 1:1 쌍**을 이룬다: his(history)/avg(time-average)/rst(restart)/ini(initial)/dai(daily-avg)/diags/floats/station/quick/tides 등. 예) `def_his.F` ↔ `wrt_his.F`, `def_rst.F` ↔ `wrt_rst.F`.

출력 파일 종류 (헤더 주석):
- `def_his.F:11` — `This module creates output HISTORY file ...`
- `def_rst.F:11` — `This module creates ouput restart file ...` (원문 오타 verbatim)
- `def_ini.F:11` — `This module open existing nonlinear model initial conditions file ...`
- `def_avg`(time-average)·`def_dai`(daily)·`def_diags`(diagnostics)·`def_quick`(quick-save)·`def_tides`·`def_floats`·`def_station`·`def_extract`. 4D-Var 전용: `def_hessian`·`def_lanczos`·`def_norm`·`def_std`·`def_state`·`def_impulse`·`def_error`. GST(고유값): `def_gst`.

---

## 2. mod_netcdf — generic 인터페이스 추상화 (Modules/mod_netcdf.F)

헤더 주석 `mod_netcdf.F:11-15`:
> `This MODULE contains all NetCDF variables definitions. ... Usually, several NetCDF library calls are required to inquire and read a dimension or variable. These routines provide a single interface for such operations.`

### 2.1 이름 오버로딩 (kind/rank 별 MODULE PROCEDURE)
동일 이름 generic procedure 가 자료형(kind)·배열 차원(rank)별로 분기한다 (`mod_netcdf.F:34-35` 주석: *"They differ in the kind type parameter and data array rank"*):

| INTERFACE | 분기 | 라인 |
|---|---|---|
| `netcdf_get_fvar` (부동소수 read) | 0d~4d (+ SINGLE_PRECISION 시 0dp~3dp) | `:45-57` |
| `netcdf_get_ivar` (정수) | 0d~2d | `:59-63` |
| `netcdf_get_lvar` (논리) | 0d~1d | `:65-68` |
| `netcdf_get_svar` (문자열) | 0d~3d | `:70-75` |
| `netcdf_get_time` | 0d~1d | `:77-80` |
| `netcdf_put_fvar` (부동소수 write) | 0d~4d (+dp) | `:82-94` |
| `netcdf_put_ivar`/`put_lvar`/`put_svar` | 0d~2d/3d | `:96-113` |

PUBLIC 진입점 (`mod_netcdf.F:115-126`): `netcdf_check_dim`, `netcdf_check_var`, `netcdf_close`, `netcdf_create`, `netcdf_enddef`, `netcdf_get_dim`, `netcdf_get_satt`, `netcdf_inq_var`, `netcdf_inq_varid`, `netcdf_open`, `netcdf_redef`, `netcdf_sync`.

### 2.2 외부 자료형 결정 (CPP 조건부)
출력 부동소수 외부표현은 cppdefs 매크로로 결정:
- `NF_FOUT` = `OUT_DOUBLE` 시 `nf90_double`, 아니면 `nf90_real` (`mod_netcdf.F:187-191`)
- `NF_FRST` (restart) = `RST_SINGLE` 시 `nf90_real`, 아니면 `nf90_double` (`:192-196`)
- `NF_TOUT` (시간·깊이 변수) = 항상 `nf90_double` — 주석 `:203-205`: *"It is set to double precision for accuaracy in both single and douple precision numerical kernel"* (원문 오타 verbatim)

### 2.3 파일 생성 모드 (CMODE)
`mod_netcdf.F:209-216` — 기본 생성 모드 플래그. `HDF5 || PARALLEL_IO || OUT_NETCDF4` 시 `CMODE = nf90_netcdf4` (NetCDF-4/HDF5), 아니면 classic. `netcdf_create` 에서 `IOR` 로 추가 플래그 합성:
- 병렬 경로 (`netcdf_create.F:9137-9140` 부근): `my_cmode=IOR(CMODE, nf90_mpiio)` → `IOR(my_cmode, nf90_clobber)` → `nf90_create(path=..., cmode=my_cmode, ...)`
- 직렬 경로 (`:9163-9169`): `my_cmode=IOR(nf90_clobber, CMODE)`, `IOR(my_cmode, nf90_share)`, `nf90_create(TRIM(ncname), my_cmode, ncid)`

(`netcdf_create` SUBROUTINE 본체: `mod_netcdf.F:9083-9216`)

---

## 3. 정의 계층 — def_dim / def_var

### 3.1 듀얼 인터페이스 패턴 (nf90 + PIO)
모든 def 모듈은 **표준 NetCDF용 `*_nf90` 와 PIO용 `*_pio`** 두 구현을 generic interface 로 묶는다. `def_dim.F:24-29`:
```
INTERFACE def_dim
  MODULE PROCEDURE def_dim_nf90
#if defined PIO_LIB && defined DISTRIBUTE
  MODULE PROCEDURE def_dim_pio
#endif
END INTERFACE def_dim
```

`def_dim_nf90` 본체 (`def_dim.F:34-120`): `OutThread` 만 `nf90_def_dim(ncid, TRIM(DimName), DimSize, DimId)` 호출 (`:94-95`) → 오류 시 `FoundError` 로 `exit_flag=3` 설정 (`:96-100`). 비병렬 I/O + DISTRIBUTE 빌드에서는 `mp_bcasti` 로 `DimID/status/exit_flag` 를 전 thread 에 broadcast (`def_dim.F:103-113`). PIO 버전(`:125-190`)은 `PIO_def_dim` 사용 (`:178`), broadcast 불필요(병렬 I/O 자체가 분산).

### 3.2 def_var — 변수 + 메타데이터 정의
`def_var.F:11` *"This routine defines the requested NetCDF variable"*. 입력 `Vinfo` 문자열 배열이 CF 규약 속성 25종을 운반 (`def_var.F:33-59`): `(1)`이름·`(2)`long_name·`(3)`units·`(4)`calendar·`(13)`cycle·`(14)`field·`(16)`time·`(17)`missing_value·`(21)`standard_name·`(22)`coordinates·`(23)`formula_terms·`(24)`_FillValue 등. `Aval` 실수배열은 add_offset/valid_min/valid_max/missing/C-grid-type/fill 값 운반 (`:26-32`).

핵심 호출:
- 스칼라(`nVdim==1 && Vdim(1)==0`): `nf90_def_var(ncid, TRIM(Vinfo(1)), Vtype, varid=Vid)` (`def_var.F:159-161`)
- 일반 다차원: `nf90_def_var(ncid, TRIM(Vinfo(1)), Vtype, Vdim(1:nVdim), Vid)` (`:162-164`)
- 압축: `DEFLATE && OUT_NETCDF4` 시 `nf90_def_var_deflate(ncid, Vid, shuffle, deflate, deflate_level)` (다차원 변수 한정, `def_var.F:175-189`)
- 속성: `nf90_put_att(...)` 반복으로 CF 메타·UGRID 위상(`cf_role`·`topology_dimension`·`node_dimensions`·`face_dimensions` 등, `def_var.F:199-346`) 기록.

> 주석 `def_var.F:75-76`: *"Notice that arrays \"Aval\" and \"Vinfo\" is destroyed on output to facilitate the definition of the next variable."* — 호출자가 같은 버퍼를 재사용하도록 함.

---

## 4. def_his — history 파일 정의 흐름 (대표 def_* 본체)

`def_his.F` (6575 라인) 가 `def_*` 의 전형. `def_his_nf90` 의 단계:

1. **파일명 설정·보고** `def_his.F:174-186` (`ncname=HIS(ng)%name`).
2. **신규 파일 생성** — `DEFINE : IF (ldef)` 분기 (`:192`) → `CALL netcdf_create (ng, model, TRIM(ncname), HIS(ng)%ncid)` (`:193`).
3. **차원 정의** `:199-` — `DimIDs=0` 초기화 후 C-grid 스태거 차원 일괄 정의: `xi_rho/xi_u/xi_v/xi_psi`, `eta_rho/eta_u/eta_v/eta_psi` (`def_his.F:205-235`), 경계조정 시 `IorJ`(`:237-241`), water-point 압축 시 `xy_rho/xy_u`(`WRITE_WATER && MASKING`, `:243-249`). 차원 크기는 `IOBOUNDS(ng)%xi_rho` 등 I/O 경계 구조에서 가져옴.
4. **변수 정의** — `status=def_var(...)` 를 변수마다 반복. 시간변수부터(`HIS(ng)%Vid(idtime)`, `def_his.F:558`), 이어 wet/dry 마스크(`idPwet/idRwet/idUwet/idVwet`, `:596-647`), 깊이(`idpthR/U/V/W`), 자유표면(`idFsur`), 운동량·추적자 등. 각 변수 ID는 `HIS(ng)%Vid(...)` 에 저장돼 wrt_* 가 참조.

---

## 5. wrt_his — 시간 레코드 출력 (대표 wrt_* 본체)

`wrt_his.F:11-14` *"This module writes requested model fields into the HISTORY output file using either the standard NetCDF library or the Parallel-IO (PIO) library."*

핵심 메커니즘:
- **시간 레코드 인덱스 전진**: `HIS(ng)%Rindex=HIS(ng)%Rindex+1` (`wrt_his.F:235`) — 매 출력 호출마다 unlimited(time) 차원 레코드 증가.
- **시간값 write**: `CALL netcdf_put_fvar (ng, model, HIS(ng)%name, ... (/HIS(ng)%Rindex/), (/1/), ...)` (`wrt_his.F:257-259`) — generic put 인터페이스(§2.1)로 0d 시간 스칼라 기록.
- **격자장 write**: 각 필드를 `nf_fwrite2d`/`nf_fwrite3d` 로 출력. 예 wet 마스크: `status=nf_fwrite2d(ng, model, HIS(ng)%ncid, idPwet, ..., HIS(ng)%Rindex, gtype, ...)` (`wrt_his.F:270-272`); 3D 깊이: `nf_fwrite3d(... idpthR ...)` (`:361-363`). 실패 시 `WRITE(stdout,20) TRIM(Vname(1,...)), HIS(ng)%Rindex` 로 보고 (`:281` 등).
- 사용 모듈: `nf_fwrite2d_mod`, `nf_fwrite2d_bry_mod`(경계), `nf_fwrite3d_mod`, `nf_fwrite3d_bry_mod` (`wrt_his.F:60-67`).

> 헤더 주석 `wrt_his.F:15-18`: *"Notice that only momentum is affected by the full time-averaged masks. If applicable, these mask contains information about river runoff and time-dependent wetting and drying variations."*

---

## 6. nf_fwrite2d / nf_fread2d — 분산 격자장 ↔ NetCDF (핵심 병렬 계층)

`nf_fwrite2d.F:11-13` *"This module writes out a generic floating point 2D array into an output file using either the standard NetCDF library or the Parallel-IO (PIO) library."*

### 6.1 인터페이스 분기
`nf_fwrite2d.F:77-82`: generic `nf_fwrite2d` = `nf90_fwrite2d` (+ PIO 시 `pio_fwrite2d`).

### 6.2 입력 인자 의미 (헤더 `:17-50`)
- `gtype` — 격자 타입. **음수면 water point 만 기록** (`:34`).
- `Ascl` — write 전 스케일 인자 (`:43`).
- `Amask` — land/sea 마스크 (`:42`).
- `ExtractField` — 0=추출안함 / 1=보간추출 / >1=decimation 추출 (`:47-50`).
- `SetFillVal` — 육지에 fill value 설정 (`:45-46`).

### 6.3 직렬-vs-병렬 분기
- `PARALLEL_IO && DISTRIBUTE` 빌드(`nf_fwrite2d.F:86-`): 각 프로세스가 PIO 로 자기 타일을 직접 write. `pack_field2d` 로 타일 데이터 패킹 (`:519-520`) 후 `nf90_put_var(ncid, ncvarid, Awrk, start, total)` (`:551`).
- 비-PARALLEL_IO 분산 빌드(`nf90_fwrite2d`, `:89-`): `mp_collect` 로 전 타일을 마스터에 모은 뒤 단일 write.
  - 일반 격자(`gtype>0`): `nf90_put_var(ncid, ncvarid, Awrk, start, total)` (`:295`).
  - water-point 압축(`gtype<0`): `CALL mp_collect (ng, model, Npts, IniVal, Awrk)` (`:356`) → `nf90_put_var(ncid, ncvarid, Awrk(Istr:), start, total)` (`:379`).
- 통계: `CALL stats_2dfld (...)` 로 min/max 산출 (`:560`).

> `POSITIVE_ZERO` 매크로 주석 `nf_fwrite2d.F:58-64`: F95 부호있는 0(-0/+0) 때문에 직렬·병렬 출력이 달라질 수 있어, 병렬 분할 버그 추적 위해 "positive zero" 강제.

### 6.4 입력 대칭 (nf_fread2d)
`nf_fread2d.F` — read 후 **scatter**: `nf90_get_var(ncid, ncvarid, wrk, start, total)` (`nf_fread2d.F:358`, `:482`, `:997`) 로 전역장 읽은 뒤 `mp_scatter2d` 로 각 타일에 분배 (`:1035`). 사용 분산 루틴 `mp_bcastf/mp_bcasti/mp_scatter2d` (`:727`).

3D/4D·경계(bry)·추출(xtr) 변형: `nf_fread3d`/`nf_fread4d`/`nf_fread2d_bry`/`nf_fread3d_bry`/`nf_fread2d_xtr`/`nf_fread3d_xtr`, write 측도 동형 (`nf_fwrite3d`/`nf_fwrite4d`/`*_bry`).

---

## 7. 입력 계층 — get_* / read_*

### 7.1 격자·상태 read (get_grid/get_state)
- `get_grid.F:13-14` *"This module reads grid information from input file using either the standard NetCDF library or the Parallel-IO (PIO) library."* — `mod_netcdf`(+ PIO 시 `mod_pio_netcdf`) 사용 (`:30-33`), 결과를 `mod_grid` 에 적재.
- `get_state.F:11-12` *"This routine reads in requested model state from specified NetCDF file. It is usually used to read initial conditions."*

### 7.2 시변 강제장 read + 시간 보간 (get_2dfld)
`get_2dfld.F` 헤더 *"This routine reads in requested 2D field (point or grided) from specified NetCDF file. Forward time processing."* (`:19-20`). reverse(adjoint) 버전은 `get_2dfldr.F`, 3D는 `get_3dfld(r)`, non-grided는 `get_ngfld(r)`.

시간 메타데이터를 per-field 상태배열에 보관·갱신:
- 정수 메타 `Iinfo(:,ifield,ng)`: Vtype/Vid/Tid/Nrec/Vsize/Tindex/Trec (`get_2dfld.F:243-250`).
- 실수 메타 `Finfo(:,ifield,ng)`: Tmin/Tmax/Clength/Tscale/Tmono/Fmin/Fmax (`:251-254`, `:359-360`, `:398`).
- 순환 강제(cycling): `Finfo(7)=Tmono`, `Tintrp(Tindex,ifield,ng)=Tmono` 로 단조시간 적재 (`:397-399`); 주석 `:389-390`: *"a cycle length. Load time value (sec) into \"Tintrp\" which used ..."*. get_2dfld 는 두 시간 스냅샷을 읽어두고, 실제 시간보간 계수 적용은 set_2dfld(다른 노트 영역)이 담당.
- `get_cycle.F` — 강제장 순환 주기 내 적절한 레코드 위치 계산 헬퍼.

### 7.3 표준입력 파라미터 read (read_*)
`read_phypar.F:11` *"This routine reads and reports physical model input parameters."* — `roms.in` 형식 키워드 입력을 파싱(8237 라인). 하위 분야별:
- `read_biopar`(생물)·`read_sedpar`(퇴적)·`read_icepar`(해빙)·`read_vegpar`(식생)·`read_stapar`(station)·`read_fltpar`/`read_fltbiopar`(floats)·`read_asspar`(데이터동화)·`read_couplepar`(모델 결합).

read_*는 NetCDF 가 아닌 **텍스트 표준입력** 파서다(파일명·스위치를 받아 이후 get_*/def_* 가 사용). NetCDF I/O 자체는 아니나 I/O 설정 진입점.

---

## 8. 공통 패턴 요약

| 패턴 | 근거 |
|---|---|
| 모든 def/wrt/get/nf_ 모듈이 nf90 + PIO 듀얼 구현을 generic INTERFACE 로 추상화 | `def_dim.F:24-29`, `nf_fwrite2d.F:77-82` |
| 오류 전파: `FoundError(status, nf90_noerr, __LINE__, MyFile)` → `exit_flag=3; ioerror=status` | `def_dim.F:96-100`, `def_var.F:166-171` |
| 비-PARALLEL_IO 분산: `OutThread`/`Master` 만 호출, 결과 `mp_bcast*` broadcast | `def_dim.F:94-113` |
| write = (gather/pack) → `nf90_put_var`; read = `nf90_get_var` → (scatter) | `nf_fwrite2d.F:295,379,551`; `nf_fread2d.F:358,1035` |
| def_*/wrt_* 출력 파일별 1:1 쌍, 변수 ID는 구조체 `<F>(ng)%Vid(idXxx)` 에 보존 | `def_his.F:558`, `wrt_his.F:270` |
| 시간 레코드(unlimited)는 wrt_* 의 `%Rindex` 가 증분 관리 | `wrt_his.F:235,257` |

---

## 9. 미확인 / 후속 (source-needed)

- `netcdf_open`/`netcdf_close`/`netcdf_enddef`/`netcdf_redef`/`netcdf_sync` 내부 구현 라인 — PUBLIC 선언만 확인(`mod_netcdf.F:117-126`), 본체 미정독. ⚠ 미확인.
- set_2dfld/set_3dfld 의 실제 시간보간 계수(`fac1`/`fac2`) 적용 — 본 노트 범위 밖(numerics 계열, 별도 노트 담당).
- 4D-Var 전용 def/wrt (def_hessian·def_lanczos·def_norm·def_std·wrt_state 등) 세부 — 헤더만 식별, 구조는 [[roms_4dvar]]/[[roms_adjoint_framework]] 와 교차. source-needed.
- `def_var.F` UGRID 위상 속성(`face_dimensions` 등) 의 전체 조건부 분기 — 대표 라인만 인용.
