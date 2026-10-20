---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/read_raster_file.h
lines: 25
sha256: dd0c372f523d75595c88c7f337884c19cf170e83516464d59de33daeb0303aac
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_raster_file.h — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 중복 포함 방지는 `#pragma once` (1). stdlib·stdio·string 및 lisflood.h를 포함한다(3–6). lis::cuda::acc_nugrid 이름공간(namespace)을 연다(8–13). 이 파일에는 전처리 조건 분기가 없다. |
| 15–25 | read_raster_file 함수 원형은 파일명, NUMERIC_TYPE 배열 포인터, const int& 확장 격자 차원, const NUMERIC_TYPE& 결측값을 받는다(15–21). 기본 인수와 실행 본문은 없다. 빈 줄과 세 이름공간의 닫는 괄호를 포함한다(22–25). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
