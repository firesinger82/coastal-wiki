---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DV_View/2DV_View_Setting.md
lines: 76
sha256: 8d05317615a5e3ae988fe43411aaa7d44271abf2e8e6ba2d6bf445e6901ae3d2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# 2DV_View_Setting.md — 판독 구간 기록

구간은 1행부터 76행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–25 | 2DV View Setting / 범례 위치별 메뉴 — 셀 왼쪽 클릭은 노란 정보 상자를 표시하며 축·제목·범례 오른쪽 클릭은 편집 기능을 연다(10). 범례 위쪽 오른쪽 클릭은 2DV View Setting, 아래쪽 오른쪽 클릭은 현재 변수의 Properties·Edit를 연다(12–20). Properties는 2DV View Properties, Edit는 Data Extraction for 2DV View로 연결한다고 적는다(20). 그림 1·2를 직접 열었다(16·22). 두 단면의 X축은 `Distance (m)`, `200`부터 `620`까지 `42` 간격이고 Y축은 `Elevation (m)`, `-1.00`부터 `2.00`까지 `0.30` 간격이다. 범례는 `Col: I = 10, Time: 2018-01-01 00:00`, `Salinity (ppt)`, 범위 `0.497`부터 `0.689`이다. 그림 1은 제목·범례 글꼴 설정 창을 겹쳐 표시하고 그림 2는 Properties for 'Salinity'·Edit 'Salinity' 메뉴를 보여 준다. |
| 26–45 | Properties / General Information — Properties를 선택하면 Layer Properties 창을 연다(28). 그림 3을 직접 열었다(30–32). 실제 창 제목은 2DV View Properties이며 Salinity 레이어의 표시·격자·범례·색상·등치선 설정을 보여 준다. 필드 원문과 동작은 `Layer Name`이 기본 이름을 표시하고 편집 가능(38), `Layer Visible`이 체크 시 2DH View에 레이어를 표시하고 전구 전환과 같은 효과(40), `Show Grid`가 격자 표시(42), `Show in Legend`가 범례 표시(44)이다. 격자 스타일 조건 원문: `If it is checked, the Grid Line Options are enabled for styling the grid.` (42). 그림의 격자 선 설정은 `Style: Solid`, 회색 `Color`, `Width: 1.0`이다(30행 그림). |
| 46–55 | Color Ramp Settings / 자동 범위·정밀도 — `Automatic Range` 조건 원문: `Checking this box causes EE to use the minimum and maximum values from the model, and disables the fields of *Min. Value* and *Max. Value*` (48). `Auto-Scale with View`는 체크 시 현재 표시 영역에서 최소·최대값을 가져오며 이동·확대·축소 때 범례 값을 갱신한다(50). `Min. Value`, `Max. Value` 편집 조건 원문: `The user can enter values for these fields unless the *Automatic Range*is unchecked.` (52). `Legend Precision` 기본값 원문: `As default, EE sets F2 for this field.` (54). 두 번 클릭하여 Number Format에서 `Decimal Digits`를 바꾼다(54). 예시 원문은 `0 - integer number, 1 - one decimal digit, 2 - two decimal digits, etc.,`이다(54). 그림 3의 예시 값은 `Min. Value: 32.28`, `Max. Value: 33.45`, `Legend Precision: F2`이며 Automatic Range는 체크, Auto-Scale with View는 해제되어 있다(30행 그림). |
| 56–65 | Color Options / 색상표 — `Reverse`는 색상표(color ramp) 표시를 반전한다(58). `Color Ramp` 목록으로 색상표를 고르며 Viridis·Plasma를 특정 자료 유형 표현과 선형 채도·명도 변화 및 색각 접근성을 위한 옵션이라고 설명한다(60). 그림 4를 직접 열었다(62–64). 보이는 옵션 이름 원문은 `Default`, `Jet`, `PBGYR`, `Rainbow`, `Rainbow-Soft`, `Parula`, `Magma`, `Inferno`, `Plasma`, `Viridis`, `HSV`, `Angular`, `Direction`, `Blue-White-Red`, `Ocean`, `Earth Relief`, `Topographic`, `NRWC`, `Gray Color`, `Black-White`, `Black-Gray-White`, `Wet/Dry`, `Salinity`, `Temperature`, `Oxygen`, `Chlorophyll`, `Turbidity`, `Density`, `Earth`, `Bathymetry`이다(62행 그림). 각 이름 왼쪽에 해당 색상 띠를 보여 준다. |
| 66–76 | Contour Options / Number Format — `Show Contours` 조건 원문: `Check on this box to show the value contours of the layer. If it is checked, the *Settings* and *Export* options will be enabled.` (68). Settings는 등치선 설정, Export는 등치선 파일 출력이다(70·72). 그림 5를 직접 열었다(74–76). Number Format 창은 `Format Type: Number`, `Decimal Digits: 2`, `Exponent Length: 1`, `Format Pattern: F2`를 보여 주며 Automatic은 체크 해제되어 있다(74행 그림). 이 값은 화면 예시 값이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 48·52: 48행은 Automatic Range를 체크하면 Min. Value·Max. Value 입력란이 비활성화된다고 적는다. 52행은 Automatic Range가 체크 해제된 경우를 제외하고 값을 입력할 수 있다고 적는다.
- 40: 2DV View Setting 문서의 Layer Visible 설명이 표시 대상을 `2DH View`라고 적는다.
- 54·64·76: 54행의 Number Format 설명은 다른 페이지의 `Bottom+Elevation+Layer+-+RMC+options#Figure4`를 가리킨다. 이 파일의 Figure 4는 Color Ramp options이며 Number Format 그림의 캡션은 Figure 5이다.
- 28: `#Figure-3` 링크가 있지만 이 Markdown 파일에는 해당 앵커 정의가 없다.

