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
claims_total: 18
claims_attached: 18
claims_dropped: 0
claims_source_needed: 0
claims_basis: legacy-ledger
has_source_needed: false
provenance: "교재 프로젝트 textbook-ai-data-full ch07(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착 + 같은 날 Codex 게이트(T14) MODIFY 반영. 주 출처 = **water-wave-mechanics(D&D) §2.3(와도·velocity potential·Kelvin) + stewart-physical-ocean §12(planetary/relative/potential vorticity·2D/3D)**. Codex 게이트 정정: ★velocity potential 부호 오류 u=∇φ→**u=-∇φ**(D&D p.42 Eq.2.70)·★늘림항·potential vorticity 보존 = stewart §12.2 실존('source-needed' 오판 철회) — Π=(ζ+f)/H 궤적 보존(p.215-216 Eq.12.9)·figure skater 늘림(p.216 Fig.12.2). Lamb-Oseen·solenoidal = 코퍼스 0건 삭제. 와도방정식 N-S 회전 정식 유도·Helmholtz 3정리(D&D 'Helmholtz'=방정식 이름 별개)·circulation Γ=∮u·dl 정식·Kelvin 순환 정리 유도·point vortex = 코퍼스 미확인 → source-needed. 미이식: 워크예제·비행기 후류·vortex atom. ★연안 핵심=planetary/potential vorticity(Coriolis·Rossby)·비회전→velocity potential(ch08). depends_on ch03·ch04·ch00.5. T14 기초 마지막([THEORY-LEDGER](../THEORY-LEDGER.md)). ★R1 I-3 코퍼스 확장(2026-07-17): kundu-cohen-2008(4판, 사용자 제공) 등록으로 source-needed 소진 — solenoidal(p.179 Eq.5.10)·순환/Kelvin 1868/Helmholtz 1858(p.93·173-176·178)·와도방정식(p.179 Eq.5.13)·Biot-Savart(p.180-181)·Lamb-Oseen 선와류 감쇠(p.344-347) 전건 부착 — sn 3 해소 + 삭제 2(solenoidal·Lamb-Oseen) 복원 → **18/18 (100%)**."
verification_method: "water-wave-mechanics(D&D) p.42-44·60(§2.3 와도 ∇×u=2Ω·velocity potential u=-∇φ Eq.2.70·Kelvin 1869 와도 보존) + stewart-physical-ocean p.38·212·215-216(2D/3D vortex lines·planetary/relative vorticity=Coriolis f·§12.2 potential vorticity Π=(ζ+f)/H 보존·figure skater) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14, Codex 게이트 재검증 포함). + kundu-cohen-2008 실측(2026-07-17): p.61·93·173-181·344-347 마커 실측."
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
- **비회전(irrotational) → velocity potential**: 와도가 없는 유동은 속도를 스칼라 함수의 (음의) 기울기로 표현 $\mathbf{u}=-\nabla\phi$ — 흐름은 $\phi$ 감소 방향("downhill")으로 (water-wave-mechanics, p.42, §2.3, Eq. 2.70; $\phi$ 단위 = 길이²/시간). 이 비회전 조건이 선형파 퍼텐셜 유동의 전제 → [[theory-ch08-linear-waves]]. 와도장은 항상 **solenoidal** $\nabla\cdot\boldsymbol\omega=0$(curl 의 발산=0) (kundu-cohen-2008, p.179, Eq. 5.10 — R1 코퍼스 확장으로 복원).

## 2. Kelvin 와도 보존

- **Kelvin(1869) 정리**: 무점성·비압축(Euler 유효) 유체는 전단응력이 0 이라 유체 입자에 회전을 줄 응력이 없음 → **와도·회전이 시간에 따라 변하지 않음**(초기 와도가 있으면 그대로 보존) (water-wave-mechanics, p.44, §2.3, "due to Lord Kelvin 1869"; 근거 [[theory-ch03-euler]] §4 무점성). 따름: **비점성 흐름은 와도를 만들거나 없앨 수 없음** — 와도는 외부 메커니즘(점성·벽)으로 생성되어야 함.
- **순환(circulation)**: $\Gamma=\oint_C\mathbf{u}\cdot d\boldsymbol\ell$ — Stokes 정리로 $\Gamma=\int_A\boldsymbol\omega\cdot d\mathbf{A}$(와도의 플럭스; 한 점의 와도 = 단위면적당 순환) (kundu-cohen-2008, p.93, Eq. 3.18). **Kelvin(1868) 순환 정리** $D\Gamma/Dt=0$ — 무점성·barotropic·보존 체적력·비회전 좌표계 4조건 하에서 물질 폐곡선의 순환 보존(유도 = 운동량 방정식의 선적분, Eq. 5.7-5.8) (kundu-cohen-2008, p.173-175, 제약 4조건 상세 p.176). **Helmholtz(1858) 와류 정리**: 와도선은 유체와 함께 이동·와류관 강도(순환)는 길이 방향 일정 등 — Kelvin 이 이 작업에서 순환 개념 도입 (kundu-cohen-2008, p.173·178; D&D 'Helmholtz'는 방정식 이름으로 별개).

