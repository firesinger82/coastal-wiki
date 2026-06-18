---
title: "Delft3D 전·후처리 도구 매뉴얼 통합 (GPP·QUICKPLOT·RGFGRID·QUICKIN·TRIANA·NEFIS·WES·DIDO)"
model: Delft3D
doc: Delft3D-GPP / Delft3D-QUICKPLOT / RGFGRID / QUICKIN / Delft3D-TRIANA / NEFIS / Delft3D-WES / Delft3D-WAQ DIDO User Manuals
canonical_source: manual
citation_status: verified
verification_method: "각 PDF를 raw/manuals/pdfs 에서 find 로 찾아 pdftotext 로 표지·Contents(TOC)·해당 도구의 목적 단락을 직접 추출. 목적 문장은 인쇄 페이지 footer(`N of M`)로 page 인용 확정 — GPP p34, QUICKPLOT p1, RGFGRID p1, QUICKIN p1, TRIANA p16(§5.4 목적문장)·p3(ch.2), NEFIS p1(ch.1), WES p2(§2.1), DIDO p3(§2.1)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/Delft3D/README.md
  - models/Delft3D/manual-notes/delft3d-manuals-overview.md
  - models/Delft3D/manual-notes/delft3d-tide-user-manual.md
---

# Delft3D 전·후처리 도구 매뉴얼 통합

> Delft3D 워크플로를 구성하는 보조 도구 8종의 **목적 + 핵심 기능**을 각 공식 User Manual 의 표지·TOC·서론 단락에서 page 인용으로 정리. 그리드 생성(RGFGRID)·수심 보간(QUICKIN)·후처리 시각화(GPP·QUICKPLOT)·조화분석(TRIANA)·파랑 enclosure 풍압장(WES)·WAQ 격자 집성(DIDO)·바이너리 I/O 라이브러리(NEFIS) 가 전체 사슬을 잇는다. 모든 PDF 경로: `models/Delft3D/raw/manuals/pdfs/`.

각 도구의 메뉴·서브루틴별 세부 기능은 이 통합 노트의 범위 밖(목적+핵심 1-2개만 인용). 깊은 분석이 필요하면 도구별 노트로 분리 권장.

---

## 1. 전처리 도구 (Grid / Bathymetry)

### 1.1 RGFGRID — 곡선격자·비정형격자 생성기

> RGFGRID User Manual (`RGFGRID_User_Manual.pdf`)

- **목적** (§2.1, p1): *"RGFGRID is a program for generation and manipulation of structured curvilinear grids for Delft3D-FLOW and Delft3D-WAVE and unstructured grids for D-Flow Flexible Mesh. The coordinate system may be Cartesian or spherical."*
- **핵심 기능**:
  - 구조적 **curvilinear grid** + 비정형 **unstructured grid** 둘 다 생성/조작. 좌표계 Cartesian 또는 spherical 지원 (§2.1, p1).
  - **Orthogonalisation** — 격자 직교성 $\cos(\theta)$ 를 지표로 평가하고 블록 단위로 직교화 (TOC §5.2.x Grid properties; Block Orthogonalise, List of Figures).
- **TOC 골자**: 1 Guide / 2 Introduction to RGFGRID (Coordinate systems, Program considerations) / 3 Getting started / 4 General program operation (Toolbars, Key stroke functions) / 5 Menu options (File·Edit: Select Domain·Irregular grid·Land Boundaries·Samples).

### 1.2 QUICKIN — 수심·초기장 보간기

> QUICKIN User Manual (`QUICKIN_User_Manual.pdf`)

- **목적** (§2.1, p1): *"QUICKIN is a program for the generation, interpolation or manipulation of space varying quantities such as bathymetries, initial conditions or parameter fields on Cartesian or spherical (curvilinear) grids e.g. created with RGFGRID."*
- **핵심 기능**:
  - **bathymetry / initial condition / parameter field** 를 격자에 보간·생성·조작. RGFGRID 로 만든 곡선격자에 적용 (§2.1, p1).
  - 다양한 **interpolation methods** + 사용자가 polygon 으로 지정하는 **'area of influence'** (Special facilities, p1).
- **TOC 골자**: 2 Introduction to QUICKIN / 5 Menu options Edit: Depth, Depth linear, Depth isoline, Depth line sweep, Samples, Check dike heights, Dry points, Thin dam points, Observation points.

---

## 2. 후처리·시각화 도구

