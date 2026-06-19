---
title: "efdc dispersion (horizontal momentum diffusion)"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable / EFDC-GVC raw source 직접 read (models/EFDC/raw/source_code/), Card C12 매뉴얼 페이지 (models/EFDC/raw/manuals/confluence/spaces/ECIG/.../Card_Image_12.md) 및 EE12 Turbulence 페이지 (.../EK/.../Turbulence.md) 직접 인용, Theory v12 §2.1.5 Eq 2.27 (models/EFDC/manual-notes/efdc-theory-v12-ch2-hydrodynamics.md) cross-ref"
note_author: "Claude Opus 4.7 (1M context) source-code 직접 read"
note_date: 2026-05-28
verification_by: "사용자 + Claude source-code direct read"
verification_date: 2026-05-28
---

## Scope

EFDC의 horizontal momentum diffusion (HMD) sub-routine — Smagorinsky subgrid-scale + 상수 AHO background viscosity 결합. EFDC-GVC `CALHDMF`·`CALDIFF` (2001 Hamrick) vs EFDC+ `CALHDMF`(2TL)·`CALHDMF3`(3TL) 비교, `AHO/AHD` (scalar) vs `AHOXY/AHDXY` (cell-by-cell map via `AHMAP.INP`), `ISHDMF` (0/1/2) 세 옵션의 wall-effect 처리, `ISWAVE`-driven wave-breaking dispersion 가산항을 다룬다. Vertical viscosity는 [[efdc_turbulence]] 별도.

## Source basis

- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calhdmf.f90` (399 lines) — 2-time-level (2TL) HMD, SGZ 호환, primary version.
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calhdmf3.f90` (340 lines) — 3-time-level (3TL) variant (AQEA legacy).
- `models/EFDC/raw/source_code/EFDC-GVC/calhdmf.for` (615 lines) — EFDC-FULL v1.0a Hamrick 2001-11 original.
- `models/EFDC/raw/source_code/EFDC-GVC/caldiff.for` (49 lines) — scalar horizontal diffusion via `AH(L,K)`.
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:621, 3722-3795` — Card C12 read + spatially-variable mapping logic.
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mod_var_global.f90:991-992, 1098-1099` — `AHO/AHD` scalar + `AHOXY/AHDXY` array declarations.
- `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_12.md` — C12 input card (AHO, AHD, AVO, ABO, AVMX, ABMX, VISMUD, AVCON, ZBRWALL).
- `models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/.../Turbulence.md` — EE12 GUI Turbulent Diffusion tab (ISHMD = ISHDMF 매핑).
- `models/EFDC/manual-notes/efdc-theory-v12-ch2-hydrodynamics.md:203-209` — Theory v12 §2.1.5 Eq 2.27 Smagorinsky 표현 + Cs 권장 범위.

## 1. Smagorinsky subgrid-scale closure (이론)

Theory v12 §2.1.5 p.16 Eq 2.27:

$$A_H = C_s \, \Delta x \, \Delta y \, \sqrt{(\partial_x u)^2 + (\partial_y v)^2 + \tfrac{1}{2}(\partial_y u + \partial_x v)^2}$$

EFDC 변수 mapping: $C_s$ = `AHD` (dimensionless), $\Delta x \Delta y$ = `DXP(L)*DYP(L)` (cell area), 그리고 background 상수 `AHO` (m²/s)가 더해진다:

$$A_H(L,K) = \mathrm{AHOXY}(L) + \mathrm{AHDXY}(L) \cdot \mathrm{DXP}(L) \cdot \mathrm{DYP}(L) \cdot \sqrt{D}$$

여기서 $D$ = strain rate magnitude squared. Theory 식의 1/2 인자는 EFDC+ 2TL에서 2011-05 Paul Craig가 GVC 4분의 1을 절반으로 수정 (`calhdmf.f90:23` change record).

## 2. EFDC+ 2TL: `CALHDMF` (`calhdmf.f90`)

기본 dispatch — SGZ (sigma-z) grid + ISHDMF ≥ 1 일 때 호출.

### 2.1 Strain rate components

```fortran
! calhdmf.f90:116-118
DXU1(L,K) = (U(LE,K) - U(L,K))/DXP(L)   ! ∂u/∂x [1/s]
DYV1(L,K) = (V(LN,K) - V(L,K))/DYP(L)   ! ∂v/∂y
```

