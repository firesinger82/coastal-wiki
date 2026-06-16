---
title: "Delft3D-WAVE 모듈 (SWAN wrapper) — INPUT 생성·grid mapping·flow↔wave 데이터 교환"
model: Delft3D
component: wave/swan-wrapper
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/wave/). swan_tot.f90 의 시간/격자 루프와 run_swan.f90 의 SWAN 호출, swan_input.f90:write_swan_inp 의 SWAN command-file(PROJECT/CGRID/INPGRID/READINP/BOUN NEST/POINTS NGRID/COMPUTE/HOTSTART/STOP) 생성, swan_flow_grid_maps.f90:make_grid_map(mkmap·ESMF) 와 grmap.f90 의 가중평균 보간, get_flow_fields.f90/map_swan_output.f90/wave2com.f90 의 데이터 교환을 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
---

# Delft3D-WAVE 모듈 (SWAN wrapper)

> Delft3D-WAVE 엔진(`src/engines_gpl/wave/`)은 **SWAN 을 구동하는 wrapper** 다. 직접 파동방정식을 풀지 않고 ① FLOW 격자→SWAN 격자로 forcing(수심·수위·유속·바람) 보간 ② SWAN command-file `INPUT` 생성 ③ SWAN 실행(라이브러리/실행파일) ④ SWAN 출력→FLOW com-file 보간·기록 을 담당한다. 본 노트는 WAVE 엔진 **자체**의 호출/데이터교환을 다루며, FLOW 측 결합(파-유 상호작용 항)은 [[wave/delft3d_flow_wave_coupling]] 를 참조.

경로: `src/engines_gpl/wave/`. 패키지 분리:
- `packages/manager/src` — 최상위 오케스트레이션 (`wave_main`, `swan_tot`, `wave_exe`, `wave_bmi`)
- `packages/kernel/src` — SWAN 실행·보간·com 변환 (`run_swan`, `grmap`, `map_swan_output`, `wave2com`, `wave2flow`)
- `packages/io/src` — 격자 데이터 read/write (`get_flow_fields`, `write_swan_datafile`, `read_swan_output`, `put_wave_fields`)
- `packages/data/src` — 자료구조·MDW 입력 파서·SWAN INPUT 생성 (`swan_flow_grid_maps`, `swan_input`, `wave_data`)

---

## 1. 전체 시간 루프 — `swan_tot`

핵심 드라이버는 `packages/manager/src/swan_tot.f90:swan_tot` (인자 `n_swan_grids, n_flow_grids, wavedata, selectedtime`, swan_tot.f90:1). 구조는 **이중 루프**:

- 바깥 루프 `do itide = 1, swan_run%nttide` — 시간(tide/timepoint) 반복 (swan_tot.f90:106)
- 안쪽 루프 `do i_swan = 1, n_swan_grids` — nested SWAN 격자 반복 (swan_tot.f90:137)

한 `(itide, i_swan)` 반복 안에서 일어나는 순서 (swan_tot.f90:140~454):

| 단계 | 호출 | file:line |
|---|---|---|
| 입력장 할당·초기화 | `alloc_input_fields` / `init_input_fields` | swan_tot.f90:141-142 |
| SWAN 수심 read (curvilinear bottom) | `get_swan_depth` | swan_tot.f90:146 |
| FLOW 결과 취득 (n_flow_grids 루프) | `get_flow_fields` | swan_tot.f90:160-167 |
| meteo(바람·기압·해빙) 갱신 | `meteoupdate`/`getmeteoval` | swan_tot.f90:176-235 |
| SWAN forcing 파일 기록 (BOTNOW/CURNOW/WNDNOW/…) | `write_swan_file` | swan_tot.f90:248-336 |
| SWAN command-file 작성 | `write_swan_input` | swan_tot.f90:344 |
| **SWAN 실행** | `run_swan(swan_run%casl)` | swan_tot.f90:354 |
| SWAN 출력 read | `read_swan_output` | swan_tot.f90:378, 404 |
| SWAN→FLOW 격자 매핑 (n_flow_grids 루프) | `map_swan_output` | swan_tot.f90:421-424 |
| WAVE map(.wavm)·NetCDF 기록 | `write_wave_map`/`write_wave_map_netcdf` | swan_tot.f90:433-444 |

