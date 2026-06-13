---
title: "FUNWAVE-TVD 소스 맵 — 지배방정식 solver·모듈 구조·툴"
model: FUNWAVE
citation_status: verified
verification_method: "models/FUNWAVE/raw/source_code/FUNWAVE-TVD/src/*.F 직접 read (39 파일) + doc/funwave_tvd_3.0.pdf(→raw/manuals MD 변환). 라인 인용은 src 기준. 2026-06-13."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
---

# FUNWAVE-TVD 소스 맵

> FUNWAVE-TVD v3.0 소스(`raw/source_code/FUNWAVE-TVD/src/`, gitignore 로컬) 구조 분석. 정체·빌드는 [`../README.md`](../README.md)·[`funwave-build-and-blackwell-port.md`](funwave-build-and-blackwell-port.md).

## 1. 지배방정식·수치기법 (manual §2-3)

- **완전비선형 Boussinesq** (Wei-Kirby 1995 / Chen 2006), reference-level zα 속도. conservative well-balanced form(Shi et al. 2012a Cartesian / Kirby 2012 spherical).
- **MUSCL-TVD finite-volume + adaptive Runge-Kutta** 시간적분, **HLL Riemann** flux.
- **wetting-drying** moving boundary(HLL 결합), **쇄파 2방식**: viscosity(eddy viscosity) + shock-capturing(질량보존 bore).

## 2. 실행 흐름 (main.F 653줄)

```
READ_INPUT(mod_input) → INDEX → INITIALIZATION(init.F)
  → 강제력 init: TIDE/METEO/VESSEL/SEDIMENT/PRECIPITATION/TRACER (mod_*)
  → [시간루프] ESTIMATE_DT(CFL) → 강제력(VESSEL/METEO/TIDE_DATA)
       → FLUXES(MUSCL-TVD) → dispersion+tridiagonal solve → SPONGE_DAMPING → MIXING_STUFF
       → OUTPUT(io.F)
```

## 3. 모듈 맵 (39 .F, 역할별)

| 영역 | 파일 | 역할 |
|---|---|---|
| **driver** | main.F (653) | 초기화 + 시간진행 orchestration |
| **flux (TVD)** | fluxes.F (2475) · fluxes_21v/33v.F | MUSCL 재구성 + HLL Riemann flux (high-order) |
| **분산(Boussinesq)** | dispersion.F (506) · etauv_solver.F (604) · **tridiagnal.F (579)** | 분산항 + **tridiagonal solve**(η,U,V 복원) — ★연산비용 핵심(GPU=cusparse 대상, [[funwave-build-and-blackwell-port]]) |
| **쇄파** | breaker.F (354) | viscosity + shock-capturing breaking |
| **조파** | wavemaker.F (3299) | WK_IRR/WK_REG/**WK_DATA2D**(2D 스펙트럼)/INI_* (소스선·내부조파) |
| **흡수경계** | sponge.F (939) | LD + friction-type + viscous-type sponge (v2.2 sawtooth 대응) |
| **경계/마스크** | bc.F (1275) · masks.F (251) | 경계조건 + wet/dry mask |
| **미분/혼합** | derivatives.F (413) · mixing.F (305) · mixing_salatin.F | 공간미분 + subgrid mixing |
| **병렬/IO** | parallel.F (547) · mod_parallel_field_io.F · io.F (5064) · samples.F (634) · statistics.F | MPI domain decomp + 입출력 + station + 통계 |
| **nesting** | nesting.F (599) · sources.F | grid nesting + source |
| **강제력 모듈** | mod_tide·mod_meteo·mod_vessel·mod_sediment·mod_tracer·mod_precipitation·mod_foam·mod_subgrid·mod_bathy_correction·mod_time_spectra | 조석·기상·선박·표사·tracer·강수·foam·subgrid·지형보정·시간스펙트럼 |
| **전역/입력** | mod_global(461) · mod_param(93) · mod_input(351) | 전역변수·파라미터·input.txt 파서 |

## 4. 툴 (tools/)

- `input_generation/PreProcessing_FUNWAVE.m` — 도메인 설정·local↔UTM·수심 보간 (입력 생성 MATLAB)
- `read_format/read_binary.m`·`read_nc.m` — 출력(binary/NetCDF) 읽기
- `plot_googlemap/plot_google_map.m` — 결과 Google Map overlay
- `filter/` — 후처리 필터

## 5. 메뉴얼

- `raw/manuals/funwave_tvd_3.0.md` (opendataloader-pdf 변환, gitignore 로컬) — 발췌·인용은 [`../manual-notes/funwave-tvd-manual.md`](../manual-notes/funwave-tvd-manual.md)
- doc/: funwave_tvd_3.0.pdf(현행) · 2.1_manual · Intro-to-FUNWAVE-CHL-TN · funwave_code_analysis

## 6. 연결

- [`../README.md`](../README.md) · [`funwave-build-and-blackwell-port.md`](funwave-build-and-blackwell-port.md)(cusparse=tridiagnal 가속)
- 정온도 적용: [`../../../concepts/waves/06-model-application.md`](../../../concepts/waves/06-model-application.md) §1.1 · [[harbor-tranquility-kds64]]
- 동일계열: [[xbeach_nonh]] (Boussinesq-type)
