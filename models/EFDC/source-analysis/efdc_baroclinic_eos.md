---
title: "EFDC+ 밀도 EOS + baroclinic 압력구배 source-analysis — calbuoy.f90 (Mellor-UNESCO) + calebi.f90 (buoyancy integrals) + FPGXE/FBBX"
topic: efdc-baroclinic-eos
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable(12.4, sha 3ed76b6) raw source 직접 read: calbuoy.f90(248)+calebi.f90(538) — IBSC==1 선형(:50)·ρ₀ quintic AT P=0(:57-62)·salinity UNESCO poly+ζ^1.5(:128-134)·B=(ρ/ρ₀)-1(:137) file:line 직접 검증. 소비처 calpuv9c.f90(FPGXE)·calexp.f90(FBBX IINTPG). 소스주석 primary Mellor 1991 JAOT 8:609(:14)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — calbuoy.f90:44-63·128-137 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/source-analysis/efdc_external_mode_solver.md
  - models/EFDC/source-analysis/efdc_bottom_friction.md
  - concepts/sst/04-code-and-tools.md
---

# EFDC+ 밀도 EOS + baroclinic 압력구배 — `calbuoy.f90` + `calebi.f90`

> 소스: [`calbuoy.f90`](../raw/source_code/EFDCPlus_Stable/EFDC/calbuoy.f90)(248, 밀도·부력) + [`calebi.f90`](../raw/source_code/EFDCPlus_Stable/EFDC/calebi.f90)(538, 외부모드 buoyancy 적분). 소비처 `calpuv9c.f90`(FPGXE/FPGYE)·`calexp.f90`(FBBX/FBBY).
> **정체**: 염분·수온 → 밀도(EOS) → 부력 → baroclinic 압력구배 → 밀도류. [[efdc_hydro_core]]:70-71 이 2줄 스케치(CALBUOY/CALEBI 이름+B=(ρ/ρ₀)-1)만 남긴 갭. EOS 다항식·ρ₀ baseline·SGZ face 적분·IINTPG 3형식·내부모드 shear 미문서.

## 1. `calbuoy.f90` — 밀도 EOS (Mellor 1991 ≈ UNESCO)

`SUBROUTINE CALBUOY(UPDATE)` (:9-248). 소스주석 (:12-14): "MELLOR'S APPROXIMATION TO THE UNESCO EQUATION OF STATE, **Mellor G.L., J. Atm and Ocean Tech vol 8 p 609 (1991)**". `UPDATE=.T.` → 이전 부력 `B1` 저장(3TL leapfrog, :68-79).

### 1.1 IBSC 밀도 모드
```fortran
IBSC==1: B(L,K) = 0.00075*SAL(L,K)     ! :50 선형 진단(★"FOR DIAGNOSTIC PURPOSES ONLY" :47)
IBSC==0: full Mellor-UNESCO 다항식      ! 아래
IBSC==2 / ISGOTM>0: GSW 잠재온도 변환    ! TEOS-10 (:94-97)
```

### 1.2 참조밀도 ρ₀ (:57-62) — ★동결 Boussinesq baseline
```fortran
! Density RHOO AT P = 0, S = 0, T = TEMO.  Only compute once (N<=5)
RHOO = 999.842594 + 6.793952D-2*TEM0 - 9.095290D-3*TEM0² + 1.001685D-4*TEM0³
     - 1.120083D-6*TEM0⁴ + 6.536332D-9*TEM0⁵     ! :61 순수물 quintic
```
`TEMO` 상수 참조온도, **전 도메인/전 run 단일 스칼라**(per-cell 아님) — Boussinesq baseline.

### 1.3 염분/수온 다항식 + 부력 (:128-137)
```fortran
RHO1 = RHOO + SSTMP*(0.824493 - 4.0899D-3*TEM0 + 7.6438D-5*TEM0² - ...)   ! :128-131 UNESCO S-terms
     + SQRT(SSTMP)*SSTMP*(-5.72466D-3 + ...) + 4.8314D-4*SSTMP²           ! :132-134 ★ζ^1.5 항
RHOW(L,K) = RHO1                    ! :136 밀도 [kg/m³]
B(L,K)    = (RHO1/RHOO) - 1.        ! :137 부력 [무차원]
```
온도전용(:148-151)·S+T full(:166-176) 분기. 유사 밀도보정(:234-237): `B = B*(1-TVAR1S) + TVAR1W`, `RHOW *= (1-TVAR1S+TVAR1W)` (부피변위 + 초과침수중량, ISTRAN(6/7) 시).

