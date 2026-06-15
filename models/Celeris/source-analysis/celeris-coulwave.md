---
title: "Celeris-WebGPU COULWAVE 고차 모드 — Pass3A/3B 보조패스·COULWAVE PCR"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/shaders/{Pass3A_COULWAVE,Pass3B_COULWAVE,Pass3_COULWAVE,Update_TriDiag_coef_COULWAVE,TriDiag_PCRx_COULWAVE,TriDiag_PCRy_COULWAVE}.wgsl 직접 read + ARCHITECTURE.md Model Modes. 라인 인용 소스 기준. 2026-06-15."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
---

> 상위: [../README.md](../README.md) · 표준 분산 모드: [celeris-boussinesq-solver.md](celeris-boussinesq-solver.md) · 파이프라인 분기: [celeris-pipeline-graph.md](celeris-pipeline-graph.md)
> COULWAVE 방정식 차수·유도·계보는 [`../web-refs/celeris-coulwave-theory.md`](../web-refs/celeris-coulwave-theory.md) (Nwogu 1993 z_α · Wei-Kirby 1995 단층 kh≲3 · Lynett-Liu 2004 다층 kh≈6). 이 노트는 WGSL 코드에서 검증 가능한 사실만 단언한다.

# COULWAVE 고차 모드 (NLSW_or_Bous == 2)

## 0. 모드 위치

`NLSW_or_Bous`로 방정식 family 선택 (ARCHITECTURE.md:63-67):

- `0` NLSW — explicit only, tridiag solver bypass.
- `1` Boussinesq — `Pass3_Bous`에 분산 source 추가 + implicit tridiag.
- `2` COULWAVE — **`Pass3A`/`Pass3B` 보조패스 추가** + COULWAVE 전용 tridiag 계수 + COULWAVE PCR shader (ARCHITECTURE.md:67).

타임스텝 내 순서 (ARCHITECTURE.md:50-54): Pass1(flux) → Pass2(explicit) → **(COULWAVE 한정) Pass3A → Pass3B** → Pass3_COULWAVE → Update_TriDiag_coef* → PCRx/PCRy. NLSW는 implicit solve를 직접 텍스처 복사로 대체.

코드상 검증되는 핵심: COULWAVE는 Bous 대비 (a) za(reference velocity 고도)를 셀별로 명시 계산하고, (b) S·T 발산항·그 1·2차 미분·E/F/G 고차 그룹을 **별도 보조패스에서 사전계산해 6-layer 3D 텍스처에 packing**하며, (c) tridiag 계수가 depth-상수형이 아니라 za·eta·z 의존형(넓은 의존)이고, (d) PCR 마지막 패스에서 velocity→flux 환산(× H_loc)을 수행한다. 정확한 분산 차수(예: O(μ⁴) 다층)는 WGSL로 환원 불가 → 원논문.

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
F/G(hu,hv) 저장량 (`:191-195`): `EzST = E*(eta*S+T)`, `TzS2 = eta²S² + 2 eta S T + T²`, `uSxvSy = 0.5(za²-eta²)(u dSdx + v dSdy)`, `uTxvTy = (za-eta)(u dTdx + v dTdy)`. 여기서 `E = dU_by_dt.x` (이전 step 연속식 우변, `:191`).

4개 출력 텍스처 (`:202-205`): `txCW_STval=(S,T,d2udxdy,d2vdxdy)`, `txCW_STgrad=(dSdx,dSdy,dTdx,dTdy)`, `txCW_Eterms=(E1,E2,E, dvdx-dudy)`, `txCW_FGterms=(EzST,TzS2,uSxvSy,uTxvTy)`. 마지막 `dvdx-dudy`는 **vorticity**.

### 3D 그룹핑 텍스처 layer 맵 (Pass3_COULWAVE.wgsl:229-234 주석)
```
level 0: txModelVelocities  [u, v, eta, h]
level 1: txCW_zalpha        [za, dzadx, dzady, 0]
level 2: txCW_STval         [S, T, d2udxdy, d2vdxdy]
level 3: txCW_STgrad        [dSdx, dSdy, dTdx, dTdy]
level 4: txCW_Eterms        [E1, E2, E, dvdx-dudy(=vort)]
level 5: txCW_FGterms       [EzST, TzS2, uSxvSy, uTxvTy]
```
즉 Pass3A(3장) + Pass3B(4장 중 7-vec 사용) = **6 layer**가 JS에 의해 단일 `texture_3d<f32>`로 묶여 main 패스에 전달된다.

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

| 모드 | NLSW_or_Bous | 분산 | 비용 | implicit solve |
|---|---|---|---|---|
| NLSW | 0 | 없음 (천수) | 최저 | bypass (텍스처 복사) |
| Boussinesq | 1 | 분산 source + tridiag | 중 | PCR |
| COULWAVE | 2 | 고차 분산 (Pass3A/B 보조 + za·S·T·E·vort) | 최고 | PCR (velocity↔flux 환산 추가) |

ARCHITECTURE.md:67은 COULWAVE를 "higher-order mode"로 규정. 정확도↑ ↔ 비용↑ 트레이드오프: COULWAVE는 매 step 보조패스 2회 + 3D 텍스처 packing + 4차 η차분으로 추가 비용을 진다. **정확한 분산 정확도 차수·적용 수심범위(deep water 한계 등)는 WGSL에서 환원 불가 — 원논문(Lynett-Liu COULWAVE) 참조.** 코드는 어떤 모드가 "언제 더 정확한지" 정량 기준을 담지 않는다(physics는 방정식 유도에 있음).

코드-검증 사실 vs 논문 필요 구분:
- **코드 검증**: 모드 분기 메커니즘, 보조패스 출력 변수, 3D layer 맵, tridiag 계수 형태, PCR velocity↔flux 환산, 현재 2차 차분(4차는 주석 비활성).
- **논문 필요**: 분산 관계 정확도 차수, multi-layer/higher-order Boussinesq 유도, za=`(1+α)H-d`의 물리적 의미(reference velocity 고도)와 최적 α, deep-water 적용한계.

---

## 5. Cross-link

- 표준 분산 모드 (NLSW_or_Bous==1) 및 PCR 기본: [celeris-boussinesq-solver.md](celeris-boussinesq-solver.md)
- 타임스텝 패스 그래프·모드 분기: [celeris-pipeline-graph.md](celeris-pipeline-graph.md)
- COULWAVE 방정식 유도·차수·계보: [`../web-refs/celeris-coulwave-theory.md`](../web-refs/celeris-coulwave-theory.md)
