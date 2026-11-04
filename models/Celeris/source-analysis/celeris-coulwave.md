---
title: "Celeris-WebGPU COULWAVE 고차 모드 — Pass3A/3B 보조패스·COULWAVE PCR"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/shaders/{Pass3A_COULWAVE,Pass3B_COULWAVE,Pass3_COULWAVE,Update_TriDiag_coef_COULWAVE,TriDiag_PCRx_COULWAVE,TriDiag_PCRy_COULWAVE}.wgsl 직접 read + ARCHITECTURE.md Model Modes. 라인 인용 소스 기준. 2026-06-15. 2026-11-04 Celeris recovery 대조 보고서 반영"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
source_scope: Celeris-WebGPU/js, Celeris-WebGPU/shaders
last_source_check: "2026-11-04 (recovery 대조 반영)"
---

> 상위: [../README.md](../README.md) · 표준 분산 모드: [celeris-boussinesq-solver.md](celeris-boussinesq-solver.md) · 파이프라인 분기: [celeris-pipeline-graph.md](celeris-pipeline-graph.md)
> COULWAVE 방정식 계보·항 매핑은 [`../web-refs/celeris-coulwave-theory.md`](../web-refs/celeris-coulwave-theory.md). **요점**: 모드2 "COULWAVE equations"는 **단일층 완전비선형(fully-nonlinear) 확장 Boussinesq**(Nwogu z_α + Wei-Kirby 1995, `constants_load_calc.js:36` 주석)이며 **2층/다층 아님**(소스에 단일 za). 모드1 "Bous"는 Madsen & Sørensen 약비선형(B=1/15). 이 노트는 WGSL 코드에서 검증 가능한 사실만 단언한다.

2020 논문이 제시한 분산항은 현재 모드 1의 계보이다 (Tavakkol 2020 p.3 식 (2)–(3)). 모드 2는 보조항 패스와 별도 비선형 삼중대각 계수를 사용한다 (`js/main.js:1553–1570,2661–2670`; `shaders/Update_TriDiag_coef.wgsl:52–61,86–95`). [11-04 대조 정정]

# COULWAVE 고차 모드 (NLSW_or_Bous == 2)

## 0. 모드 위치

`NLSW_or_Bous`로 방정식 family 선택 (ARCHITECTURE.md:63-67):

- `0` NLSW — explicit only, tridiag solver bypass.
- `1` Boussinesq — `Pass3_Bous`에 분산 source 추가 + implicit tridiag.
- `2` COULWAVE — **`Pass3A`/`Pass3B` 보조패스 추가** + COULWAVE 전용 tridiag 계수 + COULWAVE PCR shader (ARCHITECTURE.md:67).

Pass1은 면 상태를 재구성한다. Pass2는 면 수치 플럭스를 계산한다. COULWAVE의 Pass3A와 Pass3B는 보조량을 만든다. Pass3_COULWAVE는 발산·원천·시간 적분을 계산한다. BoundaryPass는 삼중대각계 풀이 전후에 호출한다 (`ARCHITECTURE.md:46–54`; `js/main.js:2641,2649,2662–2679,2696–2729`). NLSW는 implicit solve를 직접 텍스처 복사로 대체한다 (`js/Run_Tridiag_Solver.js:37–40`). [11-04 대조 정정]

코드상 검증되는 핵심: COULWAVE는 Bous 대비 (a) za(reference velocity 고도)를 셀별로 명시 계산하고, (b) S·T 발산항·그 1·2차 미분·E/F/G 고차 그룹을 **별도 보조패스에서 사전계산해 6-layer 3D 텍스처에 packing**하며, (c) tridiag 계수가 depth-상수형이 아니라 za·eta·z 의존형(넓은 의존)이고, (d) PCR 마지막 패스에서 velocity→flux 환산(× H_loc)을 수행한다. 이는 **완전비선형 분산**(η·za·속도구배 곱 유지)이며, Madsen(모드1)의 약비선형(정수심 d 기반)과의 차이가 본질 — 단·다층 구분이 아니다 (§4·web-refs §0).

---

## 1. Pass3A / Pass3B 보조패스 — 무엇을 사전계산하는가

표준 Bous에는 이 두 패스가 없다. COULWAVE에서 main 패스가 반복 참조할 고차 항을 미리 계산해 3D `txCW_groupings` 텍스처 layer로 packing한다 (`Pass3A_COULWAVE.wgsl` 문서 "Numerical Role": "JavaScript copies these outputs into layers of the 3D txCW_groupings texture").

### Pass3A — 기본량 + reference 고도 za

`Pass3A_COULWAVE.wgsl` (write 3 텍스처, line 17-19):

