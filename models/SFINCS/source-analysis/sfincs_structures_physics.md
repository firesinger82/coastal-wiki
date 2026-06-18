---
title: "SFINCS 물리·구조 모듈: structures·vegetation·crosssections·bathtub·initial_conditions·runup_gauges·obspoints"
model: SFINCS
component: structures-physics-io
canonical_source: self
citation_status: verified
verification_method: "7개 src 파일 전수 Read (sfincs_structures.f90 1-701, sfincs_vegetation.f90 1-374, sfincs_crosssections.f90 1-178, sfincs_bathtub.f90 1-216, sfincs_initial_conditions.F90 1-290, sfincs_runup_gauges.f90 1-188, sfincs_obspoints.f90 1-144). 보조 확인: sfincs_input.f90:493-496, sfincs_ncoutput.F90:1130/1709-1751, sfincs_data.f90:57/61/104/262/840."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[sfincs-architecture-source-map]]"
---

# SFINCS 물리·구조 모듈

Deltares SFINCS의 수공구조물·식생·단면·정적침수(bathtub)·초기조건·런업게이지·관측점 7개 모듈 분석. 모든 단언은 `상대경로:라인` 인용 (베이스: `models/SFINCS/raw/source_code/sfincs/source/src/`).

격자/quadtree 기반 자료구조(`uv_index_z_nm`, `z_flags_iref`, `find_uv_points_intersected_by_polyline` 등)는 [[sfincs-architecture-source-map]] 참조.

---

## 1. sfincs_structures.f90 — 수공구조물 + thin dams

### 1.1 구성과 타입 체계

`read_structures()`가 진입점 — 먼저 thin dam을 읽고(`kcs=0`) 그다음 weir를 읽음(`kcs=3`) (`sfincs_structures.f90:16-22`). 현재 입력으로 활성화되는 구조물 타입은 **weir(type=1, 파라미터 2개)** 뿐 (`sfincs_structures.f90:24-31`).

| type | 의미 | 파라미터 | 인용 |
|---|---|---|---|
| 1 | Weir | par1=마루고(ref datum 기준), par2=Cd | `:26-31` |
| 2 | (미구현 — `select case`에 빈 case) | — | `:683` |
| 3 | (미구현) | — | `:684` |

`structure_parameters(1,...)` 초기값 `-9999.0`(=height) (`:114`).

### 1.2 구조물 polyline → uv 점 매핑 (`read_structure_file`, :38-381)

1. polyline 개수 사전 카운트 후 rewind (`:121-132`).
2. 각 polyline에 대해 `find_uv_points_intersected_by_polyline`로 교차하는 uv 점 인덱스 추출 (`:159`).
3. **격자 간격 dxs 결정** — 좌표계(`crsgeo`)·방향(`idir`: 0=U,1=V)·정렬에 따라 분기 (`:181-199`). V점·지리좌표는 `1.0/dxminv(indx)` 사용 (`:188`).
4. **uv 점 좌표 산출** — refinement 레벨 비교(`irefnm>=irefnmu`)로 normal/fine-to-coarse 분기, `rotation`을 써서 셀 중심에서 uv 점으로 이동 (`:201-243`).
5. **구조물 길이 d** — uv 코너 두 점을 구조물 세그먼트에 투영: `distance_between_points_projected_on_line_segment(...)` (`:247`), `lngth(indx)`에 누적 (`:249`).
6. **마루고 보간** — 세그먼트 양 끝점까지 거리비 `wfac = dst1/(dst1+dst2)`로 선형보간 (`:251-255`), 같은 uv 점에 여러 polyline이 닿으면 `max`로 갱신 (`:257`). 나머지 파라미터(Cd 등)도 동일 가중 보간 (`:259-261`).

### 1.3 구조물 유효성 필터 (:275-306)

마루고가 셀 바닥보다 높아야 구조물로 인정:
- subgrid: `height > subgrid_uv_zmin(ip)` (`:286`)
- 비subgrid: `height > zbuvmx(ip)` (`:290`)

