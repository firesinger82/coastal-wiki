---
title: "SWAN swantech Ch 3.8 Refraction in large-scale applications — Lipschitz/CFL_θ + c_θ refraction limiter (REFRLIM) verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.8 On the approximation of refraction in large-scale SWAN applications (§3.8.1-3.8.5), doc p.92-101 (Eq 3.31-3.43). References: Whitham 1974, Holthuijsen 2007, Dietrich et al. 2013, Booij (unpublished note 1998), Snel's law."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §3.8 직접 read via pdftotext (식 번호 context-verified: energy balance 3.31·Lipschitz 3.35·CFL_θ Cr≡|c_θ|ΔT/Δθ 3.38·c_θ depth 3.40·refraction limiter 3.41·c_θ depth-form 3.42·c_θ phase-velocity-form 3.43) + website_markdown node49-54.md LaTeX alt-text. 식 번호는 PDF 번호 (online HTML +15 offset; Snel's law Booij 1998·중간 유도식은 PDF 무번호)."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 3.31-3.43 + α_θ=0.9 default + 버전 history verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch3-discretization.md
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
  - models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md
  - models/SWAN/source-analysis/swan-unstructured-time-step.md
---

# swantech Ch 3.8 Refraction limiter (REFRLIM) — verified verbatim

> swantech.pdf (v41.51) §3.8 직접 read. **대규모(특히 unstructured) SWAN 의 "겉보기 불안정"** — coarse grid 의 과도 refraction 으로 wave ray 가 거짓 교차 → 단일 격자점 에너지 집중 → 비현실적 대파고/장주기 (Dietrich et al. 2013). 해법: **CFL_θ refraction limiter** ($c_\theta$ 상한). ADCIRC+SWAN 결합 운영에서 핵심.
>
> **식 번호 주의**: PDF 번호 사용 (online HTML은 누적 +15 offset, 예: refraction limiter HTML 3.73 = PDF 3.41). Snel's law(Booij 1998)·중간 유도식은 PDF 무번호.

## 0. 문제 (§3.8.1)

대규모 응용의 불안정 2 원인:
1. **Coarse grid (특히 unstructured)** — turning rate 정확도 (§3.8.5)
2. **Non-stationary refraction 항의 fully implicit 처리** — 큰 time step 시 $c_\theta$ 를 갱신점에서 결정. $c_\theta$ 가 1 step 에 과변하면 causality 깨짐. 소규모 연안엔 보통 무문제.

> Oceanic 대규모: seamount 등에서 인접 격자 수심이 10배+ 변동 → 최천수 격자점 $c_\theta$ 가 격자간 구간을 대표 못함 → 제한 필요. 목표: 대규모는 smooth, 소규모는 무영향.

## 1. Energy transport along wave rays (§3.8.2, Eq 3.31-3.35)

Wave energy balance (source/sink·current 무시):
$$\frac{\partial E}{\partial t} + \nabla_{\vec{x}}\cdot(\vec{c}_g E) + \frac{\partial c_\theta E}{\partial\theta} = 0 \quad \text{(3.31)}$$

Characteristic 형 (Whitham 1974: $\vec{c}_g E, c_\theta E$ 가 characteristic 따라 일정):
$$\frac{dE}{dt} = -\left(\nabla_{\vec{x}}\cdot\vec{c}_g + \frac{\partial c_\theta}{\partial\theta}\right)E \quad \text{(3.32)}$$
$$\frac{dE}{dt} \equiv \frac{\partial E}{\partial t} + \vec{c}_g\cdot\nabla_{\vec{x}}E + c_\theta\frac{\partial E}{\partial\theta} \quad \text{(3.33)}$$
- slopes (PDF 무번호): $d\vec{x}/dt = \vec{c}_g$, $d\theta/dt = c_\theta$
- stationary characteristic: $d\vec{x}/d\theta = \vec{c}_g/c_\theta$ **(3.34)**

RHS 는 source/sink (군속도·turning rate gradient 의존). **Relaxation time** (PDF 무번호): $\tau^{-1} = |\nabla_{\vec{x}}\cdot\vec{c}_g + \partial c_\theta/\partial\theta|$. 정확 적분엔 step size $\Delta T < \tau$ →

$$\left|\nabla_{\vec{x}}\cdot\vec{c}_g + \frac{\partial c_\theta}{\partial\theta}\right|\Delta T < 1 \quad \text{(3.35)}$$
> **Lipschitz criterion** — 전통 CFL보다 덜 엄격. **max step size 가 안정성이 아니라 정확도로 결정**됨 (wave propagation field 곡률 관련). 큰 bottom slope 위치선 $\Delta T$ 국소 축소 필요.
>
> 연안 grid 20-50 m / oceanic 10-50 km. Seamount 처럼 수심 10배+ 변동 시 (3.35) 위배 → 파성분이 1 step 에 여러 bin jump → ray 교차·causality 위반·불안정.

## 2. Refraction in non-stationary (§3.8.3, Eq 3.36-3.41) — 핵심

균일분포 가정 시 $dE/dt = -\frac{\partial c_\theta}{\partial\theta}E$ (PDF 무번호). Geographic total derivative:
$$\frac{dE}{dt} = \frac{\partial E}{\partial t} + c_x\frac{\partial E}{\partial x} + c_y\frac{\partial E}{\partial y} \quad \text{(3.36)}$$

First-order upwind + implicit Euler (first sweep $c_x,c_y>0$) → **semi-Lagrangian** 해석:
$$\frac{E^n_{i,j} - E^{n-1}_{i^*,j^*}}{\Delta T} \quad \text{(3.37)}$$
- $i^* = i - p$, $j^* = j - q$, $p = c_x\Delta T/\Delta x$, $q = c_y\Delta T/\Delta y$ (Courant 수, 비정수 → $(i^*,j^*)$ 는 characteristic 상의 비격자점, 보간으로 획득)
- $\Delta T$ = **Lagrangian time step** ($\Delta t, \Delta x, \Delta y$ 함수, $\Delta T < \Delta t$, Eulerian $\Delta t$ 와 구분)

### 2.1 CFL_θ Courant 기준 (핵심)

Causality: refract 되는 에너지는 사이 모든 bin 통과해야. Lipschitz (3.35)의 현 맥락:
$$\left|\frac{\partial c_\theta}{\partial\theta}\right|\Delta T < 1 \quad \text{(PDF 무번호)}$$
→ **directional Courant 수 < 1**:
$$\boxed{\text{Cr} \equiv \frac{|c_\theta|\Delta T}{\Delta\theta} < 1} \quad \text{(3.38)}$$
> $\Delta T$ 동안 $\theta$ 이동이 최대 $\Delta\theta$ + 파성분이 directional sector 경계 안 넘음(첫·끝 bin 제외) → ray 교차 방지. **안정성 아닌 물리 정확도(causality)용.** $d\theta/dt = c_\theta$ **(3.39)**, $\theta^n \approx \theta^{n-1} + c_\theta\Delta T$ (PDF 무번호).

Coarse nested grid 예 (정상·long-crested, bottom gradient, 무전류): spatial turning rate $d\theta/dx = c_\theta/c_g$. $\Delta x$ 당 crest 회전 $= (c_\theta/c_g)\Delta x$ (PDF 무번호), Courant $= \frac{|c_\theta|}{c_g}\frac{\Delta x}{\Delta\theta} < 1$ (PDF 무번호).

Turning rate (PDF 3.40):
$$c_\theta = -\frac{1}{k}\frac{\partial\sigma}{\partial h}\frac{\partial h}{\partial m} \quad \text{(3.40)}$$
($m$ = crest 따라 좌표). Coarse grid 서 $\Delta h$ (즉 $c_\theta$) 매우 큼 (저주파·천수) → Lipschitz 위배 ($\text{Cr}\ge1$).

> **Dietrich et al. (2013)**: steep bottom gradient + 부실 해상도서 refraction 과도 → wave ray 거짓 교차 → 단일 격자점 에너지 집중 → 비현실적 대파고·장주기.

### 2.2 Refraction limiter (REFRLIM)

(3.38)서 $|c_\theta| < \Delta\theta/\Delta T$ (PDF 무번호). $1/\Delta T$ 를 $1/\Delta t + |c_x|/\Delta x + |c_y|/\Delta y$ 의 일부로 추정 →

$$\boxed{|c_\theta| \le \alpha_\theta\Delta\theta\left(\frac{|c_x|}{\Delta x} + \frac{|c_y|}{\Delta y}\right)} \quad \text{(3.41)}$$
- $\alpha_\theta$ = **user-defined max Courant 수 (<1), SWAN default $\alpha_\theta = 0.9$** ($\Delta t$ 항 무시한 안전마진 형)
- 국소 영향 가능 (depending on $\alpha_\theta$). **연안/fine grid 엔 무영향** (turning rate 1 step 내 미변). **과도 refraction 만 억제하는 effective survival measure.**

## 3. 역사적 배경 — Booij 1998 (§3.8.4, PDF 무번호)

Nico Booij 1998년 11월 최초 착안. 평행 등수심선 sector, $(i,j)$ 천수, $(i-1,j)·(i,j-1)$ 심수. Snel's law (Holthuijsen 2007 NOTE 7A pg.207): $d\theta/dn = \frac{1}{c}\frac{dc}{dn}\tan\theta$. $\theta\approx45°$ → $d\theta/dn = \frac{1}{c}\frac{dc}{dn}$. 천수 $c=\sqrt{gh}$ → $d\theta/dn = \frac{1}{2h}\frac{dh}{dn}$. Step 당 방향변화 $\frac{d\theta}{dn}\Delta n = \frac{h_*-h_{i,j}}{2h_{i,j}}$. 안정엔 $<90°$ →
$$h_* - h_{i,j} \le \pi h_{i,j}\quad\text{(PDF 무번호)}$$
> 프로그램선 $\pi$ → user factor $\beta$. 주변 격자 수심을 $\beta h_{i,j}$ 로 감소(초과 시). **미발표 노트, 충분히 효과적이지 않았음.**

## 4. Coarse grid turning rate 정확도 (§3.8.5, Eq 3.42-3.43) — 41.01AB 변경

SWAN 의 turning rate 2 형 (수학적 동일, 수치 결과 상이):

**Depth form (구식, 41.01A 까지):**
$$c_\theta = \frac{\sigma}{\sinh 2kh}\left(\frac{\partial h}{\partial x}\sin\theta - \frac{\partial h}{\partial y}\cos\theta\right) \quad \text{(3.42)}$$
> coarse + steep slope 서 부정확.

**Phase velocity form (신식):**
$$c_\theta = -\frac{c_g}{c}\frac{\partial c}{\partial m}\quad\text{(PDF 무번호)} = \frac{c_g}{c}\left(\frac{\partial c}{\partial x}\sin\theta - \frac{\partial c}{\partial y}\cos\theta\right) \quad \text{(3.43)}$$
> **장점**: mud(non-rigid seafloor) refraction 포함 가능 → **41.01 구현**. Coarse 해상도서도 high-resolution 과 유사 결과. **버전 41.01AB 부터 (3.42) → (3.43) 교체.**

**미분 근사 (PDF 무번호):**
- 41.01A 까지: 1차 backward $\partial c/\partial x \approx (c_{i,j}-c_{i-1,j})/\Delta x$ — coarse 부정확 + 비물리 비대칭
- **41.01AB 부터: 2차 central** $\partial c/\partial x \approx (c_{i+1,j}-c_{i-1,j})/2\Delta x$

Structured grid SWAN 적용형 (PDF 무번호):
$$c_{\theta,i,j} = \frac{c_{g,i,j}}{c_{i,j}}\left(\frac{c_{i+1,j}-c_{i-1,j}}{2\Delta x}\sin\theta - \frac{c_{i,j+1}-c_{i,j-1}}{2\Delta y}\cos\theta\right)$$
> $(i,j)$ = 최천수. $c_{i,j}$ 로 나눔은 Snel's law 와 불일치 → turning rate 과대 (큰 bottom slope 시 1 bin+ 회전) → **refraction limiter (3.41) 정당화.** $\alpha_\theta=0.9$ 는 장파용, 단파는 $\alpha_\theta=0.5$, 평행 등수심선 $90°$ 한계면 $\alpha_\theta=9$ ($\Delta\theta=10°$) 도 가능.
>
> **Unstructured grid**: 1차 근사 → Green-Gauss 공식(Eq 8.36) 으로 대체. 본 위키 [[swan-unstructured-time-step]].

## 5. SWAN 옵션 매핑 (User cmd)

| Tech (PDF §3.8) | User cmd | 비고 |
|---|---|---|
| 3.41 refraction limiter | `NUMERIC ... REFRLIM [frac] [power]` | frac = $\alpha_\theta$ (default 0.9) |
| 3.42→3.43 c_θ phase-velocity | (internal, default since 41.01AB) | mud refraction 가능 |
| 3.38 CFL_θ 기준 | (이론 근거) | Cr < 1 causality |
| refraction on/off | `OFF REFRAC` / (default on) | |

## 6. 실무 함의

- **ADCIRC+SWAN coupled (unstructured)**: Dietrich 2013 가 정확히 이 문제 — coarse mesh + steep bathymetry 서 spurious wave height. REFRLIM (α_θ=0.9) 가 표준 완화책. 본 위키 [[swan-unstructured-time-step]] (SwanCompUnstruc, Casey Dietrich 41.20 기여).
- 41.01AB phase-velocity c_θ + central difference 가 coarse grid refraction 정확도 핵심 개선.
- limiter 가 nearshore/fine grid 해 왜곡 안 함 (turning rate 완만) — large-scale survival 전용.

## 7. 한계

- §3.8.3 중간 유도식(3.49-3.61 HTML: slopes·τ^-1·Cartesian Lipschitz·semi-Lag rewrite·θ evolution 3.64-66)은 **PDF 무번호** → 본 노트 무번호 인용.
- Snel's law β-factor (Booij 1998) + structured c_θ 식: PDF 무번호 display — 핵심 결과만 전사.
- §3.9 QC approximation (node55)·§3.10-3.17 (curvilinear·obstacles·spectral ops·breaking source)은 **다음 세션** (본 세션 §3.2-3.8 커버).

## 8. 연결

- [[swan-tech-ch3-discretization]] — §3.2 BSBT/GSE/hybrid (semi-Lagrangian 기반 공유)
- [[swan-tech-ch3-solution-iteration-limiter]] — §3.3-3.7 four-sweep (causality·sweep sector)
- [[swan-tech-ch2-governing-equations]] — c_θ turning rate 정의 (Eq 2.14 kinematics)
- [[swan-unstructured-time-step]] — SwanCompUnstruc (Dietrich 41.20, unstructured refraction Green-Gauss)
