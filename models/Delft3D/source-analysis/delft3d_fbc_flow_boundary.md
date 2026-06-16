---
title: "Delft3D FBC 흐름경계조건 도구 — D-Feedback Control (구 RTC-Tools): timeseries·rules·triggers·schematization"
model: Delft3D
component: fbc/FBCTools
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/fbc/packages/FBCTools/src/...). element/rule/trigger 기반 클래스(schematization/element.h, rules/rule.h, triggers/trigger.h), 시뮬레이터 실행순서(rtcToolsSimulator.cpp), PID positional 알고리즘(rules/pidControllerPositional.cpp), 조건 평가(triggers/condition.cpp + utilities/utils.h relationalOperator), lookup table 보간(utilities/lookupTableConverter.cpp), timeseries 자료구조(timeseries/timeSeriesBasics.h), BMI 인터페이스(bmi.h), dataBinding XSD 출처(dataBinding/rtcToolsConfig.hxx) 를 file:line 인용. xerces는 외부 라이브러리로 존재만 확인(timeseries/piTimeSeriesSAX2Handler.h)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/source-analysis/delft3d_dimr_coupling.md
  - models/Delft3D/README.md
---

# Delft3D FBC 흐름경계조건 도구 (D-Feedback Control / 구 RTC-Tools)

> 실시간 피드백 제어(real-time control) 라이브러리. 시계열을 입력받아 rules·triggers 로 구성된 schematization 을 매 타임스텝 풀어, hydraulic model(D-Flow FM/flow2d3d)의 구조물·경계 setting 을 산출한다. 경로: `src/engines_gpl/fbc/packages/FBCTools/src/`

## 0. 정체성 — FBC = D-Feedback Control = 구 RTC-Tools

- `ReadMe.txt:1-11`: `"D-Feedback Control" Project Overview ... It used to be RTC.` — FBC 는 RTC-Tools 의 리네이밍.
- 빌드 산출물 제품명은 여전히 `FBC-Tools` 이며 버전 `OSS_Version "1.6.1"` (`fbc/version/fbc_version.h:15,17`: `#define OSS_Version "1.6.1"`, `#define PRODUCT_NAME "FBC-Tools"`).
- 소스 전체가 `namespace rtctools` 를 그대로 사용 (`schematization/element.h:33` `namespace rtctools`). 셸 런처도 `RTCTools.sh.in` / `FBCTools.sh.in` 두 이름 공존.
- release notes 는 `RTC Tools 1.4.x` 표제 유지 (`release_notes.txt:6` `RTC Tools 1.4.2 Release Notes`).
- 의존성: Boost(`ReadMe.txt:17-18`), CodeSynthesis XSD + Apache Xerces-C(XML 파싱, 아래 §6).

> "흐름경계조건 도구"라는 배정 주제와 관련하여: FBC 는 흐름경계값 자체를 정의하는 것이 아니라, 시뮬레이션 중 흐름·수위 관측을 받아 게이트/펌프/위어/경계 setting 을 **제어**해 되돌려주는 컨트롤러다. flow2d3d 측의 흐름경계 보정 자체는 별개로 `flow2d3d/packages/flow2d3d_io/src/input/fbcorr.f90` 에 존재(본 노트 범위 밖, 존재만 언급).

## 1. 클래스 계층 — element / rule / trigger / component

모든 모델 요소의 추상 기반은 `element` (`schematization/element.h:41`).

```
element (추상)
 ├─ rule       (rules/rule.h:38)        — 제어 설정값 산출
 ├─ trigger    (triggers/trigger.h:37)  — on/off 활성화 조건
 └─ component  (components/component.h:37) — 수리 시스템 구성요소
```

`element` 의 핵심 인터페이스 (`element.h:86-117`):

| 멤버 | 역할 | 인용 |
|---|---|---|
| `id`, `name` | 고유 식별자·이름 | `element.h:47,51` |
| `active`, `isActiveOutPosition=-1` | 활성 상태 + 상태 출력 컬럼 인덱스 | `element.h:57,62` |
| `virtual void activate()=0 / deactivate()=0` | 활성/비활성 (rule 에 의미) | `element.h:86,90` |
| `virtual void solve(stateOld, stateNew, t, dt)=0` | 정방향 1 타임스텝 전진 | `element.h:104` |
| `virtual void solveDer(...)=0` | adjoint 역방향(시간 거꾸로) | `element.h:116` |

