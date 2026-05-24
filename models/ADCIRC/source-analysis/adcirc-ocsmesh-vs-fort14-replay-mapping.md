---
title: "adcirc ocsmesh vs fort14 replay mapping"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-ocsmesh-vs-fort14-replay-mapping.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC OCSMesh vs fort.14 Replay Mapping

Date: 2026-04-13

Purpose:
- map `OCSMesh` against the `wide6 fort.14 replay recipe`
- answer a narrow question:
  - how far can `OCSMesh` replace `domain -> sizing -> mesh -> pre-boundary-correction fort.14 candidate`?

Reference recipe:
- `E:\AI_ENV\modeling-wiki\knowledge\methods\adcirc-wide6-fort14-replay-recipe.md`

Reference local OCSMesh work:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\ocsmesh_test\scripts\make_basin_mesh.py`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\ocsmesh_test\scripts\step3_ocsmesh_basin.py`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\ocsmesh_test\scripts\step3_ocsmesh_basin_jigsaw.py`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\ocsmesh_test\scripts\make_basin_whole.py`

## Short Answer

`OCSMesh` can plausibly cover:
- domain ingestion
- raster-based sizing
- mesh generation
- pre-boundary-correction ADCIRC-compatible mesh output

`OCSMesh` does **not** currently close:
- 1:1 reproduction of OceanMesh2D `edgefx(fs=3)` behavior
- original `wide6` domain-construction logic from `mainland.shp + ocean_new_w6.shp`
- trustworthy replacement of the manual boundary-correction stage

So the right interpretation is:
- `OCSMesh` can replace most of Stage 2
- it can partially replace Stage 1 if given an already curated domain polygon
- it cannot yet replace Stage 3 and Stage 4 with confidence

## Stage Mapping

| Replay stage | `wide6` recipe meaning | `OCSMesh` coverage | Current judgement | Evidence |
| --- | --- | --- | --- | --- |
| Stage 1. Domain preparation | prepare `mainland.shp` + `ocean_new_w6.shp` and the curated domain geometry | partial | `PARTIAL` | local OCSMesh scripts usually start from `wide6_domain.shp` extracted from an existing mesh, not from the original raw shape-building workflow |
| Stage 2. Mesh generation | build multiscale size field, generate initial mesh, write first `fort.14` candidate | strong but not 1:1 | `STRONG PARTIAL` | `Geom`, `Hfun`, `MeshDriver`, `jigsawpy` path, local `ocsmesh_test` outputs |
| Stage 3. Boundary review | decide if auto boundary is acceptable | weak | `WEAK` | `mesh.boundaries.auto_generate(...)` exists, but local `wide6` history already shows boundary auto logic is not trusted |
| Stage 4. Boundary correction | manually or semi-manually rewrite final boundary strings | not closed | `NOT CLOSED` | no retained OCSMesh workflow matches `classify_boundaries.py` quality for final acceptance |
| Stage 5. Retained fort.14 acceptance check | compare to retained counts and topology | possible | `POSSIBLE` | OCSMesh can write `.grd`/`.2dm`; comparison can be scripted |

## What `OCSMesh` Can Replace Well

### 1. Raster ingestion and CRS discipline

`OCSMesh` is strong here.

Evidence:
- `Raster(path, crs=...)`
- local `step3_ocsmesh_basin.py` and `make_basin_mesh.py` already load `GEBCO` and `BADA`
- local runtime showed OCSMesh forces CRS awareness rather than silently assuming one

Meaning for `wide6`:
- the GEBCO/BADA side of the replay path is a good fit for `OCSMesh`

### 2. Domain polygon as an already curated shape

`OCSMesh` can handle a finished domain polygon well.

Evidence:
- `Geom(..., base_shape=...)`
- local scripts use `wide6_domain.shp`
- local scripts clip subdomains against a retained domain polygon

Meaning for `wide6`:
- if Stage 1 is treated as "current retained domain is accepted", then `OCSMesh` can start from there

Limitation:
- this does not reconstruct the original design logic of `mainland.shp + ocean_new_w6.shp`
- it only consumes the result

### 3. Pre-boundary-correction mesh generation

`OCSMesh` can clearly generate an initial ADCIRC-style mesh candidate.

Evidence:
- `MeshDriver(geom, hfun, engine_name='gmsh')`
- local scripts write `.grd` and `.2dm`
- `step3_ocsmesh_basin.py` and `step3_ocsmesh_basin_jigsaw.py` explicitly save raw/interpolated meshes before boundary generation
- local `make_basin_whole.py` writes a `grd`-style mesh after geometry and hfun construction

