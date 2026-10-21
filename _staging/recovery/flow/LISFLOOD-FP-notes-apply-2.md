---
title: "LISFLOOD-FP 사용자 매뉴얼 노트 대조 반영 기록 — 배정 2"
citation_status: verified
last_source_check: "2026-10-21 (recovery 대조 반영)"
verification_method: "2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영"
---

# LISFLOOD-FP 사용자 매뉴얼 노트 대조 반영 기록

배정 근거는 [LISFLOOD-FP-note-job-2.tsv](../assign/LISFLOOD-FP-note-job-2.tsv)다.
최종 분류와 근거 파일은 [LISFLOOD-FP-final-conclusions.tsv](../assign/LISFLOOD-FP-final-conclusions.tsv)를 따른다.
대상 노트는 [lisflood-fp-user-manual.md](../../../models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md)다.

작업 상태: 완료.

배정표의 137행을 대상 노트에 추가했다.
추가한 행 ID와 최종 분류는 배정표의 137행과 같다.
넣지 않은 배정 행은 없다.
중복된 배정 행은 없다.

## 파일별 반영 결과

아래 줄 범위는 반영한 절을 기준으로 묶었다.

| 파일:줄 범위 | 반영 내용 |
|---|---|
| `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:7–15` | last_source_check를 추가했다. verification_method에 recovery 대조 반영 문구를 덧붙였다. citation_status는 verified를 유지했다. related 경로를 상대 경로로 바꿨다. |
| `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:21–33` | 매뉴얼 세 판을 구분했다. PDF의 머리글·정보 표·요약 판 번호를 정정했다. 체적유량과 단위폭 유량을 구분했다. |
| `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:45–69` | Routing 조건을 구분했다. CFL 설명을 정정했다. Roe의 외곽 경계와 내부 벽을 구분했다. 인쇄 연속식과 정정식을 구분했다. |
| `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:83–205` | 매개변수의 대소문자·순서를 정정했다. 문서 기본값과 코드 기본값을 구분했다. 강우·건조 검사·통계·출력의 해법별 조건을 반영했다. |
| `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:211–298` | 주석·경계 좌표·시계열·지역 파일·초기 파일 설명을 정정했다. 입력 결함 후보의 조건과 강도를 적었다. 구조물의 입력값·방향·적용 조건을 구분했다. |
| `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:320–341` | 명령 줄 인수와 순서를 정정했다. 조도 덮어쓰기의 범위를 구분했다. 정상상태 종료의 연속 횟수를 적었다. |
| `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:345–398` | 체크포인트의 검사·저장 배열·호출 경로를 구분했다. 질량수지·profile·최대값·침수 시간·유속 출력을 정정했다. 보·교량 식과 계수 설명을 정정했다. |
| `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:404–445` | NUMA 변수와 CUDA 아키텍처 설정을 정정했다. 수치 모드 설명을 추가했다. Makefile 이름을 정정했다. 기존 위키 링크를 상대 Markdown 링크로 바꿨다. |
| `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:450–468` | 대조 절에 문서 판과 코드 판을 적었다. 배정표·보고서·최종 근거의 상대 링크를 추가했다. |
| `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:469–605` | 배정 행 137개를 지정한 6열 표에 추가했다. |

## 배정 행 수

보고서별 행 수는 배정표와 대상 노트의 행 ID에서 각각 집계했다.

| 보고서 약칭 | 배정 행 수 | 넣은 행 수 |
|---|---:|---:|
| bridge-docx | 15 | 15 |
| build-83 | 3 | 3 |
| callflow | 2 | 2 |
| cpu-gpu-swe | 2 | 2 |
| docx-manual | 37 | 37 |
| files-output | 39 | 39 |
| par | 27 | 27 |
| theory | 12 | 12 |
| 합계 | 137 | 137 |

## 반영한 노트 수정안

수정안 행 수는 각 보고서에서 이 노트 경로를 포함한 수정안 표 행을 세어 69행으로 집계했다.

| 보고서 | 반영한 수정안 행 ID |
|---|---|
| [theory](../compare/lisflood-theory-vs-code.md) | `LT1-401`, `LT1-402`, `LT1-403`, `LT1-404`, `LT1-405`, `LT1-406`, `LT1-407`, `LT1-422` |
| [par](../compare/lisflood-par-vs-code.md) | `LI1-341`, `LI1-342`, `LI1-343`, `LI1-344`, `LI1-345`, `LI1-346`, `LI1-347`, `LI1-348`, `LI1-349`, `LI1-350`, `LI1-351`, `LI1-352`, `LI1-353`, `LI1-354`, `LI1-355`, `LI1-372` |
| [files-output](../compare/lisflood-files-output-vs-code.md) | `LI2-102–103`, `LI2-039–040, 301–303`, `LI2-027–028`, `LI2-059–066, 311–313`, `LI2-069–079, 346`, `LI2-100–101, 343–345`, `LI2-119, 121, 135–139`, `LI2-123–124`, `LI2-127, 145–155, 348–349`, `LI2-157, 159–167`, `LI2-172–179`, `LI2-186–191`, `LI2-192–198, 331–334, 350`, `LI2-200–205` |
| [docx-manual](../compare/lisflood-docx-manual-vs-code.md) | `LV1-001–002`, `LV1-010–011`, `LV1-029·279`, `LV1-032·184·252`, `LV1-034`, `LV1-059–060`, `LV1-076·173`, `LV1-084–085·097`, `LV1-177·180`, `LV1-191–194·266`, `LV1-195–199·204–207`, `LV1-210–211`, `LV1-220–229` |
| [bridge-docx](../compare/lisflood-bridge-docx-vs-code.md) | `LB1-383`, `LB1-384`, `LB1-385`, `LB1-386`, `LB1-387`, `LB1-388`, `LB1-389`, `LB1-390`, `LB1-391`, `LB1-392`, `LB1-393`, `LB1-394` |
| [build-83](../compare/lisflood-build-83-vs-code.md) | `LN1-233`, `LN1-234`, `LN1-235`, `LN1-236` |
| [cpu-gpu-swe](../compare/lisflood-cpu-gpu-swe.md) | `LG1-123, 140` |
| [callflow](../flow/LISFLOOD-FP-callflow.md) | `RF-021` |

build-83의 LN1-236에서 유지하라고 한 기본 구성 문장은 대상 노트 425행에 그대로 남겼다.
LN1-236의 수치 모드 추가 설명은 대상 노트 427행에 넣었다.
callflow의 RF-021은 대상 노트의 체크포인트 본문에 반영했다.
H와 일치 분류의 표 행은 대조 표에 추가하지 않았다.

## 확인 결과

대조 표 137행의 결론 문장은 지정한 최종 근거의 결론 문장과 대응한다.
대조 표 137행은 지정한 최종 근거의 확인한 원문 인용을 포함한다.
Markdown 파서는 대조 표를 자료 137행과 각 행 6열로 인식했다.
A 분류 행에는 근거 판이 있다.
E 분류 행에는 최종 근거가 정한 강도가 있다.
자기 노트 인용은 반영 전 커밋 bf804e23의 경로와 줄 번호를 사용한다.
대상 노트의 상대 링크 목적지는 모두 존재한다.
대상 노트와 이 기록은 금지된 경로 및 링크 문자열을 포함하지 않는다.
`git diff --check`는 대상 노트에서 오류를 출력하지 않았다.
