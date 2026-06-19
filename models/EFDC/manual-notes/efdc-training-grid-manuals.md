---
title: "EFDC 교육·격자 생성 실습 자료 — Training Overview(Cardno ENTRIX 2013) + Grid+ Hands-On(NY Harbor)"
model: EFDC
doc: ["EFDC_Training_Overview.pdf", "Grid1.0_Intro_Hands-On.pdf"]
canonical_source: manual
citation_status: verified
verification_method: "pdftotext -layout 로 EFDC_Training_Overview.pdf(107p, raw/manuals/pdfs/) 전체 슬라이드 + Grid1.0_Intro_Hands-On.pdf(53p, raw/manuals/confluence/spaces/EHG/attachments/2225111041/) 전체 슬라이드 직접 추출. 표지·각 슬라이드 제목·본문 bullet 직접 확인 후 슬라이드(page) 번호 인용. 격자 dump(CELL.inp 매트릭스) 슬라이드는 page 28 로 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/EFDC/README.md
  - models/EFDC/manual-notes/efdc-manuals-overview.md
  - models/EFDC/manual-notes/efdc-user-manual-r850.md
---

# EFDC 교육·격자 생성 실습 자료

> 두 개의 **슬라이드형(slide deck) 교육 자료**를 page-cited 로 정리. (1) `EFDC_Training_Overview.pdf` — Cardno ENTRIX 의 LTPR(Lower Tar Pamlico River) 모델 기반 신규 사용자 교육 흐름(107 슬라이드, 2013-09). (2) `Grid1.0_Intro_Hands-On.pdf` — EFDC_Explorer/Grid+ GUI 의 New York Harbor 격자 생성 12-step hands-on(53 슬라이드). 기존 [`efdc-manuals-overview.md`](efdc-manuals-overview.md) §4 에서 "우선순위 낮음"으로만 색인되었던 Training_Overview 의 실 내용을, Grid 실습과 함께 본 노트로 전개. **출처는 교육 슬라이드** — DSI 공식 이론/운영 매뉴얼(Theory v12 / r8.5.0)과 권위 수준이 다름. 슬라이드 단언이 이론서와 충돌 시 이론서 우선.

---

## 1. Training Overview — 자료 정체

| 항목 | 내용 | 인용 |
|---|---|---|
| 표지 | "EFDC Model Training — Drew Ackerman, Cardno ENTRIX, September X, 2013" | Training p1 |
| 대상 모델 | LTPR = Lower Tar Pamlico River EFDC 모델 (6 σ-layer, 593 horizontal cells) | Training p23 |
| 교육 초점 | "Focus of this training is temperature and salinity" (수온·염분) | Training p7 |
| 실행 환경 | Citrix server `appserver.ncwater.org` 가상 데스크톱 + OASIS 동일 로그인 | Training p82-84 |

이 자료는 **특정 프로젝트(LTPR/North Carolina) 운영 인계용**이라 도메인 결론이 아닌 *워크플로 교육 흐름*만 객관 인용 대상. 프로젝트별 수치(19 flow source, 4 model year 등)는 LTPR 한정 사례로 명시.

### 1.1 모델 배경 슬라이드 (Training p2-4)

- "Solves the three-dimensional, vertically hydrostatic, free surface, turbulent averaged equations of motions for a variable density fluid" — sigma coordinate + Cartesian/curvilinear orthogonal grid, incompressible·hydrostatic 가정, salinity·temperature dynamically coupled (Training p2).
- 시뮬레이션 능력: wetting and drying / controlled flow structures / vegetation resistance / wave-current boundary layers·wave-induced currents / embedded single port buoyant jet module (Training p3).
- linkage: hydrodynamics → sediment(cohesive/non-cohesive, deposition/resuspension, bed load) · water quality(eutrophication, sediment diagenesis) · toxics(trace metals/organic, sediment interaction) (Training p4).

### 1.2 EFDC 버전 계보 (교육 자료 관점, Training p5)

| 계보 | 설명 | 비고 |
|---|---|---|
| Tetra Tech version | EPA version, Hamrick 원본, "Last updated in 2002" | legacy |
| Sandia Labs | research version | — |
| Dynamic Solutions | "Commercial version with GUI", 추가 기능·지원, "Last updated in 2013" | DSI(현 maintainer) |

