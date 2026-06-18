---
title: "ADCIRC Foundational Papers — Annotated Bibliography (1991–2008)"
model: ADCIRC
doc: adcirc-foundational-papers
canonical_source: external
citation_status: verified
verification_method: "models/ADCIRC/raw/manuals/pdfs/ 하위 30개 foundational PDF 각각의 첫 페이지를 직접 추출하여 서지(제목·저자·연도·발행기관/보고서번호) 인용. 텍스트 임베드된 PDF(1998~2008 NRL/ERDC/논문)는 pdftotext -f 1 -l 1, 스캔 이미지 PDF(1991~1996 DRP-92-6 시리즈·2001_Becker)는 pdftoppm -r 200 후 tesseract OCR로 첫 페이지 표제 확인. 각 항목 기여 요약은 추출된 표제/초록 문장 근거."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/ADCIRC/README.md
---

# ADCIRC Foundational Papers — Annotated Bibliography (1991–2008)

> ADCIRC 공식 사이트가 배포하는 foundational 문헌 30편의 주석 색인. 각 항목은 PDF 첫 페이지에서 직접 추출한 서지(제목·저자·연도·발행처) + 1줄 기여로 구성. 파일 위치는 `models/ADCIRC/raw/manuals/pdfs/<name>.pdf`. **1991~1996년 DRP-92-6 시리즈와 2001_Becker는 스캔 이미지여서 OCR(tesseract)로 표제 확인**, 나머지는 임베드 텍스트(`pdftotext`)에서 직접 추출.

## 출처 신뢰도 주의

- **OCR 추출분(스캔본)**: 저자/연도/제목은 OCR 판독으로 확인했으나 일부 도서관 스탬프·줄바꿈 노이즈가 섞임. 표제 자체는 신뢰 가능, 세부 문장은 ⚠ 미확인 가능성.
- **DRP-92-6 시리즈**: `ADCIRC: An Advanced Three-Dimensional Circulation Model for Shelves, Coasts, and Estuaries` 라는 단일 Technical Report DRP-92-6의 **Report 1~6 분책**. ADCIRC의 1차 정전(canon) 문헌군.

---

## 1. 핵심 정전 — DRP-92-6 시리즈 (US Army WES, Dredging Research Program)

| 파일 | Report | 제목(표제) | 저자 | 연도 | 기여 |
|---|---|---|---|---|---|
| `1992_Luettich02.pdf` | **Report 1** | Theory and Methodology of ADCIRC-2DDI and ADCIRC-3DL | R.A. Luettich Jr., J.J. Westerink, N.W. Scheffner | 1992 | ADCIRC의 **이론·방법론 정전**. GWCE(일반화 파동연속방정식) 기반 2DDI·3DL 정식화 정립. ADCIRC 인용 시 표준 reference (Luettich, Westerink & Scheffner 1992). |
| `1994_Westerink01.pdf` | **Report 2** | User's Manual for ADCIRC-2DDI | J.J. Westerink, C.A. Blain, R.A. Luettich Jr., N.W. Scheffner | 1994 | ADCIRC-2DDI 최초 공식 **사용자 매뉴얼**(입력파일·실행). |
| `1993_Westerink02.pdf` | **Report 3** | Development of a Tidal Constituent Database for the Western North Atlantic and Gulf of Mexico | J.J. Westerink 외 | 1993 | **WNAT 조석 constituent DB** 개발 — 동해안/멕시코만 open-boundary 조석강제 표준 DB의 시초(이후 EC2001로 확장). |
| `1994_Blain03.pdf` | **Report 4** | Hurricane Storm Surge Modeling Using Large Domains | C.A. Blain, J.J. Westerink, R.A. Luettich Jr., N.W. Scheffner | 1994 | 대영역(large-domain) 허리케인 **폭풍해일 모델링** 전략 — 경계조건 민감도 회피를 위한 large-domain paradigm 확립. |
| `1995_Hench.pdf` | **Report 6** | Development of a Tidal Constituent Database for the Eastern North Pacific | J.L. Hench, R.A. Luettich Jr. 외 | 1995 | **동태평양(ENPAC) 조석 constituent DB** — 태평양 측 조석강제 DB. |

