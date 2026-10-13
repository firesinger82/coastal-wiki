---
title: "SWAN Scientific/Technical Ch 2 Governing equations — §2.1-2.2 verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Scientific/Technical Documentation, Cycle III 41.51, Delft 1993-2026) Ch 2 Governing equations, §2.1 Spectral description (p.7-10) + §2.2 Propagation of wave energy (p.10-12). Primary refs: Whitham 1974, Mei 1983, Komen et al. 1994, Holthuijsen 2007, Zijlema 2021."
citation_status: verified
verification_method: "raw PDF models/SWAN/raw/manuals/pdfs/swantech.pdf의 인쇄 7–13쪽(PDF 15–21쪽)을 직접 대조했다. 식 (2.1)–(2.26)의 원문과 인용한 코드 실행문을 대조했다. Figure 2.1의 Holthuijsen 2007 전재 표기를 확인했다. 2026-10-13 recovery 대조 보고서 R1–R8 반영" # [10-13 전수 검증 정정]
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "Claude Opus 4.7 (1M context) raw PDF direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — Eq 2.1-2.17 verbatim + Whitham/Mei/Komen/Holthuijsen citations"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-action-balance.md
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/manual-notes/swan-booij-1999-jgr-foundational.md
  - models/SWAN/source-analysis/swan-propagation-implementation.md
  - models/SWAN/source-analysis/swan-quasi-coherent.md
---

# SWAN swantech Ch 2 Governing equations — §2.1-2.2 verified verbatim

> swantech PDF 15–21쪽 / 인쇄 7–13쪽의 §2.1 스펙트럼 정의와 §2.2 전파식을 정리한다. 본문은 [swan-action-balance](swan-action-balance.md)의 구현 설명과 연결된다. [10-13 전수 검증 정정]

## 1. §2.1 Spectral description of wind waves (p.7-10)

### 1.1 Random-phase model (Eq 2.1)

> "Wind generated waves have irregular wave heights and periods, caused by the irregular nature of wind."

Random-phase model — sea surface = sum of harmonic waves, statistically independent:

$$\eta(t) = \sum_{i} a_i \cos(\sigma_i t + \alpha_i) \quad \text{(2.1)}$$

- $\eta$ = sea surface elevation
- $a_i$ = random amplitude of $i$-th wave (Rayleigh distributed)
- $\sigma_i$ = relative radian frequency (ambient current 존재 시)
- $\alpha_i$ = random phase (uniform 0 ~ 2π)
- Reference: **Holthuijsen 2007**

### 1.2 Dispersion relation + Doppler shift (Eq 2.2-2.3)

Ambient current 가 vertical uniform 가정 시 absolute radian frequency:

$$\omega = \sigma + \vec{k} \cdot \vec{u} \quad \text{(2.2)}$$

→ Doppler shift. $\vec{k} = (k_x, k_y)$ wave number vector.

Linear dispersion (relative frequency):

$$\sigma = \sqrt{g|\vec{k}| \tanh(|\vec{k}| d)} \quad \text{(2.3)}$$

- $g$ = 중력가속도
- $d$ = water depth

### 1.3 Variance density spectrum (Eq 2.4-2.6)

Auto-covariance Fourier 변환으로 정의:

$$E'(f) = \int_{-\infty}^{+\infty} C(\tau) e^{-2\pi i f \tau} d\tau \quad \text{(2.4)}$$

$$C(\tau) = \langle \eta(t) \eta(t+\tau) \rangle \quad \text{(2.5)}$$

- $f = \sigma/2\pi$ (Hz)
- $\langle \cdot \rangle$ = ensemble average
- $\tau$ = time lag

Stationary wave 조건에서 one-sided spectrum:

$$E(f) = 2E'(f) \text{ for } f \ge 0, \quad E(f) = 0 \text{ for } f < 0 \quad \text{(2.6)}$$

### 1.4 Total variance + energy (Eq 2.7-2.8)

