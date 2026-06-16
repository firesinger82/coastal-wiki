---
title: "Delft3D D-Flow FM 자료구조·I/O·time manager — m_flow/m_flowgeom/m_flowtimes + unstruc_netcdf + flow_externaloutput"
model: Delft3D
component: dflowfm/data-io-manager
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/). dflowfm_data(m_flow·m_flowgeom·m_flowtimes·m_flowparameters·m_transport·unstruc_model), dflowfm_io(unstruc_netcdf·unc_write_his·wrimap·caching·read_restart_from_map·unstruc_netcdf_incremental), dflowfm_manager(flow_externaloutput·inctime_user·flow_usertimestep) 의 module 헤더·변수 선언 주석·subroutine 본체를 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
---

# Delft3D D-Flow FM 자료구조 · I/O · time manager

> D-Flow FM(비구조 격자 엔진)의 전역 상태 자료구조 module, NetCDF/his/map/rst I/O 계층, time manager 를 분석한다.
> 경로: `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/` 의 `dflowfm_data/` · `dflowfm_io/` · `dflowfm_manager/`.

> ⚠ 경로 주의: 배정 프롬프트의 `engines_gpl/packages/...` 가 아니라 실제 트리는 `engines_gpl/dflowfm/packages/dflowfm_kernel/src/...` 이다. 이하 상대경로는 모두 `dflowfm/packages/dflowfm_kernel/src/` 기준.

스킴·수치해법은 [[delft3d_dflowfm_kernel_scheme]], 개요는 [[delft3d_dflowfm_overview]], MDU 입력은 [[delft3d_dflowfm_mdu_input]], sigma/z 층은 [[delft3d_sigma_z]] 참조. 본 노트는 **자료구조 module 의 변수군 + I/O 호출 흐름**에 집중한다.

---

## 1. 전역 상태 자료구조 (dflowfm_data/)

D-Flow FM 은 거대한 module 변수 집합으로 모델 상태를 보유한다 (객체지향 X, module-global allocatable 배열 중심). 핵심 4 module:

| module | 파일 | 라인 | 역할 |
|---|---|---|---|
| `m_flow` | `dflowfm_data/m_flow.f90:33` | 733 | flow 상태 배열(수위·유속·유량·염분·온도·3D 층) |
| `m_flowgeom` | `dflowfm_data/m_flowgeom.f90:35` | 356 | flow 격자 기하(node/link 번호체계·연결·기하 가중치) |
| `m_flowtimes` | `dflowfm_data/m_flowtimes.f90:34` | 397 | time manager(시각·시간간격·출력 interval) |
| `m_flowparameters` | `dflowfm_data/m_flowparameters.f90` | 1017 | 수치·물리 옵션 스위치(iadvec, itstep 등) |

### 1.1 m_flow — flow 상태 배열

module 선언부 주석 `module m_flow ! flow arrays-999` (`m_flow.f90:33`). 다수의 sub-data module 을 `use`: `fm_external_forcings_data`, `m_flowparameters`, `m_turbulence`, `m_vegetation`, `m_heatfluxes`, `m_physcoef` 등 (`m_flow.f90:34-45`).

**노드 관련 배열 (dim = ndx, 수위점/셀중심):**
- `s0(:)` / `s1(:)` — 타임스텝 시작/끝 수위 (m). `m_flow.f90:160-161`. 주석 `[m] waterlevel (m ) at start/end of timestep {"location": "face", "shape": ["ndx"]}`.
- `hs(:)` — 셀 중심 수심 = s1 - bl. `m_flow.f90:171` (`[m] waterdepth at cell centre = s1 - bl (m)`).
- `vol0(:)`/`vol1(:)` — 타임스텝 시작/끝 총부피 (m3). `m_flow.f90:166-167`.
- `a0(:)`/`a1(:)` — 저류면적 (m2). `m_flow.f90:164-165`.
- `ucx`/`ucy`/`ucz` — 셀 중심 속도 글로벌 x/y/z 성분 (m/s). `m_flow.f90:192-194`. `ucmag` 속도 크기 `m_flow.f90:199`.

