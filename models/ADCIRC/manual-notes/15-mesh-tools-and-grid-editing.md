---
citation_status: source-needed
origin: _staging/from-modeling-wiki/knowledge/methods/adcirc-sources/15-mesh-tools-and-grid-editing.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# Mesh Tools And Grid Editing

## Metadata

- date: 2026-04-12
- title: mesh-tool ecosystem, SMS, OceanMesh2D, and grid editing
- source type: manual
- authors: ADCIRC development team
- year: active documentation site
- link: https://adcirc.github.io/adcirc/tools/index.html ; https://adcirc.github.io/adcirc/tools/sms.html ; https://adcirc.github.io/adcirc/tools/oceanmesh2d.html ; https://adcirc.github.io/adcirc/user_guide/tips_and_tricks/grid_dev_edit.html
- local path: E:\AI_ENV\modeling-wiki\raw\code\adcirc\adcirc\docs\tools\index.rst and related pages

## Why This Matters

This source bundle is the official basis for narrowing the mesh-generation shortlist.

## Core Claims

- the docs explicitly surface `SMS` and `OceanMesh2D` as front-line meshing tools
- `SMS` is a commercial Windows GUI environment popular with ADCIRC users
- `OceanMesh2D` is an open MATLAB-based automated mesh generator
- `OceanMesh2D` can also help with boundary conditions, bathymetry/topography interpolation, `fort.13`, `fort.15`, and some forcing-related preprocessing
- the grid development docs warn that users should carefully weigh building new meshes versus revising existing ones

## Practical Value

- method details: justifies focusing first on `SMS` versus `OceanMesh2D`
- implementation detail: identifies scripted versus GUI-heavy workflow tradeoffs
- validation detail: reminds us that boundary construction and mesh editing are part of the same decision
- limitations: docs do not provide a universal winner

## Relevance Tags

- solver: ADCIRC
- physics: preprocessing
- numerics: mesh generation
- diagnostics: reproducibility
- failure mode: wrong toolchain choice

## Transferability

High for any 2D ADCIRC coastal setup.

## Extraction Targets

- define local shortlist and selection criteria
- identify whether scripted reproducibility is a hard requirement

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
