---
title: "ROMS 4D-Var · 특수 driver 변종 — 동화/안정성/민감도 driver 카탈로그"
model: ROMS
component: ROMS/Drivers
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Drivers/). nl/ad/tl/rp_roms.h 헤더, i4dvar.F·rbl4dvar.F·r4dvar.F 모듈 phase 주석+PUBLIC 목록, i4dvar/rbl4dvar/r4dvar_roms.h 헤더, fsv/afte/fte/op/hessian_op/hessian_so/so/so_semi_roms.h + 대응 propagator_*.h 헤더, adsen/optobs/correlation/array_modes/pert/picard/symmetry/tlcheck/jedi_roms.h, split_*_roms.h, obs_sen_*_analysis/forecast.h 를 file:line 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_4dvar.md
  - models/ROMS/source-analysis/roms_adjoint_framework.md
  - models/ROMS/README.md
---

# ROMS 4D-Var · 특수 driver 변종 — 동화/안정성/민감도 driver 카탈로그

> ROMS 의 모든 실행 모드는 `Drivers/*.h`(인라인 인클루드) 또는 `Drivers/*.F`(모듈) 한 쌍으로 구현된다. 각 driver 는 동일한 ESMF 3-단계 인터페이스(`ROMS_initialize`/`ROMS_run`/`ROMS_finalize`)를 노출하되, 내부에서 어떤 커널(NLM/TLM/RPM/ADM)을 어떤 순서로 돌리는지로 동화·안정성·민감도 모드를 구분한다. (경로: roms/ROMS/Drivers/)

상위 dispatch(`MyAppCPP` → driver 파일 선택)는 [[roms_main_driver_dispatch]] 가 다룬다. 본 노트는 **각 driver 변종이 어떤 동화/분석 모드를 구현하는지**에 집중한다. 핵심 동화 알고리즘 내부(cost function, B 행렬, observation operator)는 [[roms_4dvar]], adjoint/TL 커널 메커닉은 [[roms_adjoint_framework]] 참조.

## 1. 공통 골격: 4개 기본 커널 driver

모든 driver 는 `MODULE roms_kernel_mod` 로 이름이 같고(인라인 인클루드라 동시 컴파일 안 됨), `ROMS_initialize`/`ROMS_run`/`ROMS_finalize` 를 PUBLIC 으로 노출한다(`nl_roms.h:55-57`).

| 파일 | 커널 | 헤더 주석 |
|---|---|---|
| `nl_roms.h` | 비선형(NLM) | "executes ROMS standard nonlinear model" (`nl_roms.h:10-12`) |
| `ad_roms.h` | 수반(ADM) | "executes ROMS generic adjoint model" (`ad_roms.h:10-12`) |
| `tl_roms.h` | 접선선형(TLM) | "executes ROMS tangent linear model" (`tl_roms.h:10-12`) |
| `rp_roms.h` | representer TLM(RPM) | "executes ROMS representers tangent linear model" (`rp_roms.h:10-12`) |

- `nl_roms.h` 는 `VERIFICATION` cppdef 가 켜지면 `mod_fourdvar`·`stats_modobs` 를 가져와 모델-관측 통계만 산출하는 검증 모드로 동작(`nl_roms.h:25-27`, `nl_roms.h:45-47`).
- RPM(`rp_roms.h`)은 R4D-Var 의 inner-loop 에서 쓰는 "representer 접선선형" 커널 — TLM 과 달리 전체장(full field) 기준으로 선형화된다([[roms_4dvar]] 의 dual formulation).

## 2. 핵심 4D-Var 동화 알고리즘 (3 변종)

ROMS 4D-Var 는 **primal(model space)** 1종 + **dual(observation space)** 2종, 총 3개 알고리즘으로 구성된다. 각각 `*.F` 모듈(논리 phase 분해) + `*_roms.h` driver(phase 호출 오케스트레이션) 쌍.

| 알고리즘 | 공간 | 제약 | 최소화기 | 파일 |
|---|---|---|---|---|
| **I4D-Var** | primal (model space) | strong only (모델 완전 가정) | incremental | `i4dvar.F` + `i4dvar_roms.h` |
| **RBL4D-Var** | dual (obs space) | strong/weak | Restricted B-precond. Lanczos | `rbl4dvar.F` + `rbl4dvar_roms.h` |
| **R4D-Var** | dual (obs space) | strong/weak | indirect representer | `r4dvar.F` + `r4dvar_roms.h` |

