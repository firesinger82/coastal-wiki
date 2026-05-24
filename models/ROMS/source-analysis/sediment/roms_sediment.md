---
title: "roms sediment"
topic: sediment-transport
canonical_source: self
citation_status: verified
verification_method: "ROMS source code 직접 분석 (models/ROMS/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/roms_sediment.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

ROMS Community Sediment Transport Modeling System (CSTMS): bed-layer ordering with active layer at index 1, cohesive bed (`COHESIVE_BED`) with critical-stress profile `ibtcr`, bedload formulations (Meyer-Peter-Müller, Soulsby-Damgaard, Van der A et al. 2013), floc dynamics with size-distribution evolution, BBL coupling (SSW/MB/SG), how suspended sediment is treated as ordinary tracer in `step3d_t`, Partheniades excess-shear erosion in `sed_fluxes.F`, and multi-fraction (NCS+NNS) mass conservation. Use this when configuring sediment transport for shelf/coastal cases, choosing among CSTMS variants, or debugging bed mass balance.

## Source basis

- `sediment.F:30-160` — bed ordering, dispatch.
- `sed_bed.F:66-462` — active layer.
- `sed_bed_cohesive.F:75-658` — cohesive bed.
- `sed_bedload.F:22-1273` — MPM, Soulsby-Damgaard.
- `sed_bedload_vandera.F:16-575` — Van der A 2013.
- `sed_flocs.F:4-727` — floc dynamics.
- `sed_fluxes.F:66-306` — bed/water exchange (Partheniades).
- `mod_bbl.F:18-53`, `bbl.F:16`, `ssw_bbl.h:100-922`, `mb_bbl.h:10-626`, `sg_bbl.h:591-605` — BBL.
- `step3d_t.F:21-1543` — tracer coupling.
- `sediment_mod.h:50-546` — module definitions.

## A. Active layer

`sediment.F:30-57` documents bed ordering:
- Seawater layers run `1..N`.
- Sediment bed layers run downward from top `1` to bottom `Nbed`.

In `sed_bed.F`, **only layer 1** is directly exchanged with suspended load:
- `bed_mass(i,j,1,nnew,ised)` updated by `−(ero_flux − settling_flux)`, clipped non-negative (`:287-293`).
- Deeper layers copied from `nstp`.

Deposition can create new top layer (`:299-337`):
- Bottom two layers merged.
- Existing layers pushed down.
- `bed_mass(...,1) ← dep_mass`.

Active layer thickness (`:371-380`):
- Excess-stress thickness + `6·d50`.
- Uses BBL combined stress if available.

If layer 1 thinner than `bottom(:,:,iactv)`, mass pulled upward from deeper layers (`:393-462`).

## B. Cohesive bed (sed_bed_cohesive.F)

Selected for `COHESIVE_BED` or `MIXED_BED` (`sediment.F:80, 160`).

Adds `ibtcr` = bed critical erosion stress in Pa (`sediment_mod.h:50`).

Active-layer thickness uses `rho0*tau_w − bed(:,:,1,ibtcr)` instead of mean `bottom(:,:,itauc)` (`:327-331`).

Then searches downward through critical-stress profile (top of each layer) (`:353-399`).

**Cohesive dynamics**:
- Net deposition: surface `ibtcr` lowered/relaxed toward deposited-bed value, bounded by `tcr_min` and current stress (`:465-485`).
- Net erosion: increases toward next layer's `ibtcr` proportional to mass removed (`:650-658`).

This captures consolidation: freshly deposited mud has low `ibtcr`; older buried layers more resistant.

## C. Bedload

`sed_bedload.F` implements **MPM** + **Soulsby-Damgaard** (`:22-33`).

Transports only noncohesive classes: `DO ised = NCS+1, NST` (`:436`).

**MPM** (Meyer-Peter-Müller, unidirectional):
- `q_b = 8 · (θ − θ_c)^1.5`, `tau_mpmc = 0.047` (`:291, 528-539`).

**Soulsby-Damgaard** (combined waves+currents):
- Computes current-wave angle, mean + wave Shields stresses (`:405-450`).
- Wave asymmetry `w_asym`, two half-cycle maxima (`:471-498`).
- Along/perpendicular bedload components (`:512`).

`sed_bedload_vandera.F` implements **Van der A et al. 2013** (`:16`):
- Targets wave asymmetry, separate crest/trough transport.
- Ruessink/Abreu skewness parameters (`:436`).
- Crest/trough durations + velocities (`:451`).
- Half-cycle stress factors (`:499`).
- Separate `sandload_vandera` calls for crest/trough, then combined over wave period (`:513-575`).

## D. Floc dynamics (sed_flocs.F)

Applies only with `SUSPLOAD` and `SED_FLOCS` (`:4`).

Operates on **cohesive classes only** `1:NCS`:
1. Convert tracer mass to concentration with `Hz_inv` (`:203-208`).
2. Convert to number concentration `NNin = cv_tmp / f_mass` (`:227-231`).
3. Compute turbulent shear `Gval` from turbulence closure or BBL-enhanced bottom dissipation (`:245-263`).
4. Evolve floc size distribution with adaptive substeps (`:286-311`).
5. Redistribute negative mass (`:315`).
6. Write back to tracer mass `t(...,nnew,idsed)` (`:354-378`).

Size-distribution equation (`:681-726`) includes:
- Aggregation gain/loss.
- Differential settling terms.
- Breakup.
- Optional collision-fragmentation.

## E. BBL coupling (SSW / MB / SG)

BBL state at rho-points (`mod_bbl.F:18-53`):
- Current stress, wave stress, max combined wave-current stress.

`bbl.F:16` selects:
- `ssw_bbl.h` (Sherwood-Signell-Warner — most rich for sediment).
- `mb_bbl.h` (Madsen-Bagnold).
- `sg_bbl.h` (Styles-Glenn).

