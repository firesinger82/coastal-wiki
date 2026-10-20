---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/update_max.cu
lines: 31
sha256: 12185933669e5dd6094734fe1440e23e3d49d2dfdbc6e9da88beb89d17f33ea4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# update_max.cu — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 관련 헤더와 algorithm 포함(1–2). `__global__ void lis::cuda::acc_nugrid::update_max` (4)의 CUDA 커널(kernel)은 AssembledSolution·Solver와 maxH·totalHtm·maxHtm·initHtm 배열 포인터를 받는다(5–12). 스레드 인덱스는 `int idx = blockIdx.x * blockDim.x + threadIdx.x;` (14), 경계는 `if (idx >= d_assem_sol.length) return;` (16). 전처리 조건 분기는 없다. |
| 18–31 | 시작 시 4행 update_max 커널 안. `if (d_assem_sol.h[idx] > solver.DepthThresh)` (18)이면 젖은 셀로 처리한다. `if (initHtm[idx] == NULLVAL)` (20)일 때 첫 도달 시간을 `initHtm[idx] = solver.t / C(3600.0);` (21)로 기록한다. 젖은 시간 누적식은 `totalHtm[idx] += solver.Tstep / C(3600.0);` (23). `if (d_assem_sol.h[idx] > maxH[idx])` (25) 참이면 maxH에 현재 수심을 복사하고(27) 최대 수심 시간은 `maxHtm[idx] = solver.t / C(3600.0);` (28)로 기록한다. C(3600.0)으로 나누어 시간을 시간(hour) 단위로 바꾼다. 두 조건과 커널을 닫는다(29–31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–30: 수심이 DepthThresh와 같으면 기록을 갱신하지 않는다. 현재 수심이 maxH와 같을 때도 maxHtm 갱신은 없다.