- `txModelVelocities = (u, v, eta, H)` — 셀평균 속도. u_here/v_here는 face velocity 4성분 평균 `(u4.x+y+z+w)/4` (`Pass3A_COULWAVE.wgsl:34-35`). flux에서 직접 뽑은 속도는 주석으로 "are not better"라 폐기됨 (`:41-42`).
- `txCW_zalpha = (za, dzadx, dzady, 0)` — reference 속도 고도 `za = -d + (1+Bous_alpha)*H` (`:44`), 그 중심차분 기울기 `dzadx/dzady` (`:75-76`).
- `txCW_uvhuhv = (u, v, u*d, v*d)` — 속도와 depth-곱 (`:80`). `du = u*d`, `dv = v*d`는 Pass3B에서 발산항 T의 재료.

H = `max(delta, eta+d)` 클램프 (`:40`).

### Pass3B — S·T 발산항 및 E/F/G 고차 그룹

`Pass3B_COULWAVE.wgsl`는 Pass3A 출력(`txCW_uvhuhv`, `txCW_zalpha`)을 입력받아 (binding `:15-16`) 9점 스텐실(중심·상하좌우·4 대각, `:29-41`)로 미분을 만든다.

핵심 발산량 (`:170-175`):
```
S = dudx + dvdy            // 속도 발산
T = dhudx + dhvdy          // (u*d) 발산
dSdx, dSdy, dTdx, dTdy     // 그 1차 미분(=u의 2차 미분 조합)
```
2차 미분 `d2udx2, d2hudx2, ... , d2udxdy`는 중심차분 (`:146-154`). 4차 미분(`:157-168`)과 rightright/leftleft 등 2-칸 이웃(`:110-135`)은 **주석 처리**되어 현재 비활성 (코드상 2차 정확도). 정확도 옵션은 토글 가능.

E(eta) 저장량 (`:184-188`):
```
temp2 = 1/6*(eta²-eta*d+d²) - 1/2*za²
temp3 = 1/2*(eta-d) - za
E1 = H*(temp2*dSdx + temp3*dTdx)
E2 = H*(temp2*dSdy + temp3*dTdy)
```
F/G 저장량은 `shaders/Pass3B_COULWAVE.wgsl:192–195`의 `let EzST = E * (eta_here * S + T);`, `let TzS2 = eta_2 * S * S + 2.0 * eta_here * S * T + T * T;`, `let uSxvSy = 0.5 * (za_2 - eta_2) * (u_here * dSdx + v_here * dSdy);`, `let uTxvTy = (za_here - eta_here) * (u_here * dTdx + v_here * dTdy);`이다. E는 이미 저장된 연속식 우변을 읽는다 (`shaders/Pass3B_COULWAVE.wgsl:191` `let E = textureLoad(dU_by_dt, idx, 0).x;`; `shaders/Pass3_COULWAVE.wgsl:488,521`). 예측 단계는 직전 저장값을 읽는다 (`js/main.js:2663,2679`). 수정 단계는 예측 Pass3의 도함수를 읽는다 (`js/main.js:2797,2812`). [11-04 대조 정정] [11-04 전수 검증 정정]

4개 출력 텍스처 (`:202-205`): `txCW_STval=(S,T,d2udxdy,d2vdxdy)`, `txCW_STgrad=(dSdx,dSdy,dTdx,dTdy)`, `txCW_Eterms=(E1,E2,E, dvdx-dudy)`, `txCW_FGterms=(EzST,TzS2,uSxvSy,uTxvTy)`. 마지막 `dvdx-dudy`는 **vorticity**.

### 3D 그룹핑 텍스처 layer 맵 (`js/main.js:2664–2669`의 복사원 기준) [11-04 대조 정정]
```
level 0: txCW_uvhuhv        [u, v, u*d, v*d] // [11-04 대조 정정]
level 1: txCW_zalpha        [za, dzadx, dzady, 0]
level 2: txCW_STval         [S, T, d2udxdy, d2vdxdy]
level 3: txCW_STgrad        [dSdx, dSdy, dTdx, dTdy]
level 4: txCW_Eterms        [E1, E2, E, dvdx-dudy(=vort)]
level 5: txCW_FGterms       [EzST, TzS2, uSxvSy, uTxvTy]
```
COULWAVE 보조량은 6층 텍스처에 모은다 (`js/main.js:2664–2669`). 층 0은 `txCW_uvhuhv`이다. 채널은 `u, v, u*d, v*d`이다. 여기서 `d`는 바닥 표고의 음수이다 (`shaders/Pass3A_COULWAVE.wgsl:39,80`). [11-04 대조 정정]

---

## 2. Pass3_COULWAVE 통합 — Bous 대비 차이

