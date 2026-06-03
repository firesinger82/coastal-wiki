---
title: "SWAN output variable definitions (swanuse Appendix A) — HSIGN/TM01/TM02/TMM10/DIR/DSPR/QP/BFI/FORCE 적분식 verbatim + MS↔DSPR Table A.1 + Cartesian/Nautical convention"
topic: swan
canonical_source: external
external_source: "swanuse (User Manual, SWAN Cycle III version 41.51) Appendix A 'Definitions of variables' (p.115-120, node35.md). 모든 SWAN input/output 변수의 적분 정의. refs: Kuik et al.(1988) DIR/DSPR, Battjes-Van Vledder(1984) FSPR, Battjes-Janssen(1978) QB."
citation_status: verified
verification_method: "models/SWAN/raw/manuals/website_markdown/online_doc/swanuse/node35.md 직접 read. 각 변수 적분식 LaTeX verbatim + MS↔DSPR Table A.1 23행 verbatim + Cartesian/Nautical 정의 verbatim. swantech Eq(2.11-2.12 H_s/period, 3.59-61 radiation stress) + command QUANTITY default와 cross-check."
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 출력변수 적분식 verbatim, 이론 Eq ↔ output quantity 정합"
verification_date: 2026-06-03
related:
  - models/SWAN/manual-notes/swan-command-numerics-output-reference.md
  - models/SWAN/source-analysis/swan-output-formats.md
  - models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md
  - models/SWAN/manual-notes/swan-usage-general.md
---

# SWAN output variable definitions (swanuse Appendix A) — verified

> swanuse Appendix A (User Manual 41.51, p.115-120 / node35) 직접 read. SWAN **BLOCK/TABLE/QUANTITY 출력 quantity 의 공식 정의**(적분식). 본 노트 = output **변수의 의미**(canonical), [[swan-output-formats]] = output **파일 dispatch 메커닉**(source-code), [[swan-command-numerics-output-reference]] = output **command 구문**. swantech 이론 Eq 와 정합.

> 모든 적분은 표기상 $\iint = \int_0^{2\pi}\int_0^\infty$. **계산 편의상 $\omega$(절대) 대신 $\sigma$(상대) 적분으로 대체 가능**(무전류 시 동일). $E$ = variance density spectrum.

## 1. 파고 (height)

| 변수 | 정의 |
|---|---|
| **HSIGN** | Significant wave height $H_s$ (m): $H_s = 4\sqrt{\iint E(\omega,\theta)\,d\omega\,d\theta}$. 편의상 $H_s = 4\sqrt{\iint E(\sigma,\theta)\,d\sigma\,d\theta}$. (= swantech **Eq 2.11** $H_s=4\sqrt{m_0}$, [[swan-tech-ch2-governing-equations]]) |
| **HSWELL** | swell(저주파) significant height: $H_{s,\rm swell}=4\sqrt{\int_0^{\omega_{\rm swell}}\int_0^{2\pi}E\,d\omega\,d\theta}$. $f_{\rm swell}=0.1$ Hz **default**(QUANTITY 로 변경). |

## 2. 주기 (period) — 절대 $\omega$ vs 상대 $\sigma$ ★

전류 있으면 **절대(absolute, $\omega$) ≠ 상대(relative, $\sigma$)**; 무전류 시 동일.

| 변수 | 정의 (moment 비) |
|---|---|
| **TMM10** | $T_{m-10}=2\pi\frac{\iint \omega^{-1}E\,d\omega\,d\theta}{\iint E\,d\omega\,d\theta}$ (절대, energy period) |
| **TM01** | $T_{m01}=2\pi\left(\frac{\iint \omega E\,d\omega\,d\theta}{\iint E\,d\omega\,d\theta}\right)^{-1}$ (절대) |
| **TM02** | $T_{m02}=2\pi\left(\frac{\iint \omega^2 E\,d\omega\,d\theta}{\iint E\,d\omega\,d\theta}\right)^{-1/2}$ (절대, zero-crossing) |
| **RTMM10 / RTM01** | 위의 $\sigma$(상대) 버전. 무전류 시 = TMM10/TM01 |
| **RTP** | Relative peak period (s) of $E(\sigma)$ — **이산 스펙트럼 absolute max bin** 기준(실제 peak 와 다를 수 있음) |
| **TPS** | Relative peak period (s) — **highest bin ± 2 bin 포물선 fit** ('smoothed', RTP 보다 'real' peak 의 더 나은 추정) |
| **PER** | $T_{m,p-1,p}=2\pi\frac{\iint \omega^{p-1}E}{\iint \omega^p E}$ (절대). **QUANTITY 의 $p$**: $p=1$(default)→PER=TM01, $p=0$→PER=TMM10 |
| **RPER** | PER 의 $\sigma$ 버전. $p=1$→RTM01, $p=0$→RTMM10 |

