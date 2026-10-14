---
title: "ROMS 해석 함수 — ana_* analytical functionals (idealized forcing/IC/BC)"
model: ROMS
component: ROMS/Functionals
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Functionals/). analytical.F 디스패처 + ana_grid.h/ana_initial.h/ana_smflux.h/ana_btflux.h/ana_fsobc.h/ana_psource.h/ana_perturb.h 등 헤더·tile 본문 file:line 인용. CPP 가드·ANANAME 인덱스·idealized CASE 분기 확인. 2026-10-14 ROMS recovery 대조 보고서 반영"
last_source_check: "2026-10-14 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/README.md
---

# ROMS 해석 함수 — ana_* analytical functionals

> ROMS의 idealized test case·사용자 정의 forcing/IC/BC를 해석식으로 지정하는 `ana_*` 패키지이다.
> 현재 HEAD의 `ROMS/Functionals/`에서 `.h` 파일명을 센 수는 42개이다.
> 출처: [testcases:RT1-1514](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안), [build-options-history:RBH-3507](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안).

## 1. 패키지 구조와 디스패처

해석 함수의 디스패처는 `analytical_mod` 모듈이다 (`ROMS/Functionals/analytical.F:2`).
각 포함 헤더는 CPP 조건으로 선택한다 (`ROMS/Functionals/analytical.F:84, 258–263`).
`ana_vegetation.h`는 현재 `analytical.F`의 포함 목록에 없다.
출처: [build-options-history:RBH-3507](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안).

목적 요약은 `analytical.F:11-71` 헤더 주석에 카탈로그로 정리됨:
- `analytical.F:13-14`: "This package is used to provide various analytical fields to the model when appropriate."

전체가 **`#ifdef ANALYTICAL`** (`analytical.F:84`) 가드 아래 있고, 각 `.h` 는 추가 CPP 조건으로 인클루드된다 (예: `analytical.F:121-123` `ANA_GRID`, `analytical.F:133-135` `ANA_INITIAL`, `analytical.F:203-205` `ANA_SMFLUX`).

User 사설 응용용 템플릿이 별도 존재:
- `analytical.F:73-76`: "Notice that there is a template copy of each header file in the 'User/Functionals' directory ... distinguishing between official idealized problems and user interface."

### 호출/디스패치 구조 (3계층 tile 패턴)
각 `ana_*.h` 는 ROMS 표준 2단 구조:
1. **public 래퍼** `ana_xxx(ng,tile,model[,itrc])` — `tile.h` 인클루드 후 tile 범위(LBi..UBj) 계산, 모듈 변수(GRID/OCEAN/FORCES/BOUNDARY) 포인터를 인자로 넘겨 `_tile` 호출. 예 `ana_initial.h:38-59`, `ana_smflux.h:31-46`.
2. **`ana_xxx_tile(...)`** — 실제 해석식 본문. `set_bounds.h` 로 인덱스 범위 결정 후 DO 루프.

`ana_initial.h` 는 모델 종류(NLM/TLM/RPM/ADM)별로 별도 분기:
- `ana_initial.h:33` `IF (model.eq.iNLM) THEN` → `ana_NLMinitial_tile`
- `ana_initial.h:60` `ELSE IF ((model.eq.iTLM).or.(model.eq.iRPM))` (`#ifdef TANGENT`)

### ANANAME 추적 메커니즘
각 `ana_*` 는 자신이 사용된 헤더 파일명을 전역 배열 `ANANAME(인덱스)=MyFile` 에 등록 (`__FILE__` 매크로). 표준출력 메타데이터로 "어떤 해석 함수가 컴파일에 들어갔는지" 보고. 인덱스 고정 매핑 (`*.h` grep):

| idx | 함수 | idx | 함수 | idx | 함수 |
|---|---|---|---|---|---|
| 1 | biology | 13 | humid | 27 | tclima |
| 2 | initial | 14 | m2clima | 28 | passive |
| 3 | btflux | 15 | m2obc | 29 | rain |
| 4 | cloud | 16 | m3clima | 30 | drag/respiration |
| 5 | dqdsst | 17 | m3obc | 31 | stflux |
| 6 | fsobc | 18 | mask | 32 | respiration |
| 7 | grid | 19 | psource | 33 | tair |
| 8 | hmixcoef/nudgcoef | 20 | sediment | 34 | tobc |
| 9 | — | 21 | pair | 35 | vmix |
| 10 | — | 22 | spinning | 36 | winds |
| 11 | sponge/ssh | 23 | scope | 37 | wwave |
| 12 | — | 24 | smflux | 38 | wtype |

