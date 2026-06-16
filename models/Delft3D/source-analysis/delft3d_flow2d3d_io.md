---
title: "Delft3D flow2d3d I/O — MD-file 입력 파싱·his/map/dr·restart·NEFIS/NetCDF 출력 layer"
model: Delft3D
component: flow2d3d/flow2d3d_io
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/flow2d3d/packages/flow2d3d_io/src/). input/readmd.f90 마스터 디스패처 call 시퀀스(573-909), input/rdrund.f90 legacy search/readnc 키워드 메커니즘(98-131), input/rdmeteo.f90 modern prop_get(199-485), output/postpr.f90 his/map/rst 트리거 로직(930-1206), output/wrh_main.f90 NEFIS/NetCDF 이중 백엔드 + REQUESTTYPE_DEFINE/WRITE 2-pass(329-534), output/wrtarray.f90 typed-rank putelt/nf90_put_var dispatch(101-296), input/rstfil.f90 restart precision 자동감지(166-232), preprocessor/tdatom.f90 시변 데이터 중간파일 생성(598-718) file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
---

# Delft3D flow2d3d I/O — MD-file 입력·his/map/dr·restart·NEFIS/NetCDF 출력 layer

> flow2d3d_io: 구조격자 Delft3D-FLOW 의 입출력 계층. MD-file 파싱(`input/`), 시변 데이터 전처리(`preprocessor/`), his/map/dr/com/restart 결과 쓰기(`output/`).
> 경로: src/engines_gpl/flow2d3d/packages/flow2d3d_io/src/

이 노트는 dispatcher/compute 노트가 다루지 않는 **I/O 계층 자체**(파일 포맷, 키워드 파싱 메커니즘, 출력 트리거)에 집중한다. 격자/시그마-z 자료구조는 [[delft3d_sigma_z]], 시뮬레이션 분배는 [[delft3d_flow2d3d_dispatcher]], 퇴적·형태 출력 내용물은 [[delft3d_sediment_morphology]], WAQ 결합은 [[delft3d_delwaq]] 참조.

디렉토리 규모: `input/` 95, `output/` 99, `preprocessor/` 27 파일. 전수 전사 대신 대표 파일·메커니즘 위주로 정리.

## 1. 입력 계층 (`input/`)

### 1.1 readmd — MD-file 마스터 디스패처

`readmd` 의 역할 (헤더 verbatim, `input/readmd.f90:38`):
```
!    Function: - Reads all records from the MD-file
```
`readmd` 는 직접 파싱하지 않고 **그룹별 rd* 서브루틴을 순차 호출**하는 오케스트레이터다. 호출 시퀀스 (`input/readmd.f90`):

| 호출 | 라인 | 읽는 내용 |
|---|---|---|
| `rdrund` | 573 | 모델 설명(run description) |
| `rdxyzo` | 581 | 격자 좌표·layer thickness·anglat/anglon |
| `rdgrid` | 590 | 격자 파일(enclosure·dry point·thin dam·cut-cell) |
| `rdspec` | 600 | discharge source 등 special point |
| `rddept` | 608 | 수심(depth) |
| `rdbndd` | 619 | open boundary 정의 (`nto>0`일 때만) |
| `rdic` | 644 | 초기조건(initial condition) |
| `rdbcg` / `rdibch` | 658/675 | 경계조건 일반/천문조(astronomical) |
| `rdproc` | 726 | 물리 프로세스 on/off (salinity·htur2d 등) |
| `rdnum` | 741 | 수치 파라미터 |
| `rdstru` | 762 | 구조물(structure) |
| `rdfour` | 800 | Fourier 분석 정의 (`fourier`일 때) |
| `rdtimo` | 810 | 출력 타이밍(his/map/restart interval) |
| `rdsedmortra` | 841 | 퇴적·형태·이송 |
| `rdmeteo` | 925 | 기상(meteo) 항목 + meteo 모듈 초기화 |

각 rd* 는 `error` 반환 후 `if (error) goto 9999` 로 단락(short-circuit)된다 (`input/readmd.f90:575,586` 등).

### 1.2 두 가지 키워드 파싱 메커니즘 (legacy vs modern)