- `solve` 시그니처 주석: `stateOld` = 이전 시스템 상태(read only), `stateNew` = 신규 상태, `t` = 1970 이후 밀리초, `dt` = 타임스텝[s] (`element.h:93-103`). 즉 **상태벡터(state vector) 기반 in-place 풀이** — 모든 시계열이 하나의 평탄한 `double*` 상태배열의 컬럼 인덱스로 참조된다.
- `rule` 은 추가로 `stateTransfer()` 와 `getIYOut()` (출력 시계열 인덱스, 기본 -1) 보유 (`rules/rule.h:48-50`).

## 2. 시뮬레이터 실행 순서 (핵심) — rtcToolsSimulator

매 타임스텝 `rtcToolsSimulator::simulate(int iStep)` (`rtcToolsSimulator.cpp:69`) 의 실행 순서가 FBC 의 의미론을 규정한다:

1. **시간/상태 준비**: `dt = getDT(iStep)/1000.0` (ms→s), `stateOld = getState(iStep-1)`, `stateNew = getState(iStep)` (`rtcToolsSimulator.cpp:76-81`).
2. **rules state transfer**: 모든 rule 의 `stateTransfer()` 호출 — 상태 이월 (`rtcToolsSimulator.cpp:88-90`).
3. **triggers**: 먼저 모든 trigger 가 `deactivate()` → 그다음 `solve()`.
   - 주석 그대로: `// this deactivates all referenced rules in the triggers` / `// note a rules is not deactivated if NOT referenced in any trigger` (`rtcToolsSimulator.cpp:117-119`). 즉 트리거가 참조하는 rule 만 비활성화 대상이고, 어떤 트리거에도 참조되지 않은 rule 은 항상 활성.
4. **rules solve**: `isActive()` 인 rule 만 `solve()`. 동일 출력 인덱스(`getIYOut()`)에 두 rule 이 동시에 쓰려 하면 런타임 에러(이중 제어 충돌 검출): `... is going to enable ... when it is already enabled in ...` (`rtcToolsSimulator.cpp:146-169`). `getIYOut()==-1` (제어점 없는 unitDelay 등)은 충돌검사에서 제외 (`rtcToolsSimulator.cpp:163-167`).
5. **components solve**: 모든 component `solve()` (`rtcToolsSimulator.cpp:192-194`).
6. 마지막 스텝 제외 `incrementTimeStep()` (`rtcToolsSimulator.cpp:214-216`).

→ **정해진 순서: state transfer → trigger(deactivate→solve) → rule(active 만 solve) → component.** 따라서 트리거는 rule 보다 먼저 평가되어 어떤 rule 이 이번 스텝에 작동할지를 결정한다.

adjoint 모드 `evaluateGradient` 는 component 역순 → trigger 정방향(rule 활성화 재현 위해) → rule 역순으로 풀이 (`rtcToolsSimulator.cpp:232-267`).

## 3. Rules 라이브러리 (제어 규칙)

`schematization/rules/` 의 주요 rule. 모두 `rule` 상속, `solveDer` 는 대개 미구현(`runtime_error`).

### 3.1 PID 컨트롤러 (4 변종)
`pidController*.{cpp,h}` — positional / velocity / Sobek2 / 공통.

`pidControllerPositional::solve` (`rules/pidControllerPositional.cpp:91-147`) 가 표준 위치형 PID:

- 오차 산출: setpoint 인덱스 있으면 `e_n = stateNew[iSPIn] - stateOld[iXIn]`, 없으면 상수 setpoint `e_n = SPIn - stateOld[iXIn]` (`pidControllerPositional.cpp:103-112`).
- 적분 누적: `sum_integrator += dt * e_n` (`pidControllerPositional.cpp:117`).
- 출력: $u_n = k_p e_n + k_i \sum + k_d (e_n - e_{n-1})/\Delta t$ (`pidControllerPositional.cpp:118`).
- **rate limit**: $|u_n - u_{n-1}| \le$ `settingMaxSpeed * dt` 로 클리핑 (`pidControllerPositional.cpp:121-130`).
- **레벨 limit**: `settingMin ≤ u_n ≤ settingMax` (`pidControllerPositional.cpp:133-142`).
- 초기 출력 NaN 이면 `(settingMin+settingMax)/2` 로 시작 (`pidControllerPositional.cpp:97-100`).
- NaN 보호: 자체 `#define isnan(a) ((a)!=(a))` (`pidControllerPositional.cpp:29`).
- 헤더 주석: positional 은 하위호환용이며 향후 제거 예정 — `This method is available for backwards compatibility with Positional. It is obsolete and will be removed in a future release.` (`pidControllerPositional.cpp:33-36`).

