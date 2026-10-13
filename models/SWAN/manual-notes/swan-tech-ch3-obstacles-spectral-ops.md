---
title: "SWAN swantech Ch 3.12-3.13 obstacle 수치처리 + 3.14 σ integration + 3.15 freq transform + 3.16 spectra interpolation verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.12 Numerical treatment of obstacles + §3.13 Crossing of obstacle and grid line + §3.14 Integration over σ + §3.15 Transformation from relative to absolute frequency + §3.16 Interpolation of spectra, doc p.109-113 (Eq 3.70-3.92). WAM interpolation procedure."
citation_status: verified
last_source_check: "2026-10-13 (recovery 대조 반영)"
verification_method: "swantech.pdf (v41.51) §3.12-3.16 직접 read via pdftotext (식 번호 context-verified: obstacle propagation 3.70·line crossing 3.71-73·σ integration trapezoidal+tail 3.74-82·absolute freq 3.83-84·spectra interpolation 3.85-92) + website_markdown node58-62.md LaTeX alt-text. 식 번호는 PDF 번호 (online HTML +43 offset). 2026-10-13 recovery 대조 보고서 R1–R8 반영"
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 3.70-3.92 + FRINTF/FRINTH/PWTAIL/MSC verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md
  - models/SWAN/manual-notes/swan-tech-ch3-qc-curvilinear.md
  - models/SWAN/manual-notes/swan-tech-ch3-breaking-source.md
---

# swantech Ch 3.12-3.16 obstacle 수치 + spectral ops — verified verbatim

> swantech.pdf (v41.51) §3.12-3.16 직접 read. Obstacle 의 **수치 구현**(line crossing + K_t² reduction + reflection) + **spectral 연산**(σ 적분 + 주파수 변환 + spectra interpolation). [swan-tech-ch2-obstacles-diffraction-setup](swan-tech-ch2-obstacles-diffraction-setup.md) (§2.5 물리식)의 numerical 짝.
>
> **식 번호 주의**: PDF 번호 사용 (online HTML +43 offset, 예: obstacle propagation HTML 3.113 = PDF 3.70).

## 1. §3.12 Obstacle 수치처리 (Eq 3.70)

Obstacle = 계산격자 관통 line (Fig 3.7). Stencil grid line 이 obstacle 교차 시 (§3.13 절차) **1차 upwind(BSBT)로 회귀**.

**Transmission**: target 점 0 계산 시, 이웃 점 1 의 기여를 **$K_t^2$ 감소** (연결선이 obstacle 교차 시; power 2 는 $K_t$ 가 파고 기준이라). 점 2 (무교차)는 $K_t=1$.
> 결과는 obstacle 이 같은 grid line 교차하는 한 동일 (길어도 끝이 같은 mesh면 동일). Obstacle 은 **최소 몇 grid line 교차해야 효과** 있음.

곡선좌표 propagation 항 (transmission 반영, §3.10 Eq 3.55 에 $K_{t}^2$ 삽입):
$$\left(\frac{1}{\Delta t} + (D_{x,1}+D_{x,2})c_{x,i,j}^+ + (D_{y,1}+D_{y,2})c_{y,i,j}^+\right)N_{i,j}^+ - \frac{N_{i,j}^-}{\Delta t} - D_{x,1}(c_x K_{t,1}^2 N)_{i-1,j}^+ - D_{y,1}(c_y K_{t,1}^2 N)_{i-1,j}^+ - D_{x,2}(c_x K_{t,2}^2 N)_{i,j-1}^+ - D_{y,2}(c_y K_{t,2}^2 N)_{i,j-1}^+ = S_{i,j}^+ \quad \text{(3.70)}$$

**Reflection**: target 점 0 의 reflected 성분은 **동일 격자점 입사 성분에서** 계산 (수치 부정확하나 step→0 시 수렴). 점 1 기여 = transmission 감소 + 입사 반사로 부분 대체, 점 2 불변.
같은 대상 절점의 입사 성분을 쓰는 식은 일치한다. 정렬 호출부는 대상 절점이 비활성이거나 건조하면 반환한다. SWTRCF의 반사 링크 검사는 양쪽 활성 격자 번호를 사용한다. C는 swantech §3.12의 ‘양쪽 wet’ 설명이 활성 격자와 이웃의 동적 수심 검사를 구분하지 않는 점이다. 건조 이웃은 수송 기법을 BSBT로 낮추지만 이 반사 호출 자체의 제외 조건은 아니다. 근거: `src/swanser.ftn:3335,3761`: `CALL REFLECT(AC2, REFLSO, X1, Y1, X2, Y2,`; `REF0 * W1 * PRDIF(ABS(IDR)) * AC2(IDA,IS,KCGRD(1))`; `src/swanser.ftn:3264,3267,3273`: `IF ( ICC.GT.1 ) THEN`; `IF (KGRPNT(IXCGRD(ILINK+1),IYCGRD(ILINK+1)).GT.1) THEN`; `IF (ICGRD.EQ.0) GOTO 90`.<br>`src/swancom1.ftn:3289–3300,3527–3537`의 대상 절점 검사와 SWTRCF 호출. swanuse PDF 21–22는 예외값으로 구성한 wet/dry 계산 격자를 설명한다.

## 2. §3.13 Obstacle-grid line 교차 (Eq 3.71-3.73)

Obstacle side 끝점 $\vec{x}_3, \vec{x}_4$, grid line 끝점(격자점) $\vec{x}_1, \vec{x}_2$. 교차점:
$$\vec{x}_1 + \lambda(\vec{x}_2-\vec{x}_1) = \vec{x}_3 + \mu(\vec{x}_4-\vec{x}_3) \quad \text{(3.71)}$$
($\lambda, \mu \in [0,1]$ 이어야 교차)
swantech PDF 119쪽 / 인쇄 111쪽 (3.72)의 인쇄 원문이다.