## 3. 와도방정식·늘림항 (3D vs 2D)

- **와도방정식**: N-S 의 회전(curl)을 취하면 압력·중력(보존력) 항이 소거되고 $\dfrac{D\boldsymbol\omega}{Dt}=(\boldsymbol\omega\cdot\nabla)\mathbf{u}+\nu\nabla^2\boldsymbol\omega$ — 우변 1항 = 와도 늘림·기울임(vortex stretching/tilting), 2항 = 와도의 점성 확산 (kundu-cohen-2008, p.179, Eq. 5.11-5.13; 상수 ρ·보존 체적력 조건, R1 코퍼스 확장으로 승격).
- **늘림항의 물리(figure skater)**: 유체 기둥의 깊이 $H$ 가 변하면 관성모멘트가 바뀌어 회전율(relative vorticity)이 변함 — 피겨스케이터가 팔을 뻗으면 관성모멘트↑·회전↓ 하는 것과 같음 (stewart-physical-ocean, p.216, §12.2, Fig. 12.2). 이것이 늘림항의 각운동량 보존 해석.
- **3D vs 2D 와도**: 3차원 난류는 2차원과 근본적으로 다름 — **2D 에서는 와도선(vortex lines)이 항상 연직**이라 늘림 효과가 없음 (stewart-physical-ocean, p.38). 얕은(shallow) 대기·해양 유동이 2D 에 가까운 동역학.

## 4. Planetary vorticity — 연안·해양 응용

- ★**Planetary vorticity $f$**: 지구와 함께 회전하는 모든 것(해양·대기)이 갖는 와도 — **지구 자전율의 2배**, 곧 앞서의 **Coriolis 매개변수** $f=2\Omega\sin\phi$; 극에서 최대, 적도에서 0 (stewart-physical-ocean, p.212). [[theory-ch12-tides]] §2 Coriolis·Kelvin wave 와 연결.
- **Relative vorticity $\zeta$**: 해양·대기가 지구와 정확히 같은 속도로 돌지 않아 생기는 지구 대비 상대 회전 — 해류의 와도 (stewart-physical-ocean, p.212). 절대와도 = planetary($f$) + relative($\zeta$).
- **Potential vorticity 보존**: $\Pi=\dfrac{\zeta+f}{H}$ 가 **유체 궤적을 따라 보존**됨 — 깊이 $H$·상대와도 $\zeta$·위도(planetary $f$) 변화가 서로 결합 (stewart-physical-ocean, p.215-216, §12.2, Eq. 12.9; 성층 유체는 Pedlosky 1987 형). Rossby 파·서안 경계류의 기반 — 조석·해류 [[theory-ch12-tides]] 와 연결.

## 5. Stream function (2D)

- **2D 비압축 유동은 흐름함수 $\psi$ 로 기술**: $u=\partial\psi/\partial y$, $v=-\partial\psi/\partial x$ — 연속방정식을 자동 만족, 두 유선 사이 체적유량 = $\psi$ 차 (water-wave-mechanics·hudspeth2005-wave-forces 에 광범위; [[theory-ch00_5-math-tools]] §8 stream function 근거). 와도와는 Poisson 관계로 연결 — 벡터 퍼텐셜 정식화·Biot-Savart 법칙(와류 필라멘트 유발 속도) (kundu-cohen-2008, p.180-181, §5.6). **선와류(line vortex)의 점성 감쇠(Lamb-Oseen)**: 초기 비회전 와류가 점성으로 확산하는 자기상사 해 $u_\theta/(\Gamma/2\pi r)=F(r/\sqrt{\nu t})$ (kundu-cohen-2008, p.344-347, §9.9 Decay of a Line Vortex, Eq. 9.41-45 — R1 코퍼스 확장으로 복원).

## 6. 연결

- [[theory-ch03-euler]] — 무점성 Euler(Kelvin 와도 보존의 전제) (근거 의존)
- [[theory-ch04-navier-stokes]] — N-S(회전→와도방정식) (근거 의존)
- [[theory-ch00_5-math-tools]] — curl·벡터 항등식·stream function (근거 의존)
- [[theory-ch08-linear-waves]] — 비회전 퍼텐셜 유동 (탐색)
- [[theory-ch12-tides]] — Coriolis·planetary vorticity (탐색)
- 다음: Phase 3 파동 역학(ch08 선형 파동) — 비회전·비압축 가정의 응용. **기초 유체역학(00.5-07) 완결.**
