---
title: "FUNWAVE-TVD 코드 관계성 — USE 의존·CALL 그래프 (전수조사 토대)"
model: FUNWAVE
citation_status: verified
verification_method: "models/FUNWAVE/raw/source_code/FUNWAVE-TVD/src/*.F 전수 grep(USE/CALL/SUBROUTINE) + 직접 read. 규모·그래프 수치는 src 기준 집계. 2026-06-13."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
---

# FUNWAVE-TVD 코드 관계성

> 전수조사(33,760줄 / **218 subroutine** / 15 module / 414 USE / 1338 CALL)의 구조 토대. 서브루틴별 상세는 [`funwave-source-map.md`](funwave-source-map.md) + physics-core 노트(후속).

## 1. 모듈 USE 의존 (레이어링)

```
PARAM (mod_param, 상수·MPI)
  └→ GLOBAL (mod_global, 전역 배열·변수)
       └→ INPUT_READ (mod_input, input.txt 파서)
            └→ [feature 모듈] mod_tide·meteo·vessel·sediment·tracer·precipitation·subgrid·foam·bathy_correction·time_spectra
                 └→ main.F (상위 모듈 전부 use: TIDE/METEO/VESSEL/SEDIMENT/TRACER/PRECIPITATION/TIME_SPECTRA/MOD_FOAM)
```
- 모든 모듈이 `PARAM`(MPI 포함)·`GLOBAL` 의존 → **GLOBAL = 전역 상태 허브**(배열 U,V,Eta,H,depth 등 + nesting/dispersion 변수).
- 비-module .F(fluxes·dispersion·etauv_solver·bc·breaker·wavemaker·sponge·io·parallel 등)는 `USE GLOBAL`로 전역 상태 공유(F90 module + host association).
- 특이: mod_sediment→VESSEL_MODULE, mod_time_spectra→TIDE_MODULE (feature 간 의존).

## 2. CALL 그래프 — 지배 solver chain

```
main.F [시간루프]
  ├ ESTIMATE_DT (CFL)
  ├ FLUXES ───┬ CONSTRUCT_HO_X/Y (+ _MLP/_minmod/WENO 변형)   ← MUSCL 고차 재구성
  │           ├ FLUX_AT_INTERFACE_HLL ─ HLL ─ WAVE_SPEED       ← HLL Riemann flux
  │           └ CONSTRUCTION / DelxFun·DelyFun·DelxyFun         ← 재구성·미분
  ├ [분산 Boussinesq] dispersion / etauv_solver ──┬ DERIVATIVE_X/Y/XX/YY/XY   ← 분산항 고차미분
  │                                                ├ GET_Eta_U_V_HU_HV         ← η,U,V,HU,HV 복원
  │                                                ├ TRIDx / TRIDy / TRIDy_periodic (+ _ser)  ← ★tridiagonal solve
  │                                                └ EXCHANGE_DISPERSION       ← MPI halo
  ├ SPONGE_DAMPING (sponge.F)
  └ MIXING_STUFF (mixing.F)
```

## 3. CALL 허브 (관계 중심, 호출빈도)

| subroutine | 호출수 | 역할 |
|---|--:|---|
| READ_FLOAT/LOGICAL/STRING/Float | 156+83+42+35 | input.txt 파싱 (mod_input, 전 모듈이 호출) |
| **PHI_COLL** | 87 | 분산/nesting 변수 collection (bc.F; 분산 solve 전처리 허브) |
| PutFile | 92 | 출력 (io.F) |
| **CONSTRUCT_HO_X / _Y** | 39 / 39 | MUSCL 고차 재구성 (fluxes.F; flux 계산 허브) |
| DelxFun / DelyFun | 27 / 27 | 1차 미분 (derivatives.F) |
| MPI_FINALIZE/Gather | 102/29 | 병렬 (parallel.F) |

→ **물리 허브**: `CONSTRUCT_HO_*`(flux 재구성) · `PHI_COLL`(분산 수집) · `TRIDx/y`(tridiagonal 해) · `DERIVATIVE_*`(분산 미분). **인프라 허브**: READ_*(입력) · PutFile(출력) · MPI_*(병렬).

## 4. 파일별 subroutine 분포 (218개)

fluxes 23 · wavemaker 17 · fluxes_33v 17 · fluxes_21v 14 · io 13 · samples 11 · mod_meteo 10 · derivatives 10 · sponge 7 · mod_tide 7 · mod_foam_upwinding 7 · misc 7 · bc 6 · mod_tracer 6 · mod_input 6 · mod_foam 6 · tridiagnal 5 · mod_vessel 5 · mod_subgrid 5 · parallel 4 · mod_time_spectra 4 · mod_sediment 4 · init 3 · statistics 2 · nesting 2 · (그 외 main/etauv_solver/dispersion/breaker/sources/masks/mixing/mod_* 등)

## 5. 전수조사 진행 (체크리스트)

- [x] 코드 관계성 그래프 (본 노트)
- [x] 모듈 인벤토리·흐름 ([`funwave-source-map.md`](funwave-source-map.md))
- [ ] **physics-core 서브루틴별**: fluxes(MUSCL-TVD 23subr)·dispersion·etauv_solver·tridiagnal·breaker·derivatives·sources
- [ ] wavemaker(17subr) / sponge / bc / masks / init
- [ ] feature 모듈: sediment·tide·meteo·vessel·tracer·precipitation·subgrid·foam·bathy_correction·time_spectra
- [ ] 인프라: io·parallel·samples·statistics·nesting·misc

## 6. 연결

- [`funwave-source-map.md`](funwave-source-map.md) · [`funwave-build-and-blackwell-port.md`](funwave-build-and-blackwell-port.md)(TRIDx/y=GPU cusparse) · [`../manual-notes/funwave-tvd-manual.md`](../manual-notes/funwave-tvd-manual.md)
