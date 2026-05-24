---
title: "EFDC+ Theory Document Version 12 (DSI 2024) — TOC + Development History + 7 챕터 구조"
topic: efdc-theory-doc-v12
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf 표지·Acknowledgement·Contents pages 1-5 직접 추출 — EFDC+ Theory Version 12, DSI LLC (Edmonds WA), October 2024. 표지·Acknowledgement·Contents 페이지의 챕터 구조·페이지 번호·authorship 직접 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — PDF Read pages 1-5 직접 확인 (표지·Acknowledgement·Contents)"
verification_date: 2026-05-24
related:
  - models/EFDC/manual-notes/efdc-manuals-overview.md
  - models/EFDC/manual-notes/efdc-user-manual-r850.md
  - models/EFDC/manual-notes/efdc-sediment-theory-2003.md
  - models/EFDC/README.md
---

# EFDC+ Theory Document Version 12 — 이론서 reference

> 출처: [`models/EFDC/raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf`](../raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf) (DSI LLC, Edmonds WA, October 2024, 14.4 MB).

## 1. 자료 식별 + 인용 형식

| 항목 | 값 |
|---|---|
| 제목 | EFDC+ Theory |
| 버전 | Version 12 |
| 발행 | DSI LLC (Edmonds WA, www.dsi.llc) |
| 날짜 | October 2024 |
| 파일 | `EFDC_Theory_Document_Ver_12.pdf` |
| 크기 | 14.4 MB |
| 페이지 | 표지·Ack(i)·Contents(ii-iii)·List of Abbreviations(ix)·본문 ~120p+ |

**공식 인용 형식** (표지 페이지 직접):

> DSI LLC. 2024. EFDC+ Theory, Version 12. Published by DSI LLC, Edmonds WA. Available at https://www.eemodelingsystem.com/wp-content/Download/Documentation/EFDC_Theory_Document_Ver_12.pdf

## 2. Development History (Acknowledgement, p.i 직접 인용)

EFDC+ 의 authorship 계보:

| 기여자 | 기여 | 시기 |
|---|---|---|
| **Dr. John Hamrick** | 원본 EFDC 출간 (1992) — Environmental Fluid Dynamics Code | 1992 |
| Dr. Hamrick (Tetra Tech) | 다수 enhancement + documentation | 1990s-2000s |
| **Kyeong Park** + 외 | CE-QUAL-ICM (ICM) kinetics for eutrophication 초기 | — |
| **Craig Jones** | SEDiment dynamics — SEDZLJ implementation (Ziegler·Lick·Jones 알고리즘) + separate documentation | — |
| **Jeff Ji** | Rooted Plant Epiphytes Module (RPEM) + separate documentation | — |
| **Scott James** | 기타 code·documentation enhancement | — |
| **DSI LLC engineers** | EFDC+ 통합 + 속도·안정성·정확도 개선 (단일 comprehensive theory doc 통합) | 2009~ 현재 |

**DSI 의 primary contributors (2009~)** — Paul Craig, Thomas Mathis, Tran Duc Kien, Jeffrey Jung, Kester Scandrett, Anurag Mishra.

> "Since 2009, the engineers at DSI have been the primary contributors to the updates and maintenance of this document." (Acknowledgement, p.i)

> "Of course, EFDC source code has been publicly available since the early 2000s, so there have been numerous other contributors, resulting in a large number of versions of EFDC." (Acknowledgement, p.i)

## 3. Contents (pp.ii-iii, 직접 인용)