$$\lambda = \frac{(x_1-x_3)(y_2-y_1) - (y_1-y_3)(x_2-x_1)}{(x_4-x_3)(y_2-y_1) - (y_4-y_3)(x_2-x_1)} \quad \text{(3.72)}$$
$$\mu = \frac{(x_1-x_3)(y_4-y_3) - (y_1-y_3)(x_4-x_3)}{(x_4-x_3)(y_2-y_1) - (y_4-y_3)(x_2-x_1)} \quad \text{(3.73)}$$

(3.71)의 정의를 유지하면 (3.72)의 분수는 $\mu$다. (3.73)의 분수는 $\lambda$다. 원문 이름과 수정 이름을 구분해서 적는다. 근거: `src/swanser.ftn:2728` `MIU  = ((D*C) - (A*F)) / DIV1`; `src/swanser.ftn:2729` `LMBD = (C + (B*MIU)) / A`.
> 분모 0 → 평행 → 무교차 가정.

## 3. §3.14 σ 적분 (Eq 3.74-3.82) — 2 방법

### 3.1 Trapezoidal rule

$$I = \int_0^{\sigma_m} f\,E(\sigma)\,d\sigma \quad \text{(3.74)}$$
($\sigma_m$ = 최고 주파수, $f$ = 임의함수 보통 $\sigma^p/\omega^p/k^p$, log 분포 $\sigma_i$)
$$I \approx \sum_2^m \frac{1}{2}(f_{i-1}\sigma_{i-1}N_{i-1} + f_i\sigma_i N_i)(\sigma_i - \sigma_{i-1}) \quad \text{(3.75)}$$

**Tail 기여** ($E \propto \sigma^{-P^*}$):
$$\int_{\sigma_m}^\infty R\sigma^{-P^*}\,d\sigma = \sigma_m\frac{R\sigma_m^{-P^*}}{P^*-1} \quad \text{(3.76)}$$
$$\int_{\sigma_m}^\infty f(\sigma)\,d\sigma = \frac{\sigma_m}{P^*-1}f(\sigma_m) \quad \text{(3.77)}$$
> $P^* > 1$ 일 때만 유효 ($R\sigma_m^{-P^*} = f(\sigma_m)$).

### 3.2 Logarithmic method (FRINTF/FRINTH)

SWAN 변수: **FRINTF $= \ln(\sigma_{i+1}/\sigma_i)$**, **FRINTH $= \sqrt{\sigma_{i+1}/\sigma_i}$**. $\sigma_i = e^{\mu i}$, $\mu = \ln(\sigma_{i+1}/\sigma_i) \approx \Delta\sigma/\sigma$.
$$\int f(\sigma)\,d\sigma = \int f(\sigma)\mu e^{\mu i}\,di = \mu\int f(\sigma)\sigma\,di \quad \text{(3.78)}$$
$$\int f(\sigma)\,d\sigma \approx \mu\sum f_i\sigma_i \quad \text{(3.79)}$$
> Mesh 경계: $\sigma_i/\sqrt{\sigma_{i+1}/\sigma_i}$ ~ $\sigma_i\sqrt{\sigma_{i+1}/\sigma_i}$.

**Tail** (적분 $M\sigma_m$ 까지, $M = \sqrt{1+\Delta\sigma/\sigma}$):
$$\int_0^{2\pi}\int_{M\sigma_m}^\infty R\sigma^{-P^*}\,d\sigma d\theta = \frac{\sigma_m}{(P^*-1)M^{P^*-1}}R\sigma_m^{-P^*} \quad \text{(3.80)}$$
$$\int_0^{2\pi}\int_{M\sigma_m}^\infty f(\sigma)\,d\sigma d\theta = \frac{\sigma_m}{(P^*-1)M^{P^*-1}}f(\sigma_m) \quad \text{(3.81)}$$

해석: 인쇄 식 우변에는 방향 적분이 빠져 있다. $R$이 방향 독립이면 $2\pi$가 필요하다. $R(\theta)$이면 $\int R\,d\theta$가 필요하다. 코드의 방향 합은 존재한다. 근거: `src/swanout1.ftn:4405,4417–4418`의 `DO ID=1, MDC` 및 각 방향 꼬리 합. `src/SwanIntgratSpc.ftn90:176`은 `DDIR`도 곱한다.

SwanIntgratSpc의 절대주파수·파수·군속도 꼬리 적분은 가중치의 차수를 분모에 반영하지 않는다. 유속이 0이면 상대주파수와 절대주파수는 같지만 수렴 가능한 $p\ne0$의 두 꼬리 모멘트가 다르다. 유한 상한 보정은 차수를 반영하므로 최고 주파수의 가중치를 상수로 고정한 일관된 근사라는 해석과도 맞지 않는다. 범위 지정 출력에서 호출되며 해당 식을 끄는 전처리 표지는 없다. E 강함을 유지한다. 근거: [R1 대조](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md), TC-010.

