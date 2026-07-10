---
title: "ADCIRC Storm Surge — NWS family 비교 (NWS=3/4/13/14/20)"
topic: storm-surge
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "2026-07-10 재승격: 공식 docs 직접 대조 — nws_parameters.rst(NWS=3 :248 / =4 :251 / =13 :308-310 / =14 :311-312 / =19 discouraged :32 verbatim). NWS=13 실기능은 코드 정본(read_input.F:1782 owiWindNetcdf namelist·:4721 'OWI Netcdf (NWS13) format') — rst :308-310 'ramping' 서술은 stale(code≠docs, [[adcirc-storm-surge-foundation]] 판정 공유). 2026-07-10 L4 감사 후속: 개인 워크플로 서술은 _staging/from-canonical/adcirc-nws13-jma-msm-local-workflow.md 로 추출(절대규칙 #2·#8), 객관 단언은 [[adcirc-met-forcing-implementation]] (file:line 인용 보유) 로 소급."
note_author: "사용자 + codex source-code 분석 (2026-04 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23 → L4 레이어 정리 2026-07-10"
note_date: 2026-04 (original) / 2026-05-23 (promote) / 2026-07-10 (layer cleanup)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md
  - models/ADCIRC/raw/source_code/adcirc/src/
---

# ADCIRC Storm Surge NWS Families

Date: 2026-04-12 (2026-07-10 레이어 정리)

Purpose:
- compare the main meteorological forcing families relevant to storm-surge work

리더 인덱스 성격의 비교 노트. 각 포맷의 reader 경로·file:line 은
[[adcirc-met-forcing-implementation]] (NWS=2/12/13/14/15 reader, wind drag, inverse barometer) 및
[[adcirc-storm-surge]] §D(NWS family 표) 가 canonical.

## Scope

This is still a foundation note.

It compares forcing families and data requirements.
It does not choose final project parameter values.

## Main Families Relevant To Storm Surge

(포맷 서술 출처: `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst`)

### `NWS=3`

- type: US Navy Fleet Numeric 포맷 wind file — lon/lat 격자에서 ADCIRC grid 로 공간보간, Garret 식 wind stress (rst:248-249)
- useful for: simpler wind-run style examples
- official example: APES Wind Run (`examples/index.rst:26`)

### `NWS=4`

- type: PBL/JAG 포맷 wind/pressure at selected ADCIRC grid nodes (rst:251-252)
- useful for: older storm event examples such as Hurricane Isabel (`examples/index.rst:28`)
- limitation: legacy/example-oriented

### `NWS=13`

- type: OWI-style NetCDF gridded wind and pressure — **코드 정본** `read_input.F:1782`(owiWindNetcdf namelist 필수)·`:4721`("OWI Netcdf (NWS13) format wind/pres used")
- useful for: high-quality gridded forcing with overlays, curvilinear grids, and irregular timesteps
- reader 경로·namelist 요건: [[adcirc-met-forcing-implementation]] §D (owiwind_netcdf.F file:line 인용)
- ★code≠docs: `nws_parameters.rst:308-310` 은 NWS=13 을 "NWS=5 유사 + ramping(WRAMP)" 으로 서술 — 코드와 divergent(stale). [[adcirc-storm-surge-foundation]] 판정 참조.

### `NWS=20`

- type: Generalized Asymmetric Holland Model
- useful for: parametric tropical cyclone forcing — 공식 문서가 NWS=19 를 명시적으로 비권장: `nws_parameters.rst:32` verbatim "Use of the Dynamic Asymmetric Holland Model (NWS=19) is discouraged. The Generalized Asymmetric Holland Model (NWS=20) provides improved functionality."
- strength: compact forcing representation for hurricane workflows
- 상세: [[adcirc_gahm_vortex_model]]

### `NWS=-14` / `NWS=14`

- type: GRIB2 or NetCDF gridded wind and pressure — 표준화 기상 포맷 직접 읽기, `NWS=14` cold-start 기준/`-14` hot-start 기준 (rst:311-312)
- useful for: more generic gridded forcing workflows
- strength: broad compatibility with gridded products
- limitation: different configuration path from the OWI-NWS13 convention

## `NWS=13` Facts (docs 귀속 — 인용 소급)

아래 사실은 [[adcirc-met-forcing-implementation]] §D 가 소스 file:line 로 커버:
- `NWS=13` is the OWI NetCDF format for gridded wind and pressure
- it supports moving storm-centered grids, overlays, arbitrary and irregular timesteps, and curvilinear grids
- ADCIRC expects an OWI-NWS13-style NetCDF structure and a matching `&owiWindNetcdf` namelist in `fort.15`

## Layered Separation (구조 원칙)

storm surge forcing 은 세 레이어로 분리해 다루는 것이 유지보수에 유리:
- forcing source layer — 기상 자료 원천 (예: 재분석·수치예보 격자장)
- ADCIRC forcing interface layer — `NWS` 포맷 계약 (예: `NWS=13`)
- conversion layer — 원천 자료를 ADCIRC-readable 포맷으로 매핑하는 전처리

This separation is important because:
- source availability problems belong to the forcing source layer
- NetCDF schema problems belong to the conversion layer
- ADCIRC run interpretation belongs to the interface and model layers

## Official `NWS=13` Requirements

([[adcirc-met-forcing-implementation]] §D 소급)
- OWI-NWS13 conventions in the NetCDF file
- wind fields `U10`, `V10`
- pressure field `PSFC`
- time dimension with valid units
- `lat` and `lon` variables
- group ordering and ranking if overlays are used
- `fort.15` namelist `&owiWindNetcdf`

## Next Step

- ~~`[source-needed]` 잔여 인용(NWS=19 deprecation 문서 identity) 보강 후 verified 재승격 검토~~ — **완료(2026-07-10)**: nws_parameters.rst 인용 보강 + verified 재승격
- 개인 워크플로(JMA-MSM 경로)는 `_staging/from-canonical/adcirc-nws13-jma-msm-local-workflow.md` 에서 experience 게이트 대기
