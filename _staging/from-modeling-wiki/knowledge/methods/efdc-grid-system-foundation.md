---
auto_draft: false
authored_by: claude-opus-4-7
review_required: true
date: 2026-05-02
lane: efdc
category: method
---

# EFDC Grid System Foundation

## Scope note

This note establishes the EFDC+ grid system as a single coherent topic: how the horizontal grid, vertical coordinate, and bathymetry representation interact, and when to choose between the two vertical layering options (SIG vs SGZ).

- **Manual-backed**: orthogonal curvilinear horizontal grid; sigma transformation equation; SIG vs SGZ tradeoff; tool ecosystem
- **Practical synthesis**: SIG vs SGZ decision guide; common pitfalls in shallow-coastal use; orientation cautions
- **Out of scope**: time-varying bathymetry (separate note), grid-resolution sensitivity studies (separate note), single-grid vs multi-block topology (manual silent — flagged in Next Expansion)

## Source Basis

- `EFDC_Theory_Document_Ver_12` Chapter 2 §2.1.1 (Horizontal and Vertical Coordinate Systems), §2.6 (Vertical Layering Options), §2.6.1 (SIG), §2.6.2 (SGZ)
- `EK_241696991` — Sigma-Zed Vertical Layering (EFDC+ Explorer KB)
- `EK_260276304` — references Tetra Tech 2007 Generalized Vertical Coordinate memo, Mellor et al. 1994
- `EFDC_Training_Overview` p.21 (Model Grid)
- `CVLKB_2818252`, `CVLKB_2818253` — CVLGrid feature list
- `EFDC+_Propwash_WhitePaper` §3 Step 4 (sub-grid bottom elevation interpolation)
- `EK_2132770817` — DZC array and EFDC array postprocessing

## Why This Note Exists

EFDC's grid is the single most upstream choice in any model setup. Get it wrong and every later layer (forcing, friction, calibration) is partly chasing grid artifacts. The manual treats horizontal and vertical separately, but in practice the modeler picks them together. This note ties them, makes the tradeoffs explicit, and routes the reader to follow-up notes.

## 1. Horizontal Grid — Orthogonal Curvilinear

EFDC formulates its governing equations on a curvilinear, orthogonal horizontal grid in (x, y) [file=EFDC_Theory_Document_Ver_12 section=Chapter 2 HYDRODYNAMICS > 2.1.1 Horizontal and Vertical Coordinate Systems].

**Why curvilinear, not Cartesian:**
- Real shorelines, channels, and harbor entrances are not aligned with cardinal axes. A Cartesian grid forces step-staircase boundaries that distort momentum balance near the wall.
- Curvilinear cells follow the boundary, so wall-normal velocity is naturally resolved.

**Why orthogonal:**
- Non-orthogonal cells introduce off-diagonal metric terms in the discretized equations, which both increase computational cost and reduce accuracy of advection and pressure-gradient computations.
- The standard guideline used by DSI's CVLGrid is orthogonal deviation < 3° everywhere [file=CVLKB_2818253 section=(prologue)].

**Practical implications:**
- A grid generated for an EFDC model is usually built in CVLGrid (DSI native), but EFDC also accepts grids imported from RGFGrid (Delft3D), Grid95, or SEAGRID [file=EFDC_Training_Overview section=Model Grid > Dynamic Solutions].
- (I, J) indices are fixed once boundary conditions are placed. Re-meshing later without preserving (I, J) breaks BC links. CVLGrid explicitly preserves (I, J) when loading and editing existing EFDC grids [file=CVLKB_2818252 section=(prologue)].

## 2. Vertical Coordinate — SIG (Standard Sigma)

EFDC was originally formulated with a sigma stretched vertical coordinate [file=EFDC_Theory_Document_Ver_12 section=Chapter 2 HYDRODYNAMICS > ∑ > 2.6. Vertical Layering Options].

**Transformation:**

```
z = (z* + h) / (ζ + h) = (z* + h) / H
```

where [file=EFDC_Theory_Document_Ver_12 section=Chapter 2 HYDRODYNAMICS > 2.1.1 Horizontal and Vertical Coordinate Systems]:
- `z` is the sigma coordinate (dimensionless, −1 ≤ z ≤ 0)
- `z*` is the vertical coordinate with respect to the vertical reference datum (m)
- `h` is the water depth below the datum (m)
- `ζ` is the water surface elevation above the datum (m)
- `H = h + ζ` is the total water-column depth (m)

