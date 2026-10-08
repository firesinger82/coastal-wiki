---
title: "EFDC+ Theory v12 Ch 2 HYDRODYNAMICS — Governing Equations + Numerical Scheme + SIG/SGZ deep note"
topic: efdc-theory-v12-ch2-hydrodynamics
canonical_source: self
citation_status: verified
verification_method: "기존 판독: EFDC_Theory_Document_Ver_12.pdf 본문 인쇄 pp.8–47, 식 2.1–2.150. recovery 대조: 근거리 방류 식 2.155·2.157·2.167·2.169·2.170·2.177과 코드의 대응. 근거리 방류 실행 결과는 확인하지 않음."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — PDF Read pages 8-47 직접"
verification_date: 2026-05-24
related:
  - models/EFDC/manual-notes/efdc-theory-doc-v12.md
  - models/EFDC/manual-notes/efdc-user-manual-r850.md
  - models/EFDC/source-analysis/
  - concepts/sst/04-code-and-tools.md
  - concepts/storm-surge/02-theory.md
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

# EFDC+ Theory v12 Ch 2 HYDRODYNAMICS — 식 level deep 노트

> 출처: [`EFDC_Theory_Document_Ver_12.pdf`](../raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf) Chapter 2 (pp.8-52), DSI LLC, October 2024.
> 본 노트는 [[efdc-theory-doc-v12]] §4.1 의 "Ch 2 깊이별 후속 노트" 후보. equation level, primary source 인용 포함.

## 0. Ch 2 구조 + Primary Sources

Ch 2 는 **§2.0.1 Overview · §2.1 Governing Equations · §2.2 Boundary Conditions and External Forcings · §2.3-2.5 Numerical Solution · §2.6 Vertical Layering · §2.7 Near-Field Discharge · §2.8 Conclusion** 으로 구성 (TOC pp.ii-iii).

**§2.0.1 Overview (p.8)** — Ch 2 의 primary sources 5종 명시:

1. Hamrick 1992 — *A Three-Dimensional Environmental Fluid Dynamics Computer Code: Theoretical and Computational Aspects*
2. Hamrick 1996 — *A User's Manual for EFDC*
3. Park et al. 1995 — *HEM3D: Description of Water Quality and Sediment Processes Submodels*
4. Tetra Tech 2002a — *Theoretical and Computational Aspects of Sediment and Contaminant Transport in EFDC*
5. Thanh et al. 2008 — *SNL-EFDC: Sediment Transport User Manual*

> "This section is primarily based on Hamrick (1992) and Ji (2008) with updates from DSI and others." (Theory v12, p.8)

## 1. §2.1 Governing Equations (pp.8-16) — 식별

### 1.1 §2.1.1 Horizontal·Vertical Coordinate Systems (pp.9-10)

수평 (x, y) 은 **curvilinear orthogonal** 좌표. 수직은 **sigma-stretched (SIG)** transformation:

$$z = \frac{z^* + h}{\zeta + h} = \frac{z^* + h}{H} \quad (2.1)$$

| 기호 | 의미 |
|---|---|
| $z$ | sigma 좌표 (무차원, 0 = 저면, 1 = 자유표면) |
| $z^*$ | datum 기준 수직 좌표 (m) |
| $h$ | datum 기준 저면 수심 (m, 양수) |
| $\zeta$ | datum 기준 자유표면 elevation (m) |
| $H = \zeta + h$ | 총 수심 (m) |

**참고**: sigma transformation 의 origin 은 Blumberg-Mellor 1987, Hamrick 1986, Vinokur 1974. SGZ 옵션은 §2.6.2 (Craig et al. 2014).

### 1.2 §2.1.2 Basic Hydrodynamic Equations (pp.10-12) — 식 핵심

Boussinesq 근사 + vertically hydrostatic boundary layer form. Curvilinear-orthogonal + sigma transform 적용된 momentum + continuity + scalar transport:

#### (a) x-방향 momentum (Eq 2.2):

$$\partial_t(m_x m_y H u) + \partial_x(m_y H u u) + \partial_y(m_x H v u) + \partial_z(m_x m_y w u)$$
$$- m_x m_y f H v - \left(v \frac{\partial m_y}{\partial x} - u \frac{\partial m_x}{\partial y}\right) H v$$
$$= -m_y H \partial_x(g\zeta + p + P_{atm}) - m_y\left(\frac{\partial h}{\partial x} - z\frac{\partial H}{\partial x}\right) \partial_z p$$
$$+ \partial_x\left(\frac{m_y}{m_x} H A_H \partial_x u\right) + \partial_y\left(\frac{m_x}{m_y} H A_H \partial_y u\right) + \partial_z\left(\frac{m_x m_y}{H} A_v \partial_z u\right)$$
$$- m_x m_y c_p D_p u \sqrt{u^2 + v^2} + S_u$$

#### (b) y-방향 momentum (Eq 2.3):

$$\partial_t(m_x m_y H v) + \partial_x(m_y H u v) + \partial_y(m_x H v v) + \partial_z(m_x m_y w v)$$
$$+ m_x m_y f H u + \left(v \frac{\partial m_y}{\partial x} - u \frac{\partial m_x}{\partial y}\right) H u$$
$$= -m_x H \partial_y(g\zeta + p + P_{atm}) - m_x\left(\frac{\partial h}{\partial y} - z\frac{\partial H}{\partial y}\right) \partial_z p$$
$$+ \partial_x\left(\frac{m_y}{m_x} H A_H \partial_x v\right) + \partial_y\left(\frac{m_x}{m_y} H A_H \partial_y v\right) + \partial_z\left(\frac{m_x m_y}{H} A_v \partial_z v\right)$$
$$- m_x m_y c_p D_p v \sqrt{u^2 + v^2} + S_v$$

#### (c) Hydrostatic balance (z-방향, Eq 2.4):

$$\frac{\partial p}{\partial z} = -gH \frac{\rho - \rho_0}{\rho_0} = -gHb$$

— vertical momentum eq 가 hydrostatic 으로 축소. $b$ = buoyancy.

#### (d) Continuity (internal + external mode, Eq 2.5-2.6):

$$\partial_t(m_x m_y \zeta) + \partial_x(m_y H u) + \partial_y(m_x H v) + \partial_z(m_x m_y w) = S_h \quad (2.5)$$
$$\partial_t(m_x m_y \zeta) + \partial_x(m_y H U) + \partial_y(m_x H V) = S_h \quad (2.6)$$

— $U, V$ = depth-integrated 수평 velocity (Eq 2.7):

$$U = \int_0^1 u \, dz, \quad V = \int_0^1 v \, dz$$

#### (e) Equation of State (Eq 2.8):

$$\rho = \rho(p, S, T, C)$$

#### (f) Scalar transport — S (salinity, Eq 2.9), T (temperature, Eq 2.10):

$$\partial_t(mHS) + \partial_x(m_y HuS) + \partial_y(m_x HvS) + \partial_z(mwS) = \partial_z\left(\frac{m}{H} A_b \partial_z S\right) + Q_S$$
$$\partial_t(mHT) + \partial_x(m_y HuT) + \partial_y(m_x HvT) + \partial_z(mwT) = \partial_z\left(\frac{m}{H} A_b \partial_z T\right) + Q_T$$

#### (g) 변수 정의 (p.12, 발췌)

| 변수 | 의미 | 단위 |
|---|---|---|
| $u, v$ | 수평 velocity (curvilinear) | m/s |
| $m_x, m_y$ | metric tensor diagonal sqrt | dimless |
| $m = m_x m_y$ | metric Jacobian | dimless |
| $p$ | reference density hydrostatic 압력 초과분 | m²/s² |
| $P_{atm}$ | 기압 (reference density 정규화) | m²/s² |
| $\rho_0$ | reference water density | kg/m³ |
| $b$ | buoyancy | — |
| $f$ | Coriolis parameter | 1/s |
| $A_H$ | 수평 momentum/mass diffusivity | m²/s |
| $A_v$ | 수직 turbulent eddy viscosity | m²/s |
| $c_p$ | vegetation 항력 계수 | dimless |
| $D_p$ | unit horizontal area 당 projected vegetation 면적 | dimless |
| $S_u, S_v$ | x·y momentum source/sink | m²/s² |
| $S_h$ | 질량보존 source/sink | m³/s |
| $S$ | salinity | ppt |
| $T$ | temperature | °C |
| $C$ | TSS (총 무기 suspended solids) | g/m³ |
| $U, V$ | depth-averaged horizontal velocity | m/s |

#### (h) Vertical velocity 관계 (Eq 2.11):

SIG 좌표 vertical velocity $w$ 와 물리 vertical velocity $w^*$:


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 25쪽·인쇄 12쪽, 식 2.11)

$$w = w^* - z\left(\frac{\partial \zeta}{\partial t} + \frac{u}{m_x}\frac{\partial \zeta}{\partial x} + \frac{v}{m_y}\frac{\partial \zeta}{\partial y}\right) + (1-z)\left(\frac{u}{m_x}\frac{\partial h}{\partial x} + \frac{v}{m_y}\frac{\partial h}{\partial y}\right)$$

문서 식 2.11은 아래 문서 원문이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 25쪽·인쇄 12쪽, 식 2.11) CALPNHS의 역변환은 인터페이스 W와 층 중심 ZZ를 함께 쓴다. (`calpnhs.f90:69` — `WZ(L,K) = W(L,K)+GI*ZZ(L,K)*( DELTI*(P(L)-P1(L)) &`; EFDC_Theory_Document_Ver_12.pdf, PDF 25쪽·인쇄 12쪽) 코드의 역변환에는 저면 시간 변화 항이 있다. (`calpnhs.f90:72` — `+ (1.-ZZ(L,K))*( DELTI*(BELV(L)-BELV1(L)) &`; EFDC_Theory_Document_Ver_12.pdf, PDF 25쪽·인쇄 12쪽) 고정 저면·같은 수직 평가 위치에서만 문서 좌표 관계를 동일한 식으로 비교한다. (`calpnhs.f90:69` — `WZ(L,K) = W(L,K)+GI*ZZ(L,K)*( DELTI*(P(L)-P1(L)) &`; `calpnhs.f90:72` — `+ (1.-ZZ(L,K))*( DELTI*(BELV(L)-BELV1(L)) &`; EFDC_Theory_Document_Ver_12.pdf, PDF 25쪽·인쇄 12쪽)


