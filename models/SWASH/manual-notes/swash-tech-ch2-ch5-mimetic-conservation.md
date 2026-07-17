---
title: "SWASH swashtech Ch2·Ch5 — Hamiltonian 구조·mimetic 이산화·질량/운동량/에너지 보존 증명"
topic: swash
canonical_source: self
citation_status: verified
verification_method: "models/SWASH/raw/source_code/swash/doc/swashtech.pdf (v12.01, 2026-05-06 생성, 128 PDF쪽) 직접 열람 — Ch2 pp.5-54·Ch3 §3.1 pp.55-56·Ch5 §5.6-5.7 pp.72-83 페이지·식번호 실측. ★페이지 규약: 인쇄 페이지 기준(PDF쪽 = 인쇄+8). I-6 문서축 재검토(2026-07-17) 산출 — Codex ② 5회차 '비코어 판정 자기모순' 지적의 해소."
note_author: "Claude Fable 5 (I-6 심층 재검토)"
note_date: 2026-07-17
related:
  - swash-tech-documentation-overview.md
---

# swashtech Ch2·Ch5 — Hamiltonian·mimetic 이산화·보존 증명

> SWASH 기술문서의 이론 코어. **왜 이 장들이 핵심인가**: SWASH 이산화의 설계 원리(무엇을 *정확히* 보존하도록 격자·연산자를 짰는가)가 여기서 증명된다 — 스킴 선택(C-grid·산술평균 수심·단순평균 이류)의 이유가 전부 이 보존 조건들이다.

## 1. 지배방정식과 Hamiltonian 구조 (§2.2-2.3, p.11-17)

- **비점성·정수압 SWE(플럭스형)**: $\partial h/\partial t+\nabla\cdot\mathbf q=0$ (Eq. 2.1)·$\partial h\mathbf u/\partial t+\nabla\cdot(\mathbf q\otimes\mathbf u)=-gh\nabla\zeta$ (Eq. 2.2), $h=\zeta+d$·$\mathbf q=h\mathbf u$ (p.11; 비정수압 항 $\int\nabla p\,dz$ 는 Ch3 Eq. 3.2, p.55 에서 등장 — Ch2 는 정수압 뼈대).
- **Hamiltonian**: $H(h,m_x,m_y)=\tfrac12\int_\Omega[(m_x^2+m_y^2)/h+g\zeta^2]\,dxdy$ (p.14, $\mathbf m=h\mathbf u$) — 심플렉틱형 $\partial p/\partial t=J\,\delta H/\delta p$ (Eq. 2.11, p.14), Poisson 텐서 $J$ 는 Lie-Poisson 형·상태 선형·skew-adjoint·Jacobi 조건 만족 (Eq. 2.12, p.15). 전개하면 (2.1)-(2.2) 정확 재생 (p.15).
- **에너지 보존 = J 의 반대칭성**: $dH/dt=\langle\delta H/\delta p,J\,\delta H/\delta p\rangle=0$ (p.15-16; Noether 정리의 발현으로 서술).
- **★부하지지 항등식 Eq. 2.8 (p.13)**: $\langle f,\nabla\cdot\mathbf v\rangle=-\langle\nabla f,\mathbf v\rangle$ — "발산의 수반은 마이너스 기울기". 문서 전체의 이산 설계가 이 항등식의 이산 재현(div $=-$gradᵀ)을 축으로 함.
- **이류 연산자 조건 (p.17)**: $A\mathbf u:=\nabla\cdot(\mathbf q\otimes\mathbf u)$ 에 대해 $A+\tfrac12(\partial h/\partial t)I$ 가 반대칭이어야 에너지 보존 — $A=\tfrac12C-\tfrac12C^\mathsf T+\tfrac12(\nabla\cdot\mathbf q)I$ ($C$ 반대칭, Eq. 2.13-2.14). 압력구배·이류가 **각각 개별로** 에너지 보존해야 하고, 도수(hydraulic jump)·조석 bore 는 **의도적 소산 추가**가 필요함을 명시 (p.17).

## 2. Mimetic 이산화의 의미 (§2.1·2.4-2.5, p.5-44)

- **정의**: 이산 grad/curl/div 를 (계량 없는) **incidence 행렬**로 구성해 벡터해석 항등식 curl grad $=0$·div curl $=0$ 과 대칭관계 div $=-$gradᵀ·이산 부분적분·곱규칙을 **정확히** 재현 (p.6-7·9-10). 미분형식·일반화 Stokes 정리(§2.4)·대수적 위상(§2.5: cell complex·chain/boundary·cochain/coboundary·Hodge star·de Rham 복합체)이 그 기반.
- **분리 원리 (p.10)**: PDE 의 위상적 부분(보존 법칙)은 **이산화 오차 없이 정확히**, 계량/구성 관계(Hodge star 행렬)만 근사 — 오차의 소재를 구조적으로 한정.
- **Arakawa C-grid 는 귀결**: primal(외향)·dual(내향) 격자 구조에서 staggering 이 자연히 나옴 — Arakawa & Lamb 스킴을 자유수면 흐름 최초기 mimetic 이산화로 자리매김 (p.9).

## 3. 직교격자 반이산계와 전역 에너지 보존 (§2.6.2, p.45-53)

