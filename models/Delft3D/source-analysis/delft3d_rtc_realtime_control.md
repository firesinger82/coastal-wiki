---
title: "Delft3D RTC 실시간 제어 — rtc_kernel 의사결정 파라미터·measure·저수지 제어"
model: Delft3D
component: rtc/rtc_kernel
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/rtc/packages/rtc_kernel/src/). DecisionModule.f90 의 beslisparameter 자료구조, Cmpdecv.F90 의 decision-parameter 계산 루프(PARA/PAR2/PAR3/RSVP type)·DoOperation/DoOperationInitial 연산자 표, Chsbmeas.f90 의 measure type 1-12 결정논리·우선순위 루프, MeasureModule.f90 의 measure 자료구조, Calbar.f90 의 barrier 시간보간·RTC setpoint 주입, ReservoirModule.f90 의 RibasimReservoir rule-curve/hedging 방류 알고리즘, externaldllmodule.f90 의 외부 controller DLL 인터페이스를 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
  - models/Delft3D/source-analysis/delft3d_dimr_coupling.md
---

# Delft3D RTC 실시간 제어 (rtc_kernel)

> rtc_kernel 은 수공구조물(weir/gate/pump/barrier) 의 setpoint 를 매 시간스텝마다 결정하는 RTC(Real-Time Control) 커널. 핵심은 (1) 관측값의 선형결합·함수·시간표로 **beslisparameter(decision parameter)** 를 계산하고, (2) 그 값을 임계조건으로 검사하여 **measure(maatregel)** 의 setpoint 를 우선순위에 따라 구조물에 주입하는 rule-based 구조다. 경로: `src/engines_gpl/rtc/packages/rtc_kernel/src/`.

본 노트는 **제어 알고리즘** (decision logic·rule·저수지 제어)에 집중한다. RTC↔FLOW 의 DD/DIMR 결합 흐름은 [[delft3d_dimr_coupling]] 참조. (주석 다수가 네덜란드어 — beslisparameter=decision parameter, maatregel=measure, aanslagpeil=switch-on level, afslagpeil=switch-off level, prioriteit=priority.)

---

## 1. 아키텍처 개요 — 2단 결정 구조

RTC 의 시간스텝당 제어는 두 단계로 구성된다.

| 단계 | 서브루틴 | 입력 → 출력 |
|---|---|---|
| 1. decision parameter 계산 | `CMPDECV` (`Cmpdecv.F90:28`) | 관측 데이터(FLOW/SOBEK/RR/precip/wind) → `DCVVAL(ipara,1)` |
| 2. measure 평가·setpoint 결정 | `CHSBMEAS` (`Chsbmeas.f90:28`) | `DCVVAL` 검사 → `MSSBST(ix)` (구조물 setpoint) |
| 3. barrier 값 산출 | `CALBAR` (`Calbar.f90:28`) | 시간표 + RTC measure → `valbar(2,ibar)` |

decision parameter 의 시간이력 저장은 `DCVVAL(ipara, it)` 2차원 배열로, `it=1` 이 현재 스텝, `it>1` 이 과거 스텝이다 (`DecisionModule.f90:130-132`). 매 스텝 시작 시 이력을 한 칸씩 shift 한다 (`Cmpdecv.F90:127-133`).

이 커널은 본래 SOBEK 용으로 설계되어 Delft3D-FLOW(D3D) 위치는 별도 차원으로 추가되었다. `PARDIM(ipar,:)` 의 9개 차원이 데이터 출처를 구분한다: 1=Sobek-Flow, 2=3B(RR), 3=precipitation, 4=external(wind), 5=WQ, 6=decision parameters, 7=RSV, 8=interpolation tables, 9=D3DFlow (`DecisionModule.f90:44-52`).

---

## 2. Decision parameter 계산 — `CMPDECV`

`DCVVAL(ipara,1)` 는 4가지 parameter type 으로 계산된다. type 은 `ParTyp(ipara)` 문자열로 분기한다 (`Cmpdecv.F90:203,282,323,412`).

### 2.1 사전정의 변수 (predefined, index 1-11)

날짜·시간이 고정 인덱스로 들어간다 (`Cmpdecv.F90:169-185`):

