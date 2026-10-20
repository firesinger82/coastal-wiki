---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/ghostraster.cpp
lines: 47
sha256: ab4ce830c72ae9bad2d6536a216ab61dd92010970ea9b48adbef481454fbab81
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# ghostraster.cpp — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 헤더 포함(1–2). 고스트 래스터(ghost raster)의 전체 요소 수는 `return (geometry.xsz+2)*(geometry.ysz+2);` (6), 수심 요소 수는 `return (geometry.xsz)*(geometry.ysz);` (11), 유량 요소 수는 `return (geometry.xsz + 1)*(geometry.ysz + 1);` (16). 각각 elements·elements_H·elements_Q가 반환한다(4–17). 조건부 전처리 지시는 없다. |
| 19–38 | pitch는 `return geometry.xsz + 2;` (21), offset은 `return geometry.xsz + 3;` (26). ACC 전용 pitch_ACC는 `return geometry.xsz;` (31), offset_ACC는 `return 0;` (36). |
| 39–47 | allocate는 `return new NUMERIC_TYPE[elements(geometry)]();` (41), allocate_H는 `return new NUMERIC_TYPE[elements_H(geometry)]();` (46)로 값 초기화한 배열을 반환한다. 마지막 행 번호는 47이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
