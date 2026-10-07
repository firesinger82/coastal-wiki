---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Water_Quality_EEMS10.md
lines: 14
sha256: ad80ab7ed388d921236f73b0ce5c5cb745ea87eb1073404e86b1617aa7c77f6f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Water_Quality_EEMS10.md — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, EEMS10.2 제목, space, 원문 URL, 판본, 갱신 시각과 경로를 담은 frontmatter를 읽었다(1–9). |
| 10–14 | Water Quality / 설정 진입점 — EE는 EFDC 수질 하위모델의 그래픽 사용자 인터페이스(graphical user interface, GUI)이며 문서는 이 모델을 HEM3D라고도 부른다(10). 반응(Kinetics), 영양염(Nutrients), 조류(Algae), 초기조건(Initial Conditions), 경계조건(Boundary Conditions), 저서(Benthic)의 여섯 하위 메뉴를 연결한다(10). 항목 왼쪽 클릭은 설정 보고서를 보여 주고 오른쪽 클릭은 설정 폼을 연다고 설명한다(10). EFDC 판본마다 구현이 다르므로 해당 판본 소스코드에 무엇이 들어 있는지 알아야 한다는 조건 원문: `EE serves as a graphical user interface to the water quality sub-model of EFDC, sometimes called HEM3D (Park, et. al. 2000). The water quality module is EE has several sub-menu items including: *[Kinetics (EEMS10.2)](/wiki/spaces/EK/pages/245202988/Kinetics+EEMS10.2), [Nutrients (EEMS10.2)](/wiki/spaces/EK/pages/246710451/Nutrients+EEMS10.2), [Algae (EEMS10.2)](/wiki/spaces/EK/pages/246612149/Algae+EEMS10.2), [Initial Conditions](/wiki/spaces/EK/pages/246644845/Initial+Conditions+-+WQ+EEMS10.2), [Boundary Conditions](/wiki/spaces/EK/pages/246546596/Boundary+Conditions+-+WQ+EEMS10.2),* and *[Benthic](/wiki/spaces/EK/pages/246775976/Benthic+Flux).* The report of the configuration can be viewed with an LMC on each item, and RMC will open the *Water Quality* form to modify the settings *as*shown in Figure 1 below. These menu items are described in the pages following. Note that the implementation of the water quality varies between versions of EFDC so the user should be aware of what is contained in the source code for their particular version of EFDC.` (10). Figure 1의 `attachments/240222374/5-10-2019_10-02-31_AM.jpg`를 열었다(12). 화면은 왼쪽 `Modules`의 `Water Quality` 메뉴와 오른쪽 `Water Quality` 폼의 여섯 탭을 강조하며 빨간 화살표는 왼쪽 메뉴에서 오른쪽 폼을 향한다(12 그림). 폼의 표시값은 `Options: Module 1 (Standard)`, `# Simulated: 14`, `Kinetic Update Time Step(s): 40`, `Number of Kinetic Zones: 1`, `Current Zone: 1`, `Reaeration Options: Constant + Wind Generated`, `Reaeration Const: 1`, `COD Decay: 0.5`이다(12 그림). `Output Restart File (WQWCRST.OUT)`와 `Use Zones for Kinetics`는 선택되어 있다. `Output Negative Conc. Diagnostics`, `Use Zones for Settling`, `Use Zones for Algal Dynamics`는 해제되어 있고 `Zero Negative Concentrations`는 비활성이다(12 그림). 본문은 이 그림의 수치를 기본값으로 지정하지 않는다. 마지막 캡션까지 읽었다(14). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
