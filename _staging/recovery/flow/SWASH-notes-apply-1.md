---
title: "SWASH 대조 보고서 노트 반영 — 작업 1"
model: SWASH
canonical_source: self
citation_status: verified
last_source_check: "2026-10-15 (recovery 대조 반영)"
verification_method: "2026-10-15 SWASH recovery 대조 보고서 반영"
note_author: "Codex"
note_date: 2026-10-15
verification_by: "Codex — 배정 행과 노트 수정안 대조"
verification_date: 2026-10-15
---

# SWASH 대조 보고서 노트 반영 — 작업 1

배정 기준은 [SWASH-note-job-1.tsv](../assign/SWASH-note-job-1.tsv)이다.
배정표의 `source-analysis/swash-input-parsing-check.md` 행 수는 96개이다.
배정표의 `manual-notes/swash-tech-documentation-overview.md` 행 수는 4개이다.

파일별 반영 결과는 해당 파일을 마칠 때 아래에 덧붙인다.

## 입력 파싱 노트

대상은 [swash-input-parsing-check.md](../../../models/SWASH/source-analysis/swash-input-parsing-check.md)이다.
추가한 차이 표의 행 수는 96개이다.
배정표의 이 파일 행 수는 96개이다.
차이 절의 줄 범위는 `models/SWASH/source-analysis/swash-input-parsing-check.md:312–415`이다.
구분용 빈 줄을 포함한 추가 줄 범위는 `models/SWASH/source-analysis/swash-input-parsing-check.md:311–415`이다.
차이 표의 배정 행 범위는 `models/SWASH/source-analysis/swash-input-parsing-check.md:320–415`이다.

| 수정 줄 범위(파일:줄) | 내용 |
|---|---|
| `models/SWASH/source-analysis/swash-input-parsing-check.md:7–8` | frontmatter |
| `models/SWASH/source-analysis/swash-input-parsing-check.md:60–63` | COMPUTE 반환과 호출 반복 |
| `models/SWASH/source-analysis/swash-input-parsing-check.md:73–76` | KEYWIS·INKEYW·UNC |
| `models/SWASH/source-analysis/swash-input-parsing-check.md:124` | 명령 구문·파서 매핑 근거 |
| `models/SWASH/source-analysis/swash-input-parsing-check.md:144–145` | 1D X 반복 검사 |
| `models/SWASH/source-analysis/swash-input-parsing-check.md:201–203` | 삼각형 각도 경고 |
| `models/SWASH/source-analysis/swash-input-parsing-check.md:235–245` | 오류 수준과 MAXERR·STPNOW |
| `models/SWASH/source-analysis/swash-input-parsing-check.md:280` | CFL 순서 검사 |
| `models/SWASH/source-analysis/swash-input-parsing-check.md:306–307` | 검사와 허용 오류 수준 |
| `models/SWASH/source-analysis/swash-input-parsing-check.md:310` | source-needed 작업 메모 정정 |

| 보고서 | 반영한 수정안 행 ID | 반영 내용 |
|---|---|---|
| [theory-framework](../compare/swash-theory-framework-vs-code.md) | ST1-340 | mimetic 시간적분 검사 설명을 유지했다. |
| [inputs-setup](../compare/swash-inputs-setup-vs-code.md) | SI1-098 참조, SI1-509 참조, SI1-705, SI1-706, SI1-707 | 목적 주석을 유지했다.<br>COMPUTE 반환과 1D X 반복 검사를 추가했다.<br>UNC 설명과 오류 수준, 각도 경고를 정정했다. |
| [inputs-physics-numerics](../compare/swash-inputs-physics-numerics-vs-code.md) | SI2-292 | CFL 순서 조건을 정정했다. |
| [outputs](../compare/swash-outputs-vs-code.md) | SO1-306, SO1-307 | STOP의 조건 구분과 DIAGNOSTIC 헤더 설명을 유지했다. |
| [guide-syntax-build](../compare/swash-guide-syntax-build-vs-code.md) | SG1-920, SG1-921, SG1-922, SG1-923, SG1-924, SG1-925 | UNC 설명과 오류 수준, CFL 순서 조건을 정정했다.<br>INCLUDE 설명과 PRINT 호출 조건을 유지했다.<br>source-needed 작업 메모를 보고서의 명령 구문·파서 매핑 근거로 바꿨다. |

