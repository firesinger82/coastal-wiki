# Tavakkol 2017과 Celeris-WebGPU 코드 대조

## 1 요약

분류별 개수: 일치 41, A 판 차이 38, B 문서 오기 24, C 문서 누락 30, D 문서에만 있음 0, E 코드 결함 후보 3, F 표기 차이 6, H 코드 대조 대상 아님 27, X 외부 원문 필요 0. 총 169행이다. 이 값은 제2–4절의 고유 행 ID와 제5절의 차이 결론 표를 세어 얻었다.

현재 삼중대각 계수와 AB3·AM4 가중치는 논문과 맞는다. 교차 분산항의 시간 이산화·시작 단계·보정 횟수·면 속도 정칙화·흡수층·명시적 쇄파는 판이 다르다. 논문 식 (3)·(13)·(37)과 일부 그림·무차원화 표기에는 내부 모순이 있다. 코드 결함 후보 3행은 서로 다른 2건이다. 본판의 Psi1y 혼합 미분 분모가 첫 건이다. transect의 Psi2x 미사용이 두 번째 건이다.

이 보고서는 AI가 작성한 원문 대조 기록이다. 논문 인용과 코드 인용은 원문이다. `해석:`으로 시작하는 문장은 대조자의 해석이다. 이 보고서는 모델 실행 결과를 포함하지 않는다.

대상 논문은 Tavakkol & Lynett, *Computer Physics Communications* 217 (2017), 117–127, DOI `10.1016/j.cpc.2017.03.002`이다. 논문 p.1은 온라인 공개일을 `13 April 2017`로 적는다. 논문 p.2는 구현을 `Celeris Advent`라고 부른다. 논문 p.1은 `Programming language: C++, HLSL`로 적는다.

코드 기준은 `models/Celeris/raw/source_code/Celeris-WebGPU/`의 `ebca435d02b258768e0352fbaf27404f2f135799`이다. 이 커밋의 날짜는 `2026-07-20T16:10:36-07:00`이다. 이하 코드 경로는 이 디렉터리에 상대적이다. 현재 코드 인용의 생략된 판 접두어는 `ebca435:`이다. 과거 판은 `HASH:파일:줄`로 쓴다. 노트 경로는 위키 루트에 상대적이다.

논문 쪽 번호는 PDF 순서이다. p.2–11의 인쇄 쪽 번호는 118–127이다. 지정된 300 dpi 이미지 `cel-tavakkol2017-001.png`부터 `-011.png`까지 직접 확인했다. 판독 기록은 항목을 찾는 색인으로 사용했다. 코드 판정은 `nl -ba`로 연 원문을 사용한다. 텍스트 추출본에서 수식 배열이 흐트러진 곳은 이미지의 인쇄를 우선한다.

논문의 번호 식은 (1)–(37)이다. 논문의 그림은 Fig. 1–15이다. 논문에는 번호 붙은 표가 없다. 빈 쪽도 없다. p.5는 Fig. 1·2와 본문을 함께 싣는다. p.6은 Fig. 3·4와 본문을 함께 싣는다. p.9–11도 그림과 본문을 함께 싣는다.

`일치`는 해당 행에서 인용한 수학적 항 또는 동작의 일치를 뜻한다. 주변의 추가 처리까지 같다는 뜻으로 사용하지 않는다. `불일치`, `문서에만`, `코드에만` 행은 제5절에서 A·B·C·D·E·F·H·X 중 하나로 결론낸다. 한 행의 독립 쟁점은 나누어 기록한다.

범위 밖 디렉터리와 표시 전용 skybox·duck·model 셰이더는 판독하지 않는다. 실행·브라우저 실행·코드 수정은 수행하지 않는다. 쓰기 대상은 이 파일 하나이다. 기존 노트의 수정안은 제4절에만 제시한다.

## 2 대조 표

### 2.1 판·목적·변수와 지배식

| 행 ID | 문서(위치·원문) | 코드(파일:줄·원문) | 판정 | 이유 |
|---|---|---|---|---|
| CP1-001 | p.1 Program summary `Programming language: C++, HLSL`; p.2 `Direct3D` | `js/Config_Pipelines.js`의 WebGPU 파이프라인과 `shaders/Pass3_Bous.wgsl:95` `@compute @workgroup_size(16, 16)` | 불일치 | A. 2017년 Advent와 2023년 이후 WebGPU 구현을 구분한다. 제5절의 V1은 최초 WebGPU 코드와 날짜를 제시한다. |
| CP1-002 | p.1 `Licensing provisions: GNU General Public License 3 (GPL)`; p.11도 GPL 배포를 설명한다. | `README.md:82` `This project is licensed under the **MIT License**. See the \`LICENSE\` file for details.` | 불일치 | A. 이전 프로그램의 배포 조건과 현재 저장소의 배포 설명이 다르다. 이 행은 법적 판단을 하지 않는다. |
| CP1-003 | p.1 `faster than real-time`; p.1–2 수십–수백 CPU 코어와 평균 노트북 비교 | `js/main.js:2615` `for (let frame_c = 0; frame_c < calc_constants.render_step; frame_c++) {  // loop through the compute shaders "render_step" time` | 문서에만 | H. 성능 주장은 하드웨어와 사례에 의존한다. 호출 루프만으로 실시간 성능을 입증하지 않는다. |
| CP1-004 | p.1 `hybrid finite volume–finite difference method`; p.2 `supports moving shoreline boundaries` | `shaders/Pass2.wgsl:38` `return (aplus * Fminus - aminus * Fplus + aplus * aminus * Udifference) / (aplus - aminus);`; `shaders/Pass3_Bous.wgsl:265` `let eta_by_dx_dx = globals.one_over_d2x * (eta_right - 2.0 * eta_here + eta_left);` | 일치 | 면 수치 플럭스와 중심 차분 분산항을 결합한다. 습건의 세부 변경은 CP1-014·CP1-112–116에서 분리한다. |
| CP1-005 | p.2 무번호 정의 $h$는 총수심, $z$는 기준면 바닥 표고, $w=h+z$, $\eta=w-w_s$, $w_t=h_t$는 바닥이 시간에 일정할 때이다. | `shaders/Pass3_Bous.wgsl:117` `let B_here = textureLoad(txBottom, idx, 0).z;`; `:123` `let h_here = in_state_here.x - B_here;` | 일치 | 코드 상태 x가 수면 표고이고 바닥 z를 빼 총수심을 얻는다. `B_here`는 논문의 분산계수 $B$가 아니다. 바닥 변동은 CP1-121에서 다룬다. |
| CP1-006 | p.2 무번호 정의 $P,Q$는 x·y 방향 수심 적분 질량 플럭스이다. 미지수는 $[w,P,Q]^T$이다. | `shaders/Pass1.wgsl:125–126` `let huwy = Reconstruct(in_west.y, in_here.y, in_east.y, TWO_THETAc);`<br>`let hvwy = Reconstruct(in_west.z, in_here.z, in_east.z, TWO_THETAc);` | 일치 | 상태 y·z가 $P=hu,Q=hv$에 대응한다. `Pass3_Bous`의 지역 변수 `u_*`, `v_*`는 이 상태 채널을 읽으므로 실제 속도와 구분한다. |
| CP1-007 | Tavakkol 2017 p.2 식 (1) $\mathbf U_t+\mathbf F(\mathbf U)_x+\mathbf G(\mathbf U)_y+\mathbf S(\mathbf U)=0$ | `shaders/Pass3_Bous.wgsl:394` `let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term + vorticity_dissipation;` | 일치 | 동·북 면 플럭스를 빼고 서·남 면 플럭스를 더한다. 소스항의 부호는 CP1-009·022에서 대조한다. 추가 소스는 제3절에 분리한다. |
| CP1-008 | p.2 무번호 벡터 $\mathbf U=[h,P,Q]^T$, $\mathbf F=[P,P^2/h+gh^2/2,PQ/h]^T$, $\mathbf G=[Q,PQ/h,Q^2/h+gh^2/2]^T$ | `shaders/Pass2.wgsl:123–125` `NumericalFlux(aplus, aminus, hW_east * uW_east, h_here.y * u_here.y, mass_diff_x),`<br>`NumericalFlux(aplus, aminus, hW_east * uW_east * uW_east, h_here.y * u_here.y * u_here.y, P_diff_x),`<br>`NumericalFlux(aplus, aminus, hW_east * uW_east * vW_east, h_here.y * u_here.y * v_here.y, Q_diff_x),` | 불일치 | F. 현재 코드의 면 플럭스는 정수압 $gh^2/2$를 포함하지 않는다. 운동량 소스 `:392`의 $-gh\nabla w$가 정수압과 바닥 경사를 함께 담당한다. 변형은 제5절에 쓴다. |
| CP1-009 | p.2 무번호 $\mathbf S=[0,ghz_x+\psi_1+f_1,ghz_y+\psi_2+f_2]^T$ | `shaders/Pass3_Bous.wgsl:392` `let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x, -globals.g * h_here * detady - in_state_here.z * friction_ + breaking_y + (Psi1y + Psi2y) + press_y, hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);` | 불일치 | F. 식 (1)의 좌변 소스는 우변에서 부호가 바뀐다. 논문 $\psi$의 음의 공간항이 코드 우변에서는 양의 `Psi`로 나타난다. 추가 물리는 제3절에 분리한다. |
| CP1-010 | Tavakkol 2017 p.2 식 (2) $\psi_1=-(B+\frac13)d^2(P_{xxt}+Q_{xyt})-Bgd^3(\eta_{xxx}+\eta_{xyy})-dd_x(\frac13P_{xt}+\frac16Q_{yt}+2Bgd\eta_{xx}+Bgd\eta_{yy})-dd_y(\frac16Q_{xt}+Bgd\eta_{xy})$ | `shaders/Pass3_Bous.wgsl:269–273`의 `F_star` 전체 식은 아래 Q1에 인용한다. `shaders/Update_TriDiag_coef.wgsl:67–69`의 계수는 Q4에 인용한다. | 일치 | 동방향 시간 미분은 $U^*$에 들어간다. 교차 시간 미분은 $F^*$에 들어간다. 공간 분산항은 `Psi1x`,`Psi2x`에 들어간다. 시간 이산화 차이는 CP1-031에서 별도로 판정한다. |
| CP1-011 | Tavakkol 2017 p.2 식 (3) $\psi_2=-(B+\frac13)d^2(P_{xyt}+Q_{yyt})-Bgd^3(\eta_{yyy}+\eta_{xxy})-dd_x(\frac13Q_{yt}+\frac16P_{xt}+2Bgd\eta_{yy}+Bgd\eta_{xx})-dd_x(\frac16P_{yt}+Bgd\eta_{xy})$ | `shaders/Pass3_Bous.wgsl:286` `Psi2y = globals.Bcoef_g * d2_here * (dd_by_dy * (2.0 * eta_by_dy_dy + eta_by_dx_dx) + dd_by_dx * eta_by_dx_dy) + (G_star - F_G_star_oldOldies.z) / globals.dt * 0.5;` | 불일치 | B. 인쇄 원문은 두 괄호 앞을 모두 $dd_x$로 쓴다. 같은 논문 식 (8)·(11)은 첫 괄호에 대응하는 y 방향 계수를 사용한다. 코드의 그 계수도 `dd_by_dy`이다. |
| CP1-012 | p.2 무번호 $B=1/15$ | `js/constants_load_calc.js:37` `Bcoef: 1.0 / 15.0,  // Dispersion parameter, 1/15 is optimum value for this set of equations.` | 일치 | 분산계수 기본값이 같다. 파일에서 설정값을 덮어쓸 수 있다는 사실은 CP1-119에서 분리한다. |
| CP1-013 | p.2 `sufficiently accurate linear dispersion and shoaling characteristics for values of kd < 3` | `js/constants_load_calc.js:37`의 `Bcoef: 1.0 / 15.0` | 문서에만 | H. $kd<3$은 방정식의 이론적 적용성 주장이다. 코드가 $kd$를 계산해 이 범위를 강제한다는 뜻이 아니다. |
| CP1-014 | p.2 `we set d = 0 so the solver automatically switches to NLSW` | `shaders/Pass3_Bous.wgsl:181` `let d_here = -B_here;`; `:192–193` `if (near_dry > 0. && periodic_bc_fix < 0)`<br>`{ // only proceed if not near an initially dry cell` | 불일치 | A. 현재 코드는 양의 육상 표고에서 `d_here`를 0으로 직접 자르지 않는다. `Update_neardry`가 육상을 포함하는 ±3셀에서 분산항을 끈다. 삼중대각 계수도 항등행으로 바꾼다. |

#### Q1. 교차 시간 미분의 공간식 원문

`shaders/Pass3_Bous.wgsl:269–279`:

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
```

### 2.2 재배열·공간 이산화·재구성

| 행 ID | 문서(위치·원문) | 코드(파일:줄·원문) | 판정 | 이유 |
|---|---|---|---|---|
| CP1-015 | Tavakkol 2017 p.2 식 (4) $w_t=E(P,Q)$ | `shaders/Pass3_Bous.wgsl:394` `let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term + vorticity_dissipation;` | 일치 | x 성분은 질량 플럭스 발산이다. 코드의 추가 질량 소스는 CP1-120·121에서 분리한다. |
| CP1-016 | Tavakkol 2017 p.2 식 (5) $U_t^*=F(h,P,Q)+[F^*(Q)]_t$ | `shaders/Pass3_Bous.wgsl:283` `Psi2x = globals.Bcoef_g * d2_here * (dd_by_dx * (2.0 * eta_by_dx_dx + eta_by_dy_dy) + dd_by_dy * eta_by_dx_dy) + (F_star - F_G_star_oldOldies.y) / globals.dt * 0.5;` | 일치 | 코드가 x 방향 변환 운동량의 우변에 $F^*$ 시간 미분을 더한다. 그 시간 이산화는 식 (16)과 같지 않으며 CP1-031의 대상이다. |
| CP1-017 | Tavakkol 2017 p.2 식 (6) $V_t^*=G(h,P,Q)+[G^*(P)]_t$ | `shaders/Pass3_Bous.wgsl:286` `Psi2y = globals.Bcoef_g * d2_here * (dd_by_dy * (2.0 * eta_by_dy_dy + eta_by_dx_dx) + dd_by_dx * eta_by_dx_dy) + (G_star - F_G_star_oldOldies.z) / globals.dt * 0.5;` | 일치 | 코드가 y 방향 변환 운동량의 우변에 $G^*$ 시간 미분을 더한다. 공간 혼합 미분의 계수 오류 후보는 CP1-023에서 분리한다. |
| CP1-018 | Tavakkol 2017 p.3 식 (7) $U^*=P-\frac13dd_xP_x-(B+\frac13)d^2P_{xx}$ | `shaders/Update_TriDiag_coef.wgsl:67–69`의 전체 식은 Q4에 인용한다. | 일치 | $P_x$ 중심 차분의 서쪽 계수가 양수이다. $P_{xx}$ 중심 차분의 두 비대각 계수가 음수이다. 대각에는 $1+2(B+1/3)d^2/\Delta x^2$가 남는다. |
| CP1-019 | Tavakkol 2017 p.3 식 (8) $V^*=Q-\frac13dd_yQ_y-(B+\frac13)d^2Q_{yy}$ | `shaders/Update_TriDiag_coef.wgsl:101–103`의 전체 식은 Q4에 인용한다. | 일치 | 같은 계수 유도를 y 방향에 적용한다. `near_dry`와 경계의 항등행 조건은 CP1-115에서 분리한다. |
| CP1-020 | Tavakkol 2017 p.3 식 (9) $E(P,Q)=-(P_x+Q_y)$ | `shaders/Pass2.wgsl:123` `NumericalFlux(aplus, aminus, hW_east * uW_east, h_here.y * u_here.y, mass_diff_x),`; `shaders/Pass3_Bous.wgsl:394`의 전체 식은 CP1-015에 인용했다. | 일치 | 면의 $hu,hv$ 플럭스 차가 연속식의 이산 발산을 만든다. |
| CP1-021 | Tavakkol 2017 p.3 식 (10) $F(h,P,Q)=-(\frac{P^2}{h}+\frac{gh^2}{2})_x-(\frac{PQ}{h})_y-ghz_x-f_1+Bgd^3(\eta_{xxx}+\eta_{xyy})+Bgd^2(d_x(2\eta_{xx}+\eta_{yy})+d_y\eta_{xy})$ | `shaders/Pass3_Bous.wgsl:282` `Psi1x = globals.Bcoef_g * d3_here * ((eta_right_right - 2.0 * eta_right + 2.0 * eta_left - eta_left_left) * (0.5 * globals.one_over_d3x) + (eta_up_right - eta_up_left - 2.0 * eta_right + 2.0 * eta_left + eta_down_right - eta_down_left) * (0.5 * globals.one_over_dx * globals.one_over_d2y));` | 일치 | $Bgd^3$의 세 번째 x 미분과 x·yy 혼합 미분의 부호가 같다. $Bgd^2$ 항은 CP1-016의 `Psi2x` 앞부분과 같다. 정수압 분리는 CP1-008에서 판정했다. |
| CP1-022 | Tavakkol 2017 p.3 식 (11) $G(h,P,Q)=-(\frac{Q^2}{h}+\frac{gh^2}{2})_y-(\frac{PQ}{h})_x-ghz_y-f_2+Bgd^3(\eta_{yyy}+\eta_{xxy})+Bgd^2(d_y(2\eta_{yy}+\eta_{xx})+d_x\eta_{xy})$ | `shaders/Pass3_Bous.wgsl:286`의 전체 식은 CP1-017에 인용했다. `:285`는 CP1-023에 인용한다. | 불일치 | E. $d_y(2\eta_{yy}+\eta_{xx})+d_x\eta_{xy}$와 순수 y 세 번째 미분은 맞는다. $\eta_{xxy}$의 분모가 다르다. CP1-023은 같은 원인의 독립 코드 증거이므로 결론 집계에서 각각 행으로 센다. |
| CP1-023 | p.3 식 (11)의 $Bgd^3\eta_{xxy}$ | `shaders/Pass3_Bous.wgsl:285` `Psi1y = globals.Bcoef_g * d3_here * ((eta_up_up - 2.0 * eta_up + 2.0 * eta_down - eta_down_down) * (0.5 * globals.one_over_d3y) + (eta_up_right + eta_up_left - 2.0 * eta_up + 2.0 * eta_down - eta_down_right - eta_down_left) * (0.5 * globals.one_over_dx * globals.one_over_d2x));` | 불일치 | E, 강함. 두 번째 분자의 차분 방향은 x 두 번·y 한 번이다. 코드 분모는 $2\Delta x^3$이다. 필요한 분모는 $2\Delta x^2\Delta y$이다. x 방향 `:282`와 축 교환해도 다르다. `dx=dy`에서는 차이가 가려진다. 반대 근거 검색과 호출 근거는 제5절에 적는다. |
| CP1-024 | Tavakkol 2017 p.3 식 (12) $F^*(Q)=\frac16dd_xQ_y+\frac16dd_yQ_x+(B+\frac13)d^2Q_{xy}$ | `shaders/Pass3_Bous.wgsl:269–273`의 Q1 원문 | 일치 | 상태 z의 $Q$에 y·x 중심 차분을 각각 적용한다. 계수 $1/6,1/6,B+1/3$가 같다. |
| CP1-025 | Tavakkol 2017 p.3 식 (13) $G^*(Q)=\frac16dd_xP_y+\frac16dd_yP_x+(B+\frac13)d^2P_{xy}$ | `shaders/Pass3_Bous.wgsl:275–279`의 Q1 원문 | 불일치 | B. 논문 좌변 인수는 $Q$이지만 우변은 모두 $P$이다. 같은 논문 식 (6)은 $G^*(P)$라고 적는다. 코드도 상태 y의 $P$를 읽는다. |
| CP1-026 | p.3 `uniform Cartesian grids`; `rectangular cells with fixed dimensions of ∆x and ∆y`; 셀 중심 평균을 FDM 격자점으로 사용한다. | `js/constants_load_calc.js:27–28` `dx: 1.0,  // Cell size in the x direction.`<br>`dy: 1.0,  // Cell size in the y direction.`; `shaders/Pass3_Bous.wgsl:108–115`의 정수 이웃 인덱스 | 일치 | 본판의 Cartesian 경로가 균일 직사각형 격자를 사용한다. 구면 경로는 CP1-125에서 분리한다. |
| CP1-027 | p.3 KP07 단계 1 `linearly reconstructed ... generalized minmod limiter` | `shaders/Pass1.wgsl:41–51`의 Q2 원문 | 일치 | 세 차분의 부호가 다르면 기울기를 0으로 만든다. 같은 부호이면 가장 작은 절댓값을 택한다. $\theta$의 기본값은 논문에 없으므로 CP1-109에서 분리한다. |
| CP1-028 | p.3 단계 2 `A simple conservative correction is applied on w to preserve the positivity of h.` | `shaders/Pass1.wgsl:134–136` `w = vec4<f32>(wzx.y, wwy.y, wzx.x, wwy.x);`<br>`h = w - B;`<br>`h = max(h, vec4<f32>(0.0, 0.0, 0.0, 0.0));` | 불일치 | A. 현재 코드는 재구성한 면 수심을 직접 0 이상으로 자른다. 이 세 줄은 셀 평균 보존 보정과 동일한 연산을 적지 않는다. 양수 수심 보장에 관한 논문의 일반 주장을 이 코드의 보존성 증명으로 쓰지 않는다. |
| CP1-029 | Tavakkol 2017 p.3 식 (14) $u=\frac{\sqrt2h(P)}{\sqrt{h^4+\max(h^4,\epsilon)}},\quad v=\frac{\sqrt2h(Q)}{\sqrt{h^4+\max(h^4,\epsilon)}}$ | `shaders/Pass1.wgsl:145–149`의 Q2 원문 | 불일치 | A. 현재 역수는 $2h/(h^2+\max(h^2,\epsilon_c))$이다. 논문 역수는 $\sqrt2h/\sqrt{h^4+\max(h^4,\epsilon)}$이다. 큰 수심에서는 둘 다 $1/h$이다. 작은 수심에서 함수와 임계량의 차원이 다르다. |
| CP1-030 | p.3 단계 3 `central-upwind scheme`; 단계 4 `dispersive terms as source terms discretized by central FDM` | `shaders/Pass2.wgsl:36–41`의 Q2 원문; `shaders/Pass3_Bous.wgsl:264–266`의 Q3 원문 | 일치 | 표준 면 플럭스는 양·음 전파속도로 중앙 풍상 플럭스를 만든다. 분산 미분은 셀 중심 차분을 사용한다. 고차 옵션은 CP1-110에서 분리한다. |

#### Q2. 재구성과 역수 원문

`shaders/Pass1.wgsl:41–51`:

```wgsl
fn Reconstruct(west: f32, here: f32, east: f32, TWO_THETAc: f32) -> vec2<f32> {
    let z1 = TWO_THETAc * (here - west);
    let z2 = (east - west);
    let z3 = TWO_THETAc * (east - here);

    let dx_grad_over_two = 0.25 * MinMod(z1, z2, z3);

    let out_east = here + dx_grad_over_two;
    let out_west = here - dx_grad_over_two;

    return vec2(out_west, out_east);
```

`shaders/Pass1.wgsl:145–150`:

```wgsl
    let h2 = h * h;
    let epsilon_c = max(vec4<f32>(globals.epsilon), dB_max);
    let divide_by_h = 2.0 * h / (h2 + max(h2, epsilon_c));  // this is important - the local depth used for the edges should not be less than the difference in water depth across the edge
    u = divide_by_h * hu;
    v = divide_by_h * hv;
    c = divide_by_h * hc;
```

`shaders/Pass2.wgsl:36–41`:

```wgsl
fn NumericalFlux(aplus: f32, aminus: f32, Fplus: f32, Fminus: f32, Udifference: f32) -> f32 {
    if (aplus - aminus != 0.0) {
        return (aplus * Fminus - aminus * Fplus + aplus * aminus * Udifference) / (aplus - aminus);
    } else {
        return 0.0;
    }
```

#### Q3. 중심 차분 원문

`shaders/Pass3_Bous.wgsl:262–266`:

```wgsl
        let dd_by_dx = (-d_right_right + 8.0 * d_right - 8.0 * d_left + d_left_left) * globals.one_over_dx / 12.0;
        let dd_by_dy = (-d_up_up + 8.0 * d_up - 8.0 * d_down + d_down_down) * globals.one_over_dy / 12.0;
        let eta_by_dx_dy = 0.25 * globals.one_over_dx * globals.one_over_dy * (eta_up_right - eta_down_right - eta_up_left + eta_down_left);
        let eta_by_dx_dx = globals.one_over_d2x * (eta_right - 2.0 * eta_here + eta_left);
        let eta_by_dy_dy = globals.one_over_d2y * (eta_up - 2.0 * eta_here + eta_down);
```

### 2.3 시간 적분과 삼중대각 풀이

| 행 ID | 문서(위치·원문) | 코드(파일:줄·원문) | 판정 | 이유 |
|---|---|---|---|---|
| CP1-031 | p.3 식 (16)·(17)의 $2F^{*n}-3F^{*n-1}+F^{*n-2}$와 $2G^{*n}-3G^{*n-1}+G^{*n-2}$; 식 (19)·(20)의 $F^{*p}-F^{*n}$와 $G^{*p}-G^{*n}$ | `shaders/Pass3_Bous.wgsl:283,286`의 전체 식은 CP1-016·017에 인용했다. `:404` `newState = in_state_here_UV + globals.dt / 12.0 * (23.0 * d_by_dt - 16.0 * oldies + 5.0 * oldOldies);` | 불일치 | A. 코드가 $(F^*_{현재}-F^*_{두 단계 전})/(2\Delta t)$를 `d_by_dt`에 포함하고 AB/AM 가중한다. 논문은 비시간미분 우변만 AB/AM 가중한 뒤 별도의 $F^*,G^*$ 증분을 더한다. 두 이산화가 일반적으로 같지 않다. |
| CP1-032 | Tavakkol 2017 p.3 식 (15) $w_{ij}^{n+1}=w_{ij}^n+\frac{\Delta t}{12}(23E_{ij}^n-16E_{ij}^{n-1}+5E_{ij}^{n-2})$ | `shaders/Pass3_Bous.wgsl:404` `newState = in_state_here_UV + globals.dt / 12.0 * (23.0 * d_by_dt - 16.0 * oldies + 5.0 * oldOldies);` | 일치 | 수면 성분의 AB3 가중치와 부호가 같다. 이전 도함수의 실제 시프트는 `js/main.js:2896–2897`이다. |
| CP1-033 | Tavakkol 2017 p.3 식 (16) $U_{ij}^{*n+1}=U_{ij}^{*n}+\frac{\Delta t}{12}(23F_{ij}^n-16F_{ij}^{n-1}+5F_{ij}^{n-2})+2F_{ij}^{*n}-3F_{ij}^{*n-1}+F_{ij}^{*n-2}$ | `shaders/Pass3_Bous.wgsl:404`의 CP1-032 원문 | 불일치 | A. AB3 계수는 같지만 마지막 교차항 증분이 별도로 없다. CP1-031이 시간 미분 포함 방식을 설명한다. |
| CP1-034 | Tavakkol 2017 p.3 식 (17) $V_{ij}^{*n+1}=V_{ij}^{*n}+\frac{\Delta t}{12}(23G_{ij}^n-16G_{ij}^{n-1}+5G_{ij}^{n-2})+2G_{ij}^{*n}-3G_{ij}^{*n-1}+G_{ij}^{*n-2}$ | `shaders/Pass3_Bous.wgsl:404`의 CP1-032 원문 | 불일치 | A. y 운동량에도 같은 시간 미분 포함 방식이 적용된다. AB3 계수의 일치만으로 식 전체를 같다고 쓰지 않는다. |
| CP1-035 | Tavakkol 2017 p.3 식 (18) $w_{ij}^{n+1}=w_{ij}^n+\frac{\Delta t}{24}(9E_{ij}^{n+1}+19E_{ij}^n-5E_{ij}^{n-1}+E_{ij}^{n-2})$ | `shaders/Pass3_Bous.wgsl:408–409` `let predicted = textureLoad(predictedGradients, idx, 0);`<br>`newState = in_state_here_UV + globals.dt / 24.0 * (9.0 * d_by_dt + 19.0 * predicted - 5.0 * oldies + oldOldies);` | 일치 | `predictedGradients`는 예측 단계에서 저장한 $E^n$이다. 보정 단계의 `d_by_dt`가 예측 상태의 $E^{n+1}$이다. 가중치는 AM4이다. |
| CP1-036 | Tavakkol 2017 p.3 식 (19) $U_{ij}^{*n+1}=U_{ij}^{*n}+\frac{\Delta t}{24}(9F_{ij}^{n+1}+19F_{ij}^n-5F_{ij}^{n-1}+F_{ij}^{n-2})+F_{ij}^{*p}-F_{ij}^{*n}$ | `shaders/Pass3_Bous.wgsl:409`의 CP1-035 원문 | 불일치 | A. AM4 계수는 같지만 $F^{*p}-F^{*n}$를 별도 합산하지 않는다. $p$는 인쇄 원문의 위첨자이다. 본문은 예측값 또는 이전 보정값을 사용한다고 설명한다. |
| CP1-037 | Tavakkol 2017 p.3 식 (20) $V_{ij}^{*n+1}=V_{ij}^{*n}+\frac{\Delta t}{24}(9G_{ij}^{n+1}+19G_{ij}^n-5G_{ij}^{n-1}+G_{ij}^{n-2})+G_{ij}^{*p}-G_{ij}^{*n}$ | `shaders/Pass3_Bous.wgsl:409`의 CP1-035 원문 | 불일치 | A. y 운동량도 $G^*$ 미분을 포함한 `d_by_dt`를 가중한다. |
| CP1-038 | p.3 `a third-order Adams–Bashforth scheme as the predictor step, and an optional fourth-order Adams–Moulton scheme as the corrector step` | `js/constants_load_calc.js:32` `timeScheme: 2,  // Time integration choices: 0: Euler, 1: 3rd-order A-B predictor, 2: A-B 4th-order predictor+corrector.` | 일치 | 구현 계수는 AB3 예측과 AM4 보정이다. 코드 주석의 `A-B 4th-order`는 계수의 정확한 명칭이 아니다. 같은 오류를 옮긴 노트는 제4절에서 다룬다. |
| CP1-039 | p.3 `iterated for a predefined number of times, or until the variables converge` | `js/main.js:2757` `if (calc_constants.timeScheme == 2)  // only called when using Predictor+Corrector method.  Adding corrector allows for a time step twice as large (also adds twice the computation) and provides a more accurate solution`; `:2806` `calc_constants.pred_or_corrector = 2;` | 불일치 | A. 현재 호스트는 이 조건 블록 안에서 보정 패스를 한 번 호출한다. 보정 반복 수나 수렴 오차에 따른 반복을 두지 않는다. |
| CP1-040 | p.3 `a first order Euler time integration is used for those two steps` ($n=1,2$) | `shaders/Pass3_Bous.wgsl:399–400` `if (globals.timeScheme == 0) {`<br>`newState = in_state_here_UV + globals.dt * d_by_dt;`; `js/main.js:2618` `frame_count += 1;` | 불일치 | A. 현재 루프는 첫 두 단계에 `timeScheme`를 0으로 바꾸지 않는다. 최초 WebGPU 판부터 같은 선택식이 있었다. 첫 두 단계 Euler를 현재 코드의 기능으로 적지 않는다. |
| CP1-041 | Tavakkol 2017 p.3 식 (21) $A_{ij}^xP_{i-1,j}+B_{ij}^xP_{ij}+C_{i,j}^xP_{i+1,j}=U_{ij}^*$ | `shaders/TriDiag_PCRx.wgsl:70` `dIn = textureLoad(current_stateUVstar, idx, 0).g / bIn;`; `:103` `let txtemp2_out = vec4<f32>(CurrentState.r, dOut, CurrentState.b, CurrentState.a);` | 일치 | RHS g는 $U^*$이고 최종 g 채널은 푼 $P$이다. |
| CP1-042 | Tavakkol 2017 p.3 식 (22) $A_{ij}^yQ_{i,j-1}+B_{ij}^yQ_{ij}+C_{ij}^yQ_{i,j+1}=V_{ij}^*$ | `shaders/TriDiag_PCRy.wgsl:70` `dIn = textureLoad(current_stateUVstar, idx, 0).b / bIn;`; `:103` `let txtemp2_out = vec4<f32>(CurrentState.r, CurrentState.g, dOut, CurrentState.a);` | 일치 | RHS b는 $V^*$이고 최종 b 채널은 푼 $Q$이다. |
| CP1-043 | Tavakkol 2017 p.3 식 (23) $A^\alpha=\frac{dd_\alpha}{6\Delta\alpha}-(B+\frac13)\frac{d^2}{\Delta\alpha^2},\ B^\alpha=1+2(B+\frac13)\frac{d^2}{\Delta\alpha^2},\ C^\alpha=-\frac{dd_\alpha}{6\Delta\alpha}-(B+\frac13)\frac{d^2}{\Delta\alpha^2}$ | `shaders/Update_TriDiag_coef.wgsl:67–69,101–103`의 Q4 원문 | 일치 | $\alpha=x,y$로 대입한 세 계수가 모두 같다. 논문은 이 방향 기호를 직전·직후의 x·y 설명으로 사용한다. |
| CP1-044 | p.3 `cyclic reduction (CR)`; p.6–7 `forward reduction and backward substitution`; Fig. 4의 절반 축소·후진 복원 | `js/Run_Tridiag_Solver.js:48–50` `for (let p = 0; p < calc_constants.Px; p++) {`<br>빈 줄<br>`let s = 1 << p;`; `shaders/TriDiag_PCRx.wgsl:89–92`의 Q4 원문 | 불일치 | A. 현재 PCR은 모든 행을 유지하고 이웃 간격을 매번 두 배로 한다. 별도 후진 대입이 없다. 식 (21)–(23)의 선형계는 유지한다. |
| CP1-045 | p.3 `The water surface elevation ... is directly found`; $P,Q$는 암시적 계를 풀어 얻는다. | `js/Run_Tridiag_Solver.js:37–38` `if (calc_constants.NLSW_or_Bous == 0) {`<br>`runCopyTextures(device, calc_constants, current_stateUVstar, txNewState)`; `:66,91`의 최종 해 복사 | 일치 | NLSW는 $U^*=P,V^*=Q$이므로 삼중대각 풀이를 생략한다. Boussinesq는 x·y 운동량을 각각 푼다. |

#### Q4. 삼중대각 계수와 PCR 원문

`shaders/Update_TriDiag_coef.wgsl:67–69`:

```wgsl
            a =  d_here * d_dx / (6.0 * globals.dx) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dx * globals.dx);
            b = 1.0 + 2.0 * (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dx * globals.dx);
            c = -d_here * d_dx / (6.0 * globals.dx) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dx * globals.dx);
```

`shaders/Update_TriDiag_coef.wgsl:101–103`:

```wgsl
            a =  d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
            b = 1.0 + 2.0 * (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
            c = -d_here * d_dy / (6.0 * globals.dy) - (globals.Bcoef + 1.0 / 3.0) * d_here * d_here / (globals.dy * globals.dy);
```

`shaders/TriDiag_PCRx.wgsl:89–92`。`TriDiag_PCRy.wgsl:89–92`도 같은 네 식을 쓴다.

```wgsl
    let r = 1.0 / (1.0 - aIn * cInLeft - cIn * aInRight);
    let aOut = -r * aIn * aInLeft;
    let cOut = -r * cIn * cInRight;
    let dOut = r * (dIn - aIn * dInLeft - cIn * dInRight);
```

### 2.4 경계·쇄파·마찰·고립파

| 행 ID | 문서(위치·원문) | 코드(파일:줄·원문) | 판정 | 이유 |
|---|---|---|---|---|
| CP1-046 | p.4 §2.4 `Two layers of ghost cells ... at each boundary`; 세 종류는 `sinewave maker, sponge layer, and fully reflective solid wall` | `shaders/Pass3_Bous.wgsl:99` `if (idx.x >= globals.width - 2 \|\| idx.y >= globals.height - 2 \|\| idx.x <= 1 \|\| idx.y <= 1) {`; `shaders/BoundaryPass.wgsl:404–405` `if (idx.x <= 1) {`<br>`BCState = WestBoundarySolid(idx);` | 일치 | 양 끝의 두 층은 계산 내부에서 제외되고 경계 패스가 채운다. 추가 경계 종류는 CP1-117에서 분리한다. |
| CP1-047 | Tavakkol 2017 p.4 식 (24) $(P,Q)\cdot\mathbf n=0,\quad\nabla w\cdot\mathbf n=0$; 가장 가까운 두 내부 셀을 거울 반사한다. | `shaders/BoundaryPass.wgsl:80–83` `fn WestBoundarySolid(idx: vec2<i32>) -> vec4<f32> {`<br>`let real_idx = vec2<i32>(globals.boundary_shift  - idx.x, idx.y);`<br>`let in_state_real = textureLoad(txState, real_idx, 0);`<br>`return vec4<f32>(in_state_real.r, -in_state_real.g, in_state_real.b, in_state_real.a);` | 일치 | 서쪽은 x 법선 운동량을 반전하고 수면과 접선 운동량을 유지한다. 남북은 z 채널을 반전한다. `boundary_shift=4`이며 Fig. 3과 같은 반사점이다. |
| CP1-048 | Tavakkol 2017 p.4 식 (25) $\eta=a\sin(\omega t-k_xx-k_yy)$ | `shaders/BoundaryPass.wgsl:171–173` `let kx = cos(theta_mod) * (x + xshift) * k;`<br>`let ky = sin(theta_mod) * (y + yshift) * k;`<br>`var eta = amplitude * sin(omega * t - kx - ky + phase) * min(1.0, t / period);` | 불일치 | A. 위상·한 주기 선형 램프·시간에 따라 움직이는 원점이 추가되었다. 추가 `phase`가 0이고 램프가 1이어도 일반적으로 원점 이동이 남는다. |
| CP1-049 | Tavakkol 2017 p.4 식 (26) $P=c\cos\theta\eta$ | `shaders/BoundaryPass.wgsl:183–184` `let speed = globals.boundary_g * eta / (c * k) * tanh(k * d);`<br>`let hu = speed * cos(theta_mod);` | 불일치 | A. 코드 계수는 $g\tanh(kd)/(ck)$이다. 정확한 선형 분산관계 $\omega^2=gk\tanh(kd)$와 $c=\omega/k$를 동시에 쓰면 $c$와 같아진다. 현재 k는 근사식이므로 그 등식이 모든 입력에서 정확히 성립하지 않는다. |
| CP1-050 | Tavakkol 2017 p.4 식 (27) $Q=c\sin\theta\eta$ | `shaders/BoundaryPass.wgsl:183,185` `let speed = globals.boundary_g * eta / (c * k) * tanh(k * d);`<br>`let hv = speed * sin(theta_mod);` | 불일치 | A. y 운동량도 같은 근사 분산관계 차이를 갖는다. |
| CP1-051 | Tavakkol 2017 p.4 식 (28) $c=\frac\omega k,\quad\omega=\frac{2\pi}{T},\quad k_x=\cos(\theta)k,\quad k_y=\sin(\theta)k$ | `shaders/BoundaryPass.wgsl:155–157` `let omega = 2.0 * globals.PI / period;`<br>`let k = calc_wavenumber_approx(omega, d);`<br>`let c = omega / k;` | 일치 | 주파수·위상속도·방향별 파수의 정의가 같다. 코드의 좌표 이동은 CP1-048에서 다룬다. |
| CP1-052 | Tavakkol 2017 p.4 식 (29) $k=\frac{\omega^2}{g}\sqrt{\coth}\left(\frac{\omega^2d}{g}\right)$ | `shaders/BoundaryPass.wgsl:129` `let k = omega * omega / (globals.boundary_g * sqrt(tanh(omega * omega * d / globals.boundary_g)));` | 불일치 | F. 원문의 근호 상선은 `coth`까지만 덮고 인수는 밖에 인쇄되어 있다. 해석: 함수값에 제곱근을 적용하는 Eckart 표기로 읽으면 $\sqrt{\coth r}=1/\sqrt{\tanh r}$이며 코드와 같다. 이 해석을 인쇄식 자체의 수정으로 표시하지 않는다. |
| CP1-053 | p.4 정현파 경계 `does not allow treatment of waves approaching the boundary`와 `only if nonlinearity is insignificant` | `shaders/BoundaryPass.wgsl:453` `BCState = BoundarySineWave(idx, iBC, jBC, current_boundary);` | 일치 | 기존 해에 방사 성분을 더하지 않고 경계 상태를 대입한다. 코드에 비선형성의 크기를 검사하는 조건은 없다. 논문의 제한은 사용 조건이다. |
| CP1-054 | Tavakkol 2017 p.4 식 (30) $\gamma(x,y)=f(x)=\frac12\left(1+\cos\left(\pi\frac{L_s-D(x,y)}{L_s}\right)\right)$; 층 안에서만 $\eta,P,Q$에 곱한다. | `shaders/BoundaryPass.wgsl:105–107` `let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (f32(globals.BoundaryWidth - idx.x) + 2.0) / f32(globals.BoundaryWidth - 1))), 0.005);`<br>`let new_state = textureLoad(txState, idx, 0);`<br>`return vec4<f32>(gamma * new_state.r, gamma * new_state.g, gamma * new_state.b, gamma * new_state.a);` | 불일치 | A. 코드가 코사인 계수에 추가 0.5와 지수 0.005를 적용한다. 코드가 격자 개수와 유령 셀 위치로 거리를 계산한다. 모서리는 `:395–397`의 가중평균으로 합친다. 논문 $f(x)$의 표기는 이 감쇠함수이며 마찰계수 $f$와 구분한다. |
| CP1-055 | p.4 §2.5 `Wave breaking is not implemented ... with a direct treatment`; p.8 `does not employ an explicit wave-breaking model`; minmod 수치소산이 쇄파 소산을 닮는다고 설명한다. | `js/constants_load_calc.js:56` `useBreakingModel: 1, // inlcude breaking model when == 1`; `shaders/Pass_Breaking.wgsl:98` `// Kennedy et al breaking model, default parameters` | 불일치 | A. 2024-04-08 커밋이 명시적 쇄파 옵션과 계수를 추가했다. 현재 코드는 minmod 소산 외에 쇄파 점성 소산을 갖는다. 수치소산이 실험을 재현한다는 2017년 결과는 현재 판의 검증이 아니다. |
| CP1-056 | Tavakkol 2017 p.4 식 (31) $\begin{bmatrix}f_1\\f_2\end{bmatrix}=f\begin{bmatrix}P\\Q\end{bmatrix}\frac{\sqrt{P^2+Q^2}}{h^2}$ | `shaders/Pass3_Bous.wgsl:90` `f = f * sqrt(hu * hu + hv * hv) * divide_by_h2;`; `:392`의 소스 전체 식은 CP1-009에 인용했다. | 일치 | 정칙화·상한이 작동하지 않는 수심에서는 식 (31)의 운동량 방향·크기·음의 소스 부호와 같다. 정칙화 변경은 CP1-058에서 분리한다. |
| CP1-057 | Tavakkol 2017 p.4 식 (32) $f=\frac{gn^2}{h^{1/3}}$ | `shaders/Pass3_Bous.wgsl:82–85` `if (globals.isManning == 1) {`<br>`f = globals.g * pow(friction_here, 2.0) * pow(abs(divide_by_h), 1.0 / 3.0);`<br>`} else {`<br>`f = friction_here;` | 일치 | `isManning==1`은 n을 제곱한다. 그 외는 주어진 이차 마찰계수이다. 작은 수심 제한과 0.5 상한은 별도 행이다. |
| CP1-058 | p.4 `the same technique as in Eq. (14) is used`로 마찰의 작은 수심 나눗셈을 설명한다. | `shaders/Pass3_Bous.wgsl:74–79`의 Q5 원문 | 불일치 | A. 현재 마찰은 `h/base_depth`의 네제곱에 $10^{-6}$ 임계를 쓰고 Manning 역수에는 `max(h,delta)`를 쓴다. 면 속도의 역수와도 다르다. 코드 주석 `:69–73`은 단정도 정밀도 때문에 작은 수심 마찰을 줄인다고 명시한다. |
| CP1-059 | p.4 Manning 식의 $g,h$는 `SI units (i.e. m/s² and m respectively)`; `n is the Manning's roughness coefficient` | `js/constants_load_calc.js:42` `g: 9.80665,  // Gravitational constant.`; `:46` `friction: 0.000,  // Dimensionless friction coefficient, or Mannings 'n', depending on isManning choice.` | 문서에만 | H. SI 단위 사용은 물리 입력 규약이다. 코드가 숫자의 단위를 검사하지 않는다. 원문의 `not dimensionally balanced`를 n의 단위가 없는 수학적 증명으로 바꾸지 않는다. |
| CP1-060 | Tavakkol 2017 p.4 식 (33) $\eta_s=H_s\operatorname{sec}\,\mathrm h(k_s((x-x_0)\cos(\theta)+(y-y_0)\sin(\theta)))^2$ | `shaders/AddDisturbance.wgsl:45` `var eta = amplitude / pow(cosh(k * (xloc * cos(angle) + yloc * sin(angle))),2.0);` | 불일치 | F. 인쇄는 `sec h`로 띄워져 있다. 해석: hyperbolic secant의 제곱을 뜻하면 $\operatorname{sech}^2\xi=1/\cosh^2\xi$이다. 육상 수면 잘라내기는 CP1-124에서 분리한다. |
| CP1-061 | Tavakkol 2017 p.4 식 (34) $\begin{bmatrix}P_s\\Q_s\end{bmatrix}=c_s\eta_s\begin{bmatrix}\cos(\theta)\\\sin(\theta)\end{bmatrix}$ | `shaders/AddDisturbance.wgsl:46–47` `let P = sqrt(1.0 + 0.5 * amplitude / depth) * eta * c * cos(angle);`<br>`let Q = sqrt(1.0 + 0.5 * amplitude / depth) * eta * c * sin(angle);` | 불일치 | A. 현재 코드가 두 성분에 $\sqrt{1+H_s/(2d)}$를 더 곱한다. 부호를 임의로 바꾸거나 이 계수를 생략해 노트에 옮기지 않는다. |
| CP1-062 | Tavakkol 2017 p.4 식 (35) $k_s=\sqrt{\frac{3\lvert H_s\rvert}{4d^3}}$ | `shaders/AddDisturbance.wgsl:42` `let k = sqrt(0.75 * abs(amplitude)/pow(depth,3.0));` | 일치 | $3/4=0.75$이며 음의 파고에 절댓값을 취한다. |
| CP1-063 | Tavakkol 2017 p.4 식 (36) $c_s=\sqrt{g(H_s+d)}$ | `shaders/AddDisturbance.wgsl:43` `let c = sqrt(globals.g * (amplitude + depth));` | 일치 | 파고와 정수심을 합한 뒤 g를 곱하고 제곱근을 취한다. 파고 허용 범위에 대한 코드 검사 여부는 CP1-124에서 다룬다. |
| CP1-064 | p.4 `allows insertion of a depression wave ... with negative wave heights. However, such a wave is not expected to maintain its shape.` | `shaders/AddDisturbance.wgsl:42,45`의 CP1-060·062 원문 | 일치 | 음의 진폭이 함수의 인수로 들어갈 수 있다. 모양 유지에 대한 경고는 이론적 제한이다. 구현이 모든 음의 진폭을 정상 처리한다는 뜻으로 확장하지 않는다. |
| CP1-065 | p.4 `adding η, P, and Q in each cell`로 고립파를 중첩하고 GUI에서도 추가한다. | `shaders/AddDisturbance.wgsl:182–185` `if (globals.disturbanceType == 1) {      // solitary wave`<br>`let amplitude = globals.disturbanceCrestamp;`<br>`let angle = globals.disturbanceDir * 3.1415 / 180.;`<br>`disturbance = solitary_wave(xloc, yloc, amplitude, angle, depth, bottom);` | 일치 | 파고·방향·마루 위치를 사용한 고립파 교란 경로가 있다. 식 (34)의 변경과 입력 파일 형식은 별도 행이다. |

