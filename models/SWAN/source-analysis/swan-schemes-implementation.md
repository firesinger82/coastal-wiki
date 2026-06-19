---
title: "swan schemes implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-schemes-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN higher-order schemes — SORDUP, SANDL, GSE, FLUXLIM

## Scope note

How SWAN implements alternatives to the default BSBT propagation: stationary higher-order (`SORDUP`), nonstationary higher-order (`SANDL` = Stelling & Leendertse, internally `PROPSL=3`), GSE (Garden Sprinkler Effect) anti-diffusion, and the slope-limiter `FLUXLIM`. Includes the `PROPSL` flag's full life cycle.

## Source basis

Codex deep scan 2026-05-06 of `src/swancom1.ftn` (ACTION dispatch + flag management), `src/swancom5.ftn` (`STRSXY`, `SORDUP`, `SANDL`, `SWFLXD`), `src/swanpre1.ftn` (PROP parser).

## A. `PROPSL` flag — values and life cycle

| Variable | Default | Meaning |
|----------|---------|---------|
| `PROPSC` | 1 (set per stationary/nonstat) | global selection: `PROPSS` (stat) or `PROPSN` (nonstat) |
| `PROPSS` | 2 (SORDUP) | stationary scheme |
| `PROPSN` | 3 (SANDL) | nonstationary scheme |
| `PROPSL` | 1 (BSBT) | local-per-point scheme; degraded from PROPSC when stencil leaves domain |

Defaults at `[file=src/swanmain.ftn line=1179-1183]`. Stationary/nonstat selection at `[file=src/swanmain.ftn line=6354-6358]`.

`PROPSL = PROPSC` initialized at `[file=src/swancom1.ftn line=3052]`. Then locally degraded:
- to BSBT (`1`) or even no propagation (`0`) at points where the higher-order stencil hits domain edge / dry / obstacle — `[file=src/swancom1.ftn line=3099-3233]`

`PROP BSBT` parser branch sets both `PROPSN=1` and `PROPSS=1` at `[file=src/swanpre1.ftn line=793-795]`. **No parser branch explicitly sets `PROPSC=2` or `PROPSC=3`** — those values come from defaults; user choice is "use BSBT or use the defaults". DIFFRACTION command silently forces both to BSBT at `[file=src/swanmain.ftn line=4094-4095]`.

## B. SORDUP (`PROPSL = 2`, stationary higher-order)

- Dispatch: `[file=src/swancom1.ftn line=5401-5404]` — `IF (PROPSL.EQ.2) CALL SORDUP(...)`
- Subroutine entry: `SUBROUTINE SORDUP` at `[file=src/swancom5.ftn line=2238]`
- Adds 2nd-order upwind stencil with extra points `KCGRD(6)`, `KCGRD(7)`:
  - Form: `1.5 φ_i - 2 φ_{i-1} + 0.5 φ_{i-2}` (3-point upwind)
  - Diagonal scaling: `+1.5` `[file=src/swancom5.ftn line=2467, 2473-2476]`
  - RHS: `+2`, `-0.5` `[file=src/swancom5.ftn line=2498, 2504-2507]`
- Stencil expansion: ICMAX from 3 (BSBT) to **7** for SORDUP at `[file=src/swancom1.ftn line=999-1001]`

**Stationary-only enforcement**: hard error if `NSTATC == 1` at `[file=src/swancom5.ftn line=2420-2422]`. (Use SANDL for nonstationary higher-order.)

## C. SANDL — Stelling & Leendertse (`PROPSL = 3`, nonstationary higher-order)

The "SecondOrder" scheme isn't named that in code; the actual subroutine is `SANDL`.

- Dispatch: `[file=src/swancom1.ftn line=5396-5400]` — `IF (PROPSL.EQ.3) CALL SANDL(...)`
- Subroutine: `SUBROUTINE SANDL` at `[file=src/swancom5.ftn line=2566]`
- Stencil: ICMAX = **13** at `[file=src/swancom1.ftn line=996-998]` (largest of the three schemes)

### Implicit time integration

`SANDL` adds time term to matrix at `[file=src/swancom5.ftn line=3033-3034]`:
```
IMATDA += FXY1 + RDTIM
IMATRA += FXY2 + ACOLD * RDTIM
```
`ACOLD` selection mirrors BSBT: `AC2` if `ITERMX==1` else `AC1` `[file=src/swancom5.ftn line=3028-3032]`.

### Mixed old/new-time transport

Old-time velocities `CAX1, CAY1` are pre-computed in ACTION for nonstat `PROPSL=3` at `[file=src/swancom1.ftn line=3302-3333]`. They appear in RHS terms at `[file=src/swancom5.ftn line=2964-2971, 2982-2997, 3028-3032]`.

### Higher-order coefficients

Fractional weights `0.83333, 1.25, -0.5, 0.08333, 0.25` at `[file=src/swancom5.ftn line=2940-2971, 2975-2997, 3033-3034]` — these implement the Stelling & Leendertse 4-point scheme.

### Hard mode-compatibility checks

- `PROPSC=2` (SORDUP) **disallowed in nonstat** at `[file=src/swanmain.ftn line=6564-6568]`
- `PROPSC=3` (SANDL) **disallowed in stat** — same place

So users can't "force" either scheme into the wrong mode; SWAN substitutes BSBT or errors.

## D. Choice consequences (matrix & stability)

