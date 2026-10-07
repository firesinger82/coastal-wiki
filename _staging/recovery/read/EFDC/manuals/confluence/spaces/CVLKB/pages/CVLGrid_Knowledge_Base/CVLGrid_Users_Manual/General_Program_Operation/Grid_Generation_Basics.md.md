---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/General_Program_Operation/Grid_Generation_Basics.md
lines: 35
sha256: 23fb5f33b161d3e5b8c57962013d5575baab29e6800f6c89b774ee51a3d09a4d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Grid_Generation_Basics.md — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Grid Generation Basics`, space `CVLKB`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–14 | 격자 생성의 세 단계 — 영역 파일을 읽고, 경계를 따라 스플라인(spline)을 만든 뒤 격자를 생성한다(10). 단순 영역은 한 격자, 가지와 큰 굴곡이 있는 복잡한 영역은 여러 하위 영역과 연결 격자가 필요하다고 적는다(10). 필요조건 원문: `Four splines enclosing a region are required to generate one grid.` (10). 그림 1을 열었다(12–13). P2D 영역 경계선과 `400_Elevation` 범례, `1.2 Kilometers` 축척 막대를 보여 준다(12). |
| 15–19 | 스플라인 작성·교차 조건 — 첫 스플라인이 I 인덱스(index), 그것과 교차하는 스플라인이 J 인덱스를 정의한다(15). 조건 원문: `To create a grid, four splines must be created and must completely enclose the whole or part of the model domain.` (15); `For a very simple domain the first spline is drawn along the bottom of the domain from left to right.` (15); `The last two splines are drawn along the sides of the domain and **must intersect** the previous two splines.` (15). 교차선은 가능한 한 수직에 가깝게 그리는 것이 좋다고 적는다(19). 그림 2를 열었다(16–17). 초록 스플라인 네 개가 영역을 둘러싸며 번호는 아래 `1`, 위 `2`, 왼쪽 `3`, 오른쪽 `4`이다. 파란 화살표는 각 선 옆에서 양방향으로 표시되어 있다. 안쪽 문구는 `Grid will be generated in this area`이다(16). |
| 20–26 | Generate Grid — 네 스플라인이 영역을 완전히 둘러싼 후 버튼을 누르고 I·J축 셀 수를 지정한다(20). 첫 스플라인은 I축, 측면 스플라인은 J축을 정의한다(20). 같은 행의 격자 생성 아이콘을 열었다(20). 파란 네 칸 격자 아이콘이다. 그림 3도 열었다(22–23). 표시값은 선택 `Create a New Layer`, `Layer Name: Grid`, `I-Cells Number: 5`, `J-Cells Number: 5`이며 `Select an Existed Layer`는 비활성 상태이다(22). 기본값 여부는 본문에 없다. 생성 뒤 CVLGrid Options로 속성을 표시하고 작업공간 RMC로 수정 메뉴를 연다(25). |
| 27–35 | 새 스플라인 레이어 — 한 스플라인 레이어에서 지정한 셀 수의 격자 하나만 생성한다고 적는다(27). 적용 조건 원문: `Only one grid with a specific of cells number is generated with a layer of splines. This means if the user wants to generate a new grid they need to create a new layer of splines.` (27). Layer Control의 New를 누르고 종류·이름을 정하여 OK로 새 레이어를 만든다(27·32). 종류 지시 원문은 `Layer Type as Splines`이다(32). 그림 4·5를 열었다(29·34). 그림 4는 New 버튼, 그림 5는 `Layer Name: Spline`과 Layer Type의 Overlay·선택된 Spline·비활성 Grid를 보여 준다(34). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·15·20·27·32행: `#GridGenerationBasics-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.

