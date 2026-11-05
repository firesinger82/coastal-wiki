# PDF 판독 기록 전수 대조 — pdf-29

- 원본 PDF: `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Manual/CADMAS-STR_Program Instructions_English.pdf`.
- 대상 기록: [p055-072.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Manual/CADMAS-STR_Program%20Instructions_English.pdf/p055-072.md).
- 대조 범위는 PDF p.55–72다.
- 대조한 쪽 수는 18쪽이다.
- 고친 쪽 수는 18쪽이다.
- 정정한 쪽 수는 16쪽이다.
- 보완한 쪽 수는 14쪽이다.
- 정정과 보완을 함께 한 쪽 수는 12쪽이다.
- 위 정정·보완 수는 해당 표지가 붙은 쪽 수다.
- 두 표지가 함께 붙은 쪽은 두 범주에 각각 포함한다.
- 기존 기록을 그대로 유지한 일치 행은 0개다.
- 이미지 경로는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/cad-str-instr-NNN.png`다.
- `NNN`은 `055`부터 `072`까지다.
- 300 dpi PNG 18개를 이미지 보기 도구로 직접 열었다.
- p.58·63–67·69–71은 작은 기호와 끝주소를 추가로 확대했다.
- 확대 이미지는 메모리에서 만들었다.
- 철자 확인에는 지정된 텍스트 추출본을 참고했다.
- 판독 기준은 쪽 이미지다.
- 열지 못한 이미지는 없다.

## 정정·보완 목록

아래 표의 이전·새 내용은 변경 부분이다.
같은 쪽의 나머지 본문·표·배열 도식도 대조했다.

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.55 | 기록 없음 | [보완] 표의 열 제목은 `No.`, `Variable name`, `contents`다. | p.55 상단 KK 표 머리행. |
| p.56 | `4.1 [1] KK Table`의 | [정정] 앞 쪽에서 이어지는 절 `4.1 Control data table`의 `[1] KK Table`이다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. 표의 | p.56 상단은 KK 표의 항목 30에서 시작한다. |
| p.57 | `4.1 [1] KK Table`의 | [정정] 앞 쪽에서 이어지는 절 `4.1 Control data table`의 `[1] KK Table`이다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. 표의 | p.57 상단은 KK 표의 항목 68에서 시작한다. |
| p.58 | `4.1 [1] KK Table`의 항목 102–113과 `[2] RR table`을 싣는다. | [정정] 앞 쪽에서 이어지는 절 `4.1 Control data table`의 `[1] KK Table` 항목 102–113을 싣는다. 이 쪽에 인쇄된 소제목은 `[2] RR table`이다. | p.58 상단은 KK 표의 항목 102에서 시작한다. RR 표 앞에만 소제목이 있다. |
| p.58 | 기록 없음 | [보완] `RR table`의 열 제목은 `No.`, `contents`다. | p.58 하단 RR 표 머리행. |
| p.59 | `4.1 [3] IFL table`. | [정정] 앞 쪽에서 이어지는 절 `4.1 Control data table`이다. 이 쪽의 소제목은 `[3] IFL table`이다. | p.59 상단에는 `[3] IFL table`만 인쇄되어 있다. |
| p.59 | 기록 없음 | [보완] 표의 열 제목은 `No.`, `拡張子`, `contents`다. | p.59 IFL 표 머리행. |
| p.60 | 입력 데이터는 `NASTRAN BULK data format`이며 굵은 글씨는 대응 입력 항목 이름을 뜻한다. | [보완] `The following data tables are used to read input data (in NASTRAN BULK data format) and set its contents.`(p.60) 아래 데이터 표는 `NASTRAN BULK data format`의 입력 데이터를 읽고 그 내용을 설정하는 데 사용된다. 굵은 글씨는 각 데이터 표에 대응하는 `NASTRAN BULK` 데이터의 입력 항목 이름을 뜻한다. | p.60 첫 문장의 `are used to read input data ... and set its contents`. |
| p.60 | 기록 없음 | [보완] `INDG` 위의 열 표기는 `1`, `2`, 생략점, 마지막 열의 순서다. `IGCD`와 `GRID`는 그 아래에 같은 열 배치로 그려져 있다. | p.60 하단 Node 배열 도식. |
| p.61 | `4.2 [3] Element, element characterization`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`이다. 이 쪽의 소제목은 `[3] Element, element characterization`이다. | p.61 상단 소제목에는 `[3] Element, element characterization`만 인쇄되어 있다. |
| p.61 | 기록 없음 | [보완] 표의 열 구분 이름은 `element type`이다. 요소 종류별 총수 행의 이름은 `Total number of each element type`이다. 전체 요소 수 행의 이름은 `Total number of elements`다. 입력 항목은 `PSOLID, CTETRA, CPENTA, CHEXA`, `PROD, CROD`, `PBARL, CBAR`의 세 줄로 인쇄되어 있다. | p.61 IELM 표의 왼쪽 표제와 상단 입력 항목 세 줄. |
| p.62 | `4.2 [3] Element, element characterization`의 계속이다. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`의 `[3] Element, element characterization`이다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | p.62 상단은 `PROD`에서 시작한다. |
| p.62 | 기록 없음 | [보완] `BVEC` 첫 행의 원문 표기는 `Direction vectors X1`이다. `BARD`와 `BVEC` 위의 열 표기도 각각 `1`, `2`, 생략점, 마지막 열의 순서다. | p.62 BARD·BVEC 위의 열 번호와 BVEC 첫 행. |
| p.63 | `4.2 [4] Material`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`이다. 이 쪽의 소제목은 `[4] Material`이다. | p.63 상단 소제목에는 `[4] Material`만 인쇄되어 있다. |
| p.63 | 기록 없음 | [보완] `MAT` 위의 열 표기는 `1`, `2`, 생략점, 마지막 열의 순서다. `AMAT`는 그 아래에 같은 열 배치로 그려져 있다. | p.63 MAT·AMAT 배열 도식. |
| p.64 | `4.2 [5] Single-point restraint`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`이다. 이 쪽의 소제목은 `[5] Single-point restraint`이다. | p.64 상단 소제목에는 `[5] Single-point restraint`만 인쇄되어 있다. |
| p.64 | 기록 없음 | [보완] `ISPA`와 `ISP1` 위의 열 표기는 각각 `1`, `2`, 생략점, 마지막 열의 순서다. `NSPA`와 `NSP1` 위의 열 표기는 각각 \(1,2,\ldots,n_1,\ldots,n_2,\ldots\)와 마지막 열의 순서다. \(n_1\)과 \(n_2\) 바로 오른쪽에는 구간 경계를 표시하는 굵은 세로선이 있다. | p.64 배열 위의 열 번호·생략점·끝주소와 굵은 경계선. |
| p.65 | `4.2 [5] Single-point restraint`의 `SPC`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`의 `[5] Single-point restraint`이다. 이 쪽에 인쇄된 입력 항목 이름은 `SPC`다. | p.65 상단은 `SPC`에서 시작한다. |
| p.65 | 기록 없음 | [보완] `ISPC` 위의 열 표기는 각각 `1`, `2`, 생략점, 마지막 열의 순서다. `NSPC` 위의 열 표기는 각각 \(1,2,\ldots,n_1,\ldots,n_2,\ldots\)와 마지막 열의 순서다. \(n_1\)과 \(n_2\) 바로 오른쪽에는 구간 경계를 표시하는 굵은 세로선이 있다. | p.65 배열 위의 열 번호·생략점·끝주소와 굵은 경계선. |
| p.66 | `4.2 [6] Static load`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`이다. 이 쪽의 소제목은 `[6] Static load`이다. | p.66 상단 소제목에는 `[6] Static load`만 인쇄되어 있다. |
| p.66 | 기록 없음 | [보완] `ISPD`와 `LOAD` 위의 열 표기는 각각 `1`, `2`, 생략점, 마지막 열의 순서다. `NSPD`와 `SILD` 위의 열 표기는 각각 \(1,2,\ldots,n_1,\ldots,n_2,\ldots\)와 마지막 열의 순서다. \(n_1\)과 \(n_2\) 바로 오른쪽에는 구간 경계를 표시하는 굵은 세로선이 있다. | p.66 배열 위의 열 번호·생략점·끝주소와 굵은 경계선. |
| p.67 | `4.2 [6] Static load`의 `FORCE, MOMENT`와 `PLOAD4`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`의 `[6] Static load`이다. 이 쪽에 인쇄된 입력 항목 이름은 `FORCE, MOMENT`와 `PLOAD4`다. | p.67 상단은 `FORCE, MOMENT`에서 시작한다. |
| p.67 | 기록 없음 | [보완] `IFC`와 `IPL4` 위의 열 표기는 각각 `1`, `2`, 생략점, 마지막 열의 순서다. `NFC`와 `NPL4` 위의 열 표기는 각각 \(1,2,\ldots,n_1,\ldots,n_2,\ldots\)와 마지막 열의 순서다. \(n_1\)과 \(n_2\) 바로 오른쪽에는 구간 경계를 표시하는 굵은 세로선이 있다. | p.67 배열 위의 열 번호·생략점·끝주소와 굵은 경계선. |
| p.68 | `4.2 [6] Static load`의 `GRAV`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`의 `[6] Static load`이다. 이 쪽에 인쇄된 입력 항목 이름은 `GRAV`다. | p.68 상단은 `GRAV`에서 시작한다. |
| p.69 | `4.2 [7] Dynamic load`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`이다. 이 쪽의 소제목은 `[7] Dynamic load`이다. | p.69 상단 소제목에는 `[7] Dynamic load`만 인쇄되어 있다. |
| p.69 | 기록 없음 | [보완] `IDLD`, `ITL1`, `ITD1` 위의 열 표기는 각각 `1`, `2`, 생략점, 마지막 열의 순서다. `SIDL`과 `TBD1` 위의 열 표기는 각각 \(1,2,\ldots,n_1,\ldots,n_2,\ldots\)와 마지막 열의 순서다. \(n_1\)과 \(n_2\) 바로 오른쪽에는 구간 경계를 표시하는 굵은 세로선이 있다. | p.69 배열 위의 열 번호·생략점·끝주소와 굵은 경계선. |
| p.70 | `4.2 [8] Contact`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`이다. 이 쪽의 소제목은 `[8] Contact`이다. | p.70 상단 소제목에는 `[8] Contact`만 인쇄되어 있다. |
| p.70 | 기록 없음 | [보완] `ICPA`, `ICPR`, `ICRG` 위의 열 표기는 각각 `1`, `2`, 생략점, 마지막 열의 순서다. `NCPA`, `NCPR`, `NCRG` 위의 열 표기는 각각 \(1,2,\ldots,n_1,\ldots,n_2,\ldots\)와 마지막 열의 순서다. \(n_1\)과 \(n_2\) 바로 오른쪽에는 구간 경계를 표시하는 굵은 세로선이 있다. | p.70 배열 위의 열 번호·생략점·끝주소와 굵은 경계선. |
| p.71 | `4.2 [9] Analysis control`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`이다. 이 쪽의 소제목은 `[9] Analysis control`이다. | p.71 상단 소제목에는 `[9] Analysis control`만 인쇄되어 있다. |
| p.71 | 기록 없음 | [보완] `ISTP` 위의 열 표기는 각각 `1`, `2`, 생략점, 마지막 열의 순서다. `NSTP` 위의 열 표기는 각각 \(1,2,\ldots,n_1,\ldots,n_2,\ldots\)와 마지막 열의 순서다. \(n_1\)과 \(n_2\) 바로 오른쪽에는 구간 경계를 표시하는 굵은 세로선이 있다. | p.71 배열 위의 열 번호·생략점·끝주소와 굵은 경계선. |
| p.72 | `4.2 [10] Other`. | [정정] 앞 쪽에서 이어지는 절 `4.2 Input Data Table`이다. 이 쪽의 소제목은 `[10] Other`이다. | p.72 상단 소제목에는 `[10] Other`만 인쇄되어 있다. |