`DYU1` (∂u/∂y), `DXV1` (∂v/∂x): `ISHDMF == 1 or 2`의 wall-effect 분기 (line 121-181):
- **No wall effects** (line 124-140): central difference만.
- **Wall effects** (line 142-180): face-count `FACES = SUB3D+SUB3D(LEC)+SVB3D+SVB3D(LNC)` > 3 → open water average; 3 이하 → 인접 벽면에 log-law slip 적용. Slip 계수 `CSDRAG = 0.16 / log(1 + 0.5·DYP/ZBRWALL)²`, `SLIPFAC = SLIPCO·CSDRAG` (line 160-163).

`SXY = DYU1 + DXV1` (line 216) → cross-shear.

`SLIPCO` (line 62-65):
```fortran
SLIPCO = 1.
if( AHD > 0.0 ) SLIPCO = 0.5/SQRT(AHD)
```

### 2.2 Smagorinsky viscosity assembly

```fortran
! calhdmf.f90:225-243
if( AHD > 0.0 )then
  do K = 1,KC
    do LP = 1,LLHDMF(K,ND)
      L = LKHDMF(LP,K,ND)
      TMPVAL = AHDXY(L)*DXP(L)*DYP(L)
      DSQR = DXU1(L,K)**2 + DYV1(L,K)**2 + 0.5*SXY(L,K)**2
      AH(L,K) = AHOXY(L) + TMPVAL*SQRT(DSQR)
    enddo
  enddo
elseif( N < 10 .or. ISWAVE == 2 .or. ISWAVE == 4 )then
  AH(L,K) = AHOXY(L)   ! background only
endif
```

`DSQR`의 `0.5*SXY²` 인자가 Theory Eq 2.27의 1/2(∂yu+∂xv)² 와 정확히 일치.

### 2.3 Wave-breaking 추가 viscosity (`ISWAVE == 2 or 4`)

```fortran
! calhdmf.f90:246-294
if( ISWAVE == 2 .or. ISWAVE == 4 )then
  if( WVLSH > 0.0 .or. WVLSX > 0.0 )then
    ...
    DTMPH = WV(L).DISSIPA(K)**0.3333       ! dissipation^{1/3}
    TMPVAL = 2.*PI/WV(L).FREQ              ! wave period
    AHWVX = WVLSX*TMPVAL**2
    DTMPX = WV(L).DISSIPA(K)/HP(L)
    AH(L,K) = AH(L,K) + WVFACT*(WVLSH*DTMPH*HP(L) + AHWVX*DTMPX)
  endif
endif
```

`WVLSH` = depth-scale 계수, `WVLSX` = wavelength-scale 계수, `WV.DISSIPA(K)` = layer-wise wave dissipation 율, `WVFACT` = 0~1 ramp-up.

### 2.4 Diffusive momentum flux

```fortran
! calhdmf.f90:301-333 (ISHDMF == 1 or 2 branch)
FMDUX0 = ( DYP(L)*HP(L)*AH(L,K)*DXU1(L,K) - DYP(LW)*HP(LW)*AH(LW,K)*DXU1(LW,K) )*SUB(L)
FMDUY0 = ( DXU(LN)*HU(LN)*AH(LN,K)*SXY(LN,K) - DXU(L)*HU(L)*AH(L,K)*SXY(L,K) )*SUB(L)*SVB(L)*SVB(LN)
FMDVY0 = ( DXP(L)*HP(L)*AH(L,K)*DYV1(L,K) - DXP(LS)*HP(LS)*AH(LS,K)*DYV1(LS,K) )*SVB(L)
FMDVX0 = ( DYV(LE)*HV(LE)*AH(LE,K)*SXY(LE,K) - DYV(L)*HV(L)*AH(L,K)*SXY(L,K) )*SVB(L)*SUB(L)*SUB(LE)
```

`FMDUX/FMDUY/FMDVY/FMDVX`는 `CALEXP` (explicit momentum solver)에 전달되어 운동량 방정식의 viscous flux divergence 항이 된다.

### 2.5 ISHDMFILTER 시간 필터 (line 338-366)

```fortran
if( ISHDMFILTER > 0 .and. ((ISRESTI > 0 .and. NITER > 1) .or. NITER > 100) )then
  FMDUX(L,K) = FMDUX(L,K) + SIGN(MAX(1E-8, MIN(ABS(FMDUX0-FMDUX), ABS(0.25*FMDUX))), FMDUX0-FMDUX)
  ...
endif
```

