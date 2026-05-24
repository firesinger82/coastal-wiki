---
citation_status: source-needed
origin: _staging/from-modeling-wiki/knowledge/methods/adcirc-sources/25-local-wide6-mesh-evidence.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# Local wide6 Mesh Evidence

Date: 2026-04-13

Purpose:
- record why `wide6` is the current local mesh baseline candidate
- separate trusted local evidence from still-experimental mesh branches

## Source Paths

- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\WORK_LOG.md`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\scripts\make_mesh_om2d.m`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\scripts\make_mesh_wide6.py`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\output`

## Core Claims

- `wide6` is not just a design folder; it contains:
  - generated `fort.14`
  - generated `fort.13`
  - generated `fort.15`
  - ADCIRC run outputs
  - validation outputs
- the local work log explicitly treats `OceanMesh2D` as the successful path
- the same work log explicitly records repeated `Gmsh` failure
- `OCSMesh` exists nearby as a reimplementation track, not as the accepted baseline

## Observed OceanMesh2D Evidence

- `make_mesh_om2d.m` is a full scripted workflow, not a partial note
- it defines:
  - domain polygon assembly from shapefiles
  - two-level size setup
  - mesh generation through `meshgen`
  - bathymetry interpolation from `GEBCO` and `BADA2024`
  - automatic boundary construction
  - `fort.14` write-out
- the output folder contains runnable ADCIRC artifacts and completed run outputs under `output/oceanmesh2d`

Observed configuration in the script:
- L1 `h0=500m`, `fs=3`, `max_el=60km`
- L2 `h0=50m`, `fs=3`, `max_el=15km`
- bathymetry: `GEBCO` plus `BADA2024`

## Observed wide6 Work-Log Evidence

The log records these practical findings:
- `Gmsh` Algorithm 5/6 failed to track the size field cleanly or produced poor quality
- `Gmsh` Algorithm 1 tracked the field better but still produced irregular mesh
- the local conclusion written in the log is that `Gmsh` is not suitable for this marine mesh
- the final accepted branch used `OceanMesh2D`
- the accepted branch reduced node count from about `1.26M` to about `475K`
- later entries record stable `ADCIRC` execution and validation work on the `wide6` branch

## Observed Gmsh Evidence

- `make_mesh_wide6.py` is a serious Python+Gmsh workflow, not a toy script
- `output/gmsh` contains a generated `fort.14`, `.msh`, size-field files, and diagnostics
- but the local evidence stack still ranks it below `OceanMesh2D` because:
  - the work log records failure as the local interpretation
  - the trusted run artifacts are under `output/oceanmesh2d`, not `output/gmsh`

## Interpretation

Current local ranking:
1. `wide6` `OceanMesh2D` branch: trusted baseline candidate
2. `OCSMesh` branch: exploratory reimplementation candidate
3. `Gmsh` branch: failed but still worth structured revalidation

This ranking is based on local execution evidence, not on general community preference.

## What This Closes

- the local mesh baseline should not be an abstract `SMS vs OceanMesh2D` discussion anymore
- the actual local reference branch is `wide6`
- `wide6` currently points to `OceanMesh2D`, not to `Gmsh`

## What Still Remains Open

- whether `OceanMesh2D` can be partially or fully ported into Python without losing the behavior that made `wide6` work
- whether `OCSMesh` can reproduce the same domain, bathymetry, and stability properties
- whether `Gmsh` failed because of the tool itself or because of the current field/boundary strategy
