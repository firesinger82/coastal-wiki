---
title: "SWASH 비정수압 압력 projection + 선형 solver — SwashImpDep2DHflow·SwashImpLayP2DHflow·SwashSolvers"
model: SWASH
component: src (flow solver + linear solver)
canonical_source: self
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashImpDep2DHflow.ftn90(4284줄) Method 주석 verbatim(:42-61) + Poisson 구축/solve(:3486-3586) + SwashImpLayP2DHflow.ftn90 다층 solver 호출(:5893·5925·6009) + SwashSolvers.ftn90(5705줄) subroutine 목록(pcg:937·sip:1811·bicgstab:3312·tridiag:4297) + 전처리 주석(:14-17 ilu/iludr/iluds, Eisenstat trick :229-238). file:line 직접 인용.; 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
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

수평 유속 발산과 연직 경계 유속 차를 함께 만족시키는 국소 비압축 조건이다 (swashtech PDF p.64: `\nabla\cdot\mathbf u+\frac{w_s-w_b}{h}=0`; theory-framework:ST1-326). [10-15 대조 정정]
수평 유속 발산만 0이라고 쓰지 않는다 (`src/SwashExpDep1DHflow.ftn90:1004`; theory-framework:ST1-326). [10-15 대조 정정]

## 3. 선형 solver (SwashSolvers.ftn90, 5705줄)

| subroutine | 라인 | 방법 |
|---|---|---|
| `sip` | **1811** | **Strongly Implicit Procedure** (Stone 1968) — 5-대각, 구조 2D 수심 평균 (`src/SwashExpDep2DHflow.ftn90:4092`; theory-framework:ST1-327). [10-15 대조 정정] |
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

