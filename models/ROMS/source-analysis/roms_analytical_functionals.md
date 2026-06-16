---
title: "ROMS 해석 함수 — ana_* analytical functionals (idealized forcing/IC/BC)"
model: ROMS
component: ROMS/Functionals
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Functionals/). analytical.F 디스패처 + ana_grid.h/ana_initial.h/ana_smflux.h/ana_btflux.h/ana_fsobc.h/ana_psource.h/ana_perturb.h 등 헤더·tile 본문 file:line 인용. CPP 가드·ANANAME 인덱스·idealized CASE 분기 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/README.md
---

# ROMS 해석 함수 — ana_* analytical functionals

> ROMS의 idealized test case·사용자 정의 forcing/IC/BC를 해석식으로 지정하는 `ana_*` 패키지 (경로: roms/ROMS/Functionals/). 42개 `.h` 인클루드 파일 + 디스패처 `analytical.F`.

## 1. 패키지 구조와 디스패처

해석 함수는 모두 `analytical_mod` 모듈 안에 **`#include <ana_*.h>`** 로 인라인되는 인클루드 파일이다. `Functionals/analytical.F:2` 가 모듈 본체, 각 기능은 `.h`로 분리.

목적 요약은 `analytical.F:11-71` 헤더 주석에 카탈로그로 정리됨:
- `analytical.F:13-14`: "This package is used to provide various analytical fields to the model when appropriate."

전체가 **`#ifdef ANALYTICAL`** (`analytical.F:84`) 가드 아래 있고, 각 `.h` 는 추가 CPP 조건으로 인클루드된다 (예: `analytical.F:121-123` `ANA_GRID`, `analytical.F:133-135` `ANA_INITIAL`, `analytical.F:203-205` `ANA_SMFLUX`).

User 사설 응용용 템플릿이 별도 존재:
- `analytical.F:73-76`: "Notice that there is a template copy of each header file in the 'User/Functionals' directory ... distinguishing between official idealized problems and user interface."

### 호출/디스패치 구조 (3계층 tile 패턴)
각 `ana_*.h` 는 ROMS 표준 2단 구조:
1. **public 래퍼** `ana_xxx(ng,tile,model[,itrc])` — `tile.h` 인클루드 후 tile 범위(LBi..UBj) 계산, 모듈 변수(GRID/OCEAN/FORCES/BOUNDARY) 포인터를 인자로 넘겨 `_tile` 호출. 예 `ana_initial.h:32-53`, `ana_smflux.h:31-46`.
2. **`ana_xxx_tile(...)`** — 실제 해석식 본문. `set_bounds.h` 로 인덱스 범위 결정 후 DO 루프.

`ana_initial.h` 는 모델 종류(NLM/TLM/RPM/ADM)별로 별도 분기:
- `ana_initial.h:31` `IF (model.eq.iNLM) THEN` → `ana_NLMinitial_tile`
- `ana_initial.h:54` `ELSE IF ((model.eq.iTLM).or.(model.eq.iRPM))` (`#ifdef TANGENT`)

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

(예: `ana_initial.h:66` `ANANAME(2)`, `ana_grid.h:94`/`:95` `ANANAME(7),(10)`, `ana_smflux.h` `ANANAME(24)`, `ana_tobc.h:48` `ANANAME(34)`, `ana_perturb.h:56` `ANANAME(48)=__FILE__`.) 등록 코드는 `#ifdef DISTRIBUTE` 하 master tile 만 기록 (`ana_btflux.h:39-43`).

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
| `ana_btflux` | tracer 바닥 플럭스 `btflux` (TracerUnits·m/s) | `ana_btflux.h:10-12` |
| `ana_srflux` | 표면 단파 복사 플럭스 `srflx` (degC·m/s) | `ana_srflux.h:11` |
| `ana_specir` | 해면 직하 분광 하향 조도 Ed(λ,0⁻) (μmol quanta/m²/s) | `ana_specir.h:11-13` |

`ana_btflux` 기본 본문은 itemp/isalt/passive 모두 0 플럭스 (`ana_btflux.h:82-110`; 예 `:85` `btflux(i,j,itrc)=0.0`).

`ana_smflux` 응용별 wind stress 해석식 (`ana_smflux.h:130~`):
- `ana_smflux.h:142-147` UPWELLING: `val1=5e-5·(1+TANH((time-6일)/...))` 시간 ramp, `sustr=-val1·COS(val2·yr)`
- `ana_smflux.h:164-168` CANYON: `5e-5·SIN(2π·tdays/10)·(1-TANH((yr-0.5·el)/10000))`
- `ana_smflux.h:198-204` DOUBLE_GYRE: `windamp=-0.05/rho0`, `sustr=windamp·COS(val1·yr)` (전형적 wind-driven gyre)
- `ana_smflux.h:219-232` LAKE_SIGNELL: TANH 기반 ramp-up/ramp-down 윈도우

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

