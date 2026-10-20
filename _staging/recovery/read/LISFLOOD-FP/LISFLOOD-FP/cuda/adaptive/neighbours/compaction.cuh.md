---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/neighbours/compaction.cuh
lines: 22
sha256: b3839e7f84b9426defea2a8c704bb95d3dfcef5bc3c1c80d6d8c68366731c20e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# compaction.cuh — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1) 뒤 CUB 장치 선택·CUDA 유틸리티·AssembledSolution·Neighbours·CompactionFlags·SolverParams 헤더를 포함한다(3–10). 조건부 전처리 분기는 없다. |
| 12–22 | `__host__` (12) 지정의 compaction 호스트(host) 함수를 선언한다(13–22). 조립 해(assembled solution) 버퍼와 출력, 이웃 버퍼와 출력, 압축 플래그(compaction flag)를 참조로 받고 num_finest_elems를 값으로, SolverParams를 const 참조로 받는다(15–21). 기본 인수는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
