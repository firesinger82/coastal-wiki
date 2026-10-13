---
title: "SWAN swantech Ch 3.8 Refraction in large-scale applications — Lipschitz/CFL_θ + c_θ refraction limiter (REFRLIM) verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.8 On the approximation of refraction in large-scale SWAN applications (§3.8.1-3.8.5), doc p.92-101 (Eq 3.31-3.43). References: Whitham 1974, Holthuijsen 2007, Dietrich et al. 2013, Booij (unpublished note 1998), Snel's law."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §3.8의 PDF 100–110쪽 / 인쇄 92–102쪽과 식 (3.31)–(3.43)을 대조했다. website/online_doc/swantech/node49.html–node54.html의 식 번호는 PDF와 개별 대조했다. HTML 번호와 PDF 번호의 차이는 일정하지 않다. 본문은 PDF 식 번호를 사용한다. 2026-10-13 recovery 대조 보고서 R1–R8 반영" # [10-13 전수 검증 정정]
last_source_check: "2026-10-13 (recovery 대조 반영)"
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
- 방향 CFL 계수 기본값은 0.9이다. 제한 스위치는 기본 0이다. (swantech PDF 108–110쪽 / 인쇄 100–102쪽; swanuse PDF 95쪽 / 인쇄 87쪽; `src/swanmain.ftn:1331` `PNUMS(35) = 0.0`; `src/swancom5.ftn:1710` `IF ( INT(PNUMS(35)) == 1 ) THEN`; R1:TN-106) [10-13 전수 검증 정정]
- 국소 영향 가능 (depending on $\alpha_\theta$). **연안/fine grid 엔 무영향** (turning rate 1 step 내 미변). **과도 refraction 만 억제하는 effective survival measure.**

## 3. 역사적 배경 — Booij 1998 (§3.8.4, PDF 무번호)

Nico Booij 1998년 11월 최초 착안. 평행 등수심선 sector, $(i,j)$ 천수, $(i-1,j)·(i,j-1)$ 심수. Snel's law (Holthuijsen 2007 NOTE 7A pg.207): $d\theta/dn = \frac{1}{c}\frac{dc}{dn}\tan\theta$. $\theta\approx45°$ → $d\theta/dn = \frac{1}{c}\frac{dc}{dn}$. 천수 $c=\sqrt{gh}$ → $d\theta/dn = \frac{1}{2h}\frac{dh}{dn}$. Step 당 방향변화 $\frac{d\theta}{dn}\Delta n = \frac{h_*-h_{i,j}}{2h_{i,j}}$. 안정엔 $<90°$ →
$$h_* - h_{i,j} \le \pi h_{i,j}\quad\text{(PDF 무번호)}$$
> 문서는 “depths in surrounding grid points are reduced to $\beta h_{i,j}$, if they are larger than this value.”라고 적는다. (swantech PDF 109쪽 / 인쇄 101쪽; R1:TN-108)

41.45 이후 조사한 공개 판에는 이웃 수심을 $\beta h$로 절단하는 계산이 없다. 41.45 소스의 주석은 해당 절차가 이미 제거됐다고 기록한다. 이 공개 판 범위에서 D를 확정한다. (`2980d1a:src/swancom5.ftn:1373` `!  The depth refraction limitation procedure (i.e. IREFR=-1) has been removed, because it is basically a "dirty fix" which           40.59`, 2023-02-27; [git D 판정](../../../_staging/recovery/compare/SWAN-git-verify-D.md); R1:TN-108)

## 4. Coarse grid turning rate 정확도 (§3.8.5, Eq 3.42-3.43) — 41.01AB 변경

SWAN 의 turning rate 2 형 (수학적 동일, 수치 결과 상이):

**Depth form (구식, 41.01A 까지):**
$$c_\theta = \frac{\sigma}{\sinh 2kh}\left(\frac{\partial h}{\partial x}\sin\theta - \frac{\partial h}{\partial y}\cos\theta\right) \quad \text{(3.42)}$$
> coarse + steep slope 서 부정확.

**Phase velocity form (정렬 기본):**
$$c_\theta = -\frac{c_g}{c}\frac{\partial c}{\partial m}\quad\text{(PDF 무번호)} = \frac{c_g}{c}\left(\frac{\partial c}{\partial x}\sin\theta - \frac{\partial c}{\partial y}\cos\theta\right) \quad \text{(3.43)}$$
> **장점**: mud(non-rigid seafloor) refraction 포함 가능 → **41.01 구현**. Coarse 해상도서도 high-resolution 과 유사 결과. **버전 41.01AB 부터 (3.42) → (3.43) 교체.**

