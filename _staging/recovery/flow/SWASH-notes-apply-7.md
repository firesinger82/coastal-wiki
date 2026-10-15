---
title: "SWASH 대조 결론 노트 반영 — 작업 7"
canonical_source: self
citation_status: verified
note_author: "Codex"
note_date: 2026-10-15
verification_by: "Codex"
verification_date: 2026-10-15
verification_method: "2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
---

# SWASH 대조 결론 노트 반영 — 작업 7

배정 기준은 [SWASH-note-job-7.tsv](../assign/SWASH-note-job-7.tsv)이다.
배정표의 `source-analysis/`는 `models/SWASH/source-analysis/`를 가리킨다.
배정표의 행 수는 초기화 노트 43개, 시간 적분 노트 22개, 부유체 노트 14개, 비정수압 노트 5개이다.
파일별 반영 결과는 각 파일을 마칠 때 아래에 덧붙인다.

## swash-initialization-grid.md

- 대상: [초기화·격자 노트](../../../models/SWASH/source-analysis/swash-initialization-grid.md).
- 추가·수정 줄 범위: `models/SWASH/source-analysis/swash-initialization-grid.md:7–8`, `models/SWASH/source-analysis/swash-initialization-grid.md:52–60`, `models/SWASH/source-analysis/swash-initialization-grid.md:62–64`, `models/SWASH/source-analysis/swash-initialization-grid.md:89–93`, `models/SWASH/source-analysis/swash-initialization-grid.md:95–97`, `models/SWASH/source-analysis/swash-initialization-grid.md:123–125`, `models/SWASH/source-analysis/swash-initialization-grid.md:146–151`, `models/SWASH/source-analysis/swash-initialization-grid.md:209`, `models/SWASH/source-analysis/swash-initialization-grid.md:213–219`, `models/SWASH/source-analysis/swash-initialization-grid.md:302–354`.
- 넣은 행 수: 43개이다. 배정표의 해당 파일 43개 행과 같다.
- 반영한 수정안 행 ID: `inputs-setup:SI1-120`, `inputs-setup:SI1-503`, `inputs-setup:SI1-708`, `inputs-setup:SI1-709`, `inputs-setup:SI1-513`, `inputs-setup:SI1-260`, `theory-framework:ST1-328`, `theory-unstructured:ST2-383`.
- 기존 도메인 분할 설명에는 `guide-syntax-build:SG1-902`와 `theory-unstructured:ST2-422`의 최종 결론을 반영했다.
- 넣지 않은 배정 행: 없다.

## swash-timestepping-update-driver.md

- 대상: [시간 적분·갱신 드라이버 노트](../../../models/SWASH/source-analysis/swash-timestepping-update-driver.md).
- 추가·수정 줄 범위: `models/SWASH/source-analysis/swash-timestepping-update-driver.md:7–8`, `models/SWASH/source-analysis/swash-timestepping-update-driver.md:63–67`, `models/SWASH/source-analysis/swash-timestepping-update-driver.md:73–79`, `models/SWASH/source-analysis/swash-timestepping-update-driver.md:145`, `models/SWASH/source-analysis/swash-timestepping-update-driver.md:159–163`, `models/SWASH/source-analysis/swash-timestepping-update-driver.md:245–535`.
- 넣은 행 수: 22개이다. 배정표의 해당 파일 22개 행과 같다.
- 반영한 수정안 행 ID: `theory-framework:ST1-325 (기존 호출 표 유지)`, `theory-unstructured:ST2-151`, `guide-syntax-build:SG1-926 (20단계 조건 유지)`, `callflow:RF-010`, `callflow:RF-012 (RF-016 결함 후보 연결)`, `callflow §6.2 드라이버의 시간 값`.
- callflow §6.1의 일치한 호출 순서와 기존 출력·종료 설명은 유지했다.
- 계산 흐름도는 callflow §4의 Mermaid 원문 3개를 옮겼다. 세 블록의 문자열은 입력 보고서와 같다.
- 렌더 확인 담당은 사용자 지시에 따라 Claude이다.
- 넣지 않은 배정 행: 없다.

## swash-floating-rigid-body.md

- 대상: [부유체·강체 노트](../../../models/SWASH/source-analysis/swash-floating-rigid-body.md).
- 추가·수정 줄 범위: `models/SWASH/source-analysis/swash-floating-rigid-body.md:7–8`, `models/SWASH/source-analysis/swash-floating-rigid-body.md:18`, `models/SWASH/source-analysis/swash-floating-rigid-body.md:25–27`, `models/SWASH/source-analysis/swash-floating-rigid-body.md:75–85`, `models/SWASH/source-analysis/swash-floating-rigid-body.md:210–211`, `models/SWASH/source-analysis/swash-floating-rigid-body.md:220–250`.
- 넣은 행 수: 14개이다. 배정표의 해당 파일 14개 행과 같다.
- 반영한 수정안 행 ID: `inputs-setup:SI1-569 (기존 가속도·속도·변위 식 유지; 읽기 기본값·준비 보정·수렴 기준 추가)`, `inputs-setup:SI1-563`, `outputs:SO1-305 (기존 출력 설명 유지; 출력 단위 근거 연결)`.
- 기존 FSI 미확인 문장은 보고서의 수렴 조건과 절대·상대 기준으로 바꿨다. 근거는 `inputs-setup:SI1-567`·`SI1-568`이다.
- 넣지 않은 배정 행: 없다.

## swash-nonhydrostatic-pressure-solver.md

- 대상: [비정수압 압력 솔버 노트](../../../models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md).
- 추가·수정 줄 범위: `models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md:6–7`, `models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md:52–53`, `models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md:59`, `models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md:75–81`, `models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md:86`, `models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md:89–104`, `models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md:106–112`.
- 넣은 행 수: 5개이다. 배정표의 해당 파일 5개 행과 같다.
- 반영한 수정안 행 ID: `inputs-physics-numerics:SI2-181`, `theory-framework:ST1-326`, `theory-framework:ST1-327`, `theory-unstructured:ST2-225 (격자 조건 보완; 차이 표에는 추가하지 않음)`.
- 기존 후속 시간 적분 항목은 `guide-syntax-build:SG1-101`의 방법 선택 문장으로 바꿨다.
- 기존 링크는 상대 Markdown 링크로 바꿨다.
- 넣지 않은 배정 행: 없다.

## 최종 확인

- 배정표의 84개 행을 모두 반영했다. 파일별 행 수는 43·22·14·5개이다.
- 차이 표의 행 ID와 결론 분류는 배정표와 같다.
- 차이 표의 중복 행과 누락 행은 없다.
- H 또는 일치 판정의 행은 차이 표에 없다.
- A 행의 결론 문장에는 커밋 HASH와 날짜를 보존했다.
- E 행의 결론에는 보고서 최종 강도를 보존했다.
- 표의 각 행은 지정한 여섯 칸을 갖는다.
- 상대 링크의 파일 대상은 모두 존재한다.
- 네 노트의 기존 citation_status는 유지했다.
- 네 노트의 last_source_check와 verification_method는 요청한 값으로 갱신했다.
- 대상 파일의 `git diff --check`는 통과했다.
- 넣지 않은 배정 행과 수정안 행은 없다.
