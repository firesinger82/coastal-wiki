SWASH `swashuse.pdf` 73–108쪽의 10-15 전수 검증 기록이다.

원문은 `models/SWASH/raw/source_code/swash/doc/swashuse.pdf`이다.
쪽 번호는 PDF 쪽 번호이다.
대조에는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swhpages/swashuse-NNN.png`의 300 dpi 쪽 이미지를 사용했다.
`NNN`은 세 자리 쪽 번호이다.
73–108쪽의 모든 이미지를 열어 해당 쪽 행의 의미와 대조했다.
수식의 첨자·부호·지수·분모를 확인했다.
수치·단위·기본값을 확인했다.
명령 구문의 선택 항목·키워드·기본값 화살표를 확인했다.
조건·부정·불확실성 표현을 확인했다.
각 설명과 절 제목·명령 이름이 해당 쪽에 인쇄되어 있는지 확인했다.

| 기록 | 대조 범위 | 대조한 쪽 수 | 정정 | 보완 | 이상 없음 |
|---|---|---:|---:|---:|---:|
| [p073-090.md](../swash/doc/swashuse.pdf/p073-090.md) | 73–90 | 18 | 18 | 0 | 0 |
| [p091-108.md](../swash/doc/swashuse.pdf/p091-108.md) | 91–108 | 18 | 12 | 0 | 6 |
| 합계 | 73–108 | 36 | 30 | 0 | 6 |

집계 단위는 쪽 행이다.
같은 쪽의 여러 정정은 1건으로 집계했다.
정정한 쪽 행의 끝에 `[10-15 전수 검증 정정]`을 붙였다.
빠진 식이나 조건을 추가한 보완은 없었다.
이상 없음은 `p091-108.md`의 p.92, p.94, p.96, p.98, p.99, p.101이다.

`4.5.4 Physics` 제목은 p.73에 인쇄되어 있다.
`4.5.5 Numerics` 제목은 p.89에 인쇄되어 있다.
`4.6 Output` 제목은 p.101에 인쇄되어 있다.
`4.6.1 Output locations` 제목은 p.102에 인쇄되어 있다.
`4.6.2 Write or plot computed quantities` 제목은 p.106에 인쇄되어 있다.
후속 쪽에서 이 제목을 사용하는 경우에는 시작 쪽 또는 앞 쪽에서 이어진다는 출처를 밝혔다.

정정 내역은 다음과 같다.
인쇄 원문 칸은 해당 쪽의 관련 구절을 발췌한 것이다.
인쇄 원문의 줄바꿈은 정규화했다.
`…`는 중간 구절의 생략 표시이다.
인쇄 원문 칸의 여러 발췌는 줄바꿈으로 구분했다.

| 기록:쪽 | 이전 요지 | 새 요지 | 인쇄 원문 |
|---|---|---|---|
| p073-090.md:p.73 | Charnock 식을 바람과 거칠기 사이의 음적 관계로 설명했다. | 이 쪽에서 확인되는 음적 관계만 남겼다. 문장이 `between the wind`에서 끝남을 밝혔다. | `The Charnock drag formulation is based on an implicit relationship between the wind` |
| p073-090.md:p.74 | 4.5.4를 이 쪽 제목처럼 표시했다. Charnock 관계의 뒷부분을 앞 쪽 행에 적었다. | 절 제목의 출처를 p.73으로 밝혔다. 이 쪽 첫 구절에서 거칠기를 확인했다. | `and the roughness, while the other formulations … express a linear relationship between the drag and the wind speed.` |
| p073-090.md:p.75 | 4.5.4를 이 쪽 제목처럼 표시했다. 파봉과 파곡의 비교가 앞 쪽에서 이어짐을 밝히지 않았다. | 절 제목의 출처를 p.73으로 밝혔다. 첫 문장이 앞 쪽에서 이어짐을 밝혔다. | `wind drag on the wave crest than that in the trough (Chen et al., 2004).` |
| p073-090.md:p.76 | 4.5.4와 RELWAVE의 앞 쪽 출처를 밝히지 않았다. | 절 제목의 출처를 p.73으로 밝혔다. RELWAVE가 앞 쪽 선택지임을 밝혔다. | `Default: [crest] = 0.4` |
| p073-090.md:p.77 | 4.5.4와 CONSTANT의 앞 쪽 출처를 밝히지 않았다. | 절 제목의 출처를 p.73으로 밝혔다. CONSTANT가 앞 쪽 선택지임을 밝혔다. | `Note that [cf] is allowed to vary over the computational region` |
| p073-090.md:p.78 | 4.5.4와 LOGLAW ROUGHNESS의 앞 쪽 출처를 밝히지 않았다. | 절 제목의 출처를 p.73으로 밝혔다. 거칠기 설명이 앞 쪽에서 이어짐을 밝혔다. | `define the type of friction expression. The value of [h] in this command is then not required (it will be ignored).` |
| p073-090.md:p.79 | 4.5.4와 VISCOSITY의 앞 쪽 출처를 밝히지 않았다. | 절 제목의 출처를 p.73으로 밝혔다. 명령 설명의 출처를 p.78로 밝혔다. | `In SWASH both the horizontal and vertical eddy viscosities can be specified, either separately or combined.` |
| p073-090.md:p.80 | 4.5.4와 VISCOSITY의 출처를 밝히지 않았다. 첫 설명을 이 쪽만의 문장처럼 적었다. | 절 제목과 명령의 출처를 각각 p.73과 p.78로 밝혔다. 이차항 설명이 앞 쪽에서 이어짐을 밝혔다. | `state of the turbulent normal stresses. To this end, the nonlinear k−ε model of Speziale (1987) is applied.` |
| p073-090.md:p.81 | 4.5.4와 POROSITY 명령 구문의 앞 쪽 출처를 밝히지 않았다. | 절 제목의 출처를 p.73으로 밝혔다. 첫 설명이 앞 쪽 명령에 속함을 밝혔다. | `CANNOT BE USED IN CASE OF UNSTRUCTURED GRIDS.`<br>`This command indicates the use of porosity layers inside the computational domain` |
| p073-090.md:p.82 | 4.5.4와 VEGETATION 명령 구문의 앞 쪽 출처를 밝히지 않았다. | 절 제목의 출처를 p.73으로 밝혔다. 첫 설명이 앞 쪽 명령에 속함을 밝혔다. | `With this optional command the user can activate wave damping induced by aquatic vegetation.` |
| p073-090.md:p.83 | 4.5.4와 CORIOLIS 구문의 출처를 밝히지 않았다. 이 쪽에 없는 초기·경계조건을 언급했다. | 절 제목과 명령의 앞 쪽 출처를 밝혔다. 이 쪽 문장의 마지막 구절만 옮겼다. | `With this optional command the Coriolis force will be included in the momentum equations.`<br>`Using these commands,` |
| p073-090.md:p.84 | 4.5.4와 TRANSPORT의 앞 쪽 출처를 밝히지 않았다. | 절 제목의 출처를 p.73으로 밝혔다. TRANSPORT가 앞 쪽 명령임을 밝혔다. | `The first parameter that may be specified in this command is the horizontal eddy diffusivity.` |
| p073-090.md:p.85 | 4.5.4를 이 쪽 제목처럼 표시했다. | 절 제목의 출처를 p.73으로 밝혔다. | `Figure 4.2: Return time for unsteady salt intrusion.`<br>`For cohesive sediment … Partheniades-Krone formulations` |
| p073-090.md:p.86 | 점착성 퇴적물과 침식 임계응력 τ_ce를 이 쪽 내용으로 적었다. 절 번호와 명령의 출처가 없었다. | 이 쪽에 인쇄된 τ_cd, E, w_s만 남겼다. 앞 쪽에서 이어지는 문장임을 밝혔다. 절 제목과 명령의 출처를 밝혔다. | `sedimentation, τ_cd, the sediment erosion rate E and the fall velocity w_s must be specified by the user.` |
| p073-090.md:p.87 | 강하게 권장하지 않는다고 옮겼다. 이 쪽에 없는 적은 수직 층을 덧붙였다. 절·명령 출처가 없었다. | 사용하지 말라는 강한 권고로 고쳤다. 마지막 문장의 실제 끝만 남겼다. 절·명령 출처를 밝혔다. | `the use of this command in the case of current-limited wave breaking (see command AMBIENT) is strongly discouraged.`<br>`However, when a` |
| p073-090.md:p.88 | 4.5.4와 BREAKING의 앞 쪽 출처를 밝히지 않았다. | 절 제목의 출처를 p.73으로 밝혔다. BREAKING이 앞 쪽 명령임을 밝혔다. | `few vertical layers are to be employed …`<br>`[alpha] threshold parameter at which to initiate wave breaking.` |
| p073-090.md:p.89 | 4.5.4와 AMBIENT의 출처를 밝히지 않았다. 이 쪽 구문만으로 수직 압력경사 선택이라고 풀이했다. | 앞 쪽 절과 명령의 출처를 밝혔다. STANDARD와 BOX는 구문도의 선택지로만 적었다. | `4.5.5 Numerics`<br>`NONHYDrostatic`<br>`STAndard`<br>`→ BOX`<br>`[theta]` |
| p073-090.md:p.90 | variable thicknesses only를 적용 조건으로 단정했다. 절 제목과 첫 문장의 앞 쪽 출처가 없었다. | 등간격 층 분포 뒤의 괄호 보충으로 옮겼다. 앞 쪽 절과 설명에서 이어짐을 밝혔다. | `it is advised to choose an equidistant layer distribution (variable thicknesses only)` |
| p091-108.md:p.91 | ILU 권고 조건을 쉼표로 나열하여 or의 의미를 드러내지 않았다. | 큰 파고 또는 매우 짧은 파, 급한 바닥 경사, 많은 층 수를 각각의 권고 조건으로 적었다. | `when high waves or very short waves are involved, or when the bottom topography exhibits steep slopes, or when a considerable number of layers (> 20) is involved` |
| p091-108.md:p.93 | 이 쪽에 이름이 없는 명령을 공간 이산화 명령으로 풀이했다. UMOM·WMOM을 운동량 방정식으로 풀이했다. | 이 쪽에서는 다음 구문도의 시작과 UMOM·WMOM 분기만 확인할 수 있음을 적었다. | `UPWind`<br>`UMOM MOMentum\|HEAD`<br>`WMOM`<br>`→ Horizontal`<br>`Vertical` |
| p091-108.md:p.95 | 이 쪽에 인쇄되지 않은 DISCRETization 명령 이름의 출처를 밝히지 않았다. | 명령 이름의 출처를 앞 쪽으로 밝혔다. | `With this optional command the user can influence the spatial discretization.` |
| p091-108.md:p.97 | 다음 쪽에 인쇄된 평균 대상인 주변 모서리를 이 쪽 설명에 넣었다. | 평균을 취한다는 이 쪽 마지막 구절만 남겼다. 평균 대상은 다음 쪽으로 이어짐을 밝혔다. | `As a rule, we take the average` |
| p091-108.md:p.100 | 음의 수심 위험 설명을 이 쪽만의 문장처럼 적었다. | 앞 쪽에서 시작한 문장임을 밝혔다. | `as a larger time step is allowed.` |
| p091-108.md:p.102 | 이 쪽에 없는 §4.6 제목의 출처를 밝히지 않았다. | §4.6이 앞 쪽에서 이어짐을 명시했다. | `2. Write`<br>`plot`<br>`4.6.1 Output locations` |
| p091-108.md:p.103 | 이 쪽에 없는 §4.6.1 제목의 출처를 밝히지 않았다. | §4.6.1이 앞 쪽에서 이어짐을 명시했다. | `[myfr] number of meshes in y-direction …`<br>`GROUP ’sname’ SUBGrid [ix1] [ix2] [iy1] [iy2]` |
| p091-108.md:p.104 | 이 쪽에 없는 §4.6.1과 GROUP 이름의 출처를 밝히지 않았다. | 절의 시작 쪽을 p.102로 밝혔다. GROUP 설명이 앞 쪽에서 이어짐을 밝혔다. | `the command CGRID).`<br>`CURve ’sname’ [xp1] [yp1] < [int] [xp] [yp] >` |
| p091-108.md:p.105 | §4.6.1과 RAY의 출처를 밝히지 않았다. 첫 기준 광선 좌표를 [xp1],[yp1],[xq1],[yq1]로 적었다. | 절의 시작 쪽과 명령 설명의 연결을 밝혔다. 이 쪽에 인쇄된 첫 기준 광선의 좌표 이름을 [xq1],[yq1]로 한정했다. | `[xq1],[yq1] if Cartesian coordinates are used in m`<br>`if spherical coordinates are used in degrees (see command COORD)` |
| p091-108.md:p.106 | 이 쪽에 없는 §4.6.1과 POINTS 이름의 출처를 밝히지 않았다. | 절의 시작 쪽을 p.102로 밝혔다. POINTS 설명이 앞 쪽에서 이어짐을 밝혔다. | `’sname’ name of the points`<br>`4.6.2 Write or plot computed quantities` |
| p091-108.md:p.107 | 이 쪽에 없는 §4.6.2 제목의 출처를 밝히지 않았다. | §4.6.2가 앞 쪽에서 이어짐을 명시했다. | `reference direction for vectors.`<br>`The following data are accepted only in combination with some specific output quantities.` |
| p091-108.md:p.108 | §4.6.2 제목의 출처를 밝히지 않았다. [xcom]의 단위 정의가 앞 쪽에 있음을 밝히지 않았다. | 절의 시작 쪽을 p.106으로 밝혔다. [xcom] 단위의 정의는 앞 쪽에 있음을 명시했다. | `[ycom] y-coordinate of center of mass of floating body (in m).`<br>`[zcom] z-coordinate of center of mass of floating body (in m).`<br>`QUANT MomX xcom=200. ycom=0. zcom=-1.` |

두 기록의 frontmatter는 변경하지 않았다.
두 기록의 쪽 행 수와 순서는 변경하지 않았다.
두 기록의 쪽 행 밖 내용은 변경하지 않았다.

정정 30, 보완 0, 이상 없음 6

