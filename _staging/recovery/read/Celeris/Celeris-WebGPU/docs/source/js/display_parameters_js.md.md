---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/display_parameters_js.md
lines: 27
sha256: 93fb92c127bf387a5a833442f577702b1a1718cdc55e0fc66a5a75d62ba563e7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# display_parameters_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/display_parameters.js`

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 원문 링크와 수치 모델을 직접 바꾸지 않는 DOM 상태·위치·부피·콘솔 표시 역할이다(1–7). `displayCalcConstants()`는 설정, `displaySimStatus()`는 단계/프레임/시간, `displayTimeSeriesLocations()`는 관측점, `displaySlideVolume()`는 교란 부피, `ConsoleLogRedirection()`은 `console.log`의 페이지 복제다(11–15). 경계형 `5`는 파일 시계열 강제로 표시한다(17). DOM 표시에는 sediment/design volume 정보도 포함된다(7). `displaySimStatus()`는 run-status도 갱신한다(12). `displayTimeSeriesLocations()`는 활성 관측점을 나열한다(13). [11-04 전수 검증 보완] |
| 19–27 | 특정 DOM ID·container·text field에 결합하며 콘솔 항목 수는 제한한다(21). `grid_type == 2`에서 `displayTimeSeriesLocations()`는 내부 좌하단 상대 offset에 `lon_LL`·`lat_LL`을 더해 절대 경위도를 표시한다(23). 모델 변경은 `calc_constants` 또는 `main.js`의 명시 플래그를 거쳐 프레임 루프가 GPU에 적용하도록 하라고 적는다(27). console 항목 수 제한은 페이지가 무한히 커지는 일을 막는다(21). 표시 전용 모듈이므로 simulation 부작용을 추가하지 말라고 안내한다(27). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
