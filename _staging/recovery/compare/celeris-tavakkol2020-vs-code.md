# Tavakkol 2020 전체와 Celeris-WebGPU 코드 대조

## 1 요약

분류별 개수: 일치 29, A 43, B 12, C 37, D 4, E 2, F 8, H 44, X 0. 합계 179행이다. 이 수량은 2–4절의 고유 행 ID를 세었다. 일치가 아닌 행은 150행이다.

이 보고서는 AI가 작성한 원문 대조 기록이다. 논문의 원문과 이 보고서의 해석을 구분한다. 기준일은 2026-11-04이다.

현재 모드 1은 논문의 약비선형 확장 Boussinesq 계보와 B=1/15를 유지한다. 현재 기본 시간 적분은 AB3 예측과 AM4 보정이다. 현재 스펀지층은 논문의 식 (9)을 구현하지 않는다. 현재 코드는 논문에 없는 명시적 쇄파 경로를 기본으로 켠다. 해당 근거는 CP2-018–026·034–041과 5절의 이력 표에 있다.

논문 내부의 오기는 KP07 인용번호, 식 (11)의 수중 분모 부호, Fig. 15의 상대파고, 공통 셰이더 경로 표기에서 확인했다. 각 항목은 CP2-048·070·120·125이다. 현재 노트의 추가 오류는 4절에서 분리했다. 코드 결함 후보 두 항목은 CP2-155·156이다. 이 후보를 실행으로 확정하지 않았다.

논문은 Tavakkol & Lynett, *Computer Physics Communications* 248 (2020), 106966이다. 논문은 p.1에 온라인 공개일을 2019-09-28로 적는다. 논문은 Celeris Base의 Unity3D·C#·HLSL 구현을 설명한다. 이 보고서의 코드 기준은 `ebca435d02b258768e0352fbaf27404f2f135799`이다. 해당 커밋의 날짜는 2026-07-20이다. 이력의 첫 커밋은 `abb3875`이며 날짜는 2023-10-09이다. 따라서 현재 코드에서 Unity 클래스가 보이지 않는 사실만으로 논문 오기를 판정하지 않는다.

경로 약속: 아래의 코드 경로는 `models/Celeris/raw/source_code/Celeris-WebGPU/`를 기준으로 쓴다. 노트 경로는 저장소 루트를 기준으로 쓴다. 현재 코드 인용은 별도 표시가 없으면 `ebca435:파일:줄`이다. 과거 코드 인용은 `HASH:파일:줄`로 쓴다. 논문 원문 위치는 인쇄 쪽 번호를 따른다. `T20`은 `_staging/recovery/extract/Celeris/pdf-md/cel-tavakkol2020.md`를 뜻한다. 추출본의 줄은 본문 찾기에만 사용했다. 식과 그림 판정은 지정된 300 dpi 쪽 이미지를 직접 열어서 했다.

판정의 `일치`는 지정한 항목의 대응을 뜻한다. 코드 전체의 수치·물리 검증을 뜻하지 않는다. `불일치`에는 F 표기 차이도 포함한다. F는 식 변형으로 같은 의미를 확인한 경우이다. `코드에만`의 C는 이 논문이 해당 동작을 설명하지 않는다는 뜻이다. C는 과거 논문의 작성 의무 위반을 뜻하지 않는다. A는 이전 구현과 현재 구현의 차이이다. H는 코드로 진위를 판정할 대상이 아니다.

### 1.1 쪽별 확인 범위

| 쪽 | 직접 확인한 내용 | 대조 위치 |
|---|---|---|
| p.1 | 제목·날짜·초록·Program summary·서론 시작. 번호식·표·번호 그림 없음. | CP2-001–006 |
| p.2 | Advent와 Base의 구현 차이·배포 권고·수학 모형의 계보. 번호식·표·그림 없음. | CP2-007–012 |
| p.3 | 식 (1)–(4)·변수·계수·격자·시간 적분·쇄파·경계·Fig. 1. | CP2-013–033 |
| p.4 | 식 (5)–(9)·번호 없는 파속 관계·소스 구조·Unity 구조. 표·그림 없음. | CP2-034–045 |
| p.5 | Fig. 2·경계 UI·두 해석기·클래스 구조. 번호식·표 없음. | CP2-046–052 |
| p.6 | Fig. 3·pass1–3·삼중대각 해법·계산 셰이더·렌더 격자. 번호식·표 없음. | CP2-053–060, CP2-125 |
| p.7 | Fig. 4·Fig. 5·타일 수·UV·수면 변위·재질·색상표. 번호식·표 없음. | CP2-061–068 |
| p.8 | Fig. 6·식 (10)–(13)·지도 투영·줌·REST·지도 중첩. | CP2-069–080 |
| p.9 | Fig. 7·포인터 계측·부이·입출력 형식·컴파일 조건. 번호식·표 없음. | CP2-081–092 |
| p.10 | Fig. 8·Fig. 9·플랫폼별 텍스처 접근·빌드·실행·API 키·VR 소개. 번호식·표 없음. | CP2-093–099 |
| p.11 | Fig. 10·Fig. 11·VR 설정과 조종·검증 사례 조건. 번호식·표 없음. | CP2-100–109 |
| p.12 | Fig. 12·Fig. 13·검증 격자·시간 간격·경계·마찰·계측점·결론 시작. 번호식·표 없음. | CP2-110–118 |
| p.13 | Fig. 14·Fig. 15·결론·감사·문헌 [1]–[23]. 번호식·표 없음. | CP2-119–125 |
| p.14 | 문헌 [24]–[36]만 있음. 독립 본문·식·표·그림 없음. | CP2-126 |

14쪽 중 빈 쪽은 없다. 논문에는 번호식 (1)–(13)이 있다. 논문에는 Fig. 1–15가 있다. 논문에는 번호가 붙은 표가 없다. 이 수량은 위 쪽 이미지와 각 캡션에서 셌다. 그림의 화면 값은 기본값으로 취급하지 않는다.

### 1.2 원문 식 전사

다음 식은 논문 표기를 보존한다. 아래의 `z`는 바닥 표고이다. 코드의 `B_here`와 같은 물리량이다. 논문의 분산 계수 `B`와 혼동하지 않는다.

Tavakkol 2020 p.3 식 (1):

\[
\begin{bmatrix}h\\P\\Q\end{bmatrix}_t+
\begin{bmatrix}P\\P^2/h+gh^2/2\\PQ/h\end{bmatrix}_x+
\begin{bmatrix}Q\\PQ/h\\Q^2/h+gh^2/2\end{bmatrix}_y+
\begin{bmatrix}0\\ghz_x+\psi_1+f_1\\ghz_y+\psi_2+f_2\end{bmatrix}=0\tag{1}
\]

Tavakkol 2020 p.3 식 (2):

\[
\begin{aligned}
\psi_1={}&-\left(B+\frac13\right)d^2(P_{xxt}+Q_{xyt})-Bgd^3(\eta_{xxx}+\eta_{xyy})\\
&-dd_x\left(\frac13P_{xt}+\frac16Q_{yt}+2Bgd\eta_{xx}+Bgd\eta_{yy}\right)\\
&-dd_y\left(\frac16Q_{xt}+Bgd\eta_{xy}\right)
\end{aligned}\tag{2}
\]

Tavakkol 2020 p.3 식 (3):

\[
\begin{aligned}
\psi_2={}&-\left(B+\frac13\right)d^2(P_{xyt}+Q_{yyt})-Bgd^3(\eta_{yyy}+\eta_{xxy})\\
&-dd_y\left(\frac13Q_{yt}+\frac16P_{xt}+2Bgd\eta_{yy}+Bgd\eta_{xx}\right)\\
&-dd_x\left(\frac16P_{yt}+Bgd\eta_{xy}\right)
\end{aligned}\tag{3}
\]

Tavakkol 2020 p.3 식 (4):

\[
\gamma(\alpha)=\frac12\left(1+\cos\left(\pi\frac{L_s-D(\alpha)}{L_s}\right)\right)\tag{4}
\]

Tavakkol 2020 p.4 식 (5)–(9):

\[
\gamma(L_s-n\delta)=\prod_{i=0}^{n}\lambda(L_s-i\delta)\tag{5}
\]
\[
\gamma(L_s-n\delta)=\lambda(L_s-n\delta)\times\gamma(L_s-(n-1)\delta)\tag{6}
\]
\[
\lambda(L_s-n\delta)=\frac{\gamma(L_s-n\delta)}{\gamma(L_s-(n-1)\delta)}\tag{7}
\]
\[
\lambda(\alpha)=\frac{\gamma(\alpha)}{\gamma(\alpha+\delta)}\tag{8}
\]
\[
\lambda(\alpha)=\frac{\gamma(\alpha)}{\gamma(\alpha+c\Delta t)}\tag{9}
\]

Tavakkol 2020 p.8 식 (10):

\[
U=\frac{C-C_{\min}}{C_{\max}-C_{\min}};\quad V=0.5\tag{10}
\]

Tavakkol 2020 p.8 식 (11):

\[
\begin{cases}
U=\dfrac{C-C_{\min}}{C_{\min}},&C\leq0\\
U=\dfrac{C}{C_{\max}},&C>0
\end{cases};\quad V=0.5\tag{11}
\]

Tavakkol 2020 p.8 식 (12)–(13):

\[
M_x=\frac{lon}{\pi}\tag{12}
\]
\[
M_y=\frac1\pi\ln\left(\tan\left(\frac\pi4+\frac{lat}{2}\right)\right)\tag{13}
\]

식 (11)의 분모 `C_min`은 인쇄된 부호 그대로 옮겼다. CP2-070에서 별도로 판정한다.

## 2 대조 표

### 2.1 초록과 서론

| 행 ID | 항목 | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유와 분류 |
|---|---|---|---|---|---|
| CP2-001 | 구현 언어와 플랫폼 | p.1 “developed in the Unity3D game engine and in C# language”; “written in HLSL” | `js/Run_Compute_Shader.js:30` `export async function fetchShader(url) {`; `shaders/Pass1.wgsl:54` `@compute @workgroup_size(16, 16) //` | 불일치 | A. 논문은 2019 Base이다. 현재 구현은 JS 호스트와 WGSL이다. 이력 V1을 적용한다. |
| CP2-002 | GPU 계산과 혼합 해법 | p.1 “hybrid finite volume–finite difference method”; “solved on the GPU using compute shaders” | `js/Run_Compute_Shader.js:68` `computePass.dispatchWorkgroups(dispatchX, dispatchY);`; `shaders/Pass2.wgsl:38` `return (aplus * Fminus - aminus * Fplus + aplus * aminus * Udifference) / (aplus - aminus);` | 일치 | 공간 이산화와 GPU 계산의 역할이 대응한다. 셰이더 언어 일치는 CP2-001과 구분한다. |
| CP2-003 | VR 기능 | p.1 “view the simulations in a virtual reality headset” | 5절 검색 D1. 활성 호스트의 VR 세션 진입 코드는 검색되지 않았다. | 문서에만 | D. Base의 VR 지원을 WebGPU 지원으로 옮겨 쓰지 않는다. |
| CP2-004 | 360도 영상 | p.1 “360° video capturing”; p.2 “record a 360° video” | `js/File_Writer.js:346` `export async function createAndDownloadVideoFromTexture(device, texture, textureSize, outputPath='out.mp4', frameRate=24) {`; 5절 검색 D2 | 문서에만 | D. 일반 렌더 텍스처의 영상 저장은 360도 투영·촬영 구현의 증거가 아니다. |
| CP2-005 | 공개 배포와 라이선스 | p.1 “Program Files doi: http://dx.doi.org/10.17632/jdx7tddcxz.1”; “MIT License” | `README.md:82` ``This project is licensed under the **MIT License**. See the `LICENSE` file for details.`` | 불일치 | H. 별도 Base 배포물의 식별자이다. 라이선스 이름의 일치는 소스 파일 동일성을 뜻하지 않는다. |
| CP2-006 | 재해 사례와 모형 필요성 | p.1–2 “supercomputing facilities”; “Democratizing high-order and high-performance coastal wave modeling” | 해당 없음. 배경·목적 문장이다. | 불일치 | H. 재해 연도와 공학적 동기는 실행 코드 대조 대상이 아니다. |
| CP2-007 | Advent 구현 | p.2 “C++ and HLSL using the Direct3D framework” | `README.md:25` `Runs entirely client-side in the browser using JavaScript and WGSL shaders via the WebGPU API—no plugins or installations required.` | 불일치 | A. Advent·Base·WebGPU의 구현 판을 구별한다. V1을 적용한다. |
| CP2-008 | 이용 수와 예보 사이트 | p.2 “over 2000 times”; “50+ countries”; “five-day forecast” | 해당 없음. 이용 통계와 별도 서비스 사례이다. | 불일치 | H. 다운로드 수·예보 기간은 모델 함수·기본값이 아니다. |
| CP2-009 | Unity 물리 엔진 비사용 | p.2 “We did not use the physics engine of Unity3D” | `js/Run_Compute_Shader.js:61` `const computePass = commandEncoder.beginComputePass();` | 불일치 | A. Base의 엔진 선택 설명이다. 현재 코드도 자체 수치 셰이더를 구동하지만 Unity 프로젝트가 아니다. V1. |
| CP2-010 | 다형성·주입·모듈화 | p.2 “polymorphism, design patterns, dependency injection” | `js/main.js:23` `import { create_Pass1_BindGroupLayout, create_Pass1_BindGroup } from './Handler_Pass1.js';  // group bindings for Pass1 shaders` | 불일치 | A. JS 모듈·handler 구조를 Unity 클래스 설계와 동일시하지 않는다. V1. |
| CP2-011 | Base가 Advent를 대체하지 않는다는 권고 | p.2 “it is not meant to replace it”; “continue using Celeris Advent until new versions ...” | 해당 없음. 해당 시점의 이용 권고이다. | 불일치 | H. 권고의 조건과 시점을 유지한다. 최신 판 사용 권고로 바꾸지 않는다. |
| CP2-012 | 이론 계보와 타 모형 비교 | p.2–3 “both nonlinearity and frequency dispersion are weak”; “only weakly nonlinear”; FUNWAVE·COULWAVE·현장 불확실성 설명 | `js/constants_load_calc.js:36` `NLSW_or_Bous: 0,  // Choose 0 for Non-linear Shallow Water (NLSW), 1 for Madsen Boussinesq, 2 for Fully Non-linear Boussinesq (COULWAVE equations)` | 불일치 | H. 이론 가정·다른 모형의 사례·비용 주장은 코드 대조 대상이 아니다. 현재 모드 2를 2020 논문이 구현했다고 해석하지 않는다. |

### 2.2 지배 방정식과 수치 해법

| 행 ID | 항목 | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유와 분류 |
|---|---|---|---|---|---|
| CP2-013 | 식 (1)의 수심과 연속식 | p.3 식 (1), §1.2 전사. “h is the total water depth” | `shaders/Pass1.wgsl:78` `let h_here = in_here.x - B_here;`; `shaders/Pass3_Bous.wgsl:394` `let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term + vorticity_dissipation;` | 불일치 | F. 해석: 코드는 수면 표고를 저장한다. 고정 바닥이면 $h_t=\eta_t$이다. 추가 질량원은 3절에서 분리한다. |
| CP2-014 | 식 (1)의 이류 플럭스 | p.3 식 (1)의 $P,P^2/h,PQ/h,Q,Q^2/h$ | `shaders/Pass2.wgsl:122–127` 아래 인용 N1. | 일치 | $P=hu$, $Q=hv$를 넣으면 코드의 $hu^2$, $huv$가 대응한다. 수압항은 다음 행에서 분리한다. |
| CP2-015 | 식 (1)의 수압·바닥 경사·부호 | p.3 식 (1)의 $(gh^2/2)_x+ghz_x$ 및 y 성분 | `shaders/Pass3_Bous.wgsl:392` 아래 인용 N2. | 불일치 | F. 해석: $h=\eta-z$이면 $ghh_x+ghz_x=gh\eta_x$이다. 좌변 항을 우변으로 옮긴 코드는 `-globals.g * h_here * detadx`이다. 바닥 경사 부호 오류로 보지 않는다. |
| CP2-016 | 식 (1)의 마찰 | p.3 “f1 and f2 are the bottom friction terms” | `shaders/Pass3_Bous.wgsl:90` `f = f * sqrt(hu * hu + hv * hv) * divide_by_h2;`; `:392` N2의 `- in_state_here.y * friction_`와 z 성분 | 일치 | 논문은 마찰항의 역할만 정의한다. Manning·무차원 계수·얕은 수심 보정식은 적지 않는다. 그 세부는 CP2-132이다. |
| CP2-017 | 식 (2)–(3)의 수심·수위 기준 | p.3 “d is the still water depth”; “η ... measured from the still water surface elevation” | `shaders/Update_TriDiag_coef.wgsl:49` `let d_west = -textureLoad(txBottom, leftIdx, 0).z;`; `shaders/Pass3_Bous.wgsl:130` `let eta_here = in_state_here.x;` | 일치 | 정수면 기준을 0으로 둘 때 `d=-z`, `h=eta-z`이다. `base_depth`는 지역 `d`와 다르다. |
| CP2-018 | 식 (2)의 x 분산항 전체 | p.3 식 (2), §1.2 전사 | `shaders/Pass3_Bous.wgsl:269–273,282–283` N3. `shaders/Update_TriDiag_coef.wgsl:67–69` N4. | 불일치 | F. 해석: $P_t$의 x 방향 자기 미분은 삼중대각 연산자에 들어간다. $Q_t$ 혼합항은 `F_star`의 시간 차분에 들어간다. $Bgd^3$·$2Bgd^2d_x$·$Bgd^2d_y$의 부호는 $-\psi_1$로 우변에 옮긴 부호이다. 분산 차단 조건과 도함수 차수 변경은 CP2-023·134이다. |
| CP2-019 | 식 (3)의 y 분산항 전체 | p.3 식 (3), §1.2 전사 | `shaders/Pass3_Bous.wgsl:275–279,285–286` N3. `shaders/Update_TriDiag_coef.wgsl:101–103` N4. | 불일치 | F. 해석: $Q_t$의 y 방향 자기 미분은 y 삼중대각 연산자에 들어간다. $P_t$ 혼합항은 `G_star`에 들어간다. x/y 교환 뒤 $1/3,1/6,B$ 계수가 대응한다. |
| CP2-020 | 분산 계수 | p.3 번호 없는 식 $B=1/15$; Fig. 3의 `BCoef : float = 1/15` | `js/constants_load_calc.js:37` `Bcoef: 1.0 / 15.0,  // Dispersion parameter, 1/15 is optimum value for this set of equations.` | 일치 | 현재 모드 1의 기본 계수이다. 모드 2의 `Bous_alpha`에 적용하지 않는다. |
| CP2-021 | 계산 격자 | p.3 “uniform Cartesian grid”; “∆x × ∆y”; “cell centers and their corresponding cell averages” | `js/constants_load_calc.js:27–28` `dx: 1.0,  // Cell size in the x direction.` / `dy: 1.0,  // Cell size in the y direction.`; `shaders/Pass1.wgsl:57` `let idx = vec2<i32>(i32(id.x), i32(id.y));` | 일치 | 직교격자 경로에서 고정 간격의 셀 텍스처를 사용한다. 구면격자 경로는 CP2-129이다. |
| CP2-022 | 2차 KP07 FVM | p.3 “second-order well-balanced positivity preserving central-upwind scheme ... KP07” | `shaders/Pass1.wgsl:41–52` N5. `shaders/Pass2.wgsl:36–42` N6. | 일치 | 기본 `Accuracy_mode=0` 경로의 선형 재구성과 central-upwind 수치 플럭스가 대응한다. 양성 보존의 모든 실행 상태를 검증했다는 뜻은 아니다. |
| CP2-023 | 나머지 항의 2차 중앙차분 | p.3 “The rest of the terms are discretized using second order central FDM.” | `shaders/Pass3_Bous.wgsl:240` `// replace with 4th order when dispersion is included`; `:241–242` N7; `:262–266` N8 | 불일치 | A. 현재 코드는 분산 구간의 수면·수심 1차 미분에 4차 중앙차분을 사용한다. 2차·혼합 미분은 여전히 2차이다. V3. |
| CP2-024 | 시간 적분 차수와 선택 | p.3 “third-order fixed timestep Adams–Bashforth scheme” | `js/constants_load_calc.js:32` `timeScheme: 2,  // Time integration choices: 0: Euler, 1: 3rd-order A-B predictor, 2: A-B 4th-order predictor+corrector.`; `shaders/Pass3_Bous.wgsl:399–410` N9 | 불일치 | A. `timeScheme=1`의 예측식은 3차 AB이다. 기본 `2`는 별도 4차 Adams–Moulton 보정식을 실행한다. `0`은 Euler이다. V4. |
| CP2-025 | 고정 시간 간격 | p.3 “fixed timestep” | `js/constants_load_calc.js:486` `calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);` | 일치 | 초기화에서 정한 `dt`를 반복에 사용한다. GUI 매개변수 변경 시 재계산과 매 스텝 자동 적응을 구별한다. |
| CP2-026 | 직접 쇄파 처리의 부재 | p.3 “does not have a direct treatment for wave breaking” | `js/constants_load_calc.js:56` `useBreakingModel: 1, // inlcude breaking model when == 1`; `shaders/Pass3_Bous.wgsl:343–364` N10; `js/main.js:2652` `if(calc_constants.useBreakingModel == 1) {` | 불일치 | A. 현재 기본 경로는 명시적 쇄파 점성항을 포함한다. minmod 소산과 쇄파 모형을 같은 처리로 적지 않는다. V5. |
| CP2-027 | minmod 소산 | p.3 “numerical dissipation ... using a minmod limiter ... imitates the wave breaking” | `shaders/Pass1.wgsl:31–39` N5; `:46` `let dx_grad_over_two = 0.25 * MinMod(z1, z2, z3);` | 일치 | 제한자의 존재가 대응한다. 쇄파 재현 성능 주장은 논문의 수치 실험 주장이다. |
| CP2-028 | 두 층 ghost cell | p.3 “two layers of ghost cells at each side” | `shaders/BoundaryPass.wgsl:403–411` N11; `js/constants_load_calc.js:509` `calc_constants.boundary_shift =  4;` | 일치 | 서쪽 `idx.x<=1`은 두 ghost cell이다. `idx.x==2`는 법선 유량을 0으로 둔다. 동·남·북도 대응 분기가 있다. |
| CP2-029 | 네 종류 경계의 목록 | p.3 “fully reflective solid wall, sinewave maker, sponge layer, and irregular wavemaker” | `js/constants_load_calc.js:63–68`의 `*_boundary_type`, `incident_wave_type`; `shaders/BoundaryPass.wgsl:448–455` N12 | 불일치 | A. 현재 코드는 경계 유형과 입사파 유형을 분리한다. 사인파와 불규칙파는 주로 경계 유형 2 아래의 분기이다. 추가 경계는 CP2-135이다. V6. |
| CP2-030 | 벽·사인파 기능 | p.3 “implementations of solid walls and sinewave maker are explained in [3]” | `shaders/BoundaryPass.wgsl:101` `return vec4<f32>(in_state_real.r, in_state_real.g, -in_state_real.b, in_state_real.a);`; `:453` `BCState = BoundarySineWave(idx, iBC, jBC, current_boundary);` | 일치 | 벽의 법선 유량 반전과 입사파 함수 호출을 확인했다. 논문에 없는 파형 계수는 이 문장에서 추출하지 않는다. |
| CP2-031 | 불규칙 조파의 외부 설명 | p.3 “the irregular wavemaker is discussed in [24]” | `js/File_Loader.js:290` `const numberOfWaves = parseInt(lines[0].split(' ')[1], 10);`; `:292` `const waveData = lines.slice(2).map(line => line.trim().split(/\s+/).map(Number));` | 불일치 | H. 이 문장은 해법을 [24]로 위임한다. [24]의 계수와 스펙트럼 공식을 이 논문의 직접 설명으로 취급하지 않는다. |
| CP2-032 | 네 변의 GUI·파일 지정 | p.3 “any of the four boundaries ... either from the GUI or from the input file” | `js/constants_load_calc.js:63–66`의 네 경계 기본값; `js/constants_load_calc.js:438` `var configJson = JSON.parse(configContent);` | 일치 | 경계별 독립 설정과 파일 로딩의 역할이 대응한다. XML과 JSON 형식 차이는 CP2-087이다. |
| CP2-033 | Fig. 1 | p.3 “Diagram of γ(α), Eq. (4), inside the sponge layer.” | 해당 없음. 식 (4)의 그래프이다. | 불일치 | H. 가로축 $D(\alpha)/L_s$는 0–1이다. 세로축 $\gamma(\alpha)$는 0–1이다. 왼쪽 끝 0과 오른쪽 끝 1을 확인했다. 현재 감쇠식의 그래프로 바꿔 부르지 않는다. |

### 2.3 스펀지층 변경과 소프트웨어 구조의 시작

| 행 ID | 항목 | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유와 분류 |
|---|---|---|---|---|---|
| CP2-034 | 식 (4)의 감쇠와 적용 대상 | p.3 식 (4), §1.2 전사. “multiplying the values of η, P, and Q”; “only ... inside the sponge layer” | `shaders/BoundaryPass.wgsl:104–108` N13; `:360–366` N14 | 불일치 | A. 현재 감쇠식에는 바깥 계수 `0.5`와 지수 `0.005`가 있다. `dt`·파속·감쇠 비율은 없다. 네 번째 채널도 곱한다. 폭은 미터 `Ls`가 아니라 `BoundaryWidth` 격자점 수이다. V2. |
| CP2-035 | Advent v1.0.0의 반복 감쇠 문제 | p.3–4 “every time-step”; “higher for smaller timesteps”; $H_0$, $\gamma(L_s-\delta)$, $\gamma(L_s-2\delta)$ | `shaders/BoundaryPass.wgsl:105` N13의 감쇠식 | 불일치 | H. 논문은 과거 Advent 실험의 불필요한 반사와 시간 간격 의존성을 설명한다. 현재 코드에서도 `dt` 없는 반복 감쇠를 확인했지만 같은 반사량을 단정하지 않는다. |
| CP2-036 | 식 (5)의 누적곱 | p.4 식 (5), §1.2 전사 | 직접 코드 대응 없음. | 불일치 | H. 목표 감쇠를 만드는 계수의 수학적 정의이다. $i=0$에서 시작하는 곱을 그대로 유지한다. |
| CP2-037 | 식 (6)의 재귀식 | p.4 식 (6), §1.2 전사 | 직접 코드 대응 없음. | 불일치 | H. 식 (5)의 한 인자를 분리한 관계이다. 현재 셰이더 호출 순서로 해석하지 않는다. |
| CP2-038 | 식 (7)의 비율식 | p.4 식 (7), §1.2 전사 | 직접 코드 대응 없음. | 불일치 | H. 분모는 직전 위치의 목표 감쇠이다. 현재 코드의 `pow`와 같은 식이 아니다. |
| CP2-039 | 식 (8)의 변수 치환 | p.4 식 (8), §1.2 전사. “Substituting Ls − nδ ... α” | 직접 코드 대응 없음. | 불일치 | H. $\alpha=L_s-n\delta$를 넣으면 분모는 $\gamma(\alpha+\delta)$이다. 부호를 빼기로 바꾸지 않는다. |
| CP2-040 | 식 (9)의 실제 감쇠 | p.4 식 (9), §1.2 전사. $\delta$는 $\Delta t$ 동안 마루가 진행한 거리이다. | `shaders/BoundaryPass.wgsl:105,111,117,123` N13과 5절 V2 | 불일치 | A. 현재 네 감쇠 함수는 $\gamma(\alpha)/\gamma(\alpha+c\Delta t)$를 계산하지 않는다. V2는 2023년의 다른 감쇠식을 보여 준다. |
| CP2-041 | 감쇠 파속 근사 | p.4 번호 없는 식 $c=\sqrt{gd}$; “at each time-step” | `shaders/BoundaryPass.wgsl:104–125`의 네 감쇠 함수에는 `c`, `dt`, `d`를 사용하는 감쇠 계산이 없다. | 불일치 | A. 조파 함수의 파속 계산과 스펀지 감쇠 계산을 구별한다. 이력 V2. |
| CP2-042 | Assets와 진입 파일 | p.4 “Assets ... Celeris”; “GameManager.cs”; “Main.unity” | `js/main.js:23`의 JS 모듈 import; `README.md:61` ``Open `http://localhost:8000` in a WebGPU-enabled browser. No build step required—just refresh after code changes.`` | 불일치 | A. 현재 진입점은 HTML과 JS이다. Unity scene을 열라는 지침은 Base용이다. V1. |
| CP2-043 | 해석기 상속 관계 | p.4 “TL17Driver.cs”; “KP07Driver.cs”; “KP07Base.cs”; “Solver.cs”; “virtual ... TimeStep()” | `js/main.js:2679`의 `Pass3_Pipeline_Bous` 호출; `:2682`의 `Pass3_Pipeline_NLSW` 호출 | 불일치 | A. 현재는 모드 분기와 공통 패스이다. Unity 상속 계층을 현재 파일 구조로 인용하지 않는다. V1. |
| CP2-044 | 계산 셰이더 include와 렌더 파일 | p.4 “TL17.compute and KP07.compute”; “base_KP07.compute”; “time_integration.compute, tools.compute”; “.shader ... .cginc ... Material” | `js/main.js:1564` `var Pass3_ShaderCode_Bous = await fetchShader('/shaders/Pass3_Bous.wgsl');` | 불일치 | A. WGSL 파일별 pipeline 구성이 HLSL include 체계를 대신한다. 남아 있는 `.compute` 확장자만으로 이 체계가 유지된다고 보지 않는다. V1. |
| CP2-045 | Unity 오브젝트와 프레임 갱신 | p.4 “Main Camera, GameManager, Engine, and Canvas”; “singleton”; “Instance”; “Update”; “over 140,000”; “Unity3D 2018 ... Visual Studio 2018” | `js/main.js:1685` `const gridWidth = calc_constants.WIDTH;  // Number of vertices along the width`; `README.md:61`의 브라우저 진입 | 불일치 | A. 현재 코드는 DOM·JS·WebGPU 렌더 루프를 사용한다. `Canvas` GameObject와 HTML canvas를 동일 객체로 부르지 않는다. Unity 도구 버전·YAML 행 수는 Base 구조 설명이다. V1. |

