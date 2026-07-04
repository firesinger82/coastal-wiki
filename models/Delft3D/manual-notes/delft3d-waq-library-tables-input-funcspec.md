---
title: "Delft3D 잔여 참조문서 인덱스 — WAQ Processes Library Tables + WAQ Input File Description + Functional Specifications/course"
topic: delft3d-waq-library-tables-input-funcspec
canonical_source: self
citation_status: verified
verification_method: "raw/manuals/pdfs 4종 직접 추출 — Delft3D-WAQ_Processes_Library_Tables.pdf(336p, v2026.02 rev80917) List of Tables(pp.iii-iv, 15 tables) + Table 1.1 process listing 샘플(p.8) / Delft3D-WAQ_Input_File_Description.pdf(105p) block 구조(0-10, pp.i-iii) / Delft3D-Functional_Specifications.pdf(38p 'Functional Description') + d3d_fs_course_{hydrodynamics,environmental,wave,engineering}.pdf(각 18/26/17/23p, 'Functional Specifications' v2.20) 모듈 TOC. 본 노트는 index+구조 (336p 표 전문 복제 아님 — CLAUDE.md 규칙 #8 위키=공급원)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — pdftotext TOC/샘플 직접"
verification_date: 2026-07-04
related:
  - models/Delft3D/manual-notes/delft3d-waq-processes-tech-reference.md
  - models/Delft3D/manual-notes/delft3d-waq-user-manual.md
  - models/Delft3D/manual-notes/delft3d-manuals-overview.md
  - models/Delft3D/source-analysis/delft3d_waq_process_library.md
---

# Delft3D 잔여 참조문서 인덱스 — WAQ Library Tables · Input File Description · Functional Specifications

