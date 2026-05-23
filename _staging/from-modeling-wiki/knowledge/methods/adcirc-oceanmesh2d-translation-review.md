# ADCIRC OceanMesh2D Translation Review

Date: 2026-04-13

Purpose:
- decompose `make_mesh_om2d.m` into functional units
- assess which parts are easy to translate, hard to translate, or better replaced by another tool
- compare the main GitHub candidates for the MATLAB and Python tracks

Primary local script:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\scripts\make_mesh_om2d.m`

Supporting local evidence:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\WORK_LOG.md`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\ocsmesh_test\scripts\step3_ocsmesh_basin.py`

## Important Warning

`make_mesh_om2d.m` is not the whole workflow.

The local `wide6` evidence shows that the final viable branch also needed:
- manually drawn outer boundary geometry
- manual open-boundary classification
- bathymetry slope limiting and smoothing
- degenerate-element cleanup

So any translation effort must reproduce the workflow, not only the visible MATLAB file.

## Functional Decomposition

| Unit | Local script role | Translation judgement | Best Python-side candidate | Notes |
| --- | --- | --- | --- | --- |
| Environment bootstrap | add OceanMesh2D path and set I/O folders | Easy | plain Python | mechanical only |
| Domain polygon assembly | read `mainland.shp` and `ocean_new_w6.shp`, merge arcs into `boubox` | Easy | `geopandas` + `shapely` | direct translation is straightforward |
| Level-1 geodata setup | `geodata(... 'GSHHS_f_L1', 'dem', gebco, 'bbox', boubox, 'h0', 500)` | Medium | `oceanmesh` | concept maps well, exact internals do not |
| Level-2 local geodata setup | `geodata(... korea_coast_2025.shp, bbox_korea, h0=50)` | Medium | `oceanmesh` or `OCSMesh` | easy geometrically, harder to match behavior exactly |
| Size-function construction | `edgefx(... fs=3, max_el, g)` at two levels | Hard | `oceanmesh` first, `OCSMesh` second | exact `fs=3` semantics are the main translation risk |
| Core mesh generation | `meshgen(...).build` with multilevel boundaries and `mercator` projection | Hard | `oceanmesh` first, `OCSMesh` second | this is the heart of the porting problem |
| GEBCO bathymetry interpolation | `interp(m, gdat1, 'mindepth', 5)` | Medium | `OCSMesh`, `DEM2GRDv3`, or custom Python | achievable, but exact interpolation behavior needs testing |
| BADA local override | read `BADA2024.nc`, interpolate selected nodes, replace depths in Korean subdomain | Easy | `xarray` + `scipy` | already almost line-for-line portable |
| Boundary auto classification | `make_bc(m, 'auto', gdat1)` | Hard and risky | custom Python or partial tool support | local `wide6` evidence says auto classification failed |
| fort.14 write and plotting | `write(m, fort.14)` and quick tri plot | Medium | `OCSMesh`, custom writer, `meshio` | output format support must be verified case by case |

## What Is Actually Easy To Port

- shapefile reading and polygon assembly
- NetCDF reading
- BADA local depth override
- bookkeeping, logging, and artifact writing

## What Is Hard To Port

- exact multilevel sizing behavior behind `edgefx`
- exact mesh-quality and topology behavior behind `meshgen`
- automatic boundary classification that is trustworthy for the final domain

## What Should Not Be Treated As A Pure Porting Problem

These are workflow problems, not only language problems:
- manually designing the offshore boundary arc
- deciding which boundary nodes are truly open
- slope limiting and smoothing after interpolation
- preserving downstream ADCIRC stability

## GitHub Review

### MATLAB Upstream: `CHLNDDEV/OceanMesh2D`

Why it matters:
- direct upstream match to the local baseline
- repo architecture mirrors the local script exactly through `geodata`, `edgefx`, `meshgen`, `msh`
- current inspected repo page shows release `6.0.0` on `2024-02-28`

Assessment:
- best reference for understanding what `wide6` is doing
- still the canonical source for behavior, even if the long-term goal is Python

### Python Candidate 1: `CHLNDDEV/oceanmesh`

Why it matters:
- closest conceptual relative to `OceanMesh2D`
- uses shoreline plus DEM driven sizing and mesh generation
- includes cleanup utilities for bad boundary/quality situations

Assessment:
- best first candidate for translating the `OceanMesh2D` worldview into Python
- strongest candidate for reproducing the shape of `make_mesh_om2d.m`
- local machine now has it installed and importable
- Windows requires the local CGAL/vcpkg environment to be wired correctly

### Python Candidate 2: `noaa-ocs-modeling/OCSMesh`

Why it matters:
- local `ocsmesh_test` already exists
- strong raster-driven and engine-agnostic Python workflow
- current inspected repo page shows release `v2.1.1` on `2026-03-05`

Assessment:
- best candidate if the workflow is rebuilt around DEM, `Geom`, `Hfun`, and engine abstraction
- weaker candidate for line-by-line translation of `make_mesh_om2d.m`
- stronger candidate for a fresh Python-native rebuild
- local machine now has it installed and importable

## Refined Mapping Around `edgefx` And `meshgen`

### `edgefx(fs=3, ...)`

There is no exact 1:1 public function called `edgefx` in the Python candidates.

Closest practical matches are:

For `oceanmesh`:
- `distance_sizing_function(...)`
- `feature_sizing_function(...)`
- `bathymetric_gradient_sizing_function(...)`
- `wavelength_sizing_function(...)`
- `enforce_mesh_gradation(...)`

Interpretation:
- `oceanmesh` is the closer conceptual match
- `edgefx(fs=3)` likely maps to a combination of shoreline feature sizing plus gradation control, not to one single function

For `OCSMesh`:
- `Hfun(...)`
- `add_subtidal_flow_limiter(...)`
- `add_contour(...)`

Interpretation:
- `OCSMesh` expresses sizing more as a composable `Hfun` object than as a direct `edgefx` analogue
- this is powerful, but less 1:1 with the OceanMesh2D mental model

### `meshgen(...).build`

Closest practical matches are:

For `oceanmesh`:
- `generate_mesh(domain, edge_length, **kwargs)`
- `generate_multiscale_mesh(domains, edge_lengths, **kwargs)`

Interpretation:
- this is the cleaner conceptual analogue to `meshgen`
- especially the multiscale call is close to the local L1/L2 pattern

For `OCSMesh`:
- `MeshDriver(geom, hfun, engine_name=...)`
- `driver.run()`

Interpretation:
- this is more of an engine wrapper and workflow controller than a direct `meshgen` clone
- closer to a rebuild framework than to a port of the original script

## Current Judgement

If the question is:
- "What is the closest Python-side analogue to `edgefx + meshgen`?"

Then the answer is:
- `oceanmesh`

If the question is:
- "What Python tool can we actually run right now for a new raster-driven rebuild?"

Then the answer is:
- `OCSMesh`

## Local Runtime Status

Current machine status:
- `oceanmesh`: installed and importable in `E:\AI_ENV\.venvs\oceanmesh`
- `OCSMesh`: installed and importable in `E:\AI_ENV\.venvs\ocsmesh`

This means the comparison can now move from static reading into real small-scale experiments.

## Current Recommendation

Do not treat all Python options as the same project.

Use two separate tracks:
1. `OceanMesh2D -> oceanmesh` for closest conceptual translation
2. `wide6 -> OCSMesh` for Python-native reimplementation and revalidation

And keep one hard rule:
- neither Python path replaces the baseline until it reproduces the mesh behavior and downstream stability of `wide6`
