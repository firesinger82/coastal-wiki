# models/Celeris

> **Canonical source**: 이 디렉토리(`models/Celeris/`)가 Celeris 모델의 구현·메커닉에 대한 진실의 원천. `concepts/waves/06-model-application.md` 등은 여기로의 링크만 가짐.
>
> ⚠️ **현재 상태(2026-06-12 신설)**: source-analysis·manual-notes 미작성 — **본 위키에 소스 미확보**. README 정체카드 + web-refs(공식 GitHub·논문)는 verified(공개 출처 인용), 내부 알고리즘 분석은 소스 확보 후.

## 정체 카드

- **이름**: **Celeris** (Celeris Base/Advent → 최신 **Celeris-WebGPU**)
- **저자/관리주체**: **Sasan Tavakkol · Patrick J. Lynett** (University of Southern California, Lynett Wave Research)
- **라이선스**: open-source
- **공식 사이트**: [celeria.org](https://www.celeria.org/about)
- **GitHub (WebGPU)**: [plynett/plynett.github.io](https://github.com/plynett/plynett.github.io) — 브라우저 WebGPU 구현
- **원판**: C#/HLSL, **Direct3D** GPU (Windows), 최소 준비로 실행
- **소스 위치 (본 위키)**: ❌ 미확보 (`raw/source_code/` 없음)
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
| `source-analysis/` | ❌ 미작성 | 소스 미확보 — WebGPU GitHub clone 후 작성 |
| `manual-notes/` | ❌ 미작성 | celeria.org 문서 후보 |
| `web-refs/` | ✅ 1 verified | celeris-official-resources (사이트·GitHub·논문) |

## 본 위키에서의 핵심 활용

- [`models/FUNWAVE/`](../FUNWAVE/) — 동일 위상해상 Boussinesq(배치 vs 실시간 운용 대비)
- [`concepts/waves/`](../../concepts/waves/) — phase-resolving Boussinesq(SWAN 위상평균 대비)
- [`models/XBeach/source-analysis/xbeach_nonh.md`](../XBeach/source-analysis/xbeach_nonh.md) — Boussinesq-type 계열
