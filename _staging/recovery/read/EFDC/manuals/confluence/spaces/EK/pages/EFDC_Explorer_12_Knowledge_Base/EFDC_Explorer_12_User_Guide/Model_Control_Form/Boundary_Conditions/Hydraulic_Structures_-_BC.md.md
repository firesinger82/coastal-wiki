---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Boundary_Conditions/Hydraulic_Structures_-_BC.md
lines: 51
sha256: 328d19ba28fb7163b7c3997e9a05b955d5263950b32e8d2a422cc8df49dfe9e9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Hydraulic_Structures_-_BC.md — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Hydraulic Structures - BC / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–14 | Hydraulic Structure Boundary Conditions — 색상 CSS 뒤에 수리 구조물(hydraulic structure) 경계 그룹의 생성·편집, 구조물 식과 유량 시계열(flow series) 지정을 설명한다(10). 모델은 일반적으로 구조물 위치 이외의 흐름을 격자 마스크(grid masks)로 막고 구조물이 마스크를 가로지르는 흐름을 허용하도록 구성한다고 적는다(10). 12행 `EE10_147.png`의 로컬 사본을 열었다. 그림은 상·하류 셀, 그룹 조건, 제어 규칙(control rules), 수두(head)와 유량 조회 표(flow lookup table)를 설정하는 창이다(12). 그림의 Head Lookup Equation(s) 식을 그대로 옮긴다: `HUP=HP+BELV+HQCTLUA+HQCTLU`, `HUN=HP+BELV+HQCTLDA+HQCTLD` (12행 그림). Figure 1 캡션과 빈 줄을 포함한다(13–14). |
| 15–31 | Boundary Condition Group / Flow Control Type — 그룹명, 유량 제어 유형, 시간 제어와 유량 배율(flow multiplier)을 입력하거나 선택한다(15). 원문: `In *Boundary Condition Group*frame, the user can enter the *Group Name,*or select from drop-down menus the appropriate *Flow Control Type,* *Time Control* and *Flow Multiplier*` (15). 유량 제어 유형은 수위-유량 곡선(rating curves) 또는 식에 기초한다(17). 수문(sluice gate)은 이들의 조합으로 규칙 기반 및 시간 변화 제어를 지원한다고 적는다(17). 원문 선택값: `- Upstream Elevation Whole Channel Rating` (19); `- Upstream Depth` (20); `- Elevation Difference` (21); `- Elevation Difference with Flow Accelerations` (22); `- US and DS Elevations` (23); `- Upstream Depth with Low Chord` (24); `- Elevation Difference with Low Chord` (25); `- Equation: Culvert` (26); `- Equation: Sluice Gate` (27); `- Equation: Weir` (28). 식과 유량 표 기반 구조물의 상세 설정은 Flow Derived Hydraulic Structures 링크로 안내한다(30). |
| 32–44 | Time Control — 시간 제어 목록은 Flow Control Type에서 수문 옵션을 선택했을 때만 활성화한다(32). 원문: `The *Time Control* drop-down menu is only enabled when the sluice gate option in *Flow Control Type*is selected.` (32). 두 Markdown 표의 빈 머리글·구분선과 Name/Meaning 머리글을 포함한다(34–39). 표의 옵션과 설명을 행별로 옮긴다. `Uncontrolled Structure` — `The hydraulic structure is uncontrollable type. The previous method of flow computational using lookup table or equation will be used` (40); `Controlled using Time-Series` — `The operation of the hydraulic structure is controlled using a time-series which defines the changes with time of gate openings or rating curves` (41); `Controlled based on Upstream Elevation` — `The operation of the hydraulic structure is controlled using control rules defined based on water surface elevation at an upstream location. This location can be different from the upstream cell of the structure.` (42); `Controlled based on Head Difference` — `The operation of the hydraulic structure is controlled using control rules defined based on the difference of water surface elevations at two locations upstream and downstream of the structure. These locations can be different from the upstream and downstream cells of the structure.` (43). 상류 수위 제어 지점은 구조물의 상류 셀과 달라도 된다(42). 수두 차 제어의 두 지점은 구조물의 상·하류 셀과 달라도 된다(43). |
| 45–48 | Flow Multiplier — 경계 유량 배율 목록의 식과 단위 유량(unit discharges)을 설명한다(45). 원문: `The user can also sets boundary *Flow Multiplier* options in the *Boundary Condition Group* frame. The drop-down menu allows selection from the following equations for the boundary flow multiplier, where q(h) are unit discharges and need to be multiplied by a dimension:` (45). 47행 `image2016-6-21_10213.png`의 로컬 사본을 열었다. 그림은 `Equation`, `Units for q` 두 열의 표이다. 표의 각 행을 LaTeX로 옮긴다: `Q=q(h)` — `L^3/T`; `Q=q(h)DY` — `L^2/T`; `Q=q(h)DX` — `L^2/T`; `Q=q(h)(DX+DY)` — `L^2/T` (47행 그림). 단위 열의 위첨자 1은 각주 표시다. 각주는 `Where L is length and T is time`이라고 적는다(47행 그림). |
| 49–51 | Downstream Cell / Rating Table — 구조물 하류 셀의 좌표 입력과 길이 L, 저면 고도, 초기 수심 표시를 설명한다(49). 원문: `The user may also input the cell downstream from hydraulic structure in the *Downstream I and J* boxes. The length "L", bottom elevation and initial depth are all displayed for the downstream cell.` (49). 표별 수두를 지정한 뒤 All로 현재 그룹의 셀에 현재 유량 표 설정을 적용한다(51). 원문: `In the  *Rating Table/Flow Lookup Table frame* shown in Figure 1 allows the user to set the head for each table. After the user has selected the table number, the *All* button applies the current flow table setting for cells in the current group. The user may also enter an *Head Offset* which will apply an offset to the result as described in the *Head Lookup Table Equations* frame.` (51). `Head Offset`의 효과는 Head Lookup Table Equations 프레임으로 안내한다(51). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·13: Figure 1 링크는 `#Figure1`이다. 캡션은 13행에 있으나 이 Markdown 파일에는 해당 ID의 앵커가 없다.
- 12행 그림·15–51: 그림의 수두 식은 `HUP`, `HUN`, `HP`, `BELV`, `HQCTLUA`, `HQCTLU`, `HQCTLDA`, `HQCTLD`를 사용한다. 이 파일 본문은 이 기호들을 정의하지 않는다.
- 45·47행 그림: 본문은 `q(h)`를 단위 유량이라고 적고 차원을 곱해야 한다고 설명한다. 그림 표에는 차원을 곱하지 않는 `Q=q(h)` 행도 있다.