SwanIntgratSpc는 적분 하한과 상한이 같은 주파수 구간 안에 있으면 하한을 적용하지 않는다. 상한 분기의 적분은 그 구간의 왼쪽 격자점에서 시작한다. 파서는 하한·상한의 순서만 검사한다. 범위 지정 출력이 이 함수를 호출하며 이후 하한 보정과 해당 식의 전처리 표지는 없다. E 강함을 유지한다. 근거: [R1 대조](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md), TC-011.
$$\frac{\sigma_m}{(P^*-1)M^{P^*-1}} \approx \frac{\sigma_m}{(P^*-1)(1+(P^*-1)(M-1))} \quad \text{(3.82)}$$
해석: $P^*$를 적분함수의 감쇠 지수로 정의하면 심해 $k^nE$의 지수는 $P-2n$이다. $P-2n-1$은 꼬리 분모의 지수 차이다. 문서는 감쇠 지수와 분모 계수를 혼용한다. 근거: swantech PDF 120쪽 / 인쇄 112쪽; `src/swanout1.ftn:4401–4404` `PPTAIL = PWTAIL(1) - 1.`; `ETAIL  = 1. / (PPTAIL * (1. + PPTAIL * (FRINTH-1.)))`; `PPTAIL = PWTAIL(1) - 2.`.

## 4. §3.15 상대→절대 주파수 변환 (Eq 3.83-3.84)

SWAN 내부는 상대(각)주파수 $\sigma$ + 방향. User 가 절대주파수 $\omega$ 원할 시(고정점 측정 등) 2 변경: 평균 절대주파수 + action/energy 변환.

$$\overline{\omega} = \frac{\int\omega E(\sigma,\theta)\,d\sigma d\theta}{\int E(\sigma,\theta)\,d\sigma d\theta} \quad \text{(3.83)}$$

$\sigma\to\omega$ 변환은 1:1 아님(Jacobian 무한대 가능, $\omega = W(\sigma)$). 요건: ① current→0 시 절대=상대 ② 총에너지 보존. 분포 동일 가정.
$$E(\omega,\theta) = \int E(\sigma,\theta)\delta(\omega-W(\sigma))\,d\sigma \quad \text{(3.84)}$$
> 이산화: $\sigma_i/M$ ~ $M\sigma_i$ 구간서 energy density 일정 가정.

## 5. §3.16 Spectra interpolation (Eq 3.85-3.92) — WAM 변형

공간·시간 spectra 보간 (WAM 변형). 단순 bin-by-bin 아님 (peak 불일치 시 peak 감소) → **평균 주파수·방향으로 정규화 → 보간 → 역변환**.

주파수 moment (origin $i=1,2$, $k=0,1$):
$$m_{i,k} = \int N_i(\sigma,\theta)\sigma^k\,d\sigma d\theta \quad \text{(3.85)}$$
$$\overline{\sigma}_i = \frac{m_{i,1}}{m_{i,0}} \quad \text{(3.86)}$$

SINTRP의 작용 모멘트는 로그 주파수 격자의 주파수별 적분 폭을 생략한다. 입력은 구간 총량이 아니라 작용밀도이다. 문서 식 (3.85)의 모멘트와 다르다. peak 유지용 내부 지표라는 설계 가능성을 반영해 E 중간을 유지한다. 근거: `src/swanser.ftn:4432,4435`: `ATOT1  = ATOT1  + FL1(ID,IS)`; `ASTOT1 = ASTOT1 + FL1(ID,IS) * SPCSIG(IS)`.<br>`src/swanser.ftn:4290,4303,4409–4448`; `src/swanmain.ftn:6945–6956`은 BSPECS를 전달하고 결과 AC2에 주파수 제곱을 곱해 에너지를 구한다. [git E 판정](../../../_staging/recovery/compare/SWAN-git-verify-E.md): 최초 반입 `b2ae30e`(2022-08-10)의 `src/swanser.ftn:4863`, 41.51 `7ee8981`(2024-09-02)의 `src/swanser.ftn:4432`, patch B `0dabfa4`와 HEAD `43e9bbb`(2026-07-13)에 같은 핵심 식이 있다. 해당 식의 `git log -G`는 최초 반입만 반환한다.

SINTRP의 평균 주파수는 작용밀도의 단순 합을 분모로 쓴다. 문서 식 (3.86)의 주파수별 적분 폭을 포함한 평균과 다르다. 계산한 평균의 비는 주파수 이동량에 직접 쓰인다. TN-162와 같은 원인의 E 중간이다. 근거: `src/swanser.ftn:4491–4492`: `ASIG1  = ASTOT1 / ATOT1`; `ASIG2  = ASTOT2 / ATOT2`.<br>`src/swanser.ftn:4491–4499`; 작용밀도 입력의 호출 근거는 `src/swanmain.ftn:6945–6956`. [git E 판정](../../../_staging/recovery/compare/SWAN-git-verify-E.md): 최초 반입 `b2ae30e`(2022-08-10)의 `src/swanser.ftn:4922`, 41.51 `7ee8981`(2024-09-02)의 `src/swanser.ftn:4491`, patch B `0dabfa4`와 HEAD `43e9bbb`(2026-07-13)에 같은 핵심 식이 있다. 해당 식의 `git log -G`는 최초 반입만 반환한다.
보간 spectrum 평균주파수 (가중 $w_1+w_2=1$, $w_1$=첫 origin 까지 상대거리):
$$\overline{\sigma} = \frac{w_2 m_{1,1} + w_1 m_{2,1}}{w_2 m_{1,0} + w_1 m_{2,0}} \quad \text{(3.87)}$$

방향 moment:
$$m_{i,x} = \int N_i\cos\theta\,d\sigma d\theta \quad \text{(3.88)},\qquad m_{i,y} = \int N_i\sin\theta\,d\sigma d\theta \quad \text{(3.89)}$$
$$\overline{\theta}_i = \text{atan}\left(\frac{m_{i,y}}{m_{i,x}}\right) \quad \text{(3.90)},\qquad \overline{\theta} = \text{atan}\left[\frac{w_2 m_{1,y} + w_1 m_{2,y}}{w_2 m_{1,x} + w_1 m_{2,x}}\right] \quad \text{(3.91)}$$

