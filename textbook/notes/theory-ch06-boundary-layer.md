---
title: "이론 ch06 — 경계층: Prandtl 이론 · law of the wall · 박리 · d'Alembert 해결"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch05-rans.md
  - textbook/notes/theory-ch03-euler.md
canonical_source: self
citation_status: verified
claims_total: 18
claims_attached: 13
claims_dropped: 0
claims_source_needed: 5
claims_basis: legacy-ledger
has_source_needed: true
provenance: "교재 프로젝트 textbook-ai-data-full ch06(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착 + 같은 날 Codex 게이트(T13) MODIFY 반영. 주 출처 = **stewart-physical-ocean §8(Prandtl 경계층·law of the wall) + marine-sands-manual(bottom BL 로그 profile) + water-wave-mechanics(파 저면 경계층·wake) + hudspeth(박리/wake/vortex shedding)**. ★Codex 게이트 정정(심각): marine-sands 페이지 = grep 행번호를 페이지로 착각한 오류(κ '297'→**p.12**·bottom 로그 '2343'→**p.62**)·stewart Az·Eq.8.20·Charnock p.135→**p.134**·Prandtl p.133-134. ★★박리 '코퍼스 미확인' 오판 철회 — **Hudspeth p.620 §7.9 에 박리점·wake·vortex shedding 정식 실존**(velocity defect→separation points→wake)·D&D p.231 wake→drag·파 저면 경계층 δ≈1mm p.279. MST p.653-654 는 밀도류 계면(벽면 평판 아님)으로 축소. Blasius ODE·δ99·Cf·Falkner-Skan·T-S·천이 Re·역압력구배 정식만 source-needed 유지. ★연안 핵심=law of the wall(bottom BL). depends_on ch04·ch05·ch03(d'Alembert 핵심결과라 근거 승격). T13([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "stewart-physical-ocean p.133-134(§8 Prandtl 1904 경계층·flat plate·Kármán Az=κzu*·log profile Eq.8.20·Charnock z0) + marine-sands-manual p.12·62(von Kármán 0.40·bottom 로그 velocity profile SC Eq.22) + water-wave-mechanics p.231·279(wake→drag·파 저면 경계층 δ) + hudspeth2005-wave-forces p.620(§7.9 박리·wake·vortex shedding) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14, Codex 게이트 재검증 포함)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch05-rans.md
  - textbook/notes/theory-ch13-sediment-transport.md
  - textbook/notes/theory-ch08-linear-waves.md
---

# 경계층 — Prandtl 이론 · law of the wall · 박리

> 4-레이어 **① 이론** 노트. 큰 Re 흐름에서 점성이 결정적인 **물체 표면 근처 얇은 층**의 이론 — [[theory-ch04-navier-stokes]] 의 N-S 를 경계층 안에서 단순화하고, [[theory-ch05-rans]] 난류 로그층으로 이어지며, [[theory-ch03-euler]] §5 d'Alembert 역설을 해결(근거 의존 ①→①, 3중).
> 탐색 링크(근거 의존 아님): 바닥 경계층·표사 [[theory-ch13-sediment-transport]].

## 1. Prandtl 경계층 개념과 d'Alembert 해결

- **경계층(boundary layer)은 Prandtl 이 1904 에 발명** — 점성이 작은(큰 Re) 유동에서 점성 효과가 **물체 표면 근처 얇은 층에 국한**된다는 통찰 (stewart-physical-ocean, p.133-134, Anderson 2005; 근거 [[theory-ch03-euler]] §5). 바닥에서 점성 때문에 흐름이 0 이라 벽 근처에 속도가 급변하는 얇은 영역이 생김 — 연직 척도가 다르므로 재축척 $z=\delta z'$ 하면 점성항이 $O(1)$ 로 살아남고, $\delta$ 가 **층류 경계층 두께**(예: 5초 파에서 $\delta\approx1$ mm) (water-wave-mechanics, p.279).
- 이것이 [[theory-ch03-euler]] §5 **d'Alembert 역설의 해결**: 무점성·wake 부재 시 물체 전후 압력이 대칭이라 알짜 항력 0 이지만, 실제는 점성이 wake 를 만들어 항력 발생 (water-wave-mechanics, p.231). ※원문 교재의 평판 차원해석 $\delta/L\sim1/\sqrt{\mathrm{Re}}$·특이섭동·정합점근전개는 코퍼스 미확인 — 미이식. <!-- citation_status: source-needed -->
- **평판 경계층 이론**은 Prandtl·**G.I. Taylor·von Kármán 이 1915-1935 에 독립 발전** — mixing-length 이론으로 벽 근처 평균 속도 profile 을 잘 예측(해면 위 바람 흐름 포함) (stewart-physical-ocean, p.134).

