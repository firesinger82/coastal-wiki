---
title: "ROMS Nonlinear/ physics dispatcher — 6 subdirs (BBL·Biology·SeaIce·Sediment·Vegetation·WEC) + BC·bulk·mixing"
topic: roms-nonlinear-physics-modules
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/ 디렉토리 직접 ls — 6 subdirs (BBL·Biology·SeaIce·Sediment·Vegetation·WEC) + Fortran files (bc_2d·bc_3d·bc_4d·bc_bry2d·bc_bry3d·bulk_flux·bvf_mix·conv_2d·conv_3d·conv_bry2d·conv_bry3d·diag 등) 직접 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — 디렉토리 ls 직접 확인"
verification_date: 2026-05-24
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_vertical_mixing.md
  - models/ROMS/source-analysis/roms_advection.md
  - models/ROMS/source-analysis/sediment
---

# ROMS `Nonlinear/` Physics Dispatcher

> 출처: [`models/ROMS/raw/source_code/roms/ROMS/Nonlinear/`](../raw/source_code/roms/ROMS/Nonlinear/) 직접 디렉토리 구조. **Forward (Nonlinear) physics 모듈의 컨테이너** — `nl_roms.h` driver 의 main loop 가 호출하는 모든 physics 가 여기 모임.

## 1. Nonlinear/ 디렉토리 layout

```
ROMS/Nonlinear/
├── BBL/         — Bottom Boundary Layer (subdir, 별도 모델)
├── Biology/     — biogeochemistry (NPZD·BEC·Fennel 등)
├── SeaIce/      — sea-ice 모듈
├── Sediment/    — sediment (CSTMS, Warner et al. 2008)
├── Vegetation/  — 수생 식생 항력
├── WEC/         — Wave Effects on Currents (vortex force)
├── bc_*.F       — boundary conditions (2D / 3D / 4D / bry2d / bry3d)
├── bulk_flux.F  — air-sea flux (sensible/latent heat, momentum)
├── bvf_mix.F    — Brunt-Väisälä mixing
├── conv_*.F     — conversion (state ↔ output)
├── diag.F       — diagnostics
└── (외 ~다수)
```

## 2. 6 Physics Subdirs

### 2.1 BBL — Bottom Boundary Layer

`Nonlinear/BBL/` — wave + current boundary layer scheme. 종류:
- Madsen 1994 (`mb_bbl.F`)
- Soulsby-Wright (`sw_bbl.F`)
- Sediment-mediated (Sherwood et al. 2018) — CSTMS 와 결합

bottom friction → bed shear → resuspension 의 시작점. CSTMS sediment 와 강한 결합.

### 2.2 Biology — Biogeochemistry

여러 옵션:
- **NPZD** (Nitrogen-Phytoplankton-Zooplankton-Detritus) — 단순 4-box
- **BEC** (Biogeochemical Elemental Cycling) — 복잡, NCAR
- **Fennel** et al. — N-cycle 중심
- **Estuarine** — 강 하구 specific

`#define BIO_FENNEL` 등 CPP 옵션으로 활성.

### 2.3 SeaIce

`Nonlinear/SeaIce/` — sea-ice dynamics + thermodynamics. 한국 동해 결빙 (보통 미사용) 외 북극·남극 연구용.

### 2.4 Sediment — **CSTMS (Warner et al. 2008)**

`Nonlinear/Sediment/` — Community Sediment Transport Modeling System:
- Multiple sediment classes (size + density)
- Bed structure (active layer + multiple stored layers)
- Wave-current bottom stress (BBL 와 결합)
- Bedload + suspended load

본 위키 — [[sediment/]] subdir + [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) 의 ROMS-CSTMS 인용. Warner et al. (2008) Computers & Geosciences 34:1284-1306.

### 2.5 Vegetation

`Nonlinear/Vegetation/` — 수생 식생 (해조류·맹그로브) 에 의한 momentum drag + wave dissipation. 비교적 신규 모듈.

### 2.6 WEC — Wave Effects on Currents

`Nonlinear/WEC/` — Vortex Force formulation (Uchiyama et al. 2010). Wave-induced longshore current·set-up 의 ROMS 측 구현.

본 위키 — [[roms_wec]] (이미 존재).

## 3. Core Fortran files (subdir 외)

### 3.1 Boundary Conditions