**미분 근사 (PDF 무번호):**
- 41.01A 까지: 1차 backward $\partial c/\partial x \approx (c_{i,j}-c_{i-1,j})/\Delta x$ — coarse 부정확 + 비물리 비대칭
- **41.01AB 부터: 2차 central** $\partial c/\partial x \approx (c_{i+1,j}-c_{i-1,j})/2\Delta x$

Structured grid SWAN 적용형 (PDF 무번호):
$$c_{\theta,i,j} = \frac{c_{g,i,j}}{c_{i,j}}\left(\frac{c_{i+1,j}-c_{i-1,j}}{2\Delta x}\sin\theta - \frac{c_{i,j+1}-c_{i,j-1}}{2\Delta y}\cos\theta\right)$$
> $(i,j)$ = 최천수. $c_{i,j}$ 로 나눔은 Snel's law 와 불일치 → turning rate 과대 (큰 bottom slope 시 1 bin+ 회전) → **refraction limiter (3.41) 정당화.** $\alpha_\theta=0.9$ 는 장파용, 단파는 $\alpha_\theta=0.5$, 평행 등수심선 $90°$ 한계면 $\alpha_\theta=9$ ($\Delta\theta=10°$) 도 가능.
>
> 정렬 기본은 위상속도 기울기이다. 비정렬 기본은 파수 기울기이다. 비정렬 경로는 구면 보정 뒤 제한한다. 정렬 경로는 제한 뒤 구면 보정을 더한다. (`src/SwanPropvelS.ftn90:259–269` `cd(1) = -cgo(is,1) / kwave(is,1)`; `cd(2) = cd(1) * dkdx(is)`; `cd(3) = cd(1) * dkdy(is)`; `cad(id,is) = esin(id)*cd(2) - ecos(id)*cd(3)`; `src/SwanPropvelS.ftn90:286` `cad(id,is) = cad(id,is) - cd(2)*(cax(id,is,1)*ecos(id) + cay(id,is,1)*esin(id))`; R1:TC-003·TC-005)

## 5. SWAN 옵션 매핑 (User cmd)

| Tech (PDF §3.8) | User cmd | 비고 |
|---|---|---|
| 3.41 방향 CFL 제한 | `NUMERIC ... CTHETA` | 활성화 계수 기본값 0.9, 기본 비활성. (R1:TN-106) |
| 저주파 굴절 감쇠 | `NUMERIC ... REFRLIM` | `fac = min(1.,(spcsig(is)/frlim)**pp)`; 기본 비활성. (R1:TC-004) |
| 3.42→3.43 c_θ phase-velocity | 정렬 기본 | 비정렬 기본은 파수 기울기. (R1:TC-003) |
| 3.38 CFL_θ 기준 | (이론 근거) | Cr < 1 causality |
| refraction on/off | `OFF REFRAC` / (default on) | |

## 6. 실무 함의

- 방향 CFL 제한은 `NUMERIC CTHETA`로 켠다. 활성화 계수의 기본값은 0.9이다. 명령을 생략하면 제한기를 켜지 않는다. (swanuse PDF 95쪽 / 인쇄 87쪽; [비정렬 계산 노트](../source-analysis/swan-unstructured-time-step.md)) [10-13 전수 검증 정정]
- 41.01AB phase-velocity c_θ + central difference 가 coarse grid refraction 정확도 핵심 개선.
- limiter 가 nearshore/fine grid 해 왜곡 안 함 (turning rate 완만) — large-scale survival 전용.

## 7. 한계

- §3.8.3 중간 유도식(3.49-3.61 HTML: slopes·τ^-1·Cartesian Lipschitz·semi-Lag rewrite·θ evolution 3.64-66)은 **PDF 무번호** → 본 노트 무번호 인용.
- Snel's law β-factor (Booij 1998) + structured c_θ 식: PDF 무번호 display — 핵심 결과만 전사.
- §3.9 QC approximation (node55)·§3.10-3.17 (curvilinear·obstacles·spectral ops·breaking source)은 **다음 세션** (본 세션 §3.2-3.8 커버).

## 8. 연결

