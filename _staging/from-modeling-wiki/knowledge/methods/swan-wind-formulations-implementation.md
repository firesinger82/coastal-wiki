---
slug: swan-wind-formulations-implementation
title: SWAN wind input formulations — WNDPAR, SWIND0/3/4/5 (code-level)
category: methods
model: swan
auto_draft: false
authored_by: claude-opus-4-7
review_required: true
generated: 2026-05-06
basis: deep Codex source scan of swan/src/swancom3.ftn + swanpre1.ftn
---

# SWAN wind input formulations — WNDPAR, SWIND0/3/4/5 (code-level)

## Scope note

Per-formulation deep dive of SWAN's wind-input source terms: `WNDPAR` (GEN1/GEN2), `SWIND0` (linear seed), `SWIND3` (Snyder/Komen GEN3), `SWIND4` (Janssen GEN3), `SWIND5` (Yan / Westhuysen GEN3). The exact formulas as implemented, plus the `AGROW` option's role.

ST6/Babanin is in a separate file (`SdsBabanin.ftn90`) — see `swan-st6-babanin-implementation.md`.

## Source basis

Codex deep scan 2026-05-06 of `/mnt/e/models/swan/source_code/swan/src/swancom3.ftn` (wind input family) + `swanpre1.ftn` (parser).

## A. `WNDPAR` (GEN1, GEN2)

- Subroutine: `[file=src/swancom3.ftn line=30]`
- GEN1 (`IWIND==1`): `ALPM = 0.0081` at `[file=src/swancom3.ftn line=378-401]`
- GEN2 (`IWIND==2`): compute `ETOTW` via `WINDP2`, then `EDML`, then `ALPM = MAX(0.0081, PWIND(5) * (1./EDML)**ABS(PWIND(6)))`

`CFPM = PWIND(13)`, used in `WINDP1` for PM frequency at `[file=src/swancom3.ftn line=246-253]`, `[file=src/swancom3.ftn line=911]`. **No GEN1-vs-GEN2 `CFPM` branch in `WNDPAR`** — same constant used by both.

### Per-bin growth/relaxation split

`[file=src/swancom3.ftn line=470-500]`:
- Growth branch: `SWIND_EXP = ADUM + BDUM*AC2CEN`, `SWIND_IMP = 0`
- Relaxation branch: `SWIND_EXP = TAUINV * ALIMW`, `SWIND_IMP = TAUINV`

### Matrix accumulation
`[file=src/swancom3.ftn line=512-517]`:
```
IMATRA += SWIND_EXP    (and to GENC0)
IMATDA += SWIND_IMP    (and to GENC1)
```

So both branches feed both matrix slots — what differs is whether `SWIND_IMP` is zero (growth) or nonzero (relaxation).

## B. `SWIND0` (Cavaleri-Malanotte-Rizzoli linear seed)

- Subroutine: `[file=src/swancom3.ftn line=1526]`
- Formula at `[file=src/swancom3.ftn line=1749-1750, 1766, 1772-1773]`:
  ```
  SWINEA = max(0,
    (PWIND(31) / (g² * 2π) / σ)
    * (UFRIC * max(0, cosΔ))⁴
    * exp(-min(2, FPM/σ)⁴)
  )
  ```
  **Not** proportional to `U10²` (a common literature simplification).

### Activation
- In GEN3-family (`IWIND >= 3`) only when `PWIND(31) > 1e-20` at `[file=src/swancom1.ftn line=7410-7418]`
- This is the optional seed growth from near-zero energy

### Matrix
- Linear input added explicitly: `IMATRA += SWINEA` at `[file=src/swancom3.ftn line=1782]`
- No `IMATDA` contribution (purely explicit)

## C. `SWIND3` (Snyder / Komen)

- Subroutine: `[file=src/swancom3.ftn line=1842]`
- Implemented coefficient at `[file=src/swancom3.ftn line=2043, 2048, 2051-2052, 2058-2059]`:
  ```
  SWINEB = max(0,
    0.25 * PWIND(9) * (28 * UFRIC * (k/σ) * cosΔ - 1) * σ
  )
  ```
- Since `CINV = k/σ = 1/c` (phase speed inverse), this matches the **Komen et al. 1984** form:
  ```
  β = max(0, (ρa/ρw) * 0.25 * (28 * UFRIC * cosΔ / c - 1))
  ```
  with `PWIND(9) = ρa/ρw` and source multiplied by `σ`.

### Matrix
- Explicit only: `IMATRA(ID,IS) += SWINEB * AC2(...)` at `[file=src/swancom3.ftn line=2061]`

So Snyder/Komen contributes purely to RHS (no implicit on diagonal). Stability comes from accompanying `WCAP` (whitecapping) on diagonal.

## D. `SWIND4` (Janssen)

- Subroutine: `[file=src/swancom3.ftn line=2094]`
- More complex than the others — has **iteration** to solve for friction velocity

### Sea-state dependent state

- `USTAR, ZELEN` initialized on early iter/step branches at `[file=src/swancom3.ftn line=2331-2359]`, `[file=src/swancom3.ftn line=2365-2367]`, `[file=src/swancom3.ftn line=2583-2585]`
- Reused and updated from previous iteration

### Wave stress and Newton-Raphson on UFRIC