(예: `ROMS/Functionals/ana_initial.h:101` `        ANANAME(10)=MyFile`, `ROMS/Functionals/ana_grid.h:94` `        ANANAME( 7)=MyFile`, `ROMS/Functionals/ana_smflux.h:57` `        ANANAME(24)=MyFile`, `ROMS/Functionals/ana_tobc.h:48` `        ANANAME(34)=MyFile`, `ROMS/Functionals/ana_perturb.h:125` `        ANANAME(19)=MyFile`.) ANANAME 등록은 `Lanafile` 조건을 따른다. [10-14 전수 검증 정정]
비 `DISTRIBUTE`에서는 `IF (Lanafile.and.(tile.eq.0)) THEN`을 요구한다.
출처: `ROMS/Functionals/ana_btflux.h:39–43`, [testcases:RT1-1515](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안).

## 2. 기능별 카탈로그 (무엇을 해석적으로 지정하는가)

`analytical.F:18-71` 주석 + 각 파일 본문 인용.

### 2.1 초기조건 (Initial Conditions)
| 함수 | 지정 대상 | 인용 |
|---|---|---|
| `ana_initial` | 운동량(u,v,ubar,vbar), 자유표면 zeta, tracer t | `ana_initial.h:11-12` "sets initial conditions for momentum and tracer type variables" |
| `ana_passive` | passive inert tracer 초기장 | `ana_passive.h:11` |
| `ana_biology` | 생물 tracer 초기장 | `ana_biology.h:11` |
| `ana_sediment` | sediment tracer 농도(kg/m3) + bed 초기조건 | `ana_sediment.h:11-14` |
| `ana_vegetation` | 수중식생(SAV) 모델 초기조건 | `ana_vegetation.h:11` |
| `ana_perturb` | IC 섭동 (4D-Var/TLM/ADJ 검증용) | §3 참조 |

`ANA_BIOLOGY`가 해석 초기 조건을 선택한다.
NPZD의 `BioIni`는 그 조건에서 읽는다.
초기 상태 입력과 reaction 매개변수는 구분한다.
출처: `ROMS/Functionals/ana_biology.h:255–258`, `ROMS/Nonlinear/Biology/npzd_Franks_inp.h:72–81`, [biology:NT-021](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안).

### 2.2 격자·지형 (`ana_grid`)
`ana_grid.h:10` "sets model grid using an analytical expressions." 출력(공통블록 grid/scalars): `el, f, h, hmin, hmax, pm, pn, xl, xp, xr, yp, yr` (`ana_grid.h:18-32`).

도메인 크기·Coriolis·수심 입력 파라미터:
- `ana_grid.h:230-234`: `Xsize/Esize` (도메인 XI/ETA 길이 m), `depth` (최대 수심 m), `f0` (f-plane 상수 1/s), `beta` (beta-plane 1/s/m).

**idealized 응용별 CASE 분기** (`#if defined ... #elif ...`, `ana_grid.h:237-398`): BASIN, BENCHMARK, BL_TEST, CHANNEL, CANYON, COUPLING_TEST, DOUBLE_GYRE, ESTUARY_TEST, KELVIN, FLT_TEST, GRAV_ADJ, LAB_CANYON, LAKE_SIGNELL, LMD_TEST, MIXED_LAYER, OVERFLOW, RIVERPLUME1/2, SEAMOUNT, SOLITON, SED_TEST1, SED_TOY, SHOREFACE, TEST_CHAN, UPWELLING, WEDDELL, WINDBASIN. 예:
- `ana_grid.h:237-242` BASIN: `Xsize=3600 km, Esize=2800 km, depth=5000 m, f0=1e-4, beta=2e-11`
- `ana_grid.h:280-285` ESTUARY_TEST: `Xsize=100000 m, Esize=300 m, depth=10 m, f0=0`
- `ana_grid.h:305-309` LAB_CANYON: 극좌표 annulus (`Xsize=0.55` 환폭, `Esize=2π` 방위각 라디안)

