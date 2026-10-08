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
last_source_check: 2026-10-08 (recovery 재판독 대조)
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

- 두 복사 계수의 비 4는 일치한다. (`Transport/mod_heat.f90:646` — `HBLW = 1.312E-14*((TEM(L,KC)+273.)**4)*(0.39-0.05*SQRT(VPAT(L)))*(1.-.8*CLOUDT(L)) + &`; `Transport/mod_heat.f90:647` — `5.248E-14*((TEM(L,KC)+273.)**3)*(TEM(L,KC)-TATMT(L))`; EFDC_Theory_Document_Ver_12.pdf, PDF 73쪽·인쇄 60쪽) 구름 인자의 부호는 일치하지 않는다. (`Transport/mod_heat.f90:646` — `HBLW = 1.312E-14*((TEM(L,KC)+273.)**4)*(0.39-0.05*SQRT(VPAT(L)))*(1.-.8*CLOUDT(L)) + &`; EFDC_Theory_Document_Ver_12.pdf, PDF 73쪽·인쇄 60쪽) 문서는 1+0.8C이고 코드는 1−0.8C이다. (`Transport/mod_heat.f90:646` — `HBLW = 1.312E-14*((TEM(L,KC)+273.)**4)*(0.39-0.05*SQRT(VPAT(L)))*(1.-.8*CLOUDT(L)) + &`; EFDC_Theory_Document_Ver_12.pdf, PDF 73쪽·인쇄 60쪽) Kelvin 변환 상수도 273.15와 273으로 다르다. (`Transport/mod_heat.f90:646` — `HBLW = 1.312E-14*((TEM(L,KC)+273.)**4)*(0.39-0.05*SQRT(VPAT(L)))*(1.-.8*CLOUDT(L)) + &`; `Transport/mod_heat.f90:647` — `5.248E-14*((TEM(L,KC)+273.)**3)*(TEM(L,KC)-TATMT(L))`; EFDC_Theory_Document_Ver_12.pdf, PDF 73쪽·인쇄 60쪽) 해석: 계수비의 일치만으로 장파 식 전체의 정합을 확인할 수 없다(정적 판독, 실행 미확인). (`Transport/mod_heat.f90:646` — `HBLW = 1.312E-14*((TEM(L,KC)+273.)**4)*(0.39-0.05*SQRT(VPAT(L)))*(1.-.8*CLOUDT(L)) + &`; `Transport/mod_heat.f90:647` — `5.248E-14*((TEM(L,KC)+273.)**3)*(TEM(L,KC)-TATMT(L))`; EFDC_Theory_Document_Ver_12.pdf, PDF 73쪽·인쇄 60쪽)
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

- 반복 구현은 확인했다. (`Transport/mod_heat.f90:1589` — `BETA  = 0.255-(8.5E-3*TSTAR)+(2.04E-4*TSTAR*TSTAR)`; `Transport/mod_heat.f90:1591` — `ETP   = (SRO_BR+RA-1801.0)/CSHE+(CSHE-15.7)*(0.26*TAIR_F+BETA*TDEW_F)/(CSHE*(0.26+BETA))`; `Transport/mod_heat.f90:1592` — `J     = J+1`; EFDC_Theory_Document_Ver_12.pdf, PDF 75쪽·인쇄 62쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 76쪽·인쇄 63쪽) 문서 식 5.10·5.11의 23·0.255·0.225와 코드의 15.7·0.26은 다르다. (`Transport/mod_heat.f90:1582` — `CSHE  = 15.7+(0.26+BETA)*FW`; `Transport/mod_heat.f90:1584` — `ETP   = (SRO_BR+RA-1801.0)/CSHE+(CSHE-15.7)*(0.26*TAIR_F+BETA*TDEW_F)/(CSHE*(0.26+BETA))`; EFDC_Theory_Document_Ver_12.pdf, PDF 75쪽·인쇄 62쪽, 식 5.10; EFDC_Theory_Document_Ver_12.pdf, PDF 75쪽·인쇄 62쪽, 식 5.11) 코드는 기온 장파항 RA와 1801을 포함한다. (`Transport/mod_heat.f90:1583` — `RA    = 3.1872E-08*(TAIR_F+459.67)**4`; `Transport/mod_heat.f90:1584` — `ETP   = (SRO_BR+RA-1801.0)/CSHE+(CSHE-15.7)*(0.26*TAIR_F+BETA*TDEW_F)/(CSHE*(0.26+BETA))`; EFDC_Theory_Document_Ver_12.pdf, PDF 75쪽·인쇄 62쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 76쪽·인쇄 63쪽) 식 5.12의 이차항은 음수이고 코드는 양수이다. (`Transport/mod_heat.f90:1589` — `BETA  = 0.255-(8.5E-3*TSTAR)+(2.04E-4*TSTAR*TSTAR)`; EFDC_Theory_Document_Ver_12.pdf, PDF 76쪽·인쇄 63쪽, 식 5.12) 코드는 평형온도와 이슬점의 평균을 쓴다. (`Transport/mod_heat.f90:1588` — `TSTAR = (ET+TDEW_F)*0.5`; EFDC_Theory_Document_Ver_12.pdf, PDF 75쪽·인쇄 62쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 76쪽·인쇄 63쪽) 해석: 단위 변환 상수만으로 두 식의 동등성을 확인할 수 없다(정적 판독, 실행 미확인). (`Transport/mod_heat.f90:1582` — `CSHE  = 15.7+(0.26+BETA)*FW`; `Transport/mod_heat.f90:1584` — `ETP   = (SRO_BR+RA-1801.0)/CSHE+(CSHE-15.7)*(0.26*TAIR_F+BETA*TDEW_F)/(CSHE*(0.26+BETA))`; `Transport/mod_heat.f90:1589` — `BETA  = 0.255-(8.5E-3*TSTAR)+(2.04E-4*TSTAR*TSTAR)`; EFDC_Theory_Document_Ver_12.pdf, PDF 75쪽·인쇄 62쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 76쪽·인쇄 63쪽)
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

