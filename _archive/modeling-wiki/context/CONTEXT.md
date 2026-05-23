# Current Context

## Current Objective

Build the ADCIRC foundation first so future trial-and-error work accumulates cleanly.

## Current Domain

- active model: ADCIRC
- focus type: foundation building before regular experiment accumulation
- current domain: coastal hydrodynamics / numerical modeling

## Current Constraints

- time budget: keep the first setup lightweight and repeatable
- compute budget: avoid broad multi-model setup until ADCIRC structure is stable
- data availability: forcing and mesh evidence are partially ingested, but bathymetry and mesh reproducibility are not closed yet
- validation target: define after foundational ADCIRC sources are collected

## Current Working Assumptions

- the first durable value will come from ADCIRC-specific source curation, not from backfilling old runs
- one active model at a time will reduce vocabulary drift and mixed heuristics
- `wide6` is the current local mesh baseline candidate
- `OceanMesh2D` is the current local baseline path, while `Gmsh` and `OCSMesh` remain revalidation tracks

## Current Risks

- collecting too many generic sources before defining ADCIRC-specific needs
- starting mesh redesign before `wide6` is documented well enough to preserve
- mixing baseline-preservation work with `Gmsh` or `OCSMesh` revalidation too early

## Next Decisions

- define the exact ingredients that make `wide6` reproducible
- define the first fair revalidation frame for `OceanMesh2D` translation, `Gmsh`, and `OCSMesh`
- close the canonical bathymetry workflow used by the mesh baseline

## Notes

Use this file only for current state, not permanent knowledge.