---

### 1.3 §2.1.3 Equation of State (p.13)

**UNESCO 1981** EOS (Eq 2.12):

$$\rho = 999.842594 + 6.793952 \times 10^{-2} T - 9.095290 \times 10^{-3} T^2 + \ldots$$
$$+ 1.001685 \times 10^{-4} T^3 - 1.120083 \times 10^{-6} T^4 + 6.536332 \times 10^{-9} T^5$$
$$+ (0.824493 - 4.0899 \times 10^{-3} T + 7.6438 \times 10^{-5} T^2 - 8.2467 \times 10^{-7} T^3 + 5.3875 \times 10^{-9} T^4) S$$
$$+ (-5.72466 \times 10^{-3} + 1.0227 \times 10^{-4} T - 1.6546 \times 10^{-6} T^2) S^{1.5} + 4.8314 \times 10^{-4} S^2$$

— 14-term polynomial $\rho(T, S)$. $\rho$ kg/m³, $T$ °C, $S$ ppt.

**TSS 보정** (Eq 2.13, Tetra Tech 2007a):


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 26쪽·인쇄 13쪽, 식 2.13)

$$C_{TSS} = 1 - \sum_j^N \rho_{s,j} C_j + \sum_j^N (s_j - 1) \rho_{s,j} C_j$$

