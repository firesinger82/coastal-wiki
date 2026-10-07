---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Water_Quality/Nutrients.md
lines: 21
sha256: 133d061d50a9fc06b93ad166690c101241e4d25a8931aa8af11b0d3285761a0b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Nutrients.md — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Nutrients — 페이지 메타데이터를 담은 frontmatter이다(1–9). |
| 10–14 | 영양염(nutrient) 기본 설정 — CSS 선언 뒤에서 영양염 종류별 편집을 설명한다(10). 구역 값 우선 적용 조건은 `If the user implements kinetic zones then those values will be used in place of these values, however, the default values are still displayed in this form. For example, this can mean that the COD decay rate may be different in two places, however, the kinetic zone value will take precedence.` (10). 12행 로컬 그림 `attachments/1033371676/8.png`을 열었다. 그림은 Nutrients 탭의 영양염 버튼, 재폭기(reaeration), 흡착(sorption), 용존산소(DO, dissolved oxygen) 포화와 고도(elevation) 보정 선택을 보여 주는 화면 캡처이다(12–13). |
| 15–18 | 흡착·침적(deposition) — 흡착 기본값과 수정 가능 조건은 `The user may also specify the *Sorption Options*. The default is "None" and parameters cannot be modified. However, if *Total Active Metal (TAM) Based* or *Cohesive Sediment Based* radial buttons are selected, the user may alter these nutrient sorption parameters with the *Modify Parameters* button.` (15). 선택한 반응속도론(kinetics) 모듈에서 모의하는 성분의 습식 침적(wet deposition) 농도와 건식 침적(dry deposition) 질량 플럭스(mass flux) 설정은 `The atmospheric wet deposition concentrations for the constituents being simulated with the kinetic module selected are edited via the *Wet Deposition* button. The dry deposition mass fluxes are edited via the *Dry Deposition* button.` (17). |
| 19–21 | 재폭기·DO 포화 — 다섯 재폭기 선택과 각 기본값 지정은 ` The user can also configure reaeration options in this frame. The drop-down menu provides 5 options including constant (WQKRO), constant + wind-generated, O'Connor-Dobbins (1958), Owens & Gibbs (1964), and Owens & Gibbs (modified). Each option will assign a default reaeration value.` (19). 압력과 고도에 따른 DO 포화 농도 설명, 공식(formulation)과 고도 보정의 선택값은 `The saturation concentration of DO in water increases as pressure increases. This means that water at lower altitudes can hold more dissolved oxygen than water at higher altitudes. Allowance for the effect of elevation on the DO of the waterbody to DO, can be set in *DO Saturation Options* frame The user can select different options from the drop-down list of the *F**ormulation* option. Options include Garcia and Gordon (1992), Chapra et al. (1997), and Genet et al. (1974). There are three options in the *Elevation Adjustment* drop-down, including to not use the elevation adjustment, as well as the Chapra et al. (1997), and Zison et al. (1978) adjustments.` (21). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: CSS 선택자와 색상 선언이 본문 앞에 남아 있다.
- 10행: `#Nutrients-Figure1` 링크에 대응하는 명시적 앵커 정의가 이 Markdown 파일에 없다.

