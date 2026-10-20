---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_gauge_point_data.cuh
lines: 47
sha256: 5f9502f5efc96b535d8be151c9bc770851dfba4917d62cef150a8b0b9f2ad93d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_gauge_point_data.cuh — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 첫 빈 줄(1) 뒤 `#pragma once` (2). stdio·stdlib·AssembledSolution·compact·cuda_utils·GaugePoints를 포함한다(4–10). lis::cuda::acc_nugrid 이름공간(namespace)을 연다(13–18). 사이의 빈 줄을 포함한다. 전처리 조건 분기는 없다. |
| 21–32 | write_gauge_point_data 함수 선언이다(21–31). 결과 경로·관측점 파일명은 const char*, 조립 해(assembled solution)는 수정 가능한 참조, GaugePoints·int mesh_dim·Pars·Solver·States는 const 참조로 받는다(23–30). 기본 인수와 실행 본문은 없다. 빈 줄(32). |
| 33–47 | write_velocity_point_data는 앞 함수와 동일한 형식·이름의 인수를 받는 void 함수 선언이다(33–43). 기본 인수와 본문은 없다. 빈 줄과 이름공간 닫기(44–47). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
