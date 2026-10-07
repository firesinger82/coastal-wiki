---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Salinity/Salinity_Visualization.md
lines: 40
sha256: d8114df88b46338a916aa38a357273a75274e92937a89355aa917ecc49dc06b3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Salinity_Visualization.md — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID `2131362027`, 제목 `Salinity Visualization`, space, URL, version, 갱신 시각, 문서 계층과 frontmatter 구분자를 포함한다(1–9). |
| 10–15 | 2DH View — 10행의 CSS 선언과 절 제목을 포함한다. 염분(salinity)을 2차원 수평 보기(2DH View)에서 표시·애니메이션으로 볼 수 있다(12). 레이어 선택 원문은 `*Primary Group: Water Column*` (12); `*Parameter: Salinity*` (12)이다. 그림 1은 이 두 선택 필드와 `Options: Depth Average`를 보여 준다(14). 배경의 색 범례는 염분이 아니라 `Bottom Elevation (m)`이며 `-19.060`부터 `0.923`까지이다(14). |
| 16–21 | 2DV View — 2차원 수직 보기(2DV View)의 단면 위치를 정의한다(18). 위치 추출 조건 원문: `It is possible to select a value of I to extract the active J cells along that I, or select a value of J to extract the active I cells along that J or using a "Drape Line", which is a polyline in the same coordinate system as the LX, LY data.` (18). 매개변수 추가·제거, 배치 저장·불러오기, 순서 변경, Update와 Properties의 기능을 설명한다(18). 원문 예시 인덱스는 `I = 25` (18)이다. 20행의 첫 그림은 `Use I`, `Specify I: 25`를 선택한 추출 폼이고 두 번째 그림은 자동 색 범위·등치선(contour)·범례 정밀도 설정이다. 두 번째 그림은 `Automatic Range`가 선택되며 비활성 범위 칸 `Min. Value: 0.0000`, `Max. Value: 1.0000`, `Legend Precision: F2`를 표시한다(20). 세 번째 그림의 단면은 `Col: I = 25, Time: 2008-01-01 00:00` (20행 그림)이다. 가로축은 `Distance (m): 500, 1650, 2800, 3950, 5100, 6250, 7400, 8550, 9700, 10850, 12000` (20행 그림)이고 세로축은 `Elevation (m): 0.00, -2.50, -5.00, -7.50, -10.00, -12.50, -15.00, -17.50` (20행 그림)이다. 염분 색 범례는 `Salinity (ppt): 6.05–32.95` (20행 그림)이다. 왼쪽의 붉은 고염분 영역에서 오른쪽의 파란 저염분 영역으로 이어지는 층별 격자를 보여 준다(20). |
| 22–27 | Time Series — 시계열(time series) 아이콘은 붉은·파란 곡선 그림이다(24). 셀 하나 또는 여러 셀을 선택하고 L 인덱스를 입력하면 I·J가 자동으로 채워진다(24). 시간 조건 원문: `note that the start and stop days should be within the model's start and end date` (24). 26행의 첫 그림은 추출 폼이며 `L: 182; I: 28; J: 15` (26행 그림); `Start (day): 0.000000; Stop (day): 10.000002` (26행 그림); `Salinity (Depth Avg.)`를 표시한다. 두 번째 그림의 붉은 곡선 범례는 `Cell: 182 (I:28, J:15), Salinity (Depth Avg.)`이다(26). 가로축은 `Time (days): 0, 2, 4, 6, 8, 10` (26행 그림)이고 세로축은 `Salinity (ppt): 29.50, 29.75, 30.00, 30.25, 30.50, 30.75, 31.00, 31.25, 31.50, 31.75, 32.00, 32.25, 32.50, 32.75, 33.00, 33.25` (26행 그림)이다. 곡선은 초기 구간의 큰 하강·회복을 반복한 뒤 후반에 더 작은 변화로 이어진다(26). 그래프의 점별 수치 표는 없다(26). |
| 28–33 | Vertical Profiles — 수직 프로파일(vertical profiles) 아이콘은 축 옆의 파란 층 모양이다(30). 단일·복수 셀과 염분을 선택하고 외부 파일을 가져와 모의 결과와 비교할 수 있다(30). 32행의 첫 그림은 `L: 659; I: 28; J: 47` (32행 그림)를 표시한 추출 폼이다. 두 번째 그림의 제목은 `EFDC_DSI Testing, Cook Inlet Model`이고 범례는 `Cell: 1326 (I:15, J:40) Salinity` (32행 그림)이며 시각은 `2003-04-01 00:00`이다. 가로축은 `Salinity (ppt): 22.4835, 22.4860, 22.4884, 22.4909, 22.4933, 22.4958, 22.4982, 22.5007, 22.5031, 22.5056, 22.5080` (32행 그림)이고 세로축은 `Elevation (m): -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00, 1.25` (32행 그림)이다. 붉은 선은 오른쪽 위로 증가하는 프로파일이다(32). |
| 34–40 | Longitudinal Profiles — 종방향 프로파일(longitudinal profiles) 아이콘은 가로 방향의 붉은·파란 곡선이다(36). drape 파일 또는 I·J 인덱스로 단면을 정의하고 표시 매개변수를 정한다(36). 본문은 염분과 저면고를 함께 표시하는 예시라고 적으며 인덱스 원문은 `I=56` (36)이다. 38행의 독립된 마침표와 빈 줄을 포함한다(37–39). 40행의 첫 그림은 `Specify I: 56`, `Salinity (Depth Avg.)` 추출 폼이다. 두 번째 그림은 시각 `2008-01-10 01:00`의 깊이 평균(depth average) 염분 붉은 선이다(40). 가로축은 `Distance (m): 0, 153, 306, 459, 612, 765, 917, 1070, 1223, 1376, 1529` (40행 그림)이고 세로축은 `Salinity (ppt): 26.13, 26.25, 26.38, 26.50, 26.63, 26.75, 26.88, 27.00, 27.13, 27.25` (40행 그림)이다. 범례는 `Col: I = 56`과 `Salinity (Depth Avg.)`만 표시한다(40). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 절 제목 앞에 CSS 선택자와 색상 선언이 남아 있다.
- 32행 그림: 추출 폼의 셀은 L 659, I 28, J 47이다. 그래프 범례의 셀은 L 1326, I 15, J 40이다.
- 36행·40행 그림: 본문은 염분과 저면고를 함께 표시한 예시라고 적는다. 그래프의 축과 범례는 염분만 표시한다.
