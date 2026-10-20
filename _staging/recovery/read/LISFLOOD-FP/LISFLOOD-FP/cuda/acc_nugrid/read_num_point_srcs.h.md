---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/read_num_point_srcs.h
lines: 24
sha256: f9ea876f699c968b28e1de80aedea0c84c693ab5a87a22f8a2cd1560ed7ec880
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_num_point_srcs.h — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | `#pragma once` (1) 및 CUDA 유틸리티·표준 입출력·표준 라이브러리·문자열·PointSources·generate_morton_code 헤더를 포함한다(3–8). lis::cuda::acc_nugrid 이름공간을 연다(10–15). 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 17–24 | PointSources 반환 read_num_point_srcs를 선언한다(17–20). const char* bcifilename을 받는다(19). 기본 인수와 본문은 없다. 빈 줄과 세 이름공간 닫기를 포함한다(21–24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
