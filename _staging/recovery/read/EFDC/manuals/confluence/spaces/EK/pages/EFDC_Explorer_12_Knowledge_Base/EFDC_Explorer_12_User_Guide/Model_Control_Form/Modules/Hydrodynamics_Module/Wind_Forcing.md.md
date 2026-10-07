---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Hydrodynamics_Module/Wind_Forcing.md
lines: 79
sha256: e4b5f485bfb68d4152b41027e3c862ccbd916a61f29fadd9e955d1e854b1b844
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Wind_Forcing.md — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Wind Forcing / 메타데이터 — 페이지 식별자 `243630239` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–13 | Wind Forcing / 진입 — Hydrodynamics 아래 바람 강제력(wind forcing) 메뉴에서 `WSER.INP` (10)를 생성·편집한다. 바람 차폐계수(wind sheltering coefficient)는 Sheltering 또는 2DH View로 지정한다(10). 시계열이 둘 이상이면 Series Weighting으로 바람장 배정을 해야 한다(10). 로컬 `9-16-2021_8-51-48_AM.png`를 열었다(12). 화면은 시계열 수, Wind Speed·Wind Shelter, Tropical Cyclone·Surface Drag와 Sheltering 선택을 보여 준다. |
| 14–24 | Wind Series / 항력·좌표 — 복수 바람·대기·얼음 지점을 지원한다(16). 항력 옵션 원문은 `Original, Original Relative U/V, Hersbach 2011 (ECMW)`, `COARE3.6 Simplified` (16)이다. Original Relative U/V는 원래 EFDC 방식에 수면 유속을 반영한다(16). 로컬 `Wind_data.jpg`를 열었다(18). 화면은 바람 시계열 수 3, Original Rel U/V, 바이너리(binary) 바람장 선택을 보여 준다. `X and Y coordinates` (20)가 있으면 표시용으로 우선 사용하고, 없으면 `lat/long values` (20)로부터 계산한다. 로컬 `2019-05-02_2-28-13_PM.jpg`를 열었다(22). FORT MCMURRAY 매개변수 표는 `Longitude (deg.): -111.22`; `Latitude (deg.): 56.65`; `X (m): 486510`; `Y (m): 6278448`; `Time Scale (sec.): 86400`; `Time Offset (sec.): 0`; `Anemometer Height (m): 5`; `Factor for Speed Conversion to m/s: 1`; `Wind Direction Option: 0`이다(22, 그림). |
| 25–41 | Series Weighting / 품질·파일 — 시간 블록별 품질 지수(quality index)로 여러 지점을 가중한다(27). 예시 지점은 `WSER\_1, WSER\_2, and WSER\_3`이며 `six-time series` (29)이다. 로컬 `2019-05-15_5-33-36_PM.jpg`를 열었다(31). 하천 격자의 WSER_1 바람 가중 범례는 `0.532`–`1.000`, 시각은 `2003-01-01 00:00`, 시간 블록은 `2921-2922`이다(31, 그림). WSER_1·2·3 지점 위치가 표시되어 있다. 로컬 `2019-05-02_3-23-41_PM.jpg`를 열었다(34). Station Quality Index 표의 `(From,To,WSER_1,WSER_2,WSER_3)` 표시값은 `(2922,2922.00,1,0,0); (2921,2922.00,1,1,0); (2922,2924.04,1,1,1); (2924.037,3276.33,0.9,1,1); (3276.328,3368.79,0.9,1,0)`이다(34, 그림). Station Location 표의 `(StationID,Start,End,Easting,Northing)`은 `(WSER_1,2920.04,3655.00,401871,2936431); (WSER_2,2921.00,3368.79,440158,2920122); (WSER_3,2922.00,3276.33,450305,2964382)`이다. `Inverse Distance Power: 2`, `Number of Maps: 6`을 표시한다(34, 그림). 기본 품질 지수는 `the maximum value of one for the defaults, which is 1.` (38)이고 입력 범위는 `0 to 1` (38)이다. 문제를 모르면 1, 품질이 낮으면 더 낮은 값을 부여한다(38). `WNDMAP.INP` (40)는 유효 Julian day 구간 뒤 셀 `I, J, and weighting for each time series` (40)를 쓴다. GVC 헤더 조건은 `six comment lines only` (40)이다. 파일 대응 원문은 `ASER.INP`, `ISER.INP`, `ATMMAP.INP`, `ICEMAP.INP` (40)이다. |
| 42–65 | Weighting / 누락된 식·기호 — 지도는 셀·지점 거리의 역제곱과 각 시계열의 정성 계수를 기반으로 한다(42). 각 블록의 첫 행은 시작·끝 시각과 정성 계수, 나머지는 실제 가중계수이다. 행 수·범위 원문은 `LA-1 data rows (L=2, LA)` (42)이다. 식 자리는 `LaTeX Math Block` (44·46·48)이다. 기호 정의 원문: `N: the total number of time series (N the number of stations) where MASER represents in ASER.INP, WSER.INP, and ISER.INP,` (52); `XS(n), YS(n): UTM coordinates of one station to get time series,` (54); `XC(L), YC(L): UTM coordinates of the cell L,` (56); `L: index of a cell,` (58); `αn: qualitative coefficient of each time series` (60). 셀별 매 시간 단계 평균값 `V(L)` (62)을 계산한다는 설명 뒤 식도 `LaTeX Math Block` (64)이다. 빈 줄·Where를 포함한다. |
| 66–79 | Wind Rose Plotting — 바람 장미도(wind rose)의 시작·끝 시각을 입력하여 표시한다(68). 로컬 `2019-05-02_3-26-03_PM.jpg`를 열었다(70). 자료 표의 `(Time (days),Speed (m/s),Direction (deg.))` 완전히 보이는 행은 `(2920.037000,1.544,240.0); (2920.120000,2.059,280.0); (2920.287000,2.059,290.0); (2920.412000,3.603,270.0); (2920.453000,2.574,310.0); (2920.495000,4.118,310.0); (2920.537000,3.089,310.0); (2920.578000,4.633,300.0); (2920.620000,4.118,290.0); (2920.662000,5.148,290.0)`이다(70, 그림). 다음 행은 화면 아래에서 일부 잘려 있다. 로컬 `2019-05-02_3-26-52_PM.jpg`를 열었다(73). WSER_1 장미도 기간은 `From 2002-12-30 to 2005-01-02`, `19412 records used.`, `Direction is coming from.`, `Calm 0.01%`이다(73, 그림). N은 위, E는 오른쪽, S는 아래, W는 왼쪽이며 NW·NE·SW·SE를 표시한다. 반지름은 빈도이며 보이는 눈금은 `10%, 15%, 20%, 25%`이다. 풍속 범례 구간은 `20.8 - 24.5 m/s`; `17.2 - 20.8 m/s`; `13.9 - 17.2 m/s`; `10.8 - 13.9 m/s`; `8.0 - 10.8 m/s`; `5.5 - 8.0 m/s`; `3.3 - 5.5 m/s`; `1.5 - 3.3 m/s`; `0.5 - 1.5 m/s`이다(73, 그림). E 방향 막대가 가장 길다. 메타파일(metafile)·비트맵(bitmap) 내보내기와 설정을 설명한다(76). 로컬 `2019-05-02_3-34-13_PM.jpg`를 열었다(78). 화면은 제목·범례·단위·기간·선 모양 설정을 보여 준다. 빈 줄과 Figure 6–8 캡션을 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 44·46·48·64: 네 식 자리에는 `LaTeX Math Block`만 있고 수식 본문이 없다.
- 29·52: 예시는 세 지점과 여섯 시계열을 구분하지만 N 정의는 시계열 총수와 지점 수를 함께 적는다.
- 38: 품질 지수 표 설명은 `[Figure 4](#Figure)`를 가리킨다. 해당 표의 캡션은 36행의 Figure 5이다.
- 10·16: Figure 1·2를 참조하지만 이 Markdown 파일에는 해당 번호 캡션이 없다.

