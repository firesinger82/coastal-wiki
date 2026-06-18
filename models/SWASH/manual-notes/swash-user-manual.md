---
title: "SWASH 사용자 매뉴얼(swashuse.pdf) 검수 — command/keyword reference + 기본값"
model: SWASH
doc: swashuse.pdf
canonical_source: manual
citation_status: verified
verification_method: "swashuse.pdf (swash/doc/swashuse.pdf, v12.01, 167p) pdftotext -layout 직접 추출(/tmp/swash-user-manual.txt 6842줄) 후 TOC(p.v-viii) + Ch2 General description(§2.2-2.4) + Ch4 command reference(SET/MODE/COORD/CGRID/VERTICAL/INPGRID/INITIAL/BOUND SHAPE/BOUNDCOND/WIND/FRICTION/VISCOSITY/POROSITY/VEGETATION/CORIOLIS/TRANSPORT/BREAKING/AMBIENT/NONHYDROSTATIC/DISCRETIZATION/BOTCEL/TIME INTEGRATION/QUANTITY/COMPUTE/STOP) + Ch5 setup guideline(dispersion table 5.1-5.2) 직접 인용. 명령 syntax·기본값·옵션 verbatim 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/SWASH/README.md
---

# SWASH 사용자 매뉴얼 (swashuse.pdf) 검수

> SWASH 공식 User Manual(v12.01, 167p)의 정체·TOC·command/keyword reference + 기본값 검수. 기술문서(물리·수치 이론)는 [[swash-tech-documentation-overview]], 입력 파싱 소스는 source-analysis 의 swash-input-parsing-check 와 대응. **본 노트는 사용자 입력 command 의 syntax·옵션·기본값 verbatim 레퍼런스에 집중.**

## 1. 문서 정체

- **제목/버전**: SWASH USER MANUAL, **SWASH version 12.01** (표지). 발행 The SWASH team, TU Delft Environmental Fluid Mechanics Section (표지).
- **저작권**: (c) 2010-2026 Delft University of Technology, GNU Free Documentation License v1.2 (표지 p.iv).
- **문서 3종 체계** (§1, p.1): ① **User Manual**(입력 사양 = 본 문서) ② Implementation Manual(설치·병렬 실행) ③ Scientific/Technical documentation(물리·수학·이산화 = [[swash-tech-documentation-overview]]).
- **읽기 순서 권장** (§1, p.1): 처음이면 Ch 2·3 → Ch 5(실습) → Ch 4(command reference, 가장 자주 참조).

## 2. TOC (장별 페이지, p.v-viii)

| Ch/App | 제목 | p |
|---|---|--:|
| 1 | About this manual | 1 |
| **2** | General description and instructions for use | 3 |
| 3 | Input and output files | 19 |
| **4** | **Description of commands** (핵심) | 21 |
| 5 | Setting up your own command file | 117 |
| A | Definitions of variables | 137 |
| B | Command syntax | 141 |
| C | File swash.edt (전체 command 목록) | 147 |
| — | Bibliography / Index | 157 / 159 |

Ch4 세부(§4.4 Start-up p.24 / §4.5 Model description p.28 / §4.6 Output p.93 / §4.7 Lock-up p.115).

## 3. 모델 개요·범위 (Ch 2)