`Pass3_COULWAVE.wgsl`는 표준 `Pass3_Bous`와 골격(flux 발산 + press_x/y + friction + breaking + AB time integration)은 같으나 **분산 source 구성이 근본적으로 다르다**.

입력 차이: binding 3이 `txCW_groupings: texture_3d<f32>` (`:45`) — Bous에는 없는 입력. 분산항을 셀에서 재계산하지 않고 layer fetch로 가져온다 (`:236-316`).

내부 계산 (`near_dry>0` 분기, `:197-381`):

- η 기울기를 **4차 중심차분**으로 격상: `detadx = 1/12*(η_ll - 8η_l + 8η_r - η_rr)*1/dx` (`:222-223`). 저차 버전 `detadx_loworder`도 HO 항 내부용으로 별도 유지 (`:226-227`).
- F source `Fsrc` = temp1..temp7C 합 (`:334-347`). temp2는 E_here(연속식 우변)와 za²-eta²·dSdx 결합, temp3-6은 layer5(EzST/uSxvSy/uTxvTy/TzS2)의 x-방향 중심차분, **temp7A/B/C는 vorticity(`vort_here`)·dzadx/dzady 결합항** (`:342-345`). G source는 y-대칭 (`:350-363`).
- `F_star/G_star` = cross 미분(dvdxy/dudxy) + ddvdxy/ddudxy + detadx·(eta·dvdy+ddvdy) 형태, ×H (`:365-372`). 이것이 implicit solve로 넘어가는 분산 좌변 재료.
- 분산 source는 **Psi1/Psi2** 2-항으로 들어감 (`:374-378`): `Psi1x=Fsrc`, `Psi2x=(3 F_star - 4 F_G_star_old + F_G_star_oldold)/dt*0.5` — F_G_star의 **2차 BDF 시간미분**. 이것이 source_term의 momentum 성분에 가산 (`:486`).
- `E_src = dE1dx + dE2dy` (`:380`)는 연속식(질량) source에 가산 (`:486`).

time integration은 Bous와 동일한 3종 (Euler / predictor AB3-type `23/-16/5` / corrector `9/19/-5/1`, `:493-503`). breaking·vorticity_dissipation·friction·press·scalar transport 블록은 Bous와 공유 구조.

요약: Bous의 분산 source가 depth-기반 비교적 단순항인 데 비해, COULWAVE는 za·S·T·E·vorticity가 얽힌 다수 고차 항을 **사전계산 layer에서 조립**한다. F_star/G_star만 implicit으로 남기고 나머지(Psi)는 explicit AB로 처리.

---

## 3. COULWAVE 전용 tridiagonal — 왜 분리되었나

### 계수 (Update_TriDiag_coef_COULWAVE.wgsl)

표준 `Update_TriDiag_coef.wgsl`에도 사실 `NLSW_or_Bous==2` 분기가 존재한다 (standard `:52`, `:86`). 차이는 **za 정의와 입력 텍스처**:

| | 표준 `Update_TriDiag_coef.wgsl` | `Update_TriDiag_coef_COULWAVE.wgsl` |
|---|---|---|
| 입력 state | `current_state` (binding 2) | `current_stateUVstar` (binding 2, `:17`) |
| za | `Bous_alpha * d_here` (standard:56) | `-d_here + (1+Bous_alpha)*H_loc` (`:37`) |
| Globals | `delta` 없음 | `delta` 추가 (`:11`), H 클램프용 |
| near_dry 컷 | `near_dry < 0.0` (standard) | `near_dry < globals.delta` (`:53,86`) |
| d 우변 | 0 (coefx.w=0) | `UU_loc/H_loc` (velocity, `:52`) — flux 아닌 velocity |

COULWAVE 분기 계수 (`:67-69`, x):
```
a = (za²-z²)/2*1/d²x + (za-z)*d_west*1/d²x + zx*(z+d_west)/dx/2
b = 1 - (za²-z²)*1/d²x - 2(za-z)*d_here*1/d²x
c = (za²-z²)/2*1/d²x + (za-z)*d_east*1/d²x - zx*(z+d_east)/dx/2
```
계수가 **국소 za·z(=η)·이웃 depth·η기울기 zx 의존** — Bous의 depth-상수형 `(Bcoef+1/3)·d²/dx²` (`:75-77`)보다 비선형·자유표면 의존이 강하다. 별도 shader인 1차 이유는 (a) 입력이 `current_stateUVstar`이고 (b) `d=velocity`로 저장하며 (c) `delta` uniform이 필요해 **bind layout과 globals 구조가 다르기 때문**. 스텐실 폭은 둘 다 3-point(좌·중·우)로 동일 — "wider stencil"은 계수에는 아니다(분산항 자체는 Pass3에서 9점으로 이미 처리됨).

