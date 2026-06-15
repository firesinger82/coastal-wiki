---
title: "Celeris-WebGPU FV 재구성·Riemann flux — Pass0/Pass1/Pass2 (HLLC·HLLEM)"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/shaders/Pass{0,1,1_HighOrder,2,2_HighOrder_HLLC,2_HighOrder_HLLEM}.wgsl 직접 read + Handler_Pass*.js. 라인·수식 인용 소스 기준. 2026-06-15."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
---

> 상위: [../README.md](../README.md) · 파이프라인 전체: [celeris-pipeline-graph.md](celeris-pipeline-graph.md) · 분산항(Pass3 이후): [celeris-boussinesq-solver.md](celeris-boussinesq-solver.md)
> 이 노트의 범위: **유한체적 재구성 + Riemann flux** 서브시스템 = NLSW·Boussinesq·COULWAVE 모든 모드가 공유하는 명시적 쌍곡(hyperbolic) 코어. Pass0(near-dry 준비) → Pass1(cell-center→face 재구성) → Pass2(face flux). Pass3는 이 flux를 발산(divergence)으로 적분(다른 노트).

이 위키의 다른 단언과 마찬가지로, 아래는 모두 WGSL 소스가 실제로 보여주는 것만 기술한다. 모호한 부분은 명시했다.

---

## 0. 데이터 레이아웃 규약 (전 패스 공통)

상태 텍스처 `txState`의 채널: `.x = w`(자유수면 η), `.y = hu`, `.z = hv`, `.w = hc`(스칼라/농도 수송량). 바닥 `txBottom.z = B`(셀 중심 bed). 수심 `h = w - B`.

face-state 텍스처 `txH/txU/txV/txC`의 4채널은 **셀의 4개 face**를 담는다 — 규약은 `(N, E, S, W) = (.x, .y, .z, .w)`. Pass1에서 `w = vec4(wzx.y, wwy.y, wzx.x, wwy.x)` (`Pass1.wgsl:134`)로 조립되는데, `wzx`는 S/N 방향 재구성 `vec2(west=south, east=north)`, `wwy`는 W/E 방향 `vec2(west, east)`이므로:
- `.x = wzx.y = north`, `.y = wwy.y = east`, `.z = wzx.x = south`, `.w = wwy.x = west`.

이 N/E/S/W 순서가 Pass2에서 face flux를 셀 경계에 맞춰 읽는 방식의 전제다.

---

## 1. Pass0 — 이웃 수심 / near-dry 준비 (`Pass0.wgsl`)

값싼 prepass. 각 셀의 4 이웃 **수심**만 계산해 `txHnear`에 적재 (`Pass0.wgsl:57`).

- 이웃 인덱스는 도메인 끝에서 clamp (`min/max`, `Pass0.wgsl:27-30`) — 물리 BC 아님(물리 BC는 BoundaryPass).
- 각 이웃 free-surface(`in_*`, `.x`)와 bed(`B_*`, `.z`)를 읽어 `h_* = in_* - B_*` (`Pass0.wgsl:46-49`).
- 출력 `h_vec = (north, east, south, west)` (`Pass0.wgsl:52-55`). 채널 순서는 Pass2가 읽는 규약과 일치(공식 doc `docs/source/shaders/Pass0_wgsl.md`도 동일 명시).

**왜 분리하나**: wet/dry 판정을 무거운 재구성·flux 로직 바깥으로 빼서, Pass2가 `minH = min(4 이웃 수심)` 한 번으로 near-dry 분기를 결정하게 한다 (`Pass2.wgsl:105`, `Pass2_HighOrder_HLLC.wgsl:184`). 주석 라인(`// min(h_here, h_north)`, `Pass0.wgsl:52-55`)을 보면 원래 `h_here`와의 min을 의도했으나 현재는 이웃값만 저장한다 — 이 차이는 코드상 그대로다.

---

## 2. Pass1 — cell-center → face state 재구성

