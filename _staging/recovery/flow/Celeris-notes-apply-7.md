---
title: "Celeris 노트 반영 결과 — 작업 7"
citation_status: verified
last_source_check: "2026-11-04 (recovery 대조 반영)"
verification_method: "2026-11-04 Celeris recovery 대조 보고서 반영"
---

# Celeris 노트 반영 결과 — 작업 7

배정표: [Celeris-note-job-7.tsv](../assign/Celeris-note-job-7.tsv).

대상: [celeris-breaking-boundary.md](../../../models/Celeris/source-analysis/celeris-breaking-boundary.md).

배정표의 108개 행을 모두 반영했다.

## 파일별 반영 결과

대상 파일은 `models/Celeris/source-analysis/celeris-breaking-boundary.md`이다.

- `models/Celeris/source-analysis/celeris-breaking-boundary.md:5–6`: verification_method에 대조 반영 문구를 덧붙였다. last_source_check를 지정값으로 추가했다. 기존 citation_status를 유지했다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:15`: 쇄파 호출을 Pass2 뒤·Pass3 앞으로 정정했다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:23`: 명시적 쇄파 옵션의 추가 커밋과 Tavakkol 2017의 판 구분을 덧붙였다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:27`: 도함수 생산자를 수문 Pass3로 정정했다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:69–71`: delta_breaking을 무차원 계수로 정정했다. 본판과 transect 판의 점성 상한 차이를 덧붙였다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:82`: 거품 표시와 점성 운동량 소산을 구분했다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:124–126`: Tavakkol 2020 식 (9)와의 판 차이를 덧붙였다. 동·북 스펀지 거리식의 중간 강도 결함 후보를 덧붙였다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:148`: transient 파 수를 5로 정정했다. 종료 함수를 선형 함수로 정정했다. bb99fee의 판 변경을 적었다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:155`: 고립파 높이 입력 연결의 중간 강도 결함 후보를 덧붙였다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:210`: 조파 설명의 transient 파 수와 종료 함수를 정정했다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:222`: 지형 .w 표지의 소비자를 정정했다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:228–345`: 「문서와 코드 차이 (11-04 대조)」 절을 추가했다. 비교한 판과 인용 기준을 적었다.
- `models/Celeris/source-analysis/celeris-breaking-boundary.md:238–345`: 배정표의 108개 행을 6열 표로 넣었다.

## 반영한 수정안 행 ID

| 보고서 | 수정안 행 ID | 반영 위치·처리 |
|---|---|---|
| callflow | RF-020 | 15·27행. 호출 순서와 도함수 생산자를 정정했다. 최종 결론의 두 경계 상태 입력은 RF-020 표 행에 함께 옮겼다. |
| docs-architecture | CD1-1342·1400 | 148·210행. 파 수와 종료 함수를 최종 근거에 맞췄다. |
| docs-architecture | CD1-1343 | 151–152행의 고정 진폭 설명을 유지했다. 155행에 CD1-1303의 입력 연결 문제를 덧붙였다. |
| docs-architecture | CD1-1344 | 205행의 단일 sine 생성·주기 경계 방향 보정 설명을 그대로 유지했다. |
| docs-source | CD2-468 | 40행의 기본계수와 57–67행의 강도·점성 설명을 유지했다. |
| lynett2026 | CP3-113 | 69행. 점성 계수의 차원을 정정했다. |
| lynett2026 | CP3-014–020·089 | 40행의 기본계수와 78행의 채널 순서를 유지했다. 82행에 B를 사용하는 거품 표시를 덧붙였다. CP3-017의 최종 B 분류와 2차 문헌 근거는 배정 표 행에 옮겼다. |
| tavakkol2017 | CP1-146 | 21행의 현재 쇄파 모델 설명을 유지했다. 23행에 판 구분을 덧붙였다. |
| tavakkol2017 | CP1-147·166 | 148·210행. 최종 근거의 결론 문장을 적용했다. CP1-147의 최종 B 분류를 표에 적용했다. |
| tavakkol2017 | CP1-148 | 222행. 지형 .w 표지의 소비자를 정정했다. |
| tavakkol2020 | CP2-170 | 124–126행. 판 차이와 거리식 결함 후보를 덧붙였다. 최종 A 분류를 표에 적용했다. |
| transect | CT1-361 | 71행. 본판·transect 판의 점성 상한과 전달 방향 차이를 덧붙였다. 배정표 밖의 행이므로 차이 표에는 넣지 않았다. |

callflow의 「Claude 렌더 확인 (11-04)」에는 이 노트를 직접 가리키는 추가 수정안이 없다.

## 행 수와 확인 결과

배정표에서 센 행 수는 108개이다.
노트의 차이 표에서 센 행 수는 108개이다.
배정표와 노트 표의 행 ID·보고서 약칭·최종 분류는 모두 일치한다.

| 최종 분류 | 노트 표에서 센 행 수 |
|---|---:|
| A 판 차이 | 17 |
| B 문서 오기 | 9 |
| C 문서 누락 | 78 |
| E 코드 결함 후보 | 2 |
| F 표기 차이 | 2 |
| 합계 | 108 |

108개 결론 문장은 인용·식의 표시 형식과 A 행의 문서 판 표기를 제외하고 최종 근거 파일과 일치한다.
108개 「확인한 원문」 칸은 인용 표시 형식을 제외하고 최종 근거 파일과 일치한다.
노트의 모든 차이 표 행은 6열이다.
A 행에는 커밋 또는 문서 판이 있다.
E 행에는 중간 강도가 있다.
기존 기본계수·출력 채널·단일 sine·고립파 고정 진폭의 유지 대상 줄은 그대로 남아 있다.
상대 링크의 대상 파일은 모두 존재한다.
금지 경로·문자열과 한계 문장은 없다.

넣지 않은 배정 행은 없다.
미반영한 담당 노트 수정안 행은 없다.