```
List of Abbreviations                                                       ix

1 INTRODUCTION                                                              1
  1.1 Development History                                                   1
  1.2 EFDC+ Advancements                                                    2
  1.3 Enhancements to EFDC+ since EEMS10.3                                  4
  1.4 EFDC+ Overview                                                        5
  1.5 Conclusion                                                            7

2 HYDRODYNAMICS                                                             8
  2.0.1 Overview                                                            8
  2.1 Governing Equations                                                   8
    2.1.1 Horizontal and Vertical Coordinate Systems                        9
    2.1.2 Basic Hydrodynamic Equations                                      10
    2.1.3 Equation of State                                                 13
    2.1.4 Vertical Turbulent Closure                                        14
    2.1.5 Horizontal Turbulence Closure                                     16
  2.2 Boundary Conditions and External Forcings                             16
    2.2.1 Bottom Friction                                                   16
    2.2.2 Vegetation                                                        17
    2.2.3 Wind Forcings                                                     19
    2.2.4 Wave Action                                                       21
    2.2.5 Local Wind-Generated Waves                                        23
    2.2.6 Harmonic Forcings                                                 25
    2.2.7 Hydraulic Structures                                              26
    2.2.8 Propeller Wash                                                    30
  2.3 Numerical Solution for the Equations of Motion                        32
  2.4 Computational Aspects of the Three Time Level External Mode Solution  37
  2.5 Computational Aspects of the Three-Time Level Internal Mode Solution  42
  2.6 Vertical Layering Options                                             46
    2.6.1 Standard Sigma (SIG) Approach                                     46
    2.6.2 Sigma-Zed Approach (SGZ)                                          47
  2.7 Near-Field Discharge Dilution and Mixing Zone Analysis                48
    2.7.1 Shear-Induced Entrainment                                         49
    2.7.2 Forced Entrainment                                                50
    2.7.3 Model Implementation                                              50
  2.8 Conclusion                                                            52

3 CONSERVATIVE CONSTITUENTS TRANSPORT                                       53
  3.1 Introduction                                                          53
  3.2 Basic Equation of Advection-Diffusion Transport                       53
  3.3 Numerical Solution for Transport Equations                            54

4 DYE MODULE                                                                57
  4.1 Decay                                                                 57
  4.2 Age of Water                                                          58

5 TEMPERATURE AND HEAT TRANSFER                                             59
  5.1 Surface Heat Exchange                                                 60
    5.1.1 Full Heat Balance                                                 60
    5.1.2 COARE 3.6 Bulk Algorithm                                          61
    5.1.3 Equilibrium Temperature                                           62
  5.2 Short Wave Radiation                                                  63
    5.2.1 One-band Light Attenuation Model                                  63
    5.2.2 Two-band Light Attenuation Model                                  64
    5.2.3 Water Quality Linked Light Attenuation                            64
  5.3 Bed Heat Exchange                                                     66
  5.4 Ice Formation and Melt                                                67
    5.4.1 Heat Balance                                                      67
    5.4.2 Ice Surface Temperature                                           68
    5.4.3 Freezing Temperature                                              68
    5.4.4 Ice Melt at Air/Water Interface                                   69
    5.4.5 Ice Growth/Melt at Bottom of Ice                                  69
    5.4.6 Solar Radiation at Bottom of Ice                                  69
  5.5 Water Volume Evaporative Losses                                       70

6 SEDIMENT TRANSPORT                                                        72
  6.1 Introduction                                                          72
  6.2 Suspended Sediment Transport                                          72
    6.2.1 Governing Equations for Suspended Sediment Transport              72
    6.2.2 Numerical Solution                                                74
  6.3 EFDC Sediment Transport Module                                        77
    6.3.1 Non-Cohesive Sediment                                             77
    6.3.2 Cohesive Sediments                                                88
    6.3.3 Consolidation of Mixed Cohesive and Non-Cohesive Sediment Beds    92
  6.4 SEDZLJ Sediment Transport Module                                      95
    6.4.1 Background                                                        95
    6.4.2 Bed Shear Stress                                                  97
    6.4.3 Erosion Rate                                                      98
    6.4.4 Suspended Load                                                    104
    6.4.5 Bedload                                                           105
    6.4.6 Bed Armoring                                                      107

7 CHEMICAL FATE AND TRANSPORT                                               110
  7.1 Development Overview                                                  111
  7.2 Basic Equations                                                       111
  ...
```

## 4. 챕터별 활용 매트릭스

### 4.1 Ch 2 HYDRODYNAMICS (p.8-52, 가장 큼)

