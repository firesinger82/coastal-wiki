---
title: "ROMS 상태방정식 source-analysis — rho_eos.F (Jackett-McDougall 1995 비선형 EOS + Brunt-Väisälä bvf + alpha/beta), EFDC 대조"
topic: roms-equation-of-state
canonical_source: self
citation_status: verified
verification_method: "ROMS raw source 직접 read: ROMS/Nonlinear/rho_eos.F(889줄) + Modules/mod_eoscoef.F — den1 다항식(:274-285)·bvf 단열(:404-416)·Q00=999.842594(mod_eoscoef.F:50) file:line 직접 검증. 소스주석 primary Jackett-McDougall 1995 JAOT 12:381-389(:31-35). roms_nonlinear_core_remaining §2 부분커버 승격+bvf/alpha-beta/linear 갭 충전. EFDC [efdc_baroclinic_eos](../../EFDC/source-analysis/efdc_baroclinic_eos.md) cross-model 대조. 2026-10-14 ROMS recovery 대조 보고서 반영."
last_source_check: "2026-10-14 (recovery 대조 반영)"
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
> **정체**: 온도·염분·압력(≈수심) → 밀도 → baroclinic 압력구배·성층 bvf. 관련 core 노트는 [roms_nonlinear_core_remaining](roms_nonlinear_core_remaining.md) §2다. EFDC [efdc_baroclinic_eos](../../EFDC/source-analysis/efdc_baroclinic_eos.md)와 cross-model 대조는 §8에 있다.

## 0. NONLIN_EOS 이원 구조

