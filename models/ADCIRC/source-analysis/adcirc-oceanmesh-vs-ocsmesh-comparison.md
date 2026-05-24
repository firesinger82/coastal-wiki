---
title: "adcirc oceanmesh vs ocsmesh comparison"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-oceanmesh-vs-ocsmesh-comparison.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC oceanmesh vs OCSMesh Comparison

Date: 2026-04-13

Purpose:
- compare `oceanmesh` and `OCSMesh` against the local `wide6` baseline
- focus on the real translation targets from `make_mesh_om2d.m`
- separate "closest to OceanMesh2D" from "most usable Python rebuild path"

Primary local baseline:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\scripts\make_mesh_om2d.m`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\WORK_LOG.md`

Installed local runtimes:
- `oceanmesh` in `E:\AI_ENV\.venvs\oceanmesh`
- `OCSMesh` in `E:\AI_ENV\.venvs\ocsmesh`

## Reference View Of The `wide6` Workflow

The local `wide6` OceanMesh2D script does these main jobs:
- assemble domain boundary from `mainland.shp` plus `ocean_new_w6.shp`
- build two nested geodata levels from shoreline plus DEM
- create two sizing functions with `edgefx(fs=3, max_el, g)`
- run multilevel mesh generation through `meshgen(...).build`
- interpolate GEBCO bathymetry
- override Korean nodes with `BADA2024.nc`
- attempt automatic boundary classification
- write `fort.14`

Important local warning:
- the viable `wide6` branch was not pure script automation
- local evidence says it also required manual offshore boundary design, manual open-boundary decisions, smoothing, and cleanup

## High-Level Result

Short answer:
- `oceanmesh` is closer to `OceanMesh2D`
- `OCSMesh` is stronger as a Python-native rebuild framework

Operational answer:
- use `oceanmesh` when the question is "what is the nearest Python analogue to `edgefx + meshgen`?"
- use `OCSMesh` when the question is "what Python stack is more structured for raster-driven reimplementation and repeated experiments?"

## Side-By-Side Comparison

| Topic | `oceanmesh` | `OCSMesh` | Judgement vs `wide6` |
| --- | --- | --- | --- |
| Core mental model | shoreline + sizing grid + direct mesh generation | geometry factory + size-function factory + engine driver | `oceanmesh` is closer |
| Domain input | `Shoreline(shp, bbox, h0, ...)` directly takes shoreline vectors | `Geom(...)` can be built from raster, mesh, shapely polygons, or collections | `oceanmesh` matches `make_mesh_om2d.m` more directly |
| Size function style | explicit shoreline-oriented functions like `feature_sizing_function`, `distance_sizing_function`, `multiscale_sizing_function` | composable `Hfun` constraints like `add_contour`, `add_channel`, `add_feature`, `add_subtidal_flow_limiter` | `oceanmesh` is closer to `edgefx`, `OCSMesh` is more modular |
| Multiscale nesting | direct `generate_multiscale_mesh(domains, edge_lengths, ...)` | no single direct analogue; nesting is expressed through `Geom/Hfun` plus engine run | `oceanmesh` is closer |
| Bathymetry-driven refinement | `bathymetric_gradient_sizing_function`, `wavelength_sizing_function` | strong raster-side constraints and topo-derived controls | `OCSMesh` is stronger here |
| DEM handling | available, but shoreline-first worldview dominates | raster is first-class; `Raster(..., crs=...)` then `Geom/Hfun` | `OCSMesh` is stronger here |
| CRS behavior | explicit CRS handling but caller must wire consistent inputs | strict enough that missing raster CRS fails immediately; driver auto-projects geographic inputs to UTM for generation | `OCSMesh` is stricter and safer |
| Mesh engine | package-native mesh generation functions | `MeshDriver(..., engine_name='gmsh')` abstraction | `oceanmesh` feels closer to `meshgen`, `OCSMesh` feels closer to workflow orchestration |
| Output | direct `write_to_fort14(...)` exists | `Mesh.write(..., format='grd' or '2dm')` exists; fort.14 route is indirect through `grd` | `oceanmesh` is simpler for ADCIRC output |
| Windows install difficulty | high due CGAL, GMP, MPFR, vcpkg linkage | lower; installed cleanly in UV env | `OCSMesh` is easier operationally |
| Boundary classification | no direct drop-in replacement for `make_bc(..., 'auto', ...)` found | no direct ADCIRC boundary classifier found either | neither solves this gap |
| Fit for `wide6` port | best candidate for closest translation | better for fresh redesign than close translation | split-track approach is appropriate |

