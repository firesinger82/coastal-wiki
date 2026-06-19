---
title: "xbeach mode dispatch"
topic: general
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach_mode_dispatch.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How XBeach branches between `stationary`, `surfbeat` (instationary), and `nonh` modes, how the legacy `instat` parameter maps to the new `wavemodel` keyword, what each mode actually solves, what governs the timestep, and how flow-wave coupling differs per mode. Use this when picking a mode for a new case, debugging mode-incompatibility warnings, or interpreting `wavint`/`maxiter` reporting.

## Source basis

- `params.F90:70-79, 98-101, 286-289, 469, 1359-1369, 1559-1581, 1724, 1740-1745, 2535-2708` — `wavemodel`/`instat` parsing, mode consistency.
- `paramsconst.F90:24-35, 129-131` — constant definitions.
- `wave_timestep.F90:38-115` — wave-mode `select case`.
- `wave_instationary.F90:167-475` — surfbeat solver.
- `wave_stationary_directions.F90:252-728` — actual stationary path.
- `wave_stationary.F90:17-18` — legacy / unwired branch.
- `nonh.F90:160-2427` — non-hydrostatic predictor/corrector.
- `flow_timestep.F90:379-657` — flow loop, wave-flow forces.
- `libxbeach.F90:102-305` — top-level orchestration.
- `timestep.F90:161-646` — timestep / CFL.

## A. `instat` vs `wavemodel`

**Modern**: `wavemodel` keyword (`paramsconst.F90:129-131`):
- `stationary = 0`
- `surfbeat = 1`
- `nonh = 2`

**Legacy**: `instat` only via backward-compat path (`params.F90:2535-2575`). Mapping (`params.F90:2579-2708`):

| `instat` | → `wavemodel` |
|---|---|
| `stat` (0) | `stationary` (or `nonh` if preselected) |
| `bichrom`, `ts_1`, `ts_2` | `surfbeat` |
| `jons`, `swan`, `vardens`, `reuse` | `surfbeat` (or `nonh` if preselected) |
| `stat_table` (10) | `stationary` |
| `ts_nonh` (8) | `nonh` |

Mode consistency:
- `swave` disabled in nonh (`params.F90:1559-1563`).
- Nonh time series only allowed in nonh (`:1571-1575`).
- `ts_1/ts_2` only allowed in surfbeat (`:1576-1581`).

## B. Surfbeat (instationary)

Dispatched via `WAVEMODEL_SURFBEAT` branch in `wave_timestep.F90:83-114` → `wave_instationary` (`:103, 113`).

If `single_dir=1`, stationary directional update runs at `wavint`, but instationary action still advances every step (`wave_timestep.F90:84-103`).

`wave_instationary` workflow:
1. Depth/flow slopes, then directional velocities (`:167-187`).
2. Group/phase speeds: `c = σ/k`, `cg = c*n` (`wave_functions.F90:784-789`).
3. Directional `cgx/cgy = cg * cos/sin (+ WCI velocity)` (`:1176-1188`).
4. Refraction `ctheta` from depth slope and optional WCI gradients (`:1190-1210`).
5. **Wave-action solve**: energy → action by `/σ` (`wave_instationary.F90:189-195`); advect in x, y, θ (`:197-208`); back to energy (`:212-220`).
6. Dissipation/roller update (`:251-345`).
7. Wave forcing/Stokes drift returned to flow (`:468-475`).

This is the workhorse mode for IG-band wave-resolving runs.

## C. Non-hydrostatic (`nonh`)

Initialized only for `WAVEMODEL_NONH` (`libxbeach.F90:212-213`).

- Top level still calls `wave_bc`, but **disables short-wave model by default** (`params.F90:98-101`, hard warning if `swave=1` at `:1559-1563`).
- In `executestep`, `flow_bc/flow` runs if `flow==1` or `wavemodel==NONH` (`libxbeach.F90:296-305`).
- Flow does nonh predictor/corrector around second-order advection (`flow_timestep.F90:635-657`); comment says this "solve[s] short waves" (`:654-656`).

`nonh_cor` dispatch:
- `nonhq3d=1` → reduced 2-layer 2DV/3D predictor/corrector (`nonh.F90:160-180, 201-247`).
- Otherwise → 1-layer predictor/corrector.

- **Predictor**: explicit nonh pressure in momentum equations (`nonh.F90:1591-1609, 2408-2427`).
- **Corrector**: pressure projection — discrete Poisson equation, divergence-free correction (`:1289-1314, 1980-2005`); solver calls at `:1412, 2164`.
- Boundary nonh: water-level/velocity short-wave BCs (`boundaryconditions.F90:668-707`).

Use for short-wave-resolving runup, harbor agitation, surf-zone hydrodynamics where IG band is insufficient.

## D. Stationary (current path is `wave_stationary_directions`)

**Important nuance**: dispatch uses `wave_stationary_directions`, **not `wave_stationary`** (`wave_timestep.F90:38-40, 75-81`). The legacy `wave_stationary.F90` is unwired and even notes itself as untested (`wave_stationary.F90:17-18`).

Runs only at `wavint` or new stationary BC (`wave_timestep.F90:75-82`).

