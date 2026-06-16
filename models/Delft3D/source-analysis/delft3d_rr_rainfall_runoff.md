---
title: "Delft3D RR 강우-유출 — Sobek-RR 커널의 개념별 유출 모형 + WALRUS C 커널"
model: Delft3D
component: rr/rainfall-runoff-kernel
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/rr/packages/). WALRUS C 커널: WALRUS.hh(상태·파라미터·플럭스 enum), WALRUSinternalflux.cpp(저류방정식·substep 예측), WALRUSdostep.cpp(substep 루프), WALRUSsysfuncs.cpp(W_dV·dVeq_dG·beta·Q_hS 시스템함수), WALRUSdefaults.cpp(기본값·상수). Fortran 커널: UnpavedModule.F90(저류·배수 변수, HellingaDeZ), RunoffFormulation.f90(HellingaDeZeeuwFormule·ErnstFormule·GreenRoofBalance·RunoffFactorFormulation), Sacramento.f90(LANDSC SAC-SMA), PAVEDMODULE.f90(CMPVHG), GreenhouseModule.f90, OpenwaterModule.f90 헤더를 file:line 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
---

# Delft3D RR 강우-유출 — Sobek-RR 커널의 개념별 유출 모형 + WALRUS C 커널

> RR(Rainfall-Runoff = Sobek-RR) 엔진의 유역 강우→유출 변환 커널. 개념(concept)별 유출 모형(unpaved·paved·greenhouse·open water·sacramento)이 Fortran으로, 추가로 WALRUS 집중형 모형이 C++ DLL로 구현됨. (경로: src/engines_gpl/rr/)

이 노트는 **수문 개념·저류방정식·배수 공식** 자체에 집중한다. 엔진 디스패치·DIMR 결합은 [[delft3d_engines_overview]], [[delft3d_dimr_coupling]] 참조.

---

## 1. 패키지 구성

| 패키지 | 언어 | 역할 | 경로 |
|---|---|---|---|
| `rr_kernel_f` | Fortran 90 | Sobek-RR 본체 — 개념별 유출 모형 전부 | `rr/packages/rr_kernel_f/src/` |
| `rr_walrus_c` | C++ | WALRUS 집중형 수문 모형 (별도 클래스, DLL) | `rr/packages/rr_walrus_c/src/` |
| `rr_kernel_c` / `rr_dll` / `rr` | — | C 래퍼·DLL 진입점 (탐색 범위 외) | — |

`rr_kernel_f`는 약 90개 `.f90` 파일. 핵심 개념 모듈 5종(아래)이 각각 1개 거대 module이며, 나머지는 네트워크·파일 I/O·meteo·테이블·복원(restart)·balance 보조다.

---

## 2. 개념(Concept)별 유출 모형 — Sobek-RR 핵심

Sobek-RR은 유역을 **토지이용 개념**으로 분할하고, 개념마다 다른 저류·유출 모형을 적용한다. 각 개념은 독립 Fortran module:

| 개념 | module | 파일 | 대표 계산 subroutine |
|---|---|---|---|
| 비포장(unpaved) | `Unpaved` | `UnpavedModule.F90:35` | `CMPOVH` (`:2663`) |
| 포장(paved) | `Paved` | `PAVEDMODULE.f90:35` | `CMPVHG` (`:1115`), `CMPVHG2016` (`:1646`) |
| 온실(greenhouse) | `Greenhouse` | `GreenhouseModule.f90:35` | `CMPKAS` (`:1374`) |
| 개수면(open water) | `Openwater` | `OpenwaterModule.f90:35` | — (수위 평형) |
| 도시배수(NWRW) | `NWRW` | `NWRWModule.f90:36` | `CMPPLV` (`:2109`) |
| Sacramento | `Sacramento` | `SacramentoModule.f90:36` | `LANDSC` (`Sacramento.f90:185`) |

> 네덜란드어 약어: `onverhard`=unpaved(비포장), `verhard(geb.)`=paved(포장), `kas`=greenhouse(온실), `ovh`=onverhard 인덱스, `vhg`=verhard 인덱스. 주석이 대부분 네덜란드어다.

