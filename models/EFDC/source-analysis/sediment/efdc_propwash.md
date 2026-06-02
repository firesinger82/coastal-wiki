---
title: "EFDC+ Propwash 모듈 — 선박 프로펠러 wash 침식 (Hamill 3-zone 제트 + Maynord shear + SEDZLJ/vanRijn 결합) verified"
topic: sediment-transport
canonical_source: external
external_source: "EFDC+ source_code/EFDCPlus_Stable/EFDC/Propwash/ (17 files 3507 lines: Propwash_Calc_Sequence.f90 + Variables_Propwash.f90 + Calc_Prop_Erosion.f90 707 + Mod_Active_Ship.f90 1269 + Mod_Read_Propwash.f90 501 등) + EFDC+_Propwash_WhitePaper.pdf (DSI LLC, 2021-08-17, 93p) Ch 1-3 (Eq 2.4-2.15, 3.1-3.2). 저자 Paul M. Craig + Zander Mausolff + Luis Bastidas."
citation_status: verified
verification_method: "source_code 직접 read (Propwash_Calc_Sequence 130줄 + mod_Variables_Propwash 70줄 + Calc_Prop_Erosion 230줄 + **Mod_Active_Ship 1269줄 deep: calc_velocity 801-927·calc_erosive_flux 935-1203·setup_mesh 361-450 verbatim**) + WhitePaper.pdf p.1-3장 직접 read (Abstract·Ch1·Ch2 Eq 2.4-2.15·Ch3 11-step + Eq 3.1-3.2 Maynord shear). 식·계수·zone 경계 verbatim. **code≠WhitePaper 차이 7건 식별** (§6.6: Jiang2019 efflux·Toutant thrust·B' P'^-1·Hashmi1993 fallback·zone1 3.5·ambient 무시·13° cone)."
note_author: "Claude Opus 4.8 (1M context) raw source + PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 2.4-2.15·3.1-3.2 + zone 경계(0.35/3.25/50) + 계수 verbatim"
verification_date: 2026-06-02
related:
  - models/EFDC/source-analysis/sediment/efdc_sedzlj.md
  - models/EFDC/source-analysis/efdc_dispersion.md
  - concepts/sediment-transport/README.md
---

# EFDC+ Propwash 모듈 — verified

> EFDC+ Propwash source(17 files 3507줄) + WhitePaper(93p) 직접 read. **선박 프로펠러 wash 의 sediment 재부유·scour** — Hamill 제트 속도장 → Maynord bed shear → van Rijn/SEDZLJ 침식, **3D hydro+sediment+toxics 완전 결합**. DSI LLC(Paul Craig 등). 침식은 [[efdc_sedzlj]] 머신 재사용.

## 0. 배경 (WhitePaper Ch 1)

> "Propeller wash is the flow generated behind a rotating propeller." 도시 waterfront(San Diego Bay·Gowanus Canal·Newtown Creek·Lower Duwamish·Portland Harbor Superfund)의 **오염 sediment 재부유** + quay scour(구조 불안정/붕괴, PIANC 2015) 주범.
>
> **San Diego Bay**: 3 naval pier berthing 이 **26 tons/day** 재부유 (Wang 2016). **Kingston Ferry(WA)**: ferry 도착/출발이 ambient 대비 **유속 10-30배·shear 10-100배** (Kastner 2019).
>
> 기존 모델 한계: uncoupled(외부 empirical 계산→source term 수동 입력, Chadwick 2008), steady-state, 단일 선종. **EFDC+ = fully coupled 3D** (resuspension+scour → advection/diffusion/settling → redeposition, Fig 1.1).

**핵심 capability**: ① 선박별 독립 sub-grid mesh ② 다중 선박 동시 ③ AIS/user track 보간 ④ ambient current 포함 shear ⑤ multi-propeller superposition ⑥ Original-EFDC(van Rijn 1984)·SEDZLJ(Jones-Lick 2001) 결합 ⑦ bedload+geomorphic feedback ⑧ **efflux momentum 을 3D flow field 에 주입**.

## 1. 이론 — 프로펠러 제트 속도장 (WhitePaper Ch 2)