`rho_eos`(driver :47-106) → `rho_eos_tile` **두 배타적 본체**(컴파일 타임):
- **nonlinear** (:111-570, `#ifdef NONLIN_EOS`) — Jackett-McDougall 1995 다항식
- **linear** (:576-886, `#ifndef NONLIN_EOS`) — 요약식 `rho=R0-R0·Tcoef(T-T0)+R0·Scoef(S-S0)`는 `-1000` 대입 전의 물리 밀도이다. 이 식의 염분항은 `SALINITY`를 정의한 경로에 해당한다 (`ROMS/Nonlinear/rho_eos.F:699–704,716`; [theory-numerics 수정안 RTN-391](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#4-노트-대조와-수정안)). [10-14 전수 검증 정정]

CPP `NONLIN_EOS`(cppdefs.h:71). 옵셔널 출력 CPP 게이팅(driver :88-98): `bvf`←`BV_FREQUENCY`, `alpha/beta`←`LMD_SKPP||LMD_BKPP||BULK_FLUXES||BALANCE_OPERATOR`, `alfaobeta`←`LMD_DDMIX`.

## 1. 계수 (mod_eoscoef.F) — ★EFDC 와 공유 UNESCO/EOS-80 base

```fortran
Q00 = 999.842594     ! :50  1-atm 밀도 상수항
U00 = 0.824493       ! :56  염분 선형항
W00 = 4.8314e-04     ! :64  염분 제곱항
A00 = 1.909256e+04   ! :24  secant bulk modulus
```
`Q00=999.842594`·`U00=0.824493`·`W00=4.8314e-04`의 값은 EFDC `calbuoy.f90`의 해당 계수와 같다 (`ROMS/Modules/mod_eoscoef.F:50,56,64`; `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calbuoy.f90:61,128,134`). ROMS의 참고문헌 주석은 Jackett와 McDougall의 1995년 논문을 인용한다 (`ROMS/Nonlinear/rho_eos.F:31–35`). EFDC의 주석은 Mellor의 UNESCO 상태방정식 근사를 명시한다 (`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calbuoy.f90:12–14`; [EFDC 노트](../../EFDC/source-analysis/efdc_baroclinic_eos.md)). [10-14 전수 검증 정정]

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

## 5. ★Brunt-Väisälä bvf — 단열 parcel (:390-424)
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
→ **단열 재평가**(compressibility 반영)로 성층 계산. KPP·interior mixing 이 소비([roms_kpp_boundary_layer](roms_kpp_boundary_layer.md)·[roms_vertical_mixing](roms_vertical_mixing.md)는 bvf 를 입력으로만 사용, 산출은 여기).

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
선형 식에서 `R0`부터 시작한 값은 `-1000` 대입 전의 물리 밀도이다. (`ROMS/Nonlinear/rho_eos.F:699-703`; [수정안 RTN-391](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#4-노트-대조와-수정안))
밀도 편차 대입 원문은 `ROMS/Nonlinear/rho_eos.F:716`의 `            rho(i,j,k)=rho(i,j,k)-1000.0_r8`이다.
최종 `rho`와 `pden`은 1000 kg/m³ 기준 편차이다 (`ROMS/Nonlinear/rho_eos.F:355,476–479,716–720`; 수정안 RTN-391). [10-14 전수 검증 보완]

★**bvf 이산화가 EOS 분기별로 다름**(비선형=단열 재평가 vs 선형=단순차분) — 하류 mixing 이 EOS 선택에 의존.

## 8. Cross-model 대조 — ROMS rho_eos vs EFDC calbuoy

| 항목 | ROMS `rho_eos.F` | EFDC `calbuoy.f90` |
|---|---|---|
| 계보 | Jackett-McDougall 1995 (UNESCO 재적합) | Mellor 1991 (UNESCO 근사) |
| base 상수 | Q00=999.842594·U00=0.824493 | 동일(999.842594·0.824493) |
| **압력/압축률** | **포함**(secant bulk, Tp=z_r) | **생략**(P=0 surface EOS) |
| baseline | 최종 `rho`·`pden`은 1000 kg/m³ 기준 편차이다 (`ROMS/Nonlinear/rho_eos.F:355,476–479,716–720`; 수정안 RTN-391). | 부력은 `(ρ/ρ₀)-1`이다. 참조밀도 ρ₀는 상수 참조온도로 계산한다 (`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calbuoy.f90:57–62,137`). [10-14 전수 검증 보완] |
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
- [roms_nonlinear_core_remaining](roms_nonlinear_core_remaining.md) — §2 부분커버(본 노트가 승격·bvf/alpha-beta/linear 충전)
- [roms_baroclinic_3d](roms_baroclinic_3d.md) — prsgrd 압력구배(rho 소비)
- [roms_kpp_boundary_layer](roms_kpp_boundary_layer.md)·[roms_vertical_mixing](roms_vertical_mixing.md) — bvf 소비처
- [efdc_baroclinic_eos](../../EFDC/source-analysis/efdc_baroclinic_eos.md) — ★cross-model EOS 대조(EFDC Mellor-UNESCO surface)
- **Primary**: Jackett-McDougall 1995 JAOT 12:381-389 (소스인용) ← UNESCO/EOS-80.

## 문서와 코드 차이 (10-14 대조)

출처: [theory-numerics](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md), [inputs](../../../_staging/recovery/compare/roms-inputs-vs-code.md)의 수정안·차이 결론·최종 전수 검증 기록.

문서 판: ROMS 위키 wikitext(2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json)). 코드 판: 원본 저장소 HEAD `57aecf58`(2026-09-18, roms-4.2 이후 4.3 개발).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| inputs:RI1-0690 | 선형 상태식과 밀도 편차 | `User/External/roms.in:2402` `! Ignoring pressure, the linear equation of state is:`<br>`User/External/roms.in:2404` `!              rho(:,:,:) = R0 - R0 * TCOEF * (t(:,:,:,:,itemp) - T0)`<br>`User/External/roms.in:2405` `!                              + R0 * SCOEF * (t(:,:,:,:,isalt) - S0)`<br>`User/External/roms.in:2407` `!              Typical values:     R0 = 1027.0  kg/m3`<br>`User/External/roms.in:2408` `!                                  T0 = 10.0    Celsius`<br>`User/External/roms.in:2409` `!                                  S0 = 35.0    nondimensional`<br>`User/External/roms.in:2410` `!                               TCOEF = 1.7d-4  1/Celsius`<br>`User/External/roms.in:2411` `!                               SCOEF = 7.6d-4  1/nondimensional` | `ROMS/Nonlinear/rho_eos.F:692` `!  Compute "in situ" density anomaly (kg/m3 - 1000) using the linear`<br>`ROMS/Nonlinear/rho_eos.F:699` `rho(i,j,k)=R0(ng)-                                          &`<br>`ROMS/Nonlinear/rho_eos.F:700` `&                 R0(ng)*Tcoef(ng)*(t(i,j,k,nrhs,itemp)-T0(ng))`<br>`ROMS/Nonlinear/rho_eos.F:701` `#  ifdef SALINITY`<br>`ROMS/Nonlinear/rho_eos.F:702` `rho(i,j,k)=rho(i,j,k)+                                      &`<br>`ROMS/Nonlinear/rho_eos.F:703` `&                 R0(ng)*Scoef(ng)*(t(i,j,k,nrhs,isalt)-S0(ng))`<br>`ROMS/Nonlinear/rho_eos.F:716` `rho(i,j,k)=rho(i,j,k)-1000.0_r8`<br>`ROMS/Nonlinear/rho_eos.F:705` `#  if defined SEDIMENT && defined SED_DENS`<br>`ROMS/Nonlinear/rho_eos.F:714` `rho(i,j,k)=rho(i,j,k)+SedDen`<br>`ROMS/Nonlinear/rho_eos.F:717` `#  ifdef MASKING`<br>`ROMS/Nonlinear/rho_eos.F:718` `rho(i,j,k)=rho(i,j,k)*rmask(i,j)` | F 표기 차이 | 선형 상태식의 문서 rho는 밀도이다. 코드의 rho는 마스크 적용 전에 밀도에서 1000.0_r8을 뺀 밀도 편차이다. SALINITY는 염분항을 켠다. SEDIMENT와 SED_DENS를 함께 정의하면 퇴적물의 밀도 기여도 더한다. |
| inputs:RI1-1010 | TCOEF·SCOEF 절댓값 | 대상 문서는 입력 이름과 의미를 설명한다. 이 후처리 식·검사·덮어쓰기 조건은 적지 않는다. | `ROMS/Utility/read_phypar.F:1066` `CASE ('TCOEF')`<br>`ROMS/Utility/read_phypar.F:1067` `Npts=load_r(Nval, Rval, Ngrids, Tcoef)`<br>`ROMS/Utility/read_phypar.F:1069` `Tcoef(ng)=ABS(Tcoef(ng))`<br>`ROMS/Utility/read_phypar.F:1071` `CASE ('SCOEF')`<br>`ROMS/Utility/read_phypar.F:1072` `Npts=load_r(Nval, Rval, Ngrids, Scoef)`<br>`ROMS/Utility/read_phypar.F:1074` `Scoef(ng)=ABS(Scoef(ng))` | C 문서 누락 | 두 선형 상태식 계수를 ABS로 바꾼다. 문서의 양수 예제는 같다. 음수 입력의 부호를 보존하지 않는다. |
| theory-numerics:RTN-010 | 밀도 기준 기호 | `Equations_of_Motion.wiki:80` `\| <math>\rho_o + \rho(x,y,z,t)</math>`<br>`Equations_of_Motion.wiki:81` `\| total ''in situ'' density` | `ROMS/Nonlinear/rho_eos.F:355` `            den(i,k)=den(i,k)-1000.0_r8`<br>`ROMS/Nonlinear/rho_eos.F:476` `            rho(i,j,k)=den(i,k)` | F 표기 차이 | 코드의 rho는 실제 밀도에서 1000 kg m^-3를 뺀 값이다. |
| theory-numerics:RTN-160 | rho 평균 정의 식 (19) | `Numerical_Solution_Technique.wiki:497` `\|<math display="block">\overline{\rho} = \frac{1}{D} \int_{-h}^\zeta \rho dz , \quad`<br>`Numerical_Solution_Technique.wiki:498` `  \rho^\star = \frac{1}{\frac{1}{2} D^2} \int_{-h}^\zeta`<br>`Numerical_Solution_Technique.wiki:499` `  \left\{ \int_z^\zeta \rho dz^{\prime} \right\} dz </math><!--\eqno{(19)}-->` | `ROMS/Nonlinear/rho_eos.F:371` `          cff1=den(i,N(ng))*Hz(i,j,N(ng))`<br>`ROMS/Nonlinear/rho_eos.F:372` `          rhoS(i,j)=0.5_r8*cff1*Hz(i,j,N(ng))`<br>`ROMS/Nonlinear/rho_eos.F:373` `          rhoA(i,j)=cff1`<br>`ROMS/Nonlinear/rho_eos.F:374` `        END DO`<br>`ROMS/Nonlinear/rho_eos.F:375` `        DO k=N(ng)-1,1,-1`<br>`ROMS/Nonlinear/rho_eos.F:376` `          DO i=IstrT,IendT`<br>`ROMS/Nonlinear/rho_eos.F:377` `            cff1=den(i,k)*Hz(i,j,k)`<br>`ROMS/Nonlinear/rho_eos.F:378` `            rhoS(i,j)=rhoS(i,j)+Hz(i,j,k)*(rhoA(i,j)+0.5_r8*cff1)`<br>`ROMS/Nonlinear/rho_eos.F:379` `            rhoA(i,j)=rhoA(i,j)+cff1`<br>`ROMS/Nonlinear/rho_eos.F:380` `          END DO`<br>`ROMS/Nonlinear/rho_eos.F:381` `        END DO`<br>`ROMS/Nonlinear/rho_eos.F:382` `        cff2=1.0_r8/rho0`<br>`ROMS/Nonlinear/rho_eos.F:383` `        DO i=IstrT,IendT`<br>`ROMS/Nonlinear/rho_eos.F:384` `          cff1=1.0_r8/(z_w(i,j,N(ng))-z_w(i,j,0))`<br>`ROMS/Nonlinear/rho_eos.F:385` `          rhoA(i,j)=cff2*cff1*rhoA(i,j)`<br>`ROMS/Nonlinear/rho_eos.F:386` `          rhoS(i,j)=2.0_r8*cff1*cff1*cff2*rhoS(i,j)` | F 표기 차이 | rhoA와 rhoS는 1000 kg m^-3 기준 이상 밀도를 rho0로 나눈 수직 모멘트이다. |
| theory-numerics:RTN-161 | σ 변환의 평균 식 (20) | `Numerical_Solution_Technique.wiki:503` `Changing the vertical coordinate to <math>\sigma</math> yields:`<br>`Numerical_Solution_Technique.wiki:505` `{\| class="eqno"`<br>`Numerical_Solution_Technique.wiki:506` `\|<math display="block"> \overline{\rho} =  \int_{-1}^0 \rho d\sigma , \quad`<br>`Numerical_Solution_Technique.wiki:507` `  \rho^\star = 2 \int_{-1}^0`<br>`Numerical_Solution_Technique.wiki:508` `  \left\{ \int_\sigma^0 \rho d\sigma^{\prime} \right\} d\sigma </math><!--\eqno{(20)}-->` | `ROMS/Nonlinear/rho_eos.F:371` `          cff1=den(i,N(ng))*Hz(i,j,N(ng))`<br>`ROMS/Nonlinear/rho_eos.F:372` `          rhoS(i,j)=0.5_r8*cff1*Hz(i,j,N(ng))`<br>`ROMS/Nonlinear/rho_eos.F:373` `          rhoA(i,j)=cff1`<br>`ROMS/Nonlinear/rho_eos.F:374` `        END DO`<br>`ROMS/Nonlinear/rho_eos.F:375` `        DO k=N(ng)-1,1,-1`<br>`ROMS/Nonlinear/rho_eos.F:376` `          DO i=IstrT,IendT`<br>`ROMS/Nonlinear/rho_eos.F:377` `            cff1=den(i,k)*Hz(i,j,k)`<br>`ROMS/Nonlinear/rho_eos.F:378` `            rhoS(i,j)=rhoS(i,j)+Hz(i,j,k)*(rhoA(i,j)+0.5_r8*cff1)`<br>`ROMS/Nonlinear/rho_eos.F:379` `            rhoA(i,j)=rhoA(i,j)+cff1`<br>`ROMS/Nonlinear/rho_eos.F:380` `          END DO`<br>`ROMS/Nonlinear/rho_eos.F:381` `        END DO`<br>`ROMS/Nonlinear/rho_eos.F:382` `        cff2=1.0_r8/rho0`<br>`ROMS/Nonlinear/rho_eos.F:383` `        DO i=IstrT,IendT`<br>`ROMS/Nonlinear/rho_eos.F:384` `          cff1=1.0_r8/(z_w(i,j,N(ng))-z_w(i,j,0))`<br>`ROMS/Nonlinear/rho_eos.F:385` `          rhoA(i,j)=cff2*cff1*rhoA(i,j)`<br>`ROMS/Nonlinear/rho_eos.F:386` `          rhoS(i,j)=2.0_r8*cff1*cff1*cff2*rhoS(i,j)` | B 문서 오기 | 일반 S 좌표의 평균 적분에는 `H_z/D`의 Jacobian을 포함한다. |
| theory-numerics:RTN-194 | 비선형·선형 EOS 선택 | `Numerical_Solution_Technique.wiki:728` `The density is obtained from temperature and salinity via an equation of state. ROMS provides a choice of a nonlinear equation of state <math>\rho = \rho(T,S,z)</math> or a linear equation of state <math>\rho = \rho(T)</math>. The nonlinear equation of state has been modified and now corresponds to the UNESCO equation of state as derived by ` … `Jackett and McDougall (1995)` … `. It computes '' in situ'' density as a function of potential temperature, salinity and pressure.` | `ROMS/Nonlinear/rho_eos.F:259` `            Tt=MAX(-2.0_r8,t(i,j,k,nrhs,itemp))`<br>`ROMS/Nonlinear/rho_eos.F:260` `#  ifdef SALINITY`<br>`ROMS/Nonlinear/rho_eos.F:261` `            Ts=MAX(0.0_r8,t(i,j,k,nrhs,isalt))`<br>`ROMS/Nonlinear/rho_eos.F:262` `            sqrtTs=SQRT(Ts)`<br>`ROMS/Nonlinear/rho_eos.F:263` `#  else`<br>`ROMS/Nonlinear/rho_eos.F:264` `            Ts=0.0_r8`<br>`ROMS/Nonlinear/rho_eos.F:265` `            sqrtTs=0.0_r8`<br>`ROMS/Nonlinear/rho_eos.F:266` `#  endif`<br>`ROMS/Nonlinear/rho_eos.F:267` `            Tp=z_r(i,j,k)`<br>`ROMS/Nonlinear/rho_eos.F:268` `            Tpr10=0.1_r8*Tp`<br>`ROMS/Nonlinear/rho_eos.F:699` `            rho(i,j,k)=R0(ng)-                                          &`<br>`ROMS/Nonlinear/rho_eos.F:700` `     &                 R0(ng)*Tcoef(ng)*(t(i,j,k,nrhs,itemp)-T0(ng))`<br>`ROMS/Nonlinear/rho_eos.F:701` `#  ifdef SALINITY`<br>`ROMS/Nonlinear/rho_eos.F:702` `            rho(i,j,k)=rho(i,j,k)+                                      &`<br>`ROMS/Nonlinear/rho_eos.F:703` `     &                 R0(ng)*Scoef(ng)*(t(i,j,k,nrhs,isalt)-S0(ng))`<br>`ROMS/Nonlinear/rho_eos.F:704` `#  endif` | C 문서 누락 | 선형 EOS도 SALINITY를 켜면 온도와 염분에 의존한다. |
| theory-numerics:RTN-391 | EOS·전역 상태 노트의 밀도 기준 | 반영 전 노트 인용: `_staging/recovery/compare/roms-theory-numerics-vs-code.md:711` `` - **linear** (:576-886, `#ifndef NONLIN_EOS`) — `rho=R0-R0·Tcoef(T-T0)+R0·Scoef(S-S0)` ``<br>`_staging/recovery/compare/roms-theory-numerics-vs-code.md:711` `\| baseline \| den-1000 anomaly \| (ρ/ρ₀)-1 buoyancy, ρ₀ 동결 \|` | `ROMS/Nonlinear/rho_eos.F:699` `            rho(i,j,k)=R0(ng)-                                          &`<br>`ROMS/Nonlinear/rho_eos.F:700` `     &                 R0(ng)*Tcoef(ng)*(t(i,j,k,nrhs,itemp)-T0(ng))`<br>`ROMS/Nonlinear/rho_eos.F:701` `#  ifdef SALINITY`<br>`ROMS/Nonlinear/rho_eos.F:702` `            rho(i,j,k)=rho(i,j,k)+                                      &`<br>`ROMS/Nonlinear/rho_eos.F:703` `     &                 R0(ng)*Scoef(ng)*(t(i,j,k,nrhs,isalt)-S0(ng))`<br>`ROMS/Nonlinear/rho_eos.F:704` `#  endif`<br>`ROMS/Nonlinear/rho_eos.F:716` `            rho(i,j,k)=rho(i,j,k)-1000.0_r8` | C 문서 누락 | 물리 밀도와 1000 kg/m³ 기준 저장 편차를 같은 rho 기호로 합치지 않는다. [10-14 전수 검증 정정] |
