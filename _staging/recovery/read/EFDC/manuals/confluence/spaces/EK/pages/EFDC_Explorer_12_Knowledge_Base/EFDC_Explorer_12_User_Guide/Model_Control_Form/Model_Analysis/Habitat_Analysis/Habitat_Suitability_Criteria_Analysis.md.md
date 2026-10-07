---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Model_Analysis/Habitat_Analysis/Habitat_Suitability_Criteria_Analysis.md
lines: 93
sha256: 30fdb35d0136b80b577f98baa99ed4c1cd5717b458ab89ca014060a1302f0fb4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Habitat_Suitability_Criteria_Analysis.md — 판독 구간 기록

구간은 1행부터 93행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Habitat Suitability Criteria Analysis / 메타데이터 — 페이지 식별자 `274792449` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–36 | HSC·IFIM / 정의·누락된 식 — 서식지 적합성 기준(Habitat Suitability Criteria, HSC)의 생애단계별 평가, 하천유량 증분법(Instream Flow Incremental Method, IFIM), 물리적 서식지 모의 모형(Physical Habitat Simulation Model, PHABSIM)의 배경을 설명한다(10–14). PHABSIM의 수질 미모의와 2차원 제한을 적고 EEMS의 3차원·수질·퇴적물·독성물질 확장을 주장한다(14). 가중 이용가능 면적(weighted useable area, WUA)은 적합성 지수의 곱으로 계산한다고 적지만 식 자리는 `LaTeX Math Block` (18)이다. 기호 원문: `AL` (22), `is the area of the cell` (22); `CL` (24), `if not used or needed a value of 1.0 is used,` (24); `L` (26), `is the cell index` (26); `Si` (28), `is the habitat suitability index for parameter i for up to n parameters.` (28). 가중 이용가능 체적(weighted usable volume, WUV)의 식 자리도 `LaTeX Math Block` (32)이다. `VL` (36)은 `is the volume of the cell` (36)로 정의된다. 빈 줄과 Where 지시를 포함한다. |
| 37–44 | IFIM 설정 — 설정 파일 확장자는 `“.HSC”` (38)이다. `Criteria ID` (40)를 붙인 예시 파일은 `“HSC\_Results\_Chinook Salmon Spawning.dat”` (40)이다. 로컬 `9-4-2019_11-39-57_AM.jpg`를 열었다(42). 화면은 Water Depth·Velocity·Channel Index 적합성 곡선, Layer·Series 선택, IJ Channel Index 생성과 추출 기간을 보여 준다. 정의 가능한 매개변수의 원문 목록은 `bottom elevation, water depth, bed shear, channel index, velocity, fraction of light, cohesives, and TSS` (44)이다. IFIM 설정에서는 유입을 증분 또는 계단 형태로 적용한다(44). |
| 45–54 | Suitability Index Curves — 절 제목·빈 줄을 포함한다(45–47). 적합성 지수(Suitability Index, SI) 곡선은 생애단계별 성장·생존·생체량 정보를 이용한다고 설명한다(48). 범위·끝점은 `0.0 to 1.0 with 0.0 indicating unsuitable conditions and 1.0 optimal conditions` (48)이다. 입력 쌍은 `(parameter, suitability)` (50)이며 `These x, y values are comma delimited, with each pair then separated by a semi-colon.` (50)이다. 추출 전에는 층 범위·표시 Series 체크박스·시작·끝 날짜를 지정해야 한다(52). 로컬 `9-4-2019_11-40-53_AM.jpg`를 열었다(54). Velocity 편집 표의 `(X,Y)` 값은 `(0,0); (0.17,0); (0.2,0.1); (0.35,0.2); (0.69,1); (0.72,1); (1.14,0.5); (1.17,0.2); (1.52,0)`이다(54, 그림). 그래프는 이 점들을 파란 선으로 연결한다. x축 범위는 0–1.52, y축 범위는 0–1이다. 그림에 축 단위는 없다. |
| 55–70 | Channel Index / 생성·추출 — 절 제목·빈 줄을 포함한다(55–57). 수로 지수(channel index)는 셀별 하상 특성을 나타내며 임의 값을 허용한다(58). 일반 범위의 원문은 `0 to 1, or 0 to 100` (58)이다. 입력 파일 `Channel\_index\_interp.dat` (60)의 형식은 `“X, Y, Substrate Code”` (60)이며 `where X and Y should be in UTM.` (60)이다. 출력 확장자는 `.CI`, 형식은 `I, J, Channel Index` (60)이다. `Index`에 파일이 없으면 `assuming the index is 1.0 everywhere.` (62)로 처리한다. `Sub-Set` (62)은 폴리라인으로 영역 일부를 선택한다. 날짜 설정 후 추출하며 `#habitat` 폴더의 파일은 composite time, salinity, net weighted criteria, area, volume을 저장한다(64–66). 가중 기준 원문은 `weighted average 0 and 1 of all the cells that meet the bathymetry criteria` (66)이다. 로컬 `9-4-2019_11-52-14_AM.jpg`를 열었다(70). 그림은 후처리 선택 목록을 펼친 설정 화면이다. |
| 71–83 | Secondary Processing / 선택·그래프 — 선택 목록과 빈 줄을 포함한다(71–80). 원문 선택은 `WUA Time Series` (74); `WUA vs Q` (75); `HSC Time Series` (76); `WUV Time Series` (77); `Volume Time Series` (78); `Parameter Time Series` (79)이다. WUA vs Q에서는 적용하는 초기 경계조건에 맞는 시간·유량 곡선을 사용자가 반드시 만들고 `time versus flow (T vs Q) as x, y points` (75)를 입력한다. HSC 범위는 `0 to 1` (76)이며 전체 영역에 가중된다. Parameter Time Series는 `only one at a time may be selected` (79)이다. 이미 추출한 자료는 메모리 재사용 또는 재추출을 선택한다(81). 로컬 `Figure-2.jpg`를 열었다(83). 그래프 제목은 Skagit River, Reach 7 IFIM Study, 범례는 빨강 `WUA: Chinook Salmon Spawning`이다. x축 `Time (days)`는 0–20, y축 `Weighted Usable Area (m²)`는 0–35000이다. 곡선은 초기 약 33000에서 중간 약 3500으로 계단식 감소한 뒤 다시 약 33000으로 증가한다(83, 그림; 곡선값은 눈금에 따른 근삿값). |
| 84–93 | View Habitat Suitability Index in 2DH View — 절 제목·빈 줄을 포함한다(84–86). 시계열을 만든 뒤 평면 2차원 보기(2DH View)에서 `Ctrl + H` (87)로 Habitat Options를 열고 `Habitat Suitability Indices` (87), `\*.HSC` (87)를 선택한다. 로컬 `9-4-2019_1-29-48_PM.jpg`를 열었다(89). 화면은 HSC 파일 선택을 보여 준다. 로컬 `9-4-2019_1-34-13_PM.jpg`, `9-4-2019_1-34-34_PM.jpg`를 각각 열었다(93). 두 그림은 굽은 하천의 사각 셀 격자에 `Habitat Suitability (Water Depth)`를 초록색으로 표시한다. 범례는 `0.000`–`1.000`이며 시점은 각각 `Day: 0.0000`, `Day: 10.0000`이다(93, 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18·32: WUA와 WUV 식 자리에는 `LaTeX Math Block`만 있고 수식 본문이 없다.
- 48·50·54: 48행은 성장·생존·생체량을 y축, 적합성 지수를 x축으로 설명한다. 50행의 입력 순서는 `(parameter, suitability)`이다. 54행 Velocity 그림의 X값 범위는 0–1.52이고 Y값 범위는 0–1이다.
- 38·50·68·81·87·91: Figure 1–7을 참조하지만 이 Markdown 파일에는 번호 캡션이나 대응 앵커 선언이 없다.

