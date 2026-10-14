---
title: "ROMS Nonlinear/ physics dispatcher — 6 subdirs (BBL·Biology·SeaIce·Sediment·Vegetation·WEC) + BC·bulk·mixing"
topic: roms-nonlinear-physics-modules
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/ 디렉토리 직접 ls — 6 subdirs (BBL·Biology·SeaIce·Sediment·Vegetation·WEC) + Fortran files (bc_2d·bc_3d·bc_4d·bc_bry2d·bc_bry3d·bulk_flux·bvf_mix·conv_2d·conv_3d·conv_bry2d·conv_bry3d·diag 등) 직접 인용.; 2026-10-14 ROMS recovery 대조 보고서 반영"
last_source_check: "2026-10-14 (recovery 대조 반영)"
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
├── Biology/     — biogeochemistry (NPZD·ECB·Fennel 등)
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
- 현재 생물 dispatcher에는 BEC 선택 분기가 없다. ECB는 별도 생물 모델이다 ([NT-014](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안)).
- **Fennel** et al. — N-cycle 중심
- **ECB**는 Estuarine Carbon Biogeochemistry 모델이다 (`ROMS/Nonlinear/Biology/ecb.h:11-12`). `# elif defined ECB`는 `#  include <ecb.h>`를 선택한다 (`ROMS/Nonlinear/Biology/biology.F:111-112`).

`#define BIO_FENNEL` 등 CPP 옵션으로 활성.

### 2.3 SeaIce

`Nonlinear/SeaIce/` — sea-ice dynamics + thermodynamics. 한국 동해 결빙 (보통 미사용) 외 북극·남극 연구용.

### 2.4 Sediment — **CSTMS (Warner et al. 2008)**

`Nonlinear/Sediment/` — Community Sediment Transport Modeling System:
- Multiple sediment classes (size + density)
- Bed structure (active layer + multiple stored layers)
- Wave-current bottom stress (BBL 와 결합)
- Bedload + suspended load

본 위키 — [sediment/](sediment/roms_sediment.md) subdir + [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) 의 ROMS-CSTMS 인용. Warner et al. (2008) Computers & Geosciences 34:1284-1306.

### 2.5 Vegetation

`Nonlinear/Vegetation/` — 수생 식생 (해조류·맹그로브) 에 의한 momentum drag + wave dissipation. 비교적 신규 모듈.

### 2.6 WEC — Wave Effects on Currents

`Nonlinear/WEC/` — Vortex Force formulation (Uchiyama et al. 2010). Wave-induced longshore current·set-up 의 ROMS 측 구현.

본 위키 — [roms_wec](roms_wec.md) (이미 존재).

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

`bvf_mix`는 `ANA_VMIX`와 `LMD_MIXING`이 정의되지 않고 `BVF_MIXING`이 정의된 분기에서 호출한다 (`ROMS/Nonlinear/main3d.F:533-538`; [연직혼합 노트](roms_vertical_mixing.md)). [10-14 전수 검증 정정]

### 3.3 Conversion + diagnostics

| 파일 | 역할 |
|---|---|
| `conv_2d.F` + `conv_3d.F` + `conv_bry*.F` | state ↔ NetCDF output 변환 |
| `diag.F` | 운영 diagnostics (CFL, energy, KE 등) |

## 4. Main loop 호출 순서

비선형 3D 경로는 `diag`와 `output`을 이번 적분보다 먼저 호출한다 (`ROMS/Nonlinear/main3d.F:364,600`). `diag` 내부의 계산·출력은 `IF (MOD(iic(ng)-1,ninfo(ng)).eq.0) THEN` 조건을 따른다 (`ROMS/Nonlinear/diag.F:211`).

