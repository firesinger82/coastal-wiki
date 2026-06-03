---
title: "ADCIRC 조석 forcing & 분석 — tidal potential(TPK/ETRF Love/nodal FFT) + SAL self-attraction·loading + 직접 luni-solar ephemeris + internal tide wave drag + harmonic analysis(harm.F)"
topic: adcirc
canonical_source: self
citation_status: verified
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/timestep.F (조석 potential 1509-1556) + internaltide.F90(249) + harm.F(2071) + astronomic.F90/ephemerides.F90/moon.F90 헤더 + 적용부(momentum.F:441 barotropic, gwce.F:1181/2592, CTIP) 직접 read. TIP2 식·ETRF·species L_N·SAL·NTIP=2 path file:line 인용. Luettich-Westerink ADCIRC."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 조석 potential·SAL·internal tide·harmonic 식 verbatim"
verification_date: 2026-06-03
related:
  - models/ADCIRC/source-analysis/adcirc-momentum-implementation.md
  - models/ADCIRC/source-analysis/adcirc-gwce-implementation.md
  - models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md
---

# ADCIRC 조석 forcing & 분석

> `timestep.F`(tidal potential) + `internaltide.F90`(249) + `harm.F`(2071) + `astronomic/ephemerides/moon.F90` 직접 read. ADCIRC 조석 구동의 **body-force**(open-BC tidal elevation 과 별개): ① constituent tidal potential ② SAL(self-attraction & loading) ③ 직접 luni-solar ephemeris ④ internal tide wave drag ⑤ harmonic analysis(결과 분석). [[adcirc-momentum-implementation]] §1 의 barotropic pressure 에 합산되는 조석 항의 mechanism.

## 1. Tidal potential — constituent 방식 (timestep.F:1527-1556) ★

조석 천체 인력의 평형조위 forcing `TIP2(I)` (node별):
```fortran
ARGT  = AMIGT(J)*(timeh - NCYC*PERT(J)) + FACET(J)        ! 조석 argument
TPMUL = RampTip*ETRF(J)*TPK(J)*FFT(J)                      ! 진폭 multiplier
NA    = MIN(NINT(AMIGT(J)/7d-5),2)                         ! species (0/1/2)
TIP2(I) += TPMUL*L_N(NA,I)*COS(ARGT + NA*SLAM(I))          ! tidal potential
         + SALTMUL*SALTAMP(J,I)*COS(ARGT - SALTPHA(J,I))   ! SAL (§2)
```
- `NTIF` = tidal potential 상수 개수, `AMIGT`=각진동수, `PERT`=nodal 주기, `FACET`=평형 phase, `NCYC`=주기 cycle 정수(위상 reset).
- **ETRF** = earth-tide reduction factor = Love number 조합 `(1 + k − h) ≈ 0.69` (지구 탄성 변형 보정).
- **TPK** = tidal potential 진폭 × species 계수, **FFT** = nodal factor(18.6년 교점 보정 진폭), `RampTip`=ramp.
- **species `NA`** (주파수로 분류): 0 long-period/declinational, 1 diurnal, 2 semidiurnal. `L_N(NA,I)` = 위도 의존 geometric 함수(NA=2 → cos²φ 등), `SLAM`=경도(diurnal/semidiurnal 의 경도 의존 NA·λ).
- 적용(`CTIP`): [[adcirc-momentum-implementation]] momentum.F:441 (barotropic pressure 에 합산) + [[adcirc-gwce-implementation]] gwce.F:1181/2592. timestep.F:1133 `MOM_LV_X −= TIP1+TIP2`.

## 2. SAL — Self-Attraction & Loading (NTIP=2)

조석에 의한 해수 질량 재분포가 지구 중력장·해저 변형을 일으키는 2차 효과:
```fortran
TIP2(I) += SALTMUL * SALTAMP(J,I) * COS(ARGT - SALTPHA(J,I))    ! SALTMUL=RampTip*FFT
```
- `SALTAMP(J,I)`/`SALTPHA(J,I)` = **공간변화 SAL 진폭/위상**(constituent J × node I) — 외부 SAL DB(예: FES, GOT) 에서 fort.13/24 로 입력.
- `NTIP==2` 또는 `tidePotential` 비활성 시 적용(timestep.F:1527). 대양 규모 조석 정확도(~5-10%)에 중요.

## 3. 직접 luni-solar ephemeris (astronomic/ephemerides/moon.F90)

`tidePotential%active()` 시 constituent 합 대신 **천체력 직접 계산**(timestep.F:162 "full luni-solar tidal potential"):
- `moon.F90`(602)/`ephemerides.F90`(438)/`astronomic.F90`(460) = 달·태양 위치(적위·거리) 시계열 → 시변 tidal potential 직접. constituent truncation 없이 모든 조석 성분 포함(장기·비선형 조석 모사).
- 이 경우 SAL 만 constituent 방식(`SALTAMP`)으로 더해짐(timestep.F:1543-1547).

## 4. Internal tide wave drag (internaltide.F90, 249)

성층 대양에서 조류가 거친 해저지형 위로 흐르며 **내부조석(internal tide)으로 에너지 변환** → 순압류에 작용하는 drag:
- `apply2dinternalwavedrag`(nodalattr.F) 가 실제 적용; internaltide.F90 은 보조(가독성 분리, line 27/58).
- **시간평균 유속** `UBar = Σ wts·UAV` (~25시간 = 2×M2 주기 window, line 139/188) 로 drag tensor 계산 — 순간 조류가 아닌 조석평균 흐름에 비례하는 wave drag. deep-ocean 조석 소산의 dominant sink(천해 bottom friction 외).

## 5. Harmonic analysis (harm.F, 2071)

run 중 elevation·velocity 시계열의 **최소자승(LSQ) 조화분해** → 조석 상수 추출:
- `LSQUPDLHS`(LHS 행렬)/`LSQUPDRHS`(RHS) 누적(harm.F:62, [[adcirc-output-writers-implementation]]:64) — 요청 window 동안 frequency별 cos/sin 항 누적.
- real-time HA(HA_SUBS v3.01, RL): global elevation HA → **fort.53**, global velocity HA → **fort.54**. 불완전 run 도 분석 가능.
- 입력: fort.15 의 harmonic analysis 블록(NHARFR 주파수·HAFREQ·시작/종료). 모델 조석 ↔ 관측 조화상수 검증의 표준 도구.

## 6. 정리 — 4 조석 경로

| 항 | mechanism | 적용 |
|---|---|---|
| open-BC tidal elevation | fort.15 경계 조위(별도, BC) | 경계 node |
| **tidal potential** | constituent body force(TPK·ETRF·L_N) | 전 domain (CTIP) |
| **SAL** | self-attraction·loading(SALTAMP/PHA 공간) | 전 domain (NTIP=2) |
| **internal tide drag** | 시간평균 유속 wave drag | deep-ocean 성층 |

## 7. 연결

- [[adcirc-momentum-implementation]] — tidal potential 이 barotropic pressure(:441)에 합산
- [[adcirc-gwce-implementation]] — gwce.F:1181/2592 tidal potential
- [[adcirc-output-writers-implementation]] — harm.F harmonic accumulator → fort.53/54
- earth tide Love number(ETRF≈0.69)·SAL DB(FES/GOT) — 외부 조석 reference
- Luettich & Westerink ADCIRC theory (tidal potential·SAL 정식)
