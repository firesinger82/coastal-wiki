---
title: "SFINCS 소스 아키텍처 맵 — main(BMI) → sfincs_lib 시간루프(momentum→continuity) + 코어 36 모듈"
model: SFINCS
component: source/src (top-level)
canonical_source: self
citation_status: verified
verification_method: "SFINCS GitHub clone(depth-1, GPL-3.0) 소스 직접 read (raw/source_code/sfincs/source/src/). sfincs.f90(main 39줄) 전문 + sfincs_lib.f90 시간루프 call 흐름(compute_fluxes/compute_water_levels/compute_nonhydrostatic, :584/:618/:610) + source/src/ 36 모듈 파일명·역할 직접 확인. file:line 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/SFINCS/README.md
  - models/SFINCS/web-refs/sfincs-official-resources.md
---

# SFINCS 소스 아키텍처 맵

> SFINCS `source/src/`(코어 36 f90)의 골격. **reduced-complexity 복합침수** — 단순화 SWE를 staggered 격자에서 momentum→continuity 로 시간적분. 경로: `raw/source_code/sfincs/source/src/`.

## 1. main program (`sfincs.f90`, 39줄)

```fortran
program sfincs                  ! sfincs.f90:1
  use sfincs_data; use sfincs_lib
  bmi = .false.                 ! :17 standalone(비-BMI) 모드
  ierr = sfincs_initialize()    ! :20
  ierr = sfincs_update(deltat)  ! :28 (deltat<999 → end 까지 진행)
  ierr = sfincs_finalize()      ! :34
end program                     ! :39
```

→ **BMI(Basic Model Interface) 구조**: initialize / update / finalize 3-phase (`sfincs.f90:20,28,34`). standalone 은 `bmi=.false.`(:17), BMI 결합 시 `sfincs_bmi.f90` 가 외부 제어. 실제 본체는 `sfincs_lib.f90`.

## 2. 시간 루프 (`sfincs_lib.f90`)

`sfincs_update` 내 main time loop 의 핵심 호출 순서:

| 순서 | 호출 | 파일:line | 역할 |
|---|---|---|---|
| 1 | forcing update | `sfincs_lib.f90:528` | momentum·continuity 외력 갱신(매 스텝) |
| 2 | `compute_fluxes(dt)` | `:584` | **운동량(momentum) → flux** (`sfincs_momentum.f90`) |
| 3 | `compute_fluxes_over_structures` | `:600` | 수공구조물 통과 flux (`sfincs_structures.f90`) |
| 4 | `compute_nonhydrostatic(dt)` | `:610` | (옵션) 비정수압 보정 (`sfincs_nonhydrostatic.f90`) |
| 5 | `compute_water_levels(t,dt)` | `:618` | **연속(continuity) → 수위 갱신** (`sfincs_continuity.f90`) |
| — | `bathtub_compute_water_levels` | `:576` | (옵션) bathtub(정적) 모드 (`sfincs_bathtub.f90`) |

- 시간스텝 `dt = alfa * min_dt` (`:391`, min_dt 는 `sfincs_momentum` 에서 CFL 기반 계산, alfa=안정계수).
- `timestep_analysis` 옵션 시 적응 dt 진단(`sfincs_timestep_analysis.f90`, :588).
- 프로파일링: momentum(`tloopflux`)·continuity(`tloopcont`) 시간 비중 로그(:743,:756).

→ **reduced-complexity 핵심**: full SWE 의 advection 을 단순화(국소관성 LIE 류)한 momentum + continuity 의 explicit staggered 적분 → full-physics 대비 고속. (advection 항은 `sfincs_advection_diffusion.f90` 에서 옵션 처리.)

## 3. 코어 36 모듈 (`source/src/*.f90`) 분류

| 그룹 | 모듈 | 역할 |
|---|---|---|
| **driver/IO** | `sfincs`·`sfincs_lib`·`sfincs_bmi`·`sfincs_data`·`sfincs_input`·`sfincs_read`·`sfincs_ncinput`·`sfincs_ncoutput`·`sfincs_output`·`sfincs_log`·`sfincs_error`·`sfincs_date` | main·BMI·전역data·입출력(netCDF)·로그 |
| **수치 코어** | `sfincs_momentum`·`sfincs_continuity`·`sfincs_advection_diffusion`·`sfincs_nonhydrostatic`·`sfincs_timestep_analysis` | 운동량·연속·이류확산·비정수압·적응dt |
| **격자/지형** | `sfincs_domain`·`sfincs_quadtree`·`sfincs_subgrid` | 도메인·**quadtree 적응격자**·**subgrid** 지형보정(고속화 핵심) |
| **외력** | `sfincs_boundaries`·`sfincs_discharges`·`sfincs_meteo`·`sfincs_spiderweb`·`sfincs_wavemaker`·`sfincs_infiltration` | 경계·방류·기상·**spiderweb(태풍 parametric wind)**·조파·침투 |
| **파/처오름** | `sfincs_snapwave`(+`snapwave/` 9모듈)·`sfincs_runup_gauges`·`sfincs_wave_enhanced_roughness` | **SnapWave** 연안 파(IG 포함)·runup·파-조도 |
| **물리 추가** | `sfincs_structures`·`sfincs_vegetation`·`sfincs_crosssections`·`sfincs_bathtub`·`sfincs_initial_conditions` | 구조물·식생·단면·bathtub 모드·초기조건 |
| **HW** | `sfincs_openacc` | GPU(OpenACC) 가속 |

## 4. 후속 deep-dive 후보

- `sfincs_momentum`/`sfincs_continuity` — reduced SWE 이산화(LIE 형식·staggered) line-by-line
- `sfincs_subgrid` — subgrid 지형 look-up table (고속·정확도 균형의 핵심)
- `sfincs_quadtree` — 적응격자 자료구조
- `snapwave/snapwave_solver` — 연안 파 solver + infragravity(`snapwave_infragravity`)
- `sfincs_spiderweb` — 태풍 parametric wind(Holland 류) → [[../../../concepts/storm-surge/01-concept]] 외력
