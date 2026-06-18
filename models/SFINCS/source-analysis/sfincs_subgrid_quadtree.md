---
title: "SFINCS 고속화 핵심 — subgrid look-up table · quadtree 적응격자 · domain 셋업"
model: SFINCS
component: "grid/subgrid/quadtree (sfincs_subgrid.F90 · sfincs_quadtree.F90 · sfincs_domain.f90)"
canonical_source: self
citation_status: verified
verification_method: "3개 소스 직접 Read (sfincs_subgrid.F90 1-983, sfincs_quadtree.F90 1-1075, sfincs_domain.f90 1-200·266-605·607-766·1400-1518·1588-1763). subgrid table 소비측은 sfincs_continuity.f90:549-568 / sfincs_momentum.f90:351-378 교차확인. 모든 단언 file:line."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[sfincs-architecture-source-map]]"
---

# SFINCS 고속화 핵심: subgrid + quadtree + domain

SFINCS의 reduced-complexity 모델이 "거친 계산격자 + 정밀 지형 정확도"를 동시에 달성하는 두 축:

1. **subgrid** — 각 계산셀/uv-점 안의 sub-grid 픽셀 지형을 사전 적분해 **look-up table**(volume↔level, depth↔level)로 저장. 런타임엔 1D 보간만.
2. **quadtree** — 인접 셀이 2배씩 거칠어/고와지는 **적응 격자** 자료구조. 정밀이 필요한 곳만 refine.

`sfincs_domain.f90`는 이 둘을 읽어 활성 셀(`np`)·uv-점(`npuv`) 인덱스로 re-map 하고 이웃·플래그 배열을 구성한다.

전체 모듈 맵은 [[sfincs-architecture-source-map]] §격자/지형 참조.

---

## 1. quadtree 자료구조 (`sfincs_quadtree.F90`)

### 1.1 핵심 전역 변수

모듈 헤더에 quadtree 전체(active+inactive 모든 점) 기술 배열이 선언된다 (`sfincs_quadtree.F90:8-48`):

| 변수 | 타입 | 의미 | line |
|---|---|---|---|
| `quadtree_nr_points` | int4 | 전체 점 수 | :8 |
| `quadtree_nr_levels` | int1 | refinement 레벨 수 | :9 |
| `quadtree_x0,y0,dx,dy` | real4 | 격자 원점·기본(level 1) 셀 크기 | :12-15 |
| `quadtree_nmax,mmax` | int4 | 최저레벨 격자 n·m 차원 | :16-17 |
| `quadtree_rotation,cosrot,sinrot` | real4 | 회전각 | :18-19 |
| `quadtree_level(:)` | int1 | 각 점 refinement 레벨 | :21 |
| `quadtree_{md,mu,nd,nu}(:)` | int1 | 4방향 이웃 **레벨차 플래그** (-1 coarser / 0 same / 1 finer) | :22-31 |
| `quadtree_{md1,md2,mu1,mu2,...}(:)` | int4 | 4방향 이웃 점 인덱스(1=첫째, 2=둘째 finer) | :23-33 |
| `quadtree_{n,m}(:)` | int4 | 점의 (n,m) 격자 좌표 | :34-35 |
| `quadtree_{xz,yz,zz}(:)` | real4 | 셀중심 x·y·지형고도 | :38-40 |
| `quadtree_nm_indices(:)` | int4 | 선형 nm 인덱스(binary search용) | :41 |
| `quadtree_{first,last}_point_per_level(:)` | int4 | 레벨별 점 범위 | :42-43 |
| `quadtree_dxr,dyr(:)` | real4 | 레벨별 셀 크기 | :44-45 |
| `quadtree_mask(:)` | int1 | 활성 마스크(kcs) | :46 |
| `quadtree_{snapwave,nonh}_mask(:)` | int1 | solver별 마스크 | :47-48 |

각 점은 한 방향당 최대 2개 이웃(`mu1`,`mu2`)을 가져 **coarse→fine 전이**를 표현한다.

### 1.2 파일 읽기 — netcdf / binary 2 포맷

`quadtree_read_file()` 디스패치 (`sfincs_quadtree.F90:64-207`):
- `.nc` 포함 시 netcdf, 아니면 binary (`:87-97`).
- netcdf는 차원 `mesh2d_nFaces`로 점 수 획득(`:314-320`), `n/m/level/md.../nu2/z/mask` 변수 읽기(`:324-392`). `x0/y0/dx/dy/rotation/nmax/mmax/nr_levels`는 **global attribute**(`:431-438`).
- binary는 "old" 포맷, 경고 출력 후 stream 읽기(`:225, 257-290`).

