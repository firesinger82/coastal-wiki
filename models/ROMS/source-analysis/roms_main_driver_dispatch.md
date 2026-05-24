---
title: "ROMS Drivers/ + Master/ — 46 driver headers + ESMF coupler dispatch"
topic: roms-main-driver-dispatch
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Drivers/ 디렉토리 (46 files) + roms/Master/ ESMF coupler 직접 ls. Driver header naming convention (ad/adsen/afte/correlation/fsv/fte/hessian_op/hessian_so/i4dvar/jedi/nl roms.h) + Master ESMF interface files 직접 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — 디렉토리 ls 직접 확인"
verification_date: 2026-05-24
related:
  - models/ROMS/source-analysis/roms_barotropic_2d.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/source-analysis/roms_4dvar.md
  - models/ROMS/source-analysis/roms_nonlinear_physics_modules.md
---

# ROMS Main Driver Dispatch — Drivers/ + Master/

> 출처: [`models/ROMS/raw/source_code/roms/ROMS/Drivers/`](../raw/source_code/roms/ROMS/Drivers/) (46 files) + [`models/ROMS/raw/source_code/roms/Master/`](../raw/source_code/roms/Master/) 직접 디렉토리 구조.

## 1. Drivers/ — 46 driver headers 분류

ROMS 의 **운영 모드** 마다 별도 driver header (`*.h`) 가 존재. `ROMS/Drivers/` 디렉토리에 46 파일 (CMakeLists·Module.mk 포함).

### 1.1 Forward (Nonlinear) drivers

| Driver | 역할 |
|---|---|
| `nl_roms.h` | **Nonlinear forward** — 일반 hindcast/forecast 실행. 가장 흔한 모드 |

### 1.2 Adjoint family (데이터 동화)

| Driver | 역할 |
|---|---|
| `ad_roms.h` | **Adjoint** — sensitivity analysis |
| `adsen_roms.h` | Adjoint sensitivity (별도 변종) |
| `afte_roms.h` | Adjoint Finite-Time Eigenmodes |
| `fte_roms.h` | Forward Finite-Time Eigenmodes |
| `fsv_roms.h` | Forcing Singular Vectors |

### 1.3 4D-Var family

| Driver | 역할 |
|---|---|
| `i4dvar.F` + `i4dvar_roms.h` | **Incremental 4DVAR** — operational data assimilation. [[roms_4dvar]] |
| `r4dvar.F` (likely) | Strong constraint 4DVAR |
| `correlation.h` | Correlation length scale (background error) |
| `hessian_op_roms.h` + `hessian_so_roms.h` | Hessian-Optimal / Hessian Singular vectors |

### 1.4 JEDI integration

| Driver | 역할 |
|---|---|
| `jedi_roms.h` | **JEDI (Joint Effort for Data Assimilation)** 통합 — ROMS-JEDI repo connector |

### 1.5 Special-purpose

| Driver | 역할 |
|---|---|
| `array_modes.h` | Array Modes (배열 mode analysis) |

(46 file 중 나머지는 build artifact, variant configuration 등)

## 2. Driver 선택 메커니즘

각 driver header 는 CPP 매크로로 활성화. 일반 hindcast 운영 시:

```
#define NONLINEAR  # → nl_roms.h 사용
#undef ADJOINT
#undef IS4DVAR
...
```

4DVAR 운영 시:
```
#define IS4DVAR  # → i4dvar.F + i4dvar_roms.h
#define ADJOINT  # adjoint kernel 활성
```

상세 — myroms.org Wiki "CPP Options" 페이지 참조 ([[../web-refs/roms-official-resources]]).

## 3. Master/ — ESMF coupler entry

`Master/` 디렉토리는 **ESMF (Earth System Modeling Framework) coupler** + standalone main 엔트리:

| 파일 | 역할 |
|---|---|
| `coupler.F` | ESMF coupler 메인 entry |
| `cmeps_roms.h` | CMEPS (Community Mediator for Earth Prediction Systems) interface |
| `esmf_atm.F` | Atmosphere ESMF interface 일반 |
| `esmf_atm_wrf.h` | **WRF coupling** — WRF 대기 모델과 결합 |
| `esmf_atm_coamps.h` | COAMPS 대기 모델 coupling |
| `esmf_atm_regcm.h` | RegCM coupling |
| `esmf_atm_void.h` | Atmosphere void (대기 외부 forcing 없이 단독) |

→ ROMS 의 **multi-model coupling** 은 ESMF 표준 기반. 본 위키 보유 `raw/source_code/WRF/` 가 WRF coupling reference.

## 4. Split-explicit time-stepping (Shchepetkin & McWilliams 2005 의 핵심)

ROMS 의 가장 큰 수치적 특징:

- **2D barotropic** (fast mode) — 외력 + free surface, small Δt
- **3D baroclinic** (slow mode) — 운동량 + transport, large Δt
- 두 모드를 **별도 time-step** 으로 풀고 → 매 baroclinic step 마다 결과 결합

이 dispatcher 는 `nl_roms.h` driver 의 main loop 에서 호출:
- `ROMS/Nonlinear/main3d.F` (또는 main2d.F) 에서 barotropic loop ↔ baroclinic loop 분리

본 위키 — [[roms_barotropic_2d]] + [[roms_baroclinic_3d]] 가 각 mode 의 세부.

## 5. 운영 워크플로 — Hindcast 모드 (가장 흔함)

1. `cppdefs.h` 에 `#define NONLINEAR` (+ 기타 옵션 — TS_DIF2/4·UV_VIS2/4·KPP·MY25 등)
2. `nl_roms.h` driver 활성 → standalone main
3. `Master/` coupler 사용 시 ESMF coupler entry → WRF/COAMPS 결합
4. `Nonlinear/main3d.F` 가 split-explicit loop 실행 — [[roms_nonlinear_physics_modules]]
5. NetCDF history/restart/diags 출력 (Utility/)

## 6. 작성 우선순위 (남은 M-D)

- `roms_main3d_split_explicit_loop.md` — `Nonlinear/main3d.F` 의 시간-진행 loop 상세
- `roms_esmf_coupling_wrf.md` — WRF + ROMS ESMF coupler 운영 (한국 KOOS-EJS 적용 reference)
- `roms_cpp_options_decision_tree.md` — CPP 매크로 옵션 (KPP vs MY25, advection scheme 등) 운영 결정 가이드

## 7. 관련 자료

- [[roms_barotropic_2d]] — 2D barotropic mode (split-explicit fast)
- [[roms_baroclinic_3d]] — 3D baroclinic mode (split-explicit slow)
- [[roms_4dvar]] — i4dvar driver 의 동화 메커니즘
- [[roms_nonlinear_physics_modules]] — Nonlinear/ 의 physics dispatcher (신설)
- [[roms_atmospheric_forcing]] — 대기 forcing 일반 (a9618df promote)
- [[../web-refs/roms-official-resources]] — Shchepetkin-McWilliams 2005·Haidvogel 2008 인용
- [`concepts/sst/06-model-application.md`](../../../concepts/sst/06-model-application.md) — ROMS SST module + 한국 NIFS KOOS-EJS
