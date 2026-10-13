---
title: "SWAN swantech Ch 4 Wave BC/IC + Ch 5 Implementation of 2D wave setup (Poisson finite-volume curvilinear) verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) Ch 4 Wave boundary and initial conditions (doc p.117-118) + Ch 5 Implementation of 2D wave setup §5.1-5.2 (doc p.119-126, Eq 5.1-5.25). References: Pierson-Moskowitz 1964, Hasselmann et al. 1973 (JONSWAP), Kahma-Calkoen 1992, Dingemans 1997, Wesseling 2001, Botta-Ellenbroek 1985."
citation_status: verified
last_source_check: "2026-10-13 (recovery 대조 반영)"
verification_method: "2026-10-13 HEAD 대비 추가·수정 121줄을 R3 최종 보고서, git 판정 D·E, 현재·과거 코드, 웹 HTML, swantech PDF 65–66·125–134쪽과 swanuse 관련 쪽에 대조했다. 식 (5.14)–(5.24)의 인쇄 표기는 PDF 130–131쪽 이미지로 확인했다." # [10-13 전수 검증 정정]
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 5.1-5.25 + 9-point stencil/NWKARR=9/MXC×MYC verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch3-qc-curvilinear.md
  - models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md
  - models/SWAN/manual-notes/swan-tech-ch6-iterative-solvers.md
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
---

# swantech Ch 4 BC/IC + Ch 5 2D wave setup — verified verbatim

> swantech.pdf (v41.51) Ch 4-5 직접 read. **파 경계/초기조건** (Ch 4, 무방정식) + **2D wave setup 의 Poisson 식 finite-volume 곡선격자 해법** (Ch 5, Eq 5.1-5.25). [swan-tech-ch2-obstacles-diffraction-setup](swan-tech-ch2-obstacles-diffraction-setup.md) §5 의 1D set-up (Eq 2.143-2.145)을 2D 수치로 확장. [10-13 전수 검증 정정]
>
> **식 번호 주의**: Ch 5/6은 chapter-local 번호 → **website = PDF 일치** (Ch 2/3 같은 offset 없음).

## A. Ch 4 — Wave boundary and initial conditions (무방정식)

### A.1 Wave BC (up-wave 경계)

2D spectrum 지정, 3 옵션:
- **1D parametric spectrum + directional distribution**: Pierson-Moskowitz(1964) / **JONSWAP**(Hasselmann 1973) / Gaussian
- **1D discrete spectrum + directional dist** (측정 기반)
- **2D discrete spectrum** (다른 SWAN run 또는 WAM/WAVEWATCH III)

### A.2 Frequency/directional 경계

- 기본 암시적 주파수 경계는 흡수 조건이다. 명시적 STRSSB의 최저 주파수 바깥 면은 유출도 0으로 둔다. GEN4는 `PWTAIL(1) = 1.E8`, `PWTAIL(2:10) = 0.`으로 진단 꼬리를 억제한다. 이 GEN4 대입을 모든 SCAT 실행에 일반화하지 않는다. 근거: `src/swancom5.ftn:3688` `FLEFT = 0.`; `src/swanmain.ftn:6385–6386` `PWTAIL(1) = 1.E8` / `PWTAIL(2:10) = 0.`.
- **방향 경계**: closed circular 시 불필요. 경제성 위해 pre-defined directional sector 옵션 (경계 fully absorbing, refraction 으로 action 제거 가능)

### A.3 Geographic 경계

- **land**: 무파 생성 + 입사 에너지 전부 흡수 (무문제)
- **water**: 관측 있으면 입력. 없으면 무파 입사 + 자유 유출 가정 (오차 → 관심영역서 멀리 배치 필수)

### A.4 Initial conditions

- 기본 초기화는 계산된 취송거리와 국소 바람을 사용한다. `WSLOC.GT.1.E-10`이 거짓이면 $H_s=0.02$ m, $T=2$ s를 사용한다. 정상 2세대 예측의 조건은 `IWIND.GE.3 .AND. NSTATC.EQ.0 .AND. ICOND.NE.4`다. 격자별 취송거리 식은 BC-014의 조건을 유지한다. 근거: `src/swanmain.ftn:9074` `HSDLSS = MIN (0.21, 0.00288*FDLSS**0.45)`; `src/swanmain.ftn:9077` `TPDLSS = MIN (1./0.13, 0.46*FDLSS**0.27)`; `src/swanmain.ftn:9079` `IF (SPPARM(1).LT.0.05) SPPARM(2) = 2.`; `src/swanmain.ftn:9086` `SPPARM(1) = 0.02`.

직교좌표의 구조 격자는 `TLEN = (XCLEN + YCLEN)/2.`와 `TDXY = FLOAT(MXCGL + MYCGL)/2.`의 비를 취송거리로 쓴다. 구면좌표에서는 `TLEN = LENDEG * (COSYG*XCLEN + YCLEN)/2.`로 바꾼다(`src/swanmain.ftn:9002–9011`). `nvertsg.NE.0`이면 분모는 전체 정점 수다. C는 swantech 4장과 swanuse PDF 64의 평균 공간 간격 설명에 이 대체 계산식이 없는 차이다. 근거: `src/swanmain.ftn:9003` `TLEN = (XCLEN + YCLEN)/2.`; `src/swanmain.ftn:9008` `TDXY = FLOAT(MXCGL + MYCGL)/2.`; `src/swanmain.ftn:9009` `IF ( nvertsg.NE.0 ) TDXY = FLOAT(nvertsg)`; `src/swanmain.ftn:9011` `FETCH = TLEN/TDXY`.
- 코드는 `IF ( IWIND.GE.3 .AND. NSTATC.EQ.0 .AND. ICOND.NE.4 ) THEN`일 때만 `PRECOR = .TRUE.`로 둔다. 근거: `src/swancom1.ftn:1453` `IF ( IWIND.GE.3 .AND. NSTATC.EQ.0 .AND. ICOND.NE.4 ) THEN`; `src/swancom1.ftn:1455` `PRECOR = .TRUE.`; `src/swancom1.ftn:1457` `PRECOR = .FALSE.`.
- 이전 stationary/nonstationary 계산 결과로 초기상태 가능

## B. Ch 5 — Implementation of 2D wave setup

### B.1 §5.1 지배식 (Eq 5.1-5.3)

Wave setup = 해안 근접 narrow zone, quasi-stationary. Wave-induced force ↔ setup gradient 평형:
swantech PDF 127쪽 / 인쇄 119쪽 (5.1)의 인쇄 원문이다.

$$gd\left(\frac{\partial\zeta}{\partial x} + \frac{\partial\zeta}{\partial y}\right) + F_x + F_y = 0 \quad \text{(5.1)}$$
($\zeta$=setup, $d$=수심, $F_i$=단위질량당 wave-induced force)

두 방향 성분을 스칼라로 더한 (5.1)에 다시 “divergence”를 취해 (5.2)를 얻을 수 없다. 벡터 평형이 필요하다. 근거: swantech PDF 127쪽 / 인쇄 119쪽.

원문 식을 인용한 뒤 부호 오류를 적는다. $F=-\nabla\cdot S/\rho$이면 평형은 $gd\nabla\zeta-F=0$다. Poisson 식은 $\nabla\cdot(gd\nabla\zeta-F)=0$다. 경계 조건은 $gd\zeta_n-F_n=0$다. 근거: `src/swancom1.ftn:10392` `-(RSXXI*DIX + RSXXJ*DJX + RSXYI*DIY + RSXYJ*DJY)`.
$$\frac{\partial}{\partial x}\left(gd\frac{\partial\zeta}{\partial x}\right) + \frac{\partial}{\partial y}\left(gd\frac{\partial\zeta}{\partial y}\right) + \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} = 0 \quad \text{(5.2)}$$

경계조건 (open boundary + shoreline(depth=0)):
$$F_n + gd\frac{\partial\zeta}{\partial n} = 0 \quad \text{(5.3)}$$
코드는 계산 격자 전체에서 선택한 최심점의 set-up을 `SUPCOR`에 맞춘다. 이 점을 외곽 경계점으로 제한하지 않는다. `SUPCOR` 기본값은 0이다. 근거: `src/swancom1.ftn:10215` `DO IY = 1, MYC`; `src/swancom1.ftn:10216` `DO IX = 1, MXC`; `src/swancom1.ftn:10223` `IF (DEPSAV(INDX).GT.DEPMAX) THEN`; `src/swancom1.ftn:10413` `S_UPCOR = S_UPDP - PSETUP(2)`. 웹 `online_doc/swanuse/node28.html:2986–2999`; `src/swanmain.ftn:1201` `PSETUP(2) = 0.0`.

중첩 set-up의 Dirichlet 조립 분기는 표준 입력으로 활성화할 수 없다. 부모 모델의 set-up을 중첩 경계에 적용하는 실행 기능으로 안내하지 않는다. 근거: `src/swancom1.ftn:11781` `IF ( LSETUP.EQ.2 ) THEN`; `src/swanpre1.ftn:2094` `LSETUP = 1`; `43e9bbb:src/swanmain.ftn:1197` `! PSETUP(1) is currently unused, but can be used as setup nesting flag`.
> 매 iteration 후 setup 재계산 → 수심에 더함 (wave field 에 setup 효과 반영). 출력량 `SETUP`.

### B.2 §5.2.1 Problem definition (Eq 5.4-5.6)

$$\frac{\partial}{\partial x_k}\left(F_k + gd\frac{\partial\zeta}{\partial x_k}\right) = 0 \quad \text{(5.4)}$$
- **Neumann** (beach 항상): $F_n + gd\frac{\partial\zeta}{\partial n} = 0$ at boundary **(5.5)** (setup 가산상수 자유도)
- **Dirichlet**: $\zeta$ = given at boundary **(5.6)**
- **boundary-fitted, vertex-centered finite volume method**. 이하 $k \equiv gd$.

### B.3 Discretization (Eq 5.7-5.22) — 곡선격자 finite volume

