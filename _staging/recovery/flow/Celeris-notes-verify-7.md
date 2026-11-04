# Celeris 노트 전수 대조 7

- 대상: `models/Celeris/manual-notes/celeris-configuration-differences.md`.
- 시작 시 전체 줄 수: 247줄.
- 담당 범위: 앞 절반인 1–124줄. 홀수 줄은 첫 몫에 포함한다.
- 마지막 대상 행: 124줄의 `docs-architecture:CD1-675`.
- 진행 상태: 완료. 담당 1–124줄을 모두 대조했다.
- 수정 직전에 대상 줄을 다시 읽는다. 줄 수는 유지한다.

## 노트별 결과

- 대조한 줄 수는 124줄이다. 시작 시 파일의 1–124줄을 셌다. Frontmatter와 빈 줄을 포함한다.
- 차이 표 대상은 100행이다. 25–27줄은 B 3행이다. 28–124줄은 C 97행이다.
- 정정 수는 97줄이다. 문서 원문 칸의 설명 표기를 97곳 고쳤다. 그중 41줄에서는 잘못된 코드 사용처 인용도 교체했다. 세부 정정은 98곳이다.
- 보완 수는 0줄이다. 기존 근거 위치를 바로잡은 변경은 정정으로 셌다.
- 결론 분류와 결론 문장의 의미는 100행 모두 최종 근거와 같다. `Bcoef` 식의 백틱은 표현 차이다.
- 수정한 97행의 결론 문장 칸 끝에 `[11-04 전수 검증 정정]`을 붙였다.
- 코드·문서 위치 바로 뒤의 인용 247개를 지정 원문의 문자열과 대조했다. 표의 `\|` 이스케이프와 인용 양끝 공백을 제외하고 대조했다. 문서 63줄의 발췌는 같은 줄의 문장과 일치한다.
- 뒤쪽 근거 목록의 선언값 발췌 97개를 각 행의 `js/constants_load_calc.js` 선언과 대조했다.
- 현재 판 원문 위치를 펼쳐 중복을 제거하면 6개 파일의 571줄이다. 경로만 적힌 인용의 지정 범위도 열었다.
- 이전 판 인용은 `984091f`와 `d41fbd8`의 해당 파일을 `git show`로 열어 대조했다.
- 담당 범위에 A 행, E 행, Mermaid, 논문 인용, 반영 전 노트 인용은 없다.
- 담당 범위의 상대 링크 1개는 실제 파일을 가리킨다. 절대 경로, `~/`, `[[`, 금지된 한계 문장은 없다.
- 담당 범위의 미해결 항목은 0개다.
- 모델 실행과 git 쓰기 명령은 사용하지 않았다.

## 줄별 대조 기록