> AUDIT-LEDGER §2.1 의 🟡/⬜ 잔여 3종을 종결하는 index 노트. [[delft3d-waq-processes-tech-reference]] 가 "본 매뉴얼 범위 밖 — Processes Library Tables·Input File Description" 로 남겨둔 gap 을 채운다.
> 이 문서들은 **reference(자동생성 표)·conceptual(모듈 개요)** 성격이라 식·알고리즘이 없다. 위키는 공급원이므로 (CLAUDE.md #8) 336p 표 전문을 복제하지 않고 **구조 인덱스 + 대표 엔트리 + 위치(테이블·블록·페이지)** 만 canonical 화한다.

## 1. WAQ Processes Library Tables (336p, v2026.02 rev80917, 3 May 2026)

D-Water Quality **Processes Library** (프로세스 라이브러리) 의 **자동생성 reference 표 모음** — [[delft3d_waq_process_library]] source-analysis 의 unique-name/관계 인덱스 실물. 15개 표 (List of Tables, pp.iii-iv):

| # | Table | 시작 p (문서) | 내용 |
|--:|---|--:|---|
| 1 | Listing of DELWAQ processes | 2 | 전 프로세스 unique name + 설명 + 문서화 코드 |
| 2 | Per substance: modelled fluxes | 16 | 상태변수별 관여 flux |
| 3 | Per substance: modelled velocities | 68 | 상태변수별 (침강 등) velocity |
| 4 | Per substance: modelled dispersion | 74 | 상태변수별 dispersion |
| 5 | Listing of the modelled fluxes | 75 | 전 flux 목록 |
| 6 | Listing of the modelled velocities | 132 | 전 velocity 목록 |
| 7 | Listing of the modelled dispersions | 138 | 전 dispersion 목록 |
| 8 | Segment input **from other processes** | 139 | 프로세스간 입력 의존 |
| 9–10 | Segment input **with default value** | 163/165 | 기본값 있는 세그먼트 입력 |
| 11 | Exchange input with default value | 273 | 기본값 있는 exchange 입력 |
| 12–13 | Segment/Exchange input **without default** | — | 사용자 필수제공 입력 |
| 14–15 | Segment/Exchange output **not used by other** | — | 최종출력 (타 프로세스 미소비) |

**대표 엔트리** (Table 1.1, p.8) — 프로세스 unique name · 설명 · 문서화코드:

| unique name | 설명 | doc code |
|---|---|---|
| `CalcRadDay` | Actual radiation at segment boundaries | CLCRAD |
| `Daylength` | Daylength calculation | DAYL |
| `Reflection` | Reflection calculation | REFL |
| `vtrans` | Vertical mixing distribution over a period | VTRANS |
| `EffMBlo_P` | Momentaneous efficiency of phytoplankton (BLOOM) | EFFBLO |

> 표의 4계층 구조 = **process → substance → (flux/velocity/dispersion) → (input needed / output produced)**. 즉 라이브러리를 실행 그래프로 본 매뉴얼. 상세 process 방정식은 [[delft3d-waq-processes-tech-reference]] (WAQ_Processes_Technical_Reference 611p) 소관, 본 문서는 **인덱스/관계표**만.

## 2. WAQ Input File Description (105p)

DELWAQ 입력파일(`.inp`) 형식 정의 — **10 블록 순차 구조**. GUI 없이 DELWAQ 직접구동/디버깅 시 참조. (§0.4 markup/convenience options + glossary.)

| block | 제목 | 시작 p | 핵심 |
|--:|---|--:|---|
| 0 | A guide to this manual | — | 규약·glossary·markup |
| 1 | Identification, selected substances | 7 | first line·version·title·substance 수/이름 |
| 2 | Timers, integration, monitoring | — | time factor·**integration procedure**·monitoring 위치/transect·output timers·stationary solvers |
| 3 | Grid and values of the volumes | — | UGRID/hyd-file grid·계산 volume 수 |
| 4 | Hydrodynamic data | — | flow/area/velocity·dispersion 등 (block 순번 4, 서술위치 뒤) |
| 5 | Open boundary conditions | — | 개방경계 |
| 6 | Loads and withdrawals | — | 부하·취수 |
| 7 | Process steering | — | 활성 프로세스·상수/함수 (Library 연계) |
| 8 | Initial conditions | — | 초기 상태변수 |
| 9 | Model output | — | 출력변수/그리드 |
| 10 | Statistical output | — | 통계후처리 |

> block 7 (Process steering) 이 §1 Library Tables 와 결합 지점 — 여기서 활성화한 프로세스가 라이브러리 flux/velocity 표를 실행 그래프로 소환. 사용자 GUI 경로는 [[delft3d-waq-user-manual]] 소관.

## 3. Functional Specifications / course PDFs (개념·교육 overview)

식이 없는 **모듈 개요(Functional Description)** 문서군. 각 모듈: *Module description · Application areas · Coupling with other modules* 3항 + pre/post-processing + hardware. 인허가/제안서용 상위 서술로, canonical 기술내용은 각 모듈 User Manual 이 소관.

### 3.1 Delft3D-Functional_Specifications.pdf (38p, 'Functional Description')

6 모듈 개요: **Hydrodynamic(§2) · Water quality(§3) · Sediment transport(§4, cohesive/non-cohesive/limitations) · Ecological(§5) · Particle tracking(§6) · Wave(§7)**. framework overview + utilities (§1).

### 3.2 d3d_fs_course_*.pdf — 도메인별 Functional Specifications (v2.20, rev80611)

course/교육 자료 성격의 도메인 특화 스펙:

| 파일 | p | 모듈 초점 | 특이 §|
|---|--:|---|---|
| `d3d_fs_course_hydrodynamics` | 18 | Hydrodynamic module (§2) | pre/post §3: QUICKPLOT·grid gen·**tidal analysis/prediction(§3.5-3.7)**·nesting FLOW/WAQ·GIS/Matlab interface |
| `d3d_fs_course_environmental` | 26 | Water quality(§2)·Sediment(§3)·Ecological(§4)·Particle tracking(§5) | sediment cohesive/non-cohesive/limitations(§3.1) |
| `d3d_fs_course_wave` | 17 | Wave module (§2, SWAN) | 동일 pre/post + nesting |
| `d3d_fs_course_engineering` | 23 | Hydrodynamic(§2)·Wave(§3)·**Morphodynamic(§4, numerical aspects)** | morphodynamic module 수치측면 §4.2 |

> 이 4종은 상호 §1(Introduction/framework/utilities) 및 §pre-post 가 중복되며, 실질 신규정보는 **도메인 모듈 배치 + morphodynamic(engineering) / tidal analysis(hydrodynamics) 강조**뿐. 심화 canonical 은 각각 [[delft3d-flow-user-manual]](수력·morphology) · [[delft3d-wave-user-manual]](파랑) · [[delft3d-waq-user-manual]](수질) 소관.

## 4. 종결 판정

- **Library Tables / Input File Description**: reference index/입력형식 — 구조·대표엔트리 canonical 화 완료. 개별 프로세스 방정식·전 flux 목록 전수는 **불요**(자동생성 표 = 위키 공급원 원칙상 소스매뉴얼 포인터로 충분, CLAUDE.md #8).
- **Functional Spec / course**: conceptual overview — 식 없음, 모듈 배치·응용만. index 화 완료, deep 불요.
- → AUDIT-LEDGER §2.1 "Library Tables·Input Desc(🟡)·Functional Spec·course(⬜)" **종결**. Delft3D 문서 잔여 실질 소진 (도구 GUI 매뉴얼 S-tier·doxygen 자동생성 제외).

## 5. 관련

- [[delft3d-waq-processes-tech-reference]] — 프로세스 방정식 611p (본 노트가 남긴 gap 채움 대상이었던 그 노트)
- [[delft3d-waq-user-manual]] · [[delft3d_waq_process_library]] (source-analysis) — GUI/코드 경로
- [[delft3d-manuals-overview]] — 53 PDF 전체 인덱스
- [[delft3d-flow-user-manual]] · [[delft3d-wave-user-manual]] — Functional Spec 상위서술의 canonical 소관
