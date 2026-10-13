---
title: "SWAN swantech Ch 3.3-3.7 Solution algorithm + iteration/stopping + four-sweep + DIA-in-sweep + action limiter/under-relaxation verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.3 Solution algorithm + §3.4 Iteration process and stopping criteria + §3.5 sweeping + §3.6 DIA in four-sweep + §3.7 Action density limiter and under-relaxation, doc p.79-91 (Eq 3.16-3.30). References: Wesseling 1992, Ferziger-Perić 1999, Booij et al. 1999, Press et al. 1993, Holthuijsen-De Boer 1988, Zijlema-Wesseling 1998, WAMDI 1988, Hargreaves-Annan 2001, Hersbach-Janssen 1999, Tolman 1992·2002, Komen et al. 1994, Ris 1999, De Waal 2001, Janssen 1989·1991a."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §3.3-3.7 직접 read via pdftotext (식 번호 context-verified: matrix 3.16·S_tot linearization 3.17·Newton-Raphson 3.18·a_P 3.19·AN=b 3.20·H_m0 3.21·stopping 3.22-23·curvature 3.25-26·action limiter 3.27·limited update 3.28·under-relax 3.29-30) + website_markdown node42-48.md LaTeX alt-text. 식 번호는 PDF 번호 (online HTML +15 offset).; 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 3.16-3.30 + 계수/default 값 verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch3-discretization.md
  - models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md
  - models/SWAN/source-analysis/swan-source-terms-implementation.md
---

# swantech Ch 3.3-3.7 Solution algorithm + iteration + limiter — verified verbatim

> swantech.pdf (v41.51) §3.3–3.7은 [swan-tech-ch3-discretization](swan-tech-ch3-discretization.md)의 이산화 방정식을 푸는 알고리즘을 설명한다. 이 범위는 Gauss-Seidel four-sweep, SIP 해법, 원천항 선형화, 정지 기준, DIA 적분, 작용밀도 제한기와 주파수 의존 완화를 포함한다. `NUMERIC`의 정지 기준·스펙트럼 해법·제한기 설정은 이 설명과 연결된다. (swantech PDF 87–100쪽 / 인쇄 79–92쪽; swanuse PDF 93–95쪽 / 인쇄 85–87쪽) [10-13 전수 검증 정정]
>
> **식 번호 주의**: PDF 번호 사용 (online HTML은 §3.2 GSE 누적 + 본 절 보조식으로 +15 offset, 예: action limiter HTML 3.42 = PDF 3.27).

## 1. §3.3 Solution algorithm (Eq 3.16-3.20)

Implicit 이산화 → 선형방정식계. Matrix 구조는 geographic 전파 방향 의존 ($c_x>0, c_y>0$ 예):
$$\text{matrix structure (penta-diagonal block)} \quad \text{(3.16)}$$
- 주대각 subblock = 각 geographic 점의 $(\sigma,\theta)$ 공간 coupling, off-diagonal = geographic 점 간 coupling
- wave characteristic 이 직선·일정이면 **Gauss-Seidel 1-step** (Wesseling 1992), 격자크기 무관 → 복잡도 $\mathcal{O}(M)$ ($M$ 격자점)
- 방향을 4 quadrant($90°$)로 분할 → **four sweeps**, 각 sweep 의 방향이 domain of dependence → **CFL 자동 만족** (causality)

### 1.1 비선형 source 선형화 (Ferziger-Perić 1999)

$$S_{\text{tot}} = S_{\text{tot}}^p + S_{\text{tot}}^n N \quad \text{(3.17)}$$
- $S^p$ = 양 기여, $S^n$ = 음 기여 (둘 다 해당 bin 의 $N$ 무관). $N$ 미포함 음항은 이전 iteration 의 $N$ 으로 나눠 $S^n$ 에 추가 → 안정화. 각 source term 적용 상세: Booij et al. (1999).

Depth-induced breaking (강한 비선형) → **Newton-Raphson**:
$$S^n \approx \phi^{n-1}E^{n-1} + \left(\frac{\partial S}{\partial E}\right)^{n-1}(E^n - E^{n-1}) \quad \text{(3.18)}$$
> $S = aS_{\text{tot}}$, $E = aE_{\text{tot}}$ 형태 → $\partial S/\partial E = \partial S_{\text{tot}}/\partial E_{\text{tot}}$ 해석적.

$S=\phi E$의 Newton 식 첫 항은 $\phi^{n-1}E^{n-1}$이다. 문서의 $E^n$을 쓰면 $\phi(E^n-E^{n-1})$를 한 번 더 더한다. (swantech PDF 89쪽 / 인쇄 81쪽, 식 (3.18); `src/swancom2.ftn:2120–2121` `SURFA0 = SbrD`; `SURFA1 = WS + SbrD`; R1:TN-070)

### 1.2 5-점 stencil + SIP solver

$$a_P N_P = a_L N_L + a_R N_R + a_B N_B + a_T N_T + b_P \quad \text{(3.19)}$$
- P=중앙 bin $(l,m)$, L/R/B/T = $(l-1,m)/(l+1,m)/(l,m-1)/(l,m+1)$
- $a_k$ = $c_\sigma N, c_\theta N$ flux 이산화, $b_P$ = $S^p$ + 갱신된 $c_x N (3.3), c_y N (3.4)$, $a_P$ 는 $-S^n$ 포함

방향 quadrant 의 system:
$$A\vec{N} = \vec{b} \quad \text{(3.20)}$$
- $A\in\mathbb{R}^{K\times K}$ ($K = N_\sigma\times\frac{1}{4}N_\theta$), 비대칭, **penta-diagonal**. Source 선형화(3.17)가 diagonal dominance 강화 → 안정성 ↑
- 해: **incomplete LU + SIP (Strongly Implicit Procedure, Ferziger-Perić 1999)** — 비대칭 penta-diagonal 전용, 빠름
흐름이 없어도 시간에 따라 수심이 바뀌면 주파수 이동이 생긴다. 해법 선택은 흐름뿐 아니라 DYNDEP와 주파수 전파 설정도 따른다. (swantech PDF 18쪽 / 인쇄 10쪽, 식 (2.13); swanuse PDF 94–95쪽 / 인쇄 86–87쪽; R1:TN-073; R8:T1-010)

정렬 경로는 먼저 `IF ( IREFR.EQ.0 .AND. ITFRE.EQ.0 ) THEN`의 직접 나눗셈을 선택한다. 이어서 `ELSEIF ( (DYNDEP .OR. ICUR .EQ. 1) .AND.`와 `&           PNUMS(8).NE.0.                 ) THEN`에서 주파수 해법을 선택한다. 나머지에서 SOLMAT를 호출한다. (`src/swancom1.ftn:3656`; `src/swancom1.ftn:3681–3682`; `src/swancom1.ftn:3720–3726`; R8:T1-010)

## 2. §3.4 Iteration process + stopping criteria (Eq 3.21-3.26)

$c_x, c_y$ 부호가 도메인서 달라 다단계 필요. Wave ray 곡선(천수 depth/current refraction) → 1 iteration 불가. Quadrant 간 상호작용(refraction + nonlinear) → sweep + system(3.20) 반복. $s=1\to S$ (보통 $S=50$ max) 또는 수렴기준 충족 시 종료.

$$H_{m0} = 4\sqrt{m_0},\quad T_{m01} = 2\pi\frac{m_0}{m_1},\quad m_j = \int_0^\infty\int_0^{2\pi}\sigma^j E\,d\sigma d\theta \quad \text{(3.21)}$$

### 2.1 종래 기준 (문서의 옛 기준 설명)

전체 wet 격자의 **98% 이상**에서 둘 다 충족:
$$\frac{|\Delta H_{m0}^s(i,j)|}{H_{m0}^{s-1}(i,j)} < \varepsilon_H^r \quad\text{or}\quad |\Delta H_{m0}^s(i,j)| < \varepsilon_H^a \quad \text{(3.22)}$$
$$\frac{|\Delta T_{m01}^s(i,j)|}{T_{m01}^{s-1}(i,j)} < \varepsilon_T^r \quad\text{or}\quad |\Delta T_{m01}^s(i,j)| < \varepsilon_T^a \quad \text{(3.23)}$$
- 문서의 옛 기준 설명은 $\varepsilon_H^r = \varepsilon_T^r = 0.02$, $\varepsilon_H^a = 0.02$ m, $\varepsilon_T^a = 0.2$ s이다. (swantech PDF 91쪽 / 인쇄 83쪽; R1:TN-077)
- 첫 추정: Holthuijsen-De Boer (1988) 2nd-gen source 로 가속

> swantech의 제안된 개선 기준은 “Tm01 has been abandoned as a convergence measure and only Hm0”라고 적는다. (swantech PDF 91쪽 / 인쇄 83쪽; R8:T1-003)