Sediment modules consume BBL stress when `BBL_MODEL` enabled:
- `sed_fluxes.F:66, 227`, `sed_bed.F:66, 224`, `sed_bed_cohesive.F:75, 241`, `sed_bedload.F:101, 354` — pass `bustrcwmax/bvstrcwmax`, compute `tau_w`.

**SSW** is the richest: takes `bedldu/bedldv`, writes detailed roughness/WBL fields (`ssw_bbl.h:100-922`).

**MB/SG** also write current, wave, combined stresses, bottom roughness/ripple (`:585-605`).

## F. Suspended sediment in step3d_t

**No literal `CALTRAN` token** in `step3d_t.F` — sediment concentration is treated as ordinary tracer in `NT(ng)` loops.

`step3d_t.F:21-25` notes: `t(:,:,:,nnew,:)` already includes source/sink terms from "biology, sediment".

Generic tracer loops advect all `itrc=1, NT(ng)` horizontally and vertically (`:405, 925`).

Sediment exchange writes directly into tracer mass `t(i,j,1,nnew,idsed(ised))` during erosion (`sed_fluxes.F:261, 306`).

Morphology changes fed back in `step3d_t` by adjusting tracer mass for bed-thickness change, MPDATA and non-MPDATA paths (`step3d_t.F:1221-1543`).

## G. Bed exchange (Partheniades)

Actual exchange routine: `sed_fluxes.F`, called after settling and before bed stratigraphy (`sediment.F:146-160`).

Erosion is **Partheniades-style excess shear** (`:278-301`):
```
ero = dt · Erate · (1−porosity) · bed_frac · (tau/tau_ce − 1)
```
Clipped to available active-layer mass + settling flux.

For cohesive: `tau_ce` replaced by `bed(:,:,1,ibtcr)/rho0` (`:267`).
For mixed: blends cohesive `ibtcr` with class `tau_ce` via `bottom(:,:,idprp)` (`:270`).

Deposition fully or linearly suppressed above `tau_cd` under `SED_TAU_CD_CONST/LIN` (`:287-294`).

**No explicit Van Rijn** in these files — sand bedload uses MPM/Soulsby-Damgaard/Van der A; suspended sand erosion follows same `Erate/tau_ce` excess-shear form.

## H. Multi-fraction + conservation

Sediment tracers split into:
- `NCS` cohesive.
- `NNS` noncohesive.

Packed into `idsed(1:NST)` with mud first, sand after (`sediment_mod.h:123, 497, 541, 546`).

Mass conservation:
- Class-wise bed mass arrays (`sed_bed.F:347`).
- Fractions recomputed from total layer mass (`:350`).
- Thickness recomputed from mass, density, porosity (`:357-358`).

Bedload: flux-divergence based, limited by available top-layer mass (`sed_bedload.F:637, 1233`).

Cohesive classes that didn't participate in bedload: copied forward (`:640, 1236`).

Surface mixed properties recomputed geometrically from all `NST` bed fractions (`:1253-1273`).

## Decision Guide

| Application | Setup |
|---|---|
| Estuarine cohesive mud | `COHESIVE_BED`, `SED_FLOCS`, `SUSPLOAD`, single class |
| Sandy beach with wave asymmetry | `SED_VAN_DER_A`, `BBL_MODEL=SSW`, multi-fraction sand |
| River bedload | `SUSPLOAD`, MPM via default, no `SED_VAN_DER_A` |
| Shelf with combined waves+currents | `SED_BEDLOAD`, Soulsby-Damgaard, `BBL_MODEL=SSW` |
| Mixed mud+sand | `MIXED_BED`, `COHESIVE_BED`, `SED_FLOCS`, multi-fraction |
| Clear water (test) | `SUSPLOAD` off; just track tracer without bed |
| Hard-bottom bias | Set `Erate` very low or use morphology mask |

## Working Rules

- Active layer index 1 is the only erodible layer; deeper layers pull up only when active layer thinned.
- Cohesive `ibtcr` profile evolves with deposition/erosion — captures consolidation.
- For Korean tidal flats: `COHESIVE_BED + SED_FLOCS` essential; mud dominates.
- BBL choice: `SSW` is the modern default; `MB/SG` for legacy comparison.
- `tau_ce` per class typically 0.05-0.2 Pa for sand; for cohesive, `ibtcr` evolves dynamically.
- Output `bed_thick`, `bed_frac`, `mud_*`, `sand_*` for diagnostics.
- Multi-fraction conservation requires matched `NCS, NNS` between cold and hot start.

## Common Pitfalls

- ▢ Setting `tau_ce` very high — no erosion ever; sediment frozen.
- ▢ `SED_FLOCS` with no cohesive classes — module called but does nothing.
- ▢ Missing `BBL_MODEL` with sediment — bottom shear underestimated; transport too low.
- ▢ Comparing `bed_mass` across runs with different `Hz` — needs accounting for column volume.
- ▢ Hot-start with different `NCS+NNS` — mismatched tracer indices.
- ▢ Expecting Van Rijn in these files — not implemented; use MPM, Soulsby, or Van der A.
- ▢ Bedload at outflow boundary — explicitly zeroed; net export looks zero but suspended is OK.

## Next expansion

- SSW BBL detailed wave-current stress derivation.
- Multi-fraction sediment input (`sed_class_*`) recipe.
- Morphology coupling (`MORPHOLOGY` flag).

## References

- Warner et al. 2008 (CSTMS).
- Sherwood et al. 2018 (CSTMS update).
- Meyer-Peter & Müller 1948.
- Soulsby & Damgaard 2005.
- Van der A et al. 2013.
- Verney et al. 2011 (floc dynamics).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