입력 `txState`(보존량) → 출력 face별 `H,U,V,C`(원시 변수). 표준 `Pass1.wgsl`과 `Pass1_HighOrder.wgsl` 두 종, `Accuracy_mode`로 선택 (`js/main.js:1322-1327`: `==1`이면 HighOrder).

### 2.1 MinMod slope limiter (표준, 2nd-order)

핵심은 `Reconstruct()` (`Pass1.wgsl:39-52`):

```
z1 = TWO_THETAc*(here - west)
z2 = (east - west)
z3 = TWO_THETAc*(east - here)
dx_grad_over_two = 0.25 * MinMod(z1, z2, z3)
out_west = here - dx_grad_over_two
out_east = here + dx_grad_over_two
```

`MinMod(a,b,c)` (`Pass1.wgsl:31-39`)는 세 인자가 모두 같은 부호일 때만 절댓값 최소를 반환, 아니면 0 (TVD 제한). 이것이 **generalized MinMod / θ-limiter** (Kurganov–Petrova 계열): θ=`TWO_THETA/2`로 중심차(z2)와 한쪽 차(z1,z3)를 비교한다. `0.25*z2 = 0.25*(east-west) = 0.5*central slope`이므로 `dx_grad_over_two`는 셀 중심에서 face까지의 반쪽 증분. 한계: θ→1(중심차)와 θ→2(완전 upwind 최소소산) 사이를 보간.

**셰일라인 전이**(`Pass1.wgsl:116-118`): 가장 얕은 이웃 수심 `wetdry`로 `rampcoef = clamp(wetdry/(0.02*base_depth), 0,1)`을 만들고
```
TWO_THETAc = TWO_THETA*rampcoef + 2.0*(1-rampcoef)
```
즉 inundation limit(수심 < base_depth/50) 근처에서 θ를 2(완전 upwind)로 끌어올려 안정화.

### 2.2 well-balanced / positivity 처리

- **건-건 short-circuit** (`Pass1.wgsl:85-93`): `h_here ≤ delta` & 4 이웃 모두 ≤ delta면 H/U/V/C에 0 적재 후 즉시 return.
- **수면(w) 재구성 → 수심 clamp** (`Pass1.wgsl:134-136`): face별 `h = w - B = max(w-B, 0)`. **수심이 아니라 자유수면 η를 재구성한 뒤 bed를 빼는** 방식 — lake-at-rest well-balancing의 표준 처리.
- **near-dry 시 edge depth 보호** (`Pass1.wgsl:120-122, 146-147`): `wetdry ≤ epsilon`이면 `dB_max = 0.5*(이웃 bed 차)`. CalcUVC에서
  ```
  divide_by_h = 2h / (h² + max(h², epsilon_c)),  epsilon_c = max(epsilon, dB_max)
  u = divide_by_h * hu
  ```
  이는 `h`로 직접 나누는 대신 desingularized division(Kurganov–Petrova). edge 양단 bed 차보다 작은 국소 수심으로 나누지 않게 한다(주석 `Pass1.wgsl:147`).
- **Froude limiter** (`Pass1.wgsl:152-164`): 면 속도의 최대 Fr이 `Fr_maxallowed = 3/max(1, dBds_max)`를 넘으면 u,v를 `Fr_red`배로 축소. 가파른 경사(>45°)에서 비물리적 가속 억제.

### 2.3 HighOrder (4th-order MUSCL-TVD) 차이 (`Pass1_HighOrder.wgsl`)

