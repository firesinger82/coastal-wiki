---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Time_Series_Contours.md
lines: 34
sha256: 3f62ffc3139a151437923c8a7d006a98a2f87b818e3b64339ec5e99869a0f283
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Time_Series_Contours.md — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–17 | 시계열 등치선(Time Series Contours) / 기능과 진입 — EE7.2부터 특정 `I`·`J` 위치에서 시간·수심 배경에 수직 성분의 등치선(contour)을 열지도(heatmap)처럼 표시한다고 설명한다(10). Temperature 레이어 셀을 오른쪽 클릭하고 기간을 정해 수온의 수주(water column) 변화와 성층(thermal stratification)을 살핀다(12). 유속·염분에도 사용할 수 있으며 범례 오른쪽 클릭으로 최소·최대 등치선과 float·fixed 정밀도를 설정한다(12). 그림 1을 직접 열었으며 수심 평균 수온 레이어 셀의 Show Time Series Contours 메뉴를 보여 준다(14–16). |
| 18–29 | 그림 2–4 / 시간·수직축·등치선 설정 — 세 그림을 직접 열었다(18·22·26). 그림 2의 X축은 `Time (days)`이며 `213`부터 `713`까지 `50` 간격이다. Y축은 `Height Above Bottom (m)`이며 `0.00`부터 `25.00`까지 `2.50` 간격이다. 범례는 `Water Temperature`, `i=33, j=24`, 색상 범위 `-0.01`부터 `28.65`이다(18–20). 따뜻한 시기의 상부는 빨강·노랑이고 가운데 기간은 대부분 파랑이며 수면 위는 흰 영역이다. 그림 3의 표 원문은 `Start Extraction (day): 213`, `Stop Extraction (day): 713`이다(22–24). 그림 4는 Timeseries Contour Settings 창이다. 화면의 `Data Range`와 `Contour Range`는 모두 `Minimum: -0.01`, `Maximum: 28.65`이며 `Label Precision`은 `Fixed`, `Prec.: 2`이다(26–28). 이 값은 화면 예시 값이다. |
| 30–34 | Layer Settings와의 관계 — 적용 조건 원문: `The user can plot *Time Series Contours* for a parameter regardless of the configuration of the *Layer Settings > Options* (by each layer, depth-averaged, or for all layers) while importing that parameter into 2DH View` (30). 그림 5를 직접 열었으며 `Primary Group: Water Column`, `Parameter: Temperature`, Layer Settings의 `Options: Depth Average`인 2DH View Option 창을 보여 준다(32–34). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18행 그림 2: 수온 범례는 값 `-0.01`부터 `28.65`를 표시하지만 온도 단위를 쓰지 않는다. 14행 그림 1의 수온 범례는 `(°C)`를 표시한다.
