---
title: "SWAN swantech Ch 3.9 QC approximation impl + 3.10 curvilinear governing + 3.11 force in curvilinear verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.9 Implementation of QC approximation + §3.10 Governing equations in curvilinear co-ordinates + §3.11 Computation of force in curvilinear co-ordinates, doc p.102-108 (Eq 3.44-3.69). References: Smit et al. 2015a·2015b, Smit-Janssen 2016, Akrish et al. 2020."
citation_status: verified
last_source_check: "2026-10-13 (recovery 대조 반영)"
verification_method: "swantech.pdf (v41.51) §3.9-3.11 직접 read via pdftotext (식 번호 context-verified: W eq 3.44·S_qc convolution 3.45·curvilinear coords 3.46-47·Taylor 3.50-51·partial deriv 3.52-54·propagation 3.55·D coeff 3.56·stability 3.57·action conservation 3.58·radiation stress 3.59-61·n 3.62·force 3.63-64·ξη transform 3.65-69) + website_markdown node55-57.md LaTeX alt-text. 식 번호는 PDF 번호 (PDF (3.44)–(3.45)는 HTML (3.86)–(3.87)에 대응한다. PDF (3.46)–(3.69)는 HTML (3.89)–(3.112)에 대응한다. Tukey 창·Δσ·Δc_g·Δu 보조식은 PDF 무번호다. [D]는 PDF (3.54)다). 2026-10-13 recovery 대조 보고서 R1–R8 반영" # [10-13 전수 검증 정정]
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 3.44-3.69 + Tukey γ=0.2 + Δq=2Δk verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch3-discretization.md
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
  - models/SWAN/source-analysis/swan-quasi-coherent.md
  - models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md
---

# swantech Ch 3.9 QC impl + 3.10-3.11 curvilinear — verified verbatim

> swantech.pdf (v41.51) §3.9-3.11 직접 read. **QC scattering 의 수치 구현** (Wigner W 의 σθ↔k 변환 + convolution) + **곡선좌표 governing/force** (Taylor 기반 편미분 + radiation stress force). §3.9 는 [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md) (SwanQCM.ftn90)과 보완.
>
> **식 번호 주의**: PDF 번호 사용 (online HTML +43 offset; QC 보조식·[D]·ΔΣ 등은 PDF 무번호).

## 1. §3.9 QC approximation 구현 (Eq 3.44-3.45)

§2.7의 phase-space 식은 $(\vec{x},\vec{k})$ 공간에서 정의된다. [QC 이론 노트](swan-tech-ch2-7-qcm-theory.md)와 연결된다. swantech PDF 110쪽 / 인쇄 102쪽은 (2.154)–(2.155)를 가리킨다. 웹 `website/online_doc/swantech/node55.html:48–50`은 (2.225)–(2.230)을 가리킨다. SWAN은 $(\sigma,\theta)$에서 Wigner 분포를 정의한 뒤 $\vec{k}$ 공간으로 변환한다. SWAN은 phase space에서 산란항을 계산한 뒤 결과를 $(\sigma,\theta)$로 역변환한다. Smit et al. (2015a)와 Akrish et al. (2020)의 접근은 $\vec{k}$ 공간에서 계산한다. 근거: swantech PDF 111쪽 / 인쇄 103쪽. [10-13 전수 검증 정정]

$$\frac{\partial W}{\partial t} + \nabla_{\vec{x}}\cdot[(\vec{c}_g + \vec{u})W] = J^{-1}S_{\text{qc}} \quad \text{(3.44)}$$
- $W(\vec{x},t;\sigma,\theta)$ = Wigner 분포, $J = |\vec{c}_g|/|\vec{k}|$ = Jacobian. $S_{\text{qc}}$ 평가 전 $W(\vec{x},t;\vec{k}) = J\,W(\vec{x},t;\sigma,\theta)$ 필요
- **W 는 action density 의 cross-correlation 확장**. 이론 분포의 비음수 적분 성질과 수치 반복 진단을 구분한다. 무파 상태의 0도 허용하는 PDF 68의 비음수 조건을 유지한다. 가중 없는 VARW 진단을 그 연속 적분의 직접 계산으로 쓰지 않는다. 근거: swantech PDF 68쪽 / 인쇄 60쪽; `src/swancom1.ftn:2155` `VARW = VARW + AC2(ID,IS,IP)`.

같은 $\sigma$의 $\vec{k}_1,\vec{k}_2$가 만드는 교차 성분은 $\sigma(|(\vec{k}_1+\vec{k}_2)/2|)\ne\sigma$에 기여할 수 있다. 이 차이는 파수 공간과 주파수 공간 사이의 매핑 오차를 만든다. 매뉴얼은 이 aliasing 오차가 수용할 만큼 작을 것으로 기대한다고 적는다. 매뉴얼은 Smit et al. (2015b)의 Appendix C를 참조한다. 굴절·Doppler 효과는 $S_{\text{qc}}$에 포함된다. 이 처리는 식의 stiffness와 추가 Jacobian 매핑 오차를 피하려는 선택이다. 근거: swantech PDF 111–112쪽 / 인쇄 103–104쪽; R3:QC-074. [10-13 전수 검증 정정]

매뉴얼은 QC 쇄파를 미포함으로 설명한다. 코드에는 GEN4·쇄파 활성·젖은 계산점·sweep 선택 조건을 통과하고 두 번째 반복 이후에 실행하는 QC 쇄파 경로가 있다. 이 경로를 triad 구현의 근거로 쓰지 않는다. 근거: `src/SwanQCM.ftn90:1310` `if ( IGEN /= 4 ) goto 10`; `src/SwanQCM.ftn90:1337` `if ( ISURF > 0 ) then`; `src/SwanQCM.ftn90:1361` `if ( iter > 1 ) then`; `src/SwanQCM.ftn90:1363` `call SWQCSURF ( memqcb, ac2, dep2, cfd, wfd, wsavd, kwave, cgo, spcdir, spcsig )`.

좌변은 §3.2-3.3 (구조격자) / §8.3 (비구조) 통상 이산화. **shoaling 해소 위해 최소 2차 정확도 권장 → SORDUP/Stelling-Leendertse** ($W$ 가 전파 중 급속 narrow/broaden).

### 1.1 3 grid + convolution (Eq 3.45)