문서 원문은 ρs,j를 곱한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 26쪽·인쇄 13쪽) 문서는 이 기호를 kg/m³의 퇴적물 밀도로 정의한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 26쪽·인쇄 13쪽) 코드는 SDEN·C를 고체 체적분율로 사용한다. (`calbuoy.f90:201` — `TVAR1S(L,K) = TVAR1S(L,K) + SDEN(NS)*SED(L,K,NS)`; `calbuoy.f90:202` — `TVAR1W(L,K) = TVAR1W(L,K) + (SSG(NS)-1.)*SDEN(NS)*SED(L,K,NS)`; `calbuoy.f90:234` — `B(L,K) = B(L,K)*(1. - TVAR1S(L,K)) + TVAR1W(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 26쪽·인쇄 13쪽) 코드에 대응하는 SDEN은 g/m³ 농도에 대한 역밀도이다. (`calbuoy.f90:201` — `TVAR1S(L,K) = TVAR1S(L,K) + SDEN(NS)*SED(L,K,NS)`; `Transport/mod_diffuser.f90:1643` — `SDEN = 1./2500000.`; `input.f90:2097` — `read(1,*,IOSTAT = ISO)SEDO(NS),SEDBO(NS),SDEN(NS),SSG(NS),WSEDO(NS),SEDN(NS),SEXP(NS),TAUD(NS),ISEDSCOR(NS),ISPROBDEP(NS)`; EFDC_Theory_Document_Ver_12.pdf, PDF 26쪽·인쇄 13쪽) 문서 식의 단위와 기호 정의는 코드와 함께 일치하지 않는다. (`calbuoy.f90:201` — `TVAR1S(L,K) = TVAR1S(L,K) + SDEN(NS)*SED(L,K,NS)`; `Transport/mod_diffuser.f90:1643` — `SDEN = 1./2500000.`; `input.f90:2097` — `read(1,*,IOSTAT = ISO)SEDO(NS),SEDBO(NS),SDEN(NS),SSG(NS),WSEDO(NS),SEDN(NS),SEXP(NS),TAUD(NS),ISEDSCOR(NS),ISPROBDEP(NS)`; EFDC_Theory_Document_Ver_12.pdf, PDF 26쪽·인쇄 13쪽) 문서의 ρs,j와 코드의 역밀도 SDEN을 구별한다. (`calbuoy.f90:201` — `TVAR1S(L,K) = TVAR1S(L,K) + SDEN(NS)*SED(L,K,NS)`; `Transport/mod_diffuser.f90:1643` — `SDEN = 1./2500000.`; `input.f90:2097` — `read(1,*,IOSTAT = ISO)SEDO(NS),SEDBO(NS),SDEN(NS),SSG(NS),WSEDO(NS),SEDN(NS),SEXP(NS),TAUD(NS),ISEDSCOR(NS),ISPROBDEP(NS)`; EFDC_Theory_Document_Ver_12.pdf, PDF 26쪽·인쇄 13쪽)


— sediment 농도 $C_j$ 있을 시 density·buoyancy 보정.

---

### 1.4 §2.1.4 Vertical Turbulent Closure (pp.14-15) — **Mellor-Yamada Level 2.5 + 변형 4 옵션**

Mellor-Yamada 1982 (이후 Galperin et al. 1988 수정) 의 2nd-moment 닫음. EFDC+ 의 vertical eddy viscosity·diffusivity 는 turbulent intensity $q^2$, turbulent length scale $l$, Richardson number $R_q$ 의 함수.

#### (a) Eddy viscosity·diffusivity 정의 (Eq 2.14·2.20):

$$A_v = \phi_A A_0 q l \quad (2.14)$$
$$A_b = \rho_K K_0 q l \quad (2.20)$$

stability function (Eq 2.15):

$$\phi_A = \frac{1 + R_q/R_1}{(1 + R_q/R_2)(1 + R_q/R_3)}$$

(Eq 2.16-2.19) — $A_0, R_1, R_2, R_3$ 는 closure 상수 $A_1, A_2, B_1, B_2, C_1$ 의 algebraic 조합.

#### (b) Richardson number (Eq 2.23):

$$R_q = \frac{gH}{q^2} \cdot \frac{l^2}{H^2} \cdot \frac{\partial b}{\partial z}$$

#### (c) **Table 2.1** — closure 상수 4 모델 옵션 (p.15):

| Formulation | $K_0$ | $R_1^{-1}$ | $R_2^{-1}$ | $R_3^{-1}$ |
|---|---:|---:|---:|---:|
| **Mellor-Yamada 1982** | 0.493928 | 7.846436 | 34.676400 | 6.127200 |
| **Galperin et al. 1988** | 0.493928 | 7.760050 | 34.676440 | 6.127200 |
| **Kantha-Clayson 1994** | 0.493928 | 8.679790 | 30.192000 | 6.127200 |
| **Kantha 2003** | 0.490025 | 14.509100 | 24.388300 | 3.236400 |

— EFDC+ user 가 선택. Mellor-Yamada 1982 의 base constants: $A_1 = 0.92, B_1 = 16.6, C_1 = 0.08, A_2 = 0.74, B_2 = 10.1$.

> **구현 확인** ([[efdc_turbulence]] §B, augmented 2026-06-03): `calavb.f90` 의 `ISTOPT(0)` 는 **2(Kantha-Clayson)·3(Kantha)** 만 분기하고 기본(0/1)=**Galperin** → **MY1982 원본 상수(R₁⁻¹=7.846436)는 이 EFDC+ build 에서 선택 불가**(실질 3 옵션). 별도로 `ISGOTM>0` 시 GOTM(k-ε/MY/GLS)으로 대체.

#### (d) $q^2$ + $q^2 l$ prognostic equations (Eq 2.24·2.25):

$$\partial_t(mHq^2) + \partial_x(Pq^2) + \partial_y(Qq^2) + \partial_z(mwq^2)$$

해석 수정식 (EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽, 식 2.24; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽, 식 2.25; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽, 식 2.26)

$$= \partial_z\left(\frac{mA_q}{H}\partial_z q^2\right) + 2m\frac{A_v}{H}\left[(\partial_z u)^2 + (\partial_z v)^2\right] + 2mgA_b \partial_z b - 2m\frac{Hq^3}{B_1 l} + S_b$$

노트의 아래 식은 PDF 식 2.24에 없는 더하기 부호를 보충한 해석 수정식이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽, 식 2.24)


$$\partial_t(mHq^2 l) + \partial_x(Pq^2 l) + \partial_y(Qq^2 l) + \partial_z(mwq^2 l)$$

문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽, 식 2.24; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽, 식 2.25; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽, 식 2.26)

$$= \partial_z\left[\frac{mA_{ql}}{H}\partial_z(q^2 l)\right] + mlE_1\left\{\frac{A_v}{H}\left[(\partial_z u)^2 + (\partial_z v)^2\right] + E_3 g A_b \partial_z b\right\}$$

코드의 q²l 생성은 CTE1·전단+CTE3TMP·부력이다. (`calqq2t.f90:280` — `PQQL = DELT*HP(L)*(CTE3TMP*PQQB + CTE1*(PQQU+PQQV) + CE4VEG*PQQVEGE(L,K) + CE4MHK*PQQMHKE(L,K) + CE4SUP*PQQSUPE(L,K))`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) 문서처럼 E1을 부력항의 E3에도 다시 곱하지 않는다. (`calqq2t.f90:280` — `PQQL = DELT*HP(L)*(CTE3TMP*PQQB + CTE1*(PQQU+PQQV) + CE4VEG*PQQVEGE(L,K) + CE4MHK*PQQMHKE(L,K) + CE4SUP*PQQSUPE(L,K))`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) CTE3TMP는 성층 조건에 따라 달라진다. (`calqq2t.f90:267` — `DELB = B(L,K) - B(L,K+1)`; `calqq2t.f90:268` — `CTE3TMP = CTE3`; `calqq2t.f90:269` — `if( DELB < 0.0 ) CTE3TMP = CTE1`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) CTE2는 입력 코드가 미사용으로 명시한다. (`input.f90:734` — `! *** PMC - CTE2 NOT USED`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽)

$$- mE_2 \frac{Hq^3}{B_1}\left[1 + E_4\left(\frac{l}{\kappa H z}\right)^2 + E_5\left(\frac{l}{\kappa H (1-z)}\right)^2\right] + S_l$$

상수: $E_1 = 1.8, E_2 = 1.0, E_3 = 1.8, E_4 = 1.33, E_5 = 0.25$.

#### (e) Wall function (Eq 2.26):

$$\frac{1}{L} = \frac{1}{H}\left(\frac{1}{z} + \frac{1}{1-z}\right)$$

#### (f) Length-scale limiting (p.16):

Galperin et al. 1988 권장: $\sqrt{R_q} < 0.53$ (stable stratification 시).

$A_q = 0.2 q l$ (Mellor-Yamada 1982 추천값).

Aq=0.2ql은 문서의 추천식이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) CALAVB는 0.205·점성 합 또는 0.314·ql 합을 계산한다. (`calavb.f90:320` — `AQ(L,K) = 0.205*(AV(L,K-1)+AV(L,K))`; `calavb.f90:352` — `AQ(L,K) = 0.314*( DML(L,K-1)*QQSQR(L,K-1)+DML(L,K)*QQSQR(L,K) ) + AVOXYHPI(L)`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) Kantha의 q²l 확산 비는 0.377/0.628이다. (`calqq2t.f90:100` — `if( ISTOPT(0) == 3 )SQLDSQ = 0.377/0.628`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) CALAVB의 한 하부 경계 줄은 DML**QQSQR를 사용한다. (`calavb.f90:358` — `AQ(L,KSZ(L)) = 0.314*DML(L,KSZ(L))**QQSQR(L,KSZ(L)) + AVOXYHPI(L)`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) 이 거듭제곱은 원문 확인 사실이다. (`calavb.f90:358` — `AQ(L,KSZ(L)) = 0.314*DML(L,KSZ(L))**QQSQR(L,KSZ(L)) + AVOXYHPI(L)`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽) 해석: 곱셈 오기의 가능성을 제기할 수 있다(정적 판독, 실행 미확인). (`calavb.f90:358` — `AQ(L,KSZ(L)) = 0.314*DML(L,KSZ(L))**QQSQR(L,KSZ(L)) + AVOXYHPI(L)`; EFDC_Theory_Document_Ver_12.pdf, PDF 28쪽·인쇄 15쪽)


---

### 1.5 §2.1.5 Horizontal Turbulence Closure (p.16) — Smagorinsky

**Smagorinsky 1963** subgrid scale closure (Eq 2.27):

$$A_H = C_s \Delta x \Delta y \sqrt{(\partial_x u)^2 + (\partial_y v)^2 + \frac{1}{2}(\partial_y u + \partial_x v)^2}$$

— $C_s$ 의 typical range: **0.1 - 0.2** (Xiao & Cinnella 2019). Canuto-Cheng 1997 은 0.11 constant 권장하면서도 universal value 가 아니라고 명시. Meyers-Sagaut 2006 가 $C_s$ 의 정확한 표현 유도 — flow + grid 의존.

---

## 2. §2.2 Boundary Conditions and External Forcings (pp.16-31)

### 2.1 Vertical BCs (turbulent kinetic energy + length scale)

자유표면 (z=1):
$$q^2 = B_1^{2/3}\sqrt{t_{sx}^2 + t_{sy}^2}, \quad l = 0 \quad (2.28)$$

저면 (z=0):
$$q^2 = B_1^{2/3}\sqrt{t_{bx}^2 + t_{by}^2}, \quad l = 0 \quad (2.29)$$

— Eq 2.29 는 near-bottom sediment 농도 ↑·고주파 표면파 ↑ 시 부적절 (p.16).

### 2.2 §2.2.1 Bottom Friction (p.16)

Quadratic resistance (Eq 2.30):

$$\frac{1}{\rho_w}\begin{bmatrix}\tau_{bx} \\ \tau_{by}\end{bmatrix} = C_b \sqrt{u_1^2 + v_1^2}\begin{bmatrix}u_1 \\ v_1\end{bmatrix}$$

— $u_1, v_1$ = bottom layer velocity.

저면 stress 계수 (Nezu 1993, Eq 2.31):

$$C_b = \left[\frac{\kappa}{\ln(\Delta_1 / 2z_0) + (\Pi - 1)}\right]^2$$

PDF는 Pi=0을 설명한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽) 해당 Nezu 단층 코드의 −0.8은 Pi=0.2에 대응한다. (`caltbxy.f90:541` — `! *** NEZU & NAKAGAWA (1993) WHERE THE WAKE parameter IS 0.2  FOR TURBULENT CONDITIONS.  -0.8 = WAKE - 1.`; `caltbxy.f90:542` — `STBX(L) = (VKC/(LOG( HUDZBR ) - 0.8))**2`; `caltbxy.f90:543` — `STBY(L) = (VKC/(LOG( HVDZBR ) - 0.8))**2`; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽) 다른 단층 코드는 로그에서 1을 뺀다. (`caltbxy.f90:598` — `STBX(L) = STBXO(L)*0.16/( (LOG( HUDZBR ) -1.)**2)`; `caltbxy.f90:599` — `STBY(L) = STBYO(L)*0.16/( (LOG( HVDZBR ) -1.)**2)`; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽)

### 2.3 §2.2.2 Vegetation (pp.17-18) — Vegetation Drag

식 2.32·2.33의 생성 효율과 벽 항 기호는 코드 CE4VEG·FPROX와 구분한다. (`calqq2t.f90:280` — `PQQL = DELT*HP(L)*(CTE3TMP*PQQB + CTE1*(PQQU+PQQV) + CE4VEG*PQQVEGE(L,K) + CE4MHK*PQQMHKE(L,K) + CE4SUP*PQQSUPE(L,K))`; `aaefdc.f90:1525` — `if( IFPROX == 2 ) FPROX(L,K) = (1./(VKC*Z(L,K))**2) + CTE5*(1./(VKC*(1.-Z(L,K)))**2)/(CTE4+0.00001)`; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽, 식 2.32; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽, 식 2.33) 코드는 SCVEG·BPVEG와 층별 식생 높이를 사용한다. (`caltbxy.f90:752` — `if( ISVEGL == 1 ) CPVEGU = CPVEGU + 10.E-6/((BPVEG(MW) + BPVEG(M))*UMAGTMP )`; `caltbxy.f90:757` — `CPVEGU = SCVEG(M)*CPVEGU`; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 31쪽·인쇄 18쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽)

Bulk drag coefficient (수족산업·갈대 canopy, Plew 2011 + Scott-O'Donncha 2019 fitting, Eq 2.34):


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽, 식 2.32; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽, 식 2.33; EFDC_Theory_Document_Ver_12.pdf, PDF 31쪽·인쇄 18쪽, 식 2.34; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽, 식 2.35)

$$\bar{C}_D = 2.0 - 67 a_d$$

식 2.34의 2−67ad와 식 2.35의 수직 다항식은 대조한 f90에서 찾지 못했다. (EFDC_Theory_Document_Ver_12.pdf, PDF 31쪽·인쇄 18쪽, 식 2.34; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽, 식 2.35) 이 빌드의 두 식 자동 계산은 확인하지 않음. (`calqq2t.f90:278` — `PQQ  = DELT*( PQQB+PQQU+PQQV+PQQVEGE(L,K)+PQQMHKE(L,K)+PQQSUPE(L,K) )`; `calqq2t.f90:279` — `UUU(L,K) = UUU(L,K) + 2.*PQQ`; `calqq2t.f90:280` — `PQQL = DELT*HP(L)*(CTE3TMP*PQQB + CTE1*(PQQU+PQQV) + CE4VEG*PQQVEGE(L,K) + CE4MHK*PQQMHKE(L,K) + CE4SUP*PQQSUPE(L,K))`; `calqq2t.f90:281` — `VVV(L,K) = VVV(L,K) + DML(L,K)*PQQL`; `calqq2t.f90:355` — `CMQLTMP = 1. - CLQLTMP-CUQLTMP+DELT*(QQSQR(L,1)/(CTURBB1(L,1)*DML(L,1)*HP(L)))*(1.+CTE4*DML(L,1)*DML(L,1)*FPROX(L,1)) &`; `calqq2t.f90:356` — `+ DELT*HPI(L)*(CE4VEG*PQQVEGI(L,1)+CE4MHK*PQQMHKI(L,1)+CE4SUP*PQQSUPI(L,1))`; `aaefdc.f90:1525` — `if( IFPROX == 2 ) FPROX(L,K) = (1./(VKC*Z(L,K))**2) + CTE5*(1./(VKC*(1.-Z(L,K)))**2)/(CTE4+0.00001)`; `caltbxy.f90:750` — `! *** DRAG COEFFICIENT: U COMPONENT`; `caltbxy.f90:751` — `CPVEGU = 1.0`; `caltbxy.f90:752` — `if( ISVEGL == 1 ) CPVEGU = CPVEGU + 10.E-6/((BPVEG(MW) + BPVEG(M))*UMAGTMP )`; `caltbxy.f90:753` — `if( CPVEGU > 1.0 )then`; `caltbxy.f90:754` — `! *** CALCULATE R FOR LAMINAR FLOW`; `caltbxy.f90:755` — `CPVEGU = CPVEGU-0.5`; `caltbxy.f90:757` — `CPVEGU = SCVEG(M)*CPVEGU`; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 31쪽·인쇄 18쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽)


— $a_d$ = 무차원 canopy density.

Depth-varying drag (Eq 2.35):


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽, 식 2.32; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽, 식 2.33; EFDC_Theory_Document_Ver_12.pdf, PDF 31쪽·인쇄 18쪽, 식 2.34; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽, 식 2.35)

$$C_D(\zeta) = \bar{C}_D(1.2 + 0.8\zeta - 0.5\zeta^2)$$

식 2.34의 2−67ad와 식 2.35의 수직 다항식은 대조한 f90에서 찾지 못했다. (EFDC_Theory_Document_Ver_12.pdf, PDF 31쪽·인쇄 18쪽, 식 2.34; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽, 식 2.35) 이 빌드의 두 식 자동 계산은 확인하지 않음. (`calqq2t.f90:278` — `PQQ  = DELT*( PQQB+PQQU+PQQV+PQQVEGE(L,K)+PQQMHKE(L,K)+PQQSUPE(L,K) )`; `calqq2t.f90:279` — `UUU(L,K) = UUU(L,K) + 2.*PQQ`; `calqq2t.f90:280` — `PQQL = DELT*HP(L)*(CTE3TMP*PQQB + CTE1*(PQQU+PQQV) + CE4VEG*PQQVEGE(L,K) + CE4MHK*PQQMHKE(L,K) + CE4SUP*PQQSUPE(L,K))`; `calqq2t.f90:281` — `VVV(L,K) = VVV(L,K) + DML(L,K)*PQQL`; `calqq2t.f90:355` — `CMQLTMP = 1. - CLQLTMP-CUQLTMP+DELT*(QQSQR(L,1)/(CTURBB1(L,1)*DML(L,1)*HP(L)))*(1.+CTE4*DML(L,1)*DML(L,1)*FPROX(L,1)) &`; `calqq2t.f90:356` — `+ DELT*HPI(L)*(CE4VEG*PQQVEGI(L,1)+CE4MHK*PQQMHKI(L,1)+CE4SUP*PQQSUPI(L,1))`; `aaefdc.f90:1525` — `if( IFPROX == 2 ) FPROX(L,K) = (1./(VKC*Z(L,K))**2) + CTE5*(1./(VKC*(1.-Z(L,K)))**2)/(CTE4+0.00001)`; `caltbxy.f90:750` — `! *** DRAG COEFFICIENT: U COMPONENT`; `caltbxy.f90:751` — `CPVEGU = 1.0`; `caltbxy.f90:752` — `if( ISVEGL == 1 ) CPVEGU = CPVEGU + 10.E-6/((BPVEG(MW) + BPVEG(M))*UMAGTMP )`; `caltbxy.f90:753` — `if( CPVEGU > 1.0 )then`; `caltbxy.f90:754` — `! *** CALCULATE R FOR LAMINAR FLOW`; `caltbxy.f90:755` — `CPVEGU = CPVEGU-0.5`; `caltbxy.f90:757` — `CPVEGU = SCVEG(M)*CPVEGU`; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 31쪽·인쇄 18쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽)


### 2.4 §2.2.3 Wind Forcings (pp.19-21) — **4 + 1 = 5 wind drag 옵션**

Wind stress (Eq 2.36):

$$\frac{1}{\rho_w}\begin{bmatrix}\tau_{sx} \\ \tau_{sy}\end{bmatrix} = C_D \frac{\rho_a}{\rho_w} W_s \begin{bmatrix}W_{sx} \\ W_{sy}\end{bmatrix}$$

#### Option 1: Original EFDC piecewise (Eq 2.38)

$$C_D = \begin{cases}
3.83111 \times 10^{-5} W_s^{-3} - 0.000308715 W_s^{-2} + 0.00116012 W_s^{-1} + 0.000899602, & W_s < 5 \text{ m/s} \\
-5.37642 \times 10^{-6} W_s^3 + 0.000112556 W_s^2 - 0.000721203 W_s + 0.00259657, & 5 \le W_s < 7 \\
-3.99677 \times 10^{-7} W_s^2 + 7.32937 \times 10^{-5} W_s + 0.000726716, & W_s \ge 7
\end{cases}$$

7 m/s는 코드의 둘째 구간에 들어간다. (`caltsxy.f90:778` — `elseif( U10 >= 5.0 .and. U10 <= 7. )then`; `caltsxy.f90:779` — `CD10 = -5.37642E-006*(U10**3) + 0.000112556*(U10**2) - 0.000721203*U10 + 0.00259657`; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽)


#### Option 2: Original + relative-to-water velocity (Eq 2.39-2.40)

#### Option 3: ECMWF wave-age-dependent (Hersbach 2011, Eq 2.41)

$$C_D = \frac{c_1 + c_2 W_s^{p_1}}{W_s^{p_2}}$$

— $c_1 = 1.03 \times 10^{-3}$, $c_2 = 0.04 \times 10^{-3}$, $p_1 = 1.48$, $p_2 = 0.21$.

#### Option 4: COARE 3.6 bulk (Fairall 1996·2003·Edson 2013, neutral atmosphere 가정)

(Eq 2.42-2.44):


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽, 식 2.38; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽, 식 2.42; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽, 식 2.43; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽, 식 2.44)

$$\tau = \rho_a C_D U_r^2$$

응력은 U10·상대 풍속 벡터의 곱이다. (`caltsxy.f90:809` — `TSX(L) = 1.225E-3*CD10*U10*TSEAST             ! *** TSX IS THE WIND SHEAR IN THE U DIRECTION (M2/S2)`; `caltsxy.f90:810` — `TSY(L) = 1.225E-3*CD10*U10*TSNORT             ! *** TSY IS THE WIND SHEAR IN THE V DIRECTION (M2/S2)`; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽) 상대 풍속 크기의 제곱과 일반적으로 다르다. (`caltsxy.f90:809` — `TSX(L) = 1.225E-3*CD10*U10*TSEAST             ! *** TSX IS THE WIND SHEAR IN THE U DIRECTION (M2/S2)`; `caltsxy.f90:810` — `TSY(L) = 1.225E-3*CD10*U10*TSNORT             ! *** TSY IS THE WIND SHEAR IN THE V DIRECTION (M2/S2)`; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽)


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽, 식 2.38; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽, 식 2.42; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽, 식 2.43; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽, 식 2.44)

$$C_D = \left[\frac{\kappa}{\ln(z/z_0)}\right]^2$$

바람 전용 IWDRAG=3은 중립 COARE 근사 다항식을 쓴다. (`caltsxy.f90:786` — `elseif( IWDRAG == 3 )then`; `caltsxy.f90:789` — `CD10 = 8.394E-05*U10 + 8.285E-04`; `caltsxy.f90:791` — `CD10 = 1.376E-08*U10**4 - 9.841E-07*U10**3 + 2.324E-05*U10**2 - 1.012E-04*U10 + 8.971E-04`; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽) ISTOPT(2)=2를 함께 켜면 열교환 COARE의 항력계수를 사용한다. (`caltsxy.f90:811` — `if( IWDRAG == 3 .and. ISTOPT(2) == 2 )then`; `caltsxy.f90:812` — `TSX(L) = 1.225E-3*CDCOARE(L)*U10*TSEAST`; `caltsxy.f90:813` — `TSY(L) = 1.225E-3*CDCOARE(L)*U10*TSNORT`; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽) 로그 조도 유도식의 모든 바람 전용 분기 직접 구현은 확인하지 않음. (`caltsxy.f90:786` — `elseif( IWDRAG == 3 )then`; `caltsxy.f90:789` — `CD10 = 8.394E-05*U10 + 8.285E-04`; `caltsxy.f90:791` — `CD10 = 1.376E-08*U10**4 - 9.841E-07*U10**3 + 2.324E-05*U10**2 - 1.012E-04*U10 + 8.971E-04`; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽)


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽, 식 2.38; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽, 식 2.42; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽, 식 2.43; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽, 식 2.44)

$$z_0 = z_0^{\text{smooth}} + z_0^{\text{rough}} = \gamma \frac{\nu}{u_*} + \alpha \frac{u_*^2}{g}$$

바람 전용 IWDRAG=3은 중립 COARE 근사 다항식을 쓴다. (`caltsxy.f90:786` — `elseif( IWDRAG == 3 )then`; `caltsxy.f90:789` — `CD10 = 8.394E-05*U10 + 8.285E-04`; `caltsxy.f90:791` — `CD10 = 1.376E-08*U10**4 - 9.841E-07*U10**3 + 2.324E-05*U10**2 - 1.012E-04*U10 + 8.971E-04`; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽) ISTOPT(2)=2를 함께 켜면 열교환 COARE의 항력계수를 사용한다. (`caltsxy.f90:811` — `if( IWDRAG == 3 .and. ISTOPT(2) == 2 )then`; `caltsxy.f90:812` — `TSX(L) = 1.225E-3*CDCOARE(L)*U10*TSEAST`; `caltsxy.f90:813` — `TSY(L) = 1.225E-3*CDCOARE(L)*U10*TSNORT`; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽) 로그 조도 유도식의 모든 바람 전용 분기 직접 구현은 확인하지 않음. (`caltsxy.f90:786` — `elseif( IWDRAG == 3 )then`; `caltsxy.f90:789` — `CD10 = 8.394E-05*U10 + 8.285E-04`; `caltsxy.f90:791` — `CD10 = 1.376E-08*U10**4 - 9.841E-07*U10**3 + 2.324E-05*U10**2 - 1.012E-04*U10 + 8.971E-04`; EFDC_Theory_Document_Ver_12.pdf, PDF 32쪽·인쇄 19쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 33쪽·인쇄 20쪽)


— Charnock coefficient $\alpha$, roughness Reynolds 계수 $\gamma = 0.11$ (smooth flow laboratory experiments).

#### Option 5: User-defined linear (EFDC+ v10.4 신규, Eq 2.45)

$$C_D = \begin{cases}
C_1, & W_s \le W_1 \\
C_1 + \frac{C_2 - C_1}{W_2 - W_1}(W_s - W_1), & W_1 < W_s < W_2 \\
C_2, & W_s \ge W_2
\end{cases}$$

#### **Table 2.2** (p.21) — Linear wind drag 12 relationships:

| Formulation | $W_1$ (m/s) | $W_2$ (m/s) | $C_1$ ($\times 10^{-3}$) | $C_2$ ($\times 10^{-3}$) |
|---|---:|---:|---:|---:|
| Francis (1951) | 1 | 25 | 1.3 | 32.5 |
| Sheppard (1958) | 1 | 20 | 0.914 | 3.08 |
| Wilson (1960) | 2.8 | 20 | 1.1 | 2.6 |
| Deacon-Webb (1962) | 1 | 14 | 1.07 | 1.98 |
| Heaps (1965) | 5 | 19.2 | 0.565 | 2.513 |
| Smith-Banke (1975) | 6 | 21 | 1.06 | 2.185 |
| **Garratt (1977)** | 4 | 21 | 1.018 | 2.157 |
| **Large-Pond (1981)** | 10 | 26 | 1.14 | 2.18 |
| Wu (1982) | 1 | 80 | 0.865 | 6.0 |
| Anderson (1993) | 4.5 | 21 | 0.81 | 1.98 |
| Yelland-Taylor (1996) | 6 | 26 | 1.02 | 2.42 |
| Yelland et al. (1998) | 6 | 26 | 0.926 | 2.346 |

— Garratt 1977 + Large-Pond 1981 이 storm-surge 운영의 표준.

### 2.5 §2.2.4 Wave Action (pp.21-23) — Radiation Stress + Dispersion

두 wave 옵션 (p.21):
1. **SMB (Sverdrup-Munk-Bretschneider)** internal wind-wave 모듈 (§2.2.5)
2. **External SWAN** linkage (SWAN Team 2019)

#### (a) Radiation stress (Longuet-Higgins & Stewart 1964, Eq 2.46-2.48):


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽, 식 2.46; EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽, 식 2.48; EFDC_Theory_Document_Ver_12.pdf, PDF 35쪽·인쇄 22쪽, 식 2.49)

$$S_{xx} = n\cos^2\theta + n - \frac{1}{2}E$$

wavesxy는 방사 응력 괄호 전체에 E를 곱한다. (`Waves/wavesxy.f90:236` — `SXXTMP = WE*(WG/2+WN*COS(WV(L).DIR)**2)        ! *** RADIATION SHEAR STRESS [Kg/S2]`; `Waves/wavesxy.f90:238` — `SYYTMP = WE*(WG/2+WN*SIN(WV(L).DIR)**2)        ! *** RADIATION SHEAR STRESS [Kg/S2]`; EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 35쪽·인쇄 22쪽) 문서 식 2.46·2.48은 마지막 항에만 E를 인쇄한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽, 식 2.46; EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽, 식 2.48)

$$S_{xy} = S_{yx} = (n\cos\theta\sin\theta) E$$

문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽, 식 2.46; EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽, 식 2.48; EFDC_Theory_Document_Ver_12.pdf, PDF 35쪽·인쇄 22쪽, 식 2.49)

$$S_{yy} = n\sin^2\theta + n - \frac{1}{2}E$$

wavesxy는 방사 응력 괄호 전체에 E를 곱한다. (`Waves/wavesxy.f90:236` — `SXXTMP = WE*(WG/2+WN*COS(WV(L).DIR)**2)        ! *** RADIATION SHEAR STRESS [Kg/S2]`; `Waves/wavesxy.f90:238` — `SYYTMP = WE*(WG/2+WN*SIN(WV(L).DIR)**2)        ! *** RADIATION SHEAR STRESS [Kg/S2]`; EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 35쪽·인쇄 22쪽) 문서 식 2.46·2.48은 마지막 항에만 E를 인쇄한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽, 식 2.46; EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽, 식 2.48)


코드의 유의파고 에너지는 ρgHs²/16이다. (`Waves/wavesxy.f90:232` — `WE = 9.81*1000.*WV(L).HEIGHT**2 /16.           ! *** TOTAL WAVE ENERGY : KG/S2`; `Waves/mod_windwave.f90:741` — `WVENEP(L)= G*WV(L).HEIGHT**2./16.                         ! *** ENERGY/RHO (M3/S2) FOR RANDOM WAVE`; EFDC_Theory_Document_Ver_12.pdf, PDF 34쪽·인쇄 21쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 35쪽·인쇄 22쪽) 문서 식 2.49는 ρgHs²/8이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 35쪽·인쇄 22쪽, 식 2.49)

#### (b) Dispersion + 근사 (Hunt 1979, Eq 2.50-2.55):

$$k = \frac{2\pi}{L}, \quad L = \frac{gT^2}{2\pi}\tanh(kh) \text{ (정확)}$$

Hunt 1979 근사:
$$L \approx T\sqrt{\frac{1}{d}gh}$$
$$d = \gamma + \frac{1}{1 + 0.6522\gamma + 0.4622\gamma^2 + 0.0864\gamma^4 + 0.0675\gamma^5}, \quad \gamma = \omega^2 \frac{h}{g}$$

#### (c) Wave Reynolds + bottom friction (Swart 1974, Eq 2.57-2.60):

$$R_w = \frac{U_b A}{\nu}, \quad r = \frac{A}{k_s}$$
$$A = \frac{H_s}{2\sinh(kh)}, \quad U_b = A\omega = \frac{\omega H_s}{2\sinh(kh)}$$

문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 36쪽·인쇄 23쪽, 식 2.60)

$$f_w = \begin{cases}
e^{(5.21 r^{-0.19} - 6.0)}, & r > 1.57 \\
0.3 r, & r = 1.57
\end{cases}$$

코드의 Swart 지수식은 r≤1.57·Re>5E5에 적용한다. (`Waves/wavebl.f90:208` — `elseif( REYWAVE>5D5 .and. RA <= 1.57 )then`; `Waves/wavebl.f90:210` — `FCW = EXP(5.2*RA**(-0.19)-6)    ! *** Baird's paper`; EFDC_Theory_Document_Ver_12.pdf, PDF 36쪽·인쇄 23쪽) 코드의 Swart 지수식 계수는 5.2이다. (`Waves/wavebl.f90:210` — `FCW = EXP(5.2*RA**(-0.19)-6)    ! *** Baird's paper`; EFDC_Theory_Document_Ver_12.pdf, PDF 36쪽·인쇄 23쪽) 코드는 0.3 상한을 적용한다. (`Waves/wavebl.f90:211` — `FCW = min(FCW,0.3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 36쪽·인쇄 23쪽)


PDF 원문의 둘째 조건은 r=1.57이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 36쪽·인쇄 23쪽) 코드는 Reynolds 수 5E5를 경계로 세 분기를 쓴다. (`Waves/wavebl.f90:200` — `if( REYWAVE <= 5D5 )then`; `Waves/wavebl.f90:204` — `elseif( REYWAVE>5D5 .and. RA>1.57 )then`; `Waves/wavebl.f90:208` — `elseif( REYWAVE>5D5 .and. RA <= 1.57 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 36쪽·인쇄 23쪽) 문서식과 코드의 분기 조건은 다르다. (`Waves/wavebl.f90:200` — `if( REYWAVE <= 5D5 )then`; `Waves/wavebl.f90:204` — `elseif( REYWAVE>5D5 .and. RA>1.57 )then`; `Waves/wavebl.f90:208` — `elseif( REYWAVE>5D5 .and. RA <= 1.57 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 36쪽·인쇄 23쪽)


— Nikuradse 등가 sand grain roughness $k_s$.

### 2.6 §2.2.5 Local Wind-Generated Waves (pp.23-24) — SMB

**SMB** (Sverdrup-Munk-Bretschneider, Ji 2008) — 등가 fetch + wind 조건 기반 empirical wave height·period:

Wave height (Eq 2.61):

문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽, 식 2.61; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽, 식 2.63; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽, 식 2.64)

