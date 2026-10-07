---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Initial_Conditions/Water_Quality_IC.md
lines: 18
sha256: 8e91f8a73405c8668aa6c2f7707d1e03f78314371bf7a441aa5b8d7347a92bef
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Water_Quality_IC.md — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Water Quality IC — 문서 식별자, 제목, space, URL, 판본, 갱신 시각과 문서 계층의 frontmatter(1–9). |
| 10–15 | Water Quality IC / 초기값 형식 — CSS 선언 뒤 수질(water quality) 초기조건 양식을 소개한다(10). 상수·공간변화 자료 형식의 적용 조건 원문: `There are three options to select spatially varying initial conditions for water quality parameters. Users can set a constant value when selecting *Spatially Constant*.  If the EFDC model uses *Spatially Varying IC’s (ICIFN Format)* or *Spatially Varying IC’s (WQWCRST.INP),* then users should specify which input data format to use, i.e. ICIFN or WQWCRST.INP format.` (12) 빈 줄과 그림을 포함한다(11,13–15). `Waterquality.jpg`을 열었다(14). Options 드롭다운의 `Spatially Constant`, `Spatially Varying IC's (ICIFN Format)`, `Spatially Varying IC's (WQWCRST.INP)`와 Const IC's·Varying IC's·Initialize IC's 버튼을 보여 준다. |
| 16–18 | 수질 분류별 공간 배정 — Varying IC's로 각 분류 자료를 셀에 보간하며 파일 옵션·형식은 Bathymetry와 유사하다고 설명한다(16). 전체 초기화 범위 원문: `*Initialize IC’s* is used to assign the entire domain for all parameters to the values specified as the spatially constant IC’s.` (16) 빈 줄과 그림을 포함한다(17–18). `Waterquality2.jpg`을 열었다(18). 메뉴에서 초기조건 양식으로, Varying IC's에서 Interpolate Classed Data로 향하는 빨간 화살표가 있다. 초기조건 형식은 `Spatially Varying IC's (WQWCRST.INP)`이다. 보간 양식은 `All grid cells`, `For All Layers`, `Constant: 0`, `Replacement`, `A Specific Class: Cyanobacteria`를 선택한다. 다른 옵션은 `Only grid cells inside polygons`, `A Specific Layer: 1`, `From Scatter (XYZ) Data`, `From Profile Data`, `Maximum value`, `Minimum value`, `For All Classes`이다. 파일 목록은 비어 있다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·16: Figure 1·2 링크는 `#Figure1`, `#Figure2`를 가리킨다. 이 파일에는 해당 anchor 정의가 없다.
- 12: 첫 문장은 세 옵션을 `spatially varying initial conditions` 선택 옵션으로 소개한다. 같은 행의 첫 옵션은 `Spatially Constant`이다.
