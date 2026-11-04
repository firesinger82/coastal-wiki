---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/constants_load_calc_js.md
lines: 44
sha256: 299e616adc4cc3bc9dbe4f7fd8b92d96616dcf033cf7eeabbf67dd1709d527e7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# constants_load_calc_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/constants_load_calc.js`

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 원문 링크와 기본 설정·파생 상수 역할이다(1–7). 내보내는 `calc_constants`는 평면 설정, `timeSeriesData`는 `up to 16 gauges`, `loadConfig()`는 예제 구성, `init_sim_parameters()`는 병합·파생 계산이다(9–12). 파생 상수는 시나리오 로드 또는 매개변수 편집 뒤 재계산한다(7). `timeSeriesData`는 CPU측 저장소다(10). [11-04 전수 검증 보완] |
| 14–25 | 설정은 격자·수치·물리·경계·파랑·퇴적물·설계·선형 구조·표시·출력이며 예제가 키별로 덮어쓴다(16). 경계형 `5`는 `eta/hu/hv`, `ts_west_file`, `ts_east_file`, `ts_south_file`, `ts_north_file`, 측면 관측점 수·`BoundaryPass`를 쓴다. 첫 공통 시간은 `start_time_shift`이며 `total_time`은 부모/전역 시계다. `timeSeriesChartStartTime`·`timeSeriesDataEpoch`는 차트 창·오래된 비동기 결과 배제를 맡는다(18). 기존 출력 키 `nestedGridOutput_i0/j0/i1/j1`, `nestedGridOutput_start_time`, `nestedGridOutput_end_time`, `nestedGridOutput_dt`는 호환된다. 선택 배열 `nestedGridOutput_rectangles`는 `i0`, `j0`, `i1`, `j1`, 시간·`eta_threshold`, `file_prefix`/`name`을 지정하며 없거나 활성 항목이 없으면 스칼라를 쓴다. `nestedGridOutput_max_samples`는 현재 `8192`이며 `dt` 증가·경고로 제한한다. `nestedEtaWriteThreshold`로 조용한 앞 표본을 자르고 사각형별 `eta_threshold`가 우선한다(20). 선형 구조의 단면·끝점·좌표·정의 플래그·preview·pending add를 같은 객체에 저장해 `MouseClickChange.wgsl`와 표시를 묶는다(22). 정식 스키마는 없고 `main.js` uniform·`shaders/`의 `Globals`에 결합한다(24). 중첩 출력 설정은 save-data 매개변수에 둔다(20). 배열 항목의 timing·`eta_threshold`·`file_prefix`/`name`은 선택 항목이다(20). 상한은 사각형마다 적용한다(20). 앞 표본 절단은 readback에서 사각형의 어느 가장자리든 eta 절댓값이 임계값을 처음 초과하는 시각을 찾는다(20). 선형 구조 상태에는 crest elevation·crest width·side slope·현재 끝점 선택·공유 x/y 입력·저장 시작/끝 좌표·각 끝점 정의 여부가 포함된다(22). pending add flag는 지형 편집을 dispatch한다(22). 정식 스키마 대신 이 파일이 사실상 스키마 역할을 한다(24). [11-04 전수 검증 보완] |
| 26–44 | `init_sim_parameters()`의 파생값은 시간 간격·`TWO_THETA`, dispatch, `Px`·`Py`, 역격자·고차 역수, Boussinesq/COULWAVE 계수, 경계 인덱스, 선박/교란, 침식·Shields·낙하속도, canvas·색상 막대·표시다(28–38). `grid_type == 2`에서 `dx`는 경도·`dy`는 위도 도 간격이며 `R_earth`, `lat_LL`·크기의 최소 구면 물리 간격으로 시간 간격을 정한다(30). 새 키는 JSON·UI·uniform·WGSL을 함께 확인하고 파생값은 다음 `html_update`에 덮어쓸 수 있다(42). `grid_type == 2`는 표준 NLSW로 제한해 `NLSW_or_Bous = 0`, `Accuracy_mode = 0`, `useSedTransModel = 0`, `useBreakingModel = 0`을 강제한다고 적는다(44). 파생값은 독립적인 사용자 입력으로 취급하면 안 된다(28). dispatch 수는 grid·workgroup 크기에서 계산한다(31). 경계 인덱스는 reflection/shift다(35). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24: 문서는 정식 설정 스키마가 없다고 적는다.
- 44: 문서는 구면 모드에서 네 설정값을 `0`으로 강제한다고 적는다.