## 유지한 원문 표기와 확인 결과

- p.55–58의 KK 항목 1–113은 이미지와 대조했다.
- p.58의 RR 항목 1–14는 이미지와 대조했다.
- p.59의 IFL 항목 10–18은 이미지와 대조했다.
- 위 표의 빈 항목도 기존 기록과 일치했다.
- p.60–72의 배열 등식 40개는 기존 기록과 일치했다.
- p.68의 곱 표기 3개는 기존 기록과 일치했다.
- p.72의 마지막 행 주소 식 1개는 기존 기록과 일치했다.
- 위 수식 수는 대상 기록에서 센 값이다.
- 이미지에는 이 수식들의 식 번호가 없다.
- 이미지에는 배열 도식의 그림·표 번호와 별도 캡션이 없다.
- p.57의 `the the` 중복은 인쇄된 그대로 유지했다.
- p.63의 `Mieses` 철자는 인쇄된 그대로 유지했다.
- p.59의 `拡張子`와 한국어 뜻은 일치했다.
- p.61의 `BVEC 参照`와 한국어 뜻은 일치했다.
- p.63의 `CADMAS 用`과 한국어 뜻은 일치했다.
- p.63의 \(K_{\mathrm f}\), \(\boldsymbol{\rho}_{\mathrm f}\), \(\boldsymbol{\sigma}_{\mathrm y}\), \(\boldsymbol{\sigma}_{\mathrm t}\)의 아래첨자는 기존 기록과 일치했다.
- p.64–71의 끝주소 \(n_1\), \(n_2\)는 기존 기록과 일치했다.
- `Si`, `Li`, `Xi`, `Yi`, `SIDi`, `TIDi`, `Ni`, `NOi`, `DTi`의 `i`는 기준선 표기다.
- 기존 기록의 frontmatter에는 요청한 `verified_by` 한 줄만 추가했다.
- 기존 기록의 쪽 표는 18행을 유지했다.

정정 16, 보완 14, 일치 0
