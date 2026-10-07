---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Grid_Operation/Refine_Grid.md
lines: 66
sha256: 9155872532059663f8a6c8c40123ff6665d88c57962d3287bc929f4d2bec2a0c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Refine_Grid.md — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | Refine Grid / 도입 — 페이지 식별 정보를 포함한다(1–9). 격자 세분화(grid refinement)는 기존 셀 수에 IC, JC를 독립적으로 곱해 해상도를 높인다(10). 변수 이름과 적용 분류를 원문대로 보존한다. 원문: ``The *Refine* *grid* option is used to increase the resolution of the grid. It operates by multiplying the existing number of cells in the current grid with (IC, JC) independently. There are two grid refinement types, refining a grid globally or refining locally for a selected block of cells:`` (10). |
| 12–29 | Refine grid globally — Grid 메뉴 또는 도구모음에서 전체 격자를 세분화한다(14–15). 기본값, 이전 인자 유지, 예시와 1x1 조건을 그대로 옮긴다. 원문: ``3. The *Grid Block Refinement* form will be popup, as shown in [Figure 2](#RefineGrid-Figure2). The user needs to enter the *Refinement Factor* then click *OK* button. The default value for factors is 5. The next time when refining the grid the refinement factor will remember the values from the previous time, [Figure 3](#RefineGrid-Figure3) show examples for grid refinement with factors are 2x2. In case, entering the factors are 1x1 then the grid remains as before refining.`` (16). 그림 1은 메뉴와 도구모음의 Refine Grid 위치를 가리키는 빨간 화살표를 보여 준다(18). 그림 2의 두 그룹 제목은 모두 `Refinement in I Direction`이며 각각 `Refinement Factor: 5`가 보인다(22). 그림 3은 전체 격자선이 늘어난 결과를 보여 준다(26). |
| 30–48 | Refine grid with a selected grid segment — S 또는 선택 도구와 같은 I 또는 J 구간의 두 절점을 사용한다(32–34). 구간 방향에 따른 인자 활성 조건을 원문대로 옮긴다. 원문: ``1. Set cursor in selection mode (press the S key or click the *Select object* button from the main toolbar.`` (32); ``3. LMC on a grid node then hold the Shift key. Then LMC on the second node on the same grid segment in I or J direction. The segment will be highlighted with purple color as shown in [Figure 4](#RefineGrid-Figure4).`` (34); ``4. Select *Refine Grid* button from the main toolbar or access *Refine Grid* option from the *Grid*menu, the *Grid Block Refinement* form will be popup as shown in [Figure 5](#RefineGrid-Figure5). Either refinement factor for the I direction or refinement factor for the J direction is enabled. It depends on the grid segment is on which direction. In this case, we can enter the *Refinement Factor* for the I direction, then click the *OK* button. [Figure 6](#RefineGrid-Figure6) shows an example of grid refinement with a selected grid segment.`` (35). 그림 4는 격자 가장자리의 자홍 선택 구간을 보여 준다(37). 그림 5는 두 그룹 제목이 모두 `Refinement in I Direction`이며 위쪽 `Refinement Factor: 2`가 활성, 아래쪽 `Refinement Factor: 2`가 비활성이다(41). 그림 6은 화살표가 가리키는 구간에서 격자선이 늘어난 결과를 보여 준다(45). |
| 49–66 | Refine the grid with a selected grid block — 같은 I 또는 J 구간에 있지 않은 두 절점으로 블록(block)을 선택하고 인자를 적용한다(51–54). 원문: ``1. Set cursor in selection mode (press the S key or click the *Select object* button from the main toolbar.`` (51); ``3. LMC on a grid node then hold Shift key, LMC on the second node which is not on same grid segment in I or J direction, the grid block will be highlighted as shown in [Figure 7](#RefineGrid-Figure7).`` (53); ``4. From *Grid* menu, select *Refine Grid* option (or select *Refine Grid* button from the main toolbar), the *Grid Block Refinement* form will be popup as shown in [Figure 8](#RefineGrid-Figure8). The user needs to enter the *Refinement Factor* then click *OK* button. [Figure 9](#RefineGrid-Figure9) show examples for grid refinement with a selected grid block.`` (54). 그림 7은 선택 블록과 Grid Block Refinement 창을 보여 준다(56). 이 창의 `Refinement in I Direction` 인자는 `3`, `Refinement in J Direction` 인자는 `2`이다(56). 그림 8에서는 두 그룹 제목이 모두 `Refinement in I Direction`이며 위·아래 인자는 `3`, `2`이다(60). 그림 9는 선택 구역의 격자선 수가 늘어난 결과를 보여 준다(64). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·30·49행: 도입은 세분화를 전체·선택 블록의 두 유형으로 소개하지만 본문에는 선택 구간 절도 있다.
- 22·41·60행: 설정 그림의 두 그룹 제목이 모두 `Refinement in I Direction`이다. 56행 그림은 I와 J 제목을 구분한다.

