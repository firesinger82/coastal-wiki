---
title: "efdc SEDZLJ sediment transport (s_main / s_sedzlj / s_shear / s_slope / s_bedload)"
topic: sediment-transport
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable raw source 직접 read (models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/), Card C36 매뉴얼 페이지 (models/EFDC/raw/manuals/confluence/spaces/ECIG/.../Card_Image_36.md) 직접 인용. Theory v12 §6.4 SEDZLJ cross-ref (manual-notes/efdc-theory-doc-v12.md:136), legacy 비교는 efdc-sediment-theory-2003.md."
note_author: "Claude Opus 4.7 (1M context) source-code 직접 read"
note_date: 2026-05-28
verification_by: "사용자 + Claude source-code direct read"
verification_date: 2026-05-28
---

## Scope

EFDC+의 **SEDZLJ** (Ziegler·Lick·Jones 알고리즘) sub-module 7개 sub-routine deep coverage — Card C36 `NSEDFLUME = 98/99` 활성 시 호출되는 multi-class·multi-bed-layer cohesive + non-cohesive 통합 sediment transport. Christoffersen-Jonsson 1985 wave-current shear, Gessler 1965 / Krone deposition probability, Sedflume-derived erosion rate, active-layer dynamics, Van Rijn 1981 bedload, Lick 2009 bed-slope correction을 다룬다. **기본 (Original) SedTran 와의 dispatch는 [[efdc_sediment]] §A 참조** — 본 노트는 SEDZLJ branch (SedTran-SEDZLJ/) 내부 detail.

## Source basis

- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_main.f90` (359 lines) — SEDZLJ_MAIN driver.
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90` (917 lines) — 핵심 erosion/deposition + active-layer 관리.
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90` (340 lines) — wave-current bottom shear (Christoffersen-Jonsson 1985).
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_slope.f90` (110 lines) — bed slope shear amplification (Lick 2009).
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90` (293 lines) — Van Rijn 1981 bedload transport.
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90` (769 lines) — bed initial condition (별도 covered).
- `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md` — Card C36 `NSEDFLUME` flag 정의.
- `models/EFDC/manual-notes/efdc-theory-doc-v12.md:47, 136, 177-179, 199` — Theory v12 §6.4 SEDZLJ TOC + Craig Jones contributor.
- `models/EFDC/manual-notes/efdc-sediment-theory-2003.md:104, 155, 169, 183` — Hamrick 2003 legacy SedTran 비교.

## 1. SEDZLJ_MAIN driver (`s_main.f90`)

```fortran
! s_main.f90:54-60
call SEDZLJ_SHEAR            ! *** wave-current bottom shear stress TAU(L)
if( ISSLOPE ) call SEDZLJ_SLOPE   ! *** bed slope adjustment
if( ICALC_BL > 0 )then       ! *** Bedload active
  call BEDLOADJ              ! *** Van Rijn transport
endif
```

```fortran
! s_main.f90:150 (per cell loop)
call SEDZLJ(L)               ! *** erosion + deposition + active layer + mass balance
```

### Dispatch 조건

`s_main.f90:64`:
```fortran
if( NSEDFLUME > 0 )then
```

Card C36 `NSEDFLUME`:
- **0** = EFDC main sediment functions (SedTran-Original, [[efdc_sediment]] §C-D)
- **98** = SEDZLJ
- **99** = SEDZLJ + toxics

### Settling (anti-diffusion, KC > 1)

`s_main.f90:96-136` — vertical layer-by-layer settling solve.
`s_main.f90:234-345` — `ISTOPT(6) > 0` 시 anti-diffusion tridiagonal solver (TVAR1S/W/N/E + TVAR2/3 working arrays). Thomas algorithm 형태.

### Bedload BC handling

`s_main.f90:158-230` — `NSBDLDBC > 0` 시 bedload outflow/recirculation BC. `LSBLBCU` (upstream) → `LSBLBCD` (downstream) cell 간 bedload mass 이송.

## 2. SEDZLJ erosion/deposition core (`s_sedzlj.f90`)