⚠ 2013 시점 슬라이드라 "last updated" 연도는 당시 기준. 현재 DSI EFDC+ 최신은 [`efdc-manuals-overview.md`](efdc-manuals-overview.md) §1 참조(r8.5.0 / Theory v12).

---

## 2. Training Overview — 입력 파일 분류 교육 흐름

교육은 입력 파일을 4 그룹으로 나눠 순차 설명. **free format, integer/real 구분에 민감, Notepad++로 열람** 권장 (Training p23).

### 2.1 파일 그룹 (Training p8-10, p33-34, p55)

| 그룹 | 대표 파일 | 역할 | 인용 |
|---|---|---|---|
| Control | `EFDC.inp`(primary control), `SHOW.inp`(screen print), `WQ3DWC.inp`(WQ control) | 모델 기술·출력 셋업 | Training p10 |
| Grid | `CELL.inp`·`CELLLT.inp`(cell type), `CORNERS.inp`(corner coords), `DXDY.inp`(cell dim), `LXLY.inp`(orientation) | 격자 위치·방향·형상 정의 | Training p26 |
| Initial Condition | `SALT.inp`, `TEMP.inp`, `SEDB.inp`/`SEDW.inp`(cohesive bed/water), `BEDBDN/BEDDDN/BEDLAY.inp`(bed 밀도/공극률/두께) | 시작 시점 조건 | Training p34 |
| Boundary/Input | `PSER`(tide), `QSER`(flow), `SSER`(salinity), `TSER`(temp), `SDSER`/`SNSER`(cohesive/non-cohesive sed), `ASER`(atmos), `WSER`(wind), `GWMAP`/`GWSEEP`(groundwater), `CWQSERxx`·`WQ*`(water quality) | 도메인 유출입 시계열 | Training p39, p55 |

### 2.2 시계열 입력 파일 공통 카드 파라미터 (Training p49, p63)

`xSER.inp` 계열이 공유하는 헤더 파라미터 (예: PSER p49, QSER p59, SSER/TSER p63):

| 키 | 의미 |
|---|---|
| `M_SER` (MPSER/MQSER/MCSER) | Number of data points |
| `TC_SER` (TCPSER/TCQSER/TCCSER) | 입력 시간단위 → 초 변환 곱 계수 |
| `TA_SER` (TAPSER/TAQSER/TACSER) | Additive time adjustment |
| `RMULADJ` | Multiplying conversion (값 배율) |
| `ADDADJ` | Additive conversion (값 가산) |

### 2.3 경계/강제 입력 상세 (LTPR 사례)

- **Tidal boundary `PSER.inp`** (Training p46-50): 동쪽 단일 open boundary 가 해양 조건 정의. 세 옵션 — (a) elevation 직접 정의(calibration/validation 연도 현행), (b) tidal harmonics(M2·S2·N2·K2·O1·K1·Q1·M4·M6; JTides/ACRIC), (c) Washington stage 회귀(2007/2008 셋업, Xu et al. 2008). harmonics 방식은 정의 후 임의 기간 가능·계산 효율↑ (Training p51).
- **Surface flow `QSER.inp`** (Training p56-58): LTPR 19 source(NS=1~19; Greenville/WWTP/creek/WTP withdrawal·return 등).
- **Groundwater** (Training p59-61): `GWMAP.inp`(zone), `GWSEEP.inp`(rate) — LTPR 4 zone × 2 inflow rate(m/d).
- **Atmosphere `ASER.inp`** (Training p36-38): pressure·dry air temp·RH·rainfall·evaporation·solar radiation·cloud cover. **Wind `WSER.inp`**: speed·direction.

### 2.4 EFDC.inp 카드 구조 (Training p64)

`EFDC.inp` 가 main control: grid 정의·inputs·time steps·output·calibration parameter 를 **"cards"** 형태로 배열. (출력 station 은 Card 87 에 16 station 지정 — Training p98.)

---

## 3. Training Overview — 격자 생성 옵션 (교육 관점)

