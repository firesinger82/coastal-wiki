# Celeris 노트 전수 검증 13

검증일: 2026-11-04.
대상은 사용자 지정 노트 4개의 작업 시작 시점 `git diff -U0 HEAD` 추가 줄이다.
빈 줄과 frontmatter도 대상 줄 수에 포함한다.
원문 코드는 Celeris-WebGPU ebca435 판을 기준으로 한다.
정정 수와 보완 수는 이번 검증에서 변경한 대상 줄 수로 센다.
기계 확인 후보는 사용자 제공 목록에 없다.

## 진행 기록

## celeris-sediment.md — 완료

대조한 대상 줄은 75줄이다. 정정은 12줄이다. 보완은 1줄이다.
대상 범위는 5–6, 20–22, 67, 91–92, 95–96, 105–106, 110, 112–113, 119–122, 129, 153, 166, 180–232행이다.
차이 표 43행의 분류와 결론 문장을 지정된 conclusion-verify의 같은 ID와 대조했다.
코드·문서·이전 커밋 인용을 해당 파일에서 열어 대조했다.
본문은 보고서 §4의 CD1-1345–1348, CD2-471–473, CP1-155, CP2-172, CP3-091–096 및 CT1-363–365·RF-012와 대조했다.
Lynett 2026 p.6 Fig.2는 쪽 이미지로 확인했다.
논문의 퇴적물 식 누락은 CP1-127·CP2-142–144 최종 근거와 쪽별 판독 기록을 대조했다.
frontmatter의 반영 날짜와 방법은 notes-apply-9 기록과 일치한다.
대상 줄의 상대 링크는 모두 존재한다. 금지 경로와 한계 문장은 없다. Mermaid 블록은 없다.

정정 목록의 경로 기준은 `models/Celeris/source-analysis/`이다. 근거 코드의 경로 기준은 `models/Celeris/raw/source_code/Celeris-WebGPU/`이다.

| 노트:줄 | 전 → 후 | 근거 원문 |
|---|---|---|
| celeris-sediment.md:196 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-944 최종 근거. `shaders/Pass2.wgsl:139–145`의 조건과 확산계수는 코드 원문이다. |
| celeris-sediment.md:197 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-945 최종 근거. `shaders/SedTrans_Pass3.wgsl:143–150,212–215,239`는 코드 원문이다. |
| celeris-sediment.md:198 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-946 최종 근거. `shaders/SedTrans_Pass3.wgsl:235–240`는 농도 하한과 출력 채널을 명시한다. |
| celeris-sediment.md:199 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-947 최종 근거. `shaders/SedTrans_UpdateBottom.wgsl:84–105,115`는 부호와 경계 램프의 코드 원문이다. |
| celeris-sediment.md:207 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-1300 최종 근거. `js/constants_load_calc.js:622–630`과 `js/main.js:2339–2340`의 식을 비교한 AI 설명이다. |
| celeris-sediment.md:208 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-1301 최종 근거. `js/main.js:1134,2806–2820`의 단계 전달을 비교한 AI 설명이다. |
| celeris-sediment.md:209 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-1304 최종 근거. `shaders/SedTrans_UpdateBottom.wgsl:107–115`의 미적용 하한을 해석한 설명이다. |
| celeris-sediment.md:210 | 이전 노트 직접 인용의 `js/constants_load_calc.js:622-630` → `constants_load_calc.js:622-630` | `d8157c80:models/Celeris/source-analysis/celeris-sediment.md:89`의 원래 경로에는 `js/`가 없다. |
| celeris-sediment.md:212 | 이전 노트 직접 인용의 `shaders/`·`js/` 접두어 → 원래 짧은 경로 | `d8157c80:models/Celeris/source-analysis/celeris-sediment.md:104`는 `SedTrans_Pass3.wgsl:102-119`와 `constants_load_calc.js:112-113`으로 적혀 있다. |
| celeris-sediment.md:214 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-1398 최종 근거. `js/main.js:1573–1586`의 활성 파일 선택을 해석한 설명이다. |
| celeris-sediment.md:221 | 이전 노트 직접 인용의 `shaders/`·`js/` 접두어 → 원래 짧은 경로 | `d8157c80:models/Celeris/source-analysis/celeris-sediment.md:104` 원문과 일치하도록 복원했다. |
| celeris-sediment.md:224 | `shaders/SedTrans_Pass3.wgsl:139–150` → `:139–151` | 151행의 `}`까지 포함해야 인용한 hard-bottom 조건문 전체를 포함한다. 인용 범위 보완이다. |
| celeris-sediment.md:229 | 존재하지 않는 “아래 C13” 참조 → 106–114행의 옵션·기본 계수 선언 설명 | `js/constants_load_calc.js:106–114`에 `useSedTransModel: 0,`부터 `loadHardBottom: 0,`까지 선언되어 있다. |