첫 패스의 상태는 초기 상태이다. 이후 통상 출력 대상은 직전 적분의 완료 상태이다. 출력 뒤 마지막 단계 종료 조건을 만족하면 `RETURN`하므로 그 패스는 새 적분을 수행하지 않는다 ([RF1-016](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md#8-차이-결론)).

`BIOLOGY`가 참이면 `biology`를 3D 운동량 뒤에 호출한다 (`ROMS/Nonlinear/main3d.F:999,1035-1036`). `SEDIMENT`가 참이면 `sediment`를 그 뒤 위치에서 호출한다 (`ROMS/Nonlinear/main3d.F:1038-1039`). 기존 물리 과정 번호 목록을 실제 호출 순서로 사용하지 않는다 ([RF1-022](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md#6-기존-노트-대조와-수정안)). 계산 흐름도는 [같은 보고서 §4.2](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md#4-계산-흐름도)를 참조한다.

## 5. 본 위키 기존 source-analysis 매핑

| 기존 노트 | 매핑 Nonlinear 구성 |
|---|---|
| [roms_advection](roms_advection.md) | (Nonlinear/ 의 advection 관련 — UV_*ADV scheme) |
| [roms_vertical_mixing](roms_vertical_mixing.md) | KPP의 진입 모듈은 `ROMS/Nonlinear/lmd_vmix.F:2-3`이다. MY25의 예측·수정 모듈은 `ROMS/Nonlinear/my25_prestep.F:2-3`와 `ROMS/Nonlinear/my25_corstep.F:2-3`이다. [10-14 전수 검증 정정] |
| [roms_wec](roms_wec.md) | Nonlinear/WEC/ |
| [sediment/](sediment/roms_sediment.md) | Nonlinear/Sediment/ + BBL/ |
| [roms_open_boundaries](roms_open_boundaries.md) | bc_bry*.F |
| [roms_atmospheric_forcing](roms_atmospheric_forcing.md) | bulk_flux.F + 외부 NetCDF input |
| [roms_grid_metrics](roms_grid_metrics.md) | (Utility/ 또는 Modules/) |

→ 기존 11 노트는 Nonlinear/ 내부 모듈 + 외부 dispatch 의 mix. **Nonlinear/ 자체의 dispatcher overview 노트는 본 노트가 신설** (그 외 6 subdir 의 entry point).

## 6. 대조 결론의 위치

생물 모델 선택은 [biology 보고서의 NT-014·NT-015](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안)를 참조한다.
계산 흐름은 [비선형 계산 흐름 보고서 §4](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md#4-계산-흐름도)를 참조한다.
바닥 경계층·표면 강제는 [mixing-bc-forcing 보고서](../../../_staging/recovery/compare/roms-mixing-bc-forcing-vs-code.md#5-차이-결론)를 참조한다.

## 7. 관련 자료

- [roms_main_driver_dispatch](roms_main_driver_dispatch.md) — Drivers/ + Master/ (신설)
- [roms_barotropic_2d](roms_barotropic_2d.md) / [roms_baroclinic_3d](roms_baroclinic_3d.md) — split-explicit
- [roms_vertical_mixing](roms_vertical_mixing.md) — KPP·MY25
- [roms_advection](roms_advection.md) — UV/TS advection scheme
- [roms_wec](roms_wec.md) — WEC subdir
- [sediment/](sediment/roms_sediment.md) — Sediment subdir + CSTMS
- [roms_open_boundaries](roms_open_boundaries.md) — bc_bry*
- [roms_atmospheric_forcing](roms_atmospheric_forcing.md) — bulk_flux 외부 forcing
- [../web-refs/roms-official-resources](../web-refs/roms-official-resources.md) — Warner 2008 CSTMS·Large 1994 KPP·Mellor-Yamada 1982 인용
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — ROMS-CSTMS sediment
- [`concepts/sst/02-theory.md`](../../../concepts/sst/02-theory.md) — heat budget (bulk flux 와 연결)

## 문서와 코드 차이 (10-14 대조)

문서 판은 ROMS 위키 wikitext(2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json))이다. 코드 판은 원본 저장소 HEAD `57aecf58`(2026-09-18, roms-4.2 이후 4.3 개발)이다.

배정 행 5개는 [note-job-20.tsv](../../../_staging/recovery/assign/note-job-20.tsv)의 이 노트 행에서 셌다.
대조 보고서: [biology](../../../_staging/recovery/compare/roms-biology-vs-code.md)·[callflow-nonlinear](../../../_staging/recovery/flow/ROMS-callflow-nonlinear.md)·[outputs-metadata](../../../_staging/recovery/compare/roms-outputs-metadata-vs-code.md).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| biology:NT-014 | BEC 모델 주장 | `models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:55` `- **BEC** (Biogeochemical Elemental Cycling) — 복잡, NCAR` | `ROMS/Nonlinear/Biology/biology.F:109` `# if defined BIO_FENNEL`<br>`ROMS/Nonlinear/Biology/biology.F:110` `#  include <fennel.h>`<br>`ROMS/Nonlinear/Biology/biology.F:111` `# elif defined ECB`<br>`ROMS/Nonlinear/Biology/biology.F:112` `#  include <ecb.h>`<br>`ROMS/Nonlinear/Biology/biology.F:113` `# elif defined ECOSIM`<br>`ROMS/Nonlinear/Biology/biology.F:114` `#  include <ecosim.h>`<br>`ROMS/Nonlinear/Biology/biology.F:115` `# elif defined HYPOXIA_SRM`<br>`ROMS/Nonlinear/Biology/biology.F:116` `#  include <hypoxia_srm.h>`<br>`ROMS/Nonlinear/Biology/biology.F:117` `# elif defined NEMURO`<br>`ROMS/Nonlinear/Biology/biology.F:118` `#  include <nemuro.h>`<br>`ROMS/Nonlinear/Biology/biology.F:119` `# elif defined NPZD_FRANKS`<br>`ROMS/Nonlinear/Biology/biology.F:120` `#  include <npzd_Franks.h>`<br>`ROMS/Nonlinear/Biology/biology.F:121` `# elif defined NPZD_IRON`<br>`ROMS/Nonlinear/Biology/biology.F:122` `#  include <npzd_iron.h>`<br>`ROMS/Nonlinear/Biology/biology.F:123` `# elif defined NPZD_POWELL`<br>`ROMS/Nonlinear/Biology/biology.F:124` `#  include <npzd_Powell.h>`<br>`ROMS/Nonlinear/Biology/biology.F:125` `# elif defined RED_TIDE`<br>`ROMS/Nonlinear/Biology/biology.F:126` `#  include <red_tide.h>`<br>`ROMS/Nonlinear/Biology/biology.F:127` `# endif`<br>`ROMS/Nonlinear/Biology/ecb.h:11` `!  the Estuarine Carbon Biogeochemistry model (Feng et al., 2015, and  !`<br>`ROMS/Nonlinear/Biology/ecb.h:12` `!  follow-ups).                                                        !` | D | 현재 생물 dispatcher에는 BEC 선택 분기가 없다. ECB는 별도 생물 모델이다. 현재 소스 전체의 BEC·BIO_BEC 및 Biogeochemical Elemental Cycling 이름 검색에도 계산 분기가 없다. [git 판정 D1](../../../_staging/recovery/compare/ROMS-git-verify-D1.md)의 자료 도입 커밋 762eef46(2007-03-29)·dd819046(2010-01-25)과 삭제 커밋 6e084151(2021-07-23)·216282bb(2020-12-05)는 MCT 격자 자료와 NetCDF 강제 자료의 이력이다. 이 자료 이력은 BEC 계산 분기의 도입·삭제 근거가 아니다. [10-14 결론 검증 보완] [10-14 git 이력 판정] |
| biology:NT-015 | Estuarine 명칭 | `models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:57` `- **Estuarine** — 강 하구 specific` | `ROMS/Nonlinear/Biology/biology.F:111` `# elif defined ECB`<br>`ROMS/Nonlinear/Biology/biology.F:112` `#  include <ecb.h>` | C | Estuarine 설명을 ECB와 ecb.h에 연결한다. |
| callflow-nonlinear:RF1-016 | 출력·진단의 지연 위치 | `Numerical_Solution_Technique.wiki:119` `#Use the weighted time-means from depth-integrated fields to complete the corrector step for the 3-D fields to time <math>n+1</math>.` | `ROMS/Nonlinear/main3d.F:600` `CALL output (ng)`<br>`ROMS/Drivers/nl_roms.h:276` `!  Since the ROMS kernel has a delayed output and line diagnostics by`<br>`ROMS/Nonlinear/main3d.F:364` `CALL diag (ng, tile)`<br>`ROMS/Nonlinear/main3d.F:603` `IF ((FoundError(exit_flag, NoError, __LINE__, MyFile)).or.&`<br>`ROMS/Nonlinear/main3d.F:604` `&            ((iic(ng).eq.(ntend(ng)+1)).and.(ng.eq.Ngrids))) THEN`<br>`ROMS/Nonlinear/main3d.F:605` `RETURN`<br>`ROMS/Nonlinear/main3d.F:641` `CALL rhs3d (ng, tile)` | C 문서 누락 | main3d는 이번 rhs3d와 시간 적분보다 먼저 diag와 output을 호출한다. 첫 패스의 상태는 초기 상태이다. 이후 통상 출력 대상은 직전 적분의 완료 상태이다. 출력 뒤 마지막 단계 종료 조건을 만족하면 RETURN하므로 그 패스는 새 적분을 수행하지 않는다. 위키의 시간 단계 개요는 이 출력·진단 위치를 적지 않는다. [10-14 결론 검증 정정] [10-14 결론 검증 보완] |
| callflow-nonlinear:RF1-022 | 물리 과정 노트의 번호 순서 | `models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:120` `1. bulk_flux.F        # air-sea flux 갱신`<br>`models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:122` `3. Sediment/*         # sediment dispatch (option)`<br>`models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:123` `4. Biology/*          # bio dispatch (option)`<br>`models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:129` `10. diag.F            # 매 step diagnostics` | `ROMS/Nonlinear/main3d.F:364` `CALL diag (ng, tile)`<br>`ROMS/Nonlinear/main3d.F:600` `CALL output (ng)`<br>`ROMS/Nonlinear/main3d.F:999` `CALL step3d_uv (ng, tile)`<br>`ROMS/Nonlinear/main3d.F:1035` `# ifdef BIOLOGY`<br>`ROMS/Nonlinear/main3d.F:1036` `CALL biology (ng, tile)`<br>`ROMS/Nonlinear/main3d.F:1038` `# ifdef SEDIMENT`<br>`ROMS/Nonlinear/main3d.F:1039` `CALL sediment (ng, tile)` | B 문서 오기 | 물리 과정 노트의 번호 목록을 실제 호출 순서로 사용하지 않는다. 비선형 3D 경로는 diag와 output을 이번 적분보다 먼저 호출한다. BIOLOGY가 참이면 biology를 3D 운동량 뒤에 호출한다. SEDIMENT가 참이면 sediment를 그 뒤 위치에서 호출한다. [10-14 결론 검증 정정] [10-14 결론 검증 보완] |
| outputs-metadata:OMD-N029 | roms_nonlinear_physics_modules.md:129 | `source-analysis/roms_nonlinear_physics_modules.md:129` `10. diag.F            # 매 step diagnostics` | `ROMS/Nonlinear/diag.F:211` `      IF (MOD(iic(ng)-1,ninfo(ng)).eq.0) THEN`<br>`ROMS/Nonlinear/main3d.F:364` `                CALL diag (ng, tile)` | B 문서 오기 | main3d에서 diag를 호출한다. diag 내부의 계산·출력은 `MOD(iic(ng)-1,ninfo(ng)).eq.0` 조건을 따른다. 매 step에 진단을 출력한다는 뜻으로 쓰지 않는다. [10-14 결론 검증 보완] |
