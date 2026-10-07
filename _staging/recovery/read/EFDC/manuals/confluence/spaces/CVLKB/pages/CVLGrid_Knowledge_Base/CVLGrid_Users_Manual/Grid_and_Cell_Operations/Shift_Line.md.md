---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Grid_and_Cell_Operations/Shift_Line.md
lines: 30
sha256: 41527c34447561de4ec5ed34f5904fdd915ab3568c7a019c3e3d4d28c5f515f5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Shift_Line.md — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Shift Line / 문서 메타데이터 — 페이지 ID `2818166`, 제목, space, 원문 URL, 버전 `3`, 갱신 시각, 문서 계층을 포함한다(1–9). |
| 10–16 | Shift Line / 1단계 — 선택 격자의 한 격자선 또는 여러 평행 격자선을 이동한다(10). 경계선(boundary line)의 첫 두 점 중 첫 점은 회전 기준점(pivot), 둘째 점은 이동점이다(12). 선택 조건 원문: `1. Select the first point and the second point on the boundary line of the grid. These two points determine the line that will be moved. The first point will act as a pivot when the grid line is moved. The second point will serve as a moveable point to determine where to move to. This process is shown in [Figure 1](#ShiftLine-Figure1).` (12). 직접 연 그림 1은 파란 곡선 격자(curvilinear grid)의 위쪽 경계에 빨간 원으로 `1st point`, `2nd point`를 표시한다(14–15). 두 점 사이 경계가 색으로 강조되어 있다(14행 참조 그림). 상태 표시줄은 `Grid Cells: 150`, `NI,NJ: 15, 10`이다(14행 참조 그림). |
| 17–21 | Shift Line / 2단계 — 세 번째 절점(node)은 선택 선과 이 점 사이에서 이동할 셀 행 수를 정한다(17). 세 번째 점 선택 시 첫 두 점 사이 선분이 자동으로 강조된다(17). 선택 조건 원문: `2. Select a third node in the grid. This third point will determine the number of cell rows between this point and the selected line that will be moved. A line segment is connected by the first point and the second point will be resized after the line is moved. When the third point is chosen then the line segment will be highlighted automatically.` (17). 직접 연 그림 2는 기존 두 경계점 아래의 내부 절점에 빨간 원과 `3rd point`를 표시한다(19–20). 상태 표시줄은 `Grid Cells: 150`, `NI,NJ: 15, 10`이다(19행 참조 그림). |
| 22–26 | Shift Line / 3단계 — 원문의 `LMC` 조작으로 둘째 점의 이동을 시작하고 목적지를 다시 누른다(22). 세 번째 점과 선분 사이 격자 셀의 크기가 바뀐다(22). 조작 원문: `3. LMC on the second point to start moving then LMC again on the desired destination. The grid cells between the third point and the line segment will be resized.` (22). 직접 연 그림 3은 `1st point`, `2nd point`, `3rd point`, `Destination point`를 빨간 원으로 표시한다(24–25). 목적지는 둘째 점보다 왼쪽 위에 있다(24행 참조 그림). 목적지와 선택점 사이에는 파란 선분이 있으며 화살촉은 없다(24행 참조 그림). |
| 27–30 | Shift Line / 4단계와 비모서리점 조건 — 목적지를 누르면 격자가 바뀐다(27). 둘째 점이 모서리 절점(corner node)이 아니면 그 옆의 셀 하나도 함께 이동한다(27). 조건 원문: `4. After clicking on the destination point the grid image will be changed as shown in [Figure 4](#ShiftLine-Figure4). Note that if the second point selected is not a corner node, then one cell to the side of the second is also moved along with the second point.` (27). 직접 연 그림 4는 위쪽 경계가 목적지까지 올라가고 그 아래 셀들이 늘어난 결과다(29–30). 상태 표시줄은 `Grid Cells: 150`, `NI,NJ: 15, 10`이다(29행 참조 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12·27행: `#ShiftLine-Figure1`, `#ShiftLine-Figure4` 내부 참조가 있다. 이 파일에는 해당 ID를 정의하는 명시 앵커가 없다.
- 22·30행: `LMC`를 사용하지만 이 파일에는 약어의 풀이가 없다.
