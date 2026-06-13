---
title: "FUNWAVE-TVD 전수분석 — 쇄파·조파·sponge·소스항·wet/dry"
model: FUNWAVE
citation_status: verified
verification_method: "src/breaker.F·wavemaker.F·sponge.F·sources.F·mixing.F·masks.F 전수 read (서브에이전트, 2026-06-13). file:line src 기준."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
---

# FUNWAVE-TVD 물리 source/sink

> 쇄파·조파(17 wavemaker subr)·흡수경계·운동량 소스항·범람. 정온도 적용 시 wavemaker(WK_DATA2D=SWAN nesting) 핵심.

## 1. 쇄파 breaker.F
- `WAVE_BREAKING`(:60): 디스패처 (SHOW_BREAKING→BREAKING, WAVEMAKER_VIS→VISCOSITY_WMAKER). shock-capturing 모드선 시각화용
- `BREAKING`(:87): **Kennedy eddy viscosity** 쇄파. 임계 `tmp1=Cbrk1√(gh)`(개시~0.45)·`tmp2=Cbrk2√(gh)`(지속~0.35), AGE 추적(ETAt≥tmp1→개시), nu_break 3방식(VIS_KENNEDY 기본 `nu=h·tmp2(1+B)+nu_bkg`, B=ETAt/tmp1−1 / ORIGINAL / STATIC_TRANS). Roller flux(Schäffer 1993) `R=min(0.45ETAt/C,0.1638)`, UNDERTOW

## 2. 조파 wavemaker.F (17 subr) — 핵심
`WAVEMAKER_INITIALIZATION`(:55) 마스터 디스패처. Wei-Kirby(1999) 내부조파 소스함수 `D_gen=2A·cosθ(ω²−α₁gk⁴h³)/(ωk·rI(1−α(kh)²))`, gaussian 폭 `beta_gen=80/δ²/L²`.

| 옵션 | subr | 입력 |
|---|---|---|
| WK_REG | `WK_WAVEMAKER_REGULAR_WAVE`(:2369) | Tperiod·AMP_WK·Theta_WK |
| WK_IRR/TMA/JON | `WK_WAVEMAKER_IRREGULAR_WAVE`(:1835) | Hmo·fm·방향분산(Borgman wrapped-normal), 등에너지 분할 |
| (등Δf) | `WK_EQUAL_DFREQ_IRREGULAR_WAVE`(:2128) | df 균등 |
| **WK_DATA2D** | `WK_WAVEMAKER_2D_SPECTRAL_DATA`(:627) | **2D 방향스펙트럼**(NumFreq×NumDir) ← SWAN nesting |
| WK_NEW_DATA2D/IRR | `WK_NEW_*`(:2636/:2813) | Salatin 2021, coherence(`WAVE_COHERENCE`:3184) |
| WK_TIME | `WK_WAVEMAKER_TIME_SERIES`(:2417) | 시계열(T,A,phase) |
| LEFT_BC_IRR/ABS | `CALCULATE_DATA2D_Cm_Sm`(:903)/`CALCULATE_TMA_Cm_Sm`(:1192) | 경계 Cm/Sm 계수(분산관계 Newton) |
| INI_* | (samples.F) | 초기 hump/solitary |

- `CALCULATE_Cm_Sm`(:831): 공간 소스계수 `Cm=ΣD_gen·exp(−beta(x−Xc)²)·cos(rlamda·y+φ)` (x가우시안×y사인)
- `CalcPeriodicTheta`(:1053): PERIODIC 시 격자 이산파수에 방향 스냅
- `IRREGULAR_LEFT_BC`(:2560): 좌경계 ghost에 η,U,V 직접 부과
- `VISCOSITY_WMAKER`(:2484): wavemaker 영역 viscosity

## 3. 흡수경계 sponge.F (7 subr) — 3방식 (manual v2.2)
- `SPONGE_DAMPING`(:52): **Larsen-Dancy** `ETA=ETA/SPONGE` (SPONGE≥1, 경계로 갈수록 큼)
- `ABSORBING_GENERATING_BC`(:77): 흡수-발생(ABS) `Eta=Ein2D+(Eta−Ein2D)·SPONGE_TIDE_WEST` + 조석 중첩
- `CALCULATE_FRICTION_SPONGE`(:223): friction형 `CD=CDsponge·tanh(ri/10)` (4방향, sources.F서 −CD·U·|V|·Depth)
- `CALCULATE_DIFFUSION_SPONGE`(:405): viscous형 `nu=Csp·tanh(ri/10)`
- `CALCULATE_SPONGE`(:591)/`_MAKER`(:165): LD 계수 `Sponge=max(A_sp^(R_sp^(50i/(Iw−1))),1)`
- `CALCULATE_CD_BREAKWATER`(:778): 방파제 CD 원형분포(MPI scatter)

## 4. 운동량 소스항 SourceTerms (sources.F:56) — 합산 허브
운동량식 SourceX/Y에 모든 항 합산:
`SourceX = g·η/DX·(Depthx(I+1)−Depthx(I))` [수심구배압력] `+ FrcInsX`[마찰 −Cd·U·|V| 또는 Manning −(g·n²/H^(1/3))] `+ Gamma1·MASK9·H·`[Boussinesq 분산] `+ WaveMaker_Mass·U`[조파]. 조건부: FRICTION_SPONGE/BREAKWATER(−CD·U·|V|·Depth), WindForce(+RHO_AW·Cdw·WindU·|Wind|), Smagorinsky(nu_smg 전단발산), VISCOSITY_BREAKING(BreakSourceX HU확산), VESSEL(VesselPressureX), AirPressure(StormPressureX). WaveMaker_Mass: WK_REG `tanh(πt/Tr)D_gen·exp(−β(x−Xc)²)sin(rlamda·y−2πt/T)`, WK_IRR/DATA2D Σ성분.

## 5. 시간평균·범람 mixing.F·masks.F
- `MIXING_STUFF`(mixing.F:53)→`CALCULATE_MEAN`(:108): time≥STEADY_TIME 시 Umean·ETAmean·복사응력(Sxx=UUmean−WWmean+0.5g·ETA2mean 경도)·SigWaveHeight `Hsig=4.004√(ETA2mean)`·zero-upcrossing 파고
- `UPDATE_MASK`(masks.F:51): wet/dry. flooding(이웃 wet η>현재η) / drying(η<−Depth→Dmass 누적) / MASK9 9점곱(`MASK(I,J)·MASK(I±1,J±1)`) / 질량보존 `ETA−=Dmass/WetArea`(#CHECK_MASS_CONSERVATION)

## 6. 연결
- [`funwave-source-map.md`](funwave-source-map.md) · [`funwave-dispersion-solver.md`](funwave-dispersion-solver.md) · 조파↔정온도 [`../../../concepts/waves/06-model-application.md`](../../../concepts/waves/06-model-application.md)(WK_DATA2D=SWAN 2D스펙트럼 nesting)
