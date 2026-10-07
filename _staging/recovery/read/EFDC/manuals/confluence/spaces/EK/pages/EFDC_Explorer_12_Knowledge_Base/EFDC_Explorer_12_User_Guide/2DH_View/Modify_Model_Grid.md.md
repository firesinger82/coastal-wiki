---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Modify_Model_Grid.md
lines: 48
sha256: ca5a5799c63d6f312f031a02061e001294f22a5a68bc92640e21bc84ac9295cb
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Modify_Model_Grid.md — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–23 | 모델 격자 수정(Modify Model Grid) / 인덱스와 회전 — Layer Control의 펜을 켜고 셀 또는 레이어를 오른쪽 클릭하여 편집한다(10). 10행 펜 아이콘을 직접 열었다. Model Grid는 I·J 인덱스의 회전·반전·전치(transpose)를 제공하며 격자 생성·가져오기에서 방향 문제를 고치는 데 사용한다(14). 셀 비활성화와 격자 꼭짓점 회전을 제공한다(14). 적용 대상·파일 조건 원문: `This function applies a rotation to the cell rotation angles, it does not rotate the actual cell.`; `If using the CORNERS.INP file, just applies a user-specified rotation to the cell rotation matrix.`; `In EFDC the cell’s rotation matrix is used for velocity plots and interaction with the wind field.` (14). 그림 1은 Flip I Indices·Flip J Indices·Transpose I and J Indices·Rotate Indices Clockwise·Rotate Indices Counter-Clockwise 메뉴이다(16–18). 그림 2는 셀 비활성화와 Rotate·Auto Rotate·Reverse Grid Cell Corners 메뉴이다(20–22). 두 그림을 직접 열었다. |
| 24–41 | 경계 모서리의 삼각 셀(triangular cell) — 모서리 셀의 오른쪽 클릭에서 Change to Triangular Cells로 삼각형으로 바꾸며 다시 Change to Quadrangular Cells로 사각 셀(quadrangular cell)로 되돌린다(24). 여러 셀은 Selection Tool로 먼저 선택하여 같은 기능을 적용한다(30). 전체 영역 모서리는 `Alt + T` 후 Triangular cells on the border 창에서 Yes를 누른다(32). 그림 3은 단일 모서리 셀의 삼각형·사각형 변경 메뉴이다(26–28). 그림 4는 다중 선택 영역의 같은 메뉴이며 상태 표시는 178개 선택이다(34–36). 그림 5의 확인 문구는 `Convert the staggered border cells to triangular cells?`이다(38–40). 세 그림을 직접 열었다. |
| 42–48 | Grid Connection / 격자 연결 — 서로 다른 격자 영역에 남북 `N-S` 또는 동서 `E-W` 연결자(grid connector)를 추가한다(44). Grid Connections 레이어를 선택하고 첫 격자 셀을 오른쪽 클릭하여 Add N-S Connection 또는 Add E-W Connection을 고른 뒤 두 번째 연결점을 왼쪽 클릭한다(44). 그림 6을 직접 열었다(46–48). 메뉴에는 Add N-S Connection·Add N-S Connection Group이 표시되고 격자 사이 빨간 연결선 끝에 N·S 표시가 있다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14·24·30·32·44: `#Figure1`부터 `#Figure6`까지의 링크가 있지만 이 Markdown 파일에는 해당 앵커 정의가 없다.

