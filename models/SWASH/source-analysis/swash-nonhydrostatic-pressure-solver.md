---
title: "SWASH 비정수압 압력 projection + 선형 solver — SwashImpDep2DHflow·SwashImpLayP2DHflow·SwashSolvers"
model: SWASH
component: src (flow solver + linear solver)
canonical_source: self
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashImpDep2DHflow.ftn90(4284줄) Method 주석 verbatim(:42-61) + Poisson 구축/solve(:3486-3586) + SwashImpLayP2DHflow.ftn90 다층 solver 호출(:5893·5925·6009) + SwashSolvers.ftn90(5705줄) subroutine 목록(pcg:937·sip:1811·bicgstab:3312·tridiag:4297) + 전처리 주석(:14-17 ilu/iludr/iluds, Eisenstat trick :229-238). file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/README.md
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/web-refs/swash-official-resources.md
---

# SWASH 비정수압 압력 projection + 선형 solver

> SWASH 의 **정의적 메커닉** — Boussinesq 고차분산항 대신 **비정수압 압력 correction(projection)** 으로 분산을 표현. [`swash-architecture-source-map.md`](swash-architecture-source-map.md) 의 flow solver 내부. 경로: `raw/source_code/swash/src/`.

## 1. 시간적분 스킴 (SwashImpDep2DHflow.ftn90 Method, verbatim :42-61)

depth-averaged 2DH implicit solver 의 Method 주석 직접 인용:

| 항 | 스킴 |
|---|---|
| 연속식 + 수위경사(운동량) | **θ-scheme** (0.5 ≤ θ ≤ 1, `:46-48`) |
| 이류항(advection) | **MacCormack predictor-corrector** (`:49-50`) |
| 저면마찰 | **Euler implicit** (`:51`) |
| **비정수압 압력경사** | **semi-implicit θ-scheme** (`:52`) |
| 이류 공간이산화 | momentum-conservative(수축 시 energy-head conservative), 1차 upwind 또는 **고차 flux-limited**(CDS·Fromm·BDF·QUICK·MUSCL·Koren) — defect correction (`:53-57`) |
| w-운동량(연직) | z-방향 비정수압 압력경사만, **Keller-box scheme** (`:58-60`) |
| 비정수압 압력 | **2차 정확도 pressure correction technique** (`:61`) |

→ 시초 알고리즘 = **Stelling & Zijlema 2003** (비정수압 free-surface FD, [`web-refs §2.2`](../web-refs/swash-official-resources.md)).

## 2. 압력 correction / projection (SwashImpDep2DHflow.ftn90)

비정수압 변수: `dq` = pressure correction, `dqgrdu`/`dqgrdv` = projection 용 x/y 압력경사 (`:96-98`).

흐름 (`:3486-3586`):

1. **compute pressure correction** (`:3486`)
2. **build Poisson equation** (`:3490`) — 5-대각 행렬 `amat(nm,1:5)`:
   - 이웃 계수: `amat(nm,2)=fac2·gmatu(nmd,1)`, `amat(nm,3)=fac1·gmatu(nm,2)`, `amat(nm,4)=fac2·gmatv(ndm,1)`, `amat(nm,5)=fac1·gmatv(nm,2)` (`:3517-3530`)
   - 중심 + 압력항: `amat(nm,1) = ... − 2·gsqs(nm)/hs(nm)` (`:3534` 부근)
   - **rhs = 예측속도 발산**: `rhs(nm) = fac1·u1(nm)+fac2·u1(nmd) + fac1·v1(nm)+fac2·v1(ndm) + gsqs·(w1top+w1bot)`, 이후 `/(dt·theta3)` (`:3520-3538`)
   - dry point: `amat=단위행렬(1,0,0,0,0)`, `rhs=0` (`:3569-3574`)
3. **solve Poisson** (`:3581`) — **`call sip( amat, rhs, dq )`** (depth-averaged → SIP)
4. **MPI 교환** (`:3586`) — 이웃 subdomain 과 pressure correction 교환

