---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Update_TriDiag_coef_COULWAVE_wgsl.md
lines: 26
sha256: 7544c189c7ec2d844ce9785e5083d1b2755034c24745343bad9242995f63d491
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Update_TriDiag_coef_COULWAVE_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Update_TriDiag_coef_COULWAVE.wgsl`

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 원문 링크·설명이다(1–3). 현재 수면·총수심·`Bous_alpha`·지형으로 COULWAVE x/y 암시 계수를 만든다(1–7). `coefMatx`·`coefMaty`의 `r/g/b/a`는 하대각/대각/상대각/속도형 우변이며 x는 `U/H`, y는 `V/H`다(11–16). 경계·near-dry는 항등형 행이다(18). 계수는 수직 좌표에 의존한다(7). [11-04 전수 검증 보완] |
| 20–26 | COULWAVE PCR은 속도형 해를 최종 수심 곱으로 운동량으로 바꾸며 표준 Boussinesq는 `current_stateUVstar` 운동량을 직접 받는다(22). alpha 의미는 변형별로 다르므로 `TriDiag_PCRx_COULWAVE.wgsl`·`TriDiag_PCRy_COULWAVE.wgsl`과 동기화해야 한다(26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