물리영역 → $(\xi^1,\xi^2)$ 직사각 computational domain (dry 점 포함). 변환 관계 (summation convention):
$$\frac{\partial\varphi}{\partial x^\beta} = \frac{1}{\sqrt{g}}\frac{\partial}{\partial\xi^\gamma}(\sqrt{g}\,a^{(\gamma)}_\beta\varphi) \quad \text{(5.7)}$$
- contravariant base vector $\vec{a}^{(\alpha)} = \nabla\xi^\alpha$ **(5.8)**, Jacobian $\sqrt{g} = a^1_{(1)}a^2_{(2)} - a^2_{(1)}a^1_{(2)}$ **(5.9)**, covariant $\vec{a}_{(\alpha)} = \partial\vec{x}/\partial\xi^\alpha$ **(5.10)**
- contravariant ← covariant: $\sqrt{g}\vec{a}^{(1)} = (a^2_{(2)}, -a^1_{(2)})^T$ **(5.11)**, $\sqrt{g}\vec{a}^{(2)} = (-a^2_{(1)}, a^1_{(1)})^T$ **(5.12)**

(5.7)은 지배식 (5.4)에 적용한다. 근거: swantech PDF 129쪽 / 인쇄 121쪽의 식 (5.13).
$$\frac{1}{\sqrt{g}}\frac{\partial}{\partial\xi^\alpha}(\sqrt{g}\,\vec{a}^{(\alpha)}\cdot(k\nabla\zeta + \vec{F})) = 0 \quad \text{(5.13)}$$
> $\nabla\zeta$ 는 Cartesian $\vec{x}$ 미분 (ξ 아님).

swantech PDF 130쪽 / 인쇄 122쪽 (5.14)의 셀 적분 원문이다.
swantech PDF 130쪽 / 인쇄 122쪽, (5.14): $\int_{\Omega_x}\frac1{\sqrt g}\partial_{\xi^\alpha}(\sqrt g\vec a^{(\alpha)}\cdot(k\nabla\zeta+\vec F))d\Omega_x$; 다음 줄 $\int_{\Omega_\xi}\partial_{\xi^\alpha}(\sqrt g\vec a^{(\alpha)}\cdot(k\nabla\zeta+\vec F))d\Omega_\xi$; $\approx\left.\sqrt g\vec a^{(1)}\cdot(k\nabla\zeta+F)\right\vert_{(-1,0)}^{(1,0)}+\left.\sqrt g\vec a^{(2)}\cdot(k\nabla\zeta+\vec F)\right\vert_{(0,-1)}^{(0,1)}$. [10-13 전수 검증 정정]

$d\Omega_x=\sqrt g\,d\Omega_\xi$다. 코드는 네 면의 유출입 차를 조립한다. 우변으로 옮겨서 부호가 바뀐다. PDF의 첫 두 적분 사이에는 등호가 인쇄되지 않았다. 해당 두 적분은 같은 변수 변환을 나타낸다. 근거: `src/swancom1.ftn:10825` `RHS(INDX) = RHS(INDX) - 0.5*JCTA(INDX,1,1,1)`; 10832는 왼쪽 면의 양수 항이다. 10839는 위쪽 면의 음수 항이다. 10846은 아래쪽 면의 양수 항이다.
- 4 cell integration point (1,0),(0,1),(-1,0),(0,-1). Covariant base 중심차분: $\vec{a}_{(2)}|_{(0,1)} = \vec{x}_{(0,2)}-\vec{x}_{(0,0)}$ **(5.15)**, $\vec{a}_{(1)}|_{(1,0)} = \vec{x}_{(2,0)}-\vec{x}_{(0,0)}$ **(5.16)** (computational step=1)

**$\nabla\zeta$ 특별처리** (Cartesian 미분이나 모든 미분이 ξ 방향) → **integration path method** (Wesseling 2001): $\xi^1,\xi^2$ 2 독립방향 적분:
swantech PDF 130쪽 / 인쇄 122쪽, (5.17): $(\vec x_{2,0}-\vec x_{),0})\nabla\zeta\big\vert_{(1,0)}=\zeta_{2,0}-\zeta_{0,0}$. 두 번째 좌표의 첨자가 PDF에서 `),0`로 깨져 있다. Marker는 이를 `j,0`로 읽었다.

(5.16), 오른쪽 $\zeta$ 차, 코드의 좌표 차가 모두 $(0,0)$을 요구한다.

수정식은 $(\vec x_{2,0}-\vec x_{0,0})\nabla\zeta\big\vert_{(1,0)}=\zeta_{2,0}-\zeta_{0,0}$다. 근거: `src/swancom1.ftn:10766` `JCTA(INDX,1,2,2) = XCGRID(IX+1,IY) - XCGRID(IX  ,IY)`; 11086–11087은 중심과 오른쪽 점의 반대 계수다.
$$\tfrac{1}{2}((\vec{x}_{2,2}-\vec{x}_{2,-2})+(\vec{x}_{0,2}-\vec{x}_{0,-2}))\nabla\zeta|_{(1,0)} = \tfrac{1}{2}((\zeta_{2,2}-\zeta_{2,-2})+(\zeta_{0,2}-\zeta_{0,-2})) \quad \text{(5.18)}$$
swantech PDF 130쪽 / 인쇄 122쪽, (5.19): $\nabla\zeta\big\vert_{(1,0)}=\left.\zeta\right\vert_{(0,0)}^{(2,0)}\vec c^{(1)}+(\left.\zeta\right\vert_{(0,-2)}^{(0,2)}+\left.\zeta\right\vert_{(2,-2)}^{(2,2)})\vec c^{(2)}$.

swantech PDF 130쪽 / 인쇄 122쪽, (5.20): $\vec c^1=C^{-1}(c_{(2)}^2,-c_{(2)}^1)$; $\vec c^2=C^{-1}(-c_{(1)}^2,c_{(1)}^1)$.

swantech PDF 130쪽 / 인쇄 122쪽, (5.21): $C=c_{(2)}^2c_{(1)}^1-c_{(1)}^2c_{(2)}^1$.

swantech PDF 130쪽 / 인쇄 122쪽, (5.22): $\vec c_{(1)}=a_{(1)}\big\vert_{(1,0)}$, $\vec c_{(2)}=\vec a_{(2)}\big\vert_{(0,-1)}+\vec a_{(2)}\big\vert_{(0,1)}+\vec a_{(2)}\big\vert_{(2,-1)}+\vec a_{(2)}\big\vert_{(2,1)}$. [10-13 전수 검증 정정]

### B.4 BC 처리 (Eq 5.23-5.24)

