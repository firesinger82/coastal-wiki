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
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
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


([theory 보고서 §5 1032행 (`C09`)](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md#5-차이-결론); 항목: C09 장주기 함수의 구체식 누락) 결론: C 문서 누락. 장주기 위도 함수의 실제 식과 구문서 오류는 [이론 노트의 PDF-TIDAL-L0 정본](../manual-notes/04-theory-pdf-v44xx.md#theory-tidal-l0)에 모았다. 이 행은 기존 노트의 설명 누락을 분류한다. [10-12 결론 검증 보완]
([theory 보고서 §5 1033행 (`C10`)](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md#5-차이-결론); 항목: C10 ETRF 입력·Love 수 선택 누락) 근거: `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:1540` `TPMUL=RampTip*ETRF(J)*TPK(J)*FFT(J)`<br>`models/ADCIRC/raw/source_code/adcirc/src/tidalpotential.F90:79` `real(8) :: m_k2value = 0.302d0`<br>`models/ADCIRC/raw/source_code/adcirc/src/tidalpotential.F90:80` `real(8) :: m_h2value = 0.609d0`<br>`models/ADCIRC/raw/source_code/adcirc/src/tidalpotential.F90:160` `self%m_k2value = in_k2value`<br>`models/ADCIRC/raw/source_code/adcirc/src/tidalpotential.F90:161` `self%m_h2value = in_h2value`<br>`models/ADCIRC/raw/source_code/adcirc/src/tidalpotential.F90:347` `TIPVAL = (1.d0 + self%m_k2value - self%m_h2value)*TIPVAL`<br>해석: 보고서 C10의 약 0.69는 구문서의 선택값이다. 분조 경로는 입력 ETRF를 사용한다. FullTIP 기본 객체 값은 1+0.302−0.609=0.693이고 초기화 입력이 이를 대체할 수 있다. 결론: 문서 누락. 현재 조석 감소계수는 분조 ETRF 입력 또는 FullTIP의 Love 수 입력으로 결정된다.

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
- <a id="fulltip-branches"></a>`case (2, 3)`은 2차 P2 항을 계산한다. (`src/tidalpotential.F90:262` `select case (self%m_TIPOrder)`; `src/tidalpotential.F90:263` `case (2, 3)`; `src/tidalpotential.F90:264` `! P2  term. Degree 2 or 3 tidal potential !`) [10-12 전수 검증 정정] 선택값이 3이면 P3 항을 추가한다. (`src/tidalpotential.F90:276` `if (self%m_TIPOrder == 3) then`; `src/tidalpotential.F90:277` `self%m_workarr = 5.d0*self%m_cosZA*self%m_cosZA*self%m_cosZA`; `src/tidalpotential.F90:278` `self%m_workarr = self%m_workarr - 3.d0*self%m_cosZA`; `src/tidalpotential.F90:279` `self%m_workarr = 0.5d0*self%m_workarr`) [10-12 전수 검증 정정] `case (22)`는 2차 포텐셜의 일주·반일주 성분을 계산하는 선택값이다. (`src/tidalpotential.F90:288` `case (22)`; `src/tidalpotential.F90:289` `!   P2 - Only dirunal + semi-dirunal. A special case of`; `src/tidalpotential.F90:290` `!   the degree 2 tidal potential,`; `src/tidalpotential.F90:293` `self%m_workarr = (3.d0/4.d0)*self%m_S2SFEA*sin(2.d0*DEC)*cos(self%m_AH)`; `src/tidalpotential.F90:297` `self%m_workarr = self%m_workarr + (3.d0/4.d0)*self%m_workarr1*self%m_workarr1*cos(DEC)*cos(DEC)*cos(2.d0*self%m_AH)`) [10-12 전수 검증 정정] 별도의 `case DEFAULT`는 차수 절단 없는 식을 사용한다. (`src/tidalpotential.F90:304–312`: `case DEFAULT`; `self%m_workarr = 1.d0 + AINTPOWER(radius_div_delta, 2)`; `self%m_workarr = self%m_workarr - 2.d0*radius_div_delta*self%m_cosZA`; `self%m_workarr = sqrt(self%m_workarr)`; `self%m_workarr = 1.d0/self%m_workarr`; `self%m_workarr = self%m_workarr - radius_div_delta*self%m_cosZA`) 같은 분기는 `src/tidalpotential.F90:316–319`의 C0 보정도 사용한다. [10-12 전수 검증 정정] [10-12 결론 검증 보완]
- [FullTIP 선택 분기](#fulltip-branches)의 차수·성분 선택은 포텐셜 계산의 범위를 정한다. `case DEFAULT`의 차수 절단 없는 계산도 비선형 해양 응답을 계산했다는 뜻은 아니다. [10-12 결론 검증 보완]
- 천체력 내부의 VSOP·ELP 알고리즘은 이번 대조에서 확인하지 않음. (`src/tidalpotential.F90:262` `select case (self%m_TIPOrder)`; `src/tidalpotential.F90:263` `case (2, 3)`; `src/tidalpotential.F90:288` `case (22)`)
- 이 경우 SAL 만 constituent 방식(`SALTAMP`)으로 더해짐(timestep.F:1547-1551).


([theory 보고서 §5 1034행 (`C11`)](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md#5-차이-결론); 항목: C11 FullTIP의 모든 성분 보장) 근거: [FullTIP 선택 분기 정본](#fulltip-branches). `case (2, 3)`은 차수 전개를 선택한다. `case (22)`는 2차 일주·반일주 성분만 남긴다. `case DEFAULT`는 차수 절단 없는 직접 식이다. `src/tidalpotential.F90:347`은 Love 수 배율을 적용한다. 결론: B 문서 오기. 모든 분기가 유한 차수 전개라는 설명은 철회한다. 포텐셜 계산만으로 모든 비선형 해양 응답을 보장한다는 기존 설명은 여전히 잘못이다. [10-12 결론 검증 정정]

## 4. Internal tide wave drag (internaltide.F90, 249)

성층 대양에서 조류가 거친 해저지형 위로 흐르며 **내부조석(internal tide)으로 에너지 변환** → 순압류에 작용하는 drag:
- `apply2dinternalwavedrag`(nodalattr.F) 가 실제 적용; internaltide.F90 은 보조(가독성 분리, line 27/58).
- 현재 코드는 LoadIT_Fric가 참이고 `CBaroclinic.and.abs(IDEN).ge.5`인 경로에서 `abs(IDEN).ne.7`일 때 UNTIDE를 호출한다. (`src/nodalattr.F:2619` `LoadITFric: IF (LoadIT_Fric) THEN`; `src/nodalattr.F:2656` `Baroc: IF (CBaroclinic.and.abs(IDEN).ge.5) THEN`; `src/nodalattr.F:2658` `if (abs(IDEN).ne.7) then`; `src/nodalattr.F:2659` `CALL UNTIDE(U,V,IT)`) [10-12 전수 검증 보완]
- UNTIDE의 필터 길이 상수는 25시간이다. (`src/internaltide.F90:67` `real(8), parameter :: filtL = 25d0*3600d0 ! filter length (s)`)
- UNTIDE의 표본 간격 상수는 12분이다. (`src/internaltide.F90:68` `real(8), parameter :: Fs = 12d0*60d0 ! sampling interval (s)`)
- <a id="untide-mean"></a>UNTIDE는 첫 호출에서 UBar·VBar를 0으로 초기화한다. (`src/internaltide.F90:78` `if (first_call) then`; `src/internaltide.F90:86` `UBar = 0d0`; `src/internaltide.F90:87` `VBar = 0d0`) [10-12 전수 검증 보완] `if (L > Lm) then` 안에서 `if (ISTA > NS) then`이면 NS개 표본의 산술 평균을 사용한다. (`src/internaltide.F90:92` `if (L > Lm) then`; `src/internaltide.F90:93` `if (ISTA > NS) then`; `src/internaltide.F90:103` `UBar(ii) = sum(UAV(ii, 1:NS))/dble(NS)`; `src/internaltide.F90:104` `VBar(ii) = sum(VAV(ii, 1:NS))/dble(NS)`) [10-12 전수 검증 보완] 그 `else`에서는 지금까지 채운 ISTA개 표본의 산술 평균을 사용한다. (`src/internaltide.F90:106` `else`; `src/internaltide.F90:110` `UBar(ii) = sum(UAV(ii, 1:ISTA))/dble(ISTA)`; `src/internaltide.F90:111` `VBar(ii) = sum(VAV(ii, 1:ISTA))/dble(ISTA)`) [10-12 전수 검증 보완] `src/internaltide.F90:67–68`은 25시간 길이 상수와 12분 표본 간격을 둔다. `src/internaltide.F90:90–91`은 시간 단계 번호에 DTDP를 곱한 뒤 Fs로 나눠 L·Lm을 만든다. [10-12 결론 검증 보완]
- <a id="munk-filter"></a>MunkHPFilter는 49시간 창과 1시간 표본 간격의 별도 가중 필터다. (`src/internaltide.F90:149` `real(8), parameter :: filtL = 49d0*3600d0 ! filter length (s)`; `src/internaltide.F90:150` `real(8), parameter :: T = 60d0*60d0 ! sampling interval (s)`) (`src/internaltide.F90:119` `subroutine MunkHPFilter(U_i, V_i, TimeStep)`) [10-12 전수 검증 정정] [10-12 결론 검증 보완]
- 내부 조석 변환 마찰은 선택한 입력 및 결합 경로의 계수로 항력 텐서를 만든다. (`src/nodalattr.F:2745` `TKM(1,I) = TK(I) + adju*Fit*IT_Fric(I,2)**2d0`)
- <a id="internal-tide-drag"></a>1열·3열 경압 결합은 LoadIT_Fric가 참인 `CBaroclinic.and.abs(IDEN).ge.5` 경로에 있다. (`src/nodalattr.F:2619` `LoadITFric: IF (LoadIT_Fric) THEN`; `src/nodalattr.F:2656` `Baroc: IF (CBaroclinic.and.abs(IDEN).ge.5) THEN`; `src/nodalattr.F:2687` `ELSEIF (IT_FricNoOfVals == 3.or.IT_FricNoOfVals == 1) THEN`) [10-12 전수 검증 보완] `IF (NBdiff.le.SmallV.or.Nmdiff.le.SmallV.or.`와 이어지는 `Fdiff.le.SmallV) THEN` 분기는 내부 조석 항을 추가하지 않는다. (`src/nodalattr.F:2697` `IF (NBdiff.le.SmallV.or.Nmdiff.le.SmallV.or.`; `src/nodalattr.F:2698` `&                Fdiff.le.SmallV) THEN`; `src/nodalattr.F:2700` `TKM(1:2,I) = TK(I)`; `src/nodalattr.F:2701` `TKM(3,I)   = 0.0d0`) [10-12 전수 검증 보완] 그 `ELSE`에서 `IF (abs(IDEN).NE.7) THEN`이면 조석 잔차 소산에 따른 adju를 계산한다. (`src/nodalattr.F:2702` `ELSE`; `src/nodalattr.F:2725` `IF (abs(IDEN).NE.7) THEN`; `src/nodalattr.F:2730` `Dtotal = Cxx*U(I)**2d0 +`; `src/nodalattr.F:2733` `Dtidal = Cxx*(U(I)-UBar(I))**2d0 +`) [10-12 전수 검증 보완] `IF (Dtotal.lt.1d-10) THEN`이면 adju를 0으로 설정한다. (`src/nodalattr.F:2736` `IF (Dtotal.lt.1d-10) THEN`; `src/nodalattr.F:2737` `adju = 0d0`) [10-12 전수 검증 보완] 그 `ELSE`에서는 `adju = Dtidal/Dtotal`을 계산한다. (`src/nodalattr.F:2738` `ELSE`; `src/nodalattr.F:2739` `adju = Dtidal/Dtotal`) [10-12 전수 검증 보완] 계산 뒤에는 `adju = min(adju,100d0)`을 적용한다. (`src/nodalattr.F:2741` `adju = min(adju,100d0)`) [10-12 전수 검증 보완] abs(IDEN)이 7이면 adju의 초기값 1을 유지한다. (`src/nodalattr.F:2693` `adju = 1d0; adjv = 1d0;adjuv = 1d0;`; `src/nodalattr.F:2725` `IF (abs(IDEN).NE.7) THEN`) [10-12 전수 검증 보완] 3열 입력은 adju를 텐서 성분에 적용한다. (`src/nodalattr.F:2744` `IF (IT_FricNoOfVals == 3) then`; `src/nodalattr.F:2745` `TKM(1,I) = TK(I) + adju*Fit*IT_Fric(I,2)**2d0`; `src/nodalattr.F:2746` `TKM(2,I) = TK(I) + adju*Fit*IT_Fric(I,3)**2d0`; `src/nodalattr.F:2747` `TKM(3,I) = adju*Fit*IT_Fric(I,2)*IT_Fric(I,3)`) [10-12 전수 검증 보완] 1열 입력은 adju를 두 대각 성분에 적용한다. (`src/nodalattr.F:2748` `else`; `src/nodalattr.F:2749` `TKM(1:2,I) = TK(I) + adju*Fit*IT_Fric(I,2)`; `src/nodalattr.F:2750` `TKM(3,I)   = 0.0d0`) [10-12 전수 검증 보완] [10-12 결론 검증 보완]
- 내부 조석 마찰이 deep-ocean 조석 소산의 dominant sink인지 확인하지 않음. `[source-needed]` 별도 출처와 적용 조건이 필요하다.


([features 보고서 §5 C15 (664줄)<br>C17 (666줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 내부 조석 항력과 평균 유속) 결론: B 문서 오기. 평균 유속에 직접 비례하는 항력이라는 설명은 잘못이다. 조석 잔차 소산 비율과 적용 예외의 근거는 [내부 조석 마찰 정본](#internal-tide-drag)에 모았다. 적용 사례의 지배적 에너지 소산량은 이 정적 판독으로 판정하지 않는다. [10-12 결론 검증 보완]
([features 보고서 §5 C16 (665줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: UNTIDE와 Munk_filter 혼합) 결론: B 문서 오기. `src/nodalattr.F:2659`는 UNTIDE를 호출한다. [UNTIDE 산술 평균](#untide-mean)과 [MunkHPFilter](#munk-filter)는 서로 다른 필터이다. [10-12 결론 검증 보완]

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
| **internal tide drag** | 선택한 입력·결합 경로의 계수로 만든 항력 텐서이다. | 활성 조건, 소산 비율, 상한, abs(IDEN)=7의 예외는 [내부 조석 마찰 정본](#internal-tide-drag)을 따른다. [10-12 결론 검증 보완] |

## 7. 연결

- [[adcirc-momentum-implementation]] — tidal potential 이 barotropic pressure(:441)에 합산
- [[adcirc-gwce-implementation]] — gwce.F:1181/2592 tidal potential
- [[adcirc-output-writers-implementation]] — harm.F harmonic accumulator → fort.53/54
- earth tide Love number(ETRF≈0.69)·SAL DB(FES/GOT) — 외부 조석 reference
- Luettich & Westerink ADCIRC theory (tidal potential·SAL 정식)
