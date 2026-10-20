---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/load_neighbour_h.cu
lines: 24
sha256: 8f8debafc9ce944a69742c13ccd33c744ef7d6d8584d49f2ce0f90428b5f8a91
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# load_neighbour_h.cu — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 관련 헤더와 `<algorithm>`을 포함한다(1–2). CUDA 커널 지정은 `__global__ void lis::cuda::acc_nugrid::load_neighbour_h` (4)이다. 인수는 값으로 전달되는 조립 해(assembled solution)·비균일 이웃(nonuniform neighbours)·`bool non_uniform_n`이다(6–8). 스레드 인덱스 식은 `int idx = blockIdx.x * blockDim.x + threadIdx.x;` (11)이다. `if (idx >= d_non_uniform_nghbrs.length) return;` (13)로 이웃 길이 밖의 스레드를 종료한다. 소유 셀(owner cell)과 이웃 셀의 수심·표고 복사는 `d_non_uniform_nghbrs.h_owner[idx] = d_assem_sol.h[d_non_uniform_nghbrs.owner_elem_idcs[idx]];` (15), `d_non_uniform_nghbrs.h_nghbr[idx] = d_assem_sol.h[d_non_uniform_nghbrs.nghbr_elem_idcs[idx]];` (16), `d_non_uniform_nghbrs.z_owner[idx] = d_assem_sol.z0[d_non_uniform_nghbrs.owner_elem_idcs[idx]];` (17), `d_non_uniform_nghbrs.z_nghbr[idx] = d_assem_sol.z0[d_non_uniform_nghbrs.nghbr_elem_idcs[idx]];` (18)이다. 이 파일에는 전처리 조건 분기가 없다. |
| 20–24 | 시작 시 4–10행의 `load_neighbour_h` 커널 안. `if (non_uniform_n) {` (20)일 때 `d_non_uniform_nghbrs.n_owner[idx] = d_assem_sol.n0[d_non_uniform_nghbrs.owner_elem_idcs[idx]];` (21)와 `d_non_uniform_nghbrs.n_nghbr[idx] = d_assem_sol.n0[d_non_uniform_nghbrs.nghbr_elem_idcs[idx]];` (22)를 실행한다. 조건과 커널을 닫는다(23–24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–18·21–22: 명시적 길이 검사는 이웃 인덱스 idx에만 적용된다. `owner_elem_idcs[idx]`와 `nghbr_elem_idcs[idx]`의 값을 조립 해 배열 인덱스로 사용하기 전에 검사하는 조건문은 없다.
- 20–23: `non_uniform_n`이 거짓이면 n_owner와 n_nghbr에 대입하는 실행 경로가 없다. 이 조건에는 else가 없다.
