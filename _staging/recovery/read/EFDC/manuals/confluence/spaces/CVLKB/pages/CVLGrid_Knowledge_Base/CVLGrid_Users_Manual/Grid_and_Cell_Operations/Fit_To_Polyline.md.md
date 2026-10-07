---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Grid_and_Cell_Operations/Fit_To_Polyline.md
lines: 37
sha256: 6f4d7f5a42abb46fb21288077f85fe60a5e3306e11f243e646c5fa2f72d52722
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Fit_To_Polyline.md — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Fit To Polyline`, space `CVLKB`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–13 | Fit to Polyline 개요·경계 조건 — 생성·직교화(orthogonalization) 중 경계에서 떨어지는 격자 셀을 영역 경계에 맞추는 도구라고 적는다(10). 경계 유형 원문: `The boundary here can be of type *Overlay* or *Splines*.` (12). 같은 경계 구간의 절점 두 개로 영향 구간을 정한다(12). |
| 14–23 | 1–2단계 / 도구·첫 두 절점 선택 — RMC에서 Fit to Polyline을 선택하고 이동이 필요한 격자 가장자리의 두 절점을 선택한다(14·19). 그림 1·2를 열었다(16·21). 그림 1의 빨간 화살표는 메뉴를 오른쪽으로 가리킨다(16). 그림 2는 파란 격자의 아래 가장자리 양 끝을 빨간 원으로, 영향 가장자리를 빨간 선으로 표시한다(21). 맞출 초록 경계는 격자 아래쪽에 떨어져 있다. |
| 24–28 | 3단계 / 영향 깊이 설정 — 셋째 절점으로 수정할 행 수를 정한다(24). 예제 수량 원문: `indicating that four rows deep inside the grid will be modified (from the blue third node to the red edge that was created from the first two nodes).` (24). 그림 3을 열었다(26–27). 파란 원이 내부 셋째 절점을 가리키며 첫 두 점이 만든 빨간 가장자리와 그 사이를 보여 준다(26). |
| 29–33 | 4단계 / 대상 경계 선택 — 마지막 점을 경계에 놓아 대상 폴리라인(polyline)을 정하며 선택 직후 자동 실행한다(29). 적용 시점 원문: `Immediately after the user selects the four and final node, the *Fit to boundary* function will be automatically implemented` (29). 그림 4를 열었다(31–32). 아래 초록 경계 위 마지막 점을 빨간 원으로 표시하고 그 경계까지 아래쪽 격자선이 늘어난 모습을 보여 준다(31). |
| 34–37 | 5단계 / 간격 정리 — 가장 가까운 셀만 늘어나므로 추가 정규화(regularization)로 셀 간격을 개선할 수 있다고 적는다(34). 조건 원문: `When grid cells are fitted to a boundary only the closest cells are stretched.` (34). 그림 5를 열었다(36–37). 정규화 후 파란 격자가 초록 경계와 맞닿으며 내부 간격이 앞 그림보다 고르게 배치되어 있다(36). 화면은 `Grid Cells: 60`, `NI,NJ: 10,6`이다(36). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12행: 참조 문구에 `Figure 6 42`가 남아 있지만 이 문서의 그림은 Figure 1–5이다.
- 12·14·19·24·29·34행: `#FitToPolyline-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.