#### Q5. 마찰 정칙화 원문

`shaders/Pass3_Bous.wgsl:74–79`。`shaders/Pass3_NLSW.wgsl:74–79`도 같다.

```wgsl
    let h_scaled = h / globals.base_depth;
    let h2 = h_scaled * h_scaled;
    let h4 = h2 * h2;
    let divide_by_h2 = 2.0 * h2 / (h4 + max(h4, 1.e-6)) / globals.base_depth / globals.base_depth;
 
    let divide_by_h = 1. / max(h, globals.delta); 
```

### 2.5 소프트웨어 설명·자료 형식·Fig. 1–5

Fig. 2의 값은 논문이 제시한 입력 예제이다. 논문은 그 값을 일반 기본값이라고 부르지 않는다. 아래에서 예제값과 현재 기본값을 구분한다.

| 행 ID | 문서(위치·원문) | 코드(파일:줄·원문) | 판정 | 이유 |
|---|---|---|---|---|
| CP1-066 | p.5 §3.2 `an XML (Extensible Markup Language) file`; `we use CML as the format`; Fig. 2 `<?xml version="1.0"?>`, `<Experiment>`, `<name>Sample Experiment</name>` | `js/constants_load_calc.js:438` `var configJson = JSON.parse(configContent);`; `:443` `calc_constants = { ...calc_constants, ...loadedConfig };` | 불일치 | A. 현재 설정 입력은 평면 JSON을 기본 객체에 합친다. CML의 XML 루트·이름 태그와 동일한 파서가 아니다. |
| CP1-067 | p.5 Fig. 2 `<model type = "BSNQ">`; 본문은 `Boussinesq and NLSW` 선택을 설명한다. | `js/constants_load_calc.js:36` `NLSW_or_Bous: 0,  // Choose 0 for Non-linear Shallow Water (NLSW), 1 for Madsen Boussinesq, 2 for Fully Non-linear Boussinesq (COULWAVE equations)` | 불일치 | A. 선택 기능은 남지만 키·값 표현이 다르다. 예제 `BSNQ`는 현 기본값 0을 뜻하지 않는다. COULWAVE 추가는 CP1-126에서 분리한다. |
| CP1-068 | p.5 Fig. 2 `<parameters epsilon = 5e-12 correctionStepsNum = 2 timestep = 0.005></parameters>` | `js/constants_load_calc.js:486` `calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);`; `:502` `calc_constants.epsilon = Math.pow(calc_constants.delta, 2);` | 불일치 | A. 현재 dt와 epsilon은 파생값이다. `correctionStepsNum=2`를 해석하는 반복은 현재 경로에 없다. 현재 `timeScheme=2`는 반복 횟수가 아니다. |
| CP1-069 | p.5 Fig. 2 `<friction type = "Manning" coef = 0.0>` | `js/constants_load_calc.js:46–47` `friction: 0.000,  // Dimensionless friction coefficient, or Mannings 'n', depending on isManning choice.`<br>`isManning: 0,  // A boolean friction model value, if==1 'friction' is a Mannnigs n, otherwise it is a dimensionless friction factor (Moody).` | 불일치 | A. 현재 키는 `friction`,`isManning`이다. 예제의 Manning 선택과 현재 기본 이차 마찰 선택은 서로 다른 설정이다. 두 경우 모두 0이면 이 마찰 소스는 0이다. |
| CP1-070 | p.5 Fig. 2 `<fieldDimensions width = 30 length = 30 stillWaterElevation = 0>`; `<gridSize nx = 601 ny = 601>` | `js/constants_load_calc.js:23–28`의 `WIDTH: 800`, `HEIGHT: 600`, `dx: 1.0`, `dy: 1.0`; `:43` `seaLevel: 0.0,  // Water level shift from given datum - depreciated - no longer used` | 불일치 | A. 논문은 길이와 셀 수를 분리해 주는 예제이다. 현 입력은 셀 수와 격자 간격을 쓴다. `stillWaterElevation`을 현 활성 수위 이동 옵션으로 번역하지 않는다. |
| CP1-071 | p.5 Fig. 2 `<bathymetryFilePath> \resources\bathy.cbf </bathymetryFilePath>`; 본문은 상대·절대 경로의 formatted ASCII를 허용한다. | `js/File_Loader.js:11` `lines = bathymetryContent.split('\n');`; `:17` `filePath = calc_constants.exampleDirs[calc_constants.run_example] + 'bathy.txt';` | 불일치 | A. 지형의 텍스트 격자 입력 기능은 남는다. CML 경로 태그 대신 업로드 내용 또는 예제 `bathy.txt`를 읽는다. 실제 행·열 검사는 CP1-118에서 다룬다. |
| CP1-072 | p.5–6 초기조건은 `initial values for w, P, and Q`가 있는 formatted ASCII; Fig. 2 `<hotStartFilePath> N/A </hotStartFilePath>` | `js/File_Loader.js:99` `filePath = calc_constants.exampleDirs[calc_constants.run_example] + 'etaInitCond.txt';`; `js/constants_load_calc.js:50` `loadetaIC: 0,  // Load initial free surface from file when == 1` | 불일치 | A. 현 입력은 수면 격자를 읽는 경로이다. 논문이 설명한 세 상태 전체 hot start와 같다고 쓰지 않는다. 현재 초기 운동량 설정은 Q6에 인용한다. |
| CP1-073 | p.5 Fig. 2 `<solitaryWave H = 0.05 theta = 0 xc = 5 yc = 15>`와 `<solitaryWave H = 0.05 theta = -45 xc = 5 yc = 25>`; p.6 `several solitary waves` 초기 배치 | `js/constants_load_calc.js:138–142`의 `disturbanceType: 1`, `disturbanceXpos: 0.0`, `disturbanceYpos: 0.0`, `disturbanceCrestamp: 0.0`, `disturbanceDir: 0.0`; `shaders/AddDisturbance.wgsl:235` `let state_out = in_state_here + disturbance;` | 불일치 | A. 현재는 한 교란의 위치·파고·각도를 상태에 더한다. CML의 반복 `<solitaryWave>` 목록을 읽는 동작과 구분한다. 각도 변환은 `:184`의 도→라디안이다. |
| CP1-074 | p.5 Fig. 2 서 `type="SineWave" seaLevel=0 widthNum=2`, `amplitude=.01 period=2 theta=0`; 동 `type="Sponge" seaLevel=0 widthNum=20`; 남·북 `type="Solid" seaLevel=0 widthNum=2` | `js/constants_load_calc.js:63–68`의 경계 네 키·`BoundaryWidth: 20`·`incident_wave_type: -1`; `js/Wave_Generator.js:59` `return { numberOfWaves: 1, waveData: [[0.5 * waveHeight, wavePeriod, waveDirectionDegrees * DEG_TO_RAD, 0.0]] };` | 불일치 | A. 현재 경계값 0·1·2는 벽·흡수층·입사파이다. 흡수층 폭은 공통 셀 개수 `BoundaryWidth`이다. 현재 GUI의 H는 파고이고 셰이더 입력 진폭은 H/2이다. CML의 amplitude와 직접 동일시하지 않는다. |
| CP1-075 | p.5 Fig. 2 `<logData doLog = true logStep = 20>`, `<logPath>C:\conical_island\</logPath>`; `<range filename="island">`의 `(228,228)`–`(374,374)`; `<gauges filename="gauges">229,302,249,302,353,302,354,302,301,249</gauges>` | `js/File_Writer.js:531` `export async function writeSurfaceData(total_time,frame_count_output,device,txBottom,txState,txBreaking,txModelVelocities, buffer) {`; `:560` `let filename = \`elev_${frame_count_output}.bin\`;` | 불일치 | A. 논문은 로그 주기·저장 경로·부분 사각형·계측점을 CML에서 지정한다. 현 전체장 출력은 개별 다운로드 파일을 만든다. 현 계측점 시계열은 별도 경로이다. 이전 좌표와 이름을 현 기본값으로 옮기지 않는다. |
| CP1-076 | p.6 `The output files are written into a formatted ASCII file.` | `js/File_Writer.js:604` `const blob = new Blob([data.buffer], { type: 'application/octet-stream' });`; `scripts/load_WebGPUCeleris_output.m:30` `eta = fread(fid, [nx, ny], 'float32');` | 불일치 | A. 현 전체장 값은 float32 이진 파일이다. `time_N.txt`,`dx.txt`,`dy.txt`,`nx.txt`,`ny.txt`는 텍스트 메타데이터이다. 전부 ASCII라는 설명과 다르다. |
| CP1-077 | p.6 `In the next version ... more efficient format, such as NetCDF.` | `js/File_Writer.js:604`의 CP1-076 원문 | 문서에만 | H. 논문은 미래 계획의 예로 NetCDF를 든다. 구현 완료 주장으로 읽지 않는다. 현재 이진 출력이 NetCDF라는 뜻도 아니다. |
| CP1-078 | p.6 §3.3 `2D-texture of size n_x × n_y`; `float4`·단정도 r/g/b에 $w,P,Q$ | `js/Create_Textures.js:4–5` `size: [width, height, 1],`<br>`format: 'rgba32float',`; `shaders/Pass3_Bous.wgsl:123`의 CP1-005 원문 | 일치 | 수치 상태의 텍스처 크기와 32비트 실수 네 채널 구조는 같다. 렌더 캐시의 반정밀도는 수치 상태와 구분한다. |
| CP1-079 | p.6 `while “a” is remained unused.` | `shaders/Pass1.wgsl:127` `let hcwy = Reconstruct(in_west.w, in_here.w, in_east.w, TWO_THETAc);`; `shaders/Pass3_Bous.wgsl:414` `newState.a = max(newState.a, breaking_B);  // use the B value from Kennedy et al as a foam intensity` | 불일치 | A. 현 alpha는 스칼라·거품·오염물질 수송에 사용한다. p.6 Fig. 3의 반환 alpha=0과 현재 alpha 유지의 차이도 여기 포함한다. |
| CP1-080 | p.6 각 수치 단계는 텍스처를 셰이더에 주고 `the render target texture` 한 출력을 얻는다. | `shaders/Pass1.wgsl:23–26`의 네 `texture_storage_2d<rgba32float, write>`; `js/Run_Compute_Shader.js:12` `const computePass = commandEncoder.beginComputePass();`; `:19` `computePass.dispatchWorkgroups(dispatchX, dispatchY);` | 불일치 | A. 현 계산은 compute pass이며 한 패스에서 여러 storage texture에 쓴다. 이전 픽셀·렌더 타깃 중심 설명을 현재 GPU 호출 형식으로 적용하지 않는다. |
| CP1-081 | p.4–5 §3.1 `main.cpp`, `engine.cpp`, `compute.hlsl`, `graphics.fx`, `gui_manager.cpp`; p.5 Fig. 1 `Read CML input file` → `Simulate a few timesteps` → 선택 로그 → 렌더 → GUI | `js/main.js:2615`의 CP1-003 원문; `js/main.js:2641` `runComputeShader_EncStack(device, commandEncoderStack, Pass1_uniformBuffer, Pass1_uniforms, Pass1_Pipeline, Pass1_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);` | 불일치 | A. 역할의 흐름은 이어지지만 파일 분할·입력 파서·GPU 호출 구현이 바뀌었다. 현 호스트는 `js/main.js`이며 계산은 WGSL 파일들이다. Fig. 1을 현 파일 호출 그래프로 쓰지 않는다. |
| CP1-082 | p.7 §3.4 Visual C++ 2008 Express, `Celeris.sln`, DirectX SDK, `Coerci`, `Guichan`, `TinyXML`, `shaders`·`graphics` 배치 | `ARCHITECTURE.md:3` `Celeris-WebGPU is a static browser application that runs a coastal wave model almost entirely on the GPU. The browser loads vanilla JavaScript modules, creates WebGPU textures and pipelines, then advances the shallow-water or Boussinesq state through a sequence of WGSL compute passes. There is no server, package manager, build step, or transpilation layer. The source files in \`js/\` and \`shaders/\` are the application.` | 불일치 | A. 이전 Windows 빌드 절차이다. 외부 래퍼와 GUI·XML 라이브러리 내부는 H 대상이며 판독하지 않는다. 이 행의 결론은 현재 배포 구성과의 판 차이이다. |
| CP1-083 | p.7 §3.5 `Celeris.exe`, `setting.init`, 입력 절대경로가 없거나 잘못되면 파일 브라우저를 연다. | `README.md:36–43`의 설정 JSON·지형 업로드와 `Start Simulation`; `js/constants_load_calc.js:438` `var configJson = JSON.parse(configContent);` | 불일치 | A. 현재 진입점은 HTML과 브라우저 파일 입력이다. exe와 init 경로 탐색의 설명은 2017년 판에 한정한다. |
| CP1-084 | p.2·7·11 실행 중 물·지형·수치·물리 매개변수 변경, 고립파 추가, 일시정지·초기화 | `js/main.js:2614` `if (calc_constants.simPause < 0) {// do not run compute loop when > 0, when the simulation is paused {`; `shaders/AddDisturbance.wgsl:235` `let state_out = in_state_here + disturbance;` | 일치 | 현재 호스트에도 상호작용과 교란·정지 제어가 있다. 설정 키별 새 기본값은 논문에서 추론하지 않는다. |
| CP1-085 | p.7 Fig. 5와 본문: 반사·굴절의 Fresnel 시각화, 수면 $\eta,u,v$, 속력 색상표, 지형 색상표·텍스처, 격자 중첩과 이동 카메라 | `README.md:18` `- **Real-Time Visualization:** Choose what field to visualize (water surface elevation, flow velocity, vorticity, wave height statistics, etc.) with a dynamic color map. The interface also offers an **Explorer 3D view** for perspective navigation.` | 문서에만 | H. Fig. 5(a)–(c)는 과거 판의 표시 예시이다. 이 작업은 표시 결과를 재현하지 않는다. Fresnel 이론과 외부 영상 사용법도 수치 해법 코드의 대조 대상이 아니다. 현 표시 기능을 이 그림의 픽셀 일치로 검증하지 않는다. |
| CP1-086 | p.4 `shader files are compiled at runtime`; `compute.hlsl` 흡수층 변경으로 부분 반사를 만들 수 있다는 예; 복잡한 조건은 C++·수치해법 수정과 재컴파일을 요구할 수 있다. | `js/Config_Pipelines.js:10` `module: device.createShaderModule({ code: computeShaderCode }),` | 불일치 | A. 실행 시 셰이더 모듈을 만드는 개념은 남는다. 현 대상은 WGSL과 JS이다. `compute.hlsl` 수정·C++ 재컴파일 절차는 이전 판에 속한다. 부분 반사는 구현 완료 기능이 아니라 변경 예제이다. |

### 2.6 검증 사례·식 (37)·Fig. 6–15·나머지 본문

이 절의 H 행은 논문의 적용 사례·후처리·성능 주장을 기록한다. 범위 밖 `examples/`와 `benchmarks/`의 입력·실험 자료를 열어 대조하지 않는다. 사례의 숫자를 코드 기본값으로 바꾸지 않는다.

| 행 ID | 문서(위치·원문) | 코드(파일:줄·원문) | 판정 | 이유 |
|---|---|---|---|---|
| CP1-087 | p.7 §4.1 `1:19.85`; `a dozen wave heights`; $0.005<H/d<0.5$; $H/d<0.01$에는 $\Delta x/h=0.0625$, $\Delta t(g/h)^{0.5}=0.0075$; 나머지는 $\Delta x/d=0.25$, $\Delta t(g/d)^{0.5}=0.03$; $W/d=1$; 동쪽 해빈·서쪽 흡수층·남북 벽; $f=0.0,0.01,0.001$ | 대응 셰이더의 예는 `shaders/BoundaryPass.wgsl:405` `BCState = WestBoundarySolid(idx);`이다. 지정 사례 입력은 범위 밖이다. | 문서에만 | H. 평면 해빈 검증 설정이다. 열거한 격자·시간·파고·마찰값은 사례값이다. |
| CP1-088 | p.7 작은 파고 설정의 $\Delta x/h$, $\Delta t(g/h)^{0.5}$와 p.2의 총수심 $h$ 정의 | `shaders/Pass3_Bous.wgsl:123` `let h_here = in_state_here.x - B_here;` | 불일치 | B. 같은 문단의 나머지 설정은 $d$로 무차원화한다. 총수심 $h$는 공간·시간에 따라 달라지므로 일정 격자·일정 시간 간격의 하나의 기준값을 정하지 못한다. 해석: 의도는 정수심 $d$로 보인다. 원문은 h 그대로 보존한다. |
| CP1-089 | p.7 $100<L/d<1000\ \mathrm m$ | `js/constants_load_calc.js:27` `dx: 1.0,  // Cell size in the x direction.` | 불일치 | B. 무차원 길이비 $L/d$의 상한 뒤에 m를 붙였다. 같은 문장의 $W/d=1$ 및 무차원화 설명과 맞지 않는다. |
| CP1-090 | p.7 Fig. 6 `maximum run-up ... versus ... wave height`; 축 $R/d,H/d$; 범례 `f = 0.000`, `f = 0.010`, `f = 0.001`, `Synolakis (1987)` | 해당 실험 산출물은 현재 커널과 직접 대응하지 않는다. | 문서에만 | H. 로그 축으로 최대 수직 처오름을 비교한 그림이다. 현재 코드의 계산 결과를 확인한 그림으로 사용하지 않는다. |
| CP1-091 | p.8 Fig. 7 캡션 $t(g/h)^{0.5}=15,20,25,45$; 패널 내부 표기는 $t\sqrt{g/d}=15,20,25,45$; 실선 수치·점 실험 | `js/main.js:2624` `total_time = frame_count * calc_constants.dt + calc_constants.start_time_shift;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n` | 불일치 | B. 같은 그림의 캡션과 패널이 서로 다른 수심 기호를 쓴다. 시간의 수치는 같다. 코드 시간 생성이 이 내부 표기 모순을 해소하지 않는다. |
| CP1-092 | p.8 $H/d<0.01$에서 마찰의 처오름 영향이 없다는 결과; 큰 쇄파에서 마찰별 결과가 갈라짐; Fig. 7 사례 $H/d=0.28$, $f=0.0075$; p.10 minmod 소산의 쇄파 모사 해석 | `shaders/Pass1.wgsl:46` `let dx_grad_over_two = 0.25 * MinMod(z1, z2, z3);` | 문서에만 | H. 이전 판 실험의 결과와 저자의 인과 해석이다. `minmod`의 존재만으로 이 성능·물리 주장을 현재 판에서 입증하지 않는다. 명시적 쇄파 부재의 판 차이는 CP1-055이다. |
| CP1-093 | Tavakkol 2017 p.8 식 (37) $z=\begin{cases}0&0\le x<10.67-G\\(10.67-G-x)/25&10.67-G\le x<18.29-G\\0.3048&18.29-G\le x\end{cases}$ | 현재 일반 커널은 `shaders/Pass3_Bous.wgsl:117` `let B_here = textureLoad(txBottom, idx, 0).z;`로 입력 지형을 읽는다. 식 (37)을 하드코딩하지 않는다. | 불일치 | B. 가운데 구간의 오른쪽 극한은 $(10.67-18.29)/25=-0.3048$이다. 다음 구간은 $+0.3048$이다. p.8은 수심이 0.4572 m에서 0.1524 m로 감소한다고 설명한다. 인쇄식의 부호는 그 상승 천퇴 설명과 맞지 않는다. |
| CP1-094 | p.8 무번호 $G(y)=[y(6.096-y)]^{1/2},\quad0\le y\le6.096$ | `js/File_Loader.js:54` `bathy2D[x][y] = parsedValue;` | 문서에만 | H. 반원형 천퇴 사례의 기하 정의이다. 일반 지형 로더는 이 함수를 평가하지 않는다. 수조·사례 지형을 코드에만 없는 기능으로 분류하지 않는다. |
| CP1-095 | p.8 Whalin 수조 $25.6\ \mathrm m\times6.096\ \mathrm m$, 수심 0.4572→0.1524 m; $a=0.0075\ \mathrm m,T=2\ \mathrm s$; 계산 영역 $35\ \mathrm m\times6.096\ \mathrm m$, 서 정현파·동 5 m 흡수층·남북 벽; $2000\times65$셀·0.001 s | `js/Wave_Generator.js:59`의 CP1-074 원문은 일반 파고→진폭 변환이다. 이 사례 입력은 열지 않는다. | 문서에만 | H. 입사 진폭 a를 GUI 파고 H와 구분해야 한다. 사례의 경계폭 5 m를 `BoundaryWidth=5`셀로 옮기지 않는다. |
| CP1-096 | p.8 중심선 시계열 FFT로 제1·2·3 조화성분 진폭을 계산한다. p.9 Fig. 8 `Solid lines are numerical results ... symbols are experimental data from Whalin [15].` | `scripts/load_WebGPUCeleris_output.m:30` `eta = fread(fid, [nx, ny], 'float32');` | 문서에만 | H. Fig. 8은 x(m)에 대한 조화성분 진폭(m)을 비교한다. 후처리 FFT를 이 논문만으로 실시간 셰이더의 기능으로 간주하지 않는다. |
| CP1-097 | p.9 Fig. 9 `a = 0.0075 m and T = 2 s`; p.8 `vertical scale is exaggerated by a factor of 80`; 파 집중과 고차 조화성분 설명 | 현재 사례·영상 출력은 판독하지 않는다. | 문서에만 | H. 이전 판의 천퇴 수면 시각화이다. 확대 배율 80은 방정식 계수가 아니다. |
| CP1-098 | p.9 Briggs 실험: 섬 바닥 지름 7.2 m·측면 경사 1/4; $30\ \mathrm m\times25\ \mathrm m$ 수조·수심 0.32 m; 목표 $H/d=0.05,0.10,0.20$ | 일반 입력은 `js/File_Loader.js:54` `bathy2D[x][y] = parsedValue;`이다. | 문서에만 | H. 실험 배치·목표값이다. 수치 계산의 실제 상대파고와 구분한다. |
| CP1-099 | p.9 수치 영역 $30\ \mathrm m\times30\ \mathrm m$; 중앙 섬·서쪽 초기 고립파; 고립파와 평행한 경계 흡수층·나머지 벽; $601\times601$셀·0.005 s·마찰 무시; 실제 $H/d=0.04,0.09,0.18$ | `shaders/AddDisturbance.wgsl:235` `let state_out = in_state_here + disturbance;` | 문서에만 | H. 실제 파고를 목표값보다 작게 한 이유는 조파기 하류 관측에 가깝기 때문이다. 이 사례 수치를 현재 전역 기본값으로 쓰지 않는다. |
| CP1-100 | p.9 Fig. 10 `gauge locations ... dots`; 좌측 입사; 7.2 m·초기 해안선 4.64 m·상부 2.20 m 지름; #6·#9 전면, #16 측면, #22 후면 | 현재 계측점 입력과 이 실험의 고정 계측점은 별개이다. | 문서에만 | H. x·y(m) 평면 배치도이다. p.9 본문의 계측점 배치 참조 `Fig. 11`은 이 Fig. 10과 구분해 읽는다. |
| CP1-101 | p.9 Fig. 11 `H/d = 0.04 ... gauges #6, #9, #16, and #22 (a–d)`; 파선 실험·실선 수치 | 현재 모델 시계열은 실행하지 않았다. | 문서에만 | H. 네 패널은 시간(s)에 대한 수면 $\eta$(m)이다. 논문의 비교를 현재 커밋의 수치 검증으로 옮기지 않는다. |
| CP1-102 | p.10 Fig. 12 `H/d = 0.09 ... gauges #6, #9, #16, and #22 (a–d)` | 현재 모델 시계열은 실행하지 않았다. | 문서에만 | H. 네 계측점의 실험·수치 시계열 그림이다. |
| CP1-103 | p.10 Fig. 13 `H/d = 0.18 ... gauges #6, #9, #16, and #22 (a–d)` | 현재 모델 시계열은 실행하지 않았다. | 문서에만 | H. 네 계측점의 실험·수치 시계열 그림이다. (c)의 이중 첨두에 관한 설명은 CP1-104이다. |
| CP1-104 | p.9 선두파 높이·형태와 큰 파의 draw-down을 잘 예측하나 가장 작은 파의 draw-down을 과소예측; p.10 이중 첨두가 더 잘 분해됨; `This might be because of the finer resolutions`; 큰 파의 #22 처오름 비교에서 무쇄파 선행모델은 약 25% 과대예측 | 현재 커널의 존재는 이 경험적 정확도·인과 관계의 증거가 아니다. | 문서에만 | H. 저자의 가능성 표현 `might`를 확정 원인으로 바꾸지 않는다. 선행모델과의 상대 비교는 현재 코드 결함 판정에 사용하지 않는다. |
| CP1-105 | p.10 선행모델 $234\times201$격자·3.2 GHz Pentium 4·3.3 h; Celeris 같은 셀 수·Quadro K600·1.8 GHz Xeon·15 s 미만; `not directly comparable` | 현재 모델의 실행 시간은 측정하지 않았다. | 문서에만 | H. 서로 다른 방정식·수치 차수의 계산 시간이다. 원문은 직접 비교할 수 없다고 명시한다. 이 수치로 현재 WebGPU 가속비를 계산하지 않는다. |
| CP1-106 | p.10 무번호 $\delta=s\Delta x/3$; 초기 해안선 반지름 2.32 m로 수평 최대 처오름 무차원화; 서→동 입사; 선택 문턱의 처오름이 격자 크기별 불변이었다는 주장 | `js/constants_load_calc.js:501` `calc_constants.delta = Math.min(calc_constants.min_allowable_depth,calc_constants.base_depth / 5000.0);` | 문서에만 | H. 이 δ는 최대 처오름 후처리 문턱이다. 현재 수력 계산의 `delta`와 목적이 다르다. 논문은 s를 명시적으로 정의하지 않으므로 경사라고 확정해 덧붙이지 않는다. |
| CP1-107 | p.11 Fig. 14 $H/d=0.18$; 전면 최대 처오름(a)·후면 감싸는 파 충돌(b)·후면 최대 처오름(c); 수직 10배; p.9 (a,b)는 v 색상표, p.10 (c)는 η 색상표 | 현재 표시 영상은 실행하지 않았다. | 문서에만 | H. 세 스냅숏은 이전 판의 물리·시각화 사례이다. 수직 배율·색상 값과 계산 물리량을 구분한다. |
| CP1-108 | p.11 Fig. 15 `H/d = 0.04 (a), 0.09 (b), and 0.018 (c)`; 실선 수치·x 표식 측정 | p.9 본문과 p.10 Fig. 13, p.11 Fig. 14는 가장 큰 사례를 0.18이라고 적는다. | 불일치 | B. 캡션의 0.018은 같은 논문이 반복한 0.18과 열 배 다르다. 세 극좌표 그림의 무차원 수평 처오름 비교 자체는 H 대상이다. |

