---
title: "EFDC-GVC 레거시 분기 — Generalized Vertical Coordinate (Hamrick/EPA 계열) 구조 요약"
model: EFDC
component: source-analysis/legacy-branch
canonical_source: self
citation_status: verified
verification_method: "기존 판독 기록: EFDC-GVC 파일·헤더·본문 대조. recovery 재판독 대조: 진입 분기, 직접 호출 순서, GVC 전용 처리, EFDC+ 대응 구현. 모델 실행·수치 오차·물리 타당성·공통 헤더 내부 선언·빌드 프로젝트·라이선스 전문·GVC 입력 매뉴얼 전체 형식은 확인하지 않음."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/EFDC/README.md
  - models/EFDC/source-analysis/efdc_vertical.md
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/source-analysis/efdc_transport_scheme.md
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

# EFDC-GVC 레거시 분기 — Generalized Vertical Coordinate (Hamrick/EPA 계열) 구조 요약

> EFDC-GVC 는 DSI 가 공개한 **EFDC 레거시 분기**로, USEPA 가 한때 배포하던 EFDC 소스코드를 기반으로 EEMS 연동·버그 수정을 입힌 것. FORTRAN77 계열 fixed-form(`.for`), `PROGRAM AAEFDC` 단일 진입점·`INCLUDE 'EFDC.PAR'/'EFDC.CMN'` 글로벌 공통블록 구조. 핵심 특징은 이름 그대로 **GVC(일반화 수직좌표)** 옵션 — 셀별로 활성 수직층 수와 스케일링을 달리해 표준 σ 격자의 한계를 보완. 현행 [[efdc]](EFDCPlus_Stable)(EFDC+) 와는 **구버전/계보** 관계이며, DSI는 진행 중인 모델을 EFDC+로 전환하도록 권고한다. (`EFDC-GVC/README.md:4` — `DSI recommends that users not use the GVC code for on-going models and make the conversion to EFDC+.`) (`README.md` 직접 인용, 아래 §1)

---

## 1. 분기 정체 — README 1차 출처

`EFDC-GVC/README.md` 원문 핵심 (verbatim 발췌):

> "DSI has made the Generalized Vertical Coordinate (GVC) version of EFDC code available. EFDC-GVC code refers to the code that was developed and previously was provided by US Environmental Protection Agency (USEPA). EPA stopped providing the source code for EFDC several years ago. DSI has modified the EFDC-GVC code to work with EEMS. The code has also been modified to correct bugs found. DSI provides this updated version ... for the modeling community that is looking to upgrade legacy modeling applications to DSI's EFDC+. ... DSI recommends that users not use the GVC code for on-going models and make the conversion to EFDC+."

요점 정리:

| 항목 | 내용 |
|---|---|
| 계보 | USEPA 배포 EFDC → DSI 가 EEMS 연동·버그픽스 |
| 의도 | 레거시 EFDC 적용모델의 **테스트용 오픈소스** 제공 + EFDC+ 전환 유도 |
| 권장 | DSI는 진행 중인 모델을 EFDC+로 전환하도록 권고한다. (`EFDC-GVC/README.md:4` — `DSI recommends that users not use the GVC code for on-going models and make the conversion to EFDC+.`) |
| 지원 | "provided as-is without any support" (무지원) |

---

## 2. 코드 구조 — FORTRAN77 계열 모놀리식

### 2.1 빌드/파일 구성

- 트리 전체 **342 파일, 그중 293 개가 `.for`** fixed-form FORTRAN (ls 확장자 집계: `for 293`, `f 6`, `f90 2`, `CMN 1`, `PAR 1`).
- Visual Studio 솔루션 `EFDC_GVC_2010.sln` + Intel Fortran 프로젝트 `EFDC_GVC_2010.vfproj` (**293 `<File ` 엔트리**, grep 집계). 즉 Windows/Intel Fortran 2010 빌드 환경.

프로젝트 파일 본문과 빌드 환경은 이번 대조에서 확인하지 않음.

- 공통블록 헤더 2개:
  - `EFDC.PAR` (9.1 KB) — `PARAMETER` 차원 상수 (LCM, KCM, ICM, JCM 등 컴파일타임 배열 크기).

EFDC.PAR의 내부 선언과 크기는 이번 대조에서 확인하지 않음.

  - `EFDC.CMN` (72 KB) — 전역 `COMMON` 블록 (공유 상태배열·플래그). `CSEDSET`은(`csedset.for:19-20`) `INCLUDE 'EFDC.PAR'`/`INCLUDE 'EFDC.CMN'` 로 공유 — 모듈/파생형 없는 전형적 F77 글로벌 상태 구조이다. `LUBKSB`는 인자 배열을 사용한다(`lubksb.for:6-40`); 모든 서브루틴의 공통블록 공유는 성립하지 않는다.

### 2.2 진입점·디스패치