탈락 시 `istruc(ip)=0` (`:302`). 통과한 점은 `structure_length = lngth(ip)/dxs` (격자간격 대비 상대 길이로 변환, `:364`), `kcuv(ip)=3` 설정 (`:370`).

### 1.4 구조물 흐름 계산 (`compute_fluxes_over_structures`, :592-697)

> 헤더 주석 verbatim: `! Computes fluxes over structures (THIS HAS TO BE SERIOUSLY IMPROVED!!!)` (`:594`)

OpenACC GPU 병렬(`!$acc parallel ... loop independent gang vector`, `:625-626`). 구조물별로:

1. 먼저 `q(ip)=0, uv(ip)=0` 초기화 (`:631-632`).
2. 양쪽 수위가 모두 마루고 미만이면 무흐름 → `cycle` (`:640-644`).
3. **Broad-crested weir (type=1)** — 상수 `cweir = 1.7049` (`:651`), modular limit `m=0.0` (`:652`), `Cd=structure_parameters(2,...)` (`:653`). 상·하류 수두 결정 (`:659-667`):
   - 높은 쪽 수위에서 `h1`, 낮은 쪽에서 `h2`, 흐름방향 `idir = ±1`.
   - **완전 잠김** (`h2 > 2/3·h1`): $q = C_d \, h_2 \sqrt{\frac{2 \cdot 9.81 \,(h_1-h_2)}{1-m}}$ (`:669-673`)
   - **자유 흐름**: $q = C_d \, c_{weir}\, h_1^{1.5}$ (`:675-679`)
4. `qstruc = qstruc * structure_length` (격자상대 길이 곱), `q(ip) = qstruc*idir` (`:687-689`).

> 주석 verbatim: `q(ip)  = qstruc*idir ! Add relaxation here !!!` (`:689`) — 완화(relaxation) 미적용 상태.

### 1.5 Thin dams (`read_thin_dams`, :385-495)

`thdfile`의 polyline이 교차하는 uv 점에 대해 `kcuv(indx)=0` 설정 → 완전 차단(흐름 0) (`:459-461`). thin dam은 파라미터 없음(좌표만 읽음, `:450`). `nrthindams`에 점 개수 저장 (`:474`).

### 1.6 출력 보조

`give_structure_information`/`give_thindam_information`이 각 구조물 점의 face 중심좌표(`z_xz`/`z_yz` 평균)와 마루고를 `struc_info` 배열로 반환 (`:498-589`). face 좌표는 nm·nmu 평균 (`:536-537`, `:584-585`).

---

## 2. sfincs_vegetation.f90 — 식생 항력 파라미터

### 2.1 핵심: SFINCS 수력보다 SnapWave 파 소산용

식생은 `vegetation .or. snapwave_vegetation`일 때 `store_vegetation=.true.` (`sfincs_input.f90:493-496`). 4개 cell당 vertical-segment별 파라미터를 보관:

| 배열 | netcdf 변수명 | 의미 |
|---|---|---|
| `vegetation_stems_cd` | `snapwave_veg_Cd` | 항력계수 $C_d$ |
| `vegetation_stems_height` | `snapwave_veg_ah` | 줄기 높이 $a_h$ |
| `vegetation_stems_diameter` | `snapwave_veg_bstems` | 줄기 지름 $b$ |
| `vegetation_stems_density` | `snapwave_veg_Nstems` | 줄기 밀도 $N$ |

인용: 배열 선언 `sfincs_vegetation.f90:52-55`, netcdf 변수 매핑 `:62-72`. netcdf 변수명이 모두 `snapwave_veg_*` prefix인 점, 그리고 이 모듈 외부에서 식생 배열을 쓰는 곳이 ncoutput(저장만, `sfincs_ncoutput.F90:1709-1751`)뿐인 점에서 — **이 7개 모듈 내에는 SFINCS 운동량 방정식에 식생 항력을 가하는 코드가 없으며**, 식생은 주로 SnapWave 파 소산 입력으로 전달됨. (운동량 방정식 본체는 본 배정 범위 밖.)

