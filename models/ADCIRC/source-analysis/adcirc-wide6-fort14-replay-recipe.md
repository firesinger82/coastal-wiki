---
title: "adcirc wide6 fort14 replay recipe"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-wide6-fort14-replay-recipe.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC wide6 fort.14 Replay Recipe

Date: 2026-04-13

Purpose:
- define the narrowest plausible replay path for the retained `wide6` `fort.14`
- stop the scope before `fort.13`, `fort.15`, and run tuning
- identify exactly where scriptable generation ends and boundary correction begins

Target artifact:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\output\oceanmesh2d\fort.14`

Scope:
- `make_mesh_om2d.m`
- boundary correction stage
- current retained `fort.14`

Out of scope:
- `fort.13`
- `fort.15`
- `run.bat`
- validation plots

## Working Rule

This is a replay **candidate** recipe, not a guaranteed fully reproducible recipe.

What it is good for:
- reconstructing the mesh-generation path
- identifying the minimum manual steps
- providing a fair target before evaluating `OCSMesh`

What it is not yet good for:
- exact one-click regeneration of the retained `fort.14`

## Replay Boundary

The current best interpretation is:

1. domain and coastline inputs are prepared
2. `make_mesh_om2d.m` generates an initial OceanMesh2D mesh and writes an initial `fort.14`
3. OceanMesh2D auto boundary classification is not trusted
4. boundary classification is corrected manually or semi-manually
5. corrected `fort.14` becomes the retained mesh artifact

This is the path that must be closed before `OCSMesh` comparison is meaningful.

## Confirmed Inputs

These are the strongest confirmed mesh-generation inputs.

Core domain files:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\input\mainland.shp`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\input\ocean_new_w6.shp`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\input\korea_coast_2025.shp`

Bathymetry files:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\input\DEM\gebco_450m.nc`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\input\DEM\BADA2024.nc`

Generator:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\scripts\make_mesh_om2d.m`

Boundary-correction candidates:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\scripts\classify_boundaries.py`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\scripts\fix_boundaries.py`

Design/support evidence:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\WORK_LOG.md`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\output\design\*`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\output\oceanmesh2d\matlab_log.txt`

## Stage 0. Preconditions

The recipe assumes:
- MATLAB with OceanMesh2D is available
- `E:\numerical_models\adcirc\tools\OceanMesh2D` is a valid local install
- the retained input shapefiles are already in their current form

Important warning:
- this last point is critical
- the replay starts from the **current retained inputs**
- it does not reconstruct every earlier draft of the coastline or offshore arc

## Stage 1. Domain Preparation

### Goal

Produce the domain geometry that `make_mesh_om2d.m` expects.

### Expected retained state

`make_mesh_om2d.m` expects:
- `mainland.shp`: land boundary
- `ocean_new_w6.shp`: two line features
  - feature 1: offshore/open boundary arc
  - feature 2: Taiwan-to-China land-side continuation

### What is confirmed

From the script and log:
- the domain is built by concatenating `mainland.shp` and the reversed offshore arc
- the offshore boundary concept is NDMI-style and manually designed
- the final `ocean_new_w6.shp` is already a curated input, not a raw coastline extract

### What is not closed

Not yet closed:
- the full earlier editing history that led to the current retained `mainland.shp`
- the exact GUI click history that produced the current retained `ocean_new_w6.shp`

### Practical replay rule

For replay purposes, accept the retained current shapefiles as the domain source of truth.

## Stage 2. OceanMesh2D Mesh Generation

### Goal

Generate the first `fort.14` candidate from the retained inputs.

### Retained script behavior

`make_mesh_om2d.m` does the following:

1. reads `mainland.shp` and `ocean_new_w6.shp`
2. assembles a single domain polygon (`boubox`)
3. creates Level 1 geodata:
   - shoreline: `GSHHS_f_L1`
   - DEM: `gebco_450m.nc`
   - `h0=500`
   - `fs=3`
   - `max_el=60000`
   - `g=0.25`
4. creates Level 2 geodata:
   - shoreline: `korea_coast_2025.shp`
   - DEM: `gebco_450m.nc`
   - bbox: `[124 130; 33 38]`
   - `h0=50`
   - `fs=3`
   - `max_el=15000`
   - `g=0.20`
5. runs:
   - `meshgen('ef', {fh1, fh2}, 'bou', {gdat1, gdat2}, 'proj', 'mercator')`
