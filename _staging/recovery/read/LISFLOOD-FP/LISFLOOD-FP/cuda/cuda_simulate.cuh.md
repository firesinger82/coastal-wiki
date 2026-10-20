---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_simulate.cuh
lines: 119
sha256: 4d632ce06c54e107004b528ae0f2832c60536472da5aa4f69e1b2aa94940d521
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_simulate.cuh — 판독 구간 기록

구간은 1행부터 119행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | `#pragma once` (1), lisflood·geometry·rain·stats·cuda_stats 헤더 포함(2–4·7–8). acc flow·max_field include는 주석(5–6). lis::cuda 이름 공간(namespace)(10–13), Simulation 클래스(class)(15–16)의 protected 영역(17), print_device_info 원형(18). 별도 전처리 조건 분기는 없다. |
| 20–54 | 시작 시 15행 Simulation 클래스 protected 영역 안. initialise_H는 H·파일명·States 참조·DEM·Geometry 참조·pitch·offset·verbose를 받는다(20–30). nullify_max는 maxHtm·initHtm·totalHtm·Geometry 참조·pitch·offset·verbose를 받는다(32–41). initialise_discharge는 HU·HV·파일명·States 참조·Geometry 참조·pitch·offset·verbose를 받는다(43–53). |
| 55–79 | 시작 시 15행 클래스 protected 영역 안. initialise_manning은 manning 포인터·파일명·Geometry 참조·pitch·offset·verbose를 받는다(55–63). update_geometry는 Pars& dst·Geometry& src(65–69), load_boundaries는 Fnames·States·Pars·BoundCs 참조와 verbose를 받는다(71–78). |
| 80–96 | 시작 시 15행 클래스 protected 영역 안. read_checkpoint 원형은 Fnames·States·Pars·Solver 참조, H·Qx·Qy·maxH·totalHtm·maxHtm·initHtm 포인터, StatsCollector& Stats_Entry와 verbose를 받는다(80–95). |
| 97–119 | 시작 시 15행 클래스 protected 영역 안. write_checkpoint는 Fnames·States·Pars·Solver 참조, H·Qx·Qy·maxH·totalHtm·maxHtm·initHtm 포인터, lis::StatsEntry& Stats_Entry, NUMERIC_TYPE dt, verbose를 받는다(97–113). 빈 줄(114–115), 클래스·이름 공간 종료(116–119). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 93·110: 판독의 통계 인수 형식은 StatsCollector&이다. 기록의 통계 인수 형식은 lis::StatsEntry&이다.
