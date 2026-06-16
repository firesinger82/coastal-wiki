---
title: "Delft3D WAQ 수치 커널 — advection-diffusion-reaction 적분 스킴 디스패처·explicit 도함수·process flux→deriv"
model: Delft3D
component: waq/waq_kernel(integration·reactions·calculation)
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/waq/waq_kernel/kernel/...). integration_schemes.f90 의 intsrt select case 디스패처(L176-238), integration/integration_scheme_1.f90 의 explicit 시간루프(L167-363), integration/calculate_transport_with_explicit_derivatives.f90 의 upwind advection-diffusion(L110-253), calculation/update_concentration.f90 의 Euler 적분(L41-113), reactions/calculate_processes.f90 의 process 루프+OpenMP(L44-535)·set_explicit_time_step_for_derivatives(L1032-1097), reactions/prodr2.f90 의 flux→deriv 변환(L31-101), integration/theta_calculation.f90 의 self-adjusting theta(L38-128), integration/flux_corrected_transport.f90·gmres_solver.f90·scale_derivatives.f90 헤더 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
---

# Delft3D WAQ 수치 커널 — advection-diffusion-reaction 적분

> 경로: `src/engines_gpl/waq/waq_kernel/kernel/` (실제 트리는 `waq/waq_kernel/kernel`, 프롬프트의 `packages/waq_kernel/src/...` 경로는 존재하지 않음). DELWAQ 수질 엔진의 수치 적분 핵심: 적분 스킴 디스패처(`integration_schemes.f90`), 적분 스킴 본체(`integration/`), 반응(process) flux 계산(`reactions/`), 보조 계산(`calculation/`). 하천/연안 수질의 지배방정식은 substance 별 advection-diffusion-reaction 이며, DELWAQ 는 이를 **유한체적(finite volume) — segment(cell) + exchange(interface)** 위상으로 푼다.

관련 기존 노트: 수질 전반 구조는 [[delft3d_delwaq]], 수송 일반론은 [[delft3d_dflowfm_kernel_scheme]] 참조. 이 노트는 **waq_kernel 의 적분/반응 수치커널** 에 집중.

## 1. 자료구조 위상 (segment / exchange)

DELWAQ 의 격자 추상화는 비구조적이다. 단언 근거는 `calculate_transport_with_explicit_derivatives.f90` 의 인수 선언:

- `conc(num_substances_total, num_cells)` — 직전 시간층 농도. cell = 계산 segment (`calculate_transport_with_explicit_derivatives.f90:78`)
- `ipoint(4, num_exchanges)` — 각 exchange(interface)의 `From, to, from-1, to+1 volume numbers` (`:72`). 음수 인덱스는 open boundary 를 가리킴(아래 §3.2)
- `flow(num_exchanges)` — exchange 면을 통한 유량 m³/s (`:70`), `area(num_exchanges)` — 면적 m² (`:69`)
- `disp(3)` — 3 방향 고정 분산계수 (`:66`); substance 별 추가 분산은 `disper(num_dispersion_arrays, num_exchanges)` (`:67`)
- exchange 는 방향별로 분할: `num_exchanges_u_dir`(1방향), `num_exchanges_v_dir`(2방향), `num_exchanges_z_dir`(연직), bottom 방향. `noq12 = num_exchanges_u_dir + num_exchanges_v_dir` 가 수평 exchange 개수(`:111`)

핵심: 수치커널은 segment/exchange 위상만 알고 격자 기하는 모름 — 전처리(DELWAQ1)가 만든 `delwaq03.wrk` 파일에서 차원을 읽어 부트(`integration_schemes.f90:120-146`).

## 2. 적분 스킴 디스패처 (`integration_schemes.f90`)

`module integration_schemes` 헤더 주석 (verbatim, `integration_schemes.f90:25-27`):
> `Module integration_schemes:` / `- Encapsulate the interface of run_integration_schemes and initialize_all_conditions:` / `A, J and C are now pointers to real, integer and character arrays, respectively.`