- **스텐실 확장**: ±3셀까지 로드(`Pass1_HighOrder.wgsl:161-202`), 표준은 ±1만.
- **분기**: `wetdry ≤ epsilon` 또는 `maxB3 ≥ -epsilon`(스텐실 내 bed가 수면 근처)이면 표준 `Reconstruct`로 fallback (`:263-275`), 아니면 내부점에 `ReconstructMUSCL4` (`:276-304`).
- **`ReconstructMUSCL4`** (`:86-147`): 7점 스텐실 `(z_m3..z3)`로 좌/우 limited slope `shL,shR`를 `calcSlopes`(`:54-84`)로 만든다. `calcSlopes`는 3차차분 보정 `sh = dh - d3/6`을 적용한 4차 정밀 기울기. `dh_max > 0.60`(국소 경사 임계)일 때만 추가 TVD limiter(`ilim_c=1`, `:91-93, 116-134`) 활성, 아니면 무제한(`:135-141`). 최종 face 값:
  ```
  H_right = z0 + (bR1 + 2*bR2)/6
  H_left  = z0 - (2*bL3 + bL4)/6
  ```
  (`:143-144`). 즉 **TVD limiter는 경사가 큰 영역에서만 켜지는 적응형**이며, 평탄역에선 4차 무제한으로 분산 최소화.
- **face별 positivity** (`Pass1_HighOrder.wgsl:312-335`): 4 face 각각 `h.<ch> < delta`면 그 face의 h/hu/hv/hc를 0으로(표준의 전역 `max(h,0)`보다 face 단위로 세밀). CalcUVC·Froude limiter는 표준과 동일.

FUNWAVE의 4차 MUSCL과 직접 대응(아래 §5).

---

## 3. Pass2 — Riemann flux (txXFlux/txYFlux 형성)

입력: Pass1의 face state `txH/txU/txV/txC` + `txHnear`. 출력: x-face flux `txXFlux`, y-face flux `txYFlux` (각 vec4 = [mass, x-mom, y-mom, scalar]). `Accuracy_mode`로 표준 `Pass2.wgsl`(2nd) vs `Pass2_HighOrder_HLLC.wgsl`(4th) 선택 (`js/main.js:1329-1334`).

### 3.0 공통 — face 좌우 상태와 파속 추정

각 셀에서 **자기 face**(`h_here.xy` = N,E)와 **이웃 셀의 맞은편 face**를 읽어 Riemann 좌/우 상태로 삼는다. x-face(East 경계): 좌 = 자기 E면(`h_here.y`), 우 = 동쪽 셀의 W면(`txH(rightIdx).w = hW_east`) (`Pass2.wgsl:71-82`). y-face(North): 좌 = 자기 N면(`.x`), 우 = 북쪽 셀의 S면(`.z`).

파속(공통, 모든 변종 동일):
```
cNE = sqrt(g*h_here);  cW = sqrt(g*hW_east);  cS = sqrt(g*hS_north)
aplus  = max(max(u_here.y + cNE.y, uW_east + cW), 0)      // S_R, x
aminus = min(min(u_here.y - cNE.y, uW_east - cW), 0)      // S_L, x
bplus  = max(max(v_here.x + cNE.x, vS_north + cS), 0)     // S_R, y
bminus = min(min(v_here.x - cNE.x, vS_north - cS), 0)     // S_L, y
```
(`Pass2.wgsl:84-91`, `Pass2_HighOrder_HLLC.wgsl:171-178`, HLLEM `:153-160` 동일). 즉 **Einfeldt식 양측 파속 추정**(±√(gh) 기반), `max(...,0)`/`min(...,0)` clamp으로 한쪽 supersonic 시 upwind로 자연 축소.

### 3.1 표준 Pass2 — 성분별 HLL (`Pass2.wgsl`)

`NumericalFlux(aplus, aminus, Fplus, Fminus, Udiff)` (`Pass2.wgsl:36-42`):
```
(aplus*Fminus - aminus*Fplus + aplus*aminus*Udiff) / (aplus - aminus)   // aplus≠aminus
0                                                                        // else
```
이것이 **고전 2파 HLL flux** (S_R F_L − S_L F_R + S_L S_R ΔU)/(S_R−S_L). 4개 보존성분을 각각 스칼라로 호출 (`Pass2.wgsl:122-134`):
- mass: `F = h·u`, ΔU = `mass_diff_x = hW_east - h_here.y`
- x-mom: `F = h·u²`, ΔU = `P_diff_x`
- y-mom: `F = h·u·v`, ΔU = `Q_diff_x`
- scalar: `F = h·u·c`, ΔU = `phix*(hW_east*cW_east - h_here.y*c_here.y)`

