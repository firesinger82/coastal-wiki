---
title: "Delft3D-WAVE User Manual — 사용자 관점 설정·입력 reference (SWAN 래퍼)"
model: Delft3D
doc: Delft3D-WAVE_User_Manual.pdf
canonical_source: manual
citation_status: verified
verification_method: "Delft3D-WAVE_User_Manual.pdf pdftotext -layout 직접 추출 후 TOC(p.iii-vii) + 핵심 장 페이지 인용. §2.1.3 coupling(p.6)·§4.5 MDW data group 전체(p.18-52)·§7.3 physical background+지배방정식(p.114-119)·§5.1 running(p.55-58)·App.A.1 MDW keyword reference(p.133-138) 직접 인용. 표지 v4.07.01 rev.80779(p.표지) 확인. 페이지는 매뉴얼 logical page(총 196p, '... of 196' 러닝헤더) 기준."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/Delft3D/README.md
---

# Delft3D-WAVE User Manual — 사용자 관점 설정·입력 reference

> Delft3D-WAVE는 SWAN 3세대 위상평균 파랑모델을 Delft3D GUI/워크플로로 감싼 래퍼다. 입력은 단일 `.mdw`(Master Definition Wave) 파일이며, FLOW와 com-file을 통해 offline/online 양방향 결합한다. 이 노트는 **사용자 설정·입력·기본값** 관점(GUI data group, .mdw keyword, 실행)을 다룬다. SWAN 물리식 자체의 소스 분석은 [[delft3d_wave_swan_module]] 참조.

관련 기존 노트: [[delft3d-flow-user-manual]], [[delft3d-manuals-overview]], [[delft3d_flow_wave_coupling]], [[delft3d_wave_swan_module]](source). 본 노트는 SWAN 물리식 전개(§7.4 full source terms)는 source 노트에 위임하고 **GUI/keyword/기본값/지배방정식 개요**에 집중한다.

## 1. 문서 정체

| 항목 | 값 |
|---|---|
| 제목 | Delft3D-WAVE User Manual — Simulation of short-crested waves with SWAN (표지) |
| 버전 | 4.07.01, Revision 80779 (표지) |
| 발행일 | 3 May 2026 (표지) |
| 발행처 | Deltares, Boussinesqweg 1, 2629 HV Delft, NL (p.표지 verso) |
| 분량 | 208 PDF p / 매뉴얼 logical 196 p ('... of 196' 러닝헤더) |
| 상태 | DRAFT 워터마크 |

## 2. 전체 목차 (장별 페이지, TOC p.iii–vii)

| 장 | 제목 | p. |
|---|---|---|
| 1 | A guide to this manual | 1 |
| 2 | Introduction to Delft3D-WAVE (SWAN 개념·결합·적용분야) | 5 |
| 3 | Getting started (메인메뉴·WAVE 진입) | 9 |
| 4 | Graphical User Interface (**MDW data group 전체**) | 15 |
| 5 | Running and post-processing | 55 |
| 6 | Tutorials (Siu-Lam·Nested·Online-WAVE+morphology·FLOW-DD) | 66 |
| 7 | **Conceptual description (지배방정식·source terms·수치)** | 111 |
| — | References | 128 |
| A | Files of D-Waves (**.mdw + attribute 파일 포맷**) | 133 |
| B | Definition of SWAN wave variables | 179 |
| C | Example of MDW-file Siu-Lam | 182 |
| D | DATSEL data extraction utility | 184 |
| E | LINT Line Integration | 188 |
| F | KUBINT volume integration | 191 |

### 4장 GUI 세부 (data group = .mdw 구조, TOC p.iii–iv)
4.5 Data groups of MDW-file (p.18): Description(p.19) · Hydrodynamics(p.19) · Grids[Computational/Bathymetry/Spectral resolution/Nesting/Hydrodynamics](p.20–25) · Time frame(p.26) · Boundaries(p.29) · Obstacles(p.36) · Physical parameters[Constants/Wind/Processes/Various](p.38–44) · Numerical parameters(p.45) · Output curves(p.47) · Output parameters(p.48) · Additional parameters(p.52).