- `aaefdc.for:14` `PROGRAM AAEFDC` — 마스터 프로그램. 헤더 `aaefdc.for:5` "FILE FOR EFDC-FULL VERSION 1.0a", `aaefdc.for:144` "LAST MODIFIED BY JOHN HAMRICK ON 1 NOVEMBER 2001".
- AAEFDC 헤더는 최종 수정일을 2001년 11월 1일로 적는다. (`EFDC-GVC/aaefdc.for:14` — `PROGRAM AAEFDC`) WASPHYDROLINKGVC에는 2006년 4월 4일 생성 기록이 있다. (`EFDC-GVC/aaefdc.for:14` — `PROGRAM AAEFDC`; `EFDC-GVC/aaefdc.for:144` — `C **  LAST MODIFIED BY JOHN HAMRICK ON 1 NOVEMBER 2001`; `EFDC-GVC/wasphydrolinkgvc.for:14` — `C   4/4/2006   Hugo Rodriguez Create the subroutine`) 전체 판본의 수정 기간은 이 헤더만으로 확인하지 않음. (`EFDC-GVC/aaefdc.for:14` — `PROGRAM AAEFDC`; `EFDC-GVC/aaefdc.for:144` — `C **  LAST MODIFIED BY JOHN HAMRICK ON 1 NOVEMBER 2001`; `EFDC-GVC/wasphydrolinkgvc.for:14` — `C   4/4/2006   Hugo Rodriguez Create the subroutine`)
- **수직격자 분기는 `IGRIDV` 플래그** (CMN 선언 `EFDC.CMN:1024`, 표준 σ=0 / GVC=1). `aaefdc.for` 디스패치:
  - `aaefdc.for:957` `IF(IGRIDV.EQ.1) CALL SETGVC` — GVC 초기화.
  - AAEFDC는 ISLTMT=0에서 수리동역학 시간 반복을 선택한다. (`EFDC-GVC/aaefdc.for:2595` — `IF(ISLTMT.EQ.0)THEN`; `EFDC-GVC/aaefdc.for:2605` — `IF(ISLTMT.GE.1) CALL LTMT`) IS1DCHAN=0과 IS2TIM=0이면 IGRIDV=0은 HDMT를 선택한다. (`EFDC-GVC/aaefdc.for:2596` — `IF(IS1DCHAN.EQ.0)THEN`; `EFDC-GVC/aaefdc.for:2597` — `IF(IS2TIM.EQ.0) THEN`; `EFDC-GVC/aaefdc.for:2598` — `IF(IGRIDV.EQ.0) CALL HDMT`; `EFDC-GVC/aaefdc.for:2599` — `IF(IGRIDV.EQ.1) CALL HDMTGVC`; `EFDC-GVC/aaefdc.for:2601` — `IF(IS2TIM.GE.1) CALL HDMT2T`; `EFDC-GVC/aaefdc.for:2603` — `IF(IS1DCHAN.GE.1) CALL HDMT1D`) 같은 조건에서 IGRIDV=1은 HDMTGVC를 선택한다. (`EFDC-GVC/aaefdc.for:2598` — `IF(IGRIDV.EQ.0) CALL HDMT`; `EFDC-GVC/aaefdc.for:2599` — `IF(IGRIDV.EQ.1) CALL HDMTGVC`) IS1DCHAN=0과 IS2TIM>=1이면 HDMT2T를 선택한다. (`EFDC-GVC/aaefdc.for:2596` — `IF(IS1DCHAN.EQ.0)THEN`; `EFDC-GVC/aaefdc.for:2597` — `IF(IS2TIM.EQ.0) THEN`; `EFDC-GVC/aaefdc.for:2601` — `IF(IS2TIM.GE.1) CALL HDMT2T`; `EFDC-GVC/aaefdc.for:2603` — `IF(IS1DCHAN.GE.1) CALL HDMT1D`) IS1DCHAN>=1이면 HDMT1D를 선택한다. (`EFDC-GVC/aaefdc.for:2596` — `IF(IS1DCHAN.EQ.0)THEN`; `EFDC-GVC/aaefdc.for:2603` — `IF(IS1DCHAN.GE.1) CALL HDMT1D`) ISLTMT>=1이면 LTMT를 선택한다. (`EFDC-GVC/aaefdc.for:2595` — `IF(ISLTMT.EQ.0)THEN`; `EFDC-GVC/aaefdc.for:2605` — `IF(ISLTMT.GE.1) CALL LTMT`)

---

## 3. GVC 메커닉 — 셀별 가변 수직층

SETGVC는 셀 유형·활성 바닥층·셀과 면의 척도·활성 마스크를 설정한다. (`EFDC-GVC/setgvc.for:160` — `KGVCP(L)=KC-KLTMP+1`; `EFDC-GVC/setgvc.for:161` — `GVCSCLP(L)=FLOAT(KC)/FLOAT(KLTMP)`; `EFDC-GVC/setgvc.for:349` — `LGVCW(L,K)=.TRUE.`; `EFDC-GVC/calheatbgvc.for:119` — `THICKWAT=DZC(KBOT)*GVCSCLP(L)*HP(L)`) 물층 두께는 DZC(K)*GVCSCLP(L)*HP(L)이다. (`EFDC-GVC/setgvc.for:161` — `GVCSCLP(L)=FLOAT(KC)/FLOAT(KLTMP)`; `EFDC-GVC/calheatbgvc.for:119` — `THICKWAT=DZC(KBOT)*GVCSCLP(L)*HP(L)`) 천수·급경사 오차 완화 성능은 확인하지 않음. (`EFDC-GVC/setgvc.for:160` — `KGVCP(L)=KC-KLTMP+1`; `EFDC-GVC/setgvc.for:161` — `GVCSCLP(L)=FLOAT(KC)/FLOAT(KLTMP)`; `EFDC-GVC/setgvc.for:349` — `LGVCW(L,K)=.TRUE.`; `EFDC-GVC/calheatbgvc.for:119` — `THICKWAT=DZC(KBOT)*GVCSCLP(L)*HP(L)`)