### 2.4 수치 코드 원문 인용

**N1. `shaders/Pass2.wgsl:122–127` 원문**

```wgsl
    let xflux = vec4<f32>(
        NumericalFlux(aplus, aminus, hW_east * uW_east, h_here.y * u_here.y, mass_diff_x),
        NumericalFlux(aplus, aminus, hW_east * uW_east * uW_east, h_here.y * u_here.y * u_here.y, P_diff_x),
        NumericalFlux(aplus, aminus, hW_east * uW_east * vW_east, h_here.y * u_here.y * v_here.y, Q_diff_x),
        NumericalFlux(aplus, aminus, hW_east * uW_east * cW_east, h_here.y * u_here.y * c_here.y, phix * (hW_east * cW_east - h_here.y * c_here.y))
    );
```

**N2. `shaders/Pass3_Bous.wgsl:392–394` 원문**

```wgsl
    let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + breaking_y + (Psi1y + Psi2y) + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);

    let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term + vorticity_dissipation;
```

**N3. `shaders/Pass3_Bous.wgsl:269–286` 원문**

```wgsl
        F_star = (1.0 / 6.0) * d_here * 
            (dd_by_dx * (0.5 * globals.one_over_dy) * (v_up - v_down) + 
            dd_by_dy * (0.5 * globals.one_over_dx) * (v_right - v_left)) + 
            (globals.Bcoef + 1.0 / 3.0) * d2_here * (globals.one_over_dxdy * 0.25) * 
            (v_up_right- v_down_right - v_up_left + v_down_left);

        G_star = (1.0 / 6.0) * d_here * 
            (dd_by_dx * (0.5 * globals.one_over_dy) * (u_up - u_down) + 
            dd_by_dy * (0.5 * globals.one_over_dx) * (u_right - u_left)) + 
            (globals.Bcoef + 1.0 / 3.0) * d2_here * (globals.one_over_dxdy * 0.25) * 
            (u_up_right - u_down_right - u_up_left + u_down_left);

        
        Psi1x = globals.Bcoef_g * d3_here * ((eta_right_right - 2.0 * eta_right + 2.0 * eta_left - eta_left_left) * (0.5 * globals.one_over_d3x) + (eta_up_right - eta_up_left - 2.0 * eta_right + 2.0 * eta_left + eta_down_right - eta_down_left) * (0.5 * globals.one_over_dx * globals.one_over_d2y));
        Psi2x = globals.Bcoef_g * d2_here * (dd_by_dx * (2.0 * eta_by_dx_dx + eta_by_dy_dy) + dd_by_dy * eta_by_dx_dy) + (F_star - F_G_star_oldOldies.y) / globals.dt * 0.5;

        Psi1y = globals.Bcoef_g * d3_here * ((eta_up_up - 2.0 * eta_up + 2.0 * eta_down - eta_down_down) * (0.5 * globals.one_over_d3y) + (eta_up_right + eta_up_left - 2.0 * eta_up + 2.0 * eta_down - eta_down_right - eta_down_left) * (0.5 * globals.one_over_dx * globals.one_over_d2x));
        Psi2y = globals.Bcoef_g * d2_here * (dd_by_dy * (2.0 * eta_by_dy_dy + eta_by_dx_dx) + dd_by_dx * eta_by_dx_dy) + (G_star - F_G_star_oldOldies.z) / globals.dt * 0.5;
```

**N4. `shaders/Update_TriDiag_coef.wgsl:67–69` 원문**

```wgsl
            a =  d_here * d_dx / (6.0 * globals.dx) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dx * globals.dx);
            b = 1.0 + 2.0 * (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dx * globals.dx);
            c = -d_here * d_dx / (6.0 * globals.dx) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dx * globals.dx);
```

**N4. `shaders/Update_TriDiag_coef.wgsl:101–103` 원문**

```wgsl
            a =  d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
            b = 1.0 + 2.0 * (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
            c = -d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
```

**N5. `shaders/Pass1.wgsl:31–52` 원문**

```wgsl
fn MinMod(a: f32, b: f32, c: f32) -> f32 {
    if (a > 0.0 && b > 0.0 && c > 0.0) {
        return min(min(a, b), c);
    } else if (a < 0.0 && b < 0.0 && c < 0.0) {
        return max(max(a, b), c);
    } else {
        return 0.0;
    }
}

fn Reconstruct(west: f32, here: f32, east: f32, TWO_THETAc: f32) -> vec2<f32> {
    let z1 = TWO_THETAc * (here - west);
    let z2 = (east - west);
    let z3 = TWO_THETAc * (east - here);

    let dx_grad_over_two = 0.25 * MinMod(z1, z2, z3);

    let out_east = here + dx_grad_over_two;
    let out_west = here - dx_grad_over_two;

    return vec2(out_west, out_east);
}
```

**N6. `shaders/Pass2.wgsl:36–42` 원문**

```wgsl
fn NumericalFlux(aplus: f32, aminus: f32, Fplus: f32, Fminus: f32, Udifference: f32) -> f32 {
    if (aplus - aminus != 0.0) {
        return (aplus * Fminus - aminus * Fplus + aplus * aminus * Udifference) / (aplus - aminus);
    } else {
        return 0.0;
    }
}
```

**N7. `shaders/Pass3_Bous.wgsl:240–242` 원문**

```wgsl
    // replace with 4th order when dispersion is included
        detadx = 1.0 / 12.0 * (eta_left_left - 8.0 * eta_left + 8.0 * eta_right - eta_right_right) * globals.one_over_dx;
        detady = 1.0 / 12.0 * (eta_down_down - 8.0 * eta_down + 8.0 * eta_up - eta_up_up) * globals.one_over_dy;
```

**N8. `shaders/Pass3_Bous.wgsl:262–266` 원문**

```wgsl
        let dd_by_dx = (-d_right_right + 8.0 * d_right - 8.0 * d_left + d_left_left) * globals.one_over_dx / 12.0;
        let dd_by_dy = (-d_up_up + 8.0 * d_up - 8.0 * d_down + d_down_down) * globals.one_over_dy / 12.0;
        let eta_by_dx_dy = 0.25 * globals.one_over_dx * globals.one_over_dy * (eta_up_right - eta_down_right - eta_up_left + eta_down_left);
        let eta_by_dx_dx = globals.one_over_d2x * (eta_right - 2.0 * eta_here + eta_left);
        let eta_by_dy_dy = globals.one_over_d2y * (eta_up - 2.0 * eta_here + eta_down);
```

**N9. `shaders/Pass3_Bous.wgsl:399–410` 원문**

```wgsl
    if (globals.timeScheme == 0) {
        newState = in_state_here_UV + globals.dt * d_by_dt;

    } else if (globals.pred_or_corrector == 1) {

        newState = in_state_here_UV + globals.dt / 12.0 * (23.0 * d_by_dt - 16.0 * oldies + 5.0 * oldOldies);

    } else if (globals.pred_or_corrector == 2) {

        let predicted = textureLoad(predictedGradients, idx, 0);
        newState = in_state_here_UV + globals.dt / 24.0 * (9.0 * d_by_dt + 19.0 * predicted - 5.0 * oldies + oldOldies);
    }
```

**N10. `shaders/Pass3_Bous.wgsl:343–364` 원문**

```wgsl
    if(globals.useBreakingModel == 1) {
        breaking_B = textureLoad(txBreaking, idx, 0).z;  // breaking front parameter, non-breaking [0 - 1] breaking

        let nu_flux_here = textureLoad(txDissipationFlux, idx, 0);
        let nu_flux_right = textureLoad(txDissipationFlux, rightIdx, 0);
        let nu_flux_left = textureLoad(txDissipationFlux, leftIdx, 0);
        let nu_flux_up = textureLoad(txDissipationFlux, upIdx, 0);
        let nu_flux_down = textureLoad(txDissipationFlux, downIdx, 0);

        let dPdxx = 0.5 * (nu_flux_right.x - nu_flux_left.x) * globals.one_over_dx;
        let dPdyx = 0.5 * (nu_flux_right.y - nu_flux_left.y) * globals.one_over_dx;
        let dPdyy = 0.5 * (nu_flux_up.y - nu_flux_down.y) * globals.one_over_dy;

        let dQdxx = 0.5 * (nu_flux_right.z - nu_flux_left.z) * globals.one_over_dx;
        let dQdxy = 0.5 * (nu_flux_up.z - nu_flux_down.z) * globals.one_over_dy;
        let dQdyy = 0.5 * (nu_flux_up.w - nu_flux_down.w) * globals.one_over_dy;
        
        if (near_dry > 0.){
            breaking_x = dPdxx + 0.5 * dPdyy + 0.5 * dQdxy;
            breaking_y = dQdyy + 0.5 * dPdyx + 0.5 * dQdxx;
        }
    }
```

**N11. `shaders/BoundaryPass.wgsl:403–411` 원문**

```wgsl
    if (globals.west_boundary_type <= 1) {
        if (idx.x <= 1) {
            BCState = WestBoundarySolid(idx);
            BCState_Sed = zero;
        } else if (idx.x == 2) {
            BCState.y = 0.0;
            BCState_Sed = zero;
        }
    }
```

**N12. `shaders/BoundaryPass.wgsl:448–455` 원문**

```wgsl
    if (globals.west_boundary_type == 2 && idx.x <= 2) {
        if (globals.incident_wave_type <= 2) { // Sine Waves
            let iBC = 1;
            let jBC = 1;
            let current_boundary = 1;
            BCState = BoundarySineWave(idx, iBC, jBC, current_boundary);
            BCState_Sed = zero;
        } else if (globals.incident_wave_type == 3) {  // solitary wave
```

**N13. `shaders/BoundaryPass.wgsl:104–125` 원문**

```wgsl
fn WestBoundarySponge(idx: vec2<i32>) -> vec4<f32> {
    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - idx.x) + 2.0) / f32(globals.BoundaryWidth - 1))), 0.005);
    let new_state = textureLoad(txState, idx, 0);
    return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
}

fn EastBoundarySponge(idx: vec2<i32>, B_here: f32) -> vec4<f32> {
    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - globals.boundary_nx - idx.x)) / f32(globals.BoundaryWidth - 1))), 0.005);
    let new_state = textureLoad(txState, idx, 0);
    return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
}

fn SouthBoundarySponge(idx: vec2<i32>) -> vec4<f32> {
    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - idx.y) + 2.0) / f32(globals.BoundaryWidth - 1))), 0.005);
    let new_state = textureLoad(txState, idx, 0);
    return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
}

fn NorthBoundarySponge(idx: vec2<i32>) -> vec4<f32> {
    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - globals.boundary_ny - idx.y)) / f32(globals.BoundaryWidth - 1))), 0.005);
    let new_state = textureLoad(txState, idx, 0);
    return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
```

**N14. `shaders/BoundaryPass.wgsl:360–366` 원문**

```wgsl
    if (globals.west_boundary_type == 1 && idx.x <= 2 + globals.BoundaryWidth) {
        let s = f32(globals.BoundaryWidth + 2 - idx.x) / f32(globals.BoundaryWidth);
        let state_w = WestBoundarySponge(idx);
        state_sum  = state_sum + s * state_w;
        weight_sum = weight_sum + s;
        BCState_Sed = zero;
    }
```

### 2.5 해석기 클래스와 렌더 구조

| 행 ID | 항목 | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유와 분류 |
|---|---|---|---|---|---|
| CP2-046 | 경계 UI 연결 | p.5 “BoundaryPanelScript”; “takes the values ... from the GUI and updates the simulation parameters” | `river.html:728` `<select id="west_boundary_type-select" name="west_boundary_typeValue">`; `js/main.js:4767` `{ input: 'useBreakingModel-select', property: 'useBreakingModel' },` | 불일치 | A. 입력을 모델 설정으로 연결하는 역할은 이어진다. 연결 단위는 Unity Component에서 DOM event로 바뀌었다. V1. |
| CP2-047 | NLSW와 TL17의 구분 | p.5 “two fluid dynamics models”; “KP07”; “TL17” | `js/constants_load_calc.js:36`의 `0`, `1`, `2` 선택문 원문은 CP2-012에 인용했다. | 불일치 | A. 현재 모드는 NLSW·Madsen Boussinesq·완전비선형 COULWAVE의 세 종류이다. 논문이 세 번째 모드를 설명한다고 쓰지 않는다. V7. |
| CP2-048 | KP07 인용번호 | p.5 “Kurganov and Petrova (2007) [21]” | p.13 [20] `A. Kurganov, G. Petrova, Commun. Math. Sci. 5 (2007) 133–160.`; [21]은 Shi et al. (2012)이다. | 불일치 | B. 같은 논문 p.3의 KP07 설명은 [20]을 쓴다. p.5의 [21]은 [20]으로 고친다. 코드 판 차이로 설명할 수 없다. |
| CP2-049 | Solver의 책임·가상 함수 | p.5 “does not implement the functions to solve any equations”; “virtual TimeStep()” | `js/Run_Compute_Shader.js:55` `export function runComputeShader_EncStack(device, commandEncoder, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {` | 불일치 | A. 현재 공통 GPU 구동 함수는 상속의 가상 메서드가 아니다. V1. |
| CP2-050 | 텍스처 생성·수명 관리 | p.5 “simTextureManager ... creating and destroying ... to prevent memory leaks” | `js/Create_Textures.js:3` `const texture = device.createTexture({`; `:10` `allTextures.add(texture);` | 불일치 | A. 현재 구현은 JS의 텍스처 생성 함수와 추적 집합을 사용한다. `RenderTexture` 또는 `TextureFactory` 클래스의 존재를 주장하지 않는다. V1. |
| CP2-051 | 공통 이류 처리 | p.5–6 “KP07Base ... shared functions”; “pass1 and pass2” | `js/main.js:2641`의 `Pass1_Pipeline` 호출과 `:2649`의 `Pass2_Pipeline` 호출은 모드별 pass3 분기보다 앞에 있다. | 일치 | 기본 경로는 재구성과 수치 플럭스를 공유한다. 클래스 이름의 일치는 CP2-043에서 별도로 부정했다. |
| CP2-052 | Fig. 2의 파일과 경로 | p.5 Fig. 2 “Some of the important source files”; `CML Examples`, `Materials`, `Prefabs`, `Scripts`, `GPGPU`, `Mouse`, `Solvers`, `Scenes`, `Textures`, `Third Party` | `ARCHITECTURE.md:3` ``The source files in `js/` and `shaders/` are the application.`` | 불일치 | A. 그림의 CML·CBF, Buoy prefab, ReadCBF·ReadCML·SimSetting·Singleton, MapManager, PointerGauge, IrregularWaves·KernelLookUp, HLSL 공통 파일, Main.unity는 Base 구조이다. 자산·외부 라이브러리 내부는 판독하지 않았다. V1. |
| CP2-053 | Fig. 3의 UML | p.6 Fig. 3 “Class UML diagram”; `Solver → KP07Base → KP07Driver/TL17Driver`; `Setup`, `TimeStep`, `logToFile`, `updateTexturesForRender`, `ABC`, `BCoef` | `js/Run_Tridiag_Solver.js:3` `export function runTridiagSolver(`; `js/Create_Textures.js:2` `export function create_2D_Texture(device, width, height, allTextures) {` | 불일치 | A. 그림은 상속·접근 제어·클래스 멤버를 설명한다. 현재 모듈 간 호출 관계로 재사용할 수 없다. 그림의 B 계수는 CP2-020과 일치한다. V1. |
| CP2-054 | pass1·pass2 역할 | p.6 “reconstructing physical values and computing fluxes at cell interfaces” | `shaders/Pass1.wgsl:48–49` `let out_east = here + dx_grad_over_two;` / `let out_west = here - dx_grad_over_two;`; `shaders/Pass2.wgsl:38` N6 | 일치 | 셀 중심 값에서 면 상태를 만들고 면 플럭스를 계산한다. `txH/U/V`의 채널은 방위별 면이다. |
| CP2-055 | NLSW pass3과 시간 적분 | p.6 “pass3 ... sums up the fluxes and source terms”; “then a time integration method” | `js/main.js:2682`의 `Pass3_Pipeline_NLSW` 호출; `shaders/Pass3_Bous.wgsl:394–409` N2·N9는 대응하는 Boussinesq 경로이다. | 불일치 | A. 현재 pass3 셰이더가 RHS 조립과 시간 적분을 함께 수행한다. CPU의 별도 가상 시간 적분 함수가 아니다. V1·V4. |
| CP2-056 | TL17 pass3과 분산항 | p.6 “aggregates the results from pass2 with source and dispersive terms” | `shaders/Pass3_Bous.wgsl:392–394` N2 | 일치 | 플럭스 발산·중력·마찰·분산항을 RHS에서 합한다. 추가 물리는 3절에 나눈다. |
| CP2-057 | 삼중대각 cyclic reduction | p.6 “solve the tridiagonal matrices using the cyclic reduction algorithm” | `js/Run_Tridiag_Solver.js:48–50` `for (let p = 0; p < calc_constants.Px; p++) {` / 빈 줄 / `let s = 1 << p;`; `:73–75` y 반복도 같은 형태 | 일치 | x와 y를 나누어 간격을 두 배로 늘리는 PCR을 실행한다. NLSW는 `:37–39`에서 복사로 우회한다. |
| CP2-058 | CPU 수치 해법 비사용 | p.6 “drivers to run compute shaders on the GPU, and do not implement any CPU solutions” | `js/Run_Compute_Shader.js:61–68` `beginComputePass`, `setPipeline`, `setBindGroup`, `dispatchWorkgroups` | 일치 | JS는 호스트 구동을 맡는다. 설정·입력 파싱·readback이 CPU에서 수행되는 사실은 이 진술과 모순되지 않는다. |
| CP2-059 | compute Dispatch | p.6 “driving ... simply done with ... Dispatch”; “DirectCompute”; “CUDA” | `js/Run_Compute_Shader.js:68` `computePass.dispatchWorkgroups(dispatchX, dispatchY);` | 불일치 | A. 계산 전용 GPU 호출의 목적은 같다. Unity `Dispatch`와 WebGPU API의 호출 규약은 다르다. CUDA와의 유사성은 기술 배경이다. V1. |
| CP2-060 | Unity heightmap과 외부 렌더 도구 | p.6 “only takes square shapes”; “Surface Waves by Code Animo”; “commercial library” | 해당 없음. Unity와 외부 라이브러리의 제약·선택 설명이다. | 불일치 | H. 라이브러리 내부를 모델 완료 조건으로 삼지 않는다. |
| CP2-061 | 128×128 타일 | p.6 “square grids of size 128 × 128”; “scale up ... in one direction” | `js/main.js:1685–1686` `const gridWidth = calc_constants.WIDTH;  // Number of vertices along the width` / `const gridHeight = calc_constants.HEIGHT; // Number of vertices along the height` | 불일치 | A. 현재 3D 격자는 전체 WIDTH·HEIGHT로 만든다. 128 크기 타일 묶음이 아니다. V8. |
| CP2-062 | 타일 수 반올림과 최솟값 | p.7 “rounding ... nearest integer”; “at least two tiles in each direction” | `js/main.js:1690–1700`의 전체 grid strip 생성. `:1694` `for (let x = 0; x < gridWidth; x++) {` | 불일치 | A. 현재 3D 격자 생성에는 `round(nx/128)`·방향별 최소 두 타일 규칙이 없다. V8. |
| CP2-063 | 계산 격자와 렌더 격자의 UV 연결 | p.7 “not a 1:1 match”; “linear UV mapping ... sampling the compute textures” | `shaders/vertex3D.wgsl:75` `out.uv = v.pos * 0.5 + 0.5;`; `:78` `var elev = textureLoad(etaTexture, vec2<i32>(i32(out.uv.x * f32(globals.WIDTH - 1)), i32(out.uv.y * f32(globals.HEIGHT - 1))), 0).r;` | 불일치 | A. 현재도 UV를 사용한다. 현재 3D 격자는 WIDTH·HEIGHT의 texel 위치를 직접 읽는다. Base 타일링의 격자 불일치 설명을 그대로 적용하지 않는다. V8. |
| CP2-064 | Fig. 4 | p.7 “Rendering infrastructure ... disassembled tiles” | `js/main.js:1695–1696`의 두 strip 정점 추가문 | 불일치 | A. 그림은 Base 타일을 분리한 구조도이다. 축·물리 단위·정량 검증 곡선은 없다. 현재 strip 생성의 그림이 아니다. V8. |
| CP2-065 | Fig. 5 | p.7 “grid (a), jet colormapping (b), and terrain colormapping (c)” | `shaders/fragment.wgsl:165` `} else if(colorMap_choice == 1) {  // parula colormap`; `:183` `} else if(colorMap_choice == 2) {  // turbo colormap`; `:255` `}  else if(colorMap_choice == 6) {  // haxby for bathy/topo colormap` | 불일치 | A. 그림은 격자·jet·수중/육상 색상 띠이다. 현재 코드의 수치 RGB 배열은 이 텍스처 세 장을 그대로 읽는 구조가 아니다. 자산 파일은 열지 않았다. V1. |
| CP2-066 | 정점 셰이더의 수면 변위 | p.7 “vertex shaders to displace the mesh points every frame”; “water surface elevation” | `shaders/vertex3D.wgsl:82` `let worldZ = elev * globals.renderZScale;`; `:84` `out.clip_position = globals.viewProj * vec4<f32>(worldX, worldY, worldZ, 1.0);` | 일치 | 수면 텍스처를 높이로 사용한다. 시각화 수직 배율은 해석 수위와 구분한다. |
| CP2-067 | photorealistic.shader와 격자 재질 | p.7 “SimpleWater.mat”; “light and skybox reflection”; “grid texture ... sampled, scaled, color reversed” | `shaders/fragment.wgsl:730` `color_rgb = light_effects * color_wave;` | 불일치 | A. 현재 수면 색 계산은 WGSL이다. Unity 재질·텍스처 기반 격자 처리와 파일명을 동일시하지 않는다. skybox 전용 셰이더는 열지 않았다. V1. |
| CP2-068 | WaterColormap·TerrainColormap | p.7 “WaterColormap.shader”; “TerrainColormap.shader”; “a colormapped texture ... as an input” | `shaders/fragment.wgsl:598` `let lowerIndex = i32(floor(wavePosition * 15.0)); // Because we have 16 colors.`; `:605` `let color_wave = mix(colorMap[lowerIndex], colorMap[upperIndex], mixAmount);` | 불일치 | A. 현재는 RGB 배열의 이웃 원소를 보간한다. 텍스처의 V=0.5 단면을 샘플하는 체계와 다르다. V1. |

### 2.6 색상식과 지도

| 행 ID | 항목 | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유와 분류 |
|---|---|---|---|---|---|
| CP2-069 | 식 (10)의 정규화 | p.8 식 (10), §1.2 전사. “any value between 0 and 1 can be used for V” | `shaders/fragment.wgsl:591` `var wavePosition = f32((render_surface - minWave) / (maxWave - minWave));` | 불일치 | F. 해석: $C=render\_surface$, $C_{min}=minWave$, $C_{max}=maxWave$이면 같은 정규화이다. 현재 색상 배열에는 V 좌표가 필요하지 않다. 추가 clamp는 CP2-147이다. |
| CP2-070 | 식 (11)의 수중 분모 | p.8 식 (11)의 $U=(C-C_{\min})/C_{\min}$, $C\leq0$ | 비교 근거는 같은 쪽의 0–1 UV 설명과 Fig. 5c이다. 현재 `shaders/fragment.wgsl:586` `color_rgb = vec3<f32>(210.0 / 255.0, 180.0 / 255.0, 140.0 / 255.0) + 0.25 * (bottom - globals.bathy_cmap_zero) / globals.base_depth;`는 다른 색식이다. | 불일치 | B. $C_{min}<0$일 때 인쇄식은 $C=C_{min}$에서 0, $C=0$에서 −1을 준다. 0–1 색상 띠로 보내는 설명과 모순된다. 분모 부호를 자동 수정하여 인용하지 않는다. Base 실제 구현의 보정 여부는 이 코드로 주장하지 않는다. |
| CP2-071 | Fig. 6 | p.8 “four snapshots stitched to each other”; “different sky and grid options” | 해당 없음. Base 렌더 결과의 사례 그림이다. | 불일치 | H. 서로 다른 하늘 두 종류와 격자 표시 조합을 확인했다. 축·범례·정량 성능 자료는 없다. |
| CP2-072 | 지도 위치 입력 | p.8 “latitude and longitude of the center ... given in the CML input file” | `js/File_Loader.js:545` `function calculateZoomLevel(lat_LL, lon_LL, lat_UR, lon_UR, maxWidth, maxHeight) {` | 불일치 | A. 현재 지도 API는 좌하단·우상단 좌표를 인자로 받는다. 중심점과 미터 폭에서 모서리를 계산하는 CML 입력과 다르다. V9. |
| CP2-073 | REST·위성 기본 지도 | p.8 “REST request”; “By default ... satellite imagery map”; “configured ... other kinds” | `js/File_Loader.js:597` `const url = new URL('https://maps.googleapis.com/maps/api/staticmap');`; `:603` `url.searchParams.set('maptype', 'satellite');` | 일치 | REST 요청과 위성 종류의 하드코딩을 확인했다. 다른 maptype은 코드 변경 가능성과 GUI 옵션을 구별한다. |
| CP2-074 | 식 (12)의 경도 정규화 | p.8 식 (12), §1.2 전사. `lon`의 단위는 radians | `js/File_Loader.js:572` `var lngFraction = lngDiff / 360;` | 불일치 | F. 해석: 코드의 `lngDiff`는 도 단위 차이다. $\Delta lon/(2\pi)=\Delta M_x/2=\Delta lon_{deg}/360$이다. 절대좌표가 아니라 지도 폭 비율에 해당한다. |
| CP2-075 | 식 (13)의 위도 투영 | p.8 식 (13), §1.2 전사 | `js/File_Loader.js:685–689` 아래 지도 원문 M1 | 불일치 | F. 해석: $\ln[(1+\sin lat)/(1-\sin lat)]=2\ln\tan(\pi/4+lat/2)$이다. 코드의 $y=(1-M_y)/2$는 원점·방향·범위를 바꾼 같은 Mercator 투영이다. |
| CP2-076 | 극점 절단 | p.8 번호 없는 관계 $M_y=\pm1$; “±85.051129°” | `js/File_Loader.js:551–553` `var sin = Math.sin(lat * Math.PI / 180);` / `var radX2 = Math.log((1 + sin) / (1 - sin)) / 2;` / `return Math.max(Math.min(radX2, Math.PI), -Math.PI) / 2;` | 불일치 | F. 해석: 줌 계산은 투영 좌표를 ±π로 제한한 뒤 반으로 나눈다. 지도 UV의 M1 함수에는 같은 clamp가 없다. 모든 함수가 위도를 잘라 준다고 일반화하지 않는다. |
| CP2-077 | 줌의 타일 수 | p.8 번호 없는 관계 $2^{zoom}$, $zoom=0$, $zoom=2$, $2^2\times2^2=16$ | `js/File_Loader.js:558` `return Math.floor(Math.log(mapPx / worldPx / fraction) / Math.LN2);` | 불일치 | H. 타일 수 관계는 지도 API의 수학적 배경이다. 수치해석 격자 수를 뜻하지 않는다. 정수 줌의 계산은 CP2-078이다. |
| CP2-078 | 모서리·줌 역계산 | p.8 “haversine formula ... distances in meters ... to lon and lat”; “covers the entire simulation field” | `js/File_Loader.js:577–583` 아래 M2 | 불일치 | A. 현재 코드는 주어진 모서리의 위도·경도 범위와 256픽셀 세계 타일 크기로 줌을 구한다. 최대 줌은 21이다. Haversine으로 영역 모서리를 만드는 절차가 아니다. V9. |
| CP2-079 | 지도와 영역의 선형 UV | p.8 “four parameters (two in each direction)”; “image ... larger than the simulation domain” | `js/File_Loader.js:704` `let scaleY = targetMercatorHeight / fullMercatorHeight;`; `:708` `let offsetY = (lowerYTarget - lowerYActual) / fullMercatorHeight;`; `:713–714` x scale·offset 계산 | 일치 | 영역과 이미지의 상대 크기·시작점을 x/y 각각 두 값으로 연결한다. 반환값만으로 투영 오차가 없다고 주장하지 않는다. |
| CP2-080 | GoogleStaticMap·Lean Go Maps | p.8 “part of a Unity3D asset, Lean Go Maps”; MIT; 외부 저장소 주소 | 해당 없음. 외부 자산과 배포 설명이다. | 불일치 | H. 외부 라이브러리 내부와 서비스 구현은 판독 범위 밖이다. 현재 호스트 대응은 CP2-072·073·078이다. |