**(A) Legacy: record-pointer + `search`/`readnc`** — `rdrund` 예 (`input/rdrund.f90:98-113`):
```fortran
keyw = 'Runtxt'
call search(lunmd, lerror, newkw, nrrec, found, ntrec, mdfrec, itis, keyw, lkw, 'NO')
if (found) then
   call readnc(lunmd, lerror, keyw, newkw, nlook, mdfrec, thulp, tdef, lenc, nrrec, ...)
```
`search` 가 MD-file 안에서 키워드(`keyw`)를 record-pointer `nrrec` 부근에서 찾고, `readnc` 가 값을 읽는다. `tdef` 는 default 값, not-found 시 기본값 fallback (`input/rdrund.f90:120-124`). `search`/`readnc` 자체는 이 디렉토리 밖 공유 유틸 — ⚠ 미확인(위치).

**(B) Modern: property tree + `prop_get`** — `rdmeteo` 예 (`input/rdmeteo.f90:199-205`):
```fortran
call prop_get(gdp%mdfile_ptr,'*','Filwnd',filename)
   call prop_get(gdp%mdfile_ptr,'*','Wnsvwp',value)
      call prop_get(gdp%mdfile_ptr,'*','Wndgrd',value)
```
`gdp%mdfile_ptr` 는 MD-file 을 미리 파싱해 둔 property tree 핸들이고 `prop_get(tree, '*', key, out)` 로 키 조회(`input/rdmeteo.f90` 전반, 199-485 다수). 신규 reader 들이 이 방식으로 이행 중. `rdmeteo` 헤더(`input/rdmeteo.f90:32-33`):
```
!    Function: - Read meteo related items
!              - Initialize meteo module
```
바람/기압 파일 키워드 다수: `Filwnd`(199), `Filwu/Filwv/Filwp`(264/277/290), spiderweb `Filweb`(343), space-varying `Filspv`(246) 등.

### 1.3 restart 입력 (`rstfil` + `restart_trim_*`)

`rstfil` — unformatted single/double precision restart 파일 읽기 (헤더 `input/rstfil.f90:36-37`):
```
!    Function: Reads initial field condition records from an
!              unformatted (single precision) restart file
```
파일 탐색 우선순위 (`input/rstfil.f90:166-174`):
1. `tri-rst.<restid>.<idate>.<itime>` (날짜·시각 포함)
2. `tri-rst.<restid>` (구버전)
3. `<restid>.dat/.def` (NEFIS trim-file) → `restart_trim_flow` 호출(`input/rstfil.f90:183`)

unformatted restart 의 **precision 자동 감지**: 첫 record를 direct access(`recl=4`)로 읽어 byte length `l` 추출 후 `iprec = l/nmaxgl/mmaxgl` 로 4(single)/8(double) 판정 (`input/rstfil.f90:210-221`):
```fortran
read (luntmp, rec=1) l
iprec = l/nmaxgl/mmaxgl
if (iprec==4) then
    ftype = FTYPE_UNFORM32
elseif (iprec==8) then
    ftype = FTYPE_UNFORM64
```
판정 결과는 `dfbroadc_gdp` 로 모든 partition에 broadcast (`input/rstfil.f90:228`), 로그에 precision 기록(`230-232`).

NEFIS trim-file restart `restart_trim_flow` 는 `use properties, only: prop_get` 로 시간정보를 파싱(`input/restart_trim_flow.f90:40-42`), 헤더는 "Reads initial field condition records from a trim-file"(`input/restart_trim_flow.f90:36`). 관련: `restart_trim_bdf`(bed form), `restart_trim_fluff`, `restart_trim_lyrs`(층상 bed), `restart_trim_roller` (파일명 기준 역할).

## 2. 시변 데이터 전처리 (`preprocessor/`)

### 2.1 tdatom — 시변 입력 → 중간 unformatted 파일

`tdatom` 헤더 (`preprocessor/tdatom.f90` 32-39 verbatim):
```
!    Function: Reads and writes the time dependent data from the
!              MD-file and or attribute file to standard unfor-
!              matted file for the simulation
!              Optional extra function for astronomical tide
!              Create extra intermediate file which smallest
!              end time of all time dependent data
```
즉 시변 경계·discharge·기상·열 데이터를 미리 읽어 **simulation kernel이 빠르게 읽을 unformatted scratch 파일**로 변환한다. 호출되는 reader (`preprocessor/tdatom.f90`):

| reader | 라인 | 데이터 |
|---|---|---|
| `rdbch` | 598 | 천문 경계(harmonic) → `lunbch` unformatted 기록(`608`) |
| `rdbcq` | 628 | QH 관계 경계 |
| `rdbct` | 648 | 시계열 경계(time series) |
| `rdbcc` | 662 | 경계 농도(concentration) |
| `rddis` | 677 | discharge 시계열 |
| `rdbcb` | 693 | (bubble/기타 경계) |
| `rdheat` | 704 | 열속(heat flux) |
| `rdeva` | 718 | 증발/강수(evaporation) |

