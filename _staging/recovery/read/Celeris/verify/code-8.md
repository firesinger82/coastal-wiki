# Celeris code-8 전수 검증

검증일: 2026-11-04.

각 기록의 frontmatter `file:` 원문을 기록 구간별로 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조한다. 한 출력 구간은 200행 이하이다. 원문 인용의 문자열·행 번호 대조와 요약의 의미·바깥 블록 대조를 함께 수행한다. 원문·노트·git은 수정하지 않는다. 모델은 실행하지 않는다.

대상 11개 기록의 163개 구간을 모두 대조했다. 원문 행 수의 합계는 5,046행이다. 공백이 아닌 원문 4,380행은 각 기록의 원문 인용과 문자열·행 번호가 일치했다. 행 수는 각 원문의 실제 행과 기록의 구간 표에서 집계했다. 원문 파일의 SHA-256은 기록의 frontmatter 값과 모두 일치했다. frontmatter와 구간 경계는 변경하지 않았다.

행 수는 판독 기록의 구간 표 행 수와 해당 원문의 물리적 행 수를 구분한다. 정정·보완 수는 각 표지의 적용 구간 수이다. 한 구간에 두 표지가 있으면 각각 센다. 이상 없음 수는 완료한 기록에서 두 표지가 모두 없는 구간 수이다.

| 기록 | 상태 | 대조한 기록 구간 행 수 | 대조한 원문 행 수 |
|---|---|---:|---:|
| Handler_UpdateTrid.js.md | 완료 | 3 | 81 |
| Handler_Updateneardry.js.md | 완료 | 2 | 54 |
| Model_Loaders.js.md | 완료 | 10 | 236 |
| Run_Compute_Shader.js.md | 완료 | 3 | 52 |
| Run_Tridiag_Solver.js.md | 완료 | 3 | 77 |
| Time_Series.js.md | 완료 | 7 | 169 |
| constants_load_calc.js.md | 완료 | 13 | 480 |
| display_parameters.js.md | 완료 | 9 | 228 |
| main.js.md | 완료 | 103 | 3431 |
| site.js.md | 완료 | 1 | 4 |
| AddDisturbance.wgsl.md | 완료 | 9 | 234 |

