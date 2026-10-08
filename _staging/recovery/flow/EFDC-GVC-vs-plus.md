---
title: "EFDC-GVC 계산 흐름과 EFDCPlus_Stable 구현 비교"
citation_status: source-needed
analysis_date: 2026-10-08
---

# EFDC-GVC 계산 흐름과 EFDC+의 차이

## 1. GVC 진입, 시간 반복 선택, 직접 호출 순서

이 문서는 AI가 작성한 원문 대조 기록이다. 이 문서는 저장소에 들어 있는 두 소스 판본을 비교한다. 이 문서는 실행 결과나 수치 동등성을 판정하지 않는다.

인용 경로의 `G/`는 `models/EFDC/raw/source_code/EFDC-GVC/`이다. 인용 경로의 `P/`는 `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/`이다. 인용 경로의 `N`은 `models/EFDC/source-analysis/efdc_gvc_legacy.md`이다. 인용은 원문 줄의 선행 공백만 생략한다. 노트의 일부만 인용한 곳에는 원문에서 연속하는 발췌문을 적는다.

### 1.1 진입과 입력 플래그

GVC의 진입점은 `G/aaefdc.for:14` `PROGRAM AAEFDC`이다. `AAEFDC`는 `INPUT` 호출 뒤에 격자와 초기 상태를 준비한다. 직접 호출문 전체는 §1.3의 진입 표에 적었다.

| 입력 또는 초기화 대상 | 확인한 처리 | 원문 근거 |
|---|---|---|
| 기본 입력 | `INPUT`은 `EFDC.INP`를 연다. | `G/aaefdc.for:218` `CALL INPUT(TITLE)`<br>`G/input.f:85` `OPEN(1,FILE='EFDC.INP',STATUS='UNKNOWN')` |
| 연직격자와 시간적분 | C1A는 `IGRIDV`와 `ITIMSOL`을 읽는다. `INPUT`은 `ITIMSOL`을 `IS2TIM`에 대입한다. | `G/input.f:99` `CALL SEEK('C1A')`<br>`G/input.f:100` `READ(1,*,IOSTAT=ISO)IGRIDH,INESTH,IGRIDV,ITIMSOL,ISHOUSATONIC  !IS2TLPG`<br>`G/input.f:104` `IS2TIM=ITIMSOL` |
| 장기 수송 | C4는 `ISLTMT`와 평균 수송 제어값을 읽는다. | `G/input.f:133` `CALL SEEK('C4')`<br>`G/input.f:134` `READ(1,*,IOSTAT=ISO) ISLTMT,ISSSMMT,ISLTMTS,ISIA,RPIA,RSQMIA,`<br>`G/input.f:135` `&                     ITRMIA,ISAVEC` |
| 1차원 수로 | `INPUT`은 `ISCDMA=10`이면 `IS1DCHAN=1`을 설정한다. | `G/input.f:162` `IS1DCHAN=0`<br>`G/input.f:163` `IF(ISCDMA.EQ.10) IS1DCHAN=1` |
| GVC 층 설정 | C9A는 `KC`, `KSIG`, `ISETGVC`, `SELVREF`, `BELVREF`, `ISGVCCK`를 읽는다. | `G/input.f:228` `CALL SEEK('C9A')`<br>`G/input.f:229` `READ(1,*,IOSTAT=ISO)KC,KSIG,ISETGVC,SELVREF,BELVREF,ISGVCCK` |
| GVC 초기화 | `AAEFDC`는 `SETBCS` 뒤에 `SETGVC`를 조건부 호출한다. | `G/aaefdc.for:882` `CALL SETBCS`<br>`G/aaefdc.for:957` `IF(IGRIDV.EQ.1) CALL SETGVC` |
| 초기 농도 | `AAEFDC`는 `IGRIDV=1`일 때 비활성층 농도를 다시 0으로 설정한다. | `G/aaefdc.for:1866` `IF(IGRIDV.EQ.1)THEN`<br>`G/aaefdc.for:1871` `IF(K.LT.KGVCP(L)) SAL(L,K)=0.0`<br>`G/aaefdc.for:1872` `IF(K.LT.KGVCP(L)) SAL1(L,K)=0.0` |
| 저질과 밀도 | `AAEFDC`는 초기 농도 보정 뒤에 저질 초기화와 부력 계산을 호출한다. | `G/aaefdc.for:1926` `IF(ISTRAN(6).GE.1.OR.ISTRAN(7).GE.1) CALL BEDINIT`<br>`G/aaefdc.for:1933` `CALL CALBUOY` |
| 수질과 Explorer 출력 | `AAEFDC`는 시간 반복 루틴을 선택하기 전에 수질 입력과 Explorer 출력을 조건부 초기화한다. | `G/aaefdc.for:2581` `IF(ISTRAN(8).GE.1) CALL WQ3DINP`<br>`G/aaefdc.for:2588` `IF(ISSPH(8).EQ.1.OR.ISBEXP.EQ.1) CALL EE_LINKAGE(1)` |

### 1.2 시간 반복 루틴 선택

아래 표의 조건은 `AAEFDC`의 중첩 조건을 모두 포함한다. `IGRIDV`만으로 시간 반복 루틴을 정할 수 없다.

| 선택 루틴 | 필요한 조건 | 분기 원문 |
|---|---|---|
| `HDMT` | `ISLTMT=0`, `IS1DCHAN=0`, `IS2TIM=0`, `IGRIDV=0` | `G/aaefdc.for:2595` `IF(ISLTMT.EQ.0)THEN`<br>`G/aaefdc.for:2596` `IF(IS1DCHAN.EQ.0)THEN`<br>`G/aaefdc.for:2597` `IF(IS2TIM.EQ.0) THEN`<br>`G/aaefdc.for:2598` `IF(IGRIDV.EQ.0) CALL HDMT` |
| `HDMTGVC` | `ISLTMT=0`, `IS1DCHAN=0`, `IS2TIM=0`, `IGRIDV=1` | `G/aaefdc.for:2595` `IF(ISLTMT.EQ.0)THEN`<br>`G/aaefdc.for:2596` `IF(IS1DCHAN.EQ.0)THEN`<br>`G/aaefdc.for:2597` `IF(IS2TIM.EQ.0) THEN`<br>`G/aaefdc.for:2599` `IF(IGRIDV.EQ.1) CALL HDMTGVC` |
| `HDMT2T` | `ISLTMT=0`, `IS1DCHAN=0`, `IS2TIM>=1` | `G/aaefdc.for:2595` `IF(ISLTMT.EQ.0)THEN`<br>`G/aaefdc.for:2596` `IF(IS1DCHAN.EQ.0)THEN`<br>`G/aaefdc.for:2601` `IF(IS2TIM.GE.1) CALL HDMT2T` |
| `HDMT1D` | `ISLTMT=0`, `IS1DCHAN>=1` | `G/aaefdc.for:2595` `IF(ISLTMT.EQ.0)THEN`<br>`G/aaefdc.for:2603` `IF(IS1DCHAN.GE.1) CALL HDMT1D` |
| `LTMT` | `ISLTMT>=1` | `G/aaefdc.for:2605` `IF(ISLTMT.GE.1) CALL LTMT` |

확인: `SETGVC` 초기화 조건은 위의 루틴 선택 조건과 별개다. 근거는 `G/aaefdc.for:957` `IF(IGRIDV.EQ.1) CALL SETGVC`이다.

확인: `HDMT2T`, `HDMT1D`, `LTMT` 선택문은 `IGRIDV`를 검사하지 않는다. 근거는 위 표의 호출문이다.

해석: 이 디스패치만으로 GVC 격자의 모든 시간적분 조합을 지원한다고 판정할 수 없다. §1.3은 선택된 루틴이 실제로 부르는 계산 루틴을 보여준다.

| 시간 제어 대상 | 확인한 제어 | 원문 근거 |
|---|---|---|
| `HDMT` | 루틴은 `ISTL=3`, `IS2TL=0`, `DELT=DT2`로 시작한다. 루틴은 `NCTBC=NTSTBC`일 때 `ISTL=2`, `DELT=DT`로 바꾸고 500번 위치로 재진입한다. | `G/hdmt.for:337` `ISTL=3`<br>`G/hdmt.for:338` `IS2TL=0`<br>`G/hdmt.for:339` `DELT=DT2`<br>`G/hdmt.for:369` `DO 1000 N=1,NTS`<br>`G/hdmt.for:1408` `IF(NCTBC.EQ.NTSTBC)THEN`<br>`G/hdmt.for:1410` `ISTL=2`<br>`G/hdmt.for:1411` `DELT=DT`<br>`G/hdmt.for:1416` `GOTO 500` |
| `HDMTGVC` | 루틴은 같은 3시점과 2시점 보정 구조를 사용한다. 보정은 초기 수지 호출 뒤의 500번 위치에서 시작한다. | `G/hdmtgvc.for:320` `ISTL=3`<br>`G/hdmtgvc.for:321` `IS2TL=0`<br>`G/hdmtgvc.for:322` `DELT=DT2`<br>`G/hdmtgvc.for:352` `DO 1000 N=1,NTS`<br>`G/hdmtgvc.for:425` `500 CONTINUE`<br>`G/hdmtgvc.for:1470` `IF(NCTBC.EQ.NTSTBC)THEN`<br>`G/hdmtgvc.for:1472` `ISTL=2`<br>`G/hdmtgvc.for:1473` `DELT=DT`<br>`G/hdmtgvc.for:1478` `GOTO 500` |
| `HDMT2T` | 루틴은 `ISTL=2`, `IS2TL=1`, `DELT=DT`를 설정한다. 동적 시간간격 분기는 `CALSTEP` 또는 `CALSTEPD`를 호출한다. 루틴은 1001번 위치로 반복한다. | `G/hdmt2t.for:472` `ISTL=2`<br>`G/hdmt2t.for:473` `IS2TL=1`<br>`G/hdmt2t.for:474` `DELT=DT`<br>`G/hdmt2t.for:509` `IF(N.GE.NTS)GO TO 1000`<br>`G/hdmt2t.for:511` `IF(ISDYNSTP.EQ.0)THEN`<br>`G/hdmt2t.for:518` `IF(IDRYTBP.EQ.0)THEN`<br>`G/hdmt2t.for:519` `CALL CALSTEP`<br>`G/hdmt2t.for:521` `CALL CALSTEPD`<br>`G/hdmt2t.for:523` `DELT=DTDYN`<br>`G/hdmt2t.for:2044` `GOTO 1001` |
| `HDMT1D` | 루틴은 `ISTL=2`, `DELT=DT`를 설정한다. 내부모드와 농도 호출은 두 번째 인자로 상수 `1`을 전달한다. | `G/hdmt1d.for:211` `ISTL=2`<br>`G/hdmt1d.for:212` `DELT=DT`<br>`G/hdmt1d.for:242` `DO 1000 N=1,NTS`<br>`G/hdmt1d.for:547` `CALL CALUVW (ISTL,1)`<br>`G/hdmt1d.for:596` `CALL CALCONC (ISTL,1)` |
| `LTMT` | 루틴은 `RESTRAN.INP`의 평균 수송장을 읽는다. 루틴은 `ADJMMT`로 수송장을 조정한다. 반복 중 `ISCDCA(1)`에 따라 `CALCONC(2,0)` 또는 `CALCONC(3,0)`을 호출한다. | `G/ltmt.for:29` `OPEN(99,FILE='RESTRAN.INP',STATUS='UNKNOWN')`<br>`G/ltmt.for:37` `CALL RESTRAN`<br>`G/ltmt.for:217` `CALL ADJMMT`<br>`G/ltmt.for:232` `DO 1000 N=1,NTS`<br>`G/ltmt.for:241` `IF(ISCDCA(1).NE.1)THEN`<br>`G/ltmt.for:242` `CALL CALCONC (2,0)`<br>`G/ltmt.for:244` `CALL CALCONC (3,0)` |

확인: GVC의 `INPUT`은 `IS2TIM=0`이면 동적 시간간격을 끈다. 근거는 `G/input.f:204` `IF(IS2TIM.EQ.0)ISDYNSTP=0`이다.

### 1.3 각 루틴의 1단계 호출 순서 표

여기서 1단계는 현재 루틴이 직접 쓰는 `CALL`을 뜻한다. 표는 활성 소스의 위치 순서로 모든 직접 호출문을 적는다. 표는 초기화, 반복, 종료를 구분한다. 표는 계측과 출력 호출도 포함한다. 표의 행 수는 호출 실행 횟수를 뜻하지 않는다.

호출문 안의 한 줄 `IF`는 그 호출문의 조건이다. 마지막 열은 호출문을 감싸는 `IF` 블록의 원문이다. `ELSE` 행은 앞선 조건의 다른 분기를 뜻한다. 표는 주석 처리한 호출문을 제외한다. 표는 함수 호출과 인라인 배열 계산을 별도로 열거하지 않는다.

`HDMT`와 `HDMTGVC`의 보정 재진입은 §1.2의 500번 위치를 따른다. 따라서 소스 순서를 한 번 읽는 것만으로 한 시간단계의 호출 횟수를 정할 수 없다. `CALUVW`의 다층 분기와 단층 분기는 서로 다른 경로다. 근거는 `G/hdmt.for:788` `IF(KC.GT.1)THEN`와 `G/hdmtgvc.for:764` `IF(KC.GT.1)THEN`이다.

#### AAEFDC 진입과 반환

