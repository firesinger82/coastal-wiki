---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Grid_Operation/Coarsen_Grid.md
lines: 62
sha256: 73a4bf96df9d77f0fee40d537ac845403dc7e373453abc95e88f6ccb36f006d5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Coarsen_Grid.md — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | Coarsen Grid / 도입 — 페이지 식별 정보를 포함한다(1–9). 성긴 격자 변환(coarsening)은 I, J 방향의 기존 셀 수를 독립적으로 나누어 해상도(resolution)를 낮춘다(10). 전체·구간·블록(block)의 세 방법을 소개한다(10). |
| 12–25 | Coarsen grid globally — 레이어 선택 후 Grid 메뉴 또는 도구모음에서 실행한다(14–15). 기본 인자는 원문대로 보존한다. 원문: ``3. The *Grid Block Coarsening* form will be displayed, as shown in [Figure 1](#CoarsenGrid-Figure1). Enter the *Coarsening Factor* then click the *OK* button. The default value for factors is 2. [Figure 2](#CoarsenGrid-Figure2) shows an example of grid refinement.`` (16). 그림 1은 메뉴와 도구모음에서 설정 창을 향하는 빨간 화살표를 보여 준다(18). 창의 `Coarsening in I Direction`, `Coarsening in J Direction` 각각에 `Coarsening Factor: 2`가 보인다(18). 그림 2는 더 큰 셀로 바뀐 빨간 곡선형 격자를 보여 준다(22). |
| 26–44 | Coarsen grid with a selected grid segment — 같은 I 또는 J 방향 구간의 두 절점을 Shift로 선택하고 인자를 입력한다(28–31). 적용 선택 조건을 그대로 옮긴다. 원문: ``3. LMC on a grid node then hold Shift key. LMC on the second node on same grid segment in I or J direction, and the segment will be highlighted as shown in [Figure 3](#CoarsenGrid-Figure3).`` (30); ``4. From *Grid* menu, select *Coarsen Grid* option (or select the *Coarsen* *Grid* button from the main toolbar), the *Grid Block Coarsening* form will be displayed as shown in [Figure 4](#CoarsenGrid-Figure4). Enter the *Coarsening* *Factor* then click the *OK* button. [Figure 5](#CoarsenGrid-Figure5) shows an example of grid coarsening for a selected grid segment.`` (31). 그림 3은 초록 격자에서 한 구간을 빨강으로 선택한다(33). 그림 4의 `Coarsening in I Direction` 아래 `Coarsening Factor: 3`은 비활성 표시이며 `Coarsening in J Direction` 아래 `Coarsening Factor: 2`는 활성이다(37). 그림 5는 해당 방향의 격자선 간격이 넓어진 결과를 보여 준다(41). |
| 45–62 | Coarsen grid with a selected grid block — 같은 I 또는 J 구간에 있지 않은 두 절점을 Shift로 선택해 블록을 표시하고 인자를 입력한다(47–50). 원문: ``3. LMC on a grid node then hold the Shift key. LMC a second node which is not on the same grid segment in I or J direction. The grid block will be highlighted as shown in [Figure 6](#CoarsenGrid-Figure6).`` (49); ``4. From *Grid* menu, select *Coarsen Grid* option (or select *Coarsen Grid* button from the main toolbar), the *Grid Block Coarsening* form will be displayed as shown in [Figure 7](#CoarsenGrid-Figure7). The user needs to enter the *Coarsening Factor* then click the *OK* button. [Figure 8](#CoarsenGrid-Figure8) shows examples for grid coarsening with a selected grid block.`` (50). 그림 6은 초록 격자 안의 블록 외곽을 빨강으로 표시한다(52). 그림 7의 두 그룹 제목은 모두 `Coarsening in I Direction`이며 위·아래 `Coarsening Factor` 예시 값은 각각 `3`, `2`이다(56). 그림 8은 선택 블록을 포함하는 격자선 수가 줄어든 격자를 보여 준다(60). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16·24행: 성긴 격자 변환 절의 본문은 그림 2를 `grid refinement`의 예시로 설명하지만 캡션은 `Grid after Coarsening.`으로 적는다.
- 56행 그림 7: 인자 두 그룹의 제목이 모두 `Coarsening in I Direction`이다. 18·37행의 다른 창은 I와 J를 구분한다.