### 2.1 GPP — Graphical Post-Processor

> Delft3D-GPP User Manual (`Delft3D-GPP_User_Manual.pdf`)

- **목적** (p34): *"GPP is a framework which allows you to import certain data sets (from external files) or to create data sets from others, and to present them in any way possible and suitable."*
- **핵심 기능**:
  - data set 들을 **import / 파생 생성** 후 plot 으로 표현하는 프레임워크. window-oriented GUI (p34; Getting started, ch.2).
  - **배치/자동화** — session file 편집, batch processing, animation 생성, data set 자동 export, 사용자 정의 plot/export 루틴 (TOC ch.8 Standardising pictures·Creating animations·Automating tasks·Script commands).
  - Delft3D 시스템의 일부로 설치되나 **독립 실행도 가능** (Getting started: *"GPP is normally installed as part of the Delft3D system ... but it can be used independently as well"*; Linux `gpp`, Windows Utilities→GPP).
- **지원 포맷**: TEKAL files, Samples files, TEKAL time-series files 등 (TOC §5.3).

### 2.2 QUICKPLOT — MATLAB 기반 시각화

> Delft3D-QUICKPLOT User Manual (`Delft3D-QUICKPLOT_User_Manual.pdf`)

- **목적** (§1, p1): *"The program can be used to visualise and animate numerical results produced by various components of the Delft3D Flexible Mesh Suite, the D-HYDRO Suite, the Delft3D 4 Suite and the SOBEK Suite and various other programs such as UNIBEST, SHIPMA and PHAROS. The program has been developed using MATLAB."*
- **핵심 기능**:
  - **MATLAB 기반** interactive 데이터 시각화·애니메이션. Delft3D-MATLAB interface 를 통해 MATLAB 환경에 통합 (§1, p1).
  - 풍부한 plot 옵션 — vector style/scaling, contour/colour thresholds, colour map/bar, field thinning, data/coordinate clipping (TOC ch.4 §4.1~4.29).
- **TOC 골자**: 1 Introduction / 3 Getting started (Selecting file·field·time·location, Creating a plot) / 4 plot options / 5 Exporting data·figures / 6 Preferences.

---

## 3. 분석·특수 입력 도구

### 3.1 TRIANA — 조화분석 (Tidal analysis)

> Delft3D-TRIANA User Manual (`Delft3D-TRIANA_User_Manual.pdf`); subtitle *"Tidal analysis of FLOW time-series and comparison with observed constants"*

- **목적** (§5.4, p16): *"Delft3D-TRIANA performs a tidal analysis on computed time-series and compares the 'computed' tidal constants with 'measured' tidal constants. From the deviations in terms of amplitude ratio and phase differences you get an evaluation of the performance of your model regarding the horizontal and/or vertical tide."* (Ch.2 Introduction(p3)도 offline tidal analysis·reference set 비교를 기술)
- **핵심 기능**:
  - Delft3D-FLOW 결과 time-series 에 **tidal analysis** 수행 → tidal constants(진폭·위상) 산출, 관측 reference set 과 비교 (§2, p3).
  - **calibration 지원** — amplitude ratio / phase difference 편차로 모델 성능 평가, 입력 파라미터(예: bathymetry) 보정 (§5.4 Calibrating your model using TRIANA, p16).
- **입출력** (TOC ch.4): 입력 = General input file, 관측 tidal constants file, Time-series input file / 출력 = Print file, Table-A file, Table-B file. TRIANA 는 Delft3D-FLOW 의 **additional tools** 에 속함 (§3.7 Additional tools for the Delft3D-FLOW module, p6).

### 3.2 WES — Wind Enhance Scheme (파랑 enclosure 풍압장)

> Delft3D-WES User Manual (`Delft3D-WES_User_Manual.pdf`); cover *"Wind Enhance Scheme for cyclone modelling"*, Version 3.x

- **목적** (§2.1 Functions and data flow, p2): *"The main functions and data flow of WES is to synthesize the tropical cyclone wind and pressure drop on a circular or 'spiderweb' type grid."*
- **동기** (§2.x): NWP 격자 해상도가 cyclone 중심 부근 강한 풍속 gradient 를 충분히 표현하지 못해 별도 합성이 필요 (*"the grid resolution used in these models is usually not sufficient to accurately represent the strong variations on the wind gradients near its centre"*).
- **핵심 기능**:
  - **tropical cyclone** 의 wind + pressure drop 을 circular(=spiderweb) 격자 위에 합성 (§2.1, p2).
  - 입력 가용 정보에 따라 **7가지 method** 제공 — Method 1 ($V_{max}, A, B$) ~ Method 7 ($V_{max}$ 단독) (TOC ch.6·7). Holland 모델 기반 (TOC §5.1 *"Brief description of Holland's model"*).
