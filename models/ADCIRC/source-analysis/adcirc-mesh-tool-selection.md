---
title: "adcirc mesh tool selection"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-mesh-tool-selection.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC Mesh Tool Selection

Date: 2026-04-13

Purpose:
- reduce confusion around the tool choice for building `fort.14`
- reflect the actual local evidence, not just the official tool list

## Why This Note Changed

The earlier framing was too generic.
The current local problem is not just:
- `SMS` versus `OceanMesh2D`

It is:
- one local branch called `wide6` has real downstream evidence
- `Gmsh` and `OCSMesh` also exist locally
- prior attempts outside the tuned branch are not trusted yet

## Official Tool Families Still Matter

From the official ADCIRC ecosystem, the relevant families still include:
- `SMS`
- `OceanMesh2D`
- `VEW Utils`
- `SubgridADCIRCUtility`
- helper tools such as `f13builder`

But official availability is only one layer.
Local trust now matters more.

## Current Local Ranking

### Active Baseline

- `OceanMesh2D`

Reason:
- the `wide6` branch uses it
- the same branch contains `fort.14`, `fort.13`, `fort.15`, run outputs, and validation outputs
- this is the strongest local evidence chain currently available

### Revalidation Candidates

- `Gmsh`
- `OCSMesh`

Reason:
- both have meaningful local artifacts and scripts
- neither is yet the accepted local production-equivalent path

### Secondary Helper Tools

- `SubgridADCIRCUtility`
- `VEW Utils`
- `f13builder`
- local interpolation and grid helper programs under `tools\\utilities\\grid`

These should stay in supporting roles until the base mesh path is settled.

Local FORTRAN helper interpretation:
- `bath_interp.f` and `interp.f` are field-transfer tools, not mesh generators
- `DEM2GRDv3.F90` is a DEM-to-grid helper, not a base mesher
- `MeshChecker05.F90` and `max_elev_grad_chk.f` are QC tools
- `bnd_extr.f` is boundary-extraction support
- `Griddata_v1.32.F90` and `Gridscope_ver1.22.f90` are currently broken local artifacts, not usable source

## What The Local wide6 Evidence Changes

The local evidence now says:
- `OceanMesh2D` is not just a documented option
- it is the only currently trusted mesh-generation baseline

The local evidence also says:
- `Gmsh` has already been tried seriously
- the local work log records repeated failure modes
- `OCSMesh` exists as a promising reconstruction path, but not yet as the chosen baseline

## Tool-Specific Interpretation

### OceanMesh2D

Local status:
- baseline

Why:
- full scripted mesh workflow exists
- bathymetry merge is wired in
- boundary generation is part of the path
- downstream ADCIRC execution evidence exists

Current limitation:
- MATLAB dependence
- some behavior may be hard to port exactly

### Gmsh

Local status:
- failed branch that still deserves controlled revalidation

Why it is not rejected forever:
- Python stack is attractive
- size-field experimentation exists
- the failure may be in the current workflow design, not only the engine

Why it is not trusted now:
- the tuned branch did not end there
- the local log explicitly records poor marine-mesh behavior

### OCSMesh

Local status:
- exploratory candidate

Why it matters:
- closer to a modern Pythonic coastal-mesh workflow than raw `Gmsh`
- local scripts already try to rebuild the wide-domain basin from verified inputs

Why it is not baseline yet:
- no accepted production-equivalent branch is locked
- current evidence is still at the reimplementation stage

### SMS

Local status:
- still relevant in the ADCIRC ecosystem
- not the current local active branch

Interpretation:
- keep it in the landscape
- do not make it the default just because it is widely used

## Current Decision Rule

Do not ask:
- which tool is best in general

Ask instead:
- which tool is the trusted local baseline now
- which tool is the best candidate for translation away from MATLAB
- which tool deserves clean revalidation

Current answers:
- trusted baseline now: `OceanMesh2D` via `wide6`
- translation target to investigate: `OceanMesh2D` behavior into Python or another scripted stack
- clean revalidation candidates: `Gmsh`, `OCSMesh`

FORTRAN utility role:
- helper layer only
- useful for interpolation, QC, and boundary support
- not a replacement for the baseline mesh path

## Immediate Working Policy

1. Preserve and document the `wide6` `OceanMesh2D` path first.
2. Treat `Gmsh` and `OCSMesh` as separate revalidation tracks.
3. Do not promote any alternative path until it shows:
   - reproducible inputs
   - mesh QC
   - bathymetry path
   - boundary path
   - at least one stable downstream ADCIRC run
