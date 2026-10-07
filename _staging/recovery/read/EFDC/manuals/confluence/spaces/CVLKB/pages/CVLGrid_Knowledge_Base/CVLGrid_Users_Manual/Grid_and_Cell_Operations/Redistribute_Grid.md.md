---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Grid_and_Cell_Operations/Redistribute_Grid.md
lines: 42
sha256: cbbf715bedb999ec4d36058b621d2b125bea3f28eb8bcfdd578428754fb55669
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Redistribute_Grid.md — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Redistribute Grid / 문서 메타데이터 — 페이지 ID `2818158`, 제목, space, 원문 URL, 버전 `3`, 갱신 시각, 문서 계층을 포함한다(1–9). |
| 10–14 | Redistribute Grid / 세 옵션 — 전체 규칙화(Regularize Global)는 전체 영역의 셀 절점(node) 간격을 균등하게 한다(10). 국소 규칙화(Regularize Local)는 같은 격자선의 두 절점을 선택해 I 또는 J 방향의 절점 간격을 균등하게 한다(10). 텔레스코핑(Telescoping)은 세 절점으로 지정한 격자 블록(grid block)의 간격을 거리 계수(distance factor)에 따라 늘리거나 줄인다(10). 적용 옵션과 조건 원문: `The *Redistribute Grid* tool has three options: *Regularize Global* creates even spacing between cell's nodes for entire grid domain. *Regularize Local* creates even spacing between cell's nodes in either the I or the J direction of grid domain by selecting two nodes on a grid line. *Telescoping* creates increasing or decreasing spacing to a side of the grid block specified by three cell nodes and depends on a distance factor value in the *Telescoping* settings.` (10). 직접 연 그림 1은 `Redistribute` 메뉴 아래 `Regularize Global`, `Regularize Local`, `Telescoping`을 보여 준다(12–13). |
| 15–25 | Regularize Global / Regularize Local 비교 — 본문은 그림 2–4를 참조한다(15). 직접 연 그림 2는 녹색 스플라인(spline) 경계 안의 파란 격자(grid)이며 절점 간격이 불균등하다(17–18). 그림 3은 전체 규칙화 뒤 두 방향의 간격이 고르게 배치된 격자다(20–21). 그림 4는 I 방향 국소 규칙화 뒤의 격자이며 가로 방향 셀 폭은 고르게 배치되고 세로 방향의 조밀한 띠는 남아 있다(23–24). 세 그림의 상태 표시줄은 모두 `Grid Cells: 180`, `NI,NJ: 15, 12`이다(17·20·23행 참조 그림). |
| 26–30 | Telescoping / 절점 선택과 거리 계수 — 커서는 십자 모양으로 바뀐다(26). 처음 두 절점은 늘릴 방향에 수직인 같은 격자선에 있어야 한다(26). 세 번째 절점은 텔레스코핑을 적용할 끝점을 지정한다(26). 세 절점은 적용 블록을 정의한다(26). 선택 조건 원문: `When the user selects *Telescoping,* the mouse cursor transforms from an arrow to a cross hair. Three nodes to be selected in the Telescoping option. The user needs to first select two nodes on same grid line which are perpendicular to the direction in which the grid will be telescoped or stretched. The user should then select a third node on grid domain which the end point to which the telescoping will be applied. These three nodes define a grid block which the telescoping will be apply too.` (26). 세 번째 절점 선택 뒤 설정 창에서 거리 계수를 입력하고 `OK`를 누른다(28). 기본값·범위 원문: `After selecting the third node, a window for the T*elescoping Setting* appears to allow the user to enter the value of a distance factor. The default value of the distance factor is two and the distance factor must be a whole number greater than 1. After entering the telescoping factor click *OK*. The distance between the first two nodes in the grid block increases gradually towards the third node specified.` (28). 이 문장은 기본값을 `two`, 허용값을 `a whole number greater than 1`로 적으며 단위는 적지 않는다(28). 그림 5–8의 처리 순서를 안내한다(30). |
| 31–37 | Telescoping / 적용 전 격자와 세 선택점 — 직접 연 그림 5는 녹색 경계 안 파란 격자이며 `Grid Cells: 42`, `NI,NJ: 7, 6`을 표시한다(32–33). 그림 6에서 빨간 원으로 표시한 `1st point`와 `2nd point`는 오른쪽 경계의 위·아래 절점이다(35–36). `3rd point`는 왼쪽 경계의 중간 절점이다(35–36). 세 점에 방향 화살표는 없다(35행 참조 그림). |
| 38–42 | Telescoping / 설정과 처리 결과 — 직접 연 그림 7의 `Telescoping Setting` 표는 열 이름 `Description`, `Value`, 행 이름 `Distance factor`, 값 `2`를 표시한다(38–39행 참조 그림). 이 화면값은 예시이며 기본값의 근거는 28행이다. 그림 8은 오른쪽 경계에 촘촘하고 세 번째 점이 있는 왼쪽으로 갈수록 셀 폭이 커지는 격자다(41–42). 결과 상태 표시줄은 `Grid Cells: 42`, `NI,NJ: 7, 6`이다(41행 참조 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 15·30행: `#RedistributeGrid-Figure2`부터 `#RedistributeGrid-Figure8`까지의 내부 참조가 있다. 이 파일에는 해당 ID를 정의하는 명시 앵커가 없다.
- 35행 참조 그림 6: 본문과 캡션은 Telescoping 점 선택을 설명하지만 화면 왼쪽 아래에는 `Regularize Grid: Local`이 표시된다.