수심 평균 1D 압력 보정은 `tridiag`를 호출한다 (`src/SwashExpDep1DHflow.ftn90:1263–1265`; theory-framework:ST1-327). [10-15 대조 정정]
구조 2D 수심 평균은 별도 SIP 경로이다 (`src/SwashExpDep2DHflow.ftn90:4092`; theory-framework:ST1-327). [10-15 대조 정정]
Dep/Lay 이름만으로 선형 솔버를 결정하지 않는다 (theory-framework:ST1-327). 매뉴얼은 수직층 수를 늘려 주파수 분산을 개선한다고 설명한다 (swashuse PDF p.16, 인쇄 8). [10-15 대조 정정] [10-15 전수 검증 정정]
비구조 수심 평균 압력은 `bicgstabu`를 호출한다 (`src/SwashExpDepUflow.ftn90:1440`; `src/SwashImpDepUflow.ftn90:1749`; theory-unstructured:ST2-225 수정안). [10-15 대조 정정]
비구조 다층 압력은 `bicgstab3`를 호출한다 (`src/SwashExpLayUflow.ftn90:2450`; theory-unstructured:ST2-225 수정안). [10-15 대조 정정]
비구조 수위는 `pcgu` 또는 `newtonU`를 호출한다 (`src/SwashImpDepUflow.ftn90:1140,1233`; theory-unstructured:ST2-225 수정안). [10-15 대조 정정]
이 구분은 swashuse PDF p.92·99–101에 설명되어 있다 ([theory-unstructured §4.2](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#42-공식-문서와-구현을-연결하는-수정안), ST2-225 수정안). [10-15 대조 정정]

## 5. 본 위키 접점 + 모델 대비

- [`swash-architecture-source-map.md §2`](swash-architecture-source-map.md) — solver 명명규칙(Exp/Imp×Dep/Lay) 의 Imp 계열 내부.
- **SIP 비교**: [SWAN의 SWSIP](../../SWAN/manual-notes/swan-tech-ch6-iterative-solvers.md)는 스펙트럼 공간의 5대각 계를 푼다. [XBeach의 solver_sip](../../XBeach/source-analysis/xbeach_solver.md)는 Stone의 SIP를 사용한다. SWASH의 `sip`도 Stone(1968)을 인용한다 (`src/SwashSolvers.ftn90:1854–1858`). [10-15 전수 검증 정정]
- **분산 표현 대비**: FUNWAVE/Celeris(Boussinesq 고차분산항 + tridiagonal) vs **SWASH(연직층분할 + 비정수압 Poisson projection)** — 같은 위상해상이나 분산 기제가 다름. [`concepts/waves/04 §5.1`](../../../concepts/waves/04-code-and-tools.md) Ferdaus 2025 리뷰.

## 6. 선형 솔버·시간 가중치 근거

- PCG·SIP·BiCGSTAB·삼중대각·Newton 솔버와 ILU 전처리 개요는 [swash-linear-solvers](swash-linear-solvers.md) §1–7에 정리되어 있다. 원본의 루틴 목록은 `src/SwashSolvers.ftn90:4–23`에 있다. [10-15 전수 검증 정정]
- Keller-box의 연직 압력 결합은 `avm`의 `nconct-23` 밴드 순회에 나타난다 (`src/SwashSolvers.ftn90:121–137`). `tridiag`의 직렬 double sweep는 수평 격자점 `m`을 순회한다 (`src/SwashSolvers.ftn90:4353–4368,4395–4422,4466–4479`; `src/SwashExpDep1DHflow.ftn90:1265`). [10-15 전수 검증 정정]
- 음수 sentinel은 1로 변경한다 (`src/SwashReadInput.ftn90:1522`; `src/SwashCheckPrep.ftn90:1277,1285`; inputs-physics-numerics:SI2-181). [10-15 대조 정정]
- 준비 검사에서 `theta=0`은 통과한다 (`src/SwashCheckPrep.ftn90:1273`; inputs-physics-numerics:SI2-181). [10-15 대조 정정]
- 후속 explicit 압력 우변은 `dt*theta`로 나눈다 (`src/SwashExpDep1DHflow.ftn90:1250`; inputs-physics-numerics:SI2-181). [10-15 대조 정정]
- 이 경로는 E 강함의 코드 결함 후보이다 (inputs-physics-numerics:SI2-181). [10-15 대조 정정]
시간적분은 명시적 또는 반암시적으로 선택한다 (`src/SwashReadInput.ftn90:1858–1886`; [guide-syntax-build SG1-101](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md)). [10-15 대조 정정]


## 문서와 코드 차이 (10-15 대조)

출처: [theory-framework](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md), [inputs-physics-numerics](../../../_staging/recovery/compare/swash-inputs-physics-numerics-vs-code.md)의 최종 결론과 원문 인용.

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech, 공개 저장소 `7949227 2026-05-06 "release v12.01"`에서 마지막 변경; 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f 2026-05-26`, 12.01 뒤 `608ffd7`·`9554c98` 포함.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| inputs-physics-numerics:SI2-181 | theta 유효 범위·0 입력 | swashuse PDF p.90: “only values of [theta] in the range [0.5,1] are allowed” | `src/SwashCheckPrep.ftn90:1273`: `if ( pnums(5) > 0. .and. pnums(5) < 0.5 .or. pnums(5) > 1. ) then`; `src/SwashCheckPrep.ftn90:1277` `if ( pnums(5) < 0. ) then`; `src/SwashExpDep1DHflow.ftn90:1250`: `d(nm) = ( fac1*u1(nm) + fac2*u1(nmd) + w1top(nm) + w1bot(nm) )/(dt*theta)`; `src/SwashReadInput.ftn90:1522`: `call INREAL ('THETA', pnums(5), 'STA', -1.)`; `src/SwashCheckPrep.ftn90:1285`: `pnums(5) = 1.`은 1277행의 음수 조건 안에 있다. `src/SwashComputFlow.ftn90:74–86`은 oned·`kmax=1`·`mtimei=1`에서 명시적 1DH를 호출한다. `src/SwashExpDep1DHflow.ftn90:174`: `theta   = pnums( 5)`; `src/SwashExpDep1DHflow.ftn90:1231` `if ( ihydro == 1 ) then`; `src/SwashExpDep1DHflow.ftn90:1242` `if ( wets(nm) == 1 ) then`. | E 강함 | NONHYDROSTATIC `theta=0`은 준비 검사를 통과한다. 후속 explicit 압력 우변은 `dt*theta`로 나눈다. 이 경로는 E 강함의 코드 결함 후보이다. 검사식은 `8756667:src/SwashCheckPrep.ftn90:1145–1157`부터 같다. `7949227` 이후 두 코드 변경은 이 검사와 압력 분모를 고치지 않았다. 젖은 셀의 명시적 1DH BOX 경로가 0을 분모에 사용하므로 E 강함을 유지한다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| theory-framework:ST1-182 | 번호 없는 압력 Laplacian | swashtech PDF p.46: `\Delta p=\nabla\cdot\nabla p` | `src/SwashImpDep1DHflow.ftn90:1393–1395` `a(nm) = fac2 * gmat(nmd,1)`<br>`b(nm) = fac1 * gmat(nm ,1) + fac2 * gmat(nmd,2) - 2./hs(nm)`<br>`c(nm) = fac1 * gmat(nm ,2)` | F 표기 차이 | 해석: 코드의 `fac1`·`fac2`와 `gmat` 곱은 압력 기울기와 발산의 합성에 대응한다. F의 범위는 이 조립 구조이다. 전체 비정수압 식의 연직 `-2./hs(nm)`와 지형 계수까지 순수 스칼라 Laplacian과 같다는 뜻은 아니다. ST1-183과 같은 대응이다. [10-15 결론 검증 정정] |
| theory-framework:ST1-183 | 번호 없는 mimetic 압력 연산자 | swashtech PDF p.46: `\tilde{\mathbb H}^n\tilde{\mathbb D}^{n-1}\mathbb H^1\mathbb D^0\pi^{(0)}`; `provided that their metric is given.` 원문의 격자 조건은 `arbitrary well-centered meshes, either 2D or 3D, provided that their metric is given.`이다. | `src/SwashImpDep1DHflow.ftn90:1393` `a(nm) = fac2 * gmat(nmd,1)`; `src/SwashExpDep2DHflow.ftn90:4418`의 역 면적 적용은 ST1-164이다. | F 표기 차이 | 해석: 기울기·플럭스 변환·발산·역 면적은 코드 계수와 나눗셈에 포함된다. F의 범위는 ST1-182의 조립 구조이다. 문서의 일반 구성은 계량이 주어진 well-centered 격자를 전제로 한다. 이 코드로 임의 3D 격자 지원을 주장하지 않는다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-326 | 압력 보정의 divergence-free 뜻 | `source-analysis/swash-nonhydrostatic-pressure-solver.md:51` `divergence-free(비압축 연속식 만족) 속도장.`<br>swashtech PDF p.64: `\nabla\cdot\mathbf u+\frac{w_s-w_b}{h}=0`; | `src/SwashExpDep1DHflow.ftn90:1004` `w1bot(nm) = -0.5 * rdx * ( u1(nm) + u1(nmd) ) * ( dpu(nm) - dpu(nmd) )` | C 문서 누락 (현재 노트) | 수평 유속 발산과 연직 경계 유속 차를 함께 만족시키는 국소 비압축 조건이다. 수평 유속 발산만 0이라고 쓰지 않는다. [10-15 전수 검증 정정] |
| theory-framework:ST1-327 | 1D 압력 선형 솔버의 누락 | `source-analysis/swash-nonhydrostatic-pressure-solver.md:73` `**수심평균(Dep) = SIP / 다층(Lay) = BiCGSTAB + tridiag**.` | `src/SwashExpDep1DHflow.ftn90:1263–1265` `! solve the Poisson equation`<br>`!`<br>`call tridiag ( a, b, c, d, dq, kgrpnt )`; `src/SwashExpDep2DHflow.ftn90:4092` `call sip( amat, rhs, dq )`. | B 문서 오기 (현재 노트) | 수심 평균 1D 압력 보정은 `tridiag`를 호출한다. 구조 2D 수심 평균은 별도 SIP 경로이다. Dep/Lay 이름만으로 선형 솔버를 결정하지 않는다. `8756667:src/SwashExpDep1DHflow.ftn90:933`에도 같은 `tridiag` 호출이 있다. `git log -G 'call tridiag'`는 최초 공개판 이후 삭제·재등록만 보여 준다. 1D 경로가 SIP에서 바뀐 판 차이가 아니므로 [git 판정 AD §3](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)의 B를 유지한다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
