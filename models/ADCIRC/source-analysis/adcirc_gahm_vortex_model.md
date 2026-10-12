---
title: "GAHM 비대칭 Holland 바람 모델 (gahm 라이브러리)"
model: ADCIRC
component: Parametric vortex wind/pressure forcing (GAHM, Generalized Asymmetric Holland Model)
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "소스 직접 read (gahm/src/). gahm/GahmEquations.{h,cpp}·GahmSolver.cpp·GahmRadiusSolver.cpp·GahmRadiusSolverPrivate.cpp / vortex/Vortex.cpp / atcf/AtcfSnap.cpp·AtcfFile.cpp·AtcfIsotach.h·AtcfQuadrant.h·StormTranslation.h / preprocessor/Preprocessor.cpp / physical/Atmospheric.h·Constants.h·Earth.h / fortran/gahm.F90·gahm_fortran.cpp / output/OwiOutput.h"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ADCIRC/README.md
  - models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md
  - models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

# GAHM 비대칭 Holland 바람 모델 (gahm 라이브러리)

> 요약(`models/ADCIRC/raw/source_code/gahm/src/`). GAHM = **Generalized Asymmetric Holland Model**. ATCF best-track 4분면 isotach를 입력받아 폭풍별 **분면-개별 GAHM Holland B·radius-to-max-wind**를 Newton-Raphson으로 풀고(`gahm/`+`preprocessor/`), 임의 점군에서 경도풍 합성·기압장을 만드는(`vortex/`) C++ 라이브러리. Fortran 바인딩(`fortran/gahm.F90`)으로 ADCIRC와 결합되며 OWI 격자바람(NWS12/13)도 출력 가능(`output/OwiOutput`). Author: Zach Cobell (The Water Institute), GPLv3, ADCIRC Development Group (예: `gahm/GahmSolver.cpp:1-19`).

ADCIRC NWS 외력 패밀리 전반은 [[adcirc-storm-surge-nws-families]], met-forcing 적용 맥락은 [[adcirc-met-forcing-implementation]] 참조. 본 노트는 gahm 라이브러리의 **방정식·솔버·합성 알고리즘** 자체를 다룬다.
본 노트의 방정식·수렴 허용오차·전처리 설명은 외부 gahm C++ 라이브러리에 한정한다. 외부 C++ 내부는 이번 recovery 대조에서 확인하지 않음.

ADCIRC v56.2.1의 NWS=20 Fortran 경로는 `NWS20GET`을 호출한다. (`src/wind.F:1502` `IF(NWS.EQ.20) THEN`; `src/wind.F:1503` `CALL NWS20GET(wvnx2, wvny2, prn2, timeloc)`)

이 Fortran 경로의 수치 조건은 `src/wind.F`, `wind/vortex.F`, `wind/aswip.F`로 별도 인용한다. (`wind/vortex.F:401` `if (abs(B_new-B_new1).le.0.01d0) then`; `wind/vortex.F:412` `if (abs(B-B_new).le.0.01d0) then`; `wind/aswip.F:561` `stormMotion = 1.5d0 * h_speed(ient)**0.63d0`)

두 구현의 수치 조건을 서로 옮겨 적지 않는다.

---

## 1. 라이브러리 구조 (디렉토리별 책임)

| 디렉토리 | 책임 | 핵심 파일 |
|---|---|---|
| `gahm/` | GAHM 경도풍 함수·도함수·기압식, B·Rmax 솔버 | `GahmEquations.{h,cpp}`, `GahmSolver.cpp`, `GahmRadiusSolver*.cpp` |
| `atcf/` | ATCF best-track 파싱, 4분면 isotach 자료구조, 위치·이동 | `AtcfFile.cpp`, `AtcfSnap.cpp`, `AtcfIsotach.h`, `AtcfQuadrant.h`, `StormTranslation.h` |
| `preprocessor/` | isotach 정렬·결측 보간·이동속도·경계층풍·분면별 솔버 구동 | `Preprocessor.cpp` |
| `vortex/` | 점군에서 풍속벡터·기압 합성 (시간/공간/분면 보간) | `Vortex.cpp` |
| `physical/` | 대기·지구 물리 상수와 식 (Holland B, Rossby, coriolis, haversine) | `Atmospheric.h`, `Constants.h`, `Earth.h` |
| `datatypes/` | Date, Point, CircularArray, Uvp, VortexSolution, WindGrid | `CircularArray.h`, `Date.cpp` |
| `output/` | OWI(OceanWeather) 격자바람·기압 파일 출력 | `OwiOutput.{h,cpp}` |
| `fortran/` | Fortran ↔ C++ 바인딩 (ADCIRC 결합) | `gahm.F90`, `gahm_fortran.cpp` |

전형적 호출 체인: `AtcfFile::read()` → `Preprocessor::prepareAtcfData()` + `::solve()` → `Vortex::solve(date)` (`fortran/gahm_fortran.cpp:45-52`).

---

## 2. GAHM 방정식 (`gahm/GahmEquations`)

### 2.1 경도풍 함수 $V_g(r)$

소스 doc 주석(verbatim, `gahm/GahmEquations.cpp:28-37`):

$$V_g(r) = \sqrt{\frac{f^2 r^2}{4} + v_m^2 e^{\beta}(\gamma+1)\,\alpha^{b_g}} - \frac{f r}{2}$$

여기서 $\alpha = \frac{r_m}{r}$, $\beta = -\phi(\alpha^{b_g}-1)$, $\gamma = \frac{f r_m}{v_m}$.

구현(`gahm/GahmEquations.cpp:46-61`)은 $(\gamma+1)$을 `(1.0 + 1.0/rossby)`로 표현한다 — Rossby 수 $Ro = v_m/(f r_m)$ (`physical/Atmospheric.h:52-58`)이므로 $1/Ro = f r_m / v_m = \gamma$. $e^\beta$는 `std::exp(phi * (1.0 - rmbg))`, $\alpha^{b_g}$는 `rmbg = pow(rmax/distance, gahm_b)` (`GahmEquations.cpp:50-57`). 함수는 **isotach 풍속을 뺀 잔차**를 반환한다(`...) - isotach_windspeed_at_boundary_layer`, `GahmEquations.cpp:60`) — 즉 솔버의 근(root)이 되도록 구성. coriolis 부호로 남반구 처리(`sign_of_coriolis`, `GahmEquations.cpp:53`).

phi를 인자로 안 주는 오버로드는 내부에서 `phi(...)`를 계산해 위임(`GahmEquations.cpp:79-89`).

### 2.2 $\phi$ 파라미터 (`gahm/GahmEquations.h:68-76`)

$$\phi = 1 + \frac{1}{Ro \cdot b_g \,(1 + 1/Ro)}$$

`constexpr`, $Ro$는 `Atmospheric::rossbyNumber(vmax,rmax,f)`. assert로 $f>0, v_m>0, r_m>0$ 강제(`GahmEquations.h:70-72`).

### 2.3 GAHM 수정 Holland B (`gahm/GahmEquations.h:88-98`)

$$b_g = b_H \cdot \frac{(1 + 1/Ro)\,e^{\phi - 1}}{\phi}$$

여기서 전통적 Holland B는 (`physical/Atmospheric.h:38-43`):

$$b_H = \frac{v_m^2 \,\rho_{air}\, e}{p_{bk} - p_c}$$

$\rho_{air} = 1.293$ kg/m³ (`physical/Constants.h:88`), $e = M\_E$. assert로 $p_c \ne p_{bk}$ 강제(`Atmospheric.h:40`).

### 2.4 1차 도함수 $V_g'(r)$ (`gahm/GahmEquations.cpp:91-133`)

Newton-Raphson용. doc 주석에 폐형식(verbatim, `GahmEquations.cpp:92-96`). 구현은 항별 분해 `a + b - c` over `d` (`GahmEquations.cpp:113-132`).

### 2.5 기압장 (`gahm/GahmEquations.cpp:147-154`)

$$p(r) = p_c + (p_{bk} - p_c)\, e^{-\phi (r_m/r)^{b_g}}$$

표준 Holland 압력식의 GAHM($\phi$·$b_g$) 버전.

### 2.6 풍속 평가 (`gahm/GahmEquations.cpp:156-162`)

`GahmWindSpeed` = `GahmFunction(rmax, vmax, **0.0**, distance, coriolis, gahm_b)` — isotach 잔차항을 0으로 둬 순수 $V_g(r)$ 값을 얻는다.

---

## 3. 솔버 (`gahm/GahmSolver`, `GahmRadiusSolver*`)

### 3.1 GahmSolver — B와 Rmax 동시 수렴 외부 루프

입력: `(isotach_radius, isotach_speed, vmax, p_center, p_background, latitude)` (`gahm/GahmSolver.cpp:46-47`).

