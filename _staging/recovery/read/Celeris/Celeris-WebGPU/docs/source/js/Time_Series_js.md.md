---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Time_Series_js.md
lines: 22
sha256: 668bdd3dd3be2ce3c58544569928f9218026d3c59a4cfaa51bebfb9523109fad
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Time_Series_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Time_Series.js`

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 원문 링크와 `ExtractTimeSeries.wgsl` 표본의 GPU→CPU/UI 회수 역할이다(1–7). `readToolTipTextureData()`는 `txTimeSeries_Data`의 `NumberOfTimeSeries + 1` 픽셀을 읽으며 `Pixel 0`은 tooltip, 나머지는 time·eta·P·Q를 `timeSeriesData`에 추가한다(11). `resetTimeSeriesData()`는 초기화, `downloadTimeSeriesData()`는 다운로드, `readCornerPixelData()`는 구형 `8-bit` 모서리 유틸리티다(12–14). `readToolTipTextureData()`는 텍스처를 buffer로 복사한 뒤 첫 픽셀들부터 읽는다(11). `readCornerPixelData()`는 현재 흐름의 중심이 아니다(14). [11-04 전수 검증 보완] |
| 16–22 | `ExtractTimeSeries.wgsl`은 첫 픽셀을 현재 마우스 tooltip에 예약하고 관측은 인덱스 `1`에서 시작한다. `timeSeriesData`는 `constants_load_calc.js`에서 초기화한다. 일반 관측 시간은 최근 위치/변경/기간 초기화 이후 경과 시간이며 경계형 `5` 중첩 실행은 부모/전역 시계를 유지한다. 회수 결과는 reset epoch를 가져 초기화 전 비동기 결과가 빈 차트를 다시 채우지 않게 한다(18). 큰 출력은 `File_Writer.js`를 쓰라고 적는다(22). `timeSeriesData` 인덱스는 관측 slot과 일치한다(18). 이 경로는 소수 픽셀용이며 full-field용이 아니므로 readback 크기를 작게 유지하라고 안내한다(22). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