- **정체** (§2.2.1, p.3): "general-purpose numerical tool for simulating non-hydrostatic, free-surface, rotational flows and transport phenomena in one, two or three dimensions." 지배방정식 = **비선형 천수방정식 + 비정수압 + transport 식**. 약어 SWASH = **S**imulating **WA**ves till **SH**ore (p.4).
- **수치 핵심** (§2.2.2, p.4-5): explicit 2차 staggered 유한차분, 이산레벨 mass·momentum 엄밀 보존 → 쇄파 위치 추적·bore 재현. 압력을 hydrostatic + non-hydrostatic 으로 분리(projection method), 시간적분은 2차 leapfrog 또는 θ-method semi-implicit. semi-implicit 은 leapfrog 대비 시간스텝 5~10배(p.5).
- **Boussinesq 모델과 차이** (§2.2.4, p.8): SWASH 는 Boussinesq 가 아님. 도함수 차수 증가 대신 **연직 layer 수 증가**로 dispersion 개선. 공간 도함수 최대 2차, 시·공간 모두 최대 2차 정확. 단파 불안정 제거용 수치 필터·surface roller·slot 기법 없음(p.8).
- **순환모델과 관계** (§2.2.5, p.9): WAQUA·Delft3D-FLOW·ADCIRC·ROMS·FVCOM·UNTRIM·SLIM·SUNTANS 와 유사하나 비정수압. v7.01 이후 unstructured 삼각망 지원.
- **물리현상** (§2.2.3, p.7-8): wave shoaling/refraction/diffraction, depth-limited wind growth, 비선형 wave-wave(surf beat·triad), breaking, runup/rundown, moving shoreline, bottom friction, partial reflection/transmission, 구조물·이동강체 상호작용, wave-current·wave-induced current, 연직 난류 혼합, subgrid 난류, 난류 비등방, vegetation damping, 급변류, tidal/bore/flood wave, 풍성류, 밀도류, 부유사 수송, turbidity flow, tracer 수송.
- **한계·내부 시나리오** (§2.3, p.9-10): SWASH 는 종료 대신 robust 한 내부 시나리오 invoke — (a) 수위가 bottom 아래면 drying/flooding 최소수심 조정, (b) Courant 기반 동적 시간스텝(PRINT 파일 기록), (c) 수평 eddy viscosity 명시적 처리 안정성 위해 매 스텝 최대 eddy viscosity 제한(불안정점 >1% 시 PRINT 경고). 근본적 한계(난류 모델링)·미발견 coding bug 존재 가능.
- **단위/좌표** (§2.4, p.10-11): 모든 입력 S.I. (m, kg, s, N, Pa). 방향·구면좌표는 도(°). Cartesian 또는 spherical.

## 4. Command 분류 (§4.1, p.21-23)

| 그룹 | command |
|---|---|
| (a) Start-up | PROJECT, SET, MODE, COORD |
| (b) 계산격자 | CGRID, READGRID, VERT |
| (c) 입력장 | INPGRID, READINP, INPTRAN, READTRA, INPAMBI, READAMB |
| (d) 초기·경계 | INITIAL, BOUND, SOURCE, SPONGE, FLOAT |
| (e) **물리** | WIND, FRIC, VISC, POROS, VEGET, CORI, TRANSP, BRE, AMB |
| (f) **수치** | NONHYD, DISCRET, BOTCEL, TIMEINT |
| (g) 출력위치 | FRAME, GROUP, CURVE, RAY, ISOLINE, POINTS |
| (h) 출력량 | QUANTITY, OUTPUT, BLOCK, TABLE, TEST |
| (i) Lock-up | COMPUTE, STOP |

## 5. Start-up command + 핵심 기본값 (§4.4)

### SET (§4.4, p.25-27) — 일반 파라미터
| keyword | 의미 | 기본값 |
|---|---|---|
| `[level]` | still water level (m) | 0. |
| `[nor]` | x축 대비 North 방향(반시계, °) | 90° |
| `[depmin]` | drying 임계수심 (m) | **0.00005** |
| `[maxmes]` | error 메시지 한계 | 200 |
| `[maxerr]` | 계산중단 error level (1 경고/2 error/3 severe) | 1 |
| `[seed]` | 난수 seed (Fourier 위상) | 12345678 |
| `[grav]` | g (m/s²) | 9.81 |
| `[rhowat]` | 물 밀도 (kg/m³) | 1000. |
| `[temp]` | 수온 (°C) | 14. |
| `[salinity]` | 염분 (ppt) | 31. |
| `[dynvis]` | 동점성 (kg/ms) | 0.001 |
| `[rhoair]` | 공기 밀도 | 1.205 |
| `[rhosed]` | 퇴적물 밀도 | 2650. |
| `[cdcap]` | 풍항력계수 최대값 (99999=무제한) | 99999. (제안 2.5e-3) |
| `[backvisc]` | 배경 점성 (m²/s) | 0. (제안 1e-4~1e-3) |
| `[kappa]` | Von Karman 상수 | 0.4 |
| 방향규약 | `NAUTical` / `CARTesian` | CARTESIAN |

