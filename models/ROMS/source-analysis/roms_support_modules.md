---
title: "ROMS 지원 모듈 맵 — wetdry(wet/dry mask) + floats(Lagrangian step/interp/vwalk random-walk) + set_avg/set_tides-detide(평균·출력) + exchange_2d/3d/4d(MPI halo) + ini_fields/set_zeta/post_initial(초기화) + obc_adjust/frc_adjust(adjoint) + tkebc_im(TKE BC)"
topic: roms
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/ 직접 read — wetdry.F(928 wet/dry mask 12) + step_floats.F(1055 Lagrangian, random walk 15)/interp_floats/vwalk_floats + set_avg.F(5800 평균) + exchange_2d/3d/4d.F(MPI halo) + ini_fields/set_zeta/post_initial/get_idata + obc_adjust/frc_adjust + tkebc_im(702) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — 지원 모듈 인벤토리 verbatim"
verification_date: 2026-06-04
related:
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_4dvar.md
---

# ROMS 지원 모듈 맵 (Nonlinear/)

> ROMS `Nonlinear/` 의 **지원·제어·I/O 모듈** 종합(핵심 physics solver 외). 전 소스 커버 완결용 map.

## 1. Wetting/drying — wetdry.F(928)

- `wetdry`(:21): **wet/dry masking** 계산 — `rmask_wet`/`umask_wet`/`vmask_wet`(cell/edge 침수 여부, `Dcrit` 임계수심). 침수/노출 갯벌·조간대. flux mask 로 dry cell 운동량/transport 차단. `MASKING`+`WET_DRY` CPP.

## 2. Lagrangian floats — step/interp/vwalk_floats

- `step_floats.F`(1055): **부유체(float) 궤적** 시간전진(`FLOATS` CPP) — 흐름으로 입자 advect. **vertical random walk**(`vwalk_floats.F`, 연직 확산을 무작위 보행으로) optionally. `interp_floats.F`(543): float 위치로 흐름장 보간. 입자추적·확산 진단.

## 3. 출력·평균 — set_avg.F(5800)

- `set_avg`: **시간평균 출력**(`AVERAGES` CPP) — 모든 진단변수의 출력 간격 평균 누적(5800 라인 = 전 변수 평균 코드). + `AVERAGES_DETIDE`(조석 제거, [[roms_tidal_forcing]] §3).

## 4. MPI halo 교환 — exchange_2d/3d/4d.F

- `exchange_*`(2d/3d/4d + _xtr extended): **tile boundary halo 교환**(periodic·MPI subdomain). 모든 tiled 변수의 ghost point 갱신. [[roms_main_driver_dispatch]] tiling 의 통신 primitive. (`mp_exchange` 와 연계).

## 5. 초기화 — ini_fields/set_zeta/post_initial/get_idata

- `ini_fields.F`(1085): 초기장(운동량·tracer) 설정. `set_zeta.F`: 자유표면 ζ 초기/갱신. `post_initial.F`: 초기화 후 처리. `get_idata.F`(838): 시불변 입력 자료(grid·bathymetry·nudging coef) 읽기.

## 6. Adjoint/4D-Var 보조 — obc_adjust/frc_adjust

- `obc_adjust.F`(843): open boundary 조정(TLM/ADJ 의 경계 control). `frc_adjust.F`: forcing 조정(control). [[roms_4dvar]] 의 control variable 경로(boundary·surface forcing increment).

## 7. 난류 BC — tkebc_im.F(702)

- `tkebc_im`: GLS([[roms_vertical_mixing]]) 의 **TKE(k)·length(ψ) 경계조건**(implicit). 표면/저면 wall function·flux BC.

## 8. 기타

- `hmixing.F` → [[roms_horizontal_mixing]](별도). `set_tides.F` → [[roms_tidal_forcing]](별도).

## 9. 연결

- [[roms_baroclinic_3d]] — ini_fields/set_zeta 초기화, wetdry mask
- [[roms_main_driver_dispatch]] — exchange MPI halo, tiling
- [[roms_4dvar]] — obc_adjust/frc_adjust control
- [[roms_vertical_mixing]] — tkebc_im TKE BC
- [[roms_tidal_forcing]] / [[roms_horizontal_mixing]] — set_tides/hmixing(분리 노트)