> Report 5는 본 PDF 세트에 부재(⚠ 미확인 — 배포 누락).

---

## 2. 조석 (Tides / tidal forcing & databases)

| 파일 | 제목(표제) | 저자 | 연도 | 발행 | 기여 |
|---|---|---|---|---|---|
| `1999_Militello.pdf` | Surface-Water Modeling System Tidal Constituents Toolbox for ADCIRC (CETN IV-21) | A. Militello, A.K. Zundel | 1999 | USACE CETN | SMS 내 ADCIRC **조석경계조건 지정 toolbox** — K1·O1·P1·Q1·M2·N2·S2·K2 8개 표준 constituent 적용 가이드. |
| `2002_Mukai02.pdf` | Guidelines for Using Eastcoast 2001 Database of Tidal Constituents (CHETN-IV-40) | A.Y. Mukai, J.J. Westerink, R.A. Luettich | 2002 | ERDC/CHL | **EC2001 조석 DB** — WNAT 도메인(서북대서양·멕시코만·카리브) O1·K1·Q1·M2·S2·N2·K2 + steady·M4·M6 overtide DB 사용지침. Report 3 DB의 후속·확장판. |

---

## 3. 메소드/수치 — Wetting & Drying, 경계, GWCE, DG

| 파일 | 제목(표제) | 저자 | 연도 | 발행 | 기여 |
|---|---|---|---|---|---|
| `1995_Luettich01.pdf` | An Assessment of Flooding and Drying Techniques for Use in the ADCIRC Hydrodynamic Model: Implementation and Performance in One-Dimensional Flows | R.A. Luettich Jr., J.J. Westerink | 1995 | USACE Contractors Rep. | **wetting/drying** 1D 평가 — 침수/노출 기법 도입 초기 연구. |
| `1995_Luettich03.pdf` | Implementation and Testing of Elemental Flooding and Drying in the ADCIRC Hydrodynamic Model | R.A. Luettich Jr., J.J. Westerink | 1995 | USACE Contractors Rep. | **요소단위(elemental) wetting/drying** 정식 구현·검증. |
| `1999_Luettich01.pdf` | Elemental Wetting and Drying in the ADCIRC Hydrodynamic Model: Upgrades and Documentation for ADCIRC Version 34.XX | R.A. Luettich Jr., J.J. Westerink | 1999 | USACE Contractors Rep. | v34.XX **wetting/drying 업그레이드·문서화** — 현행 W/D 알고리즘 계보. |
| `1996_Westerink03.pdf` | ADCIRC Version 30.02 — Methodologies and I/O for Enhanced Provisions for Flow Entering and Exiting the Computational Domain | J.J. Westerink, R.A. Luettich Jr. | 1996 | USACE 계약보고서 | v30.02 **유입/유출·내외부 barrier(weir overtopping) 경계** 도입. |
| `2001_Westerink.pdf` | Leaky Internal-Barrier Normal-Flow Boundaries in the ADCIRC Coastal Hydrodynamics Code (CHETN-IV-32) | J.J. Westerink, R.A. Luettich, A. Militello | 2001 | ERDC/CHL | v40.02+ **leaky internal-barrier(누수 제방/방파제)** 경계 — 구조물 통과·월류 흐름 계산. |
| `2008_Dietrich.pdf` | Mass Residuals as a Criterion for Mesh Refinement in Continuous Galerkin Shallow Water Models | J.C. Dietrich, R.L. Kolar, K.M. Dresback | 2008 | J. Hydraul. Eng. (ASCE 134:5) | **질량잔차(mass residual)** 기반 메시 세분화 기준 — CG(continuous Galerkin) 천수모델 mesh refinement 진단. |
| `2001_Edwards.pdf` | Evaluation of an Application of Adjoint Methods to Yellow Sea Modeling (NRL/FR/7320-01-9976) | C.R. Edwards, C.A. Blain | 2001 | NRL | **adjoint(수반) 방법**의 ADCIRC 황해 적용 평가 — data assimilation/감도 분석 계보. |

