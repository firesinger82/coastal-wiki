---
title: "EFDC+ Documentation Release 8.5.0 (DSI 2021) — User Manual TOC + Input Files 구조"
topic: efdc-user-manual-r850
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/manuals/pdfs/EFDC_Manual.pdf 표지·TOC pages 1-5 직접 추출 — EFDC+ Documentation Release 8.5.0, DSI LLC, Sep 15 2021. 표지·Contents 페이지 의 챕터 구조·페이지 번호 직접 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — PDF Read pages 1-5 직접 확인"
verification_date: 2026-05-24
related:
  - models/EFDC/manual-notes/efdc-manuals-overview.md
  - models/EFDC/manual-notes/efdc-theory-doc-v12.md
  - models/EFDC/README.md
  - models/EFDC/source-analysis/efdc-tidal-forcing-conventions-v12.md
---

# EFDC+ Documentation Release 8.5.0 — User Manual

> 출처: [`models/EFDC/raw/manuals/pdfs/EFDC_Manual.pdf`](../raw/manuals/pdfs/EFDC_Manual.pdf) (DSI LLC, Sep 15 2021, 1.7 MB). 표지 페이지 직접 인용.

## 1. 자료 식별

| 항목 | 값 |
|---|---|
| 제목 | EFDC+ Documentation Release 8.5.0 |
| 발행 | DSI, LLC (Edmonds WA) |
| 날짜 | Sep 15, 2021 |
| 파일 | `EFDC_Manual.pdf` |
| 크기 | 1.7 MB |
| 페이지 | 표지 + Contents (p.i) + 80p+ 본문 |
| 단일 챕터 | Chapter 1 INTRODUCTION |

## 2. Contents (p.i, 직접 인용)

```
1 Introduction                                                    1
  1.1 Getting Started                                              1
    1.1.1 Build Instructions                                       2
    1.1.2 Running                                                  3
  1.2 Cartesian Grid Generator User Guide                          6
    1.2.1 Generate Uniform Grid                                    8
    1.2.2 Generate Radial Grid                                     12
    1.2.3 Generate Telescoping Grid                                12
    1.2.4 Import Grids from Files                                  13
  1.3 Input Files                                                  15
    1.3.1 Primary Run Control                                      15
    1.3.2 Required Spatial Files                                   66
    1.3.3 General Transport                                        68
    1.3.4 Sediment                                                 70
    1.3.5 Wave Parameter Files                                     71
    1.3.6 Eutrophication Module                                    71
    1.3.7 Toxics Module                                            72
    1.3.8 Temperature Module                                       73
  1.4 Output Files                                                 73
    1.4.1 Output Files                                             73
    1.4.2 GetEFDC                                                  74
  1.5 Sample Models                                                77
    1.5.1 Lake 2D Test Case                                        77
    1.5.2 Ohio River Test Case                                     78
    1.5.3 Lake Washington Test Case                                79
  1.6 License                                                      80
```

## 3. 챕터별 활용 가이드

### 3.1 §1.1 Getting Started (p.1-5)

- §1.1.1 Build Instructions (p.2) — CMake 빌드, 플랫폼별
- §1.1.2 Running (p.3) — 실행 명령·표준 파일 트리

운영 첫 단계. 빌드 문제 발생 시 [`efdc-manuals-overview.md`](efdc-manuals-overview.md) §4 의 `EFDC_Implementation_Guide.pdf` 참조.

### 3.2 §1.2 Cartesian Grid Generator (p.6-14)

EFDC+ 의 격자 생성 도구. 4 옵션:
- **Uniform** (p.8) — 가장 단순, 직사각형
- **Radial** (p.12) — 방사형 (포구·항만 round)
- **Telescoping** (p.12) — 점진적 해상도 (해안 zoom)
- **Import** (p.13) — 외부 격자 가져오기

연안 모델링에서는 보통 Telescoping (외해 coarse → 해안 fine).

### 3.3 §1.3 Input Files (p.15-73) — 운영 핵심

**EFDC+ 의 8 input file family**:

| § | Family | 시작 페이지 | 특기 |
|---|---|---:|---|
| 1.3.1 | Primary Run Control | 15 | **51 페이지** (15-66) — 가장 큼. EFDC.INP·CELL.INP 등 main config |
| 1.3.2 | Required Spatial Files | 66 | Grid + bathymetry + cell connectivity |
| 1.3.3 | General Transport | 68 | salt + temperature + dye 일반 transport |
| 1.3.4 | Sediment | 70 | SedTran Original + SEDZLJ inputs |
| 1.3.5 | Wave Parameter Files | 71 | wave forcing (SWAN 결합 등) |
| 1.3.6 | Eutrophication Module | 71 | CE-QUAL-ICM kinetics |
| 1.3.7 | Toxics Module | 72 | contaminant (Hg·PCB 등) |
| 1.3.8 | Temperature Module | 73 | heat balance 별도 |

**§1.3.1 의 51 페이지 분량** → Primary Run Control 이 압도적 — 신규 사용자 학습 시 여기 집중.

