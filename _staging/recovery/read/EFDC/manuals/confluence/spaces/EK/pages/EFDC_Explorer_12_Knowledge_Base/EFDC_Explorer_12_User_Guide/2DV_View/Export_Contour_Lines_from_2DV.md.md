---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DV_View/Export_Contour_Lines_from_2DV.md
lines: 24
sha256: 25b25cbc5981f25cf8a3e099f52292d2270447232e1466b18e83b115134d0021
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Export_Contour_Lines_from_2DV.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–19 | 2DV 등치선 표시 — 먼저 New 2DV View·2DV Data Extraction 설명에 따라 변수를 지정한다(10). `Show Contour` 버튼의 체크 또는 범례 오른쪽 클릭의 Properties에서 `Show Contours` 체크로 표시하는 두 방법을 설명한다(10). 메뉴 적용 조건 원문은 `*Properties for Temperature* (if you are displaying temperature)`이다(10). 그림 1·2를 직접 열었다(12·16). 그림 1은 `Show Contour` 메뉴를 열어 둔 수온 단면이다. X축은 `Distance (m)`이며 `0.00000`부터 `31420.51420`까지 표시되고 중간 눈금은 `3142.05142`, `6284.10284`, `9426.15426`, `12568.20568`, `15710.25710`, `18852.30852`, `21994.35994`, `25136.41136`, `28278.46278`이다. Y축 `Elevation (m)`는 `-60`부터 `10`까지 `10` 간격이다. 범례는 `Time: 2008-06-28 00:00`, `Temperature (°C)`, 범위 `6.70`부터 `17.70`이다(12행 그림). 그림 2는 Temperature의 2DV View Properties이며 `Min. Value: 6.70`, `Max. Value: 17.71`, `Legend Precision: F2`, `Color Ramp: Default`와 체크된 `Show Contour`, 활성 Settings·Export를 보여 준다(16행 그림). |
| 20–24 | 등치선 설정과 파일 출력 — 설정은 2DH와 같으며 상세는 Export Contour Lines from 2DH 링크로 안내한다(20). OK로 등치선을 표시하고 범례 LMC 후 Properties for Temperature의 Export로 파일을 내보낸다고 적는다(20). 그림 3을 직접 열었다(22–24). 2DV View Properties의 Export 버튼이 강조되어 있고 `Min. Value: 7`, `Max. Value: 20`, `Legend Precision: F0`, `Color Ramp: Viridis`이다(22행 그림). 배경 단면은 `2008-07-01 08:00`, `Temperature (°C)`이며 색상 범례 눈금은 `7.00`, `8.00`, `9.00`, `10.00`, `11.00`, `12.00`, `13.00`, `14.00`, `15.00`, `16.00`, `17.00`, `18.00`, `20.00`이다. 보이는 청록 등치선 표시는 `7`, `9`, `11`, `13`, `15`, `17`이며 그 사이 노란 등치선도 있다. X축은 Distance (m), Y축은 Elevation (m)이며 Y 범위는 -60부터 10이다. 오른쪽 X축 일부는 속성 창에 가려져 있다(22행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·20: Properties를 여는 클릭을 10행은 RMC, 20행은 LMC라고 적는다.
- 22·24: Figure 3 캡션은 `Contour Range Setting`이며 실제 그림은 2DV View Properties 창과 강조된 Export 버튼이다.
- 10·20: `#Figure1`, `#Figure2`, `#Figure3` 링크가 있지만 이 Markdown 파일에는 해당 앵커 정의가 없다.
