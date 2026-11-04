---
title: "Celeris 분산 방정식 계보 — Madsen(모드1) vs COULWAVE 완전비선형(모드2) + S/T/E 항 매핑"
model: Celeris
citation_status: verified
source: "모드 정의·계수·S/T/E/F/G 항은 소스 직접 read(constants_load_calc.js:36-38, Pass3A/3B/Pass3_COULWAVE.wgsl, Pass3_Bous.wgsl, 2026-06-15). 원논문 서지(권·호·페이지·DOI)는 WebSearch landing-page 확인. 단, 코드↔논문 식 동등성은 '표준형 일치' 수준의 구조 식별이며 각 논문 유도 본문 정독은 아님(명시)."
note_date: 2026-06-15
last_source_check: "2026-11-04 (recovery 대조 반영)"
verification_method: "2026-11-04 Celeris recovery 대조 보고서 반영"
source_scope: Celeris-WebGPU/js, Celeris-WebGPU/shaders
---

# Celeris 분산 방정식 계보 + COULWAVE 항 매핑

> 소스 분석 [`../source-analysis/celeris-coulwave.md`](../source-analysis/celeris-coulwave.md)가 "원논문 참조"로 미룬 항목(분산 차수·z_α reference velocity·S/T/E grouping 식대응)을 코드 정독으로 채운 노트.
>
> ⚠️ **2026-06-15 정정**: 이 노트의 이전 판은 COULWAVE를 "Lynett-Liu 2004 **2층(two-layer)** 모델, kh≈6 deep-water"로 규정했으나 **소스 정독 결과 틀림**. Celeris는 **단일 reference velocity z_α(single-layer)**만 쓴다(`Pass3A_COULWAVE.wgsl:44` za 단일값). 코드의 "COULWAVE equations"는 **단일층 완전비선형(fully-nonlinear) 확장 Boussinesq**이며, 2층 모델은 **구현돼 있지 않다**. 아래는 그 정정판.

---

## 0. 핵심 정정 — 모드는 "단·다층"이 아니라 "비선형 차수"로 갈린다

`js/constants_load_calc.js:36` 주석이 모드를 직접 규정한다 (verbatim):

```
NLSW_or_Bous: 0,  // Choose 0 for Non-linear Shallow Water (NLSW),
                  // 1 for Madsen Boussinesq,
                  // 2 for Fully Non-linear Boussinesq (COULWAVE equations)
```

| 모드 | 셰이더 | 방정식 | 분산 | 비선형 | reference velocity |
|---|---|---|---|---|---|
| **0 NLSW** | `Pass3_NLSW` | 비선형 천수 | 없음 | 완전 | — (depth-avg) |
| **1 Bous** | `Pass3_Bous` | **Madsen & Sørensen** enhanced Boussinesq | B-enhanced (B=1/15) | **약비선형(weakly)** | 없음 (정수심 d 기반) |
| **2 COULWAVE** | `Pass3_COULWAVE` | **완전비선형 확장 Boussinesq** ("COULWAVE equations") | Nwogu z_α | **완전비선형(fully)** | 단일 z_α (α=−0.531) |

즉 **모드 1→2의 격상은 "비선형 차수"**(약→완전)이지 "단층→다층"이 아니다. 둘 다 단일층·O(μ²) 분산(대략 kh≲3 intermediate water)이다. "higher-order"는 *Bous(약비선형) 대비 완전비선형*의 의미.

근거(소스):
- 모드 1 `Pass3_Bous.wgsl`는 `Bcoef`(=1/15)·`d_here`·`d2_here`·`d3_here`만 사용, `Bous_alpha`(za) **미참조**(grep 0건) → 정수심 기반 Madsen 형. (`Pass3_Bous.wgsl:272-286`)
- 모드 2 `Pass3_COULWAVE`는 `za_here`·`eta_here`·속도구배 곱(S,T) 사용 → 순간 총수심·자유표면 의존 완전비선형. (`Pass3_COULWAVE.wgsl:336-372`)

