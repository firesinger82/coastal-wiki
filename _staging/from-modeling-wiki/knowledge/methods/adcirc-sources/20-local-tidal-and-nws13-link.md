# Local Tidal And NWS13 Link

## Metadata

- date: 2026-04-12
- title: local tidal boundary update path and NWS13 runtime link
- source type: local workflow
- authors: local scripts and runtime files
- year: active local project state
- link: local scripts and `fort.15`
- local path: E:\ADCIRC_essential\01_Input_BC and E:\ADCIRC_essential\02_Run

## Why This Matters

This source bundle shows how the local workflow splits open-boundary forcing and meteorological forcing into separate preprocessing responsibilities.

## Core Claims

- local tidal scripts such as `update_tidal_bc.m` and `update_tidal_bc_only.m`:
  - read open-boundary nodes from `fort.14`
  - ingest tidal source data such as `NAO99Jb`
  - calculate nodal factors and equilibrium arguments using `tide_fac_utide`
  - write updated constituent forcing back into `fort.15`
- the run-stage `fort.15` separately configures meteorological forcing through `&owiWindNetcdf`
- the run-stage input set already includes `fort.22.nc`

## Practical Value

- method details: confirms that open-boundary forcing and meteorological forcing are separate local preprocessing branches
- implementation detail: shows that `fort.15` is a convergence point where both tidal and met settings meet
- validation detail: narrows future debugging into either the tidal-update branch or the met-conversion branch
- limitations: the exact invocation of `JMA_MSM_Converter.exe` is still not recorded

## Relevance Tags

- solver: ADCIRC
- physics: tides and meteorological forcing
- numerics: preprocessing handoff
- diagnostics: branch separation
- failure mode: forcing-branch confusion

## Transferability

High for the local workflow and moderate for similar ADCIRC pipelines.

## Extraction Targets

- record the expected inputs and outputs of the tidal boundary update scripts
- record the expected inputs and outputs of the JMA-MSM conversion step

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
