---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/read_bdy_conds.cuh
lines: 27
sha256: 210a122fd5958a1beb8ce23fb15c5650670da46a0850dfd66ff8c5463db6f73b
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_bdy_conds.cuh — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | `#pragma once` (1) 및 표준 입출력·표준 라이브러리·문자열·Boundary·gen_bdy_morton_codes·lisflood.h를 포함한다(3–8). lis::cuda::acc_nugrid 이름공간을 연다(10–15). 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 17–27 | void 반환 read_bdy_conds를 선언한다(17–23). 경계 조건(boundary condition) 파일명 const char*, 방향 const int, Boundary 참조 및 Pars 상수 참조를 받는다(19–22). 기본 인수와 본문은 없다. 빈 줄과 세 이름공간 닫기를 포함한다(24–27). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
