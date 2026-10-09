---
file: models/ADCIRC/raw/manuals/wiki/markdown/Manning_s_n_at_sea_floor.md
lines: 117
sha256: 36461ee95e5ee50d52c875cd4d39e077c495169f04505f781b6ad8c339f531bb
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Manning_s_n_at_sea_floor.md — 판독 구간 기록

구간은 1행부터 117행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | Manning's n at sea floor — fort.13의 mannings_n_at_sea_floor 절점 속성(nodal attribute)으로 공간 및 시간에 따라 변하는 저면 마찰(bottom friction)을 지정할 수 있다고 적는다(5). 제목·판본·목차·빈 줄을 포함한다(1–18). 원문: ``The `mannings_n_at_sea_floor` nodal attribute is one of the available options for specifying [bottom friction](/index.php?title=Bottom_friction&action=edit&redlink=1) in ADCIRC based on the [Manning formula](https://en.wikipedia.org/wiki/Manning_formula).  It is a [nodal attribute](/Nodal_attribute) in the [fort.13 file](/Fort.13_file), meaning that it allows spatially (and temporally) varying bottom friction in the model.  `` (5). |
| 19–36 | Attribute Summary / 그림 캡션 — `MnasfContours3.png`는 Manning의 n과 전체 수심(total depth)에 따른 항력계수(drag coefficient) 등고선(contours)이라는 캡션을 갖는다(21–35). 캡션의 LaTeX와 분해된 마크업(markup)을 포함한다(22–34). `/File:MnasfContours3.png`: 그림 파일 없음(21). 캡션만 읽었으며 그림의 축·등고선 값은 확인하지 못했다. 원문: `    {\displaystyle C_{d}}` (33). |
| 37–82 | Attribute Summary / 마찰계수 변환식 — 이 절점 속성을 쓰면 NOLIBF를 1로 설정해야 하며 그렇지 않으면 실행이 종료된다(37). ADCIRC는 매 절점·시간 단계에서 Manning의 n을 등가 이차 마찰계수(equivalent quadratic friction coefficient)로 변환한 다음 저면 응력(bottom stress)을 계산한다(37). 수식의 분해된 표기와 원문 LaTeX를 포함한다(39–81). 원문: ``If the user elects to use this nodal attribute, which ADCIRC reads in as the `[ManningsN](/index.php?title=ManningsN&action=edit&redlink=1)` variable, `[NOLIBF](/NOLIBF)` must be set to 1 or the run will terminate. During execution, the Manning’s n values specified are converted to equivalent quadratic friction coefficients before the bottom stress is calculated. The equivalent quadratic friction coefficient is calculated according to the following formula at each node at each time step: `` (37); `    {\displaystyle C_{d}(t)={\frac {gn^{2}}{\sqrt[{3}]{h+\eta (t)}}}}` (80). |
| 83–98 | Attribute Summary / 기호와 적용 조건 — Cd는 항력계수, t는 시간, g는 중력 가속도, n은 Manning의 n, h는 수심, η는 수면 고도(water surface elevation)이다(83–95). NOLIFA=0이면 η를 0으로 취급한다(97). fort.15의 CF로 계산한 등가 이차 마찰계수의 하한을 정한다(97). 기호 정의와 조건을 원문 그대로 옮긴다. 원문: `- Cd drag coefficient` (85); `- t time` (87); `- g acceleration due to gravity` (89); `- n Manning's n` (91); `- h depth` (93); `- η water surface elevation` (95); ``The addition of the water surface elevation is conditional upon the setting of `[NOLIFA](/NOLIFA)`: η is treated as zero if `NOLIFA = 0` in the [fort.15](/Fort.15) file.  Finally, the value of `[CF](/index.php?title=CF&action=edit&redlink=1)` in the fort.15 is used to set a lower limit on the resulting equivalent quadratic friction coefficient, under the assumption the Cd calculated from this formula tends to become too small in deep water.`` (97). |
| 99–106 | Negative n Values — 버전 55 이상 표기를 포함한다(101–103). 특정 절점의 n을 음수로 정하면 시간에 일정한 Cd를 사용한다(105). Cd는 fort.15의 CF 또는 fort.13의 quadratic_friction_coefficient_at_sea_floor에서 지정한다(105). 원문: `ADCIRC version:` (101); `  &#8805;  55  ` (103); ``If a combination of Manning's and time invariant [bottom friction](/index.php?title=Bottom_friction&action=edit&redlink=1) is desired, users can elect to set the Manning's [nodal attribute](/Nodal_attribute) to a negative value at certain mesh nodes. At mesh nodes where n is negative, the time invariant Cd coefficient, specified via a constant `[CF](/index.php?title=CF&action=edit&redlink=1)` in the [fort.15 file](/Fort.15_file) or the spatially varying [quadratic_friction_coefficient_at_sea_floor](/Fort.13_file#Quadratic_Friction_coefficient) fort.13 nodal attribute, will be used instead.`` (105). |
| 107–110 | Specifying n Values — 토지 피복(land cover) 자료에 따른 n 지정과 미국 자료 예시를 설명한다(109). 현장 조사나 사진 검토로 피복 값과 n을 연관시키는 것이 이상적이라고 적는다(109). 문헌 검토도 값 선택의 근거를 제공할 수 있다고 적는다(109). |
| 111–117 | File Format / Utilities — File Format 절은 제목만 있다(111–112). Utilities는 mannings_n_finder와 f13builder 링크를 적는다(113–117). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 21행: `/File:MnasfContours3.png`의 로컬 그림 파일 없음.
- 111–112행: File Format 절에는 형식 설명 본문이 없다.
- 5·37·97·105·115·117행: bottom friction, ManningsN, CF와 두 유틸리티의 링크에 `action=edit&redlink=1`이 있다.
