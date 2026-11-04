# Celeris 노트 오늘 변경분 무작위 30줄 표본 검증 (11-04)

## 방법
- 대상: `git status --short models/Celeris`의 수정 13개 + 신규 5개.
- 후보 풀: 수정 노트는 `git diff -U0 HEAD`의 추가·변경 줄, 신규 노트는 frontmatter·빈 줄 제외 전 줄. 제목 줄(`#`)·표 머리·구분선은 제외했다.
- 추출: `random.seed(1104)`. 먼저 노트 12개에서 각 1줄을 뽑고, 나머지는 줄 수 x(대형 노트 6개 가중 3)로 가중 추출해 30줄을 채웠다. 결과는 노트 18개 중 17개에 걸친다(celeris-fv-reconstruction, celeris-source-map, celeris-webgpu-infrastructure, celeris-coulwave-theory 등은 뽑히지 않음).
- 줄 번호는 검증 시점(작업 중 다른 편집으로 줄 번호가 몇 줄 밀릴 수 있음) 기준이다.
- 확인한 것: 코드 인용문 일치(Celeris-WebGPU ebca435 및 과거 커밋), 최종 결론 문자(`Celeris-final-conclusions.tsv`, `Celeris-conclusion-verify-*.md`), 논문 쪽 이미지(Tavakkol 2017 p.3·6, 2020 p.1·6·7·9·10, Lynett 2026 p.3).
- 확인하지 않은 것: 긴 표 행의 모든 인용 줄(대표 줄만 대조), Lynett 2026 p.1·4 쪽 이미지, 모델 실행.

## 결과표

