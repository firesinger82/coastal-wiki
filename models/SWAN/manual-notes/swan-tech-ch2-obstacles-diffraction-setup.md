---
title: "SWAN swantech Ch 2.5 Obstacles + 2.5.4 Diffraction + 2.6 Wave-induced set-up verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §2.5 Modelling of obstacles (doc p.52-57, Eq 2.131-2.142) + §2.6 Wave-induced set-up (doc p.57-58, Eq 2.143-2.145). References: Booij 1993, Goda 1967, Seelig 1979, d'Angremond 1996, Van der Meer 2005, Holthuijsen et al. 2003, Dingemans 1987."
citation_status: verified
last_source_check: "2026-10-13 (recovery 대조 반영)"
verification_method: "swantech.pdf (v41.51) §2.5-2.6 직접 read via pdftotext (식 번호 context-verified) + website_markdown node25-30.md LaTeX alt-text. PDF 2.131-2.135는 HTML 2.171-2.175에 대응한다. PDF의 번호 없는 자유고 R/T 식은 HTML 2.176-2.177에 대응한다. PDF 2.136-2.145는 HTML 2.178-2.187에 대응한다. 2026-10-13 recovery 대조 보고서 R1–R8 반영" # [10-13 전수 검증 정정]
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 2.131-2.145 + 계수 verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md
  - models/SWAN/manual-notes/swan-quasi-coherent.md
  - models/SWAN/manual-notes/swan-documentation-stack.md
---

# swantech Ch 2.5 Obstacles + 2.5.4 Diffraction + 2.6 Set-up — verified verbatim

> swantech.pdf (v41.51) §2.5-2.6 직접 read. Sub-grid line obstacle (breakwater/dam) 의 transmission·reflection·freeboard·diffraction + wave-induced set-up. §2.7 Quasi-coherent 는 [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md) 별도.
>
> **식 번호 주의**: PDF (2.131)–(2.135)는 HTML (2.171)–(2.175)에 대응한다. PDF의 번호 없는 자유고 R/T 식은 HTML (2.176)–(2.177)에 대응한다. PDF (2.136)–(2.145)는 HTML (2.178)–(2.187)에 대응한다. 본 노트는 PDF 번호를 사용한다. 괄호에 HTML 번호를 병기한다. 근거: swantech PDF 61–66쪽 / 인쇄 53–58쪽; `online_doc/swantech/node26.html:67–249`, `node28.html:57–88`, `node29.html:73–247`, `node30.html:57–122`. [10-13 전수 검증 정정]

## 0. Obstacle 개념 (§2.5)

Sub-grid 접근 — obstacle 이 grid size 대비 narrow. (넓으면 bathymetric feature 로.) 3가지 영향:
- 통과/월파 시 파고 감소 (transmission)
- 반사 (reflection)
- 끝단 회절 (diffraction)

> 문서는 불규칙 short-crested 파에서 장애물 끝의 1–2파장 이내를 제외하면 회절 영향이 작아 보인다고 설명한다. 입사 방향 스펙트럼이 너무 좁지 않고 깊은 음영역의 파동장을 관심 대상으로 삼지 않을 때 장애물 주변 파를 합리적으로 표현할 수 있다고 설명한다. 수치 구현은 §3.12를 참조한다. 근거: swantech PDF 61쪽 / 인쇄 53쪽: `it seems that the effect of diffraction is small`, `unless one is interested in the wave field deep into the shadow zone`; [swan-documentation-stack](swan-documentation-stack.md). [10-13 전수 검증 정정]

## 1. Transmission (§2.5.1, Eq 2.131-2.135)

투과계수 $K_t$ = downwave Hs / upwave Hs ($0 \le K_t \le 1$). 2 식 선택.

### 1.1 Goda et al. (1967) — closed-surface dam 월파

$$K_t = \begin{cases} 1, & \frac{F}{H_i} < -\beta - \alpha \\ 0.5\left[1 - \sin\left(\frac{\pi}{2\alpha}\left(\frac{F}{H_i}+\beta\right)\right)\right], & -\beta-\alpha \le \frac{F}{H_i} \le \alpha-\beta \\ 0, & \frac{F}{H_i} > \alpha-\beta \end{cases} \quad \text{(2.131) [HTML 2.171]}$$

- $F = h - d$ = freeboard (dam crest level $h$ − mean water level $d$, 둘 다 reference 기준)
- $H_i$ = upwave 입사 (유의)파고
- $\alpha, \beta$ = dam 형상 의존 (Seelig 1979), **Table 2.1**:

| case | $\alpha$ | $\beta$ |
|---|---|---|
| vertical thin wall | 1.8 | 0.1 |
| caisson | 2.2 | 0.4 |
| dam with slope 1:3/2 | 2.6 | 0.15 |

> Wave flume 실험 기반 → 엄밀히는 normal incidence. 방향 무의존 가정, 주파수 불변(에너지 스케일만 변, 형상 불변), slope 1:0.7(55°)보다 완만해야 유효.

### 1.2 d'Angremond et al. (1996) — impermeable rough low-crested dam

$$K_t = -0.4\frac{F}{H_i} + 0.64\left(\frac{B_k}{H_i}\right)^{-0.31}(1 - e^{-0.5\xi_p}) \quad \text{(2.132) [HTML 2.172]}$$
- $B_k$ = crest width, $\xi_p \equiv \tan\alpha/\sqrt{H_i/L_{0p}}$ = breaker parameter, $L_{0p} = gT_p^2/2\pi$ (deep water 파장), $\alpha$ = breakwater slope
- 제약: $0.075 \le K_t \le 0.9$ **(2.133) [HTML 2.173]**

$B_k \ge 10H_i$ 일 때 (wide crest):
$$K_t = -0.35\frac{F}{H_i} + 0.51\left(\frac{B_k}{H_i}\right)^{-0.65}(1 - e^{-0.41\xi_p}) \quad \text{(2.134) [HTML 2.174]}$$
- 제약: $0.05 \le K_t \le -0.006\frac{B_k}{H_i} + 0.93$ **(2.135) [HTML 2.175]**

> (2.132)/(2.134)는 $B_k = 10H_i$ 에서 불연속. Van der Meer(2005) 실용: $B_k<8H_i$ → (2.132), $B_k>12H_i$ → (2.134), 사이는 선형보간.

