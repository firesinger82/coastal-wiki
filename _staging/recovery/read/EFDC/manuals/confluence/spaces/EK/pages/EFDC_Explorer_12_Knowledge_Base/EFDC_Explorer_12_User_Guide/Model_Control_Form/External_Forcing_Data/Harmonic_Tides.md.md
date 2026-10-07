---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/External_Forcing_Data/Harmonic_Tides.md
lines: 34
sha256: f2ad94e8ea4953b207f7bb441be93244370b27286dcb3ec586840af28c12d35c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Harmonic_Tides.md — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Harmonic Tides / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–16 | Harmonic Forcings / 조화 성분(harmonic component) 선택 선행 조건 — 값을 입력하거나 붙여넣기 전에 사전 정의한 조석 분조(tidal constituent) 234개에서 조합할 성분을 지정해야 한다(10). 의무와 수량의 원문: ``This option is different from other external forcing options in that before updating the form by typing or pasting values, the user must specify the forcing of an arbitrary number of combinations of harmonic components from 234 predefined tidal constituents.`` (10). ``*Add New*`` (12)로 새 시계열(time series)을 추가하고 편집을 활성화한다(12). ``*Change*`` (13)로 분조 수를 설정한다(13). 15행 `EE10_125.png`의 로컬 사본을 열었다. 빈 Harmonic Forcings 양식의 표 머리글은 `ID`, `Name`, `Speed (deg/hr)`, `Amp1 (m)`, `Pha1 (sec.)`이다. 화면 설정은 `Forcings Type: Constant Forcings`, `Current Series: Harmonic Series 1`, `Number of Tidal Constituents: 0`, `Number of Series: 1`이다(15행 그림). |
| 17–27 | Harmonic Constituents / 목록·검색·추가 — Change를 선택하면 사전 정의한 분조 234개의 표가 나타난다. 분조 하나 이상을 선택해서 추가한다(17). Shift·Ctrl과 LMC로 여러 분조를 선택한 후 오른쪽 화살표로 추가할 수 있다(19–23). 이름을 알면 ``*Search*`` (24) 상자에 입력하고 ``*Search and Add Harmonic Constituents*`` (24) 버튼으로 바로 추가할 수 있다(24). 21행 `148.png`는 오른쪽 방향의 추가 화살표 아이콘이다. 24행 `EE10_127.png`는 검색·추가 아이콘이다. 26행 `EE10_29.png`는 분조 선택 양식이다. 세 로컬 그림을 모두 열었다(21·24·26). 왼쪽 Available Harmonic Constituents 표에서 완전히 보이는 행을 `ID, Name, Speed` 순서로 옮긴다: ``111, K2, 30.082137``; ``112, MSNU2, 30.471521``; ``113, MSN2, 30.544375``; ``114, ZETA2, 30.553658``; ``115, ETA2, 30.626512``; ``116, KJ2, 30.626512``; ``117, MKN2, 30.626512``; ``118, 2KM(S..., 30.708649``; ``119, 2SM2, 31.015896``; ``120, SKM2, 31.098033``; ``121, 2MS2N..., 31.088749``; ``122, 2SNU2, 31.487417``; ``123, 2SN2, 31.560270``; ``124, SKN2, 31.642408``; ``125, MQ3, 42.382765`` (26행 그림). `2KM(S...`와 `2MS2N...`는 화면의 잘린 이름 표기다. 오른쪽 Station Specific Parameters 표는 선택한 8개 분조를 표시한다. 그 행을 `ID, Name, Speed` 순서로 옮긴다: ``24, Q1, 13.398661``; ``28, O1, 13.943036``; ``40, P1, 14.958931``; ``43, K1, 15.041069``; ``80, N2, 28.439730``; ``92, M2, 28.984104``; ``108, S2, 30.000000``; ``111, K2, 30.082137`` (26행 그림). 설정은 `View Constituents By: Speed (deg/hour)`, `Forcing Type: Constant Forcings`, `Number of Constituents: 8`, `Search: K2`다(26행 그림). |
| 28–34 | 정렬·Forcing Type / 위상(phase)과 진폭(amplitude) — 정렬 선택과 단위의 원문은 ``These constituents may be sorted either by angular speed (degrees/hours) or period (days, hours, minutes, seconds) with the drop-down list *View Constituents By.*`` (28)이다. Forcing Type은 constant, linear variation, quadratic variation 중에서 고른다. 일반적으로 constant forcing을 권장한다고 적는다(30). 원문 조건과 추가 수량은 ``In the *Forcing Type* frame the user has three options; constant, linear variation and quadratic variation. It is generally recommended to use a constant forcing. With the other two options the user must specify additional one or two amplitude and phase for each tidal constituent, respectively.`` (30)이다. linear variation은 각 분조에 진폭·위상 각각 하나를 추가로 지정해야 한다. quadratic variation은 각각 둘을 추가로 지정해야 한다(30). 분조 선택 후 위상·진폭을 입력한다. EFDC는 선택한 방법과 값으로 최종 적용 위상·진폭을 변경한다. Plot으로 조석 시계열을 볼 수 있다(32). 34행 `EE10_30.png`의 로컬 사본을 열었다. 표 머리글은 `ID`, `Name`, `Speed (deg/hr)`, `Amp1 (m)`, `Pha1 (sec.)`이며 값은 `ID, Name, Speed, Amp1, Pha1` 순서로 ``24, Q1, 13.398661, 0.040, 126.073``; ``28, O1, 13.943036, 0.261, 146.432``; ``40, P1, 14.958931, 0.097, 182.577``; ``43, K1, 15.041069, 0.293, 185.991``; ``80, N2, 28.439730, 0.040, 59.376``; ``92, M2, 28.984104, 0.185, 75.861``; ``108, S2, 30.000000, 0.072, 114.865``; ``111, K2, 30.082137, 0.025, 95.187``이다(34행 그림). 화면은 `Forcings Type: Constant Forcings`, `Number of Tidal Constituents: 8`을 표시한다. 진폭·위상 열과 Plot 버튼을 빨간 테두리로 강조한다(34행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 26행 그림: 왼쪽 표에서 ID 118과 121의 Name은 각각 `2KM(S...`, `2MS2N...`으로 잘려 있다. 완전한 이름은 이 화면에서 확인할 수 없다.
- 26행 그림: View Constituents By는 `Speed (deg/hour)`다. 왼쪽 표의 ID 120·121 Speed는 순서대로 `31.098033`, `31.088749`다.