| 노트 줄 | 대조 대상 | 근거와 판정 |
|---|---|---|
| 1, 13 | Frontmatter 구분자 | YAML 시작·끝 구분자로 유지했다. |
| 2–4 | 제목·모델·canonical_source | Celeris 설정 차이 표의 실제 내용과 일치한다. |
| 5–11 | 검증 상태·검증자·작성자·날짜 | `Celeris-notes-apply-5.md`의 새 파일 작성·보고서 반영 기록 및 `CONVENTIONS.md` §2와 대조했다. 작성·반영 기록을 이번 작업의 실행 검증으로 바꾸지 않았다. |
| 12 | source_scope | 문서 원문은 CONFIGURATION.md다. 코드 원문은 js와 index.html이다. 실제 인용 경로와 일치한다. |
| 14, 16, 18, 20, 22 | 빈 줄 | 문단·표 경계로 유지했다. |
| 15 | 상대 링크 | `celeris-architecture-and-config.md`가 노트 디렉터리에 존재한다. |
| 17 | 표 절 제목 | 문서·코드 대조 내용과 일치한다. |
| 19 | 비교 판 | `Celeris-version-verify-AD1.md:29` 및 `Celeris-version-verify-AD2.md`의 현재 판 기록과 일치한다. 사용자 지정 현재 판은 ebca435다. |
| 21 | 원문 경로 기준 | 실제 원문 디렉터리와 일치한다. |
| 23–24 | 표 머리·구분선 | 여섯 열의 의미와 구분선이 맞는다. |
| 25 · CD1-227 | Courant | 최종 분류 B와 결론이 CD1b의 같은 ID와 일치한다. 현재 CONFIGURATION.md:26, constants_load_calc.js:31,484–486, main.js:4652–4657,4675, index.html:1400을 대조했다. 984091f의 문서:23·상수:27과 d41fbd8의 상수:31도 대조했다. 미지 키 병합 뒤 시간간격은 Courant_num을 읽는다. 유지했다. |
| 26 · CD1-241 | gravity | 최종 분류 B와 결론이 CD1b의 같은 ID와 일치한다. 현재 문서:37, 상수:42,46–47,484–493과 984091f 문서:34·상수:38 및 d41fbd8 상수:42를 대조했다. 현재 js의 잘못된 세 키 직접 참조와 gravity UI 매핑은 검색 결과가 없다. 유지했다. |
| 27 · CD1-288 | 중첩 출력 표본 상한 | 최종 분류 B와 결론이 CD1b의 같은 ID와 일치한다. 현재 문서:59–63, main.js:1940–1989,2008–2036을 대조했다. d41fbd8 문서:63 및 main.js:1959,1999,2022–2026도 대조했다. 상한 식·초과 조건·dt 조정식·경고가 일치한다. 유지했다. |
| 28–124 · CD1-579–675 | 선언 기본값 97행 | 각 행의 분류·결론을 최종 TSV 및 CD1d의 같은 ID와 대조했다. 현재 CONFIGURATION.md:1–105에는 이 선언 기본값 문장이 없다. 각 선언 수치·부호·빈 문자열은 상수 원문과 일치한다. 행별 변경과 선언 원문은 다음 표에 모두 기록한다. |

## 정정 목록

아래 표의 노트는 모두 `models/Celeris/manual-notes/celeris-configuration-differences.md`다. 줄 번호는 시작 시와 수정 후가 같다.

각 행의 전 표기는 문서 원문 칸에 백틱으로 감싼 `docs/architecture/CONFIGURATION.md:기본값 누락`과 백틱으로 감싼 변수별 설명이다. 후 표기는 실제 범위 `docs/architecture/CONFIGURATION.md:1–105` 뒤에 인용이 아닌 설명을 적는다. 아래 표는 변수별 설명의 전·후를 빠짐없이 적는다.

공통 문서 근거는 CONFIGURATION.md 전체 1–105줄이다. 3줄의 원문은 ``Example `config.json` files override the defaults.``이다. 21–49줄과 67–70줄은 설정 키를 열거한다. 해당 선언 기본값 문장은 없다. 최종 근거 `Celeris-conclusion-verify-CD1d.md`는 각 ID를 C로 판정한다. 표의 코드 원문은 선언값을 뒷받침한다.

