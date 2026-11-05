# CADMAS-STR Program Instructions English p.19–36 전수 대조

검증일은 2026-11-04이다. 검증 대상은 [p019-036.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Manual/CADMAS-STR_Program%20Instructions_English.pdf/p019-036.md)이다. PDF 쪽 번호를 기준으로 기록했다.

지정된 300 dpi PNG에서 p.19–36의 18쪽을 모두 직접 열었다. 고친 쪽은 15쪽이다. 기존 내용과 일치한 쪽은 p.20, p.23, p.28이다.

정정이 있는 쪽은 11쪽이다. 보완이 있는 쪽은 15쪽이다. 두 종류가 함께 있는 11쪽은 두 집계에 모두 포함한다. 마지막 줄의 수는 변경 항목 수가 아니라 쪽 수이다.

수식·행렬·작은 첨자는 p.19–27에서 해당 영역을 확대해 확인했다. p.35–36의 좌표축 첨자도 확대해 확인했다. p.32의 요소 정의 문장은 확대해 철자를 재확인했다. 확대 이미지는 메모리에서만 만들었다.

p.27의 겹친 등식은 확대해도 문자 배열을 확정할 수 없었다. 기존의 `[원문 인쇄 판독 불가]` 표시는 유지했다. 추출 텍스트의 수식으로 대체하지 않았다. p.19의 시간 순서, p.23의 불완전한 자유도 분류, p.27의 `FF`, p.30의 `Node numbers`·`Node coordinates`, p.36의 `Sefinition`은 인쇄대로 유지했다. 일본어 문장은 p.22·33·34의 이미지와 대조했다. 일본어 원문과 한국어 뜻은 기존 기록을 유지했다.

쪽 표의 본문 행은 수정 전후 모두 18개이다. 기존 frontmatter 항목은 유지했다. 요청한 `verified_by` 한 줄을 추가했다.

## 정정·보완 목록

아래의 이전·새 내용은 변경한 부분만 인용한다. 각 근거의 PNG 링크는 해당 쪽의 전체 이미지이다.

