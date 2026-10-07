---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Grid_and_Cell_Operations/Smooth_Grid.md
lines: 20
sha256: 9c04a21292617c38e326c47b34956d3a16305b1766f593aead0b419dfd400954
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Smooth_Grid.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Smooth Grid / 문서 메타데이터 — 페이지 ID `2818162`, 제목, space, 원문 URL, 버전 `3`, 갱신 시각, 문서 계층을 포함한다(1–9). |
| 10–15 | Smooth / 적용 블록 선택 — 본문은 격자 평활화(smoothing)가 모형 정확도를 개선한다고 적는다(10). 이 구간은 정확도 수치나 검증 결과를 제시하지 않는다(10–11). 도구는 원문의 `RMC`로 선택한다(10). `Smooth` 선택 후 두 절점(node)을 선택해 적용 블록(grid block)을 정의해야 한다(11). 선택 조건 원문: `When the *Smooth* feature is selected, the user must select two nodes on the grid domain to define a block on which to apply the smoothing. [Figure 2](#SmoothGrid-Figure2) and [Figure 3](#SmoothGrid-Figure3) show the grid before and after using the *Smooth* tool.` (11). 직접 연 그림 1은 격자 조작 메뉴의 `Smooth` 항목을 보여 준다(13–14). |
| 16–20 | Smooth / 처리 전후 격자 — 직접 연 그림 2는 녹색 스플라인(spline) 경계 안 파란 격자(grid)다(16–17). 빨간 타원은 오른쪽의 꺾인 격자선과 찌그러진 셀을 둘러싼다(16행 참조 그림). 그림 3에서는 같은 영역의 격자선이 부드럽게 이어지고 해당 타원이 없다(19–20). 두 그림의 상태 표시줄은 `Grid Cells: 156`, `NI,NJ: 13, 12`다(16·19행 참조 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10–11행: `#SmoothGrid-Figure1`부터 `#SmoothGrid-Figure3`까지의 내부 참조가 있다. 이 파일에는 해당 ID를 정의하는 명시 앵커가 없다.
- 10행: `RMC`를 사용하지만 이 파일에는 약어의 풀이가 없다.