중간 파일 생성 예 (`preprocessor/tdatom.f90:604-608`): "Write an unformatted intermediate file with ..." 주석 후 `open(newunit=lunbch, ..., form='unformatted')`.

천문조 보조: `bewvuf`(astronomical components V/U/F factors), `kompbs`, `asc`, `datumi` — astronomical tide 전처리 유틸(파일명 기준).

## 3. 출력 계층 (`output/`)

### 3.1 postpr — 출력 마스터 트리거

`postpr` 헤더 (`output/postpr.f90:37-41` verbatim):
```
!    Function: - Checks whether the current time step requires an
!                output
!              - Updates the cross sections informations at each
!                time step
!              - Activates the output routines
```
매 time step `nst` 마다 호출돼, **현재 step 이 각 출력 interval counter 와 일치하면** 해당 writer를 호출한다. 핵심 분기 (`output/postpr.f90`):

| 조건 | 라인 | 동작 |
|---|---|---|
| `nst==ithisc .or. nst==iphisc` | 930 | `tstat`/`tstat_sed` 로 station 통계 산출 (931-959) |
| `nst==iphisc` | 976 | `prthis` — ASCII 인쇄 출력(print HIS) |
| `nst==ithisc` | 996 | `wrh_main` — binary HIS 파일 쓰기 + `ithisc += ithisi`(1004) |
| `nst==itmapc` (itmapi>0) | 1039 | `wrm_main` — MAP 파일 쓰기 + `itmapc += itmapi`(1060) |
| `drogue .and. nst==itdroc` | 1069 | `wrd_main` — drogue(부유표) 파일 + `itdroc += itdroi`(1078) |
| fourier | 1109-1188 | `wrfou` — Fourier 분석 결과 |
| `nst==itrstc` | 1199 | `wrirst` — restart 파일 + `itrstc = min(itrstc+itrsti, itfinish)`(1206) |

counter 의미 (`output/postpr.f90:355-360`): `itdroc`(drogue), `ithisc`(history), `itmapc`(MAP), `itrstc`(restart) = "Current time counter". 각 출력 후 counter 를 interval 만큼 전진시켜 다음 출력 시각 예약. com-file(통신 파일, wave 결합용) 은 `wrcomt`(`output/postpr.f90:769`)로 별도 — 매번 첫 record 덮어써 파일 비대화 방지(`output/postpr.f90:760` 주석 "keep overwriting first record to avoid huge com-file").

### 3.2 NEFIS/NetCDF 이중 백엔드 + 2-pass define/write

`wrh_main` ("Main routine for writing the FLOW HIS file", `output/wrh_main.f90:33`)는 출력 포맷을 런타임에 선택한다 (`output/wrh_main.f90:329-330`):
```fortran
filetype = getfiletype(gdp, FILOUT_HIS)
if (filetype == FTYPE_NETCDF) filename = trim(filename)//'.nc'
```
**2-pass 패턴**: define 후 write (`output/wrh_main.f90:365-368`):
```fortran
do irequest = REQUESTTYPE_DEFINE, REQUESTTYPE_WRITE
   ! request REQUESTTYPE_DEFINE: define all groups, dimensions, and elements
   !         REQUESTTYPE_WRITE : write the data
```
- DEFINE pass 는 첫 호출(`first`)·master node 에서만 수행, 기존 파일 삭제(`delnef`, `output/wrh_main.f90:371-373`).
- NEFIS: `open_datdef` 로 `.dat`/`.def` 쌍 생성(`output/wrh_main.f90:382-387`).
- NetCDF: `nf90_create` + CF-1.6 global attribute(`Conventions`/`institution`/`source`/`history`) 부여(`output/wrh_main.f90:392-405`).

`wrh_main` 이 호출하는 그룹별 writer (`output/wrh_main.f90`): 시간독립 `wrihis`(415)·`wrihisbal`(433)·`wrihisdad`(437), 시간종속 `wrthis`(447)·`wrthisbal`(471)·`wrsedh`(475, 퇴적)·`wrthisdad`(488). NetCDF 차원 정의는 `defnewgrp`(507). `wridoc` 는 version 그룹을 쓰며 **defnewgrp 이후**에 호출돼야 함(주석 `output/wrh_main.f90:527-529`, 호출 534). MAP 측은 `wrm_main`(`output/postpr.f90:1040`)이 대칭 구조.