> `setgvc.for:117-118` — "LCTV AND IJCTV EQUAL 1 FOR FOR RESCALED HEIGHT CELLS AND 2 FOR SIGMA CELLS" — 즉 **재척도화-높이(rescaled-height) 셀(=1)** 과 **순수 σ 셀(=2)** 혼용.

핵심 전역배열 (모두 `EFDC.CMN` 선언):

| 배열 | 선언 위치 | 역할 |
|---|---|---|
| `KGVCP/KGVCU/KGVCV` | `EFDC.CMN:358-359` | KGVCP·KGVCU·KGVCV는 셀 중심·U면·V면의 최하 활성층을 정한다. (`EFDC-GVC/setgvc.for:160` — `KGVCP(L)=KC-KLTMP+1`; `EFDC-GVC/setgvc.for:281` — `KGVCU(L)=MAX(KGVCP(L),KGVCP(L-1))   ! *** Maximum layer number of active bottom layer`; `EFDC-GVC/setgvc.for:309` — `KGVCV(L)=MAX(KGVCP(L),KGVCP(LS))`) |
| `KGVCW`; `LGVCW` | `EFDC-GVC/ainit.for:242`; `EFDC-GVC/setgvc.for:347-349` | KGVCW는 1로 초기화한다. (`EFDC-GVC/ainit.for:242` — `KGVCW(L)=1`) 다른 KGVCW 사용문은 지정한 GVC 소스 검색에서 찾지 못했다. (`EFDC-GVC/ainit.for:242` — `KGVCW(L)=1`) 실제 연직 면 활성 판정은 LGVCW를 사용한다. (`EFDC-GVC/setgvc.for:349` — `LGVCW(L,K)=.TRUE.`) |
| `GVCSCLP/GVCSCLU/GVCSCLV(LCM)` + 역수 `*I` | `EFDC.CMN:173` | P/U/V 점 **층두께 스케일 계수** (및 inverse) |
| `LCTV(L)` / `IJCTV(I,J)` | setgvc | 셀 수직타입 (1=rescaled, 2=sigma) |
| 제어 플래그 `IGRIDV, ISETGVC, ISGVCCK` | `EFDC.CMN:1024` | GVC on/off, 설정모드, 체크 |

### 3.1 `SETGVC` (`setgvc.for`) — GVC 초기화 리더

- `setgvc.for:6` `SUBROUTINE SETGVC`, 헤더 `setgvc.for:21-22` "READS INFORMATION FOR THE GENERALIZED VERTICAL COORDINATE OPTION AND SETS REAL AND LOCICAL MASK".
- 입력파일 2종: `setgvc.for:79` `OPEN(1,FILE='CELLGVC.INP',...)` (셀별 수직타입 맵 `IJCTV`), `setgvc.for:144` `OPEN(1,FILE='GVCLAYER.INP',...)` (셀별 활성층 수, `ISETGVC.EQ.0` 일 때).
- SETGVC의 초기화는 GVCSCLP(LC)=0.0을 설정한다. (`EFDC-GVC/setgvc.for:59` — `GVCSCLP(LC)=0.0`) 모든 경계 척도가 1인 것은 아니다. (`EFDC-GVC/setgvc.for:59` — `GVCSCLP(LC)=0.0`)

### 3.2 GVC 스케일 계수의 플럭스 적용 — `CALEXPGVC`

`calexpgvc.for` (표준 `calexp.for` 의 GVC 대응) 에서 수송 플럭스를 `GVCSCL*` 로 가중:

- `calexpgvc.for:124-125` `UHC=0.5*(GVCSCLU(L)*UHDY2(L,K)+GVCSCLU(LS)*UHDY2(LS,K))` — U-플럭스에 셀별 스케일 적용.
- `calexpgvc.for:450,454` `FUHU/FUHV` 모멘텀 플럭스, `calexpgvc.for:493,509` `...*HP(L)*GVCSCLP(L)` — P점 스케일.

### 3.3 농도 마스킹 — 비활성층 0 처리

`aaefdc.for:1864-1875` GVC 보정 블록 "CORRECT CONCENTRATIONS FOR GVC":

