---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Grid_Operation/Merge_Two_Grids.md
lines: 44
sha256: 6b2bde7f522501f87e745e77f485261441c18fde34024eb2c74dc218243e1f99
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Merge_Two_Grids.md — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | Merge Two Grids / 생성·접속 조건 — 페이지 식별 정보를 포함한다(1–9). 복잡한 모델 영역을 여러 격자로 만든 뒤 병합(merge)하는 기능을 소개한다(10). 신규 스플라인 작성 순서, 가장자리 가까운 스플라인, 접속면 I 또는 J 셀 수의 일치 조건을 원문대로 옮긴다. 원문: ``To merge two grids, open the initial grid and then create a new layer for a new set of splines. These splines should extend from a location adjacent to the first grid and outline the new domain. Draw the farthest spline first, followed by the connection to the first grid and then the sides. When drawing the spline parallel to the first grid, ensure it is close to the edge. Generate the grid while ensuring that the number of cells in the I or J-axis of the new grid matches the number of cells connecting it to the first grid.`` (12). |
| 14–25 | Merge Two Grids / 표시·선택·실행 — 다른 격자의 가시성을 꺼야 한다(14). 접촉 격자선 두 절점 또는 겹친 블록을 선택한다(16). 모든 겹친 절점 선택은 필요하지 않다는 조건을 보존한다. 원문: ``Suppose there are two grids (red and blue) that are visible, as shown in [Merge Two Grids#Merge Two Grids#Figure 1](#MergeTwoGrids-Figure1), that we want to merge together. The visibility of all other grids should be turned off. These two grids meet the requirement for merging, as described above. Left-mouse click (LMC) on either grid01 or grid02 in the *Layer Control* panel to select it.`` (14); ``Set the cursor in selection mode by selecting the selection button from the toolbar or press **S** key from the keyboard, then LMC on the first node at the contacting edge, and hold the **SHIFT** key, then LMC on the second node along the contacting edge (note that the two nodes must be on the same grid line where two grids contact). If two grids have more than one overlapped grid line, you should select the block of overlapped nodes. In both cases, you don't have to select all overlapped grid nodes where the connection will occur, but you can select part of them where the nodes of two grids are mostly close to each other. Once the segment is highlighted, we can select one of three ways to merge them.`` (16); ``(1) Click the *Merge Two Grids* button from the main toolbar or,`` (18); ``(2) Go to the *Grid* menu then select *Merge Two Grids* option or,`` (20); ``(3) RMC to display options, select *Merge Two Grids* option.`` (22). 실행 경로는 도구모음, Grid 메뉴, RMC 메뉴 세 가지이다(18–22). |
| 26–33 | Merge Two Grids / 접촉면 그림 — 그림 1은 빨간 주 격자와 접촉하는 파란 분기 격자를 보여 준다(26). 그림 2는 접촉선을 자홍으로 선택한 상태와 도구모음·Grid 메뉴·RMC 메뉴의 `Merge Two Grids`를 가리키는 빨간 화살표를 보여 준다(30). |
| 34–44 | Merge Two Grids / 결과·중첩 블록 — 병합 결과는 새 레이어로 추가된다(34). 셀이 겹칠 때는 접촉 격자선 대신 블록을 정의한다고 적는다(36). 원문: ``After merging the two grids, a new grid layer (the result grid layer) is added to the *Layer Control* panel as shown in [Merge Two Grids#Merge Two Grids#Figure 3](#MergeTwoGrids-Figure3).`` (34); ``Grid+ also allows the merging of two grids in the case where there are overlapping cells as shown in [Merge Two Grids#Merge Two Grids#Figure 4](#MergeTwoGrids-Figure4). In this case, instead of defining a contacting gridline, we define a grid block and then select *Merge Two Grids* option.`` (36). 그림 3은 새 `Grid 003` 레이어의 주황 격자를 보여 준다(38). 그림 4는 두 격자의 중첩 블록을 검은 경계로 선택한 상태와 병합 아이콘을 가리키는 화살표를 보여 준다(42). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