- I4D-Var: "primal formulation (model space) strong constraint, incremental 4D-Var where the only errors considered are those for the observations. The model is assumed to be perfect." (`i4dvar_roms.h:13-16`)
- RBL4D-Var: "dual formulation (observation space), strong or weak constraint 4D-Var where errors may be considered in both model and observations" + "Restricted, B-preconditoned Lanczos (W4D-RBLanczos)" (`rbl4dvar_roms.h:10-16`, `rbl4dvar_roms.h:14`). Gurol et al. 2014 (B-preconditioned dual minimization) 추가 인용(`rbl4dvar_roms.h:41-44`).
- R4D-Var: "Indirect Representer Approach (R4D-Var)" dual (`r4dvar_roms.h:11-13`). Weaver-Courtier 류 representer 행렬 기반.
- 세 변종 모두 Moore et al. 2011 Part I/II(`i4dvar_roms.h:25-39` 등)을 표준 인용으로 공유.

### 2.1 알고리즘 phase 분해 (모듈 PUBLIC 목록)

`*.F` 모듈은 알고리즘을 "logical components routines" 로 쪼개 ESM 결합(coupling)·nesting 을 허용한다(`i4dvar.F:13-14`). 각 phase 는 `*_roms.h` driver 의 `ROMS_run` 에서 outer/inner 루프 순서로 호출된다.

**I4D-Var phases** (`i4dvar.F:160-166`):
`background_initialize` → `background` → `increment` → `analysis` → `posterior_analysis_initialize` → `posterior_analysis` → `prior_error`.

헤더 주석의 phase 역할(verbatim 요약):
- `background`: "Timesteps the nonlinear model to compute the basic state Xb(t) ... interpolates the nonlinear model trajectory to the observations locations." (`i4dvar.F:24-29`)
- `increment`: "Minimizes of the 4D-Var cost function over Ninner inner loops iterations to compute the data assimilation increment, dXa." (`i4dvar.F:33-35`) — 실제 inner-loop 최소화 본체(`i4dvar.F:781`).
- `analysis`: 새 초기조건 $X_a = X_b(t{=}0) + dX_a$ 를 NLM INI 파일에 기록(`i4dvar.F:38-44`).
- `posterior_analysis_*`: analysis $X_a$ 로 NLM 재적분해 posterior 상태 산출(`i4dvar.F:40-49`).
- `prior_error`: 사전(prior) 배경오차 공분산 + 정규화 계수 처리(`i4dvar.F:51-54`).

증분 갱신식:

$$X_a = X_b(t{=}0) + dX_a, \qquad dX_a = \arg\min_{dX} J(dX)$$

**RBL4D-Var phases** (`rbl4dvar.F:190-199`):
`background_initialize` → `background` → `increment` → `analysis_initialize` → `analysis` → `prior_error` → `posterior_error`. (I4D-Var 와 달리 `posterior_error` 보유 — weak-constraint 오차 추정.)

**R4D-Var phases** (`r4dvar.F:138-145`):
`background` → `increment` → `analysis` → `prior_error` → `posterior_error`.

## 3. split (다중 실행파일) driver

split 변종은 동일 알고리즘을 **2개 이상 실행파일(A/B)** 로 쪼개, 결합 시스템·nesting·inner-loop 저해상도/저정밀 실행을 허용한다.

| 파일 | 알고리즘 |
|---|---|
| `split_i4dvar_roms.h` | I4D-Var split |
| `split_rbl4dvar_roms.h` | RBL4D-Var split |
| `split_r4dvar_roms.h` | R4D-Var split |

- Executable A: "computes ROMS nonlinear trajectory used to linearize the tangent linear and adjoint models ... allows the nonlinear trajectory to be part of a coupling system and or include nested grids" → `background`/`analysis` 호출(`split_i4dvar_roms.h:18-26`).
- Executable B: `increment`/`posterior_analysis`(I4D) 또는 `increment`/`posterior_error`(RBL/R4D) 호출. "possible to use a coarser grid resolution in the inner loop ... increment phase may be run at a lower precision." (`split_i4dvar_roms.h:29-36`, `split_rbl4dvar_roms.h:21-30`, `split_r4dvar_roms.h:21-30`)

