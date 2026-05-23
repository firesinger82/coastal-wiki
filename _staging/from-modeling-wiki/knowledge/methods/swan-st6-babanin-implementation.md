---
slug: swan-st6-babanin-implementation
title: SWAN ST6/Babanin submodule — code-level
category: methods
model: swan
auto_draft: false
authored_by: claude-opus-4-7
review_required: true
generated: 2026-05-06
basis: deep Codex source scan of swan/src/SdsBabanin.ftn90
---

# SWAN ST6/Babanin submodule — code-level

## Scope note

`SdsBabanin.ftn90` is a single-file submodule that implements the ST6 / Babanin family of source terms (used when `IWIND=8` and `IWCAP=8`). It contains both the wind input (`SWIND_DBYB`) and whitecapping (`CALC_SDS`). This note documents its internal structure, formulas as they appear in code, and integration points with the rest of SWAN.

Companion to `swan-source-terms-implementation.md` (which covers other source terms).

## Source basis

Codex deep scan 2026-05-06 of `/mnt/e/models/swan/source_code/swan/src/SdsBabanin.ftn90` (~2700 lines, single module).

## A. Module structure

- Module header: `MODULE SDSBABANIN` at `[file=src/SdsBabanin.ftn90 line=3]`
- Pure procedure container: enters `CONTAINS` at `[file=src/SdsBabanin.ftn90 line=5]` immediately
- No module-scope `TYPE` / derived structures
- No module-scope `PARAMETER` constants — all constants are local to routines (e.g., `BNT` in `CALC_SDS`)
- No `PUBLIC`/`PRIVATE` — default visibility (everything accessible via `USE SDSBABANIN`)

## B. Wind input (`SWIND_DBYB`)

- Subroutine: `[file=src/SdsBabanin.ftn90 line=313]`
- Primary inputs at `[file=src/SdsBabanin.ftn90 line=505-513]`:
  - `SPCSIG, THETAW, KWAVE, AC2, UFRIC, WIND10, SPCDIR, ANYWND, CG`
  - Output arrays: `MEMSINA, MEMSINB`

### Internal computation steps

1. **1D spectral density** `SIGDENS(IS)`: build from `AC2` and `SPCSIG`, scale by `DDIR` at `[file=src/SdsBabanin.ftn90 line=542-549]`
2. **Direction-shape normalization** `KTHETA(IS,ID)`: per-frequency `DMAX`, with empty-bin guard at `[file=src/SdsBabanin.ftn90 line=552-572]`
3. **`ANAR`, `BN`, `SQRTBN`** (saturation precursors): `BN = ANAR * SIGDENS * k³ * Cg` at `[file=src/SdsBabanin.ftn90 line=575-587]`
4. **Wind speed proxy** `TEMP2`: either true `U10` (`TRUE_U10`) or `WNDSCL * UFRIC` at `[file=src/SdsBabanin.ftn90 line=598-602]`
5. **Donelan-Babanin/Yang growth-rate** at `[file=src/SdsBabanin.ftn90 line=621-629]`:
   - `TEMP4 → WPSI → GDONEL → GAMMAD → SWINEB`
   - `SWINEB` is the exponential coefficient (`BETA` in comments — see `[file=src/SdsBabanin.ftn90 line=630-635]`)
6. **`S_IN = SWINEB * AC2 * SPCSIG`**
7. **Linear-term stress** (`MEMSINA`): directional integration `TAUX_linear, TAUY_linear` at `[file=src/SdsBabanin.ftn90 line=643-656]`
8. **Stress-based reduction**: `CALL CALC_LFACTOR` at `[file=src/SdsBabanin.ftn90 line=659-660]`
9. **Final write to `MEMSINB`** at `[file=src/SdsBabanin.ftn90 line=722-726]`:
   - `MEMSINB = S_IN / SPCSIG` (after `RDFSIN(IS)` scaling)

So `SWIND_DBYB` produces a memo table `MEMSINB` that the main solver consumes via `FILSIN`.

## C. Whitecapping (`CALC_SDS`)

- Subroutine: `[file=src/SdsBabanin.ftn90 line=7]`
- Empirical saturation coefficient `BNT = (0.035)²` at `[file=src/SdsBabanin.ftn90 line=168]`

### Computation flow

1. **Threshold spectrum** `EDENST(IS) = 2π * BNT / (Cg * k³)` at `[file=src/SdsBabanin.ftn90 line=184-187]`
2. **Exceedance** `DEDENS = max(0, EDENS - EDENST)` at `[file=src/SdsBabanin.ftn90 line=192-195]`
3. **Normalized exceedance** `NDEDENS`: by `EDENST` or `EDENS` depending on `UPWARDS`, clipped nonnegative at `[file=src/SdsBabanin.ftn90 line=207-219]`
4. **Inherent breaking term** `T1(IS) = A1SDS * F * ANAR * NDEDENS^P1SDS` at `[file=src/SdsBabanin.ftn90 line=224-226]`
5. **Induced breaking term** `T2`: cumulative integral of `ADF(II) = ANAR * NDEDENS^P2SDS` at `[file=src/SdsBabanin.ftn90 line=236-248]`
6. **Output** `KDS = T1 + T2` (or `T1` only if `A2SDS ≤ 0`) at `[file=src/SdsBabanin.ftn90 line=256-259]` — passed back to caller

There is **no `SDS_TOTAL`** routine in this file (despite being mentioned in some literature). Total-dissipation diagnostics appear only as commented-out NRL local variables.