- [swan-tech-ch3-discretization](swan-tech-ch3-discretization.md) — §3.2의 공간·스펙트럼 이산화를 정리한다. [10-13 전수 검증 정정]
- [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) — §3.3-3.7 four-sweep (causality·sweep sector)
- [swan-tech-ch2-governing-equations](swan-tech-ch2-governing-equations.md) — 굴절 속도의 운동학적 정의는 swantech PDF 18쪽 / 인쇄 10쪽의 식 (2.13)에 있다. [10-13 전수 검증 정정]
- [swan-unstructured-time-step](../source-analysis/swan-unstructured-time-step.md) — SwanCompUnstruc (Dietrich 41.20, unstructured refraction Green-Gauss)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

확정 결론과 원문 인용: [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론), [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-094 | 문서 식 (3.32)·(3.33)·(3.34) | swantech PDF 101쪽 / 인쇄 93쪽, (3.32): $dE/dt=-(\nabla\cdot\vec c_g+\partial_\theta c_\theta)E$; (3.33): $dE/dt=\partial_tE+\vec c_g\cdot\nabla E+c_\theta\partial_\theta E$; 번호 없음 $d\vec x/dt=\vec c_g,\ d\theta/dt=c_\theta$; (3.34): $d\vec x/d\theta=\vec c_g/c_\theta$. | — | H 코드 대조 대상 아님 | 특성곡선 해석을 위한 곱 미분 전개이다. 코드는 입자 경로를 직접 적분하지 않는다. (3.34)는 $c_\theta\ne0$인 구간의 기울기이다. |
| R1:TN-095 | 문서 식 (3.35) | swantech PDF 102쪽 / 인쇄 94쪽, 번호 없음: $\tau^{-1}=\lvert\nabla\cdot\vec c_g+\partial_\theta c_\theta\rvert$; (3.35): $\lvert\nabla\cdot\vec c_g+\partial_\theta c_\theta\rvert\Delta T<1$. | — | H 코드 대조 대상 아님 | 문서는 정확도를 위한 Lipschitz 조건을 유도한다. 이 발산을 계산해 시간 간격을 선택하는 알고리즘을 선언하지 않는다. |
| R1:TN-096 | 문서 식 (3.36) | swantech PDF 103–104쪽 / 인쇄 95–96쪽, 번호 없음: $dE/dt=-(\partial_\theta c_\theta)E$; (3.36): $dE/dt=\partial_tE+c_x\partial_xE+c_y\partial_yE$; $dx/dt=c_x,dy/dt=c_y$. | — | H 코드 대조 대상 아님 | 방향별 에너지가 균일하다는 가정 아래의 예시이다. 일반 특성미분에서 방향 이류항을 항상 생략한다는 뜻이 아니다. |
| R1:TN-098 | 문서 식 (3.37) | swantech PDF 105쪽 / 인쇄 97쪽, (3.37): $(E_{ij}^n-E_{i^*,j^*}^{n-1})/\Delta T$; $i^*=i-p,\ j^*=j-q,\ p=c_x\Delta T/\Delta x,\ q=c_y\Delta T/\Delta y$; $\Delta T<\Delta t$. | — | H 코드 대조 대상 아님 | 문서는 시공간 보간으로 해석한 가상 출발점을 설명한다. 코드가 별도 출발점 배열을 사용하는 알고리즘은 아니다. |
| R1:TN-099 | 문서 식 (3.38) | swantech PDF 105쪽 / 인쇄 97쪽, 번호 없음: $\lvert\partial_\theta c_\theta\rvert\Delta T<1$; (3.38): $Cr\equiv\lvert c_\theta\rvert\Delta T/\Delta\theta<1$. | — | H 코드 대조 대상 아님 | 정확도 조건의 유도이다. 실제 제한식은 (3.41)이다. |
| R1:TN-100 | 문서 식 (3.39) | swantech PDF 106쪽 / 인쇄 98쪽, (3.39): $\theta^n\approx\theta^{n-1}+c_\theta\Delta T$. | — | H 코드 대조 대상 아님 | 방향 궤적의 예시 적분식이다. 모델의 별도 파향 갱신식은 아니다. |
| R1:TN-101 | 방향 궤적의 보간 가중치 | swantech PDF 106쪽 / 인쇄 98쪽, 번호 없음: $\theta^n=\theta^{n-1}+\frac{\Delta T}{\Delta\theta}[(1-\theta^{n-1})c_\theta(0^\circ)+\theta^{n-1}c_\theta(\Delta\theta)]$; 다음 식은 이를 $\theta^{n-1}(1-\frac{\Delta T}{\Delta\theta}c_\theta(0^\circ))+\frac{\Delta T}{\Delta\theta}c_\theta(0^\circ)+\frac{\Delta T}{\Delta\theta}\theta^{n-1}c_\theta(\Delta\theta)$로 전개한다. | — | B 문서 오기 | 해석: $\theta$를 실제 각도로 정의한 앞 문장에서는 첫 가중치가 $1-\theta$가 아니라 $\Delta\theta-\theta$이어야 한다. 정규화 좌표 $\theta/\Delta\theta$를 재정의하지 않았다. 두 번째 식도 같은 오류를 전개한다. |
| R1:TN-102 | 일차원 공간 굴절 예시 | swantech PDF 106–107쪽 / 인쇄 98–99쪽, 번호 없음: $d\theta/dx=c_\theta/c_g$, 방향 변화 $c_\theta\Delta x/c_g$, $Cr=\lvert c_\theta\rvert\Delta x/(c_g\Delta\theta)$. | `src/swancom5.ftn:1714` `FAC2 = ALPHA * DDIR` | H 코드 대조 대상 아님 | 공간 진행 방향 거리와 군속도를 쓰는 1차원 예시이다. 일반 x축 투영에는 $c_x$를 써야 하므로 이 예시를 임의 방향 x미분의 구현식으로 옮기지 않는다. |
| R1:TN-104 | 방향 CFL 상한의 중간 유도 | swantech PDF 107쪽 / 인쇄 99쪽, 번호 없음: $\lvert c_\theta\rvert<\Delta\theta/\Delta T$; $1/\Delta T$ 추정에 $1/\Delta t+c_x/\Delta x+c_y/\Delta y$; $\lvert c_\theta\rvert\le\alpha_\theta\Delta\theta(1/\Delta t+\lvert c_x\rvert/\Delta x+\lvert c_y\rvert/\Delta y)$. | `src/swancom5.ftn:1721–1722` `FAC = FAC2 * ( ABS((RDX(1)+RDX(2))*CAX(ID,IS,1)) +`; `&                        ABS((RDY(1)+RDY(2))*CAY(ID,IS,1)) )` | H 코드 대조 대상 아님 | 문서는 이어서 시간 역수 항을 생략한 (3.41)을 채택한다. 앞 식은 중간 유도식이다. |
| R1:TN-106 | 방향 CFL의 기본 비활성 | swantech PDF 108–110쪽 / 인쇄 100–102쪽, 제한 설명: “In SWAN, the default value is $\alpha_\theta=0.9$”.<br>swanuse PDF 95쪽 / 인쇄 87쪽 및 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):471–485은 CTHETA 미지정 시 비활성과 활성화 시 `[cfl]=0.9`를 명시한다. | `src/swanmain.ftn:1331` `PNUMS(35) = 0.0`<br>`src/swancom5.ftn:1710` `IF ( INT(PNUMS(35)) == 1 ) THEN` | C 문서 누락 | 방향 CFL 제한의 기본 비활성은 swanuse에 명시되어 있다. C는 swantech §3.8이 계수 기본값과 활성화 조건을 구분하지 않는 점으로 한정한다. 정렬 격자는 제한 뒤에 DSPHER를 호출한다. 구면 추가 항까지 같은 상한으로 제한한다는 뜻은 아니다. [10-13 전수 검증 정정]
| R1:TN-107 | 역사적 수심 제한 유도 | swantech PDF 108–109쪽 / 인쇄 100–101쪽, 번호 없음: $d\theta/dn=(1/c)(dc/dn)\tan\theta$; $\theta\sim45^\circ$에서 $d\theta/dn=(1/c)(dc/dn)$; $c=\sqrt{gh}$; $d\theta/dn=(1/2h)(dh/dn)\approx(h_*-h_{ij})/(2h_{ij}\Delta n)$; $(d\theta/dn)\Delta n=(h_*-h_{ij})/(2h_{ij})$; $h_*-h_{ij}\le\pi h_{ij}$. | — | H 코드 대조 대상 아님 | 역사적 제한의 천해 유도이다. 현재 해법의 별도 Snel 경로 적분이 아니다. |
| R1:TN-108 | 역사적 이웃 수심 절단 | swantech PDF 109쪽 / 인쇄 101쪽: “depths in surrounding grid points are reduced to $\beta h_{i,j}$, if they are larger than this value.” | `src/swanpre1.ftn:1989` `IREFR = 1` | D 문서에만 있음 | 41.45 이후 조사한 공개 판에는 이웃 수심을 $\beta h$로 절단하는 계산이 없다. 41.45 소스의 주석은 해당 절차가 이미 제거됐다고 기록한다. 이 공개 판 범위에서 D를 확정한다. 제거된 절차를 현재 기능으로 옮기지 않는다. |
| R1:TN-112 | 방향 CFL 권고값 | swantech PDF 110쪽 / 인쇄 102쪽, 번호 없음: $\alpha_\theta=0.5$ 또는 $\alpha_\theta=9$ if $\Delta\theta=10^\circ$; $90^\circ$ 이내 회전 예시. | — | H 코드 대조 대상 아님 | 해상도·파장에 따른 권고 예시이다. 기본값이나 자동 분기값이 아니다. |
| R1:TC-002 | 쌍곡선 함수 인자의 상한과 건조 stencil 처리 | — | `src/swancom5.ftn:1577–1579` `IF ( KD1 .GT. 30.0 ) KD1 = 30.`; `VLSINH = SINH (2.* KD1 )`<br>`src/SwanPropvelS.ftn90:171` `if ( dloc(1) <= DEPMIN .or. dloc(2) <= DEPMIN .or. dloc(3) <= DEPMIN ) return` | C 문서 누락 | 큰 $kd$의 함수 평가를 제한한다. 비정렬 stencil에 건조점이 있으면 먼저 0으로 초기화한 스펙트럼 속도를 반환한다. |
| R1:TC-003 | 파수 기울기로 계산하는 비정렬 기본 굴절 | swanuse PDF 141쪽 / 인쇄 133쪽의 `DIRimpl [cdd] DEP\|WNUM`; `src/SwanGradDepthorK.ftn90:348–371`. | `src/SwanPropvelS.ftn90:259–269` `cd(1) = -cgo(is,1) / kwave(is,1)`; `cd(2) = cd(1) * dkdx(is)`; `cd(3) = cd(1) * dkdy(is)`; `cad(id,is) = esin(id)*cd(2) - ecos(id)*cd(3)` | C 문서 누락 | 고정 $\sigma$에서 $\nabla c=-\sigma\nabla k/k^2$를 쓰면 swantech 식 (3.43)과 연속식은 같다. 파수 기울기 선택 WNUM은 swanuse 명령 도식에도 있다. C는 swantech §3.8의 정렬 격자 설명에 비정렬 중심 쌍대 제어체적 기울기 경로가 없는 점이다. |
| R1:TC-004 | 스펙트럼 속도의 주파수별 감쇠와 주파수 CFL 제한 | swanuse PDF 95·141; 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):488–517. | `src/SwanPropvelS.ftn90:223,230,301,304` `fac2 = alpha * FRINTF * spcsig(is)`; `if ( abs(cas(id,is)) > fac ) cas(id,is) = cas(id,is) * fac / abs(cas(id,is))`; `fac = min(1.,(spcsig(is)/frlim)**pp)`; `cad(id,is) = fac*cad(id,is)` | C 문서 누락 | CSIGMA의 역할·기본 비활성·활성화 계수 0.9는 swanuse PDF 95에 있다. REFRLIM도 PDF 141 명령 도식에 있다. C는 swantech §3.8에 저주파 감쇠 `fac = min(1.,(spcsig(is)/frlim)**pp)`와 주파수 CFL 구현식·선택 조건을 함께 적지 않은 점이다. 세 제한 스위치는 기본 0이다. |
| R1:TC-005 | 구면 굴절 보정과 제한기의 적용 순서 | — | `src/SwanPropvelS.ftn90:286,294,312` `cad(id,is) = cad(id,is) - cd(2)*(cax(id,is,1)*ecos(id) + cay(id,is,1)*esin(id))`; `if ( int(PNUMS(29)) == 1 ) then`; `if ( int(PNUMS(35)) == 1 ) then` | C 문서 누락 | 비정렬 경로는 구면 보정 뒤 제한한다. 정렬 경로는 제한 뒤 구면 보정을 더한다. 최종 방향 속도에 같은 상한을 보장한다고 쓰지 않는다. |
| R1:TC-006 | 비정렬 기울기의 건조점 처리와 비활성 수심비 조건 | — | `src/SwanGradDepthorK.ftn90:208,233–234,360,385–386` `!if ( dpmax > drat * dpmin ) goto 10`; `10    dhdx = 0.`; `dhdy = 0.`; `!if ( dpmax > drat * dpmin ) goto 30`; `30    dkdx = 0.` | C 문서 누락 | 건조 셀을 만나는 경로는 기울기를 0으로 한다. `drat=5` 조건은 일반 주석이므로 switch.pl이 활성화하지 않는다. 이를 현행 수심 기울기 제한기로 적으면 안 된다. |
| R7:H-1227 | CDLIM 제거 | `website/modifications/modifications.htm:1227` `cdlim removed` | `src/swanpre1.ftn:1988–1992` `CALL INREAL ('CDLIM'  , PNUMS(17), 'STA',-1.)`; `IF (PNUMS(17).LT.0.) IREFR = 1`; `IF (EQREAL(PNUMS(17),0.)) THEN`; `IREFR = 0`<br>`src/swancom5.ftn:1373–1377` `The depth refraction limitation procedure (i.e. IREFR=-1) has been removed` | C 제거 범위 설명 누락 | 웹의 `cdlim removed`는 기존 수심 굴절 제한 계산과 잔존 입력 인자를 구분하지 않는다. 현재 판독기는 CDLIM을 읽는다. `IF (EQREAL(PNUMS(17),0.)) THEN`에서는 굴절을 끈다. 코드 주석은 기존 `IREFR=-1` 제한 절차가 제거됐다고 적는다. 축약된 제거 문구만으로 완전 제거의 오기라고 판정하지 않는다. |
| R7:H-695 | 굴절 수심 근사·90도 제한 | `website/modifications/modifications.htm:695` `The approximation of the bathymetry in the refraction computations is improved. To give robust results (but not necessarily accurate results) in case of poor resolution in bathymetry, currents or the wave field itself, the user can activate a limiter to avoid waves turning over more than 90 degrees in one spatial grid step.` | `src/swancom5.ftn:1714` `FAC2 = ALPHA * DDIR`<br>`src/swancom5.ftn:1725` `CAD(ID,IS,1) = CAD(ID,IS,1) * FAC / ABS(CAD(ID,IS,1))`<br>`122b595:src/swancom5.ftn:1714` `FAC2 = ALPHA * DDIR`<br>`src/swancom5.ftn:1710` `IF ( INT(PNUMS(35)) == 1 ) THEN`<br>`src/swancom5.ftn:1721–1722` `FAC = FAC2 * ( ABS((RDX(1)+RDX(2))*CAX(ID,IS,1)) +`; `     &                        ABS((RDY(1)+RDY(2))*CAY(ID,IS,1)) )` | D 현재 해당 구현 없음 | 현재 굴절 제한은 ALPHA·DDIR·공간 전파속도로 임계값을 계산한다. 고정된 90도 제한이라는 구판 설명은 현재 식에 없다. 41.45 비교 코드도 같은 제한식을 사용한다. 이 제한은 `IF ( INT(PNUMS(35)) == 1 ) THEN`에서만 적용한다. |
| R7:H-778 | 강한 굴절 kd 제한 | `website/modifications/modifications.htm:778` `For very strong refraction the value of cq is reduced in each grid point and for each wave component individually with the square of the fraction of the grid spacing over which kd<3.0.` | `src/swancom5.ftn:1671` `FAC = MIN(1.,(SPCSIG(IS)/FRLIM)**PP)`<br>`src/swancom5.ftn:1577` `IF ( KD1 .GT. 30.0 ) KD1 = 30.`<br>`122b595:src/swancom5.ftn:1671` `FAC = MIN(1.,(SPCSIG(IS)/FRLIM)**PP)`<br>`src/swancom5.ftn:1667` `IF ( INT(PNUMS(29)).EQ.1 ) THEN`<br>`src/swancom5.ftn:1668` `FRLIM = PI2*PNUMS(26)`<br>`src/swancom5.ftn:1669` `PP    =     PNUMS(27)`<br>`src/swancom5.ftn:1673` `CAD(ID,IS,1) = FAC*CAD(ID,IS,1)` | D 현재 해당 구현 없음 | 구판의 kd<3.0 구간 비율 제곱 제한은 현재 구현에 없다. 현재 REFRLIM은 주파수 비율의 거듭제곱으로 CAD를 줄인다. KD1의 30 상한은 이 구판 격자 비율식과 다른 코드이다. 41.45 비교 코드도 현재 식과 같다. 주파수 제한은 `IF ( INT(PNUMS(29)).EQ.1 ) THEN`에서만 적용한다. |