`run_integration_schemes` 는 `intsrt` (integration option 번호)로 `select case` 분기 (`integration_schemes.f90:176-238`). A=real workspace, J=integer, C=character 의 단일 거대 버퍼(`waq_data_buffer`)에 모든 배열을 오프셋 인덱스(`ivol`, `iconc`, `iflow`, `iderv` 등)로 슬라이싱해 전달하는 옛 DELWAQ 메모리 모델.

### 2.1 integration scheme 번호 → 스킴 매핑 표

| `intsrt` | 호출 서브루틴 (`integration_schemes.f90` 라인) | 디스패처 주석상 의미 |
|---|---|---|
| 0 | `scheme_0_no_transport` (`:180`) | 수송 없음, process 만 (`:179` "not transport, just processes") |
| 1 | `scheme_1_time_explicit_space_backward` (`:183`) | 공간·시간 후방(upwind) explicit (`:182`) |
| 2,3,4 | 제거됨 → `goto 991` (`:184-185`) | removed |
| 5 | `scheme_5_time_explicit_flux_corrected_transport` (`:187`) | Flux corrected transport (`:186`) |
| 6–10 | 제거됨 (`:188-189`) | removed |
| 11 | `scheme_11_time_explicit_forester_hz_upwind_vl_central` (`:191`) | 수평 explicit upwind + 연직 implicit central (`:190`) |
| 12 | `scheme_12_..._flux_corrected_transport` (`:194`) | 수평 explicit FCT + 연직 implicit central (`:193`) |
| 13 | `scheme_13_time_explicit_space_upwind` (`:197`) | 수평 explicit upwind + 연직 implicit upwind (`:196`) |
| 14 | `scheme_14_..._flux_corrected_transport` (`:200`) | 수평 explicit FCT + 연직 implicit upwind (`:199`) |
| 15 | `scheme_15_time_implicit_hz_upwind` (`:203`) | GMRES, 수평 upwind, 연직 upwind (`:202`) |
| 16 | `scheme_16_time_implicit_hz_upwind_vl_central` (`:206`) | GMRES, 수평 upwind, 연직 central (`:205`) |
| 17 | `scheme_17_steady_state_hz_upwind_vl_upwind` (`:209`) | 정상상태 GMRES, 수평 upwind, 연직 upwind (`:208`) |
| 18 | `scheme_18_steady_state_hz_upwind_vl_central` (`:212`) | 정상상태 GMRES, 수평 upwind, 연직 central (`:211`) |
| 19,20 | 제거됨 (`:214-215`) | removed |
| 21 | `scheme_21_22_time_implicit_adaptive_theta_hz_upwind_vl_central` (`:218`) | self-adjusting theta (limiter Salezac) (`:217`) |
| 22 | (동일 서브루틴 `:221`) | self-adjusting theta (limiter Boris and Book) (`:220`) |
| 23 | `scheme_23_time_explicit_leonards_quickest` (`:224`) | Leonard's QUICKEST (`:223`) |
| 24 | `scheme_24_adaptive_time_step_flux_corrected_transport` (`:227`) | Leonard Postma 의 local flexible time step (`:226`) |
| 25 | `scheme_25_emission_time_explicit_space_upwind` (`:230`) | emission module 전용 (`:229`) |
| 26 | `scheme_26_adaptive_time_step_fractional_step` (`:233`) | emission module 전용 (`:232`) |

`case default` (미정의 번호) → `goto 990` "INTEGRATION OPTION NOT IMPLEMENTED" (`:235-236`, 252-253). 제거된 번호는 "INTEGRATION OPTION REMOVED" (`:254-255`).

스킴 분류 정리:
- **explicit (수평·연직 모두 명시적)**: 1, 5(FCT), 23(QUICKEST)
- **부분 implicit (수평 explicit + 연직 implicit)**: 11–14
- **완전 implicit (GMRES 반복해법)**: 15–18 (17·18 은 정상상태)
- **self-adjusting θ-방법**: 21, 22 (limiter 만 다름)
- **local adaptive time step**: 24, 26
- **emission 전용**: 25, 26