기계 확인 후보 판정: 사용자 제공 후보 없음.

## celeris-fv-reconstruction.md — 완료

대조한 대상 줄은 68줄이다. 정정은 15줄이다. 보완은 0줄이다.
대상 범위는 5–6, 28–30, 43–46, 66, 72, 133–134, 154–155, 157, 167, 173–175, 202–249행이다.
차이 표 36행의 분류와 결론 문장을 지정된 conclusion-verify의 같은 ID와 대조했다.
A 행의 문서 판은 Tavakkol 2017이다. version-verify-AD1의 CP1-028·029와 대조했다.
E 행의 강도와 비활성 HLLEM 파일의 표시를 최종 근거와 대조했다.
본판과 transect의 JS에서 `Pass2_HighOrder_HLLEM` 파일명 검색 결과는 0건이다.
transect가 별도 `Pass2_HighOrder.wgsl`의 HLLEM 함수를 부르는 사실도 확인했다.
본문은 보고서 §4의 CD1-1339–1341, CD2-467, CP1-144·145·149, CP2-169, CP3-115 및 CT1-359·360과 대조했다.
Tavakkol 2017 p.2·3, Tavakkol 2020 p.3·5·13, Lynett 2026 p.4의 해당 식과 인용번호는 쪽 이미지로 확인했다.
frontmatter는 notes-apply-9의 반영 기록과 일치한다.
대상 줄의 상대 링크는 모두 존재한다. 금지 경로와 한계 문장은 없다. Mermaid 블록은 없다.

| 노트:줄 | 전 → 후 | 근거 원문 |
|---|---|---|
| celeris-fv-reconstruction.md:66 | 현재 코드 경로 `Pass1.wgsl:31-39` → `shaders/Pass1.wgsl:31-39` | 현재 파일은 shaders 디렉터리에 있다. 31–39행은 MinMod의 양수·음수·그 밖의 분기이다. |
| celeris-fv-reconstruction.md:215 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-925 최종 근거와 `shaders/Pass1.wgsl:31–51`의 MinMod·재구성식. |
| celeris-fv-reconstruction.md:216 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-926 최종 근거와 `shaders/Pass1.wgsl:136,145–150`의 수심 제한·역수식. |
| celeris-fv-reconstruction.md:217 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-927 최종 근거의 Froude 제한식. 이 설명은 문서 원문이 아니다. |
| celeris-fv-reconstruction.md:218 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-928 최종 근거의 NumericalFlux 조건·반환식. 이 설명은 문서 원문이 아니다. |
| celeris-fv-reconstruction.md:219 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-929 최종 근거와 `shaders/Pass2.wgsl:115–120`의 질량 차·phix·phiy 처리. |
| celeris-fv-reconstruction.md:221 | 이전 노트 직접 인용의 `shaders/Pass1.wgsl:31-39` → `Pass1.wgsl:31-39` | `d8157c80:models/Celeris/source-analysis/celeris-fv-reconstruction.md:58`에는 `shaders/`가 없다. |
| celeris-fv-reconstruction.md:223 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-1381 최종 근거의 calcSlopes 보정식. 이 설명은 문서 원문이 아니다. |
| celeris-fv-reconstruction.md:224 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-1382 최종 근거의 `if (dh_max > 0.60)` 조건. 이 설명은 문서 원문이 아니다. |
| celeris-fv-reconstruction.md:225 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-1383 최종 근거의 wetdry·maxB3 조건. 이 설명은 문서 원문이 아니다. |
| celeris-fv-reconstruction.md:226 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-1384 최종 근거의 uRoe·S_star 식. 이 설명은 문서 원문이 아니다. |
| celeris-fv-reconstruction.md:227 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-1385 최종 근거와 `shaders/Pass2_HighOrder_HLLC.wgsl:113,139,143`의 결합식. |
| celeris-fv-reconstruction.md:228 | 문서 칸의 백틱 설명 → 일반 설명과 “문서에 해당 문장 없음” | CD1-1399 최종 근거와 `shaders/Pass2_HighOrder_HLLC.wgsl:106–110`의 safe_L·safe_R 식. |
| celeris-fv-reconstruction.md:246 | 직접 인용 안의 `정수압항 ...` → 삭제하여 연속된 실제 원문만 인용 | `d8157c80:models/Celeris/source-analysis/celeris-fv-reconstruction.md:125`에 `well-balanced 소스항/정수압이 Pass3 또는 reconstruction 단계로 흡수되는 구조`가 연속해서 있다. |
| celeris-fv-reconstruction.md:247 | 노트에 없는 “§1.2 전사” 참조 → 삭제하고 논문 p.3 식 (1)을 직접 지시 | Tavakkol 2020 p.3 쪽 이미지의 식 (1)과 바로 아래 `h is the total water depth`를 확인했다. 렌더 노트의 같은 형식 참조를 대조하면서 함께 정정했다. |

