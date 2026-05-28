---
title: "efdc turbulence"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_turbulence.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How EFDC+ runs the original Mellor-Yamada 2.5 closure (CALQQ1 / CALQQ2T + CALAVB), how `ISTOPT(0)` selects Galperin / Kantha-Clayson / Kantha 2003 stability functions, how the modern GOTM_Turbulence module replaces it when `ISGOTM > 0`, and how `q²` and `q²L` boundary conditions are imposed at surface and bottom. Use this when picking a closure, swapping in GOTM, or interpreting `AV/AB/AQ` output. **수평 운동량 확산 (HMD, Smagorinsky)은 본 노트 범위 밖** — [[efdc_dispersion]] 참조.

## Source basis

- `calqq1.f90`, `calqq2t.f90` — `q²` (= QQ) and `q²L` (= QQL) equation assembly and tridiagonal solve.
- `calavb.f90` — vertical viscosity / diffusivity assembly with stability functions.
- `mod_var_global.f90:1003, 1091, 1103, 1105-1107` — array storage definitions.
- `input.f90:621-685` — input cards C12 (background mixing, max), C12A (`ISTOPT`), C12B (`ISGOTM`).
- `hdmt.f90:1274, 1283`; `hdmt2t.f90:533-579, 875-964, 989` — main-loop dispatch and BC setup.
- `GOTM_Turbulence/mod_gotm.f90`, `mod_turbulence.F90` — GOTM integration.

## A. Entry points

| Path | Driver | Calls |
|---|---|---|
| Original MY2.5 (3TL) | `HDMT` | `CALAVB` then `CALQQ1` (`hdmt.f90:1274, 1283`) |
| Original MY2.5 (2TL) | `HDMT2T` | `CALAVB` then `CALQQ2T` (`hdmt2t.f90:533, 577, 989`) |
| GOTM (`ISGOTM > 0`) | `HDMT2T` | `Advance_GOTM(ISTL)` replaces both (`hdmt2t.f90:535-579`) |

`CALQQ1` and `CALQQ2T` solve for:
- `QQ = q²` (turbulent intensity squared).
- `QQL = q²L` (later converted to `DML = QQL/QQ`).

## B. Stability functions (CALAVB)

Stability functions live in **CALAVB**, not in `CALQQ*`. `ISTOPT(0)` selects:

| `ISTOPT(0)` | Family | File:Line |
|---|---|---|
| default (not 2/3) | Galperin et al. | `calavb.f90:44-51` |
| `2` | Kantha-Clayson 1994 | `:53-62` |
| `3` | Kantha 2003 | `:64-73` |

Richardson-number form:
- `RIQ = −GP * HP * DML² * DZIG * (B(k+1) − B(k)) / QQ` (clamped) (`:150-152`).
- `SFAV = SFAV0 * (1 + SFAV1*RIQ) / ((1 + SFAV2*RIQ)*(1 + SFAV3*RIQ))` (`:153`).
- `SFAB = SFAB0 / (1 + SFAB1*RIQ)` (`:154`).

Then:
- `AB = SFAB * DML * HP * sqrt(QQ) + AVBXY` (`:155`).
- `AV = SFAV * DML * HP * sqrt(QQ) + AVOXY` (`:156`).

Both depth-normalized afterward (`:157, 158`). Background `AVOXY/AVBXY` come from card C12 (`input.f90:621-633`: `AVO, ABO, AVMX, ABMX`).

## C. Production and dissipation

- **Buoyancy**: `PQQB = AB * GP * HP * DZIG * (B(k+1) − B(k))` (`calqq2t.f90:274`; 3TL `calqq1.f90:326`).
- **Shear**: `PQQU = AV * DZIGSD4U * (du/dz)²` (`calqq2t.f90:276`); same for `PQQV` (`:277`).
- `q²` RHS: gets `2*PQQ` (consistent with `QQ = q²` while production is TKE-style) (`:278-279`).
- `q²L` RHS: `CTE3TMP*PQQB + CTE1*(PQQU+PQQV)` plus vegetation/device terms (`:280`).

