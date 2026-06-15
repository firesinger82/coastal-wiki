# models/Celeris

> **Canonical source**: 이 디렉토리(`models/Celeris/`)가 Celeris 모델의 구현·메커닉에 대한 진실의 원천. `concepts/waves/06-model-application.md` 등은 여기로의 링크만 가짐.
>
> ✅ **현재 상태(2026-06-15 전수조사 완료)**: Celeris-WebGPU 소스(`raw/source_code/Celeris-WebGPU/`, 35 JS + 42 WGSL) clone + **source-analysis 9 노트 + manual-notes 1 노트** 작성(모두 `file:line` 인용 verified). web-refs 1 + 정체카드도 verified.

## 정체 카드

- **이름**: **Celeris** (Celeris Base/Advent → 최신 **Celeris-WebGPU**)
- **저자/관리주체**: **Sasan Tavakkol · Patrick J. Lynett** (University of Southern California, Lynett Wave Research)
- **라이선스**: open-source
- **공식 사이트**: [celeria.org](https://www.celeria.org/about)
- **GitHub (WebGPU)**: [plynett/plynett.github.io](https://github.com/plynett/plynett.github.io) — 브라우저 WebGPU 구현
- **원판**: C#/HLSL, **Direct3D** GPU (Windows), 최소 준비로 실행
- **소스 위치 (본 위키)**: ✅ `raw/source_code/Celeris-WebGPU/` (gitignore 로컬, plynett.github.io clone — `js/` 35 + `shaders/` 42 + 상류 `docs/`)
- **사용 도메인**: 위상해상 **nearshore Boussinesq** — 연안 파랑·runup·항만. ★**실시간 interactive 시뮬레이션 + 시각화**(faster-than-real-time)가 정체성
- **격자**: structured, **moving shoreline** boundary 지원
- **수치 기법**: **확장(extended) Boussinesq 방정식**, **hybrid finite-volume / finite-difference**, GPU 병렬(Direct3D → WebGPU). 시간적분 3rd-order Adams-Bashforth(adaptive, Tavakkol-Lynett 2019)

## 모델 분류 — GPU 실시간 위상해상 Boussinesq

[`models/FUNWAVE/`](../FUNWAVE/)와 **같은 위상해상 Boussinesq class**이나, Celeris의 차별점 = **GPU 위에서 solver+rendering을 함께 돌려 faster-than-real-time interactive**(사용자가 돌리는 중 지형·파랑 조작·관찰). FUNWAVE(Fortran/MPI 배치 HPC)와 운용 철학이 대비됨. SWAN(위상평균)과는 다른 class.

## 핵심 논문 (web-refs 상세)

- **Celeris**: Tavakkol, S., Lynett, P. (2017) *Computer Physics Communications* **217**:117-127 — "Celeris: A GPU-accelerated open source software with a Boussinesq-type wave solver for real-time interactive simulation and visualization" (arxiv:1611.05984, ADS 2017CoPhC.217..117T)
- **시간적분**: Tavakkol, Lynett (2019) "Adaptive Third Order Adams-Bashforth Time Stepping for Extended Boussinesq Equations" (arxiv:1909.04153)

→ 상세: [`web-refs/celeris-official-resources.md`](web-refs/celeris-official-resources.md)

## 하위 디렉토리 현황

| 경로 | 상태 | 비고 |
|---|---|---|
| `source-analysis/` | ✅ 9 verified | 아래 §소스 분석 맵 |
| `manual-notes/` | ✅ 1 verified | [celeris-architecture-and-config](manual-notes/celeris-architecture-and-config.md) — 상류 `docs/architecture` + config 레퍼런스 + 원논문 |
| `web-refs/` | ✅ 2 verified | [celeris-official-resources](web-refs/celeris-official-resources.md) (사이트·GitHub·Celeris 논문) + [celeris-coulwave-theory](web-refs/celeris-coulwave-theory.md) (분산 모드 위계 — 모드1 Madsen / 모드2 완전비선형 COULWAVE 단일층 + S/T/E 항 매핑, 2층 미구현 정정) |

## 소스 분석 맵 (source-analysis/)

> Celeris-WebGPU `raw/source_code/Celeris-WebGPU/` 전수조사 (2026-06-15). 모든 단언 `js/*.js`·`shaders/*.wgsl` `file:line` 인용. FUNWAVE([`../FUNWAVE/source-analysis/`](../FUNWAVE/source-analysis/))의 배치-HPC 대응.

| 노트 | 다루는 것 |
|---|---|
| [celeris-source-map](source-analysis/celeris-source-map.md) | 35 JS ↔ 42 WGSL 대응·모듈 표·텍스처 규약 개요 (진입점) |
| [celeris-pipeline-graph](source-analysis/celeris-pipeline-graph.md) | 타임스텝 패스 순서·모드 분기(NLSW/Bous/COULWAVE·Accuracy_mode)·AB predictor-corrector·핸들러 call graph |
| [celeris-fv-reconstruction](source-analysis/celeris-fv-reconstruction.md) | Pass0 near-dry · Pass1 MUSCL 재구성 · Pass2 HLL/HLLC/HLLEM Riemann flux |
| [celeris-boussinesq-solver](source-analysis/celeris-boussinesq-solver.md) | Pass3_Bous 분산항 + Update_TriDiag_coef + **PCR** tridiagonal 음해 (연산 핵심) |
| [celeris-coulwave](source-analysis/celeris-coulwave.md) | COULWAVE 고차 모드 — Pass3A/3B 보조패스 + COULWAVE PCR |
| [celeris-breaking-boundary](source-analysis/celeris-breaking-boundary.md) | Pass_Breaking(Kennedy eddy-viscosity) + BoundaryPass(벽·sponge·주기·조파·river·wet/dry) |
| [celeris-sediment](source-analysis/celeris-sediment.md) | SedTrans Pass1/Pass3 + UpdateBottom (Exner 지형변화, 선택) |
| [celeris-webgpu-infrastructure](source-analysis/celeris-webgpu-infrastructure.md) | 텍스처 상태 규약·바인드그룹 3-레이어·config 파생상수·진단(means/Hs/timeseries) |
| [celeris-render](source-analysis/celeris-render.md) | 렌더 파이프라인(비수치) — Copytxf32_txf16 + fragment/vertex3D + skybox |

## 본 위키에서의 핵심 활용

- **사용 동기 — 항만 정온도**: real-time interactive GPU라 정온도 항만 배치 **탐색·스크리닝**에 강함(돌리며 관찰 → 유망안만 설계 케이스 배치). [`concepts/waves/06-model-application.md §1.1`](../../concepts/waves/06-model-application.md)
- [`models/FUNWAVE/`](../FUNWAVE/) — 동일 위상해상 Boussinesq(배치 vs 실시간 운용 대비)
- [`concepts/waves/`](../../concepts/waves/) — phase-resolving Boussinesq(SWAN 위상평균 대비)
- [`models/XBeach/source-analysis/xbeach_nonh.md`](../XBeach/source-analysis/xbeach_nonh.md) — Boussinesq-type 계열
