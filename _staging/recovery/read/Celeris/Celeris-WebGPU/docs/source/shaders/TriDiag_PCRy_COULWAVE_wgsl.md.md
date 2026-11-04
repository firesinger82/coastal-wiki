---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/TriDiag_PCRy_COULWAVE_wgsl.md
lines: 21
sha256: 1174bb3a007754f1d58ec0eadacd8468f122e5cf9b5f8c1bcbcaeed19fcc25f8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# TriDiag_PCRy_COULWAVE_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/TriDiag_PCRy_COULWAVE.wgsl`

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 원문 링크·설명이다(1–3). COULWAVE y방향 PCR 한 반복이다(1–7). 속도형 우변을 풀어 최종 반복에서 `txBottom`의 국소 수심으로 운동량으로 바꾼다. 중간 반복은 축소 계수만 쓰며 표준 배치에 바인딩 `6`의 `txBottom`을 더한다(11–15). |
| 17–21 | 최종 검출 `globals.Py`를 `Run_Tridiag_Solver.js`와 맞춰야 한다(19). `current_state`는 수면·유지 채널이 필요한 최종 블록에서만 읽어 `txtemp2`에 쓴다(21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