| 노트 줄·행 ID | 전: 인용처럼 표시한 설명 | 후: 일반 설명 | 근거 원문 |
|---|---|---|---|
| 28 · CD1-579 | `algochanges의 기본값` | algochanges의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:16` `algochanges: 0,` |
| 29 · CD1-580 | `grid_type의 기본값` | grid_type의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:20` `grid_type: 1,` |
| 30 · CD1-581 | `WIDTH의 기본값` | WIDTH의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:23` `WIDTH: 800,` |
| 31 · CD1-582 | `HEIGHT의 기본값` | HEIGHT의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:24` `HEIGHT: 600,` |
| 32 · CD1-583 | `dx의 기본값` | dx의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:27` `dx: 1.0,` |
| 33 · CD1-584 | `dy의 기본값` | dy의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:28` `dy: 1.0,` |
| 34 · CD1-585 | `Courant_num의 기본값` | Courant_num의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:31` `Courant_num: 0.15,` |
| 35 · CD1-586 | `timeScheme의 기본값` | timeScheme의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:32` `timeScheme: 2,` |
| 36 · CD1-587 | `pred_or_corrector의 기본값` | pred_or_corrector의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:33` `pred_or_corrector: 1,` |
| 37 · CD1-588 | `NLSW_or_Bous의 기본값` | NLSW_or_Bous의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:36` `NLSW_or_Bous: 0,` |
| 38 · CD1-589 | `Bcoef의 기본값` | Bcoef의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:37` `Bcoef: 1.0 / 15.0,` |
| 39 · CD1-590 | `Bous_alpha의 기본값` | Bous_alpha의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:38` `Bous_alpha: -0.531,` |
| 40 · CD1-591 | `Accuracy_mode의 기본값` | Accuracy_mode의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:39` `Accuracy_mode: 0,` |
| 41 · CD1-592 | `g의 기본값` | g의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:42` `g: 9.80665,` |
| 42 · CD1-593 | `seaLevel의 기본값` | seaLevel의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:43` `seaLevel: 0.0,` |
| 43 · CD1-594 | `base_depth의 기본값` | base_depth의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:44` `base_depth: 20.0,` |
| 44 · CD1-595 | `Theta의 기본값` | Theta의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:45` `Theta: 2.0,` |
| 45 · CD1-596 | `friction의 기본값` | friction의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:46` `friction: 0.000,` |
| 46 · CD1-597 | `isManning의 기본값` | isManning의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:47` `isManning: 0,` |
| 47 · CD1-598 | `vort_friction_factor의 기본값` | vort_friction_factor의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:48` `vort_friction_factor: 0.0,` |
| 48 · CD1-599 | `loadFriction의 기본값` | loadFriction의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:49` `loadFriction: 0,` |
| 49 · CD1-600 | `loadetaIC의 기본값` | loadetaIC의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:50` `loadetaIC: 0,` |
| 50 · CD1-601 | `min_allowable_depth의 기본값` | min_allowable_depth의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:51` `min_allowable_depth: 0.005,` |
| 51 · CD1-602 | `R_earth의 기본값` | R_earth의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:53` `R_earth: 6371000.0,` |
| 52 · CD1-603 | `useBreakingModel의 기본값` | useBreakingModel의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:56` `useBreakingModel: 1,` |
| 53 · CD1-604 | `delta_breaking의 기본값` | delta_breaking의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:57` `delta_breaking: 2.0,` |
| 54 · CD1-605 | `T_star_coef의 기본값` | T_star_coef의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:58` `T_star_coef: 5.0,` |
| 55 · CD1-606 | `dzdt_I_coef의 기본값` | dzdt_I_coef의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:59` `dzdt_I_coef: 0.50,` |
| 56 · CD1-607 | `dzdt_F_coef의 기본값` | dzdt_F_coef의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:60` `dzdt_F_coef: 0.15,` |
| 57 · CD1-608 | `west_boundary_type의 기본값` | west_boundary_type의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:63` `west_boundary_type: 0,` |
| 58 · CD1-609 | `east_boundary_type의 기본값` | east_boundary_type의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:64` `east_boundary_type: 0,` |
| 59 · CD1-610 | `south_boundary_type의 기본값` | south_boundary_type의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:65` `south_boundary_type: 0,` |
| 60 · CD1-611 | `north_boundary_type의 기본값` | north_boundary_type의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:66` `north_boundary_type: 0,` |
| 61 · CD1-612 | `BoundaryWidth의 기본값` | BoundaryWidth의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:67` `BoundaryWidth: 20,` |
| 62 · CD1-613 | `incident_wave_type의 기본값` | incident_wave_type의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:68` `incident_wave_type: -1,` |
| 63 · CD1-614 | `amplitude의 기본값` | amplitude의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:71` `amplitude: 0.0,` |
| 64 · CD1-615 | `period의 기본값` | period의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:72` `period: 10.0,` |
| 65 · CD1-616 | `direction의 기본값` | direction의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:73` `direction: 0.0,` |
| 66 · CD1-617 | `rand_phase의 기본값` | rand_phase의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:74` `rand_phase: 0.0,` |
| 67 · CD1-618 | `incident_wave_H의 기본값` | incident_wave_H의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:77` `incident_wave_H: 1.,` |
| 68 · CD1-619 | `incident_wave_T의 기본값` | incident_wave_T의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:78` `incident_wave_T: 10.,` |
| 69 · CD1-620 | `incident_wave_direction의 기본값` | incident_wave_direction의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:79` `incident_wave_direction: 0.,` |
| 70 · CD1-621 | `numberOfWaves의 기본값` | numberOfWaves의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:80` `numberOfWaves: 1.,` |
| 71 · CD1-622 | `trough_factor의 기본값` | trough_factor의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:81` `trough_factor: 1.0,` |
| 72 · CD1-623 | `ts_west_file의 기본값` | ts_west_file의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:84` `ts_west_file: "",` |
| 73 · CD1-624 | `ts_east_file의 기본값` | ts_east_file의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:85` `ts_east_file: "",` |
| 74 · CD1-625 | `ts_south_file의 기본값` | ts_south_file의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:86` `ts_south_file: "",` |
| 75 · CD1-626 | `ts_north_file의 기본값` | ts_north_file의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:87` `ts_north_file: "",` |
| 76 · CD1-627 | `ts_west_num_points의 기본값` | ts_west_num_points의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:88` `ts_west_num_points: 0,` |
| 77 · CD1-628 | `ts_east_num_points의 기본값` | ts_east_num_points의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:89` `ts_east_num_points: 0,` |
| 78 · CD1-629 | `ts_south_num_points의 기본값` | ts_south_num_points의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:90` `ts_south_num_points: 0,` |
| 79 · CD1-630 | `ts_north_num_points의 기본값` | ts_north_num_points의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:91` `ts_north_num_points: 0,` |
| 80 · CD1-631 | `start_time_shift의 기본값` | start_time_shift의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:93` `start_time_shift: 0.0,` |
| 81 · CD1-632 | `ship_posx의 기본값` | ship_posx의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:98` `ship_posx: -100.0,` |
| 82 · CD1-633 | `ship_posy의 기본값` | ship_posy의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:99` `ship_posy: 450.0,` |
| 83 · CD1-634 | `ship_width의 기본값` | ship_width의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:100` `ship_width: 10.0,` |
| 84 · CD1-635 | `ship_length의 기본값` | ship_length의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:101` `ship_length: 30.0,` |
| 85 · CD1-636 | `ship_draft의 기본값` | ship_draft의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:102` `ship_draft: 2.0,` |
| 86 · CD1-637 | `ship_heading의 기본값` | ship_heading의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:103` `ship_heading: 0.0,` |
| 87 · CD1-638 | `useSedTransModel의 기본값` | useSedTransModel의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:106` `useSedTransModel: 0,` |
| 88 · CD1-639 | `sedC1_d50의 기본값` | sedC1_d50의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:107` `sedC1_d50: 0.2,` |
| 89 · CD1-640 | `sedC1_n의 기본값` | sedC1_n의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:108` `sedC1_n: 0.40,` |
| 90 · CD1-641 | `sedC1_psi의 기본값` | sedC1_psi의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:109` `sedC1_psi: 0.00005,` |
| 91 · CD1-642 | `sedC1_criticalshields의 기본값` | sedC1_criticalshields의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:110` `sedC1_criticalshields: 0.045,` |
| 92 · CD1-643 | `sedC1_denrat의 기본값` | sedC1_denrat의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:111` `sedC1_denrat: 2.65,` |
| 93 · CD1-644 | `sedTurbDispersion의 기본값` | sedTurbDispersion의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:112` `sedTurbDispersion: 0.01,` |
| 94 · CD1-645 | `sedBreakingDispersionCoef의 기본값` | sedBreakingDispersionCoef의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:113` `sedBreakingDispersionCoef: 0.1,` |
| 95 · CD1-646 | `loadHardBottom의 기본값` | loadHardBottom의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:114` `loadHardBottom: 0,` |
| 96 · CD1-647 | `river_sim의 기본값` | river_sim의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:117` `river_sim: 0,` |
| 97 · CD1-648 | `river_inflow_angle의 기본값` | river_inflow_angle의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:118` `river_inflow_angle: 0.0,` |
| 98 · CD1-649 | `mean_upstream_channel_elevation의 기본값` | mean_upstream_channel_elevation의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:119` `mean_upstream_channel_elevation: 0.0,` |
| 99 · CD1-650 | `channel_bottom_width의 기본값` | channel_bottom_width의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:120` `channel_bottom_width: 1.0,` |
| 100 · CD1-651 | `channel_side_slope의 기본값` | channel_side_slope의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:121` `channel_side_slope: 1.0,` |
| 101 · CD1-652 | `channel_bank_start_upstream의 기본값` | channel_bank_start_upstream의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:122` `channel_bank_start_upstream: 0.0,` |
| 102 · CD1-653 | `channel_bank_end_upstream의 기본값` | channel_bank_end_upstream의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:123` `channel_bank_end_upstream: 0.0,` |
| 103 · CD1-654 | `Q_10의 기본값` | Q_10의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:125` `Q_10: 0.0,` |
| 104 · CD1-655 | `Q_50의 기본값` | Q_50의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:126` `Q_50: 0.0,` |
| 105 · CD1-656 | `Q_100의 기본값` | Q_100의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:127` `Q_100: 0.0,` |
| 106 · CD1-657 | `Q_200의 기본값` | Q_200의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:128` `Q_200: 0.0,` |
| 107 · CD1-658 | `Q_500의 기본값` | Q_500의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:129` `Q_500: 0.0,` |
| 108 · CD1-659 | `stage_10의 기본값` | stage_10의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:130` `stage_10: 0.0,` |
| 109 · CD1-660 | `stage_50의 기본값` | stage_50의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:131` `stage_50: 0.0,` |
| 110 · CD1-661 | `stage_100의 기본값` | stage_100의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:132` `stage_100: 0.0,` |
| 111 · CD1-662 | `stage_200의 기본값` | stage_200의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:133` `stage_200: 0.0,` |
| 112 · CD1-663 | `stage_500의 기본값` | stage_500의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:134` `stage_500: 0.0,` |
| 113 · CD1-664 | `add_Disturbance의 기본값` | add_Disturbance의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:137` `add_Disturbance: -1,` |
| 114 · CD1-665 | `disturbanceType의 기본값` | disturbanceType의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:138` `disturbanceType: 1,` |
| 115 · CD1-666 | `disturbanceXpos의 기본값` | disturbanceXpos의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:139` `disturbanceXpos: 0.0,` |
| 116 · CD1-667 | `disturbanceYpos의 기본값` | disturbanceYpos의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:140` `disturbanceYpos: 0.0,` |
| 117 · CD1-668 | `disturbanceCrestamp의 기본값` | disturbanceCrestamp의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:141` `disturbanceCrestamp: 0.0,` |
| 118 · CD1-669 | `disturbanceDir의 기본값` | disturbanceDir의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:142` `disturbanceDir: 0.0,` |
| 119 · CD1-670 | `disturbanceWidth의 기본값` | disturbanceWidth의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:143` `disturbanceWidth: 0.0,` |
| 120 · CD1-671 | `disturbanceLength의 기본값` | disturbanceLength의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:144` `disturbanceLength: 0.0,` |
| 121 · CD1-672 | `disturbanceDip의 기본값` | disturbanceDip의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:145` `disturbanceDip: 0.0,` |
| 122 · CD1-673 | `disturbanceRake의 기본값` | disturbanceRake의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:146` `disturbanceRake: 0.0,` |
| 123 · CD1-674 | `disturbance_change_timescale의 기본값` | disturbance_change_timescale의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:147` `disturbance_change_timescale: 0.0,` |
| 124 · CD1-675 | `disturbance_time_shift의 기본값` | disturbance_time_shift의 선언 기본값(문서에 해당 문장 없음). | `js/constants_load_calc.js:148` `disturbance_time_shift: 0.0,` |