배정 행의 중복·누락은 없다.
표의 각 배정 행은 6개 칸을 갖는다.
넣지 않은 배정 행은 없다.

## 기술문서 개요 노트

대상은 [swash-tech-documentation-overview.md](../../../models/SWASH/manual-notes/swash-tech-documentation-overview.md)이다.
추가한 차이 표의 행 수는 4개이다.
배정표의 이 파일 행 수는 4개이다.
차이 절의 줄 범위는 `models/SWASH/manual-notes/swash-tech-documentation-overview.md:102–113`이다.
구분용 빈 줄을 포함한 추가 줄 범위는 `models/SWASH/manual-notes/swash-tech-documentation-overview.md:101–113`이다.
차이 표의 배정 행 범위는 `models/SWASH/manual-notes/swash-tech-documentation-overview.md:110–113`이다.

| 수정 줄 범위(파일:줄) | 내용 |
|---|---|
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:7–8` | frontmatter |
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:21` | 과거 manual-notes=0 작업 메모 정정 |
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:39` | 제4장 상태 |
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:56` | mimetic 이론의 설계 동기 |
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:59` | 곡선 격자 계량의 문서 범위 |
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:67–74` | 수평 이류의 기본값과 자동 선택 조건 |
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:78–80` | 제8장과 sigmal layers 원문 |
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:82` | 기존 TRIWAQ 설명을 별도 문단으로 보존 |
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:91–93` | SIP 미지수와 BiCGSTAB 구별 |
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:95` | 문서 내용 범위 절 제목 |
| `models/SWASH/manual-notes/swash-tech-documentation-overview.md:98–100` | 미완성 장 목록과 면적 식 |

| 보고서 | 반영한 수정안 행 ID | 반영 내용 |
|---|---|---|
| [theory-framework](../compare/swash-theory-framework-vs-code.md) | ST1-319, ST1-320, ST1-321 | 제4장 상태와 미완성 장 목록을 정정했다.<br>mimetic 설명을 이론의 설계 동기로 고쳤다.<br>곡선 격자 코드의 면적 식을 연결했다. |
| [theory-unstructured](../compare/swash-theory-unstructured-vs-code.md) | ST2-379, ST2-209, ST2-216 | 이류 기본값과 자동 선택 조건을 연결했다.<br>sigmal layers 원문 표기를 정정했다.<br>SIP 호출 대상을 압력 보정·수평 속도 성분으로 정정했다. |
| [callflow](../flow/SWASH-callflow.md) | §6.1 개요 노트 행, RF-005 참조 | 제9장의 under preparation 행을 유지했다.<br>인쇄 p.103과 PDF p.111의 대응을 유지했다. |

배정 행의 중복·누락은 없다.
표의 각 배정 행은 6개 칸을 갖는다.
넣지 않은 배정 행은 없다.

## 최종 대조 결과

집계 기준은 [SWASH-note-job-1.tsv](../assign/SWASH-note-job-1.tsv)의 파일별 행 ID이다.

| 파일 | 배정표 행 수 | 노트 표 행 수 | 넣지 않은 행 |
|---|---|---|---|
| [swash-input-parsing-check.md](../../../models/SWASH/source-analysis/swash-input-parsing-check.md) | 96 | 96 | 없음 |
| [swash-tech-documentation-overview.md](../../../models/SWASH/manual-notes/swash-tech-documentation-overview.md) | 4 | 4 | 없음 |

배정표의 전체 행 수는 100개이다.
두 노트 차이 표의 전체 배정 행 수는 100개이다.
노트의 배정 행 ID와 결론은 배정표와 일치한다.
중복·누락·추가 배정 행은 없다.
E 행의 결론 문장에는 강함 판정을 보존했다.
보고서가 유지하도록 한 문장은 기존 원문과 일치한다.
노트의 기존 citation_status는 유지했다.
두 노트와 이 기록의 last_source_check는 `2026-10-15 (recovery 대조 반영)`이다.
두 노트의 표는 각 배정 행에 6개 칸을 갖는다.
노트와 이 기록의 링크는 상대 링크이다.
넣지 않은 행과 그 이유는 없다.
