---
title: "adcirc preprocessing foundation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC 공식 문서(adcirc.github.io / adcirc.org) 기반 전처리 레이어 정리. file 의미·NWS·전처리 도구 생태계는 공식 docs 근거. (2026-06-18 canonical 정화: 개인 프로젝트 내용 — wide6·JMA-MSM 로컬 분기·E:\\ 경로·local-workflow 링크 — 제거. 개인 ADCIRC 운영 자료는 experience/ 레이어.)"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 마이그레이션 2026-05-23 → 2026-06-18 정화 (Opus 4.8)"
note_date: 2026-04~05 (original) / 2026-05-23 (promote) / 2026-06-18 (purify)
verification_by: "공식 ADCIRC 문서 cross-ref"
verification_date: 2026-06-18
---

# ADCIRC Preprocessing Foundation

Purpose:
- define the preprocessing layer that must be stabilized before serious ADCIRC project work
- separate mesh generation, bathymetry construction, and forcing ingestion from later parameter tuning

This note is a foundation note, not a run recipe.

## Why This Comes First

The hardest early failure modes in ADCIRC work usually do not start in `DT` or `TAU0`.
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
- 공식 메시 생성 도구는 아래 "What The Official Tooling Map Implies" 참조 (SMS / OceanMesh2D / SubgridADCIRCUtility).

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
- meteorological forcing through `fort.22` or related files (NWS 모드별)

Primary note:
- met forcing 메커닉 → `[[adcirc-met-forcing-implementation]]`

## What The Official Tooling Map Implies

The docs do not present one single universal preprocessor. Instead they expose an ecosystem:
- `SMS` as a broad GUI-based commercial environment
- `OceanMesh2D` as an open MATLAB-based end-to-end mesh-generation path
- `SubgridADCIRCUtility` as a specialized terrain/subgrid enhancement path
- `MetGet` as a meteorological forcing acquisition and development system
- `f13builder` and related utility programs for nodal attributes

This implies that tool choice is itself part of the project design, not a minor implementation detail.

## Next Notes To Keep Linked

- `adcirc-bathymetry-input-foundation.md`
- met forcing → `[[adcirc-met-forcing-implementation]]`