시간 루프 종료부에서 com-file 로 결과를 기록한다 (swan_tot.f90:499~536): `wave2flow`(벡터 → 곡선격자 방향, swan_tot.f90:506) → `wave2com`(물리 변환, swan_tot.f90:512) → `put_wave_fields`(com-file 기록, swan_tot.f90:519).

실행모드는 `wavedata%mode` (`packages/data/src/wave_data.f90:40-42`): `stand_alone=0`, `flow_online=1`, `flow_mud_online=2`. stand-alone 일 때만 매 step `setwrite_wavm(...,.true.)` 로 WAVE map 을 항상 쓴다 (swan_tot.f90:91-92).

---

## 2. SWAN 실행 — `run_swan`

`packages/kernel/src/run_swan.f90:run_swan` 의 헤더 주석 (run_swan.f90:32-33):
```
!     *** Run swan; produce output file swanout with values on     ***
!     *** swan computational grid                                  ***
```

두 실행모드 (`swan_input.f90:101-102`: `SWAN_MODE_EXE=0`, `SWAN_MODE_LIB=1`):

- **LIB 모드** (`swan_run%exemode == SWAN_MODE_LIB`, run_swan.f90:65): SWAN 을 내장 함수로 호출 — `call swan(engine_comm_world)` (run_swan.f90:100). MPI 시 `wave_mpi_bcast(SWAN_GO,...)` 로 slave 에 신호 후 `swan(...)`+`wave_mpi_barrier` (run_swan.f90:89-94). 선택적 전처리 스크립트(`swan_run%scriptname`)가 `INPUT` 파일을 생성하면 그것을 사용 (run_swan.f90:69-86).
- **EXE 모드** (else, run_swan.f90:102): `swan.sh`/`swan.bat` 셸 스크립트를 `util_system` 으로 외부 실행 (run_swan.f90:106-120).

SWAN 정상종료 확인은 **`norm_end` 파일 존재**로 판정 — 없으면 `wavestop(1,...)` 으로 중단 (run_swan.f90:127-131). 이후 `PRINT` 진단파일을 `swn-diag.<casl>` 로 append 복사 (run_swan.f90:136-142). 종료 시 SWAN 임시파일(`INPUT`,`PRINT`,`BOTNOW`,`CURNOW`,`AICENOW` 등) 삭제, SWANOUT 데이터파일만 보존 (run_swan.f90:149-161).

---

## 3. SWAN command-file(`INPUT`) 생성 — `write_swan_inp`

WAVE wrapper 의 가장 핵심 부분. `write_swan_input` (swan_input.f90:2407) 은 템플릿모드(`update_swan_inp`, swan_input.f90:2453)가 아니면 `write_swan_inp` (swan_input.f90:2542) 를 호출해 SWAN 텍스트 명령파일을 한 줄씩 작성한다. 주요 명령:

| SWAN 명령 | 의미 | file:line |
|---|---|---|
| `PROJECT` | 프로젝트 헤더 | swan_input.f90:2768 |
| `CGRID` | 계산격자 정의 | swan_input.f90:2871 |
| `INPGRID BOTTOM … / READINP BOTTOM` | 수심 입력격자·파일 | swan_input.f90:2918, 2945 |
| `INPGRID CURREN / READ CUR` | 유속 입력격자 (qextnd(q_cur)>0 또는 swuvi) | swan_input.f90:2967-2977 |
| `INPGRID … / READINP AICE` | 해빙 fraction | swan_input.f90:2999, 3008 |
| `READINP MUDL` | mud level (flow_mud_online) | swan_input.f90:3027 |
| `READINP NPLANTS` | 식생 stem 밀도 | swan_input.f90:3048, 3068 |
| `BOUN NEST / BOUN WWIII / BOUN SHAPE` | 경계조건 (nest·WW3·파라메트릭) | swan_input.f90:3223, 3233, 3248 |
| `INITIAL HOTSTART … NETCDF` | hotfile restart | swan_input.f90:3407-3409, 4281 |
| `GEN1/GEN2/GEN3 KOMEN|WESTH DRAG WU` | 파 생성 물리 | swan_input.f90:3418-3428 |
| `POINTS NGRID### / SPEC … SPEC2D ABS` | **자식 nest 출력** | swan_input.f90:3640-3673 |
| `COMPUTE [STAT|NONSTAT]` | 계산 트리거 | swan_input.f90:4059, 4062, 4091 |
| `STOP` | 종료 | swan_input.f90:4102 |

### 3.1 Grid nesting (부모↔자식 SWAN 격자)

nesting 은 **두 방향**으로 작동:

- **자식이 부모로부터 경계 받기**: 자식 도메인은 `dom%nestnr` (부모 도메인 번호, swan_input.f90:1697 에서 MDW `NestedInDomain` 으로 read)를 갖고, `dom%nesfil(1:4) = 'NEST'` 로 경계파일명을 정한다 (swan_input.f90:1703). 자식 INPUT 에는 `BOUN NEST 'NEST###' CLOSED` 가 기록된다 (swan_input.f90:3394-3400, `inest` 가 `NEST` 접미 3자리).
- **부모가 자식 경계 출력하기**: 부모 격자(`inest`)의 INPUT 에 자식들(`sr%dom(kst)%nestnr == inest`, swan_input.f90:3639)에 대해 `POINTS 'NGRID###' FILE 'SWANIN_NGRID###'` + `SPEC 'NGRID###' SPEC2D ABS 'NEST###'` 를 기록 — 즉 부모 SWAN 이 자식 격자 모서리 점에서 2D 스펙트럼(`SPEC2D ABS`)을 `NEST###` 파일로 출력하고, 그것이 다음 자식 SWAN 의 `BOUN NEST` 입력이 된다 (swan_input.f90:3636-3674).

이 구조 때문에 `swan_tot` 의 안쪽 nest 루프(`i_swan = 1, n_swan_grids`)는 **부모 먼저 자식 나중** 순으로 도메인이 정렬되어 있어, 부모가 만든 `NEST###` 파일을 자식이 곧바로 읽을 수 있다.

### 3.2 정상/비정상 계산 — `modsim`

`swan_run%modsim` (swan_input.f90:202): `0/<=1` 정상, `2` quasi-stationary(`COMPUTE STAT <tendc>`, swan_input.f90:4062), `3` non-stationary(`COMPUTE NONSTAT <tbegc> <deltc> MIN <tendc>`, swan_input.f90:4091-4095). 시각 문자열은 `datetime_to_string(refdate, timsec)` (swan_input.f90:4061, 4069). `modsim=3` + hotfile 사용 시 `usehottime > tbegc` 이면 에러 중단 (swan_input.f90:4080-4085).

### 3.3 Hotfile (restart)

`create_hotstart_line` (swan_input.f90:4256): hotfile 명을 `hot_<inest>_<yyyymmdd>_<hhmmss>.nc` 형식으로 구성(swan_input.f90:4275), 존재하면 `INITIAL HOTSTART '<file>' NETCDF` 줄 생성 (swan_input.f90:4281). 분할(MPI partitioned, `-001` 접미) hotfile 도 처리 (swan_input.f90:4284-4288). 없으면 `usehottime='00000000.000000'` 로 리셋하고 줄을 주석 `$` 처리 (swan_input.f90:4292-4293). `swan_tot` 종료부에서 `swan_run%usehottime = swan_run%writehottime` 으로 다음 step 이 직전 hotfile 을 쓰도록 갱신 (swan_tot.f90:495).

