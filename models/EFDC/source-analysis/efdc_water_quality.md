---
title: "efdc water quality"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_water_quality.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

The EFDC+ Eutrophication module: directory structure (`Eutrophication/mod_wq.f90` + diagenesis + biota + zooplankton + RPEM + shellfish), state variables in WQSKE1 (organic carbon `ROC/LOC/DOC`, organic phosphorus `ROP/LOP/DOP`, phosphate `P4D`, organic nitrogen, ammonium/nitrate, silica, DO, COD, TAM, FCB, CO2, algae groups `ALG1..ALGn` or legacy `CHC/CHD/CHG`), kinetic processes (CE-QUAL-ICM-derived), sediment diagenesis (`mod_diagen.f90` with layer-1/2 NH4/H2S/PO4/silica fluxes), Beer-Lambert light limitation with `PARADJ=0.43`, coupling to hydrodynamics via `CALCONC/CALTRAN`, the JSON/JNP-based input format (`wq_3dwc.jnp`, `wq_3dsd.jnp`, `wq_biota.jnp`), and NetCDF/EE binary output. Use this when configuring nutrient/algae simulation, debugging WQ state-variable allocation, or interpreting Eutrophication output.

## Source basis

- `Eutrophication/mod_wq.f90:9-5083` — WATERQUALITY core.
- `Eutrophication/mod_wq_vars.f90:28-118` — state variable indices.
- `Eutrophication/mod_diagen.f90:9-1031` — sediment diagenesis.
- `Eutrophication/mod_biota.f90:57-444` — biota.
- `Eutrophication/mod_zoopl.f90`, `mod_shellfish.f90`, `mod_rpem.f90` — additional modules.
- `aaefdc.f90:126, 3086` — `WQ3DINP` init.
- `hdmt.f90:1021, hdmt2t.f90:734` — `WQ3D` runtime.
- `mod_scaninp.f90:1631-1697, 1875-1890` — input scanning.
- `Transport/calconc.f90:188, 213, 467-490`, `caltran.f90:13` — transport coupling.
- `mod_netcdf.f90:291-1762` — NetCDF output.
- `SedTran-Original/ssedtox.f90:9-31` — sediment-toxic coupling.

## A. Directory and entry points

Eutrophication code in `Eutrophication/`:
- `mod_wq.f90` — core WATERQUALITY driver.
- `mod_wq_vars.f90` — state globals.
- `mod_diagen.f90` — sediment diagenesis (CE-QUAL-ICM-style).
- `mod_biota.f90` — biota / algae parameters.
- `mod_zoopl.f90` — zooplankton.
- `mod_shellfish.f90` — shellfish kinetics.
- `mod_rpem.f90` — RPEM (rooted plant ecosystem model).
- `wwqnc.f90` — WQ NetCDF helper.

Core module: `WATERQUALITY` uses WQ vars + diagenesis + RPEM + shellfish + zooplankton + biota (`mod_wq.f90:9, 34`).

Init: `WQ3DINP` from startup when WQ active (`aaefdc.f90:126, 3086`).

Runtime: `WQ3D` called from both hydro drivers when `ISTRAN(8) >= 1` (`hdmt.f90:35, 1021`; `hdmt2t.f90:37, 734`).

`WQ3D` dispatches kinetic scheme via `WQSKE0/1/2/3/4`, then optional zooplankton, sediment diagenesis, RPEM (`mod_wq.f90:333-358`).

## B. State variables

Defined in `mod_wq_vars` (`:28`):
- Organic carbon: `ROC, LOC, DOC` (refractory, labile, dissolved).
- Organic phosphorus: `ROP, LOP, DOP`.
- Phosphate: `P4D`.
- Organic nitrogen: `RON, LON, DON`.
- Ammonium `NHX`, nitrate/nitrite `NOX`.
- Silica: `SUU, SAA`.
- COD, DO, TAM, FCB, CO2.
- Algae slots (variable count `NAL`).

Legacy mapping (`mod_scaninp.f90:1631`): three named algae `CHC/CHD/CHG` before nutrients.

