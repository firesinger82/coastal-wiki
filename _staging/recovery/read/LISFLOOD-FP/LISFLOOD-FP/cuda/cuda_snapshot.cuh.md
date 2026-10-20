---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_snapshot.cuh
lines: 139
sha256: 7a3588bd7933301d5a5c6797e10a0f87fcc792f15c3c9a5c588686c4486a6ca9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_snapshot.cuh — 판독 구간 기록

구간은 1행부터 139행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | `#pragma once` (1)와 lisflood.h·geometry.h·io.h·future 포함(2–5), lis::cuda 이름공간(namespace)(7–10)이다. 파일 내부에 전처리 조건 분기는 없다. `template<typename F>` (12)의 `Snapshot` 생성자는 출력 이름·간격·다음 저장 시각·번호·상태·기하·pitch·offset·verbose·precision을 받는다(16–28). 정밀도 기본값은 `int precision = DEFAULT_PRECISION` (27)이다. 이 파일은 DEFAULT_PRECISION 값을 정의하지 않는다. |
| 29–60 | 시작 시 13행 Snapshot 클래스 안이다. `write_if_needed`·`write_max_files`·수위/유량/유속 기록 활성화 인터페이스(interface)를 선언한다(30–49). `virtual void wait() = 0;` (51), 공개 counter·next_save(53–54), 보호된 순수 가상 함수(pure virtual function) `write`·`write_maxes`(56–59)를 선언한다. |
| 61–95 | 시작 시 13행 Snapshot 클래스의 protected 영역 안이다. `template<typename T>` (61·70)인 비동기 기록(asynchronous writing) `write_async`와 최대값 기록 `write_max`를 선언한다(62–76). 상태 참조와 기본값 `bool write_elevation = false;` (79), `bool write_discharge = false;` (80), `bool write_velocity = false;` (81), `NUMERIC_TYPE DepthThresh = C(0.0);` (82)를 둔다. private에는 출력 이름·기하 참조·간격·pitch·offset·상세 출력·정밀도가 있다(84–94). |
| 96–116 | `VelocityWriter`는 H·discharge·DepthThresh를 받는 생성자와 인덱스 연산자(index operator)를 선언한다(96–109). private 멤버에는 수정 가능한 두 NUMERIC_TYPE 포인터와 임계값이 있다(111–115). |
| 117–139 | `ElevationWriter`는 const H·DEM 포인터를 받는 생성자와 const 인덱스 연산자를 선언한다(117–134). 이름공간을 닫고(136–137), `#include "cuda_snapshot.templates.cu"` (139)로 템플릿 구현을 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