| 행 ID | 문서(위치·원문) | 코드(파일:줄·원문) | 판정 | 이유 |
|---|---|---|---|---|
| CP1-130 | p.1 논문·프로그램 서지·DOI·저자·소속·접수/수정/승인/공개일·키워드·교신 정보; p.11 결론·감사의 글·부록·참고문헌 [1]–[21] | 대응 수치 커널은 없다. | 문서에만 | H. 이 서지·감사·보충자료 안내는 코드 연산이 아니다. p.11의 세 검증 사례 요약은 CP1-087–108에 대응한다. GPL·Direct3D·Windows·상호작용의 결론 반복은 CP1-001·002·083·084에 대응한다. p.4의 `Stephen Thompson`과 p.11 `Stephen Thomson`의 철자 차이 및 [2]·[3]의 중복 번호도 서지 표기로 기록한다. |
| CP1-161 | p.1–2 `first-of-its-kind interactive modeling platform`; NLSW보다 큰 Boussinesq 계산 비용·암시법·큰 stencil·GPU의 병렬성·FVM 강건성에 관한 연구 배경 | 현재 코드의 한 줄만으로 역사적 최초성·타 모델의 계산 비용을 입증할 수 없다. | 문서에만 | H. 서론의 동기·선행연구 평가이다. 구현 존재와 최초성·성능 비교를 구분한다. |
| CP1-162 | p.3 KP07 `preserves stationary steady states`, `guarantees the positivity`, `no need to keep track of the wet–dry front`, `discontinuous bottom topography`; 단정도에서 강건·정확하다는 저자의 평가 | `Pass1.wgsl:136` `h = max(h, vec4<f32>(0.0, 0.0, 0.0, 0.0));` | 문서에만 | H. 원 KP07의 수학적 성질과 저자의 구현 평가이다. 변형한 현재 이산식의 보존성·양수성·정확도 증명으로 자동 승계하지 않는다. 현재 변경은 CP1-028·029·113·114에 기록했다. |
| CP1-163 | p.4 고립파는 평탄 바닥에서 일정 속도·불변 형태로 전파한다. 비선형성과 분산이 균형을 이루면 Boussinesq 방정식이 이를 허용한다. | `AddDisturbance.wgsl:45`의 sech² 초기형 | 문서에만 | H. 고립파의 이론적 정의이다. 초기형을 코드에 넣었다는 사실과 시간 전진 중 형태 유지의 수치 검증을 구분한다. |
| CP1-164 | p.4 `We recommend users to work with the compiled version as much as possible`; p.6 Thomas 전진 소거·후진 대입은 직렬이며 GPU→CPU→GPU 복사가 병목이 된다는 설명; p.7 GUI와 영상 링크 | 현 계산 호출은 `Run_Compute_Shader.js:19` `computePass.dispatchWorkgroups(dispatchX, dispatchY);`이다. | 문서에만 | H. 이전 프로그램 사용 권고·일반 알고리즘 설명·외부 영상 안내이다. Thomas·외부 라이브러리·영상 내부를 판독하지 않는다. |
| CP1-165 | p.9 `Gauges #6 and #9 ... gauge #22 ... (Fig. 11).` | p.9 Fig. 10 캡션 `Experimental setup of the conical island. The gauge locations are shown by dots`; Fig. 11은 네 시계열 | 불일치 | B. 계측점 배치의 그림 참조는 Fig. 10이다. Fig. 11은 시계열이다. |

## 3 코드에만 있는 처리

이 절에서 `문서 없음`은 Tavakkol 2017의 11쪽 안에 해당 현 구현 설명이 없다는 뜻이다. 현재 저장소의 모든 문서에 설명이 없다는 뜻으로 사용하지 않는다. 앞 절에서 이미 A로 판정한 변경은 여기서 중복 행으로 만들지 않는다.

| 행 ID | 문서 | 코드(파일:줄·원문) | 판정 | 이유 |
|---|---|---|---|---|
| CP1-109 | p.3 minmod 설명은 현재 `Theta` 기본값과 습건 램프를 적지 않는다. | `js/constants_load_calc.js:45` `Theta: 2.0,  // Midmod limiter parameter. 1.0 most dissipative(upwind) to 2.0 least dissipative(centered).`; `shaders/Pass1.wgsl:117–118` `let rampcoef = min(max(0.0, wetdry / (0.02 * globals.base_depth)), 1.0);`<br>`let TWO_THETAc = globals.TWO_THETA * rampcoef + 2.0 * (1.0 - rampcoef);  // transition to full upwinding near the shoreline / inundation limit, start transition with a total water depth of base_depth/50.` | 코드에만 | C. `TWO_THETA=2*Theta`이다. 수심이 `0.02*base_depth`보다 작아지면 TWO_THETA가 2로 접근한다. 원문의 `full upwinding` 주석을 기울기가 항상 0이라는 뜻으로 바꾸지 않는다. |
| CP1-110 | 문서 없음. 논문은 KP07 2차 재구성을 설명한다. | `js/main.js:1541` `Pass1_ShaderCode = await fetchShader('/shaders/Pass1_HighOrder.wgsl');`; `:1548` `Pass2_ShaderCode = await fetchShader('/shaders/Pass2_HighOrder_HLLC.wgsl');` | 코드에만 | C. `Accuracy_mode==1`은 7점 MUSCL4와 HLLC 파일을 선택한다. `ReconstructMUSCL4`는 `dh_max>0.60`에서 제한자를 켠다. ±3셀 중 육상에 가까우면 표준 재구성으로 돌아간다. HLLEM 파일은 현 `main.js`가 선택하지 않는다. Q7은 조건 전체를 인용한다. |
| CP1-111 | 문서 없음. | `shaders/Pass1.wgsl:159–163` `let Fr_maxallowed = 3.0 / max(1.0, dBds_max);  // max Fr allowed on slopes less than 45 degrees is 3; for very steep slopes, artificially slow velocity - physics are just completely wrong here anyhow`<br>`if (Frumax > Fr_maxallowed) {`<br>`let Fr_red = Fr_maxallowed / Frumax;`<br>`u = u * Fr_red;`<br>`v = v * Fr_red;` | 코드에만 | C. 지형 경사에 따른 Froude 상한이 있다. `Fr` 계산은 `:154`의 고정 9.81을 사용한다. 이 제한을 논문 minmod의 일부로 합치지 않는다. |
| CP1-112 | 문서 없음. | `shaders/Pass1.wgsl:85–86` `if (h_here <= h_cut) {    //if dry and surrounded by dry, then stay dry - no need to calc`<br>`if(h_north <= h_cut && h_east <= h_cut && h_south <= h_cut && h_west <= h_cut) {`; `shaders/Pass3_Bous.wgsl:142–143`도 같은 조건 | 코드에만 | C. 현재 셀과 네 이웃이 모두 `delta` 이하이면 출력을 0으로 쓰고 반환한다. `Pass0.wgsl:52–55`는 북·동·남·서 이웃 수심을 `txHnear`에 제공한다. |
| CP1-113 | 문서 없음. | `shaders/Pass1.wgsl:120–121` `if(wetdry <= globals.epsilon){`<br>`dB_max = 0.5*vec4<f32>(dB_north, dB_east, dB_south, dB_west);`; `:146–147`의 Q2 원문 | 코드에만 | C. 건조 인접 조건에서 면별 바닥 높이 차이가 정칙화 임계에 들어간다. 해석: `h²`와 높이차의 단위 혼합은 주의가 필요한 구현이다. 이 행은 의도를 명시한 현재 주석을 먼저 반영하며 추가 독립 모순 없이 E로 올리지 않는다. |
| CP1-114 | 문서 없음. | `shaders/Pass2.wgsl:115–119` `if (minH <= globals.delta) {`<br>`mass_diff_x = 0.0;`<br>`mass_diff_y = 0.0;`<br>`phix = 1.0;`<br>`phiy = 1.0;` | 코드에만 | C. 건조 인접 수치 플럭스에서 질량 차 소산을 제거한다. 스칼라 차 소산 계수는 0.5에서 1로 바꾼다. 이 조건을 논문 식 (14)의 속도 정칙화와 구분한다. |
| CP1-115 | 문서 없음. p.2의 $d=0$ 설명보다 넓은 처리이다. | `shaders/Update_neardry.wgsl:19` `let lengthCheck = 3;    // check within three points`; `:29–31` `if (bathy_C >= 0.)`<br>`{`<br>`B_here.w = -99.;`; `shaders/Update_TriDiag_coef.wgsl:42–45`의 Q8 원문 | 코드에만 | C. 7×7 지형 창에 0 이상 표고가 있으면 분산 경로를 끈다. x·y 끝 세 위치의 계수도 항등행이다. `Update_neardry:46–50`은 단일 육상 셀의 중심 표고를 0으로 바꾸고 면 표고를 갱신한다. |
| CP1-116 | 문서 없음. | `shaders/BoundaryPass.wgsl:658` `h_cut.x= max(globals.delta, abs(B_here - B_north));`; `:703` `else if (sum_dry == 1 && (globals.algochanges == 0 \|\| nearshore <= globals.delta)) {  // freeze end of single grid channel, with free surface gradient equal to zero`; `:712` `if (h_here <= globals.delta) {` | 코드에만 | C. 방향별 표고차와 delta로 이웃 습건을 판정한다. 단일 습윤 셀·한 격자 수로 끝을 억제한다. 최종 얕은 셀의 운동량·스칼라·퇴적물 상태를 0으로 만든다. `Pass3_Bous:367–385`는 습건에 따라 수면 기울기를 0 또는 편측 차분으로 바꾼다. |
| CP1-117 | p.4는 불규칙 방향파와 시계열 경계를 후속 판의 계획으로 적는다. | `shaders/BoundaryPass.wgsl:199` `result = result + sineWave(x, y, globals.total_time, d_here, wave.r, wave.g, wave.b, wave.a, current_boundary);`; `:276` `return vec4<f32>(mix(space_value0, space_value1, globals.ts_time_alpha), 0.0);` | 코드에만 | C. 현재는 여러 파 성분 합성·TMA 생성·5파 transient pulse·주기 겹침·하천 stage/Q·type 5 시공간 보간을 갖는다. type 5는 시작 시간 이동도 적용한다. 세부 종류와 호출 조건은 Q9에 인용한다. 논문의 미래 계획과 현 지원을 구분한다. |
| CP1-118 | 문서 없음. | `js/File_Loader.js:43–45` `if (depthValues.length !== calc_constants.WIDTH) {`<br>`console.error("Bathytopo file at " + filePath + " is not in the correct format.");`<br>`return null;`; `:50` `if (isNaN(parsedValue)) {` | 코드에만 | C. 지형 각 행의 WIDTH와 수치 변환을 검사한다. `:58–77`은 입력 가장자리를 내부 표고로 평탄화한다. `Copy_Data_to_Textures.js:23–25`는 단일 육상점을 초기 입력에서도 평탄화한다. |
| CP1-119 | 문서 없음. | `js/constants_load_calc.js:443` `calc_constants = { ...calc_constants, ...loadedConfig };`; `:501–502` `calc_constants.delta = Math.min(calc_constants.min_allowable_depth,calc_constants.base_depth / 5000.0);`<br>`calc_constants.epsilon = Math.pow(calc_constants.delta, 2);` | 코드에만 | C. JSON 값으로 기본 객체를 덮어쓴 뒤 파생값을 계산한다. 기본 Courant 수는 0.15이다. 기본 `base_depth=20`, `min_allowable_depth=0.005`이면 delta는 0.004이고 epsilon은 0.000016이다. 이는 코드 기본값으로 직접 계산한 값이다. |
| CP1-120 | 문서 없음. | `shaders/Pass3_Bous.wgsl:314–315` `let press_x = -0.5 * h_here * globals.g_over_dx * (P_right - P_left);`<br>`let press_y = -0.5 * h_here * globals.g_over_dy * (P_up - P_down);`; `:389` `overflow_dry = -globals.infiltrationRate;  // hydraulic conductivity of coarse, unsaturated sand` | 코드에만 | C. 외부 압력 경사와 바닥 표고 양수 셀의 침투 질량 소스를 더한다. `:291–300`은 `vort_friction_factor>0`에서 와도 경사 혼합도 더한다. 이들은 논문 식 (1)의 세 소스항 외에 현재 추가된 처리이다. |
| CP1-121 | 문서 없음. p.2의 $w_t=h_t$는 고정 바닥 가정이다. | `shaders/Pass3_Bous.wgsl:306` `let dhdt = textureLoad(txBoundaryForcing, idx, 0).y;`; `shaders/AddDisturbance.wgsl:226–227` `depth_change = depth_motion(xloc, yloc, bottom, globals.time, globals.dt, bottom_initial);`<br>`B_here.z = depth_change.z;` | 코드에만 | C. 처방 바닥 운동과 산사태 교란 경로가 있다. 호스트는 지형 변경 뒤 near-dry와 삼중대각 계수를 갱신한다. `js/main.js:2743–2745`가 그 순서이다. |
| CP1-122 | 문서 없음. p.6은 alpha를 미사용이라고 적었다. | `shaders/Pass3_Bous.wgsl:336` `let c_dissipation = -globals.whiteWaterDecayRate * C_state_here;`; `:418` `newState.a = min(1.0, newState.a + contaminent_source);`; `:422–423` `if (globals.clearConc == 1){`<br>`newState.a = 0.0;` | 코드에만 | C. 현재 alpha에 이류·확산·감쇠·쇄파 거품·오염물질 소스·농도 지우기가 있다. 확산은 `Dxx=Dxy=Dyy=whiteWaterDispersion`을 쓴다. `hc_by_dx_dy`에 2를 곱해 합친다. |
| CP1-123 | 문서 없음. | `shaders/Pass3_Bous.wgsl:88` `f = min(f, 0.5);  // non-physical above 0.5`; `:302` `let friction_here = max(globals.friction, textureLoad(txBottomFriction, idx, 0).x);` | 코드에만 | C. 지역 마찰은 전역값과 지도값 중 큰 값이다. 최종 무차원 f는 0.5 이하로 제한한다. 정칙화의 의도와 작은 수심 제한은 CP1-058에 기록했다. |
| CP1-124 | 문서 없음. | `shaders/AddDisturbance.wgsl:49–50` `if(bottom > 0.0){`<br>`eta = max(0.0, eta - bottom);  // since this is added to the existing state - which for dry areas, eta = bottom already`; `shaders/BoundaryPass.wgsl:140` `let amplitude = 0.5;` | 코드에만 | C. 초기 교란의 육상 eta를 잘라낸다. 경계 고립파 함수는 파고 0.5를 고정한다. 함수 안에는 $H_s+d\ge0$ 또는 $1+H_s/(2d)\ge0$를 검사하는 조건이 없다. 음의 파고 지원을 모든 입력값의 유효성 보장으로 쓰지 않는다. |
| CP1-125 | 문서 없음. 논문 p.3은 Cartesian만 설명한다. | `js/constants_load_calc.js:454–457` `if (calc_constants.grid_type == 2) {`<br>`if (calc_constants.NLSW_or_Bous != 0) {`<br>`console.warn("Spherical grid mode is currently NLSW-only; forcing NLSW_or_Bous to 0.");`<br>`calc_constants.NLSW_or_Bous = 0;` | 코드에만 | C. 구면 격자는 NLSW만 허용한다. 호스트가 고차·퇴적물·Cartesian 쇄파를 0으로 바꾼다. 시간 간격은 위도별 최소 실제 격자 간격으로 계산한다. |
| CP1-126 | 문서 없음. | `js/main.js:1570` `Pass3_ShaderCode_Bous = await fetchShader('/shaders/Pass3_COULWAVE.wgsl');`; `shaders/Update_TriDiag_coef.wgsl:52–53` `if (globals.NLSW_or_Bous == 2) {`<br>`// COULWAVE equations` | 코드에만 | C. COULWAVE 보조 Pass3A·3B·3D grouping·별도 계수·PCR 경로를 지원한다. 논문 식 (2)–(23)을 이 경로 전체의 식으로 적용하지 않는다. |
| CP1-127 | 문서 없음. 2017년 논문에는 퇴적물 지배식·옵션 설명이 없다. | `js/constants_load_calc.js:106` `useSedTransModel: 0, // sed model on or off [0]`; `shaders/SedTrans_Pass3.wgsl:215` `let source_term = (erosion - deposition) * divide_by_h;  // do not add bedload here, since this is only for suspended load`; `shaders/SedTrans_UpdateBottom.wgsl:84` `let dB_here = globals.dt * (e_here_average - d_here_average) / (1.0 - globals.sedC1_n); // this is positive when eroding - when increasing depth, or decreasing elevation` | 코드에만 | C. 현재 부유사 이류·확산, Shields 문턱 침식, 침강 퇴적, MPM 소류사 발산, 공극률을 사용한 지형 변화·hard-bottom 침식 제한이 있다. 초기 기본값은 `d50=0.2`, `n=0.40`, `psi=0.00005`, `criticalshields=0.045`, `denrat=2.65`, 배경 확산 0.01·쇄파 확산 비 0.1이다. 근거는 `constants_load_calc.js:107–114`이다. |
| CP1-128 | 문서 없음. 논문 식 (10)의 순수 x 경사항도 1D에서 남는다. | `transect_version/shaders/Pass3_Bous.wgsl:286–287` `Psi1x = globals.Bcoef_g * d3_here * ((eta_right_right - 2.0 * eta_right + 2.0 * eta_left - eta_left_left) * (0.5 * globals.one_over_d3x));`<br>`Psi2x = globals.Bcoef_g * d2_here * (dd_by_dx * (2.0 * eta_by_dx_dx));`; `:386` `let source_term = vec4<f32>(dhdt + overflow_dry, -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x) + press_x, 0.0, hc_by_dx_dx + c_dissipation);` | 코드에만 | E, 중간. transect는 `Psi2x`를 계산하고 소스에서 쓰지 않는다. 같은 파일 `:385`의 주석 식은 `Psi1x+Psi2x`를 갖는다. 본판 `:392`도 둘을 더한다. 1D화로 교차항을 제거하는 의도는 확인했지만 남는 $2Bgd^2d_x\eta_{xx}$ 제거 설명은 찾지 못했다. 활성 선택 근거와 반대 근거는 제5절에 적는다. |
| CP1-129 | 문서 없음. | `js/Run_Tridiag_Solver.js:57` `const TridiagX_BindGroup_Current = (p == 0) ? TridiagX_BindGroup_BaseToA : ((p % 2 == 1) ? TridiagX_BindGroup : TridiagX_BindGroup_BToA);`; `shaders/TriDiag_PCRx.wgsl:101` `if (globals.p == globals.P - 1) {` | 코드에만 | C. 현재 PCR은 계수 텍스처를 번갈아 읽고 쓴다. 마지막 반복만 최종 운동량을 기록한다. COULWAVE PCR도 별도 파일을 사용한다. 이것은 논문 Fig. 4의 CR 후진 대입이 아니다. |
| CP1-131 | 문서 없음. | `shaders/Pass_Breaking.wgsl:125` `let nu_breaking = min(1.0 * globals.dx * globals.dy / globals.dt, B_Breaking * globals.delta_breaking * h_here * detadt);`; `:129` `let nu_Smag = 0.0; //Smag_cm * globals.dx * globals.dy * sqrt(2. * dPdx * dPdx + 2. * dQdy * dQdy + (dPdy + dQdx) * (dPdy + dQdx)) * divide_by_h;  // temporary, needs to be corrected to strain rate, right now has extra dHdx terms` | 코드에만 | C. 쇄파 나이는 지배 유향 상류 세 셀의 최대 시작시각으로 전달한다. 시작·종료 문턱은 `0.50*sqrt(gh)`, `0.15*sqrt(gh)`이다. 전이 시간은 `5*sqrt(h/g)`이다. 강도 B는 0·선형 램프·1로 나뉜다. 점성 상한은 `dx*dy/dt`이다. Smagorinsky는 0이며 주석 식은 실행하지 않는다. |
| CP1-132 | 문서 없음. | `shaders/Pass3_NLSW.wgsl:216` `// calculate breaking dissipation - breaking dissipation not added for NLSW model`; `shaders/Pass3_Bous.wgsl:360–362` `if (near_dry > 0.){`<br>`breaking_x = dPdxx + 0.5 * dPdyy + 0.5 * dQdxy;`<br>`breaking_y = dQdyy + 0.5 * dPdyx + 0.5 * dQdxx;` | 코드에만 | C. NLSW는 강도 B를 거품 표시에 사용하지만 점성 운동량 소산을 더하지 않는다. Boussinesq도 near-dry 양수 셀에서만 위 점성 소산을 더한다. NLSW의 자기 주석이 이 차이를 명시하므로 E로 분류하지 않는다. |
| CP1-133 | 문서 없음. | `js/Copy_Data_to_Textures.js:10–12` `const actualBytesPerRow = calc_constants.WIDTH * 4 * 4; // 4 channels and 4 bytes per float`<br>`const requiredBytesPerRow = Math.ceil(actualBytesPerRow / 256) * 256;`<br>`const paddedFlatData = new Float32Array(calc_constants.HEIGHT * requiredBytesPerRow / 4);` | 코드에만 | C. CPU→GPU 복사에서 행 바이트 수를 256 배수로 맞춘다. face별 RGBA는 북·동·남·서이며 `txBottom` RGBA는 북면 표고·동면 표고·중심 표고·near-dry 표지이다. 이는 논문의 주 상태 RGB 설명보다 넓은 자료 계약이다. |
| CP1-134 | 문서 없음. | `js/main.js:2915`의 `CalcMeans_Pipeline` 호출과 `:2924`의 `CalcWaveHeight_Pipeline` 호출; `scripts/load_WebGPUCeleris_output.m:55` `drynodes = find(H<=0.0);  % find dry nodes, may need to change 0.0 to some threshold (e.g. 0.1) to eliminate large velocitys in thin flows` | 코드에만 | C. 현재 평균·최댓값·파고 통계·계측점 시계열 및 이진 출력 후처리를 별도로 제공한다. MATLAB의 H≤0 문턱은 논문 처오름 δ와 같지 않다. 시계열·JPEG·GIF·nested 경계 출력은 수치 방정식의 항이 아니다. |
| CP1-135 | 문서 없음. | `index.html:1383–1384` `<option value="0">NLSW</option>`<br>`<option value="1">Boussinesq</option>`; `transect_version/js/main.js:1053` `Pass3_ShaderCode_Bous = await fetchShader('/transect_version/shaders/Pass3_Bous.wgsl');` | 코드에만 | C. HTML 진입점과 transect는 별도 입력·선택 경로를 갖는다. 호스트가 COULWAVE를 처리한다는 사실과 이 HTML 선택지에 COULWAVE가 보인다는 주장은 구분한다. 본판·headless·nots·river·MC 화면 파일의 검색 결과를 Q11에 적는다. |