**링크 관련 배열 (dim = lnkx, 속도점/엣지):**
- `u0(:)`/`u1(:)` — 타임스텝 시작/끝 유속 (m/s). `m_flow.f90:295-296`.
- `q1(:)` — 유량 (m3/s) at end of timestep n. 주석에 `used as q0 in timestep n+1, statement q0 = q1 is out of code, saves 1 array` (`m_flow.f90:298`) — 메모리 절약을 위해 q0 배열을 별도 유지하지 않는 설계.
- `au(:)` — u 점에서의 흐름면적 (m2). `m_flow.f90:304`.
- `qa(:)` — advection 용 유량 `qa=au(n)*u1(n+1)` `m_flow.f90:300`.

**스칼라 수송(노드, dim = ndkx):**
- `sa0`/`sa1` 염분(ppt), `m_flow.f90:269-270` (단위 메타 `[1e-3]`).
- `tem0`/`tem1` 수온(degC), `m_flow.f90:275-276`.

**3D 층 자료구조 (`m_flow.f90:49-156`):**
- `kmx` — 3D 층 수, `kmx==0 → 2D code, kmx==1 → 3D code` (`m_flow.f90:50-51`).
- `ndkx` — 3D flow 노드 차원(내부+경계), `m_flow.f90:54`. `lnkx` — 3D flow 링크 차원, `m_flow.f90:56`.
- 층 압축 인덱스: `kbot(:)`/`ktop(:)` — 각 ndx 수평 셀의 바닥/상단 층 셀 번호 (`m_flow.f90:128-129`), `Lbot(:)`/`Ltop(:)` — 각 lnx 수평 링크의 바닥/상단 엣지 (`m_flow.f90:132-133`). 즉 3D 셀은 (수평셀 × 가변 수직층)을 1차원 압축 인덱싱.
- `zws(:)` — 셀중심(s점)에서의 인터페이스(w점) z 레벨 (m), `m_flow.f90:106`. 주석에 ASCII 다이어그램으로 `zws(0)=interface(0)=bl`, `zws(ktop)=s1` 구조 도해 (`m_flow.f90:109-123`).
- 층 타입 상수: `LAYTP_SIGMA=1`, `LAYTP_Z=2`, `LAYTP_POLYGON_MIXED=3`, `LAYTP_DENS_SIGMA=4` (`m_flow.f90:70-73`).

### 1.2 m_flowgeom — flow 격자 기하·번호체계

D-Flow FM 의 핵심 **번호 규약(numbering convention)** 이 이 module 주석에 명시되어 있다.

**Flow node 번호체계** (`m_flowgeom.f90:82-86`, verbatim):
```
1:ndx2D, ndx2D+1:ndxi, ndxi+1:ndx1Db, ndx1Db+1:ndx
^ 2D int ^ 1D int      ^ 1D bnd       ^ 2D bnd ^ total
```
즉 2D 내부 → 1D 내부 → 1D 경계 → 2D 경계 순으로 배열. 관련 차원: `ndxi`(내부 셀=2D+1D, `m_flowgeom.f90:101`), `ndx1db`(+1D 경계, `m_flowgeom.f90:102`). `ndx2d`/`ndx`는 gridgeom 의 `m_cell_geometry` 로 이동됨 (`m_flowgeom.f90:88-93`).

**Flow link 번호체계** (`m_flowgeom.f90:124-126`, verbatim):
```
1:lnx1d, lnx1d+1:lnxi, lnxi+1:lnx1Db, lnx1Db+1:lnx
^ 1D int ^ 2D int      ^ 1D bnd       ^ 2D bnd ^ total
```
차원: `lnx1D`(1D 링크 수, `m_flowgeom.f90:127`), `lnxi`(내부 1D+2D, `m_flowgeom.f90:128`), `lnx`(전체, `m_flowgeom.f90:130`).

