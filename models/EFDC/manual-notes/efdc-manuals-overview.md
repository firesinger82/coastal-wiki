---
title: "EFDC manuals 종합 인덱스 — 6 documents (DSI v12 + r8.5.0 + Implementation + Propwash + Training + 2003 Sed Theory)"
topic: efdc-manuals
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/manuals/pdfs/ 5 PDF (EFDC_Manual.pdf r8.5.0 표지 + EFDC_Theory_Document_Ver_12.pdf 표지·TOC + EFDC_Implementation_Guide.pdf + EFDC+_Propwash_WhitePaper.pdf + EFDC_Training_Overview.pdf) 직접 표지 추출 + textbook/md/86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.md (8543 줄 추출본, source_id: efdc-sed-trans-2003, Tetra Tech 2002 prepared for US EPA) TOC + textbook/md/692624517-EFDC.md (source_id: efdc-general, 490줄 GUI wizard) 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — 각 manual 표지·TOC 직접 확인"
verification_date: 2026-05-24
related:
  - models/EFDC/README.md
  - models/EFDC/manual-notes/efdc-user-manual-r850.md
  - models/EFDC/manual-notes/efdc-theory-doc-v12.md
  - models/EFDC/manual-notes/efdc-sediment-theory-2003.md
---

# EFDC Manuals 종합 인덱스

> [`models/EFDC/README.md`](../README.md) 와 짝. 모든 manual 자산의 단일 진입점.

## 1. 자산 매트릭스

| # | 파일 | 버전·날짜 | 위치 | 크기 | 분류 | 주 내용 |
|---|---|---|---|---:|---|---|
| 1 | `EFDC_Manual.pdf` | **Release 8.5.0**, Sep 15 2021 | `raw/manuals/pdfs/` | 1.7 MB | 운영 (DSI EFDC+) | Getting Started·Grid Generator·Input Files·Output·Sample Models |
| 2 | `EFDC_Theory_Document_Ver_12.pdf` | **Version 12**, Oct 2024 | `raw/manuals/pdfs/` | 14.4 MB | 이론 (DSI EFDC+) | Hydrodynamics·Transport·Heat·Sediment·Chemical Fate·Development History |
| 3 | `EFDC_Implementation_Guide.pdf` | (DSI) | `raw/manuals/pdfs/` | 1.8 MB | 운영 보조 | Implementation Guide (참고용) |
| 4 | `EFDC+_Propwash_WhitePaper.pdf` | (DSI) | `raw/manuals/pdfs/` | 31 MB | 특수 모듈 | Propeller wash (선박 추진 mix) |
| 5 | `EFDC_Training_Overview.pdf` | (DSI) | `raw/manuals/pdfs/` | 4.1 MB | 교육 | Training overview |
| 6 | `efdc-sed-trans-2003` (source_id) | **May 2002 (3rd DRAFT)**, final revision 05/21/2003 | `textbook/md/86899804-...` | — | 이론 (legacy) | Tetra Tech for US EPA — sediment·sorptive contaminant transport 상세 |
| 7 | `efdc-general` (source_id) | (소형 wizard 자료) | `textbook/md/692624517-EFDC.md` | 48 KB pdf | GUI/wizard | "Create New Model" 마법사 페이지 |

## 2. DSI EFDC+ 의 두 핵심 reference (1, 2)

DSI LLC (Edmonds WA, www.dsi.llc) 가 2009~ 현재 main maintainer. 본 위키 보유 두 핵심:

### 2.1 EFDC_Manual.pdf — User-facing Documentation Release 8.5.0

운영 매뉴얼. 입력 파일·격자 생성·실행·출력 처리 일원.

- **챕터 1 INTRODUCTION** 단일 챕터 구조 (총 80 페이지):
  - §1.1 Getting Started (Build / Running)
  - §1.2 Cartesian Grid Generator (Uniform / Radial / Telescoping / Import)
  - §1.3 Input Files (8 분기 — Run Control 15p / Spatial 66p / Transport 68p / Sediment 70p / Wave 71p / Eutrophication 71p / Toxics 72p / Temperature 73p)
  - §1.4 Output Files + GetEFDC tool
  - §1.5 Sample Models (Lake 2D 77p / Ohio River 78p / Lake Washington 79p)
  - §1.6 License

상세는 [`efdc-user-manual-r850.md`](efdc-user-manual-r850.md).

### 2.2 EFDC_Theory_Document_Ver_12.pdf — Theory Document Version 12

이론서. 모든 모듈의 governing equation·numerical method 정형.