---

## 4. 격자 매핑 (FLOW ↔ SWAN) — `swan_flow_grid_maps`

`packages/data/src/swan_flow_grid_maps.f90` 모듈이 격자/매퍼 자료구조를 정의. 핵심 전역 포인터 (swan_flow_grid_maps.f90:154-160):
```
type(grid), pointer :: swan_grids(:)        ! SWAN 격자들
type(grid), pointer :: flow_grids(:)        ! FLOW 격자들
type(grid_map), pointer :: flow2swan_maps(:,:)  ! FLOW→SWAN 매퍼
type(grid_map), pointer :: swan2flow_maps(:,:)  ! SWAN→FLOW 매퍼
```
`init_grids` 가 `n_swan_grids × n_flow_grids` 매퍼 행렬을 할당 (swan_flow_grid_maps.f90:166-179).

### 4.1 매퍼 생성 — `make_grid_map`

`make_grid_map(i1, i2, g1, g2, gm, external_mapper)` (swan_flow_grid_maps.f90:306) — provider 격자 g1 의 점들을 receiver 격자 g2 각 점에 매핑하는 가중치 테이블을 만든다. 두 경로:

- **내장 매퍼** (`gm%ext_mapper=.false.`, swan_flow_grid_maps.f90:512~): `gm%n_surr_points = 4` (곡선격자 4점), `ref_table(4, npts)`/`weight_table(4, npts)` 할당 후 `mkmap(...)` 호출 — provider 점 인덱스와 가중치를 채운다 (swan_flow_grid_maps.f90:534-548).
- **외부 매퍼 ESMF** (`gm%ext_mapper=.true.`, swan_flow_grid_maps.f90:363~): `ESMF_RegridWeightGen_in_Delft3D-WAVE.sh/.bat` 외부 프로그램으로 weight 파일(NetCDF) 생성 후 (swan_flow_grid_maps.f90:378-394) `col/row/S/frac_b` 변수를 read (swan_flow_grid_maps.f90:437-440). 비구면격자 bilinear 시 `n_b = mmax*nmax` 검증 (swan_flow_grid_maps.f90:418). D-Flow FM 비구조격자(`flowgridfile` 지정)일 때 이 경로를 쓴다.

**coverage(`g2%covered`)**: receiver 점이 provider 격자에 의해 "덮였는지" 표시. 내장 경로는 `mkmap` 이, ESMF 경로는 점이 `msurpnts` 개 이상 유효 source 로 둘러싸이고 도메인 enclosure 폴리곤 내부(`dbpinpol_tpolies`, swan_flow_grid_maps.f90:497)일 때 `covered = i1` 로 설정 (swan_flow_grid_maps.f90:489-501). `msurpnts` 기본 3, Delft3D 비교 시 4 (swan_flow_grid_maps.f90:44-46).

### 4.2 실제 보간 — `grmap`

`packages/kernel/src/grmap.f90:grmap(f1,n1,f2,n2,iref,w,np,iprint)` — receiver 격자 모든 점에 대해 provider 값의 **가중평균**을 계산. 헤더 주석 (grmap.f90:33):
```
! compute interpolated values for all points on grid 2
```
핵심 로직 (grmap.f90:70-87):
$$ F_2(i_2) = \sum_{ip=1}^{np} w(ip, i_2)\, F_1\big(\text{iref}(ip, i_2)\big) $$
grid 1 밖의 점은 `iref(1,i2)=0` → `ifac=1` 로 기존값 유지, 내부 점은 `ifac=0` 으로 초기화 후 누적 (grmap.f90:38-42 주석, 72-74). 즉 **여러 FLOW 도메인이 한 SWAN 격자를 덮을 때**, 각 도메인이 자기가 덮는 부분만 갱신하고 나머지는 보존한다 (`get_flow_fields.f90:185` 주석 "mapping procedure only updates the part of SWAN grid covered by current FLOW domain").

---

