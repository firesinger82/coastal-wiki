---
title: "xbeach bed friction"
topic: general
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach_bed_friction.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

What `bedfriction` options are actually accepted in the parser (only 5: `chezy, cf, white-colebrook, manning, white-colebrook-grainsize`), what `fwcutoff` does, where the wave friction coefficient `fw` enters the wave-action sink, how current bed friction is computed in `flow_timestep.F90`, how the Ruessink-style combined wave-current term in flow shear is wired (and that there is no `bedfriction=ruessink` keyword), how spatially varying `bedfricfile` is read, and how grain-size dependency works (`white-colebrook-grainsize`, not `manning_grainsize`). Use this when calibrating bed roughness, debugging high friction near deep boundaries, or wiring grain-size-dependent friction.

## Source basis

- `bedroughness.F90:68-272, 491, 515` — `bedroughness_init`, runtime update, all formulae.
- `params.F90:639-650, 651, 683-731, 1155-1169` — parser, `fwcutoff`, `D50`/`D90` options.
- `paramsconst.F90:65-69` — `BEDFRICTION_*` constants.
- `params.def:196-198` — `fwcutoff` definition.
- `wave_stationary.F90:224-237, 279-283`, `wave_instationary.F90:281-327`, `wave_directions.F90:278-290`, `wave_stationary_directions.F90:418-453` — wave dissipation forms.
- `flow_timestep.F90:120, 176-177, 532-577` — current friction in flow.
- `vsm_u_XB.f90:90-129` — Q3D wave friction.
- `initialize.F90:625-637, 991-1003, 1278-1281, 1390-1395` — `fw`/`bedfriccoef`/`D50top`/`D90top` setup.
- `variables.def:290` — `fw` definition.

## A. `bedfriction` dispatch

**Accepted keywords** (only these): `chezy, cf, white-colebrook, manning, white-colebrook-grainsize`.

There is **no `manning_grainsize`, `ruessink`, or `flat`** keyword in this checkout. Constants in `paramsconst.F90:65-69`; parser in `params.F90:683-687`.

`bedroughness_init` dispatch (`bedroughness.F90:68`):

| Option | Formula | Lines |
|---|---|---|
| `chezy` | `cfu = cfv = g/C²` from `s%bedfriccoef` | `:70-72` |
| `cf` | Direct: `cfu = cfv = s%bedfriccoef` | `:73-75` |
| `manning` | `cf = g·n²/h^(1/3)`, bounded by `mincf/maxcf` | `:90-103` (init), `:208-219` (update) |
| `white-colebrook-grainsize` | `k = 3·D90top` (one fraction) or interface-averaged; `cf = g/(18·log10(12·h/k))²` | `:104-145, 220-259` |
| `white-colebrook` | Roughness from `s%bedfriccoef`, same Colebrook | `:146-164, 260-272` |

## B. `fwcutoff`

Read as "depth greater than which the bed friction factor is not applied"; default `1000` (`params.def:196-198`, `params.F90:651`).

Wave friction dissipation zeroed when depth exceeds cutoff:

| Branch | Code |
|---|---|
| Stationary | `where (s%hh > par%fwcutoff) s%Df = 0` (`wave_stationary.F90:224-229`) |
| Instationary | Same gate (`wave_instationary.F90:281-286`) |
| Directional/spectral | Apply only when `fw>0`, wet, `local depth ≤ fwcutoff` (`wave_directions.F90:278-284`, `wave_stationary_directions.F90:426-432`) |

Default `fwcutoff=1000` effectively never gates; lower (e.g., 5–10 m) to disable wave friction in deep portions of the domain.

## C. Wave bed friction `fw` and wave action sink

`fw` is a spatial array — wave friction coefficient (`variables.def:290`). Initialized from `fwfile` if present, else scalar `fw` (`initialize.F90:625-637`); parsed at `params.F90:639-650`.

Dissipation formulae:

| Branch | `Df` | File:Line |
|---|---|---|
| Stationary | `0.28*ρ*fw*uorb³` with `uorb = π·H/(Trep·sinh(k·h))` | `wave_stationary.F90:224-226` |
| Instationary | `(2/(3π))*ρ*fw*uorb³` | `wave_instationary.F90:281-283` |
| Directional | `(2/(3π))*ρ*fw*uorb³` | `wave_directions.F90:278-281` |
| Stationary directional | `0.28*ρ*fw*uorb³` | `wave_stationary_directions.F90:426-429` |

`Df` enters wave-action/energy sink:
```
dd = dder + ee*(Df + Dveg)/E
```
(`wave_stationary.F90:231-237`, `wave_instationary.F90:288-296`).

Energy density reduced by `dt*dd` (`wave_stationary.F90:279-283`, `wave_instationary.F90:322-327`).

## D. Current bed friction (in `flow_timestep.F90`)

`flow` initializes/updates roughness via `bedroughness_init`/`bedroughness_update` (`flow_timestep.F90:120, 176-177`).

Current bed shear at u/v points:
```
taubx = cfu*ρ*ueu*sqrt((1.16*urms)² + vmageu²) + taubx_add
tauby = cfv*ρ*vev*sqrt((1.16*urms)² + vmagev²) + tauby_add
```
(`flow_timestep.F90:532-552`).

