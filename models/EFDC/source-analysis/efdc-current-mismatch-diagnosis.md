---
title: "efdc current mismatch diagnosis"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc-current-mismatch-diagnosis.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# EFDC Current Mismatch Diagnosis

## Problem

Water level or tidal phase can look acceptable in EFDC while current magnitude, direction, or timing remains poor. This should be treated as a structured diagnosis problem, not as a one-parameter tuning exercise.

## Why This Matters

Current mismatch is one of the highest-value knowledge targets for this wiki because it recurs across harbor, estuary, and tidal-channel modeling. It is also easy to waste time by over-tuning friction before checking geometry, forcing, and comparison basis.

## Typical Symptom Classes

- water level amplitude and phase are acceptable, but current speed is too weak
- water level is acceptable, but current direction is biased or rotated
- flood/ebb asymmetry is wrong even though stage looks reasonable
- current timing lags or leads despite visually reasonable tide curves
- agreement looks different depending on whether speed, vector components, or depth-averaged values are compared

## First Diagnostic Axes

### 1. Comparison Basis

Check whether the observation-model comparison is fair.
- Are both values depth-averaged?
- Are both referenced to the same datum and coordinate frame?
- Are vectors being compared as speed-only, direction-only, or full components?
- Is the observation point representative of the model cell?
- Does temporal averaging or interpolation hide phase error?

### 2. Geometry And Bathymetry

Stage can be comparatively robust while current is highly sensitive to local conveyance.
- cross-sectional area errors
- channel alignment or thalweg misplacement
- over-smoothed bathymetry
- unresolved constrictions or harbor entrances
- poor wet/dry representation in tidal flats and narrow channels

### 3. Boundary And Forcing Interpretation

A visually good tide boundary does not guarantee correct current forcing.
- wrong boundary segmentation
- incomplete river or freshwater inflow
- wind omitted when currents are wind-sensitive
- density effects ignored where stratification matters
- phase or constituent setup that compensates stage while distorting flow

### 4. Friction And Mixing Parameters

Friction still matters, but it should be tuned after the comparison basis and geometry checks.
- bottom roughness zoning too uniform
- drag calibrated for stage but not for momentum distribution
- horizontal viscosity too diffusive
- vertical mixing assumptions inconsistent with the site

### 5. Wetting/Drying Logic

In shallow estuary and harbor settings, current mismatch can be downstream of wet/dry behavior.
- thresholds too aggressive or too permissive
- tidal-flat activation pattern unrealistic
- disconnected shallow pathways altering momentum exchange

## Working Rule

If stage is good but currents are bad, first suspect comparison basis, geometry, and forcing interpretation before aggressive friction tuning.

## Candidate Evidence To Add Later

- local EFDC calibration notes
- harbor or estuary case studies close to the active domain
- repeated current-mismatch experiments recorded under `experiments/`
- future failure pattern and playbook notes promoted from those experiments

## Likely Follow-On Notes

- [[efdc-parameter-glossary-v1]]
- [[efdc-calibration-foundation]]
- [[efdc-boundary-condition-foundation]]
- future `knowledge/failure-patterns/efdc-water-level-good-current-bad.md`
- future `knowledge/playbooks/efdc-tidal-calibration-order.md`
