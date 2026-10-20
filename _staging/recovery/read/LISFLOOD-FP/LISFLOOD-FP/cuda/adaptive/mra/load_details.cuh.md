---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/load_details.cuh
lines: 117
sha256: 72a5c7004054a280ec06187a79d72e3ff3d625da37b8182a77072c8730d2f0fd
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# load_details.cuh — 판독 구간 기록

구간은 1행부터 117행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `#pragma once` (1). CUDA 실행 환경, Detail.h, Details.h, HierarchyIndex.h를 포함한다(3–7). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 9–39 | `__device__ __forceinline__ DetailHW load_details_hw` (9)는 Details와 HierarchyIndex의 const 참조를 받는 장치 함수(device function)이다(10–14). 반환 집합 초기화(aggregate initialization)는 eta0, qx0, qy0, z0 순으로 각각 alpha[h_idx], beta[h_idx], gamma[h_idx]를 복사한다(15–37). 각 묶음은 eta0(17–21), qx0(22–26), qy0(27–31), z0(32–36)이다. 산술 연산이나 조건 분기는 없다. 함수 닫기와 빈 줄도 포함한다(38–39). |
| 40–81 | `__device__ __forceinline__ DetailMW load_details_mw` (40)는 Details와 HierarchyIndex의 const 참조를 받는다(41–45). 반환 집합 초기화를 시작한다(46–47). 첫 큰 묶음은 eta0, eta1x, eta1y 각각의 alpha[h_idx], beta[h_idx], gamma[h_idx]를 순서대로 복사한다(48–64). 다음 큰 묶음은 qx0, qx1x, qx1y 각각의 같은 세 필드를 복사한다(65–81). 이 구간은 qx 묶음 닫기까지이며 반환 초기화와 함수는 다음 구간으로 이어진다. |
| 82–117 | 시작 시 40–45행 load_details_mw 함수·46–47행 반환 집합 초기화 안. qy 묶음에는 qy0, qy1x, qy1y 각각의 alpha[h_idx], beta[h_idx], gamma[h_idx]를 복사한다(82–98). 마지막 z 묶음에는 z0, z1x, z1y 각각의 같은 세 필드를 복사한다(99–115). 반환 초기화와 함수를 닫는다(116–117). 산술 연산이나 조건 분기는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
