---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Boundary_Conditions.md
lines: 26
sha256: 8c89057e25305dc0a50abf635123e0a00fd4e9a536714f8569c89ef039bb34dd
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Boundary_Conditions.md — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Boundary Conditions / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–18 | Boundary Conditions / 경계 그룹 관리 — 색상 CSS 뒤에 본문이 이어진다(10). EFDC는 경계 조건(boundary conditions)을 셀별로 적용한다(10). EFDC+ Explorer는 하천 유입이나 개방 경계(open boundary)처럼 논리적인 경계 그룹(boundary group)으로 셀을 묶는다(10). 그룹 정보는 프로젝트 디렉터리의 `EFDC.EE`에 저장한다(10). 기존 그룹이 없는 프로젝트를 불러오면 경계 유형과 위치를 기준으로 기존 경계 셀을 묶는다고 적는다(10). 그룹 내부 유량(flow), 열(heat), 압력(pressure) 설정은 셀마다 달라도 되지만 수질 매개변수(water quality parameters)는 같아야 한다(10). 셀마다 수주 매개변수(water column parameters)를 달리 지정해야 하면 각 셀을 별도 그룹으로 관리해야 한다(10). 원문: `However, if there are no current groupings when EFDC+ Explorer loads a project (which is the case for existing EFDC models not managed with EFDC+ Explorer), it groups the existing boundary cells into groups based on the type of boundary condition and their locations.` (10); `Within a group, the flow, heat, and pressure settings can vary from cell to cell but the water quality parameters must be the same.` (10); `If the user needs to specify the water column parameters on a cell by cell basis the EFDC+ Explorer user needs to manage each cell as a separate group.` (10). 메뉴 트리에서 그룹 추가, 편집, 삭제와 시계열(time series) 조회를 안내한다(12–18). 셀의 개방 면은 경계 유형으로 정한다(18). 원문: `*Boundary Group Type*` (18); `In the case of the *Water Level* boundary condition the user will have to select between North, South, West, East open boundary types, as these boundary types will determine which side of the cells is open.` (18). 14행 `EE10_137.png`의 로컬 사본을 열었다. 그림은 Boundary Conditions 메뉴 트리와 Water Level 그룹의 East Open Boundary 정보를 보여 준다(14). |
| 19–26 | Boundary Conditions / 공통 프레임과 셀 — 경계 유형별 창에 공통으로 Boundary Group Information과 Current Boundary Cell 프레임이 있다고 적는다(20). 첫 프레임은 해당 경계 조건의 전체 그룹 수, 현재 그룹 번호와 ID를 담는다(24). 둘째 프레임은 현재 그룹의 셀별 정보를 담는다(24). Add 뒤 셀 번호를 입력하여 추가하고 스크롤바로 고른 셀을 Remove하거나 Remove All로 그룹의 모든 셀을 제거한다고 적는다(24). 원문: `*L, I, J*` (24); `The user may add a cell by selecting *Add* then enter the *L, I, J* number, select then *Remove* a cell from boundary group using the scroll bar or *Remove All* to remove all cells in this boundary group` (24). 22행 `EE10_138.png`의 로컬 사본을 열었다. 그림은 Open Boundary Conditions 창의 두 공통 프레임과 상수·시간 변화 농도(constant/time varying concentration) 입력 표를 보여 주며 두 농도 표의 자료 행은 비어 있다(22). 2DH View에서도 모델 경계 조건에 접근할 수 있다는 설명과 `Modify Model Boundaries` 링크를 포함한다(26). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12·16: Figure 1 링크는 문서 내부 그림 앵커 대신 `resumedraft.action?draftId=240222300`을 가리킨다.
- 20·22: Figure 2 링크는 `#Figure2`를 사용한다. 이 Markdown 파일에는 해당 ID의 앵커나 Figure 2 캡션이 없다.
