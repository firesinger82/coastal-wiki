---
title: "EFDC-GVC 레거시 분기 — Generalized Vertical Coordinate (Hamrick/EPA 계열) 구조 요약"
model: EFDC
component: source-analysis/legacy-branch
canonical_source: self
citation_status: verified
verification_method: "EFDC-GVC/ 트리 전체 ls/find/grep (342 file, 293 .for) + README.md·EFDC.CMN·EFDC.PAR·EFDC_GVC_2010.vfproj 직접 read. 핵심 파일 setgvc.for·caltrani.for·costranw.for·calwqcgvc.for·budget5.for·calexpgvc.for 헤더·본문 file:line 인용. aaefdc.for 디스패치(IGRIDV 분기) grep+read. EFDCPlus_Stable/ 와 확장자·CMake·SGZ 대조."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/EFDC/README.md
  - models/EFDC/source-analysis/efdc_vertical.md
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/source-analysis/efdc_transport_scheme.md
---

# EFDC-GVC 레거시 분기 — Generalized Vertical Coordinate (Hamrick/EPA 계열) 구조 요약

> EFDC-GVC 는 DSI 가 공개한 **EFDC 레거시 분기**로, USEPA 가 한때 배포하던 EFDC 소스코드를 기반으로 EEMS 연동·버그 수정을 입힌 것. FORTRAN77 계열 fixed-form(`.for`), `PROGRAM AAEFDC` 단일 진입점·`INCLUDE 'EFDC.PAR'/'EFDC.CMN'` 글로벌 공통블록 구조. 핵심 특징은 이름 그대로 **GVC(일반화 수직좌표)** 옵션 — 셀별로 활성 수직층 수와 스케일링을 달리해 표준 σ 격자의 한계를 보완. 현행 [[efdc]](EFDCPlus_Stable)(EFDC+) 와는 **구버전/계보** 관계이며, DSI 는 공식적으로 신규 모델에는 GVC 대신 EFDC+ 전환을 권장한다. (`README.md` 직접 인용, 아래 §1)

---

## 1. 분기 정체 — README 1차 출처

`EFDC-GVC/README.md` 원문 핵심 (verbatim 발췌):

> "DSI has made the Generalized Vertical Coordinate (GVC) version of EFDC code available. EFDC-GVC code refers to the code that was developed and previously was provided by US Environmental Protection Agency (USEPA). EPA stopped providing the source code for EFDC several years ago. DSI has modified the EFDC-GVC code to work with EEMS. The code has also been modified to correct bugs found. DSI provides this updated version ... for the modeling community that is looking to upgrade legacy modeling applications to DSI's EFDC+. ... DSI recommends that users not use the GVC code for on-going models and make the conversion to EFDC+."

요점 정리:

| 항목 | 내용 |
|---|---|
| 계보 | USEPA 배포 EFDC → DSI 가 EEMS 연동·버그픽스 |
| 의도 | 레거시 EFDC 적용모델의 **테스트용 오픈소스** 제공 + EFDC+ 전환 유도 |
| 권장 | 신규/진행중 모델에는 GVC 비권장, EFDC+ 전환 권고 |
| 지원 | "provided as-is without any support" (무지원) |

---

## 2. 코드 구조 — FORTRAN77 계열 모놀리식

### 2.1 빌드/파일 구성

- 트리 전체 **342 파일, 그중 293 개가 `.for`** fixed-form FORTRAN (ls 확장자 집계: `for 293`, `f 6`, `f90 2`, `CMN 1`, `PAR 1`).
- Visual Studio 솔루션 `EFDC_GVC_2010.sln` + Intel Fortran 프로젝트 `EFDC_GVC_2010.vfproj` (**293 `<File ` 엔트리**, grep 집계). 즉 Windows/Intel Fortran 2010 빌드 환경.
- 공통블록 헤더 2개:
  - `EFDC.PAR` (9.1 KB) — `PARAMETER` 차원 상수 (LCM, KCM, ICM, JCM 등 컴파일타임 배열 크기).
  - `EFDC.CMN` (72 KB) — 전역 `COMMON` 블록 (모든 상태배열·플래그). 모든 서브루틴이 `INCLUDE 'EFDC.PAR'`/`INCLUDE 'EFDC.CMN'` 로 공유 — 모듈/파생형 없는 전형적 F77 글로벌 상태 구조.