3 zone (Fig 3.4, $x/D_p$ 기준): **Efflux Zone (0-0.35)** → **Zone of Flow Establishment (0.35-3.25)** → **Zone of Established Flow (3.25-50)**.

### 1.1 Efflux velocity $V_0$ (Eq 2.4-2.5)

Effective push $EP$(lbf, P=engine power hp 함수) → thrust:
$$T(\text{N}) = 4.45 \times EP(\text{lbf}) \quad \text{(2.4)}$$
$$V_0 = 1.13 \times \frac{1}{D_0}\sqrt{\frac{T}{\rho_w}} \quad \text{(2.5, Maynord 2000)}$$
- $D_0$ = contracted wash diameter = **$0.71D_p$ (non-ducted)** / $D_p$ (ducted), $\rho_w$ = water density
- **대안** (Fig 3.4, Hamill thrust-coeff 형): $V_0 = 1.33\,n\,D_p\,C_t^{0.5}$ ($n$=rps, $C_t$=thrust coefficient)
- Efflux Zone($x/D_p<0.35$): $V_{x,r} = V_0$ (일정)

### 1.2 Zone of Flow Establishment (Eq 2.6-2.9)

축방향 max 속도(거리 선형 감소, Hamill-Kee 2016):
$$\frac{V_{x,max}}{V_0} = 1.51 - 0.175\left(\frac{x}{D_p}\right) - 0.46P' \quad \text{(2.6)}$$
($P'$=propeller pitch/diameter ratio). 측방향 **twin-peak Gaussian** (hub 영향, 회전축에 저속 core):
$$\frac{V_{x,r}}{V_{x,max}} = \exp\left[-\frac{1}{2}\left(\frac{r-R_{mo}}{\sigma}\right)^2\right] \quad \text{(2.7)}$$
$$\sigma = \begin{cases} 0.5R_{mo} & x/D_p < 0.5 \\ 0.5R_{mo} + 0.075(x+0.5D_p) & x/D_p \ge 0.5 \end{cases} \quad \text{(2.8)}$$
$$R_{mo} = 0.67(R_p - R_h) \quad \text{(2.9)}$$
($R_{mo}$=max 속도 반경, $R_p$=propeller 반경, $R_h$=hub 반경). **zone 끝 $x/D_p=3.25$** (Stewart 1992, Hamill-Kee 2016 권장; Fuehrer-Römisch/Blaauw 2.6, Verhey 2.77).

### 1.3 Zone of Established Flow (Eq 2.10-2.13)

outward mixing 만, single peak (회전축). Hamill(1987) 축 감쇠:
$$\frac{V_{x,max}}{V_0} = A'\left(\frac{x}{D_p}\right)^{B'} \quad \text{(2.10)}$$
$$A' = -11.4C_t + 6.65\beta + 2.16P' \quad \text{(2.11)}$$
$$B' = -C_t^{-0.216}\times\beta^{1.024}\times P'^{-1.87} \quad \text{(2.12)}$$
($\beta$=blade area ratio=disk area coefficient). 측방향 **single Gaussian** (Fuehrer-Römisch 1977):
$$\frac{V_{x,r}}{V_{x,max}} = \exp\left[-22.2\left(\frac{r}{x}\right)^2\right] \quad \text{(2.13)}$$

### 1.4 Water-sediment interface 속도 (Eq 2.14-2.15)

sub-grid 점의 종방향 $x=X_p$ **(2.14)**, 반경 $r = \sqrt{Y_p^2 + H_p^2}$ **(2.15)** ($X_p$=종거리, $Y_p$=측거리, $H_p$=프로펠러축→bed 연직거리) → Eq 2.7/2.13 으로 bed 속도 계산.

## 2. 알고리즘 (WhitePaper Ch 3, 11-step)

