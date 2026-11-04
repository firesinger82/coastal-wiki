# Celeris code-5 전수 대조 (11-04)

대상 23개 기록의 160개 구간 행을 원문 5,090행과 대조했다.
행 수는 아래 기록별 표에서 합산했다.
각 구간은 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 의미를 대조했다.
추가 인용과 행 번호의 기계 대조에서도 불일치가 없었다.
구간 경계와 frontmatter를 유지했다.
행 수는 기록 표의 구간 행 수와 해당 원문 행 수를 구분한다.
정정·보완은 각각 표시가 붙은 구간 행 수로 센다.
한 구간에 두 표시가 있으면 양쪽에 센다.
이상 없음은 두 표시가 없는 대조 완료 구간 행 수이다.
모델은 실행하지 않았다.

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 상태 |
|---|---:|---:|---|
| scripts/load_WebGPUCeleris_output.m.md | 4 | 80 | 완료 |
| shaders/AddDisturbance.wgsl.md | 8 | 241 | 완료 |
| shaders/BoundaryPass.wgsl.md | 19 | 725 | 완료 |
| shaders/CalcMeans.wgsl.md | 4 | 104 | 완료 |
| shaders/CalcWaveHeight.wgsl.md | 3 | 77 | 완료 |
| shaders/Copytxf32_txf16.wgsl.md | 3 | 50 | 완료 |
| shaders/ExtractNestedBoundaryTimeSeries.wgsl.md | 3 | 53 | 완료 |
| shaders/ExtractTimeSeries.wgsl.md | 3 | 65 | 완료 |
| shaders/MouseClickChange.wgsl.md | 7 | 246 | 완료 |
| shaders/Pass0.wgsl.md | 3 | 60 | 완료 |
| shaders/Pass1.wgsl.md | 6 | 172 | 완료 |
| shaders/Pass1_HighOrder.wgsl.md | 11 | 368 | 완료 |
| shaders/Pass2.wgsl.md | 6 | 206 | 완료 |
| shaders/Pass2_HighOrder_HLLC.wgsl.md | 9 | 291 | 완료 |
| shaders/Pass2_HighOrder_HLLEM.wgsl.md | 8 | 274 | 완료 |
| shaders/Pass3A_COULWAVE.wgsl.md | 4 | 85 | 완료 |
| shaders/Pass3B_COULWAVE.wgsl.md | 6 | 206 | 완료 |
| shaders/Pass3_Bous.wgsl.md | 12 | 430 | 완료 |
| shaders/Pass3_COULWAVE.wgsl.md | 14 | 524 | 완료 |
| shaders/Pass3_NLSW.wgsl.md | 8 | 286 | 완료 |
| shaders/Pass3_NLSW_Spherical.wgsl.md | 8 | 267 | 완료 |
| shaders/Pass_Breaking.wgsl.md | 6 | 145 | 완료 |
| shaders/SedTrans_Pass1.wgsl.md | 5 | 135 | 완료 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| scripts/load_WebGPUCeleris_output.m.md:1–22 | 바닥 단위 누락 | 주석의 `[m]` 보완 | 16 |
| scripts/load_WebGPUCeleris_output.m.md:23–50 | 주석 처리한 판독을 개괄 | 파일 이름·판독식·단위와 루프 종료 위치 보완 | 23–49, 80 |
| scripts/load_WebGPUCeleris_output.m.md:51–69 | 주석 처리한 속도·보간을 개괄 | 속도식·NaN 대입·보간 위치·보간식 보완 | 52–68 |
| shaders/AddDisturbance.wgsl.md:56–79 | 회전 좌표 | xc와 제곱합의 제곱근 yc로 정정 | 63–68 |
| shaders/AddDisturbance.wgsl.md:106–159 | 주석 대입식 누락 | disturbanceDir의 주석 대입식 보완 | 120 |
| shaders/AddDisturbance.wgsl.md:182–209 | earthquake 호출 주석이라는 요약 | 호출 인수를 원문 인용 | 194 |
| shaders/AddDisturbance.wgsl.md:210–241 | 종류 4 가지 안으로 서술 | 종류 5 가지 진입·닫힘·마지막 else 부재로 정정. 주석 조건·대입 보완 | 210, 229–240 |
| shaders/BoundaryPass.wgsl.md:154–188 | 원점 이동 목적 주석 누락 | 161행 주석은 Hs finger effect를 줄이려고 원점 위치를 시간에 따라 천천히 바꾼다고 설명한다. | 161 |
| shaders/BoundaryPass.wgsl.md:279–324 | 마지막 else 부재 미표시 | 서쪽의 300·306행 사슬과 동쪽의 314·320행 사슬에는 마지막 `else`가 없다. | 299–324 |
| shaders/BoundaryPass.wgsl.md:325–354 | 마지막 else 부재 미표시 | 남쪽의 328·334행 사슬과 북쪽의 342·348행 사슬에는 마지막 `else`가 없다. | 327–352 |
| shaders/BoundaryPass.wgsl.md:401–445 | <=1을 0·1로 한정. 마지막 else 미표시 | 경계 종류가 1 이하이면 고체벽 처리를 적용한다. 네 방향의 내부 `if`·`else if` 사슬에는 마지막 `else`가 없다. | 403–444 |
| shaders/BoundaryPass.wgsl.md:446–514 | 마지막 else 미표시 | 네 방향의 `incident_wave_type` 사슬에는 마지막 `else`가 없다. | 449–512 |
| shaders/BoundaryPass.wgsl.md:549–577 | 마지막 else 미표시 | 553–572행 사슬에는 마지막 `else`가 없다. | 553–572 |
| shaders/BoundaryPass.wgsl.md:691–725 | else 인용과 사슬 종료 맥락 누락 | 694행 조건의 반대 가지는 `else {` (698)이다. 713행 조건의 반대 가지는 `else {` (716)이다. 693·703행 사슬에는 마지막 `else`가 없다. 692행 블록은 708행에서 닫힌다. `main`은 725행에서 닫힌다. | 692–725 |
| shaders/CalcMeans.wgsl.md:28–59 | 건조 분기 주석 설명 누락 | 56행 주석의 속도 0 설명과 달리 실행식은 `eta`만 바꾼다. 누락된 주석 원문: `// If the water depth is below the base depth, set velocities to zero` (56). | 56 |
| shaders/CalcWaveHeight.wgsl.md:44–77 | 영점 통과 코드를 주석이라고만 요약 |  누락된 주석 원문: `//    var max_eta = old_vals.r;` (46);`//    var min_eta = old_vals.g;` (47);`//    var N_waves = old_vals.b;` (48);`//    var H_mean  = old_vals.a;` (49);`//  if(globals.n_time_steps_waveheight <= 1) {` (50);`//      N_waves = 0.0;` (51);`//      H_mean = 0.0;` (52);`//       max_eta = -999999.;` (53);`//       min_eta =  999999.;` (54);`//    } else if(eta_New>=0. && eta_Old<0.) {  // zero-up crossing` (56);`//       N_waves = N_waves + 1.0;` (57);`//       let H = max_eta - min_eta;` (59);`//        let update_frac = 1. / N_waves;` (61);`//        let old_frac = 1.0 - update_frac;` (62);`//        H_mean = old_frac * H_mean + update_frac * H;` (64);`//        max_eta = -999999.;` (66);`//        min_eta =  999999.;` (67);`//    } else {` (69);`//        max_eta = max(max_eta,eta_New);` (70);`//        min_eta = min(min_eta,eta_New);` (71);`//    }` (72);`//    let new_vals = vec4<f32>(max_eta, min_eta, N_waves, H_mean);` (73). | 46·47·48·49·50·51·52·53·54·56·57·59·61·62·64·66·67·69·70·71·72·73 |
| shaders/Copytxf32_txf16.wgsl.md:19–40 | 속도 0 설명 주석 누락 | 28행 주석의 설명과 달리 건조 분기는 `eta`와 `foam`만 바꾼다. 누락된 주석 원문: `// If the water depth is below the base depth, set velocities to zero` (28). | 28 |
| shaders/ExtractNestedBoundaryTimeSeries.wgsl.md:1–22 | 바닥 입력의 목적 주석 누락 |  누락된 주석 원문: `// Added by Codex: Bottom elevation is needed so dry cells export zero eta/hu/hv instead of DEM elevation.` (20). | 20 |
| shaders/ExtractTimeSeries.wgsl.md:45–65 | else 대응 조건과 닫힘 맥락 누락 | 45행 `else {`는 36행 `if (globals.river_sim == 1) {`의 반대 가지이다. 이 가지는 54행에서 닫힌다. 50행 `} else {`는 48행 `if (globals.disturbanceType > 1) {`의 반대 가지이다. 55행은 31행 조건의 반대 가지를 연다. 그 가지는 61행에서 닫힌다. `main`은 64행에서 닫힌다. | 36–64 |
| shaders/MouseClickChange.wgsl.md:40–68 | 마지막 else 부재 미표시 | 60·62행 사슬에는 마지막 `else`가 없다. | 60–64 |
| shaders/MouseClickChange.wgsl.md:69–103 | 구조물 형상·끝점 연속성 설명 누락 |  누락된 주석 원문: `// CODEX: Trapezoidal/capsule linear-structure target elevation, continuous through rounded endpoints.` (85). | 85 |
| shaders/MouseClickChange.wgsl.md:104–149 | 주석 처리된 텍스처 대입과 편집 대상 설명 누락 | 112–125행 사슬과 111–140행 사슬에는 마지막 `else`가 없다. 누락된 주석 원문: `// B_here = textureLoad(txDesignComponents, idx, 0);` (127);`// B_here2 = textureLoad(txBottomFriction, idx, 0);` (128);`// min_val = 0.0;` (129);`// CODEX: Linear structures share this panel but edit bathy/topo instead of design-component IDs.` (130). | 127·128·129·130 |
| shaders/MouseClickChange.wgsl.md:185–214 | 다음 else-if 가지를 이전 가지 안으로 서술 | 105행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {`와 150행 `if (globals.whichPanelisOpen == 3){` 안에서 185행은 169행 가지를 닫고 마찰 가지를 연다. 198행은 150행 가지를 닫고 패널 2 가지를 연다. 151–197행 사슬에는 마지막 `else`가 없다. | 169–198 |
| shaders/MouseClickChange.wgsl.md:185–214 | 주석 원형 편집식과 형상 설명 누락 |  누락된 주석 원문: `// var r = calc_radial_distance(xloc,yloc,xo,yo);` (199);`// var dH = 0.0;` (200);`// var f = 0.0;` (201);`// if(r <= 0.5 * globals.designcomponent_Radius) {` (202);`//     f = 1.0;` (203);`// }` (204);`// dH = (f32(globals.designcomponentToAdd) - B_here.x)*f;` (205);`// B_here.x = max(min_val,B_here.x + dH);` (206);`// // change friction to match` (208);`// let k_friction = 4.0 / globals.designcomponent_Radius;` (209);`// f = calc_radial_function(xloc,yloc,xo,yo,k_friction);` (210);`// dH = (globals.designcomponent_Friction - B_here2.x)*f;` (212);`// B_here2.x = max(min_val,B_here2.x + dH);` (213);`// CODEX: Add a linear structure to bathy/topo using a rounded capsule footprint and trapezoidal cross-section.` (214). | 199·200·201·202·203·204·205·206·208·209·210·212·213·214 |
| shaders/MouseClickChange.wgsl.md:215–246 | else와 바깥 블록 종료 위치 누락 | 224행 `} else {`는 215행 조건의 반대 가지이다. 이 가지는 240행에서 닫힌다. 198행 패널 2 가지는 242행에서 닫힌다. 패널 사슬에는 마지막 `else`가 없다. `main`은 246행에서 닫힌다. | 215–246 |
| shaders/Pass0.wgsl.md:21–44 | 중심 판독 주석식 누락 |  누락된 주석 원문: `//    let in_here = textureLoad(txState, idx, 0).x;` (33);`//    let B_here = textureLoad(txBottom, idx, 0).z;` (39). | 33·39 |
| shaders/Pass0.wgsl.md:45–60 | 중심 수심 주석식 누락 |  누락된 주석 원문: `//    let h_here = in_here.x - B_here;` (45). | 45 |
| shaders/Pass1.wgsl.md:96–123 | 초기화 설명 주석 누락 | 108행은 `standard deviation`을 언급하는 주석이다. 누락된 주석 원문: `// Initialize variables for water height, momentum components, and standard deviation` (108). | 108 |
| shaders/Pass1_HighOrder.wgsl.md:116–149 | else 인용 및 함수 닫힘 누락 | `else {` (135)는 116행 `if (ilim_c == 1) {`의 반대 가지이다. 이 가지는 141행에서 닫힌다. `ReconstructMUSCL4`는 147행에서 닫힌다. | 116–147 |
| shaders/Pass1_HighOrder.wgsl.md:204–249 | 초기화 설명 주석 누락 |  누락된 주석 원문: `// Initialize variables for water height, momentum components, and standard deviation` (234). | 234 |
| shaders/Pass1_HighOrder.wgsl.md:250–276 | 원래 Reconstruct의 용도를 boundary conditions라고 부른 주석 누락 | 276행 `} else {`는 263행 조건의 반대 가지를 연다. 누락된 주석 원문: `// left / right: Use the original Reconstruct function for boundary conditions` (265);`// south / north: Use the original Reconstruct function for boundary conditions` (271). | 265·271 |
| shaders/Pass1_HighOrder.wgsl.md:277–305 | 바깥 else 조건식과 주석 용도 누락 | 276행 `} else {`는 263행 `if(wetdry <= globals.epsilon \|\| maxB3 >= -globals.epsilon) {`의 반대 가지이다. 이 가지는 304행에서 닫힌다. 285·299행 주석은 이 가지를 내부 지점의 고차 재구성으로 설명한다. | 263–304 |
| shaders/Pass2.wgsl.md:36–58 | 마지막 else 부재 미표시 | 45·53행 사슬에는 마지막 `else`가 없다. 사슬 뒤의 56행은 기본값 0을 반환한다. | 37–56 |
| shaders/Pass2.wgsl.md:169–206 | 바깥 블록 닫힘 위치 누락 | 139행 `if(globals.useSedTransModel == 1){`는 205행에서 닫힌다. `main`은 206행에서 닫힌다. | 139–206 |
| shaders/Pass2_HighOrder_HLLC.wgsl.md:37–70 | HLLEM 구조와 GPU 안전성을 표방하는 주석 누락 |  누락된 주석 원문: `// HLLC FLUX – 1:1 with HLLEM structure, GPU-safe` (69). | 69 |
| shaders/Pass2_HighOrder_HLLC.wgsl.md:71–96 | HLLEM과 같은 Roe 평균이라는 주석 누락 |  누락된 주석 원문: `// 2) Roe-average velocity (exact same as HLLEM)` (83). | 83 |
| shaders/Pass2_HighOrder_HLLC.wgsl.md:97–129 | 별 상태 공식·분모 보호·혼합 설명 주석 누락 | 바깥 함수는 71행 `fn HLLC_Flux(`에서 시작한다. 함수 본문은 79행에서 열린다. 누락된 주석 원문: `// 3) HLLC star state (branch-free, Toro formula)` (97);`// Safe division: clamp denominator away from zero` (105);`// Smooth blend: use sign of (S_star) to pick dominant side` (112). | 97·105·112 |
| shaders/Pass2_HighOrder_HLLC.wgsl.md:130–145 | 주석 수식과 반확산 설명 누락 | 바깥 함수 `HLLC_Flux`는 71행에서 시작한다. 함수 본문은 144행에서 닫힌다. 누락된 주석 원문: `// 4) Star flux: F* = F + S*(U* - U)` (131);`// 5) Mass fix + HLLEM-style anti-diffusion` (137). | 131·137 |
| shaders/Pass2_HighOrder_HLLC.wgsl.md:190–221 | 주석 처리한 HLL 조건·호출식 누락 |  누락된 주석 원문: `//    if (minH <= globals.delta) {` (208);`//        xflux = HLL_Flux(aplus, aminus, Fp_x, Fm_x, state_plus_x, state_minus_x, DU_flag);` (209);`//        yflux = HLL_Flux(bplus, bminus, Fp_y, Fm_y, state_plus_y, state_minus_y, DU_flag);` (210);`//    }` (211);`//    else {` (212);`//    }` (215). | 208·209·210·211·212·215 |
| shaders/Pass2_HighOrder_HLLC.wgsl.md:251–291 | 확산 미포함 이유의 주석 누락 | 222행 퇴적 조건은 290행에서 닫힌다. `main`은 291행에서 닫힌다. 누락된 주석 원문: `// diffusion terms have NOT been incorporating into the HLLEM fluxes` (268);`// as currently configured, that would require a divide by zero` (269). | 268·269 |
| shaders/Pass2_HighOrder_HLLEM.wgsl.md:45–79 | 주석 변수 대응과 HLL 수식 누락 |  누락된 주석 원문: `//   aplus    = S_R` (47);`//   aminus   = S_L` (48);`//   Fplus    = F_R = [h⁺u⁺, h⁺u⁺², h⁺u⁺v⁺, h⁺u⁺c⁺]` (49);`//   Fminus   = F_L = [h⁻u⁻, h⁻u⁻², h⁻u⁻v⁻, h⁻u⁻c⁻]` (50);`//   Uplus    = U_R = [h⁺, h⁺u⁺, h⁺v⁺, h⁺c⁺]` (51);`//   Uminus   = U_L = [h⁻, h⁻u⁻, h⁻v⁻, h⁻c⁻]` (52);`// standard two‐wave HLL:` (71);`//   (S_R F_L - S_L F_R + S_L S_R ΔU) / (S_R - S_L)` (72). | 47·48·49·50·51·52·71·72 |
| shaders/Pass2_HighOrder_HLLEM.wgsl.md:80–108 | 접촉파를 위한 Roe 평균이라는 주석 누락 |  누락된 주석 원문: `// 2) Roe‐average velocity for the contact wave` (92). | 92 |
| shaders/Pass2_HighOrder_HLLEM.wgsl.md:109–127 | 주석의 Roe·제한자·HLLEM 수식 누락 | 바깥 함수는 80행 `fn HLLEM_Flux(`에서 시작한다. 함수 본문은 125행에서 닫힌다. 누락된 주석 원문: `// 3) Build a simple Roe‐type “linearized” flux` (109);`//    Froe = 0.5*(F⁺ + F⁻) - 0.5*\|uRoe\|*(U⁺ - U⁻)` (110);`// 4) Compute a limiter φ that restores the contact` (117);`//    φ = max(0, 1 - max(\|S_L\|,\|S_R\|)/(\|uRoe\|+ε))` (118);`// 5) Return HLLEM flux = Fhll + φ*(Froe - Fhll)` (123). | 109·110·117·118·123 |
| shaders/Pass2_HighOrder_HLLEM.wgsl.md:173–203 | 주석 HLL 조건·호출식 누락 |  누락된 주석 원문: `//    if (minH <= globals.delta) {` (190);`//        xflux = HLL_Flux(aplus, aminus, Fp_x, Fm_x, state_plus_x, state_minus_x, DU_flag);` (191);`//        yflux = HLL_Flux(bplus, bminus, Fp_y, Fm_y, state_plus_y, state_minus_y, DU_flag);` (192);`//    }` (193);`//    else {` (194);`//    }` (197). | 190·191·192·193·194·197 |
| shaders/Pass2_HighOrder_HLLEM.wgsl.md:233–274 | 확산 미포함 이유의 주석 누락 | 204행 퇴적 조건은 273행에서 닫힌다. `main`은 274행에서 닫힌다. 누락된 주석 원문: `// diffusion terms have NOT been incorporating into the HLLEM fluxes` (250);`// as currently configured, that would require a divide by zero` (251). | 250·251 |
| shaders/Pass3A_COULWAVE.wgsl.md:22–46 | 유량 기반 속도 대안·평가 주석과 za 대안식 누락 |  누락된 주석 원문: `// let u_here = textureLoad(txState, idx, 0).y / H_here;  //testing whether velocities directly from flux are better.  They are not` (41);`// let v_here = textureLoad(txState, idx, 0).z / H_here;` (42);`//let za_here = d_here * globals.Bous_alpha;` (45). | 41·42·45 |
| shaders/Pass3A_COULWAVE.wgsl.md:47–74 | 정수심 기반 za 대안식 누락 |  누락된 주석 원문: `//let za_ip1 = d_ip1 * globals.Bous_alpha;` (52);`//let za_im1 = d_im1 * globals.Bous_alpha;` (59);`//let za_jp1 = d_jp1 * globals.Bous_alpha;` (66);`//let za_jm1 = d_jm1 * globals.Bous_alpha;` (73). | 52·59·66·73 |
| shaders/Pass3B_COULWAVE.wgsl.md:109–155 | ±2 판독 주석식과 시험 설명 누락 |  누락된 주석 원문: `// // hu, hv right right  // comment this block if testing with 4th order derivatives` (109);`// all_vars = textureLoad(txCW_uvhuhv, rightrightIdx, 0);` (110);`// let u_ip2 = all_vars.x;` (111);`// let v_ip2 = all_vars.y;` (112);`// let du_ip2 = all_vars.z;` (113);`// let dv_ip2 = all_vars.w;` (114);`// all_vars = textureLoad(txCW_uvhuhv, leftleftIdx, 0);` (117);`// let u_im2 = all_vars.x;` (118);`// let v_im2 = all_vars.y;` (119);`// let du_im2 = all_vars.z;` (120);`// let dv_im2 = all_vars.w;` (121);`// all_vars = textureLoad(txCW_uvhuhv, upupIdx, 0);` (124);`// let u_jp2 = all_vars.x;` (125);`// let v_jp2 = all_vars.y;` (126);`// let du_jp2 = all_vars.z;` (127);`// let dv_jp2 = all_vars.w;` (128);`// all_vars = textureLoad(txCW_uvhuhv, downdownIdx, 0);` (131);`// let u_jm2 = all_vars.x;` (132);`// let v_jm2 = all_vars.y;` (133);`// let du_jm2 = all_vars.z;` (134);`// let dv_jm2 = all_vars.w;` (135). | 109·110·111·112·113·114·117·118·119·120·121·124·125·126·127·128·131·132·133·134·135 |
| shaders/Pass3B_COULWAVE.wgsl.md:156–176 | 미분 차수와 정확도 차수 혼동 | 4차 정확도의 1차·2차 미분 대안식은 주석 처리되어 있다. | 156–168 |
| shaders/Pass3B_COULWAVE.wgsl.md:156–176 | 주석 차분식 누락 |  누락된 주석 원문: `// let dudx = 1.0 / 12.0 *  ( u_ip2 - 8.0 *  u_ip1 + 8.0 *  u_im1 -  u_im2) * globals.one_over_dx;` (157);`// let dhudx = 1.0 / 12.0 * (du_ip2 - 8.0 * du_ip1 + 8.0 * du_im1 - du_im2) * globals.one_over_dx;` (158);`// let dudy = 1.0 / 12.0 *  ( u_jp2 - 8.0 *  u_jp1 + 8.0 *  u_jm1 -  u_jm2) * globals.one_over_dy;` (159);`// let dhudy = 1.0 / 12.0 * (du_jp2 - 8.0 * du_jp1 + 8.0 * du_jm1 - du_jm2) * globals.one_over_dy;` (160);`// let dvdx = 1.0 / 12.0 *  ( v_ip2 - 8.0 *  v_ip1 + 8.0 *  v_im1 -  v_im2) * globals.one_over_dx;` (161);`// let dhvdx = 1.0 / 12.0 * (dv_ip2 - 8.0 * dv_ip1 + 8.0 * dv_im1 - dv_im2) * globals.one_over_dx;` (162);`// let dvdy = 1.0 / 12.0 *  ( v_jp2 - 8.0 *  v_jp1 + 8.0 *  v_jm1 -  v_jm2) * globals.one_over_dy;` (163);`// let dhvdy = 1.0 / 12.0 * (dv_jp2 - 8.0 * dv_jp1 + 8.0 * dv_jm1 - dv_jm2) * globals.one_over_dy;` (164);`// let d2udx2 = 1.0 / 12.0 *   ( u_ip2 - 16.0 *  u_ip1 + 30.0 *  u_here - 16.0 *  u_im1 +  u_im2) * globals.one_over_d2x;` (165);`// let d2hudx2 = 1.0 / 12.0 *  (du_ip2 - 16.0 * du_ip1 + 30.0 * du_here - 16.0 * du_im1 + du_im2) * globals.one_over_d2x;` (166);`// let d2vdy2 = 1.0 / 12.0 *   ( v_jp2 - 16.0 *  v_jp1 + 30.0 *  v_here - 16.0 *  v_jm1 +  v_jm2) * globals.one_over_d2y;` (167);`// let d2hvdy2 = 1.0 / 12.0 *  (dv_jp2 - 16.0 * dv_jp1 + 30.0 * dv_here - 16.0 * dv_jm1 + dv_jm2) * globals.one_over_d2y;` (168). | 157·158·159·160·161·162·163·164·165·166·167·168 |
| shaders/Pass3_Bous.wgsl.md:67–94 | 단정도 정밀도·약 5% 수심·마찰 과소평가 설명 누락 | 84행 `} else {`는 82행 `if (globals.isManning == 1) {`의 반대 가지이다. 누락된 주석 원문: `// need this special scaling step due to the need to take h^4, and precision issues with a single precision solver` (69);`// this lets us explicitly control the allowed precision in the scaled h^4, which we set to 1e-6.` (70);`// this implies that bottom friction may become inaccurate for flow depths less than ~ 5% of the base depth` (71);`// this approach will make bottom friction much SMALLER in these small flow depths` (72);`// I can not see a solution to this issue within the constraints of single precision for this term` (73). | 69·70·71·72·73 |
| shaders/Pass3_Bous.wgsl.md:262–288 | 바깥 블록 닫힘 위치 누락 | 192행 `if (near_dry > 0. && periodic_bc_fix < 0)`의 블록은 287행에서 닫힌다. | 192–287 |
| shaders/Pass3_Bous.wgsl.md:366–398 | 마지막 else 부재 미표시 | 367–375행과 377–385행의 기울기 보정 사슬에는 마지막 `else`가 없다. | 367–385 |
| shaders/Pass3_Bous.wgsl.md:399–430 | 마지막 else 부재 미표시 | 399–410행 시간 적분 사슬과 412–419행 표시 사슬에는 마지막 `else`가 없다. | 399–419 |
| shaders/Pass3_COULWAVE.wgsl.md:67–94 | 단정도·약 5% 수심·마찰 과소평가 주석 누락 | 84행 `} else {`는 82행 `if (globals.isManning == 1) {`의 반대 가지이다. 누락된 주석 원문: `// need this special scaling step due to the need to take h^4, and precision issues with a single precision solver` (69);`// this lets us explicitly control the allowed precision in the scaled h^4, which we set to 1e-6.` (70);`// this implies that bottom friction may become inaccurate for flow depths less than ~ 5% of the base depth` (71);`// this approach will make bottom friction much SMALLER in these small flow depths` (72);`// I can not see a solution to this issue within the constraints of single precision for this term` (73). | 69·70·71·72·73 |
| shaders/Pass3_COULWAVE.wgsl.md:186–235 | 그룹 층의 성분 주석을 언급했으나 내용 누락 |  누락된 주석 원문: `// level 0: txModelVelocities, [u, v, eta, h]` (229);`// level 1: txCW_zalpha, [za, dzadx, dzady, 0.0)]` (230);`// level 2: txCW_STval, [S, T, d2udxdy, d2vdxdy]` (231);`// level 3: txCW_STgrad, [dSdx, dSdy, dTdx, dTdy]` (232);`// level 4: txCW_Eterms, [E1, E2, E,  dvdx - dudy]` (233);`// level 5: txCW_FGterms, [EzST, TzS2, uSxvSy, uTxvTy]` (234). | 229·230·231·232·233·234 |
| shaders/Pass3_COULWAVE.wgsl.md:349–382 | 바깥 블록 닫힘 위치 누락 | 197행 `if (near_dry > 0. && periodic_bc_fix < 0)`의 블록은 381행에서 닫힌다. | 197–381 |
| shaders/Pass3_COULWAVE.wgsl.md:460–492 | 마지막 else 부재 미표시 | 461–469행과 471–479행 기울기 보정 사슬에는 마지막 `else`가 없다. | 461–479 |
| shaders/Pass3_COULWAVE.wgsl.md:493–524 | 마지막 else 부재 미표시 | 493–504행 시간 적분 사슬과 506–513행 표시 사슬에는 마지막 `else`가 없다. | 493–513 |
| shaders/Pass3_NLSW.wgsl.md:67–95 | 단정도·약 5% 수심·마찰 과소평가 주석 누락 | 84행 `} else {`는 82행 `if (globals.isManning == 1) {`의 반대 가지이다. 누락된 주석 원문: `// need this special scaling step due to the need to take h^4, and precision issues with a single precision solver` (69);`// this lets us explicitly control the allowed precision in the scaled h^4, which we set to 1e-6.` (70);`// this implies that bottom friction may become inaccurate for flow depths less than ~ 5% of the base depth` (71);`// this approach will make bottom friction much SMALLER in these small flow depths` (72);`// I can not see a solution to this issue within the constraints of single precision for this term` (73). | 69·70·71·72·73 |
| shaders/Pass3_NLSW.wgsl.md:222–251 | 마지막 else 부재 미표시 | 223–231행과 233–241행 기울기 보정 사슬에는 마지막 `else`가 없다. | 223–241 |
| shaders/Pass3_NLSW.wgsl.md:252–286 | 마지막 else 부재 미표시 | 257–266행 시간 적분 사슬과 271–278행 표시 사슬에는 마지막 `else`가 없다. | 257–278 |
| shaders/Pass3_NLSW_Spherical.wgsl.md:73–92 | else 인용 누락 | 83행 `} else {`는 81행 `if (globals.isManning == 1) {`의 반대 가지이다. | 81–85 |
| shaders/Pass3_NLSW_Spherical.wgsl.md:180–215 | 마지막 else 부재 미표시 | 180–188행과 190–198행 기울기 보정 사슬에는 마지막 `else`가 없다. | 180–198 |
| shaders/Pass3_NLSW_Spherical.wgsl.md:216–245 | 코리올리 추가 전 주석식과 북반구 부호 설명 누락 | 238–245행 시간 적분 사슬에는 마지막 `else`가 없다. 누락된 주석 원문: `// -globals.g * h_here * inv_Rcos_phi * detadlambda - in_state_here.y * friction_ + press_lambda + curvature_P,` (224);`// -globals.g * h_here * globals.one_over_R * detadphi - in_state_here.z * friction_ + press_phi + curvature_Q,` (225);`// Added by Codex: Add Coriolis source terms with positive f in the Northern Hemisphere.` (226). | 224·225·226 |
| shaders/Pass3_NLSW_Spherical.wgsl.md:246–267 | 마지막 else 부재 미표시 | 252–258행 표시 사슬에는 마지막 `else`가 없다. | 252–258 |
| shaders/Pass_Breaking.wgsl.md:57–84 | else 인용과 부호가 0인 경우의 대응 누락 | 67행 `} else {`는 63행 `if (P_here > 0.0) {`의 반대 가지이다. 72행 `} else {`는 62행 `if (abs(P_here) > abs(Q_here) ) {`의 반대 가지이다. 77행 `} else {`는 73행 `if (Q_here > 0.0) {`의 반대 가지이다. | 62–82 |
| shaders/Pass_Breaking.wgsl.md:85–105 | Kennedy 쇄파 모델 기본 매개변수라는 주석 누락 |  누락된 주석 원문: `// Kennedy et al breaking model, default parameters` (98). | 98 |
| shaders/Pass_Breaking.wgsl.md:106–124 | else 인용과 등호 경계의 가지 누락 | 110행 `} else {`는 106·108행 조건이 모두 거짓인 가지이다. 120행 `} else {`는 115·117행 조건이 모두 거짓인 가지이다. | 106–123 |
| shaders/SedTrans_Pass1.wgsl.md:28–50 | else 인용 누락 | 33행 `} else {`는 29·31행 동부호 조건이 모두 거짓인 가지이다. 이 가지는 0을 반환한다. | 29–35 |
| shaders/SedTrans_Pass1.wgsl.md:87–113 | 초기화 설명 주석 누락 |  누락된 주석 원문: `// Initialize variables for water height, momentum components, and standard deviation` (87). | 87 |

| shaders/Pass1_HighOrder.wgsl.md:52–85 | 4차 MUSCL-TVD라는 주석의 정확도 설명 누락 |  누락된 주석 원문: `// 4th-order MUSCL-TVD optimized reconstruction` (52);`// Reconstruct function for 4th-order MUSCL-TVD` (85). | 52·85 |
| shaders/Pass3_COULWAVE.wgsl.md:318–348 | E 소스 차분의 정확도 주석 누락 |  누락된 주석 원문: `// E source terms, take to 2nd order` (329). | 329 |
| shaders/Pass_Breaking.wgsl.md:57–84 | 시작 시각 수송의 어려움과 3×3 이웃이라는 주석 설명 누락 |  누락된 주석 원문: `// figuring out how to transport "t" is tricky.  Here we look to the dominant direction of flow, and look at the three cells on that 3*3 cube` (57). | 57 |

정정 5, 보완 70, 이상 없음 89
