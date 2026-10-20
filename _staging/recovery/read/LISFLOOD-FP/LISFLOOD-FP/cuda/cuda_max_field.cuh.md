---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_max_field.cuh
lines: 45
sha256: 23bb926b410da19467be0768e534858770103a1d69717345f2de63e9032331be
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_max_field.cuh — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1), lisflood·geometry 헤더(2–3), lis::cuda 이름 공간(namespace)(5–8), MaxField 클래스(class)(10–11). 별도 전처리 조건 분기는 없다. |
| 12–30 | 공개 생성자 원형(13–23)은 resrootname·Geometry 참조·pitch·offset·dim3 grid_size·acceleration을 받는다. 기본 인수는 `int precision = DEFAULT_PRECISION` (21). update(NUMERIC_TYPE* H)·updateACC(NUMERIC_TYPE* H)·write 원형(25–27), 소멸자(destructor) 원형(29), 빈 줄(30). |
| 31–45 | 시작 시 10행 클래스 안. private 멤버는 resrootname·Geometry 참조·pitch·offset·grid_size·precision(32–37), NUMERIC_TYPE 포인터 maxH·totalHtm·maxHtm·initHtm(38–41). 클래스·이름 공간 종료(42–45). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–41: maxH 외에 totalHtm·maxHtm·initHtm 포인터를 선언한다. 이 헤더의 선언부에는 각 포인터의 기본값이 없다.
