---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/14-fort14-grid-bathymetry-boundaries.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
---
# Fort.14 Grid, Bathymetry, And Boundaries

## Metadata

- date: 2026-04-12
- title: fort.14 as the combined mesh, bathymetry, and boundary artifact
- source type: manual
- authors: ADCIRC development team
- year: active documentation site
- link: https://adcirc.github.io/adcirc/technical_reference/input_files/fort14.html
- local path: raw/code/adcirc/adcirc/docs/technical_reference/input_files/fort14.rst

## Why This Matters

This is the key source for understanding why preprocessing is the first bottleneck.

## Core Claims

- `fort.14` is required
- it contains nodal data, element data, open-boundary data, and flow-boundary data
- it also contains the bathymetric data used by ADCIRC
- therefore mesh generation, bathymetry assignment, and boundary construction are not separable in the final ADCIRC artifact

## Practical Value

- method details: defines the actual object preprocessing must produce
- implementation detail: prevents treating mesh, bathymetry, and boundaries as independent late-stage edits
- validation detail: explains why many setup failures should be debugged at the `fort.14` level first
- limitations: does not tell us which meshing tool or bathymetry source is best

## Relevance Tags

- solver: ADCIRC
- physics: preprocessing
- numerics: mesh construction
- diagnostics: boundary and depth integrity
- failure mode: malformed mesh or boundary encoding

## Transferability

Universal for all ADCIRC projects.

## Extraction Targets

- define the preprocessing object model around `fort.14`
- link bathymetry and boundary work directly to mesh-generation choices

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
