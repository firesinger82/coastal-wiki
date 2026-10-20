---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/hll.cpp
lines: 61
sha256: 156d4db89202a35364a23a6fca612efe9f7f0564a835941a7d89f40ae8d67401
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# hll.cpp — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 헤더 네 개(1–4) 뒤 `HLL_x`를 정의한다(6–22). HLL 리만 해법(Harten–Lax–van Leer Riemann solver)의 공통 함수에 양쪽 H·HU·HV와 세 출력 참조를 그대로 전달한다. 이 파일에는 조건부 전처리 분기가 없다. 원문: `HLL(Solverptr, H_neg, HU_neg, HV_neg, H_pos, HU_pos, HV_pos,` (20); `H_flux, HU_flux, HV_flux);` (21). |
| 24–42 | `HLL_y`는 공통 HLL에 법선 성분으로 HV, 접선 성분으로 −HU를 전달한다. 출력 HV_flux·HU_flux의 위치도 바꾼다. 반환 뒤 HU_flux 부호를 다시 뒤집는다. 원문: `HLL(Solverptr, H_neg, HV_neg, -HU_neg, H_pos, HV_pos, -HU_pos,` (38); `H_flux, HV_flux, HU_flux);` (39); `HU_flux = -HU_flux;` (40). |
| 43–61 | `HLL`은 Solver의 DepthThresh와 g를 지역 값으로 복사한다(57–58). 함수 본문 안에서 `hll_include.h`를 텍스트 포함하여 계산을 수행한다(60). 이 구간 자체에는 분기·수치식이 없다. 원문: `#include "hll_include.h"` (60). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60: 계산 본문은 함수 바깥의 별도 번역 단위가 아니라 HLL 함수 중괄호 안의 헤더 포함으로 들어온다.
