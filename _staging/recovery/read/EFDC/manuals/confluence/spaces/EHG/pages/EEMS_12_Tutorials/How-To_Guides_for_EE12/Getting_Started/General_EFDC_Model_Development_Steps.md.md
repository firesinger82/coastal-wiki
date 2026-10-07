---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Getting_Started/General_EFDC_Model_Development_Steps.md
lines: 130
sha256: 0d3a945b75bfefe1fc78badc3fc5a6097dec123e4331cca2d70d3ed253be800d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# General_EFDC_Model_Development_Steps.md — 판독 구간 기록

구간은 1행부터 130행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 메타데이터·단계별 개발 전제·개발 흐름도 — 앞 단계에 기반해 복잡도를 증가시키며 모델을 만들어야 한다고 적는다(1–10). HEM3D 수질 하위 모델은 EFDC 유체역학 보정(calibration) 후에만 개발할 수 있다고 적는다(10). 조건 원문: `It is imperative that an EFDC+ model be built ***step by step,***with each step building on the previous step and *increasing in complexity*.  For example, the HEM3D water quality sub-model can only be developed after the EFDC hydrodynamics has been calibrated. The basic development steps are provided below.` (10). 12행 로컬 `EEMS.jpg`를 열었다. 도식의 실선 화살표는 Natural environment, Grid+ 2D Grid Generator, 곡선 격자 생성, EE 전처리·모델 구축, EFDC+, EE 후처리·보정·검증, EE 보고서, 과학적 권고, Natural environment 순으로 원을 이룬다. `Iterate easily` 점선은 Grid+와 EE 전처리 사이 및 EE 전처리와 EE 후처리 사이에서 양방향으로 이어진다. 수식·수치 축은 없다. |
| 14–55 | 1. Gather Existing and/or New Data — GIS·지도, 고밀도 수심 자료, 상류·미계측 지류·지하수·점/비점 유량, 선택적 강우·증발, 수위, 바람, 수온 모의용 대기, 수층 성분, 퇴적물 하상 특성, 반응률과 분배 특성을 수집한다(14–55). 수위의 수직 기준면(vertical datum)은 가능하면 연결한다고 적는다(30). 이름·조건·권고 자료 간격 원문: `  - Rainfall (optional)` (26); `  - Evaporation (optional)` (27); `  - Levels should be tied to a vertical datum, if possible` (30); `  - Wind speed` (33); `  - Wind direction` (34); `  - Best if these data are 15-minute or shorter duration averaged data from 1 to 10 second sampled anemometers.` (35); `- Atmospheric data (for temperature modeling)` (36); `  - Pressure` (38); `  - Temperature` (39); `  - Relative humidity` (40); `  - Solar radiation` (41); `  - Cloud cover` (42); `  - Best if these data are hourly or of a shorter duration` (43); `  - For sediment transport also need settling speeds and flocculation` (46); `  - Vertical concentration gradients, if exist` (47); `- Kinetic rates and/or transformation process rates` (54); `- Dissolved/sorbed partitioning characteristics` (55). |
| 56–73 | 2. Review Data / 3. Develop a Conceptual Model / 4. Select Mathematical Model — 공통 수평·수직 기준면과 단위로 변환하고 공간·시간 패턴, 자료 품질, 이상값을 확인한다(57–63). 유량·변환과 구동력을 결합한 개념 모형(conceptual model)을 만들고 적절한 수학 모형(mathematical model)을 선택한다(65–72). 이 안내에서는 EEMS를 가정한다(72). |
| 74–93 | 5. Build Grid / 6. Flow/Water Surface Elevation Model — Grid+ 곡선 직교 격자(curvilinear orthogonal grid), Grid+/EE Cartesian 격자, 외부 격자 가져오기 중 선택하고 수심을 추가한다(74–84). 외부 형식 원문: `  - SEAGRID` (80); `  - CH3D` (81); `  - ECOMSED` (82); `  - Generic 4-corner format` (83). 보통 빠른 처리를 위해 1층 모델을 사용할 수 있다고 적는다(88). 초기·유량·개방 경계 조건(open boundary condition), 물수지(water balance), 유량·수위 보정을 구축한다(89–92). |
| 94–108 | 7. Full Hydrodynamics (HYD) / 8. Sediment Transport (SED/SND) — 필요할 때 수직층을 추가하고 염분·수온 초기 및 경계, 바람·대기를 설정한 뒤 유속·염분·수온 자료로 보정한다(94–99). WSER·ASER의 적용 조건 원문: `- Build boundary conditions for salinity, temperature and winds (WSER) and atmospheric data (ASER – required for temperature modeling)` (98). 퇴적물은 적용 목적에 필요한 상세 수준을 추가하고 초기·경계·수층 농도·가능한 퇴적/세굴 패턴을 보정한다(101–107). 최소 성분 권고 원문: `- Add the level of detail required for your application.  WQ models usually need some TSS for light extinction analysis, so it is best to include at least a cohesive and/or a silt.` (103). |
| 109–119 | 9. Chemical Fate and Transport (TOX) — 보정된 퇴적물 수송 모델을 확보한 후에만 독성물질(toxics) 모델링을 시작한다(109–111). 하상·수층 농도, 퇴적물·유기탄소와의 상호작용, 입자·공극수(porewater) 확산 및 혼합, 해당하는 지하수 플럭스를 설정하고 보정한다(112–118). 적용 조건 원문: `- Only start toxics modeling once a calibrated sediment transport model is available` (111); `- Determine groundwater fluxes, if applicable` (117). |
| 120–129 | 10. Water Quality (WQ) — 유체역학과 수온을 적절히 보정한 뒤에만 수질을 추가할 수 있다고 적는다(120–122). 수질·수온 상호작용 때문에 수온 보정을 조정할 가능성이 높다고 적는다(122). 퇴적물 속성작용(sediment diagenesis) 또는 영양염·DO 플럭스, 수질 복잡도·조류 구획 수, 초기·경계 조건을 정하고 보정한다(123–128). 전제·불확실성 원문: `- Water quality can only be added to the model once the hydrodynamics and temperature is suitability calibrated. Due to the WQ/temperature interaction, temperature calibration will likely need to be adjusted.` (122). |
| 130–130 | 11. Conduct the Analysis with/or Based on the Final Model — 최종 모델에 근거해 분석하는 단계의 제목만 있고 뒤 설명은 없다(130). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 130행: 11단계는 절 제목만 있으며 절 본문이 없다.
