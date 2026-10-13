---
title: "swan propagation implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-propagation-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN propagation — actual code-level implementation

## Scope note

This is a **code-level deep dive** into how SWAN actually implements propagation of action density through 4D phase space (x, y, σ, θ). It documents the actual variables, control flow, matrix assembly, solver dispatch, action-density limiter, and stationary-convergence machinery — with file:line citations into the SWAN source tree.

This is the level of detail required to debug: "why does my SWAN run blow up at high frequency?", "which solver gets used when current is on?", "where does the limiter clamp my Hs growth?". The conceptual layer is in `swan-foundation.md`.

## Source basis

- **Codex deep code analysis** of `models/swan/source_code/swan/src/{swancom1,swancom5,swanmain}.ftn` — 2026-05-06.
- **Manual cross-reference** from swantech ch.3 (Numerical approaches), `[file=website:swan:node29]` Numerics.

## A. Main sweep loop (4-quadrant directional sweeping)

### Outer iteration loop (stationary)

`SWCOMP` is the main computation entry. It loops over **iterations** for stationary convergence:

- Iteration loop start: `[file=src/swancom1.ftn line=1487]` — `DO 450 ITER = 1, ITERMX`
- 반복 상한이 양수이고 먼저 끝나지 않으면 반복 몸체는 ITERMX번 실행된다. `src/swancom1.ftn:1487`의 원문은 `DO 450 ITER = 1, ITERMX`이다. `src/swancom1.ftn:2355`의 원문은 `450  CONTINUE`이다. [R8:T1-007](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).
- Sweep header (per-iteration setup of sweep direction): `[file=src/swancom1.ftn line=1698-1715]`
- Per-iteration accuracy check: `[file=src/swancom1.ftn line=2352-2355]` — stops when `ACCUR >= PNUMS(4)` (or `ITERMX` reached)

Per iteration, all 4 sweep quadrants are processed.

### Sweep direction control

- Sweep index: `SWPDIR` selects the current quadrant.
- Sign flags: `KSX, KSY` (signed integer ±1) determine grid stride direction.
- Spatial deltas: `DDX, DDY` carry the signed grid spacing per sweep.
- Set per sweep at `[file=src/swancom1.ftn line=1741-1817]`.
- The actual per-point work runs inside `SWOMPU(...,SWPDIR,KSX,KSY,...)` at `[file=src/swancom1.ftn line=2000-2007]`.

### Action-density buffers (AC1 vs AC2)

- `AC2(MDC, MSC, MCGRD)` — **active** action-density field (current iteration / current time step).
- `AC1(MDC, MSC, MCGRD)` — **previous** time level, used for nonstationary time terms.
- `STRSXY` reads `AC1` for time term when nonstationary at `[file=src/swancom1.ftn line=5406-5409]`, `[file=src/swancom5.ftn line=2177-2184]`.
- Time-level semantics documented in `SWCOMP` argument list at `[file=src/swancom1.ftn line=337-339]`.

### Time-step loop (nonstationary outer)

Outside `SWCOMP`, in `swanmain`:

- Time-step loop: `[file=src/swanmain.ftn line=571]` — `DO 500 IT = IT0, MTC`
- Per-step `SWCOMP` call: `[file=src/swanmain.ftn line=620-623]`

So nonstationary nesting: `[outer time-step] → [iteration] → [4-sweep]`.

## B. Geographic-space propagation (BSBT discretization, matrix assembly, solve)

### Matrix coefficient buffers

Per-grid-point matrix is assembled in `ACTION` `[file=src/swancom1.ftn line=5349-5352]`:

- LA·UA는 방향 결합이다.
- 5L·6U는 주파수 결합이다.
- `IMATDA`는 대각 계수이다.
- `IMATRA`는 우변이다.

R1의 수정안은 두 결합을 구분한다. `src/swancom1.ftn:8730–8735`의 `RES(ID,IS) = IMATRA(ID,IS)`에서 IMATDA·IMAT5L·IMAT6U·IMATLA·IMATUA의 곱을 차감한다. [R1 §4](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안).

### BSBT 경로

정렬 정상 기본값은 SORDUP이다. 정렬 비정상 기본값은 S&L이다. BSBT는 선택 경로와 국소 차수 변경 경로에 사용한다. `src/swanmain.ftn:1179–1180`의 원문은 `PROPSS = 2`와 `PROPSN = 3`이다. `src/swancom1.ftn:3136,3139,3232`의 원문은 `PROPSL = 1`이다. [R1 §4](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안).

- Dispatch: `ACTION` calls `STRSXY` at `[file=src/swancom1.ftn line=5395-5410]`
- Diagonal contribution `FXY1 → IMATDA`: `[file=src/swancom5.ftn line=2148-2156]`
- RHS contribution `FXY2 → IMATRA`: `[file=src/swancom5.ftn line=2189-2193]`

Backward Time은 현재 시간의 미지수를 사용하는 음해법 Euler 시간차분을 뜻한다. 비선형 원천항 계수를 이전 반복에서 평가하는 절차와 구분한다. `src/SwanTranspX.ftn90:146,149–150`의 원문은 `acold = ac1(id,is,iv1)`, `rhs (id,is  ) = rhs (id,is  ) + acold*RDTIM`, `amat(id,is,1) = amat(id,is,1) + RDTIM`이다. [R1 §4](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안).

### Solver dispatch (SOLPRE → SOLMAT/SOLMT1/SWSIP)

After the matrix is assembled, `SWOMPU` calls `SOLPRE` (preconditioner / scaling) at `[file=src/swancom1.ftn line=3644-3653]`, then dispatches:

| 해법 | 선택 조건 | 코드 원문 |
|---|---|---|
| 직접 나눗셈 | 첫 분기 | `src/swancom1.ftn:3656` `IF ( IREFR.EQ.0 .AND. ITFRE.EQ.0 ) THEN` |
| SWSIP | 주파수 결합 분기의 `INT(PNUMS(8)).EQ.1` | `src/swancom1.ftn:3681–3682` `ELSEIF ( (DYNDEP .OR. ICUR .EQ. 1) .AND.`<br>`&           PNUMS(8).NE.0.                 ) THEN`; `src/swancom1.ftn:3693` `CALL SWSIP ( AC2, SWMATR(1,1,JMATD), SWMATR(1,1,JMATR),` |
| SOLMT1 | 같은 분기의 `INT(PNUMS(8)).EQ.2 .OR. INT(PNUMS(8)).EQ.3` | `src/swancom1.ftn:3709` `CALL SOLMT1  (IDCMIN             ,IDCMAX             ,` |
| SOLMAT | 위 분기들의 나머지 | `src/swancom1.ftn:3726` `CALL SOLMAT (IDCMIN            ,IDCMAX             ,` |

