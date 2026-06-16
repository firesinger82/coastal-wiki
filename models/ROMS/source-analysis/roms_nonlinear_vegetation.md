---
title: "ROMS 식생 모듈 — 식생 항력·파 감쇠·streaming·식생 난류"
model: ROMS
component: ROMS/Nonlinear/Vegetation
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Nonlinear/Vegetation/). vegetation_drag.F(항력·Luhar-Nepf flex reconfiguration), vegetation_stream.F(파 streaming), vegetation_turb.F(Uittenbogaard 식생 난류), vegetation_mod.h/var.h(자료구조·plant 4속성), vegetation_inp.h(CD_VEG 읽기), marsh_wave_thrust.F(Tonelli thrust) file:line 인용. rhs3d.F·step2d_LF_AM3.h 결합점 확인"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_nonlinear_physics_modules.md
  - models/ROMS/source-analysis/roms_vertical_mixing.md
  - models/ROMS/source-analysis/roms_wec.md
  - models/ROMS/README.md
---

# ROMS 식생 모듈 — 식생 항력·파 감쇠·streaming·식생 난류

> 한줄 요약(경로: roms/ROMS/Nonlinear/Vegetation/): 수중 식생(SAV: seagrass·salt marsh·mangrove)이 흐름에 가하는 항력, 식생에 의한 난류(TKE/length-scale) 생성, 파 streaming, 그리고 마쉬 가장자리 파 thrust를 계산하는 COAWST 계열 식생 모듈. 핵심은 `vegetation_drag.F`(Luhar-Nepf 굽힘식 자세의존 항력) + `vegetation_turb.F`(Uittenbogaard) + `vegetation_stream.F`. 출처: Beudin et al. 2017 (Comp. & Geosci.).

이 노트는 **식생 항력·파 감쇠·식생-흐름 상호작용·streaming·식생 난류** 에 집중한다. 같은 디렉토리의 `marsh_*` (조간대 마쉬 침식/수직성장/조차) 동역학은 별도 영역이며 wave-thrust만 항력 관련으로 간략 다룬다.

## 1. 디렉토리 구성과 모듈 정체

| 파일 | 역할 | 주요 CPP 게이트 |
|---|---|---|
| `vegetation_drag.F` | 식생 항력 → momentum RHS (3D+2D) | `VEGETATION && VEG_DRAG` |
| `vegetation_turb.F` | 식생 유발 TKE/GLS 생성 → 연직혼합 | `VEGETATION && VEG_TURB` |
| `vegetation_stream.F` | 파-식생 dissipation의 흐름 streaming 효과 | `VEGETATION && VEG_STREAMING` |
| `vegetation_mod.h` | T_VEG 자료구조·파라미터·할당/초기화 | — |
| `vegetation_var.h` | NetCDF metadata index 배정 | — |
| `vegetation_inp.h` | `read_VegPar` 입력 파라미터 읽기 | — |
| `vegetation_output.F` | 식생/마쉬 변수 NetCDF 출력 | — |
| `vegetation_biomass.F` | (미사용) 구식 식생속성 갱신 — `sed_biomass` | `SED_BIOMASS` |
| `marsh_*.F` | 마쉬 동역학(thrust·침식·수직성장·조차) | `MARSH_DYNAMICS` 등 |

식생 모듈 헤더 주석: "This routine computes the vegetation (posture-dependent) drag for rhs3d.F" (`vegetation_drag.F:13-14`). 저작자는 J.C. Warner / N.K. Ganju / A. Beudin / T.S. Kalra (`vegetation_drag.F:8-11`). 모듈 정체는 "Sumerged Aquiatic Vegetation Model" (`vegetation_mod.h:9`, 원문 오타 그대로).

`vegetation_biomass.F`는 파일 상단에 "This file is not used ... It is an old method to update vegetation properties. It is not used anywhere in the model." 명시 (`vegetation_biomass.F:2-4`) — 실 경로에서 비활성.

## 2. 식생 자료구조 — plant 4속성

식생 상태는 `T_VEG` 구조체의 `plant(i,j,iveg,iprop)` 4차원 배열로 표현되며, 마지막 인덱스는 4개 식물 속성 (`vegetation_mod.h:164-169`):

| sub-index | 의미 | 단위 |
|---|---|---|
| `isDens=1` | 밀도 (단위면적당 개체수) | indiv/m² |
| `isDiam=2` | 평균 직경 | m |
| `isHght=3` | 평균 높이 | m |
| `isThck=4` | 평균 두께 | m |

