---
title: "EFDC+ 열/온도/결빙 모듈 source-analysis — mod_heat.f90 (CALHEAT·ICECOMP·EQUILIBRIUM_TEMPERATURE) + caltranice.f90"
topic: efdc-heat-temperature-source
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable(12.4, sha 3ed76b6) raw source 직접 read: EFDC/Transport/mod_heat.f90(1738줄) + caltranice.f90(261줄). Theory v12 Ch 5 식(5.1-5.33) ↔ Fortran 라인 매핑, file:line 인용. Ch5 이론노트 [[efdc-theory-v12-ch5-temperature-heat]] 의 소스 대응."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — mod_heat.f90/caltranice.f90 직접 read + Ch5 PDF 교차"
verification_date: 2026-07-04
related:
  - models/EFDC/manual-notes/efdc-theory-v12-ch5-temperature-heat.md
  - models/EFDC/source-analysis/efdc_transport_scheme.md
  - models/EFDC/source-analysis/efdc_turbulence.md
  - concepts/sst/04-code-and-tools.md
---

# EFDC+ 열/온도/결빙 모듈 source-analysis — `mod_heat.f90` + `caltranice.f90`

> 소스: [`EFDC/Transport/mod_heat.f90`](../raw/source_code/EFDCPlus_Stable/EFDC/Transport/mod_heat.f90) (1738줄, `MODULE HEAT_MODULE`) + [`caltranice.f90`](../raw/source_code/EFDCPlus_Stable/EFDC/Transport/caltranice.f90) (261줄). EFDC+ Stable = 12.4, sha `3ed76b6`.
> 이론 짝: [[efdc-theory-v12-ch5-temperature-heat]] (Ch 5 식 5.1-5.33). 본 노트는 **이론식↔Fortran 라인** 매핑 + 소스-only 세부(incident longwave·Ryan-Harleman evap·frazil 이류).

## 0. 모듈 구조

| 서브루틴 | 라인 | 역할 | 이론 |
|---|---|---|---|
| `CALHEAT` | 52-1093 | 수면·저면 열교환 main, `ISTOPT(2)` 분기 | §5.1-5.3 |
| `SHORT_WAVE_RADIATION` | 1505-1549 | 단파복사 계산 | §5.2 |
| `SET_LIGHT` | 1652- | ice/수관 solar 감쇠 분배 | §5.2.1-5.2.3 |
| `ICECOMP` | 1095-1503 | 결빙/융해, `ISICE` 0-4 | §5.4 |
| `EQUILIBRIUM_TEMPERATURE` | 1551-1603 | W2 평형온도 반복해 | §5.1.3 |
| `SURFACE_TERMS` | 1685-1726 | back radiation·evap·conduction (ice용) | §5.4.2 |
| `CALTRANICE` (별 파일) | — | frazil ice 이류 (ISICE=4) | §5.4.1 |

## 1. `CALHEAT` — 수면 열교환 `ISTOPT(2)` 분기 (:629-863)

이론 §5.1 "3 방법"에 **소스는 5 옵션** (0=무·4=external 추가):

```
ISTOPT(2)==0  : 무 heat transfer (:629, return)
ISTOPT(2)==1  : Full Heat Balance (:633)
ISTOPT(2)==2  : COARE 3.6        (:691)
ISTOPT(2)==3  : W2 Equilibrium Temperature (:775)
ISTOPT(2)==4  : External equilibrium (CLOUDT=표면교환계수) (:850)
```

### 1.1 Full Heat Balance (:641-689) — Eq 5.2-5.4

3 flux 하드코딩 (단위 = m·degC/s, εσ/(ρcp) 등 folded):

```fortran
HBLW = 1.312E-14*((TEM+273.)**4)*(0.39-0.05*SQRT(VPAT))*(1.-.8*CLOUDT) &
     + 5.248E-14*((TEM+273.)**3)*(TEM-TATMT)          ! :648-649  Eq 5.2 longwave back
HBCV = CCNHTT*0.288E-3*WINDST*(TEM-TATMT)             ! :650      Eq 5.4 sensible H_C
HBEV = CLEVAP*0.445*WINDST*(SVPW1-VPAT)/PATMT         ! :651      Eq 5.3 latent  H_E
```

