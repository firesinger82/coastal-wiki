---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/TriDiag_PCRx_COULWAVE_wgsl.md
lines: 21
sha256: 7e85a9d92f7edbee17be0bb20e2b0ab5a5c123aa2b4b6f87a5e52914255baf7c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# TriDiag_PCRx_COULWAVE_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/TriDiag_PCRx_COULWAVE.wgsl`

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 원문 링크와 COULWAVE x방향 PCR 한 반복이다(1–7). alpha 채널 우변은 속도형이고 최종 반복은 국소 수심을 곱해 x 운동량으로 바꾸어 해를 쓴다. 중간 반복은 축소 계수만 쓴다(11). 표준 바인딩에 최종 변환용 `txBottom`의 바인딩 `6`을 더한다(15). |
| 17–21 | `globals.Px`로 마지막 반복을 검출하므로 JavaScript 반복 수 변경에 변환 시점이 영향받는다(19). `current_state`는 수면·그대로 둘 채널이 필요한 최종 반복 블록에서만 읽어 `txtemp2`에 쓴다(21). JavaScript 반복 수 논리가 바뀌면 최종 변환이 드러나지 않게 너무 이르거나 늦게 일어날 수 있다(19). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