$$H_s = 0.283 \alpha \frac{W_s^2}{g} \tanh\left[0.0125\left(\frac{gF}{\alpha W_s^2}\right)^{0.42}\right]$$

α·β의 수심은 코드 Fetch_Depth의 취송 구간 평균 수심이다. (`Waves/mod_windwave.f90:214` — `AVEDEP = Fetch_Depth(LG,ZONE)              ! *** Get the average depth along the fetch (m)`; `Waves/mod_windwave.f90:218` — `FC0 = (G*AVEDEP/WINDVEL2)**0.75`; `Waves/mod_windwave.f90:237` — `FC0 = TANH(0.833*(G*AVEDEP/WINDVEL2)**0.375)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽) 파고 상한에는 국소 HP를 사용한다. (`Waves/mod_windwave.f90:222` — `WV(L).HEIGHT = min(0.75*HP(L), FC2*FC3)                                      ! *** Wave height (m)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽) 문서의 H와 평균 수심을 같은 값으로 고정하지 않는다. (`Waves/mod_windwave.f90:214` — `AVEDEP = Fetch_Depth(LG,ZONE)              ! *** Get the average depth along the fetch (m)`; `Waves/mod_windwave.f90:218` — `FC0 = (G*AVEDEP/WINDVEL2)**0.75`; `Waves/mod_windwave.f90:237` — `FC0 = TANH(0.833*(G*AVEDEP/WINDVEL2)**0.375)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽) 코드는 파고에 0.75HP 상한을 적용한다. (`Waves/mod_windwave.f90:222` — `WV(L).HEIGHT = min(0.75*HP(L), FC2*FC3)                                      ! *** Wave height (m)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽) 코드는 주기 하한도 적용한다. (`Waves/mod_windwave.f90:240` — `WV(L).PERIOD = max(1.D-3, FC1*FC2)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽)


Peak period (Eq 2.62):
$$T_p = 7.54 \beta \frac{W_s}{g} \tanh\left[0.077\left(\frac{gF}{\beta W_s^2}\right)^{0.25}\right]$$

(Eq 2.63-2.64):

문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽, 식 2.61; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽, 식 2.63; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽, 식 2.64)

$$\alpha = \tanh\left[0.53\left(\frac{gH}{W_s^2}\right)^{0.75}\right]$$

α·β의 수심은 코드 Fetch_Depth의 취송 구간 평균 수심이다. (`Waves/mod_windwave.f90:214` — `AVEDEP = Fetch_Depth(LG,ZONE)              ! *** Get the average depth along the fetch (m)`; `Waves/mod_windwave.f90:218` — `FC0 = (G*AVEDEP/WINDVEL2)**0.75`; `Waves/mod_windwave.f90:237` — `FC0 = TANH(0.833*(G*AVEDEP/WINDVEL2)**0.375)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽) 파고 상한에는 국소 HP를 사용한다. (`Waves/mod_windwave.f90:222` — `WV(L).HEIGHT = min(0.75*HP(L), FC2*FC3)                                      ! *** Wave height (m)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽) 문서의 H와 평균 수심을 같은 값으로 고정하지 않는다. (`Waves/mod_windwave.f90:214` — `AVEDEP = Fetch_Depth(LG,ZONE)              ! *** Get the average depth along the fetch (m)`; `Waves/mod_windwave.f90:218` — `FC0 = (G*AVEDEP/WINDVEL2)**0.75`; `Waves/mod_windwave.f90:237` — `FC0 = TANH(0.833*(G*AVEDEP/WINDVEL2)**0.375)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽)


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽, 식 2.61; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽, 식 2.63; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽, 식 2.64)