## 2. Law of the wall — 로그 속도 profile

- **eddy viscosity 의 벽 거리 의존**: Prandtl·Taylor 는 큰 와류가 혼합에 효과적이므로 $A_z$ 가 벽 거리에 따라 변한다고 봄 — Kármán 은 $A_z=\kappa z u_*$ 형태 가정($\kappa$=무차원 상수) (stewart-physical-ocean, p.134).
- **로그 속도 profile(law of the wall)**: 위 가정으로 평균 속도가 $U=\dfrac{u_*}{\kappa}\ln\dfrac{z}{z_0}$ 로 유도됨 — $u_*$=마찰속도, $z_0$=속도가 0 이 되는 거칠기 길이 (stewart-physical-ocean, p.134, Eq. 8.20; 해면 위는 Charnock 1955 $z_0=0.0156\,u_*^2/g$). von Kármán 상수 **$\kappa=0.40$** (marine-sands-manual, p.12).
- ★**연안 bottom boundary layer**: 바닥 위 수 m 에서 흐름 속도가 높이에 따라 **로그 속도 profile** $U(z)=\dfrac{u_*}{\kappa}\ln\dfrac{z}{z_0}$ 를 따름($z_0$=bed roughness length·$\kappa=0.40$) — 표사 이송·바닥 전단응력 산정의 기반 (marine-sands-manual, p.62, SC Eq. 22; [[theory-ch13-sediment-transport]] §2 Shields·마찰속도와 연결). 이 로그층이 연안공학에서 Blasius 층류 경계층보다 핵심.

## 3. 층류 경계층·박리

- **파 저면 경계층(wave boundary layer)**: 파랑 유동에서 바닥 no-slip 때문에 얇은 층에서 속도가 급변 — 층류 경계층 두께 $\delta$ 는 매우 얇음(5초 파에서 $\delta\approx1$ mm) (water-wave-mechanics, p.279; §9.4 저면 경계층 스케일링). ※원문 교재의 두 흐름 계면 층류 경계층(mechanics-of-sediment-transport, p.653-654 Fig. 14.6-14.7)은 벽면 평판이 아닌 밀도류 계면. ※**Blasius 자기상사 해**($\eta=y\sqrt{U_\infty/\nu x}$·**Blasius ODE $2f'''+ff''=0$**·$\delta_{99}\approx5\sqrt{\nu x/U_\infty}$·$C_f=1.328/\sqrt{\mathrm{Re}_L}$)는 코퍼스 미확인 — 미이식(MST 'Blasius formula'는 난류 저항공식으로 별개). <!-- citation_status: source-needed -->
- **박리(separation)와 wake**: 점성이 뭉툭한 물체(bluff body) 경계 근처에 속도 결손을 만들어 **경계층 흐름이 정지→박리점(separation points) 형성→wake(후류)** 생성, wake 안에서 **와류가 방출(vortex shedding)** — 이것이 항력·횡력의 원천 (hudspeth2005-wave-forces, p.620, §7.9; wake 부재 시 항력 0 은 water-wave-mechanics, p.231). ※역압력 구배($dp/dx>0$)·박리점 정식 조건·형상 항력 정량은 코퍼스 미확인 — 미이식. <!-- citation_status: source-needed -->

## 4. 천이·응용

- **천이(층류→난류 경계층)**: 원문 교재의 평판 천이 $\mathrm{Re}_x\approx5\times10^5$·Tollmien-Schlichting 파·Falkner-Skan(1931) 자기상사·Kármán 운동량 적분(1921)은 코퍼스 미확인 — 미이식(난류 경계층 일반론은 [[theory-ch05-rans]] mixing length 로 부분 커버). <!-- citation_status: source-needed -->
- **연안·해양 응용**: 대기 경계층·해양 표층/바닥 경계층·바람 응력→표층 혼합층이 로그층 이론의 응용 (stewart-physical-ocean, p.133-134, 해면 위·아래 로그 profile). EFDC 등 환경 모델의 bottom boundary layer 마찰 처리는 `models/` 축. ※골프공 딤플·항공기 실속 등 일상예는 미이식.

## 5. 연결

- [[theory-ch04-navier-stokes]] — N-S(경계층 안 단순화)·Reynolds 수 (근거 의존)
- [[theory-ch05-rans]] — 난류·mixing length(로그층 기반) (근거 의존)
- [[theory-ch03-euler]] — d'Alembert 역설(경계층이 해결) (근거 의존)
- [[theory-ch13-sediment-transport]] — 바닥 경계층·마찰속도·Shields (탐색)
- 다음: ch07 와도방정식(N-S 회전 형태).