`Accuracy_mode`와 방정식 모드는 독립 설정이다 (`js/constants_load_calc.js:36–39`; `js/main.js:1540–1571`). 모드 2는 단일 기준 고도를 쓰는 COULWAVE 계열이다. `Bous_alpha`의 선언값은 `-0.531`이다 (`js/constants_load_calc.js:38`; `shaders/Pass3A_COULWAVE.wgsl:44`). [11-04 대조 정정]

Tavakkol 2020 p.3 식 (2)–(3)은 모드 1에 대응한다. 모드 1의 젖음·마름 조건과 주기 경계 조건은 `shaders/Pass3_Bous.wgsl:142–149,181–193`에 있다. 구체적인 현재 식 차이는 [Tavakkol 2017 대조 보고서](../../../_staging/recovery/compare/celeris-tavakkol2017-vs-code.md)의 CP1-023·031·055·058에 연결한다. [11-04 대조 정정]

---

## 1. 원논문 (verified 서지)

### 1.1 모드 1 (Bous) — Madsen & Sørensen 1992
- **Madsen, P.A., Sørensen, O.R. (1992)** "A new form of the Boussinesq equations with improved linear dispersion characteristics. Part 2. A slowly-varying bathymetry." *Coastal Engineering* **18**(3-4):183-204. DOI: [10.1016/0378-3839(92)90019-Q](https://doi.org/10.1016/0378-3839(92)90019-Q).
- (Part 1: Madsen, Murray, Sørensen (1991) *Coastal Engineering* **15**:371-388 — 평탄지형 유도.)
- B 계수로 선형분산을 Padé[2,2]에 맞춰 향상. **코드 `Bcoef = 1/15`** (`constants_load_calc.js:37`, "optimum value for this set of equations")가 이 B. dispersive 항이 정수심 d의 d²·d³로 스케일(`Pass3_Bous.wgsl:272-286`).

### 1.2 모드 2 (COULWAVE) — 완전비선형 확장 Boussinesq 계보

코드가 구현한 단일층 완전비선형 식의 이론 계보(아래 셋의 표준형):

- **Nwogu, O. (1993)** "Alternative form of Boussinesq equations for nearshore wave propagation." *J. Waterway, Port, Coastal, and Ocean Engineering* **119**(6):618-638. DOI: [10.1061/(ASCE)0733-950X(1993)119:6(618)](https://doi.org/10.1061/(ASCE)0733-950X(1993)119:6(618)). — **z_α reference velocity**(속도변수를 임의 고도 z=z_α에서 취해 분산 개선). 코드의 `Bous_alpha=-0.531`이 Nwogu 최적값, `za` 텍스처의 근거.
- **Wei, G., Kirby, J.T., Grilli, S.T., Subramanya, R. (1995)** "A fully nonlinear Boussinesq model for surface waves. Part 1." *J. Fluid Mech.* **294**:71-92. DOI: [10.1017/S0022112095002813](https://doi.org/10.1017/S0022112095002813). — Nwogu z_α를 **완전비선형**으로 확장(약비선형 가정 제거). 코드 S/T/E/F/G 항의 표준형(§3).
- **Lynett, P.J., Wu, T.-R., Liu, P.L.-F. (2002)** "Modeling wave runup with depth-integrated equations." *Coastal Engineering* **46**(2):89-107. DOI: [10.1016/S0378-3839(02)00043-1](https://doi.org/10.1016/S0378-3839(02)00043-1). — **COULWAVE**(Cornell Univ. Long and Intermediate Wave) 단일층 완전비선형 + moving-shoreline runup. 코드 "COULWAVE equations"의 직접 출처 계열.

### 1.3 ❌ 구현 안 됨 — 2층/다층 (참고용 보존)
- **Lynett, P., Liu, P.L.-F. (2004)** "A two-layer approach to wave modelling." *Proc. R. Soc. A* **460**(2049):2637-2669. DOI: [10.1098/rspa.2004.1305](https://doi.org/10.1098/rspa.2004.1305). — 2층 적분으로 분산을 **kh≈6**(deep water)까지 확장. COULWAVE 패키지의 다층 옵션이나 **Celeris-WebGPU에는 미구현**(소스에 단일 za뿐). 향후 multi-layer가 추가되면 이 논문이 근거가 될 것.

---

## 2. COULWAVE 모드 ≈ FUNWAVE-TVD 동일 방정식족

모드 2의 단일층 완전비선형 확장 Boussinesq(Nwogu z_α + Wei-Kirby 완전비선형)는 **FUNWAVE-TVD가 푸는 식과 같은 클래스**다(Shi et al. 2012 = Wei-Kirby fully-nonlinear). 차이는 *물리 방정식*이 아니라 *수치/운용*:

| | Celeris COULWAVE(모드2) | FUNWAVE-TVD |
|---|---|---|
| 방정식 | 단일층 완전비선형 확장 Boussinesq | 동일 (Wei-Kirby/Chen) |
| reference velocity | z_α (Nwogu, α=−0.531) | z_α (동일 계보) |
| 분산 음해 | PCR (GPU 텍스처) | tridiagonal (Thomas/cusparse) |
| 운용 | 브라우저 실시간 | 배치 MPI HPC |

→ [`../../FUNWAVE/source-analysis/funwave-dispersion-solver.md`](../../FUNWAVE/source-analysis/funwave-dispersion-solver.md). **Celeris의 "Bous"(모드1, Madsen 약비선형)는 FUNWAVE보다 낮은 비선형 차수**, "COULWAVE"(모드2)가 FUNWAVE급.

---

## 3. S/T/E/F/G 항 ↔ 완전비선형 확장 Boussinesq 매핑 (코드 정독)

소스 분석 노트가 미룬 핵심. `Pass3B_COULWAVE.wgsl`이 만드는 보조항을 식 의미로 식별(좌=코드, 우=물리). **좌변은 코드에서 직접 검증, 우변 식의미는 완전비선형 확장 Boussinesq 표준형과의 구조 일치**(각 논문 유도 본문 정독은 아님 — §source).

### 3.1 두 기본 발산 (auxiliary divergences)
- `S = dudx + dvdy` = **∇·u_α** (reference velocity 발산). `Pass3B_COULWAVE.wgsl:170`.
- `T = dhudx + dhvdy` = **∇·(d·u_α)** (정수심×reference velocity 발산). `:171`. (`du=u·d`, `Pass3A:80`)
- 이 둘이 완전비선형 확장 Boussinesq에서 분산항을 구성하는 두 정준 보조변수.

### 3.2 연속식(질량) 분산보정 E1/E2
`Pass3B_COULWAVE.wgsl:184-188`:
```
temp2 = 1/6(η² − η·d + d²) − 1/2·za²
temp3 = 1/2(η − d) − za
E1 = H·(temp2·∂S/∂x + temp3·∂T/∂x)   ;   E2 = H·(temp2·∂S/∂y + temp3·∂T/∂y)
```
- `temp2`,`temp3` = **완전비선형 Boussinesq 질량플럭스의 고전 분산계수**(z_α²/2 및 (η²−ηd+d²)/6 형). 약비선형(Nwogu/Madsen)이면 η→0 극한으로 환원.
- Pass3_COULWAVE에서 `E_src = ∂E1/∂x + ∂E2/∂y`로 **연속식 우변 분산항**이 됨 (`Pass3_COULWAVE.wgsl:372`).

### 3.3 운동량 분산 source (Psi1 = Fsrc/Gsrc, explicit) 과 시간미분항 (Psi2, implicit 후보)
`Pass3_COULWAVE.wgsl:336-372` (x성분 Fsrc; y성분 Gsrc 동형):

| 코드 항 | 식 의미 |
|---|---|
| `temp1 = u·(∂E1/∂x+∂E2/∂y)` | reference velocity가 질량분산을 advect |
| `temp2 = E·[½(za²−η²)∂S/∂x + (za−η)∂T/∂x − ∂η/∂x·(ηS+T)]` | 표면진동(E=∂(·)/∂t류) × 분산구배 결합 |
| `temp3 = −∂(EzST)/∂x`, `EzST=E·(ηS+T)` | 비정상 분산항 |
| `temp4 = −∂(uSxvSy)/∂x`, `uSxvSy=½(za²−η²)(u·Sx+v·Sy)` | 분산의 비선형 이류 |
| `temp5 = −∂(uTxvTy)/∂x`, `uTxvTy=(za−η)(u·Tx+v·Ty)` | 분산의 비선형 이류 |
| `temp6 = −½∂(TzS2)/∂x`, `TzS2=(ηS+T)²` | 분산의 2차 비선형 자기곱 |
| `temp7A/B = ∓v·∂za/∂{x,y}·(∂T+za·∂S)` | z_α 공간변화(가변지형) 보정 |
| `temp7C = −vort·[…∂T + …∂S]` | 와도(vorticity) 결합 분산 |

→ `Fsrc = temp1+temp2+h·(temp3+…+temp7C)` = **운동량식 완전비선형 분산 source(explicit, Psi1)**.
- `F_star/G_star`(`:367-370`) = 분산항의 시간미분 대상 → `Psi2 = (3F*−4F*_old+F*_oldold)/(2dt)` **2차 후방차분(BDF2)** (`:374-378`). 이 F_star만 implicit tridiagonal로 남고 나머지(Fsrc)는 explicit AB.
- `vort_here = ∂v/∂x − ∂u/∂y` (`Pass3B:199`) — 완전비선형이라 와도 보존항이 명시됨.

### 3.4 외부 식 대조와 E 정의 [11-04 대조 정정]
- 위 매핑은 코드 형태와 완전비선형 Boussinesq 표준형의 구조 식별이다. COULWAVE 보조항의 계수는 코드 원문을 인용한다. 외부 이론식과의 동일성을 이름만으로 확정하지 않는다 (`shaders/Pass3B_COULWAVE.wgsl:170–200`; [최종 근거 CD2-444](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD2.md)). [11-04 대조 정정]
- E의 코드 정의는 이미 저장된 eta 시간 우변 `dU_by_dt.x`다 (`shaders/Pass3B_COULWAVE.wgsl:191`; `shaders/Pass3_COULWAVE.wgsl:486–488,521`). 예측 B는 직전 단계 값을 읽는다 (`js/main.js:2663,2679`). 보정 B는 예측 Pass3 값을 읽는다 (`js/main.js:2797,2812`). [11-04 대조 정정]

---

## 4. 코드↔이론 매핑 요약 (소스 노트 미결 해소표)

| 소스 노트가 미룬 것 | 답 (이 노트) |
|---|---|
| 모드 2가 왜 "higher-order"인가 | **단·다층 아님**. Madsen 약비선형(모드1) 대비 **완전비선형**(모드2). 둘 다 단일층 O(μ²) (§0) |
| z_α(za) 물리 | Nwogu 1993 reference velocity 고도, α=−0.531 최적 (§1.2) |
| S, T 정체 | S=∇·u_α, T=∇·(d·u_α) — 완전비선형 Boussinesq 두 정준 보조변수 (§3.1) |
| E1/E2 grouping | 연속식 분산플럭스 계수(temp2/temp3 = 고전 FN 질량분산계수) (§3.2) |
| F/G grouping | 운동량 완전비선형 분산 source(이류·자기곱·vorticity·za구배) + BDF2 시간항 (§3.3) |
| 2층/kh≈6/deep-water | **미구현** (단일 za). Lynett-Liu 2004는 패키지 옵션일 뿐 Celeris엔 없음 (§1.3) |

---

## 5. 본 위키 cross-ref

- 코드 구현: [`../source-analysis/celeris-coulwave.md`](../source-analysis/celeris-coulwave.md)
- 표준 분산 모드(모드1)·PCR: [`../source-analysis/celeris-boussinesq-solver.md`](../source-analysis/celeris-boussinesq-solver.md)
- Celeris 공식 논문: [`celeris-official-resources.md`](celeris-official-resources.md)
- 동일 완전비선형 클래스(FUNWAVE): [`../../FUNWAVE/source-analysis/funwave-dispersion-solver.md`](../../FUNWAVE/source-analysis/funwave-dispersion-solver.md)
- 쇄파(Kennedy eddy-viscosity, 공유): [`../source-analysis/celeris-breaking-boundary.md`](../source-analysis/celeris-breaking-boundary.md)


## 문서와 코드 차이 (11-04 대조)

코드는 plynett/plynett.github.io main `ebca435`(2026-07-20)의 Celeris-WebGPU이다. 문서는 같은 커밋의 `docs/`·`README`이다.

코드 인용의 기준 경로는 `models/Celeris/raw/source_code/Celeris-WebGPU/`이다. 결론은 행별 최종 근거의 문장과 인용을 옮긴 AI 정리이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| callflow:RF-022 | E 생산처 | 반영 전 노트 `d8157c80:models/Celeris/web-refs/celeris-coulwave-theory.md:116` 발췌: `` `E = textureLoad(dU_by_dt).x` (`Pass3B:191`) ``. 해당 줄에 E 생산처 설명은 없다(원문 요약). | `shaders/Pass3B_COULWAVE.wgsl:191` `let E = textureLoad(dU_by_dt, idx, 0).x;`<br>`shaders/Pass3_COULWAVE.wgsl:521` `textureStore(dU_by_dt, idx, d_by_dt);`<br>확인한 원문: `d8157c80:models/Celeris/web-refs/celeris-coulwave-theory.md:116`; `shaders/Pass3B_COULWAVE.wgsl:191–195`; `shaders/Pass3_COULWAVE.wgsl:486–488,521`; `js/main.js:2663,2679,2797,2812` | C 문서 누락 | COULWAVE B의 E는 수문 Pass3가 남긴 연속식 우변이다. 읽는 시점은 예측과 보정에서 다르다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) [11-04 전수 검증 정정] |
| docs-source:CD2-479 | eta 시간 우변 | 반영 전 노트 `d8157c80:models/Celeris/web-refs/celeris-coulwave-theory.md:116` 발췌: `` `E = textureLoad(dU_by_dt).x` (`Pass3B:191`) ``. 해당 줄에 E 생산처 설명은 없다(원문 요약). | `shaders/Pass3B_COULWAVE.wgsl:191` `     let E = textureLoad(dU_by_dt, idx, 0).x; `<br>`shaders/Pass3_COULWAVE.wgsl:488` `     let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term + vorticity_dissipation; `<br>`shaders/Pass3_COULWAVE.wgsl:521` `     textureStore(dU_by_dt, idx, d_by_dt); `<br>`js/main.js:2663` `                     runComputeShader(device, Pass3B_Coulwave_uniformBuffer, Pass3B_Coulwave_uniforms, Pass3B_Coulwave_Pipeline, Pass3B_Coulwave_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY); `<br>`js/main.js:2679` `                     runComputeShader_EncStack(device, commandEncoderStack, Pass3_uniformBuffer, Pass3_uniforms, Pass3_Pipeline_Bous, Pass3_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY); `<br>확인한 원문: `d8157c80:models/Celeris/web-refs/celeris-coulwave-theory.md:116`<br>`shaders/Pass3B_COULWAVE.wgsl:191`<br>`shaders/Pass3_COULWAVE.wgsl:486–488,520–522`<br>`js/main.js:2662–2685,2795–2815` | C 문서 누락 | E의 코드 정의는 이미 저장된 eta 시간 우변 dU_by_dt.x다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD2.md)) [11-04 전수 검증 정정] |