25% growth-rate limiter — HMD 항의 급격한 변동 억제용 (run-up 100 step 후 또는 restart 시 활성).

## 3. EFDC+ 3TL: `CALHDMF3` (`calhdmf3.f90`)

`ISTL == 3` (Adams-Bashforth-Trapezoidal 3-time-level) + AQEA legacy 경로 (`calhdmf3.f90:22` change record "ADOPTED AQEA ISHDMF>0 FOR 3TL"). 핵심 차이:

### 3.1 Strain rate at SW corner

```fortran
! calhdmf3.f90:132-141
DXU1(L,K) = (U1(LE,K)-U1(L,K))/DXP(L)
DYV1(L,K) = (V1(LN,K)-V1(L,K))/DYP(L)
DYU1(L,K) = 2.*SUBO(LS)*(U1(L,K)-U1(LS,K))/(DYU(L)+DYU(LS))   ! SW corner avg
DXV1(L,K) = 2.*SVBO(LW)*(V1(L,K)-V1(LW,K))/(DXV(L)+DXV(LW))
```

이전 time-level `U1, V1` 사용 (`U, V` 가 아님).

### 3.2 Smagorinsky (cell-center + SW corner 분리)

```fortran
! calhdmf3.f90:166-174
AH(L,K)  = AHOXY(L) + AHDXY(L)*DXP(L)*DYP(L) &
            * SQRT( 2.*DXU1(L,K)**2 + 2.*DYV1(L,K)**2 &
                  + 0.0625*(DYU1(L,K)+DYU1(LN,K)+DYU1(LE,K)+DYU1(LNE,K) &
                          + DXV1(L,K)+DXV1(LN,K)+DXV1(LE,K)+DXV1(LNE,K))**2 )

AHC(L,K) = AHOXY(L) + AHDXY(L)*0.0625*((DXP(L)+DXP(LW)+DXP(LS)+DXP(LSW))**2) &
            * SQRT( 0.125*(DXU1(L,K)+DXU1(LW,K)+DXU1(LS,K)+DXU1(LSW,K))**2 &
                  + 0.125*(DYV1(L,K)+DYV1(LW,K)+DYV1(LS,K)+DYV1(LSW,K))**2 &
                  + (DYU1(L,K)+DXV1(L,K))**2 )
```

GVC 원본 식 그대로 (2× scaling + 1/16 corner avg)이며, `calhdmf.f90` (2TL)의 단순화된 `DSQR = DXU1² + DYV1² + 0.5*SXY²` 와 대비된다.

### 3.3 momentum flux (line 267-270)

```fortran
FMDUX0(L,K) = 2.0*DYP(L)*H1P(L)*AH(L,K)*DXU1(L,K)
FMDUY0(L,K) = 0.5*(DXU(L)+DXU(LS))*H1C(L)*AHC(L,K)*(DYU1(L,K)+DXV1(L,K))
FMDVY0(L,K) = 2.0*DXP(L)*H1P(L)*AH(L,K)*DYV1(L,K)
FMDVX0(L,K) = 0.5*(DYV(L)+DYV(LW))*H1C(L)*AHC(L,K)*(DYU1(L,K)+DXV1(L,K))
```

`AH` (centroid) + `AHC` (SW corner) 분리 사용 — GVC 원본 구조 유지.

## 4. EFDC-GVC: `CALHDMF` (`calhdmf.for`, Hamrick 2001-11)

EFDC+ 변경 이전의 원형. 핵심 인용:

```fortran
! calhdmf.for:7-15
C **  SUBROUTINE CALDMF CALCULATES THE HORIZONTAL VISCOSITY AND
C **  DIFFUSIVE MOMENTUM FLUXES. THE VISCOSITY, AH IS CALCULATED USING
C **  SMAGORINSKY'S SUBGRID SCALE FORMULATION PLUS A CONSTANT AHO
C
C     SMAGORINSKY, J., 1993: SOME HISTORICAL REMARKS ON THE USE OF
C     NONLINEAR VISCOSITIES. IN LARGE EDDY SIMULATION OF COMPLEX
C     ENGINEERING AND GEOPHYSICAL FLOWS. B. GALPERIN AND S. A. ORSZAG,
C     EDS. CAMBRIDGE UNIVERSITY PRESS, CAMBRIDGE, UK.
```