### 7장 개념 (TOC p.v–vi)
7.2 General background(p.111) · 7.3 Physical background of SWAN[action balance·obstacle·set-up·diffraction](p.114–119) · 7.4 Full expressions for source terms[wind·dissipation·nonlinear](p.119–125) · 7.5 Numerical implementation(p.125).

## 3. SWAN↔Delft3D 결합 유형 (§2.1.3, p.6)

WAVE 계산은 flow가 wave에 미치는 영향(set-up·current refraction·enhanced bottom friction)과 wave가 flow에 미치는 영향(forcing·enhanced turbulence·enhanced bed shear stress)을 다음 4방식으로 처리 (p.6):

1. **user-defined flow** — wave condition별 공간 균일 수위·유속 지정 (flow→wave 단방향).
2. **offline coupling** — 완료된 FLOW 계산 결과(com-file) 사용 (flow→wave).
3. **online coupling** — FLOW 모듈과 동적 양방향 상호작용 (wave↔current 둘 다).
4. flow 영향 무시 (순수 WAVE).

offline(2)·online(3) 모두 **communication file(com-file)** 로 데이터 교환 (p.6). WAVE 결과(에너지 소산율 기반 또는 radiation stress 기반 wave force, orbital bottom velocity)는 Delft3D-FLOW(wave driven current·enhanced turbulence·bed shear stress)와 FLOW 3DMOR(stirring by wave breaking)에 입력됨 (§2.5, p.7).

표준 물리: refraction(가변수심/유속)·shoaling·wind generation·whitecapping·depth-induced breaking·bottom friction(3종)·nonlinear quad+triad·wave blocking by flow·obstacle transmission/blockage/reflection·diffraction (§2.3, p.6–7).

## 4. 지배방정식 (§7.3, p.114–119)

### 4.1 작용 균형 방정식 (§7.3.1, p.114)
SWAN은 **작용밀도 스펙트럼** $N(\sigma,\theta)=E(\sigma,\theta)/\sigma$ 를 사용 (유속 존재 시 energy density는 보존 안 되나 action density는 보존, Whitham 1974) (p.114). 직교좌표 작용 균형식 (식 7.1, p.114):

$$\frac{\partial}{\partial t}N + \frac{\partial}{\partial x}c_x N + \frac{\partial}{\partial y}c_y N + \frac{\partial}{\partial \sigma}c_\sigma N + \frac{\partial}{\partial \theta}c_\theta N = \frac{S}{\sigma}$$

좌변: 시간변화 + 지리공간 전파($c_x,c_y$) + 수심·유속에 의한 주파수 천이($c_\sigma$) + 수심·유속 굴절($c_\theta$). 전파속도는 선형파 이론(Whitham 1974, Mei 1983, Dingemans 1997). 우변 $S=S_{in}+S_{ds}+S_{nl}$ (생성·소산·비선형) (p.114–115).