`CTE3TMP` = `CTE3` if `DELB > 0`, else `CTE1` (stable vs unstable buoyancy switch) (`:267-269`).

**Dissipation** is implicit in the tridiagonal diagonal:
- `q²`: `+ 2*DELT * QQSQR / (CTURBB1 * DML * HP)` (`calqq2t.f90:353`).
- `q²L`: `+ DELT * (QQSQR/(CTURBB1*DML*HP)) * (1 + CTE4*DML²*FPROX)` (`:355`).

`FPROX` = wall proximity function (`aaefdc.f90:1517-1528`).

## D. CALQQ1 (3TL) vs CALQQ2T (2TL) variant

- `CALQQ2T` uses dynamic timestep `DTDYN` when `ISDYNSTP /= 0` (`calqq2t.f90:47-53`); `CALQQ1` switches `DT2/DT` by `ISTL` (`calqq1.f90:50-57`).
- `CALQQ2T` uses current `QQ/QQL` directly in flux assembly (`:130-152`); `CALQQ1` uses `QQ1/QQL1` for `ISTL==2` and `QQ2/QQL2` (doubled) for 3TL (`:137-205`).
- `CALQQ2T` adds vegetation / MHK / structure implicit sink terms into the matrix diagonal (`:353-356, 383-386, 411-414`); `CALQQ1` lacks these in the diagonal formulas.

There is **no literal `AB ln` symbol** in this source — that nomenclature appears to be from older documentation; the actual variant difference is `CALQQ1` vs `CALQQ2T`.

## E. Storage (AV / AB / AQ / AVMX)

| Symbol | Meaning | Lines |
|---|---|---|
| `AB(LCM,KCM)` | Vertical diffusivity (depth-normalized, m/s — physical m²/s ÷ depth) | `mod_var_global.f90:1091` |
| `AV(LCM,KCM)` | Vertical viscosity (depth-normalized) | `:1105` |
| `AQ(LCM,KCM)` | Diffusivity for `QQ/QQL` | `:1103` |
| `AVOXY` | Spatially varying background `AVO` | `:1106` |
| `AVBXY` | Spatially varying background `ABO` | `:1107` |
| `AVMX` | Maximum `AV` cap from input | `:1003` |

Note: code uses `AVMX`, **not `AVOMX`** (older docs). Maximum limit applies via `AVMX*HPI`, `ABMX*HPI` (`calavb.f90:273-276`).

## F. ISTOPT(0) dispatch

`ISTOPT(0)` is read from card C12A (`input.f90:641-661`). It does **not** select GOTM (that is `ISGOTM`). It selects original-EFDC coefficient behavior inside CALAVB:

- Default Galperin if `!= 2, 3`.
- `==2`: Kantha-Clayson 1994.
- `==3`: Kantha 2003 (also changes `SQLDSQ = 0.377/0.628` for `AQ/QQL` diffusion ratio in `calqq*.f90:109-111`).

## G. GOTM integration (ISGOTM)

`ISGOTM` from card C12B (`input.f90:666-685`).

When `ISGOTM > 0`:
- `Init_GOTM` sets up GOTM turbulence + tridiagonal init (`mod_gotm.f90:17-25`).
- `Advance_GOTM(ISTL)` replaces `CALAVB` (`hdmt2t.f90:535-579`).

Per-step bridge:
1. EFDC buoyancy frequency `NN` and shear frequency `SS` passed in (`mod_gotm.f90:78-156`).
2. Each EFDC water-column copied into 1D GOTM arrays (`:271-288`).
3. `do_turbulence` called (`:290-292`).
4. GOTM `num/nuh` copied back into EFDC `AV/AB` (`:294-299`).

GOTM internal: `do_turbulence` calls production, stability functions, TKE eq, length-scale eq, then Kolmogorov-Prandtl `μ_t = c_μ * sqrt(k) * L` for first-order turbulence (`mod_turbulence.F90:2727-2756`). MY option inside GOTM dispatched by `tke_method == tke_MY` → `q2over2eq` (`:2863-2872`).