### 2.2 두 입력 경로 (`initialize_vegetation`, :8-161)

식생 입력은 **quadtree mesh 전용** — 아니면 `stop_sfincs` (`:32-34`).

- **구(old) 경로** (`veggietype_toml=='none'`, `:41`): netcdf에 4개 파라미터 배열이 cell당 직접 저장. `nsec` 차원으로 vertical segment 수 결정, 64 초과 시 중단 (`:45-50`).
- **신(new) 경로** (`:74-157`): netcdf에는 cell당 정수 `vegetation_type`만 (CF flag conventions), 파라미터는 별도 TOML lookup 테이블에서. `read_netcdf_flag_meanings`로 `flag_values`/`flag_meanings` 읽고(`:87`), `read_vegetation_toml`로 lookup 채운 뒤(`:101-102`), flag 정수→lookup 행 직접 매핑(`type_to_lookup`)으로 per-cell 확장 (`:118-151`). type 0 = 무식생 (`:130`).

> 주석 verbatim: `! FIXME - parallellisation possible?` (`:126`)

### 2.3 TOML 파서 (`read_vegetation_toml`, :164-371)

`tomlf` 라이브러리 사용 (`:169`). `[vegetation_type]` 루트 테이블 필수 (`:229-233`). 타입별로 `vegetation_stems_cd/height/diameter/density` 4개 배열을 읽고 — **4개 배열 길이가 서로 일치해야 함**(불일치 시 중단, `:292-296` 등). 타입별 layer 수가 다르면 `max_layers`에 맞춰 0-padding (헤더 주석 `:166-167`). layer 한도 64 (`max_layers_limit`, `:182`). 유효 타입 0개면 중단 (`:355-357`).

---

## 3. sfincs_crosssections.f90 — 유량 단면

### 3.1 단면 polyline → uv 점 (`read_crs_file`, :8-127)

각 단면(crs) polyline이 교차하는 uv 점을 `crs_uv_index(nr,icrs)`에 저장 (`:97`). 단면당 최대 1000점 고정 할당 (`allocate(crs_uv_index(1000,ncrs))`, `:63`).

**부호 방향 `crs_idir` 결정** — uv 점 법선각 `phiuv = atan2(z_yz(nmu)-z_yz(nm), z_xz(nmu)-z_xz(nm))`와 단면 세그먼트 각 `phic`의 차 `dphi`로 결정 (`:104-114`): `dphi<=pi`면 `+1`, 아니면 `-1` (`:110-113`). 단면 이름은 polyline 헤더에서 (`:84`).

### 3.2 단면 적산유량 (`get_discharges_through_crosssections`, :130-176)

$$ Q_{crs} = \sum_{ip} q(\text{indx}) \cdot \text{crs\_idir}_{ip} \cdot \Delta_{xy} $$

여기서 $\Delta_{xy}$는 격자폭: U점은 `dyrm(iref)`, V점은 지리좌표면 `1.0/dxminv(indx)` 아니면 `dxrm(iref)` (`:153-169`). 누적 `:171`.

---

## 4. sfincs_bathtub.f90 — 정적(bathtub) 침수 모드

### 4.1 정체

경계 수위를 도메인 전체에 보간해 바닥보다 높으면 침수로 칠하는 **정적(reduced) 모드**. 동적 항(흐름·바람·강우·침투 등)을 명시적으로 모두 끔 (`:102-112`):
`meteo3d/wind/store_meteo/store_wind/store_wind_max/precip/patmos/snapwave/infiltration/store_velocity/store_maximum_velocity = .false.`

### 4.2 초기화 (`initialize_bathtub`, :16-114)