$$\beta = \tanh\left[0.833\left(\frac{gH}{W_s^2}\right)^{0.375}\right]$$

α·β의 수심은 코드 Fetch_Depth의 취송 구간 평균 수심이다. (`Waves/mod_windwave.f90:214` — `AVEDEP = Fetch_Depth(LG,ZONE)              ! *** Get the average depth along the fetch (m)`; `Waves/mod_windwave.f90:218` — `FC0 = (G*AVEDEP/WINDVEL2)**0.75`; `Waves/mod_windwave.f90:237` — `FC0 = TANH(0.833*(G*AVEDEP/WINDVEL2)**0.375)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽) 파고 상한에는 국소 HP를 사용한다. (`Waves/mod_windwave.f90:222` — `WV(L).HEIGHT = min(0.75*HP(L), FC2*FC3)                                      ! *** Wave height (m)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽) 문서의 H와 평균 수심을 같은 값으로 고정하지 않는다. (`Waves/mod_windwave.f90:214` — `AVEDEP = Fetch_Depth(LG,ZONE)              ! *** Get the average depth along the fetch (m)`; `Waves/mod_windwave.f90:218` — `FC0 = (G*AVEDEP/WINDVEL2)**0.75`; `Waves/mod_windwave.f90:237` — `FC0 = TANH(0.833*(G*AVEDEP/WINDVEL2)**0.375)`; EFDC_Theory_Document_Ver_12.pdf, PDF 37쪽·인쇄 24쪽)


