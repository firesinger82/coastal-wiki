---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/compaction.cuh
lines: 29
sha256: 6823dcaceadf3983777fd85d077d94b08eda911767682d850cbf9476b80e5281
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# compaction.cuh — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1)로 중복 포함을 제한한다. CUB 장치 선택(device selection), 오류 확인, CUDA 메모리 도구, `AssembledSolution`, `CompactionFlags` 헤더를 포함한다(3–8). 전처리 조건 분기는 없다. |
| 10–29 | `lis::cuda::acc_nugrid` 이름 공간(namespace)을 연다(10–15). `void compaction` 선언은 해와 버퍼의 참조, 압축 플래그 참조, 최세밀 요소 수, `non_uniform_n`, `startfile`을 받는다(17–25). 인수 기본값은 없다. 이름 공간 세 개를 닫는다(27–29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