**Behavior:**
- The number of vertical layers is the same at every horizontal cell, irrespective of local depth [file=EFDC_Theory_Document_Ver_12 section=Chapter 2 HYDRODYNAMICS > ∑ > 2.6.1 Standard Sigma (SIG) Approach].
- Layer thickness varies cell-by-cell so the same fractional depth is preserved (e.g. layer 1 is always the top 10% of H, layer 2 the next 10%, etc.).
- This **resolves the water column equally well in shallow and deep regions simultaneously** and is suitable for water bodies with complicated geometry and large bottom-elevation changes [file=EFDC_Theory_Document_Ver_12 section=2.6.1 Standard Sigma (SIG) Approach].
- DZC (vertical layer thickness as decimal fraction of water depth, dimensionless) is the postprocessing array that exposes per-cell layer geometry [file=EK_2132770817 section=Data Extraction of EFDC Arrays].

**Known weakness — horizontal pressure gradient error:**
- The SIG transformation introduces a well-known error in horizontal gradient terms (concentration, velocity, pressure), documented as **Mellor et al. 1994** [file=EFDC_Theory_Document_Ver_12 section=Chapter 2 HYDRODYNAMICS > ∑ > 2.6.2 Sigma-Zed Approach (SGZ)].
- The error becomes significant only in regions with **steeply varying bathymetry**.
- In flat or gently sloped domains, SIG remains an excellent choice.

## 3. Vertical Coordinate — SGZ (Sigma-Zed)

To overcome the SIG horizontal-pressure-gradient error in steep-bathymetry regions, EFDC+ implements two computationally efficient vertical layering approaches collectively referred to as SGZ (Sigma-Zed) [file=EFDC_Theory_Document_Ver_12 section=Chapter 2 HYDRODYNAMICS > ∑ > 2.6.2 Sigma-Zed Approach (SGZ)] (Craig et al. 2014).

**Key differences from SIG:**
- The number of vertical layers is **allowed to vary across the model domain** based on local water depth — deeper cells can have more layers, shallow cells fewer [file=EFDC_Theory_Document_Ver_12 section=2.6.2 Sigma-Zed Approach (SGZ)].
- The z-coordinate system varies for each cell face, with **face matching of layers** between adjacent cells [file=EFDC_Theory_Document_Ver_12 section=2.6.2 Sigma-Zed Approach (SGZ)].
- Selection: in EFDC+ Explorer, the user picks SGZ (vs SIG) under the **Layers** sub-menu of the Model Grid configuration [file=EK_241696991 section=(prologue)].

**When SGZ pays off:**
- Estuary/harbor with **deep navigation channel adjacent to shallow flats** — uniform sigma layering would either over-resolve the flat or under-resolve the channel.
- Reservoirs with steep bathymetric gradients near dam structures.
- Any case where SIG-induced spurious horizontal currents near steep slopes contaminate calibration.

**Where SGZ doesn't help:**
- Largely flat domains where SIG error is already negligible — SGZ adds postprocessing complexity without accuracy gain.
- Very small domains where you just want a fast prototyping baseline.

**Historical naming note:**
- The original Tetra Tech 2007 memorandum titled this option the **Generalized Vertical Coordinate** (GVC) [file=EK_260276304 section=(prologue)]. EFDC variants in legacy literature may appear as `EFDC_GVC` (referenced e.g. in water-quality kinetic module choice [file=EK_245202988 section=(prologue)] — for `EFDC_GVC`, only WQ Module 3 is supported in standard sigma mode when GVC is active). Modern EFDC+ documentation uses **SGZ / Sigma-Zed**. They refer to the same family of layering scheme.

## 4. Bathymetry Representation

EFDC's grid is the discretization onto which bathymetry is mapped. Two interactions matter:

**Sub-grid bathymetry interpolation:**
- For sub-grid features (e.g. propeller-wash sub-grid points), EFDC+ interpolates bottom elevation from surrounding model grid-cell centers using an **inverse-distance-squared scheme** [file=EFDC+_Propwash_WhitePaper section=Chapter 3 EFDC+ Algorithm Implementation > Step 4. Determine Bottom Elevation].
- This means narrow channels, dredged trenches, or dredged thalwegs that exist between cell centers are **smoothed out** unless represented explicitly in the cell-center bathymetry input.

