# Celeris 노트 전수 검증 11 — 2026-11-04

대상은 `models/Celeris/source-analysis/celeris-boussinesq-solver.md`이다.
검증 범위는 작업 시작 시 `git diff -U0 HEAD -- <대상 노트>`의 모든 추가 줄이다.
frontmatter와 빈 줄을 포함한다.
원문 코드는 Celeris-WebGPU `ebca435` 판을 기준으로 한다.
논문의 식·숫자·표는 제공된 쪽 이미지로 판정한다.
상태: 완료.

## 노트별 결과

| 노트 | 대조한 대상 줄 | 정정 줄 | 보완 줄 | 유지 줄 | 미해결 |
|---|---:|---:|---:|---:|---:|
| [celeris-boussinesq-solver.md](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md) | 133 | 35 | 4 | 94 | 0 |

줄 수는 작업 시작 시 읽기 전용 `git diff -U0 HEAD -- models/Celeris/source-analysis/celeris-boussinesq-solver.md`의 `+` 줄을 세었다.
133줄에는 frontmatter 2줄과 빈 줄 7줄이 포함된다.
정정·보완 수는 이번 작업에서 바꾼 서로 다른 노트 줄 수이다.
같은 줄의 여러 수정은 한 줄로 센다.
작업 전후 노트는 모두 343줄이다.
아래 노트 줄 번호는 작업 전후에 같다.

차이 표의 71행을 [최종 배정표](../assign/Celeris-final-conclusions.tsv) 및 행별 conclusion-verify 파일과 대조했다.
노트의 분류는 A 12행, B 12행, C 39행, E 3행, F 5행이다.
이 개수는 노트 273–343행의 결론 칸을 세었다.
모든 분류는 해당 conclusion-verify의 최종 분류와 같다.
E 3행의 강도는 모두 강함이다.
이 E 행들은 호출되는 본판 모드 1의 분산 계산 경로다.
본문의 CT1-358도 호출되는 transect 경로의 E 강함 판정과 같다.
이 대상에는 최종 근거가 호출되지 않는 경로로 판정한 E 행이 없다.

CD1-936의 결론 문장 중 `속도 크기`는 원문의 `sqrt(hu * hu + hv * hv)`에 맞춰 `단위 폭 유량 벡터의 크기`로 정정했다.
이 용어 오류는 conclusion-verify에도 있다.
원문의 `Pass3_NLSW.wgsl:181`은 상태의 두 유량 성분을 FrictionCalc에 넘긴다.
최종 분류 C는 유지했다.
이 용어 정정을 제외하면 표의 결론 문장은 최종 근거와 같다.
수식 표시용 백틱·달러 기호와 추가된 판 근거 문장은 결론 문장 비교에서 구분했다.

## 대상 줄 대조 범위

| 대상 줄 | 줄 수 | 대조한 내용·근거 |
|---|---:|---|
| 5–6 | 2 | frontmatter의 recovery 반영 날짜·방법을 notes-apply-8 및 최종 보고서와 대조했다. 기존 검증 정보와 반영 기록을 구분한 값이므로 유지했다. |
| 19–22 | 4 | Pass1·Pass2 역할과 계수 갱신 조건을 SIMULATION_PIPELINE:27,29 및 main:2641,2649,2702–2705,2832–2835,2884–2886과 대조했다. |
| 80–82 | 3 | 혼합 미분 구조, B와 α의 구별, F/G 출력과 이력을 Pass3_Bous:269–279,397,428, constants:37–38, main:2735–2736 및 CP1-141·160과 대조했다. |
| 93–98 | 6 | y 혼합 미분 계수·분모·도달 조건을 논문 2017 p.3 식 (11), Pass3_Bous:99–105,142–149,184–193,285 및 CP1-022·023·142와 대조했다. |
| 104–109 | 6 | 본판 합산과 transect의 Psi2x 누락을 두 Pass3_Bous 원문 및 CT1-358 최종 근거와 대조했다. 109행은 빈 줄이다. |
| 125–129 | 5 | 두 운동량 선형계와 각각의 우변을 논문 2017 p.3 식 (21)·(22), PCRx/y:70, Run_Tridiag_Solver:48–91 및 CP1-143과 대조했다. |
| 173–174 | 2 | PCR 소거·재정규화 설명을 PCRx:89–94 및 CP1-150 최종 판정과 대조했다. |
| 201 | 1 | AB3 예측·AM4 보정 명칭을 Pass3_Bous:399–410 및 논문 2017 p.3과 대조했다. |
| 218–237 | 20 | 초기 계수, UI·처방운동·퇴적물 갱신, 이력 이동, 예측·보정 시각, 보정 조건, 지연 입력을 main:648–649,2502–2564,2649–2897과 대조했다. RF-014·015·023, CP1-031·160, CP2-164, CP3-034–036 및 callflow §4·§6·Claude 렌더 확인 절을 함께 확인했다. |
| 260–266 | 7 | 요약의 역할·계수·독립 선형계·NLSW 복사를 main과 Run_Tridiag_Solver:37–91에 대조했다. 265–266행은 빈 줄이다. |
| 267–272 | 6 | 절 제목·표 머리·빈 줄·비교 판 정보를 확인했다. version-verify-AD1:29와 논문 첫 쪽의 서지를 대조했다. |
| 273–343 | 71 | 각 표 행의 분류·결론·문서 원문·현재 코드·과거 커밋 인용을 모두 대조했다. 아래 행별 근거 목록을 사용했다. |
| 합계 | 133 | 모든 대상 줄의 대조를 마쳤다. |