## 5. FLOW → SWAN 데이터 (forcing) — `get_flow_fields`

`packages/io/src/get_flow_fields.f90:get_flow_fields` — FLOW 결과를 SWAN 격자로 가져온다. 각 양은 `sr%dom(i_swan)%qextnd(q_*)>0` 일 때만 처리 (인덱스: `q_bath=1, q_wl=2, q_cur=3, q_wind=4, q_veg=5`, swan_input.f90:375-379):

| FLOW 양 | com-file read | 보간 | file:line |
|---|---|---|---|
| 수심 dps | `get_dep` | `grmap`/`grmap_esmf` | get_flow_fields.f90:107-128 |
| 수위 s1 | `get_lev` | `grmap`/`grmap_esmf` | get_flow_fields.f90:142-164 |
| 유속 u1,v1 | `get_cur` → `flow2wav` | `grmap` | get_flow_fields.f90:173-194 |
| 바람 windu,v | `get_wind` | `grmap` | get_flow_fields.f90:231-244 |
| 식생 veg/diaveg/stemheight | `get_var_netcdf` | `grmap_esmf` | get_flow_fields.f90:278-298 |
| mud (dpsmud,s1mud,viscmud) | `get_dep`/`get_lev`/`get_visc` | `grmap` | get_flow_fields.f90:317-352 |

유속은 com-file 격자(곡선격자 u/v 벽점) → **Cartesian cell-center** 로 변환 후 보간한다 — `flow2wav(u1,v1,alfas,guu,gvv,...)` (get_flow_fields.f90:180-182). 두 입력경로 분기: `sr%flowgridfile == ' '` 이면 Delft3D4 **com-file**(`grmap`), 아니면 D-Flow FM **NetCDF**(`grmap_esmf` + ESMF weights) (get_flow_fields.f90:103, 116). 보간 후 SWAN forcing 텍스트파일(`BOTNOW`,`CURNOW`,`WNDNOW`,`MUDNOW`,`VEGNOW`,`AICENOW`)을 `write_swan_file` 로 기록 (swan_tot.f90:248-336).

### 5.1 forcing 외삽 — `write_swan_datafile::extrapolate`

`packages/io/src/write_swan_datafile.f90` 모듈. `write_swan_file` 은 `covered` 마스크가 0 인(=FLOW 가 안 덮은) SWAN 점에 대해 `extrapolate(mmax,nmax,covered,var1,var2)` 로 nearest-valid 값을 채운다 (write_swan_datafile.f90:42, swan_tot.f90 의 `extr_var1 = dom%qextnd(...)==2` 가 외삽 on/off 플래그). `qextnd == 2` 이면 외삽, `== 1` 이면 미덮인 점은 SWAN 기본값에 맡긴다.

---

## 6. SWAN → FLOW 데이터 (결과) — `read_swan_output` → `map_swan_output` → `wave2com` → `put_wave_fields`

### 6.1 SWAN 출력 read — `read_swan_output`

`packages/io/src/read_swan_output.f90` 의 `hisout` 가 SWAN TABLE 출력(`COMPGRID`)을 파싱해 `swan_output_fields` 구조(hs, dir, period, fx, fy, mx, my, dissip(:,:,1..4), ubot, wlen, setup, tps, tm02, tmm10, …, read_swan_output.f90:35-42, swan_flow_grid_maps.f90:110-152)를 채운다. `offset` 으로 출력블록 skip — `modsim=3, calccount=1` 이면 SWANOUT 에 tstart/tend 두 데이터셋이 있어 첫 셋을 offset=0, 둘째를 offset=1 로 두 번 읽는다 (swan_tot.f90:372-404, read_swan_output.f90:85 offset 주석). 방향은 nautical↔Cartesian 변환을 거친다 (read_swan_output.f90:77 `reflect_between_nautical_and_cartesian`).

### 6.2 SWAN→FLOW 보간 — `map_swan_output`