| 행 ID | 문서 | 코드(파일:줄·원문) | 판정 | 이유 |
|---|---|---|---|---|
| CP1-167 | 문서 없음. 2017년 p.2 식 (1)은 2DH이다. | `transect_version/shaders/Pass1.wgsl:119` `let wetdry = min(h_here, min(h_west, h_east));`; `transect_version/shaders/Update_TriDiag_coef.wgsl:34` `let near_dry = d_here; //textureLoad(txBottom, idx, 0).w;` | 코드에만 | C. transect는 각 y 행의 독립 x 단면을 계산한다. 표준 Pass1은 동·서 면만 재구성한다. Pass2는 x 질량·운동량·스칼라 플럭스만 만든다. 삼중대각 계수·풀이도 x만 활성이다. near-dry 계수 gate는 본판의 7×7 표지 대신 국소 정수심을 사용한다. 상세 대응은 Q12에 적는다. |
| CP1-168 | 문서 없음. | `transect_version/shaders/BoundaryPass.wgsl:158` `let ky = 0.0;`; `:162` `num_waves = 4;`; `:185` `let wave = textureLoad(txWaves_Transect, vec2<i32>(iw, idx.y), 0);` | 코드에만 | C. transect는 행별 파 입력을 사용한다. 이 경로는 ky·hv·원점 이동을 0으로 둔다. 현재 본판의 base_depth 파 입력과 달리 지역 바닥에서 d를 얻는다. transient는 아직 4파이다. 이 차이는 1D 전용 구현 설명으로 적는다. |
| CP1-169 | 문서 없음. | `shaders/Ship_pressure.compute:30` `float Z = ship_draft * exp(-pow(c1 * pow(xc, 2.0) + 2.0 * c2 * xc * yc + c3 * pow(yc, 2.0), 2.0));`; `:80` `ship_pressure[idx] = float4(Z, 0.0, 0.0, 0.0);` | 코드에만 | C. 동봉 HLSL 파일은 배의 중심·방향·크기로 압력형 함수를 만든다. 현재 실행 경로에서 호출되지 않는다. `rg -n -F 'Ship_pressure.compute' js/` 검색 결과는 0건이다. 현 main의 WGSL fetch 목록에도 이 파일이 없다. 활성 압력 입력은 CP1-120의 txBoundaryForcing이다. |

#### Q6. 초기조건의 실제 호출

`js/main.js:616–619`:

```js
        let etaIC2D = await loadInitCondSurface(etaICContent, calc_constants); 
        writeStateFlag = 1; // writing channel 1
        copyInitialConditionDataToTexture(calc_constants, device, etaIC2D, txState, writeStateFlag)
        copyInitialConditionDataToTexture(calc_constants, device, etaIC2D, txstateUVstar, writeStateFlag)
```

`js/Copy_Data_to_Textures.js:261–272`:

```js
            var eta = 0.; // * Math.exp(-(dx * dx + dy * dy) / (2 * sigma * sigma));
            var u = 0.; 
            var v = 0.; 
            if (writeStateFlag == 1){
                eta = initialState[x][y]
            }
            else if (writeStateFlag == 2){
                u = initialState[x][y]
            }   
            else if (writeStateFlag == 3){
                v = initialState[x][y]
            }
```

해석: 함수에는 한 채널을 고르는 분기가 있다. 현재 수면 초기조건 호출은 flag 1을 쓴다. 이 호출은 논문에서 말한 w·P·Q 전체 hot start 파일을 한 번에 읽지 않는다.

#### Q7. 고차 재구성 조건

`shaders/Pass1_HighOrder.wgsl:90–93`:

```wgsl
    var ilim_c = 0; // 1 = TVD limiter, 0 = no limiter
    if (dh_max > 0.60) {
        ilim_c = 1;
    }
```

`shaders/Pass1_HighOrder.wgsl:263`:

```wgsl
    if(wetdry <= globals.epsilon || maxB3 >= -globals.epsilon) {
```

위 조건의 참 분기는 `:266–275`의 표준 `Reconstruct`이다. 거짓 분기는 `:286–303`의 `ReconstructMUSCL4`이다. `shaders/Pass2_HighOrder_HLLEM.wgsl:80`의 `fn HLLEM_Flux(`는 존재한다. `js/main.js:1539–1551`의 선택 분기는 HLLC와 표준 Pass2만 고른다. 따라서 HLLEM은 현재 실행 경로에서 호출되지 않는다. HLLEM의 내부를 이 작업의 완료 조건으로 삼지 않는다.

#### Q8. 분산 정지 조건

`shaders/Update_TriDiag_coef.wgsl:42–46`:

```wgsl
    if (idx.x <= 2 || idx.x >= width - 3 || near_dry < 0.0) {
        a = 0.0;
        b = 1.0;
        c = 0.0;
    }
```

y 방향은 `:76–80`에서 `idx.y <= 2 || idx.y >= height - 3 || near_dry < 0.0`을 사용한다. `Pass3_Bous.wgsl:184,188`은 주기경계의 가장 가까운 내부 셀에서 분산 소스를 추가로 끈다. 이 표지는 순간적인 실제 습건 판정과 다르다. `BoundaryPass.wgsl:669–673`은 현재 수심으로 순간 습건을 따로 판정한다.

#### Q9. 추가 경계와 파 입력

`shaders/BoundaryPass.wgsl:175–180`:

```wgsl
    if (globals.incident_wave_type == 2){ // transient pulse
        num_waves = 5;
        if (eta < 0.0) {
            eta = eta * globals.trough_factor;
        }
        eta = eta * max(0.0, min(1.0, ((f32(num_waves) * period - t)/(period))));
```

`shaders/BoundaryPass.wgsl:517–522`:

```wgsl
    if (globals.west_boundary_type == 5 && idx.x <= 2) {
        let coordinate = BoundaryTimeSeriesYCoordinate(idx);
        BCState = BoundaryTimeSeriesState(2, coordinate, globals.ts_num_points_west);
        BCState_Sed = zero;
        BCState_Breaking = zero;
    }
```

주기 경계 조건은 `BoundaryPass.wgsl:299,313,327,341`의 네 `*_boundary_type == 3`이다. 하천 조건은 `:578,593,605`의 서·동·북 `*_boundary_type == 4`이다. 남쪽 type 4 구현은 이 열거에 없다. 입사 조건은 `:448,465,482,499`의 `*_boundary_type == 2`이다. 고립파는 그 안의 `incident_wave_type == 3`에서 선택한다.

`js/Wave_Generator.js:10–19`의 TMA 계수 원문:

```js
const TMA_SPECTRAL_COEFFICIENTS = Object.freeze({
    gammaS: 3.3,
    spreadO: 50.0,
    directionStepDegrees: 5.0,
    directionalHalfRangeDegrees: 20.0,
    truncationRatio: 0.01,
    gravity: 9.81,
    frequencyCount: 100,
    frequencyStartFactor: 1.0 / 3.0,
    frequencyEndFactor: 3.0
```

이 코드에 대한 2017년 대응식은 없다. TMA 외부 이론의 계수를 역으로 검증하는 일은 이 2017년 논문 대조의 범위가 아니다.

#### Q10. 현재 쇄파 문턱·강도·점성의 원문

`shaders/Pass_Breaking.wgsl:100–125`:

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

이 패스는 `js/main.js:2652–2654`와 `:2786–2788`의 `if(calc_constants.useBreakingModel == 1)`에서 호출된다. Boussinesq의 운동량 소스 소비는 `Pass3_Bous.wgsl:343–364`이다. NLSW의 운동량 소스 제외는 `Pass3_NLSW.wgsl:216–219,248`이다.

#### Q11. 화면 파일과 자료 계약의 확인 범위

`rg -n 'nlsw-select|courant-input|isManning-select|friction-input'`를 지정된 HTML 다섯 파일에서 실행했다. 본판 `index.html:1381–1417`, `index_nots.html:1279–1315`, `river.html:1253–1289`, `MC_examples.html:1252–1288`에서 해당 UI 항목이 검색되었다. `index_headless.html`에서는 이 검색어가 일치하지 않았다.

`index_headless.html:50`은 `<input type="file" id="configFile" accept="application/json" />`이다. `:59`는 `<button id="start-simulation-btn">Start Simulation</button>`이다. `:112`는 `<script type="module" src="js/main.js"></script>`이다. `index_nots.html:1486`과 `MC_examples.html:1468`도 같은 main 모듈을 불러온다. 이 확인은 브라우저 실행을 포함하지 않는다.

계산 셰이더 목록에 `shaders/Ship_pressure.compute`가 있다. 현재 `main.js`의 fetch 목록은 이 파일을 선택하지 않는다. 압력 소스의 실제 입력은 `txBoundaryForcing`이다. 따라서 이 외부 언어 파일의 내부를 논문 전체 대조의 완료 조건으로 삼지 않는다.

#### Q12. 1D 단면판의 식·호스트 대응

아래는 논문의 2DH 식을 현재 단면판에 그대로 적용하지 않기 위한 대조이다. E 후보인 CP1-128과 1D화 자체를 구분한다.

| 논문 항목 | 단면판 원문·위치 | 대조 결과 |
|---|---|---|
| 식 (1)·(4)·(9) 연속식과 KP07 단계 | `transect_version/shaders/Pass2.wgsl:128–132`의 x 플럭스는 질량·x 운동량·0·스칼라 네 성분이다. `Pass3_Bous.wgsl:389`은 `let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + source_term;`이다. | y 발산을 제거한다. $Q$ 방향 수송은 풀지 않는다. |
| 식 (10)–(13) 분산항 | `transect_version/shaders/Pass3_Bous.wgsl:286–287`의 CP1-128 원문과 `:393` `let F_G_here = vec4<f32>(0.0, 0.0, 0.0, 0.0);` | 교차 F*·G*를 0으로 둔다. 남는 순수 x 경사항의 미사용은 별도 E 후보이다. |
| 식 (14) 역수 | `transect_version/shaders/Pass1.wgsl:152–154`은 `let h2 = h * h;`, `let epsilon_c = max(vec4<f32>(globals.epsilon), dB_max);`, `let divide_by_h = 2.0 * h / (h2 + max(h2, epsilon_c));` 뒤의 현재 코드 주석이다. | 본판과 같은 h² 기반 정칙화를 사용한다. 북·남 면은 0으로 둔다. |
| 식 (15)–(20) 시간 적분 | `transect_version/shaders/Pass3_Bous.wgsl:400,405`는 본판과 같은 AB3·AM4 계수이다. `transect_version/js/constants_load_calc.js:25`의 기본 `timeScheme: 2`이다. | 교차 시간 미분은 제거한다. 계수의 이름과 원문 시간 증분의 차이는 본판과 구분한다. |
| 식 (21)–(23) 계수·풀이 | `transect_version/shaders/Update_TriDiag_coef.wgsl:67–69`는 Q4의 x 계수와 같다. `:108`은 `textureStore(coefMatx, idx, coefx);`이다. y 계수 출력 `:109`는 주석이다. `transect_version/js/Run_Tridiag_Solver.js:41`은 `for (let p = 0; p < calc_constants.Px; p++) {`이다. y 풀이 `:60–75`는 주석이다. | x 선형계만 푼다. 이 판은 계수 copy-back을 유지한다. 본판 V7의 새 ping-pong을 단면판에 자동 적용하지 않는다. |
| 습건 지형 창 | `transect_version/shaders/Update_neardry.wgsl:28` `let idx_C = vec2<i32>(xC, idx.y);`; `:49` `if(B_west < 0.0 && B_east < 0.0) {` | 표지 갱신 창과 단일 육상점 검사는 x 행에 한정한다. 암시 계수 gate 자체는 CP1-167의 국소 d이다. |
| 식 (24)–(30) 경계·조파 | `transect_version/shaders/BoundaryPass.wgsl:87,93`의 서·동 감쇠식은 본판과 같은 추가 0.5·지수 0.005를 갖는다. `:175–176`은 `let B_here = textureLoad(txBottom, idx, 0).b;`와 `let d_here = max(0.0, -B_here);`이다. | 서·동 경계와 행별 파 입력을 사용한다. 본판과 파 입력 수심·transient 파 개수가 다르다. |
| 식 (31)–(36) 마찰·고립파 | `transect_version/shaders/Pass3_Bous.wgsl:295` `var friction_ = FrictionCalc(in_state_here.y, 0.0, h_here, friction_here);`; `transect_version/shaders/BoundaryPass.wgsl:127` `let yloc = 0.0;` | 마찰의 횡방향 운동량 인수와 고립파 y 위치를 0으로 둔다. 본판 2DH 입사각 자유도와 구분한다. |
| 호스트 파생값 | `transect_version/js/constants_load_calc.js:358` `calc_constants.dt = calc_constants.Courant_num * Math.min(calc_constants.dx,calc_constants.dy) / Math.sqrt(calc_constants.g * calc_constants.base_depth);`; `:371–372`의 delta·epsilon 식 | 단면판도 별도 JS 기본값·파생값을 가진다. 본판의 구면 강제·type 5 추가를 자동 승계하지 않는다. |

## 4 노트 대조와 수정안

이 절은 지정된 현재 노트의 관련 문장만 대조한다. 노트 원문은 이 파일 작성 시점의 위키 파일에서 `nl -ba`로 확인했다. 이 절의 수정안은 적용하지 않았다. `일치` 행에는 유지할 서술을 적는다. 같은 오류가 여러 노트에 있으면 파일별로 행을 나눈다.

### 4.1 판·시간 적분·계수 설명

| 행 ID | 노트 파일:줄·원문 | 대조 근거 | 판정 | 노트 수정안 |
|---|---|---|---|---|
| CP1-136 | `models/Celeris/README.md:14` `- **원판**: C#/HLSL, **Direct3D** GPU (Windows), 최소 준비로 실행` | Tavakkol 2017 p.1 `Programming language: C++, HLSL`; Tavakkol 2020 p.1 `Programming language: C#, HLSL` | 불일치 | B. “2017년 Celeris Advent는 C++·HLSL과 Direct3D를 사용한다. 2020년 Celeris Base는 Unity3D와 C#·HLSL을 사용한다. 현재 저장소는 JavaScript·WGSL과 WebGPU를 사용한다.” |
| CP1-137 | `models/Celeris/README.md:18` `- **수치 기법**: **확장(extended) Boussinesq 방정식**, **hybrid finite-volume / finite-difference**, GPU 병렬(Direct3D → WebGPU). 시간적분 3rd-order Adams-Bashforth(adaptive, Tavakkol-Lynett 2019)` | `js/constants_load_calc.js:486`의 dt 식; `Pass3_Bous.wgsl:404,409`; 2017 p.3 §2.3 | 불일치 | B. “현 표준 경로는 AB3 예측과 선택적 AM4 보정을 사용한다. dt는 Courant 수·격자 간격·특성수심에서 계산한다. 이 구현을 2019년 논문의 적응 시간 적분 구현이라고 단정하지 않는다.” 2019년 논문 자체의 평가는 이 작업 밖이다. |
| CP1-138 | `models/Celeris/source-analysis/celeris-source-map.md:42` `- **시간적분 (3rd-order Adams-Bashforth predictor-corrector)**`; `:45`의 `AM4 (AB-Moulton)` | Tavakkol 2017 p.3의 `Adams–Moulton`; `Pass3_Bous.wgsl:409` | 불일치 | B. 제목은 “AB3 예측·AM4 보정”으로 쓴다. `AB-Moulton`은 `Adams–Moulton`으로 고친다. 한 번 보정과 교차항 시간 이산화의 판 차이도 덧붙인다. |
| CP1-139 | `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:191` `\| \`timeScheme\` \| 2 \| 0=Euler, 1=AB3 predictor, 2=AB4 pred+corr \|` | `Pass3_Bous.wgsl:404,409`의 AB3·AM4 계수 | 불일치 | B. “0=Euler, 1=AB3 예측, 2=AB3 예측+AM4 한 번 보정”으로 쓴다. 첫 두 단계 Euler 자동 전환은 현재 코드에 없다고 쓴다. |
| CP1-140 | `models/Celeris/manual-notes/celeris-architecture-and-config.md:183`의 `암시적 분산 솔브의 삼중대각=**PCR(Parallel Cyclic Reduction)**`를 2017년 논문 행에 둔다. | Tavakkol 2017 p.6–7 `forward reduction and backward substitution`; Fig. 4; 현 `TriDiag_PCRx.wgsl:89–105` | 불일치 | B. “2017년 논문은 CR 전진 축소·후진 대입을 설명한다. 현재 WebGPU 구현은 후진 대입 없는 PCR을 사용한다.” 상류 `docs/architecture/REFERENCE_PAPERS.md:24`도 같은 구분이 필요하다. |
| CP1-141 | `models/Celeris/source-analysis/celeris-boussinesq-solver.md:79` `\`Bcoef\`는 Boussinesq 분산 보정 계수(Nwogu류 α 관련).` | 2017 p.2 $B=1/15$; `constants_load_calc.js:37–38`의 서로 다른 `Bcoef`,`Bous_alpha` | 불일치 | B. “모드 1의 `Bcoef=1/15`는 Madsen–Sørensen형 분산계수 B이다. 모드 2의 `Bous_alpha=-0.531`과 구분한다.” |
| CP1-142 | `models/Celeris/source-analysis/celeris-boussinesq-solver.md:90` `(y는 대칭, \`:285-286\`).` | CP1-023의 `Pass3_Bous.wgsl:285` 전체 식 | 불일치 | B. “현재 `Psi1y` 혼합 미분의 분모는 x 방향과 축 교환 대칭이 아니다. `dx!=dy`에서 계수가 달라지는 코드 결함 후보이다.” 코드를 임의로 바로잡아 전사하지 않는다. |
| CP1-143 | `models/Celeris/source-analysis/celeris-boussinesq-solver.md:111` `방향분리(ADI류): x행마다 한 tridiagonal, y열마다 한 tridiagonal.` | 2017 p.3 식 (21)·(22); `TriDiag_PCRx.wgsl:70`과 `TriDiag_PCRy.wgsl:70`의 서로 다른 운동량 RHS | 불일치 | F. “x 행에서는 P를 U*로부터 푼다. y 열에서는 Q를 V*로부터 푼다. 두 운동량의 방향별 선형계를 순서대로 호출한다.” 같은 미지수에 x·y 연산자를 교대로 적용하는 ADI와 혼동을 피하도록 표현을 구체화한다. |

### 4.2 재구성·쇄파·경계

