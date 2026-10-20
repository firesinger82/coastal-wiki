---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/neighbours/compaction.cu
lines: 203
sha256: 6b19355c1669e914a5e76443a42547899aa1d2900f8333a12469ccc80cf34bc5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# compaction.cu — 판독 구간 기록

구간은 1행부터 203행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 헤더 포함(1), `__host__` (3) 지정의 호스트(host) 함수 compaction 정의(4–14). 조립 해(assembled solution)와 이웃의 입력 버퍼(buffer)·출력, 압축 플래그(compaction flag), 최세 원소 수 및 const SolverParams 참조를 받는다(6–12). 조건부 전처리 분기는 없다. 임시 저장소는 NULL, 바이트 수는 0으로 시작한다(15–16). `int* d_assem_sol_len = (int*)malloc_device( sizeof(int) );` (18)로 장치 정수 하나를 할당하고 호스트 int 하나도 new로 할당한다(19). `CHECK_CUDA_ERROR( cub::DeviceSelect::Flagged`<br>`(`<br>`d_temp_storage,`<br>`temp_storage_bytes,`<br>`d_buf_assem_sol.z0,`<br>`d_compaction_flags.north_east,`<br>`d_assem_sol.z0,`<br>`d_assem_sol_len,`<br>`num_finest_elems`<br>`) );` (21–30)은 NULL 임시 저장소와 z0 입력·출력, north_east 플래그, num_finest_elems를 전달한다. malloc_device(temp_storage_bytes)로 임시 저장소를 할당한다(32). |
| 34–77 | 시작 시 3–14행 compaction 함수 안. 34행 /*부터 76행 */까지는 블록 주석이다. h0·qx0·qy0·z0 각각에 north_east 플래그를 적용하는 CHECK_CUDA_ERROR(cub::DeviceSelect::Flagged(...)) 호출 네 개가 이 주석 안에 있다(34–43·45–54·56–65·67–76). 이 호출들은 실행문이 아니다. |
| 78–108 | 시작 시 3–14행 compaction 함수 안. CHECK_CUDA_ERROR로 감싼 cub::DeviceSelect::Flagged가 조립 해 act_idcs를 north_east 플래그로 선택한다(78–87). copy_cuda(h_sol_len, d_assem_sol_len, sizeof(int))를 호출한다(89–94). *h_sol_len을 d_assem_sol.length로 복사한다(96). 같은 선택 루틴으로 조립 해 levels를 north_east 플래그에 따라 출력한다(98–107). 모든 선택 호출의 입력 수는 num_finest_elems다. |
| 109–152 | 시작 시 3–14행 compaction 함수 안. CHECK_CUDA_ERROR(cub::DeviceSelect::Flagged(...))를 네 번 호출한다. 이웃 north.act_idcs와 east.act_idcs는 north_east 플래그(109–118·120–129), south.act_idcs와 west.act_idcs는 south_west 플래그(131–140·142–151)를 사용한다. 입력 버퍼에서 대응 출력 이웃 배열로 선택하고 d_assem_sol_len을 공통 선택 개수 포인터로 전달한다. |
| 153–198 | 시작 시 3–14행 compaction 함수 안. `if (solver_params.solver_type == MWDG2)` (153)이면 이웃 levels 네 배열에도 CHECK_CUDA_ERROR(cub::DeviceSelect::Flagged(...))를 호출한다. north·east는 north_east 플래그(155–164·166–175), south·west는 south_west 플래그(177–186·188–197)를 사용한다. num_finest_elems와 같은 임시 저장소를 전달한다. 조건 종료(198). |
| 199–203 | 시작 시 3–14행 compaction 함수 안이며 153행 if 밖. 빈 줄(199) 뒤 free_device(d_temp_storage), free_device(d_assem_sol_len), delete h_sol_len으로 두 장치 할당과 호스트 할당을 해제한다(200–202). 함수 종료(203). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–32·34–76: z0 입력·출력을 전달하는 첫 DeviceSelect::Flagged 호출은 d_temp_storage=NULL 상태에 있다. 임시 저장소 할당 뒤의 z0 선택 호출과 h0·qx0·qy0 선택 호출은 모두 블록 주석 안에 있다.
- 89–107·109–197: d_assem_sol.length는 act_idcs 선택 직후 한 번만 복사한다. 이후 levels·이웃 선택 호출들은 같은 d_assem_sol_len에 선택 개수를 출력하지만 이를 호스트로 다시 복사하는 문장은 없다.
- 153–198: 이웃 levels 배열의 선택 호출은 MWDG2 분기 안에만 있다.