매 sediment time step (Fig 3.1):
1. **Compute Hydrodynamic Flow Field** (model grid, 3D ambient)
2. **Specify Ship Position** (AIS/user track 보간 — location·heading·speed·power)
3. **Generate Sub-grid Points** (선박 뒤 독립 2D sub-grid, prop diameter 배수)
4. **Determine Bottom Elevation** (sub-grid 점, **inverse distance squared** 보간)
5. **Compute Propeller Wash Velocity at Bottom** (Ch 2, multi-prop **superposition** $V_{x,r}=V_{x,r,\text{left}}+V_{x,r,\text{right}}$ Fig 3.5)
6. **Combine Propeller Wash + Ambient Velocities** (near-bed velocity)
7. **Compute Shear Stress at Bottom** (Maynord 2000):
$$\tau_p = 0.5 \times \rho_w \times C_f \times V_{bed}^2 \quad \text{(3.1)}$$
$$C_f = 0.01 \times \frac{D_p}{H_p} \quad \text{(3.2)}$$
8. **Compute Erosion Rate at Bottom** (van Rijn 또는 SEDZLJ)
9. **Calculate Erosion Mass for Sub-grid Areas**
10. **Aggregate Sub-grid Erosion Mass to Model Grid**
11. **Compute Sediment Transport Process** (→ 다음 step) + **(Optional) Add Efflux Momentum to Flow Field**

## 3. 소스 구현

### 3.1 Propwash_Calc_Sequence.f90 (130줄, orchestration)

`Propwash_Calc_Sequence(ieffluxonly)` — Paul Craig + Zander Mausolff:
- 1회 초기화: `Det_Adjacent_Cells` (valid cell 인접 cell)
- `DTSEDJ = DTSED` (ISTRAN(6)+ISTRAN(7)>0 = sediment/toxic) else `DT`
- **전 선박 loop** (`total_ships`): `det_if_in_track`(시간이 track 내?) → active 시 `det_pos_in_track`+`interp_track`(위치 보간) → `power==0 .or. cell<2` 시 skip(docked/anchored/domain 밖)
  - `ieffluxonly==0`: `setup_mesh` + `calc_erosive_flux`
  - else: `calc_velocity` (efflux velocity 만, momentum field 용)
- **총 침식 합산**: `prop_ero(L,0) = sum(prop_ero(L,1:NSEDS))` (suspended) + `prop_bld`(bedload, ICALC_BL>0). `prop_ero(L,0)` 는 cell 침식 flag
- `TPROPW` 계산시간 logger

### 3.2 Variables_Propwash.f90 (변수·계수)

| 변수 | 기본값 | 의미 |
|---|---|---|
| `ISPROPWASH` | — | propwash primary flag (1/2) |
| `total_ships` | — | 선박 수 |
| `mesh_width` / `mesh_Length` | 30 / 60 | sub-grid 폭/길이 (**prop diameter 배수**) |
| `efflux_zone_mult` | 0.35 | efflux zone 크기 (=$x/D_p$ 경계) |
| `flow_est_zone1_mult` | 3.5 | flow establishment (single/no-influence) |
| `flow_est_zone2_mult` | 14 | flow establishment (dual-prop influence) |
| `efflux_mag_mult` | 0.75 | ISPROPWASH=2 efflux 보정 (소규모 turbulent eddy) |
| `fraction_fast` | 0 | 재부유 sediment 중 fast-settling 분율 |
| `fast_multiplier` | 30 | fast class 침강속도 배수 |
| `num_radial_elems` / `num_axial_elems` | — | mesh 점 수 (수직/축방향) |

- 출력: `prop_ero(:,:)` suspended (g/cm²) + `prop_bld(:,:)` bedload, sediment class 별
- **cohesive 분리/fast-slow settling split**: `IWC2BED`/`IBED2WC`/`IFASTCLASS`
- **change record**: 2020-01 구조 신설(Mausolff) / **2020-12 SEDZLJ+toxics 결합 완료**(Craig) / **2021-12 efflux momentum→flow field**(Craig)

### 3.3 Calc_Prop_Erosion.f90 (707줄, SEDZLJ 결합 침식)

`Calc_Prop_Erosion_SEDZLJ(L, TAUP, ELAY, SURFACE)` — propwash shear `TAUP`(N/m²)로 **[[efdc_sedzlj]] 침식 머신 재사용**:
- `TAUDYNE = 10.*TAUP` (Pa→dynes)
- surface layer 탐색 (`TSED(K,L)>0.001` 0.1mm 무시), 부족 시 high-shear flag(1e-12) return
- `D50AVGL` 표면 d50 → `TAUCRIT` 보간 (`TAUCRITE`, in-place는 `TAUCOR`)
- **active layer** `TACT = TACTM*D50AVGL*(TAUDYNE/TAUCRIT)*(BULKDENS/10000)` ([[efdc_sedzlj]] Eq 동일)
- erosion rate: `NSEDFLUME==1` Sedflume `ERATE` shear+depth 이중보간 (LAYERACTIVE==2 deeper) + `SH_SCALE`(Lick 2009 slope) — **SEDZLJ 와 동일 식**, 입력만 propwash shear
> Original-EFDC(van Rijn)용 별도 분기도 존재 (note: SEDZLJ variant 만 상세 read).

