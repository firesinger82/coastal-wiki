---
title: "xbeach parameter glossary v1"
topic: general
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach-parameter-glossary-v1.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# XBeach Parameter Glossary V1

Date: 2026-04-30

This is the first-pass XBeach glossary for the modeling wiki.

Scope note:
- this version is grounded mainly in the confirmed local source stack
- exact behavior still needs later cross-checking against the full official manual pages when details matter
- the goal here is to stabilize the first vocabulary and setup buckets, not to exhaust every parameter

## Source Basis

Primary confirmed local sources:
- `knowledge/methods/xbeach-sources/01-local-manual-stack.md`
- `/mnt/e/numerical_models/xbeach/XBEACH_MANUAL.md`
- official docs root: `https://xbeach.readthedocs.io/en/latest/`

## Why This Glossary Exists

- to stabilize the first XBeach setup vocabulary
- to separate hydrodynamic mode choice from later morphology tuning
- to prepare for boundary/wave-setup and morphology foundation notes

## Core Mode-Selection Terms

### `wavemodel`

Primary mode-selection key.

Current locally confirmed values:
- `wavemodel = stationary`
- `wavemodel = surfbeat`
- `wavemodel = nonh`

Why it matters:
- this is the first strategic choice in XBeach
- it changes what physics are resolved directly, what boundary setup is needed, and what the runtime cost will be

### `stationary`

Use when focusing on wave-averaged behavior under relatively mild or simplified forcing.

Current local interpretation:
- lower cost
- no infragravity/group-scale variability resolved the way surfbeat does
- can be useful for simpler morphodynamic studies or tide-plus-wave framing

### `surfbeat`

Current local practical default / recommended mode for storm-coast response.

Current local interpretation:
- resolves wave-group-scale forcing and infragravity response
- suitable for wave-induced setup and unsteady current behavior in many storm-impact problems
- likely the first mode to prioritize for coastal erosion and storm-scale baseline work

### `nonh`

Non-hydrostatic mode for more detailed wave-resolving situations.

Current local interpretation:
- higher cost
- more appropriate for steep settings, structures, gravel beaches, or individual-wave behavior
- not the first default unless the case really needs it

### `nhq3d`

Locally documented as:
- `nhq3d = 1` for a two-layer reduced non-hydrostatic formulation

Why it matters:
- belongs to the non-hydrostatic family of choices
- should be tracked whenever `wavemodel = nonh` is used

## Boundary And Forcing Terms

### `wbctype`

Wave-boundary condition selector.

Locally confirmed examples:
- `wbctype = params`
- `wbctype = jonstable`

Why it matters:
- one of the first parameters to log for baseline reproducibility
- separates constant/parameter-style forcing from time-varying/tabulated forcing behavior

### `single_dir`

Locally documented in the surfbeat context.

Why it matters:
- affects directional treatment of incoming waves
- should be tracked whenever a case simplifies directional spreading

### `ny`

Locally documented as part of 1D/2DH interpretation.

Current local interpretation:
- `ny = 0` indicates a 1D option in the documented framing

Why it matters:
- this is a key structural switch between profile-style and more laterally variable cases

## Breaking / Dissipation Terms

### `break`

Breaking-model selector.

Locally confirmed values include:
- `break = roelvink1`
- `break = roelvink2`
- `break = roelvink_daly`
- `break = baldock`
- `break = janssen`

Why it matters:
- breaking choice directly affects setup, infragravity response, nearshore currents, and later sediment transport behavior
- this should be logged in every serious XBeach baseline

### `gamma`

Locally documented in the Roelvink-Daly breaking context.

Current local local-note values:
- breaking start threshold around `gamma = 0.46`
- secondary threshold around `gamma2 = 0.34`

Why it matters:
- `gamma` is one of the first XBeach terms likely to reappear in calibration and sensitivity work
- should be treated as a high-value glossary item for later refinement

## Bed Friction Terms

### `bedfriction`

Bed-friction formulation selector.

Locally confirmed values:
- `bedfriction = chezy`
- `bedfriction = manning`
- `bedfriction = cf`
- `bedfriction = white-colebrook`
- `bedfriction = white-colebrook-grainsize`

Why it matters:
- XBeach current and morphology response can depend strongly on the chosen friction law
- this must be logged explicitly, not buried in a run folder

### Manning roughness

Locally documented example:
- `bedfriction = manning`
- default local-note value: `n = 0.02`

Why it matters:
- likely to be one of the first practical friction settings revisited in coastal profile or storm-response work

## Morphology Terms

### `form`

Sediment-transport formulation selector.

Locally confirmed values:
- `form = vanthiel_vanrijn`
- `form = soulsby_vanrijn`
- `form = vanrijn1993`

Why it matters:
- transport formula choice is a first-order morphology assumption
- must be logged before any interpretation of erosion/deposition skill

### `morfac`

Morphological acceleration factor.

Locally documented range:
- `morfac` may be used from about 1 to 1000 in the local note framing

Why it matters:
- changes the relationship between hydrodynamic runtime and bed-update evolution
- high leverage parameter that must be recorded in every morphology experiment

### `avalanching`

Locally documented switch:
- `avalanching = 1` enables avalanching / slope redistribution behavior

Why it matters:
- influences dune face or steep-slope behavior
- important whenever profile collapse, scarping, or slope limits matter

### `wetslp` and `dryslp`

Locally documented slope controls in the avalanching context:
- `wetslp` for submerged slope threshold
- `dryslp` for dry slope threshold

Why they matter:
- critical for morphology realism in steep or erosive settings
- likely to become recurrent sensitivity terms in later XBeach work

## Groundwater / Special-Mode Terms

### `gwflow`

Groundwater-flow switch.

Locally confirmed example:
- `gwflow = 1`

Why it matters:
- especially important for gravel-beach or infiltration-sensitive settings
- should be logged whenever XBeach-G style behavior or surface-groundwater exchange is relevant

### `gwscheme`

Groundwater scheme selector.

Locally confirmed values:
- `gwscheme = laminar`
- `gwscheme = turbulent`

Why it matters:
- belongs to the groundwater/specialized mode family of assumptions

## Structural Setup Terms

### `params.txt`

Current local framing treats `params.txt` as the central early setup file.

Why it matters:
- this is the first practical anchor for reproducibility
- future source notes should map the most important baseline fields in `params.txt`

### Staggered curvilinear grid

Current local note explicitly documents:
- staggered curvilinear grid layout
- cell-center versus cell-edge variable placement

Why it matters:
- helps interpret outputs and understand how setup choices map to velocity and bed-change behavior

## Immediate High-Value Parameters To Track In Future Experiments

Whenever the first XBeach experiment cards are created, record at minimum:
- `wavemodel`
- `wbctype`
- `single_dir` if used
- `ny`
- `break`
- `gamma` if breaking thresholds are changed
- `bedfriction` plus the associated roughness parameterization
- `form`
- `morfac`
- `avalanching`
- `wetslp`
- `dryslp`
- `gwflow` and `gwscheme` if groundwater is active

## Next Expansion Candidates

- `knowledge/methods/xbeach-boundary-and-wave-setup.md`
- `knowledge/methods/xbeach-morphology-foundation.md`
- exact output-variable vocabulary from the official docs and local runs
- first heuristic on when to prefer `surfbeat` versus `nonh`
