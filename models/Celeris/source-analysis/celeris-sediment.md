---
title: "Celeris-WebGPU 표사·지형변화 — SedTrans Pass1/Pass3 + UpdateBottom"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/shaders/SedTrans_*.wgsl + js/Handler_SedTrans_*.js 직접 read. 활성 variant는 Handler/main.js dispatch로 확인. 라인 인용 소스 기준. 2026-06-15."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
---

> 상위: [../README.md](../README.md) · 파이프라인 그래프: [celeris-pipeline-graph.md](celeris-pipeline-graph.md)
> 전용 형태변화 대조군: [../../XBeach/](../../XBeach/) (full morphodynamics).
> 본 노트는 **옵션 서브시스템**(config `useSedTransModel`)으로, 하이드로 파이프라인에 끼워지는 부유사 + 소류사 + 지형변화(Exner) 모듈을 다룸.

## 0. 개요

표사 모듈은 단일 부유사 클래스(Class 1)에 대한 **농도 이류·확산 + 픽업/침강 closure**와, 소류사 MP&M 항, 그리고 이를 받아 바닥고를 갱신하는 **Exner형 질량보존**으로 구성. config `useSedTransModel == 1`일 때만 dispatch (default `0`, `constants_load_calc.js:85`). 활성화 시 매 시간스텝 하이드로 패스 사이에 3개 GPU 패스가 삽입된다:

| 패스 | 셰이더(활성) | 삽입 위치 | 산출 |
|---|---|---|---|
| SedTrans_Pass1 | `SedTrans_Pass1.wgsl` | Pass1 직후, Pass2 전 | 셀면 농도 재구성 `txSed_C1..C4` |
| SedTrans_Pass3 | `SedTrans_Pass3.wgsl` | Pass3 직후 | 새 농도 `txNewState_Sed`, `erosion_Sed`, `depostion_Sed` |
| SedTrans_UpdateBottom | `SedTrans_UpdateBottom.wgsl` | corrector 후, gradient shift 전 | `txBottom` 갱신 + near-dry/tridiag 재계산 |

## 1. 하이드로 파이프라인 결합 (insertion points)

`main.js`의 메인 루프(predictor + corrector). 모든 호출이 `if(calc_constants.useSedTransModel == 1)`로 게이트됨.

- **Pass1 → SedTrans_Pass1**: `js/main.js:1898-1901` (predictor), `js/main.js:2032-2035` (corrector). Pass1(플럭스/셀면 재구성) 직후 Pass2 전에 농도를 셀면 재구성. Pass2는 `useSedTransModel`을 uniform offset 28로 받아(`js/main.js:847,1627`) 표사 플럭스 `txXFlux_Sed/txYFlux_Sed`를 계산.
- **Pass3 → SedTrans_Pass3**: `js/main.js:1943-1946`. Pass3(하이드로 적분) 직후, `dU_by_dt_Sed → predictedGradients_Sed` 복사 동반. BoundaryPass에서 `txNewState_Sed`도 경계처리(`js/main.js:1953-1955`).
- **UpdateBottom**: `js/main.js:2133-2143`. corrector step 완료 후, gradient/state shift 직전. 바닥 변화 → near-dry → (Bous일 때) tridiag 순서로 갱신.

각 패스는 `runComputeShader_EncStack`로 command encoder에 스택됨. 즉 하이드로 패스와 같은 encoder 안에서 순차 dispatch (별도 frequency 게이트 없음 — 매 스텝).

## 2. 수송식 (transport formulation)

### 2.1 SedTrans_Pass1 — 셀면 농도 재구성

하이드로 Pass1과 동일한 MinMod 제한 MUSCL 재구성을 농도 상태벡터 4성분에 적용. `txState_Sed`의 x/y/z/w 4채널 각각에 대해 `Reconstruct(west, here, east)`로 동/서·남/북 면값 생성(`shaders/SedTrans_Pass1.wgsl:98-112`). 이후 국소 수심으로 나눠 농도화:

```
divide_by_h = 2h / (h² + max(h², epsilon_c))      // SedTrans_Pass1.wgsl:123
c_i = divide_by_h * hc_i                           // :124-127
```

`epsilon_c`는 셀면 수심차(`dB_max`)로 하한(`:122`) — 천수/육상 전이에서 0 나눗셈 방지. 결과 `txSed_C1..C4`(4 셀면 농도)로 저장(`:129-132`). `TWO_THETAc = 2.0` 고정(상류화 전이 코드는 주석처리, `:96`).

### 2.2 SedTrans_Pass3 — 농도 적분 + 픽업/침강 closure