**핵심 연결·기하 배열:**
- `nd(:)` — flow node administration, type `tnode` (`m_flowgeom.f90:103`). `tnode` 정의 `m_flowgeom.f90:47-56`: `ln`(연결 링크 번호, `>0` 들어오는·`<0` 나가는), `nod`(net node 매핑), `nwx`/`nw`(벽 연결).
- `ln(2,*)` — 링크의 node 행정(좌/우 셀번호). `m_flowgeom.f90:131`.
- `lncn(2,*)` — 2D 링크의 corner(net node) 행정. `m_flowgeom.f90:133`.
- `kcu(:)` — 링크 코드: `1=1D link, 2=2D link, -1=bc 1D, -2=bc 2D, 3=lateral_1d2d_link, 4=longitudinal_1d2d_link, 5=street_inlet, 7=roof_gutter` (`m_flowgeom.f90:134`).
- `bl(:)` — bottom level (m, 양수 위쪽). `m_flowgeom.f90:111`.
- `dx(:)`/`wu(:)` — 링크 길이/폭 (m). `m_flowgeom.f90:140,142`. `dxi`=1/dx (`m_flowgeom.f90:141`).
- `iadv(:)` — 링크별 advection 타입. `m_flowgeom.f90:137`.
- `ln2lne`/`lne2ln` — flow link ↔ net link 번호 매핑 (`m_flowgeom.f90:193-194`).
- 가중치 배열군: `wcx1/wcy1/wcx2/wcy2`(center 벡터 cartesian 성분 가중, `m_flowgeom.f90:163-166`), `acl`(left dx 분율 alfacl, `m_flowgeom.f90:154`), `csu`/`snu`(u0,u1 의 cos/sin 성분, `m_flowgeom.f90:159-160`).

### 1.3 m_transport — 다중 스칼라 수송 자료구조

module 헤더 주석(`m_transport.f90:33-43`)에 전송 module 의 자료 규약이 verbatim 으로 기술됨:
- 모든 constituent 는 `constituents` 배열에 저장. 염분·온도는 `sa1`/`tem1` 에서 채우고 복사함.
- tracer 는 constituents 배열의 **맨 뒤**에 위치, 번호 `ITRA1`~`ITRAN` (`m_transport.f90:40,55-56`).

`m_transportdata` (`m_transport.f90:45`) 핵심:
- `NUMCONST` 총 constituent 수 (`m_transport.f90:48`), `isalt`/`itemp` 인덱스 (`m_transport.f90:50-51`), `ised1`/`isedn` 첫/끝 sediment fraction (`m_transport.f90:52-53`).
- `constituents(:,:)` — `dim(NUMCONST,Ndkx)` (`m_transport.f90:62`).
- `itrac2const`/`ifrac2const` — tracer/sediment fraction → constituent 번호 매핑 (`m_transport.f90:60-61`).

`m_transport` (`m_transport.f90:72`): `fluxhor`/`fluxver` 수평/수직 플럭스 (`m_transport.f90:77-78`), tridiag 계수 `a,b,c,d`·`sol`·`e` (`m_transport.f90:96-97`), local timestepping 용 `nsubsteps`/`ndeltasteps`/`jaupdate` (`m_transport.f90:101-103`). 자세한 수송 알고리즘은 [[delft3d_fm_compute_aux]] / 커널 노트 참조.

### 1.4 m_flowparameters — 수치·물리 옵션 스위치

- `itstep` — time step 방식: `0=no, 1=step_explicit, 2=step_reduce, 3=step_jacobi, 4: explicit` (`m_flowparameters.f90:39`).
- `iadvec` — advection 타입: `0=no, 1=Wenneker vol, ... 3/4=Perot, 5~12=Piaczek 변형, 20=Energy conserving compact` (`m_flowparameters.f90:40-46`).
- `Perot_type` — 셀중심 속도 ucx,ucy 의 Perot 가중 타입. 상수 `PEROT_WIDTH_BASED=0`, `PEROT_AREA_BASED=1`, `PEROT_VOLUME_BASED=2` (`m_flowparameters.f90:60-74`).
- `icorio`/`newcorio` — Coriolis 가중 (`m_flowparameters.f90:82-84`).

---

## 2. time manager (m_flowtimes + dflowfm_manager/)

### 2.1 m_flowtimes — 시각·간격 변수

module 주석: `this module contains the real flow times, only to be managed by setting times in module m_usertimes` (`m_flowtimes.f90:33`).

