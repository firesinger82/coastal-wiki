---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/store_details.cuh
lines: 86
sha256: e91b58c9b1f9702a4dfa024a8551e5ddeff9450d8125670b5a4a98d552f7410e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# store_details.cuh — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | `#pragma once` (1)로 중복 포함을 막고 CUDA 실행 및 Detail·Details 형식 헤더를 포함한다(3·5–6). 조건부 전처리 분기는 없다. |
| 8–29 | `__device__ __forceinline__` (8) 지정의 장치(device) 인라인(inline) 함수 store_details를 정의한다(9–15). const DetailHW·Details 참조와 const int h_idx 참조를 받는다(11–13). eta·qx·qy 각각의 alpha·beta·gamma를 d_details의 eta0·qx0·qy0 배열 h_idx 위치로 복사한다(16–26). 빈 줄과 함수 종료(27–29). 조건·계산식·기본값 대입은 없다. |
| 30–61 | `__device__ __forceinline__` (30) 지정의 DetailMW 오버로드(overload)를 정의한다(31–37). detail.eta의 _0·_1x·_1y 각각의 alpha·beta·gamma를 eta0·eta1x·eta1y에 복사한다(38–48). detail.qx의 같은 세 성분을 qx0·qx1x·qx1y에 복사한다(50–60). 모든 출력 위치는 h_idx이며 조건 분기는 없다. |
| 62–86 | 시작 시 30–37행 DetailMW용 store_details 함수 안. detail.qy의 _0·_1x·_1y 각각의 alpha·beta·gamma를 qy0·qy1x·qy1y의 h_idx에 복사한다(62–72). z0·z1x·z1y 복사문은 73행 /*와 85행 */ 사이의 블록 주석이므로 실행되지 않는다(74–84). 함수 종료(86). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 73–85: DetailMW 오버로드의 z0·z1x·z1y 상세 계수 저장문 전체가 블록 주석 안에 있다.
- 11–26·33–72: d_details는 const Details&로 받으며 그 멤버 배열의 h_idx 위치에는 값을 대입한다.