## What Maps Best From `make_mesh_om2d.m`

### Best `oceanmesh` matches

These map well to the OceanMesh2D worldview:
- `Shoreline(...)`
- `feature_sizing_function(...)`
- `distance_sizing_function(...)`
- `multiscale_sizing_function(...)`
- `enforce_mesh_gradation(...)`
- `generate_mesh(...)`
- `generate_multiscale_mesh(...)`
- `write_to_fort14(...)`

Interpretation:
- `edgefx(fs=3)` is not one function here
- the closest practical substitute is "shoreline feature sizing + distance sizing + gradation enforcement"
- `meshgen(...).build` is conceptually closest to `generate_multiscale_mesh(...)`

### Best `OCSMesh` matches

These map well to a Python-native rebuild:
- `Raster(path, crs=...)`
- `Geom(...)`
- `Hfun(...)`
- `Hfun.add_feature(...)`
- `Hfun.add_contour(...)`
- `Hfun.add_channel(...)`
- `Hfun.add_subtidal_flow_limiter(...)`
- `MeshDriver(...).run()`
- `Mesh.write(..., format='grd' or '2dm')`

Interpretation:
- `OCSMesh` does not feel like a direct `edgefx` clone
- it expresses refinement as constraint composition on a raster-backed size field
- this is powerful for research iteration, but less 1:1 with the MATLAB script

## Important Concrete Findings From Local Runtime

### `oceanmesh`

Confirmed locally:
- import works in `E:\AI_ENV\.venvs\oceanmesh`
- Windows install needed CGAL/GMP/MPFR wiring through local vcpkg
- direct `fort.14` writer exists
- shoreline-first APIs are exposed and readable

Implication:
- this is the best candidate if the target is "reproduce the shape of `wide6` in Python"

### `OCSMesh`

Confirmed locally:
- import works in `E:\AI_ENV\.venvs\ocsmesh`
- `Raster` fails if CRS is missing from DEM and caller does not provide one
- `HfunRaster` exposes contour/channel/feature/subtidal constraints
- `MeshDriver` auto-projects geographic geometry to UTM before generation
- `Mesh.write` supports `grd` and `2dm`

Implication:
- this is the best candidate if the target is "build a controlled Python meshing workflow with explicit raster and CRS discipline"

## Where Neither Package Closes The Real Gap

The hardest local problems are still outside a simple package swap:
- offshore boundary shape design
- open-boundary tagging that is trustworthy for ADCIRC
- post-interpolation slope limiting and smoothing policy
- mesh cleanup and downstream stability revalidation

So package choice alone will not reproduce `wide6`.

## Decision

For current strategy:
1. keep `wide6 + OceanMesh2D` as the baseline
2. treat `oceanmesh` as the closest-translation track
3. treat `OCSMesh` as the structured-rebuild track
4. do not promote either path until one of them reproduces the local boundary, bathymetry, and downstream ADCIRC behavior well enough

## Practical Recommendation

If only one Python path is explored first:
- choose `oceanmesh` if the immediate question is exact replacement pressure on `make_mesh_om2d.m`
- choose `OCSMesh` if the immediate question is repeatable experimentation, raster constraints, and cleaner workflow control

Given the current local evidence, the better split is:
- short-term translation study: `oceanmesh`
- medium-term operational rebuild: `OCSMesh`
