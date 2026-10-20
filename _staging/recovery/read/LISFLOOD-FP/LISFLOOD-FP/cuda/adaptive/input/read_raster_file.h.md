---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_raster_file.h
lines: 16
sha256: f648ca10db5a5cb1f7763873674c4ead5192c425e3c9c4bb823be9fb1a029b8e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_raster_file.h — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 단일 포함 지시, C 표준 라이브러리 헤더와 수치 형식 real 헤더를 포함한다(1–8). 조건부 전처리 분기는 없다. 원문: `#pragma once` (1). |
| 10–16 | read_raster_file의 void 원형을 선언한다. 파일명·출력 배열·mesh_dim 정수 상수 참조·wall_height 실수 상수 참조를 받는다(10–16). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
