---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/sample.h
lines: 117
sha256: 3a97a1d43a052727245460076eeb6bac8367c45da576be33bc05e686a350f704
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sample.h — 판독 구간 기록

구간은 1행부터 117행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | `#pragma once` (1), geometry 헤더 포함(2), lis 이름 공간(namespace)(4–5). SamplePoints는 count, 좌표 x·y 포인터, idx, x/y 방향 두 인덱스 쌍, inside_domain 포인터를 선언한다(7–18). 조건부 전처리 지시는 없다. |
| 20–45 | SampleBuffer는 size와 time·H·speed 포인터를 갖는다(20–26). Sample의 static initialise는 SamplePoints·파일명·Geometry·pitch·offset·verbose를 받고 static free는 SamplePoints 참조를 받는다(28–44). |
| 46–81 | StageFile은 SamplePoints 참조 생성자, open(resroot, checkpoint, t), write_header(DEM, sample_points_filename, checkpoint, t), write(SampleBuffer, sample_buf_idx), 소멸자를 공개한다(46–75). private 파일 포인터의 기본값은 `FILE* file = nullptr;` (78). const SamplePoints& sample_points를 보관한다(79). |
| 82–102 | GaugeFile의 public 생성자는 SamplePoints 참조를 받는다(82–88). open은 resroot·checkpoint·t를 받고(90–95), write_header는 DEM·sample_points_filename·t를 받는다(97–102). |
| 103–117 | 시작 시 4행 이름 공간·82행 GaugeFile 안. write는 SampleBuffer·sample_buf_idx를 받고(104–108), 소멸자를 선언한다(110). private의 기본값은 `FILE* file = nullptr;` (113), const SamplePoints& 참조를 보관한다(114). 클래스·이름 공간 종료(115–117). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
