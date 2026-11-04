---
title: "Lynett et al. (2026) — Celeris-WebGPU 인터랙티브 nearshore wave simulator (JWPCOE)"
model: Celeris
doc: web-ref
canonical_source: external
citation_status: verified
verification_method: "raw/source_code/Celeris-WebGPU/docs/lynett-et-al-2026-...pdf 첫 페이지를 pdftotext -f 1 -l 1 로 추출하여 제목·전체 저자·소속·초록·DOI·저널 권/호/논문번호·투고/승인/게재일을 직접 인용. 기존 celeris-official-resources.md §2.4 및 celeris-coulwave-theory.md 와 cross-ref. 2026-11-04 Celeris recovery 대조 보고서 반영"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/Celeris/README.md
  - models/Celeris/web-refs/celeris-official-resources.md
  - models/Celeris/web-refs/celeris-coulwave-theory.md
last_source_check: "2026-11-04 (recovery 대조 반영)"
---

# Lynett et al. (2026) — Celeris-WebGPU 인터랙티브 nearshore wave simulator

> 논문 초록은 Celeris-WebGPU를 연안공학 설계와 자연재해 교육을 위한 브라우저 기반 시뮬레이터로 설명한다 (Lynett 2026 p.1). 초록은 표준·고차 모드의 공간 정확도를 각각 2차·4차로 기술한다 (Lynett 2026 p.1). 본문은 분산 미분에 2차 유한차분을 사용한다고 기술한다 (Lynett 2026 p.3–4). 고차 재구성은 `Accuracy_mode=1`이다. 완전비선형 방정식은 `NLSW_or_Bous=2`이다 (`js/main.js:1540–1571`; `js/constants_load_calc.js:36–39`). 성능 주장은 논문에 귀속한다 (Lynett 2026 p.1). [11-04 대조 정정]

## 1. 서지 정보 (verified)

