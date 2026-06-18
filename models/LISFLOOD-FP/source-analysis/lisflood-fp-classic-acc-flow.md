---
title: "LISFLOOD-FP classic CPU 솔버 — ACC(local inertia)·diffusive·Roe + time loop(IterateQ)"
model: LISFLOOD-FP
component: "classic CPU floodplain solvers (fp_acc / fp_flow / fp_trent) + IterateQ time loop + UpdateH"
canonical_source: self
citation_status: verified
verification_method: "raw/source_code/LISFLOOD-FP/ 소스 직접 read: lisflood.cpp(main :34, Solver 기본값 :162-185, CPU/CUDA dispatch :416-456·:768-796), fp_acc.cpp(CalcFPQxAcc :18-111, CalcFPQyAcc :115-205, CalcT :237-280, UpdateQs :292-324), fp_flow.cpp(FloodplainQ dispatch :17-119, CalcFPQx :122-233), fp_trent.cpp(=Roe solver CalcFPQxRoe :18-440, CalcTRoe :914-960, UpdateQsRoe :972-1018), iterateq.cpp(IterateQ :16-478, UpdateH :482-587). lisflood.h(struct Solver :724-751, 함수 선언 :930-1010). 모든 식·인덱스 해당 라인 직접 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[lisflood-fp-architecture-source-map]]"
  - "[[../../SFINCS/source-analysis/sfincs-architecture-source-map]]"
---

# LISFLOOD-FP classic CPU 솔버 — ACC / diffusive / Roe + time loop

> [[lisflood-fp-architecture-source-map]] §2.1 "Classic FP 솔버" 의 식·이산화 보완.
> 범위: **CPU** classic 경로(`IterateQ`)에서 호출되는 reduced-physics floodplain flux 솔버.
> 격자: cell-centred 수심 `H[xsz·ysz]`, edge 유량 `Qx/Qy[(xsz+1)·ysz±1]` staggered grid.

---

## 0. 중요 정정 — 파일명 ≠ 솔버명

| 파일 | header 주석 | 실제 내용 |
|---|---|---|
| `fp_acc.cpp` | "FLOODPLAIN FLOW WITH ACCELERATION" (`fp_acc.cpp:3`) | **ACC = local inertia** (Bates et al. 2010) |
| `fp_flow.cpp` | "FLOODPLAIN FLOW" (`fp_flow.cpp:3`) | dispatch `FloodplainQ` + **diffusive wave** `CalcFPQx/y` |
| `fp_trent.cpp` | "FLOODPLAIN FLOW WITH ROE APPROXIMATE RIEMANN SOLVER 1st ORDER" (`fp_trent.cpp:3`) | **Roe 근사 리만 솔버** — "Trent" 아님 |

`fp_trent.cpp` 는 2008년 Ignacio TRENT formulation 용으로 신설됐으나(`VersionHistory.h:293` "New file fp_trent.cpp") 현재 코드는 Roe 솔버를 담고 있다. `[[lisflood-fp-architecture-source-map]]` §2.1 표의 "Trent — 추가 dynamic 처리" 설명은 이 정정으로 대체.

---

## 1. main() 솔버 dispatch (`lisflood.cpp`)

### 1.1 두 단계 분기

**(a) CUDA 경로** (`lisflood.cpp:416-456`, `#ifdef CUDA`): fv1·fv2·dg2·acceleration·acc_nugrid·mwdg2/hwfv1 GPU 클래스 직접 실행 후 `return 0`.

**(b) CPU 경로** (`lisflood.cpp:768-796`):

| 조건 | 호출 | 파일 |
|---|---|---|
| `Statesptr->SGC==ON` | `Fast_MainStart(...)` (:772) | sub-grid 별도 time loop |
| `Statesptr->fv1==ON` | `fv1::solve(...)` (:777) | full SWE FV1 |
| `Statesptr->dg2==ON` | `dg2::solve(...)` (:782) | full SWE DG2 |
| **else** | **`IterateQ(...)`** (:795) | **classic time loop** ← 본 노트 |

→ ACC·diffusive·Roe·qlim 는 모두 `IterateQ` 안으로 들어가며, 실제 flux 솔버 선택은 `IterateQ` → `FloodplainQ` 안에서 cell-by-cell 분기(§3).

### 1.2 Solver 구조체 기본값 (`lisflood.cpp:162-185`)

