---
title: "SWAN swantech Ch 3.12-3.13 obstacle 수치처리 + 3.14 σ integration + 3.15 freq transform + 3.16 spectra interpolation verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.12 Numerical treatment of obstacles + §3.13 Crossing of obstacle and grid line + §3.14 Integration over σ + §3.15 Transformation from relative to absolute frequency + §3.16 Interpolation of spectra, doc p.109-113 (Eq 3.70-3.92). WAM interpolation procedure."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §3.12-3.16 직접 read via pdftotext (식 번호 context-verified: obstacle propagation 3.70·line crossing 3.71-73·σ integration trapezoidal+tail 3.74-82·absolute freq 3.83-84·spectra interpolation 3.85-92) + website_markdown node58-62.md LaTeX alt-text. 식 번호는 PDF 번호 (online HTML +43 offset)."
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

> swantech.pdf (v41.51) §3.12-3.16 직접 read. Obstacle 의 **수치 구현**(line crossing + K_t² reduction + reflection) + **spectral 연산**(σ 적분 + 주파수 변환 + spectra interpolation). [[swan-tech-ch2-obstacles-diffraction-setup]] (§2.5 물리식)의 numerical 짝.
>
> **식 번호 주의**: PDF 번호 사용 (online HTML +43 offset, 예: obstacle propagation HTML 3.113 = PDF 3.70).

## 1. §3.12 Obstacle 수치처리 (Eq 3.70)

Obstacle = 계산격자 관통 line (Fig 3.7). Stencil grid line 이 obstacle 교차 시 (§3.13 절차) **1차 upwind(BSBT)로 회귀**.

**Transmission**: target 점 0 계산 시, 이웃 점 1 의 기여를 **$K_t^2$ 감소** (연결선이 obstacle 교차 시; power 2 는 $K_t$ 가 파고 기준이라). 점 2 (무교차)는 $K_t=1$.
> 결과는 obstacle 이 같은 grid line 교차하는 한 동일 (길어도 끝이 같은 mesh면 동일). Obstacle 은 **최소 몇 grid line 교차해야 효과** 있음.

곡선좌표 propagation 항 (transmission 반영, §3.10 Eq 3.55 에 $K_{t}^2$ 삽입):
$$\left(\frac{1}{\Delta t} + (D_{x,1}+D_{x,2})c_{x,i,j}^+ + (D_{y,1}+D_{y,2})c_{y,i,j}^+\right)N_{i,j}^+ - \frac{N_{i,j}^-}{\Delta t} - D_{x,1}(c_x K_{t,1}^2 N)_{i-1,j}^+ - D_{y,1}(c_y K_{t,1}^2 N)_{i-1,j}^+ - D_{x,2}(c_x K_{t,2}^2 N)_{i,j-1}^+ - D_{y,2}(c_y K_{t,2}^2 N)_{i,j-1}^+ = S_{i,j}^+ \quad \text{(3.70)}$$

**Reflection**: target 점 0 의 reflected 성분은 **동일 격자점 입사 성분에서** 계산 (수치 부정확하나 step→0 시 수렴). 점 1 기여 = transmission 감소 + 입사 반사로 부분 대체, 점 2 불변.
> **반사는 점 0·1 둘 다 wet 일 때만** — obstacle line 은 양측 wet 점으로 둘러싸여야 유효.

## 2. §3.13 Obstacle-grid line 교차 (Eq 3.71-3.73)

Obstacle side 끝점 $\vec{x}_3, \vec{x}_4$, grid line 끝점(격자점) $\vec{x}_1, \vec{x}_2$. 교차점:
$$\vec{x}_1 + \lambda(\vec{x}_2-\vec{x}_1) = \vec{x}_3 + \mu(\vec{x}_4-\vec{x}_3) \quad \text{(3.71)}$$
($\lambda, \mu \in [0,1]$ 이어야 교차)
$$\lambda = \frac{(x_1-x_3)(y_2-y_1) - (y_1-y_3)(x_2-x_1)}{(x_4-x_3)(y_2-y_1) - (y_4-y_3)(x_2-x_1)} \quad \text{(3.72)}$$
$$\mu = \frac{(x_1-x_3)(y_4-y_3) - (y_1-y_3)(x_4-x_3)}{(x_4-x_3)(y_2-y_1) - (y_4-y_3)(x_2-x_1)} \quad \text{(3.73)}$$
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
$$\frac{\sigma_m}{(P^*-1)M^{P^*-1}} \approx \frac{\sigma_m}{(P^*-1)(1+(P^*-1)(M-1))} \quad \text{(3.82)}$$
> SWAN: $M=$FRINTH, $P^*=$**PWTAIL(1)**, $m=$**MSC**. $P^*$ 는 적분량 의존 (예: $\overline{k}$ 계산 시 $P^* = P-2n-1$). **$P^* > 1$ 필수** (아니면 적분 실패).

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
보간 spectrum 평균주파수 (가중 $w_1+w_2=1$, $w_1$=첫 origin 까지 상대거리):
$$\overline{\sigma} = \frac{w_2 m_{1,1} + w_1 m_{2,1}}{w_2 m_{1,0} + w_1 m_{2,0}} \quad \text{(3.87)}$$

방향 moment:
$$m_{i,x} = \int N_i\cos\theta\,d\sigma d\theta \quad \text{(3.88)},\qquad m_{i,y} = \int N_i\sin\theta\,d\sigma d\theta \quad \text{(3.89)}$$
$$\overline{\theta}_i = \text{atan}\left(\frac{m_{i,y}}{m_{i,x}}\right) \quad \text{(3.90)},\qquad \overline{\theta} = \text{atan}\left[\frac{w_2 m_{1,y} + w_1 m_{2,y}}{w_2 m_{1,x} + w_1 m_{2,x}}\right] \quad \text{(3.91)}$$

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
- §3.16 (3.92) 최종 보간식: alt-text truncated 부분 보완 — 정밀 stretch/rotate 인자는 swantech.pdf p.113.

## 8. 연결

- [[swan-tech-ch2-obstacles-diffraction-setup]] — §2.5 obstacle 물리식(Goda/d'Angremond K_t)
- [[swan-tech-ch3-qc-curvilinear]] — §3.10 곡선 propagation(3.55, obstacle 3.70 의 base)
- [[swan-tech-ch3-breaking-source]] — §3.17 breaking source 수치 (다음)
- [[swan-tech-ch3-discretization]] — §3.2 BSBT (obstacle crossing fallback)
