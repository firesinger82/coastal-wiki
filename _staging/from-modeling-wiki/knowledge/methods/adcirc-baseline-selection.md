# ADCIRC Baseline Selection

Date: 2026-04-12

## Decision

Use the `quarter annular` family as the first baseline candidate.

More specifically, start from the `adcirc-testsuite` case referenced by the official getting-started guide for a 2D quarter annular run with NetCDF output.

## Recorded Local Path

- selected baseline path: `E:\AI_ENV\modeling-wiki\raw\code\adcirc\adcirc-testsuite\adcirc\adcirc_quarterannular-2d-netcdf`
- supporting testsuite entry: `test_list.yaml` entry `adcirc_quarterannular-2d-netcdf`

## Why This Candidate Is First

- the official getting-started page points directly to a quarter annular testsuite case as the example run
- the official examples page lists quarter annular harbor as a canonical example
- it is simpler and more controlled than storm, basin-scale, or coupled-wave examples
- it is suitable for learning file structure, execution flow, and output anatomy before handling a realistic mesh

## Comparison Candidates

### 1. Quarter Annular Harbor

- source: official examples and getting-started guide
- strength: best supported path for a first run
- weakness: idealized geometry, so it is not yet close to real project conditions
- recommendation: use first

### 2. Idealized Inlet

- source: official examples page
- strength: still controlled, but closer to boundary-condition reasoning than quarter annular
- weakness: a slightly larger step up in interpretation burden
- recommendation: use second

### 3. Beaufort Inlet

- source: official examples page
- strength: more realistic coastal behavior
- weakness: too early for the first baseline if the goal is to standardize setup discipline
- recommendation: use after the first manual baseline is stable

### 4. Global Tide Or Storm Cases

- source: official examples page
- strength: useful later for realistic forcing and operational concepts
- weakness: too much surface area for the foundation phase
- recommendation: defer

## Reasoning

This recommendation is partly a direct reading of the official getting-started guide and partly an inference from the example hierarchy. The strongest signal is that the documentation itself uses quarter annular as the example run path.

## Next Step

Extract the file anatomy and minimum required artifacts for the chosen quarter annular testsuite case.
