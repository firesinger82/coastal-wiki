# ADCIRC Mesh Revalidation Spec

Date: 2026-04-13

## Why This Spec Exists

The mesh question is no longer just "which tool is popular".
The real local problem is:
- there is one tuned branch (`wide6`)
- several other attempts exist
- many of those attempts failed
- we need a reliable way to preserve what works and re-test what did not

## Scope

This spec covers:
- local baseline selection for wide-domain ADCIRC mesh work
- revalidation tracks for `OceanMesh2D`, `Gmsh`, and `OCSMesh`
- documentation rules for mesh evidence

This spec does not yet cover:
- storm-surge run recipes
- final operational nesting setup
- final parameter tuning inside `fort.15`

## Current Baseline

Current trusted baseline candidate:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6`
- active branch: `OceanMesh2D`

Reason:
- it is the only local branch with mesh, control files, run outputs, and validation outputs all present together

## Tracks

### Track A: Preserve wide6

Questions:
- what exact inputs and scripts define the wide6 mesh
- what manual interventions were required
- what downstream fixes were essential

Artifacts to capture:
- domain shapefiles
- DEM sources
- mesh script inputs
- boundary classification rules
- bathymetry smoothing rules

### Track B: Translate OceanMesh2D

Questions:
- can the current MATLAB logic be ported into Python or another stack
- which pieces are direct translations and which are behaviorally hard to reproduce

Success condition:
- reproduced mesh quality and downstream stability close enough to the baseline

### Track C: Revalidate Gmsh

Questions:
- did `Gmsh` fail because of field design, boundary handling, or the engine itself
- can a cleaner workflow fix the known failure modes

Success condition:
- quality and downstream behavior comparable to the baseline

### Track D: Revalidate OCSMesh

Questions:
- can `OCSMesh` reproduce the wide6-scale domain from known inputs
- can it handle bathymetry and boundary generation at acceptable quality

Success condition:
- reproducible basin mesh with acceptable quality and at least one stable downstream run

## Documentation Rule

For mesh work, every promoted claim must be backed by one of:
- source script evidence
- generated mesh artifacts
- run outputs
- validation outputs
- explicit local work-log statements

## Immediate Outputs Required

- `adcirc-mesh-revalidation-principles.md`
- `25-local-wide6-mesh-evidence.md`
- update to `adcirc-mesh-tool-selection.md`
- update to preprocessing and information-gap notes