| 필드 | 기본값 | 라인 | 의미 |
|---|---|---|---|
| `InitTstep` | `10.0` | :162 | 초기/최대 Δt |
| `g` | `9.80655` | :166 | 중력가속도 |
| `cfl` | `0.7` | :168 | CFL 계수 |
| `DepthThresh` | `1e-3` | :171 | 흐름 계산 수심 하한 |
| `MomentumThresh` | `1e-2` | :172 | (Roe) 운동량 갱신 수심 하한 |
| `MaxHflow` | `10.0` | :173 | `hflow` 상한(clip) |
| `dhlin` | `0.01`→`dx·0.0002` | :177, :465 | diffusive 선형화 임계(Cunge 1980) |
| `Qlimfact` | `1.0` | :179 | flux limiter 계수 |
| `theta` | `1.0` | :184 | q-centred scheme 가중(θ=1 → Bates 2010 semi-implicit) |
| `fricSolver2D` | `ON` | :185 | 2D 마찰(직교 q 벡터 합성) |

State 기본값: `adaptive_ts=ON`(:206), `qlim=OFF`(:207), `acceleration=OFF`(:208), `Roe=OFF`(:234), `diffusive=OFF`(:193).

---

## 2. ACC — local inertia 근사 SWE (`fp_acc.cpp`)

LISFLOOD-FP 대표 reduced-physics. **advection(이류) 항 무시, 국소 관성항 유지**. `CalcFPQxAcc`(:18-111)·`CalcFPQyAcc`(:115-205) 두 함수가 x/y edge 유량을 계산(대칭 구조 — 아래는 x).

### 2.1 기하·상태 변수 (`fp_acc.cpp:26-66`)

```
p0=i+j*xsz; p1=i+1+j*xsz;           // 좌/우 cell  (:26-27)
pq0=i+j*(xsz+1)+1;                  // 두 cell 사이 edge  (:35)
q0=Arrptr->Qxold[pq0];   // 이전 step 단위폭 유량 m²/s  (:41)
```

- 자유수면 차: `dh = (z0+h0)-(z1+h1)` (:60-63), 마찰경사 `Sf = -dh/dx` (:65).
- **flow depth** `hflow = max(z0+h0, z1+h1) - max(z0,z1)` → `max(·,0)` → `min(·, MaxHflow)` (:66-68). 두 cell 중 높은 수면에서 높은 바닥을 뺀 "edge 위 유효 통수심" — LISFLOOD-FP 공통 정의.

### 2.2 마찰항 q 벡터 (`fp_acc.cpp:45-55`)

`fricSolver2D==ON` 이면 직교방향 4개 `Qyold` 평균 `qy_avg` 와 합성해 `qvect=√(q0²+qy_avg²)` (:46-51). OFF 면 `qvect=q0` (:54). 마찰 분모에 `|qvect|` 사용 → 2D 마찰.

### 2.3 핵심 이산화 — q-centred semi-implicit (`fp_acc.cpp:88`)

마찰 임계 통과(`hflow>DepthThresh`, `MaskTest`) 시 (`fp_acc.cpp:83-85`):

$$
Q = \frac{\theta\,q_0 + \tfrac{1}{2}(1-\theta)(q_{up}+q_{down}) - g\,\Delta t\,h_{flow}\,S_f}{1 + g\,\Delta t\,h_{flow}\,n^2\,|q_{vect}|\,/\,h_{flow}^{10/3}}\;\Delta x
$$

`fp_acc.cpp:88` verbatim:
```c
Q=((Solverptr->theta*q0+C(0.5)*(1-Solverptr->theta)*(qup+qdown))-(g*dt*hflow*Sf))/(1+g*dt*hflow*fn*fn*fabs(qvect)/(pow(hflow,(C(10.0)/C(3.0)))))*Parptr->dx;
```
- 분자: 관성(이전 유량) + 압력경사(`-g·Δt·hflow·Sf`). advection 항 없음 → local inertia.
- 분모: implicit 마찰 (Manning `n²`, `hflow^{10/3}`). `θ=1` → `q_up/q_down` 항 소거되어 순수 Bates(2010) semi-implicit.
- `q_up=Qxold[pq0-1]`, `q_down=Qxold[pq0+1]` (:72-73), 경계(i=0, i=xsz-2)에서 0이면 `q0` 로 대체(:74-81).

### 2.4 질량오차 보정 (`fp_acc.cpp:92-95`)

q-centred 가 부호 역전(질량오차) 유발 시 — `Q*dh < 0` (:92) — **순수 Bates 2010 semi-implicit** 로 재계산(`q_up/q_down` 제외):
```c
Q=(q0-(g*dt*hflow*Sf))/(1+g*dt*hflow*fn*fn*fabs(qvect)/(pow(hflow,(C(10.0)/C(3.0)))))*Parptr->dx;
```
(`fp_acc.cpp:94`). 주석 원문: "version of line above that will compile on windows machine" — `copysign` 비교의 대체.

