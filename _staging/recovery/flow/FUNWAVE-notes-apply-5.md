---
title: "FUNWAVE 노트 대조 반영 기록 — 작업 5"
citation_status: verified
last_source_check: "2026-10-18 (recovery 대조 반영)"
verification_method: "2026-10-18 FUNWAVE recovery 대조 보고서 반영"
---

# FUNWAVE 노트 대조 반영 기록 — 작업 5

배정 근거는 [FUNWAVE-note-job-5.tsv](../assign/FUNWAVE-note-job-5.tsv)다.
대상 노트는 [funwave-dispersion-solver.md](../../../models/FUNWAVE/source-analysis/funwave-dispersion-solver.md)다.
배정표의 반영 대상은 164행이다.
현재 상태는 반영 완료다.

| 파일:줄 | 추가·수정 내용 |
|---|---|
| `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:5–6` | verification_method에 대조 반영 구절을 추가했다. last_source_check를 지정값으로 설정했다. |
| `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:14` | GPU 대체 대상의 도입부를 수정했다. |
| `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:19–28` | U4·V4 비선형 보정과 ZALPHA 재대입을 반영했다. U1p·V1p와 비선형 나머지의 분리를 반영했다. Beta_2 배수를 반영했다. |
| `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:41–45` | 수심 하한과 x 삼중대각 계수·우변을 수정했다. |
| `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:48–52` | HU·HV 대입과 전체 수평 속력의 Froude 상한을 반영했다. |
| `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:62–64` | GPU의 기본 Thomas 풀이와 별도 cuSPARSE 경로를 구분했다. MGPU 계수 전달을 반영했다. |
| `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:77–85` | P·Q 선행 소비와 nu_break 지연을 보강했다. 마스크·쇄파·중첩·스펀지·출력 시점을 보고서의 상위 흐름도에 연결했다. |
| `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:90–264` | 문서·코드 판과 출처를 적었다. 배정 행의 차이 표를 추가했다. |

| 보고서 약칭 | 노트의 표 행 범위 | 배정표 행 수 | 넣은 행 수 |
|---|---|---:|---:|
| theory-numerics | `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:101–154` | 54 | 54 |
| inputs | `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:155–156` | 2 | 2 |
| v21-manual | `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:157–191` | 35 | 35 |
| aux-docs-build | `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:192–216` | 25 | 25 |
| gpu-vs-tvd | `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:217–261` | 45 | 45 |
| callflow | `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md:262–264` | 3 | 3 |
| 합계 | 배정표의 고유 행 ID 기준 | 164 | 164 |

반영한 수정안 행 ID는 다음과 같다.

- theory-numerics:FT1-279.
- v21-manual:FV1-552, FV1-553, FV1-554, FV1-555.
- aux-docs-build:FN1-921.
- gpu-vs-tvd:FG1-802 참조 수정안.

callflow §6의 담당 노트 수정안 두 행에는 행 ID가 없다.
[callflow:2973](FUNWAVE-callflow.md#6-기존-노트-대조와-수정안)의 대조 전 노트 16·25행 수정안은 현재 노트 77–83행에 반영했다.
[callflow:2974](FUNWAVE-callflow.md#6-기존-노트-대조와-수정안)의 대조 전 노트 54행 수정안은 현재 노트 85행에 반영했다.
기존 호출 문장과 호출 흐름은 두 수정안의 일치 판정에 따라 유지했다.

넣지 않은 배정 행은 없다.
미반영 담당 노트 수정안은 없다.
배정표와 노트 표의 행 ID·분류를 대조했다.
누락 행과 중복 행은 없다.
Markdown 파서는 차이 표의 본문을 164행·6열로 읽었다.
A 행 4개에는 커밋 HASH와 날짜를 넣었다.
E 행 56개에는 보고서의 강도를 넣었다.
보고서의 Beta_2 같은 원인 문장 37개를 그대로 보존했다.
보고서의 최종 결론 문장 164개를 대조했다.
상대 링크의 대상 파일과 금지 문자열을 검사했다.
문서·코드 원문 칸의 백틱 인용에서 문자열 불일치는 없다.
git diff의 공백 검사는 통과했다.