**M1. `js/File_Loader.js:685–689` 원문**

```javascript
    function project(lat) {
        const sin = Math.sin(lat * Math.PI / 180);
        const y = 0.5 - Math.log((1 + sin) / (1 - sin)) / (4 * Math.PI);
        return y;
    }
```

**M2. `js/File_Loader.js:577–583` 원문**

```javascript
    var latZoom = zoom(maxHeight, WORLD_DIM.height, latFraction);
    var lngZoom = zoom(maxWidth, WORLD_DIM.width, lngFraction);

    // Return the minimum between calculated latitudinal and longitudinal zooms (to fit both),
    // and also make sure it does not exceed the maximum zoom level allowed.

    return Math.min(latZoom, lngZoom, ZOOM_MAX);
```

### 2.7 사용자 상호작용과 입출력

| 행 ID | 항목 | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유와 분류 |
|---|---|---|---|---|---|
| CP2-081 | Fig. 7 | p.9 “Geographic map of the coast of Newport, OR” | 해당 없음. Base가 받은 지도 사례이다. | 불일치 | H. 지도에는 Google·Imagery ©2018 TerraMetrics 표기가 있다. 수치 축·격자 간격·정량 검증 자료는 없다. |
| CP2-082 | 포인터의 ray–수평면 교점 | p.9 “casts a ray”; “intersection ... with a horizontal plane ... mean sea-level” | `js/main.js:4536–4537` `const normalizedX = (x - bounds.left) / bounds.width; //normalizedX;` / `const normalizedY = 1.0 - (y - bounds.top) / bounds.height; //normalizedY;`; `:4543–4544` 아래 U1 | 불일치 | A. 현재 tooltip은 canvas 위치를 정규화하여 텍스처 index를 정한다. ray와 정수면 교점을 계산하는 절차가 아니다. V10. |
| CP2-083 | 포인터 위치 오차 설명 | p.9 “flow parameters always correspond to the gauge location, even if ... not precisely under the mouse pointer”; “computationally expensive” | 해당 없음. Base 위치 추정의 오차·계산비용 설명이다. | 불일치 | H. 실제 수면 교점과 평균 수면 교점이 다르다는 조건을 유지한다. 현재 3D 탐색의 정확도를 이 문장으로 검증하지 않는다. |
| CP2-084 | GetPixel readback | p.9 “reads the flow data from the textures using the GetPixel method” | `js/Time_Series.js:86` `await buffer.mapAsync(GPUMapMode.READ);`; `:90` `const bufferCopy = new Float32Array(arrayBuffer.slice(0, bytesPerPixel * (calc_constants.NumberOfTimeSeries + 1)));` | 불일치 | A. 현재는 추출 compute pass 뒤 GPU buffer를 비동기 readback한다. Unity GetPixel 호출이 아니다. V10. |
| CP2-085 | 실시간 수위 곡선 | p.9 “values read from the GPU ... plugged into a third party plotter” | `js/main.js:5393` `data: location.eta,`; `:5401–5402` `const timeseriesChart = new Chart(ctx, {` / `type: 'line',` | 일치 | GPU 계측 수위가 화면 곡선으로 연결된다. 외부 플로터 라이브러리 내부는 읽지 않았다. |
| CP2-086 | 부이 개수·배치·삭제 | p.9 “A maximum of five”; “clicking on the scene”; “plotter legend ... Ctrl” | `js/constants_load_calc.js:262` `maxNumberOfTimeSeries: 16, // max number of time series allowed, inlcuding tooltip, if greater than 16, need to update readToolTipTextureData bytesperrow.  SHould be 16*N time series`; `index.html:1023` `<select id="NumberOfTimeSeries-select" name="NumberOfTimeSeriesValue">`; `index.html:1085`의 위치 입력 label | 불일치 | A. 현재 texture slot 0은 tooltip이다. 계측점의 UI 상한은 15이다. 개수 선택·좌표 변경 방식과 Base의 최대 다섯 부이·Ctrl 삭제를 동일시하지 않는다. V10. |
| CP2-087 | XML CML 설정 | p.9 “XML file ... input CML file” | `js/constants_load_calc.js:438` `var configJson = JSON.parse(configContent);`; `:424–425` `loadedConfig = await response.json();` / `calc_constants = { ...calc_constants, ...loadedConfig };` | 불일치 | A. 현재 설정은 JSON이다. CML tag 이름을 현재 매개변수 키로 추측하지 않는다. V1·V11. |
| CP2-088 | CBF header | p.9 “CBF file starts with tags which determine the resolution” | `js/File_Loader.js:39–41` `for (let y = 0; y < calc_constants.HEIGHT; y++) {` / `// Split each line by spaces or tabs.` / `const depthValues = lines[y].split(/\s+/).filter(Boolean);` | 불일치 | A. 현재 loader는 첫 줄부터 숫자 행으로 읽는다. CBF 해상도 tag를 처리하지 않는다. V11. |
| CP2-089 | 표고 행렬의 행 방향 | p.9 “each row corresponds to the z value ... a row of the solution field” | `js/File_Loader.js:48–54` 아래 U2 | 일치 | 파일의 y번째 행을 x 방향 숫자들로 읽어 `bathy2D[x][y]`에 넣는다. 행·열 전치를 무시하지 않는다. |
| CP2-090 | 수심 격자 보간 | p.9 “If ... resolutions ... are different ... use interpolation” | `js/File_Loader.js:43–46` 아래 U3 | 불일치 | A. 현재 loader는 행의 원소 수가 WIDTH와 다르면 `null`을 반환한다. 다른 크기의 bathy를 자동 보간하는 Base 절차가 아니다. V11. |
| CP2-091 | Advent와 같은 출력 형식 | p.9 “same format for input and output files as in Celeris Advent” | `js/Time_Series.js:166` ``headers += `Time${i+1}\tEta${i+1}\tP${i+1}\tQ${i+1}\t`;``; `js/File_Writer.js:560` ``let filename = `elev_${frame_count_output}.bin`;`` | 불일치 | A. Tavakkol 2017 PDF p.6(인쇄 p.122)는 formatted ASCII 출력을 명시한다. 현재의 텍스트 시계열·float32 binary와 Base의 형식 승계 문장을 구별한다. 2020 논문은 출력 layout·주기·정밀도의 상세를 인쇄하지 않았다. V11. |
| CP2-092 | 플랫폼 지원의 한계 | p.9 “not a guarantee ... all ... platforms”; “early stages ... Linux”; “expect” | 해당 없음. Base의 개발 환경·시험 이력·전망이다. | 불일치 | H. Linux 지원을 무조건 보장한다는 문장으로 바꾸지 않는다. 현재 브라우저 실행은 확인하지 않았다. |
| CP2-093 | Fig. 8 | p.10 “Simulation of the coast of Newport, OR ... geographic map” | `shaders/fragment.wgsl:284` `let GoogleMap = textureSample(txOverlayMap, textureSampler, uv_mod).rgb;` | 불일치 | H. 그림은 Base 지도 중첩 사례이다. 축과 정량 검증값은 없다. 현재 지도 텍스처 샘플의 존재는 그림과 같은 출력 재현을 뜻하지 않는다. |
| CP2-094 | Fig. 9의 포인터 표시 | p.10 “Mouse pointer acts as a gauge”; X 1583.5190, Y 6027.1930, Z −17.7326, Eta 0.3306, U 0.2338, V −0.0225 | `shaders/ExtractTimeSeries.wgsl:53` `output = vec4<f32>(bottom, waves, hsig, friction);`; `js/main.js:4586`의 `sig wave height (m)` tooltip | 불일치 | A. Base 화면은 X/Y/Z/Eta/U/V를 표시한다. 현재 기본 tooltip의 네 값은 바닥·수면·유의파고·마찰이다. 화면의 여섯 숫자는 기본값이 아니다. 그림 자체는 단위를 인쇄하지 않는다. V10. |
| CP2-095 | 텍스처 범위 밖 접근의 플랫폼 차이 | p.10 “DirectX ... returning zero”; “may cause a crash”; “must be found and removed” | 해당 없음. 다른 플랫폼으로 이식할 때의 외부 API 동작·의무 설명이다. | 불일치 | H. 이 문장을 현재 WGSL의 모든 범위 밖 접근이 안전하다는 근거로 쓰지 않는다. |
| CP2-096 | Unity Windows 빌드 절차 | p.10 “File > Build Setting”; “PC, Mac & Linux Standalone”; “target platform ... Windows” | `README.md:61`의 “No build step required” | 불일치 | H. 외부 도구 사용법이다. Base 빌드 절차를 WebGPU 실행 지침으로 쓰지 않는다. |
| CP2-097 | 실행 파일·setting.init·파일 탐색기 | p.10 “running the executable file”; “setting.init”; “if a path ... is not provided ... file browser” | `index.html:1597` `<script type="module" src="js/main.js"></script>`; `js/constants_load_calc.js:419` `const filePath = calc_constants.exampleDirs[calc_constants.run_example] + 'config.json';` | 불일치 | A. 현재는 HTML 모듈과 업로드/예제 설정 경로이다. 실행 파일 옆의 setting.init을 우선 읽는 절차가 아니다. V1·V11. |
| CP2-098 | 지도 API 키 제공 위치 | p.10 “API key must be provided in the GoogleStaticMap.cs file” | `js/File_Loader.js:605` `url.searchParams.set('key', apiKey);` | 불일치 | A. 현재 요청 생성은 JS 함수이다. Base의 C# 파일명은 현재 API 키의 위치 안내로 사용할 수 없다. 키 값은 보고서에 인용하지 않는다. V9. |
| CP2-099 | VR의 일반적 동작과 기대 효과 | p.10–11 “in accordance with user’s real time movement”; 가상 박물관·항만·교육 수조의 예 | 해당 없음. 기술 정의와 가능한 적용 시나리오이다. | 불일치 | H. 제안된 가상 실험실을 실제 구현된 협업 기능으로 바꾸어 쓰지 않는다. |

**U1. `js/main.js:4543–4548` 원문**

```javascript
        calc_constants.mouse_current_canvas_indX = Math.round(normalizedX * calc_constants.WIDTH);
        calc_constants.mouse_current_canvas_indY = Math.round(normalizedY * calc_constants.HEIGHT);

        // Use WebGPU to read the data at (canvasX, canvasY)
        x_position = normalizedX * calc_constants.WIDTH * calc_constants.dx;
        y_position = normalizedY * calc_constants.HEIGHT * calc_constants.dy;
```

**U2. `js/File_Loader.js:48–55` 원문**

```javascript
        for (let x = 0; x < calc_constants.WIDTH; x++) {
            const parsedValue = parseFloat(depthValues[x]);
            if (isNaN(parsedValue)) {
                console.error(`Could not parse bathytopo value at [${x}, ${y}] in bathytopo file at ${filePath}`);
                return null;
            }
            bathy2D[x][y] = parsedValue;
        }
```

**U3. `js/File_Loader.js:43–46` 원문**

```javascript
        if (depthValues.length !== calc_constants.WIDTH) {
            console.error("Bathytopo file at " + filePath + " is not in the correct format.");
            return null;
        }
```

### 2.8 VR·검증 사례·결론·참고문헌

| 행 ID | 항목 | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유와 분류 |
|---|---|---|---|---|---|
| CP2-100 | Fig. 10 | p.11 “Deploying virtual buoys in Celeris Base.” | `js/main.js:5419` `text: 'Time (s)'`; `:5425` `text: 'Elevation (m)'` | 불일치 | H. Base 그림은 부이와 색별 곡선을 함께 보여 준다. 그림의 세로 눈금은 −1–1이다. 그림은 축 이름·단위를 인쇄하지 않는다. 현재 플로터의 단위를 그림 원문에 소급하지 않는다. |
| CP2-101 | Oculus Rift 대상 | p.11 “targeted ... Oculus Rift headsets”; “as of 2019” | 검색 D1. VR API와 headset 구현은 범위 내 소스·이력에서 검색되지 않았다. | 문서에만 | D. 2019년 장치 평가와 현재 브라우저 지원을 구별한다. CP2-003의 세부 대상이다. |
| CP2-102 | VR 활성화 설정 | p.11 “Edit > Project Settings > Player”; “checking a checkbox” | 해당 없음. Unity 편집기 조작이다. | 불일치 | H. 외부 도구 사용법이다. VR 이동·상호작용에는 추가 작업이 필요하다는 다음 문장의 조건을 유지한다. |
| CP2-103 | VR 통합과 외부 도구 | p.11 “there still is need for some development and integration efforts”; “ready to use libraries and Unity assets” | 해당 없음. 개발 작업·외부 도구의 설명이다. | 불일치 | H. 체크박스 한 번으로 이동·상호작용까지 완성된다고 요약하지 않는다. |
| CP2-104 | VR 이동·회전 조종 | p.11 “left controller ... move”; “right ... rotate”; “physically rotating” | 검색 D1. `js/main.js:4259` `} else if (event.button === 0 && event.ctrlKey && calc_constants.viewType == 2) {`는 마우스 탐색 분기이다. | 문서에만 | D. 키보드·마우스·touch의 3D 탐색은 Rift 양손 컨트롤러 구현의 증거가 아니다. |
| CP2-105 | Fig. 11 | p.11 “Movement control in Celeris VR.” | 해당 없음. 장치 조작 그림이다. | 불일치 | H. 왼손 Planar Move·Move Fast·Move Up·Move Down과 오른손 Rotate Left/Right를 확인했다. 외부 장치 사용법으로 분류한다. |
| CP2-106 | 선행 연구·개발 시간·현장감 주장 | p.11 “to the best of our knowledge”; “no prior work”; “could have taken”; “unique experience” | 해당 없음. 저자의 인지 범위·반사실적 추정·체험 주장이다. | 불일치 | H. 한정어를 삭제하지 않는다. GPU 코드 존재만으로 최초성·시간 절감량을 판정하지 않는다. |
| CP2-107 | Celeris VR 공개와 외부 라이선스 | p.11 “MIT License”; “external libraries ... their own licenses” | 해당 없음. Base 위에 만든 별도 배포물의 라이선스 설명이다. | 불일치 | H. 모든 외부 라이브러리가 MIT라는 문장으로 바꾸지 않는다. |
| CP2-108 | 원뿔섬 실험의 기하와 수조 | p.11 “7.2 m base diameter and side slope”; “30 m x 25 m”; “0.32 m depth” | 해당 없음. `examples/`는 사용자 지정 판독 제외 범위이다. | 불일치 | H. 실험 조건이다. 원문은 side slope 뒤의 수치를 인쇄하지 않았다. 이 보고서는 외부 실험의 경사를 보충하지 않는다. |
| CP2-109 | 목표 상대파고와 선택 이유 | p.11 번호 없는 식 $H/d=0.20$; “only simulate ... higher non-linearity and wave breaking ... expected ... more challenging” | 해당 없음. 사례 선택과 목표 조건이다. | 불일치 | H. 목표값을 실제 투입 상대파고 0.18과 구별한다. 파고·수심 비는 무차원이다. |
| CP2-110 | Fig. 12 | p.12 “Simulating a coastal area with Celeris VR.” | 해당 없음. VR 사용 사례 사진이다. | 불일치 | H. 헤드셋·두 조종기·투사 화면과 두 부이 곡선을 확인했다. 성능 축과 수치 검증 지표는 없다. |
| CP2-111 | Fig. 13의 기하·계측점 | p.12 “Experimental setup ... wave approaches ... from the left”; 원 지름 7.2 m·4.64 m·2.20 m | 해당 없음. 실험 배치 그림이다. | 불일치 | H. x·y 축 단위는 m이다. 초기 해안선은 점선 원이다. #6·#9는 전면, #16은 측면, #22는 후면이다. 그림에서 추정한 좌표를 입력 파일의 정확한 좌표로 쓰지 않는다. |
| CP2-112 | 수치 영역과 초기조건 | p.11–12 “30 m × 30 m”; “island in the center”; “solitary wave ... initial condition near ... west boundary” | `shaders/AddDisturbance.wgsl`의 고립파 기능은 별도이다. 사례 입력 파일은 열지 않았다. | 불일치 | H. 실험 수조 30×25 m와 수치 영역 30×30 m를 구별한다. 현재 일반 기본 영역을 30×30 m라고 쓰지 않는다. |
| CP2-113 | 검증 사례 경계 | p.12 “west and east ... sponge”; “north and south ... fully reflective solid walls” | `js/constants_load_calc.js:63–66`의 일반 기본 경계는 모두 0이다. | 불일치 | H. 논문은 특정 검증 사례의 경계를 정했다. 현재 일반 기본값과 달라도 코드 결함이 아니다. |
| CP2-114 | 검증 사례 격자 | p.12 “301 × 301 cells” | `js/constants_load_calc.js:23–24` `WIDTH: 800,  // Width of the computational domain.` / `HEIGHT: 600,  // Height of the computational domain.` | 불일치 | H. 사례의 계산 셀 수이다. $\Delta x=30/301$ 또는 $30/300$ 중 하나를 이 문장만으로 추가 확정하지 않는다. ghost 포함 여부도 추가하지 않는다. |
| CP2-115 | 검증 사례 시간 간격 | p.12 “a timestep of 0.0025 s” | `js/constants_load_calc.js:486`의 `dt` 산식은 CP2-025에 인용했다. | 불일치 | H. 0.0025 s는 이 사례의 값이다. 현재 전체 모형의 고정 기본값이 아니다. |
| CP2-116 | 검증 사례 무마찰 | p.12 “Bottom friction is not applied.” | `js/constants_load_calc.js:46` `friction: 0.000,  // Dimensionless friction coefficient, or Mannings 'n', depending on isManning choice.` | 불일치 | H. 사례 설정이다. 현재 기본값이 0이어도 모든 업로드 마찰맵이 꺼진다는 뜻은 아니다. |
| CP2-117 | 실제 상대파고 | p.12 번호 없는 식 $H/d=0.18$; “slightly smaller”; “closer ... downstream of the wavemaker”; [12,36,35] | 해당 없음. 사례 조건과 선택 근거이다. | 불일치 | H. 목표값 0.20을 0.18로 바꾼 이유를 유지한다. 해석: $d=0.32$ m와 결합하면 $H=0.0576$ m이다. 이 값은 계산한 값이며 원문 인쇄값이 아니다. |
| CP2-118 | 도달파·수위 하강·처오름의 예측 | p.12 “initial waveheight and subsequent drawdown ... well”; “identical ... Advent” | 해당 없음. 저자가 제시한 수치 검증 결과이다. | 불일치 | H. 검증 범위는 이 사례이다. 현재 WebGPU의 모든 모드·격자·쇄파 설정의 정확도로 승계하지 않는다. |
| CP2-119 | Fig. 14의 시계열 | p.13 캡션의 번호 없는 식 $H/d=0.18$; “Experimental (– –) and numerical (–)”; #6·#9·#16·#22 (a–d) | `shaders/ExtractTimeSeries.wgsl:60` `output = vec4<f32>(globals.time, waves, P, Q);` | 불일치 | H. 가로축은 t (s), 세로축은 η (m)이다. 시간 눈금은 8–20 s이다. 수위 범위는 −0.1–0.1 m이다. 붉은 파선과 푸른 실선의 후속 진동에는 차이가 보인다. 현재 시계열 export가 이 그림을 재현했다고 주장하지 않는다. |
| CP2-120 | Fig. 15 상대파고 | p.13 “maximum horizontal run-up for H/d = 0.018” | 같은 논문 p.12의 $H/d=0.18$와 p.13 Fig. 14의 $H/d=0.18$ | 불일치 | B. 같은 사례의 본문·인접 그림과 소수점 한 자리 차이가 난다. 노트는 “캡션은 0.018로 인쇄되었으나 본문 조건은 0.18”로 적는다. |
| CP2-121 | Fig. 15 처오름 축·기호 | p.13 “Numerical (solid line) and measured (•)”; 극좌표 눈금 | 해당 없음. 실험 비교 그림이다. | 불일치 | H. 각도 눈금은 30도 간격이다. 반지름 눈금은 0.2·0.4·0.6·0.8·1이다. 그림은 반지름의 단위·정규화 정의를 적지 않는다. 원자료 없는 오차 수치와 단위를 보충하지 않는다. |
| CP2-122 | 결론의 구현 요약 | p.12–13 “implemented in Unity3D using C# and HLSL”; “compiled version”; 지도·몰입형 환경 | `ARCHITECTURE.md:3`의 정적 브라우저 앱 설명 | 불일치 | A. 결론도 Base 구현을 요약한다. 현재 브라우저 구현의 직접 사용설명서로 인용하지 않는다. V1. |
| CP2-123 | 결론의 혼합 해법·compute shader | p.13 “hybrid finite volume–finite difference scheme and implemented on GPU” | `js/Run_Compute_Shader.js:68` `computePass.dispatchWorkgroups(dispatchX, dispatchY);`; N3·N6 | 일치 | FVM·FDM·GPU라는 수치 구조 계보는 이어진다. 특정 시간 스킴·스펀지식까지 같다는 주장은 포함하지 않는다. |
| CP2-124 | 감사·후원 | p.13 “ONR ... N00014-17-1-2878”; 익명 심사자 감사 | 해당 없음. 연구 후원·감사 문장이다. | 불일치 | H. 후원 과제 번호는 수치 설정이 아니다. |
| CP2-125 | 공통 셰이더 경로와 문헌 목록 | p.6 `Assets/Celeris/Scripts/Solver/Shared`; p.5 Fig. 2 `Solvers`; p.13 [1]–[23] | 같은 논문의 경로 표기를 대조했다. 현재 WGSL 파일 경로와는 별개이다. | 불일치 | B. 본문의 단수 `Solver`와 그림의 복수 `Solvers`는 같은 공통 폴더 설명에서 충돌한다. 문헌 [1]–[23]은 서지이며 별도 알고리즘 본문이 아니다. KP07 인용번호 오류는 CP2-048에서 분리했다. |
| CP2-126 | p.14의 참고문헌 [24]–[36] | p.14 [24] Tavakkol & Lynett (2016); [27]–[28] VR 발표; [29] arXiv:1909.04153; [33] Briggs et al. (1995); [35] Fuhrman & Madsen (2008); [36] Tonelli & Petti (2010) | 해당 없음. 이 쪽은 참고문헌만 싣는다. | 불일치 | H. [25]–[26]은 VR 배경이다. [30]–[32]는 독립 적용 연구이다. [34]는 Titov & Synolakis (1998)이다. 문헌 제목·서지로 현재 적응 시간 적분 또는 실험 경사를 확정하지 않는다. |

## 3 코드에만 있는 처리

이 절은 2020 논문의 식·해석기·설정·경계·입출력·상호작용 설명에 대응하는 현재 코드의 추가 처리를 기록한다. 논문에 없는 기본값은 논문 권고값으로 부르지 않는다. 실험 사례 폴더와 외부 라이브러리 내부는 판독하지 않았다. 표의 C는 이 논문에 대한 누락이다. 이미 2절에서 A로 분류한 구현 차이는 해당 행을 참조한다.

### 3.1 설정과 해석기

