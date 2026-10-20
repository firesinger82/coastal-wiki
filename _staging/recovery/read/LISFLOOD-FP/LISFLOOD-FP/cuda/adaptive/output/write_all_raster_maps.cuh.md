---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_all_raster_maps.cuh
lines: 16
sha256: 4b3077e9ea8fa32c1496973cafa936d072365897fb99f2649f491e33684d34be
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_all_raster_maps.cuh — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–5 | `#pragma once`와 FV1·DG2 래스터 지도(raster map) 저장 헤더를 포함한다(1–4). 전처리 조건 분기는 없다. 원문: `#pragma once` (1). |
| 6–16 | `write_all_raster_maps` 원형을 선언한다(6–16). 출력 설정·조립 해·최세 x/y간격·모의/해석기 매개변수·저장 간격·첫 시간 단계 표시를 모두 상수 참조로 받는다(8–15). 기본 인수와 실행 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
