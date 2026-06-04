---
title: "EFDC 보조 모듈 맵 — calstepd(dynamic dt CFL) + calvegser(식생 시계열) + cellmask(셀 mask) + negdep(음수수심) + mhkpwr(MHK 터빈) + mod_fields(field) + runcontrol + 로그/유틸(showval/timelog/tmsr/welcome)"
topic: efdc
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/ 직접 read — calstepd.f90(387 dynamic dt) + calvegser.f90(69) + cellmask.f90(358) + negdep.f90(311) + mhkpwr.f90(324) + mod_fields.f90(585) + runcontrol.f90(71) + showval/timelog/tmsr/welcome 헤더 file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — 보조 모듈 인벤토리 verbatim"
verification_date: 2026-06-04
related:
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/source-analysis/efdc_wetdry.md
---

# EFDC 보조 모듈 맵

> EFDC+ 최상위의 **보조·제어·유틸 모듈** 종합(물리 solver 외). 전 소스 커버 완결용 map.

## 1. 시간·안정성

- **calstepd.f90**(387): **dynamic time step** — Courant(CFL) 조건으로 `DTDYN` 산출(`ISDYNSTP`). 격자/유속/수심으로 안정 dt 계산, time step 적응(빠른 흐름·얕은 셀 제약). [[efdc_hydro_core]] 의 시간적분 안정.
- **negdep.f90**(311): **음수 수심 처리** — wetting/drying 또는 강한 flux 로 수심이 음수 되는 것 방지(질량 보정·재분배). [[efdc_wetdry]] 보조.

## 2. 격자·셀

- **cellmask.f90**(358): cell **활성/비활성 mask** 설정(LMASKDRY·land/water·boundary type). 계산영역 정의(LA active cell). 격자 전처리.
- **mod_fields.f90**(585): field 변수 module(공간장 자료구조·할당).

## 3. 외력·물리 옵션

- **calvegser.f90**(69): **식생(vegetation) 시계열** 입력(시변 식생밀도/높이). vegetation drag 외력의 time series.
- **mhkpwr.f90**(324): **MHK(Marine Hydrokinetic) 터빈 전력** — 조류/해류 터빈의 운동량 흡수(drag) + 전력 산출. tidal/current energy 응용.

## 4. 제어·로그·유틸

- **runcontrol.f90**(71): run control(시뮬레이션 흐름 제어 플래그).
- **showval.f90 / timelog.f90 / tmsr.f90 / welcome.f90**: 화면 출력(진행률·값 표시) / 시간 로깅 / timer / 시작 배너. 진단·로그 유틸.

## 5. 서브디렉토리 모듈 (Transport/ · Utilities/)

- **`Transport/coare36.f90`**(639): **COARE 3.6 bulk flux 알고리즘**(Fairall et al.) — 풍속·기온·습도·SST 로 air-sea 운동량(wind stress)·잠열·현열 flux 계산. ROMS [[../../ROMS/source-analysis/roms_bulk_flux_coare]] 와 동일 계열. EFDC heat budget(temperature 모듈, raw manual `Surface_Heat_Exchange`)의 표면 flux 산출 — heat 전용 source-analysis 노트 미작성(후속).
- **`Transport/mod_diffuser.f90`**(1780): **diffuser/outfall(점 배출구) 모델** — 산업·하수 방류 diffuser 의 jet momentum·부력 plume → 운동량/scalar source. near-field 희석.
- **`Transport/calsft.f90`**(351): surface flux 시계열(scalar 표면 flux 입력).
- **`Utilities/mod_xyijconv.f90`**(491): **xy(물리좌표)↔ij(격자 index) 변환** — 관측위치·track·diffuser 위치를 격자 cell 로 매핑(좌표 변환 유틸).

## 6. 연결

- [[efdc_hydro_core]] — calstepd dynamic dt, mod_fields 자료구조
- [[efdc_wetdry]] — negdep·cellmask wet/dry
- coare36 air-sea flux → EFDC temperature/heat 모듈(전용 source-analysis 노트 미작성, raw manual `Surface_Heat_Exchange`)
- [[efdc_vertical_turbulence]] / [[efdc_external_mode_solver]] — 본 보조가 지원하는 핵심 solver
