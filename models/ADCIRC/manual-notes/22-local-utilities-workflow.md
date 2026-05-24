---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/22-local-utilities-workflow.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# Local Utilities Workflow

Date: 2026-04-12

Purpose:
- record the local evidence found in `E:\numerical_models\adcirc\tools\utilities`
- connect notebook-level workflow evidence to the ADCIRC preprocessing knowledge base

## Top-Level Structure

Observed items:
- `JMA_MSM.ipynb`
- `merge_nc.ipynb`
- `nc2fort22.ipynb`
- `core/`
- `grid/`
- `postprocess/`
- `github/`

This is not just a scratch folder.
It looks like a local utility repository with both forcing and grid-related work.

## Forcing Workflow Evidence

Notebook evidence in `JMA_MSM.ipynb` shows:
- multiple source NetCDF files are opened with `xarray.open_mfdataset(...)`
- the file pattern includes `09*.nc`
- the merged output is written to `combined.nc`

Notebook evidence in `nc2fort22.ipynb` shows:
- `combined.nc` is opened as the source file
- `fort.22.nc` is created as the destination file
- source variables are mapped as:
  - `psea -> PSFC`
  - `u -> U10`
  - `v -> V10`
- pressure is converted from `Pa` to `mb`
- output units are written as:
  - `PSFC`: `mb`
  - `U10`: `m s-1`
  - `V10`: `m s-1`

Interpretation:
- a concrete local `JMA-MSM -> combined.nc -> fort.22.nc` branch exists
- the mapping toward ADCIRC `NWS=13` is explicit in retained notebook form
- the packaged GUI converter is probably not the only evidence-bearing implementation

## Grid Utility Evidence

Observed files under `grid/`:
- `bath_interp.f`
- `interp.f`
- `Griddata_v1.32.F90`
- `Gridscope_ver1.22.f90`
- `f13builderv8.3.zip`
- `coarsengrid.zip`
- `nicegrid2.zip`

Interpretation:
- the local preprocessing environment includes older or auxiliary grid and bathymetry tools outside the main `SMS` versus `OceanMesh2D` decision
- these should be treated as helper or legacy tools until their active use is confirmed

## Repository Mirror Evidence

Observed local mirrors under `github/` include:
- `adcirc-cg`
- `ADCIRCModules`

Interpretation:
- the utilities directory also serves as an offline technical reference cache
- it may preserve documentation or helper code that is easier to search locally than the main model tree

## What This Closes

This note closes these uncertainties:
- the local workflow is not only executable-based
- notebook logic for `fort.22.nc` creation survives locally
- forcing conversion and grid helper tools are co-located in one utilities repository

## What Still Remains Open

- whether `JMA_MSM.ipynb` is still the current production path
- what the raw upstream `JMA-MSM` source directory is for the `09*.nc` pattern
- whether `combined.nc` is only an intermediate debug artifact or part of the standard workflow
- which `grid/` utilities are still active versus archival
