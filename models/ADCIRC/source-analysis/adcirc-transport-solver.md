---
title: "ADCIRC 3D 스칼라 transport solver source-analysis — transport.F/TRANS_3D (sigma advection-diffusion, Alp4 semi-implicit, tridiagonal)"
topic: adcirc-transport-solver
canonical_source: self
citation_status: verified
verification_method: "ADCIRC raw source 직접 read: src/transport.F(1497, v45.12) — Alp4 semi-implicit DTAlp4/DT1MAlp4(:31-32)·ADC_TRIDAG2 tridiag 호출(:1182) file:line 직접 검증. dispatch vsmy.F:1548-1553. 소스 banner Luettich-Westerink. ★adcirc-3d-mode:59 가 transport 를 vsmy.F:1543 로 오귀속(정정)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-07
verification_by: "Claude Opus 4.8 (1M context) — transport.F:28-35·1178-1185 직접 read 검증"
verification_date: 2026-07-07
related:
  - models/ADCIRC/source-analysis/adcirc-3d-mode.md
  - models/ADCIRC/source-analysis/adcirc-tidal-forcing.md
  - models/ADCIRC/source-analysis/adcirc-gwce-implementation.md
---

# ADCIRC 3D 스칼라 transport solver — `transport.F` / `TRANS_3D`

> 소스: [`src/transport.F`](../raw/source_code/adcirc/src/transport.F) (1497, "PADCIRC RELEASE VERSION 45.12", Luettich·Westerink).
> **정체**: 3D baroclinic **염분/수온 이류-확산** solver(sigma 좌표). 하나의 generic in/out 배열로 S·T 모두 처리 — ADCIRC prognostic 성층 엔진(하구 성층·thermohaline surge). dispatch: `vsmy.F:1548-1553` `CALL TRANS_3D(SAL,NLSD,NVSD,...)` + `(TEMP,NLTD,NVTD,...)`.
> ★**오귀속 정정**: [[adcirc-3d-mode]]:59 는 "S/T transport (`vsmy.F:1543`)" 라 적었으나 vsmy.F 는 **dispatch만**(:1548-1553), 알고리즘 전체는 `transport.F:44-1229`. cross-model: ROMS [[roms_tracer_timestep_step3d_t]]·Delft3D [[delft3d_difu_transport]]·EFDC CALTRAN 의 ADCIRC 판.

## 0. 구조

| 서브루틴 | 라인 | 역할 |
|---|---|---|
| `TRANS_3D(inarray,diffhoriz,diffvert,outarray,field,TimeLoc)` | 44-1229 | 한 스칼라장 advection-diffusion 메인 |
| `ADC_TRIDAG2(A,B,C,R,U,N)` | 1231-1272 | Thomas 연직 tridiagonal solver |
| `CROSSPRODUCT` | 1274-1316 | 벡터 외적(geometry/normal) |
| `cubic_vertical_interpolation` | 1318-1497 | 이웃노드 sigma 준위로 cubic 보간(수심다른 노드간 수평구배용) |

## 1. Alp4 semi-implicit 연직 시간가중 (:31-32) ★GWCE 와 다른 스킴
```fortran
DTAlp4   = DelT*Alp4        ! :31 연직 dispersion 항 LHS 가중
DT1MAlp4 = DelT*(1.-Alp4)   ! :32 RHS forcing 가중  (조립 :1077-1079,1124)
```
> ★[[adcirc-gwce-implementation]] 은 "GWCE 에 semi-implicit Theta 없음" — 그러나 **transport 는 연직 semi-implicit(Alp4)**. 별개 시간적분 스킴(기존 미문서).

## 2. Compact tridiagonal 조립 (:137-140)
3-대각 `Mkm1trans`(k-1)·`Mktrans`(k)·`Mkp1trans`(k+1) + RHS `Frtrans`, 수평노드별.
- **연직 diffusion** `KNVnm(k,1:3)`(:725-736): `NTVTot`(총 연직확산, MY2.5 [[adcirc-3d-mode]] §F) / sigma 간격 `(Sigma(k+1)-Sigma(k))`.
- **연직 advection** `VAdvectrans(k)`(:841-864): surface/interior/bottom 분기, sigma 연직속도 `WSigma`·∂trans/∂sigma.
- **수평 advection** `LAdvectrans(k)`(:874,1018): element FE `a1/a2/a3·b1/b2/b3`(:122), `sponge(NH)*IFNLCT` 스케일.
- **수평 diffusion** + optional **biharmonic** `Biharmonic_LDiffusion`(:182-191).

## 3. 연직 tridiagonal solve (:1182)
```fortran
CALL ADC_TRIDAG2(Mkm1trans,Mktrans,Mkp1trans,Frtrans,Gammatrans,NFEN)   ! Thomas, 노드당 1 연직컬럼
```
> ★**독립 선형solver** — GWCE 의 ITPACK/JCG([[adcirc-gwce-implementation]]) 와 별개인 2번째 solve 경로.

## 4. 경계조건 (기존 미문서)
- **weak open-ocean BC** influx/outflux 판별(:304-372, `USE BOUNDARIES` NOPE/NETA/NBDV).
- **surface heat-flux BC** `BCFLAG_TEMP=1/2/3`(:435/456/485), 시간보간 `HFLUX=q_heat1+TTBCRATIO*(q_heat2-q_heat1)`(:447), `cpwater=4000`(:134).

## 5. 기타
- **wet/dry masking** `NCEle=NODECODE(N1)·NODECODE(N2)·NODECODE(N3)·NOFF(NEle)`(:240, dry element skip, "Casey's wet/dry").
- **cross-node sigma remapping**(:249-272): 이웃값을 local sigma 로 cubic 보간 후 수평도함수 조립(`cubic_vertical_interpolation` :1318).
- diffusion 계수 입력: `NLSD/NVSD`(염분)·`NLTD/NVTD`(수온) per-field(vsmy.F:1548-1553).

## 6. 주요 findings
- **★오귀속**: 3d-mode:59/67 이 transport 를 vsmy.F(:1543/1630) 로 귀속 → 실제 vsmy 는 dispatch만, 엔진은 transport.F. 염분엔진 추적 시 엉뚱한 파일 도달.
- **Alp4 연직 semi-implicit** — GWCE(implicit theta 無)와 대조되는 별 스킴(미문서).
- **weak ocean + heat-flux BC**(:304-504) — 기존 노트는 barotropic elevation/flux BC 만.
- **독립 tridiagonal solver `ADC_TRIDAG2`** — ITPACK/JCG 밖 2번째 solve.

## 7. 관련
- [[adcirc-3d-mode]] — 3D 모드 개요(★:59 vsmy.F 오귀속 정정 대상, MY2.5 NTVTot 공급)
- [[adcirc-gwce-implementation]] — GWCE 연속(barotropic core, transport 와 별 solve/스킴)
- [[adcirc-tidal-forcing]] — baroclinic 강제 맥락
- **Primary**: Luettich-Westerink ADCIRC 3D theory report(v45.12 banner) · Mellor-Yamada 1982(NTVTot 연직확산).