### 3.2 기타 rules

| rule | solve 동작 | 인용 |
|---|---|---|
| `constantRule` | `stateNew[yOut] = constant` (상수 setting) | `rules/constantRule.cpp:36` |
| `limiterRule` | 변화율 제한: `xNew-xOld > +threshold` 면 `xOld+threshold` 로, `< -threshold` 면 `xOld-threshold` 로 클립 (in-place `stateNew[iInput.x]`) | `rules/limiterRule.cpp:52-53` |
| `deadBandValueRule` | 데드밴드 내 변화 무시 후 `stateNew[yIn]` 갱신 | `rules/deadBandValueRule.cpp:40-48` |
| `intervalController` | setpoint 대비 below/above 두 설정 전환 + maxSpeed/maxStep 율 제한, status 출력 | `rules/intervalController.cpp:104-128` |
| `relativeTimeController` | 활성 이후 경과시간 추적(`stateNew[iTimeActiveOut]=stateOld[...]+dt`), 시간기반 setting | `rules/relativeTimeController.cpp:89,243-244` |
| `absoluteTimeController` | 절대시각 기반 제어 | `rules/absoluteTimeController.cpp` (존재) |
| `dateLookupTableRule` | 날짜→값 테이블 룩업 (계절 운영 등), `dateLookupTableConverter` 사용 | `rules/dateLookupTableRule.cpp` + `utilities/dateLookupTableConverter.{cpp,h}` |
| `guideBandRule` | 가이드밴드(상·하한 곡선) 제어 | `rules/guideBandRule.cpp` (존재) |

`intervalController` 율 제한 식 (`rules/intervalController.cpp:116-124`):
- maxSpeed 있으면 `yNew = clamp(yNew, yOld - maxSpeed*dt, yOld + maxSpeed*dt)`,
- 없고 maxStep 있으면 `yNew = clamp(yNew, yOld - maxStep, yOld + maxStep)`.
(`settingMaxSpeed==settingMaxSpeed` 는 NaN 아님 검사 관용구.)

### 3.3 lookupTable / lookup2DTable (룩업 기반 제어)

`lookupTable` 은 흥미롭게 `component`, `rule`, `trigger` 를 **다중상속** (`schematization/lookupTable.h:45`) — 어느 역할로든 쓰일 수 있는 만능 변환 요소.

`lookupTable::solve` (`schematization/lookupTable.cpp:44-57`):
- `y = conv->convert(stateOld[iXIn])` — 입력 시계열을 converter 로 변환.
- `iYIn > -1` 이면 optional 입력으로 룩업 출력을 **오버룰** (유효시) (`lookupTable.cpp:48-50`, 헤더 주석 `lookupTable.h:57-62`: optional 시계열이 valid data 면 룩업 출력을 덮어씀).
- `stateNew[iYOut] = y`.

2D 버전 `lookup2DTable.{cpp,h}` 존재(두 입력→출력).

## 4. Triggers 라이브러리 (활성화 조건)

`schematization/triggers/`. 기반 `trigger` (`triggers/trigger.h:37-71`) 는 true/false 분기 자식요소 배열을 가짐:
- `trueComponent[]`, `falseComponent[]` (`trigger.h:41-43`): 조건 참/거짓에 따라 활성화할 하위 요소들.
- 출력: `iYOut`(상태), `iTimeTrueOut`/`iTimeFalseOut`(참·거짓 지속시간) (`trigger.h:45-47`).
- `evaluateTimes()`, `evaluateSubtriggers()` (`trigger.h:68-69`) 로 시간 누적 + 하위트리거 재귀.

### 4.1 condition (관계 비교) — 모든 표준트리거의 핵심
`condition::evaluate` (`triggers/condition.cpp:42-119`):
- 두 피연산자 x1,x2 각각 상수(`x1Value`) 또는 시계열(`iX1In>-1` 이면 `stateOld[iX1In]`) (`condition.cpp:50-57`).
- 관계연산자 enum `relationalOperator { GREATER, GREATEREQUAL, EQUAL, UNEQUAL, LESSEQUAL, LESS }` (`utilities/utils.h:40-48`).
- 두 값 모두 유효(non-NaN)일 때만 비교, 결과 1.0/0.0 (`condition.cpp:60-104`).
- 단, `UNEQUAL` 은 한쪽만 NaN 이어도 평가 (`condition.cpp:107-116`). 그 외 NaN 입력은 NaN 반환.