3 이산 grid: $\vec{k}$ (간섭 해소, user $(\sigma,\theta)$ domain 변환), $\vec{x}'$ (coherent region), $\vec{q}$ (medium wavenumber).
- 자동 격자 간격은 에너지 가중 파수 분포의 표준편차로 계산한다. 유효 입사 경계 스펙트럼 중 최소 표준편차를 택한다. 이를 RFAC로 나눈 값은 파수 격자 간격이다. 전체 파수 범위와 구분한다. 근거: `src/SwanQCM.ftn90:283` `ebk(is) = 0.5 * DDIR * cg(is) * SPCSIG(is) * ebk(is)`; `src/SwanQCM.ftn90:302` `sd = sqrt( 0.5 * sd / m0 )`; `src/SwanQCM.ftn90:304` `sdev = min ( sdev, sd )`; `src/SwanQCM.ftn90:521` `dkx  = sdev / rfac`. [10-13 전수 검증 정정]
- FFT는 주기 끝점의 중복을 제외한 $N^2$ 점을 저장한다. q범위는 최소 크기와 짝수 점 수 규칙으로 바뀐다. $\Delta q=2\Delta k$의 정확한 이동 대응은 등방 파수 격자에서 성립한다. 비등방 수동 격자는 CP-015의 결함 후보에 해당한다. 근거: `src/SwanQCM.ftn90:578` `dxps = clen / real(ncoz) / 2.`; `src/SwanQCM.ftn90:580` `if ( .not.allocated(xpsc) ) allocate( xpsc(ncoz) )`; `src/SwanQCM.ftn90:584` `xpsc(1) = -clen / 4.`. `src/SwanQCM.ftn90:577` `ncoz = 2*floor(ceiling(qmax)/2.)`.
- $q_{\max} = \pi/\Delta x'$, user 또는 $q_{\max} = \alpha|\vec{k}_p|$ ($\alpha$=0.5/1/2)
- 등방 파수 격자에서는 문서의 간격 관계를 유지한다. 코드의 `qmax`는 572행에서 이미 파수 간격으로 나눈 값이다. `if ( qmax < 2. ) then`에서 `qmax = 2.`를 적용한 뒤 `ncoz = 2*floor(ceiling(qmax)/2.)`로 짝수 점 수를 정한다. 근거: `src/SwanQCM.ftn90:573` `if ( qmax < 2. ) then`; `src/SwanQCM.ftn90:575` `qmax = 2.`; `src/SwanQCM.ftn90:577` `ncoz = 2*floor(ceiling(qmax)/2.)`; `src/SwanQCM.ftn90:578` `dxps = clen / real(ncoz) / 2.`.

$$S_{qc}(x,y,k_x,k_y)=-i\sum_{q_x=-q_{max}}^{q_{max}}\sum_{q_y=-q_{max}}^{q_{max}}[\Delta\hat\sigma+\vec k\cdot\Delta\hat{\vec u}-\tfrac i2(\Delta\hat c_g\frac{\vec k}{\vert\vec k\vert}+\Delta\hat{\vec u})\cdot\nabla_{\vec x}]W(x,y,k_x-q_x/2,k_y-q_y/2)+\mathrm{c.c.} \quad \text{(3.45)}$$

근거: swantech PDF 113쪽 / 인쇄 105쪽 (3.45); `src/SwanQCM.ftn90:2231` `cax = cg * kxl / k + real(u)`; `src/SwanQCM.ftn90:2232` `cay = cg * kyl / k + real(v)`.
- $\Delta\hat{\sigma}, \Delta\hat{c_g}, \Delta\hat{\vec{u}}$ = DFT (window $\mathcal{W}$ taper 후 차분, PDF 무번호)
- **Tukey window** $\mathcal{W}(z)$ (PDF 무번호): $\ell = L_c/2$, taper $\gamma$ **hardcoded $\gamma=0.2$**
- 구조 격자는 `PROPSL=2`에서 중심차분을 사용한다. `PROPSL=1`에서는 상류차분을 사용한다. `PROPSL=3`에서 기울기 대입이 없는 문제는 CP-013의 결함 후보로 적는다. 비구조 경로는 중심쌍대 Green–Gauss 계산이다. 근거: `src/SwanQCM.ftn90:1608` `if (PROPSL == 2 ) then`; 1615의 중심차분; `src/SwanQCM.ftn90:1630` `elseif (PROPSL == 1 ) then`; 1637의 상류차분. `src/SwanQCM.ftn90:2030–2031`.

## 2. §3.10 Curvilinear governing (Eq 3.46-3.58)

곡선격자 좌표 $x_{i,j}$ **(3.46)**, $y_{i,j}$ **(3.47)** ($i=1..M, j=1..N$). Four-sweep 불변 (first sweep: $(i-1,j),(i,j-1)$ → $(i,j)$), 2D Taylor 전개로 근사.

이웃 격자 차 (3.48-3.49):
$$\Delta x_1 = x_{i,j}-x_{i-1,j},\ \Delta y_1 = y_{i,j}-y_{i-1,j},\ \Delta F_1 = F_{i,j}-F_{i-1,j} \quad \text{(3.48)}$$
$$\Delta x_2 = x_{i,j}-x_{i,j-1},\ \Delta y_2 = y_{i,j}-y_{i,j-1},\ \Delta F_2 = F_{i,j}-F_{i,j-1} \quad \text{(3.49)}$$

2D Taylor 전개의 선형 근사다. 고차 Taylor 항을 생략한 선형 근사 유도이다. 임의 함수의 정확한 등식으로 해석하지 않는다.

swantech PDF 114쪽 / 인쇄 106쪽, (3.50): $\Delta F_1=F_x\Delta x_1+F_y\Delta y_1$; (3.51): $\Delta F_2=F_x\Delta x_2+F_y\Delta y_2$.
$$\frac{\partial F}{\partial x} \approx \frac{\Delta y_2\Delta F_1 - \Delta y_1\Delta F_2}{[D]} \quad \text{(3.52)},\qquad \frac{\partial F}{\partial y} \approx \frac{\Delta x_1\Delta F_2 - \Delta x_2\Delta F_1}{[D]} \quad \text{(3.53)}$$
$$[D] = \Delta y_2\Delta x_1 - \Delta y_1\Delta x_2 \quad \text{(3.54)}$$

완전 propagation 항 (시간미분 포함, σθ 임시 무시):
$$[\Delta t^{-1}+(D_{x1}+D_{x2})c_{x,P}^++(D_{y1}+D_{y2})c_{y,P}^+]N_P^+-N_P^-/\Delta t-D_{x1}(c_xN)_2^+-D_{y1}(c_yN)_2^+-D_{x2}(c_xN)_3^+-D_{y2}(c_yN)_3^+=S_P^+ \quad \text{(3.55)}$$

