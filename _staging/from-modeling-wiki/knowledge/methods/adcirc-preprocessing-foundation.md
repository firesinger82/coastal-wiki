# ADCIRC Preprocessing Foundation

Date: 2026-04-12

Purpose:
- define the preprocessing layer that must be stabilized before serious ADCIRC project work
- separate mesh generation, bathymetry construction, and forcing ingestion from later parameter tuning

This note is a foundation note, not a run recipe.

## Why This Comes First

For local ADCIRC work, the hardest early failure modes usually do not start in `DT` or `TAU0`.
They start earlier:
- the wrong meshing toolchain is chosen
- bathymetry and coastline data are assembled inconsistently
- boundary strings are assigned incorrectly
- meteorological forcing is available, but not in a schema ADCIRC actually accepts

That means preprocessing is the first system to stabilize.

## Core Observation From Official Docs

Official ADCIRC documentation puts a large fraction of project setup pressure on the preprocessing layer:
- `fort.14` is required and contains the finite element grid, bathymetry, and boundary information
- boundary locations are defined in `fort.14`
- periodic and non-periodic boundary forcing are split across `fort.15`, `fort.19`, and `fort.20`
- meteorological forcing is selected through `NWS` and usually depends on a `fort.22` family input
- the official tools page explicitly separates mesh generation, forcing acquisition, and automation into different tool families

## Three Foundation Axes

### 1. Mesh Generation And Boundary Construction

Questions:
- which tool should be used to build or edit the mesh?
- how are shoreline, open-ocean, river, and barrier boundaries turned into node strings?
- how reproducible is the mesh-generation path?

Primary outputs:
- `fort.14`
- sometimes `fort.13`
- sometimes helper geometry, GIS, or project files outside ADCIRC itself

Primary note:
- `adcirc-mesh-tool-selection.md`

### 2. Bathymetry And Topography Assembly

Questions:
- which DEM, chart, or survey sources define the bed and land elevations?
- what datum are they in?
- how are they transferred into `DP` at each node in `fort.14`?

Primary outputs:
- bathymetric `DP` values in `fort.14`
- possibly `fort.13` nodal attributes
- possibly `fort.141` when time-varying bathymetry is actually part of the problem

Primary note:
- `adcirc-bathymetry-input-foundation.md`

### 3. External Forcing Ingestion

Questions:
- which boundary forcing data are needed?
- which meteorological forcing family should be used?
- what conversion step is needed between raw source data and ADCIRC-readable files?

Primary outputs:
- boundary forcing setup in `fort.14`, `fort.15`, `fort.19`, `fort.20`
- meteorological forcing through `fort.22` or related files
- for the local storm-surge branch, `JMA-MSM -> OWI NetCDF -> NWS=13`

Primary note:
- `adcirc-forcing-input-foundation.md`

## What The Official Tooling Map Implies

The docs do not present one single universal preprocessor. Instead they expose an ecosystem:
- `SMS` as a broad GUI-based commercial environment
- `OceanMesh2D` as an open MATLAB-based end-to-end mesh-generation path
- `SubgridADCIRCUtility` as a specialized terrain/subgrid enhancement path
- `MetGet` as a meteorological forcing acquisition and development system
- `f13builder` and related utility programs for nodal attributes

This implies that tool choice is itself part of the project design, not a minor implementation detail.

## Current Local Direction

The first local priority should be:
1. preserve and understand the currently working mesh branch
2. define the bathymetry assembly path inside that branch
3. define the forcing ingestion path
4. only after that, move deeper into project-specific storm-surge setup

Known local facts:
- for storm-surge work, the dominant forcing path is `JMA-MSM` with `NWS=13`
- for wide-area mesh work, the current local baseline candidate is `wide6`
- `wide6` currently points to an `OceanMesh2D` workflow

This changes the mesh question from:
- "what mesh tool should we pick"

to:
- "what exactly made `wide6` work, and can any other stack reproduce it"

## What This Note Does Not Decide

This note does not yet decide:
- whether `SMS` or `OceanMesh2D` should be the long-term default
- which bathymetry source should be canonical for your project
- which mesh resolution or tidal constituent set should be used
- whether subgrid ADCIRC is needed

## Next Notes To Keep Linked

- `adcirc-mesh-tool-selection.md`
- `adcirc-mesh-revalidation-principles.md`
- `adcirc-bathymetry-input-foundation.md`
- `adcirc-forcing-input-foundation.md`
- `adcirc-information-gaps.md`