`SEDZLJ(L)` — 단일 cell `L` 기준 시간 step 처리.

### 2.1 Suspended load deposition probability (line 134-154)

**Gessler 1965** for $D_{50} \ge$ `BEDLOAD_CUTOFF` (≈ 200 μm):

```fortran
! s_sedzlj.f90:139-149
PY  = 1.7544 * (TCRSUS(NS)/(TAU(L) + 1e-18) - 1)   ! *** 1.7544 = 1/0.57 from Gessler
if( PY >= 0.0 )then
  PFY = SQR2PI*EXP(-0.5*PY*PY)                     ! *** Normal PDF
  PX  = ONE/(ONE + 0.33267*PY)
  PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX² + 0.93729*PX³)
else
  PY  = ABS(PY)
  ...
  PROB(NS) = PFY*(0.43618*PX - 0.12016*PX² + 0.93729*PX³)
endif
```

Hastings (1955) 근사식으로 정규분포 CDF 평가 (Gessler 표준편차 σ = 0.57).

**Krone** for $D_{50} <$ `BEDLOAD_CUTOFF` (≈ 200 μm):

```fortran
! s_sedzlj.f90:150-153
elseif( TAU(L) <= TCRSUS(NS) )then
  PROB(NS) = ONE - TAU(L)/TCRSUS(NS)               ! *** Krone (1962)
else
  PROB(NS) = 0.0
endif
```

### 2.2 Deposition flux

```fortran
! s_sedzlj.f90:158
DEPTSS(NS) = CTB(NS) * PROB(NS) * (DWS(NS) * DTSEDJ)
! *** CTB = bottom-layer concentration (g/cm³)
! *** DWS = settling velocity (cm/s)
! *** DTSEDJ = SEDZLJ time step (s)
```

`MAXDEPLIMIT` (line 157) 으로 layer 1 의 전 sediment mass 초과 deposition 차단.

### 2.3 Bedload deposition — Van Rijn equilibrium probability

```fortran
! s_sedzlj.f90:191-201
CSEDVR(NS) = 0.18*2.65*TRANS(L,NS)/DISTAR(NS)*0.65    ! *** Van Rijn 1981 Eq 21 equilibrium bedload conc
PROBVR(NS) = MIN(CSEDSS/CSEDVR(NS), 1.0)              ! *** Van Rijn deposition probability
DEPBL(NS)  = PROBVR(NS) * CBL(L,NS) * DWS(NS) * DTSEDJ
```

### 2.4 Active layer mass

```fortran
! s_sedzlj.f90:273-277
if( TAU(L)/TAUCRIT < 1.0 )then
  TACT = TACTM * D50AVG(L) * (BULKDENS(1,L) / 10000.0)
else
  TACT = TACTM * D50AVG(L) * (TAU(L)/TAUCRIT) * (BULKDENS(1,L)/10000.0)
endif
```

`TACTM` = active-layer thickness multiplier (보통 2~10), `D50AVG` = bed-surface 평균 입경 (μm), `BULKDENS` = 건조밀도 (g/cm³).

### 2.5 TAUCRIT (critical shear) 보간

```fortran
! s_sedzlj.f90:425-435
if( LAYERACTIVE(K,L) == 1 )then
  ! *** Active/deposited layer — D50AVG 선형 보간
  TAUCRIT = TAUCRITE(NSC0) + (TAUCRITE(NSC1)-TAUCRITE(NSC0))/(NSCD(2)-NSCD(1)) &
                            * (D50AVG(L) - NSCD(1))
  TAUCOR(K,L) = TAUCRIT
elseif( LAYERACTIVE(K,L) == 2 )then
  ! *** In-place sediment layer — Sedflume data depth interpolation
  SN01 = TSED(K,L)/TSED0(K,L)
  SN11 = (TSED0(K,L)-TSED(K,L))/TSED0(K,L)
  TAUCRIT = SN01*TAUCOR(K,L) + SN11*TAUCOR(K+1,L)
endif
```

`LAYERACTIVE(K,L)`:
- `0` = 층 부재
- `1` = active/deposited (computed from D50 grain-size class)
- `2` = in-place (initial-condition, Sedflume-derived)

