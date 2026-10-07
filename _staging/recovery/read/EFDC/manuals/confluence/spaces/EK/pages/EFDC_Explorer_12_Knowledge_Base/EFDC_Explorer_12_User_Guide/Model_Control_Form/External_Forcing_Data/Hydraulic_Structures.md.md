---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/External_Forcing_Data/Hydraulic_Structures.md
lines: 15
sha256: ff10acb26e2df1901208efd59706ea58768b8682c8896cb58743ba9df7958eda
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Hydraulic_Structures.md — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Hydraulic Structures / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–13 | Hydraulic Structures / 수리 구조물(hydraulic structure) 유형·단면과 역방향 유량(reverse flow) — 암거(culvert), 보(weir), 수문(sluice gate), 오리피스(orifice)의 물리 치수를 입력하면 EFDC가 선택한 구조물의 해당 식을 사용한다(10). 유형 요약을 보고 ``*Structure Parameters.*`` (10)에서 매개변수를 조정한다. 지원 단면의 원문은 ``EEMS also supports eight common cross-sections: circle, semi-circle, ellipse, semi-ellipse, rectangle, parabola, trapezoid and V-notch.`` (10)이다. 역방향 유량과 수직 층별 취수 조건은 ``The *Bi-Directional* check box is used to indicate whether or not to allow reverse flows. In terms of vertical layering, EFDC draws equally from all the layers not impacted by the structure.`` (12)이다. 구조물에 영향을 받지 않는 모든 층에서 동일하게 취수한다고 적는다(12). |
| 14–15 | Figure 1 / 원형 암거(circular culvert) 화면과 도식 — 14행 `EE10_190.png`의 로컬 사본을 열었다. 보이는 설정은 `Select Equation: CULVERT - PIPE`, `Name: CULVERT - PIPE`, `Structure Type: Culvert`, `US Elev (m): 0.250`, `DS Elev (m): 0.250`, `Length (m): 30.00`, `Manning's n: 0.02500`, `Shape: Circle`, `Width (m): 0.25`다(14행 그림). `Bi-Directional Flow`는 선택되어 있지 않다. 왼쪽 종단 도식은 상류·하류의 `US Elev.`, `DS Elev.`를 수직 치수로 표시한다. `Length`는 수평 치수이며 유량 기호 `Q`의 화살표는 오른쪽을 향한다. 오른쪽 원형 단면 도식은 수면과 수직 `Height`, 수평 `Width`를 표시한다. 원형 치수 설명의 화면 원문은 ``Circular cross-section: Width and Height are the same as Diameter.``이다(14행 그림). 15행은 Figure 1 Hydraulic Structures form 캡션이다. 화면의 숫자는 예시이며 이 파일 본문에는 기본값·허용 범위가 없다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
