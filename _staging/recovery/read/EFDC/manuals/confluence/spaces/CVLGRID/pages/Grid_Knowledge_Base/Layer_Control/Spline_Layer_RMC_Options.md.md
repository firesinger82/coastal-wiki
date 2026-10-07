---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Layer_Control/Spline_Layer_RMC_Options.md
lines: 60
sha256: ce42c68cc92e9b1b798221c88cf62dbd717543cee43d06c08015682dfb833fd7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Spline_Layer_RMC_Options.md — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Spline Layer: RMC Options`, space `CVLGRID`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–29 | 스플라인(spline) 레이어 RMC 메뉴 — 트리 제목에서 메뉴를 연다(10). 표의 행은 `Properties` (20), `Create Grid` (21), `Zoom to Layer` (22), `Export Control Points To` (23), `Remove` (24), `Create New Spline Layer` (25), `Create New Overlay Layer` (26), `Turn All Layers Off` (27), `Turn All Layers On` (28)이다. 속성 설정, 격자 생성, 확대, 제어점(control point) 내보내기, 삭제, 레이어 생성 및 전체 레이어 표시를 설명한다(20–28). 그림 1을 열었다(12–14). 하천 위 초록 스플라인과 제어점 및 RMC 메뉴를 보여 준다. |
| 30–41 | Spline Properties — Properties에서 속성을 연다(32). 원문: `- *Layer Name*: shows the name of the layer, a new name can be entered here` (34); `- *Layer Visible*: unchecking this box will hide the spline layer (the light bulb of the layer in the *Control Panel* is also turned off)` (35); `- *Line Settings*: allows the changing of setting style, color, and thickness of the spline lines.` (36). 그림 2를 열었다(38–40). 화면의 표시값은 `Layer Name: Spline 001`, `Style: Solid`, `Width: 1.0`이며 Layer Visible은 체크되어 있다(38). 본문은 이 표시값을 기본값으로 정의하지 않는다. |
| 42–53 | Create Grid — 생성 조건을 충족할 때만 RMC에 나타난다(44). 조건 원문: `This option only appears from the RMC option when it meets the condition to generate a grid (i.e.at least four splines are crossing).` (44). I·J 방향 구간 수를 지정하고 OK를 누르며 주 도구막대에서도 접근할 수 있다(44). 그림 3·4를 열었다(46·50). 그림 3은 `Create Grid from Splines`, `Grid Points in I Direction`의 `Number of Intervals: 4`, `Grid Points in J Direction`의 `Number of Intervals: 4`를 보여 준다(46, 그림 표시값). 그림 4의 빨간 화살표는 선택된 Spline 001에서 사용할 도구막대의 격자 생성 버튼을 위쪽으로 가리킨다(50). |
| 54–60 | Export Control Points To — 파일 종류·이름·폴더를 지정한 다음 Save를 누른다(56). 기본 확장자 원문: `Define the file type (\*.spl is the default extension for spline) then enter a file name.` (56). 그림 5를 열었다(58–60). 저장창은 `Splines001.spl`과 `Spline files (*.spl;*.p2d;*.ldb;*.pol)`을 보여 준다(58). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·16·32·44·56행: `#SplineLayer:RMCOptions-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.
- 44·46·48행: 본문과 그림 창 제목은 Create Grid from Splines를 가리키지만, 그림 3 캡션은 `Show Properties`라고 적는다.