초기화(`gahm/GahmSolver.cpp:46-63`):
- coriolis: `Earth::coriolis(latitude)` (`GahmSolver.cpp:54`).
- Rmax 초기추정 `estimateRmax` (아래 3.3).
- B 초기값 = 전통 Holland B (`calcHollandB`, `GahmSolver.cpp:58`).
- $\phi$ 초기 1.0, B 수렴 tol `1e-9`, 최대 반복 200 (`GahmSolver.cpp:59-61`).
- ADCIRC Fortran 반복의 B 변화 허용오차는 0.01이다. (`wind/vortex.F:401` `if (abs(B_new-B_new1).le.0.01d0) then`; `wind/vortex.F:412` `if (abs(B-B_new).le.0.01d0) then`)
- GAHM 문서는 B와 Phi가 모두 수렴할 때까지 반복한다고 적는다. (`docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:487` ``:math:`\varphi` can be solved iteratively from (9) and (11) until both converge,``)
- Fortran의 이 비교는 Phi 변화량을 따로 검사하지 않는다. (`wind/vortex.F:401` `if (abs(B_new-B_new1).le.0.01d0) then`; `wind/vortex.F:412` `if (abs(B-B_new).le.0.01d0) then`)
- 위 C++의 `1e-9` 설명은 외부 gahm 구현 범위에 남긴다. 외부 C++ 원문은 이번 recovery 대조에서 확인하지 않음.

`solve()` 루프(`gahm/GahmSolver.cpp:68-92`):
1. `GahmRadiusSolver::solve(1.0, isotach_radius, guess)` → 새 rmax (Newton-Raphson, 하한 1, 상한 isotach 반경).
2. `phi = GahmEquations::phi(vmax, rmax, B, f)` 갱신 (`GahmSolver.cpp:77`).
3. `B = GahmEquations::gahm_b(vmax, rmax, p_c, p_bk, f, phi)` 갱신 (`GahmSolver.cpp:78`).
4. `|B - solver.gahm_b()| < 1e-9` 이면 수렴·종료(`GahmSolver.cpp:79-82`).
5. NaN/Inf 발생 시 `boost::math::evaluation_error("Solution did not converge.")` (`GahmSolver.cpp:83-87`).
6. 미수렴 시 `solver.setGahmB(B)` 후 반복(`GahmSolver.cpp:88`).

즉 **Rmax(Newton 내부) ↔ B/phi(외부) 교대 수렴(fixed-point)**. 미실행 상태에서 `rmax()`/`gahm_b()` 호출 시 예외(`GahmSolver.cpp:141-160`).

### 3.2 GahmRadiusSolver — Newton-Raphson

`boost::math::tools::newton_raphson_iterate(m_solver, guess, lower, upper, digits, iter)` 사용, 최대 200회(`gahm/GahmRadiusSolver.cpp:31,56-62`). functor `GahmRadiusSolverPrivate::operator()`가 `{Vg, Vg'}` 쌍을 반환(`gahm/GahmRadiusSolverPrivate.cpp:45-52`), 각각 `GahmFunction`/`GahmFunctionDerivative` 위임(`GahmRadiusSolverPrivate.cpp:76-97`).

### 3.3 Rmax 초기추정 (`gahm/GahmSolver.cpp:181-189`)

회귀식(dp: Pa, lat: deg):

$$r_1 = \exp\!\big(3.015 - 6.291\times10^{-5}(dp/100)^2 + 0.337\,\mathrm{lat}\big)$$

`min(r1, 0.99 × isotach_radius)` 채택(`GahmSolver.cpp:185-188`). isotach 반경의 99%를 상한으로 둔다.

---