### 4.2 standardTrigger
`standardTrigger::solve` (`triggers/standardTrigger.cpp:41-63`):
- 기본값(`yDefaultPresent`) 설정 후 `con.evaluate()` 결과가 유효하면 덮어씀 (`standardTrigger.cpp:44-55`).
- `stateNew[iYOut]=yNew` (기본값 없고 조건 평가 불가 시 NaN) (`standardTrigger.cpp:58`).
- 이어 `evaluateTimes` + `evaluateSubtriggers` (`standardTrigger.cpp:61-62`).

### 4.3 setTrigger (논리 결합)
`setTrigger::solve` (`triggers/setTrigger.cpp:48-`): 두 하위 트리거 t1,t2 를 `logicalOperator { AND, OR, XOR }` (`utils.h:49-54`) 로 결합. OR 는 한쪽만 유효해도 평가, AND/XOR 는 양쪽 모두 필요 (`setTrigger.cpp:84-96`).

### 4.4 polygonTrigger (2D 영역 조건)
`polygonTrigger::solve` (`triggers/polygonTrigger.cpp:40-`): 입력 (x1,x2) 가 어느 polygon 에 포함되면(`polygons[i].contains(x1,x2)`) 그 polygon 의 값을 출력 (`polygonTrigger.cpp:49-53`). 운영 다이어그램(예: 수위-유량 평면 영역별 운영) 표현. `polygon.{cpp,h}` 가 contains/value 보유.

### 4.5 기타 trigger
- `deadbandTrigger` / `deadbandTimeTrigger` — 채터링 방지용 데드밴드/지속시간 (`triggers/deadbandTrigger.cpp`, `deadbandTimeTrigger.cpp`).
- `ruleReferenceTrigger` — rule 의 활성상태를 트리거 입력으로 참조 (`triggers/ruleReferenceTrigger.cpp`).

## 5. timeseries 서브시스템

`timeseries/` 는 모든 입력·상태·출력 시계열의 컨테이너.

### 5.1 timeSeriesBasics (자료구조 골격)
`timeSeriesBasics` (`timeseries/timeSeriesBasics.h:49-84`):
- `nTimeStep`, `time`(밀리초 long long 벡터), `nSeries`, `seriesID` (`timeSeriesBasics.h:52-55`).
- `seriesValidation` + enum `validationEnum { VALIDATION_NO, _STATE, _UPDATE, _UPDATE_EXCEPT_STATE, _FORECAST, _FORECAST_EXCEPT_T0, _ALL, _ALL_EXCEPT_STATE }` (`timeSeriesBasics.h:37-47`) — 시계열별 검증 정책.
- `scalarIDMap`(string→int 컬럼), `vectorIDMap`(string→pair) (`timeSeriesBasics.h:57-58`) — **ID 문자열 ↔ 상태벡터 컬럼 인덱스** 매핑. §2 의 모든 rule/trigger 의 `iXIn`/`iYOut` 정수 인덱스가 여기서 해석된다.
- 시간 헬퍼: `getStartTime/getEndTime/getDT(tIndex)` (`timeSeriesBasics.h:68-73`).

### 5.2 인터페이스 계층
- `timeSeriesInterface : timeSeriesBasics` (`timeseries/timeSeriesInterface.h:34`) — 순수가상 `getValue(ens,t,series)` / `setValue(...)` / `getNEnsemble()` (`timeSeriesInterface.h:42-44`). 앙상블(`ensembleIndx`) 1급 지원 → 앙상블 예보 입력.
- 구현체: `timeSeriesTensor`(밀집 3D 앙상블×시간×계열), `timeSeriesSparseTensor`, `timeSeriesMatrix`(2D), `timeSeriesSparseMatrix`, `sparseTimeSeries`, `timeSeriesModel` (`timeseries/` 동명 `.cpp/.h`). matrix 계열은 시뮬레이터가 직접 사용(`rtcToolsSimulator.cpp:31` 인자 `timeSeriesMatrixInterface*`).

