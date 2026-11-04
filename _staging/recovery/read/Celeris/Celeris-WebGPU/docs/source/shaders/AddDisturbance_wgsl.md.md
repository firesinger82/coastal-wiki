---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/AddDisturbance_wgsl.md
lines: 28
sha256: 90cd7b051c55ff3ff84dc45ec308c4479a1294a3e4380b316baff4a6018c3ce9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# AddDisturbance_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/AddDisturbance.wgsl`

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 원문 링크·설명이다(1–3). 현재 상태에 사용자/예제 교란을 더하고 이동 바닥에서는 바닥 변화·수심 변화 강제를 계산한다(1–7). 모드는 고립파 초기장·수중 산사태형 쌍극 수면·육상 산사태형 Gaussian 융기·시간 지정 수심 운동이다(9–16). 지진 분기는 주석/비활성이다(18). |
| 19–28 | 출력은 교란 물 상태, 이동 바닥 변화율·새 바닥의 `txBoundaryForcing`, 면/중심 지형의 임시 텍스처(texture)다(20–24). 이동 바닥 기준은 초기 바닥과 누적 퇴적물 변화이며 이후 near-dry·분산성(dispersive) 삼중대각 계수를 갱신해야 한다(28). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18: 문서는 지진 분기가 주석/비활성이라고 적는다.
