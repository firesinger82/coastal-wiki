---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Temperature/Surface_Heat_Exchange.md
lines: 29
sha256: 876b05edfe451033a51ff24141a25ed3603a0a6bc569cc2c1b82489ae5848c52
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Surface_Heat_Exchange.md — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터. Surface Heat Exchange의 식별자·제목·space·URL·버전·갱신 시각·계층 경로가 있다 (2–8). |
| 10–22 | 표면 열 교환(Surface Heat Exchange) 하위 모델 선택. 열 교환 계수·빛 감쇠(light extinction) 설정은 선택한 모델에 따라 달라진다 (10). 퇴적물 미계산 조건은 `For example, if sediments are not being simulated the *Light Extinction for TSS* is hidden as not applicable.` (10)이다. 여섯 옵션은 `- No Atmospheric Linkage` (14); `- Full Heat Balance (Legacy)` (15); `- External Equilibrium Temperature` (16); `- Constant Equilibrium Temperature Coefficient` (17); `- Equilibrium Temperature (CE-QUAL-W2 Method)` (18); `- Full Heat Balance with Variable Extinction Coefficient` (19)이다. 21행은 옵션을 아래에서 더 설명한다고 적는다. |
| 23–29 | 필수 대기 자료와 가변 감쇠 계수. 원문의 파일 의무와 모델 구분은 `The ASER.INP file must be used for all of the thermal sub-models to compute the surface and bottom heat exchange processes. Also, depending on whether the current model is EFDC\_GVC or EFDC+, the EFDC+ Explorer form will have different options shown in the tab*.*` (23)이다. 25행 그림은 `Surface Heat Exchange Sub-model: Full Heat Balance with Variable Extinction Coeff` (25행 그림) 설정이다. `Surface Heat Transfer Coefficients (Dimensionless, Scaled by 1000)` (25행 그림); `Evaporative Heat Transfer: 1` (25행 그림); `Convective Heat Transfer: 1` (25행 그림); `Light Extinction Coefficients in Units of 1/m per g/m³ Unless Otherwise Specified (EFDC+)` (25행 그림); `Background: 3 (1/m)` (25행 그림)이다. 두 Vary with Wind Speed 상자는 선택되었고 Use Spatially Varying Factors는 미선택이다. 비활성 필드에는 Evaporative Coefficient가 보인다 (25행 그림). 가변 감쇠는 격자·시간별 총부유고형물(Total Suspended Solids, TSS)을 사용하고 수질 모듈이 활성화되면 입자성·용존 유기물과 chlorophyll-a도 사용한다 (27). 풍속 의존 열 교환 적용 조건은 `With this option the user may also set the evaporative and convective heat transfers to be impacted by the wind speed. The user should select the appropriate check box for the *Vary with Wind Speed*option, and then ensure a correct setting for the heat transfer coefficient for each option.` (29)이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 여섯 옵션을 아래에서 더 설명한다고 적는다 (21). 뒤의 설명은 Full Heat Balance with Variable Extinction Coefficient에 한정된다 (27–29).

