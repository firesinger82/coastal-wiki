---
title: "ADCIRC 조석 forcing & 분석 — tidal potential(TPK/ETRF Love/nodal FFT) + SAL self-attraction·loading + 직접 luni-solar ephemeris + internal tide wave drag + harmonic analysis(harm.F)"
topic: adcirc
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/timestep.F (조석 potential 1509-1556) + internaltide.F90(249) + harm.F(2071) + astronomic.F90/ephemerides.F90/moon.F90 헤더 + 적용부(momentum.F:441 barotropic, gwce.F:1181/2592, CTIP) 직접 read. TIP2 식·ETRF·species L_N·SAL·NTIP=2 path file:line 인용. Luettich-Westerink ADCIRC."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 조석 potential·SAL·internal tide·harmonic 식 verbatim"
verification_date: 2026-06-03
related:
  - models/ADCIRC/source-analysis/adcirc-momentum-implementation.md
  - models/ADCIRC/source-analysis/adcirc-gwce-implementation.md
  - models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md
last_source_check: 2026-10-11 (recovery 재판독 대조)
---

# ADCIRC 조석 forcing & 분석

> `timestep.F`(tidal potential) + `internaltide.F90`(249) + `harm.F`(2071) + `astronomic/ephemerides/moon.F90` 직접 read. ADCIRC 조석 구동의 **body-force**(open-BC tidal elevation 과 별개): ① constituent tidal potential ② SAL(self-attraction & loading) ③ 직접 luni-solar ephemeris ④ internal tide wave drag ⑤ harmonic analysis(결과 분석). [[adcirc-momentum-implementation]] §1 의 barotropic pressure 에 합산되는 조석 항의 mechanism.

## 1. Tidal potential — constituent 방식 (timestep.F:1531-1560) ★