`packages/kernel/src/map_swan_output.f90:map_swan_output(sof,fof,gm,fg)` — `swan2flow_maps` 의 `ref_table/weight_table` 로 SWAN 출력장 전부를 FLOW 격자로 `grmap` (4점 가중평균, np=4) (map_swan_output.f90:56-76). 방향성분은 cosine/sine 성분(`dirc`,`dirs`)을 따로 보간한 뒤 `fxfydr` 로 합성각으로 복원한다 (map_swan_output.f90:60-61, 78) — 각도 평균을 벡터로 처리해 wrap-around 오류 방지.

### 6.3 물리 변환 — `wave2com`

`packages/kernel/src/wave2com.f90:wave2com(fof,sr)` 헤더 주석 (wave2com.f90:31): `Head routine for calling transform_swan_physics`. `transform_wave_physics_sp(...)` 호출로 SWAN 결과(hs, dir, period, dissip 1~3, fx, fy, mx, my)를 com-file 파라미터(hrms, tp, wsbodyu, wsbodyv 등)로 변환 (wave2com.f90:44-49). `gamma0` 범위 검증 (`[1,20]`, wave2com.f90:51-52). 그 전에 `wave2flow` (swan_tot.f90:506) 가 Cartesian 벡터를 FLOW 곡선격자 방향으로 되돌린다 (`flowgridfile == ' '` 인 Delft3D4 경로에서만).

### 6.4 com-file 기록 — `put_wave_fields`

`packages/io/src/put_wave_fields.f90:put_wave_fields(...)` 가 변환된 파동장을 FLOW com-file(또는 D-Flow FM NetCDF)에 기록 (swan_tot.f90:519-521). `swan_run%append_com` 에 따라 itidewrite(=-1 또는 itide)·comcount 인덱싱을 관리 (swan_tot.f90:517-535).

---

## 7. 모듈 간 의존 요약

```
wave_main / swan_tot (manager)
   ├─ get_flow_fields (io) ──> grmap / grmap_esmf (kernel) ── 가중치: swan_flow_grid_maps::make_grid_map (mkmap/ESMF)
   ├─ write_swan_file (io: write_swan_datafile) ── extrapolate
   ├─ write_swan_input → write_swan_inp (data: swan_input)  ── SWAN INPUT 생성 (CGRID/BOUN NEST/POINTS NGRID/COMPUTE/HOTSTART)
   ├─ run_swan (kernel) ── call swan(...) [LIB] | swan.sh [EXE] ── norm_end 확인
   ├─ read_swan_output (io) ── SWAN TABLE 파싱 → swan_output_fields
   ├─ map_swan_output (kernel) ── grmap (SWAN→FLOW, swan2flow_maps)
   ├─ wave2flow / wave2com (kernel) ── transform_wave_physics
   └─ put_wave_fields (io) ── com-file/NetCDF 기록
```

자료구조는 모두 `swan_flow_grid_maps` 모듈의 `grid`/`grid_map`/`input_fields`/`output_fields` 타입(swan_flow_grid_maps.f90:37-152)과 `wave_data` 모듈의 `wave_data_type`(시간·모드·출력 상태)을 공유한다.

---

## 8. 미확인 / 추가 분석 여지 (source-needed)

- `mkmap` (`packages/data/src/mkmap.f90`)의 4점 가중치 산정 세부 알고리즘(거리역수/bilinear 여부) — 본 노트 미열람, source-needed.
- `transform_wave_physics_sp` 본체(`m_transform_wave_physics`)의 hrms/tp/wsbody 변환식 — 미열람. 파-유 결합 항의 com 변환은 [[wave/delft3d_flow_wave_coupling]] 와 교차하므로 그쪽에서 다룸이 적절.
- `wave_mpi` 의 SWAN-MPI master/slave 통신(`run_swan_slave.f90`) 상세 — 미열람, source-needed.
- BOUN(WWIII·SHAPE 파라메트릭 스펙트럼) 입력 파서 세부 — 헤더/명령줄만 확인.
