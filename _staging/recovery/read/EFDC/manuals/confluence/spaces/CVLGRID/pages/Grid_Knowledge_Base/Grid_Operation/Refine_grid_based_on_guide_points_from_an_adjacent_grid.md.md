---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Grid_Operation/Refine_grid_based_on_guide_points_from_an_adjacent_grid.md
lines: 32
sha256: 27d9b6cc76d6d563daa09e6df0858a827387bc34a70b9eba7b4839cf2f688d23
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Refine_grid_based_on_guide_points_from_an_adjacent_grid.md — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | Refine grid based on guide points from an adjacent grid / 목적 — 페이지 식별 정보를 포함한다(1–9). 작은 영역별 직교화(orthogonalization) 뒤 접촉면 절점 정렬이 맞지 않는 문제를 설명한다(10–12). 안내점(guide points)을 사용하여 첫 격자 절점을 유지하고 둘째 격자가 따르게 하는 목적을 원문대로 옮긴다. 원문: ``Before connecting two grids, we usually orthogonalize each grid first. The advantage of this activity is that Grid+ does orthogonalization quickly as the grid domain is small. However, grid nodes near the contact segment between two grids are not aligned, which can be a barrier when connecting two grids. So, this page will introduce steps on how to resolve this issue by using a feature from Grid+. Besides supporting grid connection, another purpose of using this option is to keep or fix the grid nodes from the first grid, and the grid nodes of the second grid must follow the first grid.`` (10). |
| 14–17 | Refine grid based on guide points from an adjacent grid / 선택·생성 — 첫 격자에서 안내점을 메모리로 복사하고 둘째 격자에 맞추어 새 격자를 만든다(14–16). 셀·절점·선택 수와 경계 포함 조건은 원문대로 보존한다. 원문: ``1. Left-mouse click (LMC) on a grid in the *Layer Control* panel (e.g., Grid 001), then LMC on a grid node, hold the Shift key, and left mouse click on the second node on the same grid segment. In this case, Grid 001 has six cells, so there are seven nodes, but we just select five nodes in between, not including two boundary nodes.  It will be highlighted, as shown in [Figure 2](#Refinegridbasedonguidepointsfromanadjacentgrid-Figure2). After that, right-mouse click (RMC) to show options, then select *Copy to Memory as Guide Points.*`` (14); ``2. LMC on the second grid in the *Layer Control* panel (e.g., Grid 003), hold the Shift key, and LMC on the second node on the same grid segment. For Grid 003, there are six cells, so there are seven nodes. We need to select six nodes, including two boundary nodes.  It will be highlighted, as shown in [Figure 3](#Refinegridbasedonguidepointsfromanadjacentgrid-Figure3). After that, RMC to show options, then select *Refine Grid according to Guide Points.*`` (15); ``3. As a result, a new grid is generated in the *Layer Control* (e.g., Grid 004). In this grid, we can see that the grid nodes in the contact area are aligned with the grid nodes of Grid 001, as shown in [Figure 4](#Refinegridbasedonguidepointsfromanadjacentgrid-Figure4). Now, we can connect Grid 001 with Grid 004 easily.`` (16). |
| 18–32 | Refine grid based on guide points from an adjacent grid / 그림 — 그림 1은 파란 Grid 001과 주황 Grid 003의 접촉면 절점이 어긋난 상태를 보여 준다(18). 그림 2는 `Copy to Memory as Guide Points` 메뉴와 `Columns 1 [11 - 11]`, `Rows: 5 [2 - 6]` 선택 정보를 보여 준다(22). 그림 3은 Grid 003의 검은 선택 외곽선과 `Refine Grid according to Guide Points` 메뉴를 보여 준다(26). 그림 4는 새 초록 `Grid 004`와 첫 파란 격자의 접촉 절점이 맞춰진 결과를 보여 준다(30). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14–15행: 첫 격자는 6셀·7절점 중 경계 두 절점을 제외한 5절점을 선택한다고 적는다. 둘째 격자도 6셀·7절점이라고 적지만 경계 두 절점을 포함해 6절점을 선택한다고 적으며 이 수의 이유는 설명하지 않는다.