---

## 3. 비포장(Unpaved) 개념 — 토양·지하수 저류 + 배수 공식

비포장 면적은 Sobek-RR의 핵심이며 **3층 모식**을 가진다 (`UnpavedModule.F90:82-100` 주석 verbatim):

```
 ***      -- opp. afstroming -----------> alfaoh(.,1)   ! 지표 유출
 ***   ------------------------- maaiveld               ! 지표면
 ***      ------------------------> alfa2(.,3)          ! 3차(tertiair) 배수
 ***   -------- tertiare ontwatering lvldrn(.,3)
 ***      ------------------> alfa2(.,2)                ! 2차 배수
 ***   --------- secundaire ontwatering lvldrn(.,2)
 ***      ----------------> alfa2(.,1)                  ! 1차(primair) 배수
 ***   ---------- primaire ontwatering lvldrn(.,1)
 ***           ---------> alfaoh(.,2)                   ! 지하수→개수면 배수
 ***   ----------------------- ontwateringsdiepte=open water streefpeil
 ***            <------- alfaoh(.,3)  infiltratie       ! 개수면→지하수 침투
```

핵심 상태/파라미터 (`UnpavedModule.F90:62-133`):
- `LVLOH` = maaiveld peil(지표 표고), `ONTWDP` = ontwateringsdiepte(배수심).
- `ALFAOH(.,1/2/3)` = α 인자 — 지표유출/지하수배수/침투 (단위 1/s).
- `ALFA2(.,1/2/3)` = 1·2·3차 배수계의 α (`:72-75`).
- `LVLDRN(.,1/2/3)` = 1·2·3차 배수 수위 (NAP 기준 환산, `:76-80`).
- `BERGTB` = 저류계수 표 (배수심 × 토양종, `:102-103`).
- `INF_V` = 침투속도(m/s, `:67`), `KWEL`/`WEGZG` = 상승류/침투류(seepage, `:118-122`).
- 불포화대(unsaturated zone)는 `type Unsat_Zone`로 max/min/init/actual 부피·mm 보관 (`UnpavedModule.F90:162-171`).

### 3.1 지하수 배수의 다중 배수계 수위차 (SetDeltaH)

`SetDeltaH` (`UnpavedModule.F90:6803`)는 지하수위 `GwLevel`을 1·2·3차 배수 수위와 비교해 각 배수계가 부담할 수위차 ΔH1~ΔH4를 적층(stacked) 또는 병렬(parallel)로 분배한다. **적층(gestapeld) 모드** (`DrainageDeltaH==0`, `:6842`):

| 조건 (`UnpavedModule.F90:6844-6862`) | 활성 배수계 |
|---|---|
| `GwLevel < LVLDRN(.,1)` | 지하수배수만 (DH1=GwLevel−peil) |
| `< LVLDRN(.,2)` | +1차 (DH2) |
| `< LVLDRN(.,3)` | +2차 (DH3) |
| ≥ LVLDRN(.,3) | +3차 (DH4) — 전 배수계 가동 |

병렬(parallel) 모드는 각 배수계 ΔH를 동일 GwLevel 기준으로 독립 계산 (`:6864-6881`).

### 3.2 Hellinga-De Zeeuw 배수 공식 (선형저수지 해석해)

`HellingaDeZeeuwFormule` (`RunoffFormulation.f90:129`)가 각 배수계의 유출 부피를 닫힌 형태로 계산한다. 코드(`:154-157`):

$$Q = \frac{A\,\alpha\,\beta\,\Delta H - \Delta Q}{\alpha}\,\bigl(1 - e^{-\alpha \Delta t}\bigr) + \Delta Q\,\Delta t$$

