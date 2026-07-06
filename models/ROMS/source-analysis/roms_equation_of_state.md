---
title: "ROMS 상태방정식 source-analysis — rho_eos.F (Jackett-McDougall 1995 비선형 EOS + Brunt-Väisälä bvf + alpha/beta), EFDC 대조"
topic: roms-equation-of-state
canonical_source: self
citation_status: verified
verification_method: "ROMS raw source 직접 read: ROMS/Nonlinear/rho_eos.F(889줄) + Modules/mod_eoscoef.F — den1 다항식(:274-285)·bvf 단열(:404-416)·Q00=999.842594(mod_eoscoef.F:50) file:line 직접 검증. 소스주석 primary Jackett-McDougall 1995 JAOT 12:381-389(:31-35). roms_nonlinear_core_remaining §2 부분커버 승격+bvf/alpha-beta/linear 갭 충전. EFDC [[efdc_baroclinic_eos]] cross-model 대조."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — rho_eos.F:271-285·394-424 + mod_eoscoef.F:24-64 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/ROMS/source-analysis/roms_nonlinear_core_remaining.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/source-analysis/roms_kpp_boundary_layer.md
  - models/EFDC/source-analysis/efdc_baroclinic_eos.md
---

# ROMS 상태방정식 — `rho_eos.F` (Jackett-McDougall 1995) + Brunt-Väisälä

> 소스: [`ROMS/Nonlinear/rho_eos.F`](../raw/source_code/roms/ROMS/Nonlinear/rho_eos.F)(889, `#ifdef SOLVE3D`) + 계수 [`ROMS/Modules/mod_eoscoef.F`](../raw/source_code/roms/ROMS/Modules/mod_eoscoef.F).
> **정체**: 온도·염분·압력(≈수심) → 밀도 → baroclinic 압력구배·성층 bvf. [[roms_nonlinear_core_remaining]] §2 가 부분커버(다항식·bulk modulus)했으나 **bvf(Brunt-Väisälä 단열)·alpha/beta 조립·linear branch 미커버** → 전용 노트로 승격. EFDC [[efdc_baroclinic_eos]] 와 **cross-model 대조**(§7).

## 0. NONLIN_EOS 이원 구조

`rho_eos`(driver :47-106) → `rho_eos_tile` **두 배타적 본체**(컴파일 타임):
- **nonlinear** (:111-570, `#ifdef NONLIN_EOS`) — Jackett-McDougall 1995 다항식
- **linear** (:576-886, `#ifndef NONLIN_EOS`) — `rho=R0-R0·Tcoef(T-T0)+R0·Scoef(S-S0)`

CPP `NONLIN_EOS`(cppdefs.h:71). 옵셔널 출력 CPP 게이팅(driver :88-98): `bvf`←`BV_FREQUENCY`, `alpha/beta`←`LMD_SKPP||LMD_BKPP||BULK_FLUXES||BALANCE_OPERATOR`, `alfaobeta`←`LMD_DDMIX`.

## 1. 계수 (mod_eoscoef.F) — ★EFDC 와 공유 UNESCO/EOS-80 base

```fortran
Q00 = 999.842594     ! :50  1-atm 밀도 상수항
U00 = 0.824493       ! :56  염분 선형항
W00 = 4.8314e-04     ! :64  염분 제곱항
A00 = 1.909256e+04   ! :24  secant bulk modulus
```
★**`Q00=999.842594`·`U00=0.824493`·`W00=4.8314e-04` = EFDC calbuoy 상수와 동일**([[efdc_baroclinic_eos]] :61,:128,:134) — 양 모델 모두 UNESCO/EOS-80 재적합. 인용은 소스에 없음(spirit of UNESCO).

## 2. 1-atm 밀도 다항식 (:274-285)
```fortran
Tt=MAX(-2,T) ; Ts=MAX(0,S) ; sqrtTs=SQRT(Ts) ; Tp=z_r ; Tpr10=0.1*Tp   ! :259-268 입력클램프+★Tp=z_r(수심=압력)
C(0)=Q00+Tt(Q01+Tt(Q02+Tt(Q03+Tt(Q04+Tt·Q05))))    ! :274 Horner
C(1)=U00+Tt(U01+Tt(U02+Tt(U03+Tt·U04)))              ! :275
C(2)=V00+Tt(V01+Tt·V02)                               ! :276
den1 = C(0) + Ts*(C(1) + sqrtTs*C(2) + Ts*W00)       ! :285  (ζ^1.5 = sqrtTs·Ts 항)
```

## 3. Secant bulk modulus + in-situ 밀도 (:301-355) — ★압축률 포함

```fortran
bulk0=C3+Ts(C4+sqrtTs·C5) ; bulk1=C6+Ts(C7+sqrtTs·G00) ; bulk2=C8+Ts·C9   ! :301-320
bulk = bulk0 - Tp*(bulk1 - Tp*bulk2)                  ! :322  압력(Tp) 의존
cff=1/(bulk+Tpr10) ; den = den1*bulk*cff              ! :342 in-situ (압축)
den = den - 1000                                       ! :355 anomaly(rho0 baseline)
```
> ★**EFDC 와 결정적 차이**: ROMS 는 secant bulk modulus 로 **압력/압축률 포함**(`bulk=f(Tp)`, `Tp=z_r` 수심). EFDC 는 P=0 surface EOS(압축률 생략). → 심해 성층·음속에서 갈림.