## 3. explicit 시간루프 표준형 (`integration_scheme_1.f90`)

스킴 1(`scheme_1_time_explicit_space_backward`) 헤더 주석 (verbatim, `integration_scheme_1.f90:52-55`):
> `First order upwind in space and time (1)` / `It performs first order explicit time integration using` / `upwind discretization in space. The method is explict` / `so it has a time-step stability constraint.`

이 루틴이 explicit 스킴들의 **시간루프 골격 표준형**이다. `ACTION` 인수로 4 모드 분기 (`m_actions`): INITIALISATION / SINGLESTEP / FINALISATION / FULLCOMPUTATION (`:97-163`). 한 시간스텝의 호출 순서 (`integration_scheme_1.f90:167-363`, label `10`~`goto 10` 루프):

1. **dry cell 처리** — `set_dry_cells_to_zero_and_update_volumes` (`:174`), 표면적 설정 `set_horizontal_surface_area` (`:172`)
2. **연직 분산길이** `set_vertical_dispersion_length` (`:179`)
3. **변수 grid 설정** `initialize_variables` (`:186`)
4. **입자추적 back-coupling** `delpar01` (`:193`) — PART 모듈 연계
5. **process(반응) 도함수** `calculate_processes` (`:199-217`) — §4
6. **개경계 BC** Thatcher-Harleman `thatcher_harleman_bc` (`:230`), OpenDA 보정 선택 (`:222-229`)
7. **출력** `write_output` (`:235`)
8. **process deriv 스케일링** `scale_processes_derivs_and_update_balances` (`:273`) — §4.3
9. **신규 volume 산정** — `ivflag` 분기 (`:280-306`): case 1 computed volume / case 2 "fraudulent computation option" / default 파일에서 읽기
10. **waste load 추가** `add_waste_loads` (`:313`)
11. **수송 도함수** `calculate_transport_with_explicit_derivatives` (`:323`) — §3.1
12. **시간의존 외력 갱신** `update_time_dependent_external_forcing` (`:332`)
13. **explicit Euler 적분** `update_concs_explicit_time_step` (`:343`) — §3.3
14. **closure error 보정** `calculate_closure_error_correction` (`:348-354`)
15. **dump area flux 적분** `integrate_fluxes_for_dump_areas` (`:357-360`)

시간 전진: `itime = itime + idt` (`integration_scheme_1.f90:279`), 종료조건 `itime >= itstop` (`:270`). NSTEP=(ITSTOP-ITSTRT)/IDT (`:109`).

### 3.1 upwind advection-diffusion 도함수 (`calculate_transport_with_explicit_derivatives.f90`)

이 루틴이 수치커널의 **물리적 심장**이다. 헤더 주석 (verbatim, `:34-48`):
> `Calculates transport with explicit derivatives for the advection diffusion equation.` / `Besides the (main) water flow in the array FLOW(num_exchanges), there are optional additional velocities.` / `These options are often used in the vertical for settling velocities of particulates or floating velocities of blue-green algae.`

exchange 루프(`:112-253`) 내부 한 면당:

- **분산항** `e = disp(방향)`, 길이 `al` → `dl = a/al` → `e = e*dl` (m³/s) (`:131-150`). 연직 bed 구역(`iq > noq12+num_exchanges_z_dir`)은 `e=0` (`:141`)
- substance 별 합성 분산/유속: `d = e + disper(idpnt,iq)*dl`, `v = q + velo(ivpnt,iq)*a` (`:156-159`)
- **1차 upwind 차분** (정규 case, `:162-166`):
  - $v>0$: `dq = (v+d)·conc(from) − d·conc(to)`
  - $v\le 0$: `dq = (v−d)·conc(to) + d·conc(from)`
  - 즉 $\mathrm{dq} = v\,c_{\text{up}} + d\,(c_{\text{from}} - c_{\text{to}})$ (이류=upwind, 확산=중심)