기록 경로는 `_staging/recovery/read/Celeris/Celeris-WebGPU/transect_version/` 기준이다. JS 기록은 `js/` 아래에 있다. AddDisturbance.wgsl.md는 `shaders/` 아래에 있다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 | 구분 |
|---|---|---|---|---|
| Handler_Updateneardry.js.md:34–54 | create_Updateneardry_BindGroup은 레이아웃을 생성하고 uniformBuffer, txBottom, txtemp_bottom의 뷰를 binding 0–2 순서로 연결한다(34–53). | create_Updateneardry_BindGroup은 레이아웃을 생성한다(36). binding 0의 버퍼는 `uniformBuffer`이다(39–41). binding 1·2의 텍스처 뷰는 각각 `txBottom.createView()`·`txtemp_bottom.createView()`이다(45–50). | 36–50 | 정정 |
| Run_Tridiag_Solver.js.md:57–77 | 시작 시 3행 runTridiagSolver 함수·34–35행 else 안. | 시작 시 3행 runTridiagSolver 함수 안이다. 바깥 분기는 31행 `if (calc_constants.NLSW_or_Bous == 0) {`의 34–35행 `else`이다. 이 `else`는 76행에서 닫힌다. | 31–35, 76 | 보완 |
| Model_Loaders.js.md:1–19 | models가 없으면 빈 배열을 반환한다(17). | `return config.models \|\| [];`는 `config.models`가 falsy이면 빈 배열을 반환한다(17). | 17 | 정정 |
| Model_Loaders.js.md:43–66 | 정의 로딩 실패 시 빈 model_properties를 반환한다(46–51). | 정의 로딩 실패 시 `console.error`로 URL과 예외 `e`를 출력한다(49). 그 뒤 빈 `model_properties`를 반환한다(50). | 46–51 | 보완 |
| Model_Loaders.js.md:43–66 | defs를 순회하면서 type이 box인 경우 center·size와 도 단위 rotation을 사용해 행렬을 구성하고 id·type·modelMatrix를 저장한다(53–62). | defs를 순회하면서 type이 box인 경우 center·size와 도 단위 rotation을 사용해 행렬을 구성하고 id·type·modelMatrix를 저장한다(53–62). 54행 `if (def.type === 'box') {`에는 실행되는 `else`가 없다. 61행 tree 분기는 주석이다. | 53–62 | 보완 |
| Model_Loaders.js.md:175–201 | getAccessorArray는 accessor와 bufferView 존재를 검사한다(175–185). | getAccessorArray는 `gltf.accessors[accessorIndex]`를 읽는다(176). 177행 `if (acc.bufferView === undefined) {`는 accessor의 `bufferView` 속성을 검사한다. 183행 `if (!bv) {`는 조회한 bufferView를 검사한다. accessor 객체 `acc` 자체의 존재를 검사하는 분기는 없다. | 175–185 | 정정 |
| display_parameters.js.md:68–107 | 모델 1·2의 명칭과 계산 시간·실시간 대비 속도를 표시한다(96–103). | 모델 1·2의 명칭과 계산 시간·실시간 대비 속도를 표시한다(96–103). 88–101행 모델 선택 사슬에는 마지막 `else`가 없다. | 88–103 | 보완 |
| display_parameters.js.md:204–228 | addBoundaryDescription은 기본 Unknown 문자열을 만들고 경계 0·1·2·3을 Solid Wall·Sponge Layer·Incoming Wave·Periodic Boundary로 대응한다(204–219). | addBoundaryDescription은 기본 Unknown 문자열을 만들고 경계 0·1·2·3을 Solid Wall·Sponge Layer·Incoming Wave·Periodic Boundary로 대응한다(204–219). 208–216행 사슬에는 마지막 `else`가 없다. 어느 조건도 참이 아니면 초기 Unknown 문자열을 표시한다. | 204–219 | 보완 |
| AddDisturbance.wgsl.md:56–79 | landslide_subaerial은 폭·길이 역수 계수와 회전 좌표를 계산한다(56–66). | landslide_subaerial은 폭·길이 역수 계수를 계산한다(57–58). `let xc = xloc * cos_c + yloc * sin_c;`로 xc를 계산한다(63). `let yc = sqrt( x_sin * x_sin + y_cos * y_cos);`로 yc를 계산한다(66). yc는 부호 있는 회전 y좌표가 아니다. | 56–66 | 정정 |
| AddDisturbance.wgsl.md:180–202 | 시작 시 156행 main 함수·175행 교란 형식 조건문의 후속 else if 지점. | 시작 시 156행 main 함수 안이다. 175행 `if (globals.disturbanceType == 1) {` 가지는 180행 `}`에서 닫힌다. 180행은 같은 사슬의 `else if (globals.disturbanceType == 2) {` 가지를 연다. 이 가지는 189행에서 닫힌다. 형식 3 가지는 196행에서 닫힌다. 형식 4 가지는 203행에서 닫힌다. | 175–203 | 보완 |
| AddDisturbance.wgsl.md:203–234 | 시작 시 156행 main 함수·175행 교란 형식 조건문의 후속 else if 지점. | 시작 시 156행 main 함수 안이다. 196행 `else if (globals.disturbanceType == 4) {` 가지는 203행 `}`에서 닫힌다. 203행은 같은 사슬의 `else if (globals.disturbanceType == 5) {` 가지를 연다. 이 가지는 226행에서 닫힌다. 이 사슬에는 마지막 `else`가 없다. | 196–226 | 보완 |
| AddDisturbance.wgsl.md:203–234 | 분기 밖에서 state + disturbance를 계산하고 | 분기 밖에서 `let state_out = in_state_here + disturbance;`를 계산하고 | 228 | 정정 |
| main.js.md:329–382 | catch의 문장은 비교식이다(353–356). | catch는 실패 로그를 출력한다(354). `calc_constants.GoogleMapOverlay == 0`은 대입문이 아니라 비교식이다(355). | 353–356 | 정정 |
| main.js.md:329–382 | 업로드 또는 예제 오버레이(overlay)를 고르고 | 360행 `if(OverlayFile){`와 363행 `else if(calc_constants.run_example>=0) {`는 업로드 또는 예제 오버레이(overlay)를 고른다. 이 사슬에는 마지막 `else`가 없다(365). | 360–365 | 보완 |
| main.js.md:451–491 | modelFile 존재 여부로 업로드 또는 기본 URL의 박스 모델 정의를 읽는다(458–463). 단위 큐브 정점과 면 인덱스를 만들고 | `if(modelFile){`가 참이면 `loadSceneModels(modelFile)`로 정의를 읽는다(458–460). `else`에서는 `loadSceneModels(calc_constants.models_file_url)`로 정의를 읽는다(461–463). 각 축 좌표가 -1 또는 +1인 큐브 정점과 면 인덱스를 만들고 | 458–490 | 정정 |
| main.js.md:1001–1029 | Render uniform의 나머지 마찰·수직비·패딩을 144–188에 기록한다(1001–1012). | Render uniform의 나머지 마찰 값을 144–172에 기록한다(1001–1008). `calc_constants.bathy_cmap_zero`·`calc_constants.renderZScale`을 각각 176·180에 기록한다(1009–1010). 184·188에는 `0.0`을 기록한다(1011–1012). | 1001–1012 | 정정 |
| main.js.md:1030–1072 | NLSW_or_Bous 1·2에 따라 Bous 또는 COULWAVE Pass3를 고른다(1051–1058). | NLSW_or_Bous 1·2에 따라 Bous 또는 COULWAVE Pass3를 고른다(1051–1058). 이 사슬에는 마지막 `else`가 없다. 두 조건이 모두 거짓이면 `Pass3_ShaderCode_Bous`는 1050행의 `null`을 유지한다. | 1050–1058 | 보완 |
| main.js.md:1201–1234 | 시작 시 86행 initializeWebGPUApp 함수·1190행 gridHeight > 1 분기 안. | 시작 시 86행 initializeWebGPUApp 함수·1190행 `if (gridHeight > 1) {` 분기 안. | 1190–1201 | 보완 |
| main.js.md:1339–1376 | 1328행 html_update 분기 안. | 1328행 `if (calc_constants.html_update > 0) {` 분기 안. 이 분기는 1471행에서 닫힌다. | 1328, 1471 | 보완 |
| main.js.md:1377–1405 | 1328행 html_update 분기 안. | 1328행 `if (calc_constants.html_update > 0) {` 분기 안. 이 분기는 1471행에서 닫힌다. | 1328, 1471 | 보완 |
| main.js.md:1406–1434 | 1328행 html_update 분기 안. | 1328행 `if (calc_constants.html_update > 0) {` 분기 안. 이 분기는 1471행에서 닫힌다. | 1328, 1471 | 보완 |
| main.js.md:1435–1472 | 1328행 html_update 분기 안. | 1328행 `if (calc_constants.html_update > 0) {` 분기 안. 이 분기는 1471행에서 닫힌다. | 1328, 1471 | 보완 |
| main.js.md:1406–1434 | Google 또는 위성 이미지가 이미 로딩된 선택인 경우 변환·txOverlayMap을 바꾸고 RenderBindGroup을 재생성한 뒤 로드 플래그를 켠다(1409–1433). | Google 또는 위성 이미지가 이미 로딩된 선택인 경우 변환·txOverlayMap을 바꾸고 RenderBindGroup을 재생성한 뒤 로드 플래그를 켠다(1409–1433). 1409–1432행 사슬에는 마지막 `else`가 없다. 두 조건이 모두 거짓이면 `IsOverlayMapLoaded`는 1408행의 0을 유지한다. | 1408–1433 | 보완 |
| main.js.md:1473–1500 | 요소 1–10에 따라 마찰 계수를 선택한다(1486–1495). | 요소 1–10에 따라 마찰 계수를 선택한다(1486–1495). 이 사슬에는 마지막 `else`가 없다. 어느 조건도 참이 아니면 `designcomponent_Friction`은 이 사슬에서 바뀌지 않는다. | 1486–1496 | 보완 |
| main.js.md:1501–1538 | 1474행 click_update 분기·1476행 평면 수정 분기 안. | 1474행 `if (calc_constants.click_update > 0) {`·1476행 `if (calc_constants.click_update == 1 && calc_constants.viewType == 1) {` 분기 안. 1476행 가지는 1525행에서 닫힌다. 1526행은 같은 사슬의 `else if (calc_constants.click_update == 2 && calc_constants.viewType == 2)`이다. 1474행 분기는 1536행에서 닫힌다. | 1474–1476, 1525–1536 | 보완 |
| main.js.md:1501–1538 | click_update를 -1로 설정한다(1535–1536). | click_update를 -1로 설정한다(1535–1536). 수정 대상 선택 사슬(1502–1519), 패널 선택 사슬(1501–1524), 클릭 모드 선택 사슬(1476–1533)에는 각각 마지막 `else`가 없다. | 1476–1536 | 보완 |
| main.js.md:1592–1600 | 1560행 실행 분기·1561행 frame_c 루프 | 1560행 `if (calc_constants.simPause < 0) {` 분기·1561행 `for (let frame_c = 0; frame_c < calc_constants.render_step; frame_c++) {` 루프 | 1560–1561 | 보완 |
| main.js.md:1601–1620 | 1560행 실행 분기·1561행 frame_c 루프 | 1560행 `if (calc_constants.simPause < 0) {` 분기·1561행 `for (let frame_c = 0; frame_c < calc_constants.render_step; frame_c++) {` 루프 | 1560–1561 | 보완 |
| main.js.md:1621–1654 | 1560행 실행 분기·1561행 frame_c 루프 | 1560행 `if (calc_constants.simPause < 0) {` 분기·1561행 `for (let frame_c = 0; frame_c < calc_constants.render_step; frame_c++) {` 루프 | 1560–1561 | 보완 |
| main.js.md:1655–1670 | 1560행 실행 분기·1561행 frame_c 루프 | 1560행 `if (calc_constants.simPause < 0) {` 분기·1561행 `for (let frame_c = 0; frame_c < calc_constants.render_step; frame_c++) {` 루프 | 1560–1561 | 보완 |
| main.js.md:1601–1620 | 1593행 COULWAVE 분기 안. | 1593행 `if (calc_constants.NLSW_or_Bous == 2) {` 분기 안. | 1593–1602 | 보완 |
| main.js.md:1671–1711 | 1560행 실행 분기·1561행 frame_c 루프 | 1560행 `if (calc_constants.simPause < 0) {` 분기·1561행 `for (let frame_c = 0; frame_c < calc_constants.render_step; frame_c++) {` 루프 | 1560–1561 | 보완 |
| main.js.md:1712–1754 | 1560행 실행 분기·1561행 frame_c 루프 | 1560행 `if (calc_constants.simPause < 0) {` 분기·1561행 `for (let frame_c = 0; frame_c < calc_constants.render_step; frame_c++) {` 루프 | 1560–1561 | 보완 |
| main.js.md:1755–1782 | 1560행 실행 분기·1561행 frame_c 루프 | 1560행 `if (calc_constants.simPause < 0) {` 분기·1561행 `for (let frame_c = 0; frame_c < calc_constants.render_step; frame_c++) {` 루프 | 1560–1561 | 보완 |
| main.js.md:1783–1803 | 1560행 실행 분기·1561행 frame_c 루프 | 1560행 `if (calc_constants.simPause < 0) {` 분기·1561행 `for (let frame_c = 0; frame_c < calc_constants.render_step; frame_c++) {` 루프 | 1560–1561 | 보완 |
| main.js.md:1712–1754 | 1671–1672행 보정 분기 안. | 1671–1672행 `if (calc_constants.timeScheme == 2)` 분기 안. 이 분기는 1753행에서 닫힌다. | 1671–1672, 1753 | 보완 |
| main.js.md:1804–1833 | 현재 화면 크기와 깊이 텍스처 크기가 다르면 깊이 텍스처를 재생성한다(1826–1832). | 깊이 텍스처가 없거나 현재 화면 텍스처와 폭 또는 높이가 다르면 깊이 텍스처를 재생성한다(1828–1830). | 1826–1832 | 정정 |
| main.js.md:1804–1833 | 3D 모드 2는 막대를 끄고 정점 격자 파이프라인을 생성한다(1815–1823). | 3D 모드 2는 막대를 끄고 정점 격자 파이프라인을 생성한다(1815–1823). 1806–1823행 모드 선택 사슬에는 마지막 `else`가 없다. | 1806–1823 | 보완 |
| main.js.md:1872–1911 | 1871행 viewType 2 분기 안. | 1856행 `if (calc_constants.viewType == 1)` 사슬의 1871행 `else if (calc_constants.viewType == 2)` 분기 안. | 1856–1872 | 보완 |
| main.js.md:1912–1945 | 1871행 viewType 2 분기 안. | 1856행 `if (calc_constants.viewType == 1)` 사슬의 1871행 `else if (calc_constants.viewType == 2)` 분기 안. | 1856–1872 | 보완 |
| main.js.md:1946–1977 | 1871행 viewType 2 분기 안. | 1856행 `if (calc_constants.viewType == 1)` 사슬의 1871행 `else if (calc_constants.viewType == 2)` 분기 안. | 1856–1872 | 보완 |
| main.js.md:1978–2000 | 1871행 viewType 2 분기 안. | 1856행 `if (calc_constants.viewType == 1)` 사슬의 1871행 `else if (calc_constants.viewType == 2)` 분기 안. | 1856–1872 | 보완 |
| main.js.md:2001–2031 | 1871행 3D 분기 | 1856행 `if (calc_constants.viewType == 1)` 사슬의 1871행 `else if (calc_constants.viewType == 2)` 분기 | 1856–1872 | 보완 |
| main.js.md:2032–2079 | 1871행 3D 분기 | 1856행 `if (calc_constants.viewType == 1)` 사슬의 1871행 `else if (calc_constants.viewType == 2)` 분기 | 1856–1872 | 보완 |
| main.js.md:2001–2031 | 1990행 deltaPanY 분기·1995행 지면 고정 참 분기·1996행 scaleAndAdd 호출 안. | 1990행 `if (deltaPanY !== 0) {`·1995행 `if (calc_constants.renderLocktoGround == 1) {` 분기·1996행 `vec3.scaleAndAdd(` 호출 안. 1995행 가지는 2002행에서 닫힌다. 같은 행의 `else`는 2009행에서 닫힌다. 1990행 분기는 2010행에서 닫힌다. | 1990–2010 | 보완 |
| main.js.md:2080–2124 | 1871행 3D 분기 안. | 1856행 `if (calc_constants.viewType == 1)` 사슬의 1871행 `else if (calc_constants.viewType == 2)` 분기 안. 이 가지는 2142행에서 닫힌다. | 1856–1872, 2142 | 보완 |
| main.js.md:2125–2150 | 1871행 3D 분기 안. | 1856행 `if (calc_constants.viewType == 1)` 사슬의 1871행 `else if (calc_constants.viewType == 2)` 분기 안. 이 가지는 2142행에서 닫힌다. | 1856–1872, 2142 | 보완 |
| main.js.md:2125–2150 | 3D 분기 종료 후 렌더 패스를 종료하고 큐에 제출한다(2142–2148). | 3D 분기 종료 후 렌더 패스를 종료하고 큐에 제출한다(2142–2148). 1856–2142행 모드 선택 사슬에는 마지막 `else`가 없다. | 1856–1872, 2142–2148 | 보완 |
| main.js.md:2151–2174 | 시계열 시간이 최대 지속시간을 넘으면 데이터가 있는 경우 다운로드하고 시간을 초기화한다(2159–2167). | 시계열 시간이 최대 지속시간을 넘으면 `if(calc_constants.NumberOfTimeSeries > 0) {`에서 다운로드를 호출한다(2160–2164). 이 조건은 저장된 데이터 유무를 검사하지 않는다. 최대 지속시간을 넘은 분기는 시계열 카운터와 시간을 0으로 초기화한다(2165–2166). | 2159–2167 | 정정 |
| main.js.md:2230–2263 | 2214행 create_animation > 0 분기 안. | 2214행 `if(calc_constants.create_animation > 0){` 분기 안. 이 분기는 2262행에서 닫힌다. | 2214, 2262 | 보완 |
| main.js.md:2230–2263 | 마지막 프레임에 모드 1은 GIF, 모드 2는 이미지들을 저장한다(2246–2253). | 마지막 프레임에 모드 1은 GIF, 모드 2는 이미지들을 저장한다(2246–2253). 2248–2253행 저장 모드 선택 사슬에는 마지막 `else`가 없다. | 2246–2253 | 보완 |
| main.js.md:2300–2327 | 2265행 단일 표면 저장 분기·2266행 선택 조건문의 후속 else if 지점. | 2265행 `if(calc_constants.write_individual_surface == 1){` 분기 안. 2296행 `else if(calc_constants.which_surface_to_write == 7){` 가지는 2300행에서 닫힌다. 2300행은 2266행 `if(calc_constants.which_surface_to_write == 0){` 사슬의 `else if(calc_constants.which_surface_to_write == 8){` 가지를 연다. 마지막 선택값 13 가지는 2323행에서 닫힌다. 이 사슬에는 마지막 `else`가 없다. 바깥 2265행 분기는 2326행에서 닫힌다. | 2265–2266, 2296–2326 | 보완 |
| main.js.md:2359–2400 | 2344행 자동 파고 저장 분기 안. | 2344행 `if(calc_constants.trigger_writeWaveHeight == 3 && total_time >= calc_constants.trigger_writeWaveHeight_time){` 분기 안. 이 분기는 2398행에서 닫힌다. | 2344, 2398 | 보완 |
| main.js.md:2420–2459 | 표면 저장 트리거 상태·시각에 따라 writesurfaces를 켜거나 끈다(2422–2431). | 표면 저장 트리거 상태·시각에 따라 writesurfaces를 켜거나 끈다(2422–2431). 이 사슬에는 마지막 `else`가 없다. | 2422–2431 | 보완 |
| main.js.md:2499–2542 | 카운터 > 1이면 패널을 접고 == 1이면 whichPanelisOpen을 설정한다(2514–2520). | 카운터 > 1이면 패널을 접고 == 1이면 whichPanelisOpen을 설정한다(2514–2520). 이 사슬에는 마지막 `else`가 없다. | 2514–2520 | 보완 |
| main.js.md:2567–2601 | 오른쪽·모드 2는 회전 시작 상태를 저장한다(2594–2600). | 오른쪽·모드 2는 회전 시작 상태를 저장한다(2594–2600). 2578–2599행 사슬에는 마지막 `else`가 없다. | 2578–2599 | 보완 |
| main.js.md:2602–2629 | 그 외 오른쪽 버튼이면 x/y 이동에 0.1을 곱해 회전각을 바꾸고 이전 좌표·갱신 플래그를 저장한다(2617–2628). | 그 외 오른쪽 버튼이면 x/y 이동에 0.1을 곱해 회전각을 바꾸고 이전 좌표·갱신 플래그를 저장한다(2617–2628). 2604–2627행 사슬에는 마지막 `else`가 없다. | 2604–2627 | 보완 |
| main.js.md:2630–2662 | pointerup은 포인터 캡처를 해제하고 버튼별 상태·click_update를 초기화한다(2631–2642). | pointerup은 포인터 캡처를 해제하고 버튼별 상태·click_update를 초기화한다(2631–2642). 2635–2641행 사슬에는 마지막 `else`가 없다. 버튼이 0도 2도 아니면 캡처 해제만 수행한다. | 2631–2642 | 보완 |
| main.js.md:2663–2692 | switch는 a/A/ArrowLeft, d/D/ArrowRight, w/W/ArrowUp, s/S/ArrowDown에 따라 shift_x·shift_y를 가감한다(2668–2689). | switch는 a/A/ArrowLeft, d/D/ArrowRight, w/W/ArrowUp, s/S/ArrowDown에 따라 shift_x·shift_y를 가감한다(2668–2689). 이 switch에는 `default`가 없다. 나열되지 않은 키도 switch 앞에서 `calc_constants.click_update = 2;`를 실행한다(2667). | 2665–2690 | 보완 |
| main.js.md:2693–2733 | deltaY 부호에 따라 forward를 배율 조정하고 0.001–100으로 제한한다(2709–2718). | deltaY 부호에 따라 forward를 배율 조정하고 0.001–100으로 제한한다(2709–2718). 2709–2715행 사슬에는 마지막 `else`가 없다. deltaY가 0이면 배율 조정 없이 2718행 범위 제한을 수행한다. | 2709–2718 | 보완 |
| main.js.md:2773–2800 | updateTooltip은 평면 모드의 하천·해안 분기에 따라 | updateTooltip은 평면 모드에서 `if (calc_constants.river_sim == 1){`와 그 `else`에 따라 | 2776–2783 | 정정 |
| main.js.md:2801–2829 | showBreaking 변경 시 clearConc를 켜고 값에 따라 소산 임계값·감쇠율을 바꾼다(2815–2824). | showBreaking 변경 시 clearConc를 켜고 값에 따라 소산 임계값·감쇠율을 바꾼다(2815–2824). 2817–2823행 사슬에는 마지막 `else`가 없다. 두 조건이 모두 거짓이면 소산 임계값과 감쇠율을 바꾸지 않는다. | 2815–2824 | 보완 |
| main.js.md:3269–3293 | waveFile이 없으면 /no_waves.txt를 읽고 기본 파랑으로 실행한다(3269–3278). | waveFile이 없으면 /no_waves.txt를 읽고 기본 파랑으로 실행한다(3269–3275). 이 fetch·후속 then 사슬이 거부되면 catch에서 `console.error("Failed to load the default wave file:", error);`를 호출한다(3276–3278). | 3269–3278 | 보완 |

정정 11, 보완 44, 이상 없음 111
