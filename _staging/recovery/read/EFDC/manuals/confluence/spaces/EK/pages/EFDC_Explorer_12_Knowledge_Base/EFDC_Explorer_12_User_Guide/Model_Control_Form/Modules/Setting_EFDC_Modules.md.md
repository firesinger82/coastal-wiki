---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Setting_EFDC_Modules.md
lines: 24
sha256: b13d8640d1ee97417b2ebee64975532d48c10388895c7ccce298cc2e65f0c6e7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Setting_EFDC_Modules.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터. Setting EFDC Modules의 식별자·제목·space·URL·버전·갱신 시각·계층 경로가 있다 (2–8). |
| 10–19 | 모듈의 활성화와 퇴적물 모델 선택. 본문 앞에 색상 CSS가 있다 (10). Modules 우클릭으로 EFDC Modules 폼을 연다 (10). 스위치는 `C6 in EFDC.INP` (12)에 있으며 선택 여부에 따라 모듈 하위 탭을 표시하거나 숨긴다 (12). 퇴적물 설정의 조건은 `If the *Activate Cohesive Sediments* or the *Activate Non-Cohesive Sediment* boxes have been selected, the user may make changes to the sediments and sediment bed settings.` (14)이다. `Original Model` (16)과 `SEDZLJ Model` (16) 중 퇴적물 모델을 먼저 지정한다. SEDZLJ의 퇴적물 플럭스·활성층 두께 출력도 표시할 수 있다고 적는다 (16). 18행 그림은 Active Modules와 계산 방법 선택 화면이다. Salinity·Temperature·Dye는 선택되어 있다. 나머지 목록은 `(Original) Cohesive Sediments; (Original) Non-Cohesive Sediments; (SEDZLJ) Sediments; Toxics; Water Quality; Waves; Lagrangian Particle Tracking; Propeller Wash; Marine Hydrokinetic Devices` (18행 그림)이며 미선택이다. Model Selection은 `Use EFDC+ Model` (18행 그림)이고 전역 수송 방법은 `Upwind Difference; Anti-Diffusion Correction; Flux Limitation` (18행 그림)이다. |
| 20–24 | 모델 종류와 전역 수송 방법. `EFDC\_GVC` (20)와 `EFDC+` (20)를 지원한다고 적는다. 기존 EFDC.INP로 종류를 자동 식별하며, 종류 변경 시 층 구성과 경계 조건을 확인해야 한다 (22). 해당 본문의 버전 조건은 `note that GVC is not implemented in EE10.0` (22)이다. 수송 방법 목록은 `Upwind Difference, Central Difference, and Experimental Upwind` (24)이며 `Anti-Diffusion or Anti-Diffusion Correction` (24)을 선택할 수 있다. 같은 방법을 모든 성분에 적용하고 Details에서 개별 설정을 한다 (24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 본문 앞에 색상 CSS가 남아 있다 (10).

