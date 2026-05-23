---
title: "roms baroclinic 3d"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ROMS source code 직접 분석 (models/ROMS/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/roms_baroclinic_3d.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How ROMS advances 3D momentum (`step3d_uv`) and tracers (`step3d_t`), how the s-coordinate transform builds `Hz`, how vertical velocity is diagnosed, how the equation of state is selected, and where Coriolis and surface fluxes enter. Use this when configuring stretching parameters, choosing EOS, or debugging surface/bottom flux setup.

## Source basis

- `ROMS/Nonlinear/main3d.F:441-1067` — orchestration: bulk fluxes, omega, wvelocity, step3d_uv, step3d_t.
- `ROMS/Nonlinear/step3d_uv.F` — 3D momentum new-time update and implicit vertical advection.
- `ROMS/Nonlinear/rhs3d.F` — RHS assembly: advection, Coriolis, pressure-gradient call.
- `ROMS/Nonlinear/step3d_t.F` — tracer corrector with Hadvection/Vadvection dispatch and implicit vertical mixing.
- `ROMS/Nonlinear/omega.F`, `wvelocity.F` — terrain-following flux and diagnostic m/s vertical velocity.
- `ROMS/Utility/set_scoord.F`, `ROMS/Nonlinear/set_depth.F` — Vtransform/Vstretching, `Hz`, `z_w`, `z_r`.
- `ROMS/Nonlinear/rho_eos.F` — nonlinear (Jackett-McDougall) and linear EOS branches.
- `ROMS/Nonlinear/set_data.F` — surface flux ingestion (wind stress, heat, salt).

## A. 3D momentum prediction

- `step3d_uv` is called after `rhs3d` assembly and updated depths (`main3d.F:999`).
- New-time update is explicit: `u(...,nnew) = u(...,nnew) + DC * ru(...,nrhs)` (and same for `v`/`rv`) (`step3d_uv.F:359-360, 826`).
- Horizontal momentum advection is **compile-time** selected (`rhs3d.F:743-967`):
  - `UV_C2ADVECTION` → centered-2.
  - `UV_C4ADVECTION` → centered-4.
  - else → 3rd-order upstream-biased with velocity-dependent hyperdiffusion.
- Vertical momentum advection fluxes are built from `W` (and `W_stokes` if active), then inserted into `ru/rv` (`rhs3d.F:1135-1613`).
- With `OMEGA_IMPLICIT`, vertical advection is split off and solved tridiagonally using `Wi` before final 3D coupling (`step3d_uv.F:507-590, 974-1058`).
- Pressure gradient enters via `CALL prsgrd`; compile-time variant chosen from `prsgrd31/32/40/42/44`, all loading baroclinic PGF directly into `ru/rv` (`rhs3d.F:92`, `prsgrd.F:16-26`).

## B. Tracer (T, S) equation

- Tracer corrector is `step3d_t`, called after 3D momentum and turbulence/biology/sediment cor-steps (`main3d.F:1067`, `step3d_t.F:40-72`).
- Horizontal advection dispatch is **per-tracer per-direction** via `Hadvection(itrc,ng)%<scheme>`: `CENTERED2`, `CENTERED4`, `UPSTREAM3`, `AKIMA4`, `MPDATA`, `HSIMT`, `SPLIT_U3` (`step3d_t.F:432, 451, 472, 633`).
- Vertical advection dispatch likewise per-tracer: `SPLINES`, `CENTERED2`, `CENTERED4`, `AKIMA4`, `UPSTREAM3`, `SPLIT_U3` (`step3d_t.F:936, 985, 1027, 1048, 1069, 1144`).
- Vertical mixing is applied implicitly via `Akt` tridiagonal solve (spline or standard form), updating `t(...,nnew,...)` (`step3d_t.F:1660-1789`).
- Nudging/relaxation source: `Tnudgcof * (tclm - t)` when `LnudgeTCLM` is on (`step3d_t.F:1866-1874`).
- Surface/bottom tracer fluxes injected as `FC(:,0)=dt*btflx`, `FC(:,N)=dt*stflx` (`pre_step3d.F:911-924`); `set_data` populates `stflux`/`btflux` (`set_data.F:415-557`).

## C. Vertical coordinate transform (s-coordinate)

| Choice | Behavior | Code |
|---|---|---|
| `Vtransform=1` | `hc = min(hmin, Tcline)` (bounded; "old" form) | `set_scoord.F:170-178` |
| `Vtransform=2` | `hc = Tcline` (Shchepetkin "new" form) | `set_scoord.F:170-178` |
| `Vstretching=1` | Song-Haidvogel `Cs(s)` from `theta_s/theta_b` | `:184-233` |
| `Vstretching=2` | Shchepetkin surface/bottom blend | `:240-315` |
| `Vstretching=4` | Shchepetkin double-cosine | `:393-471` |
| `Vstretching=5` | Souza et al. quadratic-stretched (high-res surface) | `:486-529` |

`Hz` is computed in `set_depth.F:147-223` as `z_w(k) - z_w(k-1)` after building `z_w/z_r` from the `Vtransform`/`Vstretching` choice. This is the active layer thickness used by all 3D solvers — every advection/mixing operator references it.

## D. Vertical velocity diagnostic

- `omega` (terrain-following flux-form, `m^3/s`) and `wvelocity` (true `m/s`) are called each 3D step (`main3d.F:543-544`).
- `W` is integrated upward from continuity by subtracting horizontal flux divergence at each level (`omega.F:225-230`).
- Free-surface-consistent correction enforces `W=0` at top in s-coordinates by subtracting linear-in-depth moving-surface contribution (`omega.F:295-347`).
- Diagnostic `wvel` (true vertical velocity) is reconstructed from `W` (and `Wi` if implicit), `pm*pn`, and geometric terms from `z_r`/`z_w` (`wvelocity.F:229-269`).

## E. Equation of state

- Nonlinear branch (`#ifdef NONLIN_EOS`, `rho_eos.F:108, 247-250`): Jackett & McDougall polynomial form for `(T, S, p)`.
- Linear branch (`#ifndef NONLIN_EOS`, `:688-704`): `rho = R0 - Tcoef*(T - T0) + Scoef*(S - S0)`.
- No separate UNESCO-1980 runtime branch in this tree; that path is folded into the polynomial form.

## F. Coriolis

- Applied when `UV_COR` is enabled: `cff = 0.5 * Hz * fomn`, added to `ru` and subtracted from `rv` (plus Stokes-Coriolis if `WEC`) (`rhs3d.F:562-619`).
- `fomn = f / (pm*pn)` is carried in grid state (`mod_grid.F:41, 198-199`).
- f-plane: `beta=0 ⇒ f=f0`. Beta-plane: `f = f0 + beta*(y - yorigin)` (`ana_grid.h:233-234, 886-896`).

## G. Surface fluxes

- Wind stress (`sustr/svstr`) is loaded from forcing file or analytical, with optional curvilinear-grid rotation (`set_data.F:573-603`).
- If `BULK_FLUXES` is enabled, `bulk_flux` computes air-sea fluxes before VBC setup (`main3d.F:441-449`).
- Shortwave (`srflx`) and net surface heat tracer flux (`stflux(:,:,itemp)`) are set in `set_data.F:258-267, 415-424`.
- Freshwater/salinity surface forcing via `stflux(:,:,isalt)` from `swflux`/`EminusP` pathways (`set_data.F:474-508`).
- These fluxes are applied through the tracer-equation vertical flux BCs (`pre_step3d.F:901-916`).

## Decision Guide

| Goal | Setting |
|---|---|
| Resolve thermocline depth | `Vstretching=4`, `theta_s ≈ 7`, `theta_b ≈ 0.4`, `Tcline ≈ depth_of_thermocline` |
| Resolve bottom boundary layer | `Vstretching=4` with `theta_b > 1` |
| Coastal shallow shelf | `Vtransform=2`, `theta_s=5`, `theta_b=0.4`, `hc=10–50 m` |
| Linear stratification test | `NONLIN_EOS` off; set `R0/T0/S0/Tcoef/Scoef` |
| Bulk fluxes from atm. data | `BULK_FLUXES` on; provide `Tair, Pair, Qair, rain, Uwind, Vwind, swrad, lwrad` |
| Prescribed heat flux only | `BULK_FLUXES` off; provide `shflux, swrad`; salt via `swflux` |
| Tracer monotonicity (sediment, biology) | `Hadvection = HSIMT` or `MPDATA` per tracer |
| Smooth tracer field, dissipation OK | `Hadvection = UPSTREAM3` |

## Working Rules

- Choose `Vstretching/Vtransform` early and keep them constant across forcing files, restart files, and child grids — the `Hz` field is the cornerstone of everything else.
- For shelf/coastal applications, `Vtransform=2` is preferred; the unbounded `hc=Tcline` keeps the surface-following property intact in deep+shallow combined domains.
- When using `BULK_FLUXES`, `srflx` is still required separately (penetrating shortwave) — do not assume `bulk_flux` handles solar.
- Per-tracer advection choice lets you keep T/S smooth (`UPSTREAM3`) but enforce monotonicity on positive-definite tracers (`HSIMT`) — exploit this.
- `OMEGA_IMPLICIT` adds robustness in tidal regimes with thin layers; expect ~10% cost increase but fewer CFL blowups.

## Common Pitfalls

- ▢ Mixing `Vtransform=1` initial conditions with `Vtransform=2` runtime — `Hz` mismatches silently corrupt T/S.
- ▢ Setting `theta_s` very high (>10) without proportional vertical resolution — produces unrealistically thin surface layers and timestep restrictions.
- ▢ Forgetting to set `srflx` when `BULK_FLUXES` is on — surface heat budget loses penetrating solar.
- ▢ Choosing `MPDATA` for T/S in long runs without rotation invariance check — known to introduce small spurious cross-frontal mixing.
- ▢ Linear EOS with realistic forcing — gives unrealistic abyssal stratification; only valid for idealized tests.

## Next expansion

- Cross-link to `roms_advection.md` (per-scheme details).
- Cross-link to `roms_vertical_mixing.md` (`Akt` provenance for the implicit step).
- Document `prsgrd.F` variants and slope-error trade-offs (separate note).

## References

- Shchepetkin & McWilliams 2003, 2005, 2009 (vertical coordinate, split-explicit, FB-AB3-AM4).
- Jackett & McDougall 1995 (EOS polynomial).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
