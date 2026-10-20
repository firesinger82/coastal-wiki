---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_sample.cuh
lines: 129
sha256: 14cd7937da618258f34563009518836698a3759cd5649190f4adc747bae471c7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_sample.cuh — 판독 구간 기록

구간은 1행부터 129행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | `#pragma once` (1), `#define DEFAULT_SAMPLE_BUFFER_SIZE 1` (2), lisflood·sample 헤더(3–4), lis::cuda 이름 공간(namespace)(6–9), Sampler 클래스(class)(11–12). 공개 생성자 원형은 SamplePoints& d_sample_points·int& sample_buf_idx·int verbose를 받는다(14–19). 별도 전처리 조건 분기는 없다. |
| 21–57 | 시작 시 11행 Sampler 클래스 공개 영역 안. load_sample_points는 파일명·Geometry 참조·pitch·offset(21–27), open_stage_file·open_gauge_file은 파일명·checkpoint·t(29–41)를 받는다. write_stage_header는 DEM·표본점 파일명·checkpoint·t(43–49), write_gauge_header는 DEM·표본점 파일명·t(51–56)를 받는다. |
| 58–79 | 시작 시 11행 클래스 공개 영역 안. sample은 H·HU·HV·t(58–64), sample_ACC는 H·Vx·Vy·t(66–72)를 받는다. write_if_buffer_full·write·소멸자(destructor) 원형(74–78), 빈 줄. |
| 80–115 | 시작 시 11행 클래스 안. private(80)의 buffer_full·copy_buffer·initialise_sample_points 원형(81–85), free(SamplePoints&)(87–90). allocate_pinned(92–97)의 기본 크기는 `int size = DEFAULT_SAMPLE_BUFFER_SIZE` (96), allocate_device(99–104)도 `int size = DEFAULT_SAMPLE_BUFFER_SIZE` (103). 두 함수는 SampleBuffer 참조·점 수·크기를 받는다. free_pinned·free_device는 SampleBuffer 참조를 받는다(106–114). |
| 116–129 | 시작 시 11행 클래스 private 영역 안. 기본 상태는 `bool active = false;` (116), `bool write_speed = false;` (117). sample_buf_idx 참조, 호스트 SamplePoints와 장치 SamplePoints 참조, SampleBuffer 두 개, StageFile·GaugeFile·verbose 멤버(118–125). 클래스·이름 공간 종료(126–129). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2·96·103: 호스트·장치 버퍼 할당의 기본 크기는 DEFAULT_SAMPLE_BUFFER_SIZE를 따르며 이 파일의 매크로 값은 1이다.