| p.N | 이전 | 새 | 근거 |
|---|---|---|---|
| p.19 | 해당 내용 없음 | **보완**. 분리 전 방정식 블록의 원문은 `Equations for both structural and seepage flow analysis.`이다. 분리 전 결과 블록의 원문은 `Determine variables`이다. 분리 후 구조 방정식 블록의 원문은 `Equations for structural analysis.`이다. 분리 후 침투류 방정식 블록의 원문은 `The equations for seepage flow analysis.`이다. 분리 후 두 결과 블록의 원문은 각각 `Determine a variable`이다. 블록 사이 화살표는 모두 아래를 향한다. | [p.19 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-019.png). 분리 전후 흐름도의 블록 문구와 연결 화살표. |
| p.21 | 다점 구속(multipoint constraint, MPC)을 적용하기 위한 변환 행렬(transformation matrix)을 설명한다. | **보완**. 다점 구속(multipoint constraint, MPC) 조건이 주어졌을 때 연립 일차방정식의 계수 행렬과 우변 벡터를 변환하는 방법을 설명한다. | [p.21 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-021.png). [1] 첫 문단은 coefficient matrix와 right-hand side vector를 모두 명시한다. |
| p.22 | **2.2 [2] Element-by-element processing in the overall stiffness matrix assembly**. | **정정**. 앞 쪽에서 이어지는 절 2.2이다. 이 쪽의 소제목은 **[2] Element-by-element processing in the overall stiffness matrix assembly**이다. | [p.22 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-022.png). 쪽 상단에는 [2] 소제목만 인쇄되어 있다. |
| p.22 | 해당 내용 없음 | **보완**. 독립 변수 벡터 \(\{\overline U\}\)에서 `IDCR` 표로 향하는 곡선 화살표가 있다. | [p.22 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-022.png). 변환 행렬 아래의 곡선 화살표. |
| p.24 | **[2]** 각 점 | **보완**. **[2]** 위 MPC 조건식을 아래와 같이 설정한다. 각 점 | [p.24 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-024.png). [2] 첫 문장 The above MPC conditional equation is set as follows. |
| p.24 | 해당 내용 없음 | **보완**. 삼각형 그림에는 점 S에서 위쪽으로 뻗는 빨간 선 두 개가 있다. | [p.24 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-024.png). 삼각형 접촉 그림의 빨간 선. |
| p.25 | **2.4 [2] (2)** 사각형 면 조건의 계속이다. | **정정**. 앞 쪽에서 이어지는 절 2.4 [2] (2)의 사각형 면 조건이다. 이 쪽 상단에는 해당 절 제목이 다시 인쇄되어 있지 않다. | [p.25 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-025.png). 쪽 상단은 U5 식으로 시작한다. |
| p.25 | +t\boldsymbol U_2\cdot\boldsymbol e_2 | **정정**. +t\cdot\boldsymbol U_2\cdot\boldsymbol e_2 | [p.25 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-025.png). (3)의 e2 조건식은 t와 U2 사이에도 곱셈점을 인쇄한다. |
| p.25 | +t\boldsymbol U_2\cdot\boldsymbol e_3 | **정정**. +t\cdot\boldsymbol U_2\cdot\boldsymbol e_3 | [p.25 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-025.png). (3)의 e3 조건식은 t와 U2 사이에도 곱셈점을 인쇄한다. |
| p.25 | 해당 내용 없음 | **보완**. 사각형 그림에는 점 S에서 위쪽으로 뻗는 빨간 선 두 개가 있다. 모서리 그림에는 공통 모서리 12를 공유하는 두 삼각형이 있다. 두 삼각형의 나머지 꼭짓점에는 번호가 없다. 모서리 그림에도 점 S에서 위쪽으로 뻗는 빨간 선 두 개가 있다. 작은 좌표축에서 \(\boldsymbol e_1\)은 오른쪽 아래를 향한다. \(\boldsymbol e_2\)는 오른쪽 위를 향한다. \(\boldsymbol e_3\)는 위를 향한다. | [p.25 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-025.png). 사각형 그림과 모서리 그림의 선, 무번호 꼭짓점, 좌표축 방향. |
| p.26 | **2.4 [2] (4) Cases when the master is on the dot**. | **정정**. 앞 쪽에서 이어지는 절 2.4 [2]이다. 이 쪽의 소제목은 **(4) Cases when the master is on the dot**이다. | [p.26 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-026.png). 쪽 상단에는 (4) 소제목만 인쇄되어 있다. |
| p.26 | 해당 내용 없음 | **보완**. 마스터 점에서 뻗는 검은 선은 다섯 개이다. 슬레이브 점에서 위쪽으로 뻗는 빨간 선은 두 개이다. | [p.26 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-026.png). 점 접촉 그림의 검은 선과 빨간 선. |
| p.27 | 번호 없는 왼쪽 그림은 블록에 작용하는 아래 방향 \(F_n\), 오른쪽 방향 F와 \(u_r\), 왼쪽 방향 \(F_t\)를 보여 준다. | **정정**. 번호 없는 왼쪽 그림은 블록 위에서 아래로 향하는 화살표를 보여 준다. 그 화살표 바로 옆에는 기호가 인쇄되어 있지 않다. 오른쪽 방향 화살표에는 F와 \(u_r\)가 표시된다. 왼쪽 방향 화살표에는 \(F_t\)가 표시된다. | [p.27 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-027.png). 왼쪽 블록 그림의 아래 방향 화살표 주변을 확대했다. Fn이라는 표기는 그 화살표 옆에 없다. |
| p.27 | 해당 내용 없음 | **보완**. 왼쪽 그림에는 수평 바닥선이 있다. 왼쪽 방향 마찰력 화살표의 시작점은 블록 아래쪽의 검은 점이다. 오른쪽 그래프의 빨간 수직선은 원점 위와 아래로 뻗는다. 그래프에는 단위가 인쇄되어 있지 않다. | [p.27 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-027.png). 마찰 그림의 바닥선과 검은 점 및 그래프의 수직 구간. |
| p.30 | **3.3 [2] Element, element characterization**. | **정정**. 앞 쪽에서 이어지는 절 3.3이다. 이 쪽의 소제목은 **[2] Element, element characterization**이다. | [p.30 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-030.png). 쪽 상단에는 [2] 소제목만 인쇄되어 있다. |
| p.31 | **3.3 [2]**의 | **정정**. 앞 쪽에서 이어지는 절 3.3 [2]의 | [p.31 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-031.png). 쪽 상단은 입력 키워드로 시작한다. 3.3 [2] 제목은 이 쪽에 인쇄되어 있지 않다. |
| p.32 | **3.3 [2]**의 | **정정**. 앞 쪽에서 이어지는 절 3.3 [2]의 | [p.32 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-032.png). 쪽 상단은 입력 키워드로 시작한다. 3.3 [2] 제목은 이 쪽에 인쇄되어 있지 않다. |
| p.33 | **3.3 [2]**의 | **정정**. 앞 쪽에서 이어지는 절 3.3 [2]의 | [p.33 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-033.png). 쪽 상단은 입력 키워드로 시작한다. 3.3 [2] 제목은 이 쪽에 인쇄되어 있지 않다. |
| p.34 | **3.3 [2]**의 | **정정**. 앞 쪽에서 이어지는 절 3.3 [2]의 | [p.34 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-034.png). 쪽 상단은 입력 키워드로 시작한다. 3.3 [2] 제목은 이 쪽에 인쇄되어 있지 않다. |
| p.35 | **3.3 [2]**의 | **정정**. 앞 쪽에서 이어지는 절 3.3 [2]의 | [p.35 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-035.png). 쪽 상단은 입력 키워드로 시작한다. 3.3 [2] 제목은 이 쪽에 인쇄되어 있지 않다. |
| p.36 | **3.3 [2]**의 | **정정**. 앞 쪽에서 이어지는 절 3.3 [2]의 | [p.36 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-036.png). 쪽 상단은 입력 키워드로 시작한다. 3.3 [2] 제목은 이 쪽에 인쇄되어 있지 않다. |
| p.29 | 해당 내용 없음 | **보완**. 두 형식 표의 머리행은 각각 `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`이다. 항목 표의 열 제목은 `Field`, `Type`, `Contents`이다. | [p.29 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-029.png). 형식 표의 번호 머리행과 항목 표의 열 제목. |
| p.30 | 해당 내용 없음 | **보완**. `Format :` 표의 머리행은 `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`이다. 항목 표의 열 제목은 `Field`, `Type`, `Contents`이다. | [p.30 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-030.png). 형식 표의 번호 머리행과 항목 표의 열 제목. |
| p.31 | 해당 내용 없음 | **보완**. `Format :` 표의 머리행은 `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`이다. 항목 표의 열 제목은 `Field`, `Type`, `Contents`이다. 주석 구역의 원문 표시는 `Remarks :`이다. | [p.31 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-031.png). 형식 표의 번호 머리행과 항목 표의 열 제목 및 Remarks 표제. |
| p.32 | 해당 내용 없음 | **보완**. `Format :` 표의 머리행은 `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`이다. 항목 표의 열 제목은 `Field`, `Type`, `Contents`이다. 주석 구역의 원문 표시는 `Remarks :`이다. | [p.32 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-032.png). 형식 표의 번호 머리행과 항목 표의 열 제목 및 Remarks 표제. |
| p.33 | 해당 내용 없음 | **보완**. `Format :` 표의 머리행은 `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`이다. 항목 표의 열 제목은 `Field`, `Type`, `Contents`이다. 주석 구역의 원문 표시는 `Remarks :`이다. | [p.33 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-033.png). 형식 표의 번호 머리행과 항목 표의 열 제목 및 Remarks 표제. |
| p.34 | 해당 내용 없음 | **보완**. 두 `Format :` 표의 머리행은 각각 `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`이다. 두 항목 표의 열 제목은 각각 `Field`, `Type`, `Contents`이다. | [p.34 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-034.png). 형식 표의 번호 머리행과 항목 표의 열 제목. |
| p.35 | 해당 내용 없음 | **보완**. `Format :` 표의 머리행은 `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`이다. 항목 표의 열 제목은 `Field`, `Type`, `Contents`이다. 주석 구역의 원문 표시는 `Remarks :`이다. | [p.35 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-035.png). 형식 표의 번호 머리행과 항목 표의 열 제목 및 Remarks 표제. |
| p.36 | 해당 내용 없음 | **보완**. `Format :` 표의 머리행은 `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`이다. 항목 표의 열 제목은 `Field`, `Type`, `Contents`이다. 주석 구역의 원문 표시는 `Remarks :`이다. | [p.36 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-036.png). 형식 표의 번호 머리행과 항목 표의 열 제목 및 Remarks 표제. |
| p.32 | `The sequence of the configuration node numbers is shown in the figure below` | **정정**. `The sequence of the configuration node numbers is shown in the figure below．` | [p.32 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-032.png). Remarks 1의 인용문 끝에 마침표가 인쇄되어 있다. |
| p.33 | `The sequence of the configuration node numbers is shown in the figure below` | **정정**. `The sequence of the configuration node numbers is shown in the figure below．` | [p.33 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-033.png). Remarks 1의 인용문 끝에 마침표가 인쇄되어 있다. |
| p.31 | 해당 내용 없음 | **보완**. 그림에서 `G1`은 왼쪽 꼭짓점이다. `G2`는 아래쪽 꼭짓점이다. `G3`는 오른쪽 꼭짓점이다. `G4`와 나머지 세 꼭짓점 사이의 모서리도 모두 실선이다. | [p.31 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-031.png). 사면체 그림의 절점 배치와 실선 모서리. |
| p.32 | 해당 내용 없음 | **보완**. 그림에서 아래 삼각형의 `G1`은 왼쪽이다. `G2`는 오른쪽 아래이다. `G3`는 오른쪽 위이다. 위 삼각형의 `G4`는 왼쪽이다. `G5`는 오른쪽 아래이다. `G6`는 오른쪽 위이다. | [p.32 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-032.png). 삼각기둥 그림의 절점 배치. |
| p.33 | 해당 내용 없음 | **보완**. 그림에서 아래 면의 `G4`는 왼쪽 앞이다. `G1`은 오른쪽 앞이다. `G3`는 왼쪽 뒤이다. `G2`는 오른쪽 뒤이다. 대응하는 위 면의 앞쪽 절점은 `G8`, `G5`이다. 뒤쪽 절점은 `G7`, `G6`이다. | [p.33 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-033.png). 육면체 그림의 절점 배치. |
| p.36 | 원문 설명은 `Sefinition of beam elements.` (p.36)이다. | **보완**. 원문 설명은 `Sefinition of beam elements.` (p.36)이다. 뜻은 “보 요소의 정의”이다. | [p.36 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-036.png). CBAR 바로 아래의 설명 문장. |
| p.36 | 해당 내용 없음 | **보완**. 보의 형상은 직사각형 단면을 가진 기둥으로 그려져 있다. 가려진 모서리는 점선이다. \(\boldsymbol\nu\)와 보의 길이 방향을 포함하는 면은 가는 선으로 표시된다. | [p.36 PNG](/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-036.png). CBAR 그림의 실선 외곽, 점선 모서리와 가는 보조선. |

## 열지 못한 이미지

없음. 지정된 p.19–36 PNG 18개를 모두 열었다.

정정 11, 보완 15, 일치 3