> ⚠️ **v12.4 소스 드리프트 (검증 2026-07)**: 이 매뉴얼(R8.5.0, 2021)의 §1.3.1 입력 카드 기술은 EFDC+ **v12.4 소스와 다수 항목에서 어긋난다** — 매뉴얼을 액면 그대로 믿지 말 것. v12.4 `EFDCPlus_Stable` 소스 직접 확인(2026-07-04) 결과 요지:
>
> - **C3**: `IDRYCK`·`FILT3TL` 식별자는 v12.4에 존재하지 않음. 실제 read = `RP RSQM ITERM IRVEC IATMP IWDRAG ITERHPM ldum ISDSOLV tmp` (`input.f90:225`). `IRVEC`은 0/9만 허용, 99는 `STOPP` (`input.f90:237`).
> - **C6**: 3·6·7·8번째 슬롯(`ISCDCA` 등)은 `ldum` 더미로 버려짐 (`input.f90:306`).
> - **C8**: `TREF`/`CORIOLIS` → v12.4 이름 `TIDALP`/`CF`, 같은 슬롯 (`input.f90:387`).
> - **C12A**: 첫 슬롯 `ISSTAB` → v12.4 `ISTOPT(0)` + 9번째 `BC_EDGEFACTOR` 추가 (`input.f90:646`).
> - **C2A**: 매뉴얼 미기재이나 v12.4는 continuation restart(`ISRESTI==1 && ICONTINUE==1`) 시 `Restart_In_Ver`·`RESTARTF` 2줄을 읽음 (`input.f90:198-200`).
> - **C22B(Shellfish)**: v12.4는 SEEK하지 않음(미독) — JSON(`READ_SHELLFISH_JSON`)으로 대체 (`input.f90:3941-3943`).
> - **C66A/B·C68–C70·C73–C83·C89–C90**: v12.4가 SEEK하지 않음(미독). C66·C67·C71/A/B·C72·C84–C88·C91/A/B/C만 잔존.
> - **mask.inp MTYPE**: v12.4는 1=U, 2=V, 3=U+V, **4=isolated waters(네 면)** (`cellmask.f90:50-66`).
> - **C17 조석 위상**: 절대 `TIMESEC` 기준 합성(η=PFAM·cos(2π(TIMESEC−PFPH)/TCP)), PFPH는 초 단위 lag. nodal 보정 내장 없음.
> - **wser `ISWDINT=2`(성분 입력)**: 런타임은 항상 풍속/풍향으로 해석 — 성분 입력은 오독됨 (`caltsxy.f90:244-251`).
>
> 카드별 상세 주석: [[efdc-implementation-guide]] §6.3의 ⚠️ 블록들. 조석·바람 강제력 규약(위상 페어링·nodal fallback 포함): [[efdc-tidal-forcing-conventions-v12]].

### 3.4 §1.4 Output Files + GetEFDC (p.73-77)

- §1.4.1 Output Files (p.73) — 표준 출력 file types (TSR·EFDC outputs)
- §1.4.2 GetEFDC (p.74) — EFDC+ 형식 binary timeseries 추출 유틸리티

post-processing 핵심 — [DSI GetEFDC GitHub](https://github.com/dsi-llc) 별도 utility.

### 3.5 §1.5 Sample Models (p.77-80)

운영 학습용 3 case:
- **Lake 2D** (p.77) — 가장 단순한 2D 호수
- **Ohio River** (p.78) — 1D 하천
- **Lake Washington** (p.79) — 3D 호수 (수질 포함)

신규 사용자 → Lake 2D 부터.

### 3.6 §1.6 License (p.80)

EFDC+ GPL-3.0 (DSI LLC). 상업 사용은 별도 라이선스.

## 4. 한국 적용 운영 cheat-sheet

| 한국 적용 | r8.5.0 참조 | 비고 |
|---|---|---|
| 항만 내 해수 교환 | §1.2.2 Radial Grid + §1.3.1-2 | 부산항·울산항 패턴 |
| 하구·연안 표사 | §1.3.4 Sediment | SEDZLJ 또는 SedTran 선택 → Theory v12 §6 |
| 적조·DO 모델 | §1.3.6 Eutrophication | 한국 남해 적조 |
| 발전소 온배수 | §1.3.8 Temperature | 영광·고리 등 |
| 항만 propwash | §1.3.5 Wave + EFDC+_Propwash_WhitePaper | 별도 모듈 |

## 5. 작성 우선순위 (남은 작업)

- §1.3.1 Primary Run Control 51 페이지 의 EFDC.INP 카드 family 매핑 (별도 노트 후보)
- §1.3.4 Sediment input cards + SedTran/SEDZLJ 선택 절차 (별도 노트)
- Sample Models 3 case 의 input file 실제 예제 분석

## 6. 관련 자료

- [[efdc-manuals-overview]] — 6 manuals 인덱스
- [[efdc-theory-doc-v12]] — 이론 reference (운영 시 식 의미 확인)
- [`models/EFDC/source-analysis/`](../source-analysis/) — codex source-code 분석 (운영 카드 ↔ Fortran 매핑)
- 외부: [DSI EFDC+ Documentation Online](https://www.eemodelingsystem.com/EFDC_Documentation/)
