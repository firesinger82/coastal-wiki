---
title: "efdc parameter glossary v1"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc-parameter-glossary-v1.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# EFDC Parameter Glossary V1

Date: 2026-04-30

This is a first-pass glossary for EFDC work in this wiki.

Important scope note:
- this note is intentionally calibration-oriented
- it mixes two levels of confidence:
  - **manual-backed groups** confirmed through the local EFDC+ manual RAG
  - **working labels / practical buckets** used to organize future local experiments
- the current retrieved manual evidence confirms broad control areas more clearly than exact variable names

## Source Basis

Manual-backed from local EFDC+ RAG:
- EFDC+ requires control/configuration style inputs for model setup
- hydrodynamics depends on governing equations, vertical layering, density effects, and external forcing options
- harmonic forcing and open-boundary treatment are part of the hydrodynamic setup foundation

Local RAG sources referenced during drafting:
- `EFDC_Theory_Document_Ver_12`
- `EFDC_Implementation_Guide`
- EFDC+ KB pages under the indexed Confluence spaces

## Why This Glossary Exists

- to stabilize EFDC vocabulary before more source notes and experiments accumulate
- to separate clearly manual-backed setup groups from local diagnostic shorthand
- to support future calibration notes, failure patterns, and playbooks

## Manual-Backed Setup Groups

### 1. Hydrodynamics Core

This is the main solver layer for stage, velocity, and circulation behavior.

Track this group when discussing:
- water level
- current magnitude and direction
- stage-current phase relationship
- basic circulation response

### 2. Vertical Layering

The EFDC+ theory material explicitly treats vertical layering as part of the hydrodynamic formulation.

Why it matters:
- influences how momentum and density structure are represented
- can affect whether a depth-averaged interpretation is enough for the site
- becomes more important when current mismatch may reflect vertical structure rather than only plan-view forcing

### 3. Density Effects

The manual-backed theory description explicitly includes density effects tied to temperature and salinity.

Why it matters:
- if density-driven circulation matters locally, stage can appear reasonable while currents remain biased
- density omission may be acceptable in some simplified tidal studies, but should be an explicit decision

### 4. External Forcing

The theory material explicitly notes external forcing options, including wave-related coupling context.

Track this group when discussing:
- tidal forcing
- wind forcing
- wave-related influences where relevant
- near-field discharge or external source/sink effects

### 5. Harmonic / Boundary Forcing

The retrieved manual evidence explicitly confirms harmonic forcing as part of EFDC+ hydrodynamic setup.

Track this group when discussing:
- tidal constituents
- phase and amplitude consistency
- open-boundary forcing interpretation
- time-series versus harmonic boundary specification

## Practical Calibration Buckets For This Wiki

These are the working parameter buckets that future experiments should log, even when exact EFDC+ variable names still need source-note confirmation.

### A. Bottom Roughness / Friction

Use this bucket for:
- bottom drag choices
- roughness zoning
- friction coefficients used for tidal-current calibration

Why this bucket matters:
- current mismatch is often blamed on friction too early
- this should be logged carefully, but usually checked after comparison basis, geometry, and forcing sanity

### B. Horizontal Mixing / Viscosity / Diffusivity

Use this bucket for:
- momentum diffusion settings
- lateral smoothing or over-diffusion concerns
- constituent-transport mixing settings when they materially interact with flow interpretation

Why this bucket matters:
- excessive mixing can damp current structure while leaving stage less obviously wrong

### C. Wetting / Drying Controls

Use this bucket for:
- cell activation/deactivation logic in shallow tidal flats, harbor margins, and estuarine shoals
- thresholds that alter shallow exchange pathways

Why this bucket matters:
- wet/dry behavior can change effective conveyance and distort currents even when water level looks acceptable

### D. Boundary Condition Settings

Use this bucket for:
- tidal constituent or stage boundary specification
- inflow/outflow treatment
- river boundary assumptions
- phase, amplitude, and segmentation choices

Why this bucket matters:
- stage can be compensated visually while momentum forcing is still wrong

### E. Time Step / Stability Controls

Use this bucket for:
- time step choices
- solver stability behavior
- oscillation, noise, or nonphysical current signals

Important note:
- the current retrieved passages did not provide a detailed manual-backed time-step parameter list, so exact names still need targeted source-note extraction

## Observation And Diagnostic Terms To Track Early

Future EFDC experiment cards should log:
- whether water level agreement is judged by amplitude, phase, or both
- whether current agreement is judged by speed, direction, vector components, or depth-averaged values
- whether station-versus-cell representativeness is questionable
- whether vertical structure is ignored or simplified

## Current Cautions

### Clearly manual-backed
- EFDC+ hydrodynamic setup depends on hydrodynamics, vertical layering, density effects, and forcing structure
- harmonic forcing is part of the hydrodynamic setup foundation

### Not yet exact-name confirmed from current retrieval
- precise friction parameter names
- precise horizontal viscosity / diffusivity field names
- exact wetting-drying control names
- exact timestep/stability parameter names

These should be promoted from "working bucket" to exact glossary entries only after targeted source-note extraction from the manuals/KB.

## Next Expansion Candidates

- exact EFDC file and control-name mapping from the implementation guide
- first-pass boundary-condition vocabulary for tidal/coastal cases
- first-pass wetting/drying term list
- friction and mixing terms tied to local calibration experiments