## 2. Reflection (§2.5.2)

Quay/breakwater 반사. obstacle 성격(smooth surface vs rubble-mound)에 따라 reflected field 산란 정도 상이. SWAN 은 반사를 여러 방향 wave component 로 diffuse 가능. (식 없음 — 정성 서술.)

## 3. Freeboard-dependent reflection & transmission (§2.5.3, PDF 번호 없는 식)

Obstacle flooding 시 relative freeboard $F/H_s$ 함수로 변화. Fixed 계수를 $\tanh$ 로 스케일:

$$R = \left[1 + \tanh\left(\frac{2}{\gamma_R}\frac{F}{H_s}\right)\right]\frac{R_0}{2} \quad \text{(PDF 번호 없는 식) [HTML 2.176]}$$

$$T = \left[1 + \tanh\left(-\frac{2}{\gamma_T}\frac{F}{H_s}\right)\right]\frac{T_0}{2} \quad \text{(PDF 번호 없는 식) [HTML 2.177]}$$
- $R_0, T_0$ = fixed 반사/투과 계수, $\gamma_R, \gamma_T$ = relative freeboard 범위 (계수가 min↔max 사이 변하는 위치와 일치)

FREEBOARD QUAY의 고정 계수 경로에서 얕은 쪽에서 깊은 쪽으로 진행하면 반사 배율은 0이고 투과 파고비는 $\min(1,99999T_0)$다. 따라서 $T_0=0$이면 투과도 0이며, $0<T_0<1/99999$이면 완전 투과보다 작다. `src/swanpre1.ftn:1084–1089`는 0을 허용한다. swantech 2.5.3과 swanuse QUAY 절은 이 작은 투과계수 예외를 적지 않는다. 주파수 의존 계수 경로에는 이 식을 일반화하지 않는다. 근거: `src/swanser.ftn:3096` `IF ( DEP2(KCGRD(ILINK+1)).LT.DEP2(KCGRD(1)) ) THEN`; `src/swanser.ftn:3097` `FBT = 99999.`; `src/swanser.ftn:3098` `FBR = 0.`; `src/swanser.ftn:3113` `OBHKT = MIN(1.,FBT * COBST%TRCOEF(1))`. `src/swanser.ftn:3079,3095,3108–3114`의 `LFREE`, `LQUAY`, `ITRAS .EQ. 0` 분기.

## 4. Diffraction (§2.5.4, Eq 2.136-2.142)

Phase-decoupled refraction-diffraction 근사 (Holthuijsen et al. 2003) — 2D 스펙트럼 개별 component 의 directional turning rate. Mild-slope 식 기반, phase 정보 생략(quasi-homogeneous 가정). (inhomogeneous diffraction 통계는 §2.7 [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md).)

swantech PDF 64쪽 / 인쇄 56쪽은 무류인 가장 단순한 경우를 설명한다. 해석: 이 절의 $c_\sigma=0$은 시간에 따라 수심이 변하지 않는 경우로 읽는다. 여기서 정수심은 수심의 시간변화가 없다는 뜻이다. 근거: 같은 쪽의 `In a simplest case, we assume there are no currents.`; `src/swancom5.ftn:1543–1548`의 `CAST2` 분기. [10-13 전수 검증 보완]
$$c_{x,0} = \frac{\partial\omega}{\partial k}\cos\theta,\quad c_{y,0} = \frac{\partial\omega}{\partial k}\sin\theta,\quad c_{\theta,0} = -\frac{1}{k}\frac{\partial\omega}{\partial h}\frac{\partial h}{\partial n} \quad \text{(2.136) [HTML 2.178]}$$
해석: $\partial\omega/\partial k=c_g$다. $n$을 파선의 왼쪽 법선으로 잡으면 $\partial h/\partial n=-\sin\theta h_x+\cos\theta h_y$다. 이 정의를 원문의 음수에 대입하면 코드의 `ESIN(ID)*DHDX-ECOS(ID)*DHDY`와 같다. $\frac1k\omega_h=\sigma/\sinh(2kh)$다. 근거: `src/swancom5.ftn:1072` `CAX(ID,IS,IC) = CGO(IS,IC) * ECOS(ID)`; `src/swancom5.ftn:1073` `CAY(ID,IS,IC) = CGO(IS,IC) * ESIN(ID)`; `src/swancom5.ftn:1591` `CAD_TMP=COEF*(ESIN(ID)*DHDX-ECOS(ID)*DHDY)`.

이 문장은 회절 절의 “가장 단순한 경우”에 둔 가정이다. 코드는 `IF ( NSTATC.EQ.0 .OR. .NOT.DYNDEP) THEN`이면 `CAST2 = 0.`으로 둔다. 비정상 DYNDEP 계산에서는 무류여도 `CAST2 = ( DLOC1 - DEP1(KCG1) ) * RDTIM`과 `CAS(ID,IS,1)=CAST1*CAST2`를 계산한다. 이 절의 $c_\sigma=0$은 정수심 가정을 함께 가진다. 일반 전파식의 수심 시간변화 항이 누락된 것으로 분류하지 않는다. 근거: `src/swancom5.ftn:1543` `IF ( NSTATC.EQ.0 .OR. .NOT.DYNDEP) THEN`; `src/swancom5.ftn:1548` `CAST2 = ( DLOC1 - DEP1(KCG1) ) * RDTIM`; `src/swancom5.ftn:1603` `CAS(ID,IS,1)=CAST1*CAST2`. 웹 `online_doc/swantech/node29.html`의 가장 단순한 경우 문장; `src/swanpre1.ftn:913` `RDTIM = 1./DT`.

Eikonal:
$$K^2 = k^2(1+\delta) \quad \text{(2.137) [HTML 2.179]}$$

Diffraction parameter:
$$\delta = \frac{\nabla(cc_g\nabla\sqrt{E})}{cc_g\sqrt{E}} \quad \text{(2.138) [HTML 2.180]}$$
($E(x,y)$ = total energy $\sim H_s^2$)

인쇄식과 코드 대응식을 구분한다. 코드 대응식 분모는 $k^2cc_g\sqrt E$다. 무류라도 시간에 따라 수심이 변하면 $c_\sigma$가 0이 아닐 수 있다. 근거: swantech PDF 64쪽 / 인쇄 56쪽 (2.138); `src/SwanDiffPar.ftn90:350` `denom = k(ivert)*cg(ivert)*hs(ivert)`.

