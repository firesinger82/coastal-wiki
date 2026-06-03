---
title: "XBeach 선형 solver(solver.F90) — SIP(Stone 1968 Strongly Implicit, α=0.94) / tridiagonal. nonh 동압력 Poisson(solver_solvemat) 해법"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/solver.F90 (514) 직접 read — public solver_init/solvemat/tridiag/sip, SOLVER_SIPP vs SOLVER_TRIDIAGG dispatch(114-122), SIP alpha=0.94(40), residual/iteration 카운터(itmea/itmax/itnconv) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — SIP/tridiag solver verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_nonh.md
---

# XBeach 선형 solver (solver.F90)

> `solver.F90`(514) 직접 read. [[xbeach_nonh]] 의 **동압력 Poisson 방정식**(5-diagonal `mat·dp=rhs`)을 푸는 elliptic 선형 solver. MPI 시 nonh 미포함(`nh_pars.inc`). public: `solver_init`/`solver_solvemat`/`solver_tridiag`/`solver_sip`.

## 1. 2 solver dispatch (solver.F90:114-122)

```fortran
if     (par%solver == SOLVER_SIPP)     → solver_sip      ! SIP (기본, 2D)
elseif (par%solver == SOLVER_TRIDIAGG) → solver_tridiag  ! 삼중대각 (1D/특수)
```
`solver_solvemat`(nonh 가 호출)이 위로 분기.

## 2. SIP — Strongly Implicit Procedure (Stone 1968) ★

5-diagonal 비대칭 행렬의 반복 해법:
- **incomplete LU 분해**(M = L·U ≈ A + N, N 은 작은 보정) — 완전 LU 의 fill-in 회피.
- **`alpha = 0.94`**(Stone partial cancellation parameter) — L·U 곱의 잉여 대각항을 부분 상쇄(0~1, 1에 가까울수록 강한 implicit; 0.92-0.95 전형).
- 반복: `residual = rhs − A·dp` → `M·δ = residual` (L forward + U back substitution) → `dp += δ`. 잔차 norm < tol 까지.
- 카운터: `itmea`(평균)/`itmin`/`itmax`/`ittot`/`itnconv`(미수렴 횟수) — 수렴 진단.

## 3. Tridiagonal (solver_tridiag)

1D(또는 분리가능) 계의 Thomas 알고리즘(직접 해). SIP 대비 빠르나 2D full coupling 불가.

## 4. 위치

- nonh 동압력 보정([[xbeach_nonh]] §4)의 핵심 — 매 timestep 2회(predictor/corrector) Poisson 해. SIP 반복수가 nonh 비용의 큰 부분.
- ADCIRC GWCE 의 ITPACK JCG([[adcirc-itpack-solver]])와 같은 역할(elliptic 압력/수위 계 반복解)이나, XBeach 는 SIP(비대칭 5-diag), ADCIRC 는 JCG(대칭).

## 5. 연결

- [[xbeach_nonh]] — solver_solvemat 호출(동압력 Poisson `mat·dp=rhs`)
- Stone 1968 (SIP) / Thomas (tridiagonal)