([features 보고서 §5 H30 (490줄)<br>C37 (686줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM 수렴 종료 기준) 근거: [10-12 결론 정정] H30: both converge라는 설명만으로 Phi의 독립 허용오차 검사를 요구할 수 없다. 소스는 B로 Phi를 갱신하며 B 변화량으로 종료한다. features 보고서 §5 H30·C37은 종료 기준 누락을 C로 분류한다.<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:486 ``Given an initial guess of :math:`R_{max}`, values of :math:`B_g` and``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:487 ``:math:`\varphi` can be solved iteratively from (9) and (11) until both converge,``<br>wind/vortex.F:401 `if (abs(B_new-B_new1).le.0.01d0) then`<br>wind/vortex.F:402 `EXIT`<br>wind/vortex.F:412 `if (abs(B-B_new).le.0.01d0) then`<br>wind/vortex.F:413 `EXIT`<br>wind/vortex.F:388 `! determine if B converges, if yes, break loop and assign`<br>해석: 문서는 both converge라고만 적고 수치 허용오차를 정의하지 않는다. 코드는 Phi를 B에 연결해 갱신하지만 Phi의 별도 변화량을 검사하지 않는다. 따라서 수렴 불가능이나 결함을 단정하지 않고 종료 기준의 누락으로 분류한다. 외부 C++의 1e-9는 다른 구현 범위다. C37의 기존 설명은 외부 C++의 범위다. 이 C 판정은 현행 rst에서 Fortran 종료 기준을 생략한 데 적용한다. 결론: 문서 누락. Fortran GAHM은 B 변화량이 0.01 이하이면 반복을 종료한다. [10-12 결론 검증 보완]
([features 보고서 §5 H43 (503줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 관측 isotach 재현 설명의 수렴·대체값 조건 누락) 근거: docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:596–598은 `match all observed storm isotaches`라고 설명한다. 같은 문서 365줄은 34·50·64 kt isotach 입력을 설명한다.<br>추가 원문: wind/vortex.F:334–338은 `innerRadius = 1.d0`, `outerRadius = 500.d0`, `zoom = 0.01d0`, `itmax = 3`을 선언한다. 364–369줄은 `dr = 1.d0`에서 시작하여 `root = findRoot(VhWithCoriFull, r1,r2, dr, r3,r4)`와 `dr = dr * zoom`을 반복한다.<br>wind/vortex.F:372·382–384: `if (root.lt.0.d0) then` / `root=1.0*radius(quad)` / `norootflg=1` / `endif`. 385줄: `Rmaxes(n+1) = root`.<br>wind/vortex.F:401–403은 `if (abs(B_new-B_new1).le.0.01d0) then`에서 반복을 끝낸다. 597–600줄은 `IF (iter >= itmax) THEN`에서 `findRoot = -99999.0`을 반환한다.<br>해석: 근을 찾지 못한 경로는 입력 isotach의 반경을 Rmax로 대입한다. 이 대체값은 원래 풍속 잔차를 0으로 만든 근이라는 조건을 검사하지 않는다. 정상 반복에도 유한한 탐색 간격과 B의 수렴 허용값이 있다. 문서의 전체 isotach 재현 설명에 이 조건들이 빠져 있으므로 C로 분류한다.<br>추가 검색: raw와 판독 기록 전체에서 `isotach`, `norootflg`, `findRoot`, `VhWithCoriFull`을 검색했다. calcRmaxesFull의 실패 처리와 GAHM 시험 입력을 추가로 확인했다. 결론: 문서 누락. 관측 isotach 재현 설명에는 근 탐색 실패 시 Rmax 대체값과 수렴 허용값을 덧붙여야 한다. [10-12 G 재판정]
([features 보고서 §5 C36 (685줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 외부 GAHM C++ 재구현과 ADCIRC Fortran의 판 차이) 근거: features 보고서 §4 C36이 보존한 노트는 외부 gahm/src 경로를 지칭한다.<br>추가 원문: `models/ADCIRC/raw/source_code/gahm/README.md:7–9`는 ADCIRC에 포함된 GAHM을 다시 구현한 독립 프로젝트라고 설명한다. 로컬 gahm의 HEAD는 `bcbb0fe857098affb91fce3c24e1f099a244b80d`이다.<br>`models/ADCIRC/raw/source_code/gahm/src/gahm/GahmSolver.cpp:59·61`은 `m_bg_tol(1e-9)`와 `m_max_it(200)`을 설정한다. 79줄은 `if (std::abs(m_bg - m_solver.gahm_b()) < m_bg_tol) {`이다.<br>`models/ADCIRC/raw/source_code/gahm/src/gahm/GahmRadiusSolver.cpp:60–62`는 `return boost::math::tools::newton_raphson_iterate(` / `m_solver, guess, lower, upper, std::numeric_limits<double>::digits,` / `iter);`를 사용한다.<br>ADCIRC의 wind/vortex.F:565는 `INTEGER , PARAMETER :: itmax = 400`이다. 577줄은 `b = x1 + iter * dx`이다. 580줄은 `IF ((fa*fb < 0.0d0) .OR. (ABS(fb) > ABS(fa))) THEN`이다. 583·585줄은 a 또는 b를 근으로 선택한다.<br>해석: 두 원문은 별도 구현임을 명시한다. 두 구현의 근 탐색 방법과 수렴 조건도 다르다. 외부 C++ 노트의 조건을 ADCIRC Fortran 조건으로 옮길 수 없는 이유를 A 판 차이로 분류한다. 이 판정은 두 라이브러리의 모든 물리식이 동치라는 주장이 아니다.<br>추가 검색: raw와 판독 기록 전체에서 `reimplements`, `GahmSolver`, `newton_raphson_iterate`, `findRoot`를 검색했다. 외부 gahm의 README·수치해법과 ADCIRC의 실제 NWS20GET 경로를 추가로 대조했다. 결론: 판 차이. 외부 GAHM C++ 재구현의 근 탐색 조건은 ADCIRC v56.2.1 Fortran과 다른 구현판의 조건이다. [10-12 G 재판정] [10-12 결론 검증 보완]

## 4. ATCF best-track 입력 (`atcf/`)

### 4.1 파일 읽기 (`atcf/AtcfFile.cpp:46-85`)

라인별 `AtcfSnap::parseAtcfSnap`. 동일 날짜 snap이 이미 있으면 **isotach만 추가**(중복 날짜 병합), 없으면 새 snap push(`AtcfFile.cpp:74-85`). `isValid()` 통과분만 수용(`AtcfFile.cpp:56-59`).

### 4.2 snap 파싱 (`atcf/AtcfSnap.cpp:309-354`)

ATCF 토큰 ≥27개 요구(`AtcfSnap.cpp:319-321`). 주요 컬럼:
- `tokens[0]` basin (WP/IO/SH/CP/EP/AL/SL → enum, `AtcfSnap.cpp:83-101`).
- `tokens[2]`+`tokens[5]` 날짜+tau (`%Y%m%d%H` + 시간 가산, `AtcfSnap.cpp:393-400`).
- `tokens[6]`/`[7]` 위/경도 (1/10 deg, S/W 부호, `AtcfSnap.cpp:328-338`).
- `tokens[8]` vmax (kt→m/s), `tokens[9]` p_min (mb→Pa ×100), `tokens[19]` rmax (nmi→m) (`AtcfSnap.cpp:340-342`).
- 배경기압은 상수 `backgroundPressure()=1013.0` mb ×100 (`AtcfSnap.cpp:346`, `Constants.h:68`).
- `tokens[27]` 폭풍명(`AtcfSnap.cpp:343`).

isotach 파싱(`AtcfSnap.cpp:361-385`): `tokens[11]` isotach 풍속(kt→m/s). **0이면** isotach 풍속=vmax, 4분면 반경=rmax로 대체(`AtcfSnap.cpp:371-376`). 아니면 `tokens[13..16]`이 4분면 반경(nmi→m)(`AtcfSnap.cpp:378-383`). 단위 변환은 `compile-time constexpr` (`Units::convert`, `AtcfSnap.cpp:311-314`).

`isValid()`(`AtcfSnap.cpp:428-444`): isotach 비어있거나, 위치가 (0,0)이거나, 날짜가 기본값이거나, 풍속 0인 isotach가 하나라도 있으면 false.

### 4.3 4분면 isotach 자료구조

- `AtcfQuadrant`(`atcf/AtcfQuadrant.h:36-103`): 분면별 `isotach_radius`, `radius_to_max_wind_speed`, `gahm_holland_b`, `isotach_speed_at_boundary_layer`, `vmax_at_boundary_layer` 보유. 분면 각도 `s_quadrant_angles = {45, -45, -135, -225}°`(`AtcfQuadrant.h:97-101`).
- `AtcfIsotach`(`atcf/AtcfIsotach.h:39-76`): 한 풍속(`m_wind_speed`)에 대한 4분면 `CircularArray<AtcfQuadrant,4>`.
- `CircularArray`(`datatypes/CircularArray.h:45-48`): 모듈로 인덱싱으로 음수·초과 인덱스 wrap. → `quadrant - 1`, `quadrant + index` 식 분면 접근(§5.3) 가능케 함.
- `AtcfSnap`(`atcf/AtcfSnap.h`): 한 시각에 여러 isotach `std::vector<AtcfIsotach>` + 분면별 반경 사전계산 `m_radii` (`CircularArray<vector<double>,4>`, `AtcfSnap.cpp:284-287,559-565`).

---


([features 보고서 §5 H18 (478줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: ATCF 입력의 통상 시간 간격) 근거: docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:360–366은 NHC의 ATCF 입력을 설명한다. 363줄의 표현은 `usually at 6-hour intervals`이다.<br>추가 원문: `models/ADCIRC/raw/source_code/gahm/tests/test_files/bal122005.dat:1–4`의 BEST 시각은 순서대로 `2005082318`, `2005082400`, `2005082406`, `2005082412`이다. 7–8줄은 같은 `2005082506` 시각의 서로 다른 isotach를 담는다.<br>해석: 첫 네 시각의 간격은 6시간이다. 같은 시각의 여러 isotach 행을 서로 다른 시각의 입력으로 세지 않는다. 문서의 usually는 모든 입력의 고정 간격을 뜻하지 않는다.<br>검색: 전체 `models/ADCIRC/raw/`에서 `rg -i`로 `6.hour|ATCF|BEST`를 확인했다. 보조 프로그램 aswip.F와 ATCF 시험 자료도 검색된다. 해석: 시험 파일은 일부 6시간 간격의 사례이다. 입력 자료의 통상 제공 주기는 코드가 진위를 정하는 주장이 아니다. 결론: H 코드 대조 대상 아님. `usually at 6-hour intervals`를 모든 입력의 고정 간격으로 바꾸지 않는다. [10-12 결론 검증 정정]
([features 보고서 §5 K62 (626줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM isotach 개수) 근거: src/wind.F:5877 `if ( cycle_num1(ient) == cycle_num1(ient-1)) then`<br>src/wind.F:5878 `isot=isot+1 ! same icyc, next isotach`<br>src/wind.F:5879 `if (isot.gt.4) then`<br>src/wind.F:5881 `&             'The GAHM fort.22 input file has more than 4 ',`<br>src/wind.F:5882 `&             'isotachs in cycle ',cycle_num1(ient),'.'`<br>src/wind.F:5883 `call terminate(exit_code=ADCIRC_EXIT_FAILURE,`<br>해석: 대조 문서는 이 입력 개수 상한을 적지 않았다. 결론: 문서 누락. GAHM fort.22 입력은 한 cycle의 isotach가 4개를 넘으면 종료한다.
([features 보고서 §5 K65 (629줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM 음의 반경 해) 근거: wind/vortex.F:372 `if (root.lt.0.d0) then`<br>wind/vortex.F:382 `root=1.0*radius(quad)`<br>wind/vortex.F:383 `norootflg=1`<br>wind/vortex.F:385 `Rmaxes(n+1) = root`<br>해석: 문서의 반복 해법 설명은 음의 해에 대한 대체값을 적지 않았다. 결론: 문서 누락. GAHM의 반경 해 root가 음수이면 코드는 관측 isotach 반경으로 대체한다.

## 5. 전처리 (`preprocessor/Preprocessor`)

### 5.1 파이프라인 (`preprocessor/Preprocessor.cpp:54-63`)

`prepareAtcfData()`:
1. `orderIsotachs()` — snap 내 isotach 풍속 **내림차순** 정렬(`Preprocessor.cpp:345-349`, `AtcfSnap.cpp:571-576`).
2. `fillMissingAtcfData()` — 결측 분면 반경 보간.
3. `computeStormTranslationVelocities()` — 이동속도·방향.
4. `computeBoundaryLayerWindspeed()` — 10m → 경계층 변환.
5. `processIsotachRadii()` — 분면별 반경 배열 사전계산.

### 5.2 결측 isotach 반경 보간 (`Preprocessor.cpp:107-201`)

분면 결측(반경=0) 개수별:
- 1개: 좌(`idx+3`)·우(`idx+1`) **이웃 평균** (CircularArray wrap, `Preprocessor.cpp:188-201`).
- 2개: 남은 둘의 평균(`/2.0`, `Preprocessor.cpp:167-182`).
- 3개: 유일하게 존재하는 값 복사(`Preprocessor.cpp:152-161`).
- 4개: 전부 snap의 rmax로 설정(`Preprocessor.cpp:141-146`).

### 5.3 이동속도 (`Preprocessor.cpp:206-257`)

snap 쌍 위치차를 `Earth::sphericalDx`(haversine 분해, `Earth.h:174-182`)로 u·v 거리 산출, $dt$로 나눠 속도. 방향 `atan2(u, v)` (북기준, `Preprocessor.cpp:249`). 합성 이동속도에 **경험식 변환** 적용(`Preprocessor.cpp:254`):

$$U_{trans} = 1.5\, U_{raw}^{0.63}$$
현재 Fortran도 원 이동속도를 경험식 보정 이동속도로 바꾼다. (`wind/aswip.F:561` `stormMotion = 1.5d0 * h_speed(ient)**0.63d0`; `src/wind.F:6193` `stormMotion = 1.5d0*(SQRT(uTransNow**2.d0+vTransNow**2.d0))**0.63d0`)

GAHM 문서의 VT는 연속 중심 위치에서 계산한 이동속도다. (`docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:390` ``:math:`\overrightarrow{V_T}` is the storm translational speed calculated from``; `docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:391` ``successive storm center locations, :math:`W_{rf} = 0.9` is the wind reduction``)

해석: 원 이동속도와 경험식 보정 이동속도를 구분하면 문서 식 (14)·(17)의 입력 차이가 드러난다(정적 판독, 실행 미확인). (`docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:382` `V_{max} = \vert \frac{\overrightarrow{V_M} - \gamma\overrightarrow{V_T}}{W_{rf}} \vert = \frac{V_M - \gamma V_T}{W_{rf}} \quad (14)`; `docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:443` `& = \frac{\vert\overrightarrow{V_{isot}} - \gamma\overrightarrow{V_T}  \vert}{W_{rf}}`; `wind/aswip.F:561` `stormMotion = 1.5d0 * h_speed(ient)**0.63d0`)

첫 snap은 다음 snap으로, 그 외는 이전 snap과의 차로 forward/backward 차분(`Preprocessor.cpp:206-222`).

### 5.4 경계층 풍속 (`Preprocessor.cpp:317-339`)

- snap vmax: 10m → 경계층 = `× tenMeterToTopOfBoundaryLayer()` = `1/0.9 ≈ 1.111` (`Preprocessor.cpp:319-320`, `Constants.h:74-82`), 이후 이동속도 제거.
- isotach 분면 풍속: `removeTranslationVelocity`로 이동성분 차감(scaling = `min(1, ws/vmax)`, `Preprocessor.cpp:307-312`) 후 경계층 변환(`Preprocessor.cpp:325-335`).
- **참고**: 분면별 회전 기반 제거(`removeTranslationVelocity(.., quadrant, ..)`)는 현재 본문이 주석처리되고 `wind_speed`를 그대로 반환 — `// TODO`/실험 상태(`Preprocessor.cpp:271-297`).
ASWIP 기본 approach=2 경로는 회전각을 만든다. (`wind/aswip.F:2828` `approach=2           ! set both Vr and quadrantVr tangential to azimuth`; `wind/aswip.F:677` `quadrantvecangles(i) = quadrantAngles(i)+`; `wind/aswip.F:678` `&             (90.0d0+quadrotateAngle(i))*deg2rad`)

이 경로는 `if ((iquadrot == 1).or.(VmwBLflag(i) == 0)) then`에서 이동 벡터를 제거한 크기를 계산한다. (`wind/aswip.F:684` `if ((iquadrot == 1).or.(VmwBLflag(i) == 0)) then`; `wind/aswip.F:706` `quadrantVr(i) = sqrt(`; `wind/aswip.F:707` `&                   (U_Vr - gamma(i)*stormMotionU)**2.0d0`; `wind/aswip.F:708` `&                  +(V_Vr - gamma(i)*stormMotionV)**2.0d0`; `wind/aswip.F:709` `&                  )/windReduction`) [10-12 전수 검증 보완] 뒤의 `if (( quadrantVr(i).gt.VmaxBL ).or.(VmwBLflag(i) == 1)) then`은 해당 분면의 값을 재계산한다. (`wind/aswip.F:718` `if (( quadrantVr(i).gt.VmaxBL ).or.(VmwBLflag(i) == 1)) then`; `wind/aswip.F:722` `if (ir(ient,i).gt.0) then`) [10-12 전수 검증 보완]

<a id="gahm-inner-inflow"></a>Fortran 유입각은 `IF (0.0d0 <= r .AND. r < rmx) THEN`에서 `fang = 10.0d0 * r/rmx`를 사용한다. (`wind/vortex.F:1147` `IF (0.0d0 <= r .AND. r < rmx) THEN`; `wind/vortex.F:1148` `fang = 10.0d0 * r/rmx`) [10-12 전수 검증 보완] 세 반경 조건을 모두 통과하지 못하면 마지막 `ELSE`에서 0을 사용한다. (`wind/vortex.F:1149` `ELSE IF (rmx <= r .AND. r < 1.2d0*rmx) THEN`; `wind/vortex.F:1151` `ELSE IF (r >= 1.2d0*rmx) THEN`; `wind/vortex.F:1153` `ELSE`; `wind/vortex.F:1154` `fang = 0.0d0`) [10-12 전수 검증 보완] [10-12 결론 검증 보완]

rst 식 (16)은 이 구간의 유입각을 상수 10°로 적는다. (`docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:424` `10^{\circ}, & r<R_{max} \\`)

위 외부 C++의 비활성 블록 설명은 이 ASWIP 경로에 적용하지 않는다.

### 5.5 분면별 솔버 구동 (`Preprocessor.cpp:68-102`)

`prepareAtcfData()` 선행 필수(미처리 시 runtime_error, `Preprocessor.cpp:69-74`). 모든 snap × isotach × **4분면** 각각:
- `vmax ≤ isotach_speed`면 `vmax = isotach_speed + 1.0`로 넛지(`Preprocessor.cpp:90-91`, "// TODO: Confirm with Rick").
- `GahmSolver(isotach_radius, isotach_speed, vmax, p_min, p_back, latitude).solve()` → 분면에 `rmax`, `gahm_b` 저장(`Preprocessor.cpp:94-98`).

즉 **각 분면이 독립적인 Rmax·B**를 가져 비대칭(asymmetric) 구조가 형성된다.

---


([features 보고서 §5 H20 (480줄)<br>K61 (625줄)<br>C38 (687줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 폭풍 이동속도 경험 보정) 근거: docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:382 `V_{max} = \vert \frac{\overrightarrow{V_M} - \gamma\overrightarrow{V_T}}{W_{rf}} \vert = \frac{V_M - \gamma V_T}{W_{rf}} \quad (14)`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:389 ``meter height assuming in the same direction as :math:`\overrightarrow{V_T}`,``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:390 ``:math:`\overrightarrow{V_T}` is the storm translational speed calculated from``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:391 ``successive storm center locations, :math:`W_{rf} = 0.9` is the wind reduction``<br>wind/aswip.F:561 `stormMotion = 1.5d0 * h_speed(ient)**0.63d0`<br>wind/aswip.F:564 `VmaxBL = ( Vmax - stormMotion ) / windReduction`<br>wind/aswip.F:561 `stormMotion = 1.5d0 * h_speed(ient)**0.63d0`<br>wind/aswip.F:2828 `approach=2           ! set both Vr and quadrantVr tangential to azimuth`<br>src/wind.F:6193 `stormMotion = 1.5d0*(SQRT(uTransNow**2.d0+vTransNow**2.d0))**0.63d0`<br>src/wind.F:6193 `stormMotion = 1.5d0*(SQRT(uTransNow**2.d0+vTransNow**2.d0))**0.63d0`<br>해석: 문서는 VT를 연속 중심 위치에서 구한 속도로 정의하지만 그 뒤의 경험 보정을 적지 않는다. aswip.F와 wind.F의 두 경로가 같은 변환을 사용한다. 외부 C++ 노트의 정확도는 이 결론에 포함하지 않는다. C38의 C++ 경험식 인용은 보고서의 보존 내용이다. 현행 Fortran에서도 같은 형태를 확인했으므로 이 C 판정은 rst의 이동속도 정의 누락에 적용한다. 결론: 문서 누락. 현재 Fortran GAHM은 원 이동속도를 1.5*Uraw**0.63으로 바꿔 사용한다.
([features 보고서 §5 H23 (483줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 이동 보정 비율의 극값 설명에서 빠진 분기) 근거: docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:402의 식은 `\gamma = \frac{V_g}{V_{max}} \quad (15)`이다. 408–411줄은 중심에서 0이고 Rmax에서 1인 이상 프로파일을 설명한다.<br>추가 원문: wind/vortex.F:829–834는 `IF (idist < 1.d0) THEN`에서 유속을 0으로 두고 RETURN한다. 846줄은 `percentCoriolis=1.0d0`이다.<br>wind/vortex.F:848–856의 원문은 `IF (geof == 1) THEN` / `speed = SQRT(` / `&           ((Vmax*kt2ms)**2.d0+Vmax*kt2ms*rmx*nm2m` / `&             *percentCoriolis*corio)` / `&                  * (rmx/idist)**B` / `&                  * EXP(Phi*(1.d0-(rmx/idist)**B))` / `&            + (nm2m*idist*percentCoriolis` / `&                           *corio/2.d0)**2.d0)` / `&            - nm2m*idist*percentCoriolis*corio/2.d0`이다.<br>해석: 식 전개를 위해 v를 `Vmax*kt2ms`로 둔다. c를 `rmx*nm2m*corio/2.d0`으로 둔다. 양수 v·c와 `idist=rmx`를 위 식에 대입하면 `sqrt((v+c)^2)-c=v`이다. 이 대입은 중심 보호 분기를 통과하는 반경에 한정한다.<br>추가 원문: wind/vortex.F:857–863의 ELSE 경로는 `speed = SQRT(` / `&           (Vmax*kt2ms)**2.d0 * (rmx/idist)**B` / `&            * EXP(1.d0-(rmx/idist)**B)` / `&            + (nm2m*idist*percentCoriolis` / `&            *corio/2.d0)**2.d0)` / `&            - nm2m*idist*percentCoriolis*corio/2.d0`이다.<br>해석: 같은 대입을 ELSE 식에 적용하면 `sqrt(v^2+c^2)-c<v`이다. 따라서 이 분기의 Rmax에서 비율은 1보다 작다.<br>wind/vortex.F:866–867: `TransSpdX = (abs(speed/(Vmax*kt2ms)))*uTrans*kt2ms` / `TransSpdY = (abs(speed/(Vmax*kt2ms)))*vTrans*kt2ms`.<br>해석: 코드의 이동 보정은 두 분기에서 계산한 speed를 사용한다. 문서의 극값 설명에는 중심 보호와 geof 분기의 범위가 빠져 있다. 이 누락을 C로 분류한다.<br>추가 검색: raw와 판독 기록 전체에서 `TransSpdX`, `geof`, `iVm`, `gamma`를 검색했다. uvpr의 두 속도 식과 이동 보정의 계산 순서를 추가로 대조했다. 결론: 문서 누락. 이동 보정 비율의 Rmax 극값 설명에는 중심 보호 조건과 geof에 따른 속도식의 차이를 덧붙여야 한다. [10-12 G 재판정]

## 6. 바람장 합성 (`vortex/Vortex`)

### 6.1 시각 솔브 (`vortex/Vortex.cpp:64-114`)

`solve(date)`:
1. `selectTime` — 날짜 구간의 snap iterator + 선형 시간가중 `time_weight` (`Vortex.cpp:266-288`). 범위 밖이면 양끝으로 clamp(`Vortex.cpp:268-272`).
2. 폭풍 위치·이동·배경/중심기압을 두 snap 사이 보간(`StormPosition::interpolate`, `StormTranslation::interpolate`, `Interpolation::linear`, `Vortex.cpp:81-92`).
3. coriolis = `Earth::coriolis(보간된 위도)` (`Vortex.cpp:106`).
4. 점군 각 점에 `solveVortexPoint` → `VortexSolution`(u,v,p) (`Vortex.cpp:109-113`).

### 6.2 점별 해 (`vortex/Vortex.cpp:116-156`)

- 거리 `Earth::distance`(haversine, `Earth.h:105-118`), 1km 이내면 (u,v)=0, p=중심기압/100(`Vortex.cpp:122-128`).
- 방위각 `Earth::azimuth` (`Earth.h:139-152`).
- `getInterpolatedPack` → 파라미터팩(rmax, vmax_bl, isotach_speed, holland_b 등).
- `phi`, `GahmWindSpeed`로 풍속, `GahmPressure`로 기압(/100 → mb)(`Vortex.cpp:140-153`).

### 6.3 분면·isotach·시간 보간 (파라미터팩)

`getInterpolatedPack`(`Vortex.cpp:158-177`): 두 시각 각각에서 점위치 파라미터팩을 만들고 시간 선형보간.

`getBaseQuadrant`(`Vortex.cpp:315-340`): 방위각을 45°/135°/225°/315° 경계로 분면 0~3 + delta_angle 산출. `getBaseIsotach`(`Vortex.cpp:349-370`): 거리에 대해 해당 분면 isotach 반경 배열에서 lower_bound로 isotach 인덱스+가중. 거리가 최외곽 isotach 밖이면 최외곽, 안쪽이면 0.
<a id="gahm-angle-interp"></a>Fortran 각도 보간은 `if ( delta_angle.lt.1.d0 ) then`에서 현재 분면의 반경 보간값을 사용한다. (`wind/vortex.F:966` `if ( delta_angle.lt.1.d0 ) then`; `wind/vortex.F:967` `spInterp=interpR(param, iquad, dist)`) [10-12 전수 검증 보완] `else if (delta_angle.gt.89.d0) then`에서는 다음 분면의 값을 사용한다. (`wind/vortex.F:968` `else if (delta_angle.gt.89.d0) then`; `wind/vortex.F:969` `spInterp=interpR(param, iquad+1, dist)`) [10-12 전수 검증 보완] 그 밖에는 사분면의 delta_angle로 역제곱 가중 보간을 수행한다. (`wind/vortex.F:970` `else`; `wind/vortex.F:973` `spInterp = ( temp1/delta_angle**2.d0`; `wind/vortex.F:974` `&             + temp2/(90.0-delta_angle)**2.d0 )`; `wind/vortex.F:975` `&             / ( 1.d0/delta_angle**2.d0`; `wind/vortex.F:976` `&              + 1.d0/(90.d0-delta_angle)**2.d0 )`) [10-12 전수 검증 보완] [10-12 결론 검증 보완]

해석: `case(3)`에서 QuadIr4의 1·2·3번 반경을 문서의 R34·R50·R64에 대응시킬 때, `else if (r > QuadIr4(quad,3)) then` 분기의 `(r-R64)/(R50-R64)`는 P50의 가중치다. (`wind/vortex.F:1004` `case(3)`; `wind/vortex.F:1005` `if (r > QuadIr4(quad,1)) then`; `wind/vortex.F:1007` `else if (r > QuadIr4(quad,2)) then`; `wind/vortex.F:1012` `else if (r > QuadIr4(quad,3)) then`; `wind/vortex.F:1013` `fac = (r-QuadIr4(quad,3))/`; `wind/vortex.F:1014` `&               (QuadIr4(quad,2)-QuadIr4(quad,3))`; `wind/vortex.F:1015` `interpR = val(quad,2)* fac+`; `wind/vortex.F:1016` `&         val(quad,3)* (1-fac)`) [10-12 전수 검증 정정]

해석: `case(3)`에서 QuadIr4의 1·2·3번 반경을 문서의 R34·R50·R64에 대응시킬 때, `else if (r > QuadIr4(quad,2)) then` 분기의 `(r-R50)/(R34-R50)`는 P34의 가중치다. (`wind/vortex.F:1004` `case(3)`; `wind/vortex.F:1005` `if (r > QuadIr4(quad,1)) then`; `wind/vortex.F:1007` `else if (r > QuadIr4(quad,2)) then`; `wind/vortex.F:1008` `fac = (r-QuadIr4(quad,2))/`; `wind/vortex.F:1009` `&               (QuadIr4(quad,1)-QuadIr4(quad,2))`; `wind/vortex.F:1010` `interpR = val(quad,1)* fac+`; `wind/vortex.F:1011` `&         val(quad,2)* (1-fac)`) [10-12 전수 검증 정정]

해석: `case(3)`의 첫 반경을 R34에 대응시킬 때 바깥 유지 조건은 r>R34다. (`wind/vortex.F:1004` `case(3)`; `wind/vortex.F:1005` `if (r > QuadIr4(quad,1)) then`; `wind/vortex.F:1006` `interpR = val(quad,1)`) [10-12 전수 검증 보완]

이 Fortran 보간은 rst 식 (20)·(22)의 가중치·괄호·IV 부등호와 구분한다. (`docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:545` `P(\theta,d)=\frac{P(quad(i),d)(90-\theta)^2+P(quad(i+1),d)\theta^2}{(90-\theta)^2+\theta^2} \quad (20)`; `docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:577` `\mathrm{II}. & R_{64}\le r<R_{50} &  f_{64}=(r-R_{64})/(R_{50}-R_{64}),f_{50}=(R_{50}-r)/(R_{50}-R_{64}), f_{34}=0 \\`; `docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:578` `\mathrm{III}. & R_{50}\le r<R_{34} &  f_{64}=0,f_{50}=(r-R_{50}/(R_{34}-R_{50})),f_{34}=(R_{34}-r/(R_{34}-R_{50})) \\`; `docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:579` `\mathrm{IV}. & r \le R_{34} & f_{64}=0,f_{50}=0,f_{34}=1`; `wind/vortex.F:973` `spInterp = ( temp1/delta_angle**2.d0`; `wind/vortex.F:1008` `fac = (r-QuadIr4(quad,2))/`; `wind/vortex.F:1013` `fac = (r-QuadIr4(quad,3))/`; `wind/vortex.F:1005` `if (r > QuadIr4(quad,1)) then`)

분면 방향 보간 `interpolateParameterPackRadial`(`Vortex.cpp:490-513`) — **역제곱 거리 가중**:

$$w_0 = \frac{1}{\theta^2}, \quad w_1 = \frac{1}{(\pi/2 - \theta)^2}, \quad x = \frac{w_0 x_0 + w_1 x_1}{w_0 + w_1}$$

isotach 방향 보간은 선형(`interpolateParameterPack`, `Vortex.cpp:464-480`).

### 6.4 풍속 벡터화·회전·이동 (`vortex/Vortex.cpp:179-214`)

순서:
1. `GahmWindSpeed`로 경도풍 산출.
2. `computeTranslationVelocityComponents` — 이동성분 (scaling = `min(1, ws/vmax_bl)`, `Vortex.cpp:245-259`). **단 현재 합산은 주석처리**(`uf += tsx; vf += tsy;`, `Vortex.cpp:206-208`).
3. 경계층 → 10m: `× topOfBoundaryLayerToTenMeter() = 0.9` (`Vortex.cpp:195`).
4. `decomposeWindVector` — 반접선(tangential) 분해, 남/북반구 부호 분기(`Vortex.cpp:223-235`).
5. `rotate_winds` — **friction(inflow) angle** 만큼 회전, 위도 부호 적용(`Vortex.cpp:202-204,548-557`).
6. 1분 → 10분 풍속: `× oneMinuteToTenMinuteWind() = 0.8928` (`Vortex.cpp:210-211`, `Constants.h:106`).

friction angle(`Vortex.cpp:521-538`): $r<r_m$이면 10°, $r_m \le r < 1.2 r_m$이면 $10° + 75°(r/r_m - 1)$, $r \ge 1.2 r_m$이면 25°. (Atmospheric.h:66-80의 Queensland inflow angle과 유사하나 별도 정의.)

---


([features 보고서 §5 H24 (484줄)<br>K66 (630줄)<br>C40 (689줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 최대풍속 반경 안쪽 유입각) 근거: `docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:423–427`의 식 (16)은 r<Rmax에서 상수 10도를 적는다. 실제 조건과 식은 [Fortran 유입각 정본](#gahm-inner-inflow)을 따른다. `wind/aswip.F:669`는 fang을 호출한다. `wind/aswip.F:706–709`는 활성 경로에서 회전된 이동 벡터를 제거한다. 결론: B 문서 오기. 현행 rst의 상수 10도는 반경에 비례하는 Fortran 구현과 다르다. 외부 C++의 비활성 주석 블록을 이 ASWIP 경로로 옮기지 않는다. [10-12 결론 검증 보완]
([features 보고서 §5 H28 (488·716줄)<br>H29 (489·717줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM 성분식의 각도·풍속 정규화) 근거: [10-12 결론 정정] H28·H29: 코드 각 θ=90°−문서 방위각 α를 대입하면 문서의 α+90°+β와 일반적으로 다르다. 같은 문서 식 (17)의 Wrf도 식 (18)·(19)에서 빠졌다. features 보고서 §5 H28·H29는 좌표 변환 미판정을 B 문서 오기로 좁힌다.<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:462 `V_r\cos(quad(i)+90+\beta)=V_{isot}\cos(\varepsilon)-\gamma {\mu}_T \quad (18)`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:479 ``where :math:`quad(i)` is the azimuth angle of the :math:`i-th` storm quadrant``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:480 ``(NE, SE, SW, NW at :math:`45^\circ, 135^\circ, 225^\circ, 315^\circ`,``<br>wind/aswip.F:677 `quadrantvecangles(i) = quadrantAngles(i)+`<br>wind/aswip.F:678 `&             (90.0d0+quadrotateAngle(i))*deg2rad`<br>wind/aswip.F:693 `U_Vr = Vr * cos(epsilonAngle(i)/rad2deg)`<br>wind/aswip.F:2960 `azimuth = 45.d0`<br>wind/aswip.F:2962 `quadrantAngles(i) = deg2rad*azimuth`<br>wind/aswip.F:2963 `azimuth = azimuth - 90.d0`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:473 `V_r\sin(quad(i)+90+\beta)=V_{isot}\sin(\varepsilon)-\gamma {\nu}_T \quad (19)`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:479 ``where :math:`quad(i)` is the azimuth angle of the :math:`i-th` storm quadrant``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:480 ``(NE, SE, SW, NW at :math:`45^\circ, 135^\circ, 225^\circ, 315^\circ`,``<br>wind/aswip.F:677 `quadrantvecangles(i) = quadrantAngles(i)+`<br>wind/aswip.F:678 `&             (90.0d0+quadrotateAngle(i))*deg2rad`<br>wind/aswip.F:694 `V_Vr = Vr * sin(epsilonAngle(i)/rad2deg)`<br>wind/aswip.F:2960 `azimuth = 45.d0`<br>wind/aswip.F:2962 `quadrantAngles(i) = deg2rad*azimuth`<br>wind/aswip.F:2963 `azimuth = azimuth - 90.d0`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:443 `& = \frac{\vert\overrightarrow{V_{isot}} - \gamma\overrightarrow{V_T}  \vert}{W_{rf}}`<br>wind/aswip.F:709 `&                  )/windReduction`<br>해석: 북기준 시계방향 방위각 α는 Cartesian 각 θ=90°−α로 바꿔야 한다. 코드는 θ+90°+β=180°−α+β를 쓴다. SE의 α=135°에서 코드는 45°+β이고 문서는 225°+β다. 또한 문서 식 (17)은 Vr=abs(Visot−γVT)/Wrf인데 (18)·(19)를 제곱합하면 Wrf가 없는 Vr=abs(Visot−γVT)가 된다. Wrf=0.9이므로 같은 문서 안에서도 모순된다. 결론: 문서 오기. GAHM rst의 식 (18)·(19)는 방위각 정의와 풍속 감소계수 표기를 수정해야 코드와 일치한다. [10-12 결론 검증 보완]
([features 보고서 §5 H33 (493줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 유입각의 반경 방향 연속성) 근거: [10-12 결론 정정] H33: 실행 없이도 fang의 두 접합점에서 좌우 값이 각각 10도·25도로 같음을 확인할 수 있다. features 보고서 §5 H33은 반경별 값의 연속성에 한정하여 F로 분류한다. 미분 연속성은 주장하지 않는다.<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:503 ``:math:`R_{max}` across all storm isotaches ensures that the cross-isobar``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:504 `frictional inflow angle changes smoothly along the radius according to (17).`<br>원하는 매끄러움의 실행 검증 없음.<br>wind/vortex.F:1148 `fang = 10.0d0 * r/rmx`<br>wind/vortex.F:1150 `fang = 10.0d0 + 75.0d0 * (r/rmx - 1.d0)`<br>wind/vortex.F:1152 `fang = 25.0d0`<br>src/wind.F:6053 `crmaxwTrue1(i) = spInterp(aziangle(i),1.d0,1)`<br>src/wind.F:6054 `!an artificial number 1.0 is chosen to ensure only`<br>src/wind.F:6055 `!rmax from the highest isotach is picked`<br>wind/vortex.F:883 `CALL rotate(u,v, fang(idist,irmx_true), cLat, uf,vf)`<br>해석: 이 값의 연속성 판정은 같은 양의 rmx를 사용하는 조건에 한정한다. 문서의 pseudo Rmax에 대응하는 코드 입력은 irmx_true다.  r/Rmax=1의 왼쪽 값 10r/Rmax와 오른쪽 값 10+75(r/Rmax−1)은 모두 10이다. r/Rmax=1.2에서는 두 인접 식이 모두 25다. 따라서 문서의 매끄러움을 값의 연속성으로 한정하면 정적으로 확인할 수 있다. 미분 연속성이나 전체 폭풍 합성의 성능까지 증명하지 않는다. 결론: 표기 차이. 같은 Rmax를 쓰는 fang 분기들은 Rmax와 1.2*Rmax에서 같은 유입각으로 연결된다. [10-12 결론 검증 보완]
([features 보고서 §5 H35 (495줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 각도 보간의 절대각·상대각) 근거: docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:532 `To begin, the relative location of a node to the storm center at given time`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:533 ``:math:`t` is calculated, specified by the azimuth angle :math:`\theta` and``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:534 ``distance :math:`d`. The angle :math:`\theta` places the node between two``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:535 ``adjacent quadrants :math:`i` and :math:`i+1`, where``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:536 ``:math:`quad(i) < \theta \le quad(i+1)`. For each storm parameter :math:`P` to be``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:545 `P(\theta,d)=\frac{P(quad(i),d)(90-\theta)^2+P(quad(i+1),d)\theta^2}{(90-\theta)^2+\theta^2} \quad (20)`<br>wind/vortex.F:973 `spInterp = ( temp1/delta_angle**2.d0`<br>wind/vortex.F:974 `&             + temp2/(90.0-delta_angle)**2.d0 )`<br>wind/vortex.F:975 `&             / ( 1.d0/delta_angle**2.d0`<br>wind/vortex.F:976 `&              + 1.d0/(90.d0-delta_angle)**2.d0 )`<br>해석: δ=θ−quad(i)로 두면 코드 역제곱 가중식은 [P_i(90−δ)²+P_(i+1)δ²]/[(90−δ)²+δ²]이다. 문서식은 같은 기호 θ를 절대 방위각으로 정의해 놓고 상대각 자리에 사용한다. θ=quad(i)에서 문서식은 일반적으로 P_i를 반환하지 않는다. 따라서 단순 동치 F가 아니라 기호 정의의 오기다. 결론: 문서 오기. GAHM의 각도 보간은 절대 방위각이 아니라 사분면 기준 상대각을 사용한다.
([features 보고서 §5 H38 (498줄)<br>H39 (499줄)<br>H40 (500줄)<br>C39 (688줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM 반경 가중치·바깥 영역) 근거: docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:575 `\begin{array}{lll}`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:577 `\mathrm{II}. & R_{64}\le r<R_{50} &  f_{64}=(r-R_{64})/(R_{50}-R_{64}),f_{50}=(R_{50}-r)/(R_{50}-R_{64}), f_{34}=0 \\`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:580 `\end{array} \quad (22)`<br>wind/vortex.F:1013 `fac = (r-QuadIr4(quad,3))/`<br>wind/vortex.F:1014 `&               (QuadIr4(quad,2)-QuadIr4(quad,3))`<br>wind/vortex.F:1015 `interpR = val(quad,2)* fac+`<br>wind/vortex.F:1016 `&         val(quad,3)* (1-fac)`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:575 `\begin{array}{lll}`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:578 `\mathrm{III}. & R_{50}\le r<R_{34} &  f_{64}=0,f_{50}=(r-R_{50}/(R_{34}-R_{50})),f_{34}=(R_{34}-r/(R_{34}-R_{50})) \\`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:580 `\end{array} \quad (22)`<br>wind/vortex.F:1008 `fac = (r-QuadIr4(quad,2))/`<br>wind/vortex.F:1009 `&               (QuadIr4(quad,1)-QuadIr4(quad,2))`<br>wind/vortex.F:1010 `interpR = val(quad,1)* fac+`<br>wind/vortex.F:1011 `&         val(quad,2)* (1-fac)`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:575 `\begin{array}{lll}`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:579 `\mathrm{IV}. & r \le R_{34} & f_{64}=0,f_{50}=0,f_{34}=1`<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:580 `\end{array} \quad (22)`<br>wind/vortex.F:1005 `if (r > QuadIr4(quad,1)) then`<br>wind/vortex.F:1006 `interpR = val(quad,1)`<br>해석: R64<=r<R50에서 P50의 가중치는 (r−R64)/(R50−R64)이다. R50<=r<R34에서 P34의 가중치는 (r−R50)/(R34−R50)이다. rst는 두 구간의 가중치를 뒤집고 III의 괄호를 잘못 적었다. IV의 r<=R34는 I–III와 겹치지만 코드는 r>R34에서 P34를 유지한다. 끝점 대입으로 문서 내부 모순을 확인한다. C39의 외부 C++ 보간 설명을 틀렸다고 판정하지 않는다. 이 B 판정은 현행 rst의 Fortran 반경 보간식에 적용한다. 결론: 문서 오기. 현재 Fortran GAHM의 반경 보간 가중치는 인접 isotach 값을 각 끝점에서 보존한다.
([features 보고서 §5 K63 (627줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM 방위 보간의 경계 처리) 결론: C 문서 누락. 1° 미만·89° 초과에서 인접 사분면 값을 고르는 근거는 [방위 보간 정본](#gahm-angle-interp)에 모았다. [10-12 결론 검증 보완]
([features 보고서 §5 K64 (628줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM isotach 수별 반경 보간) 근거: wind/vortex.F:990 `select case(total_Isot)`<br>wind/vortex.F:991 `case(1)`<br>wind/vortex.F:992 `interpR = val(quad,maxloc(QuadFlag4(quad,:),1))`<br>wind/vortex.F:993 `case(2)`<br>wind/vortex.F:1004 `case(3)`<br>wind/vortex.F:1020 `case(4)`<br>해석: 대조 문서는 개수별 분기와 단일 isotach의 직접 선택을 모두 적지 않았다. 결론: 문서 누락. GAHM은 isotach 개수 1·2·3·4에 따라 별도 반경 보간 분기를 선택한다.

## 7. Fortran 바인딩 / ADCIRC 결합 (`fortran/`)

`gahm_fortran.cpp`: `gahm_instance`가 AtcfFile·Preprocessor·Vortex를 `unique_ptr`로 소유, 생성자에서 read→solve→vortex 구성(`fortran/gahm_fortran.cpp:43-62`). 인스턴스는 `std::vector`(또는 map)로 관리, 정수 핸들을 Fortran에 반환(`gahm_fortran.cpp:64-101`).

C API(`extern "C"`, `gahm_fortran.cpp:71-83`):
- `gahm_create_ftn(filename, size, x, y, quiet)` → 핸들.
- `gahm_get_ftn(id, y,m,d,h,mi,s, size, u, v, p)` → 해당 날짜 vortex 해를 u/v/p 배열에 채움(`gahm_fortran.cpp:111-130`).
- `gahm_get_serial_date_ftn`, `gahm_date_add_ftn` — 날짜 유틸.

Fortran 측(`fortran/gahm.F90`): `gahm_t`(핸들 래퍼)·`date_t` 파생형, `iso_c_binding` interface로 위 C 함수 바인딩(`gahm.F90:21-89`). `gahm_initialize`가 파일·점군으로 인스턴스 생성, `gahm_get`이 (u,v,p) 조회(`gahm.F90:141-165`). 출력 단위: u,v는 m/s(10분 풍), p는 mb(§6.2의 /100).

NWS=20은 `NWS20GET`을 호출한다. (`src/wind.F:1502` `IF(NWS.EQ.20) THEN`; `src/wind.F:1503` `CALL NWS20GET(wvnx2, wvny2, prn2, timeloc)`)

결합 NWS=30도 `NWS20GET`을 호출한다. (`src/wind.F:1553` `case(30)`; `src/wind.F:1554` `CALL NWS20GET(vortexWVNX2,vortexWVNY2,vortexPRN2,timeloc)`)

NWS=13은 OWI NetCDF reader를 사용한다. (`src/wind.F:2045` `CALL NWS13INIT(0.D0,W)`; `src/wind.F:2046` `CALL NWS13GET(WTIME1,WVNX1,WVNY1,PRN1,`; `docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:208` `*&owiWindNetcdf* fort.15 namelist with all inputs quoted as strings`; `docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:214` `-  *NWS13File*: optional file name for netCDF file ( *fort.22.nc* default )`)

ADCIRC NWS 외력 패밀리는 [[adcirc-storm-surge-nws-families]]를 참조한다.

---


([fort15 보고서 §5 C20 (L858)](../../../_staging/recovery/compare/ADCIRC-fort15-vs-code.md#5-차이-결론); 항목: NWS13과 GAHM) 근거: 확인한 원문: `docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:10` ` Oceanweather Inc. (OWI) NetCDF Meteorological Input Files `<br>`src/wind.F:1502` ` IF(NWS.EQ.20) THEN `<br>`src/wind.F:1503` ` CALL NWS20GET(wvnx2, wvny2, prn2, timeloc) `<br>`src/wind.F:1553` ` case(30) `<br>`src/wind.F:1554` ` CALL NWS20GET(vortexWVNX2,vortexWVNY2,vortexPRN2,timeloc) `<br>`src/wind.F:2045` ` CALL NWS13INIT(0.D0,W) `<br>`src/wind.F:2046` ` CALL NWS13GET(WTIME1,WVNX1,WVNY1,PRN1, `<br>해석: C20 노트의 NWS13=GAHM 설명은 같은 판의 NWS13 NetCDF 문서 및 NWS20GET 호출 선택과 모순된다. 결론: 문서 오기. GAHM은 NWS20 또는 그 결합 NWS30에서 사용한다.
([features 보고서 §5 H02 (462줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM 주변 기압 기호) 근거: docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:49 ``where :math:`P_c` is the central pressure, :math:`P_c` is the ambient pressure``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:50 ``(theoretically at infinite radius), :math:`P(r)` is the pressure at radius``<br>wind/vortex.F:203 `Pn = pinf`<br>wind/vortex.F:204 `Pc = p0`<br>해석: 같은 문장이 두 압력을 모두 Pc라고 정의한다. 소스의 Pn=pinf와 Pc=p0가 구별을 유지한다. 결론: 문서 오기. GAHM의 주변 기압은 Pn이고 중심 기압은 Pc다.
([features 보고서 §5 H07 (467줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: Holland B의 경험 범위) 근거: docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:125 ``drop. It was also reasoned by Holland that a plausible range of :math:`B` would``<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:126 `be between 1 and 2.5 for realistic hurricanes. Substituting (4) and (5) back`<br>GAHM 계수의 1–2.5 강제 제한을 이 경로에서 찾지 못함.<br>wind/vortex.F:188 `B = MAX( MIN(B,2.5d0), 1.0d0) ! limit B to range 1.0->2.5`<br>wind/vortex.F:217 `! Jie 2013.01`<br>wind/vortex.F:218 `! B = MAX( MIN(B,2.5d0), 1.0d0) ! limit B to range 1.0->2.5`<br>해석: 문서는 Holland의 plausible range를 소개한다. newVortex:188은 제한을 수행하지만 newVortexFull:218은 같은 줄을 주석 처리했다. 그 바로 앞에 Jie 2013.01 표기가 있다. GAHM에 옛 Holland 상한을 이식하지 않는다. 결론: 판 차이. GAHM의 newVortexFull은 옛 Holland 경로의 B=1..2.5 제한을 적용하지 않는다.
([features 보고서 §5 H10 (470줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: Rossby 수의 독립 변수) 근거: [10-12 결론 정정] H10: 독립 R_o 변수 부재는 계산 부재가 아니다. vortex.F:391–392를 Ro=V/(Rf)로 정리하면 Phi=1+1/[B(Ro+1)]을 얻으므로 features 보고서 §5 H10은 F로 분류한다.<br>docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:167 `R_o = \frac{Nonlinear Acceleration}{Coriolis force} \approx \frac{V_{max}^2/R_{max}}{V_{max}f} = \frac{V_{max}}{R_{max}f} \quad (8)`<br>R_o를 이 이름으로 계산·저장하는 줄을 찾지 못함.<br>wind/vortex.F:391 `Phi_new = 1+Vmax*kt2ms*root*nm2m*corio/`<br>wind/vortex.F:392 `&       (B*((Vmax*kt2ms)**2+Vmax*kt2ms*root*nm2m*corio))`<br>해석: V=Vmax*kt2ms, R=root*nm2m, f=corio라 둔다. 아래 등가식은 V, Rf, B, V+Rf가 모두 0이 아닌 조건에 한정한다. 이 조건에서 코드의 VRf/(V²+VRf)=1/(V/(Rf)+1)=1/(Ro+1)이다. 따라서 Phi=1+1/[B(Ro+1)]이다. Rf=0에서는 이 Ro 정의로 나눌 수 없으므로 같은 변형을 적용하지 않는다. Ro라는 변수 저장은 이 식의 필요조건이 아니다. 결론: 표기 차이. GAHM은 Rossby 수의 역비를 Vmax·Rmax·Coriolis의 조합으로 계산한다. [10-12 결론 검증 보완]
([features 보고서 §5 K60 (624줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM 남반구 처리) 근거: wind/vortex.F:210 `corio = ABS(2.0d0 * omega * SIN(deg2rad*cLat))`<br>wind/vortex.F:874 `if(cLat.lt.0.d0) then ! SH`<br>wind/vortex.F:875 `u =  speed * COS(deg2rad*iangle)`<br>wind/vortex.F:876 `v = -speed * SIN(deg2rad*iangle)`<br>wind/vortex.F:878 `u = -speed * COS(deg2rad*iangle)`<br>wind/vortex.F:879 `v =  speed * SIN(deg2rad*iangle)`<br>src/wind.F:6111 `corio = ABS(2.0d0 * omega * SIN(deg2rad*cLat))`<br>해석: 대조 문서는 Coriolis 크기와 회전 방향을 분리한 구현을 적지 않았다. 결론: 문서 누락. GAHM은 Coriolis 크기의 절댓값과 남반구 회전풍의 별도 부호 전환을 사용한다.
<a id="gahm-output-limits"></a>([features 보고서 §5 K67 (631줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM 출력의 범위 제한) 근거: src/wind.F:6207 `press(i) = max(0.85d5,min(1.1d5,press(i)))  ! Typhoon Tip 870 hPa ... 12-oct-1979`<br>src/wind.F:6208 `wvnx(i)  = max(-200.d0,min(200.d0,wvnx(i)))`<br>src/wind.F:6209 `wvny(i)  = max(-200.d0,min(200.d0,wvny(i)))`<br>src/wind.F:6216 `press(i) = press(i) / RhoWatG`<br>해석: 문서는 이 압력 제한과 풍속 각 성분의 -200–200 제한을 적지 않았다. 결론: 문서 누락. NWS=20은 기압을 85000–110000 Pa로 제한한 뒤 RhoWatG로 나누어 수두로 변환한다. [10-12 결론 검증 보완]
([features 보고서 §5 K68 (632줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: GAHM 외곽 cutoff의 비활성 상태) 근거: wind/vortex.F:906 `!if ( dist.gt.401.d0 ) then`<br>wind/vortex.F:907 `!   u = 0.0d0`<br>wind/vortex.F:908 `!   v = 0.0d0`<br>wind/vortex.F:909 `!   p = mb2pa * Pn`<br>wind/vortex.F:910 `!endif`<br>해석: 대조 문서는 해당 블록의 비활성 상태를 적지 않았다. 주석의 거리 제한을 실제 적용 조건으로 세지 않는다. 결론: 문서 누락. v56.2.1의 401 nm 외곽 cutoff 블록은 주석 처리되어 실행되지 않는다.

## 8. OWI 격자바람 출력 (`output/OwiOutput`)

`OwiOutput`(`output/OwiOutput.h:44-74`): `OutputFile` 상속, 시작/종료 날짜·파일명·`WindGrid`로 구성. 별도 압력파일(`m_pressure_file`)·바람파일(`m_wind_file`) 생성, `writeHeader`/`generateRecordHeader`로 OWI 포맷 헤더 작성 후 `VortexSolution`을 레코드로 기록(`OwiOutput.h:56-73`). → ADCIRC NWS12(OWI ASCII) 입력 생성 경로. (구현 본문 `OwiOutput.cpp`은 헤더 시그니처 기준; 상세 포맷은 ⚠ 미확인 — 필요시 cpp 추가 검토.)

---

## 9. 핵심 물리 상수 (`physical/Constants.h`)

| 상수 | 값 | line |
|---|---|---|
| 배경기압 | 1013.0 mb | `Constants.h:68` |
| 경계층→10m | 0.9 | `Constants.h:74` |
| 10m→경계층 | 1/0.9 | `Constants.h:80-82` |
| $\rho_{air}$ | 1.293 kg/m³ | `Constants.h:88` |
| $g$ | 9.80665 | `Constants.h:94` |
| 1분→10분 풍 | 0.8928 | `Constants.h:106` |
| 지구 자전 $\omega$ | 7.292115e-5 rad/s | `Earth.h:38` |
| coriolis | $2\omega\sin(\mathrm{lat})$ | `Earth.h:44-46` |

---

## 10. 요점 정리

1. **비대칭(asymmetric)의 근원**: 전처리(`Preprocessor::solve`)가 **4분면 각각** 독립으로 GahmSolver를 돌려 분면별 Rmax·B를 확보(§5.5). vortex 합성은 분면·isotach·시간을 보간(§6.3).
2. **GAHM = Holland + $\phi$/$b_g$ 보정**: 표준 Holland B를 Rossby·$\phi$로 수정($b_g$), 경도풍에 $e^{-\phi(\cdot)}$ 도입(§2). Rmax↔B 교대 수렴(§3.1).
3. **Newton-Raphson**(boost) 내부에서 Rmax, fixed-point 외부에서 B/$\phi$ (§3).
4. **풍속 변환 체인**: 경도풍 → ×0.9(10m) → 분해 → inflow 회전 → ×0.8928(10분). 이동속도 합산은 현재 **주석처리**(§6.4) — 검토 시 주의.
5. **입력 = ATCF best-track**, 결측 분면은 이웃/평균/rmax 규칙으로 채움(§5.2). 출력 = Fortran (u,v,p) 또는 OWI 격자(§7-8).