### 2.6 Erosion rate 두 옵션

#### NSEDFLUME = 1 (Sedflume-derived log-linear interpolation)

`s_sedzlj.f90:530-536` (active layer):

```fortran
! *** TAU 와 D50 의 4-point log-linear interpolation
SN00 = (TAUDD(2)-TAU(L))/(TAUDD(2)-TAUDD(1))
SN10 = (TAUDD(1)-TAU(L))/(TAUDD(1)-TAUDD(2))
SN01 = D50TMPP/NSCTOT
SN11 = (NSCTOT-D50TMPP)/NSCTOT
ERATEMOD = ( SN00*EXP(SN11*LOG(ERATEND(NSC0,NTAU0)) + SN01*LOG(ERATEND(NSC1,NTAU0))) &
            +SN10*EXP(SN11*LOG(ERATEND(NSC0,NTAU1)) + SN01*LOG(ERATEND(NSC1,NTAU1))) ) &
           * BULKDENS(K,L) * SQRT(1./SH_SCALE(L))
```

`ERATEND(NSC, NTAU)` = Sedflume 실험 erosion rate (cm/s) table — d50 class × TAU level.

#### NSEDFLUME = 98 (Power-law)

```fortran
! s_sedzlj.f90:539-543 (active layer)
SN00 = ACTDEPA(NSC0) * (0.1*TAU(L))**ACTDEPN(NSC0)         ! *** A * tau^N
SN10 = ACTDEPA(NSC1) * (0.1*TAU(L))**ACTDEPN(NSC1)
SN11 = D50TMPP/NSCTOT
ERATEMOD = ((SN10-SN00)*SN11 + SN00) * BULKDENS(K,L) * SQRT(1./SH_SCALE(L))
ERATEMOD = MIN(ERATEMOD, ACTDEPMAX(NSC0))                  ! *** Limit erosion rate
```

shear는 dynes/cm² 단위지만 power law는 **Pascal 단위** 전제 (0.1 변환). `SH_SCALE` = bed slope 보정 (§4).

### 2.7 Mass balance after erosion

```fortran
! s_sedzlj.f90:572-580 (standard branch)
WHERE( TAU(L) >= TCRE(1:NSEDS) )                       ! *** Size class별 critical shear 비교
  ELAY(1:NSEDS)  = PERSED(1:NSEDS,K,L) * EBD            ! *** Size-class erosion (g/cm²)
  ETOT(1:NSEDS)  = ETOT(1:NSEDS) + ELAY(1:NSEDS)
  TTEMP(1:NSEDS) = PERSED(1:NSEDS,K,L)*TSED(K,L) - ELAY(1:NSEDS)
ELSEWHERE
  ELAY  = 0.0
  TTEMP = PERSED * TSED
ENDWHERE
```

→ class 별 `TCRE` (resuspension) ≠ overall bed `TAUCRIT` (erosion onset). 작은 입자는 먼저 erode, 큰 입자는 lagging → armoring.

### 2.8 Layer reconstitution

`s_sedzlj.f90:300-342` — 시간 step 끝 active layer 재구성:
- Net deposition (`TSED(1) > TACT`) → 잉여 mass 를 layer 2 로 이송 (line 306-312)
- Net erosion, sufficient lower mass (`TSED(1) < TACT`, `TSED(1)+TSED(SLLN) > TACT`) → lower layer 에서 borrow (line 314-318)
- Net erosion, insufficient → layer 2 흡수 + SLLN advance (line 320-339)

### 2.9 Output → EFDC water column

```fortran
! s_sedzlj.f90:700-723
SEDF(L,0,1:NSEDS2) = QBFLUX(1:NSEDS2)*10000./DTSEDJ                  ! *** Suspended sed flux (g/m²/s)
SED(L,KSZ(L),NS)   = SED2(L,KSZ(L),NS) + (SEDF(L,0,NS) - SEDF(L,KSZ(L),NS)) * WDTDZ
HBED(L,1:KB)       = 0.01 * TSED(1:KB,L) / BULKDENS(1:KB,L)          ! *** Bed thickness (m)
SEDBT(L,1:KB)      = TSED(1:KB,L) * 10000.                           ! *** Bed mass (g/m²)
```

