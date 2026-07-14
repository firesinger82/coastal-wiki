---
title: "이론 ch06 — 경계층: Prandtl 이론 · law of the wall · 박리 · d'Alembert 해결"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch05-rans.md
canonical_source: self
citation_status: verified
has_source_needed: true
provenance: "교재 프로젝트 textbook-ai-data-full ch06(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착. 주 출처 = **stewart-physical-ocean §8(Prandtl 경계층·law of the wall) + marine-sands-manual(bottom boundary layer 로그 profile)**. ★삭제 전 전체 코퍼스 grep(정확 용어+개념 동의어+주 출처 절 통독): Blasius 자기상사 ODE(2f'''+ff''=0)·δ99=5√(νx/U) 계수·Falkner-Skan·Tollmien-Schlichting·displacement/momentum thickness = 코퍼스 **미확인**(MST 'Blasius'=난류 저항공식 별개·Hudspeth 'separation'=변수분리법 오탐, 박리 flow separation 정확개념도 미확인) → source-needed. δ∝1/√Re 차원해석도 코퍼스 미확인. 미이식: 골프공 딤플·워크예제·항공기 실속. ★연안 관련성 핵심은 Blasius 층류가 아닌 **law of the wall(bottom boundary layer 로그 profile)** — stewart+marine-sands 확실 부착. depends_on ch04(N-S 단순화)·ch05(난류 mixing length→log law)·ch03(d'Alembert, 탐색). T13([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "stewart-physical-ocean p.133-135(§8 Prandtl 1904 경계층·flat plate·Kármán Az=κzu*·log profile Eq.8.20·Charnock z0) + marine-sands-manual p.297·2343(von Kármán 0.40·bottom 로그 velocity profile) + mechanics-of-sediment-transport p.653-654(laminar boundary layer velocity distribution) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch05-rans.md
  - textbook/notes/theory-ch03-euler.md
  - textbook/notes/theory-ch13-sediment-transport.md
---

# 경계층 — Prandtl 이론 · law of the wall · 박리

> 4-레이어 **① 이론** 노트. 큰 Re 흐름에서 점성이 결정적인 **물체 표면 근처 얇은 층**의 이론 — [[theory-ch03-euler]] §5 d'Alembert 역설을 해결하고, [[theory-ch04-navier-stokes]] 의 N-S 를 경계층 안에서 단순화(근거 의존 ①→①).
> 탐색 링크(근거 의존 아님): 바닥 경계층·표사 [[theory-ch13-sediment-transport]] · 난류 [[theory-ch05-rans]].

## 1. Prandtl 경계층 개념과 d'Alembert 해결

- **경계층(boundary layer)은 Prandtl 이 1904 에 발명** — 점성이 작은(큰 Re) 유동에서 점성 효과가 **물체 표면 근처 얇은 층에 국한**된다는 통찰 (stewart-physical-ocean, p.134, Anderson 2005; 근거 [[theory-ch03-euler]] §5). 층 안은 벽 no-slip($u=0$)과 자유흐름의 큰 속도차가 얇은 거리에서 일어나 점성항이 관성항과 같은 크기.
- 이것이 [[theory-ch03-euler]] §5 **d'Alembert 역설의 해결**: 무점성 극한에서도 경계층 안 점성 응력이 항력을 만듦. ※원문 교재의 차원해석 $\delta/L\sim1/\sqrt{\mathrm{Re}}$·특이섭동·정합점근전개는 코퍼스 미확인 — 미이식. <!-- citation_status: source-needed -->
- **평판 경계층 이론**은 Prandtl·**G.I. Taylor·von Kármán 이 1915-1935 에 독립 발전** — mixing-length 이론으로 벽 근처 평균 속도 profile 을 잘 예측(해면 위 바람 흐름 포함) (stewart-physical-ocean, p.134).

## 2. Law of the wall — 로그 속도 profile