6. interpolates bathymetry:
   - GEBCO first with `mindepth=5`
   - BADA2024 override in the Korean subdomain
7. calls:
   - `make_bc(m, 'auto', gdat1)`
8. writes `output/oceanmesh2d/fort.14`

### Replay checkpoint

At this point the generated file is only an **initial** `fort.14`.

Do not assume it matches the retained final `fort.14` yet.

### Strong evidence

The retained `matlab_log.txt` supports this stage:
- two-level generation
- `fs=3`
- wide and Korea subdomains
- bathymetry interpolation
- automatic boundary handling attempt

## Stage 3. Boundary Review

### Goal

Decide whether the initial OceanMesh2D boundary strings are acceptable.

### Current judgement

The answer is no.

Reason:
- `WORK_LOG.md` explicitly says auto classification failed
- the same log says manual GUI classification became necessary

### Retained evidence

Relevant retained tools:
- `classify_boundaries.py`
- `fix_boundaries.py`

Interpretation:
- `classify_boundaries.py` represents an interactive/manual correction path
- `fix_boundaries.py` represents a semi-automatic heuristic correction path

### Replay checkpoint

This is the first unavoidable provenance break:
- mesh generation is scriptable
- boundary acceptance is not yet fully scriptable with confidence

## Stage 4. Boundary Correction

### Goal

Transform the initial `fort.14` into the retained current boundary structure.

### Boundary state of the retained current `fort.14`

Direct checks on the retained file show:
- open boundaries: `1`
- total open boundary nodes: `70`
- land boundaries: `2189`
- total land boundary nodes: `102958`

Open-boundary depth range in the retained file:
- minimum: `217.727 m`
- maximum: `6313.561 m`

Interpretation:
- the retained boundary is mostly deep-water
- there is one shallow endpoint artifact
- the structure is internally consistent

### Most plausible correction path

The best current interpretation is:

Option A:
- run `make_mesh_om2d.m`
- inspect the largest boundary chain
- use `classify_boundaries.py`
- manually mark open-boundary start/end
- save corrected `fort.14`

Option B:
- run `make_mesh_om2d.m`
- apply `fix_boundaries.py`
- then review whether its result matches the retained `70`-node open boundary closely enough

### Preferred replay candidate

For provenance reconstruction, prefer:
- manual/interactively reviewed correction

Reason:
- the log explicitly says manual correction was required
- `fix_boundaries.py` is useful evidence, but it should not override the retained manual narrative

## Stage 5. Retained fort.14 Acceptance Check

After boundary correction, the replay candidate should be compared against the retained file.

Minimum checks:
- element count equals `852086`
- node count equals `475369`
- open boundary count equals `1`
- open boundary nodes equal `70`
- land boundary count equals `2189`
- bathymetry range is close to `5.0 ~ 7845.2876`
- open boundary is mostly deep-water with only endpoint shallowing

If these checks fail badly:
- the replay did not recover the retained branch

## What Is Confirmed

Confirmed:
- the retained `fort.14` is structurally valid
- `make_mesh_om2d.m` is the best replay anchor
- `GEBCO + BADA2024` are core bathymetry inputs
- boundary correction after initial generation is required
- the retained current `fort.14` is a post-correction artifact, not a raw OceanMesh2D auto-boundary output

## What Is Still Unknown

Still unknown:
- whether `classify_boundaries.py` exactly reproduces the final retained boundary if replayed today
- whether `fix_boundaries.py` was actually the last script used on the retained file
- the exact manual decisions that produced the final accepted open-boundary endpoints
- whether any additional smoothing or cleanup happened after the initial `make_mesh_om2d.m` write and before final acceptance

## Decision

For now the correct `fort.14` replay path is:

1. accept current retained input shapefiles and DEMs as source inputs
2. run `make_mesh_om2d.m` as the mesh-generation anchor
3. treat the resulting boundary strings as provisional only
4. apply manual boundary review/correction
5. compare the result against the retained current `fort.14`

## Why This Matters Before `OCSMesh`

`OCSMesh` should not be judged against:
- a vague memory of `wide6`
- or a mixed branch that includes later run tuning

It should be judged first against:
- the `fort.14` replay target

That target is now narrow enough to be meaningful:
- domain inputs
- OceanMesh2D generation
- boundary correction
- retained `fort.14`