### 4.2 source term 개요 (§7.3.1, p.115–117)
- **Wind input** (식 7.2): $S_{in}(\sigma,\theta)=A+BE(\sigma,\theta)$ — 선형(Phillips 1957 resonance)+지수(Miles 1957 feedback) 성장. $A$=Cavaleri & Malanotte-Rizzoli(1981)+PM 필터(Tolman 1992a). $B$ 두 옵션: WAM Cycle 3(Snyder et al.1981, Komen et al.1984 $U_*$ 재척도, Wu 1982 drag) / WAM Cycle 4(Janssen 1991a) (p.115).
- **Whitecapping** (식 7.3): $S_{ds,w}=-\Gamma\tilde\sigma\frac{k}{\tilde k}E$ — WAMDI(1988) pulse-based, $\Gamma$=steepness 의존, Komen et al.(1984) 보정. 대안: Van der Westhuysen(2007) saturation-based (식 7.4–7.5, $B_r=1.75\times10^{-3}$, $C'_{ds}=5.0\times10^{-5}$) (p.116).
- **Bottom friction** (식 7.6): $S_{ds,b}=-C_{bottom}\frac{\sigma^2}{g^2\sinh^2(kd)}E$ — JONSWAP(Hasselmann et al.1973)·Collins(1972) drag·Madsen et al.(1988) eddy-viscosity 3종 구현. 평균류의 bottom friction 소산 효과는 미반영(Tolman 1992b) (p.116).
- **Depth-induced breaking** (식 7.7): $S_{ds,br}=-\frac{D_{tot}}{E_{tot}}E$ — Battjes & Janssen(1978) bore model의 spectral 버전(Eldeberky & Battjes 1995). 파괴 파라미터 **$\gamma=H_{max}/d$, Delft3D-WAVE 기본값 $\gamma=0.73$**(Battjes & Stive 1985 평균) (p.117).
- **Nonlinear interactions**: 심해 quadruplet → DIA(Hasselmann et al.1985); 천해 triad → LTA(Lumped Triad Approximation, Eldeberky & Battjes 1996) (p.117).

### 4.3 보조 물리 (§7.3.2–7.3.4)
- **Obstacle transmission** (식 7.8, p.118): Goda et al.(1967) $K_t=0.5\left[1-\sin\left(\frac{\pi}{2\alpha}\left(\frac{F}{H_i}+\beta\right)\right)\right]$, $F=h-d$=freeboard. $(\alpha,\beta)$ 형상별 (Seelig 1979): vertical thin wall (1.8, 0.1) / caisson (2.2, 0.4) / dam slope 1:3/2 (2.6, 0.15). diffraction은 obstacle 끝에서 미반영 (p.118).
- **Wave-induced set-up** (§7.3.3, p.119): 1D 식 7.9 $F_x+gd\frac{\partial\bar\eta}{\partial x}=0$; 2D 식 7.10 (divergence-free 근사, Dingemans et al.1987). 2D set-up module을 Delft3D-WAVE 내에서 활성화 가능 (p.119).
- **Diffraction** (§7.3.4, p.119): phase-decoupled refraction-diffraction 근사(Holthuijsen et al.1993), mild-slope 기반, phase 정보 생략 → coherent wave field 불가 (p.119).

(§7.4 full source term 전개식·계수 상세는 [[delft3d_wave_swan_module]]에 위임.)

## 5. MDW data group / 입력 설정 (4장)

### 5.1 Grids — Spectral resolution (§4.5.3.3, p.23–24)
| 파라미터 | 하한 | 상한 | 기본 | 단위 |
|---|---|---|---|---|
| Directional space | — | — | **Circle**(전방위) | — |
| Start direction | -360 | 360 | 0 | deg |
| End direction | -360 | 360 | 0 | deg |
| Number of directions | 4 | 500 | **36** | — |
| Lowest frequency | 0.0 | — | **0.05** | Hz |
| Highest frequency | 0.0 | — | **1** | Hz |
| Number of frequency bins | 4 | — | **24** | — |

- Circle: $\Delta\theta=360°/N_{dir}$; Sector: $\Delta\theta=(End-Start)/N_{dir}$ (p.23). 주파수는 대수분포(로그) (p.24). **Reflection 활성 시 directional space는 full 360° 필수** (p.23, p.37).

### 5.2 Nesting (§4.5.3.4, p.25)
조밀-coarse 다중 격자 한 run 내 지원. coarse 격자를 먼저 계산 → finer 격자의 경계조건으로 사용, 재귀 반복 가능. 첫 격자는 nesting 불가(Boundaries data group에서 경계조건 지정 필요), 자기 자신에 nesting 불가 (p.25).

### 5.3 Hydrodynamics (offline FLOW 결합, §4.5.2, p.19)
`Use hydrodynamic result from FLOW` 체크 → FLOW의 `.mdf`(Master Definition Flow) 선택. com-file이 작업 디렉토리에 있어야 함. 수심=bottom level − water level − correction (bottom 양의 방향 아래, water level 양의 방향 위) (p.19).

### 5.4 Boundaries (§4.5.5, p.29–35)
**첫(only first) 계산격자에만** 입사 경계조건 지정 (nested 격자는 부모로부터 획득). 최대 4면, 기본 0면 (p.29). 정의 절차: (1) Orientation/Grid coord/XY coord 선택 → (2) 방향 선택 → (3) Constant/Variable → (4) integral parameter or from-file (1D/2D 스펙트럼) → (5) 값 입력 (p.29).

- **Conditions**: Uniform(면 따라 일정) / Space-varying(코너 거리별 점에서 스펙트럼 보간) (p.31).
- **Parametric 입력 4파라미터**: Significant wave height, Wave period(Peak 선택 시 peak period / Mean 선택 시 mean period), Direction(Nautical/Cartesian), Directional spreading(Degrees=표준편차 or Cosine power=$m$) (p.32–33).
- **Spectral shape** (§4.5.5 Edit spectral space, p.34): **JONSWAP(default, Peak enh.factor 기본 3.3)** / Pierson-Moskowitz / Gauss(frequency width를 Hz 표준편차로 지정) (p.34).

### 5.5 Obstacles (§4.5.6, p.36–37)
sub-grid 선형 장애물(폴리라인). 해상도=계산격자 간격. type: **Sheet**(transmission coef 일정) / **Dam**(입사파+장애물 높이 의존) / **Reflections**(specular/diffuse, transmission과 병행 가능) (p.36).

| 파라미터 | 하한 | 상한 | 기본 | 단위 |
|---|---|---|---|---|
| Reflection | — | — | **No** | — |
| Reflection coefficient | 0.0 | 1.0 | **0.0** | — |
| Transmission coef (Sheet) | 0 | 1 | **1.0** | — |
| Height (Dam) | -100 | +100 | **0.0** | m |
| Alpha (Dam) | 1.8 | 2.6 | **2.6** | — |
| Beta (Dam) | 0.1 | 0.15 | **0.15** | — |

Sheet/Dam 각 최대 250개. transmission coef=0 → 완전 차단. Height는 reference level 기준(음수=submerged) (p.37). **Reflection은 spectral direction이 full 360°일 때만 계산** (p.37).

### 5.6 Constants (§4.5.7.1, p.39)
| 파라미터 | 하한 | 상한 | 기본 | 단위 |
|---|---|---|---|---|
| Gravity | 9.8 | 10. | **9.81** | m/s² |
| Water density | 950. | 1050. | **1025.** | kg/m³ |
| North (x축 대비) | -360 | 360 | **90** | deg |
| Minimum depth | — | — | **0.05** | m |

- **Convention** (p.39): Cartesian(+x축 반시계, 파/바람이 가는 방향) vs Nautical(북에서 시계방향 +180°, 파/바람이 오는 방향).
- **Wave set-up**: 활성 시 wave-induced set-up 계산해 수심에 가산. **standalone 또는 flow에서 set-up 미반영 시에만 사용** (p.39).
- **Forces**: wave force를 에너지 소산율 기반 또는 radiation stress gradient 기반으로 계산 선택 (p.39).

### 5.7 Wind (§4.5.7.2, p.40–41)
FLOW(online/offline) wind 사용 시 이 sub-group 비표시 (p.40).
| 파라미터 | 하한 | 상한 | 기본 | 단위 |
|---|---|---|---|---|
| Wind speed (10m) | 0.0 | 50.0 | **0.0** | m/s |
| Wind direction (10m) | -360.0 | 360.0 | **0.0** | deg |

공간변동 wind은 special feature(GUI 미지원, 파일로 지정, §A.2.10) (p.40). third-gen 모드 + wind speed>0 → Quadruplets 자동 활성 (p.41).

### 5.8 Processes — 물리과정 기본값 (§4.5.7.3, p.42–43) ★핵심
- **Generation mode**: 1st / 2nd / 3rd-gen / None. **기본 3rd generation** → wind input·quadruplet·whitecapping 활성, **triad·bottom friction·depth-induced breaking은 비활성** (p.42).
- **Depth-induced breaking**: B&J(Battjes & Janssen 1978) bore model, 상수 breaker parameter. 끄면 beach 근처 wave height 폭주(unwise) (p.42).
- **Triads (LTA)** (Eldeberky & Battjes 1996): $\alpha_{EB}$, Beta=max/mean freq 비 (p.42–43).
- **Bottom friction** 3종: JONSWAP(Hasselmann et al.1973) / Collins(1972) / Madsen et al.(1988) (p.42–43).
- **Diffraction**: phase-decoupled(Holthuijsen et al.1993). 정확 해석엔 $dx\approx L/10$ 격자 필요, 거친 격자는 불안정 — "use with care" (p.43).

| 파라미터 | 하한 | 상한 | 기본 | 단위 |
|---|---|---|---|---|
| Generation mode | — | — | **3rd generation** | — |
| Depth breaking Alfa | 0.1 | 10 | **1.0** (B&J) | — |
| Depth breaking Gamma ($H_m/d$) | 0.55 | 1.2 | **0.73** | — |
| Triad interactions | — | — | **inactive** | — |
| Triad Alfa | 0.001 | 10 | **0.10** | — |
| Triad Beta | 0.001 | 10 | **2.2** | — |
| Bottom friction | — | — | **JONSWAP** | — |
| Bottom friction coef | — | — | **0.067** (JONSWAP wind sea; swell=0.038) | m²/s³ |
| Bottom friction Collins coef | — | — | 0.015 | — |
| Bottom friction Madsen coef | — | — | 0.05 (roughness length) | m |
| Diffraction | — | — | **inactive** | — |
| Diffraction Smoothing coef | 0 | 1.0 | **0.2** | — |
| Diffraction Smoothing steps | 1 | 999 | **5** | — |
| Adapt propagation | — | — | **active** | — |

### 5.9 Various (§4.5.7.4, p.44)
Wind growth·Whitecapping·Quadruplets·Refraction·Frequency shift 수정 가능. **Whitecapping 2모델: Komen et al.(1984) / Van der Westhuysen(2007)** (p.44). 초기 run엔 default 권장. wind speed>0 + 3rd-gen → Quadruplets 자동 활성 (p.44).

### 5.10 Numerical parameters (§4.5.8, p.45–46)
| 파라미터 | 하한 | 상한 | 기본 | 의미 |
|---|---|---|---|---|
| Diffusion θ-space (CDD) | 0. | 1. | **0.5** | 0=central(정확,진동위험)·1=upwind(확산,gradient 강할 때) |
| Diffusion σ-space (CSS) | 0. | 1. | **0.5** | 동상 (frequency space) |
| Relative change | 0. | — | **0.02** | Hs/period 국소 상대변화 수렴기준 |
| Relative change w.r.t. mean (Hs·Tm01) | 0. | — | **0.02** | 모델평균 대비 상대변화 |
| Percentage of wet grid points | 0. | 100% | **98%** | 수렴기준 충족 wet point 비율 |
| Max. number of iterations | 1 | — | **15** | 최대 반복 |

수렴: (a) 국소 Hs 변화 < 기준 AND (b) 국소 mean period 변화 < 기준 이 (c) wet point의 98% 이상에서 충족 시 반복 종료 (p.45–46).

## 6. 실행 (§5.1, p.55–58)

- **Standalone** (§5.1.1, p.55) / **Online with FLOW** (§5.1.2, p.55): online 시 FLOW와 WAVE 입력 파일이 **동일 runid** 필요 (p.55). FLOW DomainDecomposition은 com-file 1개만 가능, mdw명=com명 일치 필요 (p.55의 remark 영역, p.55).
- **Command-line** (§5.1.5, p.58):
  ```
  wave.exe <mdw-file> [mode]
    mode 0 = stand-alone (default)
    mode 1 = with Delft3D-FLOW
    mode 2 = with Delft3D-FLOW + Water/Mud interaction
  ```
- **병렬**: SWAN parallel 버전 default(v3.28.10~), 전 코어 사용. `OMP_NUM_THREADS` 로 제한(Windows `swan.bat` line 8 / Linux `swan.sh` line 56) (§5.2 FAQ, p.58).
- **진단**: `swn-diag.*`(SWAN report), `*-diag.*`(에러) (p.56). warning≠0이어도 성공 가능 (p.56).
- **파일 크기**: wavm-file ≈ mxr×myr×20 bytes (p.57); com-file은 격자수·저장량(C2≈15)·timestep 의존 (p.57).

## 7. 출력 파라미터

### 7.1 wavm-*.dat (NEFIS map file, Table 5.1, p.59)
HSIGN(유의파고) · DIR(평균파향, +x축 반시계, 파 진행방향) · PDIR(peak) · PERIOD(에너지밀도 평균주기) · RTP(상대 peak period) · DEPTH · FLOW VELOCITY · TRANSPORT OF ENERGY(W/m) · DSPR · DISSIP(bottom friction+breaking 소산) · LEAK · QB(breaking 비율) · UBOT(저면 orbital velocity rms 최대값) · STEEPW · WLENGTH · TPS(smoothed peak period) · TM02 · TMM10 · DHSIGN · DRTM01 · SETUP(활성 시) · WAVE FORCE(FX,FY N/m²) · WIND(WINDU,WINDV) (p.59).

### 7.2 com-*.dat (FLOW grid 출력, Table 5.2, p.60)
"Output for FLOW grid" 선택 시 `wavtim` group 기록. **HRMS** · **TP**(peak period) · **DIR**(flow grid 상대, 반시계) · **DISS**(소산율 W/m²) · **FX, FY**(wave forcing N/m²) (p.60). → Delft3D-FLOW의 wave-induced flow 입력.

## 8. .mdw 파일 keyword reference (Appendix A.1, p.133–138) ★

`.mdw`는 group/keyword 구조 NEFIS-free 텍스트. App.A.1 keyword table 발췌 (Format: R=Real, I=Integer, L=Logical, C=Character; `+`=WAVE-GUI 미지원, `*`=복수 지정 가능):

### General (p.133–134)
| keyword | format | 의미·기본값 |
|---|---|---|
| `SimMode` | key-value | stationary / quasi-stationary / non-stationary |
| `TimeStep` | 1R | 비정상 시 wave field 계산 간격(분) |
| `TimeInterval` | 1R | 비정상 SWAN instance 길이(분) |
| `FlowFile`+ | string | online FLOW mdf명 (비면 FLOW 미실행) |
| `FlowMudFile`+ | string | mud phase mdf명 |
| `FlowBedLevel` | 1I | 0=미사용·1=use don't extend·2=use and extend (default 0) |
| `FlowWaterLevel`/`FlowVelocity`/`FlowWind`/`FlowVegetation` | 1I | 위와 동일 의미 |
| `FlowVelocityType` | key-value | depth-averaged(default)/surface-layer/wave-dependent |
| `DirConvention` | key-value | nautical / cartesian |
| `ReferenceDate` | C*10 | YYYY-MM-DD |
| `ObstacleFile`/`TSeriesFile`/`MeteoFile`*+ | string | 부속 파일명 |

### Constants (p.134)
`Gravity` 1R (default 9.81) · `WaterDensity` 1R (default 1025) · `NorthDir` 1R (default 90°) · `MinimumDepth` 1R (default 0.05 m) · `WaterLevelCorrection` 1R.

### Processes (p.134–135) — 기본값 keyword 형태
| keyword | format | 기본값 |
|---|---|---|
| `GenModePhys` | 1I | 1/2/3 (gen mode) |
| `WaveSetup` | 1L | **false** |
| `Breaking` | 1L | **true** |
| `BreakAlpha` | 1R | **1.0** |
| `BreakGamma` | 1R | **0.73** |
| `Triads` | 1L | **false** |
| `TriadsAlpha` / `TriadsBeta` | 1R | 0.1 / 2.2 |
| `BedFriction` | string | none/jonswap/collins/madsen et al. (**default jonswap**) |
| `BedFricCoef` | 1R | **0.067**(jonswap)·0.015(collins)·0.05(madsen) |
| `Diffraction` | 1L | **true** |
| `DiffracCoef`/`DiffracSteps`/`DiffracProp` | 1R/1I/1L | 0.2 / 5 / true |
| `WindGrowth` | 1L | **true** |
| `WhiteCapping` | key-value | Off/Komen/Westhuysen (**default Komen**) |
| `Quadruplets` | 1L | **false** |
| `Refraction` | 1L | **true** |
| `FreqShift` | 1L | **true** |
| `WaveForces` | key-value | dissipation 3d(default)/dissipation/radiation stresses |

> ⚠ keyword 표(App.A.1, p.135)는 `Diffraction default: true`로 주석하나, GUI 표(§4.5.7.3, p.43)는 Diffraction "inactive"이고 예시 .mdw(Appendix C Siu-Lam, p.182)도 `Diffraction = false`다. Triad도 keyword 표는 default false(p.135)=GUI inactive(p.42)로 일치하나 Diffraction은 keyword 주석이 GUI/예시와 불일치. 실제 GUI/예시 default 기준으론 Diffraction=inactive로 해석하는 것이 안전(keyword 표의 true 주석은 ⚠ 의심).

### Numerics (p.135)
`DirSpaceCDD` 1R (default 0.5) · `FreqSpaceCSS` 1R (default 0.5) · `DRelHinc` 1R (0.01) · `DAbsHinc` 1R (0.005) · `RChHsTm01` 1R (0.02) · `RChMeanHs` 1R (0.02) · `RChMeanTm01` 1R (0.02) · `PercWet` 1R (98%) · `MaxIter` 1I (15) (p.135).

### Output (p.135)
`TestOutputLevel` 1I (0) · `UseHotFile` 1L (false, hotstart 읽기/쓰기) · `MapWriteInterval` 1R (map 기록 분) · `WriteCOM` 1L (false) · `COMWriteInterval` 1R (com 기록 분) (p.135).

## 9. 부속 파일 (Appendix A.2, p.139–178) 개요

orthogonal curvilinear grid(A.2.2 p.140) · wave boundary 시계열(A.2.3 p.141) · obstacle file(A.2.4 p.141) · segment file(A.2.5 p.143) · depth file(A.2.6 p.144) · space-varying bottom friction(A.2.7 — **D-Waves 미구현**, p.145) · wave boundary conditions[wavecon.rid / BCW / md-vwac UNIBEST / TPAR](A.2.8 p.146–155) · spectral I/O file(A.2.9 p.156) · space-varying wind[SWAN grid/equidistant/curvilinear/Spiderweb](A.2.10 p.161–178).

## 10. 미커버 / source-needed

- §6 Tutorials(p.66–110): Siu-Lam 단계별·Nested·**Online-WAVE+morphology**(§6.4 p.91)·FLOW-DD+Online WAVE(§6.5 p.100) — 실습 절차이므로 `examples/`/coupling 노트 영역. 필요 시 별도 발췌.
- §7.4 full source term 전개식·§7.5 numerical propagation(p.119–127) — [[delft3d_wave_swan_module]](source)에 위임.
- Appendix B(SWAN 변수 정의, p.179)·D/E/F utility(DATSEL/LINT/KUBINT, p.184–192) — 본 노트 미발췌(필요 시 추가).