여기서 (`RunoffFormulation.f90:139-145`):
- `Area` $A$ = 면적(m²), `Alfa` $\alpha$ = 반응계수(1/s), `BergCoef` $\beta$ = 저류계수, `DeltaH` $\Delta H$ = 수위차(m), `DeltaQ` $\Delta Q$ = 현 시간스텝 수직 유입(Qin), `DeltaT` $\Delta t$ = 시간스텝.
- 출력 `Q`는 **부피(m³)** (주석 `:145` "omdat met area vermenigvuldigd wordt is het een VOLUME").

이는 선형저수지(linear reservoir) 지수감쇠 응답의 해석적 적분형이다. `HellingaDeZ` (`UnpavedModule.F90:5921`)가 4개 배수계 Q1~Q4를 합쳐 토양→개수면 총 유출 `Q2O(iovh)`로 만들고 timestepSize로 나눠 m³/s로 변환(`:5960-5971`). `Q2O<0`(침투, infiltration)이면 `AlfaOh(.,3)`로 재계산(`:5979-5981`).

### 3.3 대안 배수 공식

- **Ernst** (`ErnstFormule`, `RunoffFormulation.f90:165`): 저항(weerstand) 기반. $\text{Flux} = \dfrac{\Delta H}{W \cdot V_f \cdot 86400}$ [m/s] (`:197`), $V_f$=Vormfactor(형상계수, 기본 1.0 — 0.65~0.85 권장이나 사용자가 weerstand에 반영, `:188-189`). `NrSecondsPerDay=86400` (`:187`).
- **Krayenhoff van de Leur** (`KrayenhoffvdLeur`, `UnpavedModule.F90:6298`): 푸리에 급수 reservoir 응답.

배수 공식 선택은 `CompOption`/`UseScurve` 등으로 분기.

---

## 4. Sacramento (SAC-SMA) — 토양수분 회계 모형

`Sacramento` module의 `LANDSC` 함수(`Sacramento.f90:185`)는 미국 NWS의 **Sacramento Soil Moisture Accounting**을 그대로 이식한 것이다 (작성자: "Burnash and Ferral / Henk Ogink / Johan Crebas", `Sacramento.f90:42`).

상부/하부 2층 토양수분 저류 (`Sacramento.f90:208-244` 주석 verbatim):
- **상부대(Upper Zone)**: `UZTWC`/`UZTWM`(tension water 함량/용량), `UZFWC`/`UZFWM`(free water).
- **하부대(Lower Zone)**: `LZTWC`/`LZTWM`(tension), `LZFSC`/`LZFSM`(supplemental free), `LZFPC`/`LZFPM`(primary free).
- 유출 성분: `FLOSF`(지표유출), `FLOIN`(중간류 interflow), `FLOBF`(기저류 baseflow) (`:239-241`).
- 침루(percolation): `ZPERC`(건습 배율), `REXP`(지수), `PFREE`(하부 free로 직접 배분 비율), `PERCM`(포화 침루율 = `DCLZP*LZFPM+DCLZS*LZFSM`, `:238`).
- 불투수: `PCTIM`(상시 불투수 비율), `ADIMP`(추가 불투수, tension 포화 시), `ADIMC`(직접유출 생산 면적 함량) (`:226-244`).
- 시간계수 `FRACT`: 연=365 / 월=30 / 일=1 / 시간=24 (`:218-222`).

증발 손실 계산이 먼저 상부 tension → 상부 free 순으로 처리되고(`Sacramento.f90:269-296`), 상부 free/tension 비율 불균형 시 free→tension 재분배(`:298-311`). 초기화는 `Samini`(`:119`), 단위유량도(UH) 보간은 `SegmentUH`(`:47`), Clark UH 라우팅(`:1008` 주석)으로 직접·지표·중간류를 합성.

---

## 5. 포장(Paved)·도시배수(NWRW)·온실(Greenhouse)·개수면