```fortran
IF(IGRIDV.EQ.1)THEN
 IF(ISTRAN(1).GE.1)THEN
   DO K=1,KC
   DO L=1,LC
    IF(K.LT.KGVCP(L)) SAL(L,K)=0.0      ! aaefdc.for:1871
    IF(K.LT.KGVCP(L)) SAL1(L,K)=0.0     ! aaefdc.for:1872
```

비활성층의 SAL과 SAL1 대입은 각각 aaefdc.for:1871·1872에 있다. (`EFDC-GVC/aaefdc.for:1871` — `IF(K.LT.KGVCP(L)) SAL(L,K)=0.0`; `EFDC-GVC/aaefdc.for:1872` — `IF(K.LT.KGVCP(L)) SAL1(L,K)=0.0`)


→ `KGVCP(L)` 미만(=비활성 하부층) 의 스칼라(염분 등)를 명시적으로 0 처리. GVC 의 "셀마다 활성층 수가 다름" 을 농도장에서 강제하는 부분.


<!-- count: models/EFDC/raw/source_code/EFDC-GVC/*gvc.for = 17 -->

### 3.4 GVC 전용 파일 인벤토리 (`*gvc.for`, 17개)

파일 수는 `models/EFDC/raw/source_code/EFDC-GVC/*gvc.for` 목록에서 셌다. 파일의 존재와 활성 호출 여부를 구별한다.

| 파일 | 대응 표준 | 역할(헤더 기반) |
|---|---|---|
| `setgvc.for` | (신규) | GVC 초기화·입력 리더 |
| `hdmtgvc.for` | `hdmt.for` | GVC 수력동역학 메인루프 |
| `calexpgvc.for` | `calexp.for` | GVC explicit 모멘텀/플럭스 |
| `caltrangvc.for` | `caltran.for` | GVC 스칼라 advection-diffusion 수송 |
| `caluvwgvc.for` | `caluvw.for` | GVC 3D 유속(U,V,W) |
| `calpuv9gvc.for` | `calpuv*.for` | GVC 외부모드(표면 z, P-U-V) 해 |
| `calqq1gvc.for` | `calqq1.for` | GVC 난류 폐합 (q²) |
| `calconcgvc.for` | 코드·문서 대조 | CALCONCGVC는 ISTRAN=1과 ISCDCA<4에서 CALTRANGVC를 선택한다. (`EFDC-GVC/calconcgvc.for:265` — `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).LT.4)`; `EFDC-GVC/calconcgvc.for:266` — `&  CALL CALTRANGVC (ISTL,IS2TL,1,1,SAL,SAL1)`; `EFDC-GVC/calconcgvc.for:378` — `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).EQ.4)`; `EFDC-GVC/calconcgvc.for:385` — `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).EQ.5)`) 다른 활성 선택문은 COSTRANW와 COSTRAN을 사용한다. (`EFDC-GVC/calconcgvc.for:379` — `&  CALL COSTRANW (ISTL,IS2TL,1,1,SAL,SAL1)`; `EFDC-GVC/calconcgvc.for:386` — `&  CALL COSTRAN (ISTL,IS2TL,1,1,SAL,SAL1)`) |
| `calheatgvc/calheatbgvc.for` | `calheat*.for` | GVC 열수지 |
| `calwqcgvc.for` | `calwqc.for` | GVC 수질 농도 (아래 §4) |
| `caltrwqgvc.for` | `caltrwq.for` | GVC 수질 수송 |
| `wqske3gvc.for` | `wqske*.for` | GVC 수질 동역학 (eutrophication kinetics) |
| `smmbegvc.for` | 코드·문서 대조 | SMMBEGVC는 수질 저질모델 제어 루틴이다. (`EFDC-GVC/smmbegvc.for:26` — `C  CONTROL SUBROUTINE FOR SEDIMENT COMPONENT OF WATER QUALITY MODEL`; `EFDC-GVC/wq3d.for:267` — `CALL SMMBE`) 지정한 GVC 소스에는 활성 CALL SMMBEGVC가 없다. (`EFDC-GVC/wq3d.for:267` — `CALL SMMBE`) WQ3D는 일반 SMMBE를 호출한다. (`EFDC-GVC/wq3d.for:267` — `CALL SMMBE`) |
| `calavbgvc.for` | `calavb.for` | GVC 수직 와점성/확산 |
| `calebigvc.for` | 코드·문서 대조 | CALEBIGVC는 외부 부력 적분을 계산한다. (`EFDC-GVC/calebigvc.for:19` — `C **  CALEBI CALCULATES THE EXTERNAL BUOYANCY INTEGRALS`; `EFDC-GVC/calebi.for:19` — `C **  CALEBI CALCULATES THE EXTERNAL BUOYANCY INTEGRALS`) 일반 대응 루틴은 CALEBI이다. (`EFDC-GVC/calebigvc.for:19` — `C **  CALEBI CALCULATES THE EXTERNAL BUOYANCY INTEGRALS`; `EFDC-GVC/calebi.for:19` — `C **  CALEBI CALCULATES THE EXTERNAL BUOYANCY INTEGRALS`) |
| `wasphydrolinkgvc.for` | `wasphydrolink.for` | GVC→WASP 수문 링크 |

> 주요 GVC 전용 루틴은 일반 루틴과 병행 구현한다. (`EFDC-GVC/hdmtgvc.for:633` — `IF(ISCHAN.EQ.0.AND.ISDRY.EQ.0) CALL CALPUV9GVC(ISTL)`; `EFDC-GVC/hdmtgvc.for:634` — `IF(ISCHAN.GE.1.OR.ISDRY.GE.1) CALL CALPUV9C(ISTL)`; `EFDC-GVC/hdmtgvc.for:518` — `IF(ISCDMA.EQ.5) CALL CALEXP2 (ISTL)`; `EFDC-GVC/hdmtgvc.for:519` — `IF(ISCDMA.EQ.6) CALL CALEXP2 (ISTL)`; `EFDC-GVC/hdmtgvc.for:520` — `IF(ISCDMA.EQ.9) CALL CALEXP9 (ISTL)`) HDMTGVC의 외부모드 선택에는 일반 CALPUV9C 경로도 있다. (`EFDC-GVC/hdmtgvc.for:634` — `IF(ISCHAN.GE.1.OR.ISDRY.GE.1) CALL CALPUV9C(ISTL)`) HDMTGVC의 운동량 선택에는 일반 CALEXP2·CALEXP9 경로도 있다. (`EFDC-GVC/hdmtgvc.for:518` — `IF(ISCDMA.EQ.5) CALL CALEXP2 (ISTL)`; `EFDC-GVC/hdmtgvc.for:519` — `IF(ISCDMA.EQ.6) CALL CALEXP2 (ISTL)`; `EFDC-GVC/hdmtgvc.for:520` — `IF(ISCDMA.EQ.9) CALL CALEXP9 (ISTL)`) 과도기적 설계 의도는 확인하지 않음. (`EFDC-GVC/hdmtgvc.for:633` — `IF(ISCHAN.EQ.0.AND.ISDRY.EQ.0) CALL CALPUV9GVC(ISTL)`; `EFDC-GVC/hdmtgvc.for:634` — `IF(ISCHAN.GE.1.OR.ISDRY.GE.1) CALL CALPUV9C(ISTL)`; `EFDC-GVC/hdmtgvc.for:518` — `IF(ISCDMA.EQ.5) CALL CALEXP2 (ISTL)`; `EFDC-GVC/hdmtgvc.for:519` — `IF(ISCDMA.EQ.6) CALL CALEXP2 (ISTL)`; `EFDC-GVC/hdmtgvc.for:520` — `IF(ISCDMA.EQ.9) CALL CALEXP9 (ISTL)`)

---

## 4. 배정 대표 파일 헤더·역할 (file:line)

| 파일 | 시그니처 | 헤더 설명(verbatim) | 인용 |
|---|---|---|---|
| `caltrani.for` | `SUBROUTINE CALTRANI (ISTL,M,CON,CON1)` (`:6`) | "CALCULATES THE ADVECTIVE AND DIFFUSIVE TRANSPORT OF DISSOLVED OR SUSPENDED CONSITITUENT M ... A NEW VALUE AT TIME LEVEL (N+1). ... THE SOLUTION IS IMPLICIT" | `caltrani.for:19-22` |
| `costranw.for` | `SUBROUTINE COSTRANW (ISTL,IS2TL,MVAR,M,CON,CON1)` (`:6`) | "COSTRAN CALCULATES THE ADVECTIVE TRANSPORT OF DISSOLVED OR SUSPENDED CONSITITUENT M ..." — `costranw.for:16-17` 변경기록 "added dynamic time stepping" (2002-03-05), `costranw.for:45` `IF(ISDYNSTP.EQ.0)` 동적 타임스텝 분기 | `costranw.for:20-23` |
| `calwqcgvc.for` | `SUBROUTINE CALWQCGVC (ISTL)` (`:6`) | "CALWQC CALCULATES THE CONCENTRATION OF DISSOLVED AND SUSPENDED WATER QUALITY CONSTITUTENTS AT TIME LEVEL (N+1). CALLED ONLY ON ODD THREE TIME LEVEL STEPS" — GVC 수질 농도 드라이버 | `calwqcgvc.for:19-21` |

CALWQCGVC 헤더는 홀수 3시점 단계를 적는다. (`EFDC-GVC/calwqcgvc.for:21` — `C **  CALLED ONLY ON ODD THREE TIME LEVEL STEPS`; `EFDC-GVC/hdmtgvc.for:1006` — `NTMP=MOD(N,2)`; `EFDC-GVC/hdmtgvc.for:1007` — `IF(NTMP.EQ.0.AND.ISTL.EQ.3)THEN`; `EFDC-GVC/hdmtgvc.for:1171` — `IF(ISTRAN(8).GE.1) CALL WQ3D`) HDMTGVC는 짝수 N의 ISTL=3 경로에서 WQ3D를 호출한다. (`EFDC-GVC/hdmtgvc.for:1007` — `IF(NTMP.EQ.0.AND.ISTL.EQ.3)THEN`; `EFDC-GVC/hdmtgvc.for:1171` — `IF(ISTRAN(8).GE.1) CALL WQ3D`) 두 조건은 다르다. (`EFDC-GVC/calwqcgvc.for:21` — `C **  CALLED ONLY ON ODD THREE TIME LEVEL STEPS`; `EFDC-GVC/hdmtgvc.for:1006` — `NTMP=MOD(N,2)`; `EFDC-GVC/hdmtgvc.for:1007` — `IF(NTMP.EQ.0.AND.ISTL.EQ.3)THEN`; `EFDC-GVC/hdmtgvc.for:1171` — `IF(ISTRAN(8).GE.1) CALL WQ3D`)

| `budget5.for` | `SUBROUTINE BUDGET5` (`:6`) | "SUBROUTINES BUDGETN CALCULATE SEDIMENT BUDGET (TOTAL SEDIMENTS)" — `budget5.for:8` "ADDED BY DON KINGERY, CH2M-HILL ON 15 OCTOBER 1996". `NBUD.EQ.NTSMMT` 시 부유+저질 종료량 집계(`budget5.for:34,44-52`) | `budget5.for:23` |
| `setgvc.for` | `SUBROUTINE SETGVC` (`:6`) | §3.1 참조 — GVC 격자 초기화·`CELLGVC.INP`/`GVCLAYER.INP` 리더 | `setgvc.for:21-22` |

CALCONC와 CALCONCGVC의 CALL CALTRANI는 주석이다. (`EFDC-GVC/calconc.for:411` — `C     IF(ISTRAN(1).EQ.2) CALL CALTRANI (ISTL,1,SAL,SAL1)`; `EFDC-GVC/calconcgvc.for:340` — `C     IF(ISTRAN(1).EQ.2) CALL CALTRANI (ISTL,1,SAL,SAL1)`; `EFDC-GVC/calconcgvc.for:379` — `&  CALL COSTRANW (ISTL,IS2TL,1,1,SAL,SAL1)`; `EFDC-GVC/calconcgvc.for:386` — `&  CALL COSTRAN (ISTL,IS2TL,1,1,SAL,SAL1)`) CALCONCGVC의 활성 선택문에는 COSTRANW와 COSTRAN이 있다. (`EFDC-GVC/calconcgvc.for:379` — `&  CALL COSTRANW (ISTL,IS2TL,1,1,SAL,SAL1)`; `EFDC-GVC/calconcgvc.for:386` — `&  CALL COSTRAN (ISTL,IS2TL,1,1,SAL,SAL1)`) CALTRANGVC는 ISCDCA<4의 조건부 경로이다. (`EFDC-GVC/calconcgvc.for:378` — `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).EQ.4)`; `EFDC-GVC/calconcgvc.for:385` — `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).EQ.5)`; `EFDC-GVC/calconcgvc.for:265` — `IF(ISTRAN(1).EQ.1.AND.ISCDCA(1).LT.4)`)

---

## 5. 현행 EFDC+ (EFDCPlus_Stable) 대비

같은 위키 `raw/source_code/` 내 두 분기 직접 대조 (ls/find/grep):

<!-- count: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/**/*.f90 = 208 -->


