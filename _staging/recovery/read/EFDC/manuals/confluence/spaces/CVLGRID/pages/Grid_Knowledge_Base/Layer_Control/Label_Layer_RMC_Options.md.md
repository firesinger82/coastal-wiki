---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Layer_Control/Label_Layer_RMC_Options.md
lines: 81
sha256: 0b0ca5f4d7c1e12b94884b41ed61a44e5f0e0f4442f7db4915e174e19a9b0e6e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Label_Layer_RMC_Options.md — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | Label Layer: RMC Options / 도입 — 페이지 식별 정보·판본·수정 시각을 포함한다(1–9). CSS 규칙 뒤에 트리의 라벨(layer label) 제목에서 우클릭(RMC, Right Mouse Click)하여 옵션을 연다고 적는다(10). Table 1 참조 URL은 Overlay Layer 문서를 가리킨다(10). |
| 12–23 | 라벨 파일 형식 — Labels.dat 첫 열은 X 좌표, 둘째 열은 Y 좌표, 셋째 열은 라벨 이름이라고 적는다(12). 헤더와 입력 예시 세 줄을 그대로 옮긴다. 원문: ``Label files (Labels.dat) have a format where the first column is the X coordinate, the second column is the Y coordinate, and the third column is the label name.`` (12); ``X, Y, Name`` (16); ``718099.47, 4329198.13, P1`` (18); ``709826.94, 4329920.53, P2`` (20). 라벨 표시를 위해 파일을 먼저 가져온 다음 레이어에서 RMC하여 옵션을 연다(22). 조건과 순서를 그대로 옮긴다. 원문: ``To display labels, first import the label file, then RMC on that layer to display options as shown in [Figure 1](#LabelLayer:RMCOptions-Figure1). These options are summarized in the [Table 1](#LabelLayer:RMCOptions-Table1).`` (22). |
| 24–40 | Figure 1·Table 1 / 라벨 레이어 메뉴 — Properties, Import, Export, Remove, 새 스플라인(spline)·오버레이(overlay) 레이어, 모든 레이어 표시 전환을 설명한다(32–39). 표의 모든 행을 옮긴다. 원문: ``\| Properties \| Set properties of the selected layer (described in detail below) \|`` (32); ``\| Import \| Import the label layer \|`` (33); ``\| Export \| Export the label layer to an external file \|`` (34); ``\| Remove \| Delete the selected layer \|`` (35); ``\| Create New Spline Layer \| Create a new spline layer in the layer control panel \|`` (36); ``\| Create New Overlay Layer \| Create a new overlay layer in the layer control panel \|`` (37); ``\| Turn All Layers Off \| Hide all existing layers in the layer control panel \|`` (38); ``\| Turn All Layers On \| Display all existing layers in the layer control panel \|`` (39). 직접 연 그림(24): 위성 배경과 하천 격자 위 P2 라벨 및 빨간 원 표지가 보인다. Labels 레이어의 RMC 메뉴에는 Properties, Import, Export, Remove, 새 레이어 생성, 전체 레이어 표시 전환이 있다. 캡션과 빈 줄을 포함한다(25–40). |
| 41–60 | Label Properties / 텍스트·표지 설정 — RMC 후 Properties로 설정 창을 연다(43). Show Text 해제는 텍스트를 숨기며 Font 버튼으로 글꼴 모양·크기를 정한다(45). Show Symbol 해제는 라벨 표지(symbol)를 숨기며 Symbol 버튼으로 표지 설정을 연다(47). 적용 조건을 그대로 옮긴다. 원문: ``*Show Text*: Unchecking this box will hide the label text, click the *Font* button to set font style and text size ([Figure 3](#LabelLayer:RMCOptions-Figure3)).`` (45); ``*Show Symbol*: Unchecking this box will hide the symbol of the labels, click the *Symbol* button to make settings for symbols ([Figure 4](#LabelLayer:RMCOptions-Figure4)).`` (47). 직접 연 그림(49): Label Properties에서 P1이 선택되어 있다. 화면 예시: `Text: P1`, `Show Text` 체크, `Show Symbol` 체크, `Angle (Deg.): 0.00`, `X (m): -84.48`, `Y (m): 39.08`, `Z (m): 0.00`, `X (pixels): 0.00`, `Y (pixels): 0.00`, `Horizontal: Right`, `Vertical: Center`. `Text Color`의 `Color`는 빨강이며 텍스트 `Outline Color`와 `Box Color`의 `Background` 및 `Outline`은 체커무늬 견본이다. `Sample Text`가 빨강으로 보인다. 직접 연 그림(53): Font 버튼에서 Font 창으로 향하는 빨간 화살표가 보인다. 화면 선택은 `Font: Arial`, `Font style: Bold`, `Size: 18`, `Script: Western`이다. `Strikeout`, `Underline`은 체크되지 않았다. Sample은 `AaBbYyZz`이다. 크기 목록에서 보이는 값은 `18`, `20`, `22`, `24`, `26`, `28`, `36`이다. 목록이 더 이어지므로 이 값을 설정의 전체 범위라고 적지 않는다. 직접 연 그림(57): Symbol 버튼에서 Symbol Marker 창으로 향하는 빨간 화살표가 보인다. 화면 선택은 `Style: Circle`, `Size: 8.0`, `Pixels` 선택, `Meters` 미선택, `OpenGL Point` 미체크, `Outline Thickness: 1.0`이다. `Fill Color`는 빨강이고 `Outline Color`는 검정이며 Preview에는 작은 빨간 원이 보인다. 설정 값은 화면 예시이며 문서에서 기본값으로 명시하지 않는다. |
| 61–76 | Label Properties / 목록 선택·정렬·색 — 왼쪽 Labels 패널에서 RMC하면 선택·해제·삭제 옵션이 나온다고 적는다(61). 네 옵션의 원문을 옮긴다. 원문: ``*Select All Items*: Selects all the existing items in the panel.`` (63); ``*Select No Items*: Unselects all existing items in the panel.`` (65); ``*Remove Selected Items*: Delete the selected items.`` (67); ``*Remove All Items*: Delete all existing items in the panel.`` (69). Alignment에서 가로·세로 정렬을 정하며 Text Color와 Box Color에서 텍스트·배경 색을 정한다(71). 원문: ``The *Alignment* frame is you settings the alignment of text in horizontal and vertical directions are made. The color of text and background color can be set in the *Text Color* and *Box Color* frames.`` (71). 직접 연 그림(73): Labels 목록의 P1과 P2가 선택되어 있고 빨간 `RMC` 주석이 있다. 메뉴는 `Select All Items`, `Select None Item`, `Remove Selected Items`, `Remove All Items`이다. `Apply all labels`는 체크되지 않았다. 나머지 보이는 설정 값은 49행 그림과 같다. 캡션은 LMC라고 적는다(75). |
| 77–81 | Label Properties / 설정 적용·내보내기 — 텍스트·표지 설정 후 OK로 적용한다(77). 원문은 LMC에서 Export를 선택하고 Save As에서 이름·형식을 정하며 `\*.lbl`을 설정 저장용 확장자로 설명한다(77). 마지막 버튼은 원문대로 OK라고 옮긴다. 원문: ``After setting properties for labels (text, symbol), click the *OK* button to apply the settings. We can save the settings for the labels by using the *Export* option from LMC. Select this option, the *Save As* will be displayed, as shown in [Figure 6](#LabelLayer:RMCOptions-Figure6). Put a file name and select file type (\*.lbl is an extension to save the settings). Then click the *OK* button.`` (77). 직접 연 그림(79): Save As 화면의 예시 선택은 `File name: Labels.lbl`, `Save as type: Label Files(*.lbl,*.dat,*.txt)`이다. 파일 목록에 Labels.dat와 Labels.lbl이 있고 저장 버튼은 `Save`이다. Figure 6 캡션과 빈 줄을 포함한다(80–81). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 본문 앞에 `[data-colorid=umub19o2pk]` 등 CSS 규칙이 붙어 있다.
- 10행: Table 1 링크의 URL은 `2123727100/Overlay+Layer+RMC+Options#OverlayLayer:RMCOptions-Table1`이다. 이 파일의 Label Layer 표가 아닌 다른 제목을 가리킨다.
- 61·73·75행: 본문은 `RMC`를 쓰며 Figure 5에도 빨간 `RMC`가 보인다. Figure 5 캡션은 `LMC options`이다.
- 65·73행: 본문 메뉴 이름은 `Select No Items`이며 그림 메뉴 이름은 `Select None Item`이다.
- 10·22·24·77행: 라벨 레이어 옵션은 RMC로 설명되며 Figure 1의 메뉴에 Export가 있다. 77행은 Export를 `from LMC`로 설명한다.
- 77·79행: Save As에서 마지막에 누르는 버튼을 본문은 `OK`라고 적는다. Figure 6의 저장 버튼은 `Save`이다.