$$\langle \eta^2 \rangle = C(0) = \int_0^{+\infty} E(f) df \quad \text{(2.7)}$$

→ $E(f)$ 가 variance density (m²/Hz).

$$E_{\text{tot}} = \frac{1}{2} \rho_w g \langle \eta^2 \rangle \quad \text{(2.8)}$$

문서 식 (2.8)은 $1/2$를 적는다. 이는 전체 에너지의 오기이다. 코드와 응력 식은 $E_{\rm tot}=\rho_wg\langle\eta^2\rangle$에 대응한다. (swantech PDF 16쪽 / 인쇄 8쪽, 식 (2.8); `src/SwanComputeForce.ftn90:306` `fx(ivert) = -RHO * GRAV * ( dsxxdx  + dsxydy )`; R1:TN-008)

### 1.5 2D directional spectrum (Eq 2.9)

Wave 문제 대부분 frequency-direction 동시 분포 필요:

$$E(f) = \int_0^{2\pi} E(f, \theta) d\theta \quad \text{(2.9)}$$

$E(f, \theta)$ = SWAN 의 표준 directional spectrum. **Figure 2.1**: North Sea local breeze + storm 의 1D vs 2D 비교 (Holthuijsen (2007) 재인쇄, Cambridge UP 허가).

### 1.6 Integral wave parameters (Eq 2.10-2.12)

$n$-th moment:

$$m_n = \int_0^{\infty} f^n E(f) df \quad \text{(2.10)}$$

$m_0 = \langle \eta^2 \rangle$. Significant wave height:

$$H_s = 4\sqrt{m_0} \quad \text{(2.11)}$$

Wave periods (3가지):

$$T_{m01} = \frac{m_0}{m_1}, \quad T_{m02} = \sqrt{\frac{m_0}{m_2}}, \quad T_{m-10} = \frac{m_{-1}}{m_0} \quad \text{(2.12)}$$

### 1.7 SWAN 사용 변수

> "In SWAN, the energy density spectrum $E(\sigma, \theta)$ is generally used. On a larger scale the spectral energy density function $E(\sigma, \theta)$ becomes a function of space and time, that is, $E(\vec{x}, t; \sigma, \theta)$ and wave dynamics should be considered to determine the evolution of the spectrum in space and time."

진화 미지수는 작용밀도 $N=E/\sigma$이다. $E$는 분산밀도이다. (swantech PDF 19쪽 / 인쇄 11쪽, 식 (2.16); R1 §4의 TN-018–023 수정안)

구면 밀도 $\widetilde N=N R^2\cos\varphi$를 쓰면 원천항에도 같은 Jacobian이 필요하다. 코드는 $N$의 남북 플럭스에 $\cos\varphi_{\rm up}/\cos\varphi_P$를 곱한다. (swantech PDF 20–21쪽 / 인쇄 12–13쪽, 식 (2.19) 및 Jacobian 정의; `src/swancom5.ftn:2167` `&              AC2(ID,IS,KCGRD(IC)) * COSLAT(IC) / COSLAT(1)`; R1:TN-023·TN-031)

## 2. §2.2 Propagation of wave energy (p.10-12)

### 2.1 §2.2.1 Wave kinematics — Whitham 1974, Mei 1983 (Eq 2.13-2.15)

> "Using the linear wave theory and the conservation of wave crests, the wave propagation velocities in spatial space within Cartesian framework and spectral space can be obtained from the kinematics of a wave train (Whitham, 1974; Mei, 1983)"

Propagation velocity 3개 (geographical 2 + spectral 2 = 4 component):