→ TM01/TM02/TMM10 정의는 swantech **Eq 2.12** ([[swan-tech-ch2-governing-equations]] §moments)와 동일.

## 3. 방향 (direction) — Kuik et al. 1988

| 변수 | 정의 |
|---|---|
| **DIR** | Mean wave direction (°, Cartesian/Nautical): $\rm DIR=\frac{180}{\pi}\arctan\left(\frac{\int\sin\theta E\,d\sigma\,d\theta}{\int\cos\theta E\,d\sigma\,d\theta}\right)$. **wave crest 에 수직** 방향. (Kuik et al. 1988) |
| **PDIR** | Peak direction of $E(\theta)=\int E\,d\omega=\int E\,d\sigma$ (°) |
| **TDIR** | Direction of **energy transport** (°). 전류 있으면 DIR 과 다름 |

## 4. 스펙트럼 폭·형태 (spread / shape)

| 변수 | 정의 |
|---|---|
| **FSPR** | Normalized frequency width (frequency spreading), Battjes-Van Vledder 1984: $\rm FSPR=\frac{\lvert\int_0^\infty E(\omega)e^{i\omega\tau}d\omega\rvert}{E_{\rm tot}}$, $\tau=T_{m02}$ |
| **DSPR** | One-sided directional width (directional spreading / std, °): $\rm DSPR^2=(\frac{180}{\pi})^2\int_0^{2\pi}(2\sin\frac{\theta-\bar\theta}{2})^2 D(\theta)d\theta$. WAVEC pitch-and-roll buoy 관례(Kuik et al. 1988): $(\rm DSPR\frac{\pi}{180})^2=2(1-\sqrt{(\frac{\int\sin\theta E}{\int E})^2+(\frac{\int\cos\theta E}{\int E})^2})$ |
| **QP** | Peakedness (Goda): $Q_p=2\frac{\iint \sigma E^2\,d\sigma\,d\theta}{(\iint E\,d\sigma\,d\theta)^2}$. **작을수록 wide spectrum / 더 random**(짧은 wave group), 클수록 narrow / 조직적(긴 group) |
| **MS** | BOUNDPAR/BOUNDSPEC 입력 시 방향분포 $D(\theta)=A(\cos\theta)^m$ 의 power $m$(정수 아니어도 됨). DSPR 와 **Table A.1** 대응 |

**Table A.1** (MS ↔ DSPR°): 1→37.5 / 2→31.5 / 3→27.6 / 4→24.9 / 5→22.9 / 6→21.2 / 7→19.9 / 8→18.8 / 9→17.9 / 10→17.1 / 15→14.2 / 20→12.4 / 30→10.2 / 40→8.9 / 50→8.0 / 60→7.3 / 70→6.8 / 80→6.4 / 90→6.0 / 100→5.7 / 200→4.0 / 400→2.9 / 800→2.0.

## 5. 에너지 수지 (energy balance) — 단위 W/m² 또는 m²/s (SET 의존)

| 변수 | 정의 |
|---|---|
| **PROPAGAT** | $\vec x$-, $\theta$-, $\sigma$-space 단위시간당 에너지 전파 |
| **GENERAT** | wind input 에 의한 생성 |
| **REDIST** | quadruplet + triad 합에 의한 재분배 |
| **DISSIP** | bottom friction + whitecapping + depth-induced surf breaking 합에 의한 소산 |
| **RADSTR** | radiation stress 가 한 일: $\iint\lvert\nabla_{(\sigma,\theta)}\cdot(\vec c_{(\sigma,\theta)}E)\rvert\,d\sigma\,d\theta$ |

## 6. 수송·force·radiation stress

