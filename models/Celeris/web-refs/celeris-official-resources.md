---
title: "Celeris 공식 자료·핵심 논문"
model: Celeris
citation_status: verified
source: "celeria.org + GitHub + arxiv landing-page (WebFetch/WebSearch 2026-06-12). 권·페이지·arxiv ID는 직접 확인분. [2026-06-15 추가: §2.3 Celeris Base 2020 Comput. Phys. Commun. 248:106966(ADS 2020CoPhC.24806966T) + §2.4 Lynett et al. 2026 JWPCOE 152(4) doi:10.1061/JWPED5.WWENG-2370 — WebSearch 확인.]"
note_date: 2026-06-12
last_source_check: "2026-11-04 (recovery 대조 반영)"
verification_method: "2026-11-04 Celeris recovery 대조 보고서 반영"
---

# Celeris 공식 자료·핵심 논문

## 1. 공식 사이트·저장소 (verified)

- **공식 사이트**: <https://www.celeria.org/about>
- **GitHub (WebGPU)**: <https://github.com/plynett/plynett.github.io> — Celeris-WebGPU, 브라우저에서 WebGPU API로 확장 Boussinesq 실시간 시뮬·시각화 (설치 불필요, 호환 브라우저만)
- **2017년 Advent**: C++·HLSL·Direct3D 구현이다 (Tavakkol 2017 p.1). **2020년 Base**: C#·HLSL·Unity3D 구현이다 (Tavakkol 2020 p.1). WebGPU는 JavaScript·WGSL 구현이다 (`README.md:25`). [11-04 대조 정정]

## 2. 핵심 논문