| index | 내용 |
|---|---|
| 1-6 | IYear, IMo, IDay, IHour, IMin, ISec |
| 7 | YYYYMMDD = `IYear*10000 + IMo*100 + IDay` (`Cmpdecv.F90:175`) |
| 9 | YYYYMMDD.HHMMSS 형식 (`Cmpdecv.F90:177-178`) |
| 10 | Weekday (`Cmpdecv.F90:184`) |
| 11 | RtmSiz (시간스텝 크기) |

`NParI=11` 개가 predefined (`PARAMETERMODULE.f90:141`).

### 2.2 type `'PARA'` — 관측값의 선형결합

각 데이터 출처를 순회하며 `CMPRHLP` 로 계수곱·offset·time-shift 를 적용한 항을 누적한다 (`Cmpdecv.F90:203-251`). 예: Sobek 위치 항 (`Cmpdecv.F90:205-211`), D3DFlow 위치 항 (`Cmpdecv.F90:245-251`). 계수는 `CFSBK(ipar,i,1)`=곱셈계수, `(...,2)`=덧셈계수 (`DecisionModule.f90:97-98`).

과거 decision parameter 참조 항 (`Cmpdecv.F90:254-277`):

$$\text{RHLP} = \text{CFMULT}\cdot\text{DCVVAL}(\text{IPAR2}, \text{IT}) + \text{CFADD}$$

여기서 time-shift `TISPAR < 0` 이며 시간인덱스 `IT = \min(\text{NTIMS}, 1-\text{TISPAR})` 로 과거 스텝을 가리킨다 (`Cmpdecv.F90:256, 264-266`).

### 2.3 type `'PAR2'` — 함수 조합 (산술·삼각·로그 등)

여러 항을 입력 순서(`ParOrder`)대로 읽어 `DoOperation`/`DoOperationInitial` 로 연산을 누적한다 (`Cmpdecv.F90:343-403`). 첫 항은 `DoOperationInitial`, 이후는 `DoOperation`.

`PAROPER(ipara)` 연산자 코드 표 (`Cmpdecv.F90:677-714` = 누적 연산, `Cmpdecv.F90:750-868` = 단항 함수):

| code | 누적 연산 (`DoOperation`) | code | 단항 함수 (`DoOperationInitial`) |
|---|---|---|---|
| 1 | `+ RHLP` | 9-14 | sin/cos/tan (radian·degree) |
| 2 | `- RHLP` | 15-20 | asin/acos/atan |
| 3 | `* RHLP` | 21-23 | floor/ceiling/nint |
| 4 | `/ RHLP` (0 보호 `Cmpdecv.F90:684-693`) | 24-25 | square / sqrt |
| 5 | `max(.,RHLP)` | 26-28 | exp / ln / log10 |
| 6 | `min(.,RHLP)` | 29-31 | sinh/cosh/tanh |
| 7 | `+ RHLP` (이후 평균: `Cmpdecv.F90:406` 에서 `/NTotal`) | 32 | interpolation table |
| 8 | `** RHLP` | | |
| 32 | interpolation table (입력=DCVVAL) (`Cmpdecv.F90:703-709`) | | |

degree 삼각함수는 Intel 확장 `sinD/cosD` 사용, 비-Intel 컴파일러는 `pi/180` 변환으로 대체 (`Cmpdecv.F90:743-747, 755-760`).

### 2.4 type `'PAR3'` — 시간표 직접조회

`GetNewValue` 로 시간표에서 현재 일시에 해당하는 값을 읽어 그대로 대입 (`Cmpdecv.F90:412-418`). 이것이 **time rule** (시간 기반 제어)의 본체다.

### 2.5 type `'RSVP'` — 저수지 제어 (§5 참조)

`RibasimReservoir` 호출로 방류량과 rule-curve 수위를 산출한다 (`Cmpdecv.F90:282-316`).

---

## 3. Measure 평가·setpoint 결정 — `CHSBMEAS`

decision parameter 값(`DCVVAL`)을 임계조건으로 검사해 구조물 setpoint 를 정하는 **condition rule** 의 본체. measure 는 우선순위(priority)별로 평가된다.

### 3.1 우선순위 루프

```
DO IPRIOR = LOWSPRI, 1, -1   ! Chsbmeas.f90:73
   DO IMEAS=1,NSMEAS
      IF (MEASPR(IMEAS) .EQ. IPRIOR) THEN ...
```