SINTRP의 방향 모멘트는 로그 주파수 격자의 주파수별 적분 폭을 생략한다. 주파수별 파향이 다르면 문서 식 (3.88)·(3.89)의 평균 방향과 달라진다. 원형 방향 경계 연결은 이 적분 폭 생략을 보정하지 않는다. TN-162와 같은 원인의 E 중간이다. 근거: `src/swanser.ftn:4433–4434`: `AXTOT1 = AXTOT1 + FL1(ID,IS) * SPCDIR(ID,2)`; `AYTOT1 = AYTOT1 + FL1(ID,IS) * SPCDIR(ID,3)`.<br>`src/swanser.ftn:4465–4466,4538–4555`; 작용밀도 입력의 호출 근거는 `src/swanmain.ftn:6945–6956`. [git E 판정](../../../_staging/recovery/compare/SWAN-git-verify-E.md): 최초 반입 `b2ae30e`(2022-08-10)의 `src/swanser.ftn:4864`, 41.51 `7ee8981`(2024-09-02)의 `src/swanser.ftn:4433`, patch B `0dabfa4`와 HEAD `43e9bbb`(2026-07-13)에 같은 핵심 식이 있다. 해당 식의 `git log -G`는 최초 반입만 반환한다.

C는 swantech 식 (3.90)·(3.91)의 atan 표기에 사분면 규약이 없는 점이다. 코드는 교차곱·내적의 ATAN2로 방향 차이를 구한다. 문서의 평균 방향을 atan2 관례로 해석하면 이 계산과 대응한다. 느슨한 atan 표기만으로 문서가 잘못된 사분면을 지시한다고 단정하지 않는다. 근거: `src/swanser.ftn:4465–4466`: `DELD1  = REAL(ATAN2(DBLE(AXTOT*AYTOT1 - AYTOT*AXTOT1),`; `&                        DBLE(AXTOT*AXTOT1 + AYTOT*AYTOT1))) / DDIR`.

최종 보간 spectrum (각 origin 을 $\overline{\sigma}/\overline{\theta}$ 로 stretch/rotate 후 가중합):
$$N(\sigma,\theta) = w_2 N_1[\overline{\sigma}_1\sigma/\overline{\sigma},\,\theta-(\overline{\theta}-\overline{\theta}_1)] + w_1 N_2[\overline{\sigma}_2\sigma/\overline{\sigma},\,\theta-(\overline{\theta}-\overline{\theta}_2)] \quad \text{(3.92)}$$

## 6. SWAN 옵션 매핑 (User cmd)

| Tech (PDF §) | User cmd / 변수 | 비고 |
|---|---|---|
| 3.70-3.73 obstacle | `OBSTACLE TRANS/REFL` | crossing → BSBT, K_t² height 기준 |
| 3.74-3.82 σ integration | FRINTF/FRINTH/PWTAIL/MSC | trapezoidal + log tail |
| 3.83-3.84 absolute freq | `QUANTITY ... ` (절대주파수 출력) | current 존재 시 의미 |
| 3.85-3.92 interpolation | (internal, BC nest/시간보간) | WAM 변형, peak 보존 |

## 7. 한계

- §3.12 obstacle propagation(3.70): ASCII 다행식 → 구조 전사 (K_t² 위치 명시).
- §3.14 tail factor 들은 $P^*>1$ 제약 명시. PWTAIL default 값은 User Manual 참조.
- 끝 가중치 부근은 한 스펙트럼을 그대로 복사한다. 거의 빈 스펙트럼은 이동 없이 나머지 스펙트럼의 가중합을 쓴다. 부분 방향 격자와 주파수 경계 밖의 기여를 버린다. 근거: `src/swanser.ftn:4409,4412,4415,4418`: `IF (W1.GT.0.99) THEN`; `FL(ID,IS) = FL1(ID,IS)`; `ELSE IF (W1.LT.0.01) THEN`; `FL(ID,IS) = FL2(ID,IS)`; 4442·4448의 총량 문턱은 `1.E-9`이다. `src/swanser.ftn:4442–4454,4538–4555`는 빈 스펙트럼 처리와 방향·주파수 범위 검사를 보인다. [10-13 전수 검증 보완]

## 8. 연결

