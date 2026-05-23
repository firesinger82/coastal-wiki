---
title: "adcirc wide6 validation principles"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-wide6-validation-principles.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC wide6 Validation Principles

Date: 2026-04-13

Purpose:
- define what it would mean for `wide6` to be accepted
- separate "mesh exists" from "mesh is trustworthy"
- stop treating the current `wide6` branch as implicitly validated

Target:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6`

## Current Status

`wide6` is not yet a validated mesh.

At most, it is:
- the strongest local baseline candidate
- the only branch with a relatively complete artifact chain
- a practical starting point for revalidation

That is weaker than:
- numerically validated
- physically validated
- operationally reproducible

## What Does Not Count As Validation

These are not enough by themselves:
- `fort.14` was written successfully
- the mesh looks reasonable in a plot
- one branch ran further than older failed branches
- local tuning reduced obvious errors
- one downstream run completed

## Minimum Validation Gates

`wide6` should only be treated as accepted after all of these are checked.

### 1. Reproducibility Gate

We must be able to identify:
- exact shoreline inputs
- exact DEM inputs
- exact manual geometry edits
- exact bathymetry merge and override steps
- exact smoothing and cleanup steps
- exact boundary tagging process

If these cannot be replayed, `wide6` is not reproducible.

### 2. Geometry Gate

We must verify:
- offshore boundary shape is intentional rather than accidental
- coastline retention is acceptable in key Korean coastal zones
- island retention and removal rules are explainable
- open boundary is continuous and topologically clean

If geometry rules are not reviewable, later success is fragile.

### 3. Bathymetry Gate

We must verify:
- `GEBCO + BADA2024` merge rule is explicit
- datum assumptions are known
- minimum-depth forcing is documented
- slope limiting and smoothing are documented
- no obvious artificial pits, steps, or spikes remain in critical areas

### 4. Mesh Quality Gate

We must verify:
- no unacceptable degenerate elements remain
- minimum angle and aspect-ratio checks are archived
- problematic local clusters are identified
- boundary-adjacent element quality is acceptable

### 5. Boundary Gate

We must verify:
- open boundary nodes are correctly classified
- land boundaries are not leaking
- auto-classification failures and manual corrections are archived
- resulting boundary strings are consistent with ADCIRC expectations

### 6. Downstream ADCIRC Gate

We must verify at least one controlled run for:
- startup stability
- no obvious exploding water levels or velocities
- no immediate instability attributable to mesh or bathymetry defects
- outputs that are at least internally consistent

### 7. Physical Plausibility Gate

For a real forcing case, we must verify:
- large-scale water-level behavior is not obviously nonphysical
- known coastal response patterns are not grossly wrong
- results are not only numerically stable but physically believable

## Working Rule

Until these gates are checked, use this wording:
- "`wide6` is the current baseline candidate"

Do not use this wording yet:
- "`wide6` is validated"
- "`wide6` is the correct mesh"
- "`wide6` is production-ready"

## Immediate Next Questions

The next useful checks are:
- can the `wide6` generation recipe actually be replayed
- what exact manual interventions were required
- which QC evidence already exists in the folder and which is still missing

## Decision

For now:
- preserve `wide6`
- do not trust `wide6` blindly
- validate `wide6` before asking Python tools to match it
