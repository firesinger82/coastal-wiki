---
title: "adcirc mesh revalidation principles"
topic: general
canonical_source: self
citation_status: source-needed
classification: local-workflow-notes
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-mesh-revalidation-principles.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC Mesh Revalidation Principles

Date: 2026-04-13

Purpose:
- define how mesh-tool work should proceed from this point
- treat prior local attempts as evidence, not as accepted truth

## Baseline Rule

The current local baseline candidate is:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6`
- specifically the `OceanMesh2D` branch under `output/oceanmesh2d`

Reason:
- it is the only branch with a connected chain from mesh generation to ADCIRC outputs and validation artifacts

Important restriction:
- this does not mean `wide6` is accepted as physically or numerically validated
- it only means `wide6` is the strongest local candidate to start revalidation from

## Reference Rule

Use these local folders as references only:
- `E:\numerical_models\adcirc`
- older wide-domain mesh attempts
- `Gmsh` and `OCSMesh` outputs

Do not treat prior success claims as proven until they are rechecked.

## Four Mesh Tracks

### 1. Baseline Preservation

Goal:
- understand and preserve the exact ingredients that made `wide6` viable

Immediate focus:
- domain geometry inputs
- level structure
- bathymetry merge path
- boundary classification path
- post-mesh cleanup path

### 2. OceanMesh2D Translation Track

Goal:
- determine whether the current `OceanMesh2D` workflow can be translated into Python or another maintainable scripted stack

Important constraint:
- this is not allowed to replace the baseline until it reproduces the same practical outputs

What must be matched:
- domain shape
- variable-resolution behavior
- bathymetry interpolation behavior
- boundary strings
- downstream stability

### 3. Gmsh Revalidation Track

Goal:
- re-test `Gmsh` cleanly instead of inheriting prior failed assumptions

Starting assumption:
- currently negative local evidence is strong

What must be tested again:
- size-field tracking
- boundary fidelity
- element quality
- downstream ADCIRC stability

### 4. OCSMesh Revalidation Track

Goal:
- evaluate whether `OCSMesh` can reproduce the `wide6` domain with acceptable quality and repeatability

Current status:
- promising exploratory scripts exist
- no accepted production-equivalent result has been locked yet

## Decision Rule

Do not ask one question called "best mesh tool".
Ask four narrower questions:
- what is the trusted baseline now
- what parts of that baseline are essential
- can `OceanMesh2D` behavior be reproduced outside MATLAB
- can `Gmsh` or `OCSMesh` meet the same standard

## Minimum Evidence Standard

A mesh path is not promoted just because it writes `fort.14`.

It must show:
- reproducible generation inputs
- bathymetry path
- boundary construction path
- QC evidence
- at least one stable downstream ADCIRC run

## Current Working Conclusion

For now:
- preserve and document `wide6` first
- treat `wide6` as the active baseline candidate, not as settled truth
- treat `OceanMesh2D` translation, `Gmsh`, and `OCSMesh` as separate revalidation projects