## D. Negative wind input (decay)

Dedicated block at `[file=src/SdsBabanin.ftn90 line=665-710]`:
- Active only when `ZIEGER` is true at `[file=src/SdsBabanin.ftn90 line=686]`
- Decay-side branch: `TEMP4 = MIN(0.0, UoverC*COSDIF - 1.0)`, `WPSI = TEMP4²` at `[file=src/SdsBabanin.ftn90 line=694-696]`
- Apply by subtracting `SWINEB * AC2 * SPCSIG * RDCOEF` from `S_IN` at `[file=src/SdsBabanin.ftn90 line=702]`

So negative input (wave decay during opposing wind / falling wind) is opt-in via Zieger formulation.

## E. Per-frequency / per-direction integration; A/B split

- Main exponential-term loops: nested `DO IS=1,MSC`, `DO ID=1,MDC` producing `S_IN(ID,IS)` at `[file=src/SdsBabanin.ftn90 line=605-641]`
- Linear-term stress: also nested IS/ID with cos/sin(θ) projection at `[file=src/SdsBabanin.ftn90 line=646-653]`
- Code documentation at `[file=src/SdsBabanin.ftn90 line=712-720]` explicitly: split is `A + B*E`:
  - `B*N` (`MEMSINB`) is the explicit exponential term
  - `MEMSINA` is the linear part (separate routine `SWIND0_NRL`)
- `SWIND0_NRL` writes linear `A/sigma` to `MEMSINA` at `[file=src/SdsBabanin.ftn90 line=1529]`
- `FILSIN` injects whichever memo (`MEMSINA` or `MEMSINB`) into sweep-local `IMATRA`/`GENC0` at `[file=src/SdsBabanin.ftn90 line=1696-1697]`

## F. Calls into rest of SWAN

### Imports
- `SWIND_DBYB` imports `SWCOMM1, SWCOMM3, SWCOMM4, OCPCOMM4` at `[file=src/SdsBabanin.ftn90 line=318-321]`
- `CALC_SDS` imports `SWCOMM1` + selected `SWCOMM3` coefficients (`A1SDS, A2SDS, P1SDS, P2SDS, UPWARDS, GRAV, PI`) at `[file=src/SdsBabanin.ftn90 line=7-10]`

### Consumption from main solver
- `swancom1.ftn:6875` — `SOURCE` routine `USE SdsBabanin`
- `swancom1.ftn:7428-7436` — for `IWIND=8`: linear part via `SWIND0_NRL`, then `FILSIN(MEMSINA, ...)` → `IMATRA/GENC0`
- `swancom1.ftn:7489-7497` — exponential/DBYB part via `SWIND_DBYB`, then `FILSIN(MEMSINB, ...)` → `IMATRA/GENC0`
- `swancom1.ftn:7519-7534` — with `IWCAP=8`, swell-dissipation variants (`SSWELL_ZIEGER`/`_ROGERS`/`_ARDHUIN`) → `IMATDA, DISSC1`
- `swancom2.ftn:2859` — `CALC_SDS` produces `WCAP(IS)` for `SWCAP8` flow

## Decision Guide

| Scenario | Use ST6? |
|----------|----------|
| Engineering hindcast on regional grid | No (default Komen/Westhuysen sufficient) |
| Climate-scale wave statistics | Possibly (ST6 calibrated for long simulations) |
| Surface-following autonomous platforms (waves vs swell) | Yes — Zieger negative input matters |
| Coastal storm with strong wind | Possibly (ST6 captures saturation more accurately) |
| Quick first-pass simulation | No (ST6 has more knobs to tune) |

## Working Rules

1. **ST6 is opt-in** — `GEN3 ST6` activates `IWIND=8`; pair with `WCAP ST6` to set `IWCAP=8`. Mixing ST6 wind with non-ST6 whitecapping defeats the calibration.
2. **`MEMSINA`/`MEMSINB` are zero-sized** when `IWIND ≠ 8` — don't try to read them in custom code without checking.
3. **`A1SDS`, `A2SDS`, `P1SDS`, `P2SDS`, `UPWARDS`** are the saturation tunables in `WCAP ST6`. They live in `SWCOMM3` and are settable via the command file.
4. **`ZIEGER` activates negative wind input** — required for swell decay under opposing wind. Off by default in many configurations.

## Common Pitfalls

- **`GEN3 ST6` without `WCAP ST6`** — wind input + non-ST6 dissipation = imbalanced, runaway energy or spurious decay.
- **Tuning `A1SDS` without measuring** — saturation coefficient is sensitive; published defaults are calibrated for global runs.
- **`TRUE_U10` vs scaled `UFRIC`** — small differences in wind input through `TEMP2` choice affect long-fetch results.
- **Neglecting linear `MEMSINA`** — for very low-energy seed states, the linear term matters; `SWIND0_NRL` must be active.
- ▢ User-experience cases — placeholder.

## References

- `src/SdsBabanin.ftn90` — module body.
- `src/swancom1.ftn` — `SOURCE` dispatcher (`IWIND=8`, `IWCAP=8`), `FILSIN` consumer.
- `src/swancom2.ftn` — `SWCAP8` whitecapping that consumes `CALC_SDS` output.
- `src/swmod*.ftn` — `SWCOMM1/3/4` shared-state holders for ST6 coefficients.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations within SdsBabanin.ftn90 |
| Coverage | module structure, wind input pipeline, whitecapping, negative input, A/B split, integration |
| Review status | `review_required: true` |
