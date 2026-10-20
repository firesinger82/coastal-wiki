---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/compaction.cu
lines: 158
sha256: 872af7dbe7ba4be38eb78788e874a0bbe92a2135fccc6ef1c2abd67fdbece3f1
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# compaction.cu — 판독 구간 기록

구간은 1행부터 158행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | `compaction.cuh` 포함(1), 압축(compaction) 함수 `lis::cuda::acc_nugrid::compaction` 정의와 인수 선언(3–12). 전처리 조건 분기는 없다. 장치(device) 임시 저장소와 길이, 호스트(host) 길이를 준비한다(13–17). `CHECK_CUDA_ERROR( cub::DeviceSelect::Flagged` (19) 호출은 `d_temp_storage=NULL`, 입력 `d_buf_sol.z0`, 선택 플래그 `d_compaction_flags.north_east`, 출력 `d_sol.z0`, 개수 `num_finest_elems`로 저장소 크기를 받는다(19–28). `malloc_device(temp_storage_bytes)`로 임시 저장소를 할당한다(30). |
| 32–64 | 시작 시 3행 `compaction` 함수 안. `h`, `qx`, `qy`를 선택하는 `cub::DeviceSelect::Flagged` 호출 세 블록은 모두 `//` 주석이다(32–63). 빈 줄을 포함한다(64). |
| 65–110 | 시작 시 3행 `compaction` 함수 안. `CHECK_CUDA_ERROR( cub::DeviceSelect::Flagged` (65), `CHECK_CUDA_ERROR(cub::DeviceSelect::Flagged` (76·87) 호출은 같은 `north_east` 플래그로 `z0`, `z1x`, `z1y`를 `d_buf_sol`에서 `d_sol`로 선택한다(65–96). `if (non_uniform_n) {` (98)이면 같은 선택 호출로 `n0`도 압축한다(99–108). 이 구간에는 전처리 조건 분기가 없다. |
| 111–158 | 시작 시 3행 `compaction` 함수 안. `if (startfile) {` (111)이면 `cub::DeviceSelect::Flagged`로 수심 `h`를 선택한다(112–121). 이 조건 밖에서 `levels`, `act_idcs`를 같은 `north_east` 플래그로 선택한다(124–144). `copy_cuda(h_sol_len, d_sol_len, sizeof(int))` 호출 뒤 `d_sol.length`에 호스트 길이를 복사한다(146–153). `free_device` 두 번과 `delete`로 임시 저장소와 길이 저장소를 해제한다(155–157). 함수 종료(158). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–63·111–122: `h`의 무조건 압축과 `qx`, `qy` 압축은 주석 처리되어 있다. 실행되는 `h` 압축은 `startfile` 조건 안에 있다.
- 65–144: 모든 실행 선택 호출이 같은 `d_sol_len`에 개수를 기록한다. 146–153행은 마지막 선택 호출 뒤의 길이를 읽는다.