### 5.1 Paved (`CMPVHG`, `PAVEDMODULE.f90:1115`)
포장면 강우 부피 계산(`:1167`):
$$RV = \text{AAFNodeRainfall} \cdot \text{RAIN} \cdot \text{AREAVH} \cdot \Delta t$$
하수계(sewer) 저류(`type SewerVars`, `PAVEDMODULE.f90:54-62`): `BMAXST/BINIST`(가로 max/init 저류), `BMAXRI/BINIRI`(혼합·분류식 저류 2종), 펌프 방향 `Q2VOW`(개수면/경계/하수처리장 RWZI). 건천(DWF: dry weather flow)와 강우 유출이 하수계를 거쳐 개수면·경계·RWZI로 배출.

### 5.2 NWRW 도시배수 (`RunoffFactorFormulation`, `RunoffFormulation.f90:37`)
NWRW 모형의 유출은 선형 저장식 $q = c\,h$ (c[1/min], h[mm]) (`RunoffFormulation.f90:50` 주석 verbatim). 입력 `VNow`(초기부피), `NetRain`, `RunoffFactor`=c, `RateInfiltration`; 출력 `TotUit`(총유출 m³), `Vinf`(침투). 분 단위(`NrsMin=60`)로 세분 적분(`:66-67`).

### 5.3 Greenhouse (`CMPKAS`, `GreenhouseModule.f90:1374`)
온실 면적은 **지붕 저류 + 저수조(basin/silo)** 모형 (`GreenhouseModule.f90:50-57` 주석): `AREAKK`(클래스별 총면적), `AREABK`(저수조 면적), `BMXDAK`(지붕 max 저류), `SILOC`(silo 용량), `PMPCAP`(silo 펌프능력). 지붕 강우가 저수조에 모이고 초과분이 유출.

### 5.4 Open water (`OpenwaterModule.f90:35`)
개수면은 수위 평형(연속식 기반) — 직접 강우·증발·인접 비포장 추가 저류면적(extra bergend oppervlak), seepage 옵션. `OpenwaterLevelComputations`=0(Simple)/1(Advanced, S-curve 저류곡선) (`OpenwaterModule.f90:52-62` 주석).

### 5.5 Green roof (`GreenRoofBalance`, `RunoffFormulation.f90:208`)
녹색지붕 토양수분 균형(`:216-225`):
$$\theta_{fin} = \theta_{init} + \text{Rain} - E_{act} - \text{Perc}, \quad \text{SurfRunoff}=\max(0,\theta_{fin}-\theta_{sat})$$
$\theta$는 wilting point / field capacity / saturation 기준으로 증발·침루를 분기 (`GreenRoofEact`/`GreenRoofPerc` 호출, `:217-219`).

---

## 6. WALRUS C++ 커널 — 집중형(lumped) 수문 모형

`rr_walrus_c`는 Sobek-RR 개념 모형과 **독립된** 집중형 모형으로, WALRUS(Wageningen Lowland Runoff Simulator)를 C++ class로 구현해 DLL로 노출한다 (`WALRUS.hh:142-145` "contains all the data and methods of a WALRUS model").

### 6.1 상태·저류 구조 (`WALRUS.hh`)

| 상태 (enum `WALRUS_STATE`, `:97-104`) | 의미 |
|---|---|
| `cur_dV` (61) | soil moisture deficit(불포화대 저류 결핍, mm) |
| `cur_dG` (62) | groundwater depth(지하수 깊이, mm) |
| `cur_hQ` (63) | quickflow reservoir 수위(mm) |
| `cur_hS` (64) | surface water(open water) 수위(mm) |

핵심 물리 파라미터 (enum `WALRUS_PAR`, `:19-37`, 주석 verbatim):
- `cW`(1) = "wetness index parameter, controls the divider (mm)"
- `cV`(2) = "vadose zone relaxation time, controls the connection saturated-unsaturated"
- `cG`(3) = "groundwater reservoir constant, controls the outflow of groundwater to open water (mm h)"
- `cQ`(4) = "quickflow reservoir constant"
- `cS`(5) = "bankfulle discharge of open water (mm/h)", `cD`(6) = "channel depth"
- `aS`(10) = "surface water fraction, 1-par_aS = ground water fraction", `area`(11) = 유역면적(km²)
- 불포화대: `psi_ae`(7, air entry value), `b`(8, pore size distribution), `theta_s`(9, saturated soil moisture).

