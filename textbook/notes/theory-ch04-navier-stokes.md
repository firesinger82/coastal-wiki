---
title: "이론 ch04 — Navier-Stokes: 변형률 텐서 · Newtonian 구성식 · Stokes 법칙 · Reynolds 수 · Poiseuille"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch03-euler.md
  - textbook/notes/theory-ch00_5-math-tools.md
canonical_source: self
citation_status: verified
provenance: "교재 프로젝트 textbook-ai-data-full ch04(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착. 주 출처 = **hudspeth2005-wave-forces §3.3.3-4(Newtonian 구성식·Stokes 점성마찰·N-S)·§3.6(무차원 상사) + water-wave-mechanics(D&D)**. ★삭제 전 전체 코퍼스 grep(정확 용어+개념 동의어): Millennium/Clay N-S 문제 = 코퍼스 **미확인**(stewart 'Millennium'=기상학회 서지·'Clay'=점토광물, N-S 밀레니엄 문제 아님) 삭제·bulk viscosity 용어 0건. Reynolds 임계값 2300·점성값 표·Re 일상값 표·워크예제·RANS 예고(ch05 이연)는 미이식. Stokes 가정 λ=-2μ/3 은 Hudspeth Eq.3.29d 의 -(1/3)∇·q 형태로 내장. depends_on ch03(Cauchy 운동량+무점성 대비)·ch00.5(변형률 분해·발산·Laplacian). T11([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "hudspeth2005-wave-forces p.83·87-90·101-102(§3.3.3 Newtonian·Stokes 점성마찰·§3.3.4 N-S Eq.3.36·§3.6 무차원 Table 3.2) + water-wave-mechanics(D&D) p.280(no-slip) + mechanics-of-sediment-transport p.828(Poiseuille) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch03-euler.md
  - textbook/notes/theory-ch00_5-math-tools.md
  - textbook/notes/theory-ch09-nonlinear-spectra.md
---

# Navier-Stokes — 변형률 텐서 · Newtonian 구성식 · Reynolds 수

> 4-레이어 **① 이론** 노트. [[theory-ch03-euler]] 의 Cauchy 운동량 방정식에 **점성(Newtonian 구성식)** 을 넣어 완전한 운동량 보존을 얻음 — Euler(무점성)의 확장(근거 의존 ①→①).
> 탐색 링크(근거 의존 아님): 난류·비선형 스펙트럼 [[theory-ch09-nonlinear-spectra]] · RANS(ch05)·경계층(ch06).

## 1. 점성 응력 — 편차 응력텐서

- 점성 유체의 총 응력은 **등방 압력 $-p\delta_{ij}$ + 편차 응력(deviatoric stress) $\sigma_{ij}^{dev}$**(점성·속도구배 기인): $\tau_{ij}=-p\delta_{ij}+\sigma_{ij}^{dev}$ (hudspeth2005-wave-forces, p.87, Eq. 3.29, Batchelor 1983 p.142). 무점성(Euler)은 편차부가 0 — [[theory-ch03-euler]] §3 의 $\boldsymbol\sigma=-p\mathbf{I}$.
- 압력 $p$ 측정이 어려운 이유: 편차 정규응력이 있어 속도구배가 0 이거나 유체가 정지해야 순수 압력을 잼 (hudspeth2005-wave-forces, p.87).

## 2. 변형률 텐서 — 속도구배 분해

- 속도구배 $\partial u_i/\partial x_j$ = **변형률률 텐서(대칭부, strain-rate) $\varepsilon_{ij}=\tfrac12(\partial_j u_i+\partial_i u_j)$ + 회전 텐서(반대칭부, vorticity) $\omega_{ij}$** (근거 [[theory-ch00_5-math-tools]] §6, hudspeth2005-wave-forces p.83). 변형률=모양 변화(전단·팽창), 회전=강체 회전.
- ★**점성 응력은 변형률에만 응답, 순수 회전에는 발생하지 않음** — Stokes 점성마찰법칙은 편차 전단응력을 **각변형률(rate of angular deformation)** 에 관계 (hudspeth2005-wave-forces, p.87, §3.3.3). 강체 회전에는 상대 운동이 없어 마찰 무발생.

## 3. Newtonian 구성식과 Stokes 가정

- **Stokes 점성마찰법칙(Newtonian)**: 탄성 고체 응력과의 유추로 편차 정규응력을 $\sigma_{xx}^{dev}=2\mu\!\left(\dfrac{\partial u}{\partial x}-\dfrac13\nabla\cdot\mathbf{q}\right)$ 꼴로 씀 — 전단 점성계수 $\mu$ (hudspeth2005-wave-forces, p.87-89, Eq. 3.29d). 일반형 $\sigma_{ij}=-p\delta_{ij}+2\mu\!\left(\varepsilon_{ij}-\tfrac13(\nabla\cdot\mathbf{q})\delta_{ij}\right)$.
- **Stokes 가정 내장**: 위 $-\tfrac13\nabla\cdot\mathbf{q}$ 항이 곧 체적 점성 $\lambda=-\tfrac23\mu$ 채택(응력 트레이스가 압력만으로 표현) — 음파·충격파 외 대부분 흐름에서 유효 (hudspeth2005-wave-forces, p.87-89). ※원문 교재의 "bulk viscosity/second viscosity" 용어·λ 별도 명시는 코퍼스 미확인 — Stokes 형만 이식.