**Layer thickness as fraction of depth:**
- The DZC array (vertical layer thickness as a decimal fraction of water depth) is what postprocessing tools and 2DV plots consume to render the vertical structure [file=EK_2132770817 section=Data Extraction of EFDC Arrays].
- Inspect DZC after a setup change to confirm the actual per-cell layering matches what the configuration intended.

## 5. Tooling Catalog

CVLGrid is the DSI-native 2D curvilinear orthogonal grid generator [file=CVLKB_2818253 section=(prologue)]:
- Solves grid generation as a **Laplace equation** problem using the **Method of Successive Over-Relaxations (SOR)**.
- Optimum SOR relaxation factor is computed automatically.
- Supports orthogonal-deviation reduction tools (Orthogonalize Global / Local / 1D), aiming for the < 3° standard.
- Optimised for `EFDC_DSI / EFDC+`, `EFDC_SGZ`, `EFDC_EPA`, `EFDC_Hydro` model variants [file=CVLKB_2818252 section=(prologue)].

External grid generators that can be imported into EFDC [file=EFDC_Training_Overview section=Model Grid > Dynamic Solutions]:
- **RGFGrid** — Delft3D's curvilinear grid generator
- **Grid95** — legacy academic tool
- **SEAGRID** — MATLAB-based curvilinear grid generator

The tool is not the model. Re-grid in the tool, but version-control the resulting EFDC `.inp` and grid files, not the tool's project file. Treat the imported grid as the source of truth.

## SIG vs SGZ — Decision Guide

| Case | Recommended | Reason |
|---|---|---|
| Flat lake / shallow uniform estuary | SIG | Pressure-gradient error negligible; simpler postprocessing |
| Large bottom-slope variation; steep bathymetry | SGZ | Reduces SIG horizontal-gradient error |
| Deep navigation channel adjacent to wide shallow flat | SGZ | Uniform sigma over-resolves flat / under-resolves channel |
| Stratified deep reservoir near dam | SGZ | Spurious near-bottom currents from SIG contaminate density structure |
| Quick prototyping / mass screening | SIG | Faster to set up; simpler diagnostic plots |
| Already calibrated SIG model with known bias near steep zones | Try SGZ as an experiment | Quantify the SIG error explicitly before refactoring |

## Working Rules

- **Don't pick a vertical scheme by reflex; pick by where your bathymetry is steep.** SIG is fine in a calm estuary; SGZ is the answer when steep slopes drive spurious horizontal gradients.
- **Horizontal grid orientation should align with the dominant flow axis** (tidal channel main axis, dominant wind, ebb-flood track). Cells aligned with flow direction reduce numerical diffusion of momentum across cell faces.
- **Always inspect DZC after any vertical-config change.** Misconfigured layer settings can silently produce nonphysical layer thicknesses without crashing the run.
- **The (I, J) indexing is structural — boundary conditions, observation cells, and inflow groups are tied to (I, J).** Regenerating the grid without preserving (I, J) means redoing all BC mappings.
- **Bathymetry interpolation is inverse-distance-squared.** Sharp narrow features (dredged channels, breakwater toes) that fall between cell centers will be smoothed. If they matter, refine the grid locally or pre-burn the feature into the input bathymetry.

## Common Pitfalls

The first three pitfalls are extracted from the manuals; the rest are general CFD/coastal-modeling judgments. **The "User-experience cases" subsection is intentionally left for the modeling lead to fill in from project memory.**

**Manual-derived:**
1. **Soft-smoothed thalweg.** Sub-grid bathymetry interpolation (inverse-distance-squared) flattens narrow deep channels. Symptom: model under-predicts in-channel current speed even with correct stage [file=EFDC+_Propwash_WhitePaper section=Step 4. Determine Bottom Elevation].
2. **SGZ face-matching mismatch.** With variable layer counts per cell, transitions between cells of different layer count must obey face-matching rules. Configuration mistakes produce silent artifacts at the matched face [file=EFDC_Theory_Document_Ver_12 section=Chapter 2 HYDRODYNAMICS > ∑ > 2.6.2 Sigma-Zed Approach (SGZ)].
3. **WQ kinetic module incompatibility under GVC mode.** When using the legacy `EFDC_GVC` variant in standard sigma mode, only WQ Module 3 (`ISWQLVL=3`) is guaranteed to work; selecting other kinetic modules requires care [file=EK_245202988 section=(prologue)]. (For modern EFDC+ this is less likely an issue but the historical caveat remains for legacy projects.)