부유사 농도 보존식을 플럭스 발산 + 소스항으로 적분.

**소스항(픽업/침강)** — 바닥전단·Shields 기반:

```
divide_by_h    = 2·(h/H₀) / ((h/H₀)² + max((h/H₀)², 1e-6)) / H₀   // :124  (H₀=base_depth)
f              = isManning? 9.81·n²·|divide_by_h|^(1/3) : friction  // :127-131
local_speed    = sqrt(u² + v²)                                      // :138
shear_velocity = sqrt(f)·local_speed                               // :139
shields        = shear_velocity²·sedC1_shields                     // :140
```

`sedC1_shields = 1/((s-1)·g·d50)` (무차원화 계수, `constants_load_calc.js:510`; `s = sedC1_denrat = 2.65`, `d50` mm→m). 즉 `shields`는 `τ/((ρs-ρ)g d50)` 형태의 Shields 수에 해당.

**부유사 침식(entrainment):** 임계 Shields 초과 시

```
erosion = sedC1_erosion · (shields - sedC1_criticalshields) · local_speed   // :143-145 (음수면 0)
```

`sedC1_erosion = sedC1_psi · (d50)^(-0.2)` (`constants_load_calc.js:508`, ψ=5e-5 기본). hard-bottom 잔여깊이 `B - hardbottom < delta`면 침식 0 (`:147-151`) — 비침식층 보호.

**소류사 (Meyer-Peter–Müller):** 4 이웃셀에서 각 방향 소류사 플럭스를 계산하고 발산을 취함:

```
bedload = sedC1_bedloadMPM · (shields - shields_cr)^1.5          // :165,178,191,204
bedload_X = bedload · u/|U| ,  bedload_Y = bedload · v/|U|
bedload_erosion = ½·(bedload_right_X - bedload_left_X)/dx
                + ½·(bedload_up_Y   - bedload_down_Y)/dy          // :209
```

`sedC1_bedloadMPM = 8·sqrt(g·(s-1)·d50³)` (`constants_load_calc.js:512`) — 고전적 MPM `q_b = 8(θ-θ_cr)^1.5` 계수와 일치. 소류사는 **부유사 소스항에는 더하지 않고**(`:215` 주석 명시), bed-update용으로만 `erosion_Sed`에 합산(`:239`).

**침강(deposition):** fall velocity × 농도, 가용량 상한:

```
deposition = min(2·C_here, h·(1-n))·sedC1_fallvel               // :212-213
```

`sedC1_fallvel`은 자연입자 항력식(A=25,B=1.25)으로 d50에서 도출(`constants_load_calc.js:514-522`).

**적분(소스 + 플럭스 발산):**

```
source_term = (erosion - deposition)·divide_by_h               // :215 (소류사 제외)
d_by_dt = (xflux_west-xflux_here)/dx + (yflux_south-yflux_here)/dy + source_term  // :217
```

시간적분은 하이드로와 동일한 Adams–Bashforth/Moulton (timeScheme 0 / pred 1 / corr 2, `:224-233`). 음농도 클램프(`:235`). 산출: `txNewState_Sed`(농도), `erosion_Sed = erosion·divide_by_h + bedload_erosion`(bed-update용), `depostion_Sed = deposition·divide_by_h`(`:237-240`).

> **closure 출처 주의:** 침식식 `ψ·d50^(-0.2)·(θ-θ_cr)·|U|`와 fall-velocity 항력식의 정확한 원논문/계수 유도는 소스에 인용 없음. **정확한 표사식은 원논문/config 참조** (Lynett 그룹 Celeris 표사 문헌). 코드가 *계산하는 것*은 위에 정확히 전사. MPM 소류사·Shields 무차원화는 표준형과 일치 확인.

### 2.3 확산항 (현재 비활성)

수평 난류확산(`sedTurbDispersion` 배경 + `sedBreakingDispersionCoef`×breaking eddy viscosity) 코드는 `SedTrans_Pass3.wgsl:102-119`에 **전부 주석처리**되어 있음. 즉 현재 활성 빌드는 **이류 + 픽업/침강만**, 명시적 확산 없음. config 키(`sedTurbDispersion=0.01`, `sedBreakingDispersionCoef=0.1`, `constants_load_calc.js:91-92`)는 uniform으로 전달되나 셰이더에서 미사용.

## 3. 지형변화 (morphology) — UpdateBottom

`SedTrans_UpdateBottom.wgsl`은 침식−침강 차를 공극률로 보정한 **Exner형 질량보존**으로 바닥고를 갱신:

```
dB_here = dt·(e_here - d_here)/(1 - sedC1_n)        // :84  (침식 양수 = 깊이↑ = 고도↓)
B_new   = B_here - dB                                // :115 (B는 고도, 침식 시 고도 감소)
dB_cumulative = B_new - txBottomInitial             // :117 (누적 변화 추적)
```

`e_here`는 부유사 픽업 + 소류사 발산(`erosion_Sed`), `d_here`는 침강. 면값은 인접 평균(`:78-86`)으로 j+½, i+½ 성분 구성(`dB` vec4). `1-n` (n=porosity 0.40)으로 나누는 것이 Exner의 퇴적층 부피↔질량 변환. 경계 근처는 선형 ramp로 표사 억제(`:90-105`, boundary_type==2일 때 가장자리 10셀). hard-bottom 하한도 vec4 구성(`:107-114`).

산출: `txtemp_SedTrans_Botttom`(새 B), `txtemp_SedTrans_Change`(누적). main.js에서 `txBottom`/`txBotChange_Sed`로 복사(`js/main.js:2135-2136`).

### 3.1 바닥 변경 후 near-dry + tridiag 재계산 이유

`txBottom`(수심/바닥고)은 하이드로 코어의 **near-dry 셀 판정**과 **Boussinesq 암시항의 tridiagonal 계수**에 직접 들어간다. 바닥고가 바뀌면:

1. **Updateneardry** 재실행 (`js/main.js:2137-2138`) — 건습 경계·국소 수심 한계가 변했으므로 near-dry mask/계수 재산정.
2. **UpdateTrid** 재실행 (`js/main.js:2139-2142`) — **단, `NLSW_or_Bous == 1`(Celeris Boussinesq)일 때만**. tridiag 계수는 수심 함수이므로 분산항 암시해를 위해 갱신 필요. NLSW는 암시항이 없어 skip (코드 주석 명시).

이 갱신을 빠뜨리면 다음 스텝의 tridiag 솔버가 옛 수심 계수를 쓰게 되어 분산해가 일관성을 잃는다.

## 4. 활성 vs 레거시 variant

`main.js`가 fetch하는 셰이더 파일로 활성본 확정:

- `SedTrans_Pass1.wgsl` — `js/main.js:1348` ✅ 활성
- `SedTrans_Pass3.wgsl` — `js/main.js:1349` ✅ 활성
- `SedTrans_UpdateBottom.wgsl` — `js/main.js:1361` ✅ 활성

**비활성(레거시):**

- `SedTrans_Pass3_old.wgsl` — fetch 없음. 구버전.
- `SedTrans_Pass3_wBedUpdate.wgsl` — fetch 없음. Pass3 안에서 bed update까지 합친 통합 실험본(현재는 UpdateBottom으로 분리). **비활성**.
- `SedTrans_UpdateBottom_testing.wgsl` — fetch 없음. **비활성** 실험본.

활성 Pass3는 bed update를 분리(`erosion_Sed`/`depostion_Sed`만 출력)하고, UpdateBottom이 별도 패스로 받는 구조 — `_wBedUpdate` 통합본이 아님이 dispatch로 확인됨.

## 5. XBeach 대조 (cross-link)

전용 형태변화 모델은 [../../XBeach/](../../XBeach/) 참조. 차이:

| 항목 | Celeris SedTrans | XBeach |
|---|---|---|
| 위치 | 옵션 GPU 패스, 단일 부유사 클래스 | 핵심 morphodynamics 엔진 |
| closure | 단순 Shields 픽업 + MPM 소류사 + 단일 fall-vel | 다입경·avalanching·bed slope·groundwater 등 |
| 확산 | 현재 비활성(주석처리) | 본격 advection-diffusion |
| 용도 | **실시간 스크리닝 / 정성 경향** | 정량 형태변화 예측 |

Celeris 표사는 실시간 브라우저 시뮬레이터의 **경량·스크리닝 지향** 부가기능. 정량 morphology가 필요하면 XBeach를 정본으로 사용하고 Celeris는 빠른 시나리오 탐색에 쓰는 것이 적절.

---

### 인용 요약
- 셀면 재구성: `shaders/SedTrans_Pass1.wgsl:98-132`
- Shields/픽업/MPM/침강/적분: `shaders/SedTrans_Pass3.wgsl:122-240`
- Exner bed update: `shaders/SedTrans_UpdateBottom.wgsl:84-120`
- closure 파라미터 유도: `js/constants_load_calc.js:85-92,508-522`
- 파이프라인 삽입: `js/main.js:1898-1901,1943-1946,2133-2143`
- 활성 셰이더 fetch: `js/main.js:1348-1361`