$$
\begin{aligned}
\frac{d\vec{x}}{dt} &= (c_x, c_y) = \vec{c}_g + \vec{u} = \frac{1}{2}\left(1 + \frac{2|\vec{k}|d}{\sinh(2|\vec{k}|d)}\right) \frac{\sigma \vec{k}}{|\vec{k}|^2} + \vec{u} \\
\frac{d\sigma}{dt} &= c_\sigma = \frac{\partial \sigma}{\partial d}\left(\frac{\partial d}{\partial t} + \vec{u} \cdot \nabla_{\vec{x}} d\right) - c_g \vec{k} \cdot \frac{\partial \vec{u}}{\partial s} \\
\frac{d\theta}{dt} &= c_\theta = -\frac{1}{k}\left(\frac{\partial \sigma}{\partial d} \frac{\partial d}{\partial m} + \vec{k} \cdot \frac{\partial \vec{u}}{\partial m}\right)
\end{aligned} \quad \text{(2.13)}
$$

- $c_x, c_y$ = spatial propagation velocities
- $c_\sigma$ = spectral propagation in $\sigma$ space (depth + current 변화로 인한 frequency shift)
- $c_\theta$ = spectral propagation in $\theta$ space (depth + current induced refraction)
- $\vec{u} = (u_x, u_y)$ = ambient current
- $s$ = wave propagation direction의 공간 좌표
- $m$ = $s$ 의 수직 좌표
- 주의: $c_\theta$ 는 **diffraction 효과 미포함** (§2.5.4 별도 처리)

Wave number magnitude + direction:

$$\vec{k} = (k_x, k_y) = (|\vec{k}|\cos\theta, |\vec{k}|\sin\theta) \quad \text{(2.14)}$$

Total derivative operator:

$$\frac{d}{dt} = \frac{\partial}{\partial t} + (\vec{c}_g + \vec{u}) \cdot \nabla_{\vec{x}} \quad \text{(2.15)}$$

### 2.2 §2.2.2 Spectral action balance equation (Eq 2.16-2.17)

**핵심 정의**:
> "The action density is defined as $N = E/\sigma$ and is **conserved during propagation** along its wave characteristic in the presence of ambient current, whereas energy density $E$ is not (**Whitman, 1974**). Wave action is said to be **adiabatic invariant**."

**핵심 식 (Eq 2.16)** — Mei 1983 + **Komen et al. 1994**:

$$\boxed{\frac{\partial N}{\partial t} + \nabla_{\vec{x}} \cdot \left[(\vec{c}_g + \vec{u}) N\right] + \frac{\partial c_\sigma N}{\partial \sigma} + \frac{\partial c_\theta N}{\partial \theta} = \frac{S_{\text{tot}}}{\sigma}} \quad \text{(2.16)}$$

**LHS 항 해석**:
1. $\partial N/\partial t$ — kinematic part (local change)
2. $\nabla_{\vec{x}} \cdot [(\vec{c}_g + \vec{u})N]$ — **2D geographical propagation** (shoaling 포함, $\vec{c}_g = \partial\sigma/\partial\vec{k}$ from $\sigma^2 = g|\vec{k}|\tanh(|\vec{k}|d)$)
3. $\partial c_\sigma N/\partial \sigma$ — **σ-shifting** (depth + mean current 변화)
4. $\partial c_\theta N/\partial \theta$ — **depth + current induced refraction**

**RHS**: $S_{\text{tot}}$ = non-conservative source/sink — energy density $E(\sigma, \theta)$ 단위 (not action). §2.3 deep.

### 2.3 Deep water no current (Eq 2.17)

$\sigma = \omega$, $N = E/\sigma$ 단순화:

$$\frac{\partial E}{\partial t} + \nabla_{\vec{x}} \cdot (\vec{c}_g E) = S_{\text{tot}} \quad \text{(2.17)}$$

→ **wave packet ray equation** along wave ray. Source/sink 없으면 energy conserved.

## 2b. §2.4 The influence of ambient current on waves (node24, 서술)

> swantech §2.4 직접 read — action balance 채택의 **물리적 정당화**.