41줄의 CD1-592에는 같은 줄에서 두 번째 정정도 적용했다.

- 전: `js/main.js:833` 뒤의 `const explorerCameraScaleX = calc_constants.grid_type == 2 ? Math.max(calc_constants.R_earth, 1.0) * explorerCameraCosLat * explorerCameraDegToRad : 1.0;`.
- 후: `js/main.js:1093` 뒤의 `Pass3_view.setFloat32(48, calc_constants.g, true);           // f32`.
- 근거: 현재 main.js:833은 grid_type·R_earth를 사용하는 카메라 식이다. 현재 main.js:1093은 g를 Pass3 uniform에 기록한다.
- 최종 근거: `Celeris-conclusion-verify-CD1d.md:86`의 CD1-592는 이 교체를 명시한다. g 기본값과 C 분류는 유지한다.

## 기계 확인 후보 판정

사용자 목록의 후보는 58개다. 담당 1–124줄에 49개가 있다. 후반 담당 범위에 9개가 있다. 각 후보에 대해 상수 파일의 해당 줄을 열었다.

모든 후보의 `CONFIGURATION.md:1` 귀속은 오탐이다. 노트는 문서 범위 `1–105`를 제시한 뒤 별도 코드 발췌를 이어 적었다. 같은 표 행 앞부분에 상수 파일 위치와 직접 인용이 있다. 선언값 발췌 자체는 해당 코드와 일치한다. 담당 행의 문서 원문 칸에 있던 설명의 백틱은 별도의 실제 오류이므로 위 정정 목록대로 고쳤다.

