---
title: "efdc calibration foundation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc-calibration-foundation.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# EFDC Calibration Foundation

Date: 2026-04-30

This note defines the current working calibration order for EFDC in coastal and estuarine problems.

Important scope note:
- the local EFDC+ manual RAG clearly supports the importance of hydrodynamics, vertical layering, density effects, and harmonic/external forcing
- however, the exact step-by-step calibration order below is a **practical operating synthesis** for this wiki, not a claim that the manual gives this sequence word-for-word
- manual-backed points and working practice are separated below

## Core Principle

If water level is already reasonable but currents are mismatched, do not jump straight to friction tuning.

Treat the problem in this order:
1. comparison basis
2. geometry and bathymetry
3. boundary and forcing interpretation
4. wetting/drying behavior
5. friction
6. mixing / viscosity and secondary physics

## Manual-Backed Foundation

The local EFDC+ manual RAG supports these base facts:
- EFDC+ should be built in stages, with hydrodynamics established before more complex coupled behavior is trusted
- hydrodynamic behavior depends on vertical layering, density effects, and forcing structure
- harmonic forcing is part of the hydrodynamic setup foundation
- external forcing choices matter to the resulting flow field

These points justify treating calibration as a structured setup-and-diagnosis task rather than a single-parameter optimization task.

## Recommended Calibration Order

### Step 1. Lock The Comparison Basis

Before changing parameters, make sure the comparison itself is fair.

Check:
- are observed and modeled quantities both depth-averaged, or not?
- are you comparing full vectors, components, or speed only?
- are time stamps aligned and averaged consistently?
- is the observation point representative of the model cell or channel cross section?
- are datum and coordinate conventions consistent?

Why this is first:
- a misleading comparison basis can make a physically reasonable current field look wrong
- friction tuning on top of a bad comparison basis usually contaminates later calibration

### Step 2. Check Geometry And Bathymetry

If stage is decent but currents are wrong, local conveyance may still be wrong.

Check:
- cross-sectional area realism
- channel alignment and thalweg placement
- over-smoothed bathymetry
- unresolved constrictions, inlets, or harbor entrances
- shallow exchange pathways that matter to flow direction and magnitude

Why this is early:
- water level often tolerates geometry error better than velocity does
- current mismatches commonly reflect conveyance distortion, not just friction

### Step 3. Re-check Boundary Conditions And Forcing

Use the manual-backed forcing structure as the next calibration axis.

Check:
- harmonic constituent selection, phase, and amplitude
- open-boundary segmentation and interpretation
- freshwater inflow assumptions
- wind inclusion or omission
- density-driving inputs if stratification matters
- whether stage has been visually matched by compensating boundary choices that still distort flow

Why this comes before friction tuning:
- wrong forcing can still generate acceptable stage while pushing the wrong momentum balance through the domain

### Step 4. Inspect Wetting / Drying Behavior

In shallow tidal systems, wet/dry logic can alter effective connectivity.

Check:
- unrealistic activation/deactivation of shallow cells
- tidal-flat pathways opening or closing too aggressively
- dry-cell behavior near channel margins or harbor shoals
- whether current mismatch is concentrated in marginal shallow zones

Why this is separate:
- wet/dry problems can masquerade as friction or bathymetry problems

### Step 5. Tune Bottom Friction Carefully

Only after the previous checks are acceptable should friction be tuned aggressively.

Use friction tuning for:
- depth-averaged current magnitude bias
- flood/ebb asymmetry partly linked to momentum loss
- spatial roughness contrasts that are physically defensible

Guardrails:
- do not use friction as a patch for bad geometry
- do not use uniform friction if the domain clearly needs zoning
- always log whether stage fit improves at the expense of current realism, or vice versa

### Step 6. Tune Mixing / Secondary Physics

After the main momentum pathways are believable, adjust the second-order controls.

Check:
- excessive horizontal smoothing/diffusion
- turbulence or vertical-mixing assumptions
- density effects that were simplified too early
- wave or secondary forcing where physically relevant

Why this is later:
- these terms matter, but they are often misused to compensate for upstream setup mistakes

## Practical Rule For This Wiki

For EFDC tidal calibration, treat "water level good, current bad" primarily as a diagnosis problem, not as a friction problem.

## Minimum Logging Requirement For Future Experiments

Each EFDC experiment card should record:
- the comparison basis actually used
- the geometry/bathymetry version being trusted
- the exact forcing interpretation
- wet/dry assumptions
- friction settings
- mixing settings
- which step in the calibration order was being tested

## What This Note Should Lead To Next

Natural follow-on notes:
- `knowledge/methods/efdc-boundary-condition-foundation.md`
- `knowledge/failure-patterns/efdc-water-level-good-current-bad.md`
- `knowledge/heuristics/efdc-check-comparison-basis-before-friction-tuning.md`
- `knowledge/playbooks/efdc-tidal-calibration-order.md`
