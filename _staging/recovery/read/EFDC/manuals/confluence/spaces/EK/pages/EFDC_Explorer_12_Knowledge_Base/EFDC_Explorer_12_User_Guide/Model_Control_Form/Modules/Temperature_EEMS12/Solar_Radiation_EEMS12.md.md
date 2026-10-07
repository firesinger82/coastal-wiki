---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Temperature_EEMS12/Solar_Radiation_EEMS12.md
lines: 24
sha256: 340b920cbefb8738ed82dd75d5977cf3c8250e8d61e18f96f13839276b6a2b3e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Solar_Radiation_EEMS12.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터. Solar Radiation (EEMS12)의 식별자·제목·space·URL·버전·갱신 시각·계층 경로가 있다 (2–8). |
| 10–19 | 태양복사(Solar Radiation) 자료와 분배 방법. 대기 조건을 표현하는 태양복사 자료가 필요하다고 적는다 (10). 흡수 정도와 공간 범위를 설정하는 네 방법은 `- No Solar Radiation` (12); `- Absorb 100% Solar Radiation in Surface Layer` (14); `- Use fast/slow Extinction Coefficients` (16); `- Spatially & Temporally Varying Extinction Coefficients` (18)이다. |
| 20–24 | 계수 설정과 일사량 대체 조건. `The first two options are parameterized by EE while the last two approaches are associated with different sets of parameters including *Light Extinction Coefficients* ([Figure 2](#Figure-2)) and *Light Extinction Factors for Water Column Constituent* ([Figure 3](#Figure-3)). If the Water Quality is utilized, it is advisable to compute solar radiation with the *Spatially & Temporally Varying Extinction Coefficients* approach due to the incapabilities of other methods in simulating the temperature changes made by the Water Quality components in the water column.` (20)이다. 수질(Water Quality) 성분에 따른 온도 변화를 다른 방법이 표현하지 못하므로 공간·시간 가변 감쇠 방법을 권한다고 적는다 (20). 입력 대체 조건은 `The checkbox under the method identifier enables the replacement of input solar radiation with computed solar radiation. This means that data from the external forcing repository will not be used in the simulations.` (22)이다. 24행 첫 그림은 No Solar Radiation 설정과 빈 Light Extinction Coefficients 프레임이다. 둘째 그림은 Use fast/slow Extinction Coefficients 설정이며 `Fast Coefficient: 0.125 (1/m)` (24행 그림); `Slow Coefficient: 0.063 (1/m)` (24행 그림); `Fraction Attenuated Fast: 0.78` (24행 그림)이다. 셋째 그림은 Spatially & Temporally Varying Extinction Coefficients이며 `Background: 0.063 (1/m)` (24행 그림); `Minimum Fraction Absorbed in Top Layer: 0` (24행 그림); `Water Column Constituent Related Light Extinction Factors (1/m per g/m³)` (24행 그림); `Coefficient for DOM: 0.05` (24행 그림); `Coefficient for POC: 0.7` (24행 그림); `Coefficient for Chl-a: 0.031` (24행 그림); `Chl-a Exponent: 1` (24행 그림)이다. 세 그림 모두 `Use Computed Solar Radiation to Overwrite Input Solar Radiation` (24행 그림)는 미선택이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

