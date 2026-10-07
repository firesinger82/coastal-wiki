---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Water_Quality/Rooted_Macrophytes_Options.md
lines: 78
sha256: 9c9ee647f0811b36e4d8e9b699c0b58d6e3cbfbab64cf7fe69acca69f2a060b4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Rooted_Macrophytes_Options.md — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Rooted Macrophytes Options — 페이지 메타데이터를 담은 frontmatter이다(1–9). |
| 10–15 | RPEM 활성화 — CSS 선언 뒤의 적용 조건은 `If the user wished to use the *Rooted Plant and Epiphyte Model* (RPEM), the *Use* checkbox under *Rooted Macrophytes* frame should be checked as shown in [Rooted Macrophytes Options#Figure 1](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/1071022210#RootedMacrophytesOptions-Figure1). The *Modify* button in the *Rooted Macrophytes* frame allows the user to set various constants associated with RPEM, as shown in [Rooted Macrophytes Options#Figure 2](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/1071022210#RootedMacrophytesOptions-Figure2).` (10). RPEM은 뿌리 식물 및 부착조류 모델(Rooted Plant and Epiphyte Model)이다(10). 12행 로컬 그림 `attachments/1071022210/19.png`을 열었다. 그림은 Rooted Macrophytes Options의 Use와 Modify를 강조한 화면 캡처이다(12–14). |
| 16–21 | General — 뿌리 식물(rooted plant)·부착조류(epiphyte) 모의, 식물 위 부착조류, 수층 영양염(water column nutrient) 및 퇴적물 속성작용(sediment diagenesis) 연결의 선택값은 `The *General* tab  in the *RPEM* form allows the user to enable or disable a variety of combinations for RPEM, including enabling the simulation of rooted plants or epiphytes; enabling epiphytes growing on rooted plants; enabling *RPEM – Water Column Nutrient Interaction*; and enabling *RPEM – Sediment Diagenesis Interaction.*  For details on the theory behind this sub-model, please refer to "A Generic Rooted Aquatic Plant and Epiphyte Algae Sub-Model for EFDC" (Hamrick, 2006).` (16). 18행 로컬 그림 `attachments/1071022210/20.png`을 열었다. 그림은 네 가지 모의·상호작용 선택 영역을 담은 General 화면 캡처이다(18–20). |
| 22–31 | Initial Conditions — 초기조건(initial condition) 선택값, `WQRPEMSIC.INP`·`WQRPEMRST.INP`, 탄소 생체량(carbon biomass)과 공간 자료 적용 원문은 `The *Initial Conditions* tab is shown [Rooted Macrophytes Options#Figure 3](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/1071022210#RootedMacrophytesOptions-Figure3). This tab allows the user to set various approaches for the RPEM, such as: *Constant IC's*, *Spatially varying IC's - WQRPEMSIC.INP*, and *Spatially varying IC's - WQRPEMRST.INP*. These later options allow the user to input variable carbon biomasses rather than set them as constant values. Clicking on any of the buttons for setting shoot, root, epiphyte, or detritus carbon ICs will display a form as shown in [Rooted Macrophytes Options#Figure 4](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/1071022210#RootedMacrophytesOptions-Figure4). Using this form the user may import a poly file or a data file for the IC.` (22). 24행 로컬 그림 `attachments/1071022210/21.png`은 초기 Shoot, Root, Epiphyte, Detritus 탄소 생체량과 저층 간극수(bed porewater) 농도 입력 화면이다(24–26). 28행 로컬 그림 `attachments/1071022210/22.png`은 Shoot Carbon을 전체 셀 또는 다각형 내부 셀에 상수나 XYZ 자료로 적용하는 화면이다(28–30). 두 그림을 열었다. |
| 32–37 | Rates — 지상부(shoot)·뿌리(root)·쇄설물(detritus)의 성장(growth)·호흡(respiration) 속도 설정을 설명한다(32). 34행 로컬 그림 `attachments/1071022210/23.png`을 열었다. 그림은 Rates 탭의 지상부 생성·호흡·손실, 뿌리·쇄설물 손실, 광 제한(light limitation), 뿌리에서 지상부로의 탄소 전달 설정을 보여 주는 화면 캡처이다(34–36). |
| 38–43 | Nutrient Limits — 성장·호흡률 제한 매개변수 설정을 설명한다(38). 40행 로컬 그림 `attachments/1071022210/24.png`을 열었다. 그림은 수층·저층 영양염 흡수 반포화(half-saturation)와 원소 화학양론 비율(stoichiometric ratio) 입력 화면이다(40–42). |
| 44–49 | R & S Temperature — 뿌리·지상부 온도 설정을 안내한다(44). 46행 로컬 그림 `attachments/1071022210/25.png`을 열었다. 그림은 지상부 성장·호흡과 뿌리 호흡의 최적 온도 상·하한과 온도 효과 입력 화면이다(46–48). |
| 50–55 | Epiphytes — 부착조류의 성장·호흡, 광 제한, 온도 효과 상수 설정을 설명한다(50). 52행 로컬 그림 `attachments/1071022210/26.png`을 열었다. 그림은 부착조류 성장·호흡·손실률, 질소 반포화, 광 감쇠(light extinction)와 온도 효과 입력 화면이다(52–54). |
| 56–61 | Nutrient Fractions — 영양염 분율(nutrient fraction)의 Shoot, Root, Epiphyte, Shoot Detritus, G-class 하위 탭을 나열한다(56). 58행 로컬 그림 `attachments/1071022210/2-7-2023_9-49-35_AM.png`을 열었다. 그림은 다섯 하위 탭과 호흡·감쇠(decay) 과정의 영양염 분율 입력 화면이다(58–60). |
| 62–67 | Shoot / Root / Epiphyte — 세 하위 탭의 폼이 같다고 적는다(62). 64행 로컬 그림 `attachments/1071022210/2-7-2023_9-56-05_AM.png`을 열었다. 그림은 세 하위 탭과 호흡·비호흡 탄소·인·질소 분율 입력 화면이다(64–66). |
| 68–77 | Shoot Detritus / G-class — 두 하위 탭의 폼을 안내한다(68). 70행 로컬 그림 `attachments/1071022210/2-7-2023_9-57-01_AM.png`은 지상부 쇄설물의 탄소·인·질소 분율 입력 화면이다(70–72). 74행 로컬 그림 `attachments/1071022210/2-7-2023_9-57-44_AM.png`은 뿌리에서 생성된 난분해성 입자상 유기물(refractory particulate organic matter)을 퇴적물 속성작용 모델의 G-class로 전달하는 분율 입력 화면이다(74–76). 두 그림을 열었다. |
| 78–78 | 저장 파일 — 저장 경로와 파일명 원문은 `Values of the RPEM settings are saved in the file "wq\_rpem.jnp" of the model folder.` (78). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: CSS 선택자와 색상 선언이 본문 앞에 남아 있다.
- 10·16·22행 등: 그림 링크의 `#RootedMacrophytesOptions-Figure1` 등 조각 식별자에 대응하는 명시적 앵커 정의가 이 Markdown 파일에 없다.
- 58·64행 그림: 비호흡 인 분율 항목이 `Fraction of non-respired phosphorus produced as LPOC`와 `Fraction of non-respired phosphorus produced as DOC`로 표시되어 있다.
- 70행 그림: 오른쪽 RPOP·LPOP·DOP 항목이 `Fraction of detritus carbon produced as RPOP`, `Fraction of detritus carbon produced as LPOP`, `Fraction of detritus carbon produced as DOP`로 표시되어 있다.
