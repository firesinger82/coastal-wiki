---
title: "LISFLOOD-FP classic CPU 솔버 — ACC(local inertia)·diffusive·Roe + time loop(IterateQ)"
model: LISFLOOD-FP
component: "classic CPU floodplain solvers (fp_acc / fp_flow / fp_trent) + IterateQ time loop + UpdateH"
canonical_source: self
citation_status: verified
verification_method: "v8.2 판독 이력, raw/source_code/LISFLOOD-FP/ 소스 직접 read: lisflood.cpp(main :34, Solver 기본값 :162-185, CPU/CUDA dispatch :416-456·:768-796), fp_acc.cpp(CalcFPQxAcc :18-111, CalcFPQyAcc :115-205, CalcT :237-280, UpdateQs :292-324), fp_flow.cpp(FloodplainQ dispatch :17-119, CalcFPQx :122-233), fp_trent.cpp(=Roe solver CalcFPQxRoe :18-440, CalcTRoe :914-960, UpdateQsRoe :972-1018), iterateq.cpp(IterateQ :16-478, UpdateH :482-587). lisflood.h(struct Solver :724-751, 함수 선언 :930-1010). 모든 식·인덱스 해당 라인 직접 확인.; 2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영"
last_source_check: "2026-10-21 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "lisflood-fp-architecture-source-map.md"
  - "../../SFINCS/source-analysis/sfincs-architecture-source-map.md"
---

# LISFLOOD-FP classic CPU 솔버 — ACC / diffusive / Roe + time loop

> [architecture source map](lisflood-fp-architecture-source-map.md) §2.1 "Classic FP 솔버" 의 식·이산화 보완.
> 범위: **CPU** classic 경로(`IterateQ`)에서 호출되는 reduced-physics floodplain flux 솔버.
> 격자: cell-centred 수심 `H[xsz·ysz]`, edge 유량 `Qx/Qy[(xsz+1)·ysz±1]` staggered grid.

---

## 0. 중요 정정 — 파일명 ≠ 솔버명

| 파일 | header 주석 | 실제 내용 |
|---|---|---|
| `fp_acc.cpp` | "FLOODPLAIN FLOW WITH ACCELERATION" (`fp_acc.cpp:3`) | **ACC = local inertia** (Bates et al. 2010) |
| `fp_flow.cpp` | "FLOODPLAIN FLOW" (`fp_flow.cpp:3`) | dispatch `FloodplainQ` + **diffusive wave** `CalcFPQx/y` |
| `fp_trent.cpp` | "FLOODPLAIN FLOW WITH ROE APPROXIMATE RIEMANN SOLVER 1st ORDER" (`fp_trent.cpp:3`) | **Roe 근사 리만 솔버** — "Trent" 아님 |

`fp_trent.cpp`는 2008년에 Ignacio의 TRENT formulation을 통합하면서 신설되었다(`VersionHistory.h:299–300`). 현재 코드는 공간 1차 Roe 근사 리만 해법을 구현한다(`fp_trent.cpp:3`; `fp_flow.cpp:50`). [architecture source map](lisflood-fp-architecture-source-map.md) §2.1도 이 파일을 Roe 해법으로 분류한다. [10-21 전수 검증 정정]

---

## 1. main() 솔버 dispatch (`lisflood.cpp`)

### 1.1 두 단계 분기

**(a) CUDA 경로**는 `#ifdef CUDA` 안에서 FV1·FV2·DG2·ACC·acc_nugrid·adaptive를 선택한다(`lisflood.cpp:420–457`). [10-21 대조 정정]
이 driver는 실행 뒤 `return 0;`으로 반환한다(`lisflood.cpp:457`). [10-21 대조 정정]

**(b) SGC·FV1·DG2·classic 분기**는 `lisflood.cpp:773–805`에 있다. [10-21 대조 정정]

| 조건 | 호출 | 파일 |
|---|---|---|
| `Statesptr->SGC==ON` | `Fast_MainStart(...)` (`lisflood.cpp:775`) | sub-grid 별도 time loop. [10-21 대조 정정] |
| `Statesptr->fv1==ON` | `#ifdef METAL_ENABLED` 안의 `if (Statesptr->cuda == ON && metal_is_available())`이면 Metal FV1 (`lisflood.cpp:780–784`) | 그 밖에는 `fv1::solve(...)` (`lisflood.cpp:787–788`). [10-21 대조 정정] |
| `Statesptr->dg2==ON` | `dg2::solve(...)` (`lisflood.cpp:792–793`) | full SWE DG2. [10-21 대조 정정] |
| **else** | **`IterateQ(...)`** (`lisflood.cpp:805`) | **classic time loop**. [10-21 대조 정정] |

→ ACC·diffusive·Roe·qlim 는 모두 `IterateQ` 안으로 들어가며, 실제 flux 솔버 선택은 `IterateQ` → `FloodplainQ` 안에서 cell-by-cell 분기(§3).

### 1.2 Solver 구조체 기본값 (`lisflood.cpp:165–188`) [10-21 대조 정정]

| 필드 | 기본값 | 라인 | 의미 |
|---|---|---|---|
| `InitTstep` | `10.0` | :165 | 초기/최대 Δt [10-21 대조 정정] |
| `g` | `9.80655` | :169 | 중력가속도 [10-21 대조 정정] |
| `cfl` | `0.7` | :171 | CFL 계수 [10-21 대조 정정] |
| `DepthThresh` | `1e-3` | :174 | 흐름 계산 수심 하한 [10-21 대조 정정] |
| `MomentumThresh` | `1e-2` | :175 | (Roe) 운동량 갱신 수심 하한 [10-21 대조 정정] |
| `MaxHflow` | `10.0` | :176 | `hflow` 상한(clip) [10-21 대조 정정] |
| `dhlin` | `0.01`→`dx·0.0002` | :180, :468 | diffusive 선형화 임계(Cunge 1980) [10-21 대조 정정] |
| `Qlimfact` | `1.0` | :182 | flux limiter 계수 [10-21 대조 정정] |
| `theta` | `1.0` | :187 | q-centred scheme 가중(θ=1 → Bates 2010 semi-implicit) [10-21 대조 정정] |
| `fricSolver2D` | `ON` | :188 | 2D 마찰(직교 q 벡터 합성) [10-21 대조 정정] |

