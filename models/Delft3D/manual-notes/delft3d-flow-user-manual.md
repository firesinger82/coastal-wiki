---
title: "Delft3D-FLOW User Manual v4.07.01 (Deltares May 2026) — TOC + MDF file 구조 + 입력 family 12 buckets"
topic: delft3d-flow-user-manual
canonical_source: self
citation_status: verified
verification_method: "models/Delft3D/raw/manuals/pdfs/Delft3D-FLOW_User_Manual.pdf 표지·Contents pages 1-5 직접 추출 — Delft3D-FLOW Simulation of multi-dimensional hydrodynamic flows and transport phenomena, including sediments. Version 4.07.01, Revision 80907, 3 May 2026. Deltares (Boussinesqweg 1, 2629 HV Delft, Netherlands). 5 챕터 구조 + Ch 4 §4.5 의 12 input parameter family + Ch 5 Tutorial 직접 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — PDF Read pages 1-5 직접 확인"
verification_date: 2026-05-24
related:
  - models/Delft3D/manual-notes/delft3d-manuals-overview.md
  - models/Delft3D/source-analysis/delft3d_flow2d3d_dispatcher.md
  - models/Delft3D/README.md
---

# Delft3D-FLOW User Manual

> 출처: [`models/Delft3D/raw/manuals/pdfs/Delft3D-FLOW_User_Manual.pdf`](../raw/manuals/pdfs/Delft3D-FLOW_User_Manual.pdf) (Deltares).

## 1. 자료 식별

| 항목 | 값 |
|---|---|
| 제목 | Delft3D-FLOW — Simulation of multi-dimensional hydrodynamic flows and transport phenomena, including sediments |
| 부제 | User Manual — Hydro-Morphodynamics |
| Version | 4.07.01 |
| Revision | 80907 |
| 날짜 | 3 May 2026 |
| 발행 | Deltares (Boussinesqweg 1, 2629 HV Delft, Netherlands) |
| 파일 | `Delft3D-FLOW_User_Manual.pdf` |
| 크기 | 11 MB |

상태: **DRAFT 워터마크** — 최신 활성 문서 (2026 release cycle).

## 2. 5 챕터 구조 (Contents 직접 인용)

```
List of Tables                                  xiv
List of Figures                                 xvi

1  A guide to this manual                       1
  1.1 Introduction                              1
  1.2 Typographical conventions                 2
  1.3 Changes with respect to previous versions 3

2  Introduction to Delft3D-FLOW                 6
  2.1 Areas of application                      6
  2.2 Modelling capabilities and advantages     7
  2.3 Current limitations for Delft3D-FLOW      7
  2.4 Standard features                         7
  2.5 Special features                          8
  2.6 Validation of Delft3D-FLOW                8
  2.7 Coupling to other modules                 8
  2.8 Utilities                                 9
  2.9 Installation and computer configuration   9

3  Getting started                              10
  3.1 Overview of Delft3D                       10
  3.2 Starting Delft3D                          10
  3.3 Getting into Delft3D-FLOW                 11
  3.4 Exploring some menu options               14
  3.5 Exiting the FLOW-GUI                      15

4  Graphical User Interface                     17
  4.1 Introduction                              17
  4.2 MDF-file and attribute files              17
  4.3 Filenames and conventions                 18
  4.4 Working with the FLOW-GUI                 19
  4.5 Input parameters of MDF-file              23
  4.6 Save the MDF and attribute files and exit 104
  4.7 Importing, removing and exporting of data 106

5  Tutorial                                     107
  ... (Tutorial walkthrough — IC·BC·Physical·Numerical·Operations·Monitoring)
```

## 3. Ch 4 §4.5 — Input Parameters of MDF-file (운영 핵심)

**MDF (Master Definition File) 의 12 입력 family**:

| § | Family | 페이지 | 주 입력 |
|---|---|---:|---|
| 4.5.1 | Description | 24 | 모델 설명·메타데이터 |
| 4.5.2 | **Domain** | 24 | Grid (§4.5.2.1, p.25) + Bathymetry (§4.5.2.2, p.30) + Dry points (§4.5.2.3, p.32) + Thin dams (§4.5.2.4, p.34) |
| 4.5.3 | Time frame | 36 | 시뮬레이션 시간·time-step |
| 4.5.4 | Processes | 38 | 활성 process (salt·temp·sed·morph·constituents) |
| 4.5.5 | Initial conditions | 41 | IC (zeta·u·v·temp·salt·sed) |
| 4.5.6 | **Boundaries** | 43 | Flow BC (§4.5.6.1, p.50) + Transport BC (§4.5.6.2, p.59) |
| 4.5.7 | **Physical parameters** | 61 | Constants (§4.5.7.1, p.61) + Viscosity (§4.5.7.2, p.66) + Heat flux (§4.5.7.3, p.70) + **Sediment (§4.5.7.4, p.73)** + **Morphology (§4.5.7.5, p.77)** + Wind (§4.5.7.6, p.81) + Tidal forces (§4.5.7.7, p.83) |
| 4.5.8 | Numerical parameters | 83 | scheme·CFL·iteration |
| 4.5.9 | **Operations** | 87 | Discharge (§4.5.9.1, p.88) + **Dredging and dumping (§4.5.9.2, p.92)** |
| 4.5.10 | Monitoring | 93 | Observations (§4.5.10.1, p.93) + Drogues (§4.5.10.2, p.94) + Cross-sections (§4.5.10.3, p.95) |
| 4.5.11 | Additional parameters | 97 | 보조·debug 옵션 |
| 4.5.12 | Output | 98 | Storage (§4.5.12.1, p.99) + Print (§4.5.12.2, p.102) + Details (§4.5.12.3, p.103) |

→ **운영 워크플로 = 12 family 를 순차적으로 채우는 작업**.

## 4. Sediment + Morphology 분기 (한국 적용 핵심)

| § | 페이지 | 주제 |
|---|---:|---|
| 4.5.7.4 | 73 | **Sediment** — sediment class·boundary BC·initial bed |
| 4.5.7.5 | 77 | **Morphology** — bed update mode·morfac·avalanching |
| 4.5.9.2 | 92 | **Dredging and dumping** — 항만 준설·매립 시뮬 |

→ Korean 항만 dredging·연안 erosion 분석 시 위 3 section 집중. [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) §Delft3D-SED 와 cross-ref.

## 5. Ch 5 Tutorial 분기 (학습)

- §5.5 Domain — Grid·Bathymetry·Dry points·Thin dams (실습)
- §5.10 Physical parameters — Constants·Roughness·Viscosity·Wind
- §5.13 Monitoring — Observation points·Drogues·Cross-sections

신규 사용자 권장 시퀀스 — §5.4 Description → §5.5 Domain → §5.6 Time frame → §5.7 Processes → §5.8 IC → §5.9 BC → §5.10 Physical → §5.11 Numerical → §5.13 Monitoring.

## 6. flow2d3d Fortran 매핑 (source-analysis 와 cross-ref)

| Manual section | Fortran 모듈 |
|---|---|
| §4.5.2 Domain (Grid/Bath/Dry/Thin) | `flow2d3d_io` (MDF parser) + `flow2d3d_data` (grid state) |
| §4.5.6 Boundaries (Flow/Transport BC) | `flow2d3d_kernel` 의 BC routines |
| §4.5.7.3 Heat flux | [[../source-analysis/delft3d_heat]] |
| §4.5.7.4-5 Sediment + Morphology | [[../source-analysis/sediment]] subdir |
| §4.5.7.6 Wind | `flow2d3d_kernel` wind stress |
| §4.5.9 Operations (Discharge/Dredge-Dump) | [[../source-analysis/delft3d_dredge_dump]] |
| §4.5.10 Monitoring | `flow2d3d_io` output writers |
| Domain Decomposition (별도) | [[../source-analysis/delft3d_dd]] |
| Sigma vs Z-layer | [[../source-analysis/delft3d_sigma_z]] |
| Turbulence closure (§4.5.8 부속) | [[../source-analysis/delft3d_turbulence]] |
| Wet/dry threshold | [[../source-analysis/delft3d_drying_flooding]] |

## 7. 작성 우선순위 (남은 M-C)

- `delft3d-flow-mdf-input-cards.md` — 12 family 각 키워드·기본값 카드 family (§4.5.1~4.5.12 deep)
- `delft3d-wave-user-manual.md` — WAVE User Manual TOC + SWAN integration mode
- `delft3d-waq-user-manual.md` — WAQ main + Processes Library Tables
- `delft3d-flow-tutorial-walkthrough.md` — Ch 5 Tutorial 의 실습 시퀀스 정리

## 8. 관련 자료

- [[delft3d-manuals-overview]] — 53 PDFs 인덱스
- [[../source-analysis/delft3d_engines_overview]] — engines_gpl 12 엔진 (flow2d3d 포함)
- [[../source-analysis/delft3d_flow2d3d_dispatcher]] — flow2d3d 8 packages Fortran 구조
- [[../web-refs/delft3d-official-resources]] — Lesser 2004 paper 인용
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — Delft3D-SED Van Rijn / Partheniades-Krone
- 외부: [Deltares OSS Delft3D](https://oss.deltares.nl/web/delft3d), [공식 manuals download](https://content.oss.deltares.nl/delft3d4/)