`NVEGP=4` 식물 속성 수 (`vegetation_mod.h:169`), `NVEG` = 식생 타입 수 (seagrass·salt marsh·mangrove 등, `vegetation_mod.h:174-176`).

입력 항력/물성 파라미터 (타입·격자별 allocatable, `vegetation_mod.h:186-191`):
- `CD_VEG(:,:)` 각 식생타입 항력계수
- `E_VEG(:,:)` Young's modulus (굽힘)
- `VEG_MASSDENS(:,:)` 질량밀도
- `VEGHMIXCOEF(:,:)` 식생경계 점성계수

`CD_VEG`는 `read_VegPar`에서 KEYWORD `'CD_VEG'`로 읽어 `CD_VEG(iveg,ng)=Rveg(iveg,ng)` 배정 (`vegetation_inp.h:74-78`), 출력 echo는 `vegetation_inp.h:442-445`.

## 3. 식생 항력 (vegetation_drag.F)

진입점 `vegetation_drag_cal` → `vegetation_drag_tile` (`vegetation_drag.F:46,94`). `rhs3d.F`가 매 스텝 `CALL vegetation_drag_cal(ng,tile)` 호출 (`Nonlinear/rhs3d.F:131`, 주석 "Add the effect of vegetation on the momentum terms." `rhs3d.F:128`).

### 3.1 강성 식생 (기본)

`VEG_FLEX` 미정의 시 유효 식물높이 = 실제 높이 (`vegetation_drag.F:281`):
```
plant_height_eff = plant(i,j,iveg,isHght)
```

캐노피 층 점유율 `Lveg_loc` — 격자셀이 캐노피 안에 전부/부분 들어가는지 (`vegetation_drag.F:284-289`):
$$\mathrm{dab}_k=\mathrm{dab}_{k-1}+H_{z,k},\quad L_{veg,loc}=\min\!\big(1-\min((\mathrm{dab}_k-h_{eff})/H_{z,k},\,1),\,1\big)$$

항력 항 준비 (rho-points, `vegetation_drag.F:293-294`):
$$\mathrm{wrk}=\tfrac12\,C_{d,veg}\cdot d_{veg}\cdot n_{veg}\cdot H_{z,k}\cdot L_{veg,loc}$$
여기서 `cd_veg`=항력계수, `isDiam`=직경 d, `isDens`=개체밀도 n.

면(face)에서 마찰력 — quadratic drag $|\mathbf{u}|\,u$ (`vegetation_drag.F:320-326`):
$$ru_{loc,veg}=\tfrac12(\mathrm{wrk}_{i-1,j}+\mathrm{wrk}_{i,j})\cdot u\sqrt{u^2+\bar v^2}$$
v-성분 대칭 (`vegetation_drag.F:348-354`). 여러 식생타입은 단순 합산 `ru_veg=ru_loc_veg+ru_veg` (`vegetation_drag.F:333`), 주석에 "not confident in what is happening when multiple vegetation types are concomitant" (`vegetation_drag.F:330-331`).

### 3.2 유연 식생 — Luhar & Nepf (2011) reconfiguration

`VEG_FLEX` 정의 시 흐름유발 자세 변화로 유효 길이를 줄임. 참조: "Luhar M., and H. M. Nepf, 2011: Flow-induced reconfiguration of buoyant and flexible aquatic vegetation" (`vegetation_drag.F:18-20`).

단면 2차모멘트 (`vegetation_drag.F:226-227`):
$$I=\tfrac{1}{12}\,d\cdot b^3 \quad (b=\text{isThck})$$

부력 파라미터 B (`vegetation_drag.F:236-239`):
$$B=\frac{(\rho_w-\rho_{veg})\,g\,d\,b\,l^3}{E\,I}$$

Cauchy 수 Ca (`vegetation_drag.F:249-250`):
$$\mathrm{Ca}=\frac{\tfrac12\rho_w\,C_d\,d\,U^2\,l^3}{E\,I}$$
($U$=rho-point 유속 크기, `vegetation_drag.F:243-245`).

