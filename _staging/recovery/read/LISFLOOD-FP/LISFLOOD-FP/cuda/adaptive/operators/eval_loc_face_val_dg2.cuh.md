---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/eval_loc_face_val_dg2.cuh
lines: 15
sha256: fb59db9c7efc5a901482dd5886e3aeac2fc3a5a157cef67a99c94a6f20e4562a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# eval_loc_face_val_dg2.cuh — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1) 뒤 FlowVector·PlanarCoefficients·LegendreBasis 형식 헤더를 포함한다(3–5). 조건부 전처리 분기는 없다. |
| 7–15 | `__host__ __device__ __forceinline__` (7)로 호스트(host)·장치(device) 양쪽의 인라인(inline) 함수 eval_loc_face_val_dg2를 정의한다(8–13). const PlanarCoefficients& s와 const LegendreBasis& basis를 받는다(10–11). `return s._0 * basis._0 + s._1x * basis._1x + s._1y * basis._1y;` (14)로 평면 계수(planar coefficient)와 르장드르 기저(Legendre basis)의 세 성분 내적을 반환한다. 함수 종료(15). 조건문·기본 인수는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