| 행 ID | 항목 | 문서 위치와 원문 | 코드 위치와 원문 | 판정 | 이유와 분류 |
|---|---|---|---|---|---|
| CP2-127 | 일반 기본값 | p.3은 격자·중력·제한자의 의미를 설명한다. 일반 기본값을 적지 않는다. | `js/constants_load_calc.js:23–28` WIDTH=800, HEIGHT=600, dx=1.0, dy=1.0 원문은 CP2-021·114에 인용했다. `:42` `g: 9.80665,  // Gravitational constant.`; `:44` `base_depth: 20.0,  // characteristic_depth (m), used to estimate time step, use depth in area of wave generation, or expected largest depth in domain.` | 코드에만 | C. `Courant_num=0.15`, `Theta=2.0`도 현재 기본값이다(`:31,45`). `base_depth`는 시간 간격 추정용 대표 수심이다. 지역 정수심 `d_here`와 구별한다. |
| CP2-128 | 완전비선형 COULWAVE | p.2는 COULWAVE를 다른 모형의 사례로 든다. Base 구현 모드로 정의하지 않는다. | `js/constants_load_calc.js:38` `Bous_alpha: -0.531,  // extended Boussinesq (Nwogu) parameter,`; `js/main.js:1553–1554` `const Pass3A_Coulwave_ShaderCode= await fetchShader('/shaders/Pass3A_COULWAVE.wgsl')` / `const Pass3B_Coulwave_ShaderCode= await fetchShader('/shaders/Pass3B_COULWAVE.wgsl')` | 코드에만 | C. 모드 2는 보조항 패스와 별도 비선형 삼중대각 계수를 사용한다. 2020 식 (2)–(3)을 모드 2의 전체 방정식으로 쓰지 않는다. |
| CP2-129 | 구면격자와 지원 강제 제한 | p.3은 uniform Cartesian grid를 설명한다. | `js/constants_load_calc.js:20` `grid_type: 1, // right now spherical when =2, otherwise cartesian`; `:53` `R_earth: 6371000.0,  // radius of earth, only used for spherical coordinate system`; `:455–470` 아래 C1 | 코드에만 | C. 구면격자는 NLSW만 허용한다. 구면격자는 Accuracy_mode·퇴적물·쇄파를 꺼 준다. 구면 `dt`는 위도별 물리 격자 간격의 최솟값으로 계산한다(`:475–484`). |
| CP2-130 | 고차 FVM 경로 | p.3은 2차 KP07을 설명한다. | `js/constants_load_calc.js:39` `Accuracy_mode: 0,  // Accuracy model choice: 0: 2nd-order, 1: 4th-order.`; `js/main.js:1539–1551` 아래 C2 | 코드에만 | C. `Accuracy_mode==1`은 Pass1_HighOrder와 Pass2_HighOrder_HLLC를 선택한다. 파일이 존재한다는 이유로 다른 HLLEM 경로도 자동 선택된다고 쓰지 않는다. |
| CP2-131 | 명시적 쇄파의 계수·조건·점성 상한 | p.3은 직접 쇄파 처리가 없다고 적는다. | `js/constants_load_calc.js:57–60` `delta_breaking: 2.0,  // eddy viscosity coefficient` / `T_star_coef: 5.0,  // defines length of time until breaking becomes fully developed` / `dzdt_I_coef: 0.50,  // start breaking parameter` / `dzdt_F_coef: 0.15,  // end breaking parameter`; `shaders/Pass_Breaking.wgsl:100–125` 아래 C3 | 코드에만 | C. 발생·종료 문턱은 $\sqrt{gh}$로 스케일한다. 발달 시간은 $\sqrt{h/g}$로 스케일한다. 점성은 `dx*dy/dt`로 제한한다. `:129`의 Smagorinsky 점성은 `0.0`이다. 주석 속 미완성 식을 활성 식으로 옮기지 않는다. |
| CP2-132 | 마찰 법칙·마찰맵·정밀도 보정 | p.3은 $f_1,f_2$를 바닥마찰항이라고만 정의한다. | `shaders/Pass3_Bous.wgsl:67–93` 아래 C4; `:302` `let friction_here = max(globals.friction, textureLoad(txBottomFriction, idx, 0).x);` | 코드에만 | C. `isManning==1`은 $gn^2h^{-1/3}$를 사용한다. 나머지는 무차원 계수이다. 계수 상한은 0.5이다. `h_scaled^4`와 `1.e-6`은 얕은 수심의 단정도 보정이다. 마찰맵은 전역값과 최댓값을 취한다. |
| CP2-133 | 건조 셀 검사·경사 교정 | p.3의 일반 양성 보존 설명에는 이 조건이 없다. | `js/constants_load_calc.js:501–502` `calc_constants.delta = Math.min(calc_constants.min_allowable_depth,calc_constants.base_depth / 5000.0);` / `calc_constants.epsilon = Math.pow(calc_constants.delta, 2);`; `shaders/Pass3_Bous.wgsl:142–151` 아래 C5 | 코드에만 | C. 주위 네 셀도 건조하면 상태·도함수·분산 helper를 0으로 쓰고 반환한다. 해안선에서는 수면 경사를 한쪽 차분 또는 0으로 바꾼다(`:366–385`). |
| CP2-134 | 분산항의 적용 조건과 항등 행렬 | p.3 식 (2)–(3)은 이 실행 조건을 인쇄하지 않는다. | `shaders/Pass3_Bous.wgsl:192–193` `if (near_dry > 0. && periodic_bc_fix < 0)` / `{ // only proceed if not near an initially dry cell`; `shaders/Update_TriDiag_coef.wgsl:42–46` 아래 C6 | 코드에만 | C. 초기 건조 인접 셀과 주기 경계 보정 구간에서 분산 계산을 억제한다. 삼중대각 계수는 경계·건조 인접 구간에서 `(0,1,0)`이다. |
| CP2-135 | 주기·하천·시계열 경계 | p.3은 네 종류 경계만 나열한다. | `shaders/BoundaryPass.wgsl:297` `let periodic_overlap = 2; // number of cells that overlap between periodic boundaries`; `docs/source/shaders/BoundaryPass_wgsl.md:18–19` ``- Boundary type `5` forcing from per-side `eta/hu/hv` time-series textures.`` / `- Constant stage/discharge river boundaries.` | 코드에만 | C. 주기는 타입 3이다. 하천은 수위·유량과 횡단면을 사용한다. 타입 5는 시공간 보간을 사용한다. 실제 셰이더 분기 원문은 이 절 뒤의 C7이다. |
| CP2-136 | 입사파 유형과 자료 검사 | p.3은 사인·불규칙 조파의 외부 설명을 인용한다. | `js/constants_load_calc.js:68` `incident_wave_type: -1, // 0 Sine Wave (single harmonic); 1 TMA Spectrum; 2 Transient Pulse (4 waves); 3 Solitary Wave; -1 Custom Spectum from loaded file; 5 Time Series from loaded file`; `js/File_Loader.js:378` `const expectedColumns = 1 + 3 * numPoints;` | 코드에만 | C. 타입 5 파일은 계측점 수·좌표·시간과 점별 eta/hu/hv를 읽는다. 열 수·최소 자료 수·시간 단조증가·좌표 중복·변별 시간 벡터를 검사한다. C8의 조건 원문을 따른다. |
| CP2-137 | 스펀지 모서리 합성과 퇴적물 초기화 | p.3–4는 η·P·Q 감쇠만 설명한다. | `shaders/BoundaryPass.wgsl:363–365` `state_sum  = state_sum + s * state_w;` / `weight_sum = weight_sum + s;` / `BCState_Sed = zero;`; `:395–398` 아래 C9 | 코드에만 | C. 중첩 스펀지는 거리 가중 평균을 사용한다. 스펀지에서 퇴적물 농도를 0으로 둔다. 별도 scalar/foam 채널의 감쇠와 퇴적물 텍스처 초기화를 구별한다. |
| CP2-138 | 단계별 경계 재적용 | p.6은 boundaryCondition 호출을 적지만 현재의 단계별 호출을 모두 적지 않는다. | `js/main.js:2694`의 `BoundaryPass_BindGroup` 호출; `:2728–2730` 아래 C10; `:2824,2858`은 보정 단계의 대응 호출 | 코드에만 | C. 분산 모드는 예측 단계에서 PCR 전·후 경계를 적용한다. `timeScheme==2`이면 보정 단계에서도 반복한다. 감쇠를 물리 시간 간격당 정확히 한 번 곱한다고 단정하지 않는다. |
| CP2-139 | 압력·침투·회전류 소산 | p.3 식 (1)에는 이 추가항이 없다. | `shaders/Pass3_Bous.wgsl:314–315` `let press_x = -0.5 * h_here * globals.g_over_dx * (P_right - P_left);` / `let press_y = -0.5 * h_here * globals.g_over_dy * (P_up - P_down);`; `:387–390` 아래 C11 | 코드에만 | C. 지표 표고가 0보다 크면 침투항을 넣는다. 압력은 별도 forcing 텍스처의 공간 차분이다. `vort_friction_factor>0`이면 회전류 경사 기반 운동량 소산을 더한다(`:291–300`). |
| CP2-140 | 시간 변동 수심과 교란 입력 | p.6은 고립파 초기조건을 예로 든다. 동적 바닥 forcing은 설명하지 않는다. | `shaders/Pass3_Bous.wgsl:306` `let dhdt = textureLoad(txBoundaryForcing, idx, 0).y;`; `js/constants_load_calc.js:147` `disturbance_change_timescale: 0.0,  // these are for the depth change landslide option` | 코드에만 | C. 교란에는 위치·진폭·방향·폭·길이·dip·rake·변동 시간·궤적 설정이 있다(`:137–155`). 이 설정을 2020 CML의 인쇄된 옵션 이름으로 쓰지 않는다. |
| CP2-141 | 네 번째 상태 채널 | p.3 식 (1)은 $h,P,Q$의 세 성분이다. | `shaders/Pass3_Bous.wgsl:336` `let c_dissipation = -globals.whiteWaterDecayRate * C_state_here;`; `:412–424` 아래 C12 | 코드에만 | C. foam/오염물질은 네 번째 채널을 사용한다. `showBreaking==1`이면 쇄파 front를 foam 강도로 쓴다. `==2`이면 오염원을 더하고 1로 제한한다. `clearConc==1`이면 0으로 지운다. |
| CP2-142 | 퇴적물 옵션과 기본 계수 | p.1–14는 퇴적물 수송 방정식·매개변수를 설명하지 않는다. | `js/constants_load_calc.js:106–114` 아래 C13 | 코드에만 | C. 기본은 비활성이다. d50=0.2는 초기화의 `/1000.` 변환에서 mm임을 확인한다(`:624`). 공극률·침식계수·임계 Shields·상대밀도·배경 확산·쇄파 확산·hard-bottom 로딩을 구별한다. |
| CP2-143 | 부유사·소류사·침식·퇴적 | p.1–14에 대응식 없음. | `shaders/SedTrans_Pass3.wgsl:144` `erosion = globals.sedC1_erosion * (shields - globals.sedC1_criticalshields) * local_speed;`; `:209` `bedload_erosion = 0.5 * globals.one_over_dx * (bedload_right_X - bedload_left_X) + 0.5 * globals.one_over_dy * (bedload_up_Y - bedload_down_Y);`; `:212` `var deposition = min(2.0 * C_state_here.x, h * (1.0 - globals.sedC1_n)) * globals.sedC1_fallvel;` | 코드에만 | C. 소류사 발산은 바닥 갱신에만 넣는다. 부유사 source에는 넣지 않는다(`:215` 원문 C14). 침식 가능 두께와 음농도 제한을 적용한다. |
| CP2-144 | 바닥 갱신·침강속도 | p.1–14에 대응식 없음. | `shaders/SedTrans_UpdateBottom.wgsl:84` `let dB_here = globals.dt * (e_here_average - d_here_average) / (1.0 - globals.sedC1_n); // this is positive when eroding - when increasing depth, or decreasing elevation`; `:115` `let B_new = B_here - dB;  // B is elevation, so a positive dB (eroding) should decrease the elevation` | 코드에만 | C. 침식은 표고를 낮춘다. 침강속도는 입경·상대밀도·점성 및 A=25, B=1.25, n=1로 계산한다(`js/constants_load_calc.js:622–630`, C15). 2020 논문에 이 계수의 검증 근거가 있다고 쓰지 않는다. |
| CP2-145 | 평균·최댓값·통계 파고 | p.9는 수위 실시간 곡선을 설명한다. 이 통계식을 적지 않는다. | `shaders/CalcMeans.wgsl:78` `let means_new = means_here*old_frac + state_here*update_frac;`; `shaders/CalcWaveHeight.wgsl:31–42` 아래 C16 | 코드에만 | C. 현재는 평균을 뺀 수위 제곱의 누적 평균에서 σ를 계산한다. RMS 파고는 `2.829σ`, 유의파고는 `4.000σ`이다. 주석 처리한 zero-crossing 경로와 구별한다. |
| CP2-146 | 면 출력 자료 구조 | p.9는 출력의 Advent 형식 승계만 적는다. | `js/File_Writer.js:8` `const requiredBytesPerRow = Math.ceil((width * 4 * 4) / 256) * 256; // width * RGBA * f32, padded`; `:29` `flatData[rowBaseReal + x] = bufferData[rowBasePadded + (x << 2) + chanOffset];` | 코드에만 | C. GPU readback의 256 byte 행 padding을 제거한다. export는 x가 먼저 변하는 `Float32Array(width*height)`이다. 첫 출력에는 bathytopo.bin·dx/dy/nx/ny.txt를 쓴다. 매 출력에는 time_N.txt를 쓴다. |
| CP2-147 | 색상 정규화 범위 제한 | p.8 식 (10)은 clamp를 인쇄하지 않는다. | `shaders/fragment.wgsl:594` `wavePosition = clamp(wavePosition, 0.0, 1.0);` | 코드에만 | C. 현재 색상 정규화는 범위를 0–1로 제한한다. `maxWave==minWave`의 분모 검사는 이 줄에 없다. 배열 끝 원소 문제는 CP2-156에서 별도로 다룬다. |
| CP2-148 | 시계열 export와 비동기 초기화 검사 | p.9는 부이의 화면 수위 곡선을 설명한다. | `js/Time_Series.js:108–112` 아래 C17; `:166`의 `Time/Eta/P/Q` header는 CP2-091에 인용했다. | 코드에만 | C. 시계열은 eta·P·Q를 별도 배열로 보관한다. 초기화 전 요청의 readback은 epoch가 다르면 버린다. 저장은 time_series_locations.txt와 time_series_data.txt이다. |
| CP2-149 | 이미지·면 출력 선택과 주기 | p.1–2의 360도 영상 외에 이 옵션은 없다. | `js/constants_load_calc.js:358–370` 아래 C18 | 코드에만 | C. GIF·JPEG 묶음·개별 면의 저장 플래그와 주기를 분리한다. 기본 면 출력은 eta만 켜져 있다. P·Q·u·v·turb는 꺼져 있다. `fileWritePause`의 100은 ms이다. |
| CP2-150 | 중첩격자 경계 출력 | p.1–14에 대응 설명 없음. | `js/constants_load_calc.js:380–386` `nestedGridOutput_dt: 1.0, // requested nested boundary output interval`와 `nestedGridOutput_max_samples: 8192, // hard cap on stored output times`; `js/File_Writer.js:836` ``await blobCreationAndDownload(blob, `${prefix}_time_series_bc_${side.name}.txt`);`` | 코드에만 | C. 사각형 경계의 eta/hu/hv 시계열을 저장한다. 시작·종료·최대 표본·복수 사각형·선행 무변화 구간 절단 옵션을 둔다(`:374–392`). 이는 2020의 다섯 부이 출력과 다르다. |
| CP2-151 | 설정 병합과 파생값 | p.9는 CML 입력을 설명한다. JSON 병합·검사 규칙은 없다. | `js/constants_load_calc.js:425` `calc_constants = { ...calc_constants, ...loadedConfig };`; `:438` `var configJson = JSON.parse(configContent);`; `:489–502`는 Theta·Bcoef·역격자간격·delta·epsilon 파생식이다. | 코드에만 | C. 업로드/예제 값이 기본값을 덮는다. 이후 파생값을 계산한다. JSON 구문 파싱과 수치 범위·키의 완전한 스키마 검사를 구별한다. |
| CP2-152 | 수심 자료 검사와 가장자리 평탄화 | p.9는 CBF 자료·보간을 설명한다. | `js/File_Loader.js:50–53`의 NaN 검사 U2; `:60–62` `for (let x = 0; x < 3; x++) {` / `bathy2D[x][y] = bathy2D[4][y];` / `}`; `:65–67`는 오른쪽 네 열을 WIDTH−5 열로 채운다. | 코드에만 | C. 현재 loader는 숫자 파싱 실패를 거부한다. 왼쪽·아래쪽 세 줄과 오른쪽·위쪽 네 줄을 내부 값으로 평탄화한다. 이는 해상도 보간과 다르다. |
| CP2-153 | 1D 단면 판 | p.3 식 (1)은 2DH이다. | `transect_version/shaders/Pass3_Bous.wgsl:108–115`의 원문 C19; `transect_version/js/Run_Tridiag_Solver.js:59–75`의 y solve는 주석이다. | 코드에만 | C. 단면 판의 y 미분·혼합항과 y PCR을 2D 본판에서 추론하지 않는다. x 수면 경사는 4차이다(`:242–244`). 단면 판의 정확한 원문은 C19이다. |
| CP2-154 | HTML별 진입점 | p.4·10은 Main.unity·실행 파일을 설명한다. | `index.html:1597`, `index_headless.html:112`, `index_nots.html:1486`, `river.html:1468`, `MC_examples.html:1468` 모두 `<script type="module" src="js/main.js"></script>`; `transect_version/index.html:1471` `<script type="module" src="/transect_version/js/main.js"></script>` | 코드에만 | C. 다섯 본판 HTML은 같은 main.js로 들어간다. 단면 HTML은 별도 main.js로 들어간다. `index_nots.html`이라는 이름만으로 시계열 기능이 완전히 없다고 판정하지 않는다. |
| CP2-155 | 동·북 스펀지의 거리식 | 논문의 $D(\alpha)$는 흡수 경계까지의 법선거리이다. 현재 거리 가중 설명은 `models/Celeris/source-analysis/celeris-breaking-boundary.md:115`이다. | `shaders/BoundaryPass.wgsl:111,123` N13의 `BoundaryWidth - boundary_nx - idx.x`, `BoundaryWidth - boundary_ny - idx.y`; 이력 V2의 괄호 삭제 | 불일치 | E. 근거 강도 중간. 동·북의 감쇠 인자는 경계에서 같은 거리라도 전체 WIDTH·HEIGHT에 따라 달라진다. 같은 판 노트의 거리 기반 설명과 과거 경로의 `BoundaryWidth - (boundary_nx - idx.x)`가 반대 근거이다. 5절 E1에서 의도 변경·보정 경로를 먼저 검토한다. 현재 활성 경로에서 호출한다. |
| CP2-156 | 색상 배열 상한 index | p.8 식 (10)의 현재 배열 구현에서 확인한 항목이다. | `shaders/fragment.wgsl:598–605` 아래 C20; `models/Celeris/source-analysis/celeris-render.md:57` “16색 LUT 선형보간” | 불일치 | E. 근거 강도 중간. 자기 주석의 “stay within the color map”과 같은 판 노트의 16색 설명을 대조했다. 정규화값 1이면 `lowerIndex=15`, `upperIndex=16`이다. 유효 원소는 0–15이다. `mixAmount=0`이라는 반대 근거를 5절 E2에서 함께 검토한다. 활성 렌더 경로이다. |
| CP2-157 | 지도·사용자 overlay 설정 | p.8은 자동 지도 다운로드를 설명한다. 현재의 사용자 이미지 입력과 변환 설정은 적지 않는다. | `index_headless.html:56` `<input type="file" id="satimageFile" accept="image/jpeg, image/png, image/bmp, image/gif" />`; `js/constants_load_calc.js:239–242`의 GMscaleX/Y=1.0, GMoffsetX/Y=0.0 | 코드에만 | C. 지도 API 호출과 사용자 이미지 업로드를 구별한다. 이미지 변환의 기본 배율은 1이고 기본 이동은 0이다. 지도를 자동 다운로드한 결과로 모든 overlay를 설명하지 않는다. |
| CP2-158 | 프레임당 반복 수·일시정지 | p.4은 “pre-defined number of steps”를 적는다. 자동 조정 옵션은 적지 않는다. | `js/constants_load_calc.js:248–250` `render_step: 1, // number of compute steps to run for every render step, the biggest the number the choppier the viz, but also the faster it runs` / `setRenderStep: 0, // flag to automatically find best render_step when = 0` / `simPause: -1, // check variable, simulation is paused when this value is =1, running when = -1` | 코드에만 | C. 프레임당 계산 횟수 조정은 물리 `dt`의 적응 조정과 다르다. 일시정지와 출력 대기 시간도 구별한다. |
| CP2-159 | 계산·렌더 정밀도 분리 | p.5는 RenderTexture라고만 적는다. | `js/Create_Textures.js:5` `format: 'rgba32float',`; `:18` `format: 'rgba16float',`; `shaders/vertex3D.wgsl:78`은 전체 etaTexture를 직접 읽는다. | 코드에만 | C. 계산 상태의 float32와 렌더 cache의 float16을 구별한다. 3D 높이가 언제나 float16 cache에서 온다고 쓰지 않는다. |
| CP2-160 | MATLAB 출력 판독·정리 스크립트 | p.9는 출력의 상세 판독 절차를 적지 않는다. | `scripts/load_WebGPUCeleris_output.m:18` `bathytopo = fread(fid, [nx, ny], 'float32');`; `:30` `eta = fread(fid, [nx, ny], 'float32');`; `:73` `pcolor(x, y, eta');  % note the transpose '  - the surface data is [nx,ny]`; `scripts/clean_WebGPUCeleris_output.m:4–5` `! del *.bin` / `! del *.txt` | 코드에만 | C. MATLAB은 `[nx,ny]`로 읽은 뒤 도식에서 전치한다. `nt=496`은 스크립트의 수동 수정값이다(`:14`). 정리 스크립트는 Windows 삭제 명령이다. 이 작업에서는 두 스크립트를 실행하지 않았다. |
| CP2-161 | 상류 문서의 단면 범위 제한 | p.1–14에는 현재 상류 문서의 판독 범위 규칙이 없다. | `docs/README.md:5` `The transect implementation is intentionally excluded. Do not infer transect behavior from these notes and do not use these notes as coverage for transect files.` | 코드에만 | C. 본판 docs/source 설명은 단면 판의 근거를 대신하지 않는다. 단면의 실제 파일을 별도로 열었다. |
| CP2-162 | 설계 요소·마찰 변경 | p.1–14는 현재의 설계 요소별 매개변수를 적지 않는다. | `js/constants_load_calc.js:345–355`의 Friction·Coral·Oyster·Mangrove·Kelp·Grass·Scrub·RubbleMound·Dune·Berm·Seawall 기본값; `shaders/fragment.wgsl:638–645`의 component_index 분기 | 코드에만 | C. 산호 0.1, 굴 0.035, 맹그로브 0.15, 해조 0.025, 잔디 0.03, 관목 0.075, 사석 0.04, 사구 0.03, berm 0.02, 방벽 0.02는 현재 설정이다. 셰이더는 요소별 가시심도·색 혼합을 적용한다. 이를 2020 권고 마찰값으로 쓰지 않는다. |

### 3.2 추가 처리의 코드 원문

**C1. `js/constants_load_calc.js:455–470` 원문**

```javascript
        if (calc_constants.NLSW_or_Bous != 0) {
            console.warn("Spherical grid mode is currently NLSW-only; forcing NLSW_or_Bous to 0.");
            calc_constants.NLSW_or_Bous = 0;
        }
        if (calc_constants.Accuracy_mode != 0) {
            console.warn("Spherical grid mode currently uses the standard second-order NLSW path; forcing Accuracy_mode to 0.");
            calc_constants.Accuracy_mode = 0;
        }
        if (calc_constants.useSedTransModel != 0) {
            console.warn("Spherical grid mode does not currently support sediment transport; forcing useSedTransModel to 0.");
            calc_constants.useSedTransModel = 0;
        }
        if (calc_constants.useBreakingModel != 0) {
            console.warn("Spherical grid mode does not currently support the Cartesian breaking model; forcing useBreakingModel to 0.");
            calc_constants.useBreakingModel = 0;
        }
```

**C2. `js/main.js:1539–1551` 원문**

```javascript
    if (calc_constants.Accuracy_mode == 1) {
        console.log("Using 4th-order MUSCL-TVD reconstruction scheme in Pass1");
        Pass1_ShaderCode = await fetchShader('/shaders/Pass1_HighOrder.wgsl');
    } else {
        Pass1_ShaderCode = await fetchShader('/shaders/Pass1.wgsl');
    }
    var Pass2_ShaderCode = null;
    if (calc_constants.Accuracy_mode == 1) {
        console.log("Using HLLC Flux Solver in Pass2");
        Pass2_ShaderCode = await fetchShader('/shaders/Pass2_HighOrder_HLLC.wgsl');  
    } else {
        Pass2_ShaderCode = await fetchShader('/shaders/Pass2.wgsl');  
    }
```

**C3. `shaders/Pass_Breaking.wgsl:100–125` 원문**

```wgsl
	let T_star=globals.T_star_coef*sqrt(h_here/globals.g);   
	let dzdt_I=globals.dzdt_I_coef*c_here;
	let dzdt_F=globals.dzdt_F_coef*c_here;

    var dzdt_star = 0.0;

    if(t_here <= globals.dt){
        dzdt_star = dzdt_I;
    } else if (globals.total_time - t_here <= T_star) {
        dzdt_star = dzdt_I + (globals.total_time - t_here) / T_star * (dzdt_F - dzdt_I);
    } else {
        dzdt_star = dzdt_F;
    }

    var B_Breaking = 0.;
    if(detadt < dzdt_star) {
        t_here = 0.0;
    } else if (detadt > 2.0 * dzdt_star) {
        B_Breaking = 1.0;
         if(t_here <= globals.dt) {t_here = globals.total_time;}
    } else {
        B_Breaking = detadt / dzdt_star - 1.0;
         if(t_here <= globals.dt) {t_here = globals.total_time;}
    }

    let nu_breaking = min(1.0 * globals.dx * globals.dy / globals.dt, B_Breaking * globals.delta_breaking * h_here * detadt);
```

**C4. `shaders/Pass3_Bous.wgsl:67–93` 원문**

```wgsl
fn FrictionCalc(hu: f32, hv: f32, h: f32, friction_here: f32) -> f32 {
   
     // need this special scaling step due to the need to take h^4, and precision issues with a single precision solver
     // this lets us explicitly control the allowed precision in the scaled h^4, which we set to 1e-6.
     // this implies that bottom friction may become inaccurate for flow depths less than ~ 5% of the base depth
     // this approach will make bottom friction much SMALLER in these small flow depths
     // I can not see a solution to this issue within the constraints of single precision for this term
    let h_scaled = h / globals.base_depth;
    let h2 = h_scaled * h_scaled;
    let h4 = h2 * h2;
    let divide_by_h2 = 2.0 * h2 / (h4 + max(h4, 1.e-6)) / globals.base_depth / globals.base_depth;
 
    let divide_by_h = 1. / max(h, globals.delta); 

    var f: f32;
    if (globals.isManning == 1) {
        f = globals.g * pow(friction_here, 2.0) * pow(abs(divide_by_h), 1.0 / 3.0);
    } else {
        f = friction_here;
    }

    f = min(f, 0.5);  // non-physical above 0.5

    f = f * sqrt(hu * hu + hv * hv) * divide_by_h2;

    return f;
}
```

**C5. `shaders/Pass3_Bous.wgsl:142–151` 원문**

```wgsl
    if (h_here <= h_cut) {  //if dry and surrounded by dry, then stay dry - no need to calc
        if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {
            let zero = vec4<f32>(0.0, 0.0, 0.0, 0.0);
            textureStore(txNewState, idx, zero);
            textureStore(dU_by_dt, idx, zero);
            textureStore(F_G_star, idx, zero);
            textureStore(current_stateUVstar, idx, zero);
            return; 
        }
    }
```

**C6. `shaders/Update_TriDiag_coef.wgsl:42–46` 원문**

```wgsl
    if (idx.x <= 2 || idx.x >= width - 3 || near_dry < 0.0) {
        a = 0.0;
        b = 1.0;
        c = 0.0;
    }
```

**C7. `shaders/BoundaryPass.wgsl:517–546` 원문**

```wgsl
    if (globals.west_boundary_type == 5 && idx.x <= 2) {
        let coordinate = BoundaryTimeSeriesYCoordinate(idx);
        BCState = BoundaryTimeSeriesState(2, coordinate, globals.ts_num_points_west);
        BCState_Sed = zero;
        BCState_Breaking = zero;
    }

    // east boundary
    if (globals.east_boundary_type == 5 && idx.x >= globals.width - 3) {
        let coordinate = BoundaryTimeSeriesYCoordinate(idx);
        BCState = BoundaryTimeSeriesState(3, coordinate, globals.ts_num_points_east);
        BCState_Sed = zero;
        BCState_Breaking = zero;
    }

    // south boundary
    if (globals.south_boundary_type == 5 && idx.y <= 2) {
        let coordinate = BoundaryTimeSeriesXCoordinate(idx);
        BCState = BoundaryTimeSeriesState(0, coordinate, globals.ts_num_points_south);
        BCState_Sed = zero;
        BCState_Breaking = zero;
    }

    // north boundary
    if (globals.north_boundary_type == 5 && idx.y >= globals.height - 3) {
        let coordinate = BoundaryTimeSeriesXCoordinate(idx);
        BCState = BoundaryTimeSeriesState(1, coordinate, globals.ts_num_points_north);
        BCState_Sed = zero;
        BCState_Breaking = zero;
    }
```

**C7. `shaders/BoundaryPass.wgsl:574–591` 원문**

```wgsl
    Q_c = Q_c / cos(globals.river_inflow_angle);
    let stage_elevation = globals.mean_upstream_channel_elevation + stage_c;
    let stage_speed = Q_c / stage_c / (globals.channel_bottom_width * cos(globals.river_inflow_angle) + stage_c / globals.channel_side_slope) ;

    if (globals.west_boundary_type == 4) { // west boundary is assumed to be the upstream boundary
        var left_bottom_start = globals.channel_bank_start_upstream;
        let loc_c = f32(idx.y) * globals.dy;
        if (idx.x <= 1 && loc_c > left_bottom_start && loc_c < globals.channel_bank_end_upstream ) {  //LARIVER MOD
            let flow_depth = max(stage_elevation - B_here, 0.0);
            let hu = flow_depth * stage_speed * cos(globals.river_inflow_angle);
            let hv = flow_depth * stage_speed * sin(globals.river_inflow_angle);
            var conc = 0.0;
            if (loc_c > globals.channel_bank_start_upstream && loc_c < globals.channel_bank_end_upstream && i32(globals.total_time / 30.0) % 2 == 0) {conc = 1.0;}
            BCState = vec4<f32>(stage_elevation, hu, hv, conc);
            BCState_Sed = vec4<f32>(0.0, 0.0, 0.0, 0.0);
            BCState_Breaking = vec4<f32>(0.0, 0.0, 0.0, 0.0);
        }
    }
```

**C8. `js/File_Loader.js:350–362` 원문**

```javascript
function parseBoundaryTimeSeriesText(fileContents, side, filePath) {
    const lines = cleanBoundaryTimeSeriesLines(fileContents);
    if (lines.length < 3) {
        throw new Error(`Boundary time-series file ${filePath} does not contain enough data.`);
    }

    // const countTokens = parseBoundaryTimeSeriesNumericLine(lines[0], filePath, 1);
    // const numPoints = parseInt(countTokens[countTokens.length - 1], 10);
    // Added by Codex: Allow either "3" or a labeled first line such as "number_of_ts_along_boundary 3".
    const numPoints = parseBoundaryTimeSeriesCountLine(lines[0], filePath);
    if (!Number.isInteger(numPoints) || numPoints < 1) {
        throw new Error(`Boundary time-series file ${filePath} must start with a positive station count.`);
    }
```

