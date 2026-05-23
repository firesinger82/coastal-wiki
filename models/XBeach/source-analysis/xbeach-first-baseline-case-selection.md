---
title: "xbeach first baseline case selection"
topic: general
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach-first-baseline-case-selection.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# XBeach First Baseline Case Selection

Date: 2026-04-30

This note chooses how the first XBeach baseline cases should be used in this workspace.

Scope note:
- the goal is not to pick one case for everything
- the goal is to separate:
  - smoke/regression baseline
  - hydrodynamic reference baseline
  - first morphology-oriented baseline

## Candidate Pool

Confirmed local and documented candidates:
- local smoke-test case: `models/example_1d`
- local additional candidate: `models/example_2d`
- documented reference example: DELILAH
- documented reference example: Holland Coast

## Selection Criteria

A good first baseline should score well on:
- reproducibility
- low setup ambiguity
- easy rerun path
- good documentation of forcing and intent
- good match to the question type being tested

## Baseline Roles

### 1. Smoke / Regression Baseline

Selected case:
- `models/example_1d`

Why:
- already executed successfully with the rebuilt operating executable
- short runtime
- simple local packaging
- useful for post-build sanity checks and binary regression checks

What it is good for:
- confirming the executable launches
- checking that params parsing still works
- checking that boundary setup still runs
- checking that netCDF output generation still completes

What it is not good for:
- scientific validation of coastal erosion skill
- judging advanced 2D directional behavior
- choosing final morphology parameter defaults

Linked evidence:
- `experiments/2026/xbeach/2026-04-30-example-1d-smoke-test.md`

### 2. First Hydrodynamic Reference Baseline

Preferred candidate:
- DELILAH

Why:
- explicitly framed in the local note and official examples as a 2D surfbeat directional-spreading hydrodynamic comparison case
- better aligned with checking whether wave/current response is credible before morphology interpretation expands

What it is good for:
- hydrodynamic comparison mindset
- 2D surfbeat behavior
- directional wave forcing context

What it is not ideal for:
- first morphology-centric baseline if the main question is dune or profile erosion evolution

### 3. First Morphology-Oriented Baseline

Preferred candidate:
- Holland Coast

Why:
- explicitly documented as a 1D dune-erosion style example
- local note frames it as a 42-hour storm case
- `morfac = 1` in the local note makes it attractive as an event-faithful early morphology reference
- more natural fit for profile-change and storm-erosion interpretation than DELILAH

What it is good for:
- first morphology foundation work
- dune/profile erosion framing
- checking how transport, avalanching, and slope logic affect interpretable outcomes

What it is not ideal for:
- representing all 2D directional-coast problems
- acting as the only XBeach baseline for the whole lane

## Decision

Use a two-layer baseline strategy.

### Operational decision
- first quick regression baseline: `models/example_1d`
- first hydrodynamic reference baseline: DELILAH
- first morphology-oriented reference baseline: Holland Coast

This is better than forcing one case to do all jobs.

## Why Not `example_2d` First?

`example_2d` may still become useful, but right now it is not yet better justified than the documented examples.

Current reasons to defer it:
- no successful run or note has yet anchored it in this workspace
- DELILAH and Holland Coast already provide clearer role definitions from the local documentation

## Immediate Next Actions

1. keep `example_1d` as the standard smoke/regression case after rebuilds
2. create a DELILAH source note or method note for hydrodynamic reference usage
3. create a Holland Coast source note or method note for morphology reference usage
4. only after that decide whether `example_2d` should become a local 2D baseline in its own right

## Working Rule For This Wiki

Do not use one XBeach case as the baseline for every question type. Use:
- one small local smoke test
- one hydrodynamic reference case
- one morphology-oriented reference case

## Follow-On Notes

- future source note for DELILAH
- future source note for Holland Coast
- future heuristic on baseline role separation in XBeach