현행 일반 STOPC에는 주기 검사가 남는다. 기본 1000 값은 이 검사를 느슨하게 한다. 정렬 곡률은 평균 각주파수로 계산하고 비정렬 곡률은 주기로 계산한다. (`src/swancom1.ftn:9877–9878` `( TMCURV.LE.PNUMS(16) .AND.`; `&                     (TMREL.LE.PNUMS(1) .OR. TMABS.LE.PNUMS(3)) )`; R1:TN-081)

정렬 STOPC의 TMREL은 주기 차이를 평균 각주파수로 나눈다. 이 값의 차원은 s²이며 무차원 상대오차가 아니다. 일반 STOPC 경로의 강한 결함 후보이다. QC 분기는 이 값을 합격 조건에 쓰지 않는다. (`src/swancom1.ftn:9813` `SACC2 (INDX) = MAX ( 1.E-20 , (XMOM1/XMOM0) )`; `src/swancom1.ftn:9854–9855` `TMABS = ABS ( (PI2/SACC2(INDX)) - (PI2/SACC1(INDX)) )`; `TMREL = TMABS / SACC2(INDX)`; R1:TN-076; R8:T1-011)

### 2.2 Spectral radius 통찰 (Ferziger-Perić 1999)

$$\phi^\infty - \phi^s \approx \frac{\phi^{s+1}-\phi^s}{1-\rho} \quad \text{(3.24)}$$
> $\rho$ = spectral radius (수렴률). $\rho$ 작을수록 빠름. **해 오차 > 연속 iterate 차** — $\rho\to1$ 일수록 비율 커짐. SWAN 은 nonlinear transfer 로 smooth 하지 않아 Zijlema-Wesseling(1998) 류 기준 부적합.

### 2.3 Curvature 기준 (41.01+ default)

수렴 시 iteration curve 곡률 → 0:
$$\Delta(\Delta\tilde{H}_{m0}^s)^s = \tilde{H}_{m0}^s - 2\tilde{H}_{m0}^{s-1} + \tilde{H}_{m0}^{s-2} \quad \text{(3.25)}$$
> $\tilde{H}_{m0}^s \equiv (H_{m0}^s + H_{m0}^{s-1})/2$ (소진폭 진동 제거)

$$\frac{\lvert H_{m0}^{s}(i,j)-(H_{m0}^{s-1}(i,j)+H_{m0}^{s-2}(i,j))+H_{m0}^{s-3}(i,j)\rvert}{2H_{m0}^{s}(i,j)}<\varepsilon_{\mathrm C},\quad s=3,4,\cdots \quad \text{(3.26)}$$

(swantech PDF 92쪽 / 인쇄 84쪽; R8:N1-010)
기술 문서는 “at least 99% of all wet grid points”라고 적는다. 일반 STOPC의 기본 합격점 비율은 99.5%이다. GEN4 입력과 IGEN=4의 ACCUR 전환 경로는 99%를 설정한다. (swantech PDF 92쪽 / 인쇄 84쪽; swanuse PDF 94쪽 / 인쇄 86쪽; `src/swanmain.ftn:1227` `PNUMS(4)  = 99.50`; `src/swanpre1.ftn:3107` `PNUMS(4) = 99.`; R8:T1-002)

코드의 일반 기본값은 상대 0.01, 파고 절대 0.005 m이다. 파고 절대 허용값은 미지정일 때 `ITRIAD=3`에서 0.01 m이다. QC의 0.05는 입사파고에 곱하는 무차원 계수이다. (swanuse PDF 94쪽 / 인쇄 86쪽; `src/swanmain.ftn:1219` `PNUMS(1)  = 0.01`; `src/swanmain.ftn:6503–6512`; R1:TN-077)

일반 STOPC의 파고 조건은 절대 차이 충족 또는 상대 차이와 곡률의 동시 충족이다. 파고 곡률은 모든 합격점의 필수 조건이 아니다. (`src/swancom1.ftn:9874–9875` `LCONV = ( HSABS.LE.PNUMS(2) .OR.`; `&                     (HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)) )`; R1:TN-080; R8:T1-004)

## 3. §3.5 Four-sweep technique (illustrative)

무전류: energy 전파방향 = 군속도. Upwind stencil — $(x_i,y_j)$ 는 up-wave $(x_{i-1},y_j), (x_i,y_{j-1})$ 로 결정 → $0°$-$90°$ sector = **sweep 1**. Stencil $90°$ 회전 4회 → 4 quadrant 전파. **Unconditionally stable** (characteristic 가 quadrant 내) → **CFL 무관**. Causality: geographic + spectral domain of dependence 동일.

Refraction 시 quadrant 간 action shift → 반복 (iterative four-sweep). STOPC의 개별 비교는 허용값과 같은 값도 허용한다. 합격점 백분율은 0.01 퍼센트포인트 단위로 올려 npnts 이상인지 비교한다. 첫 반복에는 이 수렴 종료를 적용하지 않는다. (`src/swancom1.ftn:9875` `HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)`; `src/swancom1.ftn:9928` `ACCUR  = CEILING(REAL(IACCUR) * 10000. / REAL(WETGRD))/100.`; `src/swancom1.ftn:2352–2353` `IF ( (ITER.NE.1 .OR. PNUMS(21).EQ.0.) .AND.`; `&                                      ACCUR.GE.PNUMS(4) ) GOTO 470`; R8:T1-006)

> **$M>4$ sweep 옵션**: 방향간격 $360°/M$. 심해(직선 ray)는 iteration 감소 가능 (8 sweep $45°$ / 12 sweep $30°$). **천수에선 역효과** — refraction 으로 wave energy 가 1 step 에 여러 bin jump → sweep sector 조기 이탈/skip ($<30°$ + 큰 depth 변화 시) → ray 교차·causality 위반·불안정 (§3.8.3 참조).

### 3.1 전류 존재 시 4 configurations

$c_x = c_{g,x}+U_x$, $c_y = c_{g,y}+U_y$. Sweep 별 부호 분류 (1: ++, 2: -+, 3: --, 4: +-). 고주파일수록 군속도 작아 current 영향 大 → sector 경계 변화 大. **4 config** (current $45°$ 예, Fig 3.3):
- **(A)** 강한 역류 → $c_x,c_y$ 모두 음 (wave blocking), sweep 1 에 아무것도 전파 안 됨
- **(B)** 약한 current → sector 경계 거의 무변 (무전류와 유사)
- **(C)** 순류 → 2 sector 가 양 전파속도
- **(D)** 강한 순류 → 전 $360°$ sector 가 sweep 1 에 전파

## 4. §3.6 DIA in four-sweep — 2 methods

Quadruplet 은 DIA(§2.3.4, [swan-tech-ch2-nonlinear-detailed](swan-tech-ch2-nonlinear-detailed.md))로 적분. Four-sweep 결과 2 방식:

| 방식 | 시점 | 비용 | 보존 | current |
|---|---|---|---|---|
| **Method 1** | 정렬 IQUAD=3은 SOURCE에서 전 방향 원천항을 계산해 MEMNL4에 저장한다. 첫 반복은 각 sweep의 SOURCE 방문마다 계산한다. 이후 반복은 아래 SWPDIR·경계점 조건을 따른다. | 문서의 메모리 약 2배 설명 (H) | 문서의 에너지 보존 설명 | ambient current 시 IQUAD=3 권고 |
| **Method 2** | sweep 별 개별 계산·적분 (인접 2 quadrant 약 $33°$ 추가) | 문서의 계산량 약 1.66배·약 2배 설명 (H) | 문서의 sweep·iteration별 비보존 설명 | 흐름과 IQUAD=1/2의 조합은 권고 경고를 내지만 실행을 차단하지 않는다. |

> Method 2 는 fully explicit 권장 (효율). Current 모델엔 **Method 1 권장**. (swantech PDF 96쪽 / 인쇄 88쪽; swanuse PDF 72쪽 / 인쇄 64쪽; R2:SS-363·SS-364)

정렬 IQUAD=3의 첫 반복 조건은 `IF ( ITER .EQ. 1 ) THEN`이다. 이후 반복의 조건은 다음 원문이다. (`src/swancom1.ftn:7637`; `src/swancom1.ftn:7648–7651`; R8:T1-008)

```fortran
ELSE IF ( ITER .GT. 1 .AND. ( SWPDIR .EQ. 1 .OR.
&        ( SWPDIR .EQ. 2 .AND. IX .EQ. 1) .OR.
&        ( SWPDIR .EQ. 3 .AND. IY .EQ. 1) .OR.
&        ( SWPDIR .EQ. 4 .AND. (IX.EQ.MXC .AND. IY.EQ.1)) )) THEN
```

fully explicit 경로도 음의 전달량을 현재 작용 밀도로 나눠 대각에 넣는다. (`src/swancom4.ftn:1544` `MAX(1.E-18,AC2(ID,I,KCGRD(1))*SIGPI)`; `src/swancom4.ftn:1542–1546`; R2:SS-362)

## 5. §3.7 Action density limiter + under-relaxation (Eq 3.27-3.30)

3rd-gen 모델은 **multiple time scale**(광대역 주파수) → action balance 가 **stiff** (Press 1993). 최소 시간척도가 수렴 지배 → over/undershoot. Nonlinear 4-wave 가 최대 난제 (spectral change 고민감).