### MODE (§4.4, p.27)
`MODE NONSTationary < TWODimensional | ONEDimensional >`. **NONSTATIONARY 필수.** 기본 = NONSTATIONARY TWODIMENSIONAL.

### COORDINATES (§4.4, p.27-28)
`CARTesian`(기본) / `SPHErical < CCM | QC >`. 구면시 regular grid 는 항상 E-W·N-S 정렬 필수(alpc=alpinp=alpfr=0), unstructured 미지원 (p.28).

## 6. 계산격자 (§4.5.1)

### CGRID (필수, §4.5.1, p.28-30)
`CGRID < REGular [xpc][ypc][alpc][xlenc][ylenc][mxc][myc] | CURVilinear [mxc][myc] (EXCeption [xexc][yexc]) | UNSTRUCtured > (REPeating < X | Y >)`
- `[mxc],[myc]` = **mesh 수 = 격자점 수 − 1**. 1D-mode 는 `[myc]=0`, `[ylenc]=0`.
- 기본값: `[xpc]=[ypc]=0.0`(Cartesian; 구면은 필수입력), `[alpc]=0.0`.
- CURVILINEAR 은 READGRID COOR, UNSTRUCTURED 는 READGRID UNSTRUC 로 좌표 제공(p.30-31).
- REPEATING: 한 방향 주기경계(한 끝 유출=반대 끝 유입), 기본 X. 1D·unstructured 불가.
- READGRID COOR 시 격자 각도 0~180° 검사, **45~135° 권장** (p.31).

### VERTICAL (선택, §4.5.1, p.32-33) — multi-layered mode
`VERTical [kmax] < [thickness] < M | -> PERC > >`
- layer 번호 = top(1) → bottom([kmax]). `[thickness]` 단위: M(고정 m) / **PERC(가변 %, 기본)**.
- 미지정 시 등간격 분포. PERC 합 = 100, **최소 1개 가변 layer 필수**. 모두 가변이면 sigma plane 과 동일.
- 단파 모의는 **가변 두께·등간격 권장**. 고정 layer 는 unstructured 미지원.

## 7. 입력장 (§4.5.2)

### INPGRID (§4.5.2, p.33-37)
`INPgrid (< BOTtom | WLEVel | CURrent|VX|VY | FRiction | WInd|WX|WY | PRessure | CORIolis | POROsity | PSIZe | HSTRUcture | NPLAnts | DRAFt | LABel >) < REGular [...] | CURVilinear STAGgered | UNSTRUCtured > (EXCeption [excval]) (NONSTATionary [tbeginp][deltinp] <Sec|MIn|HR> [tendinp])`
- READINP 가 뒤따라야 함(p.39). 옵션 FRICTION/WIND/POROSITY 등은 공간변동 입력장 정의용.

### INITIAL (§4.5.3, p.47)
`INITial < CONstant [wlev][vx][vy][tke][epsilon] | ZERO | STEAdy >`. CONSTANT 기본. STEADY 는 Chezy 정상류로 초기속도 도출(spin-up 단축).

## 8. 경계조건 (§4.5.3)

### BOUND SHAPESPEC (§4.5.3, p.47-48) — 스펙트럼 형상
`BOUnd SHAPespec < PM | -> JONswap [gamma] | TMA > < -> SIG | RMS > < -> PEAK | MEAN > DSPR < -> POWer | DEGRees >`
- 기본: **JONSWAP [gamma]=3.3**, 특성파고 SIG, 특성주기 PEAK, 방향폭 POWER (cosᵐθ 분포). TMA = 유한수심 보정 JONSWAP.

