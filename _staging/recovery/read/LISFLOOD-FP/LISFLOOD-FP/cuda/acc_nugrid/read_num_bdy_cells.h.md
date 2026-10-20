---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/read_num_bdy_cells.h
lines: 26
sha256: 76315b22d2a5bde0897d0f2445cff413bc382bba6ff0343983d95664dae2736b
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_num_bdy_cells.h — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | `#pragma once` (1) 및 표준 입출력·표준 라이브러리·문자열·Directions·InletTypes·lisflood.h를 포함한다(3–8). lis::cuda::acc_nugrid 이름공간을 연다(10–15). 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 17–26 | int 반환 read_num_bdy_cells를 선언한다(17–22). const char* bcifilename, const Pars& pars, const int direction을 받는다(19–21). 기본 인수와 본문은 없다. 빈 줄과 세 이름공간 닫기를 포함한다(23–26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
