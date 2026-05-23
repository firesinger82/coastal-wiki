---
title: "swan propagation implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-propagation-implementation.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
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

- **Codex deep code analysis** of `/mnt/e/models/swan/source_code/swan/src/{swancom1,swancom5,swanmain}.ftn` — 2026-05-06.
- **Manual cross-reference** from swantech ch.3 (Numerical approaches), `[file=website:swan:node29]` Numerics.

## A. Main sweep loop (4-quadrant directional sweeping)

### Outer iteration loop (stationary)

`SWCOMP` is the main computation entry. It loops over **iterations** for stationary convergence:

- Iteration loop start: `[file=src/swancom1.ftn line=1487]` — `DO 450 ITER = 1, ITERMX`
- Iteration loop end: `[file=src/swancom1.ftn line=2099]` — labeled `410` block
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

- `IMATLA, IMATDA, IMATUA` — lower / diagonal / upper of tri-diagonal in σ
- `IMATRA` — RHS
- `IMAT5L, IMAT6U` — extra bands when sigma-coupling is implicit (penta-diagonal)

### BSBT path (default)

When `PROPSL ≠ 2,3` (i.e., not SORDUP/SecondOrder), the BSBT first-order upwind is used:

- Dispatch: `ACTION` calls `STRSXY` at `[file=src/swancom1.ftn line=5395-5410]`
- Diagonal contribution `FXY1 → IMATDA`: `[file=src/swancom5.ftn line=2148-2156]`
- RHS contribution `FXY2 → IMATRA`: `[file=src/swancom5.ftn line=2189-2193]`

`STRSXY` computes the upwind flux factor from `(cx, cy, KSX, KSY)` and adds to the matrix. The form is the standard backward-difference upwind, hence "Backward Space Backward Time" — backward in space because of upwind, backward in time because the iteration uses lagged source terms.

### Solver dispatch (SOLPRE → SOLMAT/SOLMT1/SWSIP)

After the matrix is assembled, `SWOMPU` calls `SOLPRE` (preconditioner / scaling) at `[file=src/swancom1.ftn line=3644-3653]`, then dispatches:

| Solver | Used when | file:line |
|--------|-----------|-----------|
| `SOLMAT` (Thomas tri-diagonal) | no current, explicit sigma | `[file=src/swancom1.ftn line=3722-3731]` |
| `SOLMT1` (cyclic tri-diagonal) | current present or explicit sigma | `[file=src/swancom1.ftn line=3709-3716]` |
| `SWSIP` (penta-diagonal iterative) | implicit sigma path | `[file=src/swancom1.ftn line=3693-3700]` |

So **enabling current changes which linear solver runs** — relevant when comparing performance with/without `INPGRID CURRENT`.

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

**Default `PHILIM`** (`SET LIMITER 0` or default):
- Defined at `[file=src/swancom1.ftn line=7857]`
- Clamp magnitude formula:
  ```
  DAC2MX = ABS((PNUMS(20) * 0.0081) / (2 * SPCSIG(IS) * KWAVE(IS,1)**3 * CGO(IS,1)))
  ```
  at `[file=src/swancom1.ftn line=7978-7979]`
- `PNUMS(20)` is the limiter coefficient (`SET LIMITER` command), default 0.1.

**HJ limiter `HJLIM`** (Hersbach & Janssen, when `SET LIMITER 1` for Janssen-style wind input):
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

### Default global stationary criterion (SACCUR)

`SACCUR` computes per-point Hs and mean-period change metrics, then a global convergence percentage:

- Per-point metrics: `HSREL` (relative), `HSABS` (absolute), `HSOVAL`; same for `TM*` — `[file=src/swancom1.ftn line=4811-4843]`
- Per-point converged flag: `LCONV` based on whether all metrics fall below tolerance
- Counts converged wet points: `IACCURt`
- Global reduction: `ACCUR = REAL(IACCUR) * 100.0 / REAL(NINDX)` `[file=src/swancom1.ftn line=4874-4886]`

So `ACCUR` is **% of wet points where Hs/Tm change is below tolerance**.

### Alternative curvature-based criterion (SWSTPC)

When `NUMERICAL STOPC` curvature mode is active:

- `SWSTPC` computes `HSCURV/TMCURV` (second-difference of recent iterations) `[file=src/swancom1.ftn line=9857-9879]`
- Local `LCONV` based on curvature staying below tolerance
- Global `ACCUR` reduction at `[file=src/swancom1.ftn line=9922-9929]`

This catches oscillatory non-convergence that the simple SACCUR criterion misses.

### Stopping check

After each full 4-sweep iteration, in `SWCOMP`:
```fortran
IF (ACCUR .GE. PNUMS(4)) GOTO 460  ! first-iteration guard for SWSTPC mode
```
at `[file=src/swancom1.ftn line=2352-2355]`. Hard cap is `ITERMX` via the outer `DO 450 ITER = 1, ITERMX` `[file=src/swancom1.ftn line=1487]`.

`PNUMS(4)` is set by `NUMERICAL ACCUR` command (default 99% — i.e., 99% of wet points must have converged).

### Linear-solver convergence (separate)

Inside a single sweep point, the iterative solvers `SWSIP` and `SWSOR` have their own residual norms:
- `SWSIP` (Strongly Implicit): `[file=src/swancom1.ftn line=8655-8863]`, residual norm `RNORM`
- `SWSOR` (Successive Over-Relaxation): `[file=src/swancom1.ftn line=9151-9373]`, residual `RESM`
- On solver failure: fallback to `AC2OLD` (preserve previous iteration value)

This is **pointwise** solver convergence, distinct from the global stationary stopping `ACCUR` above.

## Decision Guide — what knob to turn for which symptom

| Symptom | Likely cause | Code-level knob |
|---------|--------------|-----------------|
| Stationary won't converge (`ACCUR` stuck below 99%) | source-term / propagation imbalance, limiter too tight | tighten `NUMERICAL ACCUR`, raise `ITERMX`, switch to `STOPC` curvature mode |
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
- ▢ **User-experience cases** — placeholder for project-specific incidents.

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
- Inventory of all subroutines: `[file=/mnt/e/models/swan/manuals/refs/subroutines.md]`.

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
| Review status | `review_required: true` — verify line numbers against the user's SWAN trunk version (this scan: 2024 release-line) |
