# ADCIRC wide7 Bootstrap

Date: 2026-04-13

Purpose:
- mark `wide7` as the clean working branch after `wide6`
- keep `wide6` as reference/evidence only

Working directory:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide7`

Initial structure:
- `docs/`
- `input/DEM/`
- `input/domain/`
- `mesh/candidates/`
- `mesh/accepted/`
- `reviews/`
- `runs/`
- `scripts/`
- `artifacts/`

Initial files:
- `README.md`
- `docs/domain-decision-record.md`
- `docs/mesh-candidate-log.md`
- `docs/manual-intervention-log.md`
- `docs/TODO.md`

Working rule:
- all new domain work starts in `wide7`
- all new decisions are recorded before mesh generation
- all mesh candidates are preserved rather than overwritten
- all manual interventions are logged explicitly

Reference rule:
- `wide6` remains a reference and evidence source
- `wide7` is the clean branch for formalized process-driven work
