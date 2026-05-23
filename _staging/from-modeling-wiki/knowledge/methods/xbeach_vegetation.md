---
slug: xbeach_vegetation
title: XBeach Vegetation (vegatt, swvegatt, multi-section, Mendez-Losada drag)
model: xbeach
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/xbeach/source_code/trunk/src/xbeachlibrary
---

## Scope

How XBeach models vegetation: per-species multi-section vertical structure, drag-force formulation, short-wave dissipation by vegetation (Mendez-Losada / Suzuki), per-cell vegetation type via `veggiemapfile`, parameter file (`veggiefile`) format (note: `N` not `NDmax`), porous canopy flow option, and how forces couple back into the flow momentum equation. Use this when wiring vegetation forcing for marsh, mangrove, or seagrass cases, or interpreting `Fvegu/Fvegv/Dveg` outputs.

## Source basis

- `vegetation.F90:29-728` — `veggie_init`, `vegatt`, `swvegatt`, `momeqveg`, `bulkdragcoeff`.
- `libxbeach.F90:184, 301-305` — init + per-step call ordering.
- `params.F90:127, 1327-1339` — vegetation switch + file parameters.
- `params.def:447-455` — definitions.
- `readkey.F90:420-424, 625-635` — species-file `key=value` parser.
- `flow_timestep.F90:563-604` — momentum-equation coupling.
- `wave_stationary.F90:235-236`, `wave_instationary.F90:294-295`, `wave_stationary_directions.F90:442-444`, `wave_directions.F90:290` — `Dveg` consumption.
- `variables.def:271, 277-280` — `vegtype, Nveg, Fvegu/v` definitions.

## A. Entry / call sequence

`vegetation.F90` exposes `veggie_init` and `vegatt` (`:69-70`).

- `veggie_init(s, par)` once during model init (`libxbeach.F90:184`).
- `vegatt(s, par)` per timestep when `par%vegetation==1` (`:301-305`).

**Per-timestep order**:
1. `wave(s, par)`.
2. `vegatt(s, par)`.
3. `flow(s, par)`.

Vegetation drag forces computed **before** flow momentum update. `Dveg` used by waves is from previous vegetation update (except at init) (`vegetation.F90:122-125`).

Inside `vegatt`:
- Standard: `swvegatt` (short-wave dissipation) + `momeqveg` (momentum drag) (`:336-342`).
- If `par%porcanflow==1`: `porcanflow` instead (`:318-321`).

## B. Parameters / input format

Main switch in `params.txt`: `vegetation` (0/1) (`params.F90:127`).

When enabled, must provide:
- `veggiefile` — list of species filenames.
- `veggiemapfile` — spatial vegetation type map.
- `Trep` — representative wave period.
- Optional: `vegnonlin, vegcanflo, veguntow, porcanflow`.

(`params.F90:1327-1339`; `params.def:447-455`).

`veggiefile` structure:
- `par%nveg = count_lines(par%veggiefile)`.
- Each line is one species-spec filename (`vegetation.F90:102-112`).

**Per-species file** uses `key = value...` syntax (`readkey.F90`):

| Key | Description | Line |
|---|---|---|
| `isCanopy` | Canopy-flow flag | `vegetation.F90:161` |
| `nsec` | Number of vertical sections | `:168` |
| `ah` | Vector of section heights | `:180` |
| `bv` | Stem diameter (non-canopy only) | `:182-185` |
| `N` | Stem density | `:182-185` |
| `Cd` | Drag coefficient | `:182-185` |

**Important**: code uses `N`, **not `NDmax`** (older docs). Documented as stems per horizontal area `[m⁻²]` (`vegetation.F90:57`, `variables.def:277`). Read as double vector then `nint(...)` to integer (`:184`).

## C. Drag formulation

For standard vegetation momentum drag, layer-integrated quadratic drag.

**`veguntow=1`** (`vegetation.F90:513-516`):
```fortran
Fvgtu = h_layer * 0.5 * Cdveg * bveg * Nveg * (ueu * vmageu)
Fvgtv = h_layer * 0.5 * Cdveg * bveg * Nveg * (vev * vmageu)
```

**`veguntow=0`** (`:517-520`):
```fortran
Fvgtu = h_layer * 0.5 * Cdveg * bveg * Nveg * (uu * vmagu)
Fvgtv = h_layer * 0.5 * Cdveg * bveg * Nveg * (vv * vmagu)
```

`h_layer = max((min(aht, watr) − ahtold), 0d0)` — the submerged vertical extent of this section.

So the formula is closer to:
```
F = ρ · ∫_(submerged) [0.5 * Cd * b * N * |u|*u dz]
```
not just `0.5*ρ*Cd*N*bv*|u|*u` flat.

Final multiplication by `rho`: `s%Fvegu = Fvgu*par%rho` (`:563-564`). Internal arrays `[N/m²]` (`variables.def:279-280`).

## D. Wave dissipation by vegetation

Computed in `swvegatt` (`vegetation.F90:347`):

1. Loop over vegetation cells + sections (`:370-375`).
2. Clip section height to local water depth (`:379-382`).
3. Compute vertical wave-orbital integral term `hterm` (`:384-385`).
4. Compute dissipation:
   ```
   Dvgt = 0.5/sqrt(π) * ρ * Cdveg * bveg * Nveg
        * (0.5*k*g/sigm)³
        * (hterm − htermold)
        * H³
   ```
   (`:387-388`).

Section explicitly notes correction for elevated layers per **Suzuki et al. 2012** (`:387`).

Module header cites:
- Short-wave + IG-wave + flow + setup attenuation.
- Nonlinear wave effects per Van Rooijen et al. 2016 (`:29-39`).