reconfiguration 계수 cflex (`vegetation_drag.F:254-268`):
$$c_{flex}=1-\frac{1-0.9\,\mathrm{Ca}^{-1/3}}{1+\mathrm{Ca}^{-3/2}\,(8+B^{3/2})},\quad c_{flex}\le 1$$
주석 "set a minimum for cflex to be 1, cflex will exceed 1 if Ca<0.7290 but don't allow those values" (`vegetation_drag.F:264-265`). 유효높이 $h_{eff}=c_{flex}\cdot l$ (`vegetation_drag.F:272`), 굽힘각 $\theta=\arccos(c_{flex}^{1/3})$ (deg) (`vegetation_drag.F:276`).

### 3.3 momentum RHS 결합 (3D & 2D)

3D: `rhs3d.F`에서 ru에서 빼줌 (`Nonlinear/rhs3d.F:541-542`):
```
cff=ru_veg(i,j,k)*om_u(i,j)*on_u(i,j)
ru(i,j,k,nrhs)=ru(i,j,k,nrhs)-cff
```
진단 `DiaRU(...,M3fveg)=-cff` (`rhs3d.F:543-545`).

2D: 3D 항력을 연직적분해 `step2d_uveg`(=Σ_k 0.5(Hz_{i-1}+Hz_i)·ru_veg) 생성 (`vegetation_drag.F:430-440`, 주석 "Add in resistance imposed on the flow by the vegetation (3D->2D). Changes feedback in Nonlinear/step2d_LF_AM3.F" `vegetation_drag.F:425-427`). 적용은 `step2d_LF_AM3.h:2218-2222`:
```
fac=step2d_uveg(i,j)*cff3*om_u(i,j)*on_u(i,j)
rhs_ubar(i,j)=rhs_ubar(i,j)-fac
```
진단 `DiaU2rhs(...,M2fveg)=-fac` (`step2d_LF_AM3.h:2223-2225`), 주석 "Add in resistance imposed on the flow by the seagrass (3D->2D)" (`step2d_LF_AM3.h:2215`).

`WET_DRY` 시 항력 제한 — 운동량 방향 반전 방지, $0.75/\Delta t$ 계수 (bottom stress와 동일), "It only should slow down to zero. The value of 0.75 is arbitrary" (`vegetation_drag.F:186-193`, 적용 `vegetation_drag.F:336-341`).

## 4. 식생 유발 난류 (vegetation_turb.F)

진입 `vegetation_turb` → `vegetation_turb_tile` (`vegetation_turb.F:43,86`). GLS(generic length scale) 연직혼합에 식생 TKE/length-scale 기여를 더함. 헤더: "computes the turbulent kinetic energy and length scale modifications due to vegetation for gls_corstep.F" (`vegetation_turb.F:13-14`). 참조: Uittenbogaard (2003) + Warner et al. (2005) (`vegetation_turb.F:18-25`).

식생이 유체에 한 일 = 추가 TKE 생성 (m³/s³, `vegetation_turb.F:181-196`): ru_loc_veg·u, rv_loc_veg·v 의 셀당 평균을 합해 `tke_loc_veg=√(wrku²+wrkv²)`.

GLS 소산 (Warner et al. 2005 Eq.12, `vegetation_turb.F:201-204`):
$$\varepsilon=(c_\mu^0)^{3+p/n}\,k^{1.5+m/n}\,\psi^{-1/n}$$
($p,m,n$=`gls_p/m/n`, `vegetation_turb.F:172-174`). 자유난류 소산시간 `taufree=k/ε` (`vegetation_turb.F:211`).

식생 solidity 와 식물 간 에디 크기 L (`vegetation_turb.F:224-233`):
$$\text{solid}=d\cdot b\cdot n,\quad L=c_{l,veg}\Big(\frac{1-\min(\text{solid},1)}{n}\Big)^{1/2}$$
($c_{l,veg}=1$, `vegetation_turb.F:142`). 식물간 에디 소산시간 (`vegetation_turb.F:237-238`):
$$\tau_{veg}=\Big(\frac{L^2}{c_k^2\,\text{tke}_{loc,veg}}\Big)^{1/3}\quad (c_k=0.09)$$
유효 소산시간 $\tau_{eff}=\min(\tau_{free},\tau_{veg})$ (`vegetation_turb.F:243`), 식생 length-scale 기여 `gls_loc_veg=gls_c2·tke_loc_veg/taueff` (`vegetation_turb.F:244`). 모든 타입 합산 → `tke_veg`/`gls_veg` (`vegetation_turb.F:250-251`).

## 5. 파 streaming (vegetation_stream.F)

