---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/reinsert_point_srcs.cu
lines: 29
sha256: fc29700cfd37f01cb754ade7622b096b7bdbb493b1a59446465f3b7317ac7527
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# reinsert_point_srcs.cu — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 헤더 포함(1), `__global__` (3) 커널(kernel) reinsert_point_srcs의 입력은 스케일 계수(scale coefficient), 점원(point source), dt·dx_finest·max_ref_lvl이다(4–12). 조건부 전처리 분기는 없다. `HierarchyIndex idx = blockIdx.x * blockDim.x + threadIdx.x;` (13)로 스레드(thread) 위치를 계산하고 `if (idx >= point_sources.num_srcs) return;` (15)로 점원 개수를 검사한다. `HierarchyIndex h_idx = get_lvl_idx(max_ref_lvl) + point_sources.d_codes[idx];` (17)로 최세 레벨의 계층 위치를 계산하고 src_type을 읽는다(19). |
| 21–29 | 시작 시 3–12행 reinsert_point_srcs 커널 안. `if (src_type == HFIX \|\| src_type == HVAR)` (21)이면 d_srcs[idx]를 eta0[h_idx]에 복사한다(23). `else if (src_type == QFIX \|\| src_type == QVAR)` (25)이면 `d_scale_coeffs.eta0[h_idx] += point_sources.q_src(dt, dx_finest, idx);` (27)로 q_src(dt, dx_finest, idx) 반환값을 수위 계수에 가산한다. 두 분기·커널 종료(24·28–29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21–28: HFIX·HVAR·QFIX·QVAR 외의 src_type에 대한 마지막 else는 없다.
- 17·23–27: 점원은 max_ref_lvl의 d_codes[idx] 위치를 사용한다. 같은 h_idx에 대한 동시 쓰기를 조정하는 atomic 함수는 이 커널에 없다.
