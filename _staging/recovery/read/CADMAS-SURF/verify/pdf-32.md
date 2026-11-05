# CADMAS-STR Program Instructions(CADMAS) English 전수 대조

대조일은 2026-11-04다.
대상 원본은 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Manual/CADMAS-STR_Program Instructions(CADMAS)_English.pdf`다.
고친 판독 기록은 [p001-023.md](</home/firesinger/coastal-wiki/_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Manual/CADMAS-STR_Program Instructions(CADMAS)_English.pdf/p001-023.md>)다.

대조한 쪽 수는 PDF p.1–23의 23쪽이다.
23쪽의 300 dpi PNG를 이미지 보기 도구로 각각 열었다.
작은 첨자와 수식은 p.3·13·15·18·19·22의 이미지 영역을 추가로 확대하여 확인했다.
텍스트 추출본은 철자 확인에만 참고했다.
판정은 쪽 이미지에 따랐다.

고친 쪽 수는 기록의 쪽 행을 기준으로 21쪽이다.
정정 표시가 있는 쪽은 20쪽이다.
보완 표시가 있는 쪽은 15쪽이다.
두 표시가 함께 있는 쪽은 14쪽이다.
마지막 줄의 정정·보완 수는 표시별 쪽 수이므로 서로 중복된다.
일치한 쪽은 p.1과 p.5의 2쪽이다.

쪽 표의 행 수는 수정 전후 모두 23개다.
기존 frontmatter의 필드와 값은 유지했다.
frontmatter에 `verified_by: codex gpt-6-astra (2026-11-04, 300dpi 이미지 전수 대조)` 한 줄을 추가했다.
원문에 인쇄된 이상 표기는 기록의 마지막 절인 “판독 중 확인된 사실”에 남겼다.

## 이미지 근거

사용한 PNG의 공통 디렉터리는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/`다.
p.N의 파일명은 `cad-str-instr-cadmas-NNN.png`다.
NNN은 PDF 쪽 번호를 세 자리로 쓴 값이다.
확인한 파일 번호는 001–023이다.
열지 못한 이미지는 없다.

## 정정·보완 목록