### 2.5 CFL time step (`fp_acc.cpp:237-280`, `CalcT`)

ACC 안정 조건은 **수심(중력파속) 기반** (advection 무시 → 유속항 없음):

$$\Delta t = \mathrm{cfl}\cdot\frac{\Delta x}{\sqrt{g\,H_{max}}}$$

`fp_acc.cpp:271`:
```c
locT=cfl*Parptr->dx/(sqrt(g*MH));
Solverptr->Tstep=getmin(Solverptr->Tstep,locT);   // :272
```
- `MH = CalcMaxH(...)` (:247) — 전 도메인 max H(OpenMP reduction, `fp_acc.cpp:208-234`). 단일 전역 Δt → 전역 안정성.
- `MH<DepthThresh` 면 `Tstep=InitTstep` (:276). h가 분모이므로 마른 격자 회피(주석 :250).
- 구식(Brett 코드 기반) 국소 Δt 루프는 주석 처리됨(:253-269) — 현재는 MSH/TJF 전역식만 사용.

### 2.6 q 갱신 (`fp_acc.cpp:292-324`, `UpdateQs`)

step 종료 후 `Qxold = Qx · (1/dx)` (m²/s 로 환원, :307), `Qyold` 동일(:319). `IterateQ` 가 매 step 호출(`iterateq.cpp:168`).

---

## 3. dispatch — FloodplainQ (`fp_flow.cpp:17-119`)

`IterateQ` 가 매 step 호출하는 flux 디스패처. **Qx 루프(:31-68) + Qy 루프(:71-117)** 분리, 각 OpenMP 병렬.

### 3.1 Δt 계산 선행 (`fp_flow.cpp:25-27`)
```c
if(Statesptr->acceleration==ON) CalcT(...);   // :25
if(Statesptr->Roe==ON) CalcTRoe(...);         // :26
TmpTstep = Solverptr->Tstep;                  // :27
```
diffusive/adaptive 는 여기서 Δt 미산정 — flux 함수 내부에서 `*TSptr` 로 누적(§4.2).

### 3.2 cell-by-cell 솔버 선택 (`fp_flow.cpp:45-52` Qx)

수심 임계 통과(`h0>DepthThresh || h1>DepthThresh`, :45) 시 우선순위 분기:

| 순위 | 조건 | 호출 | 솔버 |
|---|---|---|---|
| 1 | `weirs==ON && *wiptr!=-1` | `CalcWeirQx` (:47) | 위어/둑 |
| 2 | `porosity==ON` | `CalcFPQxPor` (:48) | porosity |
| 3 | `acceleration==ON` | **`CalcFPQxAcc`** (:49) | ACC §2 |
| 4 | `Roe==ON` | **`CalcFPQxRoe`** (:50) | Roe §5 |
| 5 | `adaptive_ts==ON \|\| qlim==ON` | **`CalcFPQx`** (:51) | diffusive §4 |

(Qy 동일: `fp_flow.cpp:95-99`).

### 3.3 Δt reduce (`fp_flow.cpp:57-67`)

ACC/Roe 는 함수 내 Δt 미변경 → reduce 생략(:57-60). diffusive/adaptive 만 thread-local `ThreadTS` 를 `#pragma omp critical` 로 전역 최소화(:63-66, Qy :112-115).

---

## 4. diffusive wave (`fp_flow.cpp:122-349`, `CalcFPQx/y`)

관성항 전부 무시, Manning 균등류식만. `dx_sqrt`·`dhlin` 선형화 포함. (방향별 if-블록 대칭, 아래 x·flow 0→1.)

### 4.1 Manning 균등류 flux (`fp_flow.cpp:139-157`)

`z0+h0 > z1+h1 && h0>DepthThresh` 시 (:139):
- `dh = (z0+h0)-(z1+h1)` (:141), `Sf = √(dh/dx)` (:142), `hflow` ACC와 동일 정의(:143-145).

$$Q = \frac{h_{flow}^{5/3}\,S_f\,\Delta y}{n}$$

`fp_flow.cpp:157`:
```c
Q=(pow(hflow,(C(5.0)/C(3.0)))*Sf*Parptr->dy/fn);
```
역방향(1→0)은 부호 반전 `-pow(...)` (:198).

### 4.2 선형화 + adaptive Δt (`fp_flow.cpp:150-162`)

