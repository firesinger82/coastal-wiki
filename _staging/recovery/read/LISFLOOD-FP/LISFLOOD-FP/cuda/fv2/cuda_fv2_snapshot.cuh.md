---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_snapshot.cuh
lines: 50
sha256: 02b7d359702d3f39dca918d01f54e6d60668da425608f8743965bef0f894c4ae
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_snapshot.cuh — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#pragma once` (1), 공통 스냅숏(snapshot)·FV2 지형·FV2 흐름 헤더 포함(2–4), lis::cuda::fv2 이름 공간(namespace)(6–11). `class Snapshot : public lis::cuda::Snapshot<Flow>` (13)와 public 구역을 연다(15). 조건부 전처리 지시는 없다. |
| 16–32 | 시작 시 6·8·10행 이름 공간·13행 Snapshot 클래스 안. 생성자는 경로·간격·다음 저장 시각·카운터·Topography·Flow·Geometry 참조·pitch·offset·verbose를 받는다(16–27). 기본 정밀도는 `int precision = DEFAULT_PRECISION` (28). 공개 wait를 선언한다(31). DEFAULT_PRECISION의 수치 정의는 이 파일에 없다. |
| 33–50 | 시작 시 6·8·10행 이름 공간·13행 클래스 안. protected write·write_maxes(33–35). private에는 const Topography& DEM·Flow& U와 여섯 future를 보관한다(37–45). 클래스·이름 공간을 닫는다(46–50). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
