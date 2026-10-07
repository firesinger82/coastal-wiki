---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Grid_and_Cell_Operations/Split_Grid.md
lines: 20
sha256: dfcf14297268cc41d433c4fdccf8521dd213a3bb2c20f9210d1dce620bd848a7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Split_Grid.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Split Grid / 문서 메타데이터 — 페이지 ID `2818165`, 제목, space, 원문 URL, 버전 `3`, 갱신 시각, 문서 계층을 포함한다(1–9). |
| 10–15 | Split Grid / 다각형으로 격자 분할 — 도구는 하나의 격자 영역을 두 하위 격자 영역(sub-grid domain)으로 나눈다(10). 원문의 `RMC`로 메뉴를 선택한다(10). 원문의 `LMC`로 기존 격자 위에 다각형(polygon)을 만들고 `RMC`로 닫으면 내부에 새 격자가 생성된다(11). 새 격자 레이어(layer)는 기존 격자 레이어를 바탕으로 `Layer Control`에 자동 생성된다(11). 적용 조건 원문: `*Split Grid* allows the user to create a polygon on an existing grid with LMC as shown in [Figure 2](#SplitGrid-Figure2). Closing the polygon with a RMC will generate a new grid inside the polygon as shown in [Figure 3](#SplitGrid-Figure3). The new grid layer will be created automatically on the *Layer Control* based on the existing grid layer.` (11). 직접 연 그림 1은 메뉴의 `Split Grid` 항목을 보여 준다(13–14). |
| 16–20 | Split Grid / 다각형과 결과 그림 — 직접 연 그림 2는 파란 격자 오른쪽 부분을 빨간 다각형 선으로 둘러싼다(16–17). 상태 표시줄은 `Grid Cells: 48`, `NI,NJ: 6, 8`이다(16행 참조 그림). 그림 3은 왼쪽 파란 격자와 오른쪽 빨간 격자를 경계에서 나눈 결과다(19–20). 범례는 빨간 선 `Grid_1`, 파란 선 `Grid`를 표시한다(19행 참조 그림). 빨간 화살표는 왼쪽에서 오른쪽으로 범례 상자를 가리킨다(19행 참조 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10–11행: `#SplitGrid-Figure1`부터 `#SplitGrid-Figure3`까지의 내부 참조가 있다. 이 파일에는 해당 ID를 정의하는 명시 앵커가 없다.
- 10–11행: `RMC`, `LMC`를 사용하지만 이 파일에는 두 약어의 풀이가 없다.
