---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Grid_Operation/Redistribute_Grid_Nodes.md
lines: 46
sha256: d61e3104f264e8ece59d3ca64a358789fb6faec0b345c9efe57cdc629d7bf6f9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Redistribute_Grid_Nodes.md — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | Redistribute Grid Nodes / Line Smooth 도입 — 페이지 식별 정보를 포함한다(1–9). 격자 영역을 고르게 하고 절점(node) 사이 거리를 재배치(redistribution)하기 위한 Line Smooth를 소개한다(10–12). |
| 14–24 | Line Smooth / 적용·그림 — 같은 격자선의 절점 두 개를 선택하고 적용 후 격자를 다시 직교화하라는 권고를 포함한다(15). 원문: ``2. RMC on a node, hold the Shift key then LMC on the second node (these two nodes must be on the same gridline), and the segment will be highlighted. RMC to display the options, and select the *Line Smooth* option as shown in [Figure 1](#RedistributeGridNodes-Figure1). As a result, grid nodes are distributed along with the selected segment as shown in [Figure 2](#RedistributeGridNodes-Figure2). Note that after applying this option, the grid should be orthogonalized again.`` (15). 그림 1은 주황 곡선형 격자의 자홍 선택 구간과 `Line Smooth` 메뉴를 보여 준다(17). 그림 2는 선택 방향으로 절점 간격이 고르게 바뀐 격자를 보여 준다(21). |
| 25–39 | Line Attraction — 선택 격자선 쪽으로 영향 영역 절점을 이동시키는 기능이다(27). 두 가장자리 절점과 세 번째 절점의 선택 조건을 보존한다. 원문: ``The *Line Attraction* tool is used to shift grid nodes forward to certain point or line. The nodes within a defined area are moved in the direction a gridline selected by the user. `` (27); ``2. Set the mouse in the selection mode, hold the Shift key then LMC on two edge grid nodes on the same grid line segment. The segment will be highlighted in purple, then LMC on the third grid node to define the area to be affected.  Next, release Shift, then RMC to show options, and select the  *Line Attraction* option, as shown in [Figure 3](#RedistributeGridNodes-Figure3). As a result, a set of nodes will be moved forward to the gridline segment as shown in [Figure 4](#RedistributeGridNodes-Figure4).`` (30). 그림 3은 빨간 영향 범위·자홍 선택 구간과 `Line Attraction` 메뉴를 보여 준다(32). 그림 4는 영향 영역의 격자선이 선택 경계 쪽으로 더 가까워진 결과를 보여 준다(36). |
| 40–46 | Line Repulsion — 선택 격자선에서 멀어지도록 영향 영역 절점을 이동한다(42). 범위 선택은 Attraction과 같다는 조건을 원문대로 옮긴다. 원문: ``The *Line Repulsion* option is opposite to the *Line Attraction* option in that the nodes in the defined area are moved away from the selected grid line. The steps to define the selected gridline and impacted area are similar to the *Line Attraction* option described above. After defining the impacted area, RMC to display options, and select the *Line Repulsion* as shown in [Figure 5](#RedistributeGridNodes-Figure5).`` (42). 그림 5는 선택 구간·영향 범위와 `Line Repulsion` 메뉴를 보여 준다(44). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 15·30행: Line Smooth의 첫 절점 선택은 `RMC`로 적으며 Line Attraction의 절점 선택은 `LMC`로 적는다.

