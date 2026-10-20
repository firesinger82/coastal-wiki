---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/neighbours/get_compaction_flags.cu
lines: 38
sha256: 7ec51709f814c1dc193ffa7bf12589f9f7cc6f09bcd49bf67e2108203a0bb927
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_compaction_flags.cu — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 헤더 포함(1), `__global__` (3) 지정의 커널(kernel) get_compaction_flags 입구·인수 선언(4–10). 조립 해(assembled solution), 압축 플래그(compaction flag), 최세 원소 수를 받는다(6–8). 조건부 전처리 분기는 없다. `HierarchyIndex idx = blockIdx.x * blockDim.x + threadIdx.x;` (11) 뒤 `if (idx >= num_finest_elems) return;` (13)로 개수를 검사하고 현재 활성 인덱스(index)를 읽는다(15). |
| 17–27 | 시작 시 3–10행 get_compaction_flags 커널 안. `if ( idx < (num_finest_elems - 1) )` (17)이면 오른쪽 활성 인덱스 act_idcs[idx + 1]를 읽고(19), `d_compaction_flags.north_east[idx] = !(current == right);` (21)로 현재 값과 달라지는 마지막 위치에 north_east 플래그를 설정한다. `else` (23)에서는 마지막 원소의 north_east를 1로 설정한다(25). |
| 28–38 | 시작 시 3–10행 get_compaction_flags 커널 안. `if (idx > 0)` (28)이면 왼쪽 활성 인덱스 act_idcs[idx - 1]를 읽고(30), `d_compaction_flags.south_west[idx] = !(current == left);` (32)로 현재 값과 달라지는 첫 위치에 south_west 플래그를 설정한다. `else` (34)에서는 첫 원소의 south_west를 1로 설정한다(36). 분기·커널 종료(37–38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