### 5.1 Action density limiter (Hersbach-Janssen 1999, WAM 1980s)

매 time step / 격자 / bin 의 net 변화를 omni-directional Phillips equilibrium 의 일부로 제한 (Booij 1999 형):
$$\Delta N \equiv \gamma\frac{\alpha_{\text{PM}}}{2\sigma k^3 c_g} \quad \text{(3.27)}$$
- $\gamma\ge0$ = limitation factor (**보통 $\gamma=0.1$**, Tolman 1992), $\alpha_{\text{PM}} = 8.1\times10^{-3}$ (Pierson-Moskowitz Phillips 상수, Komen 1994)
- 정렬 격자는 제한기가 활성이고 IWIND=4이며 NSTATC=1일 때 HJLIM을 쓴다. 그 밖의 정렬 경로와 비정렬 경로는 활성 조건 아래에서 PHILIM을 쓴다. (`src/swancom1.ftn:3791` `IF (PNUMS(20).LT.100.) THEN`; `src/swancom1.ftn:3792` `IF (IWIND.NE.4 .OR. NSTATC.NE.1) THEN`; `src/SwanCompUnstruc.ftn90:1302` `if ( PNUMS(20) < 100. ) call PHILIM ( ac2, ac2old, cgo, kwave, spcsig, anybin, islmin, nflim, qbloc )`; R8:N1-009)

제한된 갱신:
$$N_{i,j,l,m}^s = N_{i,j,l,m}^{s-1} + \frac{\Delta N_{i,j,l,m}}{|\Delta N_{i,j,l,m}|}\min\{|\Delta N_{i,j,l,m}|, \Delta N\} \quad \text{(3.28)}$$
> 저주파(에너지 함유부)는 pseudo time step 이 evolution scale 과 일치 → pre-limitation 결과. 고주파는 limiter 상한. **문제**: limiter 가 peak 근처·전 격자·전 iteration 에서 active (Tolman 2002 확인) → poor convergence (소진폭 진동). Ris(1999): 정상해가 limiter 설정에 영향받음. De Waal(2001): equilibrium 에서 hidden sink 의심.

### 5.2 Frequency-dependent under-relaxation (false time stepping)

Under-relaxation 항으로 $A$ 주대각 강화 (Ferziger-Perić 1999):
$$\frac{\vec{N}^s - \vec{N}^{s-1}}{\tau} + A\vec{N}^s = \vec{b} \quad \text{(3.29)}$$
- $\tau$ = pseudo time step. $\tau$ 작을수록 작은 갱신 (수렴 ↓, 비용 ↑)
- **주파수 비례 under-relaxation**: $\tau^{-1} = \alpha\sigma$ ($\alpha$ 무차원) → 고주파 작은 갱신, 저주파 큰 갱신:

$$(A + \alpha\sigma I)\vec{N}^s = \vec{b} + \alpha\sigma\vec{N}^{s-1} \quad \text{(3.30)}$$
> $s\to\infty$ 시 $A\vec{N}^\infty = \vec{b}$ (fixed point — 정상해 불변). $\alpha$ 증가 → 전 스펙트럼 변화 감소 → (i) action balance 실제로 푸는 주파수 범위 확대 (ii) limiter 사용 감소. **$\alpha$ 는 경험적 결정 (robustness 저하)**. 첫 iteration 은 under-relaxation off ($\alpha=0$, 2nd-gen 첫 추정 위해 — 2nd-gen 은 안정화 불필요).

## 6. SWAN 옵션 매핑 (User cmd)

| Tech (PDF §) | User cmd | 비고 |
|---|---|---|
| §3.3 해법 선택 | internal | DYNDEP와 주파수 전파 설정을 따른다. (R8:T1-010) |
| 현행 STOPC | `NUMERIC STOPC` | SWSTPC 또는 SwanConvStopc를 선택한다. 일반 기본 npnts=99.5%. (R8:T1-002·N1-011) |
| 현행 ACCUR | `NUMERIC ACCUR` | SACCUR 또는 SwanConvAccur를 선택한다. IGEN=4에서 ERRCHK는 ACCUR를 STOPC로 바꾼다. (R8:N1-011) |
| §3.4 max iteration | `NUMERIC ... [mxitst]` (stationary, 보통 50) / `[mxitns]` (nonstationary) | |
| §3.5 sweeps | (internal four-sweep) | $M>4$ 비권장 |
| §3.6 DIA-in-sweep | `QUADRUPL [iquad]` | iquad=1/2/3 method 선택 |
| 3.27-3.28 action limiter | `NUMERIC ... [limiter]` (= $\gamma$, default 0.1) | Hersbach-Janssen |
| 3.29-3.30 under-relaxation | `NUMERIC ... [alfa]` ($\alpha$) | frequency-dependent |

## 7. 한계

- Matrix 구조식(3.16): ASCII block 형태 → 본 노트 서술 요약 (penta-diagonal block coupling).
- 식 (3.26)의 완전한 분자는 $H_{m0}^{s}(i,j)-(H_{m0}^{s-1}(i,j)+H_{m0}^{s-2}(i,j))+H_{m0}^{s-3}(i,j)$이다. (swantech PDF 92쪽 / 인쇄 84쪽; R8:N1-010)
- §3.7.1 introduction (stiff·multiple time scale 배경)은 정성 서술 — 본 노트 §5 도입에 요약.
- Newton-Raphson breaking(3.18)의 $\phi^{n-1}$ 정의: §3.3 본문 + [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) §6 (S_ds,br Eq 2.68) 연계.

## 8. 연결

- [swan-tech-ch3-discretization](swan-tech-ch3-discretization.md) — §3.2 이산화 (이 system 의 출처)
- [swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) — source term S_tot (선형화 대상)
- [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) — breaking S_ds,br (Newton-Raphson 3.18 대상)
- [swan-tech-ch2-nonlinear-detailed](swan-tech-ch2-nonlinear-detailed.md) — DIA quadruplet (§3.6 four-sweep 적분)
- [swan-source-terms-implementation](../source-analysis/wave/swan-source-terms-implementation.md) — source 선형화 implementation

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