기계 확인 후보 판정: 사용자 제공 후보 없음.

## celeris-webgpu-infrastructure.md — 완료

대조한 대상 줄은 54줄이다. 정정은 3줄이다. 보완은 1줄이다.
대상 범위는 5–6, 17–22, 31, 49, 51, 55–62, 85, 110–114, 186–188, 190–193, 197, 214, 226–228, 239–240, 246–248, 255–256, 262–264, 272–276, 281–282행이다.
이 노트의 대상 줄에는 차이 표가 없다. 분리된 차이 표의 상대 링크는 실제 파일을 가리킨다.
본문은 보고서 §4의 CD1-1327–1333, CD2-474, CP1-139, CP2-173, CP3-117 및 CT1-366과 대조했다.
호출 순서는 callflow §6과 RF-002·003·011·015·020·025의 최종 결론을 대조했다.
`bb99fee:js/main.js:201–213,248–261`과 `afc1fe7:js/constants_load_calc.js:413–446`을 열어 판 차이 근거를 확인했다.
현재 코드의 텍스처 할당·PCR 우변·경계 입력·시간 적분·진단 카운터·시계열 초기화를 확인했다.
frontmatter는 notes-apply-3의 반영 기록과 일치한다.
대상 줄의 상대 링크는 모두 존재한다. 금지 경로와 한계 문장은 없다. Mermaid 블록은 없다.

| 노트:줄 | 전 → 후 | 근거 원문 |
|---|---|---|
| celeris-webgpu-infrastructure.md:17 | “CPU 행렬은 사실상 없다” → GPU 상태 갱신과 CPU 지형 배열을 각각 명시 | `js/File_Loader.js:36`은 `const bathy2D = Array.from({ length: calc_constants.WIDTH }, () => Array(calc_constants.HEIGHT));`이다. 54행에서 원소를 저장한다. `shaders/Pass3_Bous.wgsl:399–429`는 GPU 상태 갱신을 수행한다. 애플리케이션·모델 설명에는 `ARCHITECTURE.md:3,63–67`을 붙였다. |
| celeris-webgpu-infrastructure.md:20 | 파 성분·시계열의 근거 `js/main.js:559` → `:563–576` | 559행은 `txRenderVarsf16` 생성이다. 563행은 txWaves 생성이다. 566–576행은 경계·점 시계열 텍스처 생성이다. |
| celeris-webgpu-infrastructure.md:22 | “채널은 항상 4-vector” → `rgba32float` 유체 상태 텍스처의 네 채널로 범위 한정 | `js/Create_Textures.js:5`는 `rgba32float`이다. 같은 파일 91행의 렌더 깊이 텍스처는 `depth24plus`이므로 모든 텍스처에 네 채널을 일반화할 수 없다. |
| celeris-webgpu-infrastructure.md:240 | 셰이더·최종 근거만 인용 → 호스트 uniform 대입 위치 추가 | `js/main.js:1083`은 dt를 쓴다. 1095행은 초기 단계값을 쓴다. 2672–2673·2806–2807행은 예측·보정 단계값을 쓴다. 인용 보완이다. |

기계 확인 후보 판정: 사용자 제공 후보 없음.

## celeris-render.md — 완료