- 계수비 `5.248E-14/1.312E-14 = 4.0` = Eq 5.2 의 $4\varepsilon\sigma$ vs $\varepsilon\sigma$ 정합.
- $H_E$ 의 `/PATMT` = Eq 5.3 의 $0.622/P_a$ 항 (0.445 = 0.622·ρa·Le/cp scaling).
- 온도 갱신 `TEM(L,KC) += HPI(L)*RADNET(L,KC)` (:663).

> ⚠ **이론↔소스 불일치 (cloud sign)**: 소스는 구름인자 `(1.-0.8*CLOUDT)` (:648, COARE 분기 :705 동일), 그러나 Theory Eq 5.2 는 `(1+B_cC)` (Bc=0.8) 로 인쇄. **소스 `(1-0.8C)` 가 물리적 표준** (구름↑ → 순 장파 냉각↓, Rosati-Miyakoda 1988 원형). Theory Eq 5.2 의 `(1+B_cC)` 는 부호 오식으로 판단 (`1-B_cC` 이어야). → [[efdc-theory-v12-ch5-temperature-heat]] §1.1 에 disclosed-gap 표기 필요.

### 1.2 COARE 3.6 (:691-773) — Eq 5.5-5.8

외부 서브루틴 `coare36flux_coolskin(...)` 호출 (:728-729) — 풍속·기온·습도·기압·수온·solar·longwave·파랑(vcp/sigH) 입력 → `tau_/hsb/hlb` (stress·sensible·latent) 출력. longwave 는 Full Heat 와 동일 HBLW (:705). 산출물: `CDCOARE`(drag), `ZSRE`(조도 z0 Eq 5.8), `EVACOARE`=hlb/Le/1000 (evap rate m/s :737). 파랑결합: `ISWAVE>=3` 시 파장/주기/파고 전달 (:719-725).

### 1.3 W2 Equilibrium Temperature (:775-848) — Eq 5.9

```fortran
TFLUX = CSHE*(ET - TEM(L,KC))/THICK*DELT      ! :825   H_n = -K_aw(T_s - T_e)
TEM(L,KC) = TEM(L,KC) + TFLUX                 ! :826
```

`CSHE` = $K_{aw}$ (Eq 5.9 표면교환계수), `ET` = $T_e$ 평형온도. `EQUILIBRIUM_TEMPERATURE` 서브루틴이 (셀별 or NASER>1 시) 재계산 (:790,803). PSHADE/WINDSTKA 불변 시 SWAP 캐시로 재계산 회피 (:805-821, OMP 최적화).

### 1.4 EQUILIBRIUM_TEMPERATURE 서브루틴 (:1551-1603) — Eq 5.10-5.12

English 단위 반복해 (Brady et al. 1969):

```fortran
BETA = 0.255-(8.5E-3*TSTAR)+(2.04E-4*TSTAR*TSTAR)   ! :1583  Eq 5.12 β_w
TSTAR= (ET+TDEW_F)*0.5                                ! :1582  T*=0.5(Te+Td)
FW   = W_M2_TO_BTU_FT2_DAY*AFW + BCONV*BFW*WIND_2M**CFW  ! :1584  풍속함수 f(W)
CSHE = 15.7+(0.26+BETA)*FW                           ! :1585  K_aw (Eq 5.11 형)
ETP  = (SRO_BR+RA-1801.0)/CSHE + (CSHE-15.7)*(0.26*TAIR_F+BETA*TDEW_F)/(CSHE*(0.26+BETA))  ! :1586
! ... do J 반복 (:1587-1594) → ET 수렴
ET   = (ET-32.0)*5.0/9.0                    ! :1601  °F→°C
CSHE = CSHE*FLUX_BR_TO_FLUX_SI*RHOWCPI      ! :1602  English flux→SI (m/s)
```

- 계수 15.7·0.26 = Brady/Edinger 대체표현 (Eq 5.11 제시형 23·0.255 와 다른 상수, 단위변환 상수 `MPS_TO_MPH=2.23714`·`W_M2_TO_BTU_FT2_DAY=7.60796` 등 :33-37).
- 매뉴얼 "iterative/approximate technique (Brady et al. 1969)" 의 **반복 실장 확인**.