- Wave stress `TAUW` from spectrum (plus HF tail) at `[file=src/swancom3.ftn line=2368-2526]`
- **Newton-Raphson loop** (up to 20 steps) solving for `TAUTOT` at `[file=src/swancom3.ftn line=2533-2568]`
- Then `UFRIC = sqrt(TAUTOT/RHOA)` at `[file=src/swancom3.ftn line=2570]`

### Janssen-Miles parameter

`[file=src/swancom3.ftn line=2601-2615]`:
```
ZCN = log(g * ZE / c²)
ZARG = κ / ((U*/c + ZALP) * cosΔ)
BETA = F1 * exp(ZLOG) * ZLOG⁴   (if ZLOG < 0)
```

### Final coefficient

`[file=src/swancom3.ftn line=2619]`:
```
SWINEB = (ρa/ρw) * BETA * (U*/c + ZALP)² * cos²Δ * σ
```

### Matrix
- Explicit only: `IMATRA += SWINEB * AC2` at `[file=src/swancom3.ftn line=2623]`

So Janssen has internal Newton-Raphson + state from previous step, but external matrix contribution is the same explicit pattern as Snyder/Komen.

## E. `SWIND5` (Yan / Westhuysen)

- Subroutine: `[file=src/swancom3.ftn line=2668]`

### Yan branch (default, `IWCAP ≠ 7`)

`[file=src/swancom3.ftn line=2849-2853, 2868-2877]`:
- Coefficients: `COF1=0.04, COF2=0.00544, COF3=0.000055, COF4=0.00031`
- `SWINEB = max(0, ((COF1·X² + COF2·X + COF3) * cosΔ - COF4) * σ)`
- where `X = UFRIC*k/σ = U*/c`

### Westhuysen / Alves-Banner branch (`IWCAP == 7`)

`[file=src/swancom3.ftn line=2856-2861]`:
- Coefficients: `COF2=0.00552, COF3=0.000052, COF4=0.000302` (`COF1` unchanged)

So the Westhuysen tuning differs only in lower-order polynomial coefficients (COF2/3/4); the structural form is identical.

### Matrix
- Explicit only: `IMATRA += SWINEB * AC2` at `[file=src/swancom3.ftn line=2881]`

## F. `AGROW` option

- **Not parsed in swancom3.ftn**.
- Parsed by `swanpre1.ftn` at `[file=src/swanpre1.ftn line=3059-3061]` and `[file=src/swanpre1.ftn line=3273-3275]`:
  - `AGROW [A]` sets `PWIND(31)` (default `0.0015` when keyword present without value)
- Documentation tying `PWIND(31)` to `GEN3 AGROW` at `[file=src/swmod1.ftn line=2636-2639]`
- Effect: scales `SWIND0` linear seed source via `PWIND(31)` at `[file=src/swancom1.ftn line=7416-7422]` + `[file=src/swancom3.ftn line=1750]`

So **`AGROW` applies broadly to all GEN3 families** (SWIND3/4/5) since it adds the linear seed source through the shared pre-call block (`IWIND >= 3`), not specifically to one formulation.

## Decision Guide

| Use case | Recommended formulation | Why |
|----------|-------------------------|-----|
| First-pass simulation | `GEN3 KOMEN` (`SWIND3`) | simplest, explicit, robust default |
| Long-fetch, deep-water | `GEN3 JANSSEN` (`SWIND4`) | sea-state dependent ZELEN matters |
| Coastal mixed sea-swell | `GEN3 WESTHUYSEN` (`SWIND5` + `IWCAP=7`) | tuned for that regime |
| Climate run, calibration | `GEN3 ST6` | (separate note) |
| Old code reproducibility | `GEN1` or `GEN2` (`WNDPAR`) | lacks 3rd-gen physics; only for legacy reproduction |
| Initial spectrum from zero | enable `AGROW` | seeds via `SWIND0` linear term |

## Working Rules

1. **All GEN3 wind inputs are explicit** (RHS only) — pair with `WCAP` to keep diagonal stable.
2. **Janssen has internal iteration** — slowest of the GEN3 family. Use only when sea-state dependence matters.
3. **Westhuysen and Yan share `SWIND5`** — switching `IWCAP` between 7 and not-7 changes the coefficients within the same routine.
4. **`AGROW` is a global GEN3 modifier** — affects all wind formulations, not specific to one.
5. **`PWIND(31)` is the seed-growth knob** — default 0.0015 when AGROW present without value.

## Common Pitfalls

- **Dropping `WCAP` while keeping `GEN3`** → unbounded growth + limiter clamping forever (already noted in source-terms note).
- **Comparing Janssen vs Komen at first iteration** — Janssen needs prior-state `USTAR`; iterate to convergence first.
- **Confusing `PWIND(9)` (Snyder/Komen ρa/ρw) with `PWIND(31)` (AGROW seed)** — both look like "small constants" in tuning files.
- **Westhuysen with whitecapping other than `IWCAP=7`** — silently uses Yan branch coefficients, not Westhuysen tuning.
- ▢ User-experience cases — placeholder.

## References

- `src/swancom3.ftn` — `WNDPAR`, `SWIND0/3/4/5`.
- `src/swanpre1.ftn` — `AGROW` parser.
- `src/swancom1.ftn` — `SOURCE` dispatcher chooses formulation by `IWIND`.
- `src/swmod1.ftn` — `PWIND(*)` documentation.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | per-formulation formulas as in code, matrix split, AGROW |
| Review status | `review_required: true` |