> **DG(Discontinuous Galerkin)**: 본 foundational 세트에는 명시적 DG 정식화 논문이 부재(⚠ 미확인). 2008_Dietrich는 CG 기반. Cobb/Blain wave 논문군은 DG가 아님.

---

## 4. 적용/검증 — 폭풍해일·조석·해류 (validation cases)

| 파일 | 제목(표제) | 저자 | 연도 | 발행 | 기여 |
|---|---|---|---|---|---|
| `1991_Luettich02.pdf` | Application of ADCIRC-2DDI to Masonboro Inlet, North Carolina: A Brief Numerical Modeling Study | R.A. Luettich Jr., R.H. Birkhahn, J.J. Westerink | 1991 | US Army WES (DACW39-86-D-0004) | ADCIRC-2DDI 최초기 **inlet 적용** 사례 중 하나(Masonboro Inlet, NC). |
| `1994_Blain02.pdf` | The Influence of Domain Size on the Response Characteristics of a Hurricane Storm Surge Model | C.A. Blain, J.J. Westerink, R.A. Luettich Jr. | 1994 | J. Geophys. Res. 99(C9):18,467–18,479 | **도메인 크기가 폭풍해일 응답에 미치는 영향**(Hurricane Kate, Florida shelf) — large-domain 필요성의 정량적 근거(JGR 게재). |
| `1994_Blain04.pdf` | Generation of a Storm Surge Time History Data Base from the Hindcast of Extratropical Storm Events 1977–1992 | C.A. Blain, J.J. Westerink, R.A. Luettich Jr., N.W. Scheffner | 1994 | USACE DRP WU-32466 | 1977–1992 **온대저기압 hindcast 폭풍해일 시계열 DB** 생성. |
| `1998_Blain02.pdf` | A Real-Time Application of the ADCIRC-2DDI Hydrodynamic Model at Camp Pendleton, California (NRL/FR/7322-98-9684) | C.A. Blain, A.P. McManus | 1998 | NRL | ADCIRC-2DDI **실시간(real-time) 운용** 사례(Camp Pendleton, CA). |
| `1998_Blain03.pdf` | Coastal Tide Prediction Using the ADCIRC-2DDI Hydrodynamic Finite Element Model: Validation and Sensitivity in the Southern North Sea/English Channel (NRL/FR/7322-98-9682) | C.A. Blain, W.E. Rogers | 1998 | NRL | **연안 조석예측 검증·민감도**(남부 북해/영국해협) — 종합 validation 보고. |
| `2001_Becker.pdf` | A Reconnaissance Modeling Study of Two-dimensional Tidal Circulation and Sediment Bed Change in the Vicinity of the Cape Fear River Navigation Channel, NC | M.L. Becker, R. Luettich, J. Westerink | 2001 | Final Report | 2D 조석순환 + **하상변동(sediment bed change)** 연계 정찰 모델링(Cape Fear River, NC). |
| `2001_Veeramony.pdf` | Barotropic Flow in the Vicinity of an Idealized Inlet — Simulations with the ADCIRC Model (NRL/FR/7320-01-9977) | J. Veeramony, C.A. Blain | 2001 | NRL | 이상화 inlet 주변 **순압(barotropic) 흐름** ADCIRC 시뮬레이션. |
| `2001_Blain01.pdf` | Software Design Description for the Advanced Circulation Model (ADCIRC) (NRL/MR/7320-01-8271) | C.A. Blain, K.A. Kelly | 2001 | NRL | ADCIRC **소프트웨어 설계기술서(SDD)** — 코드 아키텍처 문서. |
| `2002_Edwards01.pdf` | Operational Evaluation of ADCIRC-2DDI as Applied to the Western North Atlantic Ocean (NRL/FR/7320-02-10,005) | C.R. Edwards, C.A. Blain | 2002 | NRL | WNA 해역 ADCIRC-2DDI **운용 평가**. |

