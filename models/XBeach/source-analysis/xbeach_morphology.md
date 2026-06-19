---
title: "xbeach morphology"
topic: general
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach_morphology.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How XBeach computes sediment transport (`transus`) and updates the bed (`bed_update`), where `morfac` actually multiplies, what each transport formula (Soulsby-Van Rijn, Van Thiel-Van Rijn, Van Rijn 1993) computes, how multi-fraction sediment is handled, where suspended/bed-load split happens, how bed-slope corrections (Roelvink, Soulsby, Talmon) modify transport, and how mass conservation is enforced. Use this when calibrating sediment for a beach case, debugging morfac scaling, or interpreting `dzg` outputs.

## Source basis

- `morphevolution.F90:157-3125` — `transus`, `bed_update`, `sedtransform`, avalanching, `update_fractions`.
- `libxbeach.F90:307-310` — top-level execution order.
- `params.F90:932-1180, 1674-1953` — formula selection, `morfac`, slope-effect parameters, multi-fraction.
- `paramsconst.F90:80-120` — formula and slope-effect constants.
- `variables.def:148-205, 277-280` — multi-fraction state arrays.
- `initialize.F90:1256-1416` — sediment array allocation, `D50/D90` setup, `gdist*.inp` reading.

## A. `morfac` acceleration

`transus` computes transport before bed update (`libxbeach.F90:307`), then `bed_update` changes the bed (`:310`).

`morfac` does **not** generally multiply suspended/bed transport in `transus`. Main morph acceleration is in `bed_update`:

| Application | File:Line |
|---|---|
| 2D flux-gradient: `dzg = par%morfac*par%dt/(1−par%por)*(...)` | `morphevolution.F90:738, 745` |
| 1D form, same multiplier | `:780, 785` |
| Hard-layer expected erosion estimate before limiting | `:196` |
| Hard-layer outgoing-flux limiter | `:705` |
| Avalanching loops `nint(par%morfac)` times | `:863` |

With `morfacopt=1`, input/output times scale to hydrodynamic time (`params.F90:1942-1953`).

## B. Transport formulation

Selected in `transus` (`morphevolution.F90:173-176`):
- `FORM_SOULSBY_VANRIJN`
- `FORM_VANTHIEL_VANRIJN`
- `FORM_VANRIJN1993`

→ all call `sedtransform`. Names mapped from `form` (`params.F90:932-943`); constants in `paramsconst.F90:80-91`.

`sedtransform` workflow (`morphevolution.F90:1416-1848`):
- Per-fraction: fall velocity, dimensionless grain size, critical Shields (`:1416-1428`).
- Response time: `Ts = par%tsfac * hloc / w(:,:,jg)`, limited into `s%Tsg` (`:1508-1513`).
- Critical velocity for Soulsby-Van Rijn: D50, D90, hloc (`:1517-1522`).
- Van Thiel/Van Rijn critical current/wave velocity blend (`:1523-1537`).

**Soulsby-Van Rijn**:
- `Cd` from `z0` and depth (`:1602-1607`).
- Bed coefficient `Asb`, suspended `Ass` (`:1608-1610`).
- Stirring combines current `vmg`, short-wave orbital `urms²`, `par%sws`, `Cd` (`:1612-1621`).
- Equilibrium `ceqb` and `ceqs` split (`:1623-1633`).

**Van Rijn 1993**:
- `used = vmg + s%ua` (transport velocity) (`:1664-1669`).
- Bed-load mobility (`:1670-1683`).
- Suspended: ripple roughness `deltar`, `rwave`, `uorb`, wave/current shear, reference concentration, vertical integration (`:1686-1837`).
- Final calibrated `s%ceqbg, s%ceqsg` (`:1845-1848`).

Parameters in `params.F90:1067-1180`.

## C. Bed update step

`bed_update` starts at `morphevolution.F90:594`. Runs only inside morphology window AND when `morfac > 0.999` (`:640`).

| `sourcesink` | Bed change source | Lines |
|---|---|---|
| `0` | Divergence of suspended + bed-load fluxes | `:737-743` |
| `1` | Erosion/deposition source terms + bed-load divergence | `:744-748` |