외부 강제력(enum `WALRUS_FORCING`, `:85-91`): `fc_P`(강우), `fc_ETpot`(잠재증발), `fc_XS`/`fc_XG`(개수면·지하수 외부 유출입).

### 6.2 저류 방정식 / 시간 적분 (`WALRUSinternalflux.cpp`)

`calctryvalues(tend)` (`WALRUSinternalflux.cpp:38`)가 한 (sub)스텝의 모든 플럭스와 4개 상태 갱신을 계산한다.

**강우 분배** (`:49-51`): wetness index $W$로 빠른/느린 경로 분배 + 지표면 비율 $a_S$:
$$P_Q = P\,W\,a_G, \quad P_V = P\,(1-W)\,a_G, \quad P_S = P\,a_S$$
($a_G = 1-a_S$, `WALRUSdefaults.cpp:44`).

**증발** (`:52-60`): $E_{TV} = E_{Tpot}\,\beta(dV)\,a_G$ (불포화대), 개수면 증발 $E_{TS}$는 $h_S>$ `hSzeroforET`(=1mm, `WALRUSdefaults.cpp:91`)일 때만.

**선형저수지 플럭스** (`:63-65`, $dt$=시간[h]):
$$f_{QS} = \frac{h_Q}{c_Q}\,dt \;\text{(quickflow)}, \quad f_{GS} = f_{GS}(dG)\,dt \;\text{(baseflow)}, \quad Q = Q(h_S)\,dt$$
baseflow 함수 `fGS_dG` (`:36`): $f_{GS}(dG) = (cD - dG - hS)\cdot\max(cD-dG,\,hS)/cG$.

**상태 갱신** (`:67-85`):
$$dV \mathrel{+}= \frac{-f_{XG} - P_V + E_{TV} + f_{GS}}{a_G},\quad h_Q \mathrel{+}= \frac{P_Q - f_{QS}}{a_G}$$
$$h_S \mathrel{+}= \frac{f_{XS} + P_S - E_{TS} + f_{GS} + f_{QS} - Q}{a_S},\quad dG \mathrel{+}= \frac{dV - dV_{eq}}{c_V}\,dt$$
지하수→불포화대 결합은 결핍 $dV$가 평형결핍 $dV_{eq}(dG)$로 `cV`(완화시간)로 이완되는 1차식.

**침수/범람 특수처리** (`:87-129`): $dV<0$(ponding, 토양 완전포화)이거나 $h_S>cD$(flooding, 만수위 초과)이면 과잉수를 토양↔개수면 간 면적비로 재분배.

### 6.3 시스템 함수 (`WALRUSsysfuncs.cpp`) — 해석형 닫힌식

- **wetness index** `W_dV` (`:38-43`): $W = \tfrac{1}{2}\cos\!\bigl(\tfrac{\pi}{cW}\,\mathrm{clip}(dV,0,cW)\bigr) + \tfrac12$.
- **평형결핍** `dVeq_dG` (`:55-77`): Brooks-Corey 토양수분 적분형, $dG>\psi_{ae}$일 때 $(dG - \tfrac{\psi_{ae}}{1-b} - dG\,u + \tfrac{dG}{1-b}u)\,\theta_s$ where $u=(dG/\psi_{ae})^{-1/b}$.
- **증발 감소계수** `beta_dV` (`:85-96`): 로지스틱형 $\beta = \tfrac{1-e^{-\zeta_1(\zeta_2-dV)}}{2(1+e^{-\zeta_1(\zeta_2-dV)})}+\tfrac12$ ($\zeta_1$=0.02, $\zeta_2$=400, `WALRUSdefaults.cpp:89-90`).
- **수위-유량 관계** `Q_hS` (`:104-140`): $h_S<h_{Smin}$면 0; 정상범위 $Q=cS\,(h_{frac})^{expS}$ (expS 기본 1.5, `WALRUSdefaults.cpp:41`), $h_S>cD$(범람) 시 $cS + cS\,(h_{frac})^{expS}$.