조석 천체 인력의 평형조위 forcing `TIP2(I)` (node별):
```fortran
ARGT  = AMIGT(J)*(timeh - NCYC*PERT(J)) + FACET(J)        ! 조석 argument
TPMUL = RampTip*ETRF(J)*TPK(J)*FFT(J)                      ! 진폭 multiplier
NA    = MIN(NINT(AMIGT(J)/7d-5),2)                         ! species (0/1/2)
TIP2(I) += TPMUL*L_N(NA,I)*COS(ARGT + NA*SLAM(I))          ! tidal potential
         + SALTMUL*SALTAMP(J,I)*COS(ARGT - SALTPHA(J,I))   ! SAL (§2)
```
- `NTIF` = tidal potential 상수 개수, `AMIGT`=각진동수, `PERT`=nodal 주기, `FACET`=평형 phase, `NCYC`=주기 cycle 정수(위상 reset).
- 분조 조석 포텐셜은 입력 ETRF를 곱한다. (`src/timestep.F:1540` `TPMUL=RampTip*ETRF(J)*TPK(J)*FFT(J)`)
- 0.69는 Report 1에 제시한 선택값이다. (`raw/manuals/pdfs/1992_Luettich02.pdf, PDF 쪽 23 / 인쇄 쪽 17` `\alpha=0.69;\qquad\alpha=1`)
- 코드는 모든 입력 ETRF를 0.69로 강제하지 않는다. (`src/timestep.F:1540` `TPMUL=RampTip*ETRF(J)*TPK(J)*FFT(J)`)
- 직접 FullTIP 계산의 배율은 `1.d0 + self%m_k2value - self%m_h2value`이다. (`src/tidalpotential.F90:347` `TIPVAL = (1.d0 + self%m_k2value - self%m_h2value)*TIPVAL`)
- 객체 선언의 k₂=0.302와 h₂=0.609를 그대로 쓰면 배율은 0.693이다. (`src/tidalpotential.F90:79` `real(8) :: m_k2value = 0.302d0`; `src/tidalpotential.F90:80` `real(8) :: m_h2value = 0.609d0`; `src/tidalpotential.F90:347` `TIPVAL = (1.d0 + self%m_k2value - self%m_h2value)*TIPVAL`)
- 초기화는 입력 Love 수로 선언값을 덮어쓸 수 있다. (`src/tidalpotential.F90:160` `self%m_k2value = in_k2value`; `src/tidalpotential.F90:161` `self%m_h2value = in_h2value`)
- **TPK** = tidal potential 진폭 × species 계수, **FFT** = nodal factor(18.6년 교점 보정 진폭), `RampTip`=ramp.
- **species `NA`** (주파수로 분류): 0 long-period/declinational, 1 diurnal, 2 semidiurnal. `L_N(NA,I)` = 위도 의존 geometric 함수(NA=2 → cos²φ 등), `SLAM`=경도(diurnal/semidiurnal 의 경도 의존 NA·λ).
- 현재 장주기 위도 함수는 `L_N(0,I) = 1.5d0*COS(SFEA(I))*COS(SFEA(I)) - 1d0`이다. (`src/adcirc.F:303` `L_N(0,I) = 1.5d0*COS(SFEA(I))*COS(SFEA(I)) - 1d0`)
- Report 1의 장주기 위도 함수는 `L_o=3\sin^2(\phi)-1`이다. (`raw/manuals/pdfs/1992_Luettich02.pdf, PDF 쪽 23 / 인쇄 쪽 17` `L_o=3\sin^2(\phi)-1;\quad L_1=\sin(2\phi);\quad L_2=\cos^2(\phi)`)
- 해석: 현재 장주기 위도 함수는 Report 1 함수의 −1/2이다(정적 판독, 실행 미확인). (`src/adcirc.F:303` `L_N(0,I) = 1.5d0*COS(SFEA(I))*COS(SFEA(I)) - 1d0`; `raw/manuals/pdfs/1992_Luettich02.pdf, PDF 쪽 23 / 인쇄 쪽 17`)
- 해석: 같은 진폭 계수를 넣으면 장주기 항의 부호와 크기가 다르다(정적 판독, 실행 미확인). (`src/adcirc.F:303` `L_N(0,I) = 1.5d0*COS(SFEA(I))*COS(SFEA(I)) - 1d0`)
- 일주 위도 함수는 `SIN(2d0*SFEA(I))`이다. (`src/adcirc.F:305` `L_N(1,I) = SIN(2d0*SFEA(I))`)
- 반일주 위도 함수는 `COS(SFEA(I))*COS(SFEA(I))`이다. (`src/adcirc.F:307` `L_N(2,I) = COS(SFEA(I))*COS(SFEA(I))`)
- 적용(`CTIP`): [[adcirc-momentum-implementation]] momentum.F:441 (barotropic pressure 에 합산) + [[adcirc-gwce-implementation]] gwce.F:1181/2592. timestep.F:1137-1137 `MOM_LV_X −= TIP1+TIP2`.

## 2. SAL — Self-Attraction & Loading (NTIP=2)

조석에 의한 해수 질량 재분포가 지구 중력장·해저 변형을 일으키는 2차 효과:
```fortran
TIP2(I) += SALTMUL * SALTAMP(J,I) * COS(ARGT - SALTPHA(J,I))    ! SALTMUL=RampTip*FFT
```
- `SALTAMP(J,I)`/`SALTPHA(J,I)` = **공간변화 SAL 진폭/위상**(constituent J × node I) — 외부 SAL DB(예: FES, GOT) 에서 fort.13/24 로 입력.
- `NTIP==2` 또는 `tidePotential` 비활성 시 적용(timestep.F:1531-1531). 대양 규모 조석 정확도(~5-10%)에 중요`[source-needed]`.

## 3. 직접 luni-solar ephemeris (astronomic/ephemerides/moon.F90)

`tidePotential%active()` 시 constituent 합 대신 **천체력 직접 계산**(timestep.F:162 "full luni-solar tidal potential"):
- FullTIP은 달·태양의 직접 조석 포텐셜을 계산한다. (`src/tidalpotential.F90:262` `select case (self%m_TIPOrder)`; `src/tidalpotential.F90:263` `case (2, 3)`; `src/tidalpotential.F90:288` `case (22)`; `src/tidalpotential.F90:347` `TIPVAL = (1.d0 + self%m_k2value - self%m_h2value)*TIPVAL`)
- 현재 코드에는 차수 2·3 선택과 차수 22 선택이 있다. (`src/tidalpotential.F90:262` `select case (self%m_TIPOrder)`; `src/tidalpotential.F90:263` `case (2, 3)`; `src/tidalpotential.F90:288` `case (22)`)
- 해석: 직접 천체 계산 경로의 존재는 선택한 차수 밖의 모든 항이나 비선형 해양 응답의 포텐셜 포함을 보장하지 않는다(정적 판독, 실행 미확인). (`src/tidalpotential.F90:262` `select case (self%m_TIPOrder)`; `src/tidalpotential.F90:263` `case (2, 3)`; `src/tidalpotential.F90:288` `case (22)`)
- 천체력 내부의 VSOP·ELP 알고리즘은 이번 대조에서 확인하지 않음. (`src/tidalpotential.F90:262` `select case (self%m_TIPOrder)`; `src/tidalpotential.F90:263` `case (2, 3)`; `src/tidalpotential.F90:288` `case (22)`)
- 이 경우 SAL 만 constituent 방식(`SALTAMP`)으로 더해짐(timestep.F:1547-1551).