Stress limited to `100*g*ρ*h` (`:542-557`), then enters momentum as `taub/(ρ*h)` in acceleration term before velocity update (`:563-577`).

## E. Combined wave-current friction

The combined wave-current effect is the **Ruessink-style magnitude term**: current × `sqrt((1.16*urms)² + current_magnitude²)`. Explicit comment "Ruessink et al, 2001" at `flow_timestep.F90:535, 550`.

This is **not a `bedfriction=ruessink` dispatch option** — it is the shear-stress formulation used after `cfu/cfv` are chosen. Common confusion.

For Q3D / vertical sediment velocity, `s%fw(i,j)` passed into `vsm_u_XB` (`flow_timestep.F90:956-972`); inside that, wave friction contributes via `Df = facDf*0.283*ρ*fw*uorb³` and `cf = fw/2` (`vsm_u_XB.f90:90-91, 126-129`).

## F. Spatially varying `bedfricfile`

- Allowed only if `bedfriction` is explicitly set; otherwise model halts (`params.F90:694-700`).
- Used only for `chezy, cf, manning, white-colebrook` (`:702-705`).
- Grainsize Colebrook does **not** read coefficient file — clears `bedfricfile` (`:728-731`).

If present:
- File existence + size `(nx+1, ny+1)` checked on XBeach grids (`:707-716`).
- Read row-wise into `s%bedfriccoef` at init (`initialize.F90:991-1003`), else `s%bedfriccoef = par%bedfriccoef`.

## G. Grain-size dependency

The explicit grain-size-dependent flow friction option is **`white-colebrook-grainsize`**, not `manning_grainsize`.

Uses `D90top` for roughness:
- One grain class: `k = 3*D90top`.
- Multiple classes: interface-averaged.
- Then Colebrook `cf` (`bedroughness.F90:104-145`).

`D50/D90` parsed at `params.F90:1155-1169` with different defaults under XBeach-G settings.

`D50top, D90top` allocated as top-layer bed-fraction-weighted means (`initialize.F90:1278-1281, 1390-1395`).

During morphology, top representative sizes updated for flow-friction/output (`morphevolution.F90:1170-1178`).

`D50top` also appears in extra acceleration-related bed shear: added shear scales with `min(D50top, h)` (`bedroughness.F90:491, 515`).

## Decision Guide

| Goal | Setting |
|---|---|
| Standard sandy beach | `bedfriction=manning`, `bedfriccoef=0.022` |
| Direct Cd (current literature) | `bedfriction=cf`, `bedfriccoef=0.003` |
| Logarithmic profile, sandy | `bedfriction=white-colebrook`, `bedfriccoef=0.05` (m roughness) |
| Multi-fraction with grain-size friction | `bedfriction=white-colebrook-grainsize`, multi `D90` per fraction |
| Spatially varying friction (vegetated patches, mixed substrate) | `bedfricfile=...`, choose `chezy/cf/manning/white-colebrook` |
| Disable wave friction in deep portion | Lower `fwcutoff` to ~5 m |
| Storm hindcast with calibrated `fw` | Set scalar `fw=0.012`, default fine; or `fwfile` for spatial |
| Wave-current shear physics | Built-in via Ruessink term — no separate switch |

## Working Rules

- `bedfriction=manning` is the most common production choice (Manning n directly available from sediment maps).
- `mincf/maxcf` bounds `cf` from Manning/Colebrook to prevent crazy values in shallow cells. Defaults are sane.
- `fw=0.01–0.02` typical for sand (Soulsby 1997). Set higher (~0.05) for cobble/gravel.
- For dune-impact storms, `fwcutoff` rarely matters — depth is shallow throughout; for offshore-extending grids, lower it (e.g., 10 m) to avoid spurious wave dissipation.
- "Ruessink combined wave-current shear" is automatic — no flag. The 1.16 factor is a calibrated coefficient, do not change without literature support.
- Grain-size friction (`white-colebrook-grainsize`) couples bed friction to morphology — top-layer sediment changes change friction. Useful for adaptive cases; adds compute cost.
- `bedfricfile` size is `(nx+1, ny+1)` (NODE-based, not cell-based). Off-by-one is a common error.

## Common Pitfalls

- ▢ Setting `bedfriction=manning_grainsize` — not accepted; use `white-colebrook-grainsize`.
- ▢ Setting `bedfriction=ruessink` — not accepted; the Ruessink term is automatic.
- ▢ Wave friction looks too small — check `fwcutoff`; default 1000 is fine, but if you set it to 5 thinking it's a cap, you're disabling friction in most of the domain.
- ▢ `bedfricfile` row order — XBeach reads rows from south to north (low j to high j) — check orientation.
- ▢ Setting `fwfile` without `fw` = 0 — both can be set; spatial overrides scalar.
- ▢ Grain-size Colebrook with `bedfricfile` — silently overrides; choose one.
- ▢ Manning n very high (>0.05) on smooth sand — model accepts but underpredicts current speed; n=0.022-0.030 is realistic for sand.

## Next expansion

- Wave-friction calibration recipe vs observation.
- Q3D friction details for sediment fluxes (`vsm_u_XB`).
- `bedfricfile` generation tooling for vegetated patches.

## References

- Soulsby 1997 (bed friction coefficients).
- Ruessink et al. 2001 (combined wave-current shear).
- White-Colebrook (Colebrook 1939).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.