후반 9개는 기계 후보의 인용 귀속만 판정했다. 이 9개 행 전체의 검증과 수정은 두 번째 몫이다.

| 노트 줄 | 기계 후보 | 원문 위치·문자열 | 판정 |
|---|---|---|---|
| 28 | `algochanges: 0,` | `js/constants_load_calc.js:16` `algochanges: 0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 29 | `grid_type: 1,` | `js/constants_load_calc.js:20` `grid_type: 1,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 30 | `WIDTH: 800,` | `js/constants_load_calc.js:23` `WIDTH: 800,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 31 | `HEIGHT: 600,` | `js/constants_load_calc.js:24` `HEIGHT: 600,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 32 | `dx: 1.0,` | `js/constants_load_calc.js:27` `dx: 1.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 33 | `dy: 1.0,` | `js/constants_load_calc.js:28` `dy: 1.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 35 | `timeScheme: 2,` | `js/constants_load_calc.js:32` `timeScheme: 2,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 36 | `pred_or_corrector: 1,` | `js/constants_load_calc.js:33` `pred_or_corrector: 1,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 38 | `Bcoef: 1.0 / 15.0,` | `js/constants_load_calc.js:37` `Bcoef: 1.0 / 15.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 39 | `Bous_alpha: -0.531,` | `js/constants_load_calc.js:38` `Bous_alpha: -0.531,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 40 | `Accuracy_mode: 0,` | `js/constants_load_calc.js:39` `Accuracy_mode: 0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 41 | `g: 9.80665,` | `js/constants_load_calc.js:42` `g: 9.80665,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 42 | `seaLevel: 0.0,` | `js/constants_load_calc.js:43` `seaLevel: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 43 | `base_depth: 20.0,` | `js/constants_load_calc.js:44` `base_depth: 20.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 47 | `vort_friction_factor: 0.0,` | `js/constants_load_calc.js:48` `vort_friction_factor: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 48 | `loadFriction: 0,` | `js/constants_load_calc.js:49` `loadFriction: 0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 49 | `loadetaIC: 0,` | `js/constants_load_calc.js:50` `loadetaIC: 0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 51 | `R_earth: 6371000.0,` | `js/constants_load_calc.js:53` `R_earth: 6371000.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 61 | `BoundaryWidth: 20,` | `js/constants_load_calc.js:67` `BoundaryWidth: 20,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 70 | `numberOfWaves: 1.,` | `js/constants_load_calc.js:80` `numberOfWaves: 1.,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 71 | `trough_factor: 1.0,` | `js/constants_load_calc.js:81` `trough_factor: 1.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 76 | `ts_west_num_points: 0,` | `js/constants_load_calc.js:88` `ts_west_num_points: 0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 77 | `ts_east_num_points: 0,` | `js/constants_load_calc.js:89` `ts_east_num_points: 0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 78 | `ts_south_num_points: 0,` | `js/constants_load_calc.js:90` `ts_south_num_points: 0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 79 | `ts_north_num_points: 0,` | `js/constants_load_calc.js:91` `ts_north_num_points: 0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 80 | `start_time_shift: 0.0,` | `js/constants_load_calc.js:93` `start_time_shift: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 93 | `sedTurbDispersion: 0.01,` | `js/constants_load_calc.js:112` `sedTurbDispersion: 0.01,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 94 | `sedBreakingDispersionCoef: 0.1,` | `js/constants_load_calc.js:113` `sedBreakingDispersionCoef: 0.1,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 95 | `loadHardBottom: 0,` | `js/constants_load_calc.js:114` `loadHardBottom: 0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 96 | `river_sim: 0,` | `js/constants_load_calc.js:117` `river_sim: 0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 97 | `river_inflow_angle: 0.0,` | `js/constants_load_calc.js:118` `river_inflow_angle: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 98 | `mean_upstream_channel_elevation: 0.0,` | `js/constants_load_calc.js:119` `mean_upstream_channel_elevation: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 99 | `channel_bottom_width: 1.0,` | `js/constants_load_calc.js:120` `channel_bottom_width: 1.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 100 | `channel_side_slope: 1.0,` | `js/constants_load_calc.js:121` `channel_side_slope: 1.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 101 | `channel_bank_start_upstream: 0.0,` | `js/constants_load_calc.js:122` `channel_bank_start_upstream: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 102 | `channel_bank_end_upstream: 0.0,` | `js/constants_load_calc.js:123` `channel_bank_end_upstream: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 103 | `Q_10: 0.0,` | `js/constants_load_calc.js:125` `Q_10: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 104 | `Q_50: 0.0,` | `js/constants_load_calc.js:126` `Q_50: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 105 | `Q_100: 0.0,` | `js/constants_load_calc.js:127` `Q_100: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 106 | `Q_200: 0.0,` | `js/constants_load_calc.js:128` `Q_200: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 107 | `Q_500: 0.0,` | `js/constants_load_calc.js:129` `Q_500: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 108 | `stage_10: 0.0,` | `js/constants_load_calc.js:130` `stage_10: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 109 | `stage_50: 0.0,` | `js/constants_load_calc.js:131` `stage_50: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 110 | `stage_100: 0.0,` | `js/constants_load_calc.js:132` `stage_100: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 111 | `stage_200: 0.0,` | `js/constants_load_calc.js:133` `stage_200: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 112 | `stage_500: 0.0,` | `js/constants_load_calc.js:134` `stage_500: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 113 | `add_Disturbance: -1,` | `js/constants_load_calc.js:137` `add_Disturbance: -1,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 123 | `disturbance_change_timescale: 0.0,` | `js/constants_load_calc.js:147` `disturbance_change_timescale: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 124 | `disturbance_time_shift: 0.0,` | `js/constants_load_calc.js:148` `disturbance_time_shift: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 문서 설명 표기를 정정했다. |
| 125 | `disturbance_max_distance: 0.0,` | `js/constants_load_calc.js:149` `disturbance_max_distance: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 후반 담당 범위다. |
| 126 | `disturbance_initial_traj: 0.0,` | `js/constants_load_calc.js:150` `disturbance_initial_traj: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 후반 담당 범위다. |
| 127 | `disturbance_traj_timefactor: 0.0,` | `js/constants_load_calc.js:151` `disturbance_traj_timefactor: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 후반 담당 범위다. |
| 128 | `disturbance_final_traj: 0.0,` | `js/constants_load_calc.js:152` `disturbance_final_traj: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 후반 담당 범위다. |
| 129 | `disturbance_expo: 0.0,` | `js/constants_load_calc.js:153` `disturbance_expo: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 후반 담당 범위다. |
| 130 | `disturbance_vol_data: 0.0,` | `js/constants_load_calc.js:154` `disturbance_vol_data: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 후반 담당 범위다. |
| 131 | `disturbance_gamma_val: 0.0,` | `js/constants_load_calc.js:155` `disturbance_gamma_val: 0.0,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 후반 담당 범위다. |
| 133 | `exampleDirs: [` | `js/constants_load_calc.js:159` `exampleDirs: [` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 후반 담당 범위다. |
| 135 | `dissipation_threshold: 0.2,` | `js/constants_load_calc.js:224` `dissipation_threshold: 0.2,` | 문서 1줄 인용으로 귀속한 오탐이다. 코드 발췌는 일치한다. 후반 담당 범위다. |

## 최종 확인

- 각 노트 패치는 한 파일의 한 줄로 적용했다. 각 패치 직전에 해당 줄을 다시 읽었다.
- 동시 편집 중 정정이 되돌아간 8줄은 현재 줄을 다시 확인한 뒤 재적용했다.
- 최종 파일의 1–124줄을 시작 시 원문과 예정 정정 97줄에 다시 대조했다. 누락되거나 예상과 다른 줄은 0줄이다.
- 최종 파일의 전체 줄 수는 247줄이다. 담당 밖 노트 줄을 직접 수정하는 패치는 적용하지 않았다.
- 최종 표 100행의 여섯 열, 분류, 결론 문장과 정정 표시를 재검사했다. 불일치는 0개다.
- 이 기록의 정정 표는 97행이다. 기계 후보 판정 표는 58행이다. 두 표의 행 수를 직접 집계했다.
