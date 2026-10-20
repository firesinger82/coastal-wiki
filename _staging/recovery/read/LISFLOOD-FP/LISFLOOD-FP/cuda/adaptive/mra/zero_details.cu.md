---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/zero_details.cu
lines: 56
sha256: 05d3600fff870ee9270f8a1ac112164e87378f0070832ca4d90ae5dd5aacda87
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# zero_details.cu — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 헤더 포함(1), `__global__` (3) 커널(kernel) zero_details의 인수·본문 시작(4–11). 조건부 전처리 분기는 없다. `HierarchyIndex idx = blockIdx.x * blockDim.x + threadIdx.x;` (12) 뒤 `if (idx >= num_details) return;` (14)로 개수를 검사한다. eta0·qx0·qy0의 alpha·beta·gamma를 모두 C(0.0)으로 초기화한다(16–26). 원문 초기화 예시는 `d_details.eta0.alpha[idx] = C(0.0);`<br>`d_details.eta0.beta[idx]  = C(0.0);`<br>`d_details.eta0.gamma[idx] = C(0.0);` (16–18)이다. |
| 28–56 | 시작 시 3–11행 zero_details 커널 안. `if (solver_params.solver_type == MWDG2)` (28)이면 eta1x·qx1x·qy1x·eta1y·qx1y·qy1y 각각의 alpha·beta·gamma를 C(0.0)으로 초기화한다(30–52). 분기 종료(53) 뒤 솔버(solver) 종류와 관계없이 `d_norm_details[idx] = C(0.0);` (55)로 정규화 상세(norm detail)를 초기화한다. 커널 종료(56). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