> ⚠ **surface EOS (압력 탈락)**: 다항식은 `P=0`에서 평가(:57), S/T 항에 압력/수심항 없음. GSW `PSW=(1-ZZ)*HP`(:94)는 **in-situ→잠재온도 변환에만** 사용, 밀도다항식엔 미투입. → EFDC+ 밀도 = Mellor **절단·압력무관** 근사(UNESCO 압축률/secant-bulk-modulus 분기 생략). 매뉴얼 "UNESCO EOS" 는 과대표현.

## 2. `calebi.f90` — 외부모드 buoyancy 적분 (:9-453)

부력을 연직적분해 centroid + 4면(W/E/S/N) 에서 압력구배 준비.
```fortran
DZCB = DZC*B ; BK 누적                              ! :106-125 centroid
BI1C = Σ DZC*BK                                     ! 단일적분
BI2C = Σ(DZC*BK + ZZ*DZC*B)                         ! 중간층높이 ZZ 가중 이중적분
BEC  = Σ DZC*B                                      ! bottom-slope 항용
```
- **SGZ per-face** (:156-262): 면별 층두께 `SGZKW/E/S/N`·높이 `ZZW/E/S/N`. **flat-bottom 단축** `KSZFLAT`(:54-61,136-154) → 표준 sigma centroid 로 환원.
- `INTERPB(L)`(:455-538): `IGRIDV>1`(SGZ Interpolated Vertical Grid) 시 B 를 면중점 보간.

## 3. 외부모드 baroclinic 압력구배 FPGXE (calpuv9c.f90:217-228)

`CALEBI` 호출(:171) → 적분값으로 조립:
```fortran
FPGXE = -SBX*SUBD*HU*GP*[ (BI2W(L)+BI2W(LW))*(HP(L)-HP(LW))          ! ① 수심구배
                        + 2*HU*(BI1W(L)-BI1W(LW))                     ! ② 적분부력 shear
                        + (BEW(L)+BEW(LW))*(BELV(L)-BELV(LW)) ]       ! ③ bottom-slope(sigma)보정
```
3-항 분해 = 수심구배 + 부력 shear + 저면경사(sigma) 보정. 결과 → 외부모멘텀 `FUHDYE/FVHDXE`(:256-257).

## 4. 내부모드 buoyancy shear FBBX/FBBY (calexp.f90:1162-1352)

`BSC>1.E-6 .and. KC>1` 게이트(:1167). **IINTPG 3 sigma-구배 형식** (steep bathymetry sigma 압력구배오차 억제):
```
IINTPG==0 : STANDARD      (:1207)
IINTPG==1 : JACOBIAN      (:1225)
IINTPG==2 : FINITE VOLUME (:1265)
```
+ Sigma-Z 전용 분기 `IGRIDV==1`/`>1`(:1169,1187-1204).

## 5. 주요 findings
- **surface EOS**: 압력 다항식 미포함(P=0) → 압축률 생략, "UNESCO EOS" 아니라 Mellor 절단근사.
- **IBSC==1 미문서 선형 진단**(B=0.00075·SAL, :50) — EOS 전체 우회.
- **ρ₀ 동결**: 참조온도 TEMO 단일 스칼라, N≤5 만 계산 → 전역 Boussinesq baseline.
- **유사-밀도 결합**: 부유사 loading 이 "water density" 에 이미 포함(:234-237).
- **IINTPG 0/1/2** 3형식 sigma-구배 — 매뉴얼은 통상 1문장 압축.
- **인용 누락**: calbuoy/calebi 는 Hamrick 1992·Blumberg-Mellor 1987(POM)·Fofonoff-Millard 1983(UNESCO) 직접 미인용(sigma baroclinic split·이중 buoyancy 적분이 canonical Hamrick/BM 구성임에도) — change-log 는 Paul Craig/DSI 만.

## 6. 관련
- [[efdc_hydro_core]] — CALEXP/CALPUV(본 노트가 상류 밀도/부력 공급, FPGXE/FBBX 소비)
- [[efdc_external_mode_solver]] — 외부모드 수위 CG(FPGXE 반영)
- [[efdc_bottom_friction]] — 동일 momentum 조립부 결합
- `concepts/sst/04-code-and-tools.md` — 수온/밀도 도메인 (cross-model EOS)
- **Primary**: Mellor 1991 JAOT 8:609(소스인용) ← UNESCO/Fofonoff-Millard 1983 · TEOS-10 GSW(잠재온도) · Hamrick 1992·Blumberg-Mellor 1987(uncited-attributable).
