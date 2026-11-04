---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/ExtractTimeSeries_wgsl.md
lines: 29
sha256: 327f19e0ee2e7de221706934a666f54829445c3b76bc22c9453d8bd32ee83252
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ExtractTimeSeries_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/ExtractTimeSeries.wgsl`

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 원문 링크·설명이다(1–3). tooltip·시계열을 작은 회수 텍스처(texture)에 쓴다(1–7). 인덱스 `0`은 마우스 tooltip이며 비하천은 바닥/eta/유의·최대 파고/마찰, 하천은 바닥/eta/속력/마찰이다(11–14). 인덱스 `1..N`은 time·eta·x 운동량 `P`·y 운동량 `Q`다(16–21). |
| 23–29 | 전체 영역 대신 표본당 픽셀을 써서 `@workgroup_size(1, 1)`을 쓴다(25). `Time_Series.js`의 포장·회수·출력과 동기화해야 한다(29). 관측 변수를 추가하면 GPU packing과 CPU readback/export를 모두 바꿔야 한다(29). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