격자 개발 3 옵션 제시 (Training p27-32):

| 옵션 | 슬라이드 설명 | 인용 |
|---|---|---|
| **GEFDC**(GRIDGEN) | "Original model grid generation program" — boundary point·grid type·relaxation parameter 정의, Cartesian/curvilinear, DOS·text 기반, DXF 출력 | Training p20 |
| **Dynamic Solutions** | "More flexible" — geographic file 로 boundary 정의, 타 격자(Delft RGFGrid/Grid95/SEAGRID) import 가능 | Training p21 |
| **Delft3D RGFGrid** | "Intuitive GUI", active user community·online training video | Training p22 |

격자 셀 = quadrilateral(orthogonal·curvilinear) 집합, 5 grid 파일로 location/orientation/shape 정의 (Training p20). σ-layer 는 "accordion"처럼 신축, 최저 번호가 바닥(LTPR 6 layer) (Training p35).

> 본 옵션 목록은 2013 교육 시점 기준. 현재 DSI 워크플로의 GUI 격자 생성기는 **EFDC_Explorer/Grid+** (아래 §4 hands-on 이 그 후속).

---

## 4. Training Overview — 실행·시나리오·출력 워크플로

### 4.1 실행 (Training p82-85)

Citrix 가상 데스크톱(`appserver.ncwater.org`) 로그인 → 데스크톱 아이콘으로 base case 실행 (교육자료의 `EFDCBaseCase` 작업폴더).

### 4.2 시나리오 개발 (Training p86-94)

4 종 시나리오와 변경 파일:

| 시나리오 | 변경 파일 | 인용 |
|---|---|---|
| 기존 연도 조건 변경 | `QSER`·`TSER`·`SSER.INP` (model year 2001/2003/2007/2008) | Training p88 |
| 신규 시뮬레이션 연도 | QSER·TSER·SSER·ASER·WSER·PSER·TEMP·SALT·DXDY ("significant effort") | Training p89 |
| 해수면 상승(SLR) | TSER·SSER·TEMP·SALT·DXDY·PSER·EFDC.INP | Training p90 |
| 기후변화 영향 | QSER·TSER·SSER·ASER·WSER·PSER·TEMP·SALT·DXDY·EFDC.INP ("large uncertainty, care should be taken") | Training p91 |

운영: `EFDCBaseCase` 디렉토리 복사 → 새 디렉토리에서 입력 수정·실행 (Training p93).

### 4.3 출력 후처리 (Training p95-100)

- 서버에서 `PostProc.exe`(`\EFDC_PostProcessing` 에서 복사)를 scenario 폴더에 두고 실행 (다운로드 시간 절약) (Training p95-97).
- `SALTSxx.out`·`TEMTSxx.out` 16 station(EFDC.INP Card 87) 에서 추출 → top/middle/bottom-two layer 평균 → `TempSalt.csv` 생성 (Training p98).
- percentile 계산: `PostProc.exe` → `PostProcessing.xlsx`(로컬) 에 `TempSalt.csv` 복사 (Training p99-100).

### 4.4 OASIS 연계 제약 (Training p105-107)

LTPR 모델은 특정 4 연도용으로 셋업 → OASIS(장기 time-series 모델) 출력 직접 read 불가, 입력 파일에 hard-wire 필요. 추가 연도 실행 시 boundary·forcing 재구성 필요.

---

## 5. Grid+ Hands-On — New York Harbor 격자 생성 실습

> 표지: "Hands-On with New York Harbor Grid" (Grid p1). EFDC_Explorer 계열 **Grid+** GUI 의 spline 기반 curvilinear 격자 생성 실습. Goals: Grid+ GUI 친숙·overlay 로드·spline draw/edit·grid 생성·orthogonalize·connect·delete·node 이동·refine (Grid p1).

### 5.1 핵심 워크플로 (Step 1~12)

