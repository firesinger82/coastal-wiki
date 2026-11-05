---
title: "CADMAS-SURF 노트 반영 기록 12"
canonical_source: self
citation_status: verified
verification_method: "2026-11-04 CADMAS-SURF recovery 대조 보고서 반영. 배정 ID·최종 분류·결론 문장·수정안·Markdown 표·상대 링크 대조."
last_source_check: "2026-11-04 (recovery 대조 반영)"
note_author: "Codex"
note_date: 2026-11-04
---

# CADMAS-SURF 노트 반영 기록 12

배정표: [CADMAS-SURF-note-job-12.tsv](../assign/CADMAS-SURF-note-job-12.tsv)

배정표의 두 노트에 최종 결론과 노트 수정안을 반영한다.
파일별 완료 결과는 아래에 기록한다.

## SMAC 노트

- 파일: [cadmas-surf3d-smac-velocity-pressure-solver.md](../../../models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md).
- 추가·수정 줄: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md:6–8`(frontmatter), `:44`(이류 혼합), `:69`(압력 갱신), `:75–165`(대조 절).
- 표 행 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md:87–165`.
- 넣은 행 수: 79행. 배정표에서 이 파일에 지정한 79행과 같다.
- 반영한 수정안 행 ID: `3d-theory:KS1-708`, `3d-theory:KS1-709`, `callflow:RF-007`, `callflow:RF-008`.
- `callflow`의 SMAC 포텐셜 설명 유지 행은 본문을 유지했다.
- 넣지 않은 배정 행: 없음.
- 확인: 배정 ID 집합이 표 ID 집합과 같다. Markdown 표는 본문 79행과 474셀로 파싱된다. 백틱 안쪽 앞뒤의 추가 공백은 없다.

## STR3D 노트

- 파일: [str3d-fem-core-newmark-elasto-plastic.md](../../../models/CADMAS-SURF/source-analysis/str3d-fem-core-newmark-elasto-plastic.md).
- 추가·수정 줄: `models/CADMAS-SURF/source-analysis/str3d-fem-core-newmark-elasto-plastic.md:6–8`(frontmatter), `:23–27`(주 프로그램·분기·누락 소스), `:35–41`(감쇠·세 변위 수준·침투 압력), `:45`(요소 분기), `:49`(질량행렬), `:63`(재료표), `:68`(전역 배열 크기), `:75–156`(대조 절).
- 표 행 범위: `models/CADMAS-SURF/source-analysis/str3d-fem-core-newmark-elasto-plastic.md:87–156`.
- 넣은 행 수: 70행. 배정표에서 이 파일에 지정한 70행과 같다.
- 반영한 수정안 행 ID: `str-theory:KT1-837`, `str-theory:KT1-838`, `str-theory:KT1-839`, `str-theory:KT1-840`, `str-theory:KT1-841`, `str-theory:KT1-842`, `str-theory:KT1-843`, `str-datatable:KT2-581`, `str-datatable:KT2-583`, `str-datatable:KT2-584`, `str-datatable:KT2-585`, `str-datatable:KT2-586`, `tutorials-build:KU1-765·916`, `callflow:RF-012`.
- `str-datatable:KT2-582`와 `callflow`의 세 변위 수준 유지 행은 기존 문장을 유지했다. 문서 크기 표와 병렬 추가 공간의 쪽 인용을 별도 문장에 연결했다.
- 넣지 않은 배정 행: 없음.
- 확인: 배정 ID 집합이 표 ID 집합과 같다. Markdown 표는 본문 70행과 420셀로 파싱된다. 백틱 안쪽 앞뒤의 추가 공백은 없다.

## 전체 확인

- 배정표의 149행을 두 노트에 반영했다. 행 수는 배정표의 파일별 지정 수 79행과 70행을 합한 값이다.
- 배정표 밖의 행을 표에 추가하지 않았다.
- 최종 분류는 배정표와 최종 결론표의 같은 행 ID에 대응한다.
- 최종 결론 문장 149행은 근거 파일의 같은 행과 일치한다. 이 대조는 백틱 표시와 코드 경로 약칭의 정규화를 제외한 본문 글자를 비교했다.
- A행에는 판 근거를 넣었다.
- E행에는 강함을 넣었다. 담당 E행의 최종 근거는 모두 활성 호출과 필수 빌드 항목을 적고 있다.
- H행과 일치 행을 표에 넣지 않았다.
- 두 노트의 상대 링크는 모두 연결 대상을 가리킨다.
- 검색식의 대괄호는 HTML 문자 참조로 기록했다. 원문 표시를 유지하면서 금지된 연속 대괄호 문자열을 없앴다.
- 넣지 않은 행과 이유: 없음.
