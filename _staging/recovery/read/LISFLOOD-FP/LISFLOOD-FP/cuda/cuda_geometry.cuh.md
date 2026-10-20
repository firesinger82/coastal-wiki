---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_geometry.cuh
lines: 66
sha256: 7565619f4d5a96bed349e658e8da1e607acdb13688c7c300dc08c3f3d0273df8
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_geometry.cuh — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1), lisflood·geometry 헤더(2–3), lis::cuda 이름 공간(namespace)(5–8), GhostRaster 구조체(10–11). 별도 전처리 조건 분기는 없다. |
| 12–28 | 시작 시 10행 GhostRaster 구조체 안. Geometry 참조를 받아 NUMERIC_TYPE 포인터를 반환하는 static allocate_pinned(12–15)·allocate_device(17–20). copy는 NUMERIC_TYPE* dst·src와 Geometry 참조를 받는다(22–27). |
| 29–45 | 시작 시 10행 구조체 안. static allocate_pinned_H(29–32)·allocate_device_H(34–37)는 Geometry 참조에서 NUMERIC_TYPE 포인터를 반환한다. copy_H는 dst·src 포인터와 Geometry 참조를 받는다(39–44). |
| 46–66 | 시작 시 10행 구조체 안. static allocate_pinned_Q(46–49)·allocate_device_Q(51–54)는 Geometry 참조에서 NUMERIC_TYPE 포인터를 반환한다. copy_Q는 dst·src 포인터와 Geometry 참조를 받는다(56–61). 구조체·이름 공간 종료(63–66). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