- **Dirichlet**: 해당 행 = 0, 대각 = 1, BC 값을 RHS 에. (간단)
- **Neumann**: half-cell 적분 (Fig 5.2):
swantech PDF 131쪽 / 인쇄 123쪽, (5.23): $\int_{\Omega_\xi}\partial_{\xi^\alpha}(\sqrt g\vec a^{(\alpha)}\cdot(k\nabla\zeta+\vec F)d\Omega_\xi\simeq\tfrac12\left.\sqrt g\vec a^{(1)}\cdot(k\nabla\zeta+\vec F)\right\vert_{(-1,0)}^{(1,0)}+\left.\sqrt g\vec a^{(2)}\cdot(k\nabla\zeta+\vec F)\right\vert_{(0,0)}^{(0,1)}$. 첫 적분의 바깥 닫는 괄호 누락을 원문대로 둔다.

코드는 반 셀 방정식 전체를 2배 한다. 접선 면은 내부와 같은 계수다. 안쪽 법선 면은 내부의 2배다. 경계 면 유량은 0이다. 원문의 첫 적분에는 바깥 닫는 괄호가 빠져 있지만, 이 조판 누락은 반 셀 계수의 대응을 바꾸지 않는다. 근거: `src/swancom1.ftn:10878` `RHS(INDX) = RHS(INDX) - JCTA(INDX,2,2,1)`; `src/swancom1.ftn:11218` `DEPF = DEPTH(INDX)+DEPTH(INDXU)`.
swantech PDF 131쪽 / 인쇄 123쪽, (5.24) 첫 줄: $(\vec x_{(2,0)}-\vec x_{(1,0)})\cdot\nabla\zeta\big\vert_{(1,0)}=\zeta_{(2,0)}-\zeta_{(0,0)}$.

좌변 길이는 반 격자인데 우변은 한 격자의 수위 차다. 첫 줄의 두 번째 좌표는 $(0,0)$이어야 (5.16) 및 코드와 일치한다.

수정식은 $(\vec x_{(2,0)}-\vec x_{(0,0)})\cdot\nabla\zeta\big\vert_{(1,0)}=\zeta_{(2,0)}-\zeta_{(0,0)}$다. 근거: `src/swancom1.ftn:10766` `JCTA(INDX,1,2,2) = XCGRID(IX+1,IY) - XCGRID(IX  ,IY)`.

swantech PDF 131쪽 / 인쇄 123쪽, (5.24) 둘째 줄: $((x_{(2,2)}-x_{(2,0)})+(\vec x_{(0,2)}-\vec x_{(0,0)}))\cdot\nabla\zeta\big\vert_{(1,0)}=(\zeta_{(0,2)}-\zeta_{(0,0)})+(\zeta_{(2,2)}-\zeta_{(2,0)})$. [10-13 전수 검증 정정]

가상점 값을 $\zeta_{ghost}=2\zeta_{boundary}-\zeta_{inside}$로 소거하면 같은 한쪽 차분이 된다. PDF에서 첫 좌표 차의 두 $x$에는 벡터 화살표가 생략됐지만 좌표 차의 의미는 정해진다. 근거: `src/swancom1.ftn:11237` `AMAT(INDX,5) = AMAT(INDX,5) + 2.*AMAT(INDX,2)`; `src/swancom1.ftn:11238` `AMAT(INDX,7) = AMAT(INDX,7) - AMAT(INDX,2)`; `src/swancom1.ftn:11239` `AMAT(INDX,2) = 0.`. [10-13 전수 검증 정정]

### B.5 Dry points

- 최종 마름점 행은 대각 1과 우변 0이다. 근거: `src/swancom1.ftn:11160` `AMAT(INDX,:) = 0.0`; `src/swancom1.ftn:11161` `AMAT(INDX,1) = 1.0`; `src/swancom1.ftn:11162` `RHS (INDX  ) = 0.0`. 웹 `online_doc/swantech/node72.html:51–53`과 `node75.html:97–98`의 상반된 설명.
- 젖은 점과 마른 점 사이 면은 제외한다. 내부 젖은 면의 횡방향 차분을 마름점에 따라 모두 한쪽 차분으로 바꾸는 구현은 없다. 외곽 경계의 한쪽 차분과 구분한다. 근거: `src/swancom1.ftn:11075–11157`; `src/swancom1.ftn:11237–11245`.

### B.6 Matrix 구축 + §5.2.2 solver

- Integration point loop (점 (0,1) in $(i,j)$ = 점 (0,-1) in $(i-1,j)$ → 2 set만), **distribution** (계수 × factor → matrix).
- 행렬계:
$$Ax = f \quad \text{(5.25)}$$
- 실제 벡터는 `MCGRD` 크기다. `KGRPNT`가 격자 좌표를 저장 인덱스로 변환한다. 좌표나 수심이 제외값인 점은 인덱스 1을 공유한다. 근거: `src/swancom1.ftn:10577` `REAL    AMAT(MCGRD,9), JCTA(MCGRD,2,2,2), RHS(MCGRD)`; `src/swancom1.ftn:11853` `INDX = KGRPNT(IX  ,IY  )`; 11863–11870은 여덟 비대각 계수의 이웃값을 읽는다. `src/swanpre1.ftn:5123–5169`의 주소 설정. [10-13 전수 검증 정정]

실제 저장 인덱스는 `KGRPNT`로 연결하는 `MCGRD`다. `SWDIM`은 좌표나 수심이 제외값인 점의 주소를 1로 두고 유효점에 별도 주소를 부여한다. 수심 때문에 현재 마른 점이 모두 주소 1을 공유한다고 일반화할 수 없다. 9개 계수 저장은 문서와 같다. swantech 5.2.2의 벡터 차원이 항상 $MXC\times MYC$라는 설명은 코드의 저장 구조와 다르다.
- 일반 곡선 격자와 변수 수심에서는 내부 계수도 비대칭일 수 있다. 비대칭의 원인을 경계·마름점에만 한정하지 않는다. 직교 격자 등의 별도 조건에서는 내부 대칭이 성립할 수 있다. 근거: swantech PDF 133쪽 / 인쇄 125쪽; `src/swancom1.ftn:11076` `DEPF = 0.5*(DEPTH(INDX)+DEPTH(INDXR))`; `src/swancom1.ftn:11093` `AMAT(INDX,9) = AMAT(INDX,9) + 0.25*CONTRB`; 11135의 같은 대입; 11111·11153의 `AMAT(INDX,2) = AMAT(INDX,2) - 0.25*CONTRB`.
- **Solver**: 1D = trapezoidal rule. **2D = modified SOR (Botta-Ellenbroek 1985)** ([swan-tech-ch6-iterative-solvers](swan-tech-ch6-iterative-solvers.md)).

코드는 계산 격자 전체에서 선택한 최심점의 set-up을 `SUPCOR`에 맞춘다. 이 점을 외곽 경계점으로 제한하지 않는다. `SUPCOR` 기본값은 0이다. 근거: `src/swancom1.ftn:10215` `DO IY = 1, MYC`; `src/swancom1.ftn:10216` `DO IX = 1, MXC`; `src/swancom1.ftn:10223` `IF (DEPSAV(INDX).GT.DEPMAX) THEN`; `src/swancom1.ftn:10413` `S_UPCOR = S_UPDP - PSETUP(2)`. 웹 `online_doc/swanuse/node28.html:2986–2999`; `src/swanmain.ftn:1201` `PSETUP(2) = 0.0`.

swanuse PDF 86–87·SETUP 절(node28:2971–2982)은 비구조·구면·병렬 실행 제한을 이미 설명한다. 코드는 `IF (PARLL .AND. .NOT.ONED) THEN`에서 오류 수준 4를 내고 반환한다. `IF (OPTG.EQ.5) THEN`에서는 `LSETUP = 0`으로 설정한다. 구면좌표는 `IF (KSPHER.NE.0)`에서 오류 수준 2를 보고한다. C는 swantech 5장에 없는 이 조건별 처리와 `IF ( ICONV.EQ.0 ) THEN` 안의 `CSETUP = .FALSE.`, `IF ( RESM.GT.1.E8 ) SETUP = 0.`에 한정한다. 근거: [swan-setup-solver-swancom1-crosswalk](../source-analysis/swan-setup-solver-swancom1-crosswalk.md).

## C. SWAN 옵션 매핑

| Tech (PDF) | User cmd | 비고 |
|---|---|---|
| Ch 4 BC | `BOUNDSPEC` (JONSWAP/PM/Gauss/file) + `BOUNDNEST` | 2D spectrum 3 옵션 |
| Ch 4 IC | `INITIAL DEFAULT/ZERO/PAR/HOTSTART` | Kahma-Calkoen 1992 default |
| 5.1-5.25 2D setup | `SETUP` | Poisson FV, modified SOR |
| diagnostic tail | `SET PWTAIL=...` | 선택한 발생 모드가 지수를 다시 정하는 경로와 GEN4의 꼬리 제거를 함께 적는다. `src/swanpre1.ftn:2192` `CALL INREAL ('PWTAIL', PWTAIL(1), 'UNC', 0.)` |

## D. 한계

- (5.14)–(5.24)는 swantech PDF 130–131쪽 / 인쇄 122–123쪽의 전체 식을 사용한다. (5.17) 첨자와 (5.24) 첫 줄의 좌표 오류는 인쇄 원문과 수정식을 나누어 적는다.
- (5.24)는 PDF에도 번호가 있다. 근거: swantech PDF 131쪽 / 인쇄 123쪽.
- §5.2.2 The iterative solver (node77)는 SOR 참조만 (상세는 Ch 6 [swan-tech-ch6-iterative-solvers](swan-tech-ch6-iterative-solvers.md)).

## E. 연결

- [swan-tech-ch2-obstacles-diffraction-setup](swan-tech-ch2-obstacles-diffraction-setup.md) — §2.6 1D set-up (Eq 2.143-2.145, 2D 의 출발식)
- [swan-tech-ch3-qc-curvilinear](swan-tech-ch3-qc-curvilinear.md) — §3.10 곡선좌표 (covariant/contravariant 공유)
- [swan-tech-ch6-iterative-solvers](swan-tech-ch6-iterative-solvers.md) — Ch 6 SIP/SOR (5.25 solver)
- [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) — §3.3 작용평형식의 SIP 해법 (swantech PDF 90쪽 / 인쇄 82쪽) [10-13 전수 검증 정정]

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R3:BC-005 | 명시적 최저 주파수 경계 유량 | swantech PDF 125쪽 / 인쇄 117쪽, 같은 흡수 경계 조건. | `src/swancom1.ftn:5451` `ELSE IF ( INT(PNUMS(8)) .EQ. 2 ) THEN`; `src/swancom5.ftn:3680` `IF ( IS .EQ. 1 ) THEN`; `src/swancom5.ftn:3688` `FLEFT = 0.`. | E 코드 결함 후보 · 강함 | 명시적 `STRSSB`는 최저 주파수 외부 면 유량을 부호와 무관하게 0으로 둔다. 음의 $c_\sigma$에 따른 저주파 유출도 없다. 반대 근거로 3681행의 상류법 주석과 CFL 차단을 확인했다. 둘 다 이 외부 면의 유출을 복원하지 않는다. 같은 판 문서와 `STRSSI` 경로가 모두 유출을 허용한다. `src/swancom1.ftn:5437`의 `(DYNDEP .OR. ICUR.EQ.1) .AND. ITFRE.NE.0` 및 `INT(PNUMS(8)) .EQ. 2`에서 호출한다. `b2ae30e`·`7ee8981`·`43e9bbb`의 `src/swancom5.ftn:3688`에 같은 `FLEFT = 0.`이 남는다. [SWAN-git-verify-E.md](../../../_staging/recovery/compare/SWAN-git-verify-E.md)의 E 유지(강함)를 반영한다. STRSSB는 최저 주파수 바깥 면 유량을 항상 0으로 두어 저주파 쪽 유출도 차단한다. |
| R3:BC-006 | 에너지 꼬리와 작용밀도 지수 | swantech PDF 125쪽 / 인쇄 117쪽, 번호 없음: 진단 꼬리 $f^{-m}$, $m=4$ 또는 $m=5$. | `src/swanmain.ftn:1019` `PWTAIL(1) = 4.`; `src/swanmain.ftn:8494–8495` `LSPEC(ID,IS) = LSPEC(ID,ISIGTA) *` / `(SPCSIG(ISIGTA)/SPCSIG(IS))**(PWTAIL(1)+1)`; `src/swanmain.ftn:3849` `PWTAIL(5+IP) = 1. / (PPTAIL * (1. + PPTAIL * (FRINTH-1.)))`. | F 표기 차이 | 문서는 에너지 꼬리다. 코드는 작용밀도이므로 지수가 $m+1$이다. $E=\sigma N$를 대입하면 같다. 초기 대입의 에너지 지수는 4다. 선택 모드가 5로 바꾸는 경로는 CP-031에 적는다. 모멘트는 꼬리 적분 계수를 사용한다. |
| R3:BC-007 | GEN4의 진단 꼬리 제거 | swantech PDF 125쪽 / 인쇄 117쪽, 원문: 꼬리를 고주파 비선형 상호작용과 적분 파랑량에 사용한다. | `src/swanmain.ftn:6385` `PWTAIL(1) = 1.E8`; `src/swanmain.ftn:6386` `PWTAIL(2:10) = 0.`. | C 문서 누락 | `IF (IGEN.EQ.4) THEN` 안에서 `PWTAIL(1) = 1.E8`과 `PWTAIL(2:10) = 0.`을 적용한다(`src/swanmain.ftn:6372–6386`). 일반 모드의 고정 진단 꼬리 설정과 다르다. C는 swantech 4장과 swanuse SET 절의 일반 꼬리 설명에 이 `GEN4` 처리가 없는 차이로 한정한다. `SCAT`만 켠 모든 계산에 적용하는 예외로 일반화하지 않는다. |
| R3:BC-011 | 경계 거리 권고 | swantech PDF 126쪽 / 인쇄 118쪽, 원문: 경계 파랑 조건을 지정하지 않은 경우를 특히 들어 “model boundaries must be placed far away from the area of interest.” | `src/swanmain.ftn:6945`의 `CALL SINTRP`는 주어진 경계 스펙트럼만 배치한다. | H 코드 대조 대상 아님 | 결과 오차를 줄이기 위한 경계 배치 권고다. 코드는 관심 영역까지의 최소 거리를 강제하지 않는다. 권고의 직접 조건은 관측 부재 자체가 아니라 경계 파랑 조건의 부재다. swanuse PDF 20과 `website/online_doc/swanuse/node11.html:61–69`은 다른 모델의 경계 자료가 있는 경우도 구분한다. |
| R3:BC-013 | 기본 초기화의 약풍·무풍 예외 | swantech PDF 126쪽 / 인쇄 118쪽, 원문: 국소 바람과 Kahma–Calkoen 성장곡선을 사용하고 PM 값으로 제한한다. | `src/swanmain.ftn:9074` `HSDLSS = MIN (0.21, 0.00288*FDLSS**0.45)`; `src/swanmain.ftn:9077` `TPDLSS = MIN (1./0.13, 0.46*FDLSS**0.27)`; `src/swanmain.ftn:9079` `IF (SPPARM(1).LT.0.05) SPPARM(2) = 2.`; `src/swanmain.ftn:9086` `SPPARM(1) = 0.02`. | C 문서 누락 | 제한된 성장곡선 경로가 있다. 그러나 $H_s<0.05$ m이면 주기를 2 s로 덮어쓴다. 바람이 $10^{-10}$ 이하이면 $H_s=0.02$ m, $T=2$ s의 씨앗 스펙트럼을 만든다. 문서는 이 예외를 적지 않았다. 계수의 원논문 대조는 CP-020에 구분한다. 무풍 예외의 실제 분기는 `src/swanmain.ftn:9065`의 `IF (WSLOC .GT. 1.E-10) THEN`에 대한 `ELSE`이며 9086–9089행이 네 매개변수를 정한다. swanuse PDF 64의 INITIAL DEFAULT도 성장곡선만 설명하므로 C는 이 두 매뉴얼의 작은 파고·영 바람 예외 설명에 한정한다. |
| R3:BC-014 | 초기화의 대표 취송거리 | swantech PDF 126쪽 / 인쇄 118쪽, 원문: “The average (over the model area) spatial step size is used as fetch with local wind.” | `src/swanmain.ftn:9003` `TLEN = (XCLEN + YCLEN)/2.`; `src/swanmain.ftn:9008` `TDXY = FLOAT(MXCGL + MYCGL)/2.`; `src/swanmain.ftn:9009` `IF ( nvertsg.NE.0 ) TDXY = FLOAT(nvertsg)`; `src/swanmain.ftn:9011` `FETCH = TLEN/TDXY`. | C 문서 누락 | 직교좌표의 구조 격자는 `TLEN = (XCLEN + YCLEN)/2.`와 `TDXY = FLOAT(MXCGL + MYCGL)/2.`의 비를 취송거리로 쓴다. 구면좌표에서는 `TLEN = LENDEG * (COSYG*XCLEN + YCLEN)/2.`로 바꾼다(`src/swanmain.ftn:9002–9011`). `nvertsg.NE.0`이면 분모는 전체 정점 수다. C는 swantech 4장과 swanuse PDF 64의 평균 공간 간격 설명에 이 대체 계산식이 없는 차이다. |
| R3:BC-015 | 정상 2세대 예측의 조건 | swantech PDF 126쪽 / 인쇄 118쪽, 원문: 정상 계산의 첫 추정은 기본적으로 “the second generation mode of SWAN”. | `src/swancom1.ftn:1453` `IF ( IWIND.GE.3 .AND. NSTATC.EQ.0 .AND. ICOND.NE.4 ) THEN`; `src/swancom1.ftn:1455` `PRECOR = .TRUE.`; `src/swancom1.ftn:1457` `PRECOR = .FALSE.`. | C 문서 누락 | 문서는 정상 계산의 기본 첫 추정을 설명한다. 비정상 제외 자체는 문서와 일치한다. 코드는 `IF ( IWIND.GE.3 .AND. NSTATC.EQ.0 .AND. ICOND.NE.4 ) THEN`일 때만 `PRECOR = .TRUE.`로 둔다. swanuse PDF 64–65는 HOTSTART가 기본 초기화를 덮어쓴다고 설명한다. C는 swantech 4장에 없는 활성 바람 조건과 HOTSTART 제외의 구체 분기로 좁힌다. |
| R3:CP-020 | 기본 초기화의 성장곡선 계수 | — (문서 누락) | 기본 초기화의 성장곡선 계수. `src/swanmain.ftn:9071` `FDLSS = GRAV * FETCH / (WSLOC*WSLOC)`; `src/swanmain.ftn:9074` `HSDLSS = MIN (0.21, 0.00288*FDLSS**0.45)`; `src/swanmain.ftn:9075` `SPPARM(1) = HSDLSS * WSLOC**2 / GRAV`; `src/swanmain.ftn:9077` `TPDLSS = MIN (1./0.13, 0.46*FDLSS**0.27)`; `src/swanmain.ftn:9078` `SPPARM(2) = WSLOC * TPDLSS / GRAV`. | C 문서 누락 | 무차원 취송거리 $gF/U_{10}^2$에서 파고와 주기를 구한다. 4장은 Kahma–Calkoen과 PM의 이름만 제시한다. 이 계수와 지수는 제시하지 않는다. 이 행은 코드의 성장곡선 계수와 swantech 4장의 생략을 대조한다. [10-13 전수 검증 정정] |
| R3:CP-021 | 경계 스펙트럼 형상 | — (문서 누락) | 경계 스펙트럼 형상. `src/swanser.ftn:4049` `SALPHA = ((SPPARM(1) ** 2) * (FPK4)) * 5. / 16.`; `src/swanser.ftn:4067` `RA = (SALPHA/SF5)*EXP(-(5.*FPK4)/(4.*SF4))/(PI2*SPCSIG(IS))`; 4052–4053은 Jonswap 정규화 분모 `(0.06533*(PSHAPE(1)**0.8015)+0.13467)*16.`이다. 4087·4089의 폭은 0.07·0.09다. 4091 `APSHAP =  0.5 * ((SF-FPK) / (COEFF*FPK)) **2`; `src/swanser.ftn:4096` `SYF = PSHAPE(1)**PPSHAP`. | C 문서 누락 | swanuse BOUND SHAPESPEC 절(node27:98–135)은 JONSWAP·PM·TMA·GAUSS·BIN 선택지와 BIN의 최근접 주기 빈을 이미 적는다. C는 swantech 4장과 이 절에 없는 구체 계수·정규화·절단식에 한정한다. `LSHAPE.EQ.2 .OR. LSHAPE.EQ.5`인 JONSWAP·TMA 분기에서만 `IF (CPSHAP.GT.10.) THEN`에 따라 `RA = 0.`으로 둔다. `IF (APSHAP.GT.10.) THEN`이면 `SYF = 1.`이다. TMA는 `RA = RA * (TANH(K*DP))**2 / (2.*N)`를 곱한다. BIN은 `ACLOC(MDC,IS) = ( SPPARM(1)**2 ) / ( 16. * SPCSIG(IS)**2 * FRINTF )`다. Gaussian은 4055–4056행의 `AUX1`, `AUX3`와 4117–4118행의 `RA = AUX1 * EXP ( -1. * AUX2 / AUX3 ) / SPCSIG(IS)`를 쓴다. |
| R3:CP-026 | 명시적 주파수 이동의 차단 | — (문서 누락) | 명시적 주파수 이동의 차단. `src/swancom5.ftn:3663` `TS = CASCEN / DS`; `src/swancom5.ftn:3664` `CFLCEN = TS / MAX( 1.E-20 , ( TX + TY ) )`; `src/swancom5.ftn:3670` `IF ( CFLCEN .GT. CFLMAX ) THEN`; `src/swancom5.ftn:3674` `ANYBLK(ID,IS) = .TRUE.`. | C 문서 누락 | 주파수 이동과 지리 전파의 비가 `PNUMS(19)`를 넘으면 빈을 비활성화한다. 4장의 완전 흡수 경계 설명은 이 별도 차단 기준을 적지 않는다. 저주파 외부 면 문제는 BC-005에 판정했다. swanuse 명령 구문 PDF 141·node49:317–319는 `SIGEXpl [css] [cfl]`을 이미 열거한다. C는 swantech 4장의 경계 설명과 swanuse NUMERIC 절에 없는 `CFLCEN = TS / MAX( 1.E-20 , ( TX + TY ) )` 및 `ANYBLK` 차단 동작에 한정한다. `src/swanpre1.ftn:2032–2037`은 이 명시 해법의 `CFL`을 `PNUMS(19)`에 저장한다. |
| R3:CP-029 | 파일 1D 방향 분포 | — (문서 누락) | 파일 1D 방향 분포. `src/swanmain.ftn:8358` `IF (MS.GT.10.) THEN`; `src/swanmain.ftn:8359` `CTOT = SQRT(MS/(2.*PI)) * (1. + 0.25/MS)`; `src/swanmain.ftn:8367` `CDIR = CTOT * MAX (ACOS**MS, 1.E-10)`; `src/swanmain.ftn:8369` `CDIR = 1.E-10`; `src/swanmain.ftn:8372` `BAUX2(ID,IFRE) = CDIR * ETOT`. | C 문서 누락 | 입력 에너지 `ETOT`가 양수인 파일 1D 스펙트럼은 반대 반원에도 작은 양의 방향 밀도를 둔다. 매개변수 `SSHAPE`는 반대 반원을 0으로 둔다. 정규화 근사의 전환 지수도 각각 10과 12로 다르다. 4장은 이 형식별 차이를 적지 않았다. C의 문서 범위는 swantech 4장과 swanuse BOUND SHAPESPEC·FILE 절이다. 입력 에너지가 0이면 `BAUX2(ID,IFRE) = CDIR * ETOT`도 0이다. |
| R3:CP-031 | 진단 꼬리 지수의 선택 모드 의존 | — (문서 누락) | 진단 꼬리 지수의 선택 모드 의존. `src/swanmain.ftn:1019` `PWTAIL(1) = 4.`; `src/swanpre1.ftn:2489` `CALL INREAL ('PWTAIL', PWTAIL(1), 'STA', 5.)`; `src/swanpre1.ftn:2826–2827` `IF (EQREAL(PWTAIL(1),4.)) THEN` / `PWTAIL(1) = 5.`; 2862–2863과 2927–2928도 4를 5로 바꾼다. | F 표기 차이 | swantech 4장은 $m=4$ 또는 $m=5$만 쓴다. swanuse SET 절(PDF 37; `website/online_doc/swanuse/node23.html:415–448`)은 모드별 기본값과 SET을 GEN 뒤에 두는 순서를 이미 적는다. 따라서 그 기본값과 순서는 swanuse 기준으로 일치한다. 코드에만 명시된 세부 조건은 `IF (EQREAL(PWTAIL(1),4.)) THEN`일 때 5로 바꾸는 비교와 WCAP JANSSEN 분기(2473행)의 `CALL INREAL ('PWTAIL', PWTAIL(1), 'STA', 5.)`이다. 선택 모드와 입력 순서 전체가 문서에 없다는 C 판정을 F로 낮춘다. |
| R3:NT-016 | 5장 힘 부호의 전사 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch4-5-bc-2d-setup.md:55` `F_x + F_y = 0`; 59의 `+ \frac{\partial F_x}{\partial x}`; 62의 `F_n +`; 68–69의 같은 양수. | `src/swancom1.ftn:10392` `-(RSXXI*DIX + RSXXJ*DJX + RSXYI*DIY + RSXYJ*DJY)`; 10394는 y방향 힘이다. swantech PDF 127의 “wave-induced force in $x_i$-direction per unit mass”; PDF 66 (2.145).<br>`src/swancom1.ftn:11080` `FACT = -DEPF/JAC`; `src/swancom1.ftn:11086` `AMAT(INDX,1) = AMAT(INDX,1) - CONTRB`; `src/swancom1.ftn:10825` `RHS(INDX) = RHS(INDX) - 0.5*JCTA(INDX,1,1,1)`. swantech PDF 127의 힘 단위 정의와 PDF 66 (2.145).<br>`src/swancom1.ftn:10877` `IF ( INDXU.GT.1 .AND. DEPTH(INDXU).GT.DEPMIN ) THEN`; `src/swancom1.ftn:11218` `DEPF = DEPTH(INDX)+DEPTH(INDXU)`. | B 문서 오기 | 원문 식을 인용한 뒤 부호 오류를 적는다. $F=-\nabla\cdot S/\rho$이면 평형은 $gd\nabla\zeta-F=0$다. Poisson 식은 $\nabla\cdot(gd\nabla\zeta-F)=0$다. 경계 조건은 $gd\zeta_n-F_n=0$다. |
| R3:NT-017 | 기준 수위 점의 위치 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch4-5-bc-2d-setup.md:63` `최대수심 경계점서 $\zeta=0$ 고정`; 112 `최심 경계점 = setup 0`. | `src/swancom1.ftn:10215` `DO IY = 1, MYC`; `src/swancom1.ftn:10216` `DO IX = 1, MXC`; `src/swancom1.ftn:10223` `IF (DEPSAV(INDX).GT.DEPMAX) THEN`; `src/swancom1.ftn:10413` `S_UPCOR = S_UPDP - PSETUP(2)`. 웹 `online_doc/swanuse/node28.html:2986–2999`; `src/swanmain.ftn:1201` `PSETUP(2) = 0.0`. | B 문서 오기 | 코드는 계산 격자 전체에서 선택한 최심점의 set-up을 `SUPCOR`에 맞춘다. 이 점을 외곽 경계점으로 제한하지 않는다. `SUPCOR` 기본값은 0이다. |
| R3:NT-018 | 마름점 행과 한쪽 차분 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch4-5-bc-2d-setup.md:102` `dry 점 자체: 행 + RHS = 0`; 103 `one-sided`와 `$\nabla\zeta = 0$`. | `src/swancom1.ftn:11160` `AMAT(INDX,:) = 0.0`; `src/swancom1.ftn:11161` `AMAT(INDX,1) = 1.0`; `src/swancom1.ftn:11162` `RHS (INDX  ) = 0.0`. 웹 `online_doc/swantech/node72.html:51–53`과 `node75.html:97–98`의 상반된 설명.<br>`src/swancom1.ftn:11090–11093`은 주변 네 점에 `0.25*CONTRB`를 배분한다. 11075의 조건은 면 양 끝만 검사한다. 10720–10727의 기저 계산은 이 네 점의 수심을 검사하지 않는다. swantech PDF 132 “This process is applied for all transitions from wet to dry points.”; `src/swancom1.ftn:11073–11093,11167–11245`. | B 문서 오기 | 최종 마름점 행은 대각 1과 우변 0이다. 젖은 점과 마른 점 사이 면은 제외한다. 내부 젖은 면의 횡방향 차분을 마름점에 따라 모두 한쪽 차분으로 바꾸는 구현은 없다. 외곽 경계의 한쪽 차분과 구분한다. |
| R3:NT-019 | set-up 저장 벡터 크기 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch4-5-bc-2d-setup.md:110` `direct addressing (dry 포함) → 차원 고정 $MXC\times MYC$`. | `src/swancom1.ftn:10577` `REAL    AMAT(MCGRD,9), JCTA(MCGRD,2,2,2), RHS(MCGRD)`; `src/swancom1.ftn:11853` `INDX = KGRPNT(IX  ,IY  )`; 11863–11870은 여덟 비대각 계수의 이웃값을 읽는다. `src/swanpre1.ftn:5123–5169`의 주소 설정. | B 문서 오기 | 실제 벡터는 `MCGRD` 크기다. `KGRPNT`가 격자 좌표를 저장 인덱스로 변환한다. 좌표나 수심이 제외값인 점은 인덱스 1을 공유한다. [10-13 전수 검증 정정] |
| R3:NT-020 | 5장 식의 참조·생략·첨자 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch4-5-bc-2d-setup.md:80` `(5.7)을 (5.5)에 적용:`; 125 `ASCII/truncated 다행식 → 구조 전사`; 126 `PDF 5.24 는 grep서 무번호로 보이나`. | `src/swancom1.ftn:10823` `! --- contribution of right flux`; `src/swancom1.ftn:11074` `! --- contribution of right flux`.<br>`src/swancom1.ftn:10766` `JCTA(INDX,1,2,2) = XCGRID(IX+1,IY) - XCGRID(IX  ,IY)`; 11086–11087은 중심과 오른쪽 점의 반대 계수다.<br>`src/swancom1.ftn:10766` `JCTA(INDX,1,2,2) = XCGRID(IX+1,IY) - XCGRID(IX  ,IY)`. | B 문서 오기 | (5.7)은 지배식 (5.4)에 적용한다. 이 보고서 SU-021–SU-032의 전체 식으로 생략 부호를 보충한다. (5.17) 첨자와 (5.24) 첫 줄의 좌표 오류는 인쇄 원문과 수정식을 나누어 적는다. (5.24)는 PDF에도 번호가 있다. |
| R3:NT-021 | 주파수 경계의 모드별 예외 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch4-5-bc-2d-setup.md:36` `최저·최고 이산주파수서 **fully absorbing**` 및 `diagnostic tail`. | `src/swancom1.ftn:5451` `ELSE IF ( INT(PNUMS(8)) .EQ. 2 ) THEN`; `src/swancom5.ftn:3680` `IF ( IS .EQ. 1 ) THEN`; `src/swancom5.ftn:3688` `FLEFT = 0.`.<br>`src/swanmain.ftn:6385` `PWTAIL(1) = 1.E8`; `src/swanmain.ftn:6386` `PWTAIL(2:10) = 0.`. | C 문서 누락 | 기본 암시적 주파수 경계는 흡수 조건이다. 명시적 STRSSB의 최저 주파수 바깥 면은 유출도 0으로 둔다. GEN4는 `PWTAIL(1) = 1.E8`, `PWTAIL(2:10) = 0.`으로 진단 꼬리를 억제한다. 이 GEN4 대입을 모든 SCAT 실행에 일반화하지 않는다. |
| R3:NT-022 | 초기 조건의 적용 조건 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch4-5-bc-2d-setup.md:46` `fetch = 평균 spatial step`; 47 `Stationary first guess`. | `src/swanmain.ftn:9074` `HSDLSS = MIN (0.21, 0.00288*FDLSS**0.45)`; `src/swanmain.ftn:9077` `TPDLSS = MIN (1./0.13, 0.46*FDLSS**0.27)`; `src/swanmain.ftn:9079` `IF (SPPARM(1).LT.0.05) SPPARM(2) = 2.`; `src/swanmain.ftn:9086` `SPPARM(1) = 0.02`.<br>`src/swanmain.ftn:9003` `TLEN = (XCLEN + YCLEN)/2.`; `src/swanmain.ftn:9008` `TDXY = FLOAT(MXCGL + MYCGL)/2.`; `src/swanmain.ftn:9009` `IF ( nvertsg.NE.0 ) TDXY = FLOAT(nvertsg)`; `src/swanmain.ftn:9011` `FETCH = TLEN/TDXY`.<br>`src/swancom1.ftn:1453` `IF ( IWIND.GE.3 .AND. NSTATC.EQ.0 .AND. ICOND.NE.4 ) THEN`; `src/swancom1.ftn:1455` `PRECOR = .TRUE.`; `src/swancom1.ftn:1457` `PRECOR = .FALSE.`. | C 문서 누락 | 기본 초기화는 계산된 취송거리와 국소 바람을 사용한다. `WSLOC.GT.1.E-10`이 거짓이면 $H_s=0.02$ m, $T=2$ s를 사용한다. 정상 2세대 예측의 조건은 `IWIND.GE.3 .AND. NSTATC.EQ.0 .AND. ICOND.NE.4`다. 격자별 취송거리 식은 BC-014의 조건을 유지한다. |
| R3:NT-023 | PWTAIL 명령 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch4-5-bc-2d-setup.md:121` `QUANTITY ... PWTAIL`. | `src/swanpre1.ftn:2169` `IF (KEYWIS ('SET')) THEN`; `src/swanpre1.ftn:2192` `CALL INREAL ('PWTAIL', PWTAIL(1), 'UNC', 0.)`. | B 문서 오기 | 진단 꼬리 지수는 `SET PWTAIL=...`로 지정한다. 선택한 발생 모드가 지수를 다시 정하는 경로와 GEN4의 꼬리 제거를 함께 적는다. |
| R3:NT-052 | 내부 행렬 대칭성의 전사 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch4-5-bc-2d-setup.md:111` `내부 대칭 ($a_{i,j}=a_{j,i}$)이나 BC/dry 로 **비대칭**`. | `src/swancom1.ftn:10720–10796`의 기저벡터와 11076·11093·11135·11111·11153행의 조립식을 대입하면 $a_{PQ}=s(2d_P+d_E+d_N)/8$, $a_{QP}=s(2d_Q+d_E+d_N)/8$이다. $s\ne0$, $d_P\ne d_Q$이면 두 계수는 다르다. | B 문서 오기 | 일반 곡선 격자와 변수 수심에서는 내부 계수도 비대칭일 수 있다. 비대칭의 원인을 경계·마름점에만 한정하지 않는다. 직교 격자 등의 별도 조건에서는 내부 대칭이 성립할 수 있다. |
| R3:SU-005 | 식 (5.1)의 성분·힘 부호 | swantech PDF 127쪽 / 인쇄 119쪽, (5.1): $gd(\partial_x\zeta+\partial_y\zeta)+F_x+F_y=0$. | `src/swancom1.ftn:10392` `-(RSXXI*DIX + RSXXJ*DJX + RSXYI*DIY + RSXYJ*DJY)`; 10394는 y방향 힘이다. swantech PDF 127의 “wave-induced force in $x_i$-direction per unit mass”; PDF 66 (2.145). | B 문서 오기 | 두 방향 성분을 스칼라로 더한 (5.1)에 다시 “divergence”를 취해 (5.2)를 얻을 수 없다. 벡터 평형이 필요하다. 5장은 $F_i$를 “per unit mass”로 정의한다. 2.6절의 힘을 밀도로 나눈 값과 비교하면 $gd\nabla\zeta-\vec F=0$이어야 한다. 밀도 정규화는 이 부호 차이를 없애지 않는다. |
| R3:SU-006 | 식 (5.2)의 힘 부호 | swantech PDF 127쪽 / 인쇄 119쪽, (5.2): $\partial_x(gd\partial_x\zeta)+\partial_y(gd\partial_y\zeta)+\partial_xF_x+\partial_yF_y=0$. | `src/swancom1.ftn:11080` `FACT = -DEPF/JAC`; `src/swancom1.ftn:11086` `AMAT(INDX,1) = AMAT(INDX,1) - CONTRB`; `src/swancom1.ftn:10825` `RHS(INDX) = RHS(INDX) - 0.5*JCTA(INDX,1,1,1)`. swantech PDF 127의 힘 단위 정의와 PDF 66 (2.145). | B 문서 오기 | 5장의 $F_i$는 단위 질량당 힘이다. 코드의 $\mathrm{WFRC}=F_i/g$를 대입하면 $\nabla\cdot(gd\nabla\zeta)=\nabla\cdot\vec F$다. (5.2)는 반대 부호다. $\vec F$를 복사응력 발산으로 정의하면 형식은 같아지지만, PDF 127은 파랑 유발 힘이라고 명시한다. PDF 66 (2.145)을 밀도로 나누어도 이 부호 차이가 남는다. |
| R3:SU-007 | 식 (5.3)의 힘 부호 | swantech PDF 127쪽 / 인쇄 119쪽, (5.3): $F_n+gd\partial_n\zeta=0$. | `src/swancom1.ftn:10877` `IF ( INDXU.GT.1 .AND. DEPTH(INDXU).GT.DEPMIN ) THEN`; `src/swancom1.ftn:11218` `DEPF = DEPTH(INDX)+DEPTH(INDXU)`. | B 문서 오기 | 외부 면의 순유량을 0으로 두는 반 셀 방정식이다. 코드가 닫는 유량은 $d\nabla\zeta-\vec F/g$다. 물리적 힘의 부호 문제는 SU-006과 같다. |
| R3:SU-008 | 기준 수위의 최심점 위치 | swantech PDF 127쪽 / 인쇄 119쪽, 번호 없음: “the boundary point with the largest depth”; $\zeta=0$. swantech PDF 134쪽 / 인쇄 126쪽도 “at deepest boundary point: set-up is zero.”라고 적는다. | `src/swancom1.ftn:10215` `DO IY = 1, MYC`; `src/swancom1.ftn:10216` `DO IX = 1, MXC`; `src/swancom1.ftn:10223` `IF (DEPSAV(INDX).GT.DEPMAX) THEN`; `src/swancom1.ftn:10413` `S_UPCOR = S_UPDP - PSETUP(2)`. 웹 `online_doc/swanuse/node28.html:2986–2999`; `src/swanmain.ftn:1201` `PSETUP(2) = 0.0`. | B 문서 오기 | 코드는 경계로 한정하지 않는다. 현재 젖은 전체 격자에서 `DEPSAV`가 가장 큰 점을 고른다. 기본 `SUPCOR=0`이면 그 점의 set-up이 0이다. swanuse SETUP 절은 “the deepest point in the computational grid”라고 설명하여 코드와 일치한다. B 판정은 swantech 5장의 “boundary point” 한정에만 적용한다. |
| R3:SU-009 | 식 (5.4)의 힘 부호 | swantech PDF 128쪽 / 인쇄 120쪽, (5.4): $\frac{\partial}{\partial x_k}(F_k+gd\frac{\partial\zeta}{\partial x_k})=0$. | `src/swancom1.ftn:10392` `-(RSXXI*DIX + RSXXJ*DJX + RSXYI*DIY + RSXYJ*DJY)`; `src/swancom1.ftn:11080` `FACT = -DEPF/JAC`. | B 문서 오기 | (5.2)를 첨자로 쓴 식이다. 물리적 힘의 부호 문제도 같다. [10-13 전수 검증 정정] |
| R3:SU-010 | 식 (5.5)의 힘 부호 | swantech PDF 128쪽 / 인쇄 120쪽, (5.5): $F_n+gd\frac{\partial\zeta}{\partial n}=0$ at the boundary. | `src/swancom1.ftn:11175` `IF ( INDXR.GT.1 .AND. DEPTH(INDXR).GT.DEPMIN ) THEN`; `src/swancom1.ftn:11217` `IF ( INDXU.GT.1 .AND. DEPTH(INDXU).GT.DEPMIN ) THEN`. | B 문서 오기 | (5.3)의 반복이다. 코드의 유량 부호는 SU-007과 같다. |
| R3:SU-011 | 중첩 set-up의 Dirichlet 경계 | swantech PDF 128쪽 / 인쇄 120쪽, (5.6): $\zeta=\text{given at the boundary}$. 원문: “The setup computed in the larger model is used as boundary condition in the nested model.” | `src/swancom1.ftn:11781` `IF ( LSETUP.EQ.2 ) THEN`; `src/swanpre1.ftn:2094` `LSETUP = 1`. [SWAN-git-verify-D.md](../../../_staging/recovery/compare/SWAN-git-verify-D.md)의 SU-011. `43e9bbb:src/swanmain.ftn:1197` `! PSETUP(1) is currently unused, but can be used as setup nesting flag`; `src/swancom1.ftn:11781–11802`. | D 문서에만 있음 | 표준 입력은 중첩 set-up의 Dirichlet 경계를 활성화하지 않는다. 소스의 `LSETUP=2` 분기는 활성 입력 경로가 없는 내부 조립 분기다. `2980d1a`의 `src/swanpre1.ftn:2048`과 `43e9bbb`의 2094행은 모두 `LSETUP = 1`이다. 이 범위의 `LSETUP`·`PSETUP(1)` 이력 검색에는 변경 커밋이 없다. |
| R3:SU-012 | gd에서 d로의 정규화 | swantech PDF 128쪽 / 인쇄 120쪽, 번호 없음: “we use k instead of gd.” 즉 $k=gd$. | `src/swancom1.ftn:11076` `DEPF = 0.5*(DEPTH(INDX)+DEPTH(INDXR))`. | F 표기 차이 | 코드에서는 방정식 전체를 중력가속도로 나눈다. 따라서 확산계수 역할의 `DEPF`는 평균 수심이다. 5장의 $k$는 파수가 아니다. |
| R3:SU-013 | 식 (5.7)의 보존형 좌표 변환 | swantech PDF 128쪽 / 인쇄 120쪽, (5.7): $\frac{\partial\varphi}{\partial x^\beta}=\frac1{\sqrt g}\frac{\partial}{\partial\xi^\gamma}(\sqrt g\,a^{(\gamma)}_\beta\varphi)$. | `src/swancom1.ftn:10383` `DDET = DXI*DYJ - DXJ*DYI`; `src/swancom1.ftn:10384` `DIX = DYJ / DDET`; `src/swancom1.ftn:10385` `DIY = -DXJ / DDET`; `src/swancom1.ftn:10386` `DJX = -DYI / DDET`; `src/swancom1.ftn:10387` `DJY = DXI / DDET`. | F 표기 차이 | 해석: 연속 좌표계의 계량 항등식 $\partial_{\xi^\gamma}(\sqrt g\,a^{(\gamma)}_\beta)=0$를 쓰면 보통의 연쇄법칙이다. 코드는 힘 계산에 연쇄법칙을 쓰고 set-up 방정식에 유한체적 면 유량을 쓴다. |
| R3:SU-014 | 식 (5.8)의 역변 기저 | swantech PDF 129쪽 / 인쇄 121쪽, (5.8): $\vec a^{(\alpha)}=\nabla\xi^\alpha$. | `src/swancom1.ftn:10384` `DIX = DYJ / DDET`; `src/swancom1.ftn:10385` `DIY = -DXJ / DDET`. | F 표기 차이 | `DIX,DIY`가 첫 번째 역변 기저다. `DJX,DJY`가 두 번째 역변 기저다. 연속 정의를 좌표 차분으로 평가한다. |
| R3:SU-015 | 식 (5.9)의 Jacobian | swantech PDF 129쪽 / 인쇄 121쪽, (5.9): $\sqrt g=a_{(1)}^1a_{(2)}^2-a_{(1)}^2a_{(2)}^1$. | `src/swancom1.ftn:10383` `DDET = DXI*DYJ - DXJ*DYI`; `src/swancom1.ftn:11077–11078` `JAC = JCTA(INDX,1,1,1)*JCTA(INDX,1,2,2) -` / `JCTA(INDX,1,1,2)*JCTA(INDX,1,2,1)`. | F 표기 차이 | 같은 2차원 행렬식이다. `JCTA`는 Jacobian을 곱한 역변 기저를 저장한다. 이 기저의 행렬식도 2차원에서는 같은 Jacobian이다. |
| R3:SU-016 | 식 (5.10)의 공변 기저 | swantech PDF 129쪽 / 인쇄 121쪽, (5.10): $\vec a_{(\alpha)}=\frac{\partial\vec x}{\partial\xi^\alpha}$. | `src/swancom1.ftn:10752` `JCTA(INDX,2,1,1) = YCGRID(IX,IY+1) - YCGRID(IX,IY  )`; `src/swancom1.ftn:10753` `JCTA(INDX,2,1,2) = XCGRID(IX,IY  ) - XCGRID(IX,IY+1)`. | F 표기 차이 | 공변 기저의 좌표 차분을 회전하여 `JCTA`에 직접 저장한다. 별도의 공변 기저 배열은 필요하지 않다. |
| R3:SU-019 | 식 (5.13)의 변환 지배식 | swantech PDF 129쪽 / 인쇄 121쪽, (5.13): $\frac1{\sqrt g}\frac\partial{\partial\xi^\alpha}(\sqrt g\vec a^{(\alpha)}\cdot(k\nabla\zeta+\vec F))=0$. | `src/swancom1.ftn:10825–10828` `RHS(INDX) = RHS(INDX) - 0.5*JCTA(INDX,1,1,1)` / `*(WFRCX(INDX)+WFRCX(INDXR))` / `- 0.5*JCTA(INDX,1,1,2)` / `*(WFRCY(INDX)+WFRCY(INDXR))`. | F 표기 차이 | 좌표 변환 뒤 면에서 내적을 계산한다. 코드 변수로는 $k/g=d$, $\vec F_{5장}/g=-\mathrm{WFRC}$로 대응시켜야 한다. $\sqrt g$는 셀 적분에서 소거된다. [10-13 전수 검증 정정] |
| R3:SU-020 | 식 (5.13)의 참조 번호 | swantech PDF 129쪽 / 인쇄 121쪽, 원문: “Application of (5.7) to equation (5.5) results in” (5.13). | `src/swancom1.ftn:10823` `! --- contribution of right flux`; `src/swancom1.ftn:11074` `! --- contribution of right flux`. | B 문서 오기 | (5.5)는 경계의 법선 조건이다. 영역 전체의 발산식 (5.13)은 (5.4)를 변환한 결과다. 식 참조가 잘못됐다. |
| R3:SU-021 | 식 (5.14)의 셀 적분 | swantech PDF 130쪽 / 인쇄 122쪽, (5.14): $\int_{\Omega_x}\frac1{\sqrt g}\partial_{\xi^\alpha}(\sqrt g\vec a^{(\alpha)}\cdot(k\nabla\zeta+\vec F))d\Omega_x$; 다음 줄 $\int_{\Omega_\xi}\partial_{\xi^\alpha}(\sqrt g\vec a^{(\alpha)}\cdot(k\nabla\zeta+\vec F))d\Omega_\xi$; $\approx\left.\sqrt g\vec a^{(1)}\cdot(k\nabla\zeta+F)\right\vert_{(-1,0)}^{(1,0)}+\left.\sqrt g\vec a^{(2)}\cdot(k\nabla\zeta+\vec F)\right\vert_{(0,-1)}^{(0,1)}$. | `src/swancom1.ftn:10825` `RHS(INDX) = RHS(INDX) - 0.5*JCTA(INDX,1,1,1)`; 10832는 왼쪽 면의 양수 항이다. 10839는 위쪽 면의 음수 항이다. 10846은 아래쪽 면의 양수 항이다. | F 표기 차이 | $d\Omega_x=\sqrt g\,d\Omega_\xi$다. 코드는 네 면의 유출입 차를 조립한다. 우변으로 옮겨서 부호가 바뀐다. PDF의 첫 두 적분 사이에는 등호가 인쇄되지 않았다. 해당 두 적분은 같은 변수 변환을 나타낸다. [10-13 전수 검증 정정] |
| R3:SU-024 | 식 (5.17)의 좌표 첨자 | swantech PDF 130쪽 / 인쇄 122쪽, (5.17): $(\vec x_{2,0}-\vec x_{),0})\nabla\zeta\big\vert_{(1,0)}=\zeta_{2,0}-\zeta_{0,0}$. 두 번째 좌표의 첨자가 PDF에서 `),0`로 깨져 있다. Marker는 이를 `j,0`로 읽었다. | `src/swancom1.ftn:10766` `JCTA(INDX,1,2,2) = XCGRID(IX+1,IY) - XCGRID(IX  ,IY)`; 11086–11087은 중심과 오른쪽 점의 반대 계수다. | B 문서 오기 | (5.16), 오른쪽 $\zeta$ 차, 코드의 좌표 차가 모두 $(0,0)$을 요구한다. |
| R3:SU-026 | 식 (5.19)의 기울기 복원 | swantech PDF 130쪽 / 인쇄 122쪽, (5.19): $\nabla\zeta\big\vert_{(1,0)}=\left.\zeta\right\vert_{(0,0)}^{(2,0)}\vec c^{(1)}+(\left.\zeta\right\vert_{(0,-2)}^{(0,2)}+\left.\zeta\right\vert_{(2,-2)}^{(2,2)})\vec c^{(2)}$. | `src/swancom1.ftn:11084–11085` `CONTRB = FACT*(JCTA(INDX,1,1,1)*JCTA(INDX,1,1,1)+` / `JCTA(INDX,1,1,2)*JCTA(INDX,1,1,2))`; 11088–11093은 기저 내적에 따른 네 이웃 항이다. | F 표기 차이 | 코드는 $\nabla\zeta$를 임시 배열로 만들지 않는다. 기저 역행렬을 면 법선과 먼저 내적하여 행렬 계수에 대입한다. |
| R3:SU-027 | 식 (5.20)의 역기저 계수 | swantech PDF 130쪽 / 인쇄 122쪽, (5.20): $\vec c^1=C^{-1}(c_{(2)}^2,-c_{(2)}^1)$; $\vec c^2=C^{-1}(-c_{(1)}^2,c_{(1)}^1)$. | `src/swancom1.ftn:11080` `FACT = -DEPF/JAC`; `src/swancom1.ftn:11088` `CONTRB = FACT*(JCTA(INDX,1,1,1)*JCTA(INDX,1,2,1)+`. | F 표기 차이 | 문서의 $c_{(2)}$는 코드의 횡방향 평균 기저의 4배다. 이에 따라 $C$도 4배다. $\vec c^1$은 같고 $\vec c^2$에는 1/4가 남는다. 11090–11093행이 그 1/4를 적용한다. |
| R3:SU-028 | 식 (5.21)의 행렬식 배율 | swantech PDF 130쪽 / 인쇄 122쪽, (5.21): $C=c_{(2)}^2c_{(1)}^1-c_{(1)}^2c_{(2)}^1$. | `src/swancom1.ftn:11077–11078` `JAC = JCTA(INDX,1,1,1)*JCTA(INDX,1,2,2) -` / `JCTA(INDX,1,1,2)*JCTA(INDX,1,2,1)`. | F 표기 차이 | SU-027의 기저 정규화를 대입하면 $C=4\,JAC$다. 같은 연립식의 행을 일정 배율로 나눈 결과다. |
| R3:SU-029 | 식 (5.22)의 기저 평균 | swantech PDF 130쪽 / 인쇄 122쪽, (5.22): $\vec c_{(1)}=a_{(1)}\big\vert_{(1,0)}$, $\vec c_{(2)}=\vec a_{(2)}\big\vert_{(0,-1)}+\vec a_{(2)}\big\vert_{(0,1)}+\vec a_{(2)}\big\vert_{(2,-1)}+\vec a_{(2)}\big\vert_{(2,1)}$. | `src/swancom1.ftn:10720–10723` `JCTA(INDX,1,1,1) = 0.25*( YCGRID(IX+1,IY+1) +` / `YCGRID(IX  ,IY+1) -` / `YCGRID(IX+1,IY-1) -` / `YCGRID(IX  ,IY-1) )`. | F 표기 차이 | 인접 네 공변 기저의 합을 평균으로 저장한다. SU-027의 1/4와 함께 사용하면 최종 기울기가 같다. [10-13 전수 검증 정정] |
| R3:SU-030 | 식 (5.23)의 반 셀 유량 | swantech PDF 131쪽 / 인쇄 123쪽, (5.23): $\int_{\Omega_\xi}\partial_{\xi^\alpha}(\sqrt g\vec a^{(\alpha)}\cdot(k\nabla\zeta+\vec F)d\Omega_\xi\simeq\tfrac12\left.\sqrt g\vec a^{(1)}\cdot(k\nabla\zeta+\vec F)\right\vert_{(-1,0)}^{(1,0)}+\left.\sqrt g\vec a^{(2)}\cdot(k\nabla\zeta+\vec F)\right\vert_{(0,0)}^{(0,1)}$. 첫 적분의 바깥 닫는 괄호 누락을 원문대로 둔다. | `src/swancom1.ftn:10878` `RHS(INDX) = RHS(INDX) - JCTA(INDX,2,2,1)`; `src/swancom1.ftn:11218` `DEPF = DEPTH(INDX)+DEPTH(INDXU)`. | F 표기 차이 | 코드는 반 셀 방정식 전체를 2배 한다. 접선 면은 내부와 같은 계수다. 안쪽 법선 면은 내부의 2배다. 경계 면 유량은 0이다. 원문의 첫 적분에는 바깥 닫는 괄호가 빠져 있지만, 이 조판 누락은 반 셀 계수의 대응을 바꾸지 않는다. |
| R3:SU-031 | 식 (5.24) 첫 줄의 좌표 차 | swantech PDF 131쪽 / 인쇄 123쪽, (5.24) 첫 줄: $(\vec x_{(2,0)}-\vec x_{(1,0)})\cdot\nabla\zeta\big\vert_{(1,0)}=\zeta_{(2,0)}-\zeta_{(0,0)}$. | `src/swancom1.ftn:10766` `JCTA(INDX,1,2,2) = XCGRID(IX+1,IY) - XCGRID(IX  ,IY)`. | B 문서 오기 | 좌변 길이는 반 격자인데 우변은 한 격자의 수위 차다. 첫 줄의 두 번째 좌표는 $(0,0)$이어야 (5.16) 및 코드와 일치한다. |
| R3:SU-032 | 식 (5.24) 둘째 줄의 한쪽 차분 | swantech PDF 131쪽 / 인쇄 123쪽, (5.24) 둘째 줄: $((x_{(2,2)}-x_{(2,0)})+(\vec x_{(0,2)}-\vec x_{(0,0)}))\cdot\nabla\zeta\big\vert_{(1,0)}=(\zeta_{(0,2)}-\zeta_{(0,0)})+(\zeta_{(2,2)}-\zeta_{(2,0)})$. | `src/swancom1.ftn:11237` `AMAT(INDX,5) = AMAT(INDX,5) + 2.*AMAT(INDX,2)`; `src/swancom1.ftn:11238` `AMAT(INDX,7) = AMAT(INDX,7) - AMAT(INDX,2)`; `src/swancom1.ftn:11239` `AMAT(INDX,2) = 0.`. | F 표기 차이 | 가상점 값을 $\zeta_{ghost}=2\zeta_{boundary}-\zeta_{inside}$로 소거하면 같은 한쪽 차분이 된다. PDF에서 첫 좌표 차의 두 $x$에는 벡터 화살표가 생략됐지만 좌표 차의 의미는 정해진다. [10-13 전수 검증 정정] |
| R3:SU-033 | 마름점의 최종 행 | swantech PDF 131쪽 / 인쇄 123쪽, 원문: “the corresponding row of the matrix, as well as the right hand side element completely equal to zero.” | `src/swancom1.ftn:11160` `AMAT(INDX,:) = 0.0`; `src/swancom1.ftn:11161` `AMAT(INDX,1) = 1.0`; `src/swancom1.ftn:11162` `RHS (INDX  ) = 0.0`. 웹 `online_doc/swantech/node72.html:51–53`과 `node75.html:97–98`의 상반된 설명. | B 문서 오기 | 최종 행의 대각은 1이다. swantech PDF 133쪽 / 인쇄 125쪽의 “except on the main diagonal where the value 1 is substituted”는 코드와 같다. B 판정은 PDF 131의 최종 행을 “completely equal to zero”로 적은 문장에 한정한다. 매뉴얼 전체가 대각 1 처리를 누락한 것은 아니다. |
| R3:SU-035 | 내부 마름점의 횡방향 기울기 | swantech PDF 132쪽 / 인쇄 124쪽, 원문: “one sided differences are applied for those formulas involving $\zeta_{(2,0)}$”; “we make $\nabla\zeta$ for point 2 zero.” | `src/swancom1.ftn:11090–11093`은 주변 네 점에 `0.25*CONTRB`를 배분한다. 11075의 조건은 면 양 끝만 검사한다. 10720–10727의 기저 계산은 이 네 점의 수심을 검사하지 않는다. swantech PDF 132 “This process is applied for all transitions from wet to dry points.”; `src/swancom1.ftn:11073–11093,11167–11245`. | B 문서 오기 | 내부 젖은 면의 횡방향 기울기는 주변 마른 점을 발견해 한쪽 차분으로 바뀌지 않는다. 면 양 끝이 젖어 있고 기저 내적이 0이 아닌 곡선 격자에서는 마른 횡방향 이웃에 곱하는 계수가 남을 수 있다. `11090–11093`행은 그 이웃의 수심을 검사하지 않는다. `11237–11245`행의 한쪽 차분 소거는 외곽 경계 분기다. B는 swantech PDF 132가 이 처리를 모든 습윤·건조 전환에 적용한다고 한 설명에 한정한다. |
| R3:SU-037 | 저장 벡터의 차원 | swantech PDF 133쪽 / 인쇄 125쪽, 번호 없음: 벡터 차원 $MXC\times MYC$; $NWKARR=9$. | `src/swancom1.ftn:10577` `REAL    AMAT(MCGRD,9), JCTA(MCGRD,2,2,2), RHS(MCGRD)`; `src/swancom1.ftn:11853` `INDX = KGRPNT(IX  ,IY  )`; 11863–11870은 여덟 비대각 계수의 이웃값을 읽는다. `src/swanpre1.ftn:5123–5169`의 주소 설정. | B 문서 오기 | 실제 저장 인덱스는 `KGRPNT`로 연결하는 `MCGRD`다. `SWDIM`은 좌표나 수심이 제외값인 점의 주소를 1로 두고 유효점에 별도 주소를 부여한다. 수심 때문에 현재 마른 점이 모두 주소 1을 공유한다고 일반화할 수 없다. 9개 계수 저장은 문서와 같다. swantech 5.2.2의 벡터 차원이 항상 $MXC\times MYC$라는 설명은 코드의 저장 구조와 다르다. |
| R3:SU-038 | 직접 소거의 메모리 주장 | swantech PDF 133–134쪽 / 인쇄 125–126쪽, 번호 없음: Gauss 소거 저장량 $2\times MXC+2$ 벡터; 반복법 메모리가 이산화보다 작다는 주장. | `src/swancom1.ftn:11840` `10 IF ( ICONV.EQ.0 .AND. IT.LT.MAXIT ) THEN`. | H 코드 대조 대상 아님 | 저장량 비교는 이산 행렬의 대역폭과 직접 소거법의 fill-in에 관한 설명이다. `SETUP2D`는 `IF ( ICONV.EQ.0 .AND. IT.LT.MAXIT ) THEN`에서 반복법을 수행한다. 직접 소거법을 선택하는 분기로 읽지 않는다. |
| R3:SU-041 | 발산 없는 힘이라는 설명 | swantech PDF 134쪽 / 인쇄 126쪽, 원문: “the Poisson equation of the divergence-free force field”. | `src/swancom1.ftn:10825` `RHS(INDX) = RHS(INDX) - 0.5*JCTA(INDX,1,1,1)`. | B 문서 오기 | 우변은 힘의 발산이다. 발산이 0인 성분은 이 우변에 기여하지 않는다. PDF 127의 “setup is mainly due to the rotation-free part”와도 모순된다. |
| R3:SU-042 | 내부 행렬의 대칭성 | swantech PDF 133쪽 / 인쇄 125쪽, 번호 없음: “The discrete operator is symmetric in the inner region. This means that $a_{i,j}=a_{j,i}$.” | `src/swancom1.ftn:11076` `DEPF = 0.5*(DEPTH(INDX)+DEPTH(INDXR))`; `src/swancom1.ftn:11093` `AMAT(INDX,9) = AMAT(INDX,9) + 0.25*CONTRB`; 11135의 같은 대입; 11111·11153의 `AMAT(INDX,2) = AMAT(INDX,2) - 0.25*CONTRB`. | B 문서 오기 | 해석: 완전히 젖은 내부에서 $x_{i,j}=i+s j$, $y_{i,j}=j$인 격자를 코드식에 대입한다. P의 오른쪽을 E, 위를 N, 오른쪽 위를 Q라 하면 $a_{PQ}=s(2d_P+d_E+d_N)/8$다. 반대 계수는 $a_{QP}=s(2d_Q+d_E+d_N)/8$다. 따라서 $s\ne0$이고 $d_P\ne d_Q$이면 같지 않다. 이는 실행 결과가 아니라 조립식의 대수적 반례다. 내부 대칭성을 일반 곡선 격자·변수 수심에 보편화한 설명은 맞지 않는다. `src/swancom1.ftn:10720–10727,10752–10753,10765–10766,10789–10796`의 기저벡터도 대입했다. 이 격자에서 두 면의 기저벡터는 $(1,-s)$와 $(0,1)$이다. 11858·11861·11863·11870행은 계수 2가 왼쪽 아래, 9가 오른쪽 위 이웃임을 확인한다. PDF 133 이미지의 내부 대칭 주장과 대조한 결과다. [10-13 전수 검증 정정] |