## 정정·보완 목록

아래 전·후 칸에는 바뀐 문장이나 표의 해당 칸을 적었다.
노트의 각 수정 줄 끝에 `[11-04 전수 검증 정정]` 또는 `[11-04 전수 검증 보완]`을 붙였다.
표 행의 표식은 결론 문장 칸 끝에 붙였다.
아래 근거의 코드 경로는 Celeris-WebGPU 아래 경로다.

| 노트 위치·종류 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| [노트:19](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L19) · 보완 | Pass1은 면 재구성이다 (`js/main.js:2641`). [11-04 대조 정정] | Pass1은 면 재구성이다 (`js/main.js:2641`; `docs/architecture/SIMULATION_PIPELINE.md:27`). [11-04 대조 정정] | ` docs/architecture/SIMULATION_PIPELINE.md:27 ` `` 2. `Pass1.wgsl` or `Pass1_HighOrder.wgsl` reconstructs face states from cell-centered state and bathymetry. It writes face depth, face velocity, and scalar values. `` |
| [노트:20](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L20) · 보완 | Pass2는 플럭스다 (`js/main.js:2649`). [11-04 대조 정정] | Pass2는 플럭스다 (`js/main.js:2649`; `docs/architecture/SIMULATION_PIPELINE.md:29`). [11-04 대조 정정] | ` docs/architecture/SIMULATION_PIPELINE.md:29 ` `` 4. `Pass2.wgsl`, `Pass2_HighOrder_HLLC.wgsl`, or `Pass2_HighOrder_HLLEM.wgsl` computes numerical fluxes through cell faces. The current high-order path selects HLLC. `` |
| [노트:82](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L82) · 정정 | `F_star`/`G_star`는 `F_G_star` 텍스처로 출력(`:397, 428`)되어 다음 step에서 `F_G_star_oldOldGradients`로 시간미분에 쓰인다. | `F_star`·`G_star`는 `F_G_star`에 출력된다 (`shaders/Pass3_Bous.wgsl:397,428`). 예측 뒤에는 기존 `F_G_star_oldGradients`를 `F_G_star_oldOldGradients`로 복사한다 (`js/main.js:2735`). 이어서 예측 결과 `predictedF_G_star`를 `F_G_star_oldGradients`로 복사한다 (`js/main.js:2736`). 각 분산 시간 미분은 현재 값과 저장된 `F_G_star_oldOldGradients` 값의 차를 `2dt`로 나눈다 (`shaders/Pass3_Bous.wgsl:212,283,286`). | ` js/main.js:2735 ` ` runCopyTextures_EncStack(commandEncoderStack, calc_constants, F_G_star_oldGradients, F_G_star_oldOldGradients) `<br>` js/main.js:2736 ` ` runCopyTextures_EncStack(commandEncoderStack, calc_constants, predictedF_G_star, F_G_star_oldGradients) `<br>`shaders/Pass3_Bous.wgsl:212` `let F_G_star_oldOldies = textureLoad(F_G_star_oldOldGradients, idx, 0).xyz;`<br>`:283,286`의 시간 차분은 `/ globals.dt * 0.5`이다. |
| [노트:228](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L228) · 정정 | 현재 호스트는 보정을 한 번 호출한다 (`js/main.js:2757–2865`; [CP3-034–036 최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)). [11-04 대조 정정] | 현재 호스트는 `if (calc_constants.timeScheme == 2)`에서 보정을 한 번 호출한다 (`js/main.js:2757–2865`; [CP3-034–036 최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)). [11-04 대조 정정] | `js/main.js:2757` `if (calc_constants.timeScheme == 2)`.<br>CP3 보고서 §4는 timeScheme=2의 단일 보정을 적으라고 한다. |
| [노트:235](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L235) · 정정 | Pass2도 이번 쇄파 갱신보다 먼저 txBreaking을 읽는다 (`js/main.js:2649–2679`; [RF-015 최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)). [11-04 대조 정정] | Pass2는 `if(globals.useSedTransModel == 1){` 안에서 이번 쇄파 갱신보다 먼저 txBreaking을 읽는다 (`shaders/Pass2.wgsl:139–145`; `js/main.js:2649–2679`; [RF-015 최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)). [11-04 대조 정정] | `shaders/Pass2.wgsl:139` `if(globals.useSedTransModel == 1){`.<br>141행 `let k_here =  globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, idx, 0).y;`.<br>`main.js:2649,2653`은 Pass2 뒤에 쇄파를 호출한다. |
| [노트:260](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L260) · 보완 | Pass1은 면 재구성이다 (`js/main.js:2641`). [11-04 대조 정정] | Pass1은 면 재구성이다 (`js/main.js:2641`; `docs/architecture/SIMULATION_PIPELINE.md:27`). [11-04 대조 정정] | ` docs/architecture/SIMULATION_PIPELINE.md:27 ` `` 2. `Pass1.wgsl` or `Pass1_HighOrder.wgsl` reconstructs face states from cell-centered state and bathymetry. It writes face depth, face velocity, and scalar values. `` |
| [노트:261](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L261) · 보완 | Pass2는 플럭스다 (`js/main.js:2649`). [11-04 대조 정정] | Pass2는 플럭스다 (`js/main.js:2649`; `docs/architecture/SIMULATION_PIPELINE.md:29`). [11-04 대조 정정] | ` docs/architecture/SIMULATION_PIPELINE.md:29 ` `` 4. `Pass2.wgsl`, `Pass2_HighOrder_HLLC.wgsl`, or `Pass2_HighOrder_HLLEM.wgsl` computes numerical fluxes through cell faces. The current high-order path selects HLLC. `` |
| [노트:269](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L269) · 정정 | 코드는 plynett/plynett.github.io main `ebca435`(2026-07-20)의 Celeris-WebGPU이며, 문서는 같은 커밋의 docs/·README이고, 논문은 Tavakkol & Lynett 2017(CPC), Tavakkol & Lynett 2020(CPC), Lynett et al. 2026(JWPCOE)이다. | 코드는 plynett/plynett.github.io main `ebca435`(2026-07-20)의 Celeris-WebGPU이다. 비교 문서는 같은 커밋의 docs/·README이다. 비교 논문은 Tavakkol & Lynett 2017(CPC), Tavakkol & Lynett 2020(CPC), Lynett et al. 2026(JWPCOE)이다. | version-verify-AD1:29의 현재 판 `ebca435`·날짜 `2026-07-20`.<br>세 논문의 첫 쪽 또는 쪽 머리에 있는 저자·연도·학술지. |
| [노트:273](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L273) · 정정 | 현재 원문은 §2.5. | 현재 원문은 `shaders/Pass3_Bous.wgsl:399–410`이다. | ` shaders/Pass3_Bous.wgsl:399 ` ` if (globals.timeScheme == 0) { `<br>` shaders/Pass3_Bous.wgsl:406 ` ` } else if (globals.pred_or_corrector == 2) { ` |
| [노트:274](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L274) · 정정 | `Tavakkol 2017 p.3` 식 (18) `E^{n+1},E^n,E^{n-1},E^{n-2}` | `Tavakkol 2017 p.3` 식 (18) `E_{ij}^{n+1},E_{ij}^n,E_{ij}^{n-1},E_{ij}^{n-2}` | Tavakkol 2017 p.3 식 (18)의 네 도함수는 `E_{ij}^{n+1}`, `E_{ij}^n`, `E_{ij}^{n-1}`, `E_{ij}^{n-2}`이다. |
| [노트:278](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L278) · 정정 | ` docs/architecture/CONFIGURATION.md:89 ` ` Bcoef_g의 파생식 ` | ` docs/architecture/CONFIGURATION.md:89 ` Bcoef_g의 파생식에 대한 설명 (문서에 해당 문장 없음) | ` docs/architecture/CONFIGURATION.md:89 ` `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``<br>` js/constants_load_calc.js:491 ` ` calc_constants.Bcoef_g = calc_constants.Bcoef * calc_constants.g; ` |
| [노트:279](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L279) · 정정 | ` docs/architecture/CONFIGURATION.md:89 ` ` Px의 파생식 ` | ` docs/architecture/CONFIGURATION.md:89 ` Px의 파생식에 대한 설명 (문서에 해당 문장 없음) | ` docs/architecture/CONFIGURATION.md:89 ` `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``<br>` js/constants_load_calc.js:511 ` ` calc_constants.Px = Math.ceil(Math.log(calc_constants.WIDTH)  / Math.log(2)); ` |
| [노트:280](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L280) · 정정 | ` docs/architecture/CONFIGURATION.md:89 ` ` Py의 파생식 ` | ` docs/architecture/CONFIGURATION.md:89 ` Py의 파생식에 대한 설명 (문서에 해당 문장 없음) | ` docs/architecture/CONFIGURATION.md:89 ` `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``<br>` js/constants_load_calc.js:512 ` ` calc_constants.Py = Math.ceil(Math.log(calc_constants.HEIGHT) / Math.log(2)); ` |
| [노트:281](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L281) · 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 분산 항 계산 제한 ` | 설명: 분산 항 계산 제한 (대상 8문서에 해당 문장 없음) | ` docs/architecture/SIMULATION_PIPELINE.md:32 ` `` 7. `Pass3_NLSW.wgsl`, `Pass3_NLSW_Spherical.wgsl`, `Pass3_Bous.wgsl`, or `Pass3_COULWAVE.wgsl` computes flux divergence, friction, pressure forcing, breaking/diffusion terms, scalar decay/dispersion, and the predictor/corrector update. ``<br>CD1-930 최종 근거는 구체식·조건이 문서에 없다고 판정한다. |
| [노트:282](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L282) · 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 표준 분산 생성항 ` | 설명: 표준 분산 생성항 (대상 8문서에 해당 문장 없음) | ` docs/architecture/SIMULATION_PIPELINE.md:32 ` `` 7. `Pass3_NLSW.wgsl`, `Pass3_NLSW_Spherical.wgsl`, `Pass3_Bous.wgsl`, or `Pass3_COULWAVE.wgsl` computes flux divergence, friction, pressure forcing, breaking/diffusion terms, scalar decay/dispersion, and the predictor/corrector update. ``<br>CD1-931 최종 근거는 구체식·조건이 문서에 없다고 판정한다. |
| [노트:283](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L283) · 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 표준 삼중대각 계수 ` | 설명: 표준 삼중대각 계수 (대상 8문서에 해당 문장 없음) | ` docs/architecture/SIMULATION_PIPELINE.md:32 ` `` 7. `Pass3_NLSW.wgsl`, `Pass3_NLSW_Spherical.wgsl`, `Pass3_Bous.wgsl`, or `Pass3_COULWAVE.wgsl` computes flux divergence, friction, pressure forcing, breaking/diffusion terms, scalar decay/dispersion, and the predictor/corrector update. ``<br>CD1-932 최종 근거는 구체식·조건이 문서에 없다고 판정한다. |
| [노트:284](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L284) · 정정 | ` 대상 8문서:구체식·검사 없음 ` ` PCR 감축식 ` | 설명: PCR 감축식 (대상 8문서에 해당 문장 없음) | ` docs/architecture/SIMULATION_PIPELINE.md:32 ` `` 7. `Pass3_NLSW.wgsl`, `Pass3_NLSW_Spherical.wgsl`, `Pass3_Bous.wgsl`, or `Pass3_COULWAVE.wgsl` computes flux divergence, friction, pressure forcing, breaking/diffusion terms, scalar decay/dispersion, and the predictor/corrector update. ``<br>CD1-934 최종 근거는 구체식·조건이 문서에 없다고 판정한다. |
| [노트:285](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L285) · 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 시간적분 계수 ` | 설명: 시간적분 계수 (대상 8문서에 해당 문장 없음) | ` docs/architecture/SIMULATION_PIPELINE.md:32 ` `` 7. `Pass3_NLSW.wgsl`, `Pass3_NLSW_Spherical.wgsl`, `Pass3_Bous.wgsl`, or `Pass3_COULWAVE.wgsl` computes flux divergence, friction, pressure forcing, breaking/diffusion terms, scalar decay/dispersion, and the predictor/corrector update. ``<br>CD1-935 최종 근거는 구체식·조건이 문서에 없다고 판정한다. |
| [노트:286](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L286) · 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 바닥 마찰의 얕은 흐름 정규화 `<br>반환 전 f에 속도 크기와 divide_by_h2를 곱한다. | 설명: 바닥 마찰의 얕은 흐름 정규화 (대상 8문서에 해당 문장 없음)<br>반환 전 f에 단위 폭 유량 벡터의 크기와 divide_by_h2를 곱한다. | ` docs/architecture/SIMULATION_PIPELINE.md:32 ` `` 7. `Pass3_NLSW.wgsl`, `Pass3_NLSW_Spherical.wgsl`, `Pass3_Bous.wgsl`, or `Pass3_COULWAVE.wgsl` computes flux divergence, friction, pressure forcing, breaking/diffusion terms, scalar decay/dispersion, and the predictor/corrector update. ``<br>CD1-936 최종 근거는 구체식·조건이 문서에 없다고 판정한다.<br>` shaders/Pass3_NLSW.wgsl:90 ` ` f = f * sqrt(hu * hu + hv * hv) * divide_by_h2; `<br>` shaders/Pass3_NLSW.wgsl:181 ` ` var friction_ = FrictionCalc(in_state_here.y, in_state_here.z, h_here, friction_here); ` |
| [노트:287](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L287) · 정정 | ` 대상 8문서:구체식·검사 없음 ` ` 오염원과 농도 삭제 ` | 설명: 오염원과 농도 삭제 (대상 8문서에 해당 문장 없음) | ` docs/architecture/SIMULATION_PIPELINE.md:32 ` `` 7. `Pass3_NLSW.wgsl`, `Pass3_NLSW_Spherical.wgsl`, `Pass3_Bous.wgsl`, or `Pass3_COULWAVE.wgsl` computes flux divergence, friction, pressure forcing, breaking/diffusion terms, scalar decay/dispersion, and the predictor/corrector update. ``<br>CD1-949 최종 근거는 구체식·조건이 문서에 없다고 판정한다. |
| [노트:288](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L288) · 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` showBreaking-select / 1 / Show Areas of Foam ` | 설명: showBreaking-select / 1 / Show Areas of Foam (대상 8문서에 해당 문장 없음) | ` index.html:463 ` ` <option value="1">Show Areas of Foam</option> `<br>대상 8문서는 이 id·값 대응 또는 HTML value 속성 유무를 적지 않는다. |
| [노트:289](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L289) · 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` showBreaking-select / 0 / No Foam or Tracer ` | 설명: showBreaking-select / 0 / No Foam or Tracer (대상 8문서에 해당 문장 없음) | ` index.html:464 ` ` <option value="0">No Foam or Tracer</option> `<br>대상 8문서는 이 id·값 대응 또는 HTML value 속성 유무를 적지 않는다. |
| [노트:290](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L290) · 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` showBreaking-select / 2 / Passive Tracer Conc ` | 설명: showBreaking-select / 2 / Passive Tracer Conc (대상 8문서에 해당 문장 없음) | ` index.html:465 ` ` <option value="2">Passive Tracer Conc</option> `<br>대상 8문서는 이 id·값 대응 또는 HTML value 속성 유무를 적지 않는다. |
| [노트:291](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L291) · 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` isManning-select / 0 / Quadratic Friction Drag ` | 설명: isManning-select / 0 / Quadratic Friction Drag (대상 8문서에 해당 문장 없음) | ` index.html:1408 ` ` <option value="0">Quadratic Friction Drag</option> `<br>대상 8문서는 이 id·값 대응 또는 HTML value 속성 유무를 적지 않는다. |
| [노트:292](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L292) · 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` isManning-select / 1 / Mannings Equation ` | 설명: isManning-select / 1 / Mannings Equation (대상 8문서에 해당 문장 없음) | ` index.html:1409 ` ` <option value="1">Mannings Equation</option> `<br>대상 8문서는 이 id·값 대응 또는 HTML value 속성 유무를 적지 않는다. |
| [노트:293](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L293) · 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` friction-input / value=없음 ` | 설명: friction-input / value=없음 (대상 8문서에 해당 문장 없음) | ` index.html:1417 ` ` <input type="number" id="friction-input" name="frictionValue" min="0"> `<br>대상 8문서는 이 id·값 대응 또는 HTML value 속성 유무를 적지 않는다. |
| [노트:294](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L294) · 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` whiteWaterDispersion-input / value=없음 ` | 설명: whiteWaterDispersion-input / value=없음 (대상 8문서에 해당 문장 없음) | ` index.html:1466 ` ` <input type="number" id="whiteWaterDispersion-input" name="whiteWaterDispersionValue" min="0"> `<br>대상 8문서는 이 id·값 대응 또는 HTML value 속성 유무를 적지 않는다. |
| [노트:295](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L295) · 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` whiteWaterDecayRate-input / value=없음 ` | 설명: whiteWaterDecayRate-input / value=없음 (대상 8문서에 해당 문장 없음) | ` index.html:1474 ` ` <input type="number" id="whiteWaterDecayRate-input" name="whiteWaterDecayRateValue" min="0"> `<br>대상 8문서는 이 id·값 대응 또는 HTML value 속성 유무를 적지 않는다. |
| [노트:296](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L296) · 정정 | ` 대상 8문서:HTML 세부 항목 없음 ` ` infiltrationRate-input / value=없음 ` | 설명: infiltrationRate-input / value=없음 (대상 8문서에 해당 문장 없음) | ` index.html:1482 ` ` <input type="number" id="infiltrationRate-input" name="infiltrationRateValue" min="0"> `<br>대상 8문서는 이 id·값 대응 또는 HTML value 속성 유무를 적지 않는다. |
| [노트:297](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L297) · 정정 | ` 대상 8문서:구체식·분기 상세 없음 ` ` 구면 플럭스 발산과 곡률 ` | 설명: 구면 플럭스 발산과 곡률 (대상 8문서에 해당 문장 없음) | ` shaders/Pass3_NLSW_Spherical.wgsl:206 ` ` let curvature_P = in_state_here.y * in_state_here.z * divide_by_h * tan_phi_over_R; `<br>` shaders/Pass3_NLSW_Spherical.wgsl:207 ` ` let curvature_Q = -in_state_here.y * in_state_here.y * divide_by_h * tan_phi_over_R; `<br>CD1-1388 최종 근거는 이 구체식의 문서 누락을 판정한다. |
| [노트:298](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L298) · 정정 | ` 대상 8문서:구체식·분기 상세 없음 ` ` 구면 Coriolis 항 ` | 설명: 구면 Coriolis 항 (대상 8문서에 해당 문장 없음) | ` shaders/Pass3_NLSW_Spherical.wgsl:211 ` ` let coriolis_f = 2.0 * OMEGA_EARTH * sin_phi; `<br>CD1-1389 최종 근거는 이 회전율·부호의 문서 누락을 판정한다. |
| [노트:316](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L316) · 정정 | `Tavakkol 2017 p.3` 식 (16)·(17)의 `2F^{*n}-3F^{*n-1}+F^{*n-2}`와 `2G^{*n}-3G^{*n-1}+G^{*n-2}`; 식 (19)·(20)의 `F^{*p}-F^{*n}`와 `G^{*p}-G^{*n}` | `Tavakkol 2017 p.3` 식 (16)·(17)의 `2F^{*n}-3F^{*n-1}+F_{ij}^{*n-2}`와 `2G^{*n}-3G^{*n-1}+G_{ij}^{*n-2}`; 식 (19)·(20)의 `F_{ij}^{*p}-F_{ij}^{*n}`와 `G_{ij}^{*p}-G_{ij}^{*n}` | Tavakkol 2017 p.3 식 (16)–(20)의 쪽 이미지에서 모든 F*·G* 항의 격자 첨자 ij를 확인했다. |
| [노트:317](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L317) · 정정 | `Tavakkol 2017 p.3` 식 (16) `U_{ij}^{*n+1}=U_{ij}^{*n}+\frac{\Delta t}{12}(23F_{ij}^n-16F_{ij}^{n-1}+5F_{ij}^{n-2})+2F_{ij}^{*n}-3F_{ij}^{*n-1}+F_{ij}^{*n-2}` | `Tavakkol 2017 p.3` 식 (16) `U_{ij}^{*n+1}=U_{ij}^{*n}+\frac{\Delta t}{12}(23F_{ij}^n-16F_{ij}^{n-1}+5F_{ij}^{n-2})+2F_{ij}^{*n}-3F_{ij}^{*n-1}+F_{ij}^{*n-2}` | Tavakkol 2017 p.3 식 (16)의 쪽 이미지에서 모든 F*·G* 항의 격자 첨자 ij를 확인했다. |
| [노트:318](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L318) · 정정 | `Tavakkol 2017 p.3` 식 (17) `V_{ij}^{*n+1}=V_{ij}^{*n}+\frac{\Delta t}{12}(23G_{ij}^n-16G_{ij}^{n-1}+5G_{ij}^{n-2})+2G_{ij}^{*n}-3G_{ij}^{*n-1}+G_{ij}^{*n-2}` | `Tavakkol 2017 p.3` 식 (17) `V_{ij}^{*n+1}=V_{ij}^{*n}+\frac{\Delta t}{12}(23G_{ij}^n-16G_{ij}^{n-1}+5G_{ij}^{n-2})+2G_{ij}^{*n}-3G_{ij}^{*n-1}+G_{ij}^{*n-2}` | Tavakkol 2017 p.3 식 (17)의 쪽 이미지에서 모든 F*·G* 항의 격자 첨자 ij를 확인했다. |
| [노트:319](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L319) · 정정 | `Tavakkol 2017 p.3` 식 (19) `U_{ij}^{*n+1}=U_{ij}^{*n}+\frac{\Delta t}{24}(9F_{ij}^{n+1}+19F_{ij}^n-5F_{ij}^{n-1}+F_{ij}^{n-2})+F_{ij}^{*p}-F_{ij}^{*n}` | `Tavakkol 2017 p.3` 식 (19) `U_{ij}^{*n+1}=U_{ij}^{*n}+\frac{\Delta t}{24}(9F_{ij}^{n+1}+19F_{ij}^n-5F_{ij}^{n-1}+F_{ij}^{n-2})+F_{ij}^{*p}-F_{ij}^{*n}` | Tavakkol 2017 p.3 식 (19)의 쪽 이미지에서 모든 F*·G* 항의 격자 첨자 ij를 확인했다. |
| [노트:320](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L320) · 정정 | `Tavakkol 2017 p.3` 식 (20) `V_{ij}^{*n+1}=V_{ij}^{*n}+\frac{\Delta t}{24}(9G_{ij}^{n+1}+19G_{ij}^n-5G_{ij}^{n-1}+G_{ij}^{n-2})+G_{ij}^{*p}-G_{ij}^{*n}` | `Tavakkol 2017 p.3` 식 (20) `V_{ij}^{*n+1}=V_{ij}^{*n}+\frac{\Delta t}{24}(9G_{ij}^{n+1}+19G_{ij}^n-5G_{ij}^{n-1}+G_{ij}^{n-2})+G_{ij}^{*p}-G_{ij}^{*n}` | Tavakkol 2017 p.3 식 (20)의 쪽 이미지에서 모든 F*·G* 항의 격자 첨자 ij를 확인했다. |
| [노트:333](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L333) · 정정 | `d8157c80:models/Celeris/source-analysis/celeris-boussinesq-solver.md:199` `F_G_star history ... 와 gradient history는 매 step rotate된다.` | `d8157c80:models/Celeris/source-analysis/celeris-boussinesq-solver.md:199` ``F_G_star history(`F_G_star_oldGradients`/`oldOldGradients`)와 gradient history는 매 step rotate된다.`` | ` d8157c80:models/Celeris/source-analysis/celeris-boussinesq-solver.md:199 ` `` **파이프라인 결합**: predictor 단계 → coef build → PCR(x,y) → boundary → (옵션) corrector 단계 → 다시 PCR. F_G_star history(`F_G_star_oldGradients`/`oldOldGradients`)와 gradient history는 매 step rotate된다. 전체 패스 순서·텍스처 rotation은 [celeris-pipeline-graph.md](celeris-pipeline-graph.md) 참조. `` |
| [노트:335](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L335) · 정정 | `Tavakkol 2020 p.3` 식 (2), §1.2 전사 | `Tavakkol 2020 p.3` 식 (2) | Tavakkol 2020 p.3 왼쪽에 x 분산항 식 (2)가 있다. `§1.2`는 이 원문의 절 번호가 아니다. |
| [노트:336](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md#L336) · 정정 | `Tavakkol 2020 p.3` 식 (3), §1.2 전사 | `Tavakkol 2020 p.3` 식 (3) | Tavakkol 2020 p.3 왼쪽에 y 분산항 식 (3)이 있다. `§1.2`는 이 원문의 절 번호가 아니다. |

## 차이 표 행별 근거

각 묶음의 모든 행에서 문서 인용과 코드 인용을 함께 열었다.
현재 코드와 과거 커밋을 구분했다.
문서 원문 칸의 설명은 원문 인용과 구분했다.

| 최종 근거 파일 | 노트 줄·행 ID |
|---|---|
| [Celeris-conclusion-verify-CP3RF.md](../compare/Celeris-conclusion-verify-CP3RF.md) | 273: RF-004 · 274: RF-014 · 275: RF-017 · 276: RF-023 · 303: CP3-007 · 304: CP3-022 · 305: CP3-023 · 306: CP3-031 · 307: CP3-086 · 308: CP3-087 · 309: CP3-088 |
| [Celeris-conclusion-verify-CD1d.md](../compare/Celeris-conclusion-verify-CD1d.md) | 277: CD1-532 |
| [Celeris-conclusion-verify-CD1e.md](../compare/Celeris-conclusion-verify-CD1e.md) | 278: CD1-846 · 279: CD1-866 · 280: CD1-867 |
| [Celeris-conclusion-verify-CD1f.md](../compare/Celeris-conclusion-verify-CD1f.md) | 281: CD1-930 · 282: CD1-931 · 283: CD1-932 · 284: CD1-934 · 285: CD1-935 · 286: CD1-936 · 287: CD1-949 |
| [Celeris-conclusion-verify-CD1g.md](../compare/Celeris-conclusion-verify-CD1g.md) | 288: CD1-1054 · 289: CD1-1055 · 290: CD1-1056 |
| [Celeris-conclusion-verify-CD1h.md](../compare/Celeris-conclusion-verify-CD1h.md) | 291: CD1-1226 · 292: CD1-1227 · 293: CD1-1228 · 294: CD1-1235 · 295: CD1-1236 · 296: CD1-1237 · 297: CD1-1388 · 298: CD1-1389 |
| [Celeris-conclusion-verify-CD2.md](../compare/Celeris-conclusion-verify-CD2.md) | 299: CD2-439 · 300: CD2-440 · 301: CD2-442 · 302: CD2-465 |
| [Celeris-conclusion-verify-CP1.md](../compare/Celeris-conclusion-verify-CP1.md) | 310: CP1-009 · 311: CP1-011 · 312: CP1-014 · 313: CP1-022 · 314: CP1-023 · 315: CP1-025 · 316: CP1-031 · 317: CP1-033 · 318: CP1-034 · 319: CP1-036 · 320: CP1-037 · 321: CP1-044 · 322: CP1-058 · 323: CP1-115 · 324: CP1-120 · 325: CP1-121 · 326: CP1-122 · 327: CP1-123 · 328: CP1-129 · 329: CP1-137 · 330: CP1-141 · 331: CP1-142 · 332: CP1-143 · 333: CP1-160 |
| [Celeris-conclusion-verify-CP2.md](../compare/Celeris-conclusion-verify-CP2.md) | 334: CP2-015 · 335: CP2-018 · 336: CP2-019 · 337: CP2-023 · 338: CP2-024 · 339: CP2-132 · 340: CP2-134 · 341: CP2-139 · 342: CP2-141 · 343: CP2-164 |

A 행의 판 근거는 [version-verify-AD1](../compare/Celeris-version-verify-AD1.md)과 [version-verify-AD2](../compare/Celeris-version-verify-AD2.md)의 해당 행에 대조했다.
노트가 가리킨 과거 코드의 254d71c, 6f1272f, 471c581, 366ee34, 63a12e3, f18955b, f6fd78b, 89c9824, 984091f 판을 해당 파일의 인용 줄에서 열었다.
이전 위키 인용은 d8157c80 및 938a3bb1의 해당 파일에서 열었다.
E 행은 [version-verify-E1](../compare/Celeris-version-verify-E1.md)의 CP1-022·023 및 CP2 최종 근거에 대조했다.
본문 CT1-358은 [CT1c 최종 근거](../compare/Celeris-conclusion-verify-CT1c.md)와 [version-verify-E2](../compare/Celeris-version-verify-E2.md)에 대조했다.
[외부 출처 최종 절](../compare/Celeris-external-sources.md#최종)의 CP3-013·017은 이 노트의 차이 표 배정 행이 아니다.

논문 판독은 제공된 celpages의 다음 쪽 이미지를 사용했다.
2017 논문은 p.1·2·3·4·6·7을 열었다.
2020 논문은 p.1·3을 열었다.
2026 논문은 p.1·2·3·4·5·6을 열었다.
식·첨자·부호·수치는 이 이미지로 판정했다.
쪽별 판독 기록은 원문 위치와 전사 내용을 찾는 보조 자료로 사용했다.

## 기계 확인 후보 판정

- `docs/architecture/DATA_AND_TEXTURES.md:69` 뒤의 `|`: 오판이다. 노트 277행의 세로줄은 Markdown 표의 구분자다. 원문 69행은 ``- `txtemp2_PCRx`, `txtemp2_PCRy`: solution textures written only by the final PCR iteration of each directional solve.``이다. 984091f와 현재 판에서 이 문장을 확인했다. 노트의 마지막 반복 설명은 맞으므로 유지했다.
- `docs/architecture/CONFIGURATION.md:89` 뒤의 `Bcoef_g의 파생식`: 노트 오류다. 원문 89행은 `` `init_sim_parameters()` computes values that are not meant to be edited directly: ``이다. 노트 278행에서 설명의 백틱을 빼고 문서에 해당 문장이 없다고 명시했다.
- `docs/architecture/CONFIGURATION.md:89` 뒤의 `Px의 파생식`: 노트 오류다. 원문 93행은 PCR 반복 수의 명칭만 적는다. 노트 279행에서 설명의 백틱을 빼고 문서에 해당 문장이 없다고 명시했다.
- `docs/architecture/CONFIGURATION.md:89` 뒤의 `Py의 파생식`: 노트 오류다. 원문 93행은 PCR 반복 수의 명칭만 적는다. 노트 280행에서 설명의 백틱을 빼고 문서에 해당 문장이 없다고 명시했다.

## 마지막 확인

수정 뒤에도 HEAD 대비 대상 추가 줄은 133줄이다.
이번 작업의 변경은 그중 39줄에 한정된다.
표의 열 수는 71행 모두 6개다.
인접한 파일·줄 인용과 백틱 원문 402쌍을 다시 비교했다.
그 검사에서 남은 문자 불일치는 없다.
이 검사는 바깥 공백과 Markdown의 세로줄 이스케이프를 구분했다.
범위 인용 뒤의 여러 코드 토막은 해당 파일·범위의 원문과 별도로 대조했다.

노트 전체의 Markdown 링크 185개를 검사했다.
서로 다른 링크 대상은 21개다.
깨진 상대 파일 링크는 없다.
노트에는 절대 로컬 경로, `~/`, 이중 대괄호 링크가 없다.
요청에서 금지한 한계 문장은 없다.
노트에는 Mermaid 블록이 없다.
따라서 흐름도 복사·렌더에 대한 추가 수정은 없다.

이번 작업은 대상 노트와 이 DELIVERABLE만 썼다.
git 쓰기 명령과 sudo를 사용하지 않았다.
모델을 실행하지 않았다.
노트의 대상 줄 대조를 모두 마쳤다.
미해결 항목은 없다.
