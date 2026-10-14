---
title: "ROMS Adjoint Model (ADM) 커널 — ad_* 물리 루틴의 시간 역방향 gradient 역전파"
model: ROMS
component: ROMS/Adjoint
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Adjoint/). ad_main3d.F 역방향 driver 루프, ad_rhs3d.F 의 adjoint RHS 연산 구조(Coriolis 블록 verbatim), ad_step3d_t.F corrector/spline adjoint, ad_pre_step3d.F·ad_prsgrd.F·ad_omega.F·ad_t3dmix.F·ad_uv3dmix.F dispatch 를 file:line 인용; 2026-10-14 ROMS recovery 대조 보고서 반영"
last_source_check: "2026-10-14 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_adjoint_framework.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/README.md
---

# ROMS Adjoint Model (ADM) 커널 — ad_* 물리 루틴

> 개별 ad_ 물리 커널이 NLM 의 forward 연산을 시간 역방향으로 전치(transpose)·역전파하는 구조. (경로: roms/ROMS/Adjoint/)

프레임워크(4D-Var 드라이버·I/O·precondition)는 [roms_adjoint_framework](roms_adjoint_framework.md) 참조. 본 노트는 **개별 ad_ 커널의 adjoint 연산 패턴**과 **driver 의 역방향 호출 순서**에 집중한다.

---

## 1. ADM driver: 시간 역방향 step 루프 (`ad_main3d.F`)

`ad_main3d` 는 "full 3D baroclinic ocean model" 로 구성된 adjoint ROMS 의 메인 드라이버로, `Adjoint/ad_main3d.F:12-15` 에서 그 역할을 명시한다.

> `!  This subroutine is the main driver for adjoint  ROMS when` … `!  backwards the adjoint model equations for all nested grids` (`ad_main3d.F:12-14`)

### 1.1 시간·step 카운터의 역전(reverse)

nesting step 메타데이터(`StepInfo`)는 NLM 저장 순서의 역순으로 읽힌다. `ad_main3d.F:234-237`:

> `!  (step_counter) for each grid. Their values are reversed` / `!  from the saved nonlinear model time stepping sequence.` / … / `itcount=itcount-1             ! count backwards for adjoint`

step 루프 자체가 역방향이다 — `ad_main3d.F:266`:

```
STEP_LOOP : DO istep=Nsteps,1,-1
```