네 시스템 함수 모두 `set_*_bytable`로 테이블 선형보간 대체 가능(`WALRUSsysfuncs.cpp:49-53` 등, `approxfun` linint).

### 6.4 적응적 substep 적분 (`WALRUSdostep.cpp`)

`dostep(deltime)` (`:34`)는 **적응적 substep**으로 안정적 적분을 수행한다:
1. `calctryvalues`로 try값 계산 → `pred_time_tries_OK`로 허용 가능한 최대 시각 `tc` 예측 (`:53-54`).
2. `tc`가 목표시각보다 작으면 substep 반복, 각 substep에서 플럭스 누적 (`:55-92`).
3. `pred_time_tries_OK` (`WALRUSinternalflux.cpp:132`): 음수 수위 방지(`hS_try/hQ_try < min_h`), 강우/증발/외부플럭스 step이 `max_Pstep`(=10mm) 초과, 수위변화가 `max_h_change`(=10mm) 초과 시 시간을 비례 축소. `max_substeps`=288 (`WALRUSdefaults.cpp:53`).

### 6.5 Fortran↔C 인터페이스 (`WalrusInterface.cpp`)
`walrusInstances` 벡터로 다중 인스턴스 관리. `ADDWALRUSINSTANCE`(`:32`), `WALRUSSET/GET`(`:89`/`:107`, enum id 기반), `WALRUSINIT`(`:143`, Q0·초기상태), `WALRUSDOSTEP`(`:162`). `startIndex==1`이면 Fortran 1-based 인덱스를 0-based로 변환(`:68-70`). 모든 호출 try/catch로 에러코드(-1) 반환.

---

## 7. 토양 종류 사전 (WALRUS)

`WALRUS.hh:44-60` `enum WALRUS_SOIL`: sand(21)~clay(31) 11종 + cal_H(32)/cal_C(33) 보정형 + custom(34). `set_st(soil)`로 `psi_ae`/`b`/`theta_s`를 토양종별로 일괄 설정(`WALRUSdefaults.cpp:86` 기본 `loamy_sand`).

---

## 8. 요약: 두 갈래 RR 모형

| 측면 | Sobek-RR (`rr_kernel_f`) | WALRUS (`rr_walrus_c`) |
|---|---|---|
| 공간 표현 | 토지이용 개념별 분포형 (unpaved/paved/greenhouse/openwater/sacramento) | 집중형(lumped) 단일 유역 |
| 비포장 배수 | Hellinga-De Zeeuw / Ernst / Krayenhoff 선형저수지 (`RunoffFormulation.f90`) | quickflow+groundwater 2저수지 (`WALRUSinternalflux.cpp`) |
| 토양수분 | Capsim 불포화대 / Sacramento SAC-SMA 옵션 | dV-dG 결핍 + Brooks-Corey 평형 |
| 시간적분 | 고정 timestep (분 단위 세분 일부) | 적응적 substep (`WALRUSdostep.cpp`) |
| 적분형 | 선형저수지 해석해 | 명시적 substep + 침수/범람 보정 |

---

## 미확인 / source-needed

- `CMPOVH`(unpaved 메인, `UnpavedModule.F90:2663`)의 전체 시간스텝 균형식 본체는 헤더·배수 호출만 확인. 완전 물질수지 추적은 source-needed.
- Krayenhoff van de Leur 공식 본체(`UnpavedModule.F90:6298`)는 호출 위치만 확인, 푸리에 계수식 미전사 — source-needed.
- Capsim 불포화대(`ComputeCapsim`, `UnpavedModule.F90:4846`)·Capillary rise 상세는 미전사 — source-needed.
- `balancemodule.F90` 전역 물질수지 검증 로직 미확인 — source-needed.
- WALRUS `init_by_*` 정상상태 초기화(warm-up 회피) 알고리즘은 헤더 주석만 확인(`WALRUS.hh:333-388`), 본체(`WALRUSinit.cpp`) 미전사 — source-needed.
