---
title: "이론 ch07 — 와도: ∇×u · Kelvin 보존 · 2D/3D · planetary vorticity(Coriolis) · stream function"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch03-euler.md
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch00_5-math-tools.md
canonical_source: self
citation_status: verified
has_source_needed: true
provenance: "교재 프로젝트 textbook-ai-data-full ch07(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착. 주 출처 = **water-wave-mechanics(D&D) §2.3(와도·velocity potential·Kelvin) + stewart-physical-ocean(planetary/relative vorticity·2D/3D)**. ★삭제 전 전체 코퍼스 grep(정확 용어+개념 동의어+주 출처 절 통독, 페이지는 ---PAGE-N--- 마커로 확인=T13 행번호 착각 교훈): Lamb-Oseen vortex·solenoidal = 코퍼스 **0건** 삭제. 와도방정식 정식 Dω/Dt=(ω·∇)u+ν∇²ω·늘림항(vortex stretching)·Helmholtz 3정리(D&D 'Helmholtz'=방정식 이름 별개)·circulation Γ=∮u·dl 정식·Kelvin 순환 정리 유도·point vortex = 코퍼스 미확인 → source-needed. 미이식: 워크예제·비행기 후류·vortex atom. ★연안 핵심=planetary vorticity(Coriolis, Rossby)·비회전→velocity potential(ch08 파 이론). depends_on ch03(Euler→Kelvin)·ch04(N-S)·ch00.5(curl·벡터항등식). T14 기초 마지막([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "water-wave-mechanics(D&D) p.42-44·60(§2.3 와도 ∇×u=2Ω·velocity potential·Kelvin 1869 와도 보존) + stewart-physical-ocean p.38·212(2D/3D vortex lines·planetary/relative vorticity=Coriolis f) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch03-euler.md
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch08-linear-waves.md
  - textbook/notes/theory-ch12-tides.md
---

# 와도 — ∇×u · Kelvin 보존 · planetary vorticity · stream function

> 4-레이어 **① 이론** 노트. 유동의 **국소 회전**을 표현하는 와도 $\boldsymbol\omega=\nabla\times\mathbf{u}$ 관점 — [[theory-ch03-euler]] 무점성에서 Kelvin 와도 보존, [[theory-ch04-navier-stokes]] N-S 의 회전 형태(근거 의존 ①→①).
> 탐색 링크(근거 의존 아님): 비회전 퍼텐셜 유동 [[theory-ch08-linear-waves]] · 조석 Coriolis [[theory-ch12-tides]].

## 1. 와도 정의와 velocity potential

- **와도 $\boldsymbol\omega=\nabla\times\mathbf{u}$**: 속도 벡터의 curl(근거 [[theory-ch00_5-math-tools]] §3) — **유체 입자 회전율의 2배** $\nabla\times\mathbf{u}=2\boldsymbol\Omega$ (water-wave-mechanics, p.42-43, §2.3). 큰 흐름 패턴이 아닌 **국소 회전**이 핵심.
- **비회전(irrotational) → velocity potential**: 와도가 없는 유동은 속도를 스칼라 함수의 기울기로 표현 $\mathbf{u}=\nabla\phi$ — 흐름은 $\phi$ 감소 방향("downhill")으로 (water-wave-mechanics, p.42, §2.3). 이 비회전 조건이 선형파 퍼텐셜 유동의 전제 → [[theory-ch08-linear-waves]]. ※와도장의 $\nabla\cdot\boldsymbol\omega=0$(solenoidal)·와도관 개념은 코퍼스 미확인 — 미이식.

## 2. Kelvin 와도 보존

