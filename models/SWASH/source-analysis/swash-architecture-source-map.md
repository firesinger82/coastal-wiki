---
title: "SWASH 소스 아키텍처 맵 — main·compute dispatch·flow solver 명명규칙·SWAN 인프라 공유"
model: SWASH
component: src (top-level)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). Swash.ftn90(main 71줄)·SwashComputFlow.ftn90(compute dispatch) call 라인 + 각 flow solver Purpose 주석 verbatim 인용. Fortran 원문은 .ftn90 152개와 .ftn 8개를 합친 160개다(src/srclist.cmake:2–161). 명명규칙 해독은 SwashExp/ImpDep/Lay*.ftn90 Purpose 주석 직접 인용. SWAN 인프라 공유는 src/ 파일명(SwanGrid*·ocp*·swanparll) 직접 확인. 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
related:
  - models/SWASH/README.md
  - models/SWASH/web-refs/swash-official-resources.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
---

# SWASH 소스 아키텍처 맵

> `src/`에는 `.ftn90` 원본 152개와 `.ftn` 원본 8개가 있다 (`src/srclist.cmake:2–161`). [10-15 대조 정정]
> 원본 수의 합계는 160개다 (`src/srclist.cmake:2–161`). [10-15 대조 정정]

<!-- count: models/SWASH/raw/source_code/swash/src/*.ftn90 = 152 -->
<!-- count: models/SWASH/raw/source_code/swash/src/*.ftn = 8 -->

## 1. main program (`Swash.ftn90`, 71줄)

```
program Swash
  call SWINITMPI        ! MPI 초기화 (SWAN ocean pack 공유)
  call SwashMain        ! SWASH run 본체
  call SWEXITMPI        ! MPI 종료
end program
```

- 자칭: "SWASH (Simulating WAves till SHore); a **non-hydrostatic wave-flow model**" / Purpose: "Program for simulation of wave motion and shallow water flow in coastal waters".
- 저자 v1.00 **Marcel Zijlema, 2009-12** (TU Delft Environmental Fluid Mechanics).
- `SwashMain`은 초기화 단계에서 `SwashInit`을 호출한다 (`src/SwashMain.ftn90:126`). [10-15 전수 검증 정정]
- `SwashMain`은 명령 반복문에서 `SwashReadInput`을 호출한다 (`src/SwashMain.ftn90:135–140`). [10-15 전수 검증 정정]
- `SwashMain`은 구조 격자에서 `SwashComputStruc`를 호출한다 (`src/SwashMain.ftn90:241`). [10-15 대조 정정]
- `SwashComputStruc`는 `if ( .not.momskip ) call SwashComputFlow`로 유동 계산을 호출한다 (`src/SwashComputStruc.ftn90:125`). [10-15 대조 정정] [10-15 전수 검증 정정]
- 비구조 격자의 대응 루틴은 `SwashCompUnstruc`와 `SwashCompUFlow`다 (`src/SwashMain.ftn90:247`; `src/SwashCompUnstruc.ftn90:67`). [10-15 대조 정정]
- `SwashMain`의 출력 진입점은 `SwashOutput`이다 (`src/SwashMain.ftn90:263`). [10-15 대조 정정]
- INITIAL 명령은 입력을 읽는 중 `SwashInitCond`에서 처리한다 (`src/SwashReadInput.ftn90:2825–2826`). [10-15 대조 정정] [10-15 전수 검증 정정]
- INITIAL STEADY는 `instead`를 설정한다 (`src/SwashInitCond.ftn90:146`). [10-15 대조 정정]
- 구조 격자의 `SwashInitSteady`는 검사·준비의 마지막 부분에서 속도를 계산한다 (`src/SwashCheckPrep.ftn90:5974`). [10-15 대조 정정]

## 2. compute dispatch (`SwashComputFlow.ftn90`)

시간스텝마다 **격자차원 × 연직표현 × 시간적분 × 변형** 조합으로 flow solver 호출. 명명규칙 `Swash{Exp|Imp}{Dep|Lay}[P|M]{1DH|2DH|U}flow`:

| 토큰 | 의미 |
|---|---|
| **Exp / Imp** | 수위 기울기·수심 적분 연속방정식의 명시적·반암시적 적분을 구별한다 (`src/SwashComputFlow.ftn90:44–47`). [10-15 대조 정정] |
| **Dep / Lay** | **depth-averaged**(1층) / **layer-averaged**(다층 z) |
| **P** | 비정수압 압력 **subgrid 접근**(`SwashImpLayP*` "solved with a subgrid approach") |
| **M** | M 변형은 `mimetic` 선택자로 호출한다 (`src/SwashComputFlow.ftn90:93–96`). [10-15 대조 정정] |
| **1DH / 2DH / U** | 1D-수평 / 2D-수평 / 비구조 삼각 격자 (`src/SwashExpDepUflow.ftn90:44`). [10-15 대조 정정] |

`ihydro`는 비정수압 압력 분기를 별도로 선택한다 (`src/SwashReadInput.ftn90:1499–1513`). [10-15 대조 정정]
운동량 보존만으로 일반 경로와 구별하지 않는다 (`src/SwashImpDep1DHflow.ftn90:54–57`; `src/SwashImpDepM1DHflow.ftn90:42–44`; [theory-framework:ST1-341](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md)). [10-15 대조 정정] [10-15 전수 검증 보완]
M1DH 헤더는 이산 질량·운동량 보존을 명시한다. 같은 헤더는 공간에서 에너지를 엄밀히 보존한다고 명시한다. 시간 분할 때문에 시간 에너지는 엄밀 보존이 아니라 근사 보존이다 (`src/SwashImpDepM1DHflow.ftn90:42–47`). [10-15 대조 정정] [10-15 전수 검증 정정]

호출 예 (`SwashComputFlow.ftn90`):

| 라인 | solver | 조건 |
|---|---|---|
| `:86` | `SwashExpDep1DHflow` | 1DH explicit depth-avg |
| `:94` / `:96` | `SwashImpDep1DHflow` / `...M1DHflow` | 1DH 반암시적 (`mimetic` 선택). [10-15 대조 정정] |
| `:111` / `:113` | `SwashExpLay1DHflow` / `...P1DHflow` | 1DH explicit 다층 (P=압력 subgrid) |
| `:146` | `SwashExpDep2DHflow` | 2DH explicit depth-avg |
| `:154` / `:156` | `SwashImpDep2DHflow` / `...M2DHflow` | 2DH implicit |
| `:171-184` | `SwashExp/ImpLay[P]2DHflow` | 2DH 다층 |

각 solver Purpose 주석(verbatim): "Performs the time integration for the **non-hydrostatic, depth-averaged/layer-averaged 2D shallow water equations**" (`SwashExpDep2DHflow`/`SwashExpLay2DHflow`). `SwashImpLayP2DHflow` = "...layer-averaged 2D SWE solved with a **subgrid approach**".

→ Boussinesq(FUNWAVE) 가 고차 분산항으로 분산을 표현하는 데 비해, SWASH 는 **연직 층분할 + 비정수압 압력**(Poisson)으로 분산 표현. 층 수 ↑ → 깊은 물 분산 정확.

## 3. 최대 소스 (flow solver 계열, src 크기순)

| 파일 | 줄 | 역할 |
|---|---|---|
| `SwashExpLayP2DHflow.ftn90` | 9383 | 2DH explicit 다층+압력 |
| `SwashExpLay2DHflow.ftn90` | 7746 | 2DH explicit 다층 |
| `SwashImpLayP2DHflow.ftn90` | 7539 | 2DH implicit 다층+압력(subgrid) |
| `SwashImpLay2DHflow.ftn90` | 7003 | 2DH implicit 다층 |
| `SwashSolvers.ftn90` | 5705 | **선형 solver**(matrix-vector, 압력 Poisson) |
| `SwashCheckPrep.ftn90` | 6006 | 입력 검증·전처리 |
| `SwashBCtransferfnc.ftn90` | 4709 | **경계조건/조파**(boundary transfer) |
| `SwashReadInput.ftn90` | 2902 | 명령 입력 파서 |

## 4. SWAN 인프라 공유 (같은 TU Delft 그룹)

src/ 에 SWAN 파일이 그대로 존재 — SWASH 가 SWAN OCP(Ocean Pack) 재사용:

- `SwanGrid*.ftn90` (SwanGridTopology·GridCell·GridVert·Griddata·Gridobjects) — **unstructured grid topology**
- `SwanReadADCGrid.ftn90` — **ADCIRC fort.14 reader** (SWAN 과 동일, [SWAN 격자 입력](../../SWAN/source-analysis/swan-grid-readers.md)). [10-15 대조 정정]
- `ocpcre.ftn`·`ocpmix.ftn` — Ocean Pack I/O
- `swanparll.ftn`·`swanser.ftn`·`SWINITMPI` — MPI 병렬

→ SWAN(위상평균) ↔ SWASH(위상해상) 같은 코드베이스 계보. [`web-refs §3`](../web-refs/swash-official-resources.md).

## 5. 관련 노트

- [비정수압 압력 Poisson과 Keller-box](swash-nonhydrostatic-pressure-solver.md).
- [선형 solver](swash-linear-solvers.md).
- [조파 경계](swash-boundary-wave-forcing.md).
- [기술문서 구성](../manual-notes/swash-tech-documentation-overview.md).
- [사용자 설명서](../manual-notes/swash-user-manual.md).

## 문서와 코드 차이 (10-15 대조)

출처: [callflow](../../../_staging/recovery/flow/SWASH-callflow.md), [guide-syntax-build](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md), [theory-framework](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md), [theory-unstructured](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md).

쪽 규약: `PDF 쪽 = 인쇄 쪽 + 8`.

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech는 공개 저장소 `7949227` 2026-05-06 "release v12.01"에서 마지막 변경. 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f` 2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| callflow:RF-006 | 아키텍처 노트의 U 의미 | `source-analysis/swash-architecture-source-map.md:44` `U(연직 단면)` | `src/SwashCompUFlow.ftn90:40` `!   Computes water level and flow velocities by means of solving the shallow water equations on triangular mesh` | B 문서 오기 | U는 비구조 삼각 격자를 뜻한다. |
| callflow:RF-007 | Exp/Imp를 비정수압 압력의 적분 구별로 표기 | `source-analysis/swash-architecture-source-map.md:40` `시간적분 (비정수압 압력)`; `swashuse PDF p.99`는 수위 기울기와 전역 연속방정식의 속도 발산을 θ 방법으로 적분한다고 설명한다. | `src/SwashComputFlow.ftn90:46–47` `!   Alternatively, water level gradients and the depth-integrated continuity equation are`, `!   treated explicitly using the leap-frog technique`; `src/SwashReadInput.ftn90:1864–1865` `if ( KEYWIS('IMPL') ) then`, `mtimei = 2`; `src/SwashReadInput.ftn90:1499–1513`의 NONHYD 분기에서 `ihydro`에 대입한다. | B 문서 오기 | 아키텍처 노트의 괄호 설명이 잘못되었다. Exp/Imp는 수위 기울기·수심 적분 연속방정식의 명시적·반암시적 적분을 구별한다. 비정수압 활성은 별도 변수 ihydro로 구별한다. RF-003의 적용 배수 주장과도 구별한다. |
| callflow:RF-008 | 아키텍처 노트의 중간 드라이버 생략 | `source-analysis/swash-architecture-source-map.md:32`의 ``시간루프(`SwashComputFlow`)·출력(`SwashQuanOutp`)`` | `src/SwashMain.ftn90:241` `call SwashComputStruc`; `src/SwashMain.ftn90:247` `call SwashCompUnstruc`; `src/SwashMain.ftn90:263` `call SwashOutput` | C 문서 누락 | Main의 직접 계산 진입점은 ComputStruc·CompUnstruc다. 출력 진입점은 SwashOutput이다. |
| callflow:RF-009 | 아키텍처 노트의 소스 수 집계 대상 | `source-analysis/swash-architecture-source-map.md:18`의 `` `src/`(152 Fortran) `` | 실제 확장자 집계는 `.ftn90` 152개와 `.ftn` 8개다. `152 + 8 = 160`. | F 표기 차이 | 152는 ftn90 원본 수다. 고정 형식 ftn 원본 8개를 포함하면 합계 160개다. |
| callflow:RF-011 | 초기 조건 파싱과 STEADY 계산 위치 | `source-analysis/swash-architecture-source-map.md:32`의 초기화·입력 요약. `swashuse PDF p.55`는 STEADY의 Chezy 공식 사용을 설명한다. | `src/SwashReadInput.ftn90:2825–2826` `if ( KEYWIS ('INIT') ) then`, `call SwashInitCond`; `src/SwashInitCond.ftn90:141,146` `else if ( KEYWIS('STEA') ) then`, `instead = .true.`. `7949227`과 `a486d5f`의 `src/SwashCheckPrep.ftn90:5974`는 모두 `if ( optg /= 5 .and. instead ) call SwashInitSteady`다. `9554c98 2026-05-26 updated src`는 뒤의 `9554c98:src/SwashCheckPrep.ftn90:5979`를 `if ( lsubg ) then`에서 `if ( lsubg .and. ihydro /= 3 ) then`으로 바꿨다. | C 문서 누락 | INITIAL은 명령 읽기 중 처리한다. 구조 격자의 STEADY 속도 계산은 검사·준비의 끝에서 호출한다. HEAD는 그 뒤 ihydro=3의 압력 격자 속도 초기화를 건너뛴다. STEADY 호출 위치는 문서판 이후 바뀌지 않았다. C는 아키텍처 노트의 파싱·계산 위치 구별 누락이다. |
| guide-syntax-build:SG1-931 | models/SWASH/source-analysis/swash-architecture-source-map.md:7 | `source-analysis/swash-architecture-source-map.md:18`의 `` `src/`(152 Fortran) ``; `source-analysis/swash-architecture-source-map.md:7`의 `flow solver 152 Fortran` | SG1-823의 읽기 전용 파일 목록 대조: 원문 160개·srclist 160개. 읽기 전용 `rg --files models/SWASH/raw/source_code/swash/src -g '*.ftn' -g '*.ftn90'` 집계와 `src/srclist.cmake:2–161` 대조. [AD 판정](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)의 `git log --all` 92커밋 중 src가 존재하는 80개 트리를 `git show REV:src`로 대조했다. 전체 .ftn·.ftn90 수가 152인 트리는 없다. main의 91커밋과 --all의 집계 범위를 구분한다. `a486d5f:src/srclist.cmake:2–161`은 현재 목록과 같다. | B 문서 오기 | 현재 Fortran 원문은 .ftn90 152개와 .ftn 8개를 합친 160개다. `src/srclist.cmake:2–161`은 그 160개를 중복 없이 등록한다. 152는 현재 .ftn90만 센 값이다. SG1-823의 원문 인벤토리와 일치한다. |
| theory-framework:ST1-341 | M 이름과 실제 선택자 | `source-analysis/swash-architecture-source-map.md:43` `운동량보존(momentum-conservative) 변형` | `src/SwashComputFlow.ftn90:93` `if ( .not.mimetic ) then`; `src/SwashComputFlow.ftn90:96` `call SwashImpDepM1DHflow ( u1(1,1), u0(1,1), qx(1,1), qm(1,1), q(1,1), dq(1,1), gmatu(1,1,1), rho(1,1), ui(1,1), dqgrd(1,1), ibl(1), ibr(1), kgrpnt(1,1) )`; `src/SwashReadInput.ftn90:2010–2011`의 `MIME`는 `mimetic = .true.`를 설정한다. 인용 호출은 `src/SwashComputFlow.ftn90:74,78,89`의 1D·1층·반암시적 조건 아래에 있다. | C 문서 누락 (현재 노트) | M 변형은 `mimetic` 선택자로 호출한다. 공간 질량·운동량·에너지 보존의 조건과 시간 분할 한계를 함께 적는다. 운동량 보존만으로 일반 경로와 구별하지 않는다. 선택 조건은 ST1-280·281과 같고 시간 분할 한계는 ST1-323과 같다. |
| theory-framework:ST1-342 | U 이름의 격자 뜻 | `source-analysis/swash-architecture-source-map.md:44` `U(연직 단면)` | `src/SwashExpDepUflow.ftn90:44` `!   Performs the time integration for the non-hydrostatic, depth-averaged shallow water equations on triangular mesh` | B 문서 오기 (현재 노트) | U는 비구조 삼각 격자 경로를 뜻한다. 1DH·2DH와 별도 격자 분류이다. 연직 단면이라는 뜻으로 쓰지 않는다. |
| theory-unstructured:ST2-226 | 제12장 병렬 구현 본문 | swashtech PDF p.117: `This chapter is under preparation.`; swashuse PDF p.144: `A parallel version of SWASH with the distributed memory parallelization paradigm using MPI standard has been developed.`; README.md:245 `in the current version (v 12.01), the use of unstructured mesh is not supported in parallel mode.` | `src/swanparll.ftn:146` `!MPI      CALL MPI_INIT ( IERR )`; `src/swanparll.ftn:163` `!MPI      CALL MPI_COMM_RANK ( MPI_COMM_WORLD, INODE, IERR )`; `src/swanparll.ftn:179` `!MPI      CALL MPI_COMM_SIZE ( MPI_COMM_WORLD, NPROC, IERR )`; `src/swanparll.ftn:179` `!MPI      CALL MPI_COMM_SIZE ( MPI_COMM_WORLD, NPROC, IERR )`; `switch.pl:58`의 MPI 접두어 처리 | C 문서 누락 | 해석: C는 준비 중인 swashtech 제12장 p.117의 병렬 구현 본문 누락에 한정한다. swashuse p.144는 영역 분할과 MPI 통신을 설명한다. 인용한 초기화·순위·프로세스 수 호출은 MPI 스위치에서만 활성화된다. README는 12.01의 비구조 격자 병렬 모드를 지원하지 않는다고 명시한다. MPI 인프라의 존재와 비구조 병렬 지원을 구분한다. |
| theory-unstructured:ST2-420 | rank 번호·병렬 판정·종료 | swashuse PDF p.143–144와 원자료 README.md:237–243은 MPI 실행을 설명한다. swashtech PDF p.117에는 초기화·종료 본문이 없다. | `src/swanparll.ftn:158–164` `      INODE = 0`, `      NPROC = 1`, 빈 줄, `!MPI!     --- get node number INODE`, `!MPI`, `!MPI      CALL MPI_COMM_RANK ( MPI_COMM_WORLD, INODE, IERR )`, `      INODE = INODE + 1`; `src/swanparll.ftn:194–198` `      IF ( NPROC.GT.1 ) THEN`, `         PARLL = .TRUE.`, `      ELSE`, `         PARLL = .FALSE.`, `      END IF`; `src/swanparll.ftn:316` `!MPI            CALL MPI_ABORT ( MPI_COMM_WORLD, LEVERR, IERR )`; `src/swanparll.ftn:322` `!MPI            CALL MPI_FINALIZE ( IERR )` | C 문서 누락 | 내부 노드 번호는 MPI rank에 1을 더한 값이다. MPI 빌드도 한 프로세스이면 `PARLL`은 거짓이다. MPI가 초기화된 상태에서 `LEVERR.GE.4`이면 MPI_ABORT를 호출한다. 같은 상태에서 이 조건이 거짓이면 MPI_FINALIZE를 호출한다. (`src/swanparll.ftn:307–326`) MPI 호출은 모두 MPI 스위치에서만 활성화된다. C는 내부 노드 번호·PARLL 판정과 오류/정상 종료 분기에 한정한다. [10-15 전수 검증 정정] |
| theory-unstructured:ST2-423 | 층별 halo 교환 | swashuse PDF p.144는 MPI 통신을 설명한다. swashtech PDF p.117 및 사용설명서의 해당 설명에는 아래 층별 버퍼 구성·비차단 교환식이 없다. | `src/swanparll.ftn:3713` `      IF (.NOT.PARLL) RETURN`; `src/swanparll.ftn:3722` `      DO K = KS, KE`; `src/swanparll.ftn:3736–3737` `!MPI            CALL MPI_IRECV ( RBUF(1,INB), NOVLU, SWREAL, IDOM-1, ITAG,`<br>`!MPI     &                       MPI_COMM_WORLD, RRQST(INB), IERR )`; `src/swanparll.ftn:3753` `               SBUF(J,INB) = FIELD(KGRPNT(IBLKAD(ISTART+J)),K)`; `src/swanparll.ftn:3758–3759` `!MPI            CALL MPI_ISEND ( SBUF(1,INB), NOVLU, SWREAL, IDOM-1, ITAG,`<br>`!MPI     &                       MPI_COMM_WORLD, SRQST(INB), IERR )` | C 문서 누락 | 래퍼는 요청한 층 구간을 반복한다. 코드는 이웃 자료를 버퍼에 모아 비차단 송수신을 시작한다. MPI 목적지에는 내부 노드 번호에서 1을 뺀 값을 사용한다. 두 MPI 문장은 MPI 스위치에서만 활성화된다. |
