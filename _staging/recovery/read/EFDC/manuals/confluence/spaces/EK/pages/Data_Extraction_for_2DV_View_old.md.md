---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Data_Extraction_for_2DV_View_old.md
lines: 49
sha256: ac8fa7e01ca2c160fcd6def9edb66918bc3e87b84853e1fdd7121774a6f1c8ad
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Extraction_for_2DV_View_old.md — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더를 기준으로 적었다.

| 구간 | 내용 |
|---|---|
| 1–9 | 2DV 자료 추출(Data Extraction) 구문서의 문서 ID·제목·space·URL·버전·갱신 시각·경로와 frontmatter이다(1–9행). |
| 10–17 | 2DV에 표시할 프로파일(profile)의 위치와 매개변수 선택을 설명한다(10행). 추출 전 `Profile Definition` 설정이 필요하다. I를 고정해 활성 J 셀을 추출하거나 J를 고정해 활성 I 셀을 추출할 수 있다. 세 번째 `Drape Line`은 LX·LY와 같은 좌표계의 폴리라인(polyline)을 사용한다(16행). 원문: `The *Profile Definition* frame needs to be set before a profile can be extracted from EFDC. There are three options shown in Figure 1. The user may either select a value of I to extract the active J cells along that I, or select a value of J to extract the active I cells along that J. The third option is to use a "Drape Line", which is a polyline in the same coordinate system as the LX, LY data. The I & J's along this line will be assembled and the profile will be output along with that slice. If an I or J extraction is used, the user can scroll up and down the select a coordinate.` (16). 그림 직접 확인: `attachments/442892355/4.png` — `Data Extraction for 2DV View`에서 `Use I`를 선택한 프로파일 추출 화면이다(12행). 화면의 설정은 `Specify I: 10`, `Base Model: Orginal Sediment Model`, `Primary Group: Water Column`, `Parameter: Salinity`, `Parameters to Plot: Salinity`이다. |
| 18–25 | `Primary Group` 뒤에 `Parameter`를 선택하고 왼쪽 화살표로 확정해야 한다(18행). 여러 매개변수를 선택할 수 있다. 오른쪽 화살표는 제거, `Save`·`Load`는 레이아웃 저장·불러오기, `Up`·`Down`은 표시 순서 변경이다(20행). `Update`는 강조된 매개변수를 현재 선택으로 교체한다(22행). `Properties`는 색상·등고선·정밀도·범위 등의 속성을 연다(24행). 원문: `The *Define Parameter to Plot* frame requires the user to select which parameters will be displayed. First, the user should choose the *Primary Group*, then select the *Parameter* from that group. It is required to click the left arrow button to confirm the selection. It is possible to select more than one parameter for the plot.` (18); `The *Update*button will replace the currently highlighted parameters in the *Parameters to Plot* frame with the currently selected parameters in *Define Parameter to Plot* frame.` (22). |
| 26–37 | 속성 창의 그림과 `OK` 표시 절차이다(26–30행). EFDC 배열을 표시하려면 기본 그룹을 `EFDC Arrays`로 선택해야 한다고 설명한다(32행). 원문: `The latest version of EEMS supports a new function to view the parameters of EFDC arrays in 2DV. In *Data Extraction* form, the primary group should be selected as *EFDC Arrays* and then the drop-down list of parameters are available.` (32). 그림 직접 확인: `attachments/442892355/5.png` — `2DV View Properties`의 격자선·색상 범위 설정 화면이다(26행). `Name: Salinity`, `Visible`, `Show Grid`, `Show in Legend`는 선택되어 있다. `Style: Solid`, `Width: 1.00`, `Automatic Range` 선택, `Interpolate Corner Values` 미선택, `Show Contour` 미선택, `Min. Value: 0.0000`, `Max. Value: 1.0000`, `Legend Precision: F3`, `Reverse` 미선택, `Color Ramp: Default`가 보인다. 범위 값 입력칸은 비활성화된 표시이다. 그림 직접 확인: `attachments/442892355/2022-06-13_10-28-21_AM.png` — `Primary Group: EFDC Arrays`의 매개변수 목록을 보여 준다(34행). `Specify I: 9`, `Base Model: Couette_flow`, `Parameters to Plot: AV`이다. 목록은 `DZC`, `QQ`, `DML`, `LENGHT`, `AV`, `AB` 순서이다. |
| 38–44 | EFDC 배열 매개변수의 이름·정의·단위이다(38–43행). 오탈자와 차원 표현을 고치지 않고 그대로 옮겼다. 원문: `- DZC : VERTICAL LAYER THICKNESS AS DECIMAL FRACTION OF WATER DEPTH DIMENSIONLESS` (38); `- QQ : TURBULENT INTENSITY` (39); `- DML : TURBULENCE DIMENSIONLESS LENGTH` (40); `- LENGHT : TURBULENT LENGHT SCALE` (41); `- AV : VERTICAL EDDY VISCOSITY L\*L/T` (42); `- AB : VERTICAL EDDY DIFFUSVITY L\*L/T` (43). |
| 45–49 | 선택한 매개변수를 `OK`로 표시하는 절차(45행)와 `AV` 연직 단면 그림·캡션(47–49행)이다. 그림 직접 확인: `attachments/442892355/2022-06-13_10-28-55_AM.png` — `2DV View (Couette_flow)`에서 `AV`를 색상으로 표시한 연직 단면이다(47행). 그래프 제목은 `New EFDC Model`이다. 가로축 `Distance (m)`의 표시는 `0`, `1`, `3`, `4`, `5`, `6`, `8`, `9`, `10`, `11`, `13`이다. 세로축 `Elevation (m)`의 표시는 `0.00`, `-1.25`, `-2.50`, `-3.75`, `-5.00`, `-6.25`, `-7.50`, `-8.75`, `-10.00`이다. 수면과 바닥 쪽은 파랑이고 중앙부는 빨강이다. 범례는 `Col: I = 9, Time: 2022-01-01 16:00`, 양 끝 값 `0.00`, `0.00`, 변수 `AV`를 보여 준다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 매개변수 차원 `L\*L/T`의 `L`과 `T`는 이 문서에서 정의하지 않는다(42–43행).
- AV 단면 그림의 범례 양 끝은 모두 `0.00`으로 표시되어 있으며 서로 다른 색상에 대응하는 더 정밀한 값은 보이지 않는다(47행).

