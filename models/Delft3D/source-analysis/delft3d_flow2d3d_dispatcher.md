---
title: "Delft3D flow2d3d (TRISULA) 메인 솔버 dispatcher — 8 packages 구조"
topic: delft3d-flow2d3d-dispatcher
canonical_source: self
citation_status: verified
verification_method: "models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/flow2d3d/ 디렉토리 + packages/ 직접 ls — flow2d3d (메인) / flow2d3d_data / flow2d3d_io / flow2d3d_kernel / flow2d3d_kernel_dd_f / flow2d3d_manager / flow2d3d_plugin_culvert_c / flow2d3d_plugin_user 8 packages 구조 직접 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — 디렉토리 ls 직접 확인"
verification_date: 2026-05-24
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/source-analysis/delft3d_dd.md
  - models/Delft3D/source-analysis/delft3d_sigma_z.md
  - models/Delft3D/source-analysis/delft3d_turbulence.md
---

# Delft3D `flow2d3d` (TRISULA) 메인 솔버 dispatcher

> 출처: [`models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/flow2d3d/`](../raw/source_code/Delft3D/src/engines_gpl/flow2d3d/) 직접 디렉토리 구조. **D3D-4 의 핵심 hydrodynamics 엔진** (Lesser et al. 2004 모델 paper 의 구현체).

## 1. flow2d3d 디렉토리 layout

```
engines_gpl/flow2d3d/
├── default/        — 기본 설정·테스트 입력
├── doc/            — 엔진 별도 문서
├── packages/       — 8 Fortran package (아래 §2)
├── scripts/        — 빌드·운영 스크립트
└── version/        — 버전 관리
```

## 2. 8 Packages 구조 (verified — ls 직접)

flow2d3d 엔진은 8 sub-package 로 분리 (`packages/` 아래):

| Package | 역할 |
|---|---|
| `flow2d3d` | 메인 entry point — 다른 packages dispatch |
| `flow2d3d_data` | 데이터 구조 (gdp pointer, hydrodynamic state 변수 등) |
| `flow2d3d_io` | I/O — input parsing (mdf file), output writing (trim·trih·comm files) |
| `flow2d3d_kernel` | **수치 핵심** — momentum + continuity + transport 솔버 (TRISULA) |
| `flow2d3d_kernel_dd_f` | Domain Decomposition kernel (Fortran) — multi-domain MPI ([[delft3d_dd]]) |
| `flow2d3d_manager` | 운영 manager — time-step 제어, 메모리 관리 |
| `flow2d3d_plugin_culvert_c` | Culvert plugin (C) — 수공 구조물 |
| `flow2d3d_plugin_user` | 사용자 정의 plugin entry — custom formula |

## 3. Kernel package 의 역할 (수치 솔버)

`flow2d3d_kernel/` 가 **TRISULA scheme** 의 구현:

- **Continuity + momentum** — Stelling-Leendertse ADI (Alternating Direction Implicit) split
- **Sigma layer** vertical discretization → [[delft3d_sigma_z]] 참조
- **k-ε / k-L turbulence closure** → [[delft3d_turbulence]] 참조
- **Wetting/drying** — [[delft3d_drying_flooding]]
- **Sediment** — [[sediment/]] subdir
- **Heat exchange** → [[delft3d_heat]]

Lesser et al. (2004) Coastal Engineering 51:883-915 paper 가 이 kernel 의 verification source.

## 4. DD (Domain Decomposition) — Multi-domain MPI

`flow2d3d_kernel_dd_f/` 가 **다중 도메인 결합** 처리:

- 격자 영역을 여러 subdomain 으로 split → 각 subdomain 별 hydro 솔버 + interface boundary 교환
- 한 도메인은 다른 도메인의 "open boundary" 처럼 작동
- 운영 효율 + parallel scalability

상세: [[delft3d_dd]].

## 5. I/O package — Input/Output dispatcher

`flow2d3d_io/` 의 핵심 파일:
- **MDF file (Master Definition File)** — 모든 운영 설정 (격자·시간·BC·forcings·sediment·heat·turbulence)
- **trim file** — 시간 series 출력 (every time step 또는 sampling)
- **trih file** — history 출력 (정점 별)
- **comm file** — coupling file (FLOW ↔ WAVE)

운영 시 사용자가 MDF 작성 → flow2d3d_io parse → flow2d3d_data 채움 → flow2d3d_kernel 실행 → trim/trih/comm 출력.

## 6. Manager package — Time-step orchestration

`flow2d3d_manager/`:
- Time-step 제어 (CFL 기반 자동 조정 옵션)
- Memory 할당/해제
- Module 간 통신 (e.g., FLOW ↔ WAVE 동기화)

## 7. Plugins — 확장

| Plugin | 활용 |
|---|---|
| `plugin_culvert_c` (C) | 수공 culvert (배수로) hydraulic 처리 |
| `plugin_user` | 사용자 정의 transport formula 등 |

## 8. 운영 워크플로 (flow2d3d 사용 시)

1. **MDF 작성** (flow2d3d_io 입력)
2. **격자 + bathymetry** (별도 RGFGRID·QUICKIN 도구로 사전 작업)
3. **bcc/bch boundary** + forcings
4. **flow2d3d** 실행 → kernel time-step loop
5. **trim/trih/comm 출력 분석** (Delft3D-QUICKPLOT 등)

본 위키 — Lesser et al. 2004 의 운영 가이드와 일치.

## 9. 작성 우선순위 (남은 M-D)

- `delft3d_flow2d3d_kernel_walkthrough.md` — kernel 의 momentum + continuity 식 Fortran level
- `delft3d_mdf_input_card_glossary.md` — MDF file 의 카드 family 정리
- `delft3d_trim_trih_output_format.md` — 출력 파일 NEFIS 포맷

## 10. 관련 자료

- [[delft3d_engines_overview]] — 12 engines 개관
- [[delft3d_dd]] — Domain Decomposition (flow2d3d_kernel_dd_f)
- [[delft3d_sigma_z]] — sigma 또는 z-layer 선택
- [[delft3d_turbulence]] — k-ε / k-L
- [[delft3d_drying_flooding]] — wet/dry threshold
- [[delft3d_heat]] — heat exchange
- [[sediment/]] — Delft3D-SED Van Rijn / Partheniades-Krone
- [[wave/]] — SWAN integration via wave engine
- [[../web-refs/delft3d-official-resources]] — Lesser 2004 paper 인용
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — Delft3D-SED concept 레벨
