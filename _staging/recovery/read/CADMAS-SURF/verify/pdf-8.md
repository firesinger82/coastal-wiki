# CADMAS-SURF PDF 판독 기록 전수 대조 — pdf-8

검증일은 2026-11-04이다.
대상 원본은 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf`이다.
대상 기록은 `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf/p127-144.md`이다.
대조 범위는 PDF p.127–144이다.
지정된 300 dpi PNG 18개를 이미지 보기 도구로 모두 직접 열었다.
대조한 쪽 수는 대상 기록의 p.127–144 행을 기준으로 18쪽이다.
고친 쪽 수는 내용 변경이 있는 행을 기준으로 15쪽이다.
원본 해상도로 다시 확인한 부분은 p.131의 계수·제한식·주석, p.140의 정의식, p.142의 전체 표, p.144의 입력 형식·변수 정의·위상 조건이다.
확대 이미지는 메모리에서 표시했다.
추가 이미지 파일은 만들지 않았다.
텍스트 추출본은 p.131·135·136·143·144의 철자 확인에만 참고했다.
판독 판단은 쪽 이미지를 기준으로 했다.
이 범위에는 그림이 없다.
이 범위의 표에는 표 번호와 별도 캡션이 없다.
입력 키워드, 변수 이름, 형, 단위, 기본값, 제한식, 예시 수치를 쪽별로 대조했다.
p.129의 일본어 제목 두 개는 기존 원문 인용과 한국어 뜻이 이미지와 일치했다.
기존 frontmatter는 유지했다.
frontmatter에는 요청된 `verified_by` 한 줄만 추가했다.
쪽별 기록 표는 기존 18행을 유지했다.
열지 못한 이미지는 없다.

쪽별 집계는 서로 겹치지 않는다.
정정과 보완이 함께 있는 p.131과 p.140은 집계에서 정정으로 센다.
두 행 끝에는 정정 표지와 보완 표지를 함께 붙였다.
아래 목록의 항목 수는 쪽 수와 다르다.

| 쪽 | 판정 |
|---|---|
| p.127 | 보완 |
| p.128 | 보완 |
| p.129 | 보완 |
| p.130 | 보완 |
| p.131 | 정정 및 보완 |
| p.132 | 일치 |
| p.133 | 일치 |
| p.134 | 보완 |
| p.135 | 보완 |
| p.136 | 보완 |
| p.137 | 보완 |
| p.138 | 보완 |
| p.139 | 보완 |
| p.140 | 정정 및 보완 |
| p.141 | 보완 |
| p.142 | 일치 |
| p.143 | 보완 |
| p.144 | 보완 |

## 정정·보완 목록

근거의 PNG는 다음 경로 규칙을 따른다.
`/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-3d-manual-N.png`에서 `N`은 PDF 쪽 번호이다.

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.127 | 파일 제어 데이터(file control data)의 시계열 출력 설정이 이어진다. | 앞 쪽에서 이어지는 파일 제어 데이터의 시계열 출력 설정이다. 이 쪽에는 해당 절 제목이 다시 인쇄되지 않는다. | [보완] p.127 PNG. PNG 상단은 FILE TRN POINT 입력 형식으로 시작한다. |
| p.128 | 시계열 출력 변수 표가 이어진다. | 앞 쪽에서 이어지는 시계열 출력 변수 표이다. 이 쪽 상단에는 해당 절 제목이 없다. | [보완] p.128 PNG. PNG 상단은 DIR의 SRC 설명으로 시작한다. |
| p.129 | 시간 의존 공극률(time dependent porosity) 파일의 입력 형식은 | 앞 쪽에서 이어지는 절 `Time dependent porosity file control data`의 내용이다. 해당 제목은 p.128 하단에 있다. 시간 의존 공극률(time dependent porosity) 파일의 입력 형식은 | [보완] p.129 PNG. p.128 하단의 제목과 p.129 상단의 FILE PORO 입력을 대조했다. |
| p.130 | 기포 상승 속도(rising speed of bubble) `WBUB`의 단위는 | 앞 쪽에서 이어지는 절 `Raising bubbles (Timer door method)`의 변수 표이다. 해당 제목은 p.129 하단에 있다. 기포 상승 속도(rising speed of bubble) `WBUB`의 단위는 | [보완] p.130 PNG. p.129 하단 제목과 p.130 상단 WBUB 표를 대조했다. |
| p.130 | 원문: `When the sub loop is once, it is the same as normal calculation`(p.130). | 원문: `When the sub loop is once, it is the same as normal calculation`(p.130). 서브 루프가 한 번이면 일반 계산과 같다는 뜻이다. | [보완] p.130 PNG. PNG의 LOOP 표 아래 주석에 once와 same as normal calculation이 있다. |
| p.131 | `OPTION PV=CONST`의 `PVCP0`는 | 앞 쪽에서 이어지는 절 `Calculation of air pressure`의 변수 표이다. 해당 제목과 입력 형식은 p.130 하단에 있다. `OPTION PV=CONST`의 `PVCP0`는 | [보완] p.131 PNG. p.130 하단의 제목과 p.131 상단 PVCP0·PVCGM 행을 대조했다. |
| p.131 | `[OPTION DRAG-DF]` 줄과 뒤의 `[N]`개 줄에는 주석 줄과 빈 줄을 허용하지 않는다고 적는다. | 주석 원문은 `Comment lines and blank lines are not allowed in [OPTION DRAG-DF] lines or less [N] lines`이다. 이 주석은 주석 줄과 빈 줄을 금지한다. 제한 범위의 `or less [N] lines`는 인쇄 그대로 기록한다. 이 기록은 해당 표현을 “뒤의 `[N]`개 줄”로 확정하지 않는다. | [정정] p.131 PNG. PNG 하단 주석을 원본 해상도로 확대했다. 인쇄된 범위 표현은 or less [N] lines이다. |
| p.134 | 디버깅(debugging)용 직육면체 상자(rectangular box)의 F 값 입력은 | 앞 쪽에서 이어지는 절 `F value specification data to rectangular box`의 내용이다. 해당 제목은 p.133 하단에 있다. 디버깅(debugging)용 직육면체 상자(rectangular box)의 F 값 입력은 | [보완] p.134 PNG. p.133 하단 제목과 p.134 상단 DEBUG F-BOX 입력을 대조했다. |
| p.135 | 예시는 `CADMAS-SURF/3D-MG Ver. 1. 0 START.`로 시작한다. | 예시는 `CADMAS-SURF/3D-MG Ver. 1. 0 START.`로 시작한다. 설명 열의 `Execution start comment`는 실행 시작 메시지를 뜻한다. | [보완] p.135 PNG. PNG 예시 표의 첫 Description 항목이다. |
| p.135 | `DEFAULT.`, `INPUT-DATA.` 다음에 `INPUT-LEVEL= 0`이 나온다. | `DEFAULT.`의 설명 `Default setting`은 기본 설정을 뜻한다. `INPUT-DATA.`의 설명 `Read input file`은 입력 파일 읽기를 뜻한다. 두 출력 다음에 `INPUT-LEVEL= 0`이 나온다. | [보완] p.135 PNG. PNG 예시 표의 Default setting과 Read input file 설명을 보완했다. |
| p.135 | `[GRID][X]` 아래의 첫 좌표 행은 | `[GRID][X]` 부분의 설명 `Echo of grid data`는 격자 데이터의 재출력을 뜻한다. `[GRID][X]` 아래의 첫 좌표 행은 | [보완] p.135 PNG. PNG 예시 표의 Echo of grid data 설명을 보완했다. |
| p.136 | 절 `5.3. List file`의 번호 없는 예시 표가 이어진다. | 앞 쪽에서 이어지는 절 `5.3. List file`의 번호 없는 예시 표이다. 이 쪽에는 해당 절 제목이 다시 인쇄되지 않는다. | [보완] p.136 PNG. p.136 PNG는 예시 표의 계속 부분으로 시작한다. 절 제목은 p.135에 있다. |
| p.137 | 절 `5.3. List file`의 번호 없는 예시 표가 이어진다. | 앞 쪽에서 이어지는 절 `5.3. List file`의 번호 없는 예시 표이다. 이 쪽에는 해당 절 제목이 다시 인쇄되지 않는다. | [보완] p.137 PNG. p.137 PNG는 예시 표의 계속 부분으로 시작한다. 절 제목은 p.135에 있다. |
| p.138 | 절 `5.3. List file`의 번호 없는 예시 표가 이어진다. | 앞 쪽에서 이어지는 절 `5.3. List file`의 번호 없는 예시 표이다. 이 쪽에는 해당 절 제목이 다시 인쇄되지 않는다. | [보완] p.138 PNG. p.138 PNG는 예시 표의 계속 부분으로 시작한다. 절 제목은 p.135에 있다. |
| p.139 | 절 `5.3. List file`의 번호 없는 예시 표가 이어진다. | 앞 쪽에서 이어지는 절 `5.3. List file`의 번호 없는 예시 표이다. 이 쪽에는 해당 절 제목이 다시 인쇄되지 않는다. | [보완] p.139 PNG. p.139 PNG는 예시 표의 계속 부분으로 시작한다. 절 제목은 p.135에 있다. |
| p.136 | 표 설명 원문: `Input level 2 (input of various data)`(p.136). | 표 설명 원문: `Input level 2 (input of various data)`(p.136). 입력 레벨 2는 각종 데이터를 입력하는 단계이다. 설명 열의 `Echo of various data`는 각종 데이터의 재출력을 뜻한다. `Construction of various information`은 각종 정보의 구성을 뜻한다. `Output analysis condition`은 해석 조건의 출력을 뜻한다. | [보완] p.136 PNG. PNG 오른쪽 열 상단의 네 설명을 대조했다. 행의 세로 위치를 재배치하지 않고 설명 자체를 기록했다. |
| p.136 | 병렬 제어 예시의 값은 | 표 안의 구분 이름은 `-- PARALLEL --`, `-- EQUATION --`, `-- TIME CONTROL --`이다. 이 구분은 각각 병렬 제어 데이터, 방정식 제어 데이터, 시간 제어 데이터에 대응한다. 병렬 제어 예시의 값은 | [보완] p.136 PNG. PNG 왼쪽 열의 구분 이름과 오른쪽 열의 설명을 대조했다. |
| p.137 | 물성(physical property) 예시는 | 표 안의 물성 구분 이름은 `-- MATERIAL --`이다. 물성(physical property) 예시는 | [보완] p.137 PNG. PNG 상단의 -- MATERIAL --을 보완했다. |
| p.137 | `WAVE-BC X-` 조파 모델 예시는 | 표 안의 모델 구분 이름은 `-- MODEL --`이다. 설명 열의 `Model etc. Data`는 모델 등의 데이터를 뜻한다. `WAVE-BC X-` 조파 모델 예시는 | [보완] p.137 PNG. PNG 중간의 -- MODEL --과 Model etc. Data를 보완했다. |
| p.137 | `COMPUTATION` 아래의 | 구분 이름 `-- COMPUTATION --` 아래의 | [보완] p.137 PNG. PNG 하단의 구분 이름을 그대로 기록했다. |
| p.138 | 파일 제어 예시는 | 파일 제어의 구분 이름은 `-- FILE CONTROL --`이다. 파일 제어 예시는 | [보완] p.138 PNG. PNG 왼쪽 열의 -- FILE CONTROL --을 보완했다. |
| p.138 | 옵션 예시는 | 옵션의 구분 이름은 `-- OPTION --`이다. 옵션 예시는 | [보완] p.138 PNG. PNG 왼쪽 열의 -- OPTION --을 보완했다. |
| p.138 | 격자 좌표(grid coordinate) 예시는 | 격자 좌표의 구분 이름은 `-- GRID DATA --`이다. 격자 좌표(grid coordinate) 예시는 | [보완] p.138 PNG. PNG 왼쪽 열의 -- GRID DATA --를 보완했다. |
| p.139 | `OBSTACLE`과 `BOUNDARY` 아래에 | 구분 이름 `-- OBSTACLE --`의 설명은 장애물 데이터(`Obstacle data`)이다. 구분 이름 `-- BOUNDARY --`의 설명은 경계 조건 데이터(`Boundary condition data`)이다. 두 구분 아래에 | [보완] p.139 PNG. PNG 표 상단의 두 구분 이름과 Description 항목을 보완했다. |
| p.139 | `CALCULATION.` 다음에는 스텝 정보(step information)가 나온다. | `CALCULATION.`은 계산 시작(`Start calculation`)을 뜻한다. 다음에는 스텝 정보(step information)가 나온다. | [보완] p.139 PNG. PNG 오른쪽 열의 Start calculation 설명을 보완했다. |
| p.139 | `STEP= 0`의 그래픽 출력이 이어진다. | 계산 결과를 그래픽 파일에 출력한다는 설명은 `Output calculation result to graphic file`이다. 출력 행은 `>> FILE-GRP : OUT : STEP= 0 : TIME= 0. 00000E+00`이다. | [보완] p.139 PNG. PNG STEP=0 아래 그래픽 출력 행의 TIME과 오른쪽 설명을 보완했다. |
| p.139 | `STEP= 918`의 그래픽 출력이 이어진다. | 뒤의 그래픽 출력 행은 `>> FILE-GRP : OUT : STEP= 918 : TIME= 4. 00203E+01`이다. | [보완] p.139 PNG. PNG STEP=918 아래 그래픽 출력 행의 TIME을 보완했다. |
| p.140 | 절 `5.3. List file`의 번호 없는 예시 표가 끝난다. | 앞 쪽에서 이어지는 절 `5.3. List file`의 번호 없는 예시 표가 끝난다. 이 쪽에는 해당 절 제목이 다시 인쇄되지 않는다. | [보완] p.140 PNG. PNG 상단은 CPU 시간 출력의 계속 부분이다. 절 제목은 p.135에 있다. |
| p.140 | `FCUT` 설명은 절단한 VOF 함수 F 값과 셀 면적의 곱이다. | `FCUT` 설명은 `The sum of FCUT`로 시작한다. 이 설명은 절단한 VOF 함수 F 값과 셀 면적의 곱의 합을 뜻한다. | [정정] p.140 PNG. PNG 하단의 FCUT 정의를 원본 해상도로 확대했다. 한국어 설명에서 빠진 sum을 반영했다. |
| p.141 | 절 `5.3. List file`의 스텝 정보 정의가 한 줄 이어진다. | 앞 쪽에서 이어지는 절 `5.3. List file`의 스텝 정보 정의이다. 이 쪽에는 해당 절 제목이 다시 인쇄되지 않는다. 정의는 한 줄이다. | [보완] p.141 PNG. PNG의 본문은 ITR 정의 한 줄뿐이다. 절 제목은 p.135에 있다. |
| p.143 | `NORMAL END.`는 정상 종료 메시지이다. | 설명 열의 `Execution start comment`는 실행 시작 메시지를 뜻한다. `Default setting`은 기본 설정을 뜻한다. `Read input file`은 입력 파일 읽기를 뜻한다. `Construction of various information`은 각종 정보의 구성을 뜻한다. `Output analysis condition`은 해석 조건의 출력을 뜻한다. `Setting initial condition`은 초기 조건의 설정을 뜻한다. `Start calculation`은 계산 시작을 뜻한다. `Step information`은 스텝 정보를 뜻한다. `NORMAL END.`의 설명 `End message (normal termination)`은 정상 종료 메시지를 뜻한다. | [보완] p.143 PNG. PNG 예시 표의 Description 열 전체를 출력 단계와 대조했다. |
| p.144 | 원문: `As an example, the data when the water level is given is shown below.`(p.144). | 원문: `As an example, the data when the water level is given is shown below.`(p.144). 원문은 아래 예시를 수위가 주어진 경우의 데이터라고 소개한다. | [보완] p.144 PNG. PNG 하단 예시 직전 문장의 한국어 요지를 보완했다. |

## 판독 중 확인된 사실

- p.127의 `TSTEP` 형 `*8`은 인쇄와 일치한다.
- p.128의 와도 식은 미분 기호 대신 `@`를 인쇄한다.
- p.131의 첫 계수 조건은 소수점 없는 `0 0`으로 시작한다.
- p.131의 계수 `α0`와 `β0`에서 `0`은 본문 기준선에 있다.
- p.131의 주석은 `or less [N] lines`라는 표현을 쓴다.
- p.136과 p.143은 `Construction of various information`과 `Output analysis condition`의 세로 대응 위치가 다르다.
- p.140의 `DT` 괄호식은 본문 기준선의 `tn - tn - 1`이다.
- p.140의 `FCUT` 설명에는 `The sum of FCUT`가 있다.
- p.143과 p.144는 절 번호 `5.5`를 각각 사용한다.
- p.144의 `[w *]` 설명은 연직 위치를 뜻한다.
- p.144의 `[e *]` 설명에는 `z direction flow velocity`가 함께 인쇄되어 있다.
- 위 인쇄 표기는 임의로 고치지 않았다.

정정 2, 보완 13, 일치 3