운영 해석의 핵심:
- **§2.1.4 Vertical Turbulent Closure** (p.14) — Mellor-Yamada (MY2.5)
- **§2.2.1 Bottom Friction** (p.16) — Manning n 또는 z0 + log law
- **§2.2.2 Vegetation** (p.17) — 식생 항력 (mangrove·갈대)
- **§2.2.4 Wave Action** (p.21) — SWAN 결합 시 radiation stress
- **§2.2.8 Propeller Wash** (p.30) — Propwash WhitePaper 와 함께
- **§2.3-2.5 Three Time Level scheme** (p.32-45) — split-explicit time-stepping (external·internal mode)
- **§2.6 Vertical Layering** (p.46-47) — **SIG vs SGZ 선택**:
  - SIG (Standard Sigma) — terrain-following, 단순
  - SGZ (Sigma-Zed) — hybrid, 깊은 영역 z-level + 얕은 영역 sigma (수직 일관성)
- **§2.7 Near-Field Discharge Dilution** (p.48-51) — 방류구 mixing zone

### 4.2 Ch 5 TEMPERATURE (p.59-71)

한국 적용 (영광·고리 발전소 온배수):
- **§5.1.1 Full Heat Balance** (p.60) — net shortwave + longwave + sensible + latent
- **§5.1.2 COARE 3.6 Bulk Algorithm** (p.61) — modern air-sea flux 알고리즘 (concepts/sst 와 cross-ref)
- **§5.4 Ice Formation and Melt** (p.67-69) — 동해 결빙

### 4.3 Ch 6 SEDIMENT TRANSPORT (p.72-109, 운영 핵심)

**두 분기 모듈** — 사용자가 선택:

| 항목 | EFDC SedTran Module (§6.3) | SEDZLJ Module (§6.4) |
|---|---|---|
| 출처 | Hamrick legacy + Tetra Tech 2003 ([[efdc-sediment-theory-2003]]) | Ziegler·Lick·Jones 알고리즘 (SEDZLJ) |
| 입력 키 (ISTRAN) | ISTRAN(6)=cohesive CALSED·ISTRAN(7)=noncohesive CALSND | unified |
| Bed structure | 분리 (cohesive vs noncohesive) | unified multi-bed-layer, size-class |
| Bed Shear (§6.4.2) | — | wave+current quadratic |
| Erosion (§6.4.3) | — | Lick·Jones formulation |
| Bed Armoring (§6.4.6) | — | active layer + dynamic armoring |
| 활용 | legacy·교과서 비교 | modern operational |

source-code dispatch — [`models/EFDC/source-analysis/efdc_sediment.md`](../source-analysis/efdc_sediment.md) `ssedtox.f90:868-880`.

### 4.4 Ch 7 CHEMICAL FATE (p.110+)

Hg·PCB·toxics 의 sorption + degradation. 한국 산업 폐기물 분석에 활용 가능.

## 5. 작성 우선순위 (남은 작업)

본 노트는 **TOC + Acknowledgement + 챕터 nav** 수준. 깊이별 후속 노트 후보:

- `efdc-theory-v12-ch2-hydrodynamics.md` — §2.1-2.7 equation level (gov eq + numerical scheme + SIG/SGZ)
- `efdc-theory-v12-ch5-temperature.md` — §5.1-5.5 (COARE 3.6 + ice + light attenuation)
- `efdc-theory-v12-ch6-sediment.md` — §6.3 SedTran + §6.4 SEDZLJ equation level cross-walk
- `efdc-sedzlj-vs-sedtran-comparison.md` — 두 모듈의 알고리즘 1:1 매핑

## 6. 관련 자료

- [[efdc-manuals-overview]] — 6 manuals 인덱스
- [[efdc-user-manual-r850]] — 운영 매뉴얼 (입력 파일·실행)
- [[efdc-sediment-theory-2003]] — Hamrick legacy sediment theory (DSI v12 §6.3 의 source)
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — EFDC dispatch (concept 레벨)
- [`models/EFDC/source-analysis/`](../source-analysis/) — codex source-code 분석 (이론 식 ↔ Fortran 매핑)
- 외부: [DSI EFDC+ Theory PDF Download](https://www.eemodelingsystem.com/wp-content/Download/Documentation/EFDC_Theory_Document_Ver_12.pdf)