$P=(i,j),2=(i-1,j),3=(i,j-1)$다. 근거: swantech PDF 115쪽 / 인쇄 107쪽 (3.55).
$$D_{x,1} = \frac{\Delta y_2}{[D]},\ D_{y,1} = -\frac{\Delta x_2}{[D]},\ D_{x,2} = -\frac{\Delta y_1}{[D]},\ D_{y,2} = \frac{\Delta x_1}{[D]} \quad \text{(3.56)}$$
> $+$ = 신 time level $t$, $-$ = 구 $t-\Delta t$. Stationary: $1/\Delta t \to 0$.

**Sweep 판정 안정조건** (전파방향이 $(i-1,j),(i,j-1)$ 연결선 사이):
$$D_{x,1}c_x + D_{y,1}c_y \ge 0 \quad\text{and}\quad D_{x,2}c_x + D_{y,2}c_y \ge 0 \quad \text{(3.57)}$$
> 이 기준으로 SWAN 이 spectral direction 의 sweep 소속 판정. 2nd sweep: $\Delta x_1 = x_{i,j}-x_{i,j-1}$, $\Delta x_2 = x_{i,j}-x_{i+1,j}$ 등 (3·4 sweep 유사, 식 불변).

**Action 보존** (삼각형 $(i,j),(i-1,j),(i,j-1)$, stationary·source=0 시 3 flux 균형):
$$(c_xN)_P(\Delta y_2-\Delta y_1)-(c_xN)_2\Delta y_2+(c_xN)_3\Delta y_1+(c_yN)_P(\Delta x_1-\Delta x_2)+(c_yN)_2\Delta x_2-(c_yN)_3\Delta x_1=0 \quad \text{(3.58)}$$

해석: 정상·무원천 (3.55)에 $[D]$를 곱하면 (3.58)이 된다. 국소 삼각형의 플럭스 평형이다. 이를 전체 비정렬 격자의 임의 제어체적 보존 증명으로 확대하지 않는다. 근거: `src/swancom5.ftn:2189–2190`의 정상 BSBT 조립.

## 3. §3.11 Force in curvilinear (Eq 3.59-3.69)

FORCE = wave-driven stress (N/m², radiation stress 미분). Radiation stress tensor:
$$S_{xx} = \rho g\int\left[n\cos^2\theta + n - \tfrac{1}{2}\right]E\,d\sigma d\theta \quad \text{(3.59)}$$
$$S_{xy} = S_{yx} = \rho g\int n\sin\theta\cos\theta\,E\,d\sigma d\theta \quad \text{(3.60)}$$
$$S_{yy} = \rho g\int\left[n\sin^2\theta + n - \tfrac{1}{2}\right]E\,d\sigma d\theta \quad \text{(3.61)}$$
$$n = \frac{c_g k}{\omega} \quad \text{(3.62)}$$
> 식 (3.62)의 원문은 $n=c_gk/\omega$이며 바로 앞 문장은 군속도/위상속도의 비로 정의한다. 이 국소 정의에서 주파수 기호를 고유주파수 $\sigma$로 읽으면 코드의 비와 같다. 제2장의 절대주파수 $\omega$와 혼동하지 않도록 표기를 구분한다. 이 기호 혼용만으로 다른 물리 동작을 단정하지 않는다. 근거: `src/swanser.ftn:715,718–719`: `K(IS) = SIG(IS)/C`; `N(IS) = 0.5*(1.+FAC1)`; `CG(IS)= N(IS)*C`.<br>swanuse PDF 128 및 swantech PDF 153도 $n$을 군속도/위상속도의 비로 정의한다.

Force:
$$F_x = -\frac{\partial S_{xx}}{\partial x} - \frac{\partial S_{xy}}{\partial y} \quad \text{(3.63)},\qquad F_y = -\frac{\partial S_{yx}}{\partial x} - \frac{\partial S_{yy}}{\partial y} \quad \text{(3.64)}$$

연속식은 같다. 정렬 출력 경로는 응력을 먼저 차분하지 않고 $nN$의 곱 미분을 $n\,\partial N+(\partial_dn)(\partial d)N$으로 나눠 이산화한다. 유한 격자에서 두 계산이 정확히 같지는 않다. 근거: `src/swanout1.ftn:5696–5701`: `NAX = NE(IS) * ACWX + NED(IS) * DDX * ACWAV`; `NAY = NE(IS) * ACWY + NED(IS) * DDY * ACWAV`; `FXADD = - ( (SPCDIR(ID,4) + 1.) * NAX - 0.5 * ACWX +`; y 성분도 같은 음수 발산이다.

곡선좌표 $\xi,\eta$ → physical 변환 (tensor 성분 $f$):
swantech PDF 116쪽 / 인쇄 108쪽, (3.65): $f_\xi=f_xx_\xi+f_yy_\xi$; (3.66): $f_\eta=f_xx_\eta+f_yy_\eta$.
swantech PDF 116쪽 / 인쇄 108쪽, (3.67): $f_x=(f_\xi y_\eta-f_\eta y_\xi)/(x_\xi y_\eta-x_\eta y_\xi)=f_\xi\xi_x+f_\eta\eta_x$.

swantech PDF 116쪽 / 인쇄 108쪽, (3.68): $f_y=(f_\xi x_\eta-f_\eta x_\xi)/(y_\xi x_\eta-y_\eta x_\xi)=f_\xi\xi_y+f_\eta\eta_y$.
수치근사 (2차 중심): $\frac{\partial f}{\partial\xi} \approx \frac{f_{\xi+1,\eta}-f_{\xi-1,\eta}}{2}$, $\frac{\partial f}{\partial\eta} \approx \frac{f_{\xi,\eta+1}-f_{\xi,\eta-1}}{2}$ **(3.69)**
> $x,y$ 미분도 동일 사용. 경계선 one-sided 근사.

## 4. SWAN 옵션 매핑 (User cmd)

| Tech (PDF §) | User cmd | 비고 |
|---|---|---|
| 3.44-3.45 QC | `SCAT [...]` | Tukey γ=0.2 hardcoded, [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md) |
| §3.10 curvilinear | `CGRID CURVILINEAR` + `READGRID COORDINATES` | Taylor 기반 편미분 |
| 3.59-3.69 force | `FORCE` 출력 / `SETUP` 입력 | radiation stress F_x, F_y |

## 5. 한계

- 창 모양과 1/2 계수는 같다. 그러나 실제 창 길이는 $(N-1)\Delta x'$다. 문서의 $\ell=N\Delta x'$보다 한 간격 짧다. 근거: swantech PDF 114쪽 / 인쇄 106쪽; `src/SwanQCM.ftn90:3422` `f = w * real(n-1)`.
- (3.55)는 작용밀도 전파식이다. (3.58)은 정상·무원천 조건의 국소 삼각형 플럭스 평형이다. 근거: swantech PDF 115쪽 / 인쇄 107쪽.
- 좌표 변환의 연쇄 법칙 유도이다. 근거: swantech PDF 116쪽 / 인쇄 108쪽 (3.65)–(3.68).

