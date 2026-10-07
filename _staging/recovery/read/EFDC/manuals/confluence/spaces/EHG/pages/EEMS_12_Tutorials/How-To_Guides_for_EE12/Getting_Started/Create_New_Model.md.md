---
file: models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Getting_Started/Create_New_Model.md
lines: 30
sha256: 4735f3748bf3d333d190b6b385e5d05c95a20574d9928ca7e2b79b15b7dd8ec5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Create_New_Model.md — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 메타데이터와 새 모델 생성 — 10행에는 CSS 색상 규칙 뒤에 EE10 새 모델 생성 안내가 이어진다. Model의 New Model, 도구모음 New Model, `Ctrl+N`의 세 방법을 제시한다(12–14). |
| 16–20 | 그림 1–2 / 새 모델 버튼 — 16행과 19행의 로컬 그림을 열었다. 첫 그림은 Model의 New Model과 `Ctrl+N`, 둘째 그림은 도구모음 New Model 버튼을 강조한다. |
| 21–29 | Grid Tool의 네 격자 선택 — 기존 파일 가져오기, 균일 격자(uniform grid), 방사형 격자(radial grid), 크기를 점차 바꾸는 격자(telescoping grid)를 제시한다(21–28). 여러 하위 격자일 때 Multiple grid files를 선택할 수 있으며 균일 격자는 셀 크기와 개수를 정의한다고 적는다(23–24). 조건·설정 이름 원문: `1. *Import Grids from Files*: this option allows the user to import an existing grid file; the grid can be one of a number of formats including CVLGrid or RGFGrid. If the user has multiple sub-grids for a waterbody then the *Multiple grid files*  check box may be selected. Browse to the grid file and click *OK* button to finish. (see [Create New Model#Figure 3](#Figure3) and [Create New Model#Figure 4](#Figure4)).` (23); `2. *Generate Uniform Grid*: this option allows the user to generate a Cartesian grid. The user can define grid cell size and  the number of cells (see [Create New Model#Figure 5](#Figure5)).` (24); `3. *Generate Radial Grid*: this option allows the user to generate radial grid ( see [Create New Model#Figure 6](#Figure6)).` (25); `4. *Generate Telescoping Grid*: this option allows the user to generate a telescoping grid ( see [Create New Model#Figure 7](#Figure7)).` (26). 상세 내용은 별도 Model Grid 절에 연결한다(28). |
| 30–30 | 그림 3–7 / 격자 예제 — 같은 행의 로컬 그림 다섯 개를 모두 열었다(30). 그림 3의 `Grid type` 목록은 `CVLGrid`, `RGFGrid`, `Grid95`, `DXDY/LXLY`, `ECOMSED`, `SEAGRID`, `CH3D`, `Corners(4)`이며 Multiple grid files 상자는 해제됐다. 붉은 화살표는 Import Grids에서 Import Grid 창으로 향한다. 그림 4는 녹색 곡선 격자를 보여 주며 수치 축·화살표는 없다. 그림 5의 Uniform Grid Options 표는 X Direction/Y Direction 순으로 `Lower-Left (m): 0 / 0`, `Upper-Right (m): 1000 / 1000`, `Cell Size (m): 20.00 / 20.00`, `Number of Cells: 50 / 50`, `Rotation Angle (°): -10`이다. 녹색 정사각형 셀 영역을 회전시켰으며 P1은 아래, P2는 오른쪽, P3는 위, P4는 왼쪽이다. 그림 6의 Radial Grid Options는 `Focal Point (m): 0 / 0`, `Start Angle (°): 30`, `End Angle (°): 150`, `Angular Step (°): 3`, `Radius Range (m): 4861.61 / 20000`, `# Cells Along A: 40`, `# Cells Along R: 27`, `Aspect Ratio: 1`이다. 녹색 부채꼴 격자의 P1은 안쪽 원호, P3는 바깥 원호, P2는 위쪽 변, P4는 아래쪽 변이다. 그림 7의 Telescoping Grid Options는 X/Y 순으로 `Lower-Left (m): 0 / 0`, `Upper-Right (m): 5000 / 5000`, `Focal Point (m): 2500 / 2500`, `Min. Cell Size (m): 87.30 / 87.30`, `Max. Cell Size (m): 533.91 / 533.91`, `Growth Factor: 1.10 / 1.10`, `Number of Cells: 30 / 30`, `Rotation Angle (°): 0`이다. 중심에 작은 직사각형 셀, 바깥에 큰 셀을 두며 P1은 아래, P2는 오른쪽, P3는 위, P4는 왼쪽이다. 각 그림의 `UTM Zone`은 `0`이다. 이 값은 표시된 예제이며 기본값이라고 명시하지 않았다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: `[data-colorid=...]` 및 `html[data-color-mode=dark]` CSS 문자열이 본문 첫 문장 앞에 남아 있다.
- 12·13·23–26행: `#Figure1`–`#Figure7` 링크를 사용하나 해당 ID를 선언한 앵커가 본문에 없다. 17행에는 Figure 1 캡션이 있지만 나머지 그림은 별도 캡션 없이 배치되어 있다.