아래 표의 “이전”과 “새”는 쪽 행에서 바뀐 부분이다.
“보완”은 인수 설명이나 그림 요소 등 빠진 내용을 넣은 변경이다.
앞 쪽에서 이어지는 절 제목은 해당 쪽에 새로 인쇄된 제목과 구별했다.

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.2 | **1.[1]**의 `SF_STRUCT` 변수 표가 이어진다. | **정정**. 앞 쪽에서 이어지는 절 **1. Explanation of Variables / [1] Global variables by common**의 `SF_STRUCT` 변수 표다. | p.2 상단에는 절 제목 없이 NCTR 행부터 표가 이어진다. |
| p.3 | **1.[2] Global Variables by Module**. | **정정**. 앞 쪽에서 이어지는 절 **1. Explanation of Variables**의 하위 절 **[2] Global Variables by Module**이다. | p.3 인쇄 제목은 [2] Global Variables by Module이다. |
| p.3 | 각 프로세스와 전체 간 요소 번호 대응표 | **정정**. 각 프로세스의 요소 번호를 전체 요소 번호에 대응시키는 표 | p.3 IENO의 each process → whole. |
| p.3 | 각 프로세스와 전체 간 절점 번호 대응표 | **정정**. 각 프로세스의 절점 번호를 전체 절점 번호에 대응시키는 표 | p.3 IGNO의 each process → whole. |
| p.3 | 각 프로세스와 전체 간 표면 번호 대응표 | **정정**. 각 프로세스의 표면 번호를 전체 표면 번호에 대응시키는 표 | p.3 IPFNO의 each process → total. |
| p.4 | **1.[2]**의 `SF_ARRAY` 변수 표가 이어진다. | **정정**. 앞 쪽에서 이어지는 절 **1. Explanation of Variables / [2] Global Variables by Module**의 `SF_ARRAY` 변수 표다. | p.4에는 절 제목 없이 IPGRID 행부터 표가 이어진다. |
| p.4 | `Structure node position coordinates (all processes)`(p.4) | **정정**. `Structure nodal point position coordinates (all processes)`(p.4) | p.4 POS0 설명의 인쇄 문구. |
| p.6 | **2.[1]** 흐름도의 | **정정**. 앞 쪽에서 이어지는 절 **2. Processing Flow / [1] Overall flow of the coupled analysis section with STR (showing the case of bidirectional coupling)** 흐름도의 | p.6에는 절 제목 없이 SF_STR1 흐름도가 이어진다. |
| p.6 | `SF_POS_INIT_S` 상자는 유체 셀 압력 보간과 구조 표면 절점 압력 결정, STR로의 표면 자료·압력 전송을 설명한다. | **정정**. `SF_POS_INIT_S` 상자의 원문은 `Interpolate fluid cell pressures → Transmit surface data and pressures to STR to determine pressures at structural surface nodes`이다. 이 문구는 유체 셀 압력을 보간하는 절차를 설명한다. 이 문구는 구조 표면 절점 압력을 결정하기 위해 표면 자료와 압력을 STR로 전송한다고 설명한다. | p.6 맨 위 상자는 p.7과 달리 to determine을 전송 문구 뒤에 인쇄했다. |
| p.7 | **2.[1]** 흐름도의 | **정정**. 앞 쪽에서 이어지는 절 **2. Processing Flow / [1] Overall flow of the coupled analysis section with STR (showing the case of bidirectional coupling)** 흐름도의 | p.7에는 절 제목 없이 SF_STR2 흐름도가 이어진다. |
| p.7 | 해당 설명 누락 | **보완**. `SF_UPDT_OBST`는 프로세스별 구조 절점·요소·표면 자료를 갱신한다. | p.7 SF_UPDT_OBST 상자의 본문. |
| p.7 | `SF_PFACE3`는 `AFC`를 설정한다. | **보완**. `SF_PFACE3`는 구조 표면에서 압력이 작용하는 면적 비율(area fraction) `AFC`를 설정한다. | p.7 SF_PFACE3 상자의 본문. |
| p.8 | **2.[2] Timing of data reception and transmission with STR**. | **정정**. 앞 쪽에서 이어지는 절 **2. Processing Flow**의 하위 절 **[2] Timing of data reception and transmission with STR**이다. | p.8에 인쇄된 하위 절 제목과 앞 쪽에서 이어지는 상위 절을 구분했다. |
| p.8 | 해당 설명 누락 | **보완**. ①과 ⑤의 붉은 화살표는 각각 STR 선의 `Time TSTR1`, `Time TSTR2` 위치에 도달한다. ②의 붉은 화살표는 STR 선 아래에서 `TSTR1` 위치부터 `TSTR2` 위치까지 오른쪽으로 향한다. ④의 붉은 화살표는 두 시각 사이의 CADMAS 계산 진행을 오른쪽으로 표시한다. 수직 점선은 두 시간선 사이의 시각 위치를 연결한다. | p.8 시간도의 화살표 끝점과 수직 점선. |
| p.9 | **2.[3] Porosity Calculation Method**, **(1) cell porosity**. | **정정**. 앞 쪽에서 이어지는 절 **2. Processing Flow**의 하위 절 **[3] Porosity Calculation Method**, **(1) cell porosity**이다. | p.9에 인쇄된 하위 절 제목과 앞 쪽에서 이어지는 상위 절을 구분했다. |
| p.9 | 셀 쪽인 X축 양측을 남긴다. | **정정**. 셀 쪽인 X축의 양의 방향 쪽을 남긴다. | p.9 ④의 X-axis + side. |
| p.9 | 해당 설명 누락 | **보완**. 그림의 X축은 오른쪽을 향한다. Y축은 오른쪽 위 대각선 방향을 향한다. Z축은 위를 향한다. 네 도형은 위 왼쪽부터 `Tetra`, `Prism A`, 아래 왼쪽부터 `Prism B`, `Pyramid`로 배치되어 있다. 붉은 실선과 파선은 잔여 형상을 사면체로 분할하는 선을 보여 준다. | p.9 네 도형의 축 방향·배치·분할선. |
| p.10 | **2.[3](1)**의 ⑥은 | **정정**. 앞 쪽에서 이어지는 절 **2. Processing Flow / [3] Porosity Calculation Method / (1) cell porosity**의 ⑥은 | p.10에 인쇄된 하위 절 제목과 앞 쪽에서 이어지는 상위 절을 구분했다. |
| p.10 | 경계면 쪽인 X축 양측을 남긴다. | **정정**. 경계면 쪽인 X축의 양의 방향 쪽을 남긴다. | p.10 (2)②의 X-axis + side. |
| p.10 | 해당 설명 누락 | **보완**. 이 간섭 면적으로 유체 셀 경계면의 공극률을 구한다. | p.10 (2) 첫 문단의 porosity ... is determined. |
| p.11 | 해당 설명 누락 | **보완**. `IELM`은 구조 요소 자료다. `POR`는 석재의 공극률이다. `GRID`는 구조 절점 좌표다. `INDG`는 구조 절점 번호다. `POS0`는 전체 프로세스의 구조 절점 위치 좌표다. | p.11 SF_RD_OBST의 Contents 전 행. |
| p.11 | 해당 설명 누락 | **보완**. `IELM`은 구조 요소 자료다. `IPFACE`는 프로세스별 구조 표면 자료다. `IPFACE0`는 전체 프로세스의 구조 표면 자료다. `AFC`는 구조 표면에서 압력이 작용하는 면적의 백분율이다. `IPGRID0`는 전체 프로세스의 구조 표면 절점 자료다. `IPND0`는 구조 표면 절점 압력 플래그다. `PRES0`는 전체 프로세스의 구조 표면 절점 압력이다. | p.11 SF_PFACE0의 Contents 전 행. |
| p.11 | 해당 설명 누락 | **보완**. `IELM`은 구조 요소 자료다. `POR`는 석재의 공극률이다. `GRID`는 구조 절점 좌표다. `INDG`는 구조 절점 번호다. `IPFACE`는 프로세스별 구조 표면 자료다. `IENO`, `IGNO`, `IPFNO`는 각각 프로세스별 번호를 전체 번호에 대응시키는 표다. | p.11 SF_BCS_OBST, SF_ARRAY의 Contents 전 행. |
| p.12 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.12에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.12 | 해당 설명 누락 | **보완**. `IPGRID`는 프로세스별 구조 표면 절점 자료다. `PRES`는 프로세스별 구조 표면 절점 압력이다. `POS`, `POS1`, `POS2`는 구조 절점 위치 좌표다. `POS`는 프로세스별 자료다. `DVEL`의 설명은 `Dulcie flow velocity of the ground`이다. 이 문구는 지반의 유속을 가리킨다. `DVEL1`, `DVEL2`의 유속 명칭도 `Dulcie`로 인쇄되어 있다. | p.12 SF_BCS_OBST 표의 IPGRID–DVEL2 Contents. |
| p.12 | `POS1`과 `DVEL1`은 `TSTR1` 시각의 프로세스별 자료다. `POS2`와 `DVEL2`는 `TSTR2` 시각의 프로세스별 자료다. | **보완**. `POS1`은 `TSTR1` 시각의 프로세스별 구조 절점 위치 좌표다. `POS2`는 `TSTR2` 시각의 프로세스별 구조 절점 위치 좌표다. `DVEL1`은 `TSTR1` 시각의 프로세스별 지반 유속이다. `DVEL2`는 `TSTR2` 시각의 프로세스별 지반 유속이다. | p.12 POS1·POS2·DVEL1·DVEL2의 Contents. |
| p.12 | 해당 설명 누락 | **보완**. `IPFACE0`는 전체 프로세스의 구조 표면 자료다. `ICRG`는 각 접촉체의 접촉 표면 끝 주소다. `ICTR`은 접촉 표면 자료다. `ICTB`는 접촉체 조합이다. `POS0`는 전체 프로세스의 구조 절점 위치 좌표다. | p.12 SF_RECV_CONT의 Contents 전 행. |
| p.12 | 해당 설명 누락 | **보완**. `IPFACE`는 프로세스별 구조 표면 자료다. `IPFACE0`는 전체 프로세스의 구조 표면 자료다. `IPFNO`는 프로세스별 표면 번호를 전체 표면 번호에 대응시키는 표다. | p.12 SF_PFACE1의 IPFACE·IPFACE0·IPFNO Contents. |
| p.12 | `POS(3,NNOD)`와 세 방향 격자 좌표 `XX(MAXG1,NUMI)`, `YY(MAXG1,NUMJ)`, `ZZ(MAXG1,NUMK)`는 `R8`이며 `I`다. | **보완**. `POS(3,NNOD)`는 프로세스별 구조 절점 위치 좌표다. `XX(MAXG1,NUMI)`, `YY(MAXG1,NUMJ)`, `ZZ(MAXG1,NUMK)`는 각각 X·Y·Z 방향 격자 좌표 등이다. 이 네 행은 `R8`이며 `I`다. | p.12 SF_PFACE1의 POS·XX·YY·ZZ Contents. |
| p.13 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.13에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.13 | 해당 설명 누락 | **보완**. `IPFACE0`는 전체 프로세스의 구조 표면 자료다. `ICRG`는 각 접촉체의 접촉 표면 끝 주소다. `ICTR`은 접촉 표면 자료다. `ICTB`는 접촉체 조합이다. `POS0`는 전체 프로세스의 구조 절점 위치 좌표다. `AFC`는 구조 표면에서 압력이 작용하는 면적의 백분율이다. | p.13 SF_PFACE3의 Contents 전 행. |
| p.13 | 해당 설명 누락 | **보완**. 이 표의 인수 이름 열 머리글은 `Argument reference module`로 인쇄되어 있다. 이 표에는 참조 모듈 이름이 따로 인쇄되어 있지 않다. | p.13 SF_STR_OBST의 머리글. |
| p.14 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.14에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.14 | 해당 설명 누락 | **보완**. 이 문구는 석재의 공극비를 뜻한다. | p.14 POR의 Contents. |
| p.15 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.15에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.15 | 해당 설명 누락 | **보완**. `DBUF`는 병렬 버퍼다. | p.15 SF_MDPORO의 DBUF Contents. |
| p.15 | 해당 설명 누락 | **보완**. 두 표의 인수 이름 열 머리글은 `Argument reference module`로 인쇄되어 있다. 두 표에는 참조 모듈 이름이 따로 인쇄되어 있지 않다. | p.15 두 표의 머리글. |
| p.16 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.16에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.17 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.17에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.17 | 해당 설명 누락 | **보완**. `NF`는 셀 상태 인덱스다. `INDC`는 셀 계산 상태 인덱스다. | p.17 SF_NF_RESET의 NF·INDC Contents. |
| p.17 | 해당 설명 누락 | **보완**. `GGV`는 공극률이다. | p.17 SF_NF_RESET의 GGV Contents. |
| p.17 | 해당 설명 누락 | **보완**. 값 `0`은 계산됨을 뜻한다. 값 `1`은 계산되지 않음을 뜻한다. | p.17 IVOID의 플래그 설명. |
| p.17 | 해당 설명 누락 | **보완**. `INDX`는 X면의 상태 인덱스다. | p.17 SF_INDX_RESET의 INDX Contents. |
| p.17 | 해당 설명 누락 | **보완**. 네 표의 인수 이름 열 머리글은 `Argument reference module`로 인쇄되어 있다. 네 표에는 참조 모듈 이름이 따로 인쇄되어 있지 않다. | p.17 네 표의 머리글. |
| p.18 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.18에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.18 | 해당 설명 누락 | **보완**. `INDY`는 Y면 상태 인덱스다. `INDZ`는 Z면 상태 인덱스다. | p.18 SF_INDX_RESET의 INDY·INDZ Contents. |
| p.18 | 해당 설명 누락 | **보완**. `NF`는 셀 상태 인덱스다. | p.18 SF_INDX_RESET의 NF Contents. |
| p.18 | 해당 설명 누락 | **보완**. `IELM`은 구조 요소 자료다. `IGNO`는 프로세스별 절점 번호를 전체 절점 번호에 대응시키는 표다. `IPFACE0`는 전체 프로세스의 구조 표면 자료다. `IPGRID`는 프로세스별 구조 표면 절점 자료다. `IPGRID0`는 전체 프로세스의 구조 표면 절점 자료다. `POS`는 프로세스별 구조 절점 위치 좌표다. `XX`, `YY`, `ZZ`는 각각 X·Y·Z 방향 격자 좌표 등이다. 이 표의 `NF`도 셀 상태 인덱스다. | p.18 SF_PFACE2의 Contents 전 행. |
| p.18 | `X1`, `X2`는 셀 X방향 음·양측 끝 좌표다. `Y1`, `Y2`는 셀 Y방향 음·양측 끝 좌표다. `Z1`은 셀 Z방향 음측 끝 좌표다. | **정정**. `X1`은 셀 X방향 음의 쪽 끝 좌표다. `X2`는 셀 X방향 양의 쪽 끝 좌표다. `Y1`은 셀 Y방향 음의 쪽 끝 좌표다. `Y2`는 셀 Y방향 양의 쪽 끝 좌표다. `Z1`은 셀 Z방향 음의 쪽 끝 좌표다. | p.18 X1–Z1의 negative side·positive side. |
| p.18 | 해당 설명 누락 | **보완**. `SF_PFACE2`와 `SF_ADJOIN`의 인수 이름 열 머리글은 `Argument reference module`로 인쇄되어 있다. `SF_PFACE2`의 모듈 이름은 별도의 `Argument Reference Modules` 행에 있다. `SF_ADJOIN`에는 참조 모듈 이름이 따로 인쇄되어 있지 않다. | p.18 두 표의 머리글. |
| p.19 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.19에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.19 | `Z2`는 셀 Z방향 양측 끝 좌표이며 | **정정**. `Z2`는 셀 Z방향 양의 쪽 끝 좌표이며 | p.19 Z2의 positive side. |
| p.19 | 해당 설명 누락 | **보완**. 이 표의 인수 이름 열 머리글은 `Argument reference module`로 인쇄되어 있다. 이 표에는 참조 모듈 이름이 따로 인쇄되어 있지 않다. | p.19 SF_BC_RESET의 머리글. |
| p.20 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.20에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.20 | 해당 설명 누락 | **보완**. `IELM`은 구조 요소 자료다. `POR`는 석재의 공극률이다. `IENO`는 프로세스별 요소 번호를 전체 요소 번호에 대응시키는 표다. `INDG`는 구조 절점 번호다. `IGNO`는 프로세스별 절점 번호를 전체 절점 번호에 대응시키는 표다. `IPFACE`는 프로세스별 구조 표면 자료다. 이 표의 인수 이름 열 머리글은 `Argument reference module`로 인쇄되어 있다. 참조 모듈 이름은 별도의 `Argument Reference Modules` 행에 있다. | p.20 SF_UPDT_OBST, SF_ARRAY의 Contents 전 행과 머리글. |
| p.21 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.21에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.21 | `IPFNO(NPFC)`는 표면 번호 대응표이며 | **정정**. `IPFNO(NPFC)`는 프로세스별 표면 번호를 전체 표면 번호에 대응시키는 표이며 | p.21 IPFNO의 Each process → Whole. |
| p.21 | 해당 설명 누락 | **보완**. `IPGRID`는 프로세스별 구조 표면 절점 자료다. `PRES`는 프로세스별 구조 표면 절점 압력이다. `POS1`, `POS2`는 구조 절점 위치 좌표다. `DVEL`의 설명은 `Dulcie flow velocity of the ground`이다. 이 문구는 지반의 유속을 가리킨다. `DVEL1`, `DVEL2`의 유속 명칭도 `Dulcie`로 인쇄되어 있다. | p.21 SF_UPDT_OBST 표의 IPGRID–DVEL2 Contents. |
| p.21 | `POS1`과 `DVEL1`은 `TSTR1` 시각의 프로세스별 자료다. `POS2`와 `DVEL2`는 `TSTR2` 시각의 프로세스별 자료다. | **보완**. `POS1`은 `TSTR1` 시각의 프로세스별 구조 절점 위치 좌표다. `POS2`는 `TSTR2` 시각의 프로세스별 구조 절점 위치 좌표다. `DVEL1`은 `TSTR1` 시각의 프로세스별 지반 유속이다. `DVEL2`는 `TSTR2` 시각의 프로세스별 지반 유속이다. | p.21 POS1·POS2·DVEL1·DVEL2 Contents. |
| p.21 | 해당 설명 누락 | **보완**. 이 표의 인수 이름 열 머리글은 `Argument reference module`로 인쇄되어 있다. 이 표에는 참조 모듈 이름이 따로 인쇄되어 있지 않다. | p.21 SF_CINIT의 머리글. |
| p.21 | 해당 설명 누락 | **보완**. 이 세 인수는 각각 X·Y·Z 방향 격자 좌표 등이다. | p.21 SF_CINIT의 XX·YY·ZZ Contents. |
| p.22 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.22에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.23 | **3. Subroutine Description** | **정정**. 앞 쪽에서 이어지는 절 **3. Subroutine Description** | p.23에는 3. Subroutine Description 절 제목이 인쇄되어 있지 않다. |
| p.23 | 해당 설명 누락 | **보완**. `IGNO`의 대응 방향은 프로세스별 절점 번호에서 전체 절점 번호로 향한다. | p.23 SF_GPRES의 IGNO Contents. |
| p.23 | 해당 설명 누락 | **보완**. `SF_GPRES`와 `SF_PMGBC0`의 인수 이름 열 머리글은 `Argument reference module`로 인쇄되어 있다. 이 두 표에는 참조 모듈 이름이 따로 인쇄되어 있지 않다. | p.23 상단 두 표의 머리글. |

## 일치 확인

p.1의 제목·소개 문단·공통 변수 표는 기존 기록과 일치했다.
p.5의 제목·SF_STR0 흐름도·분기·블록 설명은 기존 기록과 일치했다.
p.15의 범위식 3개는 확대 이미지와 일치했다.
p.18의 좌표 관계식 1개는 확대 이미지와 일치했다.
p.22의 좌표 식 1개는 확대 이미지와 일치했다.
p.3·13·19의 람다 첨자는 확대 이미지와 일치했다.
해당 수식과 첨자의 값은 바꾸지 않았다.

정정 20, 보완 15, 일치 2
