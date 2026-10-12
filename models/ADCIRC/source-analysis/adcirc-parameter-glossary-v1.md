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
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
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
  - 현행 RST는 TAU0=-1의 `depth >= 10`에 0.005를 적는다. (`docs/user_guide/model_configuration/model_parameters/tau0.rst:204` ``` -  ``If depth >= 10; then``\ :math:`\tau_0`\ ``= 0.005`` ```)
  - v56.2.1 코드는 `IF(Depth.LE.10.) Tau0NodalValue=0.020d0`과 `IF(Depth.GT.10.) Tau0NodalValue=0.005d0`을 사용한다. (`src/nodalattr.F:2158` ` IF(Depth.LE.10.) Tau0NodalValue=0.020d0 `; `src/nodalattr.F:2159` ` IF(Depth.GT.10.) Tau0NodalValue=0.005d0 `)
  - TAU0=-2의 코드 조건은 `(Depth.LT.200.).AND.(Depth.GE.1.)`이다. (`src/nodalattr.F:2152` ` IF((Depth.LT.200.).AND.(Depth.GE.1.)) THEN `; `src/nodalattr.F:2153` ` Tau0NodalValue=1./Depth `)
  - 현행 RST의 `1 < depth < 200` 설명은 수심 1을 빠뜨린다. (`docs/user_guide/model_configuration/model_parameters/tau0.rst:213` ``` -  ``If 1 < depth < 200; then``\ :math:`\tau_0`\ ``= 1/depth`` ```; `src/nodalattr.F:2152` ` IF((Depth.LT.200.).AND.(Depth.GE.1.)) THEN `)
  - TAU0=-2.1이 -2와 같은 수심 계수식을 쓰는지는 확인하지 않음. (`src/nodalattr.F:2149` ` IF (Scheme.eq.-2.d0) THEN `)
  - should become one of the first logged parameters in stability experiments
- `WarnElev`
  - warning threshold for large free-surface elevation (`global.F:86` verbatim: "elevation at which a warning is issued"; fort.69 dump 제어 `global.F:87-90`)
  - warning output can be an early signal of growing instability
- `ErrorElev`
  - hard-stop threshold for clearly erroneous water-surface elevations (`global.F:91` verbatim: "ADCIRC terminates if this elev is exceeded")


([fort15 보고서 §5 L712, L713, C01 (L839)](../../../_staging/recovery/compare/ADCIRC-fort15-vs-code.md#5-차이-결론); 항목: TAU0 수심 경계) 근거: 확인한 원문: `docs/user_guide/model_configuration/model_parameters/tau0.rst:204` ``` -  ``If depth >= 10; then``\ :math:`\tau_0`\ ``= 0.005`` ```<br>`docs/user_guide/model_configuration/model_parameters/tau0.rst:205` ``` -  ``If depth < 10; then``\ :math:`\tau_0`\ ``= 0.020`` ```<br>`docs/user_guide/model_configuration/model_parameters/tau0.rst:212` ``` -  ``If depth >= 200; then``\ :math:`\tau_0`\ ``= 0.005`` ```<br>`docs/user_guide/model_configuration/model_parameters/tau0.rst:213` ``` -  ``If 1 < depth < 200; then``\ :math:`\tau_0`\ ``= 1/depth`` ```<br>`docs/user_guide/model_configuration/model_parameters/tau0.rst:214` ``` -  ``If depth < 1; then``\ :math:`\tau_0 = 1` ```<br>`src/nodalattr.F:2149` ` IF (Scheme.eq.-2.d0) THEN `<br>`src/nodalattr.F:2151` ` IF(Depth.GE.200.) Tau0NodalValue=0.005 `<br>`src/nodalattr.F:2152` ` IF((Depth.LT.200.).AND.(Depth.GE.1.)) THEN `<br>`src/nodalattr.F:2153` ` Tau0NodalValue=1./Depth `<br>`src/nodalattr.F:2155` ` IF(Depth.LT.1.) Tau0NodalValue=1.0 `<br>`src/nodalattr.F:2158` ` IF(Depth.LE.10.) Tau0NodalValue=0.020d0 `<br>`src/nodalattr.F:2159` ` IF(Depth.GT.10.) Tau0NodalValue=0.005d0 `<br>해석: 같은 판 RST는 -1의 depth=10에 0.005를 적지만 코드는 <=10에 0.020을 대입한다. -2의 문서 구간은 depth=1을 빠뜨렸고 코드는 >=1 분기로 1을 만든다. exact Scheme=-2가 아니면 두 구간 초기화를 사용하므로 -2.1을 -2와 같은 초기값 선택으로 일반화하지 않는다. 결론: 문서 오기. v56.2.1의 기본 두 구간 TAU0 초기화는 수심 10 이하에서 0.020을 사용한다.
([theory 보고서 §5 1027행 (`C04`)](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md#5-차이-결론); 항목: C04 τ₀ 문서 값과 실제 분기) 근거: `models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2149` `IF (Scheme.eq.-2.d0) THEN`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2151` `IF(Depth.GE.200.) Tau0NodalValue=0.005`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2152` `IF((Depth.LT.200.).AND.(Depth.GE.1.)) THEN`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2153` `Tau0NodalValue=1./Depth`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2155` `IF(Depth.LT.1.) Tau0NodalValue=1.0`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2158` `IF(Depth.LE.10.) Tau0NodalValue=0.020d0`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2159` `IF(Depth.GT.10.) Tau0NodalValue=0.005d0`<br>보고서 C04의 노트는 현행 문서의 D=10·D=1 조건을 그대로 현재 코드 값표로 옮긴다. 해석: 문서의 경계값 오기를 노트가 이어받았다. −2.1의 별도 코드 결함 후보는 TAU-FRACTION 결론을 참조한다. 결론: 문서 오기. 현재 τ₀ 값표는 −1의 D≤10 조건과 −2의 1≤D<200 조건을 코드대로 기록해야 한다.

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