### 3.4 Mod_Active_Ship.f90 (1269줄, deep — 제트식·shear·mesh 코드 구현) ★

`active_ship` 객체 (type-bound: constructor·interp_track·det_if_in_track·det_pos_in_track·setup_mesh·interp_depth_elev·interp_bot_vel·**calc_velocity**·**calc_erosive_flux**·write_xyz). Paul Craig + Luis Bastidas + Zander Mausolff.

#### 3.4.1 `calc_velocity(ax, radius, bot_velocity, ieffluxonly)` — Ch 2 식 코드 매핑 (801-927)

**Efflux velocity** (Eq 2.4-2.5 구현, 단 코드 ≠ WhitePaper 일부):
- **rps 기반** (rps≥0): `efflux_vel = 1.59*rps*prop_diam*sqrt(thrust_coeff)` — **Jiang et al. 2019** 채택 (Hamill 1987 `1.33*` + Hamill-Kee 2016 `1.22*rps^1.01*D^0.84*C_t^0.62` 는 **주석처리**; ⚠ WhitePaper Fig 3.4 는 1.33 표기)
- **power 기반** (rps<0): power = ship power/num_props (단일 prop 가정). **Toutant thrust** EP[lbf]:
  - open: `EP = 23.57*power^0.974 - 2.3*(speed*2.237)²*sqrt(power)`, C1=0.71
  - ducted: `EP = 31.82*power^0.974 - 5.4*(speed*2.237)²*sqrt(power)`, C1=1.0
  - `EP = max(EP, power)` (Toutant high-speed/low-power 붕괴 방지), `EP = 4.448*EP` (lbf→N)
  - `efflux_vel = 1.13/C1/prop_diam*sqrt(EP/rho)` (Eq 2.5, **C1 = D_0/D_p contraction**, rho = RHOW or 999.82)
- `self.efflux_vel = efflux_vel * efflux_mag_mult` (0.75, subgrid turbulent loss). `ieffluxonly>0` → efflux 만 return (momentum field 용)

