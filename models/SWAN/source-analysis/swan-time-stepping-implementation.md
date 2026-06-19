---
title: "swan time stepping implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-time-stepping-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN nonstationary time stepping — outer loop, AC1 swap, time-varying inputs

## Scope note

How SWAN advances through time in nonstationary mode: outer time loop wiring, `AC1 ↔ AC2` swap timing, time-varying input updates (wind/current/water level), boundary-spectrum time interpolation, output trigger logic, and CFL warning emission.

Companion to `swan-propagation-implementation.md` (per-iteration solve) and `swan-data-structures-implementation.md` (`AC1`/`AC2` definitions).

## Source basis

Codex deep scan 2026-05-06 of:
- `src/swanmain.ftn` — outer time loop, time advance, output dispatch
- `src/swanpre1.ftn` — `COMPUTE` parser, time-window storage
- `src/swancom5.ftn` — time-term in matrix
- `src/swanout1.ftn` — output triggering

## A. Outer time-step loop

`[file=src/swanmain.ftn line=571]`:
```fortran
DO 500 IT = IT0, MTC
  ...
500 CONTINUE
```

Initial condition:
- `IT0 = 0` for nonstationary (`NSTATC = 1`) — `IT=0` does an initial state update before the first `SWCOMP` call
- `IT0 = 1` for stationary (`NSTATC = 0`) — single iteration block

at `[file=src/swanmain.ftn line=544-562]`.

End-of-step time advance: `TIMCO = TIMCO + DT` for `IT < MTC` at `[file=src/swanmain.ftn line=688-693]`.

## B. COMPUTE parsing → loop wiring

Parser branches `[file=src/swanpre1.ftn line=875-905]`:
- Stationary: `DT = 1.E10`, `RDTIM = 0`, `MTC = 1` — no dynamic stepping at `[file=src/swanpre1.ftn line=888-891]`
- Nonstationary: read `TBEGC, DELTC, TENDC`; compute `DT = DELTC`, `RDTIM = 1./DT`, `MTC = NINT((TFINC-TINIC)/DT)`, `TIMCO = TINIC` at `[file=src/swanpre1.ftn line=903-905]`, `[file=src/swanpre1.ftn line=913-915]`, `[file=src/swanpre1.ftn line=919]`.

Storage in `RCOMPT` at `[file=src/swanpre1.ftn line=925-930]`: `NSTATC, MTC, TFINC, TINIC, DT`.

Runtime pulls: `SWREAD(COMPUT)` fills globals at `[file=src/swanmain.ftn line=394-400]`. The `IT` loop bound at `[file=src/swanmain.ftn line=571]` consumes parsed `MTC`. Per-step `SWCOMP` call at `[file=src/swanmain.ftn line=610]`, `[file=src/swanmain.ftn line=620-627]`.

## C. Time-term contribution in matrix

`[file=src/swancom5.ftn line=2177-2184]` — when `NSTATC=1`, the time term is added in implicit backward-Euler form:
```fortran
IMATRA(...) += ACOLD * RDTIM       ! = AC_old / DT to RHS
IMATDA(...) += RDTIM                ! = 1/DT to diagonal
```

`ACOLD` source at `[file=src/swancom5.ftn line=2179-2181]`:
- `ITERMX == 1` → `ACOLD = AC2(...)` (single-iter, "explicit" old-time within step)
- `ITERMX > 1` → `ACOLD = AC1(...)` (multi-iter, true old-time)

This is the **only** place `AC1` is read during the matrix assembly path. Filename:line: `[file=src/swancom5.ftn line=2181]`.

## D. Time-varying inputs (wind/current/water level)

Inputs are updated **before** `SWCOMP` each step:
- `SNEXTI` runs first, then `SWCOMP` — at `[file=src/swanmain.ftn line=586-595]`, `[file=src/swanmain.ftn line=7020-7166]`
- Wind via `FLFILE(5,6,...)` — interpolated to `COMPDA(:, JWX2)`, `COMPDA(:, JWY2)` at `[file=src/swanmain.ftn line=7023-7029]`
- Water level via `FLFILE(7,0,...)` — depth fields recomputed from bathymetry + WL at `[file=src/swanmain.ftn line=7093]`
- Current via `FLFILE(2,3,...)` — Froude limiting after at `[file=src/swanmain.ftn line=7161-7166]`

### `FLFILE` time interpolation

`[file=src/swanmain.ftn line=8828-8850]`:
```fortran
W3 = (TIMCO - TIMR1) / (IFLTIM - TIMR1)
W1 = 1 - W3
COMPDA(:, J*2) = W1 * old + W3 * new
```
Vector quantities (wind, current) preserve magnitude with a correction term to avoid losing intensity through interpolation.

## E. Boundary update in nonstationary

