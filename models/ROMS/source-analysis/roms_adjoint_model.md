---
title: "ROMS Adjoint Model (ADM) 커널 — ad_* 물리 루틴의 시간 역방향 gradient 역전파"
model: ROMS
component: ROMS/Adjoint
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Adjoint/). ad_main3d.F 역방향 driver 루프, ad_rhs3d.F 의 adjoint RHS 연산 구조(Coriolis 블록 verbatim), ad_step3d_t.F corrector/spline adjoint, ad_pre_step3d.F·ad_prsgrd.F·ad_omega.F·ad_t3dmix.F·ad_uv3dmix.F dispatch 를 file:line 인용"
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

프레임워크(4D-Var 드라이버·I/O·precondition)는 [[roms_adjoint_framework]] 참조. 본 노트는 **개별 ad_ 커널의 adjoint 연산 패턴**과 **driver 의 역방향 호출 순서**에 집중한다.

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
| `ad_X = ad_X + …` | adjoint 변수는 **항상 누산**(transpose) | `ad_rhs3d.F:2685-2686,2701-2702` |
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
| `PJ_GRADP` | `ad_prsgrd40.h` (`:21`) | Jacobian density (4th-order 계열) |
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

## 6. 미확인 / 후속

- **adjoint 정확성 검증**(dot-product / gradient test) 루틴 위치 — source-needed (본 노트는 커널 연산 구조에 한정; 검증 드라이버는 `Drivers/` 또는 [[roms_adjoint_framework]] 영역으로 추정).
- `ad_step2d_FB.h` / `ad_step2d_LF_AM3.h` 등 순압 2D adjoint 알고리즘 상세는 미독(파일 크기 173KB~213KB). dispatch 는 `ad_step2d.F` 경유 (`ad_main3d.F:595` 호출 확인).
- WEC(`WEC_NOT_YET`)·BBL·bulk_flux adjoint 는 driver 에서 다수 `_NOT_YET` 가드로 비활성(`ad_main3d.F:50-58,118` 등) — adjoint 미완 영역.