---

## 5. 파랑유도 순환 (wave-induced / radiation stress)

| 파일 | 제목(표제) | 저자 | 연도 | 발행 | 기여 |
|---|---|---|---|---|---|
| `1999_Luettich02.pdf` | Implementation of the Wave Radiation Stress Gradient as a Forcing for the ADCIRC Hydrodynamic Model: Upgrades for ADCIRC Version 34.12 | R.A. Luettich Jr., J.J. Westerink | 1999 | USACE Contractors Rep. | **파랑 radiation stress gradient 강제** 구현(v34.12) — wave-current 결합의 시초(이후 SWAN+ADCIRC 계보). |
| `2003_Blain.pdf` | Application of a Shelf-Scale Model to Wave-Induced Circulation: Alongshore Currents on Plane and Barred Beaches (NRL/FR/7322-03-10,046) | C.A. Blain, M. Cobb | 2003 | NRL | radiation stress 강제로 **연안방향 해류(alongshore current)** — 평탄/사주 해빈. |
| `2003_Cobb.pdf` | Application of a Shelf-Scale Model to Wave-Induced Circulation: Rip Currents (NRL/FR/7322-03-10,055) | M. Cobb, C.A. Blain | 2003 | NRL | 파랑유도 **이안류(rip current)** 모델링. |

---

## 6. 기타 부가 — 교량 piling

| 파일 | 제목(표제) | 저자 | 연도 | 발행 | 기여 |
|---|---|---|---|---|---|
| `1999_Luettich03.pdf` | Implementation of Bridge Pilings in the ADCIRC Hydrodynamic Model: Upgrade for ADCIRC Version 34.19 | R.A. Luettich Jr., J.J. Westerink | 1999 | USACE Contractors Rep. | **교각(bridge piling) 항력** 구현(v34.19) — 국소 구조물 저항항. |

---

## 7. Baroclinic / 3D / sediment transport

| 파일 | 제목(표제) | 저자 | 연도 | 발행 | 기여 |
|---|---|---|---|---|---|
| `2004_Pandoe01.pdf` | Extended Three-Dimensional ADCIRC Hydrodynamic Model to Include Baroclinic Flow and Sediment Transport | W.W. Pandoe | 2004 | Texas A&M PhD 학위논문 | 3D ADCIRC를 **경압(baroclinic) 흐름 + 퇴적물 이송**까지 확장 — 밀도성층/sediment 결합. |

---

## 8. ADCIRC Theory (2004) — 현행 정식화 참조문서

| 파일 | 제목(표제) | 저자 | 연도 | 기여 |
|---|---|---|---|---|
| `2004_Luettich.pdf` (= `adcirc_theory_2004_12_08.pdf`) | **Formulation and Numerical Implementation of the 2D/3D ADCIRC Finite Element Model Version 44.XX** | R. Luettich, J. Westerink | 2004-12-08 | ADCIRC의 **현행 이론·수치구현 정전**. v44.XX 2D/3D 유한요소 정식화. 두 파일은 동일 문서(`pdfs/` 직하와 `2018/11/` 배포본). GWCE·조석·3D 연직구조의 현대 표준 reference. |

> `2004_Luettich.pdf`와 `adcirc_theory_2004_12_08.pdf`는 동일 표제·동일 날짜(12/08/2004)·동일 텍스트(86,898 chars). 중복본 1쌍.

---

## 색인 통계

- 총 PDF 항목: **30편** (중복 theory 1쌍 포함 → 고유 문서 29편)
- 임베드 텍스트 추출: 1998~2008년 NRL/ERDC/저널/학위논문 (16편)
- OCR(스캔본): DRP-92-6 시리즈 5편 + 1991_Luettich02 + 1994_Blain04 + 1995_Luettich01/03 + 1996_Westerink03 + 2001_Becker (≈13편)
- 미수록(⚠): DRP-92-6 **Report 5** 부재. 명시적 **DG 정식화** 논문 부재.