GVC는 Smagorinsky 1963 대신 1993 reprint를 인용 (Hamrick 코드 코멘트). Theory v12 §2.1.5는 Smagorinsky 1963 직접 인용.

```fortran
! calhdmf.for:306-318
DO K=1,KC
DO L=2,LA
  LN=LNC(L)
  LNE=LNEC(L)
  DSP=MIN(DXP(L),DYP(L))             ! grid scale (min of dx, dy)
  TMPVAL=AHD*DSP*DSP
  DSQR=DXU1(L,K)**2+0.25*(SXY2CC(L,K)**2+SXY2EE(L,K)**2 &
                        +SXY2NN(L,K)**2+SXY2CC(LNE,K)**2)
  AH(L,K)=AHO+TMPVAL*SQRT(DSQR)
ENDDO
ENDDO
```

GVC는 cell 4 corner의 `SXY²` 평균 사용 (1/4 인자). EFDC+ 2TL에서 Craig 2011이 이를 `DXU1² + DYV1² + 0.5*SXY²` 로 단순화·수정.

또한 GVC `DSP = MIN(DXP, DYP)` (cell의 짧은 변) — EFDC+ 2TL은 `DXP*DYP` (면적). 결과: 비등방 격자에서 GVC는 보수적, EFDC+ 2TL은 면적 비례.

## 5. EFDC-GVC: `CALDIFF` (`caldiff.for`) — 스칼라 확산

```fortran
! caldiff.for:6-44
SUBROUTINE CALDIFF (ISTL,M,CON1)
C **  SUBROUTINE CALDIFF CALCULATES THE HORIZONTAL DIFFUSIVE
C **  TRANSPORT OF DISSOLVED OR SUSPENDED CONSITITUENT M

DO K=1,KC
DO L=2,LA
  LS=LSC(L)
  FUHU(L,K)=FUHU(L,K)+0.5*SUB(L)*DYU(L)*HU(L)*(AH(L,K)+AH(L-1,K)) &
                          *(CON1(L-1,K)-CON1(L,K))*DXIU(L)
  FVHU(L,K)=FVHU(L,K)+0.5*SVB(L)*DXV(L)*HV(L)*(AH(L,K)+AH(LS,K)) &
                          *(CON1(LS,K)-CON1(L,K))*DYIV(L)
ENDDO
ENDDO
```

momentum HMD에서 계산된 `AH(L,K)` 를 그대로 scalar transport (salinity, temperature, contaminant) 확산 flux에 적용 — 즉 Schmidt/Prandtl 수 1로 가정 (momentum과 동일 diffusivity). EFDC+에서는 `ISHDMF == 2` 옵션에서만 scalar diffusion 활성 (EE12 Turbulence 문서: "When `Smagorinsky` is selected (ISHMD=1) ... contaminant diffusion is off and not accounted for. ... When `Smagorinsky with Wall Drag and WC Diffusion` is selected (ISHMD=2), then the full HMD is used as well as wall effects. This option also applies diffusivities to all constituent transport, which includes salinity and temperatures").

## 6. 입력 파라미터 — Card C12

`models/EFDC/raw/manuals/confluence/spaces/ECIG/.../Card_Image_12.md`:

```
C12 | AHO | AHD | AVO | ABO | AVMX | ABMX | VISMUD | AVCON | ZBRWALL
    | 0   | 0.025 | 0.000001 | 1.00E-07 | 0.000001 | 1.00E-07 | 0 | 1 | 0.002
```

| 변수 | 의미 | 단위 | Default | 코드 위치 |
|---|---|---|---|---|
| `AHO` | Constant horizontal momentum/mass diffusivity (m²/s) | m²/s | 0 | `input.f90:621` read, `:3737, 3742` use |
| `AHD` | Dimensionless Smagorinsky coefficient $C_s$ (ISHDMF>0 필요) | — | 0.025 | `input.f90:621, 3791-3794` |
| `ZBRWALL` | 측벽 log-law 거칠기 (ISHDMF=2 wall effect) | m | 0.002 | `input.f90:621` |
| `ISHDMF` | HMD 옵션 (0/1/2 — EE GUI ISHMD 동일) | flag | — | `input.f90` Card C2 |

**Default 0.025 주의**: Theory §2.1.5 권장 범위 $C_s = 0.1\text{-}0.2$ (Smagorinsky 표준) 보다 훨씬 작음. EE GUI 기본값은 EFDC 전통 — 사용자가 격자 해상도 따라 조정 필요. Smagorinsky 1963 원논문 권장 0.16-0.17.

