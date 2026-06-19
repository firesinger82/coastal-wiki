---
title: "GAHM 비대칭 Holland 바람 모델 (gahm 라이브러리)"
model: ADCIRC
component: Parametric vortex wind/pressure forcing (GAHM, Generalized Asymmetric Holland Model)
canonical_source: self
citation_status: verified
verification_method: "소스 직접 read (gahm/src/). gahm/GahmEquations.{h,cpp}·GahmSolver.cpp·GahmRadiusSolver.cpp·GahmRadiusSolverPrivate.cpp / vortex/Vortex.cpp / atcf/AtcfSnap.cpp·AtcfFile.cpp·AtcfIsotach.h·AtcfQuadrant.h·StormTranslation.h / preprocessor/Preprocessor.cpp / physical/Atmospheric.h·Constants.h·Earth.h / fortran/gahm.F90·gahm_fortran.cpp / output/OwiOutput.h"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ADCIRC/README.md
  - models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md
  - models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md
---

# GAHM 비대칭 Holland 바람 모델 (gahm 라이브러리)

> 요약(`models/ADCIRC/raw/source_code/gahm/src/`). GAHM = **Generalized Asymmetric Holland Model**. ATCF best-track 4분면 isotach를 입력받아 폭풍별 **분면-개별 GAHM Holland B·radius-to-max-wind**를 Newton-Raphson으로 풀고(`gahm/`+`preprocessor/`), 임의 점군에서 경도풍 합성·기압장을 만드는(`vortex/`) C++ 라이브러리. Fortran 바인딩(`fortran/gahm.F90`)으로 ADCIRC와 결합되며 OWI 격자바람(NWS12/13)도 출력 가능(`output/OwiOutput`). Author: Zach Cobell (The Water Institute), GPLv3, ADCIRC Development Group (예: `gahm/GahmSolver.cpp:1-19`).

ADCIRC NWS 외력 패밀리 전반은 [[adcirc-storm-surge-nws-families]], met-forcing 적용 맥락은 [[adcirc-met-forcing-implementation]] 참조. 본 노트는 gahm 라이브러리의 **방정식·솔버·합성 알고리즘** 자체를 다룬다.

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

첫 snap은 다음 snap으로, 그 외는 이전 snap과의 차로 forward/backward 차분(`Preprocessor.cpp:206-222`).

### 5.4 경계층 풍속 (`Preprocessor.cpp:317-339`)

- snap vmax: 10m → 경계층 = `× tenMeterToTopOfBoundaryLayer()` = `1/0.9 ≈ 1.111` (`Preprocessor.cpp:319-320`, `Constants.h:74-82`), 이후 이동속도 제거.
- isotach 분면 풍속: `removeTranslationVelocity`로 이동성분 차감(scaling = `min(1, ws/vmax)`, `Preprocessor.cpp:307-312`) 후 경계층 변환(`Preprocessor.cpp:325-335`).
- **참고**: 분면별 회전 기반 제거(`removeTranslationVelocity(.., quadrant, ..)`)는 현재 본문이 주석처리되고 `wind_speed`를 그대로 반환 — `// TODO`/실험 상태(`Preprocessor.cpp:271-297`).

### 5.5 분면별 솔버 구동 (`Preprocessor.cpp:68-102`)

`prepareAtcfData()` 선행 필수(미처리 시 runtime_error, `Preprocessor.cpp:69-74`). 모든 snap × isotach × **4분면** 각각:
- `vmax ≤ isotach_speed`면 `vmax = isotach_speed + 1.0`로 넛지(`Preprocessor.cpp:90-91`, "// TODO: Confirm with Rick").
- `GahmSolver(isotach_radius, isotach_speed, vmax, p_min, p_back, latitude).solve()` → 분면에 `rmax`, `gahm_b` 저장(`Preprocessor.cpp:94-98`).

즉 **각 분면이 독립적인 Rmax·B**를 가져 비대칭(asymmetric) 구조가 형성된다.

---

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

## 7. Fortran 바인딩 / ADCIRC 결합 (`fortran/`)

`gahm_fortran.cpp`: `gahm_instance`가 AtcfFile·Preprocessor·Vortex를 `unique_ptr`로 소유, 생성자에서 read→solve→vortex 구성(`fortran/gahm_fortran.cpp:43-62`). 인스턴스는 `std::vector`(또는 map)로 관리, 정수 핸들을 Fortran에 반환(`gahm_fortran.cpp:64-101`).

C API(`extern "C"`, `gahm_fortran.cpp:71-83`):
- `gahm_create_ftn(filename, size, x, y, quiet)` → 핸들.
- `gahm_get_ftn(id, y,m,d,h,mi,s, size, u, v, p)` → 해당 날짜 vortex 해를 u/v/p 배열에 채움(`gahm_fortran.cpp:111-130`).
- `gahm_get_serial_date_ftn`, `gahm_date_add_ftn` — 날짜 유틸.

Fortran 측(`fortran/gahm.F90`): `gahm_t`(핸들 래퍼)·`date_t` 파생형, `iso_c_binding` interface로 위 C 함수 바인딩(`gahm.F90:21-89`). `gahm_initialize`가 파일·점군으로 인스턴스 생성, `gahm_get`이 (u,v,p) 조회(`gahm.F90:141-165`). 출력 단위: u,v는 m/s(10분 풍), p는 mb(§6.2의 /100).

ADCIRC fort.15 NWS 외력 패밀리에서 GAHM 호출(NWS13 등) 맥락은 [[adcirc-storm-surge-nws-families]] 참조.

---

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