### 2.1 Celeris (원논문) — ✅ verified
- **Tavakkol, S., Lynett, P. (2017)** "Celeris: A GPU-accelerated open source software with a Boussinesq-type wave solver for real-time interactive simulation and visualization." *Computer Physics Communications* **217**:117-127.
  - arxiv: [1611.05984](https://arxiv.org/abs/1611.05984) · ADS: 2017CoPhC.217..117T
  - **확장 Boussinesq 방정식**, hybrid finite-volume / finite-difference, **moving shoreline**, GPU(Direct3D) **faster-than-real-time**, photorealistic + colormapped 동시 시각화. coastal wave 용 최초의 interactive 모델링 플랫폼.

### 2.2 시간적분 — ✅ verified (arxiv)
- **Tavakkol, S., **Son, S.**, Lynett, P. (2019)** "Adaptive Third Order Adams-Bashforth Time Stepping for Extended Boussinesq Equations." arxiv: [1909.04153](https://arxiv.org/abs/1909.04153).

### 2.3 Celeris Base (Unity3D/VR 판) — ✅ verified (Comput. Phys. Commun.)
- **Tavakkol, S., Lynett, P. (2020)** "Celeris Base: An interactive and immersive Boussinesq-type nearshore wave simulation software." *Computer Physics Communications* **248**:106966. ADS: 2020CoPhC.24806966T. — Unity3D + C#/HLSL compute shader, **VR 헤드셋·360° 비디오·지도 오버레이·실시간 게이지**. 확장 Boussinesq를 hybrid FV-FD로 GPU 풀이. WebGPU판의 직전 세대.

이 목록은 2020 Base의 기능이다 (Tavakkol 2020 p.1·9·11). VR·360° 비디오·지도·게이지 설명은 그 이전 프로그램에 귀속한다 (Tavakkol 2020 p.1). [11-04 대조 정정]

### 2.4 Celeris-WebGPU (현행 브라우저판) — ✅ verified (JWPCOE)
- **Lynett, P. et al. (2026)** "An Interactive Nearshore Wave Simulator for Rapid Design Prototyping and Natural Hazard Education." *J. Waterway, Port, Coastal, and Ocean Engineering* **152**(4). DOI: [10.1061/JWPED5.WWENG-2370](https://doi.org/10.1061/JWPED5.WWENG-2370) (2026-04-03). 논문은 두 방정식 계열과 WebGPU 구현을 설명한다 (Lynett 2026 p.2·4). 모드 명칭과 구현 경로가 대응한다 (`js/constants_load_calc.js:36–39`; `js/main.js:1564–1571`). 관련 계보는 [celeris-coulwave-theory.md](celeris-coulwave-theory.md) §0에 정리한다. 성능·설계 수준 정확도는 논문 주장으로 귀속한다 (Lynett 2026 p.1). [11-04 대조 정정]

## 3. 본 위키 cross-ref

- 정체·분류: [`../README.md`](../README.md) — GPU 실시간 위상해상 Boussinesq
- 동일 class: [`../../FUNWAVE/`](../../FUNWAVE/) (배치 HPC vs 실시간 운용 대비)

## 4. 관련 노트 (보강 완료 2026-06-15)

- ✅ WebGPU clone → `raw/source_code/Celeris-WebGPU/` + **source-analysis 9 노트**(확장 Boussinesq flux·moving shoreline·AB3·PCR·WGSL): [`../source-analysis/`](../source-analysis/)
- ✅ 상류 `docs/architecture` → **manual-notes**: [`../manual-notes/celeris-architecture-and-config.md`](../manual-notes/celeris-architecture-and-config.md)
- ✅ COULWAVE 고차 분산 이론 계보: [`celeris-coulwave-theory.md`](celeris-coulwave-theory.md)


## 문서와 코드 차이 (11-04 대조)

코드는 plynett/plynett.github.io main `ebca435`(2026-07-20)의 Celeris-WebGPU이다. 문서는 같은 커밋의 `docs/`·`README`이다. 논문은 Tavakkol & Lynett 2017(CPC), Tavakkol & Lynett 2020(CPC), Lynett et al. 2026(JWPCOE)이다.

코드 인용의 기준 경로는 `models/Celeris/raw/source_code/Celeris-WebGPU/`이다. 결론은 행별 최종 근거의 문장과 인용을 옮긴 AI 정리이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| docs-architecture:CD1-425 | 2017 플랫폼 계보 | ` docs/architecture/REFERENCE_PAPERS.md:18 ` ` It used earlier GPU shader technology rather than browser WebGPU, but the numerical structure is recognizable in this repository. ` | <br>Tavakkol 2017 p.1은 Direct3D와 C++·HLSL을 명시한다. 이 플랫폼 차이는 WebGPU 코드의 결함이 아니다.<br>확인한 원문: `docs/architecture/REFERENCE_PAPERS.md:18`<br>`js/main.js:238–254`<br>`js/main.js:1537–1543`<br>`docs/Tavakkol_2017_Celeris_GPU_accelerated_Computer_Physics_Communications.pdf` PDF p.1(인쇄 p.117), 쪽 이미지 직접 확인<br>`git log --all --format= --name-only -- '*.cpp' '*.cs' '*.unity' '*.sln' '*.vcxproj'`: 출력 없음; `fd57bb7:shaders/Pass1.compute:1–28` | A 판 차이 | 2017 논문은 Direct3D를 사용하는 C++·HLSL 구현을 설명한다. 현재 구현은 WebGPU와 WGSL을 사용한다. 이전 구현(논문이 밝힌 구현) 기준, 그 코드는 이 저장소 이력에 없다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD1c.md)) |
| docs-architecture:CD1-431 | 2020 Base 기능 계보 | ` docs/architecture/REFERENCE_PAPERS.md:29 ` ` The 2020 Celeris Base work moved the interactive model into a more accessible application environment and emphasized user workflows such as map overlays, gauges, and immersive visualization. ` | <br>Tavakkol 2020 p.1 초록은 Unity3D·C#·HLSL과 `360° video capturing, geographic map overlays, built-in real-time gauge plotters`를 명시한다.<br>확인한 원문: `docs/architecture/REFERENCE_PAPERS.md:29`<br>`js/main.js:238–254`<br>`js/main.js:1537–1543`<br>`docs/Tavakkol_2020_Celeris_Base_interactive_Computer_Physics_Communications.pdf` PDF p.1, 쪽 이미지 직접 확인<br>`git log --all --format= --name-only -- '*.cpp' '*.cs' '*.unity' '*.sln' '*.vcxproj'`: 출력 없음; `fd57bb7:shaders/Pass1.compute:1–28` | A 판 차이 | 2020 논문은 Unity3D와 C#·HLSL을 사용하는 Celeris Base를 설명한다. 논문은 지도 중첩·실시간 계측 그래프·360° 영상 기능을 설명한다. 현재 구현은 WebGPU 브라우저 프로그램이다. 이전 구현(논문이 밝힌 구현) 기준, 그 코드는 이 저장소 이력에 없다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD1c.md)) |
| docs-architecture:CD1-1353 | Base 기능의 귀속 | ` d8157c80:models/Celeris/web-refs/celeris-official-resources.md:28 ` ` - **Tavakkol, S., Lynett, P. (2020)** "Celeris Base: An interactive and immersive Boussinesq-type nearshore wave simulation software." *Computer Physics Communications* **248**:106966. ADS: 2020CoPhC.24806966T. — Unity3D + C#/HLSL compute shader, **VR 헤드셋·360° 비디오·지도 오버레이·실시간 게이지**. 확장 Boussinesq를 hybrid FV-FD로 GPU 풀이. WebGPU판의 직전 세대. ` | §2의 논문 원문 대조 참조<br>확인한 원문: `d8157c80:models/Celeris/web-refs/celeris-official-resources.md:28`; Tavakkol 2020 PDF p.1 쪽 이미지; Lynett 2026 PDF p.2·4 쪽 이미지; `ARCHITECTURE.md:3`. | A 판 차이 | Tavakkol 2020 p.1은 Celeris Base의 Unity3D·C#·HLSL 구현을 설명한다. 이전 구현(논문이 밝힌 구현) 기준, 그 코드는 이 저장소 이력에 없다. VR·360° 비디오·지도·게이지 설명은 그 이전 프로그램에 귀속한다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD1h.md)) |
| tavakkol2017:CP1-136 | Advent·Base 언어 | `d8157c80:models/Celeris/README.md:14` `C#/HLSL` | Tavakkol 2017 p.1 `Programming language: C++, HLSL`; Tavakkol 2020 p.1 `Programming language: C#, HLSL`<br>확인한 원문: Tavakkol 2017 p.1 Program summary; Tavakkol 2020 p.1 Program summary; 위키 `d8157c80:models/Celeris/README.md:14`; `d8157c80:models/Celeris/README.md:14` | B 문서 오기 | Advent의 언어는 C++·HLSL이며 Base의 C#·HLSL과 구분한다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) |
| tavakkol2017:CP1-151 | 공식 자료의 언어 구분 | `d8157c80:models/Celeris/web-refs/celeris-official-resources.md:15` `C#/HLSL Direct3D (Windows)` | Tavakkol 2017 p.1 `Programming language: C++, HLSL`; Tavakkol 2020 p.1 `Programming language: C#, HLSL`<br>확인한 원문: Tavakkol 2017 p.1; Tavakkol 2020 p.1; 위키 `d8157c80:models/Celeris/web-refs/celeris-official-resources.md:15,28` | B 문서 오기 | 공식 자료 노트도 Advent와 Base의 언어를 나누어 적는다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) |
| tavakkol2020:CP2-007 | Advent·Base·WebGPU 플랫폼 | Tavakkol 2020 p.2 “C++ and HLSL using the Direct3D framework” | `README.md:25` `Runs entirely client-side in the browser using JavaScript and WGSL shaders via the WebGPU API—no plugins or installations required.`<br>확인한 원문: Tavakkol 2020 p.2; `README.md:25`; `fd57bb7:js/main.js:17` | A 판 차이 | Advent는 C++·HLSL·Direct3D 구현이다. Base는 Unity3D·C#·HLSL 구현이다. 현재 WebGPU는 JavaScript·WGSL 구현이다. Tavakkol 2020(CPC)의 이전 구현 기준, 그 코드는 이 저장소 이력에 없다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP2.md)) |
| tavakkol2020:CP2-163 | 원판 언어 혼동 | `d8157c80:models/Celeris/README.md:14` “**원판**: C#/HLSL, **Direct3D** GPU (Windows)” | Tavakkol 2020 p.2 “Celeris Advent is developed in C++ and HLSL using the Direct3D framework.”; p.1 Base는 Unity3D·C#·HLSL이다.<br>확인한 원문: `d8157c80:models/Celeris/README.md:14`; Tavakkol 2017 p.1; Tavakkol 2020 p.1–2; `README.md:25` | B 문서 오기 | Advent는 C++·HLSL·Direct3D 구현이다. Base는 Unity3D·C#·HLSL 구현이다. WebGPU는 JavaScript·WGSL 구현이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP2.md)) |