- **eddy viscosity 의 벽 거리 의존**: Prandtl·Taylor 는 큰 와류가 혼합에 효과적이므로 $A_z$ 가 벽 거리에 따라 변한다고 봄 — Kármán 은 $A_z=\kappa z u_*$ 형태 가정($\kappa$=무차원 상수) (stewart-physical-ocean, p.135).
- **로그 속도 profile(law of the wall)**: 위 가정으로 평균 속도가 $U=\dfrac{u_*}{\kappa}\ln\dfrac{z}{z_0}$ 로 유도됨 — **$\kappa=0.4$**(von Kármán 상수), $u_*$=마찰속도, $z_0$=거칠기 길이 (stewart-physical-ocean, p.135, Eq. 8.20; 해면 위는 Charnock 1955 $z_0=0.0156\,u_*^2/g$). von Kármán 상수 0.40 은 marine-sands-manual, p.297 도 명시.
- ★**연안 bottom boundary layer**: 바닥 위 수 m 에서 흐름 속도가 높이에 따라 **로그 속도 profile** 를 따름 — 표사 이송·바닥 전단응력 산정의 기반 (marine-sands-manual, p.2343; [[theory-ch13-sediment-transport]] §2 Shields·마찰속도와 연결). 이 로그층이 연안공학에서 Blasius 층류 경계층보다 핵심.

## 3. 층류 경계층·박리

- **층류 경계층 속도 분포**: 두 흐름 계면·평판 위 층류 경계층에서 속도가 벽에서 자유흐름으로 발달 (mechanics-of-sediment-transport, p.653-654, Fig. 14.6-14.7). ※**Blasius 자기상사 해**(자기상사 변수 $\eta=y\sqrt{U_\infty/\nu x}$·**Blasius ODE $2f'''+ff''=0$**·$\delta_{99}\approx5\sqrt{\nu x/U_\infty}$·$C_f=1.328/\sqrt{\mathrm{Re}_L}$)는 코퍼스 미확인 — 미이식(MST 'Blasius formula'는 난류 저항공식으로 별개). <!-- citation_status: source-needed -->
- **박리(separation)**: 역압력 구배($dp/dx>0$)에서 경계층이 벽에서 분리되어 큰 와류·형상 항력을 만드는 현상 — 원문 교재의 핵심 주제이나 **flow separation 의 정식 정의·박리점 조건은 코퍼스 직접 미확인**(Hudspeth 'separation'은 변수분리법). 형상 항력·박리 상세는 별도 출처 확보 후 이연. <!-- citation_status: source-needed -->

## 4. 천이·응용

- **천이(층류→난류 경계층)**: 원문 교재의 평판 천이 $\mathrm{Re}_x\approx5\times10^5$·Tollmien-Schlichting 파·Falkner-Skan(1931) 자기상사·Kármán 운동량 적분(1921)은 코퍼스 미확인 — 미이식(난류 경계층 일반론은 [[theory-ch05-rans]] mixing length 로 부분 커버).
- **연안·해양 응용**: 대기 경계층·해양 표층/바닥 경계층·바람 응력→표층 혼합층이 로그층 이론의 응용 (stewart-physical-ocean, p.135, 해면 위 바람 profile). EFDC 등 환경 모델의 bottom boundary layer 마찰 처리는 `models/` 축. ※골프공 딤플·항공기 실속 등 일상예는 미이식.

## 5. 연결

- [[theory-ch04-navier-stokes]] — N-S(경계층 안 단순화)·Reynolds 수 (근거 의존)
- [[theory-ch05-rans]] — 난류·mixing length(로그층 기반) (근거 의존)
- [[theory-ch03-euler]] — d'Alembert 역설(경계층이 해결) (탐색)
- [[theory-ch13-sediment-transport]] — 바닥 경계층·마찰속도·Shields (탐색)
- 다음: ch07 와도방정식(N-S 회전 형태).