수반 모델은 시간 단계 역순으로 적분한다 (`ROMS/Adjoint/ad_main3d.F:266`).
감도 함수의 수반 forcing은 이 역적분에 입력한다 ([4D-Var 대조 보고서의 DA1-812](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md#4-노트-대조와-수정안)).

`ad_main3d`는 `obs_read` 다음에 `WEAK_CONSTRAINT`이면 `ad_htobs`를 호출한다.
`WEAK_CONSTRAINT`가 없으면 `ad_misfit`을 호출한다 (`ROMS/Adjoint/ad_main3d.F:697,709-714`; [DA 계산 흐름 대조 보고서](../../../_staging/recovery/flow/ROMS-callflow-da.md#6-기존-노트-대조와-수정안)). [10-14 전수 검증 보완]

JEDI 빌드에서는 시간 클럭도 후진한다 (`ad_main3d.F:273-274`): `jic(ng)=jic(ng)-1`, `time4jedi(ng)=time4jedi(ng)-dt(ng)`.

### 1.2 호출 순서: NLM 의 거울상

`ad_main3d` 내 ad_ 커널 호출은 NLM `main3d` 와 **반대 순서**로 배치된다. 대표 호출 시퀀스(`ad_main3d.F` grep):

| 라인 | 호출 | 역할 |
|---|---|---|
| `ad_main3d.F:451` | `CALL ad_step3d_t` | adjoint 트레이서 corrector |
| `ad_main3d.F:476`,`837` | `CALL ad_omega (…iADM)` | adjoint 수직속도 |
| `ad_main3d.F:507` | `CALL ad_step3d_uv` | adjoint 3D 운동량 |
| `ad_main3d.F:529`,`969` | `CALL ad_set_depth (…iADM)` | adjoint 깊이/두께 |
| `ad_main3d.F:595`,`647` | `CALL ad_step2d` | adjoint 순압 2D |
| `ad_main3d.F:771` | `CALL ad_rhs3d` | adjoint RHS |
| `ad_main3d.F:819` | `CALL ad_set_zeta` | adjoint 자유표면 |
| `ad_main3d.F:949` | `CALL ad_rho_eos (…iADM)` | adjoint 상태방정식 |
| `ad_main3d.F:892` | `CALL ad_set_vbc` | adjoint 수직경계조건(플럭스) |

NLM 에서 `rhs3d → step3d_uv → step2d → step3d_t` 순이라면, 여기서는 driver 상단에서 `ad_step3d_t` 가 먼저(`:451`), 하단에서 `ad_rhs3d` 가 나중(`:771`)에 불린다 — adjoint 연쇄규칙(chain rule) 전치 순서.

### 1.3 BASIC STATE 재계산(recompute) 패턴

adjoint 는 비선형 궤적(trajectory, BASIC STATE)에 선형화된다. driver 는 ad_ 호출 직전에 NLM 루틴으로 BASIC STATE 를 재구성한다. `ad_main3d.F:433-453`:

> `!  Compute intermediate BASIC STATE mass fluxes (Huon,Hvom) for use in` / `!  the adjoint horizontal advection (ad_step3d_t) and adjoint vertical` / `!  velocity (ad_omega).` → `CALL reset_massflux (ng, tile, iADM)    ! intermediate` (`:440`)

그리고 `:447-452`:

> `!  Compute basic STATE omega vertical velocity with intermediate mass` / `!  fluxes. Time-step adjoint tracer equations.` → `CALL omega (ng, tile, iADM)   ! BASIC STATE w-velocity` / `CALL ad_step3d_t (ng, tile)`

즉 **비선형 `omega`(접두사 없음) 로 BASIC STATE w 를 만든 뒤 그 위에서 `ad_step3d_t`** 를 돌린다. `ad_step3d_uv` 직전에도 동일(`:506-507`): `CALL omega(…iADM)` 후 `CALL ad_step3d_uv`. `FORWARD_READ`/`JEDI` 빌드에서는 저장된 forward 파일로부터 `set_massflux`/`rho_eos` 를 재계산한다 (`ad_main3d.F:319-335`).

2D 전용 adjoint driver 는 `ad_main2d.F:3-5`: `!  This subroutine is the main driver for adjoint  ROMS  when` / `!  advances backward  the  adjoint model`.

---

## 2. adjoint 코드의 표준 작성 규약 (TLM 전치)

ROMS adjoint 는 손으로 작성한(hand-coded) TLM 의 라인별 전치다. `ad_rhs3d.F` 의 Coriolis 항이 교과서적 예. 비선형/TLM 의 한 forward 문(`!^ tl_…` 주석으로 보존)마다 그 adjoint 가 바로 아래 온다.

### 2.1 패턴 요소

`ad_rhs3d.F:2679-2705` (비-WEC Coriolis, k-level):

```fortran
!^          tl_rv(i,j,k,nrhs)=tl_rv(i,j,k,nrhs)-tl_cff1
!^
            ad_cff1=ad_cff1-ad_rv(i,j,k,nrhs)        ! (a) adjoint 누산
!^          tl_cff1=0.5_r8*(tl_VFe(i,j)+tl_VFe(i,j-1))
!^
            adfac=0.5_r8*ad_cff1                      ! (b) 임시 adfac
            ad_VFe(i,j-1)=ad_VFe(i,j-1)+adfac        ! (c) +=  분배
            ad_VFe(i,j  )=ad_VFe(i,j  )+adfac
            ad_cff1=0.0_r8                            ! (d) 소비 후 0 리셋
```

규약 정리:

| 요소 | 의미 | 근거 |
|---|---|---|
| `!^ tl_…` 주석 | 대응하는 TLM forward 문 (검증용 거울) | `ad_rhs3d.F:2679,2682,2695,2698` |
| `ad_X = ad_X + …` | adjoint 기여 전달은 **누산**(transpose)하며, 전달 후 `ad_cff1`을 0으로 초기화하는 단계도 있다 | `ad_rhs3d.F:2681-2687,2697-2703` |
| `adfac`,`adfac1..5` | 반복 계수 임시저장 (효율·정확성) | 선언 `ad_rhs3d.F:390` |
| `ad_cff = 0.0` | 의존성 소비 후 즉시 0 리셋 (이중 누산 방지) | `ad_rhs3d.F:2687,2703` |
| forward 문 역순 | adjoint 는 NLM 문장 **역순**으로 실행 | `:2679`(rv) → `:2682`(cff1) → 입력항 순 |

BASIC STATE(비선형 궤적) 변수 곱셈은 NLM 값(`u(i,j,k,nrhs)` 등 접두사 없음)을 그대로 쓴다 — `ad_rhs3d.F:2715-2718` 에서 `ad_u(...)=ad_u(...)+adfac` 와 동시에 `ad_cff=ad_cff+(u(...)+u(...))*ad_VFe(i,j)` 로 비선형 계수에 대한 gradient 도 누산.

### 2.2 `ad_rhs3d` 모듈의 adjoint RHS 구성 (역순 dispatch)

`ad_rhs3d.F:12-13`: `!  This subroutine evaluates adjoint right-hand-side terms for` / `!  3D momentum and tracers equations`. 필요한 BASIC STATE 명시 — `ad_rhs3d.F:15-17`:

> `!  BASIC STATE variables needed: Hz, Huon, HVom, u, v, W, uclm, vclm,` / `!                                sustr, svstr, bustr, bvstr`

`ad_rhs3d` 내부 호출은 NLM `rhs3d` 의 **역순**이다 (`ad_rhs3d.F`):

| 라인 | 호출 | NLM 대응(역순 위치) |
|---|---|---|
| `:94` | `ad_uv3dmix4` (UV_VIS4) | 운동량 biharmonic 점성 |
| `:102` | `ad_uv3dmix2` (UV_VIS2) | 운동량 harmonic 점성 |
| `:112` | `ad_rhs3d_tile` | 운동량 RHS 본체 (adv·Coriolis·press) |
| `:182` | `ad_t3drelax` (RPM_RELAXATION) | 트레이서 diffusive relaxation |
| `:192` | `ad_t3dmix4` (TS_DIF4) | 트레이서 biharmonic 혼합 |
| `:200` | `ad_t3dmix2` (TS_DIF2) | 트레이서 harmonic 혼합 |
| `:208` | `ad_prsgrd` | 경압 압력경도 |
| `:215` | `ad_pre_step3d` | 새 시간단계 초기화 (NLM 에선 맨 먼저) |

`ad_pre_step3d` 가 마지막에 불리는 것이 핵심 — NLM 에서 가장 먼저 실행되는 predictor 초기화의 adjoint 이므로 역순에서 끝에 온다. `ad_pre_step3d.F:14-15`: `!  This subroutine initialize computations for new time step of the` / `!  adjoint 3D primitive variables.`

`RPM_RELAXATION` (representer model 안정화)는 outer loop 의 `ad_main3d` 호출에서만 적용 — `ad_rhs3d.F:79-82`: `!  the tangent linear representer` / `!  model 3D momentum by a "diffusive relaxation" to previous Picard` / `!  iteration solution. Only applied in the call to ad_main3d in outer / loop.`

---

## 3. adjoint 트레이서 corrector (`ad_step3d_t.F`)

`ad_step3d_t.F:14-18`:

> `!  This routine time-steps adjoint tracer equations.  Notice that` / `!  advective and diffusive terms are time-stepped differently.` / `!  It applies the corrector time-step for horizontal and vertical` / `!  advection, vertical diffusion, nudging if necessary, and lateral` / `!  boundary conditions.`

제약 — `ad_step3d_t.F:25`: `!  The MPDATA scheme is not supported in the TLM, RPM, and ADM.` 모듈 진입부에서 `#undef AD_SUPPORTED` (`ad_step3d_t.F:2`) 로 미지원 옵션을 차단.

### 3.1 forward 재계산 → adjoint 의 in-place 구조

수직 이류 spline adjoint(`ad_step3d_t.F:1255-1303`): 먼저 BASIC STATE spline 을 정방향으로 재구성한 뒤(`:1263-1295`, 비선형 `t(i,j,k,3,itrc)`·`Hz`·`CF`·`FC` 계산), 곧바로 adjoint 로 전환한다.

> `!  Now the adjoint splines code.` (`ad_step3d_t.F:1297`)

이후 `ad_FC(i,N(ng))=0.0_r8`(`:1302`) 등 boundary adjoint 초기화로 시작. 즉 한 타일·한 k-slab 안에서 **(1) 비선형 trajectory 재계산 → (2) 그 위 adjoint 전파**가 짝을 이룬다. 수평 이류 adjoint 는 scheme 별로 분기 — `ad_step3d_t.F:1861` `HADV_FLUX : IF (ad_Hadvection(itrc,ng)%CENTERED2)` … `:2318` `END IF HADV_FLUX`. 수직 확산은 LU 분해의 adjoint — `:583` `!  LU decomposition and forward substitution.` (forward 재계산) 와 `:661` `!  Adjoint LU decomposition and forward substitution.` 가 대응.

운동량 corrector 는 `ad_step3d_uv.F:13-14`(주석 위치): `!  This subroutine time-steps  the  adjoint  horizontal  momentum`.

---

## 4. 분기 dispatch 커널 (NLM 과 동일한 .h 구조)

NLM 처럼 adjoint 도 컴파일 옵션별 `.h` include 로 알고리즘을 선택한다.

**압력경도** `ad_prsgrd.F:11-12`: `!! This routine computes the adjoint baroclinic hydrostatic pressure / gradient term.` dispatch — `ad_prsgrd.F:16-26`:

| cppdef | include | 알고리즘 |
|---|---|---|
| `PJ_GRADP` | `ad_prsgrd40.h` (`:21`) | Lin (1997)의 finite-volume pressure Jacobian (`ROMS/Adjoint/ad_prsgrd40.h:10-12`) |
| `DJ_GRADPS` | `ad_prsgrd32.h` (`:23`) | spline density Jacobian |
| (default) | `ad_prsgrd31.h` (`:25`) | standard density Jacobian |

**트레이서 수평혼합** `ad_t3dmix.F:14`: `!! This routine computes adjoint horizontal mixing of tracers.` → `ad_t3dmix{2,4}_{s,geo,iso}.h` (`ad_t3dmix.F:20-34`).

**운동량 수평점성** `ad_uv3dmix.F:13`: `!! This routine computes adjoint horizontal viscosity of momentum.` → `ad_uv3dmix{2,4}_{s,geo}.h` (`ad_uv3dmix.F:19-29`).

**수직속도** `ad_omega.F:12`: `!  This routine computes S-coordinate vertical velocity (m^3/s),`. adjoint 사설변수 초기화(`:164` `!  Initialize adjoint private variables.`)와 IO 저장(`:176` `!  Save current adjoint solution for IO purposes.`), 그리고 TLM 일관성 보정의 adjoint — `:350` `!  Adjoint of code added to clear tl_W to be consistent with adjoint.`

---

## 5. NLM / TLM / ADM 대비 요약

| 측면 | NLM (`main3d`) | TLM (`tl_main3d`) | ADM (`ad_main3d`) |
|---|---|---|---|
| 시간 방향 | 정방향 | 정방향 | **역방향** `DO istep=Nsteps,1,-1` (`ad_main3d.F:266`) |
| 커널 호출 순서 | rhs→uv→t | NLM 과 동일 | **역순** (ad_step3d_t 먼저 `:451`, ad_rhs3d 나중 `:771`) |
| 변수 갱신 | 직접 대입 | 직접 대입 | **누산** `ad_X=ad_X+…` (`ad_rhs3d.F:2685`) + `=0` 리셋(`:2687`) |
| trajectory | 자체 생성 | NLM BASIC STATE 필요 | NLM BASIC STATE 재계산 후 전파 (`ad_main3d.F:447-452`) |
| TLM 미러 주석 | 없음 | (forward) | `!^ tl_…` 보존 (`ad_rhs3d.F:2679` 등, 파일당 수백개) |

`!^` 미러 주석 개수(grep `!^`): `ad_rhs3d.F` 727, `ad_step3d_uv.F` 592, `ad_pre_step3d.F` 472, `ad_step3d_t.F` 424 — 각 forward 문에 1:1 adjoint 가 손코딩되어 있음을 시사.

---

## 6. 검증 절차와 순압 dispatch

`SANITY_CHECK`는 접선형 모형과 수반 모형의 지정점 검사를 선택한다 (`Master/roms_kernel.F:142-143`).
표준 입력 `User` 배열로 검사할 변수와 격자점을 지정한다 (`ROMS/Drivers/pert_roms.h:31-39`; [빌드·옵션 대조 보고서의 RBH-1335](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#5-차이-결론)).

순압 2D 수반 알고리즘은 `ad_step2d.F`의 `# include "ad_step2d_LF_AM3.h"`로 선택한다 (`ROMS/Adjoint/ad_step2d.F:20`). [10-14 전수 검증 보완]
`ad_main3d`는 `ad_step2d`를 호출한다 (`ROMS/Adjoint/ad_main3d.F:595`).

수반 드라이버의 인용한 `_NOT_YET` 전처리 분기에서 `USE` 문은 `!!`로 주석 처리되어 있다 (`ROMS/Adjoint/ad_main3d.F:50-58,118-120`). [10-14 전수 검증 정정]

## 문서와 코드 차이 (10-14 대조)

출처는 [생지화학 대조 보고서](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론)의 최종 결론이다.

문서 판은 ROMS 위키 wikitext이다 (2026-05-03 받음; 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json)). 코드 판은 원본 저장소 HEAD `57aecf58`이다 (2026-09-18; roms-4.2 이후 4.3 개발).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| biology:ES-096 | ad_AKT_BAK | `ecosim.in.wiki:306` <code>*Vertical mixing coefficients for biological tracers: [1:&#91;&#91;Variables#NBT\|NBT&#93;&#93;,&#91;&#91;Variables#Ngrids\|Ngrids&#93;&#93;] values expected.</code><br>`ecosim.in.wiki:307` <code>:&lt;div class="box"&gt;       &#91;&#91;Variables#AKT_BAK\|AKT_BAK&#93;&#93; == 61*1.0d-6         ! m&lt;sup&gt;2&lt;/sup&gt;/s&lt;br /&gt;&lt;br /&gt;    &#91;&#91;Variables#ad_AKT_fac\|ad_AKT_fac&#93;&#93; == 61*1.0d0          ! nondimensional&lt;/div&gt;</code><br>`User/External/ecosim.in:552` `    ad_AKT_BAK == 61*1.0d0                       ! nondimensional` | `ROMS/Nonlinear/Biology/ecosim_inp.h:296` `            CASE ('ad_AKT_fac')`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:297` `              Npts=load_r(Nval, Rval, NBT, Ngrids, Rbio)`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:298` `              DO ng=1,Ngrids`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:299` `                DO itrc=1,NBT`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:300` `                  i=idbio(itrc)`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:301` `                  ad_Akt_fac(i,ng)=Rbio(itrc,ng)`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:302` `                  tl_Akt_fac(i,ng)=Rbio(itrc,ng)`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:303` `                END DO` | B 문서 오기 | EcoSim 생물 입력에서 ad_AKT_BAK를 ad_AKT_fac로 고친다. [10-14 전수 검증 보완] |
| biology:CM-097 | 생물 ad_AKT_fac의 FORWARD_MIXING 효과 | `User/External/ecosim.in:1196` `!  ad_AKT_fac     Adjoint-based algorithms vertical mixing, basic state,`<br>`User/External/ecosim.in:1197` `!                   scale factor (nondimensional) for biological tracer`<br>`User/External/ecosim.in:1198` `!                   variables; [1:NBT,1:Ngrids] values are expected. In`<br>`User/External/ecosim.in:1199` `!                   some applications, a smaller/larger values of vertical`<br>`User/External/ecosim.in:1200` `!                   mixing are necessary for stability. It is only used`<br>`User/External/ecosim.in:1201` `!                   when FORWARD_MIXING is activated.` | `ROMS/Nonlinear/Biology/ecosim_inp.h:296` `            CASE ('ad_AKT_fac')`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:297` `              Npts=load_r(Nval, Rval, NBT, Ngrids, Rbio)`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:298` `              DO ng=1,Ngrids`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:299` `                DO itrc=1,NBT`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:300` `                  i=idbio(itrc)`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:301` `                  ad_Akt_fac(i,ng)=Rbio(itrc,ng)`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:302` `                  tl_Akt_fac(i,ng)=Rbio(itrc,ng)`<br>`ROMS/Nonlinear/Biology/ecosim_inp.h:303` `                END DO`<br>`ROMS/Adjoint/ad_get_data.F:1480` `#   ifdef FORWARD_MIXING`<br>`ROMS/Adjoint/ad_get_data.F:1481` `!`<br>`ROMS/Adjoint/ad_get_data.F:1482` `!  Read in vertical mixing variables.`<br>`ROMS/Adjoint/ad_get_data.F:1483` `!`<br>`ROMS/Adjoint/ad_get_data.F:1484` `      DO i=1,NAT`<br>`ROMS/Adjoint/ad_get_data.F:1485` `        scale=Fscale(idDiff(i),ng)                    ! save and rescale`<br>`ROMS/Adjoint/ad_get_data.F:1486` `        Fscale(idDiff(i),ng)=ad_Akt_fac(i,ng)`<br>`ROMS/Tangent/tl_get_data.F:1479` `#   ifdef FORWARD_MIXING`<br>`ROMS/Tangent/tl_get_data.F:1480` `!`<br>`ROMS/Tangent/tl_get_data.F:1481` `!  Read in vertical mixing variables.`<br>`ROMS/Tangent/tl_get_data.F:1482` `!`<br>`ROMS/Tangent/tl_get_data.F:1483` `      DO i=1,NAT`<br>`ROMS/Tangent/tl_get_data.F:1484` `        scale=Fscale(idDiff(i),ng)                    ! save and rescale`<br>`ROMS/Tangent/tl_get_data.F:1485` `        Fscale(idDiff(i),ng)=tl_Akt_fac(i,ng)`<br>`ROMS/Representer/rp_get_data.F:1478` `#   ifdef FORWARD_MIXING`<br>`ROMS/Representer/rp_get_data.F:1479` `!`<br>`ROMS/Representer/rp_get_data.F:1480` `!  Read in vertical mixing variables.`<br>`ROMS/Representer/rp_get_data.F:1481` `!`<br>`ROMS/Representer/rp_get_data.F:1482` `      DO i=1,NAT`<br>`ROMS/Representer/rp_get_data.F:1483` `        scale=Fscale(idDiff(i),ng)                    ! save and rescale`<br>`ROMS/Representer/rp_get_data.F:1484` `        Fscale(idDiff(i),ng)=tl_Akt_fac(i,ng)`<br>`316e5450:ROMS/Adjoint/ad_get_data.F:1241` `        Fscale(idDiff(i),ng)=ad_Akt_fac(i,ng)`<br>`316e5450:User/External/ecosim.in:1028` `!  ad_AKT_fac     Adjoint-based algorithms vertical mixing, basic state,`<br>`316e5450:User/External/ecosim.in:1029` `!                   scale factor (nondimensional) for biological tracer`<br>`316e5450:User/External/ecosim.in:1030` `!                   variables; [1:NBT,1:Ngrids] values are expected. In`<br>`316e5450:User/External/ecosim.in:1031` `!                   some applications, a smaller/larger values of vertical`<br>`316e5450:User/External/ecosim.in:1032` `!                   mixing are necessary for stability. It is only used`<br>`316e5450:User/External/ecosim.in:1033` `!                   when FORWARD_MIXING is activated.`<br>`ROMS/Adjoint/ad_step3d_t.F:558` `        DO itrc=1,NT(ng)`<br>`ROMS/Adjoint/ad_step3d_t.F:559` `          ltrc=MIN(NAT,itrc)`<br>`ROMS/Nonlinear/Biology/npzd_Franks_inp.h:156` `            CASE ('ad_AKT_fac')`<br>`ROMS/Nonlinear/Biology/npzd_Franks_inp.h:157` `              Npts=load_r(Nval, Rval, NBT, Ngrids, Rbio)`<br>`ROMS/Nonlinear/Biology/npzd_Franks_inp.h:158` `              DO ng=1,Ngrids`<br>`ROMS/Nonlinear/Biology/npzd_Franks_inp.h:159` `                DO itrc=1,NBT`<br>`ROMS/Nonlinear/Biology/npzd_Franks_inp.h:160` `                  i=idbio(itrc)`<br>`ROMS/Nonlinear/Biology/npzd_Franks_inp.h:161` `                  ad_Akt_fac(i,ng)=Rbio(itrc,ng)`<br>`ROMS/Nonlinear/Biology/npzd_Franks_inp.h:162` `                  tl_Akt_fac(i,ng)=Rbio(itrc,ng)`<br>`ROMS/Adjoint/Biology/ad_biology.F:2` `#if defined ADJOINT && defined BIOLOGY`<br>`ROMS/Adjoint/Biology/ad_biology.F:18` `# elif defined NPZD_FRANKS`<br>`ROMS/Adjoint/Biology/ad_biology.F:19` `#  include <ad_npzd_Franks.h>`<br>`ROMS/Adjoint/ad_get_data.F:1246` `# ifdef FORWARD_READ`<br>`ROMS/Adjoint/ad_get_data.F:1333` `#  ifdef SOLVE3D` | E 코드 결함 후보 (중간) | FORWARD_READ, SOLVE3D, FORWARD_MIXING 경로에서 생물 ad_AKT_fac 입력은 저장되지만 생물 tracer별 배율로 소비되지 않는 결함 후보이다. 근거 강도는 중간이다. |
