---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass3A_COULWAVE_wgsl.md
lines: 29
sha256: bb45f9f9d5d5716895e2c2a13449fe4c9833c61a2e03c1f7acde2cd2da49eaf5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass3A_COULWAVE_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass3A_COULWAVE.wgsl`

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 원문 링크·설명이다(1–3). 첫 COULWAVE 보조 pass로 중심 평균 속도·총수심·수직좌표 보조항을 계산한다(1–7). 물 상태·지형·면속도 `txU`, `txV`를 읽는다(11–15). 출력 `txModelVelocities`는 평균 `u`, `v`, eta·총수심, `txCW_zalpha`는 `za`, `dzadx`, `dzady`, unused, `txCW_uvhuhv`는 `u`, `v`, `u*d`, `v*d`다(17–21). 이 보조항은 주 COULWAVE pass에 필요하다(7). [11-04 전수 검증 보완] |
| 23–29 | JavaScript가 재사용할 출력을 `3D` `txCW_groupings` 텍스처(texture) 층으로 복사한다(25). `za`는 `Bous_alpha`·국소 총수심에 결합하므로 변경 시 `Pass3B_COULWAVE`, `Pass3_COULWAVE`, COULWAVE 계수 셰이더를 함께 확인한다(29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
