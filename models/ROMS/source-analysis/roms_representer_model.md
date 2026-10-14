---
title: "ROMS Representer Model (RPM) — 유한진폭 접선선형(finite-amplitude TL) + Picard 반복 / R4D-Var"
model: ROMS
component: ROMS/Representer
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Representer/, roms/ROMS/Drivers/, roms/ROMS/Modules/). rp_main3d.F·rp_initial.F·rp_post_initial.F·rp_diag.F·rp_rhs3d.F·rp_pre_step3d.F·rp_prsgrd.F·rp_t3drelax.F·rp_uv3drelax.F·rp_def_ini.F 헤더·본문, Drivers/picard_roms.h·rp_roms.h, Modules/mod_param.F(iRPM) file:line 인용. 2026-10-14 ROMS recovery 대조 보고서 반영"
last_source_check: "2026-10-14 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_4dvar.md
  - models/ROMS/source-analysis/roms_adjoint_framework.md
  - models/ROMS/README.md
---

# ROMS Representer Model (RPM) — 유한진폭 접선선형 + Picard 반복

> Representer 모델: indirect-representer 기반 W4DVAR/R4DVAR(weak-constraint 4D-Var)의 순방향 엔진. `rp_*` 루틴군이 "유한진폭 접선선형(finite-amplitude tangent linear)" 방정식을 BASIC STATE(직전 Picard 반복 해) 주위에서 적분한다. (경로: `roms/ROMS/Representer/`, 드라이버 `roms/ROMS/Drivers/picard_roms.h`·`rp_roms.h`)

관련 노트: [roms_4dvar](roms_4dvar.md) (4D-Var 전체 흐름·dual formulation), [roms_adjoint_framework](roms_adjoint_framework.md) (adjoint `ad_*`), [roms_main_driver_dispatch](roms_main_driver_dispatch.md) (드라이버 디스패치). 본 노트는 **RPM 고유 영역**(rp_* 엔진·Picard 반복·RPM_RELAXATION·weak-constraint impulse 결합)에 집중한다.

## 1. 정체성 — RPM 은 무엇인가

전체 디렉토리는 `TL_IOMS` (Tangent Linear Inverse Ocean Modeling System) 매크로로 가드된다. 예: `rp_main3d.F:2` `#if defined TL_IOMS && defined SOLVE3D`, `rp_initial.F:2` `#ifdef TL_IOMS`.

모델 인덱스는 `iRPM`. 정의가 결정적이다:

- `Modules/mod_param.F:664` — `integer, parameter :: iRPM = 3   ! finite-amplitude tangent linear`