- 도함수 누적: `deriv(from) −= dq`, `deriv(to) += dq` (`:167-168`) — 보존형(conservative). 한 면의 flux 가 from 에서 빠지고 to 로 들어감
- **mass balance** 누적: `dmpq(ipb,1/2)` (유입/유출 분리, `:171-177`), 경계는 `amass2(.,4/5)` (`:200-213`)

경계 처리 2 분기:
- `ifrom<0` (from 이 경계) → label 20 (`:182-215`): `bound(-ifrom)` 사용
- `ito<0` (to 가 경계) → label 40 (`:218-250`): `bound(-ito)` 사용

`integration_id` 비트 옵션 (`:80-82` 주석): bit0=무유량시 무분산(thin dam), bit1=경계 횡단 무분산, bit3=mass balance 출력. `if (btest(integration_id,0) .and. abs(q)<1e-25) cycle` (`:122`).

**`_special` 변형** (`:273-466`): emission module(스킴 25)용. 동일 구조이나 `dq = v` 로 단순화 (총 flux = 해당 substance 유량, `:385,411,443` — 농도 가중 없음, upwind/확산 미적용).

### 3.2 boundary: Thatcher-Harleman

`scheme_1` 은 신규 경계농도 산정 시 OpenDA 버퍼 우선 적용 후 `thatcher_harleman_bc(a(ibset),a(ibsav),...)` 호출 (`integration_scheme_1.f90:222-231`). T-H 는 유입/유출 전환 시 경계농도의 시간이력 완화(return time)를 적용하는 표준 estuarine BC.

### 3.3 explicit Euler 적분 (`update_concentration.f90`)

`update_concs_explicit_time_step` 헤더 주석 (verbatim, `update_concentration.f90:35-40`):
> `Updates concentrations after a time-step explicitly integrated` / `- the mass array is increased with the deriv array * idt.` / `- the deriv array is set to zero.` / `- if applicable, computed volumes are evaluated.` / `- the concentrations of water bound substances are mass/volume` / `- the concentrations of bed susbtances are mass / surface`

핵심 연산 (배열 전체 연산):
```
amass = amass + idt * deriv   ! (update_concentration.f90:72)
deriv = 0.0                    ! (:73)
```
이후 cell 루프(`:76-105`):
- `ivflag==1` 이면 volume = `amass(1,cell)` (computed volume) (`:78`)
- 수송 substance: `conc = amass/vol` (`:94`)
- passive(bed) substance: `conc = amass/surf` (`:101`) — 단위가 면적당 질량
- 0 volume 보호: `abs(vol)<1e-25` 이면 1.0 가정 + 최대 25 회 경고 후 억제 (`:80-90,110-111`)

**`integrate_derivatives_explicitly`** (`:122-188`, 동일 module): 결과를 AMASS 가 아닌 **CONC 에 저장**해 후속 implicit step 을 가능케 하는 변형. 헤더 주석 (verbatim, `:115-121`):
> `Sets an explicit time step from DERIV.` / `This routine deviates from update_concs_explicit_time_step in the sense that the resulting masses are stored in CONC rather than in AMASS to allow for an implicit step.` / `DERIV is set to the new diagonal. This procedure is required for the old ADI solver (nr. 4) and for the 2 solvers with implicit vertical (nrs. 11 & 12)`

즉 부분 implicit 스킴(11,12)은 explicit predictor 후 deriv 에 신규 대각(volume)을 넣어 implicit corrector 로 넘긴다 (`:170` `deriv(i,cell)=vol`).

## 4. 반응(process) 커널 (`reactions/calculate_processes.f90`)

`module m_process_calculation` 의 `calculate_processes` 헤더 주석 (verbatim, `calculate_processes.f90:39-43`):
> `Process sub-system of DELWAQ water-quality modelling system.` / `Routine deals with:` / `- Processes that act on different spatial grids (important application is layered bed)` / `- Processes that act with coarser time steps (notably the Bloom algal growth model).` / `- Paralellisation of the different processes on shared memory multi core machines.`

### 4.1 process → flux → derivative 파이프라인