### 6.1 ISHDMF 옵션 매핑 (EE12 Turbulence 페이지)

| ISHDMF / ISHMD | 거동 |
|---|---|
| 0 | HMD off — `AH = AHO` (`AHOXY`) 상수만 |
| 1 | Smagorinsky on, **벽 효과 없음**, **scalar 확산 미적용** |
| 2 | Smagorinsky + 벽 log-law slip + **scalar (salinity, temperature) 확산 적용** |

### 6.2 Spatially-variable AHO/AHD — `AHMAP.INP`

`input.f90:3722-3795`:

```fortran
! AHO < 0 → cell area 의존
if( AHO < 0. )then
  do L = 2,LA
    AHOXY(L) = ABS(AHO)*DXP(L)*DYP(L)   ! input.f90:3727
  enddo
else
  AHOXY = AHO                            ! input.f90:3737
endif

! AHD < 0 → AHMAP.INP 파일에서 cell-by-cell read
if( AHD < 0. )then
  open(1,FILE = 'ahmap.inp')             ! input.f90:3757
  do LL = 2,LA_Global
    read(1,*,END=200) LG, ITMP, JTMP, T1, T2
    R2D_Global(LG,1) = T1                ! AHO per cell
    R2D_Global(LG,2) = T2                ! AHD per cell
  enddo
endif
```

EE12 GUI에서 polygon 영역별 AHO/AHD 할당 → 저장 시 `AHMAP.INP` 자동 생성 (Turbulence 문서 §"spatially variable AHD option"). 입력 AHO 가 음수면 cell-area scaling 활성 (numerical diffusion 보정용으로 큰 격자 영역에서 AHO 증가).

## 7. Cross-references

- **운동량 방정식 통합**: [[efdc_hydro_core]] `CALEXP/CALEXP2T` 가 `FMDUX/FMDUY/FMDVY/FMDVX` flux를 momentum balance에 합산.
- **Vertical diffusion 별개**: [[efdc_turbulence]] — Mellor-Yamada 2.5 / Galperin / Kantha-Clayson / Kantha 2003 / GOTM (vertical `AV`, `AB`).
- **Wave coupling**: [[efdc_waves]] (있다면) — `ISWAVE == 2/4` + `WV.DISSIPA(K)` 로 wave-breaking dispersion 가산.
- **Scalar 확산**: GVC `caldiff.for` ↔ EFDC+ `caltran.f90` (별도 노트 필요 시).
- **Theory 식**: [[efdc-theory-v12-ch2-hydrodynamics]] §2.1.5 Eq 2.27 (p.16).
- **Card C12 매뉴얼**: `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_12.md`.
- **EE GUI 매뉴얼**: `models/EFDC/raw/manuals/confluence/spaces/EK/.../Hydrodynamics_Module/Turbulence.md`.

## 8. 미해결 / 추가 보강 후보

- ~~`caldisp2.for`·`caldisp3.for` (GVC, 각 336·557 lines) — Taylor dispersion **사후처리** 도구.~~ **✅ 신설 완료**: [[efdc_caldisp_postprocess]] verified (2026-06-03) — 연직 전단×연직혼합 → 잔차(조석평균) dispersion 텐서 D_xx/xy/yx/yy. ISDISP=2(SVD)/3(LU+DISDIA 이상치 평활), N≥NDISP 마지막 조석주기 누적, /HLPF·TPN 정규화. DISTEN/UVTSC/UVERV/SINVAL/DISDIA.OUT. 본 HMD(main loop)와 별개 진단.
- `calhdmf.for` (GVC) line 245-255, 300-304, 418-433의 `AHSXY.DIA / AHNN.DIA / AHDIFF.DIA / AHD2.DIA` 디버그 출력 — EFDC+에서 제거되었으나 GVC 사용 시 진단 가치.
- ISHDMFILTER 활성 조건 (`NITER > 100 or restart` `calhdmf.f90:338`)의 25% growth limiter — 어떤 시나리오에서 numerical instability 흡수에 효과적인지 사용자 사례 누적 필요 (experience/ 후보).
- `LHDMF(L,K)` 및 `LKHDMF/LLHDMF` masking 로직 (계산되는 wet HMD 셀 식별, `calhdmf.f90:89-105`) — 부분-건조 셀 처리.
