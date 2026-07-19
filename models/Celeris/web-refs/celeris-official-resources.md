---
title: "Celeris 공식 자료·핵심 논문"
model: Celeris
citation_status: verified
source: "celeria.org + GitHub + arxiv landing-page (WebFetch/WebSearch 2026-06-12). 권·페이지·arxiv ID는 직접 확인분. [2026-06-15 추가: §2.3 Celeris Base 2020 Comput. Phys. Commun. 248:106966(ADS 2020CoPhC.24806966T) + §2.4 Lynett et al. 2026 JWPCOE 152(4) doi:10.1061/JWPED5.WWENG-2370 — WebSearch 확인.]"
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
- **Tavakkol, S., **Son, S.**, Lynett, P. (2019)** "Adaptive Third Order Adams-Bashforth Time Stepping for Extended Boussinesq Equations." arxiv: [1909.04153](https://arxiv.org/abs/1909.04153).

### 2.3 Celeris Base (Unity3D/VR 판) — ✅ verified (Comput. Phys. Commun.)
- **Tavakkol, S., Lynett, P. (2020)** "Celeris Base: An interactive and immersive Boussinesq-type nearshore wave simulation software." *Computer Physics Communications* **248**:106966. ADS: 2020CoPhC.24806966T. — Unity3D + C#/HLSL compute shader, **VR 헤드셋·360° 비디오·지도 오버레이·실시간 게이지**. 확장 Boussinesq를 hybrid FV-FD로 GPU 풀이. WebGPU판의 직전 세대.

### 2.4 Celeris-WebGPU (현행 브라우저판) — ✅ verified (JWPCOE)
- **Lynett, P. et al. (2026)** "An Interactive Nearshore Wave Simulator for Rapid Design Prototyping and Natural Hazard Education." *J. Waterway, Port, Coastal, and Ocean Engineering* **152**(4). DOI: [10.1061/JWPED5.WWENG-2370](https://doi.org/10.1061/JWPED5.WWENG-2370) (2026-04-03). — 본 위키가 분석한 **Celeris-WebGPU**(브라우저)의 논문. ★초록이 **두 위상해상 모델 = Madsen & Sørensen enhanced Boussinesq + 완전비선형 확장 Boussinesq, modern FV scheme**으로 명시 — 본 위키 소스 정독 결론([`celeris-coulwave-theory.md`](celeris-coulwave-theory.md) §0 모드1=Madsen·모드2=완전비선형)과 **독립 일치**. (repo `docs/lynett-et-al-2026-...pdf` 동봉.)

## 3. 본 위키 cross-ref

- 정체·분류: [`../README.md`](../README.md) — GPU 실시간 위상해상 Boussinesq
- 동일 class: [`../../FUNWAVE/`](../../FUNWAVE/) (배치 HPC vs 실시간 운용 대비)

## 4. 관련 노트 (보강 완료 2026-06-15)

- ✅ WebGPU clone → `raw/source_code/Celeris-WebGPU/` + **source-analysis 9 노트**(확장 Boussinesq flux·moving shoreline·AB3·PCR·WGSL): [`../source-analysis/`](../source-analysis/)
- ✅ 상류 `docs/architecture` → **manual-notes**: [`../manual-notes/celeris-architecture-and-config.md`](../manual-notes/celeris-architecture-and-config.md)
- ✅ COULWAVE 고차 분산 이론 계보: [`celeris-coulwave-theory.md`](celeris-coulwave-theory.md)
