---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Grid_Masks_1.md
lines: 105
sha256: 9b29fe5f01e84d59708f48cfa704485a3d7b4cb52c837a02f720beabfe7f8b48
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Grid_Masks_1.md — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–29 | General Purpose — 격자 마스크(grid mask)는 셀 면의 얇은 댐이며 셀 사이의 흐름을 완전히 또는 부분적으로 막는다(12). 완전 차단은 수주(water column)의 상단부터 하단까지 물의 이동을 막는다(14). 부분 차단은 고정 물체와 부유 물체를 구분하며 수위 변화에 따라 물체 아래 흐름이 달라질 수 있다(16). 치수 정의 원문: `Anchor Elevation: if set to zero, the object on the water will be considered as floating (e.g., ships). Otherwise, it is a fixed object (e.g, bridges, docks).` (24); `Draft: the thickness of the floating or fixed object on the water.` (25); `Clearance: is the thickness of space between the Draft and Bottom Sill when it equals 0. The object plays the role of a fully-blocking mask. Otherwise, it is a partial blocking mask.` (26); `Bottom Sill: the thickness of a solid structure on the surface of the riverbed.` (27); `Bottom: means the riverbed.` (28). 그림 1을 직접 열었다(18–20). 위의 회색 `Floating or Fixed Object`, 가운데 파란 개구부, 아래 회색 sill과 갈색 하상을 보여 준다. 수평 점선은 `Anchor Elevation (m)`, `WSEL`, `Bottom`이다. 오른쪽 수직 양방향 화살표는 위에서부터 `Draft (m)`, `Clearance (m)`, `Bottom Sill (m)`이며 각 경계 사이의 두께를 나타낸다. 그림에 수식은 없다. |
| 30–58 | 2DH View / Adding New Masks to Grid Cells — Masks 레이어의 전구·포인터·펜을 켠 뒤 단일 셀 또는 여러 셀에 마스크를 지정한다(34–36). 서쪽과 남쪽 면 모두, 남쪽 면만, 서쪽 면만 완전히 차단하는 메뉴와 부분 차단 편집 메뉴를 열거한다(38–41). 셀 인덱스 원문: `L, I, J indices` (41), `I, J, L index` (43). 부분 차단 편집의 기본값과 조건 원문: `so the checkbox *Floating* is checked by default.`; `In addition, the *Anchor Elevation* box is greyed out, so it is non-editable.`; `The user can now enter values for the *Draft* and *Bottom Sill.*`; `When the *Floating* checkbox is unchecked then the *Anchor Elevation* box can be edited.`; `If the value entered is non-zero, the mask is now partially blocking as a fixed object.` (모두 41). 목록의 기존 셀을 편집하며 왼쪽 화살표는 추가, 오른쪽 화살표는 선택 셀 제거, 이중 오른쪽 화살표는 전체 제거에 사용한다(43). 여러 셀은 Ctrl과 왼쪽 클릭 또는 Shift와 왼쪽 클릭으로 먼저 선택한다(57). 그림 2는 Masks 레이어의 활성 아이콘을 보여 준다(45–47). 그림 3은 격자 셀의 마스크 추가 메뉴를 보여 준다(49–51). 그림 4는 `Vertical Cell Face Blocking` 창의 서쪽 `West (U) Face`와 남쪽 `South (V) Face` 입력란을 보여 준다(53–55). 그림의 셀은 I=220, J=31, L=1157이며 두 면 모두 Floating이 체크되어 있다. 그림에 표시된 치수 입력값은 각각 `Anchor Elev. (m): 0`, `Draft (m): 0`, `Bottom Sill (m): 0`이다(53행 그림). 이 값은 화면 예시 값이다. |
| 59–83 | GUI Editing — 레이어 메뉴는 표시 속성, 레이어 변경, 셀 차단 편집, 마스크 셀로 확대, 레이어 제거를 제공한다(61–67). 표시 설정 원문: `Layer Name` (63); `Layer Visible` (63); `Show in Legend` (63). 범례 표시의 적용 조건 원문: `Checking this box is only applied when the *Layer Visible* option is checked*.*` (63). 레이어 변경 필드 원문: `Primary Group`와 `Parameter` (64). 그림 5는 레이어의 Properties·Edit·Edit Cell Blocking Masks·Zoom to Layer·Remove 메뉴를 보여 준다(69–71). 그림 6은 Mask Properties 창을 보여 준다(73–75). 그림에서 완전 차단 선은 Solid·검정·Width 3.00이며 부분 차단 선은 Dash·검정·Width 5.00이다. 이 값은 화면 예시 값이다. 그림 7은 `Primary Group: Model Grid`, `Parameter: Masks`인 2DH View Option 창을 보여 준다(77–79). 그림 8은 마스크 셀 목록과 읽기 전용 초기 조건, 두 면의 완전 차단 체크 상태를 보여 준다(81–83). |
| 84–98 | GUI Editing / 기존 마스크 변경과 삭제 — 모든 마스크 셀을 목록에 표시하며 초기 하상 표고(bottom elevation), 수심(water depth), 수면 표고(water surface elevation)는 편집할 수 없다(85). 원문은 `cell (L=97)`와 `Completely Block Mask`를 적는다(85). 완전 차단을 부분 차단으로 바꾸려면 해당 체크를 해제하고 Floating 상태와 Draft·Bottom Sill을 지정한 뒤 Close를 누른다(87). 셀의 오른쪽 클릭 메뉴에서 Delete로 마스크를 지운다(89). 그림 9를 직접 열었다(91–93). I=193, J=19, L=97인 셀의 서쪽 완전 차단은 해제되어 있고 Floating은 체크되어 있다. 서쪽 `Draft (m)`는 `4`, `Bottom Sill (m)`는 `1`이며 남쪽 완전 차단은 유지된다. 그림 10은 서쪽 마스크 삭제 메뉴 `Delete West Completely Blocking Mask`를 보여 준다(95–97). |
| 99–105 | EFDC+ Input File — `mask.inp`에는 마스크 셀 수와 `I`, `J`, `MTYPE` 세 열을 쓴다(101). `MTYPE`는 셀에 설정한 마스크 유형이다(101). 그림 11의 입력 예제를 직접 열었다(103–105). 그림 내부 주석 원문: `C MASK.INP - GRID CELL MASKS - Version: 10.2` (103행 그림, 내부 1행); `C Project: EFDC+ Testing` (내부 2행); `C MMASK: # MASKS, MTYPE: 1 = Force V Component Only` (내부 3행); `2 = Force U Component Only` (내부 4행); `3 = Both U and V Components` (내부 5행); `4 = Isolated cell` (내부 6행); `C I J MTYPE` (내부 7행). 셀 수는 `28` (내부 9행)이다. 세 열의 행별 값은 `193 19 2` (내부 10행); `194 19 2` (11); `206 23 1` (12); `206 24 1` (13); `206 25 2` (14); `221 31 1` (15); `221 32 1` (16); `141 34 1` (17); `16 35 1` (18); `141 35 1` (19); `16 36 1` (20); `22 36 1` (21); `69 36 1` (22); `77 36 1` (23); `140 36 2` (24); `16 37 1` (25); `22 37 1` (26); `16 38 1` (27); `22 38 1` (28); `16 39 1` (29); `22 39 2` (30); `23 39 2` (31); `24 39 2` (32); `16 40 1` (33); `27 40 2` (34); `28 40 2` (35); `226 42 3` (36); `225 43 2` (37). 그림에서 식별한 각 열의 값을 옮겼으며 이미지의 공백 폭을 문자 수로 환산하지 않았다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 61·71: 본문은 레이어 메뉴를 LMC로 연다고 적지만 그림 5 캡션은 `RMC options for Grid Mask layer`라고 적는다.
- 85·81·91: 본문 체크 상자 이름은 `Completely Block Mask`이며 그림 8·9의 이름은 `Completely Blocked Mask`이다.