WQSKE1 mapping (`:1655, 1697`): nutrients first, append `ALG1..ALGn` after 19 base WQ variables.

`NAL` controls algae count. Algae named legacy or `ALG1, ALG2, ...` (`mod_wq.f90:741`).

Zooplankton appended as `ZOO1...` (`:760`).

Transport activation: algae at `19 + NAL`; fixed biota explicitly NOT transported (`mod_scaninp.f90:1875, 1890`).

**No separate BOD state** — oxygen demand is `COD + DO sinks/sources` (`mod_wq.f90:2968, 4568, 4624`).

## C. Kinetic processes (WQSKE1 — primary)

`WQSKE1` is CE-QUAL-ICM-derived, adapted to unlimited phytoplankton groups (`mod_wq.f90:2875, 2884`).

Nutrient limitation: ammonium, nitrate, phosphate, CO2, silica factors for algae and biota (`:3308-3338`).

Algae kinetics:
- Production/growth `WQPA` (`:3458`).
- Basal metabolism `WQBM` (`:3467`).
- Predation `WQPR` (`:3748`).
- Salinity toxicity, bloom logic, settling, optional zooplankton coupling (`:3763`).

Organic matter / nutrients (`:3804-4385`):
- Hydrolysis, mineralization.
- Nitrification, denitrification.
- Uptake, benthic fluxes.
- Settling/sorption.

DO budget (`:3621, 4634, 4673`):
- Saturation/reaeration.
- Photosynthesis, respiration.
- DOC oxidation, nitrification, COD demand.

## D. Sediment diagenesis

`WQ_DIAGENESIS` module (`mod_diagen.f90:9`).

Initialized when `IWQBEN == 1`; reads `wq_3dsd.jnp` (`mod_wq.f90:585`, `mod_diagen.f90:160`).

Runtime coupling: `SMMBE` called from `WQ3D` (`mod_wq.f90:351`, `mod_diagen.f90:674`).

Inputs (`mod_diagen.f90:164-277`):
- Sediment zones, restart controls.
- Diffusion, stoichiometry.
- Layer-1/2 NH4/H2S/PO4/silica parameters.
- Decay rates, burial, particle mixing.
- Nitrification, SOD multipliers.

Computes (`:767-1031`):
- Depositional POM fluxes.
- Sediment POC/PON/POP mass balances.
- Diagenesis fluxes.
- SOD, NH4, NO3, COD, PO4, silica benthic fluxes.

## E. Light limitation

PAR via `PARADJ = 0.43` (photosynthetically active fraction) (`mod_wq_vars.f90:118`, `mod_wq.f90:208`).

Solar input → WQ light intensity using `PARADJ` (`mod_wq.f90:268, 284`).

Light penetration: Beer-Lambert exponential `EXP(-WQKESS * depth)` for top + bottom layer light (`:3348, 3364`).

Layer light limitation feeds phytoplankton + macroalgae growth factors (`:3377, 3381`).

## F. Coupling to hydrodynamics

WQ constituents transported through general concentration path:
- `CALCONC` calls `CALTRAN` for all water-column constituents (`Transport/calconc.f90:188`).
- `CALTRAN` is the advective transport routine (`Transport/caltran.f90:13`).
- Anti-diffusion: `CALTRAN_AD` (`Transport/calconc.f90:213`).

Settling/bed exchange (sediments/toxics) coupled via `SSEDTOX` from `CALCONC` (`:490, 506`).

`SSEDTOX` documents settling + water-column/bed exchange of sediment + sorbed toxics (`SedTran-Original/ssedtox.f90:9, 31`).

WQ passes depositional fluxes to sediment diagenesis for algae/POM/sorbed P/silica (`mod_wq.f90:4934`).

## G. Input format (JSON/JNP)

Active main WQ control: `wq_3dwc.jnp` (`mod_wq.f90:779`).

Reads (`:784-1219`):
- Title, kinetic option, var count.
- WQ zones, temperature lookup, WQ timestep.
- Sediment zones, active constituents.
- Algae count, options for silica, cyanobacteria toxicity, shellfish, zooplankton, RPEM.
- Light extinction, reaeration.
- Hydrolysis/mineralization.
- Nitrification/denitrification.
- Settling/COD/FCB/TAM.
- Benthic flux options.
- Boundaries, point sources.
- Initial conditions, deposition.
- NetCDF output flags.