코드 대응식은 $\nabla(cc_g\nabla\sqrt E)/(k^2cc_g\sqrt E)$다.

Diffraction 보정 전파속도:
$$c_x = c_{x,0}\overline{\delta},\quad c_y = c_{y,0}\overline{\delta},\quad c_\theta = c_{\theta,0}\overline{\delta} - \frac{\partial\overline{\delta}}{\partial x}c_{y,0} + \frac{\partial\overline{\delta}}{\partial y}c_{x,0} \quad \text{(2.139) [HTML 2.181]}$$

근거: swantech PDF 64쪽 / 인쇄 56쪽 (2.139); `src/swancom5.ftn:1608–1610` `CAD(ID,IS,1) = DIFPARAM(KCG1)*CAD(ID,IS,1)` / `- DIFPARDX(KCG1)*CGO(IS,1)*ESIN(ID)` / `+ DIFPARDY(KCG1)*CGO(IS,1)*ECOS(ID)`.

$$\overline{\delta} = \sqrt{1+\delta} \quad \text{(2.140) [HTML 2.182]}$$

### Smoothing (수치 안정화)

초기 계산서 $\sim2\Delta x$ 진동이 $\delta$ gradient 교란 → convolution filter:
$$E_{i,j}^n = E_{i,j}^{n-1} - 0.2[E_{i-1,j}+E_{i,j-1}-4E_{i,j}+E_{i+1,j}+E_{i,j+1}]^{n-1} \quad \text{(2.141) [HTML 2.183]}$$
($n$ = convolution iteration)

원문 (2.141)은 대괄호 앞에 음수를 인쇄했다. 코드의 평활식은 양수다. 근거: `src/swancom5.ftn:5529–5530` `! Effectively, E(i,j) = (1-4*alpha) * E(i,j) +` / `! alpha * (E(i-1,j)+E(i+1,j)+E(i,j-1)+E(i,j+1))`; `src/swancom5.ftn:5737` `EN(IND) = EN(IND) - TMP*(ENTMP(IX,IY)-ENTMP(IX+1,IY))`. swanuse PDF 87 및 웹 `online_doc/swanuse/node28.html:3063–3125`.

인쇄 원문의 필터 폭은 다음과 같다. swantech PDF 65쪽 / 인쇄 57쪽 (2.142).
$$\varepsilon_x \approx \frac{1}{2}\sqrt{3n}\,\Delta x \quad \text{(2.142) [HTML 2.184]}$$
해석: 경계·장애물·마름점이 없는 균일 격자의 코드 필터에서 한 회의 x방향 분산은 $2\alpha\Delta x^2$다. $\alpha=0.2$이면 $\varepsilon_x=\sqrt{0.4n}\Delta x$다. 문서 계수는 $\sqrt{0.75n}$이다. 동일 필터의 표준편차가 아니다. 근거: `src/swancom5.ftn:5709` `TMP = PDIFFR(1)`; 5722–5723과 5737·5751·5765행의 네 이웃 교환.

6회는 계산 사례의 권고다. 생략 기본값은 0회다. swanuse DIFFRACTION 절도 `[smpar] = 0`, `[smnum] = 0`을 기본값으로 적는다. `src/ocpcre.ftn:436`은 `'STA'`를 “variable will get value of RSTA”로 정의한다. `misc/swan.edt:242`는 명령 형식만 적는다. 근거: `src/swanpre1.ftn:2116` `CALL INREAL ('SMPAR', PDIFFR(1), 'STA', 0.0)`; `src/swanpre1.ftn:2117` `CALL INREAL ('SMNUM', PDIFFR(2), 'STA', 0.)`; `src/swancom5.ftn:5685` `DO ISM = 1, INT(PDIFFR(2))`. 웹 `online_doc/swanuse/node28.html:3131–3154`.

평활은 회절 매개변수 $\delta$를 계산하는 에너지 배열에만 적용한다. 근거: swantech PDF 65쪽 / 인쇄 57쪽; `src/swancom5.ftn:5693` `ENTMP(IX-IX1+1,IY-IY1+1) = EN(KGRPNT(IX,IY))`.

### Diffraction 사용 금지 조건 (4 동시충족 시)

① obstacle/coastline 이 down-wave view 상당 부분 가림, ② 거리 짧음(수 파장 미만), ③ 반사가 coherent, ④ 반사계수 유의. → harbour·반사 breakwater 정면·cliff wall 부적합. 흡수/반사 해안(만·라군·피요르드) + 간헐 obstacle(barrier island·breakwater·headland)엔 적합.

## 5. Wave-induced set-up (§2.6, Eq 2.143-2.145)

### 5.1 1D

연직적분 momentum balance (wave force = radiation stress gradient vs hydrostatic pressure gradient; 해안 평행 성분은 wave-induced current 만 유발, set-up 무):

$$\frac{dS_{xx}}{dx} + \rho g H\frac{d\overline{\eta}}{dx} = 0 \quad \text{(2.143) [HTML 2.185]}$$
($d$ = total depth incl. set-up, $\eta$ = mean surface elevation incl. set-up)

$$S_{xx} = \rho g\int\left[n\cos^2\theta + n - \frac{1}{2}\right]E\,d\sigma d\theta \quad \text{(2.144) [HTML 2.186]}$$
(radiation stress tensor)

해석: $n=c_g/c$를 쓰면 $CK=\sigma n$이다. $ELOC=\sigma N=E$다. 남은 $\sigma$는 로그 격자 적분의 가중이다. 코드가 저장하는 복사응력은 $R_{ij}=S_{ij}/(\rho g)$이므로 $S_{xx}$ 식과 같다. 기존 보고서가 PDF (2.144)의 인용에 보탠 $S_{xy}$·$S_{yy}$ 식은 이 쪽 원문에 없으므로 제거한다. 근거: `src/swancom1.ftn:10237` `CK = CG(1) * K(1)`; `src/swancom1.ftn:10239` `ELOC = SIG(1) * AC2(ID,IS,INDX)`; `src/swancom1.ftn:10246` `RSXX = RSXX + (CK*SPCDIR(ID,4)+CK - SIG(1)/2.) * ELOC`; `src/swancom1.ftn:10247` `RSXY = RSXY + CK*SPCDIR(ID,5) * ELOC`; `src/swancom1.ftn:10248` `RSYY = RSYY + (CK*SPCDIR(ID,6)+CK - SIG(1)/2.) * ELOC`; `src/swancom1.ftn:10263` `SETPDA(INDX,3) = RSXX * DDIR * FRINTF`.

