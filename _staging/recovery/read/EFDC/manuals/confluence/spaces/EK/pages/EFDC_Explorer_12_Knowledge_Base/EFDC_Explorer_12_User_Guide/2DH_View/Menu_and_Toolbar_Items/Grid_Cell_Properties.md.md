---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Menu_and_Toolbar_Items/Grid_Cell_Properties.md
lines: 79
sha256: 3ea48d9c2a99fe3c855d83e819e2702b89281b9a1ab1c1cf9bf571fd07987649
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Grid_Cell_Properties.md — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–24 | 셀 정보(Cell Information) — 셀 속성의 보기·수정 메뉴를 소개한다(10). 셀을 왼쪽 클릭하면 노란 사각형에 정보를 표시하며 도구 모음으로도 활성화한다(16–20). 그림 1은 속성 메뉴를 보여 준다(12–14). 18행 그림은 정보 아이콘이다. 그림 2는 선택 셀과 노란 정보 상자를 보여 준다(22–24). 세 그림을 직접 열었다. |
| 25–34 | 셀 속성 편집(Edit Cell Properties) — 적용 조건 원문: `This function is only enabled for surface values layer initial condition ie time = 0.` (26). 출력이 있으면 시간 제어의 시작 버튼으로 초기 조건(initial condition, IC)으로 돌아간다(28–30). 레이어 펜을 활성화하고 Edit Cell Properties에서 셀을 왼쪽 클릭하여 Properties의 `Parameter`, `Value`를 편집한 뒤 Apply를 누른다(30). 28행 그림은 초기 시각 복귀 아이콘이다. 그림 3은 Bottom Elevation 레이어와 속성 표를 보여 준다(32–34). 그림의 표에서 읽은 행별 값은 `L - I - J: 225 - 52 - 21`, `Bottom Elevation: -26.367`, `Delta X: 343.13`, `Delta Y: 378.22`, `Water Depth: 32.460`, `Roughness: 0.00500`, `Angle: 9.669`, `Cell Type: 5`, `Mask South` 체크 해제이다(32행 그림). 표 아래의 추가 행은 화면 경계에서 잘려 있다. 두 그림을 직접 열었다. |
| 35–47 | 속성 복사(Copy Cell Properties)·선택 값 변경(Modify Selected Values) — CTRL+LMC로 원본 셀을 정하고 입력 상자의 값 또는 연산을 CTRL+RMC로 대상 셀들에 반복 적용한다(36). 단일 셀은 레이어 펜을 켜고 선택한 뒤 Modify Selection을 연다(37). 필드 원문은 `Parameter to Modify`, `Value to Apply`이다(37). Add는 원래 값에 입력값을 더하며 Subtract·Multiply·Divide도 제공한다(37). 대입 조건 원문: `If the user skips using the operators button and clicks the *Assign* button immediately then the cell is assigned with whatever the value was in the box.` (37). 여러 셀은 먼저 다중 선택한 후 같은 기능을 사용한다(43). 그림 4는 단일 셀의 Bottom Elevation에 `Value to Apply: 10`을 대입하는 창이다(39–41). 43행 그림은 셀 선택 아이콘이다. 그림 5는 다중 선택 셀에 `Value to Apply: -60`을 대입하는 창이다(45–47). 세 그림을 직접 열었다. 화면 입력값은 예시 값이다. |
| 48–63 | 선택 값 삭제(Delete Selected Values)·누락 값 채우기(Fill Missing Values) — 삭제한 셀 값은 `"NaN "(not a number)`로 표시된다(49). 누락 값 셀을 선택하고 `Selected Cells` 또는 `All Grid Cells`를 선택하여 보간(interpolation)한다(55). 그림 6은 삭제 영역과 `Bot EL (m): NaN` 정보 표시이다(51–53). 그림 7은 `Fill Missing Values Based on Values From` 아래 Selected Cells가 선택된 창이다(57–59). 그림 8은 보간 결과와 `21 missing values have been interpolated from 21 data points.` 메시지를 보여 준다(61–63). 세 그림을 직접 열었다. |
| 64–69 | 외부 자료 보간(Interpolate from Data) — XYZ 산점 자료(scatter data)를 먼저 불러오고 대상 레이어의 펜을 켠 뒤 셀을 선택한다(65). Data Interpolation 창에서 `Use`와 `Selected Cells`를 체크하고 OK를 누른다(65). 그림 9는 Bottom Elevation을 대상으로 Data 자료의 Use가 체크되고 Selected Cells가 선택된 보간 창이다(67–69). 그림을 직접 열었다. |
| 70–79 | I·J 하상 경사(Set IJ Slopes) — I, J 또는 두 방향 모두에 일정 하상 경사를 적용한다(71). 입력 필드 원문은 `Start Value`, `I Slope`, `J Slope`, `Target Cells`이다(71). 부호 조건 원문: `If the entered slope is positive the bottom elevations will decrease with higher I's and J's.`; `The inverse is true if the entered slope is negative.` (71). 그림 10은 `Start Value: 0`, `I Slope: 0.001`, `J Slope: 0.002`의 Assign Slope 창이며 Target Cells의 Selected Cells가 선택되어 있다(73–75). 그림 11은 100개 셀 갱신 결과와 Bottom Elevation 범례 `-2.700`부터 `0.000`, 단위 `(m)`를 보여 준다(77–79). 두 그림을 직접 열었다. 화면 값은 예시이며 본문은 기본값·허용 범위·경사 단위를 명시하지 않는다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 36: `operator method noted above`라고 적지만 1–35행에는 그 연산 방법의 설명이 없다. Add·Subtract·Multiply·Divide·Assign 설명은 37행에 나온다.
- 32행 그림 3: 속성 표의 하단 행이 화면 경계에서 잘려 전체 표를 판독할 수 없다.

