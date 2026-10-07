---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/View_Layer_Control/Downstream_Projection_for_Velocity.md
lines: 30
sha256: cb488b467ec041fe87282578db4307c818845cb4efa48374aff830f6fd607bfa
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Downstream_Projection_for_Velocity.md — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–19 | 유속의 하류 방향 투영(Downstream Projection for Velocity) / 각도·기간·수주 범위 — CSS 색상 마크업 뒤에 EEMS10.4부터 제공하는 기능이라고 적는다(10). 각도 기준·단위 원문은 `an orientation angle (degrees clockwise from north, looking downstream)`이다(10). EE 자료 추출에서 상류·하류 흐름의 유속 크기를 그린다(10). 유속 레이어를 추가하고 활성 모드를 켠 뒤 셀을 선택한다(12). 측정 장치의 수면 아래 깊이를 아는 경우 모델·실측의 정확한 비교에 주로 사용한다(14). 셀 오른쪽 클릭의 Downstream Projection에서 전체 모델 기간 안의 추출 기간을 정하며 시간 형식은 `Julian date format`이다(14). 수주 비율 원문: `*From (%)* is used to indicate the percentage of the water column to be displayed from the bottom of the water column up to the *To (%)*.` (16). 예시 원문: `For example, in a 10 m water column, from 10% to 90% means the velocity magnitude it will be plotted from 1 m above the bottom and up to 9 m from the bottom.` (16). OK로 추출한다(18). |
| 20–27 | 그림 1·2 / 진입과 추출 설정 — 두 그림을 직접 열었다(20·24). 그림 1은 Velocity Magnitude (Depth Avg.) 활성 레이어, 선택 셀 정보, DownStream Projection 메뉴를 보여 준다(20–22). 그림 2의 표는 `Start Extraction (day): 2922`, `Stop Extraction (day): 2932`, `Downstream Angle(degrees from North): 169`, `From (%): 10`, `To (%): 90`이다(24–26). 이 값은 화면 예시 값이다. |
| 28–30 | 그림 3 / 유속 투영 그래프 — 그림을 직접 열었다(28). X축 `Time (days)`는 `2922.00`부터 `2930.00`까지 `0.80` 간격이다. Y축 `Current Velocity (m/s)`는 `-0.340`, `-0.264`, `-0.188`, `-0.112`, `-0.036`, `0.040`, `0.116`, `0.192`, `0.268`, `0.344`, `0.420`이다. 검은 수평선은 0이며 위쪽에 빨간 점과 `Downstream` 표기가 있다. `Downstream Angle: 169`가 표시되어 있다. 셀 `121 (I: 17, J: 10)`의 Layer 1은 빨강, Layer 2는 파랑, Layer 3은 초록, Layer 4는 자홍, `Layer Range from 10% to 90%`는 청록이다. 여러 곡선이 양수·음수 사이를 오가는 결과를 보여 준다. 캡션은 선택 셀의 모든 층을 그린 유속 투영 그림이라고 적는다(30). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14: Figure 2 링크는 이 문서가 아닌 `/wiki/spaces/EK/pages/2055176210/Velocity+Rose#Figure2`를 가리킨다. 이 문서 자체의 그림 2는 24–26행에 있다.
- 10·28: 본문은 `velocity magnitude`라고 부르며 결과 그래프 Y축은 `Current Velocity (m/s)`로 적고 음수와 양수를 모두 표시한다.

