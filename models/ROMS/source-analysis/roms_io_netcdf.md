---
title: "ROMS NetCDF I/O — def_·wrt_·get_·nf_ 계열 파일 구조와 병렬 I/O"
model: ROMS
component: ROMS/Utility
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Utility, roms/ROMS/Modules). mod_netcdf.F (INTERFACE 오버로딩·netcdf_create cmode), def_dim.F·def_var.F (nf90/PIO 듀얼 인터페이스·nf90_def_var·deflate), def_his.F (파일 생성·차원·변수 정의), wrt_his.F (Rindex 시간레코드 write·nf_fwrite), nf_fwrite2d.F·nf_fread2d.F (gather/scatter·water-point packing), get_2dfld.F·get_grid.F·get_state.F·read_phypar.F 헤더·핵심 로직 file:line 인용. 2026-10-14 ROMS recovery 대조 보고서 반영"
last_source_check: "2026-10-14 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_support_modules.md
  - models/ROMS/README.md
---

# ROMS NetCDF I/O — def_·wrt_·get_·nf_ 계열

> ROMS의 디스크 입출력 전체를 담당하는 Utility/ 의 NetCDF I/O 계층 분석. 파일/차원/변수 **정의**(`def_*`, 23개) → **출력**(`wrt_*`, 20개) → **입력**(`get_*` 18개, `read_*` 10개) → **저수준 병렬 read/write 래퍼**(`nf_f(re|w)rite*`, 12개) 의 4단 구조. (경로: roms/ROMS/Utility/, mod_netcdf 는 roms/ROMS/Modules/)

ROMS의 많은 수치 커널과 I/O 파일은 `cppdefs.h`를 포함한다([build-options-history:RBH-3504](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안)).
독립 유틸리티에는 예외가 있다(`ROMS/Utility/yaml_parser.F:1`, `ROMS/Utility/get_env.F:1`).
상위 I/O 계층의 `def_info`는 같은 generic 이름 아래 `def_info_nf90`를 제공한다(`ROMS/Utility/def_info.F:75–80`).
`PIO_LIB`와 `DISTRIBUTE`가 정의되면 `def_info_pio`도 제공한다(`ROMS/Utility/def_info.F:77–79`).
하위 `netcdf_*`와 `pio_netcdf_*` 호출 이름은 서로 다르다(`ROMS/Modules/mod_netcdf.F:38–45`, `ROMS/Modules/mod_pio_netcdf.F:42–49`).

---

## 1. 4단 I/O 계층 개요

| 계층 | 파일 prefix | 개수 | 역할 |
|---|---|---|---|
| 저수준 generic 래퍼 | `mod_netcdf` (Modules) | 1 모듈 | nf90 라이브러리 호출 단일 인터페이스화 (`netcdf_create/open/close/get_*/put_*`) |
| 파일·차원·변수 정의 | `def_*` | 23 | NetCDF 파일 생성, 차원/변수/속성 정의 (define mode) |
| 격자장 출력 | `wrt_*` | 20 | 시간 레코드별 모델 필드를 출력 파일에 write |
| 격자장 입력 | `get_*` (18), `read_*` (10) | 28 | 초기/경계/강제·격자 read, 표준입력 파라미터 read |
| 분산 2D/3D/4D read/write | `nf_fread*` / `nf_fwrite*` | 12개 .F 파일 | NetCDF·PIO 분기는 §6을 따른다. |

같은 접미사의 `def_*`·`wrt_*` 파일이 있는 출력 종류에는 his(history), avg(time-average), rst(restart), ini(initial), dai(자료동화 분석 초기조건 또는 EnKF 재시작), diags, floats, station, quick, tides가 있다. 예는 `def_his.F`·`wrt_his.F`와 `def_rst.F`·`wrt_rst.F`이다. (`ROMS/Utility/`의 해당 파일명) [10-14 전수 검증 정정]

