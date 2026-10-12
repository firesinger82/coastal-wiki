# SWAN swantech.pdf p.145–176 전수 검증

검증일은 2026-10-13이다.
원문은 두 기록의 frontmatter가 지정한 `models/SWAN/raw/manuals/pdfs/swantech.pdf`이다.
아래의 p.N은 PDF 쪽 번호다.

사용자가 지정한 300dpi 쪽 이미지 32개를 모두 직접 열어 대조했다.
이미지 경로는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swpages/swantech-NNN.png`이다.
대조한 이미지 번호는 145부터 176까지다.
추출 텍스트는 보조 확인에만 사용했다.
수식은 이미지에 인쇄된 문자·첨자·부호·지수·분모를 기준으로 대조했다.
각 쪽 행의 수치·단위·조건·한정 표현·부정·불확실성 표현을 대조했다.
절 번호와 제목은 해당 쪽에 실제로 인쇄되어 있는지 확인했다.
참고문헌은 각 쪽 행에 기록된 항목별로 대조했다.

대조한 행 수는 각 기록의 `| p.N |` 행을 세었다.
정정과 보완의 집계 단위도 쪽 행이다.
같은 쪽 행에 정정과 보완이 모두 있으면 각 분류에 한 번씩 집계했다.
목록에서는 같은 쪽 행의 같은 분류에 속하는 변경을 한 항목으로 묶었다.

| 기록 | 대조한 구간 | 대조한 행 수 | 정정 | 보완 | 정정·보완 모두 | 이상 없음 |
|---|---|---:|---:|---:|---:|---:|
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md) | p.145–162 | 18 | 14 | 8 | 6 | 2 |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md) | p.163–176 | 14 | 3 | 10 | 2 | 3 |
| 합계 | p.145–176 | 32 | 17 | 18 | 8 | 5 |

정정과 보완이 모두 있는 행은 p.147·p.151·p.158·p.159·p.161·p.162·p.163·p.167의 8개다.
서로 다른 변경 행은 27개다.
대조 행 수는 정정 17 + 보완 18 − 중복 8 + 이상 없음 5 = 32이다.

다음 목록의 ‘원문 행’은 이미지의 식 번호·참고문헌 번호·문장 발췌로 위치를 식별한다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.145 (보완) | Triangle 도구와 수심 자료에서 경계 요소를 만드는 가능성만 기록했다. | Triangle용 공개 Matlab·Python 그래픽 인터페이스와 격자 편집 기능을 이용하는 조건을 추가했다. | PDF p.145 / 인쇄 137쪽. §8.2 첫 문단의 “public-domain, graphical Matlab and Python interfaces to Triangle”. 둘째 문단의 “with the use of the mesh editing options of a mesh generation package”. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.146 (정정) | §8.3.1 제목을 계속 표기했다. 첫 항과 마지막 문장의 뜻을 인접 쪽 내용으로 완성했다. | 해당 쪽에 없는 절 번호·제목을 삭제했다. 첫 항은 인쇄된 F로 기술했다. 마지막 문장은 다음 쪽으로 이어진다고 한정했다. | PDF p.146 / 인쇄 138쪽. 쪽 첫 행 “F(x⃗, σ, θ):”. 마지막 행 “A key feature of this technique is that it takes advantage of the newly”. 해당 쪽에는 §8.3.1 제목이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.147 (정정) | §8.3.1 제목과 Gauss–Seidel 명칭을 이 쪽의 설명에 붙였다. | 해당 쪽에 없는 절 번호·제목과 기법 명칭을 삭제했다. 첫 문단을 앞 문장에 이어지는 기법 설명으로 기술했다. | PDF p.147 / 인쇄 139쪽. 첫 행 “acquired vertex values during an iteration. It is locally implicit but globally explicit.” 해당 쪽에는 §8.3.1 제목이나 Gauss–Seidel 명칭이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.147 (보완) | 안정성만 기록했다. 꼭짓점 갱신 때 각 셀을 순회하는 설명을 빠뜨렸다. | 양해법보다 빠른 정상 상태 수렴 가능성과 음해법 대비 계산량·메모리 조건을 추가했다. 각 셀 순회를 추가했다. | PDF p.147 / 인쇄 139쪽. 첫 문단 “can converge to steady state much more rapidly than explicit methods without requiring too much computational work and memory as do implicit methods”. 둘째 문단 “looping over each cell of this vertex”. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.148 (정정) | §8.3.1 제목을 계속 표기했다. | 해당 쪽에 없는 절 번호·제목을 삭제했다. | PDF p.148 / 인쇄 140쪽. Figure 8.3과 식 (8.11)–(8.14). 해당 쪽에는 §8.3.1 제목이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.149 (정정) | §8.3.1 제목을 계속 표기했다. N(arrow)와의 일치 조건에서 rectangles를 사각형으로 넓혀 적었다. | 해당 쪽에 없는 절 번호·제목을 삭제했다. 격자 생성 조건을 직사각형으로 한정했다. | PDF p.149 / 인쇄 141쪽. 식 (8.15) 뒤 문단 “on regular, triangular grids obtained from triangulation of rectangles with diagonals aligning with the wave characteristic as much as possible”. 해당 쪽에는 §8.3.1 제목이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.150 (정정) | upwave를 풍상으로 옮겼다. 갱신 순서의 예를 단정했다. sweep 수 증가가 포착하는 에너지의 양을 늘린다고 적었다. | 파랑 진행 방향의 상류로 고쳤다. 갱신 순서의 예시 한정을 복원했다. 일반적으로 방향 구간이 좁아져 에너지를 더 잘 포착한다는 뜻으로 고쳤다. sweep 3개의 절충은 경험에 근거한다고 밝혔다. | PDF p.150 / 인쇄 142쪽. §8.3.2 첫 문단 “two upwave vertices”, “e.g. left to right”. 둘째 문단 “In general, the higher the number of sweeps, the smaller the directional interval, the better the wave energy ... is captured”, “Experiences have shown”. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.151 (정정) | §8.3.2 제목과 앞 쪽의 오름차순 조건을 이 쪽에 붙였다. upwave를 풍상으로 옮겼다. | 해당 쪽에 없는 절 번호·제목을 삭제했다. 문장 중간에서 시작함을 명시했다. 두 면은 파랑 진행 방향의 상류에 있다고 고쳤다. | PDF p.151 / 인쇄 143쪽. 첫 행 “of vertices to the origin of the grid in line with the sweep direction”. 첫 문단 “The two upwave faces connecting the vertex to be updated”. 해당 쪽에는 §8.3.2 제목이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.151 (보완) | 다음 꼭짓점으로 진행하기 위한 갱신 조건을 빠뜨렸다. | 다음 꼭짓점으로 진행하기 전에 현재 꼭짓점을 지리 공간에서 갱신해야 한다는 조건을 추가했다. | PDF p.151 / 인쇄 143쪽. 첫 문단 “the solution of each vertex must be updated geographically before proceeding to the next one”. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.152 (정정) | §8.4 제목을 계속 표기했다. | 해당 쪽에 없는 절 번호·제목을 삭제했다. | PDF p.152 / 인쇄 144쪽. 첫 행 “We also need the following identity”와 식 (8.21)–(8.29). 해당 쪽에는 §8.4 제목이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.153 (정정) | 식 (8.31)에 n sinθ cosθ E를 적었다. | 원문에 없는 cos 뒤의 θ를 삭제했다. 원문 인쇄가 n sinθ cos E임을 명시했다. | PDF p.153 / 인쇄 145쪽. 식 (8.31)의 적분항 “n sin θ cos E dσ dθ”. 이미지에서 cos와 E 사이에 θ가 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.154 (정정) | §8.5 제목을 계속 표기했다. | 해당 쪽에 없는 절 번호·제목을 삭제했다. 실제 인쇄된 §8.6 제목은 유지했다. | PDF p.154 / 인쇄 146쪽. 쪽 첫 행 “the following we use the numbering from Figure 8.4”. 아래쪽에 §8.6 “Calculation of diffusion-like terms”가 있다. 해당 쪽에는 §8.5 제목이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.157 (보완) | [8]과 [10]의 제목에서 Part I을 빠뜨렸다. | 두 문헌의 Part I 표기를 추가했다. | PDF p.157 / 인쇄 149쪽. [8] “Swell transformation across the Continental Shelf. Part I: attenuation and directional broadening”. [10] “Semiempirical dissipation source functions for ocean waves. Part I: definition, calibration, and validation”. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.158 (정정) | Bibliography 제목을 계속 표기했다. | 해당 쪽에 없는 제목 대신 참고문헌 목록의 연속으로 기술했다. | PDF p.158 / 인쇄 150쪽. 쪽 상단의 인쇄 쪽 번호 150과 첫 항목 [11]. 해당 쪽에는 Bibliography 제목이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.158 (보완) | [11]의 제목에서 Part I을 빠뜨렸다. | Part I과 그 부제의 관계를 추가했다. | PDF p.158 / 인쇄 150쪽. [11] “Modelling spectral dissipation in the evolution of wind waves. Part I: Assessment of existing model performance”. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.159 (정정) | Bibliography 제목을 계속 표기했다. | 해당 쪽에 없는 제목 대신 참고문헌 목록의 연속으로 기술했다. | PDF p.159 / 인쇄 151쪽. 쪽 상단의 인쇄 쪽 번호 151과 첫 항목 [24]. 해당 쪽에는 Bibliography 제목이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.159 (보완) | [36]의 제목에서 Part I을 빠뜨렸다. | Part I과 모델 설명·검증 부제의 관계를 추가했다. | PDF p.159 / 인쇄 151쪽. [36] “A third-generation wave model for coastal regions, Part I, Model description and validation”. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.160 (정정) | Bibliography 제목을 계속 표기했다. [42]를 극한 수심 제한 풍파로 적었다. [46]의 인쇄 주소에서 줄 끝 하이픈을 제거했다. | 해당 쪽에 없는 제목을 삭제했다. extreme의 수식 대상을 풍파로 명확히 했다. 주소의 줄 끝 하이픈과 줄바꿈을 기록했다. | PDF p.160 / 인쇄 152쪽. 해당 쪽에는 Bibliography 제목이 없다. [42] “an extreme, depth-limited wind-sea”. [46] 주소 행 끝 “.../PDF/campbell-”와 다음 행 “paper.pdf”. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.161 (정정) | Bibliography 제목을 계속 표기했다. | 해당 쪽에 없는 제목 대신 참고문헌 목록의 연속으로 기술했다. | PDF p.161 / 인쇄 153쪽. 쪽 상단의 인쇄 쪽 번호 153과 첫 항목 [51]. 해당 쪽에는 Bibliography 제목이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.161 (보완) | [59]의 계산을 결합되고 확장 가능하다고만 적었다. | 결합 방식을 한정하는 integrally-coupled를 추가했다. | PDF p.161 / 인쇄 153쪽. [59] “Modeling hurricane waves and storm surge using integrally-coupled, scalable computations”. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.162 (정정) | Bibliography 제목을 계속 표기했다. | 해당 쪽에 없는 제목 대신 참고문헌 목록의 연속으로 기술했다. | PDF p.162 / 인쇄 154쪽. 쪽 상단의 인쇄 쪽 번호 154와 첫 항목 [65]. 해당 쪽에는 Bibliography 제목이 없다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.162 (보완) | [66]의 제목에서 Part II를 빠뜨렸다. | Part II와 바람 입력 매개변수화 부제의 관계를 추가했다. | PDF p.162 / 인쇄 154쪽. [66] “Wave follower field measurements of the wind input spectral function. Part II: Parameterization of the wind input”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.163 (정정) | [81]의 wave transmission over breakwaters를 방파제를 통한 파랑 투과로 적었다. | 방파제를 넘는 파랑 투과로 고쳤다. | PDF p.163 / 인쇄 155쪽. [81] “Laboratory investigation of wave transmission over breakwaters”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.163 (보완) | [79]의 Numerical 한정과 [90]–[92]의 part 번호를 빠뜨렸다. | [79]가 수치적인 초기값 문제를 다룬다고 추가했다. [90]–[92]의 part 1·2·3을 각각 추가했다. | PDF p.163 / 인쇄 155쪽. [79] “Numerical initial value problems in ordinary differential equations”. [90] “part 1. General theory”. [91] “part 2. Conservation theory”. [92] “part 3. Evaluation of energy flux”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.164 (보완) | [97]과 [98]에서 중력파 스펙트럼이라는 대상을 빠뜨렸다. [98]의 Part II 부제를 빠뜨렸다. | 중력파 스펙트럼이라는 대상과 파랑 모델 적용을 위한 매개변수화라는 부제를 추가했다. | PDF p.164 / 인쇄 156쪽. [97] “computing the non-linear transfer in a gravity-wave spectrum”. [98] “in a gravity wave spectrum. Part II: Parameterizations of the nonlinear transfer for application in wave models”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.165 (보완) | [109]와 [112]의 third-generation 한정을 빠뜨렸다. [116]의 적용 대상을 빠뜨렸다. | 3세대 파랑 모델이라는 한정과 스펙트럼 파랑 모델을 위한 방법이라는 대상을 추가했다. | PDF p.165 / 인쇄 157쪽. [109]와 [112] “verification of the third-generation wave model”. [116] “Phase-decoupled refraction-diffraction for spectral wave models”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.167 (정정) | [144]를 파랑 모델과 폭풍 해일 모델의 결합으로 적었다. | 폭풍 해일 모델 안에 파랑 모델을 결합한다는 방향을 복원했다. | PDF p.167 / 인쇄 159쪽. [144] “The dynamical coupling of a wave model in a storm surge model through the atmospheric boundary layer”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.167 (보완) | [138]의 스펙트럼 모델링과 [141]의 새로운 형태라는 표현을 빠뜨렸다. | [138]의 연구 방법과 [141]의 새 정식화 표현을 추가했다. | PDF p.167 / 인쇄 159쪽. [138] “Spectral modelling of ice-induced wave decay”. [141] “A new form of the Boussinesq equations with improved linear dispersion characteristics”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.168 (보완) | [154]–[156]을 합쳐 요약하면서 [154]의 실험 연구와 [155]의 수심 제한을 빠뜨렸다. | 각 문헌에 대응하는 제목 내용을 분리했다. 실험 연구와 수심 제한 조건을 추가했다. | PDF p.168 / 인쇄 160쪽. [154] “Design wave heights on very mild slopes: An experimental study”. [155] “Depth limited design wave heights in very flat regions”. [156] “Height limits in top down and bottom up wave environments”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.169 (보완) | [165]의 proposed 표현과 [166]의 이론 연구 한정을 빠뜨렸다. | 제안한 스펙트럼 형상이라는 표현과 이론 연구라는 한정을 추가했다. | PDF p.169 / 인쇄 161쪽. [165] “A proposed spectral form for fully developed wind seas”. [166] “eine theoretische Untersuchung”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.170 (보완) | [184]의 모델 세대·풍파 한정과 [187]의 적용 대상 모델을 빠뜨렸다. | [184]는 임의 규모의 3세대 풍파 모델로 적었다. [187]은 바람이 생성하는 표면파 모델의 입력·소산으로 한정했다. | PDF p.170 / 인쇄 162쪽. [184] “Diffusion reduction in a arbitrary scale third generation wind wave model”. [187] “in a model for wind-generated surface waves”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.171 (보완) | [199] 월파에 의한 파랑 투과 실험으로만 요약했다. [201] 2차원 격자 생성기로만 요약했다. | [199] 방파제가 파랑에 미치는 영향이라는 주제와 실내 실험이라는 한정을 보완했다. [201] quality라는 격자 생성기의 한정을 보완했다. | PDF p.171 / 인쇄 163쪽. 문헌 [199] “Effects of breakwaters on waves: laboratory tests of wave transmission by overtopping”. 문헌 [201] “a two-dimensional quality mesh generator”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.172 (보완) | [206] 준라그랑주 근사로만 요약했다. [212] 추정 지침으로만 요약했다. [216] 파랑 모델로만 요약했다. | [206] 한 부류라는 한정을 보완했다. [212] 간단한 지침이라는 한정을 보완했다. [216] 3세대 풍파 모델이라는 대상을 보완했다. | PDF p.172 / 인쇄 164쪽. 문헌 [206] “A class of semi-Lagrangian approximations for fluids”. 문헌 [212] “Simple guidelines”. 문헌 [216] “in a third-generation wind-wave model”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.174 (정정) | [245]–[246]을 합쳐 유한 진폭 파랑 이론과 불규칙 파랑에 의한 흐름으로 적었다. | [245]는 유한 진폭 파랑 이론에 기초한 수치 모델로 고쳤다. [246]은 불규칙 파랑에 의한 흐름의 수치 모델로 구분했다. | PDF p.174 / 인쇄 166쪽. 문헌 [245] “A numerical model of nearshore currents based on a finite amplitude wave theory”. 문헌 [246] “A numerical model of nearshore currents due to irregular waves”. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.175 (보완) | [247] 굴절 계산 모델로만 요약했다. [256] WAVEWATCH라는 이름만 적었다. | [247] 수치 모델이라는 한정을 보완했다. [256] 3세대 파랑 모델이라는 한정을 보완했다. | PDF p.175 / 인쇄 167쪽. 문헌 [247] “A numerical model for refraction computation”. 문헌 [256] “in the third-generation wave model WAVEWATCH”. |

이상 없음으로 집계한 행은 다음과 같다.

| 기록:구간 | 확인한 원문 |
|---|---|
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.155 | 인쇄 147쪽. §8.7과 식 (8.40)–(8.45)를 대조했다. 정상 상태와 생성항 부재 조건을 확인했다. |
| [p145-162.md](../manuals/pdfs/swantech.pdf/p145-162.md):p.156 | 인쇄 쪽 번호 148 외에 본문이 없는 쪽임을 확인했다. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.166 | 인쇄 158쪽. 문헌 [118]–[132]의 기록을 대조했다. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.173 | 인쇄 165쪽. 문헌 [218]–[231]의 기록을 대조했다. |
| [p163-176.md](../manuals/pdfs/swantech.pdf/p163-176.md):p.176 | 인쇄 168쪽. 문헌 [261]–[264]의 기록을 대조했다. 문헌 [264] 아래의 빈 영역을 확인했다. |

수정 전후의 두 기록을 비교하여 frontmatter가 같음을 확인했다.
쪽 행의 개수와 순서가 같음을 확인했다.
쪽 행 바깥의 내용이 같음을 확인했다.
변경 행의 끝에 해당 정정·보완 표식이 있는지 확인했다.
두 기록과 이 보고서만 수정했다.
모델은 실행하지 않았다.

정정 17, 보완 18, 이상 없음 5