- **이론적 토대**: §5 Conceptual description 에 방정식, §8 관측(QuikSCAT·ERS winds) 비교, §10 Glossary 수록.

### 3.3 DIDO — WAQ 격자 집성 에디터

> Delft3D-WAQ DIDO User Manual (`Delft3D-WAQ_DIDO_User_Manual.pdf`)

- **목적** (§2.1, p3): *"D-Waq DIDO is an interactive grid editor for coupling hydrodynamic models with the DELWAQ model. It uses a rectilinear, curvilinear or Finite Element hydrodynamic grid layout as input. It produces the administration file needed by the Delft3D Water quality model DELWAQ to condense the fine hydrodynamic grid to a coarser water quality grid. Each water quality grid cell consists of one or more of the hydrodynamic grid cells."*
- **핵심 기능**:
  - hydrodynamic grid(rectilinear/curvilinear/FE) → **DELWAQ 수질격자 집성** administration file 생성 (§2.1, p3).
  - **Aggregate** 연산 — 세밀한 수역학 격자 cell 들을 거친 수질 cell 로 합침. 무집성(no aggregation) 시 1:1 매핑 (§2.1, p3; TOC §5.2.1 Aggregate, ch.6 Tutorial two-by-two/default aggregation).
  - ⚠ Delft3D-FM 병렬 모드는 별도 **"Waqmerge"** 도구 사용 (§2.x note).

---

## 4. 인프라 라이브러리

### 4.1 NEFIS — 자기기술 바이너리 I/O

> NEFIS User Manual (`NEFIS_User_Manual.pdf`)

- **목적** (§1.1, p1): *"NEFIS is a library of functions designed for scientific programs ... NEFIS is able to store and retrieve large volumes of data on file or in shared memory. To achieve a good performance ... the files are self-describing binary direct access files. ... NEFIS also allows users to store data in a machine-independent way on files, which means that the data files can be interchanged between computer systems without having to be converted."*
- **핵심 기능**:
  - **self-describing binary direct-access** 파일(또는 shared memory) 로 대용량 과학 데이터 저장/조회. machine-independent → 시스템 간 변환 없이 교환 (§1.1, p1).
  - **계층 구조** group → cell → element. element 가 최소 접근 단위, cell = 1+ element, group = cells 의 다차원 배열 (§1.1, p1; TOC ch.2 Definitions). 한 배열 차원은 variable 가능.
- **API** (TOC ch.4): Crenef/Credat/Defcel/Defelm/Defgrp(생성·정의), Getelt/Getels(읽기), Inqcel/Inqdat/Inqelm(조회), Clsnef(닫기) 등 Fortran/C 함수군. NEFIS 는 Delft3D 의 `.dat`/`.def` 결과 파일 포맷 기반(GPP·QUICKPLOT 가 이를 읽음).

---

## 도구 간 워크플로 요약

| 단계 | 도구 | 산출물 | 출처 page |
|---|---|---|---|
| 격자 생성 | RGFGRID | curvilinear/unstructured grid | RGFGRID p1 |
| 수심·초기장 보간 | QUICKIN | bathymetry/initial/parameter field | QUICKIN p1 |
| 태풍 풍압장 | WES | spiderweb wind+pressure | WES p2 |
| (시뮬레이션: FLOW/WAVE/WAQ) | — | NEFIS `.dat`/`.def` | NEFIS p1 |
| WAQ 격자 집성 | DIDO | DELWAQ aggregation admin file | DIDO p3 |
| 조화분석·검정 | TRIANA | tidal constants, Table-A/B | TRIANA p16(§5.4) |
| 후처리 시각화 | GPP / QUICKPLOT | plots / animations | GPP p34, QUICKPLOT p1 |

⚠ 미확인: 각 도구의 버전 번호는 표지 기준 일부만 확인(WES v3.x, QUICKPLOT v—). 도구별 세부 메뉴·알고리즘은 본 통합 노트 범위 밖 — 필요 시 개별 노트로 deep-dive 권장.
