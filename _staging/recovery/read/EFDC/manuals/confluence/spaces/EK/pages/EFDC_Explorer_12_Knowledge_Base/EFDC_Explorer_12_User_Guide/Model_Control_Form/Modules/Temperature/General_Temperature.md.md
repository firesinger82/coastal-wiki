---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Temperature/General_Temperature.md
lines: 22
sha256: c436b75f078a29b5d96cc9dbe4905ab8a65013bb67a017730827fe9a7ff22dd5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# General_Temperature.md — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터. General (Temperature)의 식별자·제목·space·URL·버전·갱신 시각·계층 경로가 있다 (2–8). |
| 10–13 | General 폼. 본문 앞에 색상 CSS가 있다 (10). 저상 열 교환 계수(Bed Heat Exchange Coefficient)와 증발(Evaporation Options)을 설정한다. 12행 그림은 `Heat Transfer Coefficient: 1 (W/m²/°C)` (12행 그림); `Convective Heat Transfer Coefficient: 0.001` (12행 그림); `Ignore Evaporation & Rainfall from ASER` (12행 그림)를 보여 준다. |
| 14–22 | Evaporation Options의 표시 조건과 물수지(water balance). 표시 조건은 `The *Evaporation Options (Water Balance Only)*frame is only displayed if the appropriate surface heat exchange sub-model has been shown in the *Surface Heat Exchange* tab.  *Evaporation Options* will only appear for the following surface heat exchange options:` (16)이다. 적용 하위 모델 이름은 `1. Full Heal Balance (Legacy)` (18); `2. Full Heat Balance with Variable Extinction Coefficient` (19); `3. Equilibrium Temp (CE-QUAL-W2 Method)` (20)이다. 물수지에서 증발은 선택 항목이고, 물수지 변화는 부영양화(eutrophication)를 포함한 결합 모듈에 반영된다 (22). 표면 열 교환에서의 포함 조건은 `Note that evaporation is always included in the surface heat exchange processes.` (22)이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 본문 앞에 색상 CSS가 남아 있다 (10).
- 첫 하위 모델 이름이 `Full Heal Balance (Legacy)`로 쓰여 있다 (18).

