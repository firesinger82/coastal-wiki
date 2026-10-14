---
title: "ROMS recovery 노트 반영 기록 — 작업 19"
topic: roms-recovery
canonical_source: self
citation_status: verified
last_source_check: "2026-10-14 (recovery 대조 반영)"
verification_method: "2026-10-14 ROMS recovery 대조 보고서 반영"
note_author: "Codex"
note_date: 2026-10-14
verification_by: "Codex — 배정표·보고서 결론·노트 반영 대조"
verification_date: 2026-10-14
---

# ROMS recovery 노트 반영 기록 — 작업 19

배정표는 [note-job-19.tsv](../assign/note-job-19.tsv)이다.
보고서의 최종 결론과 노트 수정안을 지정된 파일에 반영한다.
파일별 완료 기록을 아래에 덧붙인다.

## roms_utility_numerics.md

대상은 [roms_utility_numerics.md](../../../models/ROMS/source-analysis/roms_utility_numerics.md)이다.

- 추가·수정 줄 범위: `models/ROMS/source-analysis/roms_utility_numerics.md:7–8`, `models/ROMS/source-analysis/roms_utility_numerics.md:20`, `models/ROMS/source-analysis/roms_utility_numerics.md:22–23`, `models/ROMS/source-analysis/roms_utility_numerics.md:75`, `models/ROMS/source-analysis/roms_utility_numerics.md:80–91`, `models/ROMS/source-analysis/roms_utility_numerics.md:96–172`, `models/ROMS/source-analysis/roms_utility_numerics.md:184–199`, `models/ROMS/source-analysis/roms_utility_numerics.md:251–256`, `models/ROMS/source-analysis/roms_utility_numerics.md:266`, `models/ROMS/source-analysis/roms_utility_numerics.md:292`, `models/ROMS/source-analysis/roms_utility_numerics.md:310–312`, `models/ROMS/source-analysis/roms_utility_numerics.md:330`, `models/ROMS/source-analysis/roms_utility_numerics.md:334–442`.
- 차이 표는 `models/ROMS/source-analysis/roms_utility_numerics.md:337–442`에 있다.
- 넣은 행 수는 100개이다. [배정표](../assign/note-job-19.tsv)의 이 파일 행 수는 100개이다.
- 반영한 수정안 행 ID: theory-numerics:RTN-368, theory-numerics:RTN-385, theory-numerics:RTN-405, da-4dvar:DA1-814, da-representer:RT2-397, da-representer:RT2-398, inputs:RI1-1045, inputs:RI1-1046, inputs:RI1-1048, inputs:RI1-1055, tools-guides:RTG-1977, outputs-metadata:OMD-N011.
- da-4dvar:DA1-814의 TIME_CONV 조건은 유지했다.
- inputs:RI1-1045의 ASCII 입력 설명은 유지했다.
- inputs:RI1-1055의 위치 좌표 변환 설명은 유지했다.
- 넣지 않은 배정 행은 없다.

## roms_tidal_forcing.md

대상은 [roms_tidal_forcing.md](../../../models/ROMS/source-analysis/roms_tidal_forcing.md)이다.

- 추가·수정 줄 범위: `models/ROMS/source-analysis/roms_tidal_forcing.md:2`, `models/ROMS/source-analysis/roms_tidal_forcing.md:6–7`, `models/ROMS/source-analysis/roms_tidal_forcing.md:19–20`, `models/ROMS/source-analysis/roms_tidal_forcing.md:25–26`, `models/ROMS/source-analysis/roms_tidal_forcing.md:29–53`, `models/ROMS/source-analysis/roms_tidal_forcing.md:57–74`, `models/ROMS/source-analysis/roms_tidal_forcing.md:78`, `models/ROMS/source-analysis/roms_tidal_forcing.md:83–85`, `models/ROMS/source-analysis/roms_tidal_forcing.md:87–144`.
- 차이 표는 `models/ROMS/source-analysis/roms_tidal_forcing.md:88–144`에 있다.
- 넣은 행 수는 51개이다. [배정표](../assign/note-job-19.tsv)의 이 파일 행 수는 51개이다.
- 반영한 수정안 행 ID: theory-numerics:RTN-396, mixing-bc-forcing:RMF1-934, mixing-bc-forcing:RMF1-935, mixing-bc-forcing:RMF1-936, mixing-bc-forcing:RMF1-937, mixing-bc-forcing:RMF1-938.
- 넣지 않은 배정 행은 없다.