Single fraction: `zb`, `dzbnow`, `dzbdt`, `sedero`, `structdepth` updated directly (`:751-758`).

Multi-fraction: convert `dzg` to mass erosion/deposition `edg` and call `update_fractions` (`:759-769`).

Water levels adjusted after bed change (`:817-843`).

## D. Multi-fraction sediment

State arrays dimensioned by `par%ngd`: `ccg, Susg, Svsg, Subg, Svbg, ceqbg, ceqsg, pbbed` (`variables.def:148-205`).

Initialization (`initialize.F90:1256-1416`):
- Allocated with `par%ngd` (`:1256-1286`).
- `D50, D90, sedcal, ucrcal` copied per fraction (`:1325-1329`).
- `ngd==1`: `pbbed(:,:,:,1)=1` (`:1332-1337`).
- `ngd>1`: read `gdist*.inp` files, normalize so layer fractions sum to 1 (`:1343-1381`).

Runtime:
- `transus` loops `jg=1, par%ngd` (`morphevolution.F90:213, 577-584`).
- `bed_update` computes `dzg` as vector over fractions (`:738-748`).
- `update_fractions` updates layer thicknesses + fraction ratios using sediment mass `Sm`, matrix exchange, top-layer erosion/deposition (`:1187-1328`).

## E. Suspended vs bed-load split

Transport arrays (`variables.def:165-168`):
- Suspended: `Susg, Svsg`.
- Bed-load: `Subg, Svbg`.

Formulae:
- X suspended: `Sus = par%sus * (cu*ureps*hu − Dc*hu*dcsdx) * wetu` (`morphevolution.F90:276-277`).
- X bed: `Sub = par%bed * (cub*urepb*hu) * wetu` (`:278-279`).
- Y analogous (`:351-354`).

Equilibrium concentrations split into `ceqbg, ceqsg`; `bulk` mode moves bed-load equilibrium into suspended (`:1845-1848`).

## F. Bed-slope corrections

Three orthogonal options (`params.F90:1073-1092`, constants `paramsconst.F90:109-120`):

| Parameter | Options | Effect |
|---|---|---|
| `bdslpeffmag` | none, Roelvink-total, Roelvink-bed, Soulsby-total, Soulsby-bed | Modifies actual transports after Sus/Sub computed |
| `bdslpeffini` | none, total, bed | Modifies critical/initiation velocity (`Ucrb, Ucrs`) |
| `bdslpeffdir` | none, Talmon | Rotates bed-load direction |

Implementation:
- `bdslpeffmag` modifies `Sus/Sub/Svs/Svb` (`morphevolution.F90:392-431`).
  - Roelvink: subtracts slope-proportional transport using `par%facsl` (`:393-406`).
  - Soulsby: rescales magnitude by `(1 − par%facsl*dzbds)` (`:407-430`).
- Talmon direction correction rotates bed-load using local velocity, shear, Shields, slopes (`:433-460`).
- `bdslpeffini` modifies initiation through `srfTotal, Ucrb, Ucrs` (`:1550-1599`).

## G. Wave-current-sediment coupling

Execution order: wave → vegetation → groundwater → flow → `transus` (`libxbeach.F90:301-307`).

Inside `transus`:
- Wave turbulence via `waveturb` when `lwt` or wave/bore-averaged turbulence active (`morphevolution.F90:157-160`).
- If short waves active, waveform model computes skewness/asymmetry velocity `ua` (`:162-168`).
- `ua` added to sediment advection velocities for both suspended and bed-load (`:222-243, 284-313`).

Skewness / asymmetry:
- **Ruessink-Van Rijn**: computes `Sk, As`, then `ua = par%sws * (par%facSk*Sk − par%facAs*As) * urms` (`:3032-3039`).
- **Van Thiel** (table interpolation): same `ua` form (`:3119-3125`).

`facua, facSk, facAs` defaults + backward-compat reading at `params.F90:959-967`; zeroed for non-short-wave modes at `:986-994`.

## H. Mass conservation / cell volume