작은 경사(`dh < dhlin`, :150)에서 `Sf` 와 `alpha` 를 선형화해 0-나눗셈 회피:
```c
Sf=sqrt(Parptr->dx/Solverptr->dhlin)*(dh/Parptr->dx);                      // :152
alpha=(pow(hflow,(5/3))*Parptr->dx_sqrt)/(fn*sqrt(Solverptr->dhlin));      // :153
```
그 외 `alpha = hflow^{5/3}/(2·fn·Sf)` (:155). adaptive Δt(:158-163):
$$\Delta t \le 0.25\,\frac{\Delta y^2}{\alpha}$$
```c
*TSptr=getmin(*TSptr,(C(0.25)*Parptr->dy*Parptr->dy/alpha));   // :160
```
diffusion-number 안정조건. → `TRecx[pTQ]` 기록(:162).

### 4.3 flow limiter (qlim, `fp_flow.cpp:167-174`)

`adaptive_ts==OFF`(=qlim 모드)이면 Δt 고정, 대신 유량 제한:
$$Q_{lim} = Q_{limfact}\cdot\frac{dA\cdot|dh|}{8\,\Delta t}$$
```c
Qlim=Solverptr->Qlimfact*Parptr->dA*fabs(dh)/(8*Solverptr->Tstep);   // :167
if(fabs(Q)>Qlim){ ... Q=±Qlim; ... }                                // :168-171
```
초과분을 clip → `LimQx[pTQ]` 기록(:173).

### 4.4 MaskTest (`fp_flow.cpp:352-358`)

채널마스크 `-1`(=floodplain) 인접 조합만 흐름 허용 — 둘 다 -1, 또는 한쪽 -1·다른쪽 >0(채널 cell) (:354-356).

---

## 5. Roe 근사 리만 솔버 (`fp_trent.cpp`)

1차 Godunov-형 full-SWE flux. ACC/diffusive 와 달리 보존변수 `H, HU, HV` 직접 적분. `CalcFPQxRoe`(:18-440)·`CalcFPQyRoe`(:444-890).

### 5.1 Roe 평균·고유값 (`fp_trent.cpp:75-128`, both wet)

`hl,hr ≥ dtol`(:75) 둘 다 젖은 경우:
- Roe 평균: `ubarra=(√hr·ur+√hl·ul)/(√hr+√hl)` (:86), `cbarra=√(0.5·g·(hl+hr))` (:88).
- 고유값 `a1=u+c, a2=u, a3=u-c` (:90-92), Harten-Hyman entropy fix(`epsilon`, `maximum()` :101-108).
- 파동강도 `alfa1..3` (:114-116), 고유벡터 `e11..e33` (:118-128).

### 5.2 intercell flux (`fp_trent.cpp:132-142`)

좌/우 물리 flux 평균에서 Roe 소산 차감:
```c
Arrptr->FHx[pq0]=C(0.5)*(f1rp+f1lp-a1m*alfa1*e11-a2m*alfa2*e21-a3m*alfa3*e31);   // :140
Arrptr->FHUx[pq0]=...;  Arrptr->FHVx[pq0]=...;   // :141-142
```
`f2 = hu·u + 0.5·g·h²`(운동량 flux, :133). 바닥경사 source `s0=-(z1-z0)/dl` → `RSHU/LSHU`(:144-150).

### 5.3 마름/젖음 처리 (`fp_trent.cpp:153-421`)

`left dry`(:153)·`right dry`(:272): overtopping(둑 넘침) vs wall(벽) 분기. `Roe_slow==ON`(:206) 이면 ghost-cell 반사로 full Roe 재계산, 아니면 flat/wall flux 근사. (Y 방향 :590-869 대칭.)

### 5.4 Roe time step (`fp_trent.cpp:914-960`, `CalcTRoe`)

ACC와 달리 **유속+파속** 둘 다 포함(advection 존재):
```c
locTx=cfl*(Parptr->dx/(fabs(locU)+(sqrt(g*locH))));   // :946
locTy=cfl*(Parptr->dx/(fabs(locV)+(sqrt(g*locH))));   // :947
locT = min(locTx,locTy);                              // :948
```
cell-by-cell 순회, 전역 최소(:950). `Tstep=InitTstep` 초기화(:931).

### 5.5 보존변수 갱신 (`fp_trent.cpp:972-1018`, `UpdateQsRoe`)

