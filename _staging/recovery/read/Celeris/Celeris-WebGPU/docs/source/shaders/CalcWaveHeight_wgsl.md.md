---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/CalcWaveHeight_wgsl.md
lines: 24
sha256: 8b5b99cfeea7288c4c60c8d32c53fb436b10bec42968b0a238ee5184dde63880
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# CalcWaveHeight_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/CalcWaveHeight.wgsl`

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 원문 링크·설명이다(1–3). 평균 eta에 대한 분산으로 파고 통계를 계산한다(1–7). 새 eta 편차제곱을 누적하고 RMS/평균 파고는 `sigma * 2.829`, 유의파고는 `sigma * 4.0`이다(11–14). 텍스처(texture)는 누적 분산·상대 변화·유의파고·평균/RMS를 저장한다(16). 활성 방법은 편차제곱 누적에서 표준편차를 계산한 뒤 파고를 추정한다(11). [11-04 전수 검증 보완] |
| 18–24 | 영점 상향 교차법은 주석이고 비활성이다(20). `n_time_steps_waveheight`로 나누므로 그 counter를 외부에서 초기화하는 동작에 의존하며 상대 변화는 이전 유의파고로 나누므로 초기값에서 의존하지 말라고 적는다(24). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20: 문서는 영점 상향 교차법을 비활성으로 구분한다.
- 24: 문서는 상대 변화 채널이 이전 유의파고로 나눈다고 적는다.
