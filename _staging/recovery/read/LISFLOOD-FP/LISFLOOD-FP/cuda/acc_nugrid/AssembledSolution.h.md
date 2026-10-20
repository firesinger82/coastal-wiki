---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/AssembledSolution.h
lines: 91
sha256: 87d0254b26cb7430f01b68a148233c4c867a0ff7e5b62f1eeb7c8600649ca3c8
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# AssembledSolution.h — 판독 구간 기록

구간은 1행부터 91행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | `#pragma once` (1), cuda_utils·lisflood·index_1D 포함(3–5), `lis::cuda::acc_nugrid` 이름공간(namespace)(7–12). 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. 구조체(struct) AssembledSolution은 h·z0·z1x·z1y·n0·v의 NUMERIC_TYPE 포인터(14–26), act_idcs·levels·nghbr_counts·cumu_nghbr_counts 포인터와 length를 보유한다(28–32). qx·qy·q3·q4·zxy 선언은 주석(17–20·24). `bool      is_copy = false;` (33). |
| 35–61 | 시작 시 14행 AssembledSolution 구조체 안. 생성자(constructor)는 최세 격자 요소 수(num_finest_elems)와 non_uniform_n을 받는다(35–36). `size_t bytes_real = num_finest_elems * sizeof(NUMERIC_TYPE);` (37), `size_t bytes_int  = num_finest_elems * sizeof(index_1D);` (38). h·v·z0·z1x·z1y에 `(NUMERIC_TYPE*)malloc_device(bytes_real)`로 장치 메모리(device memory)를 할당한다(40–41·46–48). q 계열·zxy 할당은 주석(42–45·49). `n0                = (non_uniform_n) ? (NUMERIC_TYPE*)malloc_device(bytes_real) : nullptr;` (52). act_idcs는 `(index_1D*)malloc_device(bytes_int)` (54), levels·nghbr_counts·cumu_nghbr_counts는 `(int*)malloc_device(bytes_int)` (55–57). length=num_finest_elems(58), is_copy 재설정은 주석(59). 생성자 종료와 빈 줄(60–61). |
| 62–91 | 시작 시 14행 구조체 안. 복사 생성자(copy constructor) `AssembledSolution(const AssembledSolution& original) { *this = original; is_copy = true; }` (62)는 멤버를 복사한 후 복사본 표시를 설정한다. 소멸자(64–85)의 `if (!is_copy)` (66)에서 h·z0·z1x·z1y·v·n0·act_idcs·levels·nghbr_counts·cumu_nghbr_counts에 free_device를 호출한다(68·73–76·79–83). q 계열·zxy 해제는 주석(69–72·78). 구조체·이름공간 종료와 빈 줄(86–91). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37–38·54–57: int*인 levels·nghbr_counts·cumu_nghbr_counts에도 sizeof(index_1D)로 계산한 bytes_int를 사용한다. index_1D의 실제 정의는 이 파일에 없다.
- 40–58: 생성자는 메모리를 할당하지만 h·v·지형·이웃 배열 원소를 채우는 문장을 포함하지 않는다.
- 52·66–83: non_uniform_n이 거짓이면 n0는 nullptr다. 원본 소멸자는 별도 n0 조건 없이 free_device(n0)를 호출한다. free_device 내부의 처리는 이 파일에 없다.
