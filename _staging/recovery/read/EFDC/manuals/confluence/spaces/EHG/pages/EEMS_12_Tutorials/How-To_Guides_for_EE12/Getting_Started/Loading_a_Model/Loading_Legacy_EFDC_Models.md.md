---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Getting_Started/Loading_a_Model/Loading_Legacy_EFDC_Models.md
lines: 20
sha256: 8dc6b669d95b8adc38a4a8f579b10e104a40ba1f19f969f7c9e6445e88cefccb
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Loading_Legacy_EFDC_Models.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 메타데이터와 기존 모델 로드 옵션 — EE 없이 만든 기존 모델(legacy model)에 Load Options를 사용할 수 있으며 보통 최초 로드 때만 필요하다고 적는다(1–10). EE가 다시 저장하면 최신 형식으로 바뀐다고 적는다(10). EE는 CELL.INP 형식 차이를 자동 처리하며 과거 입력 파일 대부분을 올바르게 읽으려 시도한다고 적는다(12). 불확실성과 적용 조건 원문: `The options provided in the *Legacy EFDC Project – Load Options* frame can be used when loading old/legacy EFDC projects that were developed without EFDC+ Explorer. Generally, these only need to be used the first time EE loads the project.  When EE writes a project it saves the project out in the updated formats so these options do not need to be used but once for a legacy model application.` (10); `Historically, different versions of EFDC used different CELL.INP formats.  EFDC+ Explorer automatically handles the file format to correctly load the CELL.INP file.  Similarly, the main EFDC.INP file and other input files have changed over the recent development history of EFDC.  EFDC+ Explorer attempts to correctly read most of the historical input files while ensuring the latest version works and is the standard.` (12). |
| 14–19 | Scale과 LXLY 좌표 단위 — 14행 로컬 `EE10_2.png`를 열었다. 그림은 디렉터리 선택 아래의 `Scale: 1`, `Reset BC Groups During Load`, `Force Distinct BC During Load`, `Load Water Quality Mass Loading BC's Without Associating Flow BC's to the WQ BC's`를 강조하며 세 상자는 해제됐다(14행 그림). Scale은 기존 LXLY 셀 중심좌표(centroid)의 단위를 EE 기본 XY 단위인 m로 바꾸는 계수다(16). 좌표가 km·mile이면 m로 바꿔야 하며 최초 로드에 Scale을 입력할 수 있다고 적는다(16). 큰 셀이 서로 겹쳐 보이면 LXLY 단위 변환 문제일 가능성이 높다고 적는다(18). 단위·조건·불확실성 원문: `The *Scale* input box allows the user to apply a conversion factor to the centroid units used in the legacy LXLY file.  The EFDC+ Explorer default XY unit is in meters.  Many applications use kilometers or miles as the units for the cell centroids provided in the LXLY file.  For EE to correctly display the model these cell centroid coordinates must be converted to meters.  EE can perform this function by entering the conversion factor in the *Scale* box when loading the model for the first time.` (16); `*When a model is loaded and then viewed but looks like a bunch of large cells stacked on top of one another, it is likely to be a LXLY units conversion issue.  Try reloading the model with an appropriate Scale factor.*` (18). |
| 20–20 | 경계 조건 그룹 재설정 — EE가 관리하던 기존 프로젝트의 재그룹 옵션을 설명한다(20). 최초 로드 또는 Reset BC Groups During Load 선택 시 경계 셀을 유형·위치별로 그룹화하려 시도한다(20). 특정 WQ 질량 부하 경계에 무유량 경계가 지정된 경우 해당 WQ 부하 옵션을 적용한다고 적는다(20). 적용 조건·옵션 이름 원문: `The checkboxes concerning resetting boundary condition groups apply to existing projects that have been managed by EFDC+ Explorer.  During the initial loading of a project, or if the *Reset* *BC Groups During Load*check box is selected, EFDC+ Explorer tries to logically group boundary condition cells into groups by type and location.  EFDC+ Explorer then manages the boundary conditions using this group approach.  If the user has modified the boundary conditions somehow and wants a different logical grouping, they should select one of these options. The *Load WQ Mass Loadings BC’s Without Associating Flow BC’s to the WQ BC’s* option is applicable when the user has no-flow boundary condition assigned for a specific WQ mass loading boundary.` (20). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
