---
title: "이론 ch13 — 퇴적물 이송: 침강 · Shields 임계 · bedload/suspended · Rouse · Exner · CERC"
topic: sediment
layer: 1
depends_on: []
canonical_source: self
citation_status: verified
provenance: "교재 프로젝트 textbook-ai-data-full ch13(AI 합성 MDX, 무인용) 이식분 — 2026-07-13 원자 단언 분해·(source_id, page) 부착. ★원문 연도 미지지 2건 미이식(Krone '1962'·Partheniades '1965' — 코퍼스 실측은 Ariathurai & Krone 1976·Partheniades 무연도 서술), 미매칭 삭제 5건(Rouse 매개변수 모드 구분표 2.5/0.8·기준 높이 a=2d·Van Rijn 1984 bedload 0.053 T^2.1/D*^0.3 명시 계수·boulder/cobble/pebble 상세 경계·fluid mud). 워크 예제·한국 연안 수치(동해안 0.3mm·수만 m³/년)·계절 profile(ch14 주제)·EFDC 모듈 상세는 미이식 — concepts/models 탐색 위임. ※van-rijn-1993 미러 = OCR 실패 껍데기(690p 전부 빈 텍스트) 판정 — 주 출처에서 제외. T5([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "marine-sands-manual(Soulsby) p.8·11-12·24·33·48·51·62·74·109-110·114·120·138-141·145-147·162·164-165·168·198-199 + mechanics-of-sediment-transport p.216·229-230·367-368·370·376(서지 p.423)·TOC p.15 + efdc-sed-trans-2003 p.38-42·66 — textbook/md 미러 페이지 직접 대조 (2026-07-13)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-13
related:
  - concepts/sediment-transport/01-concept.md
  - concepts/littoral-drift/01-concept.md
  - textbook/notes/theory-ch10-coastal-transformation.md
---

# 퇴적물 이송 — 침강·임계·운반 양식·Rouse·Exner·연안 이송

> 4-레이어 **① 이론** 노트. 흐름이 바닥 입자에 가하는 응력이 임계를 넘으면 이동 시작 → bedload/suspended 운반 → 이송률 수렴·발산이 바닥 변화를 만든다.
> 탐색 링크(근거 의존 아님): 도메인 요약 `concepts/sediment-transport/` · 연안 표사 `concepts/littoral-drift/` · 점착 이송 모델 구현 `models/EFDC/`(source-analysis sediment 계열) · 연안류 배경 [[theory-ch10-coastal-transformation]].

## 1. 퇴적물 분류와 침강속도

- **모래(sand) = 입경 0.062–2 mm** 가 관행 정의 — 더 가는 퇴적물은 clay·silt(mud)로 분류되며 성질이 **전기화학적 상호작용**에 강하게 지배됨 (marine-sands-manual, p.24). ※원문 교재의 boulder/cobble/pebble 상세 경계값 표는 코퍼스 미확인 — 미이식.
- **밀도**: 석영 모래 $\rho_s \approx 2650\ \mathrm{kg\,m^{-3}}$ (marine-sands-manual, p.48; 측정 절차 문맥 p.33), 물 $\rho \approx 1000$(담수)·$1027$(해수) $\mathrm{kg\,m^{-3}}$ (p.51). 밀도비 $s=\rho_s/\rho$ 가 무차원화의 기본 (p.140 기호 정의).
- **무차원 입경** $D_* = d\,[(s-1)g/\nu^2]^{1/3}$ — 다수 침강·임계 공식의 입력 (marine-sands-manual, p.8 표기·p.140).
- **침강속도 $w_s$ 의 두 극한**: 모래 최세립단($d \approx 62\ \mu\mathrm{m}$)은 **Stokes 점성 항력 법칙**, 최조립단($d \approx 2$ mm)은 **quadratic bluff-body 항력**, 중간은 혼합 — 자연 모래는 각진 표면 때문에 구(sphere) 취급이 부적절 (marine-sands-manual, p.139-140).
- 실용 공식: **Hallermeier(1981)** 는 $D_*^3<39$ 구간에서 Stokes 형 $w_s = \Delta g d^2/(18\nu)$ 꼴, **Van Rijn(1984)** 도 자연 모래용 구간별 식 제공 (marine-sands-manual, p.141, SC Eq. 100-101).

## 2. 이동의 시작 — Shields 임계