| # | 노트:줄 | 요지 | 판정 | 근거 원문 | 이유 |
|---|---|---|---|---|---|
| 1 | architecture-and-config:194 | 시간적분 계수 출처 = Tavakkol 2017 p.3 식 (15)–(20) | 맞음 | Tavakkol 2017 p.3 쪽 이미지 | 식 (15)–(20)이 AB3 예측·AM4 수정 식이다 |
| 2 | configuration-differences:107 | Q_500 선언 기본값 0.0 (CD1-658, C) | 맞음 | `js/constants_load_calc.js:129`, `js/main.js:1198`, 최종 결론 CD1-658=C | 인용문 일치, docs에 Q_500 없음, 문자 일치 |
| 3 | configuration-differences:206 | fileWritePause 기본값 100 (CD1-812, C) | 맞음 | `js/constants_load_calc.js:370`, `js/main.js:3729` | 일치 |
| 4 | docs-source-differences:19 | 코드=plynett.github.io main ebca435 (2026-07-20) | 맞음 | `git log -1` = ebca435 2026-07-20 | 일치, docs/·README 존재 |
| 5 | boussinesq-solver:125 | 운동량 방정식은 `(I + L)·U = U*` 꼴 tridiagonal | 부분 | Tavakkol 2017 p.3 식 (21)–(23) | 내용은 식 (21)–(23)과 맞다. 그러나 이 줄에 출처 인용이 없고 `(I+L)` 표기는 노트의 표기이다. 같은 줄에서 ADI류 문장을 빼며 수정한 줄이다 |
| 6 | boussinesq-solver:321 | CR/PCR 후진 대입 (CP1-044, A) | 맞음 | `shaders/TriDiag_PCRx.wgsl:89–92`, `js/Run_Tridiag_Solver.js:48–50`, `6f1272f:shaders/TriDiag_PCRx.wgsl:85–88`, Tavakkol 2017 p.3·p.6 Fig.4 | 논문은 CR에 후진 대입 단계가 있다고 쓰고, 현재 PCR은 r·aOut·cOut·dOut만 계산한다. 문자 A 일치 |
| 7 | breaking-boundary:261 | 지표 침투항 (CD1-948, C) | 맞음 | `shaders/Pass3_NLSW.wgsl:243–250` | `overflow_dry = -globals.infiltrationRate`, `dhdt + overflow_dry` 일치 |
| 8 | breaking-boundary:290 | dzdt_F_coef-input value 없음 (CD1-1232, C) | 맞음 | `index.html:1442` 외 4개 파일 | `min="0"`만 있고 value 없음 |
| 9 | breaking-boundary:293 | incident_wave_type 0 = `*Sine Wave` (CD1-1258, C) | 맞음 | `index_nots.html:723–724`, `MC_examples.html:696–697`, `transect_version/index.html:693–694` | 일치. `index.html`은 별표 없는 "Sine Wave"라 행 범위에서 제외된 것이 맞다 |
| 10 | breaking-boundary:302 | transient 파 수 4에서 5 (CD1-1400, A) | 맞음 | `shaders/BoundaryPass.wgsl:173–181`, `f6fd78b:…:155–160`, `bb99fee` diff | num_waves 4에서 5로 변경 확인, 날짜 2026-07-02 일치 |
| 11 | coulwave:72 | 층 0 txCW_uvhuhv = [u, v, u*d, v*d] | 맞음 | `shaders/Pass3A_COULWAVE.wgsl:39,80` | 코드는 `u_here*d_here`, d=-bottom.z. (`js/main.js:516`의 주석은 "du, dv"로 줄여 썼을 뿐) |
| 12 | pipeline-graph:178 | CalcMeans EncStack :2915, 항상 | 맞음 | `js/main.js:2915` | 해당 줄이 CalcMeans EncStack이고 같은 수준에서 무조건 실행 |
| 13 | render:153 | Fig. 4 = Base 타일 분리 구조도 (CP2-064, A) | 맞음 | Tavakkol 2020 p.7 Fig.4, `js/main.js:1695–1696` | 그림에 축·값 없음. 문자 A 일치. 단 렌더 메시 내용이라 범위 경계(아래 주의 참조) |
| 14 | sediment:199 | 바닥 변화 부호·경계 ramp (CD1-947, C) | 맞음 | `shaders/SedTrans_UpdateBottom.wgsl:78–92` | 인용문·주석 일치 |
| 15 | sediment:207 | 침강속도 초기화·UI 불일치 (CD1-1300, E 중간) | 맞음 | `js/constants_load_calc.js:622–633`, CD1h 검증 | 문자 E·강도 중간 일치, 인용문 일치 |
| 16 | sediment:221 | 퇴적물 확산은 표준 Pass2에 있고 Pass3 블록은 주석 (CD2-472, B) | 맞음 | `shaders/SedTrans_Pass3.wgsl:102–119`, `shaders/Pass2.wgsl:181–200`, `d8157c80:…celeris-sediment.md:102–104` | Pass3은 전부 주석, Pass2는 `k_east*...C1x_east` 확산 포함. 문자 B 일치 |
| 17 | transect-version:56 | Handler_SedTrans_Pass3.js CRLF (CT1-019, F) | 맞음 | `git show ebca435:js/Handler_SedTrans_Pass3.js` | 본판 CRLF 253, transect 0, 줄 수 254·189 일치 |
| 18 | transect-version:65 | display_parameters.js CRLF 218 (CT1-028, F) | 맞음 | 같은 방식 | CRLF 218, 범위 1–119·142–231·242–250 일치, 줄 수 251·228 일치 |
| 19 | transect-version:89 | vertex3D.wgsl CRLF 85 (CT1-052, F) | 맞음 | 같은 방식 | 85 / 0, 줄 수 86·85 일치 |
| 20 | transect-version:143 | 본판만 algochanges·grid_type (CT1-124, A) | 맞음 | `js/constants_load_calc.js:12–24`, transect 12–17 | 본판에만 두 항목 존재 확인 |
| 21 | transect-version:291 | 예측 단계 submit 묶음·total_time 차이 (CT1-301, A) | 맞음 | `js/main.js:2624`, `transect_version/js/main.js:1568`, 3646fc8·33f7ff6·bb99fee 줄 | total_time 식 두 판 차이, 쇄파 시각 `total_time - dt` 일치. 호출 순서 서술은 대표 줄만 확인 |
| 22 | webgpu-infrastructure-differences:165 | changethisTimeSeries 5 (CD1-1175, C) | 맞음 | `index.html:1058,1063` 등, `DATA_AND_TEXTURES.md:115` | 일치 |
| 23 | webgpu-infrastructure-differences:198 | write_P 0=No (CD1-1208, C) | 맞음 | `index.html:1274–1275`, `README.md:23` | 일치 |
| 24 | webgpu-infrastructure-differences:236 | surfaceToChange 4 = Water Surface Elevation (CD1-1282, C) | 맞음 | `river.html:642,646` | 일치 |
| 25 | webgpu-infrastructure-differences:288 | 셀 저장량 H·η (CP3-025, B) | 맞음 | Lynett 2026 p.3, `js/main.js:451` | 논문은 (H, Hu, Hv, HC), 코드 주석은 "eta, P, Q, c". 문자 B 일치 |
| 26 | webgpu-infrastructure-differences:320 | 부이 개수·삭제 (CP2-086, A) | 맞음 | Tavakkol 2020 p.9, `js/constants_load_calc.js:262`, `index.html:1023–1040` | "A maximum of five", Ctrl 삭제 문구 일치. UI 상한 15, slot 0 tooltip 확인 |
| 27 | webgpu-infrastructure-differences:330 | 동적 바닥 forcing·교란 (CP2-140, C) | 맞음 | `shaders/Pass3_Bous.wgsl:306`, `js/constants_load_calc.js:137–155`, Tavakkol 2020 p.6 | 인용문·설정 목록 일치 |
| 28 | lynett-2026:83 | 재구성·방정식 선택 (CD1-1357, C) | 맞음 | `js/main.js:1541,1548,1568,1570`, `constants_load_calc.js:36–39`, Lynett 2026 p.3 | 인용문 일치. "분산 미분은 2차 차분, 두 모드 동일"이 p.3에서 확인됨 |
| 29 | official-resources:58 | 2020 Base 계보 (CD1-431, A) | 맞음 | `docs/architecture/REFERENCE_PAPERS.md:29`, Tavakkol 2020 p.1 초록, `fd57bb7:shaders/Pass1.compute` | 초록 인용문 verbatim 일치 |
| 30 | papers-vs-code:23 | 코드 인용 기준 경로, AI 정리 표기 | 맞음 | 저장소 경로 존재 | 사실 진술 일치 |

