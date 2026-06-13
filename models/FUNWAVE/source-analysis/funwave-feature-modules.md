---
title: "FUNWAVE-TVD 전수분석 — feature 모듈 11종 (강제력·물리옵션)"
model: FUNWAVE
citation_status: verified
verification_method: "src/mod_{sediment,tide,meteo,vessel,tracer,precipitation,subgrid,foam,foam_upwinding,bathy_correction,time_spectra}.F 전수 read (서브에이전트, 2026-06-13). file:line src 기준."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
---

# FUNWAVE-TVD feature 모듈 (강제력·물리옵션)

> 컴파일 FLAG로 켜는 선택 물리. 각 `*_INITIAL`(input.txt 읽기·할당) + `*_FORCING/계산`. 코어 흐름은 [`funwave-source-map.md`](funwave-source-map.md).

## 1. SEDIMENT (mod_sediment.F 1679, `-DSEDIMENT`)
부유사 이송+지형변화. `SEDIMENT_ADVECTION_DIFFUSION`(:990) 농도 이류-확산(TVD/upwind), `MORPHOLOGICAL_CHANGE`(:1519) Zb.
- Pickup(비점착, Cao 2004): `c_b=0.015((τ−τcr)/τcr)^1.5·Dstar^−0.3`, τcr=(s−1)g·D50·Shields_cr(0.055)
- 침강 WS(van Rijn): `√((s−1)gD50)(√(2/3+36ν²/...)−√(36ν²/...))`
- 퇴적(Cao): `D=γ·CH·WS(1−γCH)²`; 소류사(Meyer-Peter): `8(τ−τcr)^1.5/g/(s−1)`; 지형 `Zb=−(suspend+bed)/(1−n)`; avalanche(slope>Tan_phi)
- 입력: D50·Sdensity(2.68)·n_porosity(0.47)·Shields_cr·BedLoad·Avalanche·Morph_factor·Cohesive...

## 2. TIDE (mod_tide.F 1082, 가드없음)
조석/해일 경계강제 4방향. `TIDE_BC`(:315) `ETA=ETA_tide+(ETA−ETA_tide)·SPONGE`. CONSTANT(`Tide_READ_CONSTANT`:373) 또는 DATA(시계열 `TIDE_DATA`:851 선형보간). sponge `1/max(A_sp^(R_sp^(50i/(Iw−1))),1)`(A_sp=10,R_sp=0.85). 모드: TIDAL_BC_ABS / TIDAL_BC_GEN_ABS. 입력: Tide{West/East/South/North}_{ETA/U/V} 또는 파일.

## 3. METEO (mod_meteo.F 1199, `-DMETEO`)
바람·기압 강제력 4기능. `METEO_FORCING`(:352).
- **Holland 태풍**: 기압 `Pw=Pc+(Pn−Pc)exp(−A/R^B)`, 풍속 `Vw=√(AB·100|Pn−Pc|exp(−A/R^B)/ρair/R^B)`, 기압경사 `StormPressureX=−gH(Pw(i+1)−Pw(i-1))/2dx`
- 상수바람(`Constant_Wind_Forcing`), 가우시안기압 `P=dP·exp(−(a(x−x0)²+2b..+c(y−y0)²))`, 산사태(sech분포)
- 바람응력 `τx=ρair·Cdw·|W|·Wu`(Cdw 0.002), 풍파상호작용(Chen 2004). 입력: WindHollandModel·STORM_FILE·Cdw...