## 3. Wave-current shear (`s_shear.f90`) — Christoffersen-Jonsson 1985

`s_main.f90:54` 가 호출. 핵심:

### 3.1 Wave forcing 입력 옵션

`ISWNWAVE`:
- 0 = EFDC+ internal windwave (line 55-72)
- 1 = wind-fetch wave (CERC/SPM 식, line 74-185) — FZONE 8 sector + AVGDEPTH-based wave height/period
- 2 = STWAVE external wave (line 187-220)

### 3.2 Current friction (Parker 2004)

```fortran
! s_shear.f90:261
FC = (0.42 / LOG(11.*HP(L) / (2.0*ZBTEMP(L))))**2
! *** ZBTEMP = D50AVG × 10⁻⁶ m (skin friction) 또는 ZBSKIN
```

VonKarman κ=0.42 (line 261). 11 = 30/e (Schlichting). Current-only shear:

```fortran
SHEAR = FC * VELMAG²   ! *** dynes/cm² (VELMAG in cm/s)
```

### 3.3 Combined wave-current (Christoffersen-Jonsson 1985)

```fortran
! s_shear.f90:285-302
FWW    = 2.0*(0.0747 * (KN*WVFREQ(L)/WVORBIT(L)))**0.66        ! *** Pure wave friction (Beta = 0.0747)
SIGMAWV = FC/FWW * (VELMAG/(WVORBIT*100))**2                   ! *** Eq 3.8
MMW    = SQRT(1 + SIGMAWV² + 2*SIGMAWV*|cos(VELANG-WVANG)|)    ! *** Eq 3.10 wave-current angle adjustment
JJW    = WVORBIT/(KN*WVFREQ) * SQRT(MMW*FWW/2)                 ! *** Eq 4.12
FWW    = MMW*0.15/JJW                                          ! *** Updated combined friction (Step 3 end)

! *** Wave boundary layer
DELW    = KN * 0.273 * SQRT(JJW)                               ! *** Eq 4.11 thickness (m)
APROUGH = KN * DELW/KN * EXP(-5.62*DELW/KN * SQRT(SIGMAWV/MMW)) ! *** Eq 4.23 apparent roughness

! *** Current friction iterated with apparent roughness
FC = 2.0*(1.0/(2.38*LOG(H/(2.718*KN)) - 2.38*LOG(APROUGH/KN)))**2  ! *** Eq 4.25
! *** Iterate SIGMAWV, MMW, JJW, FWW once more
```

식 번호는 Christoffersen & Jonsson 1985 "An assessment of the wave-current sediment-transport theory" (Coastal Engineering) 원논문 인용. β=0.0747 (line 285 끝) 은 동 논문 추정.

### 3.4 Final combined shear

```fortran
! s_shear.f90:305-310
SHEARW   = 0.5 * FWW * MMW * WVORBIT²            ! *** Wave-only shear (m²/s²)
SHEARW   = 10000. * SHEARW                       ! *** Convert to cm²/s² = dynes/cm²·1/ρ
QQWV3(L) = SHEARW                                ! *** Wave shear output
QQWCR(L) = SHEARC                                ! *** Current shear output
SHEAR    = SHEARC + SHEARW                       ! *** Total
```

### 3.5 Growth limiter

```fortran
! s_shear.f90:315-322
! *** Limit rate of shear growth to 10% per timestep (suppress instability)
if( SHEAR > TAU(L)*(1.+GROWTH) )then              ! *** GROWTH = 0.1
  TAU(L) = TAU(L) + GROWTH*(SHEAR-TAU(L))
else
  TAU(L) = SHEAR
endif
```

### 3.6 Constant TAU 옵션

```fortran
! s_shear.f90:329-334
else
  ! *** TAUCONST > 0 → spatial constant
  TAU(L)  = TAUCONST
  TAUB(L) = 0.1 * TAU(L)
endif
```