## 2. 저면 열교환 (:909-1003) — Eq 5.18-5.20

```fortran
TFLUX = ( HTBED1*USPD + HTBED2 )*( TEMB - TEMP )*DELT   ! :926  Eq 5.18 H_b=-(K_bv U+K_bc)(T_w-T_b)
```

- `HTBED1` = $K_{b,v}$ (convective), `HTBED2` = $K_{b,c}$ (conductive), `USPD=√(UBED²+VBED²)` = Eq 5.19 $U$.
- bed 온도 갱신 `TEMBO>0` 시 (:947-1002), longwave bed emission `FLUXQB = 4.43E-14*((TEMB+273)^4-(TEMP+273)^4)` (:970) — **`4.43E-14 = σ/(ρb·cpb)`, ρb=1600 kg/m³·cpb=800 J/kg/C** (:968 주석).
- 마른 셀 bed 온도 = 전도손실+장파방출 (:994-1000, 반값 열전도).

## 3. `ICECOMP` — 결빙/융해 (:1095-1503) — Eq 5.21-5.30

`ISICE` 옵션 (:1100-1104): 0 무·1 사용자지정 시공변·2 binary on/off·**3 fully heat coupled**·**4 coupled+frazil transport**.

### 3.1 Freezing temperature (:1178-1188) — Eq 5.26

```fortran
if( SAL(L,KC) < 35. )then
  TF = -0.0545*SAL(L,KC)                                        ! Eq 5.26 상단 (TDS<35)
else
  TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)  ! Eq 5.26 하단 (TDS>35)
endif
TFS = TF - 0.01   ! *** 과냉각(supercooled) 상태 (:1188)
```

**Eq 5.26 완전 정합** (매뉴얼 반올림 -0.3146/-0.0417 = 소스 -0.31462/-0.04177). `ISTRAN(1)==0`(염분 미모의) 시 `TF=0`.

### 3.2 Incident longwave RANLW (:1322-1327) — **소스-only (매뉴얼 미기재)**

이론 §5.4.2 는 $H_{an}$ (입사 장파) 을 항으로만 나열, 소스는 2-분기 실장:

```fortran
if( TATMT >= 5.0 )then
  RANLW = 5.31E-13*(273.15+TATMT)**6*(1.0+0.17*CLOUDT**2)*0.97           ! Swinbank 형
else
  RANLW = 5.62E-8*(273.15+TATMT)**4*(1.-0.261*EXP(-7.77E-4*TATMT**2))*(1.0+0.17*CLOUDT**2)*0.97  ! Idso-Jackson 형
endif
RT = SOLSWRT*CREFLI + RANLW    ! :1330  총 입사 (단파+장파) = Eq 5.23/5.24 H_sn+H_an
```

### 3.3 Ice surface temperature 반복해 (:1332-1344) — Eq 5.23-5.25

```fortran
do ITERI = 1, ITERMAX
  call SURFACE_TERMS(ICETEMP,L,RB,RC,RE)             ! back/conduction/evap
  RN  = RT - RB - RE - RC                            ! :1336  순 표면 flux (W/m²)
  DEL = RN + ICEK*(TF-ICETEMP)/ICETHICK              ! :1337  Eq 5.25 q_i=K_i(T_f-T_s)/θ 결합
  ICETEMP = ICETEMP + capped(DEL*ICETHICK/10.)       ! :1338-1342 update
  if( ABS(update) < 0.01 ) EXIT
enddo
```

`ICEK` = $K_i$ 얼음 열전도도. Eq 5.24 ($T_s=0$ 시 잔여 flux=결빙 latent) 의 반복 근사.

### 3.4 Ice melt/growth (:1375-1432) — Eq 5.27-5.29