**Zone 분기** (cutoff: `zone0 = efflux_zone_mult(0.35)*D_p`, `zone1 = flow_est_zone1_mult(3.5)*D_p` — ⚠ WhitePaper 는 3.25):
- **Efflux** (ax≤zone0): vel_max = efflux_vel; radial: `radius ≤ 0.75*D_p` → bot_velocity = efflux_vel
- **Flow establishment** (zone0<ax<zone1): `vel_max_ax = efflux_vel*(1.51 - 0.175*(ax/D_p) - 0.46*pitch_ratio)` (Eq 2.6). `R_m0 = 0.67*(0.5*D_p - 0.5*hub_diam)` (Eq 2.9). σ: `ax<R_p` → `0.5*R_m0` else `0.5*R_m0 + 0.075*(ax - R_p)` (Eq 2.8, ⚠ 코드 `(ax-radius_prop)` vs WhitePaper `(x+0.5D_p)`). `bot_velocity = vel_max_ax*exp(-0.5*(radius-R_m0)²/σ²)` (Eq 2.7 twin-peak)
- **Established flow** (ax≥zone1): `A' = -11.4*C_t + 6.65*BAR + 2.16*pitch_ratio` (Eq 2.11, code "eqn 2.32"). **A'>1 시**: `B' = -(C_t^-0.216)*BAR^1.024/pitch_ratio` (⚠ 코드 `P'^(-1)` vs WhitePaper Eq 2.12 `P'^(-1.87)`), `vel_max = efflux_vel*A'*(ax/D_p)^B'` (Eq 2.10). **A'≤1 또는 BAR 미상 시 fallback = Hashmi 1993**: `vel_max = efflux_vel*0.638*exp(-0.097*(ax/D_p))`. radial: `bot_velocity = vel_max*exp(-22.2*(radius/ax)²)` (Eq 2.13)
- `bot_velocity < epsilon(1e-3)` → 0

#### 3.4.2 `calc_erosive_flux(debug_)` — shear + erosion + aggregation (935-1203)

- **Maynord c_f** (Eq 3.2): `d2 = w_depth - draft` (max with prop_radius, = **H_p** prop축→bed), `c_f = 0.01*prop_diam/d2` (선박당 상수, 2021-06-28)
- **OMP PARALLEL** over `num_axial_elems` × `num_radial_elems` sub-grid:
  - `interp_depth_elev` → z_bed, w_depth; `d2 = w_depth - draft`
  - **multi-prop superposition** (Eq 3.5): `prop_off = -0.5*dist_between_props*(num_props-1)`, prop loop: `d1 = horizontal dist`, **`radius = sqrt(d1² + d2²)`** (Eq 2.15 r=√(Y_p²+H_p²)), `calc_velocity(ax, radius, vel2)` → `bot_velocity += vel2`
  - **Maynord shear** (Eq 3.1): `bot_velocity > 1e-2` 시 `shear = 0.5*RHOW*c_f*vel2²` [N/m²]. ⚠ **ambient velocity 무시** (analytical solution, 2021-11-10; ordinary sediment transport 에선 사용)
  - **erosion** (ISTRAN(6)+ISTRAN(7)>0, LBED hard-bottom bypass):
    - `LSEDZLJ` → `Calc_Prop_Erosion_SEDZLJ(cell, shear, elay, isurf)` → `elay*area` = mass(g)
    - else → `Calc_Prop_Erosion_Original(cell, shear*0.001, elay, ebld)` (van Rijn, density-normalized m²/s²): `elay*area + ebld*width*DTSEDJ`
- **accumulate** (OMP 밖, race 방지): `prop_ero(cell,1:NSEDS) += subgrid.ero`
- `self.max_bot_vel = 0.25*vb_max` (ISPROPWASH=2 momentum double-counting 방지)
- **pw_mesh_<MMSI>.out** binary 출력 (`freq_out` 주기): x/y/z + var(1)=velocity, var(2)=shear[Pa], var(3)=erosion rate(LSEDZLJ g/cm²/s / Orig g/m²/s)

#### 3.4.3 `setup_mesh(debug_)` — sub-grid 생성 (361-586)

- radial 범위: `±0.5*mesh_width(30)*(prop_diam + 0.5*width_propellers)`. axial: `0.5*efflux_zone_mult*D_p` ~ `mesh_length(60)*D_p`
- `area = width*length*10000` (cm², SEDZLJ) / `width*length` (m², Original)
- **13° spreading cone**: `tan13 = 0.23087`, `cone_max = tan13*y_pos + width_propellers`; cone 밖 점 비활성화 (x_pos=-9999, area=0) — 프로펠러 wash 확산각
- bottom elevation: `interp_depth_elev` (model cell **inverse distance squared** 보간, WhitePaper Step 4)

#### 3.4.4 `interp_track` (134-250)

AIS/user track 의 시간 보간 (prev/next track 위치 사이 선형) → ship position·heading·speed·power. `det_if_in_track`(시간 ∈ track?) + `det_pos_in_track`(track 내 위치 index).

### 3.5 기타 source (요약)

| 파일 | 줄 | 역할 |
|---|---|---|
| `Mod_Read_Propwash.f90` | 501 | propwash_config/ships/tracks.jnp 입력 |
| `mod_Setup_Ships.f90` | 245 | 선박 초기화 |
| `Mod_Ship.f90` | 118 | ship base type |
| `Mod_Position*.f90` | 25-111 | 위치/cell/elevation |
| `Mod_Erosive_Flux.f90` | 44 | erosive flux |
| `Det_Adjacent_Cells.f90` | 50 | 인접 cell |

## 4. 입력 (4 파일)

- `efdc.inp` — propwash control (Table 4.1)
- `propwash_config.jnp` — sub-grid config (mesh 크기·zone mult, Table 4.2)
- `propwash_ships.jnp` — 선박·프로펠러 spec (Table 4.3; 미지 시 **PIANC 2015·NYSDOT 2005·TugboatInformation 회귀** 가이드)
- `propwash_tracks.jnp` — track (시간·위치·power, status code "n", Table 4.4-4.5)

## 5. 검증 (WhitePaper Ch 5)

- **Flume** (Hong 2016): 속도 profile 재현 (Fig 5.1)
- **San Diego Bay tugboat** (Wang 2016, Tractor C-14): 110m 후방 ADV 속도·**modified TKE shear**·PIV erosion depth (Fig 5.4-5.6)
- **Kingston Ferry(WA)** (Kastner 2019, M/V Walla Walla/Puyallup): AIS 3-ferry track, near-bed velocity·bottom shear (Fig 5.21-5.27)
- sediment 검증: cohesive·non-cohesive·SEDZLJ bed scour (다른 propeller power·입경), straight channel 2-ship + efflux momentum 유무 비교

## 6. 핵심 finding

1. **propwash = SEDZLJ 침식의 또 다른 shear source** — `Calc_Prop_Erosion_SEDZLJ` 가 ambient bed shear 대신 propwash `TAUP` 입력, 나머지 SEDZLJ 머신([[efdc_sedzlj]]) 동일.
2. **sub-grid mesh** (선박당 독립, prop diameter 30×60) → model grid aggregate: 연안 모델 해상도 < 프로펠러 wash 스케일 문제 해결.
3. **efflux momentum→3D flow** (2021-12) = 단순 침식 source 넘어 hydro 결합 (기존 모델 한계 극복).
4. **toxics 결합** (2020-12): 오염 sediment 재부유 → Superfund remediation 평가 (San Diego/Duwamish/Portland Harbor).
5. Maynord(2000): efflux velocity(2.5) + bed shear(3.1-3.2) 둘 다 → propwash 의 핵심 reference.
6. **★ code ≠ WhitePaper(2021-08) 차이 (Mod_Active_Ship deep, §3.4)** — 실 구현이 매뉴얼보다 갱신됨:
   - efflux rps-기반: 코드 **Jiang et al. 2019 (1.59)** (Hamill 1987 1.33·Hamill-Kee 2016 주석처리; WhitePaper Fig 3.4는 1.33)
   - power-기반: **Toutant thrust** EP(open 23.57·P^0.974 / ducted 31.82, max(EP,power) 보정) — WhitePaper Ch 2는 generic
   - B' 지수: 코드 `P'^(-1)` vs WhitePaper Eq 2.12 `P'^(-1.87)`
   - A'≤1/BAR 미상 fallback: **Hashmi 1993** `0.638·exp(-0.097 x/D_p)` (WhitePaper 무)
   - zone1 cutoff: 코드 `flow_est_zone1_mult=3.5` vs WhitePaper 3.25
   - **ambient velocity**: propwash analytical shear서 **무시** (2021-11-10) — WhitePaper Abstract "including ambient currents"와 뉘앙스 차 (ordinary sediment transport엔 반영)
   - 13° spreading cone (tan13=0.23087)로 sub-grid 점 필터 (WhitePaper 미명시)
   - 코드 주석 식번호("eqn 2.32/2.33")가 WhitePaper(2.11/2.12)와 달라 → **별도/갱신 doc 버전** 존재 시사

## 7. 한계

- ✅ `Mod_Active_Ship.f90` (1269줄) deep read 완료 (§3.4) — calc_velocity·calc_erosive_flux·setup_mesh·interp_track. **code ≠ WhitePaper 차이 발견** (§6.6).
- `Calc_Prop_Erosion_Original` (van Rijn 분기) 미상세 read — SEDZLJ variant 만 §3.3 상세.
- WhitePaper Ch 4(입력 detail)·Ch 5(검증 정량값) full read 안 함 — TOC + Fig 목록 기준 요약.
- toxics linkage(caltox) 코드 미read — [[efdc-toxics]] 별도 후속.

## 8. 연결

- [[efdc_sedzlj]] — SEDZLJ 침식 머신 (Calc_Prop_Erosion 재사용, TACT/ERATE/SH_SCALE 동일)
- [[efdc_dispersion]] — EFDC 분산
- [[sediment-transport]] concepts — 표사이동 (propwash = 인위 재부유)