| 변수 | 정의 |
|---|---|
| **TRANSP** | Energy transport $P_x=\rho g\iint c_x E\,d\sigma\,d\theta$, $P_y=\rho g\iint c_y E\,d\sigma\,d\theta$. $x,y$=problem coord (단, BLOCK+FRAME 시 frame 축) |
| **VEL / WIND** | current / wind velocity $x,y$ 성분 (problem coord; BLOCK+FRAME 시 frame 축) |
| **FORCE** | wave-induced force(radiation stress gradient): $F_x=-\frac{\partial S_{xx}}{\partial x}-\frac{\partial S_{xy}}{\partial y}$, $F_y=-\frac{\partial S_{yx}}{\partial x}-\frac{\partial S_{yy}}{\partial y}$ |

**Radiation stress tensor** (= swantech **Eq 3.59-3.61**, [[swan-tech-ch3-qc-curvilinear]]):
$$S_{xx}=\rho g\int(n\cos^2\theta+n-\tfrac12)E\,d\sigma\,d\theta,\quad S_{xy}=S_{yx}=\rho g\int n\sin\theta\cos\theta\,E,\quad S_{yy}=\rho g\int(n\sin^2\theta+n-\tfrac12)E$$
$n$ = group velocity / phase velocity ($n=c_g k/\omega$, Eq 3.62).

## 7. 저면·breaking·setup

| 변수 | 정의 |
|---|---|
| **URMS** | rms orbital velocity near bottom: $U_{\rm rms}=\sqrt{\int_0^{2\pi}\int_0^\infty\frac{\sigma^2}{\sinh^2 kd}E\,d\sigma\,d\theta}$ |
| **UBOT** | $U_{\rm bot}=\sqrt2\,U_{\rm rms}$ (orbital motion maxima 의 rms, m/s) |
| **TMBOT** | near-bottom period $T_b=\sqrt2\pi a_b/U_{\rm rms}$, $a_b=\sqrt{2\int\int\frac{1}{\sinh^2 kd}E\,d\sigma\,d\theta}$ (bottom excursion amplitude) |
| **STEEPNESS** | HSIG/WLEN |
| **WLEN** | mean wave length $\rm WLEN=2\pi\left(\frac{\iint k^p E}{\iint k^{p-1}E}\right)^{-1}$, $p=1$ default (QUANTITY) |
| **BFI** | Benjamin-Feir index (steepness-over-randomness): $\rm BFI=\sqrt{2\pi}\times STEEPNESS\times QP$. **freak wave 확률** 정량화 |
| **QB** | Battjes-Janssen 1978 식의 breaker fraction (= swantech §2.3.3 $Q_b$, [[swan-tech-ch2-dissipation-detailed]]) |
| **SETUP** | radiation stress gradient 에 의한 평균수위 상승(still water level 대비) |
| **LEAK** | directional sector 경계 $\theta_1$/$\theta_2$(CGRID)를 가로지르는 $c_\theta E$ 수치 에너지 손실 |

## 8. 시간

- **TIME** = full date-time string / **TSEC** = reference time(QUANTITY) 대비 초.

## 9. 방향 convention (Appendix A 말미 verbatim) ★

- **Cartesian**: 벡터와 +$x$축 사이 각, **반시계**. = 파/바람이 **향하는(going to)** 방향.
- **Nautical**: 지리적 북(N)에서 **시계**. = 파/바람이 **오는(coming from)** 방향.

→ [[swan-usage-general]] §2.5 units/convention 와 동일(SET NAUTICAL/CARTESIAN). 계산격자 방향은 항상 Cartesian.

## 10. 연결

- [[swan-command-numerics-output-reference]] — BLOCK/TABLE/QUANTITY command (이 변수들을 출력 지정; QUANTITY 가 $p$·$f_{\rm swell}$·reference time 조정)
- [[swan-output-formats]] — output 파일 dispatch·format 메커닉(source-code)
- [[swan-tech-ch2-governing-equations]] — Eq 2.11 $H_s$ / Eq 2.12 period moments 정의 출처
- [[swan-tech-ch3-qc-curvilinear]] — Eq 3.59-3.64 radiation stress $S_{xx/xy/yy}$ + force
- [[swan-tech-ch2-dissipation-detailed]] — QB Battjes-Janssen
- [[swan-usage-general]] — §2.5 Cartesian/Nautical convention
- [[swan-documentation-stack]] §7 한계의 "Appendix A cross-walk" 충족
