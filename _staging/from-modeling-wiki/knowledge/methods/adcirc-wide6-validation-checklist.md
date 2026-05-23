# ADCIRC wide6 Validation Checklist

Date: 2026-04-13

Purpose:
- turn the `wide6` validation question into a concrete checklist
- classify what is already evidenced, what is only claimed, and what is still missing
- stop using `wide6` as an implicit truth target

Target:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6`

Status labels:
- `PASS`: evidence exists and is at least minimally reviewable
- `REVIEW`: evidence exists but is not strong enough to accept yet
- `MISSING`: required evidence is not yet found or not yet archived

## Current Overall Judgement

Current judgement:
- `wide6` is a viable baseline candidate
- `wide6` is not yet a validated reference mesh

Reason:
- there is substantial artifact evidence
- but key gates are still only partially closed
- the retained tidal validation summary itself says `REVIEW` against the NDMI benchmark

## Checklist

| Gate | What must be checked | Current status | Current evidence | Main gap |
| --- | --- | --- | --- | --- |
| Reproducibility | exact inputs, scripts, manual steps, and output chain can be replayed | `MISSING` | `WORK_LOG.md`, `scripts/`, `input/`, `output/` all exist | manual edits, agent-assisted changes, and exact replay order are not frozen |
| Geometry | offshore boundary, coastline retention, island handling, open-boundary topology | `REVIEW` | `output/design/*.png`, `mainland.shp`, `ocean_new_w6.shp`, `classify_boundaries.py`, `draw_ocean_boundary.py` | manual boundary design logic is not yet formalized |
| Bathymetry | GEBCO+BADA merge, min depth, smoothing, slope limiting are explicit and reviewable | `REVIEW` | `WORK_LOG.md` records `GEBCO + BADA2024`, min depth 5 m, slope limit 0.05 | exact executable bathymetry recipe and QC outputs are not yet frozen |
| Mesh quality | degenerate elements, angles, aspect ratio, local bad clusters are checked and archived | `REVIEW` | `matlab_log.txt` shows mesh-quality evolution; `WORK_LOG.md` says degenerate elements were removed | no final accepted QC report found yet |
| Boundary construction | open/land boundaries are correct and reproducible | `REVIEW` | `WORK_LOG.md` records auto classification failure and manual GUI correction; `fix_boundaries.py`, `classify_boundaries.py` exist; `fort.14` boundary block is internally consistent | final boundary review checklist is missing |
| Downstream numerical stability | ADCIRC run completes without obvious mesh-driven instability | `PASS` | retained run outputs in `output/oceanmesh2d/`, `fort.63.nc`, `maxele.63.nc`, `run.bat`; log records stable 30-day run | still needs a cleaner archived run-summary note |
| Physical plausibility | model behavior is believable, not just numerically stable | `REVIEW` | `output/validation/tidal_validation_summary.txt`, scatter plots, station maps, CSV outputs | validation exists but benchmark is weaker than NDMI and still flagged `REVIEW` |

## Evidence Notes

### 1. Reproducibility

What exists:
- `WORK_LOG.md` contains a strong narrative of the tuning history
- the `input/`, `scripts/`, `output/`, and `validation/` directories are retained
- both `OceanMesh2D` and `Gmsh` branches remain visible for comparison

Why this is now `MISSING` rather than `REVIEW`:
- the workflow includes manual offshore boundary design
- the workflow includes manual open-boundary correction
- the branch was improved through repeated iterative edits and agent-assisted modifications
- the exact replay order is not yet written as a single canonical recipe
- we cannot currently replay `wide6` end to end with confidence

### 2. Geometry

What exists:
- design figures exist under `output/design/`
- domain source files exist under `input/`
- `WORK_LOG.md` explains the domain concept and the open-boundary depth rule

Why still `REVIEW`:
- the offshore boundary is partly a user-designed artifact
- there is not yet a formal review note explaining why that geometry is acceptable

### 3. Bathymetry

What exists:
- `WORK_LOG.md` explicitly records:
  - `GEBCO + BADA2024`
  - minimum depth forcing of 5 m
  - slope limit of 0.05
  - smoothing as a stability-critical intervention

Why still `REVIEW`:
- this is still mainly in narrative form
- the exact executable merge-and-smooth chain has not been frozen into a reproducible recipe

### 4. Mesh Quality

What exists:
- `matlab_log.txt` records iterative mesh quality improvement
- `WORK_LOG.md` records removal of degenerate elements

Why still `REVIEW`:
- we do not yet have one final QC note saying what the accepted thresholds are
- we do not yet have a final archived report for element-quality acceptance

### 5. Boundary Construction

What exists:
- `WORK_LOG.md` clearly states that OceanMesh2D auto-classification failed
- the retained scripts show that a separate boundary-fix workflow exists
- the retained `fort.14` boundary block is internally consistent:
  - open boundaries: `1`
  - open-boundary nodes: `70`
  - land boundaries: `2189`
  - land-boundary nodes: `102958`
  - boundary references are in-range
- however, the open-boundary depth minimum computed from `fort.14` is `217.727 m`, which is shallower than the retained log claim of `283 m`

Why still `REVIEW`:
- we still need a formal final rule for:
  - how open boundary nodes are chosen
  - how shallow boundary segments are excluded
  - how the final boundary is reviewed before run

Refined note from direct check:
- the retained `fort.14` open boundary is mostly deep-water
- the depth mismatch to the log is driven by one shallow endpoint node at `217.727 m`
- this weakens the log precision, but does not yet prove that the open boundary is fundamentally misplaced

### 6. Downstream Numerical Stability

What exists:
- retained run artifacts exist in `output/oceanmesh2d/`
- the retained run setup exists in `run.bat`
- `WORK_LOG.md` states the 30-day run progressed stably and was effectively completed

Why this is `PASS`:
- this is the strongest closed gate right now
- `wide6` is not just a static mesh artifact; it reached a sustained ADCIRC run state

Limitation:
- numerical stability alone does not validate the mesh physically

### 7. Physical Plausibility

What exists:
- `output/validation/tidal_validation_summary.txt`
- validation plots and CSV outputs in `output/validation/`

Observed result from retained summary:
- M2 RMSE 23.84 cm, R 0.9673
- S2 RMSE 11.14 cm, R 0.9455
- K1 RMSE 8.31 cm, R 0.8914
- O1 RMSE 5.45 cm, R 0.9255
- all four constituents are marked `REVIEW` against the NDMI benchmark in the retained summary

Why this stays `REVIEW`:
- physical validation exists, which is good
- but it is not yet strong enough to accept `wide6` as the target truth

## Immediate Decision

Use this rule from now on:
- `wide6` is the current baseline candidate

Do not use this rule yet:
- `wide6` is the validated reference mesh

## Next Checks

The next highest-value actions are:
1. write a canonical `wide6` replay recipe from `input -> scripts -> manual edits -> final run`
2. write a boundary review checklist specifically for the manually corrected open boundary
3. write a bathymetry recipe note that turns the `GEBCO + BADA2024 + slope limit 0.05` narrative into a repeatable pipeline
4. write a mesh-QC note that defines acceptance thresholds instead of relying on qualitative memory
5. summarize the retained tidal validation into a short judgement note that explains whether the current mismatch to NDMI is acceptable, temporary, or disqualifying

## Bottom Line

Right now `wide6` is:
- stronger than the other local attempts
- useful enough to preserve
- not reliable enough to be treated as ground truth without further validation
