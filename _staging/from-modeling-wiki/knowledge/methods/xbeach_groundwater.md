---
slug: xbeach_groundwater
title: XBeach Groundwater (gwflow=1, Darcy/MODFLOW, swash infiltration, GW-flow coupling)
model: xbeach
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/xbeach/source_code/trunk/src/xbeachlibrary
---

## Scope

XBeach groundwater module: activation via `gwflow=1` (NOT `groundwater`), Darcy-style horizontal flow with optional MODFLOW-like turbulent reduction, non-hydrostatic GW via Poisson solver, surface-GW exchange (sign convention `infil` positive surface→GW; split into connected/unconnected swash cells), stability via FTCS-style timestep limit, aquifer parameters (`kx/ky/kz`, `aquiferbot`, `gw0`, `por`), and coupling to flow continuity (subtracts `s%infil`) and bed friction. Use this when configuring XBeach-G groundwater or extreme runup with infiltration.

## Source basis

- `groundwater.F90:27-1643, 27-34, 54-95, 109-178, 276-1532` — module.
- `libxbeach.F90:168-305` — call sites.
- `params.F90:121-749, 824-876, 1156-1160, 2671` — parameter parsing.
- `params.def:38, 252-268, 305` — definitions.
- `timestep.F90:594-742` — stability.
- `flow_timestep.F90:536, 733-751` — coupling to flow.
- `bedroughness.F90:292-419` — friction coupling.
- `morphevolution.F90:817-830` — morphology coupling.
- `variables.def:190-198` — output vars.

## A. Entry, call timing

`groundwater.F90` exports `gw_init, gw_bc, gwflow` (`:27-34`).

`gw_init` called during init after wave/flow/discharge, before rainfall/sediment (`libxbeach.F90:168-179`). Arrays allocated unconditionally; state initialized only when `par%gwflow=1` (`groundwater.F90:54-76`).

Per timestep:
- `gw_bc` after wave BC, before flow BC.
- `gwflow` after waves/vegetation, before main flow solve (`libxbeach.F90:293-305`).

## B. Activation flag

**`gwflow`**, NOT `groundwater`.

Declared "Turn on groundwater flow" (`params.def:38`); read as `par%gwflow = readkey_int(..., 'gwflow', ..., 0, 1, strict=T)` (`params.F90:121`).

GW parameters only read when `par%gwflow=1` (`:824-876`).

## C. GW flow equation

Horizontal velocity = Darcy hydraulic-gradient flow.

Module documents Darcy velocity in "surface water" volume terms; GW level updates divided by porosity (`groundwater.F90:276-280`).

Head gradients (`:761-784`):
```
dheaddx = (gwhead(i+1) - gwhead(i)) / dsu
```

Laminar: `vel = -Kin * headgrad` (`:1349-1363`).

Turbulent/MODFLOW (`:1414-1434`):
- Start `vest = -Kin * headgrad`.
- Reduce effective conductivity when velocity exceeds Reynolds-based threshold.

Selected by `gwscheme`: `laminar` or `turbulent` (old names `darcy`/`modflow` accepted) (`params.F90:858-866`).

For non-hydrostatic GW: head solved by Poisson, not just averaged to top (`groundwater.F90:362-383`).

**No literal `Boussinesq` symbol**. Coupling to XBeach non-hydrostatic waves: `WAVEMODEL_NONH` adds dynamic pressure to GW top-head condition (`:296-302, 352-360, 741-759`).

## D. Surface-GW exchange

Sign convention (`:282-285`):
- `infil` positive = surface → GW.
- `gww` positive = upward GW → sea.

Output var `infil` is exchange rate, surface-to-GW positive (`variables.def:190-193`).

**Split** into connected + disconnected (swash) cells (`groundwater.F90:304-319`):
- Unconnected infiltration: `gw_unconnected_infil` for wet cells where GW below bed (`:584-641`).
- Exfiltration from GW above bed: negative infiltration (`:324-326`).

Updates:
```
gwlevel += dt * infiluncon / por
zsupd = zs - dt * infiluncon
```
(`:330-334`).

Connected vertical exchange via `gww`; limited by GW storage and available surface water (`:472-510`).

Hydrostatic exchange via `gw_calculate_hydrostatic_w` (`:512-527, 1439-1532`).

Total to flow: `s%infil = infiluncon + infilcon + infilhorsw` (`:538-540`).

Free-surface continuity **subtracts `s%infil`** — positive infiltration lowers SW (`flow_timestep.F90:733-751`).

## E. GW level boundary conditions

Initial:
- `aquiferbot` / `aquiferbotfile` — aquifer bottom.
- `gw0` / `gw0file` — initial GW head.
(`groundwater.F90:76-95`, `params.F90:837-850`).

