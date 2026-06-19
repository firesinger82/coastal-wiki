---
title: "xbeach boundary and wave setup"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach-boundary-and-wave-setup.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# XBeach Boundary And Wave Setup

Date: 2026-04-30

> **canonical 안내 (2026-06-04 중복 정리)**: 본 노트는 **초기 orientation/setup-vocabulary**(first-use). 이후 deep 노트로 세분됨 — flow 경계조건 상세 **[[xbeach_flow_boundary_conditions]]**(abs_2d Van Dongeren Riemann), 파 경계 spectrum/config **[[xbeach_wave_boundary]]**, 파 경계 **생성 알고리즘**(bound IG Herbers/Van Dongeren)+SWAN 연동 **[[xbeach_wave_boundary_generation]]** 가 canonical. 본 노트는 설정 어휘·모드 선택 입문용으로 유지.

This note captures the first boundary and wave-setup foundation for XBeach in this wiki.

Scope note:
- this note is based on the confirmed local manual stack, a direct check of the official XBeach documentation site, and a quick inspection of `boundaryconditions.F90`
- it is meant to stabilize first-use setup vocabulary and mode/boundary choices before later case-specific calibration begins

## Source Basis

Primary sources used for this draft:
- `knowledge/methods/xbeach-sources/01-local-manual-stack.md`
- `numerical_models/xbeach/XBEACH_MANUAL.md`
- official docs root: `https://xbeach.readthedocs.io/en/latest/`
- source file: `numerical_models/xbeach/src/src/xbeachlibrary/boundaryconditions.F90`

## First Principle

In XBeach, boundary setup is inseparable from mode choice.

The first question is not only "what boundary file do I have?" but also:
- which `wavemodel` is active?
- is this a 1D or 2DH framing?
- am I prescribing wave conditions as simple parameters, a time-varying table, or a spectrum?
- is tide/water level static, corner-based, or time-varying?

## Mode Before Boundary

### `wavemodel = stationary`

Current local interpretation:
- lower-cost, wave-averaged framing
- can use simple parameterized or tabulated wave-boundary descriptions
- more suitable when the target is not individual-wave behavior

### `wavemodel = surfbeat`

Current local practical default:
- primary mode for storm-scale nearshore response
- supports group-scale forcing and infragravity-driven effects
- likely the first default for erosion and storm-impact baselines

### `wavemodel = nonh`

Current local interpretation:
- for more detailed wave-resolving or steep/structure-sensitive cases
- higher computational cost
- boundary assumptions should be treated more carefully because the model is resolving more detailed wave behavior

## Wave Boundary Buckets

### 1. `wbctype = parametric`

Locally documented with:
- `bcfile = jonswap.txt`

Use when:
- boundary forcing can be described by parameterized wave conditions
- a simpler baseline is preferred before moving to richer directional or time-varying input

### 2. `wbctype = jonstable`

Locally documented with:
- `bcfile = jonstable.txt`

Use when:
- time-varying JONSWAP-style conditions are needed
- a storm window requires boundary evolution in time rather than a single representative condition

### 3. `wbctype = swan`

Locally documented with:
- `bcfile = swan_spectrum.txt`
- 2D directional-frequency spectral input is supported
- netCDF support is noted in the local manual note

Use when:
- directional spectral detail matters
- the workflow already has SWAN-style or equivalent spectrum information available

## Source-Code Confirmation From `boundaryconditions.F90`

The updated local source confirms that boundary logic is mode-sensitive and more varied than the local note alone suggests.

Observed boundary categories in code include handling for:
- `WBCTYPE_TS_1`
- `WBCTYPE_TS_2`
- `WBCTYPE_JONS_TABLE`
- `WBCTYPE_PARAMETRIC`
- `WBCTYPE_SWAN`
- `WBCTYPE_VARDENS`
- `WBCTYPE_REUSE`
- `WBCTYPE_TS_NONH`

Important interpretation:
- the code path distinguishes stationary treatment from surfbeat/nonh treatment for some boundary types
- this reinforces that a boundary recipe should never be documented without the active `wavemodel`

## Tide / Water-Level Setup Terms

### `tideloc`

Locally documented examples include:
- `tideloc = 0`
- `tideloc = 2`

Working interpretation from the local note:
- `tideloc` controls how tide/water level is imposed spatially
- corner-point tide specification is one practical pattern for 2D setups

### `zs0`

Locally documented example:
- `zs0 = 0`

Why it matters:
- useful for simpler fixed-water-level assumptions or baseline water-level offset setup

### `zs0file`

Locally documented example:
- `zs0file = tide.txt`

Why it matters:
- this is the first file-based tide input anchor to log in any reproducible case
- if time-varying tide is active, this should be treated as a baseline input artifact, not an incidental file

## 1D / 2DH Boundary Framing

### `ny`

Current local interpretation:
- `ny = 0` indicates a 1D framing

Why it matters:
- 1D profiles simplify lateral variability and therefore also simplify boundary interpretation
- when a case later becomes 2DH, boundary assumptions should be reconsidered, not copied blindly

### `single_dir`

Current local interpretation:
- can be used to simplify directional treatment in the surfbeat context

Why it matters:
- directional simplification is a first-order setup decision, not a cosmetic flag
- it affects how faithfully offshore wave directionality enters the nearshore response

## Practical Setup Order For This Wiki

For the first serious XBeach baseline, choose setup in this order:
1. choose `wavemodel`
2. decide 1D versus 2DH framing
3. choose wave-boundary family (`parametric`, `jonstable`, `swan`, etc.)
4. define tide/water-level treatment (`tideloc`, `zs0`, `zs0file` as needed)
5. log all boundary files and their exact paths before touching morphology settings

## Working Rule

In XBeach, boundary-condition reproducibility begins with mode reproducibility.

That means every future experiment card should record at minimum:
- `wavemodel`
- `wbctype`
- `bcfile`
- `tideloc`
- `zs0` and/or `zs0file`
- `ny`
- `single_dir` if used

## Common Early Mistakes To Avoid

- documenting a boundary type without documenting the active `wavemodel`
- changing from 1D to 2DH while pretending the same boundary logic still applies cleanly
- treating tide input as an incidental file rather than a core forcing artifact
- mixing morphology tuning into a run before boundary and wave setup are fixed and reproducible

## Next Expansion Candidates

- `knowledge/methods/xbeach-morphology-foundation.md`
- future heuristic on when to prefer `surfbeat` versus `nonh`
- future playbook for selecting the first reproducible XBeach storm baseline