### 5.3 입출력 포맷
- **PI-XML(FEWS Published Interface)**: `piTimeSeries.{cpp,h}` + SAX2 파서 `piTimeSeriesSAX2Handler.{cpp,h}` (Delft-FEWS 연계 표준 포맷).
- **CSV**: `csvInterface.{cpp,h}`.
- **OpenMI**: `openMIInterface`, `openMIExchangeItem` (`timeseries/openMI*.{cpp,h}`).
- **state**: `stateInterface.{cpp,h}` (warm/cold state 입출력).
- **scenario tree**(앙상블 최적화용): `scenarioTreeGenerator`, `scenarioTree_binary`, `scenarioTree_oneToN` (`timeseries/scenarioTree*.{cpp,h}`).

## 6. utilities — converters / 보간 / equation 변환

`utilities/` 는 룩업·방정식 변환기 모음. 공통 추상 `converter` (`utilities/converter.h`) — `convert`/`convertDer`/`reverseConvert`.

### 6.1 lookupTableConverter (1D 보간) — 핵심 수치
`lookupTableConverter::interpolate` (`utilities/lookupTableConverter.cpp:93-168`):
- 옵션 `interpolationOption { BLOCK, LINEAR }` 가 내부(intOpt)·외삽(extOpt) 각각에 적용.
- NaN 입력 → NaN, 단일점 테이블 → `y[0]` (`lookupTableConverter.cpp:96-99`).
- 구간 내 LINEAR: $y = y_{it} + (y_{it+1}-y_{it})\dfrac{x - x_{it}}{x_{it+1}-x_{it}}$ (`lookupTableConverter.cpp:118`). 오름·내림 양방향 정렬 모두 처리 (`lookupTableConverter.cpp:104`).
- 범위 밖 LINEAR 외삽: 양끝 두 점으로 선형 연장 (`lookupTableConverter.cpp:142-143,160-162`), BLOCK 외삽은 끝값 유지 (`lookupTableConverter.cpp:131-133,150-152`).
- 미분 `convertDer` 은 유한차분(EPS=1e-6), 주석 `@todo refactor for analytical derivative` (`lookupTableConverter.cpp:52-66`).
- `getIntegrator()`: 사다리꼴 적분으로 누적 테이블 생성 $y_{int}[i]=y_{int}[i-1]+\tfrac12(y_i+y_{i-1})(x_i-x_{i-1})$ (`lookupTableConverter.cpp:81-90`).

### 6.2 방정식 변환기
- `linearEquationConverter` — 선형 $y=ax+b$ (`utilities/linearEquationConverter.{cpp,h}`).
- `powerEquationConverter` — 멱함수 (`utilities/powerEquationConverter.{cpp,h}`).
- `sigmoidLogisticEquationConverter`, `tansigEquationConverter` — 시그모이드/tansig (신경망류 활성함수; 데이터구동 변환) (`utilities/sigmoidLogisticEquationConverter.{cpp,h}`, `tansigEquationConverter.{cpp,h}`).
- `monotonLookupTableConverter`, `lookup2DTableConverter`, `dateLookupTableConverter` — 단조/2D/날짜 변형.
- `linearEquationSolvers.{cpp,h}` — 선형계 풀이(컨트롤러 내부 수치).
- `equidistantAggregation` (`utilities/aggregation.h`, `equidistantAggregation.{cpp,h}`) — 시계열 시간 집계.

### 6.3 시간·파일 유틸
`utils` 클래스(정적) (`utilities/utils.h:68-98`): `date2time`/`time2date`(1970 기준 ms 변환), `getDayOfYear`, 동적 행렬·텐서 할당(`imat/dmat/iten/dten`), 파일 존재·절대경로·`xsd_filename` 등.

## 7. dataBinding (생성 코드) + XML 파서 (외부)