- 흐름을 천천히 올리면 어느 속도에서 입자가 움직이기 시작 — **threshold(incipient) of motion**; 흐름·파·복합 조건 모두에서 동일 개념 (marine-sands-manual, p.109, §6.2).
- 정밀한 기준은 바닥 전단응력으로: **Shields(1936)** 가 바닥 전단력 대 입자 수중 무게의 비로 정식화 (marine-sands-manual, p.114) — **Shields 매개변수** $\theta = \tau/[(\rho_s-\rho)gd]$ (기호 정의 p.11).
- **Shields 곡선**: 임계값을 입자 Reynolds 수 $u_*d/\nu$ 의 함수로 실험 정리 — 입경 대 점성저층 두께의 비를 뜻함 (mechanics-of-sediment-transport, p.216, Fig. 6.4 문맥). 예시 계산에서 Shields 곡선은 $\theta_{cr}=0.0633$ 수준 (marine-sands-manual, p.120).
- **Soulsby 대수 공식**: $\theta_{cr} = \dfrac{0.30}{1+1.2D_*} + 0.055\,[1-\exp(-0.020D_*)]$ — 비점착 퇴적물 전 구간 유효 (marine-sands-manual, p.110, SC Eq. 72b/77 결합형).
- 임계 유속 형태로는 **Van Rijn(1984)** 공식(담수 15 °C·$\rho_s$=2650 전제 명시, 입경 구간별)이 병용 (marine-sands-manual, p.109-110, SC Eq. 71).
- 세립(점착) 쪽에서 임계가 커지는 이유는 §7 (전기화학 결합).

## 3. 운반 양식 — bedload vs suspended

- **Bedload**: 임계 초과 흐름에서 입자가 바닥을 따라 **구르기·미끄러짐·도약(saltation)** 으로 이동, 무게를 바닥이 간헐 지지 (marine-sands-manual, p.162; 개관 p.24).
- **Suspended**: 침강속도가 $u_*$ 에 비례하는 상향 난류 성분보다 작으면 부유 지속 — **부유 임계 $u_{*s} = w_s$** (skin-friction 마찰속도 기준) (marine-sands-manual, p.138, SC Eq. 96). 혼합 입도에서는 분급별 적용 — 가는 분급만 부유하고 굵은 분급은 bedload 로 남음 (p.138-139).
- **Rouse 수(suspension parameter)** $b = w_s/(\kappa u_*)$ 가 부유 분포의 지배 무차원수 (marine-sands-manual, p.8·p.145, SC Eq. 105) — $\kappa$ = von Kármán 상수 **0.40**(해수·부유 시에도 보편값 사용이 현재 관행) (p.12·62).
- 임계 초과가 충분히 크면 **부유 이송이 총 이송의 대부분** (marine-sands-manual, p.138, §8.1). ※원문 교재의 모드 구분표($P>2.5$ bedload only / $0.8{-}2.5$ 혼합 / $<0.8$ suspended)는 코퍼스 미확인 — 미이식(Eq. 96 기준만 이식).

## 4. Bedload 공식 계보

- **Meyer-Peter & Müller(1948)**: $\phi = 8\,(\theta-\theta_{cr})^{3/2}$, $\theta_{cr}=0.047$ — 하천용으로 개발된 고전 (marine-sands-manual, p.164, SC Eq. 117).
- 동급 계보로 **Bagnold(1963)**·**Yalin(1963)**·**Van Rijn(1984)** 공식이 병렬 정리됨 (marine-sands-manual, p.164-165, SC Eq. 118-120; saltation 모래는 계수 $F_M=9.5$, p.165). ※원문 교재의 Van Rijn(1984) bedload 명시형 "$0.053\sqrt{(s-1)gd^3}\,T^{2.1}/D_*^{0.3}$" 은 미러 OCR 로 계수 문자 검증 불가 — 계보만 이식, 계수 미전사.
- 동일 조건 예제에서 4공식 비교: $q_b$ 가 $10.9{-}23.9\times10^{-6}\ \mathrm{m^2\,s^{-1}}$ 대역으로 산포 — 반경험식 간 격차의 실감 (marine-sands-manual, p.168).

## 5. Suspended load — Rouse 분포

- 정상 상태에서 상향 난류 확산과 하향 침강의 평형이 농도 연직 분포를 결정. 와확산계수를 포물형 $K_s=\kappa u_* z(1-z/h)$ 로 두면 **Rouse profile** $\dfrac{c(z)}{c_a}=\left[\dfrac{z_a(h-z)}{z(h-z_a)}\right]^{b}$ 을 얻음 — $c_a$ = 기준 높이 $z_a$ 의 기준 농도, $b$ = Rouse 수 (marine-sands-manual, p.145-146, SC Eq. 105-106).
- $b$ 작음(세립·강한 흐름) → 전 수심 잘 혼합, $b$ 큼 → 바닥 집중; **Rouse profile 이 가장 널리 쓰임**(특히 하천) — $b=1$ 사례로 지수·멱형 분포와 형상 비교 (marine-sands-manual, p.147, Fig. 28). ※기준 높이 "$a=2d$" 관행 수치는 코퍼스 미확인 — 미이식.

## 6. 바닥 변화 — 퇴적물 연속(Exner)