- **Air/ice melt** (ICETEMP>0, :1375-1382): `DICETHI = -CP*ICETEMP*ICETHICK*MELTFACTOR/LHF*...` = Eq 5.27.
- **Bottom growth** (ICETEMP≤0, :1385-1399): `HICE = ICEK*(TF-TICEBOT)/ICETHICK`, `DICETHI = DELTICE*HICE*RHOILHFI` = Eq 5.28-5.29.
- **Water-ice interface** (:1405-1429): melt `HICE=-HWI*TEM*RHOILHFI` (TEM>0) / freeze `WTEMP*CP*THICKMIN*999.8426` (TEM<TFS) → TEM=TF.
- 총 두께 갱신 `ICETHICK += DICETHI + DICETHW` (:1432). `>=MINICE` 시 `ICECELL=.TRUE.` (:1434).

### 3.5 SURFACE_TERMS (:1685-1726) — ice 표면 3 flux

```fortran
VPA = EXP(2.3026*(7.5*TDEWT/(TDEWT+237.3)+0.6609))   ! :1697  대기 증기압(mmHg, Magnus)
VPS = ... (TSUR<0: 얼음 위 9.5/265.5, else 7.5/237.3) ! :1700-1704  포화증기압
FW  = 3.59*DTV**0.3333+4.26*WINDST  (ISRHEVAP=1)      ! :1712  Ryan-Harleman 1974 풍속함수
RE  = FW*(VPS-VPA)                                    ! :1718  evaporative (H_e)
RC  = FW*0.47*(TSUR-TATMT)                            ! :1721  conduction (Bowen 0.47, H_c)
RB  = 5.51E-8*(TSUR+273.15)**4                        ! :1724  back radiation (εσ, H_br)
```

## 4. `caltranice.f90` — frazil ice 이류 (ISICE=4)

`CALTRANICE(CON, CON1, IT)` (:9) — frazil ice(또는 ice-impacted 물질)의 **이류 전송** (2015-01 Paul Craig 추가). CALTRAN 계열(→ [[efdc_transport_scheme]])의 ice 특화 버전 — donor-cell/upwind advection, 단 frazil 경계부하는 skip (:57). ISICE=4 에서 `FRAZILICE(L,KC)` 를 유체와 함께 이송 (mod_heat ICECOMP :1197 에서 생성된 frazil 을 다음 스텝 이류).

## 5. 소스↔이론 매핑 요약

| 이론 Eq | 소스 위치 | 비고 |
|---|---|---|
| 5.2 longwave $H_L$ | mod_heat:648-649 | ⚠ cloud sign (1-0.8C) ≠ 매뉴얼 (1+BcC) |
| 5.3 latent $H_E$ | :651 (`/PATMT` = 0.622/Pa) | |
| 5.4 sensible $H_C$ | :650 | |
| 5.5-5.8 COARE | :728 `coare36flux_coolskin` | z0 Charnock=ZSRE |
| 5.9 equilibrium $H_n$ | :825 `CSHE*(ET-TEM)` | |
| 5.10-5.12 $T_e$ | :1551 반복해 J-loop | Brady 1969, English 단위 |
| 5.18-5.20 bed heat | :926 `HTBED1*USPD+HTBED2` | bed LW 4.43E-14=σ/ρb/cpb |
| 5.21-5.22 ice 초기 | ICECOMP :1190 frazil (efdc_sedzlj 아님) | |
| 5.23-5.25 ice surf T | :1332-1344 반복 + SURFACE_TERMS | |
| 5.26 freezing $T_f$ | :1181 `TF=-0.0545*SAL` | 완전 정합 |
| 5.27-5.29 melt/growth | :1378·:1389-1390·:1409 | |
| (매뉴얼無) incident LW | :1322-1327 Swinbank/Idso 2-분기 | 소스-only |
| (매뉴얼無) Ryan-Harleman evap | :1712 | 소스-only |

## 6. 관련

- [[efdc-theory-v12-ch5-temperature-heat]] — Ch 5 이론 (본 노트의 짝, cloud-sign disclosed-gap 대상)
- [[efdc_transport_scheme]] — CALTRAN/CALTRAN_AD (온도 scalar 이류, caltranice 의 모체)
- [[efdc_turbulence]] — 연직 eddy diffusivity $A_b$ (Eq 5.1 열확산 제공)
- `concepts/sst/04-code-and-tools.md` — 해수면온도 도메인 (COARE cross-model: [[roms_bulk_flux_coare]])