읽은 뒤 공통 후처리(`quadtree_read_file`, `:99-205`):
- rotation을 라디안 변환(`:99`).
- 레벨별 셀크기 `dxr(iref)=dx/2^(iref-1)` (`:111-112`) — **레벨마다 2배 세분**.
- 셀중심 좌표 회전변환(`:133-134`):
  $$x_z = x_0 + \cos\theta\,(m-0.5)\Delta x_{iref} - \sin\theta\,(n-0.5)\Delta y_{iref}$$
- **binary search용 선형 인덱스** `nm=(m-1)\cdot nmx+n` (단, `nmx=nmax\cdot2^{iref-1}`)와 레벨별 first/last 점 범위 구축(`:165-186`).

### 1.3 공간 검색 — binary search

- `find_quadtree_cell(x,y)` (`:764-820`): 좌표를 회전·정규화 후 **최고레벨부터 하향** 탐색, 각 레벨에서 `nm` 계산→`binary_search`로 그 레벨 점 범위 내 검색(`:799`), 레벨 일치 확인 후 확정(`:807-813`).
- `binary_search(x,n,val)` (`:1014-1059`) — 정렬된 `quadtree_nm_indices`에 표준 이분탐색.
- `find_cells_intersected_by_line` (`:671-760`), `find_uv_points_intersected_by_polyline` (`:853-1012`) — 관측선/구조물 폴리라인이 가로지르는 셀·uv-점 검색(thin dam/weir 등 입력에 사용). 후자는 셀 검색 후 4방향 uv(mu1/mu2/nu1/nu2)에 대해 `cross()`로 선분교차 판정(`:933-989`).

### 1.4 인덱스로부터 quadtree 생성 (regular grid 경로)

`make_quadtree_from_indices` (`:445-669`): "old" index-파일 입력일 때 단일 레벨(`quadtree_nr_levels=1`, `:592`) quadtree를 합성. nmax 기반으로 (n,m) 복원(`:517-518`), 4방향 이웃 인덱스를 `index_g_nm` 격자맵으로 채움(`:529-589`). `global` 분기는 동서 wrap-around 실험 코드(`:534-567`, 기본 `global=.false.` :474).

---

## 2. subgrid look-up table (`sfincs_subgrid.F90`)

### 2.1 테이블 자료구조 (sfincs_data 전역, 여기서 allocate)

`read_subgrid_file_netcdf`이 할당하는 배열 (`sfincs_subgrid.F90:136-148`):

**Z-점(셀) 테이블** — 셀별 부피곡선:
| 배열 | shape | 의미 |
|---|---|---|
| `subgrid_z_zmin(np)` | 셀 최저 지형고도 |
| `subgrid_z_zmax(np)` | 셀 최고 지형고도 |
| `subgrid_z_volmax(np)` | zmax까지의 저류부피 |
| `subgrid_z_dep(nlevels,np)` | 레벨별 수위(부피곡선 역함수용) |

**UV-점(셀 경계) 테이블** — 흐름면적/거칠기곡선:
| 배열 | shape | 의미 |
|---|---|---|
| `subgrid_uv_zmin/zmax(npuv)` | uv-점 지형 최저/최고 |
| `subgrid_uv_havg(nlevels,npuv)` | 수위별 grid-average 수심 |
| `subgrid_uv_nrep(nlevels,npuv)` | 수위별 representative Manning(읽으며 $g n^2$로 변환) |
| `subgrid_uv_pwet(nlevels,npuv)` | 수위별 wet fraction |
| `subgrid_uv_navg_w(npuv)` | weighted navg ($g\cdot n^2$ 저장) |
| `subgrid_uv_fnfit(npuv)` | zmax 위 외삽 fit 계수 |
| `subgrid_uv_havg_zmax/nrep_zmax(npuv)` | zmax에서의 값(고속 검색용) |

레벨 수 `subgrid_nlevels`는 netcdf `levels` 차원에서 획득(`:108`).

### 2.2 두 입력 포맷

`read_subgrid_file()`은 파일을 netcdf로 열어보고 성공 시 새 netcdf 포맷(`havg`/`nrep`), 실패(-51 = not-a-netcdf)면 "old" binary 포맷(`hrep`/`navg`)으로 분기 (`sfincs_subgrid.F90:32-52`, 경고 :48). netcdf 경로에선 `huthresh=0.0` 강제(`:40`).

### 2.3 quadtree → SFINCS 인덱스 re-map (핵심)