- **7 챕터 구조**:
  - Ch 1 INTRODUCTION — Development History (Hamrick 1992~) + EFDC+ Advancements + Enhancements since EEMS10.3 + Overview
  - Ch 2 HYDRODYNAMICS — Governing Eq·BC·Numerical·Vertical Layering (SIG/SGZ)·Near-Field Discharge (52p)
  - Ch 3 CONSERVATIVE CONSTITUENTS TRANSPORT
  - Ch 4 DYE MODULE (Decay·Age of Water)
  - Ch 5 TEMPERATURE AND HEAT TRANSFER (Heat Balance·COARE 3.6·Ice·Light Attenuation)
  - Ch 6 SEDIMENT TRANSPORT — EFDC SedTran Module (Non-Cohesive·Cohesive·Consolidation) + SEDZLJ Module (Bed Shear·Erosion·Suspended·Bedload·Armoring)
  - Ch 7 CHEMICAL FATE AND TRANSPORT

상세는 [`efdc-theory-doc-v12.md`](efdc-theory-doc-v12.md).

## 3. 2002 Tetra Tech sediment theory (legacy, 6)

DSI v12 Ch 6 의 **legacy reference** — Hamrick 시대 (Tetra Tech for US EPA) sediment 이론 상세. 본 위키에 markdown 으로 추출 (8543 줄, source_id `efdc-sed-trans-2003`).

9 sections (May 2002 / 최종 revision 05/21/2003):
1. Introduction
2. Hydrodynamic and Generic Transport (3D shallow water)
3. Solution of Sediment Transport Equation
4. Hydrodynamic and Sediment Boundary Layers (neutral + stratified)
5. Sediment Bed Mass Conservation, Armoring and Consolidation
6. Noncohesive Sediment Settling, Deposition and Resuspension
7. Cohesive Sediment Settling, Deposition and Resuspension
8. Sorptive Contaminant Transport
9. References

상세는 [`efdc-sediment-theory-2003.md`](efdc-sediment-theory-2003.md). DSI v12 Ch 6 와 cross-check 시 식별자 매핑 (Hamrick → SedTran Original → SEDZLJ → DSI v12 SedTran Module) 필요.

## 4. 특수·교육 자료 (3, 4, 5)

| 자료 | 활용 시점 |
|---|---|
| `EFDC_Implementation_Guide.pdf` | 환경 셋업·빌드·플랫폼 문제 발생 시 |
| `EFDC+_Propwash_WhitePaper.pdf` | 항만·하구 선박 통항 영향 분석 (구체 모듈) |
| `EFDC_Training_Overview.pdf` | 초기 학습·신규 사용자 인계 |

각 별도 노트 작성은 우선순위 낮음 (사용자 운영 빈도 낮은 모듈).

## 5. 사용자 운영 cheat-sheet

| 작업 | 참조 manual |
|---|---|
| 신규 grid 설계 | r8.5.0 §1.2 Cartesian Grid Generator |
| 입력 파일 셋업 | r8.5.0 §1.3 (Run Control + Spatial + Transport 우선) |
| 운영 출력 분석 | r8.5.0 §1.4 + GetEFDC |
| 운동량 방정식·time-stepping 이론 | Theory v12 §2.3-2.5 |
| 표사 모듈 선택 (SedTran vs SEDZLJ) | Theory v12 §6.3 vs §6.4 + 2003 doc §6-7 |
| 표사 BC·boundary layer 설정 | 2003 doc §4 (가장 상세) |
| 수온·열교환 | Theory v12 Ch 5 |
| 식생·구조물·propwash | Theory v12 §2.2.2 / §2.2.7 / §2.2.8 + Propwash WhitePaper |

## 6. 작성 우선순위 (남은 작업)

- 표지·TOC level 은 verified — 노트 (1), (2), (6) 작성 시 page-cited content 확장
- §1.3 Input Files 각 family (8 분기) 의 fort 파일 magic + namelist key 정리 (별도 노트 후보)
- Theory v12 §6.4 SEDZLJ vs 2003 doc §5-7 (Hamrick legacy) 의 알고리즘 일치·차이 매핑 (별도 cross-walk 노트)

## 7. 관련 자료

- [[../README]] — EFDC 모델 정체 카드
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — EFDC SedTran-Original (ISTRAN=6/7) vs SEDZLJ unified, ssedtox.f90 dispatch
- [`models/EFDC/source-analysis/`](../source-analysis/) — 18 source-analysis 노트 (codex source-code 직접 분석)
- `textbook/sources.yml` 의 `efdc-general` + `efdc-sed-trans-2003` source_id
- 외부: [DSI EFDC+ Modeling System](https://www.dsi-llc.com/efdc-modeling-system/), GitHub [dsi-llc/EFDC_Plus](https://github.com/dsi-llc/EFDC_Plus)