## 4. Internal tide wave drag (internaltide.F90, 249)

성층 대양에서 조류가 거친 해저지형 위로 흐르며 **내부조석(internal tide)으로 에너지 변환** → 순압류에 작용하는 drag:
- `apply2dinternalwavedrag`(nodalattr.F) 가 실제 적용; internaltide.F90 은 보조(가독성 분리, line 27/58).
- 현재 호출은 `UNTIDE`다. (`src/nodalattr.F:2659` `CALL UNTIDE(U,V,IT)`)
- UNTIDE의 필터 길이 상수는 25시간이다. (`src/internaltide.F90:67` `real(8), parameter :: filtL = 25d0*3600d0 ! filter length (s)`)
- UNTIDE의 표본 간격 상수는 12분이다. (`src/internaltide.F90:68` `real(8), parameter :: Fs = 12d0*60d0 ! sampling interval (s)`)
- UNTIDE의 UBar·VBar는 산술 평균이다. (`src/internaltide.F90:103` `UBar(ii) = sum(UAV(ii, 1:NS))/dble(NS)`; `src/internaltide.F90:104` `VBar(ii) = sum(VAV(ii, 1:NS))/dble(NS)`)
- Munk_filter는 49시간 창과 1시간 표본 간격의 별도 가중 필터다. (`src/internaltide.F90:149` `real(8), parameter :: filtL = 49d0*3600d0 ! filter length (s)`; `src/internaltide.F90:150` `real(8), parameter :: T = 60d0*60d0 ! sampling interval (s)`)
- 내부 조석 변환 마찰은 선택한 입력 및 결합 경로의 계수로 항력 텐서를 만든다. (`src/nodalattr.F:2745` `TKM(1,I) = TK(I) + adju*Fit*IT_Fric(I,2)**2d0`)
- 1열·3열 경압 결합은 조석 잔차 소산 비율로 항력 텐서를 조정한다. (`src/nodalattr.F:2730` `Dtotal = Cxx*U(I)**2d0 +`; `src/nodalattr.F:2733` `Dtidal = Cxx*(U(I)-UBar(I))**2d0 +`; `src/nodalattr.F:2739` `adju = Dtidal/Dtotal`; `src/nodalattr.F:2745` `TKM(1,I) = TK(I) + adju*Fit*IT_Fric(I,2)**2d0`)
- 내부 조석 마찰이 deep-ocean 조석 소산의 dominant sink인지 확인하지 않음. `[source-needed]` 별도 출처와 적용 조건이 필요하다.

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
| **internal tide drag** | 선택한 입력·결합 경로의 계수로 만든 항력 텐서. (`src/nodalattr.F:2745` `TKM(1,I) = TK(I) + adju*Fit*IT_Fric(I,2)**2d0`) | 1열·3열 경압 결합은 조석 잔차 소산 비율로 조정한다. (`src/nodalattr.F:2739` `adju = Dtidal/Dtotal`) |

## 7. 연결

- [[adcirc-momentum-implementation]] — tidal potential 이 barotropic pressure(:441)에 합산
- [[adcirc-gwce-implementation]] — gwce.F:1181/2592 tidal potential
- [[adcirc-output-writers-implementation]] — harm.F harmonic accumulator → fort.53/54
- earth tide Love number(ETRF≈0.69)·SAL DB(FES/GOT) — 외부 조석 reference
- Luettich & Westerink ADCIRC theory (tidal potential·SAL 정식)
