---
slug: xbeach_avalanching
title: XBeach Avalanching / Dune Erosion (wetslp, dryslp, struct, ne_layer)
model: xbeach
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/xbeach/source_code/trunk/src/xbeachlibrary
---

## Scope

How XBeach implements avalanching slope-failure: where the slope is checked, the wet vs dry critical-angle distinction (`wetslp`/`dryslp` + `hswitch`), the iteration scheme (`nint(morfac)` passes, no residual tolerance), mass conservation between unequal-area cells (`dAfac`), hard-structure exclusion (`struct, ne_layer, structdepth`), and how `morfac` affects avalanching differently from regular bed transport. Use this when calibrating dune-face stability, debugging avalanching that doesn't trigger, or interpreting `n_aval` diagnostics.

## Source basis

- `morphevolution.F90:640-1147` — avalanching loop, slope checks, mass updates, fraction handling.
- `params.def:380, 384-385, 388, 393-394` — `morfac, wetslp, dryslp, hswitch, struct, ne_layer` definitions.
- `params.F90:1187, 1191-1211` — defaults and validation.
- `initialize.F90:1400-1416` — `structdepth` initialization.

## A. Slope criterion

Avalanching runs only when:
- Morphology time is active.
- `morfac > 0.999` in `bed_update` (`morphevolution.F90:640`).
- `par%avalanching == 1` (`:852`).

Each pass recomputes bed slopes:
- `dzbdx = (zb(i+1) − zb(i)) / dsu` (`:866-870`).
- `dzbdy = (zb(j+1) − zb(j)) / dnv` (`:872-880`).

X-direction check:
1. Compute combined 2D slope magnitude `totslp` (`:906-914`).
2. Convert critical total slope into x-component threshold `dzmax` (`:916-918`).
3. Trigger when `abs(s%dzbdx(i,j)) > dzmax + 1e-10` AND erodible thickness available at erosion-side cell (`:920`).

Y-direction analogous: `totslp`, choose wet/dry `dzmax`, then `abs(s%dzbdy)>dzmax` AND `structdepth>eps` (`:1019-1028`).

## B. Wet vs dry criteria

`wetslp, dryslp` are separate parameters:
- "Critical avalanching slope under water" (`params.def:384`).
- "Above water" (`:385`).

Defaults (`params.F90:1191-1197`):
- XBeach-G: based on `reposeangle`.
- Standard: `wetslp = 0.15`, `dryslp = 1.0`.

`hswitch` is the water depth at which the model switches from `wetslp` to `dryslp` (`params.def:388`, parsed at `params.F90:1203`).

X-direction: uses `hav` (may include short-wave runup corrections) (`morphevolution.F90:883-901`); selects `wetslp` if `max(hav(i,j), hav(i+1,j)) > hswitch+eps` (`:909-917`).

Y-direction: uses `s%hh` directly (`:1023-1027`).

## C. Iteration and convergence

Avalanching makes **at most `nint(par%morfac)`** passes per `bed_update` call (`morphevolution.F90:863`).

There is **no residual tolerance** — convergence is event-count based:
- `n_aval` reset each pass (`:864-865`).
- Incremented when x or y avalanching correction made (`:920-922, 1028-1030`).
- Reduced across MPI ranks (`:1116-1118`).
- Loop exits when `n_aval == 0` (`:1119-1126`).

So if no further avalanching is needed, the loop terminates early — no waste.

## D. Mass conservation

**Single-fraction** beds: avalanching transfers bed elevation from erosion to deposition cell.
- Applies `dAfac` for varying grid sizes (`:930, 1037`).
- X update: deposits `dzleft*dAfac`, erodes `dzleft` (`:946-960`).
- Y same (`:1052-1066`).

**Multi-fraction** beds: erodes layer-by-layer from erosion point:
- Computes per-fraction `edg2` (erosion) and `edg1` (deposition).
- Calls `update_fractions` for both cells (`:964-996, 1070-1099`).

**Caveat**: bed boundary conditions can introduce mass error after avalanching (`:1144-1147`).

## E. `struct` hard-structure exclusion

`struct=1` enables hard structures (`params.def:393`); causes `ne_layer` to be required (`params.F90:1205-1211`).

Actual avalanching exclusion via `s%structdepth`:
- Avalanche only occurs if erosion-side cell has `structdepth > eps` (`morphevolution.F90:920, 1028`).