Ambient current(tidal·ocean·wind-generated·river·wave-generated)은 wave growth/decay 에 영향 (Yu 1952, Hedges 1985, Lia 1989). **강한 역류**서:
- wave steepness·height **급증**, **wave blocking** (current 가 군속도 접근) + current-induced **whitecapping·reflection**
- **blocking frequency**서 action 이 nonlinear wave-wave interaction 으로 고/저주파로 부분 전이 (Ris 1997)

이론적 기반은 Longuet-Higgins와 Stewart(1960, 1961, 1962)의 파랑·흐름 상호작용 연구이다. 문서는 흐름 위에서 전파할 때 에너지밀도 대신 작용밀도를 보존한다고 설명한다. SWAN은 이 설명을 근거로 작용량 수지식을 채택한다. 근거: swantech PDF 60쪽 / 인쇄 52쪽 §2.4 및 PDF 19쪽 / 인쇄 11쪽 식 (2.16). 흐름 굴절은 [swan-tech-ch3-refraction-limiter](swan-tech-ch3-refraction-limiter.md)를 참조한다. [10-13 전수 검증 보완]

## 3. 핵심 references (Ch 2 인용)

- **Whitham 1974** — Linear and Nonlinear Waves (Wiley) — wave kinematics 원전, action density conservation 증명
- **Mei 1983** — The Applied Dynamics of Ocean Surface Waves (World Scientific) — Eq 2.13 + 2.16 derivation
- **Komen et al. 1994** — Dynamics and Modelling of Ocean Waves (Cambridge UP) — WAM 표준 reference, source term framework
- **Holthuijsen 2007** — Waves in Oceanic and Coastal Waters (Cambridge UP) — Eq 2.1 random-phase + Fig 2.1 (수업용 표준 교재)
- **Zijlema 2021** — variance vs energy density 정확 구분 (별도 paper)
- 1차 SWAN paper: [swan-booij-1999-jgr-foundational](swan-booij-1999-jgr-foundational.md) (Booij·Ris·Holthuijsen 1999 JGR)

## 4. 본 위키 cross-references

### 4.1 [swan-action-balance](swan-action-balance.md) 와 보완

본 위키 기존 [swan-action-balance](swan-action-balance.md) = source-analysis level (구현). 본 노트 = theory level (Eq 2.16 verbatim). 두 노트는 상호 보완.

### 4.2 §2.1 의 implementation

- $E(\sigma, \theta) \to N = E/\sigma$ 변환: SWAN 내부 `ac2(MDC, MSC)` array
- $H_s = 4\sqrt{m_0}$ output: User cmd `BLOCK HSIGN`
- $T_{m01}, T_{m02}, T_{m-10}$: User cmd `BLOCK TMM10 TM01 TM02`

### 4.3 §2.2 의 implementation

- Eq 2.13 propagation velocities → `SwanPropvelX/SwanPropvelS` ([swan-source-coverage-audit](../source-analysis/swan-source-coverage-audit.md))
- Eq 2.16 action balance → `SwanCompUnstruc` ([swan-unstructured-time-step](../source-analysis/swan-unstructured-time-step.md)) + swancom1.ftn
- $c_\theta$는 수심·흐름 굴절의 방향 전파속도이다. 근거: swantech PDF 18쪽 / 인쇄 10쪽 (2.13); [swan-propagation-implementation](../source-analysis/swan-propagation-implementation.md). GSE 억제는 별도의 공간 확산 보정이다. 근거: `src/SwanGSECorr.ftn90:40`; [swan-gse-correction](../source-analysis/swan-gse-correction.md). [10-13 전수 검증 정정]
- $c_\sigma$ = σ-shifting → [swan-propagation-implementation](../source-analysis/swan-propagation-implementation.md) §σ space

### 4.4 §2.5.4 diffraction (별도) + §2.7 QCM (Wigner)

Eq 2.13 의 $c_\theta$ 는 diffraction 미포함. 회절 처리:
- 표준 mild-slope diffraction → [swan-diffraction-obstacles](../source-analysis/swan-diffraction-obstacles.md) (Holthuijsen 2003 후속)
- Wigner-based **quasi-coherent** → [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md) (Akrish-Smit-Zijlema 41.90)

