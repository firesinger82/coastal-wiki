---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Grid_and_Cell_Operations/Refine_Grid.md
lines: 33
sha256: fec3a59e99a7441b4792e91b2a4f0639544d57fb321e714fd962af2b63dedf72
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Refine_Grid.md — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Refine Grid / 문서 메타데이터 — 페이지 ID `2818149`, 제목, space, 원문 URL, 버전 `6`, 갱신 시각, 문서 계층을 포함한다(1–9). |
| 10–14 | Refine / 전체와 국소 세분화 — 세분화(refinement)는 현재 격자의 셀 수를 I·J 방향 배수 `(IC, JC)`로 각각 늘린다(10). `Refine Global`은 전체 격자에 적용한다(10). `Refine Local`은 선택한 구역에만 적용한다(10). 매개변수·적용 조건 원문: `The *Refine* tool increases the resolution of the grid. It operates by multiplying the existing number of cells in the current grid with (IC, JC) independently. There are two refine features: *Refine Global* and *Refine Local* as shown in [Figure 1](#RefineGrid-Figure1). *Refine Global* feature will apply the refinement for the whole grid, whereas *Refine Local* feature will only apply the refinement for the section of the grid selected.` (10). 직접 연 그림 1은 `Refine` 하위 메뉴의 `Refine Global`, `Refine Local`을 보여 준다(12–13). |
| 15–18 | Refine / 배수 입력과 국소 구역 선택 — 전체 세분화의 배수 이름은 `n I and n J`이고 예시는 `(2, 2)`이다(15). 배수는 정수여야 한다(15). 기본값·단위는 이 본문에 없다. 매개변수·정수 조건 원문: `For the  *Refine Global* feature, the user must define set the multiplier, n I and n J, to enter into the text box. [Figure 2](#RefineGrid-Figure2) and [Figure 3](#RefineGrid-Figure3) show the grid before and after applying *Refine Global* with (2, 2) for the IC and JC indices. Note that the multiplier must be a whole number.` (15). 국소 세분화는 먼저 같은 I 또는 J 방향의 두 절점(node)을 선택해 구역을 지정한다(17). 그림 예시는 I 방향 배수 `2`다(17). 선택 조건 원문: `For the *Refine Local* feature, the user must first define two nodes in the same I or J direction. This will define a "local" zone for which the refinement will be applied. [Figure 4](#RefineGrid-Figure4) and [Figure 5](#RefineGrid-Figure5) show the grid before and after applying *Refine Local* with 2 in the I direction.` (17). |
| 19–26 | Refine Global / 전후 그림 — 직접 연 그림 2는 휘어진 파란 격자 위 `Refine Grid` 창을 보여 준다(19–21). 창의 입력 안내는 `Enter the multiplier to refine the cells (nI,nJ):`, 입력값은 `2,2`다(19행 참조 그림). 적용 전 상태는 `Grid Cells: 100`, `NI,NJ: 10,10`이다(19행 참조 그림). 그림 3은 같은 외곽 형상 안의 두 방향 격자선이 조밀해진 결과이며 `Grid Cells: 400`, `NI,NJ: 20,20`이다(23–25행 참조 그림). 두 그림의 축척 막대는 `107.3 Meters`다(19·23행 참조 그림). |
| 27–33 | Refine Local / 선택점과 전후 그림 — 직접 연 그림 4의 빨간 원 두 개를 향한 말풍선 화살표는 `RMC on the first node`, `RMC on the second node`라고 적는다(27–29행 참조 그림). `Refine Option` 창은 `I Direction` 선택, `J Direction` 미선택, `Multiplier to refine cells:` 값 `2`를 보여 준다(27행 참조 그림). 적용 전 상태는 `Grid Cells: 100`, `NI,NJ: 10,10`이다(27행 참조 그림). 그림 5는 두 선택점 사이에 I 방향 격자선을 추가한 결과이며 `Grid Cells: 120`, `NI,NJ: 12,10`이다(31–33행 참조 그림). 두 그림의 축척 막대는 `107.3 Meters`다(27·31행 참조 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·15행: 10행은 배수 기호를 `(IC, JC)`로 적고 15행은 `n I and n J`로 적는다.
- 10·15·17행: `#RefineGrid-Figure1`부터 `#RefineGrid-Figure5`까지의 내부 참조가 있다. 이 파일에는 해당 ID를 정의하는 명시 앵커가 없다.
- 27행 참조 그림 4: 점 선택 안내에 `RMC`를 사용하지만 이 문서 본문에는 해당 약어의 풀이가 없다.
