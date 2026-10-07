---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Hydrodynamics_Module/Vegetation.md
lines: 71
sha256: a43e948eaffa14222bd77c0c48e433ecb627cdb7f51b2b8ae5c3e62c1b0fd3d7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Vegetation.md — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Vegetation / 메타데이터 — 페이지 식별자 `243532236` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–23 | Vegetation Options — 식생(vegetation) 저항과 진단 기능을 소개한다(10). 세 선택 원문은 `Do not use vegetation` (18); `Use vegetation with implicit momentum adjustment: implement vegetation resistance` (19); `Use vegetation with explicit momentum sink: implement with diagnostics to file CBOT.LOG` (20)이다. 로컬 `vegetation.png`, `vegetation_options.png`를 열었다(12·22). 첫 화면은 암시적 운동량 조정 선택과 Number of Classes, Include Laminar Flow, 시간·공간 가변 식생 입력을 보여 준다. 둘째 화면은 세 가지 Options를 펼쳐 보여 준다. 절 제목·빈 줄을 포함한다. |
| 24–36 | Number of Classes / 속성 — Modify로 클래스 폼을 열고 `Number of Classes`에 `(e.g., 4)` (28)를 입력하면 ID 1–4의 열을 만든다. 속성 원문 범위는 `Description`–`Drag Coeff Factor` (28)이다. 로컬 `Veg3.png`를 열었다(30). 표의 원문 행·값은 `ID: 1, 2, 3, 4`; `Description: Z1, Z2, Z3, Z4`; `Plant Density (#/m^2): 5, 10, 15, 20`; `Stem Diameter (m): 0.2, 0.5, 0.5, 0.5`; `Stem Height (m): 0.5, 1, 0.5, 2`; `Alpha (depth factor): 0.7854, 0.7854, 0.7854, 0.7854`; `Drag Coeff Factor: 0.3, 0.5, 0.7, 1`이다(30, 그림). `Load Existing VEGE.INP`, `VEGE.INP` (34)로 기존 파일을 가져오며 `Export VEGE.INP`, `#analysis`와 `as default` (35)로 기본 내보내기 위치를 설명한다. 빈 줄과 목록을 포함한다. |
| 37–53 | Apply Overlay / 구역 배정 — Grid Options는 `All grid cells` (41) 또는 `Only grid cells inside polygons` (42)이다. `Default Class: the first class is always displayed in the box` (45)이므로 사용자가 적용 클래스를 골라야 한다. 각 클래스 1–4를 각 구역 1–4에 배정하는 예를 설명한다(47). 폴리곤 예시 파일은 `Zone 1.p2d` (47)이다. 49행의 로컬 `10-23-2020_3-12-42_PM.png`, `10-21-2020_10-48-48_AM.png`, `10-23-2020_2-56-26_PM.png`를 각각 열었다. 첫 그림은 굽은 하천에서 오른쪽 부채꼴 영역으로 이어지는 곡선 격자와 초록 구역 경계를 보여 준다. 표지 Zone 1은 위쪽 가는 하천 띠, Zone 3은 하천 아래쪽 넓은 띠, Zone 2는 부채꼴 안쪽 띠, Zone 4는 바깥 부채꼴이다(49, 첫 그림). 다른 두 화면은 Zone 1.p2d에 Default Class 1을 배정하고 2DH View에 Vegetation Class를 추가하는 절차를 보여 준다(49). 로컬 `10-23-2020_11-50-41_AM.png`를 열었다(51). 같은 격자에 네 클래스를 파랑·초록·노랑·빨강으로 표시한다. 범례는 `1`–`4 Vegetation Class`, 시각은 `2018-01-01 00:00 (output not available)`이다(51, 그림). |
| 54–67 | Using Polygons to Set the Vegetation Map — 많은 종류를 배정할 때 다중 폴리곤의 shapefile 또는 P2D 파일을 사용한다(56). 조건 원문은 `the *Description* must match the ID in the shape file or in the P2D.` (56)이다. 파일·설정 원문은 `\*.p2d`, `\*.shp`, `Description`, `Z1, Z2, etc` (56); `Only grid cells inside polygons` (58); `Zone1-4.shp` (62); `Name`, `Description`, `ID Field` (66)이다. 폴리곤 내부 셀을 선택하고 Add File·Open 뒤 속성 ID Field로 Name을 골라 Apply Define Conditions로 배정한다(58–66). 빈 줄·순서 목록을 포함한다. |
| 68–71 | Shapefile 배정 그림 — 68행의 로컬 `Veg2.png`, `10-23-2020_3-53-09_PM.png`, `10-23-2020_4-01-25_PM.png`, `10-23-2020_4-02-08_PM.png`를 각각 열었다. Veg2 표는 30행 그림과 같은 클래스별 이름·밀도·줄기 지름·높이·Alpha·Drag Coeff Factor 값을 표시한다. 파일 열기 화면은 1–4 번호로 폴리곤 내부 셀·Add File·Zone 1-4.shp·Open 단계를 표시한다(68). 속성 표의 `(NAME, ATTR_, ELEVATION)`은 `(Z1,Polyline 1,0); (Z2,Polyline 2,0); (Z3,Polyline 1,0); (Z4,Polyline 1,0)`이며 LAYER 값은 화면에서 `Unclassified Line ...`으로 잘려 있다(68, 그림). `ID Field: NAME`, `Z Field: None`을 표시한다. 마지막 화면은 선택한 shapefile에 Apply Defined Conditions를 적용한다(68). 70행에서 `10-23-2020_11-50-41_AM.png`를 다시 열었다. 51행과 동일한 격자·클래스 1–4 범례·시각을 보여 준다. 빈 줄·Figure 12 캡션을 포함한다(69–71). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 26·28·37: Figure 3의 링크가 `#Figure2`를 가리킨다. 37행의 Figure 4·5, 47행의 Figure 6·7도 각각 번호보다 하나 작은 이름의 앵커를 가리킨다.
- 66: Figure 10 참조가 `[Figure 1](#Figure9)0`으로 분리되어 있다.
- 51·70: Figure 7과 Figure 12의 이미지 URL은 같은 로컬 파일을 가리킨다.

