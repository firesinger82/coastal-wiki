---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Temperature_EEMS12/Heat_Exchange_EEMS12.md
lines: 24
sha256: df4335dd53bf9a67ed489f9cd09f8ceac0225bfd0a0ad7ee46865bae9ac1efc2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Heat_Exchange_EEMS12.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터. Heat Exchange (EEMS12)의 식별자·제목·space·URL·버전·갱신 시각·계층 경로가 있다 (2–8). |
| 10–21 | 표면 열 교환(Surface Heat Exchange) 선택. 본문 앞에 색상 CSS가 있다 (10). 다섯 모델은 `- No Atmospheric Linkage` (12); `- Full Heat Balance` (13); `- COARE3.6` (14); `- Equilibrium Temp (CE-QUAL-W2 Method)` (15); `- External Equilibrium Temperature` (16)이다. Full Heat Balance와 COARE3.6의 추가 설정 조건은 `If the *Full Heat Balance* or COARE3.6 model is used, the user needs to specify the *Heat Transfer Coefficients* ([Figure 2](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2343829625#HeatExchange(EEMS12)-Fiu)) and *COARE* parameters ([Heat Exchange (EEMS12)#Figure 3](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2343829625#HeatExchange(EEMS12)-Figure3)), respectively, while other models require no further specifications.` (18)이다. DSI의 성능 비교 글을 언급하지만 링크는 없고 이 파일에 비교 결과도 없다 (18). 20행 그림은 기본 설정 폼이며 `Surface Heat Exchange Option: No Atmospheric Linkage` (20행 그림); `Heat Transfer Coefficient: 0 (m/s)` (20행 그림); `Convective Heat Transfer Coefficient: 0 (dimensionless)` (20행 그림)이다. Allow Bed Temperatures to Vary with Time은 미선택이다. |
| 22–24 | 저상 열 교환(Bed Heat Exchange)과 추가 계수. 시간에 따른 저상 온도 변동을 허용할 수 있다. 활성화·단위·보정 조건은 `The bed heat exchange configuration can be assessed under the *Bed Heat Exchange* option. The user can set to allow temporal variation of bed temperatures by checking the box. The *Heat Transfer Coefficient* larger than 0 enables the heat flux between water and the sediment bed. Attention should be given to the unit conversion of this coefficient from W/m2/°C to m/s. If the entry is larger than 1E-05 m/s, which is outside the conventional range, EE checks and corrects by multiplying it with 2.39E-07. The Convective Heat Transfer Coefficient is dimensionless and used to simulate the heat exchange at the sediment bed with the presence of solar radiation.` (22)이다. `Heat Transfer Coefficient`가 `0`보다 크면 열 플럭스를 활성화한다. 입력이 `1E-05 m/s`보다 크면 `2.39E-07`을 곱해 보정한다고 적는다 (22). 24행 첫 그림은 Full Heat Balance 설정이며 `Heat Transfer Coefficients (Dimensionless, Scaled by 1000)` (24행 그림); `Evaporative Heat Transfer Coefficient: 1` (24행 그림); `Convective Heat Transfer Coefficient: 1` (24행 그림); `Heat Transfer Coefficient: 0 (m/s)` (24행 그림); `Convective Heat Transfer Coefficient: 0 (dimensionless)` (24행 그림)이다. Vary with Wind Speed 두 상자·Use Spatially Varying Factors·Allow Bed Temperatures to Vary with Time은 미선택이다. 둘째 그림은 `Surface Heat Exchange Option: COARE 3.6` (24행 그림); `Planetary Boundary Layer Height (m): 600` (24행 그림); `Height of Temperature/Humidity Sensor (m): 2` (24행 그림); `Number of Iterations: 10` (24행 그림); `Heat Transfer Coefficient: 0 (m/s)` (24행 그림); `Convective Heat Transfer Coefficient: 0 (dimensionless)` (24행 그림)이다. 저상 온도의 시간 변동은 미선택이다 (24행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 본문 앞에 색상 CSS가 남아 있다 (10).
- Figure 2 링크의 앵커가 `#HeatExchange(EEMS12)-Fiu`로 끝난다 (18). 파일에 이 이름의 명시적 앵커는 없다 (1–24).