This gives access to GOTM's k-ε, k-ω, GLS-family closures while keeping EFDC's hydrodynamics core unchanged.

## H. Surface / bottom BCs for q² and q²L

Original EFDC sets `QQ(L,0)` (bottom) and `QQ(L,KC)` (surface) **before** solving CALQQ2T:

- Non-wave path: bottom from `TBX/TBY`, surface from `TSX/TSY` (`hdmt2t.f90:875-889`).
- Corner-corrected path: modifies bottom stress weighting (`:892-931`).
- Wave path: includes current + wave bottom stress (`:939-964`).

These enter the `q²` tridiagonal RHS at boundaries (`calqq2t.f90:361, 393-399`).

The `q²L` equation does **not** inject explicit Dirichlet values; it relies on vertical diffusion + wall proximity dissipation `FPROX` (`:355, 385, 413`).

For GOTM-MY:
- `q2over2_bc`: log-layer Dirichlet `u_τ² * b1^(2/3) / 2`; Neumann zero (`mod_turbulence.F90:3555-3560`).
- `q2l_bc`: log-layer Dirichlet `2*κ*ki*(zi+z₀)`; Neumann `−2*sqrt(2)*sl*κ²*ki^1.5*(zi+z₀)` (`:3964-3969`).

## Decision Guide

| Goal | Setting |
|---|---|
| Standard estuarine MY2.5 | `ISTOPT(0)=0` (Galperin), `ISGOTM=0` |
| Strong stratification (salt wedge) | `ISTOPT(0)=2` (Kantha-Clayson) |
| Highly stratified shelf | `ISTOPT(0)=3` (Kantha 2003) |
| K-ε / K-ω closure | `ISGOTM=1` with GOTM `tke_method=tke_keps` etc. |
| Wave-dominated nearshore | `ISGOTM=0` MY2.5 with `IS2TIM>=1` (CALQQ2T includes vegetation/MHK terms) |
| Turbulence diagnostic output needed | Output `AV`, `AB` to history (`m²/s` after multiplying by depth) |

## Working Rules

- Background mixing `AVO/ABO` (~1e-5 m²/s typical) prevents zero-`AV` regions; never set to zero.
- `AVMX` cap (~0.5 m²/s default) protects against runaway in shallow tidal regions.
- For GOTM coupling, ensure `gotm_input.nml` is consistent with EFDC vertical resolution; mismatched layer counts crash silently.
- `ISTOPT(0)` change between Galperin/Kantha mid-run is non-trivial — close the run, restart cleanly.
- MY2.5 dissipation is implicit-in-diagonal; explicit dissipation forms in older theory papers don't apply to this code.

## Common Pitfalls

- ▢ Confusing `AV` (depth-normalized, m/s) with physical vertical viscosity (m²/s) — output `AV * HP` for physical units.
- ▢ Looking for `AVOMX` symbol — code uses `AVMX`.
- ▢ Setting `ISGOTM=1` but forgetting `gotm_input.nml` — `Init_GOTM` errors at startup.
- ▢ Expecting "AB ln" symbol from old docs — the actual variant is `CALQQ1` (3TL) vs `CALQQ2T` (2TL); the latter has additional vegetation/structure sink terms in the diagonal.
- ▢ Wall proximity `FPROX` formulation — different forms initialize at `aaefdc.f90:1517-1528`; choice depends on whether you want Mellor's parabolic or alternative form. Verify the active branch matches your case (free-surface vs bottom-bounded).

## Next expansion

- Wave-current bottom stress note for sediment coupling (cross-link to `efdc_sediment.md`).
- GOTM closure choice walk-through (k-ε vs k-ω vs GLS).
- Vegetation drag in `q²L` equation detailed derivation.

## References

- Mellor & Yamada 1982 (MY 2.5 baseline).
- Galperin et al. 1988 (stability functions).
- Kantha & Clayson 1994; Kantha 2003.
- Umlauf & Burchard 2003 (GOTM/GLS framework).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
