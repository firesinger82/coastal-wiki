---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Grid_Operation/Delete_Grid_Nodes.md
lines: 60
sha256: 730b24988b48a240739ffc6e2ea86bf46d2f02585824b99cb09cb1d501e6ce2a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Delete_Grid_Nodes.md — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | Delete Grid Nodes / 도입 — 페이지 식별 정보를 포함한다(1–9). 수역 밖 등 원하지 않는 셀을 제거하기 위한 단일 절점·블록·다각형(polygon) 방법을 소개한다(10). |
| 12–22 | Delete single grid node — 격자를 불러온 뒤 레이어와 Delete node 도구를 선택한다(14–17). 반복 삭제와 종료 키를 원문대로 보존한다. 원문: ``2. From the main toolbar, select the *Delete node* button then LMC on a grid node to delete node as shown in [Figure 1](#DeleteGridNodes-Figure1). Keeping LMC on other nodes will delete those nodes also. To end using the delete function, click the select object button from the main toolbar or press the S key.`` (17). 그림 1의 위쪽 화살표는 삭제 도구를, 오른쪽을 향하는 화살표는 곡선형 격자에서 절점 삭제로 빠진 구역을 가리킨다(19). |
| 23–44 | Delete grid nodes with a grid block selection — 같은 격자선에 있지 않은 절점을 Shift로 선택하여 블록 안 또는 밖의 절점을 삭제한다(25–31). 원문: ``3. Hold the Shift key and LMC on another grid node (that one is not on the same grid line as the previous one), and the grid block defined by the two selected nodes will be highlighted ([Figure 2](#DeleteGridNodes-Figure2)).`` (29); ``After step 3, we can delete nodes inside by accessing the *Grid* menu, and selecting the *Delete Selected Grid Block* option. Alternatively, RMC to display options then select *Grid Grid Block* option, as shown in [Figure 3](#DeleteGridNodes-Figure3). To delete grid nodes outside a grid block, select *Delete Grid Nodes Outside a Block* option from the RMC options, as shown in [Figure 4](#DeleteGridNodes-Figure4).`` (31). 그림 2는 선택 블록의 경계를 파랑으로 표시한다(33). 그림 3은 `Delete Selected Grid Block`과 우클릭 메뉴의 `Delete Grid Block`을 함께 보여 준다(37). 그림 4는 `Delete Grid Nodes Outside a Block` 메뉴를 보여 준다(41). |
| 45–60 | Delete grid nodes with a polygon — 외부 다각형 또는 새 다각형으로 안·밖을 삭제할 수 있으며 Polygon Selection Mode도 사용할 수 있다(47). 다각형 그리기·선택·격자 레이어 선택·삭제의 조건과 메뉴를 그대로 옮긴다. 원문: ``For this option, we can remove nodes inside or outside of a polygon. The polygon can be loaded from an external file or after drawing a new one. You can also use the *Polygon Selection Mode* to select grid nodes.`` (47); ``1. From the main toolbar, click *Add a new polyline* button then start drawing the polygon by LMC and end by RMC (the polygon overlays the grid) as shown in [Figure 5](#DeleteGridNodes-Figure5). If the polygon file is available from an external source, skip the drawing polygon steps and load the polygon file into the workplace.`` (49); ``2. Select the *Select object* button from the main toolbar, select the overlay layer (the polygon layer) in the *Layer Control* panel. Then LMC on the polygon and it will be highlighted.`` (50); ``3. LMC on the grid layer in the *Layer Control.* it means selecting the grid that we want to delete nodes.`` (51); ``4. While the selected polygon is still highlighted, RMC to display various options. Select *Delete Grid Nodes Inside the Selected Polygon* to delete the grid nodes inside the polygon or selecting *Delete Grid Nodes Outside the Selected Polygon* to delete the grid nodes outside the polygonas shown in [Figure 6](#DeleteGridNodes-Figure6).`` (52). 그림 5는 격자와 겹친 파란 다각형을 보여 준다(54). 그림 6은 빨간 선택 다각형과 `Delete Grid Nodes Inside the Selected Polygon`, `Delete Grid Nodes Outside the Selected Polygon` 메뉴를 보여 준다(58). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 31·37행: 블록 안 삭제의 우클릭 메뉴를 본문은 `Grid Grid Block`으로 적으며 그림 3은 `Delete Grid Block`으로 표시한다.

