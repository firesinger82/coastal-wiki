---
title: SFINCS 외력 — 경계·방류·기상·spiderweb·침투
model: SFINCS
component: boundaries / forcing (water-level & flux boundaries, discharges, meteo, spiderweb cyclone, infiltration)
canonical_source: self
citation_status: verified
verification_method: >
  source/src/ 5개 파일 직접 Read 후 file:line 인용.
  sfincs_boundaries.f90 (1254 lines), sfincs_discharges.f90 (662),
  sfincs_meteo.f90 (1613), sfincs_spiderweb.f90 (486), sfincs_infiltration.f90 (1039).
  모든 식·자료구조·분기 인용 전 해당 라인 verbatim 확인.
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[sfincs-architecture-source-map]]"
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

# SFINCS 외력 (Boundaries & Forcing)

SFINCS reduced-complexity 복합침수 모델의 **외력 5종**을 한 노트로 종합한다. compound flooding 의 동인(tide+surge 경계, 하천 방류, 강우, 태풍 바람/기압, 토양 침투손실)이 모두 여기 모인다. 전역 데이터·드라이버 흐름은 [[sfincs-architecture-source-map]] 참조.

| 외력 | 모듈 파일 | 핵심 서브루틴 | 입력 키워드(파일) |
|---|---|---|---|
| 수위/flux 경계 | `sfincs_boundaries.f90` | `read_boundary_data` / `update_boundaries` | `bnd/bzs/bzi/bca/bdr` |
| 방류·배수구조물 | `sfincs_discharges.f90` | `read_discharges` / `update_discharges` | `src/dis/drn` |
| 기상(바람·기압·강우) | `sfincs_meteo.f90` | `read_meteo_data` / `update_meteo_*` | `amu/amv/amp/ampr/wnd/prcp` |
| 태풍 parametric (spiderweb) | `sfincs_spiderweb.f90` | `read_spw_*` | `spw/netspw` |
| 침투(강우손실) | `sfincs_infiltration.f90` | `initialize_infiltration` / `update_infiltration_map` | `qinf/scs/seff/psi/fc/...` |

---

## 1. 수위·flux 경계 (`sfincs_boundaries.f90`)

### 1.1 입력 파일 종류
`read_boundary_data` (`sfincs_boundaries.f90:8`) 는 우선순위 분기로 경계 입력을 읽는다:

- **NetCDF (FEWS)** `netbndbzsbzifile`: `read_netcdf_boundary_data` 호출 (`:43-47`).
- **ASCII** `bndfile`(위치) + `bzsfile`(수위 시계열) (`:56-98`). `bnd` 라인 수 = `nbnd`, `bzs` 라인 수 = `ntbnd`; `t_bnd(ntbnd)`, `zs_bnd(nbnd,ntbnd)` 할당 (`:90-96`).
- `bzifile`: incoming **infragravity wave** 시계열 `zsi_bnd` (`:126-141`).
- bnd 만 있고 bzs 없으면 수위 0.0 (단, `bcafile`도 없으면 경고) (`:100-124`).
- mask 에 open boundary 있는데 bnd 파일 없으면 1점 추가·수위 0.0 (`:166-189`).

시계열이 시뮬레이션 구간을 못 덮으면 경고 후 첫/끝 시각을 `t0-1.0` / `t1+1.0` 으로 강제 보정 (`:143-164`).

### 1.2 하류 하천 경계 (downstream river, kcs=5)
`bdrfile` 읽어 `x_bdr,y_bdr` 와 내부점 `index_zsi_bdr`, 수위차 `dzs_bdr` 산정 (`:217-268`). 경사 기반 수위강하:

$$\Delta z_{s,bdr} = -\,\text{slope} \times \text{distance}$$

distance 미제공(<0)이면 두 점 사이 거리 사용 (`:252-264`):

```fortran
dzs_bdr(ibdr) = - slope_bdr * sqrt( (x_bdr_in - x_bdr(ibdr))**2 + (y_bdr_in - y_bdr(ibdr))**2 )
```

### 1.3 천문조 (`bca` 파일, astro)
`bcafile` + `use_bcafile` 시 조석 성분 읽기 (`:293`). `[forcing]` 블록 단위(=bnd 점당), 성분당 `(name, amplitude, phase)`. 2-pass 파싱: 1차로 set/성분 수 카운트(`:311-358`), `A0` 없으면 1개 추가(`:370-376`), 2차로 `tidal_component_data(2, ic, nbnd)` 채움(`:396-439`). set 수 ≠ nbnd 면 ERROR 출력(`:362-366`). `update_nodal_factors` 로 nodal factor·주파수 산정 후 `rad/s` 변환(`:446-448`).

천문조 입력은 `bcafile`이 있고 `use_bcafile`가 참이며 `nbnd>0`일 때 실행한다. `sfincs_boundaries.f90:293` `if (bcafile(1:4) /= 'none' .and. nbnd > 0 .and. use_bcafile) then`


### 1.4 시간보간 + 조석 합성 (`update_boundary_points`, `:682`)
`itbndlast` 캐시로 시간 구간 탐색(`:714-722`), 선형보간 계수 `tbfac`(`:726`). 천문조 합성식(`:736-744`):

$$z_{s,tb} = z_{s,bnd}(\text{interp}) + \sum_{ic} A_{ic}\cos(\omega_{ic}\, t - \phi_{ic})$$

