---
title: "이론 ch08 — 선형 파동(Airy) · 분산관계 · 군속도 · 에너지"
topic: waves
layer: 1
depends_on: []
canonical_source: self
citation_status: verified
claims_total: 26
claims_attached: 24
claims_dropped: 2
claims_source_needed: 0
claims_basis: legacy-ledger
provenance: "교재 프로젝트 textbook-ai-data-full ch08(AI 합성 MDX, 무인용) 이식분 — 2026-07-12 원자 단언 분해 후 textbook/md 페이지 대조로 (source_id, page) 전수 부착. 미매칭 단언 2건(Lagrange 1788·Cauchy 1815 역사 연표) 삭제. T1 파일럿([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "water-wave-mechanics(Dean & Dalrymple) p.13·54·63(Eq3.9)·64-66·73-74(선형화)·77-80·78(§3.4.4 Eq3.40-42)·98·113-114·285·329 + holthuijsen2007 p.22-23·63·124·136(§5.4.1)·150·163·173-175·203·§5.5 — textbook/md 미러 페이지 직접 대조 (2026-07-12, Codex 게이트 ⓐ MODIFY 반영: 진행파 해 p.78 정정·선형화 페이지 분리·쓰나미/Phillips/Hasselmann 앵커 보강)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-12
related:
  - concepts/waves/01-concept.md
  - textbook/notes/waves-holthuijsen-toc.md
---

# 선형 파동 이론 (Airy) — 분산관계·입자 궤도·군속도·에너지

> 4-레이어 **① 이론** 노트. 위상평균·위상해상 모델 전부의 토대가 되는 소진폭 파 이론.
> 탐색 링크(근거 의존 아님): 도메인 요약 [waves/01-concept](../../concepts/waves/01-concept.md) · 스펙트럼 모델 구현은 `models/SWAN/`.

## 1. 가정과 지배방정식

선형(소진폭) 파 이론의 가정: 소진폭($a/L \ll 1$)·비점성·비회전·비압축, 체적력은 중력만. 비회전이므로 속도 포텐셜 $\mathbf{u} = \nabla\Phi$ 가 존재하고, 비압축 조건과 결합하면 **라플라스 방정식** $\nabla^2\Phi = 0$ — "가장 보편적인 수리물리 방정식 중 하나"로서 포텐셜 유동을 지배 (water-wave-mechanics, p.57). 선형 파 이론(Airy 이론)은 질량 보존과 운동량 보존 두 방정식(Laplace + Bernoulli)에 선형화된 경계조건을 더한 것 (holthuijsen2007, p.124).

## 2. 경계조건

| 경계 | 조건 | 출처 |
|---|---|---|
| 바닥 $z=-h$ | 관통 불가 — 수평 바닥에서 $w = 0$ (경사 바닥은 $w = -u\,dh/dx$) | (water-wave-mechanics, p.63, Eq. 3.9-3.10 — 총괄표는 p.58) |
| 자유표면 운동학(KFSBC) | 표면 $F = z-\eta = 0$ 위의 입자는 표면에 머무름(정의 p.63) → Taylor 전개·선형화로 $w = \partial\eta/\partial t$ at $z=0$ | (water-wave-mechanics, 정의 p.63·선형화 p.74) |
| 자유표면 동적(DFSBC) | 표면 압력 균일(대기압) — Bernoulli 식으로 표현(p.64-66, Eq. 3.13 계열), 2차 곱항 무시 선형화로 $\partial\Phi/\partial t + g\eta = 0$ at $z=0$ | (water-wave-mechanics, 표현 p.64-66·선형화 p.73) |

## 3. 진행파 해와 분산관계

진행파 ansatz $\eta = a\cos(kx-\omega t)$ 를 위 시스템에 대입하면 연직 구조 $F'' = k^2 F$ → 바닥 조건으로 $\cosh k(z+h)$ 형이 선택되어

$$ \Phi = \frac{ag}{\omega}\,\frac{\cosh k(z+h)}{\cosh kh}\,\sin(kx-\omega t) $$

(진행파 속도 포텐셜: water-wave-mechanics, **p.78 §3.4.4 Progressive Waves, Eq. 3.40-3.42** — 포텐셜 정의 p.54; 동형 해 holthuijsen2007, p.136 §5.4.1, Eq. 5.4.1. ⚠ p.78 md 미러는 OCR 로 식 본문 일부 소실 — 계수의 문자 단위 대조는 원 PDF 필요, 식 형태·유도 경로는 양 출처 정합). 두 자유표면 조건을 동시에 만족시키는 조건이 **분산관계**:

$$ \omega^2 = gk\tanh(kh) $$

(water-wave-mechanics, p.77; holthuijsen2007, p.63 — "$\omega^2 = gk\tanh(kd)$, 모든 파수 k 가 하나의 진동수에 대응"). 수심 $h$ 와 파수 $k$ 가 주어지면 진동수가 결정된다.

## 4. 깊은물·얕은물 한계

$\tanh(kh)$ 의 점근으로 (water-wave-mechanics, p.79-80):