## 4. Bed slope shear amplification (`s_slope.f90`) — Lick 2009

`s_main.f90:56` `if(ISSLOPE) call SEDZLJ_SLOPE`.

```fortran
! s_slope.f90:79-89
DZBETA  = DELX/XDIST*DELZX + DELY/YDIST*DELZY    ! *** Pitch (flow direction slope)
DZTHETA = DELY/XDIST*DELZX + DELX/YDIST*DELZY    ! *** Roll (cross-flow slope)
COSB = 1.0/SQRT(1+DZBETA²)
SINB = DZBETA/SQRT(1+DZBETA²)
COST = 1.0/SQRT(1+DZTHETA²)
TANT = DZTHETA
TEMP1 = (1.0+(FCO+FB)/(FG*COSB*COST))² - (TANT/TAN(ALPHA))²

if( TEMP1 > 0.0 )then
  SH_SCALE(L) = MAX(0.1, BB/AA*SINB + COSB*COST*SQRT(TEMP1))   ! *** Lick 2009 Eq 3.36
else
  SH_SCALE(L) = 0.1
endif
```

`SH_SCALE` ≥ 1 → adverse slope (uphill flow) 가 effective shear 증폭. `SEDZLJ` line 499, 517, 542 의 `SQRT(1/SH_SCALE)` 가 ERATEMOD 보정.

### 4.1 Lesser et al. bedload velocity correction

```fortran
! s_slope.f90:95-98
ALPHA_PX(L) = 1.0 - TUNEP*(TAN(ALPHA)/(COS(ATAN(DELZX/XDIST))*(TAN(ALPHA)-DELZX/XDIST))-1)  ! *** Pitch x
ALPHA_RX(L,NS) = -TUNER*SQRT(TCRE(NS)/TAU(L)) * DELZY/YDIST                                  ! *** Roll x
! (PY, RY 동일 패턴)
```

Lesser et al. (Delft3D) 추정 — gravity 가 bedload velocity vector를 downslope 으로 회전.

## 5. Bedload transport (`s_bedload.f90`) — Van Rijn 1981

`s_main.f90:59` `if(ICALC_BL > 0) call BEDLOADJ`.

```fortran
! s_bedload.f90:147-150 (Van Rijn 1981 식 번호 코멘트 직접)
TRANS(L,NS) = MAX((TAU(L)-TCRE(NS))/TCRE(NS), 0.0)                          ! *** Eq 21
DZBL(L,NS)  = D50(NS)/10000.0 * 0.3 * DISTAR(NS)**0.7 * SQRT(TRANS(L,NS))   ! *** Eq 20b - bedload layer thickness
BLVEL(L,NS) = 1.5 * TRANS(L,NS)**0.6 &
            * SQRT(((SEDDENS/WATERDENS) - 1.0) * 980.0 * D50(NS)/10000.0)   ! *** Eq 20a - bedload velocity (cm/s)
```

- `TRANS` = transport parameter (excess shear ratio)
- `DZBL` = bedload layer thickness (m)
- `BLVEL` = bedload velocity (cm/s)
- `DISTAR` = $D_*$ = dimensionless particle diameter $= D_{50} \cdot (g(s-1)/\nu^2)^{1/3}$

## 6. 입력 파라미터

### 6.1 Card C36 (SEDZLJ dispatch)

`models/EFDC/raw/manuals/confluence/spaces/ECIG/.../Card_Image_36.md`:

```
C36 | ISEDINT | ISEDBINT | NSEDFLUME | ISMUD | ISNDWC | ISEDVW | ISNDVW | KB | ISDTXBUG
    | 2       | 1        | 0         | 0     | 0      | 0      | 0      | 8  | 0
```

| 변수 | 의미 | 코드 위치 |
|---|---|---|
| `NSEDFLUME` | 0 = EFDC main / **98 = SEDZLJ** / 99 = SEDZLJ + toxics | `s_main.f90:64` |
| `KB` | 최대 bed layer 수 (active + in-place) | `s_sedzlj.f90:215, 282` |
| `ISEDINT` | 0 = constant / 1 = SEDW.INP+SNDW.INP / 2 = SEDB.INP+SNDB.INP / 3 = 둘 다 | `s_sedic.f90` |
| `ISEDBINT` | 0 = mass/area / 1 = mass fraction + BEDLAY.INP | `s_sedic.f90` |
| `ISEDVW` | cohesive settling velocity option (0 constant, 98 Lick flocculation, 99 Lick+floc advection) | `csedvis.f90` |