flux divergence + source 로 `HU/HV` 적분 후 implicit 마찰:
```c
Arrptr->HU[pc]+=-(Tstep/dx)*(FHUx[pxr]-FHUx[pxl]+FHUy[pyr]-FHUy[pyl])+Tstep*(BSHU+TSHU+LSHU+RSHU);  // :994
...
Arrptr->HU[pc]*=(1/(1+g·Tstep·sf));   // implicit friction  :1008
```
`H<MomentumThresh` 면 `HU=HV=0` (:1011-1014). H 자체는 `UpdateH`(§6, FHx/FHy 통해) 가 갱신.

---

## 6. time loop — IterateQ (`iterateq.cpp:16-478`)

classic CPU 전체 시간적분 루프.

### 6.1 모드별 초기 Δt (`iterateq.cpp:39-88`)
`t==0` 시 adaptive/acceleration/Roe/non-adaptive 모두 `Tstep=MinTstep=InitTstep`(:43-44 등). SGC 는 별도로 `CalcT` 선실행(:84).

### 6.2 메인 while (`iterateq.cpp:99-439`)

`while(t < Sim_Time)`(:99) 한 step:

| 단계 | 호출 | 라인 |
|---|---|---|
| 1. 채널(1D) | `ChannelQ`/`ChannelQ_Diff` (ts_multiple마다) | :104-116 |
| 2. Δt 리셋 | `if(t>0) Tstep=InitTstep` | :144 |
| 3. **floodplain flux** | **`FloodplainQ`** (→§3) | :146 |
| 4. 경계 | `BCs`, `drain_nodata_water` | :148-149 |
| 5. dry check | `DryCheck` | :150 |
| 6. infil/evap/rain/routing | (옵션) | :153-157 |
| 7. **수심 갱신** | **`UpdateH`** (→§6.3) | :163 |
| 8. hazard V | `UpdateV` | :165 |
| 9. 경계 flux | `BoundaryFlux` | :167 |
| 10. **q 갱신** | `UpdateQs`(ACC) / `UpdateQsRoe`(Roe) | :168-169 |
| 11. 시간 전진 | `t += Tstep` | :174 |

mass balance(:212-265), stage/gauge 출력(:268-307), checkpoint(:310-320), regular/overpass 출력(:325-410), kill/steady-state(:413-437).

> SGC 분기(:118-140)는 본 루프에서 비활성(`printf("SGC not processed here")` :120) — SGC 는 `Fast_MainStart` 별도 경로(§1.1).

### 6.3 UpdateH — 연속방정식 (`iterateq.cpp:482-587`)

cell 4-edge flux 합으로 수심 적분 (`ChanMask==-1` cell만, :526):
$$dV = \Delta t\,(Q_x^{left}-Q_x^{right}+Q_y^{top}-Q_y^{bottom}),\quad H \mathrel{+}= dV/dA$$
```c
dV = Solverptr->Tstep*(*qxptr0 - *(qxptr0+1) + *qyptr0 - *qyptr1);   // :539
(*hptr) += dV / Parptr->dA;                                          // :540
if (*hptr<C(0.0)) *hptr = C(0.0);                                    // :541  음수 clip
```
porosity 시 `dAPorTemp=PorArea(...)` 로 면적 보정(:530-535). 점source(QFIX/QVAR :496-513, HFIX/HVAR :560-583)도 여기서 H 주입.

---

## 7. 솔버 비교 요약

| 항목 | ACC (fp_acc) | diffusive (fp_flow CalcFPQx) | Roe (fp_trent) |
|---|---|---|---|
| 물리 | local inertia (관성 O, advection X) | 관성 전부 X | full SWE (advection O) |
| 변수 | edge Q | edge Q | H,HU,HV 보존변수 |
| 마찰 | implicit, q-centred (`fp_acc.cpp:88`) | explicit Manning (`fp_flow.cpp:157`) | implicit (`fp_trent.cpp:1008`) |
| Δt | `cfl·dx/√(gH)` (`:271`) | `0.25·dy²/α` (`fp_flow.cpp:160`) | `cfl·dx/(|u|+√(gH))` (`:946`) |
| q 갱신 | `UpdateQs` (`:307`) | (없음) | `UpdateQsRoe` (`:994`) |
| 안정성 출처 | 수심만(파속) | diffusion number | 유속+파속 (CFL) |
| 비용 | 저 | 저 | 고 |

물리 충실도: diffusive < **ACC** < Roe < (FV1/DG2, [[lisflood-fp-architecture-source-map]] §3). ACC 의 q-centred semi-implicit(θ=1)는 Bates et al.(2010) 식으로, 본 노트 §2.3-2.4 가 그 코드 구현.