- **깊은물** $kh \gg 1$: $\tanh\to 1$, $\omega^2 \approx gk$ → $c = \sqrt{g/k} = \sqrt{gL/2\pi}$ — 파장이 길수록 빠른 **분산성**.
- **얕은물** $kh \ll 1$: $\tanh\to kh$, $c \approx \sqrt{gh}$ — 파장 무관, 수심만으로 결정되는 **비분산**.
- 영역 구분: $kh > \pi$ (h/L > 1/2) 깊은물 / $kh < \pi/10$ (h/L < 1/20) 얕은물 / 그 사이 중간 — "shallow water, intermediate depth, deep water regions" (water-wave-mechanics, p.80; 얕은물 근사 적용 예 p.98).

산술 예(위 식의 적용, 별도 단언 아님): 쓰나미 — 해저 지진·사면활동 기원의 장파로, 대양에서 진폭이 작아 감지 어렵고 연안 접근 시 크게 증폭 (holthuijsen2007, p.23; 파 스케일 분류 Fig. 1.1, p.22). 대양 수심 4000 m 에서 얕은물 한계 적용 시 $c=\sqrt{9.8\times4000}\approx 198$ m/s ≈ 713 km/h.

## 5. 입자 궤도

선형해의 속도장에서 입자 변위는 **타원 궤도** — 반축 수평 $A = a\,\cosh k(z+h)/\sinh kh$, 수직 $B = a\,\sinh k(z+h)/\sinh kh$ ("equation of an ellipse with semiaxes A and B", water-wave-mechanics, p.98):

- 깊은물 점근: $A = B = a e^{kz}$ — 원 궤도, 반경이 깊이에 따라 지수 감쇠 (water-wave-mechanics, p.98 점근).
- 얕은물 점근($h/L<1/20$): 수평 반축이 커지고 깊이에 거의 무관, 수직 반축은 바닥 0 → 표면 $a$ 선형 — 납작한 타원 (water-wave-mechanics, p.98).
- 선형 이론에서 궤도는 닫힘 — 순 이동(질량 수송)은 2차(비선형) 효과: **mass transport(Stokes drift)** 는 별도 장에서 다룸 (water-wave-mechanics, ch.10 §10.2 Mass Transport, p.285).

## 6. 위상속도 vs 군속도

위상속도 $c=\omega/k$ 는 개별 마루, **군속도** $c_g = d\omega/dk$ 는 에너지·진폭 포락의 전파 속도. 분산관계 미분으로

$$ c_g = nC, \qquad n = \frac{1}{2}\left[1 + \frac{2kh}{\sinh 2kh}\right] $$

— $C_g = nC$ (Eq. 4.82) 이며 $n$ 의 깊은물·얕은물 점근이 각각 $1/2$·$1$ (water-wave-mechanics, p.114). 즉 깊은물에서 에너지는 마루의 절반 속도로, 얕은물에서는 마루와 같은 속도로 전파된다.

## 7. 에너지와 에너지 플럭스

- 시간 평균 에너지 밀도(단위 수면적당): $E = \frac{1}{8}\rho g H^2 = \frac{1}{2}\rho g a^2$ — "total average energy per unit surface area $E = KE + PE = \frac{1}{8}\rho g H^2$" (Eq. 4.75, water-wave-mechanics, p.113; 동일 결과 $E=\frac{1}{2}\rho g a^2$, holthuijsen2007, p.150).
- **에너지 플럭스**: 소진폭 파는 질량은 수송하지 않지만 에너지를 수송하며, 플럭스는 $F = E\,c_g$ (Energy Flux 절, water-wave-mechanics, p.113-114; 에너지 수송 = 군속도, holthuijsen2007, §5.5 Energy transport).
- 이 에너지 수송 개념이 스펙트럼 파랑 모델의 **에너지(작용) 평형 방정식**의 토대 — 바람 생성·소산·전파를 하나의 balance 로 다루는 틀 (holthuijsen2007, p.5 개관 및 ch.6).

## 8. 역사 연표 (코퍼스 실측분)

수파 역학의 실질적 출발은 한 세기 반 전: **Airy 의 선형 파 이론(1845)** → Stokes 고차 이론(1847) → Boussinesq 장파 이론(1872) → Michell(1893)·McCowan(1894) 한계파고 (water-wave-mechanics, p.13 verbatim 연표). 얕은물 약비선형의 Korteweg-DeVries 방정식은 1895 (water-wave-mechanics, p.329). 20세기 계보: 스펙트럼 형상의 Phillips(1958) 차원해석 (holthuijsen2007, p.173-175), 비선형 quadruplet 상호작용의 Hasselmann(1962) Boltzmann 적분 (holthuijsen2007, p.163·203).

> 원본 교재 챕터의 "1788 Lagrange·1815 Cauchy" 연표 2건은 코퍼스에서 페이지 확인 불가 → **삭제** (이식 원칙: 미매칭 단언은 잔존 금지).

## 9. 연결

- [[waves-holthuijsen-toc]] — holthuijsen2007 챕터 지도
- `concepts/waves/` 01(개념 요약)·02(이론) — 본 노트가 상세 이론 canonical (§8.1 소유권 규칙)
- 다음 이론 챕터: ch09 비선형·스펙트럼(T 트랙), ch12 조석(T2)
