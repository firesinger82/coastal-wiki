---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/06-parameter-definitions.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
last_source_check: 2026-10-11 (recovery 재판독 대조)
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
- 코드는 `(IEVC.EQ.50).or.(IEVC.EQ.51)` 조건에서 THETA1·THETA2를 읽는다. (`[file=src/read_input.F line=5274]` ` IF((IEVC.EQ.50).or.(IEVC.EQ.51)) THEN `; `[file=src/read_input.F line=5275]` ` READ(15,*,err=99999,end=99998,iostat=ios) Theta1,Theta2 `)
- 현행 문서는 IEVC=50일 때만 이 입력 줄을 포함하라고 적는다. (`[file=docs/technical_reference/parameter_definitions/index.rst line=1445]` ` Time weighting coefficients for the MY2.5 turbulence soln. (include this line only if IEVC = 50) `)

- boundary types, bathymetry sign conventions, and barrier semantics are stated directly
- some parameter constraints are strict enough that violating them terminates a run

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