유사 밀도 feedback(`SEDIMENT&&SED_DENS`, :344-353): `den += Σ t(itrc)·(Srho-den)/Srho` — EFDC 유사보정과 동류(양 모델 공통).

## 4. rhoA/rhoS 연직적분 (:362-388) — barotropic PGF
`VAR_RHO_2D`: 연직평균 밀도 `rhoA` + 편차 `rhoS`, `1/rho0` 정규화(:382) → 순압 압력구배력.

## 5. ★Brunt-Väisälä bvf — 단열 parcel (미커버 core, :390-424)
```
bvf = -g/rho · d(rho)/d(z)   (:396), 물덩이 단열 상하이동(z_w depth)로 밀도차
```
```fortran
bulk_up = bulk0(k+1) - z_w(k)*(bulk1(k+1) - bulk2(k+1)*z_w(k))   ! :404 이웃층 bulk 를 z_w 에서 재평가
bulk_dn = bulk0(k)   - z_w(k)*(bulk1(k)   - bulk2(k)*z_w(k))     ! :407
den_up = den1(k+1)*bulk_up/(bulk_up+0.1·z_w) ; den_dn = ...      ! :412-413
bvf(k) = -g*(den_up-den_dn)/(0.5(den_up+den_dn)*(z_r(k+1)-z_r(k))) ! :414-416
bvf(0)=bvf(N)=0                                                   ! :422-423 경계
```
→ **단열 재평가**(compressibility 반영)로 성층 계산. KPP·interior mixing 이 소비([[roms_kpp_boundary_layer]]·[[roms_vertical_mixing]]는 bvf 를 입력으로만 사용, 산출은 여기).

## 6. alpha/beta 열팽창·염수축 (:427-464) + in-situ/potential split (:474-482)
```fortran
Tcof=-(DbulkDT·cff1+Dden1DT·cff2) ; Scof=(DbulkDS·cff1+Dden1DS·cff2)  ! :445-450
alpha=Tcof/wrk ; beta=Scof/wrk ; alfaobeta=Tcof/Scof(LMD_DDMIX)        ! :459-461,454
```
★**표면만**(`DO k=N,N` :438) — DDMIX 시에만 전연직(:436). in-situ `rho=den` vs **potential `pden=den1-1000`**(surface 기준) 별도 루프(:474-482, "adjoint 편의" :471).

## 7. linear EOS branch (:576-886)
```fortran
rho = R0 - R0*Tcoef*(T-T0) + R0*Scoef*(S-S0)         ! :699-703
bvf = -gorho0*(rho(k+1)-rho(k))/(z_r(k+1)-z_r(k))     ! :760 단순 차분(≠비선형 단열)
alpha=ABS(Tcoef) ; beta=ABS(Scoef)                    ! :775-777 상수
```
★**bvf 이산화가 EOS 분기별로 다름**(비선형=단열 재평가 vs 선형=단순차분) — 하류 mixing 이 EOS 선택에 의존.

## 8. Cross-model 대조 — ROMS rho_eos vs EFDC calbuoy

| 항목 | ROMS `rho_eos.F` | EFDC `calbuoy.f90` |
|---|---|---|
| 계보 | Jackett-McDougall 1995 (UNESCO 재적합) | Mellor 1991 (UNESCO 근사) |
| base 상수 | Q00=999.842594·U00=0.824493 | 동일(999.842594·0.824493) |
| **압력/압축률** | **포함**(secant bulk, Tp=z_r) | **생략**(P=0 surface EOS) |
| baseline | den-1000 anomaly | (ρ/ρ₀)-1 buoyancy, ρ₀ 동결 |
| bvf/성층 | 여기서 산출(단열) | B 만, bvf 별도 |
| in-situ/potential | 분리(rho/pden) | 단일 |
| 유사 feedback | 있음(SED_DENS) | 있음(TVAR1S/W) |
| linear 옵션 | NONLIN_EOS 미정의 | IBSC==1(진단) |

## 9. 주요 findings
- **압축률 유무**가 ROMS vs EFDC 핵심 차이(ROMS 심해 압축 반영, EFDC surface).
- **bvf 이산화 EOS 분기 의존**(비선형 단열 vs 선형 차분) — 매뉴얼 미명시.
- **alpha/beta 표면만**(DDMIX 제외) — column-wide 가정 주의.
- **인용 1992 vs 1995 내부 불일치**: 헤더 산문 "1992"(:14) vs Reference "1995"(:31-35) — canonical=1995 JAOT 12:381-389.
- **check value(sound=1548.88 등, :21-29)는 문서용** — 이 루틴은 음속 미산출(den/bulk/alpha/beta 만).

## 10. 관련
- [[roms_nonlinear_core_remaining]] — §2 부분커버(본 노트가 승격·bvf/alpha-beta/linear 충전)
- [[roms_baroclinic_3d]] — prsgrd 압력구배(rho 소비)
- [[roms_kpp_boundary_layer]]·[[roms_vertical_mixing]] — bvf 소비처
- [[efdc_baroclinic_eos]] — ★cross-model EOS 대조(EFDC Mellor-UNESCO surface)
- **Primary**: Jackett-McDougall 1995 JAOT 12:381-389 (소스인용) ← UNESCO/EOS-80.