→ projection: 풀린 `dq` 의 경사(`dqgrdu`/`dqgrdv`)로 예측속도를 보정 → divergence-free(비압축 연속식 만족) 속도장.

## 3. 선형 solver (SwashSolvers.ftn90, 5705줄)

| subroutine | 라인 | 방법 |
|---|---|---|
| `sip` | **1811** | **Strongly Implicit Procedure** (Stone 1968) — 5-대각, depth-averaged 기본 |
| `bicgstab` | **3312** | **BiCGSTAB** (Bi-Conjugate Gradient Stabilized) — 비대칭/다층 |
| `pcg` / `pcg2` | 937 / 1374 | preconditioned conjugate gradient (대칭) |
| `tridiag` | 4297 | tridiagonal Thomas — **Keller-box 연직** 풀이 |

- **전처리(preconditioner)**: `ilu`·`iludr`(ILU diagonal row)·`iluds`(ILU diagonal symmetric) (`:14-17`), **Eisenstat trick** 으로 효율화 (`:229-238`, Eisenstat 1981 "Efficient implementation of preconditioned CG").
- matrix-vector 곱 = unpreconditioned(`:64`) / preconditioned via Eisenstat(`:229`).

## 4. 다층(layer) 시스템 — SwashImpLayP2DHflow.ftn90

다층 비정수압은 연직 층을 가로지르는 3D 압력 시스템:

- depth-integrated 부분: **`call sip( amat, rhsp, dq )`** (`:5893`), `dq0` SIP (`:6009`)
- **층 시스템 전체**: **`call bicgstab( amatp(1:mcgrd,1:qmax,1:nconct), rhsp, dq )`** (`:5925`) — `nconct` = 층간 connectivity(밴드폭), `qmax` = 층 수. 비대칭이라 SIP 대신 BiCGSTAB.
- 연직 Keller-box 분산은 `tridiag` (층 방향 삼중대각).

→ **수심평균(Dep) = SIP / 다층(Lay) = BiCGSTAB + tridiag**. 층 수↑ → 깊은 물 분산 정확(README 정체카드).

## 5. 본 위키 접점 + 모델 대비

- [`swash-architecture-source-map.md §2`](swash-architecture-source-map.md) — solver 명명규칙(Exp/Imp×Dep/Lay) 의 Imp 계열 내부.
- **SIP 공유 계보**: Stone(1968) SIP 는 [[../../Delft3D/source-analysis/delft3d_adi_solver]](difu)·[[../../SWAN/manual-notes/swan-tech-ch6-iterative-solvers]](penta-diagonal)·[[../../XBeach/source-analysis/xbeach_solver]](α=0.94) 모두 사용 — 연안모델 공통 선형 solver.
- **분산 표현 대비**: FUNWAVE/Celeris(Boussinesq 고차분산항 + tridiagonal) vs **SWASH(연직층분할 + 비정수압 Poisson projection)** — 같은 위상해상이나 분산 기제가 다름. [`concepts/waves/04 §5.1`](../../../concepts/waves/04-code-and-tools.md) Ferdaus 2025 리뷰.

## 6. 미보강 (TODO)

- ✅ `bicgstab`/`pcg` 알고리즘 line-by-line(반복·수렴기준) + ILU 전처리 구성 → [[swash-linear-solvers]] (2026-07-04 신설, SwashSolvers.ftn90 5705줄 전수: PCG/SIP/BiCGSTAB/tridiag/dac/nested-Newton + ILU RILUD + primary 인용 Eisenstat/Stone/van der Vorst/Bondeli/Brugnano-Casulli).
- ✅ Keller-box 연직 이산화(`tridiag` 적용부) — [[swash-linear-solvers]] §0·§6 (nconct-23 band 증거 + Thomas double-sweep).
- θ-scheme `theta`/`theta3` 파라미터 기본값·안정성(`SwashReadInput` 카드).
- explicit(`SwashExpDep`) vs implicit 선택 기준 + 시간스텝 CFL.
