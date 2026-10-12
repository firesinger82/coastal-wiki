---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/06-parameter-definitions.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---
# ADCIRC Parameter Definitions

## Metadata

- date: 2026-04-12
- title: Parameter Definitions
- source type: manual
- authors: ADCIRC development team
- year: active documentation site
- link: https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html

## Why This Matters

This is the main source for interpreting fort.14 and fort.15 fields without guesswork.

## Core Claims

- the page gives explicit meanings for many fort.14 and fort.15 fields

- THETA1은 v56.2.1에서 연직 확산을 가중한다. (`[file=src/vsmy.F line=2875]` ` coef2 = delt*theta1/HOamb2 `)
- THETA2는 v56.2.1에서 소산을 가중한다. (`[file=src/vsmy.F line=2883]` ` coef1 = 1.d0 + delt*theta2*tdiss `; `[file=src/vsmy.F line=2885]` ` Mqa(n) = Inm(n,1)*coef1+KQnm(n,1)*coef2 `)
- 현행 RST의 두 역할 설명은 코드의 배정과 반대이다. (`[file=docs/technical_reference/parameter_definitions/index.rst line=1449]` ` THETA1 weights the dissipation term `; `[file=docs/technical_reference/parameter_definitions/index.rst line=1451]` ` THETA2 weights the vertical diffusion term `)
- 코드는 `IF(C3D) THEN`에서 호출하는 READ_INPUT_3D의 `IF((IEVC.EQ.50).or.(IEVC.EQ.51)) THEN`에서 THETA1·THETA2를 읽는다(`src/read_input.F:4622` `IF(C3D) THEN`, `src/read_input.F:4623` `CALL READ_INPUT_3D(StaTim,NT)`, `src/read_input.F:5274` `IF((IEVC.EQ.50).or.(IEVC.EQ.51)) THEN`, `src/read_input.F:5275` `READ(15,*,err=99999,end=99998,iostat=ios) Theta1,Theta2`). [10-12 전수 검증 보완] (`[file=src/read_input.F line=5274]` ` IF((IEVC.EQ.50).or.(IEVC.EQ.51)) THEN `; `[file=src/read_input.F line=5275]` ` READ(15,*,err=99999,end=99998,iostat=ios) Theta1,Theta2 `)
- 현행 문서는 IEVC=50일 때만 이 입력 줄을 포함하라고 적는다. (`[file=docs/technical_reference/parameter_definitions/index.rst line=1445]` ` Time weighting coefficients for the MY2.5 turbulence soln. (include this line only if IEVC = 50) `)

- boundary types, bathymetry sign conventions, and barrier semantics are stated directly
- some parameter constraints are strict enough that violating them terminates a run


([theory 보고서 §5 1036행 (`C13`)](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md#5-차이-결론); 항목: C13 현행 매개변수 문서의 오류 누락) 근거: `models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort15.rst:138` ``:ref:`THETA1 <THETA1>`, :ref:`THETA2 <THETA2>`      include this line only if IEVC = 50 or 51``<br>`models/ADCIRC/raw/source_code/adcirc/src/read_input.F:5274` `IF((IEVC.EQ.50).or.(IEVC.EQ.51)) THEN`<br>`models/ADCIRC/raw/source_code/adcirc/src/read_input.F:5275` `READ(15,*,err=99999,end=99998,iostat=ios) Theta1,Theta2`<br>`models/ADCIRC/raw/source_code/adcirc/src/vsmy.F:2875` `coef2 = delt*theta1/HOamb2`<br>`models/ADCIRC/raw/source_code/adcirc/src/vsmy.F:2883` `coef1 = 1.d0 + delt*theta2*tdiss`<br>`models/ADCIRC/raw/source_code/adcirc/src/vsmy.F:2885` `Mqa(n) = Inm(n,1)*coef1+KQnm(n,1)*coef2`<br>해석: 보고서 C13의 문서 소개는 실제 입력 조건과 THETA 역할의 문서 오류를 안내하지 않는다. 3D-THETA-INPUT·3D-THETA-ROLES의 B 결론을 구체적으로 연결해야 한다. 결론: 문서 누락. 현행 매개변수 노트에는 IEVC=50·51 입력 조건과 THETA 역할의 문서 오기를 명시해야 한다.

## Practical Value

- method details: supports careful reading of mesh and boundary semantics
- implementation detail: should drive the first parameter glossary in this wiki
- validation detail: helps check whether a setup violates structural assumptions before running
- limitations: the page is extensive, so it should be mined selectively rather than read linearly each time

## Relevance Tags

- solver: ADCIRC
- physics: boundary and bathymetry semantics
- numerics: parameter meaning
- diagnostics: pre-run validation
- failure mode: invalid configuration

## Transferability

Crucial for future experiment cards, decisions, and failure-pattern notes.

## Extraction Targets

- first set of parameters to log in every experiment card
- first pre-run sanity checklist

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