직접 나눗셈 경로를 먼저 구분한다. $(\mathrm{DYNDEP}\lor\mathrm{ICUR}=1)$과 `PNUMS(8)`의 결합으로 SOLMAT·SOLMT1·SWSIP를 선택한다. 무흐름만으로 Thomas 분기를 단정할 수 없다. [R1 §4](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안), [R8 §2.2.1](../../../_staging/recovery/flow/SWAN-callflow.md#221-정렬-격자점-swompu의-직접-호출).

현재 고정값은 보정 인자 0이다. 구현 골격은 SIP이지만 활성 인수분해는 Stone 교차 보정 없는 ILU 형태이다. `src/swancom1.ftn:8438`의 원문은 `PARAMETER (ALFA=0.0,SMALL=1.E-15)`이다.

### Structured vs unstructured branching

The `SWCOMP` machinery (above) is for **structured** grids. Unstructured runs branch in `swanmain`:

- Top-level split: `[file=src/swanmain.ftn line=618-627]`
- `OPTG.NE.5` → `SWCOMP` (structured)
- `OPTG.EQ.5` → `SwanCompUnstruc` (unstructured)

The unstructured path uses different propagation primitives (out of scope for this note).

## C. Spectral-space propagation (cθ, cσ)

### Velocities computed in SPROSD

`SPROSD` computes the spectral-space propagation velocities:

- `CAS(IS, ID)` — sigma velocity (frequency shift due to current/depth) `[file=src/swancom5.ftn line=1127-1135]`
- `CAD(IS, ID)` — theta velocity (refraction)
- Formula assembly at `[file=src/swancom5.ftn line=1602-1624]`
- Gradient terms (depth/current spatial derivatives) at `[file=src/swancom5.ftn line=1486-1512]`, `[file=src/swancom5.ftn line=1571-1572]`

### Coupling into the geographic sweep

`SWOMPU` calls `SPROSD` *before* `ACTION` so that spectral velocities are ready when the matrix is assembled:

- `SPROSD` call: `[file=src/swancom1.ftn line=3384-3393]`
- `ACTION` then inserts:
  - sigma velocity via `STRSSI` (implicit) / `STRSSB` (explicit) — `[file=src/swancom1.ftn line=5437-5480]`
  - theta velocity via `STRSD` / `SWFLXD`

So the per-grid-point matrix combines:
- (cx, cy) → `STRSXY` (BSBT)
- cσ → `STRSSI` or `STRSSB` (implicit/explicit choice)
- cθ → `STRSD`/`SWFLXD`

into a single linear system, then solved via the dispatched solver above.

## D. Action density limiter

### Two limiter forms

**PHILIM**:
- Defined at `[file=src/swancom1.ftn line=7857]`
- Clamp magnitude formula:
  ```
  DAC2MX = ABS((PNUMS(20) * 0.0081) / (2 * SPCSIG(IS) * KWAVE(IS,1)**3 * CGO(IS,1)))
  ```
  at `[file=src/swancom1.ftn line=7978-7979]`
- `PNUMS(20)` is the limiter coefficient (`SET LIMITER` command), default 0.1.

**HJ 제한기 HJLIM**:

HJLIM은 정렬 격자의 비정상 Janssen 풍입력 경로에서 선택한다. `PNUMS(20)`은 제한량 계수이다. 이를 HJLIM 선택 번호로 해석하지 않는다. 정렬 격자는 `src/swancom1.ftn:3791–3792`의 `IF (PNUMS(20).LT.100.) THEN` 안에서 `IF (IWIND.NE.4 .OR. NSTATC.NE.1) THEN`이면 PHILIM을 호출하고 반대 분기에서 HJLIM을 호출한다. 비정렬 호출 원문은 `src/SwanCompUnstruc.ftn90:1302`의 `if ( PNUMS(20) < 100. ) call PHILIM ( ac2, ac2old, cgo, kwave, spcsig, anybin, islmin, nflim, qbloc )`이다.
- Defined at `[file=src/swancom1.ftn line=8004]`
- Clamp formula uses friction velocity `UFRIC_VEL`:
  ```
  DAC2MX = (C_HJ * UFRIC_VEL) / (SPCSIG**3 * KWAVE)
  ```
  at `[file=src/swancom1.ftn line=8115-8121]`

### Clamping logic

Both limiters apply:
- Upper bound: `AC2 ≤ AC2OLD + DAC2MX` `[file=src/swancom1.ftn line=7981-7984]`
- Lower bound (only if not breaking — `QB_LOC < PNUMS(28)`): `AC2 ≥ AC2OLD - DAC2MX` `[file=src/swancom1.ftn line=7988-7993]`

This prevents runaway from wind input or numerical noise but allows breaking-driven dissipation to proceed.

### When applied

Per grid point, per sweep, **after** the linear solve and **after** optional `RESCALE`:
- `[file=src/swancom1.ftn line=3753-3755]` (post-solve)
- `[file=src/swancom1.ftn line=3791-3808]` (post-rescale)

So the limiter sees the new AC2 from the linear system and bounds it before the next sweep neighbor reads it.

## E. Convergence / iteration control

### 기본 정지 기준 SWSTPC

기본 `PNUMS(21)=1`은 SWSTPC이다. SACCUR는 별도 선택 경로이다. 기본 수렴점 비율은 99.50%이다. 실제 HS 조건은 절대 변화 조건 또는 상대 변화·곡률 결합 조건이다. `src/swanmain.ftn:1227`의 원문은 `PNUMS(4)  = 99.50`이다. `src/swancom1.ftn:2270–2277`의 원문은 `IF (PNUMS(21).EQ.0.) THEN`, `CALL SACCUR (COMPDA(1,JDP2),KGRPNT          ,`, `ELSE IF (PNUMS(21).EQ.1.) THEN`이다.

일반 STOPC의 파고 조건은 절대 차이 충족 또는 상대 차이와 곡률의 동시 충족이다. `src/swancom1.ftn:9874–9875`의 원문은 `LCONV = ( HSABS.LE.PNUMS(2) .OR.`와 `&                     (HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)) )`이다. 일반 STOPC에는 기본값 1000.인 두 조건이 남아 있다. 정렬 CURVT는 평균 각주파수 곡률에 적용된다. 비정렬 CURVT는 주기 곡률에 적용된다. `src/swanpre1.ftn:1948–1949`의 원문은 `CALL INREAL ('DTABS'  , PNUMS(3) , 'STA', 1000.)`와 `CALL INREAL ('CURVT'  , PNUMS(16), 'STA', 1000.)`이다. [R8:T1-003·T1-004](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).

### 별도 선택 기준 SACCUR

정렬 TMREL·TMOVAL은 평균 각주파수 차이이다. 비정렬 경로는 주기 차이이다. `src/swancom1.ftn:4840–4841`의 원문은 `IF ( (TMREL .LE. PNUMS(1) .OR. TMOVAL .LE. PNUMS(16)) .AND.`와 `&         (HSREL .LE. PNUMS(1) .OR. HSOVAL .LE. PNUMS(15)) ) THEN`이다. 식 (3.22)·(3.23)을 현재 ACCUR의 구현식으로 쓰지 않는다. [R8:T1-015](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).

### Stopping check

After each full 4-sweep iteration, in `SWCOMP`:
```fortran
IF ( (ITER.NE.1 .OR. PNUMS(21).EQ.0.) .AND.
&                                      ACCUR.GE.PNUMS(4) ) GOTO 470
```
원문 위치는 `src/swancom1.ftn:2352–2353`이다. 첫 반복에는 STOPC의 수렴 종료를 적용하지 않는다. [R8:T1-006](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).

일반 STOPC의 기본 합격점 비율은 99.5%이다. GEN4 입력과 IGEN=4의 ACCUR 전환 경로는 99%를 설정한다. `src/swanmain.ftn:1227`의 원문은 `PNUMS(4)  = 99.50`이다. `src/swanpre1.ftn:3107`의 원문은 `PNUMS(4) = 99.`이다. [R8:T1-002](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).

### Linear-solver convergence (separate)

SIP의 상대 잔차 기준과 기본 `REPS=1.E-4`, `MAXIT=20`은 swanuse PDF 95쪽 / 인쇄 87쪽에 명시되어 있다. 코드는 갱신 전 잔차의 2-norm을 만든다. `src/swancom1.ftn:8854`의 `IF ( RNORM.GT.UNDFLW**2 .AND. RNORM.GT.EPSLIN ) ICONV = 0`으로 반복 여부를 정하고 `ICONV.EQ.0` 종료 시 `AC2OLD`로 복구한다.

SWSOR는 $\omega=0.8$의 완화 Gauss–Seidel 갱신을 구현한다. 이 값은 과소이완이다. `src/swancom1.ftn:9036`의 원문은 `PARAMETER (OMEG=0.8)`이다. 전 소스의 `call\s+swsor` 검색은 0건이다. 스펙트럼 SWSOR의 검사량은 방정식 잔차가 아니라 최대 갱신량이다. `src/swancom1.ftn:9258–9260,9364,9372`의 원문은 `RES = ABS(AC2(ID,IS,KCGRD(1)) - AC2I)`, `RESM  = RES`, `IF ( RESM.GT.REPS ) ICONV = 0`, `AC2(:,:,KCGRD(1)) = AC2OLD(:,:)`이다. swanuse의 SETUP SOR는 수위 상승을 푸는 별도 해법이다. [R1:TN-172–175](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론).

## Decision Guide — what knob to turn for which symptom

| Symptom | Likely cause | Code-level knob |
|---------|--------------|-----------------|
| 정상 수렴점 비율 | 일반 STOPC 기본값은 99.5%이다. | `src/swanmain.ftn:1227` `PNUMS(4)  = 99.50` |
| Spurious peaks at high frequency | limiter too loose | reduce `PNUMS(20)` (`SET LIMITER`) below default 0.1 |
| Solver fails (NaN, "matrix singular") | high current + implicit sigma | force `SIGEXPL` path or check current input grid |
| Long-period swell underdamped | BSBT diffusion too low | switch to `PROPAGATION SORDUP` or accept extra dissipation |
| Wave height runaway under stiff wind | both limiters off | check `SET LIMITER` and `WCAP` are actually on |

## Working Rules

1. `AC2` is the variable holding the answer at the end of a sweep — debugging dumps should target `AC2(:,:,POINT_INDEX)`.
2. Dumping the per-point matrix `IMATDA/IMATRA/IMATLA/IMATUA` before solver dispatch reveals coefficient signs (positive diagonal = stable, negative = expect failure).
3. The limiter operates **per spectral cell** — clamping is independent for each `(IS, ID)` pair. A limiter event at one cell doesn't propagate.
4. `SWCOMP` is the inner of the two-level loop. To debug a specific time step in nonstationary, inject prints inside `SWCOMP` keyed on `IT == target_step`.

## Common Pitfalls

- **Confusing `ACCUR` (global %) with `RNORM` (linear-solver residual)** — they measure different things. Both can converge while the other diverges.
- **Reading `AC1` thinking it's the answer** — it's the previous time step. `AC2` is current.
- **Running stationary with `MODE NONSTAT` or vice versa** — `SWCOMP` handles both but the time-term contribution from `AC1` is wrong if mode/COMPUTE mismatch.
- **Implicit sigma path under high refraction** — `SWSIP` can stall. Switch to explicit `SIGEXPL` and accept smaller time step.

## Next expansion

- `SWSIP` solver internals (preconditioning, smoothing).
- `SOLMT1` cyclic tri-diagonal for current case (full algorithm).
- `STRSD/SWFLXD` theta-direction flux computation in detail.
- Source-term integrators (separate `swan-source-term-implementation.md` note).
- Time-stepping in unstructured path (`SwanCompUnstruc`).

## References

### Source files (Codex deep scan, 2026-05-06)

- `src/swancom1.ftn` — `SWCOMP`, `SWOMPU`, `ACTION`, `SACCUR`, `SWSTPC`, `PHILIM`, `HJLIM`, `SWSIP`, `SWSOR`.
- `src/swancom5.ftn` — `STRSXY`, `STRSD`, `STRSSI`, `STRSSB`, `SWFLXD`, `SPROSD`.
- `src/swanmain.ftn` — outer time-step loop, structured/unstructured dispatch.
- Inventory of all subroutines: `[file=models/swan/manuals/refs/subroutines.md]`.

### Manual cross-reference

- `[file=pdf:swan:swantech]` ch.3 (Numerical approaches), pages 79–100:
  - 3.1 Discretization in geographic space (BSBT, sweeping)
  - 3.2 Note on choice of scheme (BSBT vs SORDUP vs SecondOrder)
  - 3.5 Sweeping algorithm illustration
  - 3.7 Action density limiter
- `[file=website:swan:node29]` — Numerics overview command.
- `[file=website:swan:node34]` — Lock-up (stationary convergence behavior at boundaries).

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex source scan | 30+ file:line citations across `swancom1.ftn`, `swancom5.ftn`, `swanmain.ftn` |
| Coverage | iteration loop, sweep loop, BSBT assembly, solver dispatch, spectral coupling, limiters, convergence — main solver only |
| Out of scope (companion notes) | unstructured path, source-term integrators (Sin/Sds/Snl), boundary `SWBOUN` internals, output writers |
| Review status | 2026-10-13 recovery 대조 보고서 R1–R8 반영 |

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-003 | 문서 식 (2.3) | swantech PDF 16쪽 / 인쇄 8쪽, (2.3): $\sigma=\sqrt{g\lvert\vec k\rvert\tanh(\lvert\vec k\rvert d)}$ | `src/swanser.ftn:713–715`: `C     = SQRT(GRAV*D/(SND2+1./(1.+0.666*SND2+0.445*SND2**2`; `&                                  -0.105*SND2**3+0.272*SND2**4)))`; `K(IS) = SIG(IS)/C`.<br>웹 [수정 이력](../raw/manuals/website/modifications/modifications.htm):596–598은 `Pade approximation for the wave celerity`를 명시한다. | C 문서 누락 | KSCIP1은 분산 관계를 구간별 근사로 계산한다. Padé 근사의 존재는 웹 수정 이력에도 있다. C는 swantech 식 (2.3)에 `IF (SND .GE. 2.5) THEN`, `ELSE IF (SND.LT.1.E-6) THEN`과 유한 수심 유리식이 없는 점으로 한정한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) [10-13 전수 검증 정정]
| R1:TN-073 | Thomas 해법 선택 조건 | swantech PDF 90쪽 / 인쇄 82쪽: “in the absence of mean current there are no shifts in the frequency” | `src/swancom1.ftn:3681–3682`: `ELSEIF ( (DYNDEP .OR. ICUR .EQ. 1) .AND.`; `&           PNUMS(8).NE.0.                 ) THEN`.<br>swanuse PDF 94쪽–95쪽 / 인쇄 86쪽–87쪽의 SIGIMPL은 `of currents or time varying depth`를 적용 조건으로 적는다. swantech PDF 18쪽 식 (2.13)에도 $\partial d/\partial t$가 있다. | C 문서 누락 | 수심 시간변화에 의한 주파수 이동은 다른 매뉴얼과 swantech 식 (2.13)에 이미 있다. C는 swantech §3.3의 Thomas 선택 설명이 정적 수심 조건과 주파수 해법 선택을 생략한 점이다. 실제 분기는 `ELSEIF ( (DYNDEP .OR. ICUR .EQ. 1) .AND.`; `&           PNUMS(8).NE.0.                 ) THEN`이다. `IREFR.EQ.0 .AND. ITFRE.EQ.0`이면 그보다 앞에서 대각 나눗셈만 한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-074 | 문서 식 (3.21) | swantech PDF 90쪽 / 인쇄 82쪽, (3.21): $H_{m0}=4\sqrt{m_0},\ T_{m01}=2\pi m_0/m_1,\ m_j=\int_0^\infty\int_0^{2\pi}\sigma^jE\,d\sigma d\theta$ | `src/swancom1.ftn:9800–9813`: `DO IS = 1, MSC`; `ACS2  = SPCSIG(IS)**2 * AC2(ID,IS,INDX)`; `HSACC2(INDX) = MAX ( 1.E-20 , 4.*SQRT(XMOM0) )`; `SACC2 (INDX) = MAX ( 1.E-20 , (XMOM1/XMOM0) )`. | C 문서 누락 | C는 swantech §3.4의 연속 모멘트 정의에 정지 검사용 유한 주파수 합과 꼬리 생략이 구분되지 않은 점이다. SWSTPC는 계산 주파수만 합산한다. `SACC2`는 주기가 아니라 평균 각주파수이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-075 | 문서 식 (3.22) | swantech PDF 91쪽 / 인쇄 83쪽, (3.22): $\lvert\Delta H_{m0}^s\rvert/H_{m0}^{s-1}<\varepsilon_H^r\ \mathrm{or}\ \lvert\Delta H_{m0}^s\rvert<\varepsilon_H^a$; $\Delta Q^s=Q^s-Q^{s-1}$ | `src/swancom1.ftn:9852–9853`: `HSABS = ABS ( HSACC2(INDX) - HSACC1(INDX) )`; `HSREL = HSABS / HSACC2(INDX)`.<br>swantech PDF 92쪽 / 인쇄 84쪽는 식 (3.22)를 `retained in addition to the stricter criterion (3.26)`라고 적는다. | B 문서 오기 | 식 (3.22)는 구식 기준 설명에 등장하며 PDF 92에서 개선 기준의 약한 보조 조건으로 다시 유지된다. 현행 STOPC는 현재 파고로 나누고 `.LE.`로 비교한다. B는 swantech에 재사용된 식의 이전 파고 분모와 현행 구현의 차이로 한정한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-077 | 정지 조건 기본값 | swantech PDF 91쪽 / 인쇄 83쪽, 기본값: $\varepsilon_H^r=\varepsilon_T^r=0.02,\ \varepsilon_H^a=0.02\,{\rm m},\ \varepsilon_T^a=0.2\,{\rm s}$; 습윤점 98%. swantech PDF 92쪽 / 인쇄 84쪽: 곡률 기준 습윤점 99% | `src/swanmain.ftn:1219,1224,1227,1292–1293`: `PNUMS(1)  = 0.01`; `PNUMS(3)  = 1000.`; `PNUMS(4)  = 99.50`; `PNUMS(15) = 0.005`; `PNUMS(16) = 1000.`; 6506·6508·6511의 파고 절대오차는 0.005·0.01·0.05이다.<br>swanuse PDF 94쪽 / 인쇄 86쪽의 `[dabs]`, `[drel]`, `[curvat]`, `[npnts]` 기본값. `src/swanmain.ftn:6503–6512`는 `PNUMS(2)=-1.`일 때만 파고 절대 허용값을 정한다. | B 문서 오기 | PDF 91의 0.02·0.2·98%는 옛 기준의 설명이다. 이를 현행 기본값으로 옮기지 않는다. B는 PDF 92의 기본 곡률 기준 99%가 현행 99.50%와 다른 점에 한정한다. swanuse PDF 94쪽는 현행 일반 기본값 0.005 m·0.01·0.005·99.5%를 적는다. 코드의 파고 절대 허용값은 미지정일 때 일반 0.005 m, `ITRIAD=3`에서 0.01 m이다. QC의 0.05는 입사파고에 곱하는 무차원 계수이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-080 | 문서 식 (3.26) | swantech PDF 92쪽 / 인쇄 84쪽, (3.26): $\lvert H^s-(H^{s-1}+H^{s-2})+H^{s-3}\rvert/(2H^s)<\varepsilon_C,\ s=3,4,\cdots$ | `src/swancom1.ftn:9859`의 `HSCURV`; 9874–9875: `LCONV = ( HSABS.LE.PNUMS(2) .OR.`; `&                     (HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)) )`.<br>swanuse PDF 93쪽 / 인쇄 85쪽 및 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):220–246은 상대 변화·곡률의 AND와 절대 변화의 OR를 구분한다. | B 문서 오기 | 곡률 값의 식은 같다. B는 swantech §3.4의 두 기준 동시 만족 설명에 한정한다. 현행 파고 조건은 `LCONV = ( HSABS.LE.PNUMS(2) .OR.`; `&                     (HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)) )`의 부분식이다. 일반 경로는 여기에 주기 조건도 AND로 결합한다. swanuse의 파고 조건 설명은 코드와 대응한다. git `2980d1a`에서 이 파고 논리식 변경을 확인했다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-081 | 주기 기준의 존속 | swantech PDF 91쪽–92쪽 / 인쇄 83쪽–84쪽: “$T_{m01}$ has been abandoned as a convergence measure” | `src/swancom1.ftn:9877–9878`: `( TMCURV.LE.PNUMS(16) .AND.`; `&                     (TMREL.LE.PNUMS(1) .OR. TMABS.LE.PNUMS(3)) )`.<br>웹 [수정 이력](../raw/manuals/website/modifications/modifications.htm):1308,1351–1353은 주기 곡률의 추가와 선택 사용을 적는다. swanuse PDF 141쪽의 명령 도식에도 `[dtabs] [curvt]`가 있다. | C 문서 누락 | 주기 검사 존재는 웹 수정 이력과 swanuse 명령 도식에 있다. C는 swantech §3.4의 주기 기준 폐기 설명에 선택 조건이 없는 점이다. 현행 일반 STOPC에는 주기 검사가 남는다. 기본 1000 값은 이 검사를 느슨하게 한다. 정렬 곡률은 평균 각주파수로 계산하고 비정렬 곡률은 주기로 계산한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-082 | 문서 식 (3.22)·(3.23) | swantech PDF 92쪽 / 인쇄 84쪽: 이전 (3.22)·(3.23)은 “obsolete” | `src/swancom1.ftn:2270–2277`: `IF (PNUMS(21).EQ.0.) THEN`; `CALL SACCUR (COMPDA(1,JDP2),KGRPNT          ,`; `ELSE IF (PNUMS(21).EQ.1.) THEN`. SACCUR 4840–4841: `IF ( (TMREL .LE. PNUMS(1) .OR. TMOVAL .LE. PNUMS(16)) .AND.`.<br>swanuse PDF 141쪽 / 인쇄 133쪽 및 웹 [명령 도식](../raw/manuals/website/online_doc/swanuse/node49.html):305–307은 `ACCUR [drel] [dhoval] [dtoval] [npnts]`를 명시한다. | C 문서 누락 | `obsolete`는 기능 제거를 뜻하지 않는다. ACCUR 선택은 swanuse 명령 도식에도 남아 있다. C는 swantech 식 (3.22)·(3.23)이 현행 SACCUR의 평균 각주파수 변화와 영역 평균 정규화 조건을 적지 않는 점이다. 호출 조건은 `IF (PNUMS(21).EQ.0.) THEN`이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-087 | 문서 식 (3.28) | swantech PDF 99쪽 / 인쇄 91쪽, (3.28): $N^s=N^{s-1}+(\Delta N_{\rm bin}/\lvert\Delta N_{\rm bin}\rvert)\min\{\lvert\Delta N_{\rm bin}\rvert,\Delta N\}$ | `src/swancom1.ftn:7976,7981–7983,7988–7992`: `IF (MSC.GT.3) THEN`; `AC2(ID,IS,KCGRD(1))=AC2OLD(ID,IS)+DAC2MX`; `IF (QB_LOC.LT.PNUMS(28)) THEN`; `AC2(ID,IS,KCGRD(1))=AC2OLD(ID,IS)-DAC2MX`.<br>swanuse의 `[qb]` 설명과 웹 [물리 명령](../raw/manuals/website/online_doc/swanuse/node28.html):2254–2264. | C 문서 누락 | C는 swantech 식 (3.28)에 PHILIM의 선택 bin·`IF (MSC.GT.3) THEN`·감소 제한의 `IF (QB_LOC.LT.PNUMS(28)) THEN` 조건이 없는 점이다. 쇄파율에 따라 제한기를 끄는 선택 자체는 swanuse에도 있다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-088 | HJLIM 선택 조건 | swantech PDF 99쪽 / 인쇄 91쪽: “when the physical wind formulation of Janssen (1989,1991a) is applied ... the original limiter of Hersbach and Janssen (1999) is employed.” | `src/swancom1.ftn:3791–3805`: `IF (PNUMS(20).LT.100.) THEN`; `IF (IWIND.NE.4 .OR. NSTATC.NE.1) THEN`; `CALL PHILIM` 경로와 `CALL HJLIM` 경로를 나눈다. `src/SwanCompUnstruc.ftn90:1302`: `if ( PNUMS(20) < 100. ) call PHILIM ( ac2, ac2old, cgo, kwave, spcsig, anybin, islmin, nflim, qbloc )`.<br>웹 [수정 이력](../raw/manuals/website/modifications/modifications.htm):1338–1339은 `no use of the Hersbach and Janssen limiter in the case of stationary runs`를 적는다. | C 문서 누락 | 정상 계산의 HJLIM 제외는 웹 수정 이력에 이미 있다. C는 swantech §3.7.2가 이 조건과 격자별 경로를 구분하지 않는 점이다. 정렬 격자는 `PNUMS(20).LT.100.` 안에서 `IWIND.NE.4 .OR. NSTATC.NE.1`이면 PHILIM을 호출하고 반대 분기에서 HJLIM을 호출한다. 비정렬 호출은 PHILIM이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-171 | 문서 식 (6.3) | swantech PDF 136쪽 / 인쇄 128쪽, (6.3): $U\vec N^{s+1}=L^{-1}K\vec N^s+L^{-1}\vec b$ | `src/swancom1.ftn:8737–8739,8848–8850`: `RES(ID,IS) = (RES(ID,IS) - CMAT5L(ID,IS)*RES(ID ,ISM)`; `RES(ID,IS) = RES(ID,IS) - CMAT6U(ID,IS)*RES(ID ,ISP)`; `AC2(ID,IS,KCGRD(1)) = AC2(ID,IS,KCGRD(1)) + RES(ID,IS)`. | F 표기 차이 | 해석: 코드는 $LU\delta N=b-AN^s,\ N^{s+1}=N^s+\delta N$를 푼다. $LU=A+K$를 대입하면 문서 식이 된다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-172 | SIP 반복·정지·복구 | swantech PDF 136쪽 / 인쇄 128쪽: “until convergence is reached”. 수치 문턱 식은 없다 | `src/swancom1.ftn:8638–8639,8649,8655,8854`: `EPSLIN = REPS*BNORM`; `UEPS   = 1000.*UNDFLW*BNORM`; `EPSLIN = UEPS`; `IF ( ICONV.EQ.0 .AND. IT.LT.MAXIT ) THEN`; `IF ( RNORM.GT.UNDFLW**2 .AND. RNORM.GT.EPSLIN ) ICONV = 0`.<br>swanuse PDF 95쪽 / 인쇄 87쪽 및 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):555–639. `src/swancom1.ftn:8808–8813`의 큰 잔차 중단과 제곱근. | C 문서 누락 | SIP의 상대 잔차 기준과 기본 `REPS=1.E-4`, `MAXIT=20`은 swanuse에 명시되어 있다. C는 swantech §6.1에 문턱 하한 보강·큰 잔차 중단·실패 복구가 없는 점이다. 코드는 갱신 전 잔차의 2-norm을 만든다. `IF ( RNORM.GT.UNDFLW**2 .AND. RNORM.GT.EPSLIN ) ICONV = 0`으로 반복 여부를 정하고 `ICONV.EQ.0` 종료 시 `AC2OLD`로 복구한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-173 | SWSOR 존재와 호출 | swantech PDF 136쪽 / 인쇄 128쪽, §6.2: “This section is under preparation.” | `src/swancom1.ftn:9036`: `PARAMETER (OMEG=0.8)`; 9255–9256: `AC2I = AC2I*OMEG*INVMDA(ID,IS)+`; `&                                     (1.-OMEG)*AC2(ID,IS,KCGRD(1))`.<br>swanuse PDF 95쪽 및 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):521–524,589–607의 SETUP·수위 상승 정지식. | C 문서 누락 | SWSOR는 $\omega=0.8$의 완화 Gauss–Seidel 갱신을 구현한다. 이 값은 과소이완이다. 전 소스의 `call\s+swsor` 검색은 0건이다. C는 swantech §6.2의 스펙트럼 해법 설명 누락이다. swanuse의 SETUP SOR는 수위 상승을 푸는 별도 해법이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-174 | SWSOR 정지·복구 | swantech PDF 136쪽 / 인쇄 128쪽, §6.2에는 정지식이 없다 | `src/swancom1.ftn:9258–9260,9364,9372`: `RES = ABS(AC2(ID,IS,KCGRD(1)) - AC2I)`; `RESM  = RES`; `IF ( RESM.GT.REPS ) ICONV = 0`; `AC2(:,:,KCGRD(1)) = AC2OLD(:,:)`.<br>swanuse PDF 95쪽 및 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):589–607의 SOR 미지수는 수위 상승이다. | C 문서 누락 | 스펙트럼 SWSOR의 검사량은 방정식 잔차가 아니라 최대 갱신량이다. SIP의 상대 잔차 문턱과 다르다. 상한·큰 갱신량으로 실패하면 이전 값을 복구한다. C는 swantech §6.2에 이 정지·복구 절차가 없는 점이다. swanuse의 수위 상승 SOR 정지식을 이 루틴의 설명으로 대체하지 않는다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-175 | SIP 고정 ALFA | swantech PDF 135쪽 / 인쇄 127쪽: Stone의 보간으로 $K\phi\approx0$이 되도록 보정한다는 설명 | `src/swancom1.ftn:8438`: `PARAMETER (ALFA=0.0,SMALL=1.E-15)`; 8620–8621의 `P1 = ALFA*CMATUA(ID ,ISM)`, `P2 = ALFA*CMAT6U(IDM,IS )`. | C 문서 누락 | 현재 고정값은 보정 인자 0이다. 구현 골격은 SIP이지만 활성 인수분해는 Stone 교차 보정 없는 ILU 형태이다. 문서는 이 고정값과 작은 대각 보강값을 적지 않는다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-001 | 분산 관계의 심해·천해 분기와 유한 수심 근사 | — | `src/swanser.ftn:699–719`: `IF (SND .GE. 2.5) THEN`; `ELSE IF (SND.LT.1.E-6) THEN`; 유한 수심 유리식은 TN-003에 인용했다.<br>웹 [수정 이력](../raw/manuals/website/modifications/modifications.htm):596–598은 위상속도의 Padé 근사를 설명한다. | C 문서 누락 | 분산 관계 근사의 존재는 웹 수정 이력에도 있다. C는 swantech 식 (2.3)에 KSCIP1의 심해·극천해 분기 문턱과 유한 수심 근사 계수가 없는 점으로 한정한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) [10-13 전수 검증 정정]
| R1:TC-002 | 쌍곡선 함수 인자의 상한과 건조 stencil 처리 | — | `src/swancom5.ftn:1577–1579`: `IF ( KD1 .GT. 30.0 ) KD1 = 30.`; `VLSINH = SINH (2.* KD1 )`; `src/SwanPropvelS.ftn90:171`: `if ( dloc(1) <= DEPMIN .or. dloc(2) <= DEPMIN .or. dloc(3) <= DEPMIN ) return`. | C 문서 누락 | 큰 $kd$의 함수 평가를 제한한다. 비정렬 stencil에 건조점이 있으면 먼저 0으로 초기화한 스펙트럼 속도를 반환한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-003 | 파수 기울기로 계산하는 비정렬 기본 굴절 | — | `src/SwanPropvelS.ftn90:259–269`: `cd(1) = -cgo(is,1) / kwave(is,1)`; `cd(2) = cd(1) * dkdx(is)`; `cd(3) = cd(1) * dkdy(is)`; `cad(id,is) = esin(id)*cd(2) - ecos(id)*cd(3)`.<br>swanuse PDF 141쪽 / 인쇄 133쪽의 `DIRimpl [cdd] DEP\|WNUM`; `src/SwanGradDepthorK.ftn90:348–371`. | C 문서 누락 | 고정 $\sigma$에서 $\nabla c=-\sigma\nabla k/k^2$를 쓰면 swantech 식 (3.43)과 연속식은 같다. 파수 기울기 선택 WNUM은 swanuse 명령 도식에도 있다. C는 swantech §3.8의 정렬 격자 설명에 비정렬 중심 쌍대 제어체적 기울기 경로가 없는 점이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-004 | 스펙트럼 속도의 주파수별 감쇠와 주파수 CFL 제한 | — | `src/SwanPropvelS.ftn90:223,230,301,304`: `fac2 = alpha * FRINTF * spcsig(is)`; `if ( abs(cas(id,is)) > fac ) cas(id,is) = cas(id,is) * fac / abs(cas(id,is))`; `fac = min(1.,(spcsig(is)/frlim)**pp)`; `cad(id,is) = fac*cad(id,is)`; `src/swanmain.ftn:1319–1332`의 기본값 $f_{\rm lim}=0.2,\ p=2,\alpha_\sigma=\alpha_\theta=0.9$와 세 제한 스위치 0.<br>swanuse PDF 95·141쪽; 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):488–517. | C 문서 누락 | CSIGMA의 역할·기본 비활성·활성화 계수 0.9는 swanuse PDF 95쪽에 있다. REFRLIM도 PDF 141 명령 도식에 있다. C는 swantech §3.8에 저주파 감쇠 `fac = min(1.,(spcsig(is)/frlim)**pp)`와 주파수 CFL 구현식·선택 조건을 함께 적지 않은 점이다. 세 제한 스위치는 기본 0이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-005 | 구면 굴절 보정과 제한기의 적용 순서 | — | `src/SwanPropvelS.ftn90:286,294,312`: `cad(id,is) = cad(id,is) - cd(2)*(cax(id,is,1)*ecos(id) + cay(id,is,1)*esin(id))`; `if ( int(PNUMS(29)) == 1 ) then`; `if ( int(PNUMS(35)) == 1 ) then`; 정렬 경로 `src/swancom1.ftn:3384,3402`의 `SPROSD` 다음 `DSPHER` 호출. | C 문서 누락 | 비정렬 경로는 구면 보정 뒤 제한한다. 정렬 경로는 제한 뒤 구면 보정을 더한다. 최종 방향 속도에 같은 상한을 보장한다고 쓰지 않는다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-006 | 비정렬 기울기의 건조점 처리와 비활성 수심비 조건 | — | `src/SwanGradDepthorK.ftn90:208,233–234,360,385–386`: `!if ( dpmax > drat * dpmin ) goto 10`; `10    dhdx = 0.`; `dhdy = 0.`; `!if ( dpmax > drat * dpmin ) goto 30`; `30    dkdx = 0.`; `src/SwanGradVel.ftn90:217,246–249`에도 같은 주석 조건과 영 기울기 반환이 있다. | C 문서 누락 | 건조 셀을 만나는 경로는 기울기를 0으로 한다. `drat=5` 조건은 일반 주석이므로 switch.pl이 활성화하지 않는다. 이를 현행 수심 기울기 제한기로 적으면 안 된다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-022 | 명시 주파수 수송과 CFL에 따른 bin 제거 | — | `src/swancom1.ftn:5451–5461`: `ELSE IF ( INT(PNUMS(8)) .EQ. 2 ) THEN`와 `CALL STRSSB`; `src/swancom5.ftn:3644,3670,3674,3726,3730`: `CFLMAX = PNUMS(19)`; `IF ( CFLCEN .GT. CFLMAX ) THEN`; `ANYBLK(ID,IS) = .TRUE.`; `FSA  = ( FRGHT - FLEFT ) / DS`; `IMATRA(ID,IS) = IMATRA(ID,IS) - FSA`.<br>swanuse PDF 141쪽 / 인쇄 133쪽의 `SIGEXpl [css] [cfl]`; `src/swancom1.ftn:5437–5461`의 호출 조건. | C 문서 누락 | SIGEXpl 선택은 swanuse PDF 141쪽 명령 도식에 있다. C는 swantech §3.2·§3.3에 CFL에 따른 bin 제거의 구현 조건이 없는 점이다. `PNUMS(19)=0.5*sqrt(2.)`가 기본 상한이다. `IF ( CFLCEN .GT. CFLMAX ) THEN`이면 ANYBLK를 켠다. SOLMT1은 해당 행의 대각을 1로, 우변과 방향 이웃 계수를 0으로 둔다. 이 의도된 제거와 TC-023의 분모 결함 후보를 구분한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-024 | 정상 첫 반복의 공간 예측값 | — | `src/swancom1.ftn:3460,3465–3470`: `IF (ICOND.NE.4 .AND. ITER.EQ.1 .AND. NSTATC.EQ.0) THEN`와 `CALL SPREDT`; `src/swancom5.ftn:4584–4585,4594–4598`: `WEIG1 = CDEN/CNUM`; `WEIG2 = 1. - WEIG1`; `FAC_A = TCF1 * WEIG1 * AC2(ID,IS,KCGRD(2))`; `FAC_B = TCF2 * WEIG2 * AC2(ID,IS,KCGRD(3))`; `AC2(ID,IS,KCGRD(1)) = MAX ( 0. , (FAC_A + FAC_B))`. | C 문서 누락 | `IF (ICOND.NE.4 .AND. ITER.EQ.1 .AND. NSTATC.EQ.0) THEN`에서 LPREDT를 켠다. 이후 `IF (LPREDT) THEN`에서 SPREDT를 호출한다. 정상 첫 반복의 해당 경로는 상류 두 점의 가중합을 공간 예측값으로 쓴다. 곡선 좌표 CCURV는 4514–4568행의 별도 기하식을 쓴다. C는 swantech에 이 공간 예측 절차가 없는 점이다. 제2세대 원천항 초기 추정과 구분한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-025 | 음수 제거 비율의 작은 분모 보호 | — | `src/swancom1.ftn:8303–8304`: `IF ( ATOTP .LT. 1.E-15 ) ATOTP = 1.E-15`; `FACTOR = ATOT / ATOTP`.<br>`src/swancom1.ftn:8302–8315`의 음수 존재·비음수 배율 조건. | C 문서 누락 | `IF (NEGVAL) THEN` 안에서 양의 작용밀도 합이 $10^{-15}$보다 작으면 분모를 올린다. 이후 `IF ( FACTOR .GE. 0. ) THEN`인 경우 양의 밀도를 재조정한다. 이 작은 분모 조건에서는 TN-064의 엄밀한 총량 보존 비율과 달라진다. C는 swantech §3.2.4의 보존적 제거식에 이 보호 조건이 없는 점이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R5:PN-083 | STOPC 경계값 | swanuse PDF 93쪽 / 인쇄 85쪽 `less than`, `more than` | `src/swancom1.ftn:9874` `LCONV = ( HSABS.LE.PNUMS(2) .OR.`, 2353 `ACCUR.GE.PNUMS(4) ) GOTO 470`. | B | 파고·주기·곡률 오차의 코드 비교는 `.LE.`이다. swantech PDF 91쪽–92쪽 식 (3.22)·(3.23)·(3.26)은 `<`를 명시한다. B는 이 경계값 차이에 한정한다. 만족 격자 비율의 코드 비교는 `.GE.`이며 문서의 `more than` 표현만으로 오기라고 단정하지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-084 | STOPC의 주기·첫 반복 | STOPC의 생략된 주기 조건과 첫 반복 조건. swanuse PDF 93쪽 / 인쇄 85쪽는 `significant wave height`의 수렴만 설명한다. | `src/swancom1.ftn:9877` `( TMCURV.LE.PNUMS(16) .AND.`, 2352 `IF ( (ITER.NE.1 .OR. PNUMS(21).EQ.0.) .AND.`. | C | 일반 STOPC는 파고와 주기 조건을 함께 검사한다. QC는 주기 조건을 쓰지 않는다. 첫 반복의 정확도 종료도 제한한다. swanuse PDF 141쪽 / 인쇄 133쪽·웹 `swanuse/node49.html:305`에는 주기 인수 문법이 있고 swantech PDF 91쪽–92쪽에는 주기 기준의 이력이 있다. 누락은 swanuse §4.5.5의 현 검사 동작 설명에 한정한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-090 | SIGIMPL EPS1 | swanuse PDF 93쪽 / 인쇄 85쪽의 인수 순서는 CSS·EPS2·OUTP·NITER다 | `src/swanpre1.ftn:2028` `CALL INREAL ('EPS1' , PNUMS(11), 'UNC', 0.)`. | C | 입력기는 CSS 다음에 EPS1을 추가로 읽는다. 문서의 위치 인수 순서는 실제 입력기와 다르다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-093 | SIP 수치 하한 | SIP 허용오차의 보정. swanuse PDF 95쪽 / 인쇄 87쪽의 EPS2 식에는 하한을 적지 않는다. | `src/swancom1.ftn:8639` `UEPS   = 1000.*UNDFLW*BNORM`, 8649 `EPSLIN = UEPS`. | C | SIP는 지나치게 작은 요청 허용오차를 내부 하한으로 올린다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-173 | DTABS/CURVT·ACCUR | swanuse PDF 141쪽 / 인쇄 133쪽 `[dtabs] [curvt]`, `ACCUR` | `src/swanpre1.ftn:1963` `PNUMS(21) = 0.`. | C | Appendix C는 주기 수렴 인수와 옛 ACCUR 선택을 싣는다. 본문 설명에 이 경로를 보충한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-174 | DEP/WNUM·REFRLIM·SIGEXPL | swanuse PDF 141쪽 / 인쇄 133쪽 `DEP\|WNUM`, `REFRLim`, `SIGEXpl` | `src/swancom5.ftn:1671` `FAC = MIN(1.,(SPCSIG(IS)/FRLIM)**PP)`. | C | REFRLIM의 주파수별 굴절 완화는 CTHETA의 CFL 제한과 다르다. SIGEXPL의 CFL 초기값은 √2/2다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R8:T1-002 | STOPC 기본 합격점 비율 | swantech PDF 92쪽·인쇄 84쪽은 “at least 99% of all wet grid points”라고 적는다. swanuse PDF 94쪽·인쇄 86쪽의 기본값은 “Default: [npnts] = 99.5 [−]”이다. `manual-notes/swan-tech-ch3-solution-iteration-limiter.md:143`은 이를 `npnts=99%`로 적었다 | `src/swanmain.ftn:1227` `PNUMS(4)  = 99.50`. GEN4 입력은 `src/swanpre1.ftn:3107` `PNUMS(4) = 99.`이다. `src/swanmain.ftn:6681–6688`은 `IF (IGEN.EQ.4) THEN` 안의 `IF (PNUMS(21).EQ.0.) THEN`에서 STOPC 전환과 함께 `PNUMS(4)  = 99.`를 설정한다. | B — 노트 오기 | 일반 STOPC의 기본 합격점 비율은 99.5%이다. GEN4 입력과 IGEN=4의 ACCUR 전환 경로는 99%를 설정한다. 기술 문서의 “at least 99%”만으로 현재 기본값을 99%라고 단정할 수 없다. B는 노트가 일반 기본값을 99%로 옮긴 오기에 한정한다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:T1-003 | STOPC의 주기 관련 선택 조건 | swantech PDF 91쪽·인쇄 83쪽은 제안된 개선 기준에서 “Tm01 has been abandoned as a convergence measure and only Hm0”라고 적는다. swanuse PDF 93쪽·인쇄 85쪽의 본문 구문은 DTABS·CURVT를 생략한다. 그러나 같은 책 PDF 141쪽·인쇄 133쪽과 `website/online_doc/swanuse/node49.html:305`은 `[dtabs] [curvt]`를 싣는다. `website/modifications/modifications.htm:1351–1353`은 “the curvature of Tm01 can be included as an option”이라고 명시한다 | `src/swanpre1.ftn:1948` `CALL INREAL ('DTABS'  , PNUMS(3) , 'STA', 1000.)`; `:1949` `CALL INREAL ('CURVT'  , PNUMS(16), 'STA', 1000.)`. 정렬 `src/swancom1.ftn:9873–9878`은 `IF ( IQCM.EQ.0 ) THEN`에서 `( TMCURV.LE.PNUMS(16) .AND.`와 `&                     (TMREL.LE.PNUMS(1) .OR. TMABS.LE.PNUMS(3)) )`를 파고 조건에 AND로 연결한다. `:9861–9863`은 SACC의 곡률을 계산한다. 비정렬 `src/SwanConvStopc.ftn90:208–225`는 주기의 곡률을 계산한다. | C — 본문 설명 누락 | DTABS·CURVT의 구문과 주기 곡률 선택 기능은 부록·웹에 있다. C는 swantech §3.4와 swanuse NUMERIC 본문의 선택 조건 설명 누락에 한정한다. 일반 STOPC에는 기본값 1000.인 두 조건이 남아 있다. 입력값을 강화하면 종료를 제한할 수 있다. 정렬 CURVT는 평균 각주파수 곡률에 적용된다. 비정렬 CURVT는 주기 곡률에 적용된다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:T1-004 | 곡률 조건을 우회하는 절대 Hs 차이 | swantech PDF 92쪽·인쇄 84쪽: “Condition (3.26) must be satisfied” 및 “the weaker criterion (3.22) is retained in addition to the stricter criterion (3.26)”. swanuse PDF 93쪽·인쇄 85쪽은 상대 변화와 곡률 조건 뒤에 “or the absolute change”를 적는다. 일반 STOPC의 파고 부분식은 | `src/swancom1.ftn:9874–9875` `LCONV = ( HSABS.LE.PNUMS(2) .OR.`와 `&                     (HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)) )`이다. 뒤의 `:9876–9878`에는 T1-003의 조건이 AND로 연결된다. 비정렬 `src/SwanConvStopc.ftn90:224`도 `lconv = ( hsabs <= PNUMS(2) .or. (hsabs <= hsrel .and. hscurv <= curvah) ) .and. &`이다. | B | 일반 STOPC의 파고 조건은 절대 차이 충족 또는 상대 차이와 곡률의 동시 충족이다. 파고 곡률은 모든 합격점의 필수 조건이 아니다. 이 OR 구조는 swanuse와 일치한다. B는 swantech의 곡률 필수 설명에 한정한다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:T1-005 | Hs 곡률의 저장 변수 표기 | swantech PDF 92쪽·인쇄 84쪽 이미지의 식 (3.26): $\frac{\lvert H_{m0}^{s}(i,j)-(H_{m0}^{s-1}(i,j)+H_{m0}^{s-2}(i,j))+H_{m0}^{s-3}(i,j)\rvert}{2H_{m0}^{s}(i,j)}<\varepsilon_{\mathrm C},\quad s=3,4,\cdots$ | `src/swancom1.ftn:9776–9777`은 HSACC0·HSACC1을 이전 반복값으로 옮긴다. `:9857` `HSDIFO       = HSDIFC(INDX)`; `:9858` `HSDIFC(INDX) = 0.5*( HSACC2(INDX) - HSACC0(INDX) )`; `:9859` `HSCURV       = ABS(HSDIFC(INDX) - HSDIFO)/HSACC2(INDX)`. | F | 현재 HSDIFC와 직전 HSDIFO의 차분을 전개하면 식 (3.26)의 좌변과 같다. 식의 반복 범위는 s=3,4,…이다. 이 F 판정은 좌변의 표기에 한정한다. 비교 경계는 T1-006을 따른다. 종료 논리는 T1-004를 따른다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:T1-006 | 정지 부등호·합격점 비율 경계 | swanuse PDF 93쪽·인쇄 85쪽: “less than [drel]” 및 “more than fraction [npnts]%”. swantech PDF 92쪽·인쇄 84쪽 식 (3.26)의 비교 기호는 `<`이다 | `src/swancom1.ftn:9875`은 `HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)`를 쓴다. `:9928` `ACCUR  = CEILING(REAL(IACCUR) * 10000. / REAL(WETGRD))/100.`. 종료 조건은 `:2352–2353` `IF ( (ITER.NE.1 .OR. PNUMS(21).EQ.0.) .AND.`와 `&                                      ACCUR.GE.PNUMS(4) ) GOTO 470`이다. 비정렬 `src/SwanConvStopc.ftn90:267`은 `if ( nwetp > 0. ) accur = ceiling(npacc*10000./nwetp)/100.`를 쓴다. `src/SwanCompUnstruc.ftn90:1487–1500`은 첫 반복을 제외하고 `if ( accur >= PNUMS(4) ) exit iterloop`를 검사한다. | B | STOPC의 개별 비교는 허용값과 같은 값도 허용한다. 이는 식 (3.26)의 엄격한 `<`와 다른 경계이다. 합격점 백분율은 0.01 퍼센트포인트 단위로 올려 npnts 이상인지 비교한다. 첫 반복에는 이 수렴 종료를 적용하지 않는다. B의 근거는 느슨한 산문만이 아니라 명시된 식의 비교 경계이다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:T1-007 | 최대 반복 수의 종료 시점 | swanuse PDF 94쪽·인쇄 86쪽은 최대 반복 수를 설명하며 “The computation stops when this number is exceeded.” 및 “moves to the next time step when this number is exceeded.”라고 적는다. swantech PDF 90쪽·인쇄 82쪽은 반복 범위를 s=1부터 s=S까지로 쓰고 최대 횟수가 “is reached”일 때 종료한다고 적는다 | `src/swancom1.ftn:1487` `DO 450 ITER = 1, ITERMX`; `:2355` `450  CONTINUE`. `src/SwanCompUnstruc.ftn90:671` `iterloop: do iter = 1, ITERMX`; `:1533` `enddo iterloop`. `src/swanpre1.ftn:932–935`는 정상 계산에 MXITST, 비정상 계산에 MXITNS를 ITERMX로 대입한다. | F — 종료 시점 표현 | ITERMX가 양수이고 수렴 등으로 먼저 끝나지 않으면 반복 몸체는 ITERMX번 실행된다. 다음 반복이 상한을 넘는 시점에 루프를 끝낸다는 해석은 “exceeded”와 양립한다. 원문은 ITERMX+1번째 몸체를 실행한다고 적지 않는다. 따라서 문서 오기 B를 종료 시점 표현 차이 F로 고친다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:T1-010 | Thomas 선택의 시간 수심 조건 | swantech PDF 90쪽·인쇄 82쪽: “in the absence of mean current there are no shifts in the frequency”. swanuse PDF 94쪽–95쪽·인쇄 86쪽–87쪽은 SIP 사용 조건을 “in the presence of currents or time varying depth”로 적는다. `website/online_doc/swanuse/node29.html:440–449`도 같은 조건을 명시한다. 정렬 | `src/swancom1.ftn:3656`은 먼저 `IF ( IREFR.EQ.0 .AND. ITFRE.EQ.0 ) THEN`의 직접 나눗셈을 선택한다. 이어서 `:3681–3682`의 `ELSEIF ( (DYNDEP .OR. ICUR .EQ. 1) .AND.`와 `&           PNUMS(8).NE.0.                 ) THEN`에서 주파수 해법을 선택한다. 나머지 `:3720–3726`에서 SOLMAT를 호출한다. 비정렬 `src/SwanCompUnstruc.ftn90:1228`은 `elseif ( .not.DYNDEP .and. ICUR == 0 .or. int(PNUMS(8)) == 0 ) then`에서 SOLMAT를 선택한다. | C — swantech 조건 생략 | 해법 선택은 흐름뿐 아니라 DYNDEP와 주파수 전파 설정도 따른다. 무흐름만으로 Thomas 분기를 단정할 수 없다. 시간 변동 수심 조건은 사용자 매뉴얼에 있다. C는 swantech §3.3의 무흐름 설명에서 이 조건이 생략된 범위에 한정한다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:T1-015 | ACCUR의 공간 평균 조건 | swantech PDF 91쪽·인쇄 83쪽 식 (3.22)·(3.23)은 점별 상대 차이 또는 절대 차이이며 “are both satisfied in at least 98% of all wet grid points”라고 적는다. swanuse PDF 93쪽·인쇄 85쪽 본문 구문에는 ACCUR·DHOVAL·DTOVAL이 없다. 그러나 같은 책 PDF 141쪽·인쇄 133쪽과 `website/online_doc/swanuse/node49.html:307`에는 `ACCUR [drel] [dhoval] [dtoval] [npnts]`가 있다 | `src/swanpre1.ftn:1962–1966`은 `ELSE IF (KEYWIS ('ACCUR')) THEN`에서 DHOVAL·DTOVAL을 PNUMS(15)·PNUMS(16)으로 읽는다. `src/swancom1.ftn:4811–4812`의 TMREL은 SACC 차이를 이전 SACC로 나눈다. `:4814` `TMOVAL = ABS ( SACC2(INDX) - SACC1(INDX) ) / SMN2`; `:4819` `HSOVAL = ABS ( HSACC2(INDX) - HSACC1(INDX) ) / HSMN2`. `:4840–4841`은 `IF ( (TMREL .LE. PNUMS(1) .OR. TMOVAL .LE. PNUMS(16)) .AND.`와 `&         (HSREL .LE. PNUMS(1) .OR. HSOVAL .LE. PNUMS(15)) ) THEN`이다. 공간 평균은 `:4786–4787`에서 정한다. 비정렬 `src/SwanConvAccur.ftn90:198`, `:208–213`은 주기 차이를 주기 기준 허용값과 비교한다. | C — 본문 설명 누락 | NUMERIC ACCUR의 구문은 부록·웹에 있다. C는 swanuse NUMERIC 본문과 swantech의 구 기준 설명에 현행 DHOVAL·DTOVAL의 공간 평균 정규화가 빠진 범위에 한정한다. 식 (3.22)·(3.23)을 현재 ACCUR의 구현식으로 쓰지 않는다. 정렬 TMREL·TMOVAL은 평균 각주파수 차이이다. 비정렬 경로는 주기 차이이다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