**C8. `js/File_Loader.js:378–385` 원문**

```javascript
    const expectedColumns = 1 + 3 * numPoints;
    const times = [];
    const values = [];
    for (; lineIndex < lines.length; lineIndex += 1) {
        const row = parseBoundaryTimeSeriesNumericLine(lines[lineIndex], filePath, lineIndex + 1);
        if (row.length != expectedColumns) {
            throw new Error(`Boundary time-series file ${filePath} row ${lineIndex + 1} has ${row.length} columns; expected ${expectedColumns}.`);
        }
```

**C8. `js/File_Loader.js:398–409` 원문**

```javascript
    for (let timeIndex = 1; timeIndex < times.length; timeIndex += 1) {
        if (times[timeIndex] <= times[timeIndex - 1]) {
            throw new Error(`Boundary time-series file ${filePath} time values must be strictly increasing.`);
        }
    }

    const sortedLocations = locations.map((location, index) => ({ location, index })).sort((a, b) => a.location - b.location);
    for (let locationIndex = 1; locationIndex < sortedLocations.length; locationIndex += 1) {
        if (sortedLocations[locationIndex].location <= sortedLocations[locationIndex - 1].location) {
            throw new Error(`Boundary time-series file ${filePath} contains duplicate station locations.`);
        }
    }
```

**C8. `js/File_Loader.js:433–443` 원문**

```javascript
function validateSharedBoundaryTimeVector(sharedTimes, candidateTimes, filePath) {
    if (sharedTimes.length != candidateTimes.length) {
        throw new Error(`Boundary time-series file ${filePath} does not match the shared time-vector length.`);
    }
    for (let timeIndex = 0; timeIndex < sharedTimes.length; timeIndex += 1) {
        const tolerance = Math.max(1.0e-7, 1.0e-7 * Math.abs(sharedTimes[timeIndex]));
        if (Math.abs(sharedTimes[timeIndex] - candidateTimes[timeIndex]) > tolerance) {
            throw new Error(`Boundary time-series file ${filePath} does not share the same time vector at row ${timeIndex + 1}.`);
        }
    }
}
```

**C9. `shaders/BoundaryPass.wgsl:395–398` 원문**

```wgsl
    // apply sponge if any side is active
    if (weight_sum > 0.0) {
        BCState = state_sum / weight_sum;
    }
```

**C10. `js/main.js:2728–2730` 원문**

```javascript
                if (calc_constants.NLSW_or_Bous > 0) { //BOUS
                    runComputeShader_EncStack(device, commandEncoderStack, BoundaryPass_uniformBuffer, BoundaryPass_uniforms, BoundaryPass_Pipeline, BoundaryPass_BindGroup_NewState, calc_constants.DispatchX, calc_constants.DispatchY);
                }
```

**C11. `shaders/Pass3_Bous.wgsl:387–390` 원문**

```wgsl
    var overflow_dry = 0.0;
    if(B_here > 0.0) {
        overflow_dry = -globals.infiltrationRate;  // hydraulic conductivity of coarse, unsaturated sand
    }
```

**C12. `shaders/Pass3_Bous.wgsl:412–424` 원문**

```wgsl
    if(globals.showBreaking ==1) {
        // add breaking source
        newState.a = max(newState.a, breaking_B);  // use the B value from Kennedy et al as a foam intensity
    }
    else if(globals.showBreaking == 2) {
        let contaminent_source = textureLoad(txContSource, idx, 0).r; 
        newState.a = min(1.0, newState.a + contaminent_source); 
    }

    // clear concentration if set
    if (globals.clearConc == 1){
        newState.a = 0.0; 
    }
```

**C13. `js/constants_load_calc.js:106–114` 원문**

```javascript
    useSedTransModel: 0, // sed model on or off [0]
    sedC1_d50: 0.2,   // D50 for Class 1 sed
    sedC1_n: 0.40,   // porosity for Class 1 sed
    sedC1_psi: 0.00005,   // psi for Class 1 sed
    sedC1_criticalshields: 0.045,   // critical shields for Class 1 sed
    sedC1_denrat: 2.65,   // desnity sed / desnity water for Class 1 sed
    sedTurbDispersion: 0.01, // eddy viscosity constant (background) value for sediment transport
    sedBreakingDispersionCoef: 0.1, // fraction of breaking eddy viscosity to use for sediment transport dispersion
    loadHardBottom: 0, // load hard bottom from file when == 1
```

**C14. `shaders/SedTrans_Pass3.wgsl:215–215` 원문**

```wgsl
    let source_term = (erosion - deposition) * divide_by_h;  // do not add bedload here, since this is only for suspended load
```

**C15. `js/constants_load_calc.js:622–630` 원문**

```javascript
    let nu = 0.000001; // kinematic viscosity of water in m^2/s
    let delta = calc_constants.sedC1_denrat - 1.0;
    let d = calc_constants.sedC1_d50/1000.; // convert d50 to meters
    let ds =  d * Math.pow(delta * calc_constants.g / (nu * nu) , 1.0 / 3.0)   // (delta*g/nu^2)^(1/3)*d
    let A = 25; // shape factor, natural particles
    let B = 1.25; // shape factor, natural particles
    let n = 1.0; // exponent for fall velocity, natural particles
    let fall_vel = nu / d * (Math.sqrt(0.25 * (A / B) ** (2 / n) + (4 / 3 * (ds ** 3 / B)) ** (1 / n)) - 0.5 * (A / B) ** (1 / n)) ** n; // fall velocity for natural particles; nu/d*(sqrt(0.25*(A/B)^(2/n)+(4/3*(ds^3/B))^(1/n))-0.5*(A/B)^(1/n))^n
    calc_constants.sedC1_fallvel = fall_vel; // set the fall velocity for Class 1 sediment
```

**C16. `shaders/CalcWaveHeight.wgsl:31–42` 원문**

```wgsl
    let eta = eta_New-eta_mean;
    
    sum_eta2 = sum_eta2 + eta * eta;

    var variance = sum_eta2 / f32(globals.n_time_steps_waveheight);

    let sigma = sqrt(variance);

    let H_mean = sigma * 2.829;  // RMS wave height
    let H_sig = sigma * 4.000;   // sig wave height

    let new_vals = vec4<f32>(sum_eta2, (H_sig-old_vals.b)/old_vals.b, H_sig, H_mean);
```

**C17. `js/Time_Series.js:108–112` 원문**

```javascript
        if (timeSeriesDataEpoch != calc_constants.timeSeriesDataEpoch) {
            buffer.unmap();
            buffer.destroy();
            return;
        }
```

**C18. `js/constants_load_calc.js:358–370` 원문**

```javascript
    create_animation: 0, // create animated gif when = 1
    AnimGif_dt: 1.0, // time between animated gif frames
    JPEGstack_dt: 1.0,  // time between images in jpeg stack
    JPEGstack_frames: 10,  // total number of frames to save in jpg stack
    writesurfaces: 0,  //flag for writing 2D data to file
    write_eta: 1, // flag for writing eta surface data to file, write when = 1
    write_P: 0, // flag for writing x flux surface data to file, write when = 1
    write_Q: 0, // flag for writing y flux surface data to file, write when = 1
    write_u: 0, // flag for writing x velocity surface data to file, write when = 1
    write_v: 0, // flag for writing y velocity surface data to file, write when = 1
    write_turb: 0, // flag for writing eddy visc surface data to file, write when = 1
    dt_writesurface: 1.0, // incrememnt to write to file 
    fileWritePause: 100, // time (ms) to pause during 2D surface write to not overload write buffer
```

**C19. `transect_version/shaders/Pass3_Bous.wgsl:108–115` 원문**

```wgsl
    let leftIdx = idx + vec2<i32>(-1, 0);
    let rightIdx = idx + vec2<i32>(1, 0);
   // let downIdx = idx + vec2<i32>(0, -1);
   // let upIdx = idx + vec2<i32>(0, 1);
   // let upleftIdx = idx + vec2<i32>(-1, 1);
   // let uprightIdx = idx + vec2<i32>(1, 1);
   // let downleftIdx = idx + vec2<i32>(-1, -1);
   // let downrightIdx = idx + vec2<i32>(1, -1);
```

**C19. `transect_version/shaders/Pass3_Bous.wgsl:242–244` 원문**

```wgsl
    // replace with 4th order when dispersion is included
        detadx = 1.0 / 12.0 * (eta_left_left - 8.0 * eta_left + 8.0 * eta_right - eta_right_right) * globals.one_over_dx;
       // detady = 1.0 / 12.0 * (eta_down_down - 8.0 * eta_down + 8.0 * eta_up - eta_up_up) * globals.one_over_dy;
```

**C19. `transect_version/js/Run_Tridiag_Solver.js:59–75` 원문**

```javascript
        // Copy tridaig coef into newcoef for first loop
       // runCopyTextures(device, commandEncoder, calc_constants, coefMaty, newcoef_y)
       // for (let p = 0; p < calc_constants.Py; p++) {

       //     let s = 1 << p;

       //     TridiagY_view.setInt32(8, p, true);             // i32, holds "p"
       //     TridiagY_view.setInt32(12, s, true);            // i32, hols "s"

            // Dispatch the shader computation.
       //     runComputeShader(device, commandEncoder, TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);
            // Copy reduced tridaig coef into newcoef for next loop
       //     runCopyTextures(device, commandEncoder, calc_constants, txtemp_PCRy, newcoef_y)
       // }

        // After all the iterations, copy the new state into current state.
       // runCopyTextures(device, commandEncoder, calc_constants, txtemp2_PCRy, txNewState)
```

**C20. `shaders/fragment.wgsl:590–605` 원문**

```wgsl
            // Determine where 'render_surface' falls in the range from 'minWave' to 'maxWave'.
            var wavePosition = f32((render_surface - minWave) / (maxWave - minWave));

            // Clamp the position between 0 and 1 to stay within the color map.
            wavePosition = clamp(wavePosition, 0.0, 1.0);

            // Determine the indices of the two colors we'll be interpolating between.
            // This requires the color map to have a known and fixed size.
            let lowerIndex = i32(floor(wavePosition * 15.0)); // Because we have 16 colors.
            let upperIndex = lowerIndex + 1;

            // Calculate how far between the two colors 'render_surface' falls.
            let mixAmount = fract(wavePosition * 15.0); // Fractional part represents the mix amount between colors.

            // Interpolate between the two colors in the color map.
            let color_wave = mix(colorMap[lowerIndex], colorMap[upperIndex], mixAmount);
```

**C21. `js/constants_load_calc.js:345–355` 원문**

```javascript
    designcomponent_Friction: 0.0, // friction factor of the component currently being added
    designcomponent_Fric_Coral: 0.1, // Coral Reef  friction factor
    designcomponent_Fric_Oyser: 0.035, // Mussel/Oyster Bed friction factor
    designcomponent_Fric_Mangrove: 0.15, // Mangroves friction factor
    designcomponent_Fric_Kelp: 0.025, // Kelp friction factor
    designcomponent_Fric_Grass: 0.03, // Grass friction factor
    designcomponent_Fric_Scrub: 0.075, // shrub/scrub friction factor
    designcomponent_Fric_RubbleMound: 0.04, // Rubblemound Structure friction factor
    designcomponent_Fric_Dune: 0.03, // Vegetated Dune friction factor
    designcomponent_Fric_Berm: 0.02, // Berm / Temporary Dune friction factor
    designcomponent_Fric_Seawall: 0.02, // Seawall  friction factor
```

## 4 노트 대조와 수정안

이 절은 현재 노트의 관련 서술을 원문으로 인용한다. 수정안은 이 보고서 안에만 쓴다. 현재 노트 파일은 수정하지 않았다. 같은 내용에 대한 2절의 판정과 노트 자체의 정확성 판정은 별도로 센다.

| 행 ID | 항목 | 노트 위치와 원문 | 논문·코드 근거와 원문 | 판정 | 이유와 노트 수정안 |
|---|---|---|---|---|---|
| CP2-163 | 원판의 언어 | `models/Celeris/README.md:14` “**원판**: C#/HLSL, **Direct3D** GPU (Windows)” | Tavakkol 2020 p.2 “Celeris Advent is developed in C++ and HLSL using the Direct3D framework.”; p.1 Base는 Unity3D·C#·HLSL이다. | 불일치 | B. Advent와 Base의 언어를 혼합했다. 수정안: “Advent는 C++·HLSL·Direct3D 구현이다. Base는 Unity3D·C#·HLSL 구현이다. WebGPU는 JavaScript·WGSL 구현이다.” |
| CP2-164 | 적응형 시간 적분 단정 | `models/Celeris/README.md:18` “시간적분 3rd-order Adams-Bashforth(adaptive, Tavakkol-Lynett 2019)” | Tavakkol 2020 p.3 “third-order fixed timestep”; `js/constants_load_calc.js:486`의 dt 산식; N9의 AB3·AM4 계수 | 불일치 | B. 문헌 제목의 adaptive를 현재 코드의 실행 기능으로 옮겼다. 수정안: “2020 Base 논문은 고정 시간 간격의 AB3를 설명한다. 현재 WebGPU 기본은 AB3 예측과 AM4 보정이다. 현재 코드는 대표 수심과 Courant 수로 dt를 계산한다.” |
| CP2-165 | 2019 문헌의 저자 | `models/Celeris/README.md:27` “Tavakkol, Lynett (2019)”; `models/Celeris/manual-notes/celeris-architecture-and-config.md:173` “**Tavakkol, S. & Lynett, P. (2019).**” | Tavakkol 2020 p.14 [29] “S. Tavakkol, S. Son, P. Lynett, ArXiv Prepr. ArXiv:1909.04153 (2019).” | 불일치 | B. 같은 위키의 `celeris-official-resources.md:25`도 Son을 포함한다. 수정안: “Tavakkol, S., Son, S. & Lynett, P. (2019), arXiv:1909.04153.” |
| CP2-166 | 예측·보정 명칭 | `models/Celeris/source-analysis/celeris-source-map.md:42` “시간적분 (3rd-order Adams-Bashforth predictor-corrector)” | `shaders/Pass3_Bous.wgsl:404` `newState = in_state_here_UV + globals.dt / 12.0 * (23.0 * d_by_dt - 16.0 * oldies + 5.0 * oldOldies);`; `:409` `newState = in_state_here_UV + globals.dt / 24.0 * (9.0 * d_by_dt + 19.0 * predicted - 5.0 * oldies + oldOldies);` | 불일치 | B. 본문의 AB3·AM4 구분은 맞지만 제목이 모두 3차 AB인 것처럼 보인다. 수정안: “시간 적분은 Euler, AB3 예측, AB3 예측과 AM4 보정 중에서 선택한다.” |
| CP2-167 | 예측·보정 호출 조건 | `models/Celeris/source-analysis/celeris-pipeline-graph.md:115` “**corrector substep은 `if (timeScheme==2)`에서만**” | `js/main.js:2757` `if (calc_constants.timeScheme == 2)  // only called when using Predictor+Corrector method.  Adding corrector allows for a time step twice as large (also adds twice the computation) and provides a more accurate solution` | 일치 | 유지한다. 보완 문장: “프레임당 반복 수 조정은 물리 dt의 적응형 갱신을 뜻하지 않는다.” |
| CP2-168 | 시간 적분 계수 설명 | `models/Celeris/source-analysis/celeris-boussinesq-solver.md:195` “3차 Adams-Bashforth predictor — 계수 (23, −16, 5)/12”; `:196` “4차 Adams-Moulton corrector — (9, 19, −5, 1)/24” | N9의 현재 코드 원문 | 일치 | 유지한다. 보완 문장: “2020 p.3의 시간 적분 설명은 고정 dt의 AB3이며 현재 기본 보정 경로까지 설명하지 않는다.” |
| CP2-169 | 상태와 면 위치 | `models/Celeris/source-analysis/celeris-fv-reconstruction.md:20` “수심 `h = w - B`”; `:22` “`(N, E, S, W) = (.x, .y, .z, .w)`” | `shaders/Pass1.wgsl:78` `let h_here = in_here.x - B_here;`; N1의 `.y` 동쪽, `.x` 북쪽 플럭스 | 일치 | 유지한다. 보완 문장: “논문 식 (1)의 h를 코드 txState.x와 직접 동일시하지 않는다. txState.x는 수면 표고이다.” |
| CP2-170 | 스펀지층 판 차이의 누락 | `models/Celeris/source-analysis/celeris-breaking-boundary.md:109` “cosine 윈도우를 0.005승한 감쇠계수 γ”; `:115` “거리 가중 평균” | Tavakkol 2020 p.4 식 (9); `shaders/BoundaryPass.wgsl:105` N13 | 불일치 | C. 현재 코드 설명에는 Base의 비율식과의 차이가 없다. 수정안: “현재 감쇠식은 2020 식 (9)의 γ 비율식과 다르다. 동·북 거리식에는 CP2-155의 코드 결함 후보가 있다.” |
| CP2-171 | COULWAVE와 약비선형 모드의 구분 | `models/Celeris/source-analysis/celeris-coulwave.md:12` “모드1 \"Bous\"는 Madsen & Sørensen 약비선형(B=1/15)” | Tavakkol 2020 p.3의 “only weakly nonlinear”와 $B=1/15$; `js/constants_load_calc.js:36–38` | 일치 | 유지한다. 보완 문장: “2020 논문이 제시한 분산항은 현재 모드 1의 계보이며 모드 2의 전체 식이 아니다.” |
| CP2-172 | 퇴적물 확산의 비활성 단정 | `models/Celeris/source-analysis/celeris-sediment.md:104` “현재 활성 빌드는 **이류 + 픽업/침강만**, 명시적 확산 없음”; “셰이더에서 미사용” | `shaders/Pass2.wgsl:141` `let k_here =  globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, idx, 0).y;`; `:190`은 `- k_east * hW_east * C1x_east`와 `- k_west * h_here.y * C1x_west`를 포함한다. | 불일치 | B. Pass3 안의 주석 처리만 보고 활성 Pass2의 확산 플럭스를 빠뜨렸다. 수정안: “Pass3의 별도 확산 source는 주석이다. 기본 Pass2는 Class 1 부유사 면 플럭스에 배경·쇄파 확산을 넣는다.” |
| CP2-173 | AB4라는 옵션 설명 | `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:191` “2=AB4 pred+corr” | N9의 예측 계수는 3차 AB이다. 보정 계수는 4차 AM이다. | 불일치 | B. 코드 주석의 축약을 그대로 반복했다. 수정안: “timeScheme=2는 AB3 예측과 AM4 보정이다.” |
| CP2-174 | 매뉴얼 노트의 적응형 출처 서술 | `models/Celeris/manual-notes/celeris-architecture-and-config.md:185` “§1.5의 적응형 3차 Adams-Bashforth predictor/corrector 시간적분의 학술적 출처” | 같은 노트 `:107–108`은 예측·보정을 나눈다. Tavakkol 2020 p.3은 fixed timestep이다. 현재 N9·`js/constants_load_calc.js:486`에는 가변 간격 계수가 없다. | 불일치 | B. 현재 스킴의 구현 설명에서 적응형을 단정할 수 없다. 수정안: “2019 문헌은 적응형 시간 적분 연구의 별도 참고문헌이다. 현재 구현의 예측·보정 계수와 dt 계산은 코드에서 직접 인용한다.” |
| CP2-175 | 2020 논문의 워크플로 계승 | `models/Celeris/manual-notes/celeris-architecture-and-config.md:184` “WebGPU 버전이 정적 브라우저앱으로 그 정신 계승” | `docs/architecture/REFERENCE_PAPERS.md:33` “keeps the same spirit”; 2절의 A·D 행 | 불일치 | C. 워크플로 유사성만으로 입력·스펀지·VR 구현의 일치를 주장하지 않도록 판 차이를 추가한다. 수정안: “Base의 Unity 클래스, CML·CBF 보간, 식 (9), 최대 다섯 부이, Rift·360도 영상 기능을 현재 WebGPU 기능으로 승계하지 않는다.” |
| CP2-176 | 2020 문헌의 기능 범위 | `models/Celeris/web-refs/celeris-official-resources.md:28` “Unity3D + C#/HLSL compute shader, **VR 헤드셋·360° 비디오·지도 오버레이·실시간 게이지**” | Tavakkol 2020 p.1 초록과 p.9·11 | 일치 | Base 문헌의 요약으로 유지한다. 보완 문장: “이 목록은 2020 Base의 기능이며 WebGPU의 지원 목록이 아니다.” |
| CP2-177 | 2017 계보 표의 언어 | `models/Celeris/web-refs/celeris-lynett-2026.md:59` “C#/HLSL Direct3D (Windows)” | Tavakkol 2020 p.2 “Celeris Advent is developed in C++ and HLSL” | 불일치 | B. 같은 Advent를 C#이라고 썼다. 수정안: “2017 Advent의 플랫폼은 C++·HLSL·Direct3D이다.” |
| CP2-178 | 분산 이론 노트의 모드 1 | `models/Celeris/web-refs/celeris-coulwave-theory.md:37` “정수심 기반 Madsen 형” | `shaders/Pass3_Bous.wgsl:181` `let d_here = -B_here;`; N3의 d²·d³·B 계수 | 일치 | 유지한다. 보완 문장: “Tavakkol 2020 식 (2)–(3)을 모드 1에 대응시킨다. 코드의 젖음·마름·주기 경계 조건은 별도로 인용한다.” |
| CP2-179 | 렌더 노트의 배열 보간 | `models/Celeris/source-analysis/celeris-render.md:57` “16색 LUT 선형보간”; `:79` “`textureLoad`로 읽어 elevation 취득” | `shaders/fragment.wgsl:598–605` C20; `shaders/vertex3D.wgsl:78` | 불일치 | C. 3D 높이 설명은 유지한다. 보완 문장: “색상 최댓값에서 upperIndex가 16이 되는 CP2-156의 후보를 기록한다. 128×128 타일은 2020 Base의 구조이다.” |

## 5 차이 결론

분류별 개수: 일치 29, A 43, B 12, C 37, D 4, E 2, F 8, H 44, X 0. 합계 179행이다. 아래 결론 표는 일치가 아닌 150행만 싣는다. 각 행에는 분류 하나만 부여했다. 같은 논문 문장이 여러 독립 항목을 포함하면 항목을 나눴다. 4절의 노트 판정은 별도 행으로 셌다.

### 5.1 판 차이를 뒷받침하는 이력

다음 표의 날짜는 로컬 전체 git 이력의 커밋 날짜이다. 논문 날짜는 p.1의 온라인 공개일 2019-09-28이다. 아래 증거는 WebGPU 구현이 특정 시점에 존재했음을 보인다. Unity Base 소스가 이 git 안에 있었다고 주장하지 않는다. 이 저장소의 첫 커밋보다 오래된 Unity 구현의 결함을 현재 이력으로 판정하지 않는다.

| 이력 ID | HASH·날짜·원문 변경 | 판 판정에 사용하는 범위 |
|---|---|---|
| V1 | `fd57bb7` 2023-10-09 “Add files via upload”. `fd57bb7:js/main.js:17` `const gpu = navigator.gpu;`. `fd57bb7:js/Run_Compute_Shader.js:15` `computePass.dispatchWorkgroups(dispatchX, dispatchY);`. `fd57bb7:shaders/Pass1.wgsl:65` `@compute @workgroup_size(16, 16) //`. 해당 업로드의 새 JS·WGSL 파일을 확인했다. | Unity·C#·HLSL·GameObject·상속·Material·scene에서 JS·WGSL·HTML·WebGPU로 바뀐 구현 판이다. 논문 자체는 p.1–2에서 Base와 Advent의 언어를 명시한다. |
| V2 | `cf9de63` 2023-10-24 “Add files via upload”. `cf9de63:shaders/BoundaryPass.wgsl:57`의 지수는 `0.005`이다. 부모의 같은 파일 `:63`은 `BoundaryWidth - f32(boundary_nx - idx.x)`와 지수 `0.01`이다. 변경 후 `:63`은 `f32(BoundaryWidth - boundary_nx - idx.x)`와 지수 `0.005`이다. 전체식은 N13과 아래 E1에 인용했다. | 2020 식 (9)의 비율식이 아닌 WebGPU 감쇠식을 확인한다. 이 변경은 동·북 괄호 삭제 후보의 발생 지점도 보인다. |
| V3 | `f18955b` 2024-10-01 “Update Pass3_Bous.wgsl”. 본문 메시지는 `wrong sign on high order 4th order derivative`이다. `f18955b:shaders/Pass3_Bous.wgsl:226` `let detadx = 1.0 / 12.0 * (eta_left_left - 8.0 * eta_left + 8.0 * eta_right - eta_right_right) * globals.one_over_dx;`. 같은 변경은 y 끝항을 `+ eta_up_up`에서 `- eta_up_up`으로 고쳤다(`:227`). | 2020의 나머지 항 2차 FDM 설명과 현재 4차 1차 미분을 구별한다. 이력의 수정된 과거 부호를 현재 결함으로 다시 보고하지 않는다. |
| V4 | `fd57bb7` 2023-10-09. `fd57bb7:js/constants_load_calc.js:14` `timeScheme: 2,  // Time integration choices: 0: Euler, 1: 3rd-order A-B predictor, 2: A-B 4th-order predictor+corrector.`. `63a12e3` 2023-10-19 업로드의 `shaders/Pass3_Bous.wgsl:269` `newState = in_state_here_UV + globals.dt / 24.0 * (9.0 * d_by_dt + 19.0 * predicted - 5.0 * oldies + oldOldies);`. | 2019 공개 Base의 고정 AB3 설명과 WebGPU의 AM4 보정 선택을 구별한다. AB4라는 주석 명칭보다 실제 계수를 우선한다. |
| V5 | `366ee34` 2024-04-08 “photorealism update”. diff는 breaking model parameters 블록을 추가한다. `366ee34:js/constants_load_calc.js:41` `useBreakingModel: 1, // inlcude breaking model when == 1`; `:42–45`에 2.0·5.0·0.50·0.15가 추가되었다. | 논문의 직접 쇄파 처리 부재와 현재의 명시적 쇄파를 구별한다. |
| V6 | `38a5072` 2025-01-21 “Added periodic bc and proper rendering for configs with dx~=dy”. diff는 periodic 분기에서 state 외에 sediment·breaking 복사를 추가한다. `38a5072:js/constants_load_calc.js:53`의 `incident_wave_type`에는 사인·TMA·pulse·solitary·custom 구분이 있다. | 현재의 경계 유형과 입사파 유형이 별도 축임을 확인한다. 주기 경계 처리도 2020 목록보다 확장되었다. 이 커밋이 모든 경계 종류를 처음 만들었다고 주장하지 않는다. |
| V7 | `0b4e990` 2025-05-16 “Vector arrow overlay”. diff는 `NLSW_or_Bous` 주석을 두 모드에서 세 모드로 고친다. `0b4e990:js/constants_load_calc.js:29`는 모드 2를 `Fully Non-linear Boussinesq (COULWAVE equations)`라고 적는다. `:31` `Bous_alpha: -0.531,  // extended Boussinesq parameter,`를 추가한다. | Base의 두 해석기와 현재 세 모드를 구별한다. |
| V8 | `471c581` 2024-01-04 “Add files via upload”. `471c581:js/main.js:458–459` `const gridWidth = calc_constants.WIDTH;  // Number of vertices along the width` / `const gridHeight = calc_constants.HEIGHT; // Number of vertices along the height`. 추가된 `:464–481`은 전체 영역 strip 정점을 만든다. 현재의 정점 수 교정은 `ebca435:js/main.js:1703–1704`이다. | Base의 128×128 타일과 현재 WIDTH×HEIGHT 높이 격자를 구별한다. |
| V9 | `2eb2866` 2023-10-26 “Add files via upload”. 추가된 `2eb2866:js/File_Loader.js:122` `export async function CreateGoogleMapImage(device, context, lat_LL, lon_LL, lat_UR, lon_UR, maxWidth, maxHeight) {`; `:131–144`에 모서리 좌표 기반 zoom 계산을 추가한다. | Base의 CML 중심 좌표·haversine·C# 지도 자산과 현재 JS 모서리 입력을 구별한다. |
| V10 | `efe44a2` 2024-04-02 “Add files via upload”. diff는 시계열 배열·상한·tooltip 좌표를 추가한다. `efe44a2:js/constants_load_calc.js:131` `maxNumberOfTimeSeries: 16, // max number of time series allowed, inlcuding tooltip, if greater than 16, need to update readToolTipTextureData bytesperrow.  SHould be 16*N time series`. `efe44a2:js/main.js:1416` `calc_constants.mouse_current_canvas_indX = Math.round(normalizedX * calc_constants.WIDTH);`. | Base의 ray/GetPixel/다섯 부이와 현재 canvas index·buffer readback·15점 UI를 구별한다. `ebca435` 2026-07-20 “fixed time series write bug”는 reset epoch 검사를 추가했다. |
| V11 | `fd57bb7:js/constants_load_calc.js:56,60–61`은 2023-10-09부터 config.json fetch·JSON 병합을 한다. `254d71c` 2023-10-09의 새 `js/File_Loader.js:25–31`은 bathy 행·열 불일치를 거부한다. `cf9de63` 2023-10-24의 새 `js/File_Writer.js:74` `const blob = new Blob([data.buffer], { type: 'application/octet-stream' }); // or another MIME type as appropriate`. `:79`는 `textureData.bin`이다. | Base의 CML·CBF·보간·출력 승계와 현재 입력·binary 출력을 구별한다. Tavakkol 2017 PDF p.6(인쇄 p.122)는 “The output files are written into a formatted ASCII file.”라고 적는다. 2020 p.9의 형식 승계 진술과 연결했다. |