- 연속: $d\nu^{(n)}/dt+\mathbb D^{n-1}\varphi^{(n-1)}=0$ (Eq. 2.22, p.47) — incidence 행렬 발산이라 **셀별 질량 정확 보존**.
- 압력구배: $\nabla\tfrac12gh^2=gh\nabla\zeta+gh\nabla d$ 를 **산술평균 수심** $\bar h_{\tilde e}=\tfrac12(h_l+h_r)$ 로 정확 이산화, 이산 기울기 $\tilde{\mathbb D}^0=-(\mathbb D^{n-1})^\mathsf T$ ("에너지 보존에 필수") + $\tilde{\mathbb D}^1\tilde{\mathbb D}^0=0^\mathsf T$ (curl-free → 가짜 와도원 없음) (p.48).
- 흐름·구성·최종계: Eq. 2.23 (p.49)·Eq. 2.24 (p.50, "이산 에너지 보존 달성의 본질 단계")·Eq. 2.25 (p.51)·Eq. 2.26-2.27 (p.51 — C-grid 의 발현, Ch3 직선·Ch4 곡선·Ch5 삼각 격자의 공통 기반).
- **전역 에너지 보존 증명 (p.51-53)** — 성립 3조건 (p.53): ①이산 대류 연산자 반대칭 ②div $=-$gradᵀ (①②는 Verstappen & Veldman [102] 운동에너지 계보) ③면 질량플럭스 = 면직교속도 × **산술평균** 수심 (Eq. 2.24; 위치에너지용 추가 조건). 이류 연산자의 반대칭 부분 $\mathbb C$ 가 소거를 만듦.

## 4. 삼각격자 보존 증명 (Ch5 §5.7, p.75-83) — 로컬까지 확장

대상 스킴: 셀 기반 연속 Eq. 5.28·질량플럭스 Eq. 5.29-5.30($\bar h_f=\tfrac12(h_l+h_r)$)·엣지 기반 운동량 Eq. 5.31-5.32 (p.72-73; 직교 삼각격자 형식적 1차·균일격자 2차, 실측 supraconvergence §5.6.2).

- **질량 (§5.7.1, p.75-76)**: 로컬 = (5.28) 이 플럭스형이라 자동 — **어떤 질량플럭스 이산화에도 성립**. 전역 = 내부면 쌍소거, 경계 플럭스만 잔존.
- **운동량 (§5.7.2, p.76-78)**: staggered 격자엔 이산 운동량 벡터 방정식이 없어 **Perot [76] 재구성**으로 구성 — Eq. 5.33-5.35 + 기하 항등식(Eq. 5.26-5.27)으로 셀 운동량 방정식 유도 (p.77). **로컬 보존**: 이류+압력 플럭스가 인접 셀 간 유일 → "불연속 존재 시 약해로의 수렴 보장" (p.77); 유일 요건 = 이류의 **플럭스형** 표기 (Eq. 5.23, p.78). **전역 보존은 균일 수심($\nabla d=0$)에서만** — 실무에선 드묾(비균일 수심·바람·마찰·Coriolis 는 §5.8.2) 을 정직 명시 (p.78). 격자 직교성 불요.
- **에너지 (§5.7.3, p.79-83)**: §2.6.2 가 전역만 증명한 것과 달리 **로컬+전역** (p.79 명시). 연속 대상 Eq. 5.36(에너지수두 $h_e=\zeta+\mathbf u\cdot\mathbf u/2g$) → 이산 대응 **Eq. 5.41 (p.82)**. 성립 메커니즘: 운동부 = $\bar{\mathbf u}_f$ 를 **단순평균** $\tfrac12(\mathbf u_c+\mathbf u_{nc})$ 로 두면 이류 연산자가 반대칭("요구 반대칭성에 유일하게 가능한 선택", 가짜 운동에너지 증감 방지·aliasing 최소화, p.81) / 위치부 = **이산 곱규칙 Eq. 5.40 (p.81)** — $\nabla\cdot(\mathbf q\zeta)=\zeta\nabla\cdot\mathbf q+\mathbf q\cdot\nabla\zeta$ 의 이산판, div $=-$gradᵀ(Eq. 2.8)와 동치·summation-by-parts [60] 연계 (p.82). 전역 = 내부 소거, "총에너지 비증가 = 수치 안정성 진술" (p.82).
- **4대 요건 정리 (p.82-83)**: ①Perot 셀속도 재구성(Eq. 5.24 — 비본질, 이류 이산화의 귀결) ②$\bar{\mathbf u}_f$ 단순평균(임의 격자) ③질량플럭스 = 산술평균 수심 × 면직교속도(Eq. 5.29-5.30) ④이산 곱규칙(Eq. 5.40) = 압력구배와 질량플럭스 발산이 서로의 음전치.

## 5. 증명의 범위·한계 (disclosed)

- 전 증명은 **반이산**(공간만; 시간적분 leapfrog 는 Ch6 — Ch6 은 `Eq. (??)` 미해결 참조가 남은 초안 상태).
- **비점성·무외력** (2.1)-(2.2) 한정 — §5.8 분류: 비정수압 압력구배·점성응력은 운동량 보존 / 바닥경사 반력·저면마찰·바람·Coriolis 는 비보존.
- 쇄파·bore 는 **의도적 upwind 소산**으로 에너지 보존을 깨서 정칙화 (p.17·51) — SWASH 쇄파 처리(HFA)의 이론적 자리.

## 6. 문서 상태 실측 (overview 노트 갱신분)

- placeholder 장: **Ch4**(p.57 "under preparation" — 기존 목록에 누락)·Ch8(p.101 "yet empty")·Ch9·Ch10·Ch12. 부분 미완: Ch1 §1.1·**Ch6(`??` 참조)**. 완결: Ch2·Ch3 §3.1(비정수압 방정식 Eq. 3.1-3.2, p.55-56)·Ch5·Ch7(분산 해석)·Ch11 §11.1(SIP).
- ※Ch2 p.11 이 경계조건을 Ch10 으로 미루는데 Ch10 은 빈 장 — 경계조건 이론은 문서 밖(코드 노트 축).
