---
title: "이론 ch01 — 보존법칙의 뼈대: 검사체적 · Reynolds 수송정리 · 마스터 보존형식"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch00_5-math-tools.md
canonical_source: self
citation_status: verified
claims_total: 25
claims_attached: 21
claims_dropped: 3
claims_source_needed: 1
claims_basis: legacy-ledger
has_source_needed: true
provenance: "교재 프로젝트 textbook-ai-data-full ch01(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착 + 같은 날 Codex 게이트(T8) MODIFY 반영. 주 출처 = **hudspeth2005-wave-forces §3(Fundamentals of Fluid Mechanics)** — mass·momentum·energy 를 differential element method 로 개별 유도. Codex 게이트 정정: ★마스터 balance 구조 = **holthuijsen2007 p.360 Eq.E.6**(임의 보존성질 μ 1D 수심적분형)+**Whitham hudspeth p.161 Eq.4.63** 실존 부착('코퍼스 0건' 오판 정정) — 3D 총플럭스형은 여전히 source-needed / 운동량 대입식 = Hudspeth p.90 §3.3.4 Eq.3.36(N-S)·p.91 §3.3.5 Euler 부착 / Reynolds 1883 = stewart p.130 실존(난류전이 실험)이나 RTT 계보와 무관해 범위 제외 / '적분형 불연속·미분형 매끄러운해' 대비 삭제(코퍼스 미확인) / §2 RTT·Gauss 식 재서술을 '질량 검사체적 적용'으로 축소(ch00.5 복제 회피). 미이식: conservative/non-conservative 명명(Hudspeth 미사용)·워크예제·강 위 배 비유. depends_on ch00.5(RTT·물질미분·발산정리·Taylor, 첫 ①→① 연쇄). T8([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "hudspeth2005-wave-forces p.69·75-80·90-91·161(§3.1 CV 3종·§3.2 연속·§3.3 운동량·§3.3.1 관성력·§3.3.4-5 N-S/Euler·Whitham 보존원리) + holthuijsen2007 p.360-361(부록 E 일반 balance E.6·질량 E.7-8) + stewart-physical-ocean p.130(Reynolds 1883) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14, Codex 게이트 재검증 포함)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch00_5-math-tools.md
  - textbook/notes/theory-ch09-nonlinear-spectra.md
---

# 보존법칙의 뼈대 — 검사체적 · RTT · 마스터 보존형식

> 4-레이어 **① 이론** 노트. 유체역학 지배방정식(질량·운동량·에너지)의 공통 유도 구조 — [[theory-ch00_5-math-tools]] 의 RTT·물질미분·발산정리를 검사체적 보존에 적용(근거 의존 ①→①, 첫 기초 연쇄).
> 탐색 링크(근거 의존 아님): 후속 ch02 연속·ch03 Euler·ch04 N-S 가 본 뼈대의 변형.

## 1. 검사체적의 세 가지 방법

- 유체역학 기본법칙 유도에 쓰이는 **검사체적(control volume)은 3종** (hudspeth2005-wave-forces, p.75, §3.1, Fig. 3.1):
  - **finite control volume** — 문제의 자연 경계를 식별하기 쉬울 때; 특정 검사체적에 한정.
  - **arbitrary control volume** — **수학적 유도에 가장 자주 사용**; 결과 적분식이 임의 시스템에 적용 가능(단 $dV=dx\,dy\,dz$ 등 명시 좌표 대입이 어려움).
  - **differential control volume** — arbitrary 와 유사하나 특정 좌표계의 미소 유체요소로 제한(13개 분리가능 좌표계 중 택일).
- 데카르트 미분 검사체적으로 기본법칙을 유도하며, 유체를 **연속체(continuum)=Eulerian field** 로 취급; 압축성 유체의 3개 미지장은 **질량밀도·압력·속도** (hudspeth2005-wave-forces, p.75-76). 유도 도구로 **Taylor 급수 전개**가 핵심 (p.76; 근거 [[theory-ch00_5-math-tools]] §2). ※원문 교재의 검사질량 vs 검사체적 이분법·강 위 배 비유는 Hudspeth 3종 분류로 대체.

## 2. Reynolds 수송정리 (RTT)의 적용

- RTT·발산정리 자체는 [[theory-ch00_5-math-tools]] §5·§7 canonical(재서술 금지) — 본 장은 이를 **질량 검사체적에 적용**: 임의 검사체적의 연속 적분형이 $\dfrac{d}{dt}\iiint_{cv(t)}\rho\,dV+\oiint_{cs}\rho\mathbf{q}\cdot\mathbf{n}\,dS=0$ 로 구체화됨 (hudspeth2005-wave-forces, p.78, §3.2, Eq. 3.11) — 검사체적 내 질량 변화 = 경계 통과 알짜 질량 플럭스.
- 표면적분→체적적분 변환(Gauss 발산정리)이 이 적분형을 §3의 미분형으로 잇는 결정적 단계(근거 [[theory-ch00_5-math-tools]] §5). ※원문 교재의 Reynolds 역사노트: 1883 관내 염료 실험은 난류전이(Re≈2000) 연구로 stewart-physical-ocean p.130 에 실존하나 **RTT 계보와 직접 관계가 약해 범위 제외**; RTT 의 1903 정식화 귀속은 코퍼스 미확인 — 미이식.

## 3. 질량 보존 — 보존형과 비보존형