Conservative flux-gradient form:
```
dzg = morfac * dt / (1 − por) * flux_divergence * dsdnzi
```
where fluxes are face transport rates × face widths (`dnu, dsv`), times `dsdnzi` (inverse cell area) (`morphevolution.F90:737-748`).

Suspended concentration update treats water-column volume, not just concentration (`:500-508`).

Avalanching uses `dAfac` for unequal cell areas (`:927-940, 1034-1047`); deposition `dzleft*dAfac`, erosion `dzleft` (`:948-955, 1054-1061`).

**Caveats** (in code comments):
- `sourcesink==1` with `morfac>1` warns of possible mass loss (`params.F90:1674-1679`).
- Bed Neumann boundaries introduce mass error = bed-level change × cell area (`morphevolution.F90:1144-1147`).

## Decision Guide

| Application | Setting |
|---|---|
| Beach-and-dune storm impact | `form=soulsby_vanrijn` or `vanthiel_vanrijn`, `bdslpeffmag=roelvink_total`, `bdslpeffini=total`, `bdslpeffdir=talmon` |
| Long-term morphology | `morfac=10–100`, `morfacopt=1`, `sourcesink=0` |
| Multi-fraction (sand + gravel) | `ngd=2`, `gdist*.inp` per cell, `D50/D90` per fraction |
| Single-fraction quick test | `ngd=1`, set `D50, D90` scalar |
| High-resolution surf zone | `form=vanthiel_vanrijn` (better wave-current interaction) |
| Asymmetric/skewed transport | `facua` (overall scaling), `facSk` (skewness), `facAs` (asymmetry); positive = onshore-bias |
| Steep slope (avalanching) | `wetslp=0.15, dryslp=1.0` (defaults), `morfac` controls passes |
| Morphologically calm period | Increase `morfac`; watch bed Neumann mass error |

## Working Rules

- `morfac` doesn't multiply transport — it multiplies bed change. Storm hindcasts: `morfac=1`. Long-term: `morfac=10–100` (verify mass conservation).
- `sourcesink=0` (default) is mass-conserving; `sourcesink=1` is faster but warns of mass loss when `morfac>1`.
- Soulsby-Van Rijn is the default workhorse. Van Thiel-Van Rijn is preferred for surf zone (wave-current interaction in critical velocity).
- `D50` per cell: defines critical shear AND settling velocity. Calibrate together.
- `facua=0.1–0.3` typical for storm hindcasts; positive = onshore-biased transport (sandbar formation in surf zone).
- Multi-fraction: `gdist*.inp` files must sum to 1 per cell. Normalize before running.
- Bed-slope effects: `bdslpeffini=total` is most common; `bdslpeffdir=talmon` is recommended for 2D cases with strong angled flow.

## Common Pitfalls

- ▢ Setting `morfac=10` for a storm hindcast — over-accelerates, gives unrealistic dune retreat.
- ▢ Multi-fraction without `gdist*.inp` correctly normalized — silent fraction error.
- ▢ Forgetting `morfacopt=1` — input forcing time series get out of sync with morphological time.
- ▢ Confusing `facsl` (slope effect coefficient) with `facua` (skewness/asymmetry scaling) — different physics.
- ▢ `sourcesink=1, morfac>1` accepted without checking warning — mass error grows over time.
- ▢ Avalanching `wetslp=1.0` (= dry value) — wet avalanching never triggers; symptom is artificial dune face stability.
- ▢ Hard-layer (`struct=1`) with `ne_layer` thickness too thin — runs out, then erodes through; check `structdepth` field in output.

## Next expansion

- Calibration recipe (`facua, facSk, facAs, D50, sus`, `bed`).
- Multi-fraction `gdist*.inp` generation tooling.
- Long-term morfac validation methodology.

## References

- Soulsby & Van Rijn (Soulsby 1997).
- Van Rijn 1993 (Sediment Transport, Parts I-III).
- Van Thiel de Vries 2009 (XBeach surf-zone transport).
- Talmon et al. 1995 (bed-slope direction correction).
- Ruessink et al. 2012 (wave skewness).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.
