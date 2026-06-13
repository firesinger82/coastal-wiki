---
title: "FUNWAVE-TVD 전수분석 — flux·MUSCL-TVD 재구성 (fluxes.F·derivatives.F)"
model: FUNWAVE
citation_status: verified
verification_method: "src/fluxes.F(2476)·derivatives.F(413) 전수 read (서브에이전트 분석, 2026-06-13). file:line src 기준."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
---

# FUNWAVE-TVD flux·MUSCL-TVD 재구성

> 지배 solver의 flux 계산부 (fluxes.F 23subr+2func, derivatives.F 10subr). 관계는 [`funwave-code-graph.md`](funwave-code-graph.md), 흐름은 [`funwave-source-map.md`](funwave-source-map.md).

## 1. flux 디스패처·Riemann (fluxes.F)

| subr | file:line | 역할·기법 |
|---|---|---|
| `FLUXES` | fluxes.F:52 | 최상위 디스패처. `HIGH_ORDER` 플래그 분기: FOU(4차 vanLeer+minmod)/FMI(4차 minmod)/WEN(WENO5)/MLP(MLP limiter)/else(2차 vanLeer). → 재구성 → WAVE_SPEED → FLUX_AT_INTERFACE(_HLL) → BOUNDARY_CONDITION |
| `FLUX_AT_INTERFACE_HLL` | :150 | HLL Riemann으로 P/Q/Fx/Fy/Gx/Gy 6 flux 계산 (HLL ×6) |
| `HLL` | :171 | HLL 공식 3-case: SL≥0→FL / SR≤0→FR / else `(SR·FL−SL·FR+SL·SR·(UR−UL))/(SR−SL)` (Harten 1983) |
| `FLUX_AT_INTERFACE` | :128 | 단순 산술평균 `0.5(FR+FL)` (predictor용, TVD 미사용) |
| `WAVE_SPEED` | :352 | HLL 파면속도 SxL/SxR/SyL/SyR — Zhou 2001 Roe평균 `S=0.5(L+R)+0.25(UL−UR)` |

## 2. MUSCL 재구성 (차수·limiter별)

| subr | file:line | 차수·limiter |
|---|---|---|
| `CONSTRUCTION` / `CONSTRUCT_X` / `CONSTRUCT_Y` | :452/:759/:702 | **2차 vanLeer** piecewise-linear (Zhou 2001). `OutL=Vin(I-1)+0.5DX·Din`, Din=vanLeer 제한기울기 |
| `CONSTRUCTION_HO` / `CONSTRUCT_HO_X/Y` | :1324/:1531/:1646 | **4차 FOU**(Erduran 2005): 1단계 3-arg minmod로 `Din=TXP2−(1/6)(DVP3−2DVP2+DVP1)`, 2단계 vanLeer 인터페이스. (기본 권장) |
| `CONSTRUCTION_HO_minmod` / `_X/Y_minmod` | :816/:1045/:1163 | 4차 minmod only (FMI) — "4th+minmod 불안정"(Choi 2016) 비활성, 테스트용 |
| `CONSTRUCTION_HO_MLP` / `_X/Y_MLP` | :1761/:1958/:2032 | **MLP**(다차원 limiting, Park-Kim): 횡방향 기울기(tanth1/2) 참조해 2D 정보 반영, 과제한 방지 |
| `CONSTRUCTION_WENO` / `WENO_CONSTRUCT_X/Y` | :2121/:2301/:2392 | **WENO5**(Qiu-Shu 2005, #CARTESIAN only): 3 stencil smoothness WBETA + 비선형가중 `W=d/(ε+WBETA)²`, ε=1e-6 |
| `VANLEER_LIMITER` / `MINMOD_LIMITER` (func) | :1280/:1296 | vanLeer `(A|B|+|A|B)/(|A|+|B|)` / 2·3-arg minmod |
| `DelxFun`/`DelyFun`/`DelxyFun` | :293/:239/:204 | vanLeer TVD slope limiter 미분(경계 1차 편측) |

**Boussinesq 분산 결합**: CARTESIAN+DISPERSION 시 재구성에 U4/V4(분산 보정속도) 추가, flux 조립 `PL=HUxL+Gamma1·H·U4xL`, `FxL=Gamma3·PL·(UxL+Gamma1·U4xL)+0.5g(EtaR²·Gamma3+2·EtaR·Depth)`.

## 3. 공간 미분 (derivatives.F, 분산항용)

| subr | file:line | 기법 |
|---|---|---|
| `DERIVATIVE_X/Y` | :158/:123 | 2차 중심차분 `(U(I+1)−U(I-1))/2DX·MASK` |
| `DERIVATIVE_XX/YY/XY` | :263/:192/:226 | 2차 2계·혼합 미분 |
| `DERIVATIVE_X/Y_High` | :88/:52 | 4차 1계 `(U(I+2)+2U(I+1)−U(I-2)−2U(I-1))/8DX` |
| `DERIVATIVE_XX/YY/XY_HIGH` | :351/:387/:299 | 4차 2계 5점 `(−U(I-2)+16U(I-1)−30U(I)+16U(I+1)−U(I+2))/12DX²` |

⚠️ **버그 의심**: `DERIVATIVE_YY_HIGH`(:387) 코드 L407 `Uin(I+2,J+2)` — y방향 2계인데 x-index 혼입 가능성(원저자 확인 필요).

## 4. 호출 계층

```
FLUXES → [HIGH_ORDER 분기] CONSTRUCTION{_HO/_HO_minmod/_HO_MLP/_WENO}
            → CONSTRUCT_*_X/Y (재구성 L/R 쌍)
       → WAVE_SPEED (Zhou Roe)
       → FLUX_AT_INTERFACE_HLL → HLL ×6
       → BOUNDARY_CONDITION
DERIVATIVE_* : 직접 fluxes 밖, 분산항(dispersion.F)·SGS 확산에서 호출
```

## 5. 연결
- [`funwave-code-graph.md`](funwave-code-graph.md) · [`funwave-dispersion-solver.md`](funwave-dispersion-solver.md)(U4/V4 분산) · [`funwave-tvd-manual.md`](../manual-notes/funwave-tvd-manual.md)(MUSCL-TVD scheme)
