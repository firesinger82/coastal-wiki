---
title: "Lynett et al. (2026) — Celeris-WebGPU 인터랙티브 nearshore wave simulator (JWPCOE)"
model: Celeris
doc: web-ref
canonical_source: external
citation_status: verified
verification_method: "raw/source_code/Celeris-WebGPU/docs/lynett-et-al-2026-...pdf 첫 페이지를 pdftotext -f 1 -l 1 로 추출하여 제목·전체 저자·소속·초록·DOI·저널 권/호/논문번호·투고/승인/게재일을 직접 인용. 기존 celeris-official-resources.md §2.4 및 celeris-coulwave-theory.md 와 cross-ref."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/Celeris/README.md
  - models/Celeris/web-refs/celeris-official-resources.md
  - models/Celeris/web-refs/celeris-coulwave-theory.md
---

# Lynett et al. (2026) — Celeris-WebGPU 인터랙티브 nearshore wave simulator

> **Celeris-WebGPU (version 1)**은 브라우저 기반 인터랙티브 nearshore wave 시뮬레이터로, **연안공학 설계와 자연재해 교육**을 지원한다. 두 가지 depth-integrated phase-resolving 모델을 구현한다 — (1) **standard mode**: 약비선형·약분산용 *enhanced Boussinesq* 방정식, (2) **high-order mode**: 정확도 향상을 위한 *완전비선형 확장(extended) Boussinesq* 방정식. 두 모드 모두 **hybrid finite-volume–finite-difference** 기법을 쓰며, standard는 공간 2차, high-order는 4차 정확도. 시뮬레이션·시각화 파이프라인 전체가 **WebGPU**를 통해 GPU에서 구동되어, 웹 브라우저 안에서 일반 데스크탑 하드웨어로 **faster-than-real-time** 성능을 낸다. (초록 발췌, p.04026007-1)

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

- 초록의 모드 구분(모드1 = enhanced/Madsen·Sørensen 계열 약비선형, 모드2 = 완전비선형 확장 Boussinesq)은 본 위키가 소스코드 정독으로 도출한 결론과 **독립 일치**한다. → [`celeris-coulwave-theory.md`](celeris-coulwave-theory.md) §0 (모드1=Madsen / 모드2=완전비선형).
- "hybrid finite-volume–finite-difference" 및 GPU faster-than-real-time 특성은 Celeris 계보의 일관된 설계 철학. → 아래 §4.

## 4. Celeris 논문 계보에서의 위치

| 세대 | 논문 | 플랫폼 | 본 노트 관계 |
|---|---|---|---|
| 원판 | Tavakkol & Lynett (2017) *Comput. Phys. Commun.* **217**:117-127 | C#/HLSL Direct3D (Windows) | 최초 interactive Boussinesq 플랫폼 |
| VR판 | Tavakkol & Lynett (2020) *Comput. Phys. Commun.* **248**:106966 | Unity3D + VR | WebGPU판 직전 세대 |
| **현행** | **Lynett et al. (2026) JWPCOE 152(4):04026007** | **브라우저 / WebGPU** | **← 본 노트** |

상세 서지·링크: [`celeris-official-resources.md`](celeris-official-resources.md) §2.1–2.4.

## 5. 인용 위치 출처

- 모든 인용은 동봉 PDF 첫 페이지(`raw/source_code/Celeris-WebGPU/docs/lynett-et-al-2026-an-interactive-nearshore-wave-simulator-for-rapid-design-prototyping-and-natural-hazard-education.pdf`, p.04026007-1)에서 직접 추출. Abstract·Practical Applications·Author keywords·저자 footnote·게재 정보(Note 단락) 모두 1면 내.
- Author keywords (verbatim): "Nearshore wave simulation; WebGPU; Interactive coastal modeling; Boussinesq equations; GPU acceleration; Coastal engineering design; Rapid prototyping; Natural hazard education."