진입 `vegetation_stream_cal` → `vegetation_stream_tile` (`vegetation_stream.F:32,70`). 헤더: "Calculates the effect of changes in current on waves due to the presence of vegetation" (`vegetation_stream.F:13-14`). `VEG_SWAN_COUPLING && VEG_STREAMING` 시 SWAN의 식생 파 dissipation `dissip_veg`를 흐름방향 body force로 변환.

파수/내재진동수 (`vegetation_stream.F:139-144`):
$$k=2\pi/\max(L_{wave},1),\quad \sigma=\min\!\big(\sqrt{gk\tanh(kD)},\,2\big)$$
파향 성분 `cff1=1.5π−Dwave−angler` (`vegetation_stream.F:140-142`).

streaming body force (X/Y, `vegetation_stream.F:151-154`):
$$\mathrm{BWDXL}_{veg}=\frac{\varepsilon_{veg}}{\sigma}\,L_{veg}\,k_x,\quad \mathrm{BWDYL}_{veg}=\frac{\varepsilon_{veg}}{\sigma}\,L_{veg}\,k_y$$
($\varepsilon_{veg}$=`dissip_veg`, $L_{veg}$=캐노피 점유율). 주석 "Lveg is for 1 veg type only" 및 "check if we need a local dissip_veg here" (`vegetation_stream.F:146-149`) — 다중타입 한계 명시. 이는 WEC([[roms_wec]]) 파-흐름 결합과 연계되는 식생항이다.

## 6. 마쉬 가장자리 파 thrust (marsh_wave_thrust.F) — 항력 관련 발췌

`MARSH_DYNAMICS && MARSH_WAVE_THRUST` 시 인접 수셀의 파 climate로부터 마쉬 edge 측면 thrust 계산 (`marsh_wave_thrust.F:13-16`). 참조: Dean & Dalrymple (1991), Tonelli/Fagherazzi/Petti (2010) (`marsh_wave_thrust.F:20-25`).

방사응력류 thrust (`marsh_wave_thrust.F:289-294`): 분산관계 적분항 `Integral_kp=sinh(kw·D)/(kw·cosh(kw·h))`, `F_asl=½·ρ0·g·Hwave·N_kN·Hwave`, `F_bsl=ρ0·g·Hwave·N_kN·Integral_kp`. xi/eta 면 thrust는 마쉬 마스크·force 부호 조합으로 방향 선택 (`marsh_wave_thrust.F:313-324, 349-360`) 후 수심 감쇠 `cff8=exp(-depth_all·3)` 적용 (`marsh_wave_thrust.F:332-341`). 총 thrust = 4면 절댓값 합 × marsh_mask (`marsh_wave_thrust.F:408-410`). 마쉬 침식/수직성장으로의 결합은 별도 `marsh_sed_erosion.F`·`marsh_vert_growth.F` 영역.

## 7. 입출력·결합 요약

- 항력 호출: `rhs3d.F:131` (3D RHS), 결과 적용 `rhs3d.F:541-542`(3D)·`step2d_LF_AM3.h:2221-2222`(2D). use 선언 `step2d_LF_AM3.h:42-43`.
- 진단 항: 3D `M3fveg`, 2D `M2fveg` (`DIAGNOSTICS_UV`).
- NetCDF metadata index: `idWdvg`(파 dissipation), `idCdvg`(spectral Cd) 등 `vegetation_var.h:39-44`, `vegetation_mod.h:150-160`.
- ⚠ 다중 식생타입 동시 존재 시 항력·streaming의 정확성에 대해 코드 주석이 명시적으로 불확실성 표명 (`vegetation_drag.F:330-331`, `vegetation_stream.F:148`) — source-needed 검증 대상.

## 8. 핵심 참조 (코드 인용 논문)

- Beudin, Kalra, Ganju, Warner (2017): coupled wave-flow-vegetation model, Comp. & Geosci. 100, 76-86 (`vegetation_mod.h:129-132`).
- Kalra et al. (2021): 3-D coupled wave-flow-sediment marsh model, Front. Mar. Sci. 8 (`vegetation_mod.h:134-137`).
- Luhar & Nepf (2011): flexible vegetation reconfiguration (`vegetation_drag.F:18-20`).
- Uittenbogaard (2003) + Warner et al. (2005): 식생 난류 (`vegetation_turb.F:18-25`).
- Tonelli et al. (2010), Dean & Dalrymple (1991): 마쉬 wave thrust (`marsh_wave_thrust.F:20-25`).