## 5. 한계

- 본 노트는 **§2.1-2.2 만** verified (p.7-12, 6 페이지). §2.3 sources/sinks (S_in/S_ds/S_nl) + §2.4 current + §2.5 obstacles + §2.6 setup + §2.7 QCM은 별도 chapter notes 예정.
- 식 LaTeX 표기는 PDF verbatim 옮김 — display issue 시 PDF 원본 참조.
- $E(\vec{x}, t; \sigma, \theta)$ vs $N$ vs $E(f, \theta)$ 표기 차이 (frequency vs radian frequency) 별도 표 가치.
- §2.7 quasi-homogeneous 가정 (line p.9) 의 SWAN 적용 한계 별도.
- Komen et al. 1994 / Holthuijsen 2007 인용 페이지 별도.

## 6. 연결

- [swan-action-balance](swan-action-balance.md) — source-level action balance
- [swan-documentation-stack](swan-documentation-stack.md) — 4 PDFs TOC + §2.2.2 매핑
- [swan-booij-1999-jgr-foundational](swan-booij-1999-jgr-foundational.md) — Booij 1999 JGR 원논문 (§1.4 reference)
- [swan-propagation-implementation](../source-analysis/swan-propagation-implementation.md) — Eq 2.13 implementation
- [swan-unstructured-time-step](../source-analysis/swan-unstructured-time-step.md) — Eq 2.16 unstructured implementation
- [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md) — §2.7 Wigner 확장 (별도 chapter 노트)
- [swan-diffraction-obstacles](../source-analysis/swan-diffraction-obstacles.md) — §2.5.4 diffraction
- [swan-gse-correction](../source-analysis/swan-gse-correction.md)은 GSE를 억제하는 파령 의존 공간 확산을 설명한다. 근거: `src/SwanGSECorr.ftn90:40`의 `diffusion terms in x-y space`. [10-13 전수 검증 정정]

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

