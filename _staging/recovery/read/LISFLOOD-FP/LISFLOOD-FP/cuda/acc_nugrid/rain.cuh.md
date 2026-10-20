---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/rain.cuh
lines: 60
sha256: 9f464c09709b237405a391f200ecd22e392598953a55ced0d1de6dd1a677acd5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rain.cuh — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | `#pragma once` (1) 및 강우·블록 변수 매크로·조립 해(assembled solution)·CUDA 런타임(runtime)·장치 실행·계층 인덱스·Morton 코드·압축 헤더를 포함한다(3–10). lis::cuda::acc_nugrid 이름공간(namespace)을 연다(12–17). 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 19–32 | 장치 함수 지정은 `__device__` (19)이며 NUMERIC_TYPE 반환 rate_at_cell을 선언한다(20–31). 강우 배열, i·j, dx, Pars, xsz_rain·tly_rain·dx_rain·dy_rain을 받는다(22–30). 기본 인수와 함수 본문은 없다. 빈 줄도 포함한다(32). |
| 33–49 | DynamicRain 이름공간 여는 문장은 주석이다(33–34). `__global__` (35); `void update_rain` (36)로 update_rain CUDA 커널(kernel)을 선언한다. 조립 해·강우 배열·강우 격자 크기 및 좌표·Pars·Solver를 받는다(37–46). DynamicRain 닫기도 주석이다(48). _NETCDF 조건은 이 헤더의 선언을 감싸지 않는다. |
| 50–60 | `__global__` (50); `void drain_nodata_water` (51)로 drain_nodata_water CUDA 커널을 선언한다. 조립 해·Pars·Solver를 받는다(52–56). 빈 줄과 세 이름공간 닫기를 포함한다(57–60). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
