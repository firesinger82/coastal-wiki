---
title: "ROMS tracer 시간적분 엔진 source-analysis — step3d_t.F (LF-AM3 corrector: flux-form update + MPDATA + 이중 implicit tridiagonal)"
topic: roms-tracer-timestep-step3d-t
canonical_source: self
citation_status: verified
verification_method: "ROMS raw source 직접 read: ROMS/Nonlinear/step3d_t.F(1976줄) — conservative flux-form update(:905-909)·implicit 연직확산 tridiagonal(:1730-1764) file:line 직접 검증. 소스주석 primary Wu-Zhu2010 OM33:33-51(HSIMT :478-481)·Zhang2010 JPO40(mean age :1813). 기존 [[roms_advection]]/[[roms_baroclinic_3d]] 는 advection 분기만, 시간적분 알고리즘 미커버."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — step3d_t.F:899-918·1723-1770 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/ROMS/source-analysis/roms_advection.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/source-analysis/roms_vertical_mixing.md
  - models/ROMS/source-analysis/roms_nonlinear_core_remaining.md
---

# ROMS tracer 시간적분 엔진 — `step3d_t.F`

> 소스: [`ROMS/Nonlinear/step3d_t.F`](../raw/source_code/roms/ROMS/Nonlinear/step3d_t.F)(1976, `#if !TS_FIXED && NONLINEAR && SOLVE3D`, author Shchepetkin).
> **정체**: 모든 passive/bio/sediment tracer 가 타는 **시간적분(LF-AM3 corrector half)** 엔진. 기존 노트는 advection **분기 카탈로그**만([[roms_advection]]:19 "all tracer advection branches"), corrector 조립·flux-form 갱신·MPDATA anti-diffusion·이중 implicit tridiagonal 은 미커버.

## 0. LF-AM3 corrector 입력 계약 (:21-28)

`step3d_t`(driver :40-117) → `step3d_t_tile`(전 알고리즘 :120-1974). 진입 시:
- `t(:,:,:,nnew,:)` = n+1 확산+source/sink 항
- `t(:,:,:,3,:)` = n+1/2 advection+연직확산 **predictor**([[roms_nonlinear_core_remaining]] pre_step3d)

→ 이 파일 = Leapfrog-AM3 의 **corrector half**. `oHz=1/Hz`(:382) metric 을 flux-form 전반에 사용.

## 1. 수평 advection → conservative flux-form 갱신

advection flux 분기 dispatch(:402-770, → [[roms_advection]]: CENTERED2/MPDATA/HSIMT-TVD/Akima/centered-4/upstream-3) 후 **conservative flux-form 시간갱신** (:905-909):
```fortran
cff = dt*pm(i,j)*pn(i,j)                              ! :905 격자면적 metric
cff1 = cff*(FX(i+1,j)-FX(i,j))                        ! :906 x-flux divergence
cff2 = cff*(FE(i,j+1)-FE(i,j))                        ! :907 y-flux divergence
t(i,j,k,nnew,itrc) = t(i,j,k,nnew,itrc) - (cff1+cff2)  ! :909 (단위 m·Tunits)
```
flux 단위 Tunits·m³/s → 발산이 밀도가중 tracer 변화. **MPDATA 분기는 별도** private `Ta` 중간장(:870-897, 양정치 필요).

## 2. 연직 advection (:922-1186)
spline(:938)·Akima(:987)·centered-2(:1029)·upstream-3(:1050)·HSIMT(:1071)·centered-4(:1147).

## 3. ★이중 implicit tridiagonal (OMEGA_IMPLICIT) — advection 먼저, 확산 나중

### 3.1 implicit 연직 advection (:1556-1655)
`FC=dt·Wi·pm·pn`(off-diag :1559), diagonal `BC`(:1583), tridiagonal solve(:1597)+back-sub(:1612) — **확산보다 먼저**.

### 3.2 implicit 연직 diffusion Crank-Nicholson (:1657-1789)
```fortran
FC(i,k) = -dt*lambda/(z_r(k+1)-z_r(k))*Akt(i,j,k,ltrc)   ! :1730-1734 off-diag
BC(i,k) = Hz(i,j,k) - FC(i,k) - FC(i,k-1)                 ! :1747 diagonal
DC(i,k) = t(i,j,k,nnew,itrc)                              ! :1748 RHS
! Thomas: forward elim (:1755-1764) + back-sub (:1769) → 최종 t(nnew)
```
> ★**연직 advection 과 diffusion 이 별개 tridiagonal 2회** — 매뉴얼의 단일 "implicit vertical mixing" 서술이 감춤. spline path 는 **Thomas 아닌 LU decomposition+forward sub**(:1686) — 같은 항의 2 코드경로(parabolic spline 요청 여부).

## 4. MPDATA anti-diffusion (:1371-1458)
anti-diffusive velocity 계산(:1371) → corrected flux(:1399) → corrected 수평(:1421)·연직(:1442) 갱신. **private `Ta` 중간장 사용**(in-place 아님) → **TLM/ADM 미지원 이유**([[roms_tangent_linear_model]]:172).

## 5. Point source + SED_MORPH (:1485-1554)
LwSrc tracer 주입(:1485-1526, `LTracerSrc` 시 유입농도 Tsrc, else 체적보상). SED_MORPH bed 변화 mass 를 1/N 분배(:1528-1554). ★MPDATA(:1223-1240 Ta 증분) vs non-MPDATA(:1528 체적보상) **경로 이원**.

## 6. Mean-age + LBC + nudging (:1804-1928)
mean-age tracer `t(nnew,iage) += dt·t(inert)`(:1813, Zhang 2010). t3dbc lateral BC(:1837) 후 climatology nudging `Tnudgcof·(tclm-t)`(:1866, `LnudgeTCLM`) — ★**LBC 후 적용**(내부 nudging, [[roms_open_boundaries]] M2/M3 momentum nudging 과 별개). mask(:1882)·dC/dt diag(:1894)·mp_exchange(:1908).

## 7. 주요 findings
- **연직 advection+diffusion = 별개 tridiagonal 2회**(advection 먼저, :1597 → diffusion :1752). baroclinic_3d:45 는 단일화(불완전).
- **spline diffusion = LU**(:1686), 표준 = Thomas(:1752) — 2 경로.
- **MPDATA private Ta 중간장**(:870, in-place 아님) → TLM/ADM 미지원 근본원인.
- **SED_MORPH mass 이중경로**(MPDATA Ta vs non-MPDATA 1/N 보상).
- **nudging = LBC 후, LtracerCLM&LnudgeTCLM 만**(:1852,1866).

## 8. 관련
- [[roms_advection]] — advection 분기 카탈로그(본 노트가 시간적분 보완)
- [[roms_baroclinic_3d]] — 3D momentum(step3d_t 를 dependency 로 지목 :22)
- [[roms_vertical_mixing]]·[[roms_kpp_boundary_layer]] — Akt 연직확산계수(§3.2 소비)
- [[roms_nonlinear_core_remaining]] — pre_step3d predictor half(LF-AM3 짝)
- **Primary**: Wu-Zhu 2010 OM 33:33-51(HSIMT) · Zhang et al. 2010 JPO 40:965(mean age) · Shchepetkin-McWilliams 2005/2009(LF-AM3 framework, omega/set_depth 노트).
