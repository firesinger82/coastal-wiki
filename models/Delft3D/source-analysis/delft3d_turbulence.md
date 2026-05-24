---
title: "delft3d turbulence"
topic: general
canonical_source: self
citation_status: verified
verification_method: "Delft3D source code 직접 분석 (models/Delft3D/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/delft3d_turbulence.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How Delft3D-FLOW selects between constant, algebraic, k-l, and k-ε vertical turbulence (note: option keyword is `Tkemod`, not `TKEDIS`), what each closure actually computes, where stability functions live (algebraic only), surface and bottom BCs for k and ε, how `vicww/dicww/vicuv/dicuv` are assembled, the background-viscosity floor (`vicoww/dicoww`), and how mixing coefficients couple into the momentum solver `uzd`. Use this when picking a closure, reading mixing-coefficient outputs, or debugging unrealistic mixed-layer depth.

## Source basis

- `flow2d3d_io/src/input/dimrd.f90:439-464`, `rdhyvd.f90:278-296` — `Tkemod` parsing.
- `flow2d3d_kernel/src/compute/turclo.f90` — closure dispatch + algebraic/k-l/k-ε vicww assembly (`:39-45, 190-537`).
- `flow2d3d_kernel/src/compute/tratur.f90` — k and ε transport equation (`:47-1055`).
- `flow2d3d_kernel/src/main/trisol.f90:1522-1535, 1555-1565, 2031-2071` — call sites.
- `flow2d3d_kernel/src/compute/uzd.f90:51-1229` — momentum vertical diffusion.
- `flow2d3d_kernel/src/inichk/initur.f90:248-318`, `tkecof.f90:178-197` — initial fields.
- `flow2d3d_data/include/physco.igs:43-47` — `vicoww/dicoww` declarations.
- `flow2d3d_kernel/src/compute/redvic.f90:68-77`, `reddic.f90:68-77` — background floor enforcement.

Note: this is the sigma-FLOW path. Z-model has parallel `z_turclo.f90` / `z_tratur.f90` with the same closure structure.

## A. Option dispatch (Tkemod)

`Tkemod`, not `TKEDIS`, selects the 3D turbulence model (`dimrd.f90:439-464`):

| Option | `ltur` | Behavior |
|---|---|---|
| (default) | `0` | Algebraic |
| `k-l` | `1` | k-l two-equation |
| `k-epsilon` | `2` | k-ε two-equation |
| `constant` | (`0`) | Uniform vertical mixing, separate path |

Constant sets uniform vertical `vicww=dicoww` from `Vicoww/Dicoww` (`turclo.f90:190-199`).

`tkedis` is **not** the option dispatch — it's an **internal-wave TKE dissipation source/sink array** passed into turbulence transport (`trisol.f90:1555-1565`); used in TKE/ε equations at `tratur.f90:665-666, 813-814`.

## B. K-ε equations

`tratur` solves TKE and dissipation transport implicitly: sources explicit, sinks implicit (`tratur.f90:47-75`). Loop over turbulence quantities at `:576-579`.

**TKE equation**:
- Vertical diffusion uses `vicww/pransm` plus molecular viscosity (`:628-649`).
- Buoyancy: `buoflu = vicww * bruvai / sigrho` (`:658-664`).
- Unstable buoyancy: source via `−min(0, buoflu)`; stable buoyancy + `tkedis` enter diagonal sink scaled by `k` (`:663-666`).
- Shear production: `2 * (vicmol + vicww) * S²` (`:698-710`).
- Dissipation: uses ε with Newton linearization in k-equation (`:904-912`).

**ε equation**:
- Stable stratification switches buoyancy off; unstable: `−vicww * bruvai / sigrho` (`:789-806`).
- Production/source: `cep1 * (buoflu − tkepro) * ε / k`; `tkedis` contributes to implicit term (`:810-814`).
- Shear production: `2 * cmukep * cep1 * k * S²` (`:858-868`).
- Dissipation: `cep2 * ε² / k`, Newton-linearized (`:917-924`).

## C. Stability functions

Richardson number from Brunt-Väisälä over shear:
- `bruvai = -g·dρ/dz / ρ`, `rich = bruvai / shear` (`turclo.f90:253-275`).

**Algebraic model** stability functions:
- Stable: `fl = exp(-2.3*Ri)`, `fs = (1+3.33*Ri)^1.5 / (1+10*Ri)^0.5` (`:347-356`).
- Unstable: `fl = (1−14*Ri)^0.25`, `fs = 1` (`:357-360`).
- Mixing length and algebraic eddy viscosity/diffusivity at `:362-386`.

**K-L** uses same `fl`, but `fs = 1` (`:404-416`).

**K-ε** uses standard algebraic relation, **no separate stability function** in `turclo`:
- `vicww = cmukep * k² / ε`, `dicww = vicww` (`:422-432`).

## D. Surface and bottom BC

**TKE surface** (wind-driven):
- `tkewin = sqrt((windsu² + windsv²) / cmukep) / ρ_w` (`tratur.f90:942-955`).

**TKE bottom** (logarithmic wall):
- Eulerian bottom speed, Chezy/friction average.
- `k = U² / (s² · sqrt(Cmu))` (`:978-991`).

**ε surface**:
- `epswin = cewall * tkewin^1.5 / zw` (`:1005-1023`).

**ε bottom**:
- `tkebot = U² / (s² · sqrt(Cmu))`.
- `ε = cewall * tkebot^1.5 / z₀` (`:1040-1055`).

Initialization uses same wall ideas:
- Surface/bottom k: `initur.f90:248-262`.
- Surface/bottom ε: `:300-309`.

