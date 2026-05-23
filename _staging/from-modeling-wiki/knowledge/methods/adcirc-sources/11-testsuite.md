# ADCIRC Test Suite

## Metadata

- date: 2026-04-12
- title: ADCIRC model test suite
- source type: code
- authors: ADCIRC development group
- year: active repository
- link: https://github.com/adcirc/adcirc-testsuite
- local path: E:\AI_ENV\modeling-wiki\raw\code\adcirc\adcirc-testsuite

## Why This Matters

This is the strongest candidate source for the first local baseline because it is both a regression suite and a user example set.

## Core Claims

- the suite is used to verify model changes before they enter the upstream repository
- it also acts as a set of examples for users
- the runner is Python-based and uses YAML metadata
- different tests may require different executables and features such as netCDF or GRIB2 support

## Practical Value

- method details: exposes reproducible known-good cases
- implementation detail: offers a structured way to pick the first baseline
- validation detail: provides plots and comparison logic to diagnose regressions
- limitations: some tests may require more compiled features than the simplest first run needs

## Relevance Tags

- solver: ADCIRC
- physics: examples
- numerics: regression and baseline
- diagnostics: automated comparison
- failure mode: version or build mismatch

## Transferability

This should likely become the first local baseline source after the foundation phase.

## Extraction Targets

- choose the first test case to adopt locally
- identify minimum executable feature set for that case
- recorded local quarter-annular case path: `adcirc/adcirc_quarterannular-2d-netcdf`

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