## 4. VESSEL (mod_vessel.F 961, `-DVESSEL`)
선박 항주파(다중 NumVessel). `VESSEL_FORCING`(:458). 소스 3종: PR(기압 `VesselPressureX=−gH·dP/dx`)/SL(slender-body flux gradient)/PA(Green panel). Type1(cosine bell)/Type2(Divid-Volker 2017 `P=Pv(1−cl(L/Lng)⁴)(1−cb(W/Wd)²)exp`). 프로펠러유속(#PROPELLER), 심흘수(#DEEP_DRAFT). 입력: VESSEL_FOLDER/vessel_NNNNN(경로시계열).

## 5. TRACER (mod_tracer.F 581, `-DTRACKING`)
Lagrangian 입자추적. `TRACK_XY`(:372)→`MOVE_TRACER`(:505) 삼각형 barycentric 보간 `U_tracer=ΣSi·U(ni)/Sc`, 이류 `X+=U·DT`(전진 Euler). layer 0(수심평균)/1(표층)/2(저층). 입력: TRACER_FILE(X0,Y0,StartTime,Layer).

## 6. PRECIPITATION (mod_precipitation.F 349, `-DPRECIPITATION`)
강수 수위소스. `PRECIPITATION_DISTRIBUTION`(:240) 시간보간+쌍선형 공간보간, mm/hr→m/s(×2.78e-7). 연속식 질량소스(sources.F). 입력: RAINFALL_FILE(시계열 격자).

## 7. SUBGRID (mod_subgrid.F 449, `-DSUBGRID`)
부격자 지형 공극률. `UPDATE_SUBGRID`(:193): 부격자 N² 픽셀 중 wet 비율 `Porosity=pcount/NumPixel`, 유효수심 `DepAvgSubgrid`. 입력: SubMainGridRatio·DEPTH_SUBGRID_FILE.

## 8. FOAM (mod_foam.F 542 / mod_foam_upwinding.F 561, `-DFOAM`)
쇄파 후 거품층(Reul-Chapron 2003). `FOAM_UPDATE`(:274): source `f_source·nu_break`, sink `EtaFoam/FoamTimeScale·exp(−AGE/τ)`, `EtaFoam−=dt·∇·M−SinkM·dt+SourceM·dt`. mod_foam=TVD+Cd 역학 / _upwinding=단순 upwind. 입력: f_source(0.05)·FoamTimeScale(3.8s).

## 9. BATHY_CORRECTION (mod_bathy_correction.F 294, 가드없음)
초기 급경사 평활화. `CORRECTION`(:77): max경사>SlopeCap(1.0)이면 `Depth1=0.4·Depth0+0.15(E+W+N+S)` 반복(수렴 5%). 입력: SlopeCap·SmoothBelowDepth.

## 10. TIME_SPECTRA (mod_time_spectra.F 539, 가드없음)
시간변화 2D 방향스펙트럼 경계생성(WaveMaker='TIME_SPECTRA', TIDAL_BC_GEN_ABS+DATA 필수). `CALCULATE_DATA2D_Cm_Sm_TIME`(:407) 분산관계 Newton `k(n+1)=k−(gk·tanh(kh)−σ²)/F'`, Cm/Sm `Σ Amp·cos(kx·X+ky·Y+φ)`. ABSORBING_GENERATING_BC 연동.

## 11. 요약
| 모듈 | FLAG | 핵심물리 |
|---|---|---|
| SEDIMENT | -DSEDIMENT | Cao2004 부유사·Meyer-Peter 소류사·지형변화 |
| TIDE | (always) | 조석/해일 4방향 경계강제 |
| METEO | -DMETEO | Holland태풍·바람·가우시안기압·산사태 |
| VESSEL | -DVESSEL | 선박 항주파(기압/slender/panel) |
| TRACER | -DTRACKING | Lagrangian 입자추적 |
| PRECIPITATION | -DPRECIPITATION | 강수 수위소스 |
| SUBGRID | -DSUBGRID | 부격자 공극률 유효수심 |
| FOAM | -DFOAM | 거품층 이류(Reul-Chapron) |
| BATHY_CORRECTION | (always) | 급경사 평활화 |
| TIME_SPECTRA | (always) | 시간변화 방향스펙트럼 경계 |

## 12. 연결
- [`funwave-code-graph.md`](funwave-code-graph.md)(USE: feature→GLOBAL/INPUT_READ) · [`funwave-source-map.md`](funwave-source-map.md)
