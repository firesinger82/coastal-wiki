---
title: "xbeach morphology foundation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach-morphology-foundation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# XBeach Morphology Foundation

Date: 2026-04-30

This note captures the first morphology foundation for XBeach in this wiki.

Scope note:
- this version is grounded mainly in the confirmed local manual stack and current local example/test context
- it is intended to separate hydrodynamic credibility from morphology interpretation before later erosion-case work expands

## Source Basis

Primary sources used for this draft:
- [[01-local-manual-stack]]
- `numerical_models/xbeach/XBEACH_MANUAL.md`
- [[xbeach-parameter-glossary-v1]]
- [[xbeach-boundary-and-wave-setup]]

## First Principle

Do not trust morphology before hydrodynamics are at least credible.

In XBeach, bed change is downstream of:
- wave boundary choice
- mode choice
- current response
- sediment-transport formulation
- slope-handling logic

So the first practical rule is:
- validate boundary and hydrodynamic behavior first
- then interpret erosion, deposition, scarping, or profile change

## Core Morphology Switches

### `sedtrans`

Locally documented as the on/off switch for sediment transport.

Current local interpretation:
- `sedtrans = 1` enables sediment transport

Why it matters:
- without transport active, morphology interpretation is meaningless
- this is one of the first fields to log in any morphology-capable baseline

### `morphology`

Locally documented as the on/off switch for bed evolution.

Current local interpretation:
- `morphology = 1` enables morphological change

Why it matters:
- distinguishes hydrodynamics-only tests from bed-update tests
- this should be turned on only after the boundary/hydrodynamic setup is believable enough for the intended purpose

## Transport-Formula Layer

### `form`

Transport-formulation selector.

Locally confirmed values:
- `form = vanthiel_vanrijn`
- `form = soulsby_vanrijn`
- `form = vanrijn1993`

Current local interpretation:
- `vanthiel_vanrijn` is the practical default in the local note

Why it matters:
- this is a first-order morphology assumption
- if two runs differ in erosion/deposition but use different `form`, they are not directly comparable as a pure forcing or grid sensitivity test

## Morphological Time Scaling

### `morfac`

Morphological acceleration factor.

Locally documented:
- practical range about `1-1000`
- when `morfac > 1`, input time series are effectively scaled relative to morphology evolution

Critical practical implication from the local note:
- large `morfac` can save time
- but it changes how confidently results can be interpreted as event-faithful rather than accelerated behavior

Working rule:
- for short storm/event baselines, prefer `morfac = 1` unless there is a very explicit reason not to
- use larger `morfac` only after the baseline behavior is already understood

### `morfacopt`, `morstart`, `morstop`

These control how and when morphology is advanced.

Why they matter:
- they define the effective morphology window
- they should be logged whenever a case is not simply evolving over the entire hydrodynamic run span

## Slope / Failure / Redistribution Layer

### `avalanching`

Locally documented as the avalanching switch.

Current local interpretation:
- `avalanching = 1` enables slope redistribution / failure handling

Why it matters:
- strongly relevant to dune-face retreat, steep scarps, and bed-shape realism
- must be logged whenever profile evolution is part of the interpretation

### `wetslp` and `dryslp`

Locally documented as critical slope thresholds.

Current local local-note values:
- `wetslp = 0.15`
- `dryslp = 1.0`

Why they matter:
- these are not cosmetic
- they affect when XBeach redistributes overly steep underwater or dry-face slopes
- apparent erosion patterns may partly reflect slope-limiting behavior rather than only forcing intensity

### `dzmax`

Locally documented as a maximum avalanching-related change control.

Why it matters:
- helps define how aggressively local bed updates are redistributed during steepening/failure behavior

## What Good Early Morphology Interpretation Looks Like

For a first XBeach morphology-capable baseline, a good interpretation should answer:
- was hydrodynamic forcing credible enough first?
- which transport formula was active?
- was morphology accelerated with `morfac`, or was it event-faithful (`morfac = 1`)?
- were steep-slope adjustments active through `avalanching`, `wetslp`, and `dryslp`?
- is the result being judged as profile change, shoreline change, erosion volume, or dune-face retreat?

## What Not To Do Early

Avoid these mistakes:
- comparing erosion patterns between runs that quietly changed `form`
- using high `morfac` too early and then treating results as directly event-faithful
- attributing scarping or steep profile differences only to forcing while ignoring avalanching settings
- turning on morphology before boundary/wave setup has been stabilized

## Working Rule For This Wiki

In XBeach, the first trustworthy morphology result is usually the one with the simplest credible hydrodynamic setup, explicit transport-form choice, and minimal interpretive shortcuts.

## Immediate Logging Requirements For Future XBeach Experiments

Every morphology-capable experiment card should record at minimum:
- `wavemodel`
- `wbctype`
- `bcfile`
- `sedtrans`
- `morphology`
- `form`
- `morfac`
- `morfacopt`
- `morstart`
- `morstop`
- `avalanching`
- `wetslp`
- `dryslp`
- target morphology metric (profile, shoreline, erosion volume, dune response, etc.)

## Example Framing From Local Note

Two useful reference directions already appear in the local note:
- DELILAH:
  - 2D surfbeat hydrodynamics comparison orientation
  - more useful as a hydrodynamic credibility reference than as the first morphology baseline
- Holland Coast:
  - 1D dune-erosion framing
  - 42-hour storm example with `morfac = 1`
  - more natural candidate for the first morphology-focused baseline

## Next Expansion Candidates

- [[xbeach-first-baseline-case-selection]]
- future heuristic on using `morfac = 1` first for storm-event baselines
- future failure pattern on morphology interpretation drift caused by premature acceleration or unstable boundary setup
