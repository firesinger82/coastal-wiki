---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Grid_and_Cell_Operations/Orthogonalize_Grid.md
lines: 41
sha256: 64f2decaf948d541006ccdaaa052c30f03035e5df984823e96ca9ffe0627933b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Orthogonalize_Grid.md — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Orthogonalize Grid`, space `CVLKB`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–16 | Orthogonalize Grid 개요·옵션 — 격자 직교성(orthogonality)을 최적화하면 모델 정확도가 높아진다고 적고 도구는 직교 편차(orthogonal deviation)를 줄인다고 설명한다(10). 권고 원문: `for most EFDC models an orthogonality of under 3o is recommended.` (10). 매개변수는 앞 CVLGrid Settings에서 설정한다고 적는다(10). 그림 1을 열었다(14–15). Orthogonalize Global·Orthogonalize Local·Orthogonalize 1D 메뉴를 보여 준다(14). |
| 17–24 | Global·Local·1D 적용 조건 — Global은 전체 격자에 즉시 적용한다(17). 조건 원문: `If a local operation is selected, the user must define two grid nodes and the area of the grid limited by the two points will be orthogonalized.` (17); `*Orthogonalize 1D* feature is similar to the *Orthogonalize Local* option but is only applicable for a 1D grid region. In case the feature is applied for an improper grid region, a warning message will appear.` (17). Global 예제의 평균값 원문: `the average orthogonality is 20.3.`; `it is only 2.6.` (19). Local·1D 전후 그림 안내도 포함한다(21·23). |
| 25–30 | Orthogonalize Global 전후 그림 — 그림 2·3을 열었다(25·28). 두 그림의 격자는 파란 선으로 나뉘며 색상 범례는 `Orthogonal Deviation (Deg)`이다. 그림 2 범례 끝값은 `-45.6048`, `4.96185`, 평균 표시는 `AVG [Dev]: 20.31629`이다(25). 그림 3 범례 끝값은 `-6.86291`, `7.61396`, 평균 표시는 `AVG [Dev]: 2.63357`이다(28). 두 화면은 `Grid Cells: 150`, `NI,NJ: 15,10`을 표시한다(25·28). |
| 31–36 | Orthogonalize Local 전후 그림 — 그림 4·5를 열었다(31·34). 가늘고 굽은 격자와 초록 스플라인(spline)을 보여 주며 그림 5의 빨간 큰 원은 위쪽 적용 영역을 둘러싼다(34). 범례는 `Orthogonal Deviation (Deg)`이다. 전 범례 끝값은 `-14.33235`, `51.19483`, 평균은 `AVG [Dev]: 16.68615`이다(31). 후 범례 끝값은 `-14.33235`, `10.47369`, 평균은 `AVG [Dev]: 4.45375`이다(34). 두 화면은 `Grid Cells: 78`, `NI,NJ: 26,3`을 표시한다(31·34). |
| 37–41 | Orthogonalize 1D 전후 그림 — 그림 6·7을 열었다(37·40). 세로로 굽은 다열 격자와 오른쪽으로 뻗은 단일 셀 폭 가지가 연결되어 있다(37). 그림 7의 빨간 큰 타원은 가로 가지 적용 구간을 둘러싼다(40). 범례는 `Orthogonal Deviation (Deg)`이다. 전 끝값은 `-49.50685`, `22.15636`, 평균은 `AVG [Dev]: 4.12413`이다(37). 후 끝값은 `-15.47203`, `11.3754`, 평균은 `AVG [Dev]: 2.66784`이다(40). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12·19·21·23행: `#OrthogonalizeGrid-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.
- 10행: 권고 한계의 단위 표기는 `3o`이다. 같은 파일 그림 범례는 `Deg`를 쓴다.
- 10행: 도구 매개변수는 다른 CVLGrid Settings 문서에서 정한다고 적는다. 이 파일에는 그 매개변수 이름·기본값 목록이 없다.