### 2.2 진입점·디스패치

- `aaefdc.for:14` `PROGRAM AAEFDC` — 마스터 프로그램. 헤더 `aaefdc.for:5` "FILE FOR EFDC-FULL VERSION 1.0a", `aaefdc.for:144` "LAST MODIFIED BY JOHN HAMRICK ON 1 NOVEMBER 2001".
- 거의 모든 서브루틴 헤더가 동일 banner: `C **  THIS SUBROUTINE IS PART OF EFDC-FULL VERSION 1.0a` + `C **  LAST MODIFIED BY JOHN HAMRICK ON 1 NOVEMBER 2001` (예: `setgvc.for:8,10`, `caltrani.for:8,10`, `costranw.for:8,10`, `calwqcgvc.for:8,10`, `budget5.for:11,12`). → **2001~2004 빈티지 Hamrick 코드베이스**.
- **수직격자 분기는 `IGRIDV` 플래그** (CMN 선언 `EFDC.CMN:1024`, 표준 σ=0 / GVC=1). `aaefdc.for` 디스패치:
  - `aaefdc.for:957` `IF(IGRIDV.EQ.1) CALL SETGVC` — GVC 초기화.
  - `aaefdc.for:2598-2599` `IF(IGRIDV.EQ.0) CALL HDMT` / `IF(IGRIDV.EQ.1) CALL HDMTGVC` — 수력동역학 메인루프 σ vs GVC 이원화.

---

## 3. GVC 메커닉 — 셀별 가변 수직층

GVC = 셀마다 (a) 활성 수직층 인덱스 범위와 (b) 층두께 스케일링을 달리해, 균일 σ 분할의 천수·급경사 표현 한계를 완화하는 좌표. 두 종류 셀:

> `setgvc.for:117-118` — "LCTV AND IJCTV EQUAL 1 FOR FOR RESCALED HEIGHT CELLS AND 2 FOR SIGMA CELLS" — 즉 **재척도화-높이(rescaled-height) 셀(=1)** 과 **순수 σ 셀(=2)** 혼용.

핵심 전역배열 (모두 `EFDC.CMN` 선언):

| 배열 | 선언 위치 | 역할 |
|---|---|---|
| `KGVCP/KGVCU/KGVCV/KGVCW(LCM)` | `EFDC.CMN:358-359` | 셀 L 의 P/U/V/W 점 **최하단 활성 수직층 인덱스** (그 아래 층은 비활성) |
| `GVCSCLP/GVCSCLU/GVCSCLV(LCM)` + 역수 `*I` | `EFDC.CMN:173` | P/U/V 점 **층두께 스케일 계수** (및 inverse) |
| `LCTV(L)` / `IJCTV(I,J)` | setgvc | 셀 수직타입 (1=rescaled, 2=sigma) |
| 제어 플래그 `IGRIDV, ISETGVC, ISGVCCK` | `EFDC.CMN:1024` | GVC on/off, 설정모드, 체크 |

### 3.1 `SETGVC` (`setgvc.for`) — GVC 초기화 리더

- `setgvc.for:6` `SUBROUTINE SETGVC`, 헤더 `setgvc.for:21-22` "READS INFORMATION FOR THE GENERALIZED VERTICAL COORDINATE OPTION AND SETS REAL AND LOCICAL MASK".
- 입력파일 2종: `setgvc.for:79` `OPEN(1,FILE='CELLGVC.INP',...)` (셀별 수직타입 맵 `IJCTV`), `setgvc.for:144` `OPEN(1,FILE='GVCLAYER.INP',...)` (셀별 활성층 수, `ISETGVC.EQ.0` 일 때).
- 기본 스케일·인덱스 초기화: `setgvc.for:56-67` (경계층 `GVCSCL*=1.0`), `setgvc.for:69-73` (`KGVCP/U/V(L)=1`).

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
    IF(K.LT.KGVCP(L)) SAL(L,K)=0.0      ! aaefdc.for:1870
    IF(K.LT.KGVCP(L)) SAL1(L,K)=0.0     ! aaefdc.for:1871
