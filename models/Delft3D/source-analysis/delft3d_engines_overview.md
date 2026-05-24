---
title: "Delft3D engines_gpl 12 엔진 개관 — flow2d3d·dflowfm·dimr·wave·waq·part 등 라인업"
topic: delft3d-engines-overview
canonical_source: self
citation_status: verified
verification_method: "models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/ 디렉토리 직접 ls + 각 엔진 sub-structure 확인. 12 engines (d_hydro·dflowfm·dimr·docs·dsle·fbc·flow2d3d·part·rr·rtc·waq·wave) 파일시스템 구조 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — 디렉토리 ls 직접 확인"
verification_date: 2026-05-24
related:
  - models/Delft3D/source-analysis/delft3d_flow2d3d_dispatcher.md
  - models/Delft3D/source-analysis/delft3d_dd.md
  - models/Delft3D/README.md
  - models/Delft3D/web-refs/delft3d-official-resources.md
---

# Delft3D `engines_gpl/` 12 엔진 개관

> 출처: [`models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/`](../raw/source_code/Delft3D/src/engines_gpl/) 직접 디렉토리 구조.

## 1. 12 엔진 라인업

D3D-4 의 `src/engines_gpl/` 아래 12 엔진 (=실행 가능 모듈) 이 존재:

| 엔진 | 역할 | 상태 (본 위키 분석) |
|---|---|---|
| **flow2d3d** | 3D hydrodynamics 메인 솔버 (TRISULA legacy) — D3D-FLOW 핵심 | [[delft3d_flow2d3d_dispatcher]] (신설 M-D 1차) |
| **dflowfm** | Flexible Mesh variant — 비구조 격자 D3D | 미분석 (M-D 2차 후보) |
| **dimr** | Delft3D Integrated Model Runner — 엔진 간 coupling 프레임워크 | 미분석 |
| **wave** | SWAN integration — flow-wave 양방향 coupling | [[wave/]] subdir 부분 분석 |
| **waq** | Water Quality (Delft3D-WAQ) — eutrophication·BOD·DO | [[delft3d_delwaq]] |
| **part** | Particle tracking (Delft3D-PART) — oil·dispersant·sediment particles | [[delft3d_part]] |
| **rtc** | Real-Time Control — 운영 시 hydraulic structure 제어 | 미분석 |
| **rr** | Rainfall-Runoff — 강수-유출 모델 | 미분석 |
| **fbc** | Flow Boundary Condition utility | 미분석 |
| **dsle** | Delft Sea-Level Equation — geoid·SLR | 미분석 |
| **d_hydro** | Hydro launcher (orchestrator entry point) | 미분석 |
| **docs** | 문서 (소스 트리 내) | nav only |

## 2. 본 위키 기존 분석 매핑

10 기존 source-analysis 노트 → 12 엔진 매핑:

| 기존 노트 | 매핑 엔진 |
|---|---|
| `delft3d_dd.md` | flow2d3d (Domain Decomposition) |
| `delft3d_delwaq.md` | waq |
| `delft3d_dredge_dump.md` | flow2d3d (sediment 모듈) |
| `delft3d_drying_flooding.md` | flow2d3d (wetting/drying) |
| `delft3d_heat.md` | flow2d3d (heat exchange) |
| `delft3d_part.md` | part |
| `delft3d_sigma_z.md` | flow2d3d (vertical layering) |
| `delft3d_turbulence.md` | flow2d3d (turbulence closure) |
| `sediment/` subdir | flow2d3d/sed |
| `wave/` subdir | wave (SWAN integration) |

→ 기존 10 노트 모두 **flow2d3d 또는 waq/part/wave 의 하위 모듈** 분석. **엔진 레벨 dispatcher 노트 신설 필요** ([[delft3d_flow2d3d_dispatcher]]).

## 3. D3D-4 vs Delft3D-FM 차이

본 위키 보유 source 는 D3D-4 + Delft3D-FM 둘 다 포함:

| 측면 | D3D-4 (flow2d3d) | Delft3D-FM (dflowfm) |
|---|---|---|
| 격자 | structured curvilinear | unstructured triangle/quad |
| Hydro solver | TRISULA (1990s) | DFM (Stelling-Kernkamp staggered) |
| Coupling | dimr 외 한정 | dimr 통합 native |
| 사용 시기 | 1990s-2010s | 2010s~ 현대 |
| 본 위키 분석 | 기존 10 노트 + 신설 | 미분석 (M-D 2차 후보) |

## 4. 주요 utility / tool 분리

`src/utils_gpl/`, `src/tools_gpl/`, `src/utils_lgpl/`, `src/plugins_lgpl/` 도 별도 디렉토리:

- `tools_gpl/` — datsel, vs, mormerge (morphology merger), nesthd1/2 (nesting), dfmoutput, vegetable utilities
- `plugins_lgpl/` — plugin_culvert, plugin_delftflow_traform (custom transport formula)

이들은 엔진과 별도 — 운영 도구.

## 5. 작성 우선순위 (남은 M-D)

| # | 후보 | 우선도 | 비고 |
|---|---|---|---|
| 1 | `delft3d_flow2d3d_dispatcher.md` | ✅ DONE 2026-05-24 | flow2d3d packages 구조 |
| 2 | `delft3d_dflowfm_overview.md` | 높음 | FM unstructured 엔진 entry — 현대 D3D-FM 사용 시 필요 |
| 3 | `delft3d_dimr_coupling.md` | 중 | coupling framework (FLOW+WAVE+WAQ 통합) |
| 4 | `delft3d_rtc_realtime_control.md` | 낮음 | hydraulic structure 제어 |
| 5 | `delft3d_wave_swan_integration.md` | 중 | wave 엔진 의 SWAN 호출 메커니즘 |

## 6. 관련 자료

- [[../README]] — Delft3D 모델 정체 카드
- [[../web-refs/delft3d-official-resources]] — 공식 + 논문 큐레이션
- [[delft3d_flow2d3d_dispatcher]] — flow2d3d 메인 솔버 dispatcher (신설)
- [[delft3d_dd]] — Domain Decomposition (flow2d3d 의 MPI 분해)
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — Delft3D-SED Van Rijn + Partheniades-Krone (cross-ref)
