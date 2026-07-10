---
title: "adcirc parameter glossary v1"
topic: general
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "2026-07-10 재승격: 공식 docs·소스 직접 대조 — parameter_definitions/index.rst(AGRID :10-12·DP(JN) :55-58·IBTYPE(k) :65-113)·tau0.rst(:12-19 GWCE 가중, :204-214 수심의존 값표)·global.F:86-91(WarnElev/ErrorElev 선언·주석 verbatim). 파일·실행파일·출력 항목은 위키 verified 노트([[adcirc-fort-files-reference]]·[[adcirc-parallel-implementation]]) 소급. 원본은 modeling-wiki 2026-04~05 작성분 마이그레이션(2026-05-23) — 당시 본문 인용 0건으로 2026-07-10 L4 감사에서 source-needed 강등 후 당일 보강."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23 → Claude Fable 5 인용 보강·재승격 2026-07-10"
note_date: 2026-04~05 (original) / 2026-05-23 (promote) / 2026-07-10 (verified 재승격)
verification_by: "사용자 + codex source-code analysis → Claude Fable 5 docs/소스 재검증"
verification_date: 2026-07-10
related:
  - models/ADCIRC/source-analysis/adcirc-fort-files-reference.md
  - models/ADCIRC/source-analysis/adcirc-parallel-implementation.md
---

# ADCIRC Parameter Glossary V1

Date: 2026-04-12 (2026-07-10 인용 보강)

This is a first-pass glossary for parameters and concepts that should be tracked early.

It is intentionally narrow. The goal is to stabilize vocabulary before the first experiment.

인용 기준 문서: `docs/technical_reference/parameter_definitions/index.rst` (이하 `paramdef`), `docs/user_guide/model_configuration/model_parameters/tau0.rst` (이하 `tau0.rst`), 소스 `src/global.F`. 경로는 `models/ADCIRC/raw/source_code/adcirc/` 하위.

## Files

([[adcirc-fort-files-reference]] 가 file:line 인용 보유 — 요약만)

- `fort.14`
  - grid and boundary information
  - required
- `fort.15`
  - model parameters and periodic boundary conditions
  - required
- `fort.13`
  - nodal attributes
  - optional but common (`NWP=0` 이면 무시 — [[adcirc-fort-files-reference]] `[file=src/nodalattr.F line=1051]`)

## Core Geometry And Boundary Terms

- `AGRID`
  - alphanumeric grid identification string (`paramdef:10-12`)
  - useful for labeling baseline cases consistently
- `DP(JN)`
  - bathymetric depth relative to the geoid; positive below the geoid, negative above the geoid (`paramdef:55-58` verbatim: "Bathymetric depth with respect to the geoid, positive below the geoid and negative above the geoid")
  - if nodes can dry, wetting and drying must be enabled (`paramdef:58` — "depths above the geoid or sufficiently small that nodes will dry, require that the wetting/drying option is enabled (NOLIFA=2)")
- `IBTYPE(k)`
  - boundary type identifier (`paramdef:65-113`)
  - controls whether the boundary acts like mainland(=0 no-normal-flow essential BC), island, river/open-ocean normal-flow, or barrier classes (`paramdef:67-` 클래스별 정의; fort.14 내 배치는 `docs/technical_reference/input_files/fort14.rst:34-36`)
  - early source of setup mistakes if misunderstood

## Stability-Relevant Terms

- `tau0`
  - weighting applied to the primitive continuity equation within the generalized wave continuity formulation (`tau0.rst:12-19` — "the weighting factor that determines the relative contribution of the primitive and wave portions of the GWCE")
  - 수심이 얕을수록 높은 값 사용이 공식 값표에 내장 (`tau0.rst:204-214`: `TAU0=-1` → depth≥10 에서 0.005, depth<10 에서 0.020; `TAU0=-2` → depth≥200 에서 0.005, 1<depth<200 에서 1/depth, depth<1 에서 1) — 이전 판의 익명 'FAQ guidance' 인용을 공식 문서로 대체
  - should become one of the first logged parameters in stability experiments
- `WarnElev`
  - warning threshold for large free-surface elevation (`global.F:86` verbatim: "elevation at which a warning is issued"; fort.69 dump 제어 `:87-90`)
  - warning output can be an early signal of growing instability
- `ErrorElev`
  - hard-stop threshold for clearly erroneous water-surface elevations (`global.F:91` verbatim: "ADCIRC terminates if this elev is exceeded")

## Execution Terms

([[adcirc-parallel-implementation]] 이 partmesh/prepall·PE 구조 file:line 인용 보유)

- `adcprep`
  - parallel preprocessor used to partition mesh (METIS) and prepare subdomain inputs (PE####/)
- `adcirc`
  - serial executable
- `padcirc`
  - parallel executable

## Output Terms To Track Early

([[adcirc-fort-files-reference]] 출력 표 소급)

- `fort.61.nc`
  - elevation time series at specified stations
- `fort.63.nc`
  - elevation time series at all nodes
- `fort.64.nc`
  - velocity time series at all nodes

## Why This Glossary Exists

- to reduce vocabulary drift between source notes and future experiment cards
- to identify what must be logged for the first baseline and first stability experiments
- to keep file names, executable names, and parameter names consistent in this wiki

## Next Expansion Candidates

- first-pass fort.15 parameter groups for time stepping, output, and forcing
- first-pass boundary-condition vocabulary for ocean, land, barrier, and river cases