### BOUNDCOND (§4.5.3, p.48-58)
- 경계 미지정 시 = closed(법선속도 0) (p.50). SOURCE(내부 wave 생성)와 병용 불가.
- 위치: `SIDE < N|NW|W|SW|S|SE|E|NE >`(structured 직선변) 또는 `SEGMENT < XY [x][y] | IJ [i][j] >`(곡선·부분변).
- **BTYPE (경계조건 종류)**:
  - `WLEV` 수위 / `VEL` 법선속도 / `DISCH` 단위폭 유량
  - `RIEMANN` Riemann 불변량 $u \pm 2\sqrt{gh}$ (초임계류·hydraulic jump용)
  - `LRIEMANN` 선형화 Riemann $u \pm \zeta\sqrt{g/d}$ (ζ≪d 인 아임계 심해; 대륙붕·항만 조류)
  - `WEAKREFL` 약반사 경계
  - `SOMMERFELD` 방사조건(천해 near-linear 장파)
  - `OUTFLOW` 수심을 bottom 에 정렬(초임계 S2 배수곡선, structured 한정)
  - `LAYER [k]` / `LOGARITHMIC` 연직 분포 지정
- Fourier(REGULAR) 또는 time series(SPECTRUM) 로 추가 사양 제공.

## 9. 물리 command (§4.5.4) — reference + 기본값

### WIND (§4.5.4, p.65-68) — 풍항력
- drag formulation: `CONstant [cd]`(기본 0.002), `CHARNock [beta]`(0.032), `LINEAR`(cd=0.001([a1]+[b]U₁₀)), `WU`, `GARRATT`, `SMITHBANKE`, `FIT`(2차 다항).
- `[height]` 측정고도 기본 10 m. `RELATIVE [alpha]`(0<α≤1, 기본 1) = 물 상대속도. `RELWAVE [crest]`(0≤c≤1, 기본 **0.4**) = 파속 상대, 파 crest 에만 풍응력.

### FRICTION (§4.5.4, p.68-70) — 바닥마찰
미사용시 마찰 무시. **기본 = MANNING(공간균일)**.
| 옵션 | 의미 | 기본 [cf]/[h] |
|---|---|---|
| `CONstant [cf]` | 무차원 마찰계수 | 0.002 |
| `CHEZy [cf]` | Chezy (m^½/s) | 65. |
| `MANNing [cf]` | Manning (m^−⅓ s) | **0.019** |
| `COLEbrook [h]` | Colebrook-White = Nikuradse 조도고 (m) | — |
| `LOGlaw < SMOOTH | ROUGHness [h] >` | 대수벽법칙 | SMOOTH 기본 |
- Manning 이 surf zone 파 동역학 표현 우수(p.68). 공간변동시 INPGRID/READINP FRICTION 사용, FRICTION command 는 type 정의 위해 여전히 필요.

### VISCOSITY (§4.5.4, p.70-72) — 난류 혼합
`VISCosity < -> Horizontal < -> CONstant [visc] | SMAGorinsky [cs] | MIXing [lm] > | Vertical KEPS [cfk][cfe] | FULL KEPS < -> LINear | NONLinear > >`
- 기본 = **수평 등방 점성(constant)**. SMAGORINSKY `[cs]` 기본 0.2.
- VERTICAL KEPS = 표준 k-ε (Launder-Spalding 1974). vegetation 관련 상수 `[cfk]=0.07`, `[cfe]=0.16` (Shimizu-Tsujimoto 1994, structured 한정).
- FULL = 3D 난류(LINEAR=Boussinesq 가정 기본 / NONLINEAR=Speziale 1987 비선형 응력-변형), structured 한정.

