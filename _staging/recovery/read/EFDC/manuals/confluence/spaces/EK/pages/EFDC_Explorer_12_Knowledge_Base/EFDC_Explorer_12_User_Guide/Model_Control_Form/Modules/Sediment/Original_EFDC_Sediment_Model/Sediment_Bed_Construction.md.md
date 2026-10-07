---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Sediment/Original_EFDC_Sediment_Model/Sediment_Bed_Construction.md
lines: 44
sha256: dac4c640dd39c6b553d4c7920de37deac91aea4cc4e34588f9a8609de715b148
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Sediment_Bed_Construction.md — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터. 제목은 Sediment Bed Construction이다 (3). 문서 식별자·space·URL·버전·갱신 시각·계층 경로가 있다 (2–8). |
| 10–15 | 퇴적물층 초기화(Initialization of Sediment Beds). 전체 영역 또는 다각형 내부 격자에 균일층, 다각형 디지털 퇴적물 모델(Digital Surface Model, DSM), 입도 코어를 적용하는 방법을 소개한다 (10). 그림 1은 초기화 방법과 적용 격자 선택 화면이다 (12–14). 표시값은 `Number of Initial Layers: 1` (12행 그림); `Constant Porosity: 0.4` (12행 그림); `Minimum Surface Sediment Layer Thickness (m): 0.007` (12행 그림); `Minimum Subsurface Layer Thickness (m): 0.007` (12행 그림); `No / Max (μm): 1 / 20` (12행 그림); `No / Max (μm): 2 / 100` (12행 그림); `No / Max (μm): 3 / 625.0001` (12행 그림)이다. All grid cells가 선택되며 Use Constant Porosity는 선택되지 않았다 (12행 그림). |
| 16–28 | Uniform Layers. 균일층 생성 도구에서 층수·퇴적물 종류·분율·두께·밀도를 지정한다 (18–20). 사용자가 별도로 설정해야 하는 항목과 완료 조건은 `The user must still set the cohesive and non-cohesive erosion, and deposition parameters, but once the user finishes this option, the sediment bed configuration is ready for EFDC.` (18)이다. 층 정의는 저장·재사용할 수 있고 2DH View에서 수정할 수 있다 (20). 그림 2의 표시값은 `# Sediments: 3; # Cohesives: 1; # Non-Cohesives: 2` (22행 그림); `Diameter (μm): Coh1 10; NonCoh1 40; NonCoh2 250` (22행 그림); `Specific Grav: Coh1 2.65; NonCoh1 2.65; NonCoh2 2.65` (22행 그림); `Number of Bed Layers: 4` (22행 그림); `Layer4: Thick (m) 0.5; Porosity 0.8; FracCo1 0.3333333; FracNonCo1 0.3333333; FracNonCo2 0.3333333; Bulk/Wet 1330; Dry 530` (22행 그림); `Layer3: Thick (m) 0.5; Porosity 0.8; FracCo1 0.3333333; FracNonCo1 0.3333333; FracNonCo2 0.3333333; Bulk/Wet 1330; Dry 530` (22행 그림); `Layer2: Thick (m) 0.5; Porosity 0.8; FracCo1 0.3333333; FracNonCo1 0.3333333; FracNonCo2 0.3333333; Bulk/Wet 1330; Dry 530` (22행 그림); `Layer1: Thick (m) 0.5; Porosity 0.8; FracCo1 0.3333333; FracNonCo1 0.3333333; FracNonCo2 0.3333333; Bulk/Wet 1330; Dry 530` (22행 그림); `Layer Densities (kg/m³)` (22행 그림)이다. Morphology & Consolidation의 퇴적 공극률·점착성 공극비가 생성 도구 설정에 맞춰 변경되는 동작을 설명한다 (25). 도구는 퇴적을 위한 빈 층 두 개를 추가한다 (27). 최대 두께 관련 조건은 `If the top layer is already activated and the thickness exceeds the maximum layer thickness, EFDC will just keep adding sediment to the top layer.` (27)이다. 지나치게 두꺼운 층은 모델 구성에서 피하라고 적는다 (27). |
| 29–34 | Digital Sediment Model. 외부 DSM은 다각형 뒤에 층별 두께·벌크밀도·공극률·입도 분포를 포함한다 (31). 본문은 Appendix B의 파일 형식을 연결한다 (31). 입도 구간과 대표 지름의 관계는 `The "Max (μm)" sediment diameters, one for each sediment class, are needed to break the sediment grainsize curves into ranges. These diameters are not class diameters but represent the grain size breakpoints whose geometric mean of the upper and lower limits is the corresponding sediment class' diameter.` (31)이다. Apply는 현재 모델의 퇴적물층을 새 초기화 자료로 교체하며, 이전 버전 보존을 위한 하위 폴더 저장을 권한다 (33). |
| 35–44 | Sediment Cores with Grainsize Option. 깊이별 입도 분포와 코어 위치를 이용하며 2DH View에서 코어를 편집할 수 있다 (37–39). 초기화 도구 문서 링크가 있다 (41). 그림 3은 검은 실선 원으로 코어 위치를 표시하고, 깊이 평균 중앙입경(median grain size) 지도를 보여 준다 (37, 43–44). 범례는 `Bed d50 (Avg Layers) (μm): 268.808–768.341` (43행 그림)이며 파랑에서 빨강으로 값이 커진다. 지도에는 수치 좌표축이 없다 (43행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

