---
title: "이론 ch02 — 연속방정식: 질량보존 · 보존/비보존 형태 · incompressible 조건"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch01-conservation.md
  - textbook/notes/theory-ch00_5-math-tools.md
canonical_source: self
citation_status: verified
provenance: "교재 프로젝트 textbook-ai-data-full ch02(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착. 주 출처 = **water-wave-mechanics(D&D) §2.2 + hudspeth2005-wave-forces §3.2**(연안공학 표준 교재 D&D 가 incompressible 가정을 정량 근거와 함께 완결적으로 다룸). ★삭제 전 전체 코퍼스 grep(파일럿·T8 교훈): Mach number·solenoidal·1D 도관(A·u=const)·venturi/nozzle = 전 코퍼스 **0건** 확정 삭제(hydraulics-and-hydrology 미러는 실제로는 'Surge and Wave Modeling' 보고서라 수리학 도관흐름 없음). 오일러 1755 연속방정식 역사 = sea-level 의 '1755'는 전부 Lisbon 지진해일이라 무관 — 미이식. 미이식: 나비에 1822·워크예제·노즐 데모. depends_on ch01(마스터 balance μ=ρ 대입)·ch00.5(물질미분·발산). T9([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "water-wave-mechanics(D&D) p.25-26·38-39·44(§2.2 연속·압축률·incompressible·§2.3.4 발산·Euler) + hudspeth2005-wave-forces p.77-78(§3.2 연속 3형태) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch01-conservation.md
  - textbook/notes/theory-ch00_5-math-tools.md
  - textbook/notes/theory-ch08-linear-waves.md
---

# 연속방정식 — 질량보존 · 보존/비보존 · incompressible 조건

> 4-레이어 **① 이론** 노트. [[theory-ch01-conservation]] 의 마스터 balance 에 강도량 $\mu=\rho$(질량밀도)·$S=0$ 을 대입한 결과(근거 의존 ①→①).
> 탐색 링크(근거 의존 아님): 선형파 이론의 비압축·비회전 가정 [[theory-ch08-linear-waves]].

## 1. 질량 보존 — 보존형·비보존형·텐서형

- 마스터 balance 에 $\mu=\rho$, $S=0$ 대입 → **연속방정식(보존형)** $\dfrac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf{u})=0$ (water-wave-mechanics, p.25, Eq. 2.10 "conservation of mass equation"; hudspeth2005-wave-forces, p.78, Eq. 3.10a). "한 점의 밀도 변화 = 그 점에서 알짜 빠져나가는 질량 플럭스".
- **비보존형** $\dfrac{D\rho}{Dt}+\rho\nabla\cdot\mathbf{q}=0$ — 물질미분으로 표현(곱규칙 전개; 물질미분 정의는 [[theory-ch00_5-math-tools]] §7 canonical) (hudspeth2005-wave-forces, p.78, Eq. 3.10b; water-wave-mechanics, p.39: $\tfrac{1}{\rho}\tfrac{D\rho}{Dt}$ 형). **텐서형** $\partial_t\rho+u_j\partial_j\rho+\rho\partial_j u_j=0$ 병기 (hudspeth2005-wave-forces, p.78, Eq. 3.10c).
- 세 형태는 수학적으로 등가 — **순수 운동학적 원리**(속도장·밀도장만 관여, [[theory-ch01-conservation]] §3). ※원문 교재의 "conservative/non-conservative" 명명·작은 검사체적 6면 직접 유도는 [[theory-ch01-conservation]] 의 differential control volume 로 위임(복제 회피).

## 2. Incompressible 가정 — 정량 근거

- 물은 압축률이 매우 작음: 체적탄성계수 $E=2.07\times10^9\ \mathrm{N\,m^{-2}}$ — $1\times10^6\ \mathrm{N\,m^{-2}}$(1 MPa) 압력 증가에 밀도 변화 **0.05%** 에 불과 → "henceforth water is incompressible" (water-wave-mechanics, p.26, Eq. 2.12 문맥). ※원문 교재의 Mach 수 판정($\mathrm{Ma}<0.3$ 등)은 전 코퍼스 미확인 — 미이식(연안 유동은 압축률 근거로 충분).
- **비압축 조건 $\nabla\cdot\mathbf{u}=0$**: 비압축 유체는 $\tfrac{1}{\rho}\tfrac{D\rho}{Dt}=0$ 이므로 연속 비보존형에서 속도 발산이 0 → **divergenceless(nondivergent) flow** (water-wave-mechanics, p.26 Eq. 2.13·p.39, §2.3.4). 모든 위치에서 성립.
- 물리 의미: 한 방향 유량 변화가 있으면 다른 방향에 상쇄 유량 변화가 있어 **큐브 내 유체 축적 없음** (water-wave-mechanics, p.26, Fig. 2.1). 예: 2D corner 가속류 $u=-Axt,\ w=Azt$ → $\nabla\cdot\mathbf{u}=-At+At=0$ 비압축 (water-wave-mechanics, p.26, Example 2.1).

## 3. 두 가지 "비압축" 의미

- **강한 의미**: 밀도가 시공간 모두 상수 $\rho=\rho_0$ (water-wave-mechanics, p.26, "water is incompressible" 가정).
- **약한 의미**: 입자 따라간 밀도 일정 $D\rho/Dt=0$ — 공간적으로는 다를 수 있음(성층 stratification). 둘 다 연속 비보존형에서 $\nabla\cdot\mathbf{u}=0$ 로 귀결 (water-wave-mechanics, p.39; 성층 응용은 해양 밀도장 문맥). ※원문 교재의 명시적 "정의 A/정의 B" 이분 표기는 D&D 서술로 대체.

## 4. 응용 — 비회전·압력의 역할

- **무점성+비압축 → Euler**: inviscid·incompressible 유체는 수직응력(압력)만 작용, 전단응력 0 이라 유체 입자에 회전을 줄 응력이 없음 → 비회전 입자는 비회전 유지(초기 와도는 보존) (water-wave-mechanics, p.44, §2.3 Euler 벡터형). 선형파 이론의 퍼텐셜 유동 전제 → [[theory-ch08-linear-waves]].
- **압력의 역할**: 비압축 유동에서 압력은 상태방정식으로 결정되는 물리량이 아니라 $\nabla\cdot\mathbf{u}=0$ **제약을 만족시키는 양**(운동량식+비압축 결합, Poisson형으로 결정) — 상세는 ch04 N-S. ※Poisson 방정식 $\nabla^2 p=\ldots$ 명시 전개는 본 장 미이식(ch04 위임).

## 5. 연결

- [[theory-ch01-conservation]] — 마스터 balance(μ=ρ 대입 원천, 근거 의존)
- [[theory-ch00_5-math-tools]] — 물질미분·발산 (근거 의존)
- [[theory-ch08-linear-waves]] — 비압축·비회전 퍼텐셜 유동 응용 (탐색)
- 다음: ch03 Euler(마스터에 $\phi=\rho\mathbf{u}$+무점성)·ch04 N-S(+Newtonian 응력) — 연속은 이후 모든 장의 제약조건.