대조한 대상 줄은 54줄이다. 정정은 4줄이다. 보완은 0줄이다.
대상 범위는 5–6, 13, 36–45, 76–80, 124–134, 139–163행이다.
차이 표 14행의 분류와 결론 문장을 conclusion-verify-CP2의 같은 ID와 대조했다.
A 행의 문서 판은 Tavakkol 2020이다. version-verify-AD1의 같은 ID와 대조했다.
`471c581:js/main.js:458–481`과 `2eb2866:js/File_Loader.js:122–144`을 열어 이전 코드 근거를 확인했다.
본문은 보고서 §4의 CD1-1351·1352, CD2-475, CP1-157, CP2-179, CP3-081·076 및 CT1-367·368과 대조했다.
Tavakkol 2017 p.7·9·11의 Fig.5·9·14, Tavakkol 2020 p.6–8의 타일 구조·Fig.4·5·식 (10)–(13), Lynett 2026 p.12의 f32 설명은 쪽 이미지로 확인했다.
식 (11)의 인쇄된 분모는 C_min이다. 노트는 인쇄 원문과 부호 오기 판정을 구분한다.
텍스트 데이터 흐름도는 코드의 캐시 입력·정점 높이 입력과 대조했다.
이 노트에는 Mermaid 블록이 없다. callflow §4 그림의 전사 대상은 없다.
frontmatter는 notes-apply-9의 반영 기록과 일치한다.
대상 줄의 상대 링크는 모두 존재한다. 금지 경로와 한계 문장은 없다.

| 노트:줄 | 전 → 후 | 근거 원문 |
|---|---|---|
| celeris-render.md:157 | 노트에 없는 “§1.2 전사” 참조 → 삭제하고 논문 p.8 식 (10)을 직접 지시 | Tavakkol 2020 p.8 이미지의 `U=(C-C_min)/(C_max-C_min); V=0.5`와 아래 V 설명. |
| celeris-render.md:160 | 노트에 없는 “§1.2 전사” 참조 → 삭제하고 논문 p.8 식 (12)을 직접 지시 | Tavakkol 2020 p.8 이미지의 `M_x=lon/π`와 radians 정의. |
| celeris-render.md:161 | “§1.2 전사”와 “아래 지도 원문 M1” → 논문 식 (13) 위치와 실제 코드 인용 | `js/File_Loader.js:686–688`은 sin 계산, `const y = 0.5 - Math.log((1 + sin) / (1 - sin)) / (4 * Math.PI);`, `return y;`이다. |
| celeris-render.md:163 | 노트에 없는 “아래 M2” → 위도·경도 줌 계산과 최소값 반환의 실제 코드 인용 | `js/File_Loader.js:577–578,583`은 latZoom·lngZoom을 구하고 `return Math.min(latZoom, lngZoom, ZOOM_MAX);`를 수행한다. |

기계 확인 후보 판정: 사용자 제공 후보 없음.

## 최종 집계

| 노트 | 대조한 대상 줄 | 정정 줄 | 보완 줄 |
|---|---:|---:|---:|
| celeris-sediment.md | 75 | 12 | 1 |
| celeris-fv-reconstruction.md | 68 | 15 | 0 |
| celeris-webgpu-infrastructure.md | 54 | 3 | 1 |
| celeris-render.md | 54 | 4 | 0 |
| 합계 | 251 | 34 | 2 |

대상 줄 수는 작업 시작 시점의 지정된 `git diff -U0 HEAD`에서 센 값이다.
최종 diff의 추가 줄 수도 같은 251줄이다.
정정·보완 표시는 변경한 36줄에 있다.
이 기록의 변경 목록도 36행이다.
최종 검사에서 차이 표 93행의 분류는 배정표와 일치한다.
최종 검사에서 차이 표 93행의 결론은 conclusion-verify와 일치한다.
A 행의 문서 판 부기와 CP2-048의 논문명 명시는 동일한 근거를 명확히 하는 부기이다.
표 안의 코드 인용은 인용 범위 안의 원문과 대조했다.
루트의 HTML 파일·README.md·ARCHITECTURE.md 인용도 해당 파일에서 대조했다.
비교할 때 Markdown의 세로선 이스케이프와 줄바꿈·들여쓰기 공백을 정규화했다.
조건·식·부호·수량은 정규화하지 않았다.
최종 검사에서 대상 줄의 상대 링크 98개는 모두 실제 파일을 가리킨다.
최종 검사에서 금지 경로·문자열과 끊어진 C13·M1·M2·§1.2 참조는 없다.
지정된 네 노트의 `git diff --check HEAD`는 통과했다.
사용자가 제시한 기계 확인 후보는 없다.
미해결 항목은 없다.
쓰기 범위는 지정된 네 노트와 이 결과 파일이다.
git 쓰기 명령, sudo, 모델 실행은 수행하지 않았다.
