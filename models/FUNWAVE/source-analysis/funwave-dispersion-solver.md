---
title: "FUNWAVE-TVD 전수분석 — Boussinesq 분산 + tridiagonal solver"
model: FUNWAVE
citation_status: verified
verification_method: "src/dispersion.F·etauv_solver.F·tridiagnal.F·bc.F(PHI_COLL) 전수 read (서브에이전트, 2026-06-13). file:line src 기준."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
---

# FUNWAVE-TVD Boussinesq 분산 + tridiagonal solver

> ★연산비용 핵심부 + **GPU(cusparse) 대체 대상**([`funwave-build-and-blackwell-port.md`](funwave-build-and-blackwell-port.md)). RK 각 단계마다 분산항 계산 → η,U,V 적분 → tridiagonal로 u,v 복원.

## 1. CAL_DISPERSION (dispersion.F:62)
RK 서브단계마다 Boussinesq 분산 보정항 계산 → 전역배열 저장. 호출: main.F:383 `IF(DISPERSION)`.
- **고차미분**(:77-83,151-158): DERIVATIVE_XX/XY/YY → Uxx·Uxy·Vxy·Vyy(속도), DUxx·DUxy·DVxy·DVyy(수심플럭스)
- **선형 분산항 V4**(:296-329, Madsen-Sørensen/Nwogu): `U4=(1/3−β₁+β₁²/2)h²(uxx+vxy)+(β₁−1/2)h(DUxx+DVxy)`
- **U1p·V1p**(:337-346, Shi 2012): `U1p=0.5(1−β₁)²h²(uxx+vxy)+(β₁−1)h(DUxx+DVxy)`
- **비선형 고차항 U2/V2/U3/V3**(:399-498, Gamma2>0): 시간미분 Ut=(U−U0)/DT + 소용돌이도 omega_0=Vx−Uy
- 벽경계 교차미분 zero-fix(:192-286, LEFT_BC_IRR 예외)
- → `EXCHANGE_DISPERSION`(ghost 갱신)

## 2. ESTIMATE_HUV (etauv_solver.F:53)
3차 RK 각 단계(ISTEP=1,2,3) 보존형 연속·운동량 적분. 호출: main.F:414 (FLUXES·SourceTerms 후).
- **η**(:103-280): `R1=−(1/DX)(P(I+1)−P(I))−(1/DY)(Q(J+1)−Q(J))` [연속] → `Eta=α(ISTEP)·Eta0+β(ISTEP)(Eta+DT·R1)` [RK]. WaveMaker_Mass 질량소스 추가. #ZALPHA 구면 보정. Wsurf=R1(수직속도)
- **Ubar·Vbar**(:282-346): `R2=−(1/DX)(Fx(I+1)−Fx(I))−(1/DY)(Fy(J+1)−Fy(J))+SourceX` → RK
- → `GET_Eta_U_V_HU_HV`(:348)

## 3. GET_Eta_U_V_HU_HV (etauv_solver.F:365) — tridiagonal 조립·풀이
Ubar·Vbar → 분산 implicit 연산자 `(I+Γ₁·L_xx)U=RHS`를 x/y 방향 분해 tridiagonal로 u,v 복원.
- 수심 `H=Eta·Gamma3+Depth`
- **x tridiag 계수**(:400-461): 하/주/상대각 tmp1/2/3 = `Γ₁·MASK9·(b₁/2DX²·h²+b₂/DX²·h·h_{l/r})`, RHS tmp4=`Ubar/H+Γ₁·MASK9·(−b₁/2·h²·Vxy−b₂·h·DVxy)` → 정규화 myA/myC/myD
- **풀이**: `CALL TRIDx`(parallel)/`TRIDx_ser`(serial) → U
- **y tridiag**(:478-539): DISP_TIME_LEFT 시 비선형 자유수면 보정(Γ₂·η 항). `CALL TRIDy/TRIDy_periodic/TRIDy_ser` → V
- **HU·HV + Froude cap**(:568-590): `HU=max(H,MinDepthFrc)·U`, |U|/√(gH)>FroudeCap이면 방향유지·속도제한

## 4. tridiagnal.F — Thomas + MPI 파이프라인 + Sherman-Morrison

| subr | file:line | 방식 |
|---|---|---|
| `TRIDx_ser`/`TRIDy_ser` | :375/:338 | **Thomas algorithm** 직렬. forward sweep(피벗 `1/A−C_{i-1}`)+backward subst. **각 j행(또는 i열)이 독립 1D 시스템**(외부 루프) |
| `TRIDx`/`TRIDy` | :413/:502 | **MPI 파이프라인**: west→east(south→north) 토큰 전달, 이웃 소거결과 MPI_IRECV→sweep→MPI_ISEND |
| `TRIDy_periodic` | :59 | **Sherman-Morrison**(Thomas 1995 §5.6.1): 주기경계 → TRIDy 2회 호출(B·y1=d, B·y2=w) + β스케일 `f=y1+β·y2` |

★ **GPU 대체**(FUNWAVE-GPU): TRID*_ser의 독립 배치 j(i)-루프 → `cusparseSgtsv2StridedBatch` 1회. MPI 토큰패싱(rmsg/smsg)은 단일 GPU 메모리로 제거. 계수 A,C,D는 INOUT(forward에서 덮어씀)→복사 보존 필요.

## 5. PHI_COLL·EXCHANGE_DISPERSION (bc.F) — 관계 허브
- `EXCHANGE_DISPERSION`(bc.F:306): 분산 2차/교차/1차 미분 필드 ghost 갱신 → PHI_COLL ×8~32(Gamma2 분기)
- `PHI_COLL`(bc.F:631, 87회 호출): VTYPE별 ghost 패턴 — 1(η형 대칭)/2(u형 x반대칭)/3(v형 y반대칭)/4(교차 0)/5(전대칭)/6(전반대칭) + PERIODIC + `phi_exch`(MPI)

## 6. 호출 흐름
```
main RK loop → CAL_DISPERSION(DERIVATIVE_*→EXCHANGE_DISPERSION→PHI_COLL→phi_exch)
            → FLUXES → SourceTerms → ESTIMATE_HUV → GET_Eta_U_V_HU_HV
                 → TRIDx/TRIDx_ser (U) , TRIDy/TRIDy_periodic/TRIDy_ser (V)
```

## 7. 연결
- [`funwave-flux-tvd.md`](funwave-flux-tvd.md)(U4/V4) · [`funwave-build-and-blackwell-port.md`](funwave-build-and-blackwell-port.md)(cusparse) · [`funwave-code-graph.md`](funwave-code-graph.md)
