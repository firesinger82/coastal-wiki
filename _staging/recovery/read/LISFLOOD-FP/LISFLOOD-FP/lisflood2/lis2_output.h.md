---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/lisflood2/lis2_output.h
lines: 35
sha256: d44ed17cec434e405ecc0f5019a28b7668ad6ecb6756e4d5ccc1366cbda70013
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# lis2_output.h — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1), lisflood.h·lisflood2.h·DataTypes.h 포함(3–5), 빈 줄. 이 파일에는 조건부 전처리가 없다. NUMERIC_TYPE은 lisflood.h:75–97의 정밀도 선택을 따른다. 같은 소스 루트 config.default.cmake:2의 `_NUMERIC_MODE=1`은 double을 선택한다. |
| 7–26 | 전처리 조건 밖. write_regular_output 원형은 결과 경로·격자 크기/패딩(padding)·수심 임계값·현재 시각·작업 격자 셋·수심/지형/유량/이전 유량/유속/만제 수심(bankfull depth)/최대 수심 배열·하위 격자 수로(subgrid channel) 배치/상태·셀 간격·해법/상태/매개변수/경계/수로 매개변수·출력 매개변수와 번호·출력 스위치를 받는다(7–25). 함수 본문이나 기본 인수는 없다. |
| 27–35 | 전처리 조건 밖. WriteOutput 원형은 파일명 구조체·격자 크기/패딩·수심 임계값·작업 격자·초기/누적 침수 시간·최대 수심/발생 시각·최대 유속/대응 수심/위험도(hazard)·방향별 최대 유속·지형·만제 수심·상태/매개변수/출력 매개변수를 받는다(27–35). 선언이 마지막 행에서 끝난다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