자료흐름은 3 단계:
1. **process 평가** → `flux(noflux, num_cells, num_grids)` (process 모듈별 flux 산출). process 루프(`:463-520`)에서 process 마다 `procal(...)` 호출(`:870` 부근, `update_a_proc` 내부)로 process number `promnr(iproc)` 에 해당하는 커널을 실행해 flux 배열을 채움.
2. **stoichiometry 적용** flux → deriv: `prodr2` (`:369`, §4.2)
3. **deriv → mass 적분**: `set_explicit_time_step_for_derivatives` (`:398, 563`, §4.3)

`flux = 0.0` 으로 초기화(`:326, 455`) 후 OpenMP 병렬 루프로 process 들을 평가.

### 4.2 stoichiometry: flux→deriv (`prodr2.f90`)

`PRODR2` (`prodr2.f90:31-101`) 가 process flux 를 substance 도함수로 변환하는 핵심:
```
DERIV(substance_i, cell_i) += FLUX(IFLUX, cell_i) * VOLUME(cell_i) * FACT   (prodr2.f90:85-91)
```
여기서 `ST = STOCHI(substance_i, IFLUX)` 화학량론 계수(`:80`), `FACT = FDT * ST`, `FDT = NDT`(fractional step 내 시간스텝 수, `:77`). `ST/=0` 인 항만 계산(`:81`). 즉
$$\frac{d(\text{mass}_s)}{dt}\bigg|_{\text{reaction}} = \sum_{f} \nu_{s,f}\, J_f \, V$$
($\nu$=stoichiometry, $J_f$=flux per unit volume, $V$=segment volume). flux 는 농도/시간 단위, volume 곱으로 질량/시간 변환.

### 4.3 process deriv 스케일 + Euler 적분

`set_explicit_time_step_for_derivatives` (`calculate_processes.f90:1032-1097`): water substance 는 `amass += idt*deriv`, bed substance 는 `conc = amass/max(tiny,surfac)` (`:1086-1087`).

`scale_processes_derivs_and_update_balances` (`scale_derivatives.f90:37-`) 헤더 주석 (verbatim, `scale_derivatives.f90:35-36`):
> `Uses numerically calculated derivatives for balance arrays` / `after scaling them to same dt as the transport`

process 의 시간스텝이 수송과 다를 수 있어(`itfact` = ratio Δt_process/Δt_transport, `:50`) `atfac=1/itfact` 로 deriv 를 수송 Δt 에 맞춰 재스케일하고, `iaflag==1` 이면 `amass2(:,2)` 에 process 질량변화를 누적(`scale_derivatives.f90:60-66`).

### 4.4 병렬화 (OpenMP)

process 루프(`calculate_processes.f90:463-520`)는 OpenMP. `if (omp_get_max_threads() > 1) timon = .false.` (`:460`) — 멀티스레드 시 타이머 비활성. process 간 의존(`done` 플래그)은 `!$omp flush(done)` 로 동기화(`:483, 512`). 도함수/flux dump 갱신은 병렬영역 **밖**에서 일괄(`:523-527` 주석 "Now update the derivatives and the dumps of the fluxes from all processes together outside of the parallel region", `update_derivaties_and_dump_fluxes` `:525`).

### 4.5 multi-grid 와 BLOOM fractional step

- **다중격자**: process 가 서로 다른 grid(예: layered bed)에서 작동 가능. 상위 grid deriv 는 `aggregate(...)` 로 base grid 로 변환 후 상위 grid deriv 영점화(`calculate_processes.f90:383-390, 535-546`).
- **BLOOM** 조류성장 모듈은 별도 fractional step(`:278` 주석 "BLOOM fractional step (derivs assumed zero at entry)", `:341-404`)으로 더 큰 시간스텝(`prondt(bloom_status_ind)`)에 처리.

### 4.6 additional velocity/dispersion 생성

`provel` (`calculate_processes.f90:578-585`): process 가 계산한 추가 velocity(`velonw`)·dispersion(`dispnw`) 배열을 채움. 이 배열이 §3.1 의 `velo`/`disper` 로 수송에 환류 — settling velocity(침강), 조류 부상속도 등 process↔transport 결합 경로.

