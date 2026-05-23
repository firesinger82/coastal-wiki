---
title: "adcirc bathymetry input foundation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-bathymetry-input-foundation.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC Bathymetry Input Foundation

Date: 2026-04-12

Purpose:
- organize how bathymetry and topography enter ADCIRC
- distinguish base-mesh depth construction from advanced terrain options

## Core Official Fact

The official docs define `fort.14` as the file that contains:
- the finite element grid
- bathymetric data
- boundary information

That means bathymetry is not a side input.
It is part of the core mesh artifact.

## First Principle

Before discussing parameter tuning, you need a coherent answer to:
- what terrain sources define the bed and land elevations?
- what datum are they in?
- how are they transferred into `DP` at each node in `fort.14`?

If this is unstable, later stability or validation work is built on weak ground.

## Bathymetry Input Layers

### 1. Base Bathymetry In The Mesh

This is the default layer:
- node coordinates and `DP` values are stored in `fort.14`
- initial water depths are derived from the bathymetric depth in `fort.14`

This is the foundation for almost all standard ADCIRC runs.

### 2. Nodal Attributes

Bathymetry-adjacent behavior can also be influenced by nodal attributes in `fort.13`.
Examples include:
- Manning's n
- sea-surface-height related attributes
- initially dry behavior or roughness-related fields

These are not replacements for the base bed elevation, but they often interact with how the terrain behaves dynamically.

### 3. Time-Varying Bathymetry

ADCIRC also supports `fort.141` for time-varying bathymetry.
The docs describe:
- full-domain updates when `NDDT = +/-1`
- limited-area updates when `NDDT = +/-2`

This is an advanced path.
It should not be treated as the default first way to represent terrain changes.

### 4. Subgrid Terrain Representation

The official tools page surfaces `SubgridADCIRCUtility`, which is for creating subgrid input files.

This suggests an important distinction:
- one path improves the base mesh directly
- another path keeps a manageable mesh while representing finer terrain information through subgrid methods

## What The Official Tooling Implies

The official docs indicate:
- `OceanMesh2D` can interpolate bathymetry and topography and work with DEMs
- `SubgridADCIRCUtility` exists for high-resolution terrain and landcover representation without requiring extremely fine mesh resolution

Observed local evidence:
- the bundled `OceanMesh2D` setup in `E:\ADCIRC_essential` explicitly references:
  - `GSHHS` shoreline
  - `SRTM15+` bathymetry
  - optional `GEBCO`
- `E:\numerical_models\adcirc\tools\utilities\grid` contains bathymetry and grid helper programs such as:
  - `bath_interp.f`
  - `interp.f`
  - `Griddata_v1.32.F90`
  - `Gridscope_ver1.22.f90`

So bathymetry work is not just "find a DEM and assign depths."
It is a pipeline decision:
- direct interpolation into the mesh
- plus optional nodal attributes
- plus optional subgrid enrichment

## What Must Be Controlled

At minimum, the bathymetry workflow must control:
- source datasets
- shoreline and land-water masking
- vertical datum consistency
- interpolation method
- dry land treatment
- relationship between base topography and nodal attributes

## What We Should Record For Every Bathymetry Workflow

- source dataset names
- horizontal resolution
- vertical datum
- date or vintage
- interpolation method into mesh nodes
- land cutoff or shoreline treatment
- any smoothing or editing applied
- whether subgrid processing was used

## What The Docs Do Not Give Us Directly

The official docs are strong on file semantics, but thinner on field-ready bathymetry assembly recipes.

Missing or weakly specified areas include:
- preferred bathymetry source combinations by problem type
- recommended datum harmonization workflow
- practical QC rules for coastal DEM plus bathymetry merging
- a canonical "good enough first bathymetry pipeline" for new users
- which of the local `grid` utilities are still active versus archival

These should be tracked as local knowledge gaps, not filled with guesses.

## Current Working Rule

For now, keep the bathymetry branch in this order:
1. define source datasets
2. define datum policy
3. define mesh interpolation path
4. decide whether subgrid is needed
5. only then consider advanced terrain features like `fort.141`