**기준일·사용자 시각:**
- `refdat` 기준일 문자열(e.g. '20090101'), 모든 시각은 이에 상대 (`m_flowtimes.f90:39`). `refdate_mjd` modified Julian date (`m_flowtimes.f90:41`).
- `tstart_user`/`tstop_user` — 사용자 지정 시작/종료 (s) (`m_flowtimes.f90:69,71`).
- `dt_user` — 외력 갱신용 사용자 timestep (s) (`m_flowtimes.f90:47`). `time_user` 다음 외력 갱신 시각 (`m_flowtimes.f90:72`).
- `dt_max` 사용자 계산 timestep 상한 (`m_flowtimes.f90:49`), `dt_init` 첫 스텝 (`m_flowtimes.f90:50`).

**내부 계산 시각:**
- `dts` 내부 계산 timestep (s), `dti`=1/dts (`m_flowtimes.f90:74,77`).
- `time0`/`time1` — s0/s1 의 현재 julian (s), `time1 = time0 + dt` (`m_flowtimes.f90:84-85`).

**자동 timestep(CFL):** `autotimestep` 스위치 + 파라미터 상수군 `AUTO_TIMESTEP_2D_OUT=1`, `AUTO_TIMESTEP_3D_HOR_OUT=3`, `AUTO_TIMESTEP_3D_HOR_INOUT=4`, `AUTO_TIMESTEP_3D_INOUT=5`, `AUTO_TIMESTEP_OFF=0` 등 (`m_flowtimes.f90:52-64`). 기본값 `autotimestep = AUTO_TIMESTEP_2D_OUT` (`m_flowtimes.f90:232`).

**출력 interval (각 출력형식마다 별도):**
- `ti_map`/`ti_his`/`ti_rst`/`ti_com`/`ti_waq` — map/his/restart/com/waq 출력 간격 (s) (`m_flowtimes.f90:102,105,121,111,125`). 각각 시작/끝(`ti_maps`/`ti_mape` 등) 보유 (`m_flowtimes.f90:103-104`).
- `time_map`/`time_his`/`time_rst`/`time_waq` — 다음 출력 시각 (`m_flowtimes.f90:152,157,159,161`).
- snapshot 카운터: `it_map`/`it_his`/`it_rst`/`it_waq` (`m_flowtimes.f90:172,175,177,178`).
- time-splitting: `ti_split` + `ti_split_unit`(Y/M/D/h/m/s) — 신규 his/map 파일 생성 주기 (`m_flowtimes.f90:141-143`).

기본값은 `default_flowtimes()` (`m_flowtimes.f90:220`)에서 설정: `refdat='20010101'`, `dt_user=120.0`, `dt_max=30.0`, `dtmin=1.0e-4`, `dt_fac_max=1.1` (`m_flowtimes.f90:221-231`).

### 2.2 manager — user timestep 루프

`flow_usertimestep` (`dflowfm_manager/flow_usertimestep.f90:44`) 주석 `A complete single user time step (init-run-finalize)` (`flow_usertimestep.f90:33`). 3단계 순차 호출:
1. `flow_init_usertimestep` (`flow_usertimestep.f90:62`)
2. `flow_run_usertimestep` — `do computational flowsteps until timeuser` (`flow_usertimestep.f90:67`)
3. `flow_finalize_usertimestep` (`flow_usertimestep.f90:72`)
각 단계마다 `iresult /= DFM_NOERR` 검사 후 `goto 888` 로 탈출 (`flow_usertimestep.f90:63-76`). 타이머 `handle_user` 로 user time loop 계측 (`flow_usertimestep.f90:57,77`).

`inctime_user` (`dflowfm_manager/inctime_user.F90:81`): `time1 >= time_user` 일 때 `time_user += dt_user`, `tstop_user` 로 클램프, `dnt_user += 1` (`inctime_user.F90:84-90`). 즉 외력 갱신 시각을 dt_user 만큼 전진시키는 단순 카운터.

---

## 3. NetCDF I/O 계층 (dflowfm_io/)

### 3.1 unstruc_netcdf — 중앙 NetCDF 모듈

`module unstruc_netcdf` (`dflowfm_io/unstruc_netcdf.f90:44`). **18,974 라인**으로 dflowfm_io 의 핵심. UGRID(`io_ugrid`) + `netcdf` 라이브러리 사용 (`unstruc_netcdf.f90:48,51`).

