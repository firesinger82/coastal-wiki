# Celeris transect 판과 본판 대조

분류별 개수: A 168, B 3, C 43, D 0, E 45, F 120, H 0, X 0. 합계 379행. 집계 기준은 5절의 행 ID다.

## 1 요약

이 보고서에서 문서는 본판 코드를 뜻한다.
이 보고서에서 코드는 `transect_version/` 코드를 뜻한다.
공통 코드 루트는 `models/Celeris/raw/source_code/Celeris-WebGPU/`다.
기준 커밋은 `ebca435d02b258768e0352fbaf27404f2f135799`다.
기준 커밋의 날짜는 2026-07-20이다.
이 보고서는 두 판의 `js/*.js`, `shaders/*.wgsl`, `shaders/*.compute`, `index.html`을 대조한다.
skybox·duck·model의 vertex·fragment 셰이더는 사용자 지정 범위에서 제외한다.
호스트 코드의 해당 파일은 파일 목록 대조에 포함한다.
추가 HTML 진입점과 MATLAB 출력 판독기는 차이의 호출·자료 형식 근거를 확인할 때 참조한다.
README·설계 문서·논문은 이 작업의 문서 측 대조 대상을 대체하지 않는다.
따라서 이 보고서는 별도 논문 대 코드 전수 대조를 주장하지 않는다.

transect 판은 2025-06-06 `22e1983`에서 처음 추가되었다.
커밋 메시지는 `Sediment transport updates and transect model beta`다.
2025-06-14 `3d8a61b`는 `Added many-transect version`을 기록한다.
해석: transect 판의 y 인덱스는 서로 독립적인 x 단면을 묶는 용도로 사용한다.
각 계산 셰이더의 y 미분 제거와 행별 입사파 텍스처가 이 해석의 근거다.
2026-02-06 `151017f`는 transect 판의 업로드 임시 버퍼 정리를 수정했다.
따라서 transect 판 전체를 특정 날짜에 멈춘 동일 사본으로 취급하지 않는다.

### 1.1 확인 방법과 인용

각 공통 파일에 대해 `diff -u 본판파일 transect파일`을 실행한다.
동작 차이를 읽기 위해 `diff -u --strip-trailing-cr 본판파일 transect파일`도 실행한다.
두 번째 명령은 행 끝의 CR만 제거한다.
그 명령은 공백·조건·상수·주석 차이를 제거하지 않는다.
줄바꿈 차이는 별도 F 행에서 기록한다.
2절의 diff는 두 번째 명령의 전체 출력이다.
각 diff의 `@@ -A,B +C,D @@`는 본판 A행부터 B행과 transect C행부터 D행을 뜻한다.
diff의 `-`는 본판 원문이다.
diff의 `+`는 transect 원문이다.
여러 줄 식과 조건은 diff 안에서 이어진 줄 전체를 보존한다.
원문 행은 `nl -ba`로 읽는다.
각 파일 이력은 `git log --follow -p -- 파일`로 읽는다.
차이 줄의 현재 귀속은 `git blame -w --line-porcelain -- 파일`로 보조 확인한다.
blame의 날짜는 해당 줄의 마지막 수정 날짜다.
blame의 날짜만으로 기능의 최초 도입 날짜를 단정하지 않는다.
파일별 이력과 최초 추가 커밋을 함께 기록한다.
판 인용의 형식은 `HASH:파일:줄`이다.
현재 원문 행 번호는 `ebca435:파일:줄`로 고정한다.
과거 변경의 판 인용은 해당 커밋의 원문 행 번호를 별도로 확인한다.

모델과 브라우저를 실행하지 않는다.
따라서 E는 정적 대조에 근거한 코드 결함 후보를 뜻한다.
본판만 고친 결함은 A로 덮지 않고 E로 분리한다.
의도된 1D 단순화는 F 또는 C로 분류한다.
C는 본판에 없는 transect 기능을 뜻한다.
D는 본판에만 있는 기능에 적용한다.
D 행은 현재 트리의 대소문자 무시 검색과 git 문자열 이력 검색을 함께 기록한다.
A는 실제 도입 시점으로 설명하는 판 차이에 적용한다.

## 2 대조 표

### 2.1 파일 전수 목록과 줄바꿈

파일 합집합은 78개다.
공통 파일은 66개다.
본판 전용 파일은 11개다.
transect 전용 파일은 1개다.
바이트까지 같은 공통 파일은 4개다.
CR을 제외하면 같은 공통 파일은 19개다.
이 개수는 정의한 확장자와 제외 파일명을 적용한 결과다.

| 행 ID | 파일 | 본판 행 수 | transect 행 수 | 원래 diff 행 수 | CR 제외 diff 구간 수 | 판정 |
|---|---|---:|---:|---:|---:|---|
| CT1-001 | `index.html` | 1601 | 1475 | 3055 | 23 | 내용 차이 |
| CT1-002 | `js/Config_Pipelines.js` | 283 | 283 | 569 | 0 | 줄바꿈만 다름 |
| CT1-003 | `js/Copy_Data_to_Textures.js` | 642 | 555 | 1123 | 8 | 내용 차이 |
| CT1-004 | `js/Create_Textures.js` | 100 | 100 | 203 | 0 | 줄바꿈만 다름 |
| CT1-005 | `js/File_Loader.js` | 819 | 527 | 1291 | 4 | 내용 차이 |
| CT1-006 | `js/File_Writer.js` | 848 | 657 | 1467 | 9 | 내용 차이 |
| CT1-007 | `js/Handler_AddDisturbance.js` | 121 | 108 | 232 | 2 | 내용 차이 |
| CT1-008 | `js/Handler_BoundaryPass.js` | 206 | 148 | 309 | 2 | 내용 차이 |
| CT1-009 | `js/Handler_CalcMeans.js` | 200 | 187 | 390 | 2 | 내용 차이 |
| CT1-010 | `js/Handler_CalcWaveHeight.js` | 93 | 93 | 189 | 0 | 줄바꿈만 다름 |
| — | `js/Handler_Copytxf32_txf16.js` | 134 | 121 | 39 | 2 | 내용 차이 |
| — | `js/Handler_ExtractNestedBoundaryTimeSeries.js` | 109 | 없음 | 112 | 1 | 본판에만 |
| CT1-011 | `js/Handler_ExtractTimeSeries.js` | 133 | 120 | 256 | 2 | 내용 차이 |
| — | `js/Handler_Model.js` | 58 | 58 | 0 | 0 | 일치 |
| CT1-012 | `js/Handler_MouseClickChange.js` | 120 | 120 | 243 | 0 | 줄바꿈만 다름 |
| CT1-013 | `js/Handler_Pass0.js` | 69 | 69 | 141 | 0 | 줄바꿈만 다름 |
| CT1-014 | `js/Handler_Pass1.js` | 111 | 111 | 225 | 0 | 줄바꿈만 다름 |
| CT1-015 | `js/Handler_Pass2.js` | 228 | 215 | 448 | 2 | 내용 차이 |
| CT1-016 | `js/Handler_Pass3.js` | 572 | 572 | 1147 | 0 | 줄바꿈만 다름 |
| — | `js/Handler_PassBreaking.js` | 135 | 135 | 0 | 0 | 일치 |
| CT1-017 | `js/Handler_Render.js` | 391 | 390 | 784 | 1 | 내용 차이 |
| CT1-018 | `js/Handler_SedTrans_Pass1.js` | 124 | 124 | 251 | 0 | 줄바꿈만 다름 |
| CT1-019 | `js/Handler_SedTrans_Pass3.js` | 254 | 189 | 448 | 2 | 내용 차이 |
| CT1-020 | `js/Handler_SedTrans_UpdateBottom.js` | 135 | 109 | 247 | 2 | 내용 차이 |
| — | `js/Handler_Skybox.js` | 57 | 57 | 0 | 0 | 일치 |
| CT1-021 | `js/Handler_Tridiag.js` | 109 | 109 | 221 | 0 | 줄바꿈만 다름 |
| CT1-022 | `js/Handler_UpdateTrid.js` | 81 | 81 | 165 | 0 | 줄바꿈만 다름 |
| CT1-023 | `js/Handler_Updateneardry.js` | 54 | 54 | 111 | 0 | 줄바꿈만 다름 |
| — | `js/Model_Loaders.js` | 236 | 236 | 0 | 0 | 일치 |
| CT1-024 | `js/Run_Compute_Shader.js` | 89 | 52 | 144 | 3 | 내용 차이 |
| CT1-025 | `js/Run_Tridiag_Solver.js` | 93 | 77 | 149 | 3 | 내용 차이 |
| CT1-026 | `js/Time_Series.js` | 184 | 169 | 353 | 4 | 내용 차이 |
| — | `js/Wave_Generator.js` | 374 | 없음 | 377 | 1 | 본판에만 |
| — | `js/agent_controls.js` | 949 | 없음 | 952 | 1 | 본판에만 |
| CT1-027 | `js/constants_load_calc.js` | 664 | 480 | 1128 | 15 | 내용 차이 |
| CT1-028 | `js/display_parameters.js` | 251 | 228 | 470 | 5 | 내용 차이 |
| CT1-029 | `js/main.js` | 5489 | 3431 | 8762 | 89 | 내용 차이 |
| CT1-030 | `js/site.js` | 4 | 4 | 11 | 0 | 줄바꿈만 다름 |
| CT1-031 | `shaders/AddDisturbance.wgsl` | 241 | 234 | 478 | 7 | 내용 차이 |
| CT1-032 | `shaders/BoundaryPass.wgsl` | 725 | 558 | 1286 | 11 | 내용 차이 |
| CT1-033 | `shaders/CalcMeans.wgsl` | 104 | 105 | 212 | 3 | 내용 차이 |
| CT1-034 | `shaders/CalcWaveHeight.wgsl` | 77 | 77 | 157 | 0 | 줄바꿈만 다름 |
| — | `shaders/Copytxf32_txf16.wgsl` | 50 | 35 | 53 | 2 | 내용 차이 |
| — | `shaders/ExtractNestedBoundaryTimeSeries.wgsl` | 53 | 없음 | 56 | 1 | 본판에만 |
| CT1-035 | `shaders/ExtractTimeSeries.wgsl` | 65 | 58 | 126 | 3 | 내용 차이 |
| CT1-036 | `shaders/MouseClickChange.wgsl` | 246 | 166 | 388 | 4 | 내용 차이 |
| CT1-037 | `shaders/Pass0.wgsl` | 60 | 60 | 123 | 1 | 내용 차이 |
| CT1-038 | `shaders/Pass1.wgsl` | 172 | 183 | 358 | 2 | 내용 차이 |
| — | `shaders/Pass1_HighOrder.wgsl` | 368 | 380 | 306 | 3 | 내용 차이 |
| CT1-039 | `shaders/Pass2.wgsl` | 206 | 181 | 390 | 3 | 내용 차이 |
| — | `shaders/Pass2_HighOrder.wgsl` | 없음 | 234 | 237 | 1 | transect에만 |
| — | `shaders/Pass2_HighOrder_HLLC.wgsl` | 291 | 없음 | 294 | 1 | 본판에만 |
| — | `shaders/Pass2_HighOrder_HLLEM.wgsl` | 274 | 없음 | 277 | 1 | 본판에만 |
| — | `shaders/Pass3A_COULWAVE.wgsl` | 85 | 89 | 64 | 2 | 내용 차이 |
| — | `shaders/Pass3B_COULWAVE.wgsl` | 206 | 175 | 254 | 3 | 내용 차이 |
| CT1-040 | `shaders/Pass3_Bous.wgsl` | 430 | 426 | 859 | 10 | 내용 차이 |
| — | `shaders/Pass3_COULWAVE.wgsl` | 524 | 532 | 572 | 12 | 내용 차이 |
| CT1-041 | `shaders/Pass3_NLSW.wgsl` | 286 | 277 | 566 | 6 | 내용 차이 |
| — | `shaders/Pass3_NLSW_Spherical.wgsl` | 267 | 없음 | 270 | 1 | 본판에만 |
| — | `shaders/Pass_Breaking.wgsl` | 145 | 149 | 125 | 4 | 내용 차이 |
| CT1-042 | `shaders/SedTrans_Pass1.wgsl` | 135 | 135 | 273 | 1 | 내용 차이 |
| CT1-043 | `shaders/SedTrans_Pass3.wgsl` | 241 | 140 | 384 | 5 | 내용 차이 |
| — | `shaders/SedTrans_Pass3_old.wgsl` | 181 | 없음 | 185 | 1 | 본판에만 |
| — | `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | 255 | 없음 | 259 | 1 | 본판에만 |
| CT1-044 | `shaders/SedTrans_UpdateBottom.wgsl` | 122 | 52 | 177 | 3 | 내용 차이 |
| — | `shaders/SedTrans_UpdateBottom_testing.wgsl` | 90 | 없음 | 93 | 1 | 본판에만 |
| CT1-045 | `shaders/Ship_pressure.compute` | 81 | 81 | 165 | 0 | 줄바꿈만 다름 |
| CT1-046 | `shaders/TriDiag_PCRx.wgsl` | 107 | 97 | 196 | 3 | 내용 차이 |
| — | `shaders/TriDiag_PCRx_COULWAVE.wgsl` | 116 | 106 | 40 | 2 | 내용 차이 |
| CT1-047 | `shaders/TriDiag_PCRy.wgsl` | 110 | 100 | 196 | 3 | 내용 차이 |
| — | `shaders/TriDiag_PCRy_COULWAVE.wgsl` | 119 | 109 | 41 | 2 | 내용 차이 |
| CT1-048 | `shaders/Update_TriDiag_coef.wgsl` | 111 | 111 | 225 | 3 | 내용 차이 |
| — | `shaders/Update_TriDiag_coef_COULWAVE.wgsl` | 117 | 117 | 82 | 2 | 내용 차이 |
| CT1-049 | `shaders/Update_neardry.wgsl` | 56 | 58 | 117 | 2 | 내용 차이 |
| CT1-050 | `shaders/fragment.wgsl` | 928 | 857 | 1772 | 7 | 내용 차이 |
| — | `shaders/fragment_testing.wgsl` | 867 | 없음 | 870 | 1 | 본판에만 |
| CT1-051 | `shaders/vertex.wgsl` | 19 | 19 | 41 | 0 | 줄바꿈만 다름 |
| CT1-052 | `shaders/vertex3D.wgsl` | 86 | 85 | 174 | 1 | 내용 차이 |

| 행 ID | 원문 바이트 차이 |
|---|---|
| CT1-001 | 본판 CRLF 행: 1–1309, 1371–1601. transect CRLF 행: 없음. |
| CT1-002 | 본판 CRLF 행: 1–283. transect CRLF 행: 없음. |
| CT1-003 | 본판 CRLF 행: 1–131, 192–349, 408–637. transect CRLF 행: 없음. |
| CT1-004 | 본판 CRLF 행: 1–100. transect CRLF 행: 없음. |
| CT1-005 | 본판 CRLF 행: 1–266, 268–300, 516–615, 653–819. transect CRLF 행: 없음. |
| CT1-006 | 본판 CRLF 행: 1–612, 617–631, 846–848. transect CRLF 행: 없음. |
| CT1-007 | 본판 CRLF 행: 1–120. transect CRLF 행: 없음. |
| CT1-008 | 본판 CRLF 행: 1–86, 141–181. transect CRLF 행: 없음. |
| CT1-009 | 본판 CRLF 행: 1–199. transect CRLF 행: 없음. |
| CT1-010 | 본판 CRLF 행: 1–92. transect CRLF 행: 없음. |
| CT1-011 | 본판 CRLF 행: 1–132. transect CRLF 행: 없음. |
| CT1-012 | 본판 CRLF 행: 1–119. transect CRLF 행: 없음. |
| CT1-013 | 본판 CRLF 행: 1–68. transect CRLF 행: 없음. |
| CT1-014 | 본판 CRLF 행: 1–110. transect CRLF 행: 없음. |
| CT1-015 | 본판 CRLF 행: 1–227. transect CRLF 행: 없음. |
| CT1-016 | 본판 CRLF 행: 1–572. transect CRLF 행: 없음. |
| CT1-017 | 본판 CRLF 행: 1–391. transect CRLF 행: 없음. |
| CT1-018 | 본판 CRLF 행: 1–123. transect CRLF 행: 없음. |
| CT1-019 | 본판 CRLF 행: 1–253. transect CRLF 행: 없음. |
| CT1-020 | 본판 CRLF 행: 1–134. transect CRLF 행: 없음. |
| CT1-021 | 본판 CRLF 행: 1–108. transect CRLF 행: 없음. |
| CT1-022 | 본판 CRLF 행: 1–80. transect CRLF 행: 없음. |
| CT1-023 | 본판 CRLF 행: 1–53. transect CRLF 행: 없음. |
| CT1-024 | 본판 CRLF 행: 1–89. transect CRLF 행: 없음. |
| CT1-025 | 본판 CRLF 행: 1–17, 36–43, 49–53, 64–68, 74–78, 89–93. transect CRLF 행: 없음. |
| CT1-026 | 본판 CRLF 행: 1–57, 62–97, 114–184. transect CRLF 행: 없음. |
| CT1-027 | 본판 CRLF 행: 1–76, 99–254, 263–369, 398–573, 602–664. transect CRLF 행: 없음. |
| CT1-028 | 본판 CRLF 행: 1–119, 142–231, 242–250. transect CRLF 행: 없음. |
| CT1-029 | 본판 CRLF 행: 1–2, 9–11, 16–36, 42–194, 198–205, 215–217, 221–247, 264–289, 301–328, 391–407, 415–560, 578–586, 598–1152, 1161–1204, 1219–1391, 1415–1597, 1605–1636, 1644–1716, 1721–1724, 1738–1770, 2213–2401, 2420–2483, 2496–2600, 2613–2621, 2625–2626, 2634–2886, 2898–2929, 2981–3467, 3511–3515, 3520–3989, 3996–3999, 4079–4273, 4285–4664, 4671–4726, 4744–5123, 5141–5237, 5250–5277, 5287–5309, 5316–5319, 5326–5335, 5339–5346, 5352–5469, 5476–5489. transect CRLF 행: 없음. |
| CT1-030 | 본판 CRLF 행: 1–4. transect CRLF 행: 없음. |
| CT1-031 | 본판 CRLF 행: 1–241. transect CRLF 행: 없음. |
| CT1-032 | 본판 CRLF 행: 1–725. transect CRLF 행: 없음. |
| CT1-033 | 본판 CRLF 행: 1–104. transect CRLF 행: 없음. |
| CT1-034 | 본판 CRLF 행: 1–77. transect CRLF 행: 없음. |
| CT1-035 | 본판 CRLF 행: 1–65. transect CRLF 행: 없음. |
| CT1-036 | 본판 CRLF 행: 1–13, 28–57, 63–64, 106–125, 141–197, 243–245. transect CRLF 행: 없음. |
| CT1-037 | 본판 CRLF 행: 1–60. transect CRLF 행: 없음. |
| CT1-038 | 본판 CRLF 행: 1–172. transect CRLF 행: 없음. |
| CT1-039 | 본판 CRLF 행: 1–206. transect CRLF 행: 없음. |
| CT1-040 | 본판 CRLF 행: 1–430. transect CRLF 행: 없음. |
| CT1-041 | 본판 CRLF 행: 1–285. transect CRLF 행: 없음. |
| CT1-042 | 본판 CRLF 행: 1–135. transect CRLF 행: 없음. |
| CT1-043 | 본판 CRLF 행: 1–240. transect CRLF 행: 없음. |
| CT1-044 | 본판 CRLF 행: 1–122. transect CRLF 행: 없음. |
| CT1-045 | 본판 CRLF 행: 1–81. transect CRLF 행: 없음. |
| CT1-046 | 본판 CRLF 행: 1–2, 9–19, 24–92, 107. transect CRLF 행: 없음. |
| CT1-047 | 본판 CRLF 행: 1–2, 9–19, 24–92. transect CRLF 행: 없음. |
| CT1-048 | 본판 CRLF 행: 1–111. transect CRLF 행: 없음. |
| CT1-049 | 본판 CRLF 행: 1–56. transect CRLF 행: 없음. |
| CT1-050 | 본판 CRLF 행: 1–54, 69–797, 856–928. transect CRLF 행: 없음. |
| CT1-051 | 본판 CRLF 행: 1–19. transect CRLF 행: 없음. |
| CT1-052 | 본판 CRLF 행: 1–85. transect CRLF 행: 없음. |

CR을 제외하면 같은 공통 파일은 다음과 같다.

- `js/Config_Pipelines.js`: `1–283` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Create_Textures.js`: `1–100` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_CalcWaveHeight.js`: `1–93` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_Model.js`: `1–58` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_MouseClickChange.js`: `1–120` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_Pass0.js`: `1–69` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_Pass1.js`: `1–111` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_Pass3.js`: `1–572` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_PassBreaking.js`: `1–135` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_SedTrans_Pass1.js`: `1–124` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_Skybox.js`: `1–57` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_Tridiag.js`: `1–109` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_UpdateTrid.js`: `1–81` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Handler_Updateneardry.js`: `1–54` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/Model_Loaders.js`: `1–236` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `js/site.js`: `1–4` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `shaders/CalcWaveHeight.wgsl`: `1–77` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `shaders/Ship_pressure.compute`: `1–81` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.
- `shaders/vertex.wgsl`: `1–19` 전체가 같다. 파일 안의 옵션·식·계수·조건·입출력은 두 판에서 같다.

동일 파일에도 두 경로 각각의 `git log --follow -p`를 실행했다.
transect 파일 추가 커밋을 공통 코드의 최초 개발 커밋으로 읽지 않는다.


### 2.2 js/Copy_Data_to_Textures.js

본판: `js/Copy_Data_to_Textures.js`. transect 판: `transect_version/js/Copy_Data_to_Textures.js`.
원래 diff는 1123행이다. CR 제외 diff는 8구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `bb99fee` | 2026-07-02 | Added grid nesting |
| 본판 | `afc1fe7` | 2026-06-19 | Added Spherical NLSW Solver, Japan 2011 example |
| 본판 | `ca9278e` | 2026-02-11 | Update Copy_Data_to_Textures.js |
| 본판 | `25d9c56` | 2026-02-11 | Update Copy_Data_to_Textures.js |
| 본판 | `151017f` | 2026-02-06 | Fix GPU memory leak: destroy staging buffers after texture upload |
| 본판 | `32be94a` | 2025-10-16 | hot start initial condition option added |
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| transect | `151017f` | 2026-02-06 | Fix GPU memory leak: destroy staging buffers after texture upload |
| transect | `3d8a61b` | 2025-06-14 | Added many-transect version |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-053 초기 지형 전처리와 북쪽 면

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Copy_Data_to_Textures.js:12; 아래 전체 diff의 -행 | ebca435:transect_version/js/Copy_Data_to_Textures.js:12; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 단일점 섬 제거를 주석 처리한다. transect 판은 북쪽 면 고도 BN을 0.0으로 저장한다. 이는 본판 전처리의 보존이 아니라 단면 전용 선택이다. |

본판 차이 줄의 마지막 수정: `ebc98a5` 2024-03-13 (현재 35행 포함); `63a12e3` 2023-10-19 (현재 40행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 40행 포함).

```diff
@@ -12,32 +12,32 @@
     const paddedFlatData = new Float32Array(calc_constants.HEIGHT * requiredBytesPerRow / 4);
 
     // remove single point islands
-    let change_point = 1.;
-    let new_count = 0.;
-    let old_count = 0.;
-    while (change_point > 0.5)  {
-        old_count = new_count;
-        new_count = 0.;
-        for (let y = 1; y < calc_constants.HEIGHT-1; y++) {
-            for (let x = 1; x < calc_constants.WIDTH-1; x++) {
-                if (bathy2D[x][y] >= 0.0){  // dry point
-                    if (bathy2D[x+1][y] <= 0.0 && bathy2D[x-1][y] <= 0.0 && bathy2D[x][y+1] <= 0.0 && bathy2D[x][y-1] <= 0.0 ){
-                        bathy2D[x][y] = 0.0;
-                        new_count = new_count + 1.0;
-                    }
-                }
-            }
-        }
-        change_point = new_count - old_count;
-        if (change_point > 0.5 ){
-            console.log("Flattened ", change_point, " single point islands from initial bathy/topo");
-        }
-    }
+    // let change_point = 1.;
+    // let new_count = 0.;
+    // let old_count = 0.;
+    // while (change_point > 0.5)  {
+    //     old_count = new_count;
+    //     new_count = 0.;
+    //     for (let y = 1; y < calc_constants.HEIGHT-1; y++) {
+    //         for (let x = 1; x < calc_constants.WIDTH-1; x++) {
+    //             if (bathy2D[x][y] >= 0.0){  // dry point
+    //                 if (bathy2D[x+1][y] <= 0.0 && bathy2D[x-1][y] <= 0.0 ){
+    //                     bathy2D[x][y] = 0.0;
+    //                     new_count = new_count + 1.0;
+    //                 }
+    //             }
+    //         }
+    //     }
+    //     change_point = new_count - old_count;
+    //     if (change_point > 0.5 ){
+    //         console.log("Flattened ", change_point, " single point islands from initial bathy/topo");
+    //     }
+    // }
 
     let lengthCheck = 3;    // check within three points
     for (let y = 0; y < calc_constants.HEIGHT; y++) {
         for (let x = 0; x < calc_constants.WIDTH; x++) {
-            let BN = 0.5 * bathy2D[x][y] + 0.5 * bathy2D[x][Math.min(calc_constants.HEIGHT - 1, y + 1)];
+            let BN = 0.0; // should not be used. 0.5 * bathy2D[x][y] + 0.5 * bathy2D[x][Math.min(calc_constants.HEIGHT - 1, y + 1)];
             let BE = 0.5 * bathy2D[x][y] + 0.5 * bathy2D[Math.min(calc_constants.WIDTH - 1, x + 1)][y];
 
             const paddedIndex = (y * requiredBytesPerRow / 4) + x * 4; // Adjust the index for padding
```

#### CT1-054 near-dry CPU 검사

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Copy_Data_to_Textures.js:47; 아래 전체 diff의 -행 | ebca435:transect_version/js/Copy_Data_to_Textures.js:47; 아래 전체 diff의 +행 | 불일치 (F) | 본판은 x·y 각각 ±3칸을 검사한다. transect 판은 같은 행의 x ±3칸만 검사한다. 독립 단면에서 검사 대상은 7개 x 위치로 줄어든다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 59행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 59행 포함).

```diff
@@ -47,16 +47,16 @@
             paddedFlatData[paddedIndex + 3] = 99;  // alpha
 
             // boolean near-dry check
-            for (let yy = y - lengthCheck; yy <= y + lengthCheck; ++yy) {
+            //for (let yy = y - lengthCheck; yy <= y + lengthCheck; ++yy) {
                 for (let xx = x - lengthCheck; xx <= x + lengthCheck; ++xx) {
                     let xC = Math.min(calc_constants.WIDTH - 1, Math.max(0, xx));
-                    let yC = Math.min(calc_constants.HEIGHT - 1, Math.max(0, yy));
+                   // let yC = Math.min(calc_constants.HEIGHT - 1, Math.max(0, yy));
 
-                    if (bathy2D[xC][yC] >= 0) {
+                    if (bathy2D[xC][y] >= 0) {
                         paddedFlatData[paddedIndex + 3] = -99;
                     }
                 }
-            }
+            //}
 
      //       if (y < 4 || x < 4 || y > calc_constants.HEIGHT - 3 || x > calc_constants.WIDTH - 3) {
      //           paddedFlatData[paddedIndex + 3] = -99;
```

#### CT1-055 단면별 파랑 업로드

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Copy_Data_to_Textures.js:89; 아래 전체 diff의 -행 | ebca435:transect_version/js/Copy_Data_to_Textures.js:89; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 numberOfWaves × HEIGHT 텍스처를 만든다. 입력의 첫 HEIGHT행은 진폭이다. 다음 HEIGHT행은 주기다. 마지막 HEIGHT행은 위상이다. 방향 채널은 0.0이다. bytesPerRow는 256배수로 올림한다. |

본판 차이 줄의 마지막 수정: 추가·삭제 줄 없음. transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 134행 포함); `151017f` 2026-02-06 (현재 130행 포함).

```diff
@@ -89,6 +89,49 @@
     return paddedFlatData;
 }
 
+
+function copyTransectWaveDataToTexture(calc_constants, waveData, device, txWaves_Transect) {
+    // copy waveData into txWaves_Transect
+
+    const actualBytesPerRow = calc_constants.numberOfWaves * 4 * 4; // 4 channels and 4 bytes per float
+    const requiredBytesPerRow = Math.ceil(actualBytesPerRow / 256) * 256;
+    const paddedFlatData = new Float32Array(calc_constants.HEIGHT * requiredBytesPerRow / 4);
+
+    for (let y = 0; y < calc_constants.HEIGHT; y++) {
+        for (let x = 0; x < calc_constants.numberOfWaves; x++) {
+
+            const paddedIndex = (y * requiredBytesPerRow / 4) + x * 4; // Adjust the index for padding
+            paddedFlatData[paddedIndex] = waveData[x][y];  // red, amplitude
+            paddedFlatData[paddedIndex + 1] = waveData[x][y + calc_constants.HEIGHT];  // green, period
+            paddedFlatData[paddedIndex + 2] = 0.0;  // blue, direction - zeros
+            paddedFlatData[paddedIndex + 3] = waveData[x][y + 2 * calc_constants.HEIGHT];  // alpha, phases
+        }
+    }
+    const buffer = device.createBuffer({
+        size: paddedFlatData.byteLength,
+        usage: GPUBufferUsage.COPY_SRC,
+        mappedAtCreation: true
+    });
+    new Float32Array(buffer.getMappedRange()).set(paddedFlatData);
+    buffer.unmap();
+    const commandEncoder = device.createCommandEncoder();
+    commandEncoder.copyBufferToTexture({
+        buffer: buffer,
+        bytesPerRow: requiredBytesPerRow,
+        rowsPerImage: calc_constants.HEIGHT,
+    }, {
+        texture: txWaves_Transect
+    }, {
+        width: calc_constants.numberOfWaves,
+        height: calc_constants.HEIGHT,
+        depthOrArrayLayers: 1
+    });
+    device.queue.submit([commandEncoder.finish()]);
+    buffer.destroy();
+
+}
+
+
 function copyWaveDataToTexture(calc_constants, waveData, device, txWaves) {
     // copy waveData into txWaves
```

#### CT1-056 경계 시계열 업로드와 위치 업로드

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Copy_Data_to_Textures.js:133; 아래 전체 diff의 -행 | ebca435:transect_version/js/Copy_Data_to_Textures.js:176; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 경계 관측점·시간·eta/hu/hv를 RGBA32F 텍스처로 패킹한다. transect 판은 이 자리에 측정점 위치 업로드를 둔다. 두 함수는 같은 함수의 이름 변경이 아니다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 162행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 198행 포함).

```diff
@@ -133,33 +176,26 @@
     buffer.destroy();
 }
 
-// Added by Codex: Start boundary time-series forcing texture upload support.
-function copyBoundaryTimeSeriesDataToTexture(boundaryTimeSeriesSideData, device, txBoundaryTimeSeries) {
-    const sideData = boundaryTimeSeriesSideData || {};
-    const numPoints = Number.isFinite(sideData.numPoints) ? sideData.numPoints : 0;
-    const numTimes = Number.isFinite(sideData.numTimes) ? sideData.numTimes : 0;
-    const textureWidth = Math.max(Number.isFinite(sideData.textureWidth) ? sideData.textureWidth : numPoints, 1);
-    const textureHeight = Math.max(Number.isFinite(sideData.textureHeight) ? sideData.textureHeight : numTimes + 2, 1);
-    const actualBytesPerRow = textureWidth * 4 * 4; // 4 channels and 4 bytes per float
-    const requiredBytesPerRow = Math.ceil(actualBytesPerRow / 256) * 256;
-    const paddedFlatData = new Float32Array(textureHeight * requiredBytesPerRow / 4);
 
-    for (let pointIndex = 0; pointIndex < numPoints; pointIndex += 1) {
-        const paddedIndex = pointIndex * 4;
-        paddedFlatData[paddedIndex] = sideData.locations[pointIndex];
-    }
+function copyTSlocsToTexture(calc_constants, device, txTimeSeries_Locations) {
+    // copy time series lcations into txTimeSeries_Locations
 
-    for (let timeIndex = 0; timeIndex < numTimes; timeIndex += 1) {
-        const rowStart = (timeIndex + 1) * requiredBytesPerRow / 4;
-        const rowValues = sideData.values[timeIndex];
-        for (let pointIndex = 0; pointIndex < numPoints; pointIndex += 1) {
-            const sourceIndex = pointIndex * 3;
-            const paddedIndex = rowStart + pointIndex * 4;
-            paddedFlatData[paddedIndex] = rowValues[sourceIndex];
-            paddedFlatData[paddedIndex + 1] = rowValues[sourceIndex + 1];
-            paddedFlatData[paddedIndex + 2] = rowValues[sourceIndex + 2];
-            paddedFlatData[paddedIndex + 3] = 0.0;
-        }
+    // due to the way js / webGPU works, we will need to structure our input data into a 1D array, and then place into a buffer, to be copied to a texture
+    // awesomely, the copy function requires that the buffer has a row size (in bytes) that is a multiple of 256
+    // this will generally not be the case, so the 1D array that will go into the buffer must be padded so that there is the 256 multiple
+
+    const actualBytesPerRow = calc_constants.maxNumberOfTimeSeries * 4 * 4; // 4 channels and 4 bytes per float
+    const requiredBytesPerRow = actualBytesPerRow; 
+    const paddedFlatData = new Float32Array(requiredBytesPerRow);
+
+    for (let x = 0; x < calc_constants.maxNumberOfTimeSeries; x++) {
+
+        const paddedIndex = x * 4; 
+
+        paddedFlatData[paddedIndex] = Math.round(calc_constants.locationOfTimeSeries[x].xts / calc_constants.dx);
+        paddedFlatData[paddedIndex + 1] = Math.round(calc_constants.locationOfTimeSeries[x].yts / calc_constants.dy);
+        paddedFlatData[paddedIndex + 2] = 0.0;
+        paddedFlatData[paddedIndex + 3] = 0.0;
     }
 
     const buffer = device.createBuffer({
```

#### CT1-057 측정점 업로드 정렬과 초기상태 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Copy_Data_to_Textures.js:173; 아래 전체 diff의 -행 | ebca435:transect_version/js/Copy_Data_to_Textures.js:209; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 requiredBytesPerRow를 maxNumberOfTimeSeries*16 그대로 둔다. 본판은 256배수로 올림한다. 기본 측정점 수 16에서는 두 값이 같다. 16의 배수가 아닌 수에서는 transect의 복사 정렬과 자기 주석이 모순한다. 초기상태 함수의 writeStateFlag 제거는 별도의 구판 인터페이스 차이다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 188행 포함); `ca9278e` 2026-02-11 (현재 241행 포함); `efe44a2` 2024-04-02 (현재 239행 포함); `151017f` 2026-02-06 (현재 237행 포함); `63a12e3` 2023-10-19 (현재 240행 포함); `32be94a` 2025-10-16 (현재 242행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 225행 포함).

```diff
@@ -173,73 +209,20 @@
     commandEncoder.copyBufferToTexture({
         buffer: buffer,
         bytesPerRow: requiredBytesPerRow,
-        rowsPerImage: textureHeight,
+        rowsPerImage: 1,
     }, {
-        texture: txBoundaryTimeSeries
+        texture: txTimeSeries_Locations
     }, {
-        width: textureWidth,
-        height: textureHeight,
+        width: calc_constants.maxNumberOfTimeSeries,
+        height: 1,
         depthOrArrayLayers: 1
     });
     device.queue.submit([commandEncoder.finish()]);
     buffer.destroy();
 }
-// Added by Codex: End boundary time-series forcing texture upload support.
-
 
-// Copies calc_constants.locationOfTimeSeries[] (x,y indices) into txTimeSeries_Locations.
-function copyTSlocsToTexture(calc_constants, device, txTimeSeries_Locations) {
-  const n = calc_constants.maxNumberOfTimeSeries | 0;
-
-  // RGBA32F per “pixel”: 4 floats = 16 bytes.
-  // due to the way js / webGPU works, we will need to structure our input data into a 1D array, and then place into a buffer, to be copied to a texture
-  // awesomely, the copy function requires that the buffer has a row size (in bytes) that is a multiple of 256
-  // this will generally not be the case, so the 1D array that will go into the buffer must be padded so that there is the 256 multiple
-
-  const bytesPerPixel = 16;
-  const actualBytesPerRow = n * bytesPerPixel;
-
-  // WebGPU requires bytesPerRow to be a multiple of 256 for buffer->texture copies.
-  const bytesPerRow = ((actualBytesPerRow + 255) & ~255) >>> 0;
-
-  // Float count for one row at padded bytesPerRow.
-  const rowFloats = bytesPerRow >>> 2;
-  const data = new Float32Array(rowFloats); // zero initialized; padding stays 0
-
-  const invDx = 1.0 / calc_constants.dx;
-  const invDy = 1.0 / calc_constants.dy;
-  const locs = calc_constants.locationOfTimeSeries;
-
-  for (let i = 0; i < n; i++) {
-    const o = i << 2; // i * 4
-    const p = locs[i];
-    data[o]     = Math.round(p.xts * invDx);
-    data[o + 1] = Math.round(p.yts * invDy);
-    // data[o + 2] and data[o + 3] remain 0
-  }
-
-  const buffer = device.createBuffer({
-    size: data.byteLength,
-    usage: GPUBufferUsage.COPY_SRC | GPUBufferUsage.COPY_DST,
-  });
-
-  // No mapping. Writes from CPU to GPU staging buffer directly.
-  device.queue.writeBuffer(buffer, 0, data.buffer, data.byteOffset, data.byteLength);
-
-  const encoder = device.createCommandEncoder();
-  encoder.copyBufferToTexture(
-    { buffer, bytesPerRow, rowsPerImage: 1 },
-    { texture: txTimeSeries_Locations },
-    { width: n, height: 1, depthOrArrayLayers: 1 }
-  );
 
-  device.queue.submit([encoder.finish()]);
-  buffer.destroy();
-}
-
-
-
-function copyInitialConditionDataToTexture(calc_constants, device, initialState, txState, writeStateFlag) {
+function copyInitialConditionDataToTexture(calc_constants, device, bathy2D, txState) {
     // create and place initial condition into txState
 
     // due to the way js / webGPU works, we will need to structure our input data into a 1D array, and then place into a buffer, to be copied to a texture
```

#### CT1-058 초기 수면과 속도 채널

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Copy_Data_to_Textures.js:253; 아래 전체 diff의 -행 | ebca435:transect_version/js/Copy_Data_to_Textures.js:236; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 writeStateFlag 1/2/3으로 eta/u/v 입력을 구분한다. transect 판은 river_sim==1 또는 loadFriction==1에서만 첫 채널에 입력장을 쓴다. 나머지 두 운동량 채널은 0.0이다. 진폭 0.0인 가우스 식은 유한한 격자에서 0.0이다. |

본판 차이 줄의 마지막 수정: `32be94a` 2025-10-16 (현재 277행 포함); `63a12e3` 2023-10-19 (현재 260행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 252행 포함).

```diff
@@ -253,28 +236,20 @@
     for (let y = 0; y < calc_constants.HEIGHT; y++) {
         for (let x = 0; x < calc_constants.WIDTH; x++) {
 
-             // Testing IC Calculate the differences between the current coordinates and the center
-            //let dx = x - calc_constants.WIDTH / 10.;
-            //let dy = y - calc_constants.HEIGHT / 3.;
-            //let sigma = 24.0;
-
-            var eta = 0.; // * Math.exp(-(dx * dx + dy * dy) / (2 * sigma * sigma));
-            var u = 0.; 
-            var v = 0.; 
-            if (writeStateFlag == 1){
-                eta = initialState[x][y]
-            }
-            else if (writeStateFlag == 2){
-                u = initialState[x][y]
-            }   
-            else if (writeStateFlag == 3){
-                v = initialState[x][y]
+             // Calculate the differences between the current coordinates and the center
+            let dx = x - calc_constants.WIDTH / 10.;
+            let dy = y - calc_constants.HEIGHT / 3.;
+            let sigma = 24.0;
+
+            var eta = 0. * Math.exp(-(dx * dx + dy * dy) / (2 * sigma * sigma));
+            if (calc_constants.river_sim == 1  || calc_constants.loadFriction == 1){
+                eta = bathy2D[x][y]
             }
 
             const paddedIndex = (y * requiredBytesPerRow / 4) + x * 4; // Adjust the index for padding
             paddedFlatData[paddedIndex] = eta;  // red
-            paddedFlatData[paddedIndex + 1] = u;  // green
-            paddedFlatData[paddedIndex + 2] = v;  // blue
+            paddedFlatData[paddedIndex + 1] = 0.0;  // green
+            paddedFlatData[paddedIndex + 2] = 0.0;  // blue
             paddedFlatData[paddedIndex + 3] = 0.0;  // alpha
         }
     }
```

#### CT1-059 구면 계량 업로드 없음

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Copy_Data_to_Textures.js:347; 아래 전체 diff의 -행 | ebca435:transect_version/js/Copy_Data_to_Textures.js:322; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 셀 중심 위도·북쪽 면·남쪽 면의 계량을 RGBA32F로 저장한다. transect 판에는 구면 격자 경로가 없다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 407행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -347,64 +322,6 @@
 
 }
 
-// Added by Codex: Start spherical metric texture upload support.
-function copySphericalMetricDataToTexture(calc_constants, device, txSphericalMetrics) {
-    // copy spherical-grid metric factors into txSphericalMetrics
-    const actualBytesPerRow = calc_constants.WIDTH * 4 * 4; // 4 channels and 4 bytes per float
-    const requiredBytesPerRow = Math.ceil(actualBytesPerRow / 256) * 256;
-    const paddedFlatData = new Float32Array(calc_constants.HEIGHT * requiredBytesPerRow / 4);
-    const degToRad = Math.PI / 180.0;
-    const earthRadius = Math.max(calc_constants.R_earth, 1.0);
-    const oneOverEarthRadius = 1.0 / earthRadius;
-    const dlat = calc_constants.dy;
-
-    for (let y = 0; y < calc_constants.HEIGHT; y++) {
-        // const phiCenter = (calc_constants.lat_LL + y * dlat) * degToRad;
-        // const phiNorthFace = (calc_constants.lat_LL + (y + 0.5) * dlat) * degToRad;
-        // const phiSouthFace = (calc_constants.lat_LL + (y - 0.5) * dlat) * degToRad;
-        // Added by Codex: lat_LL is the lower-left corner, so store cell-center and face metrics inside that corner-defined domain.
-        const phiCenter = (calc_constants.lat_LL + (y + 0.5) * dlat) * degToRad;
-        const phiNorthFace = (calc_constants.lat_LL + (y + 1.0) * dlat) * degToRad;
-        const phiSouthFace = (calc_constants.lat_LL + y * dlat) * degToRad;
-        const cosPhiCenter = Math.cos(phiCenter);
-        const safeCosPhiCenter = Math.sign(cosPhiCenter || 1.0) * Math.max(Math.abs(cosPhiCenter), 1.0e-6);
-        const invRcosPhi = oneOverEarthRadius / safeCosPhiCenter;
-        const cosPhiNorthFace = Math.cos(phiNorthFace);
-        const cosPhiSouthFace = Math.cos(phiSouthFace);
-        const tanPhiOverR = Math.tan(phiCenter) * oneOverEarthRadius;
-
-        for (let x = 0; x < calc_constants.WIDTH; x++) {
-            const paddedIndex = (y * requiredBytesPerRow / 4) + x * 4;
-            paddedFlatData[paddedIndex] = invRcosPhi;
-            paddedFlatData[paddedIndex + 1] = cosPhiNorthFace;
-            paddedFlatData[paddedIndex + 2] = cosPhiSouthFace;
-            paddedFlatData[paddedIndex + 3] = tanPhiOverR;
-        }
-    }
-
-    const buffer = device.createBuffer({
-        size: paddedFlatData.byteLength,
-        usage: GPUBufferUsage.COPY_SRC,
-        mappedAtCreation: true
-    });
-    new Float32Array(buffer.getMappedRange()).set(paddedFlatData);
-    buffer.unmap();
-    const commandEncoder = device.createCommandEncoder();
-    commandEncoder.copyBufferToTexture({
-        buffer: buffer,
-        bytesPerRow: requiredBytesPerRow,
-        rowsPerImage: calc_constants.HEIGHT,
-    }, {
-        texture: txSphericalMetrics
-    }, {
-        width: calc_constants.WIDTH,
-        height: calc_constants.HEIGHT,
-        depthOrArrayLayers: 1
-    });
-    device.queue.submit([commandEncoder.finish()]);
-    buffer.destroy();
-}
-// Added by Codex: End spherical metric texture upload support.
 
 function copyTridiagXDataToTexture(calc_constants, bathy2D, device, coefMatx, bathy2Dvec) {
     // copy Tridiag coef into coefMatx
```

#### CT1-060 업로드 함수 공개 목록

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Copy_Data_to_Textures.js:635; 아래 전체 diff의 -행 | ebca435:transect_version/js/Copy_Data_to_Textures.js:552; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 copyTransectWaveDataToTexture를 export한다. 본판은 경계 시계열과 구면 계량 함수를 export한다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 639행 포함); `bb99fee` 2026-07-02 (현재 642행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 555행 포함).

```diff
@@ -635,8 +552,4 @@
 
 
 
-// export { copyBathyDataToTexture, copyWaveDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture};
-// Added by Codex: Export spherical metric upload helper for grid_type == 2.
-// export { copyBathyDataToTexture, copyWaveDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copySphericalMetricDataToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture};
-// Added by Codex: Export boundary time-series forcing texture upload helper.
-export { copyBathyDataToTexture, copyWaveDataToTexture, copyBoundaryTimeSeriesDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copySphericalMetricDataToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture};
+export { copyBathyDataToTexture, copyTransectWaveDataToTexture, copyWaveDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture};
```


### 2.3 index.html

본판: `index.html`. transect 판: `transect_version/index.html`.
원래 diff는 3055행이다. CR 제외 diff는 23구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `c4be488` | 2026-07-13 | allow multiple nested grids |
| 본판 | `bb99fee` | 2026-07-02 | Added grid nesting |
| 본판 | `afc1fe7` | 2026-06-19 | Added Spherical NLSW Solver, Japan 2011 example |
| 본판 | `d778fe7` | 2026-06-02 | Added linear structures functionality |
| 본판 | `9093d7f` | 2026-06-01 | added ability to change wave conditions through the UI - on the Modify Boundary Conditions Panel |
| 본판 | `794c808` | 2026-04-06 | updated forum link |
| 본판 | `ea93d70` | 2025-10-24 | added Yakutat, Sebastian Inlet examples, and "p" for pause |
| 본판 | `32be94a` | 2025-10-16 | hot start initial condition option added |
| 본판 | `146a4ac` | 2025-09-28 | added Tracy Arm hot start |
| 본판 | `8c2b62b` | 2025-08-24 | Added Tracy Arm Example, some landslide viz additions |
| 본판 | `853c27d` | 2025-08-11 | added Endicott slide example |
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| 본판 | `2a7452d` | 2025-06-07 | Sed Trans updates |
| 본판 | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |
| transect | `3d8a61b` | 2025-06-14 | Added many-transect version |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-061 페이지 제목

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:5; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:5; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 제목에 Transect Mode를 표시한다. |

본판 차이 줄의 마지막 수정: `cf9de63` 2023-10-24 (현재 8행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 8행 포함).

```diff
@@ -5,7 +5,7 @@
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
 
-    <title>Celeris-WebGPU</title>
+    <title>Celeris-WebGPU: Transect Mode</title>
     <style>
         /* Add internal CSS here (or you could link to an external stylesheet) */
         #main-container {
```

#### CT1-062 경계 파일 UI 스타일

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:117; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:117; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 경계 시계열 업로드 행의 CSS를 정의한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 132행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -117,19 +117,6 @@
            border-color: #030303; /* slightly darker border for hover */
         }
 
-        /* Added by Codex: Start compact boundary time-series upload controls. */
-        .boundary-time-series-upload-row {
-            display: flex;
-            flex-wrap: wrap;
-            gap: 4px;
-            align-items: center;
-        }
-
-        .boundary-time-series-upload-row .custom-file-upload-button {
-            max-width: 145px;
-        }
-        /* Added by Codex: End compact boundary time-series upload controls. */
-
         .custom-window {
             border: 1px solid #ccc;
             border-radius: 5px;
```

#### CT1-063 사용자 포럼 링크

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:201; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:188; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 discourse 주소를 쓴다. transect 판은 sqrtgh 포럼 주소를 쓴다. 링크 문자열만 대조하며 외부 사이트 내용은 판독하지 않는다. |

본판 차이 줄의 마지막 수정: `794c808` 2026-04-06 (현재 204행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 191행 포함).

```diff
@@ -201,7 +188,7 @@
                 </div>
                 <div class="window-content">
                     <html4f>
-                        <b>Questions/Problems/Requests </b> - use the <a href="https://celeris.discourse.group/categories" target="_blank" rel="noopener noreferrer">Users Forum</a>
+                        <b>Questions/Problems/Requests </b> - use the <a href="https://www.sqrtgh.com/forum" target="_blank" rel="noopener noreferrer">Users Forum</a>
                         <br />
                         <b>NOTE:</b> Options with an asterisk* are not currently working - these are largely placeholders for future updates.
                         <br />
```

#### CT1-064 추가 입력 파일

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:235; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:222; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 초기 수면·hardbottom·4변 경계 시계열 업로드와 자료 형식 안내를 제공한다. 마찰 파일 입력은 양쪽에 남아 있다. |

본판 차이 줄의 마지막 수정: `32be94a` 2025-10-16 (현재 243행 포함); `b8b50c3` 2025-06-08 (현재 255행 포함); `bb99fee` 2026-07-02 (현재 281행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -235,50 +222,12 @@
                         </label>
                         <br />
                         <br />
-                        <input type="file" id="etaInitialConditionFile" accept="application/txt" style="display: none;" />
-                        <label for="etaInitialConditionFile" class="custom-file-upload-button">
-                            Load Initial Free Surface Data File [Optional]
-                        </label>
-                        <br />
-                        <br />
                         <input type="file" id="frictionmapFile" accept="application/txt" style="display: none;" />
                         <label for="frictionmapFile" class="custom-file-upload-button">
                             Load Friction Map Data File [Optional]
                         </label>
                         <br />
                         <br />
-                        <input type="file" id="hardbottomFile" accept="application/txt" style="display: none;" />
-                        <label for="hardbottomFile" class="custom-file-upload-button">
-                            Load Hard (non-erodible) Bottom Elevation Data File [Optional]
-                        </label>
-                        <br />
-                        <br />
-                        <!-- Added by Codex: Start boundary time-series upload inputs. -->
-                        <html4f>
-                            Boundary time-series files can be loaded for boundary type 5 and should contain station locations plus time, eta, hu, and hv columns.  
-                            See the Users Forum for details on how to construct these OPTIONAL boundary time series files.
-                        </html4f>
-                        <br />
-                        <div class="boundary-time-series-upload-row">
-                            <input type="file" id="westBoundaryTimeSeriesFile" accept="application/txt,.txt" style="display: none;" />
-                            <label for="westBoundaryTimeSeriesFile" class="custom-file-upload-button">
-                                Load West Boundary File
-                            </label>
-                            <input type="file" id="eastBoundaryTimeSeriesFile" accept="application/txt,.txt" style="display: none;" />
-                            <label for="eastBoundaryTimeSeriesFile" class="custom-file-upload-button">
-                                Load East Boundary File
-                            </label>
-                            <input type="file" id="southBoundaryTimeSeriesFile" accept="application/txt,.txt" style="display: none;" />
-                            <label for="southBoundaryTimeSeriesFile" class="custom-file-upload-button">
-                                Load South Boundary File
-                            </label>
-                            <input type="file" id="northBoundaryTimeSeriesFile" accept="application/txt,.txt" style="display: none;" />
-                            <label for="northBoundaryTimeSeriesFile" class="custom-file-upload-button">
-                                Load North Boundary File
-                            </label>
-                        </div>
-                        <br />
-                        <!-- Added by Codex: End boundary time-series upload inputs. -->
                         <html4f>
                             For image overlay, you have two choices.  
                             If you have a high-resolution satellite or aerial image, you can load that file below.
```

#### CT1-065 예제 선택 숨김

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:308; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:257; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 예제 label과 select를 display:none으로 숨긴다. |

본판 차이 줄의 마지막 수정: `0dd009e` 2024-03-21 (현재 318행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 263행 포함).

```diff
@@ -308,14 +257,10 @@
                         <button id="start-simulation-btn">Start Simulation</button>
                         <br />
                         <br />
-                        <html4f>
-                            ---------------------- <br>
-                            or, Load Pre-configured Examples here:</a>
-                        </html4f>
                         <!-- run example simulation using server-side configurations files-->
                          <!-- Updates go to calc_constants.simPause-->
-                         <label for="run_example-select">Choose Example:</label>
-                         <select id="run_example-select" name="run_exampleValue">
+                         <label style="display: none;" for="run_example-select">Choose Example:</label>
+                         <select style="display: none;" id="run_example-select" name="run_exampleValue">
                              <option value="0">Ventura Harbor (CA), wind waves</option>
                              <option value="27">Hermosa Beach (CA), wind waves</option>
                              <option value="37">Hermosa Beach (CA), High-Order mode</option>
```

#### CT1-066 예제 선택 항목

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:334; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:279; 아래 전체 diff의 +행 | 불일치 (A) | 본판의 후속 예제 option이 transect 판에는 없다. 예제 내부 자료는 판독하지 않는다. |

본판 차이 줄의 마지막 수정: `ea93d70` 2025-10-24 (현재 349행 포함); `afc1fe7` 2026-06-19 (현재 342행 포함); `8c2b62b` 2025-08-24 (현재 347행 포함); `146a4ac` 2025-09-28 (현재 348행 포함); `32be94a` 2025-10-16 (현재 352행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -334,22 +279,16 @@
                              <option value="21">Waimea Bay (HI), wind waves</option>
                              <option value="24">Ipan Reef (Guam), wind waves</option>
                              <option value="5">FRF Duck (NC), wind waves</option>
-                             <option value="42">Sebastian Inlet (FL), wind waves</option>
                              <option value="9">Miami Beach (FL), wind waves</option>
                              <option value="10">Miami Inlet (FL), wind waves</option>
                              <option value="22">Tyndall AFB (FL), wind waves</option>
                              <option value="8">Hania (Crete) Harbor, wind waves</option>
-                             <option value="54">Japan tsunami, spherical coords</option>
                              <option value="2">Santa Cruz Harbor (CA), tsunami</option>
                              <option value="4">Crescent City Harbor (CA), tsunami</option>
                              <option value="12">Port of LA/LB (CA), tsunami</option>
                              <option value="13">Santa Barbara (CA), tsunami</option>
-                             <option value="38">Tracy Arm (AK), tsunami</option>
-                             <option value="39">Tracy Arm (AK), hot start</option>
-                             <option value="41">Yakutat Bay (AK), tsunami</option>
                              <option value="14">Taan Fjord (AK), tsunami</option>
                              <option value="34">Portage Lake (AK), tsunami</option>
-                             <option value="40">Portage Lake & River (AK), tsunami</option>
                              <option value="3">Barry Arm (PWS, AK), tsunami</option>
                              <option value="6">Greenland (Karrat), tsunami</option>
                              <option value="35">Greenland (Umanak), tsunami</option>
```

#### CT1-067 예제 실행 버튼 숨김

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:358; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:297; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 예제 실행 버튼을 숨긴다. 직접 파일 입력 실행은 남긴다. |

본판 차이 줄의 마지막 수정: `0dd009e` 2024-03-21 (현재 371행 포함); `2eb2866` 2023-10-26 (현재 367행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 302행 포함); `3d8a61b` 2025-06-14 (현재 301행 포함).

```diff
@@ -358,17 +297,9 @@
                              <option value="15">OSU Directional Wave Basin</option>
                              <option value="17">OSU Seaside Experiments (2007) </option>
                              <option value="30">Toy Problem, wind waves</option>
-                         </select>
-                         <br />
-                         <br />                        
-                        <button id="run-example-simulation-btn">Run Example Simulation</button>
-                        <br />
-                        <br />
-      
-                        <html4f>
-                            ----------------------
-                        </html4f>
-                        <br />
+                         </select>                     
+                        <button style="display: none;" id="run-example-simulation-btn">Run Example Simulation</button>
+    
                          <!-- Updates go to calc_constants.simPause-->
                          <label for="simPause-select">Pause / Resume Simulation:</label>
                          <select id="simPause-select" name="simPauseValue">
```

#### CT1-068 가용 깊이 표시 항목

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:420; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:351; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 surfaceToPlot 19를 제공한다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 423행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -420,7 +351,6 @@
                         <option value="21">Depth Change due to Sed Transport </option>
                         <option value="17">Sediment Class 1 Concentration </option>
                         <option value="18">Sediment Class 1 Erosion Rate </option>
-                        <option value="19">Sediment Class 1 Available Depth </option>
                         <option value="22">Design Component Map </option>
                     </select>
                     <br />
```

#### CT1-069 천단고 UI 활성 상태

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:625; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:555; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 별표를 붙여 미지원임을 표시한다. 본판은 실제 선형 구조물 경로를 구현한다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 628행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 558행 포함).

```diff
@@ -625,7 +555,7 @@
                     
 
                     <!-- Updates go to calc_constants.designcomponent_CrestElev-->
-                    <label for="designcomponent_CrestElev-input">For linear structures (breakwaters, dunes, seawalls), crest elevation (m):</label>
+                    <label for="designcomponent_CrestElev-input">*For linear structures (breakwaters, dunes, seawalls), crest elevation (m):</label>
                     <br />
                     <input type="number" id="designcomponent_CrestElev-input" name="designcomponent_CrestElevValue">
                     <button id="designcomponent_CrestElev-button" type="button">Update</button>
```

#### CT1-070 천단폭 UI 활성 상태

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:633; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:563; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 별표를 붙인다. 본판은 해당 폭을 실제 지형 편집에 쓴다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 636행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 566행 포함).

```diff
@@ -633,7 +563,7 @@
                     <br />
 
                     <!-- Updates go to calc_constants.designcomponent_CrestWidth-->
-                    <label for="designcomponent_CrestWidth-input">For linear structures (breakwaters, dunes, seawalls), crest width (m):</label>
+                    <label for="designcomponent_CrestWidth-input">*For linear structures (breakwaters, dunes, seawalls), crest width (m):</label>
                     <br />
                     <input type="number" id="designcomponent_CrestWidth-input" name="designcomponent_CrestWidthValue">
                     <button id="designcomponent_CrestWidth-button" type="button">Update</button>
```

#### CT1-071 사면경사 UI 활성 상태

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:641; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:571; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 별표를 붙인다. 두 판의 안내 예시 0.25=1/4는 같다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 644행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 574행 포함).

```diff
@@ -641,7 +571,7 @@
                     <br />
 
                     <!-- Updates go to calc_constants.designcomponent_SideSlope-->
-                    <label for="designcomponent_SideSlope-input">For linear, sloping structures (breakwaters, dunes), side slope (give as decimal, e.g. 0.25 = 1/4):</label>
+                    <label for="designcomponent_SideSlope-input">*For linear, sloping structures (breakwaters, dunes), side slope (give as decimal, e.g. 0.25 = 1/4):</label>
                     <br />
                     <input type="number" id="designcomponent_SideSlope-input" name="designcomponent_SideSlopeValue">
                     <button id="designcomponent_SideSlope-button" type="button">Update</button>
```

#### CT1-072 끝점 선택 UI 활성 상태

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:649; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:579; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 별표를 붙인다. 본판은 끝점 선택을 실제 편집에 연결한다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 652행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 582행 포함).

```diff
@@ -649,7 +579,7 @@
                     <br />
 
                     <!-- Updates go to calc_constants.designcomponent_CurrentEndPoint-->
-                    <label for="designcomponent_CurrentEndPoint-select">Choose Linear Structure Start/Endpoint Coordinate to Edit:</label>
+                    <label for="designcomponent_CurrentEndPoint-select">*Choose Linear Structure Start/Endpoint Coordinate to Edit:</label>
                     <select id="designcomponent_CurrentEndPoint-select" name="designcomponent_CurrentEndPointValue">
                         <option value="1">Start Location</option>
                         <option value="2">End Location</option>
```

#### CT1-073 끝점 입력 안내

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:658; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:588; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 우클릭 입력 안내에 별표를 붙인다. 실제 선형 구조물 적용 경로는 없다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 661행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 591행 포함).

```diff
@@ -658,7 +588,7 @@
                     <br />
                     
                     <html4f>
-                        Right-click on structure start/end location (in Design Mode) or input coordinates below</a>
+                        *Right-click on structure start/end location (in Design Mode) or input coordinates below</a>
                     </html4f> 
                     <br />
                     <br />
```

#### CT1-074 내장 파 생성 UI

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:761; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:691; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 Sine와 TMA에 별표를 붙인다. 본판은 공유 파 생성 모듈을 호출한다. pulse 안내의 4 waves 문자열은 양쪽에 남아 있다. |

본판 차이 줄의 마지막 수정: `9093d7f` 2026-06-01 (현재 765행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 695행 포함).

```diff
@@ -761,8 +691,8 @@
                     <!-- Updates go to calc_constants.incident_wave_type-->
                     <label for="incident_wave_type-select">Incident Wave Type: </label>
                     <select id="incident_wave_type-select" name="incident_wave_typeValue">
-                        <option value="0">Sine Wave (single harmonic)</option>
-                        <option value="1">TMA Spectrum</option>
+                        <option value="0">*Sine Wave (single harmonic)</option>
+                        <option value="1">*TMA Spectrum</option>
                         <option value="2">*Transient Pulse (4 waves)</option>
                         <option value="3">*Solitary Wave</option>
                         <option value="-1">Custom Spectrum from loaded file</option>
```

#### CT1-075 입사 방향 문구

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:788; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:718; 아래 전체 diff의 +행 | 불일치 (F) | 본판의 0=from west·90=from south는 양의 진행축이 동·북인 관례다. transect 문구의 CCW from E는 같은 진행 방향 관례다. 실제 단면 파일 방향 채널은 별도로 0.0으로 고정한다. |

본판 차이 줄의 마지막 수정: `9093d7f` 2026-06-01 (현재 791행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 721행 포함).

```diff
@@ -788,7 +718,7 @@
                     <br />
 
                     <!-- Updates go to calc_constants.incident_wave_direction-->
-                    <label for="incident_wave_direction-input">Wave Direction (deg, 0=from west, 90=from south, 180=from east, -90/270=from north):</label>
+                    <label for="incident_wave_direction-input">Wave Direction (deg CCW from E [-180 to 180]):</label>
                     <br />
                     <input type="number" id="incident_wave_direction-input" name="incident_wave_direction">
                     <button id="incident_wave_direction-button" type="button">Update</button>
```

#### CT1-076 서쪽 type5 UI

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:802; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:732; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 파일 시계열 경계를 선택할 수 있다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 806행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -802,8 +732,6 @@
                         <option value="1">Sponge Layer</option>
                         <option value="2">Incident Waves</option>
                         <option value="3">*Periodic Boundary</option>
-                        <!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->
-                        <option value="5">Time Series from loaded file</option>
                     </select>
                     <br />
                     <br />
```

#### CT1-077 동쪽 type5 UI

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:815; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:743; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 파일 시계열 경계를 선택할 수 있다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 819행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -815,8 +743,6 @@
                         <option value="1">Sponge Layer</option>
                         <option value="2">Incident Waves</option>
                         <option value="3">*Periodic Boundary</option>
-                        <!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->
-                        <option value="5">Time Series from loaded file</option>
                     </select>
                     <br />
                     <br />
```

#### CT1-078 남쪽 type5 UI

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:828; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:754; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 파일 시계열 경계를 선택할 수 있다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 832행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -828,8 +754,6 @@
                         <option value="1">Sponge Layer</option>
                         <option value="2">Incident Waves</option>
                         <option value="3">*Periodic Boundary</option>
-                        <!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->
-                        <option value="5">Time Series from loaded file</option>
                     </select>
                     <br />
                     <br />
```

#### CT1-079 북쪽 type5 UI

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:841; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:765; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 파일 시계열 경계를 선택할 수 있다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 845행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -841,8 +765,6 @@
                         <option value="1">Sponge Layer</option>
                         <option value="2">Incident Waves</option>
                         <option value="3">*Periodic Boundary</option>
-                        <!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->
-                        <option value="5">Time Series from loaded file</option>
                     </select>
                     <br />
                     <br />
```

#### CT1-080 퇴적물 되먹임 안내

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:860; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:782; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 BETA - currently no feedback w/ hydro라고 명시한다. 바닥고 고정은 이 안내에 맞는 의도된 처리다. |

본판 차이 줄의 마지막 수정: 추가·삭제 줄 없음. transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 790행 포함).

```diff
@@ -860,6 +782,12 @@
                     <button class="minimize-button">-</button>
                 </div>
                 <div class="window-content"  data-default="minimized">
+
+                    <html4f>
+                    BETA - currently no feedback w/ hydro
+                    </html4f>
+                    <br />
+                    <br />
                     <!-- Updates go to calc_constants.sedC1_d50-->
                     <label for="sedC1_d50-input">Sediment Class 1 D50 (mm):</label>
                     <br />
```

#### CT1-081 퇴적물 psi 문구

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:882; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:810; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 erosion이라는 괄호 설명을 생략한다. 같은 sedC1_psi 입력과 기본값을 가리킨다. |

본판 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 885행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 813행 포함).

```diff
@@ -882,7 +810,7 @@
                     <br />
                     <br />                 
                    <!-- Updates go to calc_constants.sedC1_psi-->
-                   <label for="sedC1_psi-input">Sediment Class 1 psi (erosion) parameter:</label>
+                   <label for="sedC1_psi-input">Sediment Class 1 psi parameter:</label>
                    <br />
                    <input type="number" id="sedC1_psi-input" name="sedC1_psiValue">
                    <button id="sedC1_psi-button" type="button">Update</button>
```

#### CT1-082 중첩 경계 출력 UI

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:1311; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:1239; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 0기반 사각형 인덱스·기간·간격·eta 임계값·실행 버튼을 제공한다. 다중 사각형은 JSON으로 추가한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 1367행 포함); `c4be488` 2026-07-13 (현재 1328행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -1311,60 +1239,6 @@
                     <br />
                     <br />
 
-                    <!-- Added by Codex: Start nested-grid boundary time-series output controls. -->
-                    <html4f> Nested Grid Boundary Time Series Output Options: </html4f>
-                    <br />
-                    <html4f>
-                    Define a rectangle using 0-based lower-left and upper-right grid indices. The four rectangle edges
-                    will be saved as eta/hu/hv time-series boundary files for one-way nested grids.
-                    </html4f>
-                    <br />
-                    <!-- Added by Codex: Start multi-rectangle nested-grid output note. -->
-                    <html4f>
-                    These controls edit the legacy/first rectangle. Additional rectangles can be supplied in config.json
-                    with nestedGridOutput_rectangles; default output prefixes are gridD, gridD2, gridD3, etc.
-                    </html4f>
-                    <br />
-                    <!-- Added by Codex: End multi-rectangle nested-grid output note. -->
-                    <label for="nestedGridOutput_i0-input">Lower-left i-index:</label>
-                    <input type="number" id="nestedGridOutput_i0-input" name="nestedGridOutput_i0Value" min="0" step="1">
-                    <button id="nestedGridOutput_i0-button" type="button">Update</button>
-                    <br />
-                    <label for="nestedGridOutput_j0-input">Lower-left j-index:</label>
-                    <input type="number" id="nestedGridOutput_j0-input" name="nestedGridOutput_j0Value" min="0" step="1">
-                    <button id="nestedGridOutput_j0-button" type="button">Update</button>
-                    <br />
-                    <label for="nestedGridOutput_i1-input">Upper-right i-index:</label>
-                    <input type="number" id="nestedGridOutput_i1-input" name="nestedGridOutput_i1Value" min="0" step="1">
-                    <button id="nestedGridOutput_i1-button" type="button">Update</button>
-                    <br />
-                    <label for="nestedGridOutput_j1-input">Upper-right j-index:</label>
-                    <input type="number" id="nestedGridOutput_j1-input" name="nestedGridOutput_j1Value" min="0" step="1">
-                    <button id="nestedGridOutput_j1-button" type="button">Update</button>
-                    <br />
-                    <label for="nestedGridOutput_start_time-input">Start output time (sec):</label>
-                    <input type="number" id="nestedGridOutput_start_time-input" name="nestedGridOutput_start_timeValue">
-                    <button id="nestedGridOutput_start_time-button" type="button">Update</button>
-                    <br />
-                    <label for="nestedGridOutput_end_time-input">End output time (sec):</label>
-                    <input type="number" id="nestedGridOutput_end_time-input" name="nestedGridOutput_end_timeValue">
-                    <button id="nestedGridOutput_end_time-button" type="button">Update</button>
-                    <br />
-                    <label for="nestedGridOutput_dt-input">Output interval (sec):</label>
-                    <input type="number" id="nestedGridOutput_dt-input" name="nestedGridOutput_dtValue" min="0">
-                    <button id="nestedGridOutput_dt-button" type="button">Update</button>
-                    <br />
-                    <!-- Added by Codex: Start nested-grid quiet-period trim threshold control. -->
-                    <label for="nestedEtaWriteThreshold-input">Eta write threshold (m):</label>
-                    <input type="number" id="nestedEtaWriteThreshold-input" name="nestedEtaWriteThresholdValue" min="0" step="0.001">
-                    <button id="nestedEtaWriteThreshold-button" type="button">Update</button>
-                    <br />
-                    <!-- Added by Codex: End nested-grid quiet-period trim threshold control. -->
-                    <button id="startNestedGridOutput-button">Start Nested Grid Boundary Time Series Output</button>
-                    <br />
-                    <br />
-                    <!-- Added by Codex: End nested-grid boundary time-series output controls. -->
-
                 </div>
 
             </div>
```

#### CT1-083 모듈 진입 경로

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:index.html:1594; 아래 전체 diff의 -행 | ebca435:transect_version/index.html:1468; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 /transect_version/js/main.js를 로드한다. 본판은 상대 js/main.js를 로드한다. 루트 아래 배포를 가정하는 차이다. |

본판 차이 줄의 마지막 수정: `fd57bb7` 2023-10-09 (현재 1597행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 1471행 포함).

```diff
@@ -1594,7 +1468,7 @@
     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
 
     <!-- Wave solution control script - everything runs from this -->
-    <script type="module" src="js/main.js"></script>
+    <script type="module" src="/transect_version/js/main.js"></script>
  
     
 </body>
```


### 2.4 js/File_Loader.js

본판: `js/File_Loader.js`. transect 판: `transect_version/js/File_Loader.js`.
원래 diff는 1291행이다. CR 제외 diff는 4구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `bb99fee` | 2026-07-02 | Added grid nesting |
| 본판 | `bf8db50` | 2026-05-24 | Localhost debug and overlay bug fixes |
| 본판 | `32be94a` | 2025-10-16 | hot start initial condition option added |
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| transect | `3d8a61b` | 2025-06-14 | Added many-transect version |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-084 초기 수면 파일 읽기

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Loader.js:82; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Loader.js:82; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 etaInitCond.txt를 WIDTH열·HEIGHT행의 NaN을 검사하는 수치장으로 읽는다. transect 판에는 이 함수가 없다. |

본판 차이 줄의 마지막 수정: `32be94a` 2025-10-16 (현재 144행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -82,66 +82,6 @@
 }
 
 
-// load initial condition file
-export async function loadInitCondSurface(InitCondContent, calc_constants) {
-    let response;
-    let lines;
-    let filePath;
-    // Try to parse the uploaded content, if fails, then load server side file
-    try {
-
-        lines = InitCondContent.split('\n');
-
-        console.log("Initial Condition data loaded successfully from the uploaded file.");
-
-    } catch (error) {
-        console.log("Loading server side example initial condition file");
-        filePath = calc_constants.exampleDirs[calc_constants.run_example] + 'etaInitCond.txt';
-        try {
-            response = await fetch(filePath);
-        } catch (error) {
-            console.error("Could not find initial condition file at " + filePath);
-            return null;
-        }
-
-        if (!response.ok) {
-            console.error("Error fetching initial condition file:", response.statusText);
-            return null;
-        }
-
-        const fileContents = await response.text();
-
-        lines = fileContents.split('\n');
-        console.log("Server side initial condition data loaded successfully.");
-    }
-
-    const InitCond2D = Array.from({ length: calc_constants.WIDTH }, () => Array(calc_constants.HEIGHT));
-
-    // Parse the depth data.
-    for (let y = 0; y < calc_constants.HEIGHT; y++) {
-        // Split each line by spaces or tabs.
-        const InitCondValues = lines[y].split(/\s+/).filter(Boolean);
-
-        if (InitCondValues.length !== calc_constants.WIDTH) {
-            console.error("Initial Condition file at " + filePath + " is not in the correct format.");
-            return null;
-        }
-
-        for (let x = 0; x < calc_constants.WIDTH; x++) {
-            const parsedValue = parseFloat(InitCondValues[x]);
-            if (isNaN(parsedValue)) {
-                console.error(`Could not parse initial condition value at [${x}, ${y}] in initial condition file at ${filePath}`);
-                return null;
-            }
-            InitCond2D[x][y] = parsedValue;
-        }
-    }
-
-    console.log("Initial Condition data parsed successfully.");
-
-    return InitCond2D;
-}
-
 // load friction file
 export async function loadFrictionSurface(frictionContent, calc_constants) {
     let response;
```

#### CT1-085 hardbottom과 단면 파랑의 서로 다른 자료 형식

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Loader.js:202; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Loader.js:142; 아래 전체 diff의 +행 | 코드에만 (C) | 본판 함수는 hardbottom.txt의 WIDTH×HEIGHT 고도를 읽는다. transect 함수는 waves.txt의 numberOfWaves열·3*HEIGHT행을 읽는다. 두 함수는 열 수와 반환 배열 크기가 다르다. |

본판 차이 줄의 마지막 수정: `e239ace` 2025-05-18 (현재 205행 포함); `b8b50c3` 2025-06-08 (현재 263행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 202행 포함); `22e1983` 2025-06-06 (현재 205행 포함).

```diff
@@ -202,67 +142,67 @@
     return friction2D;
 }
 
-
-// load hard bottom file
-export async function loadHardBottomSurface(fileContent, calc_constants) {
+// load transect wave data
+export async function loadTransectWaveData(waveContent, calc_constants) {
     let response;
     let lines;
     let filePath;
     // Try to parse the uploaded content, if fails, then load server side file
     try {
 
-        lines = fileContent.split('\n');
+        lines = waveContent.split('\n');
 
-        console.log("Hard Bottom data loaded successfully from the uploaded file.");
+        console.log("Transect Wave data loaded successfully from the uploaded file.");
 
     } catch (error) {
-        console.log("Loading server side example hard bottom file");
-        filePath = calc_constants.exampleDirs[calc_constants.run_example] + 'hardbottom.txt';
+        console.log("Loading server side example transect wave file");
+        filePath = calc_constants.exampleDirs[calc_constants.run_example] + 'waves.txt';
         try {
             response = await fetch(filePath);
         } catch (error) {
-            console.error("Could not find hard bottom file at " + filePath);
+            console.error("Could not find transect wave file at " + filePath);
             return null;
         }
 
         if (!response.ok) {
-            console.error("Error fetching hard bottom file:", response.statusText);
+            console.error("Error fetching transect wave file:", response.statusText);
             return null;
         }
 
         const fileContents = await response.text();
 
         lines = fileContents.split('\n');
-        console.log("Server side hard bottom data loaded successfully.");
+        console.log("Server side transect wave data loaded successfully.");
     }
 
-    const filedata2D = Array.from({ length: calc_constants.WIDTH }, () => Array(calc_constants.HEIGHT));
+    const TransectWaves = Array.from({ length: calc_constants.numberOfWaves }, () => Array(3 * calc_constants.HEIGHT));
 
     // Parse the depth data.
-    for (let y = 0; y < calc_constants.HEIGHT; y++) {
+    for (let y = 0; y < 3 * calc_constants.HEIGHT; y++) {
         // Split each line by spaces or tabs.
-        const hardbottomValues = lines[y].split(/\s+/).filter(Boolean);
+        const TransectWavesValues = lines[y].split(/\s+/).filter(Boolean);
 
-        if (hardbottomValues.length !== calc_constants.WIDTH) {
-            console.error("Hard bottom file at " + filePath + " is not in the correct format.");
+        if (TransectWavesValues.length !== calc_constants.numberOfWaves) {
+            console.error("Transect wave file at " + filePath + " is not in the correct format.");
             return null;
         }
 
-        for (let x = 0; x < calc_constants.WIDTH; x++) {
-            const parsedValue = parseFloat(hardbottomValues[x]);
+        for (let x = 0; x < calc_constants.numberOfWaves; x++) {
+            const parsedValue = parseFloat(TransectWavesValues[x]);
             if (isNaN(parsedValue)) {
-                console.error(`Could not parse hard bottom value at [${x}, ${y}] in file at ${filePath}`);
+                console.error(`Could not parse transect wave value at [${x}, ${y}] in transect wave file at ${filePath}`);
                 return null;
             }
-            filedata2D[x][y] = parsedValue;
+            TransectWaves[x][y] = parsedValue;
         }
     }
 
-    console.log("Hard bottom data parsed successfully.");
+    console.log("Transect wave data parsed successfully.");
 
-    return filedata2D;
+    return TransectWaves;
 }
 
+
 // load wave data
 export async function loadWaveData(waveContent, calc_constants) {
     let lines;
```

#### CT1-086 type-5 경계 자료 검사

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Loader.js:300; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Loader.js:240; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 주석 제거·관측점 수·좌표 정렬·중복 검사·1+3*N 열 검사·시간 단조증가·공유 시간벡터 오차 검사·업로드 우선을 구현한다. transect 판에는 해당 경계 자료 경로가 없다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 513행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -300,217 +240,6 @@
     }
 }
 
-// Added by Codex: Start boundary time-series forcing loaders.
-function createEmptyBoundaryTimeSeriesSide() {
-    return {
-        active: false,
-        numPoints: 0,
-        numTimes: 0,
-        textureWidth: 1,
-        textureHeight: 1,
-        locations: [],
-        times: [],
-        values: []
-    };
-}
-
-function cleanBoundaryTimeSeriesLines(fileContents) {
-    return fileContents
-        .split(/\r?\n/)
-        .map(line => line.replace(/\/\/.*$/g, "").replace(/%.*$/g, "").replace(/#.*$/g, "").trim())
-        .filter(line => line.length > 0);
-}
-
-function parseBoundaryTimeSeriesNumericLine(line, filePath, lineNumber) {
-    const values = line.split(/\s+/).filter(Boolean).map(Number);
-    if (values.some(value => !Number.isFinite(value))) {
-        throw new Error(`Could not parse numeric values in ${filePath} at data line ${lineNumber}.`);
-    }
-    return values;
-}
-
-function parseBoundaryTimeSeriesCountLine(line, filePath) {
-    const numericTokens = line.split(/\s+/).filter(Boolean).map(Number).filter(value => Number.isFinite(value));
-    if (numericTokens.length < 1) {
-        throw new Error(`Boundary time-series file ${filePath} must start with a station count.`);
-    }
-    return parseInt(numericTokens[numericTokens.length - 1], 10);
-}
-
-function resolveBoundaryTimeSeriesFilePath(calc_constants, fileName) {
-    if (/^(https?:|\.\/|\/)/i.test(fileName)) {
-        return fileName;
-    }
-    if (calc_constants.run_example >= 0 && calc_constants.exampleDirs && calc_constants.exampleDirs[calc_constants.run_example]) {
-        return calc_constants.exampleDirs[calc_constants.run_example] + fileName;
-    }
-    return fileName;
-}
-
-function parseBoundaryTimeSeriesText(fileContents, side, filePath) {
-    const lines = cleanBoundaryTimeSeriesLines(fileContents);
-    if (lines.length < 3) {
-        throw new Error(`Boundary time-series file ${filePath} does not contain enough data.`);
-    }
-
-    // const countTokens = parseBoundaryTimeSeriesNumericLine(lines[0], filePath, 1);
-    // const numPoints = parseInt(countTokens[countTokens.length - 1], 10);
-    // Added by Codex: Allow either "3" or a labeled first line such as "number_of_ts_along_boundary 3".
-    const numPoints = parseBoundaryTimeSeriesCountLine(lines[0], filePath);
-    if (!Number.isInteger(numPoints) || numPoints < 1) {
-        throw new Error(`Boundary time-series file ${filePath} must start with a positive station count.`);
-    }
-
-    const locations = [];
-    let lineIndex = 1;
-    while (locations.length < numPoints && lineIndex < lines.length) {
-        const locationTokens = parseBoundaryTimeSeriesNumericLine(lines[lineIndex], filePath, lineIndex + 1);
-        if (locations.length + locationTokens.length > numPoints) {
-            throw new Error(`Boundary time-series file ${filePath} has too many location values before the data rows.`);
-        }
-        locations.push(...locationTokens);
-        lineIndex += 1;
-    }
-    if (locations.length != numPoints) {
-        throw new Error(`Boundary time-series file ${filePath} did not provide ${numPoints} station locations.`);
-    }
-
-    const expectedColumns = 1 + 3 * numPoints;
-    const times = [];
-    const values = [];
-    for (; lineIndex < lines.length; lineIndex += 1) {
-        const row = parseBoundaryTimeSeriesNumericLine(lines[lineIndex], filePath, lineIndex + 1);
-        if (row.length != expectedColumns) {
-            throw new Error(`Boundary time-series file ${filePath} row ${lineIndex + 1} has ${row.length} columns; expected ${expectedColumns}.`);
-        }
-        times.push(row[0]);
-        const rowValues = [];
-        for (let pointIndex = 0; pointIndex < numPoints; pointIndex += 1) {
-            const sourceIndex = 1 + pointIndex * 3;
-            rowValues.push(row[sourceIndex], row[sourceIndex + 1], row[sourceIndex + 2]);
-        }
-        values.push(rowValues);
-    }
-
-    if (times.length < 1) {
-        throw new Error(`Boundary time-series file ${filePath} does not contain any time rows.`);
-    }
-    for (let timeIndex = 1; timeIndex < times.length; timeIndex += 1) {
-        if (times[timeIndex] <= times[timeIndex - 1]) {
-            throw new Error(`Boundary time-series file ${filePath} time values must be strictly increasing.`);
-        }
-    }
-
-    const sortedLocations = locations.map((location, index) => ({ location, index })).sort((a, b) => a.location - b.location);
-    for (let locationIndex = 1; locationIndex < sortedLocations.length; locationIndex += 1) {
-        if (sortedLocations[locationIndex].location <= sortedLocations[locationIndex - 1].location) {
-            throw new Error(`Boundary time-series file ${filePath} contains duplicate station locations.`);
-        }
-    }
-
-    const sortedValues = values.map(rowValues => {
-        const sortedRowValues = [];
-        for (const sortedLocation of sortedLocations) {
-            const sourceIndex = sortedLocation.index * 3;
-            sortedRowValues.push(rowValues[sourceIndex], rowValues[sourceIndex + 1], rowValues[sourceIndex + 2]);
-        }
-        return sortedRowValues;
-    });
-
-    console.log(`Boundary time-series ${side} data parsed successfully from ${filePath}.`);
-    return {
-        active: true,
-        numPoints,
-        numTimes: times.length,
-        textureWidth: Math.max(numPoints, 1),
-        textureHeight: Math.max(times.length + 2, 1),
-        locations: sortedLocations.map(item => item.location),
-        times,
-        values: sortedValues
-    };
-}
-
-function validateSharedBoundaryTimeVector(sharedTimes, candidateTimes, filePath) {
-    if (sharedTimes.length != candidateTimes.length) {
-        throw new Error(`Boundary time-series file ${filePath} does not match the shared time-vector length.`);
-    }
-    for (let timeIndex = 0; timeIndex < sharedTimes.length; timeIndex += 1) {
-        const tolerance = Math.max(1.0e-7, 1.0e-7 * Math.abs(sharedTimes[timeIndex]));
-        if (Math.abs(sharedTimes[timeIndex] - candidateTimes[timeIndex]) > tolerance) {
-            throw new Error(`Boundary time-series file ${filePath} does not share the same time vector at row ${timeIndex + 1}.`);
-        }
-    }
-}
-
-// export async function loadBoundaryTimeSeriesData(calc_constants) {
-// Added by Codex: Accept user-uploaded boundary time-series files for custom configs outside served example folders.
-export async function loadBoundaryTimeSeriesData(calc_constants, boundaryTimeSeriesFiles = {}) {
-    const boundaryTimeSeriesData = {
-        west: createEmptyBoundaryTimeSeriesSide(),
-        east: createEmptyBoundaryTimeSeriesSide(),
-        south: createEmptyBoundaryTimeSeriesSide(),
-        north: createEmptyBoundaryTimeSeriesSide(),
-        sharedTimes: [],
-        zeroTimeIndex: 0,
-        hasActive: false
-    };
-    // Added by Codex: Reset the global clock shift unless active type-5 files define one below.
-    calc_constants.start_time_shift = 0.0;
-
-    const sides = ["west", "east", "south", "north"];
-    let sharedTimes = null;
-    for (const side of sides) {
-        if (calc_constants[`${side}_boundary_type`] != 5) {
-            calc_constants[`ts_${side}_num_points`] = 0;
-            continue;
-        }
-
-        const fileName = calc_constants[`ts_${side}_file`];
-        const uploadedFile = boundaryTimeSeriesFiles[side];
-        if (!fileName && !uploadedFile) {
-            throw new Error(`Boundary type 5 on the ${side} boundary requires ts_${side}_file.`);
-        }
-
-        let filePath = fileName;
-        let fileContents = null;
-        // Added by Codex: Uploaded files are available to the browser even when the source path is outside the served web root.
-        if (uploadedFile && typeof uploadedFile.text == "function") {
-            filePath = uploadedFile.name || fileName || `uploaded_${side}_boundary_time_series.txt`;
-            calc_constants[`ts_${side}_file`] = filePath;
-            fileContents = await uploadedFile.text();
-        } else {
-            filePath = resolveBoundaryTimeSeriesFilePath(calc_constants, fileName);
-            const response = await fetch(filePath);
-            if (!response.ok) {
-                throw new Error(`Could not load boundary time-series file ${filePath}: ${response.statusText}`);
-            }
-            fileContents = await response.text();
-        }
-
-        const parsedData = parseBoundaryTimeSeriesText(fileContents, side, filePath);
-        if (sharedTimes == null) {
-            sharedTimes = parsedData.times.slice();
-        } else {
-            validateSharedBoundaryTimeVector(sharedTimes, parsedData.times, filePath);
-        }
-
-        boundaryTimeSeriesData[side] = parsedData;
-        boundaryTimeSeriesData.hasActive = true;
-        calc_constants[`ts_${side}_num_points`] = parsedData.numPoints;
-    }
-
-    if (sharedTimes != null) {
-        boundaryTimeSeriesData.sharedTimes = sharedTimes;
-        boundaryTimeSeriesData.zeroTimeIndex = sharedTimes.length;
-        // Added by Codex: Use the first boundary time as the absolute-clock offset for nested simulations.
-        calc_constants.start_time_shift = sharedTimes[0];
-        console.log(`Boundary time-series start_time_shift set to ${calc_constants.start_time_shift} seconds.`);
-    }
-
-    return boundaryTimeSeriesData;
-}
-// Added by Codex: End boundary time-series forcing loaders.
-
 // load overlay image, if it exists
 export async function loadOverlay(calc_constants) {
     console.log("Looking for server side overlay file...");
```

#### CT1-087 지도 이미지 실패 처리

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Loader.js:615; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Loader.js:344; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 HTTP 상태와 MIME 형식을 검사하지 않는다. transect 판은 image.onerror도 설정하지 않는다. 본판은 실패를 reject한다. transect 판의 실패한 이미지 Promise는 초기화를 끝내지 못할 수 있다. |

본판 차이 줄의 마지막 수정: `bf8db50` 2026-05-24 (현재 648행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 355행 포함).

```diff
@@ -615,37 +344,16 @@
 // Step 2: Fetch Image from Google Maps.
 async function fetchMapImage(url) {
     // Fetch the image from the URL.
-    // const response = await fetch(url);
-    // const imageBlob = await response.blob();
-
-    // CODEX: Fail fast when Google Maps returns an HTTP error or non-image payload.
     const response = await fetch(url);
-    if (!response.ok) {
-        throw new Error(`Google Maps Static API request failed with HTTP ${response.status}`);
-    }
-
     const imageBlob = await response.blob();
-    if (!imageBlob.type.startsWith('image/')) {
-        throw new Error(`Google Maps Static API returned non-image content: ${imageBlob.type || 'unknown content type'}`);
-    }
 
     // Create an image element.
-    // const image = new Image();
-    // image.src = URL.createObjectURL(imageBlob);
-
-    // CODEX: Decode failure should reject so initialization can continue without Google Maps.
     const image = new Image();
     image.src = URL.createObjectURL(imageBlob);
 
     // Ensure the image is loaded.
-    // await new Promise((resolve) => {
-    //     image.onload = resolve;
-    // });
-
-    // CODEX: Reject failed image decoding instead of leaving overlay initialization incomplete.
-    await new Promise((resolve, reject) => {
+    await new Promise((resolve) => {
         image.onload = resolve;
-        image.onerror = () => reject(new Error('Unable to decode Google Maps Static API image response'));
     });
 
     return image;
```


### 2.5 js/File_Writer.js

본판: `js/File_Writer.js`. transect 판: `transect_version/js/File_Writer.js`.
원래 diff는 1467행이다. CR 제외 diff는 9구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `c4be488` | 2026-07-13 | allow multiple nested grids |
| 본판 | `bb99fee` | 2026-07-02 | Added grid nesting |
| 본판 | `9ed86a6` | 2026-02-17 | Update File_Writer.js |
| 본판 | `09cfd76` | 2026-02-15 | All 2D surface writes re-use the same buffer |
| 본판 | `b24af89` | 2026-02-10 | More memory leak fixes |
| 본판 | `dee0e14` | 2026-02-04 | clean up memory leaks |
| 본판 | `d852a23` | 2025-06-11 | Update File_Writer.js |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-088 표면 readback 버퍼 수명

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Writer.js:1; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Writer.js:1; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 전달받은 버퍼를 재사용하고 map 뒤 unmap한다. transect 판은 호출마다 버퍼를 만들고 반환 전에 unmap과 destroy를 하지 않는다. 반환 Float32Array는 별도 배열이므로 버퍼 유지가 결과 보존에 필요하지 않다. 인덱스 y*WIDTH+x와 channel-1은 같다. |

본판 차이 줄의 마지막 수정: `09cfd76` 2026-02-15 (현재 38행 포함); `b24af89` 2026-02-10 (현재 37행 포함); `cf9de63` 2023-10-24 (현재 31행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 69행 포함).

```diff
@@ -1,41 +1,72 @@
 //File_Writer.js
 import { calc_constants } from './constants_load_calc.js';
+export async function readTextureData(device, src_texture, channel) {
+    // Create a buffer to hold the data read from the texture.
+    const bytesPerChannel = 4; // Since each channel is a 32-bit float
+    const channelsPerPixel = 4; // For RGBA data
+    const actualBytesPerRow = calc_constants.WIDTH * bytesPerChannel * channelsPerPixel; // 4 channels and 4 bytes per float
+    const requiredBytesPerRow = Math.ceil(actualBytesPerRow / 256) * 256;
+    const paddedFlatData = new Float32Array(calc_constants.HEIGHT * requiredBytesPerRow / 4);
+
+    const buffer = device.createBuffer({
+        size: paddedFlatData.byteLength,
+        usage: GPUBufferUsage.COPY_DST | GPUBufferUsage.MAP_READ,
+        mappedAtCreation: true
+    });
+
+    new Float32Array(buffer.getMappedRange()).set(paddedFlatData);
+    buffer.unmap();
+
+    // Create a command encoder and copy the texture to the buffer.
+    const commandEncoder = device.createCommandEncoder();
+    commandEncoder.copyTextureToBuffer(
+        {
+            texture: src_texture,
+        },
+        {
+            buffer: buffer,
+            bytesPerRow: requiredBytesPerRow,
+            rowsPerImage: calc_constants.HEIGHT,
+        },
+        {
+            width: calc_constants.WIDTH,
+            height: calc_constants.HEIGHT,
+            depthOrArrayLayers: 1
+        },
+    );
+
+    // Submit the commands and wait for them to complete.
+    const queue = device.queue;
+    queue.submit([commandEncoder.finish()]);
+    await buffer.mapAsync(GPUMapMode.READ);
+
+    // Get an array buffer view of the buffer data.
+    const arrayBuffer = buffer.getMappedRange();
 
-export async function readTextureData(device, src_texture, channel, buffer) {
-  const width = calc_constants.WIDTH;
-  const height = calc_constants.HEIGHT;
-
-  const requiredBytesPerRow = Math.ceil((width * 4 * 4) / 256) * 256; // width * RGBA * f32, padded
-  const floatsPerRow = requiredBytesPerRow >> 2;
-  const chanOffset = channel - 1;
-
-  const commandEncoder = device.createCommandEncoder();
-  commandEncoder.copyTextureToBuffer(
-    { texture: src_texture },
-    { buffer, bytesPerRow: requiredBytesPerRow, rowsPerImage: height },
-    { width, height, depthOrArrayLayers: 1 }
-  );
-  device.queue.submit([commandEncoder.finish()]);
-
-  await buffer.mapAsync(GPUMapMode.READ);
-
-  const bufferData = new Float32Array(buffer.getMappedRange());
-  const flatData = new Float32Array(width * height);
-
-  for (let y = 0; y < height; y++) {
-    const rowBasePadded = y * floatsPerRow;
-    const rowBaseReal = y * width;
-    for (let x = 0; x < width; x++) {
-      flatData[rowBaseReal + x] = bufferData[rowBasePadded + (x << 2) + chanOffset];
+    // You could then convert the data as needed before saving, e.g., creating a Float32Array view on the data.
+    const Buffer_data = new Float32Array(arrayBuffer);
+
+    // Initialize the 1D array
+    let flatData = new Float32Array(calc_constants.WIDTH * calc_constants.HEIGHT);
+
+    // Extract data from Buffer_data into the 2D array, row by row, taking into account the padding and the 4 channels per pixel
+    for (let y = 0; y < calc_constants.HEIGHT; y++) {
+        for (let x = 0; x < calc_constants.WIDTH; x++) {
+
+            const paddedIndex = (y * requiredBytesPerRow / 4) + x * 4; // Adjust the index for padding
+            const realIndex = y * calc_constants.WIDTH + x; // Adjust the index for padding
+
+            flatData[realIndex] = Buffer_data[paddedIndex + channel - 1]; // red
+    //        data[x][y] = paddedFlatData[paddedIndex + 1];  // green
+    //        data[x][y] = paddedFlatData[paddedIndex + 2];  // blue
+    //        data[x][y] = paddedFlatData[paddedIndex + 3];  // alpha
+        }
     }
-  }
 
-  buffer.unmap();
-  return flatData;
+    return flatData; // or whatever processed form you prefer
 }
 
-
-// geotiff writer  // not used needs updates to be used
+// geotiff writer
 export async function downloadGeoTiffData(device, texture, channel,dx,dy) {
   // Assuming readTextureData returns an array or typed array of values
   const data = await readTextureData(device, texture, channel,dx,dy); // This should be compatible with the values expected by writeArrayBuffer
```

#### CT1-089 JPEG 버퍼 정리

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Writer.js:180; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Writer.js:211; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 이미지 자료를 slice한 뒤 버퍼를 unmap하고 destroy한다. transect 판은 두 정리 호출이 없다. |

본판 차이 줄의 마지막 수정: `cf9de63` 2023-10-24 (현재 183행 포함); `dee0e14` 2026-02-04 (현재 185행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -180,9 +211,6 @@
 
     // Make a copy of the buffer data immediately after mapping, to prevent "detached buffer" errors
     const bufferCopy = new Uint8ClampedArray(arrayBuffer.slice());
-    
-    buffer.unmap(); // Don't forget to unmap the buffer once done
-    buffer.destroy();  // free up memory
 
     // The buffer contains BGRA data, so we need to swap the red and blue channels for each pixel
     for (let i = 0; i < bufferCopy.length; i += 4) {
```

#### CT1-090 이미지 슬라이스 버퍼 정리

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Writer.js:324; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Writer.js:352; 아래 전체 diff의 +행 | 불일치 (E) | transect 판에는 destroy가 없다. 양쪽은 mapped view를 만든 뒤 unmap하므로 그 view의 수명 문제는 두 판의 공통 문제다. 이 행의 판간 차이는 destroy 유무다. |

본판 차이 줄의 마지막 수정: `dee0e14` 2026-02-04 (현재 329행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 355행 포함).

```diff
@@ -324,9 +352,7 @@
 
     // Extract and process the buffer data
     const copyArrayBuffer = new Uint8Array(buffer.getMappedRange());
-
-    buffer.unmap(); // Don't forget to unmap the buffer once done
-    buffer.destroy();  // free up memory
+    buffer.unmap();
 
     // Format conversion from BGRA to RGBA (if necessary)
     const imageData = new Uint8ClampedArray(width * height * 4);
```

#### CT1-091 GIF 프레임 버퍼 정리

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Writer.js:414; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Writer.js:440; 아래 전체 diff의 +행 | 불일치 (E) | 두 판은 slice 복사 후 unmap한다. transect 판에는 destroy가 없다. |

본판 차이 줄의 마지막 수정: `dee0e14` 2026-02-04 (현재 419행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 443행 포함).

```diff
@@ -414,9 +440,7 @@
         await buffer.mapAsync(GPUMapMode.READ);
         
         const arrayBuffer = new Uint8Array(buffer.getMappedRange()).slice();
-
-        buffer.unmap(); // Don't forget to unmap the buffer once done
-        buffer.destroy();  // free up memory
+        buffer.unmap();
 
         return arrayBuffer;
     }
```

#### CT1-092 애니메이션 버퍼 정리

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Writer.js:482; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Writer.js:506; 아래 전체 diff의 +행 | 불일치 (E) | 두 판은 slice 복사 후 unmap한다. transect 판에는 destroy가 없다. |

본판 차이 줄의 마지막 수정: `dee0e14` 2026-02-04 (현재 487행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 509행 포함).

```diff
@@ -482,9 +506,7 @@
         device.queue.submit([gpuCommands]);
         await buffer.mapAsync(GPUMapMode.READ);
         const arrayBuffer = new Uint8Array(buffer.getMappedRange()).slice();
-
-        buffer.unmap(); // Don't forget to unmap the buffer once done
-        buffer.destroy();  // free up memory
+        buffer.unmap();
 
         return arrayBuffer;
     }
```

#### CT1-093 표면 출력 함수 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Writer.js:528; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Writer.js:550; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 공용 readback 버퍼를 전달한다. transect 판은 호출 안에서 버퍼를 만든다. bathytopo.bin의 채널 3과 첫 프레임 조건은 같다. |

본판 차이 줄의 마지막 수정: `09cfd76` 2026-02-15 (현재 538행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 560행 포함).

```diff
@@ -528,14 +550,14 @@
     gif.render();
 }
 
-export async function writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities, buffer) {
+export async function writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities) {
 
     let time_filename = `time_${frame_count_output}.txt`;
     await saveSingleValueToFile(total_time,time_filename);
 
     if(frame_count_output == 1){
         let filename = `bathytopo.bin`;
-        await downloadTextureData(device, txBottom, 3, filename, buffer);  // number is the channel 1 = .r, 2 = .g, etc.
+        await downloadTextureData(device, txBottom, 3, filename);  // number is the channel 1 = .r, 2 = .g, etc.
 
         filename = `dx.txt`;
         await saveSingleValueToFile(calc_constants.dx,filename);
```

#### CT1-094 시간별 바닥고 출력과 표면 자료

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Writer.js:550; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Writer.js:572; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 퇴적물 또는 total_time<300.0인 disturbanceType==5에서 depth_번호.bin을 출력한다. transect 판은 이 조건부 바닥고 출력을 하지 않는다. eta/P/Q/u/v/turb의 채널 번호·파일명·대기 순서는 같다. |

본판 차이 줄의 마지막 수정: `9ed86a6` 2026-02-17 (현재 553행 포함); `d852a23` 2025-06-11 (현재 558행 포함); `09cfd76` 2026-02-15 (현재 591행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 607행 포함).

```diff
@@ -550,45 +572,39 @@
         await saveSingleValueToFile(calc_constants.HEIGHT,filename);
     }
 
-    if(calc_constants.useSedTransModel ==1 || (total_time < 300.0 && calc_constants.disturbanceType == 5)){  // write depth if using sediment transport model or landslide
-        let filename = `depth_${frame_count_output}.bin`;
-        await downloadTextureData(device, txBottom, 3, filename, buffer);  // number is the channel 1 = .r, 2 = .g, etc.
-        await sleep(calc_constants.fileWritePause); // wait long enough for the download to start…
-    }
-
     if(calc_constants.write_eta == 1){  // free surface elevation
         let filename = `elev_${frame_count_output}.bin`;
-        await downloadTextureData(device, txState, 1, filename, buffer);  // number is the channel 1 = .r, 2 = .g, etc.
+        await downloadTextureData(device, txState, 1, filename);  // number is the channel 1 = .r, 2 = .g, etc.
         await sleep(calc_constants.fileWritePause); // wait long enough for the download to start…
     }
 
     if(calc_constants.write_P == 1){  // x-dir flux Hu
         let filename = `xflux_${frame_count_output}.bin`;
-        await downloadTextureData(device, txState, 2, filename, buffer);  // number is the channel 1 = .r, 2 = .g, etc.
+        await downloadTextureData(device, txState, 2, filename);  // number is the channel 1 = .r, 2 = .g, etc.
         await sleep(calc_constants.fileWritePause); // wait long enough for the download to start…
     }
 
     if(calc_constants.write_Q == 1){  // y-dir flux Hv
         let filename = `yflux_${frame_count_output}.bin`;
-        await downloadTextureData(device, txState, 3, filename, buffer);  // number is the channel 1 = .r, 2 = .g, etc.
+        await downloadTextureData(device, txState, 3, filename);  // number is the channel 1 = .r, 2 = .g, etc.
         await sleep(calc_constants.fileWritePause); // wait long enough for the download to start…
     }
 
     if(calc_constants.write_u == 1){  // x-dir velocity u
         let filename = `xvelo_${frame_count_output}.bin`;
-        await downloadTextureData(device, txModelVelocities, 1, filename, buffer);  // number is the channel 1 = .r, 2 = .g, etc.
+        await downloadTextureData(device, txModelVelocities, 1, filename);  // number is the channel 1 = .r, 2 = .g, etc.
         await sleep(calc_constants.fileWritePause); // wait long enough for the download to start…
     }
 
     if(calc_constants.write_v == 1){  // y-dir velocity v
         let filename = `yvelo_${frame_count_output}.bin`;
-        await downloadTextureData(device, txModelVelocities, 2, filename, buffer);  // number is the channel 1 = .r, 2 = .g, etc.
+        await downloadTextureData(device, txModelVelocities, 2, filename);  // number is the channel 1 = .r, 2 = .g, etc.
         await sleep(calc_constants.fileWritePause); // wait long enough for the download to start…
     }    
 
     if(calc_constants.write_turb == 1){  // breaking eddy viscosity
         let filename = `turb_${frame_count_output}.bin`;
-        await downloadTextureData(device, txBreaking, 2, filename, buffer);  // number is the channel 1 = .r, 2 = .g, etc.
+        await downloadTextureData(device, txBreaking, 2, filename);  // number is the channel 1 = .r, 2 = .g, etc.
         await sleep(calc_constants.fileWritePause); // wait long enough for the download to start…
     }
```

#### CT1-095 바이너리 다운로드 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Writer.js:596; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Writer.js:612; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 readTextureData에 공용 버퍼를 전달한다. transect 판은 전달하지 않는다. Blob은 모두 application/octet-stream이다. |

본판 차이 줄의 마지막 수정: `09cfd76` 2026-02-15 (현재 601행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 617행 포함).

```diff
@@ -596,9 +612,9 @@
 }
 
 
-export async function downloadTextureData(device, texture, channel, filename, buffer) {
+export async function downloadTextureData(device, texture, channel, filename) {
     try {
-        const data = await readTextureData(device, texture, channel, buffer);
+        const data = await readTextureData(device, texture, channel);
 
         // Create a Blob from the data
         const blob = new Blob([data.buffer], { type: 'application/octet-stream' });
```

#### CT1-096 중첩 경계 출력 없음

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/File_Writer.js:633; 아래 전체 diff의 -행 | ebca435:transect_version/js/File_Writer.js:649; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 4변 eta/hu/hv를 9자리 유효숫자로 저장한다. 본판은 임계 eta 이전 행을 잘라내도 절대 시간을 유지한다. 본판은 사각형별 파일 접두어와 임계값을 사용한다. transect 판에는 이 writer가 없다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 842행 포함); `c4be488` 2026-07-13 (현재 828행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -633,213 +649,6 @@
     });
   }
 
-// Added by Codex: Start nested-grid boundary time-series output writer.
-async function readRgbaTextureData(device, src_texture, width, height) {
-    const bytesPerPixel = 4 * 4; // rgba32float
-    const requiredBytesPerRow = Math.ceil((width * bytesPerPixel) / 256) * 256;
-    const floatsPerRow = requiredBytesPerRow >> 2;
-    const bufferSize = requiredBytesPerRow * height;
-
-    const readbackBuffer = device.createBuffer({
-        size: bufferSize,
-        usage: GPUBufferUsage.COPY_DST | GPUBufferUsage.MAP_READ,
-    });
-
-    const commandEncoder = device.createCommandEncoder();
-    commandEncoder.copyTextureToBuffer(
-        { texture: src_texture },
-        { buffer: readbackBuffer, bytesPerRow: requiredBytesPerRow, rowsPerImage: height },
-        { width, height, depthOrArrayLayers: 1 }
-    );
-    device.queue.submit([commandEncoder.finish()]);
-
-    await readbackBuffer.mapAsync(GPUMapMode.READ);
-    const paddedData = new Float32Array(readbackBuffer.getMappedRange());
-    const data = new Float32Array(width * height * 4);
-
-    for (let row = 0; row < height; row++) {
-        const paddedRowBase = row * floatsPerRow;
-        const outputRowBase = row * width * 4;
-        for (let col = 0; col < width; col++) {
-            const paddedBase = paddedRowBase + col * 4;
-            const outputBase = outputRowBase + col * 4;
-            data[outputBase] = paddedData[paddedBase];
-            data[outputBase + 1] = paddedData[paddedBase + 1];
-            data[outputBase + 2] = paddedData[paddedBase + 2];
-            data[outputBase + 3] = paddedData[paddedBase + 3];
-        }
-    }
-
-    readbackBuffer.unmap();
-    readbackBuffer.destroy();
-    return data;
-}
-
-function formatNestedGridBoundaryValue(value) {
-    if (!Number.isFinite(value)) {
-        return "0";
-    }
-    return Number(value).toPrecision(9);
-}
-
-// Added by Codex: Start nested-grid quiet-period trim helpers.
-// function findNestedGridThresholdStartIndex(sideReadbacks, capturedTimes) {
-//     const threshold = Math.max(0.0, Number(calc_constants.nestedEtaWriteThreshold) || 0.0);
-// Added by Codex: Allow each nested-grid output rectangle to use its own threshold while preserving the global fallback.
-function findNestedGridThresholdStartIndex(sideReadbacks, capturedTimes, thresholdOverride = null) {
-    const threshold = Math.max(0.0, Number(thresholdOverride ?? calc_constants.nestedEtaWriteThreshold) || 0.0);
-    if (threshold <= 0.0) {
-        return 0;
-    }
-
-    for (let sampleIndex = 0; sampleIndex < capturedTimes.length; sampleIndex++) {
-        for (const side of sideReadbacks) {
-            for (let stationIndex = 0; stationIndex < side.width; stationIndex++) {
-                const baseIndex = (sampleIndex * side.width + stationIndex) * 4;
-                if (Math.abs(side.textureData[baseIndex]) > threshold) {
-                    return sampleIndex;
-                }
-            }
-        }
-    }
-
-    return -1;
-}
-
-// function createNestedGridStartTimeBlob(actualStartTime, threshold, triggerIndex) {
-//     // Added by Codex: Keep no-trigger metadata explicit instead of passing NaN through the zero-fallback formatter.
-//     const startTimeText = Number.isFinite(actualStartTime) ? formatNestedGridBoundaryValue(actualStartTime) : "NaN";
-//     // const pieces = [
-//     //     `% nested-grid boundary time-series absolute start time\n`,
-//     //     `start_time_series ${formatNestedGridBoundaryValue(actualStartTime)}\n`,
-//     //     `nestedEtaWriteThreshold ${formatNestedGridBoundaryValue(threshold)}\n`,
-//     //     `trigger_sample_index ${triggerIndex}\n`
-//     // ];
-//     // Added by Codex: Keep the start-time file as one simple ASCII value for downstream nested-grid scripts.
-//     const pieces = [`${startTimeText}\n`];
-//     return new Blob(pieces, { type: 'text/plain' });
-// }
-// Added by Codex: End nested-grid quiet-period trim helpers.
-
-// function createNestedGridBoundaryTimeSeriesBlob(sideData, textureData, capturedTimes) {
-// Added by Codex: Allow final nested-grid files to be trimmed without changing their shifted/global time values.
-function createNestedGridBoundaryTimeSeriesBlob(sideData, textureData, capturedTimes, startSampleIndex = 0) {
-    const pieces = [];
-    const numberOfStations = sideData.width;
-
-    pieces.push(`number_of_ts_along_boundary ${numberOfStations}\n`);
-    for (let stationIndex = 0; stationIndex < numberOfStations; stationIndex++) {
-        pieces.push(`${formatNestedGridBoundaryValue(sideData.locations[stationIndex])}\n`);
-    }
-
-    let header = "% time";
-    for (let stationIndex = 0; stationIndex < numberOfStations; stationIndex++) {
-        header += ` eta${stationIndex + 1} hu${stationIndex + 1} hv${stationIndex + 1}`;
-    }
-    pieces.push(`${header}\n`);
-
-    // for (let sampleIndex = 0; sampleIndex < capturedTimes.length; sampleIndex++) {
-    for (let sampleIndex = startSampleIndex; sampleIndex < capturedTimes.length; sampleIndex++) {
-        // const rowValues = [formatNestedGridBoundaryValue(capturedTimes[sampleIndex])];
-        // Added by Codex: Keep nested boundary output times on the shifted/global simulation clock.
-        const rowValues = [formatNestedGridBoundaryValue(capturedTimes[sampleIndex])];
-        for (let stationIndex = 0; stationIndex < numberOfStations; stationIndex++) {
-            const baseIndex = (sampleIndex * numberOfStations + stationIndex) * 4;
-            rowValues.push(formatNestedGridBoundaryValue(textureData[baseIndex]));
-            rowValues.push(formatNestedGridBoundaryValue(textureData[baseIndex + 1]));
-            rowValues.push(formatNestedGridBoundaryValue(textureData[baseIndex + 2]));
-        }
-        pieces.push(`${rowValues.join(" ")}\n`);
-    }
-
-    return new Blob(pieces, { type: 'text/plain' });
-}
-
-export async function writeNestedGridBoundaryTimeSeriesData(device, nestedGridOutputState) {
-    const capturedTimes = nestedGridOutputState.capturedTimes || [];
-    if (capturedTimes.length <= 0) {
-        console.warn("Nested-grid boundary output requested a download, but no samples were captured.");
-        return;
-    }
-
-    // const prefix = calc_constants.nestedGridOutput_file_prefix || "nested";
-    // Added by Codex: Use per-rectangle file prefixes when multi-rectangle nested output is active.
-    const prefix = nestedGridOutputState.filePrefix || calc_constants.nestedGridOutput_file_prefix || "nested";
-    const sides = [
-        {
-            name: "south",
-            texture: nestedGridOutputState.txSouth,
-            width: nestedGridOutputState.nx,
-            locations: nestedGridOutputState.southLocations
-        },
-        {
-            name: "north",
-            texture: nestedGridOutputState.txNorth,
-            width: nestedGridOutputState.nx,
-            locations: nestedGridOutputState.northLocations
-        },
-        {
-            name: "west",
-            texture: nestedGridOutputState.txWest,
-            width: nestedGridOutputState.ny,
-            locations: nestedGridOutputState.westLocations
-        },
-        {
-            name: "east",
-            texture: nestedGridOutputState.txEast,
-            width: nestedGridOutputState.ny,
-            locations: nestedGridOutputState.eastLocations
-        }
-    ];
-
-    // for (const side of sides) {
-    //     const textureData = await readRgbaTextureData(device, side.texture, side.width, capturedTimes.length);
-    //     const blob = createNestedGridBoundaryTimeSeriesBlob(side, textureData, capturedTimes);
-    //     await blobCreationAndDownload(blob, `${prefix}_time_series_bc_${side.name}.txt`);
-    //     await sleep(calc_constants.fileWritePause);
-    // }
-    // Added by Codex: Start threshold-trimmed nested-grid boundary file downloads.
-    const sideReadbacks = [];
-    for (const side of sides) {
-        sideReadbacks.push({
-            ...side,
-            textureData: await readRgbaTextureData(device, side.texture, side.width, capturedTimes.length)
-        });
-    }
-
-    // const threshold = Math.max(0.0, Number(calc_constants.nestedEtaWriteThreshold) || 0.0);
-    // Added by Codex: Prefer the rectangle-specific threshold and fall back to the legacy global threshold.
-    const threshold = Math.max(0.0, Number(nestedGridOutputState.etaThreshold ?? calc_constants.nestedEtaWriteThreshold) || 0.0);
-    // const startSampleIndex = findNestedGridThresholdStartIndex(sideReadbacks, capturedTimes);
-    // const actualStartTime = startSampleIndex >= 0 ? capturedTimes[startSampleIndex] : Number.NaN;
-    // Added by Codex: Preserve shifted/global output times while still trimming leading quiet samples.
-    const thresholdActive = threshold > 0.0;
-    const startSampleIndex = thresholdActive ? findNestedGridThresholdStartIndex(sideReadbacks, capturedTimes, threshold) : 0;
-    const actualStartTime = startSampleIndex >= 0 ? capturedTimes[startSampleIndex] : Number.NaN;
-    calc_constants.nestedGridOutput_actual_start_time = Number.isFinite(actualStartTime) ? actualStartTime : 0.0;
-
-    // const startTimeBlob = createNestedGridStartTimeBlob(actualStartTime, threshold, startSampleIndex);
-    // await blobCreationAndDownload(startTimeBlob, `${prefix}_time_series_start_time.txt`);
-    // await sleep(calc_constants.fileWritePause);
-    // Added by Codex: The first written boundary-file time now carries the start-time shift; no separate start-time file is needed.
-
-    // if (startSampleIndex < 0) {
-    if (thresholdActive && startSampleIndex < 0) {
-        console.warn(`Nested-grid boundary output ${prefix} did not exceed nestedEtaWriteThreshold=${threshold}; boundary time-series files were not written.`);
-        return;
-    }
-
-    for (const side of sideReadbacks) {
-        // const blob = createNestedGridBoundaryTimeSeriesBlob(side, side.textureData, capturedTimes, startSampleIndex, actualStartTime);
-        // Added by Codex: Write threshold-trimmed rows with their shifted/global simulation times unchanged.
-        const blob = createNestedGridBoundaryTimeSeriesBlob(side, side.textureData, capturedTimes, startSampleIndex);
-        await blobCreationAndDownload(blob, `${prefix}_time_series_bc_${side.name}.txt`);
-        await sleep(calc_constants.fileWritePause);
-    }
-    // Added by Codex: End threshold-trimmed nested-grid boundary file downloads.
-}
-// Added by Codex: End nested-grid boundary time-series output writer.
-
 export function sleep(ms) {
     return new Promise(resolve => setTimeout(resolve, ms));
 }
```


### 2.6 js/Handler_AddDisturbance.js

본판: `js/Handler_AddDisturbance.js`. transect 판: `transect_version/js/Handler_AddDisturbance.js`.
원래 diff는 232행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `4353b85` | 2025-06-09 | Sed bugs / corrections |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-097 지형변화 누적 입력 누락

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_AddDisturbance.js:64; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_AddDisturbance.js:64; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 binding 7의 txBotChange_Sed를 제공하지 않는다. 본판은 교란 지형과 누적 침식량의 합을 보존하도록 이 바인딩을 추가했다. 1D 미분 제거와 무관한 한쪽 결함 수정이다. |

본판 차이 줄의 마지막 수정: `4353b85` 2025-06-09 (현재 81행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 72행 포함).

```diff
@@ -64,21 +64,12 @@
                     format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels
                     viewDimension: '2d'       // The texture is a 2D texture
                 }
-            },
-            {
-                // 7th binding: A texture that the fragment shader will sample from.
-                binding: 7,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
             }
         ]
     });
 }
 
-export function create_AddDisturbance_BindGroup(device, uniformBuffer, txBottom, txState, txBottomInitial, txtemp_AddDisturbance, txBoundaryForcing, txtemp_bottom, txBotChange_Sed) {
+export function create_AddDisturbance_BindGroup(device, uniformBuffer, txBottom, txState, txBottomInitial, txtemp_AddDisturbance, txBoundaryForcing, txtemp_bottom) {
     return device.createBindGroup({
         layout: create_AddDisturbance_BindGroupLayout(device),
         entries: [
```

#### CT1-098 누적 지형변화 리소스 누락

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_AddDisturbance.js:112; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_AddDisturbance.js:103; 아래 전체 diff의 +행 | 불일치 (E) | transect 판에는 txBotChange_Sed.createView()가 없다. 대응 셰이더도 누적 지형변화를 읽지 않는다. 본판의 Sed bugs / corrections 이력과 함께 판정한다. |

본판 차이 줄의 마지막 수정: `4353b85` 2025-06-09 (현재 118행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -112,10 +103,6 @@
                 binding: 6,
                 resource: txtemp_bottom.createView()
             },
-            {
-                binding: 7,
-                resource: txBotChange_Sed.createView()
-            },
         ]
     });
 }
\ No newline at end of file
```


### 2.7 js/Handler_BoundaryPass.js

본판: `js/Handler_BoundaryPass.js`. transect 판: `transect_version/js/Handler_BoundaryPass.js`.
원래 diff는 309행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `bb99fee` | 2026-07-02 | Added grid nesting |
| 본판 | `8c2b62b` | 2025-08-24 | Added Tracy Arm Example, some landslide viz additions |
| transect | `3d8a61b` | 2025-06-14 | Added many-transect version |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-099 단면 파랑과 경계 시계열 바인딩

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_BoundaryPass.js:93; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_BoundaryPass.js:93; 아래 전체 diff의 +행 | 코드에만 (C) | 본판은 binding 9에 txBoundaryForcing을 둔다. 본판은 binding 10–13에 4변 경계 시계열을 둔다. transect 판은 binding 9에 txWaves_Transect를 둔다. 같은 번호의 리소스 의미가 다르다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 140행 포함); `63a12e3` 2023-10-19 (현재 131행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 100행 포함).

```diff
@@ -93,51 +93,11 @@
                     format: 'rgba32float'
                 }
             },
-            // Added by Codex: Start boundary time-series forcing texture bindings.
-            {
-                // 10th binding: South boundary type-5 eta/hu/hv time-series texture.
-                binding: 10,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
-            {
-                // 11th binding: North boundary type-5 eta/hu/hv time-series texture.
-                binding: 11,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
-            {
-                // 12th binding: West boundary type-5 eta/hu/hv time-series texture.
-                binding: 12,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
-            {
-                // 13th binding: East boundary type-5 eta/hu/hv time-series texture.
-                binding: 13,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            }
-            // Added by Codex: End boundary time-series forcing texture bindings.
         ]
     });
 }
 
-// export function create_BoundaryPass_BindGroup(device, uniformBuffer, current_stateUVstar, txBottom, txWaves, txNewState_Sed, txtemp, txtemp_Sed, txBreaking, txtemp_Breaking, txBoundaryForcing) {
-// Added by Codex: Add four optional boundary time-series textures for boundary_type == 5.
-export function create_BoundaryPass_BindGroup(device, uniformBuffer, current_stateUVstar, txBottom, txWaves, txNewState_Sed, txtemp, txtemp_Sed, txBreaking, txtemp_Breaking, txBoundaryForcing, txBoundaryTimeSeriesSouth, txBoundaryTimeSeriesNorth, txBoundaryTimeSeriesWest, txBoundaryTimeSeriesEast) {
+export function create_BoundaryPass_BindGroup(device, uniformBuffer, current_stateUVstar, txBottom, txWaves, txNewState_Sed, txtemp, txtemp_Sed, txBreaking, txtemp_Breaking, txWaves_Transect) {
     return device.createBindGroup({
         layout: create_BoundaryPass_BindGroupLayout(device),
         entries: [
```

#### CT1-100 경계 바인드 그룹 리소스

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_BoundaryPass.js:178; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_BoundaryPass.js:138; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판의 binding 9는 단면 행별 파랑을 읽는다. 본판은 경계 강제장과 시계열을 별개 리소스로 둔다. |

본판 차이 줄의 마지막 수정: `8c2b62b` 2025-08-24 (현재 184행 포함); `bb99fee` 2026-07-02 (현재 203행 포함); `38a5072` 2025-01-21 (현재 202행 포함); `63a12e3` 2023-10-19 (현재 206행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 144행 포함); `22e1983` 2025-06-06 (현재 148행 포함).

```diff
@@ -178,29 +138,11 @@
             {
                 binding: 8,
                 resource: txtemp_Breaking.createView()
-            },
+            } ,
             {
                 binding: 9,
-                resource: txBoundaryForcing.createView()
-            },
-            // Added by Codex: Start boundary time-series forcing texture resources.
-            {
-                binding: 10,
-                resource: txBoundaryTimeSeriesSouth.createView()
-            },
-            {
-                binding: 11,
-                resource: txBoundaryTimeSeriesNorth.createView()
-            },
-            {
-                binding: 12,
-                resource: txBoundaryTimeSeriesWest.createView()
-            },
-            {
-                binding: 13,
-                resource: txBoundaryTimeSeriesEast.createView()
-            }
-            // Added by Codex: End boundary time-series forcing texture resources.
+                resource: txWaves_Transect.createView()
+            } 
         ]
     });
-}
+}
\ No newline at end of file
```


### 2.8 js/Handler_CalcMeans.js

본판: `js/Handler_CalcMeans.js`. transect 판: `transect_version/js/Handler_CalcMeans.js`.
원래 diff는 390행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `dc6cc2d` | 2025-08-10 | update max free surface render |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-101 통계용 실제 수면 입력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_CalcMeans.js:120; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_CalcMeans.js:120; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 binding 13의 txNewState를 추가했다. transect 판은 재구성 수심 평균으로 수면을 산출한다. 이는 평균·최대 eta의 자료원이 다른 차이다. |

본판 차이 줄의 마지막 수정: `dc6cc2d` 2025-08-10 (현재 136행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 127행 포함).

```diff
@@ -120,20 +120,11 @@
                     format: 'rgba32float'
                 }
             },
-            {
-                // 13th binding: A storage texture. The compute shader will write results into this texture.
-                binding: 13,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            }
         ]
     });
 }
 
-export function create_CalcMeans_BindGroup(device, uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC, txNewState) {
+export function create_CalcMeans_BindGroup(device, uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC) {
     return device.createBindGroup({
         layout: create_CalcMeans_BindGroupLayout(device),
         entries: [
```

#### CT1-102 통계 바인드 그룹

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_CalcMeans.js:191; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_CalcMeans.js:182; 아래 전체 diff의 +행 | 불일치 (A) | transect 판에는 txNewState.createView()가 없다. 대응 CalcMeans 셰이더의 eta 산출식과 일치한다. |

본판 차이 줄의 마지막 수정: `dc6cc2d` 2025-08-10 (현재 197행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -191,10 +182,6 @@
                 binding: 12,
                 resource: txC.createView()
             },
-            {
-                binding: 13,
-                resource: txNewState.createView()
-            }
         ]
     });
 }
\ No newline at end of file
```


### 2.9 js/Handler_Copytxf32_txf16.js

본판: `js/Handler_Copytxf32_txf16.js`. transect 판: `transect_version/js/Handler_Copytxf32_txf16.js`.
원래 diff는 39행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-103 불투수 바닥 표시 입력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_Copytxf32_txf16.js:73; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_Copytxf32_txf16.js:73; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 binding 8의 txHardBottom을 제공한다. transect 판은 표시용 텍스처를 두 레이어만 쓴다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 90행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 81행 포함).

```diff
@@ -73,21 +73,12 @@
                     format: 'rgba32float'
                 }
             },
-            {
-                // 8th binding: A texture that the fragment shader will sample from.
-                binding: 8,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
         ]
     });
 }
 
 
-export function create_Copytxf32_txf16_BindGroup(device, uniformBuffer, txNewState, txBottom, txMeans_Speed, txRenderVarsf16, txMeans_Momflux, txModelVelocities, txMeans, txHardBottom) {
+export function create_Copytxf32_txf16_BindGroup(device, uniformBuffer, txNewState, txBottom, txMeans_Speed, txRenderVarsf16, txMeans_Momflux, txModelVelocities, txMeans) {
     return device.createBindGroup({
         layout: create_Copytxf32_txf16_BindGroupLayout(device),
         entries: [
```

#### CT1-104 불투수 바닥 리소스

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_Copytxf32_txf16.js:125; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_Copytxf32_txf16.js:116; 아래 전체 diff의 +행 | 불일치 (A) | transect 판에는 txHardBottom.createView()가 없다. 본판의 가용 퇴적층 깊이 표시와 연결된다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 131행 포함); `34abfb1` 2025-04-23 (현재 134행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 121행 포함).

```diff
@@ -125,10 +116,6 @@
                 binding: 7,
                 resource: txMeans.createView()
             },
-            {
-                binding: 8,
-                resource: txHardBottom.createView()
-            },
         ]
     });
-}  
\ No newline at end of file
+}
\ No newline at end of file
```


### 2.10 js/Handler_ExtractTimeSeries.js

본판: `js/Handler_ExtractTimeSeries.js`. transect 판: `transect_version/js/Handler_ExtractTimeSeries.js`.
원래 diff는 256행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `397c575` | 2025-09-09 | Max fs to tooltip for slide sims |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-105 툴팁 최대 수면 입력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_ExtractTimeSeries.js:71; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_ExtractTimeSeries.js:71; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 binding 8의 txMeans_Speed를 제공한다. transect 판은 항상 유의파고 자료를 툴팁에 쓴다. |

본판 차이 줄의 마지막 수정: `397c575` 2025-09-09 (현재 89행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 80행 포함).

```diff
@@ -71,22 +71,13 @@
                     format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels
                     viewDimension: '2d'       // The texture is a 1D texture
                 }
-            },
-            {
-                // 8th binding: A texture that the fragment shader will sample from.
-                binding: 8,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
             }
         ]
     });
 }
 
 
-export function create_ExtractTimeSeries_BindGroup(device, uniformBuffer, txBottom, txBottomFriction, txContSource, txState, txWaveHeight, txTimeSeries_Locations, txTimeSeries_Data, txMeans_Speed) {
+export function create_ExtractTimeSeries_BindGroup(device, uniformBuffer, txBottom, txBottomFriction, txContSource, txState, txWaveHeight, txTimeSeries_Locations, txTimeSeries_Data) {
     return device.createBindGroup({
         layout: create_ExtractTimeSeries_BindGroupLayout(device),
         entries: [
```

#### CT1-106 최대 수면 리소스

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_ExtractTimeSeries.js:124; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_ExtractTimeSeries.js:115; 아래 전체 diff의 +행 | 불일치 (A) | transect 판에는 txMeans_Speed.createView()가 없다. 점 시계열 eta/P/Q의 자료원 변경을 뜻하지 않는다. |

본판 차이 줄의 마지막 수정: `397c575` 2025-09-09 (현재 130행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -124,10 +115,6 @@
                 binding: 7,
                 resource: txTimeSeries_Data.createView()
             },
-            {
-                binding: 8,
-                resource: txMeans_Speed.createView()
-            }
         ]
     });
 }
\ No newline at end of file
```


### 2.11 js/Handler_Pass2.js

본판: `js/Handler_Pass2.js`. transect 판: `transect_version/js/Handler_Pass2.js`.
원래 diff는 448행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-107 퇴적물 확산 입력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_Pass2.js:138; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_Pass2.js:138; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 binding 15로 txBreaking을 읽어 쇄파 점성 기반 확산계수를 만든다. transect 판의 Pass2에는 해당 리소스가 없다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 156행 포함); `63a12e3` 2023-10-19 (현재 149행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 147행 포함).

```diff
@@ -138,22 +138,13 @@
                     format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels
                     viewDimension: '2d'       // The texture is a 2D texture
                 }
-            },
-            {
-                // 15th binding: A texture that the fragment shader will sample from.
-                binding: 15,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
+            }
         ]
     });
 }
 
 
-export function create_Pass2_BindGroup(device, uniformBuffer,txH, txU, txV, txBottom, txC, txHnear, txXFlux, txYFlux, txSed_C1, txSed_C2, txSed_C3, txSed_C4, txXFlux_Sed, txYFlux_Sed, txBreaking) {
+export function create_Pass2_BindGroup(device, uniformBuffer,txH, txU, txV, txBottom, txC, txHnear, txXFlux, txYFlux, txSed_C1, txSed_C2, txSed_C3, txSed_C4, txXFlux_Sed, txYFlux_Sed) {
     return device.createBindGroup({
         layout: create_Pass2_BindGroupLayout(device),
         entries: [
```

#### CT1-108 Pass2 바인드 그룹

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_Pass2.js:219; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_Pass2.js:210; 아래 전체 diff의 +행 | 불일치 (A) | 본판의 txBreaking.createView()가 transect 판에는 없다. 농도 flux의 확산항 차이와 연결된다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 225행 포함); `63a12e3` 2023-10-19 (현재 228행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 215행 포함).

```diff
@@ -219,10 +210,6 @@
                 binding: 14,
                 resource: txYFlux_Sed.createView()
             },
-            {
-                binding: 15,
-                resource: txBreaking.createView()
-            },
         ]
     });
-}  
\ No newline at end of file
+}
\ No newline at end of file
```


### 2.12 js/Handler_Render.js

본판: `js/Handler_Render.js`. transect 판: `transect_version/js/Handler_Render.js`.
원래 diff는 784행이다. CR 제외 diff는 1구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-109 가용 퇴적층 깊이 범례

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_Render.js:314; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_Render.js:314; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 surfaceToPlot==19의 가용 깊이 범례를 제공한다. transect 판에는 해당 표시 경로가 없다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 317행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -314,7 +314,6 @@
         16: "Max Free Surface Elev (m)",
         17: "Sediment Class 1 Concentration",
         18: "Sediment Class 1 Erosion Rate",
-        19: "Sediment Class 1 Available Depth (m)",
         21: "Depth Change (m) due to Sed Trans",
         22: "Design Component Map",
         23: "Mean |Vertical Vorticity| (1/s)",
```


### 2.13 js/Handler_SedTrans_Pass3.js

본판: `js/Handler_SedTrans_Pass3.js`. transect 판: `transect_version/js/Handler_SedTrans_Pass3.js`.
원래 diff는 448행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| 본판 | `2a7452d` | 2025-06-07 | Sed Trans updates |
| 본판 | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-110 퇴적물 적분 리소스 확장

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_SedTrans_Pass3.js:120; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_SedTrans_Pass3.js:120; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 binding 13–17로 쇄파·면속도·면농도·hardbottom을 받는다. transect 판은 셀 운동량과 고정 확산계수를 쓴다. |

본판 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 150행 포함); `85c2ca2` 2024-03-19 (현재 140행 포함); `2a7452d` 2025-06-07 (현재 159행 포함); `b8b50c3` 2025-06-08 (현재 174행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 129행 포함).

```diff
@@ -120,58 +120,13 @@
                     format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels
                     viewDimension: '2d'       // The texture is a 2D texture
                 }
-            },
-            {
-                // 13th binding: A texture that the fragment shader will sample from.
-                binding: 13,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
-            {
-                // 14th binding: A texture that the fragment shader will sample from.
-                binding: 14,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
-            {
-                // 15th binding: A texture that the fragment shader will sample from.
-                binding: 15,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
-            {
-                // 16th binding: A texture that the fragment shader will sample from.
-                binding: 16,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
-            {
-                // 17th binding: A texture that the fragment shader will sample from.
-                binding: 17,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
+            }
         ]
     });
 }
 
 
-export function create_SedTrans_Pass3_BindGroup(device, uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed, txBreaking, txU, txV, txSed_C1, txHardBottom) {
+export function create_SedTrans_Pass3_BindGroup(device, uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed) {
     return device.createBindGroup({
         layout: create_SedTrans_Pass3_BindGroupLayout(device),
         entries: [
```

#### CT1-111 퇴적물 바인드 그룹

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_SedTrans_Pass3.js:229; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_SedTrans_Pass3.js:184; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 13–17의 리소스 view를 제공하지 않는다. 본판의 bedload와 침식 가능 깊이 검사에 필요한 자료가 빠진다. |

본판 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 243행 포함); `2a7452d` 2025-06-07 (현재 247행 포함); `b8b50c3` 2025-06-08 (현재 251행 포함); `85c2ca2` 2024-03-19 (현재 254행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 189행 포함).

```diff
@@ -229,26 +184,6 @@
                 binding: 12,
                 resource: depostion_Sed.createView()
             },
-            {
-                binding: 13,
-                resource: txBreaking.createView()
-            },
-            {
-                binding: 14,
-                resource: txU.createView()
-            },
-            {
-                binding: 15,
-                resource: txV.createView()
-            },
-            {
-                binding: 16,
-                resource: txSed_C1.createView()
-            },
-            {
-                binding: 17,
-                resource: txHardBottom.createView()
-            },
         ]
     });
-} 
\ No newline at end of file
+}
\ No newline at end of file
```


### 2.14 js/Handler_SedTrans_UpdateBottom.js

본판: `js/Handler_SedTrans_UpdateBottom.js`. transect 판: `transect_version/js/Handler_SedTrans_UpdateBottom.js`.
원래 diff는 247행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `852ec28` | 2025-06-13 | sed trans fixes |
| 본판 | `4353b85` | 2025-06-09 | Sed bugs / corrections |
| 본판 | `a98bcc4` | 2025-06-09 | sed trans updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-112 바닥 갱신 입력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_SedTrans_UpdateBottom.js:64; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_SedTrans_UpdateBottom.js:64; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 hardbottom과 초기 바닥고를 받는다. transect 판은 가상 누적 변화량을 별도로 적산한다. |

본판 차이 줄의 마지막 수정: `852ec28` 2025-06-13 (현재 91행 포함); `85c2ca2` 2024-03-19 (현재 84행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 73행 포함).

```diff
@@ -64,31 +64,13 @@
                     format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels
                     viewDimension: '2d'       // The texture is a 2D texture
                 }
-            },
-            {
-                // 7th binding: A texture that the fragment shader will sample from.
-                binding: 7,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
-            {
-                // 8th binding: A texture that the fragment shader will sample from.
-                binding: 8,
-                visibility: GPUShaderStage.COMPUTE,
-                texture: {
-                    sampleType: 'unfilterable-float',
-                    format: 'rgba32float'
-                }
-            },
+            }
         ]
     });
 }
 
 
-export function create_SedTrans_UpdateBottom_BindGroup(device, uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change, txHardBottom, txBottomInitial) {
+export function create_SedTrans_UpdateBottom_BindGroup(device, uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change) {
     return device.createBindGroup({
         layout: create_SedTrans_UpdateBottom_BindGroupLayout(device),
         entries: [
```

#### CT1-113 바닥 갱신 리소스

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Handler_SedTrans_UpdateBottom.js:122; 아래 전체 diff의 -행 | ebca435:transect_version/js/Handler_SedTrans_UpdateBottom.js:104; 아래 전체 diff의 +행 | 불일치 (A) | transect 판에는 binding 7과 8의 view가 없다. 본판 누적 변화량은 현재 바닥고에서 초기 바닥고를 뺀 값이다. |

본판 차이 줄의 마지막 수정: `852ec28` 2025-06-13 (현재 132행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -122,14 +104,6 @@
                 binding: 6,
                 resource: txtemp_SedTrans_Change.createView()
             },
-            {
-                binding: 7,
-                resource: txHardBottom.createView()
-            },
-            {
-                binding: 8,
-                resource: txBottomInitial.createView()
-            },
         ]
     });
 }
\ No newline at end of file
```


### 2.15 js/Run_Compute_Shader.js

본판: `js/Run_Compute_Shader.js`. transect 판: `transect_version/js/Run_Compute_Shader.js`.
원래 diff는 144행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `33f7ff6` | 2026-02-13 | Further encoder streamline fixes |
| 본판 | `3646fc8` | 2026-02-08 | Stacked Command Encoders |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-114 즉시 submit 함수 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Run_Compute_Shader.js:1; 아래 전체 diff의 -행 | ebca435:transect_version/js/Run_Compute_Shader.js:1; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 commandEncoder 인자를 받은 뒤 새 encoder로 다시 대입한다. 본판은 지역 const를 만든다. 해당 함수의 명령 생성·uniform 쓰기·dispatch·submit 순서는 같다. |

본판 차이 줄의 마지막 수정: `33f7ff6` 2026-02-13 (현재 6행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 6행 포함).

```diff
@@ -1,9 +1,9 @@
 // Run_Compute_Shader.js
 
-export function runComputeShader(device, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {
+export function runComputeShader(device, commandEncoder, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {
 
     // Create a new command encoder for recording GPU commands.
-    const commandEncoder = device.createCommandEncoder();
+    commandEncoder = device.createCommandEncoder();
 
     // set uniforms buffer
     device.queue.writeBuffer(uniformBuffer, 0, uniforms);
```

#### CT1-115 복사 함수 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Run_Compute_Shader.js:35; 아래 전체 diff의 -행 | ebca435:transect_version/js/Run_Compute_Shader.js:35; 아래 전체 diff의 +행 | 불일치 (F) | 양쪽은 새 encoder로 같은 WIDTH×HEIGHT를 복사한 뒤 즉시 submit한다. transect 판의 전달 encoder 값은 사용하지 않는다. |

본판 차이 줄의 마지막 수정: `33f7ff6` 2026-02-13 (현재 41행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 41행 포함).

```diff
@@ -35,10 +35,10 @@
     return await response.text();
 }
 
-export function runCopyTextures(device, calc_constants, src_texture, dst_texture) {
+export function runCopyTextures(device, commandEncoder, calc_constants, src_texture, dst_texture) {
 
     // Create a new command encoder for recording GPU commands.
-    const commandEncoder = device.createCommandEncoder();
+    commandEncoder = device.createCommandEncoder();
 
     // copy the textures
     commandEncoder.copyTextureToTexture(
```

#### CT1-116 누적 명령 encoder 없음

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Run_Compute_Shader.js:50; 아래 전체 diff의 -행 | ebca435:transect_version/js/Run_Compute_Shader.js:50; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 EncStack 함수를 export한다. transect 판은 각 계산과 복사마다 submit한다. 수치 연산을 제거한 차이는 아니다. |

본판 차이 줄의 마지막 수정: `3646fc8` 2026-02-08 (현재 89행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -50,40 +50,3 @@
     // Submit the recorded commands to the GPU for execution.
     device.queue.submit([commandEncoder.finish()]);
 }
-
-
-export function runComputeShader_EncStack(device, commandEncoder, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {
-
-    // set uniforms buffer
-    device.queue.writeBuffer(uniformBuffer, 0, uniforms);
-
-    // Begin recording commands for the compute pass.
-    const computePass = commandEncoder.beginComputePass();
-
-    // Set the compute pipeline and bind group for the compute shader.
-    computePass.setPipeline(computePipeline);
-    computePass.setBindGroup(0, computeBindGroup);
-
-    // Dispatch workgroups for the compute shader.
-    computePass.dispatchWorkgroups(dispatchX, dispatchY);
-
-    // End the compute pass after recording all its commands.
-    computePass.end();
-
-    // update the command encoder stack
-    return commandEncoder;
-}
-
-
-export function runCopyTextures_EncStack(commandEncoder, calc_constants, src_texture, dst_texture) {
-
-    // copy the textures
-    commandEncoder.copyTextureToTexture(
-        { texture: src_texture },  //src
-        { texture: dst_texture },  //dst
-        { width: calc_constants.WIDTH, height: calc_constants.HEIGHT, depthOrArrayLayers: 1 }
-    );
-
-    // update the command encoder stack
-    return commandEncoder;
-}
```


### 2.16 js/Run_Tridiag_Solver.js

본판: `js/Run_Tridiag_Solver.js`. transect 판: `transect_version/js/Run_Tridiag_Solver.js`.
원래 diff는 149행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `984091f` | 2026-05-24 | Markdown and PCR ping-pong updates |
| 본판 | `33f7ff6` | 2026-02-13 | Further encoder streamline fixes |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-117 PCR 바인드 그룹 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Run_Tridiag_Solver.js:18; 아래 전체 diff의 -행 | ebca435:transect_version/js/Run_Tridiag_Solver.js:18; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 계수 텍스처 두 개를 번갈아 읽는 바인드 그룹을 추가한다. transect 판은 매 반복 뒤 계수를 복사한다. NLSW 우회 복사의 범위는 같다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 31행 포함); `33f7ff6` 2026-02-13 (현재 38행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 32행 포함).

```diff
@@ -18,24 +18,18 @@
     TridiagX_uniforms,
     TridiagX_Pipeline,
     TridiagX_BindGroup,
-    // CODEX: Additional PCR ping-pong bind groups for copy-free coefficient handoff.
-    TridiagX_BindGroup_BaseToA,
-    TridiagX_BindGroup_BToA,
     TridiagX_view,
     TridiagY_uniformBuffer,
     TridiagY_uniforms,
     TridiagY_Pipeline,
     TridiagY_BindGroup,
-    // CODEX: Additional PCR ping-pong bind groups for copy-free coefficient handoff.
-    TridiagY_BindGroup_BaseToA,
-    TridiagY_BindGroup_BToA,
     TridiagY_view,
     runComputeShader,
     runCopyTextures
 ) {
     
     if (calc_constants.NLSW_or_Bous == 0) {
-        runCopyTextures(device, calc_constants, current_stateUVstar, txNewState)
+        runCopyTextures(device, commandEncoder, calc_constants, current_stateUVstar, txNewState)
     }
     else
     {
```

#### CT1-118 PCR 첫 계수 전달

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Run_Tridiag_Solver.js:43; 아래 전체 diff의 -행 | ebca435:transect_version/js/Run_Tridiag_Solver.js:37; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 coefMatx를 newcoef_x에 복사한다. 본판은 첫 바인드 그룹에서 coefMatx를 직접 읽는다. 최초 입력 행렬은 같다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 47행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 40행 포함).

```diff
@@ -43,8 +37,7 @@
         // X-Solve
 
         // Copy tridaig coef into newcoef for first loop
-        // CODEX: PCR now reads the base coefficient matrix directly on the first iteration.
-        // runCopyTextures(device, calc_constants, coefMatx, newcoef_x)
+        runCopyTextures(device, commandEncoder, calc_constants, coefMatx, newcoef_x)
         for (let p = 0; p < calc_constants.Px; p++) {
 
             let s = 1 << p;
```

#### CT1-119 x PCR과 y PCR 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Run_Tridiag_Solver.js:53; 아래 전체 diff의 -행 | ebca435:transect_version/js/Run_Tridiag_Solver.js:46; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 각 x 반복 후 계수를 복사한다. 본판은 교대 바인드 그룹을 쓴다. 해석: 동일한 PCR 점화식의 입력을 전달하는 두 방법이다. transect 판은 y 솔브 전체를 주석 처리한다. v=0이고 y 미분이 없으면 y 보정은 필요하지 않다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 87행 포함); `33f7ff6` 2026-02-13 (현재 91행 포함); `63a12e3` 2023-10-19 (현재 88행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 75행 포함).

```diff
@@ -53,41 +46,32 @@
             TridiagX_view.setInt32(12, s, true);            // i32, hols "s"
 
             // Dispatch the shader computation.
-            // CODEX: Select the bind group that alternates PCR coefficients between newcoef_x and txtemp_PCRx.
-            const TridiagX_BindGroup_Current = (p == 0) ? TridiagX_BindGroup_BaseToA : ((p % 2 == 1) ? TridiagX_BindGroup : TridiagX_BindGroup_BToA);
-            // runComputeShader(device, TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-            runComputeShader(device, TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup_Current, calc_constants.DispatchX, calc_constants.DispatchY);
+            runComputeShader(device, commandEncoder, TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
             // Copy reduced tridaig coef into newcoef for next loop
-            // CODEX: The next iteration reads the texture written by the selected ping-pong bind group.
-            // runCopyTextures(device, calc_constants, txtemp_PCRx, newcoef_x)
+            runCopyTextures(device, commandEncoder, calc_constants, txtemp_PCRx, newcoef_x)
         }
 
         // After all the iterations, copy the new state into current state.
-        runCopyTextures(device, calc_constants, txtemp2_PCRx, txNewState)
+        runCopyTextures(device, commandEncoder, calc_constants, txtemp2_PCRx, txNewState)
 
         // Y-Solve
 
         // Copy tridaig coef into newcoef for first loop
-        // CODEX: PCR now reads the base coefficient matrix directly on the first iteration.
-        // runCopyTextures(device, calc_constants, coefMaty, newcoef_y)
-        for (let p = 0; p < calc_constants.Py; p++) {
+       // runCopyTextures(device, commandEncoder, calc_constants, coefMaty, newcoef_y)
+       // for (let p = 0; p < calc_constants.Py; p++) {
 
-            let s = 1 << p;
+       //     let s = 1 << p;
 
-            TridiagY_view.setInt32(8, p, true);             // i32, holds "p"
-            TridiagY_view.setInt32(12, s, true);            // i32, hols "s"
+       //     TridiagY_view.setInt32(8, p, true);             // i32, holds "p"
+       //     TridiagY_view.setInt32(12, s, true);            // i32, hols "s"
 
             // Dispatch the shader computation.
-            // CODEX: Select the bind group that alternates PCR coefficients between newcoef_y and txtemp_PCRy.
-            const TridiagY_BindGroup_Current = (p == 0) ? TridiagY_BindGroup_BaseToA : ((p % 2 == 1) ? TridiagY_BindGroup : TridiagY_BindGroup_BToA);
-            // runComputeShader(device, TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-            runComputeShader(device, TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup_Current, calc_constants.DispatchX, calc_constants.DispatchY);
+       //     runComputeShader(device, commandEncoder, TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
             // Copy reduced tridaig coef into newcoef for next loop
-            // CODEX: The next iteration reads the texture written by the selected ping-pong bind group.
-            // runCopyTextures(device, calc_constants, txtemp_PCRy, newcoef_y)
-        }
+       //     runCopyTextures(device, commandEncoder, calc_constants, txtemp_PCRy, newcoef_y)
+       // }
 
         // After all the iterations, copy the new state into current state.
-        runCopyTextures(device, calc_constants, txtemp2_PCRy, txNewState)
+       // runCopyTextures(device, commandEncoder, calc_constants, txtemp2_PCRy, txNewState)
     }
 }
```


### 2.17 js/Time_Series.js

본판: `js/Time_Series.js`. transect 판: `transect_version/js/Time_Series.js`.
원래 diff는 353행이다. CR 제외 diff는 4구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `ebca435` | 2026-07-20 | fixed time series write bug |
| 본판 | `dee0e14` | 2026-02-04 | clean up memory leaks |
| 본판 | `e9d7122` | 2026-02-02 | tooltip update |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-120 코너 readback 버퍼 정리

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Time_Series.js:47; 아래 전체 diff의 -행 | ebca435:transect_version/js/Time_Series.js:47; 아래 전체 diff의 +행 | 불일치 (E) | 본판만 unmap 뒤 destroy한다. transect 판의 버퍼는 함수 안에서 생성한다. |

본판 차이 줄의 마지막 수정: `dee0e14` 2026-02-04 (현재 50행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -47,7 +47,6 @@
     calc_constants.tooltipVal_friction = bufferCopy[3] / 255.0 / 20.; // Alpha
 
     buffer.unmap(); // Don't forget to unmap the buffer once done
-    buffer.destroy();  // free up memory
 
     return bufferCopy;
 }
```

#### CT1-121 시계열 epoch 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Time_Series.js:55; 아래 전체 diff의 -행 | ebca435:transect_version/js/Time_Series.js:54; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 요청 시작 시의 epoch를 받는다. transect 판에는 비동기 초기화 경합을 구분하는 인자가 없다. |

본판 차이 줄의 마지막 수정: `ebca435` 2026-07-20 (현재 61행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 57행 포함).

```diff
@@ -55,10 +54,7 @@
 
 
 // function to read the data from a 1D texture, and store into a variable
-// export async function readToolTipTextureData(device, texture, frame_count_time_series) {
-// Added by Codex: Start carry the reset epoch so stale asynchronous readbacks cannot refill a cleared chart.
-export async function readToolTipTextureData(device, texture, frame_count_time_series, timeSeriesDataEpoch = calc_constants.timeSeriesDataEpoch) {
-    // Added by Codex: End readback reset-epoch function signature.
+export async function readToolTipTextureData(device, texture, frame_count_time_series) {
     // For a single pixel, especially in an RGBA format
     const bytesPerPixel = 16; // RGBA: 4 channels per pixel, 32 bits per channel
     const bytesPerRow = 256; // WebGPU requires bytesPerRow to be at least 256
```

#### CT1-122 시계열 초기화 경합

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Time_Series.js:97; 아래 전체 diff의 -행 | ebca435:transect_version/js/Time_Series.js:93; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 오래된 epoch의 읽기 결과를 버린다. transect 판은 frame_count_time_series==0인 비동기 읽기가 끝난 뒤 배열을 비운다. 늦게 도착한 읽기가 새 구간 자료를 지울 수 있다. 본판의 한쪽 결함 수정이다. |

본판 차이 줄의 마지막 수정: `ebca435` 2026-07-20 (현재 113행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 98행 포함).

```diff
@@ -97,20 +93,10 @@
 
     if (calc_constants.NumberOfTimeSeries > 0) {
         let time_c = bufferCopy[4]; // use only the time for the first time series - should be the same for all
-        // if (frame_count_time_series == 0){  // after we have written the data to file, or there is a change in the chart, this value is set to 0
-        //     resetTimeSeriesData();
-        //     time_c = 0.0;
-        // }
-        // Added by Codex: Start reject stale asynchronous readbacks after a reset.
-        // Resets now occur synchronously in main.js. Drop any
-        // readback started before that reset and retain the shader timestamp,
-        // which is zero-based normally and absolute for nested runs.
-        if (timeSeriesDataEpoch != calc_constants.timeSeriesDataEpoch) {
-            buffer.unmap();
-            buffer.destroy();
-            return;
+        if (frame_count_time_series == 0){  // after we have written the data to file, or there is a change in the chart, this value is set to 0
+            resetTimeSeriesData();
+            time_c = 0.0;
         }
-        // Added by Codex: End reject stale asynchronous readbacks after a reset.
         for (let i = 0; i < calc_constants.NumberOfTimeSeries; i += 1) {  // append data to existing structure
             timeSeriesData[i]['time'].push(time_c);
             timeSeriesData[i]['eta'].push(bufferCopy[(i + 1) * 4 + 1]);
```

#### CT1-123 시계열 readback 버퍼 정리

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/Time_Series.js:122; 아래 전체 diff의 -행 | ebca435:transect_version/js/Time_Series.js:108; 아래 전체 diff의 +행 | 불일치 (E) | 본판만 unmap 뒤 destroy한다. 출력 time/eta/P/Q 배열의 채널 순서는 같다. |

본판 차이 줄의 마지막 수정: `dee0e14` 2026-02-04 (현재 125행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -122,7 +108,6 @@
     }
 
     buffer.unmap(); // Don't forget to unmap the buffer once done
-    buffer.destroy();  // free up memory
 
     return;
 }
```


### 2.18 js/constants_load_calc.js

본판: `js/constants_load_calc.js`. transect 판: `transect_version/js/constants_load_calc.js`.
원래 diff는 1128행이다. CR 제외 diff는 15구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `ebca435` | 2026-07-20 | fixed time series write bug |
| 본판 | `c4be488` | 2026-07-13 | allow multiple nested grids |
| 본판 | `bb99fee` | 2026-07-02 | Added grid nesting |
| 본판 | `afc1fe7` | 2026-06-19 | Added Spherical NLSW Solver, Japan 2011 example |
| 본판 | `d778fe7` | 2026-06-02 | Added linear structures functionality |
| 본판 | `9093d7f` | 2026-06-01 | added ability to change wave conditions through the UI - on the Modify Boundary Conditions Panel |
| 본판 | `2e46d86` | 2026-04-20 | Added examples for KB |
| 본판 | `f183cc2` | 2026-02-01 | Added ability for user to specify initial 3D camera position |
| 본판 | `896c491` | 2026-01-17 | added flags to test beta-level features in code |
| 본판 | `5a5603f` | 2026-01-15 | Update constants_load_calc.js |
| 본판 | `35b7f1c` | 2026-01-15 | addition of vorticity-based momentum mixing |
| 본판 | `ea93d70` | 2025-10-24 | added Yakutat, Sebastian Inlet examples, and "p" for pause |
| 본판 | `32be94a` | 2025-10-16 | hot start initial condition option added |
| 본판 | `146a4ac` | 2025-09-28 | added Tracy Arm hot start |
| 본판 | `853c27d` | 2025-08-11 | added Endicott slide example |
| 본판 | `3be651a` | 2025-06-11 | small fixes |
| 본판 | `ba9eb67` | 2025-06-09 | added bedload to bottom update equation |
| 본판 | `4353b85` | 2025-06-09 | Sed bugs / corrections |
| 본판 | `a98bcc4` | 2025-06-09 | sed trans updates |
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| 본판 | `5c60ac0` | 2025-06-07 | add sediment diffusion term |
| 본판 | `cb7001e` | 2025-06-06 | Update constants_load_calc.js |
| 본판 | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |
| transect | `3d8a61b` | 2025-06-14 | Added many-transect version |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-124 기본 격자 유형과 디버그 옵션

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:12; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:12; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 algochanges=0과 grid_type=1을 정의한다. transect 판은 Cartesian x 단면 계산을 쓴다. |

본판 차이 줄의 마지막 수정: `896c491` 2026-01-17 (현재 17행 포함); `afc1fe7` 2026-06-19 (현재 21행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -12,13 +12,6 @@
 
 // set simulation parameters to default values
 var calc_constants = {
-    // debugging parameters
-    algochanges: 0, // set to 1 to test alternative algorithm for various parts of the code
-    
-    // Added by Codex: Start spherical-grid configuration defaults.
-    // Grid type
-    grid_type: 1, // right now spherical when =2, otherwise cartesian
-    // Added by Codex: End spherical-grid configuration defaults.
     // Computational domain dimensions
     WIDTH: 800,  // Width of the computational domain.
     HEIGHT: 600,  // Height of the computational domain.
```

#### CT1-125 마찰·초기 수면·지구 반지름 기본값

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:45; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:38; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 vort_friction_factor=0.0·loadetaIC=0·R_earth=6371000.0을 정의한다. |

본판 차이 줄의 마지막 수정: `5a5603f` 2026-01-15 (현재 48행 포함); `32be94a` 2025-10-16 (현재 50행 포함); `afc1fe7` 2026-06-19 (현재 53행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -45,12 +38,8 @@
     Theta: 2.0,  // Midmod limiter parameter. 1.0 most dissipative(upwind) to 2.0 least dissipative(centered).
     friction: 0.000,  // Dimensionless friction coefficient, or Mannings 'n', depending on isManning choice.
     isManning: 0,  // A boolean friction model value, if==1 'friction' is a Mannnigs n, otherwise it is a dimensionless friction factor (Moody).
-    vort_friction_factor: 0.0, // coefficient for vorticity-based momentum mixing/dissipation
     loadFriction: 0,  // Load friction from file when == 1
-    loadetaIC: 0,  // Load initial free surface from file when == 1
     min_allowable_depth: 0.005, // min depth allowable, too large and runup accuracy is poor, too small and precision issues lead to model blowup (1/0)
-    // Added by Codex: Earth radius used for spherical-grid metrics.
-    R_earth: 6371000.0,  // radius of earth, only used for spherical coordinate system
 
     // breaking model parameters
     useBreakingModel: 1, // inlcude breaking model when == 1
```

#### CT1-126 입사파 기본값과 경계 파일 옵션

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:74; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:63; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 H=0·T=0·direction=0·numberOfWaves=2를 둔다. 본판은 H=1·T=10·direction=0·numberOfWaves=1을 둔다. transect 판은 파 성분 수를 파일 헤더에서 갱신하지 않는다. 본판만 trough_factor=1과 4변 시계열 파일·관측점 수·시각 이동을 정의한다. |

본판 차이 줄의 마지막 수정: `9093d7f` 2026-06-01 (현재 80행 포함); `bb99fee` 2026-07-02 (현재 95행 포함); `63a12e3` 2023-10-19 (현재 96행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 70행 포함); `3d8a61b` 2025-06-14 (현재 69행 포함).

```diff
@@ -74,26 +63,11 @@
     rand_phase: 0.0,
 
     // incident wave properties
-    incident_wave_H: 1.,  // Height (m) of Sine Wave / Pulse / Solitary Wave, or Significant Wave Height of Spectrum
-    incident_wave_T: 10.,  //Period (sec) of Sine Wave / Pulse, or Peak Period of Spectrum [not used for Solitary Wave]
-    incident_wave_direction: 0.,  // Wave Direction (deg CCW from E [-180 to 180])
-    numberOfWaves: 1., // number of wave components to be created
-    trough_factor: 1.0, // factor to increase or decrease the trough amplitude of the wave.  Needed in the ASCE-16 and 22 for incident waveform. ONLY used when globals.incident_wave_type == 2
-
-    // Added by Codex: Start boundary time-series forcing file defaults.
-    ts_west_file: "", // file for west boundary type 5 eta/hu/hv time-series forcing
-    ts_east_file: "", // file for east boundary type 5 eta/hu/hv time-series forcing
-    ts_south_file: "", // file for south boundary type 5 eta/hu/hv time-series forcing
-    ts_north_file: "", // file for north boundary type 5 eta/hu/hv time-series forcing
-    ts_west_num_points: 0, // number of loaded type-5 forcing stations on the west boundary
-    ts_east_num_points: 0, // number of loaded type-5 forcing stations on the east boundary
-    ts_south_num_points: 0, // number of loaded type-5 forcing stations on the south boundary
-    ts_north_num_points: 0, // number of loaded type-5 forcing stations on the north boundary
-    // Added by Codex: Start global time shift for nested boundary time-series forcing.
-    start_time_shift: 0.0, // added to model total_time when type-5 boundary files start at a nonzero parent-grid time
-    // Added by Codex: End global time shift for nested boundary time-series forcing.
-    // Added by Codex: End boundary time-series forcing file defaults.
-
+    incident_wave_H: 0,  // Height (m) of Sine Wave / Pulse / Solitary Wave, or Significant Wave Height of Spectrum
+    incident_wave_T: 0,  //Period (sec) of Sine Wave / Pulse, or Peak Period of Spectrum [not used for Solitary Wave]
+    incident_wave_direction: 0,  // Wave Direction (deg CCW from E [-180 to 180])
+    numberOfWaves: 2, // number of wave components to be created
+    
     // Vessel motion parameters (initial development)
     ship_posx: -100.0,  // initial ship position, if initially inside domain, the initial free surface must include the ship displacement 
     ship_posy: 450.0,
```

#### CT1-127 퇴적물 확장 기본값

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:109; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:83; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 sedTurbDispersion=0.01·sedBreakingDispersionCoef=0.1·loadHardBottom=0을 정의한다. |

본판 차이 줄의 마지막 수정: `3be651a` 2025-06-11 (현재 113행 포함); `b8b50c3` 2025-06-08 (현재 114행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -109,9 +83,6 @@
     sedC1_psi: 0.00005,   // psi for Class 1 sed
     sedC1_criticalshields: 0.045,   // critical shields for Class 1 sed
     sedC1_denrat: 2.65,   // desnity sed / desnity water for Class 1 sed
-    sedTurbDispersion: 0.01, // eddy viscosity constant (background) value for sediment transport
-    sedBreakingDispersionCoef: 0.1, // fraction of breaking eddy viscosity to use for sediment transport dispersion
-    loadHardBottom: 0, // load hard bottom from file when == 1
 
     // River sim parameters
     river_sim: 0, // equal to oneif running a river simulation, using river.html
```

#### CT1-128 예제 목록과 기본 색상

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:194; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:165; 아래 전체 diff의 +행 | 불일치 (A) | transect 판의 예제 목록은 Hermosa_Beach_CA_COULWAVE에서 끝난다. 예제 내부는 판독하지 않는다. 기본 colorMap_choice는 본판 0이고 transect 2다. |

본판 차이 줄의 마지막 수정: `853c27d` 2025-08-11 (현재 197행 포함); `146a4ac` 2025-09-28 (현재 198행 포함); `32be94a` 2025-10-16 (현재 199행 포함); `ea93d70` 2025-10-24 (현재 201행 포함); `2e46d86` 2026-04-20 (현재 212행 포함); `afc1fe7` 2026-06-19 (현재 214행 포함); `2eb2866` 2023-10-26 (현재 220행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 168행 포함); `3d8a61b` 2025-06-14 (현재 174행 포함).

```diff
@@ -194,30 +165,13 @@
         "./examples/Portage_Lake_AK/",
         "./examples/Greenland_Umanak/",
         "./examples/LA_River_Model_Large/",
-        "./examples/Hermosa_Beach_CA_COULWAVE/",
-        "./examples/Endicott_slide/",
-        "./examples/TracyArm_hotstart/",
-        "./examples/Portage_Lake_AK_rotated/",
-        "./examples/Yakutat_slide/",
-        "./examples/Sebastian_Inlet_FL/",
-        "./examples/MC_Duck_H1_T08_Normal/",
-        "./examples/MC_Duck_H2_T15_Normal/",
-        "./examples/MC_Duck_H2_T15_NE/",
-        "./examples/MC_Lejuene_H1_T08_Normal/",
-        "./examples/MC_Lejuene_H1_T08_NE/",
-        "./examples/MC_Lejuene_H2_T15_Normal/",
-        "./examples/MC_Pendelton_H2_T15_Normal/",
-        "./examples/MC_Pendelton_H2_T15_SW/", 
-        "./examples/MC_Newport_H3_T18_Normal/", 
-        "./examples/MC_Newport_H3_T18_SW/",
-        "./examples/MC_PyramidRock_H2_T15_Normal/",
-        "./examples/Japan2011_tsunami/"
+        "./examples/Hermosa_Beach_CA_COULWAVE/"
       ],
 
     // plotting parameters
     colorVal_max: 1.0,  // value that maps to the "highest" color
     colorVal_min: -1.0,  // value that maps to the "lowest" color
-    colorMap_choice: 0,  // decision variable for the colormap to use during rendering
+    colorMap_choice: 2,  // decision variable for the colormap to use during rendering
     surfaceToPlot: 0, // which surface (eta, u, v, vort) to plot
     bathy_cmap_zero: 0.0, // shift in the topo shading colormap, sometimes need to move to see topo
     showBreaking: 1,  //  show breaking (foam) areas when ==1
```

#### CT1-129 점 시계열 초기화 상태

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:255; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:209; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 timeSeriesChartStartTime과 timeSeriesDataEpoch를 0으로 정의한다. |

본판 차이 줄의 마지막 수정: `ebca435` 2026-07-20 (현재 261행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -255,10 +209,6 @@
     countTimeSeries: 0, // count of points stored in time series
     durationTimeSeries: 0., // current time series duration
     maxdurationTimeSeries: 120., // time series duration to plot, time series resets after this time.
-    // Added by Codex: Start point time-series reset state.
-    timeSeriesChartStartTime: 0.0, // current point-series chart-window start, zero normally and absolute time for nested runs
-    timeSeriesDataEpoch: 0, // invalidates asynchronous point-series readbacks issued before a chart reset
-    // Added by Codex: End point time-series reset state.
     maxNumberOfTimeSeries: 16, // max number of time series allowed, inlcuding tooltip, if greater than 16, need to update readToolTipTextureData bytesperrow.  SHould be 16*N time series
     NumberOfTimeSeries: 0, //  number of time series right now
     changethisTimeSeries: 1, // changing location of this time series
```

#### CT1-130 사용자 초기 카메라

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:306; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:256; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 초기 카메라 위치·yaw·pitch와 활성 플래그를 정의한다. |

본판 차이 줄의 마지막 수정: `f183cc2` 2026-02-01 (현재 314행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -306,12 +256,6 @@
     shift_x: 0.0, // x shift of 2D plane
     shift_y: 0.0, // y shift of 2D plane
     forward: 1.0, // zoom in/out of 2D plane
-    cameraInit_user: 0, // flag to indicate user has initialized camera position
-    cameraInit_x: 0.0, // initial camera x position for 3D explorer
-    cameraInit_y: 0.0, // initial camera y position for 3D explorer
-    cameraInit_z: 0.0, // initial camera z position for 3D explorer
-    cameraInit_yaw: 0.0, // initial camera yaw for 3D explorer
-    cameraInit_pitch: 0.0, // initial camera pitch for 3D explorer
     full_screen: 0, // = 0 regular, = 1 in fullscreen
     canvas_width_ratio: 1.0, // for full screen asepct ratio correction
     canvas_height_ratio: 1.0, // for full screen asepct ratio correction
```

#### CT1-131 선형 구조물 상태

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:326; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:270; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 천단고 0·천단폭 1·사면경사 0.25·끝점 좌표·미리보기·적용 플래그를 정의한다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 344행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -326,22 +270,6 @@
     whichPanelisOpen: 0, // tracks which GUI panel is currently maximized
     designcomponentToAdd: 1,  // which component to add
     designcomponent_Radius: 100.0, // radius of addition for surface cover components
-    // CODEX: Linear-structure design parameters and endpoint preview state.
-    designcomponent_CrestElev: 0.0, // crest elevation for linear structures
-    designcomponent_CrestWidth: 1.0, // crest width for linear structures
-    designcomponent_SideSlope: 0.25, // side slope for linear structures
-    designcomponent_CurrentEndPoint: 1, // selected linear-structure endpoint, 1=start and 2=end
-    designcomponent_xLoc: 0.0, // current linear-structure endpoint x-coordinate in meters
-    designcomponent_yLoc: 0.0, // current linear-structure endpoint y-coordinate in meters
-    designcomponent_StartX: 0.0, // stored linear-structure start x-coordinate in meters
-    designcomponent_StartY: 0.0, // stored linear-structure start y-coordinate in meters
-    designcomponent_EndX: 0.0, // stored linear-structure end x-coordinate in meters
-    designcomponent_EndY: 0.0, // stored linear-structure end y-coordinate in meters
-    designcomponent_StartDefined: 0, // start endpoint has been defined when 1
-    designcomponent_EndDefined: 0, // end endpoint has been defined when 1
-    designcomponent_PreviewOn: 0, // render linear-structure endpoint/line preview when 1
-    // CODEX: Pending action flag for applying the linear structure to bathy/topo through MouseClickChange.wgsl.
-    designcomponent_AddLinearStructure: 0, // add linear structure to bathy/topo when 1
     designcomponent_Friction: 0.0, // friction factor of the component currently being added
     designcomponent_Fric_Coral: 0.1, // Coral Reef  friction factor
     designcomponent_Fric_Oyser: 0.035, // Mussel/Oyster Bed friction factor
```

#### CT1-132 중첩 격자 출력 설정

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:370; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:298; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 사각형 인덱스·기간·간격·최대 8192 표본·트리거·접두어·사각형 배열·eta 임계값·시작시각을 정의한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 394행 포함); `c4be488` 2026-07-13 (현재 389행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -370,28 +298,6 @@
     fileWritePause: 100, // time (ms) to pause during 2D surface write to not overload write buffer
     write_individual_surface: 0, // flag to write individual 2D surface
     which_surface_to_write: 0,  // flag for which surface to write 
-    // Added by Codex: Start nested-grid boundary time-series output parameters.
-    nestedGridOutput_i0: 0, // lower-left rectangle i-index for nested boundary output
-    nestedGridOutput_j0: 0, // lower-left rectangle j-index for nested boundary output
-    nestedGridOutput_i1: 100, // upper-right rectangle i-index for nested boundary output
-    nestedGridOutput_j1: 100, // upper-right rectangle j-index for nested boundary output
-    nestedGridOutput_start_time: 0.0, // simulation time to start nested boundary output
-    nestedGridOutput_end_time: 0.0, // simulation time to end nested boundary output
-    nestedGridOutput_dt: 1.0, // requested nested boundary output interval
-    nestedGridOutput_max_samples: 8192, // hard cap on stored output times
-    nestedGridOutput_trigger: 0, // set to 1 to allocate textures and start nested boundary output
-    nestedGridOutput_active: 0, // 1 while nested boundary output is actively sampling
-    nestedGridOutput_sample_count: 0, // derived number of output samples after dt cap
-    nestedGridOutput_sample_index: 0, // current output sample index
-    nestedGridOutput_file_prefix: "nested", // prefix for generated boundary time-series files
-    // Added by Codex: Optional multi-rectangle nested-grid output specs; absent/empty keeps legacy scalar config behavior.
-    nestedGridOutput_rectangles: [],
-    nestedGridOutput_rectangle_count: 0, // number of active nested-grid output rectangles after normalization
-    // Added by Codex: Start nested-grid boundary output threshold parameters.
-    nestedEtaWriteThreshold: 0.0, // eta magnitude threshold that trims leading quiet samples when > 0
-    nestedGridOutput_actual_start_time: 0.0, // absolute simulation time used as t=0 in trimmed nested files
-    // Added by Codex: End nested-grid boundary output threshold parameters.
-    // Added by Codex: End nested-grid boundary time-series output parameters.
 
     // save trigger parameters, for automatically saving data
     trigger_animation: 0, // user trigger / automation when = 1,
```

#### CT1-133 구면 시간 간격과 강제 모드

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:449; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:355; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 구면에서 NLSW와 2차 재구성을 강제한다. 본판은 퇴적물과 쇄파를 끈다. 본판은 위도별 물리 격자간격의 최소값으로 dt를 정한다. Cartesian 식은 두 판에서 같다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 488행 포함); `38a5072` 2025-01-21 (현재 486행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 358행 포함).

```diff
@@ -449,43 +355,7 @@
     }
 
     // Add/update parameters in calc_constants
-    // calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);
-    // Added by Codex: Start grid-type-specific timestep support.
-    if (calc_constants.grid_type == 2) {
-        if (calc_constants.NLSW_or_Bous != 0) {
-            console.warn("Spherical grid mode is currently NLSW-only; forcing NLSW_or_Bous to 0.");
-            calc_constants.NLSW_or_Bous = 0;
-        }
-        if (calc_constants.Accuracy_mode != 0) {
-            console.warn("Spherical grid mode currently uses the standard second-order NLSW path; forcing Accuracy_mode to 0.");
-            calc_constants.Accuracy_mode = 0;
-        }
-        if (calc_constants.useSedTransModel != 0) {
-            console.warn("Spherical grid mode does not currently support sediment transport; forcing useSedTransModel to 0.");
-            calc_constants.useSedTransModel = 0;
-        }
-        if (calc_constants.useBreakingModel != 0) {
-            console.warn("Spherical grid mode does not currently support the Cartesian breaking model; forcing useBreakingModel to 0.");
-            calc_constants.useBreakingModel = 0;
-        }
-
-        const degToRad = Math.PI / 180.0;
-        const dlonRad = Math.max(Math.abs(calc_constants.dx) * degToRad, 1.0e-12);
-        const dlatRad = Math.max(Math.abs(calc_constants.dy) * degToRad, 1.0e-12);
-        const earthRadius = Math.max(calc_constants.R_earth, 1.0);
-        let minPhysicalGridSpacing = earthRadius * dlatRad;
-        for (let y = 0; y < calc_constants.HEIGHT; y++) {
-            // const latRad = (calc_constants.lat_LL + y * calc_constants.dy) * degToRad;
-            // Added by Codex: Use cell-center latitude because lat_LL is the lower-left corner.
-            const latRad = (calc_constants.lat_LL + (y + 0.5) * calc_constants.dy) * degToRad;
-            const cosLat = Math.max(Math.abs(Math.cos(latRad)), 1.0e-6);
-            minPhysicalGridSpacing = Math.min(minPhysicalGridSpacing, earthRadius * cosLat * dlonRad);
-        }
-        calc_constants.dt = calc_constants.Courant_num * minPhysicalGridSpacing / Math.sqrt(calc_constants.g * calc_constants.base_depth);
-    } else {
-        calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);
-    }
-    // Added by Codex: End grid-type-specific timestep support.
+    calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);
     calc_constants.TWO_THETA = calc_constants.Theta * 2.0;
     calc_constants.half_g = calc_constants.g / 2.0;
     calc_constants.Bcoef_g = calc_constants.Bcoef * calc_constants.g;
```

#### CT1-134 예제 목록 공백과 번호 주석 1

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:521; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:391; 아래 전체 diff의 +행 | 불일치 (F) | 문자열 값과 순서는 같다. 공백과 //10 주석만 다르다. |

본판 차이 줄의 마지막 수정: `7f9c6aa` 2024-04-25 (현재 524행 포함); `2e46d86` 2026-04-20 (현재 525행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 395행 포함).

```diff
@@ -521,8 +391,8 @@
         "./examples/Greenland/",
         "./examples/Half_Moon_Bay/",
         "./examples/Hania_Greece/",
-        "./examples/Miami_Beach_FL/", 
-        "./examples/Miami_FL/",  //10
+        "./examples/Miami_Beach_FL/",
+        "./examples/Miami_FL/",
         "./examples/Newport_OR/",
         "./examples/POLALB/",
         "./examples/SantaBarbara/",
```

#### CT1-135 예제 목록 공백과 번호 주석 2

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:531; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:401; 아래 전체 diff의 +행 | 불일치 (F) | 문자열 값과 순서는 같다. 공백과 //20 주석만 다르다. |

본판 차이 줄의 마지막 수정: `7f9c6aa` 2024-04-25 (현재 534행 포함); `2e46d86` 2026-04-20 (현재 535행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 405행 포함).

```diff
@@ -531,8 +401,8 @@
         "./examples/SF_Bay_tides/",
         "./examples/OSU_Seaside/",
         "./examples/Scripps_Pier/",
-        "./examples/Scripps_Canyon/",  
-        "./examples/Newport_Jetties_CA/",  //20
+        "./examples/Scripps_Canyon/",
+        "./examples/Newport_Jetties_CA/",
         "./examples/Waimea_Bay/",
         "./examples/Tyndall_FL/",
         "./examples/Mavericks/",
```

#### CT1-136 초기화 함수 안 예제 목록

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:541; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:411; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 목록을 Hermosa_Beach_CA_COULWAVE까지 재정의한다. 본판은 뒤에 추가한 예제 경로를 유지한다. //30 같은 번호 주석 차이는 동작을 바꾸지 않는다. |

본판 차이 줄의 마지막 수정: `7f7d072` 2024-05-16 (현재 544행 포함); `2e46d86` 2026-04-20 (현재 567행 포함); `853c27d` 2025-08-11 (현재 552행 포함); `146a4ac` 2025-09-28 (현재 553행 포함); `32be94a` 2025-10-16 (현재 554행 포함); `ea93d70` 2025-10-24 (현재 556행 포함); `afc1fe7` 2026-06-19 (현재 569행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 422행 포함).

```diff
@@ -541,32 +411,15 @@
         "./examples/Blacks_Beach_CA/",
         "./examples/Hermosa_Beach_CA/",
         "./examples/Morro_Rock_CA/",
-        "./examples/Pacifica_CA/", 
-        "./examples/Toy_Config/",  //30
+        "./examples/Pacifica_CA/",
+        "./examples/Toy_Config/",
         "./examples/Harrison_Lake/",
         "./examples/LA_River_Model/",
         "./examples/Oceanside_CA/",
         "./examples/Portage_Lake_AK/",
         "./examples/Greenland_Umanak/",
         "./examples/LA_River_Model_Large/",
-        "./examples/Hermosa_Beach_CA_COULWAVE/",
-        "./examples/Endicott_slide/",
-        "./examples/TracyArm_hotstart/",
-        "./examples/Portage_Lake_AK_rotated/",  //40
-        "./examples/Yakutat_slide/", 
-        "./examples/Sebastian_Inlet_FL/",
-        "./examples/MC_Duck_H1_T08_Normal/",
-        "./examples/MC_Duck_H2_T15_Normal/",
-        "./examples/MC_Duck_H2_T15_NE/",
-        "./examples/MC_Lejuene_H1_T08_Normal/",
-        "./examples/MC_Lejuene_H1_T08_NE/",
-        "./examples/MC_Lejuene_H2_T15_Normal/",
-        "./examples/MC_Pendelton_H2_T15_Normal/",
-        "./examples/MC_Pendelton_H2_T15_SW/",  //50
-        "./examples/MC_Newport_H3_T18_Normal/", 
-        "./examples/MC_Newport_H3_T18_SW/",
-        "./examples/MC_PyramidRock_H2_T15_Normal/",
-        "./examples/Japan2011_tsunami/"
+        "./examples/Hermosa_Beach_CA_COULWAVE/"
       ],
 
     calc_constants.setRenderStep = 0; // sim always starts trying to find best render step, eases into simulation
```

#### CT1-137 중첩 출력 표본 수 제한

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:574; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:427; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 양의 간격을 보장하고 표본 수가 상한을 넘으면 간격을 늘린다. 기간 0은 표본 1개다. 활성 사각형 수를 별도로 센다. transect 판에는 해당 계산이 없다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 599행 포함); `c4be488` 2026-07-13 (현재 598행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -574,29 +427,6 @@
     calc_constants.n_write_interval = Math.ceil(calc_constants.write_dt / calc_constants.dt);
     calc_constants.write_dt = calc_constants.n_write_interval * calc_constants.dt;
     calc_constants.n_writes = Math.floor((calc_constants.end_write_time - calc_constants.start_write_time) / calc_constants.write_dt) + 1;
-    // Added by Codex: Start nested-grid boundary time-series sample cap.
-    const nestedOutputMaxSamples = Math.max(1, Math.floor(calc_constants.nestedGridOutput_max_samples || 8192));
-    const nestedOutputDuration = Math.max(0.0, calc_constants.nestedGridOutput_end_time - calc_constants.nestedGridOutput_start_time);
-    if (calc_constants.nestedGridOutput_dt <= 0.0) {
-        calc_constants.nestedGridOutput_dt = Math.max(calc_constants.dt, 1.0e-6);
-    }
-    let nestedOutputSampleCount = Math.floor(nestedOutputDuration / calc_constants.nestedGridOutput_dt) + 1;
-    if (nestedOutputDuration == 0.0) {
-        nestedOutputSampleCount = 1;
-    }
-    if (nestedOutputSampleCount > nestedOutputMaxSamples) {
-        calc_constants.nestedGridOutput_dt = nestedOutputDuration / Math.max(nestedOutputMaxSamples - 1, 1);
-        nestedOutputSampleCount = nestedOutputMaxSamples;
-        console.warn(`Nested-grid boundary output requested more than ${nestedOutputMaxSamples} samples; increasing nestedGridOutput_dt to ${calc_constants.nestedGridOutput_dt}.`);
-    }
-    calc_constants.nestedGridOutput_sample_count = nestedOutputSampleCount;
-    // Added by Codex: Report configured rectangle count while keeping scalar sample-count behavior for legacy configs.
-    if (Array.isArray(calc_constants.nestedGridOutput_rectangles) && calc_constants.nestedGridOutput_rectangles.length > 0) {
-        calc_constants.nestedGridOutput_rectangle_count = calc_constants.nestedGridOutput_rectangles.filter((rectangle) => Number(rectangle?.enabled ?? 1) != 0).length;
-    } else {
-        calc_constants.nestedGridOutput_rectangle_count = 1;
-    }
-    // Added by Codex: End nested-grid boundary time-series sample cap.
 
     calc_constants.ThreadX = 16;
     calc_constants.ThreadY = 16;
```

#### CT1-138 침강속도와 Shields 계수

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/constants_load_calc.js:614; 아래 전체 diff의 -행 | ebca435:transect_version/js/constants_load_calc.js:444; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 g를 사용하고 nu=1e-6·A=25·B=1.25·n=1로 자연 입자 침강속도를 계산한다. transect 판은 9.81을 고정하고 sqrt((4/3)*9.81*d/0.2*(denrat-1))를 쓴다. 본판만 MPM 계수를 만든다. d50의 mm→m 변환은 같다. |

본판 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 631행 포함); `ba9eb67` 2025-06-09 (현재 620행 포함); `b8b50c3` 2025-06-08 (현재 633행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 449행 포함).

```diff
@@ -614,23 +444,9 @@
     calc_constants.changeAmplitude = 0.1 * calc_constants.base_depth;
 
     calc_constants.sedC1_erosion = calc_constants.sedC1_psi*Math.pow(calc_constants.sedC1_d50/1000.,-0.2);
-    
-    calc_constants.sedC1_shields = 1.0 / ( (calc_constants.sedC1_denrat - 1.0) * calc_constants.g  * calc_constants.sedC1_d50/1000.);
-
-    calc_constants.sedC1_bedloadMPM = 8.0 * Math.sqrt(calc_constants.g  * (calc_constants.sedC1_denrat - 1.0) * Math.pow(calc_constants.sedC1_d50/1000., 3.0));
-    
-    let nu = 0.000001; // kinematic viscosity of water in m^2/s
-    let delta = calc_constants.sedC1_denrat - 1.0;
-    let d = calc_constants.sedC1_d50/1000.; // convert d50 to meters
-    let ds =  d * Math.pow(delta * calc_constants.g / (nu * nu) , 1.0 / 3.0)   // (delta*g/nu^2)^(1/3)*d
-    let A = 25; // shape factor, natural particles
-    let B = 1.25; // shape factor, natural particles
-    let n = 1.0; // exponent for fall velocity, natural particles
-    let fall_vel = nu / d * (Math.sqrt(0.25 * (A / B) ** (2 / n) + (4 / 3 * (ds ** 3 / B)) ** (1 / n)) - 0.5 * (A / B) ** (1 / n)) ** n; // fall velocity for natural particles; nu/d*(sqrt(0.25*(A/B)^(2/n)+(4/3*(ds^3/B))^(1/n))-0.5*(A/B)^(1/n))^n
-    calc_constants.sedC1_fallvel = fall_vel; // set the fall velocity for Class 1 sediment
-    // console.log(ds, fall_vel)
-    //let fall_vel_a = 4.0 / 3.0 * 9.81 * calc_constants.sedC1_d50/1000. / 0.2 * (calc_constants.sedC1_denrat - 1.0); 
-    //calc_constants.sedC1_fallvel = Math.pow(fall_vel_a, 0.5);
+    calc_constants.sedC1_shields = 1.0 / ( (calc_constants.sedC1_denrat - 1.0) * 9.81 * calc_constants.sedC1_d50/1000.);
+    let fall_vel_a = 4.0 / 3.0 * 9.81 * calc_constants.sedC1_d50/1000. / 0.2 * (calc_constants.sedC1_denrat - 1.0); 
+    calc_constants.sedC1_fallvel = Math.pow(fall_vel_a, 0.5);
  
     // Set the canvas dimensions based on the above-defined WIDTH and HEIGHT values.
     let grid_ratio = calc_constants.dx / calc_constants.dy;
```


### 2.19 js/display_parameters.js

본판: `js/display_parameters.js`. transect 판: `transect_version/js/display_parameters.js`.
원래 diff는 470행이다. CR 제외 diff는 5구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `ff0d046` | 2026-07-07 | time series plot updates for spherical grids |
| 본판 | `bb99fee` | 2026-07-02 | Added grid nesting |
| 본판 | `7ae7da4` | 2026-02-23 | Minor fixes - additional debug info, and landslide volume fix |
| 본판 | `dee0e14` | 2026-02-04 | clean up memory leaks |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-139 측정점 좌표 표시

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/display_parameters.js:120; 아래 전체 diff의 -행 | ebca435:transect_version/js/display_parameters.js:120; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 구면 격자에서 절대 경위도와 소수 6자리를 쓴다. transect 판은 상대 X/Y와 소수 2자리를 쓴다. |

본판 차이 줄의 마지막 수정: `ff0d046` 2026-07-07 (현재 138행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 125행 포함).

```diff
@@ -120,22 +120,9 @@
     container.innerHTML = ''; // Clear previous contents
 
     for (let i = 1; i < calc_constants.NumberOfTimeSeries+1; i++) {
-        // Added by Codex: Display absolute lon/lat for spherical grids while internal time-series storage remains lower-left-relative.
-        const isSphericalGrid = Math.round(calc_constants.grid_type) == 2;
-        const xDisplay = isSphericalGrid
-            ? calc_constants.lon_LL + calc_constants.locationOfTimeSeries[i].xts
-            : calc_constants.locationOfTimeSeries[i].xts;
-        const yDisplay = isSphericalGrid
-            ? calc_constants.lat_LL + calc_constants.locationOfTimeSeries[i].yts
-            : calc_constants.locationOfTimeSeries[i].yts;
-        const xLabel = isSphericalGrid ? 'Lon' : 'X';
-        const yLabel = isSphericalGrid ? 'Lat' : 'Y';
         const locationInfo = `Location ${Math.round(i)}, ` +
-                             // `X: ${Math.round(calc_constants.locationOfTimeSeries[i].xts * 100) / 100}, ` +
-                             // `Y: ${Math.round(calc_constants.locationOfTimeSeries[i].yts * 100) / 100}<br>`;
-                             // Added by Codex: Use grid-aware labels and values in the time-series location list.
-                             `${xLabel}: ${Math.round(xDisplay * 1000000) / 1000000}, ` +
-                             `${yLabel}: ${Math.round(yDisplay * 1000000) / 1000000}<br>`;
+                             `X: ${Math.round(calc_constants.locationOfTimeSeries[i].xts * 100) / 100}, ` +
+                             `Y: ${Math.round(calc_constants.locationOfTimeSeries[i].yts * 100) / 100}<br>`;
         container.innerHTML += locationInfo; // Append location info directly with line breaks
     }
 }
```

#### CT1-140 수상 사면 체적 표시

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/display_parameters.js:155; 아래 전체 diff의 -행 | ebca435:transect_version/js/display_parameters.js:142; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 진폭*폭*길이를 Mm^3로 환산한다. 본판은 그 값의 0.25배를 쓴다. 교란 함수의 체적 계수와 한쪽 수정 이력을 대조한다. |

본판 차이 줄의 마지막 수정: `7ae7da4` 2026-02-23 (현재 158행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 145행 포함).

```diff
@@ -155,7 +142,7 @@
     container.innerHTML = ''; // Clear previous contents
 
     if(calc_constants.disturbanceType == 4) {
-        let slide_vol = 0.25 * calc_constants.disturbanceCrestamp * calc_constants.disturbanceWidth * calc_constants.disturbanceLength / 1000000.0;
+        let slide_vol = calc_constants.disturbanceCrestamp * calc_constants.disturbanceWidth * calc_constants.disturbanceLength / 1000000.0;
         
         const slideInfo = `Displaced Water Volume (Mm^3) from Subaerial Slide: ${slide_vol}<br>`;
         container.innerHTML += slideInfo; // Append location info directly with line breaks
```

#### CT1-141 로그 DOM 증가 제한

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/display_parameters.js:200; 아래 전체 diff의 -행 | ebca435:transect_version/js/display_parameters.js:187; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 최대 200개 entry만 유지한다. transect 판은 이 제한이 없다. 메모리 정리 수정 이력과 루프 호출을 함께 근거로 둔다. |

본판 차이 줄의 마지막 수정: `dee0e14` 2026-02-04 (현재 207행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -200,11 +187,6 @@
     const entry = document.createElement('div');
     entry.textContent = text;
     container.appendChild(entry);
-
-    const maxEntries = 200; // <-- set desired cap here
-    while (container.childNodes.length > maxEntries) {
-        container.removeChild(container.firstChild);
-    }
 }
```

#### CT1-142 type-5 경계 표시

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/display_parameters.js:232; 아래 전체 diff의 -행 | ebca435:transect_version/js/display_parameters.js:214; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 파일 시계열 경계라는 표시 문자열을 제공한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 239행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -232,11 +214,6 @@
     } else if (boundaryType == 3) {
         boundaryDescription = `${direction} Boundary: Periodic Boundary`;
     }
-    // Added by Codex: Start display label for boundary time-series forcing.
-    else if (boundaryType == 5) {
-        boundaryDescription = `${direction} Boundary: Time Series from loaded file`;
-    }
-    // Added by Codex: End display label for boundary time-series forcing.
 
     // Use the utility function to add the text to the container
     addTextToContainer(boundaryDescription, container);
```

#### CT1-143 마지막 줄 개행

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/display_parameters.js:248; 아래 전체 diff의 -행 | ebca435:transect_version/js/display_parameters.js:225; 아래 전체 diff의 +행 | 불일치 (F) | 함수 본문은 같다. 마지막 줄의 개행 유무만 다르다. |

본판 차이 줄의 마지막 수정: `cf9de63` 2023-10-24 (현재 251행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 228행 포함).

```diff
@@ -248,4 +225,4 @@
     const spacer = document.createElement("div");
     spacer.style.height = height;
     container.appendChild(spacer);
-}
+}
\ No newline at end of file
```


### 2.20 shaders/AddDisturbance.wgsl

본판: `shaders/AddDisturbance.wgsl`. transect 판: `transect_version/shaders/AddDisturbance.wgsl`.
원래 diff는 478행이다. CR 제외 diff는 7구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `185e91c` | 2026-01-30 | Update AddDisturbance.wgsl |
| 본판 | `4c903ea` | 2026-01-30 | Update AddDisturbance.wgsl |
| 본판 | `c92521c` | 2026-01-30 | Update AddDisturbance.wgsl |
| 본판 | `3425a4a` | 2026-01-30 | Update AddDisturbance.wgsl |
| 본판 | `8c2b62b` | 2025-08-24 | Added Tracy Arm Example, some landslide viz additions |
| 본판 | `4353b85` | 2025-06-09 | Sed bugs / corrections |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-144 교란 누적 바닥고 입력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/AddDisturbance.wgsl:36; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/AddDisturbance.wgsl:36; 아래 전체 diff의 +행 | 불일치 (E) | transect 판에는 txBotChange_Sed 입력이 없다. 본판의 침식 누적 보존 수정과 연결된다. |

본판 차이 줄의 마지막 수정: `4353b85` 2025-06-09 (현재 39행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 39행 포함).

```diff
@@ -36,7 +36,7 @@
 @group(0) @binding(4) var txtemp_AddDisturbance: texture_storage_2d<rgba32float, write>;
 @group(0) @binding(5) var txBoundaryForcing: texture_storage_2d<rgba32float, write>;
 @group(0) @binding(6) var txtemp_bottom: texture_storage_2d<rgba32float, write>;
-@group(0) @binding(7) var txBotChange_Sed: texture_2d<f32>; 
+
 
 fn solitary_wave(xloc: f32, yloc: f32, amplitude: f32, angle: f32, depth: f32, bottom: f32) -> vec4<f32> {
     let k = sqrt(0.75 * abs(amplitude)/pow(depth,3.0));
```

#### CT1-145 교란 시간 상한

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/AddDisturbance.wgsl:105; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/AddDisturbance.wgsl:105; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 time_local을 1.0e5*dt 이하로 제한한다. transect 판은 원래 time을 쓴다. |

본판 차이 줄의 마지막 수정: `185e91c` 2026-01-30 (현재 110행 포함); `3425a4a` 2026-01-30 (현재 112행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -105,11 +105,6 @@
 
 fn depth_motion(xloc_in: f32, yloc_in: f32, bottom: f32, time: f32, dt: f32, bottom_initial: f32) -> vec4<f32> {
     
-    var time_local = time;
-    if (time_local > 1.0e5*dt) {
-        time_local = 1.0e5*dt;
-    }
-
     let change_timescale = globals.disturbance_change_timescale;
     let time_shift = globals.disturbance_time_shift;
     let max_displacement = globals.disturbance_max_distance;
```

#### CT1-146 사면체 방향 정의

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/AddDisturbance.wgsl:117; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/AddDisturbance.wgsl:112; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 globals.disturbanceDir를 사용한다. 본판은 뒤에서 3.1415-traj_angle을 사용한다. |

본판 차이 줄의 마지막 수정: `8c2b62b` 2025-08-24 (현재 120행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 115행 포함).

```diff
@@ -117,7 +112,7 @@
     let traj_timefactor = globals.disturbance_traj_timefactor;
     let final_traj = globals.disturbance_final_traj;
 
-    //let angle = globals.disturbanceDir;
+    let angle = globals.disturbanceDir;
     let p3 = globals.disturbanceLength;
     let p4 = globals.disturbanceWidth;
```

#### CT1-147 사면 이동 궤적

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/AddDisturbance.wgsl:125; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/AddDisturbance.wgsl:120; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 초기·최종 각도의 차이에 traj_timefactor를 곱한다. transect 판은 변위 비율에 traj_timefactor만 곱한다. 본판은 사면체 회전각도 궤적에 연결한다. |

본판 차이 줄의 마지막 수정: `185e91c` 2026-01-30 (현재 128행 포함); `8c2b62b` 2025-08-24 (현재 131행 포함); `18fa7ab` 2025-04-11 (현재 132행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 124행 포함).

```diff
@@ -125,11 +120,9 @@
     let vol_data = globals.disturbance_vol_data;
     let gamma_val = globals.disturbance_gamma_val;
 
-    let displacement = max_displacement*(1.0+tanh((time_local-time_shift)/(change_timescale)))/2.0;
-    let traj_angle = min(final_traj,initial_traj + displacement/max_displacement*(final_traj-initial_traj)*traj_timefactor) * 3.1415 / 180.; 
+    let displacement = max_displacement*(1.0+tanh((time-time_shift)/(change_timescale)))/2.0;
+    let traj_angle = min(final_traj,initial_traj + displacement/max_displacement*traj_timefactor) * 3.1415 / 180.; 
     
-    let angle = 3.1415-traj_angle;
-
     let d_xdist=displacement*cos(traj_angle);
     let d_ydist=-displacement*sin(traj_angle);
```

#### CT1-148 최초 교란 정지 조건

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/AddDisturbance.wgsl:151; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/AddDisturbance.wgsl:144; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 time_local<5*dt를 쓴다. transect 판은 time<5*dt를 쓴다. 상한 전 시간에는 두 조건이 같다. |

본판 차이 줄의 마지막 수정: `185e91c` 2026-01-30 (현재 154행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 147행 포함).

```diff
@@ -151,7 +144,7 @@
     let bottom_new = bottom_initial + d_bottom;
     var dhdt = (bottom_new - bottom) / dt;
 
-    if (time_local < 5.*dt) {
+    if (time < 5.*dt) {
         dhdt = 0.0;
     }
```

#### CT1-149 교란 초기 지형과 누적 침식

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/AddDisturbance.wgsl:164; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/AddDisturbance.wgsl:157; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 초기 바닥고에 txBotChange_Sed를 더한다. transect 판은 초기 바닥고만 사용한다. 한쪽 결함 수정 이력이 있다. |

본판 차이 줄의 마지막 수정: `4353b85` 2025-06-09 (현재 167행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 160행 포함).

```diff
@@ -164,7 +157,7 @@
     let idx = vec2<i32>(i32(id.x), i32(id.y));
 
     let bottom_tex = textureLoad(txBottom, idx, 0);
-    let bottom_initial_tex = textureLoad(txBottomInitial, idx, 0) + textureLoad(txBotChange_Sed, idx, 0);
+    let bottom_initial_tex = textureLoad(txBottomInitial, idx, 0);
     var bottom = bottom_tex.z;
     let depth = globals.base_depth;
     var in_state_here = textureLoad(txState, idx, 0);
```

#### CT1-150 육상 사면 변형 억제

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/AddDisturbance.wgsl:226; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/AddDisturbance.wgsl:219; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 초기 바닥고가 양수이면 기존 바닥고를 되돌리고 dhdt를 0으로 둔다. 본판은 이 조건을 주석 처리했다. 본판 주석은 이 조건의 물 생성 방지 목적을 설명하지만 현재는 실행하지 않는다. |

본판 차이 줄의 마지막 수정: `8c2b62b` 2025-08-24 (현재 232행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 225행 포함).

```diff
@@ -226,10 +219,10 @@
         depth_change = depth_motion(xloc, yloc, bottom, globals.time, globals.dt, bottom_initial);
         B_here.z = depth_change.z;
 
-     //   if(bottom_initial_tex.z > 0.0 ) {  // without this, the slide creates water on dry land (for subaerial slides).
-     //       B_here = bottom_tex;
-     //       depth_change.y = 0.0;
-     //   } 
+        if(bottom_initial_tex.z > 0.0 ) {
+            B_here = bottom_tex;
+            depth_change.y = 0.0;
+        } 
     }
 
     let state_out = in_state_here + disturbance;
```


### 2.21 shaders/BoundaryPass.wgsl

본판: `shaders/BoundaryPass.wgsl`. transect 판: `transect_version/shaders/BoundaryPass.wgsl`.
원래 diff는 1286행이다. CR 제외 diff는 11구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `bb99fee` | 2026-07-02 | Added grid nesting |
| 본판 | `89c9824` | 2026-03-04 | slight beta change update |
| 본판 | `896c491` | 2026-01-17 | added flags to test beta-level features in code |
| 본판 | `9a7c709` | 2025-11-27 | Update BoundaryPass.wgsl |
| 본판 | `744c43a` | 2025-09-25 | river updates |
| 본판 | `8c2b62b` | 2025-08-24 | Added Tracy Arm Example, some landslide viz additions |
| 본판 | `faa12fa` | 2025-06-20 | periodic bc update |
| 본판 | `c7fb523` | 2025-06-09 | bugs |
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| transect | `ac0e0a9` | 2025-06-14 | transect updates |
| transect | `3d8a61b` | 2025-06-14 | Added many-transect version |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-151 경계 uniform 확장

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:41; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:41; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 알고리즘 시험·trough_factor·구면 원점·4변 관측점 수·시간 보간 인덱스와 가중치를 받는다. |

본판 차이 줄의 마지막 수정: `896c491` 2026-01-17 (현재 44행 포함); `bb99fee` 2026-07-02 (현재 57행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -41,20 +41,6 @@
     stage_200: f32,
     stage_500: f32,
     river_inflow_angle: f32,
-    algochanges: i32,
-    trough_factor: f32,
-    // Added by Codex: Start boundary time-series forcing uniforms.
-    grid_type: i32,
-    lon_LL: f32,
-    lat_LL: f32,
-    ts_num_points_west: i32,
-    ts_num_points_east: i32,
-    ts_num_points_south: i32,
-    ts_num_points_north: i32,
-    ts_time_idx0: i32,
-    ts_time_idx1: i32,
-    ts_time_alpha: f32
-    // Added by Codex: End boundary time-series forcing uniforms.
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-152 binding 9의 다른 물리 의미

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:69; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:55; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 binding 9를 단면별 파랑에 사용한다. 본판은 지형변동 강제장을 읽고 10–13에서 경계 시계열을 읽는다. |

본판 차이 줄의 마지막 수정: `8c2b62b` 2025-08-24 (현재 72행 포함); `bb99fee` 2026-07-02 (현재 78행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 60행 포함).

```diff
@@ -69,13 +55,9 @@
 @group(0) @binding(7) var txBreaking: texture_2d<f32>;
 @group(0) @binding(8) var txtemp_Breaking: texture_storage_2d<rgba32float, write>;
 
-@group(0) @binding(9) var txBoundaryForcing: texture_2d<f32>;
-// Added by Codex: Start boundary time-series forcing textures.
-@group(0) @binding(10) var txBoundaryTimeSeriesSouth: texture_2d<f32>;
-@group(0) @binding(11) var txBoundaryTimeSeriesNorth: texture_2d<f32>;
-@group(0) @binding(12) var txBoundaryTimeSeriesWest: texture_2d<f32>;
-@group(0) @binding(13) var txBoundaryTimeSeriesEast: texture_2d<f32>;
-// Added by Codex: End boundary time-series forcing textures.
+@group(0) @binding(9) var txWaves_Transect: texture_2d<f32>;
+
+
 
 fn WestBoundarySolid(idx: vec2<i32>) -> vec4<f32> {
     let real_idx = vec2<i32>(globals.boundary_shift  - idx.x, idx.y);
```

#### CT1-153 남북 고체벽 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:89; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:71; 아래 전체 diff의 +행 | 불일치 (F) | 독립 단면은 y 방향 반사벽을 적용하지 않는다. 동서 고체벽 함수는 유지한다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 102행 포함); `0dd009e` 2024-03-21 (현재 93행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 84행 포함).

```diff
@@ -89,17 +71,17 @@
     return vec4<f32>(in_state_real.r, -in_state_real.g, in_state_real.b, in_state_real.a);
 }
 
-fn SouthBoundarySolid(idx: vec2<i32>) -> vec4<f32> {
-    let real_idx = vec2<i32>(idx.x, globals.boundary_shift  - idx.y);
-    let in_state_real = textureLoad(txState, real_idx, 0);
-    return vec4<f32>(in_state_real.r, in_state_real.g, -in_state_real.b, in_state_real.a);
-}
-
-fn NorthBoundarySolid(idx: vec2<i32>) -> vec4<f32> {
-    let real_idx = vec2<i32>(idx.x, globals.reflect_y - idx.y);
-    let in_state_real = textureLoad(txState, real_idx, 0);
-    return vec4<f32>(in_state_real.r, in_state_real.g, -in_state_real.b, in_state_real.a);
-}
+//fn SouthBoundarySolid(idx: vec2<i32>) -> vec4<f32> {
+//    let real_idx = vec2<i32>(idx.x, globals.boundary_shift  - idx.y);
+//    let in_state_real = textureLoad(txState, real_idx, 0);
+//    return vec4<f32>(in_state_real.r, in_state_real.g, -in_state_real.b, in_state_real.a);
+//}
+
+//fn NorthBoundarySolid(idx: vec2<i32>) -> vec4<f32> {
+//    let real_idx = vec2<i32>(idx.x, globals.reflect_y - idx.y);
+//    let in_state_real = textureLoad(txState, real_idx, 0);
+//    return vec4<f32>(in_state_real.r, in_state_real.g, -in_state_real.b, in_state_real.a);
+//}
 
 fn WestBoundarySponge(idx: vec2<i32>) -> vec4<f32> {
     let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - idx.x) + 2.0) / f32(globals.BoundaryWidth - 1))), 0.005);
```

#### CT1-154 남북 sponge 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:113; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:95; 아래 전체 diff의 +행 | 불일치 (F) | 독립 단면은 y 방향 흡수층 함수를 호출하지 않는다. 동서 sponge 식은 유지한다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 126행 포함); `cf9de63` 2023-10-24 (현재 123행 포함); `8892a96` 2025-03-28 (현재 125행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 108행 포함).

```diff
@@ -113,17 +95,17 @@
     return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
 }
 
-fn SouthBoundarySponge(idx: vec2<i32>) -> vec4<f32> {
-    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - idx.y) + 2.0) / f32(globals.BoundaryWidth - 1))), 0.005);
-    let new_state = textureLoad(txState, idx, 0);
-    return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
-}
-
-fn NorthBoundarySponge(idx: vec2<i32>) -> vec4<f32> {
-    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - globals.boundary_ny - idx.y)) / f32(globals.BoundaryWidth - 1))), 0.005);
-    let new_state = textureLoad(txState, idx, 0);
-    return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
-}
+//fn SouthBoundarySponge(idx: vec2<i32>) -> vec4<f32> {
+//    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - idx.y) + 2.0) / f32(globals.BoundaryWidth - 1))), 0.005);
+//    let new_state = textureLoad(txState, idx, 0);
+//    return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
+//}
+
+//fn NorthBoundarySponge(idx: vec2<i32>) -> vec4<f32> {
+//    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - globals.boundary_ny - idx.y)) / f32(globals.BoundaryWidth - 1))), 0.005);
+//    let new_state = textureLoad(txState, idx, 0);
+//    return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
+//}
 
 fn calc_wavenumber_approx(omega: f32, d: f32) -> f32 {
     let k = omega * omega / (globals.boundary_g * sqrt(tanh(omega * omega * d / globals.boundary_g)));
```

#### CT1-155 고립파의 1D 환원

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:135; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:117; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 y와 yloc를 0.0으로 둔다. hv=0.0이다. x 진행파를 쓰는 단면에서 고립파의 x 식과 같다. |

본판 차이 줄의 마지막 수정: `040cfdf` 2024-06-07 (현재 149행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 134행 포함).

```diff
@@ -135,18 +117,21 @@
     let B_here = -globals.base_depth; //textureLoad(txBottom, idx, 0).b;
     let d = max(0.0, -B_here);
     let x = f32(idx.x) * globals.dx;
-    let y = f32(idx.y) * globals.dy;
+    //let y = f32(idx.y) * globals.dy;
+    let y = 0.0;
     let t = globals.total_time;
     let amplitude = 0.5;
 
     let xloc = x - x0;
-    let yloc = y - y0;
+    //let yloc = y - y0;
+    let yloc = 0.0;
     let k = sqrt(0.75 * abs(amplitude)/pow(d,3.0));
     let c = sqrt(globals.boundary_g * (amplitude + d));
 
     let eta = amplitude / pow(cosh(k * (xloc * cos(theta) + yloc * sin(theta) - c * t)),2.0);
     let hu = sqrt(1.0 + 0.5 * amplitude / d) * eta * c * cos(theta);
-    let hv = sqrt(1.0 + 0.5 * amplitude / d) * eta * c * sin(theta);
+   // let hv = sqrt(1.0 + 0.5 * amplitude / d) * eta * c * sin(theta);
+    let hv = 0.0;
 
     return vec4<f32>(eta, hu, hv, 0.0);
 }
```

#### CT1-156 단면 파랑·pulse·주기·sponge·type5 차이

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:161; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:146; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 ky와 기점 이동을 0으로 둔다. pulse의 성분 지속 길이는 4주기이고 본판은 5주기다. 본판만 음의 eta에 trough_factor를 곱한다. transect 판은 국소 바닥고로 파수를 계산한다. 본판은 base_depth를 쓴다. transect 판은 같은 y행의 파랑 성분을 읽는다. 본판의 시계열 공간·시간 선형 보간은 transect 판에 없다. transect 판은 dhdt 바닥 보정을 하지 않는다. 주기 경계는 비활성이다. 본판의 중첩 sponge 가중 평균 대신 동서 sponge를 순서대로 대입한다. |

본판 차이 줄의 마지막 수정: `4766ac1` 2025-01-25 (현재 193행 포함); `b70eb47` 2025-01-26 (현재 168행 포함); `bb99fee` 2026-07-02 (현재 279행 포함); `28c22e7` 2024-09-02 (현재 179행 포함); `0e8b502` 2023-10-31 (현재 185행 포함); `9f84752` 2024-04-26 (현재 190행 포함); `63a12e3` 2023-10-19 (현재 394행 포함); `8c2b62b` 2025-08-24 (현재 290행 포함); `faa12fa` 2025-06-20 (현재 354행 포함); `9a7c709` 2025-11-27 (현재 399행 포함); `0dd009e` 2024-03-21 (현재 392행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 225행 포함); `ac0e0a9` 2025-06-14 (현재 175행 포함); `3d8a61b` 2025-06-14 (현재 185행 포함).

```diff
@@ -161,242 +146,83 @@
     // modulate the location of the origin slowly in time to reduce the Hs finger effect
     var yshift= 0.0;
     var xshift= 0.0;
-    if (current_boundary == 1 || current_boundary == 3) {
-        yshift= 5.0 * L + 0.05 * L * t / period;
-    }
-    if (current_boundary == 2 || current_boundary == 4) {
-        xshift= 5.0 * L + 0.05 * L * t / period;
-    }
+    //if (current_boundary == 1 || current_boundary == 3) {
+    //    yshift= 5.0 * L + 0.05 * L * t / period;
+    //}
+    //if (current_boundary == 2 || current_boundary == 4) {
+    //    xshift= 5.0 * L + 0.05 * L * t / period;
+    //}
     
     let kx = cos(theta_mod) * (x + xshift) * k;
-    let ky = sin(theta_mod) * (y + yshift) * k;
+   // let ky = sin(theta_mod) * (y + yshift) * k;
+    let ky = 0.0;
     var eta = amplitude * sin(omega * t - kx - ky + phase) * min(1.0, t / period);
     var num_waves = 0;
     if (globals.incident_wave_type == 2){ // transient pulse
-        num_waves = 5;
-        if (eta < 0.0) {
-            eta = eta * globals.trough_factor;
-        }
+        num_waves = 4;
+    }
+    if(num_waves > 0){
         eta = eta * max(0.0, min(1.0, ((f32(num_waves) * period - t)/(period))));
     }
-
     let speed = globals.boundary_g * eta / (c * k) * tanh(k * d);
     let hu = speed * cos(theta_mod);
-    let hv = speed * sin(theta_mod);
+   // let hv = speed * sin(theta_mod);
+    let hv = 0.0;
     return vec3<f32>(eta, hu, hv);
 }
 
 fn BoundarySineWave(idx: vec2<i32>, iBC: i32, jBC: i32, current_boundary: i32) -> vec4<f32> {
-    let B_here = -globals.base_depth; //textureLoad(txBottom, idx, 0).b;
+    let B_here = textureLoad(txBottom, idx, 0).b;
     let d_here = max(0.0, -B_here);
     let x = f32(idx.x - iBC) * globals.dx;
-    let y = f32(idx.y - jBC) * globals.dy;
+   // let y = f32(idx.y - jBC) * globals.dy;
+    let y = 0.0;
     var result: vec3<f32> = vec3<f32>(0.0, 0.0, 0.0);
     
     if (d_here > 0.0001) {
         for (var iw: i32 = 0; iw < globals.numberOfWaves; iw = iw + 1) {
-            let wave = textureLoad(txWaves, vec2<i32>(iw, 0), 0);
+            //let wave = textureLoad(txWaves, vec2<i32>(iw, 0), 0);
+            let wave = textureLoad(txWaves_Transect, vec2<i32>(iw, idx.y), 0);
             result = result + sineWave(x, y, globals.total_time, d_here, wave.r, wave.g, wave.b, wave.a, current_boundary);
         }
     }
     return vec4<f32>(result, 0.0);
 }
 
-// Added by Codex: Start boundary time-series forcing support.
-fn LoadBoundaryTimeSeriesValue(side: i32, station_index: i32, row_index: i32) -> vec4<f32> {
-    if (side == 0) {
-        return textureLoad(txBoundaryTimeSeriesSouth, vec2<i32>(station_index, row_index), 0);
-    }
-    if (side == 1) {
-        return textureLoad(txBoundaryTimeSeriesNorth, vec2<i32>(station_index, row_index), 0);
-    }
-    if (side == 2) {
-        return textureLoad(txBoundaryTimeSeriesWest, vec2<i32>(station_index, row_index), 0);
-    }
-    return textureLoad(txBoundaryTimeSeriesEast, vec2<i32>(station_index, row_index), 0);
-}
-
-fn BoundaryTimeSeriesXCoordinate(idx: vec2<i32>) -> f32 {
-    var coordinate = f32(idx.x) * globals.dx;
-    if (globals.grid_type == 2) {
-        coordinate = globals.lon_LL + coordinate;
-    }
-    return coordinate;
-}
-
-fn BoundaryTimeSeriesYCoordinate(idx: vec2<i32>) -> f32 {
-    var coordinate = f32(idx.y) * globals.dy;
-    if (globals.grid_type == 2) {
-        coordinate = globals.lat_LL + coordinate;
-    }
-    return coordinate;
-}
-
-fn BoundaryTimeSeriesState(side: i32, coordinate: f32, num_points: i32) -> vec4<f32> {
-    if (num_points <= 0) {
-        return vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    }
-
-    var left_station = 0;
-    var right_station = 0;
-    var space_alpha = 0.0;
-    if (num_points > 1) {
-        let first_location = LoadBoundaryTimeSeriesValue(side, 0, 0).r;
-        let last_location = LoadBoundaryTimeSeriesValue(side, num_points - 1, 0).r;
-        if (coordinate <= first_location) {
-            left_station = 0;
-            right_station = 0;
-            space_alpha = 0.0;
-        } else if (coordinate >= last_location) {
-            left_station = num_points - 1;
-            right_station = num_points - 1;
-            space_alpha = 0.0;
-        } else {
-            for (var station_index = 0; station_index < num_points - 1; station_index = station_index + 1) {
-                let location_left = LoadBoundaryTimeSeriesValue(side, station_index, 0).r;
-                let location_right = LoadBoundaryTimeSeriesValue(side, station_index + 1, 0).r;
-                if (coordinate >= location_left && coordinate <= location_right) {
-                    left_station = station_index;
-                    right_station = station_index + 1;
-                    space_alpha = (coordinate - location_left) / max(location_right - location_left, 1.0e-12);
-                    break;
-                }
-            }
-        }
-    }
-
-    let time_row0 = 1 + globals.ts_time_idx0;
-    let time_row1 = 1 + globals.ts_time_idx1;
-    let value_left0 = LoadBoundaryTimeSeriesValue(side, left_station, time_row0).rgb;
-    let value_right0 = LoadBoundaryTimeSeriesValue(side, right_station, time_row0).rgb;
-    let value_left1 = LoadBoundaryTimeSeriesValue(side, left_station, time_row1).rgb;
-    let value_right1 = LoadBoundaryTimeSeriesValue(side, right_station, time_row1).rgb;
-    let space_value0 = mix(value_left0, value_right0, space_alpha);
-    let space_value1 = mix(value_left1, value_right1, space_alpha);
-    return vec4<f32>(mix(space_value0, space_value1, globals.ts_time_alpha), 0.0);
-}
-// Added by Codex: End boundary time-series forcing support.
-
 @compute @workgroup_size(16, 16)
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
     var BCState = textureLoad(txState, idx, 0);
     var BCState_Sed = textureLoad(txState_Sed, idx, 0);
     var BCState_Breaking = textureLoad(txBreaking, idx, 0);
-    
-    // dhdt for depth change option
-    let dhdt = textureLoad(txBoundaryForcing, idx, 0).y;
-
-    let B_here = textureLoad(txBottom, idx, 0).z - abs(dhdt) * globals.dt;
+    let B_here = textureLoad(txBottom, idx, 0).z;
     let zero = vec4<f32>(0.0, 0.0, 0.0, 0.0);
     BCState_Sed = max(BCState_Sed,zero);  // concentration can not go negative
     
-
-
-    // Periodic boundary conditions
-    let periodic_overlap = 2; // number of cells that overlap between periodic boundaries
+    // Sponge Layers
     // west boundary
-    if (globals.west_boundary_type == 3) {
-        if (idx.x <= periodic_overlap - 1) {
-            let idx_east = vec2<i32>(globals.width - 2 * periodic_overlap + idx.x - 1, idx.y);
-            BCState = textureLoad(txState, idx_east, 0);
-            BCState_Sed = textureLoad(txState_Sed, idx_east, 0);
-            BCState_Breaking = textureLoad(txBreaking, idx_east, 0);
-        }
-        else if (idx.x == periodic_overlap) {
-            let idx_east = vec2<i32>(globals.width - 2 * periodic_overlap + idx.x - 1, idx.y);
-            BCState.y = 0.5 * (BCState.y + textureLoad(txState, idx_east, 0).y);
-        }
+    if (globals.west_boundary_type == 1 && idx.x <= 2 + (globals.BoundaryWidth)) {
+        BCState = WestBoundarySponge(idx);
+        BCState_Sed = zero;
     }
 
     // east boundary
-    if (globals.east_boundary_type == 3) {
-        if (idx.x >= globals.width  - periodic_overlap) {
-            let idx_west = vec2<i32>(2 * periodic_overlap - ( (globals.width - 1) - idx.x ) , idx.y);
-            BCState = textureLoad(txState, idx_west, 0);
-            BCState_Sed = textureLoad(txState_Sed, idx_west, 0);
-            BCState_Breaking = textureLoad(txBreaking, idx_west, 0);
-        }
-        else if (idx.x == globals.width - periodic_overlap - 1) {
-            let idx_west = vec2<i32>(2 * periodic_overlap - ( (globals.width - 1) - idx.x ) , idx.y);
-            BCState.y = 0.5 * (BCState.y + textureLoad(txState, idx_west, 0).y);
-        }
+    if (globals.east_boundary_type == 1 && idx.x >= globals.width - (globals.BoundaryWidth) - 1) {
+        BCState = EastBoundarySponge(idx, B_here);
+        BCState_Sed = zero;
     }
 
     // south boundary
-    if (globals.south_boundary_type == 3) {
-        if (idx.y <= periodic_overlap - 1) {
-            let idx_north = vec2<i32>(idx.x, globals.height - 2 * periodic_overlap + idx.y - 1);
-            BCState = textureLoad(txState, idx_north, 0);
-            BCState_Sed = textureLoad(txState_Sed, idx_north, 0);
-            BCState_Breaking = textureLoad(txBreaking, idx_north, 0);
-        }
-        else if (idx.y == periodic_overlap) {
-            let idx_north = vec2<i32>(idx.x, globals.height - 2 * periodic_overlap + idx.y - 1);
-            BCState.z = 0.5 * (BCState.z + textureLoad(txState, idx_north, 0).z);
-        }
-    }
+   // if (globals.south_boundary_type == 1 && idx.y <= 2 + (globals.BoundaryWidth)) {
+   //     BCState = SouthBoundarySponge(idx);
+   //     BCState_Sed = zero;
+   // }
 
     // north boundary
-    if (globals.north_boundary_type == 3) {
-        if (idx.y >= globals.height - periodic_overlap) {
-            let idx_south = vec2<i32>(idx.x, 2 * periodic_overlap - ( (globals.height - 1) - idx.y ) );
-            BCState = textureLoad(txState, idx_south, 0);
-            BCState_Sed = textureLoad(txState_Sed, idx_south, 0);
-            BCState_Breaking = textureLoad(txBreaking, idx_south, 0);
-        }
-        else if (idx.y == globals.height - periodic_overlap - 1) {
-            let idx_south = vec2<i32>(idx.x, 2 * periodic_overlap - ( (globals.height - 1) - idx.y ) );
-            BCState.z = 0.5 * (BCState.z + textureLoad(txState, idx_south, 0).z);
-        }
-    }
-
-
-    // Sponge Layers
-    var state_sum   = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    var weight_sum  = 0.0;
-
-    // west sponge
-    if (globals.west_boundary_type == 1 && idx.x <= 2 + globals.BoundaryWidth) {
-        let s = f32(globals.BoundaryWidth + 2 - idx.x) / f32(globals.BoundaryWidth);
-        let state_w = WestBoundarySponge(idx);
-        state_sum  = state_sum + s * state_w;
-        weight_sum = weight_sum + s;
-        BCState_Sed = zero;
-    }
-
-    // east sponge
-    if (globals.east_boundary_type == 1 && idx.x >= globals.width - globals.BoundaryWidth - 1) {
-        let s = f32(idx.x - (globals.width - globals.BoundaryWidth - 1)) / f32(globals.BoundaryWidth);
-        let state_e = EastBoundarySponge(idx, B_here);
-        state_sum  = state_sum + s * state_e;
-        weight_sum = weight_sum + s;
-        BCState_Sed = zero;
-    }
-
-    // south sponge
-    if (globals.south_boundary_type == 1 && idx.y <= 2 + globals.BoundaryWidth) {
-        let s = f32(globals.BoundaryWidth + 2 - idx.y) / f32(globals.BoundaryWidth);
-        let state_s = SouthBoundarySponge(idx);
-        state_sum  = state_sum + s * state_s;
-        weight_sum = weight_sum + s;
-        BCState_Sed = zero;
-    }
-
-    // north sponge
-    if (globals.north_boundary_type == 1 && idx.y >= globals.height - globals.BoundaryWidth - 1) {
-        let s = f32(idx.y - (globals.height - globals.BoundaryWidth - 1)) / f32(globals.BoundaryWidth);
-        let state_n = NorthBoundarySponge(idx);
-        state_sum  = state_sum + s * state_n;
-        weight_sum = weight_sum + s;
-        BCState_Sed = zero;
-    }
-
-    // apply sponge if any side is active
-    if (weight_sum > 0.0) {
-        BCState = state_sum / weight_sum;
-    }
-
+   // if (globals.north_boundary_type == 1 && idx.y >= globals.height - (globals.BoundaryWidth) - 1) {
+   //     BCState = NorthBoundarySponge(idx);
+   //     BCState_Sed = zero;
+   // }
 
     // Solid Walls
     // west boundary
```

#### CT1-157 남북 고체벽 적용 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:422; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:248; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 남북 경계 상태와 퇴적물 값을 덮어쓰지 않는다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 444행 포함); `0dd009e` 2024-03-21 (현재 442행 포함); `471c581` 2024-01-04 (현재 440행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 270행 포함).

```diff
@@ -422,26 +248,26 @@
     }
 
     // south boundary
-    if (globals.south_boundary_type <= 1) {
-        if (idx.y <= 1) {
-            BCState = SouthBoundarySolid(idx);
-            BCState_Sed = zero;
-        } else if (idx.y == 2) {
-            BCState.z = 0.0;
-            BCState_Sed = zero;
-        }
-    }
+   // if (globals.south_boundary_type <= 1) {
+   //     if (idx.y <= 1) {
+   //         BCState = SouthBoundarySolid(idx);
+   //         BCState_Sed = zero;
+   //     } else if (idx.y == 2) {
+   //         BCState.z = 0.0;
+   //         BCState_Sed = zero;
+   //     }
+   // }
 
     // north boundary
-    if (globals.north_boundary_type <= 1) {
-        if (idx.y >= globals.height - 2) {
-            BCState = NorthBoundarySolid(idx);
-            BCState_Sed = zero;
-        } else if (idx.y == globals.height - 3) {
-            BCState.z = 0.0;
-            BCState_Sed = zero;
-        }
-    }
+   // if (globals.north_boundary_type <= 1) {
+   //     if (idx.y >= globals.height - 2) {
+   //         BCState = NorthBoundarySolid(idx);
+   //         BCState_Sed = zero;
+   //     } else if (idx.y == globals.height - 3) {
+   //         BCState.z = 0.0;
+   //         BCState_Sed = zero;
+   //     }
+   // }
 
     // Incoming Waves
     // west boundary
```

#### CT1-158 남북 입사파·주기·type5 미지원

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:479; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:305; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 남북 입사파와 모든 주기 경계를 주석 처리한다. 본판의 type5 시계열 경계 대입은 없다. transect UI의 별표와 연결된다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 513행 포함); `040cfdf` 2024-06-07 (현재 512행 포함); `b70eb47` 2025-01-26 (현재 501행 포함); `4766ac1` 2025-01-25 (현재 504행 포함); `0dd009e` 2024-03-21 (현재 505행 포함); `471c581` 2024-01-04 (현재 499행 포함); `bb99fee` 2026-07-02 (현재 547행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 380행 포함).

```diff
@@ -479,72 +305,79 @@
     } 
 
     // south boundary
-    if (globals.south_boundary_type == 2 && idx.y <= 2) {
-        if (globals.incident_wave_type <= 2) { // Sine Waves
-            let iBC = 1;
-            let jBC = 1;
-            let current_boundary = 2;
-            BCState = BoundarySineWave(idx, iBC, jBC, current_boundary);
-            BCState_Sed = zero;
-        } else if (globals.incident_wave_type == 3) {  // solitary wave
-            let x0 = 0.0;
-            let y0 = -10.0 * globals.base_depth;
-            let theta = 3.1415 / 2.0;
-            BCState = SolitaryWave(idx, x0, y0, theta);
-            BCState_Sed = zero;
-        }
-    }
+   // if (globals.south_boundary_type == 2 && idx.y <= 2) {
+   //     if (globals.incident_wave_type <= 2) { // Sine Waves
+   //         let iBC = 1;
+   //         let jBC = 1;
+   //         let current_boundary = 2;
+   //         BCState = BoundarySineWave(idx, iBC, jBC, current_boundary);
+   //         BCState_Sed = zero;
+   //     } else if (globals.incident_wave_type == 3) {  // solitary wave
+   //         let x0 = 0.0;
+   //         let y0 = -10.0 * globals.base_depth;
+   //         let theta = 3.1415 / 2.0;
+   //         BCState = SolitaryWave(idx, x0, y0, theta);
+   //         BCState_Sed = zero;
+   //     }
+   // }
 
     // north boundary
-    if (globals.north_boundary_type == 2 && idx.y >= globals.height - 3) {
-        if (globals.incident_wave_type <= 2) { // Sine Waves
-            let iBC = 1;
-            let jBC = globals.height - 2;
-            let current_boundary = 4;
-            BCState = BoundarySineWave(idx, iBC, jBC, current_boundary);
-            BCState_Sed = zero;
-        } else if (globals.incident_wave_type == 3) {  // solitary wave
-            let x0 = 0.0;
-            let y0 = f32(globals.height) * globals.dy + 10.0 * globals.base_depth;
-            let theta = -3.1415 / 2.0;
-            BCState = SolitaryWave(idx, x0, y0, theta);
-            BCState_Sed = zero;
-        }
-    }
+   // if (globals.north_boundary_type == 2 && idx.y >= globals.height - 3) {
+   //     if (globals.incident_wave_type <= 2) { // Sine Waves
+   //         let iBC = 1;
+   //         let jBC = globals.height - 2;
+   //         let current_boundary = 4;
+   //         BCState = BoundarySineWave(idx, iBC, jBC, current_boundary);
+   //         BCState_Sed = zero;
+   //     } else if (globals.incident_wave_type == 3) {  // solitary wave
+   //         let x0 = 0.0;
+   //         let y0 = f32(globals.height) * globals.dy + 10.0 * globals.base_depth;
+   //         let theta = -3.1415 / 2.0;
+   //         BCState = SolitaryWave(idx, x0, y0, theta);
+   //         BCState_Sed = zero;
+   //     }
+   // }
 
-    // Added by Codex: Start boundary time-series forcing conditions.
+    // Periodic boundary conditions
     // west boundary
-    if (globals.west_boundary_type == 5 && idx.x <= 2) {
-        let coordinate = BoundaryTimeSeriesYCoordinate(idx);
-        BCState = BoundaryTimeSeriesState(2, coordinate, globals.ts_num_points_west);
-        BCState_Sed = zero;
-        BCState_Breaking = zero;
-    }
+   // if (globals.west_boundary_type == 3) {
+   //     if (idx.x <= 1) {
+   //         let idx_east = vec2<i32>(globals.width - (6 - idx.x), idx.y);
+   //         BCState = textureLoad(txState, idx_east, 0);
+   //         BCState_Sed = textureLoad(txState_Sed, idx_east, 0);
+   //         BCState_Breaking = textureLoad(txBreaking, idx_east, 0);
+   //     }
+   // }
 
     // east boundary
-    if (globals.east_boundary_type == 5 && idx.x >= globals.width - 3) {
-        let coordinate = BoundaryTimeSeriesYCoordinate(idx);
-        BCState = BoundaryTimeSeriesState(3, coordinate, globals.ts_num_points_east);
-        BCState_Sed = zero;
-        BCState_Breaking = zero;
-    }
+   // if (globals.east_boundary_type == 3) {
+   //     if (idx.x >= globals.width - 2) {
+   //         let idx_west = vec2<i32>(idx.x + 6 - globals.width, idx.y);
+   //         BCState = textureLoad(txState, idx_west, 0);
+   //         BCState_Sed = textureLoad(txState_Sed, idx_west, 0);
+   //         BCState_Breaking = textureLoad(txBreaking, idx_west, 0);
+   //     }
+   // }
 
     // south boundary
-    if (globals.south_boundary_type == 5 && idx.y <= 2) {
-        let coordinate = BoundaryTimeSeriesXCoordinate(idx);
-        BCState = BoundaryTimeSeriesState(0, coordinate, globals.ts_num_points_south);
-        BCState_Sed = zero;
-        BCState_Breaking = zero;
-    }
+   // if (globals.south_boundary_type == 3) {
+   //     if (idx.y <= 1) {
+   //         let idx_north = vec2<i32>(idx.x, globals.height - (6 - idx.y));
+   //         BCState = textureLoad(txState, idx_north, 0);
+   //         BCState_Sed = textureLoad(txState_Sed, idx_north, 0);
+   //         BCState_Breaking = textureLoad(txBreaking, idx_north, 0);
+   //     }
+   // }
 
     // north boundary
-    if (globals.north_boundary_type == 5 && idx.y >= globals.height - 3) {
-        let coordinate = BoundaryTimeSeriesXCoordinate(idx);
-        BCState = BoundaryTimeSeriesState(1, coordinate, globals.ts_num_points_north);
-        BCState_Sed = zero;
-        BCState_Breaking = zero;
-    }
-    // Added by Codex: End boundary time-series forcing conditions.
+   // if (globals.north_boundary_type == 3) {
+   //     if (idx.y >= globals.height - 2) {
+   //         let idx_south = vec2<i32>(idx.x, idx.y + 6 - globals.height);
+   //         BCState = textureLoad(txState, idx_south, 0);
+   //         BCState_Sed = textureLoad(txState_Sed, idx_south, 0);
+   //         BCState_Breaking = textureLoad(txBreaking, idx_south, 0);
+   //     }
+   // }
 
     // Constant elevation boundary conditions
     // west boundary
```

#### CT1-159 서쪽 하천 경계 주석

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:575; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:408; 아래 전체 diff의 +행 | 불일치 (F) | 실행 조건은 같다. 상류 가정이라는 설명 주석만 없다. |

본판 차이 줄의 마지막 수정: `744c43a` 2025-09-25 (현재 578행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 411행 포함).

```diff
@@ -575,7 +408,7 @@
     let stage_elevation = globals.mean_upstream_channel_elevation + stage_c;
     let stage_speed = Q_c / stage_c / (globals.channel_bottom_width * cos(globals.river_inflow_angle) + stage_c / globals.channel_side_slope) ;
 
-    if (globals.west_boundary_type == 4) { // west boundary is assumed to be the upstream boundary
+    if (globals.west_boundary_type == 4) {
         var left_bottom_start = globals.channel_bank_start_upstream;
         let loc_c = f32(idx.y) * globals.dy;
         if (idx.x <= 1 && loc_c > left_bottom_start && loc_c < globals.channel_bank_end_upstream ) {  //LARIVER MOD
```

#### CT1-160 동쪽 하천 경계 주석

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:590; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:423; 아래 전체 diff의 +행 | 불일치 (F) | 실행 조건은 같다. 하류 가정이라는 설명 주석만 없다. |

본판 차이 줄의 마지막 수정: `744c43a` 2025-09-25 (현재 593행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 426행 포함).

```diff
@@ -590,7 +423,7 @@
         }
     }
     // east boundary
-    if (globals.east_boundary_type == 4) {  // east boundary is assumed to be the downstream boundary
+    if (globals.east_boundary_type == 4) {
         if (idx.x >= globals.width - 2 && f32(idx.y) * globals.dy > globals.channel_bank_start_upstream && f32(idx.y) * globals.dy < globals.channel_bank_end_upstream ) {  //LARIVER MOD
             let elev_downstream = stage_elevation - 5.0; 
             let flow_depth = max(elev_downstream - B_here, 0.0);
```

#### CT1-161 북쪽 하천과 고립 습윤점 처리 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/BoundaryPass.wgsl:602; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/BoundaryPass.wgsl:435; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 북쪽 하천 경계를 주석 처리한다. transect 판은 고립 습윤점과 단일 격자 수로 끝의 동결을 주석 처리한다. 음수 수심 검사는 유지한다. h_here 재평가는 앞에서 BCState를 더 바꾸지 않으므로 생략해도 현재 경로에서 같은 값이다. |

본판 차이 줄의 마지막 수정: `3d938d1` 2025-03-14 (현재 617행 포함); `8892a96` 2025-03-28 (현재 607행 포함); `01c8b73` 2025-04-06 (현재 610행 포함); `d4bea46` 2025-01-27 (현재 619행 포함); `ebc98a5` 2024-03-13 (현재 711행 포함); `38a5072` 2025-01-21 (현재 692행 포함); `0dd009e` 2024-03-21 (현재 706행 포함); `89c9824` 2026-03-04 (현재 703행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 544행 포함).

```diff
@@ -602,113 +435,113 @@
         }
     }
     //north
-    if (globals.north_boundary_type == 4) {
-        var left_bottom_start = globals.channel_bank_start_upstream;
-        if (idx.y >= globals.height - 2 && f32(idx.x) * globals.dx > left_bottom_start && f32(idx.x) * globals.dx < globals.channel_bank_end_upstream ) {  //LARIVER MOD
-            let flow_depth = max(stage_elevation - B_here, 0.0);
-            let hu = -flow_depth * stage_speed * sin(globals.river_inflow_angle);
-            let hv = -flow_depth * stage_speed * cos(globals.river_inflow_angle);
-            var conc = 0.0;
-            if (f32(idx.y) * globals.dy > 505 && f32(idx.y) * globals.dy < 570. && i32(globals.total_time / 30.0) % 2 == 0) {conc = 1.0;}
-            BCState = vec4<f32>(stage_elevation, hu, hv, conc);
-            BCState_Sed = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-            BCState_Breaking = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-        }
-    }    
-
-
-    let leftIdx = idx + vec2<i32>(-1, 0);
-    let rightIdx = idx + vec2<i32>(1, 0);
-    let downIdx = idx + vec2<i32>(0, -1);
-    let upIdx = idx + vec2<i32>(0, 1);
-
-    let B_south = textureLoad(txBottom, downIdx, 0).z;
-    let B_north = textureLoad(txBottom, upIdx, 0).z;
-    let B_west = textureLoad(txBottom, leftIdx, 0).z;
-    let B_east = textureLoad(txBottom, rightIdx, 0).z;
-
-    let state_west = textureLoad(txState, leftIdx, 0);
-    let state_east = textureLoad(txState, rightIdx, 0);
-    let state_south = textureLoad(txState, downIdx, 0);
-    let state_north = textureLoad(txState, upIdx, 0);
+   // if (globals.north_boundary_type == 4) {
+   //     var left_bottom_start = globals.channel_bank_start_upstream;
+   //     if (idx.y >= globals.height - 2 && f32(idx.x) * globals.dx > left_bottom_start && f32(idx.x) * globals.dx < globals.channel_bank_end_upstream ) {  //LARIVER MOD
+   //         let flow_depth = max(stage_elevation - B_here, 0.0);
+   //         let hu = -flow_depth * stage_speed * sin(globals.river_inflow_angle);
+   //         let hv = -flow_depth * stage_speed * cos(globals.river_inflow_angle);
+   //         var conc = 0.0;
+   //         if (f32(idx.y) * globals.dy > 505 && f32(idx.y) * globals.dy < 570. && i32(globals.total_time / 30.0) % 2 == 0) {conc = 1.0;}
+   //         BCState = vec4<f32>(stage_elevation, hu, hv, conc);
+   //         BCState_Sed = vec4<f32>(0.0, 0.0, 0.0, 0.0);
+   //         BCState_Breaking = vec4<f32>(0.0, 0.0, 0.0, 0.0);
+   //     }
+   // }    
+
+
+   // let leftIdx = idx + vec2<i32>(-1, 0);
+   // let rightIdx = idx + vec2<i32>(1, 0);
+   // let downIdx = idx + vec2<i32>(0, -1);
+   // let upIdx = idx + vec2<i32>(0, 1);
+
+   // let B_south = B_here; //textureLoad(txBottom, downIdx, 0).z;
+   // let B_north = B_here; //textureLoad(txBottom, upIdx, 0).z;
+   // let B_west = textureLoad(txBottom, leftIdx, 0).z;
+   // let B_east = textureLoad(txBottom, rightIdx, 0).z;
+
+   // let state_west = textureLoad(txState, leftIdx, 0);
+   // let state_east = textureLoad(txState, rightIdx, 0);
+   // let state_south = textureLoad(txState, downIdx, 0);
+   // let state_north = textureLoad(txState, upIdx, 0);
 
     var eta_here = BCState.x;
-    var eta_west = state_west.x;
-    var eta_east = state_east.x;
-    var eta_south = state_south.x;
-    var eta_north = state_north.x;
+   // var eta_west = state_west.x;
+   // var eta_east = state_east.x;
+   // var eta_south = state_south.x;
+   // var eta_north = state_north.x;
     
-    var u_west = state_west.y;
-    var u_east = state_east.y;
-    var u_south = state_south.y;
-    var u_north = state_north.y;
+   // var u_west = state_west.y;
+   // var u_east = state_east.y;
+   // var u_south = state_south.y;
+   // var u_north = state_north.y;
     
-    var v_west = state_west.z;
-    var v_east = state_east.z;
-    var v_south = state_south.z;
-    var v_north = state_north.z;
+   // var v_west = state_west.z;
+   // var v_east = state_east.z;
+   // var v_south = state_south.z;
+   // var v_north = state_north.z;
 
     var h_here = eta_here - B_here;
-    let h_west = eta_west - B_west;
-    let h_east = eta_east - B_east;
-    let h_south = eta_south - B_south;
-    let h_north = eta_north - B_north;
-
-    var h_cut = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    h_cut.x= max(globals.delta, abs(B_here - B_north));
-    h_cut.y= max(globals.delta, abs(B_here - B_east));
-    h_cut.z= max(globals.delta, abs(B_here - B_south));
-    h_cut.w= max(globals.delta, abs(B_here - B_west));
-
-    var dry_here = 1;
-    var dry_west = 1;
-    var dry_east = 1;
-    var dry_south = 1;
-    var dry_north = 1;
-
-    if (h_here <= globals.delta) { dry_here = 0;}
-    if (h_west <= h_cut.w) { dry_west = 0;}
-    if (h_east <= h_cut.y) { dry_east = 0;}
-    if (h_south <= h_cut.z) { dry_south = 0;}
-    if (h_north <= h_cut.x) { dry_north = 0;}
-
-    let sum_dry = dry_west + dry_east + dry_south + dry_north;
-
-    var h_min = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    h_min.x= min(h_here, h_north);
-    h_min.y= min(h_here, h_east);
-    h_min.z= min(h_here, h_south);
-    h_min.w= min(h_here, h_west);
-
-    let wetdry = min(h_here, min(h_south, min(h_north, min(h_west, h_east))));
-    let nearshore = min(B_here, min(B_south, min(B_north, min(B_west, B_east))));
-
-    var boundary_boolean = -1;
-    if (idx.x >= globals.width - 2 || idx.y >= globals.height - 3 || idx.x <= 1 || idx.y <= 3) {
-        boundary_boolean = 1;
-    }
+   // let h_west = eta_west - B_west;
+   // let h_east = eta_east - B_east;
+   // let h_south = eta_south - B_south;
+   // let h_north = eta_north - B_north;
+
+   // var h_cut = vec4<f32>(0.0, 0.0, 0.0, 0.0);
+   // h_cut.x= max(globals.delta, abs(B_here - B_north));
+   // h_cut.y= max(globals.delta, abs(B_here - B_east));
+   // h_cut.z= max(globals.delta, abs(B_here - B_south));
+   // h_cut.w= max(globals.delta, abs(B_here - B_west));
+
+   // var dry_here = 1;
+   // var dry_west = 1;
+   // var dry_east = 1;
+   // var dry_south = 1;
+   // var dry_north = 1;
+
+   // if (h_here <= globals.delta) { dry_here = 0;}
+   // if (h_west <= h_cut.w) { dry_west = 0;}
+   // if (h_east <= h_cut.y) { dry_east = 0;}
+   // if (h_south <= h_cut.z) { dry_south = 0;}
+   // if (h_north <= h_cut.x) { dry_north = 0;}
+
+   // let sum_dry = dry_west + dry_east + dry_south + dry_north;
+
+   // var h_min = vec4<f32>(0.0, 0.0, 0.0, 0.0);
+   // h_min.x= min(h_here, h_north);
+   // h_min.y= min(h_here, h_east);
+   // h_min.z= min(h_here, h_south);
+   // h_min.w= min(h_here, h_west);
+
+   // let wetdry = min(h_here, min(h_south, min(h_north, min(h_west, h_east))));
+   // let nearshore = min(B_here, min(B_south, min(B_north, min(B_west, B_east))));
+
+   // var boundary_boolean = -1;
+   // if (idx.x >= globals.width - 2 || idx.y >= globals.height - 3 || idx.x <= 1 || idx.y <= 3) {
+   //     boundary_boolean = 1;
+   // }
 
     // remove islands
-    if( dry_here == 1 && boundary_boolean < 0) {  // point is wet
-        if (sum_dry == 0) {  // freeze single point wet areas
-            if (B_here <= 0.0) {
-                BCState = vec4<f32>(max(BCState.x,B_here), 0.0, 0.0, 0.0);
-                BCState_Sed = zero;
-            }
-            else {
-                BCState = vec4<f32>(B_here, 0.0, 0.0, 0.0);
-                BCState_Sed = zero;
-            }
-        }
-        else if (sum_dry == 1 && (globals.algochanges == 0 || nearshore <= globals.delta)) {  // freeze end of single grid channel, with free surface gradient equal to zero
-            let wet_eta = (f32(dry_west)*eta_west + f32(dry_east)*eta_east + f32(dry_south)*eta_south + f32(dry_north)*eta_north) / f32(sum_dry);
-            BCState = vec4<f32>(wet_eta, 0.0, 0.0, 0.0);
-            BCState_Sed = zero;
-        }
-    }
+   // if( dry_here == 1 && boundary_boolean < 0) {  // point is wet
+   //     if (sum_dry == 0) {  // freeze single point wet areas
+   //         if (B_here <= 0.0) {
+   //             BCState = vec4<f32>(max(BCState.x,B_here), 0.0, 0.0, 0.0);
+   //             BCState_Sed = zero;
+   //         }
+   //         else {
+   //             BCState = vec4<f32>(B_here, 0.0, 0.0, 0.0);
+   //             BCState_Sed = zero;
+   //         }
+   //     }
+   //     else if (sum_dry == 1) {  // freeze end of single grid channel, with free surface gradient equal to zero
+   //         let wet_eta = (f32(dry_west)*eta_west + f32(dry_east)*eta_east + f32(dry_south)*eta_south + f32(dry_north)*eta_north) / f32(sum_dry);
+   //         BCState = vec4<f32>(wet_eta, 0.0, 0.0, 0.0);
+   //         BCState_Sed = zero;
+   //     }
+   // }
 
     // Check for negative depths
-    h_here = BCState.x  - B_here;
+   // h_here = BCState.x  - B_here;
     if (h_here <= globals.delta) {
             if (B_here <= 0.0) {
                 BCState = vec4<f32>(max(BCState.x,B_here), 0.0, 0.0, 0.0);
```


### 2.22 shaders/CalcMeans.wgsl

본판: `shaders/CalcMeans.wgsl`. transect 판: `transect_version/shaders/CalcMeans.wgsl`.
원래 diff는 212행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `dc6cc2d` | 2025-08-10 | update max free surface render |
| transect | `4dc20a1` | 2026-01-27 | transect updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-162 통계 실제 수면 리소스

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/CalcMeans.wgsl:22; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/CalcMeans.wgsl:22; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 txNewState를 받는다. |

본판 차이 줄의 마지막 수정: `dc6cc2d` 2025-08-10 (현재 25행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -22,7 +22,6 @@
 @group(0) @binding(10) var txtemp_Means_Momflux: texture_storage_2d<rgba32float, write>; 
 @group(0) @binding(11) var txModelVelocities: texture_storage_2d<rgba32float, write>; 
 @group(0) @binding(12) var txC: texture_2d<f32>;
-@group(0) @binding(13) var txNewState: texture_2d<f32>;
 
 
 @compute @workgroup_size(16, 16)
```

#### CT1-163 통계 수면 자료원과 1D 속도 평균

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/CalcMeans.wgsl:35; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/CalcMeans.wgsl:34; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 동·서 면 평균을 2.0으로 나눈다. 본판은 네 면 평균을 4.0으로 나눈다. 1D 환원에서 속도·수심·농도 평균은 같은 의미다. eta는 본판이 실제 txNewState 값이고 transect가 h+bottom이다. transect는 와도를 계산하지 않는다. 본판의 건조 셀 eta 대체값은 최대값 계산 전에만 적용된다. |

본판 차이 줄의 마지막 수정: `de0b465` 2025-04-24 (현재 54행 포함); `094fc2e` 2025-05-19 (현재 50행 포함); `dc6cc2d` 2025-08-10 (현재 58행 포함); `4fa700a` 2025-05-31 (현재 79행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 77행 포함); `4dc20a1` 2026-01-27 (현재 45행 포함).

```diff
@@ -35,48 +34,47 @@
 
     let h4 = textureLoad(txH, idx, 0);
     let u4 = textureLoad(txU, idx, 0);
-    let v4 = textureLoad(txV, idx, 0);
+   // let v4 = textureLoad(txV, idx, 0);
     let c4 = textureLoad(txC, idx, 0);
 
     let bottom = textureLoad(txBottom, idx, 0).z;
     
-    let h = (h4.x + h4.y + h4.z + h4.w) / 4.0;
-    let u = (u4.x + u4.y + u4.z + u4.w) / 4.0;
-    let v = (v4.x + v4.y + v4.z + v4.w) / 4.0;
-    let c = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-    var eta = textureLoad(txNewState, idx, 0).x;
+    let h = (h4.y + h4.w) / 2.0;
+    let u = (u4.y + u4.w) / 2.0;
+   // let v = (v4.x + v4.y + v4.z + v4.w) / 4.0;
+    let c = (c4.y + c4.w) / 2.0;
+    let eta = h + bottom;
     let P = h*u;
-    let Q = h*v;
-    let state_here = vec4<f32>(eta, u, v, c);
-    let speed = sqrt(u*u + v*v);
+   // let Q = h*v;
+   // let state_here = vec4<f32>(eta, u, v, c);
+    let state_here = vec4<f32>(eta, u, 0.0, c);
+   // let speed = sqrt(u*u + v*v);
+    let speed = sqrt(u*u);
     let hu2 = h*u*u;
-    let hv2 = h*v*v;
-    let momflux = sqrt(hu2*hu2 + hv2*hv2);
-    if (eta - bottom < globals.delta) {
-        // If the water depth is below the base depth, set velocities to zero
-        eta = -10.*globals.base_depth; // This is a placeholder for dry cells
-    }
+   // let hv2 = h*v*v;
+   // let momflux = sqrt(hu2*hu2 + hv2*hv2);
+    let momflux = sqrt(hu2*hu2);
 
     // for mean vorticity
-    let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));
-    let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
-    let u4_up = textureLoad(txU, upIdx, 0);
-    let u_up = (u4_up.x + u4_up.y + u4_up.z + u4_up.w) / 4.0;
-    let u4_down = textureLoad(txU, downIdx, 0);
-    let u_down = (u4_down.x + u4_down.y + u4_down.z + u4_down.w) / 4.0;
-    let v4_right = textureLoad(txV, rightIdx, 0);
-    let v_right = (v4_right.x + v4_right.y + v4_right.z + v4_right.w) / 4.0;
-    let v4_left = textureLoad(txV, leftIdx, 0);
-    let v_left = (v4_left.x + v4_left.y + v4_left.z + v4_left.w) / 4.0;
-    let vorticity = (u_up - u_down) / (2. * globals.dy) - (v_right - v_left) / (2. * globals.dx);
+   // let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));
+   // let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
+   // let u4_up = textureLoad(txU, upIdx, 0);
+   // let u_up = (u4_up.x + u4_up.y + u4_up.z + u4_up.w) / 4.0;
+   // let u4_down = textureLoad(txU, downIdx, 0);
+   // let u_down = (u4_down.x + u4_down.y + u4_down.z + u4_down.w) / 4.0;
+   // let v4_right = textureLoad(txV, rightIdx, 0);
+   // let v_right = (v4_right.x + v4_right.y + v4_right.z + v4_right.w) / 4.0;
+   // let v4_left = textureLoad(txV, leftIdx, 0);
+   // let v_left = (v4_left.x + v4_left.y + v4_left.z + v4_left.w) / 4.0;
+   // let vorticity = (u_up - u_down) / (2. * globals.dy) - (v_right - v_left) / (2. * globals.dx);
 
     let update_frac = 1. / f32(globals.n_time_steps_means);
     let old_frac = 1.0 - update_frac;
 
     let means_new = means_here*old_frac + state_here*update_frac;
-    let vorticity_means_new = momflux_means_here.w*old_frac + abs(vorticity)*update_frac;
+   // let vorticity_means_new = momflux_means_here.w*old_frac + abs(vorticity)*update_frac;
 
     var eta_max_new = 0.;
     var u_max_new = 0.;
```

#### CT1-164 통계 횡방향 출력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/CalcMeans.wgsl:87; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/CalcMeans.wgsl:85; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 v·hv2·와도의 통계 채널을 0.0으로 저장한다. x 속도·속력·x 운동량 flux·eta 최대값의 갱신 방식은 유지한다. |

본판 차이 줄의 마지막 수정: `e9c283b` 2025-04-24 (현재 95행 포함); `094fc2e` 2025-05-19 (현재 100행 포함); `4fa700a` 2025-05-31 (현재 101행 포함); `11b6bdc` 2025-05-08 (현재 102행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 103행 포함).

```diff
@@ -87,18 +85,21 @@
     var momflux_max_new = 0.;
     if (globals.n_time_steps_means > 1) {
         u_max_new = max(speed_means_here.x,u);
-        v_max_new = max(speed_means_here.y,v);
+       // v_max_new = max(speed_means_here.y,v);
         speed_max_new = max(speed_means_here.z,speed);
         eta_max_new = max(speed_means_here.a,eta);
 
         hu2_max_new = max(momflux_means_here.x,hu2);
-        hv2_max_new = max(momflux_means_here.y,hv2);
+       // hv2_max_new = max(momflux_means_here.y,hv2);
         momflux_max_new = max(momflux_means_here.z,momflux);
     }
 
     textureStore(txtemp_Means, idx, means_new);
-    textureStore(txtemp_Means_Speed, idx, vec4<f32>(u_max_new, v_max_new, speed_max_new, eta_max_new));
-    textureStore(txtemp_Means_Momflux, idx, vec4<f32>(hu2_max_new, hv2_max_new, momflux_max_new, vorticity_means_new));
-    textureStore(txModelVelocities, idx, vec4<f32>(u, v, eta, h));
+   // textureStore(txtemp_Means_Speed, idx, vec4<f32>(u_max_new, v_max_new, speed_max_new, eta_max_new));
+    textureStore(txtemp_Means_Speed, idx, vec4<f32>(u_max_new, 0.0, speed_max_new, eta_max_new));
+   // textureStore(txtemp_Means_Momflux, idx, vec4<f32>(hu2_max_new, hv2_max_new, momflux_max_new, vorticity_means_new));
+    textureStore(txtemp_Means_Momflux, idx, vec4<f32>(hu2_max_new, 0.0, momflux_max_new, 0.0));
+   // textureStore(txModelVelocities, idx, vec4<f32>(u, v, eta, h));
+    textureStore(txModelVelocities, idx, vec4<f32>(u, 0.0, eta, h));
 }
```


### 2.23 shaders/Copytxf32_txf16.wgsl

본판: `shaders/Copytxf32_txf16.wgsl`. transect 판: `transect_version/shaders/Copytxf32_txf16.wgsl`.
원래 diff는 53행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `dc6cc2d` | 2025-08-10 | update max free surface render |
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-165 표시용 건조 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Copytxf32_txf16.wgsl:1; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Copytxf32_txf16.wgsl:1; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 delta와 base_depth를 받는다. |

본판 차이 줄의 마지막 수정: `dc6cc2d` 2025-08-10 (현재 5행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -1,8 +1,6 @@
 struct Globals {
     width: i32,
     height: i32,
-    delta: f32,
-    base_depth: f32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-166 표시용 f16 패킹

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Copytxf32_txf16.wgsl:14; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Copytxf32_txf16.wgsl:12; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 건조 셀 eta를 -10*base_depth로 바꾸고 foam을 0으로 둔다. 본판은 3번째 레이어에 bottom·hardbottom·가용 깊이를 쓴다. transect 판은 eta와 foam을 그대로 두고 두 레이어만 쓴다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 48행 포함); `dc6cc2d` 2025-08-10 (현재 42행 포함); `34abfb1` 2025-04-23 (현재 37행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 25행 포함).

```diff
@@ -14,37 +12,24 @@
 @group(0) @binding(5) var txMeans_Momflux: texture_2d<f32>;
 @group(0) @binding(6) var txModelVelocities: texture_2d<f32>;
 @group(0) @binding(7) var txMeans: texture_2d<f32>;
-@group(0) @binding(8) var txHardBottom: texture_2d<f32>;
+
 
 @compute @workgroup_size(16, 16)
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
     
-    var eta = textureLoad(txNewState, idx, 0).r;
-    var foam = textureLoad(txNewState, idx, 0).a;
+    let eta = textureLoad(txNewState, idx, 0).r;
+    let foam = textureLoad(txNewState, idx, 0).a;
     let bottom = textureLoad(txBottom, idx, 0).b;
     let max_eta = textureLoad(txMeans_Speed, idx, 0).a;
-    if (eta - bottom < globals.delta) {
-        // If the water depth is below the base depth, set velocities to zero
-        eta = -10.0 * globals.base_depth; // This is a placeholder for dry cells
-        foam = 0.0; // Reset foam for dry cells
-    }
-
+    let output_layer0 = vec4<f32>(eta, max_eta, bottom, foam);
 
     let u = textureLoad(txModelVelocities, idx, 0).r;
     let v = textureLoad(txModelVelocities, idx, 0).g;
     let vort_mean = textureLoad(txMeans_Momflux, idx, 0).a;
-    
-    let hard_bottom = textureLoad(txHardBottom, idx, 0).r;
-    let avaliable_depth = bottom - hard_bottom;
-
-    
-    let output_layer0 = vec4<f32>(eta, max_eta, bottom, foam);
     let output_layer1 = vec4<f32>(u, v, 0.0, vort_mean);
-    let output_layer2 = vec4<f32>(bottom, hard_bottom, avaliable_depth, 0.0);
     
     textureStore(txRenderVarsf16, idx, 0, output_layer0);
     textureStore(txRenderVarsf16, idx, 1, output_layer1);
-    textureStore(txRenderVarsf16, idx, 2, output_layer2);
 }
```


### 2.24 shaders/ExtractTimeSeries.wgsl

본판: `shaders/ExtractTimeSeries.wgsl`. transect 판: `transect_version/shaders/ExtractTimeSeries.wgsl`.
원래 diff는 126행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `397c575` | 2025-09-09 | Max fs to tooltip for slide sims |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-167 교란 유형 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/ExtractTimeSeries.wgsl:7; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/ExtractTimeSeries.wgsl:7; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 disturbanceType을 받는다. |

본판 차이 줄의 마지막 수정: `397c575` 2025-09-09 (현재 10행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -7,7 +7,6 @@
     mouse_current_canvas_indY: i32,
     time: f32,
     river_sim: i32,
-    disturbanceType: i32
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-168 툴팁 최대수면 리소스

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/ExtractTimeSeries.wgsl:19; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/ExtractTimeSeries.wgsl:18; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 txMeans_Speed를 읽는다. |

본판 차이 줄의 마지막 수정: `397c575` 2025-09-09 (현재 22행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -19,7 +18,6 @@
 @group(0) @binding(5) var txWaveHeight: texture_2d<f32>; 
 @group(0) @binding(6) var txTimeSeries_Locations: texture_2d<f32>; 
 @group(0) @binding(7) var txTimeSeries_Data: texture_storage_2d<rgba32float, write>;
-@group(0) @binding(8) var txMeans_Speed: texture_2d<f32>;
 
 
 @compute @workgroup_size(1, 1)
```

#### CT1-169 툴팁 Hs 또는 최대수면 선택

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/ExtractTimeSeries.wgsl:44; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/ExtractTimeSeries.wgsl:42; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 disturbanceType>1이면 최대 수면을 쓴다. 나머지 경우 Hs를 쓴다. transect 판은 항상 Hs를 쓴다. |

본판 차이 줄의 마지막 수정: `397c575` 2025-09-09 (현재 52행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 45행 포함).

```diff
@@ -44,12 +42,7 @@
         }
         else {
             let waves = textureLoad(txState, current_location, 0).x;  // Free surface elevation
-            var hsig = 0.0;
-            if (globals.disturbanceType > 1) {
-                hsig = textureLoad(txMeans_Speed, current_location, 0).w;  // Max free surface elevation
-            } else {
-                hsig = textureLoad(txWaveHeight, current_location, 0).z;  // Significant wave height
-            }
+            let hsig = textureLoad(txWaveHeight, current_location, 0).z;  // Significant wave height
             output = vec4<f32>(bottom, waves, hsig, friction);
         }
     } else {  // for all other indices, store the time series data
```


### 2.25 shaders/MouseClickChange.wgsl

본판: `shaders/MouseClickChange.wgsl`. transect 판: `transect_version/shaders/MouseClickChange.wgsl`.
원래 diff는 388행이다. CR 제외 diff는 4구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `d778fe7` | 2026-06-02 | Added linear structures functionality |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-170 선형 구조물 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/MouseClickChange.wgsl:15; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/MouseClickChange.wgsl:15; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 천단고·천단폭·사면경사·양끝 좌표·적용 플래그를 받는다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 26행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -15,15 +15,6 @@
     designcomponent_Radius: f32,
     designcomponent_Friction: f32,
     changeSeaLevel_delta: f32,
-    // CODEX: Linear-structure bathy/topo edit parameters.
-    designcomponent_CrestElev: f32,
-    designcomponent_CrestWidth: f32,
-    designcomponent_SideSlope: f32,
-    designcomponent_StartX: f32,
-    designcomponent_StartY: f32,
-    designcomponent_EndX: f32,
-    designcomponent_EndY: f32,
-    designcomponent_AddLinearStructure: i32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-171 선분 거리와 사다리꼴 고도 함수

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/MouseClickChange.wgsl:66; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/MouseClickChange.wgsl:57; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 선분 투영을 [0,1]로 제한한다. 본판은 천단 절반폭 밖의 거리에 경사를 곱해 목표 고도를 만든다. 폭이나 경사가 0 이하면 -1e9를 반환한다. transect 판에는 두 함수가 없다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 102행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -66,40 +57,6 @@
     return dH;
 }
 
-// CODEX: Distance from a sample point to the finite linear-structure centerline, giving rounded end caps.
-fn calc_segment_distance(xloc: f32, yloc: f32, xstart: f32, ystart: f32, xend: f32, yend: f32) -> f32 {
-    let vx = xend - xstart;
-    let vy = yend - ystart;
-    let wx = xloc - xstart;
-    let wy = yloc - ystart;
-    let segment_len2 = vx * vx + vy * vy;
-    var t = 0.0;
-    if (segment_len2 > 1.0e-6) {
-        t = clamp((wx * vx + wy * vy) / segment_len2, 0.0, 1.0);
-    }
-    let closest_x = xstart + t * vx;
-    let closest_y = ystart + t * vy;
-    return calc_radial_distance(xloc, yloc, closest_x, closest_y);
-}
-
-// CODEX: Trapezoidal/capsule linear-structure target elevation, continuous through rounded endpoints.
-fn calc_linear_structure_elevation(xloc: f32, yloc: f32) -> f32 {
-    if (globals.designcomponent_CrestWidth <= 0.0 || globals.designcomponent_SideSlope <= 0.0) {
-        return -1.0e9;
-    }
-    let r = calc_segment_distance(
-        xloc,
-        yloc,
-        globals.designcomponent_StartX,
-        globals.designcomponent_StartY,
-        globals.designcomponent_EndX,
-        globals.designcomponent_EndY
-    );
-    let crest_half_width = 0.5 * globals.designcomponent_CrestWidth;
-    let side_distance = max(0.0, r - crest_half_width);
-    return globals.designcomponent_CrestElev - globals.designcomponent_SideSlope * side_distance;
-}
-
 
 @compute @workgroup_size(16, 16)
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
```

#### CT1-172 편집 대상 선택

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/MouseClickChange.wgsl:124; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/MouseClickChange.wgsl:81; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 선형 구조물 모드에서 바닥고·상태를 편집한다. transect 판은 설계 ID·마찰만 편집한다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 135행 포함); `98f41c9` 2024-04-18 (현재 139행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 86행 포함).

```diff
@@ -124,19 +81,9 @@
             min_val = textureLoad(txBottom, idx, 0).z;
         }
     } else if (globals.whichPanelisOpen == 2){  // design components editors
-        // B_here = textureLoad(txDesignComponents, idx, 0);
-        // B_here2 = textureLoad(txBottomFriction, idx, 0);
-        // min_val = 0.0;
-        // CODEX: Linear structures share this panel but edit bathy/topo instead of design-component IDs.
-        if (globals.designcomponent_AddLinearStructure == 1) {
-            B_here = textureLoad(txBottom, idx, 0);
-            B_here2 = textureLoad(txState, idx, 0);
-            min_val = -globals.base_depth;
-        } else {
-            B_here = textureLoad(txDesignComponents, idx, 0);
-            B_here2 = textureLoad(txBottomFriction, idx, 0);
-            min_val = 0.0;
-        }
+        B_here = textureLoad(txDesignComponents, idx, 0);
+        B_here2 = textureLoad(txBottomFriction, idx, 0);
+        min_val = 0.0;
     }
     let k = 4.0 / globals.changeRadius;  // will give a guassian that has a visual width of changeRadius
     let H = globals.changeAmplitude;
```

#### CT1-173 선형 구조물 적용

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/MouseClickChange.wgsl:196; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/MouseClickChange.wgsl:143; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 중심·북쪽 면·동쪽 면의 목표 고도를 계산해 기존 고도보다 낮추지 않게 쓴다. transect 판은 원형 영역의 설계 ID와 가우스 마찰 편집만 유지한다. 마지막 개행도 다르다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 224행 포함); `98f41c9` 2024-04-18 (현재 246행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 166행 포함).

```diff
@@ -196,51 +143,24 @@
             B_here.x = max(min_val,B_here.x + dH);
         }
     } else if (globals.whichPanelisOpen == 2){
-        // var r = calc_radial_distance(xloc,yloc,xo,yo);
-        // var dH = 0.0;
-        // var f = 0.0;
-        // if(r <= 0.5 * globals.designcomponent_Radius) {
-        //     f = 1.0;
-        // }
-        // dH = (f32(globals.designcomponentToAdd) - B_here.x)*f;
-        // B_here.x = max(min_val,B_here.x + dH);
-        //
-        // // change friction to match
-        // let k_friction = 4.0 / globals.designcomponent_Radius;
-        // f = calc_radial_function(xloc,yloc,xo,yo,k_friction);
-        //
-        // dH = (globals.designcomponent_Friction - B_here2.x)*f;
-        // B_here2.x = max(min_val,B_here2.x + dH);
-        // CODEX: Add a linear structure to bathy/topo using a rounded capsule footprint and trapezoidal cross-section.
-        if (globals.designcomponent_AddLinearStructure == 1) {
-            var target_elev = calc_linear_structure_elevation(xloc, yloc);
-            B_here.z = max(B_here.z, max(min_val, target_elev));
-
-            target_elev = calc_linear_structure_elevation(xloc, yloc + 0.5 * globals.dy);
-            B_here.x = max(B_here.x, max(min_val, target_elev));
-
-            target_elev = calc_linear_structure_elevation(xloc + 0.5 * globals.dx, yloc);
-            B_here.y = max(B_here.y, max(min_val, target_elev));
-        } else {
-            var r = calc_radial_distance(xloc,yloc,xo,yo);
-            var dH = 0.0;
-            var f = 0.0;
-            if(r <= 0.5 * globals.designcomponent_Radius) {
-                f = 1.0;
-            }
-            dH = (f32(globals.designcomponentToAdd) - B_here.x)*f;
-            B_here.x = max(min_val,B_here.x + dH);
-
-            // change friction to match
-            let k_friction = 4.0 / globals.designcomponent_Radius;
-            f = calc_radial_function(xloc,yloc,xo,yo,k_friction);
-
-            dH = (globals.designcomponent_Friction - B_here2.x)*f;
-            B_here2.x = max(min_val,B_here2.x + dH);
+        var r = calc_radial_distance(xloc,yloc,xo,yo);
+        var dH = 0.0;
+        var f = 0.0;
+        if(r <= 0.5 * globals.designcomponent_Radius) {
+            f = 1.0;
         }
+        dH = (f32(globals.designcomponentToAdd) - B_here.x)*f;
+        B_here.x = max(min_val,B_here.x + dH);
+
+        // change friction to match
+        let k_friction = 4.0 / globals.designcomponent_Radius; 
+        f = calc_radial_function(xloc,yloc,xo,yo,k_friction);
+        
+        dH = (globals.designcomponent_Friction - B_here2.x)*f;
+        B_here2.x = max(min_val,B_here2.x + dH);
 
     }
 
     textureStore(txtemp_MouseClick, idx, B_here);
     textureStore(txtemp_MouseClick2, idx, B_here2);
-}
+}
\ No newline at end of file
```


### 2.26 shaders/Pass0.wgsl

본판: `shaders/Pass0.wgsl`. transect 판: `transect_version/shaders/Pass0.wgsl`.
원래 diff는 123행이다. CR 제외 diff는 1구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `ebc98a5` | 2024-03-13 | Add files via upload |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-174 근방 수심의 1D 패킹

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass0.wgsl:25; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass0.wgsl:25; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 북·남 이웃을 읽지 않는다. h_vec의 x·z를 0.0으로 둔다. 동·서 면인 y·w는 본판과 같다. x 방향 Riemann flux가 쓰는 이웃 수심은 보존된다. |

본판 차이 줄의 마지막 수정: `ebc98a5` 2024-03-13 (현재 54행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 54행 포함).

```diff
@@ -25,33 +25,33 @@
 
     // Compute the coordinates of the neighbors for each pixel, and enforce boundary conditions
     let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+//    let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));
-    let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
+//    let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
 
     // Read in the state of the water at this pixel and its neighbors
 //    let in_here = textureLoad(txState, idx, 0).x;
-    let in_south = textureLoad(txState, downIdx, 0).x;
-    let in_north = textureLoad(txState, upIdx, 0).x;
+//    let in_south = textureLoad(txState, downIdx, 0).x;
+//    let in_north = textureLoad(txState, upIdx, 0).x;
     let in_west = textureLoad(txState, leftIdx, 0).x;
     let in_east = textureLoad(txState, rightIdx, 0).x;
 
 //    let B_here = textureLoad(txBottom, idx, 0).z;
-    let B_south = textureLoad(txBottom, downIdx, 0).z;
-    let B_north = textureLoad(txBottom, upIdx, 0).z;
+//    let B_south = textureLoad(txBottom, downIdx, 0).z;
+//    let B_north = textureLoad(txBottom, upIdx, 0).z;
     let B_west = textureLoad(txBottom, leftIdx, 0).z;
     let B_east = textureLoad(txBottom, rightIdx, 0).z;
 
 //    let h_here = in_here.x - B_here;
-    let h_south = in_south - B_south;
-    let h_north = in_north - B_north;
+//    let h_south = in_south - B_south;
+//    let h_north = in_north - B_north;
     let h_west = in_west - B_west;
     let h_east = in_east - B_east;
 
     var h_vec = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    h_vec.x= h_north; //min(h_here, h_north);
+    h_vec.x= 0.0; //h_north; //min(h_here, h_north);
     h_vec.y= h_east; //min(h_here, h_east);
-    h_vec.z= h_south; //min(h_here, h_south);
+    h_vec.z= 0.0; //h_south; //min(h_here, h_south);
     h_vec.w= h_west; //min(h_here, h_west);
 
     textureStore(txHnear, idx, h_vec);  //move this output texture to BC call, and keep the C calcs here
```


### 2.27 shaders/Pass1.wgsl

본판: `shaders/Pass1.wgsl`. transect 판: `transect_version/shaders/Pass1.wgsl`.
원래 diff는 358행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `83dd100` | 2025-05-12 | added 4th order reconstruction (Accuracy_mode = 1) |
| transect | `4dc20a1` | 2026-01-27 | transect updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-175 재구성 이웃과 건조 검사

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass1.wgsl:58; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass1.wgsl:58; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 동·서 이웃만 읽는다. 건조 조기 반환은 양쪽 x 이웃 수심으로 판정한다. y 속도 텍스처 쓰기를 생략한다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 80행 포함); `7542e27` 2024-05-24 (현재 90행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 91행 포함).

```diff
@@ -58,36 +58,37 @@
 
     // Compute the coordinates of the neighbors for each pixel, and enforce boundary conditions
     let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));
-    let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
+   // let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
 
     // Read in the state of the water at this pixel and its neighbors
     let in_here = textureLoad(txState, idx, 0);
-    let in_south = textureLoad(txState, downIdx, 0);
-    let in_north = textureLoad(txState, upIdx, 0);
+   // let in_south = textureLoad(txState, downIdx, 0);
+   // let in_north = textureLoad(txState, upIdx, 0);
     let in_west = textureLoad(txState, leftIdx, 0);
     let in_east = textureLoad(txState, rightIdx, 0);
 
     let B_here = textureLoad(txBottom, idx, 0).z;
-    let B_south = textureLoad(txBottom, downIdx, 0).z;
-    let B_north = textureLoad(txBottom, upIdx, 0).z;
+   // let B_south = textureLoad(txBottom, downIdx, 0).z;
+   // let B_north = textureLoad(txBottom, upIdx, 0).z;
     let B_west = textureLoad(txBottom, leftIdx, 0).z;
     let B_east = textureLoad(txBottom, rightIdx, 0).z;
 
     let h_here = in_here.x - B_here;
-    let h_south = in_south.x - B_south;
-    let h_north = in_north.x - B_north;
+   // let h_south = in_south.x - B_south;
+   // let h_north = in_north.x - B_north;
     let h_west = in_west.x - B_west;
     let h_east = in_east.x - B_east;
 
     let h_cut = globals.delta;
     if (h_here <= h_cut) {    //if dry and surrounded by dry, then stay dry - no need to calc
-        if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
+       // if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
+        if(h_east <= h_cut && h_west <= h_cut) {
             let zero = vec4<f32>(0.0, 0.0, 0.0, 0.0);
             textureStore(txH, idx, zero);
             textureStore(txU, idx, zero);
-            textureStore(txV, idx, zero);
+          //  textureStore(txV, idx, zero);
             textureStore(txC, idx, zero);
             return; 
         }
```

#### CT1-176 면 재구성과 Froude 제한의 1D 환원

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass1.wgsl:95; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass1.wgsl:96; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 북·남 면값을 0.0으로 둔다. 동·서 면의 eta·hu·hc 재구성은 같다. v=0을 대입하면 speed=sqrt(u*u)다. Froude 최대값은 Fr.y와 Fr.w에서 취한다. 지형 경사 제한은 dBdx만 사용한다. |

본판 차이 줄의 마지막 수정: `7542e27` 2024-05-24 (현재 105행 포함); `63a12e3` 2023-10-19 (현재 168행 포함); `ebc98a5` 2024-03-13 (현재 158행 포함); `efe44a2` 2024-04-02 (현재 159행 포함); `83dd100` 2025-05-12 (현재 133행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 179행 포함); `4dc20a1` 2026-01-27 (현재 140행 포함).

```diff
@@ -95,77 +96,87 @@
 
     // Load bed elevation data for this pixel's edges
     let Bxy = textureLoad(txBottom, idx, 0).xy;
-    let Bz = textureLoad(txBottom, downIdx, 0).x;
+   // let Bz = textureLoad(txBottom, downIdx, 0).x;
     let Bw = textureLoad(txBottom, leftIdx, 0).y;
-    let B = vec4<f32>(Bxy, Bz, Bw);
+   // let B = vec4<f32>(Bxy, Bz, Bw);
+    let B = vec4<f32>(Bxy, 0.0, Bw);
 
     let dB_west = abs(B_here - B_west);
     let dB_east = abs(B_here - B_east);
-    let dB_south = abs(B_here - B_south);
-    let dB_north = abs(B_here - B_north);
+   // let dB_south = abs(B_here - B_south);
+   // let dB_north = abs(B_here - B_north);
     var dB_max = vec4<f32>(0.0, 0.0, 0.0, 0.0);
 
     // Initialize variables for water height, momentum components, and standard deviation
     var h = vec4<f32>(0.0, 0.0, 0.0, 0.0);
     var w = vec4<f32>(0.0, 0.0, 0.0, 0.0);
     var hu = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    var hv = vec4<f32>(0.0, 0.0, 0.0, 0.0);
+   // var hv = vec4<f32>(0.0, 0.0, 0.0, 0.0);
     var hc = vec4<f32>(0.0, 0.0, 0.0, 0.0);
 
     // modify limiters based on whether near the inundation limit
-    let wetdry = min(h_here, min(h_south, min(h_north, min(h_west, h_east))));
+   // let wetdry = min(h_here, min(h_south, min(h_north, min(h_west, h_east))));
+    let wetdry = min(h_here, min(h_west, h_east));
     let rampcoef = min(max(0.0, wetdry / (0.02 * globals.base_depth)), 1.0);
     let TWO_THETAc = globals.TWO_THETA * rampcoef + 2.0 * (1.0 - rampcoef);  // transition to full upwinding near the shoreline / inundation limit, start transition with a total water depth of base_depth/50.
 
     if(wetdry <= globals.epsilon){
-        dB_max = 0.5*vec4<f32>(dB_north, dB_east, dB_south, dB_west);
+       // dB_max = 0.5*vec4<f32>(dB_north, dB_east, dB_south, dB_west);
+        dB_max = 0.5*vec4<f32>(0.0, dB_east, 0.0, dB_west);
     }
 
     let wwy = Reconstruct(in_west.x, in_here.x, in_east.x, TWO_THETAc);
     let huwy = Reconstruct(in_west.y, in_here.y, in_east.y, TWO_THETAc);
-    let hvwy = Reconstruct(in_west.z, in_here.z, in_east.z, TWO_THETAc);
+   // let hvwy = Reconstruct(in_west.z, in_here.z, in_east.z, TWO_THETAc);
     let hcwy = Reconstruct(in_west.w, in_here.w, in_east.w, TWO_THETAc);
 
-    let wzx = Reconstruct(in_south.x, in_here.x, in_north.x, TWO_THETAc);
-    let huzx = Reconstruct(in_south.y, in_here.y, in_north.y, TWO_THETAc);
-    let hvzx = Reconstruct(in_south.z, in_here.z, in_north.z, TWO_THETAc);
-    let hczx = Reconstruct(in_south.w, in_here.w, in_north.w, TWO_THETAc);
-
-    w = vec4<f32>(wzx.y, wwy.y, wzx.x, wwy.x);
-    h = w - B;
+   // let wzx = Reconstruct(in_south.x, in_here.x, in_north.x, TWO_THETAc);
+   // let huzx = Reconstruct(in_south.y, in_here.y, in_north.y, TWO_THETAc);
+   // let hvzx = Reconstruct(in_south.z, in_here.z, in_north.z, TWO_THETAc);
+   // let hczx = Reconstruct(in_south.w, in_here.w, in_north.w, TWO_THETAc);
+
+   // w = vec4<f32>(wzx.y, wwy.y, wzx.x, wwy.x);
+    w = vec4<f32>(0.0, wwy.y, 0.0, wwy.x);
+    h = vec4<f32>(0.0, wwy.y - B.y, 0.0, wwy.x - B.w);
     h = max(h, vec4<f32>(0.0, 0.0, 0.0, 0.0));
-    hu = vec4<f32>(huzx.y, huwy.y, huzx.x, huwy.x);
-    hv = vec4<f32>(hvzx.y, hvwy.y, hvzx.x, hvwy.x);
-    hc = vec4<f32>(hczx.y, hcwy.y, hczx.x, hcwy.x);
+   // hu = vec4<f32>(huzx.y, huwy.y, huzx.x, huwy.x);
+    hu = vec4<f32>(0.0, huwy.y, 0.0, huwy.x);
+   // hv = vec4<f32>(hvzx.y, hvwy.y, hvzx.x, hvwy.x);
+   // hc = vec4<f32>(hczx.y, hcwy.y, hczx.x, hcwy.x);
+    hc = vec4<f32>(0.0, hcwy.y, 0.0, hcwy.x);
 
     // CalcUVC 
     var u: vec4<f32>;
-    var v: vec4<f32>;
+   // var v: vec4<f32>;
     var c: vec4<f32>;
     let h2 = h * h;
     let epsilon_c = max(vec4<f32>(globals.epsilon), dB_max);
     let divide_by_h = 2.0 * h / (h2 + max(h2, epsilon_c));  // this is important - the local depth used for the edges should not be less than the difference in water depth across the edge
     u = divide_by_h * hu;
-    v = divide_by_h * hv;
+    u.x = 0.0;
+    u.z = 0.0;
+   // v = divide_by_h * hv;
     c = divide_by_h * hc;
 
     // Froude number limiter 
-    let speed = sqrt(u * u + v * v);
+   // let speed = sqrt(u * u + v * v);
+    let speed = sqrt(u * u);
     let Fr = speed / sqrt(9.81 / divide_by_h);
-    let Frumax = max(Fr.x, max(Fr.y, max(Fr.z, Fr.w)));
+   // let Frumax = max(Fr.x, max(Fr.y, max(Fr.z, Fr.w)));
+    let Frumax = max(Fr.y, Fr.w);
     let dBdx = abs(B_east - B_west) / (2.0 * globals.dx_global);
-    let dBdy = abs(B_north - B_south) / (2.0 * globals.dy_global);
-    let dBds_max = max(dBdx, dBdy);
-    let Fr_maxallowed = 3.0 / max(1.0, dBds_max);  // max Fr allowed on slopes less than 45 degrees is 3; for very steep slopes, artificially slow velocity - physics are just completely wrong here anyhow
+   // let dBdy = abs(B_north - B_south) / (2.0 * globals.dy_global);
+   // let dBds_max = max(dBdx, dBdy);
+    let Fr_maxallowed = 3.0 / max(1.0, dBdx);  // max Fr allowed on slopes less than 45 degrees is 3; for very steep slopes, artificially slow velocity - physics are just completely wrong here anyhow
     if (Frumax > Fr_maxallowed) {
         let Fr_red = Fr_maxallowed / Frumax;
         u = u * Fr_red;
-        v = v * Fr_red;
+       // v = v * Fr_red;
     }
 
     textureStore(txH, idx, h);
     textureStore(txU, idx, u);
-    textureStore(txV, idx, v);
+   // textureStore(txV, idx, v);
     textureStore(txC, idx, c);  //move this output texture to BC call, and keep the C calcs here
 
 }
```


### 2.28 shaders/Pass1_HighOrder.wgsl

본판: `shaders/Pass1_HighOrder.wgsl`. transect 판: `transect_version/shaders/Pass1_HighOrder.wgsl`.
원래 diff는 306행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `67ca57c` | 2025-05-22 | Added COULWAVE solver |
| transect | `4dc20a1` | 2026-01-27 | transect updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-177 고차 재구성 x 스텐실

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass1_HighOrder.wgsl:154; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass1_HighOrder.wgsl:154; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 ±1·±2·±3의 y 이웃 읽기를 생략한다. 건조 검사는 동·서 이웃만 사용한다. |

본판 차이 줄의 마지막 수정: `83dd100` 2025-05-12 (현재 216행 포함); `094fc2e` 2025-05-19 (현재 184행 포함); `67ca57c` 2025-05-22 (현재 200행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 217행 포함).

```diff
@@ -154,66 +154,67 @@
 
     // Compute the coordinates of the neighbors for each pixel, and enforce boundary conditions
     let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));
-    let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
+   // let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
    
     let right2Idx = min(idx + vec2<i32>(2, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let up2Idx = min(idx + vec2<i32>(0, 2), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let up2Idx = min(idx + vec2<i32>(0, 2), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let left2Idx = max(idx + vec2<i32>(-2, 0), vec2<i32>(0, 0));
-    let down2Idx = max(idx + vec2<i32>(0, -2), vec2<i32>(0, 0));
+   // let down2Idx = max(idx + vec2<i32>(0, -2), vec2<i32>(0, 0));
    
     let right3Idx = min(idx + vec2<i32>(3, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let up3Idx = min(idx + vec2<i32>(0, 3), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let up3Idx = min(idx + vec2<i32>(0, 3), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let left3Idx = max(idx + vec2<i32>(-3, 0), vec2<i32>(0, 0));
-    let down3Idx = max(idx + vec2<i32>(0, -3), vec2<i32>(0, 0));
+   // let down3Idx = max(idx + vec2<i32>(0, -3), vec2<i32>(0, 0));
 
     // Read in the state of the water at this pixel and its neighbors
     let in_here = textureLoad(txState, idx, 0);
-    let in_south = textureLoad(txState, downIdx, 0);
-    let in_north = textureLoad(txState, upIdx, 0);
+   // let in_south = textureLoad(txState, downIdx, 0);
+   // let in_north = textureLoad(txState, upIdx, 0);
     let in_west = textureLoad(txState, leftIdx, 0);
     let in_east = textureLoad(txState, rightIdx, 0);
 
-    let in_south2 = textureLoad(txState, down2Idx, 0);
-    let in_north2 = textureLoad(txState, up2Idx, 0);
+   // let in_south2 = textureLoad(txState, down2Idx, 0);
+   // let in_north2 = textureLoad(txState, up2Idx, 0);
     let in_west2 = textureLoad(txState, left2Idx, 0);
     let in_east2 = textureLoad(txState, right2Idx, 0);
 
-    let in_south3 = textureLoad(txState, down3Idx, 0);
-    let in_north3 = textureLoad(txState, up3Idx, 0);
+   // let in_south3 = textureLoad(txState, down3Idx, 0);
+   // let in_north3 = textureLoad(txState, up3Idx, 0);
     let in_west3 = textureLoad(txState, left3Idx, 0);
     let in_east3 = textureLoad(txState, right3Idx, 0);
 
     let B_here = textureLoad(txBottom, idx, 0).z;
-    let B_south = textureLoad(txBottom, downIdx, 0).z;
-    let B_north = textureLoad(txBottom, upIdx, 0).z;
+   // let B_south = textureLoad(txBottom, downIdx, 0).z;
+   // let B_north = textureLoad(txBottom, upIdx, 0).z;
     let B_west = textureLoad(txBottom, leftIdx, 0).z;
     let B_east = textureLoad(txBottom, rightIdx, 0).z;
 
-    let B_south2 = textureLoad(txBottom, down2Idx, 0).z;
-    let B_north2 = textureLoad(txBottom, up2Idx, 0).z;
+   // let B_south2 = textureLoad(txBottom, down2Idx, 0).z;
+   // let B_north2 = textureLoad(txBottom, up2Idx, 0).z;
     let B_west2 = textureLoad(txBottom, left2Idx, 0).z;
     let B_east2 = textureLoad(txBottom, right2Idx, 0).z;
 
-    let B_south3 = textureLoad(txBottom, down3Idx, 0).z;
-    let B_north3 = textureLoad(txBottom, up3Idx, 0).z;
+   // let B_south3 = textureLoad(txBottom, down3Idx, 0).z;
+   // let B_north3 = textureLoad(txBottom, up3Idx, 0).z;
     let B_west3 = textureLoad(txBottom, left3Idx, 0).z;
     let B_east3 = textureLoad(txBottom, right3Idx, 0).z;
 
     let h_here = in_here.x - B_here;
-    let h_south = in_south.x - B_south;
-    let h_north = in_north.x - B_north;
+   // let h_south = in_south.x - B_south;
+   // let h_north = in_north.x - B_north;
     let h_west = in_west.x - B_west;
     let h_east = in_east.x - B_east;
 
     let h_cut = globals.delta;
     if (h_here <= h_cut) {    //if dry and surrounded by dry, then stay dry - no need to calc
-        if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
+      //  if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
+        if(h_east <= h_cut && h_west <= h_cut) {
             let zero = vec4<f32>(0.0, 0.0, 0.0, 0.0);
             textureStore(txH, idx, zero);
             textureStore(txU, idx, zero);
-            textureStore(txV, idx, zero);
+          //  textureStore(txV, idx, zero);
             textureStore(txC, idx, zero);
             return; 
         }
```

#### CT1-178 고차 전환과 지형 최대값

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass1_HighOrder.wgsl:221; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass1_HighOrder.wgsl:222; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 wetdry와 maxB/maxB2/maxB3를 같은 행의 x 스텐실에서 취한다. 동·서 재구성의 저차 전환 조건과 TWO_THETAc 식은 유지한다. |

본판 차이 줄의 마지막 수정: `83dd100` 2025-05-12 (현재 275행 포함); `67ca57c` 2025-05-22 (현재 261행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 282행 포함).

```diff
@@ -221,58 +222,64 @@
 
     // Load bed elevation data for this pixel's edges
     let Bxy = textureLoad(txBottom, idx, 0).xy;
-    let Bz = textureLoad(txBottom, downIdx, 0).x;
+   // let Bz = textureLoad(txBottom, downIdx, 0).x;
     let Bw = textureLoad(txBottom, leftIdx, 0).y;
-    let B = vec4<f32>(Bxy, Bz, Bw);
+   // let B = vec4<f32>(Bxy, Bz, Bw);
+    let B = vec4<f32>(Bxy, 0.0, Bw);
 
     let dB_west = abs(B_here - B_west);
     let dB_east = abs(B_here - B_east);
-    let dB_south = abs(B_here - B_south);
-    let dB_north = abs(B_here - B_north);
+   // let dB_south = abs(B_here - B_south);
+   // let dB_north = abs(B_here - B_north);
     var dB_max = vec4<f32>(0.0, 0.0, 0.0, 0.0);
 
     // Initialize variables for water height, momentum components, and standard deviation
     var h = vec4<f32>(0.0, 0.0, 0.0, 0.0);
     var w = vec4<f32>(0.0, 0.0, 0.0, 0.0);
     var hu = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    var hv = vec4<f32>(0.0, 0.0, 0.0, 0.0);
+   // var hv = vec4<f32>(0.0, 0.0, 0.0, 0.0);
     var hc = vec4<f32>(0.0, 0.0, 0.0, 0.0);
 
     var wwy = vec2<f32>(0.0, 0.0);
     var wzx = vec2<f32>(0.0, 0.0);
     var huwy = vec2<f32>(0.0, 0.0);
     var huzx = vec2<f32>(0.0, 0.0);
-    var hvwy = vec2<f32>(0.0, 0.0);
-    var hvzx = vec2<f32>(0.0, 0.0);
+   // var hvwy = vec2<f32>(0.0, 0.0);
+   // var hvzx = vec2<f32>(0.0, 0.0);
     var hcwy = vec2<f32>(0.0, 0.0);
     var hczx = vec2<f32>(0.0, 0.0);
 
     // modify limiters based on whether near the inundation limit
-    let wetdry = min(h_here, min(h_south, min(h_north, min(h_west, h_east))));
+    //let wetdry = min(h_here, min(h_south, min(h_north, min(h_west, h_east))));
+    let wetdry = min(h_here, min(h_west, h_east));
     let rampcoef = min(max(0.0, wetdry / (0.02 * globals.base_depth)), 1.0);
     let TWO_THETAc = globals.TWO_THETA * rampcoef + 2.0 * (1.0 - rampcoef);  // transition to full upwinding near the shoreline / inundation limit, start transition with a total water depth of base_depth/50.
 
     if(wetdry <= globals.epsilon) {
-        dB_max = 0.5*vec4<f32>(dB_north, dB_east, dB_south, dB_west);
+       // dB_max = 0.5*vec4<f32>(dB_north, dB_east, dB_south, dB_west);
+        dB_max = 0.5*vec4<f32>(0.0, dB_east, 0.0, dB_west);
     }
 
-    let maxB =  max(B_here, max(B_south,  max(B_north,  max(B_west,  B_east))));
-    let maxB2 = max(maxB,   max(B_south2, max(B_north2, max(B_west2, B_east2))));
-    let maxB3 = max(maxB2,  max(B_south3, max(B_north3, max(B_west3, B_east3))));
+   // let maxB =  max(B_here, max(B_south,  max(B_north,  max(B_west,  B_east))));
+   // let maxB2 = max(maxB,   max(B_south2, max(B_north2, max(B_west2, B_east2))));
+   // let maxB3 = max(maxB2,  max(B_south3, max(B_north3, max(B_west3, B_east3))));
+    let maxB =  max(B_here, max(B_west,  B_east));
+    let maxB2 = max(maxB,   max(B_west2, B_east2));
+    let maxB3 = max(maxB2,  max(B_west3, B_east3));
 
     if(wetdry <= globals.epsilon || maxB3 >= -globals.epsilon) {
 
         // left / right: Use the original Reconstruct function for boundary conditions
         wwy =  Reconstruct(in_west.x, in_here.x, in_east.x, TWO_THETAc);
         huwy = Reconstruct(in_west.y, in_here.y, in_east.y, TWO_THETAc);
-        hvwy = Reconstruct(in_west.z, in_here.z, in_east.z, TWO_THETAc);
+      //  hvwy = Reconstruct(in_west.z, in_here.z, in_east.z, TWO_THETAc);
         hcwy = Reconstruct(in_west.w, in_here.w, in_east.w, TWO_THETAc);
 
         // south / north: Use the original Reconstruct function for boundary conditions
-        wzx =  Reconstruct(in_south.x, in_here.x, in_north.x, TWO_THETAc);
-        huzx = Reconstruct(in_south.y, in_here.y, in_north.y, TWO_THETAc);
-        hvzx = Reconstruct(in_south.z, in_here.z, in_north.z, TWO_THETAc);
-        hczx = Reconstruct(in_south.w, in_here.w, in_north.w, TWO_THETAc);
+       // wzx =  Reconstruct(in_south.x, in_here.x, in_north.x, TWO_THETAc);
+       // huzx = Reconstruct(in_south.y, in_here.y, in_north.y, TWO_THETAc);
+       // hvzx = Reconstruct(in_south.z, in_here.z, in_north.z, TWO_THETAc);
+       // hczx = Reconstruct(in_south.w, in_here.w, in_north.w, TWO_THETAc);
     } else {
 		var dh0 = in_west2.x-in_west3.x;
 		var dh1 = in_west.x-in_west2.x;
```

#### CT1-179 고차 면값과 유속 제한

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass1_HighOrder.wgsl:285; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass1_HighOrder.wgsl:292; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 x 방향 MUSCL4 재구성을 유지한다. 북·남 면과 hv를 제거한다. 건조 임계값 검사는 동·서 면에 남긴다. v=0 및 y 미분=0에서 속력과 지형 경사 제한의 본판 식이 transect 식으로 줄어든다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 333행 포함); `83dd100` 2025-05-12 (현재 364행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 376행 포함); `4dc20a1` 2026-01-27 (현재 315행 포함).

```diff
@@ -285,83 +292,88 @@
         // left / right: Use the high-order Reconstruct function for interior points
         wwy =  ReconstructMUSCL4(in_west3.x, in_west2.x, in_west.x, in_here.x, in_east.x, in_east2.x, in_east3.x, dh_max);
         huwy = ReconstructMUSCL4(in_west3.y, in_west2.y, in_west.y, in_here.y, in_east.y, in_east2.y, in_east3.y, dh_max);
-        hvwy = ReconstructMUSCL4(in_west3.z, in_west2.z, in_west.z, in_here.z, in_east.z, in_east2.z, in_east3.z, dh_max);
+       // hvwy = ReconstructMUSCL4(in_west3.z, in_west2.z, in_west.z, in_here.z, in_east.z, in_east2.z, in_east3.z, dh_max);
         hcwy = ReconstructMUSCL4(in_west3.w, in_west2.w, in_west.w, in_here.w, in_east.w, in_east2.w, in_east3.w, dh_max);
 
-        dh0 = in_south2.x-in_south3.x;
-        dh1 = in_south.x-in_south2.x;
-        dh2 = in_here.x-in_south.x;
-        dh3 = in_north.x-in_here.x;
-        dh4 = in_north2.x-in_north.x;
-        dh5 = in_north3.x-in_north2.x;
-        dh_max = max(max(abs(dh0), abs(dh1)), max(abs(dh2), max(abs(dh3), max(abs(dh4), abs(dh5))))) / globals.dy_global;
+       // dh0 = in_south2.x-in_south3.x;
+       // dh1 = in_south.x-in_south2.x;
+       // dh2 = in_here.x-in_south.x;
+       // dh3 = in_north.x-in_here.x;
+       // dh4 = in_north2.x-in_north.x;
+       // dh5 = in_north3.x-in_north2.x;
+       // dh_max = max(max(abs(dh0), abs(dh1)), max(abs(dh2), max(abs(dh3), max(abs(dh4), abs(dh5))))) / globals.dy_global;
 
         // south / north: Use the high-order Reconstruct function for interior points
-        wzx =  ReconstructMUSCL4(in_south3.x, in_south2.x, in_south.x, in_here.x, in_north.x, in_north2.x, in_north3.x, dh_max);
-        huzx = ReconstructMUSCL4(in_south3.y, in_south2.y, in_south.y, in_here.y, in_north.y, in_north2.y, in_north3.y, dh_max);
-        hvzx = ReconstructMUSCL4(in_south3.z, in_south2.z, in_south.z, in_here.z, in_north.z, in_north2.z, in_north3.z, dh_max);
-        hczx = ReconstructMUSCL4(in_south3.w, in_south2.w, in_south.w, in_here.w, in_north.w, in_north2.w, in_north3.w, dh_max);
-    }
-
-    w = vec4<f32>(wzx.y, wwy.y, wzx.x, wwy.x);
-    h = w - B;
-    hu = vec4<f32>(huzx.y, huwy.y, huzx.x, huwy.x);
-    hv = vec4<f32>(hvzx.y, hvwy.y, hvzx.x, hvwy.x);
-    hc = vec4<f32>(hczx.y, hcwy.y, hczx.x, hcwy.x);
-
-    if (h.x < globals.delta) {
-        h.x = 0.0;;
-        hu.x = 0.0;
-        hv.x = 0.0;
-        hc.x = 0.0;
-    }
+       // wzx =  ReconstructMUSCL4(in_south3.x, in_south2.x, in_south.x, in_here.x, in_north.x, in_north2.x, in_north3.x, dh_max);
+       // huzx = ReconstructMUSCL4(in_south3.y, in_south2.y, in_south.y, in_here.y, in_north.y, in_north2.y, in_north3.y, dh_max);
+       // hvzx = ReconstructMUSCL4(in_south3.z, in_south2.z, in_south.z, in_here.z, in_north.z, in_north2.z, in_north3.z, dh_max);
+       // hczx = ReconstructMUSCL4(in_south3.w, in_south2.w, in_south.w, in_here.w, in_north.w, in_north2.w, in_north3.w, dh_max);
+    }
+
+   // w = vec4<f32>(wzx.y, wwy.y, wzx.x, wwy.x);
+    w = vec4<f32>(0.0, wwy.y, 0.0, wwy.x);
+    h = vec4<f32>(0.0, wwy.y - B.y, 0.0, wwy.x - B.w);
+   // hu = vec4<f32>(huzx.y, huwy.y, huzx.x, huwy.x);
+    hu = vec4<f32>(0.0, huwy.y, 0.0, huwy.x);
+   // hv = vec4<f32>(hvzx.y, hvwy.y, hvzx.x, hvwy.x);
+   // hc = vec4<f32>(hczx.y, hcwy.y, hczx.x, hcwy.x);
+    hc = vec4<f32>(0.0, hcwy.y, 0.0, hcwy.x);
+
+   // if (h.x < globals.delta) {
+   //     h.x = 0.0;;
+   //     hu.x = 0.0;
+   //     hv.x = 0.0;
+   //     hc.x = 0.0;
+   // }
     if (h.y < globals.delta) {
         h.y =0.0;;
         hu.y = 0.0;
-        hv.y = 0.0;
+      //  hv.y = 0.0;
         hc.y = 0.0;
     }   
-    if (h.z < globals.delta) {
-        h.z =0.0;;
-        hu.z = 0.0;
-        hv.z = 0.0;
-        hc.z = 0.0;
-    }
+   // if (h.z < globals.delta) {
+   //     h.z =0.0;;
+   //     hu.z = 0.0;
+   //     hv.z = 0.0;
+   //     hc.z = 0.0;
+   // }
     if (h.w < globals.delta) {
         h.w =0.0;;
         hu.w = 0.0;
-        hv.w = 0.0;
+      //  hv.w = 0.0;
         hc.w = 0.0;
     }
 
     // CalcUVC 
     var u: vec4<f32>;
-    var v: vec4<f32>;
+   // var v: vec4<f32>;
     var c: vec4<f32>;
     let h2 = h * h;
     let epsilon_c = max(vec4<f32>(globals.epsilon), dB_max);
     let divide_by_h = 2.0 * h / (h2 + max(h2, epsilon_c));  // this is important - the local depth used for the edges should not be less than the difference in water depth across the edge
     u = divide_by_h * hu;
-    v = divide_by_h * hv;
+   // v = divide_by_h * hv;
     c = divide_by_h * hc;
 
     // Froude number limiter 
-    let speed = sqrt(u * u + v * v);
+   // let speed = sqrt(u * u + v * v);
+    let speed = sqrt(u * u);
     let Fr = speed / sqrt(9.81 / divide_by_h);
-    let Frumax = max(Fr.x, max(Fr.y, max(Fr.z, Fr.w)));
+   // let Frumax = max(Fr.x, max(Fr.y, max(Fr.z, Fr.w)));
+    let Frumax = max(Fr.y, Fr.w);
     let dBdx = abs(B_east - B_west) / (2.0 * globals.dx_global);
-    let dBdy = abs(B_north - B_south) / (2.0 * globals.dy_global);
-    let dBds_max = max(dBdx, dBdy);
-    let Fr_maxallowed = 3.0 / max(1.0, dBds_max);  // max Fr allowed on slopes less than 45 degrees is 3; for very steep slopes, artificially slow velocity - physics are just completely wrong here anyhow
+   // let dBdy = abs(B_north - B_south) / (2.0 * globals.dy_global);
+   // let dBds_max = max(dBdx, dBdy);
+    let Fr_maxallowed = 3.0 / max(1.0, dBdx);  // max Fr allowed on slopes less than 45 degrees is 3; for very steep slopes, artificially slow velocity - physics are just completely wrong here anyhow
     if (Frumax > Fr_maxallowed) {
         let Fr_red = Fr_maxallowed / Frumax;
         u = u * Fr_red;
-        v = v * Fr_red;
+       // v = v * Fr_red;
     }
 
     textureStore(txH, idx, h);
     textureStore(txU, idx, u);
-    textureStore(txV, idx, v);
+   // textureStore(txV, idx, v);
     textureStore(txC, idx, c);  //move this output texture to BC call, and keep the C calcs here
 
 }
```


### 2.29 shaders/Pass2.wgsl

본판: `shaders/Pass2.wgsl`. transect 판: `transect_version/shaders/Pass2.wgsl`.
원래 diff는 390행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-180 퇴적물 확산 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass2.wgsl:7; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass2.wgsl:7; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 배경 확산과 쇄파 확산계수를 받는다. transect 판은 Pass2의 확산 보정을 구현하지 않는다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 11행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -7,8 +7,6 @@
     dy: f32,
     delta: f32,
     useSedTransModel: i32,
-    sedTurbDispersion: f32,
-    sedBreakingDispersionCoef: f32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-181 쇄파 입력 binding

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass2.wgsl:31; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass2.wgsl:29; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 binding 15에서 쇄파 점성을 읽는다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 35행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -31,8 +29,6 @@
 @group(0) @binding(13) var txXFlux_Sed: texture_storage_2d<rgba32float, write>;
 @group(0) @binding(14) var txYFlux_Sed: texture_storage_2d<rgba32float, write>;
 
-@group(0) @binding(15) var txBreaking: texture_2d<f32>;
-
 fn NumericalFlux(aplus: f32, aminus: f32, Fplus: f32, Fminus: f32, Udifference: f32) -> f32 {
     if (aplus - aminus != 0.0) {
         return (aplus * Fminus - aminus * Fplus + aplus * aminus * Udifference) / (aplus - aminus);
```

#### CT1-182 수치 flux 1D 환원

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass2.wgsl:62; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass2.wgsl:58; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 x 방향 HLL 함수를 유지한다. y flux 저장을 생략한다. x flux의 횡운동량 채널은 0.0이다. minH는 동·서 면만 검사한다. 본판의 Class 1 확산 flux 추가는 별도 판 차이다. transect 판은 농도 flux에서 순수 이류와 수치 확산만 계산한다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 137행 포함); `ebc98a5` 2024-03-13 (현재 132행 포함); `b8b50c3` 2025-06-08 (현재 197행 포함); `85c2ca2` 2024-03-19 (현재 204행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 179행 포함).

```diff
@@ -62,145 +58,124 @@
     
     // Handle boundary conditions
     let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));
-    let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
+   // let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
     
     // Fetch the necessary data from the input textures
     let h_vec = textureLoad(txHnear, idx, 0);
     let h_here = textureLoad(txH, idx, 0).xy;
     
     let hW_east = textureLoad(txH, rightIdx, 0).w;
-    let hS_north = textureLoad(txH, upIdx, 0).z;
+   // let hS_north = textureLoad(txH, upIdx, 0).z;
 
     let u_here = textureLoad(txU, idx, 0).xy;
     let uW_east = textureLoad(txU, rightIdx, 0).w;
-    let uS_north = textureLoad(txU, upIdx, 0).z;
+   // let uS_north = textureLoad(txU, upIdx, 0).z;
 
     let v_here = textureLoad(txV, idx, 0).xy;
     let vW_east = textureLoad(txV, rightIdx, 0).w;
-    let vS_north = textureLoad(txV, upIdx, 0).z;
+   // let vS_north = textureLoad(txV, upIdx, 0).z;
 
     let cNE = sqrt((globals.g * h_here));
     let cW = sqrt((globals.g * hW_east));
-    let cS = sqrt((globals.g * hS_north));
+   // let cS = sqrt((globals.g * hS_north));
 
     let aplus = max(max(u_here.y + cNE.y, uW_east + cW), 0.0);
     let aminus = min(min(u_here.y - cNE.y, uW_east - cW), 0.0);
-    let bplus = max(max(v_here.x + cNE.x, vS_north + cS), 0.0);
-    let bminus = min(min(v_here.x - cNE.x, vS_north - cS), 0.0);
+   // let bplus = max(max(v_here.x + cNE.x, vS_north + cS), 0.0);
+   // let bminus = min(min(v_here.x - cNE.x, vS_north - cS), 0.0);
 
     let B_here = textureLoad(txBottom, idx, 0).z;
-    let dB = max(textureLoad(txBottom, downIdx, 0).z - B_here, max(textureLoad(txBottom, upIdx, 0).z - B_here, max(textureLoad(txBottom, leftIdx, 0).z - B_here, textureLoad(txBottom, rightIdx, 0).z - B_here)));
+   // let dB = max(textureLoad(txBottom, downIdx, 0).z - B_here, max(textureLoad(txBottom, upIdx, 0).z - B_here, max(textureLoad(txBottom, leftIdx, 0).z - B_here, textureLoad(txBottom, rightIdx, 0).z - B_here)));
+    let dB = max(textureLoad(txBottom, rightIdx, 0).z - B_here, textureLoad(txBottom, leftIdx, 0).z - B_here);
 
     let near_dry = textureLoad(txBottom, idx, 0).w;
 
     let c_here = textureLoad(txC, idx, 0).xy;
     let cW_east = textureLoad(txC, rightIdx, 0).w;
-    let cS_north = textureLoad(txC, upIdx, 0).z;
+   // let cS_north = textureLoad(txC, upIdx, 0).z;
 
     var phix = 0.5;
-    var phiy = 0.5;
+   // var phiy = 0.5;
+
+   // let minH = min(h_vec.w, min(h_vec.z, min(h_vec.y, h_vec.x)));
+    let minH = min(h_vec.w, h_vec.y);  // minimum water height in the cell and its neighbors
 
-    let minH = min(h_vec.w, min(h_vec.z, min(h_vec.y, h_vec.x)));
     var mass_diff_x = (hW_east - h_here.y);
-    var mass_diff_y = (hS_north - h_here.x);
+   // var mass_diff_y = (hS_north - h_here.x);
     
     var P_diff_x = (hW_east * uW_east - h_here.y * u_here.y);
-    var P_diff_y = (hS_north * uS_north - h_here.x * u_here.x);
+   // var P_diff_y = (hS_north * uS_north - h_here.x * u_here.x);
     
-    var Q_diff_x = (hW_east * vW_east - h_here.y * v_here.y);
-    var Q_diff_y = (hS_north * vS_north - h_here.x * v_here.x);
+   // var Q_diff_x = (hW_east * vW_east - h_here.y * v_here.y);
+   // var Q_diff_y = (hS_north * vS_north - h_here.x * v_here.x);
 
     if (minH <= globals.delta) {
         mass_diff_x = 0.0;
-        mass_diff_y = 0.0;
+      //  mass_diff_y = 0.0;
         phix = 1.0;
-        phiy = 1.0;
+      //  phiy = 1.0;
     }
 
+   // let xflux = vec4<f32>(
+   //     NumericalFlux(aplus, aminus, hW_east * uW_east, h_here.y * u_here.y, mass_diff_x),
+   //     NumericalFlux(aplus, aminus, hW_east * uW_east * uW_east, h_here.y * u_here.y * u_here.y, P_diff_x),
+   //     NumericalFlux(aplus, aminus, hW_east * uW_east * vW_east, h_here.y * u_here.y * v_here.y, Q_diff_x),
+   //     NumericalFlux(aplus, aminus, hW_east * uW_east * cW_east, h_here.y * u_here.y * c_here.y, phix * (hW_east * cW_east - h_here.y * c_here.y))
+   // );
+
     let xflux = vec4<f32>(
         NumericalFlux(aplus, aminus, hW_east * uW_east, h_here.y * u_here.y, mass_diff_x),
         NumericalFlux(aplus, aminus, hW_east * uW_east * uW_east, h_here.y * u_here.y * u_here.y, P_diff_x),
-        NumericalFlux(aplus, aminus, hW_east * uW_east * vW_east, h_here.y * u_here.y * v_here.y, Q_diff_x),
+        NumericalFlux(aplus, aminus, 0.0, 0.0, 0.0),
         NumericalFlux(aplus, aminus, hW_east * uW_east * cW_east, h_here.y * u_here.y * c_here.y, phix * (hW_east * cW_east - h_here.y * c_here.y))
     );
+
         
-    let yflux = vec4<f32>(
-        NumericalFlux(bplus, bminus, hS_north * vS_north, h_here.x * v_here.x, mass_diff_y),
-        NumericalFlux(bplus, bminus, hS_north * uS_north * vS_north, h_here.x * u_here.x * v_here.x, P_diff_y),
-        NumericalFlux(bplus, bminus, hS_north * vS_north * vS_north, h_here.x * v_here.x * v_here.x, Q_diff_y),
-        NumericalFlux(bplus, bminus, hS_north * cS_north * vS_north, h_here.x * c_here.x * v_here.x, phiy * (hS_north * cS_north - h_here.x * c_here.x))
-    );
+   // let yflux = vec4<f32>(
+   //     NumericalFlux(bplus, bminus, hS_north * vS_north, h_here.x * v_here.x, mass_diff_y),
+   //     NumericalFlux(bplus, bminus, hS_north * uS_north * vS_north, h_here.x * u_here.x * v_here.x, P_diff_y),
+   //     NumericalFlux(bplus, bminus, hS_north * vS_north * vS_north, h_here.x * v_here.x * v_here.x, Q_diff_y),
+   //     NumericalFlux(bplus, bminus, hS_north * cS_north * vS_north, h_here.x * c_here.x * v_here.x, phiy * (hS_north * cS_north - h_here.x * c_here.x))
+   // );
 
     textureStore(txXFlux, idx, xflux);
-    textureStore(txYFlux, idx, yflux);
+   // textureStore(txYFlux, idx, yflux);
 
     if(globals.useSedTransModel == 1){
-        
-        let k_here =  globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, idx, 0).y;
-        let k_right =  globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, rightIdx, 0).y;
-        let k_up = globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, upIdx, 0).y;
-        let k_left =  globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, leftIdx, 0).y;
-        let k_down = globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, downIdx, 0).y;
-
-        let k_east = 0.5 * (k_here + k_right);
-        let k_north = 0.5 * (k_here + k_up);
-        let k_west = 0.5 * (k_here + k_left);
-        let k_south = 0.5 * (k_here + k_down);
-
         // Sediment transport code
         let c1_here = textureLoad(txSed_C1, idx, 0).xy;
         let c1W_east = textureLoad(txSed_C1, rightIdx, 0).w;
-        let c1S_north = textureLoad(txSed_C1, upIdx, 0).z;
+       // let c1S_north = textureLoad(txSed_C1, upIdx, 0).z;
 
         let c2_here = textureLoad(txSed_C2, idx, 0).xy;
         let c2W_east = textureLoad(txSed_C2, rightIdx, 0).w;
-        let c2S_north = textureLoad(txSed_C2, upIdx, 0).z;
+       // let c2S_north = textureLoad(txSed_C2, upIdx, 0).z;
 
         let c3_here = textureLoad(txSed_C3, idx, 0).xy;
         let c3W_east = textureLoad(txSed_C3, rightIdx, 0).w;
-        let c3S_north = textureLoad(txSed_C3, upIdx, 0).z;
+       // let c3S_north = textureLoad(txSed_C3, upIdx, 0).z;
 
         let c4_here = textureLoad(txSed_C4, idx, 0).xy;
         let c4W_east = textureLoad(txSed_C4, rightIdx, 0).w;
-        let c4S_north = textureLoad(txSed_C4, upIdx, 0).z;
-
-        // this only works for one class right now
-        var c4 = textureLoad(txSed_C1, idx, 0);
-        let C_here = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-        c4 = textureLoad(txSed_C1, rightIdx, 0);
-        let C_right = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-        c4 = textureLoad(txSed_C1, leftIdx, 0);
-        let C_left = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-        c4 = textureLoad(txSed_C1, upIdx, 0);
-        let C_up = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-        c4 = textureLoad(txSed_C1, downIdx, 0);
-        let C_down = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-
-        let C1x_east = (C_right - C_here) / globals.dx;
-        let C1x_west = (C_here - C_left) / globals.dx;
-        let C1y_north =(C_up - C_here) / globals.dy;
-        let C1y_south =(C_here - C_down) / globals.dy;
-        
-        phix = 0.5;
-        phiy = 0.5;
+       // let c4S_north = textureLoad(txSed_C4, upIdx, 0).z;
 
         let xflux_Sed = vec4<f32>(
-            NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),
+            NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east, h_here.y * u_here.y * c1_here.y, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),
             NumericalFlux(aplus, aminus, hW_east * uW_east * c2W_east, h_here.y * u_here.y * c2_here.y, phix * (hW_east * c2W_east - h_here.y * c2_here.y)),
             NumericalFlux(aplus, aminus, hW_east * uW_east * c3W_east, h_here.y * u_here.y * c3_here.y, phix * (hW_east * c3W_east - h_here.y * c3_here.y)),
             NumericalFlux(aplus, aminus, hW_east * uW_east * c4W_east, h_here.y * u_here.y * c4_here.y, phix * (hW_east * c4W_east - h_here.y * c4_here.y))
         );
             
-        let yflux_Sed = vec4<f32>(
-            NumericalFlux(bplus, bminus, hS_north * c1S_north * vS_north - k_north * hS_north * C1y_north, h_here.x * c1_here.x * v_here.x - k_south * h_here.x * C1y_south, phiy * (hS_north * c1S_north - h_here.x * c1_here.x)),
-            NumericalFlux(bplus, bminus, hS_north * c2S_north * vS_north, h_here.x * c2_here.x * v_here.x, phiy * (hS_north * c2S_north - h_here.x * c2_here.x)),
-            NumericalFlux(bplus, bminus, hS_north * c3S_north * vS_north, h_here.x * c3_here.x * v_here.x, phiy * (hS_north * c3S_north - h_here.x * c3_here.x)),
-            NumericalFlux(bplus, bminus, hS_north * c4S_north * vS_north, h_here.x * c4_here.x * v_here.x, phiy * (hS_north * c4S_north - h_here.x * c4_here.x))
-        );
+       // let yflux_Sed = vec4<f32>(
+       //     NumericalFlux(bplus, bminus, hS_north * c1S_north * vS_north, h_here.x * c1_here.x * v_here.x, phiy * (hS_north * c1S_north - h_here.x * c1_here.x)),
+       //     NumericalFlux(bplus, bminus, hS_north * c2S_north * vS_north, h_here.x * c2_here.x * v_here.x, phiy * (hS_north * c2S_north - h_here.x * c2_here.x)),
+       //     NumericalFlux(bplus, bminus, hS_north * c3S_north * vS_north, h_here.x * c3_here.x * v_here.x, phiy * (hS_north * c3S_north - h_here.x * c3_here.x)),
+       //     NumericalFlux(bplus, bminus, hS_north * c4S_north * vS_north, h_here.x * c4_here.x * v_here.x, phiy * (hS_north * c4S_north - h_here.x * c4_here.x))
+       // );
 
         textureStore(txXFlux_Sed, idx, xflux_Sed);
-        textureStore(txYFlux_Sed, idx, yflux_Sed);
+       // textureStore(txYFlux_Sed, idx, yflux_Sed);
     }
 }
```


### 2.30 shaders/Pass3A_COULWAVE.wgsl

본판: `shaders/Pass3A_COULWAVE.wgsl`. transect 판: `transect_version/shaders/Pass3A_COULWAVE.wgsl`.
원래 diff는 64행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `67ca57c` | 2025-05-22 | Added COULWAVE solver |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-183 COULWAVE 면속도 평균의 절반값

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3A_COULWAVE.wgsl:24; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3A_COULWAVE.wgsl:24; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 북·남 txU 채널을 0으로 쓰지만 u_here는 여전히 네 채널 합을 4.0으로 나눈다. 같은 판 CalcMeans는 동·서 두 채널 합을 2.0으로 나눈다. 일정한 x 면속도 U에서 Pass3A 결과는 U/2다. 단면 가정과 평균식의 모순을 강함으로 둔다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 35행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 35행 포함).

```diff
@@ -24,15 +24,15 @@
     let idx = vec2<i32>(i32(id.x), i32(id.y));
 
     let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));
-    let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
+   // let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
 
     // u, v here
     var u4 = textureLoad(txU, idx, 0);
-    var v4 = textureLoad(txV, idx, 0);
+   // var v4 = textureLoad(txV, idx, 0);
     let u_here = (u4.x + u4.y + u4.z + u4.w) / 4.0;
-    let v_here = (v4.x + v4.y + v4.z + v4.w) / 4.0;
+   // let v_here = (v4.x + v4.y + v4.z + v4.w) / 4.0;
 
     // eta, depth here
     let eta_here = textureLoad(txState, idx, 0).x;
```

#### CT1-184 COULWAVE 보조장 패킹

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3A_COULWAVE.wgsl:59; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3A_COULWAVE.wgsl:59; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 v·za_y·dv를 0으로 저장한다. za_here와 za_x 식은 유지한다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 80행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 84행 포함).

```diff
@@ -59,25 +59,29 @@
     //let za_im1 = d_im1 * globals.Bous_alpha;
 
     // depth up
-    let eta_jp1 = textureLoad(txState, upIdx, 0).x;
-    let d_jp1 = -textureLoad(txBottom, upIdx, 0).z;
-    let H_jp1 = max(globals.delta, eta_jp1 + d_jp1);
-    let za_jp1 = -d_jp1 + ( 1.0 + globals.Bous_alpha ) * H_jp1;
+   // let eta_jp1 = textureLoad(txState, upIdx, 0).x;
+   // let d_jp1 = -textureLoad(txBottom, upIdx, 0).z;
+   // let H_jp1 = max(globals.delta, eta_jp1 + d_jp1);
+   // let za_jp1 = -d_jp1 + ( 1.0 + globals.Bous_alpha ) * H_jp1;
     //let za_jp1 = d_jp1 * globals.Bous_alpha;
 
     // depth down
-    let eta_jm1 = textureLoad(txState, downIdx, 0).x;
-    let d_jm1 = -textureLoad(txBottom, downIdx, 0).z;
-    let H_jm1 = max(globals.delta, eta_jm1 + d_jm1);
-    let za_jm1 = -d_jm1 + ( 1.0 + globals.Bous_alpha ) * H_jm1;
+   // let eta_jm1 = textureLoad(txState, downIdx, 0).x;
+   // let d_jm1 = -textureLoad(txBottom, downIdx, 0).z;
+   // let H_jm1 = max(globals.delta, eta_jm1 + d_jm1);
+   // let za_jm1 = -d_jm1 + ( 1.0 + globals.Bous_alpha ) * H_jm1;
     //let za_jm1 = d_jm1 * globals.Bous_alpha;
 
     let dzadx = 0.5 * (za_ip1 - za_im1) * globals.one_over_dx;
-    let dzady = 0.5 * (za_jp1 - za_jm1) * globals.one_over_dy;
+   // let dzady = 0.5 * (za_jp1 - za_jm1) * globals.one_over_dy;
 
-    let vel_out = vec4<f32>(u_here, v_here, eta_here, H_here);
-    let za_out = vec4<f32>(za_here, dzadx, dzady, 0.0);
-    let uvhuhv = vec4<f32>(u_here, v_here, u_here * d_here, v_here * d_here);
+   // let vel_out = vec4<f32>(u_here, v_here, eta_here, H_here);
+   // let za_out = vec4<f32>(za_here, dzadx, dzady, 0.0);
+   // let uvhuhv = vec4<f32>(u_here, v_here, u_here * d_here, v_here * d_here);
+
+    let vel_out = vec4<f32>(u_here, 0.0, eta_here, H_here);
+    let za_out = vec4<f32>(za_here, dzadx, 0.0, 0.0);
+    let uvhuhv = vec4<f32>(u_here, 0.0, u_here * d_here, 0.0);
 
     textureStore(txModelVelocities, idx, vel_out);
     textureStore(txCW_zalpha, idx, za_out);
```


### 2.31 shaders/Pass3B_COULWAVE.wgsl

본판: `shaders/Pass3B_COULWAVE.wgsl`. transect 판: `transect_version/shaders/Pass3B_COULWAVE.wgsl`.
원래 diff는 254행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `67ca57c` | 2025-05-22 | Added COULWAVE solver |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-185 COULWAVE 보조장 x 스텐실

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3B_COULWAVE.wgsl:27; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3B_COULWAVE.wgsl:27; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 y·대각 이웃과 v·dv 읽기를 생략한다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 48행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 48행 포함).

```diff
@@ -27,25 +27,25 @@
 
  // Compute the coordinates of the neighbors for each pixel, and enforce boundary conditions
     let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));
-    let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
+   // let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
     let rightrightIdx = min(idx + vec2<i32>(2, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let upupIdx = min(idx + vec2<i32>(0, 2), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let upupIdx = min(idx + vec2<i32>(0, 2), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let leftleftIdx = max(idx + vec2<i32>(-2, 0), vec2<i32>(0, 0));
-    let downdownIdx = max(idx + vec2<i32>(0, -2), vec2<i32>(0, 0));
+   // let downdownIdx = max(idx + vec2<i32>(0, -2), vec2<i32>(0, 0));
 
-    let upleftIdx =vec2<i32>(min(idx.x + 1, i32(globals.width)-1), max(idx.y - 1, 0));
-    let downrightIdx = vec2<i32>(max(idx.x - 1, 0), min(idx.y + 1, i32(globals.height)-1));
-    let downleftIdx = vec2<i32>(max(idx.x - 1, 0), max(idx.y - 1, 0));
-    let uprightIdx = vec2<i32>(min(idx.x + 1, i32(globals.width)-1), min(idx.y + 1, i32(globals.height)-1));
+   // let upleftIdx =vec2<i32>(min(idx.x + 1, i32(globals.width)-1), max(idx.y - 1, 0));
+   // let downrightIdx = vec2<i32>(max(idx.x - 1, 0), min(idx.y + 1, i32(globals.height)-1));
+   // let downleftIdx = vec2<i32>(max(idx.x - 1, 0), max(idx.y - 1, 0));
+   // let uprightIdx = vec2<i32>(min(idx.x + 1, i32(globals.width)-1), min(idx.y + 1, i32(globals.height)-1));
    
     // eta, hu, hv, depth here
     let eta_here = textureLoad(txState, idx, 0).x;
     let u_here = textureLoad(txCW_uvhuhv, idx, 0).x;
-    let v_here = textureLoad(txCW_uvhuhv, idx, 0).y;
+   // let v_here = textureLoad(txCW_uvhuhv, idx, 0).y;
     let du_here = textureLoad(txCW_uvhuhv, idx, 0).z;
-    let dv_here = textureLoad(txCW_uvhuhv, idx, 0).w;
+   // let dv_here = textureLoad(txCW_uvhuhv, idx, 0).w;
     let d_here = -textureLoad(txBottom, idx, 0).z;
     let za_here = textureLoad(txCW_zalpha, idx, 0).x;
     let H_here = max(0.0, eta_here + d_here);
```

#### CT1-186 COULWAVE S와 T의 1D 환원

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3B_COULWAVE.wgsl:53; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3B_COULWAVE.wgsl:53; 아래 전체 diff의 +행 | 불일치 (F) | v=0과 y 미분=0이면 S=u_x, T=(du)_x다. dSdx와 dTdx에는 순수 x 2차 차분만 남는다. 제거한 4차 미분 대안은 본판에서도 주석이다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 175행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 139행 포함).

```diff
@@ -53,126 +53,90 @@
     // eta, hu, hv, depth right
     var all_vars = textureLoad(txCW_uvhuhv, rightIdx, 0);
     let u_ip1 = all_vars.x;
-    let v_ip1 = all_vars.y;
+   // let v_ip1 = all_vars.y;
     let du_ip1 = all_vars.z;
-    let dv_ip1 = all_vars.w;
+   // let dv_ip1 = all_vars.w;
 
     // eta, hu, hv, depth left
     all_vars = textureLoad(txCW_uvhuhv, leftIdx, 0);
     let u_im1 = all_vars.x;
-    let v_im1 = all_vars.y;
+   // let v_im1 = all_vars.y;
     let du_im1 = all_vars.z;
-    let dv_im1 = all_vars.w;
+   // let dv_im1 = all_vars.w;
 
     // eta, hu, hv, depth up
-    all_vars = textureLoad(txCW_uvhuhv, upIdx, 0);
-    let u_jp1 = all_vars.x;
-    let v_jp1 = all_vars.y;
-    let du_jp1 = all_vars.z;
-    let dv_jp1 = all_vars.w;
+   // all_vars = textureLoad(txCW_uvhuhv, upIdx, 0);
+   // let u_jp1 = all_vars.x;
+   // let v_jp1 = all_vars.y;
+   // let du_jp1 = all_vars.z;
+   // let dv_jp1 = all_vars.w;
 
     // eta, hu, hv, depth down
-    all_vars = textureLoad(txCW_uvhuhv, downIdx, 0);
-    let u_jm1 = all_vars.x;
-    let v_jm1 = all_vars.y;
-    let du_jm1 = all_vars.z;
-    let dv_jm1 = all_vars.w;
+   // all_vars = textureLoad(txCW_uvhuhv, downIdx, 0);
+   // let u_jm1 = all_vars.x;
+   // let v_jm1 = all_vars.y;
+   // let du_jm1 = all_vars.z;
+   // let dv_jm1 = all_vars.w;
 
     // hu, hv, up left
-    all_vars = textureLoad(txCW_uvhuhv, upleftIdx, 0);
-    let u_jp1_im1 = all_vars.x;
-    let v_jp1_im1 = all_vars.y;
-    let du_jp1_im1 = all_vars.z;
-    let dv_jp1_im1 = all_vars.w;
+   // all_vars = textureLoad(txCW_uvhuhv, upleftIdx, 0);
+   // let u_jp1_im1 = all_vars.x;
+   // let v_jp1_im1 = all_vars.y;
+   // let du_jp1_im1 = all_vars.z;
+   // let dv_jp1_im1 = all_vars.w;
 
     // hu, hv, up right
-    all_vars = textureLoad(txCW_uvhuhv, uprightIdx, 0);
-    let u_jp1_ip1 = all_vars.x;
-    let v_jp1_ip1 = all_vars.y;
-    let du_jp1_ip1 = all_vars.z;
-    let dv_jp1_ip1 = all_vars.w;
+   // all_vars = textureLoad(txCW_uvhuhv, uprightIdx, 0);
+   // let u_jp1_ip1 = all_vars.x;
+   // let v_jp1_ip1 = all_vars.y;
+   // let du_jp1_ip1 = all_vars.z;
+   // let dv_jp1_ip1 = all_vars.w;
 
     // hu, hv, down left
-    all_vars = textureLoad(txCW_uvhuhv, downleftIdx, 0);
-    let u_jm1_im1 = all_vars.x;
-    let v_jm1_im1 = all_vars.y;
-    let du_jm1_im1 = all_vars.z;
-    let dv_jm1_im1 = all_vars.w;
+   // all_vars = textureLoad(txCW_uvhuhv, downleftIdx, 0);
+   // let u_jm1_im1 = all_vars.x;
+   // let v_jm1_im1 = all_vars.y;
+   // let du_jm1_im1 = all_vars.z;
+   // let dv_jm1_im1 = all_vars.w;
 
     // hu, hv, down right
-    all_vars = textureLoad(txCW_uvhuhv, downrightIdx, 0);
-    let u_jm1_ip1 = all_vars.x;
-    let v_jm1_ip1 = all_vars.y;
-    let du_jm1_ip1 = all_vars.z;
-    let dv_jm1_ip1 = all_vars.w;
-
-    // // hu, hv right right  // comment this block if testing with 4th order derivatives
-    // all_vars = textureLoad(txCW_uvhuhv, rightrightIdx, 0);
-    // let u_ip2 = all_vars.x;
-    // let v_ip2 = all_vars.y;
-    // let du_ip2 = all_vars.z;
-    // let dv_ip2 = all_vars.w;
-
-    // // hu, hv left left
-    // all_vars = textureLoad(txCW_uvhuhv, leftleftIdx, 0);
-    // let u_im2 = all_vars.x;
-    // let v_im2 = all_vars.y;
-    // let du_im2 = all_vars.z;
-    // let dv_im2 = all_vars.w;
-
-    // // hu, hv up up
-    // all_vars = textureLoad(txCW_uvhuhv, upupIdx, 0);
-    // let u_jp2 = all_vars.x;
-    // let v_jp2 = all_vars.y;
-    // let du_jp2 = all_vars.z;
-    // let dv_jp2 = all_vars.w;
-
-    // // hu, hv down down
-    // all_vars = textureLoad(txCW_uvhuhv, downdownIdx, 0);
-    // let u_jm2 = all_vars.x;
-    // let v_jm2 = all_vars.y;
-    // let du_jm2 = all_vars.z;
-    // let dv_jm2 = all_vars.w;
+   // all_vars = textureLoad(txCW_uvhuhv, downrightIdx, 0);
+   // let u_jm1_ip1 = all_vars.x;
+   // let v_jm1_ip1 = all_vars.y;
+   // let du_jm1_ip1 = all_vars.z;
+   // let dv_jm1_ip1 = all_vars.w;
 
     // 2nd order derivatives
     let dudx =  0.5 * ( u_ip1 -  u_im1) * globals.one_over_dx;
     let dhudx = 0.5 * (du_ip1 - du_im1) * globals.one_over_dx;
-    let dudy =  0.5 * ( u_jp1 -  u_jm1) * globals.one_over_dy;
-    let dhudy = 0.5 * (du_jp1 - du_jm1) * globals.one_over_dy;
-    let dvdx =  0.5 * ( v_ip1 -  v_im1) * globals.one_over_dx;
-    let dhvdx = 0.5 * (dv_ip1 - dv_im1) * globals.one_over_dx;
-    let dvdy =  0.5 * ( v_jp1 -  v_jm1) * globals.one_over_dy;
-    let dhvdy = 0.5 * (dv_jp1 - dv_jm1) * globals.one_over_dy;
+   // let dudy =  0.5 * ( u_jp1 -  u_jm1) * globals.one_over_dy;
+   // let dhudy = 0.5 * (du_jp1 - du_jm1) * globals.one_over_dy;
+   // let dvdx =  0.5 * ( v_ip1 -  v_im1) * globals.one_over_dx;
+   // let dhvdx = 0.5 * (dv_ip1 - dv_im1) * globals.one_over_dx;
+   // let dvdy =  0.5 * ( v_jp1 -  v_jm1) * globals.one_over_dy;
+   // let dhvdy = 0.5 * (dv_jp1 - dv_jm1) * globals.one_over_dy;
     let d2udx2 =  ( u_ip1 - 2.0 *  u_here +  u_im1) * globals.one_over_d2x;
     let d2hudx2 = (du_ip1 - 2.0 * du_here + du_im1) * globals.one_over_d2x;
-    let d2vdy2 =  ( v_jp1 - 2.0 *  v_here +  v_jm1) * globals.one_over_d2y;
-    let d2hvdy2 = (dv_jp1 - 2.0 * dv_here + dv_jm1) * globals.one_over_d2y;
+   // let d2vdy2 =  ( v_jp1 - 2.0 *  v_here +  v_jm1) * globals.one_over_d2y;
+   // let d2hvdy2 = (dv_jp1 - 2.0 * dv_here + dv_jm1) * globals.one_over_d2y;
 
-    let d2udxdy = 0.25 *   ( u_jp1_ip1 -  u_jm1_ip1 -  u_jp1_im1 +  u_jm1_im1) * globals.one_over_dxdy;
-    let d2vdxdy = 0.25 *   ( v_jp1_ip1 -  v_jm1_ip1 -  v_jp1_im1 +  v_jm1_im1) * globals.one_over_dxdy;
-    let d2hudxdy = 0.25 *  (du_jp1_ip1 - du_jm1_ip1 - du_jp1_im1 + du_jm1_im1) * globals.one_over_dxdy;
-    let d2hvdxdy = 0.25 *  (dv_jp1_ip1 - dv_jm1_ip1 - dv_jp1_im1 + dv_jm1_im1) * globals.one_over_dxdy;
+   // let d2udxdy = 0.25 *   ( u_jp1_ip1 -  u_jm1_ip1 -  u_jp1_im1 +  u_jm1_im1) * globals.one_over_dxdy;
+   // let d2vdxdy = 0.25 *   ( v_jp1_ip1 -  v_jm1_ip1 -  v_jp1_im1 +  v_jm1_im1) * globals.one_over_dxdy;
+   // let d2hudxdy = 0.25 *  (du_jp1_ip1 - du_jm1_ip1 - du_jp1_im1 + du_jm1_im1) * globals.one_over_dxdy;
+   // let d2hvdxdy = 0.25 *  (dv_jp1_ip1 - dv_jm1_ip1 - dv_jp1_im1 + dv_jm1_im1) * globals.one_over_dxdy;
     
-    // 4th order derivatives
-    // let dudx = 1.0 / 12.0 *  ( u_ip2 - 8.0 *  u_ip1 + 8.0 *  u_im1 -  u_im2) * globals.one_over_dx;  
-    // let dhudx = 1.0 / 12.0 * (du_ip2 - 8.0 * du_ip1 + 8.0 * du_im1 - du_im2) * globals.one_over_dx;
-    // let dudy = 1.0 / 12.0 *  ( u_jp2 - 8.0 *  u_jp1 + 8.0 *  u_jm1 -  u_jm2) * globals.one_over_dy;
-    // let dhudy = 1.0 / 12.0 * (du_jp2 - 8.0 * du_jp1 + 8.0 * du_jm1 - du_jm2) * globals.one_over_dy;
-    // let dvdx = 1.0 / 12.0 *  ( v_ip2 - 8.0 *  v_ip1 + 8.0 *  v_im1 -  v_im2) * globals.one_over_dx;
-    // let dhvdx = 1.0 / 12.0 * (dv_ip2 - 8.0 * dv_ip1 + 8.0 * dv_im1 - dv_im2) * globals.one_over_dx;
-    // let dvdy = 1.0 / 12.0 *  ( v_jp2 - 8.0 *  v_jp1 + 8.0 *  v_jm1 -  v_jm2) * globals.one_over_dy;  
-    // let dhvdy = 1.0 / 12.0 * (dv_jp2 - 8.0 * dv_jp1 + 8.0 * dv_jm1 - dv_jm2) * globals.one_over_dy;
-    // let d2udx2 = 1.0 / 12.0 *   ( u_ip2 - 16.0 *  u_ip1 + 30.0 *  u_here - 16.0 *  u_im1 +  u_im2) * globals.one_over_d2x;
-    // let d2hudx2 = 1.0 / 12.0 *  (du_ip2 - 16.0 * du_ip1 + 30.0 * du_here - 16.0 * du_im1 + du_im2) * globals.one_over_d2x;
-    // let d2vdy2 = 1.0 / 12.0 *   ( v_jp2 - 16.0 *  v_jp1 + 30.0 *  v_here - 16.0 *  v_jm1 +  v_jm2) * globals.one_over_d2y;
-    // let d2hvdy2 = 1.0 / 12.0 *  (dv_jp2 - 16.0 * dv_jp1 + 30.0 * dv_here - 16.0 * dv_jm1 + dv_jm2) * globals.one_over_d2y;
-
-    let S = dudx + dvdy;
-    let T = dhudx + dhvdy;
-    let dSdx = d2udx2 + d2vdxdy;
-    let dSdy = d2udxdy + d2vdy2;
-    let dTdx = d2hudx2 + d2hvdxdy;
-    let dTdy = d2hudxdy + d2hvdy2;
+   // let S = dudx + dvdy;
+   // let T = dhudx + dhvdy;
+   // let dSdx = d2udx2 + d2vdxdy;
+   // let dSdy = d2udxdy + d2vdy2;
+   // let dTdx = d2hudx2 + d2hvdxdy;
+   // let dTdy = d2hudxdy + d2hvdy2;
+
+    let S = dudx;
+    let T = dhudx;
+    let dSdx = d2udx2;
+    let dTdx = d2hudx2;
+
 
     // E (eta) storage variaables
     let eta_2 = eta_here * eta_here;
```

#### CT1-187 COULWAVE E/F/G 패킹

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3B_COULWAVE.wgsl:185; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3B_COULWAVE.wgsl:149; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 E2·교차미분·y gradient·와도를 0으로 패킹한다. x 방향 uSx와 uTx 항은 보존한다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 199행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 168행 포함).

```diff
@@ -185,18 +149,23 @@
     let temp3 = 1.0 / 2.0 * (eta_here - d_here) - za_here;
 
     let E1 = H_here * (temp2 * dSdx + temp3 * dTdx);
-    let E2 = H_here * (temp2 * dSdy + temp3 * dTdy);
+   // let E2 = H_here * (temp2 * dSdy + temp3 * dTdy);
 
     // F, G (hu, hv) storage variables
     let E = textureLoad(dU_by_dt, idx, 0).x;
     let EzST = E * (eta_here * S + T);
     let TzS2 = eta_2 * S * S + 2.0 * eta_here * S * T + T * T;
-    let uSxvSy = 0.5 * (za_2 - eta_2) * (u_here * dSdx + v_here * dSdy);
-    let uTxvTy = (za_here - eta_here) * (u_here * dTdx + v_here * dTdy);
-
-    let ST_cross = vec4<f32>(S, T, d2udxdy, d2vdxdy);
-    let ST_grads = vec4<f32>(dSdx, dSdy, dTdx, dTdy);
-    let E_terms = vec4<f32>(E1, E2, E, dvdx - dudy);  
+   // let uSxvSy = 0.5 * (za_2 - eta_2) * (u_here * dSdx + v_here * dSdy);
+   // let uTxvTy = (za_here - eta_here) * (u_here * dTdx + v_here * dTdy);
+    let uSxvSy = 0.5 * (za_2 - eta_2) * (u_here * dSdx);
+    let uTxvTy = (za_here - eta_here) * (u_here * dTdx);
+
+   // let ST_cross = vec4<f32>(S, T, d2udxdy, d2vdxdy);
+    let ST_cross = vec4<f32>(S, T, 0.0, 0.0);
+   // let ST_grads = vec4<f32>(dSdx, dSdy, dTdx, dTdy);
+    let ST_grads = vec4<f32>(dSdx, 0.0, dTdx, 0.0);
+   // let E_terms = vec4<f32>(E1, E2, E, dvdx - dudy);  
+    let E_terms = vec4<f32>(E1, 0.0, E, 0.0); 
     let FG_terms = vec4<f32>(EzST, TzS2, uSxvSy, uTxvTy);
 
     textureStore(txCW_STval, idx, ST_cross);
```


### 2.32 shaders/Pass3_Bous.wgsl

본판: `shaders/Pass3_Bous.wgsl`. transect 판: `transect_version/shaders/Pass3_Bous.wgsl`.
원래 diff는 859행이다. CR 제외 diff는 10구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `35b7f1c` | 2026-01-15 | addition of vorticity-based momentum mixing |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-188 와도 소산 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_Bous.wgsl:35; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_Bous.wgsl:35; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 후속 와도 소산계수를 받는다. |

본판 차이 줄의 마지막 수정: `35b7f1c` 2026-01-15 (현재 38행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -35,7 +35,6 @@
     east_boundary_type: i32,
     south_boundary_type: i32,
     north_boundary_type: i32,
-    vort_friction_factor: f32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-189 Boussinesq x 경계와 스텐실

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_Bous.wgsl:96; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_Bous.wgsl:95; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 x 경계에서만 조기 반환한다. y·대각 스텐실과 미사용 F_G_star 쓰기를 생략한다. |

본판 차이 줄의 마지막 수정: `471c581` 2024-01-04 (현재 99행 포함); `63a12e3` 2023-10-19 (현재 115행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 115행 포함).

```diff
@@ -96,23 +95,24 @@
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
 
-    if (idx.x >= globals.width - 2 || idx.y >= globals.height - 2 || idx.x <= 1 || idx.y <= 1) {
+   // if (idx.x >= globals.width - 2 || idx.y >= globals.height - 2 || idx.x <= 1 || idx.y <= 1) {
+    if (idx.x >= globals.width - 2 || idx.x <= 1) {
         let zero = vec4<f32>(0.0, 0.0, 0.0, 0.0);
         textureStore(txNewState, idx, zero);
         textureStore(dU_by_dt, idx, zero);
-        textureStore(F_G_star, idx, zero);
+       // textureStore(F_G_star, idx, zero);
         textureStore(current_stateUVstar, idx, zero);
         return;
     }
 
     let leftIdx = idx + vec2<i32>(-1, 0);
     let rightIdx = idx + vec2<i32>(1, 0);
-    let downIdx = idx + vec2<i32>(0, -1);
-    let upIdx = idx + vec2<i32>(0, 1);
-    let upleftIdx = idx + vec2<i32>(-1, 1);
-    let uprightIdx = idx + vec2<i32>(1, 1);
-    let downleftIdx = idx + vec2<i32>(-1, -1);
-    let downrightIdx = idx + vec2<i32>(1, -1);
+   // let downIdx = idx + vec2<i32>(0, -1);
+   // let upIdx = idx + vec2<i32>(0, 1);
+   // let upleftIdx = idx + vec2<i32>(-1, 1);
+   // let uprightIdx = idx + vec2<i32>(1, 1);
+   // let downleftIdx = idx + vec2<i32>(-1, -1);
+   // let downrightIdx = idx + vec2<i32>(1, -1);
 
     let B_here = textureLoad(txBottom, idx, 0).z;
```

#### CT1-190 Boussinesq 건조 검사

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_Bous.wgsl:122; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_Bous.wgsl:122; 아래 전체 diff의 +행 | 불일치 (F) | 독립 단면은 동·서 이웃 수심만 검사한다. h_min은 동·서 채널만 채운다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 134행 포함); `ebc98a5` 2024-03-13 (현재 156행 포함); `7542e27` 2024-05-24 (현재 147행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 157행 포함).

```diff
@@ -122,38 +122,39 @@
     // Calculate local h,w
     let h_here = in_state_here.x - B_here;
 
-    let B_south = textureLoad(txBottom, downIdx, 0).z;
-    let B_north = textureLoad(txBottom, upIdx, 0).z;
+   // let B_south = textureLoad(txBottom, downIdx, 0).z;
+   // let B_north = textureLoad(txBottom, upIdx, 0).z;
     let B_west = textureLoad(txBottom, leftIdx, 0).z;
     let B_east = textureLoad(txBottom, rightIdx, 0).z;
 
     let eta_here = in_state_here.x;
     let eta_west = textureLoad(txState, leftIdx, 0).x;
     let eta_east = textureLoad(txState, rightIdx, 0).x;
-    let eta_south = textureLoad(txState, downIdx, 0).x;
-    let eta_north = textureLoad(txState, upIdx, 0).x;
+   // let eta_south = textureLoad(txState, downIdx, 0).x;
+   // let eta_north = textureLoad(txState, upIdx, 0).x;
 
     let h_west = eta_west - B_west;
     let h_east = eta_east - B_east;
-    let h_north = eta_north - B_north;
-    let h_south = eta_south - B_south;
+   // let h_north = eta_north - B_north;
+   // let h_south = eta_south - B_south;
 
     let h_cut = globals.delta;
     if (h_here <= h_cut) {  //if dry and surrounded by dry, then stay dry - no need to calc
-        if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
+       // if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
+        if(h_east <= h_cut && h_west <= h_cut) {
             let zero = vec4<f32>(0.0, 0.0, 0.0, 0.0);
             textureStore(txNewState, idx, zero);
             textureStore(dU_by_dt, idx, zero);
-            textureStore(F_G_star, idx, zero);
+           // textureStore(F_G_star, idx, zero);
             textureStore(current_stateUVstar, idx, zero);
             return; 
         }
     }
 
     var h_min = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    h_min.x= min(h_here, h_north);
+   // h_min.x= min(h_here, h_north);
     h_min.y= min(h_here, h_east);
-    h_min.z= min(h_here, h_south);
+   // h_min.z= min(h_here, h_south);
     h_min.w= min(h_here, h_west);
 
     var near_dry = textureLoad(txBottom, idx, 0).w;
```

#### CT1-191 Boussinesq flux와 수면 기울기

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_Bous.wgsl:161; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_Bous.wgsl:162; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 x flux와 detadx만 계산한다. |

본판 차이 줄의 마지막 수정: `366ee34` 2024-04-08 (현재 165행 포함); `63a12e3` 2023-10-19 (현재 168행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 169행 포함).

```diff
@@ -161,11 +162,11 @@
     // Load values from txXFlux and txYFlux using idx
     let xflux_here = textureLoad(txXFlux, idx, 0);
     let xflux_west = textureLoad(txXFlux, leftIdx, 0);
-    let yflux_here = textureLoad(txYFlux, idx, 0);
-    let yflux_south = textureLoad(txYFlux, downIdx, 0);
+   // let yflux_here = textureLoad(txYFlux, idx, 0);
+   // let yflux_south = textureLoad(txYFlux, downIdx, 0);
 
     var detadx = 0.5*(eta_east - eta_west) * globals.one_over_dx;
-    var detady = 0.5*(eta_north - eta_south) * globals.one_over_dy;
+   // var detady = 0.5*(eta_north - eta_south) * globals.one_over_dy;
 
     // previous derivatives
     let oldies = textureLoad(oldGradients, idx, 0);
```

#### CT1-192 주기 경계 분산 차단 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_Bous.wgsl:180; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_Bous.wgsl:181; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 periodic_bc_fix를 주석 처리한다. transect 경계 셰이더는 주기 경계 복사도 주석 처리한다. UI는 주기 경계에 별표를 붙인다. 이는 지원하지 않는 경로의 단면판 선택이다. |

본판 차이 줄의 마지막 수정: `38a5072` 2025-01-21 (현재 192행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 194행 포함).

```diff
@@ -180,16 +181,17 @@
     
     let d_here = -B_here;
     // periodic boundary condition fix for Boussinesq model
-    var periodic_bc_fix = -1;
-    if (globals.west_boundary_type == 3 && (idx.x >= globals.width - 3 || idx.x <= 2) ) {
-        periodic_bc_fix = 1;
-    } 
-
-    if (globals.south_boundary_type == 3 && (idx.y >= globals.height - 3 || idx.y <= 2) ){
-        periodic_bc_fix = 1;
-    } 
+   // var periodic_bc_fix = -1;
+   // if (globals.west_boundary_type == 3 && (idx.x >= globals.width - 3 || idx.x <= 2) ) {
+   //     periodic_bc_fix = 1;
+   // } 
+
+   // if (globals.south_boundary_type == 3 && (idx.y >= globals.height - 3 || idx.y <= 2) ){
+   //     periodic_bc_fix = 1;
+   // } 
 
-    if (near_dry > 0. && periodic_bc_fix < 0)
+   // if (near_dry > 0. && periodic_bc_fix < 0)
+    if (near_dry > 0. )
     { // only proceed if not near an initially dry cell
         let d2_here = d_here * d_here;
```

#### CT1-193 Boussinesq 분산식의 1D 환원

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_Bous.wgsl:197; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_Bous.wgsl:199; 아래 전체 diff의 +행 | 불일치 (F) | y 미분과 Q를 0으로 놓으면 F_star와 G_star가 0이다. Psi1x에는 d^3*eta_xxx만 남는다. Psi2x에는 2*Bcoef_g*d^2*d_x*eta_xx가 남는다. transect 판은 이 두 x 항을 계산한다. 본판의 와도 혼합은 1D 가정에서 0이다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 285행 포함); `471c581` 2024-01-04 (현재 286행 포함); `1b1e7a3` 2024-06-24 (현재 238행 포함); `38a5072` 2025-01-21 (현재 242행 포함); `cf9de63` 2023-10-24 (현재 280행 포함); `35b7f1c` 2026-01-15 (현재 301행 포함); `98f41c9` 2024-04-18 (현재 303행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 295행 포함).

```diff
@@ -197,110 +199,100 @@
     
         let leftleftIdx = idx + vec2<i32>(-2, 0);
         let rightrightIdx = idx + vec2<i32>(2, 0);
-        let downdownIdx = idx + vec2<i32>(0, -2);
-        let upupIdx = idx + vec2<i32>(0, 2);
+       // let downdownIdx = idx + vec2<i32>(0, -2);
+       // let upupIdx = idx + vec2<i32>(0, 2);
 
         let in_state_right = textureLoad(txState, rightIdx, 0).xyz;
         let in_state_left = textureLoad(txState, leftIdx, 0).xyz;
-        let in_state_up = textureLoad(txState, upIdx, 0).xyz;
-        let in_state_down = textureLoad(txState, downIdx, 0).xyz;
-        let in_state_up_left = textureLoad(txState, upleftIdx, 0).xyz;
-        let in_state_up_right = textureLoad(txState, uprightIdx, 0).xyz;
-        let in_state_down_left = textureLoad(txState, downleftIdx, 0).xyz;
-        let in_state_down_right = textureLoad(txState, downrightIdx, 0).xyz;
+       // let in_state_up = textureLoad(txState, upIdx, 0).xyz;
+       // let in_state_down = textureLoad(txState, downIdx, 0).xyz;
+       // let in_state_up_left = textureLoad(txState, upleftIdx, 0).xyz;
+       // let in_state_up_right = textureLoad(txState, uprightIdx, 0).xyz;
+       // let in_state_down_left = textureLoad(txState, downleftIdx, 0).xyz;
+       // let in_state_down_right = textureLoad(txState, downrightIdx, 0).xyz;
 
-        let F_G_star_oldOldies = textureLoad(F_G_star_oldOldGradients, idx, 0).xyz;
+       // let F_G_star_oldOldies = textureLoad(F_G_star_oldOldGradients, idx, 0).xyz;
 
     // Calculate d stencil
         let d_left = -B_west;
         let d_right = -B_east;
-        let d_down = -B_south;
-        let d_up = -B_north;
+       // let d_down = -B_south;
+       // let d_up = -B_north;
 
         let d_left_left = max(0.0, -textureLoad(txBottom, leftleftIdx, 0).z);
         let d_right_right = max(0.0, -textureLoad(txBottom, rightrightIdx, 0).z);
-        let d_down_down = max(0.0, -textureLoad(txBottom, downdownIdx, 0).z);
-        let d_up_up = max(0.0, -textureLoad(txBottom, upupIdx, 0).z);
+       // let d_down_down = max(0.0, -textureLoad(txBottom, downdownIdx, 0).z);
+       // let d_up_up = max(0.0, -textureLoad(txBottom, upupIdx, 0).z);
 
     // Calculate eta stencil
         let eta_here = in_state_here.x;
         let eta_left = in_state_left.x;
         let eta_right = in_state_right.x;
-        let eta_down = in_state_down.x;
-        let eta_up = in_state_up.x;
+       // let eta_down = in_state_down.x;
+       // let eta_up = in_state_up.x;
         let eta_left_left = textureLoad(txState, leftleftIdx, 0).x;
         let eta_right_right = textureLoad(txState, rightrightIdx, 0).x;
-        let eta_down_down = textureLoad(txState, downdownIdx, 0).x;
-        let eta_up_up = textureLoad(txState, upupIdx, 0).x;
-        let eta_up_left = in_state_up_left.x;
-        let eta_up_right = in_state_up_right.x;
-        let eta_down_left = in_state_down_left.x;
-        let eta_down_right = in_state_down_right.x;
+       // let eta_down_down = textureLoad(txState, downdownIdx, 0).x;
+       // let eta_up_up = textureLoad(txState, upupIdx, 0).x;
+       // let eta_up_left = in_state_up_left.x;
+       // let eta_up_right = in_state_up_right.x;
+       // let eta_down_left = in_state_down_left.x;
+       // let eta_down_right = in_state_down_right.x;
 
     // replace with 4th order when dispersion is included
         detadx = 1.0 / 12.0 * (eta_left_left - 8.0 * eta_left + 8.0 * eta_right - eta_right_right) * globals.one_over_dx;
-        detady = 1.0 / 12.0 * (eta_down_down - 8.0 * eta_down + 8.0 * eta_up - eta_up_up) * globals.one_over_dy;
+       // detady = 1.0 / 12.0 * (eta_down_down - 8.0 * eta_down + 8.0 * eta_up - eta_up_up) * globals.one_over_dy;
 
-        let v_up = in_state_up.z;
-        let v_down = in_state_down.z;
-        let v_right = in_state_right.z;
-        let v_left = in_state_left.z;
-        let v_up_right = in_state_up_right.z;
-        let v_down_right = in_state_down_right.z;
-        let v_up_left = in_state_up_left.z;
-        let v_down_left = in_state_down_left.z;
+       // let v_up = in_state_up.z;
+       // let v_down = in_state_down.z;
+       // let v_right = in_state_right.z;
+       // let v_left = in_state_left.z;
+       // let v_up_right = in_state_up_right.z;
+       // let v_down_right = in_state_down_right.z;
+       // let v_up_left = in_state_up_left.z;
+       // let v_down_left = in_state_down_left.z;
 
-        let u_up = in_state_up.y;
-        let u_down = in_state_down.y;
+       // let u_up = in_state_up.y;
+       // let u_down = in_state_down.y;
         let u_right = in_state_right.y;
         let u_left = in_state_left.y;
-        let u_up_right = in_state_up_right.y;
-        let u_down_right = in_state_down_right.y;
-        let u_up_left = in_state_up_left.y;
-        let u_down_left = in_state_down_left.y;
+       // let u_up_right = in_state_up_right.y;
+       // let u_down_right = in_state_down_right.y;
+       // let u_up_left = in_state_up_left.y;
+       // let u_down_left = in_state_down_left.y;
 
         let dd_by_dx = (-d_right_right + 8.0 * d_right - 8.0 * d_left + d_left_left) * globals.one_over_dx / 12.0;
-        let dd_by_dy = (-d_up_up + 8.0 * d_up - 8.0 * d_down + d_down_down) * globals.one_over_dy / 12.0;
-        let eta_by_dx_dy = 0.25 * globals.one_over_dx * globals.one_over_dy * (eta_up_right - eta_down_right - eta_up_left + eta_down_left);
+       // let dd_by_dy = (-d_up_up + 8.0 * d_up - 8.0 * d_down + d_down_down) * globals.one_over_dy / 12.0;
+       // let eta_by_dx_dy = 0.25 * globals.one_over_dx * globals.one_over_dy * (eta_up_right - eta_down_right - eta_up_left + eta_down_left);
         let eta_by_dx_dx = globals.one_over_d2x * (eta_right - 2.0 * eta_here + eta_left);
-        let eta_by_dy_dy = globals.one_over_d2y * (eta_up - 2.0 * eta_here + eta_down);
+       // let eta_by_dy_dy = globals.one_over_d2y * (eta_up - 2.0 * eta_here + eta_down);
         
 
-        F_star = (1.0 / 6.0) * d_here * 
-            (dd_by_dx * (0.5 * globals.one_over_dy) * (v_up - v_down) + 
-            dd_by_dy * (0.5 * globals.one_over_dx) * (v_right - v_left)) + 
-            (globals.Bcoef + 1.0 / 3.0) * d2_here * (globals.one_over_dxdy * 0.25) * 
-            (v_up_right- v_down_right - v_up_left + v_down_left);
-
-        G_star = (1.0 / 6.0) * d_here * 
-            (dd_by_dx * (0.5 * globals.one_over_dy) * (u_up - u_down) + 
-            dd_by_dy * (0.5 * globals.one_over_dx) * (u_right - u_left)) + 
-            (globals.Bcoef + 1.0 / 3.0) * d2_here * (globals.one_over_dxdy * 0.25) * 
-            (u_up_right - u_down_right - u_up_left + u_down_left);
-
+       // F_star = (1.0 / 6.0) * d_here * 
+       //     (dd_by_dx * (0.5 * globals.one_over_dy) * (v_up - v_down) + 
+       //     dd_by_dy * (0.5 * globals.one_over_dx) * (v_right - v_left)) + 
+       //     (globals.Bcoef + 1.0 / 3.0) * d2_here * (globals.one_over_dxdy * 0.25) * 
+       //     (v_up_right- v_down_right - v_up_left + v_down_left);
+
+       // G_star = (1.0 / 6.0) * d_here * 
+       //     (dd_by_dx * (0.5 * globals.one_over_dy) * (u_up - u_down) + 
+       //     dd_by_dy * (0.5 * globals.one_over_dx) * (u_right - u_left)) + 
+       //     (globals.Bcoef + 1.0 / 3.0) * d2_here * (globals.one_over_dxdy * 0.25) * 
+       //     (u_up_right - u_down_right - u_up_left + u_down_left);
         
-        Psi1x = globals.Bcoef_g * d3_here * ((eta_right_right - 2.0 * eta_right + 2.0 * eta_left - eta_left_left) * (0.5 * globals.one_over_d3x) + (eta_up_right - eta_up_left - 2.0 * eta_right + 2.0 * eta_left + eta_down_right - eta_down_left) * (0.5 * globals.one_over_dx * globals.one_over_d2y));
-        Psi2x = globals.Bcoef_g * d2_here * (dd_by_dx * (2.0 * eta_by_dx_dx + eta_by_dy_dy) + dd_by_dy * eta_by_dx_dy) + (F_star - F_G_star_oldOldies.y) / globals.dt * 0.5;
+       // Psi1x = globals.Bcoef_g * d3_here * ((eta_right_right - 2.0 * eta_right + 2.0 * eta_left - eta_left_left) * (0.5 * globals.one_over_d3x) + (eta_up_right - eta_up_left - 2.0 * eta_right + 2.0 * eta_left + eta_down_right - eta_down_left) * (0.5 * globals.one_over_dx * globals.one_over_d2y));
+       // Psi2x = globals.Bcoef_g * d2_here * (dd_by_dx * (2.0 * eta_by_dx_dx + eta_by_dy_dy) + dd_by_dy * eta_by_dx_dy) + (F_star - F_G_star_oldOldies.y) / globals.dt * 0.5;
+
+        Psi1x = globals.Bcoef_g * d3_here * ((eta_right_right - 2.0 * eta_right + 2.0 * eta_left - eta_left_left) * (0.5 * globals.one_over_d3x));
+        Psi2x = globals.Bcoef_g * d2_here * (dd_by_dx * (2.0 * eta_by_dx_dx));
 
-        Psi1y = globals.Bcoef_g * d3_here * ((eta_up_up - 2.0 * eta_up + 2.0 * eta_down - eta_down_down) * (0.5 * globals.one_over_d3y) + (eta_up_right + eta_up_left - 2.0 * eta_up + 2.0 * eta_down - eta_down_right - eta_down_left) * (0.5 * globals.one_over_dx * globals.one_over_d2x));
-        Psi2y = globals.Bcoef_g * d2_here * (dd_by_dy * (2.0 * eta_by_dy_dy + eta_by_dx_dx) + dd_by_dx * eta_by_dx_dy) + (G_star - F_G_star_oldOldies.z) / globals.dt * 0.5;
+       // Psi1y = globals.Bcoef_g * d3_here * ((eta_up_up - 2.0 * eta_up + 2.0 * eta_down - eta_down_down) * (0.5 * globals.one_over_d3y) + (eta_up_right + eta_up_left - 2.0 * eta_up + 2.0 * eta_down - eta_down_right - eta_down_left) * (0.5 * globals.one_over_dx * globals.one_over_d2x));
+       // Psi2y = globals.Bcoef_g * d2_here * (dd_by_dy * (2.0 * eta_by_dy_dy + eta_by_dx_dx) + dd_by_dx * eta_by_dx_dy) + (G_star - F_G_star_oldOldies.z) / globals.dt * 0.5;
     }
    
-    // vorticity-based momentum mixing / dissipation
-    var vorticity_dissipation = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    if (globals.vort_friction_factor > 0.0) {
-        let dPdxy = 0.25 * (textureLoad(txState, uprightIdx, 0).y - textureLoad(txState, upleftIdx, 0).y - textureLoad(txState, downrightIdx, 0).y + textureLoad(txState, downleftIdx, 0).y) * globals.one_over_dxdy;
-        let dPdyy = (textureLoad(txState, upIdx, 0).y - 2.0 * in_state_here.y + textureLoad(txState, downIdx, 0).y) * globals.one_over_d2y;
-        let dQdxx = (textureLoad(txState, rightIdx, 0).z - 2.0 * in_state_here.z + textureLoad(txState, leftIdx, 0).z) * globals.one_over_d2x;
-        let dQdxy = 0.25 * (textureLoad(txState, uprightIdx, 0).z - textureLoad(txState, upleftIdx, 0).z - textureLoad(txState, downrightIdx, 0).z + textureLoad(txState, downleftIdx, 0).z) * globals.one_over_dxdy;
-        let domegady = dPdyy - dQdxy;
-        let domegadx = dPdxy - dQdxx;
-        vorticity_dissipation.y = globals.vort_friction_factor  * domegady;
-        vorticity_dissipation.z = -globals.vort_friction_factor  * domegadx;
-    }
-
     let friction_here = max(globals.friction, textureLoad(txBottomFriction, idx, 0).x);
-    var friction_ = FrictionCalc(in_state_here.y, in_state_here.z, h_here, friction_here);
+   // var friction_ = FrictionCalc(in_state_here.y, in_state_here.z, h_here, friction_here);
+    var friction_ = FrictionCalc(in_state_here.y, 0.0, h_here, friction_here);
 
     // dhdt for depth change option
     let dhdt = textureLoad(txBoundaryForcing, idx, 0).y;
```

#### CT1-194 압력과 백수 source

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_Bous.wgsl:308; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_Bous.wgsl:300; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 x 압력과 Dxx 확산만 남긴다. c_dissipation 식은 같다. |

본판 차이 줄의 마지막 수정: `18fa7ab` 2025-04-11 (현재 312행 포함); `63a12e3` 2023-10-19 (현재 333행 포함); `366ee34` 2024-04-08 (현재 340행 포함); `2eb2866` 2023-10-26 (현재 334행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 332행 포함).

```diff
@@ -308,36 +300,36 @@
     // Pressure stencil calculations
     let P_left = textureLoad(txBoundaryForcing, leftIdx, 0).x;
     let P_right = textureLoad(txBoundaryForcing, rightIdx, 0).x;
-    let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;
-    let P_up = textureLoad(txBoundaryForcing, upIdx, 0).x;
+   // let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;
+   // let P_up = textureLoad(txBoundaryForcing, upIdx, 0).x;
 
     let press_x = -0.5 * h_here * globals.g_over_dx * (P_right - P_left);
-    let press_y = -0.5 * h_here * globals.g_over_dy * (P_up - P_down);
+   // let press_y = -0.5 * h_here * globals.g_over_dy * (P_up - P_down);
 
     // Calculate scalar transport additions
     let C_state_here = textureLoad(txState, idx, 0).w;
     let C_state_right = textureLoad(txState, rightIdx, 0).w;
     let C_state_left = textureLoad(txState, leftIdx, 0).w;
-    let C_state_up = textureLoad(txState, upIdx, 0).w;
-    let C_state_down = textureLoad(txState, downIdx, 0).w;
-    let C_state_up_left = textureLoad(txState, upleftIdx, 0).w;
-    let C_state_up_right = textureLoad(txState, uprightIdx, 0).w;
-    let C_state_down_left = textureLoad(txState, downleftIdx, 0).w;
-    let C_state_down_right = textureLoad(txState, downrightIdx, 0).w;
+   // let C_state_up = textureLoad(txState, upIdx, 0).w;
+   // let C_state_down = textureLoad(txState, downIdx, 0).w;
+   // let C_state_up_left = textureLoad(txState, upleftIdx, 0).w;
+   // let C_state_up_right = textureLoad(txState, uprightIdx, 0).w;
+   // let C_state_down_left = textureLoad(txState, downleftIdx, 0).w;
+   // let C_state_down_right = textureLoad(txState, downrightIdx, 0).w;
 
     let Dxx = globals.whiteWaterDispersion;
-    let Dxy = globals.whiteWaterDispersion;
-    let Dyy = globals.whiteWaterDispersion;
+   // let Dxy = globals.whiteWaterDispersion;
+   // let Dyy = globals.whiteWaterDispersion;
 
     let hc_by_dx_dx = Dxx * globals.one_over_d2x * (C_state_right - 2.0 * in_state_here.a + C_state_left);
-    let hc_by_dy_dy = Dyy * globals.one_over_d2y * (C_state_up - 2.0 * in_state_here.a + C_state_down);
-    let hc_by_dx_dy = 0.25 * Dxy * globals.one_over_dxdy * (C_state_up_right - C_state_up_left - C_state_down_right + C_state_down_left);
+   // let hc_by_dy_dy = Dyy * globals.one_over_d2y * (C_state_up - 2.0 * in_state_here.a + C_state_down);
+   // let hc_by_dx_dy = 0.25 * Dxy * globals.one_over_dxdy * (C_state_up_right - C_state_up_left - C_state_down_right + C_state_down_left);
 
     let c_dissipation = -globals.whiteWaterDecayRate * C_state_here;
 
     // calculate breaking dissipation
     var breaking_x = 0.0;
-    var breaking_y = 0.0;
+   // var breaking_y = 0.0;
     var breaking_B = 0.0;
     
     if(globals.useBreakingModel == 1) {
```

#### CT1-195 쇄파 확산과 해안선 처리

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_Bous.wgsl:346; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_Bous.wgsl:338; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 breaking_x=dPdxx로 둔다. y 응력과 y 기울기 보정을 생략한다. y 미분=0과 Q=0에서 본판 식이 이 형태가 된다. |

본판 차이 줄의 마지막 수정: `366ee34` 2024-04-08 (현재 362행 포함); `ebc98a5` 2024-03-13 (현재 375행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 368행 포함).

```diff
@@ -346,33 +338,34 @@
         let nu_flux_here = textureLoad(txDissipationFlux, idx, 0);
         let nu_flux_right = textureLoad(txDissipationFlux, rightIdx, 0);
         let nu_flux_left = textureLoad(txDissipationFlux, leftIdx, 0);
-        let nu_flux_up = textureLoad(txDissipationFlux, upIdx, 0);
-        let nu_flux_down = textureLoad(txDissipationFlux, downIdx, 0);
+       // let nu_flux_up = textureLoad(txDissipationFlux, upIdx, 0);
+       // let nu_flux_down = textureLoad(txDissipationFlux, downIdx, 0);
 
         let dPdxx = 0.5 * (nu_flux_right.x - nu_flux_left.x) * globals.one_over_dx;
-        let dPdyx = 0.5 * (nu_flux_right.y - nu_flux_left.y) * globals.one_over_dx;
-        let dPdyy = 0.5 * (nu_flux_up.y - nu_flux_down.y) * globals.one_over_dy;
+       // let dPdyx = 0.5 * (nu_flux_right.y - nu_flux_left.y) * globals.one_over_dx;
+       // let dPdyy = 0.5 * (nu_flux_up.y - nu_flux_down.y) * globals.one_over_dy;
 
-        let dQdxx = 0.5 * (nu_flux_right.z - nu_flux_left.z) * globals.one_over_dx;
-        let dQdxy = 0.5 * (nu_flux_up.z - nu_flux_down.z) * globals.one_over_dy;
-        let dQdyy = 0.5 * (nu_flux_up.w - nu_flux_down.w) * globals.one_over_dy;
+       // let dQdxx = 0.5 * (nu_flux_right.z - nu_flux_left.z) * globals.one_over_dx;
+       // let dQdxy = 0.5 * (nu_flux_up.z - nu_flux_down.z) * globals.one_over_dy;
+       // let dQdyy = 0.5 * (nu_flux_up.w - nu_flux_down.w) * globals.one_over_dy;
         
         if (near_dry > 0.){
-            breaking_x = dPdxx + 0.5 * dPdyy + 0.5 * dQdxy;
-            breaking_y = dQdyy + 0.5 * dPdyx + 0.5 * dQdxx;
+           // breaking_x = dPdxx + 0.5 * dPdyy + 0.5 * dQdxy;
+            breaking_x = dPdxx;
+           // breaking_y = dQdyy + 0.5 * dPdyx + 0.5 * dQdxx;
         }
     }
     
     // fix slope near shoreline
-    if (h_min.x <= h_cut && h_min.z <= h_cut) {
-        detady = 0.0;
-    }
-    else if (h_min.x <= h_cut) {  //north
-        detady = 1.*(eta_here - eta_south) * globals.one_over_dy;
-    }
-    else if (h_min.z <= h_cut) {  //south
-        detady = 1.*(eta_north - eta_here) * globals.one_over_dy;
-    }
+   // if (h_min.x <= h_cut && h_min.z <= h_cut) {
+   //     detady = 0.0;
+   // }
+   // else if (h_min.x <= h_cut) {  //north
+   //     detady = 1.*(eta_here - eta_south) * globals.one_over_dy;
+   // }
+   // else if (h_min.z <= h_cut) {  //south
+   //     detady = 1.*(eta_north - eta_here) * globals.one_over_dy;
+   // }
 
     if (h_min.y <= h_cut && h_min.w <= h_cut) {
         detadx = 0.0;
```

#### CT1-196 계산한 Psi2x의 source 누락

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_Bous.wgsl:389; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_Bous.wgsl:382; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 Psi2x를 계산하지만 source_term에는 Psi1x만 더한다. 바로 위 주석과 본판 source는 Psi1x+Psi2x를 더한다. Psi2x의 지형 경사 항은 1D에서 사라지지 않는다. 의도 변경 근거와 보정 경로를 확인한 뒤 강함으로 둔다. |

본판 차이 줄의 마지막 수정: `18fa7ab` 2025-04-11 (현재 392행 포함); `35b7f1c` 2026-01-15 (현재 394행 포함); `cf9de63` 2023-10-24 (현재 397행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 393행 포함).

```diff
@@ -389,12 +382,15 @@
         overflow_dry = -globals.infiltrationRate;  // hydraulic conductivity of coarse, unsaturated sand
     }
 
-    let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + breaking_y + (Psi1y + Psi2y) + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);
+   // let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + breaking_y + (Psi1y + Psi2y) + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);
+    let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x) + press_x, 0.0, hc_by_dx_dx + c_dissipation);
 
-    let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term + vorticity_dissipation;
+   // let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term;
+    let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + source_term;
 
     var newState = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    let F_G_here = vec4<f32>(0.0, F_star, G_star, 0.0);
+   // let F_G_here = vec4<f32>(0.0, F_star, G_star, 0.0);
+    let F_G_here = vec4<f32>(0.0, 0.0, 0.0, 0.0);
 
     if (globals.timeScheme == 0) {
         newState = in_state_here_UV + globals.dt * d_by_dt;
```

#### CT1-197 분산 교차 이력 쓰기 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_Bous.wgsl:425; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_Bous.wgsl:421; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 1D에서 0인 F_G_star 출력 쓰기를 생략한다. |

본판 차이 줄의 마지막 수정: `cf9de63` 2023-10-24 (현재 428행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 424행 포함).

```diff
@@ -425,6 +421,6 @@
 
     textureStore(txNewState, idx, newState);
     textureStore(dU_by_dt, idx, d_by_dt);
-    textureStore(F_G_star, idx, F_G_here);
+   // textureStore(F_G_star, idx, F_G_here);
     textureStore(current_stateUVstar, idx, newState);
 }
```


### 2.33 shaders/Pass3_COULWAVE.wgsl

본판: `shaders/Pass3_COULWAVE.wgsl`. transect 판: `transect_version/shaders/Pass3_COULWAVE.wgsl`.
원래 diff는 572행이다. CR 제외 diff는 12구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `35b7f1c` | 2026-01-15 | addition of vorticity-based momentum mixing |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-198 COULWAVE 와도 소산계수

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:35; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:35; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 후속 vort_friction_factor uniform을 받는다. |

본판 차이 줄의 마지막 수정: `35b7f1c` 2026-01-15 (현재 38행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -35,7 +35,6 @@
     east_boundary_type: i32,
     south_boundary_type: i32,
     north_boundary_type: i32,
-    vort_friction_factor: f32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-199 COULWAVE x 경계와 이웃

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:96; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:95; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 y 경계와 y 이웃 계산을 생략한다. |

본판 차이 줄의 마지막 수정: `0b4e990` 2025-05-16 (현재 103행 포함); `67ca57c` 2025-05-22 (현재 119행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 119행 포함).

```diff
@@ -96,27 +95,28 @@
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
 
-    if (idx.x >= globals.width - 2 || idx.y >= globals.height - 2 || idx.x <= 1 || idx.y <= 1) {
+   // if (idx.x >= globals.width - 2 || idx.y >= globals.height - 2 || idx.x <= 1 || idx.y <= 1) {
+    if (idx.x >= globals.width - 2 || idx.x <= 1) {
         let zero = vec4<f32>(0.0, 0.0, 0.0, 0.0);
         textureStore(txNewState, idx, zero);
         textureStore(dU_by_dt, idx, zero);
-        textureStore(F_G_star, idx, zero);
+       // textureStore(F_G_star, idx, zero);
         textureStore(current_stateUVstar, idx, zero);
         return;
     }
     let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));
-    let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
+   // let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));
     let rightrightIdx = min(idx + vec2<i32>(2, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
-    let upupIdx = min(idx + vec2<i32>(0, 2), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
+   // let upupIdx = min(idx + vec2<i32>(0, 2), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));
     let leftleftIdx = max(idx + vec2<i32>(-2, 0), vec2<i32>(0, 0));
-    let downdownIdx = max(idx + vec2<i32>(0, -2), vec2<i32>(0, 0));
+   // let downdownIdx = max(idx + vec2<i32>(0, -2), vec2<i32>(0, 0));
 
-    let upleftIdx =vec2<i32>(min(idx.x + 1, i32(globals.width)-1), max(idx.y - 1, 0));
-    let downrightIdx = vec2<i32>(max(idx.x - 1, 0), min(idx.y + 1, i32(globals.height)-1));
-    let downleftIdx = vec2<i32>(max(idx.x - 1, 0), max(idx.y - 1, 0));
-    let uprightIdx = vec2<i32>(min(idx.x + 1, i32(globals.width)-1), min(idx.y + 1, i32(globals.height)-1));
+   // let upleftIdx =vec2<i32>(min(idx.x + 1, i32(globals.width)-1), max(idx.y - 1, 0));
+   // let downrightIdx = vec2<i32>(max(idx.x - 1, 0), min(idx.y + 1, i32(globals.height)-1));
+   // let downleftIdx = vec2<i32>(max(idx.x - 1, 0), max(idx.y - 1, 0));
+   // let uprightIdx = vec2<i32>(min(idx.x + 1, i32(globals.width)-1), min(idx.y + 1, i32(globals.height)-1));
    
     let B_here = textureLoad(txBottom, idx, 0).z;
```

#### CT1-200 COULWAVE 건조 검사

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:126; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:126; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 동·서 이웃만 검사한다. 건조 반환은 바닥고와 영 운동량을 유지한다. |

본판 차이 줄의 마지막 수정: `0b4e990` 2025-05-16 (현재 160행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 161행 포함).

```diff
@@ -126,38 +126,39 @@
     // Calculate local h,w
     let h_here = max(0.0, in_state_here.x - B_here);
 
-    let B_south = textureLoad(txBottom, downIdx, 0).z;
-    let B_north = textureLoad(txBottom, upIdx, 0).z;
+   // let B_south = textureLoad(txBottom, downIdx, 0).z;
+   // let B_north = textureLoad(txBottom, upIdx, 0).z;
     let B_west = textureLoad(txBottom, leftIdx, 0).z;
     let B_east = textureLoad(txBottom, rightIdx, 0).z;
 
     let eta_here = in_state_here.x;
     let eta_west = textureLoad(txState, leftIdx, 0).x;
     let eta_east = textureLoad(txState, rightIdx, 0).x;
-    let eta_south = textureLoad(txState, downIdx, 0).x;
-    let eta_north = textureLoad(txState, upIdx, 0).x;
+   // let eta_south = textureLoad(txState, downIdx, 0).x;
+   // let eta_north = textureLoad(txState, upIdx, 0).x;
 
     let h_west = eta_west - B_west;
     let h_east = eta_east - B_east;
-    let h_north = eta_north - B_north;
-    let h_south = eta_south - B_south;
+   // let h_north = eta_north - B_north;
+   // let h_south = eta_south - B_south;
 
     let h_cut = globals.delta;
     if (h_here <= h_cut) {  //if dry and surrounded by dry, then stay dry - no need to calc
-        if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
+       // if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
+        if(h_east <= h_cut && h_west <= h_cut) {
             let zero = vec4<f32>(0.0, 0.0, 0.0, 0.0);
             textureStore(txNewState, idx, vec4<f32>(B_here, 0.0, 0.0, 0.0));
             textureStore(dU_by_dt, idx, zero);
-            textureStore(F_G_star, idx, zero);
+           // textureStore(F_G_star, idx, zero);
             textureStore(current_stateUVstar, idx, vec4<f32>(B_here, 0.0, 0.0, 0.0));
             return; 
         }
     }
 
     var h_min = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    h_min.x= min(h_here, h_north);
+   // h_min.x= min(h_here, h_north);
     h_min.y= min(h_here, h_east);
-    h_min.z= min(h_here, h_south);
+   // h_min.z= min(h_here, h_south);
     h_min.w= min(h_here, h_west);
 
     var near_dry = textureLoad(txBottom, idx, 0).w;
```

#### CT1-201 COULWAVE flux와 기울기

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:165; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:166; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 x flux와 x 수면 기울기만 사용한다. |

본판 차이 줄의 마지막 수정: `0b4e990` 2025-05-16 (현재 172행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 173행 포함).

```diff
@@ -165,11 +166,11 @@
     // Load values from txXFlux and txYFlux using idx
     let xflux_here = textureLoad(txXFlux, idx, 0);
     let xflux_west = textureLoad(txXFlux, leftIdx, 0);
-    let yflux_here = textureLoad(txYFlux, idx, 0);
-    let yflux_south = textureLoad(txYFlux, downIdx, 0);
+   // let yflux_here = textureLoad(txYFlux, idx, 0);
+   // let yflux_south = textureLoad(txYFlux, downIdx, 0);
 
     var detadx = 0.5*(eta_east - eta_west) * globals.one_over_dx;
-    var detady = 0.5*(eta_north - eta_south) * globals.one_over_dy;
+   // var detady = 0.5*(eta_north - eta_south) * globals.one_over_dy;
 
     // previous derivatives
     let oldies = textureLoad(oldGradients, idx, 0);
```

#### CT1-202 COULWAVE 주기 경계 분산 차단 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:185; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:186; 아래 전체 diff의 +행 | 코드에만 (C) | 주기 경계를 구현하지 않는 단면판은 해당 분산 차단도 주석 처리한다. x 수면의 4차 차분은 유지한다. |

본판 차이 줄의 마지막 수정: `0b4e990` 2025-05-16 (현재 223행 포함); `67ca57c` 2025-05-22 (현재 227행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 229행 포함).

```diff
@@ -185,46 +186,47 @@
     
     let d_here = -B_here;
     // periodic boundary condition fix for Boussinesq model
-    var periodic_bc_fix = -1;
-    if (globals.west_boundary_type == 3 && (idx.x >= globals.width - 3 || idx.x <= 2) ) {
-        periodic_bc_fix = 1;
-    } 
-
-    if (globals.south_boundary_type == 3 && (idx.y >= globals.height - 3 || idx.y <= 2) ){
-        periodic_bc_fix = 1;
-    } 
+   // var periodic_bc_fix = -1;
+   // if (globals.west_boundary_type == 3 && (idx.x >= globals.width - 3 || idx.x <= 2) ) {
+   //     periodic_bc_fix = 1;
+   // } 
+
+   // if (globals.south_boundary_type == 3 && (idx.y >= globals.height - 3 || idx.y <= 2) ){
+   //     periodic_bc_fix = 1;
+   // } 
 
-    if (near_dry > 0. && periodic_bc_fix < 0) 
+   // if (near_dry > 0. && periodic_bc_fix < 0) 
+    if (near_dry > 0.) 
     { // only proceed if not near an initially dry cell
        
         let in_state_right = textureLoad(txState, rightIdx, 0).xyz;
         let in_state_left = textureLoad(txState, leftIdx, 0).xyz;
-        let in_state_up = textureLoad(txState, upIdx, 0).xyz;
-        let in_state_down = textureLoad(txState, downIdx, 0).xyz;
-        let in_state_up_left = textureLoad(txState, upleftIdx, 0).xyz;
-        let in_state_up_right = textureLoad(txState, uprightIdx, 0).xyz;
-        let in_state_down_left = textureLoad(txState, downleftIdx, 0).xyz;
-        let in_state_down_right = textureLoad(txState, downrightIdx, 0).xyz;
+       // let in_state_up = textureLoad(txState, upIdx, 0).xyz;
+       // let in_state_down = textureLoad(txState, downIdx, 0).xyz;
+       // let in_state_up_left = textureLoad(txState, upleftIdx, 0).xyz;
+       // let in_state_up_right = textureLoad(txState, uprightIdx, 0).xyz;
+       // let in_state_down_left = textureLoad(txState, downleftIdx, 0).xyz;
+       // let in_state_down_right = textureLoad(txState, downrightIdx, 0).xyz;
 
-        let F_G_star_oldies = textureLoad(F_G_star_oldGradients, idx, 0).xyz;
-        let F_G_star_oldOldies = textureLoad(F_G_star_oldOldGradients, idx, 0).xyz;
+       // let F_G_star_oldies = textureLoad(F_G_star_oldGradients, idx, 0).xyz;
+       // let F_G_star_oldOldies = textureLoad(F_G_star_oldOldGradients, idx, 0).xyz;
         
         let eta_left = in_state_left.x;
         let eta_right = in_state_right.x;
-        let eta_down = in_state_down.x;
-        let eta_up = in_state_up.x;
+       // let eta_down = in_state_down.x;
+       // let eta_up = in_state_up.x;
 
         let eta_left_left = textureLoad(txState, leftleftIdx, 0).x;
         let eta_right_right = textureLoad(txState, rightrightIdx, 0).x;
-        let eta_down_down = textureLoad(txState, downdownIdx, 0).x;
-        let eta_up_up = textureLoad(txState, upupIdx, 0).x;
+       // let eta_down_down = textureLoad(txState, downdownIdx, 0).x;
+       // let eta_up_up = textureLoad(txState, upupIdx, 0).x;
 
         detadx = 1.0 / 12.0 * (eta_left_left - 8.0 * eta_left + 8.0 * eta_right - eta_right_right) * globals.one_over_dx;
-        detady = 1.0 / 12.0 * (eta_down_down - 8.0 * eta_down + 8.0 * eta_up - eta_up_up) * globals.one_over_dy;
+       // detady = 1.0 / 12.0 * (eta_down_down - 8.0 * eta_down + 8.0 * eta_up - eta_up_up) * globals.one_over_dy;
 
         // 2nd order derivatives for inside HO terms
         let detadx_loworder = 0.5 * (eta_right - eta_left) * globals.one_over_dx;
-        let detady_loworder = 0.5 * (eta_up - eta_down) * globals.one_over_dy;
+       // let detady_loworder = 0.5 * (eta_up - eta_down) * globals.one_over_dy;
 
         // level 0: txModelVelocities, [u, v, eta, h]
         // level 1: txCW_zalpha, [za, dzadx, dzady, 0.0)]
```

#### CT1-203 COULWAVE grouping 읽기의 1D 환원

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:236; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:238; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 v·dv·혼합미분·za_y를 읽지 않는다. 레이어 번호와 x 자료의 채널은 유지한다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 275행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 277행 포함).

```diff
@@ -236,43 +238,43 @@
         // Coulwave terms fetch
         var level = 0;
         let u_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).x;
-        let v_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).y;
+       // let v_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).y;
         let u_ip1 = textureLoad(txCW_groupings, vec3<i32>(rightIdx.x, rightIdx.y, level), 0).x;
         let u_im1 = textureLoad(txCW_groupings, vec3<i32>(leftIdx.x, leftIdx.y, level), 0).x;
-        let v_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).y;
-        let v_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).y;
+       // let v_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).y;
+       // let v_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).y;
 
-        let u_ip1_jp1 = textureLoad(txCW_groupings, vec3<i32>(uprightIdx.x, uprightIdx.y, level), 0).x;
-        let u_ip1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downrightIdx.x, downrightIdx.y, level), 0).x;
-        let u_im1_jp1 = textureLoad(txCW_groupings, vec3<i32>(upleftIdx.x, upleftIdx.y, level), 0).x;
-        let u_im1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downleftIdx.x, downleftIdx.y, level), 0).x;
-
-        let v_ip1_jp1 = textureLoad(txCW_groupings, vec3<i32>(uprightIdx.x, uprightIdx.y, level), 0).y;
-        let v_ip1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downrightIdx.x, downrightIdx.y, level), 0).y;
-        let v_im1_jp1 = textureLoad(txCW_groupings, vec3<i32>(upleftIdx.x, upleftIdx.y, level), 0).y;
-        let v_im1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downleftIdx.x, downleftIdx.y, level), 0).y;
+       // let u_ip1_jp1 = textureLoad(txCW_groupings, vec3<i32>(uprightIdx.x, uprightIdx.y, level), 0).x;
+       // let u_ip1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downrightIdx.x, downrightIdx.y, level), 0).x;
+       // let u_im1_jp1 = textureLoad(txCW_groupings, vec3<i32>(upleftIdx.x, upleftIdx.y, level), 0).x;
+       // let u_im1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downleftIdx.x, downleftIdx.y, level), 0).x;
+
+       // let v_ip1_jp1 = textureLoad(txCW_groupings, vec3<i32>(uprightIdx.x, uprightIdx.y, level), 0).y;
+       // let v_ip1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downrightIdx.x, downrightIdx.y, level), 0).y;
+       // let v_im1_jp1 = textureLoad(txCW_groupings, vec3<i32>(upleftIdx.x, upleftIdx.y, level), 0).y;
+       // let v_im1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downleftIdx.x, downleftIdx.y, level), 0).y;
         
         let du_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).z;
-        let dv_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).w;
+       // let dv_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).w;
         let du_ip1 = textureLoad(txCW_groupings, vec3<i32>(rightIdx.x, rightIdx.y, level), 0).z;
         let du_im1 = textureLoad(txCW_groupings, vec3<i32>(leftIdx.x, leftIdx.y, level), 0).z;
-        let dv_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).w;
-        let dv_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).w;
+       // let dv_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).w;
+       // let dv_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).w;
 
-        let du_ip1_jp1 = textureLoad(txCW_groupings, vec3<i32>(uprightIdx.x, uprightIdx.y, level), 0).z;
-        let du_ip1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downrightIdx.x, downrightIdx.y, level), 0).z;
-        let du_im1_jp1 = textureLoad(txCW_groupings, vec3<i32>(upleftIdx.x, upleftIdx.y, level), 0).z;
-        let du_im1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downleftIdx.x, downleftIdx.y, level), 0).z;
-
-        let dv_ip1_jp1 = textureLoad(txCW_groupings, vec3<i32>(uprightIdx.x, uprightIdx.y, level), 0).w;
-        let dv_ip1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downrightIdx.x, downrightIdx.y, level), 0).w;
-        let dv_im1_jp1 = textureLoad(txCW_groupings, vec3<i32>(upleftIdx.x, upleftIdx.y, level), 0).w;
-        let dv_im1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downleftIdx.x, downleftIdx.y, level), 0).w;
+       // let du_ip1_jp1 = textureLoad(txCW_groupings, vec3<i32>(uprightIdx.x, uprightIdx.y, level), 0).z;
+       // let du_ip1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downrightIdx.x, downrightIdx.y, level), 0).z;
+       // let du_im1_jp1 = textureLoad(txCW_groupings, vec3<i32>(upleftIdx.x, upleftIdx.y, level), 0).z;
+       // let du_im1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downleftIdx.x, downleftIdx.y, level), 0).z;
+
+       // let dv_ip1_jp1 = textureLoad(txCW_groupings, vec3<i32>(uprightIdx.x, uprightIdx.y, level), 0).w;
+       // let dv_ip1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downrightIdx.x, downrightIdx.y, level), 0).w;
+       // let dv_im1_jp1 = textureLoad(txCW_groupings, vec3<i32>(upleftIdx.x, upleftIdx.y, level), 0).w;
+       // let dv_im1_jm1 = textureLoad(txCW_groupings, vec3<i32>(downleftIdx.x, downleftIdx.y, level), 0).w;
 
         level = 1;
         let za_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).x;
         let dzadx = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).y;
-        let dzady = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).z;
+       // let dzady = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).z;
 
         level = 2;
         let S_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).x;
```

#### CT1-204 COULWAVE F source 구성

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:280; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:282; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 E2_y를 생략한다. temp1=u_here*dE1dx다. E·za·eta·S·T를 쓰는 x 항은 유지한다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 334행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 349행 포함).

```diff
@@ -280,58 +282,71 @@
 
         level = 3;
         let dSdx = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).x;
-        let dSdy = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).y;
+       // let dSdy = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).y;
         let dTdx = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).z;
-        let dTdy = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).w;
+       // let dTdy = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).w;
 
         level = 4;
         let E1_ip1 = textureLoad(txCW_groupings, vec3<i32>(rightIdx.x, rightIdx.y, level), 0).x;
         let E1_im1 = textureLoad(txCW_groupings, vec3<i32>(leftIdx.x, leftIdx.y, level), 0).x;
 
-        let E2_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).y;
-        let E2_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).y;
+       // let E2_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).y;
+       // let E2_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).y;
 
         let E_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).z;
-        let vort_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).w;  
+       // let vort_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).w;  
 
         level = 5;
         let EzST_ip1 = textureLoad(txCW_groupings, vec3<i32>(rightIdx.x, rightIdx.y, level), 0).x;
         let EzST_im1 = textureLoad(txCW_groupings, vec3<i32>(leftIdx.x, leftIdx.y, level), 0).x;
-        let EzST_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).x;
-        let EzST_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).x;
+       // let EzST_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).x;
+       // let EzST_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).x;
 
         let TzS2_ip1 = textureLoad(txCW_groupings, vec3<i32>(rightIdx.x, rightIdx.y, level), 0).y;
         let TzS2_im1 = textureLoad(txCW_groupings, vec3<i32>(leftIdx.x, leftIdx.y, level), 0).y;
-        let TzS2_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).y;
-        let TzS2_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).y;
+       // let TzS2_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).y;
+       // let TzS2_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).y;
         
         let uSxvSy_ip1 = textureLoad(txCW_groupings, vec3<i32>(rightIdx.x, rightIdx.y, level), 0).z;
         let uSxvSy_im1 = textureLoad(txCW_groupings, vec3<i32>(leftIdx.x, leftIdx.y, level), 0).z;
-        let uSxvSy_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).z;
-        let uSxvSy_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).z;
+       // let uSxvSy_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).z;
+       // let uSxvSy_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).z;
         
         let uTxvTy_ip1 = textureLoad(txCW_groupings, vec3<i32>(rightIdx.x, rightIdx.y, level), 0).w;
         let uTxvTy_im1 = textureLoad(txCW_groupings, vec3<i32>(leftIdx.x, leftIdx.y, level), 0).w;
-        let uTxvTy_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).w;
-        let uTxvTy_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).w;
+       // let uTxvTy_jp1 = textureLoad(txCW_groupings, vec3<i32>(upIdx.x, upIdx.y, level), 0).w;
+       // let uTxvTy_jm1 = textureLoad(txCW_groupings, vec3<i32>(downIdx.x, downIdx.y, level), 0).w;
 
         let dudx = 0.5 * (u_ip1 - u_im1) * globals.one_over_dx;
-        let dvdy = 0.5 * (v_jp1 - v_jm1) * globals.one_over_dy;
+       // let dvdy = 0.5 * (v_jp1 - v_jm1) * globals.one_over_dy;
         
         let ddudx = 0.5 * (du_ip1 - du_im1) * globals.one_over_dx;
-        let ddvdy = 0.5 * (dv_jp1 - dv_jm1) * globals.one_over_dy;
+       // let ddvdy = 0.5 * (dv_jp1 - dv_jm1) * globals.one_over_dy;
         
-        let dudxy = 0.25 *  ( u_ip1_jp1 -  u_ip1_jm1 -  u_im1_jp1 +  u_im1_jm1) * globals.one_over_dxdy;
-        let dvdxy = 0.25 *  ( v_ip1_jp1 -  v_ip1_jm1 -  v_im1_jp1 +  v_im1_jm1) * globals.one_over_dxdy;
-        let ddudxy = 0.25 * (du_ip1_jp1 - du_ip1_jm1 - du_im1_jp1 + du_im1_jm1) * globals.one_over_dxdy;
-        let ddvdxy = 0.25 * (dv_ip1_jp1 - dv_ip1_jm1 - dv_im1_jp1 + dv_im1_jm1) * globals.one_over_dxdy;
+       // let dudxy = 0.25 *  ( u_ip1_jp1 -  u_ip1_jm1 -  u_im1_jp1 +  u_im1_jm1) * globals.one_over_dxdy;
+       // let dvdxy = 0.25 *  ( v_ip1_jp1 -  v_ip1_jm1 -  v_im1_jp1 +  v_im1_jm1) * globals.one_over_dxdy;
+       // let ddudxy = 0.25 * (du_ip1_jp1 - du_ip1_jm1 - du_im1_jp1 + du_im1_jm1) * globals.one_over_dxdy;
+       // let ddvdxy = 0.25 * (dv_ip1_jp1 - dv_ip1_jm1 - dv_im1_jp1 + dv_im1_jm1) * globals.one_over_dxdy;
  
         // E source terms, take to 2nd order
         let dE1dx = 1.0 / 2.0 * (E1_ip1 - E1_im1) * globals.one_over_dx;
-        let dE2dy = 1.0 / 2.0 * (E2_jp1 - E2_jm1) * globals.one_over_dy;
+       // let dE2dy = 1.0 / 2.0 * (E2_jp1 - E2_jm1) * globals.one_over_dy;
 
         // F source terms
-        var temp1 = u_here * (dE1dx + dE2dy);
+       // var temp1 = u_here * (dE1dx + dE2dy);
+       // var temp2 = E_here * ( 0.5 * ( za_here * za_here - eta_here * eta_here) * dSdx
+       //                        + (za_here - eta_here) * dTdx 
+       //                        - detadx_loworder * (eta_here * S_here + T_here) );
+       // var temp3 = -0.5 * (EzST_ip1 - EzST_im1) * globals.one_over_dx;
+       // var temp4 = -0.5 * (uSxvSy_ip1 - uSxvSy_im1) * globals.one_over_dx;
+       // var temp5 = -0.5 * (uTxvTy_ip1 - uTxvTy_im1) * globals.one_over_dx;
+       // var temp6 = -0.5 * 0.5 * (TzS2_ip1 - TzS2_im1) * globals.one_over_dx;
+       // var temp7A= -v_here * dzadx * (dTdy + za_here * dSdy);
+       // var temp7B=  v_here * dzady * (dTdx + za_here * dSdx);
+       // var temp7C= -vort_here * ( (za_here - 0.5 * (eta_here - d_here)) * dTdy
+       //     + (0.5 * za_here * za_here - 1.0 / 6.0 * (eta_here * eta_here  - eta_here * d_here + d_here * d_here)) * dSdy );
+
+        var temp1 = u_here * (dE1dx);
         var temp2 = E_here * ( 0.5 * ( za_here * za_here - eta_here * eta_here) * dSdx
                                + (za_here - eta_here) * dTdx 
                                - detadx_loworder * (eta_here * S_here + T_here) );
```

#### CT1-205 COULWAVE G source와 교차 이력 제거

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:339; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:354; 아래 전체 diff의 +행 | 불일치 (F) | v=0과 y 미분=0에서 Gsrc·F_star·G_star·Psi2x·Psi1y·Psi2y는 0이다. transect 판은 이 값을 생략하거나 0.0으로 둔다. E_src=dE1dx다. 마찰은 v=0에서 평가한다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 380행 포함); `35b7f1c` 2026-01-15 (현재 395행 포함); `0b4e990` 2025-05-16 (현재 397행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 401행 포함).

```diff
@@ -339,62 +354,51 @@
         var temp4 = -0.5 * (uSxvSy_ip1 - uSxvSy_im1) * globals.one_over_dx;
         var temp5 = -0.5 * (uTxvTy_ip1 - uTxvTy_im1) * globals.one_over_dx;
         var temp6 = -0.5 * 0.5 * (TzS2_ip1 - TzS2_im1) * globals.one_over_dx;
-        var temp7A= -v_here * dzadx * (dTdy + za_here * dSdy);
-        var temp7B=  v_here * dzady * (dTdx + za_here * dSdx);
-        var temp7C= -vort_here * ( (za_here - 0.5 * (eta_here - d_here)) * dTdy
-            + (0.5 * za_here * za_here - 1.0 / 6.0 * (eta_here * eta_here  - eta_here * d_here + d_here * d_here)) * dSdy );
+        var temp7A= 0.0;
+        var temp7B= 0.0;
+        var temp7C= 0.0;
 
         let Fsrc = temp1 + temp2 + h_here * (temp3 + temp4 + temp5 + temp6 + temp7A + temp7B + temp7C);
 
         // G source terms
-        temp1 = v_here * (dE1dx + dE2dy);
-        temp2 = E_here * ( 0.5 * ( za_here * za_here - eta_here * eta_here) * dSdy
-                               + (za_here - eta_here) * dTdy 
-                               - detady_loworder * (eta_here * S_here + T_here) );
-        temp3 = -0.5 * (EzST_jp1 - EzST_jm1) * globals.one_over_dy;   
-        temp4 = -0.5 * (uSxvSy_jp1 - uSxvSy_jm1) * globals.one_over_dy;
-        temp5 = -0.5 * (uTxvTy_jp1 - uTxvTy_jm1) * globals.one_over_dy;
-        temp6 = -0.5 * 0.5 * (TzS2_jp1 - TzS2_jm1) * globals.one_over_dy;
-        temp7A=  u_here * dzadx * (dTdy + za_here * dSdy);
-        temp7B= -u_here * dzady * (dTdx + za_here * dSdx);
-        temp7C=  vort_here * ( (za_here - 0.5 * (eta_here - d_here)) * dTdx
-            + (0.5 * za_here * za_here - 1.0 / 6.0 * (eta_here * eta_here  - eta_here * d_here + d_here * d_here)) * dSdx );
-
-        let Gsrc = temp1 + temp2 + h_here * (temp3 + temp4 + temp5 + temp6 + temp7A + temp7B + temp7C);
+       // temp1 = v_here * (dE1dx + dE2dy);
+       // temp2 = E_here * ( 0.5 * ( za_here * za_here - eta_here * eta_here) * dSdy
+       //                        + (za_here - eta_here) * dTdy 
+       //                        - detady_loworder * (eta_here * S_here + T_here) );
+       // temp3 = -0.5 * (EzST_jp1 - EzST_jm1) * globals.one_over_dy;   
+       // temp4 = -0.5 * (uSxvSy_jp1 - uSxvSy_jm1) * globals.one_over_dy;
+       // temp5 = -0.5 * (uTxvTy_jp1 - uTxvTy_jm1) * globals.one_over_dy;
+       // temp6 = -0.5 * 0.5 * (TzS2_jp1 - TzS2_jm1) * globals.one_over_dy;
+       // temp7A=  u_here * dzadx * (dTdy + za_here * dSdy);
+       // temp7B= -u_here * dzady * (dTdx + za_here * dSdx);
+       // temp7C=  vort_here * ( (za_here - 0.5 * (eta_here - d_here)) * dTdx
+       //     + (0.5 * za_here * za_here - 1.0 / 6.0 * (eta_here * eta_here  - eta_here * d_here + d_here * d_here)) * dSdx );
+
+       // let Gsrc = temp1 + temp2 + h_here * (temp3 + temp4 + temp5 + temp6 + temp7A + temp7B + temp7C);
 
-        let coef1 = 0.5*(eta_here * eta_here - za_here * za_here);
-        let coef2 = - (za_here - eta_here);
+       // let coef1 = 0.5*(eta_here * eta_here - za_here * za_here);
+       // let coef2 = - (za_here - eta_here);
 
-        F_star = coef1 * dvdxy + coef2 * ddvdxy + detadx * (eta_here * dvdy + ddvdy);
-        F_star = h_here * F_star;
+       // F_star = coef1 * dvdxy + coef2 * ddvdxy + detadx * (eta_here * dvdy + ddvdy);
+       // F_star = h_here * F_star;
 
-        G_star = coef1 * dudxy + coef2 * ddudxy + detady * (eta_here * dudx + ddudx);
-        G_star = h_here * G_star;
+       // G_star = coef1 * dudxy + coef2 * ddudxy + detady * (eta_here * dudx + ddudx);
+       // G_star = h_here * G_star;
 
         Psi1x = Fsrc;
-        Psi2x = (3.0 * F_star - 4.0 * F_G_star_oldies.y  + F_G_star_oldOldies.y) / globals.dt * 0.5;
+       // Psi2x = (3.0 * F_star - 4.0 * F_G_star_oldies.y  + F_G_star_oldOldies.y) / globals.dt * 0.5;
+        Psi2x = 0.0;
 
-        Psi1y = Gsrc;
-        Psi2y = (3.0 * G_star - 4.0 * F_G_star_oldies.z  + F_G_star_oldOldies.z) / globals.dt * 0.5;
+       // Psi1y = Gsrc;
+       // Psi2y = (3.0 * G_star - 4.0 * F_G_star_oldies.z  + F_G_star_oldOldies.z) / globals.dt * 0.5;
 
-        E_src = (dE1dx + dE2dy);
+       // E_src = (dE1dx + dE2dy);
+        E_src = (dE1dx);
     }
    
-    // vorticity-based momentum mixing / dissipation
-    var vorticity_dissipation = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    if (globals.vort_friction_factor > 0.0) {
-        let dPdxy = 0.25 * (textureLoad(txState, uprightIdx, 0).y - textureLoad(txState, upleftIdx, 0).y - textureLoad(txState, downrightIdx, 0).y + textureLoad(txState, downleftIdx, 0).y) * globals.one_over_dxdy;
-        let dPdyy = (textureLoad(txState, upIdx, 0).y - 2.0 * in_state_here.y + textureLoad(txState, downIdx, 0).y) * globals.one_over_d2y;
-        let dQdxx = (textureLoad(txState, rightIdx, 0).z - 2.0 * in_state_here.z + textureLoad(txState, leftIdx, 0).z) * globals.one_over_d2x;
-        let dQdxy = 0.25 * (textureLoad(txState, uprightIdx, 0).z - textureLoad(txState, upleftIdx, 0).z - textureLoad(txState, downrightIdx, 0).z + textureLoad(txState, downleftIdx, 0).z) * globals.one_over_dxdy;
-        let domegady = dPdyy - dQdxy;
-        let domegadx = dPdxy - dQdxx;
-        vorticity_dissipation.y = globals.vort_friction_factor  * domegady;
-        vorticity_dissipation.z = -globals.vort_friction_factor  * domegadx;
-    }
-
     let friction_here = max(globals.friction, textureLoad(txBottomFriction, idx, 0).x);
-    var friction_ = FrictionCalc(in_state_here.y, in_state_here.z, h_here, friction_here);
+   // var friction_ = FrictionCalc(in_state_here.y, in_state_here.z, h_here, friction_here);
+    var friction_ = FrictionCalc(in_state_here.y, 0.0, h_here, friction_here);
 
     // dhdt for depth change option
     let dhdt = textureLoad(txBoundaryForcing, idx, 0).y;
```

#### CT1-206 COULWAVE 압력과 백수 확산

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:402; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:406; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 x 압력·Dxx 확산·백수 감쇠만 남긴다. |

본판 차이 줄의 마지막 수정: `0b4e990` 2025-05-16 (현재 434행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 438행 포함).

```diff
@@ -402,36 +406,36 @@
     // Pressure stencil calculations
     let P_left = textureLoad(txBoundaryForcing, leftIdx, 0).x;
     let P_right = textureLoad(txBoundaryForcing, rightIdx, 0).x;
-    let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;
-    let P_up = textureLoad(txBoundaryForcing, upIdx, 0).x;
+   // let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;
+   // let P_up = textureLoad(txBoundaryForcing, upIdx, 0).x;
 
     let press_x = -0.5 * h_here * globals.g_over_dx * (P_right - P_left);
-    let press_y = -0.5 * h_here * globals.g_over_dy * (P_up - P_down);
+   // let press_y = -0.5 * h_here * globals.g_over_dy * (P_up - P_down);
 
     // Calculate scalar transport additions
     let C_state_here = textureLoad(txState, idx, 0).w;
     let C_state_right = textureLoad(txState, rightIdx, 0).w;
     let C_state_left = textureLoad(txState, leftIdx, 0).w;
-    let C_state_up = textureLoad(txState, upIdx, 0).w;
-    let C_state_down = textureLoad(txState, downIdx, 0).w;
-    let C_state_up_left = textureLoad(txState, upleftIdx, 0).w;
-    let C_state_up_right = textureLoad(txState, uprightIdx, 0).w;
-    let C_state_down_left = textureLoad(txState, downleftIdx, 0).w;
-    let C_state_down_right = textureLoad(txState, downrightIdx, 0).w;
+   // let C_state_up = textureLoad(txState, upIdx, 0).w;
+   // let C_state_down = textureLoad(txState, downIdx, 0).w;
+   // let C_state_up_left = textureLoad(txState, upleftIdx, 0).w;
+   // let C_state_up_right = textureLoad(txState, uprightIdx, 0).w;
+   // let C_state_down_left = textureLoad(txState, downleftIdx, 0).w;
+   // let C_state_down_right = textureLoad(txState, downrightIdx, 0).w;
 
     let Dxx = globals.whiteWaterDispersion;
-    let Dxy = globals.whiteWaterDispersion;
-    let Dyy = globals.whiteWaterDispersion;
+   // let Dxy = globals.whiteWaterDispersion;
+   // let Dyy = globals.whiteWaterDispersion;
 
     let hc_by_dx_dx = Dxx * globals.one_over_d2x * (C_state_right - 2.0 * in_state_here.a + C_state_left);
-    let hc_by_dy_dy = Dyy * globals.one_over_d2y * (C_state_up - 2.0 * in_state_here.a + C_state_down);
-    let hc_by_dx_dy = 0.25 * Dxy * globals.one_over_dxdy * (C_state_up_right - C_state_up_left - C_state_down_right + C_state_down_left);
+   // let hc_by_dy_dy = Dyy * globals.one_over_d2y * (C_state_up - 2.0 * in_state_here.a + C_state_down);
+   // let hc_by_dx_dy = 0.25 * Dxy * globals.one_over_dxdy * (C_state_up_right - C_state_up_left - C_state_down_right + C_state_down_left);
 
     let c_dissipation = -globals.whiteWaterDecayRate * C_state_here;
 
     // calculate breaking dissipation
     var breaking_x = 0.0;
-    var breaking_y = 0.0;
+   // var breaking_y = 0.0;
     var breaking_B = 0.0;
     
     if(globals.useBreakingModel == 1) {
```

#### CT1-207 COULWAVE 쇄파 확산

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:440; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:444; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 breaking_x=dPdxx로 둔다. y 응력과 y 해안선 기울기를 생략한다. |

본판 차이 줄의 마지막 수정: `0b4e990` 2025-05-16 (현재 469행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 474행 포함).

```diff
@@ -440,33 +444,34 @@
         let nu_flux_here = textureLoad(txDissipationFlux, idx, 0);
         let nu_flux_right = textureLoad(txDissipationFlux, rightIdx, 0);
         let nu_flux_left = textureLoad(txDissipationFlux, leftIdx, 0);
-        let nu_flux_up = textureLoad(txDissipationFlux, upIdx, 0);
-        let nu_flux_down = textureLoad(txDissipationFlux, downIdx, 0);
+       // let nu_flux_up = textureLoad(txDissipationFlux, upIdx, 0);
+       // let nu_flux_down = textureLoad(txDissipationFlux, downIdx, 0);
 
         let dPdxx = 0.5 * (nu_flux_right.x - nu_flux_left.x) * globals.one_over_dx;
-        let dPdyx = 0.5 * (nu_flux_right.y - nu_flux_left.y) * globals.one_over_dx;
-        let dPdyy = 0.5 * (nu_flux_up.y - nu_flux_down.y) * globals.one_over_dy;
+       // let dPdyx = 0.5 * (nu_flux_right.y - nu_flux_left.y) * globals.one_over_dx;
+       // let dPdyy = 0.5 * (nu_flux_up.y - nu_flux_down.y) * globals.one_over_dy;
 
-        let dQdxx = 0.5 * (nu_flux_right.z - nu_flux_left.z) * globals.one_over_dx;
-        let dQdxy = 0.5 * (nu_flux_up.z - nu_flux_down.z) * globals.one_over_dy;
-        let dQdyy = 0.5 * (nu_flux_up.w - nu_flux_down.w) * globals.one_over_dy;
+       // let dQdxx = 0.5 * (nu_flux_right.z - nu_flux_left.z) * globals.one_over_dx;
+       // let dQdxy = 0.5 * (nu_flux_up.z - nu_flux_down.z) * globals.one_over_dy;
+       // let dQdyy = 0.5 * (nu_flux_up.w - nu_flux_down.w) * globals.one_over_dy;
         
         if (near_dry > 0.){
-            breaking_x = dPdxx + 0.5 * dPdyy + 0.5 * dQdxy;
-            breaking_y = dQdyy + 0.5 * dPdyx + 0.5 * dQdxx;
+           // breaking_x = dPdxx + 0.5 * dPdyy + 0.5 * dQdxy;
+            breaking_x = dPdxx;
+           // breaking_y = dQdyy + 0.5 * dPdyx + 0.5 * dQdxx;
         }
     }
     
     // fix slope near shoreline
-    if (h_min.x <= h_cut && h_min.z <= h_cut) {
-        detady = 0.0;
-    }
-    else if (h_min.x <= h_cut) {  //north
-        detady = 1.*(eta_here - eta_south) * globals.one_over_dy;
-    }
-    else if (h_min.z <= h_cut) {  //south
-        detady = 1.*(eta_north - eta_here) * globals.one_over_dy;
-    }
+   // if (h_min.x <= h_cut && h_min.z <= h_cut) {
+   //     detady = 0.0;
+   // }
+   // else if (h_min.x <= h_cut) {  //north
+   //     detady = 1.*(eta_here - eta_south) * globals.one_over_dy;
+   // }
+   // else if (h_min.z <= h_cut) {  //south
+   //     detady = 1.*(eta_north - eta_here) * globals.one_over_dy;
+   // }
 
     if (h_min.y <= h_cut && h_min.w <= h_cut) {
         detadx = 0.0;
```

#### CT1-208 COULWAVE 적분 source

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:483; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:488; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 x의 Psi1x+Psi2x를 유지한다. y 운동량 source는 0.0이다. 시간적분 계수는 같다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 486행 포함); `35b7f1c` 2026-01-15 (현재 488행 포함); `0b4e990` 2025-05-16 (현재 491행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 499행 포함).

```diff
@@ -483,12 +488,15 @@
         overflow_dry = -globals.infiltrationRate;  // hydraulic conductivity of coarse, unsaturated sand
     }
 
-    let source_term = vec4<f32>(dhdt + overflow_dry + E_src, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + breaking_y + (Psi1y + Psi2y) + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);
+   // let source_term = vec4<f32>(dhdt + overflow_dry + E_src, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + breaking_y + (Psi1y + Psi2y) + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);
+    let source_term = vec4<f32>(dhdt + overflow_dry + E_src, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, 0.0, hc_by_dx_dx + c_dissipation);
 
-    let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term + vorticity_dissipation;
+   // let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term;
+    let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + source_term;
 
     var newState = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    let F_G_here = vec4<f32>(0.0, F_star, G_star, 0.0);
+   // let F_G_here = vec4<f32>(0.0, F_star, G_star, 0.0);
+    let F_G_here = vec4<f32>(0.0, 0.0, 0.0, 0.0);
 
     if (globals.timeScheme == 0) {
         newState = in_state_here_UV + globals.dt * d_by_dt;
```

#### CT1-209 COULWAVE 교차 이력 쓰기 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_COULWAVE.wgsl:519; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:527; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 1D에서 0인 F_G_star 쓰기를 생략한다. |

본판 차이 줄의 마지막 수정: `0b4e990` 2025-05-16 (현재 522행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 530행 포함).

```diff
@@ -519,6 +527,6 @@
 
     textureStore(txNewState, idx, newState);
     textureStore(dU_by_dt, idx, d_by_dt);
-    textureStore(F_G_star, idx, F_G_here);
+  //  textureStore(F_G_star, idx, F_G_here);
     textureStore(current_stateUVstar, idx, newState);
 }
```


### 2.34 shaders/Pass3_NLSW.wgsl

본판: `shaders/Pass3_NLSW.wgsl`. transect 판: `transect_version/shaders/Pass3_NLSW.wgsl`.
원래 diff는 566행이다. CR 제외 diff는 6구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `35b7f1c` | 2026-01-15 | addition of vorticity-based momentum mixing |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-210 와도 소산 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_NLSW.wgsl:35; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_NLSW.wgsl:35; 아래 전체 diff의 +행 | 불일치 (A) | 본판의 vort_friction_factor는 후속 추가 기능이다. transect 판에는 이 uniform이 없다. |

본판 차이 줄의 마지막 수정: `35b7f1c` 2026-01-15 (현재 38행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -35,7 +35,6 @@
     east_boundary_type: i32,
     south_boundary_type: i32,
     north_boundary_type: i32,
-    vort_friction_factor: f32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-211 천수 적분 스텐실과 마찰

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_NLSW.wgsl:97; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_NLSW.wgsl:96; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 x 경계에서만 조기 반환한다. 동·서 건조 검사와 x flux만 남긴다. v=0을 마찰 함수에 넣는다. y 미분과 횡운동량이 0이면 본판 와도 소산도 0이다. |

본판 차이 줄의 마지막 수정: `471c581` 2024-01-04 (현재 100행 포함); `63a12e3` 2023-10-19 (현재 159행 포함); `ebc98a5` 2024-03-13 (현재 165행 포함); `7542e27` 2024-05-24 (현재 146행 포함); `35b7f1c` 2026-01-15 (현재 179행 포함); `98f41c9` 2024-04-18 (현재 181행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 170행 포함).

```diff
@@ -97,88 +96,78 @@
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
 
-    if (idx.x >= globals.width - 2 || idx.y >= globals.height - 2 || idx.x <= 1 || idx.y <= 1) {
+ // if (idx.x >= globals.width - 2 || idx.y >= globals.height - 2 || idx.x <= 1 || idx.y <= 1) {
+    if (idx.x >= globals.width - 2 || idx.x <= 1) {
         let zero = vec4<f32>(0.0, 0.0, 0.0, 0.0);
         textureStore(txNewState, idx, zero);
         textureStore(dU_by_dt, idx, zero);
-        textureStore(F_G_star, idx, zero);
+       // textureStore(F_G_star, idx, zero);
         textureStore(current_stateUVstar, idx, zero);
         return;
     }
 
     let leftIdx = idx + vec2<i32>(-1, 0);
     let rightIdx = idx + vec2<i32>(1, 0);
-    let downIdx = idx + vec2<i32>(0, -1);
-    let upIdx = idx + vec2<i32>(0, 1);
-    let upleftIdx = idx + vec2<i32>(-1, 1);
-    let uprightIdx = idx + vec2<i32>(1, 1);
-    let downleftIdx = idx + vec2<i32>(-1, -1);
-    let downrightIdx = idx + vec2<i32>(1, -1);
+   // let downIdx = idx + vec2<i32>(0, -1);
+   // let upIdx = idx + vec2<i32>(0, 1);
+   // let upleftIdx = idx + vec2<i32>(-1, 1);
+   // let uprightIdx = idx + vec2<i32>(1, 1);
+   // let downleftIdx = idx + vec2<i32>(-1, -1);
+   // let downrightIdx = idx + vec2<i32>(1, -1);
 
     let B_here = textureLoad(txBottom, idx, 0).z;
 
     let in_state_here = textureLoad(txState, idx, 0);
     let in_state_here_UV = textureLoad(txstateUVstar, idx, 0);
 
-    let B_south = textureLoad(txBottom, downIdx, 0).z;
-    let B_north = textureLoad(txBottom, upIdx, 0).z;
+   // let B_south = textureLoad(txBottom, downIdx, 0).z;
+   // let B_north = textureLoad(txBottom, upIdx, 0).z;
     let B_west = textureLoad(txBottom, leftIdx, 0).z;
     let B_east = textureLoad(txBottom, rightIdx, 0).z;
 
     let eta_here = in_state_here.x;
     let eta_west = textureLoad(txState, leftIdx, 0).x;
     let eta_east = textureLoad(txState, rightIdx, 0).x;
-    let eta_south = textureLoad(txState, downIdx, 0).x;
-    let eta_north = textureLoad(txState, upIdx, 0).x;
+   // let eta_south = textureLoad(txState, downIdx, 0).x;
+   // let eta_north = textureLoad(txState, upIdx, 0).x;
 
     let h_here = in_state_here.x - B_here;
     let h_west = eta_west - B_west;
     let h_east = eta_east - B_east;
-    let h_north = eta_north - B_north;
-    let h_south = eta_south - B_south;
+   // let h_north = eta_north - B_north;
+   // let h_south = eta_south - B_south;
 
     let h_cut = globals.delta;
     if (h_here <= h_cut) {   //if dry and surrounded by dry, then stay dry - no need to calc
-        if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
+       // if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
+        if(h_east <= h_cut && h_west <= h_cut) {
             let zero = vec4<f32>(0.0, 0.0, 0.0, 0.0);
             textureStore(txNewState, idx, zero);
             textureStore(dU_by_dt, idx, zero);
-            textureStore(F_G_star, idx, zero);
+           // textureStore(F_G_star, idx, zero);
             textureStore(current_stateUVstar, idx, zero);
             return; 
         }
     }
 
     var h_min = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    h_min.x= min(h_here, h_north);
+   // h_min.x= min(h_here, h_north);
     h_min.y= min(h_here, h_east);
-    h_min.z= min(h_here, h_south);
+   // h_min.z= min(h_here, h_south);
     h_min.w= min(h_here, h_west);
 
     var detadx = 0.5*(eta_east - eta_west) * globals.one_over_dx;
-    var detady = 0.5*(eta_north - eta_south) * globals.one_over_dy;
+   // var detady = 0.5*(eta_north - eta_south) * globals.one_over_dy;
 
     // Load values from txXFlux and txYFlux using idx
     var xflux_here = textureLoad(txXFlux, idx, 0);
     var xflux_west = textureLoad(txXFlux, leftIdx, 0);
-    var yflux_here = textureLoad(txYFlux, idx, 0);
-    var yflux_south = textureLoad(txYFlux, downIdx, 0);
+   // var yflux_here = textureLoad(txYFlux, idx, 0);
+   // var yflux_south = textureLoad(txYFlux, downIdx, 0);
    
-    // vorticity-based momentum mixing / dissipation
-    var vorticity_dissipation = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    if (globals.vort_friction_factor > 0.0) {
-        let dPdxy = 0.25 * (textureLoad(txState, uprightIdx, 0).y - textureLoad(txState, upleftIdx, 0).y - textureLoad(txState, downrightIdx, 0).y + textureLoad(txState, downleftIdx, 0).y) * globals.one_over_dxdy;
-        let dPdyy = (textureLoad(txState, upIdx, 0).y - 2.0 * in_state_here.y + textureLoad(txState, downIdx, 0).y) * globals.one_over_d2y;
-        let dQdxx = (textureLoad(txState, rightIdx, 0).z - 2.0 * in_state_here.z + textureLoad(txState, leftIdx, 0).z) * globals.one_over_d2x;
-        let dQdxy = 0.25 * (textureLoad(txState, uprightIdx, 0).z - textureLoad(txState, upleftIdx, 0).z - textureLoad(txState, downrightIdx, 0).z + textureLoad(txState, downleftIdx, 0).z) * globals.one_over_dxdy;
-        let domegady = dPdyy - dQdxy;
-        let domegadx = dPdxy - dQdxx;
-        vorticity_dissipation.y = globals.vort_friction_factor  * domegady;
-        vorticity_dissipation.z = -globals.vort_friction_factor  * domegadx;
-    }
-
     let friction_here = max(globals.friction, textureLoad(txBottomFriction, idx, 0).x);
-    var friction_ = FrictionCalc(in_state_here.y, in_state_here.z, h_here, friction_here);
+   // var friction_ = FrictionCalc(in_state_here.y, in_state_here.z, h_here, friction_here);
+    var friction_ = FrictionCalc(in_state_here.y, 0.0, h_here, friction_here);
 
     // dhdt for depth change option
     let dhdt = textureLoad(txBoundaryForcing, idx, 0).y;
```

#### CT1-212 압력과 백수 확산의 1D 환원

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_NLSW.wgsl:186; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_NLSW.wgsl:175; 아래 전체 diff의 +행 | 불일치 (F) | x 압력 차분은 같다. transect 판은 y 압력 차분과 Dxy·Dyy의 백수 확산을 생략한다. |

본판 차이 줄의 마지막 수정: `18fa7ab` 2025-04-11 (현재 190행 포함); `63a12e3` 2023-10-19 (현재 211행 포함); `366ee34` 2024-04-08 (현재 208행 포함); `2eb2866` 2023-10-26 (현재 212행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 201행 포함).

```diff
@@ -186,30 +175,30 @@
     // Pressure stencil calculations
     let P_left = textureLoad(txBoundaryForcing, leftIdx, 0).x;
     let P_right = textureLoad(txBoundaryForcing, rightIdx, 0).x;
-    let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;
-    let P_up = textureLoad(txBoundaryForcing, upIdx, 0).x;
+   // let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;
+   // let P_up = textureLoad(txBoundaryForcing, upIdx, 0).x;
 
     let press_x = -0.5 * h_here * globals.g_over_dx * (P_right - P_left);
-    let press_y = -0.5 * h_here * globals.g_over_dy * (P_up - P_down);
+   // let press_y = -0.5 * h_here * globals.g_over_dy * (P_up - P_down);
 
     // Calculate scalar transport additions
     let C_state_here = textureLoad(txState, idx, 0).w;
     let C_state_right = textureLoad(txState, rightIdx, 0).w;
     let C_state_left = textureLoad(txState, leftIdx, 0).w;
-    let C_state_up = textureLoad(txState, upIdx, 0).w;
-    let C_state_down = textureLoad(txState, downIdx, 0).w;
-    let C_state_up_left = textureLoad(txState, upleftIdx, 0).w;
-    let C_state_up_right = textureLoad(txState, uprightIdx, 0).w;
-    let C_state_down_left = textureLoad(txState, downleftIdx, 0).w;
-    let C_state_down_right = textureLoad(txState, downrightIdx, 0).w;
+   // let C_state_up = textureLoad(txState, upIdx, 0).w;
+   // let C_state_down = textureLoad(txState, downIdx, 0).w;
+   // let C_state_up_left = textureLoad(txState, upleftIdx, 0).w;
+   // let C_state_up_right = textureLoad(txState, uprightIdx, 0).w;
+   // let C_state_down_left = textureLoad(txState, downleftIdx, 0).w;
+   // let C_state_down_right = textureLoad(txState, downrightIdx, 0).w;
 
     let Dxx = globals.whiteWaterDispersion;
-    let Dxy = globals.whiteWaterDispersion;
-    let Dyy = globals.whiteWaterDispersion;
+   // let Dxy = globals.whiteWaterDispersion;
+   // let Dyy = globals.whiteWaterDispersion;
 
     let hc_by_dx_dx = Dxx * globals.one_over_d2x * (C_state_right - 2.0 * in_state_here.a + C_state_left);
-    let hc_by_dy_dy = Dyy * globals.one_over_d2y * (C_state_up - 2.0 * in_state_here.a + C_state_down);
-    let hc_by_dx_dy = 0.25 * Dxy * globals.one_over_dxdy * (C_state_up_right - C_state_up_left - C_state_down_right + C_state_down_left);
+   // let hc_by_dy_dy = Dyy * globals.one_over_d2y * (C_state_up - 2.0 * in_state_here.a + C_state_down);
+   // let hc_by_dx_dy = 0.25 * Dxy * globals.one_over_dxdy * (C_state_up_right - C_state_up_left - C_state_down_right + C_state_down_left);
 
     let c_dissipation = -globals.whiteWaterDecayRate * C_state_here;
```

#### CT1-213 해안선 기울기 보정

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_NLSW.wgsl:220; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_NLSW.wgsl:209; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 y 기울기 보정을 생략한다. 동·서 면의 일방향 x 차분은 유지한다. |

본판 차이 줄의 마지막 수정: `ebc98a5` 2024-03-13 (현재 231행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 220행 포함).

```diff
@@ -220,15 +209,15 @@
     }
 
     // fix slope near shoreline
-    if (h_min.x <= h_cut && h_min.z <= h_cut) {
-        detady = 0.0;
-    }
-    else if (h_min.x <= h_cut) {  //north
-        detady = 1.*(eta_here - eta_south) * globals.one_over_dy;
-    }
-    else if (h_min.z <= h_cut) {  //south
-        detady = 1.*(eta_north - eta_here) * globals.one_over_dy;
-    }
+   // if (h_min.x <= h_cut && h_min.z <= h_cut) {
+   //     detady = 0.0;
+   // }
+   // else if (h_min.x <= h_cut) {  //north
+   //     detady = 1.*(eta_here - eta_south) * globals.one_over_dy;
+   // }
+   // else if (h_min.z <= h_cut) {  //south
+   //     detady = 1.*(eta_north - eta_here) * globals.one_over_dy;
+   // }
 
     if (h_min.y <= h_cut && h_min.w <= h_cut) {
         detadx = 0.0;
```

#### CT1-214 천수 source와 flux 발산

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_NLSW.wgsl:245; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_NLSW.wgsl:234; 아래 전체 diff의 +행 | 불일치 (F) | y 미분=0과 Q=0을 본판 식에 대입하면 transect 식이 된다. 침투와 백수 감쇠의 부호는 같다. Euler·AB3·AM4 계수는 이 구간 밖에서 동일하다. |

본판 차이 줄의 마지막 수정: `18fa7ab` 2025-04-11 (현재 248행 포함); `35b7f1c` 2026-01-15 (현재 250행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 241행 포함).

```diff
@@ -245,9 +234,11 @@
         overflow_dry = -globals.infiltrationRate;  // hydraulic conductivity of coarse, unsaturated sand
     }
 
-    let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);
+   // let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);
+    let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + press_x, 0.0, hc_by_dx_dx + c_dissipation);
 
-    let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term + vorticity_dissipation;
+   // let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term;
+    let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + source_term;
 
     // previous derivatives
     let oldies = textureLoad(oldGradients, idx, 0);
```

#### CT1-215 불필요한 분산 이력 쓰기 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass3_NLSW.wgsl:277; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass3_NLSW.wgsl:268; 아래 전체 diff의 +행 | 불일치 (F) | NLSW는 분산 솔브를 건너뛴다. transect 판은 사용하지 않는 F_G_star 쓰기를 주석 처리한다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 284행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 275행 포함).

```diff
@@ -277,10 +268,10 @@
         newState.a = min(1.0, newState.a + contaminent_source); 
     }
 
-    let F_G_vec = vec4<f32>(0.0, 0.0, 0.0, 1.0);
+   // let F_G_vec = vec4<f32>(0.0, 0.0, 0.0, 1.0);
 
     textureStore(txNewState, idx, newState);
     textureStore(dU_by_dt, idx, d_by_dt);
-    textureStore(F_G_star, idx, F_G_vec);
+   // textureStore(F_G_star, idx, F_G_vec);
     textureStore(current_stateUVstar, idx, newState);
 }
\ No newline at end of file
```


### 2.35 shaders/Pass_Breaking.wgsl

본판: `shaders/Pass_Breaking.wgsl`. transect 판: `transect_version/shaders/Pass_Breaking.wgsl`.
원래 diff는 125행이다. CR 제외 diff는 4구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `18fa7ab` | 2025-04-11 | moving depth (slide) additions |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-216 쇄파 x 이웃

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass_Breaking.wgsl:33; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass_Breaking.wgsl:33; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 y flux와 y·대각 이웃을 읽지 않는다. |

본판 차이 줄의 마지막 수정: `366ee34` 2024-04-08 (현재 53행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 53행 포함).

```diff
@@ -33,24 +33,24 @@
 
     let leftIdx = idx + vec2<i32>(-1, 0);
     let rightIdx = idx + vec2<i32>(1, 0);
-    let downIdx = idx + vec2<i32>(0, -1);
-    let upIdx = idx + vec2<i32>(0, 1);
-    let upleftIdx = idx + vec2<i32>(-1, 1);
-    let uprightIdx = idx + vec2<i32>(1, 1);
-    let downleftIdx = idx + vec2<i32>(-1, -1);
-    let downrightIdx = idx + vec2<i32>(1, -1);
+   // let downIdx = idx + vec2<i32>(0, -1);
+   // let upIdx = idx + vec2<i32>(0, 1);
+   // let upleftIdx = idx + vec2<i32>(-1, 1);
+   // let uprightIdx = idx + vec2<i32>(1, 1);
+   // let downleftIdx = idx + vec2<i32>(-1, -1);
+   // let downrightIdx = idx + vec2<i32>(1, -1);
 
     let xflux_here = textureLoad(txXFlux, idx, 0).x;
     let xflux_west = textureLoad(txXFlux, leftIdx, 0).x;
-    let yflux_here = textureLoad(txYFlux, idx, 0).x;
-    let yflux_south = textureLoad(txYFlux, downIdx, 0).x;
+   // let yflux_here = textureLoad(txYFlux, idx, 0).x;
+   // let yflux_south = textureLoad(txYFlux, downIdx, 0).x;
 
-    let P_south = textureLoad(txState, downIdx, 0).y;
+   // let P_south = textureLoad(txState, downIdx, 0).y;
     let P_here = textureLoad(txState, idx, 0).y;
-    let P_north = textureLoad(txState, upIdx, 0).y;
-    let Q_west = textureLoad(txState, leftIdx, 0).z;
-    let Q_here = textureLoad(txState, idx, 0).z;
-    let Q_east = textureLoad(txState, rightIdx, 0).z;
+   // let P_north = textureLoad(txState, upIdx, 0).y;
+   // let Q_west = textureLoad(txState, leftIdx, 0).z;
+   // let Q_here = textureLoad(txState, idx, 0).z;
+   // let Q_east = textureLoad(txState, rightIdx, 0).z;
 
     let detadt = textureLoad(dU_by_dt, idx, 0).x;
```

#### CT1-217 쇄파 나이 전파와 x gradient

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass_Breaking.wgsl:59; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass_Breaking.wgsl:59; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 P_here의 부호로 x 상류 이웃 t1만 사용한다. Q=0인 1D에서 y 방향 gradient와 횡응력은 0이다. |

본판 차이 줄의 마지막 수정: `366ee34` 2024-04-08 (현재 89행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 91행 포함).

```diff
@@ -59,34 +59,36 @@
     var t1 = 0.0;
     var t2 = 0.0;
     var t3 = 0.0;
-    if (abs(P_here) > abs(Q_here) ) {
+   // if (abs(P_here) > abs(Q_here) ) {
         if (P_here > 0.0) {
             t1 = textureLoad(txBreaking, leftIdx, 0).x;
-            t2 = textureLoad(txBreaking, upleftIdx, 0).x;
-            t3 = textureLoad(txBreaking, downleftIdx, 0).x;
+           // t2 = textureLoad(txBreaking, upleftIdx, 0).x;
+           // t3 = textureLoad(txBreaking, downleftIdx, 0).x;
         } else {
             t1 = textureLoad(txBreaking, rightIdx, 0).x;
-            t2 = textureLoad(txBreaking, uprightIdx, 0).x;
-            t3 = textureLoad(txBreaking, downrightIdx, 0).x;
+           // t2 = textureLoad(txBreaking, uprightIdx, 0).x;
+           // t3 = textureLoad(txBreaking, downrightIdx, 0).x;
         }
-    } else {
-        if (Q_here > 0.0) {
-            t1 = textureLoad(txBreaking, downIdx, 0).x;
-            t2 = textureLoad(txBreaking, downrightIdx, 0).x;
-            t3 = textureLoad(txBreaking, downleftIdx, 0).x;
-        } else {
-            t1 = textureLoad(txBreaking, upIdx, 0).x;
-            t2 = textureLoad(txBreaking, uprightIdx, 0).x;
-            t3 = textureLoad(txBreaking, upleftIdx, 0).x;
-        }
-    } 
-    t_here = max(t_here, max(t1, max(t2, t3)));
+   // } else {
+   //     if (Q_here > 0.0) {
+   //         t1 = textureLoad(txBreaking, downIdx, 0).x;
+   //         t2 = textureLoad(txBreaking, downrightIdx, 0).x;
+   //         t3 = textureLoad(txBreaking, downleftIdx, 0).x;
+   //     } else {
+   //         t1 = textureLoad(txBreaking, upIdx, 0).x;
+   //         t2 = textureLoad(txBreaking, uprightIdx, 0).x;
+   //         t3 = textureLoad(txBreaking, upleftIdx, 0).x;
+   //     }
+   // } 
+    
+   // t_here = max(t_here, max(t1, max(t2, t3)));
+    t_here = max(t_here, t1);
 
     let dPdx = (xflux_here - xflux_west) * globals.one_over_dx;
-    let dPdy = 0.5 * (P_north - P_south) * globals.one_over_dy;
+   // let dPdy = 0.5 * (P_north - P_south) * globals.one_over_dy;
 
-    let dQdx = 0.5 * (Q_east - Q_west) * globals.one_over_dx;
-    let dQdy = (yflux_here - yflux_south) * globals.one_over_dy;
+   // let dQdx = 0.5 * (Q_east - Q_west) * globals.one_over_dx;
+   // let dQdy = (yflux_here - yflux_south) * globals.one_over_dy;
 
     let B_here = textureLoad(txBottom, idx, 0).z;
     let eta_here = textureLoad(txState, idx, 0).x;
```

#### CT1-218 쇄파 점성 상한의 길이척도

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass_Breaking.wgsl:122; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass_Breaking.wgsl:124; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 점성 상한을 dx*dx/dt로 둔다. 본판은 dx*dy/dt다. 둘 다 길이제곱/시간 단위다. dx==dy일 때만 수치가 같다. 독립 단면의 x 격자 척도를 쓰는 의도된 단순화다. |

본판 차이 줄의 마지막 수정: `366ee34` 2024-04-08 (현재 125행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 128행 포함).

```diff
@@ -122,7 +124,8 @@
          if(t_here <= globals.dt) {t_here = globals.total_time;}
     }
 
-    let nu_breaking = min(1.0 * globals.dx * globals.dy / globals.dt, B_Breaking * globals.delta_breaking * h_here * detadt);
+   // let nu_breaking = min(1.0 * globals.dx * globals.dy / globals.dt, B_Breaking * globals.delta_breaking * h_here * detadt);
+    let nu_breaking = min(1.0 * globals.dx * globals.dx / globals.dt, B_Breaking * globals.delta_breaking * h_here * detadt);
 
     // Smagorinsky subgrid eddy viscosity
     let Smag_cm = 0.04;
```

#### CT1-219 쇄파 응력 출력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Pass_Breaking.wgsl:132; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Pass_Breaking.wgsl:135; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 nu_dPdx만 첫 채널에 저장한다. 나머지 응력 채널은 0.0이다. |

본판 차이 줄의 마지막 수정: `366ee34` 2024-04-08 (현재 140행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 144행 포함).

```diff
@@ -132,12 +135,13 @@
     let nu_total = nu_breaking + nu_Smag;
 
     let nu_dPdx = nu_total * dPdx;
-    let nu_dPdy = nu_total * dPdy;
+   // let nu_dPdy = nu_total * dPdy;
 
-    let nu_dQdx = nu_total * dQdx;
-    let nu_dQdy = nu_total * dQdy;
+   // let nu_dQdx = nu_total * dQdx;
+   // let nu_dQdy = nu_total * dQdy;
 
-    let nu_flux = vec4<f32>(nu_dPdx, nu_dPdy, nu_dQdx, nu_dQdy);
+   // let nu_flux = vec4<f32>(nu_dPdx, nu_dPdy, nu_dQdx, nu_dQdy);
+    let nu_flux = vec4<f32>(nu_dPdx, 0.0, 0.0, 0.0);
     let Bvalues = vec4<f32>(t_here, nu_breaking, B_Breaking, nu_Smag);
 
     textureStore(txDissipationFlux, idx, nu_flux);
```


### 2.36 shaders/SedTrans_Pass1.wgsl

본판: `shaders/SedTrans_Pass1.wgsl`. transect 판: `transect_version/shaders/SedTrans_Pass1.wgsl`.
원래 diff는 273행이다. CR 제외 diff는 1구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `7fa28e0` | 2025-06-12 | bug fixes |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-220 퇴적물 limiter

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/SedTrans_Pass1.wgsl:93; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/SedTrans_Pass1.wgsl:93; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 TWO_THETAc=2.0으로 고정한다. transect 판은 wetdry/base_depth의 rampcoef로 globals.TWO_THETA와 2.0을 섞는다. 기본 Theta=2.0이면 충분히 젖은 곳의 값은 4.0까지 간다. x 단면과 무관한 계수 차이다. |

본판 차이 줄의 마지막 수정: `7fa28e0` 2025-06-12 (현재 96행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 96행 포함).

```diff
@@ -93,7 +93,7 @@
     // modify limiters based on whether near the inundation limit
     let wetdry = min(h_here, min(h_south, min(h_north, min(h_west, h_east))));
     let rampcoef = min(max(0.0, wetdry / (0.02 * globals.base_depth)), 1.0);
-    let TWO_THETAc = 2.0; //globals.TWO_THETA * rampcoef + 2.0 * (1.0 - rampcoef);  // transition to full upwinding with overland flow, start transition at base_depth/50.
+    let TWO_THETAc = globals.TWO_THETA * rampcoef + 2.0 * (1.0 - rampcoef);  // transition to full upwinding with overland flow, start transition at base_depth/50.
 
     let c1_wy = Reconstruct(in_west.x, in_here.x, in_east.x, TWO_THETAc);
     let c1_zx = Reconstruct(in_south.x, in_here.x, in_north.x, TWO_THETAc);
```


### 2.37 shaders/SedTrans_Pass3.wgsl

본판: `shaders/SedTrans_Pass3.wgsl`. transect 판: `transect_version/shaders/SedTrans_Pass3.wgsl`.
원래 diff는 384행이다. CR 제외 diff는 5구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `852ec28` | 2025-06-13 | sed trans fixes |
| 본판 | `ba9eb67` | 2025-06-09 | added bedload to bottom update equation |
| 본판 | `e54def4` | 2025-06-08 | Update SedTrans_Pass3.wgsl |
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| 본판 | `2a7452d` | 2025-06-07 | Sed Trans updates |
| 본판 | `5c60ac0` | 2025-06-07 | add sediment diffusion term |
| 본판 | `a435dd4` | 2025-06-07 | Update SedTrans_Pass3.wgsl |
| 본판 | `fa47b72` | 2025-06-06 | Sed Trans Updates |
| 본판 | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-221 퇴적물 closure uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/SedTrans_Pass3.wgsl:19; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:19; 아래 전체 diff의 +행 | 불일치 (A) | transect 판에는 base_depth·delta·확산계수·MPM 계수가 없다. 본판의 후속 퇴적물 모델 확장과 연결된다. |

본판 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 23행 포함); `5c60ac0` 2025-06-07 (현재 24행 포함); `b8b50c3` 2025-06-08 (현재 25행 포함); `ba9eb67` 2025-06-09 (현재 26행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -19,11 +19,6 @@
     sedC1_erosion: f32,
     sedC1_n: f32,
     sedC1_fallvel: f32,
-    base_depth: f32,
-    delta: f32,
-    sedTurbDispersion: f32,
-    sedBreakingDispersionCoef: f32,
-    sedC1_bedloadMPM: f32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-222 퇴적물 입력 binding

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/SedTrans_Pass3.wgsl:42; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:37; 아래 전체 diff의 +행 | 불일치 (A) | transect 판에는 쇄파·면속도·면농도·hardbottom 리소스가 없다. |

본판 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 50행 포함); `2a7452d` 2025-06-07 (현재 48행 포함); `b8b50c3` 2025-06-08 (현재 49행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -42,12 +37,6 @@
 @group(0) @binding(11) var erosion_Sed: texture_storage_2d<rgba32float, write>;
 @group(0) @binding(12) var depostion_Sed: texture_storage_2d<rgba32float, write>;
 
-@group(0) @binding(13) var txBreaking: texture_2d<f32>;
-@group(0) @binding(14) var txU: texture_2d<f32>;
-@group(0) @binding(15) var txV: texture_2d<f32>;
-@group(0) @binding(16) var txSed_C1: texture_2d<f32>;
-@group(0) @binding(17) var txHardBottom: texture_2d<f32>;
-
 @compute @workgroup_size(16, 16)
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
```

#### CT1-223 퇴적물 셀 상태 읽기 위치

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/SedTrans_Pass3.wgsl:68; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:57; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 B·eta·hu·hv·h를 앞에서 읽는다. transect 판은 뒤에서 읽는다. 뒤 식에 같은 값이 들어가는 읽기 위치 자체는 동작 차이가 없다. |

본판 차이 줄의 마지막 수정: `2a7452d` 2025-06-07 (현재 78행 포함); `852ec28` 2025-06-13 (현재 77행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -68,14 +57,6 @@
     let downleftIdx = idx + vec2<i32>(-1, -1);
     let downrightIdx = idx + vec2<i32>(1, -1);
 
-    let B = textureLoad(txBottom, idx, 0).z;
-    let in_state_here = textureLoad(txState, idx, 0);
-    let eta = in_state_here.x;
-    let hu = in_state_here.y;
-    let hv = in_state_here.z;
-    let h = eta - B;
-    let C_state_here = textureLoad(txState_Sed, idx, 0);
-
     // Load values from txXFlux and txYFlux using idx
     var xflux_here = textureLoad(txXFlux_Sed, idx, 0);
     var xflux_west = textureLoad(txXFlux_Sed, leftIdx, 0);
```

#### CT1-224 퇴적물 확산과 수심 역수

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/SedTrans_Pass3.wgsl:83; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:64; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 Dxx=Dxy=Dyy=1.0으로 인접 단면과 혼합한다. transect 판은 divide_by_h=2.0*h/sqrt(h2+max(h2,epsilon))를 쓴다. 젖은 곳에서 이 값은 1/h가 아닌 sqrt(2)에 접근한다. hu에 이 값을 곱하면 유속 단위가 맞지 않는다. 마찰의 절반 계수·추가 divide_by_h·hardbottom 검사 없음·bedload 없음·침강 제한식 변경도 같은 hunk에 있다. 본판의 후속 퇴적물 수정 이력을 근거로 E로 둔다. |

본판 차이 줄의 마지막 수정: `e54def4` 2025-06-08 (현재 87행 포함); `b8b50c3` 2025-06-08 (현재 213행 포함); `85c2ca2` 2024-03-19 (현재 214행 포함); `2a7452d` 2025-06-07 (현재 121행 포함); `22e1983` 2025-06-06 (현재 135행 포함); `852ec28` 2025-06-13 (현재 215행 포함); `ba9eb67` 2025-06-09 (현재 210행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 116행 포함).

```diff
@@ -83,136 +64,56 @@
     var yflux_south = textureLoad(txYFlux_Sed, downIdx, 0);
 
     // Calculate scalar transport additions
-    var c4 = textureLoad(txSed_C1, idx, 0);
-    let C_here = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-    //let H_here = h;
-    // c4 = textureLoad(txSed_C1, rightIdx, 0);
-    // let C_right = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-    // let H_right = textureLoad(txState, rightIdx, 0).x - textureLoad(txBottom, rightIdx, 0).z;
-    // c4 = textureLoad(txSed_C1, leftIdx, 0);
-    // let C_left = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-    // let H_left = textureLoad(txState, leftIdx, 0).x - textureLoad(txBottom, leftIdx, 0).z;
-    // c4 = textureLoad(txSed_C1, upIdx, 0);
-    // let C_up = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-    // let H_up = textureLoad(txState, upIdx, 0).x - textureLoad(txBottom, upIdx, 0).z;
-    // c4 = textureLoad(txSed_C1, downIdx, 0);
-    // let C_down = (c4.x + c4.y + c4.z + c4.w) / 4.0;
-    // let H_down = textureLoad(txState, downIdx, 0).x - textureLoad(txBottom, downIdx, 0).z;
-    
-    // let max_Kh = min(10.0, 0.5 * globals.dx * globals.dy / globals.dt);
-    // let Kh_here = min(max_Kh, globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, idx, 0).y);
-    // let Kh_right = min(max_Kh, globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, rightIdx, 0).y);
-    // let Kh_up = min(max_Kh, globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, upIdx, 0).y);
-    // let Kh_left = min(max_Kh, globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, leftIdx, 0).y);
-    // let Kh_down = min(max_Kh, globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, downIdx, 0).y);
-    // let Kh_average = Kh_here; // + 0.125 * (Kh_right + Kh_up + Kh_left + Kh_down); // background nu of 1.0, good for tsunami models
-
-    // let C_xx = globals.one_over_d2x * (C_right - 2.0 * C_here + C_left);
-    // let C_yy = globals.one_over_d2y * (C_up - 2.0 * C_here + C_down);
-    // let C_x  = 0.5 * globals.one_over_dx * (C_right - C_left);
-    // let C_y  = 0.5 * globals.one_over_dy * (C_up - C_down);
-
-    // let Kh_x = 0.5 * globals.one_over_dx * (Kh_right * H_right - Kh_left * H_left);
-    // let Kh_y = 0.5 * globals.one_over_dy * (Kh_up * H_up - Kh_down * H_down);
-
-    // let hc_by_dx_dx = Kh_average * H_here * C_xx + Kh_x * C_x;
-    // let hc_by_dy_dy = Kh_average * H_here * C_yy + Kh_y * C_y;
-
-    // friction
-    let h_scaled = h / globals.base_depth;
-    let h2 = h_scaled * h_scaled;
-    let divide_by_h = 2.0 * h_scaled / (h2 + max(h2, 1.e-6)) / globals.base_depth;
+    let C_state_here = textureLoad(txState_Sed, idx, 0);
+    let C_state_right = textureLoad(txState_Sed, rightIdx, 0);
+    let C_state_left = textureLoad(txState_Sed, leftIdx, 0);
+    let C_state_up = textureLoad(txState_Sed, upIdx, 0);
+    let C_state_down = textureLoad(txState_Sed, downIdx, 0);
+    let C_state_up_left = textureLoad(txState_Sed, upleftIdx, 0);
+    let C_state_up_right = textureLoad(txState_Sed, uprightIdx, 0);
+    let C_state_down_left = textureLoad(txState_Sed, downleftIdx, 0);
+    let C_state_down_right = textureLoad(txState_Sed, downrightIdx, 0);
+
+    let Dxx = 1.0;
+    let Dxy = 1.0;
+    let Dyy = 1.0;
+
+    let hc_by_dx_dx = Dxx * globals.one_over_d2x * (C_state_right - 2.0 * C_state_here + C_state_left);
+    let hc_by_dy_dy = Dyy * globals.one_over_d2y * (C_state_up - 2.0 * C_state_here + C_state_down);
+    let hc_by_dx_dy = Dxy * globals.one_over_dxdy * (C_state_up_right - C_state_up_left - C_state_down_right + C_state_down_left) / 4.0;
+
+    let B = textureLoad(txBottom, idx, 0).z;
+    let in_state_here = textureLoad(txState, idx, 0);
+    let eta = in_state_here.x;
+    let hu = in_state_here.y;
+    let hv = in_state_here.z;
+    let h = eta - B;
+
+    let h2 = h * h;
+    let divide_by_h = 2.0 * h / sqrt(h2 + max(h2, globals.epsilon));
 
     var f: f32;
     if (globals.isManning == 1) {
         f = 9.81 * pow(globals.friction, 2.0) * pow(abs(divide_by_h), 1.0 / 3.0);
     } else {
-        f = globals.friction;
+        f = globals.friction / 2.0;
     }
 
-    // u, v here
-    var u4 = textureLoad(txU, idx, 0);
-    var v4 = textureLoad(txV, idx, 0);
-    let u_here = (u4.x + u4.y + u4.z + u4.w) / 4.0;
-    let v_here = (v4.x + v4.y + v4.z + v4.w) / 4.0;
-    let local_speed = sqrt(u_here * u_here + v_here * v_here);
+    let u = hu * divide_by_h;
+    let v = hv * divide_by_h;
+    let local_speed = sqrt(u * u + v * v);
     let shear_velocity = sqrt(f) * local_speed;
     let shields = shear_velocity * shear_velocity * globals.sedC1_shields;
 
     var erosion = 0.0;
-    if (shields > globals.sedC1_criticalshields) {
-        erosion = globals.sedC1_erosion * (shields - globals.sedC1_criticalshields) * local_speed;
-        erosion = max(erosion, 0.0);
-    }
-    let hardbottom = textureLoad(txHardBottom, idx, 0).x;
-    let avaliable_depth = B - hardbottom;
-    if (avaliable_depth < globals.delta) {
-        erosion = 0.0;
+    if (shields >= globals.sedC1_criticalshields) {
+        erosion = globals.sedC1_erosion * (shields - globals.sedC1_criticalshields) * local_speed * divide_by_h;
     }
 
-    // add Bed load MP&M
-    var bedload_erosion = 0.0;
-    if (shields > globals.sedC1_criticalshields) {
-        u4 = textureLoad(txU, leftIdx, 0);
-        v4 = textureLoad(txV, leftIdx, 0);
-        let u_left = (u4.x + u4.y + u4.z + u4.w) / 4.0;
-        let v_left = (v4.x + v4.y + v4.z + v4.w) / 4.0;
-        let local_speed_left = sqrt(u_left * u_left + v_left * v_left);
-        let shear_velocity_left = sqrt(f) * local_speed_left;
-        let shields_left = shear_velocity_left * shear_velocity_left * globals.sedC1_shields;
-        var bedload_left_X = 0.0;
-        if (shields_left > globals.sedC1_criticalshields) {
-            let bedload_left = globals.sedC1_bedloadMPM * pow(shields_left - globals.sedC1_criticalshields, 1.5);
-            bedload_left_X = bedload_left * u_left / local_speed_left;
-        }
-
-        u4 = textureLoad(txU, rightIdx, 0);
-        v4 = textureLoad(txV, rightIdx, 0);
-        let u_right = (u4.x + u4.y + u4.z + u4.w) / 4.0;
-        let v_right = (v4.x + v4.y + v4.z + v4.w) / 4.0;
-        let local_speed_right = sqrt(u_right * u_right + v_right * v_right);
-        let shear_velocity_right = sqrt(f) * local_speed_right;
-        let shields_right = shear_velocity_right * shear_velocity_right * globals.sedC1_shields;
-        var bedload_right_X = 0.0;
-        if (shields_right > globals.sedC1_criticalshields) {
-            let bedload_right = globals.sedC1_bedloadMPM * pow(shields_right - globals.sedC1_criticalshields, 1.5);
-            bedload_right_X = bedload_right * u_right / local_speed_right;
-        }
-
-        u4 = textureLoad(txU, upIdx, 0);
-        v4 = textureLoad(txV, upIdx, 0);
-        let u_up = (u4.x + u4.y + u4.z + u4.w) / 4.0;
-        let v_up = (v4.x + v4.y + v4.z + v4.w) / 4.0;
-        let local_speed_up = sqrt(u_up * u_up + v_up * v_up);
-        let shear_velocity_up = sqrt(f) * local_speed_up;
-        let shields_up = shear_velocity_up * shear_velocity_up * globals.sedC1_shields;
-        var bedload_up_Y = 0.0;
-        if (shields_up > globals.sedC1_criticalshields) {
-            let bedload_up = globals.sedC1_bedloadMPM * pow(shields_up - globals.sedC1_criticalshields, 1.5);
-            bedload_up_Y = bedload_up * v_up / local_speed_up;
-        }
-
-        u4 = textureLoad(txU, downIdx, 0);
-        v4 = textureLoad(txV, downIdx, 0);
-        let u_down = (u4.x + u4.y + u4.z + u4.w) / 4.0;
-        let v_down = (v4.x + v4.y + v4.z + v4.w) / 4.0;
-        let local_speed_down = sqrt(u_down * u_down + v_down * v_down);
-        let shear_velocity_down = sqrt(f) * local_speed_down;
-        let shields_down = shear_velocity_down * shear_velocity_down * globals.sedC1_shields;
-        var bedload_down_Y = 0.0;
-        if (shields_down > globals.sedC1_criticalshields) {
-            let bedload_down = globals.sedC1_bedloadMPM * pow(shields_down - globals.sedC1_criticalshields, 1.5);
-            bedload_down_Y = bedload_down * v_down / local_speed_down;
-        }
-        
-        // calc bedload gradients, to be used only by bed upload equation
-        bedload_erosion = 0.5 * globals.one_over_dx * (bedload_right_X - bedload_left_X) + 0.5 * globals.one_over_dy * (bedload_up_Y - bedload_down_Y);
-    }
+    let Cmin = max(1.0e-6, C_state_here.x);   // only for C1 right now
+    let deposition = min(2.0, (1.0 - globals.sedC1_n) / Cmin) * C_state_here.x * globals.sedC1_fallvel;
 
-    var deposition = min(2.0 * C_state_here.x, h * (1.0 - globals.sedC1_n)) * globals.sedC1_fallvel;
-    deposition = max(deposition, 0.0);
-
-    let source_term = (erosion - deposition) * divide_by_h;  // do not add bedload here, since this is only for suspended load
+    let source_term = hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + erosion - deposition;
 
     let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term;
```

#### CT1-225 퇴적물 비음수 보정과 바닥 전달

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/SedTrans_Pass3.wgsl:232; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:133; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 newState를 0 이상으로 제한한다. transect 판은 해당 제한이 없다. 본판은 침식·침강을 역수심으로 변환하고 침식 출력에 bedload 발산을 더한다. transect 판은 직접 erosion/deposition을 저장한다. E의 핵심은 서로 다른 수심 정규화와 한쪽 농도 보정 수정이다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 236행 포함); `852ec28` 2025-06-13 (현재 240행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 139행 포함).

```diff
@@ -232,10 +133,8 @@
         newState = C_state_here + globals.dt / 24.0 * (9.0 * d_by_dt + 19.0 * predicted - 5.0 * oldies + oldOldies);
     }
 
-    newState = max(newState, vec4<f32>(0.0, 0.0, 0.0, 0.0)); // ensure no negative concentrations
-
     textureStore(txNewState_Sed, idx, newState);
     textureStore(dU_by_dt_Sed, idx, d_by_dt);
-    textureStore(erosion_Sed, idx, vec4<f32>(erosion * divide_by_h + bedload_erosion, 0.0, 0.0, 0.0));  // add bedload here, which is used for bed update
-    textureStore(depostion_Sed, idx, vec4<f32>(deposition * divide_by_h, 0.0, 0.0, 0.0));
+    textureStore(erosion_Sed, idx, vec4<f32>(erosion, 0.0, 0.0, 0.0));
+    textureStore(depostion_Sed, idx, vec4<f32>(deposition, 0.0, 0.0, 0.0));
 }
\ No newline at end of file
```


### 2.38 shaders/SedTrans_UpdateBottom.wgsl

본판: `shaders/SedTrans_UpdateBottom.wgsl`. transect 판: `transect_version/shaders/SedTrans_UpdateBottom.wgsl`.
원래 diff는 177행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `852ec28` | 2025-06-13 | sed trans fixes |
| 본판 | `4353b85` | 2025-06-09 | Sed bugs / corrections |
| 본판 | `a98bcc4` | 2025-06-09 | sed trans updates |
| 본판 | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-226 지형 갱신 경계 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/SedTrans_UpdateBottom.wgsl:8; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/SedTrans_UpdateBottom.wgsl:8; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 4변 경계 유형을 받아 입사 경계의 지형변화를 ramp로 억제한다. |

본판 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 14행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -8,10 +8,6 @@
     timeScheme: i32,
     pred_or_corrector: i32,
     sedC1_n: f32,
-    west_boundary_type: i32,
-    east_boundary_type: i32,
-    south_boundary_type: i32,
-    north_boundary_type: i32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-227 진단 전용 지형변화 입력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/SedTrans_UpdateBottom.wgsl:22; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/SedTrans_UpdateBottom.wgsl:18; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 hardbottom·초기 바닥고·외곽 셀 조기 반환을 쓰지 않는다. 북쪽·동쪽 이웃으로 진단 면 변화량을 계산한다. HTML의 no feedback 안내와 연결된다. |

본판 차이 줄의 마지막 수정: `852ec28` 2025-06-13 (현재 50행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 31행 포함).

```diff
@@ -22,33 +18,17 @@
 @group(0) @binding(4) var depostion_Sed: texture_2d<f32>; 
 @group(0) @binding(5) var txtemp_SedTrans_Botttom: texture_storage_2d<rgba32float, write>;
 @group(0) @binding(6) var txtemp_SedTrans_Change: texture_storage_2d<rgba32float, write>;
-@group(0) @binding(7) var txHardBottom: texture_2d<f32>;
-@group(0) @binding(8) var txBottomInitial: texture_2d<f32>;
 
 
 @compute @workgroup_size(16, 16)
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
 
-    var dB_cumulative = textureLoad(txBotChange_Sed, idx, 0);
-    var B_here = textureLoad(txBottom, idx, 0);
-
-    if (idx.x >= globals.width - 2 || idx.y >= globals.height - 2 || idx.x <= 1 || idx.y <= 1) {
-        textureStore(txtemp_SedTrans_Botttom, idx, B_here);
-        textureStore(txtemp_SedTrans_Change, idx, dB_cumulative);
-        return;
-    }
-
-    let leftIdx = idx + vec2<i32>(-1, 0);
     let rightIdx = idx + vec2<i32>(1, 0);
-    let downIdx = idx + vec2<i32>(0, -1);
     let upIdx = idx + vec2<i32>(0, 1);
-    let rightrightIdX = idx + vec2<i32>(2, 0);
-    let rightupIdx = idx + vec2<i32>(1, 1);
-    let rightdownIdx = idx + vec2<i32>(1, -1);
-    let upupIdx = idx + vec2<i32>(0, 2);
-    let leftupIdx = idx + vec2<i32>(-1, 1);
 
+    var dB_cumulative = textureLoad(txBotChange_Sed, idx, 0);
+    var B_here = textureLoad(txBottom, idx, 0);
     let min_val = -globals.base_depth;
 
     let e_here =  textureLoad(erosion_Sed, idx, 0).x;
```

#### CT1-228 바닥고 고정과 누적 변화량

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/SedTrans_UpdateBottom.wgsl:57; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/SedTrans_UpdateBottom.wgsl:37; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 B_here=B_here로 현재 바닥고를 유지한다. 진단 누적값에는 -dB를 적산한다. 본판은 B_here-dB를 수리에 돌려주고 초기 바닥고와의 차이로 누적량을 만든다. 의도 근거가 있으므로 바닥고 고정 자체를 결함으로 판정하지 않는다. 동쪽 면 평균은 본판이 0.75*현재+0.25*이웃인 데 비해 transect는 0.5*현재+0.5*이웃이다. |

본판 차이 줄의 마지막 수정: `852ec28` 2025-06-13 (현재 119행 포함); `85c2ca2` 2024-03-19 (현재 87행 포함); `22e1983` 2025-06-06 (현재 106행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 49행 포함).

```diff
@@ -57,66 +37,16 @@
     let d_right =  textureLoad(depostion_Sed, rightIdx, 0).x;
     let e_up =  textureLoad(erosion_Sed, upIdx, 0).x;
     let d_up =  textureLoad(depostion_Sed, upIdx, 0).x;
-    let e_left =  textureLoad(erosion_Sed, leftIdx, 0).x;
-    let d_left =  textureLoad(depostion_Sed, leftIdx, 0).x;
-    let e_down =  textureLoad(erosion_Sed, downIdx, 0).x;
-    let d_down =  textureLoad(depostion_Sed, downIdx, 0).x;
-    let e_rightright =  textureLoad(erosion_Sed, rightrightIdX, 0).x;
-    let d_rightright =  textureLoad(depostion_Sed, rightrightIdX, 0).x;
-    let e_rightup =  textureLoad(erosion_Sed, rightupIdx, 0).x;
-    let d_rightup =  textureLoad(depostion_Sed, rightupIdx, 0).x;
-    let e_rightdown =  textureLoad(erosion_Sed, rightdownIdx, 0).x;
-    let d_rightdown =  textureLoad(depostion_Sed, rightdownIdx, 0).x;
-    let e_upup =  textureLoad(erosion_Sed, upupIdx, 0).x;
-    let d_upup =  textureLoad(depostion_Sed, upupIdx, 0).x;
-    let e_leftup =  textureLoad(erosion_Sed, leftupIdx, 0).x;
-    let d_leftup =  textureLoad(depostion_Sed, leftupIdx, 0).x;
-
-    let e_here_average = e_here; //0.25 * (e_right + e_left + e_up + e_down);
-    let d_here_average = d_here; //0.25 * (d_right + d_left + d_up + d_down);
-
-    let e_right_average = 0.5 * (e_right + e_here);
-    let d_right_average = 0.5 * (d_right + d_here);
-
-    let e_up_average = 0.5 * (e_up + e_here);;
-    let d_up_average = 0.5 * (d_up + d_here);
-
-    let dB_here = globals.dt * (e_here_average - d_here_average) / (1.0 - globals.sedC1_n); // this is positive when eroding - when increasing depth, or decreasing elevation
-    let dB_right = 0.5 * ( dB_here +  globals.dt * (e_right_average - d_right_average) / (1.0 - globals.sedC1_n));
-    let dB_up =    0.5 * ( dB_here +  globals.dt * (e_up_average - d_up_average) / (1.0 - globals.sedC1_n));
-
-    var dB = vec4<f32>(dB_up, dB_right, dB_here, 0.0);
-
-    if (globals.west_boundary_type == 2 && idx.x < 10) {
-        let ramp = max(0.0, (f32(idx.x)-5.0) / 5.0);  // Linear ramp from 0 to 1 over the first 10 columns
-        dB = ramp * dB;  // No sediment transport in the first 20 columns
-    }
-    if (globals.east_boundary_type == 2 && idx.x > globals.width - 11) {
-        let ramp = max(0.0, (f32(globals.width - idx.x) - 5.0) / 5.0);  // Linear ramp from 0 to 1 over the last 10 columns
-        dB = ramp * dB;  // No sediment transport in the last 20 columns    
-    }
-    if (globals.south_boundary_type == 2 && idx.y < 10) {
-        let ramp = max(0.0, (f32(idx.y)-5.0) / 5.0);  // Linear ramp from 0 to 1 over the first 10 rows
-        dB = ramp * dB;  // No sediment transport in the first 20 rows
-    }
-    if (globals.north_boundary_type == 2 && idx.y > globals.height - 11) {
-        let ramp = max(0.0, (f32(globals.height - idx.y) - 5.0) / 5.0);  // Linear ramp from 0 to 1 over the last 10 rows
-        dB = ramp * dB;  // No sediment transport in the last 20 rows    
-    }
-
-    // create harbottom vec4, j+1/2, i+1/2, here, 0
-    let B_hardbottom_here = textureLoad(txHardBottom, idx, 0).x;
-    let B_hardbottom = vec4<f32>(
-        0.5 * (B_hardbottom_here + textureLoad(txHardBottom, upIdx, 0).x),
-        0.5 * (B_hardbottom_here + textureLoad(txHardBottom, rightIdx, 0).x),
-        B_hardbottom_here,
-        0.0
-    );
-    let B_new = B_here - dB;  // B is elevation, so a positive dB (eroding) should decrease the elevation
-    //dB = B_here - B_new;  // dB is the change in elevation, so it should be negative when eroding
-    dB_cumulative = B_new - textureLoad(txBottomInitial, idx, 0); // update cumulative change in bottom elevation
 
-    textureStore(txtemp_SedTrans_Botttom, idx, B_new);
+    let dB_here = globals.dt * (e_here - d_here) / (1.0 - globals.sedC1_n); // this is positive when eroding - when increasing depth, or decreasing elevation
+    let dB_right = 0.5 * ( dB_here +  globals.dt * (e_right - d_right) / (1.0 - globals.sedC1_n));
+    let dB_up =    0.5 * ( dB_here +  globals.dt * (e_up - d_up) / (1.0 - globals.sedC1_n));
+
+    let dB = vec4<f32>(dB_up, dB_right, dB_here, 0.0);
+    B_here = B_here; // - dB;  // B is elevation, so a positive dB (eroding) should decrease the elevation
+    dB_cumulative = dB_cumulative - dB;
+
+    textureStore(txtemp_SedTrans_Botttom, idx, B_here);
     textureStore(txtemp_SedTrans_Change, idx, dB_cumulative);
 }
```


### 2.39 shaders/TriDiag_PCRx.wgsl

본판: `shaders/TriDiag_PCRx.wgsl`. transect 판: `transect_version/shaders/TriDiag_PCRx.wgsl`.
원래 diff는 196행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `984091f` | 2026-05-24 | Markdown and PCR ping-pong updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-229 PCR 최종 반복 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/TriDiag_PCRx.wgsl:3; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/TriDiag_PCRx.wgsl:3; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 P를 받아 최종 반복에서만 상태를 저장한다. transect 판은 모든 반복에서 저장한다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 7행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -3,8 +3,6 @@
     height: i32,
     p: i32,
     s: i32,
-    // CODEX: Total PCR iteration count; JS already writes this uniform after s.
-    P: i32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-230 PCR 상태 읽기 위치

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/TriDiag_PCRx.wgsl:19; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/TriDiag_PCRx.wgsl:17; 아래 전체 diff의 +행 | 불일치 (F) | 본판은 최종 반복에서만 상태를 읽는다. transect 판은 반복마다 읽는다. 최종 반복에 쓰는 상태와 PCR 점화식은 같다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 23행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 20행 포함).

```diff
@@ -19,8 +17,7 @@
 @compute @workgroup_size(16, 16)
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
-    // CODEX: CurrentState is only needed on the final PCR pass now.
-    // let CurrentState = textureLoad(current_state, idx, 0);
+    let CurrentState = textureLoad(current_state, idx, 0);
     
     let s = (globals.s);
     let width = (globals.width);
```

#### CT1-231 PCR 중간 상태 저장

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/TriDiag_PCRx.wgsl:92; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/TriDiag_PCRx.wgsl:89; 아래 전체 diff의 +행 | 불일치 (F) | 본판은 p==P-1일 때만 txtemp2를 쓴다. transect 판은 반복마다 쓴다. 최종 반복 뒤의 상태 복사 결과는 같다. y 셰이더는 transect 실행 경로에서 호출되지 않는다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 103행 포함); `63a12e3` 2023-10-19 (현재 105행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 95행 포함).

```diff
@@ -92,16 +89,9 @@
     let dOut = r * (dIn - aIn * dInLeft - cIn * dInRight);
     
     let txtemp_out = vec4<f32>(aOut, 1.0, cOut, dOut);
-    // let txtemp2_out = vec4<f32>(CurrentState.r, dOut, CurrentState.b, CurrentState.a);
+    let txtemp2_out = vec4<f32>(CurrentState.r, dOut, CurrentState.b, CurrentState.a);
 
     textureStore(txtemp, idx,  txtemp_out);
-    // textureStore(txtemp2, idx, txtemp2_out);
-
-    // CODEX: Only the final PCR pass writes the solved x-momentum back to the state staging texture.
-    if (globals.p == globals.P - 1) {
-        let CurrentState = textureLoad(current_state, idx, 0);
-        let txtemp2_out = vec4<f32>(CurrentState.r, dOut, CurrentState.b, CurrentState.a);
-        textureStore(txtemp2, idx, txtemp2_out);
-    }
+    textureStore(txtemp2, idx, txtemp2_out);
 }
```


### 2.40 shaders/TriDiag_PCRx_COULWAVE.wgsl

본판: `shaders/TriDiag_PCRx_COULWAVE.wgsl`. transect 판: `transect_version/shaders/TriDiag_PCRx_COULWAVE.wgsl`.
원래 diff는 40행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `984091f` | 2026-05-24 | Markdown and PCR ping-pong updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-232 COULWAVE PCR 상태 읽기

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/TriDiag_PCRx_COULWAVE.wgsl:21; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/TriDiag_PCRx_COULWAVE.wgsl:21; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 모든 반복에서 CurrentState를 읽는다. 본판은 최종 반복에서 읽는다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 25행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 24행 포함).

```diff
@@ -21,8 +21,7 @@
 @compute @workgroup_size(16, 16)
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
-    // CODEX: CurrentState is only needed on the final PCR pass now.
-    // let CurrentState = textureLoad(current_state, idx, 0);
+    let CurrentState = textureLoad(current_state, idx, 0);
     
     let s = (globals.s);
     let width = (globals.width);
```

#### CT1-233 COULWAVE PCR 최종 환산

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/TriDiag_PCRx_COULWAVE.wgsl:93; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/TriDiag_PCRx_COULWAVE.wgsl:92; 아래 전체 diff의 +행 | 불일치 (F) | 양쪽은 최종 반복에서 dOut에 H_loc를 곱해 속도를 운동량으로 환산한다. transect 판은 모든 반복에서 상태 staging을 쓴다. 본판은 최종 반복에서만 쓴다. 최종 결과식은 같다. y 셰이더는 transect 실행 경로에서 호출되지 않는다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 114행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 104행 포함).

```diff
@@ -93,24 +92,15 @@
     let cOut = -r * cIn * cInRight;
     var dOut = r * (dIn - aIn * dInLeft - cIn * dInRight);
     
-    // if(globals.p == globals.Px - 1) {  // for COULWAVE need to convert velocity back to flux
-    //     let H_loc = max(globals.delta, CurrentState.r - textureLoad(txBottom, idx, 0).z);
-    //     dOut = dOut * H_loc;
-    // }
-
-    // CODEX: Only the final PCR pass converts velocity back to flux and writes solved x-momentum.
-    if(globals.p == globals.Px - 1) {
-        let CurrentState = textureLoad(current_state, idx, 0);
+    if(globals.p == globals.Px - 1) {  // for COULWAVE need to convert velocity back to flux
         let H_loc = max(globals.delta, CurrentState.r - textureLoad(txBottom, idx, 0).z);
         dOut = dOut * H_loc;
-        let txtemp2_out = vec4<f32>(CurrentState.r, dOut, CurrentState.b, CurrentState.a);
-        textureStore(txtemp2, idx, txtemp2_out);
     }
 
     let txtemp_out = vec4<f32>(aOut, 1.0, cOut, dOut);
-    // let txtemp2_out = vec4<f32>(CurrentState.r, dOut, CurrentState.b, CurrentState.a);
+    let txtemp2_out = vec4<f32>(CurrentState.r, dOut, CurrentState.b, CurrentState.a);
 
     textureStore(txtemp, idx,  txtemp_out);
-    // textureStore(txtemp2, idx, txtemp2_out);
+    textureStore(txtemp2, idx, txtemp2_out);
 }
```


### 2.41 shaders/TriDiag_PCRy.wgsl

본판: `shaders/TriDiag_PCRy.wgsl`. transect 판: `transect_version/shaders/TriDiag_PCRy.wgsl`.
원래 diff는 196행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `984091f` | 2026-05-24 | Markdown and PCR ping-pong updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-234 PCR 최종 반복 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/TriDiag_PCRy.wgsl:3; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/TriDiag_PCRy.wgsl:3; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 P를 받아 최종 반복에서만 상태를 저장한다. transect 판은 모든 반복에서 저장한다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 7행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -3,8 +3,6 @@
     height: i32,
     p: i32,
     s: i32,
-    // CODEX: Total PCR iteration count; JS already writes this uniform after s.
-    P: i32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-235 PCR 상태 읽기 위치

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/TriDiag_PCRy.wgsl:19; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/TriDiag_PCRy.wgsl:17; 아래 전체 diff의 +행 | 불일치 (F) | 본판은 최종 반복에서만 상태를 읽는다. transect 판은 반복마다 읽는다. 최종 반복에 쓰는 상태와 PCR 점화식은 같다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 23행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 20행 포함).

```diff
@@ -19,8 +17,7 @@
 @compute @workgroup_size(16, 16)
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
-    // CODEX: CurrentState is only needed on the final PCR pass now.
-    // let CurrentState = textureLoad(current_state, idx, 0);
+    let CurrentState = textureLoad(current_state, idx, 0);
     
     let s = (globals.s);
     let width = (globals.width);
```

#### CT1-236 PCR 중간 상태 저장

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/TriDiag_PCRy.wgsl:92; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/TriDiag_PCRy.wgsl:89; 아래 전체 diff의 +행 | 불일치 (F) | 본판은 p==P-1일 때만 txtemp2를 쓴다. transect 판은 반복마다 쓴다. 최종 반복 뒤의 상태 복사 결과는 같다. y 셰이더는 transect 실행 경로에서 호출되지 않는다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 105행 포함); `63a12e3` 2023-10-19 (현재 104행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 95행 포함).

```diff
@@ -92,17 +89,10 @@
     let dOut = r * (dIn - aIn * dInLeft - cIn * dInRight);
     
     let txtemp_out = vec4<f32>(aOut, 1.0, cOut, dOut);
-    // let txtemp2_out = vec4<f32>(CurrentState.r, CurrentState.g, dOut, CurrentState.a);
+    let txtemp2_out = vec4<f32>(CurrentState.r, CurrentState.g, dOut, CurrentState.a);
 
     textureStore(txtemp, idx,  txtemp_out);
-    // textureStore(txtemp2, idx, txtemp2_out);
-
-    // CODEX: Only the final PCR pass writes the solved y-momentum back to the state staging texture.
-    if (globals.p == globals.P - 1) {
-        let CurrentState = textureLoad(current_state, idx, 0);
-        let txtemp2_out = vec4<f32>(CurrentState.r, CurrentState.g, dOut, CurrentState.a);
-        textureStore(txtemp2, idx, txtemp2_out);
-    }
+    textureStore(txtemp2, idx, txtemp2_out);
```


### 2.42 shaders/TriDiag_PCRy_COULWAVE.wgsl

본판: `shaders/TriDiag_PCRy_COULWAVE.wgsl`. transect 판: `transect_version/shaders/TriDiag_PCRy_COULWAVE.wgsl`.
원래 diff는 41행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `984091f` | 2026-05-24 | Markdown and PCR ping-pong updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-237 COULWAVE PCR 상태 읽기

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/TriDiag_PCRy_COULWAVE.wgsl:21; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/TriDiag_PCRy_COULWAVE.wgsl:21; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 모든 반복에서 CurrentState를 읽는다. 본판은 최종 반복에서 읽는다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 25행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 24행 포함).

```diff
@@ -21,8 +21,7 @@
 @compute @workgroup_size(16, 16)
 fn main(@builtin(global_invocation_id) id: vec3<u32>) {
     let idx = vec2<i32>(i32(id.x), i32(id.y));
-    // CODEX: CurrentState is only needed on the final PCR pass now.
-    // let CurrentState = textureLoad(current_state, idx, 0);
+    let CurrentState = textureLoad(current_state, idx, 0);
     
     let s = (globals.s);
     let width = (globals.width);
```

#### CT1-238 COULWAVE PCR 최종 환산

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/TriDiag_PCRy_COULWAVE.wgsl:93; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/TriDiag_PCRy_COULWAVE.wgsl:92; 아래 전체 diff의 +행 | 불일치 (F) | 양쪽은 최종 반복에서 dOut에 H_loc를 곱해 속도를 운동량으로 환산한다. transect 판은 모든 반복에서 상태 staging을 쓴다. 본판은 최종 반복에서만 쓴다. 최종 결과식은 같다. y 셰이더는 transect 실행 경로에서 호출되지 않는다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 114행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 104행 포함).

```diff
@@ -93,25 +92,16 @@
     let cOut = -r * cIn * cInRight;
     var dOut = r * (dIn - aIn * dInLeft - cIn * dInRight);
     
-    // if(globals.p == globals.Py - 1) {  // for COULWAVE need to convert velocity back to flux
-    //     let H_loc = max(globals.delta, CurrentState.r - textureLoad(txBottom, idx, 0).z);
-    //     dOut = dOut * H_loc;
-    // }
-
-    // CODEX: Only the final PCR pass converts velocity back to flux and writes solved y-momentum.
-    if(globals.p == globals.Py - 1) {
-        let CurrentState = textureLoad(current_state, idx, 0);
+    if(globals.p == globals.Py - 1) {  // for COULWAVE need to convert velocity back to flux
         let H_loc = max(globals.delta, CurrentState.r - textureLoad(txBottom, idx, 0).z);
         dOut = dOut * H_loc;
-        let txtemp2_out = vec4<f32>(CurrentState.r, CurrentState.g, dOut, CurrentState.a);
-        textureStore(txtemp2, idx, txtemp2_out);
     }
 
     let txtemp_out = vec4<f32>(aOut, 1.0, cOut, dOut);
-    // let txtemp2_out = vec4<f32>(CurrentState.r, CurrentState.g, dOut, CurrentState.a);
+    let txtemp2_out = vec4<f32>(CurrentState.r, CurrentState.g, dOut, CurrentState.a);
 
     textureStore(txtemp, idx,  txtemp_out);
-    // textureStore(txtemp2, idx, txtemp2_out);
+    textureStore(txtemp2, idx, txtemp2_out);
```


### 2.43 shaders/Update_TriDiag_coef.wgsl

본판: `shaders/Update_TriDiag_coef.wgsl`. transect 판: `transect_version/shaders/Update_TriDiag_coef.wgsl`.
원래 diff는 225행이다. CR 제외 diff는 3구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `d23dfb0` | 2025-09-01 | Small fixes |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-239 Boussinesq near-dry 차단 불일치

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Update_TriDiag_coef.wgsl:23; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Update_TriDiag_coef.wgsl:23; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 near_dry를 txBottom.w 대신 d_here로 둔다. 같은 판 Pass3_Bous는 txBottom.w>0일 때만 분산 source를 더한다. 해석: 해안 근처에서 명시 분산 source 차단과 암시 계수 차단이 달라질 수 있다. 자기 주석과 다른 분산 경로의 모순을 중간으로 둔다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 31행 포함); `d23dfb0` 2025-09-01 (현재 34행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 34행 포함).

```diff
@@ -23,15 +23,15 @@
     let idx = vec2<i32>(i32(id.x), i32(id.y));
 
     let width = i32(globals.width);
-    let height = i32(globals.height);
+   // let height = i32(globals.height);
 
     let leftIdx = idx + vec2<i32>(-1, 0);
     let rightIdx = idx + vec2<i32>(1, 0);
-    let downIdx = idx + vec2<i32>(0, -1);
-    let upIdx = idx + vec2<i32>(0, 1);
+   // let downIdx = idx + vec2<i32>(0, -1);
+   // let upIdx = idx + vec2<i32>(0, 1);
 
     let d_here = -textureLoad(txBottom, idx, 0).z;
-    let near_dry = textureLoad(txBottom, idx, 0).w;
+    let near_dry = d_here; //textureLoad(txBottom, idx, 0).w;
 
     var a = 0.0;
     var b = 1.0;
```

#### CT1-240 표준 계수 파일의 COULWAVE 대안

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Update_TriDiag_coef.wgsl:51; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Update_TriDiag_coef.wgsl:51; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 표준 파일의 NLSW_or_Bous==2 분기에서 z_loc와 zx_loc를 0.0으로 둔다. 실제 mode 2는 별도 COULWAVE 계수 파일을 fetch한다. 이 변경은 현재 실행 경로에서 호출되지 않는 대안이다. |

본판 차이 줄의 마지막 수정: `d23dfb0` 2025-09-01 (현재 55행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 55행 포함).

```diff
@@ -51,8 +51,8 @@
 
         if (globals.NLSW_or_Bous == 2) {
             // COULWAVE equations
-            let z_loc = textureLoad(current_state, idx, 0).x;
-            let zx_loc = (textureLoad(current_state, rightIdx, 0).x - textureLoad(current_state, leftIdx, 0).x) / globals.dx / 2.;
+            let z_loc = 0.0; //textureLoad(current_state, idx, 0).x;
+            let zx_loc = 0.0; //(textureLoad(current_state, rightIdx, 0).x - textureLoad(current_state, leftIdx, 0).x) / globals.dx / 2.;
             let za = globals.Bous_alpha * d_here;
             let za2 = za * za;
             let zloc2 = z_loc * z_loc;
```

#### CT1-241 Boussinesq y 계수 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Update_TriDiag_coef.wgsl:72; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Update_TriDiag_coef.wgsl:72; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 coefMaty 계산과 저장을 생략한다. y PCR도 실행하지 않는다. |

본판 차이 줄의 마지막 수정: `63a12e3` 2023-10-19 (현재 109행 포함); `85c2ca2` 2024-03-19 (현재 76행 포함); `0b4e990` 2025-05-16 (현재 105행 포함); `d23dfb0` 2025-09-01 (현재 89행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 109행 포함).

```diff
@@ -72,40 +72,40 @@
     coefx = vec4<f32>(a, b, c, 0.0);
 
     // Y-coefs
-    var coefy = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    if (idx.y <= 2 || idx.y >= height - 3 || near_dry < 0.0) {
-        a = 0.0;
-        b = 1.0;
-        c = 0.0;
-    }
-    else {
+   // var coefy = vec4<f32>(0.0, 0.0, 0.0, 0.0);
+   // if (idx.y <= 2 || idx.y >= height - 3 || near_dry < 0.0) {
+   //     a = 0.0;
+   //     b = 1.0;
+   //     c = 0.0;
+   // }
+   // else {
 
-        let d_south = -textureLoad(txBottom, downIdx, 0).z;
-        let d_north = -textureLoad(txBottom, upIdx, 0).z;
+    //    let d_south = -textureLoad(txBottom, downIdx, 0).z;
+    //    let d_north = -textureLoad(txBottom, upIdx, 0).z;
 
-        if (globals.NLSW_or_Bous == 2) {
+    //    if (globals.NLSW_or_Bous == 2) {
             // COULWAVE equations
-            let z_loc = textureLoad(current_state, idx, 0).x;
-            let zx_loc = (textureLoad(current_state, upIdx, 0).x - textureLoad(current_state, downIdx, 0).x) / globals.dy / 2.;
-            let za = globals.Bous_alpha * d_here;
-            let za2 = za * za;
-            let zloc2 = z_loc * z_loc;
-            a =     (za2-zloc2)/2.*globals.one_over_d2y +   (za-z_loc)*d_south*globals.one_over_d2y + zx_loc*(z_loc+d_south)/globals.dy/2.;
-            b = 1.0-(za2-zloc2)*globals.one_over_d2y  - 2.0*(za-z_loc)*d_here*globals.one_over_d2y;
-            c =     (za2-zloc2)/2.*globals.one_over_d2y +   (za-z_loc)*d_north*globals.one_over_d2y - zx_loc*(z_loc+d_north)/globals.dy/2.;
-        } else{
+    //        let z_loc = 0.0; //textureLoad(current_state, idx, 0).x;
+    //        let zx_loc = 0.0; //(textureLoad(current_state, upIdx, 0).x - textureLoad(current_state, downIdx, 0).x) / globals.dy / 2.;
+    //        let za = globals.Bous_alpha * d_here;
+    //        let za2 = za * za;
+    //        let zloc2 = z_loc * z_loc;
+    //        a =     (za2-zloc2)/2.*globals.one_over_d2y +   (za-z_loc)*d_south*globals.one_over_d2y + zx_loc*(z_loc+d_south)/globals.dy/2.;
+    //        b = 1.0-(za2-zloc2)*globals.one_over_d2y  - 2.0*(za-z_loc)*d_here*globals.one_over_d2y;
+    //        c =     (za2-zloc2)/2.*globals.one_over_d2y +   (za-z_loc)*d_north*globals.one_over_d2y - zx_loc*(z_loc+d_north)/globals.dy/2.;
+    //    } else{
             // Calculate the first derivative of the depth
-            let d_dy = (d_north - d_south) / (2.0 * globals.dy);
+    //        let d_dy = (d_north - d_south) / (2.0 * globals.dy);
 
             // Calculate coefficients based on the depth and its derivative
-            a =  d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
-            b = 1.0 + 2.0 * (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
-            c = -d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
-        }
-    }
-    coefy = vec4<f32>(a, b, c, 0.0);
+    //        a =  d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
+    //        b = 1.0 + 2.0 * (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
+    //        c = -d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
+    //    }
+   // }
+   // coefy = vec4<f32>(a, b, c, 0.0);
 
     textureStore(coefMatx, idx, coefx);
-    textureStore(coefMaty, idx, coefy);
+   // textureStore(coefMaty, idx, coefy);
 }
```


### 2.44 shaders/Update_TriDiag_coef_COULWAVE.wgsl

본판: `shaders/Update_TriDiag_coef_COULWAVE.wgsl`. transect 판: `transect_version/shaders/Update_TriDiag_coef_COULWAVE.wgsl`.
원래 diff는 82행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `67ca57c` | 2025-05-22 | Added COULWAVE solver |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-242 COULWAVE 계수 x 이웃

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Update_TriDiag_coef_COULWAVE.wgsl:24; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Update_TriDiag_coef_COULWAVE.wgsl:24; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 y 이웃 변수 선언을 생략한다. 현재 eta와 x 기울기·za·수심을 쓰는 x 계수식은 같다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 32행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 32행 포함).

```diff
@@ -24,12 +24,12 @@
     let idx = vec2<i32>(i32(id.x), i32(id.y));
 
     let width = i32(globals.width);
-    let height = i32(globals.height);
+   // let height = i32(globals.height);
 
     let leftIdx = idx + vec2<i32>(-1, 0);
     let rightIdx = idx + vec2<i32>(1, 0);
-    let downIdx = idx + vec2<i32>(0, -1);
-    let upIdx = idx + vec2<i32>(0, 1);
+   // let downIdx = idx + vec2<i32>(0, -1);
+   // let upIdx = idx + vec2<i32>(0, 1);
 
     let d_here = -textureLoad(txBottom, idx, 0).z;
     let z_loc = textureLoad(current_stateUVstar, idx, 0).x;
```

#### CT1-243 COULWAVE y 계수 생략

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Update_TriDiag_coef_COULWAVE.wgsl:80; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Update_TriDiag_coef_COULWAVE.wgsl:80; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 y 계수와 y RHS 정규화를 계산하지 않는다. y PCR 생략과 일치한다. |

본판 차이 줄의 마지막 수정: `67ca57c` 2025-05-22 (현재 115행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 115행 포함).

```diff
@@ -80,38 +80,38 @@
     coefx = vec4<f32>(a, b, c, d);
 
     // Y-coefs
-    var coefy = vec4<f32>(0.0, 0.0, 0.0, 0.0);
-    let VV_loc = textureLoad(current_stateUVstar, idx, 0).z;
-    d = VV_loc / H_loc;
-    if (idx.y <= 2 || idx.y >= height - 3 || near_dry < globals.delta) {
-        a = 0.0;
-        b = 1.0;
-        c = 0.0;
-    }
-    else {
+   // var coefy = vec4<f32>(0.0, 0.0, 0.0, 0.0);
+   // let VV_loc = textureLoad(current_stateUVstar, idx, 0).z;
+   // d = VV_loc / H_loc;
+   // if (idx.y <= 2 || idx.y >= height - 3 || near_dry < globals.delta) {
+   //     a = 0.0;
+   //     b = 1.0;
+   //     c = 0.0;
+   // }
+   // else {
 
-        let d_south = -textureLoad(txBottom, downIdx, 0).z;
-        let d_north = -textureLoad(txBottom, upIdx, 0).z;
+    //    let d_south = -textureLoad(txBottom, downIdx, 0).z;
+    //    let d_north = -textureLoad(txBottom, upIdx, 0).z;
 
-        if (globals.NLSW_or_Bous == 2) {
+    //    if (globals.NLSW_or_Bous == 2) {
             // COULWAVE equations
-            let zy_loc = (textureLoad(current_stateUVstar, upIdx, 0).x - textureLoad(current_stateUVstar, downIdx, 0).x) / globals.dy / 2.;
-            a =     (za2-zloc2)/2.*globals.one_over_d2y +   (za-z_loc)*d_south*globals.one_over_d2y + zy_loc*(z_loc+d_south)/globals.dy/2.;
-            b = 1.0-(za2-zloc2)*globals.one_over_d2y  - 2.0*(za-z_loc)*d_here*globals.one_over_d2y;
-            c =     (za2-zloc2)/2.*globals.one_over_d2y +   (za-z_loc)*d_north*globals.one_over_d2y - zy_loc*(z_loc+d_north)/globals.dy/2.;
-        } else{
+    //        let zy_loc = (textureLoad(current_stateUVstar, upIdx, 0).x - textureLoad(current_stateUVstar, downIdx, 0).x) / globals.dy / 2.;
+    //        a =     (za2-zloc2)/2.*globals.one_over_d2y +   (za-z_loc)*d_south*globals.one_over_d2y + zy_loc*(z_loc+d_south)/globals.dy/2.;
+    //        b = 1.0-(za2-zloc2)*globals.one_over_d2y  - 2.0*(za-z_loc)*d_here*globals.one_over_d2y;
+    //        c =     (za2-zloc2)/2.*globals.one_over_d2y +   (za-z_loc)*d_north*globals.one_over_d2y - zy_loc*(z_loc+d_north)/globals.dy/2.;
+    //    } else{
             // Calculate the first derivative of the depth
-            let d_dy = (d_north - d_south) / (2.0 * globals.dy);
+    //        let d_dy = (d_north - d_south) / (2.0 * globals.dy);
 
             // Calculate coefficients based on the depth and its derivative
-            a =  d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
-            b = 1.0 + 2.0 * (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
-            c = -d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
-        }
-    }
-    coefy = vec4<f32>(a, b, c, d);
+    //        a =  d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
+    //        b = 1.0 + 2.0 * (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
+    //        c = -d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
+    //    }
+   // }
+   // coefy = vec4<f32>(a, b, c, d);
 
     textureStore(coefMatx, idx, coefx);
-    textureStore(coefMaty, idx, coefy);
+   // textureStore(coefMaty, idx, coefy);
 }
```


### 2.45 shaders/Update_neardry.wgsl

본판: `shaders/Update_neardry.wgsl`. transect 판: `transect_version/shaders/Update_neardry.wgsl`.
원래 diff는 117행이다. CR 제외 diff는 2구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `85c2ca2` | 2024-03-19 | Add files via upload |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-244 near-dry 셰이더 검사

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Update_neardry.wgsl:18; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Update_neardry.wgsl:18; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 ±3칸의 x 이웃만 검사한다. 현재 단면의 y 인덱스는 고정한다. |

본판 차이 줄의 마지막 수정: `85c2ca2` 2024-03-19 (현재 27행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 28행 포함).

```diff
@@ -18,13 +18,14 @@
     // update neardry
     let lengthCheck = 3;    // check within three points
     B_here.w = 99.;
-    for (var yy = idx.y - lengthCheck; yy <= idx.y + lengthCheck; yy += 1) 
-    {
+   // for (var yy = idx.y - lengthCheck; yy <= idx.y + lengthCheck; yy += 1) 
+   // {
         for (var xx = idx.x - lengthCheck; xx <= idx.x + lengthCheck; xx += 1) {
             let xC = min(globals.width - 1, max(0, xx));
-            let yC = min(globals.height - 1, max(0, yy));
+           // let yC = min(globals.height - 1, max(0, yy));
 
-            let idx_C = vec2<i32>(xC, yC);
+           // let idx_C = vec2<i32>(xC, yC);
+            let idx_C = vec2<i32>(xC, idx.y);
             let bathy_C = textureLoad(txBottom, idx_C, 0).z;
             if (bathy_C >= 0.) 
             {
```

#### CT1-245 단일점 섬 보정의 1D 선택

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/Update_neardry.wgsl:32; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/Update_neardry.wgsl:33; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 동·서가 모두 음의 바닥고인 양의 중심 고도를 0으로 만든다. 북·남 면 보정은 하지 않는다. 초기 CPU 단일점 제거는 별도로 꺼져 있다. |

본판 차이 줄의 마지막 수정: `85c2ca2` 2024-03-19 (현재 49행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 51행 포함).

```diff
@@ -32,21 +33,22 @@
             }
                 
         }
-    }
+   // }
 
     // check for single point islands
     let leftIdx = idx + vec2<i32>(-1, 0);
     let rightIdx = idx + vec2<i32>(1, 0);
-    let downIdx = idx + vec2<i32>(0, -1);
-    let upIdx = idx + vec2<i32>(0, 1);
-    let B_south = textureLoad(txBottom, downIdx, 0).z;
-    let B_north = textureLoad(txBottom, upIdx, 0).z;
+   // let downIdx = idx + vec2<i32>(0, -1);
+   // let upIdx = idx + vec2<i32>(0, 1);
+   // let B_south = textureLoad(txBottom, downIdx, 0).z;
+   // let B_north = textureLoad(txBottom, upIdx, 0).z;
     let B_west = textureLoad(txBottom, leftIdx, 0).z;
     let B_east = textureLoad(txBottom, rightIdx, 0).z;
     if(B_here.z > 0.){
-        if(B_south < 0.0 && B_north < 0.0 && B_west < 0.0 && B_east < 0.0) {
+       // if(B_south < 0.0 && B_north < 0.0 && B_west < 0.0 && B_east < 0.0) {
+        if(B_west < 0.0 && B_east < 0.0) {
             B_here.z = 0.0;
-            B_here.x = B_north / 2.0;
+           // B_here.x = B_north / 2.0;
             B_here.y = B_east / 2.0;
         }
     }
```


### 2.46 shaders/fragment.wgsl

본판: `shaders/fragment.wgsl`. transect 판: `transect_version/shaders/fragment.wgsl`.
원래 diff는 1772행이다. CR 제외 diff는 7구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `d778fe7` | 2026-06-02 | Added linear structures functionality |
| 본판 | `3c1649b` | 2026-02-11 | added filled arrow for flow vectors |
| 본판 | `d23dfb0` | 2025-09-01 | Small fixes |
| 본판 | `8c2b62b` | 2025-08-24 | Added Tracy Arm Example, some landslide viz additions |
| 본판 | `3d8a61b` | 2025-06-14 | Added many-transect version |
| 본판 | `7fa28e0` | 2025-06-12 | bug fixes |
| 본판 | `3be651a` | 2025-06-11 | small fixes |
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-246 표시 uniform 확장

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/fragment.wgsl:55; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/fragment.wgsl:55; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 교란 유형과 선형 구조물 미리보기 상태를 받는다. |

본판 차이 줄의 마지막 수정: `d23dfb0` 2025-09-01 (현재 58행 포함); `d778fe7` 2026-06-02 (현재 67행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -55,16 +55,6 @@
     showArrows: i32,
     arrow_scale: f32,
     arrow_density: f32,
-    disturbanceType: f32,
-    // CODEX: Linear-structure preview state uploaded from calc_constants by main.js.
-    designcomponent_StartX: f32,
-    designcomponent_StartY: f32,
-    designcomponent_EndX: f32,
-    designcomponent_EndY: f32,
-    designcomponent_StartDefined: i32,
-    designcomponent_EndDefined: i32,
-    designcomponent_PreviewOn: i32,
-    designcomponent_RenderPad: i32,
 };
 
 @group(0) @binding(0) var<uniform> globals: Globals;
```

#### CT1-247 실제 바닥고 변화 표시

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/fragment.wgsl:285; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/fragment.wgsl:275; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 현재 바닥고와 초기 바닥고의 차이를 읽는다. transect 판은 erosion 입력을 실제 침식률 표시용으로 쓴다. |

본판 차이 줄의 마지막 수정: `2eb2866` 2023-10-26 (현재 288행 포함); `8c2b62b` 2025-08-24 (현재 290행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -285,9 +275,6 @@
     let TextDraw = textureSample(txDraw, textureSampler, uv).rgb;
     let H = max(globals.delta, waves - bottom);
     var render_surface = waves;
-    
-    // depth change option
-    let depth_change = textureSample(bottomTexture, textureSampler, uv).b - textureSample(erosion_Sed, textureSampler, uv).b; 
 
     // if not just plotting waves, load the other stuff
     if (surfaceToPlot == 0) {  // waves
```

#### CT1-248 퇴적물 표시 채널

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/fragment.wgsl:368; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/fragment.wgsl:355; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 가용 깊이 surface 19를 제공한다. 본판의 누적 지형변화 surface 21은 중심 바닥고인 b 채널이다. transect 판은 북쪽 면인 r 채널을 표시한다. 본판은 surface 21에서 최대 eta로 육상 표시 범위를 확장한다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 372행 포함); `3be651a` 2025-06-11 (현재 377행 포함); `3d8a61b` 2025-06-14 (현재 376행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 363행 포함).

```diff
@@ -368,13 +355,12 @@
         render_surface = textureSample(txNewState_Sed, textureSampler, uv).r / H; 
     } else if (surfaceToPlot == 18) {  // sed C1 erosion
         render_surface = textureSample(erosion_Sed, textureSampler, uv).r; 
-    } else if (surfaceToPlot == 19) {  // available scour depth
-        render_surface = textureSample(txRenderVarsf16, textureSampler_linear, uv, 2).b;  
+  //  } else if (surfaceToPlot == 19) {  // sed C1 deposition
+  //      render_surface = textureSample(depostion_Sed, textureSampler, uv).r; 
  //   } else if (surfaceToPlot == 20) {  // sed C1 net deposition 
  //       render_surface = textureSample(depostion_Sed, textureSampler, uv).r - textureSample(erosion_Sed, textureSampler, uv).r; 
-    } else if (surfaceToPlot == 21) {  // sed C1 depth change
-        render_surface = textureSample(txBotChange_Sed, textureSampler, uv).b; 
-        waves = textureSample(txRenderVarsf16, textureSampler_linear, uv, 0).g;  // change to max so maxs are plotted everywhere, including high runup areas that are not currently wet
+    } else if (surfaceToPlot == 21) {  // sed C1 net deposition 
+        render_surface = textureSample(txBotChange_Sed, textureSampler, uv).r; 
     } else if (surfaceToPlot == 22) {  // design components 
         render_surface = textureSample(txDesignComponents, textureSampler, uv).r; 
     } else if (surfaceToPlot == 23) {  // mean vorticity
```

#### CT1-249 렌더 영역 길이 정의

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/fragment.wgsl:390; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/fragment.wgsl:376; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 (WIDTH-1)*dx와 (HEIGHT-1)*dy를 쓴다. transect 판은 WIDTH*dx와 HEIGHT*dy를 쓴다. 격자점 끝을 세는지 셀 수를 세는지의 차이가 표시 길이를 한 격자간격 바꾼다. |

본판 차이 줄의 마지막 수정: `7fa28e0` 2025-06-12 (현재 394행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 380행 포함).

```diff
@@ -390,8 +376,8 @@
 
 
     if (photorealistic == 1) {  // add lighting for photo-realistic view
-        let width = f32(globals.WIDTH - 1) * globals.dx;
-        let length = f32(globals.HEIGHT - 1) * globals.dy;     
+        let width = f32(globals.WIDTH) * globals.dx;
+        let length = f32(globals.HEIGHT) * globals.dy;     
 
         // define local component index
         component_index = i32(0.01 + textureSample(txDesignComponents, textureSampler, uv).r); // this is equivalent to a floor operation, so add the shift just in case
```

#### CT1-250 육상 이동 사면 색상

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/fragment.wgsl:574; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/fragment.wgsl:560; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 disturbanceType==5이고 변화량이 delta를 넘으면 회색 사면을 표시한다. transect 판은 overlay·일반 육상 색상을 쓴다. |

본판 차이 줄의 마지막 수정: `8c2b62b` 2025-08-24 (현재 582행 포함); `d23dfb0` 2025-09-01 (현재 578행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 563행 포함).

```diff
@@ -574,12 +560,7 @@
     if(photorealistic != 0 && (component_index == 3 || component_index >= 5)){design_component_allowed_on_land = 1;}  //magroves, and other components that can exist above zero datum
 
     if (bottom + globals.delta >= waves && surfaceToPlot != 6 && design_component_allowed_on_land == 0) {
-
-        if (abs(depth_change) > globals.delta && globals.disturbanceType == 5) {  // make slide mass gray
-            let depth_change_scale = depth_change/globals.base_depth*50.0;  
-            color_rgb = vec3<f32>(150+depth_change_scale, 150+depth_change_scale, 150+depth_change_scale)/256; // light gray
-        }
-        else if(globals.IsOverlayMapLoaded == 1) {
+        if(globals.IsOverlayMapLoaded == 1) {
             color_rgb = GoogleMap;
         }
         else {
```

#### CT1-251 화살표 텍스처 레이어

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/fragment.wgsl:780; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/fragment.wgsl:761; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 사실적 표시에서 채워진 화살표 레이어 10을 쓴다. transect 판은 레이어 9를 쓴다. |

본판 차이 줄의 마지막 수정: `3c1649b` 2026-02-11 (현재 784행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 764행 포함).

```diff
@@ -780,8 +761,7 @@
         let rotated = vec2<f32>(centered.x * c - centered.y * s,  centered.x * s + centered.y * c) / speed_clamped + vec2<f32>(0.5, 0.5);
 
         // 8. sample your arrow layer — sampler must use repeat wrapping
-        var layer = 9;
-        if (photorealistic == 1) {layer = 10;} // filled arrows (layer = 10) when using photo-realstic, fr better view
+        let layer = 9;
         let rotated_clamped = clamp(rotated, vec2<f32>(0.0, 0.0), vec2<f32>(1.0, 1.0));
         let arrow = textureSample(txSamplePNGs, textureSampler_linear, rotated_clamped, i32(layer));
```

#### CT1-252 선형 구조물 미리보기

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/fragment.wgsl:800; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/fragment.wgsl:780; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 끝점 점과 선분을 검게 표시한다. transect 판에는 미리보기 경로가 없다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 853행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -800,57 +780,6 @@
         color_rgb = color_rgb + vec3<f32>(tracer, 0., 0.);
     }
 
-    // CODEX: Add linear-structure start/end dots and segment preview using the time-series marker coordinate mapping.
-    if (globals.designcomponent_PreviewOn == 1) {
-        let linear_current_uv = vec2<f32>(
-            uv.x / grid_ratio_y,
-            uv.y * f32(globals.HEIGHT) / f32(globals.WIDTH) / grid_ratio_x
-        );
-        let linear_start_grid = vec2<f32>(
-            globals.designcomponent_StartX / globals.dx,
-            globals.designcomponent_StartY / globals.dy
-        );
-        let linear_end_grid = vec2<f32>(
-            globals.designcomponent_EndX / globals.dx,
-            globals.designcomponent_EndY / globals.dy
-        );
-        let linear_start_uv = vec2<f32>(
-            (linear_start_grid.x / f32(globals.WIDTH)) / grid_ratio_y,
-            (linear_start_grid.y / f32(globals.HEIGHT)) * f32(globals.HEIGHT) / f32(globals.WIDTH) / grid_ratio_x
-        );
-        let linear_end_uv = vec2<f32>(
-            (linear_end_grid.x / f32(globals.WIDTH)) / grid_ratio_y,
-            (linear_end_grid.y / f32(globals.HEIGHT)) * f32(globals.HEIGHT) / f32(globals.WIDTH) / grid_ratio_x
-        );
-
-        if (globals.designcomponent_StartDefined == 1 && globals.designcomponent_EndDefined == 1) {
-            let linear_segment = linear_end_uv - linear_start_uv;
-            let linear_segment_len2 = dot(linear_segment, linear_segment);
-            if (linear_segment_len2 > 0.00000001) {
-                let linear_projection = clamp(dot(linear_current_uv - linear_start_uv, linear_segment) / linear_segment_len2, 0.0, 1.0);
-                let linear_closest = linear_start_uv + linear_projection * linear_segment;
-                let linear_line_dist = length(linear_current_uv - linear_closest);
-                if (linear_line_dist <= 0.0035) {
-                    color_rgb = vec3<f32>(0., 0., 0.);
-                }
-            }
-        }
-
-        if (globals.designcomponent_StartDefined == 1) {
-            let linear_start_dist = length(linear_current_uv - linear_start_uv);
-            if (linear_start_dist <= 0.0075) {
-                color_rgb = vec3<f32>(0., 0., 0.);
-            }
-        }
-
-        if (globals.designcomponent_EndDefined == 1) {
-            let linear_end_dist = length(linear_current_uv - linear_end_uv);
-            if (linear_end_dist <= 0.0075) {
-                color_rgb = vec3<f32>(0., 0., 0.);
-            }
-        }
-    }
-
     // Add dots for time series
     let ts_colors = array<vec3<f32>, 15>(
     vec3<f32>(0.2941, 0.7529, 0.7529),
```


### 2.47 shaders/vertex3D.wgsl

본판: `shaders/vertex3D.wgsl`. transect 판: `transect_version/shaders/vertex3D.wgsl`.
원래 diff는 174행이다. CR 제외 diff는 1구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `7fa28e0` | 2025-06-12 | bug fixes |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-253 3D 고도 샘플과 영역 길이

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:shaders/vertex3D.wgsl:74; 아래 전체 diff의 -행 | ebca435:transect_version/shaders/vertex3D.wgsl:74; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 f16 표시 텍스처를 선형 샘플링한다. 본판은 etaTexture를 정수 좌표로 직접 읽는다. transect 판은 W*dx·H*dy를 쓴다. 본판은 (W-1)*dx·(H-1)*dy를 쓴다. 고도 정밀도·보간·끝점 위치가 다르다. |

본판 차이 줄의 마지막 수정: `7fa28e0` 2025-06-12 (현재 81행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 80행 포함).

```diff
@@ -74,11 +74,10 @@
     // uv directly from position
     out.uv = v.pos * 0.5 + 0.5;
 
-    //let elev = textureSampleLevel(txRenderVarsf16, textureSampler_linear, out.uv, 0, 0.0).r;
-    var elev = textureLoad(etaTexture, vec2<i32>(i32(out.uv.x * f32(globals.WIDTH - 1)), i32(out.uv.y * f32(globals.HEIGHT - 1))), 0).r;
+    let elev = textureSampleLevel(txRenderVarsf16, textureSampler_linear, out.uv, 0, 0.0).r;
 
-    let worldX = out.uv.x * f32(globals.WIDTH - 1)  * globals.dx;
-    let worldY = out.uv.y * f32(globals.HEIGHT - 1) * globals.dy;
+    let worldX = out.uv.x * f32(globals.WIDTH)  * globals.dx;
+    let worldY = out.uv.y * f32(globals.HEIGHT) * globals.dy;
     let worldZ = elev * globals.renderZScale;
 
     out.clip_position = globals.viewProj * vec4<f32>(worldX, worldY, worldZ, 1.0);
```


### 2.48 js/main.js

본판: `js/main.js`. transect 판: `transect_version/js/main.js`.
원래 diff는 8762행이다. CR 제외 diff는 89구간이다.

파일별 `git log --follow -p` 이력은 다음과 같다.

| 판 | HASH | 날짜 | 커밋 메시지 |
|---|---|---|---|
| 본판 | `ebca435` | 2026-07-20 | fixed time series write bug |
| 본판 | `c4be488` | 2026-07-13 | allow multiple nested grids |
| 본판 | `ff0d046` | 2026-07-07 | time series plot updates for spherical grids |
| 본판 | `bb99fee` | 2026-07-02 | Added grid nesting |
| 본판 | `afc1fe7` | 2026-06-19 | Added Spherical NLSW Solver, Japan 2011 example |
| 본판 | `0ee5174` | 2026-06-18 | CelerisAgent initial commit |
| 본판 | `f6fd78b` | 2026-06-04 | Added "agent_case" automation helper |
| 본판 | `d778fe7` | 2026-06-02 | Added linear structures functionality |
| 본판 | `9093d7f` | 2026-06-01 | added ability to change wave conditions through the UI - on the Modify Boundary Conditions Panel |
| 본판 | `590bda8` | 2026-06-01 | model plot update |
| 본판 | `62b1458` | 2026-05-24 | Updated two-finger touch for ipad / iphone |
| 본판 | `24b8f13` | 2026-05-24 | Add Mac / IPhone / IPad scene navigation support |
| 본판 | `bf8db50` | 2026-05-24 | Localhost debug and overlay bug fixes |
| 본판 | `984091f` | 2026-05-24 | Markdown and PCR ping-pong updates |
| 본판 | `c3c57a4` | 2026-03-03 | fix last row vertex configuration to remove bottom pixel strand |
| 본판 | `7ae7da4` | 2026-02-23 | Minor fixes - additional debug info, and landslide volume fix |
| 본판 | `f466786` | 2026-02-20 | Update main.js |
| 본판 | `a86f73a` | 2026-02-20 | more long sim "device lost" fix attempts |
| 본판 | `09cfd76` | 2026-02-15 | All 2D surface writes re-use the same buffer |
| 본판 | `33f7ff6` | 2026-02-13 | Further encoder streamline fixes |
| 본판 | `08860f0` | 2026-02-13 | Reduced createRenderPipeline calls |
| 본판 | `7793a7e` | 2026-02-11 | Update main.js |
| 본판 | `3c1649b` | 2026-02-11 | added filled arrow for flow vectors |
| 본판 | `3646fc8` | 2026-02-08 | Stacked Command Encoders |
| 본판 | `dee0e14` | 2026-02-04 | clean up memory leaks |
| 본판 | `e9d7122` | 2026-02-02 | tooltip update |
| 본판 | `769d990` | 2026-02-01 | Update main.js |
| 본판 | `f183cc2` | 2026-02-01 | Added ability for user to specify initial 3D camera position |
| 본판 | `ff720ca` | 2026-01-30 | Update main.js |
| 본판 | `896c491` | 2026-01-17 | added flags to test beta-level features in code |
| 본판 | `35b7f1c` | 2026-01-15 | addition of vorticity-based momentum mixing |
| 본판 | `19b63cf` | 2025-11-07 | convert Pass2 High-order to HLLC |
| 본판 | `ea93d70` | 2025-10-24 | added Yakutat, Sebastian Inlet examples, and "p" for pause |
| 본판 | `32be94a` | 2025-10-16 | hot start initial condition option added |
| 본판 | `146a4ac` | 2025-09-28 | added Tracy Arm hot start |
| 본판 | `397c575` | 2025-09-09 | Max fs to tooltip for slide sims |
| 본판 | `d23dfb0` | 2025-09-01 | Small fixes |
| 본판 | `8c2b62b` | 2025-08-24 | Added Tracy Arm Example, some landslide viz additions |
| 본판 | `dc6cc2d` | 2025-08-10 | update max free surface render |
| 본판 | `852ec28` | 2025-06-13 | sed trans fixes |
| 본판 | `7fa28e0` | 2025-06-12 | bug fixes |
| 본판 | `1ce6bf7` | 2025-06-10 | bug fix |
| 본판 | `ba9eb67` | 2025-06-09 | added bedload to bottom update equation |
| 본판 | `4353b85` | 2025-06-09 | Sed bugs / corrections |
| 본판 | `a98bcc4` | 2025-06-09 | sed trans updates |
| 본판 | `c7fb523` | 2025-06-09 | bugs |
| 본판 | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| 본판 | `2a7452d` | 2025-06-07 | Sed Trans updates |
| 본판 | `5c60ac0` | 2025-06-07 | add sediment diffusion term |
| 본판 | `fa47b72` | 2025-06-06 | Sed Trans Updates |
| 본판 | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |
| transect | `3d8a61b` | 2025-06-14 | Added many-transect version |
| transect | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |

#### CT1-254 초기화 모듈 연결

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 단면 파랑 reader와 uploader를 import한다. 본판은 초기 수면·hardbottom·경계 시계열·중첩 writer·파 생성기를 import한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 3행 포함); `afc1fe7` 2026-06-19 (현재 11행 포함); `9093d7f` 2026-06-01 (현재 16행 포함); `0ee5174` 2026-06-18 (현재 17행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 3행 포함); `22e1983` 2025-06-06 (현재 4행 포함).

```diff
@@ -1,20 +1,10 @@
 ﻿// import source files
 import { calc_constants, timeSeriesData, loadConfig, init_sim_parameters } from './constants_load_calc.js';  // variables and functions needed for init_sim_parameters
-// import { loadDepthSurface, loadInitCondSurface, loadFrictionSurface, loadHardBottomSurface, loadWaveData, loadOverlay, CreateGoogleMapImage, calculateGoogleMapScaleAndOffset, loadImageBitmap, loadUserImage, loadCubeBitmaps} from './File_Loader.js';  // load depth surface and wave data file
-// Added by Codex: Import boundary time-series forcing loader for boundary_type == 5.
-import { loadDepthSurface, loadInitCondSurface, loadFrictionSurface, loadHardBottomSurface, loadWaveData, loadBoundaryTimeSeriesData, loadOverlay, CreateGoogleMapImage, calculateGoogleMapScaleAndOffset, loadImageBitmap, loadUserImage, loadCubeBitmaps} from './File_Loader.js';  // load depth surface and wave data file
-// import { readTextureData, downloadTextureData, downloadObjectAsFile, handleFileSelect, loadJsonIntoCalcConstants, saveRenderedImageAsJPEG, saveSingleValueToFile, saveTextureSlicesAsImages, createAnimatedGifFromTexture, writeSurfaceData, sleep} from './File_Writer.js';  // load depth surface and wave data file
-// Added by Codex: Import nested-grid boundary time-series output writer.
-import { readTextureData, downloadTextureData, downloadObjectAsFile, handleFileSelect, loadJsonIntoCalcConstants, saveRenderedImageAsJPEG, saveSingleValueToFile, saveTextureSlicesAsImages, createAnimatedGifFromTexture, writeSurfaceData, writeNestedGridBoundaryTimeSeriesData, sleep} from './File_Writer.js';  // load depth surface and wave data file
+import { loadDepthSurface, loadFrictionSurface, loadTransectWaveData, loadWaveData, loadOverlay, CreateGoogleMapImage, calculateGoogleMapScaleAndOffset, loadImageBitmap, loadUserImage, loadCubeBitmaps} from './File_Loader.js';  // load depth surface and wave data file
+import { readTextureData, downloadTextureData, downloadObjectAsFile, handleFileSelect, loadJsonIntoCalcConstants, saveRenderedImageAsJPEG, saveSingleValueToFile, saveTextureSlicesAsImages, createAnimatedGifFromTexture, writeSurfaceData, sleep} from './File_Writer.js';  // load depth surface and wave data file
 import { readCornerPixelData, readToolTipTextureData, downloadTimeSeriesData, resetTimeSeriesData} from './Time_Series.js';  // time series functions
 import { create_2D_Texture, create_2D_F16Texture, create_2D_Image_Texture, create_3D_Image_Texture, create_3D_Data_Texture, create_1D_Texture, createUniformBuffer, create_Depth_Texture} from './Create_Textures.js';  // create texture function
-// import { copyBathyDataToTexture, copyWaveDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture, copy2DDataTo3DTexture} from './Copy_Data_to_Textures.js';  // fills in channels of txBottom
-// Added by Codex: Import spherical metric upload helper for grid_type == 2.
-// import { copyBathyDataToTexture, copyWaveDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copySphericalMetricDataToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture, copy2DDataTo3DTexture} from './Copy_Data_to_Textures.js';  // fills in channels of txBottom
-// Added by Codex: Import boundary time-series forcing texture upload helper.
-import { copyBathyDataToTexture, copyWaveDataToTexture, copyBoundaryTimeSeriesDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copySphericalMetricDataToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture, copy2DDataTo3DTexture} from './Copy_Data_to_Textures.js';  // fills in channels of txBottom
-// Added by Codex: Boundary-wave generators keep UI-created spectra outside the main orchestrator.
-import { GENERATED_BOUNDARY_WAVE_TEXTURE_CAPACITY, buildSineWaveData, buildTmaWaveData } from './Wave_Generator.js?v=periodic-wave-fit-gated-20260611';
+import { copyBathyDataToTexture, copyTransectWaveDataToTexture, copyWaveDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture, copy2DDataTo3DTexture} from './Copy_Data_to_Textures.js';  // fills in channels of txBottom
 import { makeModelMatrix, loadSceneModels, loadglTFModel} from './Model_Loaders.js';  // functions to load 3D models
 import { createRenderBindGroupLayout, createRenderBindGroup, update_colorbar, loadImage} from './Handler_Render.js';  // group bindings for render shaders
 import { createSkyboxBindGroupLayout, createSkyboxBindGroup} from './Handler_Skybox.js';  // group bindings for skybox shaders
```

#### CT1-255 호스트 모듈 연결

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:36; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:26; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 중첩 경계 handler·EncStack·agent_controls를 import한다. transect 판은 즉시 submit 함수를 쓴다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 39행 포함); `3646fc8` 2026-02-08 (현재 43행 포함); `0ee5174` 2026-06-18 (현재 46행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 31행 포함).

```diff
@@ -36,14 +26,11 @@
 import { create_AddDisturbance_BindGroupLayout, create_AddDisturbance_BindGroup } from './Handler_AddDisturbance.js';  // group bindings for adding a landslide or tsunami impulsive source
 import { create_MouseClickChange_BindGroupLayout, create_MouseClickChange_BindGroup } from './Handler_MouseClickChange.js';  // group bindings for mouse click changes
 import { create_ExtractTimeSeries_BindGroupLayout, create_ExtractTimeSeries_BindGroup } from './Handler_ExtractTimeSeries.js';  // group bindings for storing single pixel / time series values
-// Added by Codex: Import nested-grid boundary time-series extraction handler.
-import { create_ExtractNestedBoundaryTimeSeries_BindGroupLayout, create_ExtractNestedBoundaryTimeSeries_BindGroup } from './Handler_ExtractNestedBoundaryTimeSeries.js';
 import { create_Copytxf32_txf16_BindGroupLayout, create_Copytxf32_txf16_BindGroup } from './Handler_Copytxf32_txf16.js';  // group bindings for f32 to f16 copy shader
 import { createComputePipeline, createRenderPipeline, createRenderPipeline_vertexgrid, createSkyboxPipeline, createModelPipeline, createDuckPipeline} from './Config_Pipelines.js';  // pipeline config for ALL shaders
-import { fetchShader, runComputeShader, runCopyTextures, runComputeShader_EncStack, runCopyTextures_EncStack} from './Run_Compute_Shader.js';  // function to run shaders, works for all
+import { fetchShader, runComputeShader, runCopyTextures } from './Run_Compute_Shader.js';  // function to run shaders, works for all
 import { runTridiagSolver } from './Run_Tridiag_Solver.js';  // function to run PCR triadiag solver, works for all
 import { displayCalcConstants, displaySimStatus, displayTimeSeriesLocations, displaySlideVolume, ConsoleLogRedirection} from './display_parameters.js';  // starting point for display of simulation parameters
-import { installCelerisAgentControls } from './agent_controls.js?v=agent-timeseries-duration-native-path-20260614';
 import { mat4, vec3 } from 'https://cdn.jsdelivr.net/npm/gl-matrix/esm/index.js';
 
 // Get a reference to the HTML canvas element with the ID 'webgpuCanvas'
```

#### CT1-256 선형 구조물과 전체화면 상태

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:62; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:49; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 가상 전체화면 플래그와 외부 제어 모드를 둔다. 본판은 선형 구조물 양끝점 표시와 적용 후 초기화를 구현한다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 65행 포함); `0ee5174` 2026-06-18 (현재 67행 포함); `cf9de63` 2023-10-24 (현재 69행 포함); `d778fe7` 2026-06-02 (현재 70행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -62,49 +49,6 @@
 let txDraw = null;
 let context = null;
 let adapter = null;
-// CODEX: Tracks whether the iOS/mobile pseudo-fullscreen fallback is active.
-let pseudoFullscreenActive = false;
-// CODEX: Agent-selected design workflow mode gates left/right design-panel click actions.
-let agentDesignInteractionMode = null;
-
-// CODEX: Update the linear-structure coordinate summary from calc_constants outside the DOMContentLoaded scope.
-function updateLinearStructureLocationsDisplayFromCalcConstants() {
-    const linearStructureContainer = document.getElementById('linearstructurelocs-container');
-    if (!linearStructureContainer) {
-        return;
-    }
-    const startText = calc_constants.designcomponent_StartDefined == 1
-        ? `Start: (${calc_constants.designcomponent_StartX.toFixed(2)}, ${calc_constants.designcomponent_StartY.toFixed(2)}) m`
-        : 'Start: not set';
-    const endText = calc_constants.designcomponent_EndDefined == 1
-        ? `End: (${calc_constants.designcomponent_EndX.toFixed(2)}, ${calc_constants.designcomponent_EndY.toFixed(2)}) m`
-        : 'End: not set';
-    linearStructureContainer.innerHTML = `${startText}<br>${endText}`;
-}
-
-// CODEX: Clear linear-structure endpoints and preview state after the GPU bathy/topo edit completes.
-function resetLinearStructureEndpointsAfterApply() {
-    calc_constants.designcomponent_StartX = 0.0;
-    calc_constants.designcomponent_StartY = 0.0;
-    calc_constants.designcomponent_EndX = 0.0;
-    calc_constants.designcomponent_EndY = 0.0;
-    calc_constants.designcomponent_StartDefined = 0;
-    calc_constants.designcomponent_EndDefined = 0;
-    calc_constants.designcomponent_PreviewOn = 0;
-    calc_constants.designcomponent_AddLinearStructure = 0;
-    calc_constants.designcomponent_xLoc = 0.0;
-    calc_constants.designcomponent_yLoc = 0.0;
-    const xInput = document.getElementById('designcomponent_xLoc-input');
-    const yInput = document.getElementById('designcomponent_yLoc-input');
-    if (xInput) {
-        xInput.value = calc_constants.designcomponent_xLoc;
-    }
-    if (yInput) {
-        yInput.value = calc_constants.designcomponent_yLoc;
-    }
-    calc_constants.html_update = 1;
-    updateLinearStructureLocationsDisplayFromCalcConstants();
-}
 
 // Initialize a global set to track texture, pipeline objects
 const allTextures = new Set();
```

#### CT1-257 URL 케이스 초기화

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:119; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:63; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 agent_case·autostart 쿼리를 읽고 manifest의 config·bathy·waves·선택 overlay·초기 수면을 fetch한다. 로딩 상태는 부모 창으로 postMessage한다. transect 판에는 해당 진입 경로가 없다. |

본판 차이 줄의 마지막 수정: `f6fd78b` 2026-06-04 (현재 122행 포함); `0ee5174` 2026-06-18 (현재 138행 포함); `bb99fee` 2026-07-02 (현재 195행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 67행 포함).

```diff
@@ -119,82 +63,8 @@
     throw new Error("WebGPU is not supported in this browser.");
 }
 
-function postAgentCaseStatus(status, payload = {}) {
-    const message = { source: "celeris-webgpu", status, ...payload };
-    console.log("Agent case status:", message);
-    if (window.parent && window.parent !== window) {
-        window.parent.postMessage(message, "*");
-    }
-}
-
-async function fetchAgentCaseText(url, label) {
-    const response = await fetch(url, { mode: "cors" });
-    if (!response.ok) {
-        throw new Error(`Failed to fetch ${label}: HTTP ${response.status}`);
-    }
-    return response.text();
-}
-
-async function fetchAgentCaseBlob(url, label) {
-    const response = await fetch(url, { mode: "cors" });
-    if (!response.ok) {
-        throw new Error(`Failed to fetch ${label}: HTTP ${response.status}`);
-    }
-    return response.blob();
-}
-
-function resolveAgentCaseFileUrl(caseUrl, fileUrl) {
-    if (!fileUrl || typeof fileUrl !== "string") {
-        throw new Error("Agent case manifest is missing a required file URL.");
-    }
-    return new URL(fileUrl, caseUrl).toString();
-}
-
-async function loadAgentCaseFromUrl() {
-    const params = new URLSearchParams(window.location.search);
-    const caseUrl = params.get("agent_case");
-    const autostart = params.get("autostart") === "1" || params.get("autostart") === "true";
-    if (!caseUrl || !autostart) {
-        return false;
-    }
-
-    try {
-        postAgentCaseStatus("celeris:case-loading", { caseUrl });
-        const manifestResponse = await fetch(caseUrl, { mode: "cors" });
-        if (!manifestResponse.ok) {
-            throw new Error(`Failed to fetch agent case manifest: HTTP ${manifestResponse.status}`);
-        }
-        const manifest = await manifestResponse.json();
-        const files = manifest.files || {};
-        const configUrl = resolveAgentCaseFileUrl(caseUrl, files.config);
-        const bathyUrl = resolveAgentCaseFileUrl(caseUrl, files.bathy);
-        const wavesUrl = resolveAgentCaseFileUrl(caseUrl, files.waves);
-        const overlayUrl = files.overlay ? resolveAgentCaseFileUrl(caseUrl, files.overlay) : null;
-        const initialEtaUrl = files.initial_eta ? resolveAgentCaseFileUrl(caseUrl, files.initial_eta) : null;
-        const [configContent, bathymetryContent, waveContent] = await Promise.all([
-            fetchAgentCaseText(configUrl, "config.json"),
-            fetchAgentCaseText(bathyUrl, "bathy.txt"),
-            fetchAgentCaseText(wavesUrl, "waves.txt"),
-        ]);
-        const overlayBlob = overlayUrl ? await fetchAgentCaseBlob(overlayUrl, "overlay.jpg") : undefined;
-        const initialEtaBlob = initialEtaUrl ? await fetchAgentCaseBlob(initialEtaUrl, "etaInitCond.txt") : undefined;
-
-        calc_constants.run_example = -1;
-        postAgentCaseStatus("celeris:case-loaded", { caseUrl, manifest });
-        await initializeWebGPUApp(configContent, bathymetryContent, waveContent, overlayBlob, undefined, initialEtaBlob);
-        postAgentCaseStatus("celeris:started", { caseUrl, manifest });
-        return true;
-    } catch (error) {
-        console.error("Agent case autostart failed:", error);
-        postAgentCaseStatus("celeris:error", { caseUrl, message: error.message || String(error) });
-        return false;
-    }
-}
-
 // create an async function to handle configuration routines that must be performed in order, but also have imbedded async functions.
-// async function OrderedFunctions(configContent, bathymetryContent, waveContent) {
-// Added by Codex: Carry optional uploaded boundary time-series files into the config-dependent loader.
-async function OrderedFunctions(configContent, bathymetryContent, waveContent, boundaryTimeSeriesFiles = {}) {
+async function OrderedFunctions(configContent, bathymetryContent, waveContent) {
     // Set simulation parameters - this routine inits calc_constants to default values,
     // loads the json config file and places updated values in calc_constants, and then
     // sets and values of calc_constants that are dependent on inputs(e.g.dt)
```

#### CT1-258 단면 파랑 읽기와 초기화 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:203; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:73; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 loadTransectWaveData를 호출한다. 성분 수는 config 값을 유지한다. 초기화 함수는 config·bathy·waves·overlay·model·friction의 6인자를 받는다. 본판은 초기 수면·hardbottom·4변 시계열을 추가로 받는다. |

본판 차이 줄의 마지막 수정: `0dd009e` 2024-03-21 (현재 206행 포함); `63a12e3` 2023-10-19 (현재 207행 포함); `bb99fee` 2026-07-02 (현재 208행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 76행 포함); `22e1983` 2025-06-06 (현재 81행 포함).

```diff
@@ -203,21 +73,17 @@
     // Load depth surface file, place into 2D array bathy2D
     let bathy2D = await loadDepthSurface(bathymetryContent, calc_constants);  // Start this only after the first function completes
     // Load wave data file, place into waveArray 
-    let { numberOfWaves, waveData } = await loadWaveData(waveContent, calc_constants);  // Start this only after the first function completes
-    calc_constants.numberOfWaves = numberOfWaves; 
-    // return { bathy2D, waveData };
-    // Added by Codex: Load optional boundary_type == 5 eta/hu/hv time-series forcing files after config paths are known.
-    // let boundaryTimeSeriesData = await loadBoundaryTimeSeriesData(calc_constants);
-    // Added by Codex: Uploaded boundary time-series files override ts_*_file fetch paths for custom local runs.
-    let boundaryTimeSeriesData = await loadBoundaryTimeSeriesData(calc_constants, boundaryTimeSeriesFiles);
-    return { bathy2D, waveData, boundaryTimeSeriesData };
+    //let { numberOfWaves, waveData } = await loadWaveData(waveContent, calc_constants);  // Start this only after the first function completes
+    //calc_constants.numberOfWaves = numberOfWaves; 
+
+    let waveData = await loadTransectWaveData(waveContent, calc_constants);  // Start this only after the first function completes
+ 
+    return { bathy2D, waveData };
 }
 
 // This is an asynchronous function to set up and run the WebGPU context and resources.
 // All of the compute pipelines are included in this function
-// async function initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile) {
-// Added by Codex: Optional boundary time-series upload files support custom configs outside served example folders.
-async function initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile) {
+async function initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile) {
     // Log a message indicating the start of the initialization process.
     console.log("Starting Celeris-WebGPU");
```

#### CT1-259 GPU 장치 요청과 오류 기록

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:245; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:111; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 adapter의 2D 텍스처 최대 길이를 요청한다. 본판은 device lost와 uncapturederror를 기록한다. transect 판은 기본 requiredLimits를 쓴다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 248행 포함); `769d990` 2026-02-01 (현재 266행 포함); `7ae7da4` 2026-02-23 (현재 268행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 118행 포함).

```diff
@@ -245,34 +111,15 @@
         console.log('Found high-performance GPU adapter.');
     }
 
-    // Added by Codex: Start elevated WebGPU texture-dimension request for long boundary time-series files.
-    const requestedMaxTextureDimension2D = adapter.limits?.maxTextureDimension2D || 8192;
-    console.log(`Requesting WebGPU maxTextureDimension2D limit: ${requestedMaxTextureDimension2D}`);
-    // Added by Codex: End elevated WebGPU texture-dimension request for long boundary time-series files.
-
     // Request a device. The device is a representation of the GPU and allows for resource creation and command submission.
     device = await adapter.requestDevice({
         // Enable built-in validation
         requiredFeatures: [],
-        // requiredLimits: {},
-        // Added by Codex: Ask for the adapter-supported 2D texture dimension so large boundary time-series textures can exceed the default 8192 rows when hardware allows.
-        requiredLimits: {
-            maxTextureDimension2D: requestedMaxTextureDimension2D,
-        },
+        requiredLimits: {},
         forceFallbackAdapter: false,
     });
     console.log("GPU Device acquired, starting resource creation...");
 
-    // Handle device lost and uncaptured error events
-    device.lost.then((info) => {
-    console.error(`WebGPU device lost: reason="${info.reason}", message="${info.message}"`);
-    });
-
-    device.addEventListener("uncapturederror", (e) => {
-    console.error("WebGPU uncaptured error:", e.error);
-    });
-
-
     // Get the WebGPU rendering context from the canvas.
     context = canvas.getContext('webgpu');
```

#### CT1-260 파 생성과 type5 시간 보간

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:287; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:134; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 원래 파 스펙트럼을 복사해 보존한다. 본판은 UI sine/TMA 생성과 텍스처 재업로드를 지원한다. type5는 시간 이진 탐색과 선형 보간을 쓴다. 마지막 시각 뒤는 영 상태 행을 선택한다. transect 판은 단면 파랑을 한 번 읽는다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 290행 포함); `63a12e3` 2023-10-19 (현재 301행 포함); `9093d7f` 2026-06-01 (현재 302행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 137행 포함).

```diff
@@ -287,105 +134,7 @@
     });
 
     // load the simulation parameters, the 2D depth surface, and the wave data.  "Ordered" as the sequence of how these files are loaded is important
-    // let { bathy2D, waveData } = await OrderedFunctions(configContent, bathymetryContent, waveContent);
-    // Added by Codex: Carry parsed boundary time-series data into texture allocation/upload.
-    // let { bathy2D, waveData, boundaryTimeSeriesData } = await OrderedFunctions(configContent, bathymetryContent, waveContent);
-    // Added by Codex: Group uploaded boundary time-series files by side for the loader.
-    const boundaryTimeSeriesFiles = {
-        west: westBoundaryTimeSeriesFile,
-        east: eastBoundaryTimeSeriesFile,
-        south: southBoundaryTimeSeriesFile,
-        north: northBoundaryTimeSeriesFile
-    };
-    let { bathy2D, waveData, boundaryTimeSeriesData } = await OrderedFunctions(configContent, bathymetryContent, waveContent, boundaryTimeSeriesFiles);
-
-    // Added by Codex: Start UI boundary wave regeneration support.
-    // Added by Codex: Preserve the loaded waves.txt data so UI-generated boundary waves can be toggled without losing the custom spectrum.
-    const loadedBoundaryNumberOfWaves = calc_constants.numberOfWaves;
-    const loadedBoundaryWaveData = waveData.map(row => row.slice());
-
-    // Added by Codex: Build boundary forcing rows in the same [amplitude, period, directionRadians, phaseRadians] format used by waves.txt.
-    function buildBoundaryWaveDataFromControls() {
-        if (calc_constants.incident_wave_type == 0) {
-            // const waveHeight = Number.isFinite(calc_constants.incident_wave_H) ? calc_constants.incident_wave_H : 0.0;
-            // const wavePeriod = calc_constants.incident_wave_T > 0.0 ? calc_constants.incident_wave_T : 10.0;
-            // const waveDirection = Number.isFinite(calc_constants.incident_wave_direction) ? calc_constants.incident_wave_direction * Math.PI / 180.0 : 0.0;
-            // return { numberOfWaves: 1, waveData: [[0.5 * waveHeight, wavePeriod, waveDirection, 0.0]] };
-            // Added by Codex: Reuse the shared generator contract for sine and spectral boundary waves.
-            return buildSineWaveData(calc_constants);
-        }
-
-        if (calc_constants.incident_wave_type == 1) {
-            // // Added by Codex: TMA generation will use this same return contract; until then, keep the loaded spectrum active.
-            // return { numberOfWaves: loadedBoundaryNumberOfWaves, waveData: loadedBoundaryWaveData };
-            // Added by Codex: Generate TMA components from the incident-wave UI controls.
-            return buildTmaWaveData(calc_constants);
-        }
-
-        return { numberOfWaves: loadedBoundaryNumberOfWaves, waveData: loadedBoundaryWaveData };
-    }
-
-    // Added by Codex: Re-upload boundary wave rows whenever UI-selected forcing changes the component set.
-    function refreshBoundaryWaveTexture(txWaves) {
-        const boundaryWaves = buildBoundaryWaveDataFromControls();
-        if (boundaryWaves.numberOfWaves > 0) {
-            calc_constants.numberOfWaves = boundaryWaves.numberOfWaves;
-            copyWaveDataToTexture(calc_constants, boundaryWaves.waveData, device, txWaves);
-        }
-    }
-    // Added by Codex: End UI boundary wave regeneration support.
-
-    // Added by Codex: Start boundary time-series forcing helpers.
-    function getBoundaryTimeSeriesTextureSize(sideData) {
-        return {
-            width: Math.max(sideData?.textureWidth || 1, 1),
-            height: Math.max(sideData?.textureHeight || 1, 1)
-        };
-    }
-
-    function getBoundaryTimeSeriesBracket(currentTime) {
-        const times = boundaryTimeSeriesData.sharedTimes || [];
-        if (!boundaryTimeSeriesData.hasActive || times.length < 1) {
-            return { idx0: 0, idx1: 0, alpha: 0.0 };
-        }
-
-        if (times.length == 1) {
-            if (currentTime > times[0]) {
-                return { idx0: boundaryTimeSeriesData.zeroTimeIndex, idx1: boundaryTimeSeriesData.zeroTimeIndex, alpha: 0.0 };
-            }
-            return { idx0: 0, idx1: 0, alpha: 0.0 };
-        }
-
-        if (currentTime <= times[0]) {
-            return { idx0: 0, idx1: 0, alpha: 0.0 };
-        }
-        if (currentTime > times[times.length - 1]) {
-            return { idx0: boundaryTimeSeriesData.zeroTimeIndex, idx1: boundaryTimeSeriesData.zeroTimeIndex, alpha: 0.0 };
-        }
-
-        let lower = 0;
-        let upper = times.length - 1;
-        while (upper - lower > 1) {
-            const middle = Math.floor(0.5 * (lower + upper));
-            if (times[middle] <= currentTime) {
-                lower = middle;
-            } else {
-                upper = middle;
-            }
-        }
-
-        const dtBoundary = times[upper] - times[lower];
-        const alpha = dtBoundary > 0.0 ? (currentTime - times[lower]) / dtBoundary : 0.0;
-        return { idx0: lower, idx1: upper, alpha };
-    }
-
-    function updateBoundaryTimeSeriesUniforms(BoundaryPass_view, currentTime) {
-        const bracket = getBoundaryTimeSeriesBracket(currentTime);
-        BoundaryPass_view.setInt32(204, bracket.idx0, true);              // i32
-        BoundaryPass_view.setInt32(208, bracket.idx1, true);              // i32
-        BoundaryPass_view.setFloat32(212, bracket.alpha, true);           // f32
-    }
-    // Added by Codex: End boundary time-series forcing helpers.
+    let { bathy2D, waveData } = await OrderedFunctions(configContent, bathymetryContent, waveContent);
 
     // Create buffers for storing uniform data. This buffer will be used to send parameter data to shaders.
     const Pass0_uniformBuffer = createUniformBuffer(device);
```

#### CT1-261 uniform·공용 readback 버퍼

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:408; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:157; 아래 전체 diff의 +행 | 불일치 (A) | 본판 Render_bufferSize는 304이고 transect는 272다. 본판만 표면 출력용 공용 readback 버퍼를 할당한다. 두 판은 동일한 256배수 행 길이 식을 사용한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 411행 포함); `c4be488` 2026-07-13 (현재 412행 포함); `d778fe7` 2026-06-02 (현재 414행 포함); `09cfd76` 2026-02-15 (현재 422행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 160행 포함).

```diff
@@ -408,26 +157,12 @@
     const AddDisturbance_uniformBuffer = createUniformBuffer(device);
     const MouseClickChange_uniformBuffer = createUniformBuffer(device);
     const ExtractTimeSeries_uniformBuffer = createUniformBuffer(device);
-    // Added by Codex: Uniform buffer for nested-grid boundary time-series edge extraction.
-    // const ExtractNestedBoundaryTimeSeries_uniformBuffer = createUniformBuffer(device);
-    // Added by Codex: Nested-grid output now allocates one uniform buffer per output rectangle at capture start.
-    // let Render_bufferSize = 272; // 272 bytes for render pipeline, 256 for compute pipeline
-    // CODEX: Add room for linear-structure preview uniforms appended after the existing render globals.
-    let Render_bufferSize = 304; // 304 bytes for render pipeline, 256 for compute pipeline
+    let Render_bufferSize = 272; // 272 bytes for render pipeline, 256 for compute pipeline
     const Render_uniformBuffer = createUniformBuffer(device,Render_bufferSize);
     const Skybox_uniformBuffer = createUniformBuffer(device); // View and Projection buffer: holds two 4×4 f32 view matrix (16 floats → 64 bytes)
     const Model_uniformBuffer = createUniformBuffer(device);
     const Copytxf32_txf16_uniformBuffer = createUniformBuffer(device);
 
-    // create buffer for all file writes
-    const requiredBytesPerRow_2Dbuffer = Math.ceil((calc_constants.WIDTH * 4 * 4) / 256) * 256;
-    const bufferSize_2Dbuffer = calc_constants.HEIGHT * requiredBytesPerRow_2Dbuffer;
-
-    const readbackBuffer = device.createBuffer({
-        size: bufferSize_2Dbuffer,
-        usage: GPUBufferUsage.COPY_DST | GPUBufferUsage.MAP_READ,
-    });
-
     // Create a sampler for texture sampling. This defines how the texture will be sampled (e.g., nearest-neighbor sampling).  Used only for render pipeline
     const textureSampler = device.createSampler({
         magFilter: 'nearest',
```

#### CT1-262 표시 샘플러 반복 방식

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:438; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:173; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 U/V 주소 모드 repeat를 쓴다. 본판은 mirror-repeat를 쓴다. 텍스처 경계 밖의 표시 샘플이 다르다. 계산 flux에는 영향이 없다. |

본판 차이 줄의 마지막 수정: `7fa28e0` 2025-06-12 (현재 441행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 176행 포함).

```diff
@@ -438,8 +173,8 @@
     const textureSampler_linear = device.createSampler({
         magFilter: 'linear',
         minFilter: 'linear',
-        addressModeU: 'mirror-repeat',
-        addressModeV: 'mirror-repeat'
+        addressModeU: 'repeat',
+        addressModeV: 'repeat'
     });
 
     // Create a texturse with the desired dimensions (WIDTH, HEIGHT) and format 'rgba32float'.
```

#### CT1-263 hardbottom 텍스처

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:466; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:201; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 txHardBottom을 할당한다. |

본판 차이 줄의 마지막 수정: `4353b85` 2025-06-09 (현재 469행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -466,7 +201,6 @@
     const erosion_Sed = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // local erosion for all class "e"
     const depostion_Sed = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // local depostion for all class "d"
     const txBotChange_Sed = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // cumulative bottom elevation change
-    const txHardBottom = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores hard bottom elevation
     const txBottomFriction = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores bottom friction info   
     const txDesignComponents = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores map of added components  
     const txContSource = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores passive tracer source map
```

#### CT1-264 구면 계량 텍스처

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:505; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:239; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 txSphericalMetrics를 할당한다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 508행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -505,8 +239,6 @@
     const dU_by_dt = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores d(state)/dt values output from Pass3 calls
     const dU_by_dt_Sed = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores d(state)/dt values output from Pass3 calls
     const txBoundaryForcing = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores ship pressure - not used in WebGPU yet
-    // Added by Codex: Spherical-grid metrics for Pass3_NLSW_Spherical.wgsl when grid_type == 2.
-    const txSphericalMetrics = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);
     const txModelVelocities = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores the u,v velocities from the cell size averages - these are the proper u,v used by the flux scheme
     var txCW_groupings = null;  // stores the variables groupings for the coulwave implementation 
     var txCW_uvhuhv; var txCW_zalpha = null; var txCW_STval = null; var txCW_STgrad = null; var txCW_Eterms = null; var txCW_FGterms = null; // these are only used if COULWAVE is selected
```

#### CT1-265 단면별 파랑 리소스와 초기상태

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:550; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:282; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 Nwave×HEIGHT의 txWaves_Transect를 할당하고 단면 파랑을 업로드한다. 일반 txWaves는 할당하지만 업로드하지 않는다. 본판은 파 생성 용량과 4변 시계열 텍스처를 할당한다. transect 표시 레이어는 10개 영상·2개 f16이고 본판은 11개 영상·3개 f16이다. 본판만 초기 수면과 hardbottom 파일을 읽는다. 초기 상태 API의 차이는 uploader 행과 같다. |

본판 차이 줄의 마지막 수정: `7793a7e` 2026-02-11 (현재 553행 포함); `b8b50c3` 2025-06-08 (현재 559행 포함); `9093d7f` 2026-06-01 (현재 561행 포함); `bb99fee` 2026-07-02 (현재 565행 포함); `afc1fe7` 2026-06-19 (현재 580행 포함); `32be94a` 2025-10-16 (현재 600행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 285행 포함); `3d8a61b` 2025-06-14 (현재 294행 포함).

```diff
@@ -550,100 +282,46 @@
     txDraw = create_2D_Image_Texture(device, canvas.width, canvas.height, allTextures);  // used for creating text & shapes on an HTML5 canvas
     txGoogleMap = create_2D_Texture(device, calc_constants.GMapImageWidth, calc_constants.GMapImageHeight, allTextures);  // used to store the loaded Google Maps image
     txOverlayMap = create_2D_Texture(device, calc_constants.GMapImageWidth, calc_constants.GMapImageHeight, allTextures);  // used to store the loaded Google Maps image
-    const txSamplePNGs = create_3D_Image_Texture(device, 1024, 1024, 11, allTextures); // will store all textures to be sampled for photo-realism
+    const txSamplePNGs = create_3D_Image_Texture(device, 1024, 1024, 10, allTextures); // will store all textures to be sampled for photo-realism
     const txModelPNGs = create_2D_Image_Texture(device, 1024, 1024, allTextures); // will store all textures to be sampled for photo-realism
     let skybox_image_size = 500; // size of each face of the cube map
     const txCube_Skybox = create_3D_Image_Texture(device, skybox_image_size, skybox_image_size, 6, allTextures); // will store all textures to be sampled for photo-realism
     
     let depthTexture = create_Depth_Texture(device, canvas.width, canvas.height, allTextures); // initial depth texture for Explorer mode
-    const txRenderVarsf16 = create_2D_F16Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, 3, allTextures);  // used to store the f16 render variables for the render pipeline
+    const txRenderVarsf16 = create_2D_F16Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, 2, allTextures);  // used to store the f16 render variables for the render pipeline
 
-    // const txWaves = create_1D_Texture(device, calc_constants.numberOfWaves, allTextures);  // stores spectrum wave input
-    // Added by Codex: Generated TMA spectra need more texture rows than a one-row sine waves.txt file.
-    const txWaves = create_1D_Texture(device, Math.max(calc_constants.numberOfWaves, GENERATED_BOUNDARY_WAVE_TEXTURE_CAPACITY), allTextures);  // stores spectrum wave input
-    // Added by Codex: End generated boundary wave texture capacity.
-    // Added by Codex: Start boundary time-series forcing texture allocation.
-    const boundaryTimeSeriesSouthSize = getBoundaryTimeSeriesTextureSize(boundaryTimeSeriesData.south);
-    const boundaryTimeSeriesNorthSize = getBoundaryTimeSeriesTextureSize(boundaryTimeSeriesData.north);
-    const boundaryTimeSeriesWestSize = getBoundaryTimeSeriesTextureSize(boundaryTimeSeriesData.west);
-    const boundaryTimeSeriesEastSize = getBoundaryTimeSeriesTextureSize(boundaryTimeSeriesData.east);
-    const txBoundaryTimeSeriesSouth = create_2D_Texture(device, boundaryTimeSeriesSouthSize.width, boundaryTimeSeriesSouthSize.height, allTextures);
-    const txBoundaryTimeSeriesNorth = create_2D_Texture(device, boundaryTimeSeriesNorthSize.width, boundaryTimeSeriesNorthSize.height, allTextures);
-    const txBoundaryTimeSeriesWest = create_2D_Texture(device, boundaryTimeSeriesWestSize.width, boundaryTimeSeriesWestSize.height, allTextures);
-    const txBoundaryTimeSeriesEast = create_2D_Texture(device, boundaryTimeSeriesEastSize.width, boundaryTimeSeriesEastSize.height, allTextures);
-    // Added by Codex: End boundary time-series forcing texture allocation.
+    const txWaves = create_1D_Texture(device, calc_constants.numberOfWaves, allTextures);  // stores spectrum wave input
+    const txWaves_Transect = create_2D_Texture(device, calc_constants.numberOfWaves, calc_constants.HEIGHT, allTextures);  // stores various mean values
     const txTimeSeries_Locations = create_1D_Texture(device, calc_constants.maxNumberOfTimeSeries, allTextures);  // stores spectrum wave input
     const txTimeSeries_Data = create_1D_Texture(device, calc_constants.maxNumberOfTimeSeries, allTextures);  // stores spectrum wave input
 
     // fill in the bathy texture
     let bathy2Dvec = copyBathyDataToTexture(calc_constants, bathy2D, device, txBottom);
-    // Added by Codex: Precompute latitude-dependent spherical metrics once per simulation initialization.
-    copySphericalMetricDataToTexture(calc_constants, device, txSphericalMetrics);
 
     // fill in the wave data texture
-    // if (calc_constants.numberOfWaves > 0) {
-    //     copyWaveDataToTexture(calc_constants, waveData, device, txWaves);
-    // }
-    // Added by Codex: Use one upload path for loaded spectra and UI-generated single-component sine waves.
-    refreshBoundaryWaveTexture(txWaves);
-    // Added by Codex: End startup boundary wave texture refresh.
-    // Added by Codex: Start boundary time-series forcing texture upload.
-    copyBoundaryTimeSeriesDataToTexture(boundaryTimeSeriesData.south, device, txBoundaryTimeSeriesSouth);
-    copyBoundaryTimeSeriesDataToTexture(boundaryTimeSeriesData.north, device, txBoundaryTimeSeriesNorth);
-    copyBoundaryTimeSeriesDataToTexture(boundaryTimeSeriesData.west, device, txBoundaryTimeSeriesWest);
-    copyBoundaryTimeSeriesDataToTexture(boundaryTimeSeriesData.east, device, txBoundaryTimeSeriesEast);
-    // Added by Codex: End boundary time-series forcing texture upload.
+    if (calc_constants.numberOfWaves > 0) {
+       // copyWaveDataToTexture(calc_constants, waveData, device, txWaves);
+        copyTransectWaveDataToTexture(calc_constants, waveData, device, txWaves_Transect);
+    }
 
     // fill in the time series location texture
     copyTSlocsToTexture(calc_constants, device, txTimeSeries_Locations)  
 
-    // create initial condition, initialize values
-    var writeStateFlag = 0; // used to indicate if we not writing any state (0), writing channel 1 (1), writing channel 2 (2), or writing channel 3 (3)
-    copyInitialConditionDataToTexture(calc_constants, device, bathy2D, txState, writeStateFlag);
-    copyInitialConditionDataToTexture(calc_constants, device, bathy2D, txstateUVstar, writeStateFlag);
-
-        // create initial bottom friction surface
-    if(etaInitialConditionFile || calc_constants.loadetaIC == 1){
-        console.log('Loading Initial Free Surface File')
-        calc_constants.loadetaIC = 1;
-        var etaICContent = null;
-        try { 
-            etaICContent = await etaInitialConditionFile.text()
-        } 
-        catch {
-            etaICContent = null;
-        }
-        let etaIC2D = await loadInitCondSurface(etaICContent, calc_constants); 
-        writeStateFlag = 1; // writing channel 1
-        copyInitialConditionDataToTexture(calc_constants, device, etaIC2D, txState, writeStateFlag)
-        copyInitialConditionDataToTexture(calc_constants, device, etaIC2D, txstateUVstar, writeStateFlag)
-    }
+    // create initial condition
+    copyInitialConditionDataToTexture(calc_constants, device, bathy2D, txState);
+    copyInitialConditionDataToTexture(calc_constants, device, bathy2D, txstateUVstar);
 
     // create initial bottom friction surface
     if(frictionFile){
-        console.log('Loading Friction Map File')
+        console.log('Loading Uploaded Friction Map File')
         calc_constants.loadFriction = 1;
         const frictionContent = await frictionFile.text();
         let friction2D = await loadFrictionSurface(frictionContent, calc_constants); 
-        writeStateFlag = 1; // writing channel 1
-        copyInitialConditionDataToTexture(calc_constants, device, friction2D, txBottomFriction, writeStateFlag)
+        copyInitialConditionDataToTexture(calc_constants, device, friction2D, txBottomFriction)
     } else  {    
         copyConstantValueToTexture(calc_constants, device, txBottomFriction, calc_constants.friction, 0.0, 0.0, 0.0);
     }
 
-    // create hard bottom elevation file
-    if(hardbottomFile){
-        console.log('Loading Hard Bottom Elevation File')
-        calc_constants.loadHardBottom = 1;
-        const HardBottomContent = await hardbottomFile.text();
-        let HardBottom2D = await loadHardBottomSurface(HardBottomContent, calc_constants); 
-        writeStateFlag = 1; // writing channel 1
-        copyInitialConditionDataToTexture(calc_constants, device, HardBottom2D, txHardBottom, writeStateFlag)
-    } else  {    
-        copyConstantValueToTexture(calc_constants, device, txHardBottom, -2.0 * calc_constants.base_depth, 0.0, 0.0, 0.0);
-    }
-
-
     // create tridiag coef matrices
     copyTridiagXDataToTexture(calc_constants, bathy2D, device, coefMatx, bathy2Dvec);
     copyTridiagYDataToTexture(calc_constants, bathy2D, device, coefMaty, bathy2Dvec);
```

#### CT1-266 지도 실패 플래그 대입

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:672; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:350; 아래 전체 diff의 +행 | 불일치 (E) | transect 판의 catch는 GoogleMapOverlay==0을 비교만 한다. 본판은 =0으로 대입하고 로드 플래그 둘도 0으로 초기화한다. 자기 catch 목적과 실제 대입이 모순한다. 본판의 한쪽 수정이다. |

본판 차이 줄의 마지막 수정: `bf8db50` 2026-05-24 (현재 675행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 353행 포함).

```diff
@@ -672,16 +350,9 @@
             calc_constants.IsGMMapLoaded = 1;
             calc_constants.IsOverlayMapLoaded = 1;
         }
-        // catch {
-        //     console.log('Unable to load Google Maps overlay')
-        //     calc_constants.GoogleMapOverlay == 0
-        // }
-        // CODEX: Treat Google Maps overlay failures as non-fatal so local/example overlays can still load.
-        catch (error) {
-            console.warn('Unable to load Google Maps overlay; continuing without it.', error);
-            calc_constants.GoogleMapOverlay = 0;
-            calc_constants.IsGMMapLoaded = 0;
-            calc_constants.IsOverlayMapLoaded = 0;
+        catch {
+            console.log('Unable to load Google Maps overlay')
+            calc_constants.GoogleMapOverlay == 0
         }
     }
```

#### CT1-267 화살표 영상 레이어

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:752; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:423; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 채워진 화살표를 레이어 10에 업로드한다. 영상 내용은 판독하지 않는다. |

본판 차이 줄의 마지막 수정: `3c1649b` 2026-02-11 (현재 755행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -752,10 +423,6 @@
     imageUrl = '/textures/arrow.png'; 
     imData = await loadImageBitmap(imageUrl);    
     copyImageBitmapToTexture(device, imData, txSamplePNGs, 9)
-    // filled arrow texture
-    imageUrl = '/textures/arrow_filled.png'; 
-    imData = await loadImageBitmap(imageUrl);    
-    copyImageBitmapToTexture(device, imData, txSamplePNGs, 10)
 
     // Model textures
     // red_brick texture
```

#### CT1-268 카메라 초기화 좌표

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:826; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:493; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 구면 각도 격자를 미터 척도로 바꾼다. 본판은 사용자 카메라 위치·yaw·pitch·lookDist를 적용한다. transect 판은 simWidth·simHeight의 Cartesian 기본 카메라를 쓴다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 829행 포함); `61505f2` 2025-05-08 (현재 887행 포함); `f183cc2` 2026-02-01 (현재 889행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 503행 포함).

```diff
@@ -826,101 +493,33 @@
     const simWidth   = calc_constants.WIDTH  * calc_constants.dx;
     const simHeight  = calc_constants.HEIGHT * calc_constants.dy;
     const simDim = Math.sqrt(simWidth*simWidth + simHeight*simHeight);
-    // Added by Codex: Start Explorer camera scaling for spherical grids.
-    const explorerCameraDegToRad = Math.PI / 180.0;
-    const explorerCameraMidLat = calc_constants.lat_LL + 0.5 * calc_constants.HEIGHT * calc_constants.dy;
-    const explorerCameraCosLat = Math.max(Math.abs(Math.cos(explorerCameraMidLat * explorerCameraDegToRad)), 1.0e-6);
-    const explorerCameraScaleX = calc_constants.grid_type == 2 ? Math.max(calc_constants.R_earth, 1.0) * explorerCameraCosLat * explorerCameraDegToRad : 1.0;
-    const explorerCameraScaleY = calc_constants.grid_type == 2 ? Math.max(calc_constants.R_earth, 1.0) * explorerCameraDegToRad : 1.0;
-    const explorerCameraDx = calc_constants.dx * explorerCameraScaleX;
-    const explorerCameraDy = calc_constants.dy * explorerCameraScaleY;
-    const explorerSimWidth = calc_constants.grid_type == 2 ? calc_constants.WIDTH * explorerCameraDx : simWidth;
-    const explorerSimHeight = calc_constants.grid_type == 2 ? calc_constants.HEIGHT * explorerCameraDy : simHeight;
-    const explorerSimDim = Math.sqrt(explorerSimWidth*explorerSimWidth + explorerSimHeight*explorerSimHeight);
-    // Added by Codex: End Explorer camera scaling for spherical grids.
     
     // reset view (in case its stored in json already)
     calc_constants.shift_x = 0.;
     calc_constants.shift_y = 0.;
     calc_constants.forward = 1.0;
     // base eye & forward vector
-    // var baseEye    = vec3.fromValues(
-    //   0.1 * simWidth,
-    //   0.1 * simHeight,
-    //   10.0 * calc_constants.base_depth
-    // );
-    // var baseTarget = vec3.fromValues(
-    //   0.5 * simWidth,
-    //   0.5 * simHeight,
-    //    0.0
-    // );
-    // Added by Codex: Use Explorer camera dimensions so spherical lon/lat grids start in meter-like view coordinates.
     var baseEye    = vec3.fromValues(
-      0.1 * explorerSimWidth,
-      0.1 * explorerSimHeight,
+      0.1 * simWidth,
+      0.1 * simHeight,
       10.0 * calc_constants.base_depth
     );
     var baseTarget = vec3.fromValues(
-      0.5 * explorerSimWidth,
-      0.5 * explorerSimHeight,
+      0.5 * simWidth,
+      0.5 * simHeight,
        0.0
     );
 
     if (calc_constants.river_sim == 1) { // river simulation
-        // baseEye = vec3.fromValues(
-        //     0.5 * simWidth,
-        //     0.5 * simHeight,
-        //     400.0 * calc_constants.base_depth);
-        // baseTarget = vec3.fromValues(
-        //     0.5 * simWidth,
-        //     0.5 * simHeight,
-        //     0.0);
-        // Added by Codex: Keep river camera initialization on the same Explorer camera coordinate scale.
         baseEye = vec3.fromValues(
-            0.5 * explorerSimWidth,
-            0.5 * explorerSimHeight,
+            0.5 * simWidth,
+            0.5 * simHeight,
             400.0 * calc_constants.base_depth);
         baseTarget = vec3.fromValues(
-            0.5 * explorerSimWidth,
-            0.5 * explorerSimHeight,
+            0.5 * simWidth,
+            0.5 * simHeight,
             0.0);
-    }
-
-    // user override for initial camera position
-    if (calc_constants.cameraInit_user == 1) {
-        // baseEye = vec3.fromValues(
-        //     calc_constants.cameraInit_x,
-        //     calc_constants.cameraInit_y,
-        //     calc_constants.cameraInit_z
-        // );
-        // Added by Codex: Interpret spherical cameraInit x/y in degree-domain units and convert to Explorer camera coordinates.
-        baseEye = vec3.fromValues(
-            calc_constants.grid_type == 2 ? calc_constants.cameraInit_x * explorerCameraScaleX : calc_constants.cameraInit_x,
-            calc_constants.grid_type == 2 ? calc_constants.cameraInit_y * explorerCameraScaleY : calc_constants.cameraInit_y,
-            calc_constants.cameraInit_z
-        );
-
-        const yaw   = calc_constants.cameraInit_yaw   * Math.PI / 180.0;
-        const pitch = calc_constants.cameraInit_pitch * Math.PI / 180.0;
-
-        const fwd = vec3.fromValues(
-            Math.cos(pitch) * Math.cos(yaw),
-            Math.cos(pitch) * Math.sin(yaw),
-            Math.sin(pitch)
-        );
-        vec3.normalize(fwd, fwd);
-
-        // const lookDist = (calc_constants.cameraInit_lookDist && calc_constants.cameraInit_lookDist > 0.0)
-        //     ? calc_constants.cameraInit_lookDist
-        //     : 0.5 * simDim;   // reasonable default
-        // Added by Codex: Default spherical camera look distance must use the Explorer camera coordinate scale.
-        const lookDist = (calc_constants.cameraInit_lookDist && calc_constants.cameraInit_lookDist > 0.0)
-            ? calc_constants.cameraInit_lookDist
-            : 0.5 * explorerSimDim;   // reasonable default
-
-        baseTarget = vec3.create();
-        vec3.scaleAndAdd(baseTarget, baseEye, fwd, lookDist);
-    }
+    }            
 
     const baseDir = vec3.create();
     vec3.subtract(baseDir, baseTarget, baseEye);
```

#### CT1-269 사용자 카메라 회전

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:930; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:529; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 사용자 yaw·pitch를 초기 각도로 적용한다. |

본판 차이 줄의 마지막 수정: `f183cc2` 2026-02-01 (현재 933행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -930,13 +529,6 @@
     if (calc_constants.river_sim == 1) { // river simulation
         initYaw =  Math.PI / 2.0; // river simulation yaw
     } 
-    
-    // if user provided yaw and pitch, you can also force them
-    if (calc_constants.cameraInit_user == 1) {
-        initYaw   = calc_constants.cameraInit_yaw   * Math.PI / 180.0;
-        initPitch = calc_constants.cameraInit_pitch * Math.PI / 180.0;
-    }
-
     calc_constants.rotationAngle_xz = initPitch * 180. / Math.PI;
     calc_constants.rotationAngle_xy = initYaw * 180. / Math.PI;
```

#### CT1-270 재구성 경사 격자간격

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:980; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:572; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 구면 격자의 각도 간격을 미터 근사값으로 바꿔 Froude 경사 제한에 전달한다. transect 판은 dx·dy를 그대로 전달한다. Cartesian 경로 값은 같다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 983행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 575행 포함).

```diff
@@ -980,13 +572,8 @@
     Pass1_view.setFloat32(28, calc_constants.whiteWaterDecayRate, true);           // f32
     Pass1_view.setFloat32(32, calc_constants.dt, true);           // f32
     Pass1_view.setFloat32(36, calc_constants.base_depth, true);       // f32
-    // Pass1_view.setFloat32(40, calc_constants.dx, true);           // f32
-    // Pass1_view.setFloat32(44, calc_constants.dy, true);           // f32
-    // Added by Codex: Pass1 only uses these spacings for a bed-slope Froude limiter, so spherical mode supplies approximate meters.
-    const Pass1_dx_for_slope = calc_constants.grid_type == 2 ? Math.max(calc_constants.R_earth, 1.0) * Math.max(Math.abs(Math.cos(0.5 * (calc_constants.lat_LL + calc_constants.lat_UR) * Math.PI / 180.0)), 1.0e-6) * Math.max(Math.abs(calc_constants.dx) * Math.PI / 180.0, 1.0e-12) : calc_constants.dx;
-    const Pass1_dy_for_slope = calc_constants.grid_type == 2 ? Math.max(calc_constants.R_earth, 1.0) * Math.max(Math.abs(calc_constants.dy) * Math.PI / 180.0, 1.0e-12) : calc_constants.dy;
-    Pass1_view.setFloat32(40, Pass1_dx_for_slope, true);           // f32
-    Pass1_view.setFloat32(44, Pass1_dy_for_slope, true);           // f32
+    Pass1_view.setFloat32(40, calc_constants.dx, true);           // f32
+    Pass1_view.setFloat32(44, calc_constants.dy, true);           // f32
     Pass1_view.setFloat32(48, calc_constants.delta, true);           // f32
 
     //  SedTrans_Pass1 Bindings & Uniforms Config
```

#### CT1-271 퇴적물 재구성 격자간격과 쇄파 입력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1004; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:591; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 동일한 구면 간격 변환을 사용한다. transect 판은 dx·dy를 그대로 쓴다. transect Pass2 바인드 그룹은 txBreaking을 받지 않는다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 1007행 포함); `b8b50c3` 2025-06-08 (현재 1015행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 594행 포함).

```diff
@@ -1004,15 +591,12 @@
     SedTrans_Pass1_view.setFloat32(28, calc_constants.whiteWaterDecayRate, true);           // f32
     SedTrans_Pass1_view.setFloat32(32, calc_constants.dt, true);           // f32
     SedTrans_Pass1_view.setFloat32(36, calc_constants.base_depth, true);       // f32
-    // SedTrans_Pass1_view.setFloat32(40, calc_constants.dx, true);           // f32
-    // SedTrans_Pass1_view.setFloat32(44, calc_constants.dy, true);           // f32
-    // Added by Codex: Keep sediment reconstruction slope spacings consistent with Pass1 if this path is enabled outside spherical mode.
-    SedTrans_Pass1_view.setFloat32(40, Pass1_dx_for_slope, true);           // f32
-    SedTrans_Pass1_view.setFloat32(44, Pass1_dy_for_slope, true);           // f32
+    SedTrans_Pass1_view.setFloat32(40, calc_constants.dx, true);           // f32
+    SedTrans_Pass1_view.setFloat32(44, calc_constants.dy, true);           // f32
 
     // Pass2 Bindings & Uniforms Config
     const Pass2_BindGroupLayout = create_Pass2_BindGroupLayout(device);
-    const Pass2_BindGroup = create_Pass2_BindGroup(device, Pass2_uniformBuffer, txH, txU, txV, txBottom, txC, txHnear, txXFlux, txYFlux, txSed_C1, txSed_C2, txSed_C3, txSed_C4, txXFlux_Sed, txYFlux_Sed, txBreaking);
+    const Pass2_BindGroup = create_Pass2_BindGroup(device, Pass2_uniformBuffer, txH, txU, txV, txBottom, txC, txHnear, txXFlux, txYFlux, txSed_C1, txSed_C2, txSed_C3, txSed_C4, txXFlux_Sed, txYFlux_Sed);
     const Pass2_uniforms = new ArrayBuffer(256);  // smallest multiple of 256
     let Pass2_view = new DataView(Pass2_uniforms);
     Pass2_view.setUint32(0, calc_constants.WIDTH, true);          // u32
```

#### CT1-272 Pass2 확산계수 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1023; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:607; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 오프셋 32·36에 배경·쇄파 퇴적물 확산계수를 쓴다. |

본판 차이 줄의 마지막 수정: `b8b50c3` 2025-06-08 (현재 1026행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -1023,8 +607,6 @@
     Pass2_view.setFloat32(20, calc_constants.dy, true);           // f32
     Pass2_view.setFloat32(24, calc_constants.delta, true);           // f32
     Pass2_view.setInt32(28, calc_constants.useSedTransModel, true);   //i32
-    Pass2_view.setFloat32(32, calc_constants.sedTurbDispersion, true);           // f32
-    Pass2_view.setFloat32(36, calc_constants.sedBreakingDispersionCoef, true);           // f32
 
     // Breaking Pass Bindings & Uniforms Config
     const PassBreaking_BindGroupLayout = create_PassBreaking_BindGroupLayout(device);
```

#### CT1-273 Pass3 binding 19

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1073; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:655; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 grid_type==2이면 구면 계량 텍스처를 전달한다. transect 판은 항상 쇄파 응력 텍스처를 전달한다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 1076행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 658행 포함).

```diff
@@ -1073,9 +655,7 @@
 
     // Pass3 Bindings & Uniforms Config
     const Pass3_BindGroupLayout = create_Pass3_BindGroupLayout(device);
-    // const Pass3_BindGroup = create_Pass3_BindGroup(device, Pass3_uniformBuffer, txState, txBottom, txCW_groupings, txXFlux, txYFlux, oldGradients, oldOldGradients, predictedGradients, F_G_star_oldGradients, F_G_star_oldOldGradients, txstateUVstar, txBoundaryForcing, txNewState, dU_by_dt, predictedF_G_star, current_stateUVstar,txContSource,txBreaking, txDissipationFlux, txBottomFriction);
-    // Added by Codex: In spherical NLSW mode, reuse binding 19 for txSphericalMetrics because NLSW does not read txDissipationFlux.
-    const Pass3_BindGroup = create_Pass3_BindGroup(device, Pass3_uniformBuffer, txState, txBottom, txCW_groupings, txXFlux, txYFlux, oldGradients, oldOldGradients, predictedGradients, F_G_star_oldGradients, F_G_star_oldOldGradients, txstateUVstar, txBoundaryForcing, txNewState, dU_by_dt, predictedF_G_star, current_stateUVstar,txContSource,txBreaking, calc_constants.grid_type == 2 ? txSphericalMetrics : txDissipationFlux, txBottomFriction);
+    const Pass3_BindGroup = create_Pass3_BindGroup(device, Pass3_uniformBuffer, txState, txBottom, txCW_groupings, txXFlux, txYFlux, oldGradients, oldOldGradients, predictedGradients, F_G_star_oldGradients, F_G_star_oldOldGradients, txstateUVstar, txBoundaryForcing, txNewState, dU_by_dt, predictedF_G_star, current_stateUVstar,txContSource,txBreaking, txDissipationFlux, txBottomFriction);
     const Pass3_uniforms = new ArrayBuffer(256);  // smallest multiple of 256
     let Pass3_view = new DataView(Pass3_uniforms);
     Pass3_view.setInt32(0, calc_constants.WIDTH, true);          // u32
```

#### CT1-274 Pass3·퇴적물 바인딩 확장

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1114; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:694; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 와도 소산·지구 반지름 역수를 uniform 꼬리에 쓴다. 본판의 퇴적물 적분은 추가 5개 텍스처를 받는다. |

본판 차이 줄의 마지막 수정: `35b7f1c` 2026-01-15 (현재 1117행 포함); `afc1fe7` 2026-06-19 (현재 1118행 포함); `b8b50c3` 2025-06-08 (현재 1123행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 700행 포함).

```diff
@@ -1114,13 +694,10 @@
     Pass3_view.setInt32(132, calc_constants.east_boundary_type, true);           // i32
     Pass3_view.setInt32(136, calc_constants.south_boundary_type, true);           // i32
     Pass3_view.setInt32(140, calc_constants.north_boundary_type, true);       // i32
-    Pass3_view.setFloat32(144, calc_constants.vort_friction_factor, true);       // f32
-    // Added by Codex: Spherical NLSW shader reads one_over_R from the shared Pass3 uniform buffer tail.
-    Pass3_view.setFloat32(148, 1.0 / Math.max(calc_constants.R_earth, 1.0), true);       // f32
 
     // SedTrans_Pass3 Bindings & Uniforms Config
     const SedTrans_Pass3_BindGroupLayout = create_SedTrans_Pass3_BindGroupLayout(device);
-    const SedTrans_Pass3_BindGroup = create_SedTrans_Pass3_BindGroup(device, SedTrans_Pass3_uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed, txBreaking, txU, txV, txSed_C1, txHardBottom);
+    const SedTrans_Pass3_BindGroup = create_SedTrans_Pass3_BindGroup(device, SedTrans_Pass3_uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed);
     const SedTrans_Pass3_uniforms = new ArrayBuffer(256);  // smallest multiple of 256
     let SedTrans_Pass3_view = new DataView(SedTrans_Pass3_uniforms);
     SedTrans_Pass3_view.setInt32(0, calc_constants.WIDTH, true);          // u32
```

#### CT1-275 퇴적물 uniform과 단면 경계 리소스

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1143; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:720; 아래 전체 diff의 +행 | 코드에만 (C) | transect 판은 퇴적물 확장 uniform을 쓰지 않는다. transect 판의 두 BoundaryPass 바인드 그룹은 txWaves_Transect를 받는다. 본판은 지형 강제장과 4변 시계열을 받는다. |

본판 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1146행 포함); `5c60ac0` 2025-06-07 (현재 1148행 포함); `b8b50c3` 2025-06-08 (현재 1149행 포함); `ba9eb67` 2025-06-09 (현재 1150행 포함); `bb99fee` 2026-07-02 (현재 1155행 포함). transect 차이 줄의 마지막 수정: `3d8a61b` 2025-06-14 (현재 727행 포함).

```diff
@@ -1143,21 +720,12 @@
     SedTrans_Pass3_view.setFloat32(68, calc_constants.sedC1_erosion, true);           // f32
     SedTrans_Pass3_view.setFloat32(72, calc_constants.sedC1_n, true);           // f32
     SedTrans_Pass3_view.setFloat32(76, calc_constants.sedC1_fallvel, true);           // f32
-    SedTrans_Pass3_view.setFloat32(80, calc_constants.base_depth, true);           // f32
-    SedTrans_Pass3_view.setFloat32(84, calc_constants.delta, true);           // f32
-    SedTrans_Pass3_view.setFloat32(88, calc_constants.sedTurbDispersion, true);           // f32
-    SedTrans_Pass3_view.setFloat32(92, calc_constants.sedBreakingDispersionCoef, true);           // f32
-    SedTrans_Pass3_view.setFloat32(96, calc_constants.sedC1_bedloadMPM, true);           // f32
 
 
     // BoundaryPass Bindings & Uniforms Config
     const BoundaryPass_BindGroupLayout = create_BoundaryPass_BindGroupLayout(device);
-    // const BoundaryPass_BindGroup = create_BoundaryPass_BindGroup(device, BoundaryPass_uniformBuffer, current_stateUVstar, txBottom, txWaves, txNewState_Sed, txtemp_boundary, txtemp_boundary_Sed, txBreaking, txtemp_Breaking, txBoundaryForcing);
-    // Added by Codex: Pass boundary time-series forcing textures into BoundaryPass.
-    const BoundaryPass_BindGroup = create_BoundaryPass_BindGroup(device, BoundaryPass_uniformBuffer, current_stateUVstar, txBottom, txWaves, txNewState_Sed, txtemp_boundary, txtemp_boundary_Sed, txBreaking, txtemp_Breaking, txBoundaryForcing, txBoundaryTimeSeriesSouth, txBoundaryTimeSeriesNorth, txBoundaryTimeSeriesWest, txBoundaryTimeSeriesEast);
-    // const BoundaryPass_BindGroup_NewState = create_BoundaryPass_BindGroup(device, BoundaryPass_uniformBuffer, txNewState, txBottom, txWaves, txNewState_Sed, txtemp_boundary, txtemp_boundary_Sed, txBreaking, txtemp_Breaking, txBoundaryForcing);
-    // Added by Codex: Pass the same boundary time-series forcing textures to the post-tridiagonal BoundaryPass bind group.
-    const BoundaryPass_BindGroup_NewState = create_BoundaryPass_BindGroup(device, BoundaryPass_uniformBuffer, txNewState, txBottom, txWaves, txNewState_Sed, txtemp_boundary, txtemp_boundary_Sed, txBreaking, txtemp_Breaking, txBoundaryForcing, txBoundaryTimeSeriesSouth, txBoundaryTimeSeriesNorth, txBoundaryTimeSeriesWest, txBoundaryTimeSeriesEast);
+    const BoundaryPass_BindGroup = create_BoundaryPass_BindGroup(device, BoundaryPass_uniformBuffer, current_stateUVstar, txBottom, txWaves, txNewState_Sed, txtemp_boundary, txtemp_boundary_Sed, txBreaking, txtemp_Breaking, txWaves_Transect);
+    const BoundaryPass_BindGroup_NewState = create_BoundaryPass_BindGroup(device, BoundaryPass_uniformBuffer, txNewState, txBottom, txWaves, txNewState_Sed, txtemp_boundary, txtemp_boundary_Sed, txBreaking, txtemp_Breaking, txWaves_Transect);
     const BoundaryPass_uniforms = new ArrayBuffer(256);  // smallest multiple of 256
     let BoundaryPass_view = new DataView(BoundaryPass_uniforms);
     BoundaryPass_view.setInt32(0, calc_constants.WIDTH, true);          // i32
```

#### CT1-276 경계 uniform과 x PCR 교대 바인딩

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1202; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:770; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 알고리즘·trough_factor·구면·시계열 uniform을 쓴다. 본판은 x PCR 계수 교대 바인드 그룹을 추가한다. |

본판 차이 줄의 마지막 수정: `896c491` 2026-01-17 (현재 1205행 포함); `bb99fee` 2026-07-02 (현재 1206행 포함); `984091f` 2026-05-24 (현재 1222행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -1202,28 +770,10 @@
     BoundaryPass_view.setFloat32(156, calc_constants.stage_200, true);           // f32 
     BoundaryPass_view.setFloat32(160, calc_constants.stage_500, true);           // f32 
     BoundaryPass_view.setFloat32(164, calc_constants.river_inflow_angle, true);           // f32 
-    BoundaryPass_view.setInt32(168, calc_constants.algochanges, true);           // i32
-    BoundaryPass_view.setFloat32(172,calc_constants.trough_factor, true);            // f32 
-    // Added by Codex: Start boundary time-series forcing uniforms.
-    BoundaryPass_view.setInt32(176, calc_constants.grid_type, true);              // i32
-    BoundaryPass_view.setFloat32(180, calc_constants.lon_LL, true);               // f32
-    BoundaryPass_view.setFloat32(184, calc_constants.lat_LL, true);               // f32
-    BoundaryPass_view.setInt32(188, calc_constants.ts_west_num_points, true);     // i32
-    BoundaryPass_view.setInt32(192, calc_constants.ts_east_num_points, true);     // i32
-    BoundaryPass_view.setInt32(196, calc_constants.ts_south_num_points, true);    // i32
-    BoundaryPass_view.setInt32(200, calc_constants.ts_north_num_points, true);    // i32
-    // updateBoundaryTimeSeriesUniforms(BoundaryPass_view, 0.0);
-    // Added by Codex: Initialize type-5 boundary lookup on the shifted/global model clock.
-    updateBoundaryTimeSeriesUniforms(BoundaryPass_view, calc_constants.start_time_shift);
-    // Added by Codex: End boundary time-series forcing uniforms.
     
     // TridiagX - Bindings & Uniforms Config
     const TridiagX_BindGroupLayout = create_Tridiag_BindGroupLayout(device);
-    // const TridiagX_BindGroup = create_Tridiag_BindGroup(device, TridiagX_uniformBuffer, newcoef_x, txNewState, current_stateUVstar, txtemp_PCRx, txtemp2_PCRx, txBottom);
-    // CODEX: PCR ping-pong bind groups avoid full-texture coefficient copy-back between iterations.
-    const TridiagX_BindGroup_BaseToA = create_Tridiag_BindGroup(device, TridiagX_uniformBuffer, coefMatx, txNewState, current_stateUVstar, newcoef_x, txtemp2_PCRx, txBottom);
     const TridiagX_BindGroup = create_Tridiag_BindGroup(device, TridiagX_uniformBuffer, newcoef_x, txNewState, current_stateUVstar, txtemp_PCRx, txtemp2_PCRx, txBottom);
-    const TridiagX_BindGroup_BToA = create_Tridiag_BindGroup(device, TridiagX_uniformBuffer, txtemp_PCRx, txNewState, current_stateUVstar, newcoef_x, txtemp2_PCRx, txBottom);
     const TridiagX_uniforms = new ArrayBuffer(256);  // smallest multiple of 256
     let TridiagX_view = new DataView(TridiagX_uniforms);
     TridiagX_view.setInt32(0, calc_constants.WIDTH, true);          // i32
```

#### CT1-277 y PCR 교대 바인딩

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1235; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:785; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 y 계수 교대 바인드 그룹을 만든다. transect 판은 y PCR을 실행하지 않지만 기본 바인드 그룹은 생성한다. |

본판 차이 줄의 마지막 수정: `984091f` 2026-05-24 (현재 1238행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -1235,11 +785,7 @@
 
     // TridiagY - Bindings & Uniforms Config
     const TridiagY_BindGroupLayout = create_Tridiag_BindGroupLayout(device);
-    // const TridiagY_BindGroup = create_Tridiag_BindGroup(device, TridiagY_uniformBuffer, newcoef_y, txNewState, current_stateUVstar, txtemp_PCRy, txtemp2_PCRy, txBottom);
-    // CODEX: PCR ping-pong bind groups avoid full-texture coefficient copy-back between iterations.
-    const TridiagY_BindGroup_BaseToA = create_Tridiag_BindGroup(device, TridiagY_uniformBuffer, coefMaty, txNewState, current_stateUVstar, newcoef_y, txtemp2_PCRy, txBottom);
     const TridiagY_BindGroup = create_Tridiag_BindGroup(device, TridiagY_uniformBuffer, newcoef_y, txNewState, current_stateUVstar, txtemp_PCRy, txtemp2_PCRy, txBottom);
-    const TridiagY_BindGroup_BToA = create_Tridiag_BindGroup(device, TridiagY_uniformBuffer, txtemp_PCRy, txNewState, current_stateUVstar, newcoef_y, txtemp2_PCRy, txBottom);
     const TridiagY_uniforms = new ArrayBuffer(256);  // smallest multiple of 256
     let TridiagY_view = new DataView(TridiagY_uniforms);
     TridiagY_view.setInt32(0, calc_constants.WIDTH, true);          // i32
```

#### CT1-278 바닥 갱신 바인드 그룹

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1251; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:797; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 hardbottom과 초기 바닥고를 전달한다. |

본판 차이 줄의 마지막 수정: `852ec28` 2025-06-13 (현재 1254행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 800행 포함).

```diff
@@ -1251,7 +797,7 @@
     
     // SedTrans_UpdateBottom -  Bindings & Uniforms Config
     const SedTrans_UpdateBottom_BindGroupLayout = create_SedTrans_UpdateBottom_BindGroupLayout(device);
-    const SedTrans_UpdateBottom_BindGroup = create_SedTrans_UpdateBottom_BindGroup(device, SedTrans_UpdateBottom_uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change, txHardBottom, txBottomInitial);
+    const SedTrans_UpdateBottom_BindGroup = create_SedTrans_UpdateBottom_BindGroup(device, SedTrans_UpdateBottom_uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change);
     const SedTrans_UpdateBottom_uniforms = new ArrayBuffer(256);  // smallest multiple of 256
     let SedTrans_UpdateBottom_view = new DataView(SedTrans_UpdateBottom_uniforms);
     SedTrans_UpdateBottom_view.setInt32(0, calc_constants.WIDTH, true);          // i32
```

#### CT1-279 바닥 갱신 경계 uniform

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1263; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:809; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 오프셋 36·40·44·48에 4변 경계 유형을 쓴다. |

본판 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1266행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -1263,10 +809,6 @@
     SedTrans_UpdateBottom_view.setInt32(24, calc_constants.timeScheme, true);       // f32
     SedTrans_UpdateBottom_view.setInt32(28, calc_constants.pred_or_corrector, true);       // i32
     SedTrans_UpdateBottom_view.setFloat32(32, calc_constants.sedC1_n, true);           // f32
-    SedTrans_UpdateBottom_view.setInt32(36, calc_constants.west_boundary_type, true);       // i32
-    SedTrans_UpdateBottom_view.setInt32(40, calc_constants.east_boundary_type, true);           // i32
-    SedTrans_UpdateBottom_view.setInt32(44, calc_constants.south_boundary_type, true);           // i32
-    SedTrans_UpdateBottom_view.setInt32(48, calc_constants.north_boundary_type, true);       // i32
 
     // Updateneardry -  Bindings & Uniforms Config
     const Updateneardry_BindGroupLayout = create_Updateneardry_BindGroupLayout(device);
```

#### CT1-280 평균 수면 입력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1294; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:836; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 CalcMeans에 txNewState를 전달한다. |

본판 차이 줄의 마지막 수정: `dc6cc2d` 2025-08-10 (현재 1297행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 839행 포함).

```diff
@@ -1294,7 +836,7 @@
 
     // CalcMeans -  Bindings & Uniforms Config
     const CalcMeans_BindGroupLayout = create_CalcMeans_BindGroupLayout(device);
-    const CalcMeans_BindGroup = create_CalcMeans_BindGroup(device, CalcMeans_uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC, txNewState);
+    const CalcMeans_BindGroup = create_CalcMeans_BindGroup(device, CalcMeans_uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC);
     const CalcMeans_uniforms = new ArrayBuffer(256);  // smallest multiple of 256s
     let CalcMeans_view = new DataView(CalcMeans_uniforms);
     CalcMeans_view.setInt32(0, calc_constants.n_time_steps_means, true);          // i32
```

#### CT1-281 교란 누적 침식 전달

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1314; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:856; 아래 전체 diff의 +행 | 불일치 (E) | 본판만 AddDisturbance에 txBotChange_Sed를 전달한다. 한쪽 지형 누적 보존 결함 수정이다. |

본판 차이 줄의 마지막 수정: `4353b85` 2025-06-09 (현재 1317행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 859행 포함).

```diff
@@ -1314,7 +856,7 @@
 
     // AddDisturbance -  Bindings & Uniforms Config 
     const AddDisturbance_BindGroupLayout = create_AddDisturbance_BindGroupLayout(device);
-    const AddDisturbance_BindGroup = create_AddDisturbance_BindGroup(device, AddDisturbance_uniformBuffer, txBottom, txstateUVstar, txBottomInitial, txtemp_AddDisturbance, txBoundaryForcing, txtemp_bottom, txBotChange_Sed);
+    const AddDisturbance_BindGroup = create_AddDisturbance_BindGroup(device, AddDisturbance_uniformBuffer, txBottom, txstateUVstar, txBottomInitial, txtemp_AddDisturbance, txBoundaryForcing, txtemp_bottom);
     const AddDisturbance_uniforms = new ArrayBuffer(256);  // smallest multiple of 256s
     let AddDisturbance_view = new DataView(AddDisturbance_uniforms);
     AddDisturbance_view.setInt32(0, calc_constants.WIDTH, true);          // i32
```

#### CT1-282 선형 구조물 uniform과 툴팁 binding

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1362; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:904; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 선형 구조물 오프셋 64–92를 갱신한다. 본판만 ExtractTimeSeries에 txMeans_Speed를 전달한다. 공백 차이는 물리 값을 바꾸지 않는다. |

본판 차이 줄의 마지막 수정: `98f41c9` 2024-04-18 (현재 1365행 포함); `1dffd9d` 2024-04-19 (현재 1367행 포함); `d778fe7` 2026-06-02 (현재 1368행 포함); `397c575` 2025-09-09 (현재 1383행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 907행 포함).

```diff
@@ -1362,25 +904,13 @@
     MouseClickChange_view.setFloat32(40, calc_constants.base_depth, true);             // f32 
     MouseClickChange_view.setInt32(44, calc_constants.whichPanelisOpen, true);             // i32  
     MouseClickChange_view.setInt32(48, calc_constants.designcomponentToAdd, true);             // i32  
-    MouseClickChange_view.setFloat32(52, calc_constants.designcomponent_Radius, true);             // f32
-    MouseClickChange_view.setFloat32(56, calc_constants.designcomponent_Friction, true);             // f32
-    MouseClickChange_view.setFloat32(60, calc_constants.changeSeaLevel_delta, true);             // f32
-    // CODEX: Append linear-structure parameters to the MouseClickChange uniform buffer.
-    function updateMouseClickLinearStructureUniforms() {
-        MouseClickChange_view.setFloat32(64, calc_constants.designcomponent_CrestElev, true);             // f32
-        MouseClickChange_view.setFloat32(68, calc_constants.designcomponent_CrestWidth, true);             // f32
-        MouseClickChange_view.setFloat32(72, calc_constants.designcomponent_SideSlope, true);             // f32
-        MouseClickChange_view.setFloat32(76, calc_constants.designcomponent_StartX, true);             // f32
-        MouseClickChange_view.setFloat32(80, calc_constants.designcomponent_StartY, true);             // f32
-        MouseClickChange_view.setFloat32(84, calc_constants.designcomponent_EndX, true);             // f32
-        MouseClickChange_view.setFloat32(88, calc_constants.designcomponent_EndY, true);             // f32
-        MouseClickChange_view.setInt32(92, calc_constants.designcomponent_AddLinearStructure, true);             // i32
-    }
-    updateMouseClickLinearStructureUniforms();
+    MouseClickChange_view.setFloat32(52, calc_constants.designcomponent_Radius, true);             // f32  
+    MouseClickChange_view.setFloat32(56, calc_constants.designcomponent_Friction, true);             // f32  
+    MouseClickChange_view.setFloat32(60, calc_constants.changeSeaLevel_delta, true);             // f32  
 
     // ExtractTimeSeries -  Bindings & Uniforms Config
     const ExtractTimeSeries_BindGroupLayout = create_ExtractTimeSeries_BindGroupLayout(device);
-    const ExtractTimeSeries_BindGroup = create_ExtractTimeSeries_BindGroup(device, ExtractTimeSeries_uniformBuffer, txBottom, txBottomFriction, txContSource, txState, txWaveHeight, txTimeSeries_Locations, txTimeSeries_Data, txMeans_Speed);
+    const ExtractTimeSeries_BindGroup = create_ExtractTimeSeries_BindGroup(device, ExtractTimeSeries_uniformBuffer, txBottom, txBottomFriction, txContSource, txState, txWaveHeight, txTimeSeries_Locations, txTimeSeries_Data);
     const ExtractTimeSeries_uniforms = new ArrayBuffer(256);  // smallest multiple of 256s
     let ExtractTimeSeries_view = new DataView(ExtractTimeSeries_uniforms);
     ExtractTimeSeries_view.setInt32(0, calc_constants.WIDTH, true);          // i32
```

#### CT1-283 시계열 시각과 중첩 추출 설정

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1389; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:919; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 시작 시각 이동을 점 시계열 uniform에 반영한다. 본판만 교란 유형과 중첩 경계 추출 레이아웃을 설정한다. transect 판은 시간 0에서 시작한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 1392행 포함); `397c575` 2025-09-09 (현재 1396행 포함); `efe44a2` 2024-04-02 (현재 1397행 포함); `c4be488` 2026-07-13 (현재 1400행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 922행 포함).

```diff
@@ -1389,27 +919,8 @@
     ExtractTimeSeries_view.setFloat32(12, calc_constants.dy, true);             // f32
     ExtractTimeSeries_view.setInt32(16, calc_constants.mouse_current_canvas_indX, true);             // i32
     ExtractTimeSeries_view.setInt32(20, calc_constants.mouse_current_canvas_indY, true);             // i32
-    // ExtractTimeSeries_view.setFloat32(24, 0.0, true);             // f32, total_time
-    // Added by Codex: Initialize point time-series extraction on the shifted/global model clock.
-    ExtractTimeSeries_view.setFloat32(24, calc_constants.start_time_shift, true);             // f32, total_time
+    ExtractTimeSeries_view.setFloat32(24, 0.0, true);             // f32, total_time 
     ExtractTimeSeries_view.setInt32(28, calc_constants.river_sim, true);             // i32
-    ExtractTimeSeries_view.setInt32(32, calc_constants.disturbanceType, true);             // i32
-
-    // Added by Codex: Start nested-grid boundary time-series extraction uniforms.
-    const ExtractNestedBoundaryTimeSeries_BindGroupLayout = create_ExtractNestedBoundaryTimeSeries_BindGroupLayout(device);
-    // const ExtractNestedBoundaryTimeSeries_uniforms = new ArrayBuffer(256);
-    // let ExtractNestedBoundaryTimeSeries_view = new DataView(ExtractNestedBoundaryTimeSeries_uniforms);
-    // ExtractNestedBoundaryTimeSeries_view.setInt32(0, calc_constants.WIDTH, true);          // i32
-    // ExtractNestedBoundaryTimeSeries_view.setInt32(4, calc_constants.HEIGHT, true);         // i32
-    // ExtractNestedBoundaryTimeSeries_view.setInt32(8, 0, true);                             // i32, i0
-    // ExtractNestedBoundaryTimeSeries_view.setInt32(12, 0, true);                            // i32, j0
-    // ExtractNestedBoundaryTimeSeries_view.setInt32(16, 0, true);                            // i32, i1
-    // ExtractNestedBoundaryTimeSeries_view.setInt32(20, 0, true);                            // i32, j1
-    // ExtractNestedBoundaryTimeSeries_view.setInt32(24, 1, true);                            // i32, nx
-    // ExtractNestedBoundaryTimeSeries_view.setInt32(28, 1, true);                            // i32, ny
-    // ExtractNestedBoundaryTimeSeries_view.setInt32(32, 0, true);                            // i32, sample_index
-    // Added by Codex: Per-rectangle extraction uniforms are created and packed in initializeNestedGridBoundaryOutputCapture().
-    // Added by Codex: End nested-grid boundary time-series extraction uniforms.
 
     // Skybox Bindings
     const SkyboxBindGroupLayout = createSkyboxBindGroupLayout(device);
```

#### CT1-284 render의 침식 입력 의미

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1448; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:959; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 erosion_Sed 자리의 리소스에 txBottomInitial을 전달한다. transect 판은 실제 erosion_Sed를 전달한다. 동일 binding의 의미를 두 판에서 혼용하면 안 된다. |

본판 차이 줄의 마지막 수정: `8c2b62b` 2025-08-24 (현재 1451행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 962행 포함).

```diff
@@ -1448,7 +959,7 @@
 
     // Render Bindings
     const RenderBindGroupLayout = createRenderBindGroupLayout(device);
-    var RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);
+    var RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);
     const Render_uniforms = new ArrayBuffer(Render_bufferSize);  // smallest multiple of 256
     let Render_view = new DataView(Render_uniforms);
     Render_view.setFloat32(0, calc_constants.colorVal_max, true);          // f32
```

#### CT1-285 셰이더 선택과 NLSW 초기화

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1505; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1016; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 모든 셰이더 경로에 /transect_version 접두어를 쓴다. 고차 flux는 HLLEM 파일이고 본판은 HLLC 파일이다. transect 판은 NLSW_or_Bous==0에서 Pass3_ShaderCode_Bous를 null로 남긴다. 뒤의 파이프라인 생성은 무조건 실행하므로 이 옵션의 초기화 계약과 모순한다. 본판은 Bous 소스를 먼저 읽어 이 상황을 피한다. 표시 uniform·hardbottom·중첩 추출·구면 선택 차이도 이 구간에 있다. |

본판 차이 줄의 마지막 수정: `0b4e990` 2025-05-16 (현재 1508행 포함); `d23dfb0` 2025-09-01 (현재 1510행 포함); `d778fe7` 2026-06-02 (현재 1511행 포함); `b8b50c3` 2025-06-08 (현재 1528행 포함); `dc6cc2d` 2025-08-10 (현재 1533행 포함); `ebc98a5` 2024-03-13 (현재 1537행 포함); `83dd100` 2025-05-12 (현재 1541행 포함); `19b63cf` 2025-11-07 (현재 1547행 포함); `c215adf` 2025-05-12 (현재 1550행 포함); `366ee34` 2024-04-08 (현재 1552행 포함); `67ca57c` 2025-05-22 (현재 1553행 포함); `afc1fe7` 2026-06-19 (현재 1555행 포함); `ff720ca` 2026-01-30 (현재 1564행 포함); `85c2ca2` 2024-03-19 (현재 1574행 포함); `63a12e3` 2023-10-19 (현재 1575행 포함); `0e8b502` 2023-10-31 (현재 1596행 포함); `efe44a2` 2024-04-02 (현재 1598행 포함); `9c5b1a6` 2023-10-27 (현재 1599행 포함); `bb99fee` 2026-07-02 (현재 1601행 포함); `30be4e9` 2025-04-29 (현재 1604행 포함); `e90945e` 2025-05-05 (현재 1606행 포함); `925b67e` 2025-05-03 (현재 1608행 포함); `471c581` 2024-01-04 (현재 1612행 포함); `34abfb1` 2025-04-23 (현재 1615행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1019행 포함); `3d8a61b` 2025-06-14 (현재 1031행 포함).

```diff
@@ -1505,114 +1016,88 @@
         Render_view.setFloat32(192 + i * 4, viewProj[i], /* littleEndian */ true);
     }
     Render_view.setInt32(256, calc_constants.ShowArrows, true);           // i32
-    Render_view.setFloat32(260, calc_constants.arrow_scale, true);          // f32
-    Render_view.setFloat32(264, calc_constants.arrow_density, true);          // f32
-    Render_view.setFloat32(268, calc_constants.disturbanceType, true);          // f32
-    // CODEX: Keep linear-structure endpoint preview uniforms synchronized from calc_constants.
-    function updateRenderLinearStructurePreviewUniforms() {
-        // const linearStructurePreviewOn = calc_constants.viewType == 1 && calc_constants.designcomponent_PreviewOn == 1 ? 1 : 0;
-        // CODEX: Only show the linear-structure preview while the engineered-design panel is open in Design mode.
-        const linearStructurePreviewOn = calc_constants.viewType == 1 && calc_constants.whichPanelisOpen == 2 && calc_constants.designcomponent_PreviewOn == 1 ? 1 : 0;
-        Render_view.setFloat32(272, calc_constants.designcomponent_StartX, true);          // f32
-        Render_view.setFloat32(276, calc_constants.designcomponent_StartY, true);          // f32
-        Render_view.setFloat32(280, calc_constants.designcomponent_EndX, true);          // f32
-        Render_view.setFloat32(284, calc_constants.designcomponent_EndY, true);          // f32
-        Render_view.setInt32(288, calc_constants.designcomponent_StartDefined, true);          // i32
-        Render_view.setInt32(292, calc_constants.designcomponent_EndDefined, true);          // i32
-        Render_view.setInt32(296, linearStructurePreviewOn, true);          // i32
-        Render_view.setInt32(300, 0, true);          // i32 padding
-    }
+    Render_view.setFloat32(260, calc_constants.arrow_scale, true);          // f32 
+    Render_view.setFloat32(264, calc_constants.arrow_density, true);          // f32 
 
     // Copy f32 data to f16 texture compute shader
     const Copytxf32_txf16_BindGroupLayout = create_Copytxf32_txf16_BindGroupLayout(device);
-    const Copytxf32_txf16_BindGroup = create_Copytxf32_txf16_BindGroup(device, Copytxf32_txf16_uniformBuffer, txNewState, txBottom, txMeans_Speed, txRenderVarsf16, txMeans_Momflux, txModelVelocities, txMeans, txHardBottom);
+    const Copytxf32_txf16_BindGroup = create_Copytxf32_txf16_BindGroup(device, Copytxf32_txf16_uniformBuffer, txNewState, txBottom, txMeans_Speed, txRenderVarsf16, txMeans_Momflux, txModelVelocities, txMeans);
     const Copytxf32_txf16_uniforms = new ArrayBuffer(256);  // smallest multiple of 256
     let Copytxf32_txf16_view = new DataView(Copytxf32_txf16_uniforms);
     Copytxf32_txf16_view.setInt32(0, calc_constants.WIDTH, true);          // i32
     Copytxf32_txf16_view.setInt32(4, calc_constants.HEIGHT, true);          // i32
-    Copytxf32_txf16_view.setFloat32(8, calc_constants.delta, true);           // f32
-    Copytxf32_txf16_view.setFloat32(12, calc_constants.base_depth, true);           // f32
 
     // Fetch the source code of various shaders used in the application.
-    const Pass0_ShaderCode = await fetchShader('/shaders/Pass0.wgsl');
+    const Pass0_ShaderCode = await fetchShader('/transect_version/shaders/Pass0.wgsl');
     var Pass1_ShaderCode = null;
     if (calc_constants.Accuracy_mode == 1) {
         console.log("Using 4th-order MUSCL-TVD reconstruction scheme in Pass1");
-        Pass1_ShaderCode = await fetchShader('/shaders/Pass1_HighOrder.wgsl');
+        Pass1_ShaderCode = await fetchShader('/transect_version/shaders/Pass1_HighOrder.wgsl');
     } else {
-        Pass1_ShaderCode = await fetchShader('/shaders/Pass1.wgsl');
+        Pass1_ShaderCode = await fetchShader('/transect_version/shaders/Pass1.wgsl');
     }
     var Pass2_ShaderCode = null;
     if (calc_constants.Accuracy_mode == 1) {
-        console.log("Using HLLC Flux Solver in Pass2");
-        Pass2_ShaderCode = await fetchShader('/shaders/Pass2_HighOrder_HLLC.wgsl');  
+        console.log("Using HLLEM Flux Solver in Pass2");
+        Pass2_ShaderCode = await fetchShader('/transect_version/shaders/Pass2_HighOrder.wgsl');  
     } else {
-        Pass2_ShaderCode = await fetchShader('/shaders/Pass2.wgsl');  
+        Pass2_ShaderCode = await fetchShader('/transect_version/shaders/Pass2.wgsl');  
     }
-    const PassBreaking_ShaderCode = await fetchShader('/shaders/Pass_Breaking.wgsl'); 
-    const Pass3A_Coulwave_ShaderCode= await fetchShader('/shaders/Pass3A_COULWAVE.wgsl')
-    const Pass3B_Coulwave_ShaderCode= await fetchShader('/shaders/Pass3B_COULWAVE.wgsl')
-    // const Pass3_ShaderCode_NLSW = await fetchShader('/shaders/Pass3_NLSW.wgsl')
-    // Added by Codex: Select the spherical NLSW source/integration shader only for grid_type == 2.
-    var Pass3_ShaderCode_NLSW = null;
-    if (calc_constants.grid_type == 2) {
-        console.log("Using spherical-grid NLSW equations in Pass3");
-        Pass3_ShaderCode_NLSW = await fetchShader('/shaders/Pass3_NLSW_Spherical.wgsl');
-    } else {
-        Pass3_ShaderCode_NLSW = await fetchShader('/shaders/Pass3_NLSW.wgsl');
-    }
-    var Pass3_ShaderCode_Bous = await fetchShader('/shaders/Pass3_Bous.wgsl');
+    const PassBreaking_ShaderCode = await fetchShader('/transect_version/shaders/Pass_Breaking.wgsl'); 
+    const Pass3A_Coulwave_ShaderCode= await fetchShader('/transect_version/shaders/Pass3A_COULWAVE.wgsl')
+    const Pass3B_Coulwave_ShaderCode= await fetchShader('/transect_version/shaders/Pass3B_COULWAVE.wgsl')
+    const Pass3_ShaderCode_NLSW = await fetchShader('/transect_version/shaders/Pass3_NLSW.wgsl')
+    var Pass3_ShaderCode_Bous = null;
     if (calc_constants.NLSW_or_Bous == 1) {
         console.log("Using Celeris equations in Boussinesq mode");
+        Pass3_ShaderCode_Bous = await fetchShader('/transect_version/shaders/Pass3_Bous.wgsl');
     }
     else if (calc_constants.NLSW_or_Bous == 2) {
         console.log("Using COULWAVE equations in Boussinesq mode");
-        Pass3_ShaderCode_Bous = await fetchShader('/shaders/Pass3_COULWAVE.wgsl');
+        Pass3_ShaderCode_Bous = await fetchShader('/transect_version/shaders/Pass3_COULWAVE.wgsl');
     }
     
-    const SedTrans_Pass1_ShaderCode = await fetchShader('/shaders/SedTrans_Pass1.wgsl');
-    const SedTrans_Pass3_ShaderCode = await fetchShader('/shaders/SedTrans_Pass3.wgsl')
-    const BoundaryPass_ShaderCode = await fetchShader('/shaders/BoundaryPass.wgsl');
+    const SedTrans_Pass1_ShaderCode = await fetchShader('/transect_version/shaders/SedTrans_Pass1.wgsl');
+    const SedTrans_Pass3_ShaderCode = await fetchShader('/transect_version/shaders/SedTrans_Pass3.wgsl')
+    const BoundaryPass_ShaderCode = await fetchShader('/transect_version/shaders/BoundaryPass.wgsl');
     
     var TridiagX_ShaderCode = null; var TridiagY_ShaderCode = null;  //we can likely fold thee back into a single shader
     if (calc_constants.NLSW_or_Bous == 2) {
-        TridiagX_ShaderCode = await fetchShader('/shaders/TriDiag_PCRx_COULWAVE.wgsl');
-        TridiagY_ShaderCode = await fetchShader('/shaders/TriDiag_PCRy_COULWAVE.wgsl');
+        TridiagX_ShaderCode = await fetchShader('/transect_version/shaders/TriDiag_PCRx_COULWAVE.wgsl');
+        TridiagY_ShaderCode = await fetchShader('/transect_version/shaders/TriDiag_PCRy_COULWAVE.wgsl');
     } else {
-        TridiagX_ShaderCode = await fetchShader('/shaders/TriDiag_PCRx.wgsl');
-        TridiagY_ShaderCode = await fetchShader('/shaders/TriDiag_PCRy.wgsl');
+        TridiagX_ShaderCode = await fetchShader('/transect_version/shaders/TriDiag_PCRx.wgsl');
+        TridiagY_ShaderCode = await fetchShader('/transect_version/shaders/TriDiag_PCRy.wgsl');
     }
 
-    const SedTrans_UpdateBottom_ShaderCode = await fetchShader('/shaders/SedTrans_UpdateBottom.wgsl');
-    const Updateneardry_ShaderCode = await fetchShader('/shaders/Update_neardry.wgsl');
+    const SedTrans_UpdateBottom_ShaderCode = await fetchShader('/transect_version/shaders/SedTrans_UpdateBottom.wgsl');
+    const Updateneardry_ShaderCode = await fetchShader('/transect_version/shaders/Update_neardry.wgsl');
     
     var UpdateTrid_ShaderCode = null;  // we can likely fold these back into a single shader
     if (calc_constants.NLSW_or_Bous == 2) {
-        UpdateTrid_ShaderCode = await fetchShader('/shaders/Update_TriDiag_coef_COULWAVE.wgsl');
+        UpdateTrid_ShaderCode = await fetchShader('/transect_version/shaders/Update_TriDiag_coef_COULWAVE.wgsl');
     } else {
-        UpdateTrid_ShaderCode = await fetchShader('/shaders/Update_TriDiag_coef.wgsl');
+        UpdateTrid_ShaderCode = await fetchShader('/transect_version/shaders/Update_TriDiag_coef.wgsl');
     }
 
-    const CalcMeans_ShaderCode = await fetchShader('/shaders/CalcMeans.wgsl');
-    const CalcWaveHeight_ShaderCode = await fetchShader('/shaders/CalcWaveHeight.wgsl');
-    const AddDisturbance_ShaderCode = await fetchShader('/shaders/AddDisturbance.wgsl');
-    const MouseClickChange_ShaderCode = await fetchShader('/shaders/MouseClickChange.wgsl');
-    const ExtractTimeSeries_ShaderCode = await fetchShader('/shaders/ExtractTimeSeries.wgsl');
-    // Added by Codex: Fetch nested-grid boundary time-series extraction shader.
-    const ExtractNestedBoundaryTimeSeries_ShaderCode = await fetchShader('/shaders/ExtractNestedBoundaryTimeSeries.wgsl');
-
-    const Skybox_vertexShaderCode = await fetchShader('/shaders/skybox.vertex.wgsl');
-    const Skybox_fragmentShaderCode = await fetchShader('/shaders/skybox.fragment.wgsl');
-    //const Duck_vertexShaderCode = await fetchShader('/shaders/duck.vertex.wgsl');
-    //const Duck_fragmentShaderCode = await fetchShader('/shaders/duck.fragment.wgsl');
-    const Model_vertexShaderCode = await fetchShader('/shaders/model.vertex.wgsl');
-    const Model_fragmentShaderCode = await fetchShader('/shaders/model.fragment.wgsl');
-
-    const vertexShaderCode = await fetchShader('/shaders/vertex.wgsl');
-    const vertex3DShaderCode = await fetchShader('/shaders/vertex3D.wgsl');
-    const fragmentShaderCode = await fetchShader('/shaders/fragment.wgsl');
+    const CalcMeans_ShaderCode = await fetchShader('/transect_version/shaders/CalcMeans.wgsl');
+    const CalcWaveHeight_ShaderCode = await fetchShader('/transect_version/shaders/CalcWaveHeight.wgsl');
+    const AddDisturbance_ShaderCode = await fetchShader('/transect_version/shaders/AddDisturbance.wgsl');
+    const MouseClickChange_ShaderCode = await fetchShader('/transect_version/shaders/MouseClickChange.wgsl');
+    const ExtractTimeSeries_ShaderCode = await fetchShader('/transect_version/shaders/ExtractTimeSeries.wgsl');
+
+    const Skybox_vertexShaderCode = await fetchShader('/transect_version/shaders/skybox.vertex.wgsl');
+    const Skybox_fragmentShaderCode = await fetchShader('/transect_version/shaders/skybox.fragment.wgsl');
+    //const Duck_vertexShaderCode = await fetchShader('/transect_version/shaders/duck.vertex.wgsl');
+    //const Duck_fragmentShaderCode = await fetchShader('/transect_version/shaders/duck.fragment.wgsl');
+    const Model_vertexShaderCode = await fetchShader('/transect_version/shaders/model.vertex.wgsl');
+    const Model_fragmentShaderCode = await fetchShader('/transect_version/shaders/model.fragment.wgsl');
+
+    const vertexShaderCode = await fetchShader('/transect_version/shaders/vertex.wgsl');
+    const vertex3DShaderCode = await fetchShader('/transect_version/shaders/vertex3D.wgsl');
+    const fragmentShaderCode = await fetchShader('/transect_version/shaders/fragment.wgsl');
 
-    const Copytxf32_txf16_ShaderCode = await fetchShader('/shaders/Copytxf32_txf16.wgsl');
+    const Copytxf32_txf16_ShaderCode = await fetchShader('/transect_version/shaders/Copytxf32_txf16.wgsl');
     console.log("Shaders loaded.");
 
     // Configure the pipelines, one for each shader.
```

#### CT1-286 render 파이프라인 미리 생성

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1637; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1122; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 quad와 vertexgrid 파이프라인을 미리 만든다. transect 판은 최초 quad만 만든 뒤 프레임마다 선택한 파이프라인을 새로 만든다. 본판만 중첩 추출 파이프라인을 만든다. 본판은 2026-02-13 08860f0에서 이 반복 생성을 줄였다. 같은 판의 초기 파이프라인 생성 경로와 프레임 내 재사용 원칙을 함께 근거로 중간 강도의 결함 후보로 둔다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 1640행 포함); `08860f0` 2026-02-13 (현재 1646행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1129행 포함).

```diff
@@ -1637,17 +1122,11 @@
     const AddDisturbance_Pipeline = createComputePipeline(device, AddDisturbance_ShaderCode, AddDisturbance_BindGroupLayout, allComputePipelines);
     const MouseClickChange_Pipeline = createComputePipeline(device, MouseClickChange_ShaderCode, MouseClickChange_BindGroupLayout, allComputePipelines);
     const ExtractTimeSeries_Pipeline = createComputePipeline(device, ExtractTimeSeries_ShaderCode, ExtractTimeSeries_BindGroupLayout, allComputePipelines);
-    // Added by Codex: Pipeline for deferred nested-grid boundary time-series extraction.
-    const ExtractNestedBoundaryTimeSeries_Pipeline = createComputePipeline(device, ExtractNestedBoundaryTimeSeries_ShaderCode, ExtractNestedBoundaryTimeSeries_BindGroupLayout, allComputePipelines);
 
     const SkyboxPipeline = createSkyboxPipeline(device, Skybox_vertexShaderCode, Skybox_fragmentShaderCode, swapChainFormat, SkyboxBindGroupLayout);
     //const DuckPipeline = createDuckPipeline(device, Duck_vertexShaderCode, Duck_fragmentShaderCode, swapChainFormat, DuckBindGroupLayout);
     const ModelPipeline = createModelPipeline(device, Model_vertexShaderCode, Model_fragmentShaderCode, swapChainFormat, ModelBindGroupLayout);
-    
-    const RenderPipeline_quad = createRenderPipeline(device, vertexShaderCode, fragmentShaderCode, swapChainFormat, RenderBindGroupLayout, 'depth24plus');
-    const RenderPipeline_vertexgrid = createRenderPipeline_vertexgrid(device, vertex3DShaderCode, fragmentShaderCode, swapChainFormat, RenderBindGroupLayout, 'depth24plus');
-    var RenderPipeline = RenderPipeline_quad;
-
+    var RenderPipeline = createRenderPipeline(device, vertexShaderCode, fragmentShaderCode, swapChainFormat, RenderBindGroupLayout);
     const Copytxf32_txf16_Pipeline = createComputePipeline(device, Copytxf32_txf16_ShaderCode, Copytxf32_txf16_BindGroupLayout, allComputePipelines);
 
     console.log("Pipelines set up.");
```

#### CT1-287 격자 vertex 개수

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1684; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1163; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 마지막 strip을 한 번 더 생성한다. numVertices는 2*HEIGHT*WIDTH로 고정한다. 본판은 실제 vertices.length/2를 사용한다. HEIGHT>1에서 transect 실제 vertex 수는 2*WIDTH*HEIGHT+2*HEIGHT-3이다. 고정 draw 수가 생성 개수와 다르다. 해석: 뒤에 더한 중복 strip 일부를 그리는 불필요한 처리다. 원래 마지막 줄 전체가 누락된다고 단정하지 않는다. |

본판 차이 줄의 마지막 수정: `471c581` 2024-01-04 (현재 1695행 포함); `c3c57a4` 2026-03-03 (현재 1703행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1166행 포함).

```diff
@@ -1684,24 +1163,43 @@
     // Define a simple grid as just a single quad (two triangles)
     const gridWidth = calc_constants.WIDTH;  // Number of vertices along the width
     const gridHeight = calc_constants.HEIGHT; // Number of vertices along the height
+    let numVertices = 2*gridHeight*gridWidth;
     let vertices = [];
 
     // Generate vertices for the grid
     for (let y = 0; y < gridHeight - 1; y++) {
+        // Start of new strip (except for the first row)
         if (y > 0) {
+            // Repeat the first vertex of this row (degenerate triangle)
             vertices.push(-1, 1 - 2 * y / (gridHeight - 1));
         }
         for (let x = 0; x < gridWidth; x++) {
-            vertices.push(-1 + 2 * x / (gridWidth - 1), 1 - 2 * y       / (gridHeight - 1));
+            // Top vertex of the current column
+            vertices.push(-1 + 2 * x / (gridWidth - 1), 1 - 2 * y / (gridHeight - 1));
+            // Bottom vertex of the current column
             vertices.push(-1 + 2 * x / (gridWidth - 1), 1 - 2 * (y + 1) / (gridHeight - 1));
         }
+        // End of strip (except for the last row)
         if (y < gridHeight - 2) {
+            // Repeat the last vertex of this row (degenerate triangle)
             vertices.push(1, 1 - 2 * (y + 1) / (gridHeight - 1));
         }
     }
+    
+    // Handle the last row separately to ensure it's included
+    if (gridHeight > 1) {
+        let lastY = gridHeight - 2;
+        // Repeat the last vertex of the second-to-last row (degenerate triangle)
+        vertices.push(1, 1 - 2 * lastY / (gridHeight - 1));
+        // Define the last row vertices
+        for (let x = 0; x < gridWidth; x++) {
+            // Top vertex of the current column (from the second-to-last row)
+            vertices.push(-1 + 2 * x / (gridWidth - 1), 1 - 2 * lastY / (gridHeight - 1));
+            // Bottom vertex of the current column (last row)
+            vertices.push(-1 + 2 * x / (gridWidth - 1), -1);
+        }
+    }
 
-    // Correct vertex count: 2*gridWidth vertices per strip, plus 2 degenerate vertices per interior strip join
-    const numVertices = vertices.length / 2;
     const gridVertices = new Float32Array(vertices);
     const gridVertexBuffer = device.createBuffer({
         size: gridVertices.byteLength,
```

#### CT1-288 시뮬레이션과 점 시계열 초기 시각

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1714; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1212; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 type5 시작 시각을 total_time에 더한다. 점 시계열은 일반 실행에서 0 기반을 유지하고 type5에서 절대 시각을 쓴다. transect 판은 두 시계를 0으로 둔다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 1717행 포함); `ebca435` 2026-07-20 (현재 1727행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1215행 포함).

```diff
@@ -1714,27 +1212,12 @@
     // Log that the buffers have been set up.
     console.log("Buffers set up.");
 
-    // let total_time = 0;          // Initialize time, which might be used for animations or simulations.
-    // Added by Codex: Start total_time on the loaded boundary-file clock for nested simulations.
-    let total_time = calc_constants.start_time_shift;          // Initialize time, which might be used for animations or simulations.
-    // Added by Codex: End total_time on the loaded boundary-file clock for nested simulations.
+    let total_time = 0;          // Initialize time, which might be used for animations or simulations.
     let frame_count = 0;   // Counter to keep track of the number of rendered frames.
     let frame_count_since_http_update = 0;   // Counter to keep track of the number of rendered frames.
     let total_time_since_http_update = 0;          // Initialize time, which might be used for animations or simulations.
     let frame_count_time_series = 0;   // Counter for time series
-    // let total_time_time_series = 0;          // duration for time series
-    // Added by Codex: Point time-series timestamps follow the same shifted/global clock as total_time.
-    // let total_time_time_series = calc_constants.start_time_shift;          // duration for time series
-    // Added by Codex: Start ordinary point gauges retain their original zero-based
-    // clock; only type-5 nested simulations use the shifted/global clock.
-    const useNestedPointTimeSeriesClock = calc_constants.west_boundary_type == 5 ||
-        calc_constants.east_boundary_type == 5 || calc_constants.south_boundary_type == 5 ||
-        calc_constants.north_boundary_type == 5;
-    let total_time_time_series = useNestedPointTimeSeriesClock ? calc_constants.start_time_shift : 0.0;
-    calc_constants.timeSeriesChartStartTime = total_time_time_series;
-    calc_constants.timeSeriesDataEpoch = 0;
-    let chartDataUpdateResetHandled = 0;
-    // Added by Codex: End ordinary point gauges retain their original zero-based clock.
+    let total_time_time_series = 0;          // duration for time series
     let frame_count_find_render_step = 0;   // Counter to keep track of the number of rendered frames.
     let frame_count_output = 0;   // Counter to keep track of the number of frames saved to file
     let dt_since_last_write = 0.0 // tracks amount of time since last file write
```

#### CT1-289 중첩 경계 출력 실행 상태

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:1771; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1254; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 사각형 표시·다중 상태·리소스 해제·인덱스 제한·별칭 설정 키·표본 수 제한·위치 좌표·uniform·시간별 캡처를 구현한다. 사각형마다 독립 시계를 쓴다. 출력 간격은 dt 이상으로 제한한다. GPU 텍스처 한도를 넘는 사각형은 건너뛴다. 전체 수집이 끝나면 다운로드한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 1774행 포함); `c4be488` 2026-07-13 (현재 1781행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -1771,444 +1254,6 @@
 
     update_colorbar(device, offscreenCanvas, ctx, calc_constants, txDraw, logo_left, logo_right)
 
-    // Added by Codex: Start nested-grid output rectangle overlay helpers.
-    async function uploadDrawOverlayCanvas() {
-        const imageBitmap = await createImageBitmap(offscreenCanvas);
-        device.queue.copyExternalImageToTexture({source: imageBitmap}, {texture: txDraw}, [imageBitmap.width, imageBitmap.height]);
-    }
-
-    function drawNestedGridOutputRectangleOutlinePath() {
-        // if (calc_constants.nestedGridOutput_active != 1) {
-        // Added by Codex: Draw every active/pending nested-grid output rectangle instead of only the legacy scalar rectangle.
-        const drawableRectangles = getNestedGridOutputDrawableRectangles();
-        if (calc_constants.nestedGridOutput_active != 1 || drawableRectangles.length <= 0) {
-            return false;
-        }
-
-        const maxI = Math.max(calc_constants.WIDTH - 1, 1);
-        const maxJ = Math.max(calc_constants.HEIGHT - 1, 1);
-        ctx.save();
-        ctx.strokeStyle = 'black';
-        ctx.lineWidth = Math.max(2, Math.round(Math.min(offscreenCanvas.width, offscreenCanvas.height) / 300));
-        for (const rectangle of drawableRectangles) {
-            const i0 = Math.max(0, Math.min(maxI, rectangle.i0));
-            const i1 = Math.max(0, Math.min(maxI, rectangle.i1));
-            const j0 = Math.max(0, Math.min(maxJ, rectangle.j0));
-            const j1 = Math.max(0, Math.min(maxJ, rectangle.j1));
-            const x0 = Math.min(i0, i1) / maxI * offscreenCanvas.width;
-            const x1 = Math.max(i0, i1) / maxI * offscreenCanvas.width;
-            // const y0 = Math.min(j0, j1) / maxJ * offscreenCanvas.height;
-            // const y1 = Math.max(j0, j1) / maxJ * offscreenCanvas.height;
-            // Added by Codex: Start nested-grid rectangle y-coordinate correction.
-            // The draw canvas is already vertically flipped, so invert model-space j only for the overlay.
-            const y0 = offscreenCanvas.height - Math.max(j0, j1) / maxJ * offscreenCanvas.height;
-            const y1 = offscreenCanvas.height - Math.min(j0, j1) / maxJ * offscreenCanvas.height;
-            // Added by Codex: End nested-grid rectangle y-coordinate correction.
-            ctx.strokeRect(x0, y0, Math.max(1, x1 - x0), Math.max(1, y1 - y0));
-        }
-        ctx.restore();
-        return true;
-    }
-
-    async function drawNestedGridOutputRectangleOutline() {
-        if (drawNestedGridOutputRectangleOutlinePath()) {
-            await uploadDrawOverlayCanvas();
-        }
-    }
-
-    async function redrawDrawOverlayBase() {
-        ctx.fillStyle = 'white';
-        ctx.fillRect(0, 0, offscreenCanvas.width, offscreenCanvas.height);
-        await update_colorbar(device, offscreenCanvas, ctx, calc_constants, txDraw, logo_left, logo_right);
-    }
-
-    async function redrawDrawOverlayWithNestedGridOutline() {
-        ctx.fillStyle = 'white';
-        ctx.fillRect(0, 0, offscreenCanvas.width, offscreenCanvas.height);
-        await update_colorbar(device, offscreenCanvas, ctx, calc_constants, txDraw, logo_left, logo_right);
-        await drawNestedGridOutputRectangleOutline();
-    }
-    // Added by Codex: End nested-grid output rectangle overlay helpers.
-
-    // Added by Codex: Start nested-grid boundary time-series output runtime.
-    // let nestedGridOutputState = {
-    //     active: false,
-    //     pendingDownload: false,
-    //     bindGroup: null,
-    //     txSouth: null,
-    //     txNorth: null,
-    //     txWest: null,
-    //     txEast: null,
-    //     capturedTimes: [],
-    //     nx: 1,
-    //     ny: 1,
-    //     sampleCount: 0,
-    //     sampleIndex: 0,
-    //     startTime: 0.0,
-    //     endTime: 0.0,
-    //     outputDt: 1.0,
-    //     dispatchX: 1,
-    //     southLocations: [],
-    //     northLocations: [],
-    //     westLocations: [],
-    //     eastLocations: []
-    // };
-    // Added by Codex: Multi-rectangle output stores one independent state per requested rectangle.
-    let nestedGridOutputStates = [];
-
-    function createEmptyNestedGridOutputState() {
-        return {
-            active: false,
-            pendingDownload: false,
-            bindGroup: null,
-            uniformBuffer: null,
-            uniforms: null,
-            view: null,
-            txSouth: null,
-            txNorth: null,
-            txWest: null,
-            txEast: null,
-            capturedTimes: [],
-            nx: 1,
-            ny: 1,
-            sampleCount: 0,
-            sampleIndex: 0,
-            startTime: 0.0,
-            endTime: 0.0,
-            outputDt: 1.0,
-            dispatchX: 1,
-            i0: 0,
-            j0: 0,
-            i1: 0,
-            j1: 0,
-            isLegacy: false,
-            filePrefix: "nested",
-            etaThreshold: 0.0,
-            southLocations: [],
-            northLocations: [],
-            westLocations: [],
-            eastLocations: []
-        };
-    }
-
-    function destroyNestedGridOutputStateTextures(state) {
-        const textureKeys = ["txSouth", "txNorth", "txWest", "txEast"];
-        for (const key of textureKeys) {
-            if (state[key]) {
-                state[key].destroy();
-                allTextures.delete(state[key]);
-                state[key] = null;
-            }
-        }
-        if (state.uniformBuffer) {
-            state.uniformBuffer.destroy();
-            state.uniformBuffer = null;
-        }
-    }
-
-    // function destroyNestedGridOutputTextures() {
-    //     const textureKeys = ["txSouth", "txNorth", "txWest", "txEast"];
-    //     for (const key of textureKeys) {
-    //         if (nestedGridOutputState[key]) {
-    //             nestedGridOutputState[key].destroy();
-    //             allTextures.delete(nestedGridOutputState[key]);
-    //             nestedGridOutputState[key] = null;
-    //         }
-    //     }
-    // }
-    // Added by Codex: Destroy all rectangle output resources instead of a single legacy state.
-    function destroyNestedGridOutputTextures() {
-        for (const state of nestedGridOutputStates) {
-            destroyNestedGridOutputStateTextures(state);
-        }
-        nestedGridOutputStates = [];
-    }
-
-    function clampNestedGridOutputIndex(value, maxIndex) {
-        return Math.max(0, Math.min(maxIndex, Math.round(Number(value) || 0)));
-    }
-
-    function readNestedGridOutputValue(rectangle, keys, fallback) {
-        for (const key of keys) {
-            if (rectangle && rectangle[key] !== undefined && rectangle[key] !== null) {
-                return rectangle[key];
-            }
-        }
-        return fallback;
-    }
-
-    function nestedGridOutputDefaultPrefix(basePrefix, rectangleIndex) {
-        return rectangleIndex === 0 ? basePrefix : `${basePrefix}${rectangleIndex + 1}`;
-    }
-
-    function getNestedGridOutputRectangleSpecs() {
-        const basePrefix = String(calc_constants.nestedGridOutput_file_prefix || "nested");
-        const configuredRectangles = Array.isArray(calc_constants.nestedGridOutput_rectangles)
-            ? calc_constants.nestedGridOutput_rectangles
-            : [];
-        const enabledConfiguredRectangles = configuredRectangles
-            .map((rectangle, index) => ({ rectangle: rectangle || {}, index }))
-            .filter(({ rectangle }) => Number(readNestedGridOutputValue(rectangle, ["enabled"], 1)) != 0);
-
-        if (enabledConfiguredRectangles.length > 0) {
-            return enabledConfiguredRectangles.map(({ rectangle, index }) => {
-                const defaultPrefix = nestedGridOutputDefaultPrefix(basePrefix, index);
-                const filePrefix = String(readNestedGridOutputValue(rectangle, ["file_prefix", "filePrefix", "name"], defaultPrefix) || defaultPrefix);
-                return {
-                    isLegacy: false,
-                    rectangleIndex: index,
-                    name: String(readNestedGridOutputValue(rectangle, ["name"], filePrefix) || filePrefix),
-                    filePrefix,
-                    i0: readNestedGridOutputValue(rectangle, ["i0", "nestedGridOutput_i0"], calc_constants.nestedGridOutput_i0),
-                    j0: readNestedGridOutputValue(rectangle, ["j0", "nestedGridOutput_j0"], calc_constants.nestedGridOutput_j0),
-                    i1: readNestedGridOutputValue(rectangle, ["i1", "nestedGridOutput_i1"], calc_constants.nestedGridOutput_i1),
-                    j1: readNestedGridOutputValue(rectangle, ["j1", "nestedGridOutput_j1"], calc_constants.nestedGridOutput_j1),
-                    startTime: readNestedGridOutputValue(rectangle, ["start_time", "startTime", "nestedGridOutput_start_time"], calc_constants.nestedGridOutput_start_time),
-                    endTime: readNestedGridOutputValue(rectangle, ["end_time", "endTime", "nestedGridOutput_end_time"], calc_constants.nestedGridOutput_end_time),
-                    outputDt: readNestedGridOutputValue(rectangle, ["dt", "output_dt", "outputDt", "nestedGridOutput_dt"], calc_constants.nestedGridOutput_dt),
-                    maxSamples: readNestedGridOutputValue(rectangle, ["max_samples", "maxSamples", "nestedGridOutput_max_samples"], calc_constants.nestedGridOutput_max_samples),
-                    etaThreshold: readNestedGridOutputValue(rectangle, ["eta_threshold", "etaThreshold", "nestedEtaWriteThreshold"], calc_constants.nestedEtaWriteThreshold)
-                };
-            });
-        }
-
-        return [{
-            isLegacy: true,
-            rectangleIndex: 0,
-            name: basePrefix,
-            filePrefix: basePrefix,
-            i0: calc_constants.nestedGridOutput_i0,
-            j0: calc_constants.nestedGridOutput_j0,
-            i1: calc_constants.nestedGridOutput_i1,
-            j1: calc_constants.nestedGridOutput_j1,
-            startTime: calc_constants.nestedGridOutput_start_time,
-            endTime: calc_constants.nestedGridOutput_end_time,
-            outputDt: calc_constants.nestedGridOutput_dt,
-            maxSamples: calc_constants.nestedGridOutput_max_samples,
-            etaThreshold: calc_constants.nestedEtaWriteThreshold
-        }];
-    }
-
-    function getNestedGridOutputDrawableRectangles() {
-        return nestedGridOutputStates
-            .filter((state) => state.active || state.pendingDownload)
-            .map((state) => ({
-                i0: state.i0,
-                j0: state.j0,
-                i1: state.i1,
-                j1: state.j1
-            }));
-    }
-
-    // function capNestedGridOutputSamples() {
-    //     const maxSamples = Math.max(1, Math.floor(calc_constants.nestedGridOutput_max_samples || 8192));
-    //     const startTime = Number(calc_constants.nestedGridOutput_start_time) || 0.0;
-    //     let endTime = Number(calc_constants.nestedGridOutput_end_time) || startTime;
-    // Added by Codex: Cap sample count independently for each rectangle spec.
-    function capNestedGridOutputSamples(spec) {
-        const maxSamples = Math.max(1, Math.floor(Number(spec.maxSamples) || 8192));
-        const startTime = Number(spec.startTime) || 0.0;
-        let endTime = Number(spec.endTime) || startTime;
-        if (endTime < startTime) {
-            console.warn(`Nested-grid boundary output ${spec.filePrefix} end time is before start time; setting end time equal to start time.`);
-            endTime = startTime;
-        }
-
-        let outputDt = Number(spec.outputDt) || calc_constants.dt;
-        if (outputDt <= 0.0) {
-            outputDt = calc_constants.dt;
-            console.warn(`Nested-grid boundary output ${spec.filePrefix} dt must be positive; setting output dt to model dt ${outputDt}.`);
-        }
-        if (outputDt < calc_constants.dt) {
-            outputDt = calc_constants.dt;
-            console.warn(`Nested-grid boundary output ${spec.filePrefix} dt is smaller than the model dt; increasing output dt to ${outputDt}.`);
-        }
-
-        const duration = Math.max(0.0, endTime - startTime);
-        let sampleCount = Math.floor(duration / outputDt) + 1;
-        if (duration == 0.0) {
-            sampleCount = 1;
-        }
-        if (sampleCount > maxSamples) {
-            const requestedSampleCount = sampleCount;
-            outputDt = duration / Math.max(maxSamples - 1, 1);
-            sampleCount = maxSamples;
-            console.warn(`Nested-grid boundary output ${spec.filePrefix} requested ${requestedSampleCount} samples; capping at ${maxSamples} by increasing output dt to ${outputDt}.`);
-        }
-
-        if (spec.isLegacy) {
-            calc_constants.nestedGridOutput_start_time = startTime;
-            calc_constants.nestedGridOutput_end_time = endTime;
-            calc_constants.nestedGridOutput_dt = outputDt;
-            calc_constants.nestedGridOutput_sample_count = sampleCount;
-        }
-        return { startTime, endTime, outputDt, sampleCount };
-    }
-
-    function buildNestedGridOutputLocations(count, startIndex, spacing, origin, useAbsoluteGridCoordinates) {
-        const locations = new Array(count);
-        for (let n = 0; n < count; n++) {
-            locations[n] = useAbsoluteGridCoordinates ? origin + (startIndex + n) * spacing : n * spacing;
-        }
-        return locations;
-    }
-
-    function updateNestedGridOutputUniforms(state, sampleIndex) {
-        state.view.setInt32(0, calc_constants.WIDTH, true);
-        state.view.setInt32(4, calc_constants.HEIGHT, true);
-        state.view.setInt32(8, state.i0, true);
-        state.view.setInt32(12, state.j0, true);
-        state.view.setInt32(16, state.i1, true);
-        state.view.setInt32(20, state.j1, true);
-        state.view.setInt32(24, state.nx, true);
-        state.view.setInt32(28, state.ny, true);
-        state.view.setInt32(32, sampleIndex, true);
-    }
-
-    function syncLegacyNestedGridOutputFieldsFromState(state) {
-        if (!state) {
-            calc_constants.nestedGridOutput_sample_index = 0;
-            calc_constants.nestedGridOutput_sample_count = 0;
-            return;
-        }
-        calc_constants.nestedGridOutput_i0 = state.i0;
-        calc_constants.nestedGridOutput_i1 = state.i1;
-        calc_constants.nestedGridOutput_j0 = state.j0;
-        calc_constants.nestedGridOutput_j1 = state.j1;
-        calc_constants.nestedGridOutput_start_time = state.startTime;
-        calc_constants.nestedGridOutput_end_time = state.endTime;
-        calc_constants.nestedGridOutput_dt = state.outputDt;
-        calc_constants.nestedGridOutput_sample_count = state.sampleCount;
-        calc_constants.nestedGridOutput_sample_index = state.sampleIndex;
-        if (state.isLegacy) {
-            calc_constants.nestedGridOutput_file_prefix = state.filePrefix;
-            calc_constants.nestedEtaWriteThreshold = state.etaThreshold;
-        }
-    }
-
-    function initializeNestedGridBoundaryOutputCapture(currentTime) {
-        destroyNestedGridOutputTextures();
-
-        const rectangleSpecs = getNestedGridOutputRectangleSpecs();
-        const maxTextureDimension2D = device.limits?.maxTextureDimension2D || 8192;
-        const useAbsoluteGridCoordinates = calc_constants.grid_type == 2;
-        let totalEstimatedBytes = 0;
-
-        for (const spec of rectangleSpecs) {
-            const iLower = clampNestedGridOutputIndex(spec.i0, calc_constants.WIDTH - 1);
-            const iUpper = clampNestedGridOutputIndex(spec.i1, calc_constants.WIDTH - 1);
-            const jLower = clampNestedGridOutputIndex(spec.j0, calc_constants.HEIGHT - 1);
-            const jUpper = clampNestedGridOutputIndex(spec.j1, calc_constants.HEIGHT - 1);
-            const i0 = Math.min(iLower, iUpper);
-            const i1 = Math.max(iLower, iUpper);
-            const j0 = Math.min(jLower, jUpper);
-            const j1 = Math.max(jLower, jUpper);
-            const nx = Math.max(1, i1 - i0 + 1);
-            const ny = Math.max(1, j1 - j0 + 1);
-            let sampleInfo = capNestedGridOutputSamples(spec);
-            if (sampleInfo.startTime < currentTime) {
-                console.warn(`Nested-grid boundary output ${spec.filePrefix} start time ${sampleInfo.startTime} is before the current simulation time ${currentTime}; starting output at the current time.`);
-                spec.startTime = currentTime;
-                if (sampleInfo.endTime < currentTime) {
-                    spec.endTime = currentTime;
-                }
-                sampleInfo = capNestedGridOutputSamples(spec);
-            }
-
-            if (nx > maxTextureDimension2D || ny > maxTextureDimension2D || sampleInfo.sampleCount > maxTextureDimension2D) {
-                console.error(`Nested-grid boundary output ${spec.filePrefix} texture dimensions exceed this device's maxTextureDimension2D; skipping this rectangle.`);
-                continue;
-            }
-
-            const state = createEmptyNestedGridOutputState();
-            state.active = true;
-            state.txSouth = create_2D_Texture(device, nx, sampleInfo.sampleCount, allTextures);
-            state.txNorth = create_2D_Texture(device, nx, sampleInfo.sampleCount, allTextures);
-            state.txWest = create_2D_Texture(device, ny, sampleInfo.sampleCount, allTextures);
-            state.txEast = create_2D_Texture(device, ny, sampleInfo.sampleCount, allTextures);
-            state.nx = nx;
-            state.ny = ny;
-            state.sampleCount = sampleInfo.sampleCount;
-            state.startTime = sampleInfo.startTime;
-            state.endTime = sampleInfo.endTime;
-            state.outputDt = sampleInfo.outputDt;
-            state.dispatchX = Math.max(1, Math.ceil(Math.max(nx, ny) / 16));
-            state.i0 = i0;
-            state.i1 = i1;
-            state.j0 = j0;
-            state.j1 = j1;
-            state.filePrefix = spec.filePrefix;
-            state.isLegacy = spec.isLegacy;
-            state.etaThreshold = Math.max(0.0, Number(spec.etaThreshold) || 0.0);
-            state.southLocations = buildNestedGridOutputLocations(nx, i0, calc_constants.dx, calc_constants.lon_LL, useAbsoluteGridCoordinates);
-            state.northLocations = buildNestedGridOutputLocations(nx, i0, calc_constants.dx, calc_constants.lon_LL, useAbsoluteGridCoordinates);
-            state.westLocations = buildNestedGridOutputLocations(ny, j0, calc_constants.dy, calc_constants.lat_LL, useAbsoluteGridCoordinates);
-            state.eastLocations = buildNestedGridOutputLocations(ny, j0, calc_constants.dy, calc_constants.lat_LL, useAbsoluteGridCoordinates);
-            state.uniformBuffer = createUniformBuffer(device);
-            state.uniforms = new ArrayBuffer(256);
-            state.view = new DataView(state.uniforms);
-            updateNestedGridOutputUniforms(state, 0);
-            // nestedGridOutputState.bindGroup = create_ExtractNestedBoundaryTimeSeries_BindGroup(device, ExtractNestedBoundaryTimeSeries_uniformBuffer, txNewState, nestedGridOutputState.txSouth, nestedGridOutputState.txNorth, nestedGridOutputState.txWest, nestedGridOutputState.txEast);
-            // Added by Codex: Pass txBottom so dry nested-output samples are written as zero eta/hu/hv.
-            state.bindGroup = create_ExtractNestedBoundaryTimeSeries_BindGroup(device, state.uniformBuffer, txNewState, state.txSouth, state.txNorth, state.txWest, state.txEast, txBottom);
-            nestedGridOutputStates.push(state);
-            totalEstimatedBytes += (2 * nx + 2 * ny) * sampleInfo.sampleCount * 16;
-        }
-
-        calc_constants.nestedGridOutput_trigger = 0;
-        calc_constants.nestedGridOutput_rectangle_count = nestedGridOutputStates.length;
-        if (nestedGridOutputStates.length <= 0) {
-            calc_constants.nestedGridOutput_active = 0;
-            syncLegacyNestedGridOutputFieldsFromState(null);
-            console.warn("Nested-grid boundary output did not start because no valid rectangles were available.");
-            return;
-        }
-
-        calc_constants.nestedGridOutput_active = 1;
-        syncLegacyNestedGridOutputFieldsFromState(nestedGridOutputStates[0]);
-        redrawDrawOverlayWithNestedGridOutline();
-        if (totalEstimatedBytes > 512 * 1024 * 1024) {
-            console.warn(`Nested-grid boundary output allocated approximately ${(totalEstimatedBytes / (1024 * 1024)).toFixed(1)} MB of GPU texture storage across ${nestedGridOutputStates.length} rectangle(s).`);
-        }
-        console.log(`Nested-grid boundary output started for ${nestedGridOutputStates.length} rectangle(s): ${nestedGridOutputStates.map((state) => state.filePrefix).join(", ")}.`);
-    }
-
-    // function captureNestedGridBoundaryOutputIfNeeded(commandEncoderStack, currentTime) {
-    //     if (!nestedGridOutputState.active || nestedGridOutputState.sampleIndex >= nestedGridOutputState.sampleCount) {
-    //         return;
-    //     }
-    // Added by Codex: Capture all active rectangle outputs with independent sample clocks.
-    function captureNestedGridBoundaryOutputsIfNeeded(commandEncoderStack, currentTime) {
-        let maxSampleIndex = 0;
-        for (const state of nestedGridOutputStates) {
-            if (!state.active || state.sampleIndex >= state.sampleCount) {
-                maxSampleIndex = Math.max(maxSampleIndex, state.sampleIndex);
-                continue;
-            }
-
-            const targetTime = state.startTime + state.sampleIndex * state.outputDt;
-            if (currentTime + 0.5 * calc_constants.dt < targetTime) {
-                maxSampleIndex = Math.max(maxSampleIndex, state.sampleIndex);
-                continue;
-            }
-
-            updateNestedGridOutputUniforms(state, state.sampleIndex);
-            runComputeShader_EncStack(device, commandEncoderStack, state.uniformBuffer, state.uniforms, ExtractNestedBoundaryTimeSeries_Pipeline, state.bindGroup, state.dispatchX, 1);
-            state.capturedTimes.push(currentTime);
-            state.sampleIndex += 1;
-            maxSampleIndex = Math.max(maxSampleIndex, state.sampleIndex);
-
-            if (state.sampleIndex >= state.sampleCount) {
-                state.active = false;
-                state.pendingDownload = true;
-                console.log(`Nested-grid boundary output ${state.filePrefix} sampling complete; preparing files for download.`);
-            }
-        }
-        calc_constants.nestedGridOutput_sample_index = maxSampleIndex;
-        calc_constants.nestedGridOutput_active = nestedGridOutputStates.some((state) => state.active) ? 1 : 0;
-    }
-    // Added by Codex: End nested-grid boundary time-series output runtime.
-
     console.log("Compute / Render loop starting.");
     // This function, `frame`, serves as the main loop of the application,
     // executing repeatedly to update simulation state and render the results.
```

#### CT1-290 주기적 GPU 동기화

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2216; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1261; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 600000ms마다 onSubmittedWorkDone을 기다린다. transect 판에는 해당 운영 보정이 없다. |

본판 차이 줄의 마지막 수정: `7ae7da4` 2026-02-23 (현재 2219행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -2216,19 +1261,8 @@
     var startTime = new Date();  // This captures the current time, or the time at the start of rendering
     var startTime_update = new Date();  // This captures the current time, or the time at the start of rendering
 
-    var nowFlush = Date.now();
-    var lastGpuSyncTime = Date.now();
-
     async function frame() {
 
-        // flush the GPU command queue every 10 minutes to prevent memory issues and potential GPU connection loss
-        nowFlush = Date.now();
-        if (nowFlush - lastGpuSyncTime > 600000) {   // once per 10 minutes
-            console.log("Flushing GPU queue / clearing internal GPU resources");
-            await device.queue.onSubmittedWorkDone();
-            lastGpuSyncTime = nowFlush;
-        }
-
         // render step find logic, trying to find a render step that both maximizes the usage of the GPU
         // but does not over work it.  The need for this logic is that if the GPU is too overworked, which
         // here means that there is too much wall clock time between renderings of the wave field, the html
```

#### CT1-291 HTML 갱신 시 dt와 구면 모드

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2281; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1315; 아래 전체 diff의 +행 | 불일치 (A) | 복사 함수의 commandEncoder 인자만 다르다. 본판은 구면 모드·물리 격자간격·계량을 다시 계산한다. transect 판은 Cartesian CFL 식만 다시 계산한다. |

본판 차이 줄의 마지막 수정: `33f7ff6` 2026-02-13 (현재 2284행 포함); `afc1fe7` 2026-06-19 (현재 2296행 포함); `38a5072` 2025-01-21 (현재 2331행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1318행 포함).

```diff
@@ -2281,56 +1315,19 @@
         }
         // copy the initial bathy into a seperate texture
         if (frame_count == 0) {
-            runCopyTextures(device, calc_constants, txBottom, txBottomInitial)
+            runCopyTextures(device, commandEncoder, calc_constants, txBottom, txBottomInitial)
         }
         
         // store baseline wave height map
         if (calc_constants.save_baseline == 1) {
-            runCopyTextures(device, calc_constants, txWaveHeight, txBaseline_WaveHeight)
+            runCopyTextures(device, commandEncoder, calc_constants, txWaveHeight, txBaseline_WaveHeight)
             calc_constants.save_baseline = 0;
         }
 
         // update simulation parameters in buffers if they have been changed by user through html
         if (calc_constants.html_update > 0) {
 
-            // calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);
-            // Added by Codex: Start grid-type-specific timestep refresh for HTML-driven updates.
-            if (calc_constants.grid_type == 2) {
-                if (calc_constants.NLSW_or_Bous != 0) {
-                    console.warn("Spherical grid mode is currently NLSW-only; forcing NLSW_or_Bous to 0.");
-                    calc_constants.NLSW_or_Bous = 0;
-                }
-                if (calc_constants.Accuracy_mode != 0) {
-                    console.warn("Spherical grid mode currently uses the standard second-order NLSW path; forcing Accuracy_mode to 0.");
-                    calc_constants.Accuracy_mode = 0;
-                }
-                if (calc_constants.useSedTransModel != 0) {
-                    console.warn("Spherical grid mode does not currently support sediment transport; forcing useSedTransModel to 0.");
-                    calc_constants.useSedTransModel = 0;
-                }
-                if (calc_constants.useBreakingModel != 0) {
-                    console.warn("Spherical grid mode does not currently support the Cartesian breaking model; forcing useBreakingModel to 0.");
-                    calc_constants.useBreakingModel = 0;
-                }
-
-                const degToRad = Math.PI / 180.0;
-                const dlonRad = Math.max(Math.abs(calc_constants.dx) * degToRad, 1.0e-12);
-                const dlatRad = Math.max(Math.abs(calc_constants.dy) * degToRad, 1.0e-12);
-                const earthRadius = Math.max(calc_constants.R_earth, 1.0);
-                let minPhysicalGridSpacing = earthRadius * dlatRad;
-                for (let y = 0; y < calc_constants.HEIGHT; y++) {
-                    // const latRad = (calc_constants.lat_LL + y * calc_constants.dy) * degToRad;
-                    // Added by Codex: Use cell-center latitude because lat_LL is the lower-left corner.
-                    const latRad = (calc_constants.lat_LL + (y + 0.5) * calc_constants.dy) * degToRad;
-                    const cosLat = Math.max(Math.abs(Math.cos(latRad)), 1.0e-6);
-                    minPhysicalGridSpacing = Math.min(minPhysicalGridSpacing, earthRadius * cosLat * dlonRad);
-                }
-                calc_constants.dt = calc_constants.Courant_num * minPhysicalGridSpacing / Math.sqrt(calc_constants.g * calc_constants.base_depth);
-                copySphericalMetricDataToTexture(calc_constants, device, txSphericalMetrics);
-            } else {
-                calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);
-            }
-            // Added by Codex: End grid-type-specific timestep refresh for HTML-driven updates.
+            calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);
             calc_constants.TWO_THETA = calc_constants.Theta * 2.0;
             calc_constants.render_step = Math.round(calc_constants.render_step);
```

#### CT1-292 지구 반지름 역수 갱신

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2361; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1358; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 HTML 변경 뒤 Pass3의 one_over_R을 갱신한다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 2364행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -2361,8 +1358,6 @@
             Pass3_view.setFloat32(116, calc_constants.infiltrationRate, true);           // f32
             Pass3_view.setInt32(120, calc_constants.useBreakingModel, true);           // i32
             Pass3_view.setInt32(124, calc_constants.showBreaking, true);           // i32
-            // Added by Codex: Keep spherical one_over_R current if a config/UI update changes R_earth.
-            Pass3_view.setFloat32(148, 1.0 / Math.max(calc_constants.R_earth, 1.0), true);       // f32
 
             SedTrans_Pass3_view.setFloat32(8, calc_constants.dt, true);             // f32
             SedTrans_Pass3_view.setInt32(28, calc_constants.timeScheme, true);       // f32
```

#### CT1-293 추적자 초기화 복사

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2380; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1375; 아래 전체 diff의 +행 | 불일치 (F) | commandEncoder 인자 외에는 txzeros→txContSource 복사 조건과 범위가 같다. |

본판 차이 줄의 마지막 수정: `33f7ff6` 2026-02-13 (현재 2383행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1378행 포함).

```diff
@@ -2380,7 +1375,7 @@
             SedTrans_UpdateBottom_view.setFloat32(32, calc_constants.sedC1_n, true);           // f32            
 
             if(calc_constants.clearConc == 1){  // remove all passive tracer sources when changing overlay
-                runCopyTextures(device, calc_constants, txzeros, txContSource)
+                runCopyTextures(device, commandEncoder, calc_constants, txzeros, txContSource)
             }
 
             // make sure periodic conditions are always a pair
```

#### CT1-294 경계 UI 파랑 재생성

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2390; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1385; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 UI 변경에 맞춰 파랑 텍스처와 numberOfWaves uniform을 갱신한다. 양쪽은 주기 경계를 쌍으로 맞추는 호스트 코드를 유지한다. transect 셰이더는 주기 경계를 구현하지 않는다. |

본판 차이 줄의 마지막 수정: `1b1e7a3` 2024-06-24 (현재 2393행 포함); `9093d7f` 2026-06-01 (현재 2395행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1388행 포함).

```diff
@@ -2390,15 +1385,10 @@
             }
             if(calc_constants.south_boundary_type == 3 || calc_constants.north_boundary_type == 3){
                 calc_constants.south_boundary_type = 3;
-                calc_constants.north_boundary_type = 3;
+                calc_constants.north_boundary_type = 3; 
             }
-            // Added by Codex: Keep txWaves synchronized with the incident-wave UI before updating boundary uniforms.
-            refreshBoundaryWaveTexture(txWaves);
             BoundaryPass_view.setFloat32(8, calc_constants.dt, true);             // f32
             BoundaryPass_view.setFloat32(40, calc_constants.seaLevel, true);           // f32
-            // Added by Codex: The sine-wave UI changes numberOfWaves, so this uniform must be refreshed with the wave texture.
-            BoundaryPass_view.setInt32(52, calc_constants.numberOfWaves, true);             // i32
-            // Added by Codex: End UI boundary wave texture refresh.
             BoundaryPass_view.setInt32(56, calc_constants.west_boundary_type, true);       // f32
             BoundaryPass_view.setInt32(60, calc_constants.east_boundary_type, true);           // f32
             BoundaryPass_view.setInt32(64, calc_constants.south_boundary_type, true);           // f32
```

#### CT1-295 type5 위치·관측점 수 갱신

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2407; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1397; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 경계 원점과 4변 관측점 수를 다시 uniform에 쓴다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 2410행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -2407,14 +1397,6 @@
             BoundaryPass_view.setFloat32(92, calc_constants.incident_wave_H, true);           // f32 
             BoundaryPass_view.setFloat32(96, calc_constants.incident_wave_T, true);           // f32 
             BoundaryPass_view.setFloat32(100, calc_constants.incident_wave_direction, true);   
-            // Added by Codex: Keep grid-origin and station-count uniforms available for boundary_type == 5 forcing.
-            BoundaryPass_view.setInt32(176, calc_constants.grid_type, true);              // i32
-            BoundaryPass_view.setFloat32(180, calc_constants.lon_LL, true);               // f32
-            BoundaryPass_view.setFloat32(184, calc_constants.lat_LL, true);               // f32
-            BoundaryPass_view.setInt32(188, calc_constants.ts_west_num_points, true);     // i32
-            BoundaryPass_view.setInt32(192, calc_constants.ts_east_num_points, true);     // i32
-            BoundaryPass_view.setInt32(196, calc_constants.ts_south_num_points, true);    // i32
-            BoundaryPass_view.setInt32(200, calc_constants.ts_north_num_points, true);    // i32
             
             Pass3_view.setInt32(128, calc_constants.west_boundary_type, true);       // i32
             Pass3_view.setInt32(132, calc_constants.east_boundary_type, true);           // i32
```

#### CT1-296 Google overlay 바인드 그룹 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2432; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1414; 아래 전체 diff의 +행 | 불일치 (E) | transect 판의 overlay 전환 호출은 현재 createRenderBindGroup의 인자 목록과 맞지 않는다. sampler와 txTimeSeries_Locations 등이 한 칸씩 이동하고 끝 인자는 undefined가 된다. 본판은 전체 인자 목록으로 고쳤다. |

본판 차이 줄의 마지막 수정: `bf8db50` 2026-05-24 (현재 2435행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1417행 포함).

```diff
@@ -2432,9 +1414,7 @@
                     calc_constants.GMoffsetY = transforms.offsetY;
             
                     txOverlayMap = txGoogleMap;
-                    // RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, depostion_Sed, txBotChange_Sed, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs);
-                    // CODEX: Rebuild the render bind group with the current full argument list when switching overlays.
-                    RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);
+                    RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, depostion_Sed, txBotChange_Sed, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs);
    
                     console.log('Updating Overlay with Google Maps Image')
                     calc_constants.IsOverlayMapLoaded = 1;
```

#### CT1-297 위성 overlay 바인드 그룹 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2445; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1425; 아래 전체 diff의 +행 | 불일치 (E) | transect 판의 위성 overlay 전환 호출도 현재 함수 정의와 맞지 않는다. 본판은 txDesignComponents·두 sampler·f16 텍스처까지 전달하도록 고쳤다. |

본판 차이 줄의 마지막 수정: `bf8db50` 2026-05-24 (현재 2448행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1428행 포함).

```diff
@@ -2445,9 +1425,7 @@
                     calc_constants.GMoffsetY = 1.0;  // y-direction offset for sat image
                     
                     txOverlayMap = txSatMap;
-                    // RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, depostion_Sed, txBotChange_Sed, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs);
-                    // CODEX: Rebuild the render bind group with the current full argument list when switching overlays.
-                    RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);
+                    RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, depostion_Sed, txBotChange_Sed, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs);
    
                     console.log('Updating Overlay with Sat Image')
                     calc_constants.IsOverlayMapLoaded = 1;
```

#### CT1-298 범례와 중첩 사각형 재표시

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2484; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1462; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 활성 중첩 사각형 유무에 따라 범례·윤곽 업로드를 await한다. transect 판은 기존 update_colorbar를 호출한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 2487행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1465행 포함).

```diff
@@ -2484,13 +1462,7 @@
             // reset canvas
             ctx.fillStyle = 'white';
             ctx.fillRect(0, 0, offscreenCanvas.width, offscreenCanvas.height);
-            // update_colorbar(device, offscreenCanvas, ctx, calc_constants, txDraw, logo_left, logo_right) // update colorbar with new climits
-            // Added by Codex: Redraw the colorbar and nested-grid output rectangle in upload order.
-            if (calc_constants.nestedGridOutput_active == 1) {
-                await redrawDrawOverlayWithNestedGridOutline();
-            } else {
-                await redrawDrawOverlayBase();
-            }
+            update_colorbar(device, offscreenCanvas, ctx, calc_constants, txDraw, logo_left, logo_right) // update colorbar with new climits
 
             startTime_update = new Date();  // This captures the current time, or the time at the start of rendering
             frame_count_since_http_update = 0;
```

#### CT1-299 지형 편집 뒤 near-dry 갱신

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2521; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1493; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 mode 1에서만 near-dry를 다시 계산한다. 본판은 모든 모드에서 near-dry를 갱신하고 mode>=1에서 계수를 갱신한다. mode 2의 source 분산 차단이 near-dry를 읽으므로 두 경로가 모순할 수 있다. 선형 구조물 적용은 본판 후속 기능이다. 즉시 submit 호출의 인자 변화는 수치 순서를 보존한다. |

본판 차이 줄의 마지막 수정: `98f41c9` 2024-04-18 (현재 2524행 포함); `1dffd9d` 2024-04-19 (현재 2525행 포함); `d778fe7` 2026-06-02 (현재 2527행 포함); `33f7ff6` 2026-02-13 (현재 2530행 포함); `146a4ac` 2025-09-28 (현재 2538행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1496행 포함).

```diff
@@ -2521,53 +1493,34 @@
                 else if(calc_constants.designcomponentToAdd == 8) {calc_constants.designcomponent_Friction = calc_constants.designcomponent_Fric_Dune;} 
                 else if(calc_constants.designcomponentToAdd == 9) {calc_constants.designcomponent_Friction = calc_constants.designcomponent_Fric_Berm;} 
                 else if(calc_constants.designcomponentToAdd == 10) {calc_constants.designcomponent_Friction = calc_constants.designcomponent_Fric_Seawall;} 
-                MouseClickChange_view.setFloat32(56, calc_constants.designcomponent_Friction, true);             // f32
-                MouseClickChange_view.setFloat32(60, calc_constants.changeSeaLevel_delta, true);             // f32
+                MouseClickChange_view.setFloat32(56, calc_constants.designcomponent_Friction, true);             // f32  
+                MouseClickChange_view.setFloat32(60, calc_constants.changeSeaLevel_delta, true);             // f32  
                 calc_constants.changeSeaLevel_delta = 0.0; // once the change is added once, set to zero
-                // CODEX: Upload pending linear-structure parameters before running MouseClickChange.wgsl.
-                updateMouseClickLinearStructureUniforms();
 
-                runComputeShader(device, MouseClickChange_uniformBuffer, MouseClickChange_uniforms, MouseClickChange_Pipeline, MouseClickChange_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // update depth/friction based on mouse click
+                runComputeShader(device, commandEncoder, MouseClickChange_uniformBuffer, MouseClickChange_uniforms, MouseClickChange_Pipeline, MouseClickChange_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // update depth/friction based on mouse click
                 if(calc_constants.whichPanelisOpen == 3){
                     if(calc_constants.surfaceToChange == 1){  // when changing bath/topo
-                        runCopyTextures(device, calc_constants, txtemp_MouseClick, txBottom)
-                       // runCopyTextures(device, calc_constants, txtemp_MouseClick, txBottomInitial) // not sure if I should do this - cant change depth with prescribed motion slide
-                        runCopyTextures(device, calc_constants, txtemp_MouseClick2, txstateUVstar)
-                        runComputeShader(device, Updateneardry_uniformBuffer, Updateneardry_uniforms, Updateneardry_Pipeline, Updateneardry_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
-                        runCopyTextures(device, calc_constants, txtemp_bottom, txBottom)
-                        if (calc_constants.NLSW_or_Bous >= 1) { // only update for Celeris Boussinesq equations
+                        runCopyTextures(device, commandEncoder, calc_constants, txtemp_MouseClick, txBottom)
+                        runCopyTextures(device, commandEncoder, calc_constants, txtemp_MouseClick2, txstateUVstar)
+                        if (calc_constants.NLSW_or_Bous == 1) { // only update for Celeris Boussinesq equations
                             console.log('Updating neardry & tridiag coef due to change in depth')
-                            runComputeShader(device, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
+                            runComputeShader(device, commandEncoder, Updateneardry_uniformBuffer, Updateneardry_uniforms, Updateneardry_Pipeline, Updateneardry_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
+                            runCopyTextures(device, commandEncoder, calc_constants, txtemp_bottom, txBottom)
+                            runComputeShader(device, commandEncoder, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
                         }
                     } else if(calc_constants.surfaceToChange == 2){  //when changing friction
-                        runCopyTextures(device, calc_constants, txtemp_MouseClick, txBottomFriction)
+                        runCopyTextures(device, commandEncoder, calc_constants, txtemp_MouseClick, txBottomFriction)
 
                     } else if(calc_constants.surfaceToChange == 3){  //when changing passive tracer
-                        runCopyTextures(device, calc_constants, txtemp_MouseClick, txContSource)
+                        runCopyTextures(device, commandEncoder, calc_constants, txtemp_MouseClick, txContSource)
 
                     } else if(calc_constants.surfaceToChange == 4){  //water surface elevation
-                        runCopyTextures(device, calc_constants, txtemp_MouseClick, txstateUVstar)
+                        runCopyTextures(device, commandEncoder, calc_constants, txtemp_MouseClick, txstateUVstar)
                     }
                 } else if(calc_constants.whichPanelisOpen == 2){
                     console.log('Updating Design Components')
-                    // runCopyTextures(device, calc_constants, txtemp_MouseClick, txDesignComponents)
-                    // runCopyTextures(device, calc_constants, txtemp_MouseClick2, txBottomFriction)
-                    // CODEX: Linear structures use the design panel UI but modify bathy/topo through the MouseClickChange infrastructure.
-                    if(calc_constants.designcomponent_AddLinearStructure == 1){
-                        console.log('Adding Linear Structure to Bathy/Topo')
-                        runCopyTextures(device, calc_constants, txtemp_MouseClick, txBottom)
-                        runCopyTextures(device, calc_constants, txtemp_MouseClick2, txstateUVstar)
-                        runComputeShader(device, Updateneardry_uniformBuffer, Updateneardry_uniforms, Updateneardry_Pipeline, Updateneardry_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
-                        runCopyTextures(device, calc_constants, txtemp_bottom, txBottom)
-                        if (calc_constants.NLSW_or_Bous >= 1) { // only update for Celeris Boussinesq equations
-                            console.log('Updating neardry & tridiag coef due to linear structure')
-                            runComputeShader(device, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
-                        }
-                        resetLinearStructureEndpointsAfterApply();
-                    } else {
-                        runCopyTextures(device, calc_constants, txtemp_MouseClick, txDesignComponents)
-                        runCopyTextures(device, calc_constants, txtemp_MouseClick2, txBottomFriction)
-                    }
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_MouseClick, txDesignComponents)
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_MouseClick2, txBottomFriction)
                 }
             }
             else if (calc_constants.click_update == 2 && calc_constants.viewType == 2)
```

#### CT1-300 교란 호출과 중첩 트리거

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2595; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1548; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 즉시 submit 함수를 호출한다. 본판만 중첩 출력 트리거를 처리한다. 단면판은 commandEncoderStack 변수를 두지 않는다. |

본판 차이 줄의 마지막 수정: `33f7ff6` 2026-02-13 (현재 2598행 포함); `bb99fee` 2026-07-02 (현재 2604행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1551행 포함).

```diff
@@ -2595,22 +1548,15 @@
             AddDisturbance_view.setFloat32(44, calc_constants.disturbanceDip, true);             // f32  
             AddDisturbance_view.setFloat32(48, calc_constants.disturbanceRake, true);             // f32  
 
-            runComputeShader(device, AddDisturbance_uniformBuffer, AddDisturbance_uniforms, AddDisturbance_Pipeline, AddDisturbance_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // add impulse
-            runCopyTextures(device, calc_constants, txtemp_AddDisturbance, txstateUVstar)
+            runComputeShader(device, commandEncoder, AddDisturbance_uniformBuffer, AddDisturbance_uniforms, AddDisturbance_Pipeline, AddDisturbance_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // add impulse
+            runCopyTextures(device, commandEncoder, calc_constants, txtemp_AddDisturbance, txstateUVstar)
 
             calc_constants.add_Disturbance = -1;
         }
 
-        // Added by Codex: Start nested-grid boundary time-series output trigger.
-        if (calc_constants.nestedGridOutput_trigger == 1) {
-            initializeNestedGridBoundaryOutputCapture(total_time);
-        }
-        // Added by Codex: End nested-grid boundary time-series output trigger.
-
 
          // loop through the compute shaders "render_step" times.  
         var commandEncoder;  // init the encoder
-        var commandEncoderStack;  // init the encoder for stacking
         if (calc_constants.simPause < 0) {// do not run compute loop when > 0, when the simulation is paused {
             for (let frame_c = 0; frame_c < calc_constants.render_step; frame_c++) {  // loop through the compute shaders "render_step" time
```

#### CT1-301 예측 단계 submit 묶음

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2619; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1565; 아래 전체 diff의 +행 | 불일치 (A) | Pass0→Pass1→선택 퇴적물 재구성→Pass2→쇄파→COULWAVE A/B 순서는 같다. transect 판은 매 호출을 submit한다. 본판은 encoder로 묶는다. 시간 uniform을 쓰는 위치는 바뀌지만 쇄파는 total_time-dt를 사용한다. 본판만 total_time에 시작 시각을 더한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 2622행 포함); `3646fc8` 2026-02-08 (현재 2627행 포함); `33f7ff6` 2026-02-13 (현재 2635행 포함); `366ee34` 2024-04-08 (현재 2656행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1568행 포함).

```diff
@@ -2619,48 +1565,34 @@
                 frame_count_since_http_update += 1;
                 frame_count_time_series += 1;
 
-                // total_time = frame_count * calc_constants.dt;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n
-                // Added by Codex: Reference all physical model times to the first loaded boundary time-series time when nested forcing is active.
-                total_time = frame_count * calc_constants.dt + calc_constants.start_time_shift;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n
+                total_time = frame_count * calc_constants.dt;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n
                 total_time_since_http_update = frame_count_since_http_update * calc_constants.dt; // simulation time sinze last change to interface
 
-                // set time in uniform buffers for compute shaders here, so that command encoders can be stacked
-                PassBreaking_view.setFloat32(36, total_time - calc_constants.dt, true);   //f32 - update time, minus dt as we are here finding dissipation at the previous time level
-                BoundaryPass_view.setFloat32(20, total_time, true);           // set current time
-                // Added by Codex: Update the shared type-5 boundary time-series bracket once per simulation step.
-                updateBoundaryTimeSeriesUniforms(BoundaryPass_view, total_time);
-                AddDisturbance_view.setFloat32(64, total_time ,true);             // f32   - stores time
-
-                // create command encoder for compute shaders and texture copy operations
-                commandEncoderStack = device.createCommandEncoder();
-
                 // Pass0
-                runComputeShader_EncStack(device, commandEncoderStack, Pass0_uniformBuffer, Pass0_uniforms, Pass0_Pipeline, Pass0_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                runComputeShader(device, commandEncoder, Pass0_uniformBuffer, Pass0_uniforms, Pass0_Pipeline, Pass0_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
 
                 // Pass1
-                runComputeShader_EncStack(device, commandEncoderStack, Pass1_uniformBuffer, Pass1_uniforms, Pass1_Pipeline, Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                runComputeShader(device, commandEncoder, Pass1_uniformBuffer, Pass1_uniforms, Pass1_Pipeline, Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
 
                 // SedTrans_Pass1
                 if(calc_constants.useSedTransModel == 1){
-                    runComputeShader_EncStack(device, commandEncoderStack, SedTrans_Pass1_uniformBuffer, SedTrans_Pass1_uniforms, SedTrans_Pass1_Pipeline, SedTrans_Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runComputeShader(device, commandEncoder, SedTrans_Pass1_uniformBuffer, SedTrans_Pass1_uniforms, SedTrans_Pass1_Pipeline, SedTrans_Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                 }
 
                 // Pass2
-                runComputeShader_EncStack(device, commandEncoderStack, Pass2_uniformBuffer, Pass2_uniforms, Pass2_Pipeline, Pass2_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                runComputeShader(device, commandEncoder, Pass2_uniformBuffer, Pass2_uniforms, Pass2_Pipeline, Pass2_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
 
                 // Breaking and Dissipation Pass
                 if(calc_constants.useBreakingModel == 1) {
-                    runComputeShader_EncStack(device, commandEncoderStack, PassBreaking_uniformBuffer, PassBreaking_uniforms, PassBreaking_Pipeline, PassBreaking_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_Breaking, txBreaking)
+                    PassBreaking_view.setFloat32(36, total_time - calc_constants.dt, true);   //f32 - update time, minus dt as we are here finding dissipation at the previous time level
+                    runComputeShader(device, commandEncoder, PassBreaking_uniformBuffer, PassBreaking_uniforms, PassBreaking_Pipeline, PassBreaking_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_Breaking, txBreaking)
                 }
-                
-                // break here to submit the command encoder stack
-                device.queue.submit([commandEncoderStack.finish()]);
 
                 // Pass3
                 if (calc_constants.NLSW_or_Bous == 2) {  // grouping passes for COULWAVE model
-                    runComputeShader(device, Pass3A_Coulwave_uniformBuffer, Pass3A_Coulwave_uniforms, Pass3A_Coulwave_Pipeline, Pass3A_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-                    runComputeShader(device, Pass3B_Coulwave_uniformBuffer, Pass3B_Coulwave_uniforms, Pass3B_Coulwave_Pipeline, Pass3B_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runComputeShader(device, commandEncoder, Pass3A_Coulwave_uniformBuffer, Pass3A_Coulwave_uniforms, Pass3A_Coulwave_Pipeline, Pass3A_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runComputeShader(device, commandEncoder, Pass3B_Coulwave_uniformBuffer, Pass3B_Coulwave_uniforms, Pass3B_Coulwave_Pipeline, Pass3B_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                     copy2DDataTo3DTexture(device, txCW_uvhuhv, txCW_groupings, 0, calc_constants.WIDTH, calc_constants.HEIGHT);
                     copy2DDataTo3DTexture(device, txCW_zalpha, txCW_groupings, 1, calc_constants.WIDTH, calc_constants.HEIGHT);
                     copy2DDataTo3DTexture(device, txCW_STval, txCW_groupings, 2, calc_constants.WIDTH, calc_constants.HEIGHT);
```

#### CT1-302 예측 적분·경계·PCR·사면 이동 순서

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2671; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1603; 아래 전체 diff의 +행 | 불일치 (A) | Pass3→gradient 보관→퇴적물→경계→COULWAVE 계수→PCR→분산 모드 재경계 순서는 유지한다. 본판은 계수 교대 바인드 그룹을 전달한다. transect 판은 사면 이동을 시간 제한 없이 호출한다. 본판은 첫 1e5 스텝까지만 호출한다. corrector는 양쪽에서 timeScheme==2로 시작한다. |

본판 차이 줄의 마지막 수정: `3646fc8` 2026-02-08 (현재 2674행 포함); `984091f` 2026-05-24 (현재 2711행 포함); `7ae7da4` 2026-02-23 (현재 2739행 포함); `366ee34` 2024-04-08 (현재 2790행 포함); `33f7ff6` 2026-02-13 (현재 2796행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1607행 포함).

```diff
@@ -2671,130 +1603,104 @@
 
                 calc_constants.pred_or_corrector = 1;  //set to predictor step
                 Pass3_view.setUint32(56, calc_constants.pred_or_corrector, true);       // f32
-
-                //re-init command encoder for Pass3
-                commandEncoderStack = device.createCommandEncoder();
-
                 if (calc_constants.NLSW_or_Bous > 0) { //BOUS
-                    runComputeShader_EncStack(device, commandEncoderStack, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runComputeShader(device, commandEncoder, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                 }
                 else { //NLSW
-                    runComputeShader_EncStack(device, commandEncoderStack, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_NLSW, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runComputeShader(device, commandEncoder, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_NLSW, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                 }
                 // put DuDt from predictor into predicted gradients
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, dU_by_dt, predictedGradients)
+                runCopyTextures(device, commandEncoder, calc_constants, dU_by_dt, predictedGradients)
 
                 // SedTrans Pass3
                 if(calc_constants.useSedTransModel == 1){
-                    runComputeShader_EncStack(device, commandEncoderStack, SedTrans_Pass3_uniformBuffer, SedTrans_Pass3_uniforms, SedTrans_Pass3_Pipeline, SedTrans_Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, dU_by_dt_Sed, predictedGradients_Sed)
+                    runComputeShader(device, commandEncoder, SedTrans_Pass3_uniformBuffer, SedTrans_Pass3_uniforms, SedTrans_Pass3_Pipeline, SedTrans_Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runCopyTextures(device, commandEncoder, calc_constants, dU_by_dt_Sed, predictedGradients_Sed)
                 }
 
                 // BoundaryPass
-                runComputeShader_EncStack(device, commandEncoderStack, BoundaryPass_uniformBuffer, BoundaryPass_uniforms, BoundaryPass_Pipeline, BoundaryPass_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                BoundaryPass_view.setFloat32(20, total_time, true);           // set current time
+                runComputeShader(device, commandEncoder, BoundaryPass_uniformBuffer, BoundaryPass_uniforms, BoundaryPass_Pipeline, BoundaryPass_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                 // updated texture is stored in txtemp_boundary, but back into current_stateUVstar.  Same with breaking values (mainly for periodic conditions)
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_boundary, current_stateUVstar)
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_Breaking, txBreaking)
+                runCopyTextures(device, commandEncoder, calc_constants, txtemp_boundary, current_stateUVstar)
+                runCopyTextures(device, commandEncoder, calc_constants, txtemp_Breaking, txBreaking)
                 if(calc_constants.useSedTransModel == 1){
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_boundary_Sed, txNewState_Sed)
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_boundary_Sed, txNewState_Sed)
                 }   
 
                 if (calc_constants.NLSW_or_Bous == 2) {
                     // COULWAVE Model - need to update nonlinear tridaig coefficents before running tridiag solver
-                    runComputeShader_EncStack(device, commandEncoderStack, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
+                    runComputeShader(device, commandEncoder, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
                 }
 
-                // submit encoder stack for boundary pass and updates before tridiag
-                device.queue.submit([commandEncoderStack.finish()]);
-
                 //Tridiag Solver for Bous, or copy for NLSW
-                // runTridiagSolver(device, commandEncoder, calc_constants, current_stateUVstar, txNewState, coefMatx, coefMaty, newcoef_x, newcoef_y, txtemp_PCRx, txtemp_PCRy, txtemp2_PCRx, txtemp2_PCRy,
-                //     TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, TridiagX_view,
-                //     TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup, TridiagY_view,
-                //     runComputeShader, runCopyTextures
-                // )
-                // CODEX: Pass PCR ping-pong bind groups so the solver can hand off coefficient textures without copy-back.
                 runTridiagSolver(device, commandEncoder, calc_constants, current_stateUVstar, txNewState, coefMatx, coefMaty, newcoef_x, newcoef_y, txtemp_PCRx, txtemp_PCRy, txtemp2_PCRx, txtemp2_PCRy,
-                    TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, TridiagX_BindGroup_BaseToA, TridiagX_BindGroup_BToA, TridiagX_view,
-                    TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup, TridiagY_BindGroup_BaseToA, TridiagY_BindGroup_BToA, TridiagY_view,
+                    TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, TridiagX_view,
+                    TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup, TridiagY_view,
                     runComputeShader, runCopyTextures
                 )
 
                 // after tridiag, we re-eval bc's on eta. P, Q  [this is not needed for NLSW, since U*=P and V*=Q, and these bc's have already been enforced]
-
-                // re-init command encoder for boundary pass after tridiag
-                commandEncoderStack = device.createCommandEncoder();
-
                 if (calc_constants.NLSW_or_Bous > 0) { //BOUS
-                    runComputeShader_EncStack(device, commandEncoderStack, BoundaryPass_uniformBuffer, BoundaryPass_uniforms, BoundaryPass_Pipeline, BoundaryPass_BindGroup_NewState, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runComputeShader(device, commandEncoder, BoundaryPass_uniformBuffer, BoundaryPass_uniforms, BoundaryPass_Pipeline, BoundaryPass_BindGroup_NewState, calc_constants.DispatchX, calc_constants.DispatchY);
                 }
                 // updated texture is stored in txtemp, but back into txNewState - this needs to be done for both NLSW and Bous.  Even though these are the same in NLSW, some passes use State, and these must be updated with bc's
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_boundary, txNewState)
+                runCopyTextures(device, commandEncoder, calc_constants, txtemp_boundary, txNewState)
 
                 // Shift back FG textures - only have to do this for Bous, and only after predictor step
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, F_G_star_oldGradients, F_G_star_oldOldGradients)
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, predictedF_G_star, F_G_star_oldGradients)
+                runCopyTextures(device, commandEncoder, calc_constants, F_G_star_oldGradients, F_G_star_oldOldGradients)
+                runCopyTextures(device, commandEncoder, calc_constants, predictedF_G_star, F_G_star_oldGradients)
+
 
                 // add prescriptive depth change
-                if(calc_constants.disturbanceType == 5 && total_time <= 1.0e5 * calc_constants.dt) { // only add disturbance for first 100,000 time steps, to save some work
+                if(calc_constants.disturbanceType == 5) {
+                    AddDisturbance_view.setFloat32(64, total_time ,true);             // f32   - stores time
 
-                    runComputeShader_EncStack(device, commandEncoderStack, AddDisturbance_uniformBuffer, AddDisturbance_uniforms, AddDisturbance_Pipeline, AddDisturbance_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // add impulse
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_bottom, txBottom) 
-                    runComputeShader_EncStack(device, commandEncoderStack, Updateneardry_uniformBuffer, Updateneardry_uniforms, Updateneardry_Pipeline, Updateneardry_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update neardry
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_bottom, txBottom)
-                    runComputeShader_EncStack(device, commandEncoderStack, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
+                    runComputeShader(device, commandEncoder, AddDisturbance_uniformBuffer, AddDisturbance_uniforms, AddDisturbance_Pipeline, AddDisturbance_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // add impulse
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_bottom, txBottom) 
+                    runComputeShader(device, commandEncoder, Updateneardry_uniformBuffer, Updateneardry_uniforms, Updateneardry_Pipeline, Updateneardry_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update neardry
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_bottom, txBottom)
+                    runComputeShader(device, commandEncoder, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
                         
                     // copy the initial bathy into a seperate texture
                     if (frame_count == 0) {
-                        runCopyTextures_EncStack(commandEncoderStack, calc_constants, txBottom, txBottomInitial)
+                        runCopyTextures(device, commandEncoder, calc_constants, txBottom, txBottomInitial)
                     }
-
                 }
 
-                // submit encoder stack 
-                device.queue.submit([commandEncoderStack.finish()]);
-
                 if (calc_constants.timeScheme == 2)  // only called when using Predictor+Corrector method.  Adding corrector allows for a time step twice as large (also adds twice the computation) and provides a more accurate solution
                 {
-                    // set buffers here so that command encoder stack can be maximized for corrector step
-                    PassBreaking_view.setFloat32(36, total_time, true);
-                    
-                    // re-init command encoder for corrector step
-                    commandEncoderStack = device.createCommandEncoder();
-                    
                     // put txNewState into txState for the corrector equation, so gradients use the predicted values
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txNewState, txState)
+                    runCopyTextures(device, commandEncoder, calc_constants, txNewState, txState)
                     if(calc_constants.useSedTransModel == 1){
-                        runCopyTextures_EncStack(commandEncoderStack, calc_constants, txNewState_Sed, txState_Sed)
+                        runCopyTextures(device, commandEncoder, calc_constants, txNewState_Sed, txState_Sed)
                     }                       
 
                     // Pass0
-                    runComputeShader_EncStack(device, commandEncoderStack, Pass0_uniformBuffer, Pass0_uniforms, Pass0_Pipeline, Pass0_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runComputeShader(device, commandEncoder, Pass0_uniformBuffer, Pass0_uniforms, Pass0_Pipeline, Pass0_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
 
                     // Pass1
-                    runComputeShader_EncStack(device, commandEncoderStack, Pass1_uniformBuffer, Pass1_uniforms, Pass1_Pipeline, Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runComputeShader(device, commandEncoder, Pass1_uniformBuffer, Pass1_uniforms, Pass1_Pipeline, Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
 
                     // SedTrans_Pass1
                     if(calc_constants.useSedTransModel == 1){
-                        runComputeShader_EncStack(device, commandEncoderStack, SedTrans_Pass1_uniformBuffer, SedTrans_Pass1_uniforms, SedTrans_Pass1_Pipeline, SedTrans_Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                        runComputeShader(device, commandEncoder, SedTrans_Pass1_uniformBuffer, SedTrans_Pass1_uniforms, SedTrans_Pass1_Pipeline, SedTrans_Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                     }
 
                     // Pass2
-                    runComputeShader_EncStack(device, commandEncoderStack, Pass2_uniformBuffer, Pass2_uniforms, Pass2_Pipeline, Pass2_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runComputeShader(device, commandEncoder, Pass2_uniformBuffer, Pass2_uniforms, Pass2_Pipeline, Pass2_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
 
                     // Breaking and Dissipation Pass
                     if(calc_constants.useBreakingModel == 1) {
-                        runComputeShader_EncStack(device, commandEncoderStack, PassBreaking_uniformBuffer, PassBreaking_uniforms, PassBreaking_Pipeline, PassBreaking_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-                        runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_Breaking, txBreaking)
+                        PassBreaking_view.setFloat32(36, total_time, true);   //f32 - update time
+                        runComputeShader(device, commandEncoder, PassBreaking_uniformBuffer, PassBreaking_uniforms, PassBreaking_Pipeline, PassBreaking_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                        runCopyTextures(device, commandEncoder, calc_constants, txtemp_Breaking, txBreaking)
                     }
-                    
-                    // submit encoder stack for corrector step before breaking and Pass3
-                    device.queue.submit([commandEncoderStack.finish()]);
 
                     // Pass3
                     if (calc_constants.NLSW_or_Bous == 2) {  // grouping passes for COULWAVE model
-                        runComputeShader(device, Pass3A_Coulwave_uniformBuffer, Pass3A_Coulwave_uniforms, Pass3A_Coulwave_Pipeline, Pass3A_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-                        runComputeShader(device, Pass3B_Coulwave_uniformBuffer, Pass3B_Coulwave_uniforms, Pass3B_Coulwave_Pipeline, Pass3B_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                        runComputeShader(device, commandEncoder, Pass3A_Coulwave_uniformBuffer, Pass3A_Coulwave_uniforms, Pass3A_Coulwave_Pipeline, Pass3A_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                        runComputeShader(device, commandEncoder, Pass3B_Coulwave_uniformBuffer, Pass3B_Coulwave_uniforms, Pass3B_Coulwave_Pipeline, Pass3B_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                         copy2DDataTo3DTexture(device, txCW_uvhuhv, txCW_groupings, 0, calc_constants.WIDTH, calc_constants.HEIGHT);
                         copy2DDataTo3DTexture(device, txCW_zalpha, txCW_groupings, 1, calc_constants.WIDTH, calc_constants.HEIGHT);
                         copy2DDataTo3DTexture(device, txCW_STval, txCW_groupings, 2, calc_constants.WIDTH, calc_constants.HEIGHT);
```

#### CT1-303 수정 단계와 후처리의 단면판 경로

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2805; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1711; 아래 전체 diff의 +행 | 코드에만 (C) | 수정 단계의 계산·경계·PCR 순서는 같다. 통계 카운터 uniform은 transect가 직전에 갱신하고 본판은 encoder 생성 전에 갱신한다. transect의 퇴적물 바닥고 고정은 HTML 안내에 맞는다. 본판만 중첩 경계 캡처·다운로드·리소스 해제를 실행한다. 이력 texture 이동과 통계의 상대 순서는 같다. |

본판 차이 줄의 마지막 수정: `3646fc8` 2026-02-08 (현재 2808행 포함); `984091f` 2026-05-24 (현재 2841행 포함); `bb99fee` 2026-07-02 (현재 2890행 포함); `c4be488` 2026-07-13 (현재 2891행 포함); `85c2ca2` 2024-03-19 (현재 2902행 포함); `63a12e3` 2023-10-19 (현재 2930행 포함); `cf9de63` 2023-10-24 (현재 2931행 포함); `33f7ff6` 2026-02-13 (현재 2980행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1715행 포함).

```diff
@@ -2805,179 +1711,95 @@
 
                     calc_constants.pred_or_corrector = 2;
                     Pass3_view.setUint32(56, calc_constants.pred_or_corrector, true);       // f32
-
-                    // re-init command encoder for Pass3 corrector step
-                    commandEncoderStack = device.createCommandEncoder();
                     if (calc_constants.NLSW_or_Bous > 0) { //BOUS
-                        runComputeShader_EncStack(device, commandEncoderStack, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                        runComputeShader(device, commandEncoder, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                     }
                     else { //NLSW
-                        runComputeShader_EncStack(device, commandEncoderStack, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_NLSW, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                        runComputeShader(device, commandEncoder, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_NLSW, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                     }
 
                     // SedTrans Pass3
                     if(calc_constants.useSedTransModel == 1){
-                        runComputeShader_EncStack(device, commandEncoderStack, SedTrans_Pass3_uniformBuffer, SedTrans_Pass3_uniforms, SedTrans_Pass3_Pipeline, SedTrans_Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                        runComputeShader(device, commandEncoder, SedTrans_Pass3_uniformBuffer, SedTrans_Pass3_uniforms, SedTrans_Pass3_Pipeline, SedTrans_Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                     }
 
                     // BoundaryPass
-                    runComputeShader_EncStack(device, commandEncoderStack, BoundaryPass_uniformBuffer, BoundaryPass_uniforms, BoundaryPass_Pipeline, BoundaryPass_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runComputeShader(device, commandEncoder, BoundaryPass_uniformBuffer, BoundaryPass_uniforms, BoundaryPass_Pipeline, BoundaryPass_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
                     // updated texture is stored in txtemp, but back into current_stateUVstar
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_boundary, current_stateUVstar)
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_Breaking, txBreaking)
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_boundary, current_stateUVstar)
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_Breaking, txBreaking)
                     if(calc_constants.useSedTransModel == 1){
-                        runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_boundary_Sed, txNewState_Sed)
+                        runCopyTextures(device, commandEncoder, calc_constants, txtemp_boundary_Sed, txNewState_Sed)
                     }                    
 
                     if (calc_constants.NLSW_or_Bous == 2) {
                         // COULWAVE Model - need to update nonlinear tridaig coefficents before running tridiag solver
-                        runComputeShader_EncStack(device, commandEncoderStack, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
+                        runComputeShader(device, commandEncoder, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
                     }
 
-                    // submit encoder stack for corrector step before tridiag
-                    device.queue.submit([commandEncoderStack.finish()]);
-
                     //Tridiag Solver for Bous, or copy for NLSW
-                    // runTridiagSolver(device, commandEncoder, calc_constants, current_stateUVstar, txNewState, coefMatx, coefMaty, newcoef_x, newcoef_y, txtemp_PCRx, txtemp_PCRy, txtemp2_PCRx, txtemp2_PCRy,
-                    //         TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, TridiagX_view,
-                    //         TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup, TridiagY_view,
-                    //         runComputeShader, runCopyTextures
-                    // )
-                    // CODEX: Pass PCR ping-pong bind groups so the solver can hand off coefficient textures without copy-back.
                     runTridiagSolver(device, commandEncoder, calc_constants, current_stateUVstar, txNewState, coefMatx, coefMaty, newcoef_x, newcoef_y, txtemp_PCRx, txtemp_PCRy, txtemp2_PCRx, txtemp2_PCRy,
-                            TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, TridiagX_BindGroup_BaseToA, TridiagX_BindGroup_BToA, TridiagX_view,
-                            TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup, TridiagY_BindGroup_BaseToA, TridiagY_BindGroup_BToA, TridiagY_view,
+                            TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, TridiagX_view,
+                            TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup, TridiagY_view,
                             runComputeShader, runCopyTextures
                     )
 
-                    // re-init command encoder for boundary pass after tridiag in corrector step
-                    commandEncoderStack = device.createCommandEncoder();
-
                     // after tridiag, we re-eval bc's on eta. P, Q  [this is not needed for NLSW, since U*=P and V*=Q, and these bc's have already been enforced]
                     if (calc_constants.NLSW_or_Bous > 0) { //BOUS
-                        runComputeShader_EncStack(device, commandEncoderStack, BoundaryPass_uniformBuffer, BoundaryPass_uniforms, BoundaryPass_Pipeline, BoundaryPass_BindGroup_NewState, calc_constants.DispatchX, calc_constants.DispatchY);
+                        runComputeShader(device, commandEncoder, BoundaryPass_uniformBuffer, BoundaryPass_uniforms, BoundaryPass_Pipeline, BoundaryPass_BindGroup_NewState, calc_constants.DispatchX, calc_constants.DispatchY);
                     }
                     // updated texture is stored in txtemp, but back into txNewState - this needs to be done for both NLSW and Bous.  Even though these are the same in NLSW, some passes use State, and these must be updated with bc's
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_boundary, txNewState)
-
-                    // submit encoder stack for boundary pass after tridiag in corrector step
-                    device.queue.submit([commandEncoderStack.finish()]);
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_boundary, txNewState)
                 }
 
-                // setup variables and re-set buffers as needed here, above the encoder stack
-                calc_constants.n_time_steps_means += 1;
-                CalcMeans_view.setInt32(0, calc_constants.n_time_steps_means, true);          // i32
-
-                calc_constants.n_time_steps_waveheight += 1;
-                CalcWaveHeight_view.setInt32(0, calc_constants.n_time_steps_waveheight, true);          // i32
-
-                // re-init command encoder for copy operations after corrector step
-                commandEncoderStack = device.createCommandEncoder();
-
                 // Update Bottom from Sed Transport
                 if(calc_constants.useSedTransModel == 1){
-                    runComputeShader_EncStack(device, commandEncoderStack, SedTrans_UpdateBottom_uniformBuffer, SedTrans_UpdateBottom_uniforms, SedTrans_UpdateBottom_Pipeline, SedTrans_UpdateBottom_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_SedTrans_Botttom, txBottom)
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_SedTrans_Change, txBotChange_Sed)
-                    runComputeShader_EncStack(device, commandEncoderStack, Updateneardry_uniformBuffer, Updateneardry_uniforms, Updateneardry_Pipeline, Updateneardry_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_bottom, txBottom)
+                    runComputeShader(device, commandEncoder, SedTrans_UpdateBottom_uniformBuffer, SedTrans_UpdateBottom_uniforms, SedTrans_UpdateBottom_Pipeline, SedTrans_UpdateBottom_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_SedTrans_Botttom, txBottom)
+                    runCopyTextures(device, commandEncoder, calc_constants, txtemp_SedTrans_Change, txBotChange_Sed)
                     if (calc_constants.NLSW_or_Bous == 1) { // only need to update neardry and tridiagonal coefficients for Celeris Boussinesq equations
                      //   console.log('Updating neardry & tridiag coef sediment transport depth change')
-                        runComputeShader_EncStack(device, commandEncoderStack, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
+                        runComputeShader(device, commandEncoder, Updateneardry_uniformBuffer, Updateneardry_uniforms, Updateneardry_Pipeline, Updateneardry_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
+                        runCopyTextures(device, commandEncoder, calc_constants, txtemp_bottom, txBottom)
+                        runComputeShader(device, commandEncoder, UpdateTrid_uniformBuffer, UpdateTrid_uniforms, UpdateTrid_Pipeline, UpdateTrid_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  //need to update tridiagonal coefficients due to change inn depth
                     }
                 }
 
-                // Added by Codex: Store rectangle-edge eta/hu/hv on the GPU only at requested nested-output times.
-                // captureNestedGridBoundaryOutputIfNeeded(commandEncoderStack, total_time);
-                // Added by Codex: Capture every active nested-grid output rectangle at its own requested output time.
-                captureNestedGridBoundaryOutputsIfNeeded(commandEncoderStack, total_time);
-
                 // shift gradient textures
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, oldGradients, oldOldGradients)
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, predictedGradients, oldGradients)
+                runCopyTextures(device, commandEncoder, calc_constants, oldGradients, oldOldGradients)
+                runCopyTextures(device, commandEncoder, calc_constants, predictedGradients, oldGradients)
 
                 // Copy future_ocean_texture back to ocean_texture
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, txNewState, txState)
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, current_stateUVstar, txstateUVstar)
-                
+                runCopyTextures(device, commandEncoder, calc_constants, txNewState, txState)
+                runCopyTextures(device, commandEncoder, calc_constants, current_stateUVstar, txstateUVstar)
+
                 // shift/Copy SedTrans
                 if(calc_constants.useSedTransModel == 1){
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, oldGradients_Sed, oldOldGradients_Sed)
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, predictedGradients_Sed, oldGradients_Sed)
-                    runCopyTextures_EncStack(commandEncoderStack, calc_constants, txNewState_Sed, txState_Sed)
+                    runCopyTextures(device, commandEncoder, calc_constants, oldGradients_Sed, oldOldGradients_Sed)
+                    runCopyTextures(device, commandEncoder, calc_constants, predictedGradients_Sed, oldGradients_Sed)
+                    runCopyTextures(device, commandEncoder, calc_constants, txNewState_Sed, txState_Sed)
                 }
 
                 //  Update Statistics - means and wave height
-                //calc_constants.n_time_steps_means += 1;  // moved above
+                calc_constants.n_time_steps_means += 1;
                 // update Pass1 cell side textures as these are used for the velocities outputs - can probably remove the Pass1 call in the predictor step, but do not want to break anything right now
-                runComputeShader_EncStack(device, commandEncoderStack, Pass1_uniformBuffer, Pass1_uniforms, Pass1_Pipeline, Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-                //CalcMeans_view.setInt32(0, calc_constants.n_time_steps_means, true);          // i32 moved above
-                runComputeShader_EncStack(device, commandEncoderStack, CalcMeans_uniformBuffer, CalcMeans_uniforms, CalcMeans_Pipeline, CalcMeans_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-                
-                // Stack command encoder for copy operations
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_Means, txMeans)
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_Means_Speed, txMeans_Speed)
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_Means_Momflux, txMeans_Momflux)
-
-                //calc_constants.n_time_steps_waveheight += 1;  // moved above
-                //CalcWaveHeight_view.setInt32(0, calc_constants.n_time_steps_waveheight, true);          // i32 moved above
-                runComputeShader_EncStack(device, commandEncoderStack, CalcWaveHeight_uniformBuffer, CalcWaveHeight_uniforms, CalcWaveHeight_Pipeline, CalcWaveHeight_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
-                runCopyTextures_EncStack(commandEncoderStack, calc_constants, txtemp_WaveHeight, txWaveHeight)
-                
-                // submit encoder stack for copy operations after corrector step
-                device.queue.submit([commandEncoderStack.finish()]);
+                runComputeShader(device, commandEncoder, Pass1_uniformBuffer, Pass1_uniforms, Pass1_Pipeline, Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                CalcMeans_view.setInt32(0, calc_constants.n_time_steps_means, true);          // i32
+                runComputeShader(device, commandEncoder, CalcMeans_uniformBuffer, CalcMeans_uniforms, CalcMeans_Pipeline, CalcMeans_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                runCopyTextures(device, commandEncoder, calc_constants, txtemp_Means, txMeans)
+                runCopyTextures(device, commandEncoder, calc_constants, txtemp_Means_Speed, txMeans_Speed)
+                runCopyTextures(device, commandEncoder, calc_constants, txtemp_Means_Momflux, txMeans_Momflux)
 
-            }
-        }
+                calc_constants.n_time_steps_waveheight += 1;
+                CalcWaveHeight_view.setInt32(0, calc_constants.n_time_steps_waveheight, true);          // i32
+                runComputeShader(device, commandEncoder, CalcWaveHeight_uniformBuffer, CalcWaveHeight_uniforms, CalcWaveHeight_Pipeline, CalcWaveHeight_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+                runCopyTextures(device, commandEncoder, calc_constants, txtemp_WaveHeight, txWaveHeight)
 
-        // Added by Codex: Start deferred nested-grid boundary output readback and download.
-        // if (nestedGridOutputState.pendingDownload) {
-        //     nestedGridOutputState.pendingDownload = false;
-        //     try {
-        //         await writeNestedGridBoundaryTimeSeriesData(device, nestedGridOutputState);
-        //         console.log("Nested-grid boundary output files downloaded.");
-        //     } catch (error) {
-        //         console.error("Failed to write nested-grid boundary output files:", error);
-        //     } finally {
-        //         destroyNestedGridOutputTextures();
-        //         nestedGridOutputState.bindGroup = null;
-        //         nestedGridOutputState.capturedTimes = [];
-        //         // redrawDrawOverlayBase();
-        //         // Added by Codex: Clear the nested-grid rectangle only after capture/download completes.
-        //         await redrawDrawOverlayBase();
-        //     }
-        // }
-        // Added by Codex: Write and release completed rectangle outputs independently so other active rectangles can continue.
-        const pendingNestedOutputStates = nestedGridOutputStates.filter((state) => state.pendingDownload);
-        // Added by Codex: Avoid CPU readback/download stalls while any rectangle is still actively sampling.
-        const hasActiveNestedOutputStates = nestedGridOutputStates.some((state) => state.active);
-        if (pendingNestedOutputStates.length > 0 && !hasActiveNestedOutputStates) {
-            for (const state of pendingNestedOutputStates) {
-                state.pendingDownload = false;
-                try {
-                    await writeNestedGridBoundaryTimeSeriesData(device, state);
-                    console.log(`Nested-grid boundary output files downloaded for ${state.filePrefix}.`);
-                } catch (error) {
-                    console.error(`Failed to write nested-grid boundary output files for ${state.filePrefix}:`, error);
-                } finally {
-                    destroyNestedGridOutputStateTextures(state);
-                    state.bindGroup = null;
-                    state.capturedTimes = [];
-                }
-            }
-            nestedGridOutputStates = nestedGridOutputStates.filter((state) => state.active || state.pendingDownload);
-            calc_constants.nestedGridOutput_rectangle_count = nestedGridOutputStates.length;
-            calc_constants.nestedGridOutput_active = nestedGridOutputStates.some((state) => state.active) ? 1 : 0;
-            if (nestedGridOutputStates.length > 0) {
-                await redrawDrawOverlayWithNestedGridOutline();
-            } else {
-                await redrawDrawOverlayBase();
             }
         }
-        // Added by Codex: End deferred nested-grid boundary output readback and download.
 
         // copy eta and bottom data to the f16 texture for filtered rendering
-        runComputeShader(device, Copytxf32_txf16_uniformBuffer, Copytxf32_txf16_uniforms, Copytxf32_txf16_Pipeline, Copytxf32_txf16_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
+        runComputeShader(device, commandEncoder, Copytxf32_txf16_uniformBuffer, Copytxf32_txf16_uniforms, Copytxf32_txf16_Pipeline, Copytxf32_txf16_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
              
         // Define the settings for the render pass.
         Render_view.setFloat32(116, total_time, true);             // f32
```

#### CT1-304 프레임별 render 파이프라인 생성

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:2985; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1807; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 매 프레임 quad 또는 vertexgrid 파이프라인을 새로 만든다. 본판은 미리 만든 객체를 선택한다. view 1은 colorbar를 켜고 view 2는 끈다는 조건은 같다. 본판은 2026-02-13 08860f0에서 이 반복 생성을 줄였다. 같은 판의 초기 파이프라인 생성 경로와 프레임 내 재사용 원칙을 함께 근거로 중간 강도의 결함 후보로 둔다. |

본판 차이 줄의 마지막 수정: `08860f0` 2026-02-13 (현재 2990행 포함); `efe44a2` 2024-04-02 (현재 2994행 포함); `d778fe7` 2026-06-02 (현재 3002행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1810행 포함).

```diff
@@ -2985,22 +1807,20 @@
         {
             // turn back on colorbar
             calc_constants.CB_show = 1;
+            Render_view.setInt32(84, calc_constants.CB_show, true);          // i32  
             
             // Render QUAD
-            Render_view.setInt32(84, calc_constants.CB_show, true);          // i32
-            RenderPipeline = RenderPipeline_quad;
+            RenderPipeline = createRenderPipeline(device, vertexShaderCode, fragmentShaderCode, swapChainFormat, RenderBindGroupLayout, 'depth24plus');
         }
         else if (calc_constants.viewType == 2)
-        {
+        {  
             // turn off colorbar
             calc_constants.CB_show = 0;
+            Render_view.setInt32(84, calc_constants.CB_show, true);          // i32  
 
             // Render Vertex grid
-            Render_view.setInt32(84, calc_constants.CB_show, true);          // i32
-            RenderPipeline = RenderPipeline_vertexgrid;
+            RenderPipeline = createRenderPipeline_vertexgrid(device, vertex3DShaderCode, fragmentShaderCode, swapChainFormat, RenderBindGroupLayout, 'depth24plus');
         }
-        // CODEX: Upload linear-structure preview state just before the render uniform buffer is written.
-        updateRenderLinearStructurePreviewUniforms();
 
         // make sure depthTexture matches the current canvas / window size
         const colorTexture = context.getCurrentTexture();
```

#### CT1-305 Design 모드 건물 footprint

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3046; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1866; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 JSON box 모델을 위에서 본 footprint로 표시한다. 본판은 범례와 로고 영역을 scissor로 보호한다. transect 판은 quad만 그린다. |

본판 차이 줄의 마지막 수정: `471c581` 2024-01-04 (현재 3049행 포함); `590bda8` 2026-06-01 (현재 3050행 포함); `d289986` 2025-04-21 (현재 3139행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1869행 포함).

```diff
@@ -3046,97 +1866,10 @@
             // Render QUAD
             RenderPass.setVertexBuffer(0, quadVertexBuffer);
             // Issue draw command to draw
-            RenderPass.draw(4);  // Draw the quad
-
-            // CODEX: Draw loaded JSON box models as top-down footprints in Design mode.
-            const designModelViewProj = mat4.fromValues(
-                2.0 / simWidth, 0.0, 0.0, 0.0,
-                0.0, 2.0 / simHeight, 0.0, 0.0,
-                0.0, 0.0, 0.0, 0.0,
-                -1.0, -1.0, 0.0, 1.0
-            );
-            RenderPass.setPipeline(ModelPipeline);
-
-            // CODEX: Previous single-colorbar scissor path retained while adding logo protection.
-            // const designColorbarVisible = calc_constants.CB_show == 1 && !(calc_constants.surfaceToPlot == 0 && calc_constants.colorMap_choice == 0);
-            // if (designColorbarVisible) {
-            //     const designColorbarProtectedHeight = Math.min(
-            //         canvas.height - 1,
-            //         Math.ceil(((calc_constants.CB_ystart + 20) / calc_constants.HEIGHT * grid_ratio + 0.5 * calc_constants.CB_xbuffer_uv) * canvas.height)
-            //     );
-            //     RenderPass.setScissorRect(0, 0, canvas.width, canvas.height - designColorbarProtectedHeight);
-            // }
-            // for (const obj of model_properties) {
-            //     const mv = obj.uniformView;
-            //     for (let i = 0; i < 16; ++i) {
-            //         mv.setFloat32(4 * i,         designModelViewProj[i], true);
-            //         mv.setFloat32(4 * (16 + i),  obj.modelMatrix[i],     true);
-            //     }
-            //     mv.setFloat32(128, 0.5 * simWidth, true);
-            //     mv.setFloat32(132, 0.5 * simHeight, true);
-            //     mv.setFloat32(136, simDim, true);
-            //     device.queue.writeBuffer(obj.uniformBuffer, 0, obj.uniforms);
-            //     RenderPass.setBindGroup(0, obj.bindGroup);
-            //     RenderPass.setVertexBuffer(0, boxVB);
-            //     RenderPass.setIndexBuffer(boxIB, 'uint32');
-            //     RenderPass.drawIndexed(boxIndices.length);
-            // }
-            // if (designColorbarVisible) {
-            //     RenderPass.setScissorRect(0, 0, canvas.width, canvas.height);
-            // }
-
-            // CODEX: Draw Design-mode model footprints only inside regions not reserved for overlays.
-            const drawDesignModelFootprints = () => {
-                for (const obj of model_properties) {
-                    const mv = obj.uniformView;
-                    for (let i = 0; i < 16; ++i) {
-                        mv.setFloat32(4 * i,         designModelViewProj[i], true);
-                        mv.setFloat32(4 * (16 + i),  obj.modelMatrix[i],     true);
-                    }
-                    mv.setFloat32(128, 0.5 * simWidth, true);
-                    mv.setFloat32(132, 0.5 * simHeight, true);
-                    mv.setFloat32(136, simDim, true);
-                    device.queue.writeBuffer(obj.uniformBuffer, 0, obj.uniforms);
-                    RenderPass.setBindGroup(0, obj.bindGroup);
-                    RenderPass.setVertexBuffer(0, boxVB);
-                    RenderPass.setIndexBuffer(boxIB, 'uint32');
-                    RenderPass.drawIndexed(boxIndices.length);
-                }
-            };
-
-            // CODEX: Protect the bottom colorbar except in the Ocean/photo-realistic free-surface view.
-            const designColorbarVisible = calc_constants.CB_show == 1 && !(calc_constants.surfaceToPlot == 0 && calc_constants.colorMap_choice == 0);
-            const designColorbarProtectedHeight = designColorbarVisible
-                ? Math.min(
-                    canvas.height - 1,
-                    Math.ceil(((calc_constants.CB_ystart + 20) / calc_constants.HEIGHT * grid_ratio + 0.5 * calc_constants.CB_xbuffer_uv) * canvas.height)
-                )
-                : 0;
-
-            // CODEX: In this UI, ShowLogos == 0 is the selected "Yes" value.
-            const designLogosVisible = calc_constants.ShowLogos == 0;
-            const designLogoProtectedHeight = designLogosVisible
-                ? Math.min(canvas.height - designColorbarProtectedHeight, Math.ceil(Math.max(logo_left.height, logo_right.height)))
-                : 0;
-            const drawDesignModelsInRect = (x, y, width, height) => {
-                if (width <= 0 || height <= 0) {
-                    return;
-                }
-                RenderPass.setScissorRect(x, y, width, height);
-                drawDesignModelFootprints();
-            };
-
-            if (designLogosVisible) {
-                drawDesignModelsInRect(Math.ceil(logo_left.width), 0, Math.floor(canvas.width - logo_left.width - logo_right.width), designLogoProtectedHeight);
-                drawDesignModelsInRect(0, designLogoProtectedHeight, canvas.width, canvas.height - designLogoProtectedHeight - designColorbarProtectedHeight);
-            } else {
-                drawDesignModelsInRect(0, 0, canvas.width, canvas.height - designColorbarProtectedHeight);
-            }
-            // CODEX: Restore full-canvas drawing after the Design-mode model footprint overlay.
-            RenderPass.setScissorRect(0, 0, canvas.width, canvas.height);
+            RenderPass.draw(4);  // Draw the quad 
         }
         else if (calc_constants.viewType == 2)  // 3D / drone / walk-through perspective !
-        {
+        {  
           // ──────────────────────────────────────────────────────────────────────────────
             // ──────────────────────────────────────────────────────────────────────────────
             // FULL "Perspective + Model" setup
```

#### CT1-306 카메라 투영 범위

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3144; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1877; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 가상 전체화면 크기와 구면 미터 척도를 반영한다. transect 판은 window 크기와 Cartesian dx·dy를 쓴다. fovY=45도는 같다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 3147행 포함); `afc1fe7` 2026-06-19 (현재 3157행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1880행 포함).

```diff
@@ -3144,24 +1877,15 @@
 
             // ─────────────────────────────────────────────────────────────
             // 1. Canvas dimensions
-            // const window_width  = calc_constants.full_screen ? window.innerWidth  : canvas.width;
-            // const window_height = calc_constants.full_screen ? window.innerHeight : canvas.height;
-            // CODEX: Pseudo-fullscreen uses explicit canvas dimensions from visualViewport instead of window size.
-            const window_width  = (calc_constants.full_screen && !pseudoFullscreenActive) ? window.innerWidth  : canvas.width;
-            const window_height = (calc_constants.full_screen && !pseudoFullscreenActive) ? window.innerHeight : canvas.height;
+            const window_width  = calc_constants.full_screen ? window.innerWidth  : canvas.width;
+            const window_height = calc_constants.full_screen ? window.innerHeight : canvas.height;
 
             // ─────────────────────────────────────────────────────────────
             // 2. Perspective projection
             const fovY   = 45 * Math.PI / 180;
             const aspect = window_width / window_height;
-            // const nearZ  = Math.min(0.1, Math.min(calc_constants.dx, calc_constants.dy) / 10);
-            // const farZ   = 10 * (simWidth + simHeight);
-            // Added by Codex: Use Explorer camera spacing for clipping so spherical degree grids do not clip meter-scale elevations.
-            const explorerMinCell = Math.max(Math.min(Math.abs(explorerCameraDx), Math.abs(explorerCameraDy)), 1.0e-6);
-            const explorerHorizontalExtent = Math.max(Math.abs(explorerSimWidth) + Math.abs(explorerSimHeight), 1.0);
-            const explorerVerticalExtent = Math.max(Math.abs(baseEye[2]), Math.abs(calc_constants.renderZScale * calc_constants.base_depth), Math.abs(calc_constants.base_depth), 1.0);
-            const nearZ  = Math.min(0.1, explorerMinCell / 10);
-            const farZ   = calc_constants.grid_type == 2 ? 10 * Math.max(explorerHorizontalExtent, explorerVerticalExtent) : 10 * (simWidth + simHeight);
+            const nearZ  = Math.min(0.1, Math.min(calc_constants.dx, calc_constants.dy) / 10);
+            const farZ   = 10 * (simWidth + simHeight);
             const P      = mat4.perspective(mat4.create(), fovY, aspect, nearZ, farZ);
 
             // ─────────────────────────────────────────────────────────────
```

#### CT1-307 카메라 바닥 보간 좌표

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3186; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1910; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 구면 미터 격자간격으로 카메라 위치를 인덱스화한다. transect 판은 dx·dy로 나눈다. Cartesian일 때 식은 같다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 3189행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1913행 포함).

```diff
@@ -3186,11 +1910,8 @@
             camState.forward = calc_constants.forward;
 
             // bathy interp - find ground elevation at current position
-            // const x = camState.position[0] / calc_constants.dx;
-            // const y = camState.position[1] / calc_constants.dy;
-            // Added by Codex: Convert Explorer camera x/y back to grid indices for spherical camera coordinates.
-            const x = camState.position[0] / explorerCameraDx;
-            const y = camState.position[1] / explorerCameraDy;
+            const x = camState.position[0] / calc_constants.dx;
+            const y = camState.position[1] / calc_constants.dy;
             // clamp to [0 ... N-1]
             const Nx = bathy2D.length;
             const Ny = bathy2D[0].length;
```

#### CT1-308 카메라 좌우 이동 척도

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3261; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1982; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 explorerSimDim을 사용한다. transect 판은 simDim을 사용한다. Cartesian일 때 두 척도는 같다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 3264행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 1985행 포함).

```diff
@@ -3261,9 +1982,7 @@
                 camState.position,
                 camState.position,
                 right,
-                // deltaPanX * simDim
-                // Added by Codex: Explorer movement should use the same coordinate scale as camera initialization.
-                deltaPanX * explorerSimDim
+                deltaPanX * simDim
                 );
             }
```

#### CT1-309 카메라 전후 이동 척도

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3278; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:1997; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 지면 잠금 여부와 무관하게 explorerSimDim을 사용한다. transect 판은 simDim을 사용한다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 3281행 포함); `d289986` 2025-04-21 (현재 3293행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2000행 포함).

```diff
@@ -3278,19 +1997,15 @@
                     camState.position,
                     camState.position,
                     horFwd,  // if locked to the ground, only forward in horizontal - jump if using forward here
-                    // deltaPanY * simDim
-                    // Added by Codex: Explorer movement should use the same coordinate scale as camera initialization.
-                    deltaPanY * explorerSimDim
+                    deltaPanY * simDim
                     );
                 } else {
                     vec3.scaleAndAdd(
                     camState.position,
                     camState.position,
                     forward,
-                    // deltaPanY * simDim
-                    // Added by Codex: Explorer movement should use the same coordinate scale as camera initialization.
-                    deltaPanY * explorerSimDim
-                    );
+                    deltaPanY * simDim
+                    );   
                 }
             }
```

#### CT1-310 카메라 model 행렬

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3316; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2031; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 구면에서 x·y 미터 변환을 적용한다. Cartesian 경로와 transect 판은 재척도*역척도인 항등 행렬이다. 제거된 카메라 로그는 본판에서도 주석이다. |

본판 차이 줄의 마지막 수정: `afc1fe7` 2026-06-19 (현재 3319행 포함); `ba4e12c` 2025-04-22 (현재 3345행 포함); `d289986` 2025-04-21 (현재 3350행 포함); `f183cc2` 2026-02-01 (현재 3365행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2036행 포함).

```diff
@@ -3316,58 +2031,27 @@
 
             // ─────────────────────────────────────────────────────────────
             // 4. Model matrix (identity - we're handling movement in camera space)
-            // const model = mat4.create();
-            //
-            // // grid transformations:
-            // const T_unskew = mat4.fromScaling(mat4.create(), [
-            //     1 / calc_constants.dx,
-            //     1 / calc_constants.dy,
-            //     1
-            // ]);
-            //
-            // const T_reskew = mat4.fromScaling(mat4.create(), [
-            //     calc_constants.dx,
-            //     calc_constants.dy,
-            //     1
-            // ]);
-            //
-            // mat4.multiply(model, T_reskew, T_unskew);
-            // Added by Codex: Start Explorer view-projection model transform for spherical camera coordinates.
             const model = mat4.create();
-            if (calc_constants.grid_type == 2) {
-                mat4.fromScaling(model, [
-                    explorerCameraScaleX,
-                    explorerCameraScaleY,
-                    1
-                ]);
-            } else {
-                // Added by Codex: Preserve the existing Cartesian identity transform.
-                const T_unskew = mat4.fromScaling(mat4.create(), [
-                    1 / calc_constants.dx,
-                    1 / calc_constants.dy,
-                    1
-                ]);
-
-                const T_reskew = mat4.fromScaling(mat4.create(), [
-                    calc_constants.dx,
-                    calc_constants.dy,
-                    1
-                ]);
 
-                mat4.multiply(model, T_reskew, T_unskew);
-            }
-            // Added by Codex: End Explorer view-projection model transform for spherical camera coordinates.
+            // grid transformations:
+            const T_unskew = mat4.fromScaling(mat4.create(), [
+                1 / calc_constants.dx,
+                1 / calc_constants.dy,
+                1
+            ]);
+
+            const T_reskew = mat4.fromScaling(mat4.create(), [
+                calc_constants.dx,
+                calc_constants.dy,
+                1
+            ]);
+
+            mat4.multiply(model, T_reskew, T_unskew);
 
             // ─────────────────────────────────────────────────────────────
             // 5. Final view-projection matrix
             const viewProj = mat4.mul(mat4.create(), P, mat4.mul(mat4.create(), V, model)); // view profection
 
-
-            // display current camera position, pitch, and yaw to the console
-            //console.log(`Camera position: x=${camState.position[0].toFixed(2)}, y=${camState.position[1].toFixed(2)}, z=${camState.position[2].toFixed(2)}`);
-            //console.log(`Camera pitch (xz)=${(camState.pitch * 180 / Math.PI).toFixed(2)}°, yaw (xy)=${(camState.yaw * 180 / Math.PI).toFixed(2)}°`);
-
-
             // skybox view matrix
             // Make a rotation‐only copy for the sky
             const skyView = mat4.clone(V);
```

#### CT1-311 점 시계열 초기화와 epoch

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3465; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2149; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 UI 갱신을 한 번만 처리하고 동기적으로 배열을 초기화한다. transect 판은 chartDataUpdate가 유지되는 동안 매 프레임 초기화를 요청한다. 본판은 epoch로 이전 readback을 버린다. 시간창 경계는 본판 >=이고 transect >다. 일반 실행은 양쪽 0 기반이고 본판 type5만 절대 시각이다. |

본판 차이 줄의 마지막 수정: `ebca435` 2026-07-20 (현재 3468행 포함); `bb99fee` 2026-07-02 (현재 3480행 포함); `33f7ff6` 2026-02-13 (현재 3515행 포함); `efe44a2` 2024-04-02 (현재 3521행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2152행 포함).

```diff
@@ -3465,60 +2149,29 @@
         // end screen render    
 
         // for the tooltip & time series, extract pixel values
-        // if(calc_constants.updateTimeSeriesTx == 1 || calc_constants.chartDataUpdate == 1) {  // update the time series locations texture, and reset plot
-        // Added by Codex: Start point time-series reset and clock handling.
-        // Handle a chart-update request once while its UI flag
-        // waits for the one-second chart refresh callback to clear it.
-        if (calc_constants.chartDataUpdate == 0) {
-            chartDataUpdateResetHandled = 0;
-        }
-        const pointTimeSeriesResetRequested = calc_constants.updateTimeSeriesTx == 1 ||
-            (calc_constants.chartDataUpdate == 1 && chartDataUpdateResetHandled == 0);
-        if(pointTimeSeriesResetRequested) {  // update the time series locations texture, and reset plot
+        if(calc_constants.updateTimeSeriesTx == 1 || calc_constants.chartDataUpdate == 1) {  // update the time series locations texture, and reset plot
             copyTSlocsToTexture(calc_constants, device, txTimeSeries_Locations) 
             frame_count_time_series = 0; 
-            // total_time_time_series = 0.0;
-            // Added by Codex: Reset ordinary gauges to zero and nested gauges
-            // to the current parent/global time.
-            total_time_time_series = useNestedPointTimeSeriesClock ? total_time : 0.0;
-            calc_constants.timeSeriesChartStartTime = total_time_time_series;
-            calc_constants.timeSeriesDataEpoch += 1;
-            resetTimeSeriesData();
+            total_time_time_series = 0.0;
             calc_constants.updateTimeSeriesTx = 0;
-            chartDataUpdateResetHandled = 1;
         }
 
-        // total_time_time_series = frame_count_time_series * calc_constants.dt; // step up time series time vector
-        // Added by Codex: Point-series output is locally elapsed for ordinary
-        // runs and follows total_time only for nested type-5 runs.
-        total_time_time_series = useNestedPointTimeSeriesClock
-            ? total_time
-            : frame_count_time_series * calc_constants.dt;
-        if(frame_count_time_series * calc_constants.dt >= calc_constants.maxdurationTimeSeries ){  // reset display if greater than max time
+        total_time_time_series = frame_count_time_series * calc_constants.dt; // step up time series time vector
+        if(total_time_time_series > calc_constants.maxdurationTimeSeries ){  // reset display if greater than max time
             if(calc_constants.NumberOfTimeSeries > 0) {
                 console.log('Reseting time series chart data, and saving time series to file')
                 downloadTimeSeriesData();
             }
             frame_count_time_series = 0; 
-            // total_time_time_series = 0.0;
-            // Added by Codex: Start the next ordinary chart at zero and the
-            // next nested chart at the current parent/global time.
-            total_time_time_series = useNestedPointTimeSeriesClock ? total_time : 0.0;
-            calc_constants.timeSeriesChartStartTime = total_time_time_series;
-            calc_constants.timeSeriesDataEpoch += 1;
-            resetTimeSeriesData();
+            total_time_time_series = 0.0;
         }
         
         ExtractTimeSeries_view.setInt32(16, calc_constants.mouse_current_canvas_indX, true);             // i32
         ExtractTimeSeries_view.setInt32(20, calc_constants.mouse_current_canvas_indY, true);             // i32
         ExtractTimeSeries_view.setFloat32(24,  total_time_time_series, true);             // f32, total_time
-        runComputeShader(device, ExtractTimeSeries_uniformBuffer, ExtractTimeSeries_uniforms, ExtractTimeSeries_Pipeline, ExtractTimeSeries_BindGroup, calc_constants.NumberOfTimeSeries + 1, 1);  //extract tooltip and time series data into a 1D texture        
-        // readToolTipTextureData(device, txTimeSeries_Data, frame_count_time_series);  //  read the tooltip / time series data and place into variables
-        // Added by Codex: Tag asynchronous readback with the active reset epoch.
-        readToolTipTextureData(device, txTimeSeries_Data, frame_count_time_series, calc_constants.timeSeriesDataEpoch);  //  read the tooltip / time series data and place into variables
-        // Added by Codex: End point time-series reset and clock handling.
+        runComputeShader(device, commandEncoder, ExtractTimeSeries_uniformBuffer, ExtractTimeSeries_uniforms, ExtractTimeSeries_Pipeline, ExtractTimeSeries_BindGroup, calc_constants.NumberOfTimeSeries + 1, 1);  //extract tooltip and time series data into a 1D texture        
+        readToolTipTextureData(device, txTimeSeries_Data, frame_count_time_series);  //  read the tooltip / time series data and place into variables
 
-        
         // store the current screen render as a texture, and then copy to a storage texture that will not be destroyed.  This is for creating jpgs, animations, only when not fullscreen
         if(calc_constants.full_screen == 0){
             const current_render = context.getCurrentTexture();
```

#### CT1-312 외부 제어 시간 진단

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3536; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2189; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 agent_total_time·agent_total_time_since_http_update·실시간 배율을 노출한다. 1000과 1000.0의 밀리초 환산은 JS에서 같다. |

본판 차이 줄의 마지막 수정: `a86f73a` 2026-02-20 (현재 3539행 포함); `0ee5174` 2026-06-18 (현재 3541행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2192행 포함).

```diff
@@ -3536,13 +2189,8 @@
 
         // determine elapsed time
         const now = new Date();
-        calc_constants.elapsedTime = (now - startTime) / 1000.0;
-        calc_constants.elapsedTime_update = (now - startTime_update) / 1000.0;
-        calc_constants.agent_total_time = total_time;
-        calc_constants.agent_total_time_since_http_update = total_time_since_http_update;
-        calc_constants.agent_faster_than_realtime_ratio = calc_constants.elapsedTime_update > 0
-            ? total_time_since_http_update / calc_constants.elapsedTime_update
-            : null;
+        calc_constants.elapsedTime = (now - startTime) / 1000;
+        calc_constants.elapsedTime_update = (now - startTime_update) / 1000;
 
         // Call the function to display the constants in the index.html page
         calc_constants.clearConc = 0; // reset back to default value - no easier place to set this back.
```

#### CT1-313 개별 표면 출력 버퍼

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3617; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2265; 아래 전체 diff의 +행 | 불일치 (A) | 13개 표면 선택의 텍스처·채널·파일명은 같다. 본판만 공용 readbackBuffer를 전달한다. |

본판 차이 줄의 마지막 수정: `09cfd76` 2026-02-15 (현재 3620행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2268행 포함).

```diff
@@ -3617,61 +2265,61 @@
         if(calc_constants.write_individual_surface == 1){
             if(calc_constants.which_surface_to_write == 0){  // free surface elevation
                 let filename = 'current_eta.bin';
-                downloadTextureData(device, txNewState, 1, filename, readbackBuffer);  // last number is the channel 1 = .r, 2 = .g, etc.
+                downloadTextureData(device, txNewState, 1, filename);  // last number is the channel 1 = .r, 2 = .g, etc.
              //   downloadGeoTiffData(device, txNewState, 1, calc_constants.dx, calc_constants.dy);  // current implemntation does not allow writing of float32, only uint8
              //  can update to write an RGB geotiff, but that doesnt seem too useful
 
             } else if(calc_constants.which_surface_to_write == 1){  // HU
                 let filename = 'current_HU.bin';
-                downloadTextureData(device, txNewState, 2, filename, readbackBuffer);  
+                downloadTextureData(device, txNewState, 2, filename);  
 
             } else if(calc_constants.which_surface_to_write == 2){  // HV
                 let filename = 'current_HV.bin';
-                downloadTextureData(device, txNewState, 3, filename, readbackBuffer);  
+                downloadTextureData(device, txNewState, 3, filename);  
 
             } else if(calc_constants.which_surface_to_write == 3){  // eddy viscosity
                 let filename = 'current_eddyvisc.bin';
-                downloadTextureData(device, txBreaking, 2, filename, readbackBuffer);  
+                downloadTextureData(device, txBreaking, 2, filename);  
 
             } else if(calc_constants.which_surface_to_write == 4){  // foam
                 let filename = 'current_tracer.bin';
-                downloadTextureData(device, txNewState, 4, filename, readbackBuffer);  
+                downloadTextureData(device, txNewState, 4, filename);  
 
             } else if(calc_constants.which_surface_to_write == 5){  // Bathymetry/Topography
                 let filename = 'current_bathytopo.bin';
-                downloadTextureData(device, txBottom, 3, filename, readbackBuffer);  
+                downloadTextureData(device, txBottom, 3, filename);  
 
             } else if(calc_constants.which_surface_to_write == 6){  // Bottom Friction Map 
                 let filename = 'current_friction.bin';
-                downloadTextureData(device, txBottomFriction, 1, filename, readbackBuffer);  
+                downloadTextureData(device, txBottomFriction, 1, filename);  
 
             } else if(calc_constants.which_surface_to_write == 7){  // Design Component Map
                 let filename = 'current_designcomponents.bin';
-                downloadTextureData(device, txDesignComponents, 1, filename, readbackBuffer);  
+                downloadTextureData(device, txDesignComponents, 1, filename);  
 
             } else if(calc_constants.which_surface_to_write == 8){  // RMS Wave Height
                 let filename = 'current_Hrms.bin';
-                downloadTextureData(device, txWaveHeight, 4, filename,readbackBuffer);  
+                downloadTextureData(device, txWaveHeight, 4, filename);  
 
             } else if(calc_constants.which_surface_to_write == 9){  // Significant Wave Height
                 let filename = 'current_Hs.bin';
-                downloadTextureData(device, txWaveHeight, 3, filename, readbackBuffer);  
+                downloadTextureData(device, txWaveHeight, 3, filename);  
 
             } else if(calc_constants.which_surface_to_write == 10){  // Max Free Surface Elev 
                 let filename = 'current_FSmax.bin';
-                downloadTextureData(device, txMeans_Speed, 4, filename, readbackBuffer); 
+                downloadTextureData(device, txMeans_Speed, 4, filename); 
 
             } else if(calc_constants.which_surface_to_write == 11){  // Mean Free Surface Elev 
                 let filename = 'current_FSmean.bin';
-                downloadTextureData(device, txMeans, 1, filename, readbackBuffer);  
+                downloadTextureData(device, txMeans, 1, filename);  
 
             } else if(calc_constants.which_surface_to_write == 12){  // Mean Fluid Flux [E-W]
                 let filename = 'current_Umean.bin';
-                downloadTextureData(device, txMeans, 2, filename, readbackBuffer);  
+                downloadTextureData(device, txMeans, 2, filename);  
 
             } else if(calc_constants.which_surface_to_write == 13){  // Mean Fluid Flux [N-S]
                 let filename = 'current_Vmean.bin';
-                downloadTextureData(device, txMeans, 3, filename, readbackBuffer);  
+                downloadTextureData(device, txMeans, 3, filename);  
             }   
 
             calc_constants.write_individual_surface = 0;  // reset
```

#### CT1-314 묶음 표면 출력

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3720; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2368; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 current_SedTransDepthChange.bin을 중심 b 채널에서 출력한다. 공용 버퍼 인자 차이 외에 나머지 파일은 같다. |

본판 차이 줄의 마지막 수정: `fa47b72` 2025-06-06 (현재 3723행 포함); `09cfd76` 2026-02-15 (현재 3727행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2374행 포함).

```diff
@@ -3720,11 +2368,10 @@
                 { tx: txMeans,        ch: 3, filename: 'current_Vmean.bin'},
                 { tx: txMeans,        ch: 4, filename: 'current_Foammean.bin'},
                 { tx: txMeans_Momflux,ch: 4, filename: 'current_Vorticitymean.bin'},
-                { tx: txBotChange_Sed,ch: 3, filename: 'current_SedTransDepthChange.bin'},
             ];
             
             for (const {tx, ch, filename} of files) {
-                await downloadTextureData(device, tx, ch, filename, readbackBuffer);
+                await downloadTextureData(device, tx, ch, filename);
                 // give the browser a breather before the next one
                 await sleep(calc_constants.fileWritePause);
             }
```

#### CT1-315 주기적 표면 출력 호출

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3791; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2438; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 공용 readbackBuffer를 전달한다. 시간·프레임 번호·6개 텍스처 인자는 같다. |

본판 차이 줄의 마지막 수정: `09cfd76` 2026-02-15 (현재 3794행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2441행 포함).

```diff
@@ -3791,7 +2438,7 @@
                 try {
                     frame_count_output = frame_count_output + 1;
                     console.log('Writing 2D surface data to file at time (s) ', total_time, ' with increment(s) ', dt_since_last_write);
-                    await writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities,readbackBuffer);
+                    await writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities);
                     dt_since_last_write = 0.0; // reset time counter
                 } catch (error) {
                     console.error("Failed to write surface data:", error);
```

#### CT1-316 포인터의 표시 영역 좌표

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3903; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2550; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 object-fit 여백을 제외한 canvas 내용 영역을 계산한다. transect 판은 외곽 사각형 전체를 쓴다. 여백이 있으면 표시한 격자와 편집 위치가 어긋난다. 외부 제어 모드 제한도 본판에만 있다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 3906행 포함); `0ee5174` 2026-06-18 (현재 3914행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2556행 포함).

```diff
@@ -3903,21 +2550,10 @@
     var lastMouseY_right = 0;
     var lastMouseX_left = 0;
     var lastMouseY_left = 0;
-    // CODEX: Touch-only Explorer gesture state for two-finger pan and pinch zoom.
-    const activeExplorerTouches = new Map();
-    var lastTouchMidX = 0;
-    var lastTouchMidY = 0;
-    var lastTouchDistance = 0;
 
     // Helper function to handle click or mouse move while button is pressed
     function handleMouseEvent(event) {
-        if (calc_constants.viewType == 1 && ["linear", "timeseries"].includes(agentDesignInteractionMode)) {
-            return;
-        }
-        const rect = getCanvasContentRect();
-        if (!rect || !isPointerInCanvasContent(event, rect)) {
-            return;
-        }
+        var rect = canvas.getBoundingClientRect();
         var scaleX = calc_constants.WIDTH / rect.width;
         var scaleY = calc_constants.HEIGHT / rect.height;
```

#### CT1-317 좌표 변환·선형 구조물·터치 helper

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:3928; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2564; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 object-fit 위치·표시 영역 검사·world 좌표·구면 상대/절대 좌표·선형 끝점 상태·양의 폭/경사 검사·두 손가락 중점과 거리를 구현한다. transect 판은 해당 함수가 없다. |

본판 차이 줄의 마지막 수정: `0ee5174` 2026-06-18 (현재 3931행 포함); `ff0d046` 2026-07-07 (현재 3990행 포함); `d778fe7` 2026-06-02 (현재 3991행 포함); `24b8f13` 2026-05-24 (현재 4204행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -3928,295 +2564,6 @@
     //    console.log("Canvas clicked/moved at X:", calc_constants.xClick, " Y:", calc_constants.yClick);
     }
 
-    function getCanvasContentRect() {
-        const bounds = canvas.getBoundingClientRect();
-        const boundsWidth = bounds.right - bounds.left;
-        const boundsHeight = bounds.bottom - bounds.top;
-        if (boundsWidth <= 0 || boundsHeight <= 0 || canvas.width <= 0 || canvas.height <= 0) {
-            return null;
-        }
-        const boundsRatio = boundsWidth / boundsHeight;
-        const canvasRatio = canvas.width / canvas.height;
-        if (boundsRatio > canvasRatio) {
-            const contentWidth = boundsHeight * canvasRatio;
-            const insetX = objectFitOffset(boundsWidth - contentWidth, getComputedStyle(canvas).objectPosition, "x");
-            return {
-                left: bounds.left + insetX,
-                right: bounds.left + insetX + contentWidth,
-                top: bounds.top,
-                bottom: bounds.bottom,
-                width: contentWidth,
-                height: boundsHeight
-            };
-        }
-        const contentHeight = boundsWidth / canvasRatio;
-        const insetY = objectFitOffset(boundsHeight - contentHeight, getComputedStyle(canvas).objectPosition, "y");
-        return {
-            left: bounds.left,
-            right: bounds.right,
-            top: bounds.top + insetY,
-            bottom: bounds.top + insetY + contentHeight,
-            width: boundsWidth,
-            height: contentHeight
-        };
-    }
-
-    function objectFitOffset(extraSpace, objectPosition, axis) {
-        if (extraSpace <= 0) {
-            return 0;
-        }
-        const tokens = String(objectPosition || "50% 50%").toLowerCase().trim().split(/\s+/);
-        const token = axis === "x" ? tokens[0] : (tokens[1] || tokens[0]);
-        if (token === "left" || token === "top") {
-            return 0;
-        }
-        if (token === "right" || token === "bottom") {
-            return extraSpace;
-        }
-        const percent = token.endsWith("%") ? Number.parseFloat(token) : NaN;
-        if (Number.isFinite(percent)) {
-            return extraSpace * percent / 100.0;
-        }
-        return 0.5 * extraSpace;
-    }
-
-    function isPointerInCanvasContent(event, rect) {
-        return event.clientX >= rect.left
-            && event.clientX <= rect.right
-            && event.clientY >= rect.top
-            && event.clientY <= rect.bottom;
-    }
-
-    // CODEX: Convert a pointer location on the canvas to lower-left-relative model coordinates used by design and time-series UI.
-    function getCanvasWorldCoordinates(event) {
-        const bounds = getCanvasContentRect();
-        if (!bounds || !isPointerInCanvasContent(event, bounds)) {
-            return null;
-        }
-        const normalizedX = Math.min(1.0, Math.max(0.0, (event.clientX - bounds.left) / bounds.width));
-        const normalizedY = Math.min(1.0, Math.max(0.0, 1.0 - (event.clientY - bounds.top) / bounds.height));
-        return {
-            x: normalizedX * calc_constants.WIDTH * calc_constants.dx,
-            y: normalizedY * calc_constants.HEIGHT * calc_constants.dy
-        };
-    }
-
-    // Added by Codex: Start time-series coordinate conversion helpers.
-    function isSphericalGrid() {
-        return Math.round(calc_constants.grid_type) == 2;
-    }
-
-    function timeSeriesOffsetToDisplayX(xOffset) {
-        if (isSphericalGrid()) {
-            return calc_constants.lon_LL + xOffset;
-        }
-        return xOffset;
-    }
-
-    function timeSeriesOffsetToDisplayY(yOffset) {
-        if (isSphericalGrid()) {
-            return calc_constants.lat_LL + yOffset;
-        }
-        return yOffset;
-    }
-
-    function timeSeriesDisplayToOffsetX(xDisplay) {
-        if (isSphericalGrid()) {
-            return xDisplay - calc_constants.lon_LL;
-        }
-        return xDisplay;
-    }
-
-    function timeSeriesDisplayToOffsetY(yDisplay) {
-        if (isSphericalGrid()) {
-            return yDisplay - calc_constants.lat_LL;
-        }
-        return yDisplay;
-    }
-
-    function getSelectedTimeSeriesLocation() {
-        const index = Math.round(calc_constants.changethisTimeSeries);
-        return calc_constants.locationOfTimeSeries[index] || null;
-    }
-
-    function updateTimeSeriesCoordinateLabels() {
-        const xLabel = document.querySelector('label[for="changeXTimeSeries-input"]');
-        const yLabel = document.querySelector('label[for="changeYTimeSeries-input"]');
-        if (!xLabel || !yLabel) {
-            return;
-        }
-        if (isSphericalGrid()) {
-            xLabel.textContent = 'New Time Series longitude (deg) :';
-            yLabel.textContent = 'New Time Series latitude (deg) :';
-        } else {
-            xLabel.textContent = 'New Time Series x-location (m) :';
-            yLabel.textContent = 'New Time Series y-location (m) :';
-        }
-    }
-
-    function syncTimeSeriesInputsFromSelectedLocation() {
-        const selectedLocation = getSelectedTimeSeriesLocation();
-        if (!selectedLocation) {
-            return;
-        }
-
-        calc_constants.changeXTimeSeries = timeSeriesOffsetToDisplayX(selectedLocation.xts);
-        calc_constants.changeYTimeSeries = timeSeriesOffsetToDisplayY(selectedLocation.yts);
-
-        const xInput = document.getElementById('changeXTimeSeries-input');
-        const yInput = document.getElementById('changeYTimeSeries-input');
-        if (xInput) {
-            xInput.value = calc_constants.changeXTimeSeries;
-        }
-        if (yInput) {
-            yInput.value = calc_constants.changeYTimeSeries;
-        }
-    }
-    // Added by Codex: End time-series coordinate conversion helpers.
-
-    // CODEX: Refresh the visible start/end coordinate summary from calc_constants.
-    function updateLinearStructureLocationsDisplay() {
-        const linearStructureContainer = document.getElementById('linearstructurelocs-container');
-        if (!linearStructureContainer) {
-            return;
-        }
-        const startText = calc_constants.designcomponent_StartDefined == 1
-            ? `Start: (${calc_constants.designcomponent_StartX.toFixed(2)}, ${calc_constants.designcomponent_StartY.toFixed(2)}) m`
-            : 'Start: not set';
-        const endText = calc_constants.designcomponent_EndDefined == 1
-            ? `End: (${calc_constants.designcomponent_EndX.toFixed(2)}, ${calc_constants.designcomponent_EndY.toFixed(2)}) m`
-            : 'End: not set';
-        linearStructureContainer.innerHTML = `${startText}<br>${endText}`;
-    }
-
-    // CODEX: Store the current x/y input pair into the selected linear-structure endpoint.
-    function storeLinearStructureEndpointFromInputs() {
-        if (Math.round(calc_constants.designcomponent_CurrentEndPoint) == 1) {
-            calc_constants.designcomponent_StartX = calc_constants.designcomponent_xLoc;
-            calc_constants.designcomponent_StartY = calc_constants.designcomponent_yLoc;
-            calc_constants.designcomponent_StartDefined = 1;
-        } else {
-            calc_constants.designcomponent_EndX = calc_constants.designcomponent_xLoc;
-            calc_constants.designcomponent_EndY = calc_constants.designcomponent_yLoc;
-            calc_constants.designcomponent_EndDefined = 1;
-        }
-        calc_constants.designcomponent_PreviewOn = 1;
-        calc_constants.html_update = 1;
-        updateLinearStructureLocationsDisplay();
-    }
-
-    // CODEX: Load the selected stored endpoint back into the shared x/y input fields.
-    function loadLinearStructureEndpointIntoInputs() {
-        if (Math.round(calc_constants.designcomponent_CurrentEndPoint) == 1 && calc_constants.designcomponent_StartDefined == 1) {
-            calc_constants.designcomponent_xLoc = calc_constants.designcomponent_StartX;
-            calc_constants.designcomponent_yLoc = calc_constants.designcomponent_StartY;
-        } else if (Math.round(calc_constants.designcomponent_CurrentEndPoint) == 1) {
-            calc_constants.designcomponent_xLoc = 0.0;
-            calc_constants.designcomponent_yLoc = 0.0;
-        } else if (Math.round(calc_constants.designcomponent_CurrentEndPoint) == 2 && calc_constants.designcomponent_EndDefined == 1) {
-            calc_constants.designcomponent_xLoc = calc_constants.designcomponent_EndX;
-            calc_constants.designcomponent_yLoc = calc_constants.designcomponent_EndY;
-        } else if (Math.round(calc_constants.designcomponent_CurrentEndPoint) == 2) {
-            calc_constants.designcomponent_xLoc = 0.0;
-            calc_constants.designcomponent_yLoc = 0.0;
-        }
-        const xInput = document.getElementById('designcomponent_xLoc-input');
-        const yInput = document.getElementById('designcomponent_yLoc-input');
-        if (xInput) {
-            xInput.value = calc_constants.designcomponent_xLoc;
-        }
-        if (yInput) {
-            yInput.value = calc_constants.designcomponent_yLoc;
-        }
-        updateLinearStructureLocationsDisplay();
-    }
-
-    // CODEX: Clear linear-structure endpoints and preview state after the Add Linear Structure action completes.
-    function resetLinearStructureEndpoints() {
-        calc_constants.designcomponent_StartX = 0.0;
-        calc_constants.designcomponent_StartY = 0.0;
-        calc_constants.designcomponent_EndX = 0.0;
-        calc_constants.designcomponent_EndY = 0.0;
-        calc_constants.designcomponent_StartDefined = 0;
-        calc_constants.designcomponent_EndDefined = 0;
-        calc_constants.designcomponent_PreviewOn = 0;
-        // CODEX: Clear any pending linear-structure add request when endpoints are reset.
-        calc_constants.designcomponent_AddLinearStructure = 0;
-        calc_constants.designcomponent_xLoc = 0.0;
-        calc_constants.designcomponent_yLoc = 0.0;
-        const xInput = document.getElementById('designcomponent_xLoc-input');
-        const yInput = document.getElementById('designcomponent_yLoc-input');
-        if (xInput) {
-            xInput.value = calc_constants.designcomponent_xLoc;
-        }
-        if (yInput) {
-            yInput.value = calc_constants.designcomponent_yLoc;
-        }
-        calc_constants.html_update = 1;
-        updateLinearStructureLocationsDisplay();
-    }
-
-    // CODEX: Queue a linear-structure bathy/topo edit for the next MouseClickChange dispatch.
-    function requestAddLinearStructure(options = {}) {
-        const fail = (message) => {
-            if (!options.silent) {
-                alert(message);
-            }
-            return { ok: false, message };
-        };
-        if (!device) {
-            return fail('Start a simulation before adding a linear structure.');
-        }
-        if (calc_constants.viewType != 1 || calc_constants.whichPanelisOpen != 2) {
-            return fail('Open the Add Engineered Design Components panel in Design mode before adding a linear structure.');
-        }
-        if (calc_constants.designcomponent_StartDefined != 1 || calc_constants.designcomponent_EndDefined != 1) {
-            return fail('Define both the linear structure start and end locations before adding the structure.');
-        }
-        const linearStructureLength = Math.hypot(
-            calc_constants.designcomponent_EndX - calc_constants.designcomponent_StartX,
-            calc_constants.designcomponent_EndY - calc_constants.designcomponent_StartY
-        );
-        if (linearStructureLength <= Math.max(calc_constants.dx, calc_constants.dy)) {
-            return fail('Choose start and end locations that are farther apart.');
-        }
-        if (calc_constants.designcomponent_CrestWidth <= 0.0 || calc_constants.designcomponent_SideSlope <= 0.0) {
-            return fail('Use a positive crest width and positive side slope before adding the linear structure.');
-        }
-        calc_constants.designcomponent_AddLinearStructure = 1;
-        calc_constants.click_update = 1;
-        calc_constants.designcomponent_PreviewOn = 1;
-        return { ok: true };
-    }
-
-    // CODEX: Store a right-clicked world point as the currently selected linear-structure endpoint.
-    function storeLinearStructureEndpointFromPointer(event) {
-        const endpointLocation = getCanvasWorldCoordinates(event);
-        if (!endpointLocation) {
-            return;
-        }
-        calc_constants.designcomponent_xLoc = endpointLocation.x;
-        calc_constants.designcomponent_yLoc = endpointLocation.y;
-        storeLinearStructureEndpointFromInputs();
-        loadLinearStructureEndpointIntoInputs();
-    }
-
-    // CODEX: Compute midpoint and distance for active two-finger Explorer gestures.
-    function getExplorerTouchGesture() {
-        const touches = Array.from(activeExplorerTouches.values());
-        if (touches.length < 2) {
-            return null;
-        }
-        const firstTouch = touches[0];
-        const secondTouch = touches[1];
-        const midX = 0.5 * (firstTouch.x + secondTouch.x);
-        const midY = 0.5 * (firstTouch.y + secondTouch.y);
-        const deltaX = firstTouch.x - secondTouch.x;
-        const deltaY = firstTouch.y - secondTouch.y;
-        const distance = Math.max(1.0, Math.hypot(deltaX, deltaY));
-        return { midX, midY, distance };
-    }
-
     // Event listener for mousedown - start of the hold
     canvas.addEventListener('pointerdown', function (event) {
         // edit for touch screens
```

#### CT1-318 pointerdown 입력 경로

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4228; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2575; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 한 손가락 회전·두 손가락 이동·Ctrl 좌클릭 회전·선형 끝점 우클릭·측정점 좌표 표시 동기화를 추가한다. transect 판은 기존 마우스 버튼 처리만 쓴다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 4231행 포함); `d778fe7` 2026-06-02 (현재 4269행 포함); `0ee5174` 2026-06-18 (현재 4270행 포함); `ff0d046` 2026-07-07 (현재 4280행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2578행 포함).

```diff
@@ -4228,57 +2575,20 @@
 
         // 3) existing logic:
 
-        // CODEX: Touch in Explorer mode uses mobile gestures instead of mouse-button semantics.
-        if (event.pointerType === 'touch' && calc_constants.viewType == 2) {
-            activeExplorerTouches.set(event.pointerId, { x: event.clientX, y: event.clientY });
-            if (activeExplorerTouches.size >= 2) {
-                const touchGesture = getExplorerTouchGesture();
-                if (touchGesture) {
-                    leftMouseIsDown = false;
-                    rightMouseIsDown = false;
-                    lastTouchMidX = touchGesture.midX;
-                    lastTouchMidY = touchGesture.midY;
-                    lastTouchDistance = touchGesture.distance;
-                }
-            } else {
-                rightMouseIsDown = true;
-                lastMouseX_right = event.clientX;
-                lastMouseY_right = event.clientY;
-            }
-            calc_constants.click_update = 2;
-        // if (event.button === 0 && calc_constants.viewType == 1) { // Left mouse button, Design mode
-        } else if (event.button === 0 && calc_constants.viewType == 1) { // Left mouse button, Design mode
+        if (event.button === 0 && calc_constants.viewType == 1) { // Left mouse button, Design mode
             leftMouseIsDown = true;
             handleMouseEvent(event);  // Handle the initial click
-        // } else if (event.button === 0 && calc_constants.viewType == 2) { // Left mouse button, Explorer mode
-        //     leftMouseIsDown = true;
-        //     lastMouseX_left = event.clientX;
-        //     lastMouseY_left = event.clientY;
-        //     calc_constants.click_update = 2;
-        // CODEX: On Mac trackpads, Ctrl + left-drag provides a rotation fallback when right-drag is awkward.
-        } else if (event.button === 0 && event.ctrlKey && calc_constants.viewType == 2) {
-            rightMouseIsDown = true;
-            lastMouseX_right = event.clientX;
-            lastMouseY_right = event.clientY;
-            calc_constants.click_update = 2;
         } else if (event.button === 0 && calc_constants.viewType == 2) { // Left mouse button, Explorer mode
             leftMouseIsDown = true;
             lastMouseX_left = event.clientX;
             lastMouseY_left = event.clientY;
             calc_constants.click_update = 2;
-        } else if (event.button === 2 && calc_constants.viewType == 1 && calc_constants.whichPanelisOpen == 2) { // CODEX: Right-click stores the selected linear-structure endpoint in Design mode.
-            if (agentDesignInteractionMode === "surface") {
-                return;
-            }
-            storeLinearStructureEndpointFromPointer(event);
         } else if (event.button === 2 && calc_constants.viewType == 1 && calc_constants.whichPanelisOpen == 7) { // right mouse button, Design mode for time series
             rightMouseIsDown = true;
             lastMouseX_right = event.clientX;
             lastMouseY_right = event.clientY;
             calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].xts = x_position;
             calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].yts = y_position;
-            // Added by Codex: Display lon/lat in the time-series inputs for spherical grids while storing lower-left-relative offsets internally.
-            syncTimeSeriesInputsFromSelectedLocation();
             calc_constants.click_update = 2;
             calc_constants.updateTimeSeriesTx = 1;  // by setting to one, will tell timesereies shader to run and update chart
         } else if (event.button === 2 && calc_constants.viewType == 2) { // right mouse button, Explorer mode
```

#### CT1-319 pointermove 터치 동작

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4291; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2601; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 터치 한 손가락 회전과 두 손가락 pan·pinch를 처리한다. 수치 계산식은 바뀌지 않는다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 4294행 포함); `62b1458` 2026-05-24 (현재 4301행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -4291,41 +2601,6 @@
 
     // Event listener for mousemove - if mouse is down, it's equivalent to multiple clicks
     canvas.addEventListener('pointermove', function (event) {
-        // CODEX: iPhone/iPad Explorer gestures: one finger rotates, two fingers pan and pinch-zoom.
-        if (event.pointerType === 'touch' && calc_constants.viewType == 2 && activeExplorerTouches.has(event.pointerId)) {
-            activeExplorerTouches.set(event.pointerId, { x: event.clientX, y: event.clientY });
-            if (activeExplorerTouches.size >= 2) {
-                const touchGesture = getExplorerTouchGesture();
-                if (touchGesture) {
-                    const deltaX = touchGesture.midX - lastTouchMidX;
-                    // const deltaY = touchGesture.midY - lastTouchMidY;
-                    const motion_inc = 0.0001 * calc_constants.forward;
-                    // CODEX: Two-finger horizontal drag strafes left/right; pinch maps to shift_y like W/S and up/down keys.
-                    const pinchDelta = touchGesture.distance - lastTouchDistance;
-                    calc_constants.shift_x += deltaX * motion_inc;
-                    calc_constants.shift_y += pinchDelta * 0.0001;
-                    // calc_constants.shift_y -= deltaY * motion_inc * calc_constants.WIDTH / calc_constants.HEIGHT;
-                    // calc_constants.forward *= lastTouchDistance / touchGesture.distance;
-                    // calc_constants.forward = Math.max(0.001, Math.min(100, calc_constants.forward));
-                    lastTouchMidX = touchGesture.midX;
-                    lastTouchMidY = touchGesture.midY;
-                    lastTouchDistance = touchGesture.distance;
-                    calc_constants.click_update = 2;
-                }
-            } else {
-                const deltaX = event.clientX - lastMouseX_right;
-                calc_constants.rotationAngle_xy -= deltaX * 0.1;
-
-                const deltaY = event.clientY - lastMouseY_right
-                calc_constants.rotationAngle_xz -= deltaY * 0.1;
-
-                lastMouseX_right = event.clientX;
-                lastMouseY_right = event.clientY;
-                calc_constants.click_update = 2;
-            }
-            return;
-        }
-
         if (leftMouseIsDown && calc_constants.viewType == 1) {
             handleMouseEvent(event);
         } else if (leftMouseIsDown && calc_constants.viewType == 2) {
```

#### CT1-320 pointerup 정리

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4357; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2632; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 터치 목록과 Ctrl 좌클릭 회전 상태까지 정리한다. transect 판은 좌·우 마우스 상태만 정리한다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 4360행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2635행 포함).

```diff
@@ -4357,32 +2632,8 @@
         // release capture so the pointer is freed, edit for touch screens
         canvas.releasePointerCapture(event.pointerId);
 
-        // CODEX: End or downgrade active Explorer touch gestures without touching desktop mouse state.
-        if (event.pointerType === 'touch' && calc_constants.viewType == 2) {
-            activeExplorerTouches.delete(event.pointerId);
-            if (activeExplorerTouches.size == 1) {
-                const remainingTouch = Array.from(activeExplorerTouches.values())[0];
-                rightMouseIsDown = true;
-                leftMouseIsDown = false;
-                lastMouseX_right = remainingTouch.x;
-                lastMouseY_right = remainingTouch.y;
-                calc_constants.click_update = 2;
-            } else {
-                leftMouseIsDown = false;
-                rightMouseIsDown = false;
-                calc_constants.click_update = 0;
-            }
-            return;
-        }
-
-        // if (event.button === 0) { // Left mouse button
-        // CODEX: Touch rotation also uses this cleanup path, even when pointerup is not reported as a mouse button.
-        if (event.pointerType === 'touch' || event.button === 0) { // Left mouse button or touch
-            // leftMouseIsDown = false;
-            // calc_constants.click_update = 0;  // Optionally, reset the click_update here if needed
-            // CODEX: Ctrl + left-drag rotation uses rightMouseIsDown, so left-button release clears both drag modes.
+        if (event.button === 0) { // Left mouse button
             leftMouseIsDown = false;
-            rightMouseIsDown = false;
             calc_constants.click_update = 0;  // Optionally, reset the click_update here if needed
         } else if (event.button === 2) { // Right mouse button
             rightMouseIsDown = false;
```

#### CT1-321 pointercancel 터치 목록

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4399; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2650; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 activeExplorerTouches에서 취소한 포인터를 제거한다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 4402행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -4399,8 +2650,6 @@
     // also handle pointercancel just in case the browser forcibly cancels:
     canvas.addEventListener('pointercancel', function(event) {
         canvas.releasePointerCapture(event.pointerId);
-        // CODEX: Keep touch gesture bookkeeping in sync with browser-cancelled touch pointers.
-        activeExplorerTouches.delete(event.pointerId);
         leftMouseIsDown = rightMouseIsDown = false;
         calc_constants.click_update = 0;
     });
```

#### CT1-322 키보드 입력 중 카메라 간섭

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4415; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2664; 아래 전체 diff의 +행 | 불일치 (E) | 본판은 폼 편집과 Design 모드에서 Explorer 이동키를 차단한다. transect 판은 입력 대상과 viewType을 검사하지 않는다. event.key 대신 code를 쓰는 변경과 P/Pause 정지 기능 추가도 본판에 있다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 4418행 포함); `471c581` 2024-01-04 (현재 4434행 포함); `ea93d70` 2025-10-24 (현재 4467행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2667행 포함).

```diff
@@ -4415,62 +2664,28 @@
     // Event listener for keydown - to handle arrow keys for shifting
     document.addEventListener('keydown', function (event) {
         const shiftAmount = 0.001; // Change this value to shift by more or less  
-        // calc_constants.click_update = 2;
-        // CODEX: Ignore keyboard shortcuts while the user is editing form controls.
-        const eventTargetTag = event.target && event.target.tagName ? event.target.tagName.toLowerCase() : '';
-        if (eventTargetTag === 'input' || eventTargetTag === 'select' || eventTargetTag === 'textarea' || event.target?.isContentEditable) {
-            return;
-        }
-
-        // CODEX: Explorer navigation keys should only affect the 3D Explorer view.
-        const isExplorerNavigationKey = ['KeyA', 'KeyD', 'KeyW', 'KeyS', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(event.code);
-        if (isExplorerNavigationKey && calc_constants.viewType != 2) {
-            return;
-        }
-        if (isExplorerNavigationKey && event.cancelable) {
-            event.preventDefault();
-        }
-        if (isExplorerNavigationKey) {
-            calc_constants.click_update = 2;
-        }
-
-        // switch (event.key) {
-        // CODEX: Use physical key codes so WASD navigation is layout-stable across platforms.
-        switch (event.code) {
-            // case 'a': // 'A' key for left
-            // case 'A':
-            case 'KeyA':
+        calc_constants.click_update = 2;
+        switch (event.key) {
+            case 'a': // 'A' key for left
+            case 'A':
             case 'ArrowLeft': // Left arrow key
                 calc_constants.shift_x -= shiftAmount;
                 break;
-            // case 'd': // 'D' key for right
-            // case 'D':
-            case 'KeyD':
+            case 'd': // 'D' key for right
+            case 'D':
             case 'ArrowRight': // Right arrow key
                 calc_constants.shift_x += shiftAmount;
                 break;
-            // case 'w': // 'W' key for up
-            // case 'W':
-            case 'KeyW':
+            case 'w': // 'W' key for up
+            case 'W':
             case 'ArrowUp': // Up arrow key
                 calc_constants.shift_y += shiftAmount;
                 break;
-            // case 's': // 'S' key for down
-            // case 'S':
-            case 'KeyS':
+            case 's': // 'S' key for down
+            case 'S':
             case 'ArrowDown': // Down arrow key
                 calc_constants.shift_y -= shiftAmount;
                 break;
-            // case 'p': // 'P' key for pause
-            // case 'P':
-            case 'KeyP':
-            case 'Pause': // Pause/Break key
-                if (calc_constants.simPause < 0) {
-                    calc_constants.simPause = 1;
-                } else {
-                    calc_constants.simPause = -1;
-                }
-                break;
         }
     });
     // end keyboard interaction
```

#### CT1-323 툴팁의 표시 영역 좌표

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4522; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2737; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 canvas 외곽 사각형을 정규화한다. 본판은 object-fit 여백을 제외한다. 격자 좌표와 표시 위치의 불일치를 고친 한쪽 수정이다. |

본판 차이 줄의 마지막 수정: `0ee5174` 2026-06-18 (현재 4525행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2740행 포함).

```diff
@@ -4522,19 +2737,17 @@
     let x_position = 0.0;
     let y_position = 0.0;
     canvas.addEventListener('mousemove', async (event) => {
-        const bounds = getCanvasContentRect(); // Visible rendered canvas content, excluding object-fit letterboxing.
-        if (!bounds || !isPointerInCanvasContent(event, bounds)) {
-            tooltip.style.display = 'none';
-            return;
-        }
+        const bounds = canvas.getBoundingClientRect(); // Get the bounding rectangle of the canvas
     
         // Calculate coordinates relative to the canvas
         const x = event.clientX;
         const y = event.clientY;
         
         // Normalize the coordinates to [0, 1]
-        const normalizedX = (x - bounds.left) / bounds.width; //normalizedX;
-        const normalizedY = 1.0 - (y - bounds.top) / bounds.height; //normalizedY;
+        const canvas_width = bounds.right - bounds.left;
+        const canvas_height = bounds.bottom - bounds.top;
+        const normalizedX = (x - bounds.left) / canvas_width; //normalizedX;
+        const normalizedY = 1.0 - (y - bounds.top) / canvas_height; //normalizedY;
         
         // Update your constants for WebGPU
         //calc_constants.mouse_current_canvas_positionX = normalizedX;
```

#### CT1-324 툴팁 단위와 교란 표시

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4559; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2772; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 구면 경위도 소수 6자리와 교란 시 최대수면을 표시한다. transect 판은 X/Y m 소수 2자리와 유의파고를 표시한다. 하천의 속력 표시는 유지한다. |

본판 차이 줄의 마지막 수정: `a0a8a9c` 2024-05-01 (현재 4562행 포함); `afc1fe7` 2026-06-19 (현재 4564행 포함); `5eaa968` 2025-03-05 (현재 4577행 포함); `397c575` 2025-09-09 (현재 4578행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2775행 포함).

```diff
@@ -4559,36 +2772,20 @@
     
     function updateTooltip() {
         // Assuming x_position and y_position are updated elsewhere in your code and accessible here
-
-        if (calc_constants.viewType == 1){
-            // Added by Codex: Start grid-aware tooltip coordinate labels.
-            let tooltipCoordinateText = `x-coordinate (m): ${x_position.toFixed(2)}<br>y-coordinate (m): ${y_position.toFixed(2)}`;
-            if (calc_constants.grid_type == 2) {
-                const tooltipLongitude = calc_constants.lon_LL + x_position;
-                const tooltipLatitude = calc_constants.lat_LL + y_position;
-                tooltipCoordinateText = `longitude (deg): ${tooltipLongitude.toFixed(6)}<br>latitude (deg): ${tooltipLatitude.toFixed(6)}`;
-            }
-            // Added by Codex: End grid-aware tooltip coordinate labels.
+        
+        if (calc_constants.viewType == 1){ 
             if (calc_constants.river_sim == 1){
                 let flow_depth = calc_constants.tooltipVal_eta - calc_constants.tooltipVal_bottom;
-                // tooltip.innerHTML = `x-coordinate (m): ${x_position.toFixed(2)}<br>y-coordinate (m): ${y_position.toFixed(2)}<br>bottom elevation (m): ${calc_constants.tooltipVal_bottom.toFixed(2)} <br>friction factor: ${calc_constants.tooltipVal_friction.toFixed(3)}<br>surface elevation (m): ${calc_constants.tooltipVal_eta.toFixed(2)} <br>flow depth (m): ${flow_depth.toFixed(2)} <br>flow speed (m/s): ${calc_constants.tooltipVal_Hs.toFixed(2)}`;
-                // Added by Codex: Use grid-aware coordinates in tooltip output.
-                tooltip.innerHTML = `${tooltipCoordinateText}<br>bottom elevation (m): ${calc_constants.tooltipVal_bottom.toFixed(2)} <br>friction factor: ${calc_constants.tooltipVal_friction.toFixed(3)}<br>surface elevation (m): ${calc_constants.tooltipVal_eta.toFixed(2)} <br>flow depth (m): ${flow_depth.toFixed(2)} <br>flow speed (m/s): ${calc_constants.tooltipVal_Hs.toFixed(2)}`;
-            }
-            else if (calc_constants.disturbanceType > 1) {
-                // tooltip.innerHTML = `x-coordinate (m): ${x_position.toFixed(2)}<br>y-coordinate (m): ${y_position.toFixed(2)}<br>bathy/topo (m): ${calc_constants.tooltipVal_bottom.toFixed(2)} <br>friction factor: ${calc_constants.tooltipVal_friction.toFixed(3)}<br>surface elevation (m): ${calc_constants.tooltipVal_eta.toFixed(2)} <br>max free surface (m): ${calc_constants.tooltipVal_Hs.toFixed(2)}`;
-                // Added by Codex: Use grid-aware coordinates in tooltip output.
-                tooltip.innerHTML = `${tooltipCoordinateText}<br>bathy/topo (m): ${calc_constants.tooltipVal_bottom.toFixed(2)} <br>friction factor: ${calc_constants.tooltipVal_friction.toFixed(3)}<br>surface elevation (m): ${calc_constants.tooltipVal_eta.toFixed(2)} <br>max free surface (m): ${calc_constants.tooltipVal_Hs.toFixed(2)}`;
+                tooltip.innerHTML = `x-coordinate (m): ${x_position.toFixed(2)}<br>y-coordinate (m): ${y_position.toFixed(2)}<br>bottom elevation (m): ${calc_constants.tooltipVal_bottom.toFixed(2)} <br>friction factor: ${calc_constants.tooltipVal_friction.toFixed(3)}<br>surface elevation (m): ${calc_constants.tooltipVal_eta.toFixed(2)} <br>flow depth (m): ${flow_depth.toFixed(2)} <br>flow speed (m/s): ${calc_constants.tooltipVal_Hs.toFixed(2)}`;    
             }
             else {
-                // tooltip.innerHTML = `x-coordinate (m): ${x_position.toFixed(2)}<br>y-coordinate (m): ${y_position.toFixed(2)}<br>bathy/topo (m): ${calc_constants.tooltipVal_bottom.toFixed(2)} <br>friction factor: ${calc_constants.tooltipVal_friction.toFixed(3)}<br>surface elevation (m): ${calc_constants.tooltipVal_eta.toFixed(2)} <br>sig wave height (m): ${calc_constants.tooltipVal_Hs.toFixed(2)}`;
-                // Added by Codex: Use grid-aware coordinates in tooltip output.
-                tooltip.innerHTML = `${tooltipCoordinateText}<br>bathy/topo (m): ${calc_constants.tooltipVal_bottom.toFixed(2)} <br>friction factor: ${calc_constants.tooltipVal_friction.toFixed(3)}<br>surface elevation (m): ${calc_constants.tooltipVal_eta.toFixed(2)} <br>sig wave height (m): ${calc_constants.tooltipVal_Hs.toFixed(2)}`;
+                tooltip.innerHTML = `x-coordinate (m): ${x_position.toFixed(2)}<br>y-coordinate (m): ${y_position.toFixed(2)}<br>bathy/topo (m): ${calc_constants.tooltipVal_bottom.toFixed(2)} <br>friction factor: ${calc_constants.tooltipVal_friction.toFixed(3)}<br>surface elevation (m): ${calc_constants.tooltipVal_eta.toFixed(2)} <br>sig wave height (m): ${calc_constants.tooltipVal_Hs.toFixed(2)}`;
             }
          } else {
             tooltip.innerHTML = ``;
         }
     }
+    
     // Set this function to be called every 100 milliseconds
     const updateInterval = 100; // Adjust the interval as needed
     setInterval(updateTooltip, updateInterval);
```

#### CT1-325 UI 동기화 후처리

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4662; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2859; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 선형 끝점 요약과 격자 유형별 측정점 좌표 입력을 동기화한다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 4665행 포함); `ff0d046` 2026-07-07 (현재 4667행 포함); `9c5b1a6` 2023-10-27 (현재 4670행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2862행 포함).

```diff
@@ -4662,12 +2859,7 @@
             var selectElement = document.getElementById(action.input);
             selectElement.value = currentValue;
         });
-        // CODEX: Keep the linear-structure start/end status display synchronized with calc_constants.
-        updateLinearStructureLocationsDisplay();
-        // Added by Codex: Keep time-series inputs/labels in lon/lat for spherical grids and x/y for Cartesian grids.
-        updateTimeSeriesCoordinateLabels();
-        syncTimeSeriesInputsFromSelectedLocation();
-    }
+    }    
 
     // Parameters for each button/input pair which has some numerical input value, and an associated "Update" button
     const buttonActions = [
```

#### CT1-326 선형 구조물 수치 버튼

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4708; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2900; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 천단고·폭·경사·양끝 좌표를 표준 update 버튼 목록에 넣는다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 4711행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -4708,12 +2900,6 @@
         { id: 'JPEGstack_dt-button', input: 'JPEGstack_dt-input', property: 'JPEGstack_dt' },
         { id: 'JPEGstack_frames-button', input: 'JPEGstack_frames-input', property: 'JPEGstack_frames' },
         { id: 'designcomponent_Radius-button', input: 'designcomponent_Radius-input', property: 'designcomponent_Radius' },
-        // CODEX: Wire linear-structure numeric inputs into the standard calc_constants update path.
-        { id: 'designcomponent_CrestElev-button', input: 'designcomponent_CrestElev-input', property: 'designcomponent_CrestElev' },
-        { id: 'designcomponent_CrestWidth-button', input: 'designcomponent_CrestWidth-input', property: 'designcomponent_CrestWidth' },
-        { id: 'designcomponent_SideSlope-button', input: 'designcomponent_SideSlope-input', property: 'designcomponent_SideSlope' },
-        { id: 'designcomponent_xLoc-button', input: 'designcomponent_xLoc-input', property: 'designcomponent_xLoc' },
-        { id: 'designcomponent_yLoc-button', input: 'designcomponent_yLoc-input', property: 'designcomponent_yLoc' },
         { id: 'designcomponent_Fric_Coral-button', input: 'designcomponent_Fric_Coral-input', property: 'designcomponent_Fric_Coral' },
         { id: 'designcomponent_Fric_Oyser-button', input: 'designcomponent_Fric_Oyser-input', property: 'designcomponent_Fric_Oyser' },
         { id: 'designcomponent_Fric_Mangrove-button', input: 'designcomponent_Fric_Mangrove-input', property: 'designcomponent_Fric_Mangrove' },
```

#### CT1-327 중첩 출력 수치 버튼

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4726; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2912; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 사각형 인덱스·출력 기간·간격·eta 임계값을 update 버튼 목록에 넣는다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 4729행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -4726,18 +2912,6 @@
         { id: 'designcomponent_Fric_Seawall-button', input: 'designcomponent_Fric_Seawall-input', property: 'designcomponent_Fric_Seawall' },
         { id: 'changeSeaLevel-button', input: 'changeSeaLevel-input', property: 'changeSeaLevel' },
         { id: 'dt_writesurface-button', input: 'dt_writesurface-input', property: 'dt_writesurface' },
-        // Added by Codex: Start nested-grid boundary time-series output controls.
-        { id: 'nestedGridOutput_i0-button', input: 'nestedGridOutput_i0-input', property: 'nestedGridOutput_i0' },
-        { id: 'nestedGridOutput_j0-button', input: 'nestedGridOutput_j0-input', property: 'nestedGridOutput_j0' },
-        { id: 'nestedGridOutput_i1-button', input: 'nestedGridOutput_i1-input', property: 'nestedGridOutput_i1' },
-        { id: 'nestedGridOutput_j1-button', input: 'nestedGridOutput_j1-input', property: 'nestedGridOutput_j1' },
-        { id: 'nestedGridOutput_start_time-button', input: 'nestedGridOutput_start_time-input', property: 'nestedGridOutput_start_time' },
-        { id: 'nestedGridOutput_end_time-button', input: 'nestedGridOutput_end_time-input', property: 'nestedGridOutput_end_time' },
-        { id: 'nestedGridOutput_dt-button', input: 'nestedGridOutput_dt-input', property: 'nestedGridOutput_dt' },
-        // Added by Codex: Start nested-grid quiet-period trim threshold control.
-        { id: 'nestedEtaWriteThreshold-button', input: 'nestedEtaWriteThreshold-input', property: 'nestedEtaWriteThreshold' },
-        // Added by Codex: End nested-grid quiet-period trim threshold control.
-        // Added by Codex: End nested-grid boundary time-series output controls.
         { id: 'incident_wave_H-button', input: 'incident_wave_H-input', property: 'incident_wave_H' },
         { id: 'incident_wave_T-button', input: 'incident_wave_T-input', property: 'incident_wave_T' },
         { id: 'incident_wave_direction-button', input: 'incident_wave_direction-input', property: 'incident_wave_direction' },
```

#### CT1-328 선형 끝점 선택 목록

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4766; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2940; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 시작점·끝점 선택을 calc_constants에 연결한다. |

본판 차이 줄의 마지막 수정: `d778fe7` 2026-06-02 (현재 4769행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -4766,8 +2940,6 @@
         { input: 'changethisTimeSeries-select', property: 'changethisTimeSeries' },
         { input: 'useBreakingModel-select', property: 'useBreakingModel' },
         { input: 'designcomponentToAdd-select', property: 'designcomponentToAdd' },
-        // CODEX: Track which linear-structure endpoint the shared x/y inputs edit.
-        { input: 'designcomponent_CurrentEndPoint-select', property: 'designcomponent_CurrentEndPoint' },
         { input: 'ShowArrows-select', property: 'ShowArrows' },
         { input: 'ShowLogos-select', property: 'ShowLogos' },
         { input: 'write_eta-select', property: 'write_eta' },
```

#### CT1-329 외부 제어 설치

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4782; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2954; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 installCelerisAgentControls에 수치 상태 조회·예제 실행·view 선택·전체화면 정리·설계 모드·선형 구조물 요청 callback을 전달한다. CelerisAgent 내부는 판독하지 않는다. |

본판 차이 줄의 마지막 수정: `0ee5174` 2026-06-18 (현재 4785행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -4782,45 +2954,6 @@
 
     // Call the function for setting up listeners on dropdown menus
     setupDropdownListeners(button_dropdown_Actions);
-    installCelerisAgentControls({
-        calcConstants: calc_constants,
-        getCalcConstants: () => calc_constants,
-        updateCalcConstants,
-        updateAllUIElements,
-        runExample: (exampleValue) => {
-            agentDesignInteractionMode = null;
-            calc_constants.run_example = exampleValue;
-            initializeWebGPUApp();
-            setTimeout(updateAllUIElements, 5000);
-        },
-        updateViewMode: (viewType) => {
-            updateCalcConstants("viewType", viewType);
-            updateZoomListener();
-            updateAllUIElements();
-        },
-        exitFullscreenCleanup: () => {
-            if (pseudoFullscreenActive) {
-                exitPseudoFullscreen();
-                return;
-            }
-            canvas.classList.remove('fullscreen');
-            calc_constants.full_screen = 0;
-            resizeCanvas();
-            updateCalcConstants("viewType", 1);
-            calc_constants.click_update = 1;
-            updateAllUIElements();
-            updateZoomListener();
-        },
-        setLinearStructureEndpointMode: (endpointMode) => {
-            updateCalcConstants("designcomponent_CurrentEndPoint", endpointMode);
-            loadLinearStructureEndpointIntoInputs();
-        },
-        setDesignInteractionMode: (mode) => {
-            agentDesignInteractionMode = mode === "surface" || mode === "linear" || mode === "timeseries" ? mode : null;
-        },
-        requestAddLinearStructure,
-        postStatus: postAgentCaseStatus,
-    });
 
     // set up listeners for the "Update" button fields
     buttonActions.forEach(({ id, input, property }) => {
```

#### CT1-330 전체화면 크기

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4854; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:2987; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 가상 전체화면과 visualViewport를 처리한다. transect 판은 실제 document.fullscreenElement만 처리한다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 4857행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 2994행 포함).

```diff
@@ -4854,29 +2987,18 @@
 
     // to make the canvas go full screen
     const fullscreenButton = document.getElementById('fullscreen-button');
-    // CODEX: Preserve inline styles so iOS pseudo-fullscreen can be reversed cleanly.
-    var pseudoFullscreenSavedStyle = null;
     // Function to adjust canvas size
     function resizeCanvas() {
         
         let grid_ratio = calc_constants.dx / calc_constants.dy;
-        // if (document.fullscreenElement) {
-        //     const window_width = window.innerWidth;
-        //     const window_height = window.innerHeight;
-        // CODEX: Treat pseudo-fullscreen like fullscreen for canvas sizing, using visualViewport when available.
-        if (document.fullscreenElement || pseudoFullscreenActive) {
-            const viewport = pseudoFullscreenActive && window.visualViewport ? window.visualViewport : window;
-            const window_width = Math.round(viewport.width || window.innerWidth);
-            const window_height = Math.round(viewport.height || window.innerHeight);
+        if (document.fullscreenElement) {
+            const window_width = window.innerWidth;
+            const window_height = window.innerHeight;
 
             // canvas_width_ratio and height will be updated at render time
             
             canvas.width = window_width;
             canvas.height = window_height;
-            if (pseudoFullscreenActive) {
-                canvas.style.width = `${window_width}px`;
-                canvas.style.height = `${window_height}px`;
-            }
         } else {
             // Set canvas size back to normal when exiting full screen
             if (grid_ratio >= 1.0) {
```

#### CT1-331 가상 전체화면 대체 경로

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:4920; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3042; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 실제 전체화면 미지원·거절 때 CSS 고정 화면을 쓴다. 종료 때 원래 inline style과 스크롤 상태를 복구한다. transect 판은 requestFullscreen 오류를 로그로만 남긴다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 4923행 포함); `6df8db9` 2024-01-05 (현재 5026행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 3046행 포함).

```diff
@@ -4920,119 +3042,14 @@
         });
     });
 
-    // CODEX: iOS fallback for browsers that cannot put the canvas into true fullscreen.
-    function enterPseudoFullscreen() {
-        if (pseudoFullscreenActive) {
-            return;
-        }
-        pseudoFullscreenSavedStyle = {
-            position: canvas.style.position,
-            left: canvas.style.left,
-            top: canvas.style.top,
-            width: canvas.style.width,
-            height: canvas.style.height,
-            zIndex: canvas.style.zIndex,
-            marginTop: canvas.style.marginTop,
-            marginBottom: canvas.style.marginBottom,
-            backgroundColor: canvas.style.backgroundColor,
-            bodyOverflow: document.body.style.overflow,
-            buttonPosition: fullscreenButton.style.position,
-            buttonRight: fullscreenButton.style.right,
-            buttonBottom: fullscreenButton.style.bottom,
-            buttonZIndex: fullscreenButton.style.zIndex,
-            buttonText: fullscreenButton.textContent,
-        };
-        pseudoFullscreenActive = true;
-        canvas.classList.add('fullscreen');
-        canvas.style.position = 'fixed';
-        canvas.style.left = '0px';
-        canvas.style.top = '0px';
-        canvas.style.zIndex = '9999';
-        canvas.style.marginTop = '0px';
-        canvas.style.marginBottom = '0px';
-        canvas.style.backgroundColor = 'black';
-        // CODEX: Keep the existing fullscreen button reachable as the pseudo-fullscreen exit control.
-        fullscreenButton.style.position = 'fixed';
-        fullscreenButton.style.right = '12px';
-        fullscreenButton.style.bottom = '12px';
-        fullscreenButton.style.zIndex = '10000';
-        fullscreenButton.textContent = 'Exit Full Screen';
-        document.body.style.overflow = 'hidden';
-        resizeCanvas();
-        updateCalcConstants('viewType', 2);
-        calc_constants.click_update = 2;
-        calc_constants.full_screen = 1;
-        updateZoomListener();
-        console.log("Entered pseudo-fullscreen mode");
-    }
-
-    // CODEX: Restore layout after the iOS pseudo-fullscreen fallback.
-    function exitPseudoFullscreen() {
-        if (!pseudoFullscreenActive) {
-            return;
-        }
-        pseudoFullscreenActive = false;
-        canvas.classList.remove('fullscreen');
-        if (pseudoFullscreenSavedStyle) {
-            canvas.style.position = pseudoFullscreenSavedStyle.position;
-            canvas.style.left = pseudoFullscreenSavedStyle.left;
-            canvas.style.top = pseudoFullscreenSavedStyle.top;
-            canvas.style.width = pseudoFullscreenSavedStyle.width;
-            canvas.style.height = pseudoFullscreenSavedStyle.height;
-            canvas.style.zIndex = pseudoFullscreenSavedStyle.zIndex;
-            canvas.style.marginTop = pseudoFullscreenSavedStyle.marginTop;
-            canvas.style.marginBottom = pseudoFullscreenSavedStyle.marginBottom;
-            canvas.style.backgroundColor = pseudoFullscreenSavedStyle.backgroundColor;
-            fullscreenButton.style.position = pseudoFullscreenSavedStyle.buttonPosition;
-            fullscreenButton.style.right = pseudoFullscreenSavedStyle.buttonRight;
-            fullscreenButton.style.bottom = pseudoFullscreenSavedStyle.buttonBottom;
-            fullscreenButton.style.zIndex = pseudoFullscreenSavedStyle.buttonZIndex;
-            fullscreenButton.textContent = pseudoFullscreenSavedStyle.buttonText;
-            document.body.style.overflow = pseudoFullscreenSavedStyle.bodyOverflow;
-        }
-        resizeCanvas();
-        updateCalcConstants('viewType', 1);
-        calc_constants.click_update = 1;
-        calc_constants.full_screen = 0;
-        updateAllUIElements();
-        updateZoomListener();
-        console.log("Exited pseudo-fullscreen mode");
-    }
-
-    // fullscreenButton.addEventListener('click', function () {
-    //     if (!document.fullscreenElement) {
-    //         canvas.requestFullscreen().then(() => {
-    //             canvas.classList.add('fullscreen'); // Add the full-screen class for styling
-    //             resizeCanvas(); // Resize the canvas to full screen dimensions
-    //         }).catch(err => {
-    //             console.log(`Error attempting to enable full-screen mode: ${err.message}`);
-    //         });
-    //     } else {
-    //         document.exitFullscreen().then(() => {
-    //             canvas.classList.remove('fullscreen'); // Remove the full-screen class
-    //             resizeCanvas(); // Resize the canvas back to normal dimensions
-    //             
-    //         }).catch(err => {
-    //             console.log(`Error attempting to disable full-screen mode: ${err.message}`);
-    //         });
-    //     }
-    // });
-    // CODEX: Keep desktop fullscreen unchanged, but fall back to pseudo-fullscreen when unsupported or rejected.
     fullscreenButton.addEventListener('click', function () {
-        if (pseudoFullscreenActive) {
-            exitPseudoFullscreen();
-        } else if (!document.fullscreenElement) {
-            if (canvas.requestFullscreen) {
-                canvas.requestFullscreen().then(() => {
-                    canvas.classList.add('fullscreen'); // Add the full-screen class for styling
-                    resizeCanvas(); // Resize the canvas to full screen dimensions
-                }).catch(err => {
-                    console.log(`Error attempting to enable full-screen mode: ${err.message}`);
-                    enterPseudoFullscreen();
-                });
-            } else {
-                enterPseudoFullscreen();
-            }
+        if (!document.fullscreenElement) {
+            canvas.requestFullscreen().then(() => {
+                canvas.classList.add('fullscreen'); // Add the full-screen class for styling
+                resizeCanvas(); // Resize the canvas to full screen dimensions
+            }).catch(err => {
+                console.log(`Error attempting to enable full-screen mode: ${err.message}`);
+            });
         } else {
             document.exitFullscreen().then(() => {
                 canvas.classList.remove('fullscreen'); // Remove the full-screen class
```

#### CT1-332 resize 이벤트 제한

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5045; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3062; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 80ms debounce와 visualViewport resize·scroll을 사용한다. transect 판은 window resize마다 즉시 갱신한다. |

본판 차이 줄의 마지막 수정: `24b8f13` 2026-05-24 (현재 5048행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 3065행 포함).

```diff
@@ -5045,18 +3062,7 @@
     });
 
     // Handle resize events when in full screen
-    // window.addEventListener('resize', resizeCanvas);
-    // CODEX: Debounce mobile viewport changes so iPhone/iPad browser chrome does not thrash canvas resizing.
-    var resizeCanvasTimer = null;
-    function scheduleResizeCanvas() {
-        clearTimeout(resizeCanvasTimer);
-        resizeCanvasTimer = setTimeout(resizeCanvas, 80);
-    }
-    window.addEventListener('resize', scheduleResizeCanvas);
-    if (window.visualViewport) {
-        window.visualViewport.addEventListener('resize', scheduleResizeCanvas);
-        window.visualViewport.addEventListener('scroll', scheduleResizeCanvas);
-    }
+    window.addEventListener('resize', resizeCanvas);
 
     // Listen for fullscreen change events
     document.addEventListener('fullscreenchange', function () {
```

#### CT1-333 측정점·선형 끝점·view 선택

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5123; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3129; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 구면 표시 좌표를 상대좌표로 바꾼다. 본판만 선형 끝점 버튼을 연결한다. 본판은 view 선택 뒤 blur하여 문서 키보드 동작을 복구한다. |

본판 차이 줄의 마지막 수정: `ff0d046` 2026-07-07 (현재 5126행 포함); `d778fe7` 2026-06-02 (현재 5143행 포함); `24b8f13` 2026-05-24 (현재 5162행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 3132행 포함).

```diff
@@ -5123,49 +3129,20 @@
     
     // add time series listener, to update time series location texture changeXTimeSeries-button
     document.getElementById('changeXTimeSeries-button').addEventListener('click', function () {
-        // calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].xts = calc_constants.changeXTimeSeries;
-        // Added by Codex: Convert displayed lon/lat input to lower-left-relative model offset for spherical grids.
-        calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].xts = timeSeriesDisplayToOffsetX(calc_constants.changeXTimeSeries);
-        syncTimeSeriesInputsFromSelectedLocation();
+        calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].xts = calc_constants.changeXTimeSeries;
         calc_constants.updateTimeSeriesTx = 1;  // by setting to one, will tell timesereies shader to run
     });
     document.getElementById('changeYTimeSeries-button').addEventListener('click', function () {
-        // calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].yts = calc_constants.changeYTimeSeries;
-        // Added by Codex: Convert displayed lon/lat input to lower-left-relative model offset for spherical grids.
-        calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].yts = timeSeriesDisplayToOffsetY(calc_constants.changeYTimeSeries);
-        syncTimeSeriesInputsFromSelectedLocation();
+        calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].yts = calc_constants.changeYTimeSeries;
         calc_constants.updateTimeSeriesTx = 1;  // by setting to one, will tell timesereies shader to run
     });
     document.getElementById('NumberOfTimeSeries-select').addEventListener('change', function () {
         calc_constants.chartDataUpdate = 1;  // Indicate that the number of time series changed, need to update chart legends, etc.
     });
 
-    // CODEX: Linear-structure endpoint UI listeners store all endpoint state in calc_constants.
-    document.getElementById('designcomponent_xLoc-button').addEventListener('click', function () {
-        storeLinearStructureEndpointFromInputs();
-    });
-    document.getElementById('designcomponent_yLoc-button').addEventListener('click', function () {
-        storeLinearStructureEndpointFromInputs();
-    });
-    document.getElementById('designcomponent_CurrentEndPoint-select').addEventListener('change', function () {
-        loadLinearStructureEndpointIntoInputs();
-    });
-    document.getElementById('linearstructure-button').addEventListener('click', function () {
-        // CODEX: Future bathy/topo modification should run before this reset.
-        // resetLinearStructureEndpoints();
-        // CODEX: Request the GPU bathy/topo edit; the frame loop resets endpoints after copy-back and refresh.
-        requestAddLinearStructure();
-    });
-    updateLinearStructureLocationsDisplay();
-
     // add remove scroll wheel functionality
-    // document.getElementById('viewType-select').addEventListener('change', function () {
-    //     updateZoomListener(); // Ensure the listener state matches the new viewType
-    // });
-    // CODEX: Blur the view selector after changing modes so Explorer WASD shortcuts reach the document handler.
-    document.getElementById('viewType-select').addEventListener('change', function (event) {
+    document.getElementById('viewType-select').addEventListener('change', function () {
         updateZoomListener(); // Ensure the listener state matches the new viewType
-        event.target.blur();
     });
```

#### CT1-334 중첩 출력 시작 버튼

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5239; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3216; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 nestedGridOutput_trigger=1을 설정한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 5242행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -5239,13 +3216,6 @@
         calc_constants.writesurfaces = 0;  // stop writing 2D data to file
     });
 
-    // Added by Codex: Start nested-grid boundary time-series output button.
-    document.getElementById('startNestedGridOutput-button').addEventListener('click', function () {
-        calc_constants.nestedGridOutput_trigger = 1;
-        console.log('Nested-grid boundary time-series output requested.');
-    });
-    // Added by Codex: End nested-grid boundary time-series output button.
-
     // start simulation
 
     // Ensure to bind this function to your button's 'click' event in the HTML or here in the JS.
```

#### CT1-335 시작 시 선택 파일

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5273; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3243; 아래 전체 diff의 +행 | 불일치 (A) | 본판만 초기 수면·hardbottom·4변 시계열 파일을 읽는다. transect 판은 config·bathy·waves·friction·overlay·model 파일을 읽는다. |

본판 차이 줄의 마지막 수정: `32be94a` 2025-10-16 (현재 5276행 포함); `b8b50c3` 2025-06-08 (현재 5278행 포함); `bb99fee` 2026-07-02 (현재 5281행 포함). transect 차이 줄의 마지막 수정: 추가·삭제 줄 없음.

```diff
@@ -5273,17 +3243,9 @@
         var configFile = document.getElementById('configFile').files[0];
         var bathymetryFile = document.getElementById('bathymetryFile').files[0];
         var waveFile = document.getElementById('waveFile').files[0];
-        var etaInitialConditionFile = document.getElementById('etaInitialConditionFile').files[0];
         var frictionFile = document.getElementById('frictionmapFile').files[0];
-        var hardbottomFile = document.getElementById('hardbottomFile').files[0];
         var OverlayFile = document.getElementById('satimageFile').files[0];
         var modelFile = document.getElementById('modelFile').files[0];
-        // Added by Codex: Start optional boundary time-series upload files.
-        var westBoundaryTimeSeriesFile = document.getElementById('westBoundaryTimeSeriesFile').files[0];
-        var eastBoundaryTimeSeriesFile = document.getElementById('eastBoundaryTimeSeriesFile').files[0];
-        var southBoundaryTimeSeriesFile = document.getElementById('southBoundaryTimeSeriesFile').files[0];
-        var northBoundaryTimeSeriesFile = document.getElementById('northBoundaryTimeSeriesFile').files[0];
-        // Added by Codex: End optional boundary time-series upload files.
     
         // Check if the required files are not uploaded
         if (!configFile || !bathymetryFile) {
```

#### CT1-336 기본 파랑 파일 경로와 마찰 누락

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5309; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3271; 아래 전체 diff의 +행 | 불일치 (E) | transect 판은 파랑 파일 미지정 시 /no_waves.txt를 fetch한다. 단면 reader는 3*HEIGHT행을 기대한다. 일반 no_waves.txt 형식은 그 계약과 다르다. 이 호출은 이미 읽은 frictionFile도 전달하지 않는다. 업로드 파랑 경로와 자기 함수 인자 계약이 모순한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 5312행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 3274행 포함).

```diff
@@ -5309,9 +3271,7 @@
                     fetch('/no_waves.txt')
                         .then(response => response.text())
                         .then(defaultWaveContent => {
-                            // startSimulationWithWave(configContent, bathymetryContent, defaultWaveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile);
-                            // Added by Codex: Pass optional boundary time-series files with custom startup.
-                            startSimulationWithWave(configContent, bathymetryContent, defaultWaveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile);
+                            startSimulationWithWave(configContent, bathymetryContent, defaultWaveContent, OverlayFile, modelFile);
                         })
                         .catch(error => {
                             console.error("Failed to load the default wave file:", error);
```

#### CT1-337 업로드 파랑 시작 인자

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5319; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3279; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 실제 파랑 업로드 경로에서 frictionFile을 전달한다. 본판은 초기 수면·hardbottom·4변 시계열 파일도 전달한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 5322행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 3282행 포함).

```diff
@@ -5319,9 +3279,7 @@
                 } else {
                     waveReader.onload = function (e) {
                         var waveContent = e.target.result;
-                        // startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile);
-                        // Added by Codex: Pass optional boundary time-series files with custom startup.
-                        startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile);
+                        startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile);
                     };
                     waveReader.readAsText(waveFile);
                 }
```

#### CT1-338 시작 함수 인자 목록

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5333; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3291; 아래 전체 diff의 +행 | 불일치 (A) | transect 판의 시작 함수는 6인자다. 본판은 추가 입력 파일을 포함한 13인자다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 5336행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 3294행 포함).

```diff
@@ -5333,9 +3291,7 @@
         configReader.readAsText(configFile);
     }
     
-    // function startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile) {
-    // Added by Codex: Optional boundary time-series upload files flow into initializeWebGPUApp.
-    function startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile) {
+    function startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile) {
         // Here you could do the actual simulation initialization
     //    console.log("Starting simulation with the following data:");
     //    console.log("Config:", configContent);
```

#### CT1-339 초기화 호출과 자동 시작

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5344; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3300; 아래 전체 diff의 +행 | 불일치 (A) | transect 판은 6인자를 초기화에 전달한다. 본판만 URL 케이스 자동 시작 뒤 5000ms 후 UI를 갱신한다. |

본판 차이 줄의 마지막 수정: `bb99fee` 2026-07-02 (현재 5347행 포함); `98f41c9` 2024-04-18 (현재 5353행 포함); `f6fd78b` 2026-06-04 (현재 5354행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 3303행 포함).

```diff
@@ -5344,19 +3300,11 @@
     //    console.log("Overlay:", OverlayFile);
     
         // Initialize your WebGPU application here
-        // initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile).catch(error => {
-        // Added by Codex: Pass optional boundary time-series upload files to initialization.
-        initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile).catch(error => {
+        initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile).catch(error => {
              console.error("Initialization failed:", error);
         });
     }
-
-    loadAgentCaseFromUrl().then(function (started) {
-        if (started) {
-            const delay = 5000;
-            setTimeout(updateAllUIElements, delay);
-        }
-    });
+    
 
 });
 // end web GUI code
```

#### CT1-340 시계열 수 0일 때 chart 갱신

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5456; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3404; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 NumberOfTimeSeries>0일 때만 기존 dataset을 갱신한다. transect 판은 무조건 else로 들어간다. 내부 timeSeriesData[index] 검사 때문에 이 차이만으로 잘못된 접근을 확정하지 않는다. 이 guard 변경은 ebca435의 epoch 수정과 구분한다. |

본판 차이 줄의 마지막 수정: `dee0e14` 2026-02-04 (현재 5459행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 3407행 포함).

```diff
@@ -5456,7 +3404,7 @@
         // Apply the new datasets to the chart
         timeseriesChart.data.datasets = newDatasets;
         calc_constants.chartDataUpdate = 0; // Reset the update flag
-    } else if (calc_constants.NumberOfTimeSeries > 0) {
+    } else {
         // If no new datasets but data might have been updated
         timeseriesChart.data.datasets.forEach((dataset, index) => {
             if(timeSeriesData[index]) { // Ensure there's corresponding data
```

#### CT1-341 chart 시간축

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5467; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3415; 아래 전체 diff의 +행 | 불일치 (A) | 본판은 시작 시각부터 시작 시각+기간까지 표시한다. transect 판은 최대값만 maxdurationTimeSeries로 둔다. 일반 0기반 실행에서는 같은 창이다. |

본판 차이 줄의 마지막 수정: `ebca435` 2026-07-20 (현재 5470행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 3418행 포함).

```diff
@@ -5467,12 +3415,7 @@
 
     // Always update the labels and x-axis limit to reflect any changes in the time vector or chart configuration
     timeseriesChart.data.labels = timeSeriesData[0].time;
-    // timeseriesChart.options.scales.x.max = calc_constants.maxdurationTimeSeries;
-    // Added by Codex: Start ordinary windows remain 0..duration; nested windows
-    // retain absolute parent/global timestamps and move after each reset.
-    timeseriesChart.options.scales.x.min = calc_constants.timeSeriesChartStartTime;
-    timeseriesChart.options.scales.x.max = calc_constants.timeSeriesChartStartTime + calc_constants.maxdurationTimeSeries;
-    // Added by Codex: End point time-series chart-window limits.
+    timeseriesChart.options.scales.x.max = calc_constants.maxdurationTimeSeries;
 
     // Dynamically adjust the stepSize if needed
     const desiredNumberOfTicks = 20; // Example: aim for 10 ticks
```

#### CT1-342 chart update await

| 문서 위치·원문 | 코드 위치·원문 | 판정 | 이유 |
|---|---|---|---|
| ebca435:js/main.js:5481; 아래 전체 diff의 -행 | ebca435:transect_version/js/main.js:3424; 아래 전체 diff의 +행 | 불일치 (F) | transect 판은 timeseriesChart.update()를 await한다. 동기 update의 결과를 기다리는 문법 차이는 기록 자료 값을 바꾸지 않는다. 마지막 빈 줄도 다르다. |

본판 차이 줄의 마지막 수정: `dee0e14` 2026-02-04 (현재 5484행 포함); `7793a7e` 2026-02-11 (현재 5489행 포함). transect 차이 줄의 마지막 수정: `22e1983` 2025-06-06 (현재 3427행 포함).

```diff
@@ -5481,9 +3424,8 @@
     timeseriesChart.options.scales.x.ticks.stepSize = stepSize;
 
     // Update the chart to apply changes
-    timeseriesChart.update();
+    await timeseriesChart.update();
 }
 
 // Set an interval to update the chart every second (1000 milliseconds)
 setInterval(updateChartData, 1000);
-
```


### 2.49 한쪽 판에만 있는 파일

이 목록은 같은 이름 경로의 존재 여부로 판정한다.
이름이 다른 고차 flux 파일은 역할과 이력을 함께 연결한다.
`--follow`가 찾은 이전 이름의 이력과 현재 이름 경로의 최초 추가 날짜를 구분한다.
아래 최초 추가는 `git log --diff-filter=A -- 현재경로`로 보조 확인했다.

| 행 ID | 판·파일 | 역할·현재 호출 | 최초 추가 HASH·날짜 | 원문 인용 | 판정 |
|---|---|---|---|---|---|
| CT1-343 | 본판 `js/Handler_ExtractNestedBoundaryTimeSeries.js` | 중첩 경계 추출의 uniform·상태·4변 출력·바닥고 바인딩을 만든다. main.js가 파이프라인을 생성하므로 본판에서 호출한다. | bb99fee 2026-07-02 Added grid nesting | `ebca435:js/Handler_ExtractNestedBoundaryTimeSeries.js:3` `// Added by Codex: Start nested-grid boundary time-series extraction handler.` | A |
| CT1-344 | 본판 `js/Wave_Generator.js` | Sine와 TMA 파 성분을 생성한다. H는 0.5배 진폭으로 바꾼다. TMA는 주파수 100개·방향 간격 5도·방향 반폭 20도·gamma 3.3·spread 50·절단비 0.01을 쓴다. 에너지는 4.004 계수로 입력 파고에 맞춘다. 횡방향 주기 경계일 때 방향을 경계 파수에 맞춘다. 임의 위상은 [0,2π)다. 4096 성분 용량과 계산 결과 캐시를 제공한다. | 9093d7f 2026-06-01 added ability to change wave conditions through the UI - on the Modify Boundary Conditions Panel | `ebca435:js/Wave_Generator.js:44` `export function buildSineWaveData(calc_constants) {` | A |
| CT1-345 | 본판 `js/agent_controls.js` | 브라우저의 수치 상태·표시·경계·퇴적물·측정점·설계·예제·전체화면 제어 API를 노출한다. applyCommand/applyCommands/getState와 postMessage 입출력을 제공한다. CelerisAgent 폴더의 내부 구현은 범위 밖이다. | 0ee5174 2026-06-18 CelerisAgent initial commit | `ebca435:js/agent_controls.js:820` `window.CelerisAgentControls = {` | A |
| CT1-346 | 본판 `shaders/ExtractNestedBoundaryTimeSeries.wgsl` | 직사각형 4변의 eta/hu/hv를 관측점×표본시각 텍스처로 쓴다. workgroup은 16×1이다. 수심<=0이면 0.0을 쓴다. 자료는 child 경계 type 5로 재입력한다. | bb99fee 2026-07-02 Added grid nesting | `ebca435:shaders/ExtractNestedBoundaryTimeSeries.wgsl:23` `fn LoadState(i: i32, j: i32) -> vec4<f32> {` | A |
| CT1-347 | transect `shaders/Pass2_HighOrder.wgsl` | transect 고차 모드의 활성 x HLLEM flux다. near-dry에서 DU.x를 0으로 만든다. y flux와 횡운동량을 생략한다. 퇴적물 4개 채널의 x flux는 NumericalFlux로 쓴다. phix=1.0이다. 본판은 같은 이름 파일을 2025-11-07에 HLLC/HLLEM 이름으로 분리했다. | 22e1983 2025-06-06 Sediment transport updates and transect model beta | `ebca435:transect_version/shaders/Pass2_HighOrder.wgsl:191` `xflux = HLLEM_Flux(aplus, aminus, Fp_x, Fm_x, state_plus_x, state_minus_x, DU_flag);` | C |
| CT1-348 | 본판 `shaders/Pass2_HighOrder_HLLC.wgsl` | 본판 고차 모드의 활성 HLLC 이름 파일이다. Roe 평균·star 상태·HLL 혼합을 계산한다. x·y 두 flux를 저장한다. 퇴적물 배경·쇄파 확산 항도 받는다. main.js:1548이 이 파일을 fetch한다. | 19b63cf 2025-11-07 convert Pass2 High-order to HLLC | `ebca435:shaders/Pass2_HighOrder_HLLC.wgsl:71` `fn HLLC_Flux(` | A |
| CT1-349 | 본판 `shaders/Pass2_HighOrder_HLLEM.wgsl` | 본판에 보존한 HLLEM flux 대안이다. 현재 main.js에는 이 경로를 fetch하는 줄이 없다. transect 고차 파일은 이 계열을 1D로 줄인 것이다. | 19b63cf 2025-11-07 convert Pass2 High-order to HLLC | `ebca435:shaders/Pass2_HighOrder_HLLEM.wgsl:76` `/ denom;` | A |
| CT1-350 | 본판 `shaders/Pass3_NLSW_Spherical.wgsl` | 본판의 구면 NLSW source와 시간적분이다. 경위도 도를 radian 차분으로 바꾼다. 위도 cos 면가중 flux·압력·곡률·Coriolis를 더한다. mode와 계량 바인딩은 main.js의 grid_type==2 분기가 선택한다. | afc1fe7 2026-06-19 Added Spherical NLSW Solver, Japan 2011 example | `ebca435:shaders/Pass3_NLSW_Spherical.wgsl:217` `let spherical_flux_divergence = (` | A |
| CT1-351 | 본판 `shaders/SedTrans_Pass3_old.wgsl` | 본판의 구판 퇴적물 적분이다. 면농도 평균·면속도·hardbottom·픽업·침강을 사용한다. 현재 main.js가 fetch하지 않는다. 활성 SedTrans_Pass3와 같은 판으로 섞어 설명하면 안 된다. | a98bcc4 2025-06-09 sed trans updates | `ebca435:shaders/SedTrans_Pass3_old.wgsl:154` `let source_term = erosion - deposition;` | A |
| CT1-352 | 본판 `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | 부유사와 bedload 지형변화를 한 패스에서 함께 시간적분하려는 실험본이다. 전역 oldGradients_Sed·oldOldGradients_Sed·predictedGradients_Sed를 각각 두 번 선언한다. 선언하지 않은 txBedState_Sed·txOldBedGradients_Sed·txOldOldBedGradients_Sed를 읽는다. .x를 취해 f32가 된 Bed_state_here에 다시 .x를 쓴다. 현재 실행 경로에서 호출되지 않음. main.js의 fetch 목록은 활성 SedTrans_Pass3와 SedTrans_UpdateBottom만 선택한다. 정적 오류 근거 강함. | 852ec28 2025-06-13 sed trans fixes | `ebca435:shaders/SedTrans_Pass3_wBedUpdate.wgsl:235` `newBed.x = Bed_state_here.x + globals.dt * d_by_dt_Bed;` | E |
| CT1-353 | 본판 `shaders/SedTrans_UpdateBottom_testing.wgsl` | 지형변화의 시간 적산과 주기적 갱신을 시험한 본판 파일이다. 현재 코드는 B_initial을 그대로 출력한다. 지형 되먹임과 최근 누적량 갱신은 주석이다. 현재 main.js가 fetch하지 않는다. | 4353b85 2025-06-09 Sed bugs / corrections | `ebca435:shaders/SedTrans_UpdateBottom_testing.wgsl:77` `let B_here = B_initial; // + dB_cumulative;` | A |
| CT1-354 | 본판 `shaders/fragment_testing.wgsl` | 색상·수면·파고·퇴적물·설계·화살표·측정점·범례를 합성하는 본판의 보존 표시 실험본이다. 현재 main.js는 fragment.wgsl을 fetch한다. 이 실험본은 현재 실행 경로에서 호출되지 않는다. | f183cc2 2026-02-01 Added ability for user to specify initial 3D camera position | `ebca435:shaders/fragment_testing.wgsl:864` `out.color = vec4<f32>(color_rgb, 1.0); // Normal shader output` | A |


전용 파일별 `git log --follow -p`의 최근 이력은 다음과 같다.

| 파일 | HASH | 날짜 | 메시지 |
|---|---|---|---|
| `js/Handler_ExtractNestedBoundaryTimeSeries.js` | `bb99fee` | 2026-07-02 | Added grid nesting |
| `js/Wave_Generator.js` | `0ee5174` | 2026-06-18 | CelerisAgent initial commit |
| `js/Wave_Generator.js` | `9093d7f` | 2026-06-01 | added ability to change wave conditions through the UI - on the Modify Boundary Conditions Panel |
| `js/agent_controls.js` | `0ee5174` | 2026-06-18 | CelerisAgent initial commit |
| `shaders/ExtractNestedBoundaryTimeSeries.wgsl` | `bb99fee` | 2026-07-02 | Added grid nesting |
| `transect_version/shaders/Pass2_HighOrder.wgsl` | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |
| `shaders/Pass2_HighOrder_HLLC.wgsl` | `19b63cf` | 2025-11-07 | convert Pass2 High-order to HLLC |
| `shaders/Pass2_HighOrder_HLLC.wgsl` | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| `shaders/Pass2_HighOrder_HLLC.wgsl` | `fa47b72` | 2025-06-06 | Sed Trans Updates |
| `shaders/Pass2_HighOrder_HLLEM.wgsl` | `19b63cf` | 2025-11-07 | convert Pass2 High-order to HLLC |
| `shaders/Pass2_HighOrder_HLLEM.wgsl` | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| `shaders/Pass2_HighOrder_HLLEM.wgsl` | `fa47b72` | 2025-06-06 | Sed Trans Updates |
| `shaders/Pass3_NLSW_Spherical.wgsl` | `afc1fe7` | 2026-06-19 | Added Spherical NLSW Solver, Japan 2011 example |
| `shaders/Pass3_NLSW_Spherical.wgsl` | `35b7f1c` | 2026-01-15 | addition of vorticity-based momentum mixing |
| `shaders/SedTrans_Pass3_old.wgsl` | `a98bcc4` | 2025-06-09 | sed trans updates |
| `shaders/SedTrans_Pass3_old.wgsl` | `e54def4` | 2025-06-08 | Update SedTrans_Pass3.wgsl |
| `shaders/SedTrans_Pass3_old.wgsl` | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| `shaders/SedTrans_Pass3_old.wgsl` | `2a7452d` | 2025-06-07 | Sed Trans updates |
| `shaders/SedTrans_Pass3_old.wgsl` | `5c60ac0` | 2025-06-07 | add sediment diffusion term |
| `shaders/SedTrans_Pass3_old.wgsl` | `a435dd4` | 2025-06-07 | Update SedTrans_Pass3.wgsl |
| `shaders/SedTrans_Pass3_old.wgsl` | `fa47b72` | 2025-06-06 | Sed Trans Updates |
| `shaders/SedTrans_Pass3_old.wgsl` | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |
| `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | `852ec28` | 2025-06-13 | sed trans fixes |
| `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | `ba9eb67` | 2025-06-09 | added bedload to bottom update equation |
| `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | `e54def4` | 2025-06-08 | Update SedTrans_Pass3.wgsl |
| `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | `b8b50c3` | 2025-06-08 | Sed Trans Updates |
| `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | `2a7452d` | 2025-06-07 | Sed Trans updates |
| `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | `5c60ac0` | 2025-06-07 | add sediment diffusion term |
| `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | `a435dd4` | 2025-06-07 | Update SedTrans_Pass3.wgsl |
| `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | `fa47b72` | 2025-06-06 | Sed Trans Updates |
| `shaders/SedTrans_Pass3_wBedUpdate.wgsl` | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |
| `shaders/SedTrans_UpdateBottom_testing.wgsl` | `4353b85` | 2025-06-09 | Sed bugs / corrections |
| `shaders/SedTrans_UpdateBottom_testing.wgsl` | `a98bcc4` | 2025-06-09 | sed trans updates |
| `shaders/SedTrans_UpdateBottom_testing.wgsl` | `22e1983` | 2025-06-06 | Sediment transport updates and transect model beta |
| `shaders/fragment_testing.wgsl` | `f183cc2` | 2026-02-01 | Added ability for user to specify initial 3D camera position |
| `shaders/fragment_testing.wgsl` | `d23dfb0` | 2025-09-01 | Small fixes |
| `shaders/fragment_testing.wgsl` | `8c2b62b` | 2025-08-24 | Added Tracy Arm Example, some landslide viz additions |
| `shaders/fragment_testing.wgsl` | `3d8a61b` | 2025-06-14 | Added many-transect version |
| `shaders/fragment_testing.wgsl` | `7fa28e0` | 2025-06-12 | bug fixes |
| `shaders/fragment_testing.wgsl` | `3be651a` | 2025-06-11 | small fixes |
| `shaders/fragment_testing.wgsl` | `b8b50c3` | 2025-06-08 | Sed Trans Updates |

같은 내용 파일의 마지막 변경과 복제 이력은 다음과 같다.

| 파일 | 본판 마지막 변경 | transect 마지막 변경 | 내용 판정 |
|---|---|---|---|
| `js/Config_Pipelines.js` | e90945e 2025-05-05 loading box config file; initial attempts to integrate igTL models | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Create_Textures.js` | 4fa700a 2025-05-31 Display updates - added mean vorticity to display options | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_CalcWaveHeight.js` | 0e8b502 2023-10-31 Add files via upload | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_Model.js` | e90945e 2025-05-05 loading box config file; initial attempts to integrate igTL models | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_MouseClickChange.js` | 98f41c9 2024-04-18 Photo-realism update | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_Pass0.js` | ebc98a5 2024-03-13 Add files via upload | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_Pass1.js` | 63a12e3 2023-10-19 Add files via upload | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_Pass3.js` | 67ca57c 2025-05-22 Added COULWAVE solver | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_PassBreaking.js` | 366ee34 2024-04-08 photorealism update | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_SedTrans_Pass1.js` | 85c2ca2 2024-03-19 Add files via upload | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_Skybox.js` | 30be4e9 2025-04-29 added skybox | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_Tridiag.js` | 67ca57c 2025-05-22 Added COULWAVE solver | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_UpdateTrid.js` | 63a12e3 2023-10-19 Add files via upload | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Handler_Updateneardry.js` | 85c2ca2 2024-03-19 Add files via upload | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/Model_Loaders.js` | e90945e 2025-05-05 loading box config file; initial attempts to integrate igTL models | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `js/site.js` | 63a12e3 2023-10-19 Add files via upload | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `shaders/CalcWaveHeight.wgsl` | 0e8b502 2023-10-31 Add files via upload | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `shaders/Ship_pressure.compute` | 63a12e3 2023-10-19 Add files via upload | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |
| `shaders/vertex.wgsl` | 63a12e3 2023-10-19 Add files via upload | 22e1983 2025-06-06 Sediment transport updates and transect model beta | 일치. CR 차이는 2.1의 F 행. |

### 2.50 E 판정의 반대 근거와 근거 강도

이 절은 같은 결함 후보를 가리키는 여러 diff 행을 묶는다.
묶음 수와 E 행 수는 다르다.
E 행은 코드 수정안을 뜻하지 않는다.
강도는 정적 원문 대조의 강도다.

#### CT1-057 측정점 행 정렬

반대 근거 확인: 기본 maxNumberOfTimeSeries=16이면 256바이트라 문제가 나타나지 않는다. 이 반대 근거를 반영해 비기본 개수 조건으로 제한한다.

확인한 모순: 자기 주석은 행 길이를 256배수로 요구한다. transect 실제 requiredBytesPerRow는 N*16이다. 본판은 ca9278e에서 정렬식을 수정했다. 16의 배수가 아닌 N에서 세 근거가 어긋난다.

근거 강도: 약함. 같은 판의 16*N 입력 사전조건을 반영한다.

#### CT1-087·CT1-266 지도 실패 처리

반대 근거 확인: 성공한 HTTP 이미지에서는 결과가 같을 수 있다. 지도 실패 시 시뮬레이션을 중단하려는 의도 변경 근거는 찾지 못했다.

확인한 모순: transect File_Loader는 onerror를 처리하지 않는다. main catch는 GoogleMapOverlay==0을 비교만 한다. 본판은 bf8db50에서 reject와 =0 대입을 함께 고쳤다.

근거 강도: 강함.

#### CT1-088·CT1-089·CT1-090·CT1-091·CT1-092·CT1-120·CT1-123 readback 버퍼 수명

반대 근거 확인: JS 객체 수거가 결국 리소스를 회수할 수 있다. 정적 검토만으로 영구 누수를 확정하지 않는다. 업로드 버퍼 정리 151017f는 두 판에 들어갔으므로 업로드까지 같은 결함으로 확대하지 않는다.

확인한 모순: transect readback은 함수마다 버퍼를 생성한다. 해당 함수들의 명시적 destroy가 없다. 같은 판 업로드 함수는 submit 뒤 destroy한다. 본판 dee0e14·b24af89·09cfd76은 정리와 버퍼 재사용을 추가했다. 결과 자료를 별도 배열로 복사하므로 readback 버퍼를 유지할 필요가 없는 경로가 있다.

근거 강도: 중간.

#### CT1-097·CT1-098·CT1-144·CT1-149·CT1-281 교란과 누적 침식의 결합

반대 근거 확인: transect HTML의 no feedback 안내와 B_here=B_here는 물리 바닥고를 고정한다. 따라서 진단 누적량을 실제 바닥고에 더하지 않는 현재 beta 경로에는 타당한 반대 근거가 있다.

확인한 모순: 본판 4353b85는 Sed bugs / corrections라는 메시지와 함께 txBotChange_Sed를 교란 기준 지형에 더했다. transect 판에는 그 바인딩과 덧셈이 없다. 한쪽만 수정한 결함은 E로 두라는 지시에 따라 E로 유지한다. 다만 현재 beta의 동작 오류를 확정하지 않는다. 실제 지형 되먹임을 연결하거나 진단 누적량을 교란과 결합할 때 재검토할 항목이다.

근거 강도: 약함.

#### CT1-122·CT1-311 비동기 시계열 초기화

반대 근거 확인: ebca435 메시지는 중첩 기능을 넣으면서 발생한 결함을 명시한다. transect 판에는 중첩 시계열이 없다. 따라서 절대 시각 회귀가 transect 판에도 발생한다고 쓰지 않는다.

확인한 모순: 두 판은 비동기 readback을 await하지 않고 시작한다. transect 판은 읽기 완료 뒤 reset하고 UI flag가 유지되는 동안 reset 요청을 반복한다. 본판은 동기 reset과 epoch 검사를 쓴다. 일반 실행에서도 늦은 readback의 reset 순서는 따로 점검할 필요가 있다. ebca435는 본판만 수정했다.

근거 강도: 중간.

#### CT1-140 사면 체적 계수

반대 근거 확인: 7ae7da4는 volume fix라고 명시하지만 Gaussian 교란 함수는 그 커밋에서 바뀌지 않았다. transect 표시가 항상 4배 과대라고 결론내리지 않는다.

확인한 모순: 두 판의 landslide_subaerial은 theta=0·bottom<=0인 무한 영역에서 thickness*exp(-π*x²/L²)*exp(-π*y²/W²)를 준다. 해석: 이 식의 면적분은 π를 정확히 쓸 때 thickness*L*W다. 본판 표시만 0.25배다. 현재 본판의 표시 계수와 교란 함수도 모순할 수 있다. 유한 영역·양의 bottom 조건에서는 이 적분값을 그대로 적용하지 않는다.

근거 강도: 중간.

#### CT1-141 로그 DOM 증가

반대 근거 확인: 단회 로그에는 영향이 작다. 본판의 200개 제한은 출력 자료의 물리 의미를 바꾸지 않는다.

확인한 모순: 매 프레임 상태 갱신은 DOM에 entry를 추가한다. transect 판에는 오래된 entry 제거가 없다. 본판 dee0e14의 clean up memory leaks는 200개 제한을 추가했다. 같은 판의 일반 표시 함수가 container.innerHTML을 비우는 경로와도 자원 수명이 다르다.

근거 강도: 중간.

#### CT1-183 COULWAVE u 평균

반대 근거 확인: Pass3A 주석은 셀 운동량에서 직접 속도를 얻는 대안을 좋지 않다고 명시한다. 이 반대 근거는 면속도 사용을 지지한다. 이 주석은 1D에서 분모 4를 유지할 근거가 아니다.

확인한 모순: Pass1은 북·남 u 채널을 0으로 쓴다. Pass3A는 네 채널 합을 4로 나눈다. 같은 판 CalcMeans는 동·서 두 채널 합을 2로 나눈다. x 면속도 U가 일정하면 두 값은 U/2와 U다. main.js는 mode 2에서 Pass3A를 매 예측·수정 단계에 호출한다. 22e1983 원문부터 이 조합이 존재한다.

근거 강도: 강함.

#### CT1-196 Boussinesq Psi2x 누락

반대 근거 확인: 1D에서 y 미분과 교차 F/G 항을 지우는 것은 타당하다. 그러나 d_x*eta_xx는 그 가정에서 0이 아니다. 이를 다른 source나 PCR에서 보정한다는 코드와 의도 변경 메시지는 찾지 못했다.

확인한 모순: transect는 Psi2x를 실제 계산한다. 바로 위 주석과 본판 source는 Psi1x+Psi2x를 더한다. transect source는 Psi1x만 더한다. PCR 계수에는 eta_xx가 없다. 22e1983:transect_version/shaders/Pass3_Bous.wgsl:287과 :386에 이미 이 차이가 있다.

근거 강도: 강함.

#### CT1-224·CT1-225 퇴적물 수심 정규화와 단면 간 확산

반대 근거 확인: HTML은 수리 되먹임이 없다고 명시한다. 이는 바닥고를 고정할 근거다. 이 안내는 농도가 다른 y 단면으로 확산하거나 hu에서 속도를 얻는 단위를 바꿀 근거가 아니다. 기본 useSedTransModel=0에서는 이 경로를 dispatch하지 않는다.

확인한 모순: transect의 역수심 식은 젖은 h에서 sqrt(2)가 된다. hu*divide_by_h는 m/s가 아니라 운동량 flux의 단위를 유지한다. 같은 판 수리 마찰 함수와 본판 퇴적물 함수는 역수심을 사용한다. Dyy=Dxy=1은 독립 단면 전제와 x 전용 Pass2에 모순한다. 퇴적물 Pass3는 바깥 두 y행을 건조 경계처럼 지우지만 수리 Pass3는 모든 단면 행을 계산한다. 본판 4353b85·a98bcc4·ba9eb67의 후속 수정과 별개로 22e1983부터 정규화·y 결합 문제를 확인한다. 농도 비음수 제한은 BoundaryPass에도 있어 일부 보정한다. 이 반대 경로 때문에 비음수 clamp 부재만으로 별도 강한 결함을 세지 않는다.

근거 강도: 강함.

#### CT1-239 near-dry 차단 불일치

반대 근거 확인: transect가 near_dry=d_here를 명시적으로 대입한 흔적은 있다. 그러나 명시 분산 source와 암시 계수를 다르게 차단하려는 이유는 없다. COULWAVE 전용 계수 경로까지 이 결함으로 확대하지 않는다.

확인한 모순: transect Update_TriDiag_coef:34는 d_here를 쓴다. 같은 판 Pass3_Bous:160은 txBottom.w를 읽고 :194에서 >0을 검사한다. CPU/GPU near-dry 갱신은 x ±3칸에 양의 지형이 있으면 w=-99로 둔다. 따라서 잠긴 해안 인접 셀에서 source는 꺼지고 비항등 PCR 계수는 남을 수 있다.

근거 강도: 중간.

#### CT1-285 NLSW 초기화의 null 셰이더

반대 근거 확인: NLSW 적분 dispatch 자체는 mode 0용 파이프라인을 선택한다. 그러나 초기화가 그 dispatch보다 먼저 Bous 파이프라인을 무조건 생성한다. 기본 mode 1로만 실행하면 이 조건은 드러나지 않는다.

확인한 모순: transect main:1050은 Bous 코드를 null로 둔다. :1051–1058은 mode 1/2에서만 대입한다. :1112는 무조건 createComputePipeline에 전달한다. 같은 판 Config_Pipelines:10은 그 값을 createShaderModule의 code에 쓴다. 본판은 Bous 파일을 먼저 fetch한다.

근거 강도: 강함.

#### CT1-286·CT1-304 프레임마다 파이프라인 재생성

반대 근거 확인: 그림의 수학적 값은 같을 수 있다. 실행 성능과 메모리 사용을 측정하지 않았다.

확인한 모순: transect는 초기 생성 후에도 매 프레임 같은 shader/layout으로 createRenderPipeline을 부른다. 본판 08860f0는 Reduced createRenderPipeline calls를 명시하며 미리 만든 두 파이프라인을 재사용한다. 같은 렌더 경로의 초기 객체와 매 프레임 객체가 중복된다는 근거를 함께 둔다.

근거 강도: 중간.

#### CT1-287 중복 마지막 strip과 vertex 개수

반대 근거 확인: transect의 원래 y 루프가 이미 마지막 줄을 포함한다. 고정 개수 때문에 원래 마지막 줄이 모두 빠진다고 단정할 수 없다.

확인한 모순: 마지막 strip 추가 코드와 numVertices=2*H*W는 실제 vertices.length/2와 다르다. 본판 c3c57a4의 fix last row vertex configuration to remove bottom pixel strand는 마지막 strip 추가를 지우고 실제 길이를 사용했다. H>1인 정적 계산에서 실제 개수는 2*W*H+2*H-3이다.

근거 강도: 중간.

#### CT1-296·CT1-297 overlay 전환 인자 불일치

반대 근거 확인: 초기 RenderBindGroup 생성은 transect에서도 현재 인자 목록과 맞는다. 따라서 초기 표시 전체의 결함으로 확대하지 않는다. 문제는 overlay 전환 경로에 한정한다.

확인한 모순: transect Handler_Render:179는 txDesignComponents·txOverlayMap·txDraw·sampler·측정점·쇄파·영상·선형 sampler·f16를 순서대로 요구한다. main:1417와 :1428은 구 인자 목록을 전달한다. 함수 본문은 잘못 전달된 sampler에 createView를 호출할 수 있다. 본판 bf8db50:js/main.js:1530과 :1543은 전체 목록으로 수정했다.

근거 강도: 강함.

#### CT1-299 편집 뒤 near-dry 갱신

반대 근거 확인: COULWAVE는 매 스텝 비선형 계수를 다시 만든다. 따라서 계수 자체가 영원히 고정된다는 주장은 하지 않는다.

확인한 모순: transect는 지형 편집 후 near-dry 갱신을 mode==1 블록 안에 둔다. mode 2의 명시 source는 txBottom.w를 사용한다. 본판은 near-dry를 모드 조건 밖으로 옮기고 계수 갱신은 >=1로 넓혔다. mode 2의 계수 재계산만으로 w가 새 지형을 반영하지는 않는다.

근거 강도: 중간.

#### CT1-316·CT1-323 포인터와 표시 영역

반대 근거 확인: canvas 표시 비율이 내부 비율과 같아 여백이 없으면 좌표 식은 같다.

확인한 모순: transect는 외곽 getBoundingClientRect 전체를 모델 영역으로 환산한다. 본판은 object-fit 여백과 objectPosition을 반영한다. 같은 canvas의 격자 표시와 좌표 입력이 여백 조건에서 어긋난다. 본판 0ee5174에 추가된 좌표 보정을 확인한다.

근거 강도: 중간.

#### CT1-322 폼 입력과 카메라 이동

반대 근거 확인: Explorer 모드에서 폼에 초점이 없을 때 WASD 이동은 의도된 기능이다.

확인한 모순: transect의 keydown은 viewType과 입력 대상을 검사하지 않고 shift_x/shift_y를 갱신한다. 같은 판에는 수치 input·select 입력이 존재한다. 본판은 폼 편집과 비 Explorer 상태를 먼저 배제한다. 물리 매개변수 입력과 카메라 조작 경로가 간섭하는 한쪽 수정이다.

근거 강도: 중간.

#### CT1-336 기본 no_waves와 friction 인자

반대 근거 확인: 단면 형식 파랑 파일을 실제 업로드하면 이 분기 대신 6인자 호출을 사용한다. 따라서 정상 업로드 실행이 모두 실패한다고 쓰지 않는다.

확인한 모순: 일반 /no_waves.txt는 4행이고 첫 데이터는 파 개수 header다. transect File_Loader는 첫 행부터 수치 numberOfWaves열을 3*HEIGHT행 읽는다. 초기 형식 검사부터 서로 다르다. 같은 분기 호출은 선택된 frictionFile도 전달하지 않는다. 업로드 분기와 함수 선언은 frictionFile을 요구한다.

근거 강도: 강함.

#### CT1-352 비활성 통합 퇴적물 셰이더

반대 근거 확인: 현재 실행 경로에서 호출되지 않음. main.js는 활성 SedTrans_Pass3와 SedTrans_UpdateBottom을 fetch한다. 따라서 이 파일의 정적 오류로 현재 본판 전체가 실행 불가라고 쓰지 않는다.

확인한 모순: 동일 전역 이름 중복 선언과 선언하지 않은 텍스처 참조가 함께 있다. Bed_state_here는 .x를 취한 f32인데 다시 .x를 사용한다. 852ec28의 파일 최초 추가 원문에도 같은 오류가 있다. 실제 셰이더 컴파일은 실행하지 않았다.

근거 강도: 강함.

### 2.51 과거 판의 원문 줄과 문자열 이력

이 절의 과거 줄 번호는 `git show HASH:파일`의 원문을 세어 확인했다.
현재 줄에 붙인 blame HASH와 과거 줄 번호를 혼용하지 않는다.

`22e1983:transect_version/shaders/Pass3_Bous.wgsl`

- `22e1983:transect_version/shaders/Pass3_Bous.wgsl:284` `// Psi2x = globals.Bcoef_g * d2_here * (dd_by_dx * (2.0 * eta_by_dx_dx + eta_by_dy_dy) + dd_by_dy * eta_by_dx_dy) + (F_star - F_G_star_oldOldies.y) / globals.dt * 0.5;`
- `22e1983:transect_version/shaders/Pass3_Bous.wgsl:287` `Psi2x = globals.Bcoef_g * d2_here * (dd_by_dx * (2.0 * eta_by_dx_dx));`
- `22e1983:transect_version/shaders/Pass3_Bous.wgsl:385` `// let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + breaking_y + (Psi1y + Psi2y) + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);`
- `22e1983:transect_version/shaders/Pass3_Bous.wgsl:386` `let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x) + press_x, 0.0, hc_by_dx_dx + c_dissipation);`

`22e1983:transect_version/shaders/Pass3A_COULWAVE.wgsl`

- `22e1983:transect_version/shaders/Pass3A_COULWAVE.wgsl:34` `let u_here = (u4.x + u4.y + u4.z + u4.w) / 4.0;`
- `22e1983:transect_version/shaders/Pass3A_COULWAVE.wgsl:41` `// let u_here = textureLoad(txState, idx, 0).y / H_here;  //testing whether velocities directly from flux are better.  They are not`

`22e1983:transect_version/shaders/SedTrans_Pass3.wgsl`

- `22e1983:transect_version/shaders/SedTrans_Pass3.wgsl:77` `let Dxx = 1.0;`
- `22e1983:transect_version/shaders/SedTrans_Pass3.wgsl:78` `let Dxy = 1.0;`
- `22e1983:transect_version/shaders/SedTrans_Pass3.wgsl:79` `let Dyy = 1.0;`
- `22e1983:transect_version/shaders/SedTrans_Pass3.wgsl:93` `let divide_by_h = 2.0 * h / sqrt(h2 + max(h2, globals.epsilon));`

`22e1983:transect_version/shaders/Update_TriDiag_coef.wgsl`

- `22e1983:transect_version/shaders/Update_TriDiag_coef.wgsl:34` `let near_dry = d_here; //textureLoad(txBottom, idx, 0).w;`

`22e1983:transect_version/js/main.js`

- `22e1983:transect_version/js/main.js:957` `var RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);`
- `22e1983:transect_version/js/main.js:1045` `var Pass3_ShaderCode_Bous = null;`
- `22e1983:transect_version/js/main.js:1107` `const Pass3_Pipeline_Bous = createComputePipeline(device, Pass3_ShaderCode_Bous, Pass3_BindGroupLayout, allComputePipelines);`
- `22e1983:transect_version/js/main.js:1412` `RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, depostion_Sed, txBotChange_Sed, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs);`
- `22e1983:transect_version/js/main.js:1423` `RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, depostion_Sed, txBotChange_Sed, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs);`
- `22e1983:transect_version/js/main.js:3269` `startSimulationWithWave(configContent, bathymetryContent, defaultWaveContent, OverlayFile, modelFile);`

`7ae7da4:js/display_parameters.js`

- `7ae7da4:js/display_parameters.js:145` `let slide_vol = 0.25 * calc_constants.disturbanceCrestamp * calc_constants.disturbanceWidth * calc_constants.disturbanceLength / 1000000.0;`

`08860f0:js/main.js`

- `08860f0:js/main.js:1221` `const RenderPipeline_quad = createRenderPipeline(device, vertexShaderCode, fragmentShaderCode, swapChainFormat, RenderBindGroupLayout, 'depth24plus');`
- `08860f0:js/main.js:1223` `var RenderPipeline = RenderPipeline_quad;`
- `08860f0:js/main.js:1966` `RenderPipeline = RenderPipeline_quad;`

`bf8db50:js/main.js`

- `bf8db50:js/main.js:98` `calc_constants.GoogleMapOverlay = 0; // not all configs have this declared, so can create issue when switching back and forth`
- `bf8db50:js/main.js:407` `calc_constants.GoogleMapOverlay = 0;`
- `bf8db50:js/main.js:1075` `var RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);`
- `bf8db50:js/main.js:1528` `// RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, depostion_Sed, txBotChange_Sed, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs);`
- `bf8db50:js/main.js:1530` `RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);`
- `bf8db50:js/main.js:1541` `// RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, depostion_Sed, txBotChange_Sed, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs);`
- `bf8db50:js/main.js:1543` `RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);`

`852ec28:shaders/SedTrans_Pass3_wBedUpdate.wgsl`

- `852ec28:shaders/SedTrans_Pass3_wBedUpdate.wgsl:34` `@group(0) @binding(4) var oldGradients_Sed: texture_2d<f32>;`
- `852ec28:shaders/SedTrans_Pass3_wBedUpdate.wgsl:50` `@group(0) @binding(18) var oldGradients_Sed: texture_2d<f32>;`
- `852ec28:shaders/SedTrans_Pass3_wBedUpdate.wgsl:229` `let Bed_state_here = textureLoad(txBedState_Sed, idx, 0).x;`
- `852ec28:shaders/SedTrans_Pass3_wBedUpdate.wgsl:235` `newBed.x = Bed_state_here.x + globals.dt * d_by_dt_Bed;`
- `852ec28:shaders/SedTrans_Pass3_wBedUpdate.wgsl:239` `newBed.x = Bed_state_here.x + globals.dt / 12.0 * (23.0 * d_by_dt_Bed - 16.0 * oldBedGradients_Sed + 5.0 * oldOldBedGradients_Sed);`
- `852ec28:shaders/SedTrans_Pass3_wBedUpdate.wgsl:246` `newBed.x = Bed_state_here.x + globals.dt / 24.0 * (9.0 * d_by_dt_Bed + 19.0 * predictedBed - 5.0 * oldBedGradients_Sed + oldOldBedGradients_Sed);`

`ebca435:js/Time_Series.js`

- `ebca435:js/Time_Series.js:108` `if (timeSeriesDataEpoch != calc_constants.timeSeriesDataEpoch) {`

문자열 검색은 다음과 같다.
각 명령은 읽기 전용 `git log -S`다.

| 검색어 | 경로 | 결과 |
|---|---|---|
| `Psi2x` | `transect_version/shaders/Pass3_Bous.wgsl` | 22e1983 2025-06-06 Sediment transport updates and transect model beta |
| `let u_here = (u4.x + u4.y + u4.z + u4.w) / 4.0;` | `transect_version/shaders/Pass3A_COULWAVE.wgsl` | 22e1983 2025-06-06 Sediment transport updates and transect model beta |
| `BETA - currently no feedback` | `transect_version/index.html` | 22e1983 2025-06-06 Sediment transport updates and transect model beta |
| `B_here = B_here` | `transect_version/shaders/SedTrans_UpdateBottom.wgsl` | 22e1983 2025-06-06 Sediment transport updates and transect model beta |
| `timeSeriesDataEpoch` | `js/Time_Series.js` | ebca435 2026-07-20 fixed time series write bug |
| `const bytesPerRow = ((actualBytesPerRow + 255)` | `js/Copy_Data_to_Textures.js` | ca9278e 2026-02-11 Update Copy_Data_to_Textures.js |

`Psi2x`와 면속도 평균의 transect 이력에는 최초 추가 이후 해당 문자열 개수의 변화가 없다.
이 문장은 모든 줄이 최초 추가 이후 같다는 뜻이 아니다.
해당 파일의 `--follow -p` 원문과 현재 diff가 나머지 변경을 판별한다.


### 2.52 진입점·출력 판독기·기존 문서의 적용 범위

추가 진입점은 모두 본판 모듈을 가리킨다.
이 사실은 transect 수치 경로가 다른 HTML을 통해 실행된다는 근거가 아니다.

| 위치 | 원문 | 확인한 의미 |
|---|---|---|
| `ebca435:index_headless.html:112` | `<script type="module" src="js/main.js"></script>` | 본판 main 모듈을 로드한다. |
| `ebca435:index_nots.html:1486` | `<script type="module" src="js/main.js"></script>` | 본판 main 모듈을 로드한다. |
| `ebca435:river.html:1468` | `<script type="module" src="js/main.js"></script>` | 본판 main 모듈을 로드한다. |
| `ebca435:MC_examples.html:1468` | `<script type="module" src="js/main.js"></script>` | 본판 main 모듈을 로드한다. |

`index_headless.html:53–59`와 다른 진입점의 초기 수면·hardbottom 입력은 본판 초기화의 추가 인자와 연결된다.
이 보고서는 이 부속 진입점의 DOM 계약 전체가 현재 main.js와 일치한다고 검증하지 않았다.

`scripts/load_WebGPUCeleris_output.m:18`의 원문은 `bathytopo = fread(fid, [nx, ny], 'float32');`다.
`scripts/load_WebGPUCeleris_output.m:30`의 원문은 `eta = fread(fid, [nx, ny], 'float32');`다.
`scripts/load_WebGPUCeleris_output.m:73`의 원문은 `pcolor(x, y, eta');  % note the transpose '  - the surface data is [nx,ny]`다.
두 판의 writer는 실수 배열을 `y*WIDTH+x` 순서로 쓴다.
이 MATLAB reader의 `[nx,ny]` 및 전치는 그 순서와 연결된다.
transect 출력의 각 y행은 독립 단면이라는 의미를 추가해야 한다.
본판의 시간별 `depth_*.bin`은 이 reader의 고정 `bathytopo.bin` 읽기와 구분한다.
`scripts/clean_WebGPUCeleris_output.m:4`와 `:5`는 각각 `! del *.bin`과 `! del *.txt`다.
두 줄은 Windows 정리 명령이다.
정리 스크립트는 실행하지 않았다.

`ARCHITECTURE.md:5`의 원문은 다음과 같다.

```text
This document intentionally excludes the transect implementation. The transect directory is a separate specialized model with its own contracts and should be documented separately.
```

`docs/README.md:5`의 원문은 다음과 같다.

```text
The transect implementation is intentionally excluded. Do not infer transect behavior from these notes and do not use these notes as coverage for transect files.
```

이 두 원문은 본판 문서를 transect 기능 명세로 그대로 적용하지 말라는 직접 근거다.
사용자 지시에 따라 이 보고서는 코드끼리의 차이를 별도로 판정한다.

## 3 코드에만 있는 처리

이 절에서 코드에만 있는 처리는 본판 문서가 설명하지 않는 transect의 선택·식·검사를 뜻한다.
C 행은 본판과 수학적으로 동등하다는 뜻이 아니다.
동등성을 보인 1D 식은 F 행이다.
현재 transect에만 있는 파일은 `shaders/Pass2_HighOrder.wgsl` 한 개다.
파일 안의 transect 전용 함수도 아래 목록에 포함한다.

| 행 ID | transect 전용 처리·옵션·자료 형식 | 근거 |
|---|---|---|
| CT1-053 | transect 판은 단일점 섬 제거를 주석 처리한다. transect 판은 북쪽 면 고도 BN을 0.0으로 저장한다. 이는 본판 전처리의 보존이 아니라 단면 전용 선택이다. | `js/Copy_Data_to_Textures.js:15` `let change_point = 1.;` / `transect_version/js/Copy_Data_to_Textures.js:15` `// let change_point = 1.;` |
| CT1-055 | transect 판은 numberOfWaves × HEIGHT 텍스처를 만든다. 입력의 첫 HEIGHT행은 진폭이다. 다음 HEIGHT행은 주기다. 마지막 HEIGHT행은 위상이다. 방향 채널은 0.0이다. bytesPerRow는 256배수로 올림한다. | `transect_version/js/Copy_Data_to_Textures.js:92` `` |
| CT1-060 | transect 판은 copyTransectWaveDataToTexture를 export한다. 본판은 경계 시계열과 구면 계량 함수를 export한다. | `js/Copy_Data_to_Textures.js:638` `// export { copyBathyDataToTexture, copyWaveDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture};` / `transect_version/js/Copy_Data_to_Textures.js:555` `export { copyBathyDataToTexture, copyTransectWaveDataToTexture, copyWaveDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture};` |
| CT1-061 | transect 판은 제목에 Transect Mode를 표시한다. | `index.html:8` `<title>Celeris-WebGPU</title>` / `transect_version/index.html:8` `<title>Celeris-WebGPU: Transect Mode</title>` |
| CT1-065 | transect 판은 예제 label과 select를 display:none으로 숨긴다. | `index.html:311` `<html4f>` / `transect_version/index.html:262` `<label style="display: none;" for="run_example-select">Choose Example:</label>` |
| CT1-067 | transect 판은 예제 실행 버튼을 숨긴다. 직접 파일 입력 실행은 남긴다. | `index.html:361` `</select>` / `transect_version/index.html:300` `</select>` |
| CT1-080 | transect 판은 BETA - currently no feedback w/ hydro라고 명시한다. 바닥고 고정은 이 안내에 맞는 의도된 처리다. | `transect_version/index.html:785` `` |
| CT1-083 | transect 판은 /transect_version/js/main.js를 로드한다. 본판은 상대 js/main.js를 로드한다. 루트 아래 배포를 가정하는 차이다. | `index.html:1597` `<script type="module" src="js/main.js"></script>` / `transect_version/index.html:1471` `<script type="module" src="/transect_version/js/main.js"></script>` |
| CT1-085 | 본판 함수는 hardbottom.txt의 WIDTH×HEIGHT 고도를 읽는다. transect 함수는 waves.txt의 numberOfWaves열·3*HEIGHT행을 읽는다. 두 함수는 열 수와 반환 배열 크기가 다르다. | `js/File_Loader.js:205` `` / `transect_version/js/File_Loader.js:145` `// load transect wave data` |
| CT1-099 | 본판은 binding 9에 txBoundaryForcing을 둔다. 본판은 binding 10–13에 4변 경계 시계열을 둔다. transect 판은 binding 9에 txWaves_Transect를 둔다. 같은 번호의 리소스 의미가 다르다. | `js/Handler_BoundaryPass.js:96` `// Added by Codex: Start boundary time-series forcing texture bindings.` / `transect_version/js/Handler_BoundaryPass.js:100` `export function create_BoundaryPass_BindGroup(device, uniformBuffer, current_stateUVstar, txBottom, txWaves, txNewState_Sed, txtemp, txtemp_Sed, txBreaking, txtemp_Breaking, txWaves_Transect) {` |
| CT1-100 | transect 판의 binding 9는 단면 행별 파랑을 읽는다. 본판은 경계 강제장과 시계열을 별개 리소스로 둔다. | `js/Handler_BoundaryPass.js:181` `},` / `transect_version/js/Handler_BoundaryPass.js:141` `} ,` |
| CT1-126 | transect 판은 H=0·T=0·direction=0·numberOfWaves=2를 둔다. 본판은 H=1·T=10·direction=0·numberOfWaves=1을 둔다. transect 판은 파 성분 수를 파일 헤더에서 갱신하지 않는다. 본판만 trough_factor=1과 4변 시계열 파일·관측점 수·시각 이동을 정의한다. | `js/constants_load_calc.js:77` `incident_wave_H: 1.,  // Height (m) of Sine Wave / Pulse / Solitary Wave, or Significant Wave Height of Spectrum` / `transect_version/js/constants_load_calc.js:66` `incident_wave_H: 0,  // Height (m) of Sine Wave / Pulse / Solitary Wave, or Significant Wave Height of Spectrum` |
| CT1-152 | transect 판은 binding 9를 단면별 파랑에 사용한다. 본판은 지형변동 강제장을 읽고 10–13에서 경계 시계열을 읽는다. | `shaders/BoundaryPass.wgsl:72` `@group(0) @binding(9) var txBoundaryForcing: texture_2d<f32>;` / `transect_version/shaders/BoundaryPass.wgsl:58` `@group(0) @binding(9) var txWaves_Transect: texture_2d<f32>;` |
| CT1-156 | transect 판은 ky와 기점 이동을 0으로 둔다. pulse의 성분 지속 길이는 4주기이고 본판은 5주기다. 본판만 음의 eta에 trough_factor를 곱한다. transect 판은 국소 바닥고로 파수를 계산한다. 본판은 base_depth를 쓴다. transect 판은 같은 y행의 파랑 성분을 읽는다. 본판의 시계열 공간·시간 선형 보간은 transect 판에 없다. transect 판은 dhdt 바닥 보정을 하지 않는다. 주기 경계는 비활성이다. 본판의 중첩 sponge 가중 평균 대신 동서 sponge를 순서대로 대입한다. | `shaders/BoundaryPass.wgsl:164` `if (current_boundary == 1 \|\| current_boundary == 3) {` / `transect_version/shaders/BoundaryPass.wgsl:149` `//if (current_boundary == 1 \|\| current_boundary == 3) {` |
| CT1-158 | transect 판은 남북 입사파와 모든 주기 경계를 주석 처리한다. 본판의 type5 시계열 경계 대입은 없다. transect UI의 별표와 연결된다. | `shaders/BoundaryPass.wgsl:482` `if (globals.south_boundary_type == 2 && idx.y <= 2) {` / `transect_version/shaders/BoundaryPass.wgsl:308` `// if (globals.south_boundary_type == 2 && idx.y <= 2) {` |
| CT1-161 | transect 판은 북쪽 하천 경계를 주석 처리한다. transect 판은 고립 습윤점과 단일 격자 수로 끝의 동결을 주석 처리한다. 음수 수심 검사는 유지한다. h_here 재평가는 앞에서 BCState를 더 바꾸지 않으므로 생략해도 현재 경로에서 같은 값이다. | `shaders/BoundaryPass.wgsl:605` `if (globals.north_boundary_type == 4) {` / `transect_version/shaders/BoundaryPass.wgsl:438` `// if (globals.north_boundary_type == 4) {` |
| CT1-192 | transect 판은 periodic_bc_fix를 주석 처리한다. transect 경계 셰이더는 주기 경계 복사도 주석 처리한다. UI는 주기 경계에 별표를 붙인다. 이는 지원하지 않는 경로의 단면판 선택이다. | `shaders/Pass3_Bous.wgsl:183` `var periodic_bc_fix = -1;` / `transect_version/shaders/Pass3_Bous.wgsl:184` `// var periodic_bc_fix = -1;` |
| CT1-202 | 주기 경계를 구현하지 않는 단면판은 해당 분산 차단도 주석 처리한다. x 수면의 4차 차분은 유지한다. | `shaders/Pass3_COULWAVE.wgsl:188` `var periodic_bc_fix = -1;` / `transect_version/shaders/Pass3_COULWAVE.wgsl:189` `// var periodic_bc_fix = -1;` |
| CT1-218 | transect 판은 점성 상한을 dx*dx/dt로 둔다. 본판은 dx*dy/dt다. 둘 다 길이제곱/시간 단위다. dx==dy일 때만 수치가 같다. 독립 단면의 x 격자 척도를 쓰는 의도된 단순화다. | `shaders/Pass_Breaking.wgsl:125` `let nu_breaking = min(1.0 * globals.dx * globals.dy / globals.dt, B_Breaking * globals.delta_breaking * h_here * detadt);` / `transect_version/shaders/Pass_Breaking.wgsl:127` `// let nu_breaking = min(1.0 * globals.dx * globals.dy / globals.dt, B_Breaking * globals.delta_breaking * h_here * detadt);` |
| CT1-227 | transect 판은 hardbottom·초기 바닥고·외곽 셀 조기 반환을 쓰지 않는다. 북쪽·동쪽 이웃으로 진단 면 변화량을 계산한다. HTML의 no feedback 안내와 연결된다. | `shaders/SedTrans_UpdateBottom.wgsl:25` `@group(0) @binding(7) var txHardBottom: texture_2d<f32>;` / `transect_version/shaders/SedTrans_UpdateBottom.wgsl:30` `var dB_cumulative = textureLoad(txBotChange_Sed, idx, 0);` |
| CT1-228 | transect 판은 B_here=B_here로 현재 바닥고를 유지한다. 진단 누적값에는 -dB를 적산한다. 본판은 B_here-dB를 수리에 돌려주고 초기 바닥고와의 차이로 누적량을 만든다. 의도 근거가 있으므로 바닥고 고정 자체를 결함으로 판정하지 않는다. 동쪽 면 평균은 본판이 0.75*현재+0.25*이웃인 데 비해 transect는 0.5*현재+0.5*이웃이다. | `shaders/SedTrans_UpdateBottom.wgsl:60` `let e_left =  textureLoad(erosion_Sed, leftIdx, 0).x;` / `transect_version/shaders/SedTrans_UpdateBottom.wgsl:41` `let dB_here = globals.dt * (e_here - d_here) / (1.0 - globals.sedC1_n); // this is positive when eroding - when increasing depth, or decreasing elevation` |
| CT1-240 | transect 판은 표준 파일의 NLSW_or_Bous==2 분기에서 z_loc와 zx_loc를 0.0으로 둔다. 실제 mode 2는 별도 COULWAVE 계수 파일을 fetch한다. 이 변경은 현재 실행 경로에서 호출되지 않는 대안이다. | `shaders/Update_TriDiag_coef.wgsl:54` `let z_loc = textureLoad(current_state, idx, 0).x;` / `transect_version/shaders/Update_TriDiag_coef.wgsl:54` `let z_loc = 0.0; //textureLoad(current_state, idx, 0).x;` |
| CT1-245 | transect 판은 동·서가 모두 음의 바닥고인 양의 중심 고도를 0으로 만든다. 북·남 면 보정은 하지 않는다. 초기 CPU 단일점 제거는 별도로 꺼져 있다. | `shaders/Update_neardry.wgsl:35` `}` / `transect_version/shaders/Update_neardry.wgsl:36` `// }` |
| CT1-254 | transect 판은 단면 파랑 reader와 uploader를 import한다. 본판은 초기 수면·hardbottom·경계 시계열·중첩 writer·파 생성기를 import한다. | `js/main.js:3` `// import { loadDepthSurface, loadInitCondSurface, loadFrictionSurface, loadHardBottomSurface, loadWaveData, loadOverlay, CreateGoogleMapImage, calculateGoogleMapScaleAndOffset, loadImageBitmap, loadUserImage, loadCubeBitmaps} from './File_Loader.js';  // load depth surface and wave data file` / `transect_version/js/main.js:3` `import { loadDepthSurface, loadFrictionSurface, loadTransectWaveData, loadWaveData, loadOverlay, CreateGoogleMapImage, calculateGoogleMapScaleAndOffset, loadImageBitmap, loadUserImage, loadCubeBitmaps} from './File_Loader.js';  // load depth surface and wave data file` |
| CT1-258 | transect 판은 loadTransectWaveData를 호출한다. 성분 수는 config 값을 유지한다. 초기화 함수는 config·bathy·waves·overlay·model·friction의 6인자를 받는다. 본판은 초기 수면·hardbottom·4변 시계열을 추가로 받는다. | `js/main.js:206` `let { numberOfWaves, waveData } = await loadWaveData(waveContent, calc_constants);  // Start this only after the first function completes` / `transect_version/js/main.js:76` `//let { numberOfWaves, waveData } = await loadWaveData(waveContent, calc_constants);  // Start this only after the first function completes` |
| CT1-262 | transect 판은 U/V 주소 모드 repeat를 쓴다. 본판은 mirror-repeat를 쓴다. 텍스처 경계 밖의 표시 샘플이 다르다. 계산 flux에는 영향이 없다. | `js/main.js:441` `addressModeU: 'mirror-repeat',` / `transect_version/js/main.js:176` `addressModeU: 'repeat',` |
| CT1-265 | transect 판은 Nwave×HEIGHT의 txWaves_Transect를 할당하고 단면 파랑을 업로드한다. 일반 txWaves는 할당하지만 업로드하지 않는다. 본판은 파 생성 용량과 4변 시계열 텍스처를 할당한다. transect 표시 레이어는 10개 영상·2개 f16이고 본판은 11개 영상·3개 f16이다. 본판만 초기 수면과 hardbottom 파일을 읽는다. 초기 상태 API의 차이는 uploader 행과 같다. | `js/main.js:553` `const txSamplePNGs = create_3D_Image_Texture(device, 1024, 1024, 11, allTextures); // will store all textures to be sampled for photo-realism` / `transect_version/js/main.js:285` `const txSamplePNGs = create_3D_Image_Texture(device, 1024, 1024, 10, allTextures); // will store all textures to be sampled for photo-realism` |
| CT1-275 | transect 판은 퇴적물 확장 uniform을 쓰지 않는다. transect 판의 두 BoundaryPass 바인드 그룹은 txWaves_Transect를 받는다. 본판은 지형 강제장과 4변 시계열을 받는다. | `js/main.js:1146` `SedTrans_Pass3_view.setFloat32(80, calc_constants.base_depth, true);           // f32` / `transect_version/js/main.js:727` `const BoundaryPass_BindGroup = create_BoundaryPass_BindGroup(device, BoundaryPass_uniformBuffer, current_stateUVstar, txBottom, txWaves, txNewState_Sed, txtemp_boundary, txtemp_boundary_Sed, txBreaking, txtemp_Breaking, txWaves_Transect);` |
| CT1-303 | 수정 단계의 계산·경계·PCR 순서는 같다. 통계 카운터 uniform은 transect가 직전에 갱신하고 본판은 encoder 생성 전에 갱신한다. transect의 퇴적물 바닥고 고정은 HTML 안내에 맞는다. 본판만 중첩 경계 캡처·다운로드·리소스 해제를 실행한다. 이력 texture 이동과 통계의 상대 순서는 같다. | `js/main.js:2808` `` / `transect_version/js/main.js:1715` `runComputeShader(device, commandEncoder, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);` |
| CT1-347 | transect 고차 모드의 활성 x HLLEM flux다. near-dry에서 DU.x를 0으로 만든다. y flux와 횡운동량을 생략한다. 퇴적물 4개 채널의 x flux는 NumericalFlux로 쓴다. phix=1.0이다. 본판은 같은 이름 파일을 2025-11-07에 HLLC/HLLEM 이름으로 분리했다. | `ebca435:transect_version/shaders/Pass2_HighOrder.wgsl:191` `xflux = HLLEM_Flux(aplus, aminus, Fp_x, Fm_x, state_plus_x, state_minus_x, DU_flag);` |

추가로 분리한 transect 전용 처리는 다음과 같다.

| 행 ID | 처리 | 원문 근거 |
|---|---|---|
| CT1-375 | transect main은 모든 셰이더 URL을 /transect_version/shaders 아래에서 읽는다. 이 URL은 문서 루트에 transect_version 경로가 존재한다고 가정한다. 계산식 변경과 배포 경로 변경을 분리해서 적는다. | 4.3절의 같은 행 ID와 전체 diff. |
| CT1-378 | transect BoundarySineWave는 해당 행·해당 경계 셀의 바닥고를 쓴다. 본판은 -base_depth를 쓴다. 따라서 단면마다 경계 수심이 다르면 파수와 운동량의 크기도 단면마다 달라진다. 이 선택은 단지 y 위상을 0으로 둔 대수적 환원과 다르다. | 4.3절의 같은 행 ID와 전체 diff. |

코드에만 남은 잘못된 식과 입력 경로는 C로 정당화하지 않는다.
`CT1-183`의 면속도 평균과 `CT1-196`의 Psi2x 누락은 E다.
`CT1-224`의 역수심·y 확산과 `CT1-285`의 null 셰이더도 E다.
`CT1-336`의 기본 파랑 파일과 마찰 인자 누락은 E다.
근거 강도와 반대 근거는 2.50절에 있다.

## 4 노트 대조와 수정안

현재 노트는 수정하지 않았다.
아래 문장은 해당 노트에 넣을 수정안이다.
원래 문장이 본판 설명으로 맞는 경우에는 transect 차이를 덧붙인다.
B는 노트 자체의 서술 오류다.
E는 노트 오기가 아니라 소스의 결함 후보를 노트에 추가할 항목이다.

### CT1-355 분석 범위와 파일 수

현재 노트: `models/Celeris/README.md:5`

```text
> ✅ **현재 상태(2026-06-15 전수조사 완료)**: Celeris-WebGPU 소스(`raw/source_code/Celeris-WebGPU/`, 35 JS + 42 WGSL) clone + **source-analysis 9 노트 + manual-notes 1 노트** 작성(모두 `file:line` 인용 verified). web-refs 1 + 정체카드도 verified.
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| A | 2.1 및 해당 파일의 전체 diff. | 기존 완료 표시는 본판의 해당 날짜 조사로 한정한다. 이번 대조의 78개 경로와 본판 66개 공통·11개 전용, transect 1개 전용이라는 집계를 별도 표로 적는다. 분류 E 행 수를 독립 결함 수로 쓰지 않는다. |

### CT1-356 고차 flux의 판별

현재 노트: `models/Celeris/source-analysis/celeris-source-map.md:41`

```text
- **Riemann 수치플럭스**: `Pass2.wgsl:34-40` `NumericalFlux()` = HLL 형태 `(a⁺F⁻−a⁻F⁺+a⁺a⁻ΔU)/(a⁺−a⁻)`. High-order 경로는 HLLC를 선택(`main.js:1548`).
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | CT1-285 및 해당 파일의 전체 diff. | 본판 Accuracy_mode==1은 Pass2_HighOrder_HLLC를 선택한다. transect 판은 Pass2_HighOrder의 HLLEM 함수를 선택한다. transect 파일은 별도 source map으로 연결한다. |

### CT1-357 실행 그래프 범위

현재 노트: `models/Celeris/source-analysis/celeris-pipeline-graph.md:96`

```text
| `Accuracy_mode` | 1 | Pass1 → `Pass1_HighOrder.wgsl` (4th-order MUSCL-TVD), Pass2 → `Pass2_HighOrder_HLLC.wgsl` | `js/main.js:1539-1551` |
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | CT1-285 및 해당 파일의 전체 diff. | 이 표는 본판 경로다. transect 판은 고차 flux에 HLLEM을 사용한다. transect 판은 각 계산·복사를 즉시 submit한다. transect 판은 y PCR을 실행하지 않는다. |

### CT1-358 Psi2x 적용 범위

현재 노트: `models/Celeris/source-analysis/celeris-boussinesq-solver.md:94`

```text
이 Psi 항이 source_term의 운동량 성분에 더해져(`:392`) **명시(explicit) RHS**를 만든다. 이 RHS가 `current_stateUVstar`로 출력(`:429`)되고, 이것이 **음해 tridiagonal solve의 우변 b**가 된다.
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| E | CT1-196 및 해당 파일의 전체 diff. | 본판은 Psi1x+Psi2x를 x 운동량 source에 더한다. transect 판은 Psi2x를 계산하지만 source에서 빼먹는다. 지형 경사와 수면 곡률이 모두 0이 아닌 조건에서 정적 결함 후보가 된다. |

### CT1-359 near-dry 이웃 수

현재 노트: `models/Celeris/source-analysis/celeris-fv-reconstruction.md:37`

```text
**왜 분리하나**: wet/dry 판정을 무거운 재구성·flux 로직 바깥으로 빼서, Pass2가 `minH = min(4 이웃 수심)` 한 번으로 near-dry 분기를 결정하게 한다 (`Pass2.wgsl:105`, `Pass2_HighOrder_HLLC.wgsl:184`). 주석 라인(`// min(h_here, h_north)`, `Pass0.wgsl:52-55`)을 보면 원래 `h_here`와의 min을 의도했으나 현재는 이웃값만 저장한다 — 이 차이는 코드상 그대로다.
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | CT1-175 및 CT1-182 및 해당 파일의 전체 diff. | 본판은 네 이웃을 쓰고 transect 판은 동·서 두 이웃만 쓴다. transect의 h_vec.x와 h_vec.z는 0.0이다. 따라서 본판의 네 성분 최소값 식을 transect에 그대로 적용하지 않는다. |

### CT1-360 활성 HLLEM의 판 구분

현재 노트: `models/Celeris/source-analysis/celeris-fv-reconstruction.md:162`

```text
**활성 여부** (`ARCHITECTURE.md:69-72`): `Accuracy_mode==1`(고차)에서 `main.js`는 `Pass2_HighOrder_HLLC.wgsl`만 fetch (`js/main.js:1547-1548`). **HLLEM은 소스에 존재하나 현재 main.js 경로에서 선택되지 않음**(present-but-not-default).
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | CT1-285 및 해당 파일의 전체 diff. | HLLEM 비활성이라는 문장은 본판 main.js에 한정한다. transect main.js는 Accuracy_mode==1에서 Pass2_HighOrder의 HLLEM 함수를 활성화한다. |

### CT1-361 쇄파 점성 상한

현재 노트: `models/Celeris/source-analysis/celeris-breaking-boundary.md:66`

```text
`B·δ_b·h·(∂η/∂t)` 형태(δ_b = `delta_breaking`)에 수치 안정 상한 `dx·dy/dt`을 건다. 이는 FUNWAVE eddy-viscosity breaker의 ν ∝ δ²·h·(∂η/∂t) 구조와 동형(δ_b가 길이 스케일 역할).
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | CT1-218 및 해당 파일의 전체 diff. | 본판의 점성 상한은 dx*dy/dt다. transect 판의 점성 상한은 dx*dx/dt다. 두 값은 dx==dy일 때 같다. transect 판은 x 방향 쇄파 나이와 응력만 전달한다. |

### CT1-362 면속도 평균

현재 노트: `models/Celeris/source-analysis/celeris-coulwave.md:38`

```text
- `txModelVelocities = (u, v, eta, H)` — 셀평균 속도. u_here/v_here는 face velocity 4성분 평균 `(u4.x+y+z+w)/4` (`Pass3A_COULWAVE.wgsl:34-35`). flux에서 직접 뽑은 속도는 주석으로 "are not better"라 폐기됨 (`:41-42`).
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| E | CT1-183 및 해당 파일의 전체 diff. | 네 면 평균은 본판에서 사용한다. transect Pass1은 북·남 면속도를 0으로 쓰므로 동일한 분모 4는 일정 x 유속을 절반으로 만든다. transect CalcMeans의 두 면 평균과 이 차이를 함께 경고한다. |

### CT1-363 표준 flux의 활성 확산

현재 노트: `models/Celeris/source-analysis/celeris-sediment.md:104`

```text
수평 난류확산(`sedTurbDispersion` 배경 + `sedBreakingDispersionCoef`×breaking eddy viscosity) 코드는 `SedTrans_Pass3.wgsl:102-119`에 **전부 주석처리**되어 있음. 즉 현재 활성 빌드는 **이류 + 픽업/침강만**, 명시적 확산 없음. config 키(`sedTurbDispersion=0.01`, `sedBreakingDispersionCoef=0.1`, `constants_load_calc.js:112-113`)는 uniform으로 전달되나 셰이더에서 미사용.
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| B | CT1-182 및 해당 파일의 전체 diff. | 본판 SedTrans_Pass3 안의 확산 대안은 주석이다. 그러나 표준 Pass2는 class 1 flux에 -k*h*grad(C)를 실제로 넣는다. 고차 HLLC/HLLEM 경로는 별도 식을 쓰므로 Accuracy_mode에 따라 확산 구현을 나눠 적는다. transect SedTrans_Pass3는 Dxx=Dxy=Dyy=1.0의 확산을 source에서 계산한다. |

### CT1-364 수리 지형 되먹임의 판 차이

현재 노트: `models/Celeris/source-analysis/celeris-sediment.md:108`

```text
`SedTrans_UpdateBottom.wgsl`은 침식−침강 차를 공극률로 보정한 **Exner형 질량보존**으로 바닥고를 갱신:
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | CT1-228 및 해당 파일의 전체 diff. | 본판 UpdateBottom은 바닥고를 갱신한다. transect UpdateBottom은 B_here=B_here로 수리 바닥고를 고정하고 진단 누적량만 적산한다. 이 동작은 transect HTML의 no feedback 안내와 일치한다. |

### CT1-365 비활성 통합본의 정적 오류

현재 노트: `models/Celeris/source-analysis/celeris-sediment.md:140`

```text
- `SedTrans_Pass3_wBedUpdate.wgsl` — fetch 없음. Pass3 안에서 bed update까지 합친 통합 실험본(현재는 UpdateBottom으로 분리). **비활성**.
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| E | CT1-352 및 해당 파일의 전체 diff. | SedTrans_Pass3_wBedUpdate는 현재 실행 경로에서 호출되지 않는다. 이 파일에는 중복 전역 선언과 미정의 바닥 이력 텍스처 참조가 있다. 비활성 실험본을 활성 모델 근거로 인용하지 않는다. |

### CT1-366 시계열 초기화와 버퍼 수명

현재 노트: `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:238`

```text
- readback: `readToolTipTextureData`가 1D 텍스처를 256B/행 버퍼로 `copyTextureToBuffer` → `mapAsync(READ)` → `timeSeriesData[i].{time,eta,P,Q}`에 push (`js/Time_Series.js:60-128`). `downloadTimeSeriesData`가 위치·시계열을 텍스트로 내보냄 (라인 128-171). 차트는 1초 간격 갱신 (`js/main.js:5488`).
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| E | CT1-311 및 해당 파일의 전체 diff. | 점 readback의 단일 행 복사 규약은 유지한다. 본판 ebca435는 epoch 검사로 오래된 readback을 버린다. transect 판은 해당 수정이 없다. 초기화 순서 결함과 type5의 절대 시각 지원 차이를 분리한다. |

### CT1-367 f16 레이어 수

현재 노트: `models/Celeris/source-analysis/celeris-render.md:22`

```text
매 렌더 직전 1회 compute 패스. full-precision `rgba32float` 시뮬 텍스처 여러 장을 자주 샘플되는 변수만 골라 **단일 `rgba16float` 2D-array 텍스처**(`txRenderVarsf16`, 3 layer)로 packing. 목적: fragment/vertex3D가 적은 수의 텍스처만, 또 절반 대역폭(f16)으로 sample하게 해 렌더 압력 감소 (`docs/architecture/DATA_AND_TEXTURES.md:97-103`).
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | CT1-166 및 해당 파일의 전체 diff. | 본판 txRenderVarsf16은 세 레이어다. transect 판은 두 레이어다. transect 판은 가용 퇴적층 깊이 레이어를 만들지 않는다. 건조 eta와 foam의 표시 보정도 본판에만 있다. |

### CT1-368 vertex3D 고도 입력

현재 노트: `models/Celeris/source-analysis/celeris-render.md:34`

```text
fragment·vertex3D는 이후 `txRenderVarsf16`를 layer index로 sample (예: 유속은 layer 1, 세굴심도는 layer 2).
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| B | CT1-253 및 해당 파일의 전체 diff. | 본판 vertex3D는 etaTexture를 textureLoad하여 full precision 수면을 읽는다. transect vertex3D는 txRenderVarsf16의 레이어 0을 textureSampleLevel로 읽는다. 두 판의 영역 길이도 각각 (W-1)*dx와 W*dx다. |

### CT1-369 설정 표의 적용 판

현재 노트: `models/Celeris/manual-notes/celeris-architecture-and-config.md:79`

```text
| `Accuracy_mode` (고차) | — | `Pass1_HighOrder.wgsl`, `Pass2_HighOrder_HLLC.wgsl` (현 고차 경로는 HLLC 선택) |
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | CT1-285 및 해당 파일의 전체 diff. | 고차 HLLC 선택은 본판에 한정한다. transect 판의 입력 waves.txt는 numberOfWaves열·3*HEIGHT행의 진폭·주기·위상 묶음이다. 같은 이름의 JSON 키라도 파랑 파일과 바인딩 계약을 두 판 사이에서 그대로 옮기지 않는다. |

### CT1-370 이론 계보와 단면 구현 분리

현재 노트: `models/Celeris/web-refs/celeris-coulwave-theory.md:14`

```text
> ⚠️ **2026-06-15 정정**: 이 노트의 이전 판은 COULWAVE를 "Lynett-Liu 2004 **2층(two-layer)** 모델, kh≈6 deep-water"로 규정했으나 **소스 정독 결과 틀림**. Celeris는 **단일 reference velocity z_α(single-layer)**만 쓴다(`Pass3A_COULWAVE.wgsl:44` za 단일값). 코드의 "COULWAVE equations"는 **단일층 완전비선형(fully-nonlinear) 확장 Boussinesq**이며, 2층 모델은 **구현돼 있지 않다**. 아래는 그 정정판.
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | CT1-184 및 해당 파일의 전체 diff. | 단일 reference velocity라는 설명은 유지한다. 이론 계보만으로 transect 수식의 누락을 정당화하지 않는다. transect의 y 미분 제거와 실제 1D 구현 결함 후보는 이 보고서의 원문 대조를 별도로 인용한다. |

### CT1-371 공식 자료와 transect 적용 범위

현재 노트: `models/Celeris/web-refs/celeris-official-resources.md:31`

```text
- **Lynett, P. et al. (2026)** "An Interactive Nearshore Wave Simulator for Rapid Design Prototyping and Natural Hazard Education." *J. Waterway, Port, Coastal, and Ocean Engineering* **152**(4). DOI: [10.1061/JWPED5.WWENG-2370](https://doi.org/10.1061/JWPED5.WWENG-2370) (2026-04-03). — 본 위키가 분석한 **Celeris-WebGPU**(브라우저)의 논문. ★초록이 **두 위상해상 모델 = Madsen & Sørensen enhanced Boussinesq + 완전비선형 확장 Boussinesq, modern FV scheme**으로 명시 — 본 위키 소스 정독 결론([`celeris-coulwave-theory.md`](celeris-coulwave-theory.md) §0 모드1=Madsen·모드2=완전비선형)과 **독립 일치**. (repo `docs/lynett-et-al-2026-...pdf` 동봉.)
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | 2.52 및 해당 파일의 전체 diff. | WebGPU 논문과 공식 저장소 연결은 유지한다. 본판과 transect 판을 구분하는 문장을 추가한다. 논문 초록의 모드·정확도 서술을 transect의 현재 모든 경로에 자동 적용하지 않는다. |

### CT1-372 논문 초록과 코드 판

현재 노트: `models/Celeris/web-refs/celeris-lynett-2026.md:18`

```text
> **Celeris-WebGPU (version 1)**은 브라우저 기반 인터랙티브 nearshore wave 시뮬레이터로, **연안공학 설계와 자연재해 교육**을 지원한다. 두 가지 depth-integrated phase-resolving 모델을 구현한다 — (1) **standard mode**: 약비선형·약분산용 *enhanced Boussinesq* 방정식, (2) **high-order mode**: 정확도 향상을 위한 *완전비선형 확장(extended) Boussinesq* 방정식. 두 모드 모두 **hybrid finite-volume–finite-difference** 기법을 쓰며, standard는 공간 2차, high-order는 4차 정확도. 시뮬레이션·시각화 파이프라인 전체가 **WebGPU**를 통해 GPU에서 구동되어, 웹 브라우저 안에서 일반 데스크탑 하드웨어로 **faster-than-real-time** 성능을 낸다. (초록 발췌, p.04026007-1)
```

| 판정 | 코드 근거 | 노트 수정안 |
|---|---|---|
| C | 2.52 및 해당 파일의 전체 diff. | 이 문단은 논문 초록의 주장임을 유지한다. transect 판의 고차 재구성과 고차 flux 선택은 현재 소스에서 따로 확인한다. 이 보고서는 PDF 식·표·그림의 새로운 검증을 주장하지 않는다. |

### 4.1 B 판정의 시점 근거

퇴적물 노트의 `note_date`는 2026-06-15다.
2025-06-08 `b8b50c3`의 표준 Pass2 원문은 이미 확산 flux를 포함한다.
`b8b50c3:shaders/Pass2.wgsl:189–194`의 이어진 식은 다음과 같다.

```wgsl
let xflux_Sed = vec4<f32>(
    NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),
    NumericalFlux(aplus, aminus, hW_east * uW_east * c2W_east, h_here.y * u_here.y * c2_here.y, phix * (hW_east * c2W_east - h_here.y * c2_here.y)),
    NumericalFlux(aplus, aminus, hW_east * uW_east * c3W_east, h_here.y * u_here.y * c3_here.y, phix * (hW_east * c3W_east - h_here.y * c3_here.y)),
    NumericalFlux(aplus, aminus, hW_east * uW_east * c4W_east, h_here.y * u_here.y * c4_here.y, phix * (hW_east * c4W_east - h_here.y * c4_here.y))
);
```

렌더 노트의 `note_date`도 2026-06-15다.
`git log --follow -p -- shaders/vertex3D.wgsl`의 마지막 변경은 2025-06-12 `7fa28e0`이다.
현 원문의 `shaders/vertex3D.wgsl:78`은 다음과 같다.

```wgsl
var elev = textureLoad(etaTexture, vec2<i32>(i32(out.uv.x * f32(globals.WIDTH - 1)), i32(out.uv.y * f32(globals.HEIGHT - 1))), 0).r;
```

이 직접 읽기는 노트 날짜보다 앞선 판에도 존재한다.
따라서 두 문장의 오류는 transect 분기나 2026년 이후 기능 추가로 설명되지 않는다.
이 보고서는 논문 본문의 식을 새로 판정하지 않았다.
논문 노트의 기존 서지·초록 주장은 그대로 원래 자료의 주장으로 남긴다.


### 4.2 추가 확인한 한쪽 결함 수정

#### CT1-220 퇴적물 limiter 한쪽 수정

반대 근거 확인: transect 식은 유효한 기존 ramp 식이다. 본판의 고정 TWO_THETAc=2.0은 사용자 Theta 변경을 무시한다. 이 원문만으로 transect가 항상 불안정하다고 단정하지 않는다.

확인한 모순: 본판 7fa28e0의 bug fixes는 이 식을 2.0 고정으로 바꿨다. transect 판에는 변경이 없다. 수리 Pass1의 limiter와 표사 Pass1의 limiter가 같은 판에서 서로 다른 안정화 선택을 쓰게 된다. 한쪽만 고친 결함 수정은 E로 두라는 사용자 지시를 적용한다. 수정 목적의 세부 수치 검증은 수행하지 않았다.

근거 강도: 중간.

#### CT1-248 중심 지형변화 표시 채널

반대 근거 확인: transect 판은 북쪽 면의 변화량도 실제로 계산하므로 r 채널이 항상 0인 것은 아니다. 표시 값이 항상 0이라고 쓰지 않는다.

확인한 모순: 바닥고 패킹의 r은 북쪽 면이고 b는 셀 중심이다. transect surface 21은 r을 읽는다. 같은 판의 dx/dy 및 중심 기반 표면 출력과 위치가 다르다. 본판 3d8a61b는 같은 줄을 r에서 b로 수정했다. 독립 y 단면의 중심 변화량을 표시하려는 목적에는 b가 맞는다.

근거 강도: 중간.

#### CT1-249·CT1-253 렌더 격자 길이와 고도 읽기 한쪽 수정

반대 근거 확인: 호스트 simWidth는 여전히 WIDTH*dx를 카메라 척도로 쓴다. 따라서 W*dx라는 곱 전체를 물리적 오류로 분류하지 않는다. 여기서는 렌더 격자점 끝 좌표에 한정한다.

확인한 모순: 두 판은 W개 인덱스 0..W-1의 상태장을 저장한다. MATLAB reader도 마지막 x를 (nx-1)*dx로 둔다. transect vertex의 끝점은 W*dx이므로 상태장 끝 좌표와 한 간격 다르다. 본판 7fa28e0의 bug fixes는 fragment와 vertex3D를 함께 W-1/H-1로 고쳤고 직접 etaTexture 읽기로 바꿨다. 한쪽 결함 수정은 E로 둔다.

근거 강도: 중간.

`7fa28e0`의 저자 날짜는 2025-06-12다.
해당 커밋의 UTC 시각은 다음 날이지만 이 보고서의 날짜 표시는 `git log --date=short`의 저자 날짜로 통일한다.


### 4.3 혼합 diff 구간에서 분리한 세부 판정

한 diff 구간에 서로 다른 의미가 있는 경우 다음 행으로 결론을 분리한다.
CT1-182의 F 결론은 수리 flux의 1D 환원에 한정한다.
그 구간의 퇴적물 확산 차이는 아래 A 행이다.

#### CT1-373 표준 Pass2의 퇴적물 확산과 phi

| 문서·코드 근거 | 판정 | 이유·노트 수정안 |
|---|---|---|
| `shaders/Pass2.wgsl:190` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),` / `transect_version/shaders/Pass2.wgsl:165`는 CT1-182의 전체 diff 참조. | A | 본판 표준 Pass2는 class 1의 x·y flux에 -k*h*grad(C)를 더한다. 본판은 퇴적물 flux 직전에 phix=phiy=0.5로 다시 설정한다. transect 판은 x 순수 이류 flux를 쓰고 수리 near-dry 분기에서 정한 phix를 유지한다. 이 차이는 수리 flux의 1D 동등성에 포함되지 않는다. |

#### CT1-374 두 면 통계 평균의 1D 동등성

| 문서·코드 근거 | 판정 | 이유·노트 수정안 |
|---|---|---|
| `transect_version/shaders/CalcMeans.wgsl:42` `let h = (h4.y + h4.w) / 2.0;` / CT1-163의 전체 diff. | F | 북·남 두 면의 본판 속도가 각 동·서 면 평균과 같다면 네 면 평균은 두 x 면 평균과 같다. transect의 h·u·c 평균은 이 두 면 평균을 명시한다. 실제 txNewState에서 읽는 본판 eta와 h+bottom으로 만든 transect eta는 별도 A 차이다. |

#### CT1-375 transect 셰이더 URL 접두어

| 문서·코드 근거 | 판정 | 이유·노트 수정안 |
|---|---|---|
| `transect_version/js/main.js:1031` `const Pass0_ShaderCode = await fetchShader('/transect_version/shaders/Pass0.wgsl');` / CT1-285. | C | transect main은 모든 셰이더 URL을 /transect_version/shaders 아래에서 읽는다. 이 URL은 문서 루트에 transect_version 경로가 존재한다고 가정한다. 계산식 변경과 배포 경로 변경을 분리해서 적는다. |

#### CT1-376 pulse 지속 길이와 trough 배율

| 문서·코드 근거 | 판정 | 이유·노트 수정안 |
|---|---|---|
| `shaders/BoundaryPass.wgsl:176` `num_waves = 5;` / `transect_version/shaders/BoundaryPass.wgsl:165`의 전체 이어진 조건은 CT1-156 참조. | A | transect pulse는 4주기이고 본판 pulse는 5주기다. 본판은 음의 eta에만 trough_factor를 곱한다. 본판 bb99fee의 2026-07-02 변경은 transect의 1D 미분 제거와 별개의 입사 파형 변경이다. |

#### CT1-377 본판 pulse UI의 4 waves 오기

| 문서·코드 근거 | 판정 | 이유·노트 수정안 |
|---|---|---|
| `index.html:766` `<option value="2">*Transient Pulse (4 waves)</option>` / `shaders/BoundaryPass.wgsl:176` `num_waves = 5;` | B | 본판 index의 pulse label은 4 waves지만 같은 판 BoundaryPass는 num_waves=5를 사용한다. 두 파일은 같은 ebca435 판이다. label의 별표는 미지원 안내지만 활성 incident_wave_type==2의 수치 5를 4로 바꾸지 않는다. 노트에는 UI 표시와 구현의 수량 불일치를 적는다. |

#### CT1-378 단면 입사파의 국소 수심

| 문서·코드 근거 | 판정 | 이유·노트 수정안 |
|---|---|---|
| `shaders/BoundaryPass.wgsl:190` `let B_here = -globals.base_depth; //textureLoad(txBottom, idx, 0).b;` / `transect_version/shaders/BoundaryPass.wgsl:175`의 전체 diff는 CT1-156 참조. | C | transect BoundarySineWave는 해당 행·해당 경계 셀의 바닥고를 쓴다. 본판은 -base_depth를 쓴다. 따라서 단면마다 경계 수심이 다르면 파수와 운동량의 크기도 단면마다 달라진다. 이 선택은 단지 y 위상을 0으로 둔 대수적 환원과 다르다. |

본판 pulse label의 문자열 이력은 2024-04-23 `48357ce`와 2024-04-25 `a9a18ea`를 포함한다.
`git log -S'num_waves = 5' -- shaders/BoundaryPass.wgsl`은 2026-07-02 `bb99fee`를 반환한다.
현재 같은 판 안에 수량 불일치가 남으므로 B로 둔다.


### 4.4 비활성 출력 함수의 추가 결함 후보

#### CT1-379 비활성 GeoTIFF 호출의 readback 인자

본판 readTextureData는 네 번째 인자로 버퍼를 받는다. 같은 본판 downloadGeoTiffData는 그 자리에 dx를 넘긴다. 이 API 불일치는 09cfd76의 공용 버퍼 변경 뒤 남은 결함 후보다. 현재 실행 경로에서 호출되지 않음. 본판 주석도 not used needs updates to be used라고 명시한다. 근거 강도는 강함이다.

`js/File_Writer.js:41` `const data = await readTextureData(device, texture, channel,dx,dy); // This should be compatible with the values expected by writeArrayBuffer` / `js/File_Writer.js:20` `await buffer.mapAsync(GPUMapMode.READ);`

`js/File_Writer.js:4`는 `export async function readTextureData(device, src_texture, channel, buffer) {`다.
`js/File_Writer.js:38`은 `// geotiff writer  // not used needs updates to be used`다.
`rg -n 'downloadGeoTiffData' js transect_version/js`는 두 함수 정의와 두 main.js의 주석 호출만 반환한다.
`git log -S'function readTextureData(device, src_texture, channel, buffer)' -- js/File_Writer.js`는 2026-02-15 `09cfd76`을 반환한다.
transect의 세 인자 readTextureData는 추가 dx·dy 인자를 무시하므로 이 특정 인자 불일치는 본판 공용 버퍼 변경과 연결된다.
GeoTIFF 외부 라이브러리 내부는 판독하지 않았다.

측정점 행 정렬 후보 `CT1-057`에는 추가 반대 근거가 있다.
transect constants의 maxNumberOfTimeSeries 주석은 `SHould be 16*N time series`라고 적는다.
이 사전조건을 지키면 행 정렬이 맞으므로 해당 후보의 근거 강도를 약함으로 낮춘다.
본판이 정렬식을 보강한 사실은 E 분류로 유지한다.


## 5 차이 결론

분류 개수는 아래 결론 표의 행 ID를 센 값이다.
같은 결함 후보를 가리키는 호스트·바인딩·셰이더·노트 행도 각각 센다.
따라서 E 행 수는 독립 결함 수가 아니다.
2.50절과 4.2절은 E의 반대 근거와 강도를 구분한다.
4.4절은 비활성 출력 함수의 E를 추가한다.

A의 비교 시점은 본판 `ebca435`와 각 transect 파일의 실제 변경 이력이다.
2017·2020 논문의 이전 플랫폼과 2026 WebGPU 논문의 차이를 이 두 코드 판의 연대 차이로 대신 쓰지 않았다.
본판 전용 파일은 해당 파일의 실제 도입 커밋이 있으므로 A로 판정했다.
이 보고서에는 D 판정이 없다.
따라서 D의 외부 부재를 입증했다고 주장하지 않는다.
H와 X 판정도 없다.
의도된 1D 단순화는 F 또는 C로 판정했다.

F는 각 단면을 y 방향으로 일정하게 연장하고 Q=0으로 둔 경우의 환원을 뜻한다.
서로 다른 y행의 단면 자료를 본판의 단일 2D 장으로 붙여도 결과가 같다는 뜻이 아니다.
두 면 통계 평균의 F는 그 행에 적은 추가 면값 조건도 요구한다.
쇄파 점성 상한의 dx*dy→dx*dx 변경은 일반적으로 같지 않으므로 C다.

`git log --follow -p`는 비교 대상의 양쪽 현재 경로마다 실행했다.
과거 줄 번호가 필요한 핵심 결함은 `git show HASH:파일`로 다시 확인했다.
아래 이력의 줄 귀속은 기능의 최초 도입과 구분한다.
분기 전에 있던 본판 줄과 transect의 다른 줄 사이 차이는 최초 transect 추가 때부터 존재한다.
행의 마지막 변경 HASH만 보고 그 HASH가 기능의 최초 도입이라고 단정하지 않는다.

이 표의 분류별 개수: A 168, B 3, C 43, D 0, E 45, F 120, H 0, X 0. 합계 379행.

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| CT1-001 | index.html 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–1309, 1371–1601. transect CRLF 행: 없음. | 본판의 CRLF 1540개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-002 | js/Config_Pipelines.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–283. transect CRLF 행: 없음. | 본판의 CRLF 283개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-003 | js/Copy_Data_to_Textures.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–131, 192–349, 408–637. transect CRLF 행: 없음. | 본판의 CRLF 519개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-004 | js/Create_Textures.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–100. transect CRLF 행: 없음. | 본판의 CRLF 100개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-005 | js/File_Loader.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–266, 268–300, 516–615, 653–819. transect CRLF 행: 없음. | 본판의 CRLF 566개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-006 | js/File_Writer.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–612, 617–631, 846–848. transect CRLF 행: 없음. | 본판의 CRLF 630개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-007 | js/Handler_AddDisturbance.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–120. transect CRLF 행: 없음. | 본판의 CRLF 120개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-008 | js/Handler_BoundaryPass.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–86, 141–181. transect CRLF 행: 없음. | 본판의 CRLF 127개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-009 | js/Handler_CalcMeans.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–199. transect CRLF 행: 없음. | 본판의 CRLF 199개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-010 | js/Handler_CalcWaveHeight.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–92. transect CRLF 행: 없음. | 본판의 CRLF 92개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-011 | js/Handler_ExtractTimeSeries.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–132. transect CRLF 행: 없음. | 본판의 CRLF 132개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-012 | js/Handler_MouseClickChange.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–119. transect CRLF 행: 없음. | 본판의 CRLF 119개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-013 | js/Handler_Pass0.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–68. transect CRLF 행: 없음. | 본판의 CRLF 68개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-014 | js/Handler_Pass1.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–110. transect CRLF 행: 없음. | 본판의 CRLF 110개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-015 | js/Handler_Pass2.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–227. transect CRLF 행: 없음. | 본판의 CRLF 227개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-016 | js/Handler_Pass3.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–572. transect CRLF 행: 없음. | 본판의 CRLF 572개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-017 | js/Handler_Render.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–391. transect CRLF 행: 없음. | 본판의 CRLF 391개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-018 | js/Handler_SedTrans_Pass1.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–123. transect CRLF 행: 없음. | 본판의 CRLF 123개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-019 | js/Handler_SedTrans_Pass3.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–253. transect CRLF 행: 없음. | 본판의 CRLF 253개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-020 | js/Handler_SedTrans_UpdateBottom.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–134. transect CRLF 행: 없음. | 본판의 CRLF 134개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-021 | js/Handler_Tridiag.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–108. transect CRLF 행: 없음. | 본판의 CRLF 108개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-022 | js/Handler_UpdateTrid.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–80. transect CRLF 행: 없음. | 본판의 CRLF 80개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-023 | js/Handler_Updateneardry.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–53. transect CRLF 행: 없음. | 본판의 CRLF 53개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-024 | js/Run_Compute_Shader.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–89. transect CRLF 행: 없음. | 본판의 CRLF 89개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-025 | js/Run_Tridiag_Solver.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–17, 36–43, 49–53, 64–68, 74–78, 89–93. transect CRLF 행: 없음. | 본판의 CRLF 45개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-026 | js/Time_Series.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–57, 62–97, 114–184. transect CRLF 행: 없음. | 본판의 CRLF 164개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-027 | js/constants_load_calc.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–76, 99–254, 263–369, 398–573, 602–664. transect CRLF 행: 없음. | 본판의 CRLF 578개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-028 | js/display_parameters.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–119, 142–231, 242–250. transect CRLF 행: 없음. | 본판의 CRLF 218개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-029 | js/main.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–2, 9–11, 16–36, 42–194, 198–205, 215–217, 221–247, 264–289, 301–328, 391–407, 415–560, 578–586, 598–1152, 1161–1204, 1219–1391, 1415–1597, 1605–1636, 1644–1716, 1721–1724, 1738–1770, 2213–2401, 2420–2483, 2496–2600, 2613–2621, 2625–2626, 2634–2886, 2898–2929, 2981–3467, 3511–3515, 3520–3989, 3996–3999, 4079–4273, 4285–4664, 4671–4726, 4744–5123, 5141–5237, 5250–5277, 5287–5309, 5316–5319, 5326–5335, 5339–5346, 5352–5469, 5476–5489. transect CRLF 행: 없음. | 본판의 CRLF 4473개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-030 | js/site.js 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–4. transect CRLF 행: 없음. | 본판의 CRLF 4개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-031 | shaders/AddDisturbance.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–241. transect CRLF 행: 없음. | 본판의 CRLF 241개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-032 | shaders/BoundaryPass.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–725. transect CRLF 행: 없음. | 본판의 CRLF 725개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-033 | shaders/CalcMeans.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–104. transect CRLF 행: 없음. | 본판의 CRLF 104개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-034 | shaders/CalcWaveHeight.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–77. transect CRLF 행: 없음. | 본판의 CRLF 77개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-035 | shaders/ExtractTimeSeries.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–65. transect CRLF 행: 없음. | 본판의 CRLF 65개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-036 | shaders/MouseClickChange.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–13, 28–57, 63–64, 106–125, 141–197, 243–245. transect CRLF 행: 없음. | 본판의 CRLF 125개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-037 | shaders/Pass0.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–60. transect CRLF 행: 없음. | 본판의 CRLF 60개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-038 | shaders/Pass1.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–172. transect CRLF 행: 없음. | 본판의 CRLF 172개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-039 | shaders/Pass2.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–206. transect CRLF 행: 없음. | 본판의 CRLF 206개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-040 | shaders/Pass3_Bous.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–430. transect CRLF 행: 없음. | 본판의 CRLF 430개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-041 | shaders/Pass3_NLSW.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–285. transect CRLF 행: 없음. | 본판의 CRLF 285개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-042 | shaders/SedTrans_Pass1.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–135. transect CRLF 행: 없음. | 본판의 CRLF 135개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-043 | shaders/SedTrans_Pass3.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–240. transect CRLF 행: 없음. | 본판의 CRLF 240개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-044 | shaders/SedTrans_UpdateBottom.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–122. transect CRLF 행: 없음. | 본판의 CRLF 122개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-045 | shaders/Ship_pressure.compute 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–81. transect CRLF 행: 없음. | 본판의 CRLF 81개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-046 | shaders/TriDiag_PCRx.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–2, 9–19, 24–92, 107. transect CRLF 행: 없음. | 본판의 CRLF 83개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-047 | shaders/TriDiag_PCRy.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–2, 9–19, 24–92. transect CRLF 행: 없음. | 본판의 CRLF 82개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-048 | shaders/Update_TriDiag_coef.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–111. transect CRLF 행: 없음. | 본판의 CRLF 111개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-049 | shaders/Update_neardry.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–56. transect CRLF 행: 없음. | 본판의 CRLF 56개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-050 | shaders/fragment.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–54, 69–797, 856–928. transect CRLF 행: 없음. | 본판의 CRLF 856개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-051 | shaders/vertex.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–19. transect CRLF 행: 없음. | 본판의 CRLF 19개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-052 | shaders/vertex3D.wgsl 줄바꿈 | F 표기 차이 | 본판 CRLF 행: 1–85. transect CRLF 행: 없음. | 본판의 CRLF 85개와 transect 판의 CRLF 0개는 물리식과 자료 값을 바꾸지 않는다. |
| CT1-053 | js/Copy_Data_to_Textures.js 구간 1 초기 지형 전처리와 북쪽 면 | C 문서 누락 | `ebca435:js/Copy_Data_to_Textures.js:15` `let change_point = 1.;` / `ebca435:transect_version/js/Copy_Data_to_Textures.js:40` `let BN = 0.0; // should not be used. 0.5 * bathy2D[x][y] + 0.5 * bathy2D[x][Math.min(calc_constants.HEIGHT - 1, y + 1)];` | transect 판은 단일점 섬 제거를 주석 처리한다. transect 판은 북쪽 면 고도 BN을 0.0으로 저장한다. 이는 본판 전처리의 보존이 아니라 단면 전용 선택이다. |
| CT1-054 | js/Copy_Data_to_Textures.js 구간 2 near-dry CPU 검사 | F 표기 차이 | `ebca435:js/Copy_Data_to_Textures.js:50` `for (let yy = y - lengthCheck; yy <= y + lengthCheck; ++yy) {` / `ebca435:transect_version/js/Copy_Data_to_Textures.js:55` `if (bathy2D[xC][y] >= 0) {` | 본판은 x·y 각각 ±3칸을 검사한다. transect 판은 같은 행의 x ±3칸만 검사한다. 독립 단면에서 검사 대상은 7개 x 위치로 줄어든다. |
| CT1-055 | js/Copy_Data_to_Textures.js 구간 3 단면별 파랑 업로드 | C 문서 누락 | 삭제 줄 없음 / `ebca435:transect_version/js/Copy_Data_to_Textures.js:93` `function copyTransectWaveDataToTexture(calc_constants, waveData, device, txWaves_Transect) {` | transect 판은 numberOfWaves × HEIGHT 텍스처를 만든다. 입력의 첫 HEIGHT행은 진폭이다. 다음 HEIGHT행은 주기다. 마지막 HEIGHT행은 위상이다. 방향 채널은 0.0이다. bytesPerRow는 256배수로 올림한다. |
| CT1-056 | js/Copy_Data_to_Textures.js 구간 4 경계 시계열 업로드와 위치 업로드 | A 판 차이 | `ebca435:js/Copy_Data_to_Textures.js:137` `function copyBoundaryTimeSeriesDataToTexture(boundaryTimeSeriesSideData, device, txBoundaryTimeSeries) {` / `ebca435:transect_version/js/Copy_Data_to_Textures.js:180` `function copyTSlocsToTexture(calc_constants, device, txTimeSeries_Locations) {` 이력 본판: `bb99fee` 2026-07-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 경계 관측점·시간·eta/hu/hv를 RGBA32F 텍스처로 패킹한다. transect 판은 이 자리에 측정점 위치 업로드를 둔다. 두 함수는 같은 함수의 이름 변경이 아니다. |
| CT1-057 | js/Copy_Data_to_Textures.js 구간 5 측정점 업로드 정렬과 초기상태 인자 | E 코드 결함 후보 (약함) | `ebca435:js/Copy_Data_to_Textures.js:176` `rowsPerImage: textureHeight,` / `ebca435:transect_version/js/Copy_Data_to_Textures.js:212` `rowsPerImage: 1,` 반대 근거·두 경로 대조: 측정점 행 정렬 절. | transect 판은 requiredBytesPerRow를 maxNumberOfTimeSeries*16 그대로 둔다. 본판은 256배수로 올림한다. 기본 측정점 수 16에서는 두 값이 같다. 16의 배수가 아닌 수에서는 transect의 복사 정렬과 자기 주석이 모순한다. 초기상태 함수의 writeStateFlag 제거는 별도의 구판 인터페이스 차이다. |
| CT1-058 | js/Copy_Data_to_Textures.js 구간 6 초기 수면과 속도 채널 | A 판 차이 | `ebca435:js/Copy_Data_to_Textures.js:261` `var eta = 0.; // * Math.exp(-(dx * dx + dy * dy) / (2 * sigma * sigma));` / `ebca435:transect_version/js/Copy_Data_to_Textures.js:240` `let dx = x - calc_constants.WIDTH / 10.;` 이력 본판: `32be94a` 2025-10-16; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 writeStateFlag 1/2/3으로 eta/u/v 입력을 구분한다. transect 판은 river_sim==1 또는 loadFriction==1에서만 첫 채널에 입력장을 쓴다. 나머지 두 운동량 채널은 0.0이다. 진폭 0.0인 가우스 식은 유한한 격자에서 0.0이다. |
| CT1-059 | js/Copy_Data_to_Textures.js 구간 7 구면 계량 업로드 없음 | A 판 차이 | `ebca435:js/Copy_Data_to_Textures.js:351` `function copySphericalMetricDataToTexture(calc_constants, device, txSphericalMetrics) {` / 추가 줄 없음 이력 본판: `afc1fe7` 2026-06-19; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 셀 중심 위도·북쪽 면·남쪽 면의 계량을 RGBA32F로 저장한다. transect 판에는 구면 격자 경로가 없다. |
| CT1-060 | js/Copy_Data_to_Textures.js 구간 8 업로드 함수 공개 목록 | C 문서 누락 | `ebca435:js/Copy_Data_to_Textures.js:642` `export { copyBathyDataToTexture, copyWaveDataToTexture, copyBoundaryTimeSeriesDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copySphericalMetricDataToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture};` / `ebca435:transect_version/js/Copy_Data_to_Textures.js:555` `export { copyBathyDataToTexture, copyTransectWaveDataToTexture, copyWaveDataToTexture, copyTSlocsToTexture, copyInitialConditionDataToTexture, copyConstantValueToTexture, copyTridiagXDataToTexture, copyTridiagYDataToTexture, copyImageBitmapToTexture};` | transect 판은 copyTransectWaveDataToTexture를 export한다. 본판은 경계 시계열과 구면 계량 함수를 export한다. |
| CT1-061 | index.html 구간 1 페이지 제목 | C 문서 누락 | `ebca435:index.html:8` `<title>Celeris-WebGPU</title>` / `ebca435:transect_version/index.html:8` `<title>Celeris-WebGPU: Transect Mode</title>` | transect 판은 제목에 Transect Mode를 표시한다. |
| CT1-062 | index.html 구간 2 경계 파일 UI 스타일 | A 판 차이 | `ebca435:index.html:120` `/* Added by Codex: Start compact boundary time-series upload controls. */` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 경계 시계열 업로드 행의 CSS를 정의한다. |
| CT1-063 | index.html 구간 3 사용자 포럼 링크 | A 판 차이 | `ebca435:index.html:204` `<b>Questions/Problems/Requests </b> - use the <a href="https://celeris.discourse.group/categories" target="_blank" rel="noopener noreferrer">Users Forum</a>` / `ebca435:transect_version/index.html:191` `<b>Questions/Problems/Requests </b> - use the <a href="https://www.sqrtgh.com/forum" target="_blank" rel="noopener noreferrer">Users Forum</a>` 이력 본판: `794c808` 2026-04-06; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 discourse 주소를 쓴다. transect 판은 sqrtgh 포럼 주소를 쓴다. 링크 문자열만 대조하며 외부 사이트 내용은 판독하지 않는다. |
| CT1-064 | index.html 구간 4 추가 입력 파일 | A 판 차이 | `ebca435:index.html:238` `<input type="file" id="etaInitialConditionFile" accept="application/txt" style="display: none;" />` / 추가 줄 없음 이력 본판: `32be94a` 2025-10-16, `b8b50c3` 2025-06-08, `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 초기 수면·hardbottom·4변 경계 시계열 업로드와 자료 형식 안내를 제공한다. 마찰 파일 입력은 양쪽에 남아 있다. |
| CT1-065 | index.html 구간 5 예제 선택 숨김 | C 문서 누락 | `ebca435:index.html:311` `<html4f>` / `ebca435:transect_version/index.html:262` `<label style="display: none;" for="run_example-select">Choose Example:</label>` | transect 판은 예제 label과 select를 display:none으로 숨긴다. |
| CT1-066 | index.html 구간 6 예제 선택 항목 | A 판 차이 | `ebca435:index.html:337` `<option value="42">Sebastian Inlet (FL), wind waves</option>` / 추가 줄 없음 이력 본판: `ea93d70` 2025-10-24, `afc1fe7` 2026-06-19, `8c2b62b` 2025-08-24, `146a4ac` 2025-09-28, `32be94a` 2025-10-16; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판의 후속 예제 option이 transect 판에는 없다. 예제 내부 자료는 판독하지 않는다. |
| CT1-067 | index.html 구간 7 예제 실행 버튼 숨김 | C 문서 누락 | `ebca435:index.html:361` `</select>` / `ebca435:transect_version/index.html:300` `</select>` | transect 판은 예제 실행 버튼을 숨긴다. 직접 파일 입력 실행은 남긴다. |
| CT1-068 | index.html 구간 8 가용 깊이 표시 항목 | A 판 차이 | `ebca435:index.html:423` `<option value="19">Sediment Class 1 Available Depth </option>` / 추가 줄 없음 이력 본판: `b8b50c3` 2025-06-08; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 surfaceToPlot 19를 제공한다. |
| CT1-069 | index.html 구간 9 천단고 UI 활성 상태 | A 판 차이 | `ebca435:index.html:628` `<label for="designcomponent_CrestElev-input">For linear structures (breakwaters, dunes, seawalls), crest elevation (m):</label>` / `ebca435:transect_version/index.html:558` `<label for="designcomponent_CrestElev-input">*For linear structures (breakwaters, dunes, seawalls), crest elevation (m):</label>` 이력 본판: `d778fe7` 2026-06-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 별표를 붙여 미지원임을 표시한다. 본판은 실제 선형 구조물 경로를 구현한다. |
| CT1-070 | index.html 구간 10 천단폭 UI 활성 상태 | A 판 차이 | `ebca435:index.html:636` `<label for="designcomponent_CrestWidth-input">For linear structures (breakwaters, dunes, seawalls), crest width (m):</label>` / `ebca435:transect_version/index.html:566` `<label for="designcomponent_CrestWidth-input">*For linear structures (breakwaters, dunes, seawalls), crest width (m):</label>` 이력 본판: `d778fe7` 2026-06-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 별표를 붙인다. 본판은 해당 폭을 실제 지형 편집에 쓴다. |
| CT1-071 | index.html 구간 11 사면경사 UI 활성 상태 | A 판 차이 | `ebca435:index.html:644` `<label for="designcomponent_SideSlope-input">For linear, sloping structures (breakwaters, dunes), side slope (give as decimal, e.g. 0.25 = 1/4):</label>` / `ebca435:transect_version/index.html:574` `<label for="designcomponent_SideSlope-input">*For linear, sloping structures (breakwaters, dunes), side slope (give as decimal, e.g. 0.25 = 1/4):</label>` 이력 본판: `d778fe7` 2026-06-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 별표를 붙인다. 두 판의 안내 예시 0.25=1/4는 같다. |
| CT1-072 | index.html 구간 12 끝점 선택 UI 활성 상태 | A 판 차이 | `ebca435:index.html:652` `<label for="designcomponent_CurrentEndPoint-select">Choose Linear Structure Start/Endpoint Coordinate to Edit:</label>` / `ebca435:transect_version/index.html:582` `<label for="designcomponent_CurrentEndPoint-select">*Choose Linear Structure Start/Endpoint Coordinate to Edit:</label>` 이력 본판: `d778fe7` 2026-06-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 별표를 붙인다. 본판은 끝점 선택을 실제 편집에 연결한다. |
| CT1-073 | index.html 구간 13 끝점 입력 안내 | A 판 차이 | `ebca435:index.html:661` `Right-click on structure start/end location (in Design Mode) or input coordinates below</a>` / `ebca435:transect_version/index.html:591` `*Right-click on structure start/end location (in Design Mode) or input coordinates below</a>` 이력 본판: `d778fe7` 2026-06-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 우클릭 입력 안내에 별표를 붙인다. 실제 선형 구조물 적용 경로는 없다. |
| CT1-074 | index.html 구간 14 내장 파 생성 UI | A 판 차이 | `ebca435:index.html:764` `<option value="0">Sine Wave (single harmonic)</option>` / `ebca435:transect_version/index.html:694` `<option value="0">*Sine Wave (single harmonic)</option>` 이력 본판: `9093d7f` 2026-06-01; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 Sine와 TMA에 별표를 붙인다. 본판은 공유 파 생성 모듈을 호출한다. pulse 안내의 4 waves 문자열은 양쪽에 남아 있다. |
| CT1-075 | index.html 구간 15 입사 방향 문구 | F 표기 차이 | `ebca435:index.html:791` `<label for="incident_wave_direction-input">Wave Direction (deg, 0=from west, 90=from south, 180=from east, -90/270=from north):</label>` / `ebca435:transect_version/index.html:721` `<label for="incident_wave_direction-input">Wave Direction (deg CCW from E [-180 to 180]):</label>` | 본판의 0=from west·90=from south는 양의 진행축이 동·북인 관례다. transect 문구의 CCW from E는 같은 진행 방향 관례다. 실제 단면 파일 방향 채널은 별도로 0.0으로 고정한다. |
| CT1-076 | index.html 구간 16 서쪽 type5 UI | A 판 차이 | `ebca435:index.html:805` `<!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 파일 시계열 경계를 선택할 수 있다. |
| CT1-077 | index.html 구간 17 동쪽 type5 UI | A 판 차이 | `ebca435:index.html:818` `<!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 파일 시계열 경계를 선택할 수 있다. |
| CT1-078 | index.html 구간 18 남쪽 type5 UI | A 판 차이 | `ebca435:index.html:831` `<!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 파일 시계열 경계를 선택할 수 있다. |
| CT1-079 | index.html 구간 19 북쪽 type5 UI | A 판 차이 | `ebca435:index.html:844` `<!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 파일 시계열 경계를 선택할 수 있다. |
| CT1-080 | index.html 구간 20 퇴적물 되먹임 안내 | C 문서 누락 | 삭제 줄 없음 / `ebca435:transect_version/index.html:786` `<html4f>` | transect 판은 BETA - currently no feedback w/ hydro라고 명시한다. 바닥고 고정은 이 안내에 맞는 의도된 처리다. |
| CT1-081 | index.html 구간 21 퇴적물 psi 문구 | F 표기 차이 | `ebca435:index.html:885` `<label for="sedC1_psi-input">Sediment Class 1 psi (erosion) parameter:</label>` / `ebca435:transect_version/index.html:813` `<label for="sedC1_psi-input">Sediment Class 1 psi parameter:</label>` | transect 판은 erosion이라는 괄호 설명을 생략한다. 같은 sedC1_psi 입력과 기본값을 가리킨다. |
| CT1-082 | index.html 구간 22 중첩 경계 출력 UI | A 판 차이 | `ebca435:index.html:1314` `<!-- Added by Codex: Start nested-grid boundary time-series output controls. -->` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02, `c4be488` 2026-07-13; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 0기반 사각형 인덱스·기간·간격·eta 임계값·실행 버튼을 제공한다. 다중 사각형은 JSON으로 추가한다. |
| CT1-083 | index.html 구간 23 모듈 진입 경로 | C 문서 누락 | `ebca435:index.html:1597` `<script type="module" src="js/main.js"></script>` / `ebca435:transect_version/index.html:1471` `<script type="module" src="/transect_version/js/main.js"></script>` | transect 판은 /transect_version/js/main.js를 로드한다. 본판은 상대 js/main.js를 로드한다. 루트 아래 배포를 가정하는 차이다. |
| CT1-084 | js/File_Loader.js 구간 1 초기 수면 파일 읽기 | A 판 차이 | `ebca435:js/File_Loader.js:86` `export async function loadInitCondSurface(InitCondContent, calc_constants) {` / 추가 줄 없음 이력 본판: `32be94a` 2025-10-16; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 etaInitCond.txt를 WIDTH열·HEIGHT행의 유한 수치장으로 읽는다. transect 판에는 이 함수가 없다. |
| CT1-085 | js/File_Loader.js 구간 2 hardbottom과 단면 파랑의 서로 다른 자료 형식 | C 문서 누락 | `ebca435:js/File_Loader.js:207` `export async function loadHardBottomSurface(fileContent, calc_constants) {` / `ebca435:transect_version/js/File_Loader.js:146` `export async function loadTransectWaveData(waveContent, calc_constants) {` | 본판 함수는 hardbottom.txt의 WIDTH×HEIGHT 고도를 읽는다. transect 함수는 waves.txt의 numberOfWaves열·3*HEIGHT행을 읽는다. 두 함수는 열 수와 반환 배열 크기가 다르다. |
| CT1-086 | js/File_Loader.js 구간 3 type-5 경계 자료 검사 | A 판 차이 | `ebca435:js/File_Loader.js:304` `function createEmptyBoundaryTimeSeriesSide() {` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 주석 제거·관측점 수·좌표 정렬·중복 검사·1+3*N 열 검사·시간 단조증가·공유 시간벡터 오차 검사·업로드 우선을 구현한다. transect 판에는 해당 경계 자료 경로가 없다. |
| CT1-087 | js/File_Loader.js 구간 4 지도 이미지 실패 처리 | E 코드 결함 후보 (강함) | `ebca435:js/File_Loader.js:623` `if (!response.ok) {` / `ebca435:transect_version/js/File_Loader.js:355` `await new Promise((resolve) => {` 반대 근거·두 경로 대조: 지도 실패 처리 절. | transect 판은 HTTP 상태와 MIME 형식을 검사하지 않는다. transect 판은 image.onerror도 설정하지 않는다. 본판은 실패를 reject한다. transect 판의 실패한 이미지 Promise는 초기화를 끝내지 못할 수 있다. |
| CT1-088 | js/File_Writer.js 구간 1 표면 readback 버퍼 수명 | E 코드 결함 후보 (중간) | `ebca435:js/File_Writer.js:4` `export async function readTextureData(device, src_texture, channel, buffer) {` / `ebca435:transect_version/js/File_Writer.js:3` `export async function readTextureData(device, src_texture, channel) {` 반대 근거·두 경로 대조: readback 버퍼 수명 절. | 본판은 전달받은 버퍼를 재사용하고 map 뒤 unmap한다. transect 판은 호출마다 버퍼를 만들고 반환 전에 unmap과 destroy를 하지 않는다. 반환 Float32Array는 별도 배열이므로 버퍼 유지가 결과 보존에 필요하지 않다. 인덱스 y*WIDTH+x와 channel-1은 같다. |
| CT1-089 | js/File_Writer.js 구간 2 JPEG 버퍼 정리 | E 코드 결함 후보 (중간) | `ebca435:js/File_Writer.js:184` `buffer.unmap(); // Don't forget to unmap the buffer once done` / 추가 줄 없음 반대 근거·두 경로 대조: readback 버퍼 수명 절. | 본판은 이미지 자료를 slice한 뒤 버퍼를 unmap하고 destroy한다. transect 판은 두 정리 호출이 없다. |
| CT1-090 | js/File_Writer.js 구간 3 이미지 슬라이스 버퍼 정리 | E 코드 결함 후보 (중간) | `ebca435:js/File_Writer.js:328` `buffer.unmap(); // Don't forget to unmap the buffer once done` / `ebca435:transect_version/js/File_Writer.js:355` `buffer.unmap();` 반대 근거·두 경로 대조: readback 버퍼 수명 절. | transect 판에는 destroy가 없다. 양쪽은 mapped view를 만든 뒤 unmap하므로 그 view의 수명 문제는 두 판의 공통 문제다. 이 행의 판간 차이는 destroy 유무다. |
| CT1-091 | js/File_Writer.js 구간 4 GIF 프레임 버퍼 정리 | E 코드 결함 후보 (중간) | `ebca435:js/File_Writer.js:418` `buffer.unmap(); // Don't forget to unmap the buffer once done` / `ebca435:transect_version/js/File_Writer.js:443` `buffer.unmap();` 반대 근거·두 경로 대조: readback 버퍼 수명 절. | 두 판은 slice 복사 후 unmap한다. transect 판에는 destroy가 없다. |
| CT1-092 | js/File_Writer.js 구간 5 애니메이션 버퍼 정리 | E 코드 결함 후보 (중간) | `ebca435:js/File_Writer.js:486` `buffer.unmap(); // Don't forget to unmap the buffer once done` / `ebca435:transect_version/js/File_Writer.js:509` `buffer.unmap();` 반대 근거·두 경로 대조: readback 버퍼 수명 절. | 두 판은 slice 복사 후 unmap한다. transect 판에는 destroy가 없다. |
| CT1-093 | js/File_Writer.js 구간 6 표면 출력 함수 인자 | A 판 차이 | `ebca435:js/File_Writer.js:531` `export async function writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities, buffer) {` / `ebca435:transect_version/js/File_Writer.js:553` `export async function writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities) {` 이력 본판: `09cfd76` 2026-02-15; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 공용 readback 버퍼를 전달한다. transect 판은 호출 안에서 버퍼를 만든다. bathytopo.bin의 채널 3과 첫 프레임 조건은 같다. |
| CT1-094 | js/File_Writer.js 구간 7 시간별 바닥고 출력과 표면 자료 | A 판 차이 | `ebca435:js/File_Writer.js:553` `if(calc_constants.useSedTransModel ==1 \|\| (total_time < 300.0 && calc_constants.disturbanceType == 5)){  // write depth if using sediment transport model or landslide` / `ebca435:transect_version/js/File_Writer.js:577` `await downloadTextureData(device, txState, 1, filename);  // number is the channel 1 = .r, 2 = .g, etc.` 이력 본판: `9ed86a6` 2026-02-17, `d852a23` 2025-06-11, `09cfd76` 2026-02-15; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 퇴적물 또는 total_time<300.0인 disturbanceType==5에서 depth_번호.bin을 출력한다. transect 판은 이 조건부 바닥고 출력을 하지 않는다. eta/P/Q/u/v/turb의 채널 번호·파일명·대기 순서는 같다. |
| CT1-095 | js/File_Writer.js 구간 8 바이너리 다운로드 인자 | A 판 차이 | `ebca435:js/File_Writer.js:599` `export async function downloadTextureData(device, texture, channel, filename, buffer) {` / `ebca435:transect_version/js/File_Writer.js:615` `export async function downloadTextureData(device, texture, channel, filename) {` 이력 본판: `09cfd76` 2026-02-15; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 readTextureData에 공용 버퍼를 전달한다. transect 판은 전달하지 않는다. Blob은 모두 application/octet-stream이다. |
| CT1-096 | js/File_Writer.js 구간 9 중첩 경계 출력 없음 | A 판 차이 | `ebca435:js/File_Writer.js:637` `async function readRgbaTextureData(device, src_texture, width, height) {` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02, `c4be488` 2026-07-13; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 4변 eta/hu/hv를 9자리 유효숫자로 저장한다. 본판은 임계 eta 이전 행을 잘라내도 절대 시간을 유지한다. 본판은 사각형별 파일 접두어와 임계값을 사용한다. transect 판에는 이 writer가 없다. |
| CT1-097 | js/Handler_AddDisturbance.js 구간 1 지형변화 누적 입력 누락 | E 코드 결함 후보 (약함) | `ebca435:js/Handler_AddDisturbance.js:70` `binding: 7,` / `ebca435:transect_version/js/Handler_AddDisturbance.js:72` `export function create_AddDisturbance_BindGroup(device, uniformBuffer, txBottom, txState, txBottomInitial, txtemp_AddDisturbance, txBoundaryForcing, txtemp_bottom) {` 반대 근거·두 경로 대조: 교란과 누적 침식의 결합 절. | transect 판은 binding 7의 txBotChange_Sed를 제공하지 않는다. 본판은 교란 지형과 누적 침식량의 합을 보존하도록 이 바인딩을 추가했다. 1D 미분 제거와 무관한 한쪽 결함 수정이다. |
| CT1-098 | js/Handler_AddDisturbance.js 구간 2 누적 지형변화 리소스 누락 | E 코드 결함 후보 (약함) | `ebca435:js/Handler_AddDisturbance.js:116` `binding: 7,` / 추가 줄 없음 반대 근거·두 경로 대조: 교란과 누적 침식의 결합 절. | transect 판에는 txBotChange_Sed.createView()가 없다. 대응 셰이더도 누적 지형변화를 읽지 않는다. 본판의 Sed bugs / corrections 이력과 함께 판정한다. |
| CT1-099 | js/Handler_BoundaryPass.js 구간 1 단면 파랑과 경계 시계열 바인딩 | C 문서 누락 | `ebca435:js/Handler_BoundaryPass.js:99` `binding: 10,` / `ebca435:transect_version/js/Handler_BoundaryPass.js:100` `export function create_BoundaryPass_BindGroup(device, uniformBuffer, current_stateUVstar, txBottom, txWaves, txNewState_Sed, txtemp, txtemp_Sed, txBreaking, txtemp_Breaking, txWaves_Transect) {` | 본판은 binding 9에 txBoundaryForcing을 둔다. 본판은 binding 10–13에 4변 경계 시계열을 둔다. transect 판은 binding 9에 txWaves_Transect를 둔다. 같은 번호의 리소스 의미가 다르다. |
| CT1-100 | js/Handler_BoundaryPass.js 구간 2 경계 바인드 그룹 리소스 | C 문서 누락 | `ebca435:js/Handler_BoundaryPass.js:184` `resource: txBoundaryForcing.createView()` / `ebca435:transect_version/js/Handler_BoundaryPass.js:144` `resource: txWaves_Transect.createView()` | transect 판의 binding 9는 단면 행별 파랑을 읽는다. 본판은 경계 강제장과 시계열을 별개 리소스로 둔다. |
| CT1-101 | js/Handler_CalcMeans.js 구간 1 통계용 실제 수면 입력 | A 판 차이 | `ebca435:js/Handler_CalcMeans.js:125` `binding: 13,` / `ebca435:transect_version/js/Handler_CalcMeans.js:127` `export function create_CalcMeans_BindGroup(device, uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC) {` 이력 본판: `dc6cc2d` 2025-08-10; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 binding 13의 txNewState를 추가했다. transect 판은 재구성 수심 평균으로 수면을 산출한다. 이는 평균·최대 eta의 자료원이 다른 차이다. |
| CT1-102 | js/Handler_CalcMeans.js 구간 2 통계 바인드 그룹 | A 판 차이 | `ebca435:js/Handler_CalcMeans.js:195` `binding: 13,` / 추가 줄 없음 이력 본판: `dc6cc2d` 2025-08-10; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판에는 txNewState.createView()가 없다. 대응 CalcMeans 셰이더의 eta 산출식과 일치한다. |
| CT1-103 | js/Handler_Copytxf32_txf16.js 구간 1 불투수 바닥 표시 입력 | A 판 차이 | `ebca435:js/Handler_Copytxf32_txf16.js:78` `binding: 8,` / `ebca435:transect_version/js/Handler_Copytxf32_txf16.js:81` `export function create_Copytxf32_txf16_BindGroup(device, uniformBuffer, txNewState, txBottom, txMeans_Speed, txRenderVarsf16, txMeans_Momflux, txModelVelocities, txMeans) {` 이력 본판: `b8b50c3` 2025-06-08; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 binding 8의 txHardBottom을 제공한다. transect 판은 표시용 텍스처를 두 레이어만 쓴다. |
| CT1-104 | js/Handler_Copytxf32_txf16.js 구간 2 불투수 바닥 리소스 | A 판 차이 | `ebca435:js/Handler_Copytxf32_txf16.js:129` `binding: 8,` / `ebca435:transect_version/js/Handler_Copytxf32_txf16.js:121` `}` 이력 본판: `b8b50c3` 2025-06-08; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판에는 txHardBottom.createView()가 없다. 본판의 가용 퇴적층 깊이 표시와 연결된다. |
| CT1-105 | js/Handler_ExtractTimeSeries.js 구간 1 툴팁 최대 수면 입력 | A 판 차이 | `ebca435:js/Handler_ExtractTimeSeries.js:77` `binding: 8,` / `ebca435:transect_version/js/Handler_ExtractTimeSeries.js:80` `export function create_ExtractTimeSeries_BindGroup(device, uniformBuffer, txBottom, txBottomFriction, txContSource, txState, txWaveHeight, txTimeSeries_Locations, txTimeSeries_Data) {` 이력 본판: `397c575` 2025-09-09; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 binding 8의 txMeans_Speed를 제공한다. transect 판은 항상 유의파고 자료를 툴팁에 쓴다. |
| CT1-106 | js/Handler_ExtractTimeSeries.js 구간 2 최대 수면 리소스 | A 판 차이 | `ebca435:js/Handler_ExtractTimeSeries.js:128` `binding: 8,` / 추가 줄 없음 이력 본판: `397c575` 2025-09-09; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판에는 txMeans_Speed.createView()가 없다. 점 시계열 eta/P/Q의 자료원 변경을 뜻하지 않는다. |
| CT1-107 | js/Handler_Pass2.js 구간 1 퇴적물 확산 입력 | A 판 차이 | `ebca435:js/Handler_Pass2.js:144` `binding: 15,` / `ebca435:transect_version/js/Handler_Pass2.js:147` `export function create_Pass2_BindGroup(device, uniformBuffer,txH, txU, txV, txBottom, txC, txHnear, txXFlux, txYFlux, txSed_C1, txSed_C2, txSed_C3, txSed_C4, txXFlux_Sed, txYFlux_Sed) {` 이력 본판: `b8b50c3` 2025-06-08; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 binding 15로 txBreaking을 읽어 쇄파 점성 기반 확산계수를 만든다. transect 판의 Pass2에는 해당 리소스가 없다. |
| CT1-108 | js/Handler_Pass2.js 구간 2 Pass2 바인드 그룹 | A 판 차이 | `ebca435:js/Handler_Pass2.js:223` `binding: 15,` / `ebca435:transect_version/js/Handler_Pass2.js:215` `}` 이력 본판: `b8b50c3` 2025-06-08; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판의 txBreaking.createView()가 transect 판에는 없다. 농도 flux의 확산항 차이와 연결된다. |
| CT1-109 | js/Handler_Render.js 구간 1 가용 퇴적층 깊이 범례 | A 판 차이 | `ebca435:js/Handler_Render.js:317` `19: "Sediment Class 1 Available Depth (m)",` / 추가 줄 없음 이력 본판: `b8b50c3` 2025-06-08; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 surfaceToPlot==19의 가용 깊이 범례를 제공한다. transect 판에는 해당 표시 경로가 없다. |
| CT1-110 | js/Handler_SedTrans_Pass3.js 구간 1 퇴적물 적분 리소스 확장 | A 판 차이 | `ebca435:js/Handler_SedTrans_Pass3.js:126` `binding: 13,` / `ebca435:transect_version/js/Handler_SedTrans_Pass3.js:129` `export function create_SedTrans_Pass3_BindGroup(device, uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed) {` 이력 본판: `22e1983` 2025-06-06, `2a7452d` 2025-06-07, `b8b50c3` 2025-06-08; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 binding 13–17로 쇄파·면속도·면농도·hardbottom을 받는다. transect 판은 셀 운동량과 고정 확산계수를 쓴다. |
| CT1-111 | js/Handler_SedTrans_Pass3.js 구간 2 퇴적물 바인드 그룹 | A 판 차이 | `ebca435:js/Handler_SedTrans_Pass3.js:233` `binding: 13,` / `ebca435:transect_version/js/Handler_SedTrans_Pass3.js:189` `}` 이력 본판: `22e1983` 2025-06-06, `2a7452d` 2025-06-07, `b8b50c3` 2025-06-08; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 13–17의 리소스 view를 제공하지 않는다. 본판의 bedload와 침식 가능 깊이 검사에 필요한 자료가 빠진다. |
| CT1-112 | js/Handler_SedTrans_UpdateBottom.js 구간 1 바닥 갱신 입력 | A 판 차이 | `ebca435:js/Handler_SedTrans_UpdateBottom.js:70` `binding: 7,` / `ebca435:transect_version/js/Handler_SedTrans_UpdateBottom.js:73` `export function create_SedTrans_UpdateBottom_BindGroup(device, uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change) {` 이력 본판: `852ec28` 2025-06-13; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 hardbottom과 초기 바닥고를 받는다. transect 판은 가상 누적 변화량을 별도로 적산한다. |
| CT1-113 | js/Handler_SedTrans_UpdateBottom.js 구간 2 바닥 갱신 리소스 | A 판 차이 | `ebca435:js/Handler_SedTrans_UpdateBottom.js:126` `binding: 7,` / 추가 줄 없음 이력 본판: `852ec28` 2025-06-13; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판에는 binding 7과 8의 view가 없다. 본판 누적 변화량은 현재 바닥고에서 초기 바닥고를 뺀 값이다. |
| CT1-114 | js/Run_Compute_Shader.js 구간 1 즉시 submit 함수 인자 | F 표기 차이 | `ebca435:js/Run_Compute_Shader.js:3` `export function runComputeShader(device, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {` / `ebca435:transect_version/js/Run_Compute_Shader.js:3` `export function runComputeShader(device, commandEncoder, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {` | transect 판은 commandEncoder 인자를 받은 뒤 새 encoder로 다시 대입한다. 본판은 지역 const를 만든다. 해당 함수의 명령 생성·uniform 쓰기·dispatch·submit 순서는 같다. |
| CT1-115 | js/Run_Compute_Shader.js 구간 2 복사 함수 인자 | F 표기 차이 | `ebca435:js/Run_Compute_Shader.js:38` `export function runCopyTextures(device, calc_constants, src_texture, dst_texture) {` / `ebca435:transect_version/js/Run_Compute_Shader.js:38` `export function runCopyTextures(device, commandEncoder, calc_constants, src_texture, dst_texture) {` | 양쪽은 새 encoder로 같은 WIDTH×HEIGHT를 복사한 뒤 즉시 submit한다. transect 판의 전달 encoder 값은 사용하지 않는다. |
| CT1-116 | js/Run_Compute_Shader.js 구간 3 누적 명령 encoder 없음 | A 판 차이 | `ebca435:js/Run_Compute_Shader.js:55` `export function runComputeShader_EncStack(device, commandEncoder, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {` / 추가 줄 없음 이력 본판: `3646fc8` 2026-02-08; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 EncStack 함수를 export한다. transect 판은 각 계산과 복사마다 submit한다. 수치 연산을 제거한 차이는 아니다. |
| CT1-117 | js/Run_Tridiag_Solver.js 구간 1 PCR 바인드 그룹 인자 | A 판 차이 | `ebca435:js/Run_Tridiag_Solver.js:22` `TridiagX_BindGroup_BaseToA,` / `ebca435:transect_version/js/Run_Tridiag_Solver.js:32` `runCopyTextures(device, commandEncoder, calc_constants, current_stateUVstar, txNewState)` 이력 본판: `984091f` 2026-05-24, `33f7ff6` 2026-02-13; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 계수 텍스처 두 개를 번갈아 읽는 바인드 그룹을 추가한다. transect 판은 매 반복 뒤 계수를 복사한다. NLSW 우회 복사의 범위는 같다. |
| CT1-118 | js/Run_Tridiag_Solver.js 구간 2 PCR 첫 계수 전달 | F 표기 차이 | `ebca435:js/Run_Tridiag_Solver.js:46` `// CODEX: PCR now reads the base coefficient matrix directly on the first iteration.` / `ebca435:transect_version/js/Run_Tridiag_Solver.js:40` `runCopyTextures(device, commandEncoder, calc_constants, coefMatx, newcoef_x)` | transect 판은 coefMatx를 newcoef_x에 복사한다. 본판은 첫 바인드 그룹에서 coefMatx를 직접 읽는다. 최초 입력 행렬은 같다. |
| CT1-119 | js/Run_Tridiag_Solver.js 구간 3 x PCR과 y PCR 생략 | F 표기 차이 | `ebca435:js/Run_Tridiag_Solver.js:57` `const TridiagX_BindGroup_Current = (p == 0) ? TridiagX_BindGroup_BaseToA : ((p % 2 == 1) ? TridiagX_BindGroup : TridiagX_BindGroup_BToA);` / `ebca435:transect_version/js/Run_Tridiag_Solver.js:49` `runComputeShader(device, commandEncoder, TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);` | transect 판은 각 x 반복 후 계수를 복사한다. 본판은 교대 바인드 그룹을 쓴다. 해석: 동일한 PCR 점화식의 입력을 전달하는 두 방법이다. transect 판은 y 솔브 전체를 주석 처리한다. v=0이고 y 미분이 없으면 y 보정은 필요하지 않다. |
| CT1-120 | js/Time_Series.js 구간 1 코너 readback 버퍼 정리 | E 코드 결함 후보 (중간) | `ebca435:js/Time_Series.js:50` `buffer.destroy();  // free up memory` / 추가 줄 없음 반대 근거·두 경로 대조: readback 버퍼 수명 절. | 본판만 unmap 뒤 destroy한다. transect 판의 버퍼는 함수 안에서 생성한다. |
| CT1-121 | js/Time_Series.js 구간 2 시계열 epoch 인자 | A 판 차이 | `ebca435:js/Time_Series.js:60` `export async function readToolTipTextureData(device, texture, frame_count_time_series, timeSeriesDataEpoch = calc_constants.timeSeriesDataEpoch) {` / `ebca435:transect_version/js/Time_Series.js:57` `export async function readToolTipTextureData(device, texture, frame_count_time_series) {` 이력 본판: `ebca435` 2026-07-20; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 요청 시작 시의 epoch를 받는다. transect 판에는 비동기 초기화 경합을 구분하는 인자가 없다. |
| CT1-122 | js/Time_Series.js 구간 3 시계열 초기화 경합 | E 코드 결함 후보 (중간) | `ebca435:js/Time_Series.js:108` `if (timeSeriesDataEpoch != calc_constants.timeSeriesDataEpoch) {` / `ebca435:transect_version/js/Time_Series.js:96` `if (frame_count_time_series == 0){  // after we have written the data to file, or there is a change in the chart, this value is set to 0` 반대 근거·두 경로 대조: 비동기 시계열 초기화 절. | 본판은 오래된 epoch의 읽기 결과를 버린다. transect 판은 frame_count_time_series==0인 비동기 읽기가 끝난 뒤 배열을 비운다. 늦게 도착한 읽기가 새 구간 자료를 지울 수 있다. 본판의 한쪽 결함 수정이다. |
| CT1-123 | js/Time_Series.js 구간 4 시계열 readback 버퍼 정리 | E 코드 결함 후보 (중간) | `ebca435:js/Time_Series.js:125` `buffer.destroy();  // free up memory` / 추가 줄 없음 반대 근거·두 경로 대조: readback 버퍼 수명 절. | 본판만 unmap 뒤 destroy한다. 출력 time/eta/P/Q 배열의 채널 순서는 같다. |
| CT1-124 | js/constants_load_calc.js 구간 1 기본 격자 유형과 디버그 옵션 | A 판 차이 | `ebca435:js/constants_load_calc.js:16` `algochanges: 0, // set to 1 to test alternative algorithm for various parts of the code` / 추가 줄 없음 이력 본판: `896c491` 2026-01-17, `afc1fe7` 2026-06-19; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 algochanges=0과 grid_type=1을 정의한다. transect 판은 Cartesian x 단면 계산을 쓴다. |
| CT1-125 | js/constants_load_calc.js 구간 2 마찰·초기 수면·지구 반지름 기본값 | A 판 차이 | `ebca435:js/constants_load_calc.js:48` `vort_friction_factor: 0.0, // coefficient for vorticity-based momentum mixing/dissipation` / 추가 줄 없음 이력 본판: `5a5603f` 2026-01-15, `32be94a` 2025-10-16, `afc1fe7` 2026-06-19; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 vort_friction_factor=0.0·loadetaIC=0·R_earth=6371000.0을 정의한다. |
| CT1-126 | js/constants_load_calc.js 구간 3 입사파 기본값과 경계 파일 옵션 | C 문서 누락 | `ebca435:js/constants_load_calc.js:77` `incident_wave_H: 1.,  // Height (m) of Sine Wave / Pulse / Solitary Wave, or Significant Wave Height of Spectrum` / `ebca435:transect_version/js/constants_load_calc.js:66` `incident_wave_H: 0,  // Height (m) of Sine Wave / Pulse / Solitary Wave, or Significant Wave Height of Spectrum` | transect 판은 H=0·T=0·direction=0·numberOfWaves=2를 둔다. 본판은 H=1·T=10·direction=0·numberOfWaves=1을 둔다. transect 판은 파 성분 수를 파일 헤더에서 갱신하지 않는다. 본판만 trough_factor=1과 4변 시계열 파일·관측점 수·시각 이동을 정의한다. |
| CT1-127 | js/constants_load_calc.js 구간 4 퇴적물 확장 기본값 | A 판 차이 | `ebca435:js/constants_load_calc.js:112` `sedTurbDispersion: 0.01, // eddy viscosity constant (background) value for sediment transport` / 추가 줄 없음 이력 본판: `3be651a` 2025-06-11, `b8b50c3` 2025-06-08; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 sedTurbDispersion=0.01·sedBreakingDispersionCoef=0.1·loadHardBottom=0을 정의한다. |
| CT1-128 | js/constants_load_calc.js 구간 5 예제 목록과 기본 색상 | A 판 차이 | `ebca435:js/constants_load_calc.js:197` `"./examples/Hermosa_Beach_CA_COULWAVE/",` / `ebca435:transect_version/js/constants_load_calc.js:168` `"./examples/Hermosa_Beach_CA_COULWAVE/"` 이력 본판: `853c27d` 2025-08-11, `146a4ac` 2025-09-28, `32be94a` 2025-10-16, `ea93d70` 2025-10-24, `2e46d86` 2026-04-20, `afc1fe7` 2026-06-19; transect: `22e1983` 2025-06-06, `3d8a61b` 2025-06-14. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판의 예제 목록은 Hermosa_Beach_CA_COULWAVE에서 끝난다. 예제 내부는 판독하지 않는다. 기본 colorMap_choice는 본판 0이고 transect 2다. |
| CT1-129 | js/constants_load_calc.js 구간 6 점 시계열 초기화 상태 | A 판 차이 | `ebca435:js/constants_load_calc.js:259` `timeSeriesChartStartTime: 0.0, // current point-series chart-window start, zero normally and absolute time for nested runs` / 추가 줄 없음 이력 본판: `ebca435` 2026-07-20; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 timeSeriesChartStartTime과 timeSeriesDataEpoch를 0으로 정의한다. |
| CT1-130 | js/constants_load_calc.js 구간 7 사용자 초기 카메라 | A 판 차이 | `ebca435:js/constants_load_calc.js:309` `cameraInit_user: 0, // flag to indicate user has initialized camera position` / 추가 줄 없음 이력 본판: `f183cc2` 2026-02-01; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 초기 카메라 위치·yaw·pitch와 활성 플래그를 정의한다. |
| CT1-131 | js/constants_load_calc.js 구간 8 선형 구조물 상태 | A 판 차이 | `ebca435:js/constants_load_calc.js:330` `designcomponent_CrestElev: 0.0, // crest elevation for linear structures` / 추가 줄 없음 이력 본판: `d778fe7` 2026-06-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 천단고 0·천단폭 1·사면경사 0.25·끝점 좌표·미리보기·적용 플래그를 정의한다. |
| CT1-132 | js/constants_load_calc.js 구간 9 중첩 격자 출력 설정 | A 판 차이 | `ebca435:js/constants_load_calc.js:374` `nestedGridOutput_i0: 0, // lower-left rectangle i-index for nested boundary output` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02, `c4be488` 2026-07-13; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 사각형 인덱스·기간·간격·최대 8192 표본·트리거·접두어·사각형 배열·eta 임계값·시작시각을 정의한다. |
| CT1-133 | js/constants_load_calc.js 구간 10 구면 시간 간격과 강제 모드 | A 판 차이 | `ebca435:js/constants_load_calc.js:454` `if (calc_constants.grid_type == 2) {` / `ebca435:transect_version/js/constants_load_calc.js:358` `calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);` 이력 본판: `afc1fe7` 2026-06-19; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 구면에서 NLSW와 2차 재구성을 강제한다. 본판은 퇴적물과 쇄파를 끈다. 본판은 위도별 물리 격자간격의 최소값으로 dt를 정한다. Cartesian 식은 두 판에서 같다. |
| CT1-134 | js/constants_load_calc.js 구간 11 예제 목록 공백과 번호 주석 1 | F 표기 차이 | `ebca435:js/constants_load_calc.js:524` `"./examples/Miami_Beach_FL/",` / `ebca435:transect_version/js/constants_load_calc.js:394` `"./examples/Miami_Beach_FL/",` | 문자열 값과 순서는 같다. 공백과 //10 주석만 다르다. |
| CT1-135 | js/constants_load_calc.js 구간 12 예제 목록 공백과 번호 주석 2 | F 표기 차이 | `ebca435:js/constants_load_calc.js:534` `"./examples/Scripps_Canyon/",` / `ebca435:transect_version/js/constants_load_calc.js:404` `"./examples/Scripps_Canyon/",` | 문자열 값과 순서는 같다. 공백과 //20 주석만 다르다. |
| CT1-136 | js/constants_load_calc.js 구간 13 초기화 함수 안 예제 목록 | A 판 차이 | `ebca435:js/constants_load_calc.js:544` `"./examples/Pacifica_CA/",` / `ebca435:transect_version/js/constants_load_calc.js:414` `"./examples/Pacifica_CA/",` 이력 본판: `2e46d86` 2026-04-20, `853c27d` 2025-08-11, `146a4ac` 2025-09-28, `32be94a` 2025-10-16, `ea93d70` 2025-10-24, `afc1fe7` 2026-06-19; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 목록을 Hermosa_Beach_CA_COULWAVE까지 재정의한다. 본판은 뒤에 추가한 예제 경로를 유지한다. //30 같은 번호 주석 차이는 동작을 바꾸지 않는다. |
| CT1-137 | js/constants_load_calc.js 구간 14 중첩 출력 표본 수 제한 | A 판 차이 | `ebca435:js/constants_load_calc.js:578` `const nestedOutputMaxSamples = Math.max(1, Math.floor(calc_constants.nestedGridOutput_max_samples \|\| 8192));` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02, `c4be488` 2026-07-13; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 양의 간격을 보장하고 표본 수가 상한을 넘으면 간격을 늘린다. 기간 0은 표본 1개다. 활성 사각형 수를 별도로 센다. transect 판에는 해당 계산이 없다. |
| CT1-138 | js/constants_load_calc.js 구간 15 침강속도와 Shields 계수 | A 판 차이 | `ebca435:js/constants_load_calc.js:618` `calc_constants.sedC1_shields = 1.0 / ( (calc_constants.sedC1_denrat - 1.0) * calc_constants.g  * calc_constants.sedC1_d50/1000.);` / `ebca435:transect_version/js/constants_load_calc.js:447` `calc_constants.sedC1_shields = 1.0 / ( (calc_constants.sedC1_denrat - 1.0) * 9.81 * calc_constants.sedC1_d50/1000.);` 이력 본판: `22e1983` 2025-06-06, `ba9eb67` 2025-06-09, `b8b50c3` 2025-06-08; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 g를 사용하고 nu=1e-6·A=25·B=1.25·n=1로 자연 입자 침강속도를 계산한다. transect 판은 9.81을 고정하고 sqrt((4/3)*9.81*d/0.2*(denrat-1))를 쓴다. 본판만 MPM 계수를 만든다. d50의 mm→m 변환은 같다. |
| CT1-139 | js/display_parameters.js 구간 1 측정점 좌표 표시 | A 판 차이 | `ebca435:js/display_parameters.js:124` `const isSphericalGrid = Math.round(calc_constants.grid_type) == 2;` / `ebca435:transect_version/js/display_parameters.js:124` ```X: ${Math.round(calc_constants.locationOfTimeSeries[i].xts * 100) / 100}, ` +`` 이력 본판: `ff0d046` 2026-07-07; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 구면 격자에서 절대 경위도와 소수 6자리를 쓴다. transect 판은 상대 X/Y와 소수 2자리를 쓴다. |
| CT1-140 | js/display_parameters.js 구간 2 수상 사면 체적 표시 | E 코드 결함 후보 (중간) | `ebca435:js/display_parameters.js:158` `let slide_vol = 0.25 * calc_constants.disturbanceCrestamp * calc_constants.disturbanceWidth * calc_constants.disturbanceLength / 1000000.0;` / `ebca435:transect_version/js/display_parameters.js:145` `let slide_vol = calc_constants.disturbanceCrestamp * calc_constants.disturbanceWidth * calc_constants.disturbanceLength / 1000000.0;` 반대 근거·두 경로 대조: 사면 체적 계수 절. | transect 판은 진폭*폭*길이를 Mm^3로 환산한다. 본판은 그 값의 0.25배를 쓴다. 교란 함수의 체적 계수와 한쪽 수정 이력을 대조한다. |
| CT1-141 | js/display_parameters.js 구간 3 로그 DOM 증가 제한 | E 코드 결함 후보 (중간) | `ebca435:js/display_parameters.js:204` `const maxEntries = 200; // <-- set desired cap here` / 추가 줄 없음 반대 근거·두 경로 대조: 로그 DOM 증가 절. | 본판은 최대 200개 entry만 유지한다. transect 판은 이 제한이 없다. 메모리 정리 수정 이력과 루프 호출을 함께 근거로 둔다. |
| CT1-142 | js/display_parameters.js 구간 4 type-5 경계 표시 | A 판 차이 | `ebca435:js/display_parameters.js:236` `else if (boundaryType == 5) {` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 파일 시계열 경계라는 표시 문자열을 제공한다. |
| CT1-143 | js/display_parameters.js 구간 5 마지막 줄 개행 | F 표기 차이 | `ebca435:js/display_parameters.js:251` `}` / `ebca435:transect_version/js/display_parameters.js:228` `}` | 함수 본문은 같다. 마지막 줄의 개행 유무만 다르다. |
| CT1-144 | shaders/AddDisturbance.wgsl 구간 1 교란 누적 바닥고 입력 | E 코드 결함 후보 (약함) | `ebca435:shaders/AddDisturbance.wgsl:39` `@group(0) @binding(7) var txBotChange_Sed: texture_2d<f32>;` / `ebca435:transect_version/shaders/AddDisturbance.wgsl:39` `` 반대 근거·두 경로 대조: 교란과 누적 침식의 결합 절. | transect 판에는 txBotChange_Sed 입력이 없다. 본판의 침식 누적 보존 수정과 연결된다. |
| CT1-145 | shaders/AddDisturbance.wgsl 구간 2 교란 시간 상한 | A 판 차이 | `ebca435:shaders/AddDisturbance.wgsl:108` `var time_local = time;` / 추가 줄 없음 이력 본판: `185e91c` 2026-01-30, `3425a4a` 2026-01-30; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 time_local을 1.0e5*dt 이하로 제한한다. transect 판은 원래 time을 쓴다. |
| CT1-146 | shaders/AddDisturbance.wgsl 구간 3 사면체 방향 정의 | A 판 차이 | `ebca435:shaders/AddDisturbance.wgsl:120` `//let angle = globals.disturbanceDir;` / `ebca435:transect_version/shaders/AddDisturbance.wgsl:115` `let angle = globals.disturbanceDir;` 이력 본판: `8c2b62b` 2025-08-24; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 globals.disturbanceDir를 사용한다. 본판은 뒤에서 3.1415-traj_angle을 사용한다. |
| CT1-147 | shaders/AddDisturbance.wgsl 구간 4 사면 이동 궤적 | A 판 차이 | `ebca435:shaders/AddDisturbance.wgsl:128` `let displacement = max_displacement*(1.0+tanh((time_local-time_shift)/(change_timescale)))/2.0;` / `ebca435:transect_version/shaders/AddDisturbance.wgsl:123` `let displacement = max_displacement*(1.0+tanh((time-time_shift)/(change_timescale)))/2.0;` 이력 본판: `185e91c` 2026-01-30, `8c2b62b` 2025-08-24; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 초기·최종 각도의 차이에 traj_timefactor를 곱한다. transect 판은 변위 비율에 traj_timefactor만 곱한다. 본판은 사면체 회전각도 궤적에 연결한다. |
| CT1-148 | shaders/AddDisturbance.wgsl 구간 5 최초 교란 정지 조건 | A 판 차이 | `ebca435:shaders/AddDisturbance.wgsl:154` `if (time_local < 5.*dt) {` / `ebca435:transect_version/shaders/AddDisturbance.wgsl:147` `if (time < 5.*dt) {` 이력 본판: `185e91c` 2026-01-30; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 time_local<5*dt를 쓴다. transect 판은 time<5*dt를 쓴다. 상한 전 시간에는 두 조건이 같다. |
| CT1-149 | shaders/AddDisturbance.wgsl 구간 6 교란 초기 지형과 누적 침식 | E 코드 결함 후보 (약함) | `ebca435:shaders/AddDisturbance.wgsl:167` `let bottom_initial_tex = textureLoad(txBottomInitial, idx, 0) + textureLoad(txBotChange_Sed, idx, 0);` / `ebca435:transect_version/shaders/AddDisturbance.wgsl:160` `let bottom_initial_tex = textureLoad(txBottomInitial, idx, 0);` 반대 근거·두 경로 대조: 교란과 누적 침식의 결합 절. | 본판은 초기 바닥고에 txBotChange_Sed를 더한다. transect 판은 초기 바닥고만 사용한다. 한쪽 결함 수정 이력이 있다. |
| CT1-150 | shaders/AddDisturbance.wgsl 구간 7 육상 사면 변형 억제 | A 판 차이 | `ebca435:shaders/AddDisturbance.wgsl:229` `//   if(bottom_initial_tex.z > 0.0 ) {  // without this, the slide creates water on dry land (for subaerial slides).` / `ebca435:transect_version/shaders/AddDisturbance.wgsl:222` `if(bottom_initial_tex.z > 0.0 ) {` 이력 본판: `8c2b62b` 2025-08-24; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 초기 바닥고가 양수이면 기존 바닥고를 되돌리고 dhdt를 0으로 둔다. 본판은 이 조건을 주석 처리했다. 본판 주석은 이 조건의 물 생성 방지 목적을 설명하지만 현재는 실행하지 않는다. |
| CT1-151 | shaders/BoundaryPass.wgsl 구간 1 경계 uniform 확장 | A 판 차이 | `ebca435:shaders/BoundaryPass.wgsl:44` `algochanges: i32,` / 추가 줄 없음 이력 본판: `896c491` 2026-01-17, `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 알고리즘 시험·trough_factor·구면 원점·4변 관측점 수·시간 보간 인덱스와 가중치를 받는다. |
| CT1-152 | shaders/BoundaryPass.wgsl 구간 2 binding 9의 다른 물리 의미 | C 문서 누락 | `ebca435:shaders/BoundaryPass.wgsl:72` `@group(0) @binding(9) var txBoundaryForcing: texture_2d<f32>;` / `ebca435:transect_version/shaders/BoundaryPass.wgsl:58` `@group(0) @binding(9) var txWaves_Transect: texture_2d<f32>;` | transect 판은 binding 9를 단면별 파랑에 사용한다. 본판은 지형변동 강제장을 읽고 10–13에서 경계 시계열을 읽는다. |
| CT1-153 | shaders/BoundaryPass.wgsl 구간 3 남북 고체벽 생략 | F 표기 차이 | `ebca435:shaders/BoundaryPass.wgsl:92` `fn SouthBoundarySolid(idx: vec2<i32>) -> vec4<f32> {` / `ebca435:transect_version/shaders/BoundaryPass.wgsl:74` `//fn SouthBoundarySolid(idx: vec2<i32>) -> vec4<f32> {` | 독립 단면은 y 방향 반사벽을 적용하지 않는다. 동서 고체벽 함수는 유지한다. |
| CT1-154 | shaders/BoundaryPass.wgsl 구간 4 남북 sponge 생략 | F 표기 차이 | `ebca435:shaders/BoundaryPass.wgsl:116` `fn SouthBoundarySponge(idx: vec2<i32>) -> vec4<f32> {` / `ebca435:transect_version/shaders/BoundaryPass.wgsl:98` `//fn SouthBoundarySponge(idx: vec2<i32>) -> vec4<f32> {` | 독립 단면은 y 방향 흡수층 함수를 호출하지 않는다. 동서 sponge 식은 유지한다. |
| CT1-155 | shaders/BoundaryPass.wgsl 구간 5 고립파의 1D 환원 | F 표기 차이 | `ebca435:shaders/BoundaryPass.wgsl:138` `let y = f32(idx.y) * globals.dy;` / `ebca435:transect_version/shaders/BoundaryPass.wgsl:121` `let y = 0.0;` | transect 판은 y와 yloc를 0.0으로 둔다. hv=0.0이다. x 진행파를 쓰는 단면에서 고립파의 x 식과 같다. |
| CT1-156 | shaders/BoundaryPass.wgsl 구간 6 단면 파랑·pulse·주기·sponge·type5 차이 | C 문서 누락 | `ebca435:shaders/BoundaryPass.wgsl:164` `if (current_boundary == 1 \|\| current_boundary == 3) {` / `ebca435:transect_version/shaders/BoundaryPass.wgsl:158` `let ky = 0.0;` | transect 판은 ky와 기점 이동을 0으로 둔다. pulse의 성분 지속 길이는 4주기이고 본판은 5주기다. 본판만 음의 eta에 trough_factor를 곱한다. transect 판은 국소 바닥고로 파수를 계산한다. 본판은 base_depth를 쓴다. transect 판은 같은 y행의 파랑 성분을 읽는다. 본판의 시계열 공간·시간 선형 보간은 transect 판에 없다. transect 판은 dhdt 바닥 보정을 하지 않는다. 주기 경계는 비활성이다. 본판의 중첩 sponge 가중 평균 대신 동서 sponge를 순서대로 대입한다. |
| CT1-157 | shaders/BoundaryPass.wgsl 구간 7 남북 고체벽 적용 생략 | F 표기 차이 | `ebca435:shaders/BoundaryPass.wgsl:425` `if (globals.south_boundary_type <= 1) {` / `ebca435:transect_version/shaders/BoundaryPass.wgsl:251` `// if (globals.south_boundary_type <= 1) {` | transect 판은 남북 경계 상태와 퇴적물 값을 덮어쓰지 않는다. |
| CT1-158 | shaders/BoundaryPass.wgsl 구간 8 남북 입사파·주기·type5 미지원 | C 문서 누락 | `ebca435:shaders/BoundaryPass.wgsl:482` `if (globals.south_boundary_type == 2 && idx.y <= 2) {` / `ebca435:transect_version/shaders/BoundaryPass.wgsl:308` `// if (globals.south_boundary_type == 2 && idx.y <= 2) {` | transect 판은 남북 입사파와 모든 주기 경계를 주석 처리한다. 본판의 type5 시계열 경계 대입은 없다. transect UI의 별표와 연결된다. |
| CT1-159 | shaders/BoundaryPass.wgsl 구간 9 서쪽 하천 경계 주석 | F 표기 차이 | `ebca435:shaders/BoundaryPass.wgsl:578` `if (globals.west_boundary_type == 4) { // west boundary is assumed to be the upstream boundary` / `ebca435:transect_version/shaders/BoundaryPass.wgsl:411` `if (globals.west_boundary_type == 4) {` | 실행 조건은 같다. 상류 가정이라는 설명 주석만 없다. |
| CT1-160 | shaders/BoundaryPass.wgsl 구간 10 동쪽 하천 경계 주석 | F 표기 차이 | `ebca435:shaders/BoundaryPass.wgsl:593` `if (globals.east_boundary_type == 4) {  // east boundary is assumed to be the downstream boundary` / `ebca435:transect_version/shaders/BoundaryPass.wgsl:426` `if (globals.east_boundary_type == 4) {` | 실행 조건은 같다. 하류 가정이라는 설명 주석만 없다. |
| CT1-161 | shaders/BoundaryPass.wgsl 구간 11 북쪽 하천과 고립 습윤점 처리 생략 | C 문서 누락 | `ebca435:shaders/BoundaryPass.wgsl:605` `if (globals.north_boundary_type == 4) {` / `ebca435:transect_version/shaders/BoundaryPass.wgsl:438` `// if (globals.north_boundary_type == 4) {` | transect 판은 북쪽 하천 경계를 주석 처리한다. transect 판은 고립 습윤점과 단일 격자 수로 끝의 동결을 주석 처리한다. 음수 수심 검사는 유지한다. h_here 재평가는 앞에서 BCState를 더 바꾸지 않으므로 생략해도 현재 경로에서 같은 값이다. |
| CT1-162 | shaders/CalcMeans.wgsl 구간 1 통계 실제 수면 리소스 | A 판 차이 | `ebca435:shaders/CalcMeans.wgsl:25` `@group(0) @binding(13) var txNewState: texture_2d<f32>;` / 추가 줄 없음 이력 본판: `dc6cc2d` 2025-08-10; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 txNewState를 받는다. |
| CT1-163 | shaders/CalcMeans.wgsl 구간 2 통계 수면 자료원과 1D 속도 평균 | A 판 차이 | `ebca435:shaders/CalcMeans.wgsl:38` `let v4 = textureLoad(txV, idx, 0);` / `ebca435:transect_version/shaders/CalcMeans.wgsl:42` `let h = (h4.y + h4.w) / 2.0;` 이력 본판: `dc6cc2d` 2025-08-10; transect: `22e1983` 2025-06-06, `4dc20a1` 2026-01-27. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 동·서 면 평균을 2.0으로 나눈다. 본판은 네 면 평균을 4.0으로 나눈다. 1D 환원에서 속도·수심·농도 평균은 같은 의미다. eta는 본판이 실제 txNewState 값이고 transect가 h+bottom이다. transect는 와도를 계산하지 않는다. 본판의 건조 셀 eta 대체값은 최대값 계산 전에만 적용된다. |
| CT1-164 | shaders/CalcMeans.wgsl 구간 3 통계 횡방향 출력 | F 표기 차이 | `ebca435:shaders/CalcMeans.wgsl:90` `v_max_new = max(speed_means_here.y,v);` / `ebca435:transect_version/shaders/CalcMeans.wgsl:99` `textureStore(txtemp_Means_Speed, idx, vec4<f32>(u_max_new, 0.0, speed_max_new, eta_max_new));` | transect 판은 v·hv2·와도의 통계 채널을 0.0으로 저장한다. x 속도·속력·x 운동량 flux·eta 최대값의 갱신 방식은 유지한다. |
| CT1-165 | shaders/Copytxf32_txf16.wgsl 구간 1 표시용 건조 uniform | A 판 차이 | `ebca435:shaders/Copytxf32_txf16.wgsl:4` `delta: f32,` / 추가 줄 없음 이력 본판: `dc6cc2d` 2025-08-10; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 delta와 base_depth를 받는다. |
| CT1-166 | shaders/Copytxf32_txf16.wgsl 구간 2 표시용 f16 패킹 | A 판 차이 | `ebca435:shaders/Copytxf32_txf16.wgsl:17` `@group(0) @binding(8) var txHardBottom: texture_2d<f32>;` / `ebca435:transect_version/shaders/Copytxf32_txf16.wgsl:21` `let eta = textureLoad(txNewState, idx, 0).r;` 이력 본판: `b8b50c3` 2025-06-08, `dc6cc2d` 2025-08-10; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 건조 셀 eta를 -10*base_depth로 바꾸고 foam을 0으로 둔다. 본판은 3번째 레이어에 bottom·hardbottom·가용 깊이를 쓴다. transect 판은 eta와 foam을 그대로 두고 두 레이어만 쓴다. |
| CT1-167 | shaders/ExtractTimeSeries.wgsl 구간 1 교란 유형 uniform | A 판 차이 | `ebca435:shaders/ExtractTimeSeries.wgsl:10` `disturbanceType: i32` / 추가 줄 없음 이력 본판: `397c575` 2025-09-09; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 disturbanceType을 받는다. |
| CT1-168 | shaders/ExtractTimeSeries.wgsl 구간 2 툴팁 최대수면 리소스 | A 판 차이 | `ebca435:shaders/ExtractTimeSeries.wgsl:22` `@group(0) @binding(8) var txMeans_Speed: texture_2d<f32>;` / 추가 줄 없음 이력 본판: `397c575` 2025-09-09; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 txMeans_Speed를 읽는다. |
| CT1-169 | shaders/ExtractTimeSeries.wgsl 구간 3 툴팁 Hs 또는 최대수면 선택 | A 판 차이 | `ebca435:shaders/ExtractTimeSeries.wgsl:47` `var hsig = 0.0;` / `ebca435:transect_version/shaders/ExtractTimeSeries.wgsl:45` `let hsig = textureLoad(txWaveHeight, current_location, 0).z;  // Significant wave height` 이력 본판: `397c575` 2025-09-09; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 disturbanceType>1이면 최대 수면을 쓴다. 나머지 경우 Hs를 쓴다. transect 판은 항상 Hs를 쓴다. |
| CT1-170 | shaders/MouseClickChange.wgsl 구간 1 선형 구조물 uniform | A 판 차이 | `ebca435:shaders/MouseClickChange.wgsl:19` `designcomponent_CrestElev: f32,` / 추가 줄 없음 이력 본판: `d778fe7` 2026-06-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 천단고·천단폭·사면경사·양끝 좌표·적용 플래그를 받는다. |
| CT1-171 | shaders/MouseClickChange.wgsl 구간 2 선분 거리와 사다리꼴 고도 함수 | A 판 차이 | `ebca435:shaders/MouseClickChange.wgsl:70` `fn calc_segment_distance(xloc: f32, yloc: f32, xstart: f32, ystart: f32, xend: f32, yend: f32) -> f32 {` / 추가 줄 없음 이력 본판: `d778fe7` 2026-06-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 선분 투영을 [0,1]로 제한한다. 본판은 천단 절반폭 밖의 거리에 경사를 곱해 목표 고도를 만든다. 폭이나 경사가 0 이하면 -1e9를 반환한다. transect 판에는 두 함수가 없다. |
| CT1-172 | shaders/MouseClickChange.wgsl 구간 3 편집 대상 선택 | A 판 차이 | `ebca435:shaders/MouseClickChange.wgsl:131` `if (globals.designcomponent_AddLinearStructure == 1) {` / `ebca435:transect_version/shaders/MouseClickChange.wgsl:84` `B_here = textureLoad(txDesignComponents, idx, 0);` 이력 본판: `d778fe7` 2026-06-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 선형 구조물 모드에서 바닥고·상태를 편집한다. transect 판은 설계 ID·마찰만 편집한다. |
| CT1-173 | shaders/MouseClickChange.wgsl 구간 4 선형 구조물 적용 | A 판 차이 | `ebca435:shaders/MouseClickChange.wgsl:215` `if (globals.designcomponent_AddLinearStructure == 1) {` / `ebca435:transect_version/shaders/MouseClickChange.wgsl:146` `var r = calc_radial_distance(xloc,yloc,xo,yo);` 이력 본판: `d778fe7` 2026-06-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 중심·북쪽 면·동쪽 면의 목표 고도를 계산해 기존 고도보다 낮추지 않게 쓴다. transect 판은 원형 영역의 설계 ID와 가우스 마찰 편집만 유지한다. 마지막 개행도 다르다. |
| CT1-174 | shaders/Pass0.wgsl 구간 1 근방 수심의 1D 패킹 | F 표기 차이 | `ebca435:shaders/Pass0.wgsl:28` `let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` / `ebca435:transect_version/shaders/Pass0.wgsl:52` `h_vec.x= 0.0; //h_north; //min(h_here, h_north);` | transect 판은 북·남 이웃을 읽지 않는다. h_vec의 x·z를 0.0으로 둔다. 동·서 면인 y·w는 본판과 같다. x 방향 Riemann flux가 쓰는 이웃 수심은 보존된다. |
| CT1-175 | shaders/Pass1.wgsl 구간 1 재구성 이웃과 건조 검사 | F 표기 차이 | `ebca435:shaders/Pass1.wgsl:61` `let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` / `ebca435:transect_version/shaders/Pass1.wgsl:87` `if(h_east <= h_cut && h_west <= h_cut) {` | transect 판은 동·서 이웃만 읽는다. 건조 조기 반환은 양쪽 x 이웃 수심으로 판정한다. y 속도 텍스처 쓰기를 생략한다. |
| CT1-176 | shaders/Pass1.wgsl 구간 2 면 재구성과 Froude 제한의 1D 환원 | F 표기 차이 | `ebca435:shaders/Pass1.wgsl:98` `let Bz = textureLoad(txBottom, downIdx, 0).x;` / `ebca435:transect_version/shaders/Pass1.wgsl:102` `let B = vec4<f32>(Bxy, 0.0, Bw);` | transect 판은 북·남 면값을 0.0으로 둔다. 동·서 면의 eta·hu·hc 재구성은 같다. v=0을 대입하면 speed=sqrt(u*u)다. Froude 최대값은 Fr.y와 Fr.w에서 취한다. 지형 경사 제한은 dBdx만 사용한다. |
| CT1-177 | shaders/Pass1_HighOrder.wgsl 구간 1 고차 재구성 x 스텐실 | F 표기 차이 | `ebca435:shaders/Pass1_HighOrder.wgsl:157` `let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` / `ebca435:transect_version/shaders/Pass1_HighOrder.wgsl:213` `if(h_east <= h_cut && h_west <= h_cut) {` | transect 판은 ±1·±2·±3의 y 이웃 읽기를 생략한다. 건조 검사는 동·서 이웃만 사용한다. |
| CT1-178 | shaders/Pass1_HighOrder.wgsl 구간 2 고차 전환과 지형 최대값 | F 표기 차이 | `ebca435:shaders/Pass1_HighOrder.wgsl:224` `let Bz = textureLoad(txBottom, downIdx, 0).x;` / `ebca435:transect_version/shaders/Pass1_HighOrder.wgsl:228` `let B = vec4<f32>(Bxy, 0.0, Bw);` | transect 판은 wetdry와 maxB/maxB2/maxB3를 같은 행의 x 스텐실에서 취한다. 동·서 재구성의 저차 전환 조건과 TWO_THETAc 식은 유지한다. |
| CT1-179 | shaders/Pass1_HighOrder.wgsl 구간 3 고차 면값과 유속 제한 | F 표기 차이 | `ebca435:shaders/Pass1_HighOrder.wgsl:288` `hvwy = ReconstructMUSCL4(in_west3.z, in_west2.z, in_west.z, in_here.z, in_east.z, in_east2.z, in_east3.z, dh_max);` / `ebca435:transect_version/shaders/Pass1_HighOrder.wgsl:314` `w = vec4<f32>(0.0, wwy.y, 0.0, wwy.x);` | transect 판은 x 방향 MUSCL4 재구성을 유지한다. 북·남 면과 hv를 제거한다. 건조 임계값 검사는 동·서 면에 남긴다. v=0 및 y 미분=0에서 속력과 지형 경사 제한의 본판 식이 transect 식으로 줄어든다. |
| CT1-180 | shaders/Pass2.wgsl 구간 1 퇴적물 확산 uniform | A 판 차이 | `ebca435:shaders/Pass2.wgsl:10` `sedTurbDispersion: f32,` / 추가 줄 없음 이력 본판: `b8b50c3` 2025-06-08; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 배경 확산과 쇄파 확산계수를 받는다. transect 판은 Pass2의 확산 보정을 구현하지 않는다. |
| CT1-181 | shaders/Pass2.wgsl 구간 2 쇄파 입력 binding | A 판 차이 | `ebca435:shaders/Pass2.wgsl:34` `@group(0) @binding(15) var txBreaking: texture_2d<f32>;` / 추가 줄 없음 이력 본판: `b8b50c3` 2025-06-08; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 binding 15에서 쇄파 점성을 읽는다. |
| CT1-182 | shaders/Pass2.wgsl 구간 3 수치 flux 1D 환원 | F 표기 차이 | `ebca435:shaders/Pass2.wgsl:65` `let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` / `ebca435:transect_version/shaders/Pass2.wgsl:91` `let dB = max(textureLoad(txBottom, rightIdx, 0).z - B_here, textureLoad(txBottom, leftIdx, 0).z - B_here);` | transect 판은 x 방향 HLL 함수를 유지한다. y flux 저장을 생략한다. x flux의 횡운동량 채널은 0.0이다. minH는 동·서 면만 검사한다. 본판의 Class 1 확산 flux 추가는 별도 판 차이다. transect 판은 농도 flux에서 순수 이류와 수치 확산만 계산한다. |
| CT1-183 | shaders/Pass3A_COULWAVE.wgsl 구간 1 COULWAVE 면속도 평균의 절반값 | E 코드 결함 후보 (강함) | `ebca435:shaders/Pass3A_COULWAVE.wgsl:27` `let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` / `ebca435:transect_version/shaders/Pass3A_COULWAVE.wgsl:27` `// let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` 반대 근거·두 경로 대조: COULWAVE u 평균 절. | transect 판은 북·남 txU 채널을 0으로 쓰지만 u_here는 여전히 네 채널 합을 4.0으로 나눈다. 같은 판 CalcMeans는 동·서 두 채널 합을 2.0으로 나눈다. 일정한 x 면속도 U에서 Pass3A 결과는 U/2다. 단면 가정과 평균식의 모순을 강함으로 둔다. |
| CT1-184 | shaders/Pass3A_COULWAVE.wgsl 구간 2 COULWAVE 보조장 패킹 | F 표기 차이 | `ebca435:shaders/Pass3A_COULWAVE.wgsl:62` `let eta_jp1 = textureLoad(txState, upIdx, 0).x;` / `ebca435:transect_version/shaders/Pass3A_COULWAVE.wgsl:82` `let vel_out = vec4<f32>(u_here, 0.0, eta_here, H_here);` | transect 판은 v·za_y·dv를 0으로 저장한다. za_here와 za_x 식은 유지한다. |
| CT1-185 | shaders/Pass3B_COULWAVE.wgsl 구간 1 COULWAVE 보조장 x 스텐실 | F 표기 차이 | `ebca435:shaders/Pass3B_COULWAVE.wgsl:30` `let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` / `ebca435:transect_version/shaders/Pass3B_COULWAVE.wgsl:30` `// let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` | transect 판은 y·대각 이웃과 v·dv 읽기를 생략한다. |
| CT1-186 | shaders/Pass3B_COULWAVE.wgsl 구간 2 COULWAVE S와 T의 1D 환원 | F 표기 차이 | `ebca435:shaders/Pass3B_COULWAVE.wgsl:56` `let v_ip1 = all_vars.y;` / `ebca435:transect_version/shaders/Pass3B_COULWAVE.wgsl:135` `let S = dudx;` | v=0과 y 미분=0이면 S=u_x, T=(du)_x다. dSdx와 dTdx에는 순수 x 2차 차분만 남는다. 제거한 4차 미분 대안은 본판에서도 주석이다. |
| CT1-187 | shaders/Pass3B_COULWAVE.wgsl 구간 3 COULWAVE E/F/G 패킹 | F 표기 차이 | `ebca435:shaders/Pass3B_COULWAVE.wgsl:188` `let E2 = H_here * (temp2 * dSdy + temp3 * dTdy);` / `ebca435:transect_version/shaders/Pass3B_COULWAVE.wgsl:160` `let uSxvSy = 0.5 * (za_2 - eta_2) * (u_here * dSdx);` | transect 판은 E2·교차미분·y gradient·와도를 0으로 패킹한다. x 방향 uSx와 uTx 항은 보존한다. |
| CT1-188 | shaders/Pass3_Bous.wgsl 구간 1 와도 소산 uniform | A 판 차이 | `ebca435:shaders/Pass3_Bous.wgsl:38` `vort_friction_factor: f32,` / 추가 줄 없음 이력 본판: `35b7f1c` 2026-01-15; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 후속 와도 소산계수를 받는다. |
| CT1-189 | shaders/Pass3_Bous.wgsl 구간 2 Boussinesq x 경계와 스텐실 | F 표기 차이 | `ebca435:shaders/Pass3_Bous.wgsl:99` `if (idx.x >= globals.width - 2 \|\| idx.y >= globals.height - 2 \|\| idx.x <= 1 \|\| idx.y <= 1) {` / `ebca435:transect_version/shaders/Pass3_Bous.wgsl:99` `if (idx.x >= globals.width - 2 \|\| idx.x <= 1) {` | transect 판은 x 경계에서만 조기 반환한다. y·대각 스텐실과 미사용 F_G_star 쓰기를 생략한다. |
| CT1-190 | shaders/Pass3_Bous.wgsl 구간 3 Boussinesq 건조 검사 | F 표기 차이 | `ebca435:shaders/Pass3_Bous.wgsl:125` `let B_south = textureLoad(txBottom, downIdx, 0).z;` / `ebca435:transect_version/shaders/Pass3_Bous.wgsl:144` `if(h_east <= h_cut && h_west <= h_cut) {` | 독립 단면은 동·서 이웃 수심만 검사한다. h_min은 동·서 채널만 채운다. |
| CT1-191 | shaders/Pass3_Bous.wgsl 구간 4 Boussinesq flux와 수면 기울기 | F 표기 차이 | `ebca435:shaders/Pass3_Bous.wgsl:164` `let yflux_here = textureLoad(txYFlux, idx, 0);` / `ebca435:transect_version/shaders/Pass3_Bous.wgsl:165` `// let yflux_here = textureLoad(txYFlux, idx, 0);` | transect 판은 x flux와 detadx만 계산한다. |
| CT1-192 | shaders/Pass3_Bous.wgsl 구간 5 주기 경계 분산 차단 생략 | C 문서 누락 | `ebca435:shaders/Pass3_Bous.wgsl:183` `var periodic_bc_fix = -1;` / `ebca435:transect_version/shaders/Pass3_Bous.wgsl:194` `if (near_dry > 0. )` | transect 판은 periodic_bc_fix를 주석 처리한다. transect 경계 셰이더는 주기 경계 복사도 주석 처리한다. UI는 주기 경계에 별표를 붙인다. 이는 지원하지 않는 경로의 단면판 선택이다. |
| CT1-193 | shaders/Pass3_Bous.wgsl 구간 6 Boussinesq 분산식의 1D 환원 | F 표기 차이 | `ebca435:shaders/Pass3_Bous.wgsl:200` `let downdownIdx = idx + vec2<i32>(0, -2);` / `ebca435:transect_version/shaders/Pass3_Bous.wgsl:286` `Psi1x = globals.Bcoef_g * d3_here * ((eta_right_right - 2.0 * eta_right + 2.0 * eta_left - eta_left_left) * (0.5 * globals.one_over_d3x));` | y 미분과 Q를 0으로 놓으면 F_star와 G_star가 0이다. Psi1x에는 d^3*eta_xxx만 남는다. Psi2x에는 2*Bcoef_g*d^2*d_x*eta_xx가 남는다. transect 판은 이 두 x 항을 계산한다. 본판의 와도 혼합은 1D 가정에서 0이다. |
| CT1-194 | shaders/Pass3_Bous.wgsl 구간 7 압력과 백수 source | F 표기 차이 | `ebca435:shaders/Pass3_Bous.wgsl:311` `let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;` / `ebca435:transect_version/shaders/Pass3_Bous.wgsl:303` `// let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;` | transect 판은 x 압력과 Dxx 확산만 남긴다. c_dissipation 식은 같다. |
| CT1-195 | shaders/Pass3_Bous.wgsl 구간 8 쇄파 확산과 해안선 처리 | F 표기 차이 | `ebca435:shaders/Pass3_Bous.wgsl:349` `let nu_flux_up = textureLoad(txDissipationFlux, upIdx, 0);` / `ebca435:transect_version/shaders/Pass3_Bous.wgsl:354` `breaking_x = dPdxx;` | transect 판은 breaking_x=dPdxx로 둔다. y 응력과 y 기울기 보정을 생략한다. y 미분=0과 Q=0에서 본판 식이 이 형태가 된다. |
| CT1-196 | shaders/Pass3_Bous.wgsl 구간 9 계산한 Psi2x의 source 누락 | E 코드 결함 후보 (강함) | `ebca435:shaders/Pass3_Bous.wgsl:392` `let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + breaking_y + (Psi1y + Psi2y) + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);` / `ebca435:transect_version/shaders/Pass3_Bous.wgsl:386` `let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x) + press_x, 0.0, hc_by_dx_dx + c_dissipation);` 반대 근거·두 경로 대조: Boussinesq Psi2x 누락 절. | transect 판은 Psi2x를 계산하지만 source_term에는 Psi1x만 더한다. 바로 위 주석과 본판 source는 Psi1x+Psi2x를 더한다. Psi2x의 지형 경사 항은 1D에서 사라지지 않는다. 의도 변경 근거와 보정 경로를 확인한 뒤 강함으로 둔다. |
| CT1-197 | shaders/Pass3_Bous.wgsl 구간 10 분산 교차 이력 쓰기 생략 | F 표기 차이 | `ebca435:shaders/Pass3_Bous.wgsl:428` `textureStore(F_G_star, idx, F_G_here);` / `ebca435:transect_version/shaders/Pass3_Bous.wgsl:424` `// textureStore(F_G_star, idx, F_G_here);` | transect 판은 1D에서 0인 F_G_star 출력 쓰기를 생략한다. |
| CT1-198 | shaders/Pass3_COULWAVE.wgsl 구간 1 COULWAVE 와도 소산계수 | A 판 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:38` `vort_friction_factor: f32,` / 추가 줄 없음 이력 본판: `35b7f1c` 2026-01-15; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 후속 vort_friction_factor uniform을 받는다. |
| CT1-199 | shaders/Pass3_COULWAVE.wgsl 구간 2 COULWAVE x 경계와 이웃 | F 표기 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:99` `if (idx.x >= globals.width - 2 \|\| idx.y >= globals.height - 2 \|\| idx.x <= 1 \|\| idx.y <= 1) {` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:99` `if (idx.x >= globals.width - 2 \|\| idx.x <= 1) {` | transect 판은 y 경계와 y 이웃 계산을 생략한다. |
| CT1-200 | shaders/Pass3_COULWAVE.wgsl 구간 3 COULWAVE 건조 검사 | F 표기 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:129` `let B_south = textureLoad(txBottom, downIdx, 0).z;` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:148` `if(h_east <= h_cut && h_west <= h_cut) {` | transect 판은 동·서 이웃만 검사한다. 건조 반환은 바닥고와 영 운동량을 유지한다. |
| CT1-201 | shaders/Pass3_COULWAVE.wgsl 구간 4 COULWAVE flux와 기울기 | F 표기 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:168` `let yflux_here = textureLoad(txYFlux, idx, 0);` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:169` `// let yflux_here = textureLoad(txYFlux, idx, 0);` | transect 판은 x flux와 x 수면 기울기만 사용한다. |
| CT1-202 | shaders/Pass3_COULWAVE.wgsl 구간 5 COULWAVE 주기 경계 분산 차단 생략 | C 문서 누락 | `ebca435:shaders/Pass3_COULWAVE.wgsl:188` `var periodic_bc_fix = -1;` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:199` `if (near_dry > 0.)` | 주기 경계를 구현하지 않는 단면판은 해당 분산 차단도 주석 처리한다. x 수면의 4차 차분은 유지한다. |
| CT1-203 | shaders/Pass3_COULWAVE.wgsl 구간 6 COULWAVE grouping 읽기의 1D 환원 | F 표기 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:239` `let v_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).y;` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:241` `// let v_here = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).y;` | transect 판은 v·dv·혼합미분·za_y를 읽지 않는다. 레이어 번호와 x 자료의 채널은 유지한다. |
| CT1-204 | shaders/Pass3_COULWAVE.wgsl 구간 7 COULWAVE F source 구성 | F 표기 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:283` `let dSdy = textureLoad(txCW_groupings, vec3<i32>(idx.x, idx.y, level), 0).y;` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:349` `var temp1 = u_here * (dE1dx);` | transect 판은 E2_y를 생략한다. temp1=u_here*dE1dx다. E·za·eta·S·T를 쓰는 x 항은 유지한다. |
| CT1-205 | shaders/Pass3_COULWAVE.wgsl 구간 8 COULWAVE G source와 교차 이력 제거 | F 표기 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:342` `var temp7A= -v_here * dzadx * (dTdy + za_here * dSdy);` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:357` `var temp7A= 0.0;` | v=0과 y 미분=0에서 Gsrc·F_star·G_star·Psi2x·Psi1y·Psi2y는 0이다. transect 판은 이 값을 생략하거나 0.0으로 둔다. E_src=dE1dx다. 마찰은 v=0에서 평가한다. |
| CT1-206 | shaders/Pass3_COULWAVE.wgsl 구간 9 COULWAVE 압력과 백수 확산 | F 표기 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:405` `let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:409` `// let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;` | transect 판은 x 압력·Dxx 확산·백수 감쇠만 남긴다. |
| CT1-207 | shaders/Pass3_COULWAVE.wgsl 구간 10 COULWAVE 쇄파 확산 | F 표기 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:443` `let nu_flux_up = textureLoad(txDissipationFlux, upIdx, 0);` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:460` `breaking_x = dPdxx;` | transect 판은 breaking_x=dPdxx로 둔다. y 응력과 y 해안선 기울기를 생략한다. |
| CT1-208 | shaders/Pass3_COULWAVE.wgsl 구간 11 COULWAVE 적분 source | F 표기 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:486` `let source_term = vec4<f32>(dhdt + overflow_dry + E_src, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + breaking_y + (Psi1y + Psi2y) + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:492` `let source_term = vec4<f32>(dhdt + overflow_dry + E_src, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, 0.0, hc_by_dx_dx + c_dissipation);` | transect 판은 x의 Psi1x+Psi2x를 유지한다. y 운동량 source는 0.0이다. 시간적분 계수는 같다. |
| CT1-209 | shaders/Pass3_COULWAVE.wgsl 구간 12 COULWAVE 교차 이력 쓰기 생략 | F 표기 차이 | `ebca435:shaders/Pass3_COULWAVE.wgsl:522` `textureStore(F_G_star, idx, F_G_here);` / `ebca435:transect_version/shaders/Pass3_COULWAVE.wgsl:530` `//  textureStore(F_G_star, idx, F_G_here);` | transect 판은 1D에서 0인 F_G_star 쓰기를 생략한다. |
| CT1-210 | shaders/Pass3_NLSW.wgsl 구간 1 와도 소산 uniform | A 판 차이 | `ebca435:shaders/Pass3_NLSW.wgsl:38` `vort_friction_factor: f32,` / 추가 줄 없음 이력 본판: `35b7f1c` 2026-01-15; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판의 vort_friction_factor는 후속 추가 기능이다. transect 판에는 이 uniform이 없다. |
| CT1-211 | shaders/Pass3_NLSW.wgsl 구간 2 천수 적분 스텐실과 마찰 | F 표기 차이 | `ebca435:shaders/Pass3_NLSW.wgsl:100` `if (idx.x >= globals.width - 2 \|\| idx.y >= globals.height - 2 \|\| idx.x <= 1 \|\| idx.y <= 1) {` / `ebca435:transect_version/shaders/Pass3_NLSW.wgsl:100` `if (idx.x >= globals.width - 2 \|\| idx.x <= 1) {` | transect 판은 x 경계에서만 조기 반환한다. 동·서 건조 검사와 x flux만 남긴다. v=0을 마찰 함수에 넣는다. y 미분과 횡운동량이 0이면 본판 와도 소산도 0이다. |
| CT1-212 | shaders/Pass3_NLSW.wgsl 구간 3 압력과 백수 확산의 1D 환원 | F 표기 차이 | `ebca435:shaders/Pass3_NLSW.wgsl:189` `let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;` / `ebca435:transect_version/shaders/Pass3_NLSW.wgsl:178` `// let P_down = textureLoad(txBoundaryForcing, downIdx, 0).x;` | x 압력 차분은 같다. transect 판은 y 압력 차분과 Dxy·Dyy의 백수 확산을 생략한다. |
| CT1-213 | shaders/Pass3_NLSW.wgsl 구간 4 해안선 기울기 보정 | F 표기 차이 | `ebca435:shaders/Pass3_NLSW.wgsl:223` `if (h_min.x <= h_cut && h_min.z <= h_cut) {` / `ebca435:transect_version/shaders/Pass3_NLSW.wgsl:212` `// if (h_min.x <= h_cut && h_min.z <= h_cut) {` | transect 판은 y 기울기 보정을 생략한다. 동·서 면의 일방향 x 차분은 유지한다. |
| CT1-214 | shaders/Pass3_NLSW.wgsl 구간 5 천수 source와 flux 발산 | F 표기 차이 | `ebca435:shaders/Pass3_NLSW.wgsl:248` `let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);` / `ebca435:transect_version/shaders/Pass3_NLSW.wgsl:238` `let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + press_x, 0.0, hc_by_dx_dx + c_dissipation);` | y 미분=0과 Q=0을 본판 식에 대입하면 transect 식이 된다. 침투와 백수 감쇠의 부호는 같다. Euler·AB3·AM4 계수는 이 구간 밖에서 동일하다. |
| CT1-215 | shaders/Pass3_NLSW.wgsl 구간 6 불필요한 분산 이력 쓰기 생략 | F 표기 차이 | `ebca435:shaders/Pass3_NLSW.wgsl:280` `let F_G_vec = vec4<f32>(0.0, 0.0, 0.0, 1.0);` / `ebca435:transect_version/shaders/Pass3_NLSW.wgsl:271` `// let F_G_vec = vec4<f32>(0.0, 0.0, 0.0, 1.0);` | NLSW는 분산 솔브를 건너뛴다. transect 판은 사용하지 않는 F_G_star 쓰기를 주석 처리한다. |
| CT1-216 | shaders/Pass_Breaking.wgsl 구간 1 쇄파 x 이웃 | F 표기 차이 | `ebca435:shaders/Pass_Breaking.wgsl:36` `let downIdx = idx + vec2<i32>(0, -1);` / `ebca435:transect_version/shaders/Pass_Breaking.wgsl:36` `// let downIdx = idx + vec2<i32>(0, -1);` | transect 판은 y flux와 y·대각 이웃을 읽지 않는다. |
| CT1-217 | shaders/Pass_Breaking.wgsl 구간 2 쇄파 나이 전파와 x gradient | F 표기 차이 | `ebca435:shaders/Pass_Breaking.wgsl:62` `if (abs(P_here) > abs(Q_here) ) {` / `ebca435:transect_version/shaders/Pass_Breaking.wgsl:85` `t_here = max(t_here, t1);` | transect 판은 P_here의 부호로 x 상류 이웃 t1만 사용한다. Q=0인 1D에서 y 방향 gradient와 횡응력은 0이다. |
| CT1-218 | shaders/Pass_Breaking.wgsl 구간 3 쇄파 점성 상한의 길이척도 | C 문서 누락 | `ebca435:shaders/Pass_Breaking.wgsl:125` `let nu_breaking = min(1.0 * globals.dx * globals.dy / globals.dt, B_Breaking * globals.delta_breaking * h_here * detadt);` / `ebca435:transect_version/shaders/Pass_Breaking.wgsl:128` `let nu_breaking = min(1.0 * globals.dx * globals.dx / globals.dt, B_Breaking * globals.delta_breaking * h_here * detadt);` | transect 판은 점성 상한을 dx*dx/dt로 둔다. 본판은 dx*dy/dt다. 둘 다 길이제곱/시간 단위다. dx==dy일 때만 수치가 같다. 독립 단면의 x 격자 척도를 쓰는 의도된 단순화다. |
| CT1-219 | shaders/Pass_Breaking.wgsl 구간 4 쇄파 응력 출력 | F 표기 차이 | `ebca435:shaders/Pass_Breaking.wgsl:135` `let nu_dPdy = nu_total * dPdy;` / `ebca435:transect_version/shaders/Pass_Breaking.wgsl:144` `let nu_flux = vec4<f32>(nu_dPdx, 0.0, 0.0, 0.0);` | transect 판은 nu_dPdx만 첫 채널에 저장한다. 나머지 응력 채널은 0.0이다. |
| CT1-220 | shaders/SedTrans_Pass1.wgsl 구간 1 퇴적물 limiter | E 코드 결함 후보 (중간) | `ebca435:shaders/SedTrans_Pass1.wgsl:96` `let TWO_THETAc = 2.0; //globals.TWO_THETA * rampcoef + 2.0 * (1.0 - rampcoef);  // transition to full upwinding with overland flow, start transition at base_depth/50.` / `ebca435:transect_version/shaders/SedTrans_Pass1.wgsl:96` `let TWO_THETAc = globals.TWO_THETA * rampcoef + 2.0 * (1.0 - rampcoef);  // transition to full upwinding with overland flow, start transition at base_depth/50.` 반대 근거·두 경로 대조: 퇴적물 limiter 한쪽 수정 절. | 본판은 TWO_THETAc=2.0으로 고정한다. transect 판은 wetdry/base_depth의 rampcoef로 globals.TWO_THETA와 2.0을 섞는다. 기본 Theta=2.0이면 충분히 젖은 곳의 값은 4.0까지 간다. x 단면과 무관한 계수 차이다. |
| CT1-221 | shaders/SedTrans_Pass3.wgsl 구간 1 퇴적물 closure uniform | A 판 차이 | `ebca435:shaders/SedTrans_Pass3.wgsl:22` `base_depth: f32,` / 추가 줄 없음 이력 본판: `22e1983` 2025-06-06, `5c60ac0` 2025-06-07, `b8b50c3` 2025-06-08, `ba9eb67` 2025-06-09; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판에는 base_depth·delta·확산계수·MPM 계수가 없다. 본판의 후속 퇴적물 모델 확장과 연결된다. |
| CT1-222 | shaders/SedTrans_Pass3.wgsl 구간 2 퇴적물 입력 binding | A 판 차이 | `ebca435:shaders/SedTrans_Pass3.wgsl:45` `@group(0) @binding(13) var txBreaking: texture_2d<f32>;` / 추가 줄 없음 이력 본판: `22e1983` 2025-06-06, `2a7452d` 2025-06-07, `b8b50c3` 2025-06-08; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판에는 쇄파·면속도·면농도·hardbottom 리소스가 없다. |
| CT1-223 | shaders/SedTrans_Pass3.wgsl 구간 3 퇴적물 셀 상태 읽기 위치 | A 판 차이 | `ebca435:shaders/SedTrans_Pass3.wgsl:71` `let B = textureLoad(txBottom, idx, 0).z;` / 추가 줄 없음 이력 본판: `2a7452d` 2025-06-07, `852ec28` 2025-06-13; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 B·eta·hu·hv·h를 앞에서 읽는다. transect 판은 뒤에서 읽는다. 뒤 식에 같은 값이 들어가는 읽기 위치 자체는 동작 차이가 없다. |
| CT1-224 | shaders/SedTrans_Pass3.wgsl 구간 4 퇴적물 확산과 수심 역수 | E 코드 결함 후보 (강함) | `ebca435:shaders/SedTrans_Pass3.wgsl:86` `var c4 = textureLoad(txSed_C1, idx, 0);` / `ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:67` `let C_state_here = textureLoad(txState_Sed, idx, 0);` 반대 근거·두 경로 대조: 퇴적물 수심 정규화와 단면 간 확산 절. | transect 판은 Dxx=Dxy=Dyy=1.0으로 인접 단면과 혼합한다. transect 판은 divide_by_h=2.0*h/sqrt(h2+max(h2,epsilon))를 쓴다. 젖은 곳에서 이 값은 1/h가 아닌 sqrt(2)에 접근한다. hu에 이 값을 곱하면 유속 단위가 맞지 않는다. 마찰의 절반 계수·추가 divide_by_h·hardbottom 검사 없음·bedload 없음·침강 제한식 변경도 같은 hunk에 있다. 본판의 후속 퇴적물 수정 이력을 근거로 E로 둔다. |
| CT1-225 | shaders/SedTrans_Pass3.wgsl 구간 5 퇴적물 비음수 보정과 바닥 전달 | E 코드 결함 후보 (강함) | `ebca435:shaders/SedTrans_Pass3.wgsl:235` `newState = max(newState, vec4<f32>(0.0, 0.0, 0.0, 0.0)); // ensure no negative concentrations` / `ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:138` `textureStore(erosion_Sed, idx, vec4<f32>(erosion, 0.0, 0.0, 0.0));` 반대 근거·두 경로 대조: 퇴적물 수심 정규화와 단면 간 확산 절. | 본판은 newState를 0 이상으로 제한한다. transect 판은 해당 제한이 없다. 본판은 침식·침강을 역수심으로 변환하고 침식 출력에 bedload 발산을 더한다. transect 판은 직접 erosion/deposition을 저장한다. E의 핵심은 서로 다른 수심 정규화와 한쪽 농도 보정 수정이다. |
| CT1-226 | shaders/SedTrans_UpdateBottom.wgsl 구간 1 지형 갱신 경계 uniform | A 판 차이 | `ebca435:shaders/SedTrans_UpdateBottom.wgsl:11` `west_boundary_type: i32,` / 추가 줄 없음 이력 본판: `22e1983` 2025-06-06; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 4변 경계 유형을 받아 입사 경계의 지형변화를 ramp로 억제한다. |
| CT1-227 | shaders/SedTrans_UpdateBottom.wgsl 구간 2 진단 전용 지형변화 입력 | C 문서 누락 | `ebca435:shaders/SedTrans_UpdateBottom.wgsl:25` `@group(0) @binding(7) var txHardBottom: texture_2d<f32>;` / `ebca435:transect_version/shaders/SedTrans_UpdateBottom.wgsl:30` `var dB_cumulative = textureLoad(txBotChange_Sed, idx, 0);` | transect 판은 hardbottom·초기 바닥고·외곽 셀 조기 반환을 쓰지 않는다. 북쪽·동쪽 이웃으로 진단 면 변화량을 계산한다. HTML의 no feedback 안내와 연결된다. |
| CT1-228 | shaders/SedTrans_UpdateBottom.wgsl 구간 3 바닥고 고정과 누적 변화량 | C 문서 누락 | `ebca435:shaders/SedTrans_UpdateBottom.wgsl:60` `let e_left =  textureLoad(erosion_Sed, leftIdx, 0).x;` / `ebca435:transect_version/shaders/SedTrans_UpdateBottom.wgsl:41` `let dB_here = globals.dt * (e_here - d_here) / (1.0 - globals.sedC1_n); // this is positive when eroding - when increasing depth, or decreasing elevation` | transect 판은 B_here=B_here로 현재 바닥고를 유지한다. 진단 누적값에는 -dB를 적산한다. 본판은 B_here-dB를 수리에 돌려주고 초기 바닥고와의 차이로 누적량을 만든다. 의도 근거가 있으므로 바닥고 고정 자체를 결함으로 판정하지 않는다. 동쪽 면 평균은 본판이 0.75*현재+0.25*이웃인 데 비해 transect는 0.5*현재+0.5*이웃이다. |
| CT1-229 | shaders/TriDiag_PCRx.wgsl 구간 1 PCR 최종 반복 uniform | A 판 차이 | `ebca435:shaders/TriDiag_PCRx.wgsl:7` `P: i32,` / 추가 줄 없음 이력 본판: `984091f` 2026-05-24; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 P를 받아 최종 반복에서만 상태를 저장한다. transect 판은 모든 반복에서 저장한다. |
| CT1-230 | shaders/TriDiag_PCRx.wgsl 구간 2 PCR 상태 읽기 위치 | F 표기 차이 | `ebca435:shaders/TriDiag_PCRx.wgsl:22` `// CODEX: CurrentState is only needed on the final PCR pass now.` / `ebca435:transect_version/shaders/TriDiag_PCRx.wgsl:20` `let CurrentState = textureLoad(current_state, idx, 0);` | 본판은 최종 반복에서만 상태를 읽는다. transect 판은 반복마다 읽는다. 최종 반복에 쓰는 상태와 PCR 점화식은 같다. |
| CT1-231 | shaders/TriDiag_PCRx.wgsl 구간 3 PCR 중간 상태 저장 | F 표기 차이 | `ebca435:shaders/TriDiag_PCRx.wgsl:101` `if (globals.p == globals.P - 1) {` / `ebca435:transect_version/shaders/TriDiag_PCRx.wgsl:92` `let txtemp2_out = vec4<f32>(CurrentState.r, dOut, CurrentState.b, CurrentState.a);` | 본판은 p==P-1일 때만 txtemp2를 쓴다. transect 판은 반복마다 쓴다. 최종 반복 뒤의 상태 복사 결과는 같다. y 셰이더는 transect 실행 경로에서 호출되지 않는다. |
| CT1-232 | shaders/TriDiag_PCRx_COULWAVE.wgsl 구간 1 COULWAVE PCR 상태 읽기 | F 표기 차이 | `ebca435:shaders/TriDiag_PCRx_COULWAVE.wgsl:24` `// CODEX: CurrentState is only needed on the final PCR pass now.` / `ebca435:transect_version/shaders/TriDiag_PCRx_COULWAVE.wgsl:24` `let CurrentState = textureLoad(current_state, idx, 0);` | transect 판은 모든 반복에서 CurrentState를 읽는다. 본판은 최종 반복에서 읽는다. |
| CT1-233 | shaders/TriDiag_PCRx_COULWAVE.wgsl 구간 2 COULWAVE PCR 최종 환산 | F 표기 차이 | `ebca435:shaders/TriDiag_PCRx_COULWAVE.wgsl:102` `if(globals.p == globals.Px - 1) {` / `ebca435:transect_version/shaders/TriDiag_PCRx_COULWAVE.wgsl:95` `if(globals.p == globals.Px - 1) {  // for COULWAVE need to convert velocity back to flux` | 양쪽은 최종 반복에서 dOut에 H_loc를 곱해 속도를 운동량으로 환산한다. transect 판은 모든 반복에서 상태 staging을 쓴다. 본판은 최종 반복에서만 쓴다. 최종 결과식은 같다. y 셰이더는 transect 실행 경로에서 호출되지 않는다. |
| CT1-234 | shaders/TriDiag_PCRy.wgsl 구간 1 PCR 최종 반복 uniform | A 판 차이 | `ebca435:shaders/TriDiag_PCRy.wgsl:7` `P: i32,` / 추가 줄 없음 이력 본판: `984091f` 2026-05-24; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 P를 받아 최종 반복에서만 상태를 저장한다. transect 판은 모든 반복에서 저장한다. |
| CT1-235 | shaders/TriDiag_PCRy.wgsl 구간 2 PCR 상태 읽기 위치 | F 표기 차이 | `ebca435:shaders/TriDiag_PCRy.wgsl:22` `// CODEX: CurrentState is only needed on the final PCR pass now.` / `ebca435:transect_version/shaders/TriDiag_PCRy.wgsl:20` `let CurrentState = textureLoad(current_state, idx, 0);` | 본판은 최종 반복에서만 상태를 읽는다. transect 판은 반복마다 읽는다. 최종 반복에 쓰는 상태와 PCR 점화식은 같다. |
| CT1-236 | shaders/TriDiag_PCRy.wgsl 구간 3 PCR 중간 상태 저장 | F 표기 차이 | `ebca435:shaders/TriDiag_PCRy.wgsl:101` `if (globals.p == globals.P - 1) {` / `ebca435:transect_version/shaders/TriDiag_PCRy.wgsl:92` `let txtemp2_out = vec4<f32>(CurrentState.r, CurrentState.g, dOut, CurrentState.a);` | 본판은 p==P-1일 때만 txtemp2를 쓴다. transect 판은 반복마다 쓴다. 최종 반복 뒤의 상태 복사 결과는 같다. y 셰이더는 transect 실행 경로에서 호출되지 않는다. |
| CT1-237 | shaders/TriDiag_PCRy_COULWAVE.wgsl 구간 1 COULWAVE PCR 상태 읽기 | F 표기 차이 | `ebca435:shaders/TriDiag_PCRy_COULWAVE.wgsl:24` `// CODEX: CurrentState is only needed on the final PCR pass now.` / `ebca435:transect_version/shaders/TriDiag_PCRy_COULWAVE.wgsl:24` `let CurrentState = textureLoad(current_state, idx, 0);` | transect 판은 모든 반복에서 CurrentState를 읽는다. 본판은 최종 반복에서 읽는다. |
| CT1-238 | shaders/TriDiag_PCRy_COULWAVE.wgsl 구간 2 COULWAVE PCR 최종 환산 | F 표기 차이 | `ebca435:shaders/TriDiag_PCRy_COULWAVE.wgsl:102` `if(globals.p == globals.Py - 1) {` / `ebca435:transect_version/shaders/TriDiag_PCRy_COULWAVE.wgsl:95` `if(globals.p == globals.Py - 1) {  // for COULWAVE need to convert velocity back to flux` | 양쪽은 최종 반복에서 dOut에 H_loc를 곱해 속도를 운동량으로 환산한다. transect 판은 모든 반복에서 상태 staging을 쓴다. 본판은 최종 반복에서만 쓴다. 최종 결과식은 같다. y 셰이더는 transect 실행 경로에서 호출되지 않는다. |
| CT1-239 | shaders/Update_TriDiag_coef.wgsl 구간 1 Boussinesq near-dry 차단 불일치 | E 코드 결함 후보 (중간) | `ebca435:shaders/Update_TriDiag_coef.wgsl:26` `let height = i32(globals.height);` / `ebca435:transect_version/shaders/Update_TriDiag_coef.wgsl:34` `let near_dry = d_here; //textureLoad(txBottom, idx, 0).w;` 반대 근거·두 경로 대조: near-dry 차단 불일치 절. | transect 판은 near_dry를 txBottom.w 대신 d_here로 둔다. 같은 판 Pass3_Bous는 txBottom.w>0일 때만 분산 source를 더한다. 해석: 해안 근처에서 명시 분산 source 차단과 암시 계수 차단이 달라질 수 있다. 자기 주석과 다른 분산 경로의 모순을 중간으로 둔다. |
| CT1-240 | shaders/Update_TriDiag_coef.wgsl 구간 2 표준 계수 파일의 COULWAVE 대안 | C 문서 누락 | `ebca435:shaders/Update_TriDiag_coef.wgsl:54` `let z_loc = textureLoad(current_state, idx, 0).x;` / `ebca435:transect_version/shaders/Update_TriDiag_coef.wgsl:54` `let z_loc = 0.0; //textureLoad(current_state, idx, 0).x;` | transect 판은 표준 파일의 NLSW_or_Bous==2 분기에서 z_loc와 zx_loc를 0.0으로 둔다. 실제 mode 2는 별도 COULWAVE 계수 파일을 fetch한다. 이 변경은 현재 실행 경로에서 호출되지 않는 대안이다. |
| CT1-241 | shaders/Update_TriDiag_coef.wgsl 구간 3 Boussinesq y 계수 생략 | F 표기 차이 | `ebca435:shaders/Update_TriDiag_coef.wgsl:75` `var coefy = vec4<f32>(0.0, 0.0, 0.0, 0.0);` / `ebca435:transect_version/shaders/Update_TriDiag_coef.wgsl:75` `// var coefy = vec4<f32>(0.0, 0.0, 0.0, 0.0);` | transect 판은 coefMaty 계산과 저장을 생략한다. y PCR도 실행하지 않는다. |
| CT1-242 | shaders/Update_TriDiag_coef_COULWAVE.wgsl 구간 1 COULWAVE 계수 x 이웃 | F 표기 차이 | `ebca435:shaders/Update_TriDiag_coef_COULWAVE.wgsl:27` `let height = i32(globals.height);` / `ebca435:transect_version/shaders/Update_TriDiag_coef_COULWAVE.wgsl:27` `// let height = i32(globals.height);` | transect 판은 y 이웃 변수 선언을 생략한다. 현재 eta와 x 기울기·za·수심을 쓰는 x 계수식은 같다. |
| CT1-243 | shaders/Update_TriDiag_coef_COULWAVE.wgsl 구간 2 COULWAVE y 계수 생략 | F 표기 차이 | `ebca435:shaders/Update_TriDiag_coef_COULWAVE.wgsl:83` `var coefy = vec4<f32>(0.0, 0.0, 0.0, 0.0);` / `ebca435:transect_version/shaders/Update_TriDiag_coef_COULWAVE.wgsl:83` `// var coefy = vec4<f32>(0.0, 0.0, 0.0, 0.0);` | transect 판은 y 계수와 y RHS 정규화를 계산하지 않는다. y PCR 생략과 일치한다. |
| CT1-244 | shaders/Update_neardry.wgsl 구간 1 near-dry 셰이더 검사 | F 표기 차이 | `ebca435:shaders/Update_neardry.wgsl:21` `for (var yy = idx.y - lengthCheck; yy <= idx.y + lengthCheck; yy += 1)` / `ebca435:transect_version/shaders/Update_neardry.wgsl:28` `let idx_C = vec2<i32>(xC, idx.y);` | transect 판은 ±3칸의 x 이웃만 검사한다. 현재 단면의 y 인덱스는 고정한다. |
| CT1-245 | shaders/Update_neardry.wgsl 구간 2 단일점 섬 보정의 1D 선택 | C 문서 누락 | `ebca435:shaders/Update_neardry.wgsl:40` `let downIdx = idx + vec2<i32>(0, -1);` / `ebca435:transect_version/shaders/Update_neardry.wgsl:49` `if(B_west < 0.0 && B_east < 0.0) {` | transect 판은 동·서가 모두 음의 바닥고인 양의 중심 고도를 0으로 만든다. 북·남 면 보정은 하지 않는다. 초기 CPU 단일점 제거는 별도로 꺼져 있다. |
| CT1-246 | shaders/fragment.wgsl 구간 1 표시 uniform 확장 | A 판 차이 | `ebca435:shaders/fragment.wgsl:58` `disturbanceType: f32,` / 추가 줄 없음 이력 본판: `d23dfb0` 2025-09-01, `d778fe7` 2026-06-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 교란 유형과 선형 구조물 미리보기 상태를 받는다. |
| CT1-247 | shaders/fragment.wgsl 구간 2 실제 바닥고 변화 표시 | A 판 차이 | `ebca435:shaders/fragment.wgsl:290` `let depth_change = textureSample(bottomTexture, textureSampler, uv).b - textureSample(erosion_Sed, textureSampler, uv).b;` / 추가 줄 없음 이력 본판: `8c2b62b` 2025-08-24; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 현재 바닥고와 초기 바닥고의 차이를 읽는다. transect 판은 erosion 입력을 실제 침식률 표시용으로 쓴다. |
| CT1-248 | shaders/fragment.wgsl 구간 3 퇴적물 표시 채널 | E 코드 결함 후보 (중간) | `ebca435:shaders/fragment.wgsl:371` `} else if (surfaceToPlot == 19) {  // available scour depth` / `ebca435:transect_version/shaders/fragment.wgsl:362` `} else if (surfaceToPlot == 21) {  // sed C1 net deposition` 반대 근거·두 경로 대조: 중심 지형변화 표시 채널 절. | 본판은 가용 깊이 surface 19를 제공한다. 본판의 누적 지형변화 surface 21은 중심 바닥고인 b 채널이다. transect 판은 북쪽 면인 r 채널을 표시한다. 본판은 surface 21에서 최대 eta로 육상 표시 범위를 확장한다. |
| CT1-249 | shaders/fragment.wgsl 구간 4 렌더 영역 길이 정의 | E 코드 결함 후보 (중간) | `ebca435:shaders/fragment.wgsl:393` `let width = f32(globals.WIDTH - 1) * globals.dx;` / `ebca435:transect_version/shaders/fragment.wgsl:379` `let width = f32(globals.WIDTH) * globals.dx;` 반대 근거·두 경로 대조: 렌더 격자 길이와 고도 읽기 한쪽 수정 절. | 본판은 (WIDTH-1)*dx와 (HEIGHT-1)*dy를 쓴다. transect 판은 WIDTH*dx와 HEIGHT*dy를 쓴다. 격자점 끝을 세는지 셀 수를 세는지의 차이가 표시 길이를 한 격자간격 바꾼다. |
| CT1-250 | shaders/fragment.wgsl 구간 5 육상 이동 사면 색상 | A 판 차이 | `ebca435:shaders/fragment.wgsl:578` `if (abs(depth_change) > globals.delta && globals.disturbanceType == 5) {  // make slide mass gray` / `ebca435:transect_version/shaders/fragment.wgsl:563` `if(globals.IsOverlayMapLoaded == 1) {` 이력 본판: `8c2b62b` 2025-08-24, `d23dfb0` 2025-09-01; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 disturbanceType==5이고 변화량이 delta를 넘으면 회색 사면을 표시한다. transect 판은 overlay·일반 육상 색상을 쓴다. |
| CT1-251 | shaders/fragment.wgsl 구간 6 화살표 텍스처 레이어 | A 판 차이 | `ebca435:shaders/fragment.wgsl:783` `var layer = 9;` / `ebca435:transect_version/shaders/fragment.wgsl:764` `let layer = 9;` 이력 본판: `3c1649b` 2026-02-11; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 사실적 표시에서 채워진 화살표 레이어 10을 쓴다. transect 판은 레이어 9를 쓴다. |
| CT1-252 | shaders/fragment.wgsl 구간 7 선형 구조물 미리보기 | A 판 차이 | `ebca435:shaders/fragment.wgsl:804` `if (globals.designcomponent_PreviewOn == 1) {` / 추가 줄 없음 이력 본판: `d778fe7` 2026-06-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 끝점 점과 선분을 검게 표시한다. transect 판에는 미리보기 경로가 없다. |
| CT1-253 | shaders/vertex3D.wgsl 구간 1 3D 고도 샘플과 영역 길이 | E 코드 결함 후보 (중간) | `ebca435:shaders/vertex3D.wgsl:78` `var elev = textureLoad(etaTexture, vec2<i32>(i32(out.uv.x * f32(globals.WIDTH - 1)), i32(out.uv.y * f32(globals.HEIGHT - 1))), 0).r;` / `ebca435:transect_version/shaders/vertex3D.wgsl:77` `let elev = textureSampleLevel(txRenderVarsf16, textureSampler_linear, out.uv, 0, 0.0).r;` 반대 근거·두 경로 대조: 렌더 격자 길이와 고도 읽기 한쪽 수정 절. | transect 판은 f16 표시 텍스처를 선형 샘플링한다. 본판은 etaTexture를 정수 좌표로 직접 읽는다. transect 판은 W*dx·H*dy를 쓴다. 본판은 (W-1)*dx·(H-1)*dy를 쓴다. 고도 정밀도·보간·끝점 위치가 다르다. |
| CT1-254 | js/main.js 구간 1 초기화 모듈 연결 | C 문서 누락 | `ebca435:js/main.js:5` `import { loadDepthSurface, loadInitCondSurface, loadFrictionSurface, loadHardBottomSurface, loadWaveData, loadBoundaryTimeSeriesData, loadOverlay, CreateGoogleMapImage, calculateGoogleMapScaleAndOffset, loadImageBitmap, loadUserImage, loadCubeBitmaps} from './File_Loader.js';  // load depth surface and wave data file` / `ebca435:transect_version/js/main.js:3` `import { loadDepthSurface, loadFrictionSurface, loadTransectWaveData, loadWaveData, loadOverlay, CreateGoogleMapImage, calculateGoogleMapScaleAndOffset, loadImageBitmap, loadUserImage, loadCubeBitmaps} from './File_Loader.js';  // load depth surface and wave data file` | transect 판은 단면 파랑 reader와 uploader를 import한다. 본판은 초기 수면·hardbottom·경계 시계열·중첩 writer·파 생성기를 import한다. |
| CT1-255 | js/main.js 구간 2 호스트 모듈 연결 | A 판 차이 | `ebca435:js/main.js:40` `import { create_ExtractNestedBoundaryTimeSeries_BindGroupLayout, create_ExtractNestedBoundaryTimeSeries_BindGroup } from './Handler_ExtractNestedBoundaryTimeSeries.js';` / `ebca435:transect_version/js/main.js:31` `import { fetchShader, runComputeShader, runCopyTextures } from './Run_Compute_Shader.js';  // function to run shaders, works for all` 이력 본판: `bb99fee` 2026-07-02, `3646fc8` 2026-02-08, `0ee5174` 2026-06-18; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 중첩 경계 handler·EncStack·agent_controls를 import한다. transect 판은 즉시 submit 함수를 쓴다. |
| CT1-256 | js/main.js 구간 3 선형 구조물과 전체화면 상태 | A 판 차이 | `ebca435:js/main.js:66` `let pseudoFullscreenActive = false;` / 추가 줄 없음 이력 본판: `24b8f13` 2026-05-24, `0ee5174` 2026-06-18, `d778fe7` 2026-06-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 가상 전체화면 플래그와 외부 제어 모드를 둔다. 본판은 선형 구조물 양끝점 표시와 적용 후 초기화를 구현한다. |
| CT1-257 | js/main.js 구간 4 URL 케이스 초기화 | A 판 차이 | `ebca435:js/main.js:122` `function postAgentCaseStatus(status, payload = {}) {` / `ebca435:transect_version/js/main.js:67` `async function OrderedFunctions(configContent, bathymetryContent, waveContent) {` 이력 본판: `f6fd78b` 2026-06-04, `0ee5174` 2026-06-18, `bb99fee` 2026-07-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 agent_case·autostart 쿼리를 읽고 manifest의 config·bathy·waves·선택 overlay·초기 수면을 fetch한다. 로딩 상태는 부모 창으로 postMessage한다. transect 판에는 해당 진입 경로가 없다. |
| CT1-258 | js/main.js 구간 5 단면 파랑 읽기와 초기화 인자 | C 문서 누락 | `ebca435:js/main.js:206` `let { numberOfWaves, waveData } = await loadWaveData(waveContent, calc_constants);  // Start this only after the first function completes` / `ebca435:transect_version/js/main.js:79` `let waveData = await loadTransectWaveData(waveContent, calc_constants);  // Start this only after the first function completes` | transect 판은 loadTransectWaveData를 호출한다. 성분 수는 config 값을 유지한다. 초기화 함수는 config·bathy·waves·overlay·model·friction의 6인자를 받는다. 본판은 초기 수면·hardbottom·4변 시계열을 추가로 받는다. |
| CT1-259 | js/main.js 구간 6 GPU 장치 요청과 오류 기록 | A 판 차이 | `ebca435:js/main.js:249` `const requestedMaxTextureDimension2D = adapter.limits?.maxTextureDimension2D \|\| 8192;` / `ebca435:transect_version/js/main.js:118` `requiredLimits: {},` 이력 본판: `bb99fee` 2026-07-02, `769d990` 2026-02-01, `7ae7da4` 2026-02-23; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 adapter의 2D 텍스처 최대 길이를 요청한다. 본판은 device lost와 uncapturederror를 기록한다. transect 판은 기본 requiredLimits를 쓴다. |
| CT1-260 | js/main.js 구간 7 파 생성과 type5 시간 보간 | A 판 차이 | `ebca435:js/main.js:294` `const boundaryTimeSeriesFiles = {` / `ebca435:transect_version/js/main.js:137` `let { bathy2D, waveData } = await OrderedFunctions(configContent, bathymetryContent, waveContent);` 이력 본판: `bb99fee` 2026-07-02, `9093d7f` 2026-06-01; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 원래 파 스펙트럼을 복사해 보존한다. 본판은 UI sine/TMA 생성과 텍스처 재업로드를 지원한다. type5는 시간 이진 탐색과 선형 보간을 쓴다. 마지막 시각 뒤는 영 상태 행을 선택한다. transect 판은 단면 파랑을 한 번 읽는다. |
| CT1-261 | js/main.js 구간 8 uniform·공용 readback 버퍼 | A 판 차이 | `ebca435:js/main.js:416` `let Render_bufferSize = 304; // 304 bytes for render pipeline, 256 for compute pipeline` / `ebca435:transect_version/js/main.js:160` `let Render_bufferSize = 272; // 272 bytes for render pipeline, 256 for compute pipeline` 이력 본판: `bb99fee` 2026-07-02, `c4be488` 2026-07-13, `d778fe7` 2026-06-02, `09cfd76` 2026-02-15; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판 Render_bufferSize는 304이고 transect는 272다. 본판만 표면 출력용 공용 readback 버퍼를 할당한다. 두 판은 동일한 256배수 행 길이 식을 사용한다. |
| CT1-262 | js/main.js 구간 9 표시 샘플러 반복 방식 | C 문서 누락 | `ebca435:js/main.js:441` `addressModeU: 'mirror-repeat',` / `ebca435:transect_version/js/main.js:176` `addressModeU: 'repeat',` | transect 판은 U/V 주소 모드 repeat를 쓴다. 본판은 mirror-repeat를 쓴다. 텍스처 경계 밖의 표시 샘플이 다르다. 계산 flux에는 영향이 없다. |
| CT1-263 | js/main.js 구간 10 hardbottom 텍스처 | A 판 차이 | `ebca435:js/main.js:469` `const txHardBottom = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores hard bottom elevation` / 추가 줄 없음 이력 본판: `4353b85` 2025-06-09; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 txHardBottom을 할당한다. |
| CT1-264 | js/main.js 구간 11 구면 계량 텍스처 | A 판 차이 | `ebca435:js/main.js:509` `const txSphericalMetrics = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);` / 추가 줄 없음 이력 본판: `afc1fe7` 2026-06-19; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 txSphericalMetrics를 할당한다. |
| CT1-265 | js/main.js 구간 12 단면별 파랑 리소스와 초기상태 | C 문서 누락 | `ebca435:js/main.js:553` `const txSamplePNGs = create_3D_Image_Texture(device, 1024, 1024, 11, allTextures); // will store all textures to be sampled for photo-realism` / `ebca435:transect_version/js/main.js:285` `const txSamplePNGs = create_3D_Image_Texture(device, 1024, 1024, 10, allTextures); // will store all textures to be sampled for photo-realism` | transect 판은 Nwave×HEIGHT의 txWaves_Transect를 할당하고 단면 파랑을 업로드한다. 일반 txWaves는 할당하지만 업로드하지 않는다. 본판은 파 생성 용량과 4변 시계열 텍스처를 할당한다. transect 표시 레이어는 10개 영상·2개 f16이고 본판은 11개 영상·3개 f16이다. 본판만 초기 수면과 hardbottom 파일을 읽는다. 초기 상태 API의 차이는 uploader 행과 같다. |
| CT1-266 | js/main.js 구간 13 지도 실패 플래그 대입 | E 코드 결함 후보 (강함) | `ebca435:js/main.js:680` `catch (error) {` / `ebca435:transect_version/js/main.js:353` `catch {` 반대 근거·두 경로 대조: 지도 실패 처리 절. | transect 판의 catch는 GoogleMapOverlay==0을 비교만 한다. 본판은 =0으로 대입하고 로드 플래그 둘도 0으로 초기화한다. 자기 catch 목적과 실제 대입이 모순한다. 본판의 한쪽 수정이다. |
| CT1-267 | js/main.js 구간 14 화살표 영상 레이어 | A 판 차이 | `ebca435:js/main.js:756` `imageUrl = '/textures/arrow_filled.png';` / 추가 줄 없음 이력 본판: `3c1649b` 2026-02-11; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 채워진 화살표를 레이어 10에 업로드한다. 영상 내용은 판독하지 않는다. |
| CT1-268 | js/main.js 구간 15 카메라 초기화 좌표 | A 판 차이 | `ebca435:js/main.js:830` `const explorerCameraDegToRad = Math.PI / 180.0;` / `ebca435:transect_version/js/main.js:503` `0.1 * simWidth,` 이력 본판: `afc1fe7` 2026-06-19, `f183cc2` 2026-02-01; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 구면 각도 격자를 미터 척도로 바꾼다. 본판은 사용자 카메라 위치·yaw·pitch·lookDist를 적용한다. transect 판은 simWidth·simHeight의 Cartesian 기본 카메라를 쓴다. |
| CT1-269 | js/main.js 구간 16 사용자 카메라 회전 | A 판 차이 | `ebca435:js/main.js:935` `if (calc_constants.cameraInit_user == 1) {` / 추가 줄 없음 이력 본판: `f183cc2` 2026-02-01; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 사용자 yaw·pitch를 초기 각도로 적용한다. |
| CT1-270 | js/main.js 구간 17 재구성 경사 격자간격 | A 판 차이 | `ebca435:js/main.js:986` `const Pass1_dx_for_slope = calc_constants.grid_type == 2 ? Math.max(calc_constants.R_earth, 1.0) * Math.max(Math.abs(Math.cos(0.5 * (calc_constants.lat_LL + calc_constants.lat_UR) * Math.PI / 180.0)), 1.0e-6) * Math.max(Math.abs(calc_constants.dx) * Math.PI / 180.0, 1.0e-12) : calc_constants.dx;` / `ebca435:transect_version/js/main.js:575` `Pass1_view.setFloat32(40, calc_constants.dx, true);           // f32` 이력 본판: `afc1fe7` 2026-06-19; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 구면 격자의 각도 간격을 미터 근사값으로 바꿔 Froude 경사 제한에 전달한다. transect 판은 dx·dy를 그대로 전달한다. Cartesian 경로 값은 같다. |
| CT1-271 | js/main.js 구간 18 퇴적물 재구성 격자간격과 쇄파 입력 | A 판 차이 | `ebca435:js/main.js:1010` `SedTrans_Pass1_view.setFloat32(40, Pass1_dx_for_slope, true);           // f32` / `ebca435:transect_version/js/main.js:594` `SedTrans_Pass1_view.setFloat32(40, calc_constants.dx, true);           // f32` 이력 본판: `afc1fe7` 2026-06-19, `b8b50c3` 2025-06-08; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 동일한 구면 간격 변환을 사용한다. transect 판은 dx·dy를 그대로 쓴다. transect Pass2 바인드 그룹은 txBreaking을 받지 않는다. |
| CT1-272 | js/main.js 구간 19 Pass2 확산계수 uniform | A 판 차이 | `ebca435:js/main.js:1026` `Pass2_view.setFloat32(32, calc_constants.sedTurbDispersion, true);           // f32` / 추가 줄 없음 이력 본판: `b8b50c3` 2025-06-08; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 오프셋 32·36에 배경·쇄파 퇴적물 확산계수를 쓴다. |
| CT1-273 | js/main.js 구간 20 Pass3 binding 19 | A 판 차이 | `ebca435:js/main.js:1078` `const Pass3_BindGroup = create_Pass3_BindGroup(device, Pass3_uniformBuffer, txState, txBottom, txCW_groupings, txXFlux, txYFlux, oldGradients, oldOldGradients, predictedGradients, F_G_star_oldGradients, F_G_star_oldOldGradients, txstateUVstar, txBoundaryForcing, txNewState, dU_by_dt, predictedF_G_star, current_stateUVstar,txContSource,txBreaking, calc_constants.grid_type == 2 ? txSphericalMetrics : txDissipationFlux, txBottomFriction);` / `ebca435:transect_version/js/main.js:658` `const Pass3_BindGroup = create_Pass3_BindGroup(device, Pass3_uniformBuffer, txState, txBottom, txCW_groupings, txXFlux, txYFlux, oldGradients, oldOldGradients, predictedGradients, F_G_star_oldGradients, F_G_star_oldOldGradients, txstateUVstar, txBoundaryForcing, txNewState, dU_by_dt, predictedF_G_star, current_stateUVstar,txContSource,txBreaking, txDissipationFlux, txBottomFriction);` 이력 본판: `afc1fe7` 2026-06-19; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 grid_type==2이면 구면 계량 텍스처를 전달한다. transect 판은 항상 쇄파 응력 텍스처를 전달한다. |
| CT1-274 | js/main.js 구간 21 Pass3·퇴적물 바인딩 확장 | A 판 차이 | `ebca435:js/main.js:1117` `Pass3_view.setFloat32(144, calc_constants.vort_friction_factor, true);       // f32` / `ebca435:transect_version/js/main.js:700` `const SedTrans_Pass3_BindGroup = create_SedTrans_Pass3_BindGroup(device, SedTrans_Pass3_uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed);` 이력 본판: `35b7f1c` 2026-01-15, `afc1fe7` 2026-06-19, `b8b50c3` 2025-06-08; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 와도 소산·지구 반지름 역수를 uniform 꼬리에 쓴다. 본판의 퇴적물 적분은 추가 5개 텍스처를 받는다. |
| CT1-275 | js/main.js 구간 22 퇴적물 uniform과 단면 경계 리소스 | C 문서 누락 | `ebca435:js/main.js:1146` `SedTrans_Pass3_view.setFloat32(80, calc_constants.base_depth, true);           // f32` / `ebca435:transect_version/js/main.js:727` `const BoundaryPass_BindGroup = create_BoundaryPass_BindGroup(device, BoundaryPass_uniformBuffer, current_stateUVstar, txBottom, txWaves, txNewState_Sed, txtemp_boundary, txtemp_boundary_Sed, txBreaking, txtemp_Breaking, txWaves_Transect);` | transect 판은 퇴적물 확장 uniform을 쓰지 않는다. transect 판의 두 BoundaryPass 바인드 그룹은 txWaves_Transect를 받는다. 본판은 지형 강제장과 4변 시계열을 받는다. |
| CT1-276 | js/main.js 구간 23 경계 uniform과 x PCR 교대 바인딩 | A 판 차이 | `ebca435:js/main.js:1205` `BoundaryPass_view.setInt32(168, calc_constants.algochanges, true);           // i32` / 추가 줄 없음 이력 본판: `896c491` 2026-01-17, `bb99fee` 2026-07-02, `984091f` 2026-05-24; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 알고리즘·trough_factor·구면·시계열 uniform을 쓴다. 본판은 x PCR 계수 교대 바인드 그룹을 추가한다. |
| CT1-277 | js/main.js 구간 24 y PCR 교대 바인딩 | A 판 차이 | `ebca435:js/main.js:1240` `const TridiagY_BindGroup_BaseToA = create_Tridiag_BindGroup(device, TridiagY_uniformBuffer, coefMaty, txNewState, current_stateUVstar, newcoef_y, txtemp2_PCRy, txBottom);` / 추가 줄 없음 이력 본판: `984091f` 2026-05-24; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 y 계수 교대 바인드 그룹을 만든다. transect 판은 y PCR을 실행하지 않지만 기본 바인드 그룹은 생성한다. |
| CT1-278 | js/main.js 구간 25 바닥 갱신 바인드 그룹 | A 판 차이 | `ebca435:js/main.js:1254` `const SedTrans_UpdateBottom_BindGroup = create_SedTrans_UpdateBottom_BindGroup(device, SedTrans_UpdateBottom_uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change, txHardBottom, txBottomInitial);` / `ebca435:transect_version/js/main.js:800` `const SedTrans_UpdateBottom_BindGroup = create_SedTrans_UpdateBottom_BindGroup(device, SedTrans_UpdateBottom_uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change);` 이력 본판: `852ec28` 2025-06-13; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 hardbottom과 초기 바닥고를 전달한다. |
| CT1-279 | js/main.js 구간 26 바닥 갱신 경계 uniform | A 판 차이 | `ebca435:js/main.js:1266` `SedTrans_UpdateBottom_view.setInt32(36, calc_constants.west_boundary_type, true);       // i32` / 추가 줄 없음 이력 본판: `22e1983` 2025-06-06; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 오프셋 36·40·44·48에 4변 경계 유형을 쓴다. |
| CT1-280 | js/main.js 구간 27 평균 수면 입력 | A 판 차이 | `ebca435:js/main.js:1297` `const CalcMeans_BindGroup = create_CalcMeans_BindGroup(device, CalcMeans_uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC, txNewState);` / `ebca435:transect_version/js/main.js:839` `const CalcMeans_BindGroup = create_CalcMeans_BindGroup(device, CalcMeans_uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC);` 이력 본판: `dc6cc2d` 2025-08-10; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 CalcMeans에 txNewState를 전달한다. |
| CT1-281 | js/main.js 구간 28 교란 누적 침식 전달 | E 코드 결함 후보 (약함) | `ebca435:js/main.js:1317` `const AddDisturbance_BindGroup = create_AddDisturbance_BindGroup(device, AddDisturbance_uniformBuffer, txBottom, txstateUVstar, txBottomInitial, txtemp_AddDisturbance, txBoundaryForcing, txtemp_bottom, txBotChange_Sed);` / `ebca435:transect_version/js/main.js:859` `const AddDisturbance_BindGroup = create_AddDisturbance_BindGroup(device, AddDisturbance_uniformBuffer, txBottom, txstateUVstar, txBottomInitial, txtemp_AddDisturbance, txBoundaryForcing, txtemp_bottom);` 반대 근거·두 경로 대조: 교란과 누적 침식의 결합 절. | 본판만 AddDisturbance에 txBotChange_Sed를 전달한다. 한쪽 지형 누적 보존 결함 수정이다. |
| CT1-282 | js/main.js 구간 29 선형 구조물 uniform과 툴팁 binding | A 판 차이 | `ebca435:js/main.js:1365` `MouseClickChange_view.setFloat32(52, calc_constants.designcomponent_Radius, true);             // f32` / `ebca435:transect_version/js/main.js:907` `MouseClickChange_view.setFloat32(52, calc_constants.designcomponent_Radius, true);             // f32` 이력 본판: `d778fe7` 2026-06-02, `397c575` 2025-09-09; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 선형 구조물 오프셋 64–92를 갱신한다. 본판만 ExtractTimeSeries에 txMeans_Speed를 전달한다. 공백 차이는 물리 값을 바꾸지 않는다. |
| CT1-283 | js/main.js 구간 30 시계열 시각과 중첩 추출 설정 | A 판 차이 | `ebca435:js/main.js:1394` `ExtractTimeSeries_view.setFloat32(24, calc_constants.start_time_shift, true);             // f32, total_time` / `ebca435:transect_version/js/main.js:922` `ExtractTimeSeries_view.setFloat32(24, 0.0, true);             // f32, total_time` 이력 본판: `bb99fee` 2026-07-02, `397c575` 2025-09-09, `c4be488` 2026-07-13; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 시작 시각 이동을 점 시계열 uniform에 반영한다. 본판만 교란 유형과 중첩 경계 추출 레이아웃을 설정한다. transect 판은 시간 0에서 시작한다. |
| CT1-284 | js/main.js 구간 31 render의 침식 입력 의미 | A 판 차이 | `ebca435:js/main.js:1451` `var RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);` / `ebca435:transect_version/js/main.js:962` `var RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);` 이력 본판: `8c2b62b` 2025-08-24; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 erosion_Sed 자리의 리소스에 txBottomInitial을 전달한다. transect 판은 실제 erosion_Sed를 전달한다. 동일 binding의 의미를 두 판에서 혼용하면 안 된다. |
| CT1-285 | js/main.js 구간 32 셰이더 선택과 NLSW 초기화 | E 코드 결함 후보 (강함) | `ebca435:js/main.js:1508` `Render_view.setFloat32(260, calc_constants.arrow_scale, true);          // f32` / `ebca435:transect_version/js/main.js:1019` `Render_view.setFloat32(260, calc_constants.arrow_scale, true);          // f32` 반대 근거·두 경로 대조: NLSW 초기화의 null 셰이더 절. | transect 판은 모든 셰이더 경로에 /transect_version 접두어를 쓴다. 고차 flux는 HLLEM 파일이고 본판은 HLLC 파일이다. transect 판은 NLSW_or_Bous==0에서 Pass3_ShaderCode_Bous를 null로 남긴다. 뒤의 파이프라인 생성은 무조건 실행하므로 이 옵션의 초기화 계약과 모순한다. 본판은 Bous 소스를 먼저 읽어 이 상황을 피한다. 표시 uniform·hardbottom·중첩 추출·구면 선택 차이도 이 구간에 있다. |
| CT1-286 | js/main.js 구간 33 render 파이프라인 미리 생성 | E 코드 결함 후보 (중간) | `ebca435:js/main.js:1641` `const ExtractNestedBoundaryTimeSeries_Pipeline = createComputePipeline(device, ExtractNestedBoundaryTimeSeries_ShaderCode, ExtractNestedBoundaryTimeSeries_BindGroupLayout, allComputePipelines);` / `ebca435:transect_version/js/main.js:1129` `var RenderPipeline = createRenderPipeline(device, vertexShaderCode, fragmentShaderCode, swapChainFormat, RenderBindGroupLayout);` 반대 근거·두 경로 대조: 프레임마다 파이프라인 재생성 절. | 본판은 quad와 vertexgrid 파이프라인을 미리 만든다. transect 판은 최초 quad만 만든 뒤 프레임마다 선택한 파이프라인을 새로 만든다. 본판만 중첩 추출 파이프라인을 만든다. 본판은 2026-02-13 08860f0에서 이 반복 생성을 줄였다. 같은 판의 초기 파이프라인 생성 경로와 프레임 내 재사용 원칙을 함께 근거로 중간 강도의 결함 후보로 둔다. |
| CT1-287 | js/main.js 구간 34 격자 vertex 개수 | E 코드 결함 후보 (중간) | `ebca435:js/main.js:1695` `vertices.push(-1 + 2 * x / (gridWidth - 1), 1 - 2 * y       / (gridHeight - 1));` / `ebca435:transect_version/js/main.js:1166` `let numVertices = 2*gridHeight*gridWidth;` 반대 근거·두 경로 대조: 중복 마지막 strip과 vertex 개수 절. | transect 판은 마지막 strip을 한 번 더 생성한다. numVertices는 2*HEIGHT*WIDTH로 고정한다. 본판은 실제 vertices.length/2를 사용한다. HEIGHT>1에서 transect 실제 vertex 수는 2*WIDTH*HEIGHT+2*HEIGHT-3이다. 고정 draw 수가 생성 개수와 다르다. 해석: 뒤에 더한 중복 strip 일부를 그리는 불필요한 처리다. 원래 마지막 줄 전체가 누락된다고 단정하지 않는다. |
| CT1-288 | js/main.js 구간 35 시뮬레이션과 점 시계열 초기 시각 | A 판 차이 | `ebca435:js/main.js:1719` `let total_time = calc_constants.start_time_shift;          // Initialize time, which might be used for animations or simulations.` / `ebca435:transect_version/js/main.js:1215` `let total_time = 0;          // Initialize time, which might be used for animations or simulations.` 이력 본판: `bb99fee` 2026-07-02, `ebca435` 2026-07-20; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 type5 시작 시각을 total_time에 더한다. 점 시계열은 일반 실행에서 0 기반을 유지하고 type5에서 절대 시각을 쓴다. transect 판은 두 시계를 0으로 둔다. |
| CT1-289 | js/main.js 구간 36 중첩 경계 출력 실행 상태 | A 판 차이 | `ebca435:js/main.js:1775` `async function uploadDrawOverlayCanvas() {` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02, `c4be488` 2026-07-13; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 사각형 표시·다중 상태·리소스 해제·인덱스 제한·별칭 설정 키·표본 수 제한·위치 좌표·uniform·시간별 캡처를 구현한다. 사각형마다 독립 시계를 쓴다. 출력 간격은 dt 이상으로 제한한다. GPU 텍스처 한도를 넘는 사각형은 건너뛴다. 전체 수집이 끝나면 다운로드한다. |
| CT1-290 | js/main.js 구간 37 주기적 GPU 동기화 | A 판 차이 | `ebca435:js/main.js:2219` `var nowFlush = Date.now();` / 추가 줄 없음 이력 본판: `7ae7da4` 2026-02-23; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 600000ms마다 onSubmittedWorkDone을 기다린다. transect 판에는 해당 운영 보정이 없다. |
| CT1-291 | js/main.js 구간 38 HTML 갱신 시 dt와 구면 모드 | A 판 차이 | `ebca435:js/main.js:2284` `runCopyTextures(device, calc_constants, txBottom, txBottomInitial)` / `ebca435:transect_version/js/main.js:1318` `runCopyTextures(device, commandEncoder, calc_constants, txBottom, txBottomInitial)` 이력 본판: `33f7ff6` 2026-02-13, `afc1fe7` 2026-06-19; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 복사 함수의 commandEncoder 인자만 다르다. 본판은 구면 모드·물리 격자간격·계량을 다시 계산한다. transect 판은 Cartesian CFL 식만 다시 계산한다. |
| CT1-292 | js/main.js 구간 39 지구 반지름 역수 갱신 | A 판 차이 | `ebca435:js/main.js:2365` `Pass3_view.setFloat32(148, 1.0 / Math.max(calc_constants.R_earth, 1.0), true);       // f32` / 추가 줄 없음 이력 본판: `afc1fe7` 2026-06-19; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 HTML 변경 뒤 Pass3의 one_over_R을 갱신한다. |
| CT1-293 | js/main.js 구간 40 추적자 초기화 복사 | F 표기 차이 | `ebca435:js/main.js:2383` `runCopyTextures(device, calc_constants, txzeros, txContSource)` / `ebca435:transect_version/js/main.js:1378` `runCopyTextures(device, commandEncoder, calc_constants, txzeros, txContSource)` | commandEncoder 인자 외에는 txzeros→txContSource 복사 조건과 범위가 같다. |
| CT1-294 | js/main.js 구간 41 경계 UI 파랑 재생성 | A 판 차이 | `ebca435:js/main.js:2393` `calc_constants.north_boundary_type = 3;` / `ebca435:transect_version/js/main.js:1388` `calc_constants.north_boundary_type = 3;` 이력 본판: `9093d7f` 2026-06-01; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 UI 변경에 맞춰 파랑 텍스처와 numberOfWaves uniform을 갱신한다. 양쪽은 주기 경계를 쌍으로 맞추는 호스트 코드를 유지한다. transect 셰이더는 주기 경계를 구현하지 않는다. |
| CT1-295 | js/main.js 구간 42 type5 위치·관측점 수 갱신 | A 판 차이 | `ebca435:js/main.js:2411` `BoundaryPass_view.setInt32(176, calc_constants.grid_type, true);              // i32` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 경계 원점과 4변 관측점 수를 다시 uniform에 쓴다. |
| CT1-296 | js/main.js 구간 43 Google overlay 바인드 그룹 인자 | E 코드 결함 후보 (강함) | `ebca435:js/main.js:2437` `RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);` / `ebca435:transect_version/js/main.js:1417` `RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, depostion_Sed, txBotChange_Sed, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs);` 반대 근거·두 경로 대조: overlay 전환 인자 불일치 절. | transect 판의 overlay 전환 호출은 현재 createRenderBindGroup의 인자 목록과 맞지 않는다. sampler와 txTimeSeries_Locations 등이 한 칸씩 이동하고 끝 인자는 undefined가 된다. 본판은 전체 인자 목록으로 고쳤다. |
| CT1-297 | js/main.js 구간 44 위성 overlay 바인드 그룹 인자 | E 코드 결함 후보 (강함) | `ebca435:js/main.js:2450` `RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);` / `ebca435:transect_version/js/main.js:1428` `RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, depostion_Sed, txBotChange_Sed, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs);` 반대 근거·두 경로 대조: overlay 전환 인자 불일치 절. | transect 판의 위성 overlay 전환 호출도 현재 함수 정의와 맞지 않는다. 본판은 txDesignComponents·두 sampler·f16 텍스처까지 전달하도록 고쳤다. |
| CT1-298 | js/main.js 구간 45 범례와 중첩 사각형 재표시 | A 판 차이 | `ebca435:js/main.js:2489` `if (calc_constants.nestedGridOutput_active == 1) {` / `ebca435:transect_version/js/main.js:1465` `update_colorbar(device, offscreenCanvas, ctx, calc_constants, txDraw, logo_left, logo_right) // update colorbar with new climits` 이력 본판: `bb99fee` 2026-07-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 활성 중첩 사각형 유무에 따라 범례·윤곽 업로드를 await한다. transect 판은 기존 update_colorbar를 호출한다. |
| CT1-299 | js/main.js 구간 46 지형 편집 뒤 near-dry 갱신 | E 코드 결함 후보 (중간) | `ebca435:js/main.js:2524` `MouseClickChange_view.setFloat32(56, calc_constants.designcomponent_Friction, true);             // f32` / `ebca435:transect_version/js/main.js:1496` `MouseClickChange_view.setFloat32(56, calc_constants.designcomponent_Friction, true);             // f32` 반대 근거·두 경로 대조: 편집 뒤 near-dry 갱신 절. | transect 판은 mode 1에서만 near-dry를 다시 계산한다. 본판은 모든 모드에서 near-dry를 갱신하고 mode>=1에서 계수를 갱신한다. mode 2의 source 분산 차단이 near-dry를 읽으므로 두 경로가 모순할 수 있다. 선형 구조물 적용은 본판 후속 기능이다. 즉시 submit 호출의 인자 변화는 수치 순서를 보존한다. |
| CT1-300 | js/main.js 구간 47 교란 호출과 중첩 트리거 | A 판 차이 | `ebca435:js/main.js:2598` `runComputeShader(device, AddDisturbance_uniformBuffer, AddDisturbance_uniforms, AddDisturbance_Pipeline, AddDisturbance_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // add impulse` / `ebca435:transect_version/js/main.js:1551` `runComputeShader(device, commandEncoder, AddDisturbance_uniformBuffer, AddDisturbance_uniforms, AddDisturbance_Pipeline, AddDisturbance_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // add impulse` 이력 본판: `33f7ff6` 2026-02-13, `bb99fee` 2026-07-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 즉시 submit 함수를 호출한다. 본판만 중첩 출력 트리거를 처리한다. 단면판은 commandEncoderStack 변수를 두지 않는다. |
| CT1-301 | js/main.js 구간 48 예측 단계 submit 묶음 | A 판 차이 | `ebca435:js/main.js:2624` `total_time = frame_count * calc_constants.dt + calc_constants.start_time_shift;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n` / `ebca435:transect_version/js/main.js:1568` `total_time = frame_count * calc_constants.dt;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n` 이력 본판: `bb99fee` 2026-07-02, `3646fc8` 2026-02-08, `33f7ff6` 2026-02-13; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | Pass0→Pass1→선택 퇴적물 재구성→Pass2→쇄파→COULWAVE A/B 순서는 같다. transect 판은 매 호출을 submit한다. 본판은 encoder로 묶는다. 시간 uniform을 쓰는 위치는 바뀌지만 쇄파는 total_time-dt를 사용한다. 본판만 total_time에 시작 시각을 더한다. |
| CT1-302 | js/main.js 구간 49 예측 적분·경계·PCR·사면 이동 순서 | A 판 차이 | `ebca435:js/main.js:2676` `commandEncoderStack = device.createCommandEncoder();` / `ebca435:transect_version/js/main.js:1607` `runComputeShader(device, commandEncoder, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);` 이력 본판: `3646fc8` 2026-02-08, `984091f` 2026-05-24, `7ae7da4` 2026-02-23, `33f7ff6` 2026-02-13; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | Pass3→gradient 보관→퇴적물→경계→COULWAVE 계수→PCR→분산 모드 재경계 순서는 유지한다. 본판은 계수 교대 바인드 그룹을 전달한다. transect 판은 사면 이동을 시간 제한 없이 호출한다. 본판은 첫 1e5 스텝까지만 호출한다. corrector는 양쪽에서 timeScheme==2로 시작한다. |
| CT1-303 | js/main.js 구간 50 수정 단계와 후처리의 단면판 경로 | C 문서 누락 | `ebca435:js/main.js:2810` `commandEncoderStack = device.createCommandEncoder();` / `ebca435:transect_version/js/main.js:1715` `runComputeShader(device, commandEncoder, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);` | 수정 단계의 계산·경계·PCR 순서는 같다. 통계 카운터 uniform은 transect가 직전에 갱신하고 본판은 encoder 생성 전에 갱신한다. transect의 퇴적물 바닥고 고정은 HTML 안내에 맞는다. 본판만 중첩 경계 캡처·다운로드·리소스 해제를 실행한다. 이력 texture 이동과 통계의 상대 순서는 같다. |
| CT1-304 | js/main.js 구간 51 프레임별 render 파이프라인 생성 | E 코드 결함 후보 (중간) | `ebca435:js/main.js:2990` `Render_view.setInt32(84, calc_constants.CB_show, true);          // i32` / `ebca435:transect_version/js/main.js:1810` `Render_view.setInt32(84, calc_constants.CB_show, true);          // i32` 반대 근거·두 경로 대조: 프레임마다 파이프라인 재생성 절. | transect 판은 매 프레임 quad 또는 vertexgrid 파이프라인을 새로 만든다. 본판은 미리 만든 객체를 선택한다. view 1은 colorbar를 켜고 view 2는 끈다는 조건은 같다. 본판은 2026-02-13 08860f0에서 이 반복 생성을 줄였다. 같은 판의 초기 파이프라인 생성 경로와 프레임 내 재사용 원칙을 함께 근거로 중간 강도의 결함 후보로 둔다. |
| CT1-305 | js/main.js 구간 52 Design 모드 건물 footprint | A 판 차이 | `ebca435:js/main.js:3049` `RenderPass.draw(4);  // Draw the quad` / `ebca435:transect_version/js/main.js:1869` `RenderPass.draw(4);  // Draw the quad` 이력 본판: `590bda8` 2026-06-01; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 JSON box 모델을 위에서 본 footprint로 표시한다. 본판은 범례와 로고 영역을 scissor로 보호한다. transect 판은 quad만 그린다. |
| CT1-306 | js/main.js 구간 53 카메라 투영 범위 | A 판 차이 | `ebca435:js/main.js:3150` `const window_width  = (calc_constants.full_screen && !pseudoFullscreenActive) ? window.innerWidth  : canvas.width;` / `ebca435:transect_version/js/main.js:1880` `const window_width  = calc_constants.full_screen ? window.innerWidth  : canvas.width;` 이력 본판: `24b8f13` 2026-05-24, `afc1fe7` 2026-06-19; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 가상 전체화면 크기와 구면 미터 척도를 반영한다. transect 판은 window 크기와 Cartesian dx·dy를 쓴다. fovY=45도는 같다. |
| CT1-307 | js/main.js 구간 54 카메라 바닥 보간 좌표 | A 판 차이 | `ebca435:js/main.js:3192` `const x = camState.position[0] / explorerCameraDx;` / `ebca435:transect_version/js/main.js:1913` `const x = camState.position[0] / calc_constants.dx;` 이력 본판: `afc1fe7` 2026-06-19; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 구면 미터 격자간격으로 카메라 위치를 인덱스화한다. transect 판은 dx·dy로 나눈다. Cartesian일 때 식은 같다. |
| CT1-308 | js/main.js 구간 55 카메라 좌우 이동 척도 | A 판 차이 | `ebca435:js/main.js:3266` `deltaPanX * explorerSimDim` / `ebca435:transect_version/js/main.js:1985` `deltaPanX * simDim` 이력 본판: `afc1fe7` 2026-06-19; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 explorerSimDim을 사용한다. transect 판은 simDim을 사용한다. Cartesian일 때 두 척도는 같다. |
| CT1-309 | js/main.js 구간 56 카메라 전후 이동 척도 | A 판 차이 | `ebca435:js/main.js:3283` `deltaPanY * explorerSimDim` / `ebca435:transect_version/js/main.js:2000` `deltaPanY * simDim` 이력 본판: `afc1fe7` 2026-06-19; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 지면 잠금 여부와 무관하게 explorerSimDim을 사용한다. transect 판은 simDim을 사용한다. |
| CT1-310 | js/main.js 구간 57 카메라 model 행렬 | A 판 차이 | `ebca435:js/main.js:3337` `if (calc_constants.grid_type == 2) {` / `ebca435:transect_version/js/main.js:2037` `const T_unskew = mat4.fromScaling(mat4.create(), [` 이력 본판: `afc1fe7` 2026-06-19, `f183cc2` 2026-02-01; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 구면에서 x·y 미터 변환을 적용한다. Cartesian 경로와 transect 판은 재척도*역척도인 항등 행렬이다. 제거된 카메라 로그는 본판에서도 주석이다. |
| CT1-311 | js/main.js 구간 58 점 시계열 초기화와 epoch | E 코드 결함 후보 (중간) | `ebca435:js/main.js:3472` `if (calc_constants.chartDataUpdate == 0) {` / `ebca435:transect_version/js/main.js:2152` `if(calc_constants.updateTimeSeriesTx == 1 \|\| calc_constants.chartDataUpdate == 1) {  // update the time series locations texture, and reset plot` 반대 근거·두 경로 대조: 비동기 시계열 초기화 절. | 본판은 UI 갱신을 한 번만 처리하고 동기적으로 배열을 초기화한다. transect 판은 chartDataUpdate가 유지되는 동안 매 프레임 초기화를 요청한다. 본판은 epoch로 이전 readback을 버린다. 시간창 경계는 본판 >=이고 transect >다. 일반 실행은 양쪽 0 기반이고 본판 type5만 절대 시각이다. |
| CT1-312 | js/main.js 구간 59 외부 제어 시간 진단 | A 판 차이 | `ebca435:js/main.js:3539` `calc_constants.elapsedTime = (now - startTime) / 1000.0;` / `ebca435:transect_version/js/main.js:2192` `calc_constants.elapsedTime = (now - startTime) / 1000;` 이력 본판: `a86f73a` 2026-02-20, `0ee5174` 2026-06-18; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 agent_total_time·agent_total_time_since_http_update·실시간 배율을 노출한다. 1000과 1000.0의 밀리초 환산은 JS에서 같다. |
| CT1-313 | js/main.js 구간 60 개별 표면 출력 버퍼 | A 판 차이 | `ebca435:js/main.js:3620` `downloadTextureData(device, txNewState, 1, filename, readbackBuffer);  // last number is the channel 1 = .r, 2 = .g, etc.` / `ebca435:transect_version/js/main.js:2268` `downloadTextureData(device, txNewState, 1, filename);  // last number is the channel 1 = .r, 2 = .g, etc.` 이력 본판: `09cfd76` 2026-02-15; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 13개 표면 선택의 텍스처·채널·파일명은 같다. 본판만 공용 readbackBuffer를 전달한다. |
| CT1-314 | js/main.js 구간 61 묶음 표면 출력 | A 판 차이 | `ebca435:js/main.js:3723` `{ tx: txBotChange_Sed,ch: 3, filename: 'current_SedTransDepthChange.bin'},` / `ebca435:transect_version/js/main.js:2374` `await downloadTextureData(device, tx, ch, filename);` 이력 본판: `fa47b72` 2025-06-06, `09cfd76` 2026-02-15; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 current_SedTransDepthChange.bin을 중심 b 채널에서 출력한다. 공용 버퍼 인자 차이 외에 나머지 파일은 같다. |
| CT1-315 | js/main.js 구간 62 주기적 표면 출력 호출 | A 판 차이 | `ebca435:js/main.js:3794` `await writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities,readbackBuffer);` / `ebca435:transect_version/js/main.js:2441` `await writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities);` 이력 본판: `09cfd76` 2026-02-15; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 공용 readbackBuffer를 전달한다. 시간·프레임 번호·6개 텍스처 인자는 같다. |
| CT1-316 | js/main.js 구간 63 포인터의 표시 영역 좌표 | E 코드 결함 후보 (중간) | `ebca435:js/main.js:3907` `const activeExplorerTouches = new Map();` / `ebca435:transect_version/js/main.js:2556` `var rect = canvas.getBoundingClientRect();` 반대 근거·두 경로 대조: 포인터와 표시 영역 절. | 본판은 object-fit 여백을 제외한 canvas 내용 영역을 계산한다. transect 판은 외곽 사각형 전체를 쓴다. 여백이 있으면 표시한 격자와 편집 위치가 어긋난다. 외부 제어 모드 제한도 본판에만 있다. |
| CT1-317 | js/main.js 구간 64 좌표 변환·선형 구조물·터치 helper | A 판 차이 | `ebca435:js/main.js:3931` `function getCanvasContentRect() {` / 추가 줄 없음 이력 본판: `0ee5174` 2026-06-18, `ff0d046` 2026-07-07, `d778fe7` 2026-06-02, `24b8f13` 2026-05-24; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 object-fit 위치·표시 영역 검사·world 좌표·구면 상대/절대 좌표·선형 끝점 상태·양의 폭/경사 검사·두 손가락 중점과 거리를 구현한다. transect 판은 해당 함수가 없다. |
| CT1-318 | js/main.js 구간 65 pointerdown 입력 경로 | A 판 차이 | `ebca435:js/main.js:4232` `if (event.pointerType === 'touch' && calc_constants.viewType == 2) {` / `ebca435:transect_version/js/main.js:2578` `if (event.button === 0 && calc_constants.viewType == 1) { // Left mouse button, Design mode` 이력 본판: `24b8f13` 2026-05-24, `d778fe7` 2026-06-02, `0ee5174` 2026-06-18, `ff0d046` 2026-07-07; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 한 손가락 회전·두 손가락 이동·Ctrl 좌클릭 회전·선형 끝점 우클릭·측정점 좌표 표시 동기화를 추가한다. transect 판은 기존 마우스 버튼 처리만 쓴다. |
| CT1-319 | js/main.js 구간 66 pointermove 터치 동작 | A 판 차이 | `ebca435:js/main.js:4295` `if (event.pointerType === 'touch' && calc_constants.viewType == 2 && activeExplorerTouches.has(event.pointerId)) {` / 추가 줄 없음 이력 본판: `24b8f13` 2026-05-24, `62b1458` 2026-05-24; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 터치 한 손가락 회전과 두 손가락 pan·pinch를 처리한다. 수치 계산식은 바뀌지 않는다. |
| CT1-320 | js/main.js 구간 67 pointerup 정리 | A 판 차이 | `ebca435:js/main.js:4361` `if (event.pointerType === 'touch' && calc_constants.viewType == 2) {` / `ebca435:transect_version/js/main.js:2635` `if (event.button === 0) { // Left mouse button` 이력 본판: `24b8f13` 2026-05-24; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 터치 목록과 Ctrl 좌클릭 회전 상태까지 정리한다. transect 판은 좌·우 마우스 상태만 정리한다. |
| CT1-321 | js/main.js 구간 68 pointercancel 터치 목록 | A 판 차이 | `ebca435:js/main.js:4403` `activeExplorerTouches.delete(event.pointerId);` / 추가 줄 없음 이력 본판: `24b8f13` 2026-05-24; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 activeExplorerTouches에서 취소한 포인터를 제거한다. |
| CT1-322 | js/main.js 구간 69 키보드 입력 중 카메라 간섭 | E 코드 결함 후보 (중간) | `ebca435:js/main.js:4420` `const eventTargetTag = event.target && event.target.tagName ? event.target.tagName.toLowerCase() : '';` / `ebca435:transect_version/js/main.js:2667` `calc_constants.click_update = 2;` 반대 근거·두 경로 대조: 폼 입력과 카메라 이동 절. | 본판은 폼 편집과 Design 모드에서 Explorer 이동키를 차단한다. transect 판은 입력 대상과 viewType을 검사하지 않는다. event.key 대신 code를 쓰는 변경과 P/Pause 정지 기능 추가도 본판에 있다. |
| CT1-323 | js/main.js 구간 70 툴팁의 표시 영역 좌표 | E 코드 결함 후보 (중간) | `ebca435:js/main.js:4525` `const bounds = getCanvasContentRect(); // Visible rendered canvas content, excluding object-fit letterboxing.` / `ebca435:transect_version/js/main.js:2740` `const bounds = canvas.getBoundingClientRect(); // Get the bounding rectangle of the canvas` 반대 근거·두 경로 대조: 포인터와 표시 영역 절. | transect 판은 canvas 외곽 사각형을 정규화한다. 본판은 object-fit 여백을 제외한다. 격자 좌표와 표시 위치의 불일치를 고친 한쪽 수정이다. |
| CT1-324 | js/main.js 구간 71 툴팁 단위와 교란 표시 | A 판 차이 | `ebca435:js/main.js:4563` `if (calc_constants.viewType == 1){` / `ebca435:transect_version/js/main.js:2776` `if (calc_constants.viewType == 1){` 이력 본판: `afc1fe7` 2026-06-19, `397c575` 2025-09-09; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 구면 경위도 소수 6자리와 교란 시 최대수면을 표시한다. transect 판은 X/Y m 소수 2자리와 유의파고를 표시한다. 하천의 속력 표시는 유지한다. |
| CT1-325 | js/main.js 구간 72 UI 동기화 후처리 | A 판 차이 | `ebca435:js/main.js:4666` `updateLinearStructureLocationsDisplay();` / `ebca435:transect_version/js/main.js:2862` `}` 이력 본판: `d778fe7` 2026-06-02, `ff0d046` 2026-07-07; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 선형 끝점 요약과 격자 유형별 측정점 좌표 입력을 동기화한다. |
| CT1-326 | js/main.js 구간 73 선형 구조물 수치 버튼 | A 판 차이 | `ebca435:js/main.js:4712` `{ id: 'designcomponent_CrestElev-button', input: 'designcomponent_CrestElev-input', property: 'designcomponent_CrestElev' },` / 추가 줄 없음 이력 본판: `d778fe7` 2026-06-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 천단고·폭·경사·양끝 좌표를 표준 update 버튼 목록에 넣는다. |
| CT1-327 | js/main.js 구간 74 중첩 출력 수치 버튼 | A 판 차이 | `ebca435:js/main.js:4730` `{ id: 'nestedGridOutput_i0-button', input: 'nestedGridOutput_i0-input', property: 'nestedGridOutput_i0' },` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 사각형 인덱스·출력 기간·간격·eta 임계값을 update 버튼 목록에 넣는다. |
| CT1-328 | js/main.js 구간 75 선형 끝점 선택 목록 | A 판 차이 | `ebca435:js/main.js:4770` `{ input: 'designcomponent_CurrentEndPoint-select', property: 'designcomponent_CurrentEndPoint' },` / 추가 줄 없음 이력 본판: `d778fe7` 2026-06-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 시작점·끝점 선택을 calc_constants에 연결한다. |
| CT1-329 | js/main.js 구간 76 외부 제어 설치 | A 판 차이 | `ebca435:js/main.js:4785` `installCelerisAgentControls({` / 추가 줄 없음 이력 본판: `0ee5174` 2026-06-18; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 installCelerisAgentControls에 수치 상태 조회·예제 실행·view 선택·전체화면 정리·설계 모드·선형 구조물 요청 callback을 전달한다. CelerisAgent 내부는 판독하지 않는다. |
| CT1-330 | js/main.js 구간 77 전체화면 크기 | A 판 차이 | `ebca435:js/main.js:4858` `var pseudoFullscreenSavedStyle = null;` / `ebca435:transect_version/js/main.js:2994` `if (document.fullscreenElement) {` 이력 본판: `24b8f13` 2026-05-24; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 가상 전체화면과 visualViewport를 처리한다. transect 판은 실제 document.fullscreenElement만 처리한다. |
| CT1-331 | js/main.js 구간 78 가상 전체화면 대체 경로 | A 판 차이 | `ebca435:js/main.js:4924` `function enterPseudoFullscreen() {` / `ebca435:transect_version/js/main.js:3046` `if (!document.fullscreenElement) {` 이력 본판: `24b8f13` 2026-05-24; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 실제 전체화면 미지원·거절 때 CSS 고정 화면을 쓴다. 종료 때 원래 inline style과 스크롤 상태를 복구한다. transect 판은 requestFullscreen 오류를 로그로만 남긴다. |
| CT1-332 | js/main.js 구간 79 resize 이벤트 제한 | A 판 차이 | `ebca435:js/main.js:5050` `var resizeCanvasTimer = null;` / `ebca435:transect_version/js/main.js:3065` `window.addEventListener('resize', resizeCanvas);` 이력 본판: `24b8f13` 2026-05-24; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 80ms debounce와 visualViewport resize·scroll을 사용한다. transect 판은 window resize마다 즉시 갱신한다. |
| CT1-333 | js/main.js 구간 80 측정점·선형 끝점·view 선택 | A 판 차이 | `ebca435:js/main.js:5128` `calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].xts = timeSeriesDisplayToOffsetX(calc_constants.changeXTimeSeries);` / `ebca435:transect_version/js/main.js:3132` `calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].xts = calc_constants.changeXTimeSeries;` 이력 본판: `ff0d046` 2026-07-07, `d778fe7` 2026-06-02, `24b8f13` 2026-05-24; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 구면 표시 좌표를 상대좌표로 바꾼다. 본판만 선형 끝점 버튼을 연결한다. 본판은 view 선택 뒤 blur하여 문서 키보드 동작을 복구한다. |
| CT1-334 | js/main.js 구간 81 중첩 출력 시작 버튼 | A 판 차이 | `ebca435:js/main.js:5243` `document.getElementById('startNestedGridOutput-button').addEventListener('click', function () {` / 추가 줄 없음 이력 본판: `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 nestedGridOutput_trigger=1을 설정한다. |
| CT1-335 | js/main.js 구간 82 시작 시 선택 파일 | A 판 차이 | `ebca435:js/main.js:5276` `var etaInitialConditionFile = document.getElementById('etaInitialConditionFile').files[0];` / 추가 줄 없음 이력 본판: `32be94a` 2025-10-16, `b8b50c3` 2025-06-08, `bb99fee` 2026-07-02; transect: 분기 전 코드. 최초 transect 추가: `22e1983` 2025-06-06. | 본판만 초기 수면·hardbottom·4변 시계열 파일을 읽는다. transect 판은 config·bathy·waves·friction·overlay·model 파일을 읽는다. |
| CT1-336 | js/main.js 구간 83 기본 파랑 파일 경로와 마찰 누락 | E 코드 결함 후보 (강함) | `ebca435:js/main.js:5314` `startSimulationWithWave(configContent, bathymetryContent, defaultWaveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile);` / `ebca435:transect_version/js/main.js:3274` `startSimulationWithWave(configContent, bathymetryContent, defaultWaveContent, OverlayFile, modelFile);` 반대 근거·두 경로 대조: 기본 no_waves와 friction 인자 절. | transect 판은 파랑 파일 미지정 시 /no_waves.txt를 fetch한다. 단면 reader는 3*HEIGHT행을 기대한다. 일반 no_waves.txt 형식은 그 계약과 다르다. 이 호출은 이미 읽은 frictionFile도 전달하지 않는다. 업로드 파랑 경로와 자기 함수 인자 계약이 모순한다. |
| CT1-337 | js/main.js 구간 84 업로드 파랑 시작 인자 | A 판 차이 | `ebca435:js/main.js:5324` `startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile);` / `ebca435:transect_version/js/main.js:3282` `startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile);` 이력 본판: `bb99fee` 2026-07-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 실제 파랑 업로드 경로에서 frictionFile을 전달한다. 본판은 초기 수면·hardbottom·4변 시계열 파일도 전달한다. |
| CT1-338 | js/main.js 구간 85 시작 함수 인자 목록 | A 판 차이 | `ebca435:js/main.js:5338` `function startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile) {` / `ebca435:transect_version/js/main.js:3294` `function startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile) {` 이력 본판: `bb99fee` 2026-07-02; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판의 시작 함수는 6인자다. 본판은 추가 입력 파일을 포함한 13인자다. |
| CT1-339 | js/main.js 구간 86 초기화 호출과 자동 시작 | A 판 차이 | `ebca435:js/main.js:5349` `initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile).catch(error => {` / `ebca435:transect_version/js/main.js:3303` `initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile).catch(error => {` 이력 본판: `bb99fee` 2026-07-02, `f6fd78b` 2026-06-04; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | transect 판은 6인자를 초기화에 전달한다. 본판만 URL 케이스 자동 시작 뒤 5000ms 후 UI를 갱신한다. |
| CT1-340 | js/main.js 구간 87 시계열 수 0일 때 chart 갱신 | A 판 차이 | `ebca435:js/main.js:5459` `} else if (calc_constants.NumberOfTimeSeries > 0) {` / `ebca435:transect_version/js/main.js:3407` `} else {` 이력 본판: `dee0e14` 2026-02-04; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 NumberOfTimeSeries>0일 때만 기존 dataset을 갱신한다. transect 판은 무조건 else로 들어간다. 내부 timeSeriesData[index] 검사 때문에 이 차이만으로 잘못된 접근을 확정하지 않는다. 이 guard 변경은 ebca435의 epoch 수정과 구분한다. |
| CT1-341 | js/main.js 구간 88 chart 시간축 | A 판 차이 | `ebca435:js/main.js:5473` `timeseriesChart.options.scales.x.min = calc_constants.timeSeriesChartStartTime;` / `ebca435:transect_version/js/main.js:3418` `timeseriesChart.options.scales.x.max = calc_constants.maxdurationTimeSeries;` 이력 본판: `ebca435` 2026-07-20; transect: `22e1983` 2025-06-06. 최초 transect 추가: `22e1983` 2025-06-06. | 본판은 시작 시각부터 시작 시각+기간까지 표시한다. transect 판은 최대값만 maxdurationTimeSeries로 둔다. 일반 0기반 실행에서는 같은 창이다. |
| CT1-342 | js/main.js 구간 89 chart update await | F 표기 차이 | `ebca435:js/main.js:5484` `timeseriesChart.update();` / `ebca435:transect_version/js/main.js:3427` `await timeseriesChart.update();` | transect 판은 timeseriesChart.update()를 await한다. 동기 update의 결과를 기다리는 문법 차이는 기록 자료 값을 바꾸지 않는다. 마지막 빈 줄도 다르다. |
| CT1-343 | js/Handler_ExtractNestedBoundaryTimeSeries.js 전용 파일 | A 판 차이 | `ebca435:js/Handler_ExtractNestedBoundaryTimeSeries.js:3` `// Added by Codex: Start nested-grid boundary time-series extraction handler.` 현재 이름 경로 최초 추가: bb99fee 2026-07-02 Added grid nesting. | 중첩 경계 추출의 uniform·상태·4변 출력·바닥고 바인딩을 만든다. main.js가 파이프라인을 생성하므로 본판에서 호출한다. |
| CT1-344 | js/Wave_Generator.js 전용 파일 | A 판 차이 | `ebca435:js/Wave_Generator.js:44` `export function buildSineWaveData(calc_constants) {` 현재 이름 경로 최초 추가: 9093d7f 2026-06-01 added ability to change wave conditions through the UI - on the Modify Boundary Conditions Panel. | Sine와 TMA 파 성분을 생성한다. H는 0.5배 진폭으로 바꾼다. TMA는 주파수 100개·방향 간격 5도·방향 반폭 20도·gamma 3.3·spread 50·절단비 0.01을 쓴다. 에너지는 4.004 계수로 입력 파고에 맞춘다. 횡방향 주기 경계일 때 방향을 경계 파수에 맞춘다. 임의 위상은 [0,2π)다. 4096 성분 용량과 계산 결과 캐시를 제공한다. |
| CT1-345 | js/agent_controls.js 전용 파일 | A 판 차이 | `ebca435:js/agent_controls.js:820` `window.CelerisAgentControls = {` 현재 이름 경로 최초 추가: 0ee5174 2026-06-18 CelerisAgent initial commit. | 브라우저의 수치 상태·표시·경계·퇴적물·측정점·설계·예제·전체화면 제어 API를 노출한다. applyCommand/applyCommands/getState와 postMessage 입출력을 제공한다. CelerisAgent 폴더의 내부 구현은 범위 밖이다. |
| CT1-346 | shaders/ExtractNestedBoundaryTimeSeries.wgsl 전용 파일 | A 판 차이 | `ebca435:shaders/ExtractNestedBoundaryTimeSeries.wgsl:23` `fn LoadState(i: i32, j: i32) -> vec4<f32> {` 현재 이름 경로 최초 추가: bb99fee 2026-07-02 Added grid nesting. | 직사각형 4변의 eta/hu/hv를 관측점×표본시각 텍스처로 쓴다. workgroup은 16×1이다. 수심<=0이면 0.0을 쓴다. 자료는 child 경계 type 5로 재입력한다. |
| CT1-347 | shaders/Pass2_HighOrder.wgsl 전용 파일 | C 문서 누락 | `ebca435:transect_version/shaders/Pass2_HighOrder.wgsl:191` `xflux = HLLEM_Flux(aplus, aminus, Fp_x, Fm_x, state_plus_x, state_minus_x, DU_flag);` | transect 고차 모드의 활성 x HLLEM flux다. near-dry에서 DU.x를 0으로 만든다. y flux와 횡운동량을 생략한다. 퇴적물 4개 채널의 x flux는 NumericalFlux로 쓴다. phix=1.0이다. 본판은 같은 이름 파일을 2025-11-07에 HLLC/HLLEM 이름으로 분리했다. |
| CT1-348 | shaders/Pass2_HighOrder_HLLC.wgsl 전용 파일 | A 판 차이 | `ebca435:shaders/Pass2_HighOrder_HLLC.wgsl:71` `fn HLLC_Flux(` 현재 이름 경로 최초 추가: 19b63cf 2025-11-07 convert Pass2 High-order to HLLC. | 본판 고차 모드의 활성 HLLC 이름 파일이다. Roe 평균·star 상태·HLL 혼합을 계산한다. x·y 두 flux를 저장한다. 퇴적물 배경·쇄파 확산 항도 받는다. main.js:1548이 이 파일을 fetch한다. |
| CT1-349 | shaders/Pass2_HighOrder_HLLEM.wgsl 전용 파일 | A 판 차이 | `ebca435:shaders/Pass2_HighOrder_HLLEM.wgsl:76` `/ denom;` 현재 이름 경로 최초 추가: 19b63cf 2025-11-07 convert Pass2 High-order to HLLC. | 본판에 보존한 HLLEM flux 대안이다. 현재 main.js에는 이 경로를 fetch하는 줄이 없다. transect 고차 파일은 이 계열을 1D로 줄인 것이다. |
| CT1-350 | shaders/Pass3_NLSW_Spherical.wgsl 전용 파일 | A 판 차이 | `ebca435:shaders/Pass3_NLSW_Spherical.wgsl:217` `let spherical_flux_divergence = (` 현재 이름 경로 최초 추가: afc1fe7 2026-06-19 Added Spherical NLSW Solver, Japan 2011 example. | 본판의 구면 NLSW source와 시간적분이다. 경위도 도를 radian 차분으로 바꾼다. 위도 cos 면가중 flux·압력·곡률·Coriolis를 더한다. mode와 계량 바인딩은 main.js의 grid_type==2 분기가 선택한다. |
| CT1-351 | shaders/SedTrans_Pass3_old.wgsl 전용 파일 | A 판 차이 | `ebca435:shaders/SedTrans_Pass3_old.wgsl:154` `let source_term = erosion - deposition;` 현재 이름 경로 최초 추가: a98bcc4 2025-06-09 sed trans updates. | 본판의 구판 퇴적물 적분이다. 면농도 평균·면속도·hardbottom·픽업·침강을 사용한다. 현재 main.js가 fetch하지 않는다. 활성 SedTrans_Pass3와 같은 판으로 섞어 설명하면 안 된다. |
| CT1-352 | shaders/SedTrans_Pass3_wBedUpdate.wgsl 전용 파일 | E 코드 결함 후보 (강함) | `ebca435:shaders/SedTrans_Pass3_wBedUpdate.wgsl:235` `newBed.x = Bed_state_here.x + globals.dt * d_by_dt_Bed;` 반대 근거·두 경로 대조: 비활성 통합 퇴적물 셰이더 절. | 부유사와 bedload 지형변화를 한 패스에서 함께 시간적분하려는 실험본이다. 전역 oldGradients_Sed·oldOldGradients_Sed·predictedGradients_Sed를 각각 두 번 선언한다. 선언하지 않은 txBedState_Sed·txOldBedGradients_Sed·txOldOldBedGradients_Sed를 읽는다. .x를 취해 f32가 된 Bed_state_here에 다시 .x를 쓴다. 현재 실행 경로에서 호출되지 않음. main.js의 fetch 목록은 활성 SedTrans_Pass3와 SedTrans_UpdateBottom만 선택한다. 정적 오류 근거 강함. |
| CT1-353 | shaders/SedTrans_UpdateBottom_testing.wgsl 전용 파일 | A 판 차이 | `ebca435:shaders/SedTrans_UpdateBottom_testing.wgsl:77` `let B_here = B_initial; // + dB_cumulative;` 현재 이름 경로 최초 추가: 4353b85 2025-06-09 Sed bugs / corrections. | 지형변화의 시간 적산과 주기적 갱신을 시험한 본판 파일이다. 현재 코드는 B_initial을 그대로 출력한다. 지형 되먹임과 최근 누적량 갱신은 주석이다. 현재 main.js가 fetch하지 않는다. |
| CT1-354 | shaders/fragment_testing.wgsl 전용 파일 | A 판 차이 | `ebca435:shaders/fragment_testing.wgsl:864` `out.color = vec4<f32>(color_rgb, 1.0); // Normal shader output` 현재 이름 경로 최초 추가: f183cc2 2026-02-01 Added ability for user to specify initial 3D camera position. | 색상·수면·파고·퇴적물·설계·화살표·측정점·범례를 합성하는 본판의 보존 표시 실험본이다. 현재 main.js는 fragment.wgsl을 fetch한다. 이 실험본은 현재 실행 경로에서 호출되지 않는다. |
| CT1-355 | 분석 범위와 파일 수 | A 판 차이 | `models/Celeris/README.md:5` ``> ✅ **현재 상태(2026-06-15 전수조사 완료)**: Celeris-WebGPU 소스(`raw/source_code/Celeris-WebGPU/`, 35 JS + 42 WGSL) clone + **source-analysis 9 노트 + manual-notes 1 노트** 작성(모두 `file:line` 인용 verified). web-refs 1 + 정체카드도 verified.`` | 기존 완료 표시는 본판의 해당 날짜 조사로 한정한다. 이번 대조의 78개 경로와 본판 66개 공통·11개 전용, transect 1개 전용이라는 집계를 별도 표로 적는다. 분류 E 행 수를 독립 결함 수로 쓰지 않는다. |
| CT1-356 | 고차 flux의 판별 | C 문서 누락 | `models/Celeris/source-analysis/celeris-source-map.md:41` ``- **Riemann 수치플럭스**: `Pass2.wgsl:34-40` `NumericalFlux()` = HLL 형태 `(a⁺F⁻−a⁻F⁺+a⁺a⁻ΔU)/(a⁺−a⁻)`. High-order 경로는 HLLC를 선택(`main.js:1548`).`` | 본판 Accuracy_mode==1은 Pass2_HighOrder_HLLC를 선택한다. transect 판은 Pass2_HighOrder의 HLLEM 함수를 선택한다. transect 파일은 별도 source map으로 연결한다. |
| CT1-357 | 실행 그래프 범위 | C 문서 누락 | `models/Celeris/source-analysis/celeris-pipeline-graph.md:96` ``\| `Accuracy_mode` \| 1 \| Pass1 → `Pass1_HighOrder.wgsl` (4th-order MUSCL-TVD), Pass2 → `Pass2_HighOrder_HLLC.wgsl` \| `js/main.js:1539-1551` \|`` | 이 표는 본판 경로다. transect 판은 고차 flux에 HLLEM을 사용한다. transect 판은 각 계산·복사를 즉시 submit한다. transect 판은 y PCR을 실행하지 않는다. |
| CT1-358 | Psi2x 적용 범위 | E 코드 결함 후보 (강함) | `models/Celeris/source-analysis/celeris-boussinesq-solver.md:94` ``이 Psi 항이 source_term의 운동량 성분에 더해져(`:392`) **명시(explicit) RHS**를 만든다. 이 RHS가 `current_stateUVstar`로 출력(`:429`)되고, 이것이 **음해 tridiagonal solve의 우변 b**가 된다.`` 반대 근거·두 경로 대조: Boussinesq Psi2x 누락 절. | 본판은 Psi1x+Psi2x를 x 운동량 source에 더한다. transect 판은 Psi2x를 계산하지만 source에서 빼먹는다. 지형 경사와 수면 곡률이 모두 0이 아닌 조건에서 정적 결함 후보가 된다. |
| CT1-359 | near-dry 이웃 수 | C 문서 누락 | `models/Celeris/source-analysis/celeris-fv-reconstruction.md:37` ``**왜 분리하나**: wet/dry 판정을 무거운 재구성·flux 로직 바깥으로 빼서, Pass2가 `minH = min(4 이웃 수심)` 한 번으로 near-dry 분기를 결정하게 한다 (`Pass2.wgsl:105`, `Pass2_HighOrder_HLLC.wgsl:184`). 주석 라인(`// min(h_here, h_north)`, `Pass0.wgsl:52-55`)을 보면 원래 `h_here`와의 min을 의도했으나 현재는 이웃값만 저장한다 — 이 차이는 코드상 그대로다.`` | 본판은 네 이웃을 쓰고 transect 판은 동·서 두 이웃만 쓴다. transect의 h_vec.x와 h_vec.z는 0.0이다. 따라서 본판의 네 성분 최소값 식을 transect에 그대로 적용하지 않는다. |
| CT1-360 | 활성 HLLEM의 판 구분 | C 문서 누락 | `models/Celeris/source-analysis/celeris-fv-reconstruction.md:162` ``**활성 여부** (`ARCHITECTURE.md:69-72`): `Accuracy_mode==1`(고차)에서 `main.js`는 `Pass2_HighOrder_HLLC.wgsl`만 fetch (`js/main.js:1547-1548`). **HLLEM은 소스에 존재하나 현재 main.js 경로에서 선택되지 않음**(present-but-not-default).`` | HLLEM 비활성이라는 문장은 본판 main.js에 한정한다. transect main.js는 Accuracy_mode==1에서 Pass2_HighOrder의 HLLEM 함수를 활성화한다. |
| CT1-361 | 쇄파 점성 상한 | C 문서 누락 | `models/Celeris/source-analysis/celeris-breaking-boundary.md:66` ```B·δ_b·h·(∂η/∂t)` 형태(δ_b = `delta_breaking`)에 수치 안정 상한 `dx·dy/dt`을 건다. 이는 FUNWAVE eddy-viscosity breaker의 ν ∝ δ²·h·(∂η/∂t) 구조와 동형(δ_b가 길이 스케일 역할).`` | 본판의 점성 상한은 dx*dy/dt다. transect 판의 점성 상한은 dx*dx/dt다. 두 값은 dx==dy일 때 같다. transect 판은 x 방향 쇄파 나이와 응력만 전달한다. |
| CT1-362 | 면속도 평균 | E 코드 결함 후보 (강함) | `models/Celeris/source-analysis/celeris-coulwave.md:38` ``- `txModelVelocities = (u, v, eta, H)` — 셀평균 속도. u_here/v_here는 face velocity 4성분 평균 `(u4.x+y+z+w)/4` (`Pass3A_COULWAVE.wgsl:34-35`). flux에서 직접 뽑은 속도는 주석으로 "are not better"라 폐기됨 (`:41-42`).`` 반대 근거·두 경로 대조: COULWAVE u 평균 절. | 네 면 평균은 본판에서 사용한다. transect Pass1은 북·남 면속도를 0으로 쓰므로 동일한 분모 4는 일정 x 유속을 절반으로 만든다. transect CalcMeans의 두 면 평균과 이 차이를 함께 경고한다. |
| CT1-363 | 표준 flux의 활성 확산 | B 문서 오기 | `models/Celeris/source-analysis/celeris-sediment.md:104` ``수평 난류확산(`sedTurbDispersion` 배경 + `sedBreakingDispersionCoef`×breaking eddy viscosity) 코드는 `SedTrans_Pass3.wgsl:102-119`에 **전부 주석처리**되어 있음. 즉 현재 활성 빌드는 **이류 + 픽업/침강만**, 명시적 확산 없음. config 키(`sedTurbDispersion=0.01`, `sedBreakingDispersionCoef=0.1`, `constants_load_calc.js:112-113`)는 uniform으로 전달되나 셰이더에서 미사용.`` | 본판 SedTrans_Pass3 안의 확산 대안은 주석이다. 그러나 표준 Pass2는 class 1 flux에 -k*h*grad(C)를 실제로 넣는다. 고차 HLLC/HLLEM 경로는 별도 식을 쓰므로 Accuracy_mode에 따라 확산 구현을 나눠 적는다. transect SedTrans_Pass3는 Dxx=Dxy=Dyy=1.0의 확산을 source에서 계산한다. |
| CT1-364 | 수리 지형 되먹임의 판 차이 | C 문서 누락 | `models/Celeris/source-analysis/celeris-sediment.md:108` ```SedTrans_UpdateBottom.wgsl`은 침식−침강 차를 공극률로 보정한 **Exner형 질량보존**으로 바닥고를 갱신:`` | 본판 UpdateBottom은 바닥고를 갱신한다. transect UpdateBottom은 B_here=B_here로 수리 바닥고를 고정하고 진단 누적량만 적산한다. 이 동작은 transect HTML의 no feedback 안내와 일치한다. |
| CT1-365 | 비활성 통합본의 정적 오류 | E 코드 결함 후보 (강함) | `models/Celeris/source-analysis/celeris-sediment.md:140` ``- `SedTrans_Pass3_wBedUpdate.wgsl` — fetch 없음. Pass3 안에서 bed update까지 합친 통합 실험본(현재는 UpdateBottom으로 분리). **비활성**.`` 반대 근거·두 경로 대조: 비활성 통합 퇴적물 셰이더 절. | SedTrans_Pass3_wBedUpdate는 현재 실행 경로에서 호출되지 않는다. 이 파일에는 중복 전역 선언과 미정의 바닥 이력 텍스처 참조가 있다. 비활성 실험본을 활성 모델 근거로 인용하지 않는다. |
| CT1-366 | 시계열 초기화와 버퍼 수명 | E 코드 결함 후보 (중간) | `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:238` ``- readback: `readToolTipTextureData`가 1D 텍스처를 256B/행 버퍼로 `copyTextureToBuffer` → `mapAsync(READ)` → `timeSeriesData[i].{time,eta,P,Q}`에 push (`js/Time_Series.js:60-128`). `downloadTimeSeriesData`가 위치·시계열을 텍스트로 내보냄 (라인 128-171). 차트는 1초 간격 갱신 (`js/main.js:5488`).`` 반대 근거·두 경로 대조: 비동기 시계열 초기화 절. | 점 readback의 단일 행 복사 규약은 유지한다. 본판 ebca435는 epoch 검사로 오래된 readback을 버린다. transect 판은 해당 수정이 없다. 초기화 순서 결함과 type5의 절대 시각 지원 차이를 분리한다. |
| CT1-367 | f16 레이어 수 | C 문서 누락 | `models/Celeris/source-analysis/celeris-render.md:22` ``매 렌더 직전 1회 compute 패스. full-precision `rgba32float` 시뮬 텍스처 여러 장을 자주 샘플되는 변수만 골라 **단일 `rgba16float` 2D-array 텍스처**(`txRenderVarsf16`, 3 layer)로 packing. 목적: fragment/vertex3D가 적은 수의 텍스처만, 또 절반 대역폭(f16)으로 sample하게 해 렌더 압력 감소 (`docs/architecture/DATA_AND_TEXTURES.md:97-103`).`` | 본판 txRenderVarsf16은 세 레이어다. transect 판은 두 레이어다. transect 판은 가용 퇴적층 깊이 레이어를 만들지 않는다. 건조 eta와 foam의 표시 보정도 본판에만 있다. |
| CT1-368 | vertex3D 고도 입력 | B 문서 오기 | `models/Celeris/source-analysis/celeris-render.md:34` ``fragment·vertex3D는 이후 `txRenderVarsf16`를 layer index로 sample (예: 유속은 layer 1, 세굴심도는 layer 2).`` | 본판 vertex3D는 etaTexture를 textureLoad하여 full precision 수면을 읽는다. transect vertex3D는 txRenderVarsf16의 레이어 0을 textureSampleLevel로 읽는다. 두 판의 영역 길이도 각각 (W-1)*dx와 W*dx다. |
| CT1-369 | 설정 표의 적용 판 | C 문서 누락 | `models/Celeris/manual-notes/celeris-architecture-and-config.md:79` ``\| `Accuracy_mode` (고차) \| — \| `Pass1_HighOrder.wgsl`, `Pass2_HighOrder_HLLC.wgsl` (현 고차 경로는 HLLC 선택) \|`` | 고차 HLLC 선택은 본판에 한정한다. transect 판의 입력 waves.txt는 numberOfWaves열·3*HEIGHT행의 진폭·주기·위상 묶음이다. 같은 이름의 JSON 키라도 파랑 파일과 바인딩 계약을 두 판 사이에서 그대로 옮기지 않는다. |
| CT1-370 | 이론 계보와 단면 구현 분리 | C 문서 누락 | `models/Celeris/web-refs/celeris-coulwave-theory.md:14` ``> ⚠️ **2026-06-15 정정**: 이 노트의 이전 판은 COULWAVE를 "Lynett-Liu 2004 **2층(two-layer)** 모델, kh≈6 deep-water"로 규정했으나 **소스 정독 결과 틀림**. Celeris는 **단일 reference velocity z_α(single-layer)**만 쓴다(`Pass3A_COULWAVE.wgsl:44` za 단일값). 코드의 "COULWAVE equations"는 **단일층 완전비선형(fully-nonlinear) 확장 Boussinesq**이며, 2층 모델은 **구현돼 있지 않다**. 아래는 그 정정판.`` | 단일 reference velocity라는 설명은 유지한다. 이론 계보만으로 transect 수식의 누락을 정당화하지 않는다. transect의 y 미분 제거와 실제 1D 구현 결함 후보는 이 보고서의 원문 대조를 별도로 인용한다. |
| CT1-371 | 공식 자료와 transect 적용 범위 | C 문서 누락 | `models/Celeris/web-refs/celeris-official-resources.md:31` ``- **Lynett, P. et al. (2026)** "An Interactive Nearshore Wave Simulator for Rapid Design Prototyping and Natural Hazard Education." *J. Waterway, Port, Coastal, and Ocean Engineering* **152**(4). DOI: [10.1061/JWPED5.WWENG-2370](https://doi.org/10.1061/JWPED5.WWENG-2370) (2026-04-03). — 본 위키가 분석한 **Celeris-WebGPU**(브라우저)의 논문. ★초록이 **두 위상해상 모델 = Madsen & Sørensen enhanced Boussinesq + 완전비선형 확장 Boussinesq, modern FV scheme**으로 명시 — 본 위키 소스 정독 결론([`celeris-coulwave-theory.md`](celeris-coulwave-theory.md) §0 모드1=Madsen·모드2=완전비선형)과 **독립 일치**. (repo `docs/lynett-et-al-2026-...pdf` 동봉.)`` | WebGPU 논문과 공식 저장소 연결은 유지한다. 본판과 transect 판을 구분하는 문장을 추가한다. 논문 초록의 모드·정확도 서술을 transect의 현재 모든 경로에 자동 적용하지 않는다. |
| CT1-372 | 논문 초록과 코드 판 | C 문서 누락 | `models/Celeris/web-refs/celeris-lynett-2026.md:18` `> **Celeris-WebGPU (version 1)**은 브라우저 기반 인터랙티브 nearshore wave 시뮬레이터로, **연안공학 설계와 자연재해 교육**을 지원한다. 두 가지 depth-integrated phase-resolving 모델을 구현한다 — (1) **standard mode**: 약비선형·약분산용 *enhanced Boussinesq* 방정식, (2) **high-order mode**: 정확도 향상을 위한 *완전비선형 확장(extended) Boussinesq* 방정식. 두 모드 모두 **hybrid finite-volume–finite-difference** 기법을 쓰며, standard는 공간 2차, high-order는 4차 정확도. 시뮬레이션·시각화 파이프라인 전체가 **WebGPU**를 통해 GPU에서 구동되어, 웹 브라우저 안에서 일반 데스크탑 하드웨어로 **faster-than-real-time** 성능을 낸다. (초록 발췌, p.04026007-1)` | 이 문단은 논문 초록의 주장임을 유지한다. transect 판의 고차 재구성과 고차 flux 선택은 현재 소스에서 따로 확인한다. 이 보고서는 PDF 식·표·그림의 새로운 검증을 주장하지 않는다. |
| CT1-373 | 표준 Pass2의 퇴적물 확산과 phi | A 판 차이 | `shaders/Pass2.wgsl:190` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),` / `transect_version/shaders/Pass2.wgsl:165`는 CT1-182의 전체 diff 참조. | 본판 표준 Pass2는 class 1의 x·y flux에 -k*h*grad(C)를 더한다. 본판은 퇴적물 flux 직전에 phix=phiy=0.5로 다시 설정한다. transect 판은 x 순수 이류 flux를 쓰고 수리 near-dry 분기에서 정한 phix를 유지한다. 이 차이는 수리 flux의 1D 동등성에 포함되지 않는다. |
| CT1-374 | 두 면 통계 평균의 1D 동등성 | F 표기 차이 | `transect_version/shaders/CalcMeans.wgsl:42` `let h = (h4.y + h4.w) / 2.0;` / CT1-163의 전체 diff. | 북·남 두 면의 본판 속도가 각 동·서 면 평균과 같다면 네 면 평균은 두 x 면 평균과 같다. transect의 h·u·c 평균은 이 두 면 평균을 명시한다. 실제 txNewState에서 읽는 본판 eta와 h+bottom으로 만든 transect eta는 별도 A 차이다. |
| CT1-375 | transect 셰이더 URL 접두어 | C 문서 누락 | `transect_version/js/main.js:1031` `const Pass0_ShaderCode = await fetchShader('/transect_version/shaders/Pass0.wgsl');` / CT1-285. | transect main은 모든 셰이더 URL을 /transect_version/shaders 아래에서 읽는다. 이 URL은 문서 루트에 transect_version 경로가 존재한다고 가정한다. 계산식 변경과 배포 경로 변경을 분리해서 적는다. |
| CT1-376 | pulse 지속 길이와 trough 배율 | A 판 차이 | `shaders/BoundaryPass.wgsl:176` `num_waves = 5;` / `transect_version/shaders/BoundaryPass.wgsl:165`의 전체 이어진 조건은 CT1-156 참조. | transect pulse는 4주기이고 본판 pulse는 5주기다. 본판은 음의 eta에만 trough_factor를 곱한다. 본판 bb99fee의 2026-07-02 변경은 transect의 1D 미분 제거와 별개의 입사 파형 변경이다. |
| CT1-377 | 본판 pulse UI의 4 waves 오기 | B 문서 오기 | `index.html:766` `<option value="2">*Transient Pulse (4 waves)</option>` / `shaders/BoundaryPass.wgsl:176` `num_waves = 5;` | 본판 index의 pulse label은 4 waves지만 같은 판 BoundaryPass는 num_waves=5를 사용한다. 두 파일은 같은 ebca435 판이다. label의 별표는 미지원 안내지만 활성 incident_wave_type==2의 수치 5를 4로 바꾸지 않는다. 노트에는 UI 표시와 구현의 수량 불일치를 적는다. |
| CT1-378 | 단면 입사파의 국소 수심 | C 문서 누락 | `shaders/BoundaryPass.wgsl:190` `let B_here = -globals.base_depth; //textureLoad(txBottom, idx, 0).b;` / `transect_version/shaders/BoundaryPass.wgsl:175`의 전체 diff는 CT1-156 참조. | transect BoundarySineWave는 해당 행·해당 경계 셀의 바닥고를 쓴다. 본판은 -base_depth를 쓴다. 따라서 단면마다 경계 수심이 다르면 파수와 운동량의 크기도 단면마다 달라진다. 이 선택은 단지 y 위상을 0으로 둔 대수적 환원과 다르다. |
| CT1-379 | 비활성 GeoTIFF 호출의 readback 인자 | E 코드 결함 후보 (강함) | `js/File_Writer.js:41` `const data = await readTextureData(device, texture, channel,dx,dy); // This should be compatible with the values expected by writeArrayBuffer` / `js/File_Writer.js:20` `await buffer.mapAsync(GPUMapMode.READ);` 반대 근거·두 경로 대조: 비활성 GeoTIFF 호출 절. | 본판 readTextureData는 네 번째 인자로 버퍼를 받는다. 같은 본판 downloadGeoTiffData는 그 자리에 dx를 넘긴다. 이 API 불일치는 09cfd76의 공용 버퍼 변경 뒤 남은 결함 후보다. 현재 실행 경로에서 호출되지 않음. 본판 주석도 not used needs updates to be used라고 명시한다. 근거 강도는 강함이다. |

### 5.1 기록 대조 확인

공통 66개 파일의 `diff -u --strip-trailing-cr`를 다시 실행했다.
기대 diff 구간은 290개다.
보고서의 diff 코드 블록도 290개다.
차이 구간의 누락은 0개다.
추가로 끼어든 diff 구간도 0개다.
이 수치는 diff 구간 전체 문자열의 다중집합을 비교한 결과다.
결론 표의 행 ID는 379개다.
중복 행 ID는 0개다.
파일·줄과 바로 붙인 원문 인용 631개를 원본 줄과 다시 대조했다.
해당 인용의 줄 불일치는 0개다.
이 검사는 문장 해석이나 수치 타당성 검증을 대체하지 않는다.

`22e1983`의 공통 66쌍 원문도 읽기 전용 `git show`로 열었다.
그 판의 CRLF 파일은 본판의 52개다.
그 판의 transect 파일은 모두 LF다.
따라서 2.1절의 52개 줄바꿈 F 행은 transect 최초 추가 때부터의 판 차이를 기록한다.
각 파일의 뒤 이력은 파일별 `--follow -p` 표를 따른다.

비일치 행은 모두 A·B·C·E·F 중 하나의 결론을 갖는다.
일치 파일과 줄바꿈만 다른 파일의 범위는 2.1절에서 확인할 수 있다.
모델·브라우저·셰이더 컴파일·수치 실험은 실행하지 않았다.
실행 결과와 물리적 타당성 검증은 이 보고서의 완료 주장에 포함하지 않는다.
원본 코드와 현재 노트는 수정하지 않았다.

분류별 개수: A 168, B 3, C 43, D 0, E 45, F 120, H 0, X 0. 합계 379행. 열지 못한 파일: 없음.