- 미분 검사체적의 질량 플럭스 균형에서 **연속 방정식**을 얻음: 보존형 $\dfrac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf{q})=0$, 비보존형 $\dfrac{D\rho}{Dt}+\rho\nabla\cdot\mathbf{q}=0$ — 두 형태는 등가 (hudspeth2005-wave-forces, p.77-78, Eq. 3.9·3.10). **순수 운동학적 원리**로, 미지장 중 속도장 $\mathbf{q}$·질량밀도 $\rho$ 만 관여 (p.78).
- 비보존형은 물질미분 $D/Dt=\partial_t+\mathbf{q}\cdot\nabla$ 로 표현됨(근거 [[theory-ch00_5-math-tools]] §7). ※원문 교재의 "conservative form / non-conservative form" 명명은 Hudspeth 미사용 — 두 형태 식만 이식(수치 유한체적의 보존성 의미는 모델 축).

## 4. 마스터 보존 구조 — 일반 강도량

- 모든 보존법칙은 **동일 balance 구조 "국소 변화율 + 이류(transport) = 생성원"** 을 공유. 임의 보존 성질 $\mu$(밀도)에 대한 (1차원 수심적분) balance 방정식 $\dfrac{\partial(\mu D)}{\partial t}+\dfrac{\partial(u_x\mu D)}{\partial x}=S$ — 좌변=국소 변화율+이류항, 우변=단위면적·단위시간당 생성/소산원 (holthuijsen2007, p.360, Eq. E.6; $D=\eta+d$ 수주 높이). Whitham(1974)의 일반 보존원리 $\partial_t P+\partial_x Q(P)$(RTT 와 유사, 파동밀도 $P$·플럭스밀도 $Q(P)$)도 동형 (hudspeth2005-wave-forces, p.161, Eq. 4.63).
- **3차원·총플럭스 일반형** $\dfrac{\partial\phi}{\partial t}+\nabla\cdot\mathbf{J}=S_\phi$ — 플럭스 $\mathbf{J}$ 는 대류 $\phi\mathbf{u}$ + 비대류(응력·확산·열전도); 순수 대류 $\mathbf{J}=\phi\mathbf{u}$ 는 질량 사례. Holthuijsen 은 3D balance 를 §5.3.2 에서 다루고 1D(E.6)를 그 유추로 유도. ※3D 총플럭스 마스터식의 완전 전사는 코퍼스 페이지 미확정 — 1D(E.6)·Whitham(4.63)이 지지. <!-- citation_status: source-needed -->
- 강도량 대입으로 각 법칙이 나옴:
  - **질량**: $\mu=\rho$, $S=0$ → 연속 방정식 (holthuijsen2007 p.361, Eq. E.7→E.8; 3D 는 hudspeth2005-wave-forces p.78). → ch02.
  - **운동량**: 비압축 Newtonian 유체의 **N-S** $\rho\partial_t\mathbf{q}+\rho(\mathbf{q}\cdot\nabla)\mathbf{q}=-\nabla(p+\rho gz)+\mu\nabla^2\mathbf{q}$ (hudspeth2005-wave-forces, p.90, §3.3.4, Eq. 3.36)·무점성이면 **Euler** (p.91, §3.3.5) → ch03·ch04.
  - **에너지**: Hudspeth §3.4 Mechanical Energy Principle 에 있으나 후속 장으로 범위 이연.

## 5. 운동량 원리 — 관성력의 국소·대류 분해

- **운동량 원리**: 미분 검사체적의 힘 균형 (hudspeth2005-wave-forces, p.78, §3.3). 단위체적당 힘 성분은 **관성(국소가속·대류가속)·체적력·점성전단응력 구배·수직응력 구배** (p.79, Table 3.1).
- **관성력 = 국소가속 + 대류가속**: Stokes 물질미분 연산자 적용 결과 $\dfrac{D\mathbf{q}}{Dt}=\underbrace{\dfrac{\partial\mathbf{q}}{\partial t}}_{\text{국소(병진)}}+\underbrace{(\mathbf{q}\cdot\nabla)\mathbf{q}}_{\text{대류(팽창·변형·회전)}}$ (hudspeth2005-wave-forces, p.79-80, §3.3.1, Eq. 3.14; 대류항은 미소요소의 변형·회전 기하에서, Lamb 1932). 이것이 N-S 좌변 $\rho D\mathbf{u}/Dt$ 의 정체.
- **무점성($\mu=0$)+비회전($\nabla\times\mathbf{q}=0$)** 가정 시 운동량 원리가 단순화 → Euler·Bernoulli 계열 (hudspeth2005-wave-forces, p.91; Phillips 1977 검토) → ch03.

## 6. 적분형 vs 미분형

- 같은 보존법칙을 **arbitrary control volume**(적분형, 임의 시스템 적용)과 **differential control volume**(미분형, 특정 좌표계 미소요소)로 표현 — 두 방법은 발산정리로 연결 (hudspeth2005-wave-forces, p.75, §3.1). 본 계열(선형파 이론 전개)은 데카르트 미분 검사체적 중심. ※"적분형은 불연속 허용·미분형은 매끄러운 해" 대비는 코퍼스 직접 확인 안 됨 — 미이식(충격파 등은 본 장 범위 밖).

## 7. 연결

- [[theory-ch00_5-math-tools]] — RTT·물질미분·발산정리·Taylor (근거 의존)
- 다음: ch02 연속방정식(마스터에 $\phi=\rho$)·ch03 Euler(운동량+무점성)·ch04 N-S(운동량+Newtonian 응력) — 모두 본 뼈대의 변형(후속 노트가 depends_on).
