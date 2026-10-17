---
title: FUNWAVE 대조 결론 노트 반영 기록 — 작업 8
citation_status: verified
last_source_check: "2026-10-18 (recovery 대조 반영)"
verification_method: "2026-10-18 FUNWAVE recovery 대조 보고서 반영"
---

# FUNWAVE 대조 결론 노트 반영 기록 — 작업 8

배정 근거는 [FUNWAVE-note-job-8.tsv](../assign/FUNWAVE-note-job-8.tsv)다.
배정표의 GPU 노트 행 수는 46개다.
배정표의 소스 지도 노트 행 수는 26개다.
배정표의 검증 사례 노트 행 수는 10개다.

## 파일별 반영 결과

### GPU CUDA 포팅 노트

대상 파일은 [funwave-gpu-cuda-port.md](../../../models/FUNWAVE/source-analysis/funwave-gpu-cuda-port.md)다.
추가·수정 범위는 `models/FUNWAVE/source-analysis/funwave-gpu-cuda-port.md:7–8,20–21,35,39–40,54,135,138,171,182,199,215,221,232,238–293,295–305`이다.
차이 표 범위는 `models/FUNWAVE/source-analysis/funwave-gpu-cuda-port.md:247–292`이다.
넣은 행 수는 배정표의 46행과 같다.
반영한 수정안 행 ID는 `aux-docs-build:FN1-923·FN1-924`와 `gpu-vs-tvd:FG1-904·FG1-878 참조·FG1-602 참조·FG1-849 참조·FG1-482 참조`다.
`theory-numerics:FT1-288`의 Makefile 두 대입 설명을 유지했다.
`callflow` §6의 `phi_exch_cuda` generic 인터페이스 설명을 유지했다.
`gpu-vs-tvd` §4 끝의 보고서 연결 목록을 반영했다.
넣지 않은 배정 행은 없다.

### 소스 지도 노트

대상 파일은 [funwave-source-map.md](../../../models/FUNWAVE/source-analysis/funwave-source-map.md)다.
추가·수정 범위는 `models/FUNWAVE/source-analysis/funwave-source-map.md:5–6,14–15,25–31,33,39,44,60–360,364–367`이다.
차이 표 범위는 `models/FUNWAVE/source-analysis/funwave-source-map.md:72–97`이다.
계산 흐름도 절 범위는 `models/FUNWAVE/source-analysis/funwave-source-map.md:99–360`이다.
넣은 행 수는 배정표의 26행과 같다.
반영한 수정안 행 ID는 `theory-numerics:FT1-289`, `inputs:FI1-319·FI1-320`, `v21-manual:FV1-574·FV1-575·FV1-576·FV1-577·FV1-578·FV1-579`, `aux-docs-build:FN1-901·FN1-902·FN1-920`, `gpu-vs-tvd:FG1-802 참조`, `callflow:RF-043·RF-044·RF-045`다.
callflow §4의 Mermaid 블록 3개는 노트의 블록 3개와 글자 단위로 일치한다.
노트는 callflow의 b35·c36 정정이 반영된 현재 블록을 수록한다.
노트는 callflow의 렌더 확인 기록을 연결한다.
넣지 않은 배정 행은 없다.

### 검증 사례 노트

대상 파일은 [funwave-validation-cases.md](../../../models/FUNWAVE/manual-notes/funwave-validation-cases.md)다.
추가·수정 범위는 `models/FUNWAVE/manual-notes/funwave-validation-cases.md:7–8,86–88,101,135–153`이다.
차이 표 범위는 `models/FUNWAVE/manual-notes/funwave-validation-cases.md:144–153`이다.
넣은 행 수는 배정표의 10행과 같다.
반영한 수정안 행 ID는 `v21-examples:FV2-407·FV2-408`이다.
`examples:FX1-917`이 가리킨 2.1의 절 번호 설명을 유지했다.
넣지 않은 배정 행은 없다.

## 최종 확인

[배정표](../assign/FUNWAVE-note-job-8.tsv)의 82행은 세 노트의 82개 고유 행 ID와 일치한다.
각 행의 결론은 해당 보고서의 최종 차이 결론과 일치한다.
A 행의 결론 문장에는 커밋 HASH와 날짜가 있다.
E 행의 결론에는 강도가 있다.
각 차이 표의 열 수는 지정한 6개다.
세 노트와 이 기록의 상대 링크는 파일 대상 존재 검사를 통과했다.
세 노트는 `git diff --check`를 통과했다.