- `SNEXTI` calls `RBFILE` for each boundary file every step (master rank), broadcasts `BSPECS` at `[file=src/swanmain.ftn line=6916-6919]`.
- In `RBFILE`, when `TIMCO > TIMF2` → read new spectra, shift prior "new" to "old" at `[file=src/swanmain.ftn line=7724-7754]`.
- Time interpolation weight `W1 = (TIMF2 - TIMCO) / (TIMF2 - TIMF1)`; spectra blend via `SINTRP(W1, 1-W1, old, new, ...)` at `[file=src/swanmain.ftn line=8033-8048]`.
- Spatial interpolation between two stored boundaries on the boundary side uses local `W1`/`W2` from `BGRIDP`; result written into `AC2` at `[file=src/swanmain.ftn line=6941-6946]`.

## F. Output writing per step

- `BLOCK`/`TABLE`/`SPECout` parse `TBEG` + `DELT` into `ORQTMP%OQR(1:2)` at `[file=src/swanpre2.ftn line=1486-1487]`, `[file=src/swanpre2.ftn line=1837-1838]`, `[file=src/swanpre2.ftn line=1961-1962]`.
- `SWOUTP` is called every step at `[file=src/swanmain.ftn line=677-680]`. Per-request gating decides write vs no-write.
- Trigger logic in `SWORDC` `[file=src/swanout1.ftn line=682-704]`:
  - Periodic: `OUTR(2) > 0` and `TIMCO >= TNEXT` → write, advance `OUTR(1) = TNEXT + OUTR(2)`
  - End-only: `OUTR(2) < 0` → write only when `|TFINC - TIMCO| < 0.5 * DT`
- Active dispatch to `SWBLOK`/`SWTABP`/`SWSPEC` at `[file=src/swanout1.ftn line=436-509]`.

**Output stride `DELT` is independent from compute stride `DELTC`** — explicit in trigger code at `[file=src/swanout1.ftn line=693-694]`.

## G. CFL / time-step warnings

`[file=src/swancom5.ftn line=2889-2894]` computes a CFL-like metric for higher-order propagation:
```fortran
MYU = ABS(DT * CGO(1,1) / MIN(DXMYU, DYMYU))
```

`[file=src/swancom5.ftn line=2893-2904]`: if `MYU > 10` and not warned yet, `MSGERR(2, ...)` emits an advisability warning recommending `PROP BSBT` for nonstationary higher-order with large CFL.

User-set `CFL` parameters (in `PNUMS` indices 6 and adjacent) at `[file=src/swanpre1.ftn line=2037,2051,2059]` — these affect explicit-scheme controls, not stability of the implicit BSBT path.

General error handling: `MSGERR` writes to `PRINTF`; halt when `LEVERR > MAXERR` at `[file=src/swanmain.ftn line=523-528]`, `[file=src/swanmain.ftn line=573-578]`.

## Decision Guide

| Symptom | Likely cause | Where to check |
|---------|--------------|----------------|
| Run divergence at large DT | CFL violation w/ higher-order scheme | warning at `swancom5.ftn:2893`; reduce DT or switch to BSBT |
| Time stamps in output skip | output `DELT` < compute `DELTC`, or wall-clock between writes | `SWORDC` trigger at `swanout1.ftn:682-704` |
| Wind interpolation looks step-wise | input `SERIES` interval too large vs `DT` | `FLFILE` weight at `swanmain.ftn:8828-8850` |
| Boundary stays at stale value | `TIMF2 < TIMCO` exhaustion | exhaustion message at `swanmain.ftn:8019` |
| `AC1` "wrong" between iterations | `ITERMX==1` vs `>1` toggles AC1 vs AC2 source | `ACOLD` selection at `swancom5.ftn:2179-2181` |

## Working Rules

1. The **time-term in matrix** is the only place `AC1` enters during a time step (besides the swap at start). All physics are computed against `AC2`.
2. **Always run `IT=0` first** in nonstationary — it lets initial conditions settle without modifying state from a "before" assumption.
3. **Output `DELT` is decoupled from compute `DELT`** — set finer compute (`DELTC`) for stability + coarser output (`DELT`) for storage.
4. CFL warning at `MYU>10` is **advisory not fatal**. Higher-order can still run; just expect dispersion if you ignore it.

## Common Pitfalls

- **`SET TIMINC` confusion**: this command sets the *parsing* time format step, not the compute time step. Compute `DT` comes from `COMPUTE NONSTAT` `DELTC`.
- **Hot-restart at non-zero `TIMCO`**: `SWREAD(COMPUT)` re-reads `TINIC` from the next `COMPUTE` block. If you intended to continue from hot-start, `TINIC` must match the hot-start time.
- **`SET TIMEFORMAT` mismatch** between command file and input data files (wind, level, current) → time interpolation reads wrong epoch.

## References

- `src/swanmain.ftn` — outer time loop, FLFILE, output dispatch, error handling.
- `src/swancom5.ftn` — time-term in matrix; CFL warning emission.
- `src/swanpre1.ftn` — `COMPUTE` parser; CFL parameter slots.
- `src/swanout1.ftn` — `SWORDC` output trigger logic.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | time loop, AC1/AC2 swap, FLFILE interp, boundary time interp, output trigger, CFL warning |
| Review status | `review_required: true` |