문서의 입력은 TDS이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) 코드의 입력은 SAL이다. (`Transport/mod_heat.f90:1178` — `if( SAL(L,KC) < 35. )then`; `Transport/mod_heat.f90:1181` — `TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) TDS와 SAL을 같은 값으로 놓아야 식을 비교할 수 있다. (`Transport/mod_heat.f90:1178` — `if( SAL(L,KC) < 35. )then`; `Transport/mod_heat.f90:1181` — `TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) 고염분 계수 −0.0417과 −0.04177은 숫자가 다르다. (`Transport/mod_heat.f90:1181` — `TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) −0.3146과 −0.31462도 숫자가 다르다. (`Transport/mod_heat.f90:1181` — `TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) SAL=35는 코드의 둘째 분기이다. (`Transport/mod_heat.f90:1178` — `if( SAL(L,KC) < 35. )then`; `Transport/mod_heat.f90:1180` — `else`; `Transport/mod_heat.f90:1181` — `TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) 문서는 등호 조건을 비워 두었다. (EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽)

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
| 5.5-5.8 COARE | 코드·문서 대조 | COARE 호출과 Charnock+매끈한 조도 구조는 대응한다. (`Transport/coare36.f90:393` — `zo = charn*usr*usr/grav + 0.11*visa/usr !% surface roughness`; `Transport/coare36.f90:527` — `zo10  = 0.011*usr*usr/grav + 0.11*visa/(usr+1.e-12)`; EFDC_Theory_Document_Ver_12.pdf, PDF 74쪽·인쇄 61쪽) 코드 visa는 공기 동점성이다. (`Transport/coare36.f90:393` — `zo = charn*usr*usr/grav + 0.11*visa/usr !% surface roughness`; EFDC_Theory_Document_Ver_12.pdf, PDF 74쪽·인쇄 61쪽) 문서의 물 동점성 설명과 다르다. (`Transport/coare36.f90:393` — `zo = charn*usr*usr/grav + 0.11*visa/usr !% surface roughness`; EFDC_Theory_Document_Ver_12.pdf, PDF 74쪽·인쇄 61쪽) 최종 조도의 Charnock 계수 선택을 고정 0.011로 일반화하지 않는다. (`Transport/coare36.f90:393` — `zo = charn*usr*usr/grav + 0.11*visa/usr !% surface roughness`; `Transport/coare36.f90:527` — `zo10  = 0.011*usr*usr/grav + 0.11*visa/(usr+1.e-12)`; EFDC_Theory_Document_Ver_12.pdf, PDF 74쪽·인쇄 61쪽) |
| 5.9 equilibrium $H_n$ | :825 `CSHE*(ET-TEM)` | |
| 5.10-5.12 $T_e$ | :1551 반복해 J-loop | Brady 1969, English 단위 |
| 5.18-5.20 bed heat | :926 `HTBED1*USPD+HTBED2` | bed LW 4.43E-14=σ/ρb/cpb |
| 5.21-5.22 ice 초기 | ICECOMP :1190 frazil (efdc_sedzlj 아님) | |
| 5.23-5.25 ice surf T | 코드·문서 대조 | 선형 공기–얼음 식 5.21은 별도 구현식으로 찾지 못했다. (`Transport/mod_heat.f90:1334` — `RN = RT-RB-RE-RC                                    ! *** W/M2`; `Transport/mod_heat.f90:1335` — `DEL = RN + ICEK*(TF-ICETEMP(L))/ICETHICK(L)         ! *** W/M2`; `Transport/mod_heat.f90:1333` — `call SURFACE_TERMS (ICETEMP(L),L,RB,RC,RE)          ! *** OUT: RB,RC,RE`; EFDC_Theory_Document_Ver_12.pdf, PDF 80쪽·인쇄 67쪽, 식 5.21) 코드 빙면 잔차에는 증발 손실 RE를 포함한다. (`Transport/mod_heat.f90:1334` — `RN = RT-RB-RE-RC                                    ! *** W/M2`; EFDC_Theory_Document_Ver_12.pdf, PDF 80쪽·인쇄 67쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 82쪽·인쇄 69쪽) 문서 식 5.23은 이를 빠뜨린다. (`Transport/mod_heat.f90:1334` — `RN = RT-RB-RE-RC                                    ! *** W/M2`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽, 식 5.23) |
| 5.26 freezing $T_f$ | 코드·문서 대조 | 문서의 입력은 TDS이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) 코드의 입력은 SAL이다. (`Transport/mod_heat.f90:1178` — `if( SAL(L,KC) < 35. )then`; `Transport/mod_heat.f90:1181` — `TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) TDS와 SAL을 같은 값으로 놓아야 식을 비교할 수 있다. (`Transport/mod_heat.f90:1178` — `if( SAL(L,KC) < 35. )then`; `Transport/mod_heat.f90:1181` — `TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) 고염분 계수 −0.0417과 −0.04177은 숫자가 다르다. (`Transport/mod_heat.f90:1181` — `TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) −0.3146과 −0.31462도 숫자가 다르다. (`Transport/mod_heat.f90:1181` — `TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) SAL=35는 코드의 둘째 분기이다. (`Transport/mod_heat.f90:1178` — `if( SAL(L,KC) < 35. )then`; `Transport/mod_heat.f90:1180` — `else`; `Transport/mod_heat.f90:1181` — `TF = -0.31462-0.04177*SAL(L,KC)-0.000166*SAL(L,KC)*SAL(L,KC)`; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) 문서는 등호 조건을 비워 두었다. (EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽) |
| 5.27-5.29 melt/growth | 코드·문서 대조 | 코드 융해는 CP=4179와 MELTFACTOR를 사용한다. (`Transport/mod_heat.f90:1376` — `DICETHI = -CP*ICETEMP(L)*ICETHICK(L)*MELTFACTOR/LHF*ICESTEP/DELTICE`; `Transport/mod_heat.f90:40` — `real, save, PRIVATE :: CP      = 4179.0                  ! *** SPECIFIC HEAT (J/KG/degC)    (Previously EFDC used 4179.0)   4184`; EFDC_Theory_Document_Ver_12.pdf, PDF 80쪽·인쇄 67쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 82쪽·인쇄 69쪽) 문서의 얼음 비열과 고정 1/2와 다르다. (`Transport/mod_heat.f90:1376` — `DICETHI = -CP*ICETEMP(L)*ICETHICK(L)*MELTFACTOR/LHF*ICESTEP/DELTICE`; `Transport/mod_heat.f90:40` — `real, save, PRIVATE :: CP      = 4179.0                  ! *** SPECIFIC HEAT (J/KG/degC)    (Previously EFDC used 4179.0)   4184`; EFDC_Theory_Document_Ver_12.pdf, PDF 80쪽·인쇄 67쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 82쪽·인쇄 69쪽) 수중 융해는 TEM>0에서 TEM을 사용한다. (`Transport/mod_heat.f90:1407` — `HICE   = -HWI*TEM(L,KC)*RHOILHFI`; `Transport/mod_heat.f90:1405` — `if( TEM(L,KC) > 0.0 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 80쪽·인쇄 67쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 82쪽·인쇄 69쪽) 문서는 Tw−Tf를 사용한다. (`Transport/mod_heat.f90:1407` — `HICE   = -HWI*TEM(L,KC)*RHOILHFI`; `Transport/mod_heat.f90:1405` — `if( TEM(L,KC) > 0.0 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 80쪽·인쇄 67쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 82쪽·인쇄 69쪽) 문서 식 5.29에는 시간 간격이 없다. (`Transport/mod_heat.f90:1388` — `DICETHI = DELTICE*HICE*RHOILHFI`; `Transport/mod_heat.f90:1408` — `DICETHW = DELTICE*HICE`; EFDC_Theory_Document_Ver_12.pdf, PDF 82쪽·인쇄 69쪽, 식 5.29) 코드는 DELTICE를 곱한다. (`Transport/mod_heat.f90:1388` — `DICETHI = DELTICE*HICE*RHOILHFI`; `Transport/mod_heat.f90:1408` — `DICETHW = DELTICE*HICE`; EFDC_Theory_Document_Ver_12.pdf, PDF 80쪽·인쇄 67쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 82쪽·인쇄 69쪽) 코드는 성장과 융해를 별도 조건에서 갱신한다. (`Transport/mod_heat.f90:1334` — `RN = RT-RB-RE-RC                                    ! *** W/M2`; `Transport/mod_heat.f90:1335` — `DEL = RN + ICEK*(TF-ICETEMP(L))/ICETHICK(L)         ! *** W/M2`; `Transport/mod_heat.f90:1387` — `HICE    = ICEK*(TF-TICEBOT)/ICETHICK(L)         ! *** W/M2`; `Transport/mod_heat.f90:1388` — `DICETHI = DELTICE*HICE*RHOILHFI`; `Transport/mod_heat.f90:1407` — `HICE   = -HWI*TEM(L,KC)*RHOILHFI`; `Transport/mod_heat.f90:1408` — `DICETHW = DELTICE*HICE`; `Transport/mod_heat.f90:1333` — `call SURFACE_TERMS (ICETEMP(L),L,RB,RC,RE)          ! *** OUT: RB,RC,RE`; `Transport/mod_heat.f90:1336` — `TMPVAL = DEL*ICETHICK(L)/10.`; `Transport/mod_heat.f90:1337` — `if( ABS(TMPVAL) > 1. )then`; `Transport/mod_heat.f90:1338` — `TMPVAL = SIGN(1.0,TMPVAL)`; `Transport/mod_heat.f90:1340` — `ICETEMP(L) = ICETEMP(L) + TMPVAL`; `Transport/mod_heat.f90:1341` — `if( ABS(TMPVAL) < 0.01 ) EXIT`; `Transport/mod_heat.f90:1375` — `ICETEMP(L) = min(ICETEMP(L),0.001/ICETHICK(L))`; `Transport/mod_heat.f90:1376` — `DICETHI = -CP*ICETEMP(L)*ICETHICK(L)*MELTFACTOR/LHF*ICESTEP/DELTICE`; `Transport/mod_heat.f90:40` — `real, save, PRIVATE :: CP      = 4179.0                  ! *** SPECIFIC HEAT (J/KG/degC)    (Previously EFDC used 4179.0)   4184`; `Transport/mod_heat.f90:1386` — `TICEBOT = min(ICETEMP(L) + TEM(L,KC),0.0)       ! *** ADJUST ICE TEMPERATURE FOR WATER CONTACT`; `Transport/mod_heat.f90:1405` — `if( TEM(L,KC) > 0.0 )then`; `Transport/mod_heat.f90:1406` — `! *** MELT`; EFDC_Theory_Document_Ver_12.pdf, PDF 80쪽·인쇄 67쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 81쪽·인쇄 68쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 82쪽·인쇄 69쪽) |
| (매뉴얼無) incident LW | :1322-1327 Swinbank/Idso 2-분기 | 소스-only |
| (매뉴얼無) Ryan-Harleman evap | :1712 | 소스-only |

## 6. 관련

- [[efdc-theory-v12-ch5-temperature-heat]] — Ch 5 이론 (본 노트의 짝, cloud-sign disclosed-gap 대상)
- [[efdc_transport_scheme]] — CALTRAN/CALTRAN_AD (온도 scalar 이류, caltranice 의 모체)
- [[efdc_turbulence]] — 연직 eddy diffusivity $A_b$ (Eq 5.1 열확산 제공)
- `concepts/sst/04-code-and-tools.md` — 해수면온도 도메인 (COARE cross-model: [[roms_bulk_flux_coare]])
