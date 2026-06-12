---
title: "Celeris 공식 자료·핵심 논문"
model: Celeris
citation_status: verified
source: "celeria.org + GitHub + arxiv landing-page (WebFetch/WebSearch 2026-06-12). 권·페이지·arxiv ID는 직접 확인분."
note_date: 2026-06-12
---

# Celeris 공식 자료·핵심 논문

## 1. 공식 사이트·저장소 (verified)

- **공식 사이트**: <https://www.celeria.org/about>
- **GitHub (WebGPU)**: <https://github.com/plynett/plynett.github.io> — Celeris-WebGPU, 브라우저에서 WebGPU API로 확장 Boussinesq 실시간 시뮬·시각화 (설치 불필요, 호환 브라우저만)
- **원판**: C#/HLSL Direct3D (Windows), 최소 준비 실행

## 2. 핵심 논문

### 2.1 Celeris (원논문) — ✅ verified
- **Tavakkol, S., Lynett, P. (2017)** "Celeris: A GPU-accelerated open source software with a Boussinesq-type wave solver for real-time interactive simulation and visualization." *Computer Physics Communications* **217**:117-127.
  - arxiv: [1611.05984](https://arxiv.org/abs/1611.05984) · ADS: 2017CoPhC.217..117T
  - **확장 Boussinesq 방정식**, hybrid finite-volume / finite-difference, **moving shoreline**, GPU(Direct3D) **faster-than-real-time**, photorealistic + colormapped 동시 시각화. coastal wave 용 최초의 interactive 모델링 플랫폼.

### 2.2 시간적분 — ✅ verified (arxiv)
- **Tavakkol, S., Lynett, P. (2019)** "Adaptive Third Order Adams-Bashforth Time Stepping for Extended Boussinesq Equations." arxiv: [1909.04153](https://arxiv.org/abs/1909.04153).

## 3. 본 위키 cross-ref

- 정체·분류: [`../README.md`](../README.md) — GPU 실시간 위상해상 Boussinesq
- 동일 class: [`../../FUNWAVE/`](../../FUNWAVE/) (배치 HPC vs 실시간 운용 대비)

## 4. 미보강 (소스 확보 후)

- WebGPU GitHub clone → `raw/source_code/` + source-analysis (확장 Boussinesq flux·moving shoreline·AB3 time-step·WGSL compute shader)
- celeria.org 문서 → manual-notes (입력·시나리오 설정)
