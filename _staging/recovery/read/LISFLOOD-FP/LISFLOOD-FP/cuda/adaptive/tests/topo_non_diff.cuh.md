---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/topo_non_diff.cuh
lines: 33
sha256: efaf47b53f8cbc399142f67a28bdee0451e5e45a8d33459e0696884c795bd625
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# topo_non_diff.cuh — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_runtime.h` (3)와 `real.h` (5)를 포함한다. 원문 출처 주석은 `// from https://www.sciencedirect.com/science/article/pii/S004578251830389X` (7)다. CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (8)가 붙은 `topo_non_diff`를 정의하며 x·y 좌표를 상수 참조로 받는다(9–14). 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 15–33 | 시작 시 9–14행 `topo_non_diff` 본문 안. 초기값은 `real z_int = 0;` (15)다. 공통 y 범위 식은 `bool y_bound = ( C(11.0) <= y_int && y_int <= C(19.0) );` (17)다. `if (C(16.0) <= x_int && x_int <= C(24.0) && y_bound)` (19)이면 `z_int = C(0.86);` (21), `else if (C(36.0) <= x_int && x_int <= C(44.0) && y_bound)` (23)이면 `z_int = C(1.78);` (25), `else if (C(56.0) <= x_int && x_int <= C(64.0) && y_bound)` (27)이면 `z_int = C(2.30);` (29)다. 세 직사각형 블록(rectangular block)의 경계를 모두 포함한다. 마지막 `else`는 없다. `return z_int;` (32), 빈 줄, 함수 종료를 포함한다(16·18·22·26·30–31·33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
