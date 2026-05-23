# Active Questions

Use this file for questions that are not settled yet.

For each question, note:
- why it matters
- what evidence would resolve it
- which source or experiment should answer it next

## Open Questions

- question: which official ADCIRC example should become the first baseline case?
  why it matters: the first experiment should start from a known-good case rather than a fresh custom setup
  next evidence: compare official examples and adcirc-testsuite coverage

- question: what exact ingredients make `wide6` reproducible as the current local mesh baseline?
  why it matters: preserving the only tuned branch matters more than debating tools in the abstract
  next evidence: extract the required shapefiles, DEM sources, manual edits, smoothing rules, and boundary-classification interventions from `wide6`

- question: is `wide6` actually valid, or only the least-bad local candidate?
  why it matters: comparing new mesh tools against an unvalidated reference can lock in the wrong target
  next evidence: define and check reproducibility, geometry, bathymetry, mesh-quality, boundary, downstream-stability, and physical-plausibility gates for `wide6`

- question: can the final `wide6` branch be reconstructed into a replayable workflow despite iterative manual and agent-assisted edits?
  why it matters: without provenance reconstruction, `wide6` cannot serve as a fair target for revalidation or Python migration
  next evidence: identify confirmed source inputs, confirmed final scripts, confirmed manual interventions, and explicitly unknown steps

- question: which retained `fort.13` and `fort.15` generation steps actually correspond to the current run artifacts in `output/oceanmesh2d`?
  why it matters: the current retained run branch mixes NAO99jb, earlier FES2022b notes, and later tuning changes
  next evidence: compare current file contents, backup files, script signatures, and validation outputs to reconstruct the final retained run branch

- question: which parts of the `wide6` `OceanMesh2D` workflow are straightforward to translate into Python, and which parts are not?
  why it matters: the user wants to move away from MATLAB dependence without losing the behavior that actually worked
  next evidence: compare `make_mesh_om2d.m` against the available Python-side scripts and identify functionality gaps

- question: can `Gmsh` be fairly revalidated after the earlier failures?
  why it matters: there is already a serious Python+Gmsh branch, but the local evidence is negative
  next evidence: turn the logged failure modes into a revalidation checklist covering size field, boundary fidelity, element quality, and downstream stability

- question: can `OCSMesh` reproduce the `wide6` basin with acceptable quality and stability?
  why it matters: `OCSMesh` may be a better Python-side coastal meshing path than raw `Gmsh`
  next evidence: compare the `ocsmesh_test` reconstruction assumptions against the verified `wide6` inputs and outputs

- question: what is the local canonical path for constructing bathymetry and topography in `fort.14`?
  why it matters: terrain definition is upstream of later stability and validation work
  next evidence: identify actual source datasets, datum policy, interpolation workflow, and slope-limiting/QC steps, starting from the `wide6` branch

- question: what is the exact local conversion path from `JMA-MSM` to OWI-`NWS=13` NetCDF?
  why it matters: this is the real forcing bottleneck for local storm-surge work
  next evidence: reconcile the GUI downloader contract in `E:\numerical_models\adcirc\data\wind\jma` with the retained notebook workflow in `E:\numerical_models\adcirc\tools\utilities`, then identify which branch is the trusted editable path for producing the `fort.22.nc` used in `02_Run`

- question: what exact raw files does the GUI downloader save for a given JMA-MSM date range?
  why it matters: the upstream source URL is known now, but reproducible reruns still need the local raw-file contract
  next evidence: compare additional download windows to the observed `E:\AI_ENV\2003\0901.nc` to `0903.nc` result and verify whether `MMDD.nc` is the stable naming rule

- question: which local `grid` helper programs are still active in the preprocessing chain?
  why it matters: mesh and bathymetry work will stay confusing until we separate active tools from archived utilities
  next evidence: classify the files under `E:\numerical_models\adcirc\tools\utilities\grid` into active, legacy, and reference-only groups

- question: when should `SubgridADCIRCUtility` or time-varying bathymetry enter the workflow?
  why it matters: advanced terrain options can help, but adopting them too early can hide the base bathymetry pipeline
  next evidence: define the first standard bathymetry path and identify where it fails

- question: when should ADCIRCpy or ASGS enter the workflow?
  why it matters: early automation can help, but adding tooling too soon can hide core model understanding
  next evidence: finish preprocessing foundation phase and identify whether setup automation or operational runs are the next bottleneck