| 구간 | 직접 호출문 위치와 원문 | 외부 IF 분기 원문 |
|---|---|---|
| 진입·초기화 | `G/aaefdc.for:175` `CALL WELCOME` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:218` `CALL INPUT(TITLE)` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:224` `IF(NSHMAX.GE.1) CALL DEPSMTH` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:686` `CALL AINIT` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:882` `CALL SETBCS` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:957` `IF(IGRIDV.EQ.1) CALL SETGVC` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:1057` `IF(ISRESTI.EQ.1) CALL RESTIN1` | `G/aaefdc.for:1055` `IF(ISLTMT.EQ.0)THEN`<br>`G/aaefdc.for:1056` `IF(ISRESTI.GE.1)THEN` |
| 진입·초기화 | `G/aaefdc.for:1058` `IF(ISRESTI.EQ.2) CALL RESTIN2` | `G/aaefdc.for:1055` `IF(ISLTMT.EQ.0)THEN`<br>`G/aaefdc.for:1056` `IF(ISRESTI.GE.1)THEN` |
| 진입·초기화 | `G/aaefdc.for:1059` `IF(ISRESTI.EQ.10) CALL RESTIN10` | `G/aaefdc.for:1055` `IF(ISLTMT.EQ.0)THEN`<br>`G/aaefdc.for:1056` `IF(ISRESTI.GE.1)THEN` |
| 진입·초기화 | `G/aaefdc.for:1061` `IF(ISRESTI.EQ.-1) CALL RESTIN1` | `G/aaefdc.for:1055` `IF(ISLTMT.EQ.0)THEN` |
| 진입·초기화 | `G/aaefdc.for:1926` `IF(ISTRAN(6).GE.1.OR.ISTRAN(7).GE.1) CALL BEDINIT` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:1933` `CALL CALBUOY` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:2527` `CALL SALTSMTH` | `G/aaefdc.for:2526` `IF(NSBMAX.GE.1)THEN` |
| 진입·초기화 | `G/aaefdc.for:2542` `CALL PPLOT (2)` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:2546` `CALL DEPPLT` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:2557` `CALL PPLOT (1)` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:2581` `IF(ISTRAN(8).GE.1) CALL WQ3DINP` | 외부 IF 블록 없음 |
| 진입·초기화 | `G/aaefdc.for:2588` `IF(ISSPH(8).EQ.1.OR.ISBEXP.EQ.1) CALL EE_LINKAGE(1)` | 외부 IF 블록 없음 |
| 시간 반복 선택 | `G/aaefdc.for:2598` `IF(IGRIDV.EQ.0) CALL HDMT` | `G/aaefdc.for:2595` `IF(ISLTMT.EQ.0)THEN`<br>`G/aaefdc.for:2596` `IF(IS1DCHAN.EQ.0)THEN`<br>`G/aaefdc.for:2597` `IF(IS2TIM.EQ.0) THEN` |
| 시간 반복 선택 | `G/aaefdc.for:2599` `IF(IGRIDV.EQ.1) CALL HDMTGVC` | `G/aaefdc.for:2595` `IF(ISLTMT.EQ.0)THEN`<br>`G/aaefdc.for:2596` `IF(IS1DCHAN.EQ.0)THEN`<br>`G/aaefdc.for:2597` `IF(IS2TIM.EQ.0) THEN` |
| 시간 반복 선택 | `G/aaefdc.for:2601` `IF(IS2TIM.GE.1) CALL HDMT2T` | `G/aaefdc.for:2595` `IF(ISLTMT.EQ.0)THEN`<br>`G/aaefdc.for:2596` `IF(IS1DCHAN.EQ.0)THEN` |
| 시간 반복 선택 | `G/aaefdc.for:2603` `IF(IS1DCHAN.GE.1) CALL HDMT1D` | `G/aaefdc.for:2595` `IF(ISLTMT.EQ.0)THEN` |
| 시간 반복 선택 | `G/aaefdc.for:2605` `IF(ISLTMT.GE.1) CALL LTMT` | 외부 IF 블록 없음 |
| 반환 후 계측 | `G/aaefdc.for:2685` `CALL TIMELOG(N,TIMEDAY)` | 외부 IF 블록 없음 |

#### HDMT

| 구간 | 직접 호출문 위치와 원문 | 외부 IF 분기 원문 |
|---|---|---|
| 초기화 | `G/hdmt.for:34` `CALL TIMEF(WTTMP)` | `G/hdmt.for:30` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:32` `ELSE` |
| 초기화 | `G/hdmt.for:85` `IF(ISWAVE.EQ.1) CALL WAVEBL` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt.for:86` `IF(ISWAVE.EQ.2) CALL WAVESXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt.for:94` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt.for:100` `IF(ISHDMF.GE.1) CALL CALHDMF` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt.for:109` `CALL CALTSXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt.for:141` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt.for:174` `CALL CALTSXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt.for:360` `CALL TIMELOG(N,TIMEDAY)` | 외부 IF 블록 없음 |
| 반복·초기 수지 | `G/hdmt.for:415` `CALL CALBAL1` | `G/hdmt.for:412` `IF(IS2TIM.EQ.0) THEN`<br>`G/hdmt.for:414` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN` |
| 반복·초기 수지 | `G/hdmt.for:418` `CALL CBALEV1` | `G/hdmt.for:412` `IF(IS2TIM.EQ.0) THEN`<br>`G/hdmt.for:414` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN`<br>`G/hdmt.for:417` `IF(NTMP.EQ.0)THEN` |
| 반복·초기 수지 | `G/hdmt.for:420` `CALL CBALOD1` | `G/hdmt.for:412` `IF(IS2TIM.EQ.0) THEN`<br>`G/hdmt.for:414` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN`<br>`G/hdmt.for:417` `IF(NTMP.EQ.0)THEN`<br>`G/hdmt.for:419` `ELSE` |
| 반복·초기 수지 | `G/hdmt.for:427` `CALL BUDGET1` | `G/hdmt.for:412` `IF(IS2TIM.EQ.0) THEN`<br>`G/hdmt.for:426` `IF(NCTBC.NE.NTSTBC.AND.ISSBAL.GE.1)THEN` |
| 반복·연직 혼합 | `G/hdmt.for:452` `CALL TIMEF(WT1TMP)` | `G/hdmt.for:448` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:450` `ELSE` |
| 반복·연직 혼합 | `G/hdmt.for:456` `IF(ISTOPT(0).EQ.0)CALL CALAVBOLD (ISTL)` | `G/hdmt.for:454` `IF(KC.GT.1)THEN`<br>`G/hdmt.for:455` `IF(ISQQ.EQ.1)THEN` |
| 반복·연직 혼합 | `G/hdmt.for:457` `IF(ISTOPT(0).GE.1)CALL CALAVB (ISTL)` | `G/hdmt.for:454` `IF(KC.GT.1)THEN`<br>`G/hdmt.for:455` `IF(ISQQ.EQ.1)THEN` |
| 반복·연직 혼합 | `G/hdmt.for:459` `IF(ISQQ.EQ.2) CALL CALAVB2 (ISTL)` | `G/hdmt.for:454` `IF(KC.GT.1)THEN` |
| 반복·연직 혼합 | `G/hdmt.for:465` `CALL TIMEF(WT2TMP)` | `G/hdmt.for:461` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:463` `ELSE` |
| 반복·파랑 | `G/hdmt.for:475` `IF(ISWAVE.EQ.1) CALL WAVEBL` | `G/hdmt.for:474` `IF(ISTL.EQ.3)THEN` |
| 반복·파랑 | `G/hdmt.for:476` `IF(ISWAVE.EQ.2) CALL WAVESXY` | `G/hdmt.for:474` `IF(ISTL.EQ.3)THEN` |
| 반복·명시적 운동량 | `G/hdmt.for:487` `CALL TIMEF(WT1TMP)` | `G/hdmt.for:483` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:485` `ELSE` |
| 반복·명시적 운동량 | `G/hdmt.for:526` `IF(ISCDMA.LE.2) CALL CALEXP (ISTL)` | 외부 IF 블록 없음 |
| 반복·명시적 운동량 | `G/hdmt.for:529` `IF(ISCDMA.EQ.5) CALL CALEXP2 (ISTL)` | 외부 IF 블록 없음 |
| 반복·명시적 운동량 | `G/hdmt.for:530` `IF(ISCDMA.EQ.6) CALL CALEXP2 (ISTL)` | 외부 IF 블록 없음 |
| 반복·명시적 운동량 | `G/hdmt.for:531` `IF(ISCDMA.EQ.9) CALL CALEXP9 (ISTL)` | 외부 IF 블록 없음 |
| 반복·명시적 운동량 | `G/hdmt.for:538` `CALL TIMEF(WT2TMP)` | `G/hdmt.for:534` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:536` `ELSE` |
| 반복·시계열·동화 준비 | `G/hdmt.for:548` `CALL CALCSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmt.for:549` `CALL CALVEGSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmt.for:550` `CALL CALQVS (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmt.for:552` `IF(NPSER.GE.1) CALL CALPSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmt.for:561` `IF(ISWSEDA.GT.0.OR.ISUVDA.GT.0) CALL PUVDASM(ISTL,1)` | 외부 IF 블록 없음 |
| 반복·수면 응력 | `G/hdmt.for:582` `CALL CALTSXY` | `G/hdmt.for:570` `IF(ISCDMA.GE.3.AND.ISCDMA.LE.8)THEN`<br>`G/hdmt.for:571` `IF(ISTL.EQ.3)THEN` |
| 반복·외부모드 | `G/hdmt.for:609` `CALL TIMEF(WT1TMP)` | `G/hdmt.for:605` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:607` `ELSE` |
| 반복·외부모드 | `G/hdmt.for:649` `IF(ISCHAN.EQ.0.AND.ISDRY.EQ.0) CALL CALPUV9(ISTL)` | 외부 IF 블록 없음 |
| 반복·외부모드 | `G/hdmt.for:650` `IF(ISCHAN.GE.1.OR.ISDRY.GE.1) CALL CALPUV9C(ISTL)` | 외부 IF 블록 없음 |
| 반복·외부모드 | `G/hdmt.for:690` `CALL TIMEF(WT2TMP)` | `G/hdmt.for:686` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:688` `ELSE` |
| 반복·수면 응력 | `G/hdmt.for:762` `CALL CALTSXY` | `G/hdmt.for:750` `IF(ISCDMA.LE.2.OR.ISCDMA.GE.9)THEN`<br>`G/hdmt.for:751` `IF(ISTL.EQ.3)THEN` |
| 반복·내부모드 | `G/hdmt.for:786` `CALL TIMEF(WT1TMP)` | `G/hdmt.for:782` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:784` `ELSE` |
| 반복·내부모드 | `G/hdmt.for:789` `CALL CALUVW (ISTL,IS2TL)` | `G/hdmt.for:788` `IF(KC.GT.1)THEN` |
| 반복·내부모드 | `G/hdmt.for:802` `CALL CALUVW (ISTL,IS2TL)` | `G/hdmt.for:788` `IF(KC.GT.1)THEN`<br>`G/hdmt.for:790` `ELSE` |
| 반복·내부모드 | `G/hdmt.for:808` `CALL TIMEF(WT2TMP)` | `G/hdmt.for:804` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:806` `ELSE` |
| 반복·동화 진단 | `G/hdmt.for:820` `IF(ISWSEDA.GT.0.OR.ISUVDA.GT.0) CALL PUVDASM(ISTL,2)` | 외부 IF 블록 없음 |
| 반복·농도 | `G/hdmt.for:829` `CALL CALCONC (ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 반복·수질·부유생물 | `G/hdmt.for:1125` `IF(ISTRAN(8).GE.1) CALL WQ3D` | `G/hdmt.for:1023` `IF(ITMP.EQ.1)THEN`<br>`G/hdmt.for:1025` `IF(NTMP.EQ.0.AND.ISTL.EQ.3)THEN` |
| 반복·수질·부유생물 | `G/hdmt.for:1126` `IF(ISTRAN(4).GE.1) CALL CALSFT(2)` | `G/hdmt.for:1023` `IF(ITMP.EQ.1)THEN`<br>`G/hdmt.for:1025` `IF(NTMP.EQ.0.AND.ISTL.EQ.3)THEN` |
| 반복·부력 | `G/hdmt.for:1153` `CALL CALBUOY` | `G/hdmt.for:1152` `IF(BSC.GT.1.E-6)THEN` |
| 반복·중간 수지 | `G/hdmt.for:1163` `CALL CALBAL4` | `G/hdmt.for:1162` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN` |
| 반복·중간 수지 | `G/hdmt.for:1166` `CALL CBALEV4` | `G/hdmt.for:1162` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN`<br>`G/hdmt.for:1165` `IF(NTMP.EQ.0)THEN` |
| 반복·중간 수지 | `G/hdmt.for:1168` `CALL CBALOD4` | `G/hdmt.for:1162` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN`<br>`G/hdmt.for:1165` `IF(NTMP.EQ.0)THEN`<br>`G/hdmt.for:1167` `ELSE` |
| 반복·수평 혼합 | `G/hdmt.for:1197` `IF(ISTL.NE.2.AND.ISHDMF.GE.1) CALL CALHDMF` | 외부 IF 블록 없음 |
| 반복·바닥 응력 | `G/hdmt.for:1256` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 반복·난류 수송 | `G/hdmt.for:1370` `CALL TIMEF(WT1TMP)` | `G/hdmt.for:1366` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:1368` `ELSE` |
| 반복·난류 수송 | `G/hdmt.for:1374` `IF(ISTOPT(0).EQ.0)CALL CALQQ1OLD (ISTL)` | `G/hdmt.for:1372` `IF(KC.GT.1)THEN`<br>`G/hdmt.for:1373` `IF(ISQQ.EQ.1)THEN` |
| 반복·난류 수송 | `G/hdmt.for:1375` `IF(ISTOPT(0).GE.1)CALL CALQQ1 (ISTL)` | `G/hdmt.for:1372` `IF(KC.GT.1)THEN`<br>`G/hdmt.for:1373` `IF(ISQQ.EQ.1)THEN` |
| 반복·난류 수송 | `G/hdmt.for:1377` `IF(ISQQ.EQ.2) CALL CALQQ2 (ISTL)` | `G/hdmt.for:1372` `IF(KC.GT.1)THEN` |
| 반복·난류 수송 | `G/hdmt.for:1383` `CALL TIMEF(WT2TMP)` | `G/hdmt.for:1379` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:1381` `ELSE` |
| 반복·평균 수송·보정 판단 | `G/hdmt.for:1395` `IF(ISTL.EQ.3.AND.NTMP.EQ.0) CALL CALMMT` | `G/hdmt.for:1392` `IF(ISSSMMT.NE.2)THEN`<br>`G/hdmt.for:1393` `IF(ISICM.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1441` `CALL TMSR` | `G/hdmt.for:1438` `IF(ISTMSR.GE.1)THEN`<br>`G/hdmt.for:1440` `IF(NCTMSR.GE.NWTMSR)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1457` `CALL DUMP` | `G/hdmt.for:1454` `IF(ISDUMP.GE.1)THEN`<br>`G/hdmt.for:1455` `IF(TIME.GE.TSDUMP.AND.TIME.LE.TEDUMP)THEN`<br>`G/hdmt.for:1456` `IF(NCDUMP.GE.NSDUMP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1473` `CALL HYDOUT` | `G/hdmt.for:1470` `IF(IHYDOUT.GE.1)THEN`<br>`G/hdmt.for:1471` `IF(N.GE.NBTMSR.AND.N.LE.NSTMSR)THEN`<br>`G/hdmt.for:1472` `IF(NCHYDOUT.EQ.NWHYDOUT)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1518` `CALL VSFP` | `G/hdmt.for:1516` `IF(ISVSFP.EQ.1)THEN`<br>`G/hdmt.for:1517` `IF(N.GE.NBVSFP.AND.N.LE.NSVSFP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1527` `IF(ISICM.EQ.0) CALL CALMMT` | `G/hdmt.for:1526` `IF(ISSSMMT.NE.2)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1537` `IF(N.GE.NPDRT) CALL DRIFTER` | `G/hdmt.for:1536` `IF(ISPD.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1544` `CALL TIMEF(WT1TMP)` | `G/hdmt.for:1539` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt.for:1540` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:1542` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1547` `IF(N.GE.NLRPDRT(1)) CALL LAGRES` | `G/hdmt.for:1539` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt.for:1546` `IF(ISLRPD.LE.2)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1550` `IF(N.GE.NLRPDRT(1)) CALL GLMRES` | `G/hdmt.for:1539` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt.for:1549` `IF(ISLRPD.GE.3)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1556` `CALL TIMEF(WT2TMP)` | `G/hdmt.for:1539` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt.for:1552` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:1554` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1567` `CALL CALBAL5` | `G/hdmt.for:1566` `IF(ISBAL.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1570` `CALL CBALEV5` | `G/hdmt.for:1566` `IF(ISBAL.GE.1)THEN`<br>`G/hdmt.for:1569` `IF(NTMP.EQ.0)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1572` `CALL CBALOD5` | `G/hdmt.for:1566` `IF(ISBAL.GE.1)THEN`<br>`G/hdmt.for:1569` `IF(NTMP.EQ.0)THEN`<br>`G/hdmt.for:1571` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1579` `CALL BUDGET5` | `G/hdmt.for:1578` `IF(ISSBAL.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1600` `IF(ISDISP.EQ.2) CALL CALDISP2` | `G/hdmt.for:1599` `IF(N.GE.NDISP.AND.NCTBC.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1601` `IF(ISDISP.EQ.3) CALL CALDISP3` | `G/hdmt.for:1599` `IF(N.GE.NDISP.AND.NCTBC.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1609` `CALL LSQHARM` | `G/hdmt.for:1608` `IF(ISLSHA.EQ.1.AND.N.EQ.NCLSHA)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1621` `CALL OUTPUT1` | `G/hdmt.for:1619` `IF(NPRINT .EQ. NTSPP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1633` `CALL SURFPLT` | `G/hdmt.for:1632` `IF(N.GE.NCPPH.AND.ISPPH.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1642` `CALL VELPLTH` | `G/hdmt.for:1641` `IF(N.GE.NCVPH.AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1649` `CALL VELPLTV` | `G/hdmt.for:1648` `IF(N.GE.NCVPV.AND.ISVPV.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1664` `IF(ISTRAN(1).GE.1) CALL SALPLTH (1,SAL)` | `G/hdmt.for:1663` `IF(N.GE.NCSPH(1).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1671` `IF(ISTRAN(2).GE.1) CALL SALPLTH (2,TEM)` | `G/hdmt.for:1670` `IF(N.GE.NCSPH(2).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1678` `IF(ISTRAN(3).GE.1) CALL SALPLTH (3,DYE)` | `G/hdmt.for:1677` `IF(N.GE.NCSPH(3).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1685` `IF(ISTRAN(4).GE.1) CALL SALPLTH (4,SFL)` | `G/hdmt.for:1684` `IF(N.GE.NCSPH(4).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1692` `IF(ISTRAN(5).GE.1) CALL SALPLTH (5,TVAR1S)` | `G/hdmt.for:1691` `IF(N.GE.NCSPH(5).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1699` `IF(ISTRAN(6).GE.1) CALL SALPLTH (6,SEDT)` | `G/hdmt.for:1698` `IF(N.GE.NCSPH(6).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1706` `IF(ISTRAN(7).GE.1) CALL SALPLTH (7,SNDT)` | `G/hdmt.for:1705` `IF(N.GE.NCSPH(7).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1713` `CALL SALPLTV(ITMP)` | `G/hdmt.for:1712` `IF(N.GE.NCSPV(ITMP).AND.ISSPV(ITMP).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1723` `CALL EE_LINKAGE(0)` | `G/hdmt.for:1721` `IF(ISSPH(8).EQ.1.OR.ISBEXP.EQ.1)THEN`<br>`G/hdmt.for:1722` `IF(N.GE.NCSPH(8))THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1735` `CALL OUT3D` | `G/hdmt.for:1734` `IF(N.EQ.NC3DO.AND.IS3DO.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1747` `CALL RESTOUT(0)` | `G/hdmt.for:1743` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmt.for:1746` `IF(ISSREST.EQ.0)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1749` `IF(IWQRST.EQ.1) CALL WWQRST` | `G/hdmt.for:1743` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmt.for:1746` `IF(ISSREST.EQ.0)THEN`<br>`G/hdmt.for:1748` `IF(ISTRAN(8).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1750` `IF(IWQBEN.EQ.1 .AND. ISMRST.EQ.1) CALL WSMRST` | `G/hdmt.for:1743` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmt.for:1746` `IF(ISSREST.EQ.0)THEN`<br>`G/hdmt.for:1748` `IF(ISTRAN(8).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1763` `CALL TIMELOG(N,TIMEDAY)` | `G/hdmt.for:1762` `IF(NTIMER.EQ.NTSPTC)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1774` `IF(ISHOW.EQ.1) CALL SHOWVAL1` | 외부 IF 블록 없음 |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1775` `IF(ISHOW.EQ.2) CALL SHOWVAL2` | 외부 IF 블록 없음 |
| 반복·잔류 수송·진단·출력 | `G/hdmt.for:1776` `IF(ISHOW.EQ.3) CALL SHOWVAL3` | 외부 IF 블록 없음 |
| 종료 | `G/hdmt.for:1790` `CALL TIMEF(WT2TMP)` | `G/hdmt.for:1786` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt.for:1788` `ELSE` |
| 종료 | `G/hdmt.for:1852` `CALL OUTPUT2` | 외부 IF 블록 없음 |
| 종료 | `G/hdmt.for:1859` `CALL RESTOUT(0)` | `G/hdmt.for:1858` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN` |
| 종료 | `G/hdmt.for:1861` `IF(IWQRST.EQ.1) CALL WWQRST` | `G/hdmt.for:1858` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN`<br>`G/hdmt.for:1860` `IF(ISTRAN(8).GE.1)THEN` |
| 종료 | `G/hdmt.for:1862` `IF(IWQBEN.EQ.1 .AND. ISMRST.EQ.1) CALL WSMRST` | `G/hdmt.for:1858` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN`<br>`G/hdmt.for:1860` `IF(ISTRAN(8).GE.1)THEN` |
| 종료 | `G/hdmt.for:1866` `CALL RESTMOD` | `G/hdmt.for:1865` `IF(ISRESTO.EQ.-2)THEN` |
| 종료 | `G/hdmt.for:1874` `IF(ISLSHA.EQ.1) CALL LSQHARM` | 외부 IF 블록 없음 |

#### HDMTGVC

| 구간 | 직접 호출문 위치와 원문 | 외부 IF 분기 원문 |
|---|---|---|
| 초기화 | `G/hdmtgvc.for:34` `CALL TIMEF(WTTMP)` | `G/hdmtgvc.for:30` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:32` `ELSE` |
| 초기화 | `G/hdmtgvc.for:97` `IF(ISWAVE.EQ.1) CALL WAVEBL` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmtgvc.for:98` `IF(ISWAVE.EQ.2) CALL WAVESXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmtgvc.for:109` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmtgvc.for:115` `IF(ISHDMF.GE.1) CALL CALHDMF` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmtgvc.for:124` `CALL CALTSXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmtgvc.for:159` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmtgvc.for:192` `CALL CALTSXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmtgvc.for:343` `CALL TIMELOG(N,TIMEDAY)` | 외부 IF 블록 없음 |
| 반복·초기 수지 | `G/hdmtgvc.for:398` `CALL CALBAL1` | `G/hdmtgvc.for:395` `IF(IS2TIM.EQ.0) THEN`<br>`G/hdmtgvc.for:397` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN` |
| 반복·초기 수지 | `G/hdmtgvc.for:401` `CALL CBALEV1` | `G/hdmtgvc.for:395` `IF(IS2TIM.EQ.0) THEN`<br>`G/hdmtgvc.for:397` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN`<br>`G/hdmtgvc.for:400` `IF(NTMP.EQ.0)THEN` |
| 반복·초기 수지 | `G/hdmtgvc.for:403` `CALL CBALOD1` | `G/hdmtgvc.for:395` `IF(IS2TIM.EQ.0) THEN`<br>`G/hdmtgvc.for:397` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN`<br>`G/hdmtgvc.for:400` `IF(NTMP.EQ.0)THEN`<br>`G/hdmtgvc.for:402` `ELSE` |
| 반복·초기 수지 | `G/hdmtgvc.for:410` `CALL BUDGET1` | `G/hdmtgvc.for:395` `IF(IS2TIM.EQ.0) THEN`<br>`G/hdmtgvc.for:409` `IF(NCTBC.NE.NTSTBC.AND.ISSBAL.GE.1)THEN` |
| 반복·연직 혼합 | `G/hdmtgvc.for:435` `CALL TIMEF(WT1TMP)` | `G/hdmtgvc.for:431` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:433` `ELSE` |
| 반복·연직 혼합 | `G/hdmtgvc.for:439` `IF(ISTOPT(0).EQ.0)CALL CALAVBOLD (ISTL)` | `G/hdmtgvc.for:437` `IF(KC.GT.1)THEN`<br>`G/hdmtgvc.for:438` `IF(ISQQ.EQ.1)THEN` |
| 반복·연직 혼합 | `G/hdmtgvc.for:443` `IF(ISTOPT(0).GE.1)CALL CALAVBGVC (ISTL)` | `G/hdmtgvc.for:437` `IF(KC.GT.1)THEN`<br>`G/hdmtgvc.for:438` `IF(ISQQ.EQ.1)THEN` |
| 반복·연직 혼합 | `G/hdmtgvc.for:445` `IF(ISQQ.EQ.2) CALL CALAVB2 (ISTL)` | `G/hdmtgvc.for:437` `IF(KC.GT.1)THEN` |
| 반복·연직 혼합 | `G/hdmtgvc.for:451` `CALL TIMEF(WT2TMP)` | `G/hdmtgvc.for:447` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:449` `ELSE` |
| 반복·파랑 | `G/hdmtgvc.for:461` `IF(ISWAVE.EQ.1) CALL WAVEBL` | `G/hdmtgvc.for:460` `IF(ISTL.EQ.3)THEN` |
| 반복·파랑 | `G/hdmtgvc.for:462` `IF(ISWAVE.EQ.2) CALL WAVESXY` | `G/hdmtgvc.for:460` `IF(ISTL.EQ.3)THEN` |
| 반복·명시적 운동량 | `G/hdmtgvc.for:473` `CALL TIMEF(WT1TMP)` | `G/hdmtgvc.for:469` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:471` `ELSE` |
| 반복·명시적 운동량 | `G/hdmtgvc.for:515` `IF(ISCDMA.LE.2) CALL CALEXPGVC (ISTL)` | 외부 IF 블록 없음 |
| 반복·명시적 운동량 | `G/hdmtgvc.for:518` `IF(ISCDMA.EQ.5) CALL CALEXP2 (ISTL)` | 외부 IF 블록 없음 |
| 반복·명시적 운동량 | `G/hdmtgvc.for:519` `IF(ISCDMA.EQ.6) CALL CALEXP2 (ISTL)` | 외부 IF 블록 없음 |
| 반복·명시적 운동량 | `G/hdmtgvc.for:520` `IF(ISCDMA.EQ.9) CALL CALEXP9 (ISTL)` | 외부 IF 블록 없음 |
| 반복·명시적 운동량 | `G/hdmtgvc.for:527` `CALL TIMEF(WT2TMP)` | `G/hdmtgvc.for:523` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:525` `ELSE` |
| 반복·시계열·동화 준비 | `G/hdmtgvc.for:537` `CALL CALCSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmtgvc.for:538` `CALL CALVEGSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmtgvc.for:539` `CALL CALQVS (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmtgvc.for:541` `IF(NPSER.GE.1) CALL CALPSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmtgvc.for:550` `IF(ISWSEDA.GT.0.OR.ISUVDA.GT.0) CALL PUVDASM(ISTL,1)` | 외부 IF 블록 없음 |
| 반복·수면 응력 | `G/hdmtgvc.for:567` `CALL CALTSXY` | `G/hdmtgvc.for:559` `IF(ISCDMA.GE.3.AND.ISCDMA.LE.8)THEN`<br>`G/hdmtgvc.for:560` `IF(ISTL.EQ.3)THEN` |
| 반복·외부모드 | `G/hdmtgvc.for:590` `CALL TIMEF(WT1TMP)` | `G/hdmtgvc.for:586` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:588` `ELSE` |
| 반복·외부모드 | `G/hdmtgvc.for:633` `IF(ISCHAN.EQ.0.AND.ISDRY.EQ.0) CALL CALPUV9GVC(ISTL)` | 외부 IF 블록 없음 |
| 반복·외부모드 | `G/hdmtgvc.for:634` `IF(ISCHAN.GE.1.OR.ISDRY.GE.1) CALL CALPUV9C(ISTL)` | 외부 IF 블록 없음 |
| 반복·외부모드 | `G/hdmtgvc.for:674` `CALL TIMEF(WT2TMP)` | `G/hdmtgvc.for:670` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:672` `ELSE` |
| 반복·수면 응력 | `G/hdmtgvc.for:742` `CALL CALTSXY` | `G/hdmtgvc.for:734` `IF(ISCDMA.LE.2.OR.ISCDMA.GE.9)THEN`<br>`G/hdmtgvc.for:735` `IF(ISTL.EQ.3)THEN` |
| 반복·내부모드 | `G/hdmtgvc.for:762` `CALL TIMEF(WT1TMP)` | `G/hdmtgvc.for:758` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:760` `ELSE` |
| 반복·내부모드 | `G/hdmtgvc.for:768` `CALL CALUVWGVC (ISTL,IS2TL)` | `G/hdmtgvc.for:764` `IF(KC.GT.1)THEN` |
| 반복·내부모드 | `G/hdmtgvc.for:780` `CALL CALUVWGVC (ISTL,IS2TL)` | `G/hdmtgvc.for:764` `IF(KC.GT.1)THEN`<br>`G/hdmtgvc.for:769` `ELSE` |
| 반복·내부모드 | `G/hdmtgvc.for:786` `CALL TIMEF(WT2TMP)` | `G/hdmtgvc.for:782` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:784` `ELSE` |
| 반복·동화 진단 | `G/hdmtgvc.for:799` `IF(ISWSEDA.GT.0.OR.ISUVDA.GT.0) CALL PUVDASM(ISTL,2)` | 외부 IF 블록 없음 |
| 반복·농도 | `G/hdmtgvc.for:811` `CALL CALCONCGVC (ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 반복·수질·부유생물 | `G/hdmtgvc.for:1171` `IF(ISTRAN(8).GE.1) CALL WQ3D` | `G/hdmtgvc.for:1005` `IF(ITMP.EQ.1)THEN`<br>`G/hdmtgvc.for:1007` `IF(NTMP.EQ.0.AND.ISTL.EQ.3)THEN` |
| 반복·수질·부유생물 | `G/hdmtgvc.for:1172` `IF(ISTRAN(4).GE.1) CALL CALSFT(2)` | `G/hdmtgvc.for:1005` `IF(ITMP.EQ.1)THEN`<br>`G/hdmtgvc.for:1007` `IF(NTMP.EQ.0.AND.ISTL.EQ.3)THEN` |
| 반복·부력 | `G/hdmtgvc.for:1197` `CALL CALBUOY` | `G/hdmtgvc.for:1196` `IF(BSC.GT.1.E-6)THEN` |
| 반복·중간 수지 | `G/hdmtgvc.for:1207` `CALL CALBAL4` | `G/hdmtgvc.for:1206` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN` |
| 반복·중간 수지 | `G/hdmtgvc.for:1210` `CALL CBALEV4` | `G/hdmtgvc.for:1206` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN`<br>`G/hdmtgvc.for:1209` `IF(NTMP.EQ.0)THEN` |
| 반복·중간 수지 | `G/hdmtgvc.for:1212` `CALL CBALOD4` | `G/hdmtgvc.for:1206` `IF(NCTBC.NE.NTSTBC.AND.ISBAL.GE.1)THEN`<br>`G/hdmtgvc.for:1209` `IF(NTMP.EQ.0)THEN`<br>`G/hdmtgvc.for:1211` `ELSE` |
| 반복·수평 혼합 | `G/hdmtgvc.for:1245` `IF(ISTL.NE.2.AND.ISHDMF.GE.1) CALL CALHDMF` | 외부 IF 블록 없음 |
| 반복·바닥 응력 | `G/hdmtgvc.for:1307` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 반복·난류 수송 | `G/hdmtgvc.for:1429` `CALL TIMEF(WT1TMP)` | `G/hdmtgvc.for:1425` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:1427` `ELSE` |
| 반복·난류 수송 | `G/hdmtgvc.for:1433` `IF(ISTOPT(0).EQ.0)CALL CALQQ1OLD (ISTL)` | `G/hdmtgvc.for:1431` `IF(KC.GT.1)THEN`<br>`G/hdmtgvc.for:1432` `IF(ISQQ.EQ.1)THEN` |
| 반복·난류 수송 | `G/hdmtgvc.for:1437` `IF(ISTOPT(0).GE.1)CALL CALQQ1GVC (ISTL)` | `G/hdmtgvc.for:1431` `IF(KC.GT.1)THEN`<br>`G/hdmtgvc.for:1432` `IF(ISQQ.EQ.1)THEN` |
| 반복·난류 수송 | `G/hdmtgvc.for:1439` `IF(ISQQ.EQ.2) CALL CALQQ2 (ISTL)` | `G/hdmtgvc.for:1431` `IF(KC.GT.1)THEN` |
| 반복·난류 수송 | `G/hdmtgvc.for:1445` `CALL TIMEF(WT2TMP)` | `G/hdmtgvc.for:1441` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:1443` `ELSE` |
| 반복·평균 수송·보정 판단 | `G/hdmtgvc.for:1457` `IF(ISTL.EQ.3.AND.NTMP.EQ.0) CALL CALMMT` | `G/hdmtgvc.for:1454` `IF(ISSSMMT.NE.2)THEN`<br>`G/hdmtgvc.for:1455` `IF(ISICM.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1503` `CALL TMSR` | `G/hdmtgvc.for:1500` `IF(ISTMSR.GE.1)THEN`<br>`G/hdmtgvc.for:1502` `IF(NCTMSR.GE.NWTMSR)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1519` `CALL DUMP` | `G/hdmtgvc.for:1516` `IF(ISDUMP.GE.1)THEN`<br>`G/hdmtgvc.for:1517` `IF(TIME.GE.TSDUMP.AND.TIME.LE.TEDUMP)THEN`<br>`G/hdmtgvc.for:1518` `IF(NCDUMP.GE.NSDUMP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1535` `CALL HYDOUT` | `G/hdmtgvc.for:1532` `IF(IHYDOUT.GE.1)THEN`<br>`G/hdmtgvc.for:1533` `IF(N.GE.NBTMSR.AND.N.LE.NSTMSR)THEN`<br>`G/hdmtgvc.for:1534` `IF(NCHYDOUT.EQ.NWHYDOUT)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1580` `CALL VSFP` | `G/hdmtgvc.for:1578` `IF(ISVSFP.EQ.1)THEN`<br>`G/hdmtgvc.for:1579` `IF(N.GE.NBVSFP.AND.N.LE.NSVSFP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1589` `IF(ISICM.EQ.0) CALL CALMMT` | `G/hdmtgvc.for:1588` `IF(ISSSMMT.NE.2)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1599` `IF(N.GE.NPDRT) CALL DRIFTER` | `G/hdmtgvc.for:1598` `IF(ISPD.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1606` `CALL TIMEF(WT1TMP)` | `G/hdmtgvc.for:1601` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmtgvc.for:1602` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:1604` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1609` `IF(N.GE.NLRPDRT(1)) CALL LAGRES` | `G/hdmtgvc.for:1601` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmtgvc.for:1608` `IF(ISLRPD.LE.2)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1612` `IF(N.GE.NLRPDRT(1)) CALL GLMRES` | `G/hdmtgvc.for:1601` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmtgvc.for:1611` `IF(ISLRPD.GE.3)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1618` `CALL TIMEF(WT2TMP)` | `G/hdmtgvc.for:1601` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmtgvc.for:1614` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:1616` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1629` `CALL CALBAL5` | `G/hdmtgvc.for:1628` `IF(ISBAL.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1632` `CALL CBALEV5` | `G/hdmtgvc.for:1628` `IF(ISBAL.GE.1)THEN`<br>`G/hdmtgvc.for:1631` `IF(NTMP.EQ.0)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1634` `CALL CBALOD5` | `G/hdmtgvc.for:1628` `IF(ISBAL.GE.1)THEN`<br>`G/hdmtgvc.for:1631` `IF(NTMP.EQ.0)THEN`<br>`G/hdmtgvc.for:1633` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1641` `CALL BUDGET5` | `G/hdmtgvc.for:1640` `IF(ISSBAL.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1662` `IF(ISDISP.EQ.2) CALL CALDISP2` | `G/hdmtgvc.for:1661` `IF(N.GE.NDISP.AND.NCTBC.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1663` `IF(ISDISP.EQ.3) CALL CALDISP3` | `G/hdmtgvc.for:1661` `IF(N.GE.NDISP.AND.NCTBC.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1671` `CALL LSQHARM` | `G/hdmtgvc.for:1670` `IF(ISLSHA.EQ.1.AND.N.EQ.NCLSHA)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1683` `CALL OUTPUT1` | `G/hdmtgvc.for:1681` `IF(NPRINT .EQ. NTSPP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1695` `CALL SURFPLT` | `G/hdmtgvc.for:1694` `IF(N.GE.NCPPH.AND.ISPPH.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1704` `CALL VELPLTH` | `G/hdmtgvc.for:1703` `IF(N.GE.NCVPH.AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1711` `CALL VELPLTV` | `G/hdmtgvc.for:1710` `IF(N.GE.NCVPV.AND.ISVPV.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1726` `IF(ISTRAN(1).GE.1) CALL SALPLTH (1,SAL)` | `G/hdmtgvc.for:1725` `IF(N.GE.NCSPH(1).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1733` `IF(ISTRAN(2).GE.1) CALL SALPLTH (2,TEM)` | `G/hdmtgvc.for:1732` `IF(N.GE.NCSPH(2).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1740` `IF(ISTRAN(3).GE.1) CALL SALPLTH (3,DYE)` | `G/hdmtgvc.for:1739` `IF(N.GE.NCSPH(3).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1747` `IF(ISTRAN(4).GE.1) CALL SALPLTH (4,SFL)` | `G/hdmtgvc.for:1746` `IF(N.GE.NCSPH(4).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1754` `IF(ISTRAN(5).GE.1) CALL SALPLTH (5,TVAR1S)` | `G/hdmtgvc.for:1753` `IF(N.GE.NCSPH(5).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1761` `IF(ISTRAN(6).GE.1) CALL SALPLTH (6,SEDT)` | `G/hdmtgvc.for:1760` `IF(N.GE.NCSPH(6).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1768` `IF(ISTRAN(7).GE.1) CALL SALPLTH (7,SNDT)` | `G/hdmtgvc.for:1767` `IF(N.GE.NCSPH(7).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1775` `CALL SALPLTV(ITMP)` | `G/hdmtgvc.for:1774` `IF(N.GE.NCSPV(ITMP).AND.ISSPV(ITMP).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1787` `CALL EE_LINKAGE(0)` | `G/hdmtgvc.for:1785` `IF(ISSPH(8).EQ.1.OR.ISBEXP.EQ.1)THEN`<br>`G/hdmtgvc.for:1786` `IF(N.GE.NCSPH(8))THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1799` `CALL OUT3D` | `G/hdmtgvc.for:1798` `IF(N.EQ.NC3DO.AND.IS3DO.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1811` `CALL RESTOUT(0)` | `G/hdmtgvc.for:1807` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmtgvc.for:1810` `IF(ISSREST.EQ.0)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1813` `IF(IWQRST.EQ.1) CALL WWQRST` | `G/hdmtgvc.for:1807` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmtgvc.for:1810` `IF(ISSREST.EQ.0)THEN`<br>`G/hdmtgvc.for:1812` `IF(ISTRAN(8).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1814` `IF(IWQBEN.EQ.1 .AND. ISMRST.EQ.1) CALL WSMRST` | `G/hdmtgvc.for:1807` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmtgvc.for:1810` `IF(ISSREST.EQ.0)THEN`<br>`G/hdmtgvc.for:1812` `IF(ISTRAN(8).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1827` `CALL TIMELOG(N,TIMEDAY)` | `G/hdmtgvc.for:1826` `IF(NTIMER.EQ.NTSPTC)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1840` `IF(ISHOW.EQ.1) CALL SHOWVAL1` | 외부 IF 블록 없음 |
| 반복·잔류 수송·진단·출력 | `G/hdmtgvc.for:1841` `IF(ISHOW.EQ.2) CALL SHOWVAL2` | 외부 IF 블록 없음 |
| 종료 | `G/hdmtgvc.for:1855` `CALL TIMEF(WT2TMP)` | `G/hdmtgvc.for:1851` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmtgvc.for:1853` `ELSE` |
| 종료 | `G/hdmtgvc.for:1917` `CALL OUTPUT2` | 외부 IF 블록 없음 |
| 종료 | `G/hdmtgvc.for:1924` `CALL RESTOUT(0)` | `G/hdmtgvc.for:1923` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN` |
| 종료 | `G/hdmtgvc.for:1926` `IF(IWQRST.EQ.1) CALL WWQRST` | `G/hdmtgvc.for:1923` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN`<br>`G/hdmtgvc.for:1925` `IF(ISTRAN(8).GE.1)THEN` |
| 종료 | `G/hdmtgvc.for:1927` `IF(IWQBEN.EQ.1 .AND. ISMRST.EQ.1) CALL WSMRST` | `G/hdmtgvc.for:1923` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN`<br>`G/hdmtgvc.for:1925` `IF(ISTRAN(8).GE.1)THEN` |
| 종료 | `G/hdmtgvc.for:1931` `CALL RESTMOD` | `G/hdmtgvc.for:1930` `IF(ISRESTO.EQ.-2)THEN` |
| 종료 | `G/hdmtgvc.for:1939` `IF(ISLSHA.EQ.1) CALL LSQHARM` | 외부 IF 블록 없음 |

#### HDMT2T

`HDMT2T`의 `ISTL=3` 조건부 `CALMMT` 문은 소스에 남아 있다. 루틴의 활성 대입문은 `ISTL=2`를 유지한다. 따라서 이 호출문을 보통의 2시점 반복에서 실행하는 평균 수송 호출로 해석하지 않는다. 근거는 `G/hdmt2t.for:472` `ISTL=2`, `G/hdmt2t.for:1559` `IF(ISTL.EQ.3.AND.NTMP.EQ.0) CALL CALMMT`, `G/hdmt2t.for:1583` `C2T       ISTL=3`이다. 마지막 근거는 `C2T`로 시작하는 주석이다.

| 구간 | 직접 호출문 위치와 원문 | 외부 IF 분기 원문 |
|---|---|---|
| 초기화 | `G/hdmt2t.for:40` `CALL TIMEF(WTTMP)` | `G/hdmt2t.for:36` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:38` `ELSE` |
| 초기화 | `G/hdmt2t.for:142` `IF(ISWAVE.EQ.1) CALL WAVEBL` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt2t.for:143` `IF(ISWAVE.EQ.2) CALL WAVESXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt2t.for:149` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt2t.for:155` `IF(ISHDMF.GE.1) CALL CALHDMF` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt2t.for:164` `CALL CALTSXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt2t.for:179` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt2t.for:195` `CALL CALTSXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt2t.for:495` `CALL TIMELOG(N,TIMEDAY)` | 외부 IF 블록 없음 |
| 반복·시간간격 | `G/hdmt2t.for:519` `CALL CALSTEP` | `G/hdmt2t.for:511` `IF(ISDYNSTP.EQ.0)THEN`<br>`G/hdmt2t.for:517` `ELSE`<br>`G/hdmt2t.for:518` `IF(IDRYTBP.EQ.0)THEN` |
| 반복·시간간격 | `G/hdmt2t.for:521` `CALL CALSTEPD` | `G/hdmt2t.for:511` `IF(ISDYNSTP.EQ.0)THEN`<br>`G/hdmt2t.for:517` `ELSE`<br>`G/hdmt2t.for:518` `IF(IDRYTBP.EQ.0)THEN`<br>`G/hdmt2t.for:520` `ELSE` |
| 반복·초기 수지 | `G/hdmt2t.for:597` `CALL BAL2T1` | `G/hdmt2t.for:595` `IF(IS2TIM.GE.1) THEN`<br>`G/hdmt2t.for:596` `IF(ISBAL.GE.1)THEN` |
| 반복·연직 혼합 | `G/hdmt2t.for:615` `CALL TIMEF(WT1TMP)` | `G/hdmt2t.for:611` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:613` `ELSE` |
| 반복·연직 혼합 | `G/hdmt2t.for:619` `IF(ISTOPT(0).EQ.0)CALL CALAVBOLD (ISTL)` | `G/hdmt2t.for:617` `IF(KC.GT.1)THEN`<br>`G/hdmt2t.for:618` `IF(ISQQ.EQ.1)THEN` |
| 반복·연직 혼합 | `G/hdmt2t.for:620` `IF(ISTOPT(0).GE.1)CALL CALAVB (ISTL)` | `G/hdmt2t.for:617` `IF(KC.GT.1)THEN`<br>`G/hdmt2t.for:618` `IF(ISQQ.EQ.1)THEN` |
| 반복·연직 혼합 | `G/hdmt2t.for:622` `IF(ISQQ.EQ.2) CALL CALAVB2 (ISTL)` | `G/hdmt2t.for:617` `IF(KC.GT.1)THEN` |
| 반복·연직 혼합 | `G/hdmt2t.for:628` `CALL TIMEF(WT2TMP)` | `G/hdmt2t.for:624` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:626` `ELSE` |
| 반복·파랑 | `G/hdmt2t.for:637` `IF(ISWAVE.EQ.1) CALL WAVEBL` | 외부 IF 블록 없음 |
| 반복·파랑 | `G/hdmt2t.for:638` `IF(ISWAVE.EQ.2) CALL WAVESXY` | 외부 IF 블록 없음 |
| 반복·운동량 | `G/hdmt2t.for:648` `CALL TIMEF(WT1TMP)` | `G/hdmt2t.for:644` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:646` `ELSE` |
| 반복·운동량 | `G/hdmt2t.for:651` `IF(IS2TIM.EQ.1) CALL CALEXP2T` | 외부 IF 블록 없음 |
| 반복·운동량 | `G/hdmt2t.for:652` `IF(IS2TIM.EQ.2) CALL CALIMP2T` | 외부 IF 블록 없음 |
| 반복·운동량 | `G/hdmt2t.for:658` `CALL TIMEF(WT2TMP)` | `G/hdmt2t.for:654` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:656` `ELSE` |
| 반복·시계열·동화 준비 | `G/hdmt2t.for:668` `CALL CALCSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmt2t.for:669` `CALL CALVEGSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmt2t.for:670` `CALL CALQVS (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmt2t.for:672` `IF(NPSER.GE.1) CALL CALPSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열·동화 준비 | `G/hdmt2t.for:681` `IF(ISWSEDA.GT.0.OR.ISUVDA.GT.0) CALL PUVDASM(ISTL,1)` | 외부 IF 블록 없음 |
| 반복·수면 응력 | `G/hdmt2t.for:698` `CALL CALTSXY` | `G/hdmt2t.for:690` `IF(ISCDMA.GE.3.AND.ISCDMA.LE.8)THEN` |
| 반복·외부모드 | `G/hdmt2t.for:721` `CALL TIMEF(WT1TMP)` | `G/hdmt2t.for:717` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:719` `ELSE` |
| 반복·외부모드 | `G/hdmt2t.for:724` `IF(ISCHAN.EQ.0.AND.ISDRY.EQ.0) CALL CALPUV2T` | 외부 IF 블록 없음 |
| 반복·외부모드 | `G/hdmt2t.for:725` `IF(ISCHAN.GE.1.OR.ISDRY.GE.1) CALL CALPUV2C` | 외부 IF 블록 없음 |
| 반복·외부모드 | `G/hdmt2t.for:731` `CALL TIMEF(WT2TMP)` | `G/hdmt2t.for:727` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:729` `ELSE` |
| 반복·수면 응력 | `G/hdmt2t.for:799` `CALL CALTSXY` | `G/hdmt2t.for:791` `IF(ISCDMA.LE.2.OR.ISCDMA.GE.9)THEN` |
| 반복·내부모드 | `G/hdmt2t.for:819` `CALL TIMEF(WT1TMP)` | `G/hdmt2t.for:815` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:817` `ELSE` |
| 반복·내부모드 | `G/hdmt2t.for:823` `CALL CALUVW (ISTL,IS2TL)` | `G/hdmt2t.for:822` `IF(KC.GT.1)THEN` |
| 반복·내부모드 | `G/hdmt2t.for:832` `CALL CALUVW (ISTL,IS2TL)` | `G/hdmt2t.for:822` `IF(KC.GT.1)THEN`<br>`G/hdmt2t.for:824` `ELSE` |
| 반복·내부모드 | `G/hdmt2t.for:839` `CALL TIMEF(WT2TMP)` | `G/hdmt2t.for:835` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:837` `ELSE` |
| 반복·동화 진단 | `G/hdmt2t.for:851` `IF(ISWSEDA.GT.0.OR.ISUVDA.GT.0) CALL PUVDASM(ISTL,2)` | 외부 IF 블록 없음 |
| 반복·농도 | `G/hdmt2t.for:860` `CALL CALCONC (ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 반복·수질·부유생물 | `G/hdmt2t.for:1105` `IF(ISTRAN(8).GE.1) CALL WQ3D` | `G/hdmt2t.for:1052` `IF(ISTRAN(4).GE.1.OR.ISTRAN(8).GE.1)THEN` |
| 반복·수질·부유생물 | `G/hdmt2t.for:1106` `IF(ISTRAN(4).GE.1) CALL CALSFT(2)` | `G/hdmt2t.for:1052` `IF(ISTRAN(4).GE.1.OR.ISTRAN(8).GE.1)THEN` |
| 반복·부력 | `G/hdmt2t.for:1129` `CALL CALBUOY` | `G/hdmt2t.for:1128` `IF(BSC.GT.1.E-6)THEN` |
| 반복·중간 수지 | `G/hdmt2t.for:1152` `CALL BAL2T4` | `G/hdmt2t.for:1150` `IF(IS2TIM.GE.1) THEN`<br>`G/hdmt2t.for:1151` `IF(ISBAL.GE.1)THEN` |
| 반복·수평 혼합 | `G/hdmt2t.for:1184` `IF(ISHDMF.GE.1) CALL CALHDMF` | 외부 IF 블록 없음 |
| 반복·바닥 응력 | `G/hdmt2t.for:1239` `CALL TIMEF(WT1TMP)` | `G/hdmt2t.for:1235` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:1237` `ELSE` |
| 반복·바닥 응력 | `G/hdmt2t.for:1242` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 반복·바닥 응력 | `G/hdmt2t.for:1519` `CALL TIMEF(WT2TMP)` | `G/hdmt2t.for:1515` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:1517` `ELSE` |
| 반복·난류 수송 | `G/hdmt2t.for:1534` `CALL TIMEF(WT1TMP)` | `G/hdmt2t.for:1530` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:1532` `ELSE` |
| 반복·난류 수송 | `G/hdmt2t.for:1538` `IF(ISTOPT(0).EQ.0)CALL CALQQ2TOLD (ISTL)` | `G/hdmt2t.for:1536` `IF(KC.GT.1)THEN`<br>`G/hdmt2t.for:1537` `IF(ISQQ.EQ.1)THEN` |
| 반복·난류 수송 | `G/hdmt2t.for:1539` `IF(ISTOPT(0).GE.1)CALL CALQQ2T (ISTL)` | `G/hdmt2t.for:1536` `IF(KC.GT.1)THEN`<br>`G/hdmt2t.for:1537` `IF(ISQQ.EQ.1)THEN` |
| 반복·난류 수송 | `G/hdmt2t.for:1541` `IF(ISQQ.EQ.2) CALL CALQQ2 (ISTL)` | `G/hdmt2t.for:1536` `IF(KC.GT.1)THEN` |
| 반복·난류 수송 | `G/hdmt2t.for:1547` `CALL TIMEF(WT2TMP)` | `G/hdmt2t.for:1543` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:1545` `ELSE` |
| 반복·평균 수송·보정 주석 | `G/hdmt2t.for:1559` `IF(ISTL.EQ.3.AND.NTMP.EQ.0) CALL CALMMT` | `G/hdmt2t.for:1556` `IF(ISSSMMT.NE.2)THEN`<br>`G/hdmt2t.for:1557` `IF(ISICM.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1618` `CALL TMSR` | `G/hdmt2t.for:1615` `IF(ISTMSR.GE.1)THEN`<br>`G/hdmt2t.for:1617` `IF(NCTMSR.GE.NWTMSR)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1636` `CALL DUMP` | `G/hdmt2t.for:1632` `IF(ISDUMP.GE.1)THEN`<br>`G/hdmt2t.for:1633` `IF(TIME.GE.TSDUMP.AND.TIME.LE.TEDUMP)THEN`<br>`G/hdmt2t.for:1635` `IF(NCDUMP.GE.NSDUMP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1655` `CALL TOXALL` | `G/hdmt2t.for:1652` `IF(ISTOXALL.EQ.1)THEN`<br>`G/hdmt2t.for:1654` `IF(N.GE.MSTOXALL)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1668` `CALL HYDOUT` | `G/hdmt2t.for:1665` `IF(IHYDOUT.GE.1)THEN`<br>`G/hdmt2t.for:1666` `IF(N.GE.NBTMSR.AND.N.LE.NSTMSR)THEN`<br>`G/hdmt2t.for:1667` `IF(NCHYDOUT.EQ.NWHYDOUT)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1716` `CALL VSFP` | `G/hdmt2t.for:1714` `IF(ISVSFP.EQ.1)THEN`<br>`G/hdmt2t.for:1715` `IF(N.GE.NBVSFP.AND.N.LE.NSVSFP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1725` `IF(ISICM.EQ.0) CALL CALMMT` | `G/hdmt2t.for:1724` `IF(ISSSMMT.NE.2)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1735` `IF(N.GE.NPDRT) CALL DRIFTER` | `G/hdmt2t.for:1734` `IF(ISPD.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1742` `CALL TIMEF(WT1TMP)` | `G/hdmt2t.for:1737` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt2t.for:1738` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:1740` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1745` `IF(N.GE.NLRPDRT(1)) CALL LAGRES` | `G/hdmt2t.for:1737` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt2t.for:1744` `IF(ISLRPD.LE.2)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1748` `IF(N.GE.NLRPDRT(1)) CALL GLMRES` | `G/hdmt2t.for:1737` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt2t.for:1747` `IF(ISLRPD.GE.3)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1754` `CALL TIMEF(WT2TMP)` | `G/hdmt2t.for:1737` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt2t.for:1750` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:1752` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1790` `CALL BAL2T5` | `G/hdmt2t.for:1788` `IF(IS2TIM.GE.1) THEN`<br>`G/hdmt2t.for:1789` `IF(ISBAL.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1798` `IF(ISHTA.EQ.1) CALL CALHTA` | 외부 IF 블록 없음 |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1806` `IF(ISDISP.EQ.2) CALL CALDISP2` | `G/hdmt2t.for:1805` `IF(N.GE.NDISP.AND.NCTBC.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1807` `IF(ISDISP.EQ.3) CALL CALDISP3` | `G/hdmt2t.for:1805` `IF(N.GE.NDISP.AND.NCTBC.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1815` `CALL LSQHARM` | `G/hdmt2t.for:1814` `IF(ISLSHA.EQ.1.AND.N.EQ.NCLSHA)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1827` `CALL OUTPUT1` | `G/hdmt2t.for:1825` `IF(NPRINT .EQ. NTSPP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1841` `CALL SURFPLT` | `G/hdmt2t.for:1840` `IF(N.GE.NCPPH.AND.ISPPH.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1852` `CALL BEDPLTH` | `G/hdmt2t.for:1850` `IF(N.GE.NCBPH.AND.ISBPH.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1864` `CALL VELPLTH` | `G/hdmt2t.for:1863` `IF(N.GE.NCVPH.AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1873` `CALL VELPLTV` | `G/hdmt2t.for:1872` `IF(N.GE.NCVPV.AND.ISVPV.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1926` `IF(ISTRAN(1).GE.1) CALL SALPLTH (1,SAL)` | `G/hdmt2t.for:1925` `IF(N.GE.NCSPH(1).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1933` `IF(ISTRAN(2).GE.1) CALL SALPLTH (2,TEM)` | `G/hdmt2t.for:1932` `IF(N.GE.NCSPH(2).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1940` `IF(ISTRAN(3).GE.1) CALL SALPLTH (3,DYE)` | `G/hdmt2t.for:1939` `IF(N.GE.NCSPH(3).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1947` `IF(ISTRAN(4).GE.1) CALL SALPLTH (4,SFL)` | `G/hdmt2t.for:1946` `IF(N.GE.NCSPH(4).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1954` `IF(ISTRAN(5).GE.1) CALL SALPLTH (5,TVAR1S)` | `G/hdmt2t.for:1953` `IF(N.GE.NCSPH(5).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1961` `IF(ISTRAN(6).GE.1) CALL SALPLTH (6,SEDT)` | `G/hdmt2t.for:1960` `IF(N.GE.NCSPH(6).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1968` `IF(ISTRAN(7).GE.1) CALL SALPLTH (7,SNDT)` | `G/hdmt2t.for:1967` `IF(N.GE.NCSPH(7).AND.IPLTTMP.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1976` `CALL SALPLTV(ITMP)` | `G/hdmt2t.for:1975` `IF(N.GE.NCSPV(ITMP).AND.ISSPV(ITMP).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1987` `CALL EE_LINKAGE(0)` | `G/hdmt2t.for:1985` `IF(ISSPH(8).EQ.1.OR.ISBEXP.EQ.1)THEN`<br>`G/hdmt2t.for:1986` `IF(N.GE.NCSPH(8))THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:1999` `CALL OUT3D` | `G/hdmt2t.for:1998` `IF(N.EQ.NC3DO.AND.IS3DO.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:2011` `CALL RESTOUT(0)` | `G/hdmt2t.for:2007` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmt2t.for:2010` `IF(ISSREST.EQ.0)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:2013` `IF(IWQRST.EQ.1) CALL WWQRST` | `G/hdmt2t.for:2007` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmt2t.for:2010` `IF(ISSREST.EQ.0)THEN`<br>`G/hdmt2t.for:2012` `IF(ISTRAN(8).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:2014` `IF(IWQBEN.EQ.1 .AND. ISMRST.EQ.1) CALL WSMRST` | `G/hdmt2t.for:2007` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmt2t.for:2010` `IF(ISSREST.EQ.0)THEN`<br>`G/hdmt2t.for:2012` `IF(ISTRAN(8).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:2027` `CALL TIMELOG(N,TIMEDAY)` | `G/hdmt2t.for:2026` `IF(NTIMER.EQ.NTSPTC)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:2038` `IF(ISHOW.EQ.1) CALL SHOWVAL1` | 외부 IF 블록 없음 |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:2039` `IF(ISHOW.EQ.2) CALL SHOWVAL2` | 외부 IF 블록 없음 |
| 반복·잔류 수송·진단·출력 | `G/hdmt2t.for:2040` `IF(ISHOW.EQ.3) CALL SHOWVAL3` | 외부 IF 블록 없음 |
| 종료 | `G/hdmt2t.for:2057` `CALL TIMEF(WT2TMP)` | `G/hdmt2t.for:2053` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt2t.for:2055` `ELSE` |
| 종료 | `G/hdmt2t.for:2119` `CALL OUTPUT2` | 외부 IF 블록 없음 |
| 종료 | `G/hdmt2t.for:2126` `CALL RESTOUT(0)` | `G/hdmt2t.for:2125` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN` |
| 종료 | `G/hdmt2t.for:2128` `IF(IWQRST.EQ.1) CALL WWQRST` | `G/hdmt2t.for:2125` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN`<br>`G/hdmt2t.for:2127` `IF(ISTRAN(8).GE.1)THEN` |
| 종료 | `G/hdmt2t.for:2129` `IF(IWQBEN.EQ.1 .AND. ISMRST.EQ.1) CALL WSMRST` | `G/hdmt2t.for:2125` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN`<br>`G/hdmt2t.for:2127` `IF(ISTRAN(8).GE.1)THEN` |
| 종료 | `G/hdmt2t.for:2133` `CALL RESTMOD` | `G/hdmt2t.for:2132` `IF(ISRESTO.EQ.-2)THEN` |
| 종료 | `G/hdmt2t.for:2141` `IF(ISLSHA.EQ.1) CALL LSQHARM` | 외부 IF 블록 없음 |
| 종료 | `G/hdmt2t.for:2186` `IF(ISTRAN(5).GE.1.AND.ISFDCH.GE.1)CALL FOODCHAIN(1)` | 외부 IF 블록 없음 |
| 종료 | `G/hdmt2t.for:2194` `CALL BAL2T5` | `G/hdmt2t.for:2192` `IF(IS2TIM.GE.1) THEN`<br>`G/hdmt2t.for:2193` `IF(ISBAL.GE.1)THEN` |

#### HDMT1D

| 구간 | 직접 호출문 위치와 원문 | 외부 IF 분기 원문 |
|---|---|---|
| 초기화 | `G/hdmt1d.for:35` `CALL TIMEF(WTTMP)` | `G/hdmt1d.for:31` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:33` `ELSE` |
| 초기화 | `G/hdmt1d.for:71` `CALL CALAREA(1)` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt1d.for:73` `CALL CALAREA(2)` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt1d.for:97` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt1d.for:103` `IF(ISHDMF.GE.1) CALL CALHDMF` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt1d.for:112` `CALL CALTSXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt1d.for:131` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt1d.for:151` `CALL CALTSXY` | 외부 IF 블록 없음 |
| 초기화 | `G/hdmt1d.for:233` `CALL TIMELOG(N,TIMEDAY)` | 외부 IF 블록 없음 |
| 반복·초기 수지 | `G/hdmt1d.for:313` `CALL BAL2T1` | `G/hdmt1d.for:311` `IF(IS2TIM.GE.1) THEN`<br>`G/hdmt1d.for:312` `IF(ISBAL.GE.1)THEN` |
| 반복·연직 혼합 | `G/hdmt1d.for:331` `CALL TIMEF(WT1TMP)` | `G/hdmt1d.for:327` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:329` `ELSE` |
| 반복·연직 혼합 | `G/hdmt1d.for:334` `IF(N.EQ.1.OR.ISTOPT(0).EQ.0) CALL CALAVB (ISTL)` | `G/hdmt1d.for:333` `IF(KC.GT.1)THEN` |
| 반복·연직 혼합 | `G/hdmt1d.for:335` `IF(N.GT.1.AND.ISTOPT(0).GT.1) CALL CALAVB2 (ISTL)` | `G/hdmt1d.for:333` `IF(KC.GT.1)THEN` |
| 반복·연직 혼합 | `G/hdmt1d.for:341` `CALL TIMEF(WT2TMP)` | `G/hdmt1d.for:337` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:339` `ELSE` |
| 반복·명시적 운동량 | `G/hdmt1d.for:363` `CALL TIMEF(WT1TMP)` | `G/hdmt1d.for:359` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:361` `ELSE` |
| 반복·명시적 운동량 | `G/hdmt1d.for:366` `CALL CALEXP1D (ISTL)` | 외부 IF 블록 없음 |
| 반복·명시적 운동량 | `G/hdmt1d.for:372` `CALL TIMEF(WT2TMP)` | `G/hdmt1d.for:368` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:370` `ELSE` |
| 반복·시계열 | `G/hdmt1d.for:382` `CALL CALCSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열 | `G/hdmt1d.for:383` `CALL CALQVS (ISTL)` | 외부 IF 블록 없음 |
| 반복·시계열 | `G/hdmt1d.for:385` `IF(NPSER.GE.1) CALL CALPSER (ISTL)` | 외부 IF 블록 없음 |
| 반복·수면 응력 | `G/hdmt1d.for:406` `CALL CALTSXY` | `G/hdmt1d.for:394` `IF(ISCDMA.GE.3.AND.ISCDMA.LE.8)THEN`<br>`G/hdmt1d.for:395` `IF(ISTL.EQ.3)THEN` |
| 반복·외부모드 | `G/hdmt1d.for:433` `CALL TIMEF(WT1TMP)` | `G/hdmt1d.for:429` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:431` `ELSE` |
| 반복·외부모드 | `G/hdmt1d.for:436` `CALL CALPUV1D(ISTL)` | 외부 IF 블록 없음 |
| 반복·외부모드 | `G/hdmt1d.for:442` `CALL TIMEF(WT2TMP)` | `G/hdmt1d.for:438` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:440` `ELSE` |
| 반복·수면 응력 | `G/hdmt1d.for:514` `CALL CALTSXY` | `G/hdmt1d.for:502` `IF(ISCDMA.LE.2.OR.ISCDMA.GE.9)THEN`<br>`G/hdmt1d.for:503` `IF(ISTL.EQ.3)THEN` |
| 반복·내부모드 | `G/hdmt1d.for:543` `CALL TIMEF(WT1TMP)` | `G/hdmt1d.for:539` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:541` `ELSE` |
| 반복·내부모드 | `G/hdmt1d.for:547` `CALL CALUVW (ISTL,1)` | `G/hdmt1d.for:546` `IF(KC.GT.1)THEN` |
| 반복·내부모드 | `G/hdmt1d.for:564` `CALL CALUVW (ISTL,1)` | `G/hdmt1d.for:546` `IF(KC.GT.1)THEN`<br>`G/hdmt1d.for:548` `ELSE` |
| 반복·내부모드 | `G/hdmt1d.for:578` `CALL TIMEF(WT2TMP)` | `G/hdmt1d.for:574` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:576` `ELSE` |
| 반복·농도 | `G/hdmt1d.for:596` `CALL CALCONC (ISTL,1)` | 외부 IF 블록 없음 |
| 반복·수질·부유생물 | `G/hdmt1d.for:894` `IF(ISTRAN(8).GE.1) CALL WQ3D` | `G/hdmt1d.for:792` `IF(ISTRAN(4).GE.1.OR.ISTRAN(8).GE.1)THEN` |
| 반복·수질·부유생물 | `G/hdmt1d.for:895` `IF(ISTRAN(4).GE.1) CALL CALSFT(2)` | `G/hdmt1d.for:792` `IF(ISTRAN(4).GE.1.OR.ISTRAN(8).GE.1)THEN` |
| 반복·부력 | `G/hdmt1d.for:922` `CALL CALBUOY` | `G/hdmt1d.for:921` `IF(BSC.GT.1.E-6)THEN` |
| 반복·중간 수지 | `G/hdmt1d.for:945` `CALL BAL2T4` | `G/hdmt1d.for:943` `IF(IS2TIM.GE.1) THEN`<br>`G/hdmt1d.for:944` `IF(ISBAL.GE.1)THEN` |
| 반복·수평 혼합 | `G/hdmt1d.for:973` `IF(ISTL.NE.2.AND.ISHDMF.GE.1) CALL CALHDMF` | 외부 IF 블록 없음 |
| 반복·바닥 응력 | `G/hdmt1d.for:1032` `CALL CALTBXY(ISTL,IS2TL)` | 외부 IF 블록 없음 |
| 반복·난류 수송 | `G/hdmt1d.for:1087` `CALL TIMEF(WT1TMP)` | `G/hdmt1d.for:1083` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:1085` `ELSE` |
| 반복·난류 수송 | `G/hdmt1d.for:1090` `IF(ISQQ.EQ.1) CALL CALQQ1 (ISTL)` | `G/hdmt1d.for:1089` `IF(KC.GT.1)THEN` |
| 반복·난류 수송 | `G/hdmt1d.for:1091` `IF(ISQQ.EQ.2) CALL CALQQ2 (ISTL)` | `G/hdmt1d.for:1089` `IF(KC.GT.1)THEN` |
| 반복·난류 수송 | `G/hdmt1d.for:1097` `CALL TIMEF(WT2TMP)` | `G/hdmt1d.for:1093` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:1095` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1142` `CALL TMSR` | `G/hdmt1d.for:1139` `IF(ISTMSR.GE.1)THEN`<br>`G/hdmt1d.for:1140` `IF(N.GE.NBTMSR.AND.N.LE.NSTMSR)THEN`<br>`G/hdmt1d.for:1141` `IF(NCTMSR.EQ.NWTMSR)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1158` `CALL DUMP` | `G/hdmt1d.for:1155` `IF(ISDUMP.GE.1)THEN`<br>`G/hdmt1d.for:1156` `IF(TIME.GE.TSDUMP.AND.TIME.LE.TEDUMP)THEN`<br>`G/hdmt1d.for:1157` `IF(NCDUMP.EQ.NSDUMP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1174` `CALL HYDOUT` | `G/hdmt1d.for:1171` `IF(IHYDOUT.GE.1)THEN`<br>`G/hdmt1d.for:1172` `IF(N.GE.NBTMSR.AND.N.LE.NSTMSR)THEN`<br>`G/hdmt1d.for:1173` `IF(NCHYDOUT.EQ.NWHYDOUT)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1220` `CALL VSFP` | `G/hdmt1d.for:1218` `IF(ISVSFP.EQ.1)THEN`<br>`G/hdmt1d.for:1219` `IF(N.GE.NBVSFP.AND.N.LE.NSVSFP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1228` `IF(ISSSMMT.NE.2) CALL CALMMT` | 외부 IF 블록 없음 |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1235` `IF(N.GE.NPDRT) CALL DRIFTER` | `G/hdmt1d.for:1234` `IF(ISPD.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1242` `CALL TIMEF(WT1TMP)` | `G/hdmt1d.for:1237` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt1d.for:1238` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:1240` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1245` `IF(N.GE.NLRPDRT(1)) CALL LAGRES` | `G/hdmt1d.for:1237` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt1d.for:1244` `IF(ISLRPD.LE.2)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1248` `IF(N.GE.NLRPDRT(1)) CALL GLMRES` | `G/hdmt1d.for:1237` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt1d.for:1247` `IF(ISLRPD.GE.3)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1254` `CALL TIMEF(WT2TMP)` | `G/hdmt1d.for:1237` `IF(ISLRPD.GE.1)THEN`<br>`G/hdmt1d.for:1250` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:1252` `ELSE` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1277` `CALL BUDGET5` | `G/hdmt1d.for:1276` `IF(ISSBAL.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1290` `CALL BAL2T5` | `G/hdmt1d.for:1288` `IF(IS2TIM.GE.1) THEN`<br>`G/hdmt1d.for:1289` `IF(ISBAL.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1306` `IF(ISDISP.EQ.2) CALL CALDISP2` | `G/hdmt1d.for:1305` `IF(N.GE.NDISP.AND.NCTBC.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1307` `IF(ISDISP.EQ.3) CALL CALDISP3` | `G/hdmt1d.for:1305` `IF(N.GE.NDISP.AND.NCTBC.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1315` `CALL LSQHARM` | `G/hdmt1d.for:1314` `IF(ISLSHA.EQ.1.AND.N.EQ.NCLSHA)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1327` `CALL OUTPUT1` | `G/hdmt1d.for:1325` `IF(NPRINT .EQ. NTSPP)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1339` `CALL SURFPLT` | `G/hdmt1d.for:1338` `IF(N.EQ.NCPPH.AND.ISPPH.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1346` `CALL VELPLTH` | `G/hdmt1d.for:1345` `IF(N.EQ.NCVPH.AND.ISVPH.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1353` `CALL VELPLTV` | `G/hdmt1d.for:1352` `IF(N.EQ.NCVPV.AND.ISVPV.GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1366` `IF(ISTRAN(1).GE.1) CALL SALPLTH (1,SAL)` | `G/hdmt1d.for:1365` `IF(N.EQ.NCSPH(1).AND.ISSPH(1).EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1371` `IF(ISTRAN(2).GE.1) CALL SALPLTH (2,TEM)` | `G/hdmt1d.for:1370` `IF(N.EQ.NCSPH(2).AND.ISSPH(2).EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1376` `IF(ISTRAN(3).GE.1) CALL SALPLTH (3,DYE)` | `G/hdmt1d.for:1375` `IF(N.EQ.NCSPH(3).AND.ISSPH(3).EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1381` `IF(ISTRAN(4).GE.1) CALL SALPLTH (4,SFL)` | `G/hdmt1d.for:1380` `IF(N.EQ.NCSPH(4).AND.ISSPH(4).EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1386` `IF(ISTRAN(5).GE.1) CALL SALPLTH (5,TVAR1S)` | `G/hdmt1d.for:1385` `IF(N.EQ.NCSPH(5).AND.ISSPH(5).EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1391` `IF(ISTRAN(6).GE.1) CALL SALPLTH (6,SEDT)` | `G/hdmt1d.for:1390` `IF(N.EQ.NCSPH(6).AND.ISSPH(6).EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1396` `IF(ISTRAN(7).GE.1) CALL SALPLTH (7,SNDT)` | `G/hdmt1d.for:1395` `IF(N.EQ.NCSPH(7).AND.ISSPH(7).EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1404` `CALL SALPLTV(ITMP)` | `G/hdmt1d.for:1403` `IF(N.EQ.NCSPV(ITMP).AND.ISSPV(ITMP).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1416` `CALL OUT3D` | `G/hdmt1d.for:1415` `IF(N.EQ.NC3DO.AND.IS3DO.EQ.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1428` `CALL RESTOUT(0)` | `G/hdmt1d.for:1424` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmt1d.for:1427` `IF(ISSREST.EQ.0)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1430` `IF(IWQRST.EQ.1) CALL WWQRST` | `G/hdmt1d.for:1424` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmt1d.for:1427` `IF(ISSREST.EQ.0)THEN`<br>`G/hdmt1d.for:1429` `IF(ISTRAN(8).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1431` `IF(IWQBEN.EQ.1 .AND. ISMRST.EQ.1) CALL WSMRST` | `G/hdmt1d.for:1424` `IF(ISRESTO.GE.1)THEN`<br>`G/hdmt1d.for:1427` `IF(ISSREST.EQ.0)THEN`<br>`G/hdmt1d.for:1429` `IF(ISTRAN(8).GE.1)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1444` `CALL TIMELOG(N,TIMEDAY)` | `G/hdmt1d.for:1443` `IF(NTIMER.EQ.NTSPTC)THEN` |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1455` `IF(ISHOW.EQ.1) CALL SHOWVAL1` | 외부 IF 블록 없음 |
| 반복·잔류 수송·진단·출력 | `G/hdmt1d.for:1456` `IF(ISHOW.EQ.2) CALL SHOWVAL2` | 외부 IF 블록 없음 |
| 종료 | `G/hdmt1d.for:1470` `CALL TIMEF(WT2TMP)` | `G/hdmt1d.for:1466` `IF(ISCRAY.EQ.0)THEN`<br>`G/hdmt1d.for:1468` `ELSE` |
| 종료 | `G/hdmt1d.for:1532` `CALL OUTPUT2` | 외부 IF 블록 없음 |
| 종료 | `G/hdmt1d.for:1539` `CALL RESTOUT(0)` | `G/hdmt1d.for:1538` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN` |
| 종료 | `G/hdmt1d.for:1541` `IF(IWQRST.EQ.1) CALL WWQRST` | `G/hdmt1d.for:1538` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN`<br>`G/hdmt1d.for:1540` `IF(ISTRAN(8).GE.1)THEN` |
| 종료 | `G/hdmt1d.for:1542` `IF(IWQBEN.EQ.1 .AND. ISMRST.EQ.1) CALL WSMRST` | `G/hdmt1d.for:1538` `IF(ISRESTO.EQ.-1.OR.ISRESTO.EQ.-11)THEN`<br>`G/hdmt1d.for:1540` `IF(ISTRAN(8).GE.1)THEN` |
| 종료 | `G/hdmt1d.for:1546` `CALL RESTMOD` | `G/hdmt1d.for:1545` `IF(ISRESTO.EQ.-2)THEN` |
| 종료 | `G/hdmt1d.for:1554` `IF(ISLSHA.EQ.1) CALL LSQHARM` | 외부 IF 블록 없음 |

#### LTMT

| 구간 | 직접 호출문 위치와 원문 | 외부 IF 분기 원문 |
|---|---|---|
| 초기화 | `G/ltmt.for:37` `CALL RESTRAN` | 외부 IF 블록 없음 |
| 초기화 | `G/ltmt.for:145` `CALL RESTRAN` | `G/ltmt.for:143` `IF(ISSSMMT.EQ.0)THEN` |
| 초기화 | `G/ltmt.for:217` `CALL ADJMMT` | 외부 IF 블록 없음 |
| 반복·농도·진단 | `G/ltmt.for:242` `CALL CALCONC (2,0)` | `G/ltmt.for:241` `IF(ISCDCA(1).NE.1)THEN` |
| 반복·농도·진단 | `G/ltmt.for:244` `CALL CALCONC (3,0)` | `G/ltmt.for:241` `IF(ISCDCA(1).NE.1)THEN`<br>`G/ltmt.for:243` `ELSE` |
| 반복·농도·진단 | `G/ltmt.for:246` `IF(ISHOW.GE.1) CALL SHOWVAL1` | 외부 IF 블록 없음 |
| 반복·평균 수송장 갱신 | `G/ltmt.for:332` `CALL RESTRAN` | `G/ltmt.for:313` `IF(ISSSMMT.EQ.0)THEN`<br>`G/ltmt.for:315` `IF(NCTS.EQ.NTSMMT)THEN` |
| 반복·평균 수송장 갱신 | `G/ltmt.for:369` `CALL ADJMMT` | `G/ltmt.for:313` `IF(ISSSMMT.EQ.0)THEN`<br>`G/ltmt.for:315` `IF(NCTS.EQ.NTSMMT)THEN` |
| 종료·잔류장 출력 | `G/ltmt.for:464` `CALL RSALPLTH(1,SALLPF)` | `G/ltmt.for:463` `IF(ISRSPH(1).EQ.1.AND.ISTRAN(1).GE.1)THEN` |
| 종료·잔류장 출력 | `G/ltmt.for:468` `CALL RSALPLTH(2,TEMLPF)` | `G/ltmt.for:467` `IF(ISRSPH(2).EQ.1.AND.ISTRAN(2).GE.1)THEN` |
| 종료·잔류장 출력 | `G/ltmt.for:472` `CALL RSALPLTH(3,DYELPF)` | `G/ltmt.for:471` `IF(ISRSPH(3).EQ.1.AND.ISTRAN(3).GE.1)THEN` |
| 종료·잔류장 출력 | `G/ltmt.for:476` `CALL RSALPLTH(4,SEDTLPF)` | `G/ltmt.for:475` `IF(ISRSPH(4).EQ.1.AND.ISTRAN(4).GE.1)THEN` |
| 종료·잔류장 출력 | `G/ltmt.for:480` `CALL RSALPLTH(5,SNDTLPF)` | `G/ltmt.for:479` `IF(ISRSPH(4).EQ.1.AND.ISTRAN(5).GE.1)THEN` |
| 종료·잔류장 출력 | `G/ltmt.for:488` `CALL RSALPLTH(7,SFLLPF)` | `G/ltmt.for:487` `IF(ISRSPH(7).EQ.1.AND.ISTRAN(7).GE.1)THEN` |
| 종료·잔류장 출력 | `G/ltmt.for:497` `CALL RVELPLTH` | `G/ltmt.for:496` `IF(ISRVPH.EQ.1)THEN` |
| 종료·잔류장 출력 | `G/ltmt.for:506` `CALL RSURFPLT` | `G/ltmt.for:505` `IF(ISRPPH.EQ.1)THEN` |
| 종료·잔류장 출력 | `G/ltmt.for:515` `CALL RSALPLTV(1)` | `G/ltmt.for:514` `IF(ISRSPV(1).GE.1)THEN` |
| 종료·잔류장 출력 | `G/ltmt.for:525` `CALL RVELPLTV` | `G/ltmt.for:524` `IF(ISRVPV.GE.1)THEN` |

## 2. GVC 고유 처리와 일반 루틴의 차이

### 2.1 SETGVC의 입력, 활성층, 척도

| 처리 | 확인한 내용 | 원문 근거 |
|---|---|---|
| 셀 유형 | `LCTV=1`은 재척도화 높이 셀이다. `LCTV=2`는 시그마 셀이다. | `G/setgvc.for:117` `C     LCTV AND IJCTV EQUAL 1 FOR FOR RESCALED HEIGHT CELLS AND`<br>`G/setgvc.for:118` `C     2 FOR SIGMA CELLS` |
| 셀 유형 입력 | `SETGVC`는 `CELLGVC.INP`를 읽어서 `IJCTV`를 `LCTV`에 옮긴다. | `G/setgvc.for:79` `OPEN(1,FILE='CELLGVC.INP',STATUS='UNKNOWN')`<br>`G/setgvc.for:103` `READ(1,101,IOSTAT=ISO)JDUMY,(IJCTV(I,J),I=IFIRST,ILAST)`<br>`G/setgvc.for:128` `LCTV(L)=IJCTV(I,J)` |
| 지정 층 수 | `ISETGVC=0`이면 `SETGVC`는 `GVCLAYER.INP`에서 `I,J,KLTMP`를 읽는다. 재척도화 높이 셀은 `KGVCP=KC-KLTMP+1`을 사용한다. 재척도화 높이 셀은 `GVCSCLP=KC/KLTMP`를 사용한다. | `G/setgvc.for:142` `IF(ISETGVC.EQ.0) THEN`<br>`G/setgvc.for:144` `OPEN(1,FILE='GVCLAYER.INP',STATUS='UNKNOWN')`<br>`G/setgvc.for:151` `READ(1,*)I,J,KLTMP`<br>`G/setgvc.for:159` `IF(LCTV(L).EQ.1) THEN`<br>`G/setgvc.for:160` `KGVCP(L)=KC-KLTMP+1`<br>`G/setgvc.for:161` `GVCSCLP(L)=FLOAT(KC)/FLOAT(KLTMP)` |
| 시그마 셀의 층 수 | 시그마 셀은 파일의 `KLTMP` 대신 전역 `KSIG`를 사용한다. | `G/setgvc.for:154` `IF(LCTV(L).EQ.2) THEN`<br>`G/setgvc.for:155` `KGVCP(L)=KC-KSIG+1`<br>`G/setgvc.for:156` `GVCSCLP(L)=FLOAT(KC)/FLOAT(KSIG)` |
| 자동 층 수 | `ISETGVC=1`이면 `SETGVC`는 기준 수위와 바닥 높이 비율을 반올림하여 층 수를 정한다. | `G/setgvc.for:192` `IF(ISETGVC.EQ.1) THEN`<br>`G/setgvc.for:203` `TMPSCL=SELVREF-BELVREF`<br>`G/setgvc.for:207` `TMPVAL=(SELVREF-BELV(L))/TMPSCL`<br>`G/setgvc.for:208` `TMPVAL=TMPVAL*FLOAT(KC)`<br>`G/setgvc.for:209` `KLTMP=NINT(TMPVAL)`<br>`G/setgvc.for:213` `KGVCP(L)=KC-KLTMP+1` |
| 바닥 높이 보정의 범위 | `SETGVC`는 `BELVCOR`를 계산해 출력한다. 이 파일은 `BELVCOR`를 `BELV`에 대입하지 않는다. | `G/setgvc.for:212` `BELVCOR(L)=SELVREF-TMPSCL/GVCSCLP(L)`<br>`G/setgvc.for:227` `WRITE(1,110)IL(L),JL(L),KLTMP,KGVCP(L),GVCSCLP(L),`<br>`G/setgvc.for:228` `&                BELV(L),BELVCOR(L)`. `BELVCOR`의 파일 내 참조는 선언 30줄과 이 계산·출력뿐이다. |
| 셀 중심 활성 마스크 | `LGVCP`의 참값은 활성층을 뜻한다. | `G/setgvc.for:267` `IF(K.GE.KGVCP(L))LGVCP(L,K)=.TRUE.` |
| 수평 면 활성층 | U면의 시작층은 인접 셀 중심 시작층의 최댓값이다. V면도 같은 방식으로 시작층을 정한다. | `G/setgvc.for:281` `KGVCU(L)=MAX(KGVCP(L),KGVCP(L-1))   ! *** Maximum layer number of active bottom layer`<br>`G/setgvc.for:283` `GVCSCLU(L)=FLOAT(KC)/FLOAT(KLTMP)   ! *** Ratio of Total/Minimum Active Layers`<br>`G/setgvc.for:309` `KGVCV(L)=MAX(KGVCP(L),KGVCP(LS))`<br>`G/setgvc.for:311` `GVCSCLV(L)=FLOAT(KC)/FLOAT(KLTMP)` |
| 연직 면 활성 마스크 | `SETGVC`는 위아래 셀 중심층이 모두 활성일 때 `LGVCW`를 참으로 설정한다. | `G/setgvc.for:347` `IF(LGVCP(L,K))THEN`<br>`G/setgvc.for:348` `IF(LGVCP(L,K+1))THEN`<br>`G/setgvc.for:349` `LGVCW(L,K)=.TRUE.` |
| `KGVCW`의 한계 | `AINIT`는 `KGVCW`를 1로 초기화한다. 이번 GVC 소스 검색은 그 밖의 `KGVCW` 사용문을 찾지 못했다. 실제 연직 면 설정은 위 행의 `LGVCW`를 사용한다. | `G/ainit.for:242` `KGVCW(L)=1`. 검색 범위는 `G/*.for`, `G/*.f`, `G/*.f90`의 `KGVCW` 토큰이다. |
| 면 수심 | `SETGVC`는 셀 중심 척도를 곱한 수심을 면 척도로 나눈다. | `G/setgvc.for:374` `HU(L)=0.5*(DXP(L)*DYP(L)*GVCSCLP(L)*HP(L)`<br>`G/setgvc.for:375` `&           +DXP(L-1)*DYP(L-1)*GVCSCLP(L-1)*HP(L-1))`<br>`G/setgvc.for:376` `&           /(GVCSCLU(L)*DXU(L)*DYU(L))` |
| 내부모드 계수 | `SETGVC`는 활성 바닥층에서 면별 누적 계수 계산을 시작한다. | `G/setgvc.for:428` `KBTMPU=KGVCU(L)`<br>`G/setgvc.for:430` `CDZRGVCU(L,KBTMPU)=GVCSCLU(L)*DZC(KBTMPU)-1.`<br>`G/setgvc.for:432` `CDZRGVCU(L,K)=GVCSCLU(L)*DZC(K)+CDZRGVCU(L,K-1)`<br>`G/setgvc.for:465` `CDZDGVCU(L,KBTMPU)=GVCSCLU(L)*DZC(KBTMPU)`<br>`G/setgvc.for:467` `CDZDGVCU(L,K)=GVCSCLU(L)*DZC(K)+CDZDGVCU(L,K-1)` |
| 난류 근접 함수 | `SETGVC`는 `KGVCP-1`을 바닥 기준 인덱스로 사용한다. | `G/setgvc.for:549` `KBOT=KGVCP(L)-1`<br>`G/setgvc.for:550` `IF(K.GE.KGVCP(L))THEN`<br>`G/setgvc.for:551` `FPROXGVC(L,K)=1./(VKC*(Z(K)-Z(KBOT))*(1.-Z(K)))**2` |
| 정상 유입 | `SETGVC`는 활성층의 `QSS`에 셀 중심 척도를 곱한다. `SETGVC`는 비활성층의 `QSS`를 0으로 설정한다. | `G/setgvc.for:585` `IF(K.GE.KGVCP(L))THEN`<br>`G/setgvc.for:586` `QSS(K,LL)=GVCSCLP(L)*QSS(K,LL)`<br>`G/setgvc.for:588` `QSS(K,LL)=0.0` |

확인: `SETGVC`는 단순한 층 번호 리더보다 많은 배열을 설정한다. 위 표의 면 마스크, 면 수심, 내부모드 계수, 난류 근접 함수, 정상 유입이 그 근거다.

해석: 활성층 수가 달라지는 것과 면에서 실제 층 두께를 정합하는 것은 다른 판정 대상이다. §3은 이 구분으로 SGZ를 비교한다.

### 2.2 모든 *gvc.for 루틴의 역할과 일반 루틴 대조

아래 표는 `G/` 바로 아래에서 이름이 `*gvc.for`와 일치하는 파일을 모두 포함한다. 17개라는 값은 이 파일명 집계와 아래 행 목록에서 얻었다. `SETGVC`의 상세 근거는 §2.1에 적었다.

| GVC 루틴과 역할 | GVC 원문 | 일반 루틴과 확인한 차이 |
|---|---|---|
| `SETGVC`: GVC 입력과 격자 상태 초기화 | `G/setgvc.for:6` `SUBROUTINE SETGVC`<br>`G/setgvc.for:21` `C **  SUBROUTINE SETGVC READS INFORMATION FOR THE GENERALIZED VERTICAL`<br>`G/setgvc.for:22` `C **  COORDINATE OPTION AND SETS REAL AND LOCICAL MASK` | `AAEFDC`의 일반 격자 경로는 이 호출을 건너뛴다. 근거는 `G/aaefdc.for:957` `IF(IGRIDV.EQ.1) CALL SETGVC`이다. |
| `HDMTGVC`: 수리동역학과 수송 시간 반복 | `G/hdmtgvc.for:6` `SUBROUTINE HDMTGVC`<br>`G/hdmtgvc.for:443` `IF(ISTOPT(0).GE.1)CALL CALAVBGVC (ISTL)`<br>`G/hdmtgvc.for:811` `CALL CALCONCGVC (ISTL,IS2TL)` | 일반 `HDMT`는 `G/hdmt.for:457` `IF(ISTOPT(0).GE.1)CALL CALAVB (ISTL)`와 `G/hdmt.for:829` `CALL CALCONC (ISTL,IS2TL)`을 사용한다. 두 루틴의 나머지 직접 호출 조건은 §1.3에서 대조한다. |
| `CALEXPGVC`: 명시적 운동량 항 | `G/calexpgvc.for:6` `SUBROUTINE CALEXPGVC (ISTL)`<br>`G/calexpgvc.for:124` `UHC=0.5*(GVCSCLU(L)*UHDY2(L,K)+GVCSCLU(LS )*UHDY2(LS,K))`<br>`G/calexpgvc.for:125` `UHB=0.5*(GVCSCLU(L)*UHDY2(L,K)+GVCSCLU(L+1)*UHDY2(L+1,K))` | 일반 `CALEXP`의 대응 플럭스에는 `GVCSCLU` 곱이 없다. 근거는 `G/calexp.for:122` `UHC=0.5*(UHDY2(L,K)+UHDY2(LS,K))`와 `G/calexp.for:123` `UHB=0.5*(UHDY2(L,K)+UHDY2(L+1,K))`이다. |
| `CALPUV9GVC`: 외부모드의 압력과 수심 적분 유량 | `G/calpuv9gvc.for:6` `SUBROUTINE CALPUV9GVC (ISTL)`<br>`G/calpuv9gvc.for:83` `IF(BSC.GT.1.E-6) CALL CALEBIGVC`<br>`G/calpuv9gvc.for:115` `KU=KGVCU(L)`<br>`G/calpuv9gvc.for:118` `&        -SBX(L)*GVCSCLU(L)*HU(L)*((BI2GVC(L,KU)+BI2GVC(L-1,KU)`<br>`G/calpuv9gvc.for:860` `CALL CONGRAD (ISTL)` | 일반 `CALPUV9`는 `G/calpuv9.for:83` `IF(BSC.GT.1.E-6) CALL CALEBI`을 호출한다. GVC판은 면의 활성 바닥층에서 GVC 부력 적분을 사용한다. GVC판은 `CONGRAD(ISTL)`로 외부모드를 푼다. |
| `CALEBIGVC`: 외부모드용 부력 적분 | `G/calebigvc.for:19` `C **  CALEBI CALCULATES THE EXTERNAL BUOYANCY INTEGRALS`<br>`G/calebigvc.for:69` `IF(K.GE.KGVCP(L))THEN`<br>`G/calebigvc.for:71` `BEGVC(L,K)=BEGVC(L,K+1)+GP*DZC(K)*B(L,K)`<br>`G/calebigvc.for:80` `BI1GVC(L,KBOT)=BI1GVC(L,KBOT)`<br>`G/calebigvc.for:81` `&        +GP*DZC(K)*(CH(L,K)-0.5*DZC(K)*B(L,K))` | 일반 `CALEBI`는 셀마다 하나의 `BE`, `BI1`, `BI2`를 계산한다. GVC판은 바닥 후보층별 `BI1GVC`, `BI2GVC`와 층별 `BEGVC`를 계산한다. 일반판 근거는 `G/calebi.for:40` `BE(L)=BE(L)+GP*DZC(K)*B(L,K)`와 `G/calebi.for:47` `BI1(L)=BI1(L)+GP*DZC(K)*(CH(L,K)-0.5*DZC(K)*B(L,K))`이다. |
| `CALUVWGVC`: 내부 전단모드와 3차원 유속 | `G/caluvwgvc.for:6` `SUBROUTINE CALUVWGVC (ISTL,IS2TL)`<br>`G/caluvwgvc.for:226` `IF(LGVCU(L,K))THEN`<br>`G/caluvwgvc.for:227` `IF(K.EQ.KGVCU(L))THEN`<br>`G/caluvwgvc.for:228` `CMU=1.+RCDZM*GVCSCLU(L)*HU(L)*AVUI(L,K)`<br>`G/caluvwgvc.for:387` `IF(LGVCU(L,K)) UHE(L)=UHE(L)+CDZDGVCU(L,K)*DU(L,K)`<br>`G/caluvwgvc.for:612` `IF(K.GE.KGVCP(L))THEN` | 일반 `CALUVW`는 1층에서 내부모드 소거를 시작한다. GVC판은 활성 면과 활성 바닥층을 구분한다. GVC판은 면별 내부모드 계수와 척도를 사용한다. 일반판 근거는 `G/caluvw.for:165` `CMU=1.+RCDZM*HU(L)*AVUI(L,1)`이다. |
| `CALAVBGVC`: 연직 와점성 및 확산계수 | `G/calavbgvc.for:101` `AV(L,K)=AVO*GVCSCLPI(L)*HPI(L)`<br>`G/calavbgvc.for:102` `AB(L,K)=ABO*GVCSCLPI(L)*HPI(L)`<br>`G/calavbgvc.for:334` `IF(LGVCU(L,K)) AVUI(L,K)=2./(AV(L,K)+AV(L-1,K))`<br>`G/calavbgvc.for:366` `IF(KGVCP(L).LT.KC) AQ(L,KGVCP(L))=0.205*AV(L,KGVCP(L))` | 일반 `CALAVB`의 초기 계수에는 셀 중심 역척도가 없다. GVC판은 활성 면에서만 면 계수를 계산한다. GVC판은 난류 확산의 바닥 위치를 `KGVCP`로 옮긴다. 일반판 근거는 `G/calavb.for:102` `AV(L,K)=AVO*HPI(L)`와 `G/calavb.for:103` `AB(L,K)=ABO*HPI(L)`이다. |
| `CALQQ1GVC`: 난류 강도와 난류 길이 수송 | `G/calqq1gvc.for:6` `SUBROUTINE CALQQ1GVC (ISTL)`<br>`G/calqq1gvc.for:311` `UUU(L,K)=QQ1(L,K)*GVCSCLP(L)*H1P(L)`<br>`G/calqq1gvc.for:339` `PQQB=GP*GVCSCLP(L)*HP(L)*AB(L,K)*DZIG(K)*(B(L,K+1)-B(L,K))`<br>`G/calqq1gvc.for:566` `CLQTMP=-DELT*CDZKK(K)*AQ(L,K)*GVCSCLPI(L)*HPI(L)`<br>`G/calqq1gvc.for:572` `&       +CTE4*DML(L,K)*DML(L,K)*FPROXGVC(L,K))` | GVC판은 수송량, 부력 생성항, 연직 확산에 척도를 적용한다. GVC판은 `FPROXGVC`를 사용한다. 일반 `CALQQ1`의 부력 생성항은 `G/calqq1.for:266` `PQQB=AB(L,K)*GP*HP(L)*DZIG(K)*(B(L,K+1)-B(L,K))`이다. |
| `CALCONCGVC`: 염분·수온·염료·독성물질·퇴적물 농도 제어 | `G/calconcgvc.for:6` `SUBROUTINE CALCONCGVC (ISTL,IS2TL)`<br>`G/calconcgvc.for:265` `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).LT.4)`<br>`G/calconcgvc.for:266` `&  CALL CALTRANGVC (ISTL,IS2TL,1,1,SAL,SAL1)`<br>`G/calconcgvc.for:622` `IF(ISTRAN(2).GE.1) CALL CALHEATGVC(ISTL)`<br>`G/calconcgvc.for:873` `CCLBTMP(L)=RCDZKMK*GVCSCLPI(L)*HPI(L)*SWB3D(L,K-1)*AB(L,K-1)` | 일반 `CALCONC`는 `G/calconc.for:273` `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).LT.4)`과 `G/calconc.for:274` `&  CALL CALTRAN (ISTL,IS2TL,1,1,SAL,SAL1)`을 사용한다. GVC판은 해당 수송 호출과 열 계산을 GVC판으로 바꾼다. GVC판은 농도 연직 확산계수에 역척도를 곱한다. |
| `CALTRANGVC`: 스칼라 이류 수송과 보정 | `G/caltrangvc.for:6` `SUBROUTINE CALTRANGVC(ISTL,IS2TL,MVAR,M,CON,CON1)`<br>`G/caltrangvc.for:377` `FUHU(L,K)=GVCSCLU(L)*FUHU(L,K)`<br>`G/caltrangvc.for:378` `FVHU(L,K)=GVCSCLV(L)*FVHU(L,K)`<br>`G/caltrangvc.for:421` `IF(LGVCP(L,K))THEN`<br>`G/caltrangvc.for:422` `CH(L,K)=CON1(L,K)*GVCSCLP(L)*H1P(L)`<br>`G/caltrangvc.for:519` `CON(L,K)=SCB(L)*CH(L,K)*GVCSCLPI(L)*HPI(L)+(1.-SCB(L))*CON(L,K)` | GVC판은 수평 플럭스에 면 척도를 곱한다. GVC판은 활성층에서 척도 적용 수송량을 갱신한다. 일반판의 대응식은 `G/caltran.for:419` `CH(L,K)=CON1(L,K)*H1P(L)`와 `G/caltran.for:502` `CON(L,K)=SCB(L)*CH(L,K)*HPI(L)+(1.-SCB(L))*CON(L,K)`이다. |
| `CALHEATGVC`: 수면과 내부 열원·열손실 | `G/calheatgvc.for:21` `C **  SUBROUTINE CALHEAT CALCULATES SURFACE AND INTERNAL HEAT SOURCES`<br>`G/calheatgvc.for:74` `&     FSWRATF*EXP(SWRATNF*HDEP*GVCSCLP(L)*(Z(KC)-1.))`<br>`G/calheatgvc.for:100` `IF(K.LT.KGVCP(L))TVAR1S(L,K)=0.0`<br>`G/calheatgvc.for:108` `K=KGVCP(L)`<br>`G/calheatgvc.for:111` `&     +(DELT*DZIC(K)*GVCSCLPI(L))*0.2385E-6*SOLSWRT(L)*(` | GVC판은 광학 경로와 열원 환산에 척도를 사용한다. GVC판은 남은 단파 복사를 활성 바닥층에 넣는다. 일반판은 `G/calheat.for:104` `K=1`와 `G/calheat.for:107` `&     +(DELT*DZIC(K))*0.2385E-6*SOLSWRT(L)*(`을 사용한다. |
| `CALHEATBGVC`: 다층 저질 열확산과 바닥 물층의 연성 | `G/calheatbgvc.for:21` `C **  SUBROUTINE CALHEATB CALCULATES TEMPERATURE DISTRIBUTION IN`<br>`G/calheatbgvc.for:117` `KBOT=KGVCP(L)`<br>`G/calheatbgvc.for:119` `THICKWAT=DZC(KBOT)*GVCSCLP(L)*HP(L)`<br>`G/calheatbgvc.for:143` `BBEDTEM(L,K)=(1./DELT)-ABEDTEM(L,K)-CBEDTEM(L,K)`<br>`G/calheatbgvc.for:191` `TEMB(L,K)=UBEDTEM(L,K)`<br>`G/calheatbgvc.for:196` `TEM(L,KGVCP(L))=UBEDTEM(L,KBH)` | 일반판의 바닥 물층은 1층이다. GVC판의 바닥 물층은 `KGVCP`층이다. 일반판 근거는 `G/calheatb.for:130` `THICKWAT=DZC(1)*HP(L)`와 `G/calheatb.for:207` `TEM(L,1)=UBEDTEM(L,KBH)`이다. |
| `CALWQCGVC`: 수질 농도의 수송과 연직 확산 제어 | `G/calwqcgvc.for:6` `SUBROUTINE CALWQCGVC (ISTL)`<br>`G/calwqcgvc.for:80` `CALL CALTRWQGVC (8,NW,CWQ,CWQ2)`<br>`G/calwqcgvc.for:137` `CCUBTMP=RCDZKK*GVCSCLPI(L)*HWQI(L)*SWB3D(L,1)*AB(L,1)` | GVC판은 `CALTRWQGVC`를 호출한다. GVC판의 연직 확산계수는 역척도를 포함한다. 일반판 근거는 `G/calwqc.for:80` `CALL CALTRWQ (8,NW,CWQ,CWQ2)`와 `G/calwqc.for:137` `CCUBTMP=RCDZKK*HWQI(L)*AB(L,1)`이다. |
| `CALTRWQGVC`: 수질 변수의 이류 수송과 보정 | `G/caltrwqgvc.for:6` `SUBROUTINE CALTRWQGVC (M,NW,CON,CON1)`<br>`G/caltrwqgvc.for:188` `FUHU(L,K)=GVCSCLU(L)*FUHU(L,K)`<br>`G/caltrwqgvc.for:200` `CH(L,K)=CONT(L,K)*GVCSCLP(L)*H2WQ(L)`<br>`G/caltrwqgvc.for:217` `CON(L,K)=SCB(L)*CH(L,K)*GVCSCLPI(L)/HWQ(L)+(1.-SCB(L))*CON1(L,K)` | GVC판은 수질 수심 `H2WQ/HWQ`에 셀 중심 척도를 적용한다. 일반판의 대응식은 `G/caltrwq.for:187` `CH(L,K)=CONT(L,K)*H2WQ(L)`와 `G/caltrwq.for:204` `CON(L,K)=SCB(L)*CH(L,K)/HWQ(L)+(1.-SCB(L))*CON1(L,K)`이다. |
| `WQSKE3GVC`: 수질 반응식과 저질 침강 플럭스 | `G/wqske3gvc.for:6` `SUBROUTINE WQSKE3GVC`<br>`G/wqske3gvc.for:65` `DZWQ(L) = 1.0 / (DZC(K)*GVCSCLP(L)*HP(L))`<br>`G/wqske3gvc.for:692` `IF(K.EQ.KGVCP(L)) WQR20(L) = WQR20(L)`<br>`G/wqske3gvc.for:1654` `IF(K.LT.KGVCP(L))THEN`<br>`G/wqske3gvc.for:1655` `WQV(L,K,NW)=0.0`<br>`G/wqske3gvc.for:1721` `KBWQ=KGVCP(L)` | GVC판은 반응 환산 두께에 척도를 넣는다. GVC판은 바닥 반응 위치를 `KGVCP`로 옮긴다. GVC판은 마지막에 비활성층 농도를 0으로 설정한다. 일반판의 대응 근거는 `G/wqske3.for:70` `DZWQ(L) = 1.0 / (DZC(K)*HP(L))`와 `G/wqske3.for:704` `IF(K.EQ.1) WQR20(L) = WQR20(L)`이다. |
| `SMMBEGVC`: 수질 저질모델 제어 | `G/smmbegvc.for:26` `C  CONTROL SUBROUTINE FOR SEDIMENT COMPONENT OF WATER QUALITY MODEL`<br>`G/smmbegvc.for:51` `SMT(L) = (SMT(L) + SM1DIFT(IZ)*TEM(L,KGVCP(L))) * SM2DIFT(IZ)`<br>`G/smmbegvc.for:137` `XSMO20(L) = MAX( WQV(L,KGVCP(L),19), 3.0 )`<br>`G/smmbegvc.for:264` `WQBFNH4(L) = SMSS(L) * (SMFD1NH4*SM1NH4(L) - WQV(L,KGVCP(L),14))` | GVC판은 저질 온도와 수질 교환에 활성 바닥층 값을 사용한다. 일반판은 `G/smmbe.for:51` `SMT(L) = (SMT(L) + SM1DIFT(IZ)*TEM(L,1)) * SM2DIFT(IZ)`과 `G/smmbe.for:135` `XSMO20(L) = MAX( WQV(L,1,19), 3.0 )`을 사용한다. 이 역할은 퇴적물 총량 수지 계산과 다르다. |
| `WASPHYDROLINKGVC`: GVC 격자의 WASP 수문 링크 출력 | `G/wasphydrolinkgvc.for:1` `SUBROUTINE WASPHYDROLINKgvc`<br>`G/wasphydrolinkgvc.for:5` `C   Subroutine WASPHYDROLINKgvc writes the hyd file for WINWASP water quality model`<br>`G/wasphydrolinkgvc.for:333` `if (LGVCP(L,K)) THEN`<br>`G/wasphydrolinkgvc.for:772` `SegDepth(LWASP)=HP(L)*DZC(K)*GVCSCLP(L)` | GVC판은 활성 셀 중심층을 세그먼트로 번호화한다. GVC판은 세그먼트 두께에 척도를 곱한다. 일반판의 대응식은 `G/wasphydrolink.for:685` `SegDepth(LWASP)=HP(L)*DZC(K)`이다. |

### 2.3 파일 존재와 활성 호출 경로의 구분

| 대상 | 확인한 연결 또는 제한 | 원문 근거 |
|---|---|---|
| GVC 운동량 분기 | `HDMTGVC`는 `ISCDMA<=2`일 때만 `CALEXPGVC`를 선택한다. 다른 활성 선택문은 일반 `CALEXP2`와 `CALEXP9`를 가리킨다. | `G/hdmtgvc.for:515` `IF(ISCDMA.LE.2) CALL CALEXPGVC (ISTL)`<br>`G/hdmtgvc.for:518` `IF(ISCDMA.EQ.5) CALL CALEXP2 (ISTL)`<br>`G/hdmtgvc.for:519` `IF(ISCDMA.EQ.6) CALL CALEXP2 (ISTL)`<br>`G/hdmtgvc.for:520` `IF(ISCDMA.EQ.9) CALL CALEXP9 (ISTL)` |
| GVC 외부모드 분기 | `HDMTGVC`는 수로와 젖음·마름 조건에 따라 일반 `CALPUV9C`도 선택한다. | `G/hdmtgvc.for:633` `IF(ISCHAN.EQ.0.AND.ISDRY.EQ.0) CALL CALPUV9GVC(ISTL)`<br>`G/hdmtgvc.for:634` `IF(ISCHAN.GE.1.OR.ISDRY.GE.1) CALL CALPUV9C(ISTL)` |
| GVC 난류 분기 | `HDMTGVC`는 `ISQQ=1`과 `ISTOPT(0)>=1`에서 전용 와점성 및 난류 루틴을 선택한다. 다른 선택문은 일반 루틴을 가리킨다. | `G/hdmtgvc.for:437` `IF(KC.GT.1)THEN`<br>`G/hdmtgvc.for:438` `IF(ISQQ.EQ.1)THEN`<br>`G/hdmtgvc.for:439` `IF(ISTOPT(0).EQ.0)CALL CALAVBOLD (ISTL)`<br>`G/hdmtgvc.for:443` `IF(ISTOPT(0).GE.1)CALL CALAVBGVC (ISTL)`<br>`G/hdmtgvc.for:445` `IF(ISQQ.EQ.2) CALL CALAVB2 (ISTL)`<br>`G/hdmtgvc.for:1432` `IF(ISQQ.EQ.1)THEN`<br>`G/hdmtgvc.for:1433` `IF(ISTOPT(0).EQ.0)CALL CALQQ1OLD (ISTL)`<br>`G/hdmtgvc.for:1437` `IF(ISTOPT(0).GE.1)CALL CALQQ1GVC (ISTL)`<br>`G/hdmtgvc.for:1439` `IF(ISQQ.EQ.2) CALL CALQQ2 (ISTL)` |
| GVC 스칼라 수송 | `CALCONCGVC`는 `ISCDCA<4`에서 `CALTRANGVC`를 선택한다. `ISCDCA=4`와 `5`의 활성 선택문은 `COSTRANW`와 `COSTRAN`을 가리킨다. | `G/calconcgvc.for:265` `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).LT.4)`<br>`G/calconcgvc.for:266` `&  CALL CALTRANGVC (ISTL,IS2TL,1,1,SAL,SAL1)`<br>`G/calconcgvc.for:367` `IF(IS1DCHAN.EQ.0)THEN`<br>`G/calconcgvc.for:368` `IF(ISCOSMIC.EQ.1)THEN`<br>`G/calconcgvc.for:378` `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).EQ.4)`<br>`G/calconcgvc.for:379` `&  CALL COSTRANW (ISTL,IS2TL,1,1,SAL,SAL1)`<br>`G/calconcgvc.for:385` `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).EQ.5)`<br>`G/calconcgvc.for:386` `&  CALL COSTRAN (ISTL,IS2TL,1,1,SAL,SAL1)` |
| GVC 수질 주기 | `HDMTGVC`는 짝수 `N`의 `ISTL=3` 경로에서 `WQ3D`를 호출한다. `WQ3D`는 `IGRIDV=1`이면 `CALWQCGVC`를 호출한다. | `G/hdmtgvc.for:1006` `NTMP=MOD(N,2)`<br>`G/hdmtgvc.for:1007` `IF(NTMP.EQ.0.AND.ISTL.EQ.3)THEN`<br>`G/hdmtgvc.for:1171` `IF(ISTRAN(8).GE.1) CALL WQ3D`<br>`G/wq3d.for:182` `IF(IGRIDV.EQ.1) CALL CALWQCGVC(2)` |
| 수질 반응식 선택 | `WQ3D`는 `ISWQLVL=3`의 GVC 경로에서 `WQSKE3GVC`를 호출한다. | `G/wq3d.for:230` `IF(ISWQLVL.EQ.3) THEN`<br>`G/wq3d.for:232` `IF(IGRIDV.EQ.1) CALL WQSKE3GVC` |
| 수질 헤더의 주기 설명 | `CALWQCGVC` 헤더는 홀수 3시점 단계를 적는다. 위의 실제 `HDMTGVC` 호출 조건은 짝수 `N`이다. | `G/calwqcgvc.for:21` `C **  CALLED ONLY ON ODD THREE TIME LEVEL STEPS`<br>`G/hdmtgvc.for:1007` `IF(NTMP.EQ.0.AND.ISTL.EQ.3)THEN`. 이 비교는 `N`의 홀짝을 기준으로 한다. |
| 저질 열 계산 주기 | `CALHEATGVC`는 `DABEDT>0`에서 `CALHEATBGVC`를 조건부 호출한다. 3시점 경로의 호출 조건은 `NCTBC=NTSTBC-1`이다. | `G/calheatgvc.for:173` `NTSTBCM1=NTSTBC-1`<br>`G/calheatgvc.for:174` `IF(DABEDT.GT.0.0) THEN`<br>`G/calheatgvc.for:175` `IF(IS2TIM.EQ.1) CALL CALHEATBGVC(ISTL)`<br>`G/calheatgvc.for:176` `IF(IS2TIM.EQ.0) THEN`<br>`G/calheatgvc.for:177` `IF(NCTBC.EQ.NTSTBCM1) CALL CALHEATBGVC(ISTL)` |
| `SMMBEGVC` 연결 | 범위 내 GVC 소스에는 활성 `CALL SMMBEGVC`가 없다. `WQ3D`의 저질모델 호출문은 일반 `SMMBE`를 가리킨다. | `G/smmbegvc.for:6` `SUBROUTINE SMMBEGVC`<br>`G/wq3d.for:267` `CALL SMMBE`. 검색 범위는 `G/*.for`, `G/*.f`, `G/*.f90`이다. 검색은 대소문자를 구분하지 않는다. |
| `WASPHYDROLINKGVC` 연결 | 범위 내 GVC 소스에는 활성 `CALL WASPHYDROLINKGVC`가 없다. 따라서 이 루틴의 존재를 진입점에서 이어지는 출력 경로로 판정하지 않는다. | `G/wasphydrolinkgvc.for:1` `SUBROUTINE WASPHYDROLINKgvc`. 검색 범위는 앞 행과 같다. |

문서 확인: 저장된 「Kinetics (EEMS12)」는 GVC 선택 시 모듈 3만 작동한다고 설명한다. 이 문서는 EFDC+의 표준 전체 수질 반응 모듈을 1로 설명한다. 원문은 `DK:10` `ONLY module 3 works`와 `DK:10` `For the EFDC+ version, the standard full kinetic module is Module 1 (ISWQLVL=1).`이다. `DK` 경로는 §3.1에 적었다.

해석: 전용 루틴이 있다는 사실은 모든 GVC 옵션 조합의 수치적 적합성을 보장하지 않는다. 이 문서는 일반 루틴으로 빠지는 경로와 호출되지 않는 전용 루틴을 위 표에서 분리했다.

## 3. EFDC+ 대응 루틴과 입력·물리·수치 차이

### 3.1 판본과 문서 근거

아래 대응은 계산 역할의 대응이다. 대응은 같은 입력이나 같은 계산 결과를 뜻하지 않는다. `EFDC+에 없음`은 이번 `P/**/*.f90` 범위에서 독립 루틴 정의가 없다는 뜻이다. 이 판정은 디렉터리 이름이 `third_party_open`, `lib`, `redist`, `include`인 하위 트리를 제외한 검색에 한정한다.

문서 약칭은 다음과 같다.

| 약칭 | 저장소 원문 또는 PDF 근거 |
|---|---|
| `D1` | `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_1A.md` |
| `D9` | `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_9A.md` |
| `DK` | `models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Water_Quality_EEMS12/Kinetics_EEMS12.md` |
| `T` | `models/EFDC/raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf`. 해당 근거는 PDF 60쪽·인쇄 47쪽·§2.6.2다. 추출본은 `_staging/recovery/extract/EFDC/pdf-md/EFDC_Theory_Document_Ver_12.md`의 4293줄 쪽 경계와 4305줄 본문이다. 쪽별 기록은 `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p055-072.md`의 p.60 행이다. |

문서 확인: 이론서는 셀 면의 층 정합을 GVC와의 근본적 차이로 명시한다. 원문은 `T`, PDF 60쪽·인쇄 47쪽의 `face matching of layering is a fundamental difference with the GVC approach`이다. 이 문장의 위치는 추출본 4305줄이다. 판독자는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/epages/EFDC_Theory_Document_Ver_12-060.png`를 직접 확인했다.

문서 확인: EFDC+ C1A는 `IGRIDV=1`을 셀별 가변 층의 SGZ로 설명한다. 원문은 `D1:26` `\*              1 SIGMA-ZED (SGZ) VERTICAL LAYERING ALLOWING VARYING LAYERS FOR EACH CELL (DSI)`이다. C9A의 `ISETGVC`와 `ISGVCCK`는 사용하지 않는다. 원문은 `D9:18` `\* ISETGVC: NOT USED`와 `D9:28` `\* ISGVCCK: NOT USED`이다.

### 3.2 대응표

| GVC 루틴 | EFDC+ 대응 루틴과 파일 | 확인한 차이와 근거 |
|---|---|---|
| `AAEFDC` (`aaefdc.for`) | `EFDC` (`aaefdc.f90`) | 입력·흐름: EFDC+는 `IS2TIM`으로 `HDMT`와 `HDMT2T`를 선택한다. EFDC+는 GVC 전용 시간 반복 루틴을 따로 선택하지 않는다. 근거는 `P/aaefdc.f90:37` `PROGRAM EFDC`, `P/aaefdc.f90:3189` `if( IS2TIM == 0 ) CALL HDMT`, `P/aaefdc.f90:3190` `if( IS2TIM >= 1 ) CALL HDMT2T`이다. GVC의 선택 조건은 §1.2에 적었다. |
| `INPUT` (`input.f`) | `INPUT` (`input.f90`) | 입력: EFDC+ C1A의 필드 순서는 GVC와 다르다. EFDC+는 C9A에서 `KC` 외의 옛 GVC 필드를 더미 변수로 읽는다. 근거는 `P/input.f90:150` `read(1,*,IOSTAT = ISO) IS2TIM, IGRIDH, IGRIDV, KMINV, SGZHPDELTA  !, ISWGS84        ! NTL: Waiting for the implementation of Geographic Coordinate`와 `P/input.f90:538` `read(1,*,IOSTAT = ISO) KC, ldum, ldum, tmp, tmp, ldum`이다. GVC 근거는 `G/input.f:100` `READ(1,*,IOSTAT=ISO)IGRIDH,INESTH,IGRIDV,ITIMSOL,ISHOUSATONIC  !IS2TLPG`와 `G/input.f:229` `READ(1,*,IOSTAT=ISO)KC,KSIG,ISETGVC,SELVREF,BELVREF,ISGVCCK`이다. |
| `SETGVC` (`setgvc.for`) | 독립 `SETGVC`는 EFDC+에 없음. 대응 초기화는 `aaefdc.f90`에 있다. | 입력: GVC는 활성층 수 `KLTMP`를 읽는다. EFDC+의 `IGRIDV=1`은 최하 활성층 인덱스 `K`를 읽는다. EFDC+의 `IGRIDV>1`은 층별 두께 비율도 읽는다. 근거는 `G/setgvc.for:151` `READ(1,*)I,J,KLTMP`, `G/setgvc.for:160` `KGVCP(L)=KC-KLTMP+1`, `P/aaefdc.f90:1343` `if( IGRIDV == 1 )then`, `P/aaefdc.f90:1344` `read(1,*,END = 1000) IIN, JIN, K`, `P/aaefdc.f90:1346` `read(1,*,END = 1000) IIN, JIN, K, (R1D_Global(KK),KK = 1,KC)`이다. 수치: EFDC+는 셀별 `DZC(L,K)`를 사용한다. 근거는 `P/aaefdc.f90:1439` `DZC(L,K)  = 0.0`와 `P/aaefdc.f90:1443` `if( IGRIDV == 1 ) DZC(L,K) = DZCK(K)/DZPC`이다. |
| `HDMT` (`hdmt.for`) | `HDMT` (`hdmt.f90`) | 흐름: EFDC+는 `CALCSER`, `CALVEGSER`, `CALPSER` 뒤에 운동량과 외부모드를 계산한다. GVC의 일반 `HDMT`는 명시적 운동량 계산 뒤에 시계열을 갱신한다. 근거는 `P/hdmt.f90:673` `call CALCSER`, `P/hdmt.f90:674` `call CALVEGSER`, `P/hdmt.f90:677` `if( NPSER >= 1 ) CALL CALPSER`, `P/hdmt.f90:684` `call CALEXP`, `P/hdmt.f90:690` `call CALPUV9C` 및 §1.3의 GVC 호출표다. |
| `HDMTGVC` (`hdmtgvc.for`) | 독립 `HDMTGVC`는 EFDC+에 없음. 역할 대응은 `HDMT` (`hdmt.f90`)다. | 수치: EFDC+는 일반 시간 반복 루틴에서 SGZ 대응 `CALEXP`, `CALPUV9C`, `CALUVW`, `CALCONC`를 부른다. 근거는 `P/hdmt.f90:684` `call CALEXP`, `P/hdmt.f90:690` `call CALPUV9C`, `P/hdmt.f90:772` `call CALUVW`, `P/hdmt.f90:814` `call CALCONC`이다. 각 루틴의 SGZ 처리 근거는 아래 행에 적었다. |
| `HDMT2T` (`hdmt2t.for`) | `HDMT2T` (`hdmt2t.f90`) | 흐름·수치: GVC는 `IS2TIM=1/2`에 따라 `CALEXP2T/CALIMP2T`를 선택한다. EFDC+의 해당 단계는 `CALEXP2T`와 `CALPUV2C`를 호출한다. 근거는 `G/hdmt2t.for:651` `IF(IS2TIM.EQ.1) CALL CALEXP2T`, `G/hdmt2t.for:652` `IF(IS2TIM.EQ.2) CALL CALIMP2T`, `P/hdmt2t.f90:619` `call CALEXP2T`, `P/hdmt2t.f90:627` `call CALPUV2C`이다. |
| `HDMT1D` (`hdmt1d.for`) | EFDC+에 없음. | 흐름: 이번 EFDC+ 소스에는 `HDMT1D` 정의가 없다. EFDC+ 진입점에는 두 시간 반복 호출만 남아 있다. 근거는 `P/aaefdc.f90:3189` `if( IS2TIM == 0 ) CALL HDMT`와 `P/aaefdc.f90:3190` `if( IS2TIM >= 1 ) CALL HDMT2T`이다. 이 판정은 일반 수로 기능 전체의 부재를 뜻하지 않는다. |
| `LTMT` (`ltmt.for`) | EFDC+에 없음. | 흐름: EFDC+ 진입점은 장기 수송 호출을 주석 처리했다. 근거는 `P/aaefdc.f90:3186` `! *** LONG-TERM MASS TRANSPORT CALCULATION  (DISABLED)`와 `P/aaefdc.f90:3191` `!IF(ISLTMT >= 1 ) CALL LTMT`이다. 이번 EFDC+ 소스에는 `LTMT` 정의도 없다. |
| `CALEXPGVC` (`calexpgvc.for`) | `CALEXP` (`calexp.f90`) | 수치: GVC는 전역 층 비율과 셀·면 척도를 조합한다. EFDC+는 `IGRIDV=1`과 `>1`의 부력 전단을 구분한다. EFDC+는 면별 `SGZU/SGZV`와 면별 바닥 높이를 사용한다. 근거는 `G/calexpgvc.for:124` `UHC=0.5*(GVCSCLU(L)*UHDY2(L,K)+GVCSCLU(LS )*UHDY2(LS,K))`, `P/calexp.f90:1169` `if( IGRIDV == 1 )then`, `P/calexp.f90:1178` `FBBX(L,K) = ROLD*FBBX(L,K) + RNEW*SUB3D(L,K)*SBX(L)*GP*HU(L)*( HU(L)*( (B(L,K+1)-B(LW,K+1))*SGZU(L,K+1) + (B(L,K)-B(LW,K))*SGZU(L,K) )                                &`, `P/calexp.f90:1179` `- (B(L,K+1)-B(L,K)+B(LW,K+1)-B(LW,K))*( BELVW(L)+ZW(L,K)*HPW(L) - (BELVE(LW)+ZE(LW,K)*HPE(LW)) ) )`, `P/calexp.f90:1187` `elseif( IGRIDV > 1 )then`이다. |
| `CALPUV9GVC` (`calpuv9gvc.for`) | `CALPUV9C` (`calpuv9c.f90`) | 수치: EFDC+는 SGZ 층 두께와 이웃 활성 바닥층 차이로 면 수심을 다시 계산한다. 근거는 `P/calpuv9c.f90:1570` `HPK(L,K)  = HP(L)*DZC(L,K)`, `P/calpuv9c.f90:1585` `if( KSZ(LW) > KSZ(L) )then`, `P/calpuv9c.f90:1586` `HU(L) = max( 0.5*HPK(L,KSZ(LW)), HP(LW)*(1.+DZC(L,KSZ(LW))*0.1) )`, `P/calpuv9c.f90:1588` `HU(L) = max( 0.5*HPK(LW,KSZ(L)), HP(L)*(1.+DZC(LW,KSZ(L))*0.1) )`이다. GVC의 면 수심은 `G/calpuv9gvc.for:1002` `HU(L)=0.5*(DXP(L)*DYP(L)*GVCSCLP(L)*HP(L)`, `G/calpuv9gvc.for:1003` `&           +DXP(L-1)*DYP(L-1)*GVCSCLP(L-1)*HP(L-1))`, `G/calpuv9gvc.for:1004` `&           /(GVCSCLU(L)*DXU(L)*DYU(L))`이다. EFDC+는 젖음·마름 외부모드를 이 루틴에 포함한다. 근거는 `P/calpuv9c.f90:15` `! *** WITH PROVISIONS FOR WETTING AND DRYING OF CELLS`이다. |
| `CALEBIGVC` (`calebigvc.for`) | `CALEBI` (`calebi.f90`) | 수치: GVC는 후보 바닥층별 부력 적분을 저장한다. EFDC+는 셀 중심 적분과 각 방향 면 적분을 구분한다. 서쪽 면의 근거는 `P/calebi.f90:135` `else   ! *** SGZ FACE INTEGRALS`, `P/calebi.f90:161` `do K = KSZW(L),KC`, `P/calebi.f90:162` `DZCB(K,ND) = SGZKW(K,L)*BW(L,K)`, `P/calebi.f90:174` `BI1W(L) = BI1W(L) + DZCBK`, `P/calebi.f90:175` `BI2W(L) = BI2W(L) + DZCBK + ZZW(K,L)*DZCB(K,ND)`이다. GVC 근거는 §2.2에 적었다. |
| `CALUVWGVC` (`caluvwgvc.for`) | `CALUVW` (`caluvw.f90`) | 입력·수치: EFDC+의 호출에는 `ISTL/IS2TL` 인자가 없다. EFDC+는 `KSZU/KSZV`와 면별 소거계수를 사용한다. 근거는 `G/caluvwgvc.for:6` `SUBROUTINE CALUVWGVC (ISTL,IS2TL)`, `P/caluvw.f90:16` `SUBROUTINE CALUVW`, `P/caluvw.f90:404` `RCDZM = CDZMU(L,K)*DELTI`, `P/caluvw.f90:411` `elseif( K == KSZU(L) )then`, `P/caluvw.f90:413` `RCDZL = CDZLU(L,K)`, `P/caluvw.f90:437` `elseif( K == KSZV(L) )then`이다. |
| `CALAVBGVC` (`calavbgvc.for`) | `CALAVB` (`calavb.f90`) | 물리: 두 헤더는 Galperin 수정 Mellor–Yamada 폐합을 적는다. 근거는 `G/calavbgvc.for:9` `C **  USING GLAPERIN ET AL'S MODIFICATION OF THE MELLOR-YAMADA MODEL`와 `P/calavb.f90:13` `! *** USING GLAPERIN ET AL'S MODIFICATION OF THE MELLOR-YAMADA MODEL`이다. 수치: EFDC+는 공간별 배경계수와 셀별 활성 바닥층을 사용한다. 근거는 `P/calavb.f90:89` `AV(L,K) = AVOXY(L)*HPI(L)`, `P/calavb.f90:90` `AB(L,K) = AVBXY(L)*HPI(L)`, `P/calavb.f90:325` `AQ(L,KSZ(L)) = 0.205*AV(L,KSZ(L))`이다. 이 대응은 폐합식 전체의 동등성을 뜻하지 않는다. |
| `CALQQ1GVC` (`calqq1gvc.for`) | `CALQQ1` (`calqq1.f90`); 2시점 역할은 `CALQQ2T` (`calqq2t.f90`) | 수치: EFDC+의 3시점 난류 소거는 `KSZ`에서 시작한다. EFDC+는 셀별 `CDZKK`와 `FPROX`를 사용한다. 근거는 `P/calqq1.f90:499` `K = KSZ(L)`, `P/calqq1.f90:500` `CLQTMP  = -DELT*CDZKK(L,K) *AQ(L,K)  *HPI(L)`, `P/calqq1.f90:505` `CMQLTMP = 1.-CLQLTMP-CUQLTMP  +DELT*(QQSQR(L,K)/(CTURBB1(L,K)*DML(L,K)*HP(L)))*(1.+CTE4*DML(L,K)*DML(L,K)*FPROX(L,K))`이다. 2시점 호출은 `P/hdmt2t.f90:994` `call CALQQ2T`이다. 물리 선택: EFDC+는 `ISGOTM` 경로와 기존 폐합 경로를 구분한다. 근거는 `P/hdmt.f90:1275` `if( ISGOTM > 0 )then`와 `P/hdmt.f90:1284` `call CALQQ1`이다. GOTM 내부는 이번 대조 범위가 아니다. |
| `CALCONCGVC` (`calconcgvc.for`) | `CALCONC` (`Transport/calconc.f90`) | 흐름·입력: EFDC+는 활성 수주 변수 목록을 반복한다. EFDC+는 `ISQUICK`으로 `CALTRAN_QUICKEST`와 `CALTRAN`을 선택한다. 근거는 `P/Transport/calconc.f90:194` `do IW = 1,NACTIVEWC`, `P/Transport/calconc.f90:198` `if( ISQUICK == 1 )then`, `P/Transport/calconc.f90:200` `call CALTRAN_QUICKEST( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )`, `P/Transport/calconc.f90:203` `call CALTRAN( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )`이다. 수치: EFDC+의 농도 연직 확산은 `KSZ`층에서 시작한다. 근거는 `P/Transport/calconc.f90:353` `RCDZKK  = -DELT*CDZKK(L,KSZ(L))`와 `P/Transport/calconc.f90:392` `K = KSZ(L)`이다. |
| `CALTRANGVC` (`caltrangvc.for`) | `CALTRAN` (`Transport/caltran.f90`); 선택 경로는 `CALTRAN_QUICKEST` (`Transport/caltran_quickest.f90`) | 입력: GVC는 `ISTL/IS2TL`을 수송 인자로 전달한다. EFDC+는 `IW`, `IT`, `WCCUTOFF`, `ISKIP`을 수송 인자로 받는다. 근거는 `G/caltrangvc.for:6` `SUBROUTINE CALTRANGVC(ISTL,IS2TL,MVAR,M,CON,CON1)`와 `P/Transport/caltran.f90:13` `SUBROUTINE CALTRAN (MVAR, MO, CON, CON1, IW, IT, WCCUTOFF, ISKIP)`이다. 선택 경로의 시그니처는 `P/Transport/caltran_quickest.f90:14` `SUBROUTINE CALTRAN_QUICKEST (MVAR, MO, CON, CON1, IW, IT, WCCUTOFF, ISKIP)`이다. 수치: GVC는 `CON1*GVCSCLP*H1P` 형태를 사용한다. EFDC+는 층 두께 `H2PK/HPKI`로 수송량과 농도를 환산한다. 근거는 `G/caltrangvc.for:422` `CH(L,K)=CON1(L,K)*GVCSCLP(L)*H1P(L)`, `P/Transport/caltran.f90:183` `CD(L,K,IT) = CON1(L,K)*H2PK(L,K) + DDELT*( ( FQC(L,K,IT) +                                                                      &`, `P/Transport/caltran.f90:204` `CON(L,K) = CD(L,K,IT)*HPKI(L,K)`이다. |
| `CALHEATGVC` (`calheatgvc.for`) | `CALHEAT` (`Transport/mod_heat.f90`) | 물리: EFDC+ 열 모듈은 기존 열수지 외에 COARE 3.6 분기를 갖는다. 근거는 `P/Transport/mod_heat.f90:631` `elseif( ISTOPT(2) == 1 )then                       ! *** Full heat balance`와 `P/Transport/mod_heat.f90:689` `elseif( ISTOPT(2) == 2 )then                   ! *** COARE 3.6`이다. 수치: EFDC+는 활성 바닥층의 실제 물층 두께 `HPK`로 저질 열교환을 환산한다. 근거는 `P/Transport/mod_heat.f90:924` `TFLUX = ( HTBED1*USPD + HTBED2 )*( TEMB(L) - TEMP )*DELT   ! *** C*m`와 `P/Transport/mod_heat.f90:928` `THICK = HPK(L,KSZ(L))`이다. |
| `CALHEATBGVC` (`calheatbgvc.for`) | 독립 `CALHEATB/CALHEATBGVC`는 EFDC+에 없음. 저질 열교환 역할은 `CALHEAT` (`Transport/mod_heat.f90`)에 있다. | 수치: GVC는 `TEMB(L,K)`의 다층 저질 열확산과 바닥 물층을 연성한다. EFDC+는 `TEMB(L)`과 열 플럭스를 갱신한다. 근거는 `G/calheatbgvc.for:143` `BBEDTEM(L,K)=(1./DELT)-ABEDTEM(L,K)-CBEDTEM(L,K)`, `G/calheatbgvc.for:191` `TEMB(L,K)=UBEDTEM(L,K)`, `G/calheatbgvc.for:196` `TEM(L,KGVCP(L))=UBEDTEM(L,KBH)`, `P/Transport/mod_heat.f90:924` `TFLUX = ( HTBED1*USPD + HTBED2 )*( TEMB(L) - TEMP )*DELT   ! *** C*m`, `P/Transport/mod_heat.f90:978` `TEMB(L) = TEMB(L) + ( RHOWCPI*RADBOTT(L) - FLUXTB(L) )/TBEDTHK(L)        ! *** Update bed temperature`이다. 이 구현을 같은 저질 열모델로 판정하지 않는다. |
| `WQ3D` (`wq3d.for`) | `WQ3D` (`Eutrophication/mod_wq.f90`) | 흐름: GVC의 `WQ3D`는 물리 수송을 별도 호출한다. EFDC+는 수질 변수를 공통 `CALCONC` 수송 목록에 연결한다. 근거는 `G/wq3d.for:182` `IF(IGRIDV.EQ.1) CALL CALWQCGVC(2)`, `P/varinit.f90:343` `if( ISTRAN(8) > 0 )then`, `P/varinit.f90:348` `IACTIVEWC1(NACTIVEWC) = 8`, `P/varinit.f90:352` `WCV(NACTIVEWC).VAL0 => WQV(:,:,MW)`, `P/Transport/calconc.f90:203` `call CALTRAN( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )`이다. EFDC+의 `WQ3D`는 반응식과 저질모델을 호출한다. 근거는 `P/Eutrophication/mod_wq.f90:335` `if( ISWQLVL == 1 ) CALL WQSKE1 ! *** Extension of CEQUAL-ICM for unlimited algae + zooplankton`와 `P/Eutrophication/mod_wq.f90:354` `call SMMBE`이다. |
| `CALWQCGVC` (`calwqcgvc.for`) | 독립 `CALWQC/CALWQCGVC`는 EFDC+에 없음. 역할 대응은 `CALCONC` (`Transport/calconc.f90`)다. | 수치: GVC는 `NW`별 복사 배열을 수송한 뒤 별도의 수질 연직 확산을 계산한다. EFDC+는 수질 포인터와 공통 농도 연직 확산을 사용한다. 근거는 `G/calwqcgvc.for:80` `CALL CALTRWQGVC (8,NW,CWQ,CWQ2)`, `G/calwqcgvc.for:137` `CCUBTMP=RCDZKK*GVCSCLPI(L)*HWQI(L)*SWB3D(L,1)*AB(L,1)`, `P/varinit.f90:352` `WCV(NACTIVEWC).VAL0 => WQV(:,:,MW)`, `P/varinit.f90:353` `WCV(NACTIVEWC).VAL1 => WQV(:,:,MW)`, `P/Transport/calconc.f90:353` `RCDZKK  = -DELT*CDZKK(L,KSZ(L))`이다. |
| `CALTRWQGVC` (`caltrwqgvc.for`) | 독립 `CALTRWQ/CALTRWQGVC`는 EFDC+에 없음. 역할 대응은 `CALTRAN` (`Transport/caltran.f90`)과 선택 수송 경로다. | 입력·수치: GVC의 수질 전용 인자는 `M,NW,CON,CON1`이다. EFDC+의 수질 변수는 공통 활성 변수 목록으로 들어간다. 근거는 `G/caltrwqgvc.for:6` `SUBROUTINE CALTRWQGVC (M,NW,CON,CON1)`, `P/varinit.f90:348` `IACTIVEWC1(NACTIVEWC) = 8`, `P/varinit.f90:349` `IACTIVEWC2(NACTIVEWC) = MSVWQV(MW)`, `P/varinit.f90:352` `WCV(NACTIVEWC).VAL0 => WQV(:,:,MW)`이다. GVC의 `HWQ` 환산식은 `G/caltrwqgvc.for:217` `CON(L,K)=SCB(L)*CH(L,K)*GVCSCLPI(L)/HWQ(L)+(1.-SCB(L))*CON1(L,K)`이다. EFDC+의 층 두께 환산식은 `P/Transport/caltran.f90:204` `CON(L,K) = CD(L,K,IT)*HPKI(L,K)`이다. |
| `WQSKE3GVC` (`wqske3gvc.for`) | 물리 역할 대응은 `WQSKE1` (`Eutrophication/mod_wq.f90`)다. 옛 모듈 3 계산 구현은 EFDC+에 없음. | 물리·입력: EFDC+의 표준 전체 반응식은 모듈 1이다. 문서 근거는 `DK:10` `For the EFDC+ version, the standard full kinetic module is Module 1 (ISWQLVL=1).`이다. 코드 근거는 `P/Eutrophication/mod_wq.f90:335` `if( ISWQLVL == 1 ) CALL WQSKE1 ! *** Extension of CEQUAL-ICM for unlimited algae + zooplankton`와 `P/Eutrophication/mod_wq.f90:2872` `!> @details  Modeling of unlimited algae groups`이다. EFDC+의 `WQSKE3`는 `P/Eutrophication/mod_wq.f90:5171` `PRINT *,'WQSKE3 HAS BEEN REMOVED.  NEEDS CODE IF IWQSKE = 3 IMPLEMENTED'`을 출력하고 `P/Eutrophication/mod_wq.f90:5173` `return`한다. 같은 모듈 번호를 그대로 대응시키지 않는다. |
| `SMMBEGVC` (`smmbegvc.for`) | `SMMBE` (`Eutrophication/mod_diagen.f90`) | 흐름: GVC 원문의 전용판은 호출되지 않는다. EFDC+의 `WQ3D`는 `SMMBE`를 호출한다. 근거는 §2.3과 `P/Eutrophication/mod_wq.f90:354` `call SMMBE`이다. 물리·수치: EFDC+의 `SMMBE`는 `KSZ`층의 수온과 산소를 사용한다. 근거는 `P/Eutrophication/mod_diagen.f90:742` `SMT(L) = (SMT(L) + SM1DIFT(IZ)*TEM(L,KSZ(L))) * SM2DIFT(IZ)`와 `P/Eutrophication/mod_diagen.f90:828` `XSMO20(L) = max( WQV(L,KSZ(L),IDOX), 3.0 )`이다. |
| `WASPHYDROLINKGVC` (`wasphydrolinkgvc.for`) | 출력 역할 대응은 `WASP7HYDRO/WASP8HYDRO` (`Linkages/wasp7hydro.f90`, `Linkages/wasp8hydro.f90`)다. 독립 `WASPHYDROLINKGVC`는 EFDC+에 없음. | 수치·출력: EFDC+의 세그먼트 두께는 셀별 `DZC(L,K)`를 사용한다. 근거는 `P/Linkages/wasp7hydro.f90:1074` `SegDepth(LWASP) = HP(L)*DZC(L,K)`이다. 활성 출력 호출은 `CALMMT`의 `WASPOUT` 전처리 조건 안에서 `ISWASP=17`일 때 `WASP8HYDRO`를 가리킨다. 근거는 `P/Post_Processing/calmmt.f90:580` `#ifdef WASPOUT`와 `P/Post_Processing/calmmt.f90:586` `if( ISWASP == 17 ) CALL WASP8HYDRO`이다. 이 행은 파일 형식의 완전 호환성을 판정하지 않는다. |

### 3.3 SGZ와 GVC의 핵심 수치 차이

확인: GVC의 `KLTMP`는 활성층 수다. EFDC+의 `sgzlayer.inp`에 들어가는 `K`는 최하 활성층 인덱스다. 근거는 `G/setgvc.for:151` `READ(1,*)I,J,KLTMP`, `G/setgvc.for:160` `KGVCP(L)=KC-KLTMP+1`, `P/aaefdc.f90:1344` `read(1,*,END = 1000) IIN, JIN, K`, `P/aaefdc.f90:1356` `KSZ_Global(LG) = K`이다.

해석: GVC의 활성층 수를 EFDC+의 최하 활성층 인덱스로 옮기는 관계는 `K=KC-KLTMP+1`이다. 이 관계는 위 코드의 인덱스 정의에서 얻었다. 이 관계만으로 전체 입력을 변환할 수 있다고 판정하지 않는다.

확인: GVC 열 계산의 물층 두께는 `DZC(K)*GVCSCLP(L)*HP(L)` 형태다. 근거는 `G/calheatbgvc.for:119` `THICKWAT=DZC(KBOT)*GVCSCLP(L)*HP(L)`이다. EFDC+의 물층 두께는 `HP(L)*DZC(L,K)`다. 근거는 `P/aaefdc.f90:2615` `HPK(L,K) = HP(L)*DZC(L,K)`이다.

확인: GVC는 면 시작층의 최댓값과 면 척도를 설정한다. 근거는 `G/setgvc.for:281` `KGVCU(L)=MAX(KGVCP(L),KGVCP(L-1))   ! *** Maximum layer number of active bottom layer`와 `G/setgvc.for:283` `GVCSCLU(L)=FLOAT(KC)/FLOAT(KLTMP)   ! *** Ratio of Total/Minimum Active Layers`이다. EFDC+는 셀별 층 비율을 설정한 뒤 면별 층 비율을 정한다. 근거는 `P/aaefdc.f90:1443` `if( IGRIDV == 1 ) DZC(L,K) = DZCK(K)/DZPC`, `P/aaefdc.f90:2398` `SGZU(L,K)  = DZC(LW,K)`, `P/aaefdc.f90:2400` `SGZU(L,K)  = DZC(L,K)`이다.

확인: EFDC+는 서쪽 이웃의 활성 바닥층이 더 높으면 서쪽 면의 바닥 높이를 옮긴다. EFDC+는 그 아래 층의 두께 비율을 면의 활성층에 재배분한다. 근거는 `P/aaefdc.f90:2667` `if( KSZ(LW) > KSZ(L) )then`, `P/aaefdc.f90:2669` `BELVW(L) =  BELVW(L) + HPK(L,K)`, `P/aaefdc.f90:2672` `DZCAD = DZCBT/(KC-KSZ(LW)+1.)`, `P/aaefdc.f90:2675` `SGZW(L,K)  = DZC(L,K) + DZCAD`이다. 이 처리는 이론서의 면별 층 정합 설명과 연결된다.

해석: 확인한 대응은 전용 파일을 일반 파일로 합친 것보다 범위가 넓다. 셀별 층 두께, 면별 격자, 부력 적분, 농도 수송 구조가 함께 달라졌다. 이 문서는 두 판본의 오차 크기, 안정성, 보존 성능을 비교하지 않았다.

## 4. 현재 노트의 서술 판정과 수정안

### 4.1 서술별 판정

표의 노트 인용은 수정 전 원문이다. `확인`은 이번 원문 대조가 해당 범위의 서술을 지지한다는 뜻이다. `수정`은 조건, 수량, 역할 또는 근거 수준을 고쳐야 한다는 뜻이다. `보류`는 이번 계산 흐름 대조 범위에서 다시 판정하지 않았다는 뜻이다.

| 현재 노트 위치와 원문 | 판정 | 근거와 수정 방향 |
|---|---|---|
| `N:19` `USEPA 가 한때 배포하던 EFDC 소스코드를 기반으로 EEMS 연동·버그 수정을 입힌 것.`<br>`N:33` `\| 계보 \| USEPA 배포 EFDC → DSI 가 EEMS 연동·버그픽스 \|` | 확인 | 저장된 README는 EPA 배포 코드와 DSI 수정 사실을 적는다. 근거는 `G/README.md:4` `EFDC-GVC code refers to the code that was developed and previously was provided by US Environmental Protection Agency (USEPA).`와 `G/README.md:4` `DSI has modified the EFDC-GVC code to work with EEMS.`이다. |
| `N:19` `DSI 는 공식적으로 신규 모델에는 GVC 대신 EFDC+ 전환을 권장한다.`<br>`N:35` `\| 권장 \| 신규/진행중 모델에는 GVC 비권장, EFDC+ 전환 권고 \|` | 수정 | README의 직접 권고 대상은 `on-going models`다. 근거는 `G/README.md:4` `DSI recommends that users not use the GVC code for on-going models and make the conversion to EFDC+.`이다. 수정안은 진행 중인 모델의 EFDC+ 전환 권고로 쓴다. |
| `N:36` `\| 지원 \| "provided as-is without any support" (무지원) \|` | 확인 | 원문은 `G/README.md:6` `Please do note that this code is provided as-is without any support.`이다. |
| `N:44` ``- 트리 전체 **342 파일, 그중 293 개가 `.for`** fixed-form FORTRAN (ls 확장자 집계: `for 293`, `f 6`, `f90 2`, `CMN 1`, `PAR 1`).`` | 수량 확인 | 2026-10-08 파일명 집계는 허용된 GVC 전체 트리에서 342개 파일과 293개 `.for`를 얻었다. GVC 바로 아래 파일은 313개다. 노트의 전체 트리 수량은 맞다. 이 집계는 빌드에 포함하는 소스 수를 뜻하지 않는다. |
| `N:45` ``- Visual Studio 솔루션 `EFDC_GVC_2010.sln` + Intel Fortran 프로젝트 `EFDC_GVC_2010.vfproj` (**293 `<File ` 엔트리**, grep 집계). 즉 Windows/Intel Fortran 2010 빌드 환경.``<br>`N:47` ``- `EFDC.PAR` (9.1 KB) — `PARAMETER` 차원 상수 (LCM, KCM, ICM, JCM 등 컴파일타임 배열 크기).`` | 보류 | 프로젝트 파일 본문과 `EFDC.PAR`의 선언·크기는 이번 대조에서 확인하지 않았다. 빌드 환경과 공통 헤더 상세를 새 판정으로 승계하지 않는다. |
| `N:48` `모든 서브루틴의 공통블록 공유는 성립하지 않는다.` | 제한 범위 확인 | `CSEDSET`의 include는 `G/csedset.for:19` `INCLUDE 'EFDC.PAR'`와 `G/csedset.for:20` `INCLUDE 'EFDC.CMN'`이다. `LUBKSB`의 인자 시그니처는 `G/lubksb.for:6` `SUBROUTINE LUBKSB(A,N,NP,INDX,B)`이다. 배열 선언은 `G/lubksb.for:21` `DIMENSION A(NP,NP),INDX(N),B(N)`이다. `G/lubksb.for` 전체 1–46줄에는 `COMMON`과 `INCLUDE` 사용문이 없다. 이번 표는 공통 헤더 본문의 모든 선언을 판정하지 않는다. |
| `N:52` ``- `aaefdc.for:14` `PROGRAM AAEFDC` — 마스터 프로그램. 헤더 `aaefdc.for:5` "FILE FOR EFDC-FULL VERSION 1.0a", `aaefdc.for:144` "LAST MODIFIED BY JOHN HAMRICK ON 1 NOVEMBER 2001".``<br>`N:53` `2001~2004 빈티지 Hamrick 코드베이스` | 수정 | 프로그램 이름과 헤더 문구는 확인했다. 그러나 헤더의 최종 수정일로 전체 판본의 수정 기간을 정할 수 없다. GVC 링크 루틴에는 2006년 생성 기록도 있다. 근거는 `G/aaefdc.for:14` `PROGRAM AAEFDC`, `G/aaefdc.for:144` `C **  LAST MODIFIED BY JOHN HAMRICK ON 1 NOVEMBER 2001`, `G/wasphydrolinkgvc.for:14` `C   4/4/2006   Hugo Rodriguez Create the subroutine`이다. |
| `N:54` `표준 σ=0 / GVC=1`<br>`N:55` ``- `aaefdc.for:957` `IF(IGRIDV.EQ.1) CALL SETGVC` — GVC 초기화.``<br>`N:56` ``- `aaefdc.for:2598-2599` `IF(IGRIDV.EQ.0) CALL HDMT` / `IF(IGRIDV.EQ.1) CALL HDMTGVC` — 수력동역학 메인루프 σ vs GVC 이원화.`` | 조건 보완 | `IGRIDV`의 두 경로는 확인했다. §1.2의 `ISLTMT`, `IS1DCHAN`, `IS2TIM` 조건을 추가한다. |
| `N:62` `셀마다 (a) 활성 수직층 인덱스 범위와 (b) 층두께 스케일링을 달리해`<br>`N:64` ``> `setgvc.for:117-118` — "LCTV AND IJCTV EQUAL 1 FOR FOR RESCALED HEIGHT CELLS AND 2 FOR SIGMA CELLS" — 즉 **재척도화-높이(rescaled-height) 셀(=1)** 과 **순수 σ 셀(=2)** 혼용.`` | 구현 확인 | `KGVCP`, `GVCSCLP`, 두 셀 유형은 §2.1의 원문과 맞는다. 천수·급경사 오차를 완화한다는 성능 설명은 구현 사실과 구분한다. 이번 대조는 성능을 검증하지 않았다. |
| `N:70` ``\| `KGVCP/KGVCU/KGVCV/KGVCW(LCM)` \| `EFDC.CMN:358-359` \| 셀 L 의 P/U/V/W 점 **최하단 활성 수직층 인덱스** (그 아래 층은 비활성) \|`` | 수정 | `KGVCP/KGVCU/KGVCV`의 역할은 §2.1과 맞는다. `KGVCW`를 실제 연직 면 활성층 인덱스로 함께 설명하지 않는다. `AINIT`의 초기화 외 사용문을 찾지 못했다. 실제 연직 면 마스크는 `LGVCW`다. |
| `N:78` ``- 입력파일 2종: `setgvc.for:79` `OPEN(1,FILE='CELLGVC.INP',...)` (셀별 수직타입 맵 `IJCTV`), `setgvc.for:144` `OPEN(1,FILE='GVCLAYER.INP',...)` (셀별 활성층 수, `ISETGVC.EQ.0` 일 때).``<br>`N:79` `` 경계층 `GVCSCL*=1.0` `` | 일부 수정 | 두 입력 파일과 `ISETGVC=0` 조건은 확인했다. 그러나 `G/setgvc.for:59` `GVCSCLP(LC)=0.0`는 `GVCSCLP(LC)=0.0`을 설정한다. 모든 경계 척도를 1이라고 쓰지 않는다. |
| `N:85` ``- `calexpgvc.for:124-125` `UHC=0.5*(GVCSCLU(L)*UHDY2(L,K)+GVCSCLU(LS)*UHDY2(LS,K))` — U-플럭스에 셀별 스케일 적용.``<br>`N:86` ``- `calexpgvc.for:450,454` `FUHU/FUHV` 모멘텀 플럭스, `calexpgvc.for:493,509` `...*HP(L)*GVCSCLP(L)` — P점 스케일.`` | 확인 | `CALEXPGVC`의 면 척도 사용은 §2.2의 원문과 맞는다. 운동량 플럭스의 원문은 `G/calexpgvc.for:450` `FUHU(L,K)=0.25*(GVCSCLU(L+1)*UHDY(L+1,K)+GVCSCLU(L)*UHDY(L,K))`와 `G/calexpgvc.for:454` `FUHV(L,K)=0.25*(GVCSCLU(L)*UHDY(L,K)+GVCSCLU(LS)*UHDY(LS,K))`이다. 셀 중심 척도는 코리올리·곡률 가속 계수에 적용한다. 원문은 `G/calexpgvc.for:477` `C **  CALCULATE CORIOLIS AND CURVATURE ACCELERATION COEFFICIENTS`, `G/calexpgvc.for:493` `&        -0.5*SNLT*(U(L+1,K)+U(L,K))*DXDJ(L) )*HP(L)*GVCSCLP(L)`, `G/calexpgvc.for:509` `&        -0.5*SNLT*(U(L+1,K)+U(L,K))*DXDJ(L) )*HP(L)*GVCSCLP(L)`이다. |
| `N:97` `IF(K.LT.KGVCP(L)) SAL(L,K)=0.0      ! aaefdc.for:1870`<br>`N:98` `IF(K.LT.KGVCP(L)) SAL1(L,K)=0.0     ! aaefdc.for:1871` | 줄 번호 수정 | 실제 현재 원문의 `SAL=0`은 1871줄이다. `SAL1=0`은 1872줄이다. 근거는 `G/aaefdc.for:1871` `IF(K.LT.KGVCP(L)) SAL(L,K)=0.0`와 `G/aaefdc.for:1872` `IF(K.LT.KGVCP(L)) SAL1(L,K)=0.0`이다. |
| `N:103` ``### 3.4 GVC 전용 파일 인벤토리 (`*gvc.for`, 18개)``<br>`N:105` `ls 집계 (전부 표준 비-GVC 루틴의 GVC 대응판):` | 수정 | 현재 `*gvc.for`는 §2.2 목록의 17개다. `SETGVC`를 포함하므로 모두 일반 루틴 복제판이라고 쓰지 않는다. 파일 목록과 활성 호출 여부를 분리한다. |
| `N:116` ``\| `calconcgvc.for` \| `calconc.for` \| GVC 농도 디스패처 (→ `CALTRANGVC` 호출, `calconcgvc.for:266-326`) \|`` | 조건 보완 | `CALTRANGVC` 호출은 `ISTRAN=1`과 `ISCDCA<4` 조건을 갖는다. 다른 수송 선택문은 일반 `COSTRANW/COSTRAN`을 가리킨다. 근거는 §2.3이다. |
| `N:121` ``\| `smmbegvc.for` \| sediment 수지 \| GVC 질량수지 \|`` | 수정 | `SMMBEGVC`는 수질 저질모델 제어 루틴이다. 근거는 `G/smmbegvc.for:26` `C  CONTROL SUBROUTINE FOR SEDIMENT COMPONENT OF WATER QUALITY MODEL`이다. 총 퇴적물 수지의 별도 루틴은 `G/budget5.for:23` `C **  SUBROUTINES BUDGETN CALCULATE SEDIMENT BUDGET (TOTAL SEDIMENTS)`에 역할을 적는다. `SMMBEGVC`의 활성 호출 부재도 추가한다. |
| `N:123` ``\| `calebigvc.for` \| — \| GVC EBI \|`` | 수정 | `EBI`는 외부 부력 적분이다. 일반 대응은 `CALEBI`다. 근거는 `G/calebigvc.for:19` `C **  CALEBI CALCULATES THE EXTERNAL BUOYANCY INTEGRALS`와 `G/calebi.for:19` `C **  CALEBI CALCULATES THE EXTERNAL BUOYANCY INTEGRALS`이다. |
| `N:126` `` `IGRIDV` 가 런타임에 둘 중 하나를 호출 ``<br>`N:126` `과도기적 설계` | 수정 | 주요 GVC 전용 루틴의 병행 구현은 확인했다. 모든 호출을 두 파일 중 하나의 단순 선택으로 일반화하지 않는다. 설계 의도를 `과도기적`이라고 단정하지 않는다. 근거는 §1.2와 §2.3이다. |
| `N:134` ``\| `caltrani.for` \| `SUBROUTINE CALTRANI (ISTL,M,CON,CON1)` (`:6`) \| "CALCULATES THE ADVECTIVE AND DIFFUSIVE TRANSPORT OF DISSOLVED OR SUSPENDED CONSITITUENT M ... A NEW VALUE AT TIME LEVEL (N+1). ... THE SOLUTION IS IMPLICIT" \| `caltrani.for:19-22` \|``<br>`N:135` ``\| `costranw.for` \| `SUBROUTINE COSTRANW (ISTL,IS2TL,MVAR,M,CON,CON1)` (`:6`) \| "COSTRAN CALCULATES THE ADVECTIVE TRANSPORT OF DISSOLVED OR SUSPENDED CONSITITUENT M ..." — `costranw.for:16-17` 변경기록 "added dynamic time stepping" (2002-03-05), `costranw.for:45` `IF(ISDYNSTP.EQ.0)` 동적 타임스텝 분기 \| `costranw.for:20-23` \|`` | 구현·호출 분리 | `CALTRANI` 헤더의 암시적 해법 설명과 `COSTRANW`의 동적 시간간격 기록은 확인했다. 근거는 `G/caltrani.for:22` `C **  THE NUMBER OF TIME LEVELS IN THE STEP. THE SOLUTION IS IMPLICIT`와 `G/costranw.for:17` `C  added dynamic time stepping`이다. 활성 진입 경로 판정은 다음 행에서 고친다. |
| `N:136` ``\| `calwqcgvc.for` \| `SUBROUTINE CALWQCGVC (ISTL)` (`:6`) \| "CALWQC CALCULATES THE CONCENTRATION OF DISSOLVED AND SUSPENDED WATER QUALITY CONSTITUTENTS AT TIME LEVEL (N+1). CALLED ONLY ON ODD THREE TIME LEVEL STEPS" — GVC 수질 농도 드라이버 \| `calwqcgvc.for:19-21` \|`` | 호출 주기 수정 | 헤더의 `ODD`는 그대로 인용할 수 있다. 실제 `HDMTGVC`는 짝수 `N`에서 `WQ3D`를 호출한다. 헤더 설명과 호출 조건의 불일치를 §2.3처럼 명시한다. |
| `N:137` `SUBROUTINES BUDGETN CALCULATE SEDIMENT BUDGET (TOTAL SEDIMENTS)` | 역할 확인 | 원문은 `G/budget5.for:23` `C **  SUBROUTINES BUDGETN CALCULATE SEDIMENT BUDGET (TOTAL SEDIMENTS)`이다. 수지 기간 조건은 `G/budget5.for:34` `IF(NBUD.EQ.NTSMMT)THEN`이다. 이 판정은 GVC 척도가 수지 전체에 일관되게 적용되는지를 뜻하지 않는다. |
| `N:140` `` `caltrani` / `costranw` 는 σ-격자 표준 수송 루틴(GVC 접미사 없음) — `caltrani`(implicit advection-diffusion) vs `costranw`(explicit + 동적 타임스텝) 의 alternative 수송 스킴. GVC 활성 시 대응 `caltrangvc` 가 별도 사용된다. `` | 수정 | `CALCONC`와 `CALCONCGVC`의 `CALL CALTRANI`는 주석이다. 근거는 `G/calconc.for:411` `C     IF(ISTRAN(1).EQ.2) CALL CALTRANI (ISTL,1,SAL,SAL1)`와 `G/calconcgvc.for:340` `C     IF(ISTRAN(1).EQ.2) CALL CALTRANI (ISTL,1,SAL,SAL1)`이다. GVC 농도 제어에도 활성 `COSTRANW/COSTRAN` 경로가 있다. `CALTRANGVC`가 모든 대안을 대신한다는 설명을 고친다. |
| `N:150` ``\| 언어/형식 \| F77 fixed-form `.for` (293개) \| **Fortran 90 `.f90` 전부 (206개)**, 모듈화 \|`` | 수량 수정 | 이번 허용된 `P/**/*.f90` 파일명 집계는 208개다. 206개를 현 판본의 전체 수량으로 유지하지 않는다. 이 수량은 컴파일 대상 수를 뜻하지 않는다. |
| `N:151` ``\| 빌드 \| Windows VS2010 + Intel `.vfproj`/`.sln` \| **CMake** (`CMakeLists.txt` 존재) — 크로스플랫폼 \|``<br>`N:154` ``\| 병렬 \| (단일, MPI 미상) \| MPI 도메인 분할 (`efdc_mpi_decomposition.md` 참조) \|``<br>`N:155` ``\| 출력 \| 자체 바이너리/WASP 링크 \| netCDF (`mod_netcdf.f90`) 등 \|``<br>`N:156` `\| 위치 \| EFDC-FULL v1.0a, Hamrick 2001 \| DSI EFDC+ (GPL-3.0) \|` | 일부 보류 | 빌드 체계, MPI 분해, netCDF 출력, 라이선스 전문은 이번 계산 흐름 대조에서 다시 판정하지 않았다. WASP 출력 역할의 대응만 §3.2에서 확인했다. 소스의 라이선스 헤더만으로 라이선스 전문을 판정하지 않는다. |
| `N:153` ``\| 수직좌표 \| GVC = σ 루틴 + `*gvc` 평행 복제 (`IGRIDV` 분기) \| **SGZ (Sigma-Zed)** — GVC 후속, 통합 구현. `SGZ`/`KSZ` 토큰이 `caluvw.f90`·`hdmt.f90`·`aaefdc.f90` 등 코어에 직접 내장 (grep 확인) \|``<br>`N:160` `전면 재작성한 **상위(현행) 버전**`<br>`N:161` ``2. **GVC → SGZ**: 셀별 가변 수직층이라는 개념은 EFDC+ 의 **SGZ(Sigma-Zed)** 로 계승·통합. GVC 의 `*gvc` 복제 패턴이 SGZ 에서는 코어 루틴 내부 분기로 흡수됨.`` | 수정 | 주요 계산 역할의 대응은 §3.2에서 확인했다. 면별 층 정합과 수질·저질 열모델의 변경을 단순 흡수로 설명하지 않는다. `전면 재작성`과 `상위`는 이번 자료로 판정하지 않는다. 이론서 근거는 `T`, PDF 60쪽·인쇄 47쪽이다. |
| `N:169` ``- SGZ 와 GVC 의 수식적 정확한 차이(층 재배치 알고리즘)는 EFDC+ 측 코드/이론서 비교가 필요 — 본 노트는 **분기 구조·계보** 범위. SGZ 메커닉 상세는 `source-analysis/efdc_vertical.md` 범위.``<br>`N:170` ``- GVC 입력파일 `CELLGVC.INP`/`GVCLAYER.INP` 포맷 상세는 `setgvc.for` READ 문 외 메뉴얼 미대조 (source-needed for full format spec).`` | 갭 구체화 | 이 대조는 입력 읽기 방식과 면별 격자 처리 차이를 확인했다. 전체 좌표식 유도와 GVC 입력 매뉴얼의 완전 대조는 하지 않았다. 수정안은 이 남은 범위를 명시한다. |
| `N:6` `citation_status: verified`<br>`N:7` `aaefdc.for 디스패치(IGRIDV 분기) grep+read` | 근거 범위 수정안 | 노트의 기존 검증 상태는 이번 작업에서 변경하지 않았다. 수정안은 새 원문 대조 범위와 보류 항목을 구분한다. 기존 상태를 새 수치·물리 검증의 근거로 쓰지 않는다. |

파일 수의 근거는 2026-10-08의 저장소 파일명 집계다. GVC 집계는 `G/` 하위의 파일 이름을 세었다. EFDC+ 집계는 허용된 `P/**/*.f90` 이름을 세었다. 두 집계는 금지된 디렉터리 내부를 제외했다. 이 집계는 파일 내용을 모두 판독했다는 뜻이 아니다.

### 4.2 현재 노트에 넣을 수정안

아래 문장은 `N`의 해당 절을 대체하거나 보강할 수 있는 수정안이다. 이번 작업은 `N`을 직접 수정하지 않았다.

**진입점·디스패치 절의 수정안.** `AAEFDC`는 `ISLTMT=0`에서 수리동역학 시간 반복을 선택한다. `IS1DCHAN=0`과 `IS2TIM=0`이면 `IGRIDV=0`은 `HDMT`를 선택한다. 같은 조건에서 `IGRIDV=1`은 `HDMTGVC`를 선택한다. `IS1DCHAN=0`과 `IS2TIM>=1`이면 `HDMT2T`를 선택한다. `IS1DCHAN>=1`이면 `HDMT1D`를 선택한다. `ISLTMT>=1`이면 `LTMT`를 선택한다. 근거는 `G/aaefdc.for:2595` `IF(ISLTMT.EQ.0)THEN`, `G/aaefdc.for:2596` `IF(IS1DCHAN.EQ.0)THEN`, `G/aaefdc.for:2597` `IF(IS2TIM.EQ.0) THEN`, `G/aaefdc.for:2598` `IF(IGRIDV.EQ.0) CALL HDMT`, `G/aaefdc.for:2599` `IF(IGRIDV.EQ.1) CALL HDMTGVC`, `G/aaefdc.for:2601` `IF(IS2TIM.GE.1) CALL HDMT2T`, `G/aaefdc.for:2603` `IF(IS1DCHAN.GE.1) CALL HDMT1D`, `G/aaefdc.for:2605` `IF(ISLTMT.GE.1) CALL LTMT`이다.

**GVC 메커니즘 절의 수정안.** `SETGVC`는 셀 유형, 활성 바닥층, 셀과 면의 척도, 활성 마스크를 설정한다. 근거는 §2.1이다. 일반화 연직좌표의 물층 두께 계산은 `DZC(K)*GVCSCLP(L)*HP(L)`을 사용한다. 원문은 `G/calheatbgvc.for:119` `THICKWAT=DZC(KBOT)*GVCSCLP(L)*HP(L)`이다. `KGVCP`, `KGVCU`, `KGVCV`는 각각 셀 중심, U면, V면의 최하 활성층을 정한다. 연직 면의 실제 활성 판정은 `G/setgvc.for:347` `IF(LGVCP(L,K))THEN`, `G/setgvc.for:348` `IF(LGVCP(L,K+1))THEN`, `G/setgvc.for:349` `LGVCW(L,K)=.TRUE.`을 사용한다. `KGVCW`에는 초기화 사실만 적는다. 원문은 `G/ainit.for:242` `KGVCW(L)=1`이다.

**전용 파일 목록 절의 수정안.** 현재 트리의 `*gvc.for` 목록은 §2.2의 17개 파일이다. 목록은 파일별 역할과 일반 대응 루틴을 구분한다. `SMMBEGVC`의 역할은 수질 저질모델 제어다. 원문은 `G/smmbegvc.for:26` `C  CONTROL SUBROUTINE FOR SEDIMENT COMPONENT OF WATER QUALITY MODEL`이다. `CALEBIGVC`의 역할은 외부 부력 적분이다. 일반 대응은 `CALEBI`다. 원문은 `G/calebigvc.for:19` `C **  CALEBI CALCULATES THE EXTERNAL BUOYANCY INTEGRALS`와 `G/calebi.for:19` `C **  CALEBI CALCULATES THE EXTERNAL BUOYANCY INTEGRALS`이다. 활성 호출 여부는 §2.3의 조건과 검색 범위를 함께 적는다.

**수송과 수질 절의 수정안.** `CALCONCGVC`는 `ISCDCA<4`에서 `CALTRANGVC`를 선택한다. 원문은 `G/calconcgvc.for:265` `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).LT.4)`와 `G/calconcgvc.for:266` `&  CALL CALTRANGVC (ISTL,IS2TL,1,1,SAL,SAL1)`이다. 다른 활성 선택문은 `COSTRANW`와 `COSTRAN`을 사용한다. 원문은 `G/calconcgvc.for:378` `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).EQ.4)`, `G/calconcgvc.for:379` `&  CALL COSTRANW (ISTL,IS2TL,1,1,SAL,SAL1)`, `G/calconcgvc.for:385` `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).EQ.5)`, `G/calconcgvc.for:386` `&  CALL COSTRAN (ISTL,IS2TL,1,1,SAL,SAL1)`이다. `CALTRANI`의 농도 제어 호출은 주석이다. 원문은 `G/calconcgvc.for:340` `C     IF(ISTRAN(1).EQ.2) CALL CALTRANI (ISTL,1,SAL,SAL1)`이다. `HDMTGVC`의 `WQ3D` 호출은 짝수 `N`의 `ISTL=3` 경로에 있다. 원문은 `G/hdmtgvc.for:1007` `IF(NTMP.EQ.0.AND.ISTL.EQ.3)THEN`과 `G/hdmtgvc.for:1171` `IF(ISTRAN(8).GE.1) CALL WQ3D`이다. `CALWQCGVC` 헤더의 홀수 단계 설명은 이 조건과 구분한다. 원문은 `G/calwqcgvc.for:21` `C **  CALLED ONLY ON ODD THREE TIME LEVEL STEPS`이다.

**EFDC+ 대비 절의 수정안.** 이번 EFDC+ 소스는 SGZ 초기화를 `aaefdc.f90`에 넣는다. 원문은 `P/aaefdc.f90:1310` `if( IGRIDV > 0 )then`와 `P/aaefdc.f90:1339` `open(1,FILE = 'sgzlayer.inp',STATUS = 'UNKNOWN')`이다. EFDC+의 주요 계산 루틴은 셀별 층 두께와 면별 SGZ 계수를 사용한다. 근거는 §3.2다. 이론서는 면별 층 정합을 GVC와의 근본적 차이로 설명한다. 원문은 `T`, PDF 60쪽·인쇄 47쪽의 `face matching of layering is a fundamental difference with the GVC approach`이다. EFDC+의 표준 전체 수질 반응 모듈은 `WQSKE1`이다. 원문은 `P/Eutrophication/mod_wq.f90:335` `if( ISWQLVL == 1 ) CALL WQSKE1 ! *** Extension of CEQUAL-ICM for unlimited algae + zooplankton`이다. EFDC+의 `WQSKE3`는 계산을 제거했다는 안내문 뒤에 반환한다. 원문은 `P/Eutrophication/mod_wq.f90:5171` `PRINT *,'WQSKE3 HAS BEEN REMOVED.  NEEDS CODE IF IWQSKE = 3 IMPLEMENTED'`과 `P/Eutrophication/mod_wq.f90:5173` `return`이다. 같은 모듈 번호와 같은 파일 역할만으로 물리·수치 동등성을 판정하지 않는다.

**한계·검증 기록 절의 수정안.** 이번 대조는 진입 분기, 직접 호출 순서, GVC 전용 처리, EFDC+의 대응 구현을 확인했다. 이번 대조는 모델을 실행하지 않았다. 이번 대조는 두 판본의 수치 오차와 물리 타당성을 검증하지 않았다. 이번 대조는 포함 파일의 내부 선언, 빌드 프로젝트, 라이선스 전문을 판독하지 않았다. 이번 대조는 GVC 입력 매뉴얼의 전체 형식을 검증하지 않았다. 검증 기록은 §1–§3의 코드 줄과 문서 쪽을 새 근거로 연결한다. 수정된 서술의 사람 확인 상태는 별도로 남긴다.

열지 못한 파일: 없음.