### 5.2 2D (Dingemans et al. 1987)

Wave-induced current 는 force 의 divergence-free 부분, set-up 은 rotation-free 부분 주도. Momentum balance 의 divergence 고려 + acceleration divergence 무시:

$$\frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} - \frac{\partial}{\partial x}\left(\rho g H\frac{\partial\overline{\eta}}{\partial x}\right) - \frac{\partial}{\partial y}\left(\rho g H\frac{\partial\overline{\eta}}{\partial y}\right) = 0 \quad \text{(2.145) [HTML 2.187]}$$

> **Open coast 한정** (외부 무제한 급수 — 연안·하구). Closed basin(호수)엔 부적합.

원문은 $\frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}-\frac{\partial}{\partial x}(\rho g H\frac{\partial\bar\eta}{\partial x})-\frac{\partial}{\partial y}(\rho g H\frac{\partial\bar\eta}{\partial y})=0$ (2.145)다. 코드와 비교할 때 물리 힘을 $\rho g$로 나눈 정규화와 수심 기호를 명시한다. 근거: swantech PDF 66쪽 / 인쇄 58쪽 (2.145); `src/swancom1.ftn:10263` `SETPDA(INDX,3) = RSXX * DDIR * FRINTF`.

## 6. SWAN 옵션 매핑 (User cmd)

| Tech 식 (PDF) | User cmd | 비고 |
|---|---|---|
| 2.131 Goda transmission | `OBSTACLE TRANSM ... DAM` (Goda) | Seelig 1979 α,β |
| 2.132-2.135 d'Angremond | `OBSTACLE DAM ...` | low-crested, Van der Meer 2005 보간 |
| PDF 번호 없는 freeboard R/T | `OBSTACLE ... FREEBOARD [hgt] [gammat] [gammar] QUAY` | FREEBOARD의 첫 인수는 HGT다. swantech PDF 63쪽 / 인쇄 55쪽; `src/swanpre1.ftn:1214` `CALL INREAL ('HGT'   , HGT , 'REQ', 0.)` |
| reflection | `OBSTACLE REFL [reflc] [RDIFF]` | diffuse 반사 |
| 2.136-2.142 diffraction | `DIFFRACtion [idiffr] [smpar] [smnum] [cgmod]` | Holthuijsen 2003, $n$=smnum |
| 2.143-2.145 set-up | `SETUP` | open coast only |

## 7. 한계

- 보정식은 $c_\theta=c_{\theta,0}\bar\delta-\bar\delta_xc_{y,0}+\bar\delta_yc_{x,0}$다. 근거: swantech PDF 64쪽 / 인쇄 56쪽 (2.139); `src/swancom5.ftn:1608–1610`.
- §2.5.2 Reflection 은 식 없는 정성 서술 — 수치 구현(diffuse 각도 분배)은 §3.12 / source-analysis 별도.
- §2.4 ambient current (Longuet-Higgins-Stewart, $N=E/\sigma$ 보존)은 [swan-tech-ch2-vegetation-ice-bragg-gen12](swan-tech-ch2-vegetation-ice-bragg-gen12.md) §2.4 brief 참조.
- §2.7 Quasi-coherent → [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md).

## 8. 연결