## 6. 연결

- [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md) — SwanQCM.ftn90 (QC source-analysis, §2.7+§3.9)
- [swan-tech-ch3-discretization](swan-tech-ch3-discretization.md) — §3.2 직교격자 이산화 (곡선격자 일반화 전)
- [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) — four-sweep (곡선격자서 불변)
- [swan-tech-ch2-obstacles-diffraction-setup](swan-tech-ch2-obstacles-diffraction-setup.md) — set-up $S_{xx}$ (force 와 동일 radiation stress)
- [swan-tech-ch3-obstacles-spectral-ops](swan-tech-ch3-obstacles-spectral-ops.md) — §3.12-3.16 (다음)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-115 | QC 분산 관계 매핑 오차 | swantech PDF 111–112쪽 / 인쇄 103–104쪽, 번호 없음: $\sigma(\lvert\vec k_1\rvert)=\sigma(\lvert\vec k_2\rvert)=\sigma$, $\sigma(\lvert(\vec k_1+\vec k_2)/2\rvert)\ne\sigma$; 평면 근사로 추출 가능한 $\nabla_{\vec x}\omega\cdot\nabla_{\vec k}W$. | `src/SwanQCM.ftn90:1588`의 보간과 1593행의 Jacobian. | H 코드 대조 대상 아님 | 교차상관을 분산 관계로 옮길 때의 오차와 대안 설명이다. 이 별도 굴절항을 구현했다고 말하지 않는다. |
| R1:TN-116 | QC 파수 격자·coherent 길이 | swantech PDF 112–113쪽 / 인쇄 104–105쪽, 번호 없음: $D_{\vec k}=\{(k_x,k_y):k_{x,0}\le k_x\le k_{x,\max},k_{y,0}\le k_y\le k_{y,\max}\}$; $\Delta k=$ 입사 작용 스펙트럼의 표준편차; $L_c=2\pi/\Delta k$. | `src/SwanQCM.ftn90:521–526,561`: `dkx  = sdev / rfac`; `dky  = sdev / rfac`; `dkx  = kxlen / float(mkxc)`; `clen = PI2 / max(dkx,dky)`.<br>swanuse PDF 91쪽 / 인쇄 83쪽, SCAT GRID `[rfac]` 및 PDF 139–140 명령 도식. | C 문서 누락 | 기본 `rfac=1`과 같은 두 파수 간격에서는 문서의 coherent 길이와 같다. 파수 격자 배율과 기본값 1은 swanuse SCAT GRID 설명에 있다. C는 swantech §3.9에 입력 격자 수에 따른 간격 변경과 `clen = PI2 / max(dkx,dky)`의 큰 간격 선택이 없는 점으로 한정한다. |
| R1:TN-117 | QC FFT 격자·q 상한 | swantech PDF 113쪽 / 인쇄 105쪽, 번호 없음: $D_{\vec x'}=[-L_c/4,L_c/4]^2$; $(M+1)^2$ 절점; $q_{\max}=\pi/\Delta x'=\alpha\lvert\vec k_p\rvert$; $\Delta q=2\Delta k$; $N=q_{\max}/\Delta k$; $M=L_c/(2\Delta x')=L_cq_{\max}/(2\pi)=N$. | `src/SwanQCM.ftn90:572,575,577–578,584`: `qmax = min (qmu, alfa * kmean) / max(dkx,dky)`; `qmax = 2.`; `ncoz = 2*floor(ceiling(qmax)/2.)`; `dxps = clen / real(ncoz) / 2.`; `xpsc(1) = -clen / 4.`.<br>`src/SwanQCM.ftn90:573–578`; swanuse PDF 91 및 PDF 140의 `TRUnc [alpha] [qmax]`. | C 문서 누락 | C는 swantech §3.9의 닫힌 구간 $(M+1)$점 설명과 FFT용 이산 격자의 차이다. 코드의 `qmax`는 격자 수 단위이다. `if ( qmax < 2. ) then`일 때 2로 올린다. 이후 짝수 `ncoz`를 정한다. 좌표는 끝 중복점 없이 `ncoz`개이며 마지막 점은 $L_c/4-\Delta x'$이다. 사용자 TRUNC의 상한 선택 자체는 swanuse에도 있다. |
| R1:TN-118 | 문서 식 (3.45) | swantech PDF 113쪽 / 인쇄 105쪽, (3.45): $S_{qc}=-i\sum_{q_x=-q_{\max}}^{q_{\max}}\sum_{q_y=-q_{\max}}^{q_{\max}}[\Delta\hat\sigma+\vec k\cdot\Delta\hat{\vec u}-\frac i2(\Delta\hat c_g\vec k/\lvert\vec k\rvert+\Delta\hat{\vec u})\cdot\nabla_{\vec x}]W(x,y,k_x-q_x/2,k_y-q_y/2)+{\rm c.c.}$ | `src/SwanQCM.ftn90:2234`: `ctb = ctb + 2. * ( sig + kxl*imag(u) + kyl*imag(v) ) * W(iky-jk,ikx-ik) - cax * dwdx(iky-jk,ikx-ik) - cay * dwdy(iky-jk,ikx-ik)`; 2253·2272·2291은 나머지 부호 구역이다. | F 표기 차이 | 해석: $-iz+{\rm c.c.}=2\Im z$이고 $(-i)(-i/2)z+{\rm c.c.}=-\Re z$이다. 따라서 밀도항의 2와 기울기항의 음수가 맞다. $\Delta q=2\Delta k$이므로 반파수 이동이 정수 index 이동이다. Marker의 끊어진 괄호를 쪽 이미지로 정정했다. |
| R1:TN-120 | Tukey 창의 끝점 | swantech PDF 114쪽 / 인쇄 106쪽, 번호 없음: $\mathcal W(z)=\frac12\{1+\cos[\pi(z/(\ell\gamma)-1)]\}$ if $0\le z<\ell\gamma$; $1$ if $\ell\gamma\le z\le(1-\gamma)\ell$; $\frac12\{1+\cos[\pi((\ell-z)/(\ell\gamma)-1)]\}$ if $(1-\gamma)\ell<z\le\ell$; $\ell=L_c/2,\ \gamma=0.2$. | `src/SwanQCM.ftn90:3401,3422,3428,3432,3436,3456`: `real, parameter :: w = 0.2  ! taper`; `f = w * real(n-1)`; `yw = 1. + cos( pi * (real(iy - 1)/f - 1.) )`; `yw = 1. + cos( pi * (real(n - iy)/f - 1.) )`; `yw = 2.`; `a(ix,iy) = 0.25 * a(ix,iy) * xw * yw`. | C 문서 누락 | 창의 모양과 0.2는 같다. 구현은 `n-1`개 간격을 창 길이로 삼는다. TN-117의 FFT 좌표에서 이 길이는 $\ell-\Delta x'$이다. 문서의 $\ell$과 정확히 같지 않다. |
| R1:TN-121 | QC 공간 기울기 | swantech PDF 114쪽 / 인쇄 106쪽: “second order central differences on structured grids”; 비정렬 격자는 (8.35). | `src/SwanQCM.ftn90:1608,1615,1630,1637`: `if (PROPSL == 2 ) then`; `dwdx(iky,ikx) = 0.5*rdx(1) * ( W(iky,ikx,5) - W(iky,ikx,2) ) + 0.5*rdx(2) * ( W(iky,ikx,4) - W(iky,ikx,3) )`; `elseif (PROPSL == 1 ) then`; 편측 기울기.<br>`src/SwanQCM.ftn90:1613–1625,1635–1645`의 밀도 조건. | C 문서 누락 | C는 swantech §3.9의 정렬 격자 중심차분 설명에 국소 기법·영 밀도 조건이 없는 점이다. `if (PROPSL == 2 ) then`은 중심차분이고 `elseif (PROPSL == 1 ) then`은 편측차분이다. 두 분기 모두 `if ( W(iky,ikx,1) /= 0. ) then`에서 기울기를 구한다. 반대 분기에서는 두 기울기를 0으로 둔다. |
| R1:TN-122 | QC 쇄파 호출의 존재 | swantech PDF 112쪽 / 인쇄 104쪽: QC 쇄파와 삼파 상호작용은 “not considered in the current QC framework”. | `src/SwanQCM.ftn90:1209`: `!   41.91, February 2022: extension QCM with surf breaking`; 1413: `call FILQCM ( imatra, idcmin, idcmax, isstop, memqcm, memqcb, plqcs, plwbrk, redc0, dissc0 )`.<br>`src/swancom1.ftn:3589–3591`, `src/SwanQCM.ftn90:1337–1363,3304–3316`의 실제 호출·반영. swanuse PDF 90쪽 / 인쇄 82쪽의 QC 설명. | B 문서 오기 | swantech §3.9와 swanuse의 QC 설명은 QC에 일관된 쇄파 처리를 향후 확장으로 적는다. 현행 코드는 QCSOURCE에서 `if ( ISURF > 0 ) then` 안의 지정 sweep 조건과 `if ( iter > 1 ) then`을 만족하면 SWQCSURF를 호출한다. FILQCM은 `if ( ISURF > 0 .and. IGEN == 4 ) then`에서 `memqcb`를 행렬 우변에 더한다. B는 이 조건부 구현과 문서의 미구현 설명의 차이이다. |
| R1:TN-123 | QC 차수 권고 | swantech PDF 112쪽 / 인쇄 104쪽: “recommended to apply at least second order accuracy”; 비정렬 고차 해법 개발 설명. | `src/SwanTranspX.ftn90:128–136`의 1차 삼각형 수송. | H 코드 대조 대상 아님 | QC 정확도 권고와 향후 개발 설명이다. 현재 고차 비정렬 해법의 구현 선언이 아니다. |
| R1:TN-127 | 문서 식 (3.50)·(3.51) | swantech PDF 114쪽 / 인쇄 106쪽, (3.50): $\Delta F_1=F_x\Delta x_1+F_y\Delta y_1$; (3.51): $\Delta F_2=F_x\Delta x_2+F_y\Delta y_2$. | `src/swancom5.ftn:189–192`의 역변환 계수. | H 코드 대조 대상 아님 | 고차 Taylor 항을 생략한 선형 근사 유도이다. 임의 함수의 정확한 등식으로 해석하지 않는다. |
| R1:TN-134 | 문서 식 (3.58) | swantech PDF 115쪽 / 인쇄 107쪽, (3.58): $(c_xN)_P(\Delta y_2-\Delta y_1)-(c_xN)_2\Delta y_2+(c_xN)_3\Delta y_1+(c_yN)_P(\Delta x_1-\Delta x_2)+(c_yN)_2\Delta x_2-(c_yN)_3\Delta x_1=0$. | `src/swancom5.ftn:2189–2190`의 정상 BSBT 조립. | F 표기 차이 | 해석: 정상·무원천 (3.55)에 $[D]$를 곱하면 (3.58)이 된다. 국소 삼각형의 플럭스 평형이다. 이를 전체 비정렬 격자의 임의 제어체적 보존 증명으로 확대하지 않는다. |
| R1:TN-138 | 문서 식 (3.62) | swantech PDF 116쪽 / 인쇄 108쪽, (3.62): $n=c_gk/\omega$. 쪽 이미지 확인. | `src/swanser.ftn:715,718–719`: `K(IS) = SIG(IS)/C`; `N(IS) = 0.5*(1.+FAC1)`; `CG(IS)= N(IS)*C`.<br>swanuse PDF 128 및 swantech PDF 153도 $n$을 군속도/위상속도의 비로 정의한다. | F 표기 차이 | 식 (3.62)의 원문은 $n=c_gk/\omega$이며 바로 앞 문장은 군속도/위상속도의 비로 정의한다. 이 국소 정의에서 주파수 기호를 고유주파수 $\sigma$로 읽으면 코드의 비와 같다. 제2장의 절대주파수 $\omega$와 혼동하지 않도록 표기를 구분한다. 이 기호 혼용만으로 다른 물리 동작을 단정하지 않는다. |
| R1:TN-139 | 문서 식 (3.63)·(3.64) | swantech PDF 116쪽 / 인쇄 108쪽, (3.63): $F_x=-\partial_xS_{xx}-\partial_yS_{xy}$; (3.64): $F_y=-\partial_xS_{yx}-\partial_yS_{yy}$. | `src/swanout1.ftn:5696–5701`: `NAX = NE(IS) * ACWX + NED(IS) * DDX * ACWAV`; `NAY = NE(IS) * ACWY + NED(IS) * DDY * ACWAV`; `FXADD = - ( (SPCDIR(ID,4) + 1.) * NAX - 0.5 * ACWX +`; y 성분도 같은 음수 발산이다. | C 문서 누락 | 연속식은 같다. 정렬 출력 경로는 응력을 먼저 차분하지 않고 $nN$의 곱 미분을 $n\,\partial N+(\partial_dn)(\partial d)N$으로 나눠 이산화한다. 유한 격자에서 두 계산이 정확히 같지는 않다. |
| R1:TN-140 | 문서 식 (3.65)·(3.66) | swantech PDF 116쪽 / 인쇄 108쪽, (3.65): $f_\xi=f_xx_\xi+f_yy_\xi$; (3.66): $f_\eta=f_xx_\eta+f_yy_\eta$. | `src/swanout1.ftn:5611–5615`의 역 Jacobian. | H 코드 대조 대상 아님 | 좌표 변환의 연쇄 법칙 유도이다. |
| R3:NT-032 | QC 쇄파의 문서 누락 반복 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch3-qc-curvilinear.md:33` `Depth-breaking(Smit 2015b)·triad(Smit-Janssen 2016) QC 는 미포함 (진행 중)`. | `src/SwanQCM.ftn90:1310` `if ( IGEN /= 4 ) goto 10`; `src/SwanQCM.ftn90:1337` `if ( ISURF > 0 ) then`; `src/SwanQCM.ftn90:1361` `if ( iter > 1 ) then`; `src/SwanQCM.ftn90:1363` `call SWQCSURF ( memqcb, ac2, dep2, cfd, wfd, wsavd, kwave, cgo, spcdir, spcsig )`. | C 문서 누락 | 매뉴얼은 QC 쇄파를 미포함으로 설명한다. 코드에는 GEN4·쇄파 활성·젖은 계산점·sweep 선택 조건을 통과하고 두 번째 반복 이후에 실행하는 QC 쇄파 경로가 있다. 이 경로를 triad 구현의 근거로 쓰지 않는다. |
| R3:NT-033 | 자동 격자 폭의 가중량 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch3-qc-curvilinear.md:40` `incident $N(\vec{k})$ 표준편차`. | `src/SwanQCM.ftn90:283` `ebk(is) = 0.5 * DDIR * cg(is) * SPCSIG(is) * ebk(is)`; `src/SwanQCM.ftn90:302` `sd = sqrt( 0.5 * sd / m0 )`; `src/SwanQCM.ftn90:304` `sdev = min ( sdev, sd )`; `src/SwanQCM.ftn90:521` `dkx  = sdev / rfac`. | B 문서 오기 | 자동 격자 간격은 에너지 가중 파수 분포의 표준편차로 계산한다. 유효 입사 경계 스펙트럼 중 최소 표준편차를 택한다. 이를 RFAC로 나눈 값은 파수 격자 간격이다. 전체 파수 범위와 구분한다. [10-13 전수 검증 정정]
| R3:NT-034 | FFT 점 수와 등방 이동 조건 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch3-qc-curvilinear.md:41` `$(M+1)^2$ 점`; 43 `$M = N$ (1:1 매핑, 무보간)`. | `src/SwanQCM.ftn90:573` `if ( qmax < 2. ) then`; `src/SwanQCM.ftn90:575` `qmax = 2.`; `src/SwanQCM.ftn90:577` `ncoz = 2*floor(ceiling(qmax)/2.)`; `src/SwanQCM.ftn90:578` `dxps = clen / real(ncoz) / 2.`. | C 문서 누락 | FFT는 주기 끝점의 중복을 제외한 $N^2$ 점을 저장한다. q범위는 최소 크기와 짝수 점 수 규칙으로 바뀐다. $\Delta q=2\Delta k$의 정확한 이동 대응은 등방 파수 격자에서 성립한다. 비등방 수동 격자는 CP-015의 결함 후보에 해당한다. |
| R3:NT-035 | QC 기울기의 전파법 조건 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch3-qc-curvilinear.md:48` `구조격자 2차 중심차분 / 비구조 Green-Gauss`. | `src/SwanQCM.ftn90:1608` `if (PROPSL == 2 ) then`; 1615의 중심차분; `src/SwanQCM.ftn90:1630` `elseif (PROPSL == 1 ) then`; 1637의 상류차분. | C 문서 누락 | 구조 격자는 `PROPSL=2`에서 중심차분을 사용한다. `PROPSL=1`에서는 상류차분을 사용한다. `PROPSL=3`에서 기울기 대입이 없는 문제는 CP-013의 결함 후보로 적는다. 비구조 경로는 중심쌍대 Green–Gauss 계산이다. |
| R3:NT-036 | 이론 비음수성과 반복 진단 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch3-qc-curvilinear.md:31` `$\iint W\,d\sigma d\theta > 0$`; `manual-notes/swan-tech-ch2-7-qcm-theory.md:46` `$\int W(\vec{x},\vec{k})\,d\vec{k} \ge 0$`. | `src/swancom1.ftn:2155` `VARW = VARW + AC2(ID,IS,IP)`; `src/swancom1.ftn:2158` `IF (VARW.LT.0.) NVARW = NVARW + 1`. | H 코드 대조 대상 아님 | 이론 분포의 비음수 적분 성질과 수치 반복 진단을 구분한다. 무파 상태의 0도 허용하는 PDF 68의 비음수 조건을 유지한다. 가중 없는 VARW 진단을 그 연속 적분의 직접 계산으로 쓰지 않는다. |
| R3:QC-073 | 음의 적분 분포 진단 | swantech PDF 111쪽 / 인쇄 103쪽, 번호 없음: $\iint W(\sigma,\theta)d\sigma d\theta>0$. | `src/swancom1.ftn:2155` `VARW = VARW + AC2(ID,IS,IP)`; `src/swancom1.ftn:2158` `IF (VARW.LT.0.) NVARW = NVARW + 1`. | H 이론 성질 | 원문은 적분 양수성을 “by definition”으로 진술한다(`website/online_doc/swantech/node55.html:136–145`). 이는 Wigner 분포의 이론 성질이며 별도 강제 알고리즘의 요구가 아니다. 코드의 `VARW = VARW + AC2(ID,IS,IP)`는 가중치 없는 음수 진단이다. 이 진단을 문서 적분의 정확한 검사로 설명하지 않는다. |
| R3:QC-074 | 파수 매핑 오차의 수용성 | swantech PDF 111쪽 / 인쇄 103쪽, 번호 없음: $\sigma(\vert\vec k_1\vert)=\sigma(\vert\vec k_2\vert)=\sigma$인데 $\sigma(\vert(\vec k_1+\vec k_2)/2\vert)\ne\sigma$. 원문: “we expect that such aliasing errors would prove to be small enough to be accepted”. | `src/SwanQCM.ftn90:1540` `sig = sqrt( k * GRAV * tanh(k*dp) )`; 1588의 쌍선형 보간. | H 코드 대조 대상 아님 | 교차 성분의 매핑 오차를 설명하는 예다. 동일 분산식을 사용한다는 사실로 오차가 작다는 기대까지 검증할 수 없다. |
| R3:QC-075 | QC 쇄파의 존재와 판 | swantech PDF 112쪽 / 인쇄 104쪽, 원문: QC 쇄파와 triad는 “not considered in the current QC framework”; “These developments are in progress.” | `src/SwanQCM.ftn90:1310` `if ( IGEN /= 4 ) goto 10`; `src/SwanQCM.ftn90:1337` `if ( ISURF > 0 ) then`; `src/SwanQCM.ftn90:1361` `if ( iter > 1 ) then`; `src/SwanQCM.ftn90:1363` `call SWQCSURF ( memqcb, ac2, dep2, cfd, wfd, wsavd, kwave, cgo, spcdir, spcsig )`. | C 문서 누락 | `GEN4`, 쇄파 활성, 두 번째 반복 이후에 QC 쇄파 경로가 있다. SWQCSURF 호출은 `src/SwanQCM.ftn90:1349–1352`의 sweep 선택 조건 안에 있다. 호출자의 `src/swancom1.ftn:3289–3296`은 마른 계산점에서 반환한다. 공개 41.51 커밋 `7ee8981`에도 같은 호출이 있다. `git log -S 'subroutine SWQCSURF'`는 `b2ae30e` 초기 반입까지 거슬러 간다. 따라서 다른 공개 판의 추가로 단정하지 않는다. 문서가 이 쇄파 경로를 반영하지 않았다. QC triad 경로는 이 호출에 없다. swanuse PDF 90도 QC 쇄파·triad의 포함을 향후 개발로 설명한다. C는 swantech 3.9와 swanuse SCAT 절이 `GEN4`의 조건부 QC 쇄파 경로를 반영하지 않은 차이다. |
| R3:QC-076 | 전파법 정확도 권고 | swantech PDF 112쪽 / 인쇄 104쪽, 원문: “at least second order accuracy”; 정상에서는 SORDUP, 비정상에서는 Stelling–Leendertse 권고. | `src/swancom1.ftn:5396` `IF (PROPSL.EQ.3) THEN`; `src/swancom1.ftn:5401` `ELSE IF (PROPSL.EQ.2) THEN`. | H 코드 대조 대상 아님 | `src/swanmain.ftn:1179`의 `PROPSS = 2`와 1180행의 `PROPSN = 3`은 기본 전파법을 정한다. 그러나 문장의 정확도 권고는 모든 국소 스텐실의 차수를 보증하지 않는다. 문서의 권고만으로 모든 QC 계산이 2차라고 쓰면 안 된다. `PROPSL=3`의 QC 기울기 문제는 CP-013에 따로 판정한다. [10-13 전수 검증 정정]
| R3:QC-078 | 자동 격자 폭의 에너지 가중 | swantech PDF 112–113쪽 / 인쇄 104–105쪽, 번호 없음: $\Delta k$를 “standard deviation ... of the action density $N(\vec k)$”로 정한다. | `src/SwanQCM.ftn90:283` `ebk(is) = 0.5 * DDIR * cg(is) * SPCSIG(is) * ebk(is)`; `src/SwanQCM.ftn90:302` `sd = sqrt( 0.5 * sd / m0 )`; `src/SwanQCM.ftn90:304` `sdev = min ( sdev, sd )`; `src/SwanQCM.ftn90:521` `dkx  = sdev / rfac`. | B 문서 오기 | `SPCSIG`를 곱하므로 실제 가중량은 작용밀도가 아니라 에너지밀도다. `m0`도 수면 분산이다. 경계점 중 가장 작은 표준편차를 택한다. `RFAC` 생략값 1에서만 그 표준편차가 격자 폭과 같다. `src/SwanQCM.ftn90:275`도 `compute the incoming energy density in wave number space, integrated over all directions`라고 적는다. swanuse PDF 90–91과 `website/online_doc/swanuse/node28.html:3388–3403`은 `RFAC`에 의한 간격 조절을 설명한다. B는 swantech의 작용밀도 가중이라는 명시에 한정한다. [10-13 전수 검증 정정]
| R3:QC-079 | 공간 FFT의 끝점과 점 수 | swantech PDF 113쪽 / 인쇄 105쪽, 번호 없음: $D_{\vec x'}=\{(x',y')\mid-L_c/4\le x'\le L_c/4,\ -L_c/4\le y'\le L_c/4\}$; $(M+1)\times(M+1)$ 점; $\Delta x'=\Delta y'$. | `src/SwanQCM.ftn90:578` `dxps = clen / real(ncoz) / 2.`; `src/SwanQCM.ftn90:580` `if ( .not.allocated(xpsc) ) allocate( xpsc(ncoz) )`; `src/SwanQCM.ftn90:584` `xpsc(1) = -clen / 4.`. | C 문서 누락 | 양의 끝점은 중복 저장하지 않는다. 실제 점 수는 $N^2$이고 마지막 좌표는 $L_c/4-\Delta x'$다. 문서가 FFT의 주기 끝점 제외를 적지 않았다. `src/SwanQCM.ftn90:585–586`은 저장 좌표를 `ncoz`개까지만 증가시킨다. C는 swantech 3.9의 끝점 포함 점 수와 FFT 저장점 수의 연결 설명에 한정한다. |
| R3:QC-080 | Nyquist 끝점과 합 영역 | swantech PDF 113쪽 / 인쇄 105쪽, 번호 없음: $D_{\vec q}=\{(q_x,q_y)\mid-q_{max}\le q_x\le q_{max},\ -q_{max}\le q_y\le q_{max}\}$; Nyquist 파장 $2\Delta x'$; $q_{max}=\pi/\Delta x'$. | `src/SwanQCM.ftn90:578` `dxps = clen / real(ncoz) / 2.`; 590 출력에 `-PI/dxps, PI/dxps`를 사용한다. | C 문서 누락 | Nyquist 한계는 같다. 그러나 FFT는 양·음 Nyquist 끝점을 별도 독립 빈으로 모두 저장하지 않는다. 산란 합은 `ish-1`까지만 사용한다. 닫힌 구간의 연속 범위와 실제 합의 끝점은 다르다. `src/SwanQCM.ftn90:2175`의 `ish = ncoz/2`와 2222–2242행의 `ish-1` 상한을 대조했다. C는 swantech 3.9가 실제 합의 Nyquist 빈 제외를 설명하지 않은 차이다. 연속 영역 표기만으로 양끝을 독립 빈으로 저장한다고 해석하지 않는다. |
| R3:QC-081 | q최댓값의 결합 제한 | swantech PDF 113쪽 / 인쇄 105쪽, 번호 없음: $q_{max}=\alpha\vert\vec k_p\vert$; “peak (or mean)”; $\alpha$는 보통 0.5, 1, 2. | `src/SwanQCM.ftn90:572` `qmax = min (qmu, alfa * kmean) / max(dkx,dky)`; `src/swanmain.ftn:1417` `PSCAT(1) = 1.`; `src/swanmain.ftn:1418` `PSCAT(2) = 99999.`; `src/swanpre1.ftn:3610` `CALL INREAL ('ALPHA', PSCAT(1), 'STA', 1.)`. | C 문서 누락 | swanuse PDF 91과 `website/online_doc/swanuse/node28.html:3473–3506`은 두 제한의 최솟값, 기본 `alpha=1`, 입력 `qmax`의 단위 `1/m`를 이미 설명한다. 이 부분은 일치한다. `src/SwanQCM.ftn90:294`는 `kmean = max ( kmean, km )`으로 경계점 평균 파수 중 최댓값을 선택한다. 572행의 내부 `qmax`는 `max(dkx,dky)`로 나눈 무차원 값이다. C는 swantech 3.9에 없는 경계점 집계와 내부 격자 변수의 정의로 좁힌다. |
| R3:QC-082 | 짝수 FFT 크기로의 정수화 | swantech PDF 113쪽 / 인쇄 105쪽, 번호 없음: $\Delta q=2\Delta k$, $N=q_{max}/\Delta k$, $M=\tfrac12L_c/\Delta x'=L_cq_{max}/2\pi=L_cN\Delta k/2\pi=N$. | `src/SwanQCM.ftn90:573` `if ( qmax < 2. ) then`; `src/SwanQCM.ftn90:575` `qmax = 2.`; `src/SwanQCM.ftn90:577` `ncoz = 2*floor(ceiling(qmax)/2.)`; `src/SwanQCM.ftn90:578` `dxps = clen / real(ncoz) / 2.`. | C 문서 누락 | 등방 파수 격자에서는 문서의 간격 관계를 유지한다. 코드의 `qmax`는 572행에서 이미 파수 간격으로 나눈 값이다. `if ( qmax < 2. ) then`에서 `qmax = 2.`를 적용한 뒤 `ncoz = 2*floor(ceiling(qmax)/2.)`로 짝수 점 수를 정한다. C는 swantech 3.9와 swanuse SCAT 절에 없는 이 하한·정수화 규칙으로 한정한다. |
| R3:QC-083 | 이산 산란식 (3.45) | swantech PDF 113쪽 / 인쇄 105쪽, (3.45): $S_{qc}(x,y,k_x,k_y)=-i\sum_{q_x=-q_{max}}^{q_{max}}\sum_{q_y=-q_{max}}^{q_{max}}[\Delta\hat\sigma+\vec k\cdot\Delta\hat{\vec u}-\tfrac i2(\Delta\hat c_g\frac{\vec k}{\vert\vec k\vert}+\Delta\hat{\vec u})\cdot\nabla_{\vec x}]W(x,y,k_x-q_x/2,k_y-q_y/2)+\mathrm{c.c.}$ | `src/SwanQCM.ftn90:2231` `cax = cg * kxl / k + real(u)`; `src/SwanQCM.ftn90:2232` `cay = cg * kyl / k + real(v)`; 2234의 `2. * ( sig + kxl*imag(u) + kyl*imag(v) ) * W(iky-jk,ikx-ik)`와 두 음의 기울기 항. | F 표기 차이 | PDF는 대괄호 전체 뒤에 $W$를 곱한다. Marker의 두 줄 분리는 이 구조를 잃었다. $\Delta\hat\sigma$의 허수부와 $\Delta\hat c_g$의 실수부를 저장하는 코드가 정확히 필요한 성분을 취한다. 복소켤레의 계수 변형은 QC-053과 같다. |
| R3:QC-087 | Tukey 창의 실제 길이 | swantech PDF 114쪽 / 인쇄 106쪽, 번호 없음: $\mathcal W(z)=\begin{cases}\frac12\{1+\cos[\pi(z/(\ell\gamma)-1)]\},&0\le z<\ell\gamma\\1,&\ell\gamma\le z\le(1-\gamma)\ell\\\frac12\{1+\cos[\pi((\ell-z)/(\ell\gamma)-1)]\},&(1-\gamma)\ell<z\le\ell\end{cases}$; $\ell=L_c/2$. | `src/SwanQCM.ftn90:3422` `f = w * real(n-1)`; `src/SwanQCM.ftn90:3428` `yw = 1. + cos( pi * (real(iy - 1)/f - 1.) )`; 3432는 반대 끝의 코사인이다. 3436 `yw = 2.`; `src/SwanQCM.ftn90:3456` `a(ix,iy) = 0.25 * a(ix,iy) * xw * yw`. | C 문서 누락 | 창 모양과 1/2 계수는 같다. 그러나 실제 창 길이는 $(N-1)\Delta x'$다. 문서의 $\ell=N\Delta x'$보다 한 간격 짧다. 마지막 저장점에서 창을 0으로 만들기 위한 이산 끝점 처리를 문서가 적지 않았다. `src/SwanQCM.ftn90:578,585–586`의 저장 간격과 `f = w * real(n-1)`을 함께 대조했다. C는 swantech 3.9가 창의 길이를 마지막 저장점까지의 거리로 바꾸는 규칙을 설명하지 않은 차이다. |
| R3:QC-089 | 구조 QC 기울기의 조건 | swantech PDF 114쪽 / 인쇄 106쪽, 번호 없음: $\nabla_{\vec x}W$는 구조 격자에서 “second order central differences”. | `src/SwanQCM.ftn90:1608` `if (PROPSL == 2 ) then`; 1615의 중심차분; `src/SwanQCM.ftn90:1630` `elseif (PROPSL == 1 ) then`; 1637의 상류차분. | C 문서 누락 | 중심차분은 `PROPSL=2`에 한정된다. `PROPSL=1`은 1차 상류차분이다. 중심 $W=0$이면 기울기를 0으로 만든다. 이 조건들을 문서가 적지 않았다. `src/SwanQCM.ftn90:1613–1645`의 영값 조건은 `PROPSL=1,2` 분기에 적용된다. C는 swantech 3.9의 중심차분 설명에 이 분기 조건이 없는 차이다. `PROPSL=3`의 미정의 기울기는 CP-013의 E 판정으로 구분한다. |