- **SnapWave 옵션** (`bathtub_snapwave`, `:34`): 파 경계조건(`read_snapwave_boundary_data`)을 읽어, bzs 시간별로 경계 수위에 `bathtub_fac_hs * (w1·h1 + w2·h2)` (보통 f=0.2) 더함 — 파 setup 근사 (`:59-82`, 주석 `:59`). `zs_bnd(ib,itb) += bathtub_fac_hs*(...)` (`:78`).
- 각 grid 점마다 경계 polyline에 대한 보간 인덱스/가중치를 `interp_segment`로 산출해 `bathtub_i1/i2/w1` 저장 (`:88-100`).

### 4.3 수위 계산 (`bathtub_compute_water_levels`, :117-174)

OpenMP 병렬(`!$omp ... schedule(dynamic,256)`, `:135-137`). grid 점별:

$$ z_{bt} = w_1 \, zst\_bnd(i_1) + w_2 \, zst\_bnd(i_2), \quad w_2 = 1 - w_1 $$

(`:145`). 그 뒤 **바닥 클리핑** (`:147-155`):
- subgrid: `zs(nm) = max(subgrid_z_zmin(nm), zbt)`
- 비subgrid: `zs(nm) = max(zb(nm), zbt)`

`store_maximum_waterlevel`이면 `zsmax` 갱신 (`:157-163`). 마지막에 `!$acc update device(zs, zsmax)`로 GPU 동기화 (`:169`).

> 주석 verbatim (왜 snapwave_data를 직접 못 쓰는지): `! We cannot use snapwave_data and snapwave_boundaries unfortunately, as these share common variable names.` (`:37`)

---

## 5. sfincs_initial_conditions.F90 — 초기조건

### 5.1 진입점 (`set_initial_conditions`, :14-179)

기본값: `inizs=zini`(수위), `iniq=0`(플럭스) (`:38-40`). **`q` 배열 크기 주의** — 주석 verbatim: `iniq(npuv+ncuv+1)) ! Note: q is actually larger than npuv! It has size npuv + ncuv + 1` (`:36`).

초기조건 소스 우선순위 (`:44-94`):
1. `rstfile` ≠ none → 바이너리 restart (`:44-54`)
2. `zsinifile` ≠ none → 확장자 `nc`면 netcdf real*8 (`:63-76`), 아니면 바이너리 real*4 (`:78-86`)
3. 둘 다 없으면 무처리 (`:90-94`)

### 5.2 수위·플럭스 초기화

수위는 바닥 클리핑 — subgrid면 `max(subgrid_z_zmin(nm), inizs(nm))`, 아니면 `max(zb(nm), inizs(nm))` (`:98-106`).

플럭스→유속 변환은 momentum과 동일 방식 (`:110-174`): uv 점 수위 `zsuv=max(zs(nm),zs(nmu))` (`:120`), 젖음 판정 후 subgrid면 havg 테이블 보간으로 `huv` 산출(완전 젖음이면 보간 생략, `:143-160`), `huv=max(huv,huthresh)` (`:162`). 유속은 `uv(ip)=max(min(q(ip)/huv,4.0),-4.0)` — **±4 m/s 클램프** (`:170`).

### 5.3 Restart 파일 형식 (`read_binary_restart_file`, :183-268)

stream-unformatted, 레코드마다 dummy로 감쌈. `rsttype` 1-6, 범위 밖이면 경고 후 skip (`:209-216`). 헤더 주석 verbatim (`:194-200`):

```
! 1: zs, q, uvmean
! 2: zs, q
! 3: zs  -
! 4: zs, q, uvmean and cnb infiltration (writing scs_Se)
! 5: zs, q, uvmean and gai infiltration (writing GA_sigma & GA_F)
! 6: zs, q, uvmean and hor infiltration (writing rain_T1)
```

`inizs4`는 항상 읽음 (`:221-222`). type 1/2/4/5/6은 `iniq`·`uvmean`도 읽음 (`:227-235`). type 4/5/6은 각각 침투 상태변수 `scs_Se`/`GA_sigma`+`GA_F`/`rain_T1` 추가 (`:237-259`). 끝에 real*4→real*8 remap (`:264`).

### 5.4 zsini 호환성