- [swan-tech-ch2-governing-equations](swan-tech-ch2-governing-equations.md) — §2.1-2.2 (action balance, 전파속도 $c_x,c_y,c_\theta,c_\sigma$ 정의)
- [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md) — §2.7 QC (inhomogeneous diffraction 통계)
- [swan-documentation-stack](swan-documentation-stack.md) — 4 PDFs TOC, §3.12 numerical obstacle
- [swan-tech-ch2-vegetation-ice-bragg-gen12](swan-tech-ch2-vegetation-ice-bragg-gen12.md) — §2.3.5-8 + §2.4 ambient current

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R3:NT-006 | 장애물·회절·set-up 식 번호 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:69` `Eq 2.136-2.137`; 80 `Eq 2.138-2.144`; 114 `Eq 2.145-2.147`. | — | B 문서 오기 | PDF 자유고 R·T 식은 번호 없는 식이다. 회절 식은 (2.136)–(2.142)다. set-up 식은 (2.143)–(2.145)다. 본문·표·교차 참조에서 같은 번호를 사용한다. HTML 식 번호는 별도 표시한다. |
| R3:NT-007 | 방향 전파속도의 전사 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:85`의 `-\frac{1}{k}`; 96의 `+ \cdots`와 `\frac{\partial\overline{\delta}}{\partial x}c_{y,0} - \frac{\partial\overline{\delta}}{\partial y}c_{x,0}`. swantech PDF 64쪽 / 인쇄 56쪽 (2.136)은 $c_{\theta,0}=-k^{-1}\omega_hh_n$이다. `online_doc/swantech/node29.html:75–77`도 음수다. | `src/swancom5.ftn:1082` `CAX(ID,IS,IC) = CAX(ID,IS,IC)*DIFPARAM(KCGRD(IC))`; 1083은 `CAY`의 같은 곱셈이다. 1608–1610 `CAD(ID,IS,1) = DIFPARAM(KCG1)*CAD(ID,IS,1)` / `- DIFPARDX(KCG1)*CGO(IS,1)*ESIN(ID)` / `+ DIFPARDY(KCG1)*CGO(IS,1)*ECOS(ID)`. | B 문서 오기 | 보정식은 $c_\theta=c_{\theta,0}\bar\delta-\bar\delta_xc_{y,0}+\bar\delta_yc_{x,0}$다. 기본 식의 음수 판독은 R3:OQ-017의 최종 정정과 같다. [10-13 전수 검증 보완] |
| R3:NT-008 | 회절 분모와 무류 설명 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:92` `\frac{\nabla(cc_g\nabla\sqrt{E})}{cc_g\sqrt{E}}`; 84 `무전류 ($c_\sigma=0$)`. | `src/swancom5.ftn:5823–5825` `TMP = 0.5*(CG(INDL)/K(INDL)+CG(IND)/K(IND)) *` / `DYLOC * (EN(IND)-EN(INDL)) / DXLOC` / `EAD = DXLOC * DYLOC * EN(IND)*CG(IND)*K(IND)`; `src/swancom5.ftn:5885` `TMP = 2.*LAPE(IND)/DENOM(IND)`. `src/SwanDiffPar.ftn90:68` `! k^2 pH`. `src/SwanDiffPar.ftn90:319–320,350–353`의 실행문. 웹 `online_doc/swantech/node29.html`도 분모에 $k^2$를 적지 않는다.<br>`src/swancom5.ftn:1543` `IF ( NSTATC.EQ.0 .OR. .NOT.DYNDEP) THEN`; `src/swancom5.ftn:1548` `CAST2 = ( DLOC1 - DEP1(KCG1) ) * RDTIM`; `src/swancom5.ftn:1603` `CAS(ID,IS,1)=CAST1*CAST2`. 웹 `online_doc/swantech/node29.html`의 가장 단순한 경우 문장; `src/swanpre1.ftn:913` `RDTIM = 1./DT`. | B 문서 오기 | 인쇄식과 코드 대응식을 구분한다. 코드 대응식 분모는 $k^2cc_g\sqrt E$다. 무류라도 시간에 따라 수심이 변하면 $c_\sigma$가 0이 아닐 수 있다. |
| R3:NT-009 | 평활 부호와 표준편차 전사 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:103` `- 0.2[`; 107 `\frac{1}{2}\sqrt{3n}`. | `src/swancom5.ftn:5529–5530` `! Effectively, E(i,j) = (1-4*alpha) * E(i,j) +` / `! alpha * (E(i-1,j)+E(i+1,j)+E(i,j-1)+E(i,j+1))`; `src/swancom5.ftn:5737` `EN(IND) = EN(IND) - TMP*(ENTMP(IX,IY)-ENTMP(IX+1,IY))`. swanuse PDF 87 및 웹 `online_doc/swanuse/node28.html:3063–3125`.<br>`src/swancom5.ftn:5709` `TMP = PDIFFR(1)`; 5722–5723과 5737·5751·5765행의 네 이웃 교환. | B 문서 오기 | 원문 (2.141)은 대괄호 앞에 음수를 인쇄했다. 코드의 평활식은 양수다. 해석: 균일 무장애물 격자에서 코드 필터의 표준편차는 $\sqrt{2\alpha n}\Delta x$다. $\alpha=0.2$이면 $\sqrt{0.4n}\Delta x$다. |
| R3:NT-010 | 2D set-up 식의 단위·번호 | 현재 노트의 수정 전 원문: `manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:130` `\rho g H`와 `\text{(2.147) [HTML 2.187]}`. | `src/swancom1.ftn:10392` `-(RSXXI*DIX + RSXXJ*DJX + RSXYI*DIY + RSXYJ*DJY)`; `src/swancom1.ftn:10394` `-(RSXYI*DIX + RSXYJ*DJX + RSYYI*DIY + RSYYJ*DJY)`; `src/swancom1.ftn:11080` `FACT = -DEPF/JAC`; `src/swancom1.ftn:10825` `RHS(INDX) = RHS(INDX) - 0.5*JCTA(INDX,1,1,1)`. | F 표기 차이 | 원문은 $\frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}-\frac{\partial}{\partial x}(\rho g H\frac{\partial\bar\eta}{\partial x})-\frac{\partial}{\partial y}(\rho g H\frac{\partial\bar\eta}{\partial y})=0$ (2.145)다. 코드와 비교할 때 물리 힘을 $\rho g$로 나눈 정규화와 수심 기호를 명시한다. $\rho g H$ 자체를 오기로 고치지 않는다. |
| R3:OQ-003 | 형상별 α·β와 입력 생략값 | swantech PDF 62쪽 / 인쇄 54쪽, 표 2.1: “vertical thin wall” $(\alpha,\beta)=(1.8,0.1)$; “caisson” $(2.2,0.4)$; “dam with slope 1:3/2” $(2.6,0.15)$. | `src/swanpre1.ftn:1104` `CALL INREAL ('ALPHA', OGAM, 'STA', 2.6 )`; `src/swanpre1.ftn:1105` `CALL INREAL ('BETA' , OBET, 'STA', 0.15)`. | H 코드 대조 대상 아님 | 표는 형상별 권고값이다. 코드는 형상을 자동 판별하지 않는다. 입력 생략값은 표의 세 번째 행이다. 다른 두 행은 사용자가 지정할 값이다. |
| R3:OQ-006 | 심해 파장의 고정 중력 계수 | swantech PDF 62쪽 / 인쇄 54쪽, 번호 없음: $L_{0p}=gT_p^2/2\pi$. | `src/swanser.ftn:3166` `TP=2.*PI/SPCSIG(ISIGM)`; `src/swanser.ftn:3169` `L0P = MAX(1.E-8,1.5613*TP*TP)`; `src/swanmain.ftn:1006` `GRAV = 9.81`. swanuse PDF 36의 `[grav]` 설명; 웹 `online_doc/swanuse/node23.html`의 SET 절. | C 문서 누락 | 코드는 $9.81/(2\pi)\simeq1.56130999$를 1.5613으로 고정한다. swanuse SET 절은 `[grav]` 변경을 허용한다. `src/swanpre1.ftn:2175`도 `CALL INREAL ('GRAV',   GRAV,   'UNC', 0.)`로 읽는다. 이 값은 `L0P` 계산에 쓰이지 않는다. 기본 중력에서는 반올림 근사다. swantech 2.5.1과 swanuse의 SET·OBSTACLE 절은 이 고정 계수 예외를 적지 않는다. |
| R3:OQ-009 | 넓은 마루 투과 한계의 우선순위 | swantech PDF 62쪽 / 인쇄 54쪽, (2.135): $0.05\le K_t\le-0.006B_k/H_i+0.93$. | `src/swanser.ftn:3185` `IF (OBHKT.GT.0.93-0.006*BVH) OBHKT = 0.93-0.006*BVH`; `src/swanser.ftn:3186` `IF (OBHKT.LT.0.05 ) OBHKT = 0.05`. 웹 `online_doc/swantech/node26.html:242`도 같은 두 제한을 적는다. | C 문서 누락 | $B_k/H_i\le146\frac23$이면 코드의 결과가 문서의 두 부등식을 만족한다. 그보다 크면 (2.135)의 상한이 하한보다 작아진다. 코드는 상한을 적용한 뒤 하한을 적용하여 최종적으로 0.05를 택한다. swantech 2.5.1과 swanuse OBSTACLE 절은 충돌 때의 하한 우선순위를 적지 않는다. [10-13 전수 검증 정정] |
| R3:OQ-013 | 자유고 증가와 투과계수의 방향 | swantech PDF 63쪽 / 인쇄 55쪽, 원문: “transmission increases with increasing freeboard.” | `src/swanser.ftn:3088` `FBT = 0.5 * ( 1. - TANH(2.*FVH/GAMT) )`; `src/swanser.ftn:3130` `OBHKT = 0.5*(1.0-SIN(PI*(FVH+OBET)/(2.0*OGAM)))`. | B 문서 오기 | 양의 $\gamma_T$에서 자유고가 커지면 투과계수는 감소한다. swantech PDF 63의 투과식과 코드가 같은 방향이다. 같은 쪽의 “transmission increases with increasing freeboard”는 반대 방향을 적었다. 그림 2.4의 반사·투과 범례도 식과 뒤바뀌어 있으므로 그림을 식과 일치하는 근거로 쓰지 않는다. |
| R3:OQ-014 | QUAY의 완전 투과 조건 | swantech PDF 64쪽 / 인쇄 56쪽, QUAY의 번호 없는 조건: “When waves travel from the shallower part to the deeper part”에는 $R=0$, $T=1$. | `src/swanser.ftn:3096` `IF ( DEP2(KCGRD(ILINK+1)).LT.DEP2(KCGRD(1)) ) THEN`; `src/swanser.ftn:3097` `FBT = 99999.`; `src/swanser.ftn:3098` `FBR = 0.`; `src/swanser.ftn:3113` `OBHKT = MIN(1.,FBT * COBST%TRCOEF(1))`. `src/swanser.ftn:3079,3095,3108–3114`의 `LFREE`, `LQUAY`, `ITRAS .EQ. 0` 분기. | C 문서 누락 | FREEBOARD QUAY의 고정 계수 경로에서 얕은 쪽에서 깊은 쪽으로 진행하면 반사 배율은 0이고 투과 파고비는 $\min(1,99999T_0)$다. 따라서 $T_0=0$이면 투과도 0이며, $0<T_0<1/99999$이면 완전 투과보다 작다. `src/swanpre1.ftn:1084–1089`는 0을 허용한다. swantech 2.5.3과 swanuse QUAY 절은 이 작은 투과계수 예외를 적지 않는다. 주파수 의존 계수 경로에는 이 식을 일반화하지 않는다. |
| R3:OQ-015 | 자유고 그림 예와 기본값 | swantech PDF 63쪽 / 인쇄 55쪽, 그림 예: $R_0=0.6$, $T_0=0.9$, $H_s=2\ \mathrm m$. 원문: “In this example”. | `src/swanpre1.ftn:1157` `CALL INREAL ('REFLC', REF0, 'STA', 1.)`; `src/swanpre1.ftn:1215` `CALL INREAL ('GAMMAT', GAMT, 'STA', 1.)`; `src/swanpre1.ftn:1216` `CALL INREAL ('GAMMAR', GAMR, 'STA', 1.)`; `src/swanpre1.ftn:1113` `TRCF = 0.`. | H 코드 대조 대상 아님 | 그림 값은 기본값이 아니다. 반사를 켰을 때 생략 반사계수는 1이다. FREEBOARD의 생략 $\gamma_T$, $\gamma_R$는 각각 1이다. 투과 옵션을 생략하면 0이다. |
| R3:OQ-017 | 기본 방향 전파속도의 법선 | swantech PDF 64쪽 / 인쇄 56쪽, (2.136): $c_{x,0}=\frac{\partial\omega}{\partial k}\cos\theta$, $c_{y,0}=\frac{\partial\omega}{\partial k}\sin\theta$, $c_{\theta,0}=-\frac1k\frac{\partial\omega}{\partial h}\frac{\partial h}{\partial n}$. PDF와 웹 node29의 마지막 식은 모두 음수다. | `src/swancom5.ftn:1072` `CAX(ID,IS,IC) = CGO(IS,IC) * ECOS(ID)`; `src/swancom5.ftn:1073` `CAY(ID,IS,IC) = CGO(IS,IC) * ESIN(ID)`; `src/swancom5.ftn:1591` `CAD_TMP=COEF*(ESIN(ID)*DHDX-ECOS(ID)*DHDY)`. | F 표기 차이 | 해석: $\partial\omega/\partial k=c_g$다. $n$을 파선의 왼쪽 법선으로 잡으면 $\partial h/\partial n=-\sin\theta h_x+\cos\theta h_y$다. 이 정의를 원문의 음수에 대입하면 코드의 `ESIN(ID)*DHDX-ECOS(ID)*DHDY`와 같다. $\frac1k\omega_h=\sigma/\sinh(2kh)$다. 기존 보고서의 “PDF는 양수” 판독을 정정한다. |
| R3:OQ-018 | 무류와 주파수 이동 | swantech PDF 64쪽 / 인쇄 56쪽, 번호 없음: “In a simplest case, we assume there are no currents. This means that $c_\sigma=0$.” | `src/swancom5.ftn:1543` `IF ( NSTATC.EQ.0 .OR. .NOT.DYNDEP) THEN`; `src/swancom5.ftn:1548` `CAST2 = ( DLOC1 - DEP1(KCG1) ) * RDTIM`; `src/swancom5.ftn:1603` `CAS(ID,IS,1)=CAST1*CAST2`. 웹 `online_doc/swantech/node29.html`의 가장 단순한 경우 문장; `src/swanpre1.ftn:913` `RDTIM = 1./DT`. | H 코드 대조 대상 아님 | 이 문장은 회절 절의 “가장 단순한 경우”에 둔 가정이다. 코드는 `IF ( NSTATC.EQ.0 .OR. .NOT.DYNDEP) THEN`이면 `CAST2 = 0.`으로 둔다. 비정상 DYNDEP 계산에서는 무류여도 `CAST2 = ( DLOC1 - DEP1(KCG1) ) * RDTIM`과 `CAS(ID,IS,1)=CAST1*CAST2`를 계산한다. 이 절의 $c_\sigma=0$은 정수심 가정을 함께 가진다. 일반 전파식의 수심 시간변화 항이 누락된 것으로 분류하지 않는다. |
| R3:OQ-019 | 유효 파수와 전파속도 배율 | swantech PDF 64쪽 / 인쇄 56쪽, (2.137): $K^2=k^2(1+\delta)$. | `src/swancom5.ftn:5892` `DIFPARAM(IND) = SQRT(1.+TMP)`; `src/SwanDiffPar.ftn90:62` `! K = k (1+delta)^0.5`. | F 표기 차이 | $K/k=\sqrt{1+\delta}$를 사용한다. 코드는 $K$ 배열을 별도로 갱신하지 않고 전파속도에 이 비를 적용한다. `src/swancom5.ftn:1082–1083`은 지리 전파속도에 곱하고 1608–1610행은 방향 전파속도를 보정한다. |
| R3:OQ-020 | 회절 매개변수의 분모 | swantech PDF 64쪽 / 인쇄 56쪽, (2.138): $\delta=\frac{\nabla(cc_g\nabla\sqrt E)}{cc_g\sqrt E}$. | `src/swancom5.ftn:5823–5825` `TMP = 0.5*(CG(INDL)/K(INDL)+CG(IND)/K(IND)) *` / `DYLOC * (EN(IND)-EN(INDL)) / DXLOC` / `EAD = DXLOC * DYLOC * EN(IND)*CG(IND)*K(IND)`; `src/swancom5.ftn:5885` `TMP = 2.*LAPE(IND)/DENOM(IND)`. `src/SwanDiffPar.ftn90:68` `! k^2 pH`. `src/SwanDiffPar.ftn90:319–320,350–353`의 실행문. 웹 `online_doc/swantech/node29.html`도 분모에 $k^2$를 적지 않는다. | B 문서 오기 | swantech PDF (2.138)의 분모에는 $k^2$가 없다. 인쇄식의 차원은 $\mathrm{m}^{-2}$지만 (2.137)의 $\delta$는 무차원이어야 한다. 일정 $\sigma$에서 $c=\sigma/k$를 대입하면 코드의 분자 가중 $c_g/k$와 분모 $c_gk\sqrt E$는 $\nabla(cc_g\nabla\sqrt E)/(k^2cc_g\sqrt E)$에 대응한다. 비구조 코드도 `denom = k(ivert)*cg(ivert)*hs(ivert)`와 `delta = (dgxdx + dgydy)/denom`을 사용한다. |
| R3:OQ-022 | δ가 −1보다 작은 경우 | swantech PDF 64쪽 / 인쇄 56쪽, (2.140): $\bar\delta=\sqrt{1+\delta}$. | `src/swancom5.ftn:5889` `IF (TMP.LT.-1.) THEN`; `src/swancom5.ftn:5890` `DIFPARAM(IND) = 0.`; `src/swancom5.ftn:5892` `DIFPARAM(IND) = SQRT(1.+TMP)`. | C 문서 누락 | 구조 격자의 `DIFPAR`는 $\delta\ge-1$에서 문서와 같다. $\delta<-1$이면 `DIFPARAM(IND) = 0.`으로 제한한다. swantech 회절 절과 swanuse DIFFRACTION 절은 이 제한을 적지 않는다. 이 판정은 인용한 구조 격자 분기에 한정한다. |
| R3:OQ-023 | 회절 평활식의 부호 | swantech PDF 65쪽 / 인쇄 57쪽, (2.141): $E^n_{i,j}=E^{n-1}_{i,j}-0.2[E_{i-1,j}+E_{i,j-1}-4E_{i,j}+E_{i+1,j}+E_{i,j+1}]^{n-1}$. | `src/swancom5.ftn:5529–5530` `! Effectively, E(i,j) = (1-4*alpha) * E(i,j) +` / `! alpha * (E(i-1,j)+E(i+1,j)+E(i,j-1)+E(i,j+1))`; `src/swancom5.ftn:5737` `EN(IND) = EN(IND) - TMP*(ENTMP(IX,IY)-ENTMP(IX+1,IY))`. swanuse PDF 87 및 웹 `online_doc/swanuse/node28.html:3063–3125`. | B 문서 오기 | 코드의 각 이웃 기여는 $+\alpha(E_{neighbor}-E_{center})$다. swantech (2.141)의 대괄호 앞 음수는 반확산을 만든다. swanuse DIFFRACTION의 모 필터 식도 음수를 적지만, 같은 절의 “exchange [smpar] times the energy with their neighbours”는 코드의 평활 동작과 같다. 코드 주석과 실행문은 평활 부호로 일치한다. |
| R3:OQ-024 | 평활 필터의 표준편차 | swantech PDF 65쪽 / 인쇄 57쪽, (2.142): $\varepsilon_x\approx\frac12\sqrt{3n}\Delta x$. | `src/swancom5.ftn:5709` `TMP = PDIFFR(1)`; 5722–5723과 5737·5751·5765행의 네 이웃 교환. | B 문서 오기 | 해석: 경계·장애물·마름점이 없는 균일 격자의 코드 필터에서 한 회의 x방향 분산은 $2\alpha\Delta x^2$다. $\alpha=0.2$이면 $\varepsilon_x=\sqrt{0.4n}\Delta x$다. 문서 계수는 $\sqrt{0.75n}$이다. 동일 필터의 표준편차가 아니다. |
| R3:OQ-025 | 평활 6회 권고 | swantech PDF 65쪽 / 인쇄 57쪽, 번호 없음: “$n=6$ is found to be an optimum value”; $\varepsilon_x\approx2\Delta x$; y방향에도 동일 적용. | `src/swanpre1.ftn:2116` `CALL INREAL ('SMPAR', PDIFFR(1), 'STA', 0.0)`; `src/swanpre1.ftn:2117` `CALL INREAL ('SMNUM', PDIFFR(2), 'STA', 0.)`; `src/swancom5.ftn:5685` `DO ISM = 1, INT(PDIFFR(2))`. 웹 `online_doc/swanuse/node28.html:3131–3154`. | H 코드 대조 대상 아님 | 6회는 계산 사례의 권고다. 생략 기본값은 0회다. swanuse DIFFRACTION 절도 `[smpar] = 0`, `[smnum] = 0`을 기본값으로 적는다. `src/ocpcre.ftn:436`은 `'STA'`를 “variable will get value of RSTA”로 정의한다. `misc/swan.edt:242`는 명령 형식만 적는다. |
| R3:OQ-027 | 회절 사용 금지의 네 동시 조건 | swantech PDF 65쪽 / 인쇄 57쪽, 원문: “Diffraction in SWAN should not be used if,” 뒤의 네 조건은 각각 “and”로 연결된다. | `src/swanmain.ftn:6454` `IF ( IQCM.NE.0 .AND. IDIFFR.GT.0 ) THEN`; `src/swanmain.ftn:6457` `IDIFFR = 0`. | H 코드 대조 대상 아님 | 시야 차폐, 수 파장 미만의 거리, 결맞는 반사, 유의한 반사계수의 동시 조건은 적용 권고다. 이 코드는 그 네 조건을 검사하지 않는다. QC와의 중복 차단은 별개다. |
| R3:SU-001 | 1D set-up과 정규화 복사응력 | swantech PDF 65쪽 / 인쇄 57쪽, (2.143): $\frac{dS_{xx}}{dx}+\rho gH\frac{d\bar\eta}{dx}=0$. | `src/swancom1.ftn:10290` `ETA2 = ETA1 + ( SXX1 - SXX2 ) / ( 0.5 * ( DP2 + DP1 ) )`. | F 표기 차이 | $\bar\eta_{i+1}-\bar\eta_i=-(R_{xx,i+1}-R_{xx,i})/[(d_i+d_{i+1})/2]$다. 셀 길이가 양변에서 소거된다. 문서의 $H$는 바로 뒤 설명의 총수심 $d$와 같은 역할이다. 파고가 아니다. |
| R3:SU-002 | 복사응력 적분의 ρg | swantech PDF 66쪽 / 인쇄 58쪽, (2.144): $S_{xx}=\rho g\int[n\cos^2\theta+n-\frac12]E\,d\sigma d\theta$. 이 쪽의 식은 $S_{xx}$만 적는다. | `src/swancom1.ftn:10237` `CK = CG(1) * K(1)`; `src/swancom1.ftn:10239` `ELOC = SIG(1) * AC2(ID,IS,INDX)`; `src/swancom1.ftn:10246` `RSXX = RSXX + (CK*SPCDIR(ID,4)+CK - SIG(1)/2.) * ELOC`; `src/swancom1.ftn:10247` `RSXY = RSXY + CK*SPCDIR(ID,5) * ELOC`; `src/swancom1.ftn:10248` `RSYY = RSYY + (CK*SPCDIR(ID,6)+CK - SIG(1)/2.) * ELOC`; `src/swancom1.ftn:10263` `SETPDA(INDX,3) = RSXX * DDIR * FRINTF`. | F 표기 차이 | 해석: $n=c_g/c$를 쓰면 $CK=\sigma n$이다. $ELOC=\sigma N=E$다. 남은 $\sigma$는 로그 격자 적분의 가중이다. 코드가 저장하는 복사응력은 $R_{ij}=S_{ij}/(\rho g)$이므로 $S_{xx}$ 식과 같다. 기존 보고서가 PDF (2.144)의 인용에 보탠 $S_{xy}$·$S_{yy}$ 식은 이 쪽 원문에 없으므로 제거한다. |
| R3:SU-003 | 2D set-up의 힘과 부호 | swantech PDF 66쪽 / 인쇄 58쪽, (2.145): $\frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}-\frac{\partial}{\partial x}(\rho gH\frac{\partial\bar\eta}{\partial x})-\frac{\partial}{\partial y}(\rho gH\frac{\partial\bar\eta}{\partial y})=0$. | `src/swancom1.ftn:10392` `-(RSXXI*DIX + RSXXJ*DJX + RSXYI*DIY + RSXYJ*DJY)`; `src/swancom1.ftn:10394` `-(RSXYI*DIX + RSXYJ*DJX + RSYYI*DIY + RSYYJ*DJY)`; `src/swancom1.ftn:11080` `FACT = -DEPF/JAC`; `src/swancom1.ftn:10825` `RHS(INDX) = RHS(INDX) - 0.5*JCTA(INDX,1,1,1)`. | F 표기 차이 | 원문 (2.145)은 $\rho gH$를 쓴다. $H$를 총수심으로 해석하고 식 전체를 $\rho g$로 나누면 코드의 $\mathrm{WFRC}=F/(\rho g)$와 대응한다. 행렬은 $-\nabla\cdot(d\nabla\bar\eta)$를, 우변은 $-\nabla\cdot\mathrm{WFRC}$를 이산화한다. 기존 인용에서 빠뜨린 $\rho$를 복원한다. 5장의 단위 질량당 힘과 구분한다. |
| R3:SU-004 | 유도류 생략의 적용 평가 | swantech PDF 66쪽 / 인쇄 58쪽, 원문: “If the divergence of the acceleration in the resulting equation is ignored, the result is:”. 같은 쪽은 이 근사를 개방 해안에만 적용하도록 제한한다. | `src/swancom1.ftn:10402` `CALL SETUP2D( SETUP2, XCGRID, YCGRID, SETPDA(1,1), SETPDA(1,2),`; `src/swancom1.ftn:10440` `DEP2(INDX) = DEPSAV(INDX) + SETUP2(INDX)`. | H 코드 대조 대상 아님 | 문서는 가속도 발산을 무시하는 set-up 근사와 적용 범위를 설명한다. 코드는 `SETUP2D`로 구한 set-up을 `DEP2(INDX) = DEPSAV(INDX) + SETUP2(INDX)`로 수심에 더한다. 근사의 물리적 적용성은 코드 대입문의 일치 여부로 판정하는 항목이 아니다. 기존에 인용한 “ignoring these currents seems to be acceptable”와 “preliminary nature”는 지정한 PDF 쪽과 로컬 웹판에 없어 실제 문장으로 교체한다. |
