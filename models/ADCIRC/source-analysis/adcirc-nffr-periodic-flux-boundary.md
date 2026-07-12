---
title: "ADCIRC fort.15 NFFR 주기 flux 경계 — 레코드 구조·QN 합성·IBTYPE=32 radiation 이산식·부호 규약"
topic: general
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "read_input.F NFFR 블록(:3504-3589)·timestep.F QN/EN 합성(:860-880)·gwce.F flux BC 블록(:1725-1810, Note 2 주석 :1727-1733, JCG :2003)·normal_flow_boundary.F90 rotate_normal_flux(:59-104) + 공식 docs fort15.rst:79-90·parameter_definitions/index.rst:806-840 직접 read (2026-07-12). 모든 식·주석 verbatim 인용."
note_author: "Claude Fable 5 (source-code direct read)"
note_date: 2026-07-12
related:
  - models/ADCIRC/source-analysis/adcirc-boundary-conditions.md
  - models/ADCIRC/source-analysis/adcirc-gwce-implementation.md
  - models/ADCIRC/source-analysis/adcirc-tidal-forcing.md
---

# ADCIRC fort.15 NFFR 주기 normal-flux 경계 강제

> [[adcirc-boundary-conditions]] 가 IBTYPE 분류·mesh 측을 커버하나 fort.15 쪽 NFFR 레코드 구조와 gwce.F 의 flux 경계 이산식은 미커버였던 갭의 해소 노트 (2026-07-12, 사용자 지목 3건).

## 1. fort.15 NFFR 레코드 구조 (read_input.F:3504-3589 + docs fort15.rst:79-90)

NFFR 라인은 mesh(fort.14)에 flux 경계(IBTYPE 2/12/22/32/52)가 있어 `NFLUXF=1`일 때만 포함 (read_input.F:3505, docs fort15.rst:79 "include this line only if IBTYPE = 2, 12, 22, 32 or 52").

```
NFFR                              ← 정수. 0/-1 = 비주기(fort.20에서 읽음; 0=coldstart 기점, -1=hotstart 기점, :3509-3516·paramdef:811)
k = 1..NFFR:                      ← 분조 정의 블록
  FBOUNTAG(k)                     ← 분조명 한 줄 (READ '(A5)', :3549)
  FAMIGT(k)  FFF(k)  FFACE(k)     ← 주파수(rad/s)·nodal factor·평형인수(★도 단위, :3550; 코드가 DEG2RAD 변환 :3553)
k = 1..NFFR:                      ← 분조별 노드값 블록
  ALPHAQ(k)                       ← 검증용 태그 한 줄 (READ '(A10)', :3568; paramdef "verifying that the correct data matches a given frequency")
  j = 1..NVEL 순서로, flux 경계 노드만:
    QNAM(k,j)  QNPH(k,j)                          ← IBTYPE 2/12/22/52 노드 (:3570-3576)
    QNAM(k,j)  QNPH(k,j)  ENAM(k,j)  ENPH(k,j)    ← IBTYPE=32 노드 (:3578-3584)
```

- **단위**: QNAM = 단위폭당 유량 진폭 "normal flow/unit width (e.g. m2/s)" (paramdef:834). QNPH·ENPH = 위상(도) — 코드가 라디안 변환(:3576, :3583-3584). ENAM = IBTYPE=32 "outgoing wave" 진폭(수위, m)(paramdef:839-840).
- **줄 존재 규칙**: `DO J=1,NVEL` 루프 내 `LBCODEI(J)` 조건 READ(:3571-3584) — **flux 경계 노드만 줄이 있고**, land 등 비대상 노드는 줄 자체가 없음. 노드 순서 = fort.14 velocity 경계 나열 순서(NBV).
- ★**code≠docs 1건**: fort15.rst:87 은 2-필드 줄을 "IBTYPE = 2, 12, 22"로만 표기하나 코드는 **52 도 같은 분기**(:3570 `.OR.(LBCODEI(J).EQ.52)`) — NFFR 포함조건 줄(:79)에는 52 명시, 필드 줄에서만 누락. (※초판의 "QNAM 앵커 `ln` 오염" 지적은 **철회** — 2026-07-12 Codex 표본 재검증에서 검증 도구 오류(`rg -r` 치환 플래그 오용)로 판명, 실제 docs 는 `.. _QNAM:` 정상(:830-834).)

## 2. 런타임 QN·EN 합성 (timestep.F:860-880)

매 스텝, `NFLUXF=1 & NFFR>0`일 때:

```fortran
ARGJ = FAMIG(J)*(timeh - NCYC*FPER(J)) + FFACE(J)     ! :869 (NCYC = 위상 wrap)
RFF  = FFF(J)*RampExtFlux                             ! :870 (nodal factor × 외부flux 램프)
CASE(2,12,22,52): QN2(I) += rotate_normal_flux(ICS, I, QNAM(J,I)*RFF*COS(ARGJ-QNPH(J,I)))   ! :874
CASE(32):         QN2(I) += rotate_normal_flux(...)  ;  EN2(I) += ENAM(J,I)*RFF*COS(ARGJ-ENPH(J,I))  ! :876-877
```