- [swan-tech-ch2-obstacles-diffraction-setup](swan-tech-ch2-obstacles-diffraction-setup.md) — §2.5 obstacle 물리식(Goda/d'Angremond K_t)
- [swan-tech-ch3-qc-curvilinear](swan-tech-ch3-qc-curvilinear.md) — §3.10 곡선 propagation(3.55, obstacle 3.70 의 base)
- [swan-tech-ch3-breaking-source](swan-tech-ch3-breaking-source.md) — §3.17 breaking source 수치 (다음)
- [swan-tech-ch3-discretization](swan-tech-ch3-discretization.md) — §3.2 BSBT (obstacle crossing fallback)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TC-010 | 절대주파수·파수·군속도 모멘트의 꼬리 적분 | — (R1 제3절의 코드 처리 항목) | `src/SwanIntgratSpc.ftn90:161,238,256,313,323,327,336`: 상대주파수는 `ftail = 1. / (PWTAIL(1) - q)`; 다른 경로는 `ftail = 1. / (PWTAIL(1) - 1.)`; `pmom = pmom + ehfr * (omeg2**p * spcsig(MSC) - ctail) * DDIR * ftail`; `pmom = pmom + ehfr * (wpar(MSC)**p * spcsig(MSC) - ctail) * DDIR * ftail`.<br>`src/swanout1.ftn:4394–4397,4421–4431,4370–4381`의 실제 itype 2·3 호출. `src/SwanIntgratSpc.ftn90:234–260,309–340`의 조건은 `fmax > spcsig(MSC)`와 `MSC > 3`이다. [git E 판정](../../../_staging/recovery/compare/SWAN-git-verify-E.md): 최초 반입 `b2ae30e`(2022-08-10)의 `src/SwanIntgratSpc.ftn90:238`, 41.51 `7ee8981`(2024-09-02)의 `src/SwanIntgratSpc.ftn90:238`, patch B `0dabfa4`와 HEAD `43e9bbb`(2026-07-13)에 같은 핵심 식이 있다. 해당 식의 `git log -G`는 최초 반입만 반환한다. | E 코드 결함 후보 (강함) | SwanIntgratSpc의 절대주파수·파수·군속도 꼬리 적분은 가중치의 차수를 분모에 반영하지 않는다. 유속이 0이면 상대주파수와 절대주파수는 같지만 수렴 가능한 $p\ne0$의 두 꼬리 모멘트가 다르다. 유한 상한 보정은 차수를 반영하므로 최고 주파수의 가중치를 상수로 고정한 일관된 근사라는 해석과도 맞지 않는다. 범위 지정 출력에서 호출되며 해당 식을 끄는 전처리 표지는 없다. E 강함을 유지한다. [10-13 전수 검증 정정]
| R1:TC-011 | 한 주파수 구간 안에 놓인 적분 하한·상한 | — (R1 제3절의 코드 처리 항목) | `src/SwanIntgratSpc.ftn90:119–129`: `elseif ( spcsig(is) > fmax ) then`; `dsf = fmax - spcsig(is-1)`; 다음 배타 분기는 `elseif ( spcsig(is) > fmin ) then`이다. 202–214·275–287도 같은 분기이다.<br>`src/swanpre1.ftn:2297–2308`; `src/swanout1.ftn:3501–3508`은 Hz 경계를 PI2로 바꿔 전달한다. `src/SwanIntgratSpc.ftn90:64–65,114–145`. [git E 판정](../../../_staging/recovery/compare/SWAN-git-verify-E.md): 최초 반입 `b2ae30e`(2022-08-10)의 `src/SwanIntgratSpc.ftn90:119`, 41.51 `7ee8981`(2024-09-02)의 `src/SwanIntgratSpc.ftn90:119`, patch B `0dabfa4`와 HEAD `43e9bbb`(2026-07-13)에 같은 핵심 식이 있다. 해당 식의 `git log -G`는 최초 반입만 반환한다. | E 코드 결함 후보 (강함) | SwanIntgratSpc는 적분 하한과 상한이 같은 주파수 구간 안에 있으면 하한을 적용하지 않는다. 상한 분기의 적분은 그 구간의 왼쪽 격자점에서 시작한다. 파서는 하한·상한의 순서만 검사한다. 범위 지정 출력이 이 함수를 호출하며 이후 하한 보정과 해당 식의 전처리 표지는 없다. E 강함을 유지한다. [10-13 전수 검증 정정]
| R1:TC-012 | 꼬리 적용과 큰 상한의 무한대 취급 | — (문서 누락) | `src/SwanIntgratSpc.ftn90:153,155,157,163–165`: `if ( MSC > 3 ) then`; `if ( PWTAIL(1) <= q ) then`; `SwanIntgratSpc = -999.`; `if ( fmax > 100. ) then`; `ctail = 0.`. | C 문서 누락 | 꼬리는 주파수 수가 3보다 클 때 적용한다. 상대주파수 모멘트의 발산 조건은 오류 반환이다. $\sigma$ 상한이 $100\ \mathrm{rad\,s^{-1}}$를 넘으면 유한 상한 잔여량을 0으로 둔다. |
| R1:TC-013 | Doppler 변환의 폭 0 구간 | — (문서 누락) | `src/swanout2.ftn:2313–2316,2348–2351`: `IF ( .NOT.EQREAL(OMEG1,OMEG2) ) THEN`; `EE = ECLL * DSIG / ABS(OMEG2-OMEG1)`; 대체식 `EE = ECLL * DSIG`와 `DOMEG = 1.`.<br>`src/swanout2.ftn:2330–2370`의 구간 겹침 검사·누적·출력 폭 나눗셈. | C 문서 누락 | 두 절대주파수 경계가 EQREAL에서 같으면 `EE`에 구간 에너지를 넣고 곱셈 인자 `DOMEG = 1.`을 쓴다. 실제 출력 bin의 물리적 폭이 1이라는 뜻은 아니다. 출력 bin과 겹치는지 검사한 뒤 구간 에너지를 더하며 마지막에 출력 폭으로 나눈다. C는 swantech §3.15에 이 영 폭 예외가 없는 점이다. 행 끝 `41.54` 표지는 변경 판의 근거가 아니다. 해당 식의 git 검색은 최초 반입 `b2ae30e`만 반환했다. |
| R1:TN-145 | 반사의 활성 격자 조건 | swantech PDF 118–119쪽 / 인쇄 110–111쪽: 반사는 같은 대상 절점의 입사 성분을 사용한다. 양쪽 격자점이 wet일 때만 작용한다. | `src/swanser.ftn:3335,3761`: `CALL REFLECT(AC2, REFLSO, X1, Y1, X2, Y2,`; `REF0 * W1 * PRDIF(ABS(IDR)) * AC2(IDA,IS,KCGRD(1))`; `src/swanser.ftn:3264,3267,3273`: `IF ( ICC.GT.1 ) THEN`; `IF (KGRPNT(IXCGRD(ILINK+1),IYCGRD(ILINK+1)).GT.1) THEN`; `IF (ICGRD.EQ.0) GOTO 90`.<br>`src/swancom1.ftn:3289–3300,3527–3537`의 대상 절점 검사와 SWTRCF 호출. swanuse PDF 21–22는 예외값으로 구성한 wet/dry 계산 격자를 설명한다. | C 문서 누락 | 같은 대상 절점의 입사 성분을 쓰는 식은 일치한다. 정렬 호출부는 대상 절점이 비활성이거나 건조하면 반환한다. SWTRCF의 반사 링크 검사는 양쪽 활성 격자 번호를 사용한다. C는 swantech §3.12의 ‘양쪽 wet’ 설명이 활성 격자와 이웃의 동적 수심 검사를 구분하지 않는 점이다. 건조 이웃은 수송 기법을 BSBT로 낮추지만 이 반사 호출 자체의 제외 조건은 아니다. |
| R1:TN-147 | 문서 식 (3.72) | swantech PDF 119쪽 / 인쇄 111쪽, (3.72): $\lambda=[(x_1-x_3)(y_2-y_1)-(y_1-y_3)(x_2-x_1)]/[(x_4-x_3)(y_2-y_1)-(y_4-y_3)(x_2-x_1)]$. | `src/swanser.ftn:2700–2707,2728`의 `MIU  = ((D*C) - (A*F)) / DIV1`. | B 문서 오기 | 해석: 일반 비수직 분기에서 이 비는 $\mu$이다. 문서가 (3.71)의 두 매개변수 이름을 교환했다. |
| R1:TN-148 | 문서 식 (3.73) | swantech PDF 119쪽 / 인쇄 111쪽, (3.73): $\mu=[(x_1-x_3)(y_4-y_3)-(y_1-y_3)(x_4-x_3)]/[(x_4-x_3)(y_2-y_1)-(y_4-y_3)(x_2-x_1)]$. | `src/swanser.ftn:2729`: `LMBD = (C + (B*MIU)) / A`. | B 문서 오기 | 해석: 이 비는 $\lambda$이다. 두 값 모두 $[0,1]$인지 검사하는 교차 여부는 이름 교환에 영향을 받지 않는다. |
| R1:TN-153 | 로그 주파수 기준점 | swantech PDF 120쪽 / 인쇄 112쪽, 번호 없음: $\mathrm{FRINTF}=\ln(\sigma_{i+1}/\sigma_i)=\mu,\ \mathrm{FRINTH}=\sqrt{\sigma_{i+1}/\sigma_i}$; $\sigma_i=e^{\mu i}$; $\mu\approx\Delta\sigma/\sigma$. | `src/swanpre1.ftn:4685–4691`의 `SFAC = EXP(FRINTF)`와 등비 재귀. | F 표기 차이 | 해석: 일반식은 $\sigma_i=\sigma_1e^{\mu(i-1)}$이다. 문서의 지수식은 주파수 기준값과 index 원점을 흡수한 표기이다. $\mu=\Delta\sigma/\sigma$를 정확한 등식으로 사용하지 않는다. |
| R1:TN-156 | 문서 식 (3.80)·(3.81) | swantech PDF 120쪽 / 인쇄 112쪽, (3.80): $\int_0^{2\pi}\int_{M\sigma_m}^\infty R\sigma^{-P^*}d\sigma d\theta=R M^{1-P^*}\sigma_m^{1-P^*}/(P^*-1)=\sigma_mR\sigma_m^{-P^*}/[(P^*-1)M^{P^*-1}]$; (3.81): 같은 이중적분을 $f$에 대해 $\sigma_m f(\sigma_m)/[(P^*-1)M^{P^*-1}]$로 쓴다. | `src/swanout1.ftn:4405,4417–4418`의 `DO ID=1, MDC` 및 각 방향 꼬리 합. `src/SwanIntgratSpc.ftn90:176`은 `DDIR`도 곱한다. | B 문서 오기 | 해석: 인쇄 식 우변에는 방향 적분이 빠져 있다. $R$이 방향 독립이면 $2\pi$가 필요하다. $R(\theta)$이면 $\int R\,d\theta$가 필요하다. 코드의 방향 합은 존재한다. |
| R1:TN-158 | 꼬리 지수와 분모 | swantech PDF 120쪽 / 인쇄 112쪽, 번호 없음: “$P^*=PWTAIL(1)$”; $\bar k$ 계산에서 “$P^*=P-2n-1$”. | TN-157의 `PPTAIL`과 `PWTAIL(1)`. | B 문서 오기 | 해석: $P^*$를 적분함수의 감쇠 지수로 정의하면 심해 $k^nE$의 지수는 $P-2n$이다. $P-2n-1$은 꼬리 분모의 지수 차이다. 문서는 감쇠 지수와 분모 계수를 혼용한다. |
| R1:TN-161 | Doppler 변환의 유한 대역 | swantech PDF 121쪽 / 인쇄 113쪽: 무흐름 극한에서 두 밀도가 같고 “The total energy density ... is identical”. | `src/swanout2.ftn:2330`: `DO 90 IOM = 1, MSC`; 2368–2370에서 출력 폭으로 나눈다. | C 문서 누락 | 전체 입력 에너지가 출력 주파수 범위 안에 매핑될 때 보존한다. 범위 밖으로 옮겨진 에너지는 이 유한 출력 루프에 들어가지 않는다. 무흐름 동일성은 bin 폭으로 다시 나눌 때 성립한다. |
| R1:TN-162 | 문서 식 (3.85) | swantech PDF 121쪽 / 인쇄 113쪽, (3.85): $m_{i,k}=\int N_i(\sigma,\theta)\sigma^k\,d\sigma d\theta$, $i=1,2,\ k=0,1$. | `src/swanser.ftn:4432,4435`: `ATOT1  = ATOT1  + FL1(ID,IS)`; `ASTOT1 = ASTOT1 + FL1(ID,IS) * SPCSIG(IS)`.<br>`src/swanser.ftn:4290,4303,4409–4448`; `src/swanmain.ftn:6945–6956`은 BSPECS를 전달하고 결과 AC2에 주파수 제곱을 곱해 에너지를 구한다. [git E 판정](../../../_staging/recovery/compare/SWAN-git-verify-E.md): 최초 반입 `b2ae30e`(2022-08-10)의 `src/swanser.ftn:4863`, 41.51 `7ee8981`(2024-09-02)의 `src/swanser.ftn:4432`, patch B `0dabfa4`와 HEAD `43e9bbb`(2026-07-13)에 같은 핵심 식이 있다. 해당 식의 `git log -G`는 최초 반입만 반환한다. | E 코드 결함 후보 (중간) | SINTRP의 작용 모멘트는 로그 주파수 격자의 주파수별 적분 폭을 생략한다. 입력은 구간 총량이 아니라 작용밀도이다. 문서 식 (3.85)의 모멘트와 다르다. peak 유지용 내부 지표라는 설계 가능성을 반영해 E 중간을 유지한다. |
| R1:TN-163 | 문서 식 (3.86) | swantech PDF 122쪽 / 인쇄 114쪽, (3.86): $\bar\sigma_i=m_{i,1}/m_{i,0}$. | `src/swanser.ftn:4491–4492`: `ASIG1  = ASTOT1 / ATOT1`; `ASIG2  = ASTOT2 / ATOT2`.<br>`src/swanser.ftn:4491–4499`; 작용밀도 입력의 호출 근거는 `src/swanmain.ftn:6945–6956`. [git E 판정](../../../_staging/recovery/compare/SWAN-git-verify-E.md): 최초 반입 `b2ae30e`(2022-08-10)의 `src/swanser.ftn:4922`, 41.51 `7ee8981`(2024-09-02)의 `src/swanser.ftn:4491`, patch B `0dabfa4`와 HEAD `43e9bbb`(2026-07-13)에 같은 핵심 식이 있다. 해당 식의 `git log -G`는 최초 반입만 반환한다. | E 코드 결함 후보 (중간) | SINTRP의 평균 주파수는 작용밀도의 단순 합을 분모로 쓴다. 문서 식 (3.86)의 주파수별 적분 폭을 포함한 평균과 다르다. 계산한 평균의 비는 주파수 이동량에 직접 쓰인다. TN-162와 같은 원인의 E 중간이다. |
| R1:TN-164 | 문서 식 (3.87) | swantech PDF 122쪽 / 인쇄 114쪽, (3.87): $\bar\sigma=(w_2m_{1,1}+w_1m_{2,1})/(w_2m_{1,0}+w_1m_{2,0})$; $w_1+w_2=1$. | `src/swanser.ftn:4493–4495`: `ATOT   = W1 * ATOT1  + W2 * ATOT2`; `ASTOT  = W1 * ASTOT1 + W2 * ASTOT2`; `ASIG   = ASTOT / ATOT`. | F 표기 차이 | 해석: 문서 $w_1$은 첫 원점까지의 상대거리이다. 코드 `W1`은 첫 스펙트럼에 곱하는 가중치이다. 따라서 코드 `W1=w_2,W2=w_1`이다. 모멘트 값의 차이는 TN-162·163에서 별도로 판정했다. |
| R1:TN-165 | 문서 식 (3.88)·(3.89) | swantech PDF 122쪽 / 인쇄 114쪽, (3.88): $m_{i,x}=\int N_i\cos\theta\,d\sigma d\theta$; (3.89): $m_{i,y}=\int N_i\sin\theta\,d\sigma d\theta$. | `src/swanser.ftn:4433–4434`: `AXTOT1 = AXTOT1 + FL1(ID,IS) * SPCDIR(ID,2)`; `AYTOT1 = AYTOT1 + FL1(ID,IS) * SPCDIR(ID,3)`.<br>`src/swanser.ftn:4465–4466,4538–4555`; 작용밀도 입력의 호출 근거는 `src/swanmain.ftn:6945–6956`. [git E 판정](../../../_staging/recovery/compare/SWAN-git-verify-E.md): 최초 반입 `b2ae30e`(2022-08-10)의 `src/swanser.ftn:4864`, 41.51 `7ee8981`(2024-09-02)의 `src/swanser.ftn:4433`, patch B `0dabfa4`와 HEAD `43e9bbb`(2026-07-13)에 같은 핵심 식이 있다. 해당 식의 `git log -G`는 최초 반입만 반환한다. | E 코드 결함 후보 (중간) | SINTRP의 방향 모멘트는 로그 주파수 격자의 주파수별 적분 폭을 생략한다. 주파수별 파향이 다르면 문서 식 (3.88)·(3.89)의 평균 방향과 달라진다. 원형 방향 경계 연결은 이 적분 폭 생략을 보정하지 않는다. TN-162와 같은 원인의 E 중간이다. |
| R1:TN-166 | 문서 식 (3.90)·(3.91) | swantech PDF 122쪽 / 인쇄 114쪽, (3.90): $\bar\theta_i=\operatorname{atan}(m_{i,y}/m_{i,x})$; (3.91): $\bar\theta=\operatorname{atan}[(w_2m_{1,y}+w_1m_{2,y})/(w_2m_{1,x}+w_1m_{2,x})]$. | `src/swanser.ftn:4465–4466`: `DELD1  = REAL(ATAN2(DBLE(AXTOT*AYTOT1 - AYTOT*AXTOT1),`; `&                        DBLE(AXTOT*AXTOT1 + AYTOT*AYTOT1))) / DDIR`. | C 문서 누락 | C는 swantech 식 (3.90)·(3.91)의 atan 표기에 사분면 규약이 없는 점이다. 코드는 교차곱·내적의 ATAN2로 방향 차이를 구한다. 문서의 평균 방향을 atan2 관례로 해석하면 이 계산과 대응한다. 느슨한 atan 표기만으로 문서가 잘못된 사분면을 지시한다고 단정하지 않는다. |
| R1:TN-168 | SINTRP 경계·빈 스펙트럼 | swantech PDF 121–122쪽 / 인쇄 113–114쪽, §3.16의 일반 보간식. | `src/swanser.ftn:4409,4412,4415,4418`: `IF (W1.GT.0.99) THEN`; `FL(ID,IS) = FL1(ID,IS)`; `ELSE IF (W1.LT.0.01) THEN`; `FL(ID,IS) = FL2(ID,IS)`; 4442·4448의 총량 문턱은 `1.E-9`이다. `src/swanser.ftn:4442–4454,4538–4555`는 빈 스펙트럼 처리와 방향·주파수 범위 검사를 보인다. | C 문서 누락 | 끝 가중치 부근은 한 스펙트럼을 그대로 복사한다. 거의 빈 스펙트럼은 이동 없이 나머지 스펙트럼의 가중합을 쓴다. 부분 방향 격자와 주파수 경계 밖의 기여를 버린다. [10-13 전수 검증 보완]
| R3:CP-006 | 교차 허용오차·선분 역할 교환·끝점 처리 | — (문서 누락) | 교차 허용오차·선분 역할 교환·끝점 처리. `src/swanser.ftn:2698` `EPS = EPSILON(X1)*SQRT((X2-X1)*(X2-X1)+(Y2-Y1)*(Y2-Y1))`; `src/swanser.ftn:2699` `IF (EPS ==0.) EPS = TINY(X1)`; `src/swanser.ftn:2702` `IF (ABS(A) .GT. TINY(X1)) THEN`; `src/swanser.ftn:2735` `! Only (X1,Y1) is checked, because of otherwise possible double`. | C 문서 누락 | 격자 링크의 x차이가 거의 0이면 격자 링크와 장애물 선분의 역할을 바꾼다. 두 매개변수의 이름도 교환한다. 한 끝점만 중복 여부를 검사한다. 비구조 `src/SwanCrossObstacle.ftn90:100`은 `.not.EQREAL(det,0.)`로 평행을 판정한다. (3.71)–(3.73)은 이 수치 보호를 적지 않는다. |
| R3:NT-011 | 교차식 매개변수의 이름 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch3-obstacles-spectral-ops.md:42`의 `\lambda =`; 43의 `\mu =`. | `src/swanser.ftn:2728` `MIU  = ((D*C) - (A*F)) / DIV1`; `src/SwanCrossObstacle.ftn90:102` `p = ( a*d - b*c ) / det`. `src/swanser.ftn:2700–2717`; `src/SwanCrossObstacle.ftn90:87–103`.<br>`src/swanser.ftn:2729` `LMBD = (C + (B*MIU)) / A`; `src/SwanCrossObstacle.ftn90:103` `q = ( a*f - b*e ) / det`. | B 문서 오기 | (3.71)의 정의를 유지하면 (3.72)의 분수는 $\mu$다. (3.73)의 분수는 $\lambda$다. 원문 이름과 수정 이름을 구분해서 적는다. |
| R3:OQ-029 | 교차 매개변수 λ의 분수 | swantech PDF 119쪽 / 인쇄 111쪽, (3.72): $\lambda=\frac{(x_1-x_3)(y_2-y_1)-(y_1-y_3)(x_2-x_1)}{(x_4-x_3)(y_2-y_1)-(y_4-y_3)(x_2-x_1)}$. | `src/swanser.ftn:2728` `MIU  = ((D*C) - (A*F)) / DIV1`; `src/SwanCrossObstacle.ftn90:102` `p = ( a*d - b*c ) / det`. `src/swanser.ftn:2700–2717`; `src/SwanCrossObstacle.ftn90:87–103`. | B 문서 오기 | 이 분수는 (3.71)의 $\mu$다. `ABS(A) .GT. TINY(X1)` 분기에서는 구조 코드의 `MIU`가 이를 계산한다. 비구조 코드의 `p`도 장애물 선분의 매개변수다. 문서가 $\lambda$라는 이름을 바꿔 적었다. 구조 코드의 두 선분을 교환하는 분기에서는 `MIU`와 `LMBD`의 역할도 교환된다. |
| R3:OQ-030 | 교차 매개변수 μ의 분수 | swantech PDF 119쪽 / 인쇄 111쪽, (3.73): $\mu=\frac{(x_1-x_3)(y_4-y_3)-(y_1-y_3)(x_4-x_3)}{(x_4-x_3)(y_2-y_1)-(y_4-y_3)(x_2-x_1)}$. | `src/swanser.ftn:2729` `LMBD = (C + (B*MIU)) / A`; `src/SwanCrossObstacle.ftn90:103` `q = ( a*f - b*e ) / det`. | B 문서 오기 | 이 분수는 (3.71)의 $\lambda$다. 문서가 이름을 바꿔 적었다. 두 값 모두 0–1 범위를 검사하므로 이름 교환만으로 교차 여부는 바뀌지 않는다. |