판 인용은 `git log --follow -p -- <파일>`, `git show HASH:<파일>`, `git log -S'<문자열>' -- <파일>`로 확인했다. V3의 과거 4차 식은 현재 식의 근거로 사용하기 전에 부호 수정 커밋을 확인했다. V2의 지수 변경은 스펀지 비율식으로의 변경이 아니다.

### 5.2 문서에만 있는 기능의 검색

검색 루트 `S`는 `models/Celeris/raw/source_code/Celeris-WebGPU`이다. `rg -i -n`은 이 루트 전체에 적용했다. `CelerisAgent`, `automation*`, `benchmarks`, 모든 깊이의 `examples`, `externals`, `assets`, `textures`, `skybox` 폴더를 제외했다. skybox·duck·model 전용 셰이더도 제외했다. 이 제외는 파일 내용 열기 전에 적용했다. PDF는 최종 전체 검색의 제외 목록에 넣지 않았다. `rg`는 기본 binary 처리 규칙을 사용한다. 따라서 PDF 내용의 존재 여부는 키워드 검색이 아니라 직접 연 쪽 이미지에서 판정했다.

```bash
rg -i -n '\bVR\b|oculus|webxr|xrSession|requestSession|headset' "$S" \
  -g '!**/CelerisAgent/**' -g '!**/automation*/**' \
  -g '!**/benchmarks/**' -g '!**/examples/**' -g '!**/externals/**' \
  -g '!**/assets/**' -g '!**/textures/**' -g '!**/skybox/**' \
  -g '!**/skybox.*.wgsl' -g '!**/duck.*.wgsl' -g '!**/model.*.wgsl'
```

실제 도구 호출은 위 인자 배열을 Python `subprocess.run`으로 전달했다. `S` 자리에는 실제 경로 문자열을 넣었다. D2도 같은 인자와 제외 목록을 사용했다.

| 검색 ID | 대상 행 | `rg -i` 검색어와 결과 | `git log -S` 검색어와 결과 | 결론 |
|---|---|---|---|---|
| D1 | CP2-003·101·104 | `\bVR\b\|oculus\|webxr\|xrSession\|requestSession\|headset`의 정규식 OR 검색. 최종 전체 검색은 0행이다. 종료코드는 1이다. | `git -C S log --all --format='%h %ad %s' --date=short -i -S<검색어> -- <범위 내 tracked 파일 목록>`을 실행했다. `oculus`, `requestSession`, `xrSession` 각각 0커밋이다. 종료코드는 모두 0이다. | 논문은 Rift와 양손 조종기를 명시한다. 현재 소스·검색 이력에서 이 기능의 구현을 확인하지 못했다. D로 분류한다. |
| D2 | CP2-004 | `360.{0,12}(video\|captur)\|equirectangular\|panoram\|capture360\|record360\|spherical.{0,12}video`의 정규식 OR 검색. 최종 전체 검색은 0행이다. 종료코드는 1이다. | 위 명령에서 `equirectangular`, `panorama`, `capture360`, `record360`, `360° video`를 각각 검색했다. 모두 0커밋이다. 종료코드는 모두 0이다. | MP4·GIF·JPEG 함수는 존재한다. 360도 투영·촬영 구현은 검색되지 않았다. D로 분류한다. |

`git ls-files`로 tracked 목록을 얻었다. 경로 구성요소에 같은 제외 목록을 적용한 뒤 `--` 뒤의 파일 인자 배열로 전달했다. 삭제된 VR 기능이 있었다는 주장도 이 검색 결과에서 도출하지 않았다. D는 알려진 구현 키워드·실행 진입 경로와 이력 검색에 근거한 결론이다.

### 5.3 코드 결함 후보의 반대 근거와 강도

**E1 — CP2-155: 동·북 스펀지의 원점 의존성.** 먼저 변경 의도를 찾았다. `cf9de63`의 메시지는 “Add files via upload”이다. 이 변경은 BoundaryWidth의 타입 변환과 감쇠 지수를 함께 바꾼다. 감쇠를 전체 영역 폭에 의존시키겠다는 주석은 없다. `git log --grep='sponge\|damp\|cosine\|color' -i`의 결과에서 이 동·북 거리식 변경을 설명하는 메시지는 찾지 못했다. 색상 관련 수정 메시지는 이 식의 보정 근거가 아니다.

다음은 `63a12e3:shaders/BoundaryPass.wgsl:62–66`의 원문이다. 날짜는 2023-10-19이다.

```wgsl
fn EastBoundarySponge(idx: vec2<i32>) -> vec4<f32> {
    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (globals.BoundaryWidth - f32(globals.boundary_nx - idx.x)) / (globals.BoundaryWidth - 1.0))), 0.01);
    let new_state = textureLoad(txState, idx, 0);
    return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
}
```

`cf9de63:shaders/BoundaryPass.wgsl:62–66`의 변경 후 원문은 다음과 같다.

```wgsl
fn EastBoundarySponge(idx: vec2<i32>) -> vec4<f32> {
    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - globals.boundary_nx - idx.x)) / f32(globals.BoundaryWidth - 1))), 0.005);
    let new_state = textureLoad(txState, idx, 0);
    return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);
}
```

북쪽도 같은 변경에서 `BoundaryWidth - f32(boundary_ny - idx.y)`를 `f32(BoundaryWidth - boundary_ny - idx.y)`로 바꿨다. 현재 본판의 식은 N13에 있다. 현재 단면 판의 동쪽도 `transect_version/shaders/BoundaryPass.wgsl:93`에서 같은 뺄셈을 사용한다. 따라서 단면 판이 이 식을 보정한다고 볼 수 없다. 현재 호스트는 `js/constants_load_calc.js:505–506`에서 `boundary_nx=WIDTH-1`, `boundary_ny=HEIGHT-1`로 설정한다. `js/main.js:2694`와 `:2729`는 해당 BoundaryPass를 호출한다. 이 후보는 호출되지 않는 코드가 아니다.

해석: 변경 전 동쪽 식의 괄호 안은 경계까지의 index 거리이다. 변경 후 식은 경계 index와 셀 index를 모두 뺀다. 현재 거리 가중 설명(`models/Celeris/source-analysis/celeris-breaking-boundary.md:115`)과 과거의 거리식 경로를 함께 대조하면 지역 거리 기반 감쇠라는 설명과 어긋난다. 현재 식의 인자에는 `-2*boundary_nx`에 해당하는 전체 폭 의존성이 남는다.

정적 산술로 `BoundaryWidth=20`, 동쪽 경계까지의 index 거리 2를 넣었다. WIDTH=800, idx.x=797이면 γ=0.971993955903이다. WIDTH=802, idx.x=799이면 γ=0.982641514602이다. 두 값은 N13의 코드 식을 Python으로 직접 계산한 값이다. 모델을 실행한 결과가 아니다. 코사인의 주기성 때문에 일부 폭에서 값이 우연히 같을 수 있다. 이 우연은 일반적인 거리 불변성을 보장하지 않는다. 가중 평균 뒤의 보정은 `:396–397`의 상태 평균이며 감쇠 인자의 전체 폭 의존성을 제거하지 않는다. 근거 강도는 **중간**이다. 실제 반사량과 안정성 영향은 검증하지 않았다.

**E2 — CP2-156: 색상 배열의 끝 원소.** 먼저 보정 경로를 찾았다. `shaders/fragment.wgsl:594`는 정규화값을 0–1로 제한한다. 그러나 `:599`는 upperIndex를 제한하지 않는다. 같은 파일의 색상막대 경로 `:907–914`도 같은 index 식을 사용한다. 단면 판 `transect_version/shaders/fragment.wgsl:579–586,836–843`도 같은 식이다. `ebc98a5` 2024-03-13의 `shaders/fragment.wgsl:296–303`에도 같은 상한 계산이 있다. `0f41edc` 2024-06-19 “Portage example / colorbar fix”의 변경을 열었지만 이 상한 계산의 보정은 없다.

해석: 자기 주석의 `// Clamp the position between 0 and 1 to stay within the color map.`와 같은 판 노트의 “16색 LUT 선형보간”을 기준으로 하면 유효 index는 0–15이다. 정규화값 1은 lowerIndex=15, upperIndex=16을 만든다. 반대 근거는 같은 값에서 mixAmount가 0이라는 사실이다. 따라서 이 보고서는 화면에 반드시 오류색이 나타난다고 주장하지 않는다. 잘못된 index가 평가되는 코드 결함 후보로 남긴다. 활성 호출 근거는 `js/main.js:1613`의 fragment.wgsl 로딩과 `:1647–1648`의 2D·3D pipeline 생성이다. 근거 강도는 **중간**이다. 브라우저별 처리와 실제 영상은 확인하지 않았다.

### 5.4 행별 최종 결론