**Convention 상수:**
- `UNC_CONV_CFOLD = 1` (구 CF 전용), `UNC_CONV_UGRID = 2` (신 CF+UGRID) (`unstruc_netcdf.f90:85-86`). map 출력 시 `iconv` 분기 (`unstruc_netcdf.f90:5285-5312`).

**열린 파일 관리:** 모든 NetCDF 는 `unc_open`/`unc_create` 통해 열어 추적, `unc_closeall` 로 일괄 종료 (`unstruc_netcdf.f90:71-77`). 최대 `maxopenfiles = 50` (`unstruc_netcdf.f90:74`), 배열 `open_files_`/`open_datasets_`/`nopen_files_` (`unstruc_netcdf.f90:75-77`).
- `unc_open` (`unstruc_netcdf.f90:2469`): `nf90_open` 래퍼 + 추적 리스트 등록.
- `unc_create` (`unstruc_netcdf.f90:2490`): `nf90_create` 래퍼, `cmode_ = ior(cmode, unc_cmode)` 로 전역 cmode 합성 (`unstruc_netcdf.f90:2498`), 성공 시 `unc_addglobalatts` 호출 (`unstruc_netcdf.f90:2508`).
- `unc_close` (`unstruc_netcdf.f90:2518`): 추적 리스트에서 데이터셋 탐색 후 제거.

**메타데이터 무결성:** 사용자 metadata 파일로 덮어쓸 수 없는 forbidden 속성 19개 — `references`, `source`, `history`, `Conventions`, `uuid`, `date_created`, `geospatial_*`, `time_coverage_*` (`unstruc_netcdf.f90:104-125`). 환경변수로 설정 가능한 속성: `creator_name`/`creator_email`/`creator_url` (env `DFM_META_<NAME>`) (`unstruc_netcdf.f90:127-133`).

**id 관리 타입:**
- `t_unc_timespace_id` (`unstruc_netcdf.f90:139-185`): 반복 쓰기용 시간·공간 행정. UGRID mesh id(`meshids1d/2d/3d`, `network1d`), 차원 id(`id_timedim`=유일한 `nf90_unlimited`, `id_laydim`, `id_wdim`), `idx_curtime`(최신 snapshot 인덱스, `unstruc_netcdf.f90:181`).
- `t_unc_mapids` (`unstruc_netcdf.f90:190`): map 파일별 NetCDF id 전체 집합 — `ncid` 파일포인터 + `id_tsp`(timespace) + 변수 id 군(`id_s1`, `id_hs`, `id_vol1`, `id_au`, `id_taus`...). `MAX_ID_VAR=4` (1D/2D/3D/1D2D 격자부) (`unstruc_netcdf.f90:97,232-243`).

**핵심 쓰기 subroutine:**
- `unc_write_map` (`unstruc_netcdf.f90:5273`) → conv 분기 → `unc_write_map_filepointer_ugrid` (`unstruc_netcdf.f90:5312`) 또는 `unc_write_map_filepointer` (`unstruc_netcdf.f90:8282`, CF-old).
- `unc_write_rst`/`unc_write_rst_filepointer` (`unstruc_netcdf.f90:2931,2950`) — restart 파일.
- `unc_write_net`/`unc_write_net_ugrid2` (`unstruc_netcdf.f90:11197,11903`) — net(grid) 파일.
- `unc_write_flowgeom` (`unstruc_netcdf.f90:15405`) / `..._ugrid` (`unstruc_netcdf.f90:15665`) — flow geometry 파일.
- 3D geom: `unc_append_3dflowgeom_def`/`_put` (`unstruc_netcdf.f90:2750,2826`).

**변수 정의/put helper:** `unc_def_var_map` (`unstruc_netcdf.f90:843`, location code 로 1D/2D/3D 일반화), `unc_put_var_map_real`/`_dble`/`_int`/`_byte` (`unstruc_netcdf.f90:1380,1411,1349,1711` — iloc 위치코드별 데이터 put).