## 4. 관측 민감도 / 영향 (observation impact·sensitivity) driver

4D-Var 동화 자체의 수반(adjoint of the assimilation algorithm)을 취해 **각 관측이 분석 증분에 미친 영향/민감도**를 산출한다.

| 파일 | 모드 |
|---|---|
| `obs_sen_i4dvar_analysis.h` | I4D-Var 관측 민감도 (analysis) |
| `obs_sen_rbl4dvar_analysis.h` | RBL4D-Var 관측 민감도 (analysis) |
| `obs_sen_rbl4dvar_forecast.h` | RBL4D-Var 관측 민감도 (forecast 기간) |
| `obs_sen_r4dvar_analysis.h` | R4D-Var 관측 민감도 (analysis) |
| `array_modes.h` | R4D-Var representer 행렬 array modes / clipping + 관측 민감도 |

- I4D obs_sen: "evaluates the impact of each observation in the 4D-Var analysis increment by measuring their sensitivity over a specified circulation functional index, J ... equivalent to taking the adjoint of the 4D-Var algorithm." (`obs_sen_i4dvar_analysis.h:10-15`). 헤더에 NLM(전·후 기간)·ADM(역적분)·TLM(동화창) 시간선 ASCII 다이어그램 + Lanczos 벡터 $q_i$ 저장 절차(`obs_sen_i4dvar_analysis.h:21-44`).
- obs_sen 일반: "computes the sensitivity of the assimilation system to each observation. It measures the degree to which each observation contributes to the uncertainty in the estimate ... determine the type of measurements that need to be made, where to observe, and when." (`obs_sen_rbl4dvar_analysis.h:18-23`) — 적응형 관측망 설계.
- `array_modes.h`: "computes the array modes of the stabilized representer matrix or clips the analysis by disregarding potentially unphysical array modes." (`array_modes.h:18-20`). Moore et al. 2011 Part III(관측 영향/민감도) 추가 인용(`array_modes.h:46-53`).

## 5. 안정성·민감도 분석 driver (propagator R(0,t) 기반)

NLM 궤적에 대해 선형화한 propagator $R(0,t)$ (TLM)와 그 수반 $R^{T}(t,0)$ (ADM)의 고유/특이 분해를 **ARPACK** reverse-communication 으로 계산한다. driver 는 `propagator_mod` 를 통해 대응 `propagator_*.h` 의 연산자 적용 루틴을 호출. 공통 인용: Moore et al. 2004 (TL/adjoint 종합 시스템).

| driver | 산출물 | propagator | 연산자 |
|---|---|---|---|
| `fte_roms.h` | Finite Time Eigenmodes | `propagator_fte.h` | $R(0,t)\,u$ (TLM 전방 1회) |
| `afte_roms.h` | Adjoint FTE | `propagator_afte.h` | $R^{T}(t,0)\,u$ (ADM 역방 1회) |
| `op_roms.h` | Optimal Perturbations (singular vectors) | `propagator_op.h` | $R^{T}R$ (TLM 전방 → ADM 역방) |
| `hessian_op_roms.h` | Hessian singular vectors | `propagator_hop.h` | $R^{T}R$ + Hessian metric |
| `so_roms.h` | Stochastic Optimals (white noise) | `propagator_so.h` | white-noise forcing SO |
| `hessian_so_roms.h` | Hessian Stochastic Optimals | `propagator_hso.h` | white-noise SO + Hessian metric |
| `so_semi_roms.h` | SO, seminorm estimation | `propagator_so_semi.h` | seminorm 기준 SO 고유벡터 |
| `fsv_roms.h` | Forcing Singular Vectors | `propagator_fsv.h` | 상수 forcing $M(t)$ |

