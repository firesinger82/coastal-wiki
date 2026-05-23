---
title: "roms open boundaries"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ROMS source code 직접 분석 (models/ROMS/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/roms_open_boundaries.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

Per-edge OBC dispatch via `LBC(edge, var, ng)`, the actual implementations of free-surface (Chapman explicit/implicit, clamped, radiation+nudge), 2D momentum (Flather, Reduced, Shchepetkin Maison-2010, radiation+nudge), 3D momentum (Orlanski radiation, clamped, closed with `gamma2` slip control), tracers (radiation with inflow/outflow `obc_in/out` switching, nudging, clamped, gradient/closed), the `M3CLM` climatology nudging path through TLM/ADJ kernels, volume-conservation OBC adjustment via `obc_flux_tile/set_DUV_bc_tile`, and recommended combinations for typical applications. Use this when wiring a regional ROMS run, debugging boundary noise, or interpreting `Cha/Fla/RadNud` keywords.

## Source basis

- `mod_param.F:340-373, 1731-1798` — `LBC` shape, fields, allocation.
- `inp_decode.F:1617-1658` — `Cha/Che/Cla/Clo/Fla/Rad/RadNud/Red/Shc` keyword parsing.
- `zetabc.F:121-713` — free-surface BCs.
- `u2dbc_im.F:145-783, v2dbc_im.F:150-774` — 2D momentum.
- `u3dbc_im.F:99-676, v3dbc_im.F:99-676` — 3D momentum.
- `t3dbc_im.F:98-615` — tracers.
- `rhs3d.F:718-738`, `tl_rhs3d.F:810-836`, `ad_rhs3d.F:2432-2457` — M3CLM nudging.
- `obc_volcons.F:131-358` — volume conservation.
- `step2d_FB_LF_AM3.h:626-1749` — calls in 2D fast steps.

## A. Free surface (zetabc.F)

Per-edge dispatch via `LBC(edge, isFsur, ng)`:

| Type | Lines (W/E/S/N) |
|---|---|
| `Chapman_explicit` | `:186/345/504/663` (formula `:198-199` etc.) |
| `Chapman_implicit` | `:209/368/527/686` (with `1/(1+C)` factor) |
| `Clamped` | `:233/392/551/710` (copies `BOUNDARY%zeta_*`) |
| Radiation + nudge | `:121-176/280-334/439-493/598-652` (uses `FSobc_in/out` by sign) |

`Chapman_implicit` is preferred for stability; uses new interior `zeta(...,kout)`.

## B. 2D momentum (u2dbc_im.F, v2dbc_im.F)

Per-edge dispatch via `LBC(edge, isUbar/isVbar, ng)`:

| Type | u edge:line | v edge:line |
|---|---|---|
| `Flather` | W:`224 (267-285)`, E:`575 (618-636)` | S:`230 (299-317)`, N:`608 (677-695)` |
| `Reduced` | W:`400-432`, E:`751-783` | S:`432-464` |
| `Shchepetkin` (Maison 2010, with limiter `Co`) | W:`296-364`, E:`647-715` | S:`328-396`, N:`706-774` |
| Radiation+nudge | W:`145-214`, E:`496-564` | W:`150-220`, S:`528-597` |

`Flather` ties normal barotropic velocity to external `zeta` and boundary velocity — most common for SSH-driven open boundaries.

## C. 3D momentum (u3dbc_im.F, v3dbc_im.F)

Orlanski-type implicit upstream radiation, plus clamped, gradient, closed:

| Type | u (W/E/S/N) | v (S/N/W/E) |
|---|---|---|
| Radiation/Orlanski | `:99-169/241-310/383-453/541-610` | `:99-169/241-310/383-453/541-610` |
| Clamped | `:184/326/468/626` | `:184/326/468/626` |
| Closed normal | `:222-226/364-368` (zero) | `:222-226/364-368` (zero) |
| Closed tangential (with `gamma2`) | `:507-518/665-676` | `:507-518/665-676` |

`Closed` zeros normal velocity; tangential is free-slip or no-slip via `gamma2` (1.0 = free-slip; 0.0 = no-slip).

## D. Tracers (t3dbc_im.F)

Per-tracer dispatch via `LBC(edge, isTvar(itrc), ng)`:

| Type | Lines (W/E/S/N) |
|---|---|
| Radiation | `:98-168/232-301/366-435/500-569` |
| Inflow vs outflow switch (sign of `dTdt*dTdx`) | `:127-132/261-266/395-400/529-534` |
| Inward radiation suppression | `:135/269/403/537` |
| Nudging (`LnudgeTCLM` or scalar `Tobc_in/out`) | `:119-126/253-260/387-394/521-528` |
| Clamped | `:179/313/447/581` |
| Closed/gradient (zero-gradient) | `:194-213/328-347/462-481/596-615` |

Inflow/outflow distinction is critical: tighter relaxation on inflow (`obc_in ≪ obc_out`) keeps interior solution leaving while locking incoming BC.

## E. M3CLM (3D momentum climatology nudging)

`LnudgeM3CLM=.TRUE.` → use spatial `CLIMA(ng)%M3nudgcof`; otherwise scalar `M3obc_in/out`:
- `u3dbc_im.F:112-130, 254-272, 396-414, 554-572`.
- `v3dbc_im.F:112-130, 254-272, 396-414, 554-572`.

Same switch adds **interior** 3D momentum climatology tendency (`rhs3d.F:718-738`).

TLM carries tangent (`tl_rhs3d.F:810-836`); ADJ backpropagates (`ad_rhs3d.F:2432-2457`).

TLM/ADJ OBC files mirror M3CLM branch (`tl_u3dbc_im.F:111-119`, `tl_v3dbc_im.F:111-119`, `ad_u3dbc_im.F:659-667`, `ad_v3dbc_im.F:659-667`).

For data assimilation: M3CLM is full-domain nudging; OBC files apply only at boundaries.

## F. Volume conservation

`obc_flux_tile` integrates open-boundary area/flux for `VolCons(edge, ng)`:
- W/E/S/N: `obc_volcons.F:131-183`.
- Globally sums; sets correction velocity `ubar_xs = bc_flux / bc_area` (`:191-228`).

`set_DUV_bc_tile` applies `ubar_xs` to barotropic fluxes `Duon/Dvom`:
- W/E/S/N: `:310-358`.

Called in 2D fast steps (`step2d_FB_LF_AM3.h:626-627, 1748-1749`).

This corrects spurious volume drift from Flather BC discretization — essential for long-term integrations.

## G. LBC structure

Shape and meaning (`mod_param.F:340-353`):
```
LBC(1:4, nLBCvar, Ngrids)
edge: 1=W, 2=S, 3=E, 4=N
var:  isFsur, isUbar, isVbar, isUvel, isVvel, isTvar(itrc), ...
```

Fields (`:357-373`): `Chapman_explicit, Chapman_implicit, clamped, closed, Flather, gradient, nudging, radiation, reduced, Shchepetkin`.

Allocated for NLM/TLM/ADJ (`:1731-1798`).

Input keyword → flag mapping (`inp_decode.F:1617-1658`):

| Keyword | Sets |
|---|---|
| `Cha` | Chapman_explicit |
| `Che` | Chapman_implicit |
| `Cla` | clamped |
| `Clo` | closed |
| `Fla` | Flather (forces free-surface acquire) |
| `Rad` | radiation |
| `RadNud` | radiation + nudging (sets `acquire`) |
| `Red` | reduced |
| `Shc` | Shchepetkin (forces free-surface acquire) |

## H. Common combinations

| Application | Free surface | 2D momentum | 3D momentum | Tracers |
|---|---|---|---|---|
| Open ocean with external SSH | `Cha` (or `Che`) | `Fla` | `Rad`/`RadNud` | `RadNud` |
| Coastal with one land edge | Same on open + `Clo` on land | Same | Same | Same |
| Closed basin (test) | `Clo` everywhere | `Clo` | `Clo` | `Clo` |
| Tide-only forcing | `Cha` | `Fla` | `Clo` (or `Rad`) | `Cla`/`Clo` |
| Strong inflow from external model | `Cla` | `Cla` | `Cla` | `RadNud` (tight inflow) |

Examples in source:
- `roms_cblast.in:184-191` — Cha/Fla/RadNud.
- `roms_wcofs.in:184-190` — coastal with land edge.
- `roms_natl.in:184-191` — closed basin.

## Decision Guide

| Domain | Recommendation |
|---|---|
| Korean coast nesting in HYCOM | `Che + Fla + RadNud` (3D momentum + tracers) |
| Tide-only run | `Cha + Fla` (no nudging, tracers `Cla` if S/T fixed) |
| Long climate integration | All `RadNud` with weak nudging; verify volume conservation |
| Idealized test case | `Clo` (no leakage) |
| Inflow-dominated boundary | `Cla` (clamped) on inflow side, `RadNud` on outflow |
| Storm surge with open ocean | `Che + Fla` for primary; tracers may be `Cla` |

## Working Rules

- `Che` (Chapman implicit) > `Cha` (explicit) for stability — use unless replicating older paper.
- `Fla` requires SSH and barotropic velocity in BC files; pair with `Che` always.
- `RadNud` time scales: inflow ~1 day, outflow ~1 year (factor 100-1000 ratio).
- For closed basins, do not use `Clo` for free surface — use `Cla` with constant SSH.
- Volume conservation correction (`obc_flux_tile`) is automatic when Flather active; verify via `VolCons` diagnostic output.
- M3CLM full-domain nudging is computationally expensive; use only when DA-driven correction needed.

## Common Pitfalls

- ▢ `Fla` without `Che`/`Cha` — runtime error; Flather requires SSH BC.
- ▢ `RadNud` with same `obc_in` and `obc_out` — defeats the purpose; use ratio.
- ▢ `Clo` on free surface for closed basin — actually no SSH evolution; basin can't drain.
- ▢ Missing `M3nudgcof` field with `LnudgeM3CLM=T` — runtime error.
- ▢ Volume drift in long runs — verify `Fla` is set (not `Cla`); volume conservation only with Flather.
- ▢ Tangential `gamma2=0.5` for partial slip — usually `gamma2=1.0` (free-slip) is fine for ocean; `0.0` for closed estuary.

## Next expansion

- Volume-conservation diagnostic walkthrough.
- M3CLM coupling with HYCOM example.
- Inflow/outflow nudging timescale calibration.

## References

- Marchesiello et al. 2001 (radiation BCs).
- Mason et al. 2010 (Shchepetkin BC).
- Chapman 1985 (Chapman free-surface).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
