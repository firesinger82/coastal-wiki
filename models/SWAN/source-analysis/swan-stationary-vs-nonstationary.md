---
title: "swan stationary vs nonstationary"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-stationary-vs-nonstationary.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How SWAN dispatches between stationary (`MODE STAT`) and non-stationary (`MODE NONST/DYN`) computation, the relationship between intent (`NSTATM`) and actual computation (`NSTATC`), the four-quadrant Gauss-Seidel sweep order (WS-SE-EN-NW), how `MXITST` (default 50) vs `MXITNS` (default 1) iteration limits work, the convergence test (`STOPC`/`ACCUR`/`PNUMS`), the propagation scheme dispatch (`PROPSC=1` BSBT, `2` SORDUP, `3` S&L), how the time-derivative enters the transport matrix only in non-stationary mode, and the memory implications for AC1/AC2 storage. Use this when picking a mode for a domain, debugging stationary convergence, or estimating memory for long unstructured runs.

## Source basis

- `swanpre1.ftn:738-936, 791-795, 1913-1979, 4007-4554` — `MODE`, `COMPUTE`, `NUMERIC STOPC/ACCUR`, propagation flags.
- `swanmain.ftn:266-693, 493-628, 1092-1095, 6889-6904` — main loop, AC1/AC2 alloc, sweep dispatch.
- `swancom1.ftn:724-2356, 5393-5411, 9618-9928` — sweep order, accuracy tests, `STRSXY/SACCUR/SWSTPC`.
- `swancom5.ftn:2148-2904, 2629-2700` — propagation scheme implementations.
- `swmod1.ftn:2272-2403, 2869-2874` — defaults, `PROPSC` codes.
- `swmod2.ftn:990-1028` — AC2 storage.
- `SwanCompUnstruc.ftn90:780-1080`, `SwanVertlist.ftn90:45-181` — unstructured.

## A. Top-level dispatch

`MODE` sets intent (`swanpre1.ftn:738-752`):
- `MODE NONST/DYN` → `NSTATM=1`.
- `MODE STAT` → `NSTATM=0`.

`COMPUTE` sets actual computation (`:879-936`):

| Mode | Settings |
|---|---|
| Stationary | `DT=1e10, RDTIM=0, NSTATC=0, MTC=1` |
| Non-stationary | Reads `tbeg, DELTC, tend`; `NSTATC=1, RDTIM=1/DT`, computes `MTC` |

Iteration limits: `ITERMX = MXITST` for stationary, `MXITNS` for non-stationary (`:930-936`).

`SWMAIN` runs time-step loop `DO 500 IT = IT0, MTC` (`swanmain.ftn:571`):
- Stationary: `IT0=1`.
- Non-stationary: `IT0=0` for initial conditions (`:544-559`).

Structured grids → `SWCOMP`; unstructured → `SwanCompUnstruc` (`:610-628`). Time advances only for non-stationary (`:686-695`).

## B. Stationary iteration

Defaults: `MXITST=50, MXITNS=1, ITERMX=MXITST` (`swanmain.ftn:1092-1095`).

`NUMERIC STOPC/ACCUR` parses convergence tolerances + `NPNTS` + max iterations (`swanpre1.ftn:1913-1979`).

Default `PNUMS` (`swmod1.ftn:2393-2403`):
- Relative Hs/Tm01.
- Absolute Hs/Tm01.
- Required percent wet points.

Structured stationary: `DO 450 ITER = 1, ITERMX` (`swancom1.ftn:1487`):
- `ACCUR` mode → calls `SACCUR`.
- `STOPC` mode → calls `SWSTPC` (`:2270-2284`).

Termination: `ACCUR >= PNUMS(4)`, with guard preventing `STOPC` from stopping on iteration 1 (`:2349-2356`).

`SWSTPC` checks Hs/Tm changes + curvature (`:9618-9886`); converts converged wet points to percent accuracy (`:9912-9928`).