- `rotate_normal_flux`(normal_flow_boundary.F90:59-104): 회전 구면좌표계(ICS 20-24)에서만 경계 법선(CSII/SIII)·구면 스케일팩터(SFCX/SFCY·YCSFAC)로 flux 를 회전 변환, 그 외 `QROT=Q` 그대로(:100-101). ★**EN2(수위)는 회전 없음** — 스칼라라 당연하나, QN 만 통과시키는 비대칭을 코드에서 확인.
- EN 도 QN 과 동일한 `RFF`(nodal factor·램프) 를 곱음(:877) — 램프 중 radiation 기준수위도 함께 램프됨.

## 3. gwce.F flux 경계 이산식 — IBTYPE=32 (gwce.F:1725-1810)

GWCE 로드벡터 조립 직전, 노드별 `QFORCEJ` (= GWCE 가 요구하는 `∂q/∂t + τ₀·q` 조합):

| LBCODEI | QFORCEJ | 의미 |
|---|---|---|
| ≤29, 64 | `(QN2-QN0)/DT2 + τ₀·QN1` | 지정 flux (하천 22 등) (:1741) |
| 30 | `-c·ETAS/DT - τ₀·QN1` | radiation(Sommerfeld) — **명시적 −1** (:1745-1746) |
| **32** | `(QN2-QN0)/DT2 - c·(2·ETAS-(EN2-EN0))/DT2 + τ₀·(QN1 - c·(ETA1-EN1))` | **지정 flux + radiation 결합** (:1758-1760) |
| 40/41 | `-(QN1-QN0)/DT - τ₀·(QN1+QN0)/2` | zero-normal-gradient 계열 (:1763-1764) |
| 52 | ≤29 식 + settling 후 `-c·(ETAS/DT + τ₀·(ETA1-ElevDisc))` 감쇠항 (:1768-1775) | steady flux + 수위 이산 |

IBTYPE=32 의 구조 = 유효 flux **q_eff = QN − c·(η − EN)**, `c = √(g·H1(node))`(:1751) 에 GWCE 연산자(∂/∂t + τ₀)를 적용한 것:

- τ₀ 항이 그대로 `τ₀·(QN1 − c·(ETA1−EN1))` — q_eff 의 정의를 노출.
- 시간미분 항: 주석처리된 **원식(1차)** `(QN1-QN0)/DT − c·(ETAS−(EN1-EN0))/DT` (in-code 주석 "This is an original formula and is definitely correct (1st order in time)", :1792-1795) 을 **2차 버전**으로 교체 — DW 주석(:1797-1798) "a 2nd-order extrapolation formula: η^{n+1} = 2·ηⁿ − η^{n−1} is used and second order in time derivative is used". `ETAS` = 직전 GWCE solve 의 미지수(수위 증분; JCG 가 ETAS 를 풀고 η 갱신, :2003) 이므로 `2·ETAS ≈ η^{n+1}−η^{n−1}`(외삽) — `(…)/DT2` 가 2Δt 중심차분.

**물리 해석**: 경계 밖으로 나가는 교란은 radiation flux `c·(η−EN)` 로 방출시키면서, 순 유입 flux 를 지정값 QN 으로 강제 — EN 은 "지정 수위"가 아니라 **outgoing wave 를 판정할 기준 수위**(paramdef:839 "Amplitude and phase of outgoing wave").

## 4. QNAM 부호 규약 — 최종 확정

**양(+) = 도메인 안쪽(내향)**. 이중 확정:

1. **공식 docs** (paramdef:834 verbatim): *"A positive flow/unit width is into the domain and a negative flow/unit width is out of the domain."*
2. **코드 주석** (gwce.F:1727-1733 Note 2 verbatim): *"Boundary conditions using specified fluxes (LBCODEI < 29) assume that QN is positive into the domain. QFORCEJ has a -1 built in and the terms are not explicitly negated. Boundary conditions using computed fluxes (LBCODEI 30, 40) compute a normal flux that is positive out of the domain. Therefore, to match the formulation these terms must be explicitly multiplied by -1."* — IBTYPE=30 식의 선두 `-c·ETAS` 가 그 명시적 −1(:1746).

따라서 **IBTYPE=32 의 유효 flux 는 `q = QN − c(η − EN)`** (QN 내향 양 규약에서). "q = QN **+** c(η−EN)" 독해는 소스와 부호가 반대 — τ₀ 항 `QN1 - CELERITY*(ETA1-EN1)`(:1760, :1802)에서 마이너스가 명시적. 물리로도 정합: η > EN(내부 수위가 기준 초과)이면 radiation 이 **유출**(내향 flux 감소) 방향이어야 함.

## 5. 연결

- [[adcirc-boundary-conditions]] — IBTYPE 분류·mesh 측 (본 노트가 fort.15·gwce 측 보완)
- [[adcirc-gwce-implementation]] — GWCE 로드벡터·JCG solve
- [[adcirc-tidal-forcing]] — 수위 경계(NBFR·EMO/EFA) 대응 구조 (NFFR 은 그 flux 판)
- docs: `docs/technical_reference/input_files/fort15.rst` · `docs/technical_reference/parameter_definitions/index.rst:806-840`
