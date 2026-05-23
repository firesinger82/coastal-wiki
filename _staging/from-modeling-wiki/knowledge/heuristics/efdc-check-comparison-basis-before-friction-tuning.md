# Heuristic Note

## Rule

When EFDC water level looks reasonable but currents do not, check the comparison basis, geometry/bathymetry, and forcing interpretation before serious friction tuning.

## Applies When

- water level amplitude or phase already looks acceptable
- current speed, direction, or timing is still mismatched
- the domain is shallow, estuarine, harbor-like, or strongly sensitive to local conveyance
- the next impulse is to change bottom roughness everywhere

## Does Not Apply When

- both stage and current are obviously wrong from the start
- the model is still failing basic numerical sanity or crashing outright
- a targeted friction study is already justified after comparison basis, geometry, and forcing have been checked

## Evidence

- supporting experiments:
  - future EFDC calibration experiments should be linked here once recorded
- supporting sources:
  - `knowledge/methods/efdc-current-mismatch-diagnosis.md`
  - `knowledge/methods/efdc-calibration-foundation.md`
  - `knowledge/methods/efdc-parameter-glossary-v1.md`
  - local EFDC+ manual RAG synthesis used to draft those notes

## Why It Works

Water level is often less sensitive than velocity to local conveyance, observation representativeness, and omitted momentum drivers. That means a visually good stage fit can coexist with wrong current pathways, wrong tidal asymmetry, or wrong velocity structure. If friction is tuned too early, it may hide geometry, forcing, or wet/dry mistakes instead of resolving them.

## Fast Checks Before Use

- are you comparing like with like: depth-averaged, layered, speed-only, or vector components?
- is the current station actually representative of the modeled cell and local channel geometry?
- are the main tidal boundary assumptions, river inflows, and wind/density drivers credible?
- are the mismatch zones concentrated near shallow flats, constrictions, or harbor entrances?
- has wetting/drying behavior been inspected in the problem area?

## Failure Modes

This heuristic can mislead if it becomes a blanket excuse to avoid friction calibration entirely. Friction still matters, especially for current magnitude and spatial drag structure. The point is sequencing: use friction after the upstream checks are made, not instead of them. It can also fail if the geometry and comparison basis are already sound and the real issue genuinely is bottom drag zoning.

## Confidence

medium