## C. Stationary sweeping (4-quadrant Gauss-Seidel)

Comments define 4 sweep directions WS-SE-EN-NW (`swancom1.ftn:724-740`).

Documented order (`:761-793`):
1. `KSX=−1, KSY=−1`, forward `IX/IY` (sweeping toward NE).
2. `KSX=+1, KSY=−1`, reverse `IX`, forward `IY` (toward NW).
3. `KSX=+1, KSY=+1`, reverse both (toward SW).
4. `KSX=−1, KSY=+1`, forward `IX`, reverse `IY` (toward SE).

Executable sweep-direction branches at `swancom1.ftn:1741-1817`. Each grid point calls `SWOMPU` for actual solve (`:2000-2033`).

This means **each iteration solves all four sweeps**; convergence requires multiple iterations until all directional information has propagated through the domain.

## D. Non-stationary time stepping

Wraps same sweep machinery inside explicit time steps:
1. `SNEXTI` updates BC/input (`swanmain.ftn:586-595`).
2. `SWCOMP` / `SwanCompUnstruc` computes (`:610-628`).
3. `TIMCO` advances by `DT` (`:686-695`).

Default: **one iteration per time step** (`MXITNS=1`).

Time derivative enters transport matrix only when `NSTATC=1`: `STRSXY` adds `ACOLD*RDTIM` to RHS, `RDTIM` to diagonal (`swancom5.ftn:2177-2188`).

With one iteration: uses `AC2` as old action.
With multiple iterations: uses `AC1` (`:2177-2184`).

## E. BSBT / SORDUP / S&L

`PROPSC` codes (`swmod1.ftn:2869-2874`):

| `PROPSC` | Scheme | Order |
|---|---|---|
| `1` | BSBT (Backward Space Backward Time) | 1st-order upwind |
| `2` | SORDUP (Second-Order UPwind) | 2nd-order |
| `3` | S&L (Stelling & Leendertse) | 3rd-order space-time |

`PROP BSBT` sets both stationary and non-stationary to first-order (`swanpre1.ftn:791-795`).

In `SWOMPU`, stencil sizes (`swancom1.ftn:3052-3078`):
- BSBT: smallest.
- SORDUP: larger.
- S&L: largest.

Code falls back to lower-order schemes near boundaries, dry points, obstacles (`:3079-3235`).

Dispatch (`swancom1.ftn:5393-5411`):
- `PROPSL=3` → `SANDL`.
- `PROPSL=2` → `SORDUP`.
- else → `STRSXY`/BSBT.

`SORDUP` is **stationary-only**; warns/errors if used non-stationary (`swancom5.ftn:2304-2422`).

`SANDL` warns on large non-stationary CFL (`:2889-2904`).

## F. Stationary unstructured grid

For unstructured (`OPTG=5`):
- `SWMAIN` builds vertex list (`swanmain.ftn:493-495`).
- Calls `SwanCompUnstruc` (`:623-627`).

`SwanVertlist` creates vertex orderings aligned with sweep directions (`SwanVertlist.ftn90:45-181`):
- First sweep direction follows user/wave/wind direction.
- Allocates `vlist(nverts, nsweep)`.
- Projects vertices onto each sweep direction; sorts by distance.

`SwanCompUnstruc` iterates over sweeps + ordered vertices (`SwanCompUnstruc.ftn90:829-987`):
- Identifies upwave vertices from cell topology.
- Selects spectral sector for each sweep.

This is the unstructured analogue of the structured-grid dependence chain.

## G. Memory: AC1 / AC2

`AC2` = present-time action density storage (`swmod2.ftn:990-1028`); allocated in preprocessing (`swanpre1.ftn:4979-4989`).

`AC1` = local previous-time action density in `SWMAIN` (`swanmain.ftn:266, 296`).

`AC1` allocated **only**:
- Non-stationary runs with multiple iterations.
- S&L propagation.

Otherwise zero-size placeholder (`swanmain.ftn:497-519`).

