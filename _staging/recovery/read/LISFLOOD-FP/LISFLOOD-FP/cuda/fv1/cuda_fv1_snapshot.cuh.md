---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv1/cuda_fv1_snapshot.cuh
lines: 48
sha256: df6ca7b848ba5603a73901db9ae250cd5ebf5409457e17e0b24c777502f81272
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv1_snapshot.cuh — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1), 공통 스냅숏(snapshot)과 FV1 흐름 헤더 포함(2–3), lis::cuda::fv1 이름 공간(namespace)(5–10). `class Snapshot : public lis::cuda::Snapshot<Flow>` (12)를 연다. 조건부 전처리 지시는 없다. |
| 15–31 | 시작 시 5·7·9행 이름 공간·12행 Snapshot 클래스의 public 구역 안. 생성자는 경로·시간 간격·다음 저장 시각·카운터·DEM·Flow·Geometry·pitch·offset·verbose를 받는다(15–26). 기본 정밀도 선언은 `int precision = DEFAULT_PRECISION` (27). 공개 `void wait();` (30)를 선언한다. DEFAULT_PRECISION의 수치 정의는 이 파일에 없다. |
| 32–48 | 시작 시 5·7·9행 이름 공간·12행 Snapshot 클래스 안. protected에 `write(const int& call_gzip)`·`write_maxes()`를 선언한다(32–34). private에는 const DEM 포인터와 여섯 `std::future<void>`를 보관한다(36–43). 클래스·이름 공간을 닫고 빈 줄을 포함한다(44–48). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
