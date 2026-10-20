---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/GaugePoints.h
lines: 32
sha256: b6763c2f5cdd96df38ae8a47638200d6c3b603b85dc9548871eb2f34bbb5365a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# GaugePoints.h — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `#pragma once` (1), MortonCode.h 포함(3), `lis::cuda::acc_nugrid` 이름공간(namespace)(5–10). 관측점(gauge point) 구조체(struct) GaugePoints(12–13)는 MortonCode* codes·int num_points(14–15), `bool        is_copy = false;` (16)를 보유한다. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 18–32 | 시작 시 12행 GaugePoints 구조체 안. 생성자(constructor)는 num_points를 받고(18–19), `this->codes = (num_points > 0) ? new MortonCode[num_points] : nullptr;` (20), this->num_points에 인수 복사(21). 복사 생성자(copy constructor)는 `GaugePoints(const GaugePoints& original) { *this = original; is_copy = true; }` (24). 소멸자(destructor)는 `~GaugePoints() { if (!is_copy && codes != nullptr) delete[] codes; }` (26). 구조체·이름공간 종료와 빈 줄(27–32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–22: 생성자는 codes 배열을 할당하지만 Morton 코드(Morton code) 원소를 채우는 문장을 포함하지 않는다.
