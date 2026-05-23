# Taxonomy

Use the same vocabulary everywhere.

## Asset Types

- `raw source`: original paper, report, code, example, manual, or forum content
- `source note`: distilled note about one raw source
- `experiment`: one concrete run or tightly scoped run set
- `failure pattern`: recurring symptom-cause cluster
- `heuristic`: reusable rule of thumb with evidence
- `playbook`: step-by-step operating procedure
- `context`: temporary working state

## Recommended Domain Tags

- `domain:coastal`
- `domain:hydrodynamics`
- `domain:transport`
- `domain:wave`
- `domain:morphodynamics`
- `domain:storm-surge`
- `domain:estuary`
- `domain:groundwater`
- `domain:atmospheric`

## Recommended Model Tags

- `model:adcirc`
- `model:efdc`
- `model:xbeach`
- `model:swan`
- `model:schism`
- `model:roms`
- `model:fvcom`
- `model:custom`

## Recommended Method Tags

- `method:fem`
- `method:fvm`
- `method:fdm`
- `method:implicit`
- `method:explicit`
- `method:adaptive-step`

## Recommended Failure Tags

- `failure:divergence`
- `failure:oscillation`
- `failure:mass-drift`
- `failure:boundary-instability`
- `failure:boundary-mismatch`
- `failure:wet-dry-instability`
- `failure:mesh-quality`
- `failure:forcing-inconsistency`
- `failure:calibration-drift`
- `failure:nonphysical-state`
- `failure:slow-convergence`
- `failure:performance`

## Recommended Evidence Tags

- `evidence:paper`
- `evidence:report`
- `evidence:code`
- `evidence:experiment`
- `evidence:diagnostic-plot`
- `evidence:log`

## Naming Rule

Prefer short filenames with the main object first.

Examples:
- `adcirc-boundary-instability.md`
- `cfl-limits-on-refined-grid.md`
- `wind-forcing-spinup-playbook.md`