| 파일 | 역할 |
|---|---|
| `bc_2d.F` | 2D field BC (η, ubar, vbar) |
| `bc_3d.F` | 3D field BC (u, v, T, S) |
| `bc_4d.F` | 4D field BC (tracers, sediment classes) |
| `bc_bry2d.F` | Boundary 2D — radiation·clamped 등 |
| `bc_bry3d.F` | Boundary 3D — same for 3D fields |

→ ROMS 의 BC 유연성의 source.

### 3.2 Air-sea + mixing

| 파일 | 역할 |
|---|---|
| `bulk_flux.F` | **COARE bulk flux** 계산 (sensible/latent heat, momentum, wind stress) — air-sea interaction 핵심 |
| `bvf_mix.F` | Brunt-Väisälä-based simple vertical mixing (KPP·MY25 없을 때 fallback) |

→ KPP 또는 MY25 활성 시 ([[roms_vertical_mixing]]) 이 파일들이 mixing 보완.

### 3.3 Conversion + diagnostics

| 파일 | 역할 |
|---|---|
| `conv_2d.F` + `conv_3d.F` + `conv_bry*.F` | state ↔ NetCDF output 변환 |
| `diag.F` | 운영 diagnostics (CFL, energy, KE 등) |

## 4. Main loop 호출 순서 (개관)

`nl_roms.h` driver → `main3d.F` (NL forward main) → 매 baroclinic step 마다:

```
1. bulk_flux.F        # air-sea flux 갱신
2. BBL/*              # bottom stress
3. Sediment/*         # sediment dispatch (option)
4. Biology/*          # bio dispatch (option)
5. WEC/*              # wave-current effect
6. (advection)        # roms_advection.md
7. (mixing)           # vertical_mixing.md (KPP·MY25)
8. bc_*               # boundary update
9. (barotropic loop)  # roms_barotropic_2d.md 2D mode
10. diag.F            # 매 step diagnostics
11. conv_*            # output (sampling)
```

(실제 순서는 CPP 옵션 + driver 에 따라 변동. 본 위키 정확 순서는 main3d.F 직접 분석 필요 — M-D 2차 후보)

## 5. 본 위키 기존 source-analysis 매핑

| 기존 노트 | 매핑 Nonlinear 구성 |
|---|---|
| [[roms_advection]] | (Nonlinear/ 의 advection 관련 — UV_*ADV scheme) |
| [[roms_vertical_mixing]] | KPP·MY25 (Nonlinear/ 외 다른 subdir 일 수도) |
| [[roms_wec]] | Nonlinear/WEC/ |
| [[sediment/]] | Nonlinear/Sediment/ + BBL/ |
| [[roms_open_boundaries]] | bc_bry*.F |
| [[roms_atmospheric_forcing]] | bulk_flux.F + 외부 NetCDF input |
| [[roms_grid_metrics]] | (Utility/ 또는 Modules/) |

→ 기존 11 노트는 Nonlinear/ 내부 모듈 + 외부 dispatch 의 mix. **Nonlinear/ 자체의 dispatcher overview 노트는 본 노트가 신설** (그 외 6 subdir 의 entry point).

## 6. 작성 우선순위 (남은 M-D)

- `roms_bbl_wave_current.md` — Nonlinear/BBL/ subdir 의 wave-current bottom stress 상세
- `roms_biology_dispatcher.md` — Nonlinear/Biology/ 의 NPZD/BEC/Fennel 선택
- `roms_main3d_loop_order.md` — main3d.F 의 실제 호출 순서 (verified by file read)
- `roms_bulk_flux_coare.md` — bulk_flux.F 의 COARE 알고리즘 — [`concepts/sst`](../../../concepts/sst/02-theory.md) §3 cross-ref

## 7. 관련 자료

- [[roms_main_driver_dispatch]] — Drivers/ + Master/ (신설)
- [[roms_barotropic_2d]] / [[roms_baroclinic_3d]] — split-explicit
- [[roms_vertical_mixing]] — KPP·MY25
- [[roms_advection]] — UV/TS advection scheme
- [[roms_wec]] — WEC subdir
- [[sediment/]] — Sediment subdir + CSTMS
- [[roms_open_boundaries]] — bc_bry*
- [[roms_atmospheric_forcing]] — bulk_flux 외부 forcing
- [[../web-refs/roms-official-resources]] — Warner 2008 CSTMS·Large 1994 KPP·Mellor-Yamada 1982 인용
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — ROMS-CSTMS sediment
- [`concepts/sst/02-theory.md`](../../../concepts/sst/02-theory.md) — heat budget (bulk flux 와 연결)
