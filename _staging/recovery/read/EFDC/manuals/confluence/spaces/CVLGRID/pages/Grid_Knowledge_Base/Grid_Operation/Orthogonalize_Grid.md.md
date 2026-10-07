---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Grid_Operation/Orthogonalize_Grid.md
lines: 57
sha256: aeb1114fd1e6ac9f4538edab3590892704878d679717b3c9a6e3a49cfbf8b130
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Orthogonalize_Grid.md — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | Orthogonalize Grid / 기준·표시 — 페이지 식별 정보를 포함한다(1–9). 직교성(orthogonality) 최적화와 직교 편차(orthogonal deviation) 감소를 설명한다(10). 대부분의 EFDC 모델에 대한 권고 조건의 원문은 다음과 같다. 원문: ``The computational accuracy of a model is increased when the orthogonality of a grid is optimized. A perfect grid would have all cells perpendicular to the boundary lines. In practice, this is very difficult to achieve, and thus, for most EFDC models an orthogonal deviation of less than 3o is recommended. The orthogonalization tool is used to reduce the orthogonal deviation of a grid.`` (10); ``To view the orthogonal deviation of a grid, LMC on the grid layer in the *Layer Control* then RMC on that grid layer to show RMC's options, select *Show Properties/Orthogonal Deviation* as shown in [Figure 1](#OrthogonalizeGrid-Figure1). In addition, the orthogonal deviation of a grid can be viewed from the *Grid* menu as shown in [Figure 2](#OrthogonalizeGrid-Figure2).`` (12). |
| 14–27 | Orthogonalize Grid / 표시 그림·방법 — 그림 1은 레이어 RMC의 `Show Properties`·`Orthogonal Deviation`을 보여 준다(14). 그림 2는 Grid 메뉴의 `Show Grid Properties`·`Orthogonal Deviation`을 보여 준다(18). 그림 3은 색칠한 곡선형 격자와 `Orthogonal Deviation, Mean: 27.91 (°)` 범례를 보여 준다(22). 범례 눈금은 `0.03, 18.50, 36.97, 55.45, 73.92`이다(22). 전체 격자와 격자 블록의 두 적용 방법을 소개한다(26). |
| 28–40 | Othogonalize the entire grid — 선택 레이어 전체에 즉시 적용한다고 적는다(30–31). 원문: ``2. From *Grid* menu, select *Orthogonalize Grid*, or click on the *Orthogonalize grid* button from the main toolbar as shown in [Figure 4](#OrthogonalizeGrid-Figure4). When this is done the entire grid will be immediately orthogonalized. [Figure 5](#OrthogonalizeGrid-Figure5) shows a change in orthogonality of the grid after applying *Orthogonalize Grid.*`` (31). 그림 4는 메뉴와 아이콘을 향하는 양쪽 빨간 화살표와 적용 전 범례를 보여 준다(33). 이 범례는 `Orthogonal Deviation, Mean: 27.91 (°)`이며 눈금은 `0.03, 18.50, 36.97, 55.45, 73.92`이다(33). 그림 5는 직교화 후 격자와 `Orthogonal Deviation, Mean: 0.64 (°)`를 보여 준다(37). 적용 후 눈금은 `0.00, 2.46, 4.92, 7.38, 9.84`이다(37). 그림의 평균과 최대 눈금을 서로 바꾸어 설명하지 않았다. |
| 41–57 | Orthogonalize a grid block — Shift로 두 절점을 선택하여 블록을 표시하고 메뉴·도구모음·RMC 중 한 경로로 즉시 직교화한다(43–45). 원문: ``2. From the main toolbar, select the *Select object* button then select a grid node, hold the Shift key and select the second grid node. The grid block will be highlighted as shown [Figure 6](#OrthogonalizeGrid-Figure6).`` (44); ``3. Next, from *Grid* menu, select *Orthogonalize Grid* or click on the *Orthogonalize grid* button from the main toolbar. A further option is to select *Orthogonalize Grid Block* from the RMC options as shown in [Figure 7](#OrthogonalizeGrid-Figure7). As a result, the grid block will be immediately orthogonalized. [Figure 8](#OrthogonalizeGrid-Figure8) shows a change in orthogonality of the grid after applying *Orthogonalize Grid* for a grid block.`` (45). 그림 6은 빨간 선택 블록 경계를 보여 준다(47). 그림 7은 `Orthogonalize Grid Block` 메뉴를 보여 준다(51). 그림 8은 선택 블록 안 격자선 교차가 바뀐 결과를 보여 준다(55). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 권고 각도는 `3o`로 표기되어 있다. 22·37행 그림의 각도 단위는 `°`로 표시된다.

