# Celeris 판 차이 재검증 — CT1

## 1 요약

대상은 `_staging/recovery/compare/celeris-transect-vs-main.md`의 「5 차이 결론」이다.
이 보고서에서 문서는 본판 코드다.
이 보고서에서 코드는 transect 사본이다.
코드 경로의 기준 루트는 `models/Celeris/raw/source_code/Celeris-WebGPU/`다.
위키 문서 경로는 저장소 루트를 기준으로 적었다.
판정은 로컬 git 이력과 파일 원문에 근거한다.

대상 행 수는 원 보고서 5절의 행 ID를 센 값이다.
원 A는 168행이다.
원 B는 3행이다.
원 D는 0행이다.
대상 합계는 171행이다.

| 원 결론 | 확정 결론 | 행 수 |
|---|---|---:|
| A | A | 167 |
| A | F | 1 |
| B | A | 0 |
| B | B | 3 |
| D | A | 0 |
| D | D | 0 |

CT1-223은 읽기 위치의 이동이므로 F로 재분류했다.
확정 A는 167행이다.
확정 B는 3행이다.
확정 F는 1행이다.
확정 행 수는 아래 판정 표의 행 ID를 센 값이다.

현재 줄은 작업 사본과 `ebca435` 스냅샷을 대조했다.
변경 줄은 각 커밋의 diff와 그 커밋의 파일 원문을 대조했다.
인용의 `HASH:파일:줄`은 해당 커밋에서의 줄 번호다.
인용의 `파일:줄`은 현재 파일의 줄 번호다.
변경 커밋은 인용 줄을 추가하거나 수정한 커밋이다.
변경 커밋이 기능 전체의 최초 도입을 뜻하는 경우에는 이유에 별도로 적었다.
표의 L 번호는 2절 뒤에 수록한 두 파일의 `git log --follow` 원문 목록을 가리킨다.
이 목록이 사본 추가 이전 경로까지 따라가는 경우에는 그 이전 커밋을 transect 경로의 존재 시점으로 읽지 않는다.
Markdown 표의 역슬래시는 원문 `|`을 보존하기 위한 구분자 이스케이프다.

## 2 A 행 판정 표

