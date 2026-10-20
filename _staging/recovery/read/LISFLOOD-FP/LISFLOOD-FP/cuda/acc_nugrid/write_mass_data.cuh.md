---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_mass_data.cuh
lines: 40
sha256: 1e6c972e700201df21e64cfe5e84ebc62f072760c47c2d49c038e999a9e36e3d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_mass_data.cuh — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 첫 빈 줄 뒤 `#pragma once` (2). stdio·stdlib·AssembledSolution·compact·cuda_utils·GaugePoints를 포함한다(4–9). lis::cuda::acc_nugrid 이름공간(namespace)을 연다(11–16). 전처리 조건 분기는 없다. |
| 18–40 | write_mass_data의 void 함수 원형이다(18–36). 결과 경로, GaugePoints·mesh_dim·Solver·States const 참조, NUMERIC_TYPE const 참조 FArea·vol2·Qin·Hds·Qout·Qerror·Verror·RainTotalLoss·InfilTotalLoss·EvapTotalLoss를 받는다(20–35). AssembledSolution 인수는 주석이다(21). 기본 인수와 본문은 없다. 빈 줄과 이름공간 닫기(37–40). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