Solver (`wave_stationary_directions.F90`):
- Local pseudo-time / iteration by grid row (`:252-287`).
- Energy → action (`:294-300`); advect x/y/θ (`:302-355`); back to energy (`:357-363`).
- Breaking/friction/vegetation dissipation + roller (`:418-453, 503-519`).
- Iterate to `maxerror` / `maxerror_angle` or `maxiter` (`:619-677`).
- Compute radiation-stress forcing, orbital velocity, Stokes drift at end (`:717-728`).

## E. Top-level dispatch

```
init: read params, init wave/flow/nonh (libxbeach.F90:102-176, 212-213)
executestep:
  compute wet cells / timestep
  wave_bc
  optional wave (wave_timestep.F90:75-115 select case)
  flow (libxbeach.F90:283-305)
```

Nonh is dispatched **inside `flow_timestep.F90:635-657`**, not through `wave_timestep`'s select.

## F. Timestep requirements

| Source | File:Line | Behavior |
|---|---|---|
| Base hydrodynamic CFL | `timestep.F90:461-591` | Grid/depth, velocity, viscosity limits |
| Surfbeat directional refraction CFL | `:632-646` | Adds when `swave=1`, except stationary |
| Stationary internal pseudo-time `dtw` | `wave_stationary_directions.F90:256-277` | From `cgx/cgy/ctheta`, optionally capped by hydro `dt` for WCI |
| Stationary update interval | `timestep.F90:161-179` | At `wavint`; `wavint/maxiter/maxerror` only read for stationary or `single_dir` |
| Nonh: `swave=0` default → no short-wave CFL | `params.F90:98-101` | Practical step is hydro/wave-resolving CFL |
| Explosion limiter `maxdtfac` | `params.F90:286-289` | `50` for stationary/surfbeat, `500` for nonh |

## G. Flow-wave coupling per mode

**Ordering** (every step): waves before flow (`libxbeach.F90:296-305`).

**Wave → flow**:
- Radiation-stress forces enter momentum via `Fx/Fy` (`flow_timestep.F90:564-569, 600-605`).
- Wave orbital velocity affects bed friction (`:534-550`).
- Roller dissipation affects viscosity when `swave=1` (`:379-384`).
- Forces from radiation stresses + roller (`wave_functions.F90:1238-1275`).

**Flow → waves (WCI)**:
- Surfbeat/stationary use smoothed flow/depth means (`wave_functions.F90:24-48`); selected in `wave_timestep.F90:84-102`.
- **Nonh coupling is monolithic in flow**: pressure predictor/projection modifies velocities directly (`flow_timestep.F90:635-657`, `nonh.F90:1980-2005`); no surfbeat radiation-stress wave solve in nonh.

## Decision Guide

| Use case | `wavemodel` | Notes |
|---|---|---|
| IG-band runup, dune erosion, beach response | `surfbeat` | The default; pair with `instat=jons` or `swan` |
| Short-wave-resolving harbor / structure | `nonh` | Higher cost; expects fine grid (Δx ~ Lp/30) |
| Wave climate / equilibrium beach state | `stationary` | Iterates to converge per `wavint` step; cheap |
| Wave overtopping with wave-by-wave detail | `nonh` | `swave=0` automatic |
| 1D bichromatic test | `surfbeat` (legacy `instat=bichrom`) | Maps to surfbeat |
| Reuse prior BC time series | `wbctype=reuse` (surfbeat) | Skips spectral generation |

## Working Rules

- For `surfbeat`, set `wavint` 5-30 s; default OK for Hs ≤ 4 m.
- Stationary mode reports `maxiter` reached as a warning — if frequent, reduce `maxerror` or increase `maxiter`.
- Nonh mode default `swave=0` is correct; ignore short-wave dissipation/breaking parameters in input — they don't apply.
- `single_dir=1` in surfbeat is for cases where directional spread is small; reduces refraction CFL cost ~30%.
- `wbctype` and `wavemodel` must be compatible; old `instat`+old constants are translated but warnings can be confusing — set `wavemodel` explicitly.
- `maxdtfac=500` (nonh default) is very permissive; if your nonh run stalls, reducing to 100 trims explosion checks.

## Common Pitfalls

- ▢ Setting `instat=jons` then expecting nonh — old `instat` defaults to `surfbeat`. Set `wavemodel=nonh` explicitly.
- ▢ Activating `swave=1` in nonh — hard warning; then forced to `0`.
- ▢ Editing `wave_stationary.F90` thinking it's the active branch — actual code is `wave_stationary_directions.F90`.
- ▢ Setting `wavint` very small (~1 s) for stationary — the iterative solver runs every `wavint`, so cost explodes; usually `wavint` ~ wave period is enough.
- ▢ Mixing nonh forcing (`ts_nonh`) with surfbeat run — input parser refuses, but error message confusing.
- ▢ Expecting refraction CFL to govern timestep in nonh — it doesn't because `swave=0`; use hydrodynamic CFL.

## Next expansion

- Stationary solver convergence diagnostics walkthrough (`maxerror_angle`).
- Surfbeat WCI option (`wci=1`) effects and cost.
- Nonh 2-layer (`nonhq3d=1`) vs 1-layer comparison.

## References

- Roelvink et al. 2009 (XBeach surfbeat formulation).
- Smit et al. 2013 (XBeach non-hydrostatic).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.
