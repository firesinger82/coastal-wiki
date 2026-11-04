---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_ExtractTimeSeries_js.md
lines: 27
sha256: c02bdc18aba2be0584d1a94bd8f573f3e8d88a32d3d244f864730a48a70b75a8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_ExtractTimeSeries_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_ExtractTimeSeries.js`

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크·역할 설명(1–7). `ExtractTimeSeries.wgsl`의 tooltip·관측값 표본용 바인드 그룹(bind group)을 만든다(7). |
| 9–27 | `0` 추출 uniform, `1` `txBottom`, `2` `txBottomFriction`, `3` `txContSource`, `4` `txState`, `5` `txWaveHeight`, `6` `txTimeSeries_Locations`, `7` 출력 `txTimeSeries_Data`, `8` `txMeans_Speed`다(11–19). 전체 격자 대신 작은 dispatch로 작은 텍스처(texture)를 쓰고 JavaScript가 회수해 tooltip·시계열 배열을 갱신한다(23). 출력 `Pixel 0`은 tooltip, 시계열은 `pixel 1`에서 시작하며 `Time_Series.js`와 맞춰야 한다(27). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
