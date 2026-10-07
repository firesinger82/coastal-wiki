---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Hydrodynamic_Modeling/Build_a_3D_Coastal_Model_Level_2_Step-by-Step_Guidance/Harmonic_Boundary_Series.md
lines: 55
sha256: 5aad307ff1a825ffa25487bd65016803882c9ffd55b62639224075e7641336fa
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Harmonic_Boundary_Series.md — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 문서 메타데이터(metadata)는 ID `232751289` (2), 제목(3), space `EHG` (4), URL(5), version `9` (6), 갱신 시각(7), 경로(8)를 담는다. 10행의 CSS 뒤에 Tra Khuc 하구의 조석 분조(harmonic constituent) 예제 표라는 안내가 이어진다. 빈 줄(11)을 포함한다. |
| 12–13 | 표의 원문 열 이름·단위는 `Name`, `Speed(deg/hr)`, `Amplitude (m)`, `Phase (s)` (12)이다. 구분 행(13)을 포함한다. 속도(speed), 진폭(amplitude), 위상(phase)이라는 이름을 문서 표기대로 기록한다. |
| 14–14 | 분조 `Q1`; `Speed(deg/hr) = 13.3987`; `Amplitude (m) = 0.04`; `Phase (s) = 126.073` (14). |
| 15–15 | 분조 `O1`; `Speed(deg/hr) = 13.943`; `Amplitude (m) = 0.261`; `Phase (s) = 146.432` (15). |
| 16–16 | 분조 `P1`; `Speed(deg/hr) = 14.9589`; `Amplitude (m) = 0.097`; `Phase (s) = 182.577` (16). |
| 17–17 | 분조 `K1`; `Speed(deg/hr) = 15.0411`; `Amplitude (m) = 0.293`; `Phase (s) = 185.991` (17). |
| 18–18 | 분조 `N2`; `Speed(deg/hr) = 28.4397`; `Amplitude (m) = 0.04`; `Phase (s) = 59.376` (18). |
| 19–19 | 분조 `M2`; `Speed(deg/hr) = 28.9841`; `Amplitude (m) = 0.185`; `Phase (s) = 75.861` (19). |
| 20–20 | 분조 `S2`; `Speed(deg/hr) = 30`; `Amplitude (m) = 0.072`; `Phase (s) = 114.865` (20). |
| 21–22 | 분조 `K2`; `Speed(deg/hr) = 30.0821`; `Amplitude (m) = 0.025`; `Phase (s) = 95.187` (21). 빈 줄(22)을 포함한다. |
| 23–41 | EE10에서 분조를 개방 경계(open boundary)에 쓰는 절차이다(23). External Forcing Data의 Harmonic Tides에 새 계열을 만든다(25, 29). 계열 이름은 `3. Enter the name in *Current Series,*as "Tides"` (31)이다. 분조 수는 `4. Select *Change* to add the harmonic constituents*,*in this case, there are 8.` (33)이며 검색·추가 조건은 `5. Enter the name of harmonic constituents (Q1, O1,...) in the *Search* box and select *Search and add Harmonic Constituent*` (37)이다. `all 8 harmonic constituents`를 추가했을 때 OK를 누르도록 한다(39). 그림(27)은 External Forcing Data의 Harmonic Tides를 오른쪽 클릭하여 Add New Data Series를 여는 화면이다. 보고서 값은 `Number of Tidal Constituents: 0`, `Number of Harmonic Series: 0`이다(27).<br>Harmonic Forcings 창은 `Forcings Type: Constant Forcings`, `Current Series: Tides`, 현재 번호 `1`, `Number of Tidal Constituents: 0`, `Number of Series: 1`을 보여 준다(35). 빈 표의 열은 `ID`, `Name`, `Speed (deg/hr)`, `Amp1 (m)`, `Pha1 (sec.)`이다(35). Add New와 Change 버튼이 붉은 테두리로 표시된다.<br>Harmonic Constituents 창은 `View Constituents By: Speed (deg/hour)`, `Forcing Type: Constant Forcings`, `Number of Constituents: 8`, `Search: K2`이다(41). 선택된 표의 열 `ID / Name / Speed`와 행은 `24 / Q1 / 13.398661`; `28 / O1 / 13.943036`; `40 / P1 / 14.958931`; `43 / K1 / 15.041069`; `80 / N2 / 28.439730`; `92 / M2 / 28.984104`; `108 / S2 / 30.000000`; `111 / K2 / 30.082137`이다(41). Available Harmonic Constituents 표의 같은 열 순서에서 보이는 행은 `111 / K2 / 30.082137`; `112 / MSNU2 / 30.471521`; `113 / MSN2 / 30.544375`; `114 / ZETA2 / 30.553658`; `115 / ETA2 / 30.626512`; `116 / KJ2 / 30.626512`; `117 / MKN2 / 30.626512`; `118 / 2KM(S... / 30.708649`; `119 / 2SM2 / 31.015896`; `120 / SKM2 / 31.098033`; `121 / 2MS2N... / 31.088749`; `122 / 2SNU2 / 31.487417`; `123 / 2SN2 / 31.560270`; `124 / SKN2 / 31.642408`; `125 / MQ3 / 43.382765`이다(41). ID 118과 121의 이름은 화면에서 잘려 있다. 가운데의 오른쪽·왼쪽·이중 왼쪽 화살표는 두 목록 사이의 이동 버튼이다. |
| 42–50 | 표의 진폭·위상을 입력창으로 복사한다(43). Plot으로 시계열을 확인하고 OK로 끝낸다(45, 47). 49행에는 두 그림이 연이어 있다. 입력 완료 그림의 `Forcings Type: Constant Forcings`, `Current Series: Harmonic Series 1`, 현재 번호 `1`, `Number of Tidal Constituents: 8`, `Number of Series: 1`을 보여 준다(49). 표의 열 순서는 `ID / Name / Speed (deg/hr) / Amp1 (m) / Pha1 (sec.)`이다. 행은 `24 / Q1 / 13.398661 / 0.040 / 126.073`; `28 / O1 / 13.943036 / 0.261 / 146.432`; `40 / P1 / 14.958931 / 0.097 / 182.577`; `43 / K1 / 15.041069 / 0.293 / 185.991`; `80 / N2 / 28.439730 / 0.040 / 59.376`; `92 / M2 / 28.984104 / 0.185 / 75.861`; `108 / S2 / 30.000000 / 0.072 / 114.865`; `111 / K2 / 30.082137 / 0.025 / 95.187`이다(49). Amp1과 Pha1 열 및 Plot 버튼이 붉은 테두리로 표시된다.<br>조위 그래프의 제목은 `New EFDC Model / Head Type Boundary`, 빨간 선 범례는 `Harmonic Series 1`이다(49). 가로축 `Time (days)`의 표시 범위는 `0.0`–`30.0`이며 눈금은 `0.0`, `3.0`, `6.0`, `9.0`, `12.0`, `15.0`, `18.0`, `21.0`, `24.0`, `27.0`, `30.0`이다(49). 세로축 `Water Elevation (m)`의 보이는 눈금은 위에서부터 `0.9`, `0.8`, `0.6`, `0.5`, `0.4`, `0.3`, `0.1`, `0.0`, `-0.1`, `-0.3`, `-0.4`, `-0.5`이다(49). 빨간 곡선의 주기 진동과 진폭 변화가 보인다. 약 18–19일의 첨두는 약 0.84 m이고 약 19일의 저점은 약 -0.49 m이다(49, 그림 눈금에 따른 근삿값). |
| 51–55 | Assign Tidal Boundary. 경계 셀 선택은 3D 연안 모델의 4.3.2절을 참조한다(53). 조석 적용 선택 조건의 원문은 `To assign these tides to the open boundary cells, steps are introduced in section 4.3.2 ([Build a 3D Coastal Model (Level 2 Step-by-Step Guidance](/wiki/spaces/EHG/pages/225870269/Build+a+3D+Coastal+Model+Level+2+Step-by-Step+Guidance)). However, instead of choosing tidal series for *Pressure*, the user selects the series for *Harmonic*as shown in [Figure 6](https://eemodelingsystem.atlassian.net/wiki/spaces/EHG/pages/232751289#HarmonicBoundarySeries-Figure6).` (53)이다. Open Boundary Conditions 그림은 `Number of Open Boundary Groups: 2`, `Number of Water Level Series: 1`, `Number of Harmonic Series:` 공란, `Boundary Group: 2`, `Group Name: 23`, `Open Face: East`, `Type of Open Boundary: Elevation Specified`, `Number of Time Steps for Smooth Transition: 0`이다(55). `Forcing Approach`의 `Constant`와 `Time Varying`은 모두 선택되어 있다(55). `Number of Cells: 42`, `Current Cell: 1`, `L: 181`, `I: 89`, `J: 12`, `Initial WSEL: -0.021`, `Depth: 14.264`, `Bottom: -14.285`, `Level Data: None`, `Harmonic Data: Tides`, `Series 2:` 공란·비활성, `Tangential Factor: 0`이다(55). 농도 표 `Constituent / Bottom / Surface`와 `Constituent / Data Series`는 빈 표이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행의 설명 문장 앞에 CSS 문자열이 본문으로 남아 있다.
- 31행과 35행의 계열 이름은 `Tides`이다. 49행 입력창과 그래프 범례의 이름은 `Harmonic Series 1`이다. 55행의 Harmonic Data는 `Tides`이다.
- 45행의 `#Figure5`와 53행 링크의 `#HarmonicBoundarySeries-Figure6` 대상 anchor 선언은 본문에 없다.
- 53행은 조위 시계열 선택 항목을 `Pressure`, 분조 계열 선택 항목을 `Harmonic`이라고 부른다. 55행 그림의 해당 입력 칸은 `Level Data`와 `Harmonic Data`이다.
- 55행 그림은 `Harmonic Data: Tides`를 표시한다. 같은 그림의 `Number of Harmonic Series`는 공란이다.