| 행 ID | 노트 파일:줄·원문 | 대조 근거 | 판정 | 노트 수정안 |
|---|---|---|---|---|
| CP1-144 | `models/Celeris/source-analysis/celeris-fv-reconstruction.md:58` `한계: θ→1(중심차)와 θ→2(완전 upwind 최소소산) 사이를 보간.` | `constants_load_calc.js:45`의 `1.0 most dissipative(upwind) to 2.0 least dissipative(centered).`; Q2 재구성 식 | 불일치 | B. “θ=1은 더 강하게 제한한다. θ=2는 덜 제한한다. 같은 부호의 세 차분 중 θ를 곱한 두 항과 중심 항의 최솟값을 사용한다.” 원문의 θ 방향을 뒤집어 고친다. |
| CP1-145 | `models/Celeris/source-analysis/celeris-fv-reconstruction.md:64` `즉 inundation limit(수심 < base_depth/50) 근처에서 θ를 2(완전 upwind)로 끌어올려 안정화.` | `Pass1.wgsl:118` `let TWO_THETAc = globals.TWO_THETA * rampcoef + 2.0 * (1.0 - rampcoef);  // transition to full upwinding near the shoreline / inundation limit, start transition with a total water depth of base_depth/50.`; `constants_load_calc.js:489` `calc_constants.TWO_THETA = calc_constants.Theta * 2.0;` | 불일치 | B. “rampcoef가 0으로 가면 TWO_THETAc는 2로 간다. 따라서 θ는 1로 간다.” TWO_THETA와 θ를 구분한다. |
| CP1-146 | `models/Celeris/source-analysis/celeris-breaking-boundary.md:20`의 `**Kennedy et al. eddy-viscosity 쇄파 모델**` | 2017 p.4 §2.5의 직접 쇄파 부재; `366ee34`의 쇄파 옵션 추가; 현 `Pass_Breaking.wgsl:98–125` | 일치 | 현재 코드 설명은 유지한다. “이 명시적 쇄파모델은 2017년 Advent의 기능 설명과 다르다. 현재 WebGPU 추가 기능이다.”라는 판 구분을 덧붙인다. |
| CP1-147 | `models/Celeris/source-analysis/celeris-breaking-boundary.md:137`의 `num_waves=4`; `:197`의 `4파 taper` | `bb99fee` 2026-07-02가 4를 5로 바꿈; 현 `BoundaryPass.wgsl:175–180` Q9 | 불일치 | A. “type 2 transient는 `num_waves=5`를 사용한다. 음의 수면에는 `trough_factor`를 곱한다.” 감쇠 함수 종류의 별도 오기는 CP1-166이다. |
| CP1-148 | `models/Celeris/source-analysis/celeris-breaking-boundary.md:209` `이 .w 플래그는 flux 패스(Pass1)가 near-dry 셀에서 보수적 Riemann/재구성을 쓰도록 gate하는 데 쓰인다` | `Pass1.wgsl:116–118`의 현재 수심 램프; `Pass3_Bous.wgsl:159,192`; `Update_TriDiag_coef.wgsl:34,42` | 불일치 | B. “지형 .w 표지는 Pass3_Bous의 분산 소스와 삼중대각 계수를 제한한다. 표준 Pass1은 현재 이웃 수심으로 제한자 램프를 계산한다. Pass2는 txHnear 수심으로 습건 플럭스 분기를 고른다.” |
| CP1-149 | `models/Celeris/source-analysis/celeris-fv-reconstruction.md:125` `정수압항 ... well-balanced 소스항/정수압이 Pass3 또는 reconstruction 단계로 흡수되는 구조` | `Pass3_Bous.wgsl:392`와 `Pass3_NLSW.wgsl:248`의 `-globals.g * h_here * detadx` | 불일치 | C. “정수압 기울기와 바닥 경사 소스는 Pass3의 `-gh∇w`로 합친다.” 현재 행의 위치 미확정을 구체화한다. 이 연속식 변형이 이산 KP07의 보존성·양수성 증명을 대신하지 않는다고 덧붙인다. |
| CP1-150 | `models/Celeris/source-analysis/celeris-boussinesq-solver.md:155` `불확실: ... (1 - aIn·cInLeft - cIn·aInRight) ... 수학적 유도는 코드 밖이다.` | Q4의 PCR 네 식과 아래 제5절 F 유도 | 불일치 | F. “정규화한 현재 행에서 왼쪽 행의 a배와 오른쪽 행의 c배를 빼면 새 대각은 `1-a*cLeft-c*aRight`이다. 그 역수 r로 다시 정규화한다.” 부호 규약의 수학적 동치를 직접 제시한다. |

### 4.3 나머지 지정 노트와 적용 범위

| 행 ID | 노트 파일:줄·원문 | 대조 근거 | 판정 | 노트 수정안 |
|---|---|---|---|---|
| CP1-151 | `models/Celeris/web-refs/celeris-official-resources.md:15` `- **원판**: C#/HLSL Direct3D (Windows), 최소 준비 실행` | Tavakkol 2017 p.1의 C++·HLSL과 Tavakkol 2020 p.1의 C#·HLSL | 불일치 | B. “2017년 Advent: C++·HLSL·Direct3D. 2020년 Base: C#·HLSL·Unity3D.”로 판을 나눈다. |
| CP1-152 | `models/Celeris/web-refs/celeris-lynett-2026.md:59` `\| 원판 \| Tavakkol & Lynett (2017) ... \| C#/HLSL Direct3D (Windows) \| 최초 interactive Boussinesq 플랫폼 \|` | Tavakkol 2017 p.1 `Programming language: C++, HLSL` | 불일치 | B. 2017년 행의 `C#/HLSL`을 `C++/HLSL`로 고친다. 2020년 행과 합치지 않는다. |
| CP1-153 | `models/Celeris/source-analysis/celeris-source-map.md:25` `\| **COULWAVE** ... \| 다층 z-α 그룹핑 텍스처 \| ... \|` | 같은 지정 노트 `celeris-coulwave.md:12`의 `단일층 ... 2층/다층 아님`; `js/main.js:2664–2669`의 보조량 여섯 layer 복사 | 불일치 | B. “단일 reference 고도의 COULWAVE 보조량을 여섯 텍스처 layer에 저장한다.” 수직 물리층과 저장 layer를 구분한다. 2017년 식을 그 여섯 layer의 원식으로 인용하지 않는다. |
| CP1-154 | `models/Celeris/source-analysis/celeris-coulwave.md:24` `Pass1(flux) → Pass2(explicit) → ...` | `Pass1.wgsl:166–169`의 face 상태 출력; `Pass2.wgsl:136–137`의 플럭스 출력; `Pass3_Bous.wgsl:404`의 시간 갱신 | 불일치 | B. “Pass1은 면 상태를 재구성한다. Pass2는 면 수치 플럭스를 계산한다. Pass3는 우변과 시간 적분을 계산한다.” 나머지 COULWAVE 보조 패스 위치는 유지한다. |
| CP1-155 | `models/Celeris/source-analysis/celeris-sediment.md:17` `config \`useSedTransModel == 1\`일 때만 dispatch (default \`0\`, \`constants_load_calc.js:106\`).` | `constants_load_calc.js:106` `useSedTransModel: 0, // sed model on or off [0]`; `js/main.js:2644,2688,2878` | 일치 | 기본 비활성·조건부 호출 서술을 유지한다. “2017년 논문은 이 퇴적물 모듈을 기술하지 않는다.”를 출처 범위에 덧붙인다. |
| CP1-156 | `models/Celeris/source-analysis/celeris-pipeline-graph.md:115` `corrector substep은 \`if (timeScheme==2)\`에서만`; `:137`은 predictor·tridiag 후 F_G 이력 시프트를 적는다. | `js/main.js:2735–2736,2757,2896–2897` | 일치 | 호출 순서 서술은 유지한다. “현 보정은 한 번이다. 논문의 반복 보정·첫 두 단계 Euler·별도 F* 증분과 구분한다.”를 추가한다. 오래된 줄 인용은 이 보고서의 현재 줄을 사용한다. |
| CP1-157 | `models/Celeris/source-analysis/celeris-render.md:11` `본 노트는 **시각화 파이프라인** — 수치 적분(Pass0~3·TriDiag·Breaking·Boundary)을 **전혀 전진시키지 않는다**.` | 2017 p.6의 계산 여러 단계 뒤 렌더 호출; `Config_Pipelines.js:6,22`의 계산·렌더 파이프라인 분리 | 일치 | 표시와 수치 시간 전진의 구분을 유지한다. 2017년 Fig. 5·9·14의 시각화가 현 커널의 물리 검증을 뜻하지 않는다고 덧붙인다. |
| CP1-158 | `models/Celeris/web-refs/celeris-coulwave-theory.md:31` `모드 1 Bous ... Madsen & Sørensen ... B=1/15 ... 정수심 d 기반` | Tavakkol 2017 p.2 §2.1과 $B=1/15$; `constants_load_calc.js:36–38`; `Pass3_Bous.wgsl:181,269–286` | 일치 | 모드 1의 계보 서술을 유지한다. 구체적인 현재 식 차이로 CP1-023·031·055·058을 연결한다. 이 행은 모드 2의 외부 유도 전부를 검증하지 않는다. |
| CP1-159 | `models/Celeris/manual-notes/celeris-architecture-and-config.md:185` `2019 arXiv 1909.04153 ... 적응형 3차 Adams-Bashforth predictor/corrector 시간적분의 학술적 출처` | 2017 p.3은 이미 AB3 예측·AM4 보정을 적는다. 현 `Pass3_Bous.wgsl:404,409`도 고정 계수를 쓴다. | 불일치 | B. “AB3·AM4 계수의 직접 출처는 Tavakkol 2017 p.3 식 (15)–(20)이다. 2019년 적응 시간 적분 논문은 별도 문헌이다. 현재 구현의 적응 시간 적분 채택은 이 자료만으로 단정하지 않는다.” |
| CP1-160 | `models/Celeris/source-analysis/celeris-boussinesq-solver.md:199` `F_G_star history ... 와 gradient history는 매 step rotate된다.` | `js/main.js:2735–2736`과 `:2896–2897`의 서로 다른 시점; `Pass3_Bous.wgsl:283,286` | 불일치 | C. “F_G 이력은 predictor 후에 이동한다. 일반 도함수 이력은 보정 뒤에 이동한다. 현재 분산 시간 미분은 각 호출의 현재 F*와 저장된 oldOld의 차를 2dt로 나눈다.” 두 이력의 시점을 명시한다. |
| CP1-166 | `models/Celeris/source-analysis/celeris-breaking-boundary.md:137`의 `cos-taper로 꺼짐` | `bb99fee^:shaders/BoundaryPass.wgsl:160` `eta = eta * max(0.0, min(1.0, ((f32(num_waves) * period - t)/(period))));`; 현 `:180`도 같은 함수이다. | 불일치 | B. “마지막 한 주기에 선형 감쇠 함수를 곱한다.” 노트 날짜의 4파 코드에도 cosine 감쇠 함수는 없었다. |

## 5 차이 결론

분류별 개수는 아래 최종 행 표의 행 ID를 기준으로 센다. 같은 결함의 식 전체 행과 세부 항 행도 각각 센다. 서로 다른 결함의 개수와 혼동하지 않는다. 일치 행은 최종 차이 표에 다시 싣지 않는다.

### 5.1 판 차이의 공통 원문·git 근거

논문 판의 공통 기준은 Tavakkol 2017 p.1의 온라인 공개일 `13 April 2017`과 `Programming language: C++, HLSL`이다. p.2는 `Celeris Advent`라고 명시한다. Tavakkol 2020 p.1은 `Celeris Base`와 `Unity3D`, `C#` 및 `HLSL` compute shader를 명시한다. Lynett et al. 2026 p.1은 `Celeris-WebGPU (version 1)`과 브라우저·WebGPU를 명시한다. 보조 두 논문은 이 판 식별에 필요한 첫 쪽만 직접 열었다. 두 논문의 전체 식 대조는 이 보고서의 대상이 아니다.

아래 V 번호는 최종 차이 표의 A 행이 재사용하는 판 증거이다. 각 기록은 날짜·HASH·원문 줄을 포함한다. 기존 2017년 C++ 저장소의 이력은 이 WebGPU git 이력에 포함되지 않는다. 따라서 “첫 WebGPU 관찰”은 2017년 코드가 그 날짜에 수정되었다는 뜻이 아니다. 추가·변경된 WebGPU 코드가 논문보다 뒤의 다른 판이라는 근거이다.

| 근거 ID | 커밋·날짜 | 바뀐 줄 또는 해당 판의 원문 |
|---|---|---|
| V1 | `fd57bb7` · 2023-10-09 · `Add files via upload` | 첫 WebGPU 추가에서 `fd57bb7:js/Config_Pipelines.js:7`은 `return device.createComputePipeline({`이다. `:10`은 `module: device.createShaderModule({ code: computeShaderCode }),`이다. `fd57bb7:js/constants_load_calc.js:60–61`은 `loadedConfig = await response.json();`와 `calc_constants = { ...calc_constants, ...loadedConfig };`이다. C++·HLSL·CML 실행물을 JS·WGSL·JSON 구현과 구분할 직접 근거이다. |
| V2 | `69827ba` · 2025-05-18 · `Create README.md` | `69827ba:README.md:82`에 `This project is licensed under the **MIT License**. See the \`LICENSE\` file for details.`를 추가했다. 2017 p.1의 GPL 배포 설명과 다른 판이다. 2020 p.1에도 Base의 `MIT License`가 명시되어 있다. |
| V3 | `6f1272f` · 2023-10-19 · `Add files via upload` | `6f1272f:shaders/Pass3_Bous.wgsl:87` `let near_dry = textureLoad(txBottom, idx, 0).w;`; `:137–138` `let d_here = globals.seaLevel - B_here;`와 `if (near_dry > 0)`이다. 최초 Boussinesq WebGPU 추가부터 near-dry gate를 사용한다. 현재는 `ebca435:shaders/Pass3_Bous.wgsl:181` `let d_here = -B_here;`와 `:192`의 gate를 사용한다. |
| V4 | `ebc98a5` · 2024-03-13 · `Add files via upload` | `Reconstruct_w`와 수심/수면 선택 분기를 제거했다. `ebc98a5:shaders/Pass1.wgsl:105–107`에 `w = vec4<f32>(wzx.y, wwy.y, wzx.x, wwy.x);`, `h = w - B;`, `h = max(h, vec4<f32>(0.0, 0.0, 0.0, 0.0));`를 둔다. 보존적 w 보정이라는 2017년 설명과 현재 clamp를 구분한다. |
| V5 | `fd57bb7` · 2023-10-09 · 첫 WebGPU 속도 정칙화 | `fd57bb7:shaders/Pass1.wgsl:142–143`은 `let h2 = h * h;`와 `let divide_by_h = 2.0 * h / (h2 + max(h2, vec4<f32>(globals.epsilon)));`이다. 2017 식 (14)의 네제곱·근호 함수와 이미 다르다. V4의 커밋이 `epsilon_c`를 추가했다. |
| V6 | `6f1272f` · 2023-10-19 및 `471c581` · 2024-01-04 | `6f1272f:shaders/Pass3_Bous.wgsl:265,269`은 현재와 같은 AB3·AM4 벡터 갱신이다. 별도 $2F^*-3F^*+F^*$ 증분이 없다. 당시 `:218,221`은 교차 시간 미분 앞에 `0.*`를 두었다. `471c581:shaders/Pass3_Bous.wgsl:234,237`은 그 `0.*`를 제거해 시간 미분을 켰다. 변경 후 x 식 원문은 아래 V6a에 인용한다. |
| V7 | `6f1272f` · 2023-10-19; `984091f` · 2026-05-24 | `6f1272f:shaders/TriDiag_PCRx.wgsl:85–88`은 Q4와 같은 `r,aOut,cOut,dOut` 네 식이다. WebGPU 첫 Boussinesq 추가부터 PCR이다. `984091f` 메시지는 `Markdown and PCR ping-pong updates`이며 계수 copy를 주석 처리하고 `BaseToA`·`BToA` 선택을 추가했다. 현 `ebca435:js/Run_Tridiag_Solver.js:57,82`가 그 선택이다. 이 커밋은 CR에서 PCR로 처음 전환한 날짜가 아니다. |
| V8 | `6f1272f` · 2023-10-19; `4766ac1` · 2025-01-25 | `6f1272f:shaders/BoundaryPass.wgsl:91`은 `let eta = amplitude * sin(omega * t - kx - ky + phase) * min(1.0, t / period);`이다. `:92`는 `let speed = globals.boundary_g * eta / (c * k) * tanh(k * d);`이다. `4766ac1`은 `modulate the location of the origin slowly in time to reduce the Hs finger effect` 주석과 x·y 원점 이동을 추가했다. |
| V9 | `fd57bb7` · 2023-10-09 · 첫 흡수층 WebGPU 코드 | `fd57bb7:shaders/BoundaryPass.wgsl:56`의 원문은 아래 V9a에 인용한다. 코사인에 추가 0.5와 지수 0.01이 이미 있다. 현재 지수는 0.005이다. 따라서 2017 식 (30)의 계수를 현재 감쇠식으로 직접 인용할 수 없다. |
| V10 | `366ee34` · 2024-04-08 · `photorealism update` | `js/constants_load_calc.js`의 diff가 `useBreakingModel: 1`, `delta_breaking: 2.0`, `T_star_coef: 5.0`, `dzdt_I_coef: 0.50`, `dzdt_F_coef: 0.15`를 추가했다. 같은 커밋이 Boussinesq 소스에 `breaking_x`,`breaking_y`를 추가했다. 현재 기본값은 `ebca435:js/constants_load_calc.js:56–60`이다. |
| V11 | `366ee34` · 2024-04-08 · 마찰 정밀도 변경 | `366ee34:shaders/Pass3_Bous.wgsl:62–66`은 단정도와 작은 수심 마찰 과소를 설명한다. `:67–72`가 `h_scaled`, `h4`, `divide_by_h2`, `1. / max(h, globals.delta)`를 추가한 판이다. 현 Q5의 처리로 이어진다. |
| V12 | `040cfdf` · 2024-06-07 · `write write update` | `040cfdf:shaders/AddDisturbance.wgsl:31–32`는 `let P = sqrt(1.0 + 0.5 * amplitude / depth) * eta * c * cos(angle);`와 `let Q = sqrt(1.0 + 0.5 * amplitude / depth) * eta * c * sin(angle);`이다. 바로 이전 두 줄은 `eta * c * cos(angle)`, `eta * c * sin(angle)`였으며 이 커밋이 제곱근 계수를 추가했다. |
| V13 | `fd57bb7` · 2023-10-09 · 초기 설정 체계 | `fd57bb7:js/constants_load_calc.js:5–6`은 WIDTH 800·HEIGHT 600이다. `:18`은 `NLSW_or_Bous: 0,  // Choose 0 for Non-linear Shallow Water (NLSW) or 1 for Boussinesq.`이다. `:74`는 `calc_constants.dt = calc_constants.Courant_num * calc_constants.dx / Math.sqrt(calc_constants.g * calc_constants.base_depth);`이다. `:87`은 `calc_constants.epsilon = Math.pow(calc_constants.base_depth / 1000.0, 2);`이다. CML의 길이·시간·epsilon·보정 반복 태그를 그대로 읽는 구현이 아니다. 현재 파생식은 CP1-068·119이다. |
| V14 | `32be94a` · 2025-10-16 · `hot start initial condition option added` | `32be94a:js/constants_load_calc.js:42` `loadetaIC: 0,  // Load initial free surface from file when == 1`을 추가했다. `js/main.js` diff가 `loadInitCondSurface`와 flag 1 호출을 추가했다. 현재 `ebca435:js/main.js:616–619` Q6가 동일한 수면 전용 경로이다. |
| V15 | `cf9de63` · 2023-10-24 · `Add files via upload` | `cf9de63:js/File_Writer.js:74` `const blob = new Blob([data.buffer], { type: 'application/octet-stream' }); // or another MIME type as appropriate`를 추가했다. 현재 전체장 writer는 `ebca435:js/File_Writer.js:531–604`이며 이진값과 텍스트 메타데이터를 나눈다. |
| V16 | `fd57bb7` · 2023-10-09 및 `471c581` · 2024-01-04 | `fd57bb7:shaders/Pass1.wgsl:134–136`은 상태 w(alpha)의 `hcwy`,`hczx`,`hc` 재구성이다. `471c581`은 `txContSource`와 `clearConc`를 더했다. 현재 alpha 거품·오염물질 사용은 `ebca435:shaders/Pass3_Bous.wgsl:412–424`이다. |
| V17 | `bb99fee` · 2026-07-02 · `Added grid nesting` | `BoundaryPass.wgsl` diff는 `num_waves = 4;`를 `num_waves = 5;`로 바꾸고 `trough_factor`를 추가했다. `bb99fee:shaders/BoundaryPass.wgsl:175–181`은 Q9의 현재 조건과 같다. 그 전 판 `bb99fee^:shaders/BoundaryPass.wgsl:160`도 선형 taper를 썼다. |

V6a. `471c581:shaders/Pass3_Bous.wgsl:234`:

```wgsl
        Psi2x = globals.Bcoef_g * d2_here * (dd_by_dx * (2.0 * eta_by_dx_dx + eta_by_dy_dy) + dd_by_dy * eta_by_dx_dy) + (F_star - F_G_star_oldOldies.y) / globals.dt * 0.5;
```

V9a. `fd57bb7:shaders/BoundaryPass.wgsl:56`:

```wgsl
    let gamma = pow(0.5 * (0.5 + 0.5 * cos(globals.PI * (globals.BoundaryWidth - f32(idx.x) + 2.0) / (globals.BoundaryWidth - 1.0))), 0.01);
```

### 5.2 E의 반대 근거·호출 경로와 F의 식 변형

**E1: CP1-022·023.** 먼저 `git log --follow -p -- shaders/Pass3_Bous.wgsl`에서 `Psi1y`의 변경을 확인했다. `6f1272f:shaders/Pass3_Bous.wgsl:220`의 최초 Boussinesq WebGPU 추가부터 혼합 분모가 `globals.one_over_dx * globals.one_over_d2x`이다. `471c581:shaders/Pass3_Bous.wgsl:236`도 그 분모를 유지한다. `git log -S'one_over_dy * globals.one_over_d2x' -- shaders/Pass3_Bous.wgsl`은 결과가 없었다. 의도 변경·보정 메시지를 찾으려고 커밋 메시지에서 `Psi1y|anisotrop|mixed derivative|transect|slope term`을 검색했다. transect 관련 변경은 나왔지만 본판의 이 분모를 설명하는 메시지는 없었다.

반대 근거는 1D transect에서 y 항을 주석 처리했다는 사실이다. `transect_version/shaders/Pass3_Bous.wgsl:289`의 `Psi1y`는 현재 실행 경로에서 호출되지 않는 식이다. 이 사실은 본판의 y 분산항을 보정하지 않는다. 본판은 `js/main.js:1564`에서 `Pass3_Bous.wgsl`을 불러온다. `NLSW_or_Bous>0`의 Pass3 호출은 `:2678–2679`와 `:2811–2812`이다. COULWAVE 선택이면 `:1570`이 별도 셰이더로 바꾼다. 따라서 E1은 모드 1의 `near_dry>0`·주기경계 가드 밖 경로에 적용된다.