| 축 | EFDC-GVC (레거시) | EFDCPlus_Stable (현행) |
|---|---|---|
| 언어/형식 | F77 fixed-form `.for` (293개) | **Fortran 90 `.f90` 전부 (208개)**, 모듈화 |
| 빌드 | Windows VS2010 + Intel `.vfproj`/`.sln` (이번 대조에서 확인하지 않음) | **CMake** (`CMakeLists.txt` 존재) — 크로스플랫폼 (이번 대조에서 확인하지 않음) |
| 전역상태 | `INCLUDE EFDC.PAR/EFDC.CMN` COMMON 블록 | F90 module (`mod_*.f90`, 예 `mod_netcdf.f90`) |
| 수직좌표 | 코드·문서 대조 | EFDC+는 aaefdc.f90에서 SGZ를 초기화한다. (`EFDCPlus_Stable/EFDC/aaefdc.f90:1310` — `if( IGRIDV > 0 )then`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1339` — `open(1,FILE = 'sgzlayer.inp',STATUS = 'UNKNOWN')`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2615` — `HPK(L,K) = HP(L)*DZC(L,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1443` — `if( IGRIDV == 1 ) DZC(L,K) = DZCK(K)/DZPC`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2398` — `SGZU(L,K)  = DZC(LW,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2400` — `SGZU(L,K)  = DZC(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 60쪽·인쇄 47쪽 — `face matching of layering is a fundamental difference with the GVC approach`) EFDC+의 물층 두께는 HP(L)*DZC(L,K)이다. (`EFDCPlus_Stable/EFDC/aaefdc.f90:2615` — `HPK(L,K) = HP(L)*DZC(L,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1443` — `if( IGRIDV == 1 ) DZC(L,K) = DZCK(K)/DZPC`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2398` — `SGZU(L,K)  = DZC(LW,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2400` — `SGZU(L,K)  = DZC(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 60쪽·인쇄 47쪽 — `face matching of layering is a fundamental difference with the GVC approach`) EFDC+는 셀별 층 비율과 면별 SGZ 계수를 사용한다. (`EFDCPlus_Stable/EFDC/aaefdc.f90:1310` — `if( IGRIDV > 0 )then`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1339` — `open(1,FILE = 'sgzlayer.inp',STATUS = 'UNKNOWN')`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2615` — `HPK(L,K) = HP(L)*DZC(L,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1443` — `if( IGRIDV == 1 ) DZC(L,K) = DZCK(K)/DZPC`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2398` — `SGZU(L,K)  = DZC(LW,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2400` — `SGZU(L,K)  = DZC(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 60쪽·인쇄 47쪽 — `face matching of layering is a fundamental difference with the GVC approach`) 이론서는 면별 층 정합을 GVC와의 근본적 차이로 설명한다. (`EFDCPlus_Stable/EFDC/aaefdc.f90:1310` — `if( IGRIDV > 0 )then`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1339` — `open(1,FILE = 'sgzlayer.inp',STATUS = 'UNKNOWN')`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2615` — `HPK(L,K) = HP(L)*DZC(L,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1443` — `if( IGRIDV == 1 ) DZC(L,K) = DZCK(K)/DZPC`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2398` — `SGZU(L,K)  = DZC(LW,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2400` — `SGZU(L,K)  = DZC(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 60쪽·인쇄 47쪽 — `face matching of layering is a fundamental difference with the GVC approach`) |
| 병렬 | 확인하지 않음 | MPI 도메인 분할 (`efdc_mpi_decomposition.md` 참조) (이번 대조에서 확인하지 않음) |
| 출력 | WASP 수문 링크 루틴은 존재한다. 활성 호출은 지정한 소스 검색에서 찾지 못했다. (`EFDC-GVC/wasphydrolinkgvc.for:1` — `SUBROUTINE WASPHYDROLINKgvc`) | netCDF (`mod_netcdf.f90`) 등 (netCDF 출력은 이번 대조에서 확인하지 않음) |
| 위치 | AAEFDC 헤더의 판본·날짜 (전체 수정 기간은 확인하지 않음) | DSI EFDC+ (라이선스 전문은 확인하지 않음) |

EFDC+ 파일 수는 `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/**/*.f90` 목록에서 셌다. 이 수는 컴파일 대상 수가 아니다.


핵심 결론:

1. EFDC-GVC는 EPA 배포 EFDC에 DSI가 EEMS 연동과 버그 수정을 적용한 분기이다. (`EFDC-GVC/README.md:4` — `EFDC-GVC code refers to the code that was developed and previously was provided by US Environmental Protection Agency (USEPA).`) EFDC+의 전면 재작성 여부와 상위 버전이라는 평가는 이번 대조에서 확인하지 않음. (`EFDC-GVC/README.md:4` — `EFDC-GVC code refers to the code that was developed and previously was provided by US Environmental Protection Agency (USEPA).`)
2. EFDC+는 aaefdc.f90에서 SGZ를 초기화한다. (`EFDCPlus_Stable/EFDC/aaefdc.f90:1310` — `if( IGRIDV > 0 )then`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1339` — `open(1,FILE = 'sgzlayer.inp',STATUS = 'UNKNOWN')`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2615` — `HPK(L,K) = HP(L)*DZC(L,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1443` — `if( IGRIDV == 1 ) DZC(L,K) = DZCK(K)/DZPC`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2398` — `SGZU(L,K)  = DZC(LW,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2400` — `SGZU(L,K)  = DZC(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 60쪽·인쇄 47쪽 — `face matching of layering is a fundamental difference with the GVC approach`) EFDC+의 물층 두께는 HP(L)*DZC(L,K)이다. (`EFDCPlus_Stable/EFDC/aaefdc.f90:2615` — `HPK(L,K) = HP(L)*DZC(L,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1443` — `if( IGRIDV == 1 ) DZC(L,K) = DZCK(K)/DZPC`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2398` — `SGZU(L,K)  = DZC(LW,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2400` — `SGZU(L,K)  = DZC(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 60쪽·인쇄 47쪽 — `face matching of layering is a fundamental difference with the GVC approach`) EFDC+는 셀별 층 비율과 면별 SGZ 계수를 사용한다. (`EFDCPlus_Stable/EFDC/aaefdc.f90:1310` — `if( IGRIDV > 0 )then`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1339` — `open(1,FILE = 'sgzlayer.inp',STATUS = 'UNKNOWN')`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2615` — `HPK(L,K) = HP(L)*DZC(L,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1443` — `if( IGRIDV == 1 ) DZC(L,K) = DZCK(K)/DZPC`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2398` — `SGZU(L,K)  = DZC(LW,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2400` — `SGZU(L,K)  = DZC(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 60쪽·인쇄 47쪽 — `face matching of layering is a fundamental difference with the GVC approach`) 이론서는 면별 층 정합을 GVC와의 근본적 차이로 설명한다. (`EFDCPlus_Stable/EFDC/aaefdc.f90:1310` — `if( IGRIDV > 0 )then`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1339` — `open(1,FILE = 'sgzlayer.inp',STATUS = 'UNKNOWN')`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2615` — `HPK(L,K) = HP(L)*DZC(L,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1443` — `if( IGRIDV == 1 ) DZC(L,K) = DZCK(K)/DZPC`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2398` — `SGZU(L,K)  = DZC(LW,K)`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2400` — `SGZU(L,K)  = DZC(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 60쪽·인쇄 47쪽 — `face matching of layering is a fundamental difference with the GVC approach`)

EFDC+의 표준 전체 수질 반응 모듈은 ISWQLVL=1의 WQSKE1이다. (`EFDCPlus_Stable/EFDC/Eutrophication/mod_wq.f90:335` — `if( ISWQLVL == 1 ) CALL WQSKE1 ! *** Extension of CEQUAL-ICM for unlimited algae + zooplankton`) EFDC+의 WQSKE3는 계산 제거 안내문 뒤에 반환한다. (`EFDCPlus_Stable/EFDC/Eutrophication/mod_wq.f90:5171` — `PRINT *,'WQSKE3 HAS BEEN REMOVED.  NEEDS CODE IF IWQSKE = 3 IMPLEMENTED'`) 같은 모듈 번호와 같은 파일 역할만으로 물리·수치 동등성을 판정할 수 없다. (`EFDCPlus_Stable/EFDC/Eutrophication/mod_wq.f90:335` — `if( ISWQLVL == 1 ) CALL WQSKE1 ! *** Extension of CEQUAL-ICM for unlimited algae + zooplankton`; `EFDCPlus_Stable/EFDC/Eutrophication/mod_wq.f90:5171` — `PRINT *,'WQSKE3 HAS BEEN REMOVED.  NEEDS CODE IF IWQSKE = 3 IMPLEMENTED'`; `EFDCPlus_Stable/EFDC/Eutrophication/mod_wq.f90:5173` — `return`)

3. DSI는 진행 중인 모델을 EFDC+로 전환하도록 권고한다. (`EFDC-GVC/README.md:4` — `DSI recommends that users not use the GVC code for on-going models and make the conversion to EFDC+.`)

---

## 6. 한계·미확인

- `EFDC-GVC/LICENSE` 별도 라이선스 전문 (35 KB) — 본 노트에서 GPL/기타 분류 미확인 (⚠ 미확인, 필요시 별도 read).
- 입력 읽기 방식과 면별 격자 처리 차이는 확인했다. (`EFDC-GVC/setgvc.for:151` — `READ(1,*)I,J,KLTMP`; `EFDC-GVC/setgvc.for:160` — `KGVCP(L)=KC-KLTMP+1`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1344` — `read(1,*,END = 1000) IIN, JIN, K`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1356` — `KSZ_Global(LG) = K`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2667` — `if( KSZ(LW) > KSZ(L) )then`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2675` — `SGZW(L,K)  = DZC(L,K) + DZCAD`) 전체 좌표식 유도와 GVC 입력 매뉴얼의 전체 형식은 확인하지 않음. (`EFDC-GVC/setgvc.for:151` — `READ(1,*)I,J,KLTMP`; `EFDC-GVC/setgvc.for:160` — `KGVCP(L)=KC-KLTMP+1`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1344` — `read(1,*,END = 1000) IIN, JIN, K`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1356` — `KSZ_Global(LG) = K`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2667` — `if( KSZ(LW) > KSZ(L) )then`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2675` — `SGZW(L,K)  = DZC(L,K) + DZCAD`)
- 입력 읽기 방식과 면별 격자 처리 차이는 확인했다. (`EFDC-GVC/setgvc.for:151` — `READ(1,*)I,J,KLTMP`; `EFDC-GVC/setgvc.for:160` — `KGVCP(L)=KC-KLTMP+1`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1344` — `read(1,*,END = 1000) IIN, JIN, K`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1356` — `KSZ_Global(LG) = K`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2667` — `if( KSZ(LW) > KSZ(L) )then`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2675` — `SGZW(L,K)  = DZC(L,K) + DZCAD`) 전체 좌표식 유도와 GVC 입력 매뉴얼의 전체 형식은 확인하지 않음. (`EFDC-GVC/setgvc.for:151` — `READ(1,*)I,J,KLTMP`; `EFDC-GVC/setgvc.for:160` — `KGVCP(L)=KC-KLTMP+1`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1344` — `read(1,*,END = 1000) IIN, JIN, K`; `EFDCPlus_Stable/EFDC/aaefdc.f90:1356` — `KSZ_Global(LG) = K`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2667` — `if( KSZ(LW) > KSZ(L) )then`; `EFDCPlus_Stable/EFDC/aaefdc.f90:2675` — `SGZW(L,K)  = DZC(L,K) + DZCAD`)

이번 recovery 대조는 진입 분기·직접 호출 순서·GVC 전용 처리·EFDC+ 대응 구현을 확인했다. 모델 실행·두 판본의 수치 오차·물리 타당성은 확인하지 않음. 포함 파일의 내부 선언·빌드 프로젝트·라이선스 전문·GVC 입력 매뉴얼의 전체 형식은 확인하지 않음.