**읽기(restart/net):**
- `unc_read_net`/`unc_read_net_ugrid` (`unstruc_netcdf.f90:12975,12433`).
- `unc_read_map_or_rst` (`unstruc_netcdf.f90:13445`) — map/restart 파일에서 상태 복원.
- `unc_read_merged_map` (`unstruc_netcdf.f90:14818`) — 병합 map(병렬 partition 통합)에서 읽기. `get_var_and_shift`/`assign_restart_data_to_local_array` (`unstruc_netcdf.f90:13270,13215`) 로 partition shift 처리.

### 3.2 unc_write_his — history(관측점) 출력

별도 파일 `dflowfm_io/unc_write_his.F90` (1741 라인). public 진입점 `unc_write_his(tim)` 주석 `Write history data in NetCDF format` (`unc_write_his.F90:84`, 별칭 `wrihis`). 모듈 변수로 station/구조물별 dim·var id 를 대량 보유: 관측점 `id_statdim`/`id_statx`/`id_staty`/`id_statname` (`unc_write_his.F90:45,44`), 횡단면 `id_crsdim`/`id_crs_id` (`unc_write_his.F90:44,50`), 구조물별 id(weir/gate/pump/culvert/dambreak/source...) (`unc_write_his.F90:49-64`). 즉 his 파일은 0차원(점) 시계열 + 구조물 시계열 전용.

### 3.3 wrimap 래퍼 + map class(incremental)

- `wrimap(tim)` (`dflowfm_io/wrimap.f90:34`): map 파일 ncid 가 없으면 `unc_create` 로 생성 (`wrimap.f90:79-92`), conv 에 따라 `unc_write_map_filepointer_ugrid` (`wrimap.f90:106`) 또는 `unc_write_map_filepointer` (`wrimap.f90:112`) 호출, 후 `nf90_sync` (`wrimap.f90:116-120`). 타이머 세분화(`handle_extra(80~83)`)로 inq/create/write/sync 계측.
- `unstruc_netcdf_map_class.f90` (module `unstruc_netcdf_map_class`, `unstruc_netcdf_incremental.f90:32`): class map(분류된 수위/수심/속도 클래스) UGRID 출력. `write_map_classes_ugrid` (`unstruc_netcdf_incremental.f90:97`), `put_in_classes`/`classes_to_classbounds` helper (`unstruc_netcdf_incremental.f90:512,631`). 정수 클래스로 양자화하여 저장 → 용량 절감.

### 3.4 caching — 격자 기반 정보 캐시

`module unstruc_caching` (`dflowfm_io/caching.f90:38`) 주석 `Manages the caching file - store and retrieve the grid-based information` (`caching.f90:37`). 격자 의존 전처리 결과(crossed flow links, thin dams, netcell, cross sections, 관측점 매핑)를 캐시 파일에 저장/복원하여 재시작 전처리 비용 절감. store: `caching.f90:580` 이하, load: `caching.f90:207` 이하, partition 간 동기화 포함 (`caching.f90:187`). 호환성 검사 `caching.f90:182`.

### 3.5 restart 진입

`read_restart_from_map(filename, ierr)` (`dflowfm_io/read_restart_from_map.f90:43`) — restart 의 얇은 래퍼 (53줄). 실제 복원은 unstruc_netcdf 의 `unc_read_map_or_rst` 가 담당.

---

## 4. 출력 dispatcher (dflowfm_manager/flow_externaloutput)

`module m_flow_externaloutput` (`dflowfm_manager/flow_externaloutput.F90:33`), public `flow_externaloutput(tim)`.

subroutine 주석(verbatim): `Write solution data to output files (map/his/restart/waq). Each output type has its own interval (see m_flowtimes), and output is only written if the current time tim exceeds the last written interval.` (`flow_externaloutput.F90:48-51`).

**호출 흐름 (각 출력형식 독립 분기):**
1. `inctime_split(tim)` — time-split 파일 경계 갱신 (`flow_externaloutput.F90:92`).
2. **his**: `ti_his > 0 .and. tim >= time_his` 이면 (병렬 시 `my_rank==0` 에서만) `unc_write_his(tim)` 호출 (`flow_externaloutput.F90:94-101`). 통계 출력은 `finalize_average`/`reset_statistical_output` 로 감쌈 (`flow_externaloutput.F90:96-104`). 다음 시각 `time_his` 갱신은 `floor((tim-ti_hiss)/ti_his)` 기반 (`flow_externaloutput.F90:113-118`).
3. **map**: `ti_map > 0 .or. ti_mpt(1) > 0` 이고 `tim >= time_map` 이면, 1D 출력용 업데이트(freeboard/depth-on-ground/vol-on-ground/s1gradient) 후 wrimap (`flow_externaloutput.F90:129-152` 이하).

