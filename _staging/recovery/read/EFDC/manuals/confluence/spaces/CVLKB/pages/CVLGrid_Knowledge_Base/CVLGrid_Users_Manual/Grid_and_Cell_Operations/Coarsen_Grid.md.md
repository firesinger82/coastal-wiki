---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Grid_and_Cell_Operations/Coarsen_Grid.md
lines: 37
sha256: 02b05a81f46aa1a8c08863338e6c2027abde94274794b8c716d900da6fec3721
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Coarsen_Grid.md — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Coarsen Grid`, space `CVLKB`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–19 | Coarsen Grid 기능·범위 — 격자 성김화(coarsening)는 Refine Grid의 반대로 해상도를 낮춘다(10). 덜 중요한 영역의 해상도를 줄이면 계산 시간이 줄어든다고 적는다(12). 설정 지시 원문: `The user must first define the divisor by which cells will be coarsened in the I and/or J direction when prompted.` (14). `If a global operation is selected the entire grid will be coarsened by the specified amount.` (16). 국소 조건 원문: `If a local operation is selected, the user must define two nodes on a grid line either I or J axis to be coarsened.` (18). |
| 20–30 | Coarsen Global 화면·전후 격자 — 그림 1–3을 열었다(20·23·27). 그림 1은 Coarsen Global·Coarsen Local 메뉴를 보여 준다(20). 그림 2의 입력 문구는 `Enter the Divisor to coarsen (IC,JC):`, 입력은 `2,2`이다(23, 예제 표시값). 같은 화면의 하단은 `Grid Cells: 90`, `NI,NJ: 10,9`이며 그림 3의 하단은 `Grid Cells: 20`, `NI,NJ: 5,4`이다(23·27). 그림 3에서 파란 격자선 간격이 커져 있다. 두 화면의 축척은 `107.3 Meters`이다(23·27). |
| 31–37 | Coarsen Local 화면·전후 격자 — 그림 4·5를 열었다(31·35). 그림 4의 빨간 원과 설명선은 같은 격자선의 첫째·둘째 절점을 가리킨다(31). 설정 창에는 `I Direction`, 선택된 `J Direction`, `Divisor to coarsen cells: 2`가 보인다(31). 예제 하단의 셀 수는 전 `Grid Cells: 90`, 후 `Grid Cells: 40`이다(31·35). 두 하단 모두 `NI,NJ: 10,9`를 표시한다(31·35). 그림 5는 J방향 선 수가 줄어든 파란 격자와 `107.3 Meters` 축척을 보여 준다(35). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16·18행: `#CoarsenGrid-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.
- 31·35행 그림: 셀 수 표시는 90에서 40으로 달라지지만 `NI,NJ` 표시는 두 그림 모두 `10,9`이다.