- **Kelvin(1869) 정리**: 무점성·비압축(Euler 유효) 유체는 전단응력이 0 이라 유체 입자에 회전을 줄 응력이 없음 → **와도·회전이 시간에 따라 변하지 않음**(초기 와도가 있으면 그대로 보존) (water-wave-mechanics, p.44, §2.3, "due to Lord Kelvin 1869"; 근거 [[theory-ch03-euler]] §4 무점성). 따름: **비점성 흐름은 와도를 만들거나 없앨 수 없음** — 와도는 외부 메커니즘(점성·벽)으로 생성되어야 함.
- ※순환 $\Gamma=\oint_C\mathbf{u}\cdot d\boldsymbol\ell$ 정식·Kelvin 순환 정리 $D\Gamma/Dt=0$ 유도·Helmholtz 3정리는 코퍼스 미확인 — source-needed(D&D 'Helmholtz'는 방정식 이름으로 별개). <!-- citation_status: source-needed -->

## 3. 와도방정식·늘림항 (3D vs 2D)

- **와도방정식**: N-S 의 회전을 취하면 압력항이 소거되고 와도의 물질미분 식 $\dfrac{D\boldsymbol\omega}{Dt}=(\boldsymbol\omega\cdot\nabla)\mathbf{u}+\nu\nabla^2\boldsymbol\omega$ 을 얻음(늘림·기울임항 + 점성 확산) — ※정식 유도·늘림항(vortex stretching)은 코퍼스 직접 미확인 — source-needed. <!-- citation_status: source-needed -->
- **3D vs 2D 와도**: 3차원 난류는 2차원과 근본적으로 다름 — **2D 에서는 와도선(vortex lines)이 항상 연직**이라 늘림 효과가 없음 (stewart-physical-ocean, p.38). 얕은(shallow) 대기·해양 유동이 2D 에 가까운 동역학.

## 4. Planetary vorticity — 연안·해양 응용

- ★**Planetary vorticity $f$**: 지구와 함께 회전하는 모든 것(해양·대기)이 갖는 와도 — **지구 자전율의 2배**, 곧 앞서의 **Coriolis 매개변수** $f=2\Omega\sin\phi$; 극에서 최대, 적도에서 0 (stewart-physical-ocean, p.212). [[theory-ch12-tides]] §2 Coriolis·Kelvin wave 와 연결.
- **Relative vorticity**: 해양·대기가 지구와 정확히 같은 속도로 돌지 않아 생기는 지구 대비 상대 회전 — 해류의 와도 (stewart-physical-ocean, p.212). 절대와도 = planetary + relative(Rossby 파·potential vorticity 계보). ※potential vorticity 보존 정식은 본 장 미이식(해양동역학 축).

## 5. Stream function (2D)

- **2D 비압축 유동은 흐름함수 $\psi$ 로 기술**: $u=\partial\psi/\partial y$, $v=-\partial\psi/\partial x$ — 연속방정식을 자동 만족, 두 유선 사이 체적유량 = $\psi$ 차 (water-wave-mechanics·hudspeth2005-wave-forces 에 광범위; [[theory-ch00_5-math-tools]] §8 stream function 근거). 와도와 $\nabla^2\psi=-\omega$(Poisson) 로 연결(정식은 source-needed). ※Lamb-Oseen vortex $\omega=\frac{\Gamma}{4\pi\nu t}e^{-r^2/4\nu t}$·point vortex 계는 코퍼스 0건 — 미이식. <!-- citation_status: source-needed -->

## 6. 연결

- [[theory-ch03-euler]] — 무점성 Euler(Kelvin 와도 보존의 전제) (근거 의존)
- [[theory-ch04-navier-stokes]] — N-S(회전→와도방정식) (근거 의존)
- [[theory-ch00_5-math-tools]] — curl·벡터 항등식·stream function (근거 의존)
- [[theory-ch08-linear-waves]] — 비회전 퍼텐셜 유동 (탐색)
- [[theory-ch12-tides]] — Coriolis·planetary vorticity (탐색)
- 다음: Phase 3 파동 역학(ch08 선형 파동) — 비회전·비압축 가정의 응용. **기초 유체역학(00.5-07) 완결.**