`wridoc` ("Writes the initial group 4 ('"ftype"-version')", `output/wridoc.f90:32`)는 그룹명을 `grnam4 = ftype(1:3) // '-version'` 로 구성(`output/wridoc.f90:110`) — 예 `his-version`, 버전 문자열은 `getfullversionstring_flow2d3d`(`output/wridoc.f90:117`).

### 3.3 wrtarray — typed/rank generic NEFIS·NetCDF 쓰기 모듈

`output/wrtarray.f90` 은 module 로, `interface wrtvar` 가 int/sp/hp × 0~5 차원 procedure 를 묶는다 (`output/wrtarray.f90:45-58`). 각 procedure 가 백엔드를 `select case(ftype)` 로 분기 (예 `wrtarray_*`, `output/wrtarray.f90:132-152`):
```fortran
case (FTYPE_NEFIS)
   ierr = putelt(fds, grpnam_nfs, varnam_nfs, uindex, 1, var)
case (FTYPE_NETCDF)
   ierr = nf90_put_var(fds, idvar, var, start=(/ itime /))
```
2D/3D 는 `count`/`start` 에 차원·시간 인덱스 추가(`output/wrtarray.f90:222,296`). 즉 모든 grouped 출력이 이 단일 추상화로 NEFIS `putelt` 와 NetCDF `nf90_put_var` 를 동시 지원. restart writer `wrirst` 도 `use wrtarray, only: wrtarray_nm, wrtarray_nmk, wrtarray_nmkl` 로 (n,m)/(n,m,k)/(n,m,k,l) 배열을 쓴다(`output/wrirst.f90:44`), 헤더 "writes the relevant output arrays to the (single precision) restart file"(`output/wrirst.f90:35-36`).

### 3.4 기타 출력 writer (역할 요약)

대표 파일만 (file:line 헤더 미확인분은 파일명 기준 역할 — source-needed):
- `wrcomi`/`wrcomt`/`wrcomwind`: com-file(wave 결합 통신) 시간독립/종속/바람.
- `wrsedm`/`wrsedh`/`wrsedmavg`/`wrsedmgrp`/`wrmorm`/`wrmorst`: 퇴적·형태 MAP/HIS/평균/restart (내용물은 [[delft3d_sediment_morphology]]).
- `wrwaq*`(F90 다수: `wrwaqcco`/`wrwaqhyd`/`wrwaqvol`/`wrwaqflo`/`wrwaqpnt` 등): WAQ 수질 모델용 hydrodynamic coupling 파일 생성. `wrwaqfil` 은 `postpr` 에서 호출됨(`output/postpr.f90:809`). WAQ 결합 전반은 [[delft3d_delwaq]].
- `wrfou`/`wrfous`/`wrfouv`/`fouana`: Fourier 분석 결과 (scalar/vector).
- `wrirst`/`wrrolm`(roller)/`wrhfluff`·`wrmfluff`(fluff layer): restart 계열.
- `wrboun`/`wridoc`/`wrgrid`/`wridro`/`wrtdro`: 경계·doc·격자·drogue.

## 4. 요약 — I/O 계층 아키텍처

1. **입력**: `readmd` 가 그룹별 rd* 디스패치. 키워드 파싱은 legacy `search`/`readnc`(record-pointer) 와 modern `prop_get`(property tree) 가 공존, 신규 코드는 후자로 이행(`input/rdmeteo.f90` vs `input/rdrund.f90`).
2. **전처리**: `tdatom` 가 시변 데이터를 unformatted 중간파일로 변환해 kernel 읽기 비용 절감(`preprocessor/tdatom.f90:32-39`).
3. **출력 트리거**: `postpr` 가 매 step counter(`ithisc`/`itmapc`/`itdroc`/`itrstc`) 일치 검사로 writer 활성화·counter 전진(`output/postpr.f90:996-1206`).
4. **출력 포맷**: 런타임 `getfiletype` 으로 NEFIS(`.dat`/`.def`) 또는 NetCDF(CF-1.6 `.nc`) 선택, 모든 writer 가 REQUESTTYPE_DEFINE→WRITE 2-pass + `wrtarray` generic 추상화로 두 백엔드 동시 지원(`output/wrh_main.f90:329-534`, `output/wrtarray.f90:132-152`).
5. **restart**: 입력측 precision 자동감지(`input/rstfil.f90:215`), 출력측 single-precision `wrirst`(`output/wrirst.f90:35`).

⚠ 미확인/source-needed: `search`/`readnc` 구현 위치(공유 util), 3.4 의 헤더 미인용 writer 들의 정확한 그룹명·element. 본 노트는 인용한 file:line 범위에 한해 verified.