— $F$ = fetch length, 16 방향 cell-by-cell 계산.

### 2.7 §2.2.6 Harmonic Forcings (p.25) — 조석 OBC

Open BC 의 조위 시계열 분해 (Eq 2.65):

$$\zeta(t) = \zeta_0(t) + a_0 + \sum_{k=1}^N [a_k \cos(\omega_k t) + b_k \sin(\omega_k t)]$$

amplitude + phase form (Eq 2.67-2.69):
$$\zeta(t) = \zeta_0(t) + a_0 + \sum_k A_k \cos(\omega_k t - \phi_k)$$

문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 38쪽·인쇄 25쪽, 식 2.68; EFDC_Theory_Document_Ver_12.pdf, PDF 38쪽·인쇄 25쪽, 식 2.69)

$$A_k = \sqrt{a_k^2 + b_k^2}, \quad f_k = \arctan(b_k / a_k)$$

진폭과 위상의 식은 문서의 역변환 관계이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 38쪽·인쇄 25쪽) 코드 입력은 진폭과 시간 지연에서 사인·코사인 계수를 만든다. (`input.f90:1227` — `AMP = G*PFAM(NPFORE,M)`; `input.f90:1228` — `PCBE_GL(L,M) = AMP*COS(RAD)`; `input.f90:1229` — `PSBE_GL(L,M) = AMP*SIN(RAD)`; `input.f90:1226` — `RAD = PI2*PFPH(NPFORE,M)/TCP(M)`; EFDC_Theory_Document_Ver_12.pdf, PDF 38쪽·인쇄 25쪽) f_k 표기는 원문에 있고 φ_k와 구분해야 한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 38쪽·인쇄 25쪽) 해석: arctan(b/a)는 사분면 정보를 잃는다(정적 판독, 실행 미확인). (EFDC_Theory_Document_Ver_12.pdf, PDF 38쪽·인쇄 25쪽) 확인한 코드에서 이 역변환 계산은 찾지 못했다. (`input.f90:1227` — `AMP = G*PFAM(NPFORE,M)`; `input.f90:1228` — `PCBE_GL(L,M) = AMP*COS(RAD)`; `input.f90:1229` — `PSBE_GL(L,M) = AMP*SIN(RAD)`; `input.f90:1226` — `RAD = PI2*PFPH(NPFORE,M)/TCP(M)`; EFDC_Theory_Document_Ver_12.pdf, PDF 38쪽·인쇄 25쪽)


— estuary/coastal storm-surge + 조석 superposition.

### 2.8 §2.2.7 Hydraulic Structures (pp.26-29) — Culverts·Weirs·Sluices·Orifices

EFDC+ 의 hydraulic structure: **rating curve** (lookup table) 또는 **physical equation**.

#### Culverts (Dill 2011, 6 cases) — 4 flow regimes (cases a~d):

Manning eq: $Q = AV = AC\sqrt{RS} = K\sqrt{S}$ (Eq 2.70), $C = \frac{1}{n}R^{1/6}$ (Eq 2.71).

문서의 수리 수심 D=A/수면 폭과 코드 HRAD=A/젖은 둘레를 구분한다. (`mod_hydstructure.f90:956` — `HRAD = FAREA/WETPER                          ! *** HYDRAULIC RADIUS`; EFDC_Theory_Document_Ver_12.pdf, PDF 40쪽·인쇄 27쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 43쪽·인쇄 30쪽) 코드는 HCR=HUD−HRAD/2를 관경 이하로 제한한다. (`mod_hydstructure.f90:273` — `HCR =  HUD - 0.5*HRAD               ! *** Critical depth`; `mod_hydstructure.f90:274` — `HCR = min(HCR,DIA)`; EFDC_Theory_Document_Ver_12.pdf, PDF 40쪽·인쇄 27쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 43쪽·인쇄 30쪽) VCR은 sqrt(9.81HRAD)이다. (`mod_hydstructure.f90:275` — `VCR = SQRT(9.81*HRAD)`; EFDC_Theory_Document_Ver_12.pdf, PDF 40쪽·인쇄 27쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 43쪽·인쇄 30쪽) HCR 제한 뒤에는 문서의 에너지 식을 그대로 보존하지 않는다. (`mod_hydstructure.f90:273` — `HCR =  HUD - 0.5*HRAD               ! *** Critical depth`; `mod_hydstructure.f90:274` — `HCR = min(HCR,DIA)`; EFDC_Theory_Document_Ver_12.pdf, PDF 40쪽·인쇄 27쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 43쪽·인쇄 30쪽) 코드의 오리피스 수두에는 별도 기준 표고와 부분 잠김 보정이 있다. (`mod_hydstructure.f90:494` — `HUD = ZHU - USINV + 0.5*HB  ! *** HUD based on centerline`; `mod_hydstructure.f90:498` — `if( ZHD > USINV )then`; `mod_hydstructure.f90:499` — `QHS = QHS*(1.-HDD/HUD)**0.385`; EFDC_Theory_Document_Ver_12.pdf, PDF 40쪽·인쇄 27쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 43쪽·인쇄 30쪽)

#### Weirs (Eq 2.80, free flow):
$$Q = C_d W \sqrt{2g H_{HW}^3}$$

Submerged (Villemonte 1947, Eq 2.81):
$$Q = \left(1 - \frac{H_{TW}}{H_{HW}}\right)^{0.385} C_d W\sqrt{2g H_{HW}^3}$$

#### Sluice gates (Eq 2.82-2.85):

Super-critical: $Q = C_1 W\sqrt{g(\frac{2}{3}H_{HW})^3}$
Sub-critical: $Q = C_2 W H_{TW}\sqrt{2g(H_{HW} - H_{TW})}$

— $H_{TW}/H_{HW} < 0.64$ 시 supercritical, > 0.68 시 subcritical, between 시 가중평균.

### 2.9 §2.2.8 Propeller Wash (pp.30-31)

DSI 2021. ship traffic 의 sub-grid propeller efflux → momentum source + bed shear stress.

Efflux velocity component (Eq 2.87-2.89):
$$V_i = V_0 \cos(\theta_3 - \theta_1), \quad V_j = V_0 \sin(\theta_3 - \theta_1), \quad \theta_3 = \theta_2 - \frac{\pi}{2}$$

Momentum flux (Eq 2.90-2.91):
$$M_{pi} = |V_i \times A_P| \times V_i \times f_p$$
$$M_{pj} = |V_j \times A_P| \times V_j \times f_p$$

