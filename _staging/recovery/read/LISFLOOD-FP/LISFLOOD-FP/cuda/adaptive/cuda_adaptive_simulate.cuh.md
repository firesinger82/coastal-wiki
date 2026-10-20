---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/cuda_adaptive_simulate.cuh
lines: 26
sha256: 27d16f309e1890ca790633a428d0dba7da5b41a56a2f032b3c6a5f99fbbd8d3f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_adaptive_simulate.cuh — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1) 뒤 lisflood.h·geometry.h·cuda_simulate.cuh를 포함한다(2–4). 전처리 조건 분기는 없다. lis·cuda·adaptive 이름공간(namespace)을 연다(6–11). |
| 13–26 | 시작 시 6·8·10행 lis::cuda::adaptive 이름공간 안. Simulation 클래스는 cuda::Simulation을 공개 상속(public inheritance)한다(13–14). 공개 run 메서드가 int argc와 char** argv를 받는다고 선언한다(15–20). 클래스·세 이름공간을 닫고 마지막 빈 줄을 포함한다(21–26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
