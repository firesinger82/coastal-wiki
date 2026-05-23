# Failure Pattern

## Pattern Name

wet/dry connectivity bias

## Symptom

An EFDC model shows suspicious current behavior in shallow flats, harbor margins, shoals, or channel edges that appears disproportionate to the stage mismatch.

Typical signs:
- stage is broadly reasonable but currents are distorted near shallow transition zones
- flow pathways look too blocked or too permissive in marginal shallow areas
- flood/ebb asymmetry is exaggerated in flats or side channels
- isolated shallow cells trap water or drain unrealistically
- friction tuning produces unstable or inconsistent improvements because the deeper issue is connectivity logic

## Common Context

- solver / model: EFDC or EFDC+
- mesh / geometry: shallow coastal, estuarine, wetland, or harbor-margin domain
- forcing: tidal or mixed tidal/river/wind case with active shallow exchange zones
- parameter regime: wetting/drying enabled, or shallow-cell behavior strongly affecting effective conveyance

## Likely Causes

1. the chosen `ISDRY` mode is too blocking or too permissive for the physical setting
2. `Dry Depth` is inconsistent with the intended shallow-cell activation behavior
3. `Minimum Height` initialization is inconsistent with `Dry Depth`, biasing the initial wet state
4. draining / dry-step behavior is altering isolated shallow cells in a way that changes effective connectivity
5. the real issue is connectivity control, but the calibration effort is being framed as friction or bathymetry only

## Quick Triage

1. record the exact wet/dry settings first
   - `ISDRY`
   - `Dry Depth`
   - `Minimum Height`
   - draining / dry-step settings
2. inspect where mismatch clusters in space
   - tidal flats
   - channel margins
   - harbor shoals
   - intermittently wet pathways
3. ask whether the model is over-blocking or over-rewetting shallow exchange routes
4. check whether initialization forced cells wet that should be allowed to dry
5. only after wet/dry behavior is understood, return to friction or secondary tuning

## Supporting Evidence

- related experiments:
  - future EFDC experiment cards should be linked here once wet/dry sensitivity runs exist
- related sources:
  - `knowledge/methods/efdc-wetting-drying-foundation.md`
  - `knowledge/methods/efdc-calibration-foundation.md`
  - `knowledge/methods/efdc-current-mismatch-diagnosis.md`
  - `knowledge/playbooks/efdc-tidal-calibration-order.md`

## Common False Leads

- false lead 1: assuming shallow-zone current mismatch is only a friction issue
- false lead 2: treating wet/dry as a minor numerical detail rather than a connectivity-control choice
- false lead 3: ignoring initialization consistency between `Minimum Height` and `Dry Depth`
- false lead 4: assuming good stage fit means wet/dry behavior is already acceptable

## Confidence

medium