If `struct=0`: `structdepth` initialized to `100.d0`, so this limit is effectively inactive (`initialize.F90:1400-1404`).

## F. `ne_layer` depth limit

`ne_layer` = file containing erodible-layer thickness (`params.def:394`).

When `struct==1`, read into `s%structdepth` (`initialize.F90:1404-1416`).

Avalanching cannot erode more than available `structdepth`:
- X positive/negative cases clamp `dzb` by `s%structdepth(i+1,j)` or `s%structdepth(i,j)` (`morphevolution.F90:927-940`).
- Y clamps similarly (`:1034-1047`).

`structdepth` decreased at erosion cell, increased at deposition cell (`:954-955, 1060-1061`).

## G. Interaction with `morfac`

`morfac` = morphological acceleration factor (`params.F90:1187`; `params.def:380`).

**Normal bed evolution** scales transport-gradient bed change by `par%morfac*par%dt/(1−por)` (`morphevolution.F90:738-748, 780-788`).

**Avalanching uses `morfac` differently**:
- Repeats avalanching relaxation loop `nint(par%morfac)` times (`:863`).
- Each correction scaled by `dt/avaltime` and a swash-excursion/grid factor — **not directly by `morfac` inside `dzb`** (`:922-925, 1030-1032`).

So `morfac` increases avalanching mainly by **allowing more passes per morphological step**, with early exit when no avalanching remains.

## Decision Guide

| Application | Setting |
|---|---|
| Standard sandy beach | `wetslp=0.15, dryslp=1.0, hswitch=0.01, avaltime=` default |
| Coarse cobble beach | `wetslp=0.30, dryslp=1.4` (steeper repose) |
| XBeach-G groundwater coupled | `reposeangle`-based; defaults handle |
| Hard structure (revetment, seawall) | `struct=1`, `ne_layer` file with thickness |
| Long-term `morfac=10–100` | Avalanching auto-loops more times — works correctly |
| No avalanching at all | `avalanching=0` |
| Verify avalanching active | Output `n_aval` per step or check global mass change |
| Asymmetric repose (lee vs windward) | Not directly supported — symmetric `wetslp/dryslp` only |

## Working Rules

- `wetslp=0.15` (≈ 8.5°) is the underwater repose for sand. `dryslp=1.0` (45°) is dry repose.
- `hswitch` defines the dry/wet threshold; default ~0.01 m means anything above MSL+1cm is "dry."
- Avalanching is event-based — for storm peak, expect many `n_aval` events; calm period, few or none.
- Mass conservation: single-fraction `dAfac` is exact; multi-fraction `update_fractions` may have small residual; for budget studies, monitor `dz_avg` vs `flux_in - flux_out`.
- `morfac` scaling on avalanching is intentional: with accelerated morphology, the bed needs more relaxation passes per step. Early termination at `n_aval=0` keeps cost bounded.
- `ne_layer` thickness should be the depth-to-bedrock or depth-to-construction layer. If exceeded, structure exposed.
- Hard-structure cells (`structdepth=0` after full erosion) freeze further avalanching at that location — sandbar cannot grow into a dredged channel.

## Common Pitfalls

- ▢ Setting `wetslp=1.0` (= dry value) — wet avalanching never triggers. Symptom: dune face stays vertical underwater.
- ▢ Setting `hswitch` very large (~10 m) — most cells use `wetslp` even on dry beach; over-active avalanching.
- ▢ `struct=1` without `ne_layer` file — model halts.
- ▢ `ne_layer` thickness too small — structure exposed mid-storm; check `structdepth` output.
- ▢ Setting `avalanching=0` then noticing dunes don't retreat — trace to this.
- ▢ Multi-fraction bed with very different `D50` per fraction — avalanching mass transfer can produce locally non-physical fraction ratios in deposition cell.
- ▢ Comparing avalanching events across `morfac` settings — `morfac=1` vs `morfac=10` show different `n_aval` counts but similar net effect; don't compare counts directly.

## Next expansion

- Avaltime calibration recipe.
- Multi-fraction mass-conservation audit walkthrough.
- Comparison: avalanching+transport vs transport-only for storm cases.

## References

- Roelvink et al. 2009 (XBeach avalanching base).
- Soulsby 1997 (repose angles, sediment).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.