수심 `h(i,j)` (`ana_grid.h:931~`)·Coriolis `f(i,j)` (`ana_grid.h:870~`) 도 응용별 분기. 곡선격자 각도 angler 는 `#if defined CURVGRID && defined UV_ADV` 가드 (`ana_grid.h:56`).

### 2.3 표면/바닥 플럭스 (forcing)
| 함수 | 지정 대상 (단위) | 인용 |
|---|---|---|
| `ana_smflux` | 운동량 표면 플럭스 = wind stress `sustr,svstr` (m²/s²) | `ana_smflux.h:10-11` |
| `ana_stflux` | tracer 표면 플럭스 `stflux(:,:,itrc)` (TracerUnits·m/s); set_vbc에서 stflx로 로드 | `ana_stflux.h:10-12` |
| `ana_btflux` | 수온 입력은 degC·m/s이다. 염분 freshwater 입력은 m/s이다. passive tracer 입력은 TracerUnits·m/s이다. | `ROMS/Functionals/ana_btflux.h:79, 90–91, 102` |
| `ana_srflux` | 표면 단파 복사 플럭스 `srflx` (degC·m/s) | `ana_srflux.h:11` |
| `ana_specir` | 해면 직하 분광 하향 조도 Ed(λ,0⁻) (μmol quanta/m²/s) | `ana_specir.h:11-13` |

`ana_btflux` 기본 본문은 itemp/isalt/passive 모두 0 플럭스 (`ana_btflux.h:82-110`; 예 `:85` `btflux(i,j,itrc)=0.0`).