## 4. Navier-Stokes 방정식

- Cauchy 운동량([[theory-ch03-euler]] §3)에 Newtonian 응력 발산을 대입 → **비압축 N-S**: $\rho\dfrac{\partial\mathbf{q}}{\partial t}+\rho(\mathbf{q}\cdot\nabla)\mathbf{q}=-\gamma\nabla(U+z)+\mu\nabla^2\mathbf{q}$ ($\gamma=\rho g$, 중력 체적력 $F_B=-\rho g\nabla z$) (hudspeth2005-wave-forces, p.90, §3.3.4, Eq. 3.36, Lamb 1932). 동점성 $\nu=\mu/\rho$ 로 나눈 kinematic 형: $\partial_t\mathbf{u}+(\mathbf{u}\cdot\nabla)\mathbf{u}=-\tfrac1\rho\nabla p+\nu\nabla^2\mathbf{u}+\mathbf{f}$.
- 5항의 의미: 국소가속·**비선형 대류가속** $(\mathbf{u}\cdot\nabla)\mathbf{u}$·압력구배·**점성 확산** $\nu\nabla^2\mathbf{u}$·체적력. ★비선형 대류항이 난류·와류·박리 등 풍성한 동역학의 원천(무점성이면 [[theory-ch03-euler]] §5 d'Alembert 역설). ※원문 교재의 Clay Millennium 문제(3D N-S 매끄러움) 단언은 코퍼스 미확인 — 미이식.

## 5. 무차원화 — Reynolds 수와 상사

- 물리 모델링은 **3가지 상사(similitude)** 보존 필요: 기하·운동학·동역학 (hudspeth2005-wave-forces, p.101, §3.6). N-S 무차원화에서 **무차원 힘비**들이 등장 (Table 3.2).
- **Reynolds 수 $\mathrm{Re}=\dfrac{Ub}{\nu}=\dfrac{\rho Ub}{\mu}$ = 관성/점성 힘비** (hudspeth2005-wave-forces, p.102, Table 3.2). 같은 표의 병렬 무차원수: **Froude** $U^2/gb$(관성/중력)·**Cauchy** $\rho U^2/E$(관성/탄성)·**Euler** $\rho U^2/2\Delta p$(관성/압력)·**Weber** $\rho bU^2/\sigma$(관성/표면장력)·**Keulegan-Carpenter** $UT/b$·**Strouhal** $b/UT$(와류 방출). $\mathrm{Re}$ 가 같으면 동역학 상사 — 모형↔실물 유동 예측 가능.
- $\mathrm{Re}\gg1$ 관성 압도(경계층·난류 가능), $\mathrm{Re}\ll1$ 점성 압도(Stokes 흐름). ※원문 교재의 파이프 임계 $\mathrm{Re}_c\approx2300$·Re 일상값 표는 미이식(임계값은 stewart p.130 Reynolds 실험 문맥에 실존, 본 장 범위 밖).

## 6. Poiseuille 흐름·경계조건

- **no-slip 경계조건**: 벽에서 유체 속도 = 0 (water-wave-mechanics, p.280, 파 경계층 문맥 $u=0$ at bed).
- **Poiseuille 흐름**: 압력구배 구동 관/평판 층류의 **포물선 속도 분포** 정확해 — N-S 가 해석적으로 풀리는 대표 예 (mechanics-of-sediment-transport, p.828, "conventional Poiseuille formula"). ※원문 교재의 평판 유도 전개·Hagen-Poiseuille $Q\propto R^4$·마이크로유체 응용은 미이식(핵심 결과·귀속만).

## 7. 한계 — 난류(RANS 예고)

- $\mathrm{Re}\gg1$ 에서 해는 난류가 되어 직접수치해가 격자 폭증으로 불가 → **통계 평균 + 난류 모델(RANS)** 필요 — 속도를 평균+변동으로 분해하면 **Reynolds 응력** $-\overline{u_i'u_j'}$ 이 등장, 이를 모델링(k-ε 등) — 상세는 ch05 (탐색; [[theory-ch09-nonlinear-spectra]] 스펙트럼과 연결). ※RANS 정식은 코퍼스 확보 후 ch05 canonical.

## 8. 연결

- [[theory-ch03-euler]] — Cauchy 운동량·무점성 Euler (근거 의존)
- [[theory-ch00_5-math-tools]] — 변형률/회전 분해·발산·Laplacian (근거 의존)
- [[theory-ch09-nonlinear-spectra]] — 난류·비선형 (탐색)
- 다음: ch05 RANS(난류 평균)·ch06 경계층(Prandtl·d'Alembert 해결)·ch07 와도방정식.
