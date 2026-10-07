---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Grid_Operation/Insert_Cells.md
lines: 34
sha256: 0a710a315eb6eb27449e0f2c832e8d9cc5ff57fc6be504ddb794af679297e0f1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Insert_Cells.md — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | Insert Cells / 도입 — 페이지 식별 정보를 포함한다(1–9). 기존 격자에 단일 또는 여러 셀(cell)을 추가하는 방법을 소개한다(10). |
| 12–23 | Insert a single cell — 원문은 첫 절점 RMC, Shift와 두 번째 절점 LMC로 구간을 선택한 뒤 Line Mirror를 적용한다고 적는다(14). 적용 결과는 기존 셀과 격자선을 공유하는 셀이다(14). 원문: ``To insert a grid cell next to an existing cell, select two grid nodes of the existing cell (RMC on a node, hold the Shift key then LMC on the second node, the segment will be highlighted) then RMC to display options, select *Line Mirror* option as shown in [Insert Cells#Insert Cells#Figure 1](#InsertCells-Figure1). As a result, a cell will be added that shares a grid line with the existing cell as shown in [Insert Cells#Insert Cells#Figure 2](#InsertCells-Figure2).`` (14). 그림 1은 선택 구간과 `Line Mirror` 메뉴를 보여 주며 빨간 화살표가 삽입 위치를 가리킨다(16). 그림 2는 빨간 곡선형 격자의 외곽에 추가된 셀 하나를 가리킨다(20). |
| 24–34 | Insert multiple cells — 첫 절점 LMC, Shift와 두 번째 절점 LMC로 여러 셀 변을 포함하는 긴 격자선을 선택한 뒤 Line Mirror를 적용한다(26). 원문: ``The method to insert multiple cells is similar to inserting a single cell, the difference is in the selected grid line. In this case, we select a longer grid line that contains many cell sides in the same line by LMC on the first node then hold Shift and LMC on the second node ([Insert Cells#Insert Cells#Figure 3](#InsertCells-Figure3)), then RMC to display options, and then select the *Line Mirror* option. As a result, a number of cells will be added as shown in [Insert Cells#Insert Cells#Figure 4](#InsertCells-Figure4).`` (26). 그림 3은 자홍 선택 구간과 `Line Mirror` 메뉴를 보여 주며 화살표가 긴 삽입 구간을 가리킨다(28). 그림 4는 해당 외곽에 셀 한 줄이 추가된 결과를 보여 준다(32). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14·26행: 단일 셀의 첫 절점 선택은 `RMC`로 적지만 여러 셀의 첫 절점 선택은 `LMC`로 적는다.