State 기본값은 `adaptive_ts=ON`·`qlim=OFF`·`acceleration=OFF`·`Roe=OFF`·`diffusive=OFF`이다(`lisflood.cpp:196,209–211,237`). [10-21 대조 정정]
현재 고전 경로의 `drychecking` 기본값은 ON이다(`lisflood.cpp:240`). [10-21 대조 정정]

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
- 활성 조건은 `if(MH>Solverptr->DepthThresh)`이다(`fp_acc.cpp:250`). [10-21 대조 정정]
- 이 조건을 통과하지 않으면 `Solverptr->Tstep=Solverptr->InitTstep;`이다(`fp_acc.cpp:276`). [10-21 대조 정정]
- 실제 CFL 적용은 현재 시간 간격과 위 식의 상한 중 최소값을 쓴다(`fp_acc.cpp:271–272`). [10-21 대조 정정]
- 고전 CPU는 단계별로 초기 상한을 복원한다(`iterateq.cpp:143–146`). [10-21 대조 정정]
- 균일 CUDA ACC의 `dt_field` 후보 이력은 이 CPU 복원과 다르다([cpu-gpu-acc-adaptive의 LG2-008 수정안](../../../_staging/recovery/compare/lisflood-cpu-gpu-acc-adaptive.md#4-노트-대조와-수정안)). [10-21 대조 정정]
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

`user manual +bridge.docx p.48(변환본)` 식 [9]의 분모는 4이다([bridge-docx:LB1-227 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1a.md)). [10-21 대조 정정]
기본 `Qlimfact=1`인 코드의 분모는 8이다(`lisflood.cpp:182`; `fp_flow.cpp:167`). [10-21 대조 정정]
QL 격자는 고정 시간 간격 제한 분기의 부호 있는 유량을 기록한다([files-output:LI2-207 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md)). [10-21 대조 정정]

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
기본 `Roe` 키워드는 `Roe_slow`를 OFF로 지정한다(`pars.cpp:410–428`). [10-21 대조 정정]
별도 `Roe_slow` 키워드는 ghost cell 방식을 선택한다([par:LI1-216 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md)). [10-21 대조 정정]

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
`t==0` 시 adaptive/acceleration/Roe/non-adaptive 모두 `Tstep=MinTstep=InitTstep`(:43-44 등).
IterateQ에는 SGC 초기 `CalcT` 분기가 있다(`iterateq.cpp:79–88`). [10-21 대조 정정]
이 분기는 정상 main의 SGC 진입 경로가 아니다(`lisflood.cpp:775`). [10-21 대조 정정]
정상 SGC는 Fast_MainStart에서 시작한다(`lisflood.cpp:775`). [10-21 대조 정정]

### 6.2 메인 while (`iterateq.cpp:99-439`)

종료 조건은 `while (Solverptr->t < Solverptr->Sim_Time)`이다(`iterateq.cpp:99`). [10-21 대조 정정]
`sim_time`은 시작 시각에 더하는 기간이 아니라 종료 시각의 문턱이다([par:LI1-025 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md)). [10-21 대조 정정]

하도 호출은 `if (Statesptr->ChannelPresent == ON)` 안에서 수행된다(`iterateq.cpp:101–115`). [10-21 대조 정정]
호출 시점은 `if (tstep_counter == -1 || tstep_counter == Solverptr->ts_multiple)`로 정한다(`iterateq.cpp:90–115`). [10-21 대조 정정]
하도 시간 간격은 `tstep_channel = Solverptr->t - Previous_t;`이다(`iterateq.cpp:90–115`). [10-21 대조 정정]
하도는 현재 범람원 CFL 계산 전에 실행된다(`iterateq.cpp:104–146`). [10-21 대조 정정]
BankQ는 첫 호출에서 초기화·복구된 범람원 유량을 읽는다([callflow:RF-009 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md)). [10-21 대조 정정]
이후 호출에서는 직전 범람원 단계의 유량을 읽는다([동일 근거 RF-009](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md)). [10-21 대조 정정]

한 step:

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

`mint_hk`의 고전 적산은 선택된 한 시간간격의 젖은 시간만 더한다(`iterateq.cpp:189–205`). [10-21 대조 정정]
표본 사이의 젖은 시간이 빠질 수 있는 결함 후보 강도는 중간이다([bridge-docx:LB1-374 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md)). [10-21 대조 정정]

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
| Δt | `cfl·dx/√(gH)` (`:271`) | `0.25·dy²/α` (`fp_flow.cpp:160`) | `cfl·dx/(\|u\|+√(gH))` (`:946`) |
| q 갱신 | `UpdateQs` (`:307`) | (없음) | `UpdateQsRoe` (`:994`) |
| 안정성 출처 | 수심만(파속) | diffusion number | 유속+파속 (CFL) |
| 비용 | 저 | 저 | 고 |

확산파 해법은 국소 가속도와 이류 가속도를 생략한다(user manual.pdf p.10 표 1). ACC는 이류 가속도를 생략한다(user manual.pdf p.10 표 1). Roe·FV1·DG2는 완전 천수방정식 해법이다(user manual.docx p.13(변환본) 표 1). 해법별 설명은 [architecture source map](lisflood-fp-architecture-source-map.md) §2–3에 있다. ACC의 q 중심식은 θ=1일 때 Bates et al.(2010)의 semi-implicit 식과 같다(`fp_acc.cpp:88,93–94`). [10-21 전수 검증 정정]

## 문서와 코드 차이 (10-21 대조)

문서 판: 2013 PDF 매뉴얼은 표지 Code release 6.1.1, 2013-11-25이다. user manual.docx p.5(변환본)의 판 이력 맨 위에는 밑줄로 추가한 8.0이 있다. user manual +bridge.docx는 Code release 4.3.6, 2008-04-25이다. 코드 판: Zenodo 8.2(10.5281/zenodo.13121102)에 공식 8.3 패치(10.5281/zenodo.13121119)를 적용했다. `VersionHistory.h:16–23`의 숫자 판은 8.1.0이다. 릴리스 이름은 8.3이다. [10-21 전수 검증 정정]

코드 인용의 기준 디렉터리는 [LISFLOOD-FP 원자료](../raw/source_code/LISFLOOD-FP/)이다. `v8.0:`·`v8.1:`·`v8.2:`는 이전 배포본을 가리킨다. `bf804e23:`는 반영 전 노트의 커밋과 줄을 가리킨다.

최종 분류와 결론 문장은 [최종 결론 배정](../../../_staging/recovery/assign/LISFLOOD-FP-final-conclusions.tsv)에 지정된 같은 행 ID의 근거를 따른다. 분류는 A 판 차이, B 문서 오기, C 문서 누락, D 문서에만 있음, E 코드 결함 후보, F 표기 차이이다.

행별 최종 근거: [LB1a](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1a.md), [LB1b](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md), [LN1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LN1.md), [RF](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md), [LV1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md), [LI2](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md), [LI1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md), [LT1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LT1.md).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| bridge-docx:LB1-080 | user manual +bridge.docx p.7·22(변환본) `resettimeinit`; 지정 초에서 초기 침수 계수기를 `zero`로 재설정 | user manual +bridge.docx p.7·22(변환본) `resettimeinit`; 지정 초에서 초기 침수 계수기를 `zero`로 재설정 | `pars.cpp:575` `if (read_numeric_param(param_name, line_number, param_value_ptr, "resettimeinit", &Parptr->reset_timeinit_time, verbose, mode))`; `iterateq.cpp:177–185` 조건 `if ((Statesptr->reset_timeinit == ON) & (Solverptr->t>Parptr->reset_timeinit_time))`과 대입 `Arrptr->initHtm[ptr] = (NULLVAL);`; `lisflood.h:128` `#define NULLVAL C(-9999.0) // MT: define ascii file NULL value as constant`; 8.0 대조: `v8.0:pars.cpp:564` `if (read_numeric_param(param_name, line_number, param_value_ptr, "resettimeinit", &Parptr->reset_timeinit_time, verbose, mode))`<br>확인한 원문: user manual +bridge.docx p.1·7·22(변환본); `pars.cpp:575–579`; `iterateq.cpp:177–199`; `lisflood.h:128`; `VersionHistory.h:438–442`; `v8.0:iterateq.cpp:177–199` | A 판 차이 | 8.0 이전 판(4.3.6) 기준, 그 판 코드는 배포본이 없다. v8.0과 현재 고전 경로는 `if ((Statesptr->reset_timeinit == ON) & (Solverptr->t>Parptr->reset_timeinit_time))`에서 `Arrptr->initHtm[ptr] = (NULLVAL);`을 실행한다. `NULLVAL`은 `C(-9999.0)`이다. 이후 `if (Solverptr->t >= Parptr->MassTotal \|\| Statesptr->mint_hk == OFF)`의 진단 갱신에서 `if (Arrptr->H[ptr] > Solverptr->DepthThresh)`와 미침수 표지 조건을 만족하면 `Arrptr->initHtm[ptr] = Solverptr->t / C(3600.0);`을 실행한다. |
| bridge-docx:LB1-085 | user manual +bridge.docx p.22–23(변환본) `qloutput`; `calculated by the adaptive time stepping routine using equation [8]` | user manual +bridge.docx p.22–23(변환본) `qloutput`; `calculated by the adaptive time stepping routine using equation [8]` | `pars.cpp:443–445` `if (read_empty_param(param_name, line_number, param_value_ptr, "qloutput", verbose, mode))` / `{` / `Statesptr->save_QLs = ON;`; `lisflood.cpp:229` `SimStates.save_QLs = OFF;`; `fp_flow.cpp:158–167`의 `if(Statesptr->adaptive_ts==ON)` 뒤 `else`에서 `Qlim=Solverptr->Qlimfact*Parptr->dA*fabs(dh)/(8*Solverptr->Tstep);`; 8.0 대조: `v8.0:pars.cpp:432` `if (read_empty_param(param_name, line_number, param_value_ptr, "qloutput", verbose, mode))`; `v8.0:lisflood.cpp:219` `SimStates.save_QLs = OFF;`<br>확인한 원문: user manual +bridge.docx p.22–23·48–50(변환본); user manual.pdf p.21; `pars.cpp:443–446`; `lisflood.cpp:229`; `fp_flow.cpp:158–174`; `v8.0:pars.cpp:432–434` | B 문서 오기 | 제한값은 적응 경로의 반대 분기에서 계산한다. 식 [8]은 Manning 유량이며 제한식은 [9]이다. user manual.pdf p.21의 적용 해법 칸은 `2D fixed timestep`으로 바꾼다. |
| bridge-docx:LB1-183 | user manual +bridge.docx p.6(변환본) Version 3.4.0의 매 저장 때 남은 시간 추정 출력; 분 단위 `M C M/C ETot EFin` | user manual +bridge.docx p.6(변환본) Version 3.4.0의 매 저장 때 남은 시간 추정 출력; 분 단위 `M C M/C ETot EFin` | `iterateq.cpp:329–335` `Comp_time = (NUMERIC_TYPE)difftime(Solverptr->time_check, Solverptr->time_start) / 60;` / `if (Comp_time != 0 && Statesptr->comp_out == ON) // only of t is not zero (can't divide by zero)` / `{` / `Model_Comp_Ratio = ((Solverptr->t / 60) / Comp_time);` / `Model_time_left = (Solverptr->Sim_Time - Solverptr->t) / 60;` / `Est_Time_Fin = (Model_time_left / Model_Comp_Ratio);` / `Est_Time_Tot = Comp_time + Est_Time_Fin;`<br>확인한 원문: user manual +bridge.docx p.1·6·36(변환본); `VersionHistory.h:332–341`; `lisflood.cpp:234`; `iterateq.cpp:325–336` | A 판 차이 | 8.0 이전 판(4.3.6에 수록된 3.4.0 변경 목록) 기준, 그 판 코드는 배포본이 없다. 3.4.1 이력은 시간 추정 출력을 `comp_out` 선택 옵션으로 바꿨다고 기록한다. 현재 기본값은 OFF이다. 저장 시점의 출력 조건은 `if (Comp_time != 0 && Statesptr->comp_out == ON)`이다. 출력 시간의 단위는 분이다. |
| bridge-docx:LB1-227 | user manual +bridge.docx p.48(변환본) [9] `Q_x^{i,j}=\min\left(Q_x^{i,j},\frac{\Delta x\,\Delta y(h^{i,j}-h^{i-1,j})}{4\Delta t}\right)` | user manual +bridge.docx p.48(변환본) [9] `Q_x^{i,j}=\min\left(Q_x^{i,j},\frac{\Delta x\,\Delta y(h^{i,j}-h^{i-1,j})}{4\Delta t}\right)` | `fp_flow.cpp:167–174` `Qlim=Solverptr->Qlimfact*Parptr->dA*fabs(dh)/(8*Solverptr->Tstep);` / `if(fabs(Q)>Qlim)` / `{` / `if(Q>0) Q=Qlim;` / `if(Q<0) Q=-Qlim;` / `// MT added to record Qlim` / `Arrptr->LimQx[pTQ]=Q;` / `}`<br>확인한 원문: user manual +bridge.docx p.48(변환본) 식 [8]·[9]; `lisflood.cpp:182`; `fp_flow.cpp:164–174` | B 문서 오기 | 기본 Qlimfact=1에서 분모는 8이다. 문서 분모는 4이다. 코드의 제한 크기는 절댓값이며 원래 유량 부호를 유지한다. 문서 [8]의 양의 수면차 조건을 [9]에 넣으면 제한항이 음수가 된다. 문서 식은 자체 부호와도 충돌한다. |
| bridge-docx:LB1-234 | user manual +bridge.docx p.50(변환본) [16] `\Delta t=\frac{\Delta x^2}{4}\min\left(\frac{2n}{h_{flow}^{5/3}}\left\lvert\frac{\partial h}{\partial x}\right\rvert^{1/2},\frac{2n}{h_{flow}^{5/3}}\left\lvert\frac{\partial h}{\partial y}\right\rvert^{1/2}\right)` | user manual +bridge.docx p.50(변환본) [16] `\Delta t=\frac{\Delta x^2}{4}\min\left(\frac{2n}{h_{flow}^{5/3}}\left\lvert\frac{\partial h}{\partial x}\right\rvert^{1/2},\frac{2n}{h_{flow}^{5/3}}\left\lvert\frac{\partial h}{\partial y}\right\rvert^{1/2}\right)` | `fp_flow.cpp:155` `else alpha=pow(hflow,(C(5.0)/C(3.0)))/(C(2.)*fn*Sf);`; 160행 `*TSptr=getmin(*TSptr,(C(0.25)*Parptr->dy*Parptr->dy/alpha));`; 65행 `Solverptr->Tstep=getmin(Solverptr->Tstep,ThreadTS);`<br>확인한 원문: user manual +bridge.docx p.49–50(변환본) 식 [14]–[16]; `input.cpp:1488–1489`; `iterateq.cpp:143–146`; `fp_flow.cpp:27–65,139–160,179–201,271–276` | F 표기 차이 | 정사각 격자 `dx=dy`의 비선형 분기는 식 [16]과 같은 표기이다. `if(dh<Solverptr->dhlin)`의 else에서 `alpha=pow(hflow,(C(5.0)/C(3.0)))/(C(2.)*fn*Sf);`를 쓴다. 적응 시간간격은 `*TSptr=getmin(*TSptr,(C(0.25)*Parptr->dy*Parptr->dy/alpha));`로 줄인다. x·y의 계산 대상 경계에서 최소값을 취한다. 초기 상한도 유지한다. |
| bridge-docx:LB1-237 | user manual +bridge.docx p.50(변환본) [17] `q_x=\frac{h_{flow}^{5/3}}n\left(\frac{\Delta x}{h_{lin}}\right)^{1/2}\left(\frac{\partial h}{\partial x}\right)` | user manual +bridge.docx p.50(변환본) [17] `q_x=\frac{h_{flow}^{5/3}}n\left(\frac{\Delta x}{h_{lin}}\right)^{1/2}\left(\frac{\partial h}{\partial x}\right)` | `fp_flow.cpp:152` `Sf=sqrt(Parptr->dx/Solverptr->dhlin)*(dh/Parptr->dx);`; 157행 `Q=(pow(hflow,(C(5.0)/C(3.0)))*Sf*Parptr->dy/fn);`<br>확인한 원문: user manual +bridge.docx p.49–50(변환본) 식 [11]·[17]; `input.cpp:1488–1489`; `fp_flow.cpp:139–157,179–198,258–273,296–315` | F 표기 차이 | 정사각 격자의 선형 분기는 단위폭 유량의 크기로 비교하면 식 [17]과 같다. 조건은 `if(dh<Solverptr->dhlin)`이다. `Sf=sqrt(Parptr->dx/Solverptr->dhlin)*(dh/Parptr->dx);`를 쓴다. 양의 x 유량은 `Q=(pow(hflow,(C(5.0)/C(3.0)))*Sf*Parptr->dy/fn);`이다. 반대 방향 분기는 음의 Q를 계산한다. 문서의 `h_{lin}`은 코드의 `dhlin`에 대응한다. 선형 alpha에는 비선형 alpha의 1/2가 없다. |
| bridge-docx:LB1-272 | bridge판에 없는 `steady` | user manual +bridge.docx p.21–24(변환본) 표 5<br>bridge판에 없는 `steady` | `pars.cpp:259` `if (read_empty_param(param_name, line_number, param_value_ptr, "steady", verbose, mode))` / `pars.cpp:261` `Statesptr->steadycheck = ON;`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5; `pars.cpp:259` `if (read_empty_param(param_name, line_number, param_value_ptr, "steady", verbose, mode))` / `pars.cpp:261` `Statesptr->steadycheck = ON;` | C 문서 누락 | 논리 키워드를 읽는다. |
| bridge-docx:LB1-273 | bridge판에 없는 `steadytol` | user manual +bridge.docx p.21–24(변환본) 표 5<br>bridge판에 없는 `steadytol` | `pars.cpp:264` `if (read_numeric_param(param_name, line_number, param_value_ptr, "steadytol", &Parptr->steadyQtol, verbose, mode))`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5; `pars.cpp:264` `if (read_numeric_param(param_name, line_number, param_value_ptr, "steadytol", &Parptr->steadyQtol, verbose, mode))` | C 문서 누락 | 실수 입력을 읽는다. 읽기 대상은 `Parptr->steadyQtol`이다. |
| bridge-docx:LB1-275 | bridge판에 없는 `acceleration` | user manual +bridge.docx p.21–24(변환본) 표 5<br>bridge판에 없는 `acceleration` | `pars.cpp:307` `if (read_empty_param(param_name, line_number, param_value_ptr, "acceleration", verbose, mode))` / `pars.cpp:309` `Statesptr->acceleration = ON;` / `pars.cpp:310` `Statesptr->adaptive_ts = OFF;` / `pars.cpp:311` `Statesptr->qlim = OFF;`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5; `pars.cpp:307` `if (read_empty_param(param_name, line_number, param_value_ptr, "acceleration", verbose, mode))` / `pars.cpp:309` `Statesptr->acceleration = ON;` / `pars.cpp:310` `Statesptr->adaptive_ts = OFF;` / `pars.cpp:311` `Statesptr->qlim = OFF;` | C 문서 누락 | 논리 키워드를 읽는다. |
| bridge-docx:LB1-284 | bridge판에 없는 `Roe` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `Roe` | `pars.cpp:410` `if (read_empty_param(param_name, line_number, param_value_ptr, "Roe", verbose, mode))` / `pars.cpp:412` `Statesptr->Roe = ON;` / `pars.cpp:413` `Statesptr->Roe_slow = OFF;` / `pars.cpp:414` `Statesptr->adaptive_ts = OFF;` / `pars.cpp:415` `Statesptr->acceleration = OFF;`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:410` `if (read_empty_param(param_name, line_number, param_value_ptr, "Roe", verbose, mode))` / `pars.cpp:412` `Statesptr->Roe = ON;` / `pars.cpp:413` `Statesptr->Roe_slow = OFF;` / `pars.cpp:414` `Statesptr->adaptive_ts = OFF;` / `pars.cpp:415` `Statesptr->acceleration = OFF;` | C 문서 누락 | 논리 키워드를 읽는다. |
| bridge-docx:LB1-285 | bridge판에 없는 `Roe_slow` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `Roe_slow` | `pars.cpp:420` `if (read_empty_param(param_name, line_number, param_value_ptr, "Roe_slow", verbose, mode))` / `pars.cpp:422` `Statesptr->Roe_slow = ON; // uses ghost cell version of Roe solver.` / `pars.cpp:423` `Statesptr->Roe = ON;` / `pars.cpp:424` `Statesptr->adaptive_ts = OFF;` / `pars.cpp:425` `Statesptr->acceleration = OFF;`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:420` `if (read_empty_param(param_name, line_number, param_value_ptr, "Roe_slow", verbose, mode))` / `pars.cpp:422` `Statesptr->Roe_slow = ON; // uses ghost cell version of Roe solver.` / `pars.cpp:423` `Statesptr->Roe = ON;` / `pars.cpp:424` `Statesptr->adaptive_ts = OFF;` / `pars.cpp:425` `Statesptr->acceleration = OFF;` | C 문서 누락 | 논리 키워드를 읽는다. |
| bridge-docx:LB1-305 | bridge판에 없는 `theta` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `theta` | `pars.cpp:651` `if (read_numeric_param(param_name, line_number, param_value_ptr, "theta", &Solverptr->theta, verbose, mode))`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:651` `if (read_numeric_param(param_name, line_number, param_value_ptr, "theta", &Solverptr->theta, verbose, mode))` | C 문서 누락 | 실수 입력을 읽는다. 읽기 대상은 `Solverptr->theta`이다. |
| bridge-docx:LB1-306 | bridge판에 없는 `1Dfriction` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `1Dfriction` | `pars.cpp:663` `if (read_empty_param(param_name, line_number, param_value_ptr, "1Dfriction", verbose, mode))` / `pars.cpp:665` `Solverptr->fricSolver2D = OFF;`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:663` `if (read_empty_param(param_name, line_number, param_value_ptr, "1Dfriction", verbose, mode))` / `pars.cpp:665` `Solverptr->fricSolver2D = OFF;` | C 문서 누락 | 논리 키워드를 읽는다. |
| bridge-docx:LB1-313 | bridge판에 없는 `momentumthresh` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `momentumthresh` | `pars.cpp:728` `if (read_numeric_param(param_name, line_number, param_value_ptr, "momentumthresh", &Solverptr->MomentumThresh, verbose, mode))`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:728` `if (read_numeric_param(param_name, line_number, param_value_ptr, "momentumthresh", &Solverptr->MomentumThresh, verbose, mode))` | C 문서 누락 | 실수 입력을 읽는다. 읽기 대상은 `Solverptr->MomentumThresh`이다. |
| bridge-docx:LB1-314 | bridge판에 없는 `drycheckoff` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `drycheckoff` | `pars.cpp:733` `if (read_empty_param(param_name, line_number, param_value_ptr, "drycheckoff", verbose, mode))` / `pars.cpp:735` `Statesptr->drychecking = OFF;`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:733` `if (read_empty_param(param_name, line_number, param_value_ptr, "drycheckoff", verbose, mode))` / `pars.cpp:735` `Statesptr->drychecking = OFF;` | C 문서 누락 | 논리 키워드를 읽는다. |
| bridge-docx:LB1-374 | mint_hk와 총 침수시간 적산 | user manual +bridge.docx p.23·38(변환본); user manual.pdf p.37–38<br>mint_hk와 총 침수시간 적산 | `iterateq.cpp:189–190` `// Update maxH, maxHtm, totalHtm and initHtm at the mass interval if mint_hk is specifed in the .par file OR at every time step if not` / `if (Solverptr->t >= Parptr->MassTotal \|\| Statesptr->mint_hk == OFF)`; 201행 `Arrptr->totalHtm[ptr] += Solverptr->Tstep / C(3600.0);`; `lisflood2/sgm_fast.cpp:3928–3931` `if (time_next >= Parptr->MassTotal \|\| Statesptr->mint_hk == OFF)` / `{` / `NUMERIC_TYPE delta_time_hours = delta_time / C(3600.0);` / `NUMERIC_TYPE current_time_hours = time_next / C(3600.0);`; 3192행 `totalHtm_grid[index] += delta_time_hours;`<br>확인한 원문: user manual +bridge.docx p.23·38(변환본); user manual.pdf p.37–38; `iterateq.cpp:189–205,265`; `lisflood2/sgm_fast.cpp:3187–3192,3928–3947`; `VersionHistory.h:301–302`; `v8.0:iterateq.cpp:189–201` | E 코드 결함 후보(중간) | 해석: E 후보, 근거 강도 중간. mint_hk는 의도적으로 통계 갱신 빈도를 줄인다. 고전 경로의 조건은 `if (Solverptr->t >= Parptr->MassTotal \|\| Statesptr->mint_hk == OFF)`이다. 젖은 셀에 더하는 값은 `Arrptr->totalHtm[ptr] += Solverptr->Tstep / C(3600.0);`이다. Fast도 `if (time_next >= Parptr->MassTotal \|\| Statesptr->mint_hk == OFF)`에서 `NUMERIC_TYPE delta_time_hours = delta_time / C(3600.0);`을 넘긴다. 누적식은 `totalHtm_grid[index] += delta_time_hours;`이다. MassInt가 여러 시간간격을 포함하면 표본 사이의 젖은 시간이 빠질 수 있다. |
| bridge-docx:LB1-422 | user manual +bridge.docx p.36(변환본) 계산 시간 추정을 verbose 모드와 comp_out으로 출력한다는 설명 | user manual +bridge.docx p.36(변환본) 계산 시간 추정을 verbose 모드와 comp_out으로 출력한다는 설명 | `iterateq.cpp:330` `if (Comp_time != 0 && Statesptr->comp_out == ON) // only of t is not zero (can't divide by zero)`<br>확인한 원문: user manual +bridge.docx p.1·36(변환본); user manual.pdf p.1·34–35; `iterateq.cpp:325–336` | A 판 차이 | 현재 고전 경로는 `if (Solverptr->t >= Parptr->SaveTotal)` 안에서 계산 시간을 갱신한다. 추정 출력의 안쪽 조건은 `if (Comp_time != 0 && Statesptr->comp_out == ON)`이다. verbose는 이 출력의 조건이 아니다. user manual.pdf p.34도 comp_out만 적는다. user manual +bridge.docx p.36(변환본)의 M/C=94.94를 100이라고 설명한 수치는 근사값이다. 8.0 이전 판(4.3.6) 기준, 그 판 코드는 배포본이 없다. |
| build-83:LN1-240 | classic FV1 분기 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-classic-acc-flow.md:46` ``\| `Statesptr->fv1==ON` \| `fv1::solve(...)` (:777) \| full SWE FV1 \|`` | 현재 `lisflood.cpp:780–788`·`../LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch:282–295`·노트 작성일 `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-classic-acc-flow.md:9` `note_date: 2026-06-18`<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-classic-acc-flow.md:9,39–48`; `v8.2:lisflood.cpp:775–778`; `lisflood.cpp:419–459,778–788`; `../LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch:282–295` | A 판 차이 | v8.2의 CPU FV1 설명에 8.3의 Metal 조건부 호출을 추가한다. CUDA 분기를 지나지 않은 현재 FV1 실행도 Metal을 선택할 수 있다. |
| callflow:RF-008 | 시간 간격의 역수 비례 표기 | user manual.pdf p.11·15; user manual.docx p.14(변환본) 쪽 이미지 | user manual.pdf p.11 및 user manual.docx p.14(변환본)의 `scales with 1/∆t`, `scales with (1/∆x)2`; user manual.pdf p.15의 `reduces quadratically with grid size`·`linearly with the ‘acceleration’ model`; `fp_acc.cpp:271` `locT=cfl*Parptr->dx/(sqrt(g*MH));`; `fp_flow.cpp:160` `*TSptr=getmin(*TSptr,(C(0.25)*Parptr->dy*Parptr->dy/alpha));`. 쪽 이미지를 확인했다.<br>확인한 원문: user manual.pdf p.11·15; user manual.docx p.14(변환본) 쪽 이미지; `fp_acc.cpp:249–272`; `fp_flow.cpp:149–160` | B 문서 오기 | ACC의 CFL 식은 고정 수심에서 격자 폭에 비례한다. 원문은 `locT=cfl*Parptr->dx/(sqrt(g*MH));`이다. Manning 확산식의 시간 간격 제한은 `*TSptr=getmin(*TSptr,(C(0.25)*Parptr->dy*Parptr->dy/alpha));`이다. Manning 확산식의 분자는 격자 폭의 제곱이다. 매뉴얼의 역수 표기를 시간 간격 식으로 옮기지 않는다. |
| callflow:RF-009 | 하도·범람원의 단계 사이 지연 | user manual.pdf p.19; user manual.docx p.23(변환본); user manual +bridge.docx p.23(변환본) 쪽 이미지 | user manual.pdf p.19·user manual.docx p.23(변환본) `Decouples the channel and floodplain time step and increases the channel timestep.`; `iterateq.cpp:102` `// ChannelQ routine is run using Tstep calculated for previous iteration`; `ch_flow.cpp:514–520`의 Qx·Qy 읽기; `iterateq.cpp:146`의 뒤따르는 FloodplainQ.<br>확인한 원문: user manual.pdf p.19; user manual.docx p.23(변환본); user manual +bridge.docx p.23(변환본) 쪽 이미지; `iterateq.cpp:90–115,143–146`; `ch_flow.cpp:413–422,505–524,807–812` | C 문서 누락 | 하도 호출은 `if (Statesptr->ChannelPresent == ON)` 안에서 수행된다. 호출 시점은 `if (tstep_counter == -1 \|\| tstep_counter == Solverptr->ts_multiple)`로 정한다. 하도 시간 간격은 `tstep_channel = Solverptr->t - Previous_t;`이다. 하도는 현재 범람원 계산 전에 실행된다. BankQ는 첫 호출에서 초기화·복구된 범람원 유량을 읽는다. 이후 호출에서는 직전 범람원 단계의 유량을 읽는다. |
| docx-manual:LV1-016 | user manual.docx p.14(변환본) `the stable time step scales with` `(1/\Delta x)^2`. | user manual.docx p.14·19(변환본) 표 4; user manual.pdf p.11·15<br>user manual.docx p.14(변환본) `the stable time step scales with` `(1/\Delta x)^2`.<br>user manual.pdf p.11과 같음. | `fp_flow.cpp:160` `*TSptr=getmin(*TSptr,(C(0.25)*Parptr->dy*Parptr->dy/alpha));`<br>확인한 원문: user manual.docx p.14·19(변환본) 표 4; user manual.pdf p.11·15; `fp_flow.cpp:160`; `v8.0:fp_flow.cpp:154` | B 문서 오기 | 같은 문서 p.19는 격자 크기가 줄면 시간 간격도 제곱으로 줄어든다고 적는다. 인쇄된 역제곱은 그 문장과 반대다. 확산계수를 고정한 비교에서는 코드의 격자 길이가 분자에 제곱으로 들어간다. |
| docx-manual:LV1-017 | user manual.docx p.14(변환본) acceleration의 안정 시간 간격은 `1/\Delta t`에 비례한다고 적는다. | user manual.docx p.14·19(변환본) 표 4; user manual.pdf p.11·15<br>user manual.docx p.14(변환본) acceleration의 안정 시간 간격은 `1/\Delta t`에 비례한다고 적는다.<br>user manual.pdf p.11과 같음. | `fp_acc.cpp:270–272`: `// Time step control for stability from actual equations (MSH, implemented by TJF)`<br>`locT=cfl*Parptr->dx/(sqrt(g*MH));`<br>`Solverptr->Tstep=getmin(Solverptr->Tstep,locT);`<br>확인한 원문: user manual.docx p.14·19(변환본) 표 4; user manual.pdf p.11·15; `fp_acc.cpp:270–272`; `v8.0:fp_acc.cpp:247` | B 문서 오기 | 코드의 CFL 시간 간격은 셀 크기에 선형으로 비례한다. 문서 p.19의 선형 감소 설명도 이를 지지한다. |
| docx-manual:LV1-185 | user manual.docx p.39(변환본) `-steady`, 기본 허용차 `0.0005\,\mathrm{m^3s^{-1}}`. `-steadytol`은 이를 바꾼다. | user manual.docx p.39(변환본); user manual.pdf p.34<br>user manual.docx p.39(변환본) `-steady`, 기본 허용차 `0.0005\,\mathrm{m^3s^{-1}}`. `-steadytol`은 이를 바꾼다.<br>user manual.pdf p.34와 같음. | `pars.cpp:259–261`의 `"steady"`, `Statesptr->steadycheck = ON;`; `pars.cpp:264` `if (read_numeric_param(param_name, line_number, param_value_ptr, "steadytol", &Parptr->steadyQtol, verbose, mode))`; `lisflood.cpp:127` `Params.steadyQtol = C(0.0005); // tolerance for steady-state definition`<br>확인한 원문: user manual.docx p.39(변환본); user manual.pdf p.34; `pars.cpp:259–264`; `lisflood.cpp:127–129`; `iterateq.cpp:426–436` | C 문서 누락 | 정상상태 판정은 `if (fabs(Parptr->steadyQdiff)<Parptr->steadyQtol)`를 10회 연속 충족해야 한다. 기본 검사 간격은 1800 s다. 기본 허용차는 0.0005 m³/s다. |
| docx-manual:LV1-271 | classic adaptive·flow limiter의 실제 식. | user manual.docx p.14(변환본); user manual.pdf p.11<br>classic adaptive·flow limiter의 실제 식. | `fp_flow.cpp:157` `Q=(pow(hflow,(C(5.0)/C(3.0)))*Sf*Parptr->dy/fn);`; `fp_flow.cpp:160`의 `C(0.25)*Parptr->dy*Parptr->dy/alpha`; `fp_flow.cpp:167` `Qlim=Solverptr->Qlimfact*Parptr->dA*fabs(dh)/(8*Solverptr->Tstep);`<br>확인한 원문: user manual.docx p.14(변환본); user manual.pdf p.11; `fp_flow.cpp:157–168` | C 문서 누락 | 문서는 해법 이름·시간 간격 변화 경향을 적는다. 실제 1/4·1/8 계수와 국소 유량 제한식을 생략한다. dhlin 분기는 같은 함수의 LV1-090을 참조한다. |
| docx-manual:LV1-272 | acceleration CFL의 실제 식과 상한. | user manual.docx p.14(변환본); user manual.pdf p.11<br>acceleration CFL의 실제 식과 상한. | `fp_acc.cpp:271–276`: `locT=cfl*Parptr->dx/(sqrt(g*MH));` / `Solverptr->Tstep=getmin(Solverptr->Tstep,locT);` 이후 건조 영역은 `Solverptr->Tstep=Solverptr->InitTstep;`다.<br>확인한 원문: user manual.docx p.14(변환본); user manual.pdf p.11; `fp_acc.cpp:246–276` | C 문서 누락 | `if(MH > Solverptr->DepthThresh)`이면 `locT=cfl*Parptr->dx/(sqrt(g*MH));`를 계산한다. 이어 `Solverptr->Tstep=getmin(Solverptr->Tstep,locT);`를 적용한다. 그 외에는 `Solverptr->Tstep=Solverptr->InitTstep;`이다. 바로 앞의 주석 처리된 CFL 식은 활성 구현이 아니다. |
| files-output:LI2-207 | QL 배열의 실제 의미 | user manual.pdf p.38–39<br>user manual.pdf p.38 제목 `Adaptive time step and flow limiter (-xxxx.QLx and -xxxx.QLy) values` | `fp_flow.cpp:199–214`의 adaptive 분기 `Arrptr->TRecx[pTQ]=*TSptr;`와 else 분기 `Qlim=Solverptr->Qlimfact*Parptr->dA*fabs(dh)/(8*Solverptr->Tstep);`, `if(fabs(Q)>Qlim)`, `Arrptr->LimQx[pTQ]=Q;`<br>확인한 원문: user manual.pdf p.38–39; `fp_flow.cpp:208–215`; `output.cpp:979–981` | C 문서 누락 | QL은 적응 시간 간격 배열이 아니다. 제한 분기에서 기록한 부호 있는 유량이다. |
| files-output:LI2-327 | 추가 계산 선택·문턱 | user manual.pdf p.16·19–20 | `pars.cpp:210`, `216`, `410`, `420`, `663`, `679`, `728`, `733`, `863`의 `"qlimfact"`, `"ts_multiple"`, `"Roe"`, `"Roe_slow"`, `"1Dfriction"`, `"depththresh"`, `"momentumthresh"`, `"drycheckoff"`, `"gravity"`; `lisflood.cpp:174–175` `ParSolver.DepthThresh = C(1e-3);`<br>`ParSolver.MomentumThresh = C(1e-2);`; `lisflood.cpp:169` `ParSolver.g = C(9.8065500000000);`<br>확인한 원문: user manual.pdf p.16·19–20; `pars.cpp:210–219,410–428,663–683,728–739,863–869` | C 문서 누락 | 열거한 일반 해법·임계값 옵션은 문서 p.16·19–20에 있다. 별도 Roe_slow 키워드는 ghost cell 방식의 Roe 해법을 선택한다. |
| par:LI1-025 | sim_time과 tstart의 결합 | user manual.pdf p.16<br>user manual.pdf p.16 `Total length of the simulation in seconds (real value).`; `Default: 3600`; `All solvers` | `pars.cpp:198` `if (read_numeric_param(param_name, line_number, param_value_ptr, "sim_time", &Solverptr->Sim_Time, verbose, mode) \|\|`<br>`pars.cpp:199` `read_numeric_param(param_name, line_number, param_value_ptr, "simtime", &Solverptr->Sim_Time, verbose, mode))`<br>`lisflood.cpp:164` `ParSolver.Sim_Time = C(3600.0);`<br>`iterateq.cpp:99` `while (Solverptr->t < Solverptr->Sim_Time)`<br>확인한 원문: user manual.pdf p.16; `pars.cpp:198–199,855–862`; `lisflood.cpp:164`; `iterateq.cpp:99`; `pars.cpp:855–861`; `iterateq.cpp:99,174` | C 문서 누락 | 고전 CPU 반복의 종료 조건은 `while (Solverptr->t < Solverptr->Sim_Time)`이다. sim_time은 시작 시각에 더하는 기간이 아니라 종료 시각의 문턱이다. tstart가 0이 아니면 요청한 시간 구간은 sim_time과 tstart의 차이이다. |
| par:LI1-097 | drycheck의 기본 상태 | user manual.pdf p.19; user manual.pdf p.1<br>user manual.pdf p.19 drycheckon·drycheckoff 두 행 `Default: drycheck is off` | LI1-098, LI1-099<br>`lisflood.cpp:240` `SimStates.drychecking = ON;`<br>`iterateq.cpp:150` `if (Statesptr->drychecking == ON) DryCheck(Parptr, Solverptr, Arrptr);`<br>확인한 원문: user manual.pdf p.19; `lisflood.cpp:240`; `iterateq.cpp:150`; `v8.0:lisflood.cpp:230`; `v8.1:lisflood.cpp:236`; `VersionHistory.h:246–247`; user manual.pdf p.1; `VersionHistory.h:244–247`; `v8.0:lisflood.cpp:230`; `v8.1:lisflood.cpp:236`; `v8.2:lisflood.cpp:237` | A 판 차이 | 8.0 이전 판(문서 표지 6.1.1·머리글 5.9.6) 기준, 그 판 코드는 배포본이 없다. PDF는 drycheck 기본값을 OFF로 적는다. 현재 drychecking 기본값은 ON이다. |
| par:LI1-110 | `momentumthresh value` | user manual.pdf p.20; user manual.pdf p.1<br>user manual.pdf p.20 `threshold for the momentum equation used by the Roe solver.`; `Default: 0.001` | `pars.cpp:728` `if (read_numeric_param(param_name, line_number, param_value_ptr, "momentumthresh", &Solverptr->MomentumThresh, verbose, mode))`<br>`pars.cpp:729` `{`<br>`pars.cpp:730` `if (verbose == ON) printf("Momentum threshold changed to %" NUM_FMT" \n", Solverptr->MomentumThresh);`<br>`pars.cpp:731` `return;`<br>`pars.cpp:732` `}`<br>`lisflood.cpp:175` `ParSolver.MomentumThresh = C(1e-2);`<br>`fp_trent.cpp:987` `if(Arrptr->H[pc] > Solverptr->MomentumThresh)`<br>확인한 원문: user manual.pdf p.20; `pars.cpp:728–732`; `lisflood.cpp:175`; `fp_trent.cpp:987`; `v8.0:lisflood.cpp:168`; `v8.1:lisflood.cpp:171`; user manual.pdf p.1; `VersionHistory.h:225–226`; `v8.0:lisflood.cpp:168`; `v8.1:lisflood.cpp:171`; `v8.2:lisflood.cpp:172` | A 판 차이 | 8.0 이전 판(문서 표지 6.1.1·머리글 5.9.6) 기준, 그 판 코드는 배포본이 없다. PDF의 momentumthresh 기본값은 0.001이다. 현재 기본값은 0.01m이다. |
| par:LI1-125 | `resettimeinit value` | user manual.pdf p.20; user manual.pdf p.1<br>user manual.pdf p.20 `Resets the time of initial inundation counter to zero at a specified time`; 초; `Default: 0` | `pars.cpp:575` `if (read_numeric_param(param_name, line_number, param_value_ptr, "resettimeinit", &Parptr->reset_timeinit_time, verbose, mode))`<br>`pars.cpp:576` `{`<br>`pars.cpp:577` `Statesptr->reset_timeinit = ON;`<br>`pars.cpp:578` `if (verbose == ON) printf("\n Time of initial inundation will be reset at %" NUM_FMT" seconds\n", Parptr->reset_timeinit_time);`<br>`pars.cpp:579` `return;`<br>`pars.cpp:580` `}`<br>`lisflood.cpp:124` `Params.reset_timeinit_time = 0;`<br>`lisflood.cpp:224` `SimStates.reset_timeinit = OFF;`<br>`iterateq.cpp:177` `if ((Statesptr->reset_timeinit == ON) & (Solverptr->t>Parptr->reset_timeinit_time))`<br>`iterateq.cpp:178` `{ //reset the time of initial inundation if called for in parameter file`<br>`iterateq.cpp:179` `Statesptr->reset_timeinit = OFF;`<br>`iterateq.cpp:180` (빈 줄)<br>`iterateq.cpp:181` `//#pragma omp parallel for private(j,ptr) // irrelevent benefit JCN`<br>`iterateq.cpp:182` `for (j = 0; j<Parptr->ysz; j++) for (i = 0; i<Parptr->xsz; i++)`<br>`iterateq.cpp:183` `{`<br>`iterateq.cpp:184` `ptr = i + j*Parptr->xsz;`<br>`iterateq.cpp:185` `Arrptr->initHtm[ptr] = (NULLVAL);`<br>확인한 원문: user manual.pdf p.20; `pars.cpp:575–580`; `lisflood.cpp:124,224`; `iterateq.cpp:177–185,198–199`; user manual.pdf p.1; `iterateq.cpp:198–199`; `VersionHistory.h:438–442` | A 판 차이 | 8.0 이전 판(문서 표지 6.1.1·머리글 5.9.6) 기준, 그 판 코드는 배포본이 없다. 현재 재설정 조건은 `if ((Statesptr->reset_timeinit == ON) & (Solverptr->t>Parptr->reset_timeinit_time))`이다. 이때 `Arrptr->initHtm[ptr] = (NULLVAL);`을 실행한다. 다음 침수 기록은 `Arrptr->initHtm[ptr] = Solverptr->t / C(3600.0);`이다. |
| par:LI1-138 | `qloutput` | user manual.pdf p.21<br>user manual.pdf p.21 `flow limiter values calculated by the adaptive time stepping routine`; `*.QLx and *.QLy`; 적용 열 `2D fixed timestep`; 기본 off. | `pars.cpp:443` `if (read_empty_param(param_name, line_number, param_value_ptr, "qloutput", verbose, mode))`<br>`pars.cpp:444` `{`<br>`pars.cpp:445` `Statesptr->save_QLs = ON;`<br>`pars.cpp:446` `return;`<br>`pars.cpp:447` `}`<br>`lisflood.cpp:229` `SimStates.save_QLs = OFF;`<br>`fp_flow.cpp:164` `else`<br>`fp_flow.cpp:165` `{`<br>`fp_flow.cpp:166` `// flow limiter`<br>`fp_flow.cpp:167` `Qlim=Solverptr->Qlimfact*Parptr->dA*fabs(dh)/(8*Solverptr->Tstep);`<br>`fp_flow.cpp:168` `if(fabs(Q)>Qlim)`<br>`fp_flow.cpp:169` `{`<br>`fp_flow.cpp:170` `if(Q>0) Q=Qlim;`<br>`fp_flow.cpp:171` `if(Q<0) Q=-Qlim;`<br>`fp_flow.cpp:172` `// MT added to record Qlim`<br>`fp_flow.cpp:173` `Arrptr->LimQx[pTQ]=Q;`<br>`fp_flow.cpp:174` `}`<br>`output.cpp:981` `if(Statesptr->save_QLs==ON)`<br>`output.cpp:982` `{`<br>`output.cpp:983` `if (Statesptr->binary_out==ON) // output binary of ascii rasters`<br>`output.cpp:984` `{`<br>`output.cpp:985` `write_binrasterfile(Fnameptr->resrootname,Parptr->SaveNo,".QLxb",Arrptr->LimQx,Arrptr->DEM,1,Statesptr,Parptr);`<br>`output.cpp:986` `write_binrasterfile(Fnameptr->resrootname,Parptr->SaveNo,".QLyb",Arrptr->LimQy,Arrptr->DEM,2,Statesptr,Parptr);`<br>`output.cpp:987` `}`<br>`output.cpp:988` `else`<br>`output.cpp:989` `{`<br>`output.cpp:990` `write_ascfile(Fnameptr->resrootname,Parptr->SaveNo,".QLx",Arrptr->LimQx,Arrptr->DEM,1,Statesptr,Parptr);`<br>`output.cpp:991` `write_ascfile(Fnameptr->resrootname,Parptr->SaveNo,".QLy",Arrptr->LimQy,Arrptr->DEM,2,Statesptr,Parptr);`<br>확인한 원문: user manual.pdf p.21; `pars.cpp:443–447`; `lisflood.cpp:229`; `fp_flow.cpp:158–174`; `output.cpp:981–991`; `VersionHistory.h:287–294`; `fp_flow.cpp:158–174` | B 문서 오기 | QL 격자의 제한 유량은 고정 시간 간격 가지에서 계산한다. |
| par:LI1-141 | mint_hk의 총 침수시간 | user manual.pdf p.21; user manual.pdf p.37–38<br>user manual.pdf p.21 `totalHtm (total inundation time)` | `pars.cpp:404` `if (read_empty_param(param_name, line_number, param_value_ptr, "mint_hk", verbose, mode))`<br>`pars.cpp:405` `{`<br>`pars.cpp:406` `Statesptr->mint_hk = ON;`<br>`pars.cpp:407` `return;`<br>`pars.cpp:408` `}`<br>`lisflood.cpp:236` `SimStates.mint_hk = OFF;`<br>`iterateq.cpp:190` `if (Solverptr->t >= Parptr->MassTotal \|\| Statesptr->mint_hk == OFF)`<br>`iterateq.cpp:191` `{`<br>`iterateq.cpp:192` `#pragma omp parallel for private (i, ptr)`<br>`iterateq.cpp:193` `for (j = 0; j<Parptr->ysz; j++) for (i = 0; i<Parptr->xsz; i++)`<br>`iterateq.cpp:194` `{`<br>`iterateq.cpp:195` `ptr = i + j*Parptr->xsz;`<br>`iterateq.cpp:196` `if (Arrptr->H[ptr] > Solverptr->DepthThresh)`<br>`iterateq.cpp:197` `{`<br>`iterateq.cpp:198` `if (Arrptr->initHtm[ptr] == NULLVAL /*&& (Arrptr->H[ptr]>C(0.01)*/)`<br>`iterateq.cpp:199` `Arrptr->initHtm[ptr] = Solverptr->t / C(3600.0);`<br>`iterateq.cpp:200` `//if (Arrptr->H[ptr]>C(0.01))`<br>`iterateq.cpp:201` `Arrptr->totalHtm[ptr] += Solverptr->Tstep / C(3600.0);`<br>`lisflood2/sgm_fast.cpp:3928` `if (time_next >= Parptr->MassTotal \|\| Statesptr->mint_hk == OFF)`<br>`lisflood2/sgm_fast.cpp:3929` `{`<br>`lisflood2/sgm_fast.cpp:3930` `NUMERIC_TYPE delta_time_hours = delta_time / C(3600.0);`<br>`lisflood2/sgm_fast.cpp:3931` `NUMERIC_TYPE current_time_hours = time_next / C(3600.0);`<br>`lisflood2/sgm_fast.cpp:3932` (빈 줄)<br>`lisflood2/sgm_fast.cpp:3933` `#pragma omp for schedule(static) nowait`<br>`lisflood2/sgm_fast.cpp:3934` `for (int block_index = 0; block_index < wet_dry_bounds->block_count; block_index++)`<br>`lisflood2/sgm_fast.cpp:3935` `{`<br>`lisflood2/sgm_fast.cpp:3936` `SGC2_Inundation_block(block_index, grid_cols, grid_rows, grid_cols_padded,`<br>`lisflood2/sgm_fast.cpp:3937` `depth_thresh,`<br>`lisflood2/sgm_fast.cpp:3938` `current_time_hours,`<br>`lisflood2/sgm_fast.cpp:3939` `delta_time_hours,`<br>확인한 원문: user manual.pdf p.21; `pars.cpp:404–408`; `lisflood.cpp:236`; `iterateq.cpp:190–201`; `lisflood2/sgm_fast.cpp:3192,3928–3939`; user manual.pdf p.37–38; `iterateq.cpp:189–201,265`; `lisflood.h:612`; `VersionHistory.h:301–303` | C 문서 누락 | mint_hk의 massint 표본화는 문서가 밝힌 효율 선택이다. 고전 CPU는 `if (Solverptr->t >= Parptr->MassTotal \|\| Statesptr->mint_hk == OFF)` 안에서 수심 문턱을 넘은 셀에 `Arrptr->totalHtm[ptr] += Solverptr->Tstep / C(3600.0);`을 적용한다. 표본 사이의 시간 길이는 누적하지 않는다. 문서는 이 총 침수시간의 과소 누적 가능성을 구체적으로 적지 않는다. |
| par:LI1-208 | `steady` 무인자 | user manual.pdf p.15–22 | `steady` 무인자<br>`pars.cpp:259` `if (read_empty_param(param_name, line_number, param_value_ptr, "steady", verbose, mode))`<br>`lisflood.cpp:242` `SimStates.steadycheck = OFF;`<br>`iterateq.cpp:426` `if (Statesptr->steadycheck == ON && Solverptr->t >= Parptr->steadyTotal)`<br>`iterateq.cpp:427` `{`<br>`iterateq.cpp:428` `Parptr->steadyQdiff = BCptr->Qin - BCptr->Qout;`<br>`iterateq.cpp:429` `if (fabs(Parptr->steadyQdiff)<Parptr->steadyQtol) {`<br>`iterateq.cpp:430` `steadyCount += 1; // keep going a bit to make sure...`<br>`iterateq.cpp:431` `if (steadyCount == 10) break;`<br>`iterateq.cpp:432` `}`<br>`iterateq.cpp:433` `else {`<br>`iterateq.cpp:434` `steadyCount = 0;`<br>`iterateq.cpp:435` `}`<br>`iterateq.cpp:436` `Parptr->steadyTotal += Parptr->steadyInt;`<br>`iterateq.cpp:437` `}`<br>확인한 원문: user manual.pdf p.15–22; `pars.cpp:259`; `lisflood.cpp:242`; `iterateq.cpp:426–437` | C 문서 누락 | 공통 파서는 `steady`을 읽는다. 정상 상태 도달 여부를 검사하여 조기 종료할 수 있다. |
| par:LI1-209 | `steadytol` 실수; m³/s | user manual.pdf p.15–22 | `steadytol` 실수; m³/s<br>`pars.cpp:264` `if (read_numeric_param(param_name, line_number, param_value_ptr, "steadytol", &Parptr->steadyQtol, verbose, mode))`<br>`lisflood.cpp:127` `Params.steadyQtol = C(0.0005); // tolerance for steady-state definition`<br>`lisflood.cpp:128` `Params.steadyInt = C(1800.0); // interval at which to assess steady-state`<br>`iterateq.cpp:426` `if (Statesptr->steadycheck == ON && Solverptr->t >= Parptr->steadyTotal)`<br>`iterateq.cpp:427` `{`<br>`iterateq.cpp:428` `Parptr->steadyQdiff = BCptr->Qin - BCptr->Qout;`<br>`iterateq.cpp:429` `if (fabs(Parptr->steadyQdiff)<Parptr->steadyQtol) {`<br>`iterateq.cpp:430` `steadyCount += 1; // keep going a bit to make sure...`<br>`iterateq.cpp:431` `if (steadyCount == 10) break;`<br>`iterateq.cpp:432` `}`<br>`iterateq.cpp:433` `else {`<br>`iterateq.cpp:434` `steadyCount = 0;`<br>`iterateq.cpp:435` `}`<br>`iterateq.cpp:436` `Parptr->steadyTotal += Parptr->steadyInt;`<br>`iterateq.cpp:437` `}`<br>확인한 원문: user manual.pdf p.15–22; `pars.cpp:264`; `lisflood.cpp:127–128`; `iterateq.cpp:426–437` | C 문서 누락 | 공통 파서는 `steadytol`을 읽는다. 유입·유출 차이의 허용값이다. 기본값은 0.0005이다. 검사 간격의 기본값은 1800s이다. |
| par:LI1-216 | `Roe_slow` 무인자 | user manual.pdf p.15–22 | `Roe_slow` 무인자<br>`pars.cpp:420` `if (read_empty_param(param_name, line_number, param_value_ptr, "Roe_slow", verbose, mode))`<br>`lisflood.cpp:245` `SimStates.Roe_slow = OFF;`<br>`fp_trent.cpp:206` `if (Statesptr->Roe_slow==ON)`<br>`fp_trent.cpp:207` `{`<br>`fp_trent.cpp:208` `hl = hr;`<br>`fp_trent.cpp:209` `hul = -hur;`<br>`fp_trent.cpp:210` `hvl = hvr;`<br>`fp_trent.cpp:211` (빈 줄)<br>`fp_trent.cpp:212` `//s0=-(Arrptr->DEM[p1+1]-Arrptr->DEM[p1])/dl;`<br>확인한 원문: user manual.pdf p.15–22; `pars.cpp:420`; `lisflood.cpp:245`; `fp_trent.cpp:206–212` | C 문서 누락 | 공통 파서는 `Roe_slow`을 읽는다. Roe와 ghost-cell 스위치를 켠다. 다른 시간 간격 스위치는 끈다. 실제 Roe 유량 함수는 Roe_slow로 경계 처리를 구분한다. |
| par:LI1-244 | `kill` 실수; 계산시간 h | user manual.pdf p.15–22 | `kill` 실수; 계산시간 h<br>`pars.cpp:886` `if (read_numeric_param(param_name, line_number, param_value_ptr, "kill", &Parptr->killsim_time, verbose, mode))`<br>`lisflood.cpp:238` `SimStates.killsim = OFF;`<br>`pars.cpp:886` `if (read_numeric_param(param_name, line_number, param_value_ptr, "kill", &Parptr->killsim_time, verbose, mode))`<br>`pars.cpp:887` `{`<br>`pars.cpp:888` `if (verbose == ON) printf("\n***** WARNING: Simulation will be killed after %.2" NUM_FMT" hours *****\n", Parptr->killsim_time);`<br>`pars.cpp:889` `Parptr->killsim_time *= 3600;//convert hours to seconds`<br>`pars.cpp:890` `Statesptr->killsim = ON;`<br>`pars.cpp:891` `return;`<br>`pars.cpp:892` `}`<br>`iterateq.cpp:413` `if (Statesptr->killsim == ON)`<br>`iterateq.cpp:414` `{`<br>`iterateq.cpp:415` `//iteration time`<br>`iterateq.cpp:416` `time(&Solverptr->time_check);`<br>`iterateq.cpp:417` `Solverptr->itrn_time_now = Solverptr->itrn_time + (NUMERIC_TYPE)difftime(Solverptr->time_check, Solverptr->time_start);`<br>`iterateq.cpp:418` `// check if we have reached the kill time`<br>`iterateq.cpp:419` `if (Solverptr->itrn_time_now >= Parptr->killsim_time) {`<br>`iterateq.cpp:420` `if (verbose == ON) printf("Simulation kill time reached... ");`<br>`iterateq.cpp:421` `break;`<br>`iterateq.cpp:422` `}`<br>`iterateq.cpp:423` `}`<br>확인한 원문: user manual.pdf p.15–22; `pars.cpp:886–892`; `lisflood.cpp:238`; `iterateq.cpp:413–423` | C 문서 누락 | 공통 파서는 `kill`을 읽는다. 시간을 3600배하여 초로 저장한다. 계산 경과 시간이 문턱 이상이면 종료한다. |
| theory:LT1-063 | 체적유량과 단위폭 유량 | user manual.pdf p.10<br>user manual.pdf p.10 “Qx is volumetric flow rate in the x Cartesian direction”; `A`는 통수단면적; `h` 수심; `z` 하상 표고; `g` 중력; `n` Manning 계수; `R` 동수반경; `t` 시간; `x` 거리 | `ch_flow.cpp:368` `else                           csp->A[i]=Arrptr->H[csp->ChanX[i]+csp->ChanY[i]*Parptr->xsz]*csp->ChanWidth[i]; // all other points`; `weir_flow.cpp:131–132` `A = Width*hflow; // calc open channel flow area` / `R = A / (Width+2*hflow); // calc hydraulic radius from open channel flow`; `fp_acc.cpp:41` `q0=Arrptr->Qxold[pq0]; // in m2/s`; `fp_acc.cpp:306–307` `// Divide Q by dx to return m2/s` / `Arrptr->Qxold[pqptr]=Arrptr->Qx[pqptr]*dxinv;`<br>확인한 원문: user manual.pdf p.10; `ch_flow.cpp:363–368`; `weir_flow.cpp:130–132`; `fp_acc.cpp:41·306–307`; `sgc.cpp:826·844` | F 표기 차이 | 고전 ACC의 `Qxold`는 단위폭 유량이다. 셀 경계의 체적유량은 `Q=q\Delta x`이다. SGC의 이전 유량은 이미 체적유량이다. |
| theory:LT1-068 | 유량 제한자의 상세식 | user manual.pdf p.11·20<br>user manual.pdf p.11 유량 제한자는 “flow depth, grid size and time step”의 함수이다. | `fp_flow.cpp:167–174` `Qlim=Solverptr->Qlimfact*Parptr->dA*fabs(dh)/(8*Solverptr->Tstep);` / `if(fabs(Q)>Qlim)` / `{` / `if(Q>0) Q=Qlim;` / `if(Q<0) Q=-Qlim;` / `// MT added to record Qlim` / `Arrptr->LimQx[pTQ]=Q;` / `}`<br>확인한 원문: user manual.pdf p.11·20; `fp_flow.cpp:139–174` | C 문서 누락 | 유량 제한자는 `Qlim=Solverptr->Qlimfact*Parptr->dA*fabs(dh)/(8*Solverptr->Tstep);`로 계산한다. `if(fabs(Q)>Qlim)`이면 유량의 부호를 보존하여 제한한다. 문서는 계수 8을 포함한 식을 적지 않는다. `qlimfact`의 의미와 기본값 1은 user manual.pdf p.20에 있다. |
| theory:LT1-070 | Adaptive 안정 시간 간격 비례식 | user manual.pdf p.11·15 표 4<br>user manual.pdf p.11 번호 없는 비례식 “the stable time step scales with `(1/\Delta x)^2`” | `fp_flow.cpp:160` `*TSptr=getmin(*TSptr,(C(0.25)*Parptr->dy*Parptr->dy/alpha));`; `v8.0:fp_flow.cpp:154` 같은 식<br>확인한 원문: user manual.pdf p.11·15 표 4; `fp_flow.cpp:150–160`; `v8.0:fp_flow.cpp:146–154` | B 문서 오기 | 문서는 안정 시간 간격을 `(1/\Delta x)^2`에 비례한다고 적는다. 정방 격자와 고정한 수리 상태에서 코드의 상한은 `\Delta x^2`에 비례한다. |
| theory:LT1-074 | ACC 안정 시간 간격 비례식 | user manual.pdf p.11·15 표 4<br>user manual.pdf p.11 번호 없는 비례식 “The stable time step scales with `1/\Delta t`” | `fp_acc.cpp:271` `locT=cfl*Parptr->dx/(sqrt(g*MH));`; `v8.0:fp_acc.cpp:247` 같은 식<br>확인한 원문: user manual.pdf p.11·15 표 4; `fp_acc.cpp:249–276`; `v8.0:fp_acc.cpp:247–248` | B 문서 오기 | 문서의 `1/\Delta t` 비례식은 오기이다. 코드의 조건은 `if(MH > Solverptr->DepthThresh)`이다. 이 조건에서 `locT=cfl*Parptr->dx/(sqrt(g*MH));`를 계산한다. 조건을 통과하지 않으면 `Solverptr->Tstep=Solverptr->InitTstep;`로 지정한다. |
| theory:LT1-076 | Roe 마찰의 거듭제곱 표기 | user manual.pdf p.11<br>user manual.pdf p.11 Roe “point-wise friction based on the Manning´s equation” | `fp_trent.cpp:997` `norm=pow((Arrptr->HU[pc]/Arrptr->H[pc])*(Arrptr->HU[pc]/Arrptr->H[pc])+(Arrptr->HV[pc]/Arrptr->H[pc])*(Arrptr->HV[pc]/Arrptr->H[pc]),C(0.5)) ;`; `fp_trent.cpp:1006–1008` `manning=pow((pow(fn,C(1.5))/Arrptr->H[pc]+C(0.)*pow(fn,C(1.5))/Parptr->dx),(C(4.)/C(3.))) ;` / `sf=manning*norm  ;` / `Arrptr->HU[pc]*=(C(1.)/(C(1.)+Solverptr->g*Solverptr->Tstep*sf)) ;`<br>확인한 원문: user manual.pdf p.11; `fp_trent.cpp:987–1009` | F 표기 차이 | Roe의 `\big(n^{3/2}/h\big)^{4/3}`은 `n^2/h^{4/3}`과 같다. 코드의 측벽 후보 항은 0을 곱한다. |
| theory:LT1-077 | Roe 내부 벽의 옵션 조건 | user manual.pdf p.11<br>user manual.pdf p.11 Roe “domain boundary/internal boundary (wall) uses the ghost cell approach” | `fp_trent.cpp:301–305` `if (Statesptr->Roe_slow==ON)` / `{` / `hr = hl;` / `hur = -hul;` / `hvr = hvl;`; `pars.cpp:410–413` `if (read_empty_param(param_name, line_number, param_value_ptr, "Roe", verbose, mode))` / `{` / `Statesptr->Roe = ON;` / `Statesptr->Roe_slow = OFF;`<br>확인한 원문: user manual.pdf p.11; `VersionHistory.h:214–216`; `fp_trent.cpp:301–305`; `pars.cpp:410–428` | B 문서 오기 | 고전 Roe의 내부 벽 처리는 `Roe_slow`에 따라 달라진다. 기본 `Roe` 키워드는 이 상태를 OFF로 지정한다. |
| theory:LT1-307 | Manning 소경사 선형화 | user manual.pdf p.11·19<br>user manual.pdf p.11 Manning 확산파의 소경사 선형화·통수심 상한·조도 평균 식이 없다. | `fp_flow.cpp:136–137` `if(Arrptr->Manningsn!=NULL) fn=C(0.5)*(Arrptr->Manningsn[p0]+Arrptr->Manningsn[p1]);` / `else fn=Parptr->FPn;`; `fp_flow.cpp:143–145` `hflow=getmax(z0+h0,z1+h1)-getmax(z0,z1);` / `hflow=getmax(hflow,0);` / `hflow=getmin(hflow,Solverptr->MaxHflow);`; `fp_flow.cpp:150–155` `if(dh<Solverptr->dhlin)` / `{` / `Sf=sqrt(Parptr->dx/Solverptr->dhlin)*(dh/Parptr->dx);` / `alpha=(pow(hflow,(C(5.0)/C(3.0)))*Parptr->dx_sqrt)/(fn*sqrt(Solverptr->dhlin));` / `}` / `else alpha=pow(hflow,(C(5.0)/C(3.0)))/(C(2.)*fn*Sf);`<br>확인한 원문: user manual.pdf p.11·19; `fp_flow.cpp:136–155`; `lisflood.cpp:176·467–468`; `pars.cpp:668–677` | C 문서 누락 | 고전 Manning 유량은 두 셀 조도의 산술평균을 쓴다. 통수심을 `MaxHflow`로 제한한다. 기본 소경사 문턱은 DEM을 읽은 뒤 `dx*0.0002`로 설정한다. |
| theory:LT1-308 | ACC q 중심식의 재계산 | user manual.pdf p.11·20<br>user manual.pdf p.11 ACC의 q 중심 가중치·부호 보정·경계 대체값 식이 없다. | `fp_acc.cpp:72–81` `qup=Arrptr->Qxold[pq0-1];` / `qdown=Arrptr->Qxold[pq0+1];` / `if (i == 0 && qup == 0)` / `{` / `qup = q0;` / `}` / `if (i == Parptr->xsz - 2 && qdown == 0)` / `{` / `qdown = q0;` / `}`; `fp_acc.cpp:92–95` `if (Q*dh < C(0.0)){ // version of line above that will compile on windows machine` / `//Semi-implicit scheme of Bates et al (2010)` / `Q=(q0-(g*dt*hflow*Sf))/(1+g*dt*hflow*fn*fn*fabs(qvect)/(pow(hflow,(C(10.0)/C(3.0)))))*Parptr->dx;` / `}`<br>확인한 원문: user manual.pdf p.11·20; `fp_acc.cpp:72–95` | C 문서 누락 | ACC q 중심식이 수면차와 반대 부호의 유량을 만들면 Bates 2010 식으로 다시 계산한다. |
| theory:LT1-309 | Roe의 세부 수치 처리 | user manual.pdf p.11·19–20<br>user manual.pdf p.11 Roe는 방법 이름만 설명한다. 엔트로피 보정·유량 식·습윤/건조·운동량 문턱 식은 없다. | `fp_trent.cpp:246–248` `Arrptr->FHx[pq0]=C(0.5)*(f1rp+f1lp-a1m*alfa1*e11-a2m*alfa2*e21-a3m*alfa3*e31) ;` / `Arrptr->FHUx[pq0]=C(0.5)*(f2rp+f2lp-a1m*alfa1*e12-a2m*alfa2*e22-a3m*alfa3*e32) ;` / `Arrptr->FHVx[pq0]=C(0.5)*(f3rp+f3lp-a1m*alfa1*e13-a2m*alfa2*e23-a3m*alfa3*e33) ;`; `fp_trent.cpp:987` `if(Arrptr->H[pc] > Solverptr->MomentumThresh)`<br>확인한 원문: user manual.pdf p.11·19–20; `fp_trent.cpp:75·229–248·987–1013`; `lisflood.cpp:175` | C 문서 누락 | Roe는 고유파에 따른 소산과 엔트로피 보정을 사용한다. 습윤/건조 및 운동량 문턱을 별도로 검사한다. |
| theory:LT1-311 | 음수 수심 방지 | user manual.pdf p.12·19<br>user manual.pdf p.12 저장 셀 설명은 음수 수심·유출 재조정 검사를 적지 않는다. | `util.cpp:15–16` `// If dV is going to make the water depth -ve, scale all flows out of cell` / `// so that the water volume in the cell goes to 0 in`; `util.cpp:45–51` `if (cv + dV < 0)` / `{` / `WDweight = -cv / dV; // C(0.5) for improved drying stability` / `if (*q1 < 0) *q1 *= WDweight;` / `if (*q2 > 0) *q2 *= WDweight;` / `if (*q3 < 0) *q3 *= WDweight;` / `if (*q4 > 0) *q4 *= WDweight;`; `iterateq.cpp:150` `if (Statesptr->drychecking == ON) DryCheck(Parptr, Solverptr, Arrptr);`<br>확인한 원문: user manual.pdf p.12·19; `util.cpp:15–51`; `iterateq.cpp:150·528–541` | C 문서 누락 | 고전 경로는 `if (Statesptr->drychecking == ON)`일 때 `DryCheck`를 호출한다. 검사 대상은 `*hptr>Solverptr->DepthThresh`인 셀이다. `if (cv + dV < 0)`이면 유출 유량을 `WDweight = -cv / dV;`로 비례 조정한다. 수심 갱신 뒤 남은 음수 수심은 0으로 자른다. |