## 5. implicit / 고급 스킴 보조 루틴 (`integration/`)

### 5.1 GMRES (`gmres_solver.f90`) — 스킴 15–18

`module` 헤더 주석 (verbatim, `gmres_solver.f90:24-25`):
> `The Generalized Minimal Residual (GMRES) method is an iterative solver for nonsymmetric linear systems, and its implementation often relies on BLAS and LAPACK routines for efficient performance.`

`sgmres` 헤더 주석 (verbatim, `gmres_solver.f90:38-46`):
> `Solver for Generalized Minimal Residual (GMRES)` / `The solver preconditions with the gmres_pre_conditioner routine either:` / `- none / - upper triangular matrix / - lower triangular matrix / - both (this is the default preconditioner)` / `- constructs an orthonormal set of approximation vectors (Krylov space)` / `- if no convergence at end of Krilov space, solver restarts` / `- if no convergence at maxiter the solver stops`

`sgmres(ntrace, rhs, sol, restrt, work, ldw, hess, ldh, maxit, tol, ...)` (`gmres_solver.f90:47-`): substance 1 개당 1 선형계, `restrt`=Krylov 부분공간 크기, `tol`=수렴기준, sparse 행렬은 `amat(fast_solver_arr_size)`(off-diagonal)+`diag(ntrace)`+`idiag`(대각 위치) 형식(`:64-69`). `iexseg(ntrace)` 가 0 이면 explicit volume(self-adjusting θ 와 연계, §5.3). 정밀도는 `dp`(double).

### 5.2 Flux Corrected Transport (`flux_corrected_transport.f90`) — 스킴 5,12,14,24

`first_step_fct` 헤더 주석 (verbatim, `flux_corrected_transport.f90:35-43`):
> `Calculates first step of Flux Corrected Transport (FCT) scheme` / `Makes derivatives, upwind in space, advection only, for first step of FCT` / `First step of FCT consists of first order, upwind, monotonous, advection step, with numerical diffusion. In the correction step an anti diffusion is computed, to arrive at 2nd order Lax Wendroff, if no artificial minima and maxima are generated, otherwise the flux limiter will become active.` / `The desired diffusion is subtracted from the anti diffusion in the correction step if a positive diffusion remains, then no correction takes place, if a negative diffusion remains, it is applied to the degree possible.`

1단계는 advection-only upwind(`flux_corrected_transport.f90:92-102`): `dq = v·conc(upwind)`, 확산항 없음. 보정단계에서 anti-diffusion 으로 2차 Lax-Wendroff 에 접근하되 flux limiter 로 monotonicity 보장. 즉 **1차 upwind(예측) + anti-diffusion 보정(limiter) = 비진동 2차 정확도**.

### 5.3 self-adjusting theta (`theta_calculation.f90`) — 스킴 21,22

`calculate_theta` 헤더 주석 (verbatim, `theta_calculation.f90:35-37`):
> `Compute the values for theta` / `The calculation is limited to horizontal directions.` / `For the vertical direction it is almost always theta= 1.0 so it is assumed to be that.`

cell 별 국소 θ 계산 (`theta_calculation.f90:78-101`):
- segment 의 유출합 `thetaseg = Σ max(0,flow) + disp` (`:80-85`)
- 국소 θ: `thetaseg = max(0, 1 − volold/(idt·thetaseg))` (`:89`) — Courant 수 기반. CFL 만족(작은 유출/큰 volume)이면 θ→0(explicit), 위반이면 θ↑(implicit)
- edge θ = 인접 두 cell θ 의 max (`:97`)
- antidiffusion=false(기본)면 θ≥0.5 강제 (`:104-108`)
- `iexseg(cell)`: θ<1e-25 이면 0(explicit), 아니면 1(implicit) (`:117-125`) → GMRES(§5.1) 의 explicit cell 마스크로 전달