Meaning for `wide6`:
- this is the strongest place to compare `OCSMesh` against the `fort.14` replay recipe

## What `OCSMesh` Only Partially Replaces

### 1. `edgefx(fs=3)` sizing semantics

This is only a conceptual replacement, not a literal one.

OceanMesh2D recipe uses:
- nested `edgefx(fs=3, max_el, g)`

OCSMesh uses:
- `Hfun(...)`
- `add_subtidal_flow_limiter(...)`
- `add_contour(...)`
- optionally `add_feature(...)`, `add_channel(...)`

Meaning:
- `OCSMesh` can produce a serious size field
- but it does not reproduce the OceanMesh2D sizing worldview 1:1
- matching behavior will require calibration, not translation

### 2. Multilevel nest logic

OceanMesh2D recipe is explicitly:
- Level 1 wide domain
- Level 2 Korea coast refinement

Current local OCSMesh attempts are different:
- `make_basin_mesh.py` uses 4 spatial subdomains plus merge
- `make_basin_whole.py` uses a single polygon plus a raster-derived size table
- `step3_ocsmesh_basin.py` uses contour and flow-limiter constraints

Meaning:
- `OCSMesh` can replace the function of multiscale generation
- but not the exact retained two-level logic without deliberate redesign

## What `OCSMesh` Does Not Yet Replace

### 1. Original domain-construction provenance

The original recipe includes:
- manual offshore boundary design
- interpretation of `mainland.shp`
- interpretation of `ocean_new_w6.shp`

Current local OCSMesh practice usually starts from:
- `wide6_domain.shp` extracted from an already existing mesh

This means:
- `OCSMesh` does not currently replace the earliest domain-design stage
- it starts after that stage has already been solved

### 2. Final boundary correction

This is the biggest non-closure.

Local `wide6` evidence says:
- OceanMesh2D auto boundary classification failed
- manual GUI correction was required

OCSMesh offers:
- `mesh.boundaries.auto_generate(...)`

But current evidence does not justify trusting it as a replacement for the retained manual boundary workflow.

So:
- `OCSMesh` can produce a pre-boundary-correction mesh candidate
- it cannot yet produce the final accepted `fort.14` boundary state without extra review logic

## Best Current Mapping

The most defensible mapping is:

### `OCSMesh` can be fairly compared at this cut line

Accepted comparison target:
- `domain accepted`
- `sizing applied`
- `mesh generated`
- `bathymetry interpolated`
- **before** final manual boundary correction

This is the fair boundary for evaluation because:
- it avoids pretending that `OCSMesh` already solves the manual boundary problem
- it still tests the most important Python-side replacement question

### `OCSMesh` should not yet be asked to match this cut line

Do **not** require it yet to match:
- the final retained 70-node open boundary
- the exact land-boundary segmentation count of `2189`
- the exact final manual corrections embedded in the current retained `fort.14`

Those belong to the boundary-correction problem, not to the meshing-core comparison

## Local Script Mapping

### Closest local `OCSMesh` analogue to Stage 2

Best candidates:
- `step3_ocsmesh_basin.py`
- `step3_ocsmesh_basin_jigsaw.py`

Why:
- they explicitly use `Geom + Hfun`
- they save raw/interpolated meshes
- they separate DEM interpolation and boundary generation
- they are closer to the replay-recipe cut line than the older merged-basin experiments

### Less suitable as direct replay analogues

- `make_basin_mesh.py`
  - uses 4 subdomains and merge
  - changes the topology problem too much
- `make_basin_whole.py`
  - bypasses OCSMesh engine logic and goes more directly through `jigsawpy`
  - useful for meshing quality experiments, less clean as an `OCSMesh` replacement answer

## Decision

For current work, `OCSMesh` should be judged as follows:

1. Can it consume a curated `wide6` domain polygon?
   - yes
2. Can it build a serious basin-scale size field from `GEBCO + BADA`?
   - yes
3. Can it generate an ADCIRC-compatible pre-boundary mesh candidate?
   - yes
4. Can it replace the retained manual boundary-correction stage today?
   - not yet
5. Can it therefore replace the whole `fort.14 replay recipe` end to end today?
   - not yet

## Practical Recommendation

Before comparing final boundary strings, use this test target:
- `OCSMesh` must first match the **pre-boundary-correction** mesh behavior

That means the next fair experiment is:
- same accepted domain polygon
- same DEM families
- comparable target size ranges
- generate an `OCSMesh` mesh
- compare node/element scale, bathymetry range, and broad geometry
- postpone final open-boundary equivalence until boundary correction is treated as a separate problem