### 6.2 핵심 array 변수 (`mod_var_global.f90`)

| Symbol | 단위 | 의미 |
|---|---|---|
| `TSED(K,L)` | g/cm² | Layer K, cell L 의 단위면적 sediment mass |
| `PERSED(NS,K,L)` | — | Size class NS 의 mass 분율 (sum = 1) |
| `LAYERACTIVE(K,L)` | flag | 0/1/2 (부재/active deposited/in-place) |
| `BULKDENS(K,L)` | g/cm³ | 건조밀도 |
| `TAUCOR(K,L)` | dynes/cm² | Layer-specific critical shear |
| `TCRE(NS)` | dynes/cm² | Size-class critical shear (resuspension onset) |
| `TCRSUS(NS)` | dynes/cm² | Suspension critical shear (deposition threshold) |
| `TAU(L)` | dynes/cm² | Total bed shear (s_shear 출력) |
| `SH_SCALE(L)` | — | Bed slope shear scale (s_slope) |
| `D50AVG(L)` | μm | Cell L 의 bed 평균 D50 |
| `HBED(L,K)` | m | Bed layer 두께 |

## 7. SedTran-Original 와의 비교

[[efdc_sediment]] §C-D 의 원형 SedTran 와 SEDZLJ 의 핵심 차이:

| 항목 | SedTran-Original | SEDZLJ |
|---|---|---|
| Cohesive erosion | Krone-Partheniades (constant M) | Sedflume-derived ERATEND table 또는 power law |
| Cohesive deposition | Krone (PROB = 1 - τ/τc) | Krone (작은 D50) + Gessler (큰 D50) |
| Non-cohesive | Van Rijn / Engelund-Hansen (calsnd.f90) | 통합 Van Rijn (s_bedload.f90) |
| Bed structure | 단일 또는 단순 다층 | Active layer + multi in-place layer (`LAYERACTIVE` 0/1/2) |
| Wave-current shear | EFDC main (calwave2 등) | Christoffersen-Jonsson 1985 (s_shear.f90) |
| Bed slope | 없음 | Lick 2009 (s_slope.f90) `SH_SCALE` |
| Mass-class 정밀도 | water-column class만 | Bed mass-class + propwash fast/slow split |
| Toxic linkage | 별도 | NSEDFLUME=99 통합 |

## 8. Wave coupling

### 8.1 Wave parameter 입력 옵션 (`s_shear.f90`)

| `ISWAVE` × `ISWNWAVE` | 거동 | Code line |
|---|---|---|
| 0 | wave 없음 (current shear만) | 264 |
| > 0 × 0 | EFDC+ WINDWAVECAL 호출 (UDEL, FREQ, DIR) | 55-72 |
| > 0 × 1 | Wind-fetch wave (FZONE 8 sector + AVGDEPTH) | 74-185 |
| > 0 × 2 | STWAVE external NetCDF | 187-220 |

### 8.2 Wave breaking dispersion 별개

수평 운동량 확산의 wave breaking 가산항은 본 노트 아닌 [[efdc_dispersion]] §2.3 calhdmf.f90:246-294.

## 9. Cross-references

- **Dispatch / SedTran 비교**: [[efdc_sediment]] §A (ISTRAN(6)/(7), SEDZLJ enable)
- **수평 momentum diffusion**: [[efdc_dispersion]] (Smagorinsky + AHO, 별개 layer)
- **Vertical turbulence**: [[efdc_turbulence]] (Mellor-Yamada / Galperin / GOTM)
- **Theory 식**: [[efdc-theory-doc-v12]] §6.4 SEDZLJ (TOC line 136)
- **2003 legacy**: [[efdc-sediment-theory-2003]] §5 bed armoring (DSI SEDZLJ 에 흡수, line 169)
- **Card C36**: `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md`
- **EE12 GUI tutorial**: `models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Sediment_Transport_Modeling.md` + Yen & Lee U-Shaped Flume SEDZLJ tutorial