확정 결론과 원문 인용: [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-001 | 문서 식 (2.1) | swantech PDF 15쪽 / 인쇄 7쪽, (2.1): $\eta(t)=\sum_i a_i\cos(\sigma_i t+\alpha_i)$. | `src/swancom1.ftn:9802` `ACS2  = SPCSIG(IS)**2 * AC2(ID,IS,INDX)` | H 코드 대조 대상 아님 | 수면 시계열의 통계적 표현이다. 위상별 수면 재구성을 작용 평형 해법의 완료 조건으로 삼지 않는다. |
| R1:TN-003 | 문서 식 (2.3) | swantech PDF 16쪽 / 인쇄 8쪽, (2.3): $\sigma=\sqrt{g\lvert\vec k\rvert\tanh(\lvert\vec k\rvert d)}$.<br>웹 [수정 이력](../raw/manuals/website/modifications/modifications.htm):596–598은 `Pade approximation for the wave celerity`를 명시한다. | `src/swanser.ftn:713–715` `C     = SQRT(GRAV*D/(SND2+1./(1.+0.666*SND2+0.445*SND2**2`; `&                                  -0.105*SND2**3+0.272*SND2**4)))`; `K(IS) = SIG(IS)/C` | C 문서 누락 | KSCIP1은 분산 관계를 구간별 근사로 계산한다. Padé 근사의 존재는 웹 수정 이력에도 있다. C는 swantech 식 (2.3)에 `IF (SND.GE.2.5) THEN`, `ELSE IF (SND.LT.1.E-6) THEN`과 유한 수심 유리식이 없는 점으로 한정한다. |
| R1:TN-004 | 문서 식 (2.4) | swantech PDF 16쪽 / 인쇄 8쪽, (2.4): $E'(f)=\int_{-\infty}^{+\infty}C(\tau)e^{-2\pi if\tau}d\tau$. | — | H 코드 대조 대상 아님 | 공분산과 스펙트럼의 정의다. |
| R1:TN-005 | 문서 식 (2.5) | swantech PDF 16쪽 / 인쇄 8쪽, (2.5): $C(\tau)=\langle\eta(t)\eta(t+\tau)\rangle$. | — | H 코드 대조 대상 아님 | 앙상블 공분산의 정의다. |
| R1:TN-006 | 문서 식 (2.6) | swantech PDF 16쪽 / 인쇄 8쪽, (2.6): $E(f)=2E'(f)$ for $f\ge0$ and $E(f)=0$ for $f<0$. | `src/swanpre1.ftn:4689` `SPCSIG(1) = SLOW` | H 코드 대조 대상 아님 | 양측 스펙트럼과 단측 스펙트럼의 정의다. 음의 주파수 배열 변환을 요구하는 식이 아니다. |
| R1:TN-008 | 문서 식 (2.8) | swantech PDF 16쪽 / 인쇄 8쪽, (2.8): $E_{\rm tot}=\frac12\rho_wg\langle\eta^2\rangle$. | `src/SwanComputeForce.ftn90:179,187,195,306` `sxxsumd = sxxsumd + ( n(1)*(spcdir(id,4) + 1.) -0.5 ) * ac2(id,is,ivert)`; `sxxsums = sxxsums + sxxsumd * spcsig(is)**2`; `sxx(ivert) = sxxsums * DDIR * FRINTF`; `fx(ivert) = -RHO * GRAV * ( dsxxdx  + dsxydy )` | B 문서 오기 | 해석: 문서는 분산에 $\rho g/2$를 곱한다. 같은 문서 (3.59)와 (8.30), 코드의 힘 계산은 분산에 $\rho g$를 곱한다. 진폭 제곱의 $1/2$와 분산을 혼동한 계수다. |
| R1:TN-017 | 문서 식 (2.15) | swantech PDF 19쪽 / 인쇄 11쪽, (2.15): $d/dt=\partial_t+(\vec c_g+\vec u)\cdot\nabla_{\vec x}$. | `src/swancom5.ftn:2183–2184` `IMATRA(ID,IS) = IMATRA(ID,IS) + FXY2 + ACOLD*RDTIM`; `IMATDA(ID,IS) = IMATDA(ID,IS) + FXY1 + RDTIM` | H 코드 대조 대상 아님 | 공간 경로를 따라 정의한 미분 연산자다. 코드가 직접 이 연산자를 별도 계산하는 것은 아니다. 스펙트럼 특성곡선의 전체 미분은 (3.33)에 추가 항을 포함한다. |
| R1:TN-021 | 에너지 플럭스 곱미분 | swantech PDF 20쪽 / 인쇄 12쪽, 번호 없음: $\partial_tE+\vec c_g\cdot\nabla E+E\nabla\cdot\vec c_g=S_{\rm tot}$. | `src/swancom5.ftn:2153` `FXY2 =  RDX(1) * CAX(ID,IS,2)* TCF1 * AC2(ID,IS,IND2)` | F 표기 차이 | 해석: $\nabla\cdot(\vec c_gE)=\vec c_g\cdot\nabla E+E\nabla\cdot\vec c_g$이다. 코드가 이웃점의 속도와 밀도를 함께 곱하므로 천수화 항을 빠뜨리지 않는다. |
| R1:TN-023 | 문서 식 (2.19) | swantech PDF 20쪽 / 인쇄 12쪽, (2.19): $\partial_t\widetilde N+\partial_\lambda(c_\lambda\widetilde N)+\partial_\varphi(c_\varphi\widetilde N)+\partial_\sigma(c_\sigma\widetilde N)+\partial_\theta(\widetilde c_\theta\widetilde N)=S_{\rm tot}/\sigma$. | `src/swancom5.ftn:2167` `&              AC2(ID,IS,KCGRD(IC)) * COSLAT(IC) / COSLAT(1)` | B 문서 오기 | 해석: 문서가 뒤에서 정의한 $\widetilde N=NR^2\cos\varphi$를 적용하면 이 식의 우변에도 $R^2\cos\varphi$가 필요하다. 원천항 기호를 재정의하지 않고 (2.26)을 얻을 수 없다. 코드의 (2.26) 경로에는 이 누락이 없다. |
| R1:TN-026 | 문서 식 (2.22) | swantech PDF 21쪽 / 인쇄 13쪽, (2.22): $R\cos\varphi\cos\theta=\mathrm{constant}$. | `src/swancom5.ftn:1918–1921` `CTTMP = ECOS(ID) * TANLAT / REARTH`; `CAD(ID,IS,1) = CAD(ID,IS,1) -`; `&           (CAX(ID,IS,1)*ECOS(ID) + CAY(ID,IS,1)*ESIN(ID)) * CTTMP` | H 코드 대조 대상 아님 | 심해·무흐름에서 대권 굴절 항을 유도하는 Clairaut 관계다. |
| R1:TN-027 | 문서 식 (2.23) | swantech PDF 21쪽 / 인쇄 13쪽, (2.23): $-R\sin\varphi\cos\theta\,d\varphi/ds-R\cos\varphi\sin\theta\,d\theta/ds=0$. | — | H 코드 대조 대상 아님 | (2.22)의 미분식이다. |
| R1:TN-028 | 구면 경로의 거리·위도 관계 | swantech PDF 21쪽 / 인쇄 13쪽, 번호 없음: $dy=ds\sin\theta,\ d\varphi/ds=\sin\theta/R,\ ds=(c_x\cos\theta+c_y\sin\theta)dt$. | — | H 코드 대조 대상 아님 | 대권 항 유도의 중간식이다. 흐름이 파향과 평행하지 않으면 공간 에너지 경로와 파수 방향을 구분해야 한다. |
| R1:TN-031 | 구면 작용밀도 Jacobian | swantech PDF 21쪽 / 인쇄 13쪽, 번호 없음: $\widetilde N\,d\sigma d\theta d\varphi d\lambda=N\,d\sigma d\theta dxdy$, $\widetilde N=NR^2\cos\varphi$. | `src/swancom5.ftn:2167` `&              AC2(ID,IS,KCGRD(IC)) * COSLAT(IC) / COSLAT(1)` | F 표기 차이 | 해석: 코드는 $\widetilde N$ 배열을 만들지 않는다. $N$의 남북 플럭스에 $\cos\varphi_{\rm up}/\cos\varphi_P$를 곱한다. |
| R1:TN-034 | 흐름 차단의 관측 현상 | swantech PDF 60쪽 / 인쇄 52쪽, §2.4: “often accompanied with current-induced whitecapping and wave reflections.” | `src/swancom1.ftn:3702–3715` `ELSE IF (INT(PNUMS(8)).EQ.2 .OR. INT(PNUMS(8)).EQ.3) THEN` | H 코드 대조 대상 아님 | 이 문장은 관측 현상의 서술이다. 흐름 차단에 의한 반사를 SWAN이 구현한다는 기능 선언으로 옮기면 안 된다. |
| R1:TC-001 | 분산 관계의 심해·천해 분기와 유한 수심 근사 | 웹 [수정 이력](../raw/manuals/website/modifications/modifications.htm):596–598은 위상속도의 Padé 근사를 설명한다. | `src/swanser.ftn:699–719` `IF (SND.GE.2.5) THEN`; `ELSE IF (SND.LT.1.E-6) THEN` | C 문서 누락 | 분산 관계 근사의 존재는 웹 수정 이력에도 있다. C는 swantech 식 (2.3)에 KSCIP1의 심해·극천해 분기 문턱과 유한 수심 근사 계수가 없는 점으로 한정한다. |
