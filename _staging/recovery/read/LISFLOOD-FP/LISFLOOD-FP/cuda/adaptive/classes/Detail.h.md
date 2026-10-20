---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/Detail.h
lines: 56
sha256: d14234bae08b55f5b35916bb00423d326848435ca372cf3b2b9ae3e73bcd1107
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# Detail.h — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1), SubDetail.h·Maxes.h 포함(3–4). 전처리 조건 분기는 없다. DetailHW는 SubDetailHW 형식의 eta·qx·qy·z를 보유한다(6–11). |
| 13–31 | 시작 시 6–7행 DetailHW 구조체 안. 장치 인라인(inline) 한정자 `__device__ __forceinline__` (13)와 get_norm_detail(Maxes maxes)(14–15). 초기값 `real norm_detail = C(0.0);` (16), 각 get_max()를 maxes로 나누는 정규화(normalization) 식 전체 `real eta_norm = eta.get_max() / maxes.eta;`<br>`real qx_norm  = qx.get_max()  / maxes.qx;`<br>`real qy_norm  = qy.get_max()  / maxes.qy;`<br>`real z_norm   = z.get_max()   / maxes.z;` (18–21), 네 값의 최댓값 누적 전체 `norm_detail = max(eta_norm, qx_norm);`<br>`norm_detail = max(qy_norm,  norm_detail);`<br>`norm_detail = max(z_norm,   norm_detail);` (23–25). norm_detail 반환·메서드·구조체 종료(27–30). |
| 32–56 | DetailMW는 SubDetailMW eta·qx·qy·z를 보유한다(32–37). `__device__ __forceinline__` (39)의 get_norm_detail(40–41)에서 초기값 `real norm_detail = C(0.0);` (42), 정규화 식 전체 `real eta_norm = eta.get_max() / maxes.eta;`<br>`real qx_norm  =  qx.get_max() / maxes.qx;`<br>`real qy_norm  =  qy.get_max() / maxes.qy;`<br>`real z_norm   =   z.get_max() / maxes.z;` (44–47), 최댓값 누적 전체 `norm_detail = max(eta_norm, qx_norm);`<br>`norm_detail = max(qy_norm,  norm_detail);`<br>`norm_detail = max(z_norm,   norm_detail);` (49–51). norm_detail 반환·종료(53–56). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–21·44–47: 두 get_norm_detail은 maxes.eta·qx·qy·z로 나눈다. 이 메서드들에는 분모가 0인지 확인하는 분기가 없다.