**General CFD/coastal-modeling cautions:**
4. **Grid orientation misaligned with dominant flow.** Cells diagonal to flow exaggerate cross-cell numerical diffusion of momentum.
5. **Sigma at sharp bathymetric step.** A small region of steep slope can pollute the entire model with spurious horizontal currents under SIG. The "small region" loophole is what the Mellor 1994 result highlights.
6. **Wrong assumption that orthogonality is a binary check.** Even a grid that passes the < 3° threshold globally may have one or two cells at 6–8° in a sensitive zone. Inspect orthogonal-deviation maps locally.
7. **Re-grid without re-doing the BC audit.** Even when (I, J) is preserved, edge cells may have moved subtly enough that an open-boundary segment now intersects a slightly different bathymetry — re-validate stage at the boundary cell after any grid edit.

**User-experience cases (to be filled by the lead modeler):**
- ▢ Korean estuary case where SIG/SGZ choice mattered concretely (e.g. specific harbor or river-mouth case): which scheme, what triggered the decision, what was the observed difference?
- ▢ Memorable grid-related mistake from past projects: what went wrong, how it was diagnosed, what lesson was promoted from it?
- ▢ CVLGrid (or external tool) experience: any version-specific gotchas, file-format conversions that surprised you, orthogonalization passes that helped or hurt.

## Next Expansion Candidates

- **single-grid vs multi-block topology** — the EFDC manual is largely silent on this. Investigate via the EFDC source tree (`/mnt/e/numerical_models/EFDCPlus_Stable/EFDC/MPI_*` directories suggest some multi-block / domain-decomposition is implemented for MPI). Likely worth a separate `efdc-domain-decomposition-foundation.md` once that is examined.
- **time-varying bathymetry** — referenced in propwash and in some SGZ contexts but never fully specified for general use. Belongs in a `efdc-time-varying-bathymetry.md` once a project case forces the issue.
- **quantitative layer-count guidelines** — depth-to-vertical-resolution ratios and CFL-vs-layer-thickness tradeoffs are not in the chunks consulted; would need a sensitivity-test study to compile.
- **Korean estuary case cross-references** — once 2–3 site-specific cases are written, link from this note into the experiment cards.

## References (manual-backed)

- Hamrick (1992); Ji (2008) — primary theoretical sources for EFDC+ hydrodynamics [file=EFDC_Theory_Document_Ver_12 section=Chapter 2 HYDRODYNAMICS > 2.0.1 Overview].
- Mellor, G. L., Ezer, T., Oey, L.-Y. (1994) — sigma-coordinate horizontal pressure-gradient error [file=EFDC_Theory_Document_Ver_12 section=Chapter 2 HYDRODYNAMICS > ∑ > 2.6.2 Sigma-Zed Approach (SGZ)].
- Craig et al. (2014) — SGZ implementation [file=EFDC_Theory_Document_Ver_12 section=Chapter 2 HYDRODYNAMICS > ∑ > 2.6.2 Sigma-Zed Approach (SGZ)].
- Tetra Tech (2007) — Theoretical and Computational Aspects of the Generalized Vertical Coordinate Option in the EFDC Model [file=EK_260276304 section=(prologue)].

## Provenance

- **Date**: 2026-05-02
- **Authored by**: Claude Opus 4.7 (1M context) — direct authoring (not the auto-draft pipeline that previously failed)
- **Manual chunks consulted**: 18 (`manuals` collection, multi-query retrieval with bilingual fusion)
- **Sections needing user input before promotion to wiki**: "Common Pitfalls > User-experience cases"
- **Once filled, run**: `~/rag/.venv/bin/python ~/rag/scripts/ingest_wiki.py` (after moving file to `/mnt/e/AI_ENV/modeling-wiki/knowledge/methods/`)
