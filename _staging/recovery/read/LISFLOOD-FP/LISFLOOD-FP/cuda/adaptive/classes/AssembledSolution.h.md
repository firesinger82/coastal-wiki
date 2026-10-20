---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/AssembledSolution.h
lines: 83
sha256: 03dba1704e4d08b15823b9051595da1ce3dbe1a4b9329f8abff38b97d81ed925
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# AssembledSolution.h — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | `#pragma once` (1). CUDA 유틸리티·real·HierarchyIndex·SolverTypes 헤더를 포함한다(3–7). 전처리 조건 분기는 없다. AssembledSolution은 h·qx·qy·z의 0·1x·1y 계수 포인터(pointer), 활성 인덱스·레벨·길이와 is_copy_cuda=false를 보유한다(9–30). |
| 32–56 | 시작 시 9–10행 AssembledSolution 구조체 안. 생성자(constructor)의 바이트 식 `size_t bytes_real = num_finest_elems * sizeof(real);`<br>`size_t bytes_int  = num_finest_elems * sizeof(HierarchyIndex);` (34–35). h0·qx0·qy0·z0는 malloc_device로 할당한다(37–40). x·y계수의 조건부 할당식 전체 `h1x  = (solver_type == MWDG2) ? (real*)malloc_device(bytes_real) : nullptr;`<br>`qx1x = (solver_type == MWDG2) ? (real*)malloc_device(bytes_real) : nullptr;`<br>`qy1x = (solver_type == MWDG2) ? (real*)malloc_device(bytes_real) : nullptr;`<br>`z1x  = (solver_type == MWDG2) ? (real*)malloc_device(bytes_real) : nullptr;`<br>`h1y  = (solver_type == MWDG2) ? (real*)malloc_device(bytes_real) : nullptr;`<br>`qx1y = (solver_type == MWDG2) ? (real*)malloc_device(bytes_real) : nullptr;`<br>`qy1y = (solver_type == MWDG2) ? (real*)malloc_device(bytes_real) : nullptr;`<br>`z1y  = (solver_type == MWDG2) ? (real*)malloc_device(bytes_real) : nullptr;` (42–50). 활성 인덱스·레벨도 bytes_int로 할당하고 length=num_finest_elems를 저장한다(52–54). MWDG2의 정의·값은 이 파일에 없다. |
| 57–83 | 시작 시 9–10행 AssembledSolution 구조체 안. 복사 생성자(copy constructor)는 *this=original 뒤 is_copy_cuda=true로 설정한다(57). 소멸자(destructor)는 `if (!is_copy_cuda)` (61)일 때만 모든 계수·인덱스·레벨 포인터에 free_device를 호출하고 CHECK_CUDA_ERROR로 감싼다. 호출 전체 `CHECK_CUDA_ERROR( free_device(h0) );`<br>`CHECK_CUDA_ERROR( free_device(qx0) );`<br>`CHECK_CUDA_ERROR( free_device(qy0) );`<br>`CHECK_CUDA_ERROR( free_device(z0) );`<br>`CHECK_CUDA_ERROR( free_device(h1x) );`<br>`CHECK_CUDA_ERROR( free_device(qx1x) );`<br>`CHECK_CUDA_ERROR( free_device(qy1x) );`<br>`CHECK_CUDA_ERROR( free_device(z1x) );`<br>`CHECK_CUDA_ERROR( free_device(h1y) );`<br>`CHECK_CUDA_ERROR( free_device(qx1y) );`<br>`CHECK_CUDA_ERROR( free_device(qy1y) );`<br>`CHECK_CUDA_ERROR( free_device(z1y) );`<br>`CHECK_CUDA_ERROR( free_device(act_idcs) );`<br>`CHECK_CUDA_ERROR( free_device(levels) );` (63–79). 소멸자·구조체 종료(80–83). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35·52–53: bytes_int는 sizeof(HierarchyIndex)를 사용한다. levels의 형식은 int*이지만 같은 bytes_int로 할당한다. 두 형식의 크기 일치는 이 파일에서 확인하지 않았다.
- 32–55: 생성자는 장치(device) 메모리를 할당하지만 계수·인덱스·레벨 배열의 원소 값을 초기화하는 문장은 없다.
