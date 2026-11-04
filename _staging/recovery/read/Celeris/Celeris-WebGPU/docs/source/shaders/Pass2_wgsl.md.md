---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass2_wgsl.md
lines: 23
sha256: 0bff5d969a03095c7d93b11b29ff4add83780f1797e37596fee17acf0306fa74
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass2_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass2.wgsl`

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크·설명이다(1–3). `Pass2`는 면 수심·속도·스칼라에서 유한체적법(finite-volume) x/y 물 유량과 선택 퇴적물 유량을 계산한다(1–7). 동·북면 파속과 HLL형 식을 쓰며 채널은 질량·x 운동량·y 운동량·스칼라다(11). 동·북면에서 구하는 파속은 일차원 파속이다(11). [11-04 전수 검증 보완] |
| 13–23 | `txHnear`로 건조 한계 아래 이웃을 판별해 질량 차이를 억제하고 더 확산적인 제한을 적용한다(15). 조건 `useSedTransModel == 1`에서 `txSed_C1` through `txSed_C4`와 `txBreaking` 기반 `class-1` 난류/쇄파 분산을 쓴다(19). 모든 `Pass3`·퇴적물·쇄파·진단이 유량 의미에 의존한다(23). 건조 주변 처리는 건조 셀을 통한 불안정한 물 교환을 막기 위한 것이다(15). flux 채널 의미 변경은 물·퇴적물 적분·쇄파·진단에 전파해야 한다(23). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