### PCR (TriDiag_PCRx/y_COULWAVE.wgsl)

PCR(Parallel Cyclic Reduction) 본체 알고리즘은 표준과 동일: `r=1/(1-a·c_left-c·a_right)`, `aOut/cOut/dOut` reduction (`PCRx_COULWAVE:91-94`). 분리된 **단 하나의 실질 차이**는 최종 패스(velocity→flux 환산):

```
if (p == Px - 1) {                          // PCRx_COULWAVE:102-108
    H_loc = max(delta, CurrentState.r - txBottom.z);
    dOut = dOut * H_loc;                     // velocity → flux
    txtemp2 = (η, dOut, ..., ...);
}
```
표준 `TriDiag_PCRx.wgsl` 최종 패스는 `dOut`을 **그대로** flux로 기록(× H_loc 없음, standard `:102-104`). COULWAVE는 계수 단계에서 우변을 `velocity = UU/H`로 정규화했기 때문에 solve 후 H를 곱해 flux로 되돌려야 한다. 이 한 줄이 COULWAVE PCR을 별도 파일로 둔 이유 (Globals에 `Px`/`Py`·`delta` 포함, `:5-7`). PCRy도 y-momentum에 대해 동형 (`PCRy_COULWAVE:102-108`).

> 주석 흔적: 두 파일 모두 "CODEX: ... only the final PCR pass converts velocity back to flux"로 이 환산이 최종 패스에만 적용됨을 명시.

---

## 4. COULWAVE vs Bous vs NLSW — 선택 기준

코드/문서에서 검증되는 계층 (ARCHITECTURE.md:63-67):

| 모드 | NLSW_or_Bous | 방정식 (`constants_load_calc.js:36`) | 분산 | 비선형 | implicit solve |
|---|---|---|---|---|---|
| NLSW | 0 | 비선형 천수 | 없음 | 완전 | bypass (텍스처 복사) |
| Bous | 1 | **Madsen** Boussinesq (B=1/15) | B-enhanced | **약비선형** | PCR |
| COULWAVE | 2 | **Fully Non-linear** Boussinesq (COULWAVE eq.) | Nwogu z_α | **완전비선형** | PCR (velocity↔flux 환산 추가) |

**모드 1→2 격상의 본질은 "비선형 차수"(약→완전)이지 "단층→다층"이 아니다** — 둘 다 단일층·O(μ²) 분산. 코드 주석이 모드1을 "Madsen", 모드2를 "Fully Non-linear Boussinesq (COULWAVE equations)"로 명시(`constants_load_calc.js:36`). za(Nwogu reference)는 **모드2만** 사용, 모드1 `Pass3_Bous`는 정수심 d 기반(za 미참조). 항별 식대응·계보는 [`../web-refs/celeris-coulwave-theory.md`](../web-refs/celeris-coulwave-theory.md) §3.

COULWAVE는 매 step 보조패스 2회 + 3D 텍스처 packing + 4차 η차분으로 추가 비용. 정확도↑↔비용↑.

코드-검증 사실 vs 논문 필요 구분:
- **코드 검증**: 모드 분기 메커니즘, 보조패스 출력 변수(S/T/E/F/G), 3D layer 맵, tridiag 계수 형태, PCR velocity↔flux 환산, 현재 2차 차분(4차는 주석 비활성), za=`−d+(1+α)H` (정수면 za=α·d, α=−0.531=Nwogu 최적).
- **논문 정독 필요(미수행)**: temp2/temp3 등 분산계수가 Wei-Kirby 1995/Lynett-Wu-Liu 2002의 어느 식번호와 1:1인지. (PDF repo 부재 — web-refs §3.4)

---

## 5. Cross-link

- 표준 분산 모드 (NLSW_or_Bous==1) 및 PCR 기본: [celeris-boussinesq-solver.md](celeris-boussinesq-solver.md)
- 타임스텝 패스 그래프·모드 분기: [celeris-pipeline-graph.md](celeris-pipeline-graph.md)
- COULWAVE 방정식 유도·차수·계보: [`../web-refs/celeris-coulwave-theory.md`](../web-refs/celeris-coulwave-theory.md)


## 문서와 코드 차이 (11-04 대조)

코드는 plynett/plynett.github.io main `ebca435`(2026-07-20)의 Celeris-WebGPU이다. 문서는 같은 커밋의 `docs/`·`README`이다. 논문은 Tavakkol & Lynett 2017(CPC), Tavakkol & Lynett 2020(CPC), Lynett et al. 2026(JWPCOE)이다.

