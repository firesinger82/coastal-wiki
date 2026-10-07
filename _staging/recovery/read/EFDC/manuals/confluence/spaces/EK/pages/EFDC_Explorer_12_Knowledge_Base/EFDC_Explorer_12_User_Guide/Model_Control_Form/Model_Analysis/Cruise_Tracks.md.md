---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Model_Analysis/Cruise_Tracks.md
lines: 33
sha256: 36d3429281036dddc3ff882b395d9cdb25f790df9e35d072178494806945b834
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Cruise_Tracks.md — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Cruise Tracks — 문서 식별자, 제목, space, URL, 판본, 갱신 시각과 문서 계층의 frontmatter(1–9). |
| 10–14 | Cruise Tracks — CSS 선언 뒤 영역 내 거리 방향의 연속 시료와 모델 출력 비교를 설명한다(10). 2DH View 또는 EE 외부에서 시료 횡단선(transect)에 대응하는 cruise line 다각형(polygon)을 만들며 EE가 선상의 자료를 추출·비교한다(10). Cruise Tracks를 오른쪽 클릭(RMC)해 설정한다(10). 빈 줄·그림·캡션을 포함한다(11–14). `5-13-2019_4-59-23_PM.jpg`을 열었다(12). Define Calibration Series에서 비교 양식으로 향하는 빨간 화살표가 있다. `# of Comps: 25`, `Time Tolerance (minutes): 5`, `Reload Model Output` 미체크, `Cruise Stations Location` 경로와 Error Statistics·Line Plots·Profile Plots를 보여 준다. 표 열은 `Name`, `Data Type`, `Date`, `Param`, `Data File`, `Use`이다. 보이는 14개 행의 Name·Param은 `Salinity: 1`; `Temp: 2`; `Dye: 3`; `Cohesives: 60`; `RPOrg C: 804`; `LPOrg C: 805`; `DOrg C: 806`; `RPOrg P: 807`; `LPOrg P: 808`; `DOrg P: 809`; `TPO4-P: 810`; `RPOrg N: 811`; `LPOrg N: 812`; `DOrg N: 813`이다. 모든 표시 행의 `Data Type`은 `2`, `Date`는 비어 있고 `Use`는 체크되어 있다. 긴 Data File 경로는 줄임표로 잘려 있다. |
| 15–24 | Station Information / 입력자료 형식 — 셀의 오른쪽 클릭으로 관측점(station) 양식을 열고 관측점 또는 경로(track) 자료와 cruise ID를 지정한다(15). 자료 유형·파일 조건 원문: `Right mouse click on the cells to obtain *Station Information* form to set the cruise plot data as shown in Figure 2. EE allows the use of two different kinds of cruise plot data. These are defined by station or by track. The user should define a cruise number ID for each data set. This ID will correspond to the USGS defined station IDs. If using native USGS data sets the user should select type 1 for the cruise data type. In this case the format is as shown in Figure 4. If using track data the data form should be as shown for type 2.` (15) `The data path should be set for text files that are tab delimited format required for the following parameter as explained above and shown in Figure 2. All the common parameter type codes are based on the list shown in Figure 3.` (17) 빈 줄·그림·캡션을 포함한다(16,18–24). `5-13-2019_5-03-48_PM.jpg`을 열었다(19). `ID: Salinity`, `X (m): 0.0`, `Y (m): 0.0`, `Filter: 0`, `Group: 0`, `Primary Group: Water Column`, `Parameter: Salinity`, `Options: Depth Average`와 Data File 경로 입력란을 보여 준다. `worddavd315989aa23a8f2eb19f67ca12d0aaa4.png`을 열었다(22). 그림은 매개변수 코드 목록 대신 Cruise Data Type과 자료 형식을 보여 준다. 유형은 `1 - By Station`, `2 - By Track`이다. 조건 문구는 `Note: If using By Station (1) user must enter the Date`이다. 첫 형식 제목은 `- Cruise Data By Track (1) Format`이며 예시 줄은 `StationID   Time     Parameter1     Parameter2 ....  ParameterN`, `value       value    value          value            value`, `value       value    value          value            value`, `...`이다. 둘째 제목은 `- Cruise Data By Track (2) Format`이며 예시 줄은 `Time        X        Y        Z        Parameter`, `value       value    value    value    value`, `value       value    value    value    value`, `...`이다. 그림에 단위·필드별 허용범위는 없다. |
| 25–33 | Cruise Tracks / 경로·연직 비교 예제 — 본문은 San Francisco Bay와 USGS 실측 염분(salinity) 예제로 설명한다(25). 색은 종단·연직 분포를 나타내며 빨강이 높고 파랑이 낮다(27). 왼쪽→오른쪽은 cruise line의 종단 변화이고 위→아래는 수면에서 저면까지의 연직 변화이다(27). 빈 줄·그림·캡션을 포함한다(26,28–33). `5-13-2019_5-13-42_PM.jpg`을 열었다(29). 그림은 구부러진 하천과 부채꼴 하구 격자, 청록색 경로 선과 빨간 원들을 보여 준다. 범례는 `2003-01-01 00:00`, `Cruise Tracks`, `Bottom Elevation (m)`이며 파랑 쪽 `-7.518`–빨강 쪽 `0.550`이다. `5-13-2019_5-18-14_PM.jpg`을 열었다(32). 그림 제목은 `Caloosahatchee TMDL, Water Quality Calibration - 2003: Salinity(ppt)`이다. 위 패널은 `Cruise Data`, 아래 패널은 `Cruise Model`이다. 두 가로축은 `Distance (m)`의 `0`–`50000`을 5000 간격으로 표시하고 세로축은 `Elevation (m)`의 `-7`–`1`을 1 간격으로 표시한다. 위 염분 색 눈금은 `0.25`, `4.39`, `8.54`, `12.68`, `16.83`, `20.97`, `25.11`, `29.26`이며 아래 색 눈금은 `0.00`, `3.87`, `7.73`, `11.60`, `15.47`, `19.33`, `23.20`, `27.06`이다. 두 패널은 상류 쪽 파랑과 하류 쪽 빨강을 보여 주고 모델 패널의 고염분은 연직으로도 분포가 달라진다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 15·29: 15행은 type 1 자료 형식을 Figure 4에서 볼 수 있다고 적는다. 29행의 Figure 4 그림은 2DH View 경로 지도이다.
- 17·22–23: 본문·캡션은 Figure 3을 공통 매개변수 유형 코드로 설명한다. 해당 그림은 Cruise Data Type과 입력자료 형식을 보여 준다.
- 22의 그림: 첫 목록은 `1 - By Station`이다. type 1 형식 제목은 `Cruise Data By Track (1) Format`이다.
- 25·32의 그림: 본문은 예제를 San Francisco Bay로 설명한다. 그림 제목은 Caloosahatchee TMDL이다.