near-dry(`minH ≤ delta`, `Pass2.wgsl:115-120`): `mass_diff` 0으로, `phi=1`. **압력항 누락 주의**: 표준 Pass2의 x-mom flux는 `h·u²`만이고 정수압항 `½g h²`이 여기 없다 — well-balanced 소스항/정수압이 Pass3 또는 reconstruction 단계로 흡수되는 구조(이 노트 범위에선 flux에 `½gh²`가 **없음**을 사실로 기록; 정확한 흡수 위치는 Pass3 노트에서 다룸).

### 3.2 HighOrder HLLC (`Pass2_HighOrder_HLLC.wgsl`, 4th-order 기본)

flux를 성분별 스칼라가 아니라 **vec4 상태벡터**로 처리. face 상태:
```
state_plus_x  = (hW, hW·uW, hW·vW, hW·cW)        // U_R
state_minus_x = (h⁻, h⁻·u⁻, h⁻·v⁻, h⁻·c⁻)        // U_L
Fp_x = state_plus_x * uW_east                     // F_R
Fm_x = state_minus_x * u_here.y                   // F_L
```
(`Pass2_HighOrder_HLLC.wgsl:191-203`).

`HLLC_Flux` (`:71-144`):
1. base HLL: `Fhll = HLL_Flux(...)` (`:81`, vec4판 HLL `:45-66`, DU_flag시 ΔU.x=0).
2. **접촉파속 S\* = Roe 평균 속도** (`:84-95`): `uL=Fminus.x/Uminus.x`, `uR=Fplus.x/Uplus.x`, `uRoe = (√hL·uL + √hR·uR)/(√hL+√hR)`, `S_star = uRoe`.
3. **star 수심**(Toro 공식, `:97-114`): `h_star_L = hL*(aminus-uL)/(S*-aminus)`, `h_star_R = hR*(aplus-uR)/(S*-aplus)`, 분모는 ε-clamp. `blend = 0.5+0.5*sign(S*)`로 S\*≥0이면 L, 아니면 R 채택.
4. **star flux** F\* = F_base + S·(U\* − U_base) (`:131-135`), 여기서 S/U_base/F_base는 blend로 선택된 한쪽.
5. **질량 보정 + anti-diffusion** (`:137-143`): near-dry(`DU_flag==1`)면 `F_final.x = Fhll.x`. 마지막에
   ```
   psi = max(0, 1 - max(|aminus|,|aplus|)/(|uRoe|+1e-6))
   return Fhll + psi*(F_final - Fhll)
   ```
   즉 HLLC star flux를 HLL 위에 `psi`로 blend. **참고**: `psi` 공식상 파속이 클수록 0에 가까워져 사실상 HLL로 수렴하므로, 여기 HLLC 구현은 정통 HLLC라기보다 **HLL + Roe-속도 기반 접촉파 복원(HLLEM류 anti-diffusion)을 HLLC star로 표현한 변종**이다. 코드가 보여주는 한 그렇게 기술한다.

활성 경로(`:206-218`): `xflux = HLLC_Flux(aplus, aminus, ...)`, `yflux = HLLC_Flux(bplus, bminus, ...)`. 주석 처리된 `if(minH≤delta) HLL_Flux` 분기(`:208-212`)가 있으나 현재 **무조건 HLLC** 호출.

### 3.3 HighOrder HLLEM (`Pass2_HighOrder_HLLEM.wgsl`, 존재하나 미사용)

구조는 HLLC와 1:1. `HLLEM_Flux` (`:80-125`):
- base `Fhll`, Roe 속도 `uRoe`(HLLC와 동일 `:93-107`).
- **Roe 선형화 flux**: `Froe = 0.5*(Fplus+Fminus) - 0.5*|uRoe|*ΔU` (`:115`).
- 동일한 `psi = max(0, 1 - wavespeed_max/(|uRoe|+1e-6))` (`:119-121`).
- **return `Fhll + psi*(Froe - Fhll)`** (`:124`) — 접촉 불연속을 복원하는 anti-diffusion.