독립 모순은 두 가지이다. 첫째, 본판 x 경로 `Pass3_Bous.wgsl:282`는 x·yy 혼합 차분에 $1/(2\Delta x\Delta y^2)$를 사용한다. y 경로의 x·x·y 분자와 현재 분모 $1/(2\Delta x^3)$는 축 교환 대칭을 깨뜨린다. 둘째, 현재 노트 `celeris-boussinesq-solver.md:90`은 이 y 경로를 `y는 대칭`이라고 적는다. 원문의 식 (11)도 $\eta_{xxy}$를 요구한다. 해석: 시험 다항식 $\eta=x^2y$에서 두 번째 분자는 $4\Delta x^2\Delta y$이다. 현 코드가 계산하는 혼합 미분은 $2\Delta y/\Delta x$이다. 정확한 혼합 미분은 2이다. 이는 모델을 실행하지 않고 stencil을 대수적으로 평가한 결과이다. 근거 강도는 **강함**이다. 수치 실행·물리 오차의 크기는 확인하지 않았다.

**E2: CP1-128.** 먼저 `git log --follow -p -- transect_version/shaders/Pass3_Bous.wgsl`과 `git log -S'Psi2x' -- transect_version/shaders/Pass3_Bous.wgsl`을 확인했다. `22e1983`(2025-06-06, `Sediment transport updates and transect model beta`)가 이 파일을 추가했다. 이 판의 `:287`은 `Psi2x = globals.Bcoef_g * d2_here * (dd_by_dx * (2.0 * eta_by_dx_dx));`이다. `:386`은 현재와 같이 소스에 `(Psi1x)`만 넣는다. 메시지는 beta임을 밝히고 퇴적물 강건성을 언급한다. 이 $d_x\eta_{xx}$ 항을 제거해야 한다는 수학적 설명은 없다.

반대 근거는 1D화가 교차 시간 미분·y 미분을 의도적으로 제거했다는 사실이다. 이 파일 `:271–284,289–290`은 그러한 항을 주석 처리한다. `transect_version/shaders/Pass3_COULWAVE.wgsl:389–390`도 교차 시간 미분을 주석 처리하고 `Psi2x=0`을 둔다. 그러나 Madsen형 순수 x 경사항 $2Bgd^2d_x\eta_{xx}$는 1D에서도 남는다. 그것을 계산한 뒤 사용하지 않는 사실은 이 반대 근거로 설명되지 않는다.

독립 모순은 자기 파일 `:385`의 주석 소스식 `(Psi1x + Psi2x)` 및 본판 `Pass3_Bous.wgsl:392`의 실행 소스식이다. 호출 근거는 `transect_version/js/main.js:1051–1053`의 모드 1 셰이더 선택이다. 이 후보는 본판의 일반 실행 경로에 적용하지 않는다. 근거 강도는 **중간**이다. `d_x=0` 또는 $\eta_{xx}=0$에서는 생략된 항 자체가 0이다. 지형 경사가 있는 1D 입력에서의 실제 오차는 실행하지 않았다.

**F1: CP1-008·009.** 고정 바닥에서 $w=h+z$이므로 $\partial_x(gh^2/2)+ghz_x=gh(h_x+z_x)=ghw_x$이다. y 방향도 같다. 따라서 운동량 우변의 정수압·지형항은 $-gh\nabla w$로 합칠 수 있다. 또한 논문 식 (1)의 $+\mathbf S$를 우변으로 옮기면 $-\mathbf S$이다. 이 변형은 연속식의 동치이다. 코드와 논문의 서로 다른 정칙화·면 소산·기울기 차분까지 이산적으로 같다는 주장은 하지 않는다.

**F2: CP1-052·060.** $\coth r=1/\tanh r$에서 $\sqrt{\coth r}=1/\sqrt{\tanh r}$를 얻는다. $\operatorname{sech}\xi=1/\cosh\xi$에서 $\operatorname{sech}^2\xi=1/\cosh^2\xi$를 얻는다. 이 두 행은 원문의 함수 표기 해석을 명시한 표기 차이이다. 원문 인쇄를 고쳐 전사하지 않는다.

**F3: CP1-143·150.** 논문 식 (21)은 P에 대한 x 선형계이고 식 (22)는 Q에 대한 y 선형계이다. 방향별 독립 운동량 풀이를 “ADI류” 대신 구체적인 두 선형계로 표현한다. PCR 정규화 행 $a_iX_{i-s}+X_i+c_iX_{i+s}=d_i$에서 왼쪽 행의 $a_i$배와 오른쪽 행의 $c_i$배를 빼면 대각은 $1-a_ic_{i-s}-c_ia_{i+s}$가 된다. 남은 비대각은 $-a_ia_{i-s}$와 $-c_ic_{i+s}$이다. 우변은 $d_i-a_id_{i-s}-c_id_{i+s}$이다. 대각으로 나누면 Q4의 `r,aOut,cOut,dOut`과 같다.

### 5.3 행별 최종 결론 — 판 차이

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| CP1-001 | 언어·GPU API | A 판 차이 | 2017 p.1 `C++, HLSL`; V1 `fd57bb7:js/Config_Pipelines.js:7` `return device.createComputePipeline({` | 2017년 Advent의 C++·HLSL·Direct3D와 현재 JS·WGSL·WebGPU를 구분한다. |
| CP1-002 | 배포 라이선스 설명 | A 판 차이 | 2017 p.1 `GNU General Public License 3 (GPL)`; V2 `69827ba:README.md:82`의 `MIT License` | 논문의 GPL 배포 설명은 2017년 Advent에 한정한다. |
| CP1-014 | 육상 분산 정지 | A 판 차이 | 2017 p.2 `we set d = 0`; V3 `6f1272f:shaders/Pass3_Bous.wgsl:138` `if (near_dry > 0)` | 현재 표준 경로는 육상 인접 창에서 분산항과 암시 계수를 끈다. |
| CP1-028 | 양수 수심 처리 | A 판 차이 | 2017 p.3 `conservative correction ... on w`; V4 `ebc98a5:shaders/Pass1.wgsl:107` `h = max(h, vec4<f32>(0.0, 0.0, 0.0, 0.0));` | 현 구현은 재구성 면 수심을 0 이상으로 자른다. |
| CP1-029 | 면 속도 정칙화 | A 판 차이 | 2017 p.3 식 (14); V5 `fd57bb7:shaders/Pass1.wgsl:143`의 `2.0 * h / (h2 + max(h2, vec4<f32>(globals.epsilon)))` | 현재 속도 역수는 논문 식 (14)의 네제곱·근호 함수와 다르다. |
| CP1-031 | 교차 분산 시간 미분 | A 판 차이 | V6 `471c581:shaders/Pass3_Bous.wgsl:234` V6a 전체 식; 2017 p.3 식 (16)–(20) | 현재 F*·G* 시간 미분은 우변 도함수에 포함되어 AB·AM 가중을 받는다. |
| CP1-033 | 식 (16) 전체 | A 판 차이 | 2017 p.3 식 (16)의 $2F^{*n}-3F^{*n-1}+F^{*n-2}$; V6 `6f1272f:shaders/Pass3_Bous.wgsl:265`의 AB3 벡터 갱신 | x 운동량 예측식 전체를 논문 식 (16)과 동일하다고 쓰지 않는다. |
| CP1-034 | 식 (17) 전체 | A 판 차이 | 2017 p.3 식 (17)의 $2G^{*n}-3G^{*n-1}+G^{*n-2}$; V6 | y 운동량 예측식도 별도 교차항 증분을 사용하지 않는다. |
| CP1-036 | 식 (19) 전체 | A 판 차이 | 2017 p.3 식 (19)의 $F^{*p}-F^{*n}$; V6 `6f1272f:shaders/Pass3_Bous.wgsl:269`의 AM4 벡터 갱신 | x 운동량 보정의 교차항 시간 처리가 논문과 다르다. |
| CP1-037 | 식 (20) 전체 | A 판 차이 | 2017 p.3 식 (20)의 $G^{*p}-G^{*n}$; V6 | y 운동량 보정의 교차항 시간 처리도 논문과 다르다. |
| CP1-039 | 반복 보정 | A 판 차이 | 2017 p.3 `until the variables converge`; V1의 WebGPU 호스트와 V6의 시간 분기; 현 `js/main.js:2757` `if (calc_constants.timeScheme == 2)` | 현재 호스트는 선택한 보정 단계를 한 번 호출한다. |
| CP1-040 | 시작 두 단계 Euler | A 판 차이 | 2017 p.3 `for those two steps`; V6 `6f1272f:shaders/Pass3_Bous.wgsl:261` `if (globals.timeScheme == 0) {` | 현재 첫 두 단계의 Euler 자동 전환은 구현되어 있지 않다. |
| CP1-044 | CR과 PCR | A 판 차이 | 2017 p.6 `backward substitution`; V7 `6f1272f:shaders/TriDiag_PCRx.wgsl:85` `let r = 1.0 / (1.0 - aIn * cInLeft - cIn * aInRight);` | 현재 PCR은 별도 후진 대입을 사용하지 않는다. |
| CP1-048 | 정현파 수면 식 | A 판 차이 | 2017 p.4 식 (25); V8 `6f1272f:shaders/BoundaryPass.wgsl:91`의 phase·램프 | 현재 파 입력은 위상·램프·원점 이동을 포함한다. |
| CP1-049 | 정현파 P 식 | A 판 차이 | 2017 p.4 식 (26); V8 `6f1272f:shaders/BoundaryPass.wgsl:92` `let speed = globals.boundary_g * eta / (c * k) * tanh(k * d);` | 현재 P 계수와 cη의 동치는 정확한 분산관계에서만 성립한다. |
| CP1-050 | 정현파 Q 식 | A 판 차이 | 2017 p.4 식 (27); V8의 `speed`; 현 `BoundaryPass.wgsl:185` `let hv = speed * sin(theta_mod);` | 현재 Q도 같은 분산관계 근사의 영향을 받는다. |
| CP1-054 | 흡수층 계수 | A 판 차이 | 2017 p.4 식 (30); V9 `fd57bb7:shaders/BoundaryPass.wgsl:56` V9a | 현재 감쇠계수의 추가 0.5·지수·격자 위치를 그대로 적는다. |
| CP1-055 | 직접 쇄파 처리 | A 판 차이 | 2017 p.8 `does not employ an explicit wave-breaking model`; V10의 `useBreakingModel: 1` 추가 | 현재 표준 Boussinesq에는 명시적 점성 쇄파모델이 있다. |
| CP1-058 | 마찰의 작은 수심 처리 | A 판 차이 | 2017 p.4 `same technique as in Eq. (14)`; V11 `366ee34:shaders/Pass3_Bous.wgsl:67` `let h_scaled = h / globals.base_depth;` | 현재 마찰 정칙화는 특성수심으로 스케일한 네제곱 임계를 쓴다. |
| CP1-061 | 고립파 운동량 | A 판 차이 | 2017 p.4 식 (34); V12 `040cfdf:shaders/AddDisturbance.wgsl:31–32`의 제곱근 계수 추가 | 현재 고립파 운동량은 $\sqrt{1+H_s/(2d)}$를 추가로 곱한다. |
| CP1-066 | CML·XML 입력 | A 판 차이 | 2017 p.5 `we use CML`; V1 `fd57bb7:js/constants_load_calc.js:60` `loadedConfig = await response.json();` | 현 설정 입력은 CML이 아니라 JSON이다. |
| CP1-067 | 모델 선택 키 | A 판 차이 | 2017 p.5 Fig. 2 `type = "BSNQ"`; V13 `fd57bb7:js/constants_load_calc.js:18`의 `NLSW_or_Bous: 0` | CML BSNQ 예제와 현 NLSW_or_Bous 값을 구분한다. |
| CP1-068 | epsilon·dt·보정 횟수 | A 판 차이 | Fig. 2 `epsilon = 5e-12 correctionStepsNum = 2 timestep = 0.005`; V13의 `:74,87` 파생식 | 현재 dt·epsilon은 파생값이며 timeScheme 2는 반복 횟수가 아니다. |
| CP1-069 | 마찰 선택 키 | A 판 차이 | Fig. 2 `type = "Manning" coef = 0.0`; V13 `fd57bb7:js/constants_load_calc.js:27`의 `isManning: 1`; 현 `:47`의 `isManning: 0` | 예제의 마찰 선택과 현재 기본 마찰 선택을 구분한다. |
| CP1-070 | 영역·격자·정수위 키 | A 판 차이 | Fig. 2 `stillWaterElevation = 0`; V13의 WIDTH·HEIGHT·dx; 현 `constants_load_calc.js:43`의 `no longer used` | 현 입력은 셀 수·격자 간격을 사용하며 seaLevel은 활성 수위 이동 옵션이 아니다. |
| CP1-071 | 지형 경로 형식 | A 판 차이 | Fig. 2 `bathymetryFilePath`; V1 JSON 기반 입력; 현 `File_Loader.js:17` `filePath = calc_constants.exampleDirs[calc_constants.run_example] + 'bathy.txt';` | 지형 텍스트 격자는 업로드 내용 또는 예제 경로에서 읽는다. |
| CP1-072 | 전체 상태 hot start | A 판 차이 | 2017 p.5 `w, P, and Q`; V14 `32be94a:js/constants_load_calc.js:42`의 `loadetaIC: 0` 추가 | 현 수면 전용 초기조건 호출을 전체 상태 hot start로 설명하지 않는다. |
| CP1-073 | 복수 고립파 CML 목록 | A 판 차이 | Fig. 2의 두 `<solitaryWave>`; V1의 JSON 구현과 V12의 단일 교란 함수; 현 `AddDisturbance.wgsl:235` `let state_out = in_state_here + disturbance;` | 현 위치·방향·진폭 교란을 CML 목록 파싱과 구분한다. |
| CP1-074 | 경계 예제의 이름·값 | A 판 차이 | Fig. 2 `widthNum=20`, `amplitude=.01`; V13 설정 객체; 현 `Wave_Generator.js:59`의 `0.5 * waveHeight` | 현재 경계 번호·공통 셀 폭·파고 H와 논문 예제의 진폭 a를 구분한다. |
| CP1-075 | 로그 경로·범위·계측점 | A 판 차이 | Fig. 2 `logStep = 20`, `filename = "island"`; V15 `cf9de63:js/File_Writer.js:74`의 Blob 다운로드 | 현재 출력 파일 다운로드를 CML의 Windows 로그 경로·부분 범위 형식과 구분한다. |
| CP1-076 | ASCII 전체장 출력 | A 판 차이 | 2017 p.6 `formatted ASCII file`; V15의 `application/octet-stream` | 현재 전체장 값은 float32 이진 형식이고 메타데이터는 텍스트이다. |
| CP1-079 | 미사용 alpha | A 판 차이 | 2017 p.6 `a ... unused`; V16 `fd57bb7:shaders/Pass1.wgsl:134–136`의 hc 재구성 | 현재 alpha는 스칼라·거품·오염물질에 사용한다. |
| CP1-080 | 렌더 타깃 계산 | A 판 차이 | 2017 p.6 `render target texture`; V1의 `createComputePipeline`·WGSL storage 출력 | 현재 수치 패스는 여러 storage texture에 쓰는 WebGPU compute pass이다. |
| CP1-081 | 파일 분할·Fig. 1 | A 판 차이 | 2017 p.5 `main.cpp`, `engine.cpp`, `compute.hlsl`; V1 JS 파이프라인 추가 | Fig. 1은 역할의 계보이며 현재 파일 호출 그래프가 아니다. |
| CP1-082 | 빌드·외부 구성 | A 판 차이 | 2017 p.7 `Celeris.sln`, `DirectX SDK`; V1 JS·WGSL 추가 및 현 `ARCHITECTURE.md:3` `no ... build step` | 2017년 C++ 빌드 지침을 현재 브라우저 판에 적용하지 않는다. |
| CP1-083 | 실행물·setting.init | A 판 차이 | 2017 p.7 `Celeris.exe`, `setting.init`; V1 JSON 입력과 현 `index_headless.html:112`의 main 모듈 | 현재 진입점은 HTML과 JavaScript 모듈이다. |
| CP1-086 | 셰이더 수정·재컴파일 | A 판 차이 | 2017 p.4 `compute.hlsl`; V1 `fd57bb7:js/Config_Pipelines.js:10`의 `createShaderModule` | 현재 실행 시 모듈 생성의 대상은 WGSL이며 C++ 재컴파일 절차가 아니다. |
| CP1-147 | transient 파 개수 | A 판 차이 | V17 `bb99fee` 2026-07-02 diff `num_waves = 4;` → `num_waves = 5;`; 현 `BoundaryPass.wgsl:176` | 현재 transient의 num_waves는 5이다. |

### 5.4 행별 최종 결론 — 문서 오기

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| CP1-011 | 식 (3)의 방향 계수 | B 문서 오기 | Tavakkol 2017 p.2 식 (3)의 두 $dd_x$; p.3 식 (11)의 $d_y(2\eta_{yy}+\eta_{xx})+d_x\eta_{xy}$ | 식 (3)의 첫 경사 괄호는 같은 문서의 y 재배열식과 모순한다. |
| CP1-025 | 식 (13)의 함수 인수 | B 문서 오기 | p.3 식 (13) $G^*(Q)$와 P 미분 우변; p.2 식 (6) $G^*(P)$ | 식 (13)의 좌변 인수 Q는 P와 일치하지 않는다. |
| CP1-088 | 작은 파고의 h 무차원화 | B 문서 오기 | p.7 $\Delta x/h$, $\Delta t(g/h)^{0.5}$와 같은 문단의 $\Delta x/d$, $\Delta t(g/d)^{0.5}$ | 작은 파고 설정의 h 표기는 총수심 정의와 일정 격자 설정에 맞지 않는다. |
| CP1-089 | 무차원 길이의 단위 | B 문서 오기 | p.7 $100<L/d<1000\ \mathrm m$ | 무차원 L/d의 상한 뒤 m는 단위 표기 오기이다. |
| CP1-091 | Fig. 7 시간 기호 | B 문서 오기 | p.8 캡션 $t(g/h)^{0.5}$와 패널 $t\sqrt{g/d}$ | Fig. 7의 캡션 h와 패널 d는 서로 다르다. |
| CP1-093 | 식 (37)의 천퇴 부호 | B 문서 오기 | p.8 $(10.67-G-x)/25$의 끝값은 −0.3048이며 다음 인쇄값은 +0.3048이다. | 식 (37)의 가운데 구간 부호는 상승 천퇴 설명과 내부적으로 맞지 않는다. |
| CP1-108 | Fig. 15(c) 파고 | B 문서 오기 | p.11 `0.018 (c)`와 p.9 본문·p.10 Fig. 13·p.11 Fig. 14의 `0.18` | Fig. 15(c)의 0.018은 같은 논문의 가장 큰 파고 0.18과 다르다. |
| CP1-136 | README의 원판 언어 | B 문서 오기 | `models/Celeris/README.md:14` `C#/HLSL`; 2017 p.1 `C++, HLSL` | Advent의 언어는 C++·HLSL이며 Base의 C#·HLSL과 구분한다. |
| CP1-137 | 적응 시간 적분 단정 | B 문서 오기 | README `:18`의 `adaptive`; 현 `constants_load_calc.js:486`의 특성수심 dt 식과 `Pass3_Bous.wgsl:404,409`의 고정 계수 | 현재 코드는 AB3·AM4와 특성수심 기반 dt를 사용한다. |
| CP1-138 | AB3·AM4 이름 | B 문서 오기 | `celeris-source-map.md:42,45`의 `Adams-Bashforth predictor-corrector`, `AB-Moulton`; 2017 p.3 `Adams–Moulton` | 시간 적분을 AB3 예측·AM4 보정으로 명명한다. |
| CP1-139 | AB4 pred+corr | B 문서 오기 | `celeris-webgpu-infrastructure.md:191` `2=AB4 pred+corr`; `Pass3_Bous.wgsl:409`의 `(9,19,-5,1)/24` | timeScheme 2는 AB3 예측과 AM4 한 번 보정이다. |
| CP1-140 | 2017년 CR을 PCR로 서술 | B 문서 오기 | `celeris-architecture-and-config.md:183`의 `PCR`; 2017 p.6 `forward reduction and backward substitution` | 2017년 CR과 현재 PCR을 나누어 적는다. |
| CP1-141 | Bcoef와 Nwogu α | B 문서 오기 | `celeris-boussinesq-solver.md:79` `Nwogu류 α 관련`; `constants_load_calc.js:37–38`의 별도 Bcoef·Bous_alpha | 모드 1의 B=1/15와 모드 2의 α를 구분한다. |
| CP1-142 | y 대칭 단정 | B 문서 오기 | `celeris-boussinesq-solver.md:90` `y는 대칭`; `Pass3_Bous.wgsl:285`의 `one_over_dx * globals.one_over_d2x` | 현재 Psi1y는 축 교환 대칭이 아닌 결함 후보를 포함한다. |
| CP1-144 | θ 방향 | B 문서 오기 | `celeris-fv-reconstruction.md:58` `θ→1(중심차)`; `constants_load_calc.js:45` `1.0 most dissipative(upwind) to 2.0 least dissipative(centered).` | θ=1이 더 제한적이고 θ=2가 덜 제한적이다. |
| CP1-145 | TWO_THETA와 θ | B 문서 오기 | 같은 노트 `:64` `θ를 2 ... 끌어올려`; `Pass1.wgsl:118`의 TWO_THETAc→2 | 얕은 곳에서 TWO_THETAc는 2로 가며 θ는 1로 간다. |
| CP1-148 | near-dry 소비자 | B 문서 오기 | `celeris-breaking-boundary.md:209` `Pass1 ... gate`; `Pass3_Bous.wgsl:159,192`와 `Update_TriDiag_coef.wgsl:34,42` | 지형 .w 표지는 표준 Pass1의 재구성 gate가 아니라 분산 소스·암시 계수의 gate이다. |
| CP1-151 | 공식 자료 노트의 언어 | B 문서 오기 | `celeris-official-resources.md:15` `C#/HLSL`; 2017 p.1 `C++, HLSL` | 공식 자료 노트도 Advent와 Base의 언어를 나누어 적는다. |
| CP1-152 | 2026 노트의 계보 표 | B 문서 오기 | `celeris-lynett-2026.md:59` `C#/HLSL`; 2017 p.1 `C++, HLSL` | 계보 표의 2017년 행은 C++·HLSL이다. |
| CP1-153 | 물리 다층과 텍스처 layer | B 문서 오기 | `celeris-source-map.md:25` `다층 z-α`; `celeris-coulwave.md:12` `단일층 ... 2층/다층 아님` | 여섯 보조량 저장 layer를 수직 다층 모델이라고 부르지 않는다. |
| CP1-154 | Pass1·Pass2 역할 | B 문서 오기 | `celeris-coulwave.md:24` `Pass1(flux) → Pass2(explicit)`; `Pass2.wgsl:136` `textureStore(txXFlux, idx, xflux);` | Pass1은 재구성이고 Pass2는 플럭스이며 Pass3가 시간 갱신이다. |
| CP1-159 | 2019년 단독 출처 연결 | B 문서 오기 | `celeris-architecture-and-config.md:185`의 `적응형 ... 출처`; 2017 p.3 식 (15)–(20) | 현 AB3·AM4 계수의 직접 비교 출처는 2017년 식이다. |
| CP1-165 | 계측점 배치 그림 번호 | B 문서 오기 | p.9 본문 `(Fig. 11)`과 Fig. 10 `gauge locations` | 계측점 배치는 Fig. 10이며 Fig. 11은 시계열이다. |
| CP1-166 | cosine taper 단정 | B 문서 오기 | 노트 `celeris-breaking-boundary.md:137` `cos-taper`; `bb99fee^:shaders/BoundaryPass.wgsl:160`의 선형 max/min 식 | transient 종료 함수는 cosine이 아니라 선형 함수이다. |

