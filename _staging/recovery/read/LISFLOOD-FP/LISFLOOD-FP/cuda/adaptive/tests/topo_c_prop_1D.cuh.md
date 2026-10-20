---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/topo_c_prop_1D.cuh
lines: 42
sha256: 1e2bfb9fbfe7223451a59f98b3ea7ea086a75025ddef53d2f846f4059b9f9596
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# topo_c_prop_1D.cuh — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_runtime.h` (3)와 `real.h` (5)를 포함한다. 블록 주석은 GK의 HFV1_MATLAB c-property 시험을 흉내 낸 1차원 지형이라는 설명(7–8), `https://github.com/ci1xgk/HFV1_MATLAB/tree/master/Test1_C_Pty` 출처 문자열(9), 입력한 절점(nodal point) 좌표 방향으로만 변한다는 설명(10–12)을 적는다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 14–19 | CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (14)가 붙은 `real topo_c_prop_1D(real x_or_y_int)` (15)을 정의한다. 본문을 열고 입력 좌표를 `a`에 복사한다(16–17). `real z_int;`를 초기값 없이 선언한다(18). 19행은 빈 줄이다. |
| 20–42 | 시작 시 15–16행 `topo_c_prop_1D` 본문 안. `if (a >= 22 && a < 25)` (20)이면 `z_int = C(0.05) * a - C(1.1);` (22)다. `else if (a >= 25 && a <= 28)` (24)이면 `z_int = C(-0.05) * a + C(1.4);` (26)다. `else if (a > 8 && a < 12)` (28)이면 `z_int = C(0.2) - C(0.05) * (a - 10) * (a - 10);` (30)다. `else if (a > 39 && a < 46.5)` (32)이면 `z_int = C(0.3);` (34)다. 마지막 `else` (36)는 `z_int = 0;` (38)이다. 분기를 닫고 `return C(10.0) * z_int;` (41)로 모든 구간의 높이에 10을 곱해 반환한다. 빈 줄과 함수 종료도 포함된다(40·42). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