| Step | 작업 | 인용 |
|---|---|---|
| 1 | overlay 파일(`.P2D`) 로드 | Grid p2-4 |
| 2 | spline 생성 — `Add a new spline` 버튼으로 draw, `S`(Select object) 단축키로 선택 모드, RMC→`Export Control Points To…` 로 저장 | Grid p6-9 |
| 2(cont.) | `Create grid from splines` 버튼 → I/J 방향 cell 수 입력 → OK | Grid p10 |
| 3 | 생성 grid 확인 | Grid p11 |
| 4 | grid export/save (grid layer 선택 → `Export to a file`) | Grid p12 |
| 5 | 다음 grid 생성 (두 grid 가 서로 overlay 해야 함) | Grid p13-14 |
| 6 | grid 연결 — 첫 grid 선택 → `Select object` → 첫 node LMC → Shift+두 번째 node LMC → `Merge two grids` | Grid p15-16 |
| 7-8 | branch grid 생성·연결 | Grid p17-18 |
| 9 | island 처리 (아래 §5.2) | Grid p19-34 |
| 10 | orthogonalize (global: grid layer→`Orthogonalize grid`; local: 영역 선택→RMC→`Orthogonalize Grid Block`) | Grid p36-38 |
| 11 | orthogonal deviation 확인 (Average Orthogonal Deviation index) | Grid p39-40 |
| 12 | in-land cell 제거 (`Delete node`) | Grid p41 |

### 5.2 Island 격자 처리 2법 (Grid p19-20)

| 방법 | 절차 | 장단점 |
|---|---|---|
| Method 1 | 본류+island+branch 덮는 domain 생성 후 island cell 삭제 | 쉽고 빠름 / bank fitting 낮음 |
| Method 2 | 본류·branch 만 생성, island 무시 | bank fitting 우수 / 시간↑·난이도↑ |

**Method 2 원칙** (Grid p21): 본류·branch 의 cell 수는 beginning→ending point 까지 유지. branch 가 본류보다 복잡(굴곡·길이)하면 branch 먼저 생성 후 본류 cell 수 정의. beginning point 의 I, J 방향 주의. 실습은 grid06_x → grid07 까지 점진 연결·refine·연결 반복 (예: 2x27, 30x6, 12x2, 115x8, 18x25 grid 생성·merge) (Grid p22-35). 본류 cell 수 = 116-1 = 115 (node index 기준) (Grid p31-32).

### 5.3 추가 기능 (Grid p42-53)

- **Create Rectangular Grid** (Grid p43): 버튼→요건 입력→OK, 후 move/rotate/extend·narrow.
- **Create Radial Grid** (Grid p44): 버튼→요건 입력→OK, move/expand·narrow.
- **Line Smooth** (Grid p45): 두 edge node Shift+LMC→RMC→`Line Smooth` 로 node 간격 균등 재분배. 후 재-orthogonalize 필요.
- **Line Attraction / Line Repulsion** (Grid p46-47): edge node 2 + 세 번째 node 로 영향 영역 정의→RMC→해당 옵션, 특정 점/선 방향으로 node 이동.
- **Fit to Spline** (Grid p48-49): grid node 3개 Shift 선택→RMC→`Fit to Nearest Spline`.
- **Refine grid (Local)** (Grid p50-53; §10 단계에서도 Grid p27): grid segment 의 두 node 선택→`Refine grid` 버튼→multiplier(예: 3) 입력→OK.

---

## 6. 두 자료의 위치 (canonical 경계)

| 자료 | 권위 수준 | 활용 |
|---|---|---|
| Training Overview | 교육 슬라이드(프로젝트 인계용) | 신규 사용자 워크플로 이해·입력 파일 그룹 개요. **이론/수치 단언은 인용 금지** — Theory v12 사용 |
| Grid+ Hands-On | 교육 슬라이드(GUI 조작 절차) | EFDC_Explorer Grid+ 격자 생성 UI 절차. spline·orthogonalize·connect 버튼 흐름 |

- 운영 매뉴얼 격자 생성기(`Cartesian Grid Generator`)는 [`efdc-user-manual-r850.md`](efdc-user-manual-r850.md) §1.2 — 본 hands-on(Grid+) 과 구분.
- 이론·numerical 은 [`efdc-theory-v12-ch2-hydrodynamics.md`](efdc-theory-v12-ch2-hydrodynamics.md).
- 전 자산 인덱스: [`efdc-manuals-overview.md`](efdc-manuals-overview.md).