즉 RPM 은 일반 접선선형(TLM, iTLM)과 달리 **유한진폭(finite-amplitude) 접선선형**이며, `Representer/` **39개 `.F` 중 23개**가 `iRPM` 인덱스를 사용한다 (예: `rp_diag.F:45` `CALL wclock_on (ng

지배방정식의 기호 형태는 Picard 드라이버 헤더에 명시되어 있다:

- `Drivers/picard_roms.h:14-22`:
  > "all tangent linear variables are in term of the full fields and the model can expressed symbolically as: `d(S')/d(t) = N(So) + A(S' - So)` where S' is the tangent linear state and So is the 'basic state'. The 'basic state' here is the solution of previous tangent linear model iteration."

$$\frac{dS'}{dt} = N(S_o) + A\,(S' - S_o)$$

- $S'$ : (유한진폭) 접선선형 전체장 상태
- $S_o$ : BASIC STATE = **직전 Picard 반복의 해**
- $N$ : 비선형 연산자, $A$ : 선형(접선) 연산자

이 형태가 RPM 을 순수 TLM과 구분한다: RPM 변수는 perturbation 이 아니라 full field 로 표현되며, BASIC STATE 가 매 Picard 반복마다 갱신된다.

## 2. Picard 반복 — indirect representer 의 핵

`Drivers/picard_roms.h` 가 RPM 의 외부 반복 루프를 구동한다.

- `picard_roms.h:10-13` 헤더:
  > "ROMS Picard Iterations Driver: This driver is used to perform the Picard iterations test for the representers tangent linear model used in IOMs weak constraint 4D variational data assimilation (R4D-Var)."

루프 구조 (`picard_roms.h`):

| 단계 | 코드 | 라인 |
|---|---|---|
| Picard 반복 헤더 출력 | `WRITE (stdout,20) 'ROMS Picard Iteration: ', Nrun, ng,` | `picard_roms.h:244` |
| RPM 초기화 | `CALL rp_initial (ng)` | `picard_roms.h:264` |
| RPM 시간적분 (3D) | `CALL rp_main3d (RunInterval)` | `picard_roms.h:279` |
| RPM 시간적분 (2D) | `CALL rp_main2d (RunInterval)` | `picard_roms.h:281` |
| 파일 close (TLM/FWD) | `CALL close_file (ng, iRPM, TLM(ng))` / `... FWD(ng)` | `picard_roms.h:289`, `292` |

각 Picard 반복은 직전 해를 BASIC STATE 로 받아 `d(S')/dt = N(So) + A(S'-So)` 를 다시 적분한다. 반복이 수렴하면 비선형 궤적에 일치하는 접선선형 궤적을 얻는다 — 이것이 indirect representer 방법에서 representer 행렬을 명시적으로 만들지 않고 observation-space 최소화를 가능케 하는 순방향 적분이다.

별도로 `rp_roms.h` 는 단일 RPM 실행(ESMF init/run/finalize) 드라이버:

- `rp_roms.h:12` > "This driver executes ROMS representers tangent linear model."
- `rp_roms.h:220` > "Initialize finite amplitude tangent linear (representer) model." → `rp_roms.h:226` `CALL rp_initial (ng)`
- 입력 파싱도 iRPM: `rp_roms.h:128` `CALL inp_par (iRPM)`

RPM 을 사용하는 상위 드라이버들 (iRPM grep): `Drivers/r4dvar.F`, `Drivers/tl_r4dvar_roms.h`, `Drivers/array_modes.h`, `Drivers/obs_sen_r4dvar_analysis.h`, `Drivers/picard_roms.h`, `Drivers/rp_roms.h`.

RPM은 R4D-Var의 prior·analysis 궤적을 적분한다(`ROMS/Drivers/r4dvar.F:906`, `ROMS/Drivers/r4dvar.F:1694`).
inner-loop의 행렬 작용은 ADM·공분산·TLM으로 계산한다(`ROMS/Drivers/r4dvar.F:1074`, `ROMS/Drivers/r4dvar.F:1128–1130`, `ROMS/Drivers/r4dvar.F:1212`).
이 내부 반복은 `# ifndef DATALESS_LOOPS` 아래에 있다(`ROMS/Drivers/r4dvar.F:879`, `ROMS/Drivers/r4dvar.F:1384`).

## 3. 시간적분 드라이버 `rp_main3d`

`rp_main3d.F:3` `SUBROUTINE rp_main3d (RunInterval)`. 헤더 `rp_main3d.F:12-16`:
> "This routine is the main driver for representers tangent linear ROMS when configure as a full 3D baroclinic ocean model. It advances forward the representer model equations for all nested grids ..."

시간스텝 루프(`rp_main3d.F:138` `STEP_LOOP`) 1 step 내 호출 순서 (핵심):

| 순서 | 호출 | 라인 | 역할 |
|---|---|---|---|
| 입력 read | `rp_get_data (ng)` | `rp_main3d.F:163` | NetCDF 강제력·BASIC STATE 읽기 |
| 데이터 처리 | `rp_set_data (ng, tile)` | `rp_main3d.F:176` | 시간보간 |
| BASIC STATE 깊이 | `set_depth (ng,tile,iRPM)` | `rp_main3d.F:178` | `FORWARD_READ` |
| BASIC STATE 질량플럭스 | `set_massflux (ng,tile,iRPM)` | `rp_main3d.F:193` | `FORWARD_READ` |
| **weak-constraint 강제** | `tl_forcing (ng,tile,...)` | `rp_main3d.F:211` | §4 |
| 첫 step 초기화 | `rp_post_initial (ng, iRPM)` | `rp_main3d.F:227` | §5 |
| RPM 질량플럭스 | `rp_set_massflux (ng,tile,iRPM)` | `rp_main3d.F:239` | |
| RPM 상태방정식 | `rp_rho_eos (ng,tile,iRPM)` | `rp_main3d.F:241` | `!TS_FIXED` |
| 진단 | `rp_diag (ng,tile)` | `rp_main3d.F:246` | §6 |
| 수직경계 | `rp_set_vbc (ng,tile)` | `rp_main3d.F:304` | |
| OBC 증분 조정 | `rp_obc_adjust`, `rp_obc2d_adjust` | `rp_main3d.F:322`,`324` | `ADJUST_BOUNDARY` |
| 표면강제 증분 | `rp_frc_adjust (ng,tile,Lfinp)` | `rp_main3d.F:341` | `ADJUST_STFLUX/WSTRESS` |
| 수직속도 | `rp_omega (ng,tile,iRPM)` | `rp_main3d.F:363` | |
| 자유표면 시간평균 | `rp_set_zeta (ng,tile)` | `rp_main3d.F:377` | |
| 출력 | `rp_output (ng)` | `rp_main3d.F:396` | |

3D 운동량/추적자 시간적분 본체(`rp_step3d_uv`, `rp_step3d_t`, `rp_step2d` 등)는 위 발췌 이후 루프 후반에서 호출된다(`rp_main3d.F:98-100`의 `USE` 선언으로 확인).

## 4. Weak-constraint impulse forcing 결합 (R4D-Var)

RPM 이 4D-Var 약제약(weak constraint) 에서 핵심인 이유: convolved adjoint 해의 impulse 를 매 step 주입한다.

- `rp_main3d.F:198-216` (`#ifdef WEAK_CONSTRAINT`) 헤더 주석:
  > "If appropriate, add convolved adjoint solution impulse forcing to the representer model solution. Notice that the forcing is only needed after finishing all inner loops. The forcing is continuous. That is, it is time interpolated at every time-step from available snapshots (FrequentImpulse=TRUE)."
- 조건·호출: `rp_main3d.F:209` `IF (FrequentImpulse(ng)) THEN` → `rp_main3d.F:211` `CALL tl_forcing (ng, tile, kstp(ng), nstp(ng))` (모듈 `tl_forcing_mod`, `rp_main3d.F:105`).

즉 RPM 은 [roms_adjoint_framework](roms_adjoint_framework.md)의 adjoint 해를 배경오차공분산으로 convolve 한 impulse 를 강제력으로 받아, observation-space(dual) 최소화에서 나온 increment 를 순방향으로 전파한다.
R4의 분석 RPM에서 impulse는 inner-loop 종료 후에만 주입된다(`ROMS/Representer/rp_main3d.F:198–216`).
이 impulse는 `FrequentImpulse` 조건에서 시간 보간된다(`ROMS/Representer/rp_main3d.F:209–211`).
최종 계수를 기록하는 `wrt_impulse`는 분석 RPM의 강제를 준비한다. `DISTRIBUTE`에서는 `CALL wrt_impulse (ng, MyRank, iADM, ADM(ng)%name)`를 호출한다. 그 외에는 `CALL wrt_impulse (ng, -1, iADM, ADM(ng)%name)`를 호출한다(`ROMS/Drivers/r4dvar.F:1365–1380`). [10-14 전수 검증 정정]

## 5. 초기화 — `rp_initial` / `rp_post_initial`

`rp_initial.F:3` `SUBROUTINE rp_initial (ng)`, 헤더 `rp_initial.F:12` > "This routine initializes representers tangent linear model." 로그 `rp_initial.F:122` `'initializing representer model ...'`.

BASIC STATE 와 adjoint 의 관계 — `rp_initial.F:162`:
> "... value is assigned when computing or processing the basic state trajectory needed to linearize the adjoint model."

초기시각 처리(`rp_initial.F:164-172`): NLM IC 시각 `INItime(ng)` 가 알려져 있으면 그것을, 아니면 `dstart` 를 사용. → `ntstart`/`ntend` 산정(`rp_initial.F:174-175`).

약제약 시 RPM 초기조건 파일 정의: `rp_initial.F:72-74` (`#ifdef WEAK_CONSTRAINT`) `USE rp_def_ini_mod, ONLY : rp_def_ini`. 모듈 `rp_def_ini.F:12` > "This module opens existing representer model initial conditions" — `iRPM` 으로 NetCDF/PIO 변수 정의(`rp_def_ini.F:139`, `:408`, `:931` 등).

첫 step 후처리 `rp_post_initial.F:39` `SUBROUTINE rp_post_initial (ng, model)`, 헤더 `rp_post_initial.F:13-16`:
> "On the first timestep, it computes the initial depths and level thicknesses from the initial free-surface field. Additionally, it initializes the representer state variables for all time levels and applies lateral boundary conditions."

내부: `rp_ini_zeta`→`rp_set_depth`(`rp_post_initial.F:56-57`), `rp_ini_fields`(`:66`), nesting 시 `rp_nesting(...,ngetD)`(`:78`).

## 6. 진단 `rp_diag` — adjoint 미구현 경고

`rp_diag.F:12-13` > "This routine computes various representer tangent linear diagnostic fields." 부피평균 운동/위치/총 에너지·부피를 `tl_*` 장으로 계산(`rp_diag.F:154-191`, `tl_Hz`/`tl_z_w`/`tl_rho`/`tl_u`/`tl_v` 등).

중요한 주석 — `rp_diag.F:153-157`:
> "Compute and report out volume averaged kinetic, potential total energy, and volume of tangent linear fields. **Notice that the proper adjoint of these quantities are not coded.**"

→ 진단량은 adjoint 가능하지 않으므로 4D-Var cost-function 계산에 직접 들어가지 않는 보고용. blow-up 검출(`NaN`/`*`)로 `exit_flag=1`(`rp_diag.F:312-318`).

## 7. 우변 — BASIC STATE 주위 선형화

`rp_rhs3d.F:3` `#if defined TL_IOMS && defined SOLVE3D`, 헤더 `rp_rhs3d.F:12-17`:
> "This subroutine evaluates representers tangent linear right-hand-side terms for 3D momentum and tracers equations. BASIC STATE variables needed: Hz, Huon, HVom, u, v, W, uclm, vclm, sustr, svstr, bustr, bvstr."

각 항은 BASIC STATE와 Representer 전체장 변수를 함께 받는다(`rp_rhs3d.F:121-178` argument 목록).
BASIC STATE와 Representer 변수의 쌍은 `Hz`·`tl_Hz`, `Huon`·`tl_Huon`, `Hvom`·`tl_Hvom`, `u`·`tl_u`, `v`·`tl_v`, `W`·`tl_W`, `sustr`·`tl_sustr` 등이다(`rp_rhs3d.F:121-178`).

선형화 곱 패턴 — 예 표면응력 항(`rp_rhs3d.F:479-481`):
```
tl_Uwrk(i,j)=tl_sustr(i,j)*cff1+
&            sustr(i,j)*tl_cff1- ...
```
`TL_IOMS`의 Representer 변수는 전체장이다(`ROMS/Representer/rp_ini_fields.F:339–357`).
순수 TLM 증분 변수와 같은 뜻으로 쓰지 않는다([da-representer:RT2-366](../../../_staging/recovery/compare/roms-da-representer-vs-code.md#5-차이-결론)).

`rp_pre_step3d.F:13-14` > "This subroutine initialize computations for new time step of the representers tangent linear 3D primitive variables."
헤더는 Adams/Bashforth의 n-1·n-2 항 추가를 설명한다(`rp_pre_step3d.F:16–19`).
헤더의 Crank–Nicolson 설명은 현재 `lambda` 대입과 구분한다([theory-numerics:RTN-384](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#4-노트-대조와-수정안)).
현행 공통 `lambda`는 1이다(`ROMS/Modules/mod_scalars.F:760–765`).
현재 단계 확산 기여 `dt*(1-lambda)`는 0이다(`ROMS/Nonlinear/pre_step3d.F:917–925`, `ROMS/Representer/rp_pre_step3d.F:1337–1364`). [10-14 전수 검증 보완]
미래 단계는 backward implicit으로 계산한다(`ROMS/Nonlinear/step3d_t.F:1730–1734`, `ROMS/Representer/rp_step3d_t.F:1479–1500`). [10-14 전수 검증 보완]
`lambda=0.5`일 때만 Crank–Nicolson이다(`ROMS/Modules/mod_scalars.F:756–758`).
필요한 BASIC STATE 목록은 `AKt, AKv, Huon, Hvom, Hz, Tsrc, W, bustr, bvstr, ghats, srflx, sustr, svstr, t, z_r, z_w`이다(`rp_pre_step3d.F:29-31`).

압력경도 디스패치 `rp_prsgrd.F:10-13` > "This routine computes the representers tangent linear baroclinic hydrostatic pressure gradient term." — cppdefs 따라 `rp_prsgrd40.h`(PJ_GRADP), `rp_prsgrd32.h`(DJ_GRADPS), `rp_prsgrd31.h`(기본) 중 include (`rp_prsgrd.F:16-26`).

## 8. RPM 고유 — Picard 안정화 relaxation (`RPM_RELAXATION`)

순수 TLM/ADM 에는 없고 RPM 에만 존재하는 안정화 기법. 현재 Picard 반복 해를 **직전 Picard 반복 해(BASIC STATE)** 로 확산 relaxation 하여 수렴·안정성을 개선한다.

추적자: `rp_t3drelax.F:4` `#if defined TL_IOMS && defined RPM_RELAXATION && defined SOLVE3D`, 헤더 `rp_t3drelax.F:13-15`:
> "This routine relaxes current representer tangent linear tracer type variables to previous Picard iteration solution (basic state) to improve stability and convergence."

핵심 계산(`rp_t3drelax.F:138-176`): 계수 `tl_Tdiff(itrc,ng)>0` 일 때, 현재−직전 반복 차분의 확산플럭스를 적분.
플럭스(`rp_t3drelax.F:146-149`):
```
FX(i,j)=0.5*tl_Tdiff(itrc,ng)*pmon_u(i,j)*(Hz(i,j,k)+Hz(i-1,j,k))*
&       (tl_t(i  ,j,k,nrhs,itrc)-t(i  ,j,k,nrhs,itrc)-
&        tl_t(i-1,j,k,nrhs,itrc)+t(i-1,j,k,nrhs,itrc))
```
$(tl\_t - t)$ = (현재 RPM 해) − (BASIC STATE) 의 수평 라플라시안 확산. 주석 `rp_t3drelax.F:132-136` > "Compute horizontal diffusion relaxation of tracers between current and previous representer tangent linear Picard iteration trajectory (basic state)."

운동량: `rp_uv3drelax.F:4` 동일 가드, 헤더 `rp_uv3drelax.F:13-14` > "This routine relaxes current representer tangent linear 3D momentum to previous Picard iteration solution (basic state)" — `rp_uv3drelax.F:153` 동일 설명.

디스패치 위치 — `rp_rhs3d.F:51-53` (`#ifdef RPM_RELAXATION` `USE rp_t3drelax_mod`), `:60-62` (`USE rp_uv3drelax_mod`). 호출 `rp_pre_step3d` 경유 `rp_rhs3d.F:104-113`:
> "Improve stability and convergence of the tangent linear representer model tracer type variables by a 'diffusive relaxation' to previous Picard iteration solution." → `CALL rp_t3drelax (ng, tile)`.

## 9. 파일군 역할 요약

전체 58 항목. `rp_*` 접두 = iRPM(유한진폭 TL) 엔진. 분류:

| 그룹 | 대표 파일 | 역할 |
|---|---|---|
| 드라이버/제어 | `rp_main3d.F`, `rp_main2d.F`, `rp_initial.F`, `rp_post_initial.F` | RPM 시간적분·초기화 |
| 3D 엔진 | `rp_rhs3d.F`, `rp_pre_step3d.F`, `rp_step3d_uv.F`, `rp_step3d_t.F`, `rp_prsgrd.F`(+`.h`) | 운동량·추적자 RHS/시간스텝 |
| 2D 엔진 | `rp_step2d.F`가 `rp_step2d_LF_AM3.h`만 포함한다(`ROMS/Representer/rp_step2d.F:21`). | LF-AM3 순압 시간계 |
| 수평혼합 | `rp_t3dmix{2,4}_*.h`, `rp_uv3dmix{2,4}_*.h` | harmonic/biharmonic, geo/iso/s 좌표 |
| **Picard relaxation** | `rp_t3drelax.F`, `rp_uv3drelax.F` | RPM 고유 안정화 (§8) |
| 경계조건 | `rp_zetabc.F`, `rp_{u,v}2dbc_im.F`, `rp_{u,v,t}3dbc_im.F`, `rp_obc_adjust.F`, `rp_obc_volcons.F` | LBC + OBC 증분 조정 |
| 물리/강제 | `rp_rho_eos.F`, `rp_set_vbc.F`, `rp_bulk_flux.F`, `rp_lmd_swfrac.F`, `rp_set_data.F`, `rp_get_data.F`, `rp_get_idata.F`, `rp_frc_adjust.F` | 상태방정식·플럭스·강제 증분 |
| 기하/깊이 | `rp_set_depth.F`, `rp_omega.F`, `rp_set_massflux.F`, `rp_set_zeta.F`, `rp_ini_fields.F` | 수직격자·질량플럭스 |
| I/O | `rp_def_ini.F`, `rp_wrt_ini.F`, `rp_output.F`, `rp_diag.F` | NetCDF 정의/쓰기·진단 |

미구현(stub) 마커: BBL(`rp_main3d.F:51-53`), GLS/LMD/MY25 mixing(`:64-74`), sediment(`:86-88`), tides(`:91-93`), floats(`:101-103`) 는 `*_NOT_YET` cppdef 로 비활성(`!!` 주석).

## 10. 4D-Var·adjoint 프레임워크와의 관계

관련 노트는 [roms_4dvar](roms_4dvar.md)와 [roms_adjoint_framework](roms_adjoint_framework.md)이다.

- **adjoint(`ad_*`)** 가 cost-function 경도/impulse 를 만든다 → 배경오차공분산 convolution → **RPM(`rp_*`)** 이 그 impulse 를 `tl_forcing`(§4)으로 받아 순방향 전파.
- RPM 의 **Picard 반복**(§2)이 비선형 궤적 주위 유한진폭 TL 해를 수렴시켜 indirect-representer dual(observation-space) 최소화를 닫는다.
- iRPM(=3) 은 iNLM/iTLM/iADM 과 구분되는 별도 모델 인덱스(`mod_param.F:664`)로, 동일 코어 물리를 finite-amplitude TL 형태로 재구현한 것.

## 11. Representer 계수와 관련 구현 위치

R4DVAR의 increment는 `congrad`를 호출한다(`ROMS/Drivers/r4dvar.F:1013`, `ROMS/Drivers/r4dvar.F:1259`).
간접 Representer 계수는 `congrad`에서 `(R_n + Cobs) * Beta_n = h_n`을 푼다(`ROMS/Utility/congrad.F:24`).
관측 잔차는 `h_n = Xo - H * X_n`이다(`ROMS/Utility/congrad.F:26`).
행렬은 `P_n = R_n + Cobs`이다(`ROMS/Utility/congrad.F:36`).
행렬 작용은 `P_n * PSI = R_n * PSI + Cobs * PSI`이다(`ROMS/Utility/congrad.F:40`).

I4DVAR의 최소화기 호출 위치는 `ROMS/Drivers/i4dvar.F:1524`이다.
RBL4DVAR의 최소화기 호출 위치는 `ROMS/Drivers/rbl4dvar.F:1354`, `ROMS/Drivers/rbl4dvar.F:1364`, `ROMS/Drivers/rbl4dvar.F:1595`이다.
`zgrad0`의 생산·소비 위치는 `ROMS/Utility/rpcg_lanczos.F:251`, `ROMS/Utility/rpcg_lanczos.F:257`이다.
`cg_beta`의 계산·정규화 위치는 `ROMS/Utility/rpcg_lanczos.F:365–400`이다.
`px` 계산과 `ADmodVal` 사용 위치는 `ROMS/Utility/congrad.F:687–689`, `ROMS/Utility/congrad.F:989–1007`이다.
이 연결의 출처는 [callflow-da:RF2-032](../../../_staging/recovery/flow/ROMS-callflow-da.md#8-차이-결론)이다.

`rp_main3d`의 impulse 보간 호출 대상은 `ROMS/Tangent/tl_forcing.F:25`이다([callflow-da §2의 Q67-006](../../../_staging/recovery/flow/ROMS-callflow-da.md#2-계산-순서와-직접-호출)).
순압 엔진의 활성 include는 §9의 `rp_step2d_LF_AM3.h`이다(`ROMS/Representer/rp_step2d.F:21`).

## 문서와 코드 차이 (10-14 대조)

출처: [da-representer 대조 보고서](../../../_staging/recovery/compare/roms-da-representer-vs-code.md#5-차이-결론), [theory-numerics 대조 보고서](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md#5-차이-결론).

문서 판: ROMS 위키 wikitext, 2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json). 코드 판: 원본 저장소 HEAD `57aecf58`, 2026-09-18, roms-4.2 이후 4.3 개발.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| da-representer:RT2-366 | Representer의 전체장 변수 | — | `ROMS/Representer/rp_ini_fields.F:3` `#ifdef TL_IOMS`<br>`ROMS/Representer/rp_ini_fields.F:339` `CF(i,0)=CF(i,0)+DC(i,k)*u(i,j,k,nstp)`<br>`ROMS/Representer/rp_ini_fields.F:340` `tl_CF(i,0)=tl_CF(i,0)+tl_DC(i,k)*u(i,j,k,nstp)+             &`<br>`ROMS/Representer/rp_ini_fields.F:341` `&                            DC(i,k)*tl_u(i,j,k,nstp)-             &`<br>`ROMS/Representer/rp_ini_fields.F:342` `#  ifdef TL_IOMS`<br>`ROMS/Representer/rp_ini_fields.F:343` `&                            DC(i,k)*u(i,j,k,nstp)`<br>`ROMS/Representer/rp_ini_fields.F:348` `cff1=1.0_r8/DC(i,0)`<br>`ROMS/Representer/rp_ini_fields.F:349` `tl_cff1=-cff1*cff1*tl_DC(i,0)+                                &`<br>`ROMS/Representer/rp_ini_fields.F:350` `#  ifdef TL_IOMS`<br>`ROMS/Representer/rp_ini_fields.F:351` `&            2.0_r8*cff1`<br>`ROMS/Representer/rp_ini_fields.F:355` `tl_cff2=tl_CF(i,0)*cff1+CF(i,0)*tl_cff1-                      &`<br>`ROMS/Representer/rp_ini_fields.F:356` `#  ifdef TL_IOMS`<br>`ROMS/Representer/rp_ini_fields.F:357` `&            CF(i,0)*cff1`<br>`ROMS/Representer/rp_main3d.F:132` `!  Time-step representers tangent linear 3D primitive equations.` | C 문서 누락 | TL_IOMS의 Representer 변수는 전체장이다. 순수 TLM 증분 변수와 같은 뜻으로 쓰지 않는다. |
| da-representer:RT2-390 | RPM의 순방향 엔진 설명 | `models/ROMS/source-analysis/roms_representer_model.md:71` `` RPM 을 사용하는 상위 드라이버들 (iRPM grep): `Drivers/r4dvar.F`, `Drivers/tl_r4dvar_roms.h`, `Drivers/array_modes.h`, `Drivers/obs_sen_r4dvar_analysis.h`, `Drivers/picard_roms.h`, `Drivers/rp_roms.h`. 즉 RPM 은 R4D-Var(dual/indirect representer) 와 그 진단·민감도 드라이버의 공통 순방향 엔진이다. `` | `ROMS/Drivers/r4dvar.F:906` ` CALL rp_main3d (RunInterval) `<br>`ROMS/Drivers/r4dvar.F:1074` ` CALL ad_main3d (RunInterval) `<br>`ROMS/Drivers/r4dvar.F:1212` ` CALL tl_main3d (RunInterval) `<br>`ROMS/Drivers/r4dvar.F:1694` ` CALL rp_main3d (RunInterval) `<br>`ROMS/Drivers/r4dvar.F:1128` `CALL error_covariance (iTLM, driver, my_outer, my_inner,      &`<br>`ROMS/Drivers/r4dvar.F:1129` `&                           Lbck, Lini, Lold, Lnew,                &`<br>`ROMS/Drivers/r4dvar.F:1130` `&                           Rec1, Rec2, Lposterior)` | C 문서 누락 | RPM은 R4D-Var의 prior·analysis 궤적을 적분한다. inner-loop의 행렬 작용은 ADM·공분산·TLM으로 계산한다. |
| da-representer:RT2-391 | Representer 계수 해법의 근거 | `models/ROMS/source-analysis/roms_representer_model.md:200` <code>dual(observation-space) cost-function 최소화 알고리즘(켤레경사·Lanczos)·representer 계수 해법</code> | `ROMS/Drivers/r4dvar.F:1013` ` CALL congrad (ng, iRPM, my_outer, my_inner, Ninner, Lcgini) `<br>`ROMS/Drivers/r4dvar.F:1259` ` CALL congrad (ng, iRPM, my_outer, my_inner, Ninner, Lcgini) `<br>`ROMS/Utility/congrad.F:24` ` !              (R_n + Cobs) * Beta_n = h_n                             ! `<br>`ROMS/Utility/congrad.F:26` ` !              h_n = Xo - H * X_n                                      ! `<br>`ROMS/Utility/congrad.F:36` ` !              P_n = R_n + Cobs                                        ! `<br>`ROMS/Utility/congrad.F:40` ` !              P_n * PSI = R_n * PSI + Cobs * PSI                      ! ` | C 문서 누락 | 간접 Representer 계수는 congrad에서 `(R_n+Cobs) Beta_n=h_n`을 푼다. 대조 근거는 [da-representer:RT2-365](../../../_staging/recovery/compare/roms-da-representer-vs-code.md#5-차이-결론)와 congrad.F:24·26·36·40이다. [10-14 전수 검증 정정] |
| theory-numerics:RTN-388 | RPM 노트의 2D FB 파일 목록 | models/ROMS/source-analysis/roms_representer_model.md:182 ``\| 2D 엔진 \| `rp_step2d.F` + `rp_step2d_FB.h`/`_LF_AM3.h`/`_FB_LF_AM3.h` \| 순압 모드(FB/LF-AM3 시간계) \|`` | ROMS/Representer/rp_step2d.F:21 `# include "rp_step2d_LF_AM3.h"` | C 문서 누락 | RPM의 실제 step2d include는 rp_step2d_LF_AM3.h이다. |
