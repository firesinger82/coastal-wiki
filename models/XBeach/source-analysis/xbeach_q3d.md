---
title: "xbeach q3d"
topic: general
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach_q3d.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

Q3D activation via `q3d=1` (or auto with `form=FORM_VANRIJN1993`), `vsm_u_XB.f90` building vertical sigma profiles with log + boundary-layer + upper regions, **Rouse-weighted** (not depth-averaged) sediment velocity `ue_sed/ve_sed`, vertical mass-flux/Stokes correction in the profile, the depth-averaged 2DH transport machinery still in `transus` (Q3D feeds different velocities, doesn't replace `par%sus/par%bed`), the Van Rijn 1993 vertical concentration integration over `kmax` layers, and when Q3D justifies the cost (surf-zone undertow, near-bed-concentrated suspended load, asymmetry on vertically structured velocity).

## Source basis

- `params.F90:122, 1139-1152` — Q3D activation, parameters.
- `params.def:39, 273` — keyword definitions.
- `flow_timestep.F90:957-985` — Q3D dispatch in flow.
- `vsm_u_XB.f90:7-326` — vertical structure routine.
- `morphevolution.F90:94-1830` — 3D arrays, vertical concentration, transus dispatch.

## A. Activation

`q3d` keyword in `params.txt`: `par%q3d = readkey_int(..., 'q3d', 0, 0, 1, ...)` (`params.F90:122`).

When `q3d=1` OR `form == FORM_VANRIJN1993`, reads Q3D parameters: `vonkar, vicmol, kmax, sigfac, deltar, rwave` (`:1139-1150`).

Sets `par%nz = par%kmax`. If Q3D inactive: `par%kmax = 1` for allocation compatibility (`:1146-1152`).

**Switch in flow**: `par%nz > 1` → calls `vsm_u_XB`; otherwise `s%ue_sed = s%ue, s%ve_sed = s%ve` (depth-averaged) (`flow_timestep.F90:957-985`).

## B. vsm_u_XB vertical structure

Takes depth-averaged Eulerian `ue, ve`, wave quantities, roughness, fall velocity, and `n` vertical layers (`vsm_u_XB.f90:7-45`).

Returns:
- `sigz, uz, vz, ustz, nutz` — vertical profiles.
- `ue_sed, ve_sed` — representative sediment advection velocities.

Builds vertical sigma grid (`:207-212`).

Velocity profile in three regions (`:255-294`):
- Near-bottom linear layer.
- Bottom boundary / log-type layer.
- Upper layer.

Optional GLM/Stokes corrections (`:295-303`).

**Sediment velocity is Rouse-weighted vertical average** (NOT depth mean):
```
ue_sed = Σ(dsig · uz · crel) / Σ(dsig · crel)
```
(`:308-326`).

## C. Log profile + vertical sediment integration

Log expressions in bottom + upper profile parts (`:156-170, 219-237, 270-292`).

For sediment concentration, **Van Rijn 1993** path (`morphevolution.F90:1748-1830`):
- Creates vertical grid from reference height to water depth (`:1748-1757`).
- Integrates vertical concentration profile layer by layer (`:1759-1806`).
- Stores `s%ccz` (`:1808-1813`).
- Converts to depth-averaged suspended equilibrium concentration (`:1815-1830`).

## D. Wave-induced sediment fluxes vs depth-averaged

`vsm_u_XB` explicitly includes wave mass flux/Stokes effects (`:61-69`):
- Mass flux has vertical distribution.
- Bottom shear reacts to Stokes drift at bottom.
- Stokes drift subtracted from computed profile.

Computes wave mass flux `Qw, Qwe, Qwx, Qwy` (`:96-116`).
Constructs vertical Stokes drift (`:239-253`).
Modifies `uz/vz` with Stokes + roller/flux corrections (`:295-303`).

Without Q3D: transport uses depth-averaged sediment velocities directly.

## E. par%sus/par%bed scaling unchanged

Q3D **changes velocities** used by **same transport machinery**.

In `transus`, if `par%nz > 1`, face sediment velocities interpolated from `s%ue_sed/s%ve_sed`; otherwise standard face Eulerian `s%ueu, s%vev` (`morphevolution.F90:225-295`).

Suspended + bed-load still scaled by same switches:
- `Sus = par%sus*(...)`, `Sub = par%bed*(...)` (`:273-279`).
- `Svs = par%sus*(...)`, `Svb = par%bed*(...)` (`:347-354`).

So **Q3D does NOT replace `par%sus/par%bed`**; feeds different velocities into existing 2DH flux formulas.

## F. Coupling to morphology

Time-step driver: flow → sediment → bed update.
- `flow` (`libxbeach.F90:305`).
- `transus` (`:307`).
- `bed_update` when `morphology=1` (`:309-310`).

`transus` stores per-fraction fluxes into `s%Susg, s%Svsg, s%Subg, s%Svbg` (`morphevolution.F90:577-584`).

`bed_update` computes bed change from gradients of those fluxes (`:735-748` 2D, `:777-788` 1D); updates `zb, dzbnow, dzbdt, sedero` (`:751-797`).

## G. Cost vs accuracy

`kmax`: 1 to 1000; defaults to 100 in Q3D block (`params.F90:1146`); `kmax=1` = no vertical structure.

Cost when active:
- `flow_timestep.F90:957-972` calls `vsm_u_XB` inside full `(i,j)` grid loop.
- Morphology allocates 3D arrays over `nx+1, ny+1, kmax` (`:94-106`).
- Van Rijn vertical concentration loops over `par%kmax` per active cell (`:1753-1806`).

Accuracy gain: resolved near-bed weighted transport, undertow/Stokes structure, vertical concentration profile.

## H. When Q3D needed

Q3D most useful when **depth-averaged flow is poor proxy for sediment-carrying velocity**:
- Surf-zone undertow / Stokes compensation.
- Strong wave-induced vertical shear.
- Suspended load concentrated near bed.

For steep slopes, transport is already slope-sensitive via `bdslpeffmag/bdslpeffini/bdslpeffdir` (`morphevolution.F90:383-453`); Q3D helps when slopes coincide with vertical shear or near-bed concentration gradients.

For asymmetric wave currents, XBeach adds skewness/asymmetry velocity `s%ua` via `RvR` or `vT` (`:162-168`); Q3D needed when asymmetry should act on vertically structured, sediment-weighted velocity.

## Decision Guide

| Application | Setup |
|---|---|
| Standard surf-zone storm | `q3d=1, kmax=20-50` |
| Plain 2DH (cheap) | `q3d=0` (default) |
| Van Rijn 1993 transport | Auto Q3D enabled (or set `q3d=1`) |
| Soulsby-Van Rijn (default) | `q3d=0` (Q3D not required) |
| Long-term morfac | Cost prohibitive — verify Q3D really needed |
| Validation of vertical concentration profile | `q3d=1, kmax=50+`, output `ccg` |
| Rip-current resolution | `q3d=1` highly recommended |

## Working Rules

- `kmax=20-50` typically sufficient for surf-zone applications.
- Check cost: Q3D adds ~50-100% runtime over 2DH.
- Verify Rouse number consistency: `wf/(κ·u*)` ~ 1 typical for surf-zone sand.
- Output `ccz` to confirm vertical concentration structure realistic.
- Q3D + multi-fraction: arrays scale `(nx+1, ny+1, kmax, ngd)`; memory grows fast.
- For Korean coast, Q3D for storm-surge surf zone where undertow matters.

## Common Pitfalls

- ▢ Setting `q3d=1` thinking it changes `par%sus/par%bed` — those switches unchanged.
- ▢ Comparing 2DH and Q3D results expecting same depth-averaged transport — Q3D feeds different effective velocity.
- ▢ Setting `kmax=1` thinking it's depth-averaged — same as Q3D off.
- ▢ Running Q3D with `form != FORM_VANRIJN1993` and expecting vertical concentration — only Van Rijn 1993 has vertical concentration integration.
- ▢ Memory blow-up with `kmax > 100` in 2D — cubic scaling.

## References

- Van Rijn 1993 (Sediment Transport, Parts I-III).
- Rouse 1937 (suspended load profile).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.