| Scheme | Stencil | Diagonal | RHS | CFL note |
|--------|---------|----------|-----|----------|
| BSBT (`PROPSL=1`) | `ICMAX=3` (3-point upwind) | `FXY1` from local coeffs | `FXY2` from points 2/3 | unconditionally stable (implicit BSBT) |
| SORDUP (`PROPSL=2`) | `ICMAX=7` | `+1.5 ×` higher-order | mixed `+2/-0.5` | stationary only; iteration convergence may slow |
| SANDL (`PROPSL=3`) | `ICMAX=13` | mixed old/new-time | fractional 0.83/1.25/-0.5/0.08/0.25 | nonstat; CFL warning fires if MYU>10 |

`STRSXY` (BSBT) coeff assembly: `[file=src/swancom5.ftn line=2148-2156, 2183-2190]`.

## E. GSE (Garden Sprinkler Effect) handling

GSE is unphysical "spreading" of swell into rays/spokes when angular resolution is coarse. Anti-GSE diffusion smooths it out.

- Parser: `PROP GSE [WAVEAGE]` at `[file=src/swanpre1.ftn line=796-802]`. Warns if context is non-SANDL (`PROPSN.NE.3`) at `[file=src/swanpre1.ftn line=797-800]`.
- Application **only inside SANDL** — `IF (WAVAGE.GT.0.)` block at `[file=src/swancom5.ftn line=2916-2935]` computes:
  - `DSS, DNN` (along-spoke, across-spoke diffusion magnitudes from wave age)
  - `DXX, DYY, DXY` (anisotropic 2D diffusion tensor)
- Adds anti-GSE diffusion correction to RHS via second-derivative-like terms: `FXY2 += ...` using `D11AC, D12AC, D22AC` at `[file=src/swancom5.ftn line=3000-3017]`.

So **GSE works only when `PROPSC=3` (nonstat SANDL)**. Stationary runs (using SORDUP) do not have this anti-spoke option.

## F. FLUXLIM (slope-limited theta-direction transport)

- Parser: `PROP FLUXLIM` sets `PROPFL=1`, `PNUMS(6)=0` at `[file=src/swanpre1.ftn line=803-805]`.
- Applied **only in directional `D` transport dispatch in ACTION** at `[file=src/swancom1.ftn line=5471-5479]`:
  - `PROPFL=0` → `STRSD` (default)
  - `PROPFL=1` → `SWFLXD` (limiter version)
- Not used in `STRSXY`/`SORDUP`/`SANDL` (XY propagation).

### Limiter formula in `SWFLXD`

PL-kappa slope limiter with `XKAP = PNUMS(6)`:
```
FACT = MIN(2., 0.5*(1+XKAP)*R + 0.5*(1-XKAP))
XLIM = MAX(0., MIN(2*R, FACT))
```
Anti-diffusive correction:
```
DFCOR = 0.5 * (CAP*XLIMP*(ACT0-ACT1) - CAN*XLIMN*(ACT3-ACT2))
```
at `[file=src/swancom5.ftn line=5308, 5352-5363, 5408-5418]`.

## Decision Guide

| Use case | Recommended scheme | Why |
|----------|-------------------|-----|
| Stationary engineering hindcast | SORDUP (default `PROPSS=2`) | better accuracy than BSBT, no time-step constraint |
| Stationary with spectral surf-zone breaking | BSBT (`PROP BSBT`) | SORDUP iteration may stall on stiff source terms |
| Nonstationary storm hindcast | SANDL (default `PROPSN=3`) + GSE | accurate for swell propagation, GSE prevents spokes |
| Nonstat with large CFL (DT cannot be reduced) | BSBT (`PROP BSBT`) | unconditionally stable but more dissipative |
| Theta-direction sharp gradients (refraction near coast) | enable `PROP FLUXLIM` | slope-limited transport in θ |
| Diffraction needed | (forced) BSBT | SWAN auto-disables higher-order with diffraction |

## Working Rules

1. **`PROPSL` is per-grid-point**, demoted from `PROPSC` near edges/obstacles. So a "SORDUP" run actually runs BSBT at the boundaries — visible in spurious results if you analyze near boundaries.
2. **GSE only with SANDL** — don't bother enabling `PROP GSE` if you're in stationary mode.
3. **`FLUXLIM` is θ-only** — it doesn't affect XY propagation.
4. **DIFFRACTION forces BSBT** — silently. If accuracy matters and you need higher-order, drop diffraction.
5. **Hard error path**: if `NSTATC=1` and `PROPSC=2`, you get BSBT at run time (silently degraded), not the SORDUP you asked for.

## Common Pitfalls

- Setting `PROP BSBT` then expecting GSE to work — GSE silently has no effect.
- Comparing SORDUP vs BSBT residuals across boundary points — SORDUP degrades to BSBT there, so the comparison is degenerate near boundaries.
- `FLUXLIM` with PNUMS(6) at default 0 — gives the most diffusive limiter; tune `PNUMS(6)` toward 0.5–1 for sharper transport.
- Switching `PROPSS` ↔ `PROPSN` mid-run via successive `PROP` commands — only the LAST one applied wins (parser overwrites globals).

## References

- `src/swanpre1.ftn` — `PROP` parser.
- `src/swancom1.ftn` — ACTION dispatch, `PROPSL` degradation logic, ICMAX selection.
- `src/swancom5.ftn` — `STRSXY` (BSBT), `SORDUP`, `SANDL`, `SWFLXD` (FLUXLIM).
- `src/swanmain.ftn` — defaults, `PROPSC = PROPSS/PROPSN` selection, mode-compatibility checks.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | flag values, SORDUP, SANDL, GSE, FLUXLIM, mode compatibility |
| Review status | `review_required: true` |
