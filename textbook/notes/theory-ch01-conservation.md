---
title: "이론 ch01 — 보존법칙의 뼈대: 검사체적 · Reynolds 수송정리 · 마스터 보존형식"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch00_5-math-tools.md
canonical_source: self
citation_status: verified
has_source_needed: true
provenance: "교재 프로젝트 textbook-ai-data-full ch01(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착. 주 출처 = **hudspeth2005-wave-forces §3(Fundamentals of Fluid Mechanics)** — Hudspeth 는 mass·momentum·energy 를 differential element method 로 개별 유도(§3.2·§3.3). ★마스터 보존법칙(일반 강도량 φ 의 ∂φ/∂t+∇·(φu)=S_φ)은 Hudspeth 에 일반형으로 명시 없음 — 연속(φ=ρ)·운동량(φ=ρu) 구체 사례로 부착하고 일반 φ 추상은 교재 교수법 틀로 표시. 미매칭 삭제/미이식: Reynolds 역사노트(1883 파이프 실험·1903 RTT 정식, 코퍼스 0건)·conservative/non-conservative 용어(Hudspeth 미사용, 두 형태 식은 실측)·워크 예제·강 위 배 비유. depends_on ch00.5(RTT·물질미분·발산정리·Taylor 근거 의존, 첫 ①→① 연쇄). T8([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "hudspeth2005-wave-forces p.69·75-80·91(§3.1 CV 3종·§3.2 연속·§3.3 운동량·§3.3.1 관성력) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch00_5-math-tools.md
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

## 2. Reynolds 수송정리 (RTT)

- 임의 검사체적에 대한 보존의 적분형 — 연속을 예로 $\dfrac{d}{dt}\iiint_{cv(t)}\rho\,dV+\oiint_{cs}\rho\mathbf{q}\cdot\mathbf{n}\,dS=0$ (hudspeth2005-wave-forces, p.78, §3.2, Eq. 3.11). 좌변=검사체적 내 양의 시간변화, 표면적분=경계 통과 알짜 플럭스 — 이 두 항 분해가 RTT 의 본질(근거 [[theory-ch00_5-math-tools]] §7 Leibniz·RTT).
- 표면적분→체적적분 변환은 **Gauss 발산정리** (hudspeth2005-wave-forces, p.69, Eq. 2.122a; 근거 [[theory-ch00_5-math-tools]] §5) — 적분형↔미분형 보존법칙을 잇는 결정적 단계. ※원문 교재의 Reynolds(1883 파이프 실험·1903 정식) 역사노트는 코퍼스 미확인 — 미이식.

## 3. 질량 보존 — 보존형과 비보존형

- 미분 검사체적의 질량 플럭스 균형에서 **연속 방정식**을 얻음: 보존형 $\dfrac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf{q})=0$, 비보존형 $\dfrac{D\rho}{Dt}+\rho\nabla\cdot\mathbf{q}=0$ — 두 형태는 등가 (hudspeth2005-wave-forces, p.77-78, Eq. 3.9·3.10). **순수 운동학적 원리**로, 미지장 중 속도장 $\mathbf{q}$·질량밀도 $\rho$ 만 관여 (p.78).
- 비보존형은 물질미분 $D/Dt=\partial_t+\mathbf{q}\cdot\nabla$ 로 표현됨(근거 [[theory-ch00_5-math-tools]] §7). ※원문 교재의 "conservative form / non-conservative form" 명명은 Hudspeth 미사용 — 두 형태 식만 이식(수치 유한체적의 보존성 의미는 모델 축).

## 4. 마스터 보존 구조 — 일반 강도량

- 모든 보존법칙은 **동일 구조 "국소 변화 + 대류 플럭스 발산 = 생성원"** 을 공유: 강도량 $\phi$ 에 대해 $\dfrac{\partial\phi}{\partial t}+\nabla\cdot(\phi\mathbf{u})=S_\phi$ (교재 교수법 틀; Hudspeth 는 이 일반형을 명시하지 않고 아래 구체 사례로 개별 유도). ※일반 강도량 마스터식 자체는 코퍼스 직접 지지 없음 — 구체 사례(질량·운동량)가 근거. <!-- citation_status: source-needed -->
- 강도량 대입으로 각 법칙이 나옴:
  - **질량**: $\phi=\rho$, $S=0$ → 연속 방정식 (§3, hudspeth2005-wave-forces p.78). → ch02.
  - **운동량**($i$성분): $\phi=\rho u_i$, $S=(\nabla\cdot\boldsymbol\sigma)_i+\rho f_i$ → 운동량 방정식 (§5). → ch03·ch04.
  - 에너지·물질 종은 후속(코퍼스 확보 시).

## 5. 운동량 원리 — 관성력의 국소·대류 분해

- **운동량 원리**: 미분 검사체적의 힘 균형 (hudspeth2005-wave-forces, p.78, §3.3). 단위체적당 힘 성분은 **관성(국소가속·대류가속)·체적력·점성전단응력 구배·수직응력 구배** (p.79, Table 3.1).
- **관성력 = 국소가속 + 대류가속**: Stokes 물질미분 연산자 적용 결과 $\dfrac{D\mathbf{q}}{Dt}=\underbrace{\dfrac{\partial\mathbf{q}}{\partial t}}_{\text{국소(병진)}}+\underbrace{(\mathbf{q}\cdot\nabla)\mathbf{q}}_{\text{대류(팽창·변형·회전)}}$ (hudspeth2005-wave-forces, p.79-80, §3.3.1, Eq. 3.14; 대류항은 미소요소의 변형·회전 기하에서, Lamb 1932). 이것이 N-S 좌변 $\rho D\mathbf{u}/Dt$ 의 정체.
- **무점성($\mu=0$)+비회전($\nabla\times\mathbf{q}=0$)** 가정 시 운동량 원리가 단순화 → Euler·Bernoulli 계열 (hudspeth2005-wave-forces, p.91; Phillips 1977 검토) → ch03.

## 6. 적분형 vs 미분형

- 같은 보존법칙을 **적분형**(arbitrary control volume, 전역·불연속 허용)과 **미분형**(differential control volume, 점별·매끄러운 해)으로 표현 — 두 형태는 발산정리로 연결 (hudspeth2005-wave-forces, p.75, §3.1). 본 계열(선형파 이론 전개)은 미분형 중심. ※충격파·불연속(적분형 강점)은 본 장 범위 밖.

## 7. 연결

- [[theory-ch00_5-math-tools]] — RTT·물질미분·발산정리·Taylor (근거 의존)
- 다음: ch02 연속방정식(마스터에 $\phi=\rho$)·ch03 Euler(운동량+무점성)·ch04 N-S(운동량+Newtonian 응력) — 모두 본 뼈대의 변형(후속 노트가 depends_on).
