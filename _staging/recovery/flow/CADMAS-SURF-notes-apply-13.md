---
title: "CADMAS-SURF 노트 반영 기록 13"
canonical_source: self
citation_status: verified
verification_method: "배정표·최종 근거·노트 수정안·표 형식·상대 링크·Mermaid 원문 일치 대조. 2026-11-04 CADMAS-SURF recovery 대조 보고서 반영"
last_source_check: "2026-11-04 (recovery 대조 반영)"
note_author: "Codex"
note_date: 2026-11-04
---

# CADMAS-SURF 노트 반영 기록 13

배정표는 [CADMAS-SURF-note-job-13.tsv](../assign/CADMAS-SURF-note-job-13.tsv)이다.
대상은 VOF 노트 60행과 구조·소스맵 노트 59행이다.
파일별 완료 결과는 아래에 덧붙인다.

## VOF 자유수면 노트

대상은 [cadmas-surf3d-vof-free-surface.md](../../../models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md)이다.
추가·수정 범위는 `models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md:6–7,30,38,46–47,68–69,78–81,85–87,96–163`이다.
표에 넣은 행 수는 배정표의 이 파일 대상 60행과 같은 60행이다.
본문에 반영한 수정안 행 ID는 `3d-theory:KS1-710`, `3d-theory:KS1-711`, `3d-input:KS3-402`, `3d-program:KS2-813`, `3d2f-vs-3d:KD1-905`이다.
`2f-theory:KF1-111·208` 수정안의 ISCMFF 선택·평면 재구성 설명은 유지했다.
KD1-905의 결론은 최종 근거 `CADMAS-SURF-conclusion-verify-KD1f.md`를 따랐다.
배정표에 없는 수정안 행은 본문에만 반영했다.
넣지 않은 배정 행은 없다.

## 구조·소스맵 노트

대상은 [cadmas-surf3d-architecture-source-map.md](../../../models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md)이다.
이번 추가 범위는 `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:107,157–394`이다.
표의 범위는 `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:165–223`이다.
표에 넣은 행 수는 배정표의 이 파일 대상 59행과 같은 59행이다.
그림의 범위는 `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:226–394`이다.
[호출 흐름 보고서 §4](CADMAS-SURF-callflow.md#4-계산-흐름도)의 Mermaid 3개를 그대로 옮겼다.
각 그림 위에 mmdc 렌더 확인 문장을 넣었다.
렌더 확인 문장의 근거는 원 보고서의 [Claude 렌더 확인 (11-04)](CADMAS-SURF-callflow.md#claude-렌더-확인-11-04)이다.
세 Mermaid 블록은 원 보고서와 글자 단위로 일치한다.

수정안 반영 상태를 확인한 범위는 `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:24,34–46,58–87,99–111,131–141`이다.
이미 반영된 수정안은 유지했다.
배열 크기 문장은 107줄에 보충했다.
반영한 수정안 행 ID는 `2f-program:KF2-047·251–328`, `2f-program:KF2-308·313·363`, `3d-program:KS2-800–805`, `3d-input:KS3-409`, `3d-theory:KS1-721`, `callflow:RF-006`, `tutorials-build:KU1-816·222`이다.
호출 흐름 보고서의 일치 행에서 유지하라고 한 중첩 격자 교환·VOF 뒤 경계 재설정 설명은 유지했다.
last_source_check와 verification_method에는 요청한 반영 날짜와 문구가 이미 있다.
기존 citation_status는 유지했다.
넣지 않은 배정 행은 없다.

## 최종 확인

배정표의 119행을 각 배정 파일에서 한 번씩 확인했다.
VOF 노트의 표는 60행이다.
구조·소스맵 노트의 표는 59행이다.
두 노트의 표에는 배정표 밖의 행이 없다.
두 노트의 표는 모두 6열이다.
행별 최종 분류는 배정표·최종 결론 TSV·근거 파일과 일치한다.
과거 노트 인용에는 반영 전 커밋 `05fdbedb`를 붙였다.
세 파일의 상대 링크 대상은 모두 존재한다.
세 파일에는 금지된 절대 경로와 위키 링크 구분자가 없다.
넣지 않은 행과 이유는 없다.