### POROSITY (§4.5.4, p.72-73) — 다공질 구조물
`POROsity [size] [height] [alpha0] [beta0] [wper]`. **unstructured 불가.** VARANS 식·Van Gent(1995) 마찰식.
- `[height]` 기본 99999.(돌출 구조물), `[alpha0]`(층류 마찰) 기본 **200.**, `[beta0]`(난류 마찰) 기본 **1.1**, `[wper]` 특성파주기(파-구조물 상호작용 시 필수).

### VEGETATION (§4.5.4, p.73-74) — 식생 파 감쇠
`VEGEtation < [height][diamtr][nstems][drag] > INERtia [cm] POROsity Vertical`. **unstructured 불가.** Morison 식(수직 실린더 항력). 연직 segment 별 반복.
- `[nstems]` 기본 1(공간변동시 INPGRID/READINP NPLANTS). INERTIA `[cm]`=부가질량계수(=관성계수−1). POROSITY/VERTICAL 옵션.

### CORIOLIS (§4.5.4, p.74-75)
`CORIolis [fpar]`. Cartesian 은 SET [latitude] 위도 필요, spherical 은 위도서 자동계산. `[fpar]` 양수=북반구.

### TRANSPORT (§4.5.4, p.75-79) — 구성물 수송
- noncohesive(sand, 기본) `[size]`(µm) / cohesive(mud) `[tauce][taucd][erate][fall]`. fall velocity 미지정시 Rubey(1933) 식 자동 산정.
- `[snum]` Schmidt 수 기본 0.7. `[ak]`(Von Karman 보정) Adams-Weatherly(1981) 5.5. `DENSITY < YES(기본) | NO >`(혼합밀도 효과). `ANTICREEP < NONE(기본) | STANDARD | SVK >`(anti-creepage; Stelling-Van Kester, unstructured 불가).
- cohesive Partheniades-Krone 침식/퇴적 flux (식 본문 p.78).

### BREAKING (§4.5.4, p.79-80) — depth-limited 쇄파 제어
`BREaking [alpha] [beta]`. **연직 layer 수가 적을 때만** 사용(layer 10개+ 면 비활성 권장). bore 유사성으로 에너지 소산은 항상 자동 계산.
- 쇄파 개시: $\frac{\partial\zeta}{\partial t} > \alpha\sqrt{gh}$ 이면 해당 점 비정수압 압력 무시. `[alpha]` 기본 **0.6** (전면슬로프 ~25°, 캘리브레이션 불요).
- 지속: 이웃점이 hydrostatic 라벨이고 $\frac{\partial\zeta}{\partial t} > \beta\sqrt{gh}$ 면 유지. `[beta]` 기본 **0.3** (0<β<α).

### AMBIENT (§4.5.4, p.80-81)
`AMBient [U] [V] [eta]`. 공간균일 ambient current·평균수위. unstructured 불가. 공간변동시 INPAMB/READAMB.

## 10. 수치 command (§4.5.5) — reference + 기본값

### NONHYDROSTATIC (§4.5.5, p.81-85) — 비정수압 압력
미사용시 정수압 가정. (소스 대응: [[swash-nonhydrostatic-pressure-solver]])
- **연직 압력경사 스킴**: `STAndard`(중앙차분; 연직구조 중요·밀도류·undertow·급변바닥) vs `BOX`(Keller-box; **기본**, 단파 2~3 layer, 등간격 권장).
- `[theta]` θ-method (0.5=Crank-Nicolson, 1=implicit Euler). **범위 [0.5,1]만 허용**, 기본 **1.0**.
- `SUBGrid [pmax]`: 압력/속도 연직해상도 분리(structured 한정, pmax 기본 = kmax, 가압류 불가).
- `REDuced [qlay]`: Poisson rank 축소(BOX 병용 필수). reduced 2-layer(qlay=1)는 ~30% CPU 절감. `[qlay]` 기본 1.
- `SOLVer [rhsaccur] [initaccur] [maxiter] [relax]`: 정수압 = SIP(`[relax]` 기본 0.91), 다층 = ILUD-BiCGSTAB. `[rhsaccur]` 기본 **0.01**, `[initaccur]` 기본 0.0, `[maxiter]` 기본 **500**. 정지기준 $\|r_m\|_2/\|b\|_2 < \epsilon$; ε=0.01 최적.
- `PREConditioner < ILUD(기본) | ILU >` (structured 한정; ILU 가 robust — 고파·초단파·급경사·layer>20·가압류·unstructured 시).
- `PROJection ITERative [tol] [maxiter]`: Chorin(1968) 1차 projection(가압류·부유체) 또는 Van Kan(1986) 2차 pressure correction(기본). `[tol]` 기본 0.0001, `[maxiter]` 기본 50.
- **기본 요약**: BOX, theta=1.0, 2차 pressure correction, SIP(정수압)/ILUD-BiCGSTAB(다층).

