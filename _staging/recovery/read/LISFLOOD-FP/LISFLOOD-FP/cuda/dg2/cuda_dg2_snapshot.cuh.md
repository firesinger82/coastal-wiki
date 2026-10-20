---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_snapshot.cuh
lines: 56
sha256: f591333bace7f0ba1613044049ed4144719502edb4a88d7ff35a228549f59e3d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_snapshot.cuh — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1), 공통 snapshot·DG2 DEM·flow 헤더 포함(2–4), lis::cuda::dg2 이름공간(namespace)(6–11)이다. 전처리 조건 분기는 없다. |
| 13–32 | `class Snapshot : public lis::cuda::Snapshot<Flow>` (13)은 공통 템플릿 클래스를 공개 상속(public inheritance)한다. 생성자는 출력 이름·간격·다음 시각·번호·Topography·Flow·기하·pitch·offset·verbose·정밀도를 받는다(16–29). 정밀도 기본값은 `int precision = DEFAULT_PRECISION` (28)이다. 이 파일은 해당 매크로 값을 정의하지 않는다. 공개 wait를 선언한다(31). |
| 33–56 | 시작 시 13행 Snapshot 클래스 안이다. protected에는 write(call_gzip)·write_maxes(33–35), private에는 const Topography& DEM·Flow& U(37–39)가 있다. 비동기 기록(asynchronous writing)의 std::future<void>를 수위·수심 계수 3개·x 유량 계수 3개·y 유량 계수 3개·속도 2개에 각각 보유한다(40–51). 클래스·이름공간을 닫는다(52–56). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