아래 표의 원문 인용과 행 번호는 위 대조 표 및 원문 블록을 함께 참조한다. A 행은 논문의 2019-09-28 공개일과 이력 ID의 날짜·변경 줄을 연결한다. B 행은 동일 문서 내부의 모순 또는 현 노트와 직접 원문·코드의 충돌로 판정했다. X로 넘겨야 할 외부 계수 판정은 이 대조에 남지 않았다. 2019 적응 시간 적분 문헌의 미열람 식을 현재 AB3·AM4 구현의 식으로 확정하지 않았다.

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| CP2-001 | 구현 언어와 플랫폼 | A 판 차이 | p.1 “developed in the Unity3D game engine and in C# language”; “written in HLSL”; `js/Run_Compute_Shader.js:30` `export async function fetchShader(url) {`; `shaders/Pass1.wgsl:54` `@compute @workgroup_size(16, 16) //`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 논문은 2019 Base이다. 현재 구현은 JS 호스트와 WGSL이다. |
| CP2-003 | VR 기능 | D 문서에만 있음 | p.1 “view the simulations in a virtual reality headset”; 5절 검색 D1. 활성 호스트의 VR 세션 진입 코드는 검색되지 않았다.; 5.2의 rg -i·log -S 검색 결과 0. | Base는 VR 헤드셋을 지원했다. 현재 WebGPU 범위의 소스·이력에서는 VR 구현이 검색되지 않았다. |
| CP2-004 | 360도 영상 | D 문서에만 있음 | p.1 “360° video capturing”; p.2 “record a 360° video”; `js/File_Writer.js:346` `export async function createAndDownloadVideoFromTexture(device, texture, textureSize, outputPath='out.mp4', frameRate=24) {`; 5절 검색 D2; 5.2의 rg -i·log -S 검색 결과 0. | Base는 360도 영상 기능을 소개했다. 현재의 일반 영상 저장 함수를 360도 촬영 지원으로 부르지 않는다. |
| CP2-005 | 공개 배포와 라이선스 | H 코드 대조 대상 아님 | p.1 “Program Files doi: http://dx.doi.org/10.17632/jdx7tddcxz.1”; “MIT License”; `README.md:82` ``This project is licensed under the **MIT License**. See the `LICENSE` file for details.`` | 별도 Base 배포물의 식별자이다. 라이선스 이름의 일치는 소스 파일 동일성을 뜻하지 않는다. |
| CP2-006 | 재해 사례와 모형 필요성 | H 코드 대조 대상 아님 | p.1–2 “supercomputing facilities”; “Democratizing high-order and high-performance coastal wave modeling”; 해당 없음. 배경·목적 문장이다. | 재해 연도와 공학적 동기는 실행 코드 대조 대상이 아니다. |
| CP2-007 | Advent 구현 | A 판 차이 | p.2 “C++ and HLSL using the Direct3D framework”; `README.md:25` `Runs entirely client-side in the browser using JavaScript and WGSL shaders via the WebGPU API—no plugins or installations required.`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | Advent·Base·WebGPU의 구현 판을 구별한다. V1을 적용한다. |
| CP2-008 | 이용 수와 예보 사이트 | H 코드 대조 대상 아님 | p.2 “over 2000 times”; “50+ countries”; “five-day forecast”; 해당 없음. 이용 통계와 별도 서비스 사례이다. | 다운로드 수·예보 기간은 모델 함수·기본값이 아니다. |
| CP2-009 | Unity 물리 엔진 비사용 | A 판 차이 | p.2 “We did not use the physics engine of Unity3D”; `js/Run_Compute_Shader.js:61` `const computePass = commandEncoder.beginComputePass();`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | Base의 엔진 선택 설명이다. 현재 코드도 자체 수치 셰이더를 구동하지만 Unity 프로젝트가 아니다. |
| CP2-010 | 다형성·주입·모듈화 | A 판 차이 | p.2 “polymorphism, design patterns, dependency injection”; `js/main.js:23` `import { create_Pass1_BindGroupLayout, create_Pass1_BindGroup } from './Handler_Pass1.js';  // group bindings for Pass1 shaders`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | JS 모듈·handler 구조를 Unity 클래스 설계와 동일시하지 않는다. V1. |
| CP2-011 | Base가 Advent를 대체하지 않는다는 권고 | H 코드 대조 대상 아님 | p.2 “it is not meant to replace it”; “continue using Celeris Advent until new versions ...”; 해당 없음. 해당 시점의 이용 권고이다. | 권고의 조건과 시점을 유지한다. 최신 판 사용 권고로 바꾸지 않는다. |
| CP2-012 | 이론 계보와 타 모형 비교 | H 코드 대조 대상 아님 | p.2–3 “both nonlinearity and frequency dispersion are weak”; “only weakly nonlinear”; FUNWAVE·COULWAVE·현장 불확실성 설명; `js/constants_load_calc.js:36` `NLSW_or_Bous: 0,  // Choose 0 for Non-linear Shallow Water (NLSW), 1 for Madsen Boussinesq, 2 for Fully Non-linear Boussinesq (COULWAVE equations)` | 이론 가정·다른 모형의 사례·비용 주장은 코드 대조 대상이 아니다. 현재 모드 2를 2020 논문이 구현했다고 해석하지 않는다. |
| CP2-013 | 식 (1)의 수심과 연속식 | F 표기 차이 | p.3 식 (1), §1.2 전사. “h is the total water depth”; `shaders/Pass1.wgsl:78` `let h_here = in_here.x - B_here;`; `shaders/Pass3_Bous.wgsl:394` `let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term + vorticity_dissipation;` | 코드는 수면 표고를 저장한다. 고정 바닥이면 $h_t=\eta_t$이다. |
| CP2-015 | 식 (1)의 수압·바닥 경사·부호 | F 표기 차이 | p.3 식 (1)의 $(gh^2/2)_x+ghz_x$ 및 y 성분; `shaders/Pass3_Bous.wgsl:392` 아래 인용 N2. | $h=\eta-z$이면 $ghh_x+ghz_x=gh\eta_x$이다. 좌변 항을 우변으로 옮긴 코드는 `-globals.g * h_here * detadx`이다. |
| CP2-018 | 식 (2)의 x 분산항 전체 | F 표기 차이 | p.3 식 (2), §1.2 전사; `shaders/Pass3_Bous.wgsl:269–273,282–283` N3. `shaders/Update_TriDiag_coef.wgsl:67–69` N4. | $P_t$의 x 방향 자기 미분은 삼중대각 연산자에 들어간다. $Q_t$ 혼합항은 `F_star`의 시간 차분에 들어간다. |
| CP2-019 | 식 (3)의 y 분산항 전체 | F 표기 차이 | p.3 식 (3), §1.2 전사; `shaders/Pass3_Bous.wgsl:275–279,285–286` N3. `shaders/Update_TriDiag_coef.wgsl:101–103` N4. | $Q_t$의 y 방향 자기 미분은 y 삼중대각 연산자에 들어간다. $P_t$ 혼합항은 `G_star`에 들어간다. |
| CP2-023 | 나머지 항의 2차 중앙차분 | A 판 차이 | p.3 “The rest of the terms are discretized using second order central FDM.”; `shaders/Pass3_Bous.wgsl:240` `// replace with 4th order when dispersion is included`; `:241–242` N7; `:262–266` N8; 논문 공개 2019-09-28; V3 (f18955b, 2024-10-01) | 현재 코드는 분산 구간의 수면·수심 1차 미분에 4차 중앙차분을 사용한다. 2차·혼합 미분은 여전히 2차이다. |
| CP2-024 | 시간 적분 차수와 선택 | A 판 차이 | p.3 “third-order fixed timestep Adams–Bashforth scheme”; `js/constants_load_calc.js:32` `timeScheme: 2,  // Time integration choices: 0: Euler, 1: 3rd-order A-B predictor, 2: A-B 4th-order predictor+corrector.`; `shaders/Pass3_Bous.wgsl:399–410` N9; 논문 공개 2019-09-28; V4 (fd57bb7, 2023-10-09; 63a12e3, 2023-10-19) | `timeScheme=1`의 예측식은 3차 AB이다. 기본 `2`는 별도 4차 Adams–Moulton 보정식을 실행한다. |
| CP2-026 | 직접 쇄파 처리의 부재 | A 판 차이 | p.3 “does not have a direct treatment for wave breaking”; `js/constants_load_calc.js:56` `useBreakingModel: 1, // inlcude breaking model when == 1`; `shaders/Pass3_Bous.wgsl:343–364` N10; `js/main.js:2652` `if(calc_constants.useBreakingModel == 1) {`; 논문 공개 2019-09-28; V5 (366ee34, 2024-04-08) | 현재 기본 경로는 명시적 쇄파 점성항을 포함한다. minmod 소산과 쇄파 모형을 같은 처리로 적지 않는다. |
| CP2-029 | 네 종류 경계의 목록 | A 판 차이 | p.3 “fully reflective solid wall, sinewave maker, sponge layer, and irregular wavemaker”; `js/constants_load_calc.js:63–68`의 `*_boundary_type`, `incident_wave_type`; `shaders/BoundaryPass.wgsl:448–455` N12; 논문 공개 2019-09-28; V6 (38a5072, 2025-01-21) | 현재 코드는 경계 유형과 입사파 유형을 분리한다. 사인파와 불규칙파는 주로 경계 유형 2 아래의 분기이다. |
| CP2-031 | 불규칙 조파의 외부 설명 | H 코드 대조 대상 아님 | p.3 “the irregular wavemaker is discussed in [24]”; `js/File_Loader.js:290` `const numberOfWaves = parseInt(lines[0].split(' ')[1], 10);`; `:292` `const waveData = lines.slice(2).map(line => line.trim().split(/\s+/).map(Number));` | 이 문장은 해법을 [24]로 위임한다. [24]의 계수와 스펙트럼 공식을 이 논문의 직접 설명으로 취급하지 않는다. |
| CP2-033 | Fig. 1 | H 코드 대조 대상 아님 | p.3 “Diagram of γ(α), Eq. (4), inside the sponge layer.”; 해당 없음. 식 (4)의 그래프이다. | 가로축 $D(\alpha)/L_s$는 0–1이다. 세로축 $\gamma(\alpha)$는 0–1이다. |
| CP2-034 | 식 (4)의 감쇠와 적용 대상 | A 판 차이 | p.3 식 (4), §1.2 전사. “multiplying the values of η, P, and Q”; “only ... inside the sponge layer”; `shaders/BoundaryPass.wgsl:104–108` N13; `:360–366` N14; 논문 공개 2019-09-28; V2 (cf9de63, 2023-10-24) | 현재 감쇠식에는 바깥 계수 `0.5`와 지수 `0.005`가 있다. `dt`·파속·감쇠 비율은 없다. |
| CP2-035 | Advent v1.0.0의 반복 감쇠 문제 | H 코드 대조 대상 아님 | p.3–4 “every time-step”; “higher for smaller timesteps”; $H_0$, $\gamma(L_s-\delta)$, $\gamma(L_s-2\delta)$; `shaders/BoundaryPass.wgsl:105` N13의 감쇠식 | 논문은 과거 Advent 실험의 불필요한 반사와 시간 간격 의존성을 설명한다. 현재 코드에서도 `dt` 없는 반복 감쇠를 확인했지만 같은 반사량을 단정하지 않는다. |
| CP2-036 | 식 (5)의 누적곱 | H 코드 대조 대상 아님 | p.4 식 (5), §1.2 전사; 직접 코드 대응 없음. | 목표 감쇠를 만드는 계수의 수학적 정의이다. $i=0$에서 시작하는 곱을 그대로 유지한다. |
| CP2-037 | 식 (6)의 재귀식 | H 코드 대조 대상 아님 | p.4 식 (6), §1.2 전사; 직접 코드 대응 없음. | 식 (5)의 한 인자를 분리한 관계이다. 현재 셰이더 호출 순서로 해석하지 않는다. |
| CP2-038 | 식 (7)의 비율식 | H 코드 대조 대상 아님 | p.4 식 (7), §1.2 전사; 직접 코드 대응 없음. | 분모는 직전 위치의 목표 감쇠이다. 현재 코드의 `pow`와 같은 식이 아니다. |
| CP2-039 | 식 (8)의 변수 치환 | H 코드 대조 대상 아님 | p.4 식 (8), §1.2 전사. “Substituting Ls − nδ ... α”; 직접 코드 대응 없음. | $\alpha=L_s-n\delta$를 넣으면 분모는 $\gamma(\alpha+\delta)$이다. 부호를 빼기로 바꾸지 않는다. |
| CP2-040 | 식 (9)의 실제 감쇠 | A 판 차이 | p.4 식 (9), §1.2 전사. $\delta$는 $\Delta t$ 동안 마루가 진행한 거리이다.; `shaders/BoundaryPass.wgsl:105,111,117,123` N13과 5절 V2; 논문 공개 2019-09-28; V2 (cf9de63, 2023-10-24) | 현재 네 감쇠 함수는 $\gamma(\alpha)/\gamma(\alpha+c\Delta t)$를 계산하지 않는다. V2는 2023년의 다른 감쇠식을 보여 준다. |
| CP2-041 | 감쇠 파속 근사 | A 판 차이 | p.4 번호 없는 식 $c=\sqrt{gd}$; “at each time-step”; `shaders/BoundaryPass.wgsl:104–125`의 네 감쇠 함수에는 `c`, `dt`, `d`를 사용하는 감쇠 계산이 없다.; 논문 공개 2019-09-28; V2 (cf9de63, 2023-10-24) | 조파 함수의 파속 계산과 스펀지 감쇠 계산을 구별한다. 이력 V2. |
| CP2-042 | Assets와 진입 파일 | A 판 차이 | p.4 “Assets ... Celeris”; “GameManager.cs”; “Main.unity”; `js/main.js:23`의 JS 모듈 import; `README.md:61` ``Open `http://localhost:8000` in a WebGPU-enabled browser. No build step required—just refresh after code changes.``; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 현재 진입점은 HTML과 JS이다. Unity scene을 열라는 지침은 Base용이다. |
| CP2-043 | 해석기 상속 관계 | A 판 차이 | p.4 “TL17Driver.cs”; “KP07Driver.cs”; “KP07Base.cs”; “Solver.cs”; “virtual ... TimeStep()”; `js/main.js:2679`의 `Pass3_Pipeline_Bous` 호출; `:2682`의 `Pass3_Pipeline_NLSW` 호출; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 현재는 모드 분기와 공통 패스이다. Unity 상속 계층을 현재 파일 구조로 인용하지 않는다. |
| CP2-044 | 계산 셰이더 include와 렌더 파일 | A 판 차이 | p.4 “TL17.compute and KP07.compute”; “base_KP07.compute”; “time_integration.compute, tools.compute”; “.shader ... .cginc ... Material”; `js/main.js:1564` `var Pass3_ShaderCode_Bous = await fetchShader('/shaders/Pass3_Bous.wgsl');`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | WGSL 파일별 pipeline 구성이 HLSL include 체계를 대신한다. 남아 있는 `.compute` 확장자만으로 이 체계가 유지된다고 보지 않는다. |
| CP2-045 | Unity 오브젝트와 프레임 갱신 | A 판 차이 | p.4 “Main Camera, GameManager, Engine, and Canvas”; “singleton”; “Instance”; “Update”; “over 140,000”; “Unity3D 2018 ... Visual Studio 2018”; `js/main.js:1685` `const gridWidth = calc_constants.WIDTH;  // Number of vertices along the width`; `README.md:61`의 브라우저 진입; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 현재 코드는 DOM·JS·WebGPU 렌더 루프를 사용한다. `Canvas` GameObject와 HTML canvas를 동일 객체로 부르지 않는다. |
| CP2-046 | 경계 UI 연결 | A 판 차이 | p.5 “BoundaryPanelScript”; “takes the values ... from the GUI and updates the simulation parameters”; `river.html:728` `<select id="west_boundary_type-select" name="west_boundary_typeValue">`; `js/main.js:4767` `{ input: 'useBreakingModel-select', property: 'useBreakingModel' },`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 입력을 모델 설정으로 연결하는 역할은 이어진다. 연결 단위는 Unity Component에서 DOM event로 바뀌었다. |
| CP2-047 | NLSW와 TL17의 구분 | A 판 차이 | p.5 “two fluid dynamics models”; “KP07”; “TL17”; `js/constants_load_calc.js:36`의 `0`, `1`, `2` 선택문 원문은 CP2-012에 인용했다.; 논문 공개 2019-09-28; V7 (0b4e990, 2025-05-16) | 현재 모드는 NLSW·Madsen Boussinesq·완전비선형 COULWAVE의 세 종류이다. 논문이 세 번째 모드를 설명한다고 쓰지 않는다. |
| CP2-048 | KP07 인용번호 | B 문서 오기 | p.5 “Kurganov and Petrova (2007) [21]”; p.13 [20] `A. Kurganov, G. Petrova, Commun. Math. Sci. 5 (2007) 133–160.`; [21]은 Shi et al. (2012)이다. | p.5의 KP07 인용번호 [21]은 같은 논문의 [20]으로 고친다. |
| CP2-049 | Solver의 책임·가상 함수 | A 판 차이 | p.5 “does not implement the functions to solve any equations”; “virtual TimeStep()”; `js/Run_Compute_Shader.js:55` `export function runComputeShader_EncStack(device, commandEncoder, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 현재 공통 GPU 구동 함수는 상속의 가상 메서드가 아니다. V1. |
| CP2-050 | 텍스처 생성·수명 관리 | A 판 차이 | p.5 “simTextureManager ... creating and destroying ... to prevent memory leaks”; `js/Create_Textures.js:3` `const texture = device.createTexture({`; `:10` `allTextures.add(texture);`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 현재 구현은 JS의 텍스처 생성 함수와 추적 집합을 사용한다. `RenderTexture` 또는 `TextureFactory` 클래스의 존재를 주장하지 않는다. |
| CP2-052 | Fig. 2의 파일과 경로 | A 판 차이 | p.5 Fig. 2 “Some of the important source files”; `CML Examples`, `Materials`, `Prefabs`, `Scripts`, `GPGPU`, `Mouse`, `Solvers`, `Scenes`, `Textures`, `Third Party`; `ARCHITECTURE.md:3` ``The source files in `js/` and `shaders/` are the application.``; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 그림의 CML·CBF, Buoy prefab, ReadCBF·ReadCML·SimSetting·Singleton, MapManager, PointerGauge, IrregularWaves·KernelLookUp, HLSL 공통 파일, Main.unity는 Base 구조이다. 자산·외부 라이브러리 내부는 판독하지 않았다. |
| CP2-053 | Fig. 3의 UML | A 판 차이 | p.6 Fig. 3 “Class UML diagram”; `Solver → KP07Base → KP07Driver/TL17Driver`; `Setup`, `TimeStep`, `logToFile`, `updateTexturesForRender`, `ABC`, `BCoef`; `js/Run_Tridiag_Solver.js:3` `export function runTridiagSolver(`; `js/Create_Textures.js:2` `export function create_2D_Texture(device, width, height, allTextures) {`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 그림은 상속·접근 제어·클래스 멤버를 설명한다. 현재 모듈 간 호출 관계로 재사용할 수 없다. |
| CP2-055 | NLSW pass3과 시간 적분 | A 판 차이 | p.6 “pass3 ... sums up the fluxes and source terms”; “then a time integration method”; `js/main.js:2682`의 `Pass3_Pipeline_NLSW` 호출; `shaders/Pass3_Bous.wgsl:394–409` N2·N9는 대응하는 Boussinesq 경로이다.; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09), V4 (fd57bb7, 2023-10-09; 63a12e3, 2023-10-19) | 현재 pass3 셰이더가 RHS 조립과 시간 적분을 함께 수행한다. CPU의 별도 가상 시간 적분 함수가 아니다. |
| CP2-059 | compute Dispatch | A 판 차이 | p.6 “driving ... simply done with ... Dispatch”; “DirectCompute”; “CUDA”; `js/Run_Compute_Shader.js:68` `computePass.dispatchWorkgroups(dispatchX, dispatchY);`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 계산 전용 GPU 호출의 목적은 같다. Unity `Dispatch`와 WebGPU API의 호출 규약은 다르다. |
| CP2-060 | Unity heightmap과 외부 렌더 도구 | H 코드 대조 대상 아님 | p.6 “only takes square shapes”; “Surface Waves by Code Animo”; “commercial library”; 해당 없음. Unity와 외부 라이브러리의 제약·선택 설명이다. | 라이브러리 내부를 모델 완료 조건으로 삼지 않는다. |
| CP2-061 | 128×128 타일 | A 판 차이 | p.6 “square grids of size 128 × 128”; “scale up ... in one direction”; `js/main.js:1685–1686` `const gridWidth = calc_constants.WIDTH;  // Number of vertices along the width` / `const gridHeight = calc_constants.HEIGHT; // Number of vertices along the height`; 논문 공개 2019-09-28; V8 (471c581, 2024-01-04) | 현재 3D 격자는 전체 WIDTH·HEIGHT로 만든다. 128 크기 타일 묶음이 아니다. |
| CP2-062 | 타일 수 반올림과 최솟값 | A 판 차이 | p.7 “rounding ... nearest integer”; “at least two tiles in each direction”; `js/main.js:1690–1700`의 전체 grid strip 생성. `:1694` `for (let x = 0; x < gridWidth; x++) {`; 논문 공개 2019-09-28; V8 (471c581, 2024-01-04) | 현재 3D 격자 생성에는 `round(nx/128)`·방향별 최소 두 타일 규칙이 없다. V8. |
| CP2-063 | 계산 격자와 렌더 격자의 UV 연결 | A 판 차이 | p.7 “not a 1:1 match”; “linear UV mapping ... sampling the compute textures”; `shaders/vertex3D.wgsl:75` `out.uv = v.pos * 0.5 + 0.5;`; `:78` `var elev = textureLoad(etaTexture, vec2<i32>(i32(out.uv.x * f32(globals.WIDTH - 1)), i32(out.uv.y * f32(globals.HEIGHT - 1))), 0).r;`; 논문 공개 2019-09-28; V8 (471c581, 2024-01-04) | 현재도 UV를 사용한다. 현재 3D 격자는 WIDTH·HEIGHT의 texel 위치를 직접 읽는다. |
| CP2-064 | Fig. 4 | A 판 차이 | p.7 “Rendering infrastructure ... disassembled tiles”; `js/main.js:1695–1696`의 두 strip 정점 추가문; 논문 공개 2019-09-28; V8 (471c581, 2024-01-04) | 그림은 Base 타일을 분리한 구조도이다. 축·물리 단위·정량 검증 곡선은 없다. |
| CP2-065 | Fig. 5 | A 판 차이 | p.7 “grid (a), jet colormapping (b), and terrain colormapping (c)”; `shaders/fragment.wgsl:165` `} else if(colorMap_choice == 1) {  // parula colormap`; `:183` `} else if(colorMap_choice == 2) {  // turbo colormap`; `:255` `}  else if(colorMap_choice == 6) {  // haxby for bathy/topo colormap`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 그림은 격자·jet·수중/육상 색상 띠이다. 현재 코드의 수치 RGB 배열은 이 텍스처 세 장을 그대로 읽는 구조가 아니다. |
| CP2-067 | photorealistic.shader와 격자 재질 | A 판 차이 | p.7 “SimpleWater.mat”; “light and skybox reflection”; “grid texture ... sampled, scaled, color reversed”; `shaders/fragment.wgsl:730` `color_rgb = light_effects * color_wave;`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 현재 수면 색 계산은 WGSL이다. Unity 재질·텍스처 기반 격자 처리와 파일명을 동일시하지 않는다. |
| CP2-068 | WaterColormap·TerrainColormap | A 판 차이 | p.7 “WaterColormap.shader”; “TerrainColormap.shader”; “a colormapped texture ... as an input”; `shaders/fragment.wgsl:598` `let lowerIndex = i32(floor(wavePosition * 15.0)); // Because we have 16 colors.`; `:605` `let color_wave = mix(colorMap[lowerIndex], colorMap[upperIndex], mixAmount);`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 현재는 RGB 배열의 이웃 원소를 보간한다. 텍스처의 V=0.5 단면을 샘플하는 체계와 다르다. |
| CP2-069 | 식 (10)의 정규화 | F 표기 차이 | p.8 식 (10), §1.2 전사. “any value between 0 and 1 can be used for V”; `shaders/fragment.wgsl:591` `var wavePosition = f32((render_surface - minWave) / (maxWave - minWave));` | $C=render\_surface$, $C_{min}=minWave$, $C_{max}=maxWave$이면 같은 정규화이다. 현재 색상 배열에는 V 좌표가 필요하지 않다. |
| CP2-070 | 식 (11)의 수중 분모 | B 문서 오기 | p.8 식 (11)의 $U=(C-C_{\min})/C_{\min}$, $C\leq0$; 비교 근거는 같은 쪽의 0–1 UV 설명과 Fig. 5c이다. 현재 `shaders/fragment.wgsl:586` `color_rgb = vec3<f32>(210.0 / 255.0, 180.0 / 255.0, 140.0 / 255.0) + 0.25 * (bottom - globals.bathy_cmap_zero) / globals.base_depth;`는 다른 색식이다. | 식 (11)은 수중 가지의 분모 부호에 오기가 있다. 인쇄 원문과 보정 해석을 구별한다. |
| CP2-071 | Fig. 6 | H 코드 대조 대상 아님 | p.8 “four snapshots stitched to each other”; “different sky and grid options”; 해당 없음. Base 렌더 결과의 사례 그림이다. | 서로 다른 하늘 두 종류와 격자 표시 조합을 확인했다. 축·범례·정량 성능 자료는 없다. |
| CP2-072 | 지도 위치 입력 | A 판 차이 | p.8 “latitude and longitude of the center ... given in the CML input file”; `js/File_Loader.js:545` `function calculateZoomLevel(lat_LL, lon_LL, lat_UR, lon_UR, maxWidth, maxHeight) {`; 논문 공개 2019-09-28; V9 (2eb2866, 2023-10-26) | 현재 지도 API는 좌하단·우상단 좌표를 인자로 받는다. 중심점과 미터 폭에서 모서리를 계산하는 CML 입력과 다르다. |
| CP2-074 | 식 (12)의 경도 정규화 | F 표기 차이 | p.8 식 (12), §1.2 전사. `lon`의 단위는 radians; `js/File_Loader.js:572` `var lngFraction = lngDiff / 360;` | 코드의 `lngDiff`는 도 단위 차이다. $\Delta lon/(2\pi)=\Delta M_x/2=\Delta lon_{deg}/360$이다. |
| CP2-075 | 식 (13)의 위도 투영 | F 표기 차이 | p.8 식 (13), §1.2 전사; `js/File_Loader.js:685–689` 아래 지도 원문 M1 | $\ln[(1+\sin lat)/(1-\sin lat)]=2\ln\tan(\pi/4+lat/2)$이다. 코드의 $y=(1-M_y)/2$는 원점·방향·범위를 바꾼 같은 Mercator 투영이다. |
| CP2-076 | 극점 절단 | F 표기 차이 | p.8 번호 없는 관계 $M_y=\pm1$; “±85.051129°”; `js/File_Loader.js:551–553` `var sin = Math.sin(lat * Math.PI / 180);` / `var radX2 = Math.log((1 + sin) / (1 - sin)) / 2;` / `return Math.max(Math.min(radX2, Math.PI), -Math.PI) / 2;` | 줌 계산은 투영 좌표를 ±π로 제한한 뒤 반으로 나눈다. 지도 UV의 M1 함수에는 같은 clamp가 없다. |
| CP2-077 | 줌의 타일 수 | H 코드 대조 대상 아님 | p.8 번호 없는 관계 $2^{zoom}$, $zoom=0$, $zoom=2$, $2^2\times2^2=16$; `js/File_Loader.js:558` `return Math.floor(Math.log(mapPx / worldPx / fraction) / Math.LN2);` | 타일 수 관계는 지도 API의 수학적 배경이다. 수치해석 격자 수를 뜻하지 않는다. |
| CP2-078 | 모서리·줌 역계산 | A 판 차이 | p.8 “haversine formula ... distances in meters ... to lon and lat”; “covers the entire simulation field”; `js/File_Loader.js:577–583` 아래 M2; 논문 공개 2019-09-28; V9 (2eb2866, 2023-10-26) | 현재 코드는 주어진 모서리의 위도·경도 범위와 256픽셀 세계 타일 크기로 줌을 구한다. 최대 줌은 21이다. |
| CP2-080 | GoogleStaticMap·Lean Go Maps | H 코드 대조 대상 아님 | p.8 “part of a Unity3D asset, Lean Go Maps”; MIT; 외부 저장소 주소; 해당 없음. 외부 자산과 배포 설명이다. | 외부 라이브러리 내부와 서비스 구현은 판독 범위 밖이다. 현재 호스트 대응은 CP2-072·073·078이다. |
| CP2-081 | Fig. 7 | H 코드 대조 대상 아님 | p.9 “Geographic map of the coast of Newport, OR”; 해당 없음. Base가 받은 지도 사례이다. | 지도에는 Google·Imagery ©2018 TerraMetrics 표기가 있다. 수치 축·격자 간격·정량 검증 자료는 없다. |
| CP2-082 | 포인터의 ray–수평면 교점 | A 판 차이 | p.9 “casts a ray”; “intersection ... with a horizontal plane ... mean sea-level”; `js/main.js:4536–4537` `const normalizedX = (x - bounds.left) / bounds.width; //normalizedX;` / `const normalizedY = 1.0 - (y - bounds.top) / bounds.height; //normalizedY;`; `:4543–4544` 아래 U1; 논문 공개 2019-09-28; V10 (efe44a2, 2024-04-02) | 현재 tooltip은 canvas 위치를 정규화하여 텍스처 index를 정한다. ray와 정수면 교점을 계산하는 절차가 아니다. |
| CP2-083 | 포인터 위치 오차 설명 | H 코드 대조 대상 아님 | p.9 “flow parameters always correspond to the gauge location, even if ... not precisely under the mouse pointer”; “computationally expensive”; 해당 없음. Base 위치 추정의 오차·계산비용 설명이다. | 실제 수면 교점과 평균 수면 교점이 다르다는 조건을 유지한다. 현재 3D 탐색의 정확도를 이 문장으로 검증하지 않는다. |
| CP2-084 | GetPixel readback | A 판 차이 | p.9 “reads the flow data from the textures using the GetPixel method”; `js/Time_Series.js:86` `await buffer.mapAsync(GPUMapMode.READ);`; `:90` `const bufferCopy = new Float32Array(arrayBuffer.slice(0, bytesPerPixel * (calc_constants.NumberOfTimeSeries + 1)));`; 논문 공개 2019-09-28; V10 (efe44a2, 2024-04-02) | 현재는 추출 compute pass 뒤 GPU buffer를 비동기 readback한다. Unity GetPixel 호출이 아니다. |
| CP2-086 | 부이 개수·배치·삭제 | A 판 차이 | p.9 “A maximum of five”; “clicking on the scene”; “plotter legend ... Ctrl”; `js/constants_load_calc.js:262` `maxNumberOfTimeSeries: 16, // max number of time series allowed, inlcuding tooltip, if greater than 16, need to update readToolTipTextureData bytesperrow.  SHould be 16*N time series`; `index.html:1023` `<select id="NumberOfTimeSeries-select" name="NumberOfTimeSeriesValue">`; `index.html:1085`의 위치 입력 label; 논문 공개 2019-09-28; V10 (efe44a2, 2024-04-02) | 현재 texture slot 0은 tooltip이다. 계측점의 UI 상한은 15이다. |
| CP2-087 | XML CML 설정 | A 판 차이 | p.9 “XML file ... input CML file”; `js/constants_load_calc.js:438` `var configJson = JSON.parse(configContent);`; `:424–425` `loadedConfig = await response.json();` / `calc_constants = { ...calc_constants, ...loadedConfig };`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09), V11 (254d71c, 2023-10-09; cf9de63, 2023-10-24) | 현재 설정은 JSON이다. CML tag 이름을 현재 매개변수 키로 추측하지 않는다. |
| CP2-088 | CBF header | A 판 차이 | p.9 “CBF file starts with tags which determine the resolution”; `js/File_Loader.js:39–41` `for (let y = 0; y < calc_constants.HEIGHT; y++) {` / `// Split each line by spaces or tabs.` / `const depthValues = lines[y].split(/\s+/).filter(Boolean);`; 논문 공개 2019-09-28; V11 (254d71c, 2023-10-09; cf9de63, 2023-10-24) | 현재 loader는 첫 줄부터 숫자 행으로 읽는다. CBF 해상도 tag를 처리하지 않는다. |
| CP2-090 | 수심 격자 보간 | A 판 차이 | p.9 “If ... resolutions ... are different ... use interpolation”; `js/File_Loader.js:43–46` 아래 U3; 논문 공개 2019-09-28; V11 (254d71c, 2023-10-09; cf9de63, 2023-10-24) | 현재 loader는 행의 원소 수가 WIDTH와 다르면 `null`을 반환한다. 다른 크기의 bathy를 자동 보간하는 Base 절차가 아니다. |
| CP2-091 | Advent와 같은 출력 형식 | A 판 차이 | p.9 “same format for input and output files as in Celeris Advent”; `js/Time_Series.js:166` ``headers += `Time${i+1}\tEta${i+1}\tP${i+1}\tQ${i+1}\t`;``; `js/File_Writer.js:560` ``let filename = `elev_${frame_count_output}.bin`;``; 논문 공개 2019-09-28; V11 (254d71c, 2023-10-09; cf9de63, 2023-10-24) | Tavakkol 2017 PDF p.6(인쇄 p.122)는 formatted ASCII 출력을 명시한다. 현재의 텍스트 시계열·float32 binary와 Base의 형식 승계 문장을 구별한다. |
| CP2-092 | 플랫폼 지원의 한계 | H 코드 대조 대상 아님 | p.9 “not a guarantee ... all ... platforms”; “early stages ... Linux”; “expect”; 해당 없음. Base의 개발 환경·시험 이력·전망이다. | Linux 지원을 무조건 보장한다는 문장으로 바꾸지 않는다. 현재 브라우저 실행은 확인하지 않았다. |
| CP2-093 | Fig. 8 | H 코드 대조 대상 아님 | p.10 “Simulation of the coast of Newport, OR ... geographic map”; `shaders/fragment.wgsl:284` `let GoogleMap = textureSample(txOverlayMap, textureSampler, uv_mod).rgb;` | 그림은 Base 지도 중첩 사례이다. 축과 정량 검증값은 없다. |
| CP2-094 | Fig. 9의 포인터 표시 | A 판 차이 | p.10 “Mouse pointer acts as a gauge”; X 1583.5190, Y 6027.1930, Z −17.7326, Eta 0.3306, U 0.2338, V −0.0225; `shaders/ExtractTimeSeries.wgsl:53` `output = vec4<f32>(bottom, waves, hsig, friction);`; `js/main.js:4586`의 `sig wave height (m)` tooltip; 논문 공개 2019-09-28; V10 (efe44a2, 2024-04-02) | Base 화면은 X/Y/Z/Eta/U/V를 표시한다. 현재 기본 tooltip의 네 값은 바닥·수면·유의파고·마찰이다. |
| CP2-095 | 텍스처 범위 밖 접근의 플랫폼 차이 | H 코드 대조 대상 아님 | p.10 “DirectX ... returning zero”; “may cause a crash”; “must be found and removed”; 해당 없음. 다른 플랫폼으로 이식할 때의 외부 API 동작·의무 설명이다. | 이 문장을 현재 WGSL의 모든 범위 밖 접근이 안전하다는 근거로 쓰지 않는다. |
| CP2-096 | Unity Windows 빌드 절차 | H 코드 대조 대상 아님 | p.10 “File > Build Setting”; “PC, Mac & Linux Standalone”; “target platform ... Windows”; `README.md:61`의 “No build step required” | 외부 도구 사용법이다. Base 빌드 절차를 WebGPU 실행 지침으로 쓰지 않는다. |
| CP2-097 | 실행 파일·setting.init·파일 탐색기 | A 판 차이 | p.10 “running the executable file”; “setting.init”; “if a path ... is not provided ... file browser”; `index.html:1597` `<script type="module" src="js/main.js"></script>`; `js/constants_load_calc.js:419` `const filePath = calc_constants.exampleDirs[calc_constants.run_example] + 'config.json';`; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09), V11 (254d71c, 2023-10-09; cf9de63, 2023-10-24) | 현재는 HTML 모듈과 업로드/예제 설정 경로이다. 실행 파일 옆의 setting.init을 우선 읽는 절차가 아니다. |
| CP2-098 | 지도 API 키 제공 위치 | A 판 차이 | p.10 “API key must be provided in the GoogleStaticMap.cs file”; `js/File_Loader.js:605` `url.searchParams.set('key', apiKey);`; 논문 공개 2019-09-28; V9 (2eb2866, 2023-10-26) | 현재 요청 생성은 JS 함수이다. Base의 C# 파일명은 현재 API 키의 위치 안내로 사용할 수 없다. |
| CP2-099 | VR의 일반적 동작과 기대 효과 | H 코드 대조 대상 아님 | p.10–11 “in accordance with user’s real time movement”; 가상 박물관·항만·교육 수조의 예; 해당 없음. 기술 정의와 가능한 적용 시나리오이다. | 제안된 가상 실험실을 실제 구현된 협업 기능으로 바꾸어 쓰지 않는다. |
| CP2-100 | Fig. 10 | H 코드 대조 대상 아님 | p.11 “Deploying virtual buoys in Celeris Base.”; `js/main.js:5419` `text: 'Time (s)'`; `:5425` `text: 'Elevation (m)'` | Base 그림은 부이와 색별 곡선을 함께 보여 준다. 그림의 세로 눈금은 −1–1이다. |
| CP2-101 | Oculus Rift 대상 | D 문서에만 있음 | p.11 “targeted ... Oculus Rift headsets”; “as of 2019”; 검색 D1. VR API와 headset 구현은 범위 내 소스·이력에서 검색되지 않았다.; 5.2의 rg -i·log -S 검색 결과 0. | Oculus Rift는 2019 Base의 대상 장치이다. 현재 WebGPU의 지원 장치로 기재하지 않는다. |
| CP2-102 | VR 활성화 설정 | H 코드 대조 대상 아님 | p.11 “Edit > Project Settings > Player”; “checking a checkbox”; 해당 없음. Unity 편집기 조작이다. | 외부 도구 사용법이다. VR 이동·상호작용에는 추가 작업이 필요하다는 다음 문장의 조건을 유지한다. |
| CP2-103 | VR 통합과 외부 도구 | H 코드 대조 대상 아님 | p.11 “there still is need for some development and integration efforts”; “ready to use libraries and Unity assets”; 해당 없음. 개발 작업·외부 도구의 설명이다. | 체크박스 한 번으로 이동·상호작용까지 완성된다고 요약하지 않는다. |
| CP2-104 | VR 이동·회전 조종 | D 문서에만 있음 | p.11 “left controller ... move”; “right ... rotate”; “physically rotating”; 검색 D1. `js/main.js:4259` `} else if (event.button === 0 && event.ctrlKey && calc_constants.viewType == 2) {`는 마우스 탐색 분기이다.; 5.2의 rg -i·log -S 검색 결과 0. | Base의 왼손 이동·오른손 회전 조종을 현재 WebGPU 기능으로 승계하지 않는다. |
| CP2-105 | Fig. 11 | H 코드 대조 대상 아님 | p.11 “Movement control in Celeris VR.”; 해당 없음. 장치 조작 그림이다. | 왼손 Planar Move·Move Fast·Move Up·Move Down과 오른손 Rotate Left/Right를 확인했다. 외부 장치 사용법으로 분류한다. |
| CP2-106 | 선행 연구·개발 시간·현장감 주장 | H 코드 대조 대상 아님 | p.11 “to the best of our knowledge”; “no prior work”; “could have taken”; “unique experience”; 해당 없음. 저자의 인지 범위·반사실적 추정·체험 주장이다. | 한정어를 삭제하지 않는다. GPU 코드 존재만으로 최초성·시간 절감량을 판정하지 않는다. |
| CP2-107 | Celeris VR 공개와 외부 라이선스 | H 코드 대조 대상 아님 | p.11 “MIT License”; “external libraries ... their own licenses”; 해당 없음. Base 위에 만든 별도 배포물의 라이선스 설명이다. | 모든 외부 라이브러리가 MIT라는 문장으로 바꾸지 않는다. |
| CP2-108 | 원뿔섬 실험의 기하와 수조 | H 코드 대조 대상 아님 | p.11 “7.2 m base diameter and side slope”; “30 m x 25 m”; “0.32 m depth”; 해당 없음. `examples/`는 사용자 지정 판독 제외 범위이다. | 실험 조건이다. 원문은 side slope 뒤의 수치를 인쇄하지 않았다. |
| CP2-109 | 목표 상대파고와 선택 이유 | H 코드 대조 대상 아님 | p.11 번호 없는 식 $H/d=0.20$; “only simulate ... higher non-linearity and wave breaking ... expected ... more challenging”; 해당 없음. 사례 선택과 목표 조건이다. | 목표값을 실제 투입 상대파고 0.18과 구별한다. 파고·수심 비는 무차원이다. |
| CP2-110 | Fig. 12 | H 코드 대조 대상 아님 | p.12 “Simulating a coastal area with Celeris VR.”; 해당 없음. VR 사용 사례 사진이다. | 헤드셋·두 조종기·투사 화면과 두 부이 곡선을 확인했다. 성능 축과 수치 검증 지표는 없다. |
| CP2-111 | Fig. 13의 기하·계측점 | H 코드 대조 대상 아님 | p.12 “Experimental setup ... wave approaches ... from the left”; 원 지름 7.2 m·4.64 m·2.20 m; 해당 없음. 실험 배치 그림이다. | x·y 축 단위는 m이다. 초기 해안선은 점선 원이다. |
| CP2-112 | 수치 영역과 초기조건 | H 코드 대조 대상 아님 | p.11–12 “30 m × 30 m”; “island in the center”; “solitary wave ... initial condition near ... west boundary”; `shaders/AddDisturbance.wgsl`의 고립파 기능은 별도이다. 사례 입력 파일은 열지 않았다. | 실험 수조 30×25 m와 수치 영역 30×30 m를 구별한다. 현재 일반 기본 영역을 30×30 m라고 쓰지 않는다. |
| CP2-113 | 검증 사례 경계 | H 코드 대조 대상 아님 | p.12 “west and east ... sponge”; “north and south ... fully reflective solid walls”; `js/constants_load_calc.js:63–66`의 일반 기본 경계는 모두 0이다. | 논문은 특정 검증 사례의 경계를 정했다. 현재 일반 기본값과 달라도 코드 결함이 아니다. |
| CP2-114 | 검증 사례 격자 | H 코드 대조 대상 아님 | p.12 “301 × 301 cells”; `js/constants_load_calc.js:23–24` `WIDTH: 800,  // Width of the computational domain.` / `HEIGHT: 600,  // Height of the computational domain.` | 사례의 계산 셀 수이다. $\Delta x=30/301$ 또는 $30/300$ 중 하나를 이 문장만으로 추가 확정하지 않는다. |
| CP2-115 | 검증 사례 시간 간격 | H 코드 대조 대상 아님 | p.12 “a timestep of 0.0025 s”; `js/constants_load_calc.js:486`의 `dt` 산식은 CP2-025에 인용했다. | 0.0025 s는 이 사례의 값이다. 현재 전체 모형의 고정 기본값이 아니다. |
| CP2-116 | 검증 사례 무마찰 | H 코드 대조 대상 아님 | p.12 “Bottom friction is not applied.”; `js/constants_load_calc.js:46` `friction: 0.000,  // Dimensionless friction coefficient, or Mannings 'n', depending on isManning choice.` | 사례 설정이다. 현재 기본값이 0이어도 모든 업로드 마찰맵이 꺼진다는 뜻은 아니다. |
| CP2-117 | 실제 상대파고 | H 코드 대조 대상 아님 | p.12 번호 없는 식 $H/d=0.18$; “slightly smaller”; “closer ... downstream of the wavemaker”; [12,36,35]; 해당 없음. 사례 조건과 선택 근거이다. | 목표값 0.20을 0.18로 바꾼 이유를 유지한다. 해석: $d=0.32$ m와 결합하면 $H=0.0576$ m이다. |
| CP2-118 | 도달파·수위 하강·처오름의 예측 | H 코드 대조 대상 아님 | p.12 “initial waveheight and subsequent drawdown ... well”; “identical ... Advent”; 해당 없음. 저자가 제시한 수치 검증 결과이다. | 검증 범위는 이 사례이다. 현재 WebGPU의 모든 모드·격자·쇄파 설정의 정확도로 승계하지 않는다. |
| CP2-119 | Fig. 14의 시계열 | H 코드 대조 대상 아님 | p.13 캡션의 번호 없는 식 $H/d=0.18$; “Experimental (– –) and numerical (–)”; #6·#9·#16·#22 (a–d); `shaders/ExtractTimeSeries.wgsl:60` `output = vec4<f32>(globals.time, waves, P, Q);` | 가로축은 t (s), 세로축은 η (m)이다. 시간 눈금은 8–20 s이다. |
| CP2-120 | Fig. 15 상대파고 | B 문서 오기 | p.13 “maximum horizontal run-up for H/d = 0.018”; 같은 논문 p.12의 $H/d=0.18$와 p.13 Fig. 14의 $H/d=0.18$ | Fig. 15 캡션은 H/d=0.018로 인쇄되었다. 같은 시험의 본문·Fig. 14 조건은 H/d=0.18이다. |
| CP2-121 | Fig. 15 처오름 축·기호 | H 코드 대조 대상 아님 | p.13 “Numerical (solid line) and measured (•)”; 극좌표 눈금; 해당 없음. 실험 비교 그림이다. | 각도 눈금은 30도 간격이다. 반지름 눈금은 0.2·0.4·0.6·0.8·1이다. |
| CP2-122 | 결론의 구현 요약 | A 판 차이 | p.12–13 “implemented in Unity3D using C# and HLSL”; “compiled version”; 지도·몰입형 환경; `ARCHITECTURE.md:3`의 정적 브라우저 앱 설명; 논문 공개 2019-09-28; V1 (fd57bb7, 2023-10-09) | 결론도 Base 구현을 요약한다. 현재 브라우저 구현의 직접 사용설명서로 인용하지 않는다. |
| CP2-124 | 감사·후원 | H 코드 대조 대상 아님 | p.13 “ONR ... N00014-17-1-2878”; 익명 심사자 감사; 해당 없음. 연구 후원·감사 문장이다. | 후원 과제 번호는 수치 설정이 아니다. |
| CP2-125 | 공통 셰이더 경로와 문헌 목록 | B 문서 오기 | p.6 `Assets/Celeris/Scripts/Solver/Shared`; p.5 Fig. 2 `Solvers`; p.13 [1]–[23]; 같은 논문의 경로 표기를 대조했다. 현재 WGSL 파일 경로와는 별개이다. | Base 공통 셰이더 경로는 본문의 Solver와 Fig. 2의 Solvers가 충돌한다. |
| CP2-126 | p.14의 참고문헌 [24]–[36] | H 코드 대조 대상 아님 | p.14 [24] Tavakkol & Lynett (2016); [27]–[28] VR 발표; [29] arXiv:1909.04153; [33] Briggs et al. (1995); [35] Fuhrman & Madsen (2008); [36] Tonelli & Petti (2010); 해당 없음. 이 쪽은 참고문헌만 싣는다. | [25]–[26]은 VR 배경이다. [30]–[32]는 독립 적용 연구이다. |
| CP2-127 | 일반 기본값 | C 문서 누락 | p.3은 격자·중력·제한자의 의미를 설명한다. 일반 기본값을 적지 않는다.; `js/constants_load_calc.js:23–28` WIDTH=800, HEIGHT=600, dx=1.0, dy=1.0 원문은 CP2-021·114에 인용했다. `:42` `g: 9.80665,  // Gravitational constant.`; `:44` `base_depth: 20.0,  // characteristic_depth (m), used to estimate time step, use depth in area of wave generation, or expected largest depth in domain.` | `Courant_num=0.15`, `Theta=2.0`도 현재 기본값이다(`:31,45`). `base_depth`는 시간 간격 추정용 대표 수심이다. 지역 정수심 `d_here`와 구별한다. |
| CP2-128 | 완전비선형 COULWAVE | C 문서 누락 | p.2는 COULWAVE를 다른 모형의 사례로 든다. Base 구현 모드로 정의하지 않는다.; `js/constants_load_calc.js:38` `Bous_alpha: -0.531,  // extended Boussinesq (Nwogu) parameter,`; `js/main.js:1553–1554` `const Pass3A_Coulwave_ShaderCode= await fetchShader('/shaders/Pass3A_COULWAVE.wgsl')` / `const Pass3B_Coulwave_ShaderCode= await fetchShader('/shaders/Pass3B_COULWAVE.wgsl')` | 모드 2는 보조항 패스와 별도 비선형 삼중대각 계수를 사용한다. 2020 식 (2)–(3)을 모드 2의 전체 방정식으로 쓰지 않는다. |
| CP2-129 | 구면격자와 지원 강제 제한 | C 문서 누락 | p.3은 uniform Cartesian grid를 설명한다.; `js/constants_load_calc.js:20` `grid_type: 1, // right now spherical when =2, otherwise cartesian`; `:53` `R_earth: 6371000.0,  // radius of earth, only used for spherical coordinate system`; `:455–470` 아래 C1 | 구면격자는 NLSW만 허용한다. 구면격자는 Accuracy_mode·퇴적물·쇄파를 꺼 준다. |
| CP2-130 | 고차 FVM 경로 | C 문서 누락 | p.3은 2차 KP07을 설명한다.; `js/constants_load_calc.js:39` `Accuracy_mode: 0,  // Accuracy model choice: 0: 2nd-order, 1: 4th-order.`; `js/main.js:1539–1551` 아래 C2 | `Accuracy_mode==1`은 Pass1_HighOrder와 Pass2_HighOrder_HLLC를 선택한다. 파일이 존재한다는 이유로 다른 HLLEM 경로도 자동 선택된다고 쓰지 않는다. |
| CP2-131 | 명시적 쇄파의 계수·조건·점성 상한 | C 문서 누락 | p.3은 직접 쇄파 처리가 없다고 적는다.; `js/constants_load_calc.js:57–60` `delta_breaking: 2.0,  // eddy viscosity coefficient` / `T_star_coef: 5.0,  // defines length of time until breaking becomes fully developed` / `dzdt_I_coef: 0.50,  // start breaking parameter` / `dzdt_F_coef: 0.15,  // end breaking parameter`; `shaders/Pass_Breaking.wgsl:100–125` 아래 C3 | 발생·종료 문턱은 $\sqrt{gh}$로 스케일한다. 발달 시간은 $\sqrt{h/g}$로 스케일한다. |
| CP2-132 | 마찰 법칙·마찰맵·정밀도 보정 | C 문서 누락 | p.3은 $f_1,f_2$를 바닥마찰항이라고만 정의한다.; `shaders/Pass3_Bous.wgsl:67–93` 아래 C4; `:302` `let friction_here = max(globals.friction, textureLoad(txBottomFriction, idx, 0).x);` | `isManning==1`은 $gn^2h^{-1/3}$를 사용한다. 나머지는 무차원 계수이다. |
| CP2-133 | 건조 셀 검사·경사 교정 | C 문서 누락 | p.3의 일반 양성 보존 설명에는 이 조건이 없다.; `js/constants_load_calc.js:501–502` `calc_constants.delta = Math.min(calc_constants.min_allowable_depth,calc_constants.base_depth / 5000.0);` / `calc_constants.epsilon = Math.pow(calc_constants.delta, 2);`; `shaders/Pass3_Bous.wgsl:142–151` 아래 C5 | 주위 네 셀도 건조하면 상태·도함수·분산 helper를 0으로 쓰고 반환한다. 해안선에서는 수면 경사를 한쪽 차분 또는 0으로 바꾼다(`:366–385`). |
| CP2-134 | 분산항의 적용 조건과 항등 행렬 | C 문서 누락 | p.3 식 (2)–(3)은 이 실행 조건을 인쇄하지 않는다.; `shaders/Pass3_Bous.wgsl:192–193` `if (near_dry > 0. && periodic_bc_fix < 0)` / `{ // only proceed if not near an initially dry cell`; `shaders/Update_TriDiag_coef.wgsl:42–46` 아래 C6 | 초기 건조 인접 셀과 주기 경계 보정 구간에서 분산 계산을 억제한다. 삼중대각 계수는 경계·건조 인접 구간에서 `(0,1,0)`이다. |
| CP2-135 | 주기·하천·시계열 경계 | C 문서 누락 | p.3은 네 종류 경계만 나열한다.; `shaders/BoundaryPass.wgsl:297` `let periodic_overlap = 2; // number of cells that overlap between periodic boundaries`; `docs/source/shaders/BoundaryPass_wgsl.md:18–19` ``- Boundary type `5` forcing from per-side `eta/hu/hv` time-series textures.`` / `- Constant stage/discharge river boundaries.` | 주기는 타입 3이다. 하천은 수위·유량과 횡단면을 사용한다. |
| CP2-136 | 입사파 유형과 자료 검사 | C 문서 누락 | p.3은 사인·불규칙 조파의 외부 설명을 인용한다.; `js/constants_load_calc.js:68` `incident_wave_type: -1, // 0 Sine Wave (single harmonic); 1 TMA Spectrum; 2 Transient Pulse (4 waves); 3 Solitary Wave; -1 Custom Spectum from loaded file; 5 Time Series from loaded file`; `js/File_Loader.js:378` `const expectedColumns = 1 + 3 * numPoints;` | 타입 5 파일은 계측점 수·좌표·시간과 점별 eta/hu/hv를 읽는다. 열 수·최소 자료 수·시간 단조증가·좌표 중복·변별 시간 벡터를 검사한다. |
| CP2-137 | 스펀지 모서리 합성과 퇴적물 초기화 | C 문서 누락 | p.3–4는 η·P·Q 감쇠만 설명한다.; `shaders/BoundaryPass.wgsl:363–365` `state_sum  = state_sum + s * state_w;` / `weight_sum = weight_sum + s;` / `BCState_Sed = zero;`; `:395–398` 아래 C9 | 중첩 스펀지는 거리 가중 평균을 사용한다. 스펀지에서 퇴적물 농도를 0으로 둔다. |
| CP2-138 | 단계별 경계 재적용 | C 문서 누락 | p.6은 boundaryCondition 호출을 적지만 현재의 단계별 호출을 모두 적지 않는다.; `js/main.js:2694`의 `BoundaryPass_BindGroup` 호출; `:2728–2730` 아래 C10; `:2824,2858`은 보정 단계의 대응 호출 | 분산 모드는 예측 단계에서 PCR 전·후 경계를 적용한다. `timeScheme==2`이면 보정 단계에서도 반복한다. |
| CP2-139 | 압력·침투·회전류 소산 | C 문서 누락 | p.3 식 (1)에는 이 추가항이 없다.; `shaders/Pass3_Bous.wgsl:314–315` `let press_x = -0.5 * h_here * globals.g_over_dx * (P_right - P_left);` / `let press_y = -0.5 * h_here * globals.g_over_dy * (P_up - P_down);`; `:387–390` 아래 C11 | 지표 표고가 0보다 크면 침투항을 넣는다. 압력은 별도 forcing 텍스처의 공간 차분이다. |
| CP2-140 | 시간 변동 수심과 교란 입력 | C 문서 누락 | p.6은 고립파 초기조건을 예로 든다. 동적 바닥 forcing은 설명하지 않는다.; `shaders/Pass3_Bous.wgsl:306` `let dhdt = textureLoad(txBoundaryForcing, idx, 0).y;`; `js/constants_load_calc.js:147` `disturbance_change_timescale: 0.0,  // these are for the depth change landslide option` | 교란에는 위치·진폭·방향·폭·길이·dip·rake·변동 시간·궤적 설정이 있다(`:137–155`). 이 설정을 2020 CML의 인쇄된 옵션 이름으로 쓰지 않는다. |
| CP2-141 | 네 번째 상태 채널 | C 문서 누락 | p.3 식 (1)은 $h,P,Q$의 세 성분이다.; `shaders/Pass3_Bous.wgsl:336` `let c_dissipation = -globals.whiteWaterDecayRate * C_state_here;`; `:412–424` 아래 C12 | foam/오염물질은 네 번째 채널을 사용한다. `showBreaking==1`이면 쇄파 front를 foam 강도로 쓴다. |
| CP2-142 | 퇴적물 옵션과 기본 계수 | C 문서 누락 | p.1–14는 퇴적물 수송 방정식·매개변수를 설명하지 않는다.; `js/constants_load_calc.js:106–114` 아래 C13 | 기본은 비활성이다. d50=0.2는 초기화의 `/1000.` 변환에서 mm임을 확인한다(`:624`). 공극률·침식계수·임계 Shields·상대밀도·배경 확산·쇄파 확산·hard-bottom 로딩을 구별한다. |
| CP2-143 | 부유사·소류사·침식·퇴적 | C 문서 누락 | p.1–14에 대응식 없음.; `shaders/SedTrans_Pass3.wgsl:144` `erosion = globals.sedC1_erosion * (shields - globals.sedC1_criticalshields) * local_speed;`; `:209` `bedload_erosion = 0.5 * globals.one_over_dx * (bedload_right_X - bedload_left_X) + 0.5 * globals.one_over_dy * (bedload_up_Y - bedload_down_Y);`; `:212` `var deposition = min(2.0 * C_state_here.x, h * (1.0 - globals.sedC1_n)) * globals.sedC1_fallvel;` | 소류사 발산은 바닥 갱신에만 넣는다. 부유사 source에는 넣지 않는다(`:215` 원문 C14). 침식 가능 두께와 음농도 제한을 적용한다. |
| CP2-144 | 바닥 갱신·침강속도 | C 문서 누락 | p.1–14에 대응식 없음.; `shaders/SedTrans_UpdateBottom.wgsl:84` `let dB_here = globals.dt * (e_here_average - d_here_average) / (1.0 - globals.sedC1_n); // this is positive when eroding - when increasing depth, or decreasing elevation`; `:115` `let B_new = B_here - dB;  // B is elevation, so a positive dB (eroding) should decrease the elevation` | 침식은 표고를 낮춘다. 침강속도는 입경·상대밀도·점성 및 A=25, B=1.25, n=1로 계산한다(`js/constants_load_calc.js:622–630`, C15). 2020 논문에 이 계수의 검증 근거가 있다고 쓰지 않는다. |
| CP2-145 | 평균·최댓값·통계 파고 | C 문서 누락 | p.9는 수위 실시간 곡선을 설명한다. 이 통계식을 적지 않는다.; `shaders/CalcMeans.wgsl:78` `let means_new = means_here*old_frac + state_here*update_frac;`; `shaders/CalcWaveHeight.wgsl:31–42` 아래 C16 | 현재는 평균을 뺀 수위 제곱의 누적 평균에서 σ를 계산한다. RMS 파고는 `2.829σ`, 유의파고는 `4.000σ`이다. |
| CP2-146 | 면 출력 자료 구조 | C 문서 누락 | p.9는 출력의 Advent 형식 승계만 적는다.; `js/File_Writer.js:8` `const requiredBytesPerRow = Math.ceil((width * 4 * 4) / 256) * 256; // width * RGBA * f32, padded`; `:29` `flatData[rowBaseReal + x] = bufferData[rowBasePadded + (x << 2) + chanOffset];` | GPU readback의 256 byte 행 padding을 제거한다. export는 x가 먼저 변하는 `Float32Array(width*height)`이다. |
| CP2-147 | 색상 정규화 범위 제한 | C 문서 누락 | p.8 식 (10)은 clamp를 인쇄하지 않는다.; `shaders/fragment.wgsl:594` `wavePosition = clamp(wavePosition, 0.0, 1.0);` | 현재 색상 정규화는 범위를 0–1로 제한한다. `maxWave==minWave`의 분모 검사는 이 줄에 없다. |
| CP2-148 | 시계열 export와 비동기 초기화 검사 | C 문서 누락 | p.9는 부이의 화면 수위 곡선을 설명한다.; `js/Time_Series.js:108–112` 아래 C17; `:166`의 `Time/Eta/P/Q` header는 CP2-091에 인용했다. | 시계열은 eta·P·Q를 별도 배열로 보관한다. 초기화 전 요청의 readback은 epoch가 다르면 버린다. |
| CP2-149 | 이미지·면 출력 선택과 주기 | C 문서 누락 | p.1–2의 360도 영상 외에 이 옵션은 없다.; `js/constants_load_calc.js:358–370` 아래 C18 | GIF·JPEG 묶음·개별 면의 저장 플래그와 주기를 분리한다. 기본 면 출력은 eta만 켜져 있다. |
| CP2-150 | 중첩격자 경계 출력 | C 문서 누락 | p.1–14에 대응 설명 없음.; `js/constants_load_calc.js:380–386` `nestedGridOutput_dt: 1.0, // requested nested boundary output interval`와 `nestedGridOutput_max_samples: 8192, // hard cap on stored output times`; `js/File_Writer.js:836` ``await blobCreationAndDownload(blob, `${prefix}_time_series_bc_${side.name}.txt`);`` | 사각형 경계의 eta/hu/hv 시계열을 저장한다. 시작·종료·최대 표본·복수 사각형·선행 무변화 구간 절단 옵션을 둔다(`:374–392`). 이는 2020의 다섯 부이 출력과 다르다. |
| CP2-151 | 설정 병합과 파생값 | C 문서 누락 | p.9는 CML 입력을 설명한다. JSON 병합·검사 규칙은 없다.; `js/constants_load_calc.js:425` `calc_constants = { ...calc_constants, ...loadedConfig };`; `:438` `var configJson = JSON.parse(configContent);`; `:489–502`는 Theta·Bcoef·역격자간격·delta·epsilon 파생식이다. | 업로드/예제 값이 기본값을 덮는다. 이후 파생값을 계산한다. |
| CP2-152 | 수심 자료 검사와 가장자리 평탄화 | C 문서 누락 | p.9는 CBF 자료·보간을 설명한다.; `js/File_Loader.js:50–53`의 NaN 검사 U2; `:60–62` `for (let x = 0; x < 3; x++) {` / `bathy2D[x][y] = bathy2D[4][y];` / `}`; `:65–67`는 오른쪽 네 열을 WIDTH−5 열로 채운다. | 현재 loader는 숫자 파싱 실패를 거부한다. 왼쪽·아래쪽 세 줄과 오른쪽·위쪽 네 줄을 내부 값으로 평탄화한다. |
| CP2-153 | 1D 단면 판 | C 문서 누락 | p.3 식 (1)은 2DH이다.; `transect_version/shaders/Pass3_Bous.wgsl:108–115`의 원문 C19; `transect_version/js/Run_Tridiag_Solver.js:59–75`의 y solve는 주석이다. | 단면 판의 y 미분·혼합항과 y PCR을 2D 본판에서 추론하지 않는다. x 수면 경사는 4차이다(`:242–244`). 단면 판의 정확한 원문은 C19이다. |
| CP2-154 | HTML별 진입점 | C 문서 누락 | p.4·10은 Main.unity·실행 파일을 설명한다.; `index.html:1597`, `index_headless.html:112`, `index_nots.html:1486`, `river.html:1468`, `MC_examples.html:1468` 모두 `<script type="module" src="js/main.js"></script>`; `transect_version/index.html:1471` `<script type="module" src="/transect_version/js/main.js"></script>` | 다섯 본판 HTML은 같은 main.js로 들어간다. 단면 HTML은 별도 main.js로 들어간다. |
| CP2-155 | 동·북 스펀지의 거리식 | E 코드 결함 후보 | 논문의 $D(\alpha)$는 흡수 경계까지의 법선거리이다. 현재 거리 가중 설명은 `models/Celeris/source-analysis/celeris-breaking-boundary.md:115`이다.; `shaders/BoundaryPass.wgsl:111,123` N13의 `BoundaryWidth - boundary_nx - idx.x`, `BoundaryWidth - boundary_ny - idx.y`; 이력 V2의 괄호 삭제; 5.3의 반대 근거·활성 호출 경로 포함. | 현재 동·북 스펀지의 거리식은 전체 영역 크기에 의존하는 코드 결함 후보이다. 근거 강도는 중간이다. |
| CP2-156 | 색상 배열 상한 index | E 코드 결함 후보 | p.8 식 (10)의 현재 배열 구현에서 확인한 항목이다.; `shaders/fragment.wgsl:598–605` 아래 C20; `models/Celeris/source-analysis/celeris-render.md:57` “16색 LUT 선형보간”; 5.3의 반대 근거·활성 호출 경로 포함. | 현재 색상 최댓값에서 upperIndex가 배열 범위를 넘는 코드 결함 후보가 있다. 근거 강도는 중간이다. |
| CP2-157 | 지도·사용자 overlay 설정 | C 문서 누락 | p.8은 자동 지도 다운로드를 설명한다. 현재의 사용자 이미지 입력과 변환 설정은 적지 않는다.; `index_headless.html:56` `<input type="file" id="satimageFile" accept="image/jpeg, image/png, image/bmp, image/gif" />`; `js/constants_load_calc.js:239–242`의 GMscaleX/Y=1.0, GMoffsetX/Y=0.0 | 지도 API 호출과 사용자 이미지 업로드를 구별한다. 이미지 변환의 기본 배율은 1이고 기본 이동은 0이다. |
| CP2-158 | 프레임당 반복 수·일시정지 | C 문서 누락 | p.4은 “pre-defined number of steps”를 적는다. 자동 조정 옵션은 적지 않는다.; `js/constants_load_calc.js:248–250` `render_step: 1, // number of compute steps to run for every render step, the biggest the number the choppier the viz, but also the faster it runs` / `setRenderStep: 0, // flag to automatically find best render_step when = 0` / `simPause: -1, // check variable, simulation is paused when this value is =1, running when = -1` | 프레임당 계산 횟수 조정은 물리 `dt`의 적응 조정과 다르다. 일시정지와 출력 대기 시간도 구별한다. |
| CP2-159 | 계산·렌더 정밀도 분리 | C 문서 누락 | p.5는 RenderTexture라고만 적는다.; `js/Create_Textures.js:5` `format: 'rgba32float',`; `:18` `format: 'rgba16float',`; `shaders/vertex3D.wgsl:78`은 전체 etaTexture를 직접 읽는다. | 계산 상태의 float32와 렌더 cache의 float16을 구별한다. 3D 높이가 언제나 float16 cache에서 온다고 쓰지 않는다. |
| CP2-160 | MATLAB 출력 판독·정리 스크립트 | C 문서 누락 | p.9는 출력의 상세 판독 절차를 적지 않는다.; `scripts/load_WebGPUCeleris_output.m:18` `bathytopo = fread(fid, [nx, ny], 'float32');`; `:30` `eta = fread(fid, [nx, ny], 'float32');`; `:73` `pcolor(x, y, eta');  % note the transpose '  - the surface data is [nx,ny]`; `scripts/clean_WebGPUCeleris_output.m:4–5` `! del *.bin` / `! del *.txt` | MATLAB은 `[nx,ny]`로 읽은 뒤 도식에서 전치한다. `nt=496`은 스크립트의 수동 수정값이다(`:14`). 정리 스크립트는 Windows 삭제 명령이다. |
| CP2-161 | 상류 문서의 단면 범위 제한 | C 문서 누락 | p.1–14에는 현재 상류 문서의 판독 범위 규칙이 없다.; `docs/README.md:5` `The transect implementation is intentionally excluded. Do not infer transect behavior from these notes and do not use these notes as coverage for transect files.` | 본판 docs/source 설명은 단면 판의 근거를 대신하지 않는다. 단면의 실제 파일을 별도로 열었다. |
| CP2-162 | 설계 요소·마찰 변경 | C 문서 누락 | p.1–14는 현재의 설계 요소별 매개변수를 적지 않는다.; `js/constants_load_calc.js:345–355`의 Friction·Coral·Oyster·Mangrove·Kelp·Grass·Scrub·RubbleMound·Dune·Berm·Seawall 기본값; `shaders/fragment.wgsl:638–645`의 component_index 분기 | 산호 0.1, 굴 0.035, 맹그로브 0.15, 해조 0.025, 잔디 0.03, 관목 0.075, 사석 0.04, 사구 0.03, berm 0.02, 방벽 0.02는 현재 설정이다. 셰이더는 요소별 가시심도·색 혼합을 적용한다. |
| CP2-163 | 원판의 언어 | B 문서 오기 | `models/Celeris/README.md:14` “**원판**: C#/HLSL, **Direct3D** GPU (Windows)”; Tavakkol 2020 p.2 “Celeris Advent is developed in C++ and HLSL using the Direct3D framework.”; p.1 Base는 Unity3D·C#·HLSL이다. | Advent는 C++·HLSL·Direct3D 구현이다. Base는 Unity3D·C#·HLSL 구현이다. WebGPU는 JavaScript·WGSL 구현이다. |
| CP2-164 | 적응형 시간 적분 단정 | B 문서 오기 | `models/Celeris/README.md:18` “시간적분 3rd-order Adams-Bashforth(adaptive, Tavakkol-Lynett 2019)”; Tavakkol 2020 p.3 “third-order fixed timestep”; `js/constants_load_calc.js:486`의 dt 산식; N9의 AB3·AM4 계수 | 2020 Base 논문은 고정 시간 간격의 AB3를 설명한다. 현재 WebGPU 기본은 AB3 예측과 AM4 보정이다. 현재 코드는 대표 수심과 Courant 수로 dt를 계산한다. |
| CP2-165 | 2019 문헌의 저자 | B 문서 오기 | `models/Celeris/README.md:27` “Tavakkol, Lynett (2019)”; `models/Celeris/manual-notes/celeris-architecture-and-config.md:173` “**Tavakkol, S. & Lynett, P. (2019).**”; Tavakkol 2020 p.14 [29] “S. Tavakkol, S. Son, P. Lynett, ArXiv Prepr. ArXiv:1909.04153 (2019).” | Tavakkol, S., Son, S. & Lynett, P. (2019), arXiv:1909.04153. |
| CP2-166 | 예측·보정 명칭 | B 문서 오기 | `models/Celeris/source-analysis/celeris-source-map.md:42` “시간적분 (3rd-order Adams-Bashforth predictor-corrector)”; `shaders/Pass3_Bous.wgsl:404` `newState = in_state_here_UV + globals.dt / 12.0 * (23.0 * d_by_dt - 16.0 * oldies + 5.0 * oldOldies);`; `:409` `newState = in_state_here_UV + globals.dt / 24.0 * (9.0 * d_by_dt + 19.0 * predicted - 5.0 * oldies + oldOldies);` | 시간 적분은 Euler, AB3 예측, AB3 예측과 AM4 보정 중에서 선택한다. |
| CP2-170 | 스펀지층 판 차이의 누락 | C 문서 누락 | `models/Celeris/source-analysis/celeris-breaking-boundary.md:109` “cosine 윈도우를 0.005승한 감쇠계수 γ”; `:115` “거리 가중 평균”; Tavakkol 2020 p.4 식 (9); `shaders/BoundaryPass.wgsl:105` N13 | 현재 감쇠식은 2020 식 (9)의 γ 비율식과 다르다. 동·북 거리식에는 CP2-155의 코드 결함 후보가 있다. |
| CP2-172 | 퇴적물 확산의 비활성 단정 | B 문서 오기 | `models/Celeris/source-analysis/celeris-sediment.md:104` “현재 활성 빌드는 **이류 + 픽업/침강만**, 명시적 확산 없음”; “셰이더에서 미사용”; `shaders/Pass2.wgsl:141` `let k_here =  globals.sedTurbDispersion + globals.sedBreakingDispersionCoef * textureLoad(txBreaking, idx, 0).y;`; `:190`은 `- k_east * hW_east * C1x_east`와 `- k_west * h_here.y * C1x_west`를 포함한다. | Pass3의 별도 확산 source는 주석이다. 기본 Pass2는 Class 1 부유사 면 플럭스에 배경·쇄파 확산을 넣는다. |
| CP2-173 | AB4라는 옵션 설명 | B 문서 오기 | `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:191` “2=AB4 pred+corr”; N9의 예측 계수는 3차 AB이다. 보정 계수는 4차 AM이다. | timeScheme=2는 AB3 예측과 AM4 보정이다. |
| CP2-174 | 매뉴얼 노트의 적응형 출처 서술 | B 문서 오기 | `models/Celeris/manual-notes/celeris-architecture-and-config.md:185` “§1.5의 적응형 3차 Adams-Bashforth predictor/corrector 시간적분의 학술적 출처”; 같은 노트 `:107–108`은 예측·보정을 나눈다. Tavakkol 2020 p.3은 fixed timestep이다. 현재 N9·`js/constants_load_calc.js:486`에는 가변 간격 계수가 없다. | 2019 문헌은 적응형 시간 적분 연구의 별도 참고문헌이다. 현재 구현의 예측·보정 계수와 dt 계산은 코드에서 직접 인용한다. |
| CP2-175 | 2020 논문의 워크플로 계승 | C 문서 누락 | `models/Celeris/manual-notes/celeris-architecture-and-config.md:184` “WebGPU 버전이 정적 브라우저앱으로 그 정신 계승”; `docs/architecture/REFERENCE_PAPERS.md:33` “keeps the same spirit”; 2절의 A·D 행 | Base의 Unity 클래스, CML·CBF 보간, 식 (9), 최대 다섯 부이, Rift·360도 영상 기능을 현재 WebGPU 기능으로 승계하지 않는다. |
| CP2-177 | 2017 계보 표의 언어 | B 문서 오기 | `models/Celeris/web-refs/celeris-lynett-2026.md:59` “C#/HLSL Direct3D (Windows)”; Tavakkol 2020 p.2 “Celeris Advent is developed in C++ and HLSL” | 2017 Advent의 플랫폼은 C++·HLSL·Direct3D이다. |
| CP2-179 | 렌더 노트의 배열 보간 | C 문서 누락 | `models/Celeris/source-analysis/celeris-render.md:57` “16색 LUT 선형보간”; `:79` “`textureLoad`로 읽어 elevation 취득”; `shaders/fragment.wgsl:598–605` C20; `shaders/vertex3D.wgsl:78` | 색상 최댓값에서 upperIndex가 16이 되는 CP2-156의 후보를 기록한다. 128×128 타일은 2020 Base의 구조이다. |


확인 범위: Tavakkol 2020의 모든 쪽 이미지와 본문을 확인했다. 대조에 필요한 본판·단면 코드, HTML 진입점, 출력 스크립트, 관련 상류 문서, 현재 노트, 읽기 전용 git 이력을 확인했다. 2017 PDF의 출력 형식 설명은 보조 근거로 확인했다. 2026 논문 전체를 다시 판독한 작업으로 보고하지 않는다. 모델·브라우저·MATLAB 스크립트는 실행하지 않았다. 수치 오차·반사율·성능·VR 동작을 검증하지 않았다. 범위 밖 자산·외부 라이브러리·자동화·벤치마크·사례 파일은 판독 대상으로 삼지 않았다.

분류별 개수: 일치 29, A 43, B 12, C 37, D 4, E 2, F 8, H 44, X 0. 합계 179행. 열지 못한 파일: 없음.