subgrid 파일은 **quadtree 전체 점**(kcs==0 포함)에 대한 값을 담고 있어 활성 셀 인덱스로 재매핑해야 한다 (주석 `:96-98`). netcdf 경로는 uv-점 재매핑 인덱스 `uv_index`를 quadtree 순회로 구축(`:166-272`): 각 점에서 mu(<1이면 1개, 아니면 mu1+mu2 둘) / nu 방향을 세며, 활성셀(`nm>0`)이고 그 방향 uv가 활성(`z_index_uv_mu1(nm)>0`)이면 `uv_index(npuvs)=npuvq`로 quadtree-uv순번을 기록(`:178-240`). regular grid 경로는 항등 매핑(`:244-270`).

읽은 raw 배열 `rtmpz/rtmpuv`를 이 인덱스로 끌어와 활성 배열에 채움(예 z_zmin `:276-280`, uv_havg `:332-338`). 거칠기는 읽으며 곧장 물리량으로 변환:
- `subgrid_uv_navg_w = g\cdot\max(navg,1e-4)^2` (`:329`)
- `subgrid_uv_nrep = g\cdot\max(nrep,1e-4)^2` (`:347`) — **$gn^2$ 사전계산**으로 런타임 절약.

### 2.4 일관성 보정(테이블 정합성)

- uv_zmin ≥ 양옆 셀 z_zmin 강제, 차이 >0.1m면 경고(HydroMT 버전 의심) (`:362-394`).
- z_zmax > z_zmin, uv_zmax > uv_zmin 보장(1cm 마진) (`:400-439`).
- "old" binary 포맷은 `index_quadtree_in_sfincs`로 재매핑(`:606`), `nrep`을 `g*max(...,0.005)^2`로 변환(`:658`), bottom 레벨을 한 레벨 위 값으로 복사(`:662`). regular subgrid는 별도 변수 순서(zmin/zmax/dhdz/hrep/navg)로 stream 읽기(`:677-868`).

### 2.5 테이블 소비 (런타임)

**셀 부피→수위 역보간** (`compute_initial_subgrid_volumes` `:907-962`, 본 모듈; 시간루프는 `sfincs_continuity.f90:549-568`):
- 셀이 완전 침수면 `z_volume = z_volmax + A\cdot(zs - zmax)` (`:929-931`).
- 아니면 레벨 검색 후 1D 보간(`:938-948`):
  $$\text{facint}=\frac{zs - z_{dep}(ivol)}{z_{dep}(ivol{+}1)-z_{dep}(ivol)},\quad z_{vol}=(ivol{-}1)dz_{vol}+\text{facint}\cdot dz_{vol}$$
- 역방향(continuity, `sfincs_continuity.f90:565-568`): `iuv=int(z_volume/dzvol)+1`로 부피→수위.

**uv-점 momentum** (`sfincs_momentum.f90:373-378`): 수위 `zsu`로 레벨 인덱스/보간계수 계산 후 `havg`(흐름수심)·`nrep`($gn^2$)·`pwet`(wet fraction)을 1D 보간. `zsu>zmax`면 `fnfit` 기반 외삽(`sfincs_momentum.f90:351-364`). 이것이 거친 셀에서도 sub-grid 지형 효과를 보존하는 메커니즘.

---

## 3. domain 셋업 (`sfincs_domain.f90`)

### 3.1 초기화 순서

`initialize_domain()` (`:8-56`): processes → mesh → bathymetry → boundaries → roughness → infiltration → storage → vegetation → hydro 순. 단일 레벨이면 `use_quadtree=.false.`로 되돌려 regular-grid 출력(`:42-50`). 끝에 `set_advection_mask`·`fill_h73_tables`(`:52-54`).

`initialize_processes()` (`:59-140`): 입력 파일명으로 물리과정 on/off 플래그 설정. `qtrfile/=none`이면 `use_quadtree=.true.`(`:71-73`).

### 3.2 mesh 구성 — quadtree → 활성 셀 re-map

`initialize_mesh()` (`:143-1586`)이 핵심. 흐름:

1. quadtree 읽기(`:197`) 또는 old index 파일(`:200-`). quadtree 전역값을 domain 전역(`x0,nmax,dx,nref=quadtree_nr_levels`)으로 복사(`:266-277`).
2. **마스크 적용·활성 셀 추출**: `msk`(=quadtree_mask)에서 `msk>0`인 점만 카운트해 `np` 결정(`:331-337`).
3. **양방향 인덱스 매핑** (`:425-435`):
   - `index_sfincs_in_quadtree(quadtree점) = SFINCS순번`
   - `index_quadtree_in_sfincs(SFINCS순번) = quadtree점`
   이 두 배열이 subgrid 재매핑(§2.3)·지형 복사 등 전반에 사용된다.
4. quadtree 이웃 플래그/인덱스를 활성 인덱스로 복사 (`z_flags_iref`←level, `z_flags_nu/mu/...`, `z_index_z_nu1/...`은 이웃을 `index_sfincs_in_quadtree`로 변환) (`:439-482`).

