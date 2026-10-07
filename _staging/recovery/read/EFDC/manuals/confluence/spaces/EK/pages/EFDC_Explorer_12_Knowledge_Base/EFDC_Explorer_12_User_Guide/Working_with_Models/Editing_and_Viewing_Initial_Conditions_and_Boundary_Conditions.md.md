---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Working_with_Models/Editing_and_Viewing_Initial_Conditions_and_Boundary_Conditions.md
lines: 32
sha256: 255eba3289892219b6d6de88e42649ee8f71f448778efe004d83a7b0b4d1fa00
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Editing_and_Viewing_Initial_Conditions_and_Boundary_Conditions.md — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 초기조건(initial conditions)·경계조건(boundary conditions) 편집·보기 페이지의 ID, URL, 버전, 갱신 시각, 계층을 수록한다(1–9). |
| 10–18 | 모듈과 초기조건 — 기능은 대부분 Modules 메뉴에서 켜야 한다고 적는다(10). 조건 원문: `In most cases, a feature has to be turned on in the *Modules* menu ( as shown in [Figure 1](#Figure1))*.*The detailed process for turning on modules can be found in [Setting EFDC Modules](/wiki/spaces/EK/pages/240418923/Setting+EFDC+Modules)` (10) Figure 1 로컬 그림을 직접 열었다(12). EFDC Modules에서 Salinity, Temperature, Dye를 선택한 화면이다(12 그림). 초기조건 진입의 두 방법 원문: `Once a module is enabled, the user can view the enabled module on the Model Control Form. To assign initial conditions to a module RMC on the corresponding item in *Modules* and then select *Initial Conditions*as in [Figure 2](#Figure2). Alternatively, the user can also go to the distinct *initial Conditions* menu item and RMC on the corresponding item.` (14) Figure 2 로컬 그림을 직접 열었다(16). RMC 표시는 트리 항목을 향하고 다음 화살표는 Initial Conditions 메뉴를 향한다(16 그림). 해당 초기조건 절의 안내 링크를 포함한다(18). |
| 19–28 | 경계조건 데이터와 2DH View 배정 — 편집 전에 데이터 시계열(time series)을 먼저 생성하거나 불러와야 한다(20). 선행 조건 원문: `Before the user can edit boundary conditions, data series for the boundary condition must first be created or imported. Both of these options can be done in the *External Forcing Data* menu item and is covered [here](/wiki/spaces/EK/pages/240386145/External+Forcing+Data). The *Boundary Conditions* menu item provides settings for the boundary and provides options to assign these data series to cells. For more information on these forms, please see [Boundary Conditions](/wiki/spaces/EK/pages/240222300/Boundary+Conditions) and the respective page for each boundary.` (20) Boundaries 선택, Enable Edit, 위치 셀 우클릭 또는 Shift-LMC 다중 선택, Add New Boundary Group 순서를 적는다(22–26). 원문: `1. Choose *Boundaries*in the *Viewing Layer Control.*` (24) `3. RMC on the boundary location cell (or Shift-LMC to select multiple cells then RMC) and click on *Add New Boundary Group*` (26) 25행의 작은 로컬 그림을 직접 열었으며 편집용 연필 아이콘이다. Figure 3 로컬 그림을 직접 열었다(28). 경계 레이어 편집과 격자 셀의 Add New Boundary Group 메뉴를 보여 준다(28 그림). 색상 범례는 `Water Depth (m)`의 `0.680`–`4.340`, `Bottom Elevation (m)`의 `7.160`–`10.820`이며 시각은 `[Time: 2019-01-01 00:00]`이다(28 그림). 별도의 좌표축은 없으며 선택 셀 정보에 X,Y와 dX,dY의 m 단위를 표시한다(28 그림). |
| 29–32 | 경계 그룹 유형 — 수위(Water Level) 경계 그룹에 속하는 남·서·동·북 개방경계(open boundary) 유형을 설명한다(30). 유형·그룹 원문: `The user is then prompted to choose the boundary group types, and these types are the same as the boundary types in *Boundary Conditions* menu, with the types *South Open Boundary*, *West Open Boundary*, *East Open Boundary*, *North Open Boundary* belonging to the *Water Level* boundary group ( shown in [Figure 4](#Figure4) ).` (30) Figure 4 로컬 그림을 직접 열었다(32). Add BC Group의 `Boundary Group Name: Inflow`, `Boundary Group Type: Flow Boundary`와 개방경계 등의 선택 목록을 보여 준다(32 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 색상 CSS가 본문 시작에 남아 있다.
- 16행 그림: 트리에서 `Salinity`가 선택되어 있으나 오른쪽 보고서 제목은 `Temperature`이다.