HLLC와의 실질 차이: HLLC는 Toro star 상태 `U*`를 명시 구성 후 blend, HLLEM은 중앙평균 Roe flux `Froe`를 직접 blend. 둘 다 같은 `psi` 한계함수 사용.

**활성 여부** (`ARCHITECTURE.md:69-72`): `Accuracy_mode==1`(고차)에서 `main.js`는 `Pass2_HighOrder_HLLC.wgsl`만 fetch (`js/main.js:1330-1331`). **HLLEM은 소스에 존재하나 현재 main.js 경로에서 선택되지 않음**(present-but-not-default).

### 3.4 어느 것이 언제 (Accuracy_mode)

| Accuracy_mode | Pass1 | Pass2 |
|---|---|---|
| `0` (2nd-order, 기본 default `constants_load_calc.js:35`) | `Pass1.wgsl` (MinMod θ-limiter) | `Pass2.wgsl` (성분별 HLL) |
| `1` (4th-order) | `Pass1_HighOrder.wgsl` (MUSCL4) | `Pass2_HighOrder_HLLC.wgsl` (HLLC) |
| — | — | `Pass2_HighOrder_HLLEM.wgsl` (미연결) |

(선택 로직 `js/main.js:1322-1334`. cross-ref [celeris-pipeline-graph.md](celeris-pipeline-graph.md).)

### 3.5 sediment flux (옵션)

`useSedTransModel==1`이면 동일 Riemann 솔버로 4 sediment class 수송 flux(`txXFlux_Sed/txYFlux_Sed`)를 추가 계산 (`Pass2.wgsl:139-205`, HLLC `:222-290`). class-1에만 확산항 `-k·h·∇C`가 들어가나, HLLC/HLLEM판은 0-나눗셈 회피를 위해 **확산항을 flux에 합치지 않음**(주석 `Pass2_HighOrder_HLLEM.wgsl:250-251`).

---

## 4. Pass3로의 연결 (flux divergence)

Pass2 출력 `txXFlux`(x-face), `txYFlux`(y-face)는 Pass3에서 **flux 발산**으로 적분된다: 보존형 `∂U/∂t = -(F_{i+½}-F_{i-½})/dx - (G_{j+½}-G_{j-½})/dy + S`. NLSW는 `Pass3_NLSW`, Boussinesq/COULWAVE는 분산 소스항 + 암시적 tridiagonal 보정이 추가된다. 자세한 적분·소스항·분산 처리는 → [celeris-boussinesq-solver.md](celeris-boussinesq-solver.md).

---

## 5. 지배 스킴과 FUNWAVE 대비

Celeris의 명시적 코어는 **hybrid FV(쌍곡)·FD(분산) 보존형 스킴**: 쌍곡항은 유한체적(MUSCL 재구성 + 근사 Riemann), 분산항(Boussinesq)은 유한차분 + 암시 solve. 본 노트의 Pass0-2가 그 FV 절반.

FORTRAN 대응물은 FUNWAVE-TVD의 MUSCL-TVD + Riemann flux: [../../FUNWAVE/source-analysis/funwave-flux-tvd.md](../../FUNWAVE/source-analysis/funwave-flux-tvd.md). 공통점은 (a) 자유수면/수심의 MinMod·MUSCL 재구성, (b) Einfeldt 양측 파속, (c) well-balanced desingularized division. **차이**: FUNWAVE는 **HLL**(2파, 접촉 불연속 미복원)을 쓰고, Celeris는 고차 모드에서 **HLLC/HLLEM류**(Roe-속도 기반 접촉파 anti-diffusion 추가)를 쓴다 — 전단/소용돌이·물질 경계에서 수치 소산이 덜하다. 단 §3.2에서 밝혔듯 Celeris의 HLLC는 `psi` blend로 HLL로 연속 축소되는 변종이라, 정통 Toro HLLC와는 anti-diffusion 형태가 다르다.