연산자 의미(헤더 주석):
- **FTE/AFTE**: $R(0,t)$ 의 finite time normal modes = 순환의 점근 안정성 측정(`fte_roms.h:12-15`); AFTE 는 transpose, 비정규성(non-normality) 정량화(`afte_roms.h:12-17`). 둘 다 **ESMF super-structure 에서 실행 불가**(`afte_roms.h:25-26`, `fte_roms.h:23-24`).
- **OP / Hessian-OP**: "singular vectors of the propagator R(0,t) which measure the fastest growing of all possible perturbations over a given time interval" — TLM 전방 [0,t] → ADM 역방 [t,0] 1쌍(`op_roms.h:12-16`, `propagator_op.h:12-17`). Hessian 변종은 Smith-Moore-Arango 2015 (Hessian SV 기반 예보오차 공분산) 추가(`propagator_hop.h:25-28`).
- **SO / Hessian-SO**: 백색잡음 강제(white noise forcing)에 대한 stochastic optimals(`propagator_so.h:5`, `propagator_hso.h:5`).
- **SO-semi**: "eigenvectors of the stochastic optimals operator with respect the seminorm of the chosen functional ... influence of stochastic variations (biases) in ocean forcing ... build forecast ensembles." (`so_semi_roms.h:12-19`)
- **FSV**: 시간상수 forcing $f$ 의 특이벡터. $s(t)=M(t)f$, $M(t)=\int_0^t R(t',t)\,dt'$; $M^{T}M$ 의 고유벡터 = forcing singular vectors → 표면강제 계통오차 앙상블 생성(`fsv_roms.h:12-25`). FSV propagator 는 TLM 전방 [0,t] + ADM 역방 [t,0](`propagator_fsv.h:12-17`).

ARPACK 사용 증거(fsv 예시): `which='LM'` (NEV largest eigenvalues), `howmany='A'`, 대칭 연산자에 `pdsaupd` reverse-communication 호출(`fsv_roms.h:283-284`, `fsv_roms.h:346-349`, `fsv_roms.h:414-415`). Lehoucq-Sorensen-Yang 1997 ARPACK user guide 인용(`fsv_roms.h:349`).

$$\text{OP}:\ \max \frac{\|R(0,t)\,u\|^2}{\|u\|^2}\ \Rightarrow\ \text{eig}(R^{T}R)\,;\qquad \text{FSV}:\ \text{eig}(M^{T}M),\ \ M(t)=\int_0^t R(t',t)\,dt'$$

## 6. 수반 민감도 / 최적 관측 driver

| 파일 | 모드 |
|---|---|
| `adsen_roms.h` | Adjoint Sensitivity Analysis |
| `optobs_roms.h` | Optimal Observation |

- `adsen_roms.h`: 함수/지수 $J$ 의 상태변수 $S$ 에 대한 민감도를 ADM 1회 적분으로 산출. "dJ/dS = transpose(R) S ... the sensitivity for ALL variables, parameters, and space-time points can be computed from a single integration of the adjoint model." (`adsen_roms.h:21-26`). Moore et al. 2009 (남캘리포니아 해류 수반 민감도) 인용(`adsen_roms.h:36-39`).

$$dJ = \frac{\partial J}{\partial \zeta}d\zeta + \frac{\partial J}{\partial u}du + \frac{\partial J}{\partial v}dv + \frac{\partial J}{\partial T}dT + \cdots,\qquad \frac{dJ}{dS} = R^{T} S$$

- `optobs_roms.h`: adsen 과 동일한 $dJ/dS = R^{T}S$ 정식(`optobs_roms.h:13-26`)이나 `convolve_mod::error_covariance`·`def_norm_mod::def_norm` 를 사용(`optobs_roms.h:50-52`) — 오차공분산을 적용한 **최적 관측 배치** 산출 모드(헤더 제목 "Optimal Observation Driver", `optobs_roms.h:10`).

## 7. 4D-Var 보조 인프라 / 정합성 테스트 driver

| 파일 | 역할 |
|---|---|
| `correlation.h` | 배경오차 상관(B-error correlation) 모델 빌드·테스트 |
| `symmetry.h` | weak-constraint inner-loop $H R R^{T} H^{T}$ 대칭성 검증 |
| `pert_roms.h` | TL/AD 모델 sanity test (inner-product / sanity check) |
| `tlcheck_roms.h` | TLM 선형화(linearization) 테스트 |
| `picard_roms.h` | RPM Picard 반복 테스트 (R4D-Var inner loop) |

- `correlation.h`: 일반화 확산연산자 기반 B 모델. $B = S C S$, $C = C^{1/2}C^{T/2}$, $C^{1/2}=G L^{1/2} W^{-1/2}$ (G=정규화 계수, L=self-adjoint 확산필터, S=배경오차 표준편차, W=격자셀 면적/체적 대각행렬)(`correlation.h:14-31`). Weaver-Courtier 2001 인용(`correlation.h:43-46`).
- `symmetry.h`: "checks the symmetry of the H R R' H' operator ... R' H' term is computed by integrating the adjoint model backwards while the H R is computed integrating forward the tangent linear model." (`symmetry.h:13-16`). representer 행렬이 대칭이어야 하는 dual 4D-Var 의 일관성 검사.
- `pert_roms.h`: 내부점 섭동 앙상블로 $T - \text{transpose}(A) = 0$ (round-off 내) 확인 — `INNER_PRODUCT` 스위치는 대칭행렬 검사, `SANITY_CHECK` 스위치는 `user(1..8)` 로 지정한 단일점 검사(`pert_roms.h:18-43`).
- `tlcheck_roms.h`: gradient test 유사 구조로 TLM 선형화 검증, `dotproduct_mod::ad_dotproduct` 사용(`tlcheck_roms.h:11-14`, `tlcheck_roms.h:28`).
- `picard_roms.h`: RPM Picard 반복 — $d(S')/dt = N(S_o) + A(S'-S_o)$, $S_o$=직전 TLM 반복해(basic state)(`picard_roms.h:11-16`).

## 8. ROMSJEDI 인터페이스 driver

`jedi_roms.h` — JEDI(Joint Effort for Data-assimilation Integration) 외부 동화 프레임워크 결합용. 3-phase 초기화(`ROMS_initializeP1/P2/P3`) + `ROMS_run`/`ROMS_finalize` 노출(`jedi_roms.h:10-13`). `ad_post_initial_mod` 등 TLM/ADM 후처리 모듈을 cppdef 조건부로 가져옴(`jedi_roms.h:28-31`).

## 9. driver ↔ cppdef ↔ 동화 모드 요약

| driver 파일 | 모드 | 커널 사용 | 비고 |
|---|---|---|---|
| nl/ad/tl/rp_roms.h | 단일 커널 실행 | NLM/ADM/TLM/RPM | §1 |
| i4dvar.F+i4dvar_roms.h | primal strong 4D-Var | NLM+TLM+ADM | §2, operational |
| rbl4dvar.F+rbl4dvar_roms.h | dual strong/weak (Lanczos) | NLM+TLM+ADM | §2 |
| r4dvar.F+r4dvar_roms.h | dual strong/weak (representer) | NLM+RPM+ADM | §2 |
| split_*_roms.h | 위 3종의 다중실행파일 분할 | 동일 | §3 |
| obs_sen_*_analysis/forecast.h | 관측 영향/민감도 | 동화 adjoint | §4 |
| array_modes.h | representer array modes/clipping | RPM+ADM | §4 |
| fte/afte/op/hessian_op/so/hessian_so/so_semi/fsv_roms.h | 안정성·SV·SO 분석 | TLM±ADM + ARPACK | §5 |
| adsen/optobs_roms.h | 수반 민감도 / 최적관측 | ADM | §6 |
| correlation/symmetry/pert/tlcheck/picard_roms.h | B 모델·정합성 테스트 | 다양 | §7 |
| jedi_roms.h | ROMSJEDI 결합 | 외부 동화 | §8 |

## 미확인 / source-needed

- `rbl4dvar.F`/`r4dvar.F` 의 increment 루틴 내부 Lanczos/MINRES 수치 세부(반복 행렬연산 라인)는 본 노트에서 미추적 — 필요 시 `i4dvar.F:781` (increment 본체) 및 각 모듈 increment 라인 직접 분석 필요. **source-needed**.
- `propagator_*.h` 의 정규화(weight)·내적 정의 세부 라인은 헤더 주석 범위로만 인용, 본문 알고리즘 라인 미추적. **source-needed**.