코드 인용의 기준 경로는 `models/Celeris/raw/source_code/Celeris-WebGPU/`이다. 결론은 행별 최종 근거의 문장과 인용을 옮긴 AI 정리이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| callflow:RF-026 | 보조량 층 0 | `d8157c80:models/Celeris/source-analysis/celeris-coulwave.md:69` `level 0: txModelVelocities  [u, v, eta, h]` | `js/main.js:2664` `copy2DDataTo3DTexture(device, txCW_uvhuhv, txCW_groupings, 0, calc_constants.WIDTH, calc_constants.HEIGHT);`<br>확인한 원문: `d8157c80:models/Celeris/source-analysis/celeris-coulwave.md:67–74`; `67ca57c:js/main.js:1589`; `67ca57c:shaders/Pass3A_COULWAVE.wgsl:78–84`; `js/main.js:2664`; `shaders/Pass3A_COULWAVE.wgsl:38–40,78–84`; `shaders/Pass3_COULWAVE.wgsl:229` | B 문서 오기 | txCW_groupings의 층 0은 txCW_uvhuhv다. 채널은 u, v, u*d, v*d다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) |
| docs-architecture:CD1-933 | 총수심과 기준 고도 | 대상 8문서: COULWAVE 기준 고도의 구체식 없음. | ` shaders/Pass3A_COULWAVE.wgsl:38 ` `     let eta_here = textureLoad(txState, idx, 0).x; `<br>` shaders/Pass3A_COULWAVE.wgsl:39 ` `     let d_here = -textureLoad(txBottom, idx, 0).z; `<br>` shaders/Pass3A_COULWAVE.wgsl:40 ` `     let H_here = max(globals.delta, eta_here + d_here); `<br>` shaders/Pass3A_COULWAVE.wgsl:44 ` `     let za_here = -d_here + ( 1.0 + globals.Bous_alpha ) * H_here;  `<br>` shaders/Pass3A_COULWAVE.wgsl:80 ` `     let uvhuhv = vec4<f32>(u_here, v_here, u_here * d_here, v_here * d_here); `<br>확인한 원문: `shaders/Pass3A_COULWAVE.wgsl:38–45`<br>`shaders/Pass3A_COULWAVE.wgsl:75–84`<br>`docs/architecture/SIMULATION_PIPELINE.md:24–49`<br>`js/main.js:2664,2798` | C 문서 누락 | `let H_here = max(globals.delta, eta_here + d_here);`로 전체 수심을 제한한다. 기준 고도는 `let za_here = -d_here + ( 1.0 + globals.Bous_alpha ) * H_here;`이다. 층 0에 복사할 벡터는 `let uvhuhv = vec4<f32>(u_here, v_here, u_here * d_here, v_here * d_here);`이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD1f.md)) |
| docs-architecture:CD1-1299 | 일반 메뉴의 모드 선택 | `ARCHITECTURE.md:67` `2`: COULWAVE-style higher-order mode. | ` index.html:1382 ` `                     <select id="nlsw-select" name="nlswValue"> `<br>` index.html:1383 ` `                         <option value="0">NLSW</option> `<br>` index.html:1384 ` `                         <option value="1">Boussinesq</option> `<br>` index.html:1385 ` `                     </select> `<br>확인한 원문: `ARCHITECTURE.md:67`; `index.html:1382-1385`; `js/main.js:1564-1571,4748`; `ARCHITECTURE.md:67` 원문: `2`: COULWAVE-style higher-order mode. | C 문서 누락 | COULWAVE는 코드에 있지만 일반 Simulation Type 메뉴에는 선택값 2가 없다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD1h.md)) |
| docs-architecture:CD1-1386 | 비선형 계수와 경계 조건 | 대상 8문서: COULWAVE 비선형 계수와 우변의 구체식·분기 상세 없음. | ` shaders/Update_TriDiag_coef_COULWAVE.wgsl:36 ` `     let H_loc = max(globals.delta, z_loc + d_here); `<br>` shaders/Update_TriDiag_coef_COULWAVE.wgsl:37 ` `     let za = -d_here + ( 1.0 + globals.Bous_alpha ) * H_loc;  `<br>` shaders/Update_TriDiag_coef_COULWAVE.wgsl:52 ` `     d = UU_loc / H_loc; `<br>` shaders/Update_TriDiag_coef_COULWAVE.wgsl:53 ` `     if (idx.x <= 2 \|\| idx.x >= width - 3 \|\| near_dry < globals.delta) { `<br>` shaders/Update_TriDiag_coef_COULWAVE.wgsl:67 ` `             a =     (za2-zloc2)/2.*globals.one_over_d2x +   (za-z_loc)*d_west*globals.one_over_d2x + zx_loc*(z_loc+d_west)/globals.dx/2.; `<br>` shaders/Update_TriDiag_coef_COULWAVE.wgsl:68 ` `             b = 1.0-(za2-zloc2)*globals.one_over_d2x  - 2.0*(za-z_loc)*d_here*globals.one_over_d2x; `<br>` shaders/Update_TriDiag_coef_COULWAVE.wgsl:69 ` `             c =     (za2-zloc2)/2.*globals.one_over_d2x +   (za-z_loc)*d_east*globals.one_over_d2x - zx_loc*(z_loc+d_east)/globals.dx/2.; `<br>확인한 원문: `shaders/Update_TriDiag_coef_COULWAVE.wgsl:34-80`; `shaders/Update_TriDiag_coef_COULWAVE.wgsl:82-110`. | C 문서 누락 | `let H_loc = max(globals.delta, z_loc + d_here);`로 현재 수심을 정한다. `let za = -d_here + ( 1.0 + globals.Bous_alpha ) * H_loc;`로 기준 고도를 정한다. 각 운동량 우변은 H_loc로 나눈다. x방향은 `if (idx.x <= 2 \|\| idx.x >= width - 3 \|\| near_dry < globals.delta)`에서 단위 대각계를 사용한다. y방향은 `if (idx.y <= 2 \|\| idx.y >= height - 3 \|\| near_dry < globals.delta)`에서 단위 대각계를 사용한다. 내부 COULWAVE 계수는 현재 수면과 그 기울기에 의존한다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD1h.md)) |
| docs-source:CD2-299 | Pass3B 호출 순서 | `docs/source/shaders/Pass3B_COULWAVE_wgsl.md:24` `` This pass depends on `dU_by_dt.x` for the `E` term. In the main loop it must run after the derivative texture has been produced for the relevant substep. `` | `shaders/Pass3B_COULWAVE.wgsl:191` `     let E = textureLoad(dU_by_dt, idx, 0).x; `<br>`js/main.js:2663` `                     runComputeShader(device, Pass3B_Coulwave_uniformBuffer, Pass3B_Coulwave_uniforms, Pass3B_Coulwave_Pipeline, Pass3B_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY); `<br>`js/main.js:2679` `                     runComputeShader_EncStack(device, commandEncoderStack, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY); `<br>`js/main.js:2797` `                         runComputeShader(device, Pass3B_Coulwave_uniformBuffer, Pass3B_Coulwave_uniforms, Pass3B_Coulwave_Pipeline, Pass3B_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY); `<br>`js/main.js:2812` `                         runComputeShader_EncStack(device, commandEncoderStack, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY); `<br>확인한 원문: `docs/source/shaders/Pass3B_COULWAVE_wgsl.md:24`<br>`shaders/Pass3B_COULWAVE.wgsl:191`<br>`js/main.js:2662–2685,2795–2815`<br>`984091f:js/main.js:1711,1727`<br>`shaders/Pass3_COULWAVE.wgsl:521` | B 문서 오기 | Pass3B는 main Pass3보다 먼저 실행하며 이미 저장된 dU_by_dt.x를 E에 사용한다. 수정 단계의 Pass3B는 예측 단계의 Pass3가 갱신한 값을 읽는다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD2.md)) |
| docs-source:CD2-443 | 평가 표고의 수면 연동 | `docs/source/shaders/Pass3A_COULWAVE_wgsl.md:29` `` The definition of `za` is tied to `Bous_alpha` and the local total depth. If this definition changes, `Pass3B_COULWAVE`, `Pass3_COULWAVE`, and the COULWAVE tridiagonal coefficient shader must be checked together. `` | `shaders/Pass3A_COULWAVE.wgsl:44` `     let za_here = -d_here + ( 1.0 + globals.Bous_alpha ) * H_here;  `<br>`shaders/Update_TriDiag_coef_COULWAVE.wgsl:36` `     let H_loc = max(globals.delta, z_loc + d_here); `<br>`shaders/Update_TriDiag_coef_COULWAVE.wgsl:37` `     let za = -d_here + ( 1.0 + globals.Bous_alpha ) * H_loc;  `<br>확인한 원문: `docs/source/shaders/Pass3A_COULWAVE_wgsl.md:29`<br>`shaders/Pass3A_COULWAVE.wgsl:44`<br>`shaders/Update_TriDiag_coef_COULWAVE.wgsl:34–40` | C 문서 누락 | 현재 COULWAVE의 평가 표고는 `let za_here = -d_here + ( 1.0 + globals.Bous_alpha ) * H_here;`이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD2.md)) |
| docs-source:CD2-444 | COULWAVE 보조항 계수 | `docs/source/shaders/Pass3B_COULWAVE_wgsl.md:20` `` These values feed the high-order source terms in `Pass3_COULWAVE`. The shader currently uses second-order derivative stencils, with commented alternate fourth-order derivative blocks. ``<br>`docs/source/shaders/Pass3B_COULWAVE_wgsl.md:21` `  `<br>`docs/source/shaders/Pass3B_COULWAVE_wgsl.md:22` ` ## Change Notes `<br>`docs/source/shaders/Pass3B_COULWAVE_wgsl.md:23` `  `<br>`docs/source/shaders/Pass3B_COULWAVE_wgsl.md:24` `` This pass depends on `dU_by_dt.x` for the `E` term. In the main loop it must run after the derivative texture has been produced for the relevant substep. `` | `shaders/Pass3B_COULWAVE.wgsl:170` `     let S = dudx + dvdy; `<br>`shaders/Pass3B_COULWAVE.wgsl:171` `     let T = dhudx + dhvdy; `<br>`shaders/Pass3B_COULWAVE.wgsl:184` `     let temp2 = 1.0 / 6.0 * (eta_2 - eta_here * d_here + d_2) - 1.0 / 2.0 * za_2; `<br>`shaders/Pass3B_COULWAVE.wgsl:185` `     let temp3 = 1.0 / 2.0 * (eta_here - d_here) - za_here; `<br>`shaders/Pass3B_COULWAVE.wgsl:187` `     let E1 = H_here * (temp2 * dSdx + temp3 * dTdx); `<br>`shaders/Pass3B_COULWAVE.wgsl:188` `     let E2 = H_here * (temp2 * dSdy + temp3 * dTdy); `<br>`shaders/Pass3B_COULWAVE.wgsl:191` `     let E = textureLoad(dU_by_dt, idx, 0).x; `<br>`shaders/Pass3B_COULWAVE.wgsl:192` `     let EzST = E * (eta_here * S + T); `<br>`shaders/Pass3B_COULWAVE.wgsl:193` `     let TzS2 = eta_2 * S * S + 2.0 * eta_here * S * T + T * T; `<br>`shaders/Pass3B_COULWAVE.wgsl:194` `     let uSxvSy = 0.5 * (za_2 - eta_2) * (u_here * dSdx + v_here * dSdy); `<br>`shaders/Pass3B_COULWAVE.wgsl:195` `     let uTxvTy = (za_here - eta_here) * (u_here * dTdx + v_here * dTdy); `<br>확인한 원문: `docs/source/shaders/Pass3B_COULWAVE_wgsl.md:20–24`<br>`shaders/Pass3B_COULWAVE.wgsl:170–200` | C 문서 누락 | COULWAVE 보조항의 계수는 코드 원문을 인용한다. 외부 이론식과의 동일성을 이름만으로 확정하지 않는다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD2.md)) |
| docs-source:CD2-470 | E의 저장 시점 | `d8157c80:models/Celeris/source-analysis/celeris-coulwave.md:63` `` F/G(hu,hv) 저장량 (`:191-195`): `EzST = E*(eta*S+T)`, `TzS2 = eta²S² + 2 eta S T + T²`, `uSxvSy = 0.5(za²-eta²)(u dSdx + v dSdy)`, `uTxvTy = (za-eta)(u dTdx + v dTdy)`. 여기서 `E = dU_by_dt.x` (이전 step 연속식 우변, `:191`). `` | `shaders/Pass3B_COULWAVE.wgsl:191` `     let E = textureLoad(dU_by_dt, idx, 0).x; `<br>`js/main.js:2663` `                     runComputeShader(device, Pass3B_Coulwave_uniformBuffer, Pass3B_Coulwave_uniforms, Pass3B_Coulwave_Pipeline, Pass3B_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY); `<br>`js/main.js:2679` `                     runComputeShader_EncStack(device, commandEncoderStack, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY); `<br>`js/main.js:2797` `                         runComputeShader(device, Pass3B_Coulwave_uniformBuffer, Pass3B_Coulwave_uniforms, Pass3B_Coulwave_Pipeline, Pass3B_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY); `<br>`js/main.js:2812` `                         runComputeShader_EncStack(device, commandEncoderStack, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY); `<br>확인한 원문: `d8157c80:models/Celeris/source-analysis/celeris-coulwave.md:63`<br>`shaders/Pass3B_COULWAVE.wgsl:191`<br>`shaders/Pass3_COULWAVE.wgsl:488,521`<br>`js/main.js:2662–2685,2795–2815`<br>`f6fd78b:js/main.js:1918,1934,2052,2061,2067` | B 문서 오기 | Pass3B의 E는 이미 저장된 dU_by_dt.x다. 예측과 수정은 서로 다른 최신 저장값을 읽는다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD2.md)) |
| lynett2026:CP3-090 | PCR과 보조량 저장 | Lynett 2026 p.3–5. PCR·중간 상태·COULWAVE 그룹의 구현 상세 누락. | `js/Run_Tridiag_Solver.js:50` `let s = 1 << p;`; `:57` `const TridiagX_BindGroup_Current = (p == 0) ? TridiagX_BindGroup_BaseToA : ((p % 2 == 1) ? TridiagX_BindGroup : TridiagX_BindGroup_BToA);`; `shaders/Pass3A_COULWAVE.wgsl:44` `let za_here = -d_here + ( 1.0 + globals.Bous_alpha ) * H_here;`<br>확인한 원문: Lynett 2026 p.3–5; `js/Run_Tridiag_Solver.js:48–91`; `js/main.js:514–521,2662–2669`; `shaders/Pass3A_COULWAVE.wgsl:38–45` | C 문서 누락 | PCR은 `let s = 1 << p;`로 간격을 늘린다. COULWAVE 보조량은 6층 텍스처에 모은다. 기준면은 `let H_here = max(globals.delta, eta_here + d_here);`와 `let za_here = -d_here + ( 1.0 + globals.Bous_alpha ) * H_here;`로 계산한다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) |
| lynett2026:CP3-114 | 패스 역할 | `d8157c80:models/Celeris/source-analysis/celeris-coulwave.md:24` `Pass1(flux) → Pass2(explicit)` | `js/main.js:2641,2649,2679`; `ARCHITECTURE.md:46–51`<br>확인한 원문: `d8157c80:models/Celeris/source-analysis/celeris-coulwave.md:24`; `ARCHITECTURE.md:46–51`; `js/main.js:2641,2649,2679` | B 문서 오기 | Pass1은 재구성, Pass2는 플럭스, Pass3는 적분이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) |
| tavakkol2017:CP1-126 | COULWAVE 별도 경로 | 문서 없음. | `js/main.js:1570` `Pass3_ShaderCode_Bous = await fetchShader('/shaders/Pass3_COULWAVE.wgsl');`; `shaders/Update_TriDiag_coef.wgsl:52–53` `if (globals.NLSW_or_Bous == 2) {`<br>`// COULWAVE equations`<br>확인한 원문: Tavakkol 2017 p.2–3 식 (2)–(23); `js/constants_load_calc.js:36–38`; `js/main.js:1553–1554,1568–1583,2661–2669`; `shaders/Update_TriDiag_coef.wgsl:52–61` | C 문서 누락 | 현재 COULWAVE는 2017년 Madsen형 식과 별도 경로이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) |
| tavakkol2017:CP1-154 | 재구성·플럭스·시간 갱신 | `d8157c80:models/Celeris/source-analysis/celeris-coulwave.md:24` `Pass1(flux) → Pass2(explicit)` | `shaders/Pass1.wgsl:166–169`; `shaders/Pass2.wgsl:136` `textureStore(txXFlux, idx, xflux);`; `shaders/Pass3_Bous.wgsl:404`<br>확인한 원문: 위키 `d8157c80:models/Celeris/source-analysis/celeris-coulwave.md:24`; `shaders/Pass1.wgsl:128–171`; `shaders/Pass2.wgsl:122–140`; `shaders/Pass3_Bous.wgsl:392–409` | B 문서 오기 | Pass1은 재구성이고 Pass2는 플럭스이며 Pass3가 시간 갱신이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) [11-04 전수 검증 정정] |
| tavakkol2020:CP2-128 | 모드 2의 비선형 계수 | Tavakkol 2020 p.2는 COULWAVE를 다른 모형의 사례로 든다. Base 구현 모드로 정의하지 않는다. | `js/constants_load_calc.js:38` `Bous_alpha: -0.531,  // extended Boussinesq (Nwogu) parameter,`; `js/main.js:1553–1554` `const Pass3A_Coulwave_ShaderCode= await fetchShader('/shaders/Pass3A_COULWAVE.wgsl')` / `const Pass3B_Coulwave_ShaderCode= await fetchShader('/shaders/Pass3B_COULWAVE.wgsl')`<br>확인한 원문: Tavakkol 2020 p.2–3; `js/constants_load_calc.js:38`; `js/main.js:1553–1570,2661–2670`; `shaders/Update_TriDiag_coef.wgsl:52–61,86–95` | C 문서 누락 | 모드 2는 보조항 패스와 별도 비선형 삼중대각 계수를 사용한다. 2020 식 (2)–(3)을 모드 2의 전체 방정식으로 쓰지 않는다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP2.md)) |
