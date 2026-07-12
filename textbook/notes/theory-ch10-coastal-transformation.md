---
title: "이론 ch10 — 연안 파 변형: 천수·굴절·회절·쇄파·setup·연안류"
topic: waves
layer: 1
depends_on:
  - textbook/notes/theory-ch08-linear-waves.md
  - textbook/notes/theory-ch09-nonlinear-spectra.md
canonical_source: self
citation_status: verified
provenance: "교재 프로젝트 textbook-ai-data-full ch10(AI 합성 MDX, 무인용) 이식분 — 2026-07-12 원자 단언 분해·(source_id, page) 부착. ★원문 계보 오류 1건 대체(회절 해석해 'Sommerfeld 1896'→코퍼스 실측 Penney & Price 1952), 미매칭 삭제 4건(Fresnel 적분식 전개·연안류 5π/16 폐형식 계수·setup ~0.15Hb 크기·rip 익사 80% 통계). rip 상세·해안보호 구조물(§10.6-10.7)은 개념·설계 축 — concepts 탐색 위임. T4([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "water-wave-mechanics(D&D) p.121·124·128-129·132-133·177·303-309·351 + holthuijsen2007 p.207·215·222·260 — textbook/md 미러 페이지 직접 대조 (2026-07-12)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-12
related:
  - textbook/notes/theory-ch08-linear-waves.md
  - textbook/notes/theory-ch09-nonlinear-spectra.md
  - concepts/waves/02-theory.md
  - concepts/rip-currents/01-concept.md
---

# 연안 파 변형 — 천수·굴절·회절·쇄파·setup·연안류

> 4-레이어 **① 이론** 노트. 외양 파([[theory-ch08-linear-waves]]·[[theory-ch09-nonlinear-spectra]])가 연안 수심 변화에서 겪는 변형(근거 의존 ①→①).
> 탐색 링크(근거 의존 아님): rip 상세 `concepts/rip-currents/` · 해안 보호 구조물·설계 `concepts/waves/06`·KDS 노트 · 모델 구현 [[wave-breaking-cross-model]].

## 1. 천수효과 (Shoaling)

- 완경사·수직입사·무마찰에서 **에너지 플럭스 보존** $E\,c_g = \text{const}$ ([[theory-ch08-linear-waves]] §7 의 $F=Ec_g$ 에서) → $H_1/H_0 = \sqrt{c_{g,0}/c_{g,1}}$ — **천수 계수 $K_s$** 로 도표화 (water-wave-mechanics, p.124, shoaling coefficient). 개념 정의: 천수 = 전파 방향 수심 변화에 의한 군속도 변화가 만드는 진폭 변화 (holthuijsen2007, p.215).
- 얕아질수록 $c_g$ 감소 → 동일 플럭스 수송에 큰 $E \propto H^2$ 필요 → 파고 증가.

## 2. 굴절 (Refraction)

- **Snell 법칙**: $\sin\theta/c = \text{const}$ — 기하광학에서 온 관계로 수심(→위상속도) 변화가 파선을 휘게 함 (Eq. 4.109, water-wave-mechanics, p.121; 명명 유래 Snellius, holthuijsen2007, p.222). 해안 접근 시 파봉이 등수심선에 평행해짐.
- 직선·평행 등수심선에서 **굴절 계수 $K_r$** 산정 가능 — 실용 합성 $H = K_s K_r H_0$ (water-wave-mechanics, p.124).
- 파선 집중(곶)→파고·침식 집중, 분산(만)→감쇠 — 굴절·천수·회절의 역할 구분은 holthuijsen2007, p.215.

## 3. 회절 (Diffraction)

- 진폭의 수평 변화가 유발하는 전파 방향 변화 — 기하학적 그늘 영역으로 파가 휘어 들어감 (holthuijsen2007, p.215). 전형: **방파제 차폐면** 뒤로 교란 전달 (water-wave-mechanics, p.132).
- 반무한 방파제류 구조물의 회절 해석해 계보는 **Penney & Price(1952)** 검토로 정리 (water-wave-mechanics, p.133). ※원문 교재의 "Sommerfeld 1896" 표기·Fresnel 적분 전개식은 코퍼스 미확인 — 출처 실측 계보로 대체·미이식.

## 4. 쇄파

- 천수로 파고 증가 → 한계 도달: 얕은물 $H_b/h_b = 0.78$(경사 의존 보정 Weggel 1972) (water-wave-mechanics, p.129), 깊은물 경사 한계 $H/L_0=0.142$ (p.351; 심해 관측 ~0.14, holthuijsen2007, p.207).
- 쇄파 유형은 **Iribarren 수** $\xi$ 로 분류 — spilling/plunging/collapsing·surging (Battjes 1974 정리, holthuijsen2007, p.260; plunging=가파른 해빈, water-wave-mechanics, p.128-129). [[theory-ch09-nonlinear-spectra]] §2 와 공유.

## 5. Wave setup·setdown — radiation stress

- 파는 운동량 플럭스 **radiation stress** 를 수송: $S_{xx} = \int p\,dz - \frac{1}{2}\rho g(h+\bar\eta)^2 + \rho\overline{u^2}\ldots = E(2n-\tfrac12)$ 꼴 (Eq. 10.23, water-wave-mechanics, p.306).
- 쇄파 전 완만한 **setdown**(p.303), 쇄파대에서 onshore 운동량 플럭스 감소를 평균 수위 상승으로 보상하는 **setup**(p.307) — 평균 수면 경사가 $dS_{xx}/dx$ 와 평형. ※크기 "~0.15 H_b" 수치는 코퍼스 페이지 미확인 — 미이식.
- surf zone 의 set-up·wave groupiness 조합이 부진동 등 저주파 운동을 생성 (holthuijsen2007, p.215).

## 6. 연안 흐름

- 경사 입사 쇄파의 해안 평행 운동량 전달 → **연안류(longshore current)** — 방향 규칙·발생은 water-wave-mechanics, p.177, 정량 이론 계보는 **Longuet-Higgins(1970)** (p.309, 선형 이론으로 평균류를 계산하는 §10 요약). ※폐형식 $V=\frac{5\pi}{16}\ldots$ 계수는 코퍼스에서 문자 확인 불가 — 미이식.
- **Rip current**(쇄파대 유입 질량의 국소 외해 방출)는 도메인 토픽이 canonical — `concepts/rip-currents/`(탐색 위임; 원문 교재의 "익사 80%" 통계는 무출처라 미이식).

## 7. 연결

- [[theory-ch08-linear-waves]]·[[theory-ch09-nonlinear-spectra]] — 에너지 플럭스·쇄파 한계 (근거 의존)
- `concepts/rip-currents/`·`concepts/waves/` — 도메인·설계 (탐색)
- 다음: ch13 표사 이송 — 본 장의 쇄파대 흐름이 이송의 원동력.