| 보고서 | 행 ID | 원 결론 | 확정 결론 | 근거 커밋·행 | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|
| CT1 §5 | CT1-056 | A 판 차이 | A 판 차이 | 현재 `js/Copy_Data_to_Textures.js:137` `function copyBoundaryTimeSeriesDataToTexture(boundaryTimeSeriesSideData, device, txBoundaryTimeSeries) {`<br>현재 `transect_version/js/Copy_Data_to_Textures.js:180` `function copyTSlocsToTexture(calc_constants, device, txTimeSeries_Locations) {`<br>변경 bb99fee 2026-07-02: `bb99fee:js/Copy_Data_to_Textures.js:137` `function copyBoundaryTimeSeriesDataToTexture(boundaryTimeSeriesSideData, device, txBoundaryTimeSeries) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/Copy_Data_to_Textures.js:135` `function copyTSlocsToTexture(calc_constants, device, txTimeSeries_Locations) {`<br>두 파일 이력: L02. | 대상은 경계 시계열 업로드와 위치 업로드이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 경계 관측점·시간·eta/hu/hv를 RGBA32F 텍스처로 패킹한다. transect 판은 이 자리에 측정점 위치 업로드를 둔다. 두 함수는 같은 함수의 이름 변경이 아니다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-058 | A 판 차이 | A 판 차이 | 현재 `js/Copy_Data_to_Textures.js:261` `var eta = 0.; // * Math.exp(-(dx * dx + dy * dy) / (2 * sigma * sigma));`<br>현재 `transect_version/js/Copy_Data_to_Textures.js:240` `let dx = x - calc_constants.WIDTH / 10.;`<br>변경 32be94a 2025-10-16: `32be94a:js/Copy_Data_to_Textures.js:198` `var eta = 0.; // * Math.exp(-(dx * dx + dy * dy) / (2 * sigma * sigma));`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/Copy_Data_to_Textures.js:194` `let dx = x - calc_constants.WIDTH / 10.;`<br>두 파일 이력: L02. | 대상은 초기 수면과 속도 채널이다. 본판의 32be94a 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 writeStateFlag 1/2/3으로 eta/u/v 입력을 구분한다. transect 판은 river_sim==1 또는 loadFriction==1에서만 첫 채널에 입력장을 쓴다. 나머지 두 운동량 채널은 0.0이다. 진폭 0.0인 가우스 식은 유한한 격자에서 0.0이다. 이 행의 판 차이 근거는 32be94a의 본판 변경이다. |
| CT1 §5 | CT1-059 | A 판 차이 | A 판 차이 | 현재 `js/Copy_Data_to_Textures.js:351` `function copySphericalMetricDataToTexture(calc_constants, device, txSphericalMetrics) {`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/Copy_Data_to_Textures.js:298` `function copySphericalMetricDataToTexture(calc_constants, device, txSphericalMetrics) {`<br>두 파일 이력: L02. | 대상은 구면 계량 업로드 없음이다. 본판의 afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 셀 중심 위도·북쪽 면·남쪽 면의 계량을 RGBA32F로 저장한다. transect 판에는 구면 격자 경로가 없다. 이 행의 판 차이 근거는 afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-062 | A 판 차이 | A 판 차이 | 현재 `index.html:120` `/* Added by Codex: Start compact boundary time-series upload controls. */`<br>변경 bb99fee 2026-07-02: `bb99fee:index.html:121` `.boundary-time-series-upload-row {`<br>현재 대응 `index.html:121` `.boundary-time-series-upload-row {`<br>두 파일 이력: L01. | 대상은 경계 파일 UI 스타일이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 경계 시계열 업로드 행의 CSS를 정의한다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-063 | A 판 차이 | A 판 차이 | 현재 `index.html:204` `<b>Questions/Problems/Requests </b> - use the <a href="https://celeris.discourse.group/categories" target="_blank" rel="noopener noreferrer">Users Forum</a>`<br>현재 `transect_version/index.html:191` `<b>Questions/Problems/Requests </b> - use the <a href="https://www.sqrtgh.com/forum" target="_blank" rel="noopener noreferrer">Users Forum</a>`<br>변경 794c808 2026-04-06: `794c808:index.html:191` `<b>Questions/Problems/Requests </b> - use the <a href="https://celeris.discourse.group/categories" target="_blank" rel="noopener noreferrer">Users Forum</a>`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/index.html:191` `<b>Questions/Problems/Requests </b> - use the <a href="https://www.sqrtgh.com/forum" target="_blank" rel="noopener noreferrer">Users Forum</a>`<br>두 파일 이력: L01. | 대상은 사용자 포럼 링크이다. 본판의 794c808 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 discourse 주소를 쓴다. transect 판은 sqrtgh 포럼 주소를 쓴다. 이 행의 판 차이 근거는 794c808의 본판 변경이다. |
| CT1 §5 | CT1-064 | A 판 차이 | A 판 차이 | 현재 `index.html:238` `<input type="file" id="etaInitialConditionFile" accept="application/txt" style="display: none;" />`<br>변경 32be94a 2025-10-16: `32be94a:index.html:225` `<input type="file" id="etaInitialConditionFile" accept="application/txt" style="display: none;" />`<br>변경 b8b50c3 2025-06-08: `b8b50c3:index.html:231` `<input type="file" id="hardbottomFile" accept="application/txt" style="display: none;" />`<br>현재 대응 `index.html:250` `<input type="file" id="hardbottomFile" accept="application/txt" style="display: none;" />`<br>변경 bb99fee 2026-07-02: `bb99fee:index.html:257` `<html4f>`<br>현재 대응 `index.html:257` `<html4f>`<br>두 파일 이력: L01. | 대상은 추가 입력 파일이다. 본판의 32be94a·b8b50c3·bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 초기 수면·hardbottom·4변 경계 시계열 업로드와 자료 형식 안내를 제공한다. 마찰 파일 입력은 양쪽에 남아 있다. 이 행의 판 차이 근거는 32be94a·b8b50c3·bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-066 | A 판 차이 | A 판 차이 | 현재 `index.html:337` `<option value="42">Sebastian Inlet (FL), wind waves</option>`<br>변경 ea93d70 2025-10-24: `ea93d70:index.html:298` `<option value="42">Sebastian Inlet (FL), wind waves</option>`<br>변경 afc1fe7 2026-06-19: `afc1fe7:index.html:303` `<option value="54">Japan tsunami, spherical coords</option>`<br>현재 대응 `index.html:342` `<option value="54">Japan tsunami, spherical coords</option>`<br>변경 8c2b62b 2025-08-24: `8c2b62b:index.html:300` `<option value="38">Tracy Arm (AK), tsunami</option>`<br>현재 대응 `index.html:347` `<option value="38">Tracy Arm (AK), tsunami</option>`<br>변경 146a4ac 2025-09-28: `146a4ac:index.html:301` `<option value="39">Tracy Arm (AK), hot start</option>`<br>현재 대응 `index.html:348` `<option value="39">Tracy Arm (AK), hot start</option>`<br>변경 32be94a 2025-10-16: `32be94a:index.html:310` `<option value="40">Portage Lake & River (AK), tsunami</option>`<br>현재 대응 `index.html:352` `<option value="40">Portage Lake & River (AK), tsunami</option>`<br>두 파일 이력: L01. | 대상은 예제 선택 항목이다. 본판의 ea93d70·afc1fe7·8c2b62b·146a4ac·32be94a 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판의 후속 예제 option이 transect 판에는 없다. 이 행의 판 차이 근거는 ea93d70·afc1fe7·8c2b62b·146a4ac·32be94a의 본판 변경이다. |
| CT1 §5 | CT1-068 | A 판 차이 | A 판 차이 | 현재 `index.html:423` `<option value="19">Sediment Class 1 Available Depth </option>`<br>변경 b8b50c3 2025-06-08: `b8b50c3:index.html:372` `<option value="19">Sediment Class 1 Available Depth </option>`<br>두 파일 이력: L01. | 대상은 가용 깊이 표시 항목이다. 본판의 b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 surfaceToPlot 19를 제공한다. 이 행의 판 차이 근거는 b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-069 | A 판 차이 | A 판 차이 | 현재 `index.html:628` `<label for="designcomponent_CrestElev-input">For linear structures (breakwaters, dunes, seawalls), crest elevation (m):</label>`<br>현재 `transect_version/index.html:558` `<label for="designcomponent_CrestElev-input">*For linear structures (breakwaters, dunes, seawalls), crest elevation (m):</label>`<br>변경 d778fe7 2026-06-02: `d778fe7:index.html:588` `<label for="designcomponent_CrestElev-input">For linear structures (breakwaters, dunes, seawalls), crest elevation (m):</label>`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/index.html:570` `<label for="designcomponent_CrestElev-input">*For linear structures (breakwaters, dunes, seawalls), crest elevation (m):</label>`<br>두 파일 이력: L01. | 대상은 천단고 UI 활성 상태이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 별표를 붙여 미지원임을 표시한다. 본판은 실제 선형 구조물 경로를 구현한다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-070 | A 판 차이 | A 판 차이 | 현재 `index.html:636` `<label for="designcomponent_CrestWidth-input">For linear structures (breakwaters, dunes, seawalls), crest width (m):</label>`<br>현재 `transect_version/index.html:566` `<label for="designcomponent_CrestWidth-input">*For linear structures (breakwaters, dunes, seawalls), crest width (m):</label>`<br>변경 d778fe7 2026-06-02: `d778fe7:index.html:596` `<label for="designcomponent_CrestWidth-input">For linear structures (breakwaters, dunes, seawalls), crest width (m):</label>`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/index.html:578` `<label for="designcomponent_CrestWidth-input">*For linear structures (breakwaters, dunes, seawalls), crest width (m):</label>`<br>두 파일 이력: L01. | 대상은 천단폭 UI 활성 상태이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 별표를 붙인다. 본판은 해당 폭을 실제 지형 편집에 쓴다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-071 | A 판 차이 | A 판 차이 | 현재 `index.html:644` `<label for="designcomponent_SideSlope-input">For linear, sloping structures (breakwaters, dunes), side slope (give as decimal, e.g. 0.25 = 1/4):</label>`<br>현재 `transect_version/index.html:574` `<label for="designcomponent_SideSlope-input">*For linear, sloping structures (breakwaters, dunes), side slope (give as decimal, e.g. 0.25 = 1/4):</label>`<br>변경 d778fe7 2026-06-02: `d778fe7:index.html:604` `<label for="designcomponent_SideSlope-input">For linear, sloping structures (breakwaters, dunes), side slope (give as decimal, e.g. 0.25 = 1/4):</label>`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/index.html:586` `<label for="designcomponent_SideSlope-input">*For linear, sloping structures (breakwaters, dunes), side slope (give as decimal, e.g. 0.25 = 1/4):</label>`<br>두 파일 이력: L01. | 대상은 사면경사 UI 활성 상태이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 별표를 붙인다. 두 판의 안내 예시 0.25=1/4는 같다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-072 | A 판 차이 | A 판 차이 | 현재 `index.html:652` `<label for="designcomponent_CurrentEndPoint-select">Choose Linear Structure Start/Endpoint Coordinate to Edit:</label>`<br>현재 `transect_version/index.html:582` `<label for="designcomponent_CurrentEndPoint-select">*Choose Linear Structure Start/Endpoint Coordinate to Edit:</label>`<br>변경 d778fe7 2026-06-02: `d778fe7:index.html:612` `<label for="designcomponent_CurrentEndPoint-select">Choose Linear Structure Start/Endpoint Coordinate to Edit:</label>`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/index.html:594` `<label for="designcomponent_CurrentEndPoint-select">*Choose Linear Structure Start/Endpoint Coordinate to Edit:</label>`<br>두 파일 이력: L01. | 대상은 끝점 선택 UI 활성 상태이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 별표를 붙인다. 본판은 끝점 선택을 실제 편집에 연결한다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-073 | A 판 차이 | A 판 차이 | 현재 `index.html:661` `Right-click on structure start/end location (in Design Mode) or input coordinates below</a>`<br>현재 `transect_version/index.html:591` `*Right-click on structure start/end location (in Design Mode) or input coordinates below</a>`<br>변경 d778fe7 2026-06-02: `d778fe7:index.html:621` `Right-click on structure start/end location (in Design Mode) or input coordinates below</a>`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/index.html:603` `*Right-click on structure start/end location (in Design Mode) or input coordinates below</a>`<br>두 파일 이력: L01. | 대상은 끝점 입력 안내이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 우클릭 입력 안내에 별표를 붙인다. 실제 선형 구조물 적용 경로는 없다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-074 | A 판 차이 | A 판 차이 | 현재 `index.html:764` `<option value="0">Sine Wave (single harmonic)</option>`<br>현재 `transect_version/index.html:694` `<option value="0">*Sine Wave (single harmonic)</option>`<br>변경 9093d7f 2026-06-01: `9093d7f:index.html:724` `<option value="0">Sine Wave (single harmonic)</option>`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/index.html:706` `<option value="0">*Sine Wave (single harmonic)</option>`<br>두 파일 이력: L01. | 대상은 내장 파 생성 UI이다. 본판의 9093d7f 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 Sine와 TMA에 별표를 붙인다. 본판은 공유 파 생성 모듈을 호출한다. pulse 안내의 4 waves 문자열은 양쪽에 남아 있다. 이 행의 판 차이 근거는 9093d7f의 본판 변경이다. |
| CT1 §5 | CT1-076 | A 판 차이 | A 판 차이 | 현재 `index.html:805` `<!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->`<br>변경 bb99fee 2026-07-02: `bb99fee:index.html:806` `<option value="5">Time Series from loaded file</option>`<br>현재 대응 `index.html:806` `<option value="5">Time Series from loaded file</option>`<br>두 파일 이력: L01. | 대상은 서쪽 type5 UI이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 파일 시계열 경계를 선택할 수 있다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-077 | A 판 차이 | A 판 차이 | 현재 `index.html:818` `<!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->`<br>변경 bb99fee 2026-07-02: `bb99fee:index.html:819` `<option value="5">Time Series from loaded file</option>`<br>현재 대응 `index.html:819` `<option value="5">Time Series from loaded file</option>`<br>두 파일 이력: L01. | 대상은 동쪽 type5 UI이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 파일 시계열 경계를 선택할 수 있다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-078 | A 판 차이 | A 판 차이 | 현재 `index.html:831` `<!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->`<br>변경 bb99fee 2026-07-02: `bb99fee:index.html:832` `<option value="5">Time Series from loaded file</option>`<br>현재 대응 `index.html:832` `<option value="5">Time Series from loaded file</option>`<br>두 파일 이력: L01. | 대상은 남쪽 type5 UI이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 파일 시계열 경계를 선택할 수 있다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-079 | A 판 차이 | A 판 차이 | 현재 `index.html:844` `<!-- Added by Codex: Boundary type 5 uses eta/hu/hv from a configured time-series file. -->`<br>변경 bb99fee 2026-07-02: `bb99fee:index.html:845` `<option value="5">Time Series from loaded file</option>`<br>현재 대응 `index.html:845` `<option value="5">Time Series from loaded file</option>`<br>두 파일 이력: L01. | 대상은 북쪽 type5 UI이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 파일 시계열 경계를 선택할 수 있다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-082 | A 판 차이 | A 판 차이 | 현재 `index.html:1314` `<!-- Added by Codex: Start nested-grid boundary time-series output controls. -->`<br>변경 bb99fee 2026-07-02: `bb99fee:index.html:1315` `<html4f> Nested Grid Boundary Time Series Output Options: </html4f>`<br>현재 대응 `index.html:1315` `<html4f> Nested Grid Boundary Time Series Output Options: </html4f>`<br>변경 c4be488 2026-07-13: `c4be488:index.html:1323` `<html4f>`<br>현재 대응 `index.html:1323` `<html4f>`<br>두 파일 이력: L01. | 대상은 중첩 경계 출력 UI이다. 본판의 bb99fee·c4be488 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 0기반 사각형 인덱스·기간·간격·eta 임계값·실행 버튼을 제공한다. 다중 사각형은 JSON으로 추가한다. 이 행의 판 차이 근거는 bb99fee·c4be488의 본판 변경이다. |
| CT1 §5 | CT1-084 | A 판 차이 | A 판 차이 | 현재 `js/File_Loader.js:86` `export async function loadInitCondSurface(InitCondContent, calc_constants) {`<br>변경 32be94a 2025-10-16: `32be94a:js/File_Loader.js:86` `export async function loadInitCondSurface(InitCondContent, calc_constants) {`<br>두 파일 이력: L03. | 대상은 초기 수면 파일 읽기이다. 본판의 32be94a 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 etaInitCond.txt를 WIDTH열·HEIGHT행의 유한 수치장으로 읽는다. transect 판에는 이 함수가 없다. 이 행의 판 차이 근거는 32be94a의 본판 변경이다. |
| CT1 §5 | CT1-086 | A 판 차이 | A 판 차이 | 현재 `js/File_Loader.js:304` `function createEmptyBoundaryTimeSeriesSide() {`<br>변경 bb99fee 2026-07-02: `bb99fee:js/File_Loader.js:304` `function createEmptyBoundaryTimeSeriesSide() {`<br>두 파일 이력: L03. | 대상은 type-5 경계 자료 검사이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 주석 제거·관측점 수·좌표 정렬·중복 검사·1+3*N 열 검사·시간 단조증가·공유 시간벡터 오차 검사·업로드 우선을 구현한다. transect 판에는 해당 경계 자료 경로가 없다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-093 | A 판 차이 | A 판 차이 | 현재 `js/File_Writer.js:531` `export async function writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities, buffer) {`<br>현재 `transect_version/js/File_Writer.js:553` `export async function writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities) {`<br>변경 09cfd76 2026-02-15: `09cfd76:js/File_Writer.js:531` `export async function writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities, buffer) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/File_Writer.js:553` `export async function writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities) {`<br>두 파일 이력: L04. | 대상은 표면 출력 함수 인자이다. 본판의 09cfd76 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 공용 readback 버퍼를 전달한다. transect 판은 호출 안에서 버퍼를 만든다. bathytopo.bin의 채널 3과 첫 프레임 조건은 같다. 이 행의 판 차이 근거는 09cfd76의 본판 변경이다. |
| CT1 §5 | CT1-094 | A 판 차이 | A 판 차이 | 현재 `js/File_Writer.js:553` `if(calc_constants.useSedTransModel ==1 \|\| (total_time < 300.0 && calc_constants.disturbanceType == 5)){  // write depth if using sediment transport model or landslide`<br>현재 `transect_version/js/File_Writer.js:577` `await downloadTextureData(device, txState, 1, filename);  // number is the channel 1 = .r, 2 = .g, etc.`<br>변경 9ed86a6 2026-02-17: `9ed86a6:js/File_Writer.js:553` `if(calc_constants.useSedTransModel ==1 \|\| (total_time < 300.0 && calc_constants.disturbanceType == 5)){  // write depth if using sediment transport model or landslide`<br>변경 d852a23 2025-06-11: `d852a23:js/File_Writer.js:576` ``let filename = `depth_${frame_count_output}.bin`;``<br>현재 대응 `js/File_Writer.js:554` ``let filename = `depth_${frame_count_output}.bin`;``<br>변경 09cfd76 2026-02-15: `09cfd76:js/File_Writer.js:555` `await downloadTextureData(device, txBottom, 3, filename, buffer);  // number is the channel 1 = .r, 2 = .g, etc.`<br>현재 대응 `js/File_Writer.js:555` `await downloadTextureData(device, txBottom, 3, filename, buffer);  // number is the channel 1 = .r, 2 = .g, etc.`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/File_Writer.js:577` `await downloadTextureData(device, txState, 1, filename);  // number is the channel 1 = .r, 2 = .g, etc.`<br>두 파일 이력: L04. | 대상은 시간별 바닥고 출력과 표면 자료이다. 본판의 9ed86a6·d852a23·09cfd76 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 퇴적물 또는 total_time<300.0인 disturbanceType==5에서 depth_번호.bin을 출력한다. transect 판은 이 조건부 바닥고 출력을 하지 않는다. eta/P/Q/u/v/turb의 채널 번호·파일명·대기 순서는 같다. 이 행의 판 차이 근거는 9ed86a6·d852a23·09cfd76의 본판 변경이다. |
| CT1 §5 | CT1-095 | A 판 차이 | A 판 차이 | 현재 `js/File_Writer.js:599` `export async function downloadTextureData(device, texture, channel, filename, buffer) {`<br>현재 `transect_version/js/File_Writer.js:615` `export async function downloadTextureData(device, texture, channel, filename) {`<br>변경 09cfd76 2026-02-15: `09cfd76:js/File_Writer.js:599` `export async function downloadTextureData(device, texture, channel, filename, buffer) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/File_Writer.js:615` `export async function downloadTextureData(device, texture, channel, filename) {`<br>두 파일 이력: L04. | 대상은 바이너리 다운로드 인자이다. 본판의 09cfd76 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 readTextureData에 공용 버퍼를 전달한다. transect 판은 전달하지 않는다. Blob은 모두 application/octet-stream이다. 이 행의 판 차이 근거는 09cfd76의 본판 변경이다. |
| CT1 §5 | CT1-096 | A 판 차이 | A 판 차이 | 현재 `js/File_Writer.js:637` `async function readRgbaTextureData(device, src_texture, width, height) {`<br>변경 bb99fee 2026-07-02: `bb99fee:js/File_Writer.js:637` `async function readRgbaTextureData(device, src_texture, width, height) {`<br>변경 c4be488 2026-07-13: `c4be488:js/File_Writer.js:689` `function findNestedGridThresholdStartIndex(sideReadbacks, capturedTimes, thresholdOverride = null) {`<br>현재 대응 `js/File_Writer.js:689` `function findNestedGridThresholdStartIndex(sideReadbacks, capturedTimes, thresholdOverride = null) {`<br>두 파일 이력: L04. | 대상은 중첩 경계 출력 없음이다. 본판의 bb99fee·c4be488 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 4변 eta/hu/hv를 9자리 유효숫자로 저장한다. 본판은 임계 eta 이전 행을 잘라내도 절대 시간을 유지한다. 본판은 사각형별 파일 접두어와 임계값을 사용한다. transect 판에는 이 writer가 없다. 이 행의 판 차이 근거는 bb99fee·c4be488의 본판 변경이다. |
| CT1 §5 | CT1-101 | A 판 차이 | A 판 차이 | 현재 `js/Handler_CalcMeans.js:125` `binding: 13,`<br>현재 `transect_version/js/Handler_CalcMeans.js:127` `export function create_CalcMeans_BindGroup(device, uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC) {`<br>변경 dc6cc2d 2025-08-10: `dc6cc2d:js/Handler_CalcMeans.js:125` `binding: 13,`<br>`dc6cc2d:js/Handler_CalcMeans.js:126` `visibility: GPUShaderStage.COMPUTE,`<br>`dc6cc2d:js/Handler_CalcMeans.js:127` `texture: {`<br>`dc6cc2d:js/Handler_CalcMeans.js:128` `sampleType: 'unfilterable-float',`<br>`dc6cc2d:js/Handler_CalcMeans.js:129` `format: 'rgba32float'`<br>`dc6cc2d:js/Handler_CalcMeans.js:130` `}`<br>현재 대응 `js/Handler_CalcMeans.js:129` `format: 'rgba32float'`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/Handler_CalcMeans.js:127` `export function create_CalcMeans_BindGroup(device, uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC) {`<br>두 파일 이력: L05. | 대상은 통계용 실제 수면 입력이다. 본판의 dc6cc2d 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 binding 13의 txNewState를 추가했다. transect 판은 재구성 수심 평균으로 수면을 산출한다. 이는 평균·최대 eta의 자료원이 다른 차이다. 이 행의 판 차이 근거는 dc6cc2d의 본판 변경이다. |
| CT1 §5 | CT1-102 | A 판 차이 | A 판 차이 | 현재 `js/Handler_CalcMeans.js:195` `binding: 13,`<br>변경 dc6cc2d 2025-08-10: `dc6cc2d:js/Handler_CalcMeans.js:196` `resource: txNewState.createView()`<br>현재 대응 `js/Handler_CalcMeans.js:196` `resource: txNewState.createView()`<br>두 파일 이력: L05. | 대상은 통계 바인드 그룹이다. 본판의 dc6cc2d 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판에는 txNewState.createView()가 없다. 대응 CalcMeans 셰이더의 eta 산출식과 일치한다. 이 행의 판 차이 근거는 dc6cc2d의 본판 변경이다. |
| CT1 §5 | CT1-103 | A 판 차이 | A 판 차이 | 현재 `js/Handler_Copytxf32_txf16.js:78` `binding: 8,`<br>현재 `transect_version/js/Handler_Copytxf32_txf16.js:81` `export function create_Copytxf32_txf16_BindGroup(device, uniformBuffer, txNewState, txBottom, txMeans_Speed, txRenderVarsf16, txMeans_Momflux, txModelVelocities, txMeans) {`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/Handler_Copytxf32_txf16.js:78` `binding: 8,`<br>`b8b50c3:js/Handler_Copytxf32_txf16.js:79` `visibility: GPUShaderStage.COMPUTE,`<br>`b8b50c3:js/Handler_Copytxf32_txf16.js:80` `texture: {`<br>`b8b50c3:js/Handler_Copytxf32_txf16.js:81` `sampleType: 'unfilterable-float',`<br>`b8b50c3:js/Handler_Copytxf32_txf16.js:82` `format: 'rgba32float'`<br>`b8b50c3:js/Handler_Copytxf32_txf16.js:83` `}`<br>현재 대응 `js/Handler_Copytxf32_txf16.js:82` `format: 'rgba32float'`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/Handler_Copytxf32_txf16.js:81` `export function create_Copytxf32_txf16_BindGroup(device, uniformBuffer, txNewState, txBottom, txMeans_Speed, txRenderVarsf16, txMeans_Momflux, txModelVelocities, txMeans) {`<br>두 파일 이력: L06. | 대상은 불투수 바닥 표시 입력이다. 본판의 b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 binding 8의 txHardBottom을 제공한다. transect 판은 표시용 텍스처를 두 레이어만 쓴다. 이 행의 판 차이 근거는 b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-104 | A 판 차이 | A 판 차이 | 현재 `js/Handler_Copytxf32_txf16.js:129` `binding: 8,`<br>현재 `transect_version/js/Handler_Copytxf32_txf16.js:121` `}`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/Handler_Copytxf32_txf16.js:130` `resource: txHardBottom.createView()`<br>현재 대응 `js/Handler_Copytxf32_txf16.js:130` `resource: txHardBottom.createView()`<br>두 파일 이력: L06. | 대상은 불투수 바닥 리소스이다. 본판의 b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판에는 txHardBottom.createView()가 없다. 본판의 가용 퇴적층 깊이 표시와 연결된다. 이 행의 판 차이 근거는 b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-105 | A 판 차이 | A 판 차이 | 현재 `js/Handler_ExtractTimeSeries.js:77` `binding: 8,`<br>현재 `transect_version/js/Handler_ExtractTimeSeries.js:80` `export function create_ExtractTimeSeries_BindGroup(device, uniformBuffer, txBottom, txBottomFriction, txContSource, txState, txWaveHeight, txTimeSeries_Locations, txTimeSeries_Data) {`<br>변경 397c575 2025-09-09: `397c575:js/Handler_ExtractTimeSeries.js:77` `binding: 8,`<br>`397c575:js/Handler_ExtractTimeSeries.js:78` `visibility: GPUShaderStage.COMPUTE,`<br>`397c575:js/Handler_ExtractTimeSeries.js:79` `texture: {`<br>`397c575:js/Handler_ExtractTimeSeries.js:80` `sampleType: 'unfilterable-float',`<br>`397c575:js/Handler_ExtractTimeSeries.js:81` `format: 'rgba32float'`<br>`397c575:js/Handler_ExtractTimeSeries.js:82` `}`<br>현재 대응 `js/Handler_ExtractTimeSeries.js:81` `format: 'rgba32float'`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/Handler_ExtractTimeSeries.js:80` `export function create_ExtractTimeSeries_BindGroup(device, uniformBuffer, txBottom, txBottomFriction, txContSource, txState, txWaveHeight, txTimeSeries_Locations, txTimeSeries_Data) {`<br>두 파일 이력: L08. | 대상은 툴팁 최대 수면 입력이다. 본판의 397c575 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 binding 8의 txMeans_Speed를 제공한다. transect 판은 항상 유의파고 자료를 툴팁에 쓴다. 이 행의 판 차이 근거는 397c575의 본판 변경이다. |
| CT1 §5 | CT1-106 | A 판 차이 | A 판 차이 | 현재 `js/Handler_ExtractTimeSeries.js:128` `binding: 8,`<br>변경 397c575 2025-09-09: `397c575:js/Handler_ExtractTimeSeries.js:129` `resource: txMeans_Speed.createView()`<br>현재 대응 `js/Handler_ExtractTimeSeries.js:129` `resource: txMeans_Speed.createView()`<br>두 파일 이력: L08. | 대상은 최대 수면 리소스이다. 본판의 397c575 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판에는 txMeans_Speed.createView()가 없다. 점 시계열 eta/P/Q의 자료원 변경을 뜻하지 않는다. 이 행의 판 차이 근거는 397c575의 본판 변경이다. |
| CT1 §5 | CT1-107 | A 판 차이 | A 판 차이 | 현재 `js/Handler_Pass2.js:144` `binding: 15,`<br>현재 `transect_version/js/Handler_Pass2.js:147` `export function create_Pass2_BindGroup(device, uniformBuffer,txH, txU, txV, txBottom, txC, txHnear, txXFlux, txYFlux, txSed_C1, txSed_C2, txSed_C3, txSed_C4, txXFlux_Sed, txYFlux_Sed) {`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/Handler_Pass2.js:144` `binding: 15,`<br>`b8b50c3:js/Handler_Pass2.js:145` `visibility: GPUShaderStage.COMPUTE,`<br>`b8b50c3:js/Handler_Pass2.js:146` `texture: {`<br>`b8b50c3:js/Handler_Pass2.js:147` `sampleType: 'unfilterable-float',`<br>`b8b50c3:js/Handler_Pass2.js:148` `format: 'rgba32float'`<br>`b8b50c3:js/Handler_Pass2.js:149` `}`<br>현재 대응 `js/Handler_Pass2.js:148` `format: 'rgba32float'`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/Handler_Pass2.js:147` `export function create_Pass2_BindGroup(device, uniformBuffer,txH, txU, txV, txBottom, txC, txHnear, txXFlux, txYFlux, txSed_C1, txSed_C2, txSed_C3, txSed_C4, txXFlux_Sed, txYFlux_Sed) {`<br>두 파일 이력: L09. | 대상은 퇴적물 확산 입력이다. 본판의 b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 binding 15로 txBreaking을 읽어 쇄파 점성 기반 확산계수를 만든다. transect 판의 Pass2에는 해당 리소스가 없다. 이 행의 판 차이 근거는 b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-108 | A 판 차이 | A 판 차이 | 현재 `js/Handler_Pass2.js:223` `binding: 15,`<br>현재 `transect_version/js/Handler_Pass2.js:215` `}`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/Handler_Pass2.js:224` `resource: txBreaking.createView()`<br>현재 대응 `js/Handler_Pass2.js:224` `resource: txBreaking.createView()`<br>두 파일 이력: L09. | 대상은 Pass2 바인드 그룹이다. 본판의 b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판의 txBreaking.createView()가 transect 판에는 없다. 농도 flux의 확산항 차이와 연결된다. 이 행의 판 차이 근거는 b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-109 | A 판 차이 | A 판 차이 | 현재 `js/Handler_Render.js:317` `19: "Sediment Class 1 Available Depth (m)",`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/Handler_Render.js:317` `19: "Sediment Class 1 Available Depth (m)",`<br>두 파일 이력: L10. | 대상은 가용 퇴적층 깊이 범례이다. 본판의 b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 surfaceToPlot==19의 가용 깊이 범례를 제공한다. transect 판에는 해당 표시 경로가 없다. 이 행의 판 차이 근거는 b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-110 | A 판 차이 | A 판 차이 | 현재 `js/Handler_SedTrans_Pass3.js:126` `binding: 13,`<br>현재 `transect_version/js/Handler_SedTrans_Pass3.js:129` `export function create_SedTrans_Pass3_BindGroup(device, uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed) {`<br>변경 22e1983 2025-06-06: `22e1983:js/Handler_SedTrans_Pass3.js:126` `binding: 13,`<br>`22e1983:js/Handler_SedTrans_Pass3.js:127` `visibility: GPUShaderStage.COMPUTE,`<br>`22e1983:js/Handler_SedTrans_Pass3.js:128` `texture: {`<br>`22e1983:js/Handler_SedTrans_Pass3.js:129` `sampleType: 'unfilterable-float',`<br>`22e1983:js/Handler_SedTrans_Pass3.js:130` `format: 'rgba32float'`<br>`22e1983:js/Handler_SedTrans_Pass3.js:131` `}`<br>현재 대응 `js/Handler_SedTrans_Pass3.js:130` `format: 'rgba32float'`<br>변경 2a7452d 2025-06-07: `2a7452d:js/Handler_SedTrans_Pass3.js:153` `binding: 16,`<br>`2a7452d:js/Handler_SedTrans_Pass3.js:154` `visibility: GPUShaderStage.COMPUTE,`<br>`2a7452d:js/Handler_SedTrans_Pass3.js:155` `texture: {`<br>`2a7452d:js/Handler_SedTrans_Pass3.js:156` `sampleType: 'unfilterable-float',`<br>`2a7452d:js/Handler_SedTrans_Pass3.js:157` `format: 'rgba32float'`<br>`2a7452d:js/Handler_SedTrans_Pass3.js:158` `}`<br>현재 대응 `js/Handler_SedTrans_Pass3.js:157` `format: 'rgba32float'`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/Handler_SedTrans_Pass3.js:162` `binding: 17,`<br>`b8b50c3:js/Handler_SedTrans_Pass3.js:163` `visibility: GPUShaderStage.COMPUTE,`<br>`b8b50c3:js/Handler_SedTrans_Pass3.js:164` `texture: {`<br>`b8b50c3:js/Handler_SedTrans_Pass3.js:165` `sampleType: 'unfilterable-float',`<br>`b8b50c3:js/Handler_SedTrans_Pass3.js:166` `format: 'rgba32float'`<br>`b8b50c3:js/Handler_SedTrans_Pass3.js:167` `}`<br>현재 대응 `js/Handler_SedTrans_Pass3.js:166` `format: 'rgba32float'`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/Handler_SedTrans_Pass3.js:129` `export function create_SedTrans_Pass3_BindGroup(device, uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed) {`<br>두 파일 이력: L11. | 대상은 퇴적물 적분 리소스 확장이다. 본판의 22e1983·2a7452d·b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 binding 13–17로 쇄파·면속도·면농도·hardbottom을 받는다. transect 판은 셀 운동량과 고정 확산계수를 쓴다. 이 행의 판 차이 근거는 22e1983·2a7452d·b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-111 | A 판 차이 | A 판 차이 | 현재 `js/Handler_SedTrans_Pass3.js:233` `binding: 13,`<br>현재 `transect_version/js/Handler_SedTrans_Pass3.js:189` `}`<br>변경 22e1983 2025-06-06: `22e1983:js/Handler_SedTrans_Pass3.js:216` `resource: txBreaking.createView()`<br>현재 대응 `js/Handler_SedTrans_Pass3.js:234` `resource: txBreaking.createView()`<br>변경 2a7452d 2025-06-07: `2a7452d:js/Handler_SedTrans_Pass3.js:237` `resource: txSed_C1.createView()`<br>현재 대응 `js/Handler_SedTrans_Pass3.js:246` `resource: txSed_C1.createView()`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/Handler_SedTrans_Pass3.js:250` `resource: txHardBottom.createView()`<br>현재 대응 `js/Handler_SedTrans_Pass3.js:250` `resource: txHardBottom.createView()`<br>두 파일 이력: L11. | 대상은 퇴적물 바인드 그룹이다. 본판의 22e1983·2a7452d·b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 13–17의 리소스 view를 제공하지 않는다. 본판의 bedload와 침식 가능 깊이 검사에 필요한 자료가 빠진다. 이 행의 판 차이 근거는 22e1983·2a7452d·b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-112 | A 판 차이 | A 판 차이 | 현재 `js/Handler_SedTrans_UpdateBottom.js:70` `binding: 7,`<br>현재 `transect_version/js/Handler_SedTrans_UpdateBottom.js:73` `export function create_SedTrans_UpdateBottom_BindGroup(device, uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change) {`<br>변경 852ec28 2025-06-13: `852ec28:js/Handler_SedTrans_UpdateBottom.js:70` `binding: 7,`<br>`852ec28:js/Handler_SedTrans_UpdateBottom.js:71` `visibility: GPUShaderStage.COMPUTE,`<br>`852ec28:js/Handler_SedTrans_UpdateBottom.js:72` `texture: {`<br>`852ec28:js/Handler_SedTrans_UpdateBottom.js:73` `sampleType: 'unfilterable-float',`<br>`852ec28:js/Handler_SedTrans_UpdateBottom.js:74` `format: 'rgba32float'`<br>`852ec28:js/Handler_SedTrans_UpdateBottom.js:75` `}`<br>현재 대응 `js/Handler_SedTrans_UpdateBottom.js:74` `format: 'rgba32float'`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/Handler_SedTrans_UpdateBottom.js:73` `export function create_SedTrans_UpdateBottom_BindGroup(device, uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change) {`<br>두 파일 이력: L12. | 대상은 바닥 갱신 입력이다. 본판의 852ec28 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 hardbottom과 초기 바닥고를 받는다. transect 판은 가상 누적 변화량을 별도로 적산한다. 이 행의 판 차이 근거는 852ec28의 본판 변경이다. |
| CT1 §5 | CT1-113 | A 판 차이 | A 판 차이 | 현재 `js/Handler_SedTrans_UpdateBottom.js:126` `binding: 7,`<br>변경 852ec28 2025-06-13: `852ec28:js/Handler_SedTrans_UpdateBottom.js:127` `resource: txHardBottom.createView()`<br>현재 대응 `js/Handler_SedTrans_UpdateBottom.js:127` `resource: txHardBottom.createView()`<br>두 파일 이력: L12. | 대상은 바닥 갱신 리소스이다. 본판의 852ec28 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판에는 binding 7과 8의 view가 없다. 본판 누적 변화량은 현재 바닥고에서 초기 바닥고를 뺀 값이다. 이 행의 판 차이 근거는 852ec28의 본판 변경이다. |
| CT1 §5 | CT1-116 | A 판 차이 | A 판 차이 | 현재 `js/Run_Compute_Shader.js:55` `export function runComputeShader_EncStack(device, commandEncoder, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {`<br>변경 3646fc8 2026-02-08: `3646fc8:js/Run_Compute_Shader.js:55` `export function runComputeShader_EncStack(device, commandEncoder, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {`<br>두 파일 이력: L13. | 대상은 누적 명령 encoder 없음이다. 본판의 3646fc8 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 EncStack 함수를 export한다. transect 판은 각 계산과 복사마다 submit한다. 수치 연산을 제거한 차이는 아니다. 이 행의 판 차이 근거는 3646fc8의 본판 변경이다. |
| CT1 §5 | CT1-117 | A 판 차이 | A 판 차이 | 현재 `js/Run_Tridiag_Solver.js:22` `TridiagX_BindGroup_BaseToA,`<br>현재 `transect_version/js/Run_Tridiag_Solver.js:32` `runCopyTextures(device, commandEncoder, calc_constants, current_stateUVstar, txNewState)`<br>변경 984091f 2026-05-24: `984091f:js/Run_Tridiag_Solver.js:22` `TridiagX_BindGroup_BaseToA,`<br>변경 33f7ff6 2026-02-13: `33f7ff6:js/Run_Tridiag_Solver.js:32` `runCopyTextures(device, calc_constants, current_stateUVstar, txNewState)`<br>현재 대응 `js/Run_Tridiag_Solver.js:38` `runCopyTextures(device, calc_constants, current_stateUVstar, txNewState)`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/Run_Tridiag_Solver.js:32` `runCopyTextures(device, commandEncoder, calc_constants, current_stateUVstar, txNewState)`<br>두 파일 이력: L14. | 대상은 PCR 바인드 그룹 인자이다. 본판의 984091f·33f7ff6 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 계수 텍스처 두 개를 번갈아 읽는 바인드 그룹을 추가한다. transect 판은 매 반복 뒤 계수를 복사한다. NLSW 우회 복사의 범위는 같다. 이 행의 판 차이 근거는 984091f·33f7ff6의 본판 변경이다. |
| CT1 §5 | CT1-121 | A 판 차이 | A 판 차이 | 현재 `js/Time_Series.js:60` `export async function readToolTipTextureData(device, texture, frame_count_time_series, timeSeriesDataEpoch = calc_constants.timeSeriesDataEpoch) {`<br>현재 `transect_version/js/Time_Series.js:57` `export async function readToolTipTextureData(device, texture, frame_count_time_series) {`<br>변경 ebca435 2026-07-20: `ebca435:js/Time_Series.js:60` `export async function readToolTipTextureData(device, texture, frame_count_time_series, timeSeriesDataEpoch = calc_constants.timeSeriesDataEpoch) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/Time_Series.js:57` `export async function readToolTipTextureData(device, texture, frame_count_time_series) {`<br>두 파일 이력: L15. | 대상은 시계열 epoch 인자이다. 본판의 ebca435 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 요청 시작 시의 epoch를 받는다. transect 판에는 비동기 초기화 경합을 구분하는 인자가 없다. 이 행의 판 차이 근거는 ebca435의 본판 변경이다. |
| CT1 §5 | CT1-124 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:16` `algochanges: 0, // set to 1 to test alternative algorithm for various parts of the code`<br>변경 896c491 2026-01-17: `896c491:js/constants_load_calc.js:16` `algochanges: 0, // set to 1 to test alternative algorithm for various parts of the code`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/constants_load_calc.js:20` `grid_type: 1, // right now spherical when =2, otherwise cartesian`<br>현재 대응 `js/constants_load_calc.js:20` `grid_type: 1, // right now spherical when =2, otherwise cartesian`<br>두 파일 이력: L18. | 대상은 기본 격자 유형과 디버그 옵션이다. 본판의 896c491·afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 algochanges=0과 grid_type=1을 정의한다. transect 판은 Cartesian x 단면 계산을 쓴다. 이 행의 판 차이 근거는 896c491·afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-125 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:48` `vort_friction_factor: 0.0, // coefficient for vorticity-based momentum mixing/dissipation`<br>변경 5a5603f 2026-01-15: `5a5603f:js/constants_load_calc.js:41` `vort_friction_factor: 0.0, // coefficient for vorticity-based momentum mixing/dissipation`<br>변경 32be94a 2025-10-16: `32be94a:js/constants_load_calc.js:42` `loadetaIC: 0,  // Load initial free surface from file when == 1`<br>현재 대응 `js/constants_load_calc.js:50` `loadetaIC: 0,  // Load initial free surface from file when == 1`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/constants_load_calc.js:53` `R_earth: 6371000.0,  // radius of earth, only used for spherical coordinate system`<br>현재 대응 `js/constants_load_calc.js:53` `R_earth: 6371000.0,  // radius of earth, only used for spherical coordinate system`<br>두 파일 이력: L18. | 대상은 마찰·초기 수면·지구 반지름 기본값이다. 본판의 5a5603f·32be94a·afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 vort_friction_factor=0.0·loadetaIC=0·R_earth=6371000.0을 정의한다. 이 행의 판 차이 근거는 5a5603f·32be94a·afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-127 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:112` `sedTurbDispersion: 0.01, // eddy viscosity constant (background) value for sediment transport`<br>변경 3be651a 2025-06-11: `3be651a:js/constants_load_calc.js:86` `sedTurbDispersion: 0.01, // eddy viscosity constant (background) value for sediment transport`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/constants_load_calc.js:88` `loadHardBottom: 0, // load hard bottom from file when == 1`<br>현재 대응 `js/constants_load_calc.js:114` `loadHardBottom: 0, // load hard bottom from file when == 1`<br>두 파일 이력: L18. | 대상은 퇴적물 확장 기본값이다. 본판의 3be651a·b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 sedTurbDispersion=0.01·sedBreakingDispersionCoef=0.1·loadHardBottom=0을 정의한다. 이 행의 판 차이 근거는 3be651a·b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-128 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:197` `"./examples/Hermosa_Beach_CA_COULWAVE/",`<br>현재 `transect_version/js/constants_load_calc.js:168` `"./examples/Hermosa_Beach_CA_COULWAVE/"`<br>변경 853c27d 2025-08-11: `853c27d:js/constants_load_calc.js:171` `"./examples/Hermosa_Beach_CA_COULWAVE/",`<br>변경 146a4ac 2025-09-28: `146a4ac:js/constants_load_calc.js:172` `"./examples/Endicott_slide/",`<br>현재 대응 `js/constants_load_calc.js:198` `"./examples/Endicott_slide/",`<br>변경 32be94a 2025-10-16: `32be94a:js/constants_load_calc.js:174` `"./examples/TracyArm_hotstart/",`<br>현재 대응 `js/constants_load_calc.js:199` `"./examples/TracyArm_hotstart/",`<br>변경 ea93d70 2025-10-24: `ea93d70:js/constants_load_calc.js:175` `"./examples/Portage_Lake_AK_rotated/",`<br>현재 대응 `js/constants_load_calc.js:200` `"./examples/Portage_Lake_AK_rotated/",`<br>변경 2e46d86 2026-04-20: `2e46d86:js/constants_load_calc.js:181` `"./examples/Sebastian_Inlet_FL/",`<br>현재 대응 `js/constants_load_calc.js:202` `"./examples/Sebastian_Inlet_FL/",`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/constants_load_calc.js:198` `"./examples/MC_PyramidRock_H2_T15_Normal/",`<br>현재 대응 `js/constants_load_calc.js:213` `"./examples/MC_PyramidRock_H2_T15_Normal/",`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/constants_load_calc.js:168` `"./examples/Hermosa_Beach_CA_COULWAVE/"`<br>transect 3d8a61b 2025-06-14: `3d8a61b:transect_version/js/constants_load_calc.js:168` `"./examples/Hermosa_Beach_CA_COULWAVE/"`<br>두 파일 이력: L18. | 대상은 예제 목록과 기본 색상이다. 본판의 853c27d·146a4ac·32be94a·ea93d70·2e46d86·afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판의 예제 목록은 Hermosa_Beach_CA_COULWAVE에서 끝난다. 기본 colorMap_choice는 본판 0이고 transect 2다. 이 행의 판 차이 근거는 853c27d·146a4ac·32be94a·ea93d70·2e46d86·afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-129 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:259` `timeSeriesChartStartTime: 0.0, // current point-series chart-window start, zero normally and absolute time for nested runs`<br>변경 ebca435 2026-07-20: `ebca435:js/constants_load_calc.js:259` `timeSeriesChartStartTime: 0.0, // current point-series chart-window start, zero normally and absolute time for nested runs`<br>두 파일 이력: L18. | 대상은 점 시계열 초기화 상태이다. 본판의 ebca435 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 timeSeriesChartStartTime과 timeSeriesDataEpoch를 0으로 정의한다. 이 행의 판 차이 근거는 ebca435의 본판 변경이다. |
| CT1 §5 | CT1-130 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:309` `cameraInit_user: 0, // flag to indicate user has initialized camera position`<br>변경 f183cc2 2026-02-01: `f183cc2:js/constants_load_calc.js:272` `cameraInit_user: 0, // flag to indicate user has initialized camera position`<br>두 파일 이력: L18. | 대상은 사용자 초기 카메라이다. 본판의 f183cc2 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 초기 카메라 위치·yaw·pitch와 활성 플래그를 정의한다. 이 행의 판 차이 근거는 f183cc2의 본판 변경이다. |
| CT1 §5 | CT1-131 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:330` `designcomponent_CrestElev: 0.0, // crest elevation for linear structures`<br>변경 d778fe7 2026-06-02: `d778fe7:js/constants_load_calc.js:304` `designcomponent_CrestElev: 0.0, // crest elevation for linear structures`<br>두 파일 이력: L18. | 대상은 선형 구조물 상태이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 천단고 0·천단폭 1·사면경사 0.25·끝점 좌표·미리보기·적용 플래그를 정의한다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-132 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:374` `nestedGridOutput_i0: 0, // lower-left rectangle i-index for nested boundary output`<br>변경 bb99fee 2026-07-02: `bb99fee:js/constants_load_calc.js:370` `nestedGridOutput_i0: 0, // lower-left rectangle i-index for nested boundary output`<br>변경 c4be488 2026-07-13: `c4be488:js/constants_load_calc.js:384` `nestedGridOutput_rectangles: [],`<br>현재 대응 `js/constants_load_calc.js:388` `nestedGridOutput_rectangles: [],`<br>두 파일 이력: L18. | 대상은 중첩 격자 출력 설정이다. 본판의 bb99fee·c4be488 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 사각형 인덱스·기간·간격·최대 8192 표본·트리거·접두어·사각형 배열·eta 임계값·시작시각을 정의한다. 이 행의 판 차이 근거는 bb99fee·c4be488의 본판 변경이다. |
| CT1 §5 | CT1-133 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:454` `if (calc_constants.grid_type == 2) {`<br>현재 `transect_version/js/constants_load_calc.js:358` `calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/constants_load_calc.js:413` `if (calc_constants.grid_type == 2) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/constants_load_calc.js:358` `calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);`<br>두 파일 이력: L18. | 대상은 구면 시간 간격과 강제 모드이다. 본판의 afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 구면에서 NLSW와 2차 재구성을 강제한다. 본판은 퇴적물과 쇄파를 끈다. 본판은 위도별 물리 격자간격의 최소값으로 dt를 정한다. Cartesian 식은 두 판에서 같다. 이 행의 판 차이 근거는 afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-136 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:544` `"./examples/Pacifica_CA/",`<br>현재 `transect_version/js/constants_load_calc.js:414` `"./examples/Pacifica_CA/",`<br>변경 2e46d86 2026-04-20: `2e46d86:js/constants_load_calc.js:444` `"./examples/Pacifica_CA/",`<br>변경 853c27d 2025-08-11: `853c27d:js/constants_load_calc.js:426` `"./examples/Hermosa_Beach_CA_COULWAVE/",`<br>현재 대응 `js/constants_load_calc.js:552` `"./examples/Hermosa_Beach_CA_COULWAVE/",`<br>변경 146a4ac 2025-09-28: `146a4ac:js/constants_load_calc.js:428` `"./examples/Endicott_slide/",`<br>현재 대응 `js/constants_load_calc.js:553` `"./examples/Endicott_slide/",`<br>변경 32be94a 2025-10-16: `32be94a:js/constants_load_calc.js:431` `"./examples/TracyArm_hotstart/",`<br>현재 대응 `js/constants_load_calc.js:554` `"./examples/TracyArm_hotstart/",`<br>변경 ea93d70 2025-10-24: `ea93d70:js/constants_load_calc.js:435` `"./examples/Yakutat_slide/",`<br>현재 대응 `js/constants_load_calc.js:556` `"./examples/Yakutat_slide/",`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/constants_load_calc.js:527` `"./examples/MC_PyramidRock_H2_T15_Normal/",`<br>현재 대응 `js/constants_load_calc.js:568` `"./examples/MC_PyramidRock_H2_T15_Normal/",`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/constants_load_calc.js:414` `"./examples/Pacifica_CA/",`<br>두 파일 이력: L18. | 대상은 초기화 함수 안 예제 목록이다. 본판의 2e46d86·853c27d·146a4ac·32be94a·ea93d70·afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 목록을 Hermosa_Beach_CA_COULWAVE까지 재정의한다. 본판은 뒤에 추가한 예제 경로를 유지한다. //30 같은 번호 주석 차이는 동작을 바꾸지 않는다. 이 행의 판 차이 근거는 2e46d86·853c27d·146a4ac·32be94a·ea93d70·afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-137 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:578` `const nestedOutputMaxSamples = Math.max(1, Math.floor(calc_constants.nestedGridOutput_max_samples \|\| 8192));`<br>변경 bb99fee 2026-07-02: `bb99fee:js/constants_load_calc.js:571` `const nestedOutputMaxSamples = Math.max(1, Math.floor(calc_constants.nestedGridOutput_max_samples \|\| 8192));`<br>변경 c4be488 2026-07-13: `c4be488:js/constants_load_calc.js:590` `if (Array.isArray(calc_constants.nestedGridOutput_rectangles) && calc_constants.nestedGridOutput_rectangles.length > 0) {`<br>현재 대응 `js/constants_load_calc.js:594` `if (Array.isArray(calc_constants.nestedGridOutput_rectangles) && calc_constants.nestedGridOutput_rectangles.length > 0) {`<br>두 파일 이력: L18. | 대상은 중첩 출력 표본 수 제한이다. 본판의 bb99fee·c4be488 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 양의 간격을 보장하고 표본 수가 상한을 넘으면 간격을 늘린다. 기간 0은 표본 1개다. 활성 사각형 수를 별도로 센다. transect 판에는 해당 계산이 없다. 이 행의 판 차이 근거는 bb99fee·c4be488의 본판 변경이다. |
| CT1 §5 | CT1-138 | A 판 차이 | A 판 차이 | 현재 `js/constants_load_calc.js:618` `calc_constants.sedC1_shields = 1.0 / ( (calc_constants.sedC1_denrat - 1.0) * calc_constants.g  * calc_constants.sedC1_d50/1000.);`<br>현재 `transect_version/js/constants_load_calc.js:447` `calc_constants.sedC1_shields = 1.0 / ( (calc_constants.sedC1_denrat - 1.0) * 9.81 * calc_constants.sedC1_d50/1000.);`<br>변경 22e1983 2025-06-06: `22e1983:js/constants_load_calc.js:459` `// console.log(ds, fall_vel)`<br>현재 대응 `js/constants_load_calc.js:631` `// console.log(ds, fall_vel)`<br>변경 ba9eb67 2025-06-09: `ba9eb67:js/constants_load_calc.js:451` `calc_constants.sedC1_shields = 1.0 / ( (calc_constants.sedC1_denrat - 1.0) * calc_constants.g  * calc_constants.sedC1_d50/1000.);`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/constants_load_calc.js:453` `let nu = 0.000001; // kinematic viscosity of water in m^2/s`<br>현재 대응 `js/constants_load_calc.js:622` `let nu = 0.000001; // kinematic viscosity of water in m^2/s`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/constants_load_calc.js:447` `calc_constants.sedC1_shields = 1.0 / ( (calc_constants.sedC1_denrat - 1.0) * 9.81 * calc_constants.sedC1_d50/1000.);`<br>두 파일 이력: L18. | 대상은 침강속도와 Shields 계수이다. 본판의 22e1983·ba9eb67·b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 g를 사용하고 nu=1e-6·A=25·B=1.25·n=1로 자연 입자 침강속도를 계산한다. transect 판은 9.81을 고정하고 sqrt((4/3)*9.81*d/0.2*(denrat-1))를 쓴다. 본판만 MPM 계수를 만든다. d50의 mm→m 변환은 같다. 이 행의 판 차이 근거는 22e1983·ba9eb67·b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-139 | A 판 차이 | A 판 차이 | 현재 `js/display_parameters.js:124` `const isSphericalGrid = Math.round(calc_constants.grid_type) == 2;`<br>현재 `transect_version/js/display_parameters.js:124` `` `X: ${Math.round(calc_constants.locationOfTimeSeries[i].xts * 100) / 100}, ` + ``<br>변경 ff0d046 2026-07-07: `ff0d046:js/display_parameters.js:124` `const isSphericalGrid = Math.round(calc_constants.grid_type) == 2;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/display_parameters.js:124` `` `X: ${Math.round(calc_constants.locationOfTimeSeries[i].xts * 100) / 100}, ` + ``<br>두 파일 이력: L19. | 대상은 측정점 좌표 표시이다. 본판의 ff0d046 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 구면 격자에서 절대 경위도와 소수 6자리를 쓴다. transect 판은 상대 X/Y와 소수 2자리를 쓴다. 이 행의 판 차이 근거는 ff0d046의 본판 변경이다. |
| CT1 §5 | CT1-142 | A 판 차이 | A 판 차이 | 현재 `js/display_parameters.js:236` `else if (boundaryType == 5) {`<br>변경 bb99fee 2026-07-02: `bb99fee:js/display_parameters.js:223` `else if (boundaryType == 5) {`<br>두 파일 이력: L19. | 대상은 type-5 경계 표시이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 파일 시계열 경계라는 표시 문자열을 제공한다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-145 | A 판 차이 | A 판 차이 | 현재 `shaders/AddDisturbance.wgsl:108` `var time_local = time;`<br>변경 185e91c 2026-01-30: `185e91c:shaders/AddDisturbance.wgsl:108` `var time_local = time;`<br>변경 3425a4a 2026-01-30: `3425a4a:shaders/AddDisturbance.wgsl:108` `if (time > 1.0e5*dt) {`<br>두 파일 이력: L21. | 3425a4a는 시간 제한 코드를 추가했다. 185e91c는 그 코드를 time_local을 쓰도록 수정했다. transect 판은 원래 time을 사용한다. | 본판은 time_local을 1.0e5*dt 이하로 제한한다. transect 판은 원래 time을 쓴다. 이 행의 판 차이 근거는 185e91c·3425a4a의 본판 변경이다. |
| CT1 §5 | CT1-146 | A 판 차이 | A 판 차이 | 현재 `shaders/AddDisturbance.wgsl:120` `//let angle = globals.disturbanceDir;`<br>현재 `transect_version/shaders/AddDisturbance.wgsl:115` `let angle = globals.disturbanceDir;`<br>변경 8c2b62b 2025-08-24: `8c2b62b:shaders/AddDisturbance.wgsl:115` `//let angle = globals.disturbanceDir;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/shaders/AddDisturbance.wgsl:115` `let angle = globals.disturbanceDir;`<br>두 파일 이력: L21. | 대상은 사면체 방향 정의이다. 본판의 8c2b62b 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 globals.disturbanceDir를 사용한다. 본판은 뒤에서 3.1415-traj_angle을 사용한다. 이 행의 판 차이 근거는 8c2b62b의 본판 변경이다. |
| CT1 §5 | CT1-147 | A 판 차이 | A 판 차이 | 현재 `shaders/AddDisturbance.wgsl:128` `let displacement = max_displacement*(1.0+tanh((time_local-time_shift)/(change_timescale)))/2.0;`<br>현재 `transect_version/shaders/AddDisturbance.wgsl:123` `let displacement = max_displacement*(1.0+tanh((time-time_shift)/(change_timescale)))/2.0;`<br>변경 185e91c 2026-01-30: `185e91c:shaders/AddDisturbance.wgsl:128` `let displacement = max_displacement*(1.0+tanh((time_local-time_shift)/(change_timescale)))/2.0;`<br>변경 8c2b62b 2025-08-24: `8c2b62b:shaders/AddDisturbance.wgsl:124` `let traj_angle = min(final_traj,initial_traj + displacement/max_displacement*(final_traj-initial_traj)*traj_timefactor) * 3.1415 / 180.;`<br>현재 대응 `shaders/AddDisturbance.wgsl:129` `let traj_angle = min(final_traj,initial_traj + displacement/max_displacement*(final_traj-initial_traj)*traj_timefactor) * 3.1415 / 180.;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/shaders/AddDisturbance.wgsl:123` `let displacement = max_displacement*(1.0+tanh((time-time_shift)/(change_timescale)))/2.0;`<br>두 파일 이력: L21. | 대상은 사면 이동 궤적이다. 본판의 185e91c·8c2b62b 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 초기·최종 각도의 차이에 traj_timefactor를 곱한다. transect 판은 변위 비율에 traj_timefactor만 곱한다. 본판은 사면체 회전각도 궤적에 연결한다. 이 행의 판 차이 근거는 185e91c·8c2b62b의 본판 변경이다. |
| CT1 §5 | CT1-148 | A 판 차이 | A 판 차이 | 현재 `shaders/AddDisturbance.wgsl:154` `if (time_local < 5.*dt) {`<br>현재 `transect_version/shaders/AddDisturbance.wgsl:147` `if (time < 5.*dt) {`<br>변경 185e91c 2026-01-30: `185e91c:shaders/AddDisturbance.wgsl:154` `if (time_local < 5.*dt) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/shaders/AddDisturbance.wgsl:147` `if (time < 5.*dt) {`<br>두 파일 이력: L21. | 대상은 최초 교란 정지 조건이다. 본판의 185e91c 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 time_local<5*dt를 쓴다. transect 판은 time<5*dt를 쓴다. 상한 전 시간에는 두 조건이 같다. 이 행의 판 차이 근거는 185e91c의 본판 변경이다. |
| CT1 §5 | CT1-150 | A 판 차이 | A 판 차이 | 현재 `shaders/AddDisturbance.wgsl:229` `//   if(bottom_initial_tex.z > 0.0 ) {  // without this, the slide creates water on dry land (for subaerial slides).`<br>현재 `transect_version/shaders/AddDisturbance.wgsl:222` `if(bottom_initial_tex.z > 0.0 ) {`<br>변경 8c2b62b 2025-08-24: `8c2b62b:shaders/AddDisturbance.wgsl:224` `//   if(bottom_initial_tex.z > 0.0 ) {  // without this, the slide creates water on dry land (for subaerial slides).`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/shaders/AddDisturbance.wgsl:222` `if(bottom_initial_tex.z > 0.0 ) {`<br>두 파일 이력: L21. | 대상은 육상 사면 변형 억제이다. 본판의 8c2b62b 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 초기 바닥고가 양수이면 기존 바닥고를 되돌리고 dhdt를 0으로 둔다. 본판은 이 조건을 주석 처리했다. 본판 주석은 이 조건의 물 생성 방지 목적을 설명하지만 현재는 실행하지 않는다. 이 행의 판 차이 근거는 8c2b62b의 본판 변경이다. |
| CT1 §5 | CT1-151 | A 판 차이 | A 판 차이 | 현재 `shaders/BoundaryPass.wgsl:44` `algochanges: i32,`<br>변경 896c491 2026-01-17: `896c491:shaders/BoundaryPass.wgsl:44` `algochanges: i32,`<br>변경 bb99fee 2026-07-02: `bb99fee:shaders/BoundaryPass.wgsl:45` `trough_factor: f32,`<br>현재 대응 `shaders/BoundaryPass.wgsl:45` `trough_factor: f32,`<br>두 파일 이력: L22. | 대상은 경계 uniform 확장이다. 본판의 896c491·bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 알고리즘 시험·trough_factor·구면 원점·4변 관측점 수·시간 보간 인덱스와 가중치를 받는다. 이 행의 판 차이 근거는 896c491·bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-162 | A 판 차이 | A 판 차이 | 현재 `shaders/CalcMeans.wgsl:25` `@group(0) @binding(13) var txNewState: texture_2d<f32>;`<br>변경 dc6cc2d 2025-08-10: `dc6cc2d:shaders/CalcMeans.wgsl:25` `@group(0) @binding(13) var txNewState: texture_2d<f32>;`<br>두 파일 이력: L23. | 대상은 통계 실제 수면 리소스이다. 본판의 dc6cc2d 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 txNewState를 받는다. 이 행의 판 차이 근거는 dc6cc2d의 본판 변경이다. |
| CT1 §5 | CT1-163 | A 판 차이 | A 판 차이 | 현재 `shaders/CalcMeans.wgsl:38` `let v4 = textureLoad(txV, idx, 0);`<br>현재 `transect_version/shaders/CalcMeans.wgsl:42` `let h = (h4.y + h4.w) / 2.0;`<br>변경 dc6cc2d 2025-08-10: `dc6cc2d:shaders/CalcMeans.wgsl:47` `var eta = textureLoad(txNewState, idx, 0).x;`<br>현재 대응 `shaders/CalcMeans.wgsl:47` `var eta = textureLoad(txNewState, idx, 0).x;`<br>transect 4dc20a1 2026-01-27: `4dc20a1:transect_version/shaders/CalcMeans.wgsl:42` `let h = (h4.y + h4.w) / 2.0;`<br>두 파일 이력: L23. | 대상은 통계 수면 자료원과 1D 속도 평균이다. 본판의 dc6cc2d 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 동·서 면 평균을 2.0으로 나눈다. 본판은 네 면 평균을 4.0으로 나눈다. 1D 환원에서 속도·수심·농도 평균은 같은 의미다. eta는 본판이 실제 txNewState 값이고 transect가 h+bottom이다. transect는 와도를 계산하지 않는다. 본판의 건조 셀 eta 대체값은 최대값 계산 전에만 적용된다. 이 행의 판 차이 근거는 dc6cc2d의 본판 변경이다. |
| CT1 §5 | CT1-165 | A 판 차이 | A 판 차이 | 현재 `shaders/Copytxf32_txf16.wgsl:4` `delta: f32,`<br>변경 dc6cc2d 2025-08-10: `dc6cc2d:shaders/Copytxf32_txf16.wgsl:4` `delta: f32,`<br>두 파일 이력: L24. | 대상은 표시용 건조 uniform이다. 본판의 dc6cc2d 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 delta와 base_depth를 받는다. 이 행의 판 차이 근거는 dc6cc2d의 본판 변경이다. |
| CT1 §5 | CT1-166 | A 판 차이 | A 판 차이 | 현재 `shaders/Copytxf32_txf16.wgsl:17` `@group(0) @binding(8) var txHardBottom: texture_2d<f32>;`<br>현재 `transect_version/shaders/Copytxf32_txf16.wgsl:21` `let eta = textureLoad(txNewState, idx, 0).r;`<br>변경 b8b50c3 2025-06-08: `b8b50c3:shaders/Copytxf32_txf16.wgsl:15` `@group(0) @binding(8) var txHardBottom: texture_2d<f32>;`<br>변경 dc6cc2d 2025-08-10: `dc6cc2d:shaders/Copytxf32_txf16.wgsl:23` `var eta = textureLoad(txNewState, idx, 0).r;`<br>현재 대응 `shaders/Copytxf32_txf16.wgsl:23` `var eta = textureLoad(txNewState, idx, 0).r;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/shaders/Copytxf32_txf16.wgsl:21` `let eta = textureLoad(txNewState, idx, 0).r;`<br>두 파일 이력: L24. | 대상은 표시용 f16 패킹이다. 본판의 b8b50c3·dc6cc2d 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 건조 셀 eta를 -10*base_depth로 바꾸고 foam을 0으로 둔다. 본판은 3번째 레이어에 bottom·hardbottom·가용 깊이를 쓴다. transect 판은 eta와 foam을 그대로 두고 두 레이어만 쓴다. 이 행의 판 차이 근거는 b8b50c3·dc6cc2d의 본판 변경이다. |
| CT1 §5 | CT1-167 | A 판 차이 | A 판 차이 | 현재 `shaders/ExtractTimeSeries.wgsl:10` `disturbanceType: i32`<br>변경 397c575 2025-09-09: `397c575:shaders/ExtractTimeSeries.wgsl:10` `disturbanceType: i32`<br>두 파일 이력: L26. | 대상은 교란 유형 uniform이다. 본판의 397c575 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 disturbanceType을 받는다. 이 행의 판 차이 근거는 397c575의 본판 변경이다. |
| CT1 §5 | CT1-168 | A 판 차이 | A 판 차이 | 현재 `shaders/ExtractTimeSeries.wgsl:22` `@group(0) @binding(8) var txMeans_Speed: texture_2d<f32>;`<br>변경 397c575 2025-09-09: `397c575:shaders/ExtractTimeSeries.wgsl:22` `@group(0) @binding(8) var txMeans_Speed: texture_2d<f32>;`<br>두 파일 이력: L26. | 대상은 툴팁 최대수면 리소스이다. 본판의 397c575 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 txMeans_Speed를 읽는다. 이 행의 판 차이 근거는 397c575의 본판 변경이다. |
| CT1 §5 | CT1-169 | A 판 차이 | A 판 차이 | 현재 `shaders/ExtractTimeSeries.wgsl:47` `var hsig = 0.0;`<br>현재 `transect_version/shaders/ExtractTimeSeries.wgsl:45` `let hsig = textureLoad(txWaveHeight, current_location, 0).z;  // Significant wave height`<br>변경 397c575 2025-09-09: `397c575:shaders/ExtractTimeSeries.wgsl:47` `var hsig = 0.0;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/shaders/ExtractTimeSeries.wgsl:45` `let hsig = textureLoad(txWaveHeight, current_location, 0).z;  // Significant wave height`<br>두 파일 이력: L26. | 대상은 툴팁 Hs 또는 최대수면 선택이다. 본판의 397c575 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 disturbanceType>1이면 최대 수면을 쓴다. 나머지 경우 Hs를 쓴다. transect 판은 항상 Hs를 쓴다. 이 행의 판 차이 근거는 397c575의 본판 변경이다. |
| CT1 §5 | CT1-170 | A 판 차이 | A 판 차이 | 현재 `shaders/MouseClickChange.wgsl:19` `designcomponent_CrestElev: f32,`<br>변경 d778fe7 2026-06-02: `d778fe7:shaders/MouseClickChange.wgsl:19` `designcomponent_CrestElev: f32,`<br>두 파일 이력: L27. | 대상은 선형 구조물 uniform이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 천단고·천단폭·사면경사·양끝 좌표·적용 플래그를 받는다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-171 | A 판 차이 | A 판 차이 | 현재 `shaders/MouseClickChange.wgsl:70` `fn calc_segment_distance(xloc: f32, yloc: f32, xstart: f32, ystart: f32, xend: f32, yend: f32) -> f32 {`<br>변경 d778fe7 2026-06-02: `d778fe7:shaders/MouseClickChange.wgsl:70` `fn calc_segment_distance(xloc: f32, yloc: f32, xstart: f32, ystart: f32, xend: f32, yend: f32) -> f32 {`<br>두 파일 이력: L27. | 대상은 선분 거리와 사다리꼴 고도 함수이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 선분 투영을 [0,1]로 제한한다. 본판은 천단 절반폭 밖의 거리에 경사를 곱해 목표 고도를 만든다. 폭이나 경사가 0 이하면 -1e9를 반환한다. transect 판에는 두 함수가 없다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-172 | A 판 차이 | A 판 차이 | 현재 `shaders/MouseClickChange.wgsl:131` `if (globals.designcomponent_AddLinearStructure == 1) {`<br>현재 `transect_version/shaders/MouseClickChange.wgsl:84` `B_here = textureLoad(txDesignComponents, idx, 0);`<br>변경 d778fe7 2026-06-02: `d778fe7:shaders/MouseClickChange.wgsl:131` `if (globals.designcomponent_AddLinearStructure == 1) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/shaders/MouseClickChange.wgsl:84` `B_here = textureLoad(txDesignComponents, idx, 0);`<br>두 파일 이력: L27. | 대상은 편집 대상 선택이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 선형 구조물 모드에서 바닥고·상태를 편집한다. transect 판은 설계 ID·마찰만 편집한다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-173 | A 판 차이 | A 판 차이 | 현재 `shaders/MouseClickChange.wgsl:215` `if (globals.designcomponent_AddLinearStructure == 1) {`<br>현재 `transect_version/shaders/MouseClickChange.wgsl:146` `var r = calc_radial_distance(xloc,yloc,xo,yo);`<br>변경 d778fe7 2026-06-02: `d778fe7:shaders/MouseClickChange.wgsl:215` `if (globals.designcomponent_AddLinearStructure == 1) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/shaders/MouseClickChange.wgsl:146` `var r = calc_radial_distance(xloc,yloc,xo,yo);`<br>두 파일 이력: L27. | 대상은 선형 구조물 적용이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 중심·북쪽 면·동쪽 면의 목표 고도를 계산해 기존 고도보다 낮추지 않게 쓴다. transect 판은 원형 영역의 설계 ID와 가우스 마찰 편집만 유지한다. 마지막 개행도 다르다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-180 | A 판 차이 | A 판 차이 | 현재 `shaders/Pass2.wgsl:10` `sedTurbDispersion: f32,`<br>변경 b8b50c3 2025-06-08: `b8b50c3:shaders/Pass2.wgsl:10` `sedTurbDispersion: f32,`<br>두 파일 이력: L28. | 대상은 퇴적물 확산 uniform이다. 본판의 b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 배경 확산과 쇄파 확산계수를 받는다. transect 판은 Pass2의 확산 보정을 구현하지 않는다. 이 행의 판 차이 근거는 b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-181 | A 판 차이 | A 판 차이 | 현재 `shaders/Pass2.wgsl:34` `@group(0) @binding(15) var txBreaking: texture_2d<f32>;`<br>변경 b8b50c3 2025-06-08: `b8b50c3:shaders/Pass2.wgsl:34` `@group(0) @binding(15) var txBreaking: texture_2d<f32>;`<br>두 파일 이력: L28. | 대상은 쇄파 입력 binding이다. 본판의 b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 binding 15에서 쇄파 점성을 읽는다. 이 행의 판 차이 근거는 b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-188 | A 판 차이 | A 판 차이 | 현재 `shaders/Pass3_Bous.wgsl:38` `vort_friction_factor: f32,`<br>변경 35b7f1c 2026-01-15: `35b7f1c:shaders/Pass3_Bous.wgsl:38` `vort_friction_factor: f32,`<br>두 파일 이력: L31. | 대상은 와도 소산 uniform이다. 본판의 35b7f1c 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 후속 와도 소산계수를 받는다. 이 행의 판 차이 근거는 35b7f1c의 본판 변경이다. |
| CT1 §5 | CT1-198 | A 판 차이 | A 판 차이 | 현재 `shaders/Pass3_COULWAVE.wgsl:38` `vort_friction_factor: f32,`<br>변경 35b7f1c 2026-01-15: `35b7f1c:shaders/Pass3_COULWAVE.wgsl:38` `vort_friction_factor: f32,`<br>두 파일 이력: L32. | 대상은 COULWAVE 와도 소산계수이다. 본판의 35b7f1c 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 후속 vort_friction_factor uniform을 받는다. 이 행의 판 차이 근거는 35b7f1c의 본판 변경이다. |
| CT1 §5 | CT1-210 | A 판 차이 | A 판 차이 | 현재 `shaders/Pass3_NLSW.wgsl:38` `vort_friction_factor: f32,`<br>변경 35b7f1c 2026-01-15: `35b7f1c:shaders/Pass3_NLSW.wgsl:38` `vort_friction_factor: f32,`<br>두 파일 이력: L33. | 대상은 와도 소산 uniform이다. 본판의 35b7f1c 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판의 vort_friction_factor는 후속 추가 기능이다. transect 판에는 이 uniform이 없다. 이 행의 판 차이 근거는 35b7f1c의 본판 변경이다. |
| CT1 §5 | CT1-221 | A 판 차이 | A 판 차이 | 현재 `shaders/SedTrans_Pass3.wgsl:22` `base_depth: f32,`<br>변경 22e1983 2025-06-06: `22e1983:shaders/SedTrans_Pass3.wgsl:22` `base_depth: f32,`<br>변경 5c60ac0 2025-06-07: `5c60ac0:shaders/SedTrans_Pass3.wgsl:24` `sedTurbDispersion: f32,`<br>현재 대응 `shaders/SedTrans_Pass3.wgsl:24` `sedTurbDispersion: f32,`<br>변경 b8b50c3 2025-06-08: `b8b50c3:shaders/SedTrans_Pass3.wgsl:25` `sedBreakingDispersionCoef: f32,`<br>현재 대응 `shaders/SedTrans_Pass3.wgsl:25` `sedBreakingDispersionCoef: f32,`<br>변경 ba9eb67 2025-06-09: `ba9eb67:shaders/SedTrans_Pass3.wgsl:26` `sedC1_bedloadMPM: f32,`<br>현재 대응 `shaders/SedTrans_Pass3.wgsl:26` `sedC1_bedloadMPM: f32,`<br>두 파일 이력: L35. | 대상은 퇴적물 closure uniform이다. 본판의 22e1983·5c60ac0·b8b50c3·ba9eb67 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판에는 base_depth·delta·확산계수·MPM 계수가 없다. 본판의 후속 퇴적물 모델 확장과 연결된다. 이 행의 판 차이 근거는 22e1983·5c60ac0·b8b50c3·ba9eb67의 본판 변경이다. |
| CT1 §5 | CT1-222 | A 판 차이 | A 판 차이 | 현재 `shaders/SedTrans_Pass3.wgsl:45` `@group(0) @binding(13) var txBreaking: texture_2d<f32>;`<br>변경 22e1983 2025-06-06: `22e1983:shaders/SedTrans_Pass3.wgsl:42` `@group(0) @binding(13) var txBreaking: texture_2d<f32>;`<br>변경 2a7452d 2025-06-07: `2a7452d:shaders/SedTrans_Pass3.wgsl:46` `@group(0) @binding(16) var txSed_C1: texture_2d<f32>;`<br>현재 대응 `shaders/SedTrans_Pass3.wgsl:48` `@group(0) @binding(16) var txSed_C1: texture_2d<f32>;`<br>변경 b8b50c3 2025-06-08: `b8b50c3:shaders/SedTrans_Pass3.wgsl:48` `@group(0) @binding(17) var txHardBottom: texture_2d<f32>;`<br>현재 대응 `shaders/SedTrans_Pass3.wgsl:49` `@group(0) @binding(17) var txHardBottom: texture_2d<f32>;`<br>두 파일 이력: L35. | 대상은 퇴적물 입력 binding이다. 본판의 22e1983·2a7452d·b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판에는 쇄파·면속도·면농도·hardbottom 리소스가 없다. 이 행의 판 차이 근거는 22e1983·2a7452d·b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-223 | A 판 차이 | F 표기 차이 | 현재 `shaders/SedTrans_Pass3.wgsl:71` `let B = textureLoad(txBottom, idx, 0).z;`<br>변경 2a7452d 2025-06-07: `2a7452d:shaders/SedTrans_Pass3.wgsl:69` `let B = textureLoad(txBottom, idx, 0).z;`<br>변경 852ec28 2025-06-13: `852ec28:shaders/SedTrans_Pass3.wgsl:77` `let C_state_here = textureLoad(txState_Sed, idx, 0);`<br>현재 대응 `shaders/SedTrans_Pass3.wgsl:77` `let C_state_here = textureLoad(txState_Sed, idx, 0);`<br>두 파일 이력: L35.<br>같은 상태식 `ebca435:shaders/SedTrans_Pass3.wgsl:71` `let B = textureLoad(txBottom, idx, 0).z;`<br>`ebca435:shaders/SedTrans_Pass3.wgsl:72` `let in_state_here = textureLoad(txState, idx, 0);`<br>`ebca435:shaders/SedTrans_Pass3.wgsl:73` `let eta = in_state_here.x;`<br>`ebca435:shaders/SedTrans_Pass3.wgsl:74` `let hu = in_state_here.y;`<br>`ebca435:shaders/SedTrans_Pass3.wgsl:75` `let hv = in_state_here.z;`<br>`ebca435:shaders/SedTrans_Pass3.wgsl:76` `let h = eta - B;`<br>`ebca435:shaders/SedTrans_Pass3.wgsl:77` `let C_state_here = textureLoad(txState_Sed, idx, 0);`<br>transect의 같은 상태식 `ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:85` `let B = textureLoad(txBottom, idx, 0).z;`<br>`ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:86` `let in_state_here = textureLoad(txState, idx, 0);`<br>`ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:87` `let eta = in_state_here.x;`<br>`ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:88` `let hu = in_state_here.y;`<br>`ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:89` `let hv = in_state_here.z;`<br>`ebca435:transect_version/shaders/SedTrans_Pass3.wgsl:90` `let h = eta - B;` | 2a7452d는 동일한 B·eta·hu·hv·h 읽기를 앞으로 옮겼다. 852ec28은 C_state_here 읽기를 앞으로 옮겼다. 이 행이 비교한 읽기 위치에는 값이나 식의 차이가 없다. 커밋의 다른 퇴적물 식 변경은 이 행의 읽기 위치 차이를 동작 차이로 만들지 않는다. | 본판과 transect 판은 같은 셀 상태식을 서로 다른 위치에서 읽는다. 이 읽기 위치 차이는 F 표기 차이다. |
| CT1 §5 | CT1-226 | A 판 차이 | A 판 차이 | 현재 `shaders/SedTrans_UpdateBottom.wgsl:11` `west_boundary_type: i32,`<br>변경 22e1983 2025-06-06: `22e1983:shaders/SedTrans_UpdateBottom.wgsl:11` `west_boundary_type: i32,`<br>두 파일 이력: L37.<br>변경 전 `4fa700a:shaders/SedTrans_UpdateBottom.wgsl:8` `timeScheme: i32,`<br>`4fa700a:shaders/SedTrans_UpdateBottom.wgsl:9` `pred_or_corrector: i32,`<br>`4fa700a:shaders/SedTrans_UpdateBottom.wgsl:10` `sedC1_n: f32,`<br>`4fa700a:shaders/SedTrans_UpdateBottom.wgsl:11` `};`<br><br>같은 커밋의 transect `22e1983:transect_version/shaders/SedTrans_UpdateBottom.wgsl:8` `timeScheme: i32,`<br>`22e1983:transect_version/shaders/SedTrans_UpdateBottom.wgsl:9` `pred_or_corrector: i32,`<br>`22e1983:transect_version/shaders/SedTrans_UpdateBottom.wgsl:10` `sedC1_n: f32,`<br>`22e1983:transect_version/shaders/SedTrans_UpdateBottom.wgsl:11` `};`<br> | 대상은 지형 갱신 경계 uniform이다. 본판의 22e1983 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. 22e1983은 본판을 수정하면서 수정 전 코드를 가진 transect 사본을 추가했다. | 본판은 22e1983에서 바닥 갱신의 경계 유형 입력을 추가했다. transect 판은 그 입력이 없는 코드를 보존한다. |
| CT1 §5 | CT1-229 | A 판 차이 | A 판 차이 | 현재 `shaders/TriDiag_PCRx.wgsl:7` `P: i32,`<br>변경 984091f 2026-05-24: `984091f:shaders/TriDiag_PCRx.wgsl:7` `P: i32,`<br>두 파일 이력: L39. | 대상은 PCR 최종 반복 uniform이다. 본판의 984091f 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 P를 받아 최종 반복에서만 상태를 저장한다. transect 판은 모든 반복에서 저장한다. 이 행의 판 차이 근거는 984091f의 본판 변경이다. |
| CT1 §5 | CT1-234 | A 판 차이 | A 판 차이 | 현재 `shaders/TriDiag_PCRy.wgsl:7` `P: i32,`<br>변경 984091f 2026-05-24: `984091f:shaders/TriDiag_PCRy.wgsl:7` `P: i32,`<br>두 파일 이력: L40. | 대상은 PCR 최종 반복 uniform이다. 본판의 984091f 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 P를 받아 최종 반복에서만 상태를 저장한다. transect 판은 모든 반복에서 저장한다. 이 행의 판 차이 근거는 984091f의 본판 변경이다. |
| CT1 §5 | CT1-246 | A 판 차이 | A 판 차이 | 현재 `shaders/fragment.wgsl:58` `disturbanceType: f32,`<br>변경 d23dfb0 2025-09-01: `d23dfb0:shaders/fragment.wgsl:58` `disturbanceType: f32,`<br>변경 d778fe7 2026-06-02: `d778fe7:shaders/fragment.wgsl:58` `disturbanceType: f32,`<br>두 파일 이력: L41. | 대상은 표시 uniform 확장이다. 본판의 d23dfb0·d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 교란 유형과 선형 구조물 미리보기 상태를 받는다. 이 행의 판 차이 근거는 d23dfb0·d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-247 | A 판 차이 | A 판 차이 | 현재 `shaders/fragment.wgsl:290` `let depth_change = textureSample(bottomTexture, textureSampler, uv).b - textureSample(erosion_Sed, textureSampler, uv).b;`<br>변경 8c2b62b 2025-08-24: `8c2b62b:shaders/fragment.wgsl:280` `let depth_change = textureSample(bottomTexture, textureSampler, uv).b - textureSample(erosion_Sed, textureSampler, uv).b;`<br>두 파일 이력: L41. | 대상은 실제 바닥고 변화 표시이다. 본판의 8c2b62b 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 현재 바닥고와 초기 바닥고의 차이를 읽는다. transect 판은 erosion 입력을 실제 침식률 표시용으로 쓴다. 이 행의 판 차이 근거는 8c2b62b의 본판 변경이다. |
| CT1 §5 | CT1-250 | A 판 차이 | A 판 차이 | 현재 `shaders/fragment.wgsl:578` `if (abs(depth_change) > globals.delta && globals.disturbanceType == 5) {  // make slide mass gray`<br>현재 `transect_version/shaders/fragment.wgsl:563` `if(globals.IsOverlayMapLoaded == 1) {`<br>변경 8c2b62b 2025-08-24: `8c2b62b:shaders/fragment.wgsl:569` `let depth_change_scale = depth_change/globals.base_depth*50.0;`<br>현재 대응 `shaders/fragment.wgsl:579` `let depth_change_scale = depth_change/globals.base_depth*50.0;`<br>변경 d23dfb0 2025-09-01: `d23dfb0:shaders/fragment.wgsl:569` `if (abs(depth_change) > globals.delta && globals.disturbanceType == 5) {  // make slide mass gray`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/shaders/fragment.wgsl:563` `if(globals.IsOverlayMapLoaded == 1) {`<br>두 파일 이력: L41. | 대상은 육상 이동 사면 색상이다. 본판의 8c2b62b·d23dfb0 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 disturbanceType==5이고 변화량이 delta를 넘으면 회색 사면을 표시한다. transect 판은 overlay·일반 육상 색상을 쓴다. 이 행의 판 차이 근거는 8c2b62b·d23dfb0의 본판 변경이다. |
| CT1 §5 | CT1-251 | A 판 차이 | A 판 차이 | 현재 `shaders/fragment.wgsl:783` `var layer = 9;`<br>현재 `transect_version/shaders/fragment.wgsl:764` `let layer = 9;`<br>변경 3c1649b 2026-02-11: `3c1649b:shaders/fragment.wgsl:774` `var layer = 9;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/shaders/fragment.wgsl:764` `let layer = 9;`<br>두 파일 이력: L41. | 대상은 화살표 텍스처 레이어이다. 본판의 3c1649b 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 사실적 표시에서 채워진 화살표 레이어 10을 쓴다. transect 판은 레이어 9를 쓴다. 이 행의 판 차이 근거는 3c1649b의 본판 변경이다. |
| CT1 §5 | CT1-252 | A 판 차이 | A 판 차이 | 현재 `shaders/fragment.wgsl:804` `if (globals.designcomponent_PreviewOn == 1) {`<br>변경 d778fe7 2026-06-02: `d778fe7:shaders/fragment.wgsl:804` `if (globals.designcomponent_PreviewOn == 1) {`<br>두 파일 이력: L41. | 대상은 선형 구조물 미리보기이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 끝점 점과 선분을 검게 표시한다. transect 판에는 미리보기 경로가 없다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-255 | A 판 차이 | A 판 차이 | 현재 `js/main.js:40` `import { create_ExtractNestedBoundaryTimeSeries_BindGroupLayout, create_ExtractNestedBoundaryTimeSeries_BindGroup } from './Handler_ExtractNestedBoundaryTimeSeries.js';`<br>현재 `transect_version/js/main.js:31` `import { fetchShader, runComputeShader, runCopyTextures } from './Run_Compute_Shader.js';  // function to run shaders, works for all`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:40` `import { create_ExtractNestedBoundaryTimeSeries_BindGroupLayout, create_ExtractNestedBoundaryTimeSeries_BindGroup } from './Handler_ExtractNestedBoundaryTimeSeries.js';`<br>변경 3646fc8 2026-02-08: `3646fc8:js/main.js:31` `import { fetchShader, runComputeShader, runCopyTextures, runComputeShader_EncStack, runCopyTextures_EncStack} from './Run_Compute_Shader.js';  // function to run shaders, works for all`<br>현재 대응 `js/main.js:43` `import { fetchShader, runComputeShader, runCopyTextures, runComputeShader_EncStack, runCopyTextures_EncStack} from './Run_Compute_Shader.js';  // function to run shaders, works for all`<br>변경 0ee5174 2026-06-18: `0ee5174:js/main.js:36` `import { installCelerisAgentControls } from './agent_controls.js?v=agent-timeseries-duration-native-path-20260614';`<br>현재 대응 `js/main.js:46` `import { installCelerisAgentControls } from './agent_controls.js?v=agent-timeseries-duration-native-path-20260614';`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:31` `import { fetchShader, runComputeShader, runCopyTextures } from './Run_Compute_Shader.js';  // function to run shaders, works for all`<br>두 파일 이력: L20. | 대상은 호스트 모듈 연결이다. 본판의 bb99fee·3646fc8·0ee5174 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 중첩 경계 handler·EncStack·agent_controls를 import한다. transect 판은 즉시 submit 함수를 쓴다. 이 행의 판 차이 근거는 bb99fee·3646fc8·0ee5174의 본판 변경이다. |
| CT1 §5 | CT1-256 | A 판 차이 | A 판 차이 | 현재 `js/main.js:66` `let pseudoFullscreenActive = false;`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:53` `let pseudoFullscreenActive = false;`<br>변경 0ee5174 2026-06-18: `0ee5174:js/main.js:58` `let agentDesignInteractionMode = null;`<br>현재 대응 `js/main.js:68` `let agentDesignInteractionMode = null;`<br>변경 d778fe7 2026-06-02: `d778fe7:js/main.js:58` `function updateLinearStructureLocationsDisplayFromCalcConstants() {`<br>현재 대응 `js/main.js:71` `function updateLinearStructureLocationsDisplayFromCalcConstants() {`<br>두 파일 이력: L20. | 대상은 선형 구조물과 전체화면 상태이다. 본판의 24b8f13·0ee5174·d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 가상 전체화면 플래그와 외부 제어 모드를 둔다. 본판은 선형 구조물 양끝점 표시와 적용 후 초기화를 구현한다. 이 행의 판 차이 근거는 24b8f13·0ee5174·d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-257 | A 판 차이 | A 판 차이 | 현재 `js/main.js:122` `function postAgentCaseStatus(status, payload = {}) {`<br>현재 `transect_version/js/main.js:67` `async function OrderedFunctions(configContent, bathymetryContent, waveContent) {`<br>변경 f6fd78b 2026-06-04: `f6fd78b:js/main.js:109` `function postAgentCaseStatus(status, payload = {}) {`<br>변경 0ee5174 2026-06-18: `0ee5174:js/main.js:128` `async function fetchAgentCaseBlob(url, label) {`<br>현재 대응 `js/main.js:138` `async function fetchAgentCaseBlob(url, label) {`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:122` `function postAgentCaseStatus(status, payload = {}) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:67` `async function OrderedFunctions(configContent, bathymetryContent, waveContent) {`<br>두 파일 이력: L20. | 대상은 URL 케이스 초기화이다. 본판의 f6fd78b·0ee5174·bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 agent_case·autostart 쿼리를 읽고 manifest의 config·bathy·waves·선택 overlay·초기 수면을 fetch한다. 로딩 상태는 부모 창으로 postMessage한다. transect 판에는 해당 진입 경로가 없다. 이 행의 판 차이 근거는 f6fd78b·0ee5174·bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-259 | A 판 차이 | A 판 차이 | 현재 `js/main.js:249` `const requestedMaxTextureDimension2D = adapter.limits?.maxTextureDimension2D \|\| 8192;`<br>현재 `transect_version/js/main.js:118` `requiredLimits: {},`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:249` `const requestedMaxTextureDimension2D = adapter.limits?.maxTextureDimension2D \|\| 8192;`<br>변경 769d990 2026-02-01: `769d990:js/main.js:121` `device.lost.then((info) => {`<br>현재 대응 `js/main.js:267` `device.lost.then((info) => {`<br>변경 7ae7da4 2026-02-23: `7ae7da4:js/main.js:122` ``console.error(`WebGPU device lost: reason="${info.reason}", message="${info.message}"`);``<br>현재 대응 `js/main.js:268` ``console.error(`WebGPU device lost: reason="${info.reason}", message="${info.message}"`);``<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:115` `requiredLimits: {},`<br>두 파일 이력: L20. | 대상은 GPU 장치 요청과 오류 기록이다. 본판의 bb99fee·769d990·7ae7da4 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 adapter의 2D 텍스처 최대 길이를 요청한다. 본판은 device lost와 uncapturederror를 기록한다. transect 판은 기본 requiredLimits를 쓴다. 이 행의 판 차이 근거는 bb99fee·769d990·7ae7da4의 본판 변경이다. |
| CT1 §5 | CT1-260 | A 판 차이 | A 판 차이 | 현재 `js/main.js:294` `const boundaryTimeSeriesFiles = {`<br>현재 `transect_version/js/main.js:137` `let { bathy2D, waveData } = await OrderedFunctions(configContent, bathymetryContent, waveContent);`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:294` `const boundaryTimeSeriesFiles = {`<br>변경 9093d7f 2026-06-01: `9093d7f:js/main.js:152` `const loadedBoundaryNumberOfWaves = calc_constants.numberOfWaves;`<br>현재 대응 `js/main.js:304` `const loadedBoundaryNumberOfWaves = calc_constants.numberOfWaves;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:134` `let { bathy2D, waveData } = await OrderedFunctions(configContent, bathymetryContent, waveContent);`<br>두 파일 이력: L20. | 대상은 파 생성과 type5 시간 보간이다. 본판의 bb99fee·9093d7f 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 원래 파 스펙트럼을 복사해 보존한다. 본판은 UI sine/TMA 생성과 텍스처 재업로드를 지원한다. type5는 시간 이진 탐색과 선형 보간을 쓴다. 마지막 시각 뒤는 영 상태 행을 선택한다. transect 판은 단면 파랑을 한 번 읽는다. 이 행의 판 차이 근거는 bb99fee·9093d7f의 본판 변경이다. |
| CT1 §5 | CT1-261 | A 판 차이 | A 판 차이 | 현재 `js/main.js:416` `let Render_bufferSize = 304; // 304 bytes for render pipeline, 256 for compute pipeline`<br>현재 `transect_version/js/main.js:160` `let Render_bufferSize = 272; // 272 bytes for render pipeline, 256 for compute pipeline`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:415` `let Render_bufferSize = 304; // 304 bytes for render pipeline, 256 for compute pipeline`<br>변경 c4be488 2026-07-13: `c4be488:js/main.js:413` `// Added by Codex: Nested-grid output now allocates one uniform buffer per output rectangle at capture start.`<br>현재 대응 `js/main.js:413` `// Added by Codex: Nested-grid output now allocates one uniform buffer per output rectangle at capture start.`<br>변경 d778fe7 2026-06-02: `d778fe7:js/main.js:248` `let Render_bufferSize = 304; // 304 bytes for render pipeline, 256 for compute pipeline`<br>변경 09cfd76 2026-02-15: `09cfd76:js/main.js:174` `const requiredBytesPerRow_2Dbuffer = Math.ceil((calc_constants.WIDTH * 4 * 4) / 256) * 256;`<br>현재 대응 `js/main.js:423` `const requiredBytesPerRow_2Dbuffer = Math.ceil((calc_constants.WIDTH * 4 * 4) / 256) * 256;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:157` `let Render_bufferSize = 272; // 272 bytes for render pipeline, 256 for compute pipeline`<br>두 파일 이력: L20. | 대상은 uniform·공용 readback 버퍼이다. 본판의 bb99fee·c4be488·d778fe7·09cfd76 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판 Render_bufferSize는 304이고 transect는 272다. 본판만 표면 출력용 공용 readback 버퍼를 할당한다. 두 판은 동일한 256배수 행 길이 식을 사용한다. 이 행의 판 차이 근거는 bb99fee·c4be488·d778fe7·09cfd76의 본판 변경이다. |
| CT1 §5 | CT1-263 | A 판 차이 | A 판 차이 | 현재 `js/main.js:469` `const txHardBottom = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores hard bottom elevation`<br>변경 4353b85 2025-06-09: `4353b85:js/main.js:201` `const txHardBottom = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);  // stores hard bottom elevation`<br>두 파일 이력: L20. | 대상은 hardbottom 텍스처이다. 본판의 4353b85 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 txHardBottom을 할당한다. 이 행의 판 차이 근거는 4353b85의 본판 변경이다. |
| CT1 §5 | CT1-264 | A 판 차이 | A 판 차이 | 현재 `js/main.js:509` `const txSphericalMetrics = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:418` `const txSphericalMetrics = create_2D_Texture(device, calc_constants.WIDTH, calc_constants.HEIGHT, allTextures);`<br>두 파일 이력: L20. | 대상은 구면 계량 텍스처이다. 본판의 afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 txSphericalMetrics를 할당한다. 이 행의 판 차이 근거는 afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-267 | A 판 차이 | A 판 차이 | 현재 `js/main.js:756` `imageUrl = '/textures/arrow_filled.png';`<br>변경 3c1649b 2026-02-11: `3c1649b:js/main.js:465` `imageUrl = '/textures/arrow_filled.png';`<br>두 파일 이력: L20. | 대상은 화살표 영상 레이어이다. 본판의 3c1649b 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 채워진 화살표를 레이어 10에 업로드한다. 이 행의 판 차이 근거는 3c1649b의 본판 변경이다. |
| CT1 §5 | CT1-268 | A 판 차이 | A 판 차이 | 현재 `js/main.js:830` `const explorerCameraDegToRad = Math.PI / 180.0;`<br>현재 `transect_version/js/main.js:503` `0.1 * simWidth,`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:723` `const explorerCameraDegToRad = Math.PI / 180.0;`<br>변경 f183cc2 2026-02-01: `f183cc2:js/main.js:553` `if (calc_constants.cameraInit_user == 1) {`<br>현재 대응 `js/main.js:890` `if (calc_constants.cameraInit_user == 1) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:498` `0.1 * simWidth,`<br>두 파일 이력: L20. | 대상은 카메라 초기화 좌표이다. 본판의 afc1fe7·f183cc2 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 구면 각도 격자를 미터 척도로 바꾼다. 본판은 사용자 카메라 위치·yaw·pitch·lookDist를 적용한다. transect 판은 simWidth·simHeight의 Cartesian 기본 카메라를 쓴다. 이 행의 판 차이 근거는 afc1fe7·f183cc2의 본판 변경이다. |
| CT1 §5 | CT1-269 | A 판 차이 | A 판 차이 | 현재 `js/main.js:935` `if (calc_constants.cameraInit_user == 1) {`<br>변경 f183cc2 2026-02-01: `f183cc2:js/main.js:588` `if (calc_constants.cameraInit_user == 1) {`<br>두 파일 이력: L20. | 대상은 사용자 카메라 회전이다. 본판의 f183cc2 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 사용자 yaw·pitch를 초기 각도로 적용한다. 이 행의 판 차이 근거는 f183cc2의 본판 변경이다. |
| CT1 §5 | CT1-270 | A 판 차이 | A 판 차이 | 현재 `js/main.js:986` `const Pass1_dx_for_slope = calc_constants.grid_type == 2 ? Math.max(calc_constants.R_earth, 1.0) * Math.max(Math.abs(Math.cos(0.5 * (calc_constants.lat_LL + calc_constants.lat_UR) * Math.PI / 180.0)), 1.0e-6) * Math.max(Math.abs(calc_constants.dx) * Math.PI / 180.0, 1.0e-12) : calc_constants.dx;`<br>현재 `transect_version/js/main.js:575` `Pass1_view.setFloat32(40, calc_constants.dx, true);           // f32`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:879` `const Pass1_dx_for_slope = calc_constants.grid_type == 2 ? Math.max(calc_constants.R_earth, 1.0) * Math.max(Math.abs(Math.cos(0.5 * (calc_constants.lat_LL + calc_constants.lat_UR) * Math.PI / 180.0)), 1.0e-6) * Math.max(Math.abs(calc_constants.dx) * Math.PI / 180.0, 1.0e-12) : calc_constants.dx;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:570` `Pass1_view.setFloat32(40, calc_constants.dx, true);           // f32`<br>두 파일 이력: L20. | 대상은 재구성 경사 격자간격이다. 본판의 afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 구면 격자의 각도 간격을 미터 근사값으로 바꿔 Froude 경사 제한에 전달한다. transect 판은 dx·dy를 그대로 전달한다. Cartesian 경로 값은 같다. 이 행의 판 차이 근거는 afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-271 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1010` `SedTrans_Pass1_view.setFloat32(40, Pass1_dx_for_slope, true);           // f32`<br>현재 `transect_version/js/main.js:594` `SedTrans_Pass1_view.setFloat32(40, calc_constants.dx, true);           // f32`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:903` `SedTrans_Pass1_view.setFloat32(40, Pass1_dx_for_slope, true);           // f32`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/main.js:607` `const Pass2_BindGroup = create_Pass2_BindGroup(device, Pass2_uniformBuffer, txH, txU, txV, txBottom, txC, txHnear, txXFlux, txYFlux, txSed_C1, txSed_C2, txSed_C3, txSed_C4, txXFlux_Sed, txYFlux_Sed, txBreaking);`<br>현재 대응 `js/main.js:1015` `const Pass2_BindGroup = create_Pass2_BindGroup(device, Pass2_uniformBuffer, txH, txU, txV, txBottom, txC, txHnear, txXFlux, txYFlux, txSed_C1, txSed_C2, txSed_C3, txSed_C4, txXFlux_Sed, txYFlux_Sed, txBreaking);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:589` `SedTrans_Pass1_view.setFloat32(40, calc_constants.dx, true);           // f32`<br>두 파일 이력: L20. | 대상은 퇴적물 재구성 격자간격과 쇄파 입력이다. 본판의 afc1fe7·b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 동일한 구면 간격 변환을 사용한다. transect 판은 dx·dy를 그대로 쓴다. transect Pass2 바인드 그룹은 txBreaking을 받지 않는다. 이 행의 판 차이 근거는 afc1fe7·b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-272 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1026` `Pass2_view.setFloat32(32, calc_constants.sedTurbDispersion, true);           // f32`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/main.js:618` `Pass2_view.setFloat32(32, calc_constants.sedTurbDispersion, true);           // f32`<br>두 파일 이력: L20. | 대상은 Pass2 확산계수 uniform이다. 본판의 b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 오프셋 32·36에 배경·쇄파 퇴적물 확산계수를 쓴다. 이 행의 판 차이 근거는 b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-273 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1078` `const Pass3_BindGroup = create_Pass3_BindGroup(device, Pass3_uniformBuffer, txState, txBottom, txCW_groupings, txXFlux, txYFlux, oldGradients, oldOldGradients, predictedGradients, F_G_star_oldGradients, F_G_star_oldOldGradients, txstateUVstar, txBoundaryForcing, txNewState, dU_by_dt, predictedF_G_star, current_stateUVstar,txContSource,txBreaking, calc_constants.grid_type == 2 ? txSphericalMetrics : txDissipationFlux, txBottomFriction);`<br>현재 `transect_version/js/main.js:658` `const Pass3_BindGroup = create_Pass3_BindGroup(device, Pass3_uniformBuffer, txState, txBottom, txCW_groupings, txXFlux, txYFlux, oldGradients, oldOldGradients, predictedGradients, F_G_star_oldGradients, F_G_star_oldOldGradients, txstateUVstar, txBoundaryForcing, txNewState, dU_by_dt, predictedF_G_star, current_stateUVstar,txContSource,txBreaking, txDissipationFlux, txBottomFriction);`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:971` `const Pass3_BindGroup = create_Pass3_BindGroup(device, Pass3_uniformBuffer, txState, txBottom, txCW_groupings, txXFlux, txYFlux, oldGradients, oldOldGradients, predictedGradients, F_G_star_oldGradients, F_G_star_oldOldGradients, txstateUVstar, txBoundaryForcing, txNewState, dU_by_dt, predictedF_G_star, current_stateUVstar,txContSource,txBreaking, calc_constants.grid_type == 2 ? txSphericalMetrics : txDissipationFlux, txBottomFriction);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:653` `const Pass3_BindGroup = create_Pass3_BindGroup(device, Pass3_uniformBuffer, txState, txBottom, txCW_groupings, txXFlux, txYFlux, oldGradients, oldOldGradients, predictedGradients, F_G_star_oldGradients, F_G_star_oldOldGradients, txstateUVstar, txBoundaryForcing, txNewState, dU_by_dt, predictedF_G_star, current_stateUVstar,txContSource,txBreaking, txDissipationFlux, txBottomFriction);`<br>두 파일 이력: L20. | 대상은 Pass3 binding 19이다. 본판의 afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 grid_type==2이면 구면 계량 텍스처를 전달한다. transect 판은 항상 쇄파 응력 텍스처를 전달한다. 이 행의 판 차이 근거는 afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-274 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1117` `Pass3_view.setFloat32(144, calc_constants.vort_friction_factor, true);       // f32`<br>현재 `transect_version/js/main.js:700` `const SedTrans_Pass3_BindGroup = create_SedTrans_Pass3_BindGroup(device, SedTrans_Pass3_uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed);`<br>변경 35b7f1c 2026-01-15: `35b7f1c:js/main.js:727` `Pass3_view.setFloat32(144, calc_constants.vort_friction_factor, true);       // f32`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:1012` `Pass3_view.setFloat32(148, 1.0 / Math.max(calc_constants.R_earth, 1.0), true);       // f32`<br>현재 대응 `js/main.js:1119` `Pass3_view.setFloat32(148, 1.0 / Math.max(calc_constants.R_earth, 1.0), true);       // f32`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/main.js:710` `const SedTrans_Pass3_BindGroup = create_SedTrans_Pass3_BindGroup(device, SedTrans_Pass3_uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed, txBreaking, txU, txV, txSed_C1, txHardBottom);`<br>현재 대응 `js/main.js:1123` `const SedTrans_Pass3_BindGroup = create_SedTrans_Pass3_BindGroup(device, SedTrans_Pass3_uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed, txBreaking, txU, txV, txSed_C1, txHardBottom);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:695` `const SedTrans_Pass3_BindGroup = create_SedTrans_Pass3_BindGroup(device, SedTrans_Pass3_uniformBuffer, txState_Sed, txXFlux_Sed, txYFlux_Sed, oldGradients_Sed, oldOldGradients_Sed, predictedGradients_Sed, txBottom, txState, txNewState_Sed, dU_by_dt_Sed, erosion_Sed, depostion_Sed);`<br>두 파일 이력: L20. | 대상은 Pass3·퇴적물 바인딩 확장이다. 본판의 35b7f1c·afc1fe7·b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 와도 소산·지구 반지름 역수를 uniform 꼬리에 쓴다. 본판의 퇴적물 적분은 추가 5개 텍스처를 받는다. 이 행의 판 차이 근거는 35b7f1c·afc1fe7·b8b50c3의 본판 변경이다. |
| CT1 §5 | CT1-276 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1205` `BoundaryPass_view.setInt32(168, calc_constants.algochanges, true);           // i32`<br>변경 896c491 2026-01-17: `896c491:js/main.js:809` `BoundaryPass_view.setInt32(168, calc_constants.algochanges, true);           // i32`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:1204` `BoundaryPass_view.setInt32(168, calc_constants.algochanges, true);           // i32`<br>변경 984091f 2026-05-24: `984091f:js/main.js:871` `const TridiagX_BindGroup_BaseToA = create_Tridiag_BindGroup(device, TridiagX_uniformBuffer, coefMatx, txNewState, current_stateUVstar, newcoef_x, txtemp2_PCRx, txBottom);`<br>현재 대응 `js/main.js:1224` `const TridiagX_BindGroup_BaseToA = create_Tridiag_BindGroup(device, TridiagX_uniformBuffer, coefMatx, txNewState, current_stateUVstar, newcoef_x, txtemp2_PCRx, txBottom);`<br>두 파일 이력: L20. | 대상은 경계 uniform과 x PCR 교대 바인딩이다. 본판의 896c491·bb99fee·984091f 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 알고리즘·trough_factor·구면·시계열 uniform을 쓴다. 본판은 x PCR 계수 교대 바인드 그룹을 추가한다. 이 행의 판 차이 근거는 896c491·bb99fee·984091f의 본판 변경이다. |
| CT1 §5 | CT1-277 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1240` `const TridiagY_BindGroup_BaseToA = create_Tridiag_BindGroup(device, TridiagY_uniformBuffer, coefMaty, txNewState, current_stateUVstar, newcoef_y, txtemp2_PCRy, txBottom);`<br>변경 984091f 2026-05-24: `984091f:js/main.js:887` `const TridiagY_BindGroup_BaseToA = create_Tridiag_BindGroup(device, TridiagY_uniformBuffer, coefMaty, txNewState, current_stateUVstar, newcoef_y, txtemp2_PCRy, txBottom);`<br>두 파일 이력: L20. | 대상은 y PCR 교대 바인딩이다. 본판의 984091f 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 y 계수 교대 바인드 그룹을 만든다. transect 판은 y PCR을 실행하지 않지만 기본 바인드 그룹은 생성한다. 이 행의 판 차이 근거는 984091f의 본판 변경이다. |
| CT1 §5 | CT1-278 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1254` `const SedTrans_UpdateBottom_BindGroup = create_SedTrans_UpdateBottom_BindGroup(device, SedTrans_UpdateBottom_uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change, txHardBottom, txBottomInitial);`<br>현재 `transect_version/js/main.js:800` `const SedTrans_UpdateBottom_BindGroup = create_SedTrans_UpdateBottom_BindGroup(device, SedTrans_UpdateBottom_uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change);`<br>변경 852ec28 2025-06-13: `852ec28:js/main.js:815` `const SedTrans_UpdateBottom_BindGroup = create_SedTrans_UpdateBottom_BindGroup(device, SedTrans_UpdateBottom_uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change, txHardBottom, txBottomInitial);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:795` `const SedTrans_UpdateBottom_BindGroup = create_SedTrans_UpdateBottom_BindGroup(device, SedTrans_UpdateBottom_uniformBuffer, txBottom, txBotChange_Sed, erosion_Sed, depostion_Sed, txtemp_SedTrans_Botttom, txtemp_SedTrans_Change);`<br>두 파일 이력: L20. | 대상은 바닥 갱신 바인드 그룹이다. 본판의 852ec28 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 hardbottom과 초기 바닥고를 전달한다. 이 행의 판 차이 근거는 852ec28의 본판 변경이다. |
| CT1 §5 | CT1-279 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1266` `SedTrans_UpdateBottom_view.setInt32(36, calc_constants.west_boundary_type, true);       // i32`<br>변경 22e1983 2025-06-06: `22e1983:js/main.js:808` `SedTrans_UpdateBottom_view.setInt32(36, calc_constants.west_boundary_type, true);       // i32`<br>두 파일 이력: L20.<br>변경 전 입력 끝 `4fa700a:js/main.js:806` `SedTrans_UpdateBottom_view.setFloat32(32, calc_constants.sedC1_n, true);           // f32`<br><br>`4fa700a:js/main.js:808` `// Updateneardry -  Bindings & Uniforms Config`<br>변경 전 입력 끝 `22e1983:transect_version/js/main.js:806` `SedTrans_UpdateBottom_view.setFloat32(32, calc_constants.sedC1_n, true);           // f32`<br><br>`22e1983:transect_version/js/main.js:808` `// Updateneardry -  Bindings & Uniforms Config` | 대상은 바닥 갱신 경계 uniform이다. 본판의 22e1983 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. 22e1983은 본판을 수정하면서 수정 전 코드를 가진 transect 사본을 추가했다. | 본판은 22e1983에서 바닥 갱신의 경계 유형 입력을 추가했다. transect 판은 그 입력이 없는 코드를 보존한다. |
| CT1 §5 | CT1-280 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1297` `const CalcMeans_BindGroup = create_CalcMeans_BindGroup(device, CalcMeans_uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC, txNewState);`<br>현재 `transect_version/js/main.js:839` `const CalcMeans_BindGroup = create_CalcMeans_BindGroup(device, CalcMeans_uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC);`<br>변경 dc6cc2d 2025-08-10: `dc6cc2d:js/main.js:858` `const CalcMeans_BindGroup = create_CalcMeans_BindGroup(device, CalcMeans_uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC, txNewState);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:834` `const CalcMeans_BindGroup = create_CalcMeans_BindGroup(device, CalcMeans_uniformBuffer, txMeans, txMeans_Speed, txMeans_Momflux, txH, txU, txV, txBottom, txtemp_Means, txtemp_Means_Speed, txtemp_Means_Momflux, txModelVelocities, txC);`<br>두 파일 이력: L20. | 대상은 평균 수면 입력이다. 본판의 dc6cc2d 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 CalcMeans에 txNewState를 전달한다. 이 행의 판 차이 근거는 dc6cc2d의 본판 변경이다. |
| CT1 §5 | CT1-282 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1365` `MouseClickChange_view.setFloat32(52, calc_constants.designcomponent_Radius, true);             // f32`<br>현재 `transect_version/js/main.js:907` `MouseClickChange_view.setFloat32(52, calc_constants.designcomponent_Radius, true);             // f32`<br>변경 d778fe7 2026-06-02: `d778fe7:js/main.js:1106` `MouseClickChange_view.setFloat32(52, calc_constants.designcomponent_Radius, true);             // f32`<br>변경 397c575 2025-09-09: `397c575:js/main.js:932` `const ExtractTimeSeries_BindGroup = create_ExtractTimeSeries_BindGroup(device, ExtractTimeSeries_uniformBuffer, txBottom, txBottomFriction, txContSource, txState, txWaveHeight, txTimeSeries_Locations, txTimeSeries_Data, txMeans_Speed);`<br>현재 대응 `js/main.js:1383` `const ExtractTimeSeries_BindGroup = create_ExtractTimeSeries_BindGroup(device, ExtractTimeSeries_uniformBuffer, txBottom, txBottomFriction, txContSource, txState, txWaveHeight, txTimeSeries_Locations, txTimeSeries_Data, txMeans_Speed);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:902` `MouseClickChange_view.setFloat32(52, calc_constants.designcomponent_Radius, true);             // f32`<br>두 파일 이력: L20. | 대상은 선형 구조물 uniform과 툴팁 binding이다. 본판의 d778fe7·397c575 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 선형 구조물 오프셋 64–92를 갱신한다. 본판만 ExtractTimeSeries에 txMeans_Speed를 전달한다. 공백 차이는 물리 값을 바꾸지 않는다. 이 행의 판 차이 근거는 d778fe7·397c575의 본판 변경이다. |
| CT1 §5 | CT1-283 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1394` `ExtractTimeSeries_view.setFloat32(24, calc_constants.start_time_shift, true);             // f32, total_time`<br>현재 `transect_version/js/main.js:922` `ExtractTimeSeries_view.setFloat32(24, 0.0, true);             // f32, total_time`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:1393` `ExtractTimeSeries_view.setFloat32(24, calc_constants.start_time_shift, true);             // f32, total_time`<br>변경 397c575 2025-09-09: `397c575:js/main.js:943` `ExtractTimeSeries_view.setInt32(32, calc_constants.disturbanceType, true);             // i32`<br>현재 대응 `js/main.js:1396` `ExtractTimeSeries_view.setInt32(32, calc_constants.disturbanceType, true);             // i32`<br>변경 c4be488 2026-07-13: `c4be488:js/main.js:1400` `// const ExtractNestedBoundaryTimeSeries_uniforms = new ArrayBuffer(256);`<br>현재 대응 `js/main.js:1400` `// const ExtractNestedBoundaryTimeSeries_uniforms = new ArrayBuffer(256);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:917` `ExtractTimeSeries_view.setFloat32(24, 0.0, true);             // f32, total_time`<br>두 파일 이력: L20. | 대상은 시계열 시각과 중첩 추출 설정이다. 본판의 bb99fee·397c575·c4be488 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 시작 시각 이동을 점 시계열 uniform에 반영한다. 본판만 교란 유형과 중첩 경계 추출 레이아웃을 설정한다. transect 판은 시간 0에서 시작한다. 이 행의 판 차이 근거는 bb99fee·397c575·c4be488의 본판 변경이다. |
| CT1 §5 | CT1-284 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1451` `var RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);`<br>현재 `transect_version/js/main.js:962` `var RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);`<br>변경 8c2b62b 2025-08-24: `8c2b62b:js/main.js:981` `var RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, txBottomInitial, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:957` `var RenderBindGroup = createRenderBindGroup(device, Render_uniformBuffer, txNewState, txBottom, txMeans, txWaveHeight, txBaseline_WaveHeight, txBottomFriction, txNewState_Sed, erosion_Sed, txBotChange_Sed, txDesignComponents, txOverlayMap, txDraw, textureSampler, txTimeSeries_Locations, txBreaking, txSamplePNGs, textureSampler_linear, txRenderVarsf16);`<br>두 파일 이력: L20. | 대상은 render의 침식 입력 의미이다. 본판의 8c2b62b 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 erosion_Sed 자리의 리소스에 txBottomInitial을 전달한다. transect 판은 실제 erosion_Sed를 전달한다. 동일 binding의 의미를 두 판에서 혼용하면 안 된다. 이 행의 판 차이 근거는 8c2b62b의 본판 변경이다. |
| CT1 §5 | CT1-288 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1719` `let total_time = calc_constants.start_time_shift;          // Initialize time, which might be used for animations or simulations.`<br>현재 `transect_version/js/main.js:1215` `let total_time = 0;          // Initialize time, which might be used for animations or simulations.`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:1717` `let total_time = calc_constants.start_time_shift;          // Initialize time, which might be used for animations or simulations.`<br>변경 ebca435 2026-07-20: `ebca435:js/main.js:1730` `const useNestedPointTimeSeriesClock = calc_constants.west_boundary_type == 5 \|\|`<br>`ebca435:js/main.js:1731` `calc_constants.east_boundary_type == 5 \|\| calc_constants.south_boundary_type == 5 \|\|`<br>`ebca435:js/main.js:1732` `calc_constants.north_boundary_type == 5;`<br>현재 대응 `js/main.js:1730` `const useNestedPointTimeSeriesClock = calc_constants.west_boundary_type == 5 \|\|`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1210` `let total_time = 0;          // Initialize time, which might be used for animations or simulations.`<br>두 파일 이력: L20. | 대상은 시뮬레이션과 점 시계열 초기 시각이다. 본판의 bb99fee·ebca435 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 type5 시작 시각을 total_time에 더한다. 점 시계열은 일반 실행에서 0 기반을 유지하고 type5에서 절대 시각을 쓴다. transect 판은 두 시계를 0으로 둔다. 이 행의 판 차이 근거는 bb99fee·ebca435의 본판 변경이다. |
| CT1 §5 | CT1-289 | A 판 차이 | A 판 차이 | 현재 `js/main.js:1775` `async function uploadDrawOverlayCanvas() {`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:1763` `async function uploadDrawOverlayCanvas() {`<br>변경 c4be488 2026-07-13: `c4be488:js/main.js:1773` `const drawableRectangles = getNestedGridOutputDrawableRectangles();`<br>현재 대응 `js/main.js:1783` `const drawableRectangles = getNestedGridOutputDrawableRectangles();`<br>두 파일 이력: L20. | 대상은 중첩 경계 출력 실행 상태이다. 본판의 bb99fee·c4be488 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 사각형 표시·다중 상태·리소스 해제·인덱스 제한·별칭 설정 키·표본 수 제한·위치 좌표·uniform·시간별 캡처를 구현한다. 사각형마다 독립 시계를 쓴다. 출력 간격은 dt 이상으로 제한한다. GPU 텍스처 한도를 넘는 사각형은 건너뛴다. 전체 수집이 끝나면 다운로드한다. 이 행의 판 차이 근거는 bb99fee·c4be488의 본판 변경이다. |
| CT1 §5 | CT1-290 | A 판 차이 | A 판 차이 | 현재 `js/main.js:2219` `var nowFlush = Date.now();`<br>변경 7ae7da4 2026-02-23: `7ae7da4:js/main.js:1368` `var nowFlush = Date.now();`<br>두 파일 이력: L20. | 대상은 주기적 GPU 동기화이다. 본판의 7ae7da4 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 600000ms마다 onSubmittedWorkDone을 기다린다. transect 판에는 해당 운영 보정이 없다. 이 행의 판 차이 근거는 7ae7da4의 본판 변경이다. |
| CT1 §5 | CT1-291 | A 판 차이 | A 판 차이 | 현재 `js/main.js:2284` `runCopyTextures(device, calc_constants, txBottom, txBottomInitial)`<br>현재 `transect_version/js/main.js:1318` `runCopyTextures(device, commandEncoder, calc_constants, txBottom, txBottomInitial)`<br>변경 33f7ff6 2026-02-13: `33f7ff6:js/main.js:1413` `runCopyTextures(device, calc_constants, txBottom, txBottomInitial)`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:1699` `if (calc_constants.grid_type == 2) {`<br>현재 대응 `js/main.js:2298` `if (calc_constants.grid_type == 2) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1313` `runCopyTextures(device, commandEncoder, calc_constants, txBottom, txBottomInitial)`<br>두 파일 이력: L20. | 대상은 HTML 갱신 시 dt와 구면 모드이다. 본판의 33f7ff6·afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 복사 함수의 commandEncoder 인자만 다르다. 본판은 구면 모드·물리 격자간격·계량을 다시 계산한다. transect 판은 Cartesian CFL 식만 다시 계산한다. 이 행의 판 차이 근거는 33f7ff6·afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-292 | A 판 차이 | A 판 차이 | 현재 `js/main.js:2365` `Pass3_view.setFloat32(148, 1.0 / Math.max(calc_constants.R_earth, 1.0), true);       // f32`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:1766` `Pass3_view.setFloat32(148, 1.0 / Math.max(calc_constants.R_earth, 1.0), true);       // f32`<br>두 파일 이력: L20. | 대상은 지구 반지름 역수 갱신이다. 본판의 afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 HTML 변경 뒤 Pass3의 one_over_R을 갱신한다. 이 행의 판 차이 근거는 afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-294 | A 판 차이 | A 판 차이 | 현재 `js/main.js:2393` `calc_constants.north_boundary_type = 3;`<br>현재 `transect_version/js/main.js:1388` `calc_constants.north_boundary_type = 3;`<br>변경 9093d7f 2026-06-01: `9093d7f:js/main.js:1545` `calc_constants.north_boundary_type = 3;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1383` `calc_constants.north_boundary_type = 3;`<br>두 파일 이력: L20. | 대상은 경계 UI 파랑 재생성이다. 본판의 9093d7f 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 UI 변경에 맞춰 파랑 텍스처와 numberOfWaves uniform을 갱신한다. 양쪽은 주기 경계를 쌍으로 맞추는 호스트 코드를 유지한다. transect 셰이더는 주기 경계를 구현하지 않는다. 이 행의 판 차이 근거는 9093d7f의 본판 변경이다. |
| CT1 §5 | CT1-295 | A 판 차이 | A 판 차이 | 현재 `js/main.js:2411` `BoundaryPass_view.setInt32(176, calc_constants.grid_type, true);              // i32`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:2207` `BoundaryPass_view.setInt32(176, calc_constants.grid_type, true);              // i32`<br>두 파일 이력: L20. | 대상은 type5 위치·관측점 수 갱신이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 경계 원점과 4변 관측점 수를 다시 uniform에 쓴다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-298 | A 판 차이 | A 판 차이 | 현재 `js/main.js:2489` `if (calc_constants.nestedGridOutput_active == 1) {`<br>현재 `transect_version/js/main.js:1465` `update_colorbar(device, offscreenCanvas, ctx, calc_constants, txDraw, logo_left, logo_right) // update colorbar with new climits`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:2285` `if (calc_constants.nestedGridOutput_active == 1) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1460` `update_colorbar(device, offscreenCanvas, ctx, calc_constants, txDraw, logo_left, logo_right) // update colorbar with new climits`<br>두 파일 이력: L20. | 대상은 범례와 중첩 사각형 재표시이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 활성 중첩 사각형 유무에 따라 범례·윤곽 업로드를 await한다. transect 판은 기존 update_colorbar를 호출한다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-300 | A 판 차이 | A 판 차이 | 현재 `js/main.js:2598` `runComputeShader(device, AddDisturbance_uniformBuffer, AddDisturbance_uniforms, AddDisturbance_Pipeline, AddDisturbance_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // add impulse`<br>현재 `transect_version/js/main.js:1551` `runComputeShader(device, commandEncoder, AddDisturbance_uniformBuffer, AddDisturbance_uniforms, AddDisturbance_Pipeline, AddDisturbance_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // add impulse`<br>변경 33f7ff6 2026-02-13: `33f7ff6:js/main.js:1647` `runComputeShader(device, AddDisturbance_uniformBuffer, AddDisturbance_uniforms, AddDisturbance_Pipeline, AddDisturbance_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // add impulse`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:2401` `if (calc_constants.nestedGridOutput_trigger == 1) {`<br>현재 대응 `js/main.js:2605` `if (calc_constants.nestedGridOutput_trigger == 1) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1546` `runComputeShader(device, commandEncoder, AddDisturbance_uniformBuffer, AddDisturbance_uniforms, AddDisturbance_Pipeline, AddDisturbance_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);  // add impulse`<br>두 파일 이력: L20. | 대상은 교란 호출과 중첩 트리거이다. 본판의 33f7ff6·bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 즉시 submit 함수를 호출한다. 본판만 중첩 출력 트리거를 처리한다. 단면판은 commandEncoderStack 변수를 두지 않는다. 이 행의 판 차이 근거는 33f7ff6·bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-301 | A 판 차이 | A 판 차이 | 현재 `js/main.js:2624` `total_time = frame_count * calc_constants.dt + calc_constants.start_time_shift;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n`<br>현재 `transect_version/js/main.js:1568` `total_time = frame_count * calc_constants.dt;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:2420` `total_time = frame_count * calc_constants.dt + calc_constants.start_time_shift;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n`<br>변경 3646fc8 2026-02-08: `3646fc8:js/main.js:1660` `PassBreaking_view.setFloat32(36, total_time - calc_constants.dt, true);   //f32 - update time, minus dt as we are here finding dissipation at the previous time level`<br>현재 대응 `js/main.js:2628` `PassBreaking_view.setFloat32(36, total_time - calc_constants.dt, true);   //f32 - update time, minus dt as we are here finding dissipation at the previous time level`<br>변경 33f7ff6 2026-02-13: `33f7ff6:js/main.js:1674` `commandEncoderStack = device.createCommandEncoder();`<br>현재 대응 `js/main.js:2635` `commandEncoderStack = device.createCommandEncoder();`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1563` `total_time = frame_count * calc_constants.dt;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n`<br>두 파일 이력: L20. | 대상은 예측 단계 submit 묶음이다. 본판의 bb99fee·3646fc8·33f7ff6 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | Pass0→Pass1→선택 퇴적물 재구성→Pass2→쇄파→COULWAVE A/B 순서는 같다. transect 판은 매 호출을 submit한다. 본판은 encoder로 묶는다. 시간 uniform을 쓰는 위치는 바뀌지만 쇄파는 total_time-dt를 사용한다. 본판만 total_time에 시작 시각을 더한다. 이 행의 판 차이 근거는 bb99fee·3646fc8·33f7ff6의 본판 변경이다. |
| CT1 §5 | CT1-302 | A 판 차이 | A 판 차이 | 현재 `js/main.js:2676` `commandEncoderStack = device.createCommandEncoder();`<br>현재 `transect_version/js/main.js:1607` `runComputeShader(device, commandEncoder, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);`<br>변경 3646fc8 2026-02-08: `3646fc8:js/main.js:1706` `commandEncoderStack = device.createCommandEncoder();`<br>변경 984091f 2026-05-24: `984091f:js/main.js:1766` `TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, TridiagX_BindGroup_BaseToA, TridiagX_BindGroup_BToA, TridiagX_view,`<br>현재 대응 `js/main.js:2718` `TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, TridiagX_BindGroup_BaseToA, TridiagX_BindGroup_BToA, TridiagX_view,`<br>변경 7ae7da4 2026-02-23: `7ae7da4:js/main.js:1792` `if(calc_constants.disturbanceType == 5 && total_time <= 1.0e5 * calc_constants.dt) { // only add disturbance for first 100,000 time steps, to save some work`<br>현재 대응 `js/main.js:2739` `if(calc_constants.disturbanceType == 5 && total_time <= 1.0e5 * calc_constants.dt) { // only add disturbance for first 100,000 time steps, to save some work`<br>변경 33f7ff6 2026-02-13: `33f7ff6:js/main.js:1829` `runComputeShader(device, Pass3A_Coulwave_uniformBuffer, Pass3A_Coulwave_uniforms, Pass3A_Coulwave_Pipeline, Pass3A_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);`<br>현재 대응 `js/main.js:2796` `runComputeShader(device, Pass3A_Coulwave_uniformBuffer, Pass3A_Coulwave_uniforms, Pass3A_Coulwave_Pipeline, Pass3A_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1602` `runComputeShader(device, commandEncoder, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);`<br>두 파일 이력: L20. | 대상은 예측 적분·경계·PCR·사면 이동 순서이다. 본판의 3646fc8·984091f·7ae7da4·33f7ff6 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | Pass3→gradient 보관→퇴적물→경계→COULWAVE 계수→PCR→분산 모드 재경계 순서는 유지한다. 본판은 계수 교대 바인드 그룹을 전달한다. transect 판은 사면 이동을 시간 제한 없이 호출한다. 본판은 첫 1e5 스텝까지만 호출한다. corrector는 양쪽에서 timeScheme==2로 시작한다. 이 행의 판 차이 근거는 3646fc8·984091f·7ae7da4·33f7ff6의 본판 변경이다. |
| CT1 §5 | CT1-305 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3049` `RenderPass.draw(4);  // Draw the quad`<br>현재 `transect_version/js/main.js:1869` `RenderPass.draw(4);  // Draw the quad`<br>변경 590bda8 2026-06-01: `590bda8:js/main.js:2057` `RenderPass.draw(4);  // Draw the quad`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1864` `RenderPass.draw(4);  // Draw the quad`<br>두 파일 이력: L20. | 대상은 Design 모드 건물 footprint이다. 본판의 590bda8 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 JSON box 모델을 위에서 본 footprint로 표시한다. 본판은 범례와 로고 영역을 scissor로 보호한다. transect 판은 quad만 그린다. 이 행의 판 차이 근거는 590bda8의 본판 변경이다. |
| CT1 §5 | CT1-306 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3150` `const window_width  = (calc_constants.full_screen && !pseudoFullscreenActive) ? window.innerWidth  : canvas.width;`<br>현재 `transect_version/js/main.js:1880` `const window_width  = calc_constants.full_screen ? window.innerWidth  : canvas.width;`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:2071` `const window_width  = (calc_constants.full_screen && !pseudoFullscreenActive) ? window.innerWidth  : canvas.width;`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:2486` `const explorerMinCell = Math.max(Math.min(Math.abs(explorerCameraDx), Math.abs(explorerCameraDy)), 1.0e-6);`<br>현재 대응 `js/main.js:3160` `const explorerMinCell = Math.max(Math.min(Math.abs(explorerCameraDx), Math.abs(explorerCameraDy)), 1.0e-6);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1875` `const window_width  = calc_constants.full_screen ? window.innerWidth  : canvas.width;`<br>두 파일 이력: L20. | 대상은 카메라 투영 범위이다. 본판의 24b8f13·afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 가상 전체화면 크기와 구면 미터 척도를 반영한다. transect 판은 window 크기와 Cartesian dx·dy를 쓴다. fovY=45도는 같다. 이 행의 판 차이 근거는 24b8f13·afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-307 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3192` `const x = camState.position[0] / explorerCameraDx;`<br>현재 `transect_version/js/main.js:1913` `const x = camState.position[0] / calc_constants.dx;`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:2518` `const x = camState.position[0] / explorerCameraDx;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1908` `const x = camState.position[0] / calc_constants.dx;`<br>두 파일 이력: L20. | 대상은 카메라 바닥 보간 좌표이다. 본판의 afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 구면 미터 격자간격으로 카메라 위치를 인덱스화한다. transect 판은 dx·dy로 나눈다. Cartesian일 때 식은 같다. 이 행의 판 차이 근거는 afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-308 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3266` `deltaPanX * explorerSimDim`<br>현재 `transect_version/js/main.js:1985` `deltaPanX * simDim`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:2592` `deltaPanX * explorerSimDim`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:1980` `deltaPanX * simDim`<br>두 파일 이력: L20. | 대상은 카메라 좌우 이동 척도이다. 본판의 afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 explorerSimDim을 사용한다. transect 판은 simDim을 사용한다. Cartesian일 때 두 척도는 같다. 이 행의 판 차이 근거는 afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-309 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3283` `deltaPanY * explorerSimDim`<br>현재 `transect_version/js/main.js:2000` `deltaPanY * simDim`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:2609` `deltaPanY * explorerSimDim`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:2002` `deltaPanY * simDim`<br>두 파일 이력: L20. | 대상은 카메라 전후 이동 척도이다. 본판의 afc1fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 지면 잠금 여부와 무관하게 explorerSimDim을 사용한다. transect 판은 simDim을 사용한다. 이 행의 판 차이 근거는 afc1fe7의 본판 변경이다. |
| CT1 §5 | CT1-310 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3337` `if (calc_constants.grid_type == 2) {`<br>현재 `transect_version/js/main.js:2037` `const T_unskew = mat4.fromScaling(mat4.create(), [`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:2663` `if (calc_constants.grid_type == 2) {`<br>변경 f183cc2 2026-02-01: `f183cc2:js/main.js:2134` `// display current camera position, pitch, and yaw to the console`<br>현재 대응 `js/main.js:3366` `// display current camera position, pitch, and yaw to the console`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:2032` `const T_unskew = mat4.fromScaling(mat4.create(), [`<br>두 파일 이력: L20. | 대상은 카메라 model 행렬이다. 본판의 afc1fe7·f183cc2 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 구면에서 x·y 미터 변환을 적용한다. Cartesian 경로와 transect 판은 재척도*역척도인 항등 행렬이다. 제거된 카메라 로그는 본판에서도 주석이다. 이 행의 판 차이 근거는 afc1fe7·f183cc2의 본판 변경이다. |
| CT1 §5 | CT1-312 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3539` `calc_constants.elapsedTime = (now - startTime) / 1000.0;`<br>현재 `transect_version/js/main.js:2192` `calc_constants.elapsedTime = (now - startTime) / 1000;`<br>변경 a86f73a 2026-02-20: `a86f73a:js/main.js:2364` `calc_constants.elapsedTime = (now - startTime) / 1000.0;`<br>변경 0ee5174 2026-06-18: `0ee5174:js/main.js:2688` `calc_constants.elapsedTime = (now - startTime) / 1000.0;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:2187` `calc_constants.elapsedTime = (now - startTime) / 1000;`<br>두 파일 이력: L20. | 대상은 외부 제어 시간 진단이다. 본판의 a86f73a·0ee5174 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 agent_total_time·agent_total_time_since_http_update·실시간 배율을 노출한다. 1000과 1000.0의 밀리초 환산은 JS에서 같다. 이 행의 판 차이 근거는 a86f73a·0ee5174의 본판 변경이다. |
| CT1 §5 | CT1-313 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3620` `downloadTextureData(device, txNewState, 1, filename, readbackBuffer);  // last number is the channel 1 = .r, 2 = .g, etc.`<br>현재 `transect_version/js/main.js:2268` `downloadTextureData(device, txNewState, 1, filename);  // last number is the channel 1 = .r, 2 = .g, etc.`<br>변경 09cfd76 2026-02-15: `09cfd76:js/main.js:2438` `downloadTextureData(device, txNewState, 1, filename, readbackBuffer);  // last number is the channel 1 = .r, 2 = .g, etc.`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:2263` `downloadTextureData(device, txNewState, 1, filename);  // last number is the channel 1 = .r, 2 = .g, etc.`<br>두 파일 이력: L20. | 대상은 개별 표면 출력 버퍼이다. 본판의 09cfd76 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 13개 표면 선택의 텍스처·채널·파일명은 같다. 본판만 공용 readbackBuffer를 전달한다. 이 행의 판 차이 근거는 09cfd76의 본판 변경이다. |
| CT1 §5 | CT1-314 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3723` `{ tx: txBotChange_Sed,ch: 3, filename: 'current_SedTransDepthChange.bin'},`<br>현재 `transect_version/js/main.js:2374` `await downloadTextureData(device, tx, ch, filename);`<br>변경 fa47b72 2025-06-06: `fa47b72:js/main.js:2371` `{ tx: txBotChange_Sed,ch: 3, filename: 'current_SedTransDepthChange.bin'},`<br>변경 09cfd76 2026-02-15: `09cfd76:js/main.js:2545` `await downloadTextureData(device, tx, ch, filename, readbackBuffer);`<br>현재 대응 `js/main.js:3727` `await downloadTextureData(device, tx, ch, filename, readbackBuffer);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:2369` `await downloadTextureData(device, tx, ch, filename);`<br>두 파일 이력: L20. | 대상은 묶음 표면 출력이다. 본판의 fa47b72·09cfd76 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 current_SedTransDepthChange.bin을 중심 b 채널에서 출력한다. 공용 버퍼 인자 차이 외에 나머지 파일은 같다. 이 행의 판 차이 근거는 fa47b72·09cfd76의 본판 변경이다. |
| CT1 §5 | CT1-315 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3794` `await writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities,readbackBuffer);`<br>현재 `transect_version/js/main.js:2441` `await writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities);`<br>변경 09cfd76 2026-02-15: `09cfd76:js/main.js:2612` `await writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities,readbackBuffer);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:2436` `await writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities);`<br>두 파일 이력: L20. | 대상은 주기적 표면 출력 호출이다. 본판의 09cfd76 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 공용 readbackBuffer를 전달한다. 시간·프레임 번호·6개 텍스처 인자는 같다. 이 행의 판 차이 근거는 09cfd76의 본판 변경이다. |
| CT1 §5 | CT1-317 | A 판 차이 | A 판 차이 | 현재 `js/main.js:3931` `function getCanvasContentRect() {`<br>변경 0ee5174 2026-06-18: `0ee5174:js/main.js:3080` `function getCanvasContentRect() {`<br>변경 ff0d046 2026-07-07: `ff0d046:js/main.js:3734` `function getCanvasWorldCoordinates(event) {`<br>현재 대응 `js/main.js:3991` `function getCanvasWorldCoordinates(event) {`<br>변경 d778fe7 2026-06-02: `d778fe7:js/main.js:2995` `function getCanvasWorldCoordinates(event) {`<br>현재 대응 `js/main.js:3991` `function getCanvasWorldCoordinates(event) {`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:2772` `function getExplorerTouchGesture() {`<br>현재 대응 `js/main.js:4205` `function getExplorerTouchGesture() {`<br>두 파일 이력: L20. | 대상은 좌표 변환·선형 구조물·터치 helper이다. 본판의 0ee5174·ff0d046·d778fe7·24b8f13 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 object-fit 위치·표시 영역 검사·world 좌표·구면 상대/절대 좌표·선형 끝점 상태·양의 폭/경사 검사·두 손가락 중점과 거리를 구현한다. transect 판은 해당 함수가 없다. 이 행의 판 차이 근거는 0ee5174·ff0d046·d778fe7·24b8f13의 본판 변경이다. |
| CT1 §5 | CT1-318 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4232` `if (event.pointerType === 'touch' && calc_constants.viewType == 2) {`<br>현재 `transect_version/js/main.js:2578` `if (event.button === 0 && calc_constants.viewType == 1) { // Left mouse button, Design mode`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:2799` `if (event.pointerType === 'touch' && calc_constants.viewType == 2) {`<br>변경 d778fe7 2026-06-02: `d778fe7:js/main.js:3194` `} else if (event.button === 2 && calc_constants.viewType == 1 && calc_constants.whichPanelisOpen == 2) { // CODEX: Right-click stores the selected linear-structure endpoint in Design mode.`<br>현재 대응 `js/main.js:4269` `} else if (event.button === 2 && calc_constants.viewType == 1 && calc_constants.whichPanelisOpen == 2) { // CODEX: Right-click stores the selected linear-structure endpoint in Design mode.`<br>변경 0ee5174 2026-06-18: `0ee5174:js/main.js:3346` `if (agentDesignInteractionMode === "surface") {`<br>현재 대응 `js/main.js:4270` `if (agentDesignInteractionMode === "surface") {`<br>변경 ff0d046 2026-07-07: `ff0d046:js/main.js:4024` `syncTimeSeriesInputsFromSelectedLocation();`<br>현재 대응 `js/main.js:4281` `syncTimeSeriesInputsFromSelectedLocation();`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:2573` `if (event.button === 0 && calc_constants.viewType == 1) { // Left mouse button, Design mode`<br>두 파일 이력: L20. | 대상은 pointerdown 입력 경로이다. 본판의 24b8f13·d778fe7·0ee5174·ff0d046 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 한 손가락 회전·두 손가락 이동·Ctrl 좌클릭 회전·선형 끝점 우클릭·측정점 좌표 표시 동기화를 추가한다. transect 판은 기존 마우스 버튼 처리만 쓴다. 이 행의 판 차이 근거는 24b8f13·d778fe7·0ee5174·ff0d046의 본판 변경이다. |
| CT1 §5 | CT1-319 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4295` `if (event.pointerType === 'touch' && calc_constants.viewType == 2 && activeExplorerTouches.has(event.pointerId)) {`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:2855` `if (event.pointerType === 'touch' && calc_constants.viewType == 2 && activeExplorerTouches.has(event.pointerId)) {`<br>변경 62b1458 2026-05-24: `62b1458:js/main.js:2864` `const pinchDelta = touchGesture.distance - lastTouchDistance;`<br>현재 대응 `js/main.js:4304` `const pinchDelta = touchGesture.distance - lastTouchDistance;`<br>두 파일 이력: L20. | 대상은 pointermove 터치 동작이다. 본판의 24b8f13·62b1458 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 터치 한 손가락 회전과 두 손가락 pan·pinch를 처리한다. 수치 계산식은 바뀌지 않는다. 이 행의 판 차이 근거는 24b8f13·62b1458의 본판 변경이다. |
| CT1 §5 | CT1-320 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4361` `if (event.pointerType === 'touch' && calc_constants.viewType == 2) {`<br>현재 `transect_version/js/main.js:2635` `if (event.button === 0) { // Left mouse button`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:2918` `if (event.pointerType === 'touch' && calc_constants.viewType == 2) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:2630` `if (event.button === 0) { // Left mouse button`<br>두 파일 이력: L20. | 대상은 pointerup 정리이다. 본판의 24b8f13 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 터치 목록과 Ctrl 좌클릭 회전 상태까지 정리한다. transect 판은 좌·우 마우스 상태만 정리한다. 이 행의 판 차이 근거는 24b8f13의 본판 변경이다. |
| CT1 §5 | CT1-321 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4403` `activeExplorerTouches.delete(event.pointerId);`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:2960` `activeExplorerTouches.delete(event.pointerId);`<br>두 파일 이력: L20. | 대상은 pointercancel 터치 목록이다. 본판의 24b8f13 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 activeExplorerTouches에서 취소한 포인터를 제거한다. 이 행의 판 차이 근거는 24b8f13의 본판 변경이다. |
| CT1 §5 | CT1-324 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4563` `if (calc_constants.viewType == 1){`<br>현재 `transect_version/js/main.js:2776` `if (calc_constants.viewType == 1){`<br>변경 afc1fe7 2026-06-19: `afc1fe7:js/main.js:3784` `if (calc_constants.viewType == 1){`<br>변경 397c575 2025-09-09: `397c575:js/main.js:2805` `else if (calc_constants.disturbanceType > 1) {`<br>현재 대응 `js/main.js:4578` `else if (calc_constants.disturbanceType > 1) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:2771` `if (calc_constants.viewType == 1){`<br>두 파일 이력: L20. | 대상은 툴팁 단위와 교란 표시이다. 본판의 afc1fe7·397c575 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 구면 경위도 소수 6자리와 교란 시 최대수면을 표시한다. transect 판은 X/Y m 소수 2자리와 유의파고를 표시한다. 하천의 속력 표시는 유지한다. 이 행의 판 차이 근거는 afc1fe7·397c575의 본판 변경이다. |
| CT1 §5 | CT1-325 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4666` `updateLinearStructureLocationsDisplay();`<br>현재 `transect_version/js/main.js:2862` `}`<br>변경 d778fe7 2026-06-02: `d778fe7:js/main.js:3571` `updateLinearStructureLocationsDisplay();`<br>변경 ff0d046 2026-07-07: `ff0d046:js/main.js:4409` `updateLinearStructureLocationsDisplay();`<br>두 파일 이력: L20. | 대상은 UI 동기화 후처리이다. 본판의 d778fe7·ff0d046 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 선형 끝점 요약과 격자 유형별 측정점 좌표 입력을 동기화한다. 이 행의 판 차이 근거는 d778fe7·ff0d046의 본판 변경이다. |
| CT1 §5 | CT1-326 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4712` `{ id: 'designcomponent_CrestElev-button', input: 'designcomponent_CrestElev-input', property: 'designcomponent_CrestElev' },`<br>변경 d778fe7 2026-06-02: `d778fe7:js/main.js:3614` `{ id: 'designcomponent_CrestElev-button', input: 'designcomponent_CrestElev-input', property: 'designcomponent_CrestElev' },`<br>두 파일 이력: L20. | 대상은 선형 구조물 수치 버튼이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 천단고·폭·경사·양끝 좌표를 표준 update 버튼 목록에 넣는다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-327 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4730` `{ id: 'nestedGridOutput_i0-button', input: 'nestedGridOutput_i0-input', property: 'nestedGridOutput_i0' },`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:4395` `{ id: 'nestedGridOutput_i0-button', input: 'nestedGridOutput_i0-input', property: 'nestedGridOutput_i0' },`<br>두 파일 이력: L20. | 대상은 중첩 출력 수치 버튼이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 사각형 인덱스·출력 기간·간격·eta 임계값을 update 버튼 목록에 넣는다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-328 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4770` `{ input: 'designcomponent_CurrentEndPoint-select', property: 'designcomponent_CurrentEndPoint' },`<br>변경 d778fe7 2026-06-02: `d778fe7:js/main.js:3660` `{ input: 'designcomponent_CurrentEndPoint-select', property: 'designcomponent_CurrentEndPoint' },`<br>두 파일 이력: L20. | 대상은 선형 끝점 선택 목록이다. 본판의 d778fe7 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 시작점·끝점 선택을 calc_constants에 연결한다. 이 행의 판 차이 근거는 d778fe7의 본판 변경이다. |
| CT1 §5 | CT1-329 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4785` `installCelerisAgentControls({`<br>변경 0ee5174 2026-06-18: `0ee5174:js/main.js:3831` `installCelerisAgentControls({`<br>두 파일 이력: L20. | 대상은 외부 제어 설치이다. 본판의 0ee5174 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 installCelerisAgentControls에 수치 상태 조회·예제 실행·view 선택·전체화면 정리·설계 모드·선형 구조물 요청 callback을 전달한다. 이 행의 판 차이 근거는 0ee5174의 본판 변경이다. |
| CT1 §5 | CT1-330 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4858` `var pseudoFullscreenSavedStyle = null;`<br>현재 `transect_version/js/main.js:2994` `if (document.fullscreenElement) {`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:3336` `var pseudoFullscreenSavedStyle = null;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:2989` `if (document.fullscreenElement) {`<br>두 파일 이력: L20. | 대상은 전체화면 크기이다. 본판의 24b8f13 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 가상 전체화면과 visualViewport를 처리한다. transect 판은 실제 document.fullscreenElement만 처리한다. 이 행의 판 차이 근거는 24b8f13의 본판 변경이다. |
| CT1 §5 | CT1-331 | A 판 차이 | A 판 차이 | 현재 `js/main.js:4924` `function enterPseudoFullscreen() {`<br>현재 `transect_version/js/main.js:3046` `if (!document.fullscreenElement) {`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:3402` `function enterPseudoFullscreen() {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:3041` `if (!document.fullscreenElement) {`<br>두 파일 이력: L20. | 대상은 가상 전체화면 대체 경로이다. 본판의 24b8f13 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 실제 전체화면 미지원·거절 때 CSS 고정 화면을 쓴다. 종료 때 원래 inline style과 스크롤 상태를 복구한다. transect 판은 requestFullscreen 오류를 로그로만 남긴다. 이 행의 판 차이 근거는 24b8f13의 본판 변경이다. |
| CT1 §5 | CT1-332 | A 판 차이 | A 판 차이 | 현재 `js/main.js:5050` `var resizeCanvasTimer = null;`<br>현재 `transect_version/js/main.js:3065` `window.addEventListener('resize', resizeCanvas);`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:3528` `var resizeCanvasTimer = null;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:3060` `window.addEventListener('resize', resizeCanvas);`<br>두 파일 이력: L20. | 대상은 resize 이벤트 제한이다. 본판의 24b8f13 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 80ms debounce와 visualViewport resize·scroll을 사용한다. transect 판은 window resize마다 즉시 갱신한다. 이 행의 판 차이 근거는 24b8f13의 본판 변경이다. |
| CT1 §5 | CT1-333 | A 판 차이 | A 판 차이 | 현재 `js/main.js:5128` `calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].xts = timeSeriesDisplayToOffsetX(calc_constants.changeXTimeSeries);`<br>현재 `transect_version/js/main.js:3132` `calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].xts = calc_constants.changeXTimeSeries;`<br>변경 ff0d046 2026-07-07: `ff0d046:js/main.js:4871` `calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].xts = timeSeriesDisplayToOffsetX(calc_constants.changeXTimeSeries);`<br>변경 d778fe7 2026-06-02: `d778fe7:js/main.js:3989` `document.getElementById('designcomponent_xLoc-button').addEventListener('click', function () {`<br>현재 대응 `js/main.js:5144` `document.getElementById('designcomponent_xLoc-button').addEventListener('click', function () {`<br>변경 24b8f13 2026-05-24: `24b8f13:js/main.js:3620` `document.getElementById('viewType-select').addEventListener('change', function (event) {`<br>현재 대응 `js/main.js:5166` `document.getElementById('viewType-select').addEventListener('change', function (event) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:3127` `calc_constants.locationOfTimeSeries[calc_constants.changethisTimeSeries].xts = calc_constants.changeXTimeSeries;`<br>두 파일 이력: L20. | 대상은 측정점·선형 끝점·view 선택이다. 본판의 ff0d046·d778fe7·24b8f13 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 구면 표시 좌표를 상대좌표로 바꾼다. 본판만 선형 끝점 버튼을 연결한다. 본판은 view 선택 뒤 blur하여 문서 키보드 동작을 복구한다. 이 행의 판 차이 근거는 ff0d046·d778fe7·24b8f13의 본판 변경이다. |
| CT1 §5 | CT1-334 | A 판 차이 | A 판 차이 | 현재 `js/main.js:5243` `document.getElementById('startNestedGridOutput-button').addEventListener('click', function () {`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:4902` `document.getElementById('startNestedGridOutput-button').addEventListener('click', function () {`<br>두 파일 이력: L20. | 대상은 중첩 출력 시작 버튼이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 nestedGridOutput_trigger=1을 설정한다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-335 | A 판 차이 | A 판 차이 | 현재 `js/main.js:5276` `var etaInitialConditionFile = document.getElementById('etaInitialConditionFile').files[0];`<br>변경 32be94a 2025-10-16: `32be94a:js/main.js:3294` `var etaInitialConditionFile = document.getElementById('etaInitialConditionFile').files[0];`<br>변경 b8b50c3 2025-06-08: `b8b50c3:js/main.js:3265` `var hardbottomFile = document.getElementById('hardbottomFile').files[0];`<br>현재 대응 `js/main.js:5278` `var hardbottomFile = document.getElementById('hardbottomFile').files[0];`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:4937` `var hardbottomFile = document.getElementById('hardbottomFile').files[0];`<br>현재 대응 `js/main.js:5278` `var hardbottomFile = document.getElementById('hardbottomFile').files[0];`<br>두 파일 이력: L20. | 대상은 시작 시 선택 파일이다. 본판의 32be94a·b8b50c3·bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판만 초기 수면·hardbottom·4변 시계열 파일을 읽는다. transect 판은 config·bathy·waves·friction·overlay·model 파일을 읽는다. 이 행의 판 차이 근거는 32be94a·b8b50c3·bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-337 | A 판 차이 | A 판 차이 | 현재 `js/main.js:5324` `startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile);`<br>현재 `transect_version/js/main.js:3282` `startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile);`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:4983` `startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile);`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:3277` `startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile);`<br>두 파일 이력: L20. | 대상은 업로드 파랑 시작 인자이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 실제 파랑 업로드 경로에서 frictionFile을 전달한다. 본판은 초기 수면·hardbottom·4변 시계열 파일도 전달한다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-338 | A 판 차이 | A 판 차이 | 현재 `js/main.js:5338` `function startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile) {`<br>현재 `transect_version/js/main.js:3294` `function startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile) {`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:4997` `function startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:3289` `function startSimulationWithWave(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile) {`<br>두 파일 이력: L20. | 대상은 시작 함수 인자 목록이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판의 시작 함수는 6인자다. 본판은 추가 입력 파일을 포함한 13인자다. 이 행의 판 차이 근거는 bb99fee의 본판 변경이다. |
| CT1 §5 | CT1-339 | A 판 차이 | A 판 차이 | 현재 `js/main.js:5349` `initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile).catch(error => {`<br>현재 `transect_version/js/main.js:3303` `initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile).catch(error => {`<br>변경 bb99fee 2026-07-02: `bb99fee:js/main.js:5008` `initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, etaInitialConditionFile, frictionFile, hardbottomFile, westBoundaryTimeSeriesFile, eastBoundaryTimeSeriesFile, southBoundaryTimeSeriesFile, northBoundaryTimeSeriesFile).catch(error => {`<br>변경 f6fd78b 2026-06-04: `f6fd78b:js/main.js:4238` `loadAgentCaseFromUrl().then(function (started) {`<br>현재 대응 `js/main.js:5354` `loadAgentCaseFromUrl().then(function (started) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:3298` `initializeWebGPUApp(configContent, bathymetryContent, waveContent, OverlayFile, modelFile, frictionFile).catch(error => {`<br>두 파일 이력: L20. | 대상은 초기화 호출과 자동 시작이다. 본판의 bb99fee·f6fd78b 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | transect 판은 6인자를 초기화에 전달한다. 본판만 URL 케이스 자동 시작 뒤 5000ms 후 UI를 갱신한다. 이 행의 판 차이 근거는 bb99fee·f6fd78b의 본판 변경이다. |
| CT1 §5 | CT1-340 | A 판 차이 | A 판 차이 | 현재 `js/main.js:5459` `} else if (calc_constants.NumberOfTimeSeries > 0) {`<br>현재 `transect_version/js/main.js:3407` `} else {`<br>변경 dee0e14 2026-02-04: `dee0e14:js/main.js:3517` `} else if (calc_constants.NumberOfTimeSeries > 0) {`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:3402` `} else {`<br>두 파일 이력: L20. | 대상은 시계열 수 0일 때 chart 갱신이다. 본판의 dee0e14 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 NumberOfTimeSeries>0일 때만 기존 dataset을 갱신한다. transect 판은 무조건 else로 들어간다. 내부 timeSeriesData[index] 검사 때문에 이 차이만으로 잘못된 접근을 확정하지 않는다. 이 guard 변경은 ebca435의 epoch 수정과 구분한다. 이 행의 판 차이 근거는 dee0e14의 본판 변경이다. |
| CT1 §5 | CT1-341 | A 판 차이 | A 판 차이 | 현재 `js/main.js:5473` `timeseriesChart.options.scales.x.min = calc_constants.timeSeriesChartStartTime;`<br>현재 `transect_version/js/main.js:3418` `timeseriesChart.options.scales.x.max = calc_constants.maxdurationTimeSeries;`<br>변경 ebca435 2026-07-20: `ebca435:js/main.js:5473` `timeseriesChart.options.scales.x.min = calc_constants.timeSeriesChartStartTime;`<br>transect 22e1983 2025-06-06: `22e1983:transect_version/js/main.js:3413` `timeseriesChart.options.scales.x.max = calc_constants.maxdurationTimeSeries;`<br>두 파일 이력: L20. | 대상은 chart 시간축이다. 본판의 ebca435 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 시작 시각부터 시작 시각+기간까지 표시한다. transect 판은 최대값만 maxdurationTimeSeries로 둔다. 일반 0기반 실행에서는 같은 창이다. 이 행의 판 차이 근거는 ebca435의 본판 변경이다. |
| CT1 §5 | CT1-343 | A 판 차이 | A 판 차이 | 현재 `js/Handler_ExtractNestedBoundaryTimeSeries.js:3` `// Added by Codex: Start nested-grid boundary time-series extraction handler.`<br>변경 bb99fee 2026-07-02: `bb99fee:js/Handler_ExtractNestedBoundaryTimeSeries.js:3` `// Added by Codex: Start nested-grid boundary time-series extraction handler.`<br>transect 대응 경로 없음.<br>두 파일 이력: L07. | 대상은 js/Handler_ExtractNestedBoundaryTimeSeries.js이다. bb99fee가 현재 이름의 파일을 본판에 추가했다. transect 판에는 같은 경로가 없다. | js/Handler_ExtractNestedBoundaryTimeSeries.js는 bb99fee에서 본판에 추가된 파일이다. transect 판과의 차이는 해당 추가 시점에 따른 A 판 차이다. |
| CT1 §5 | CT1-344 | A 판 차이 | A 판 차이 | 현재 `js/Wave_Generator.js:44` `export function buildSineWaveData(calc_constants) {`<br>변경 9093d7f 2026-06-01: `9093d7f:js/Wave_Generator.js:44` `export function buildSineWaveData(calc_constants) {`<br>transect 대응 경로 없음.<br>두 파일 이력: L16. | 대상은 js/Wave_Generator.js이다. 9093d7f가 현재 이름의 파일을 본판에 추가했다. transect 판에는 같은 경로가 없다. | js/Wave_Generator.js는 9093d7f에서 본판에 추가된 파일이다. transect 판과의 차이는 해당 추가 시점에 따른 A 판 차이다. |
| CT1 §5 | CT1-345 | A 판 차이 | A 판 차이 | 현재 `js/agent_controls.js:820` `window.CelerisAgentControls = {`<br>변경 0ee5174 2026-06-18: `0ee5174:js/agent_controls.js:820` `window.CelerisAgentControls = {`<br>transect 대응 경로 없음.<br>두 파일 이력: L17. | 대상은 js/agent_controls.js이다. 0ee5174가 현재 이름의 파일을 본판에 추가했다. transect 판에는 같은 경로가 없다. | js/agent_controls.js는 0ee5174에서 본판에 추가된 파일이다. transect 판과의 차이는 해당 추가 시점에 따른 A 판 차이다. |
| CT1 §5 | CT1-346 | A 판 차이 | A 판 차이 | 현재 `shaders/ExtractNestedBoundaryTimeSeries.wgsl:23` `fn LoadState(i: i32, j: i32) -> vec4<f32> {`<br>변경 bb99fee 2026-07-02: `bb99fee:shaders/ExtractNestedBoundaryTimeSeries.wgsl:23` `fn LoadState(i: i32, j: i32) -> vec4<f32> {`<br>transect 대응 경로 없음.<br>두 파일 이력: L25. | 대상은 shaders/ExtractNestedBoundaryTimeSeries.wgsl이다. bb99fee가 현재 이름의 파일을 본판에 추가했다. transect 판에는 같은 경로가 없다. | shaders/ExtractNestedBoundaryTimeSeries.wgsl는 bb99fee에서 본판에 추가된 파일이다. transect 판과의 차이는 해당 추가 시점에 따른 A 판 차이다. |
| CT1 §5 | CT1-348 | A 판 차이 | A 판 차이 | 현재 `shaders/Pass2_HighOrder_HLLC.wgsl:71` `fn HLLC_Flux(`<br>변경 19b63cf 2025-11-07: `19b63cf:shaders/Pass2_HighOrder_HLLC.wgsl:71` `fn HLLC_Flux(`<br>`19b63cf:shaders/Pass2_HighOrder_HLLC.wgsl:72` `aplus:    f32,`<br>`19b63cf:shaders/Pass2_HighOrder_HLLC.wgsl:73` `aminus:   f32,`<br>`19b63cf:shaders/Pass2_HighOrder_HLLC.wgsl:74` `Fplus:    vec4<f32>,`<br>`19b63cf:shaders/Pass2_HighOrder_HLLC.wgsl:75` `Fminus:   vec4<f32>,`<br>`19b63cf:shaders/Pass2_HighOrder_HLLC.wgsl:76` `Uplus:    vec4<f32>,`<br>`19b63cf:shaders/Pass2_HighOrder_HLLC.wgsl:77` `Uminus:   vec4<f32>,`<br>`19b63cf:shaders/Pass2_HighOrder_HLLC.wgsl:78` `DU_flag:  i32`<br>`19b63cf:shaders/Pass2_HighOrder_HLLC.wgsl:79` `) -> vec4<f32> {`<br>transect 대응 경로 없음.<br>두 파일 이력: L29. | 대상은 shaders/Pass2_HighOrder_HLLC.wgsl이다. 19b63cf가 현재 이름의 파일을 본판에 추가했다. transect 판에는 같은 경로가 없다. | shaders/Pass2_HighOrder_HLLC.wgsl는 19b63cf에서 본판에 추가된 파일이다. transect 판과의 차이는 해당 추가 시점에 따른 A 판 차이다. |
| CT1 §5 | CT1-349 | A 판 차이 | A 판 차이 | 현재 `shaders/Pass2_HighOrder_HLLEM.wgsl:76` `/ denom;`<br>변경 19b63cf 2025-11-07: `19b63cf:shaders/Pass2_HighOrder_HLLEM.wgsl:73` `return (aplus * Fminus`<br>`19b63cf:shaders/Pass2_HighOrder_HLLEM.wgsl:74` `- aminus * Fplus`<br>`19b63cf:shaders/Pass2_HighOrder_HLLEM.wgsl:75` `+ aplus * aminus * DU)`<br>`19b63cf:shaders/Pass2_HighOrder_HLLEM.wgsl:76` `/ denom;`<br>transect 대응 경로 없음.<br>두 파일 이력: L30. | 대상은 shaders/Pass2_HighOrder_HLLEM.wgsl이다. 19b63cf가 현재 이름의 파일을 본판에 추가했다. transect 판에는 같은 경로가 없다. | shaders/Pass2_HighOrder_HLLEM.wgsl는 19b63cf에서 본판에 추가된 파일이다. transect 판과의 차이는 해당 추가 시점에 따른 A 판 차이다. |
| CT1 §5 | CT1-350 | A 판 차이 | A 판 차이 | 현재 `shaders/Pass3_NLSW_Spherical.wgsl:217` `let spherical_flux_divergence = (`<br>변경 afc1fe7 2026-06-19: `afc1fe7:shaders/Pass3_NLSW_Spherical.wgsl:217` `let spherical_flux_divergence = (`<br>`afc1fe7:shaders/Pass3_NLSW_Spherical.wgsl:218` `(xflux_west - xflux_here) * one_over_dlambda`<br>`afc1fe7:shaders/Pass3_NLSW_Spherical.wgsl:219` `+ (cos_phi_south_face * yflux_south - cos_phi_north_face * yflux_here) * one_over_dphi`<br>`afc1fe7:shaders/Pass3_NLSW_Spherical.wgsl:220` `) * inv_Rcos_phi;`<br>transect 대응 경로 없음.<br>두 파일 이력: L34. | 대상은 shaders/Pass3_NLSW_Spherical.wgsl이다. afc1fe7가 현재 이름의 파일을 본판에 추가했다. transect 판에는 같은 경로가 없다. | shaders/Pass3_NLSW_Spherical.wgsl는 afc1fe7에서 본판에 추가된 파일이다. transect 판과의 차이는 해당 추가 시점에 따른 A 판 차이다. |
| CT1 §5 | CT1-351 | A 판 차이 | A 판 차이 | 현재 `shaders/SedTrans_Pass3_old.wgsl:154` `let source_term = erosion - deposition;`<br>변경 a98bcc4 2025-06-09: `a98bcc4:shaders/SedTrans_Pass3_old.wgsl:154` `let source_term = erosion - deposition;`<br>transect 대응 경로 없음.<br>두 파일 이력: L36. | 대상은 shaders/SedTrans_Pass3_old.wgsl이다. a98bcc4가 현재 이름의 파일을 본판에 추가했다. transect 판에는 같은 경로가 없다. | shaders/SedTrans_Pass3_old.wgsl는 a98bcc4에서 본판에 추가된 파일이다. transect 판과의 차이는 해당 추가 시점에 따른 A 판 차이다. |
| CT1 §5 | CT1-353 | A 판 차이 | A 판 차이 | 현재 `shaders/SedTrans_UpdateBottom_testing.wgsl:77` `let B_here = B_initial; // + dB_cumulative;`<br>변경 4353b85 2025-06-09: `4353b85:shaders/SedTrans_UpdateBottom_testing.wgsl:77` `let B_here = B_initial; // + dB_cumulative;`<br>transect 대응 경로 없음.<br>두 파일 이력: L38. | 대상은 shaders/SedTrans_UpdateBottom_testing.wgsl이다. 4353b85가 현재 이름의 파일을 본판에 추가했다. transect 판에는 같은 경로가 없다. | shaders/SedTrans_UpdateBottom_testing.wgsl는 4353b85에서 본판에 추가된 파일이다. transect 판과의 차이는 해당 추가 시점에 따른 A 판 차이다. |
| CT1 §5 | CT1-354 | A 판 차이 | A 판 차이 | 현재 `shaders/fragment_testing.wgsl:864` `out.color = vec4<f32>(color_rgb, 1.0); // Normal shader output`<br>변경 f183cc2 2026-02-01: `f183cc2:shaders/fragment_testing.wgsl:864` `out.color = vec4<f32>(color_rgb, 1.0); // Normal shader output`<br>transect 대응 경로 없음.<br>두 파일 이력: L42. | 대상은 shaders/fragment_testing.wgsl이다. f183cc2가 현재 이름의 파일을 본판에 추가했다. transect 판에는 같은 경로가 없다. | shaders/fragment_testing.wgsl는 f183cc2에서 본판에 추가된 파일이다. transect 판과의 차이는 해당 추가 시점에 따른 A 판 차이다. |
| CT1 §5 | CT1-355 | A 판 차이 | A 판 차이 | `938a3bb1:models/Celeris/README.md:5` ``> ✅ **현재 상태(2026-06-15 전수조사 완료)**: Celeris-WebGPU 소스(`raw/source_code/Celeris-WebGPU/`, 35 JS + 42 WGSL) clone + **source-analysis 9 노트 + manual-notes 1 노트** 작성(모두 `file:line` 인용 verified). web-refs 1 + 정체카드도 verified.``<br>git ls-tree f6fd78b 집계: js/*.js 35개, shaders/*.wgsl 42개.<br>git ls-tree ebca435 집계: js/*.js 37개, shaders/*.wgsl 44개.<br>추가 0ee5174 2026-06-18: `0ee5174:js/agent_controls.js:820` `window.CelerisAgentControls = {`<br>두 경로 이력 L17.<br>추가 afc1fe7 2026-06-19: `afc1fe7:shaders/Pass3_NLSW_Spherical.wgsl:217` `let spherical_flux_divergence = (`<br>`afc1fe7:shaders/Pass3_NLSW_Spherical.wgsl:218` `(xflux_west - xflux_here) * one_over_dlambda`<br>`afc1fe7:shaders/Pass3_NLSW_Spherical.wgsl:219` `+ (cos_phi_south_face * yflux_south - cos_phi_north_face * yflux_here) * one_over_dphi`<br>`afc1fe7:shaders/Pass3_NLSW_Spherical.wgsl:220` `) * inv_Rcos_phi;`<br>두 경로 이력 L34.<br>추가 bb99fee 2026-07-02: `bb99fee:js/Handler_ExtractNestedBoundaryTimeSeries.js:3` `// Added by Codex: Start nested-grid boundary time-series extraction handler.`<br>두 경로 이력 L07.<br>추가 bb99fee 2026-07-02: `bb99fee:shaders/ExtractNestedBoundaryTimeSeries.wgsl:23` `fn LoadState(i: i32, j: i32) -> vec4<f32> {`<br>두 경로 이력 L25. | README의 마지막 변경은 위키 938a3bb1(2026-06-15)이다. 그날의 상류 최신 커밋 f6fd78b에는 실제로 JS 35개와 WGSL 42개가 있다. 후속 커밋은 JS 2개와 WGSL 2개를 추가했다. 보고서의 78개 경로는 일부 표시 셰이더를 제외하고 HTML과 compute 파일을 포함한 별도 범위다. | README의 35 JS·42 WGSL 집계는 2026-06-15 본판의 파일 수다. ebca435 본판의 같은 확장자 집계는 37 JS·44 WGSL이다. transect 대조의 78개 경로는 별도 집계 범위다. |
| CT1 §5 | CT1-373 | A 판 차이 | A 판 차이 | 현재 `shaders/Pass2.wgsl:190` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),`<br>현재 `transect_version/shaders/Pass2.wgsl:165` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east, h_here.y * u_here.y * c1_here.y, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),`<br>변경 b8b50c3 2025-06-08: `b8b50c3:shaders/Pass2.wgsl:190` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),`<br>두 파일 이력: L28.<br>동시 변경 `b8b50c3:shaders/Pass2.wgsl:186` `phix = 0.5;`<br>`b8b50c3:shaders/Pass2.wgsl:187` `phiy = 0.5;`<br><br>`b8b50c3:shaders/Pass2.wgsl:189` `let xflux_Sed = vec4<f32>(`<br>`b8b50c3:shaders/Pass2.wgsl:190` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),`<br>transect 순수 이류 `22e1983:transect_version/shaders/Pass2.wgsl:165` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east, h_here.y * u_here.y * c1_here.y, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),`<br>`22e1983:transect_version/shaders/Pass2.wgsl:166` `NumericalFlux(aplus, aminus, hW_east * uW_east * c2W_east, h_here.y * u_here.y * c2_here.y, phix * (hW_east * c2W_east - h_here.y * c2_here.y)),`<br>`22e1983:transect_version/shaders/Pass2.wgsl:167` `NumericalFlux(aplus, aminus, hW_east * uW_east * c3W_east, h_here.y * u_here.y * c3_here.y, phix * (hW_east * c3W_east - h_here.y * c3_here.y)),`<br>`22e1983:transect_version/shaders/Pass2.wgsl:168` `NumericalFlux(aplus, aminus, hW_east * uW_east * c4W_east, h_here.y * u_here.y * c4_here.y, phix * (hW_east * c4W_east - h_here.y * c4_here.y))`<br>`22e1983:transect_version/shaders/Pass2.wgsl:169` `);`<br> | 대상은 표준 Pass2의 퇴적물 확산과 phi이다. 본판의 b8b50c3 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 b8b50c3(2025-06-08)에서 표준 Pass2에 퇴적물 확산을 추가했다. 같은 커밋은 퇴적물 flux의 phix와 phiy를 0.5로 설정했다. transect 판은 이 변경 전의 flux를 보존한다. |
| CT1 §5 | CT1-376 | A 판 차이 | A 판 차이 | 현재 `shaders/BoundaryPass.wgsl:176` `num_waves = 5;`<br>현재 `transect_version/shaders/BoundaryPass.wgsl:165` `eta = eta * max(0.0, min(1.0, ((f32(num_waves) * period - t)/(period))));`<br>변경 bb99fee 2026-07-02: `bb99fee:shaders/BoundaryPass.wgsl:176` `num_waves = 5;`<br>두 파일 이력: L22.<br>현재 pulse 분기 `bb99fee:shaders/BoundaryPass.wgsl:174` `var num_waves = 0;`<br>`bb99fee:shaders/BoundaryPass.wgsl:175` `if (globals.incident_wave_type == 2){ // transient pulse`<br>`bb99fee:shaders/BoundaryPass.wgsl:176` `num_waves = 5;`<br>`bb99fee:shaders/BoundaryPass.wgsl:177` `if (eta < 0.0) {`<br>`bb99fee:shaders/BoundaryPass.wgsl:178` `eta = eta * globals.trough_factor;`<br>`bb99fee:shaders/BoundaryPass.wgsl:179` `}`<br>`bb99fee:shaders/BoundaryPass.wgsl:180` `eta = eta * max(0.0, min(1.0, ((f32(num_waves) * period - t)/(period))));`<br>`bb99fee:shaders/BoundaryPass.wgsl:181` `}`<br>transect pulse 분기 `22e1983:transect_version/shaders/BoundaryPass.wgsl:159` `}`<br>`22e1983:transect_version/shaders/BoundaryPass.wgsl:160` `if(num_waves > 0){`<br>`22e1983:transect_version/shaders/BoundaryPass.wgsl:161` `eta = eta * max(0.0, min(1.0, ((f32(num_waves) * period - t)/(period))));`<br>`22e1983:transect_version/shaders/BoundaryPass.wgsl:162` `}`<br>`22e1983:transect_version/shaders/BoundaryPass.wgsl:163` `let speed = globals.boundary_g * eta / (c * k) * tanh(k * d);`<br>`22e1983:transect_version/shaders/BoundaryPass.wgsl:164` `let hu = speed * cos(theta_mod);`<br>`22e1983:transect_version/shaders/BoundaryPass.wgsl:165` `// let hv = speed * sin(theta_mod);`<br>`22e1983:transect_version/shaders/BoundaryPass.wgsl:166` `let hv = 0.0;` | 대상은 pulse 지속 길이와 trough 배율이다. 본판의 bb99fee 변경 줄이 현재 본판에 남아 있다. 두 사본의 해당 줄은 서로 다르다. | 본판은 bb99fee(2026-07-02)에서 pulse를 4주기에서 5주기로 바꿨다. 같은 커밋은 음의 eta에 trough_factor를 곱하도록 바꿨다. transect 판은 이전 pulse를 보존한다. |

### A 행의 보충 원문

CT1-376의 transect 최초 사본은 다음 pulse 분기를 갖는다.

`22e1983:transect_version/shaders/BoundaryPass.wgsl:156` `var num_waves = 0;`

`22e1983:transect_version/shaders/BoundaryPass.wgsl:157` `if (globals.incident_wave_type == 2){ // transient pulse`

`22e1983:transect_version/shaders/BoundaryPass.wgsl:158` `num_waves = 4;`

`22e1983:transect_version/shaders/BoundaryPass.wgsl:159` `}`

`22e1983:transect_version/shaders/BoundaryPass.wgsl:160` `if(num_waves > 0){`

`22e1983:transect_version/shaders/BoundaryPass.wgsl:161` `eta = eta * max(0.0, min(1.0, ((f32(num_waves) * period - t)/(period))));`

`22e1983:transect_version/shaders/BoundaryPass.wgsl:162` `}`

### 두 사본의 파일별 이력

각 목록은 다음 읽기 명령의 출력이다.

`git -C models/Celeris/raw/source_code/Celeris-WebGPU log --follow --format='%h %ad %s' --date=short -- <파일>`

#### L01 index.html

`index.html`

```text
c4be488 2026-07-13 allow multiple nested grids
bb99fee 2026-07-02 Added grid nesting
afc1fe7 2026-06-19 Added Spherical NLSW Solver, Japan 2011 example
d778fe7 2026-06-02 Added linear structures functionality
9093d7f 2026-06-01 added ability to change wave conditions through the UI - on the Modify Boundary Conditions Panel
794c808 2026-04-06 updated forum link
ea93d70 2025-10-24 added Yakutat, Sebastian Inlet examples, and "p" for pause
32be94a 2025-10-16 hot start initial condition option added
146a4ac 2025-09-28 added Tracy Arm hot start
8c2b62b 2025-08-24 Added Tracy Arm Example, some landslide viz additions
853c27d 2025-08-11 added Endicott slide example
b8b50c3 2025-06-08 Sed Trans Updates
2a7452d 2025-06-07 Sed Trans updates
22e1983 2025-06-06 Sediment transport updates and transect model beta
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
bea2af6 2025-05-22 added Hermosa Beach w/ HO COULWAVE solution example
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
e239ace 2025-05-18 updates for user uploaded 2D friction map file
3551e59 2025-05-16 Update index.html
0b4e990 2025-05-16 Vector arrow overlay
ea37aaa 2025-05-15 Update index.html
f9c9eb4 2025-05-05 added 3D model forum link to htmls
e90945e 2025-05-05 loading box config file; initial attempts to integrate igTL models
d09410b 2025-04-24 max speed / flux calc corrections
34abfb1 2025-04-23 drone and render updates
b2d240f 2025-04-22 View Mode option text update
6ee7dc5 2025-04-16 touch screen updates
422f485 2025-03-04 integration of river model
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
950b3fd 2024-10-09 greenland umanak
28c22e7 2024-09-02 pre-release code update
10172d1 2024-07-08 Update index.html
1b1e7a3 2024-06-24 subaerial slide tsunami update
0f41edc 2024-06-19 Portage example / colorbar fix
52056eb 2024-06-11 Oceanside Example
040cfdf 2024-06-07 write write update
7f73bb4 2024-05-25 write update
275f624 2024-05-24 Update index.html
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
7f7d072 2024-05-16 new examples
c65b6f2 2024-05-07 Add files via upload
a338156 2024-05-07 Add files via upload
600104d 2024-05-04 Update index.html
7fb2c82 2024-05-03 console log redirect
a0a8a9c 2024-05-01 Guam add
944c34a 2024-04-29 new / updated examples
1783ba9 2024-04-29 Update index.html
9f84752 2024-04-26 New Examples
7915e97 2024-04-25 Update index.html
a9a18ea 2024-04-25 General Update / Fixes
48357ce 2024-04-23 Add files via upload
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
de9a1b6 2024-04-04 Add files via upload
efe44a2 2024-04-02 Add files via upload
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
6df8db9 2024-01-05 Add files via upload
b63de30 2024-01-05 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
677da5c 2023-10-29 Add files via upload
b274961 2023-10-27 Add files via upload
83c36ef 2023-10-27 Add files via upload
7aee944 2023-10-27 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/index.html`

```text
3d8a61b 2025-06-14 Added many-transect version
22e1983 2025-06-06 Sediment transport updates and transect model beta
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
bea2af6 2025-05-22 added Hermosa Beach w/ HO COULWAVE solution example
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
e239ace 2025-05-18 updates for user uploaded 2D friction map file
3551e59 2025-05-16 Update index.html
0b4e990 2025-05-16 Vector arrow overlay
ea37aaa 2025-05-15 Update index.html
f9c9eb4 2025-05-05 added 3D model forum link to htmls
e90945e 2025-05-05 loading box config file; initial attempts to integrate igTL models
d09410b 2025-04-24 max speed / flux calc corrections
34abfb1 2025-04-23 drone and render updates
b2d240f 2025-04-22 View Mode option text update
6ee7dc5 2025-04-16 touch screen updates
422f485 2025-03-04 integration of river model
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
950b3fd 2024-10-09 greenland umanak
28c22e7 2024-09-02 pre-release code update
10172d1 2024-07-08 Update index.html
1b1e7a3 2024-06-24 subaerial slide tsunami update
0f41edc 2024-06-19 Portage example / colorbar fix
52056eb 2024-06-11 Oceanside Example
040cfdf 2024-06-07 write write update
7f73bb4 2024-05-25 write update
275f624 2024-05-24 Update index.html
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
7f7d072 2024-05-16 new examples
c65b6f2 2024-05-07 Add files via upload
a338156 2024-05-07 Add files via upload
600104d 2024-05-04 Update index.html
7fb2c82 2024-05-03 console log redirect
a0a8a9c 2024-05-01 Guam add
944c34a 2024-04-29 new / updated examples
1783ba9 2024-04-29 Update index.html
9f84752 2024-04-26 New Examples
7915e97 2024-04-25 Update index.html
a9a18ea 2024-04-25 General Update / Fixes
48357ce 2024-04-23 Add files via upload
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
de9a1b6 2024-04-04 Add files via upload
efe44a2 2024-04-02 Add files via upload
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
6df8db9 2024-01-05 Add files via upload
b63de30 2024-01-05 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
677da5c 2023-10-29 Add files via upload
b274961 2023-10-27 Add files via upload
83c36ef 2023-10-27 Add files via upload
7aee944 2023-10-27 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L02 js/Copy_Data_to_Textures.js

`js/Copy_Data_to_Textures.js`

```text
bb99fee 2026-07-02 Added grid nesting
afc1fe7 2026-06-19 Added Spherical NLSW Solver, Japan 2011 example
ca9278e 2026-02-11 Update Copy_Data_to_Textures.js
25d9c56 2026-02-11 Update Copy_Data_to_Textures.js
151017f 2026-02-06 Fix GPU memory leak: destroy staging buffers after texture upload
32be94a 2025-10-16 hot start initial condition option added
b8b50c3 2025-06-08 Sed Trans Updates
67ca57c 2025-05-22 Added COULWAVE solver
e239ace 2025-05-18 updates for user uploaded 2D friction map file
0b4e990 2025-05-16 Vector arrow overlay
8892a96 2025-03-28 river sim updates
98f41c9 2024-04-18 Photo-realism update
efe44a2 2024-04-02 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
e9ad2fb 2023-10-09 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/Copy_Data_to_Textures.js`

```text
151017f 2026-02-06 Fix GPU memory leak: destroy staging buffers after texture upload
3d8a61b 2025-06-14 Added many-transect version
22e1983 2025-06-06 Sediment transport updates and transect model beta
67ca57c 2025-05-22 Added COULWAVE solver
e239ace 2025-05-18 updates for user uploaded 2D friction map file
0b4e990 2025-05-16 Vector arrow overlay
8892a96 2025-03-28 river sim updates
98f41c9 2024-04-18 Photo-realism update
efe44a2 2024-04-02 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
e9ad2fb 2023-10-09 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L03 js/File_Loader.js

`js/File_Loader.js`

```text
bb99fee 2026-07-02 Added grid nesting
bf8db50 2026-05-24 Localhost debug and overlay bug fixes
32be94a 2025-10-16 hot start initial condition option added
b8b50c3 2025-06-08 Sed Trans Updates
e239ace 2025-05-18 updates for user uploaded 2D friction map file
30be4e9 2025-04-29 added skybox
7fb2c82 2024-05-03 console log redirect
9f84752 2024-04-26 New Examples
a9a18ea 2024-04-25 General Update / Fixes
98f41c9 2024-04-18 Photo-realism update
0dd009e 2024-03-21 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
ff53b22 2023-10-26 Update File_Loader.js
2eb2866 2023-10-26 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/File_Loader.js`

```text
3d8a61b 2025-06-14 Added many-transect version
22e1983 2025-06-06 Sediment transport updates and transect model beta
e239ace 2025-05-18 updates for user uploaded 2D friction map file
30be4e9 2025-04-29 added skybox
7fb2c82 2024-05-03 console log redirect
9f84752 2024-04-26 New Examples
a9a18ea 2024-04-25 General Update / Fixes
98f41c9 2024-04-18 Photo-realism update
0dd009e 2024-03-21 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
ff53b22 2023-10-26 Update File_Loader.js
2eb2866 2023-10-26 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L04 js/File_Writer.js

`js/File_Writer.js`

```text
c4be488 2026-07-13 allow multiple nested grids
bb99fee 2026-07-02 Added grid nesting
9ed86a6 2026-02-17 Update File_Writer.js
09cfd76 2026-02-15 All 2D surface writes re-use the same buffer
b24af89 2026-02-10 More memory leak fixes
dee0e14 2026-02-04 clean up memory leaks
d852a23 2025-06-11 Update File_Writer.js
11b6bdc 2025-05-08 option to write u,v to write - not just P,Q
c54a721 2025-04-25 file write fixes
040cfdf 2024-06-07 write write update
7f73bb4 2024-05-25 write update
7542e27 2024-05-24 write file update
98f41c9 2024-04-18 Photo-realism update
efe44a2 2024-04-02 Add files via upload
85c2ca2 2024-03-19 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
```

`transect_version/js/File_Writer.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
11b6bdc 2025-05-08 option to write u,v to write - not just P,Q
c54a721 2025-04-25 file write fixes
040cfdf 2024-06-07 write write update
7f73bb4 2024-05-25 write update
7542e27 2024-05-24 write file update
98f41c9 2024-04-18 Photo-realism update
efe44a2 2024-04-02 Add files via upload
85c2ca2 2024-03-19 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
```


#### L05 js/Handler_CalcMeans.js

`js/Handler_CalcMeans.js`

```text
dc6cc2d 2025-08-10 update max free surface render
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
11b6bdc 2025-05-08 option to write u,v to write - not just P,Q
de0b465 2025-04-24 means calc update
e9c283b 2025-04-24 added max velocity and momentum flux surfaces
0e8b502 2023-10-31 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/Handler_CalcMeans.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
11b6bdc 2025-05-08 option to write u,v to write - not just P,Q
de0b465 2025-04-24 means calc update
e9c283b 2025-04-24 added max velocity and momentum flux surfaces
0e8b502 2023-10-31 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L06 js/Handler_Copytxf32_txf16.js

`js/Handler_Copytxf32_txf16.js`

```text
b8b50c3 2025-06-08 Sed Trans Updates
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
34abfb1 2025-04-23 drone and render updates
ebc98a5 2024-03-13 Add files via upload
0e8b502 2023-10-31 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/Handler_Copytxf32_txf16.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
34abfb1 2025-04-23 drone and render updates
ebc98a5 2024-03-13 Add files via upload
0e8b502 2023-10-31 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L07 js/Handler_ExtractNestedBoundaryTimeSeries.js

`js/Handler_ExtractNestedBoundaryTimeSeries.js`

```text
bb99fee 2026-07-02 Added grid nesting
```

`transect_version/js/Handler_ExtractNestedBoundaryTimeSeries.js`

git log 출력은 0행이다.


#### L08 js/Handler_ExtractTimeSeries.js

`js/Handler_ExtractTimeSeries.js`

```text
397c575 2025-09-09 Max fs to tooltip for slide sims
efe44a2 2024-04-02 Add files via upload
85c2ca2 2024-03-19 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/Handler_ExtractTimeSeries.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
efe44a2 2024-04-02 Add files via upload
85c2ca2 2024-03-19 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L09 js/Handler_Pass2.js

`js/Handler_Pass2.js`

```text
b8b50c3 2025-06-08 Sed Trans Updates
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/Handler_Pass2.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
fd57bb7 2023-10-09 Add files via upload
```


#### L10 js/Handler_Render.js

`js/Handler_Render.js`

```text
b8b50c3 2025-06-08 Sed Trans Updates
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
0b4e990 2025-05-16 Vector arrow overlay
34abfb1 2025-04-23 drone and render updates
d289986 2025-04-21 3D render view attempt updates
422f485 2025-03-04 integration of river model
0f41edc 2024-06-19 Portage example / colorbar fix
a9a18ea 2024-04-25 General Update / Fixes
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
efe44a2 2024-04-02 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
2eb2866 2023-10-26 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/Handler_Render.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
0b4e990 2025-05-16 Vector arrow overlay
34abfb1 2025-04-23 drone and render updates
d289986 2025-04-21 3D render view attempt updates
422f485 2025-03-04 integration of river model
0f41edc 2024-06-19 Portage example / colorbar fix
a9a18ea 2024-04-25 General Update / Fixes
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
efe44a2 2024-04-02 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
2eb2866 2023-10-26 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
fd57bb7 2023-10-09 Add files via upload
```


#### L11 js/Handler_SedTrans_Pass3.js

`js/Handler_SedTrans_Pass3.js`

```text
b8b50c3 2025-06-08 Sed Trans Updates
2a7452d 2025-06-07 Sed Trans updates
22e1983 2025-06-06 Sediment transport updates and transect model beta
85c2ca2 2024-03-19 Add files via upload
471c581 2024-01-04 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/Handler_SedTrans_Pass3.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
85c2ca2 2024-03-19 Add files via upload
471c581 2024-01-04 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
fd57bb7 2023-10-09 Add files via upload
```


#### L12 js/Handler_SedTrans_UpdateBottom.js

`js/Handler_SedTrans_UpdateBottom.js`

```text
852ec28 2025-06-13 sed trans fixes
4353b85 2025-06-09 Sed bugs / corrections
a98bcc4 2025-06-09 sed trans updates
85c2ca2 2024-03-19 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/Handler_SedTrans_UpdateBottom.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
85c2ca2 2024-03-19 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L13 js/Run_Compute_Shader.js

`js/Run_Compute_Shader.js`

```text
33f7ff6 2026-02-13 Further encoder streamline fixes
3646fc8 2026-02-08 Stacked Command Encoders
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/Run_Compute_Shader.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L14 js/Run_Tridiag_Solver.js

`js/Run_Tridiag_Solver.js`

```text
984091f 2026-05-24 Markdown and PCR ping-pong updates
33f7ff6 2026-02-13 Further encoder streamline fixes
471c581 2024-01-04 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
```

`transect_version/js/Run_Tridiag_Solver.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
471c581 2024-01-04 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
```


#### L15 js/Time_Series.js

`js/Time_Series.js`

```text
ebca435 2026-07-20 fixed time series write bug
dee0e14 2026-02-04 clean up memory leaks
e9d7122 2026-02-02 tooltip update
0af7673 2024-05-22 new examples
7f7d072 2024-05-16 new examples
366ee34 2024-04-08 photorealism update
efe44a2 2024-04-02 Add files via upload
```

`transect_version/js/Time_Series.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
0af7673 2024-05-22 new examples
7f7d072 2024-05-16 new examples
366ee34 2024-04-08 photorealism update
efe44a2 2024-04-02 Add files via upload
```


#### L16 js/Wave_Generator.js

`js/Wave_Generator.js`

```text
0ee5174 2026-06-18 CelerisAgent initial commit
9093d7f 2026-06-01 added ability to change wave conditions through the UI - on the Modify Boundary Conditions Panel
```

`transect_version/js/Wave_Generator.js`

git log 출력은 0행이다.


#### L17 js/agent_controls.js

`js/agent_controls.js`

```text
0ee5174 2026-06-18 CelerisAgent initial commit
```

`transect_version/js/agent_controls.js`

git log 출력은 0행이다.


#### L18 js/constants_load_calc.js

`js/constants_load_calc.js`

```text
ebca435 2026-07-20 fixed time series write bug
c4be488 2026-07-13 allow multiple nested grids
bb99fee 2026-07-02 Added grid nesting
afc1fe7 2026-06-19 Added Spherical NLSW Solver, Japan 2011 example
d778fe7 2026-06-02 Added linear structures functionality
9093d7f 2026-06-01 added ability to change wave conditions through the UI - on the Modify Boundary Conditions Panel
2e46d86 2026-04-20 Added examples for KB
f183cc2 2026-02-01 Added ability for user to specify initial 3D camera position
896c491 2026-01-17 added flags to test beta-level features in code
5a5603f 2026-01-15 Update constants_load_calc.js
35b7f1c 2026-01-15 addition of vorticity-based momentum mixing
ea93d70 2025-10-24 added Yakutat, Sebastian Inlet examples, and "p" for pause
32be94a 2025-10-16 hot start initial condition option added
146a4ac 2025-09-28 added Tracy Arm hot start
853c27d 2025-08-11 added Endicott slide example
3be651a 2025-06-11 small fixes
ba9eb67 2025-06-09 added bedload to bottom update equation
4353b85 2025-06-09 Sed bugs / corrections
a98bcc4 2025-06-09 sed trans updates
b8b50c3 2025-06-08 Sed Trans Updates
5c60ac0 2025-06-07 add sediment diffusion term
cb7001e 2025-06-06 Update constants_load_calc.js
22e1983 2025-06-06 Sediment transport updates and transect model beta
bea2af6 2025-05-22 added Hermosa Beach w/ HO COULWAVE solution example
67ca57c 2025-05-22 Added COULWAVE solver
e239ace 2025-05-18 updates for user uploaded 2D friction map file
0b4e990 2025-05-16 Vector arrow overlay
c0bfb59 2025-05-12 Update constants_load_calc.js
5902c7a 2025-05-12 accuracy mode edits
83dd100 2025-05-12 added 4th order reconstruction (Accuracy_mode = 1)
11b6bdc 2025-05-08 option to write u,v to write - not just P,Q
e90945e 2025-05-05 loading box config file; initial attempts to integrate igTL models
925b67e 2025-05-03 Added 3D box models for buildings
3a12949 2025-04-22 drone render updates
83cbac3 2025-04-22 drone view updates
ba4e12c 2025-04-22 drone render updates
18fa7ab 2025-04-11 moving depth (slide) additions
53ee4ca 2025-04-06 river updates
01c8b73 2025-04-06 river updates
39286cb 2025-03-30 automation working deploy
f18a0eb 2025-03-29 trigger updates
b83c9af 2025-03-29 trigger update
200ca81 2025-03-29 trigger - automation updates
8892a96 2025-03-28 river sim updates
5eaa968 2025-03-05 river integration
3872e7f 2025-02-09 Update constants_load_calc.js
2bf637e 2025-01-27 Update constants_load_calc.js
d4bea46 2025-01-27 River BC
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
950b3fd 2024-10-09 greenland umanak
1b1e7a3 2024-06-24 subaerial slide tsunami update
45107ff 2024-06-20 Update constants_load_calc.js
0f41edc 2024-06-19 Portage example / colorbar fix
52056eb 2024-06-11 Oceanside Example
040cfdf 2024-06-07 write write update
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
7f7d072 2024-05-16 new examples
7fb2c82 2024-05-03 console log redirect
a0a8a9c 2024-05-01 Guam add
9f84752 2024-04-26 New Examples
7f9c6aa 2024-04-25 Update constants_load_calc.js
a9a18ea 2024-04-25 General Update / Fixes
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
281fb9e 2024-04-04 Add files via upload
de9a1b6 2024-04-04 Add files via upload
efe44a2 2024-04-02 Add files via upload
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
83fd01d 2024-01-05 Add files via upload
9e694cd 2024-01-05 Add files via upload
b63de30 2024-01-05 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
677da5c 2023-10-29 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/constants_load_calc.js`

```text
3d8a61b 2025-06-14 Added many-transect version
22e1983 2025-06-06 Sediment transport updates and transect model beta
bea2af6 2025-05-22 added Hermosa Beach w/ HO COULWAVE solution example
67ca57c 2025-05-22 Added COULWAVE solver
e239ace 2025-05-18 updates for user uploaded 2D friction map file
0b4e990 2025-05-16 Vector arrow overlay
c0bfb59 2025-05-12 Update constants_load_calc.js
5902c7a 2025-05-12 accuracy mode edits
83dd100 2025-05-12 added 4th order reconstruction (Accuracy_mode = 1)
11b6bdc 2025-05-08 option to write u,v to write - not just P,Q
e90945e 2025-05-05 loading box config file; initial attempts to integrate igTL models
925b67e 2025-05-03 Added 3D box models for buildings
3a12949 2025-04-22 drone render updates
83cbac3 2025-04-22 drone view updates
ba4e12c 2025-04-22 drone render updates
18fa7ab 2025-04-11 moving depth (slide) additions
53ee4ca 2025-04-06 river updates
01c8b73 2025-04-06 river updates
39286cb 2025-03-30 automation working deploy
f18a0eb 2025-03-29 trigger updates
b83c9af 2025-03-29 trigger update
200ca81 2025-03-29 trigger - automation updates
8892a96 2025-03-28 river sim updates
5eaa968 2025-03-05 river integration
3872e7f 2025-02-09 Update constants_load_calc.js
2bf637e 2025-01-27 Update constants_load_calc.js
d4bea46 2025-01-27 River BC
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
950b3fd 2024-10-09 greenland umanak
1b1e7a3 2024-06-24 subaerial slide tsunami update
45107ff 2024-06-20 Update constants_load_calc.js
0f41edc 2024-06-19 Portage example / colorbar fix
52056eb 2024-06-11 Oceanside Example
040cfdf 2024-06-07 write write update
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
7f7d072 2024-05-16 new examples
7fb2c82 2024-05-03 console log redirect
a0a8a9c 2024-05-01 Guam add
9f84752 2024-04-26 New Examples
7f9c6aa 2024-04-25 Update constants_load_calc.js
a9a18ea 2024-04-25 General Update / Fixes
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
281fb9e 2024-04-04 Add files via upload
de9a1b6 2024-04-04 Add files via upload
efe44a2 2024-04-02 Add files via upload
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
83fd01d 2024-01-05 Add files via upload
9e694cd 2024-01-05 Add files via upload
b63de30 2024-01-05 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
677da5c 2023-10-29 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L19 js/display_parameters.js

`js/display_parameters.js`

```text
ff0d046 2026-07-07 time series plot updates for spherical grids
bb99fee 2026-07-02 Added grid nesting
7ae7da4 2026-02-23 Minor fixes - additional debug info, and landslide volume fix
dee0e14 2026-02-04 clean up memory leaks
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
5eaa968 2025-03-05 river integration
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
1b1e7a3 2024-06-24 subaerial slide tsunami update
7fb2c82 2024-05-03 console log redirect
efe44a2 2024-04-02 Add files via upload
85c2ca2 2024-03-19 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
677da5c 2023-10-29 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
```

`transect_version/js/display_parameters.js`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
5eaa968 2025-03-05 river integration
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
1b1e7a3 2024-06-24 subaerial slide tsunami update
7fb2c82 2024-05-03 console log redirect
efe44a2 2024-04-02 Add files via upload
85c2ca2 2024-03-19 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
677da5c 2023-10-29 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
```


#### L20 js/main.js

`js/main.js`

```text
ebca435 2026-07-20 fixed time series write bug
c4be488 2026-07-13 allow multiple nested grids
ff0d046 2026-07-07 time series plot updates for spherical grids
bb99fee 2026-07-02 Added grid nesting
afc1fe7 2026-06-19 Added Spherical NLSW Solver, Japan 2011 example
0ee5174 2026-06-18 CelerisAgent initial commit
f6fd78b 2026-06-04 Added "agent_case" automation helper
d778fe7 2026-06-02 Added linear structures functionality
9093d7f 2026-06-01 added ability to change wave conditions through the UI - on the Modify Boundary Conditions Panel
590bda8 2026-06-01 model plot update
62b1458 2026-05-24 Updated two-finger touch for ipad / iphone
24b8f13 2026-05-24 Add Mac / IPhone / IPad scene navigation support
bf8db50 2026-05-24 Localhost debug and overlay bug fixes
984091f 2026-05-24 Markdown and PCR ping-pong updates
c3c57a4 2026-03-03 fix last row vertex configuration to remove bottom pixel strand
7ae7da4 2026-02-23 Minor fixes - additional debug info, and landslide volume fix
f466786 2026-02-20 Update main.js
a86f73a 2026-02-20 more long sim "device lost" fix attempts
09cfd76 2026-02-15 All 2D surface writes re-use the same buffer
33f7ff6 2026-02-13 Further encoder streamline fixes
08860f0 2026-02-13 Reduced createRenderPipeline calls
7793a7e 2026-02-11 Update main.js
3c1649b 2026-02-11 added filled arrow for flow vectors
3646fc8 2026-02-08 Stacked Command Encoders
dee0e14 2026-02-04 clean up memory leaks
e9d7122 2026-02-02 tooltip update
769d990 2026-02-01 Update main.js
f183cc2 2026-02-01 Added ability for user to specify initial 3D camera position
ff720ca 2026-01-30 Update main.js
896c491 2026-01-17 added flags to test beta-level features in code
35b7f1c 2026-01-15 addition of vorticity-based momentum mixing
19b63cf 2025-11-07 convert Pass2 High-order to HLLC
ea93d70 2025-10-24 added Yakutat, Sebastian Inlet examples, and "p" for pause
32be94a 2025-10-16 hot start initial condition option added
146a4ac 2025-09-28 added Tracy Arm hot start
397c575 2025-09-09 Max fs to tooltip for slide sims
d23dfb0 2025-09-01 Small fixes
8c2b62b 2025-08-24 Added Tracy Arm Example, some landslide viz additions
dc6cc2d 2025-08-10 update max free surface render
852ec28 2025-06-13 sed trans fixes
7fa28e0 2025-06-12 bug fixes
1ce6bf7 2025-06-10 bug fix
ba9eb67 2025-06-09 added bedload to bottom update equation
4353b85 2025-06-09 Sed bugs / corrections
a98bcc4 2025-06-09 sed trans updates
c7fb523 2025-06-09 bugs
b8b50c3 2025-06-08 Sed Trans Updates
2a7452d 2025-06-07 Sed Trans updates
5c60ac0 2025-06-07 add sediment diffusion term
fa47b72 2025-06-06 Sed Trans Updates
22e1983 2025-06-06 Sediment transport updates and transect model beta
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
e239ace 2025-05-18 updates for user uploaded 2D friction map file
0b4e990 2025-05-16 Vector arrow overlay
c215adf 2025-05-12 Added HLLEM Flux Solver
5902c7a 2025-05-12 accuracy mode edits
83dd100 2025-05-12 added 4th order reconstruction (Accuracy_mode = 1)
37189b6 2025-05-08 Update main.js
11b6bdc 2025-05-08 option to write u,v to write - not just P,Q
61505f2 2025-05-08 river_sim initial camera position
f3d80f8 2025-05-07 Update main.js
e90945e 2025-05-05 loading box config file; initial attempts to integrate igTL models
925b67e 2025-05-03 Added 3D box models for buildings
30be4e9 2025-04-29 added skybox
c54a721 2025-04-25 file write fixes
c4cdf29 2025-04-25 Update main.js
8eeac64 2025-04-25 Update main.js
de0b465 2025-04-24 means calc update
d09410b 2025-04-24 max speed / flux calc corrections
e9c283b 2025-04-24 added max velocity and momentum flux surfaces
91a3d60 2025-04-23 drone view updates
34abfb1 2025-04-23 drone and render updates
3a12949 2025-04-22 drone render updates
83cbac3 2025-04-22 drone view updates
ba4e12c 2025-04-22 drone render updates
cebecb4 2025-04-21 drone render updates
d289986 2025-04-21 3D render view attempt updates
37057bf 2025-04-20 fly through view render changes
a403e11 2025-04-18 render updates for cases with dx ~= dy
6ee7dc5 2025-04-16 touch screen updates
18fa7ab 2025-04-11 moving depth (slide) additions
6df60fd 2025-04-10 Update main.js
c85b8c1 2025-04-10 Change "mouse" events to "pointer" events
01c8b73 2025-04-06 river updates
ede90ee 2025-03-30 Update main.js
f18a0eb 2025-03-29 trigger updates
b83c9af 2025-03-29 trigger update
200ca81 2025-03-29 trigger - automation updates
8892a96 2025-03-28 river sim updates
5eaa968 2025-03-05 river integration
422f485 2025-03-04 integration of river model
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
28c22e7 2024-09-02 pre-release code update
1b1e7a3 2024-06-24 subaerial slide tsunami update
0f41edc 2024-06-19 Portage example / colorbar fix
040cfdf 2024-06-07 write write update
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
7f7d072 2024-05-16 new examples
717cb5b 2024-05-03 Update main.js
7fb2c82 2024-05-03 console log redirect
a0a8a9c 2024-05-01 Guam add
9f84752 2024-04-26 New Examples
a9a18ea 2024-04-25 General Update / Fixes
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
281fb9e 2024-04-04 Add files via upload
6c28a9d 2024-04-04 Add files via upload
de9a1b6 2024-04-04 Add files via upload
efe44a2 2024-04-02 Add files via upload
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
9e694cd 2024-01-05 Add files via upload
6df8db9 2024-01-05 Add files via upload
b63de30 2024-01-05 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
677da5c 2023-10-29 Add files via upload
b274961 2023-10-27 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
bcca2ce 2023-10-24 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/js/main.js`

```text
3d8a61b 2025-06-14 Added many-transect version
22e1983 2025-06-06 Sediment transport updates and transect model beta
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
e239ace 2025-05-18 updates for user uploaded 2D friction map file
0b4e990 2025-05-16 Vector arrow overlay
c215adf 2025-05-12 Added HLLEM Flux Solver
5902c7a 2025-05-12 accuracy mode edits
83dd100 2025-05-12 added 4th order reconstruction (Accuracy_mode = 1)
37189b6 2025-05-08 Update main.js
11b6bdc 2025-05-08 option to write u,v to write - not just P,Q
61505f2 2025-05-08 river_sim initial camera position
f3d80f8 2025-05-07 Update main.js
e90945e 2025-05-05 loading box config file; initial attempts to integrate igTL models
925b67e 2025-05-03 Added 3D box models for buildings
30be4e9 2025-04-29 added skybox
c54a721 2025-04-25 file write fixes
c4cdf29 2025-04-25 Update main.js
8eeac64 2025-04-25 Update main.js
de0b465 2025-04-24 means calc update
d09410b 2025-04-24 max speed / flux calc corrections
e9c283b 2025-04-24 added max velocity and momentum flux surfaces
91a3d60 2025-04-23 drone view updates
34abfb1 2025-04-23 drone and render updates
3a12949 2025-04-22 drone render updates
83cbac3 2025-04-22 drone view updates
ba4e12c 2025-04-22 drone render updates
cebecb4 2025-04-21 drone render updates
d289986 2025-04-21 3D render view attempt updates
37057bf 2025-04-20 fly through view render changes
a403e11 2025-04-18 render updates for cases with dx ~= dy
6ee7dc5 2025-04-16 touch screen updates
18fa7ab 2025-04-11 moving depth (slide) additions
6df60fd 2025-04-10 Update main.js
c85b8c1 2025-04-10 Change "mouse" events to "pointer" events
01c8b73 2025-04-06 river updates
ede90ee 2025-03-30 Update main.js
f18a0eb 2025-03-29 trigger updates
b83c9af 2025-03-29 trigger update
200ca81 2025-03-29 trigger - automation updates
8892a96 2025-03-28 river sim updates
5eaa968 2025-03-05 river integration
422f485 2025-03-04 integration of river model
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
28c22e7 2024-09-02 pre-release code update
1b1e7a3 2024-06-24 subaerial slide tsunami update
0f41edc 2024-06-19 Portage example / colorbar fix
040cfdf 2024-06-07 write write update
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
7f7d072 2024-05-16 new examples
717cb5b 2024-05-03 Update main.js
7fb2c82 2024-05-03 console log redirect
a0a8a9c 2024-05-01 Guam add
9f84752 2024-04-26 New Examples
a9a18ea 2024-04-25 General Update / Fixes
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
281fb9e 2024-04-04 Add files via upload
6c28a9d 2024-04-04 Add files via upload
de9a1b6 2024-04-04 Add files via upload
efe44a2 2024-04-02 Add files via upload
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
9e694cd 2024-01-05 Add files via upload
6df8db9 2024-01-05 Add files via upload
b63de30 2024-01-05 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
677da5c 2023-10-29 Add files via upload
b274961 2023-10-27 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
bcca2ce 2023-10-24 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
3681fdc 2023-10-19 Delete js directory
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L21 shaders/AddDisturbance.wgsl

`shaders/AddDisturbance.wgsl`

```text
185e91c 2026-01-30 Update AddDisturbance.wgsl
4c903ea 2026-01-30 Update AddDisturbance.wgsl
c92521c 2026-01-30 Update AddDisturbance.wgsl
3425a4a 2026-01-30 Update AddDisturbance.wgsl
8c2b62b 2025-08-24 Added Tracy Arm Example, some landslide viz additions
4353b85 2025-06-09 Sed bugs / corrections
18fa7ab 2025-04-11 moving depth (slide) additions
7aefeb6 2024-10-10 Update AddDisturbance.wgsl
fd5a260 2024-10-08 Greenland Umanak scenario
1b1e7a3 2024-06-24 subaerial slide tsunami update
040cfdf 2024-06-07 write write update
281fb9e 2024-04-04 Add files via upload
de9a1b6 2024-04-04 Add files via upload
efe44a2 2024-04-02 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
```

`transect_version/shaders/AddDisturbance.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
18fa7ab 2025-04-11 moving depth (slide) additions
7aefeb6 2024-10-10 Update AddDisturbance.wgsl
fd5a260 2024-10-08 Greenland Umanak scenario
1b1e7a3 2024-06-24 subaerial slide tsunami update
040cfdf 2024-06-07 write write update
281fb9e 2024-04-04 Add files via upload
de9a1b6 2024-04-04 Add files via upload
efe44a2 2024-04-02 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
```


#### L22 shaders/BoundaryPass.wgsl

`shaders/BoundaryPass.wgsl`

```text
bb99fee 2026-07-02 Added grid nesting
89c9824 2026-03-04 slight beta change update
896c491 2026-01-17 added flags to test beta-level features in code
9a7c709 2025-11-27 Update BoundaryPass.wgsl
744c43a 2025-09-25 river updates
8c2b62b 2025-08-24 Added Tracy Arm Example, some landslide viz additions
faa12fa 2025-06-20 periodic bc update
c7fb523 2025-06-09 bugs
b8b50c3 2025-06-08 Sed Trans Updates
53ee4ca 2025-04-06 river updates
01c8b73 2025-04-06 river updates
8892a96 2025-03-28 river sim updates
8c34679 2025-03-25 river updates
3d938d1 2025-03-14 Update BoundaryPass.wgsl
5eaa968 2025-03-05 river integration
d4bea46 2025-01-27 River BC
b70eb47 2025-01-26 Update BoundaryPass.wgsl
4766ac1 2025-01-25 Periodic BC Examples added
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
ccdacc6 2024-09-02 Update BoundaryPass.wgsl
28c22e7 2024-09-02 pre-release code update
1b1e7a3 2024-06-24 subaerial slide tsunami update
040cfdf 2024-06-07 write write update
9f84752 2024-04-26 New Examples
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/shaders/BoundaryPass.wgsl`

```text
ac0e0a9 2025-06-14 transect updates
3d8a61b 2025-06-14 Added many-transect version
22e1983 2025-06-06 Sediment transport updates and transect model beta
53ee4ca 2025-04-06 river updates
01c8b73 2025-04-06 river updates
8892a96 2025-03-28 river sim updates
8c34679 2025-03-25 river updates
3d938d1 2025-03-14 Update BoundaryPass.wgsl
5eaa968 2025-03-05 river integration
d4bea46 2025-01-27 River BC
b70eb47 2025-01-26 Update BoundaryPass.wgsl
4766ac1 2025-01-25 Periodic BC Examples added
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
ccdacc6 2024-09-02 Update BoundaryPass.wgsl
28c22e7 2024-09-02 pre-release code update
1b1e7a3 2024-06-24 subaerial slide tsunami update
040cfdf 2024-06-07 write write update
9f84752 2024-04-26 New Examples
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
254d71c 2023-10-09 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L23 shaders/CalcMeans.wgsl

`shaders/CalcMeans.wgsl`

```text
dc6cc2d 2025-08-10 update max free surface render
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
a69bc15 2025-05-21 Update CalcMeans.wgsl
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
0b4e990 2025-05-16 Vector arrow overlay
11b6bdc 2025-05-08 option to write u,v to write - not just P,Q
de0b465 2025-04-24 means calc update
18275a3 2025-04-24 Update CalcMeans.wgsl
76f8b85 2025-04-24 Update CalcMeans.wgsl
4168d69 2025-04-24 Update CalcMeans.wgsl
c481579 2025-04-24 Update CalcMeans.wgsl
d09410b 2025-04-24 max speed / flux calc corrections
e9c283b 2025-04-24 added max velocity and momentum flux surfaces
ebc98a5 2024-03-13 Add files via upload
0e8b502 2023-10-31 Add files via upload
```

`transect_version/shaders/CalcMeans.wgsl`

```text
4dc20a1 2026-01-27 transect updates
22e1983 2025-06-06 Sediment transport updates and transect model beta
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
a69bc15 2025-05-21 Update CalcMeans.wgsl
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
0b4e990 2025-05-16 Vector arrow overlay
11b6bdc 2025-05-08 option to write u,v to write - not just P,Q
de0b465 2025-04-24 means calc update
18275a3 2025-04-24 Update CalcMeans.wgsl
76f8b85 2025-04-24 Update CalcMeans.wgsl
4168d69 2025-04-24 Update CalcMeans.wgsl
c481579 2025-04-24 Update CalcMeans.wgsl
d09410b 2025-04-24 max speed / flux calc corrections
e9c283b 2025-04-24 added max velocity and momentum flux surfaces
ebc98a5 2024-03-13 Add files via upload
0e8b502 2023-10-31 Add files via upload
```


#### L24 shaders/Copytxf32_txf16.wgsl

`shaders/Copytxf32_txf16.wgsl`

```text
dc6cc2d 2025-08-10 update max free surface render
b8b50c3 2025-06-08 Sed Trans Updates
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
34abfb1 2025-04-23 drone and render updates
```

`transect_version/shaders/Copytxf32_txf16.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
34abfb1 2025-04-23 drone and render updates
```


#### L25 shaders/ExtractNestedBoundaryTimeSeries.wgsl

`shaders/ExtractNestedBoundaryTimeSeries.wgsl`

```text
bb99fee 2026-07-02 Added grid nesting
```

`transect_version/shaders/ExtractNestedBoundaryTimeSeries.wgsl`

git log 출력은 0행이다.


#### L26 shaders/ExtractTimeSeries.wgsl

`shaders/ExtractTimeSeries.wgsl`

```text
397c575 2025-09-09 Max fs to tooltip for slide sims
5eaa968 2025-03-05 river integration
0af7673 2024-05-22 new examples
7f7d072 2024-05-16 new examples
efe44a2 2024-04-02 Add files via upload
```

`transect_version/shaders/ExtractTimeSeries.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
5eaa968 2025-03-05 river integration
0af7673 2024-05-22 new examples
7f7d072 2024-05-16 new examples
efe44a2 2024-04-02 Add files via upload
```


#### L27 shaders/MouseClickChange.wgsl

`shaders/MouseClickChange.wgsl`

```text
d778fe7 2026-06-02 Added linear structures functionality
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
```

`transect_version/shaders/MouseClickChange.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
```


#### L28 shaders/Pass2.wgsl

`shaders/Pass2.wgsl`

```text
b8b50c3 2025-06-08 Sed Trans Updates
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
b63de30 2024-01-05 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/shaders/Pass2.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
b63de30 2024-01-05 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
fd57bb7 2023-10-09 Add files via upload
```


#### L29 shaders/Pass2_HighOrder_HLLC.wgsl

`shaders/Pass2_HighOrder_HLLC.wgsl`

```text
19b63cf 2025-11-07 convert Pass2 High-order to HLLC
b8b50c3 2025-06-08 Sed Trans Updates
fa47b72 2025-06-06 Sed Trans Updates
67ca57c 2025-05-22 Added COULWAVE solver
c215adf 2025-05-12 Added HLLEM Flux Solver
```

`transect_version/shaders/Pass2_HighOrder_HLLC.wgsl`

git log 출력은 0행이다.


#### L30 shaders/Pass2_HighOrder_HLLEM.wgsl

`shaders/Pass2_HighOrder_HLLEM.wgsl`

```text
19b63cf 2025-11-07 convert Pass2 High-order to HLLC
b8b50c3 2025-06-08 Sed Trans Updates
fa47b72 2025-06-06 Sed Trans Updates
67ca57c 2025-05-22 Added COULWAVE solver
c215adf 2025-05-12 Added HLLEM Flux Solver
```

`transect_version/shaders/Pass2_HighOrder_HLLEM.wgsl`

git log 출력은 0행이다.


#### L31 shaders/Pass3_Bous.wgsl

`shaders/Pass3_Bous.wgsl`

```text
35b7f1c 2026-01-15 addition of vorticity-based momentum mixing
67ca57c 2025-05-22 Added COULWAVE solver
18fa7ab 2025-04-11 moving depth (slide) additions
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
f18955b 2024-10-01 Update Pass3_Bous.wgsl
1b1e7a3 2024-06-24 subaerial slide tsunami update
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
f8092b5 2024-04-04 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/shaders/Pass3_Bous.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
67ca57c 2025-05-22 Added COULWAVE solver
18fa7ab 2025-04-11 moving depth (slide) additions
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
f18955b 2024-10-01 Update Pass3_Bous.wgsl
1b1e7a3 2024-06-24 subaerial slide tsunami update
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
f8092b5 2024-04-04 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L32 shaders/Pass3_COULWAVE.wgsl

`shaders/Pass3_COULWAVE.wgsl`

```text
35b7f1c 2026-01-15 addition of vorticity-based momentum mixing
67ca57c 2025-05-22 Added COULWAVE solver
0b4e990 2025-05-16 Vector arrow overlay
18fa7ab 2025-04-11 moving depth (slide) additions
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
f18955b 2024-10-01 Update Pass3_Bous.wgsl
1b1e7a3 2024-06-24 subaerial slide tsunami update
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
f8092b5 2024-04-04 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/shaders/Pass3_COULWAVE.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
67ca57c 2025-05-22 Added COULWAVE solver
0b4e990 2025-05-16 Vector arrow overlay
18fa7ab 2025-04-11 moving depth (slide) additions
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
f18955b 2024-10-01 Update Pass3_Bous.wgsl
1b1e7a3 2024-06-24 subaerial slide tsunami update
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
f8092b5 2024-04-04 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L33 shaders/Pass3_NLSW.wgsl

`shaders/Pass3_NLSW.wgsl`

```text
35b7f1c 2026-01-15 addition of vorticity-based momentum mixing
67ca57c 2025-05-22 Added COULWAVE solver
18fa7ab 2025-04-11 moving depth (slide) additions
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
f8092b5 2024-04-04 Add files via upload
de9a1b6 2024-04-04 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/shaders/Pass3_NLSW.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
67ca57c 2025-05-22 Added COULWAVE solver
18fa7ab 2025-04-11 moving depth (slide) additions
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
f8092b5 2024-04-04 Add files via upload
de9a1b6 2024-04-04 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L34 shaders/Pass3_NLSW_Spherical.wgsl

`shaders/Pass3_NLSW_Spherical.wgsl`

```text
afc1fe7 2026-06-19 Added Spherical NLSW Solver, Japan 2011 example
35b7f1c 2026-01-15 addition of vorticity-based momentum mixing
67ca57c 2025-05-22 Added COULWAVE solver
18fa7ab 2025-04-11 moving depth (slide) additions
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
7542e27 2024-05-24 write file update
0af7673 2024-05-22 new examples
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
f8092b5 2024-04-04 Add files via upload
de9a1b6 2024-04-04 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
2eb2866 2023-10-26 Add files via upload
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/shaders/Pass3_NLSW_Spherical.wgsl`

git log 출력은 0행이다.


#### L35 shaders/SedTrans_Pass3.wgsl

`shaders/SedTrans_Pass3.wgsl`

```text
852ec28 2025-06-13 sed trans fixes
ba9eb67 2025-06-09 added bedload to bottom update equation
e54def4 2025-06-08 Update SedTrans_Pass3.wgsl
b8b50c3 2025-06-08 Sed Trans Updates
2a7452d 2025-06-07 Sed Trans updates
5c60ac0 2025-06-07 add sediment diffusion term
a435dd4 2025-06-07 Update SedTrans_Pass3.wgsl
fa47b72 2025-06-06 Sed Trans Updates
22e1983 2025-06-06 Sediment transport updates and transect model beta
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
```

`transect_version/shaders/SedTrans_Pass3.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
```


#### L36 shaders/SedTrans_Pass3_old.wgsl

`shaders/SedTrans_Pass3_old.wgsl`

```text
a98bcc4 2025-06-09 sed trans updates
e54def4 2025-06-08 Update SedTrans_Pass3.wgsl
b8b50c3 2025-06-08 Sed Trans Updates
2a7452d 2025-06-07 Sed Trans updates
5c60ac0 2025-06-07 add sediment diffusion term
a435dd4 2025-06-07 Update SedTrans_Pass3.wgsl
fa47b72 2025-06-06 Sed Trans Updates
22e1983 2025-06-06 Sediment transport updates and transect model beta
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
```

`transect_version/shaders/SedTrans_Pass3_old.wgsl`

git log 출력은 0행이다.


#### L37 shaders/SedTrans_UpdateBottom.wgsl

`shaders/SedTrans_UpdateBottom.wgsl`

```text
852ec28 2025-06-13 sed trans fixes
4353b85 2025-06-09 Sed bugs / corrections
a98bcc4 2025-06-09 sed trans updates
22e1983 2025-06-06 Sediment transport updates and transect model beta
85c2ca2 2024-03-19 Add files via upload
```

`transect_version/shaders/SedTrans_UpdateBottom.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
85c2ca2 2024-03-19 Add files via upload
```


#### L38 shaders/SedTrans_UpdateBottom_testing.wgsl

`shaders/SedTrans_UpdateBottom_testing.wgsl`

```text
4353b85 2025-06-09 Sed bugs / corrections
a98bcc4 2025-06-09 sed trans updates
22e1983 2025-06-06 Sediment transport updates and transect model beta
85c2ca2 2024-03-19 Add files via upload
```

`transect_version/shaders/SedTrans_UpdateBottom_testing.wgsl`

git log 출력은 0행이다.


#### L39 shaders/TriDiag_PCRx.wgsl

`shaders/TriDiag_PCRx.wgsl`

```text
984091f 2026-05-24 Markdown and PCR ping-pong updates
366ee34 2024-04-08 photorealism update
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
```

`transect_version/shaders/TriDiag_PCRx.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
366ee34 2024-04-08 photorealism update
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
```


#### L40 shaders/TriDiag_PCRy.wgsl

`shaders/TriDiag_PCRy.wgsl`

```text
984091f 2026-05-24 Markdown and PCR ping-pong updates
366ee34 2024-04-08 photorealism update
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
```

`transect_version/shaders/TriDiag_PCRy.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
366ee34 2024-04-08 photorealism update
cf9de63 2023-10-24 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
```


#### L41 shaders/fragment.wgsl

`shaders/fragment.wgsl`

```text
d778fe7 2026-06-02 Added linear structures functionality
3c1649b 2026-02-11 added filled arrow for flow vectors
d23dfb0 2025-09-01 Small fixes
8c2b62b 2025-08-24 Added Tracy Arm Example, some landslide viz additions
3d8a61b 2025-06-14 Added many-transect version
7fa28e0 2025-06-12 bug fixes
3be651a 2025-06-11 small fixes
b8b50c3 2025-06-08 Sed Trans Updates
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
0b4e990 2025-05-16 Vector arrow overlay
8317d6e 2025-05-06 Update fragment.wgsl
74b1a7d 2025-05-06 Update fragment.wgsl
60b932d 2025-05-05 breaking updates
34abfb1 2025-04-23 drone and render updates
8892a96 2025-03-28 river sim updates
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
28c22e7 2024-09-02 pre-release code update
1b1e7a3 2024-06-24 subaerial slide tsunami update
0f41edc 2024-06-19 Portage example / colorbar fix
a9a18ea 2024-04-25 General Update / Fixes
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
efe44a2 2024-04-02 Add files via upload
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/shaders/fragment.wgsl`

```text
22e1983 2025-06-06 Sediment transport updates and transect model beta
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
0b4e990 2025-05-16 Vector arrow overlay
8317d6e 2025-05-06 Update fragment.wgsl
74b1a7d 2025-05-06 Update fragment.wgsl
60b932d 2025-05-05 breaking updates
34abfb1 2025-04-23 drone and render updates
8892a96 2025-03-28 river sim updates
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
28c22e7 2024-09-02 pre-release code update
1b1e7a3 2024-06-24 subaerial slide tsunami update
0f41edc 2024-06-19 Portage example / colorbar fix
a9a18ea 2024-04-25 General Update / Fixes
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
efe44a2 2024-04-02 Add files via upload
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```


#### L42 shaders/fragment_testing.wgsl

`shaders/fragment_testing.wgsl`

```text
f183cc2 2026-02-01 Added ability for user to specify initial 3D camera position
d23dfb0 2025-09-01 Small fixes
8c2b62b 2025-08-24 Added Tracy Arm Example, some landslide viz additions
3d8a61b 2025-06-14 Added many-transect version
7fa28e0 2025-06-12 bug fixes
3be651a 2025-06-11 small fixes
b8b50c3 2025-06-08 Sed Trans Updates
4fa700a 2025-05-31 Display updates - added mean vorticity to display options
67ca57c 2025-05-22 Added COULWAVE solver
094fc2e 2025-05-19 Added 4th-order MUSCL-TVD to Pass1_High_Order
0b4e990 2025-05-16 Vector arrow overlay
8317d6e 2025-05-06 Update fragment.wgsl
74b1a7d 2025-05-06 Update fragment.wgsl
60b932d 2025-05-05 breaking updates
34abfb1 2025-04-23 drone and render updates
8892a96 2025-03-28 river sim updates
38a5072 2025-01-21 Added periodic bc and proper rendering for configs with dx~=dy
28c22e7 2024-09-02 pre-release code update
1b1e7a3 2024-06-24 subaerial slide tsunami update
0f41edc 2024-06-19 Portage example / colorbar fix
a9a18ea 2024-04-25 General Update / Fixes
1dffd9d 2024-04-19 SRL update
98f41c9 2024-04-18 Photo-realism update
366ee34 2024-04-08 photorealism update
efe44a2 2024-04-02 Add files via upload
0dd009e 2024-03-21 Add files via upload
85c2ca2 2024-03-19 Add files via upload
ebc98a5 2024-03-13 Add files via upload
471c581 2024-01-04 Add files via upload
0e8b502 2023-10-31 Add files via upload
9c5b1a6 2023-10-27 Add files via upload
2eb2866 2023-10-26 Add files via upload
63a12e3 2023-10-19 Add files via upload
5fe6e6b 2023-10-19 Delete shaders directory
6f1272f 2023-10-19 Add files via upload
fd57bb7 2023-10-09 Add files via upload
```

`transect_version/shaders/fragment_testing.wgsl`

git log 출력은 0행이다.


## 3 B 행 판정 표

위키 노트의 문서 시점은 위키 git에서 그 파일을 마지막으로 변경한 커밋이다.
상류 HTML의 문서 시점은 상류 git에서 그 파일을 마지막으로 변경한 커밋이다.
문서 시점의 상류 스냅샷은 그 시점까지의 최신 커밋이다.
2026-09-20과 2026-09-21의 상류 최신 커밋은 모두 ebca435(2026-07-20)이다.
노트의 본문 작성일인 2026-06-15의 상류 최신 커밋은 f6fd78b(2026-06-04)이다.

| 보고서 | 행 ID | 원 결론 | 확정 결론 | 근거 커밋·행 | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|
| CT1 §5 | CT1-363 | B 문서 오기 | B 문서 오기 | `caf75a25:models/Celeris/source-analysis/celeris-sediment.md:104` ``수평 난류확산(`sedTurbDispersion` 배경 + `sedBreakingDispersionCoef`×breaking eddy viscosity) 코드는 `SedTrans_Pass3.wgsl:102-119`에 **전부 주석처리**되어 있음. 즉 현재 활성 빌드는 **이류 + 픽업/침강만**, 명시적 확산 없음. config 키(`sedTurbDispersion=0.01`, `sedBreakingDispersionCoef=0.1`, `constants_load_calc.js:112-113`)는 uniform으로 전달되나 셰이더에서 미사용.``<br>문서 마지막 변경: `caf75a25 2026-09-21`<br>문서 시점의 표준 경로 `ebca435:js/main.js:1545` `var Pass2_ShaderCode = null;`<br>`ebca435:js/main.js:1546` `if (calc_constants.Accuracy_mode == 1) {`<br>`ebca435:js/main.js:1547` `console.log("Using HLLC Flux Solver in Pass2");`<br>`ebca435:js/main.js:1548` `Pass2_ShaderCode = await fetchShader('/shaders/Pass2_HighOrder_HLLC.wgsl');`<br>`ebca435:js/main.js:1549` `} else {`<br>`ebca435:js/main.js:1550` `Pass2_ShaderCode = await fetchShader('/shaders/Pass2.wgsl');`<br>`ebca435:js/main.js:1551` `}`<br>문서 시점의 확산식 `ebca435:shaders/Pass2.wgsl:190` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),`<br>문서 시점의 y 확산식 `ebca435:shaders/Pass2.wgsl:197` `NumericalFlux(bplus, bminus, hS_north * c1S_north * vS_north - k_north * hS_north * C1y_north, h_here.x * c1_here.x * v_here.x - k_south * h_here.x * C1y_south, phiy * (hS_north * c1S_north - h_here.x * c1_here.x)),`<br>변경 b8b50c3 2025-06-08: <br>`b8b50c3:shaders/Pass2.wgsl:141` `let k_here =  globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, idx, 0).y;`<br>`b8b50c3:shaders/Pass2.wgsl:190` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),`<br>본문 작성일의 스냅샷 `f6fd78b:shaders/Pass2.wgsl:190` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),`<br>현재 `shaders/Pass2.wgsl:190` `NumericalFlux(aplus, aminus, hW_east * uW_east * c1W_east - k_east * hW_east * C1x_east, h_here.y * u_here.y * c1_here.y  - k_west * h_here.y * C1x_west, phix * (hW_east * c1W_east - h_here.y * c1_here.y)),` | 노트의 마지막 변경 시점에도 표준 Pass2는 class 1 flux에 확산항을 넣었다. 이 확산항은 본문 작성일보다 앞선 b8b50c3에서 추가되었다. SedTrans_Pass3의 주석 처리 사실을 전체 활성 경로에 적용한 문장은 문서 시점에도 틀렸다. | 본판 표준 Pass2의 class 1 flux에는 배경 확산과 쇄파 확산이 활성화되어 있다. SedTrans_Pass3 안의 주석 처리된 확산 대안과 구분한다. |
| CT1 §5 | CT1-368 | B 문서 오기 | B 문서 오기 | `7c34b6a2:models/Celeris/source-analysis/celeris-render.md:34` ``fragment·vertex3D는 이후 `txRenderVarsf16`를 layer index로 sample (예: 유속은 layer 1, 세굴심도는 layer 2).``<br>문서 마지막 변경: `7c34b6a2 2026-09-20`<br>같은 문서의 반대 서술 `7c34b6a2:models/Celeris/source-analysis/celeris-render.md:79` ``정점 버퍼의 `pos`(vec2)를 `uv=pos*0.5+0.5`로 변환, `etaTexture.r`를 `textureLoad`로 읽어 elevation 취득, world좌표 `(uv.x·(W-1)·dx, uv.y·(H-1)·dy, elev·renderZScale)`를 `viewProj` 카메라행렬로 clip 변환 (`shaders/vertex3D.wgsl:71-85`). 즉 시뮬 수면을 그대로 3D 높이장 메시로 들어올린다. fragment는 2D `fragment.wgsl` 재사용(Explorer 3D view).``<br>문서 시점의 코드 `ebca435:shaders/vertex3D.wgsl:77` `//let elev = textureSampleLevel(txRenderVarsf16, textureSampler_linear, out.uv, 0, 0.0).r;`<br>`ebca435:shaders/vertex3D.wgsl:78` `var elev = textureLoad(etaTexture, vec2<i32>(i32(out.uv.x * f32(globals.WIDTH - 1)), i32(out.uv.y * f32(globals.HEIGHT - 1))), 0).r;`<br><br>`ebca435:shaders/vertex3D.wgsl:80` `let worldX = out.uv.x * f32(globals.WIDTH - 1)  * globals.dx;`<br>`ebca435:shaders/vertex3D.wgsl:81` `let worldY = out.uv.y * f32(globals.HEIGHT - 1) * globals.dy;`<br>변경 7fa28e0 2025-06-12: `7fa28e0:shaders/vertex3D.wgsl:77` `//let elev = textureSampleLevel(txRenderVarsf16, textureSampler_linear, out.uv, 0, 0.0).r;`<br>`7fa28e0:shaders/vertex3D.wgsl:78` `var elev = textureLoad(etaTexture, vec2<i32>(i32(out.uv.x * f32(globals.WIDTH - 1)), i32(out.uv.y * f32(globals.HEIGHT - 1))), 0).r;`<br>본문 작성일의 코드 `f6fd78b:shaders/vertex3D.wgsl:78` `var elev = textureLoad(etaTexture, vec2<i32>(i32(out.uv.x * f32(globals.WIDTH - 1)), i32(out.uv.y * f32(globals.HEIGHT - 1))), 0).r;`<br>현재 `shaders/vertex3D.wgsl:78` `var elev = textureLoad(etaTexture, vec2<i32>(i32(out.uv.x * f32(globals.WIDTH - 1)), i32(out.uv.y * f32(globals.HEIGHT - 1))), 0).r;` | 본판 vertex3D는 7fa28e0에서 etaTexture의 textureLoad로 바뀌었다. 이 변경은 본문 작성일보다 앞선다. 같은 노트 79행은 이 동작을 맞게 적었다. 노트 34행의 vertex3D 설명은 문서 시점의 코드와도 모순한다. | 본판 vertex3D는 etaTexture에서 수면 고도를 읽는다. transect vertex3D의 f16 샘플링과 구분한다. |
| CT1 §5 | CT1-377 | B 문서 오기 | B 문서 오기 | 문서 마지막 변경: `c4be488 2026-07-13`<br>`c4be488:index.html:766` `<option value="2">*Transient Pulse (4 waves)</option>`<br>같은 문서 시점의 코드 `c4be488:shaders/BoundaryPass.wgsl:174` `var num_waves = 0;`<br>`c4be488:shaders/BoundaryPass.wgsl:175` `if (globals.incident_wave_type == 2){ // transient pulse`<br>`c4be488:shaders/BoundaryPass.wgsl:176` `num_waves = 5;`<br>`c4be488:shaders/BoundaryPass.wgsl:177` `if (eta < 0.0) {`<br>`c4be488:shaders/BoundaryPass.wgsl:178` `eta = eta * globals.trough_factor;`<br>`c4be488:shaders/BoundaryPass.wgsl:179` `}`<br>`c4be488:shaders/BoundaryPass.wgsl:180` `eta = eta * max(0.0, min(1.0, ((f32(num_waves) * period - t)/(period))));`<br>`c4be488:shaders/BoundaryPass.wgsl:181` `}`<br>실제 변경 bb99fee 2026-07-02: `bb99fee:shaders/BoundaryPass.wgsl:175` `if (globals.incident_wave_type == 2){ // transient pulse`<br>`bb99fee:shaders/BoundaryPass.wgsl:176` `num_waves = 5;`<br>`bb99fee:shaders/BoundaryPass.wgsl:177` `if (eta < 0.0) {`<br>`bb99fee:shaders/BoundaryPass.wgsl:178` `eta = eta * globals.trough_factor;`<br>`bb99fee:shaders/BoundaryPass.wgsl:179` `}`<br>`bb99fee:shaders/BoundaryPass.wgsl:180` `eta = eta * max(0.0, min(1.0, ((f32(num_waves) * period - t)/(period))));`<br>현재 `index.html:766` `<option value="2">*Transient Pulse (4 waves)</option>`<br>현재 `shaders/BoundaryPass.wgsl:176` `num_waves = 5;` | 본판 pulse의 5주기 변경은 bb99fee이다. index.html의 마지막 변경은 그 뒤인 c4be488이다. c4be488의 HTML은 4 waves를 표시하지만 같은 커밋의 셰이더는 5주기를 사용한다. 지정한 문서 시점 규칙에 따라 B를 유지한다. | 본판 HTML의 4 waves 표시는 문서 오기다. 본판 pulse 구현은 bb99fee 이후 5주기다. |

## 4 D 행 판정 표

대상 보고서 5절에는 D 행이 없다.
행 ID를 기준으로 센 D 행 수는 0개다.
원문 근거는 `_staging/recovery/compare/celeris-transect-vs-main.md:15901` `이 보고서에는 D 판정이 없다.`이다.
D 행에 대응하는 검색어는 없다.
D 행의 git log -S 검색 결과 목록은 빈 목록이다.

| 보고서 | 행 ID | 원 결론 | 확정 결론 | 근거 커밋·행 | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|

A 확정 167, B→A 0, D→A 0, 그 밖 재분류 1
