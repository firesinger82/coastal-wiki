---
title: "adcirc baseline selection"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-baseline-selection.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

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