Initial `gwlevel` clipped between aquifer bottom and bed (`:109-117`).

`gw_bc` boundary application:
- Front/top: copy interior head and bottom (`:142-148`).
- Back/bottom: copy interior or apply stored `gw0back` based on `tideloc` and `paulrevere` (`:149-156`).
- Left/right: copy adjacent interior `gwbottom, gwhead, gwlevel` (`:158-166`).
- Boundary `gwlevel` recomputed as `min(gwhead, zb)` on top/bottom edges (`:173-178`).

After `gwflow`, level/head/curvature/bottom/vertical exchange mirrored at boundaries (`:541-575`).

## F. Coupling to swash zone

Code explicitly treats disconnected cells as "swash infiltration, seepage" (`:304-307`).

Connection controlled by wetness + bed-GW distance:
```
wetz==1 .and. zb-gwlevel < connectcrit
```
(`:309-313`).

For XBeach-G, infiltration-friction coupling defaults on when GW active (`params.F90:749-755`). Bed roughness uses `s%infil` to alter BL/shear stress (`bedroughness.F90:292-419`). Main flow applies `taubx_add` from infiltration effects (`flow_timestep.F90:536`).

Morphology adjusts GW/SW during accretion/erosion when `gwflow=1` (`morphevolution.F90:817-830`).

## G. Time-step considerations

Stability enforced only for hydrostatic GW (`par%gwflow=1 .and. par%gwnonh=0`) (`timestep.F90:594-595`).

Diffusion-style FTCS limit:
```
dt <= CFL · dsc² · por / (2 · kx)
```
(`:603-607`); 2D adds `dt <= CFL · dnc² · por / (2·ky)` (`:615-620`).

If GW dominates: log "Groundwater condition is too high" (`:730-742`).

GW exchange fluxes limited by available surface water, aquifer storage, dt, por (`groundwater.F90:1154-1643`).

## H. Aquifer parameters

Core hydraulic params (`params.def:252-255`):
- `kx, ky, kz` — Darcy permeability x/y/z.
- Runtime turbulent fields stored as `Kx, Ky, Kz, Kzinf` (`variables.def:195-198`).

Defaults when GW active (`params.F90:828-836`):
- XBeach-G mode: `kx=0.01, ky=kx, kz=kx`.
- Other: `kx=0.0001, ky=kx, kz=kx`.

Other controls: `dwetlayer, aquiferbot, aquiferbotfile, gw0, gw0file, gwnonh, gwfastsolve, gwscheme, gwReturb, gwheadmodel, gwhorinfil` (`params.def:256-268`, `params.F90:837-875`).

Porosity: `por` default 0.4 (range 0.3-0.5) (`params.def:305`, `params.F90:1155-1160`); scales GW storage updates throughout (`groundwater.F90:276-1636`).

## Decision Guide

| Application | Setup |
|---|---|
| XBeach-G gravel beach | `gwflow=1, kx=0.01, gwscheme=turbulent` |
| Sand beach with infiltration | `gwflow=1, kx=0.0001, gwscheme=laminar` |
| Coral / permeable substrate | `gwflow=1, kx=0.001`, increased porosity |
| Hard substrate (concrete) | `gwflow=0` (default) |
| Non-hydrostatic GW + waves | `gwflow=1, gwnonh=1, wavemodel=nonh` |
| Validation against wells | `gwflow=1, gw0` from observations, output `gwlevel, gwhead` |
| Swash zone infiltration | Always with `gwflow=1` for runup studies |

## Working Rules

- `kx` is hydraulic conductivity (m/s); typical: sand 1e-4, gravel 1e-2, fine sand 1e-5.
- Porosity 0.4 is fine for sand; 0.3 for compact mud, 0.5 for clean gravel.
- For runup studies, GW dominates dt — small `kx` keeps timestep large.
- `gwReturb` controls turbulent transition; default OK for typical beaches.
- Output `infil, gwlevel, gwhead` for diagnostics.
- `aquiferbot` should be below all expected GW levels; otherwise GW gets clipped.
- For Korean cobble/gravel beaches: `gwflow=1, kx=0.01, gwscheme=turbulent`.

## Common Pitfalls

- ▢ Looking for `groundwater` flag — actually `gwflow`.
- ▢ Missing `gw0` IC — model crashes or initializes unrealistic.
- ▢ Setting `kx` very high (>0.1) — timestep crashes (FTCS limit).
- ▢ Hot-start without GW state preserved — GW level resets.
- ▢ Boundary copy of `gwlevel` for wide domain — front/back may be inconsistent; use `gw0back`.
- ▢ Comparing GW levels expecting actual head — `gwlevel` is min(gwhead, zb), not raw head.

## References

- McCall et al. 2014 (XBeach-G).
- Bear 1972 (groundwater hydrology).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.