salinity scale을 적용한 `btflx`의 단위와 입력 `btflux`의 단위는 구분한다 (`ROMS/Nonlinear/set_vbc.F:402`).
`SOLVE3D`와 `SALINITY`에서 nonzero bottom salt flux를 지정하는 경우의 입력 복사 누락 후보는 [RMF1-869](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#5-차이-결론)이다 (`ROMS/Nonlinear/set_vbc.F:24,363,402`). 이 후보의 근거 강도는 강함이다. [10-14 전수 검증 보완]
출처: [mixing-bc-forcing:RMF1-949, RMF1-950](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#4-노트-대조와-수정안).

내부 운동량 플럭스는 m²/s²이다.
내부 추적자 플럭스는 TracerUnits·m/s이다.
실습의 Pa·W/m² 그림은 물리 단위 표시이다.
출처: `ROMS/Functionals/ana_smflux.h:12`, `ROMS/Functionals/ana_stflux.h:12`, [da-4dvar:DA1-819](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md#4-노트-대조와-수정안).

`ana_smflux` 응용별 wind stress 해석식 (`ana_smflux.h:130~`):
- BASIN은 TANH 시간 ramp와 COS 공간 분포를 사용한다.
  출처: `ROMS/Functionals/ana_smflux.h:142` `      val1=5.0E-05_r8*(1.0_r8+TANH((time(ng)-6.0_r8*86400.0_r8)/        &`<br>`ROMS/Functionals/ana_smflux.h:143` `     &                 (3.0_r8*86400.0_r8)))`<br>`ROMS/Functionals/ana_smflux.h:147` `          sustr(i,j)=-val1*COS(val2*yr(i,j))`.
- UPWELLING은 `IF (NSperiodic(ng)) THEN` 분기가 먼저 선택된다 (`ROMS/Functionals/ana_smflux.h:307`).
- 그 분기가 선택되지 않고 EWperiodic이 참이면 서향 응력을 첫 2일 동안 sine 함수로 늘린다.
  출처: `ROMS/Functionals/ana_smflux.h:316` `      ELSE IF (EWperiodic(ng)) THEN`<br>`ROMS/Functionals/ana_smflux.h:317` `        IF ((tdays(ng)-dstart).le.2.0_r8) THEN`<br>`ROMS/Functionals/ana_smflux.h:318` `          windamp=-0.1_r8*SIN(pi*(tdays(ng)-dstart)/4.0_r8)/rho0`.
- 최종 물리 응력의 크기는 0.1 Pa다 (`ROMS/Functionals/ana_smflux.h:320` `          windamp=-0.1_r8/rho0`).
- 출처: [testcases:RT1-1517](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안).
- `ana_smflux.h:164-168` CANYON: `5e-5·SIN(2π·tdays/10)·(1-TANH((yr-0.5·el)/10000))`
- `ana_smflux.h:198-204` DOUBLE_GYRE: `windamp=-0.05/rho0`, `sustr=windamp·COS(val1·yr)` (전형적 wind-driven gyre)
- `ana_smflux.h:219-232` LAKE_SIGNELL: TANH 기반 ramp-up/ramp-down 윈도우

기본 헤더의 함수 선택 원문은 다음과 같다.

- `ROMS/Include/canyon.h:15` `#ifndef SOLVE3D                   /* 2D set-up */`.
- `ROMS/Include/canyon.h:24` `# define ANA_SMFLUX`.
- `ROMS/Include/canyon.h:38` `# define ANA_SMFLUX`.
- `ROMS/Include/double_gyre.h:36` `#define SOLVE3D`.
- `ROMS/Include/double_gyre.h:45` `# if defined SOLVE3D                   /* 3D Application */`.
- `ROMS/Include/double_gyre.h:75` `#  define ANA_SMFLUX`.
- `ROMS/Include/lake_signell.h:24` `#define SOLVE3D`.
- `ROMS/Include/lake_signell.h:70` `#define ANA_SMFLUX`.

출처: [testcases:RT1-1518](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안).

### 2.4 개경계조건 (Open Boundary Conditions)
| 함수 | 지정 대상 | 인용 |
|---|---|---|
| `ana_fsobc` | 자유표면 OBC `BOUNDARY%zeta_{west,east,...}` | `ana_fsobc.h:11-12` |
| `ana_m2obc` | 2D 운동량 OBC | `ana_m2obc.h:11-12` |
| `ana_m3obc` | 3D 운동량 OBC | `ana_m3obc.h:11-12` |
| `ana_tobc` | tracer OBC | `ana_tobc.h:11-12` |

`ana_fsobc` 조석 강제 예 (`ana_fsobc.h:77~`):
- `ana_fsobc.h:85-103` KELVIN: M2 조석 `omega=2π/(12.42·3600)`, `zeta_west=val·COS(omega·time)`, `zeta_east` 는 위상전파 포함
- `ana_fsobc.h:106-111` ESTUARY_TEST: `zeta_west=1·SIN(2π·time/(12·3600))` (12h 조석)
- `ana_fsobc.h:155-174` WEDDELL: M2 조석 진폭·위상 분포

경계 대입은 경계 자료 acquire·tile 조건을 따른다.
KELVIN의 서쪽 경계 조건은 `ROMS/Functionals/ana_fsobc.h:88` `      IF (LBC(iwest,isFsur,ng)%acquire.and.                             &`<br>`ROMS/Functionals/ana_fsobc.h:89` `     &    DOMAIN(ng)%Western_Edge(tile)) THEN`이다.
ESTUARY_TEST의 서쪽 경계 조건은 `ROMS/Functionals/ana_fsobc.h:107` `      IF (LBC(iwest,isFsur,ng)%acquire.and.                             &`<br>`ROMS/Functionals/ana_fsobc.h:108` `     &    DOMAIN(ng)%Western_Edge(tile)) THEN`이다.
WEDDELL의 서쪽 경계 조건은 `ROMS/Functionals/ana_fsobc.h:156` `      IF (LBC(iwest,isFsur,ng)%acquire.and.                             &`<br>`ROMS/Functionals/ana_fsobc.h:157` `     &    DOMAIN(ng)%Western_Edge(tile)) THEN`이다.
출처: [testcases:RT1-1519](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안).

### 2.5 기후값·넛징 (climatology / nudging)
| 함수 | 지정 대상 | 인용 |
|---|---|---|
| `ana_m2clima` / `ana_m3clima` | 2D/3D 운동량 기후값 | `ana_m2clima.h:11`, `ana_m3clima.h:11` |
| `ana_tclima` | tracer 기후값 | `ana_tclima.h:11` |
| `ana_ssh` | 해수면고도 기후값 | `ana_ssh.h:11` |
| `ana_nudgcoef` | 공간변동 넛징 계수 시간척도 (1/s) | `ana_nudgcoef.h:11-13` "spatially varying nudging coefficients time-scales (1/s) ... used for nuding to climatology" |

### 2.6 대기 강제 (bulk flux / ECOSIM 입력)
각 ANA의 포함 조건은 다음과 같다. 아래 include는 모두 `#ifdef ANALYTICAL` 안에 있다 (`ROMS/Functionals/analytical.F:84`). [10-14 전수 검증 보완]
출처: [mixing-bc-forcing:RMF1-951](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#4-노트-대조와-수정안).

| 함수 | 포함 CPP 조건 원문 | 코드 위치 |
|---|---|---|
| `ana_cloud` | `# ifdef SOLVE3D`<br>`#  if defined ANA_CLOUD && defined CLOUDS` | `ROMS/Functionals/analytical.F:97–99` |
| `ana_humid` | `# ifdef SOLVE3D`<br>`#  if defined ANA_HUMIDITY && \`<br>`    (defined BULK_FLUXES \|\| defined ECOSIM \|\| \`<br>`    (defined ANA_SRFLUX  && defined ALBEDO) )` | `ROMS/Functionals/analytical.F:125–128` |
| `ana_pair` | `# if defined ANA_PAIR && (defined BULK_FLUXES \|\| defined ECOSIM \|\| \`<br>`                          defined ATM_PRESS)` | `ROMS/Functionals/analytical.F:161–162` |
| `ana_rain` | `# ifdef SOLVE3D`<br>`#  if defined ANA_RAIN && defined BULK_FLUXES` | `ROMS/Functionals/analytical.F:178–179` |
| `ana_tair` | `# ifdef SOLVE3D`<br>`#  if defined ANA_TAIR && \`<br>`    (defined BULK_FLUXES \|\| defined ECOSIM \|\| \`<br>`    (defined ANA_SRFLUX && defined ALBEDO) )` | `ROMS/Functionals/analytical.F:246–249` |
| `ana_winds` | `# if defined ANA_WINDS && (defined BULK_FLUXES \|\| defined ECOSIM)` | `ROMS/Functionals/analytical.F:266` |

### 2.7 표면 보정용 관측장 (correction/relaxation)
`ana_sst`(SST degC, QCORRECTION용, `ana_sst.h:11-13`), `ana_sss`(SSS PSU, SCORRECTION/SRELAXATION용, `ana_sss.h:11-12`), `ana_dqdsst`(dQ/dSST 민감도, W/m²/degC → m/s/degC 스케일, `ana_dqdsst.h:11-14`).

### 2.8 혼합/마찰/스폰지 계수
| 함수 | 지정 대상 | 인용 |
|---|---|---|
| `ana_vmix` | 연직 혼합계수 Akv(운동량)·Akt(tracer) (m²/s) | `ana_vmix.h:11-12` |
| `ini_hmixcoef` | 현재 격자 크기에 따른 수평 혼합계수 조정 | `ROMS/Utility/ini_hmixcoef.F:301–312` |
| `ana_sponge` | 스폰지 영역 점성/확산 증대 (OBC/nesting 노이즈 억제) | `ana_sponge.h:11-14` |
| `ana_drag` | 공간변동 바닥조도 길이(m)/선형(m/s)/2차(무차원) 마찰계수 (활성 stress 식 의존) | `ana_drag.h:11-14` |
| `ana_wtype` | 공간변동 Jerlov 수괴 type 지수 (lmd_swfrac 단파흡수용) | `ana_wtype.h:11-14` |

과거 `ana_hmixcoef`는 격자 크기에 따라 수평 혼합계수를 조정했다.
`46f20897`(2014-03-13)에서 이 조정을 `ini_hmixcoef`로 옮겼다.
현재 해석 sponge 함수는 `ANA_SPONGE`로 선택하는 `ana_sponge`이다.
출처: `ROMS/Functionals/analytical.F:211–213`, [mixing-bc-forcing:RMF1-952](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#4-노트-대조와-수정안).

### 2.9 기타
- `ana_psource`: 질량/tracer point source/sink. **하천 유입을 point source로** (`ana_psource.h:11-12`). §4 참조.
- `ana_spinning`: 극좌표(annulus) 응용용 Coriolis+구심가속 합 회전력 (`ana_spinning.h:11-13`).
- `ana_wwave`: BBL용 풍성파 진폭·방향·주기 (`ana_wwave.h:11-12`).
- `ana_mask`: 해석적 육/해 마스킹 (`ana_mask.h:11`, `ANA_GRID && MASKING` 가드 `analytical.F:153-155`).
- `ana_respiration`: 저산소(hypoxia) 호흡률 (`ana_respiration.h:11-12`, `HYPOXIA_SRM` 가드).

`HYPOXIA_SRM`의 `ANA_RESPIRATION` 분기는 동봉 해석 함수로 `respiration`을 채운다.
이 함수는 `ResRate`를 대입한다.
`CHESAPEAKE_1TERM`의 지정 영역에는 0을 대입한다.
커널은 `cff1=dtdays*respiration(i,j,k)`를 산소 농도에서 직접 뺀다.
따라서 필요한 차원은 농도/일이다.
입력·화면 출력·NetCDF의 1/day 표기는 이 농도 소비식과 맞지 않는다.
출처: `ROMS/Functionals/ana_respiration.h:87–108`, `ROMS/Nonlinear/Biology/hypoxia_srm.h:334–338`, [biology:NT-022](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안).
- `ana_diag`: 사용자 정의 진단, 매 3D 스텝 종료 시 호출 (`ana_diag.h:11-13`).
- `ana_scope`: adjoint 민감도 공간 scope 마스킹 (`ana_scope.h:11-12`). §3 참조.

## 3. 4D-Var/Adjoint 연계 (data assimilation)

해석 함수 일부는 ROMS의 4D-Var(adjoint/TLM/representer) 프레임워크 전용. ([roms_4dvar](roms_4dvar.md), [roms_adjoint_framework](roms_adjoint_framework.md)의 IC 섭동·민감도 측면 보강.)

### ana_perturb — IC 섭동 (gradient 검증)
`ana_perturb.h:11-14`: "perturbs initial conditions ... It is also used to perturb the tangent linear and adjoint models at specified state variable and spatial (i,j,k) point to verify [adjoint correctness]."

섭동 위치 지정은 `user(:)` 입력 (`ana_perturb.h:31-34`):
- `user(1)` → 섭동할 state 변수, `user(2)/user(3)/user(4)` → I/J/K 인덱스.

tile 호출이 ADJ/TLM 상태배열 전체를 인자로 받음: `ad_t_obc, ad_u_obc, ..., ad_zeta_obc` (`ana_perturb.h:69-75`), `ad_ustr/ad_vstr, ad_tflux` (`ana_perturb.h:78-82`), `ad_t/ad_u/ad_v/ad_ubar/ad_vbar/ad_zeta` (`ana_perturb.h:85-90`). 즉 **OBC·표면강제·내부 state 모든 control 변수 단위 섭동** 가능 — adjoint 일관성(impulse-response) 검증의 표준 도구.

### ana_scope — 민감도 공간 scope
`ana_scope.h:11-12` adjoint 민감도 마스크. 인클루드 가드 (`analytical.F:190-195`): `ANA_GRID && (AD_SENSITIVITY || I4DVAR_ANA_SENSITIVITY || OPT_OBSERVATIONS || SENSITIVITY_4DVAR || SO_SEMI)`.

## 4. ana_psource — 하천/점원 상세

`ana_psource.h:11-12` "sets analytical tracer and mass point Sources and/or Sinks. River runoff can be consider as a point source."

설정 자료구조 (`ana_psource.h:146-154`): `Nsrc(ng)`(점원 개수), `Dsrc`(방향: 0=XI, 1=ETA, 2=W연직), `Isrc/Jsrc`(격자 위치). 응용별 분기 (`#if defined RIVERPLUME1 ...`, `:156~`):
- `ana_psource.h:156-173` RIVERPLUME1: 수평 하천 1개(`Dsrc=0, Isrc=2, Jsrc=50, LuvSrc=T`) + 연직 강수 점원 10개(`Dsrc=2, LwSrc=T`)

`LuvSrc`·`LwSrc`를 실제 runtime 입력으로 켜야 한다.
출처: `ROMS/Functionals/ana_psource.h:159, 165, 170`, [testcases:RT1-1520](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안).
- RIVERPLUME2 헤더는 `ANA_PSOURCE`를 정의한다 (`ROMS/Include/riverplume2.h:42`).
- 호출은 `IF (LuvSrc(ng).or.LwSrc(ng).or.ANY(LtracerSrc(:,ng))) THEN`을 따른다 (`ROMS/Nonlinear/set_data.F:130`).
- 위치 대입은 `IF ((iic(ng).eq.ntstart(ng)).or.(iic(ng).eq.0)) THEN` 안의 `IF (Master.and.DOMAIN(ng)%SouthWest_Test(tile)) THEN`에서 수행한다 (`ROMS/Functionals/ana_psource.h:144, 176`).
- `Nsrc(ng)=1+Lm(ng)*2`로 전체 수를 정한다 (`ROMS/Functionals/ana_psource.h:177`).
- 남북 경계의 ETA source 뒤에 XI source를 하나 추가한다 (`ROMS/Functionals/ana_psource.h:178–188`).
- 마지막 source에는 `SOURCES(ng)%Isrc(Nsrc(ng))=1`과 `SOURCES(ng)%Jsrc(Nsrc(ng))=60`을 대입한다 (`ROMS/Functionals/ana_psource.h:189–190`).
- 출처: [testcases:RT1-1521](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안).

질량유입 `Qbar`·연직분포·tracer 농도(`Tsrc`)도 동일 CASE 블록에서 해석 지정.

## 5. 요약

- ROMS 해석 함수는 컴파일타임 idealized 시나리오와 사용자 forcing 주입점이다.
- 현재 `ROMS/Functionals/`의 `.h` 파일은 42개이다.
- 실제 include 대상은 `analytical.F`의 CPP 조건을 따른다.
- `ana_vegetation.h`는 현재 `analytical.F`의 포함 목록에 없다.
- 출처: [build-options-history:RBH-3507](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#4-노트-대조와-수정안).
- IC(initial/passive/biology/sediment/vegetation), 격자(grid/mask), forcing(smflux/stflux/btflux/srflux/specir + 대기 bulk), OBC(fsobc/m2obc/m3obc/tobc), clima/nudge, 혼합·마찰(vmix/hmixcoef/sponge/drag/wtype), point source(psource), 4D-Var(perturb/scope) 망라.
- 각 함수 본문은 `#if defined <APP>` 분기로 BASIN·UPWELLING·KELVIN·ESTUARY_TEST·RIVERPLUME 등 공식 test case 해석식을 담는다 (예 `ana_grid.h:237-398`).
- `ANANAME(idx)=__FILE__` (`ana_perturb.h:56` 등)로 사용된 해석 함수가 런타임 메타데이터로 보고된다.

## 사례별 초기장 대조 (10-14)

ESTUARY_TEST의 격자 분기는 `Esize=300.0_r8`를 사용한다 (`ROMS/Functionals/ana_grid.h:282`).
SOLVE3D·SALINITY의 nonlinear 초기장 분기는 `IF (xr(i,j).le.30000.0_r8) then`에서 염분 30을 대입한다 (`ROMS/Functionals/ana_initial.h:660–662`).
SED_TOY의 SEDIMENT bed 초기화는 각 층에 0.01 m를 대입한다 (`ROMS/Functionals/ana_sediment.h:323, 329, 331`).
LAKE_SIGNELL의 SOLVE3D nonlinear 초기 수온은 10이다 (`ROMS/Functionals/ana_initial.h:716, 720`).
SALINITY가 있으면 LAKE_SIGNELL의 초기 염분은 30이다 (`ROMS/Functionals/ana_initial.h:721–722`).
각 값은 해당 ANA 함수가 선택되고 인용한 호출·분기 조건을 충족할 때 대입한다.
초기장 호출 조건 원문은 `ROMS/Nonlinear/initial.F:356` `        IF (nrrec(ng).eq.0) THEN`이다.
퇴적물 초기장 호출 조건 원문은 `ROMS/Nonlinear/initial.F:399` `        IF (nrrec(ng).eq.0) THEN`이다.
출처: [testcases:RT1-1536](../../../_staging/recovery/compare/roms-testcases-vs-code.md#4-노트-대조와-수정안).

## 문서와 코드 차이 (10-14 대조)

- [roms_analytical_functionals-differences-1.md](roms_analytical_functionals-differences-1.md)
- [roms_analytical_functionals-differences-2.md](roms_analytical_functionals-differences-2.md)

[note-job-16.tsv](../../../_staging/recovery/assign/note-job-16.tsv)는 `roms_analytical_functionals-differences-1.md`에 134행을 배정한다. [note-job-17.tsv](../../../_staging/recovery/assign/note-job-17.tsv)는 `roms_analytical_functionals-differences-2.md`에 133행을 배정한다. 두 배정표에서 이 두 파일에 배정한 267행의 결론별 개수는 A 13행, B 30행, C 178행, D 30행, E 1행, F 15행이다. [10-14 전수 검증 정정]