연직은 거의 항상 θ=1.0(완전 implicit) 가정 (`:74-76`). 즉 21/22 는 **공간적으로 explicit/implicit 를 혼합**하는 적응형 θ-방법 (22 는 limiter 만 Boris-Book, 21 은 Salezac — 동일 서브루틴, §2.1).

### 5.4 adaptive local time step (`adaptive_time_step.f90`) — 스킴 24,26

`adaptive_time_step.f90` 헤더 주석 (verbatim, `:31-38`):
> `Self-adjusting time-step method.` / `() Per time step it is determined what time step should be set for which computational cell.` / `Each cell is assigned the box number of the time step that it should use.` / `() A separate procedure is applied for flooding cells, since they can have both an inflow and an outflow, but may not yet have realistic concentrations. This procedure steps with the highest necessary frequency.` / `() Per box the following steps are set:` / `- The horizontal advective transport is set in the mass array with appropriate time step.`

cell 별로 "box 번호"(시간스텝 등급)를 할당해 국소적으로 다른 Δt 를 적용 — Leonard Postma 의 local flexible time step (§2.1, 스킴 24).

## 6. mass balance 와 보존성

- exchange flux 는 항상 from −= dq / to += dq 의 보존형 누적 (§3.1, `calculate_transport_with_explicit_derivatives.f90:167-168`) → 내부적으로 질량 보존
- 전역 mass balance: `amass2(num_substances_total, 5)` — 매 시간스텝 monitoring file 헤더로 출력 (`calculate_transport_with_explicit_derivatives.f90:44-46` 주석). column 4/5 = 경계 유입/유출 (`:200-213, 236-249`)
- 상세(dump area) balance: `dmpq(num_substances_transported, ndmpq, 2)` — `iqdmp` 가 exchange→dump 위치를 매핑, [.,1]=유입 / [.,2]=유출 (`:88-90, 171-177`)
- closure error 보정: rewind+steady record 시 `calculate_closure_error_correction` 로 volume 불일치 보정(`integration_scheme_1.f90:348-349`)
- 정상상태/implicit balance: `mass_balance_calculation.f90` 에 `calculate_mass_balance_steady_state`(`:38`), `calculate_mass_balance_space_central_difference`(`:239`), implicit 버전(`:446-447`) 의 3 변형 존재 (각 헤더 주석 인용)

## 7. 정리 — 수치커널 데이터 플로우

```
[DELWAQ1 전처리] → delwaq03.wrk (차원·포인터)
        ↓ boot (integration_schemes.f90:120-161)
run_integration_schemes  --select case(intsrt)-->  scheme_N (§2.1 표)
        ↓ (스킴 1 예시, 시간루프 integration_scheme_1.f90:167-363)
  calculate_processes ──prodr2──> deriv(반응)     ……… reactions/ §4
  calculate_transport_with_explicit_derivatives ──> deriv(수송, upwind A-D)  … integration/ §3.1
  scale_processes_derivs_and_update_balances (Δt 정합)                       … calculation/ §4.3
  update_concs_explicit_time_step:  amass += idt*deriv ; conc=amass/vol      … calculation/ §3.3
  (implicit 스킴: integrate_derivatives_explicitly → sgmres GMRES)           … integration/ §5.1
        ↓
  mass balance (amass2, dmpq) → monitoring/dump output
```

## 8. 미확인 / source-needed

- `procal` (process 커널 실행 디스패처) 본체는 `waq_process`/`waq_proc_preprocess` 패키지에 있을 것으로 보이나 본 검수 범위(`waq_kernel/kernel`) 밖 — **source-needed**
- 스킴 16/17/18/23/24/26 의 시간루프 본체 세부(scheme_16_utils, scheme_23_utils 등)는 헤더·디스패처 매핑만 확인, 본체 라인별 미검수 — **source-needed**
- `double_sweep_solver.f90`(tridiagonal 연직 solver 추정)·`vertical_forester_filter.f90`(Forester 필터, 스킴 11) 본체 미검수 — **source-needed**
- `initialize_pointer_matrices_fast_solver.f90`(GMRES sparse 행렬 구성) 미검수 — **source-needed**
