---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/31-wide6-fort14-structural-check.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# wide6 fort.14 Structural Check

Date: 2026-04-13

Target file:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\output\oceanmesh2d\fort.14`

Purpose:
- perform the first low-cost direct check on the retained `wide6` mesh
- separate file-structure correctness from higher-level physical validation

## What Was Checked

- header counts
- node coordinate and bathymetry ranges
- element line structure and node references
- open-boundary count and node count
- land-boundary count and node count
- boundary node references
- open-boundary depth range

## Results

### File header

- title: `OceanMesh2D`
- elements: `852086`
- nodes: `475369`

This matches the retained `WORK_LOG.md` counts.

### Node ranges

- longitude range: `116.4120499176` to `146.085424266`
- latitude range: `18.010983624` to `52.1838404002`
- bathymetry range: `5.0` to `7845.2876`

This is broadly consistent with the retained wide-domain design narrative.

### Element integrity

- malformed element lines: `0`
- non-triangular element declarations: `0`
- out-of-range element node references: `0`

Interpretation:
- the mesh file is structurally sound at the element-connectivity level

### Boundary integrity

- open boundaries: `1`
- total open-boundary nodes: `70`
- land boundaries: `2189`
- total land-boundary nodes: `102958`
- land boundary `ibtype` counts:
  - `20`: `1`
  - `21`: `2188`
- out-of-range boundary node references: `0`

Interpretation:
- the boundary block is internally consistent
- the retained `WORK_LOG.md` statement "`open 1개(70pts) + land 2,189개`" matches the file if `2,189` is read as the number of land boundary segments, not the total number of land-boundary nodes

### Open-boundary depth check

Computed directly from the `fort.14` open-boundary nodes:
- minimum open-boundary depth: `217.727`
- maximum open-boundary depth: `6313.561`

This is important because the retained `WORK_LOG.md` says:
- `경계1 (open): 태평양 arc, 수심 283~6314m`

Interpretation:
- the upper deep-water claim is consistent
- the minimum depth claim is not exactly consistent with the retained `fort.14`
- this does not invalidate the mesh, but it does show that the log is not precise enough to be treated as ground truth

## Judgement

What this check closes:
- `fort.14` is structurally valid enough to be taken seriously
- the retained `wide6` artifact is not corrupt or obviously malformed

What this check does **not** close:
- whether the boundary geometry is physically appropriate
- whether the bathymetry processing is correct
- whether the open-boundary placement is optimal
- whether the mesh is good enough for accepted tidal or surge validation

## Practical Meaning

This check strengthens one claim:
- `wide6` is a real and internally consistent mesh artifact

But it weakens another claim:
- `WORK_LOG.md` should not be treated as exact truth without checking the artifacts themselves

## Next Direct Checks

The next useful `fort.14`-adjacent checks are:
- inspect the open-boundary geometry and depth profile directly
- inspect whether the `217.727 m` shallowest open-boundary node is acceptable or a cleanup miss
- inspect boundary strings and nearby elements around the open boundary
- connect this to the retained validation summary and decide whether the current boundary placement could explain part of the tidal mismatch
