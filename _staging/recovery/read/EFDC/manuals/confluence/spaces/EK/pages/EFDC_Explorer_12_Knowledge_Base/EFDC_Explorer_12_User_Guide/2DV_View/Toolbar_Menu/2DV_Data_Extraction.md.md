---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DV_View/Toolbar_Menu/2DV_Data_Extraction.md
lines: 63
sha256: 7c39f2d08960facbf9118e9bf13564f8d4823c15797d3fcae35c99c23b2cb304
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# 2DV_Data_Extraction.md — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–19 | Data Extraction Constituents / 프로파일 위치 — 제목에 CSS 색상 마크업이 섞여 있다(10). Data Extraction은 프로파일 위치·변수를 정한다(12). `Primary Group`의 그룹 수는 모델에서 시뮬레이션한 모듈에 따라 달라지며 선택한 그룹의 변수 목록이 `Parameter`에 표시된다(12). 그림 1을 직접 열었다(14–16). Use I·Specify I의 `6`, Primary Group의 `Water Column`, Parameter의 `Temperature`를 보여 준다. 추출 전에 Profile Definition을 설정해야 하며 I 고정 시 해당 I의 활성 J 셀을, J 고정 시 해당 J의 활성 I 셀을 추출한다(18). 드레이프 선(Drape Line) 좌표 조건 원문: `The third option is to use a "Drape Line", which is a polyline in the same coordinate system as the LX, LY data.` (18). 이 선의 I·J들을 조합해 단면을 출력하며 I·J 추출은 좌표 선택을 위아래로 이동할 수 있다(18). |
| 20–29 | 변수·레이아웃·속성 — Define Parameter to Plot에서 `Primary Group`, `Parameter`를 고른 뒤 반드시 왼쪽 화살표로 확인하며 여러 변수를 추가할 수 있다(20). Parameters to Plot에서 오른쪽 화살표로 제거하고 Save·Load로 레이아웃을 저장·불러오며 Up·Down으로 표시 순서를 바꾼다(22). Update는 현재 강조된 변수를 Define Parameter to Plot의 현재 선택 변수로 교체한다(24). Properties는 색상표·등치선·정밀도·범위를 설정한다(26). 예시 인덱스 원문은 `temperature of the I = 38 at a specific time`이다(28). |
| 30–41 | 그림 2–4 / 수온 예시 — 세 그림을 직접 열었다(30·34·38). 그림 2는 Temperature의 속성 창이며 `Min. Value: 0.0000`, `Max. Value: 1.0000`, `Legend Precision: F2`, `Color Ramp: Default`이다. `Automatic Range`는 체크, `Interpolate Corner Values`·`Auto-Scale with View`·`Reverse`·`Show Contour`는 해제되어 있다(30행 그림). 그림 3의 프로파일 옵션은 `Use J`, `Specify J: 38`이며 Temperature가 추가되어 있다(34행 그림). 그림 4 범례는 `Row: J = 38, Time: 2013-01-29 04:00`, `Temperature (°C)`, 범위 `0.80`부터 `2.69`이다. X축은 `Distance (m)`, `0`부터 `8600`까지 `860` 간격이다. Y축은 `Elevation (m)`, `232.50`부터 `260.00`까지 `2.50` 간격이다. 상부의 낮은 수온은 파랑이며 깊은 하부의 높은 수온은 주황·빨강이다(38행 그림). |
| 42–51 | Data Extraction of EFDC Arrays — EEMS11.3에서 EFDC 배열(array) 변수의 2DV 표시를 추가했다고 적는다(44). 설정 원문: `Select EFDC Arrays for the *Primary Group*, and then select a parameter from the drop-down list` (44). 그림 5에 해당하는 46행 그림을 직접 열었다. `Use I`, `Specify I: 9`, `Primary Group: EFDC Arrays`, `Parameter: AV`이며 목록의 이름은 `DZC`, `QQ`, `DML`, `LENGHT`, `AV`, `AB`이다(46행 그림). 48행 캡션은 Figure 2라고 적는다. 50행은 EFDC Arrays Parameters 표 제목이다. |
| 52–60 | EFDC 배열 변수 표 — 각 행의 이름·설명·단위 원문은 `DZC` / `Vertical layer thickness as a decimal fraction of water depth dimensionless` / `unitless` (54); `QQ` / `Turbulent intensity` / `L\*L/T\*T` (55); `DML` / `Turbulence dimensionless length` / `unitless` (56); `LENGHT` / `Turbulence length scale` / `meters` (57); `AV` / `Vertical Eddy viscosity` / `L\*L/T` (58); `AB` / `Vertical Eddy diffusivity` / `L\*L/T` (59). 기본값과 허용 범위는 표에 없다. 단위 문자열의 연산 순서와 철자를 수정하지 않았다. |
| 61–63 | 그림 6 / 수직 와점성(Vertical Eddy viscosity) — 그림을 직접 열었다(61). 범례는 `Col: I = 9, Time: 2022-01-01 00:00`, `AV`, 범위 `0.00000`부터 `0.00282`이다. X축은 `Distance (m)`이며 보이는 눈금은 `0`, `1`, `3`, `4`, `5`, `6`, `8`, `9`, `10`, `11`, `13`이다. Y축은 `Elevation (m)`, `-10.00`부터 `0.00`까지 `1.25` 간격이다. 수면·저면 부근은 파랑이고 중간 표고는 빨강인 수평 띠를 보여 준다. 색상 범례에는 AV 단위가 표시되어 있지 않다(61행 그림). 캡션은 특정 시각의 I=9 AV 단면이라고 적는다(63). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 28·34·38: 본문은 수온 예시를 `I = 38`이라고 적지만 그림 3은 `Use J`, `Specify J: 38`이며 그림 4 범례도 `Row: J = 38`이다.
- 32·44·48: 본문은 EFDC Arrays 선택 그림을 Figure 5로 참조한다. 48행 캡션은 Figure 2이며 32행에도 Figure 2 캡션이 있다.
- 55: QQ 단위는 `L\*L/T\*T`로 적혀 있다. 이 문서에는 연산 우선순위나 L·T의 정의가 없다.
- 57·46행 그림: 매개변수 이름은 표와 목록 모두 `LENGHT`로 적혀 있다.
- 12·18·26·28·44: `#Figure1`부터 `#Figure6` 및 `#Table1` 링크가 있지만 이 Markdown 파일에는 해당 앵커 정의가 없다.
