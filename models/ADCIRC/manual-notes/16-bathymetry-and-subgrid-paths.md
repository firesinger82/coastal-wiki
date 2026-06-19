---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/16-bathymetry-and-subgrid-paths.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
---
# Bathymetry And Subgrid Paths

## Metadata

- date: 2026-04-12
- title: bathymetry in fort.14, time-varying bathymetry, and subgrid support
- source type: manual
- authors: ADCIRC development team
- year: active documentation site
- link: https://adcirc.github.io/adcirc/technical_reference/input_files/fort14.html ; https://adcirc.github.io/adcirc/technical_reference/input_files/time_varying_bathymetry.html ; https://adcirc.github.io/adcirc/tools/subgrid_adcirc_utility.html ; https://adcirc.github.io/adcirc/tools/oceanmesh2d.html
- local path: raw/code/adcirc/adcirc/docs/technical_reference/input_files and tools pages

## Why This Matters

Bathymetry handling is one of the least documented but most consequential setup layers in real projects.

## Core Claims

- base bathymetry is stored directly in `fort.14`
- ADCIRC supports time-varying bathymetry through `fort.141` when `NDDT` is nonzero
- `OceanMesh2D` provides bathymetry/topography interpolation and DEM support
- `SubgridADCIRCUtility` supports high-resolution terrain representation without requiring uniformly fine mesh resolution

## Practical Value

- method details: distinguishes standard bathymetry assignment from advanced terrain workflows
- implementation detail: keeps `fort.141` and subgrid methods from being confused with the default first setup path
- validation detail: highlights that vertical-datum and interpolation workflow must be documented outside the solver itself
- limitations: official docs do not prescribe a canonical topo-bathy assembly recipe

## Relevance Tags

- solver: ADCIRC
- physics: bathymetry and topography
- numerics: terrain representation
- diagnostics: datum and interpolation consistency
- failure mode: inconsistent terrain pipeline

## Transferability

High for coastal inundation and surge projects.

## Extraction Targets

- define the local bathymetry assembly checklist
- decide when subgrid or time-varying bathymetry should be considered

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