| 항목 | 값 |
|---|---|
| 제목 | *An Interactive Nearshore Wave Simulator for Rapid Design Prototyping and Natural Hazard Education* |
| 저자 | Patrick Lynett; Behzad Ebrahimi; Sangyoung Son; Sooncheol Hwang; Spicer Bak |
| 저널 | *Journal of Waterway, Port, Coastal, and Ocean Engineering* (ASCE) |
| 권/호/논문번호 | **152(4): 04026007** |
| DOI | [10.1061/JWPED5.WWENG-2370](https://doi.org/10.1061/JWPED5.WWENG-2370) |
| ISSN | 0733-950X |
| 투고 / 승인 / 게재 | 2025-06-06 / 2026-01-27 / 2026-04-03 (online) |
| Discussion 마감 | 2026-09-03 |

### 저자 소속 (첫 페이지 footnote 1–5 직접 인용)
| # | 저자 | 소속 |
|---|---|---|
| 1 | Patrick Lynett (corresponding, ORCID 0000-0002-2856-9405) | Univ. of Southern California, Civil & Environmental Eng. |
| 2 | Behzad Ebrahimi | USC, Civil & Environmental Eng. (Research Assistant) |
| 3 | Sangyoung Son (ORCID 0000-0002-2819-5140) | Korea Univ., Seoul (Civil/Environmental/Architectural Eng.) |
| 4 | Sooncheol Hwang (ORCID 0000-0003-2012-8098) | KIOST, Busan (Ocean Space Development & Energy Research) |
| 5 | Spicer Bak (ORCID 0000-0001-6586-5409) | US Army ERDC, Duck, NC |

## 2. 핵심 기여 (초록·Practical Applications 인용)

1. **브라우저 내 인터랙티브 위상해상 Boussinesq 시뮬레이터.** 설치 불필요(no installation required), WebGPU만 지원하면 임의 GPU 장치에서 구동. "running a physics-based wave simulation directly in a web browser, with no installation required" (Practical Applications).
2. **이중 모드 구조** — standard(enhanced Boussinesq, 2차) = "rapid, iterative, and interactive simulations"용 / high-order(완전비선형 extended Boussinesq, 4차) = "design-level simulations in which accuracy is paramount"용. (초록)
3. **Rapid design prototyping.** 사용자가 가상 offshore breakwater를 "paint"하면 파고·흐름 변화를 즉시 관찰 — "comparison of different designs in minutes rather than hours" (Practical Applications).
4. **자연재해 교육.** 해변 경사·주기를 바꾸며 실시간 애니메이션으로 wave run-up·연안 변형을 학습 — "reinforcing theory through visual feedback" (Practical Applications).
5. **검증 벤치마크.** ① 해변에서의 규칙파 쇄파, ② 원추형 섬에서의 solitary wave run-up, ③ Duck, North Carolina nearshore wave transformation. 추가로 Oceanside, California 앞바다 breakwater 설계 시나리오. "Results show good agreement with experimental and field data." (초록)

## 3. 본 위키 소스 분석과의 일치 (cross-ref)

- 논문의 모드 명칭과 구현 경로가 대응한다 (Lynett 2026 p.1–4; `js/constants_load_calc.js:36–39`; `js/main.js:1564–1571`). 관련 방정식 계보는 [celeris-coulwave-theory.md](celeris-coulwave-theory.md) §0에 정리한다. [11-04 대조 정정]
- 논문 초록은 hybrid finite-volume–finite-difference 기법과 faster-than-real-time 성능을 기술한다 (Lynett 2026 p.1). [11-04 대조 정정]

## 4. Celeris 논문 계보에서의 위치

| 세대 | 논문 | 플랫폼 | 본 노트 관계 |
|---|---|---|---|
| 원판 | Tavakkol & Lynett (2017) *Comput. Phys. Commun.* **217**:117-127 | C++/HLSL Direct3D (Windows) | 최초 interactive Boussinesq 플랫폼 (Tavakkol 2017 p.1) [11-04 대조 정정] |
| VR판 | Tavakkol & Lynett (2020) *Comput. Phys. Commun.* **248**:106966 | Unity3D + VR | WebGPU판 직전 세대 |
| **현행** | **Lynett et al. (2026) JWPCOE 152(4):04026007** | **브라우저 / WebGPU** | **← 본 노트** |

상세 서지·링크: [`celeris-official-resources.md`](celeris-official-resources.md) §2.1–2.4.

## 5. 인용 위치 출처

- §1의 서지와 §2의 초록·Practical Applications 인용은 동봉 PDF 첫 페이지(`raw/source_code/Celeris-WebGPU/docs/lynett-et-al-2026-an-interactive-nearshore-wave-simulator-for-rapid-design-prototyping-and-natural-hazard-education.pdf`, Lynett 2026 p.1, 인쇄 p.04026007-1)에서 추출했다. 아래 대조 표는 본문 쪽별 근거를 구분한다. [11-04 대조 정정]
- Author keywords (verbatim): "Nearshore wave simulation; WebGPU; Interactive coastal modeling; Boussinesq equations; GPU acceleration; Coastal engineering design; Rapid prototyping; Natural hazard education."


쪽별 원문은 [Lynett 2026 대조 보고서](../../../_staging/recovery/compare/celeris-lynett2026-vs-code.md)에 연결한다. 방정식은 CP3-009·012(Lynett 2026 p.2–3)에 연결한다. 쇄파는 CP3-014–018(Lynett 2026 p.3)에 연결한다. HLLC는 CP3-030(Lynett 2026 p.4)에 연결한다. 정확도·성능 조건은 CP3-054·065·077(Lynett 2026 p.7·10·12)에 연결한다. [11-04 대조 정정]

## 문서와 코드 차이 (11-04 대조)

코드는 plynett/plynett.github.io main `ebca435`(2026-07-20)의 Celeris-WebGPU이다. 문서는 같은 커밋의 `docs/`·`README`이다. 논문은 Tavakkol & Lynett 2017(CPC), Tavakkol & Lynett 2020(CPC), Lynett et al. 2026(JWPCOE)이다.

코드 인용의 기준 경로는 `models/Celeris/raw/source_code/Celeris-WebGPU/`이다. 결론은 행별 최종 근거의 문장과 인용을 옮긴 AI 정리이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| callflow:RF-024 | 2017 원판 언어 | `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:59` `C#/HLSL Direct3D (Windows)` | Tavakkol 2017 p.1 `Programming language: C++, HLSL`; Tavakkol 2020 p.1 `Programming language: C#, HLSL`<br>확인한 원문: Tavakkol 2017 p.1 초록·Program summary; Tavakkol 2020 p.1 초록·Program summary; `d8157c80:models/Celeris/README.md:14`; `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:59` | B 문서 오기 | 2017 원판은 C++·HLSL·Direct3D다. 2020 Base는 C#·HLSL·Unity3D다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) |
| docs-architecture:CD1-1357 | 재구성과 방정식 선택 | ` d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:18 ` ` > **Celeris-WebGPU (version 1)**은 브라우저 기반 인터랙티브 nearshore wave 시뮬레이터로, **연안공학 설계와 자연재해 교육**을 지원한다. 두 가지 depth-integrated phase-resolving 모델을 구현한다 — (1) **standard mode**: 약비선형·약분산용 *enhanced Boussinesq* 방정식, (2) **high-order mode**: 정확도 향상을 위한 *완전비선형 확장(extended) Boussinesq* 방정식. 두 모드 모두 **hybrid finite-volume–finite-difference** 기법을 쓰며, standard는 공간 2차, high-order는 4차 정확도. 시뮬레이션·시각화 파이프라인 전체가 **WebGPU**를 통해 GPU에서 구동되어, 웹 브라우저 안에서 일반 데스크탑 하드웨어로 **faster-than-real-time** 성능을 낸다. (초록 발췌, p.04026007-1) ` | ` js/main.js:1541 ` `         Pass1_ShaderCode = await fetchShader('/shaders/Pass1_HighOrder.wgsl'); `<br>` js/main.js:1548 ` `         Pass2_ShaderCode = await fetchShader('/shaders/Pass2_HighOrder_HLLC.wgsl');   `<br>` js/main.js:1568 ` `     else if (calc_constants.NLSW_or_Bous == 2) { `<br>` js/main.js:1570 ` `         Pass3_ShaderCode_Bous = await fetchShader('/shaders/Pass3_COULWAVE.wgsl'); `<br>확인한 원문: `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:18`; `js/main.js:1540-1571`; Lynett 2026 PDF p.1·4 쪽 이미지; `js/constants_load_calc.js:36-39`. | C 문서 누락 | 고차 재구성은 `Accuracy_mode=1`이다. 완전비선형 방정식은 `NLSW_or_Bous=2`다. 고차 모드의 모든 미분을 4차라고 쓰지 않는다. 성능 주장은 논문에 귀속한다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD1h.md)) |
| docs-architecture:CD1-1358 | 2017 계보 표 언어 | `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:59` `C#/HLSL Direct3D (Windows)` | Tavakkol 2017 p.1 `Programming language: C++, HLSL`; Tavakkol 2020 p.1 `Programming language: C#, HLSL`<br>확인한 원문: `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:59`; Tavakkol 2017 PDF p.1 쪽 이미지; Tavakkol 2020 PDF p.1 쪽 이미지. | B 문서 오기 | 2017 원판의 플랫폼은 C++·HLSL·Direct3D다. C#·HLSL·Unity3D는 2020 Celeris Base에 해당한다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD1h.md)) |
| lynett2026:CP3-003 | 공간 정확도 표현 | Lynett 2026 p.1 초록: “standard mode’s accuracy is of second-order in space, while the high-order mode’s accuracy is of fourth-order” | `js/constants_load_calc.js:39` `Accuracy_mode: 0,  // Accuracy model choice: 0: 2nd-order, 1: 4th-order.`<br>확인한 원문: Lynett 2026 p.1 초록, p.3 Spatial Discretization, p.4 공간 이산화; `js/constants_load_calc.js:36–39` | B 문서 오기 | 논문의 4차 표현은 재구성 차수와 구분한다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) |
| lynett2026:CP3-005 | 세대별 플랫폼 | Lynett 2026 p.2: “DirectX shaders”; “Unity3D game engine”; “migrates to WebGPU and JavaScript” | `js/main.js:1548` `Pass2_ShaderCode = await fetchShader('/shaders/Pass2_HighOrder_HLLC.wgsl');`<br>확인한 원문: Tavakkol 2017 p.1–2; Tavakkol 2020 p.1; Lynett 2026 p.2,4; `fd57bb7:js/main.js:32–40`; `js/main.js:1541–1548` | A 판 차이 | 2017·2020 구현과 2026 WebGPU 구현의 플랫폼 차이를 분리한다. 이전 구현(논문이 밝힌 구현) 기준, 그 코드는 이 저장소 이력에 없다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) |
| lynett2026:CP3-053 | Fig. 3(d) 사례 번호 | Lynett 2026 p.7 Fig. 3 캡션: “(d) Case 067071”; 같은 패널 제목: “Case: 061071 [kh = 0.79, ka = 0.07]” | 논문 내부 대조: 코드 대조 없이 같은 그림 안에서 확인한다.<br>확인한 원문: Lynett 2026 p.7 Fig.3(d) 제목·캡션과 본문, p.8 Fig.4 캡션 | B 문서 오기 | Fig. 3(d)의 캡션 번호 067071은 그래프·본문·Fig. 4와 맞지 않는다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) |
| lynett2026:CP3-111 | 2017 구현 언어 | `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:59` `C#/HLSL Direct3D (Windows)` | Tavakkol 2017 p.1 `Programming language: C++, HLSL`; Tavakkol 2020 p.1 `C#, HLSL`<br>확인한 원문: Tavakkol 2017 p.1 Program summary; `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:59`; `d8157c80:models/Celeris/web-refs/celeris-official-resources.md:15` | B 문서 오기 | 2017 원판의 구현 언어는 C++/HLSL이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) |
| tavakkol2017:CP1-152 | 계보 표의 2017 언어 | `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:59` `C#/HLSL Direct3D (Windows)` | Tavakkol 2017 p.1 `Programming language: C++, HLSL`<br>확인한 원문: Tavakkol 2017 p.1; Tavakkol 2020 p.1; Lynett 2026 p.1; 위키 `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:59` | B 문서 오기 | 계보 표의 2017년 행은 C++·HLSL이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) |
| tavakkol2020:CP2-177 | Advent 플랫폼 | `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:59` “C#/HLSL Direct3D (Windows)” | Tavakkol 2020 p.2 “Celeris Advent is developed in C++ and HLSL”<br>확인한 원문: `d8157c80:models/Celeris/web-refs/celeris-lynett-2026.md:59`; Tavakkol 2017 p.1; Tavakkol 2020 p.2 | B 문서 오기 | 2017 Advent의 플랫폼은 C++·HLSL·Direct3D이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP2.md)) |