priority 1 이 최상위이며, 루프를 `LOWSPRI`(최저=가장 큰 숫자)부터 1까지 **내림차순**으로 돈다. 따라서 동일 구조물에 여러 measure 가 걸리면 priority 1 measure 가 마지막에 평가되어 setpoint 를 덮어쓴다(=최우선) (`Chsbmeas.f90:73-75`, 우선순위 의미는 `rdsmeas.f90:808-812` "priority 1 = highest (first) priority").

### 3.2 measure type 1-12 결정논리

`MEASTY(imeas)` 로 분기. 각 type 의 의미와 조건검사 (`Chsbmeas.f90:76-207`):

| type | 검사방식 | setpoint 출처 |
|---|---|---|
| 1 | check value·setpoint 모두 수치입력 | numeric `MEASSP` |
| 2 | check value/setpoint 배열, **보간** 으로 setpoint 산출 (`Chsbmeas.f90:108-119`) | `INTERP_double` |
| 3 | check value 가 다른 decision parameter, setpoint 수치 | numeric |
| 4 | check value·setpoint 모두 다른 decision parameter | decision parameter |
| 5-8 | **다변수 AND 검사**: nv 개 decision var 를 nv 개 check value 와 모두 비교, 전부 참일 때만 발동 (`Chsbmeas.f90:121-152`) | value/parameter |
| 9 | Matlab measure, 항상 활성 (`Chsbmeas.f90:156-168`) | decision parameter 값 |
| 10 | 검사 없음, setpoint=parameter (`Chsbmeas.f90:169-179`) | parameter |
| 11 | **DLL measure**, 항상 활성 (`Chsbmeas.f90:180-191`) | decision parameter 값 |
| 12 | Exe(TCN) measure, 데이터 없으면 InitSp default (`Chsbmeas.f90:192-206`) | decision parameter / InitSp |

핵심 비교연산은 `MEASCH(imeas)` 문자(`<`,`=`,`>`)로 분기. `=` 는 부동소수 허용오차 `1e-7` 적용 (`Chsbmeas.f90:91-96`):

```fortran
IF (MEASCH .EQ. '<') CHKTRUE = (RVAL .LT. MEASCV)        ! Chsbmeas.f90:91-92
ELSEIF (MEASCH .EQ. '=') CHKTRUE = (ABS(RVAL-MEASCV) .LT. .0000001)  ! :93-94
ELSEIF (MEASCH .EQ. '>') CHKTRUE = (RVAL .GT. MEASCV)    ! :95-96
```

type 5-8 의 다변수 검사는 하나라도 거짓이면 `GOTO 501` 로 즉시 탈출(short-circuit AND) (`Chsbmeas.f90:148`).

### 3.3 활성화·setpoint 주입 + missing value

measure 가 발동(`MSB_ON`)하려면 (조건 참) AND (setpoint 이 missing value 아님) 둘 다 만족해야 한다 (`Chsbmeas.f90:102`). 발동 시 해당 구조물의 unique-id 슬롯에 setpoint 를 쓴다: `MSSBST(IX) = MEASSP(IMEAS)` (`Chsbmeas.f90:106, 116, 152`).

`CheckMissingValue` 는 값이 missing value ±0.0009 범위면 false 반환 (`Chsbmeas.f90:258-272`). missing value 인 measure 는 무시되어 하위 priority 결과를 덮어쓰지 않는다.

measure 자료구조는 `MeasureModule.f90` 에 정의: `MEASTY`=type, `MEASPR`=priority, `MEASCV`=check value, `MEASSP`=set point, `MEASCH`=비교문자, `INITSP`=구조물 초기 setpoint (`MeasureModule.f90:117-126`, 주석 `:87-115`). 3B(RR) measure 는 별도로 aanslagpeil/afslagpeil(on/off level) 기반 hysteresis 제어 (`MSON3B`/`MSOFF3B`/`ONCH3B`/`OFCH3B`, `MeasureModule.f90:41-46, 70-72`).

---

## 4. Barrier 제어 — `CALBAR`

D3D-FLOW barrier(가동보)의 값을 매 스텝 산출한다. 두 소스의 합성이다.

### 4.1 시간표 보간 (time rule)

요청 일시 `juldt` 가 활성 구간 `[barlju, barhju]` 안이면 보간 또는 block value (`Calbar.f90:165-182`). 선형보간:

$$\text{ratio} = 1 - \frac{\text{juldt} - \text{barlju}}{\text{barhju} - \text{barlju}}, \quad \text{valbar} = \text{ratio}\cdot\text{barlvl} + (1-\text{ratio})\cdot\text{barhvl}$$

(`Calbar.f90:173-174`). `barint(ibar)` 가 false 이면 보간 대신 block value(앞 점 유지) (`Calbar.f90:176-181`). 활성구간 이후이면 다음 행을 탐색하거나 외삽 (`Calbar.f90:190-239`).

`valbar(1,:)=-1` (no steering signal), `valbar(2,:)=0` 으로 초기화 후, 값이 정해지면 `valbar(1,ibar)=1.0` (steering active) 로 표시 (`Calbar.f90:142-143, 159-160`).

### 4.2 RTC measure 주입 (override)

시간표 계산 후, barrier 이름이 RTC measure 의 id 또는 description 과 일치하면 measure 의 setpoint(`MSSBST`)로 **덮어쓴다** (`Calbar.f90:243-260`):

```fortran
do i = NsMsId_SBK+1, NsMsId_D3D       ! Calbar.f90:245  (D3D measure 범위)
   ID = MSSBID(i); NM = MSSBDescr(i)
   if (BarrierNames(ibar) == ID) then  valbar(2,ibar) = MSSBST(i)  ! :253-254
```

즉 time rule(시간표) 위에 condition rule(RTC measure) 이 우선한다.

---

## 5. 저수지 제어 — `RibasimReservoir` (Ribasim-style rule curve)

type `'RSVP'` decision parameter 가 호출하는 저수지 방류 결정 알고리즘. Ribasim 모방 방식으로, **rule curve 3선 + hedging + gate 용량**으로 방류량을 결정한다 (`ReservoirModule.f90:1228-1800`).

### 5.1 입력·출력

입력(`Cmpdecv.F90:283-298`): 초기수위 `InitLevel`, 예상유입 `ExpInflow`, 최대허용수위 `MaxAllowedLvl`, 각 outlet link 의 수요 `DesiredQcons`·최대유량 `MaxFlowOutletLinks`.

출력: 3종 gate 방류(bottom gate / turbine / spillway)와 rule-curve 수위 3선 `HFlood`(홍수조절), `HTarget`(목표), `HFirm`(확보) (`Cmpdecv.F90:78-83, 306-311`; `ReservoirModule.f90:1236-1237, 1246`).

### 5.2 rule curve 와 hedging

3개 rule-curve 수위를 시간표에서 조회 (`ReservoirModule.f90:1357-1366`): col1=flood control, col2=target, col3=firm storage (주석 `ReservoirModule.f90:394` "3rd column = firm storage curve").

hedging 수위는 dead level 과 firm level 사이를 백분율로 보간 (`ReservoirModule.f90:1368-1371`):

$$\text{HedgingLevel}_i = \text{DeadLevel} + \text{HedgingLevelPercentage}_i \cdot (\text{HFirm} - \text{DeadLevel})$$

일관성 강제: $\text{HFlood} \ge \text{HTarget} \ge \text{HFirm} \ge \text{DeadLevel}$, 그리고 $\text{HFlood} \le \text{FullRsvLevel}$ (`ReservoirModule.f90:1374-1384`).

### 5.3 방류 결정·반복

수요(소비+에너지)를 outlet link 별 desired release 로 합성하되 에너지 수요는 turbine link 에만 (`ReservoirModule.f90:1336-1349`).

**2단 반복**:
1. **방류용량 수렴 반복** (`ReservoirModule.f90:1459-1494`): `SetReleaseCapacities` 로 gate 용량 한계를 적용, 평균수위 `Hav=0.5*(InitLevel+HProv)` 로 단순 implicit 처리, `Sprov`(임시저수)와 `Hprov` 가 `EpsVolume=0.1`·`EpsFlow=0.001` 기준 수렴까지 반복(최대 `MxIter=10`) (수렴기준 `ReservoirModule.f90:91-98, 1493`).
2. **운영규칙 반복** (`ReservoirModule.f90:1504-1581`): flood 수위 초과 시 임의 gate 로 추가방류, target 초과 시 turbine 으로만 추가방류, firm 미만 시 hedging 으로 방류 감축 (주석 `ReservoirModule.f90:1499-1503`). 방류는 gate 유형별로 분배(`SetFlows`): turbine→bottom gate→spillway 순 (`ReservoirModule.f90:1541, 1578-1580`).

