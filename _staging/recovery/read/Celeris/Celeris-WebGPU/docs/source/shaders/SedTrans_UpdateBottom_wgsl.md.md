---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/SedTrans_UpdateBottom_wgsl.md
lines: 22
sha256: 40477da5af40f425271b548d6c000940eaed00a378587a4dbc8401bad7769faf
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# SedTrans_UpdateBottom_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/SedTrans_UpdateBottom.wgsl`

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 원문 링크와 침식·퇴적률 기반 지형 갱신이다(1–7). 침식에서 퇴적을 뺀 양을 공극률 보정으로 나누며 중심·동면·북면 변화로 `txBottom` 채널을 맞춘다(11). 입사파 경계 근처는 변화를 완화한다(13). 입사파 경계 근처 완화는 즉각적인 경계 artifact를 피하기 위한 것이다(13). [11-04 전수 검증 보완] |
| 15–22 | 출력 `txtemp_SedTrans_Botttom`은 새 바닥, `txtemp_SedTrans_Change`는 `txBottomInitial` 대비 누적 변화다(17–18). JavaScript 복사·`Update_neardry`·분산성(dispersive) 모드 계수 갱신이 뒤따르며 `Botttom`의 `three`개 `t` 철자를 보존하라고 적는다(22). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17·22: 문서는 바닥 출력 이름의 철자를 `txtemp_SedTrans_Botttom`으로 명시한다.