Related files:
- `wq_biota.jnp` — algae/biota parameters (`mod_biota.f90:57`).
- `wq_bio_zones.jnp` (optional) (`:444`).
- `wq_kin_zones.jnp` (`mod_wq.f90:1266`).
- `wq_3dsd.jnp` — sediment diagenesis (`mod_diagen.f90:160`).
- `wqwcmap.inp`, `wqbenmap.inp` (`mod_wq.f90:1707, 1756`).
- `WQBENFLX.INP` — prescribed benthic fluxes (`:2386, 2431`).

## H. Output

Text output (`mod_wq.f90:396-472`):
- `WQ3D.OUT, WQWCTS.OUT, DIURNDO.OUT, LIGHT.OUT`.

WQ time-series station count marked "not used by EEMS"; older station path appears vestigial (`mod_wq_vars.f90:77`).

Light + diurnal DO diagnostics actively written (`:5010, 5083`).

Global/map output mainly NetCDF and EE binary:
- NetCDF flags read from WQ control (`mod_wq.f90:1219`).
- Disabled if WQ inactive (`mod_netcdf.f90:291`).
- Defined for WQ/algae/sediment diagenesis (`:945`).
- Written for WQ constituents, algae, zooplankton, sediment diagenesis flux/state (`:1747-1762`).

## Decision Guide

| Application | Setup |
|---|---|
| Standard CE-QUAL-ICM-style WQ | `WQSKE1`, `NAL=2-3`, `IWQBEN=1` (sediment diagenesis on) |
| Eutrophication study (algae blooms) | Multiple algae groups via `wq_biota.jnp` |
| Anoxia study | DO + COD + sediment diagenesis (SOD, sulfide) |
| Cyanobacteria toxin | Activate cyanobacteria toxicity option in `wq_3dwc.jnp` |
| Tidal mixing dominance | Couple with hydrodynamic turbulence; `WQSKE1` handles |
| Fresh water reservoir | Disable salinity toxicity |
| Estuarine | Standard `WQSKE1` with full nutrients |
| Korean Yeongsan/Han River | `WQSKE1`, sediment diagenesis, multiple algae for Microcystis |

## Working Rules

- WQ timestep can be different from hydro timestep; set in `wq_3dwc.jnp`.
- Sediment diagenesis (`IWQBEN=1`) is essential for SOD-driven anoxia; without it, DO budget incomplete.
- `PARADJ=0.43` is the standard PAR fraction; rarely changed.
- `WQKESS` (light extinction) typically 0.5-2.0 m⁻¹; calibrate from Secchi depth observations.
- Algae growth limitation: typically nutrient + light + temperature multiplicative.
- For Korean coastal cases, multiple algae groups (diatoms, dinoflagellates, cyanobacteria) recommended.

## Common Pitfalls

- ▢ Setting `ISTRAN(8)=1` without configuring `wq_3dwc.jnp` — runtime crash.
- ▢ Mixing legacy `CHC/CHD/CHG` mapping with `WQSKE1` modern `ALG1..ALGn` — index confusion.
- ▢ No sediment diagenesis (`IWQBEN=0`) for stratified eutrophic system — bottom DO unrealistically OK.
- ▢ Cold-start with WQ but no IC file — all zeros; weeks-long spin-up required.
- ▢ Missing `wq_biota.jnp` with `WQSKE1` — algae parameters undefined.
- ▢ Looking for BOD state — use COD instead.
- ▢ Light extinction `WQKESS` constant in space — for optically variable water, use spatial map.

## Next expansion

- Diagenesis stoichiometry calibration recipe.
- Multi-algae setup for Korean coastal HABs.
- Coupling RPEM (rooted aquatic vegetation).

## References

- Cerco & Cole 1995 (CE-QUAL-ICM).
- Di Toro 2001 (sediment diagenesis).
- Park et al. 1995 (CE-QUAL-ICM original).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
