---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Getting_Started/Checklist_for_Building_a_Hydrodynamic_Model.md
lines: 80
sha256: 37a27b982a25419df3c9f6b2a45c1fe406be1f04eea7acc5d0b6a9812d8949b2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Checklist_for_Building_a_Hydrodynamic_Model.md — 판독 구간 기록

구간은 1행부터 80행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 메타데이터와 점검표 권고 — EEMS 모델 구축의 주요 요소를 점검하기 위해 이 목록 사용을 권고한다(1–10). 이는 원문에 실린 모델 구축 점검표이며 이번 판독 작업의 수행 지시로 적용하지 않았다. |
| 12–37 | Pre-modeling / A1–A10 — 연구 목적·제약·일정, 대상 영역·질문, 현장 특성·자료·주요 과정, 적합한 모델, 방정식 차원과 가정, 필요한 과정·계산 자원, 경계·검증 자료, 충분한 자원, 검증 기준, 문서화·의뢰인 동의·검토를 확인한다(12–36). 모델 선택 예시 원문: `1. Correct equations solved (e.g., 1D/2D/3D, mild slope, hydrostatic assumption)` (22); `2. Important processes included (e.g., long/short waves, rising/plunging flow, stratification/lateral variation)` (23). Tier 1과 Tier 2 분석을 수행한 항목이 있다(34). |
| 38–39 | 수심 자료 수집·용도 도식 — 38행 로컬 `bathymetry-fig1-rev5.jpg`를 열었다. 제목은 `Collection Methods and Uses of Bathymetry`다. 왼쪽 비행기의 LiDAR 광선은 지면으로 내려간다. 가운데 얕은 수역 선박의 Single Beam Echo Sounders (SBES) 빔은 하상 한 곳으로 내려간다. 오른쪽 선박의 Multi-Beam Echo Sounders (MBES) 빔은 깊은 하상에 부채꼴로 펼쳐진다. SBES 빔 폭 원문은 `Typically has a-width of 10-30 degrees.`이다(38행 그림). MBES는 더 깊은 수역에 적합하며 고정 방위각에서 경사 거리와 고도각을 추정한다고 적는다. 수치 축·수식·화살촉은 없다. 도식은 수심 자료의 용도를 퇴적물 오염 구역·어류 서식 및 번식 구역·군사와 국방·해양 순환·해저 케이블·천연자원과 생물다양성·조석 침수 예측·항해 해도로 나열한다(38행 그림). |
| 40–53 | Model Setup / B1–B4 — 경계 위치 영향, 격자 세분화(grid refinement)에 의한 해상도, 수심 및 형상을 시험·확인한다(40–46). 목적에 맞는 경계 조건(boundary condition), 과도현상을 제거할 충분한 초기 조건(initial condition)·준비 기간(spin-up), 별도 검토자의 확인을 점검한다(48–52). 충분성 조건 원문: `B3. Initial conditions and spin-up is shown to be adequate to eliminate transients` (50). |
| 54–61 | Model Validation / C1–C3 — 조정 매개변수가 알려진 불확실성의 합리적 범위 안에 있는지, 모델과 실물(model-prototype) 일치가 목적·검증 기준에 부합하는지, 문서화·의뢰인 동의·검토 여부를 점검한다(54–60). 이 구간은 실제 매개변수 이름이나 수치 범위를 제공하지 않는다. |
| 62–71 | Model Tests / D1–D4 — 목적에 맞는 시험 조건, 매개변수·계획 민감도, 기대 및 다른 연구와 일치하는 합리적 결과, 문서화·의뢰인 동의·검토 여부를 점검한다(62–70). |
| 72–80 | Reporting / E1–E4 — A–D 문서화, 적절한 신뢰 한계(confidence limits)·유보 조건(caveats), 목적과 결과 한계에 맞는 해석·결론, 의뢰인·검토자 피드백을 통한 보고서 개선을 점검한다(72–80). E1 원문은 `E1. Items A-D documented inconsistent understandable fashion` (74)이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 34행: `Tier 1`과 `Tier 2` 분석의 정의·내용은 이 파일에 없다.
- 74행: E1 문장은 `Items A-D documented inconsistent understandable fashion`으로 적혀 있다. 원문 문구를 수정하지 않고 기록했다.