### DISCRETIZATION (§4.5.5, p.85-89) — 공간 이산화
`DISCRETization < UPWind <UMOM MOMentum|HEAD <Horizontal|Vertical> | WMOM <H|V>> | CORRdep | TRANSPort <H|V> | ACURrent <Umom|Wmom> > < NONe | FIRstorder | HIGherorder [kappa] | LIMiter <SWEBy [phi]|RKAPpa [kappa]|PLKAPpa [kappa][mbound]> | FROmm | BDF|LUDs(기본) | QUIck | CUI | MINMod | SUPerbee | VANLeer | MUScl | KORen | SMArt >`
- κ-formulation (−1≤κ≤1): BDF(κ=−1), QUICK(κ=½), CUI(κ=⅓, 3차정확), Fromm(κ=0), 중앙차분(κ=1).
- 기본: **수평 advective = BDF**(2차 후방 upwind), **CORRDEP = MUSCL**. transport(salinity/temp/sediment)는 TVD 필수(음수 농도 방지).
- unstructured = Casulli-Zanolli(2005) r-ratio.

### BOTCEL (§4.5.5, p.89-90) — cell center bottom level
`BOTCel < MIN | -> MEAN | MAX | SHIFt >`. unstructured 불가. 기본 **MEAN**. 급경사·tidal flat·수직벽 overtopping 정확도 위해 MIN(tiled bottom) 등 사용. 하향양수 기준(MIN=최천 bottom).

### TIME INTEGRATION (§4.5.5, p.90-93)
`TIMEI METH < EXPL [cfllow][cflhig] | IMPL [thetac][thetas] SOLVer [tol][maxiter][weight] NEWTon > VERTical [thetau][thetaw][thetat]`
- **EXPLICIT**: structured 기본. 장파속도 Courant 제한. 고파·비선형·급경사 구조물은 **최대 Courant 0.5 권장**. 자동 시간스텝: Courant > `[cflhig]` 면 반감, < `[cfllow]` 면 배증. 기본 `[cfllow]=0.4`, `[cflhig]=0.8`.
- **IMPLICIT**(semi-implicit): unstructured 기본. 수위경사·발산 θ-method 음해 → 장파속도 무관 무조건안정(시간스텝 5~10배). 수평 advective 명시적. `[thetac]`(연속식) 기본 0.5, `[thetas]`(수위경사) 기본 0.5. PCG solver. `NEWTon` = 수심 비음수 강제(Casulli 2009), 부유체 가압류는 semi-implicit 필수.
- 다층 mode 는 연직 advective·점성항 θ-method 음해.

## 11. 출력 (§4.6)