### 5.5 행별 최종 결론 — 문서 누락

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| CP1-109 | 제한자 기본값·램프 | C 문서 누락 | `constants_load_calc.js:45`의 `Theta: 2.0`; `Pass1.wgsl:117` `let rampcoef = min(max(0.0, wetdry / (0.02 * globals.base_depth)), 1.0);` | 현재 θ 기본값과 수심 기반 램프는 2017년 설명에 없는 세부 처리이다. |
| CP1-110 | 고차 재구성·플럭스 선택 | C 문서 누락 | `js/main.js:1541,1548`의 `Pass1_HighOrder.wgsl`, `Pass2_HighOrder_HLLC.wgsl`; Q7의 `dh_max > 0.60` | 고차 옵션은 2017년 KP07 설명과 구분한다. |
| CP1-111 | Froude 상한 | C 문서 누락 | `Pass1.wgsl:159` `let Fr_maxallowed = 3.0 / max(1.0, dBds_max);` 뒤의 안정화 주석과 CP1-111 전체 분기 | 경사에 따른 면 속도 상한을 현재 코드 처리로 적는다. |
| CP1-112 | 건조 셀 조기 반환 | C 문서 누락 | `Pass1.wgsl:85–86`의 현재 셀·북동남서 수심 조건; `Pass3_Bous.wgsl:142–143`의 같은 조건 | 현재 셀과 네 이웃이 모두 얕으면 계산을 생략한다. |
| CP1-113 | 바닥차 정칙화 | C 문서 누락 | `Pass1.wgsl:146` `let epsilon_c = max(vec4<f32>(globals.epsilon), dB_max);`; Q2 전체 역수 | 면 속도 정칙화의 임계에 지형 표고차가 들어간다. |
| CP1-114 | 얕은 면 질량 소산 | C 문서 누락 | `Pass2.wgsl:115–119`의 `mass_diff_x = 0.0;`, `mass_diff_y = 0.0;`, `phix = 1.0;`, `phiy = 1.0;` | 얕은 이웃에서 질량 차 소산과 스칼라 소산 계수를 따로 바꾼다. |
| CP1-115 | 지형 창·항등 계수 | C 문서 누락 | `Update_neardry.wgsl:19` `let lengthCheck = 3;`; Q8의 항등행 식 | 육상 인접 창과 경계 행의 분산 계수를 항등행으로 바꾼다. |
| CP1-116 | 습건 후처리 | C 문서 누락 | `BoundaryPass.wgsl:703`의 `sum_dry == 1 && (globals.algochanges == 0 \|\| nearshore <= globals.delta)`; CP1-116의 전체 조건 | 단일 습윤 셀·수로 끝·음수 수심 후처리를 구분해 적는다. |
| CP1-117 | 추가 경계·다성분 입력 | C 문서 누락 | `BoundaryPass.wgsl:276` `return vec4<f32>(mix(space_value0, space_value1, globals.ts_time_alpha), 0.0);`; Q9 | 현 코드의 주기·하천·시계열·다성분 파 입력은 2017년 세 경계 외의 기능이다. |
| CP1-118 | 입력 검사·평탄화 | C 문서 누락 | `File_Loader.js:43` `if (depthValues.length !== calc_constants.WIDTH) {`; `:50` `if (isNaN(parsedValue)) {` | 현재 지형 입력은 열 수와 수치 변환을 검사하고 가장자리를 평탄화한다. |
| CP1-119 | 설정 병합·임계 파생 | C 문서 누락 | `constants_load_calc.js:443` `calc_constants = { ...calc_constants, ...loadedConfig };`; `:501–502`의 delta·epsilon 식 | 현재 기본값·JSON 덮어쓰기·파생값 계산을 나누어 적는다. |
| CP1-120 | 외부 소스·혼합 | C 문서 누락 | `Pass3_Bous.wgsl:314` `let press_x = -0.5 * h_here * globals.g_over_dx * (P_right - P_left);`; `:389`의 침투 소스 | 현재 압력·침투·와도 혼합 소스를 2017년 기본 소스와 구분한다. |
| CP1-121 | 바닥 운동 | C 문서 누락 | `Pass3_Bous.wgsl:306` `let dhdt = textureLoad(txBoundaryForcing, idx, 0).y;`; `AddDisturbance.wgsl:227` `B_here.z = depth_change.z;` | 바닥 변동 경로에는 고정 바닥의 wt=ht 가정을 그대로 적용하지 않는다. |
| CP1-122 | alpha 수송·소스 | C 문서 누락 | `Pass3_Bous.wgsl:336` `let c_dissipation = -globals.whiteWaterDecayRate * C_state_here;`; `:418`의 오염 소스 | 현재 alpha의 이류·확산·감쇠·거품·오염물질 소스를 별도로 기술한다. |
| CP1-123 | 마찰 지도·상한 | C 문서 누락 | `Pass3_Bous.wgsl:302` `let friction_here = max(globals.friction, textureLoad(txBottomFriction, idx, 0).x);`; `:88` `f = min(f, 0.5);` | 마찰 지도는 전역값과 최댓값을 취하고 f 상한을 적용한다. |
| CP1-124 | 고립파 추가 조건 | C 문서 누락 | `AddDisturbance.wgsl:50`의 육상 eta clamp; `BoundaryPass.wgsl:140` `let amplitude = 0.5;` | 초기 고립파 교란과 고정 진폭 경계 고립파를 구분한다. |
| CP1-125 | 구면 제약 | C 문서 누락 | `constants_load_calc.js:456` `console.warn("Spherical grid mode is currently NLSW-only; forcing NLSW_or_Bous to 0.");` | 구면 격자는 NLSW 경로로 제한하며 고차·퇴적물·Cartesian 쇄파를 끈다. |
| CP1-126 | COULWAVE 모드 | C 문서 누락 | `js/main.js:1570` `Pass3_ShaderCode_Bous = await fetchShader('/shaders/Pass3_COULWAVE.wgsl');` | 현재 COULWAVE는 2017년 Madsen형 식과 별도 경로이다. |
| CP1-127 | 퇴적물·지형 변화 | C 문서 누락 | `SedTrans_Pass3.wgsl:215`의 `erosion - deposition`; `SedTrans_UpdateBottom.wgsl:84`의 공극률 분모 | 2017년 논문을 현재 표사 모듈의 식 출처로 쓰지 않는다. |
| CP1-129 | PCR 텍스처 교대 | C 문서 누락 | `Run_Tridiag_Solver.js:57`의 `BaseToA`·`BToA` 선택 전체 식; V7 `984091f` 2026-05-24 | 현재 PCR의 텍스처 교대와 마지막 해 기록을 현 구현 근거로 적는다. |
| CP1-131 | 명시적 쇄파 세부식 | C 문서 누락 | `Pass_Breaking.wgsl:125`의 `min(dx*dy/dt, B*delta_breaking*h*detadt)` 전체 식 Q10; `:129` `let nu_Smag = 0.0;` 뒤의 비활성 주석 | 현 쇄파 나이·문턱·점성 상한을 기술하며 Smagorinsky는 비활성으로 적는다. |
| CP1-132 | NLSW와 Bous 소산 차이 | C 문서 누락 | `Pass3_NLSW.wgsl:216` `breaking dissipation not added for NLSW model`; `Pass3_Bous.wgsl:360–362`의 near-dry 조건 | NLSW의 거품 표시와 Boussinesq의 점성 운동량 소산을 구분한다. |
| CP1-133 | GPU 자료 배치 | C 문서 누락 | `Copy_Data_to_Textures.js:11` `const requiredBytesPerRow = Math.ceil(actualBytesPerRow / 256) * 256;` | CPU→GPU 복사의 행 정렬과 면·바닥 채널 의미를 명시한다. |
| CP1-134 | 통계·출력 후처리 | C 문서 누락 | `js/main.js:2915,2924`의 통계 패스; `scripts/load_WebGPUCeleris_output.m:30`의 `float32` 읽기 | 통계·시계열·이진 출력 후처리를 논문 처오름 분석과 구분한다. |
| CP1-135 | 진입점·선택지 | C 문서 누락 | `index.html:1383–1384`의 NLSW·Boussinesq 선택지; `index_headless.html:112` `<script type="module" src="js/main.js"></script>` | 각 HTML의 UI와 호스트가 지원하는 계산 모드를 구분한다. |
| CP1-149 | 정수압 흡수 위치 | C 문서 누락 | `Pass3_Bous.wgsl:392`의 `-globals.g * h_here * detadx`; `Pass3_NLSW.wgsl:248`도 같다. | 정수압·바닥 경사 결합 위치는 Pass3의 -gh∇w이다. |
| CP1-160 | 분산 이력 시점 | C 문서 누락 | `js/main.js:2735` `runCopyTextures_EncStack(commandEncoderStack, calc_constants, F_G_star_oldGradients, F_G_star_oldOldGradients)`; 일반 이력은 `:2896–2897` | F_G 이력은 예측 뒤에 이동하고 일반 도함수 이력은 보정 뒤에 이동한다. |
| CP1-167 | 독립 x 단면 계산 | C 문서 누락 | `transect_version/shaders/Pass1.wgsl:119` `let wetdry = min(h_here, min(h_west, h_east));`; `Update_TriDiag_coef.wgsl:34`의 `let near_dry = d_here;` | 단면판의 면·분산·삼중대각·습건 처리는 본판 2DH와 나누어 적는다. |
| CP1-168 | 행별 단면 조파 | C 문서 누락 | `transect_version/shaders/BoundaryPass.wgsl:185` `let wave = textureLoad(txWaves_Transect, vec2<i32>(iw, idx.y), 0);`; `:162` `num_waves = 4;` | 단면판은 지역 수심·행별 파 입력·4파 transient를 사용한다. |
| CP1-169 | 동봉 HLSL 선박 압력 | C 문서 누락 | `Ship_pressure.compute:30,80`의 압력·출력 식; `rg -n -F 'Ship_pressure.compute' js/` 0건 | 동봉 HLSL 선박 압력 파일은 현재 실행 경로에서 호출되지 않는다. |

### 5.6 행별 최종 결론 — 코드 결함 후보·표기 차이

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| CP1-022 | 식 (11) 구현의 혼합항 | E 코드 결함 후보·강함 | `Pass3_Bous.wgsl:285`의 `one_over_dx * globals.one_over_d2x`; CP1-023 전체 식·§5.2 E1 | 식 (11)의 η_xxy 계수는 비정방 격자에서 맞지 않는 후보를 포함한다. |
| CP1-023 | Psi1y의 분모 | E 코드 결함 후보·강함 | `6f1272f:shaders/Pass3_Bous.wgsl:220`부터 같은 분모; 현 `:282`의 축 교환 대조; 노트 `:90` `y는 대칭` | 혼합 분자의 x²y 차분은 분모 2dx²dy를 요구하지만 현 코드는 2dx³을 쓴다. |
| CP1-128 | transect의 Psi2x 미사용 | E 코드 결함 후보·중간 | `22e1983:transect_version/shaders/Pass3_Bous.wgsl:287,385–386`; 현 `:287` 계산과 `:386`의 `(Psi1x)` | 1D에서도 남는 바닥 경사 분산항을 계산하고 소스에서 사용하지 않는다. |
| CP1-008 | 정수압 플럭스 분리 | F 표기 차이 | 2017 p.2의 $gh^2/2$; 현 `Pass3_Bous.wgsl:392`의 `-globals.g * h_here * detadx`; §5.2 F1 | 연속식에서는 정수압과 바닥 경사를 -gh∇w로 결합할 수 있다. |
| CP1-009 | 소스 부호 | F 표기 차이 | 2017 p.2 식 (1) $+\mathbf S$; 현 `Pass3_Bous.wgsl:392`의 음의 마찰·기울기 | 좌변 소스를 우변으로 옮긴 부호를 기준으로 비교한다. |
| CP1-052 | Eckart 함수 표기 | F 표기 차이 | 2017 p.4 식 (29)의 $\sqrt{\coth}$; `BoundaryPass.wgsl:129`의 `sqrt(tanh(...))` 분모 전체 식 | 함수값의 제곱근으로 해석하면 coth와 tanh 역수 표현은 같다. |
| CP1-060 | sec h와 cosh 역수 | F 표기 차이 | 2017 p.4 식 (33) `sec h`; `AddDisturbance.wgsl:45`의 cosh 제곱 분모 전체 식 | 원문의 sec h를 hyperbolic secant로 해석한 동치를 명시한다. |
| CP1-143 | 방향별 운동량 풀이 표현 | F 표기 차이 | 2017 p.3 식 (21)·(22)의 서로 다른 P·Q; `TriDiag_PCRx/y.wgsl:70`의 g·b RHS | x에서는 P를 풀고 y에서는 Q를 푼다고 구체적으로 적는다. |
| CP1-150 | PCR 정규화 부호 | F 표기 차이 | `TriDiag_PCRx.wgsl:89` `let r = 1.0 / (1.0 - aIn * cInLeft - cIn * aInRight);`; §5.2 F3 | 두 이웃 행 소거와 대각 재정규화가 이 분모를 만든다. |

### 5.7 행별 최종 결론 — 코드 대조 대상 아님

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| CP1-003 | 실시간·CPU 비교 성능 | H 코드 대조 대상 아님 | 2017 p.1 `faster than real-time`; `dozens to hundreds of CPU cores` | 논문의 성능 주장을 현재 커밋의 측정값으로 쓰지 않는다. |
| CP1-013 | kd 적용성 | H 코드 대조 대상 아님 | p.2 `kd < 3` | kd<3은 방정식의 적용성 주장이고 코드의 자동 입력 제한이 아니다. |
| CP1-059 | Manning 단위 규약 | H 코드 대조 대상 아님 | p.4 `SI units (i.e. m/s² and m respectively)` | g·h의 SI 단위를 입력 규약으로 보존한다. |
| CP1-077 | NetCDF 계획 | H 코드 대조 대상 아님 | p.6 `In the next version ... such as NetCDF` | NetCDF는 이 논문 시점의 향후 계획이다. |
| CP1-085 | Fig. 5·Fresnel·표시 옵션 | H 코드 대조 대상 아님 | p.7 Fig. 5 `reflections and refractions (a)`, `colormap ... (b) ... (c)` | Fig. 5는 이전 판의 시각화 사례이다. |
| CP1-087 | 평면 해빈 설정 | H 코드 대조 대상 아님 | p.7 `1:19.85`, `0.005 < H/d < 0.5`, 마찰 `f = 0.0, 0.01, and 0.001` | 평면 해빈의 수치 설정값은 사례값이다. |
| CP1-090 | Fig. 6 처오름 | H 코드 대조 대상 아님 | p.7 Fig. 6 `maximum run-up ... versus ... wave height` | Fig. 6은 이전 판의 무차원 처오름 비교이다. |
| CP1-092 | 평면 해빈 정확도·소산 해석 | H 코드 대조 대상 아님 | p.8 `H/d = 0.28`, `f = 0.0075`; `minmod limiter ... sufficient numerical dissipation` | 사례 결과와 수치소산의 물리 해석을 현재 코드 검증과 구분한다. |
| CP1-094 | 천퇴 기하 G | H 코드 대조 대상 아님 | p.8 $G(y)=[y(6.096-y)]^{1/2}$, $0\le y\le6.096$ | G(y)는 Whalin 사례의 기하 정의이다. |
| CP1-095 | Whalin 수조·수치 설정 | H 코드 대조 대상 아님 | p.8 `2000 × 65 cells with a time step of 0.001 s`, `a = 0.0075 m`, `T = 2 s` | Whalin 사례의 진폭·주기·흡수층 폭을 현 기본값으로 옮기지 않는다. |
| CP1-096 | FFT·Fig. 8 | H 코드 대조 대상 아님 | p.8 `FFT analyses`; p.9 Fig. 8 `symbols are experimental data from Whalin [15]` | 조화성분 후처리 비교와 실시간 커널을 구분한다. |
| CP1-097 | Fig. 9 표시 | H 코드 대조 대상 아님 | p.8 `vertical scale ... factor of 80`; p.9 Fig. 9 `Water surface elevation` | 수직 표시 배율 80은 모델 물리 계수가 아니다. |
| CP1-098 | 원뿔섬 실험 배치 | H 코드 대조 대상 아님 | p.9 `7.2 m base diameter and 1/4 side slope`, `0.32 m depth` | 실험 배치와 계산 영역의 수치를 구분한다. |
| CP1-099 | 원뿔섬 수치 설정 | H 코드 대조 대상 아님 | p.9 `601×601 cells`, `0.005 s`, `H/d = 0.04, 0.09, and 0.18` | 원뿔섬 계산은 마찰을 무시한 세 실제 상대파고 사례이다. |
| CP1-100 | Fig. 10 계측점 | H 코드 대조 대상 아님 | p.9 Fig. 10 `gauge locations are shown by dots` | Fig. 10은 계측점 평면 배치이다. |
| CP1-101 | Fig. 11 | H 코드 대조 대상 아님 | p.9 Fig. 11 `H/d = 0.04 ... #6, #9, #16, and #22` | Fig. 11의 실험·수치 시계열을 현재 실행 결과로 부르지 않는다. |
| CP1-102 | Fig. 12 | H 코드 대조 대상 아님 | p.10 Fig. 12 `H/d = 0.09` | Fig. 12는 두 번째 원뿔섬 사례의 비교이다. |
| CP1-103 | Fig. 13 | H 코드 대조 대상 아님 | p.10 Fig. 13 `H/d = 0.18` | Fig. 13은 세 번째 원뿔섬 사례의 비교이다. |
| CP1-104 | 정확도·해상도 해석 | H 코드 대조 대상 아님 | p.10 `This might be because of the finer resolutions`; `about 25%` | 해상도 원인은 가능성으로 적고 선행모델 비교 수치를 현재 오차로 옮기지 않는다. |
| CP1-105 | 시간 성능 비교 | H 코드 대조 대상 아님 | p.10 `less than 15 s`; `not directly comparable` | 원문이 직접 비교할 수 없다고 한 계산 시간을 가속비로 바꾸지 않는다. |
| CP1-106 | 수평 처오름 문턱 | H 코드 대조 대상 아님 | p.10 $\delta=s\Delta x/3$, `initial shoreline radius (2.32 m)` | 처오름 후처리 δ와 수력 계산 delta를 구분한다. |
| CP1-107 | Fig. 14 | H 코드 대조 대상 아님 | p.11 `vertical scale ... factor of 10`; (a)·(b)·(c)의 전면·충돌·후면 설명 | Fig. 14는 이전 판의 세 시점 표시이다. |
| CP1-130 | 서지·감사·부록·참고문헌 | H 코드 대조 대상 아님 | p.11 `Acknowledgments`, `Appendix A. Supplementary data`, `References` | 서지·감사·외부 자료 링크는 수치 커널과 구분한다. |
| CP1-161 | 최초성·연구 배경 | H 코드 대조 대상 아님 | p.1 `first-of-its-kind`; p.2 `robustness ... accuracy` | 최초성과 연구 배경 평가는 구현 존재의 증거와 구분한다. |
| CP1-162 | KP07 수학 성질·평가 | H 코드 대조 대상 아님 | p.3 `guarantees the positivity`, `no need to keep track of the wet–dry front` | 원 KP07 성질을 현재 변형 코드에 대한 증명으로 자동 승계하지 않는다. |
| CP1-163 | 고립파 이론 정의 | H 코드 대조 대상 아님 | p.4 `non-linear and dispersive effects are in balance` | 초기 고립파 형식과 수치 시간 전진 중 모양 유지를 구분한다. |
| CP1-164 | 사용 권고·일반 알고리즘·외부 영상 | H 코드 대조 대상 아님 | p.4 `compiled version as much as possible`; p.6 `Thomas algorithm`; p.7 영상 주소 | 이전 프로그램 사용법과 외부 도구 내부를 현재 모델 완료 조건으로 삼지 않는다. |

### 5.8 범위와 집계 확인

| PDF 쪽 | 확인한 원문 항목 | 주 대조 행 |
|---|---|---|
| p.1 | 초록·프로그램 정보·서론·서지. 번호 식·그림·표 없음. | CP1-001–004·130·161 |
| p.2 | 서론 계속·무번호 변수/벡터 정의·식 (1)–(6)·B=1/15·kd 제한·육상 NLSW | CP1-005–017·013–014 |
| p.3 | 식 (7)–(23)·KP07 네 단계·습건·AB3/AM4·시작 단계·삼중대각 계수 | CP1-018–045·162 |
| p.4 | 식 (24)–(36)·세 경계·마찰·쇄파·고립파·소프트웨어 설명 시작 | CP1-046–065·086·163–164 |
| p.5 | Fig. 1 흐름·Fig. 2 CML 모든 태그·입출력 설명 | CP1-066–075·081 |
| p.6 | Fig. 3 경계 코드·Fig. 4 CR·ASCII/NetCDF 계획·GPU 자료·구현 | CP1-044·047·076–080·164 |
| p.7 | 빌드·실행·GUI·Fig. 5·Fig. 6·평면 해빈 설정 | CP1-082–090·164 |
| p.8 | Fig. 7·평면 해빈 결과·식 (37)·G 정의·Whalin 설정·FFT·배율 | CP1-091–097 |
| p.9 | Fig. 8–11·원뿔섬 배치/계산·결과·색상표 | CP1-096–104·165 |
| p.10 | Fig. 12–13·성능과 정확도 비교·처오름 문턱·결론 시작 | CP1-102–107·130 |
| p.11 | Fig. 14–15·결론·감사·부록·참고문헌 | CP1-107–108·130 |

이 보고서는 D로 판정한 행이 없다. CML·실행물·hot start·ASCII 등 실제 차이는 판 식별과 git 이력이 있는 A이다. NetCDF는 미래 계획이므로 H이다. 적용 사례·후처리·이론 정의도 H이다. 따라서 검색 부재만으로 기능이 없다고 확정한 D 행은 없다. X로 판정한 행도 없다. 이 보고서의 오기 판정은 같은 논문의 내부 모순·식의 직접 계산·현재 코드와 노트의 직접 모순으로 해소했다. 외부 원문의 유도 전부를 검증했다는 뜻은 아니다.

모델 실행과 브라우저 실행은 하지 않았다. 표시 영상·성능·수치 수렴·물리 정확도는 검증하지 않았다. 이 보고서는 지정된 2017년 논문의 문서 항목 대조와 현재 코드 경로·이력 대조를 끝낸다. 부속 도구·외부 라이브러리·범위 밖 예제 내부로 확장하지 않는다.

제2–4절의 행 ID는 CP1-001부터 CP1-169까지 누락과 중복 없이 있다. 그중 일치 41행은 제5절에서 제외했다. 제5절 차이 결론 표에는 나머지 128행이 각각 한 번씩 있다. 이 집계는 파일의 표 행을 읽는 정적 검사로 확인했다. 모델은 실행하지 않았다.

분류별 개수: 일치 41, A 38, B 24, C 30, D 0, E 3, F 6, H 27, X 0, 총 169행. 열지 못한 파일: `fd57bb7:shaders/TriDiag_PCRx.wgsl`은 해당 커밋에 없음. `6f1272f:shaders/TriDiag_PCRx.wgsl`을 대신 열어 최초 Boussinesq PCR을 확인함. 현재 기준의 요청 대상 파일과 2017년 11쪽 이미지 중 열기 실패로 남은 파일은 없음.