### 3.3 uv-점 생성 + refinement 전이 점

5. **uv-점 카운트** (`:489-533`): 셀마다 오른쪽(mu)·위쪽(nu)을 검사. same/coarse(`flag<1`)면 1개, finer(`flag==1`)면 mu1·mu2 2개 → `npu+npv=npuv`.
6. **combined uv 점 (ncuv)** (`:537-596`): refinement 전이(`z_flags_*==1`, finer side)마다 1개 추가. `npuvtotal=npuv+ncuv`. 거친-고운 경계에서 2개의 fine-uv를 1개 coarse-uv 흐름으로 묶기 위한 가상 점(주석 `:539`, 로그 "number of quadtree refinement transitions" `:593`).
7. **uv 플래그 설정** (`:680-996`): `uv_index_z_nm/nmu`(좌/우 셀), `z_index_uv_mu1/...`(셀→uv 역인덱스), 그리고 점별 플래그:
   - `uv_flags_iref` — uv-점 레벨(finer 측이면 `z_flags_iref(nm)+1`, 예 :830)
   - `uv_flags_dir` — 0=u(가로), 1=v(세로) (`:751, 936`)
   - `uv_flags_type` — `0` 동일레벨 / `-1` fine→coarse / `1` coarse→fine (주석 `:752`)
   `uv_flags_type`은 bathymetry에서 비대칭 가중(`zbuv`)에 쓰임(§3.5).
8. **8-이웃 uv 인덱스** (`:1005-`): advection/coriolis/viscosity 등 켜진 경우만 할당(`:699-719`), refinement 경계의 fine/coarse 이웃을 분기 처리(`:1028-1092`).

### 3.4 셀 크기·면적 (geographic vs projected)

`crsgeo`(지리좌표) 분기 (`:1403-1518`):
- **geographic**(`:1403-1473`): dx는 위도 의존 → uv-점별 `dxminv=1/(dxr\cdot111111.1\cdot\cos(lat))` (`:1429`), 셀면적 `cell_area_m2(nm)=dxm\cdot dyrm` (`:1463`). 공간변화 Coriolis `f=2\Omega\sin(lat)` (`:1471`).
- **projected**(`:1475-1518`): 레벨별 상수 `cell_area(iref)=dxrm\cdot dyrm` (`:1504`). coarse 이웃용 `dxrinvc=1/(1.5\,dxrm)` (`:1508`).
둘 다 `dxymin`(최소격자, dtmax CFL 결정용)을 추적(`:1434,1515`).

### 3.5 bathymetry

`initialize_bathymetry()` (`:1588-1744`):
- **subgrid 켜짐 시**: `read_subgrid_file()` 호출(`:1716`)로 §2 테이블 적재. nonh solver면 `zb`도 quadtree_zz에서 추가 로드(`:1720-1738`).
- **subgrid 꺼짐 시**(`:1608-1710`): `zb`(셀) 읽고 uv-점 수심 `zbuv`를 `uv_flags_type`별 가중평균:
  - type 0: `0.5 zb(nm)+0.5 zb(nmu)` (`:1692`)
  - type -1(fine→coarse): `0.3333/0.6667` (`:1698`)
  - type 1(coarse→fine): `0.6667/0.3333` (`:1704`)
  - `zbuvmx=max(zb,zbu)+huthresh` (`:1708`, 별도 `compute_zbuvmx` `:1746-1763`).

---

## 4. 설계 요점 (왜 빠른가)

| 메커니즘 | 효과 | 근거 |
|---|---|---|
| subgrid 부피/수심 곡선을 사전적분 | 거친 셀에서도 정밀지형 정확도, 런타임은 1D 보간만 | `sfincs_continuity.f90:565-568`, `sfincs_momentum.f90:373-378` |
| `nrep`을 읽으며 $gn^2$로 변환 | 시간루프 내 제곱·곱셈 제거 | `sfincs_subgrid.F90:347` |
| `*_zmax` 사전계산 배열 | zmax 초과 영역 고속 분기 | `sfincs_subgrid.F90:443-446` |
| quadtree 레벨별 binary search | 점 검색 O(log n) | `sfincs_quadtree.F90:799` |
| 양방향 index_*_in_* 매핑 | 비활성 점 제거 + 캐시친화 선형 배열 | `sfincs_domain.f90:425-435` |
| combined uv 점 | refinement 경계 흐름 보존 | `sfincs_domain.f90:537-596` |

연결: 시간루프 전체는 [[sfincs-architecture-source-map]] 참조 (momentum→continuity).