확정 결론과 원문 인용: [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론), [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md#5-차이-결론), [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론), [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-068 | 한 sweep의 계산량 | swantech PDF 87쪽 / 인쇄 79쪽, 번호 없음: $\mathcal O(M)$, “in one step, if the wave characteristic is a straight line and constant everywhere”. | — | H 코드 대조 대상 아님 | 제한된 선형 문제의 계산량 주장이다. 원천항과 굴절을 포함한 실제 반복 횟수 보증이 아니다. |
| R1:TN-070 | 문서 식 (3.18) | swantech PDF 89쪽 / 인쇄 81쪽, (3.18): $S^n\approx\phi^{n-1}E^n+(\partial S/\partial E)^{n-1}(E^n-E^{n-1})$. 번호 없음: $S=aS_{\rm tot}, E=aE_{\rm tot},\ \partial S/\partial E=\partial S_{\rm tot}/\partial E_{\rm tot}$. | `src/swancom2.ftn:2120–2121` `SURFA0 = SbrD`; `SURFA1 = WS + SbrD`; `src/swancom2.ftn:2188–2190` `IMATDA(ID,IS) = IMATDA(ID,IS) + REAL(SURFA1)`; `IMATRA(ID,IS) = IMATRA(ID,IS) + REAL(DIS0)`; `src/swancom2.ftn:2177–2185` | B 문서 오기 | $S=\phi E$의 Newton 식 첫 항은 $\phi^{n-1}E^{n-1}$이다. 문서의 $E^n$을 쓰면 $\phi(E^n-E^{n-1})$를 한 번 더 더한다. 코드의 선형화는 대각에 양의 소산 계수를 더하고 이전 밀도 항을 우변에 더한다. 실제 행렬 계수에는 `KTETA`·`FRFAC(IS)`가 곱해진다. `IF ( IGEN.EQ.4 .AND. ITER.GT.1 ) THEN`이면 이 SSURF 기여는 0이다. 동일 분율 $a$의 미분 관계는 맞다. [10-13 전수 검증 보완]
| R1:TN-073 | Thomas 해법 선택 조건 | swantech PDF 90쪽 / 인쇄 82쪽: “in the absence of mean current there are no shifts in the frequency”.<br>swanuse PDF 94–95쪽 / 인쇄 86–87쪽의 SIGIMPL은 `of currents or time varying depth`를 적용 조건으로 적는다. swantech PDF 18 식 (2.13)에도 $\partial d/\partial t$가 있다. | `src/swancom1.ftn:3681–3682` `ELSEIF ( (DYNDEP .OR. ICUR .EQ. 1) .AND.`; `&           PNUMS(8).NE.0.                 ) THEN` | C 문서 누락 | 수심 시간변화에 의한 주파수 이동은 다른 매뉴얼과 swantech 식 (2.13)에 이미 있다. C는 swantech §3.3의 Thomas 선택 설명이 정적 수심 조건과 주파수 해법 선택을 생략한 점이다. 실제 분기는 `ELSEIF ( (DYNDEP .OR. ICUR .EQ. 1) .AND.`; `&           PNUMS(8).NE.0.                 ) THEN`이다. `IREFR.EQ.0 .AND. ITFRE.EQ.0`이면 그보다 앞에서 대각 나눗셈만 한다. |
| R1:TN-074 | 문서 식 (3.21) | swantech PDF 90쪽 / 인쇄 82쪽, (3.21): $H_{m0}=4\sqrt{m_0},\ T_{m01}=2\pi m_0/m_1,\ m_j=\int_0^\infty\int_0^{2\pi}\sigma^jE\,d\sigma d\theta$. | `src/swancom1.ftn:9800–9813` `DO IS = 1, MSC`; `ACS2  = SPCSIG(IS)**2 * AC2(ID,IS,INDX)`; `HSACC2(INDX) = MAX ( 1.E-20 , 4.*SQRT(XMOM0) )`; `SACC2 (INDX) = MAX ( 1.E-20 , (XMOM1/XMOM0) )` | C 문서 누락 | C는 swantech §3.4의 연속 모멘트 정의에 정지 검사용 유한 주파수 합과 꼬리 생략이 구분되지 않은 점이다. SWSTPC는 계산 주파수만 합산한다. `SACC2`는 주기가 아니라 평균 각주파수이다. |
| R1:TN-075 | 문서 식 (3.22) | swantech PDF 91쪽 / 인쇄 83쪽, (3.22): $\lvert\Delta H_{m0}^s\rvert/H_{m0}^{s-1}<\varepsilon_H^r\ \mathrm{or}\ \lvert\Delta H_{m0}^s\rvert<\varepsilon_H^a$; $\Delta Q^s=Q^s-Q^{s-1}$.<br>swantech PDF 92쪽 / 인쇄 84쪽는 식 (3.22)를 `retained in addition to the stricter criterion (3.26)`라고 적는다. | `src/swancom1.ftn:9852–9853` `HSABS = ABS ( HSACC2(INDX) - HSACC1(INDX) )`; `HSREL = HSABS / HSACC2(INDX)` | B 문서 오기 | 식 (3.22)는 구식 기준 설명에 등장하며 PDF 92에서 개선 기준의 약한 보조 조건으로 다시 유지된다. 현행 STOPC는 현재 파고로 나누고 `.LE.`로 비교한다. B는 swantech에 재사용된 식의 이전 파고 분모와 현행 구현의 차이로 한정한다. |
| R1:TN-076 | 문서 식 (3.23) | swantech PDF 91쪽 / 인쇄 83쪽, (3.23): $\lvert\Delta T_{m01}^s\rvert/T_{m01}^{s-1}<\varepsilon_T^r\ \mathrm{or}\ \lvert\Delta T_{m01}^s\rvert<\varepsilon_T^a$. | `src/swancom1.ftn:9854–9855` `TMABS = ABS ( (PI2/SACC2(INDX)) - (PI2/SACC1(INDX)) )`; `TMREL = TMABS / SACC2(INDX)`<br>`src/SwanConvStopc.ftn90:187,219` `tmcurr(ivert) = max ( 1.e-20, PI2*(m0/m1) )`; `tmrel  = PNUMS( 1) * tmcurr(ivert)` | E 코드 결함 후보 (강함) | 정렬 STOPC는 주기 차이를 평균 각주파수로 나눈다. 이 식은 주기 상대오차의 차원과 맞지 않는다. `IF ( IQCM.EQ.0 ) THEN`인 일반 경로의 수렴 조건에 쓰인다. QC의 파고 전용 수렴 판정에는 쓰이지 않는다. 기본 주기 허용값 1000은 영향을 가릴 수 있다. 비정렬 경로는 주기로 허용오차를 만든다. E 강함을 유지한다. |
| R1:TN-077 | 정지 조건 기본값 | swantech PDF 91쪽 / 인쇄 83쪽, 기본값: $\varepsilon_H^r=\varepsilon_T^r=0.02,\ \varepsilon_H^a=0.02\,{\rm m},\ \varepsilon_T^a=0.2\,{\rm s}$; 습윤점 98%. swantech PDF 92쪽 / 인쇄 84쪽: 곡률 기준 습윤점 99%.<br>swanuse PDF 94쪽 / 인쇄 86쪽의 `[dabs]`, `[drel]`, `[curvat]`, `[npnts]` 기본값. `src/swanmain.ftn:6503–6512`는 `PNUMS(2)=-1.`일 때만 파고 절대 허용값을 정한다. | `src/swanmain.ftn:1219,1224,1227,1292–1293` `PNUMS(1)  = 0.01`; `PNUMS(3)  = 1000.`; `PNUMS(4)  = 99.50`; `PNUMS(15) = 0.005`; `PNUMS(16) = 1000.` | B 문서 오기 | PDF 91의 0.02·0.2·98%는 옛 기준의 설명이다. 이를 현행 기본값으로 옮기지 않는다. B는 PDF 92의 기본 곡률 기준 99%가 현행 99.50%와 다른 점에 한정한다. swanuse PDF 94는 현행 일반 기본값 0.005 m·0.01·0.005·99.5%를 적는다. 코드의 파고 절대 허용값은 미지정일 때 일반 0.005 m, `ITRIAD=3`에서 0.01 m이다. QC의 0.05는 입사파고에 곱하는 무차원 계수이다. |
| R1:TN-078 | 문서 식 (3.24) | swantech PDF 91쪽 / 인쇄 83쪽, (3.24): $\phi^\infty-\phi^s\approx(\phi^{s+1}-\phi^s)/(1-\rho)$. | — | H 코드 대조 대상 아님 | 문서는 이 스펙트럼 반지름 기반 기준이 SWAN에 덜 적합하다고 설명한다. 현행 정지식이라고 주장하지 않는다. |
| R1:TN-080 | 문서 식 (3.26) | swantech PDF 92쪽 / 인쇄 84쪽, (3.26): $\lvert H^s-(H^{s-1}+H^{s-2})+H^{s-3}\rvert/(2H^s)<\varepsilon_C,\ s=3,4,\cdots$.<br>swanuse PDF 93쪽 / 인쇄 85쪽 및 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):220–246은 상대 변화·곡률의 AND와 절대 변화의 OR를 구분한다. | `src/swancom1.ftn:9874–9875` `LCONV = ( HSABS.LE.PNUMS(2) .OR.`; `&                     (HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)) )` | B 문서 오기 | 곡률 값의 식은 같다. B는 swantech §3.4의 두 기준 동시 만족 설명에 한정한다. 현행 파고 조건은 `LCONV = ( HSABS.LE.PNUMS(2) .OR.`; `&                     (HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)) )`의 부분식이다. 일반 경로는 여기에 주기 조건도 AND로 결합한다. swanuse의 파고 조건 설명은 코드와 대응한다. git `2980d1a`에서 이 파고 논리식 변경을 확인했다. |
| R1:TN-081 | 주기 기준의 존속 | swantech PDF 91–92쪽 / 인쇄 83–84쪽: “$T_{m01}$ has been abandoned as a convergence measure”.<br>웹 [수정 이력](../raw/manuals/website/modifications/modifications.htm):1308,1351–1353은 주기 곡률의 추가와 선택 사용을 적는다. swanuse PDF 141의 명령 도식에도 `[dtabs] [curvt]`가 있다. | `src/swancom1.ftn:9877–9878` `( TMCURV.LE.PNUMS(16) .AND.`; `&                     (TMREL.LE.PNUMS(1) .OR. TMABS.LE.PNUMS(3)) )` | C 문서 누락 | 주기 검사 존재는 웹 수정 이력과 swanuse 명령 도식에 있다. C는 swantech §3.4의 주기 기준 폐기 설명에 선택 조건이 없는 점이다. 현행 일반 STOPC에는 주기 검사가 남는다. 기본 1000 값은 이 검사를 느슨하게 한다. 정렬 곡률은 평균 각주파수로 계산하고 비정렬 곡률은 주기로 계산한다. |
| R1:TN-082 | 문서 식 (3.22)·(3.23) | swantech PDF 92쪽 / 인쇄 84쪽: 이전 (3.22)·(3.23)은 “obsolete”.<br>swanuse PDF 141쪽 / 인쇄 133쪽 및 웹 [명령 도식](../raw/manuals/website/online_doc/swanuse/node49.html):305–307은 `ACCUR [drel] [dhoval] [dtoval] [npnts]`를 명시한다. | `src/swancom1.ftn:2270–2277` `IF (PNUMS(21).EQ.0.) THEN`; `CALL SACCUR (COMPDA(1,JDP2),KGRPNT          ,`; `ELSE IF (PNUMS(21).EQ.1.) THEN`<br>`src/swancom1.ftn:4840–4841` `IF ( (TMREL .LE. PNUMS(1) .OR. TMOVAL .LE. PNUMS(16)) .AND.` | C 문서 누락 | `obsolete`는 기능 제거를 뜻하지 않는다. ACCUR 선택은 swanuse 명령 도식에도 남아 있다. C는 swantech 식 (3.22)·(3.23)이 현행 SACCUR의 평균 각주파수 변화와 영역 평균 정규화 조건을 적지 않는 점이다. 호출 조건은 `IF (PNUMS(21).EQ.0.) THEN`이다. |
| R1:TN-085 | 정렬 M-sweep 비교 | swantech PDF 94쪽 / 인쇄 86쪽, 번호 없음: sweep 수 $M$, 구간 $360^\circ/M$; $M=8,12$, $45^\circ,30^\circ$ 예시. 각주: “in SWAN the number of sweeps equals 4 and is hard-coded.” | `src/swancom1.ftn:1698` `!WFR        DO 410 SWPDIR = 1, 4` | H 코드 대조 대상 아님 | 이 절의 $M>4$는 정렬 격자에 대한 가상 비교이다. 비정렬 격자의 가변 sweep 수는 제8장에서 별도로 다룬다. |
| R1:TN-087 | 문서 식 (3.28) | swantech PDF 99쪽 / 인쇄 91쪽, (3.28): $N^s=N^{s-1}+(\Delta N_{\rm bin}/\lvert\Delta N_{\rm bin}\rvert)\min\{\lvert\Delta N_{\rm bin}\rvert,\Delta N\}$. | `src/swancom1.ftn:7976,7981–7983,7988–7992` `IF (MSC.GT.3) THEN`; `AC2(ID,IS,KCGRD(1))=AC2OLD(ID,IS)+DAC2MX`; `IF (QB_LOC.LT.PNUMS(28)) THEN`; `AC2(ID,IS,KCGRD(1))=AC2OLD(ID,IS)-DAC2MX`; `[qb]` | C 문서 누락 | C는 swantech 식 (3.28)에 PHILIM의 선택 bin·`IF (MSC.GT.3) THEN`·감소 제한의 `IF (QB_LOC.LT.PNUMS(28)) THEN` 조건이 없는 점이다. 쇄파율에 따라 제한기를 끄는 선택 자체는 swanuse에도 있다. |
| R1:TN-088 | HJLIM 선택 조건 | swantech PDF 99쪽 / 인쇄 91쪽: “when the physical wind formulation of Janssen (1989,1991a) is applied ... the original limiter of Hersbach and Janssen (1999) is employed.”<br>웹 [수정 이력](../raw/manuals/website/modifications/modifications.htm):1338–1339은 `no use of the Hersbach and Janssen limiter in the case of stationary runs`를 적는다. | `src/swancom1.ftn:3791–3805` `IF (PNUMS(20).LT.100.) THEN`; `IF (IWIND.NE.4 .OR. NSTATC.NE.1) THEN`; `CALL PHILIM`; `CALL HJLIM`<br>`src/SwanCompUnstruc.ftn90:1302` `if ( PNUMS(20) < 100. ) call PHILIM ( ac2, ac2old, cgo, kwave, spcsig, anybin, islmin, nflim, qbloc )` | C 문서 누락 | 정상 계산의 HJLIM 제외는 웹 수정 이력에 이미 있다. C는 swantech §3.7.2가 이 조건과 격자별 경로를 구분하지 않는 점이다. 정렬 격자는 `PNUMS(20).LT.100.` 안에서 `IWIND.NE.4 .OR. NSTATC.NE.1`이면 PHILIM을 호출하고 반대 분기에서 HJLIM을 호출한다. 비정렬 호출은 PHILIM이다. |
| R1:TN-089 | SWAN/WAM 제한량 비율 | swantech PDF 99쪽 / 인쇄 91쪽, 각주: SWAN의 유효 $\gamma$는 WAM보다 $2\pi$ 크다. | `src/swancom1.ftn:7978–7979,8115–8121`; [외부 원문 대조](../../../_staging/recovery/compare/SWAN-external-sources.md) §1 | H 코드 대조 대상 아님 | 대체 문헌(ECMWF IFS Cy48r1 매뉴얼·ECWAM 코드) 기준의 H 판정이다. Hersbach and Janssen (1999) 1차 논문 기준 판정과 구분한다. SWAN의 PHILIM 제한 폭은 로컬 swantech PDF 99 식 (3.27)의 $\gamma\alpha_{PM}/(2\sigma k^3c_g)$와 같다. 외부 판정서의 식 (3.42)는 웹판 번호이며 로컬 PDF 번호는 (3.27)이다. IFS 식 (3.37)·(3.38)은 1차원과 방향별 Phillips 준위의 정규화를 구분한다. 각주의 $2\pi$는 WAM과의 정규화 비교 설명으로 남긴다. IFS의 $1/\pi$만으로 1999 WAM과의 정확한 $2\pi$ 비율을 확정하지 않는다. HJLIM은 `C_HJ = PI2**2*3.0*1.0E-7*DT*SPCSIG(MSC)`와 `DAC2MX=ABS((C_HJ*UFRIC_VEL)/`; `&             (SPCSIG(IS)**3*KWAVE(IS,1)))`를 사용한다. 주석의 제한식 환산은 `UFRIC_VEL = MAX(USTAR(KCGRD(1)), GRAV*SPM_NOND/SPCSIG(IS))`의 하한을 포함해 읽는다. [10-13 전수 검증 보완]
| R1:TC-007 | 비정렬 반복의 주기 상대 변화량 | — | `src/SwanConvStopc.ftn90:187,195,219,225` `tmcurr(ivert) = max ( 1.e-20, PI2*(m0/m1) )`; `tmabs = abs ( tmcurr(ivert) - tmprev(ivert) )`; `tmrel  = PNUMS( 1) * tmcurr(ivert)`; `( tmcurv <= curvat .and. tmabs <= max(tmrel,PNUMS(3)) )` | C 문서 누락 | 비정렬 경로는 주기 단위로 상대 오차를 비교한다. 정렬 경로 R1:TN-076의 `TMABS/SACC2`와 다르다. 이 차이는 R1:TN-076 결함 후보의 반대 경로 근거이다. |
| R1:TC-024 | 정상 첫 반복의 공간 예측값 | — | `src/swancom1.ftn:3460,3465–3470` `IF (ICOND.NE.4 .AND. ITER.EQ.1 .AND. NSTATC.EQ.0) THEN`; `CALL SPREDT`<br>`src/swancom5.ftn:4584–4585,4594–4598` `WEIG1 = CDEN/CNUM`; `WEIG2 = 1. - WEIG1`; `FAC_A = TCF1 * WEIG1 * AC2(ID,IS,KCGRD(2))`; `FAC_B = TCF2 * WEIG2 * AC2(ID,IS,KCGRD(3))`; `AC2(ID,IS,KCGRD(1)) = MAX ( 0. , (FAC_A + FAC_B))` | C 문서 누락 | `IF (ICOND.NE.4 .AND. ITER.EQ.1 .AND. NSTATC.EQ.0) THEN`에서 LPREDT를 켠다. 이후 `IF (LPREDT) THEN`에서 SPREDT를 호출한다. 정상 첫 반복의 해당 경로는 상류 두 점의 가중합을 공간 예측값으로 쓴다. 곡선 좌표 CCURV는 4514–4568행의 별도 기하식을 쓴다. C는 swantech에 이 공간 예측 절차가 없는 점이다. 제2세대 원천항 초기 추정과 구분한다. |
| R2:SS-361 | DIA의 수치 구현: 3.6 · 96/88, `calculated in every iteration prior to the first sweep`; `stored in internal memory`. | swantech PDF 96쪽 / 인쇄 88쪽, `calculated in every iteration prior to the first sweep`; `stored in internal memory`. | `src/swancom1.ftn:7637` `IF (ITER.EQ.1) THEN`<br>`src/swancom1.ftn:7643` `CALL SWSNL3`<br>`src/swancom1.ftn:7653` `CALL SWSNL3`<br>`src/swancom1.ftn:7663` `CALL FILNL3` | C | 해석: `IQUAD=3`은 `MEMNL4`에 저장한다. 첫 반복에서는 안정화를 위해 각 스윕에서 다시 계산한다. 이후에는 격자점의 첫 방문에서 계산한다. 모든 격자점에 대해 첫 스윕 전에 일괄 계산한다는 뜻으로 구현을 설명하면 틀린다. [10-13 전수 검증 정정]
| R2:SS-362 | DIA의 수치 구현: 3.6 · 96/88, `two different numerical schemes ... a semi-implicit scheme and a fully explicit scheme`. | swantech PDF 96쪽 / 인쇄 88쪽, `two different numerical schemes ... a semi-implicit scheme and a fully explicit scheme`. | `src/swancom1.ftn:7604` `IF (IQUAD.EQ.1) THEN`<br>`src/swancom1.ftn:7609` `CALL SWSNL1`<br>`src/swancom1.ftn:7618` `ELSE IF (IQUAD.EQ.2) THEN`<br>`src/swancom4.ftn:1544` `MAX(1.E-18,AC2(ID,I,KCGRD(1))*SIGPI)` | C | 해석: swantech PDF 96쪽 / 인쇄 88쪽의 semi-implicit·fully explicit 선택은 코드의 두 경로에 대응한다. fully explicit 경로도 음의 전달량을 현재 작용 밀도로 나눠 대각에 넣는다. C의 범위는 해당 절에 이 부호별 조립 처리가 생략된 점이다. 명칭만으로 전체 Jacobian 사용 여부나 저자의 의도를 정의하지 않는다. |
| R2:SS-363 | DIA의 수치 구현: 3.6 · 96/88, 인접 두 사분면의 `about 33°`, 메모리 약 2배, 계산량 약 1.66배·약 2배, 수렴 결과 및 에너지 보존 주장. | swantech PDF 96쪽 / 인쇄 88쪽, 인접 두 사분면의 `about 33°`, 메모리 약 2배, 계산량 약 1.66배·약 2배, 수렴 결과 및 에너지 보존 주장. | — | H | 해석: 약 33°는 R2:SS-075의 약 33.56° 공명 배치와 대응한다. 문서의 `about`·`a factor of about`는 근삿값 표현이다. 메모리·계산량 배수와 수렴 서술은 문서의 구현 비용·성능 주장으로 H에 둔다. |
| R2:SS-718 | 노트 · manual-notes/swan-tech-ch3-solution-iteration-limiter.md:107 | `manual-notes/swan-tech-ch3-solution-iteration-limiter.md:107` `iteration 시작 시 first sweep 전 1회 계산`; 108 `current 시 불가`. R2:SS-361·362·364. | `src/swanmain.ftn:6585` `IF (ICUR.NE.0 .AND. (IQUAD.EQ.1 .OR. IQUAD.EQ.2)) THEN`<br>`src/swanmain.ftn:6586` `CALL MSGERR(0,'In presence of a current it is recommended to')` | C | 해석: `IQUAD=3`은 첫 반복의 각 sweep에서 source를 다시 계산한다. 이후에는 해당 격자점의 첫 방문에서 계산한다. 흐름과 `IQUAD=1/2`의 조합은 권고 경고를 내지만 실행을 차단하지 않는다. [10-13 전수 검증 정정]
| R8:T1-002 | STOPC 기본 합격점 비율 | swantech PDF 92쪽·인쇄 84쪽은 “at least 99% of all wet grid points”라고 적는다. swanuse PDF 94쪽·인쇄 86쪽의 기본값은 “Default: [npnts] = 99.5 [−]”이다. `manual-notes/swan-tech-ch3-solution-iteration-limiter.md:143`은 이를 `npnts=99%`로 적었다. | `src/swanmain.ftn:1227` `PNUMS(4)  = 99.50`<br>`src/swanpre1.ftn:3107` `PNUMS(4) = 99.`<br>`src/swanmain.ftn:6681–6688` `IF (IGEN.EQ.4) THEN`; `IF (PNUMS(21).EQ.0.) THEN`; `PNUMS(4)  = 99.` | B — 노트 오기 | 일반 STOPC의 기본 합격점 비율은 99.5%이다. GEN4 입력과 IGEN=4의 ACCUR 전환 경로는 99%를 설정한다. 기술 문서의 “at least 99%”만으로 현재 기본값을 99%라고 단정할 수 없다. B는 노트가 일반 기본값을 99%로 옮긴 오기에 한정한다. |
| R8:T1-003 | STOPC의 주기 관련 선택 조건 | swantech PDF 91쪽·인쇄 83쪽은 제안된 개선 기준에서 “Tm01 has been abandoned as a convergence measure and only Hm0”라고 적는다. swanuse PDF 93쪽·인쇄 85쪽의 본문 구문은 DTABS·CURVT를 생략한다. 그러나 같은 책 PDF 141쪽·인쇄 133쪽과 `website/online_doc/swanuse/node49.html:305`은 `[dtabs] [curvt]`를 싣는다. `website/modifications/modifications.htm:1351–1353`은 “the curvature of Tm01 can be included as an option”이라고 명시한다. | `src/swanpre1.ftn:1948` `CALL INREAL ('DTABS'  , PNUMS(3) , 'STA', 1000.)`<br>`src/swanpre1.ftn:1949` `CALL INREAL ('CURVT'  , PNUMS(16), 'STA', 1000.)`<br>`src/swancom1.ftn:9873–9878` `IF ( IQCM.EQ.0 ) THEN`; `( TMCURV.LE.PNUMS(16) .AND.`; `&                     (TMREL.LE.PNUMS(1) .OR. TMABS.LE.PNUMS(3)) )` | C — 본문 설명 누락 | DTABS·CURVT의 구문과 주기 곡률 선택 기능은 부록·웹에 있다. C는 swantech §3.4와 swanuse NUMERIC 본문의 선택 조건 설명 누락에 한정한다. 일반 STOPC에는 기본값 1000.인 두 조건이 남아 있다. 입력값을 강화하면 종료를 제한할 수 있다. 정렬 CURVT는 평균 각주파수 곡률에 적용된다. 비정렬 CURVT는 주기 곡률에 적용된다. |
| R8:T1-004 | 곡률 조건을 우회하는 절대 Hs 차이 | swantech PDF 92쪽·인쇄 84쪽: “Condition (3.26) must be satisfied” 및 “the weaker criterion (3.22) is retained in addition to the stricter criterion (3.26)”. swanuse PDF 93쪽·인쇄 85쪽은 상대 변화와 곡률 조건 뒤에 “or the absolute change”를 적는다. | `src/swancom1.ftn:9874–9875` `LCONV = ( HSABS.LE.PNUMS(2) .OR.`; `&                     (HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)) )`<br>`src/SwanConvStopc.ftn90:224` `lconv = ( hsabs <= PNUMS(2) .or. (hsabs <= hsrel .and. hscurv <= curvah) ) .and. &` | B | 일반 STOPC의 파고 조건은 절대 차이 충족 또는 상대 차이와 곡률의 동시 충족이다. 파고 곡률은 모든 합격점의 필수 조건이 아니다. 이 OR 구조는 swanuse와 일치한다. B는 swantech의 곡률 필수 설명에 한정한다. |
| R8:T1-005 | Hs 곡률의 저장 변수 표기 | swantech PDF 92쪽·인쇄 84쪽 이미지의 식 (3.26): $\frac{\lvert H_{m0}^{s}(i,j)-(H_{m0}^{s-1}(i,j)+H_{m0}^{s-2}(i,j))+H_{m0}^{s-3}(i,j)\rvert}{2H_{m0}^{s}(i,j)}<\varepsilon_{\mathrm C},\quad s=3,4,\cdots$. | `src/swancom1.ftn:9857` `HSDIFO       = HSDIFC(INDX)`<br>`src/swancom1.ftn:9858` `HSDIFC(INDX) = 0.5*( HSACC2(INDX) - HSACC0(INDX) )`<br>`src/swancom1.ftn:9859` `HSCURV       = ABS(HSDIFC(INDX) - HSDIFO)/HSACC2(INDX)` | F | 현재 HSDIFC와 직전 HSDIFO의 차분을 전개하면 식 (3.26)의 좌변과 같다. 식의 반복 범위는 s=3,4,…이다. 이 F 판정은 좌변의 표기에 한정한다. 비교 경계는 R8:T1-006을 따른다. 종료 논리는 R8:T1-004를 따른다. |
| R8:T1-006 | 정지 부등호·합격점 비율 경계 | swanuse PDF 93쪽·인쇄 85쪽: “less than [drel]” 및 “more than fraction [npnts]%”. swantech PDF 92쪽·인쇄 84쪽 식 (3.26)의 비교 기호는 `<`이다. | `src/swancom1.ftn:9875` `HSREL.LE.PNUMS(1).AND.HSCURV.LE.PNUMS(15)`<br>`src/swancom1.ftn:9928` `ACCUR  = CEILING(REAL(IACCUR) * 10000. / REAL(WETGRD))/100.`<br>`src/swancom1.ftn:2352–2353` `IF ( (ITER.NE.1 .OR. PNUMS(21).EQ.0.) .AND.`; `&                                      ACCUR.GE.PNUMS(4) ) GOTO 470`<br>`src/SwanConvStopc.ftn90:267` `if ( nwetp > 0. ) accur = ceiling(npacc*10000./nwetp)/100.`<br>`src/SwanCompUnstruc.ftn90:1487–1500` `if ( accur >= PNUMS(4) ) exit iterloop` | B | STOPC의 개별 비교는 허용값과 같은 값도 허용한다. 이는 식 (3.26)의 엄격한 `<`와 다른 경계이다. 합격점 백분율은 0.01 퍼센트포인트 단위로 올려 npnts 이상인지 비교한다. 첫 반복에는 이 수렴 종료를 적용하지 않는다. B의 근거는 느슨한 산문만이 아니라 명시된 식의 비교 경계이다. |
| R8:T1-007 | 최대 반복 수의 종료 시점 | swanuse PDF 94쪽·인쇄 86쪽은 최대 반복 수를 설명하며 “The computation stops when this number is exceeded.” 및 “moves to the next time step when this number is exceeded.”라고 적는다. swantech PDF 90쪽·인쇄 82쪽은 반복 범위를 s=1부터 s=S까지로 쓰고 최대 횟수가 “is reached”일 때 종료한다고 적는다. | `src/swancom1.ftn:1487` `DO 450 ITER = 1, ITERMX`<br>`src/SwanCompUnstruc.ftn90:671` `iterloop: do iter = 1, ITERMX` | F — 종료 시점 표현 | ITERMX가 양수이고 수렴 등으로 먼저 끝나지 않으면 반복 몸체는 ITERMX번 실행된다. 다음 반복이 상한을 넘는 시점에 루프를 끝낸다는 해석은 “exceeded”와 양립한다. 원문은 ITERMX+1번째 몸체를 실행한다고 적지 않는다. 따라서 문서 오기 B를 종료 시점 표현 차이 F로 고친다. |
| R8:T1-008 | 정렬 전 방향 DIA의 생산 시점 | swantech PDF 96쪽·인쇄 88쪽: “the interactions are calculated in every iteration prior to the first sweep”. 웹 `website/online_doc/swantech/node45.html:52–62`도 첫 sweep 전 계산과 저장을 설명한다. | `src/swancom1.ftn:7630` `ELSE IF ( IQUAD .EQ. 3) THEN`<br>`src/swancom1.ftn:7637` `IF ( ITER .EQ. 1 ) THEN`<br>`src/swancom1.ftn:7648–7651` `ELSE IF ( ITER .GT. 1 .AND. ( SWPDIR .EQ. 1 .OR.`; `&        ( SWPDIR .EQ. 2 .AND. IX .EQ. 1) .OR.`; `&        ( SWPDIR .EQ. 3 .AND. IY .EQ. 1) .OR.`; `&        ( SWPDIR .EQ. 4 .AND. (IX.EQ.MXC .AND. IY.EQ.1)) )) THEN` | B | 정렬 IQUAD=3은 격자점의 SOURCE 호출 안에서 전 방향 원천항을 계산해 MEMNL4에 저장한다. 첫 반복에서는 각 sweep의 SOURCE 방문마다 계산한다. 이후 반복에서는 인용한 SWPDIR·경계점 조건을 만족할 때 계산한다. 전 영역의 원천항을 첫 sweep 전에 선계산한다는 설명과 다르다. 코드의 `:7634–7635` 주석도 “prior to every iteration”이라고 적지만 실행문은 점별 호출이다. |
| R8:T1-010 | Thomas 선택의 시간 수심 조건 | swantech PDF 90쪽·인쇄 82쪽: “in the absence of mean current there are no shifts in the frequency”. swanuse PDF 94–95쪽·인쇄 86–87쪽은 SIP 사용 조건을 “in the presence of currents or time varying depth”로 적는다. `website/online_doc/swanuse/node29.html:440–449`도 같은 조건을 명시한다. | `src/swancom1.ftn:3656` `IF ( IREFR.EQ.0 .AND. ITFRE.EQ.0 ) THEN`<br>`src/swancom1.ftn:3681–3682` `ELSEIF ( (DYNDEP .OR. ICUR .EQ. 1) .AND.`; `&           PNUMS(8).NE.0.                 ) THEN`<br>`src/SwanCompUnstruc.ftn90:1228` `elseif ( .not.DYNDEP .and. ICUR == 0 .or. int(PNUMS(8)) == 0 ) then` | C — swantech 조건 생략 | 해법 선택은 흐름뿐 아니라 DYNDEP와 주파수 전파 설정도 따른다. 무흐름만으로 Thomas 분기를 단정할 수 없다. 시간 변동 수심 조건은 사용자 매뉴얼에 있다. C는 swantech §3.3의 무흐름 설명에서 이 조건이 생략된 범위에 한정한다. |
| R8:T1-011 | 정렬 STOPC의 TMREL 정규화 | swantech PDF 90쪽·인쇄 82쪽 식 (3.21): $T_{m01}=2\pi\frac{m_0}{m_1}$. 코드 주석 `src/swancom1.ftn:9646`은 `!     SACC2       mean wave frequency at iter`, `:9691`은 `!     TMREL :     relative value of Tm`이다. [git 판정 E](../../../_staging/recovery/compare/SWAN-git-verify-E.md)의 결론을 유지한다. `git log -G 'TMREL = TMABS' -- src/swancom1.ftn`은 최초 반입 `b2ae30e`(2022-08-10, `initial release`)만 반환한다. 식은 `b2ae30e:src/swancom1.ftn:9606`, `7ee8981:src/swancom1.ftn:9855`, 현재 `43e9bbb`에 있다. | `src/swancom1.ftn:2277–2283` `ELSE IF (PNUMS(21).EQ.1.) THEN`<br>`src/swancom1.ftn:9813` `SACC2 (INDX) = MAX ( 1.E-20 , (XMOM1/XMOM0) )`<br>`src/swancom1.ftn:9854` `TMABS = ABS ( (PI2/SACC2(INDX)) - (PI2/SACC1(INDX)) )`<br>`src/swancom1.ftn:9855` `TMREL = TMABS / SACC2(INDX)`<br>`src/swancom1.ftn:9873` `IF ( IQCM.EQ.0 ) THEN`<br>`src/swancom1.ftn:9878` `(TMREL.LE.PNUMS(1) .OR. TMABS.LE.PNUMS(3))`<br>`src/SwanConvStopc.ftn90:187` `tmcurr(ivert) = max ( 1.e-20, PI2*(m0/m1) )`<br>`src/SwanConvStopc.ftn90:219` `tmrel  = PNUMS( 1) * tmcurr(ivert)` | E — 근거 강함 | 정렬 STOPC의 TMREL은 주기 차이를 평균 각주파수로 나눈다. 이 값의 차원은 s²이며 무차원 상대오차가 아니다. 자체 주석과 비정렬 주기 기준 비교에 모두 모순된다. 일반 STOPC 경로의 강한 결함 후보이다. QC 분기는 이 값을 합격 조건에 쓰지 않는다. 기본 DTABS·CURVT=1000.은 주기 조건을 완화하지만 단위를 보정하지 않는다. 두 입력을 바꾸는 경로는 `src/swanpre1.ftn:1948–1949`에 있다. |
| R8:T1-015 | ACCUR의 공간 평균 조건 | swantech PDF 91쪽·인쇄 83쪽 식 (3.22)·(3.23)은 점별 상대 차이 또는 절대 차이이며 “are both satisfied in at least 98% of all wet grid points”라고 적는다. swanuse PDF 93쪽·인쇄 85쪽 본문 구문에는 ACCUR·DHOVAL·DTOVAL이 없다. 그러나 같은 책 PDF 141쪽·인쇄 133쪽과 `website/online_doc/swanuse/node49.html:307`에는 `ACCUR [drel] [dhoval] [dtoval] [npnts]`가 있다. | `src/swanpre1.ftn:1962–1966` `ELSE IF (KEYWIS ('ACCUR')) THEN`<br>`src/swancom1.ftn:4814` `TMOVAL = ABS ( SACC2(INDX) - SACC1(INDX) ) / SMN2`<br>`src/swancom1.ftn:4819` `HSOVAL = ABS ( HSACC2(INDX) - HSACC1(INDX) ) / HSMN2`<br>`src/swancom1.ftn:4840–4841` `IF ( (TMREL .LE. PNUMS(1) .OR. TMOVAL .LE. PNUMS(16)) .AND.`; `&         (HSREL .LE. PNUMS(1) .OR. HSOVAL .LE. PNUMS(15)) ) THEN` | C — 본문 설명 누락 | NUMERIC ACCUR의 구문은 부록·웹에 있다. C는 swanuse NUMERIC 본문과 swantech의 구 기준 설명에 현행 DHOVAL·DTOVAL의 공간 평균 정규화가 빠진 범위에 한정한다. 식 (3.22)·(3.23)을 현재 ACCUR의 구현식으로 쓰지 않는다. 정렬 TMREL·TMOVAL은 평균 각주파수 차이이다. 비정렬 경로는 주기 차이이다. |
| R8:N1-009 | HJLIM 호출 조건 | `manual-notes/swan-tech-ch3-solution-iteration-limiter.md:121` `Janssen(1989,1991a) wind 사용 시 원 Hersbach-Janssen(1999) limiter 적용`. `website/modifications/modifications.htm:1338–1339`은 “no use of the Hersbach and Janssen limiter in the case of stationary runs”라고 적는다. | `src/swancom1.ftn:3791` `IF (PNUMS(20).LT.100.) THEN`<br>`src/swancom1.ftn:3792` `IF (IWIND.NE.4 .OR. NSTATC.NE.1) THEN`<br>`src/SwanCompUnstruc.ftn90:1302` `if ( PNUMS(20) < 100. ) call PHILIM ( ac2, ac2old, cgo, kwave, spcsig, anybin, islmin, nflim, qbloc )` | C — 노트의 조건 누락 | 정렬 격자는 제한기가 활성이고 IWIND=4이며 NSTATC=1일 때 HJLIM을 쓴다. 그 밖의 정렬 경로와 비정렬 경로는 활성 조건 아래에서 PHILIM을 쓴다. C는 노트가 격자·비정상·활성 조건을 빠뜨린 범위이다. 정상 계산 제외 조건은 웹 변경 기록에 이미 있다. |
| R8:N1-010 | 노트의 불완전한 곡률 분자 | `manual-notes/swan-tech-ch3-solution-iteration-limiter.md:80`은 `(H_{m0}^{s-1}(i,j) + H_{m0}^{s-2}(i,j))/2 \cdots`를 분자에 넣는다. `:153`은 분자가 잘렸다고 적는다. swantech PDF 92쪽·인쇄 84쪽 이미지에는 완전한 식 (3.26)이 있다. | `src/swancom1.ftn:9857–9859` `HSDIFO       = HSDIFC(INDX)`; `HSDIFC(INDX) = 0.5*( HSACC2(INDX) - HSACC0(INDX) )`; `HSCURV       = ABS(HSDIFC(INDX) - HSDIFO)/HSACC2(INDX)` | B | 식 (3.26)을 $\frac{\lvert H_{m0}^{s}(i,j)-(H_{m0}^{s-1}(i,j)+H_{m0}^{s-2}(i,j))+H_{m0}^{s-3}(i,j)\rvert}{2H_{m0}^{s}(i,j)}<\varepsilon_{\mathrm C},\quad s=3,4,\cdots$로 교체한다. 노트의 분자 내부 `/2`와 생략 부호는 원식을 재현하지 않는다. |
| R8:N1-011 | 구 수렴 기준의 명령 매핑 | `manual-notes/swan-tech-ch3-solution-iteration-limiter.md:142`은 `3.22-3.23 종래 stopping`을 `NUMERIC STOPC ... STAT mxitst`에 연결한다. swanuse PDF 141쪽·인쇄 133쪽과 `website/online_doc/swanuse/node49.html:305–307`은 STOPC·ACCUR를 별도 선택지로 싣는다. | `src/swanpre1.ftn:1943` `PNUMS(21) = 1.`<br>`src/swanpre1.ftn:1962` `ELSE IF (KEYWIS ('ACCUR')) THEN`<br>`src/swanpre1.ftn:1963` `PNUMS(21) = 0.`<br>`src/swanmain.ftn:6681–6685` `IF (IGEN.EQ.4) THEN`; `IF (PNUMS(21).EQ.0.) THEN`; `PNUMS(21) = 1.` | B | STOPC는 SWSTPC 또는 SwanConvStopc를 선택한다. ACCUR는 SACCUR 또는 SwanConvAccur를 선택한다. IGEN=4에서 ERRCHK는 ACCUR를 STOPC로 바꾼다. 현재 ACCUR의 실제 수식은 R8:T1-015를 따른다. 구 식 (3.22)·(3.23)을 현재 STOPC나 ACCUR의 완전한 구현식으로 적지 않는다. |
| R7:H-213p | 곡률 정지 기준의 정확도·성능 | `website/modifications/modifications.htm:213` `An alternative stopping criterion is implemented and is based on the curvature of the iteration curve of the significant wave height. It is found to be more effective in locating the point of model convergence, yielding results that are closer to the fully-converged solution.` | `src/swancom1.ftn:2278` `CALL SWSTPC ( HSAC0         ,HSAC1           ,HSAC2 ,          40.41` | H 코드 대조 대상 아님 | 성능·정확도·관측 적합성에 관한 문장이다. 소스 분기의 존재만으로 이 효과의 크기나 보편성을 판정하지 않는다. |
| R7:H-219 | 빠른 DIA | `website/modifications/modifications.htm:219` `A fast version of the DIA approximation for quadruplets is included. Neighbouring interactions are interpolated in a piecewise constant manner instead of linear one. Moreover, the DIA calculation is carried out in the full spectral circle per iteration (instead of a quadrant per iteration). As a result, a significant speed-up in the computation can be obtained. Use of this technique can be realised by setting QUAD IQUAD = 8. This approach has almost no effect on the model results compared to the default method (IQUAD = 2).`; `website/online_doc/swantech/node45.html:52–63`은 매 반복의 첫 sweep 전에 계산한다고 설명한다. | `src/swancom1.ftn:7703` `IF ( ITER .EQ. 1 ) THEN`<br>`src/swancom1.ftn:7713–7716` `ELSE IF ( ITER .GT. 1 .AND. ( SWPDIR .EQ. 1 .OR.`; `     &        ( SWPDIR .EQ. 2 .AND. IX .EQ. 1) .OR.`; `     &        ( SWPDIR .EQ. 3 .AND. IY .EQ. 1) .OR.`; `     &        ( SWPDIR .EQ. 4 .AND. (IX.EQ.MXC .AND. IY.EQ.1)) )) THEN` | C 문서 누락 | IQUAD=8은 전체 방향의 상호작용을 계산한다. `IF ( ITER .EQ. 1 ) THEN` 분기는 매 sweep에서 SWSNL8을 호출한다. 이후 반복은 인용한 SWPDIR·IX·IY 조건에서 갱신한다. C는 수정 이력과 swantech의 반복 설명이 이 첫 반복·경계점 조건을 생략한 부분이다. |
| R7:H-219p | 빠른 DIA의 정확도·성능 | `website/modifications/modifications.htm:219` `A fast version of the DIA approximation for quadruplets is included. Neighbouring interactions are interpolated in a piecewise constant manner instead of linear one. Moreover, the DIA calculation is carried out in the full spectral circle per iteration (instead of a quadrant per iteration). As a result, a significant speed-up in the computation can be obtained. Use of this technique can be realised by setting QUAD IQUAD = 8. This approach has almost no effect on the model results compared to the default method (IQUAD = 2).` | `src/swancom1.ftn:7695` `ELSE IF ( IQUAD .EQ. 8) THEN                                      40.41` | H 코드 대조 대상 아님 | 성능·정확도·관측 적합성에 관한 문장이다. 소스 분기의 존재만으로 이 효과의 크기나 보편성을 판정하지 않는다. |
| R7:H-789 | 초기 추정·정지 기준 성능 | `website/modifications/modifications.htm:789` `To improve the convergence characteristics of SWAN, the first-guess (in stationary mode) and the break-off criteria for the iterative procedure have been changed. The effect of these changes are usually hardly noticeable in field conditions whereas the computations are more accurate in laboratory conditions.` | `src/swanmain.ftn:1311` `PNUMS(21) = 1.                                                      40.80 40.41` | H 코드 대조 대상 아님 | 필드·실험실 결과의 영향과 정확도 주장이다. 현재 STOPC 기본 선택만 소스로 확인했다. |
| R7:H-1228 | 유속에서 IQUAD=3 자동 설정 | `website/modifications/modifications.htm:1228` `in case of ambient current set IQUAD to 3 by default`; `website/modifications/modifications.htm:522` `<li>In case of ambient current now advice will be given on setting IQUAD=3 (is therefore not automatically adjusted).` | `src/swanmain.ftn:6586` `CALL MSGERR(0,'In presence of a current it is recommended to')`; `122b595 2023-02-28 initial release (v 41.45)`<br>`122b595:src/swanmain.ftn:6472` `      IF (ICUR.NE.0 .AND. (IQUAD.EQ.1 .OR. IQUAD.EQ.2)) THEN`<br>`122b595:src/swanmain.ftn:6473` `         CALL MSGERR(0,'In presence of a current it is recommended to')`<br>`122b595:src/swanmain.ftn:6474` `         CALL MSGERR(0,'update quadruplets per iteration instead of')`<br>`43e9bbb:src/swanmain.ftn:6585` `      IF (ICUR.NE.0 .AND. (IQUAD.EQ.1 .OR. IQUAD.EQ.2)) THEN`<br>`43e9bbb:src/swanmain.ftn:6586` `         CALL MSGERR(0,'In presence of a current it is recommended to')`<br>`43e9bbb:src/swanmain.ftn:6587` `         CALL MSGERR(0,'update quadruplets per iteration instead of')`<br>`43e9bbb:src/swanmain.ftn:6588` `         CALL MSGERR(0,'per sweep. This will, however, increase the')`<br>`43e9bbb:src/swanmain.ftn:6589` `         CALL MSGERR(0,'amount of internal memory with a factor 2.')`; `<li>In case of ambient current now advice will be given on setting IQUAD=3 (is therefore not automatically adjusted).` | A 확정 (41.41 권고 메시지로 대체) | 유속이 있으면 IQUAD=3을 자동 지정하던 41.01의 규칙은 41.41에서 권고 메시지로 바뀌었다. 41.45 비교 코드(122b595, 2023-02-28)와 현재 코드도 권고 메시지를 사용한다. |