수위↔저수량 변환은 `LevelToVolume`/`VolumeToLevel` (HAV 곡선 보간) (`ReservoirModule.f90:1312-1314, 1387-1389`). gate 유형 차원은 `MaxTypeGates=3`(1=bottom gate, 2=turbine, 3=spillway), `MaxSameGates=15` (`ReservoirModule.f90:83-86`).

---

## 6. 외부 controller DLL 인터페이스 — RTC-Tools

PID 등 본격 제어 알고리즘은 이 Fortran 커널이 아니라 **외부 DLL(RTC-Tools)** 에 위임된다. 커널은 데이터 전달자 역할만 한다.

`CMPDECV` 말미에서 `dll_handle .ne. 0` 이면 (`Cmpdecv.F90:438`): `set_pointers` 로 결과배열을 노출하고 (`Cmpdecv.F90:442-443`), 모든 구조물 상태를 dll 통신 배열로 복사한 뒤 `rtc_perf_function(dll_handle, dll_function, ...)` 으로 DLL 함수를 호출한다 (`Cmpdecv.F90:563-576`). 반환된 setpoint(`DllSobekS`)를 `'Dll'` 로 시작하는 decision parameter 에 되쓴다 (`Cmpdecv.F90:589-606`).

DLL 에 노출되는 구조물 변수 인덱스(`externaldllmodule.f90:48-82`): water level, discharge, crest level/width, gate lower edge/opening(orifice), pump capacity, head over structure 등. controller 출력은 `isobeks=1` "set point of SOBEK-flow controller" (`externaldllmodule.f90:75`).

`set_pointers` (`externaldllmodule.f90:145-` 이하)는 결과 배열 구간에 포인터를 연결해 Matlab 구현과 동일한 형태로 개별 배열을 노출하는 것이 목적이다 (모듈 헤더 `externaldllmodule.f90:30-37`).

> ⚠ PID 게인(Kp/Ki/Kd)·deadband 등 연속 제어기 파라미터는 본 rtc_kernel 디렉토리 소스에 **존재하지 않는다**. 커널 내 제어는 (a) 선형결합·함수·시간표 기반 decision parameter, (b) 임계조건 기반 measure(on/off·보간 setpoint), (c) rule-curve 기반 저수지 방류로 한정된다. 본격 feedback controller(PID 포함)는 외부 RTC-Tools DLL 책임이며 그 소스는 이 패키지 범위 밖 — **source-needed** (RTC-Tools 별도 저장소).

---

## 7. 요약 — 제어 알고리즘 분류

| 제어 유형 | 구현 위치 | 메커니즘 |
|---|---|---|
| time rule | `PAR3` decision param, `CALBAR` 시간보간 | 시간표 직접조회·선형보간 (`Cmpdecv.F90:412-418`, `Calbar.f90:173-174`) |
| condition rule | `CHSBMEAS` measure type 1-12 | `<`/`=`/`>` 임계검사 → setpoint 주입, 우선순위 override (`Chsbmeas.f90:73-207`) |
| 다변수 AND rule | measure type 5-8 | nv개 조건 모두 참일 때 발동 (`Chsbmeas.f90:121-152`) |
| 보간 setpoint | measure type 2 | check value→setpoint 1D 보간 (`Chsbmeas.f90:108-119`) |
| 함수 결합 | `PAR2` decision param | 산술·삼각·로그·max/min 누적연산 (`Cmpdecv.F90:677-868`) |
| 저수지 rule curve | `RibasimReservoir` | flood/target/firm 3선 + hedging + gate 용량 반복수렴 (`ReservoirModule.f90:1228-1800`) |
| 일반 feedback (PID 등) | 외부 RTC-Tools DLL | `rtc_perf_function` 위임 (`Cmpdecv.F90:563-576`) — 소스 범위 밖 |

핵심: rtc_kernel 자체는 **rule-based(임계·시간표·rule curve) 제어**의 본체이고, 연속 feedback 제어는 외부 DLL 로 분리된 아키텍처다.