```

→ `KGVCP(L)` 미만(=비활성 하부층) 의 스칼라(염분 등)를 명시적으로 0 처리. GVC 의 "셀마다 활성층 수가 다름" 을 농도장에서 강제하는 부분.

### 3.4 GVC 전용 파일 인벤토리 (`*gvc.for`, 18개)

ls 집계 (전부 표준 비-GVC 루틴의 GVC 대응판):

| 파일 | 대응 표준 | 역할(헤더 기반) |
|---|---|---|
| `setgvc.for` | (신규) | GVC 초기화·입력 리더 |
| `hdmtgvc.for` | `hdmt.for` | GVC 수력동역학 메인루프 |
| `calexpgvc.for` | `calexp.for` | GVC explicit 모멘텀/플럭스 |
| `caltrangvc.for` | `caltran.for` | GVC 스칼라 advection-diffusion 수송 |
| `caluvwgvc.for` | `caluvw.for` | GVC 3D 유속(U,V,W) |
| `calpuv9gvc.for` | `calpuv*.for` | GVC 외부모드(표면 z, P-U-V) 해 |
| `calqq1gvc.for` | `calqq1.for` | GVC 난류 폐합 (q²) |
| `calconcgvc.for` | `calconc.for` | GVC 농도 디스패처 (→ `CALTRANGVC` 호출, `calconcgvc.for:266-326`) |
| `calheatgvc/calheatbgvc.for` | `calheat*.for` | GVC 열수지 |
| `calwqcgvc.for` | `calwqc.for` | GVC 수질 농도 (아래 §4) |
| `caltrwqgvc.for` | `caltrwq.for` | GVC 수질 수송 |
| `wqske3gvc.for` | `wqske*.for` | GVC 수질 동역학 (eutrophication kinetics) |
| `smmbegvc.for` | sediment 수지 | GVC 질량수지 |
| `calavbgvc.for` | `calavb.for` | GVC 수직 와점성/확산 |
| `calebigvc.for` | — | GVC EBI |
| `wasphydrolinkgvc.for` | `wasphydrolink.for` | GVC→WASP 수문 링크 |

> 패턴: GVC 분기는 **새 추상화가 아니라, 핵심 σ 루틴 각각의 `*gvc` 평행 복제본** 으로 구현. 코드 중복이 크고 (`hdmtgvc.for` 52 KB, `caltrangvc.for` 52 KB), `IGRIDV` 가 런타임에 둘 중 하나를 호출. → EFDC+ 가 후술 SGZ 로 통합하기 전의 과도기적 설계.

---

## 4. 배정 대표 파일 헤더·역할 (file:line)

| 파일 | 시그니처 | 헤더 설명(verbatim) | 인용 |
|---|---|---|---|
| `caltrani.for` | `SUBROUTINE CALTRANI (ISTL,M,CON,CON1)` (`:6`) | "CALCULATES THE ADVECTIVE AND DIFFUSIVE TRANSPORT OF DISSOLVED OR SUSPENDED CONSITITUENT M ... A NEW VALUE AT TIME LEVEL (N+1). ... THE SOLUTION IS IMPLICIT" | `caltrani.for:19-22` |
| `costranw.for` | `SUBROUTINE COSTRANW (ISTL,IS2TL,MVAR,M,CON,CON1)` (`:6`) | "COSTRAN CALCULATES THE ADVECTIVE TRANSPORT OF DISSOLVED OR SUSPENDED CONSITITUENT M ..." — `costranw.for:16-17` 변경기록 "added dynamic time stepping" (2002-03-05), `costranw.for:45` `IF(ISDYNSTP.EQ.0)` 동적 타임스텝 분기 | `costranw.for:20-23` |
| `calwqcgvc.for` | `SUBROUTINE CALWQCGVC (ISTL)` (`:6`) | "CALWQC CALCULATES THE CONCENTRATION OF DISSOLVED AND SUSPENDED WATER QUALITY CONSTITUTENTS AT TIME LEVEL (N+1). CALLED ONLY ON ODD THREE TIME LEVEL STEPS" — GVC 수질 농도 드라이버 | `calwqcgvc.for:19-21` |
| `budget5.for` | `SUBROUTINE BUDGET5` (`:6`) | "SUBROUTINES BUDGETN CALCULATE SEDIMENT BUDGET (TOTAL SEDIMENTS)" — `budget5.for:8` "ADDED BY DON KINGERY, CH2M-HILL ON 15 OCTOBER 1996". `NBUD.EQ.NTSMMT` 시 부유+저질 종료량 집계(`budget5.for:34,44-52`) | `budget5.for:23` |
| `setgvc.for` | `SUBROUTINE SETGVC` (`:6`) | §3.1 참조 — GVC 격자 초기화·`CELLGVC.INP`/`GVCLAYER.INP` 리더 | `setgvc.for:21-22` |

`caltrani` / `costranw` 는 σ-격자 표준 수송 루틴(GVC 접미사 없음) — `caltrani`(implicit advection-diffusion) vs `costranw`(explicit + 동적 타임스텝) 의 alternative 수송 스킴. GVC 활성 시 대응 `caltrangvc` 가 별도 사용된다.

---

## 5. 현행 EFDC+ (EFDCPlus_Stable) 대비

같은 위키 `raw/source_code/` 내 두 분기 직접 대조 (ls/find/grep):

| 축 | EFDC-GVC (레거시) | EFDCPlus_Stable (현행) |
|---|---|---|
| 언어/형식 | F77 fixed-form `.for` (293개) | **Fortran 90 `.f90` 전부 (206개)**, 모듈화 |
| 빌드 | Windows VS2010 + Intel `.vfproj`/`.sln` | **CMake** (`CMakeLists.txt` 존재) — 크로스플랫폼 |
| 전역상태 | `INCLUDE EFDC.PAR/EFDC.CMN` COMMON 블록 | F90 module (`mod_*.f90`, 예 `mod_netcdf.f90`) |
| 수직좌표 | GVC = σ 루틴 + `*gvc` 평행 복제 (`IGRIDV` 분기) | **SGZ (Sigma-Zed)** — GVC 후속, 통합 구현. `SGZ`/`KSZ` 토큰이 `caluvw.f90`·`hdmt.f90`·`aaefdc.f90` 등 코어에 직접 내장 (grep 확인) |
| 병렬 | (단일, MPI 미상) | MPI 도메인 분할 (`efdc_mpi_decomposition.md` 참조) |
| 출력 | 자체 바이너리/WASP 링크 | netCDF (`mod_netcdf.f90`) 등 |
| 위치 | EFDC-FULL v1.0a, Hamrick 2001 | DSI EFDC+ (GPL-3.0) |

핵심 결론:

1. **계보**: EFDC-GVC 는 Hamrick/EPA EFDC(2001 v1.0a) → DSI 가 떠받친 레거시 분기. EFDC+ 가 이를 F90/CMake/SGZ 로 전면 재작성한 **상위(현행) 버전**.
2. **GVC → SGZ**: 셀별 가변 수직층이라는 개념은 EFDC+ 의 **SGZ(Sigma-Zed)** 로 계승·통합. GVC 의 `*gvc` 복제 패턴이 SGZ 에서는 코어 루틴 내부 분기로 흡수됨.
3. **사용 권고**: DSI 공식 README — GVC 는 레거시 모델 테스트/마이그레이션 출발점일 뿐, 신규 작업은 EFDC+ 전환 (§1).

---

## 6. 한계·미확인

- `EFDC-GVC/LICENSE` 별도 라이선스 전문 (35 KB) — 본 노트에서 GPL/기타 분류 미확인 (⚠ 미확인, 필요시 별도 read).
- SGZ 와 GVC 의 수식적 정확한 차이(층 재배치 알고리즘)는 EFDC+ 측 코드/이론서 비교가 필요 — 본 노트는 **분기 구조·계보** 범위. SGZ 메커닉 상세는 `source-analysis/efdc_vertical.md` 범위.
- GVC 입력파일 `CELLGVC.INP`/`GVCLAYER.INP` 포맷 상세는 `setgvc.for` READ 문 외 메뉴얼 미대조 (source-needed for full format spec).
