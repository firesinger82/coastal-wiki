---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/metal/metal_integrate.h
lines: 11
sha256: 185aa5686bedb8f3eab9d913f16355b2d9f877917ff2edbe27ede506819dde73
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# metal_integrate.h — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Metal 그래픽 처리 장치(graphics processing unit, GPU) 진입점(entry point) 주석(1), `#pragma once` (2), ../lisflood.h 포함(3), 빈 줄(4·7). 가용한 Metal GPU가 있으면 true라는 주석과 `bool metal_is_available();` 선언(5–6). 이 파일에는 조건부 컴파일 전처리문이 없다. |
| 8–11 | Metal GPU에서 FV1 해법(solver)을 실행한다는 주석(8). `run_metal_fv1`은 Fnames·Files 포인터·States·Pars·Solver·BoundCs·Stage·Arrays·verbose를 인수로 선언한다(9–11). 반환형은 void이고 선언에는 기본 인수 값이 없다. 조건부 컴파일 전처리문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