```fortran
zstb = zstb + tidal_component_data(1, ic, ib) * cos(tidal_component_frequency(ic) * t - tidal_component_data(2, ic, ib))
```

### 1.5 그리드 경계점 매핑 (`find_boundary_indices`, `:455`)
각 grid boundary point(`ngbnd`)에 대해 kcs 별 처리:

| kcs | 의미 | 처리 (`:537-675`) |
|---|---|---|
| 2 | 수위 경계 | 최근접 2점 거리가중 `fac = dst2/(dst1+dst2)` (`:577`) |
| 5 | 하류 하천 outflow | bdr 최근접 1점 (`:587-613`) |
| 6 | 측면(Neumann) 경계 | 4방향 이웃 중 kcs=1 내부점 탐색→`nmi_gbp`; 없으면 셀 비활성화 (`:615-672`) |

kcs 의미 주석은 `:793-798` 에 정리:
```fortran
! kcs = 1 : regular point
! kcs = 2 : water level boundary point
! kcs = 3 : outflow boundary point
! kcs = 4 : wave maker point
! kcs = 5 : river outflow point (dzs/dx = i)
! kcs = 6 : lateral (coastal) boundary point (Neumann dzs/dx = 0.0)
```

#### 문서와 코드 차이 (외부 원문 판정)

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| <a id="cv-s-b050"></a>B050 | Neumann 경계(msk=6) 버그 | Deltares/SFINCS, `v2.3.0_mt_Faber_release`, [`source/src/sfincs_boundaries.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.3.0_mt_Faber_release/source/src/sfincs_boundaries.f90), `sfincs_boundaries.f90:633, 638, 643, 648`<br>Deltares/SFINCS, `v2.4.0_Galibier_release`, [`source/src/sfincs_boundaries.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.4.0_Galibier_release/source/src/sfincs_boundaries.f90), `sfincs_boundaries.f90:661–668`<br>[Deltares/SFINCS 커밋 `6dea570`](https://github.com/Deltares/SFINCS/commit/6dea570) (2026-04-03)<br>`docs/developments.rst:66`의 `specific cases`를 `sfincs_boundaries.f90:661–668`의 `if (nmi_gbp(ib) == 0) then` 분기에 대조했다. | A 판 차이. v2.4.0은 Neumann 경계 셀(msk=6)에 활성 이웃(msk=1)이 하나도 없으면 그 셀을 비활성(`kcs = 0`)으로 되돌린다. 같은 분기는 경고를 쓴다. v2.3.0에는 이 분기가 없다. [대조 보고서 §5 B050](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1028) [10-12 외부 원문 판정] [10-12 결론 검증 보완] |

### 1.6 경계 수위 갱신 (`update_boundary_conditions`, `:761`)
kcs=2: 거리가중 수위 `zst`(`:810`) + **기압보정**(`patmos .and. pavbnd>1.0`, `:820-826`):

$$z_s \mathrel{+}= (p_{av,bnd} - p_{atm,b})/(\rho_w \cdot 9.81)$$

경계 수위의 spin-up은 `if (t < (tspinup - 1.0e-3)) then`에서 실행한다(`sfincs_boundaries.f90:851` `if (t < (tspinup - 1.0e-3)) then`). [10-12 전수 검증 보완] `sfincs_boundaries.f90:851` `if (t < (tspinup - 1.0e-3)) then`; `sfincs_boundaries.f90:856,860` 입력 tspinup은 기간이다. 내부 tspinup은 `sfincs_input.f90:369`의 `tspinup = t0 + tspinup`으로 종료 시각이 된다. `:365–366`의 t0는 tref부터 tstart까지의 초이다. `sfincs_boundaries.f90:853`은 `smfac = 1.0 - (t - t0) / (tspinup - t0)`를 쓴다. 시간 원점 차이는 이 변환으로 반박되므로 별도 결함으로 분류하지 않는다. [10-12 결론 검증 보완]
이 분기는 초기 수위와 현재 경계 수위를 가중평균한다. `sfincs_boundaries.f90:851` `if (t < (tspinup - 1.0e-3)) then`; `sfincs_boundaries.f90:856,860`

### 1.7 경계 flux (`update_boundary_fluxes`, `:924`) — **weakly reflective**
`bndtype==1`(기본, `:968`). subgrid lookup 으로 경계 uv 점 수심 `hnmb`(`:976-997`). 약반사 Riemann 류 유속(`:1019-1022`):

$$u_i = \sqrt{g/h}\,(z_{s,b}-z_{s0,b}), \quad u_b = \text{dir}\,(2u_i - \sqrt{g/h}\,(z_{s,i}-z_{s0,b})), \quad q = u_b h + \overline{uv}$$

```fortran
ui = sqrt(g / hnmb) * (zsnmb - zs0nmb)
ub = ibuvdir(ib) * (2 * ui - sqrt(g / hnmb) * (zsnmi - zs0nmb))
q(ip) = ub * hnmb + uvmean(ib)
```

inflow/outflow 부호 제한(빈 셀/얕은 경계, `:1034-1073`), 유속 ±4 m/s clamp(`:1077`). `uvmean` 은 `btfilter`/`btrelax` 로 relaxation — "persistent jets" 억제, 기본 `btrelax=3600s`(`:1081-1093`). 코드 주석에 미사용 대안 Riemann 식도 기록(`:1024-1032`).

`update_boundaries`는 `boundaries_in_mask`가 참이면 경계 작업을 선택한다. `sfincs_boundaries.f90:1145` `if (boundaries_in_mask) then`; `sfincs_boundaries.f90:1147` `if (nbnd > 0) then`; `sfincs_boundaries.f90:1151` `call update_boundary_points(t)`; `sfincs_boundaries.f90:1158` `if (.not. bathtub) then`; `sfincs_boundaries.f90:1162` `call update_boundary_conditions(t, dt)`; `sfincs_boundaries.f90:1166` `call update_boundary_fluxes(dt, t)`
경계점 갱신은 `nbnd>0`을 추가로 요구한다. `sfincs_boundaries.f90:1145` `if (boundaries_in_mask) then`; `sfincs_boundaries.f90:1147` `if (nbnd > 0) then`; `sfincs_boundaries.f90:1151` `call update_boundary_points(t)`; `sfincs_boundaries.f90:1158` `if (.not. bathtub) then`; `sfincs_boundaries.f90:1162` `call update_boundary_conditions(t, dt)`; `sfincs_boundaries.f90:1166` `call update_boundary_fluxes(dt, t)`
격자 수위·유량 갱신은 `bathtub=false`에서 순서대로 실행한다. `sfincs_boundaries.f90:1145` `if (boundaries_in_mask) then`; `sfincs_boundaries.f90:1147` `if (nbnd > 0) then`; `sfincs_boundaries.f90:1151` `call update_boundary_points(t)`; `sfincs_boundaries.f90:1158` `if (.not. bathtub) then`; `sfincs_boundaries.f90:1162` `call update_boundary_conditions(t, dt)`; `sfincs_boundaries.f90:1166` `call update_boundary_fluxes(dt, t)`

---

## 2. 방류·배수구조물 (`sfincs_discharges.f90`)

### 2.1 입력 (`read_discharges`, `:8`)
- `srcfile`(점위치)+`disfile`(시계열) ASCII (`:36-128`), 또는 NetCDF `netsrcdisfile`(`:55-66`).
- `nsrcdrn = nsrc + 2*ndrn` (`:86`) — drainage 는 sink/source 한 쌍이므로 ×2.
- 소스점 quadtree 셀 매핑 `nmindsrc`(`:159-171`).

### 2.2 배수 구조물 타입 (`drnfile`)
`drainage_type` 정수가 5번째 항목(`:209`). 파라미터 수(`:213-225`):

| type | 구조물 | npars | 비고 |
|---|---|---|---|
| 1 | Pump | 1 | 고정 유량 |
| 2 | Culvert | 1 | 양방향 |
| 3 | Check valve | 1 | 단방향(culvert+`max(qq,0)`) |
| 4 | Controlled gate | 6 | width·sill·manning·zmin·zmax·closing time |
| 5 | Controlled gate (시간제어) | 6 | width·sill·manning·tclose·topen·closing time |

`drainage_params(ndrn,6)`, `drainage_status`(0=closed/1=open/2=closing/3=opening, `:201`), `drainage_fraction_open`(`:200`). 두 점 거리 `drainage_distance`(`:298`).

### 2.3 유량 계산 (`update_discharges`, `:325`)
**점소스**: 시계열 선형보간 `qtsrc`(`:354-365`).

**구조물별** (`select case`, `:384-620`):
- Pump(1): `qq = params(1)` (`:390`).
- Culvert(2)/Check valve(3): $qq = c\sqrt{|z_{s,in}-z_{s,out}|}$ 부호반영 (`:396-418`); check valve 는 `max(qq,0)`(`:422`).
- Gate(4): 수위 zmin~zmax 시 개방, 시간상수 `tcls` 로 `frac` 증감(`:444-514`). **Bates et al.(2010)** 관성포함 식(`:516-518`):

$$qq = \frac{qq_0 - g\,h_{gate}\,(\partial z_s/\partial s)\,\Delta t}{1 + g\,n^2\,\Delta t\,|qq_0| / h_{gate}^{7/3}}$$

```fortran
qq = (qq0 - g * hgate * dzds * dt) / (1.0 + g * mng**2 * dt * abs(qq0) / hgate**(7.0 / 3.0))
qq = qq * wdt * frac
```
- Gate(5): 동일식이나 개폐 트리거가 사용자 지정 시각 `topen/tclose`(`:548-563`).

Darcy–Weisbach 도입 계획: 근거: `docs/input_structures.rst:222` `Future updates will incorporate the Darcy–Weisbach equation for more accurate discharge estimates by considering frictional and minor losses along the culvert length, which is particularly useful for longer or rougher conduits.`<br>`docs/input_structures.rst:207` ``` ``par1 = \(\mu \cdot A \cdot \sqrt{2g}\)`` ```<br>`sfincs_discharges.f90:398` `qq  = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`<br>`sfincs_discharges.f90:402` `qq  = -drainage_params(idrn, 1) * sqrt(zs(nmout) - zs(nmin))` [대조 보고서 §5 B135](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1054) 결론: 문서에만 있음. 이 판의 암거 계산은 Darcy–Weisbach 관로식 대신 par1과 수두차 제곱근을 사용한다. raw 전체에서 Darcy·Weisbach를 대소문자 무시 검색했다. docs/input_structures.rst:222의 미래 계획만 찾았다. 보조 프로그램에서도 대응 구현은 찾지 못했다. [raw 전체 검색 기록](../../../_staging/recovery/flow/conclusions-verify-cv-s.md#d-search). [10-12 결론 검증 보완]


공통 후처리: `structure_relax`(기본 10s) relaxation(`:625`), 셀 가용 volume 으로 유량 제한(subgrid: `z_volume`, regular: `(zs-zb)*cell_area`)(`:629-645`), `qtsrc(jin)=-qq`, `qtsrc(jout)=qq`(`:647-648`).

배수 구조물은 현재 연속식 이전의 수위·부피로 유량을 정한다. `sfincs_discharges.f90:398` `qq  = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`; `sfincs_discharges.f90:632` `qq = min(qq, max(z_volume(nmin), 0.0) / dt)`; `sfincs_discharges.f90:647` `qtsrc(jin)  = -qq`; `sfincs_continuity.f90:100` `zs(nmindsrc(isrc)) = max(zs(nm) + qtsrc(isrc) * dt / cell_area(z_flags_iref(nm)), zb(nm))`; `sfincs_continuity.f90:319` `z_volume(nm) = z_volume(nm) + qtsrc(isrc) * dt`
연속식은 같은 단계에서 새 `qtsrc`를 적용한다. `sfincs_discharges.f90:398` `qq  = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`; `sfincs_discharges.f90:632` `qq = min(qq, max(z_volume(nmin), 0.0) / dt)`; `sfincs_discharges.f90:647` `qtsrc(jin)  = -qq`; `sfincs_continuity.f90:100` `zs(nmindsrc(isrc)) = max(zs(nm) + qtsrc(isrc) * dt / cell_area(z_flags_iref(nm)), zb(nm))`; `sfincs_continuity.f90:319` `z_volume(nm) = z_volume(nm) + qtsrc(isrc) * dt` subgrid 점 유량 대입은 `if (nsrcdrn > 0) then` 안에서 `if ((z_volume(nm) >= 0) .or. ((qtsrc(isrc)<0.0) .and. (z_volume(nm) >= 0))) then`을 통과할 때 수행한다(`sfincs_continuity.f90:311` `if (nsrcdrn > 0) then`; `sfincs_continuity.f90:318` `if ((z_volume(nm) >= 0) .or. ((qtsrc(isrc)<0.0) .and. (z_volume(nm) >= 0))) then`; `sfincs_continuity.f90:319` `z_volume(nm) = z_volume(nm) + qtsrc(isrc) * dt`). [10-12 전수 검증 보완]


---

## 3. 기상 강제 (`sfincs_meteo.f90`)

### 3.1 입력 종류 (`read_meteo_data`, `:5`)
플래그 `spw_wind/am_wind/am_pres/am_prcp/tm_wind/tm_prcp`(`:23-33`):

| 입력 | ASCII | NetCDF(FEWS) | 자료 |
|---|---|---|---|
| spiderweb | `spwfile` (`:35`) | `netspwfile` (`:101`) | 태풍 극좌표 wind/pres/precip |
| 격자 바람 | `amufile/amvfile` (`:133`) | `netamuamvfile` (`:155`) | wu/wv |
| 격자 기압 | `ampfile` (`:202`) | `netampfile` (`:220`) | patm |
| 격자 강우 | `amprfile` (`:170`) | `netamprfile` (`:188`) | precip |
| 시계열 바람 | `wndfile` (`:234`) | — | mag/dir |
| 시계열 강우 | `prcpfile` (`:269`) | — | mm/hr |

`wndfile` 풍향은 cartesian + 격자회전 변환(`:262`): `wnddir = pi*(270-dir)/180 - rotation`.

### 3.2 항력계수 Cd & enhancement
풍속별 Cd 테이블 보간(`cdval(iw)`, 0.1 m/s bin, `:303-315`). 보정계수 `factor_wind`/`factor_pres`/`factor_prcp`/`factor_spw_size`(기본 1.0) 일괄 적용(`:319-402`). 기압보정식(`:353`): `spw_pabs = gapres - factor_pres*(gapres - spw_pabs)`.

### 3.3 spiderweb 보간 (`update_spiderweb_data`, `:437`)
두 시점(`meteo_t0/t1`) 각각(`:466`):
- spw 시간범위 밖이면 첫/끝 시점 사용 + **6시간(21600s) ramp** spin-up factor(`:476-494`).
- 극좌표 bilinear: 반경 bin `idstspw`, 각도 bin `iphispw`(`:624-655`); 첫 bin 음수 `dj1` clamp 주석(`:632-635`).
- wind→stress(`:744-745`): $\tau = \text{vmag}\cdot(\cos\!/\!\sin\,\text{rot})\cdot w \cdot \rho_a C_d/\rho_w$.
- **wave-age Cd** (`waveage>0`, LGX 테이블 `cdlgx`, `:683-697`).
- **wind reduction over land** (Westerink et al. 2008, `:709-740`): marine vs land 거칠기 `z0` 비교, `z0land` 방향별 테이블 + `z0land_table` lookup 으로 vmag/wup/wvp 감쇠.
- spw 가장자리 background 병합 `merge_frac`(`:701-707`), `tspinup_fac` 곱.
- precip 단위 `prp/(1000*3600)` → m/s(`:752`).

bin u/v 분해(`:77-78`): `spw_wu = vmag*cos(pi*(270-vdir)/180)`.

#### 문서와 코드 차이 (외부 원문 판정)

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| <a id="cv-s-b068"></a>B068 | `spwmergefrac` 병합 버그 | Deltares/SFINCS, `v2.2.0_col_dEze_release`, [`source/src/sfincs_meteo.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.2.0_col_dEze_release/source/src/sfincs_meteo.f90), `sfincs_meteo.f90:510–511`<br>Deltares/SFINCS, `v2.3.0_mt_Faber_release`, [`source/src/sfincs_meteo.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.3.0_mt_Faber_release/source/src/sfincs_meteo.f90), `sfincs_meteo.f90:668–669`<br>Deltares/SFINCS, `v2.2.0_col_dEze_release`, [`source/src/sfincs_input.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.2.0_col_dEze_release/source/src/sfincs_input.f90), `sfincs_input.f90:104`<br>Deltares/SFINCS, `v2.3.0_mt_Faber_release`, [`source/src/sfincs_input.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.3.0_mt_Faber_release/source/src/sfincs_input.f90), `sfincs_input.f90:108`<br>[Deltares/SFINCS 커밋 `0c7d4f7`](https://github.com/Deltares/SFINCS/commit/0c7d4f7) (2025-06-23)<br>`docs/developments.rst:123`의 수정 이력을 이전·이후 병합식에 대조했다. 로컬 `sfincs_meteo.f90:701–702`는 v2.3.0의 식과 같다. | A 판 차이. v2.3.0은 spiderweb 병합 비율의 기울기 계수를 상수 2에서 `1/(1 - min(spw_merge_frac, 0.999))`로 바꾸었다. 기본값 0.5에서는 두 판의 계수가 2로 같다. 기본값이 아닌 값에서만 두 판이 다르다. [대조 보고서 §5 B068](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1033) [10-12 외부 원문 판정] [10-12 결론 검증 보완] |

### 3.4 격자 데이터 보간 (`update_amuv_data` `:789` / `update_amp_data` `:967` / `update_ampr_data` `:1097`)
직교격자 bilinear. amu/amv: `radstr` 시 바람을 radiation stress 로 취급(임시 wave forcing, `:929-939`). 격자 밖이면 wind=0 / patm=gapres / prcp=0(`:873-887`,`:1049-1064`,`:1186-1201`). ampr 는 `ampr_block` 기본 true 시 block(계단)보간(`twfac=0`, `:1142-1148`). 근거: `docs/parameters.rst:174` `ampr_block`<br>`docs/input_forcing.rst:224` `**NOTE - ampr_block - keyword controlling whether the input precipitation rate is kept constant for the duration of the input time interval (block interpolation, ampr_block = 1, default), or whether it is interpolated linearly in time (ampr_block = 0).**`<br>`sfincs_input.f90:106` `call read_int_input(500,'amprblock',iamprblock,1)`<br>`sfincs_input.f90:537` `ampr_block = .true. ! Default use data in ampr file as block rather than linear interpolation`<br>`sfincs_input.f90:538` `if (iamprblock==0) then`<br>`sfincs_input.f90:539` `ampr_block = .false.`<br>`sfincs_read.f90:28` `if (trim(keystr)==trim(keyword)) then` [대조 보고서 §5 A029·K066·C003](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:947) 결론: 문서 오기. 이 판의 강수 시간 보간 입력 이름은 amprblock이다.

### 3.5 매 timestep 적용 (`update_meteo_forcing`, `:1233`)
`meteo3d` 시 t0/t1 시간보간(`:1259`). wind→`tauwu/tauwv`, patm, precip→`prcp`(m/s) 보간(`:1273-1327`). 음수 prcp(effective rainfall) 는 물 없는 셀에서 0 처리(`:1303-1315`). meteo spin-up(`spinup_meteo`, `:1336-1385`): 바람·patm·netprcp 를 `(t-t0)/(tspinup-t0)` 로 ramp, patm 은 gapres 로 보간. 경계점 기압 `patmb`(`:1387-1404`). 시계열 wind/precip 은 별도 호출(`:1410-1424`).

격자 기상은 먼저 현재 시각으로 보간한다. `sfincs_meteo.f90:1257` `if (meteo3d) then`; `sfincs_meteo.f90:1336` `if (t < (tspinup - 1.0e-3) .and. spinup_meteo) then`; `sfincs_meteo.f90:1414` `call update_wind_forcing_from_timeseries(t)`; `sfincs_meteo.f90:1422` `call update_precipitation_from_timeseries(t, dt)`; `sfincs_meteo.f90:1474` `tauwu(nm) = twu`; `sfincs_meteo.f90:1532` `netprcp(nm) = ptmp`
격자 spin-up은 이 격자장 분기 안에서 실행한다. `sfincs_meteo.f90:1257` `if (meteo3d) then`; `sfincs_meteo.f90:1336` `if (t < (tspinup - 1.0e-3) .and. spinup_meteo) then`; `sfincs_meteo.f90:1414` `call update_wind_forcing_from_timeseries(t)`; `sfincs_meteo.f90:1422` `call update_precipitation_from_timeseries(t, dt)`; `sfincs_meteo.f90:1474` `tauwu(nm) = twu`; `sfincs_meteo.f90:1532` `netprcp(nm) = ptmp` 활성·시간 조건은 `sfincs_meteo.f90:1336` `if (t < (tspinup - 1.0e-3) .and. spinup_meteo) then`이다. [10-12 전수 검증 보완]
시계열 바람·강수는 이후 해당 최종 강제를 덮어쓴다. `sfincs_meteo.f90:1257` `if (meteo3d) then`; `sfincs_meteo.f90:1336` `if (t < (tspinup - 1.0e-3) .and. spinup_meteo) then`; `sfincs_meteo.f90:1414` `call update_wind_forcing_from_timeseries(t)`; `sfincs_meteo.f90:1422` `call update_precipitation_from_timeseries(t, dt)`; `sfincs_meteo.f90:1474` `tauwu(nm) = twu`; `sfincs_meteo.f90:1532` `netprcp(nm) = ptmp`


`update_meteo_fields`(`:1548`)는 t0/t1 격자 필드를 재계산하고 device 로 갱신(`:1568-1606`).

`update_meteo_fields`는 `meteo3d`이고 예정 갱신 시각에 도달했을 때 실행한다. `sfincs_lib.f90:519` `if (meteo3d .and. update_meteo)  then`; `sfincs_lib.f90:524` `call update_meteo_fields(t, tloopwnd1)`; `sfincs_input.f90:69` `call read_real_input(500,'dtwnd',dtwindupd,1800.0)`; `sfincs_lib.f90:517` `if (wind .or. patmos .or. precip) then`; `sfincs_lib.f90:530` `call update_meteo_forcing(t, dt, tloopwnd2)` 상위 호출 조건은 `sfincs_lib.f90:517` `if (wind .or. patmos .or. precip) then`이다. [10-12 전수 검증 보완]
`dtwnd`의 기본값은 1800초다. `sfincs_lib.f90:519` `if (meteo3d .and. update_meteo)  then`; `sfincs_lib.f90:524` `call update_meteo_fields(t, tloopwnd1)`; `sfincs_input.f90:69` `call read_real_input(500,'dtwnd',dtwindupd,1800.0)`; `sfincs_lib.f90:517` `if (wind .or. patmos .or. precip) then`; `sfincs_lib.f90:530` `call update_meteo_forcing(t, dt, tloopwnd2)`
`update_meteo_forcing`는 기상 과정이 하나라도 켜져 있으면 각 시간 단계에서 실행한다. `sfincs_lib.f90:519` `if (meteo3d .and. update_meteo)  then`; `sfincs_lib.f90:524` `call update_meteo_fields(t, tloopwnd1)`; `sfincs_input.f90:69` `call read_real_input(500,'dtwnd',dtwindupd,1800.0)`; `sfincs_lib.f90:517` `if (wind .or. patmos .or. precip) then`; `sfincs_lib.f90:530` `call update_meteo_forcing(t, dt, tloopwnd2)`


---

## 4. Spiderweb 파일 I/O (`sfincs_spiderweb.f90`)

태풍 parametric wind(Holland 류 등 외부 생성 .spw 극좌표 격자)을 읽는 저수준 I/O. **물리 모델(Holland)은 SFINCS 내부에 없음** — .spw 는 외부(예: Delft3D meteo, tropical cyclone 툴) 생성물.

### 4.1 차원 읽기 (`read_spw_dimensions`, `:231`)
헤더 키워드 `n_cols/n_rows/n_quantity/spw_radius`(`:252-255`). `nquant==4` 면 precip 포함. `TIME` 블록 위치로 헤더줄 수 자동탐지(첫 30줄), 실패 시 hardcode nheader=16/18(`:264-287`). 시간블록 수 카운트로 `nt`(`:297-312`).

spiderweb 헤더 spw_radius: 근거: K055: `sfincs_spiderweb.f90:255` `call read_real_input(888,'spw_radius',spwrad,0.0)` [대조 보고서 §5 K055](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:986) 결론: 문서 누락. 이 판은 spiderweb 헤더에서 spw_radius를 기본값 0으로 읽는다.


### 4.2 데이터 읽기 (`read_spw_file`, `:8`)
블록당: time → `xe`(eye lon) → `ye`(eye lat) → peye(dummy) → `vmag`/`vdir`/`pdrp`(+`prcp` if nquant=4) 각 nrows×ncols(`:82-128`). 양은 풍속·풍향·기압강하·강우.

### 4.3 amu/amv 읽기 (`read_amuv_file` `:135` / `read_amuv_dimensions` `:320`)
직교격자 ASCII(Delft3D meteo 포맷). 헤더 `x_llcorner/y_llcorner/dx/dy`(`:347-350`), hardcode nheader=13(`:375`).

### 4.4 시간파싱 (`compute_time_in_seconds`, `:410`)
`"... <value> <unit> since YYYY-MM-DD HH:MM:SS"` 파싱. unit→ifac(seconds=1/minutes=60/hours=3600/days=86400, `:442-466`), `time_difference` 로 trefstr 기준 초 변환(`:476-482`).

---

## 5. 침투 (강우손실) (`sfincs_infiltration.f90`)

> 핵심 주석(`:28`): *"Infiltration only works when rainfall is activated"* — 강우 없이 쓰려면 0.0 precip 파일 필요. 방법들은 stack 되도록 설계되지 않음(`:30`).

### 5.1 타입 선택 (`initialize_infiltration`, `:8`)
`precip` true 시에만(`:63`). `inftype ∈ {c2d,cna,cnb,gai,hor}` (NetCDF) 또는 파일 존재로 자동 선택(`:74-135`):

| inftype | 방법 | 입력 파일/키 | 식 |
|---|---|---|---|
| `con` | 공간균일 상수 | `qinf` (sfincs.inp) | — |
| `c2d` | 공간변동 상수 | `qinffile`/`qinf` | mm/hr→m/s (`:256`) |
| `cna` | Curve Number (구, recovery 없음) | `scsfile`/`scs` | inch→m ×0.0254 (`:290`) |
| `cnb` | Curve Number (신, recovery) | `seff/smax/ks` | SWMM 회복 |
| `gai` | Green-Ampt | `psi/sigma/ks` | SWMM Eq 4-27 |
| `hor` | modified Horton | `fc/f0/kd` | 지수감쇠 |

NetCDF 입력은 quadtree mesh 전용, ASCII binary 입력은 regular mesh 전용(`:170-189`). `cumprcp/cuminf/qinfmap` 할당(`:139-152`).

균일 상수 `con`은 격자 형식 제한에서 제외한다. `sfincs_infiltration.f90:170` `if (infiltration .and. inftype /= 'con') then !constant uniform works for both options`; `sfincs_infiltration.f90:174` `if (use_quadtree .eqv. .false.) then`; `sfincs_infiltration.f90:176` `call stop_sfincs('Error ! Netcdf infiltration input format can only be specified for quadtree mesh model !', 1)`; `sfincs_infiltration.f90:182` `if (use_quadtree .eqv. .true.) then`; `sfincs_infiltration.f90:184` `call stop_sfincs('Error ! Infiltration input for quadtree mesh model can only be specified using the infiltrationfile Netcdf format! !', 1)`
나머지 netCDF 침투 자료는 quadtree를 요구한다. `sfincs_infiltration.f90:170` `if (infiltration .and. inftype /= 'con') then !constant uniform works for both options`; `sfincs_infiltration.f90:174` `if (use_quadtree .eqv. .false.) then`; `sfincs_infiltration.f90:176` `call stop_sfincs('Error ! Netcdf infiltration input format can only be specified for quadtree mesh model !', 1)`; `sfincs_infiltration.f90:182` `if (use_quadtree .eqv. .true.) then`; `sfincs_infiltration.f90:184` `call stop_sfincs('Error ! Infiltration input for quadtree mesh model can only be specified using the infiltrationfile Netcdf format! !', 1)`
나머지 기존 침투 자료는 quadtree를 허용하지 않는다. `sfincs_infiltration.f90:170` `if (infiltration .and. inftype /= 'con') then !constant uniform works for both options`; `sfincs_infiltration.f90:174` `if (use_quadtree .eqv. .false.) then`; `sfincs_infiltration.f90:176` `call stop_sfincs('Error ! Netcdf infiltration input format can only be specified for quadtree mesh model !', 1)`; `sfincs_infiltration.f90:182` `if (use_quadtree .eqv. .true.) then`; `sfincs_infiltration.f90:184` `call stop_sfincs('Error ! Infiltration input for quadtree mesh model can only be specified using the infiltrationfile Netcdf format! !', 1)`


회복률(`cnb`,`gai`) **SWMM Eq 4-36**(`:374-375`): `inf_kr = sqrt(ksfield/25.4)/75` (ks mm/hr→inch/hr, /75=days). Green-Ampt 상부회복깊이 **Eq 4-33**(`:488`): `GA_Lu = 4*sqrt(25.4)*sqrt(ksfield)`. GA 단위 m/m·s 변환(`:492-494`).

### 5.2 매 timestep 갱신 (`update_infiltration_map`, `:607`)
모든 분기 공통 후처리: `netprcp(nm) -= qinfmap(nm)`(`:661` 등), `cuminf += qinfmap*dt`(store 시).

- **con/c2d**(`:630`): `qinfmap=qinffield`, 물 없으면 0(`:639-657`).
- **cna**(`:676`): Curve Number. `Ia = sfacinf·S`(S=`qinffield`) 초과 시 누적 runoff(`:689-695`):

  $$Q = \frac{(P - I_a)^2}{P + (1-\text{sfacinf})S}, \quad I = P - Q, \quad q_{inf} = (I - \text{cuminf})/\Delta t$$

- **cnb**(`:722`): 이벤트별 `scs_P1/F1/S1`, recovery(비강우 시 `rain_T1` 누적, **Eq 4-37** `0.06/inf_kr` 초과 시 S 회복, `:800-806`).
- **gai** Green-Ampt(`:828`): `prcp<ks` 면 전량 침투, 아니면 **SWMM Eq 4-27**(`:856`):

  $$q_{inf} = k_s\left(1 + \frac{\psi\cdot\sigma}{F}\right)$$

  ```fortran
  qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))
  ```

B123·C026의 Green-Ampt 인덱스 후보는 [검증 정본](sfincs_infiltration.md#cv-s-b123)을 따른다. 고강수 분기와 결과 제한의 조건도 정본에 적었다. [10-12 결론 검증 보완]
  이 식은 명시적인 h0 항을 포함하지 않는다. `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`
B123·C026의 Green-Ampt 인덱스 후보는 [검증 정본](sfincs_infiltration.md#cv-s-b123)을 따른다. 고강수 분기와 결과 제한의 조건도 정본에 적었다. [10-12 결론 검증 보완]
  포화 수리전도도와 누적 침투 상태는 각 셀의 값을 사용한다. `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`; `sfincs_infiltration.f90:863` `GA_sigma(nm) = max(GA_sigma(nm) - (qinfmap(nm) * dt / GA_Lu(nm)), 0.0)`; `sfincs_infiltration.f90:867` `GA_F(nm)    = GA_F(nm) + qinfmap(nm) * dt   ! internal cumulative rainfall from Green-Ampt`
  전체 침투율이 공간적으로 균일해진다고 단정할 수 없다. `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`; `sfincs_infiltration.f90:863` `GA_sigma(nm) = max(GA_sigma(nm) - (qinfmap(nm) * dt / GA_Lu(nm)), 0.0)`; `sfincs_infiltration.f90:867` `GA_F(nm)    = GA_F(nm) + qinfmap(nm) * dt   ! internal cumulative rainfall from Green-Ampt`
  np를 nm로 바꾸는 작성 의도는 확인하지 않았다. `sfincs_infiltration.f90:838` `do nm = 1, np`; `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`
  원문 식과 결함 해석을 구분한다. `docs/input.rst:496` `**f(t) = K(1+ delta_theta (sigma + h0) / F(t) )**`; `sfincs_infiltration.f90:838` `do nm = 1, np`; `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`

  σ·F 갱신(`:863-867`), 비강우 회복 **Eq 4-35**(`:884`).
- **hor** modified Horton(`:912`): 침투능 지수감쇠(`:967`,`:979`):

  $$f = f_c + (f_0 - f_c)\,e^{k_d\, t/3600}, \quad I = e^{k_d\, t/3600}$$

  ```fortran
  I = exp(horton_kd(nm) * rain_T1(nm) / 3600)
  qinfmap(nm) = (horton_fc(nm) + (horton_f0(nm) - horton_fc(nm)) * I) / 3600 / 1000
  ```
  `rain_T1` 은 침투중 음수 누적(storm 시작 시 0 reset, `:955-963`), 1% 미만이면 `f_c` 로 수렴(`:971-975`). 가용수량 `Qq` 로 capacity scale(`:1000-1004`), 비강우·비ponding 시 `horton_kr_kd` 비율로 회복(`:1010`).

---

## 6. compound flooding 외력 종합

SFINCS compound flooding 의 동인이 본 5모듈에서 합쳐진다:

1. **해양측**: tide(`bca` 천문조) + surge(`bzs`) + IG wave(`bzi`) + 기압역조(`patmos` 보정) → kcs=2 약반사 경계 flux.
2. **태풍 강제**: spiderweb(`spw`) 바람→wind stress(land reduction 포함) + 기압강하 + (옵션)강우. 격자 meteo(`am*`)와 background 병합 가능.
3. 기상 강제는 `prcp`와 `netprcp`를 만든다. `sfincs_meteo.f90:1319` `netprcp(nm) = prcp(nm)`; `sfincs_infiltration.f90:661` `netprcp(nm) = netprcp(nm) - qinfmap(nm)`; `sfincs_continuity.f90:118` `zs(nm) = zs(nm) + netprcp(nm) * dt`; `sfincs_continuity.f90:481` `dzsdt = dzsdt + netprcp(nm)`
   침투는 같은 단계의 `netprcp`에서 `qinfmap`을 뺀다. `sfincs_meteo.f90:1319` `netprcp(nm) = prcp(nm)`; `sfincs_infiltration.f90:661` `netprcp(nm) = netprcp(nm) - qinfmap(nm)`; `sfincs_continuity.f90:118` `zs(nm) = zs(nm) + netprcp(nm) * dt`; `sfincs_continuity.f90:481` `dzsdt = dzsdt + netprcp(nm)`
   연속식은 같은 단계의 차감 결과를 읽는다. `sfincs_meteo.f90:1319` `netprcp(nm) = prcp(nm)`; `sfincs_infiltration.f90:661` `netprcp(nm) = netprcp(nm) - qinfmap(nm)`; `sfincs_continuity.f90:118` `zs(nm) = zs(nm) + netprcp(nm) * dt`; `sfincs_continuity.f90:481` `dzsdt = dzsdt + netprcp(nm)`
4. **하천측**: 점소스 방류(`src/dis`) + 하류 하천 경계(`bdr`, kcs=5) + 배수구조물(pump/culvert/gate).

외력의 연속식 net source·모멘텀 forcing 연결은 계산 모드별로 구분한다; `bathtub` 모드는 경계조건에 따라 수위만 갱신한다(`sfincs_lib.f90:572-584`; 상세 솔버는 [[sfincs-architecture-source-map]]). 모든 외력의 동일 경로 처리는 이 근거로 확인되지 않았다.

## 문서 참고 링크 오류

v2.0.2 릴리스 링크의 정정은 [변경 이력 노트의 정본](../manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md#문서-참고-링크-오류)을 따른다. [10-12 결론 검증 보완]