## E. VICOFF/DICOFF assembly

Vertical interface coefficients in `turclo` as `vicww/dicww`:

| Closure | Formula | Lines |
|---|---|---|
| Constant | `vicww=vicoww`, `dicww=dicoww` | `turclo.f90:194-199` |
| Algebraic | `vicww = cmukl * L * sqrt(k)`; `dicww = vicww/fs` | `:366-386` |
| K-L | `vicww = dicww = cmukl * L * sqrt(k)` | `:392-416` |
| K-ε | `vicww = cmukep * k² / ε`; `dicww = vicww` | `:422-432` |

Surface/bottom interface coefficients overwritten/limited:
- Surface wind viscosity/diffusivity + k-ε override (`:450-474`).
- Bottom logarithmic stress velocity (`:476-489`).
- Cap at 10 m²/s (`:512-517`).

Layer-center horizontal coefficients:
- `vicuv = 0.5*(vicww(k) + vicww(k-1)) + background + HLES`; same for `dicuv` (`:528-537`).

## F. Background viscosity / minimum k, ε

Background vertical coefficients: `vicoww, dicoww` (`physco.igs:43-47`).

Minimum restriction applied via helpers:
- `redvic = max(vicww, vicoww)` unless low-Re damping (`redvic.f90:68-77`).
- `reddic = max(dicww, dicoww)` unless low-Re damping (`reddic.f90:68-77`).

Initial minima:
- `tkecof` initializes turbulence to `1e-7` (`tkecof.f90:178-197`).
- `initur` enforces minimum k (`:314-318`).
- ε initialized with `max(1e-7, ...)` (`:287-309`).

## G. Coupling to momentum

`trisol` order:
1. `turclo` (compute `vicww`) before momentum (`trisol.f90:1522-1535`).
2. Momentum solve `uzd`.
3. `tratur` (transport k/ε) when `ltur > 0` (`:2031-2071`).

Momentum solver `uzd` uses `vicww` in vertical diffusion:
- Vertical diffusion coefficients: `vicmol + redvic(vicww)` from adjacent water-level points (`uzd.f90:947-959`).
- Coefficients enter tridiagonal `aak/bbk/cck` (`:960-969`).
- Matrix row-scaled, vertically solved by forward/back substitution (`:1090-1128, 1213-1229`).

## H. Algebraic option clarification

**Important correction**: `Algebraic` is **not** simply uniform background mixing. It computes Richardson-damped mixing-length viscosity with wind and bottom friction contributions (`turclo.f90:280-386`).

**Uniform background mixing is the `Constant` option**:
- Read `Tkemod, Vicoww, Dicoww` (`rdhyvd.f90:278-296`).
- Apply uniform `vicoww/dicoww` (`turclo.f90:194-199`).

## Decision Guide

| Application | `Tkemod` | Notes |
|---|---|---|
| Idealized 2D / 2DH | `constant` | Set `Vicoww=1e-5` |
| Estuarine tidal mixing | `algebraic` | Cheap, captures Richardson damping |
| Stratified shelf / fjord | `k-epsilon` | Captures TKE budget; pair with HLES horizontal mixing if needed |
| Coastal upwelling | `k-epsilon` | Best for surface boundary layer |
| Lake / reservoir thermal | `k-l` or `k-epsilon` | Length-scale variants both work |
| Sediment-laden flow | `k-epsilon` | TKE drives suspension; output `vicww` for diagnostic |
| Background mixing only | `constant` | Or `algebraic` with very small Richardson sensitivity |

## Working Rules

- For `k-ε` runs, output `RTUR1` (k) and `RTUR2` (ε) to TRIM-MAP for diagnostics. Surface k spike at strong winds is normal.
- `vicoww` (background) typical 1e-6 to 1e-5 m²/s; never zero.
- Internal-wave dissipation `tkedis` is small in coastal seas; significant in deep stratified fjords.
- For shallow tidal flats, `algebraic` is sufficient and 30% cheaper than `k-ε`.
- HLES (Horizontal Large Eddy Simulation) sets `vicuv` background — orthogonal to vertical closure choice.
- Surface BC: `tkewin` requires wind stress; if wind is weak, surface k floors at 1e-7.
- Bottom BC: depends on `Chezy/Manning/White-Colebrook` choice; ensure roughness map is consistent.

## Common Pitfalls

- ▢ Looking for `TKEDIS` keyword — it's `Tkemod`. `tkedis` is the internal-wave source array, not the option.
- ▢ Setting `Tkemod=algebraic` thinking it's uniform mixing — it's Richardson-damped mixing-length. Use `constant` for uniform.
- ▢ K-ε with cold-start `k=ε=0` — singular dissipation; always init to `1e-7` minimum.
- ▢ Confusing `vicww` (vertical viscosity) with `vicuv` (horizontal viscosity at layer centers).
- ▢ Setting `Vicoww=0` — model accepts but `vicww` can become spuriously small in stratified zones.
- ▢ Comparing `vicww` output across closures expecting same magnitude — k-ε can produce 10× algebraic in active mixing regions.
- ▢ Forgetting that Z-model uses `z_turclo.f90` / `z_tratur.f90` — same closure structure but different layer mechanics.

## Next expansion

- Cross-link to `delft3d_drying_flooding.md` (KFS interaction with turbulence).
- HLES horizontal mixing interaction with `vicuv`.
- Z-model parallel turbulence walkthrough.

## References

- Rodi 1980 (algebraic and two-equation closures).
- Burchard & Petersen 1999 (k-ε in coastal models).
- Delft3D-FLOW Theory Manual (Deltares).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/delft3d/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src`. Auto-draft = false; review_required = true.
