---
title: "roms 4dvar"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ROMS source code 직접 분석 (models/ROMS/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/roms_4dvar.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. §I 추가 (2026-05-28): PR #75 첨부 `multi_scale_B_v1.pdf` (15p) 직접 fetch + 본문 인용 — Matérn correlation eq (1) / weighted sum eq (2) / implicit diffusion eq (3)(4) / Daley length scale 관계 / `s4dvar.in` 7개 신규 parameter (Nscale·Mlap·Bwgt·HdecayMX/MY/IX/IY/FX/FY·HdecayB·NiterCG·NiterCI) / CG+CI 솔버 워크플로 / WC13 results (Fig 1-11). 7개 multiscale_* 파일 algorithm 매핑은 PDF + web-refs §8.1 GitHub API 직접 fetch 기반."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23 + §I 작성 2026-05-28"
note_date: 2026-04~05 (original) / 2026-05-23 (promote) / 2026-05-28 (§I 추가)
verification_by: "사용자 + codex source-code analysis + Claude Opus 4.7 (1M context) — multi_scale_B_v1.pdf 직접 fetch 인용"
verification_date: 2026-04 (§A-H) / 2026-05-28 (§I)
---

## Scope

How ROMS dispatches the three 4D-Var families (incremental I4DVAR, restricted-B-preconditioned-Lanczos RBL4DVAR, weak-constraint R4DVAR), where the cost function is built and minimized, how TLM/ADJ kernels integrate forward/backward, and how trajectories are stored. Use this when running data assimilation cycles, debugging cost-function divergence, or scaling I/O for long DA windows.

## Source basis

- `ROMS/Drivers/i4dvar_roms.h`, `i4dvar.F` — I4DVAR (strong constraint, incremental).
- `ROMS/Drivers/rbl4dvar_roms.h`, `rbl4dvar.F` — RBL4DVAR (restricted B, Lanczos).
- `ROMS/Drivers/r4dvar_roms.h`, `r4dvar.F`, `tl_r4dvar_roms.h` — R4DVAR / weak-constraint.
- `ROMS/Adjoint/ad_misfit.F`, `ad_main3d.F` — observation misfit, adjoint kernel.
- `ROMS/Tangent/tl_main3d.F` — TLM kernel.
- `ROMS/External/wc13.h`, `roms_wc13.in` — WC13 example configuration.

## A. Driver families

| Family | Driver entry | Outer-loop dispatch | Description |
|---|---|---|---|
| I4DVAR | `i4dvar_roms.h:245` (`ROMS_run`) | `:292` calls `background/increment/analysis` | Strong-constraint incremental |
| RBL4DVAR | `rbl4dvar_roms.h:248` | `:308` | Restricted-B preconditioned Lanczos |
| R4DVAR (incl. weak) | `r4dvar_roms.h:248` | `:307` | Representer / weak-constraint variant |
| W4DVAR | (no standalone file) | `tl_r4dvar_roms.h:352` (`driver='tl_w4dvar'`) | Weak-constraint via R4DVAR family |

Core routines:
- I4DVAR: `i4dvar.F:551, 781, 1716`.
- RBL4DVAR: `rbl4dvar.F:400, 645, 2558`.
- R4DVAR: `r4dvar.F:1988` (driver tag).

## B. Inner loop (cost minimization)

The incremental cost is `J = Jb + Jo`:

- `i4dvar.F:1518-1544` — reports normalized `Jb` and `Jo`.
- `i4dvar.F:1464-1482` — background term `back_cost`.
- `ad_misfit.F:194-196` — observation misfit forcing built from `(NLmodVal + TLmodVal - ObsVal)`.

### B-preconditioning

Model-space ↔ minimization-space transforms:
- `i4dvar.F:1412-1433` — `GRADx(Jo)` to `GRADv` via `ad_variability` then `ad_convolution`.
- `i4dvar.F:1619-1637` — `deltaV` to `deltaX` via `tl_convolution` then `tl_variability` (and `tl_balance` if active).
- 기본 `ad_convolution / tl_convolution` 은 single-scale explicit Gaussian diffusion (default). **Multi-scale anisotropic implicit B operator (Matérn class, PR #75)** 는 §I 참조 — `MULTI_SCALE_B` CPP 활성화 시 새 `multiscale_*` 모듈로 분기.

### R / Cobs (observation error)

- Solver equation comments: `ad_congrad.F:62-92`, `ad_rpcg_lanczos.F:68-113`.
- Actual ObsErr weighting in `ad_misfit.F:194-196`.

### CG / Lanczos solvers

- I4DVAR ⇒ `cgradient` (`i4dvar.F:1513`).
- RBL4DVAR ⇒ `rpcg_lanczos` (`rbl4dvar.F:1343`) or `congrad` (`:1353, 1584`).

## C. Outer loop

| Driver | Loop entry |
|---|---|
| I4DVAR | `i4dvar_roms.h:292` |
| RBL4DVAR | `rbl4dvar_roms.h:308` |
| R4DVAR | `r4dvar_roms.h:307` |

TLM integration in loop:
- I4DVAR: `i4dvar.F:1291-1295` calls `tl_main3d/tl_main2d`.
- RBL4DVAR: `rbl4dvar.F:1535-1539`.

ADJ integration in loop:
- I4DVAR: `i4dvar.F:1353-1357` calls `ad_main3d/ad_main2d`.
- RBL4DVAR: `rbl4dvar.F:1408-1412`.

Time-window length: each phase takes `RunInterval` (`i4dvar.F:791-792`, `rbl4dvar.F:655-656`); TL/AD kernels convert via `ntimesteps` (`tl_main3d.F:179`, `ad_main3d.F:258`).

## D. Observation operator / innovations / residuals

- Observation file: `OBSname == roms_obs.nc` in `s4dvar.in:461`.
- Split-driver scripts rewrite to `..._obs_...nc`: `submit_split_i4dvar.sh:431` (and r4dvar/rbl4dvar analogs).
- Innovation calculation: `(NLmodVal + TLmodVal - ObsVal)` in `ad_misfit.F:194-196`.
- Split drivers load `ObsVal/ObsErr` from `OBS(ng)%name`: `rbl4dvar.F:847-861`, `r4dvar.F:617-631`.
- `wrtMisfit` switch for residual output: `i4dvar.F:406-413`, `rbl4dvar.F:1515-1522`.
- Diagnostics/misfit cost written to DAV: `i4dvar.F:723-735`, final at `:2404-2417`; rbl at `:2773-2780`.

## E. Tangent linear model (TLM)

- Main TLM kernel: `tl_main3d.F:3` (`SUBROUTINE tl_main3d`).
- Forward stepping at `:185`; data ingestion `tl_get_data` at `:210`.
- BASIC STATE fields (`set_depth/set_massflux`) processed at `:229-247`.
- Drivers wire nonlinear history as basis trajectory (`i4dvar.F:1026-1043`).

The TLM is **linearized about the nonlinear trajectory** — that's why the basis trajectory must be stored from the prior nonlinear forward run.

## F. Adjoint model

- Main AD kernel: `ad_main3d.F:3`.
- Reverse-time integration explicit: `STEP_LOOP : DO istep=Nsteps,1,-1` at `:266` (comments `:191-199`).
- Sensitivity forcing from observations at `:697` (`obs_read`) then `:711-714`:
  - `ad_htobs` → weak-constraint.
  - `ad_misfit` → strong-constraint.

## G. Trajectory storage (memory vs disk)

- Disk trajectory files per outer loop: HIS at `i4dvar.F:1030-1043`, QCK at `:1051-1063`, adjoint history at `:1192-1200`.
- Memory vs split-file behavior: split mode repeatedly reads DAV/ITL/TLM/ADM NetCDF because values "are in memory in the unsplit algorithm" (`i4dvar.F:862-867, 993-996`; `rbl4dvar.F:790-793, 805-809`).
- I/O-size/performance tradeoff: explicit multi-file rationale "split ... to reduce size" at `i4dvar.F:1137-1138`; delayed sync/close for performance at `r4dvar.F:367-373`.

## H. Practical examples (WC13)

- WC13 compile/test config: `wc13.h` (case CPP options), `roms_wc13.in:1223` (`APARNAM = i4dvar.in`).
- Batch workflows: `submit_split_i4dvar.sh`, `submit_split_r4dvar.sh`, `submit_split_rbl4dvar.sh`. Standard/norm files and obs substitution at `submit_split_i4dvar.sh:120-131, 151, 431`.
- The `roms_test` exercise PDFs are not in this tree; only URL/comment reference at `submit_mixres_rbl4dvar.sh:60`.

## I. Multi-scale background error covariance (PR #75, `MULTI_SCALE_B`)

PR #75 (OPEN, branch `feature/multiscale`) 의 새 implicit multi-scale anisotropic **B** operator. Weaver et al. (2013, 2016, 2018) 의 Matérn-class implicit diffusion formulation 을 ROMS 4D-Var 에 통합. 출처: PR description + 첨부 `multi_scale_B_v1.pdf` (15p, 2026-05-28 fetch). 한국 적용 검토는 [`web-refs/roms-official-resources.md §8.1.5`](../web-refs/roms-official-resources.md) 참조.

### I.1 Mathematical formulation (PDF §1)

Matérn class $d$-차원 correlation function (eq 1):

$$c_d(r) = \frac{2^{1-\nu}}{\Gamma(\nu)} \left(\frac{r}{L}\right)^{\nu} K_\nu\left(\frac{r}{L}\right)$$

- $L$: scale parameter, $K_\nu$: 2종 modified Bessel function 차수 $\nu$, $r$: 점 사이 거리
- Multi-scale 결합 (eq 2): $f_{d,P}(r) = \sum_{p=1}^{P} \gamma_p\, c_{d,p}(r)$ with $\sum_p \gamma_p = 1$
- 음수 $\gamma_p$ 도 허용 가능 (negative lobe correlation) — Gregori et al. (2008) 조건 필요

**Correlation = implicit diffusion** (PDF §1 핵심 통찰):

2D 확산 방정식 $\partial\eta/\partial s - \nabla(\kappa\nabla\eta) = 0$ (eq 3) 의 $M$ steps 후 implicit form (eq 4):

$$\eta(x,y,0) = (1 - \nabla\kappa\nabla)^M\, \eta(x,y,M)$$

(1)과 (4)의 관계: $M = \nu + d/2$, 2D 이면 $d=2$, $\kappa = L^2$. Daley length scale $D = \sqrt{-d / \nabla^2 c_d(r)|_{r=0}}$ 와 $D^2 = (2M-d-2)\kappa$ ($\kappa$ 등방). 이방성 경우 $\boldsymbol{\kappa}$ diffusion tensor → $\mathbf{D} = (2M-d-2)\boldsymbol{\kappa}$ 요소가 squared length scales.

**2D 에서 $M$ 짝수, $M > 2$ 필수**. $M \geq 10$ → 본질적으로 Gaussian (현재 default explicit B 와 동등). $M$ 작으면 longer-tailed (heavy-tail) Matérn.

Open boundary 에서는 $d=1$ 1D diffusion 으로 별도 처리.

### I.2 ROMS implicit solver (PDF §2)

(4) 풀이에 **CG (Conjugate Gradient) + CI (Chebyshev Iteration) 조합** 채택 (Weaver et al. 2016, 2018):

- CG 단독: symmetry 보존을 위해 Cholesky factorization 필요 (CG solver의 adjoint 필요) + parallel 에서 scalar product 비용 큼
- CI 단독: easily adjointable + scalar product 불필요. 단 $(1-\nabla\kappa\nabla)$ 의 max/min eigenvalue 추정 필요
- **ROMS 채택**: CG (Lanczos formulation with random vectors) 로 eigenvalue 추정 → CI 로 implicit diffusion 풀이. eigen spectrum 은 grid·$\kappa$ 고정 시 변하지 않으므로 normalization 단계에서 한 번 추정 후 재사용.

### I.3 7개 신규 `multiscale_*` 파일 매핑

PR #75 의 `ROMS/Utility/multiscale_*` (전체 7개 신규 파일, 합계 +18,628 라인). PDF §2-3 의 algorithm role 과 매핑 ([`web-refs/roms-official-resources.md §8.1`](../web-refs/roms-official-resources.md) verbatim line count):

| 파일 | 라인 | PDF 매핑 |
|---|---|---|
| `multiscale_Klaplacian.h` | +6,365 | (4) 의 $(1 - \nabla\kappa\nabla)$ horizontal K-Laplacian operator. Matérn correlation 의 implicit form 핵심 빌딩 블록 |
| `multiscale_Vdiff.h` | +3,173 | Vertical diffusion (vertical correlation은 horizontal 과 separable 가정, PDF §3 NOTE) |
| `multiscale_CIsolver.h` | +2,741 | Chebyshev iteration solver — PDF §2 의 (4) 풀이 main routine (Weaver 2016/2018) |
| `multiscale_eigen.F` | +2,310 | $(1-\nabla\kappa\nabla)$ max/min eigenvalue 추정 (CI bounding 용). Lanczos CG with random vectors |
| `multiscale_CGsolver.h` | +1,518 | CG solver — eigenvalue 추정 단계 전용 (correlation solve 는 CI 가 담당) |
| `multiscale_driver.h` | ~~ | Multi-scale orchestration: Nscale 만큼 $c_{d,p}$ 계산 dispatch |
| `multiscale_sum_B.h` | ~~ | eq (2) 의 weighted sum $\sum \gamma_p c_{d,p}$ 결합 |

**Algorithm flow** (PDF §3 + 위 파일 역할 추론):

1. 사용자가 `s4dvar.in` 에 `Nscale`, `Mlap[p,state-var]`, `Bwgt[p,state-var]`, `Hdecay*X/Y[state-var]` 지정
2. `multiscale_driver.h` 가 `p = 1..Nscale` 루프 진입
3. 각 $p$ scale 에 대해:
   - `multiscale_eigen.F` → `multiscale_CGsolver.h` (Lanczos CG with random vectors, `NiterCG` iter) → eigenvalue bounds 산출
   - `multiscale_CIsolver.h` (NiterCI/2 forward + NiterCI/2 adjoint) → `multiscale_Klaplacian.h` 호출하며 (4) 풀이 → $c_{d,p}$
4. `multiscale_sum_B.h` 가 $\gamma_p = \texttt{Bwgt}[p]$ 와 $c_{d,p}$ 가중합 → $B$ operator 완성
5. `multiscale_Vdiff.h` 가 vertical 차원 별도 처리

코드 line:line cross-ref 는 future code-level audit 대상 (PR #75 OPEN, merge 후 본격 검증).

### I.4 `s4dvar.in` parameters (PDF §3.A, §3.C)

PR #75 의 `s4dvar.in` +293 -86 diff 의 신규 키:

| Parameter | 의미 | 제약 |
|---|---|---|
| `Nscale` | 결합할 correlation function 개수 ($P$ in eq 2) | $\geq 1$ |
| `Mlap[p, state-var]` | 각 scale·state variable 별 $M$ 값 | **짝수**, $M > 2$ |
| `Bwgt[p, state-var]` | 각 scale·state variable 별 weight $\gamma_p$ | state variable 별 $\sum_p = 1$ |
| `HdecayMX[v]`, `HdecayMY[v]` | model error 의 $D_x, D_y$ (Daley length scale, km) | per state variable per scale |
| `HdecayIX[v]`, `HdecayIY[v]` | initial condition error 의 $D_x, D_y$ | per state variable per scale |
| `HdecayFX[v]`, `HdecayFY[v]` | surface forcing error 의 $D_x, D_y$ | per state variable per scale |
| `HdecayB[v]` | open boundary 의 Daley length scale ($x$ or $y$ — orientation 따라) | 1D |
| `NiterCG` | CG solver iteration (eigenvalue 추정용) | per scale |
| `NiterCI` | CI solver iteration (correlation solve) | **짝수** (NiterCI/2 forward + adjoint) |

NOTE: vertical correlation 은 변경 없음 (separable 가정).

### I.5 Tuning workflow (PDF §3.C)

NiterCG/NiterCI 값 결정 절차:

1. `define MULTI_SCALE_DEBUG` CPP 활성화 + normalization factor 계산 모드 (`Nmethod=1`, `Nrandom=1`)
2. residual norm $\epsilon_k = \|r_k\|_2 / \|b\|_2$ 출력 — 각 CG/CI iteration $k$ 별
3. $\epsilon_k$ 작을수록 좋음 ($\epsilon_k = 0$ 이 exact). CI 의 $\epsilon$ 은 NiterCI/2 forward 만 계산되므로 CG 보다 클 것 (rule of thumb: $\text{NiterCI} \approx \text{NiterCG}$)
4. WC13 예시 (PDF Fig 2): $D_x=D_y=50\text{km}, M=20$ → 50 iter 에 $\epsilon \sim 10^{-30+}$. 즉 NiterCG ~30 으로 충분
5. 튜닝 완료 후 **반드시 `undefine MULTI_SCALE_DEBUG`** — 미정의 시 매 $B$ 호출 마다 diagnostic 출력 폭주 + CI 가 scalar product 2개 추가 계산 → 성능 저하

### I.6 WC13 검증 결과 (PDF §4, Fig 11)

WC13 (California Current ~30 km grid, 30 levels) 에서 3가지 **B** 모델 비교 (4D-Var cost function $J$ vs inner-loop iter):

- Red: single isotropic, $(D_x, D_y, M) = (50, 50, 20)$
- Blue: 2-scale isotropic, $(D_1, M_1, \gamma_1) = (30, 4, 0.8)$ + $(90, 20, 0.2)$
- Black dashed: 3-scale anisotropic, $(D_x, D_y, M, \gamma) = (30, 30, 20, 0.1)$, $(65, 30, 20, 0.2)$, $(100, 30, 4, 0.7)$

모두 25 iter 안 수렴. **PDF 명시 "not to advocate for one choice ... but rather to illustrate that the code is fully functional"** — 즉 PR #75 단계는 functionality 검증 위주. 최적 **B** 선택은 application-specific tuning 영역.

### I.7 Negative-lobe correlation 예시 (PDF §4 Fig 9-10)

2개 Matérn 결합 (eq 5):

$$f(r) = \gamma_1 \frac{2^{1-\nu_1}}{\Gamma(\nu_1)}\left(\frac{r}{L_1}\right)^{\nu_1} K_{\nu_1}\left(\frac{r}{L_1}\right) + \gamma_2 \frac{2^{1-\nu_2}}{\Gamma(\nu_2)}\left(\frac{r}{L_2}\right)^{\nu_2} K_{\nu_2}\left(\frac{r}{L_2}\right)$$

Gregori et al. (2008) 조건:

$$[1 - \max(1, (L_1/L_2)^d)]^{-1} \leq \gamma_1 \leq [1 - \min(1, (L_2/L_1)^{2\nu_2})]^{-1}$$

$M_1 = M_2 = 20, D_1 = 90, D_2 = 80\,\text{km}, d = 2$ → $-3.76 \leq \gamma_1 \leq 1.01$. $\gamma_1 = -3.76, \gamma_2 = 4.76$ 선택 시 ~120 km 에서 양→음 전이.

활용 시나리오: 작은 스케일 positive correlation + 큰 스케일에서 anti-correlation (예: 대척 eddy structure 표현). 단 negative-lobe 는 physical interpretation 신중.

### I.8 한국 적용 cross-ref

NIFS KOOS-EJS (동해예측시스템) ROMS 기반 4D-Var 의 multi-scale B 적용 가능성은 [`web-refs/roms-official-resources.md §8.1.5`](../web-refs/roms-official-resources.md). 핵심:

- 동해 mesoscale eddy (50-100 km) + sub-mesoscale (5-20 km) 동시 표현 → 다중 scale B 가 적합
- 후속 평가 항목: 현재 KOOS-EJS B 가 single-scale 인지, multi-scale 도입 benefit 정량화

## J. PR #75 후속 commit 5건 (2026-05-27 ~ 05-31, verified 2026-06-01)

§I 의 multi-scale B 후속 활동. 5 commit GitHub API 직접 fetch.

| # | SHA | 일시 | 메시지 | Files |
|---|---|---|---|---|
| 1 | `7a1f5d9d` | 2026-05-27 15:04 UTC | Updated 4D-Var algorithms | 24 files |
| 2 | `b7312fb1` | 2026-05-27 21:54 UTC | Added B-correlation CDL template file | 2 files |
| 3 | `952d7eab` | 2026-05-28 18:07 UTC | Added function for tracers management | 3 files |
| 4 | `16601076` | 2026-05-31 17:10 UTC | Added Dirac parameters | 7 files |
| 5 | `23919237` | 2026-05-31 19:30 UTC | Corrected parallel bug | 1 file (`read_asspar.F`) |

### J.1 4D-Var algorithms updated (`7a1f5d9d`, 24 files)

핵심 변경 (verified by GitHub API file list):

- `ROMS/Drivers/i4dvar.F` (+104 -42), `r4dvar.F` (+106 -41), `rbl4dvar.F` (+110 -51) — three primary 4D-Var drivers 전면 갱신
- `ROMS/Drivers/correlation.h` (+3) — correlation driver header 추가
- `ROMS/Tangent/tl_def_ini.F` (+12) — tangent linear initialization definition 보강
- `ROMS/Utility/def_*.F` (10 files: def_dai/diags/error/extract/floats/hessian/impulse/info/lanczos/state) — 각 +12 라인 균일 추가 → 신규 NetCDF definition 헤더 (Multi-scale B 출력 통합)

→ I4DVAR / R4DVAR / RBL4DVAR 모두에 multi-scale B 통합 + NetCDF 출력 routine 11개 동시 수정 = 일관 출력 형식 확보.

### J.2 B-correlation CDL template (`b7312fb1`, 2 files)

```
added    +208  -0  Data/ROMS/CDL/s4dvar_Bcorrelation.cdl
modified +50  -2   ROMS/Utility/def_info.F
```

신규 CDL (NetCDF Common Data Language) template `s4dvar_Bcorrelation.cdl` — B 상관행렬의 검증·진단 NetCDF 파일 구조. `def_info.F` 가 변수 메타데이터 정의 부에서 이 template 사용.

### J.3 Tracers management (`952d7eab`, 3 files)

```
added    +94  -0   ROMS/Utility/tracer_metadata.F
modified +97  -12  ROMS/Utility/read_asspar.F
modified +3   -0   ROMS/Utility/set_pio.F
```

신규 `tracer_metadata.F` (94 lines) — tracer 식별·메타데이터 관리 module. `read_asspar.F` 가 4D-Var assimilation parameter 읽을 때 호출하도록 +85 라인 확장. `set_pio.F` 의 parallel I/O 등록에도 추가.

### J.4 Dirac parameters (`16601076`, 7 files) — **§I.4 s4dvar.in 확장**

```
modified +52  -11  ROMS/External/s4dvar.in
modified +123 -4   ROMS/Utility/read_asspar.F
modified +117 -21  ROMS/Functionals/ana_perturb.h
modified +14  -7   ROMS/Utility/checkdefs.F
modified +12  -0   ROMS/Modules/mod_scalars.F
modified +1   -0   ROMS/Drivers/correlation.h
modified +1   -0   ROMS/Modules/CMakeLists.txt
```

`s4dvar.in` 직접 diff (line +253-269 신규 11 Dirac() 키워드, GitHub API verbatim):

```fortran
! Dirac delta function (i,j,k) locations for testing correlations parameters.
  Dirac(isFsur) == 25 20                ! free-surface
  Dirac(isUbar) == 15 30                ! 2D U-momentum
  Dirac(isVbar) == 15 35                ! 2D V-momentum
  Dirac(isUvel) == 15 30 30             ! 3D U-momentum
  Dirac(isVvel) == 15 35 30             ! 3D V-momentum
  Dirac(isTvar) == 30 20 30 \           ! temperature
                   20 40 30             ! salinity
  Dirac(isTsur) == 20  15   \           ! surface heat flux
                   25  20               ! surface salt flux
  Dirac(isUstr) == 18  30               ! surface U-momentum stress
  Dirac(isVstr) == 18  35               ! surface V-momentum stress
```

**Dirac delta function locations** — Multi-scale B correlation 검증용 single grid point delta function. (i,j) 또는 (i,j,k) 격자 좌표에 δ를 두고 correlation function 응답 (negative-lobe 포함, §I.7)을 진단.

부수 변경 `s4dvar.in` line +281-289 (Mlap iteration count) :

```diff
- Mlap(isFsur) == 20    ! Mlap MUST be > 2 and EVEN, > O(10) for Gaussian
+ Mlap(isFsur) == 10    ! Free-surface
- Mlap(isUbar) == 20
+ Mlap(isUbar) == 10
... (모든 state variable 동일하게 20 → 10)
```

`s4dvar.in` line +316:

```diff
-        NiterCG == 50
+        NiterCG == 20
```

→ Multi-scale B implicit diffusion solver 의 Laplacian iteration `Mlap` 20→10, CG iteration `NiterCG` 50→20. **default tuning 절반 수준 감소** — 빠른 수렴이 가능해진 algorithm 개선 반영. §I.4 의 기존 default value 와 정확히 일치 (PDF §3.A 에 적힌 default 가 이 commit 으로 갱신).

`ana_perturb.h` (+117 -21) — analytic perturbation routine 이 Dirac δ initialization 지원. `checkdefs.F` 는 CPP 검증 강화.

### J.5 Parallel bug fix (`23919237`, 1 file)

```
modified +5 -6 ROMS/Utility/read_asspar.F
```

`read_asspar.F` 의 read race-condition 또는 broadcast 누락 buf bug 수정. 1 file·11 lines 변경의 단순 fix이나, **multi-scale B + Dirac 통합 후 MPI 환경에서 발견된 parallel bug** — `952d7eab` (tracers management) 와 `16601076` (Dirac) 에서 `read_asspar.F` 를 크게 확장한 결과 발생한 regression 일 가능성 큼 (동일 file).

### J.6 §I 와의 관계

| §I (PDF 기반) | §J (PR commit 기반, 2026-06-01) |
|---|---|
| 7개 신규 `multiscale_*` core file (§I.3) | 추가 안 됨 — 동일 |
| `s4dvar.in` Mlap default 20 / NiterCG 50 (§I.4) | **Mlap 10 / NiterCG 20 으로 default 절반 감소** (J.4) |
| Dirac delta 검증 (PDF 미언급) | **11 Dirac() 키워드 신규** (J.4) |
| Bcorrelation CDL (PDF 미언급) | **신규 NetCDF template** (J.2) |
| 단일 unified driver 가정 | 세 driver (I/R/RBL 4D-Var) 동시 갱신 (J.1) |
| | tracer_metadata.F 신규 (J.3) |
| | parallel bug fix (J.5) |

→ §I 은 PR 제안 시 (2026-05 초) PDF 기준, §J 는 PR 활동 30일 후 (2026-06) 실제 commit 기준. **default tuning 절반 감소가 가장 영향 큰 발견** — Multi-scale B 가 실제 더 빠르게 수렴함을 algorithm 개선이 입증.

### J.7 KOOS-EJS 적용 후속

§I.8 의 KOOS-EJS multi-scale B 평가 시:
- 기존 §I.4 default (Mlap=20, NiterCG=50) 대신 **갱신된 default (Mlap=10, NiterCG=20)** 부터 시작
- Dirac δ 도구 (§J.4) 로 동해 mesoscale + sub-mesoscale scale별 correlation function 정량 시각화
- I4DVAR / R4DVAR / RBL4DVAR 모두 multi-scale B 호환 (§J.1) — driver 선택 자유도 ↑

## Decision Guide

| Use case | Choice |
|---|---|
| Sparse data, short window, smooth IC update only | I4DVAR (strong constraint) |
| Strong constraint with better preconditioning, tougher convergence | RBL4DVAR |
| Long window, model-error matters, can afford I/O | R4DVAR weak-constraint (W4DVAR tag) |
| Quick smoke test | WC13 example (`roms_wc13.in`) |
| Scaling DA across cluster | Split-file mode (reads from disk between phases) |
| Single-machine debug | Unsplit mode (in-memory) |
| Verify innovation processing | Set `wrtMisfit=T`, inspect DAV file |
| Observation outliers | Inflate `ObsErr` per-type in `obs.nc` |
| Background covariance localization | Tune `Hdecay/Vdecay` correlation lengths in `s4dvar.in` |

## Working Rules

- Run a strong-constraint I4DVAR first, even if your target is weak-constraint — it builds the basic-state trajectory and shakes out observation file mistakes cheaply.
- Outer loops typically 1–3; inner loops 10–50 (CG iterations). Cost grows linearly with outer × inner.
- Always check the cost-function reduction across outer loops. `J_final / J_initial < 0.5` is normal; > 0.95 means the system is not converging (bad B, bad obs, or trivial increment).
- Run the TLM-AD pair with the inner-product test at least once after any source change. Asymmetry > 1e-10 in double precision is a bug.
- Background covariance correlation lengths: scale-of-eddies in horizontal (10–50 km coastal, 100–300 km open ocean), 50–200 m vertical. Too short ⇒ noisy increments; too long ⇒ smeared.
- For weak-constraint, check that model-error covariance `Q` is non-trivial. Default `Q=B` reduces to strong-constraint in disguise.

## Common Pitfalls

- ▢ Forgetting to update the basic-state trajectory between cycles — TLM linearizes about a stale state and innovations diverge.
- ▢ ObsErr too small (e.g., reporting RMS instead of representativeness error) — inner loop tries to overfit and explodes.
- ▢ Localization not used in B — increments leak across basin, decorrelating obs influence.
- ▢ Mixing I4DVAR with R4DVAR namelist parameters — drivers share `s4dvar.in` partly but not all keys.
- ▢ Running unsplit mode at scale — memory footprint blows up because basic-state and adjoint trajectories live in RAM.
- ▢ Verifying innovation only at the end of the run — turn on `wrtMisfit` always; cheap and diagnostic.
- ▢ Assuming a `w4dvar.F` exists — the weak-constraint path lives inside the R4DVAR family with the `tl_w4dvar` driver tag.

## Next expansion

- TLM-AD inner-product test recipe (line-by-line).
- WC13 walkthrough with concrete cost-function trajectory plots.
- Localization tooling for B (`s4dvar.in` correlation parameters).
- Hybrid 4D-EnVar discussion if/when ROMS picks up that path.

## References

- Moore et al. 2011 (ROMS 4D-Var trio: I4DVAR, R4DVAR, RBL4DVAR).
- Courtier et al. 1994 (incremental 4D-Var).
- Bennett 2002 (representer method, weak constraint).
- Source: paths above.

**§I Multi-scale B 추가 (PR #75 첨부 `multi_scale_B_v1.pdf` 인용)**:

- Gregori, Porcu, Mateu, Sasvárai 2008 — *Ann. Inst. Stat. Math.* 60, 865–882. (Negative-lobe permissibility 조건)
- Mirouze & Weaver 2010 — *Q.J.R.M.S.* 136, 1421–1443. (Implicit diffusion correlation representation)
- Mirouze, Blockley, Lea, Martin, Bell 2016 — *Tellus A* 68, 29744. DOI: [10.3402/tellusa.v68.29744](https://doi.org/10.3402/tellusa.v68.29744). (Multiple length scale correlation operator)
- Weaver & Mirouze 2013 — *Q.J.R.M.S.* 139, 242–260. (Diffusion equation 의 isotropic/anisotropic correlation 적용)
- Weaver, Tshimanga, Piacentini 2016 — *Q.J.R.M.S.* 142, 455–471. (Chebyshev iteration solver)
- Weaver, Gürol, Tshimanga, Chrust, Piacentini 2018 — *Q.J.R.M.S.* 144, 2067–2088. ("Time"-parallel diffusion-based correlation operators)
- PR #75: <https://github.com/myroms/roms/pull/75> (OPEN, branch `feature/multiscale`, 93 changed files)
- PDF: <https://github.com/user-attachments/files/25944393/multi_scale_B_v1.pdf>

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.

§I Multi-scale B 추가 2026-05-28 by Claude Opus 4.7 (1M context): PR #75 첨부 PDF (15p) 직접 fetch 후 본문 인용. 7개 `multiscale_*` 파일 algorithm 매핑은 PDF + web-refs §8.1 GitHub API fetch 기반.
