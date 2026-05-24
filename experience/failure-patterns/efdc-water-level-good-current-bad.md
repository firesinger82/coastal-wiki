---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/failure-patterns/efdc-water-level-good-current-bad.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: experience-only
notes: P1 triage mixed default (model=EFDC; source-needed)
---
# Failure Pattern

## Pattern Name

water level good, current bad

## Symptom

The EFDC model reproduces water level amplitude and/or phase reasonably well, but current magnitude, direction, flood/ebb asymmetry, or timing remains poor.

Typical signs:
- stage curves look acceptable at tide stations
- modeled current speed is too weak or too strong at ADCP/current-meter locations
- current direction is rotated or biased even though stage looks visually convincing
- current timing lags or leads while water level timing seems acceptable
- calibration effort keeps returning to bottom friction without stable improvement

## Common Context

- solver / model: EFDC or EFDC+
- mesh / geometry: harbor, estuary, tidal channel, or shallow coastal domain
- forcing: tidal boundaries with possible river, wind, density, or wave influence
- parameter regime: partially calibrated stage response but unresolved momentum-field mismatch

## Likely Causes

1. the observation-model comparison basis is unfair or inconsistent
2. geometry or bathymetry distort local conveyance more than they distort stage
3. boundary or forcing interpretation is compensating stage while still driving the wrong momentum balance
4. wetting/drying behavior is altering shallow connectivity and exchange pathways
5. friction or mixing is wrong, but only after the upstream issues above are excluded

## Quick Triage

1. verify the comparison basis first
   - depth-averaged versus layered values
   - vector components versus speed-only
   - time alignment and averaging window
   - station representativeness versus model cell footprint
2. inspect geometry and bathymetry in the mismatch zones
   - cross-sectional area
   - constrictions, inlets, shoals, tidal flats, harbor entrances
   - over-smoothed or mislocated channels
3. re-check boundary and forcing assumptions
   - harmonic constituent phase/amplitude
   - open-boundary segmentation
   - river inflow, wind, density effects, and other omitted drivers
4. inspect wetting/drying logic before aggressive friction tuning
5. only then tune friction and mixing in a logged, hypothesis-driven way

## Supporting Evidence

- related experiments:
  - future EFDC experiment cards should be linked here once current-mismatch runs exist
- related sources:
  - `knowledge/methods/efdc.md`
  - `knowledge/methods/efdc-current-mismatch-diagnosis.md`
  - `knowledge/methods/efdc-parameter-glossary-v1.md`
  - `knowledge/methods/efdc-calibration-foundation.md`

## Common False Leads

- false lead 1: assuming good stage fit means the geometry is already good enough
- false lead 2: treating bottom friction as the first lever instead of the later lever
- false lead 3: comparing observed vectors against model speed magnitude only and calling the mismatch physical
- false lead 4: using friction to patch bad boundary forcing or wet/dry behavior

## Confidence

medium
