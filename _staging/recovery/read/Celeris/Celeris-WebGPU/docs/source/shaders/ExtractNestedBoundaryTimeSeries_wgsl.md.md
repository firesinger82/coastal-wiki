---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/ExtractNestedBoundaryTimeSeries_wgsl.md
lines: 24
sha256: 7b511f2556f78eabd5a94bedeb0245448a6e4ed7a904ff76dd8ed0b027254692
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ExtractNestedBoundaryTimeSeries_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/ExtractNestedBoundaryTimeSeries.wgsl`

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 원문 링크·설명이다(1–3). 승인된 상태의 사각형 `four edges`에서 `eta`, `hu`, `hv`를 추출해 단방향 중첩 경계형 `5`를 만든다. 건조 조건 `eta - bottom <= 0`은 모두 영값이다(1–7). `Four` `rgba32float` 저장 텍스처(texture)의 남/북 폭은 x 인덱스 수, 서/동은 y 인덱스 수, 높이는 표본 수다. 픽셀은 `[eta, hu, hv, 0]`, 건조는 `[0, 0, 0, 0]`다(11–16). 건조 판단을 위해 바닥고도 읽는다(7). 영값 출력은 eta 열에 DEM 고도가 들어가는 일을 막는다(16). [11-04 전수 검증 보완] |
| 18–24 | 실행은 `max(nx, ny)`의 한 차원이며 `station_index < nx`는 가로 면, `station_index < ny`는 세로 면을 쓴다(20). 시간은 저장하지 않고 JavaScript가 실제 표본 시간을 기록해 텍스트에 더한다(24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