- **출력위치** (§4.6.1, p.94-98): FRAME(regular grid)·GROUP·CURVE·RAY·ISOLINE·POINTS.
- **QUANTITY/BLOCK/TABLE** (§4.6.2, p.98-114): 주요 출력량(verbatim, Appendix A p.107-111) —
  - 스칼라/벡터: `WATLEV`(수위 m), `DEP`(수심), `VEL/VMAG/VDIR`(속도), `VKSI/VETA`(격자정렬 U/V), `PRESS`(바닥압 hPa), `NHPRES`(정규화 비정수압 m²/s²), `DISCH/QMAG`(단위폭 유량 m²/s), `VORT`(와도), `WIND/WMAG/WDIR`, `FRC`, `USTAR/UFRIC`(마찰속도), `SAL/TEMP/SED`.
  - 파 관련: `HSIG`(유의파고), `HRMS`(RMS 파고), `SETUP`(wave setup), `HRUN`(runup mask), `BRKP`(breaking mask).
  - layer별(`...K` 접미): `ZK`(layer 계면), `HK`(layer 두께), `VELK`, `VZ`(연직속도), `VOMEGA`(sigma 상대 연직속도), `TKE`, `EPS`, `VISC`(연직 eddy viscosity), `NHPRSK`.
  - 시간평균(`M...` 접두): `MVEL`, `MSAL`, `MTEMP`, `MSED` 등.
- **TEST** (§4.6.3, p.114): 진단 출력(기본파일 DIAGNOSTIC).

## 12. Lock-up (§4.7)

- **COMPUTE** (§4.7, p.115-116): `COMPute [tbegc] [deltc] <Sec(기본)|MIn|HR|DAy> [tendc]`. 시간형식 7종(기본 옵션 7 = `153000.000`). 복수 COMPUTE 가능(이전 종료상태=다음 초기상태, 중간 INIT 없으면) → 시간스텝/경계/수치파라미터 변경 가능.
- **STOP** (§4.7, p.116): 필수, command 파일 끝 표시. 이후 정보 무시.

## 13. 설정 가이드라인 (Ch 5) — 핵심 수치

- **수평 해상도** (§5.1, p.118): peak 파장당 최소 **50 cell**(저파고 H/d≪1), 고파고는 **100 cell** 권장. 경계는 area of interest 에서 최소 2 파장 이격. sponge layer 만큼 도메인 확장.
- **연직 layer 수 ↔ kd 정확도** (Table 5.1, p.119): 정규화 파속 상대오차 기준 —

  | K(layer) | kd 범위 | 오차 |
  |---|---|---|
  | 1 | kd ≤ 0.5 | 1% |
  | 1 | kd ≤ 2.9 | 3% |
  | 2 | kd ≤ 7.7 | 1% |
  | 3 | kd ≤ 16.4 | 1% |

  단파 모의는 최대 3 layer 면 충분, **가변두께·등분포 사용(고정 layer 금지)** (p.120).
- **SWASH 근사 dispersion 식** (p.120): 정확식 $\omega^2 = gk\tanh(kd)$ 대신 1 layer 는 $\omega^2 = gk\,\dfrac{kd}{1+\frac14 k^2d^2}$, 2·3 layer 는 더 높은 차수 유리식(p.120, 식 verbatim). 1·2·3 등간격 layer 에만 적용, PRINT 파일에 표기.
- **layer별 최대 주파수**(Table 5.2, p.121, 발췌): d=10m → K=1: 0.26 Hz, K=2: 0.43, K=3: 0.63 Hz. (수심·layer 수에 따라 정확 표현 가능한 상한 주파수 존재.)

## 14. 미커버 영역 / 후속

- 본 노트 미상세: SOURCE(내부 wave 생성, p.58)·SPONGE LAYER(p.59)·FLOAT/BODY(부유체, p.61-63 → 소스 [[swash-floating-rigid-body]])·READGRID/READINP 세부 format·Appendix B 명령 문법·Appendix C swash.edt 전문. 필요시 해당 페이지 직접 참조.
- 부유체·비정수압·vegetation/porosity 물리 메커닉은 source-analysis(swash-floating-rigid-body / swash-nonhydrostatic-pressure-solver / swash-vegetation-porosity) 및 [[swash-tech-documentation-overview]] 와 상보.