`tim` 인자 주석: `Current time, should in fact be time1, since all writers use s1, q1, etc.` (`flow_externaloutput.F90:86`) — 모든 writer 가 타임스텝 끝 상태(s1, q1)를 쓰므로 time1 을 넘겨야 함.

각 출력 형식의 다음 시각 계산은 `comparereal(tim, time_*, EPS10)` 패턴으로 부동소수 안전 비교 사용 (`flow_externaloutput.F90:95,110,131`).

---

## 5. unstruc_model — 모델 정의·MDU 버전

`unstruc_model.f90` (4385 라인) 은 MDU 파일 파싱·모델 식별·파일명 관리를 담당. 자세한 MDU 키워드는 [[delft3d_dflowfm_mdu_input]] 참조. 본 노트는 자료구조 측면만:
- MDU 포맷 버전: `MDUFormatMajorVersion=1`, `MDUFormatMinorVersion=9` (`unstruc_model.f90:60-61`). 버전 history 주석 `unstruc_model.f90:63-73` (e.g. `1.08: Default density Eckart→UNESCO`).
- ext 파일 버전: `ExtfileNewMajorVersion=2`, minor=2 (`unstruc_model.f90:76-77`).
- `md_ptr` — MDU 를 tree_data 로 파싱한 포인터 (`unstruc_model.f90:101`). `md_ident` 모델 식별자(runid) (`unstruc_model.f90:103`).
- 파일명 변수군: `md_netfile`(net), `md_flowgeomfile`(flowgeom 출력), `md_fixedweirfile` 등 (`unstruc_model.f90:113-122`).

---

## 6. 정리 — 자료/IO 아키텍처 요약

- **상태 보유**: module-global allocatable 배열(`m_flow`/`m_flowgeom`/`m_transport`). 노드(ndx/ndkx)·링크(lnx/lnkx) 두 축, 3D 는 (수평셀×가변층) 압축 인덱스(`kbot/ktop`, `Lbot/Ltop`). (`m_flow.f90:128-133`)
- **번호 규약**: 2D내부→1D내부→1D경계→2D경계 (node), 1D내부→2D내부→1D경계→2D경계 (link). (`m_flowgeom.f90:82-86,124-126`)
- **time 관리**: 사용자 시각(`tstart/tstop/dt_user`) vs 내부 계산 시각(`time0/time1/dts`) 분리, CFL 자동 timestep(`autotimestep`). (`m_flowtimes.f90:47-85`)
- **I/O**: 중앙 `unstruc_netcdf`(18974줄)가 map/rst/net/flowgeom 을 CF-old + UGRID 양 convention 으로 쓰고, his 는 별도 `unc_write_his`, class map 은 `unstruc_netcdf_map_class`. 모든 파일은 추적 리스트(`unc_open/create/closeall`)로 관리. (`unstruc_netcdf.f90:44,2469-2558`)
- **출력 trigger**: `flow_externaloutput` 가 형식별 독립 interval 검사로 dispatch. (`flow_externaloutput.F90:48-152`)

### ⚠ 본 노트 범위 밖 (source-needed / 타 노트)
- ADI/연속방정식 reduce solver: [[delft3d_adi_solver]] (flow2d3d 계열) — D-Flow FM 의 conjugate gradient solver(`m_solver`/`m_reduce`)는 본 노트에서 헤더만 확인, 알고리즘 본체는 별도 검수 필요.
- WAQ I/O(`wrwaq.F90`)·shapefile 출력(`unc_write_shp.F90`): 본 노트 미read, source-needed.
- partition/METIS(`partition_METIS_to_idomain.F90`): 병렬 분할 자료는 본 노트 범위 밖, source-needed.
- ec-module(외력 보간)·구조물 자료(`m_strucs`): 본 노트 미read, source-needed.
