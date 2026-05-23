# wide6 Replay Candidate Spec

Date: 2026-04-13

Purpose:
- reconstruct the most plausible `wide6` workflow from retained artifacts
- separate confirmed steps from probable steps and unknown steps
- define what can and cannot currently be replayed

Target:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6`

## Core Judgement

`wide6` is currently an artifact-rich branch but not a replayable workflow.

The main reason is:
- the retained folder contains multiple generations of scripts and outputs
- the currently retained `fort.13` and `fort.15` do not cleanly correspond to one single retained script state
- some later changes were clearly manual or agent-assisted and are not fully recoverable from the current script set alone

## Branches That Must Be Kept Separate

There are at least three layers inside `wide6`.

### 1. Mesh-generation branch

This is the branch that produced the retained `fort.14`.

Strong candidates:
- `scripts/make_mesh_om2d.m`
- `input/mainland.shp`
- `input/ocean_new_w6.shp`
- `input/korea_coast_2025.shp`
- `input/DEM/gebco_450m.nc`
- `input/DEM/BADA2024.nc`

Manual/interactive companions:
- `scripts/draw_ocean_boundary.py`
- `scripts/design_ocean_boundary*.py`
- `scripts/prepare_boundary_qgis.py`
- `scripts/classify_boundaries.py`
- `scripts/fix_boundaries.py`

### 2. Retained run branch

This is the branch reflected by the current `output/oceanmesh2d/fort.13`, `fort.15`, and `run.bat`.

Strong evidence:
- `run.bat` says `wide6 Run4 (NAO99jb + Manning tuning)`
- current `fort.15` says `tide_nao99jb`
- current `fort.15` has `RNDAY=30`
- current `fort.13` includes Manning levels up to `0.060`

### 3. Historical tuning branches

These were retained but are not the same as the final branch.

Examples:
- `scripts/make_fort15.py` describes `FES2022b`
- `scripts/make_fort24_and_update.py` describes SAL activation through `fort.24`
- `scripts/tune_phase2_3.py` describes a different Manning pattern and `RNDAY 20 -> 30`
- `fort.13.bak_phase2_3` and `fort.15.bak_phase2_3` preserve one earlier state

## Confidence Table

| Item | Current confidence | Evidence | Notes |
| --- | --- | --- | --- |
| Current retained `fort.14` is real and structurally valid | Confirmed | direct `fort.14` check | counts and boundary block are internally consistent |
| `make_mesh_om2d.m` is the closest retained generator for current `fort.14` | Confirmed | file timing, file paths, mesh size narrative, output location | this is the strongest mesh-generation script candidate |
| `mainland.shp` + `ocean_new_w6.shp` are core domain inputs | Confirmed | script references and retained inputs | these are part of the final mesh path |
| `GEBCO + BADA2024` were core bathymetry inputs | Confirmed | `make_mesh_om2d.m`, `WORK_LOG.md`, retained DEM files | exact smoothing recipe still unresolved |
| open-boundary auto classification failed and manual correction was required | Confirmed | `WORK_LOG.md`, `classify_boundaries.py`, `fix_boundaries.py` | critical provenance gap |
| current retained `fort.15` came from `make_fort15_nao99jb.py` or a close derivative | High | current `fort.15` says `tide_nao99jb`; script writes same identifier and same general structure | likely, but not fully frozen |
| current retained `run.bat` belongs to the NAO99jb tuning branch | Confirmed | direct file content | points to a later branch than the early FES2022b notes |
| current retained `fort.13` came directly from one retained script | Unconfirmed | current `fort.13` has `0.050` and `0.060` Manning values | these values are not produced by the retained `make_fort13.py`, `make_fort13_tuned.py`, `make_fort24_and_update.py`, or `tune_phase2_3.py` exactly |
| current retained validation figures correspond exactly to the currently retained `fort.13/fort.15` pair | Unconfirmed | artifact chain exists but provenance is mixed | very likely related, not yet proven exactly |

## Confirmed Inputs

These should be treated as confirmed replay inputs for the mesh branch:
- `input/mainland.shp`
- `input/ocean_new_w6.shp`
- `input/korea_coast_2025.shp`
- `input/DEM/gebco_450m.nc`
- `input/DEM/BADA2024.nc`

These should be treated as confirmed retained outputs:
- `output/oceanmesh2d/fort.14`
- `output/oceanmesh2d/fort.13`
- `output/oceanmesh2d/fort.15`
- `output/oceanmesh2d/run.bat`
- `output/validation/*`

## Most Plausible Replay Skeleton

This is the current best reconstruction.

### Stage A. Domain preparation

Likely steps:
1. derive or edit mainland boundary
2. design offshore boundary arc manually using NDMI-style guidance
3. save domain inputs under `mainland.shp` and `ocean_new_w6.shp`
4. prepare Korean high-resolution coastline input

Evidence:
- `WORK_LOG.md`
- `draw_ocean_boundary.py`
- `design_ocean_boundary*.py`
- `prepare_boundary_qgis.py`
- `output/design/*.png`

Confidence:
- medium

Reason confidence is not higher:
- final manual GUI sequence is not frozen

### Stage B. Mesh generation

Likely steps:
1. run `make_mesh_om2d.m`
2. use Level 1 `GSHHS_f_L1` + GEBCO with `h0=500`
3. use Level 2 `korea_coast_2025.shp` + GEBCO with `h0=50`
4. apply `fs=3` sizing on both levels
5. interpolate GEBCO and override Korean nodes with BADA
6. write initial `fort.14`

Evidence:
- `make_mesh_om2d.m`
- `matlab_log.txt`
- retained `fort.14`

Confidence:
- high

### Stage C. Boundary correction

Likely steps:
1. review the generated mesh boundary
2. reject OceanMesh2D auto boundary strings
3. reclassify open vs land boundary manually or semi-manually
4. rewrite `fort.14`

Evidence:
- `WORK_LOG.md`
- `classify_boundaries.py`
- `fix_boundaries.py`
- direct `fort.14` boundary inspection

Confidence:
- high that this stage existed
- low that the exact retained script can replay the final outcome without manual help

### Stage D. Control-file generation and tuning

Likely steps:
1. generate an initial `fort.13`
2. generate an initial `fort.15`
3. apply later tuning for tides, Manning, output windows, and run settings

Evidence:
- `make_fort13.py`
- `make_fort13_tuned.py`
- `make_fort15.py`
- `make_fort15_nao99jb.py`
- `make_fort24_and_update.py`
- `tune_phase2_3.py`
- `fort.13.bak_phase2_3`
- `fort.15.bak_phase2_3`

Confidence:
- low for an exact replay

Reason:
- the current retained `fort.15` is clearly NAO99jb-based, not the early FES2022b version
- the current retained `fort.13` contains Manning values not exactly reproduced by the retained scripts

### Stage E. Run and validation

Likely steps:
1. run `adcprep`
2. run `padcirc`
3. postprocess `fort.63.nc`
4. compare harmonics and generate validation figures

Evidence:
- `run.bat`
- retained PE folders
- `fort.63.nc`, `fort.64.nc`, `maxele.63.nc`, `maxvel.63.nc`
- `validate_tidal_harmonics.py`
- `output/validation/*`

Confidence:
- high that this happened
- medium that the currently retained postprocessing scripts exactly match the current retained validation images

## Strong Provenance Warnings

### Warning 1. `fort.15` branch drift

`WORK_LOG.md` earlier describes:
- `FES2022b`

But the current retained `fort.15` says:
- `tide_nao99jb`

So the folder mixes at least two forcing/control eras.

### Warning 2. `fort.13` script mismatch

The current retained `fort.13` contains Manning values:
- `0.025`
- `0.030`
- `0.035`
- `0.040`
- `0.045`
- `0.050`
- `0.060`

But the retained scripts that generate `fort.13` do not cleanly explain this exact set as the final state.

Interpretation:
- later manual or agent-assisted edits likely happened
- or an unretained generator script existed
- or a retained script was edited after the file was generated

### Warning 3. Validation provenance is not yet frozen

The retained validation outputs are valuable evidence.

But we do not yet know with full confidence:
- which exact `fort.13`
- which exact `fort.15`
- which exact forcing option
- and which exact run window

produced every retained validation figure.

## Replay Candidate Levels

To avoid pretending more certainty than we have, use three replay levels.

### Replay Level 1: Artifact inspection only

What it means:
- inspect retained files
- do not regenerate anything

Status:
- possible now

### Replay Level 2: Mesh replay candidate

What it means:
- regenerate something close to the retained `fort.14`
- using the retained mesh inputs and `make_mesh_om2d.m`
- then apply explicit manual boundary correction

Status:
- plausible now

Main risk:
- boundary correction and bathymetry smoothing are not frozen enough

### Replay Level 3: Full run replay candidate

What it means:
- regenerate `fort.14`, `fort.13`, `fort.15`
- rerun ADCIRC
- reproduce validation figures

Status:
- not yet credible

Main risk:
- current control-file provenance is mixed and partly unknown

## Immediate Next Step

The next best document is:
- `wide6 replay candidate matrix`

It should mark each file or step as:
- confirmed final
- likely final
- historical branch only
- unknown provenance

## Decision

For now:
- treat `make_mesh_om2d.m` as the best available mesh replay anchor
- treat boundary correction as a mandatory manual stage
- treat current `fort.13` and `fort.15` as retained run artifacts, not as cleanly reproducible outputs