- **Exner** 가 물·퇴적물 연속방정식 쌍으로 바닥 파형 발달을 해석 — 이송률을 유속에 비례로 두면 초기 요철(hump)이 **비대칭 ripple 로 성장·하류 이동**함을 보임 (mechanics-of-sediment-transport, p.229-230, Eq. 6.1-6.2 문맥; 퇴적물 연속식의 계수 전사는 OCR 판독 한계로 생략).
- 물리 해석: 이송률이 흐름 방향으로 **증가**하는 구간은 침식, **감소**하는 구간은 퇴적 — 해안 단면 변화·사주 발달·항내 매몰의 공통 골격. ※원문 교재의 $(1-n)\partial z_b/\partial t + \nabla\cdot\mathbf{q}_T = E-D$ 표기(공극률 $n$·침식/퇴적 항 분리)는 코퍼스 문자 미확인 — 형태 미전사.

## 7. 점착성 퇴적물(mud) 기초

- 모래(비점착)는 개별 입자가 흐름에 직접 응답하지만, clay·silt 는 **전기화학적 상호작용**이 지배 (marine-sands-manual, p.24).
- **점착 진흙 = Bingham 유체 거동**: 임계 마찰속도가 Bingham 항복응력과 결부되며, **소성 상태와 압밀 상태의 임계식이 다름** — 압밀이 임계를 키움 (mechanics-of-sediment-transport, p.367-368, Eq. 8.52-8.53 문맥). 갓 퇴적된 층과 압밀층의 이동 시작 조건 비교는 **Partheniades** 연구로 정리 (p.370).
- **응집(flocculation)과 침강**: floc 침강속도를 농도 등으로 파라미터화 — 농도 의존 침강식의 고전은 **Ariathurai & Krone(1976)** (efdc-sed-trans-2003, p.66). ※원문 교재의 "Krone 1962·Partheniades 1965" 연도는 코퍼스 미지지 — 미이식.
- **다층 bed·압밀 추적** 정식화는 모델 구현 축 (efdc-sed-trans-2003, p.38-42, §5 Sediment Bed Mass Conservation, Armoring and Consolidation) — 상세는 `models/EFDC/`(탐색). ※fluid mud 는 코퍼스 미확인 — 미이식.

## 8. 연안 표사 — CERC 공식

- 연안 방향 이송이 구조물(groyne·항 입구·도류제)에 막히면 **updrift 퇴적·downdrift 침식** (marine-sands-manual, p.198).
- **CERC 공식** = surf zone 폭 적분 총 연안이송률의 최광용 공식 — 원형은 **Shore Protection Manual(CERC, 1984)**. $c_g=(gh)^{1/2}$·쇄파 기준 $H_b=0.8h$·$H_s=\sqrt2 H_{rms}$ 를 대입한 최단순형(SC Eq. 138)은 쇄파선 유의파고 $H_{sb}$ 와 쇄파선 입사각 $\alpha_b$ 만의 함수($\sin 2\alpha_b$ 꼴) — 겉보기에 입경·해빈 경사 무관 (marine-sands-manual, p.198-199).
- **적용 한계**: 선도 계수는 $d<0.6$ mm(부유 지배) 모래 해빈 자료로 보정 — 자갈(shingle) 해빈에 그대로 쓰면 **약 20배 과대예측**(Brampton & Motyka 1984), 입경·경사 보정판(Kamphuis 1991 등) 또는 전용 공식(Damgaard & Soulsby 1997 bedload 형) 필요 (marine-sands-manual, p.199).
- 계절 단면 변화(summer/winter profile)·평형 단면은 ch14 형태동역학 주제 — [[theory-ch10-coastal-transformation]](연안류 발생)과 T6 노트로 위임. ※원문 교재의 한국 연안 수치(동해안 연간 수만 m³ 등)는 지역 의존 값 — 미이식.

## 9. 역사 연표 (코퍼스 실측분)

**du Boys**(19세기 말, 전단응력 기반 첫 bedload 이론; 1879 서지) (mechanics-of-sediment-transport, p.376·서지 p.423) → **Shields 1936** 임계 무차원화 (marine-sands-manual, p.114) → **Meyer-Peter & Müller 1948** (p.164) → **Einstein 1950** bed-load function 계보 (p.74 언급; 전용 절 §9.1.3 은 mechanics-of-sediment-transport TOC p.15) → **Bagnold·Yalin 1963** (p.164-165) → **Van Rijn 1984** 침강·임계·이송 일괄 체계 (p.109·141·164). ※원문 교재의 "Partheniades 1965" 연도·"ASCE 표준 교과" 단언은 코퍼스 미확인 — 미이식.

## 10. 연결

- [[theory-ch10-coastal-transformation]] — 쇄파대 연안류(이송의 구동력, 탐색)
- `concepts/sediment-transport/`·`concepts/littoral-drift/` — 도메인 요약·한국 연안 (탐색)
- `models/EFDC/` source-analysis sediment 계열 — 점착·다층 bed 구현 (탐색)
- 다음: ch14 해안 형태동역학 (T6) — Dean profile·Bruun rule·CERC 응용.