— $f_p$ = momentum effect factor (Kee 2006, Hamill-Kee 2016): **0.3 ~ 0.7** range.

---

## 3. §2.3-2.5 Numerical Solution (pp.32-45)

### 3.1 §2.3 Equations of Motion Discretization (pp.32-36)

**Staggered Arakawa C-grid** (Arakawa-Lamb 1977, Peyret-Taylor 1983).

Cell 변수 위치 (Fig 2.6 - 2.7):
- $H, \zeta, A, C$: cell center
- $u$: cell-W·E face
- $v$: cell-N·S face

Finite volume + finite difference 조합.

Modified momentum eq (Eq 2.92, x-방향, hydrostatic 적용 후):

$$\partial_t(m_x m_y H u) + \partial_x(m_y Huu) + \partial_y(m_x Hvu) + \partial_z(m_x m_y wu)$$
$$- \left(v\frac{\partial m_y}{\partial x} - u\frac{\partial m_x}{\partial y}\right) Hv - m_x m_y f H v$$
$$= -m_y H \partial_x p - m_y H g \partial_x \zeta + m_y H g b \partial_x h - m_y H g b z \partial_x H + \partial_z\left(\frac{m_x m_y A_v}{H}\partial_z u\right) + S_u$$

Advection — **central difference** (Eq 2.123) 또는 **upwind** (Eq 2.124, Smolarkiewicz-Clark 1986):

$$\delta_x^u(P_{i,j,k} u_{i,j,k}) = \frac{1}{\Delta x}\left[\max\left(\frac{P_{i+1,j,k} + P_{i,j,k}}{2}, 0\right) u_{i,j,k}^{n-1} - \max\left(\frac{P_{i,j,k} + P_{i-1,j,k}}{2}, 0\right) u_{i-1,j,k}^{n-1}\right]$$
$$+ \frac{1}{\Delta x}\left[\min\left(\frac{P_{i+1,j,k} + P_{i,j,k}}{2}, 0\right) u_{i+1,j,k}^{n-1} - \min\left(\frac{P_{i,j,k} + P_{i-1,j,k}}{2}, 0\right) u_{i,j,k}^{n-1}\right]$$

— upwind: time level $n-1$ velocity (Smolarkiewicz-Clark 1986 stability·accuracy). central: no numerical diffusion, but cell-cell oscillations possible → $A_H$ smoothing 필요.

### 3.2 §2.4 Three-Time Level External Mode (pp.37-41)

External mode = depth-integrated mode (long surface gravity wave).

External mode eq (Eq 2.101): K cells 적분.

핵심 — **Helmholtz elliptic equation** for free surface displacement (Eq 2.132):


해석 수정식 (EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽, 식 2.96; EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽, 식 2.100; EFDC_Theory_Document_Ver_12.pdf, PDF 48쪽·인쇄 35쪽, 식 2.102; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽, 식 2.113; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽, 식 2.116; EFDC_Theory_Document_Ver_12.pdf, PDF 51쪽·인쇄 38쪽, 식 2.117; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽, 식 2.118; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽, 식 2.119; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽, 식 2.132; EFDC_Theory_Document_Ver_12.pdf, PDF 56쪽·인쇄 43쪽, 식 2.134; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽, 식 2.144)

$$\zeta^{n+1} - g\Delta t^2 \left(\frac{1}{m}\right)^\zeta \left[\delta_x^\zeta\left(\frac{Hm_y}{m_x}\right)^u \delta_x^u \zeta^{n+1} + \delta_y^\zeta\left(\frac{Hm_x}{m_y}\right)^v \delta_y^v \zeta^{n+1}\right] - \phi = 0$$

노트의 아래 Helmholtz 식은 PDF의 둘째 바깥 δx를 δy로 바꾼 해석 수정식이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 48쪽·인쇄 35쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 51쪽·인쇄 38쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 56쪽·인쇄 43쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽)


— **Conjugate Gradient (CG)** with multicolor/red-black ordering (Hageman-Young 1981) 으로 풀이. CG iteration 은 squared residual sum < threshold 까지.

### 3.3 §2.5 Three-Time Level Internal Mode (pp.42-45) — Fractional Step

Internal mode = vertical current 구조. Fractional step (Peyret-Taylor 1983):

#### Step 1 (explicit, Eq 2.133-2.134):

$$(P_{k+1} - P_k)^{**} = (P_{k+1} - P_k)^{n-1} - 2\Delta t \left[\text{advection} + \text{Coriolis} + \text{pressure gradient} + \text{source}\right]$$

#### Step 2 (implicit, Eq 2.138-2.139):

$$\frac{(P_{k+1} - P_k)^{n+1}}{m_y^u \Delta_{k+1,k}} = \frac{(P_{k+1} - P_k)^{**}}{m_y^u \Delta_{k+1,k}} + 2\Delta t \left[\frac{(\tau_{xz})_{k+1} - (\tau_{xz})_k}{\Delta_{k+1}\Delta_{k+1,k}} - \frac{(\tau_{xz})_k - (\tau_{xz})_{k-1}}{\Delta_k \Delta_{k+1,k}}\right]^{n+1}$$

— Tri-diagonal system → **Sherman-Morrison formula** (Press et al. 1986) 로 풀이.

#### Bottom stress (Eq 2.146-2.148):

$$(\tau_{xz})_0^{n+1} = C_b \sqrt{(u_1)^2 + (v_1)^2}^n \frac{P_1^{n+1}}{m_y^u H^u}$$

다층 로그는 1+반층 두께/조도이다. (`caltbxy.f90:601` — `DZHUDZBR = 1. + SGZUU(L,KSZU(L))*HURTMP/ZBRATU(L)`; `caltbxy.f90:602` — `DZHVDZBR = 1. + SGZVV(L,KSZV(L))*HVRTMP/ZBRATV(L)`; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽) 저면 계수의 SGZ 조건과 안정성 상한은 별도 분기이다. (`caltbxy.f90:545` — `STBX(L) = min(CDMAXU, STBX(L) )`; `caltbxy.f90:546` — `STBY(L) = min(CDMAXV, STBY(L) )`; `caltbxy.f90:601` — `DZHUDZBR = 1. + SGZUU(L,KSZU(L))*HURTMP/ZBRATU(L)`; `caltbxy.f90:602` — `DZHVDZBR = 1. + SGZVV(L,KSZV(L))*HVRTMP/ZBRATV(L)`; EFDC_Theory_Document_Ver_12.pdf, PDF 30쪽·인쇄 17쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽)

#### Vertical velocity (Eq 2.150):

$$w_k = w_{k-1} - \frac{\Delta_k}{m^\zeta}\left[\delta_x^\zeta(P_k - \hat{P}) + \delta_y^\zeta(Q_k - \hat{Q})\right]$$

— $k=1$ 부터 (no-slip bottom $w_0 = 0$). 주기적 2-time-level correction.

---

## 4. §2.6 Vertical Layering Options (pp.46-47) — **SIG vs SGZ 결정**

### 4.1 §2.6.1 Standard Sigma (SIG, p.46)

- **Topographically conformal** — domain 전체 동일한 vertical layer 수 $K$
- 천해·심해 동시 uniform vertical resolution
- Wide range of applications 적합 (단순 geometry + smooth bathymetry)
- **단점**: **Internal pressure gradient errors** (Mellor et al. 1994) — 가파른 bathymetry slope 에서 horizontal pressure gradient term 의 numerical error 가 spurious flow 유발

### 4.2 §2.6.2 Sigma-Zed (SGZ, p.47)

**Craig et al. 2014** — SIG 의 한계 해결.

| 구분 | SIG | SGZ |
|---|---|---|
| Vertical layer 수 | domain 전체 동일 K | **cell 별로 다른 layer 수** |
| 좌표 | sigma-stretched, terrain-following | sigma + z hybrid |
| Pressure gradient error | 가파른 bathymetry 에서 큼 | 크게 감소 |
| Face matching | 동일 layer | **active layer face matching** (GVC 와 fundamental 차이) |
| 계산 시간 | 표준 | **SGZ 가 더 빠를 수 있음** (large layer 수 가능) |

**3가지 SGZ sub-option** (Fig 2.9):
- (a) **SIG** — Standard Sigma stretch 10 layer
- (b) **SGZ-Specified Bottom** — cell 별 user-specified layer 수
- (c) **SGZ-Uniform Layering** — bottom 의 layer thickness uniform horizontal alignment

**EEMS 12.1 신규** — **Sigma-Zed (SGZ Specified Thickness from Top)** — top 부터 actual layer thickness (m) 로 지정.

### 4.3 사용자 결정 가이드

| 상황 | 권장 |
|---|---|
| Smooth bathymetry estuary, 단순 geometry | **SIG** |
| 가파른 slope (deep reservoir, navigation channel in shallow estuary) | **SGZ** (b) Specified Bottom |
| 매우 깊은 domain + 표면층 정밀 분해 | **SGZ Specified Thickness from Top** (EEMS 12.1+) |
| 한국 항만 (얕은 dredged channel + 천해 평면) | **SGZ** |

---

## 5. 한국·EFDC 운영 관점 매핑

### 5.1 식 ↔ 입력 키 cross-walk (Theory v12 ↔ User Manual r850)

| Theory v12 식·옵션 | 영향 입력 키 |
|---|---|
| §2.1.4 Vertical closure (Mellor-Yamada 4 옵션) | `MMTRMODELS` (turbulence model 선택) |
| §2.1.5 Smagorinsky $C_s$ | `AHO` (horizontal momentum diffusion ref), `AHD` (Smagorinsky 선택) |
| §2.2.1 Bottom friction $z_0$ | `ZBR` (bottom roughness), `ISWAVE` (wave action 활성) |
| §2.2.3 Wind drag option 1-5 | `IWDRAG` |
| §2.2.4-2.2.5 Wave action | `ISWAVE`, `IFWAVE` (SWAN linkage on/off) |
| §2.2.6 Harmonic forcings | `ISMRMC`, `IBNDR` (open boundary radiation) |
| §2.2.7 Hydraulic structures | `ISTRGW` (gate operation rules) |
| §2.2.8 Propeller wash | `ISPROPWASH` |
| §2.6.1 SIG | `ISSGZIJ = 0` |
| §2.6.2 SGZ | `ISSGZIJ = 1` (Specified Bottom), `=2` (Uniform), `=3` (Specified Thickness from Top, EEMS 12.1+) |