## 10. 미해결 / 추가 보강 후보

- ~~`s_sedic.f90` (769 lines) — bed initial-condition reader.~~ **§11 verified line 1-380 (2026-06-01 §11.1-5 + 2026-06-02 §11.6-8 deep: VAR_BED NCORENO core map + Sedflume core read + core→cell 매핑 + 층질량/LAYERACTIVE 초기화). 잔여: line 380-769 (HBED·HBED1 IC + bedload IC + morph 후처리) 별도.**
- `s_tecplot.f90` (310 lines) — SEDZLJ Tecplot 출력 — 분석 측면에서 별도 노트 필요 시.
- Propwash 연동 (`Variables_Propwash` use, line 27) — `s_sedzlj.f90:135-180, 559-617` 의 `PROP_ERO(L,1:NSEDS)` 처리. [[efdc-propwash]] (별도 노트) 후보.
- Mass erosion fast class (`NSEDS2 > NSEDS`, `s_sedzlj.f90:165-180, 604-617`) — propwash 시 fast/normal 분리 동작.
- Toxics linkage (`NSEDFLUME = 99`) — **deprecated 2016-12 ([[efdc_sedzlj]] §11.4)**. 매뉴얼 Card C36 의 NSEDFLUME=99 표기는 stale → ISTRAN(5)>0 가 현행.
- Wave-current 식 번호와 Christoffersen-Jonsson 1985 원논문 페이지 cross-check (현재는 코드 코멘트 기준 인용).

## 11. SEDIC initialization (`s_sedic.f90`, 769 lines, line 1-380 verified — §11.1-5 2026-06-01, §11.6-8 deep 2026-06-02)

SEDZLJ bed 초기화: 입력 read(bed.sdf/erate.sdf) → VAR_BED core map(NCORENO) → Sedflume core data → core→cell 매핑 → 층질량/LAYERACTIVE 초기화.

### 11.1 Subroutine 호출 + 입력 파일 (line 53-58, master process)

```fortran
open(UNIT = 10, FILE = 'erate.sdf')   ! line 57 - Sedflume erosion rate table + TACTM
open(UNIT = 30, FILE = 'bed.sdf')     ! line 58 - bed parameters + size class
```

### 11.2 bed.sdf 입력 (line 63-96)

```fortran
read(30,*) VAR_BED, KB, ICALC_BL, SEDSTEP, SEDSTART, IHTSTRT, IMORPH, ISWNWAVE, MAXDEPLIMIT, HPMIN
if( HPMIN < 0.003 .or. HPMIN >= 1.0 ) HPMIN = 0.25                  ! line 65 fallback
if( SEDSTEP < TIDALP/REAL(NTSPTC) ) SEDSTEP = TIDALP/REAL(NTSPTC)    ! line 67

read(30,*) ZBSKIN, TAUCONST, ISSLOPE, BEDLOAD_CUTOFF                 ! line 80
read(30,*) (D50(K), K=1,NSEDS)                                       ! line 84 - 중앙 입경
read(30,*) (TCRE(K), K=1,NSEDS)                                      ! line 88 - 침식 임계
read(30,*) (TCRSUS(K), K=1,NSEDS)                                    ! line 92 - 부유 임계
read(30,*) (DWSIN(K), K=1,NSEDS)                                     ! line 96 - 침강속도 입력
```

매핑:
- `VAR_BED` = 1 → spatially varying bed
- `KB` = max bed layer (Card C36 일치)
- `HPMIN` = SEDZLJ 활성 최소 수심 (m), [0.003, 1.0] 외 시 0.25 fallback
- `ZBSKIN` = bed skin friction roughness ([[efdc_sedzlj]] §3.2 s_shear:243)
- `TAUCONST` > 0 → spatial constant shear ([[efdc_sedzlj]] §3.6)
- `ISSLOPE` = bed slope correction 활성 ([[efdc_sedzlj]] §4)
- `BEDLOAD_CUTOFF` = D50 임계 (Krone vs Gessler dispatch, [[efdc_sedzlj]] §2.1)

