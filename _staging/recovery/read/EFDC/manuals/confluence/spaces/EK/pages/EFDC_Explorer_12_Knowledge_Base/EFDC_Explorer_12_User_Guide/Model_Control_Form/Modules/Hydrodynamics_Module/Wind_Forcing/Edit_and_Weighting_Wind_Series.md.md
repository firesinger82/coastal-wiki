---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Hydrodynamics_Module/Wind_Forcing/Edit_and_Weighting_Wind_Series.md
lines: 54
sha256: 3fe7f40419f25cc093e9842fbaf24269d2f9219a8e6882e93c2bc152d5bd8231
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Edit_and_Weighting_Wind_Series.md — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Edit and Weighting Wind Series / 메타데이터 — 페이지 식별자 `2056093697` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–21 | Edit Wind Series / 좌표 — CSS 뒤에 복수 바람 시계열과 유연한 지점 가중을 소개한다(10). 로컬 `12.png`를 열었다(12). 화면은 Number of Series 3과 Edit·Weighting을 보여 준다. 시계열 추가·복사·삭제와 Parameters 탭을 설명한다(16). 좌표 우선 원문은 `if both are entered, it should be noted that EE will use the X and Y coordinates.` (16)이다. X/Y가 없으면 lat/long에서 자동 계산한다(16). 로컬 `14.png`를 열었다(18). 매개변수 표는 `Longitude (deg.): -81.9`; `Latitude (deg.): 26.5`; `X (m): -44740164.0`; `Y (m): 193014162.0`; `Time Scale (sec.): 86400.000`; `Time Offset (sec.): 0.0`; `Invalid Flag: -999`; `Anemometer Height (m): 10`; `Factor for Speed Conversion to m/s: 1.0`; `Wind Direction Option: 0`이다(18, 그림). 빈 줄·Figure 1·2 캡션을 포함한다. |
| 22–31 | Station Weighting / 품질·파일 — 품질 지수로 시계열과 시간 블록을 평가한다(22). 로컬 `13.png`를 열었다(24). 가중 표의 `(From,To,WSER_1,WSER_2,WSER_3)`은 `(2920.037109375,3654.995,1,1,1)`이며 `Number of Maps: 1`, `Inverse Distance Power: 2`이다(24, 그림). 지점 표의 `(StationID,Start,End,Easting,Northing,Longitude,Latitude)`는 `(WSER_1,2920.04,3655.00,-44740164,193014162,-81.9,26.5); (WSER_2,2920.04,3655.00,-45040120,203014178,-50,12); (WSER_3,2920.04,3655.00,-41740150,193015665,-80,30)`이다(24, 그림). 기본 품질 지수는 `the maximum value of one for the defaults, which is 1.` (28), 사용자 입력 범위는 `0 to 1` (28)이다. 품질이 높은 시계열이 모형에 더 큰 영향을 준다(28). 파일·헤더 원문은 `WNDMAP.INP`; `I, J, and weighting for each time series`; `six comment lines only`; `ASER.INP`; `ISER.INP`; `ATMMAP.INP`; `ICEMAP.INP` (30)이다. Julian day 유효 구간 뒤 셀별 시계열 가중을 기록한다(30). |
| 32–54 | Weighting coefficients / 누락된 식·기호 — 역제곱 거리·정성 계수로 지도 블록을 계산하며 첫 행은 시작·끝 시각과 정성 계수이다(32). 행 수·범위는 `LA-1 data rows (L=2, LA)` (32)이다. 식 자리 원문은 `LaTeX Math Block` (34·36·38)이다. 기호 정의 원문은 `N: the total number of time series (N the number of stations) where MASER represents in ASER.INP, WSER.INP, and ISER.INP,` (42); `XS(n), YS(n): UTM coordinates of one station to get time series,` (44); `XC(L), YC(L): UTM coordinates of the cell L,` (46); `L: index of a cell,` (48); `αn: qualitative coefficient of each time series` (50)이다. 셀별 매 시간 단계 평균값 `V(L)` (52)을 계산한다는 설명 뒤도 `LaTeX Math Block` (54)만 있다. 빈 줄·Where를 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 34·36·38·54: 네 식 자리에는 `LaTeX Math Block`만 있고 수식 본문이 없다.
- 16: Parameters 그림의 한 링크는 다른 페이지 draftId를 사용하는 `resumedraft.action?draftId=243630239#WindForcing-Figure2` 초안 URL이다.
- 42: N의 정의는 시계열 총수와 지점 수를 동시에 적는다.

