---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/metal/fv1/metal_fv1_simulate.h
lines: 78
sha256: 24c529444ca4c2b3fdc0e7ef9b29976cabb5355c8160a5d5b8536a46c0155318
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# metal_fv1_simulate.h — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | C++와 Metal 그래픽 처리 장치(graphics processing unit, GPU) 계산 인터페이스 머리말·빈 줄(1–5), `#pragma once` (6). `#ifdef __APPLE__` (8) 안에서 geometry.h·lisflood.h를 포함(10–11)하고 lis::metal::fv1 이름공간을 연다(13–15). SimulatorImpl을 전방 선언한다(17–18). 8행 조건은 78행까지 이어지며 이 파일에 `#else`는 없다. |
| 20–30 | 시작 시 8행 `#ifdef __APPLE__` 안이며 13–15행 이름공간 안. CUDA 구조를 따른다는 주석(20)과 `Flow` 구조체(21–29). NUMERIC_TYPE 포인터 H·HU·HV·maxH·totalHtm·maxHtm·initHtm을 선언한다(22–28). 필드 초기값 대입은 없다. |
| 31–50 | 시작 시 8행 `#ifdef __APPLE__`·13–15행 이름공간 안. Simulator 클래스와 public 영역(31–33), 생성자·소멸자(34–37). initialize는 H·HU·HV·DEM·Mann을 받는다(39–41). step은 NUMERIC_TYPE을 반환한다(43–44). copy_to_host는 H·HU·HV를 받으며 copy_max_to_host는 maxH를 받는다(46–50). 이 구간은 선언이며 구현은 없다. |
| 51–66 | 시작 시 8행 `#ifdef __APPLE__`·13–15행 이름공간·32행 Simulator 클래스 안. get_time·apply_uniform_rain·정적 is_available 선언(52–59). 유효성 함수는 `bool is_valid() const { return impl != nullptr; }` (62). private의 SimulatorImpl 포인터 impl은 구현 은닉(pointer to implementation) 용도이다(64–65). 클래스 종료(66). |
| 67–78 | 시작 시 8행 `#ifdef __APPLE__`·13–15행 이름공간 안. 통합 진입점 주석 두 줄(68–69), simulate 선언(70–72). Solver의 전역 이름공간을 `::Solver` (71)로 지정한다. 이름공간 종료(74–76), `#endif // __APPLE__` (78). `__APPLE__`가 정의되지 않으면 10–76행은 컴파일 대상에서 제외된다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–28: Flow의 일곱 포인터 필드는 선언에 초기값이 없다.
- 68–69: 통합 진입점 주석이 같은 내용으로 두 번 연속 등장한다.