→ 상세 입력 키는 [[efdc-user-manual-r850]] 참조.

### 5.2 한국 storm-surge 적용 시 권장 셋팅 (Theory v12 식 level)

| 항목 | 권장 | 근거 (Theory v12) |
|---|---|---|
| Wind drag | Option 1 piecewise OR Option 4 COARE 3.6 | Eq 2.38·2.42-2.44, Garratt/Large-Pond 표준 (Table 2.2) |
| Bottom roughness $z_0$ | 0.005-0.02 m (한국 서해·남해 mud), 0.02-0.05 m (남해 sand) | Eq 2.31 |
| Vertical closure | Mellor-Yamada 1982 or Galperin 1988 | Table 2.1, 가장 검증된 |
| Wave coupling | SWAN external (NWS=13 + ADCIRC 와 일관) | §2.2.4 External SWAN |
| Vertical layering | SIG 10 layers (천해 항만) / SGZ (수심 변화 큰 외해) | §2.6 결정표 |

### 5.3 §2.1.5 의 $C_s$ 선택 — 한국 실무

- 한국 항만 (격자 < 100 m): $C_s = 0.1$ (작은 격자, dissipation 적게)
- 외해 (격자 > 500 m): $C_s = 0.15-0.2$ (Smagorinsky 표준)
- Theory v12 명시: $C_s$ 는 **flow + grid 모두에 의존하는 uncertain quantity** (Meyers-Sagaut 2006) — calibration 필요

---

## 6. 인용 핵심 reference (Theory v12 본문에서 직접)

primary sources of Ch 2 (각 식 옆 인용):

1. **Hamrick (1992)** — 전체 EFDC 기반
2. **Ji (2008)** — *Hydrodynamics and Water Quality* (CRC) — Ch 2 의 보조 reference
3. **Mellor-Yamada (1982)** — Level 2.5 turbulence closure (§2.1.4)
4. **Galperin et al. (1988)** — closure constants 수정 (§2.1.4, Table 2.1)
5. **Kantha-Clayson (1994)** — alternative closure (Table 2.1)
6. **Kantha (2003)** — updated closure (Table 2.1)
7. **Smagorinsky (1963)** — horizontal subgrid closure (Eq 2.27)
8. **Blumberg-Mellor (1987), Vinokur (1974), Hamrick (1986)** — sigma transformation (Eq 2.1)
9. **UNESCO (1981)** — EOS (Eq 2.12)
10. **Nezu (1993)** — bottom friction log-law (Eq 2.31)
11. **Fairall et al. (1996, 2003), Edson et al. (2013)** — COARE 3.6 (Eq 2.42-2.44)
12. **Hersbach (2011)** — ECMWF wind drag (Eq 2.41)
13. **Longuet-Higgins-Stewart (1964)** — wave radiation stress (Eq 2.46-2.48)
14. **Hunt (1979)** — dispersion 근사 (Eq 2.53)
15. **Swart (1974)** — wave bottom friction (Eq 2.60)
16. **Dill (2011)** — culvert flow types (§2.2.7.2)
17. **Villemonte (1947)** — submerged weir (Eq 2.81)
18. **Arakawa-Lamb (1977), Peyret-Taylor (1983)** — C-grid + fractional step
19. **Smolarkiewicz-Clark (1986)** — upwind discretization (Eq 2.124)
20. **Hageman-Young (1981)** — Conjugate Gradient solver
21. **Press et al. (1986)** — Sherman-Morrison
22. **Mellor et al. (1994)** — SIG pressure gradient error
23. **Craig et al. (2014)** — SGZ 도입
24. **DSI (2021)** — propeller wash white paper
25. **Tetra Tech (2007a)** — sediment density correction (Eq 2.13)
26. **Plew (2011), Scott-O'Donncha (2019)** — vegetation drag fitting

---

## 7. 후속 노트 후보 (proportional)

본 노트는 Ch 2 의 **식 + 옵션 + 결정표** 수준. 추가 deep 시:

- `efdc-theory-v12-ch5-temperature.md` — §5.1.2 COARE 3.6 + §5.4 ice + §5.2 light attenuation (Paulson-Simpson 1977 Table 5.1)
- `efdc-theory-v12-ch6-sediment.md` — §6.3 SedTran + §6.4 SEDZLJ equation level
- `efdc-mellor-yamada-vs-kantha-comparison.md` — Table 2.1 의 4 옵션 한국 실무 선택 guide

---

## 8. 관련 자료

- [[efdc-theory-doc-v12]] — Ch 2 모든 nav + TOC
- [[efdc-user-manual-r850]] — 입력 키 매핑
- [[efdc-manuals-overview]] — 6 manuals 인덱스
- [`models/EFDC/source-analysis/`](../source-analysis/) — Fortran source ↔ Theory v12 식 매핑
- [`concepts/storm-surge/02-theory.md`](../../../concepts/storm-surge/02-theory.md) — Pugh + ADCIRC GWCE 식 level (cross-ref 가능)
- [`concepts/sst/04-code-and-tools.md`](../../../concepts/sst/04-code-and-tools.md) — COARE 3.6 운영 데이터
- 외부 (Theory v12 본문 인용):
  - Hamrick 1992 — VIMS Special Report 317
  - Ji, Z.G. (2008) — *Hydrodynamics and Water Quality* (Wiley)
  - Mellor-Yamada 1982 — *Rev. Geophys.* 20:851-875
  - Craig et al. 2014 — DSI internal doc
  - Fairall et al. 2003 — *J. Climate* 16:571-591

## 근거리 방류(식 2.151–2.181)

문서 2장의 번호 식은 2.1–2.181이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 62쪽·인쇄 49쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 63쪽·인쇄 50쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 64쪽·인쇄 51쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 65쪽·인쇄 52쪽) ISENT=0의 연행은 두 항의 최댓값이다. (`Transport/mod_diffuser.f90:1008` — `if( JET_PLM(NJP).ISENT == 0 )then`; `Transport/mod_diffuser.f90:1010` — `DRMAJ = max(DRMAJSA,DRMAJFA)`; EFDC_Theory_Document_Ver_12.pdf, PDF 62쪽·인쇄 49쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 63쪽·인쇄 50쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 64쪽·인쇄 51쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 65쪽·인쇄 52쪽) 연행 계수의 부호와 초기 밀도 차 참조는 식 2.157과 다르다. (`Transport/mod_diffuser.f90:979` — `FRD2I = FTOP/(ALPH2*DVEL*DVEL)`; `Transport/mod_diffuser.f90:980` — `EBOT = 1. + 5.*RDQA(1)/DVEL`; `Transport/mod_diffuser.f90:981` — `ETOP = 0.057 + 0.554*SINPHJ*FRD2I`; `Transport/mod_diffuser.f90:982` — `ENTS = 1.414*ETOP/EBOT`; EFDC_Theory_Document_Ver_12.pdf, PDF 63쪽·인쇄 50쪽, 식 2.157) 제트 밀도는 TSS를 포함한다. (`Transport/mod_diffuser.f90:1101` — `RHOJ(N2) = FUNDEN(SALJ(N2),SEDJETT,TEMJ(N2))`; `Transport/mod_diffuser.f90:1659` — `RHO = RHO*( (1. - SDEN*SEDIN) + (SSG - 1.)*SDEN*SEDIN )`; EFDC_Theory_Document_Ver_12.pdf, PDF 62쪽·인쇄 49쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 63쪽·인쇄 50쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 64쪽·인쇄 51쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 65쪽·인쇄 52쪽) 주변 y·z 운동량을 혼합한다. (`Transport/mod_diffuser.f90:1105` — `VJG(N2) = RMAJI*( RMAJP(N1)*VJG(N1) + DRMAJ*VAG )                   ! ***`; `Transport/mod_diffuser.f90:1107` — `WJG(N2) = RMAJI*( RMAJP(N1)*WJG(N1) + DRMAJ*WAG ) + G*DRHO*DTJP     ! ***`; EFDC_Theory_Document_Ver_12.pdf, PDF 62쪽·인쇄 49쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 63쪽·인쇄 50쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 64쪽·인쇄 51쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 65쪽·인쇄 52쪽) 수직 부력 갱신은 문서의 연행 질량 가중과 다르다. (`Transport/mod_diffuser.f90:1102` — `DRHO = (RHOA(N2) - RHOJ(N2))/RHOA(N2)`; `Transport/mod_diffuser.f90:1107` — `WJG(N2) = RMAJI*( RMAJP(N1)*WJG(N1) + DRMAJ*WAG ) + G*DRHO*DTJP     ! ***`; EFDC_Theory_Document_Ver_12.pdf, PDF 62쪽·인쇄 49쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 63쪽·인쇄 50쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 64쪽·인쇄 51쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 65쪽·인쇄 52쪽) 수평 방향각은 ATAN2를 사용한다. (`Transport/mod_diffuser.f90:1162` — `THJG(N2) = 57.2958*ATAN2(VJG(N2),UJG(N2))                             ! *** Horizontal angle of the jet`; EFDC_Theory_Document_Ver_12.pdf, PDF 62쪽·인쇄 49쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 63쪽·인쇄 50쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 64쪽·인쇄 51쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 65쪽·인쇄 52쪽)