`SNEXTI` copies `AC2 → AC1` only for non-stationary multi-iteration or S&L (`:6889-6904`).

So **stationary BSBT/SORDUP** generally stores only `AC2`; **non-stationary multi-iter** and **S&L** need `AC1+AC2` (~2× memory).

## H. Recommended choice

**Stationary mode** when:
- Forcing/BC/currents/water level/depth steady enough for equilibrium snapshot.
- Steady design cases.
- Small domains where propagation lag negligible.

Code embeds rule of thumb: stationary often acceptable for domains smaller than ~100 km or 1° per side (`swancom5.ftn:2899-2904`).

**Non-stationary mode** when:
- Time history matters: storms, moving wind, tides/surge, time-varying BCs.
- Large domains (arrival-time effects).
- Coupling to hydrodynamics.

SWAN enforces non-stationary input fields require `MODE NONSTAT` (`swanpre1.ftn:4007-4010, 4553-4554`).

## Decision Guide

| Domain / Situation | Mode + Settings |
|---|---|
| Steady design wave (single sea state) | `MODE STAT`, `MXITST=50` (default), `BSBT` |
| Tidal bay with wave-current interaction | `MODE NONSTAT`, `DELTC=15-30 min`, `BSBT`, `MXITNS=1` |
| Storm hindcast (wide domain) | `MODE NONSTAT`, `DELTC=30-60 min`, `BSBT` |
| Surf-zone resolved (very fine grid) | `MODE NONSTAT`, `DELTC` matching wave period × 5-10 |
| Stratified shelf, accuracy critical | `MODE NONSTAT`, `S&L` propagation |
| ADCIRC coupled (NWS=320) | `MODE NONSTAT`, `DELTC` matches `Flpp` from ADCIRC |
| Memory-tight large grid | Stationary BSBT (only AC2) |
| Multiple iterations needed for convergence (sub-domain) | `MXITNS > 1`, accept doubled memory (AC1+AC2) |

## Working Rules

- Stationary `MXITST=50` is generous; reduce to 30 for speed if convergence robust.
- For non-stationary, `MXITNS=1` is the production default; only raise for special cases.
- BSBT is the default and works for nearly all cases. SORDUP and S&L for academic comparison only.
- Convergence criterion: `STOPC` more rigorous than `ACCUR`; recommend `STOPC` for production.
- For unstructured grids, sweep ordering matters — first sweep along dominant wave direction speeds convergence.
- Output `BLOCK 'sname' ITERMAX HSIGN ...` to monitor iteration count and Hs convergence per stationary call.
- For coupled runs, ensure `DELTC` ≥ ADCIRC coupling interval × 1-2; otherwise wave field over-iterated.

## Common Pitfalls

- ▢ Using `MODE STAT` with time-varying wind/water level — input parser refuses; need `MODE NONSTAT`.
- ▢ `MODE NONSTAT` with `DELTC=1 s` — extremely expensive; SWAN doesn't need that fine timestep for kinematic waves.
- ▢ Setting `MXITST=1` for stationary — single sweep insufficient; use `MXITST >= 30`.
- ▢ Using SORDUP in non-stationary — runtime error.
- ▢ Expecting `MXITNS > 1` to add accuracy without memory cost — `AC1` allocated, doubles spectrum memory.
- ▢ Confusing `NSTATM` (intent) and `NSTATC` (actual) — both must be set; `NSTATC=NSTATM` typically.
- ▢ For unstructured stationary, expecting same `MXITST` as structured — unstructured may need more (40-80) for similar convergence.

## Next expansion

- ITERMAX block-output diagnostic for stationary convergence monitoring.
- Convergence parameter (PNUMS) tuning recipe.
- BSBT vs S&L comparison on canonical wave-current refraction case.

## References

- Booij et al. 1999 (SWAN baseline + sweeping).
- Stelling & Leendertse 1992 (S&L scheme).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/swan/source_code/swan/src`. Auto-draft = false; review_required = true.