- `dataBinding/` 24 파일(`*.cxx/.hxx`)은 **CodeSynthesis XSD 자동생성** 산출물: `rtcToolsConfig.hxx:3` `This program was generated by CodeSynthesis XSD, an XML Schema to ...`, `:36` `@brief Generated from rtcToolsConfig.xsd.`, 런타임 버전 체크 `XSD_INT_VERSION != 3030000L` (`rtcToolsConfig.hxx:49-50`). 설정 스키마: `rtcToolsConfig`(schematization), `rtcDataConfig`(시계열 매핑), `rtcRuntimeConfig`, `rtcObjectiveConfig`, PI 포맷용 `pi_*`(diag/run/state/timeseries/modelparameters). `schematisation` 생성자가 이 바인딩으로 XML→객체를 빌드 (`schematization/schematisation.h:33,72` `auto_ptr<RtcToolsConfigComplexType> rtcToolsConfig`).
- **Apache Xerces-C** (XML SAX 파서)는 T-tier 외부 라이브러리로 **검수 제외**(배정 지침). 본 코드에서의 사용 흔적만: `timeseries/piTimeSeriesSAX2Handler.h:33-34` `#include <xercesc/sax2/Attributes.hpp>` / `DefaultHandler.hpp`, 그리고 XSD 런타임 `<xsd/cxx/...>`. PI-XML 시계열은 Xerces SAX2 로 스트림 파싱된다.

## 8. 통합·진입점 (BMI / OpenMI / 런타임)

FBC 는 독립 실행 + 라이브러리 호출 양쪽으로 동작:

- **BMI** (Basic Model Interface): `bmi.h` 에 표준 BMI 1.0 C API 선언 — `initialize(config_file)`, `update(dt)`, `finalize()`, `get/set_var`, `get_current_time` 등 (`bmi.h:41-74`). DIMR 가 이 BMI 로 FBC 를 구동(참조: [[delft3d_dimr_coupling]]).
- BMI 구현: `rtcToolsBMI.cpp`; OpenMI 래퍼: `rtcToolsOpenMI.{cpp,h}`.
- 런타임: `rtcToolsRuntime.{cpp,h}` (가장 큰 파일, 42KB) — 앙상블 맵·모드·파라미터 구성·시뮬레이터 오케스트레이션. 시간루프 `for (step = iStart; step <= iEnd; step++)` (`rtcToolsRuntime.cpp:122`). 부가 출력으로 각 trigger/rule 의 `_isActive` 컬럼을 CSV 에 추가 (`rtcToolsRuntime.cpp:1197-1213`).
- 진단/로깅: `piDiagInterface.{cpp,h}` → PI diag XML.
- 최적화: `rtcToolsOptimizer.h` + `evaluateGradient`(adjoint) 로 예보기반 최적제어(scenario tree) 지원.

## 9. 흐름경계조건 관점 요약

- FBC 의 출력 setting(게이트 높이, 펌프 용량, 위어 crest, 경계 setting)은 상태벡터의 `iYOut` 컬럼에 기록되고, hydraulic model(D-Flow FM/flow2d3d)이 다음 스텝 경계·구조물 조건으로 읽어간다(BMI `set_var`/시계열 교환). 결합 메커니즘은 [[delft3d_dimr_coupling]] 참조.
- flow2d3d 자체의 **흐름경계 보정** 루틴 `fbcorr.f90` 은 FBCTools 와 별개 모듈(존재만 언급, 본 노트 범위 밖). ⚠ 두 fbc 의 관계(이름 우연 일치 vs 설계 연계)는 본 디렉토리 코드만으로 단정 불가 — source-needed.
- adjoint(`solveDer`)는 대부분의 rule 에서 미구현(`runtime_error`) — 실무 RTC 구성에서 gradient-based 최적화는 lookupTable/component 위주로만 가능. (rule 별 `solveDer` 본문 = `not implemented`, 예 `rules/limiterRule.cpp:57-60`, `rules/pidControllerPositional.cpp:152-154`.)

## 10. 미확인 / source-needed

- `component.{cpp,h}` 의 구체 solve 본문(수리 시스템 모델링)은 미독 — 역할만 확인(`components/component.h:37` element 상속). source-needed.
- `expression` 클래스의 연산자 적용 본문(`schematization/expression.cpp`)은 헤더 enum `OPERATOR { PLUS, ..., MULTIPLY, ... }` (`schematization/expression.h:53-57`)와 "두 입력 + 연산자(+,-,*,/,min,max)" 주석(`expression.h:42-46`)만 확인, solve 본문 미독. source-needed.
- `mergerSplitter` / `rtcMerger` / `unitDelay` 본문 미독(역할: 시계열 병합·분기·단위지연) — 파일 존재만(`schematization/mergerSplitter.{cpp,h}`, `rtcMerger.{cpp,h}`, `unitDelay.{cpp,h}`).
- 앙상블 최적화 목적함수(`rtcObjectiveConfig`) 세부 미독.