## 집계 (표본 30줄)
- 맞음 29
- 부분 1 (5번)
- 틀림 0

## 부분 판정 사유
- 5번 boussinesq-solver:125: 내용은 Tavakkol 2017 식 (21)–(23)과 맞다. 줄 자체에 출처 인용이 없다. canonical 단언은 출처 필수(절대 규칙 1)이다.

## 표본 밖에서 발견한 문제
- `manual-notes/celeris-architecture-and-config.md:186`의 "구버전 호출문은 주석으로만 남아 있다(`js/main.js:2435,2448`)"는 최종 결론 CD1-1325(H, 코드 대조 대상 아님: 오버레이 바인딩 표시 전용)에 해당한다. H 행은 노트에 두지 않는 기준이므로 제거 대상 후보이다. 코드 인용 자체(2435, 2448 주석 처리)는 맞다.
- 범위 경계 주의: render:153(CP2-064, Fig.4)과 webgpu-infrastructure-differences의 HTML select 항목 행(CD1-1172·1208·1282 등)은 표시 계층에 가깝다. 최종 문자가 A·C로 확정되어 있어 이번에는 틀림으로 보지 않았다.
- 초기 추출 단계에서 같은 표의 인접 행 CP1-033(boussinesq-solver:317)도 검토했다. 결론 A와 식 (16) 인용은 맞다. 그러나 코드 원문 칸이 인용문이 아니라 "`:404`의 CP1-032 원문"이라는 다른 행 지시문이라 이 행만으로는 코드 근거를 확인할 수 없다(부분). 최종 30줄에는 들어가지 않았다.