> 주석/로그 verbatim: `'Warning : binary ini files from SFINCS v2.1.1 and older are not compatible with SFINCS v2.1.2+, remake your inifile containing zs as real*8 double precision'` (`:279`). 바이너리 zsini는 여전히 real*4로 읽고 remap (`:282-286`).

---

## 6. sfincs_runup_gauges.f90 — 런업 게이지

### 6.1 읽기 (`read_rug_file`, :5-135)

각 게이지는 **시작점·끝점 2개 vertex만 허용** — `nrows>2`면 경고(초과분 무시, `:45-47`, `:98`). 게이지 라인을 `dxstep = 0.2*dxyr(nref)` 간격으로 샘플링(가장 미세 격자의 1/5, `:66`), 점 수 `int(rlen/dxstep)+1` (`:108`).

각 샘플점은 `find_quadtree_cell`로 quadtree cell 찾고(`:117`), `index_sfincs_in_quadtree`로 SFINCS 인덱스 변환해 `runup_gauge_nm(ip,irug)`에 저장 (`:119-125`). 도메인 밖이면 0 유지.

> 버그성 주목: 파일 존재 체크가 `rugfile`이 아닌 `obsfile`을 검사 — `ok = check_file_exists(obsfile, 'Run-up gauge rug file', .true.)` (`:35`). (open은 `rugfile`로 정상, `:39`.)

### 6.2 런업 수위 (`get_runup_levels`, :138-186)

초기값 `zru = -999.0` (`:151`). 게이지 라인을 따라가며 수심이 `runup_gauge_depth`보다 깊은 **가장 마지막(가장 육지쪽) 점의 수위**를 런업으로 채택:
- 바닥 `zbt` = subgrid면 `subgrid_z_zmin(nm)` 아니면 `zb(nm)` (`:159-167`)
- `zs(nm) > zbt + runup_gauge_depth`면 `zru(irug)=zs(nm)` (덮어쓰기, `:169-173`)

`else` 분기에 `!exit` 주석처리 — 얕은 점에서 멈추지 않고 계속 진행 (`:175-180`).

---

## 7. sfincs_obspoints.f90 — 관측점

### 7.1 읽기 (`read_obs_points`, :5-142)

`obsfile`의 각 행 = 관측점 1개. **이름 파싱** — `'...'` 또는 `"..."`로 감싼 이름 인식, 없으면 `station_NNN` 자동 부여 (`:67-82`). 좌표는 행의 첫 2값 (`:84-85`).

각 점에 대해 `find_quadtree_cell`(`:104`)→`index_sfincs_in_quadtree`(`:108`)로 SFINCS cell `nm` 결정. 저장: `nmindobs`(cell index), `nindobs`/`mindobs`(n,m), face 좌표 `xgobs/ygobs`, 바닥고 `zbobs`(subgrid면 `subgrid_z_zmin` 아니면 `zb`) (`:112-123`). 도메인 밖이면 경고 (`:131-135`).

로그 포맷에 nm/n/m/iref/z 출력 (`:128`).

---

## 부록: 공통 패턴

| 패턴 | 등장 | 의미 |
|---|---|---|
| `subgrid` 분기 | structures `:285`, bathtub `:147`, initial `:100`, runup `:159`, obs `:119` | subgrid 켜짐이면 `subgrid_*_zmin`, 아니면 `zb`/`zbuvmx` 사용 |
| polyline 2-pass 읽기 | structures `:121-132`, crs `:48-59`, thd `:423-434` | 개수 카운트→rewind→본 읽기 |
| `find_uv_points_intersected_by_polyline` | structures `:159`, thd `:453`, crs `:86` | polyline-격자 교차 uv 점 추출 (geometry 모듈) |
| quadtree cell 검색 | runup `:117`, obs `:104` | `find_quadtree_cell`+`index_sfincs_in_quadtree` |
| GPU/병렬 지시 | structures `!$acc :625`, bathtub `!$omp :135` / `!$acc :169` | structures는 ACC, bathtub은 OMP+ACC 동기화 |