### 11.3 erate.sdf (line 112-113)

```fortran
read(10,*) TACTM   ! active layer thickness multiplier — [[efdc_sedzlj]] §2.4 핵심 식 입력
```

### 11.4 NSEDFLUME = 99 deprecated note (line 47-50, 정확 인용)

> "2016-12 — Rearranged SEDZLJ initialization and added parameters for better toxics simulations. **Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics) Toxics are handled by ISTRAN(5)>0. NEQUIL no longer used**. Paul M. Craig"

→ §6.1 Card C36 매뉴얼 (2018-01-08) 의 "NSEDFLUME = 99" 표기는 **stale** — 현행 ISTRAN(5)>0.

### 11.5 MPI broadcast (line 117-)

Master only read, 그 후 `Broadcast_Scalar/Array` 분배. `mod_var_global.f90` SEDZLJ 변수 전체.

### 11.6 VAR_BED core map (line 142-210) — deep 2026-06-02

`VAR_BED >= 1` (spatially variable bed) → **NCORENO(I,J) core 번호 맵** 읽기 (unit 20):
- **DSI standard**: `I2D_Global(I,J) = CORE` (cell별 core 번호)
- **SNL standard**: `read(20,'(120(I1,1X))')(I2D_Global(I,J), I=1,IC)` (J행별 1-digit core)
- local domain 매핑(MPI). VAR_BED=0 시 단일 core 전역.

### 11.7 Sedflume core data read (line 255-302) — deep

각 core (unit 10, NCORENO 가 참조):
- `TSED0S(K,CORE)` 층두께 + `BDEN(CORE,K)` bulk density + `WATERDENS, SEDDENS(CORE)` (물·sediment solid 밀도) + `PNEW(CORE,K,NS)` 층별 size fraction(%)
- **erosion data (NSEDFLUME 분기)**:
  - **NSEDFLUME==1** (Sedflume 측정): `TAULOC(M)` shear 카테고리(ITBM개) + `ERATETEMP(CORE,K,M)` 층·shear별 침식률
  - **NSEDFLUME==2** (power-law): `TAULOC=[0, 1000]` + `EA(CORE,K), EN(CORE,K), MAXRATE(CORE,K)` (A·τ^N, [[efdc_sedzlj]] §2.2). `MAXRATE` cm/s → g/m²/s `×BDEN` (dry bulk density)

### 11.8 core→cell 매핑 + 초기화 (line 306-380) — deep

`NCORENO(I,J)>0` 인 cell L 에 core 값 할당:
- `TAUCOR(K,L) = TAUTEMP(CORE,K)` (층별 critical shear) + `ERATE(K,L,M) = ERATETEMP` (NSEDFLUME=1)
- `PERSED(NS,K,L) = PNEW/100` (mass fraction, `/DTOTAL` 정규화 mass balance)
- **porosity·bulk density**: dry density 입력 시 `PORBED = 1 - BDEN/SEDDENS`, `BULKDENS = BDEN`; wet 시 별식. BULKDENS≤0 → STOPP
- **Non-cohesive 비활성**: `SNDBT=0`, `ISTRAN(7)=0` (SEDZLJ 가 cohesive+noncohesive 내부 CALTRAN 처리)
- **초기 층질량** (NSEDFLUME≠3): `LAYERACTIVE = 2`(in-place, TSED0S>0) 또는 `0`; `TSED = TSED0 = TSED0S × BULKDENS` (g/cm²)
- **post-process**: `TSED0/BULKDENS < 1e-8` 또는 `K≤2`(active layer) → `HBED=TSED=TSED0=0`, `TAUCOR=1000` (무침식)
> §3 s_shear·§2 s_sedzlj 가 사용하는 bed state (TAUCOR/ERATE/PERSED/TSED/LAYERACTIVE/BULKDENS)를 모두 SEDIC 가 초기화.