위 표의 12개는 Utility의 `nf_fread*.F` 7개와 `nf_fwrite*.F` 5개를 센 값이다([outputs-metadata:OMD-N016](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#4-노트-대조와-수정안)).

출력 파일 종류 (헤더 주석):
- `def_his.F:11` — `This module creates output HISTORY file ...`
- `def_rst.F:11` — `This module creates ouput restart file ...` (원문 오타 verbatim)
- `def_ini.F:11` — `This module open existing nonlinear model initial conditions file ...`
- `def_avg`(time-average)·`def_dai`(자료동화 분석 초기조건 또는 EnKF 재시작)·`def_diags`(diagnostics)·`def_quick`(quick-save)·`def_tides`·`def_floats`·`def_station`·`def_extract`. 4D-Var 전용: `def_hessian`·`def_lanczos`·`def_norm`·`def_std`·`def_state`·`def_impulse`·`def_error`. GST(고유값): `def_gst`.

`def_dai`는 `FOUR_DVAR` 또는 `ENKF_RESTART` 조건에서 자료동화 분석 초기조건 또는 EnKF 재시작 파일을 정의한다(`ROMS/Utility/def_dai.F:3`, `ROMS/Utility/def_dai.F:12–15`).

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

PUBLIC 진입점 (`mod_netcdf.F:117-128`): `netcdf_check_dim`, `netcdf_check_var`, `netcdf_close`, `netcdf_create`, `netcdf_enddef`, `netcdf_get_dim`, `netcdf_get_satt`, `netcdf_inq_var`, `netcdf_inq_varid`, `netcdf_open`, `netcdf_redef`, `netcdf_sync`.

### 2.2 외부 자료형 결정 (CPP 조건부)
출력 부동소수 외부표현은 cppdefs 매크로로 결정:
- `NF_FOUT` = `OUT_DOUBLE` 시 `nf90_double`, 아니면 `nf90_real` (`mod_netcdf.F:189-193`)
- `NF_FRST` (restart) = `RST_SINGLE` 시 `nf90_real`, 아니면 `nf90_double` (`:192-196`)
- `NF_TOUT` (시간·깊이 변수) = 항상 `nf90_double` — 주석 `:203-205`: *"It is set to double precision for accuaracy in both single and douple precision numerical kernel"* (원문 오타 verbatim)

### 2.3 파일 생성 모드 (CMODE)
`#if defined HDF5 || defined PARALLEL_IO` 분기는 `CMODE = nf90_netcdf4`를 선택한다(`ROMS/Modules/mod_netcdf.F:215–216`).
`#elif defined OUT_NETCDF4` 분기도 `CMODE = nf90_netcdf4`를 선택한다(`ROMS/Modules/mod_netcdf.F:217–218`).
일반 기본은 `nf90_64bit_offset`이다(`ROMS/Modules/mod_netcdf.F:220`).
`PARALLEL_IO` 생성은 `my_cmode=IOR(CMODE, nf90_mpiio)`로 `nf90_mpiio`를 추가한다(`ROMS/Modules/mod_netcdf.F:9696`).

(`netcdf_create` SUBROUTINE 본체: `mod_netcdf.F:9642-9775`)

---

## 3. 정의 계층 — def_dim / def_var

### 3.1 듀얼 인터페이스 패턴 (nf90 + PIO)
`def_dim`은 **표준 NetCDF용 `*_nf90` 와 PIO용 `*_pio`** 두 구현을 generic interface 로 묶는다(PIO는 `PIO_LIB && DISTRIBUTE` 조건부, `def_dim.F:24-29`). `def_his`는 PUBLIC wrapper와 PRIVATE backend 구성이므로 동일 generic 구조로 일반화하지 않는다(`def_his.F:71-79`). `def_dim.F:24-29`:
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
`def_var.F:11` *"This routine defines the requested NetCDF variable"*.
`Vinfo`는 변수 정의 정보를 담는 `Natt=26`개의 문자열 슬롯이다(`ROMS/Modules/mod_ncparam.F:114`, `ROMS/Utility/def_var.F:127`).
첫 슬롯은 변수 이름이다(`ROMS/Utility/def_var.F:34`).
`Vinfo`는 이름·조건·자료형 정보를 함께 운반한다([outputs-metadata:OMD-N018](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#4-노트-대조와-수정안)).
26번째 `range`는 NetCDF와 PIO 출력부에서 별도 속성으로 처리한다(`ROMS/Utility/def_var.F:59`, `ROMS/Utility/def_var.F:1000–1004`, `ROMS/Utility/def_var.F:2029–2033`).
`Aval` 실수배열은 add_offset/valid_min/valid_max/missing/C-grid-type/fill 값을 운반한다(`def_var.F:26-32`).

핵심 호출:
- 스칼라(`nVdim==1 && Vdim(1)==0`): `nf90_def_var(ncid, TRIM(Vinfo(1)), Vtype, varid=Vid)` (`def_var.F:160-162`)
- 일반 다차원: `nf90_def_var(ncid, TRIM(Vinfo(1)), Vtype, Vdim(1:nVdim), Vid)` (`:162-164`)
- 압축: `DEFLATE && OUT_NETCDF4` 시 `nf90_def_var_deflate(ncid, Vid, shuffle, deflate, deflate_level)` (다차원 변수 한정, `def_var.F:176-190`)
- 속성: `nf90_put_att(...)` 반복으로 CF 메타·UGRID 위상(`cf_role`·`topology_dimension`·`node_dimensions`·`face_dimensions` 등, `def_var.F:200-347`) 기록.

> 주석 `def_var.F:76-77`: *"Notice that arrays \"Aval\" and \"Vinfo\" is destroyed on output to facilitate the definition of the next variable."* — 호출자가 같은 버퍼를 재사용하도록 함.

---

## 4. def_his — history 파일 정의 흐름 (대표 def_* 본체)

`def_his.F` (6575 라인) 가 `def_*` 의 전형. `def_his_nf90` 의 단계:

1. **파일명 설정·보고** `def_his.F:172-184` (`ncname=HIS(ng)%name`).
2. **신규 파일 생성** — `DEFINE : IF (ldef)` 분기 (`:192`) → `CALL netcdf_create (ng, model, TRIM(ncname), HIS(ng)%ncid)` (`:193`).
3. **차원 정의** `:199-` — `DimIDs=0` 초기화 후 C-grid 스태거 차원 일괄 정의: `xi_rho/xi_u/xi_v/xi_psi`, `eta_rho/eta_u/eta_v/eta_psi` (`def_his.F:203-233`), 경계조정 시 `IorJ`(`:237-241`), water-point 압축 시 `xy_rho/xy_u`(`WRITE_WATER && MASKING`, `:243-249`). 차원 크기는 `IOBOUNDS(ng)%xi_rho` 등 I/O 경계 구조에서 가져옴.
4. **변수 정의** — `status=def_var(...)` 를 변수마다 반복. 시간변수부터(`HIS(ng)%Vid(idtime)`, `def_his.F:562`), 이어 wet/dry 마스크(`idPwet/idRwet/idUwet/idVwet`, `:596-647`), 깊이(`idpthR/U/V/W`), 자유표면(`idFsur`), 운동량·추적자 등. 각 변수 ID는 `HIS(ng)%Vid(...)` 에 저장돼 wrt_* 가 참조.

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
`pio_fwrite2d`는 `#if defined PIO_LIB && defined DISTRIBUTE` 조건에서 제공된다(`ROMS/Utility/nf_fwrite2d.F:79–80`).

### 6.2 입력 인자 의미 (헤더 `:17-50`)
- `gtype` — 격자 타입. **음수면 water point 만 기록** (`:34`).
- `Ascl` — write 전 스케일 인자 (`:43`).
- `Amask` — land/sea 마스크 (`:42`).
- `ExtractField` — 0=추출안함 / 1=보간추출 / >1=decimation 추출 (`:47-50`).
- `SetFillVal` — 육지에 fill value 설정 (`:45-46`).

### 6.3 직렬-vs-병렬 분기
`#if defined PARALLEL_IO && defined DISTRIBUTE`의 표준 NetCDF 경로는 각 노드가 자기 타일을 직접 쓴다(`ROMS/Utility/nf_fwrite2d.F:86`, `ROMS/Utility/nf_fwrite2d.F:286–295`).
이 경로의 쓰기 호출은 `nf90_put_var(ncid, ncvarid, Awrk, start, total)`이다(`ROMS/Utility/nf_fwrite2d.F:295`).

그 외 표준 NetCDF 쓰기 경로는 `pack_field2d`를 호출한다(`ROMS/Utility/nf_fwrite2d.F:394`, `ROMS/Utility/nf_fwrite2d.F:519–527`).
분산 실행의 gather 호출은 `#ifdef DISTRIBUTE` 안의 `IF (Extract_Flag.ge.0) THEN`에 있다(`ROMS/Utility/pack_field.F:697`, `ROMS/Utility/pack_field.F:712–718`).
실제 쓰기는 `IF (OutThread) THEN` 아래의 `nf90_put_var(ncid, ncvarid, Awrk, start, total)`이다(`ROMS/Utility/nf_fwrite2d.F:550–551`).

- 통계: `CALL stats_2dfld (...)` 로 min/max 산출 (`:560`).

> `POSITIVE_ZERO` 매크로 주석 `nf_fwrite2d.F:58-64`: F95 부호있는 0(-0/+0) 때문에 직렬·병렬 출력이 달라질 수 있어, 병렬 분할 버그 추적 위해 "positive zero" 강제.

### 6.4 입력 대칭 (nf_fread2d)
`#if defined PARALLEL_IO && defined DISTRIBUTE`의 표준 NetCDF 경로는 각 노드가 자기 타일을 직접 읽는다(`ROMS/Utility/nf_fread2d.F:78`, `ROMS/Utility/nf_fread2d.F:339–358`).
그 외 경로에서는 `InpThread`가 읽는다(`ROMS/Utility/nf_fread2d.F:996–997`).
이 경로의 `IF (.not.interpolate) THEN` 안에서 `DISTRIBUTE`가 정의되면 `mp_scatter2d`를 호출한다(`ROMS/Utility/nf_fread2d.F:1030–1040`).
이 표준 NetCDF 경로에서 보간이 필요하고 `DISTRIBUTE`가 정의되면 `mp_bcastf`를 호출한다. 보간이 필요한 경우는 `regrid_nf90` 경로를 따른다([outputs-metadata:OMD-N021](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#4-노트-대조와-수정안), `ROMS/Utility/nf_fread2d.F:1070–1085`). [10-14 전수 검증 정정]
`IF (.not.interpolate) THEN` 안에서 `DISTRIBUTE`가 없으면 배열을 직접 푼다(`ROMS/Utility/nf_fread2d.F:1030–1045`). [10-14 전수 검증 정정]

일반 격자의 3D·4D reader는 `nf_fread3d`·`nf_fread4d`이다([outputs-metadata:OMD-N022](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#4-노트-대조와-수정안)).
경계(bry) reader는 `nf_fread2d_bry`·`nf_fread3d_bry`이다([outputs-metadata:OMD-N022](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#4-노트-대조와-수정안)).
추출(xtr) reader는 `nf_fread2d_xtr`·`nf_fread3d_xtr`이다([outputs-metadata:OMD-N022](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#4-노트-대조와-수정안)).
경계·추출 차원은 일반 2D·3D 격자 차원과 구분한다([outputs-metadata:OMD-N022](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#4-노트-대조와-수정안)).
대응 writer에는 `nf_fwrite3d`·`nf_fwrite4d`·`*_bry`가 있다([outputs-metadata:OMD-N022](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md#4-노트-대조와-수정안)).

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
`read_phypar.F:11` *"This routine reads and reports physical model input parameters."* — `roms.in` 형식 키워드 입력을 파싱한다.
입력 처리의 코드 판은 HEAD `57aecf58`이다. `Ngrids` 입력은 `CASE ('Ngrids')`에서 읽는다(`ROMS/Utility/read_phypar.F:171–173`; [inputs:RI1-1044](../../../_staging/recovery/compare/roms-inputs-vs-code.md#5-차이-결론)). [10-14 전수 검증 정정]
하위 분야별:
- `read_biopar`(생물)·`read_sedpar`(퇴적)·`read_icepar`(해빙)·`read_vegpar`(식생)·`read_stapar`(station)·`read_fltpar`/`read_fltbiopar`(floats)·`read_asspar`(데이터동화)·`read_couplepar`(모델 결합).

read_*는 NetCDF 가 아닌 **텍스트 표준입력** 파서다(파일명·스위치를 받아 이후 get_*/def_* 가 사용). NetCDF I/O 자체는 아니나 I/O 설정 진입점.

MCT는 `read_couplepar`를 사용한다(`ROMS/Utility/read_couplepar.F:2`, `ROMS/Utility/read_couplepar.F:102`).
native ESMF는 `mod_esmf_esm`의 입력 판독을 사용한다(`Master/mod_esmf_esm.F:1598`).
CMEPS는 YAML 설정을 읽는다(`Master/cmeps_roms.h:726`).

---

## 8. 공통 패턴 요약

| 패턴 | 근거 |
|---|---|
| `def_dim`·`nf_fwrite2d`는 nf90 + 조건부 PIO 구현을 generic INTERFACE 로 추상화; `def_his`는 PUBLIC wrapper/PRIVATE backend 구성 | `def_dim.F:24-29`, `nf_fwrite2d.F:77-82`, `def_his.F:71-79` |
| 오류 전파: `FoundError(status, nf90_noerr, __LINE__, MyFile)` → `exit_flag=3; ioerror=status` | `def_dim.F:96-100`, `def_var.F:167-172` |
| 비-PARALLEL_IO 분산: `OutThread`/`Master` 만 호출, 결과 `mp_bcast*` broadcast | `def_dim.F:94-113` |
| `#if defined PARALLEL_IO && defined DISTRIBUTE`의 NetCDF 경로는 타일을 직접 읽고 쓴다. | `ROMS/Utility/nf_fread2d.F:78,339–358`, `ROMS/Utility/nf_fwrite2d.F:86,286–295` |
| 그 외 쓰기 경로는 `pack_field2d`를 호출한다. | `ROMS/Utility/nf_fwrite2d.F:519–527` |
| 분산 쓰기의 gather는 `IF (Extract_Flag.ge.0) THEN` 안에 있다. | `ROMS/Utility/pack_field.F:697,712–718` |
| 그 외 읽기 경로의 scatter 조건은 `DISTRIBUTE`와 `IF (.not.interpolate) THEN`이다. | `ROMS/Utility/nf_fread2d.F:1030–1040` |
| 이 표준 NetCDF 보간 경로는 `DISTRIBUTE`가 정의되면 broadcast를 사용한다. [10-14 전수 검증 정정] | `ROMS/Utility/nf_fread2d.F:1070–1074` |
| 비분산 읽기 경로는 `IF (.not.interpolate) THEN` 안에서 배열을 직접 푼다. [10-14 전수 검증 정정] | `ROMS/Utility/nf_fread2d.F:1030–1045` |
| def_*/wrt_* 출력 파일별 1:1 쌍, 변수 ID는 구조체 `<F>(ng)%Vid(idXxx)` 에 보존 | `def_his.F:562`, `wrt_his.F:270` |
| 시간 레코드(unlimited)는 wrt_* 의 `%Rindex` 가 증분 관리 | `wrt_his.F:235,257` |

---

## 9. 관련 구현 위치

- `netcdf_open`/`netcdf_close`/`netcdf_enddef`/`netcdf_redef`/`netcdf_sync`의 PUBLIC 선언: `mod_netcdf.F:119-128`.
- 시간보간 계수(`fac1`/`fac2`) 적용: `set_2dfld`/`set_3dfld`. (`ROMS/Utility/set_2dfld.F:116–124`, `ROMS/Utility/set_3dfld.F:126–135`) [10-14 전수 검증 보완]
- 자료동화 파일의 관련 설명: [roms_4dvar](roms_4dvar.md)·[roms_adjoint_framework](roms_adjoint_framework.md). [10-14 전수 검증 정정]
- SGRID 위상 속성(`face_dimensions` 등)의 대표 기록부: `ROMS/Utility/def_var.F:196–203,230–233`. [10-14 전수 검증 정정]

### 9.1 정규화 파일의 생성·조회와 LCZ 레코드

`def_norm`은 `SELECT CASE (NRM(ifile,ng)%IOtype)`으로 표준 NetCDF와 PIO를 구분한다(`ROMS/Utility/def_norm.F:68–74`).
PIO 경로의 조건은 `# if defined PIO_LIB && defined DISTRIBUTE`이다(`ROMS/Utility/def_norm.F:72–74`).
`DEFINE : IF (LdefNRM(ifile,ng)) THEN`은 파일 생성 분기이다(`ROMS/Utility/def_norm.F:151`).
`QUERY : IF (.not.LdefNRM(ifile,ng)) THEN`은 기존 파일의 변수·차원을 조회한다(`ROMS/Utility/def_norm.F:1094–1114`). [10-14 전수 검증 보완]
`LdefNRM=F, LwrtNRM=T` 조합은 기존 파일에 새 정규화 값을 계산하여 쓴다([da-4dvar:DA1-659](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md#5-차이-결론), `ROMS/Utility/normalization_mono.h:3590`).
LCZ에는 추가 다음 벡터를 포함한 `Ninner+1` 레코드가 있다(`ROMS/Utility/ini_lanczos.F:24–26`).
감도에 사용하는 Q의 열 수는 `Ninner`이다([da-4dvar:DA1-305](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md#5-차이-결론)).
감도 초기화는 LCZ의 추가 마지막 레코드를 제외한다(`ROMS/Utility/ini_lanczos.F:26`).

## 문서와 코드 차이 (10-14 대조)

차이 표: [roms_io_netcdf-differences.md](roms_io_netcdf-differences.md).
결론별 개수: A 37행, B 85행, C 67행, D 27행, E 5행, F 16행, 합계 237행([배정표](../../../_staging/recovery/assign/)의 `ROMS-assign-*.tsv`에서 3열이 `source-analysis/roms_io_netcdf.md`인 행을 집계).