### 2.5 기후값·넛징 (climatology / nudging)
| 함수 | 지정 대상 | 인용 |
|---|---|---|
| `ana_m2clima` / `ana_m3clima` | 2D/3D 운동량 기후값 | `ana_m2clima.h:11`, `ana_m3clima.h:11` |
| `ana_tclima` | tracer 기후값 | `ana_tclima.h:11` |
| `ana_ssh` | 해수면고도 기후값 | `ana_ssh.h:11` |
| `ana_nudgcoef` | 공간변동 넛징 계수 시간척도 (1/s) | `ana_nudgcoef.h:11-13` "spatially varying nudging coefficients time-scales (1/s) ... used for nuding to climatology" |

### 2.6 대기 강제 (bulk flux / ECOSIM 입력)
모두 `SOLVE3D` + (`BULK_FLUXES`/`ECOSIM`/`ALBEDO`) 가드. `ana_cloud`(구름분율, `ana_cloud.h:11`), `ana_humid`(대기 습도 3종, `ana_humid.h:11-14`), `ana_pair`(대기압 mb, `ana_pair.h:11`), `ana_rain`(강수율 kg/m²/s, `ana_rain.h:11`), `ana_tair`(대기온 degC, `ana_tair.h:11`), `ana_winds`(표면풍, `ana_winds.h:11`).

### 2.7 표면 보정용 관측장 (correction/relaxation)
`ana_sst`(SST degC, QCORRECTION용, `ana_sst.h:11-13`), `ana_sss`(SSS PSU, SCORRECTION/SRELAXATION용, `ana_sss.h:11-12`), `ana_dqdsst`(dQ/dSST 민감도, W/m²/degC → m/s/degC 스케일, `ana_dqdsst.h:11-14`).

### 2.8 혼합/마찰/스폰지 계수
| 함수 | 지정 대상 | 인용 |
|---|---|---|
| `ana_vmix` | 연직 혼합계수 Akv(운동량)·Akt(tracer) (m²/s) | `ana_vmix.h:11-12` |
| `ana_hmixcoef` | 수평 혼합계수 격자크기 rescale + 스폰지 증대 | `ana_hmixcoef.h:11-13` |
| `ana_sponge` | 스폰지 영역 점성/확산 증대 (OBC/nesting 노이즈 억제) | `ana_sponge.h:11-14` |
| `ana_drag` | 공간변동 바닥조도 길이(m)/선형(m/s)/2차(무차원) 마찰계수 (활성 stress 식 의존) | `ana_drag.h:11-14` |
| `ana_wtype` | 공간변동 Jerlov 수괴 type 지수 (lmd_swfrac 단파흡수용) | `ana_wtype.h:11-14` |

### 2.9 기타
- `ana_psource`: 질량/tracer point source/sink. **하천 유입을 point source로** (`ana_psource.h:11-12`). §4 참조.
- `ana_spinning`: 극좌표(annulus) 응용용 Coriolis+구심가속 합 회전력 (`ana_spinning.h:11-13`).
- `ana_wwave`: BBL용 풍성파 진폭·방향·주기 (`ana_wwave.h:11-12`).
- `ana_mask`: 해석적 육/해 마스킹 (`ana_mask.h:11`, `ANA_GRID && MASKING` 가드 `analytical.F:153-155`).
- `ana_respiration`: 저산소(hypoxia) 호흡률 (`ana_respiration.h:11-12`, `HYPOXIA_SRM` 가드).
- `ana_diag`: 사용자 정의 진단, 매 3D 스텝 종료 시 호출 (`ana_diag.h:11-13`).
- `ana_scope`: adjoint 민감도 공간 scope 마스킹 (`ana_scope.h:11-12`). §3 참조.

## 3. 4D-Var/Adjoint 연계 (data assimilation)

해석 함수 일부는 ROMS의 4D-Var(adjoint/TLM/representer) 프레임워크 전용. ([[roms_4dvar]], [[roms_adjoint_framework]] 의 IC 섭동·민감도 측면 보강.)

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
- `ana_psource.h:175-183` RIVERPLUME2: `Nsrc=1+Lm·2`, ETA 방향(`Dsrc=1`) 경계 따라 분포

질량유입 `Qbar`·연직분포·tracer 농도(`Tsrc`)도 동일 CASE 블록에서 해석 지정.

## 5. 요약

- ROMS 해석 함수 = **컴파일타임 idealized 시나리오 + 사용자 forcing 주입점**. 42 `.h` 파일이 `analytical_mod` (`analytical.F:2`)에 CPP 가드로 인라인.
- IC(initial/passive/biology/sediment/vegetation), 격자(grid/mask), forcing(smflux/stflux/btflux/srflux/specir + 대기 bulk), OBC(fsobc/m2obc/m3obc/tobc), clima/nudge, 혼합·마찰(vmix/hmixcoef/sponge/drag/wtype), point source(psource), 4D-Var(perturb/scope) 망라.
- 각 함수 본문은 `#if defined <APP>` 분기로 BASIN·UPWELLING·KELVIN·ESTUARY_TEST·RIVERPLUME 등 공식 test case 해석식을 담는다 (예 `ana_grid.h:237-398`).
- `ANANAME(idx)=__FILE__` (`ana_perturb.h:56` 등)로 사용된 해석 함수가 런타임 메타데이터로 보고된다.