## roms_barotropic_2d.md

대상은 [roms_barotropic_2d.md](../../../models/ROMS/source-analysis/roms_barotropic_2d.md)이다.

- 추가·수정 줄 범위: `models/ROMS/source-analysis/roms_barotropic_2d.md:6–7`, `models/ROMS/source-analysis/roms_barotropic_2d.md:23`, `models/ROMS/source-analysis/roms_barotropic_2d.md:25`, `models/ROMS/source-analysis/roms_barotropic_2d.md:29–30`, `models/ROMS/source-analysis/roms_barotropic_2d.md:33–37`, `models/ROMS/source-analysis/roms_barotropic_2d.md:68–73`, `models/ROMS/source-analysis/roms_barotropic_2d.md:81–83`, `models/ROMS/source-analysis/roms_barotropic_2d.md:92–112`, `models/ROMS/source-analysis/roms_barotropic_2d.md:133–165`.
- 기존 `models/ROMS/source-analysis/roms_barotropic_2d.md:99`의 보존성 실패 단정을 삭제했다.
- 기존 `models/ROMS/source-analysis/roms_barotropic_2d.md:101`의 낮은 NDTFAST에 대한 실패 단정을 삭제했다.
- 차이 표는 `models/ROMS/source-analysis/roms_barotropic_2d.md:134–165`에 있다.
- 넣은 행 수는 26개이다. [배정표](../assign/note-job-19.tsv)의 이 파일 행 수는 26개이다.
- 반영한 수정안 행 ID: theory-numerics:RTN-382, theory-numerics:RTN-406, inputs:RI1-1061, inputs:RI1-1062, inputs:RI1-1063, callflow-nonlinear:N-03, callflow-nonlinear:RF1-019, callflow-nonlinear:RF1-020, callflow-nonlinear:RF1-029, outputs-metadata:OMD-N030.
- callflow-nonlinear:N-03의 nfast·NDTFAST 구분 문장은 유지했다.
- callflow-nonlinear:N-03의 DU_avg1·DV_avg1 결합 설명은 유지했다.
- callflow-nonlinear:N-03의 Huon·Hvom 보정 설명은 유지했다.
- callflow-nonlinear:N-03이 요청한 V 방향 대응 위치를 추가했다.
- 넣지 않은 배정 행은 없다.

## roms-coawst-wci-benetazzo-2013.md

대상은 [roms-coawst-wci-benetazzo-2013.md](../../../models/ROMS/web-refs/roms-coawst-wci-benetazzo-2013.md)이다.

- 추가·수정 줄 범위는 없다.
- 넣은 행 수는 0개이다. [배정표](../assign/note-job-19.tsv)의 이 파일 행 수는 0개이다.
- 지정 보고서의 수정안 절에 이 노트의 원문을 가리키는 행은 없다.
- 사용자 지시에 따라 이 파일을 고치지 않았다.
- 차이 절을 만들지 않았다.
- 넣지 않은 배정 행은 없다.

## 최종 대조

- [배정표](../assign/note-job-19.tsv)의 177행과 세 노트 차이 표의 177행이 파일별로 대응한다.
- 배정 행의 누락은 0개이다.
- 배정 행의 중복은 0개이다.
- 배정표 밖의 차이 행은 0개이다.
- 차이 표의 모든 행은 지정한 6열을 사용한다.
- A 행의 결론 문장은 변경 커밋과 날짜를 포함한다.
- E 행의 결론 문장은 근거 강도를 포함한다.
- 차이 표 코드 원문 칸의 현재 코드 인용 1306개를 지정 파일·줄 범위의 원문과 대조했다.
- 현재 코드 인용의 불일치는 0개이다.
- 세 노트의 상대 링크 대상은 존재한다.
- 세 노트의 기존 citation_status는 유지했다.
- 세 노트에 지정한 last_source_check와 verification_method 구절을 반영했다.