`Dveg` stored in `s%Dveg` (`:400`); consumed in wave dissipation:
- Stationary: `s%Df + s%Dveg` (`wave_stationary.F90:235-236`).
- Instationary: `s%Df + s%Dveg` (`wave_instationary.F90:294-295`).
- Stationary directions: `s%Df + s%Dveg` (`wave_stationary_directions.F90:442-444`).

**Note**: `Dveg` is missing in `wave_directions.F90:290` (explicit code comment).

**Bulk drag coefficient** (Mendez-Losada 2004) when `Cdveg < 0`:
- `vegatt` calls `bulkdragcoeff` (`:327-329`).
- Hard-wires `myflag = 2` (`:728`) with comment "Mendez and Losada (2004), eq. 40" (`:760-763`).

## E. Multi-layer vegetation

**Important distinction**: `nveg` = number of **species** (not vertical layers).
- Set from line count in `veggiefile` (`vegetation.F90:102-104`).

**Vertical layering** is `nsec` per species (`:53, 168`).

The model supports multiple vertical sections:
- Arrays `ah, Cd, bv, N` allocated to length `nsec` (`:174-178`).
- Mapped into 3D fields `Cdveg/ahveg/bveg/Nveg` over `s%nsecvegmax` (`:205-214`).
- Runtime loops `m=1, s%nsecveg(i,j)` in both wave dissipation and momentum drag (`:375, 487`).

For canopy-flow vegetation (`isCanopy=1`), `nsec > 1` is **rejected** (`:169-172`).

## F. Coupling to flow momentum

Vegetation forces written to `s%Fvegu, s%Fvegv` (`vegetation.F90:563-564`).

Flow solver acceleration includes:
- u-momentum: `+ s%Fvegu(i,j)/(par%rho*s%hu(i,j))` (`flow_timestep.F90:563-568`).
- v-momentum: `+ s%Fvegv(i,j)/(par%rho*s%hv(i,j))` (`:600-604`).

Velocity update: `s%uu = s%uu − par%dt*dudt` (`:576`). Since `Fvegu` has the sign of `u*|u|`, this term acts as **drag/deceleration**.

## G. Spatial distribution

There is **no separate boolean vegetation mask**. `veggiemapfile` is the spatial distribution:
- Read into integer `s%vegtype(i, j)` over `(nx+1, ny+1)` (`vegetation.F90:130-154`).
- `vegtype = 1` corresponds to first species in `veggiefile` (`:130-131`).

Cells with `vegtype > 0`: receive species' `nsec, Cd, ah, bv, N` (`:223-232`).
Cells with `vegtype <= 0`: no vegetation, all properties zeroed (`:240-245`).

Documented as "vegetation type index" (`variables.def:271`).

## Decision Guide

| Application | Setup |
|---|---|
| Salt marsh wave attenuation | `vegetation=1`, `veggiefile` with grass species (1 section), `Cdveg ≈ 1.0`, `N ≈ 100–1000/m²`, `bv ≈ 5e-3 m` |
| Mangrove forest | Multi-section: roots, trunk, canopy with different `bv, Cd, N` |
| Seagrass meadow (flexible) | `vegnonlin=1` for nonlinear reduction (Van Rooijen 2016) |
| Reef / coral | `Cdveg=1.5–2.0`, `bv ≈ 0.1 m`, low `N` |
| Auto-calibrate `Cd` | Set `Cdveg < 0` → activates Mendez-Losada bulk drag |
| Porous canopy (dense vegetation) | `porcanflow=1`, `nsec=1` only |
| Flow-only friction (no wave dissipation) | Use `bedfricfile` instead, not vegetation |
| Wave-only dissipation | Set vegetation but only short waves matter — long-wave/flow effects are coupled |

## Working Rules

- `vegtype=0` cells are fully transparent — useful for vegetation-free patches in a vegetated domain.
- `nsec` 2-3 sections is enough for most marsh/seagrass cases. More than 5 rarely improves accuracy.
- Stem density `N` is in stems per horizontal m² (not per stem volume). Stem density of 200/m² is typical for spartina.
- `Cd=1.0` is a reasonable default for slender stems (per Mendez-Losada empirical fit). Use `Cdveg=−1` to auto-calibrate from wave conditions.
- Vegetation drag **decelerates** flow — verify by output `Fvegu, Fvegv` near vegetated patches.
- For storm hindcasts, vegetation persists through inundation; the model handles submergence automatically via `h_layer = min(aht, watr)`.
- `Dveg` missing in `wave_directions.F90:290` is a known limitation — directional wave model does not include vegetation dissipation (only standard surfbeat does).

## Common Pitfalls

- ▢ Using `NDmax` parameter name from old docs — actual key in species file is `N`.
- ▢ `vegtype` map size — must be `(nx+1, ny+1)`, NODE-based.
- ▢ Setting `nsec=2` with `isCanopy=1` — rejected, use `nsec=1` for canopy.
- ▢ `Cdveg=0` (zero) — completely disables drag silently. Use `Cdveg<0` for auto-calibrate.
- ▢ Forgetting `Trep` — vegetation dissipation formula needs representative period.
- ▢ Using `wave_directions` (advanced directional wave model) and expecting vegetation dissipation — currently not implemented.
- ▢ Single-species runs with multi-species `veggiemapfile` — non-existent vegtype indices silently zero.

## Next expansion

- Mendez-Losada `bulkdragcoeff` formula details.
- Suzuki 2012 elevated-layer correction validation.
- Comparison: porcanflow vs standard vegetation for dense stands.

## References

- Mendez & Losada 2004 (bulk drag coefficient).
- Suzuki et al. 2012 (elevated-layer wave dissipation).
- Van Rooijen et al. 2016 (nonlinear vegetation effects).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.
