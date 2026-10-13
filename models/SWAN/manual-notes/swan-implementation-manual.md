---
title: "SWAN Implementation Manual (swanimp v41.51) — source file map + build (GNU make/CMake) + switch.pl + MPI/Metis/netCDF + swaninit + run/test verbatim"
topic: swan
canonical_source: external
external_source: "swanimp (SWAN Implementation Manual, Cycle III version 41.51, SWAN team 2026-03-13). Chapters 1 Introduction(material) / 2 Patch files / 3 Installation(classic GNU make + switch.pl + MPI/Metis/netCDF + CMake) / 4 swaninit / 5 Run / 6 Testing. 공식: http://www.swan.tudelft.nl + GitLab https://gitlab.tudelft.nl/citg/wavemodels/swan."
citation_status: verified
verification_method: "models/SWAN/raw/manuals/website_markdown/online_doc/swanimp/ node1-21.md 전 노드 직접 read. 빌드 명령·switch.pl 옵션·macros.inc 변수·swaninit 필드·swanrun 구문 verbatim. swantech doc-stack §4 TOC와 cross-check. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — build/switch/run 명령 verbatim, source file list ↔ source-analysis cross-walk"
verification_date: 2026-06-03
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/manual-notes/swan-programming-rules.md
  - models/SWAN/source-analysis/swan-foundation.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-parallel-implementation.md
---

# SWAN Implementation Manual (swanimp v41.51) — verified

> swanimp (Implementation Manual, Cycle III 41.51) node1-21 직접 read. **설치·빌드·실행·테스트**의 객관 레이어. swanuse(input 명세)·swantech(이론)와 별개로 "SWAN을 컴퓨터에 올리고 돌리는 절차"를 다룸. source-analysis 의 파일 인벤토리([swan-source-coverage-audit](../source-analysis/swan-source-coverage-audit.md))와 build switch 의 1차 출처.

노트의 문서 기준판은 41.51이다. 코드 검증 기준은 43e9bbb의 41.51AB이다. (`src/swanmain.ftn:965` `VERNUM = 41.51`; `src/swanmain.ftn:967` `CALL BUGFIX ('A')`; `src/swanmain.ftn:968` `CALL BUGFIX ('B')`; R7:N-001, patch A `c6d3136` 2026-03-13, patch B `0dabfa4` 2026-07-13.)

## 1. Implementation 5단계 (node1 verbatim)

> "Implementation involves the following steps: 1. Copying the source code … 2. If necessary, applying patches … 3. Making a few adaptions in installation-dependent parts of the code. 4. Compiling and linking … 5. Testing of the built SWAN."

→ steps 3·4 는 `switch.pl` + `make` 로 **완전 자동화 가능** (node1). 배포물: source code, **pre-built Windows release**, User/Implementation/Technical/Programming 4 docs, utilities, test cases. GitLab 호스팅 **since 41.41** ([swan-documentation-stack](swan-documentation-stack.md) §1과 일치).

## 2. The material — source file 인벤토리 (node2) ★

tarball `swan4151.tar.gz`. **본 표는 [swan-source-coverage-audit](../source-analysis/swan-source-coverage-audit.md) / [swan-foundation](../source-analysis/swan-foundation.md) 의 1차 출처** (어떤 .ftn/.ftn90 이 무슨 역할인지 공식 분류):

| 역할 | 파일 |
|---|---|
| main program | `swanmain.ftn` |
| pre-processing | `swanpre1.ftn` `swanpre2.ftn` `SwanBndStruc.ftn90` |
| computational | `swancom1.ftn` … `swancom5.ftn` |
| post-processing | `swanout1.ftn` `swanout2.ftn` `SwanVTKWriteHeader/Data/PDataSets.ftn90` |
| service | `swanser.ftn` `SwanIntgratSpc.ftn90` |
| Bragg scattering | `SwanBraggScat.ftn90` |
| QCM | `SwanQCM.ftn90` |
| ST6 package | `SdsBabanin.ftn90` |
| parallel MPI | `swanparll.ftn` |
| unstructured grids (routines) | `SwanReadGrid/ReadADCGrid/ReadTriangleGrid/ReadEasymeshGrid`, `SwanInitCompGrid`, `SwanCheckGrid`, `SwanCreateEdges`, `SwanGridTopology/Vert/Cell/Face`, `SwanPrintGridInfo`, `SwanFindPoint`, `SwanPointinMesh`, `SwanBpntlist`, `SwanPrepComp`, `SwanVertlist`, `SwanCompUnstruc`, `SwanDispParm`, `SwanPropvelX/S`, `SwanSweepSel`, `SwanTranspAc/X`, `SwanGradDepthorK`, `SwanGradVel`, `SwanDiffPar`, `SwanGSECorr`, `SwanInterpolatePoint/Ac/Output`, `SwanConvAccur`, `SwanConvStopc`, `SwanFindObstacles`, `SwanCrossObstacle`, `SwanComputeForce` (.ftn90) |
| parallel + unstructured | `SwanParallel.ftn90` |
| netCDF | `nctablemd.ftn90` `agioncmd.ftn90` `swn_outnc.ftn90` |
| 매뉴얼 tarball의 couplers (현재 Git 배포에 없음) | `couple2adcirc.ftn90` `swan2coh.ftn90` |
| installation | `ocpids.ftn` |
| command reading | `ocpcre.ftn` |
| miscellaneous | `ocpmix.ftn` |
| general modules | `swmod1.ftn` `swmod2.ftn` |
| XNL modules | `m_constants.ftn90` `m_fileio.ftn90` `serv_xnl4v5.ftn90` `mod_xnl4v5.ftn90` |
| unstructured modules | `SwanGriddata.ftn90` `SwanGridobjects.ftn90` `SwanCompdata.ftn90` |
| spectral partitioning | `SwanSpectPart.ftn` |
| FFT | `fftpack51.ftn90` |

SwanThreadBounds는 41.51 공개 코드에 있던 파일이다. patch B는 이 파일을 삭제했다. (`7ee8981:src/SwanThreadBounds.ftn90:1` `subroutine SwanThreadBounds ( nwetp, ivlow, ivup, tlist, n )`; `0dabfa4` 2026-07-13의 삭제 원문 `deleted file mode 100644`.)

현재 Git 배포의 파일 목록에서 couple2adcirc.ftn90과 swan2coh.ftn90을 제외한다. 매뉴얼의 목록을 인용할 때에는 두 파일이 조사한 Git 배포에 없다고 명시한다. (swanimp PDF 8–10쪽 / 인쇄 2–4쪽; R7:I-058·N-035.)

- **확장자 규칙**: fixed form = `for`/`f`, free form = `f90`. 원본은 `ftn`/`ftn90` → `switch.pl`이 OS별로 변환.
- `fftpack51` = John Burkardt (FSU) 가 Fortran 90 으로 번역한 FFT 라이브러리.
- 수정 후 공식 반영 원하면 SWAN team (m.zijlema@tudelft.nl) 에 제출. DUT 는 modified version 미지원.
- classic tarball 부속 파일 (swanimp PDF 11쪽 / 인쇄 5쪽): `INSTALL.README`, `Makefile`, `macros.inc`, `which.cmd`, `platform.pl`, `switch.pl`, `SWANRUN.README`, `swanrun`/`swanrun.bat`, `machinefile`, `swanhcat.ftn`+`hcat.nml`(hotfile 병합), `swan.edt`(edit file), `plotunswan.m`/`plotgrid.m`(unstructured Matlab).

INSTALL.README·macros.inc·which.cmd·platform.pl은 classic tarball 목록으로 한정한다. 41.51 공개 시점의 Git 배포도 CMake를 사용했다. 현재 Git Makefile은 뒤에 추가한 CMake 래퍼이다. (`7ee8981:README.md:74` `$ cmake .. -G Ninja`; `Makefile:44` `cd build && cmake $(CURDIR) $(CMAKE_FLAGS)`; R7:N-003.)

## 3. Patch files (node3)

릴리스 사이 bug fix/feature 는 patchfile 로 배포. 명명: `41.51.A` → `B` → `C`… 적용 후 출력 버전이 `41.51ABC` 로 갱신.

현행 코드가 선언하는 패치는 AB이다. (`src/swanmain.ftn:967` `CALL BUGFIX ('A')`; `src/swanmain.ftn:968` `CALL BUGFIX ('B')`; R7:N-004.)
```
patch -p0 < patchfile
```
→ 적용 후 **재컴파일** 필요. 브라우저 cut&paste 금지(tab 손실). Linux: CR 제거 `dos2unix` 또는 `cat 41.51.[A-C] | tr -d '\r' | patch`. Windows 는 SWAN 사이트의 patch 프로그램 사용.

## 4. Classic build — GNU make (node6-8)

빌드 전 **Perl ≥ 5.0.0** 필요(`platform.pl`/`switch.pl`). 3 run mode: serial / shared(OpenMP) / distributed(MPI).

macros.inc를 만드는 make config와 make ser·make omp·make mpi는 classic 절차이다. 현재 Git make config는 build를 다시 만드는 래퍼이다. 이 배포 범위 구분은 41.51 공개 코드에도 필요했다. (swanimp PDF 16–18쪽 / 인쇄 10–12쪽; `Makefile:42` `config: clobber`; `Makefile:43` `mkdir build`; `7ee8981:README.md:74` `$ cmake .. -G Ninja`; R7:N-005.)

```
make config        # macros.inc 생성 (1회, 필수 선행)
make ser           # serial
make omp           # parallel, shared (OpenMP)
make mpi           # parallel, distributed (MPI)
make clean         # object/module 정리
make clobber       # 이전 컴파일 잔여 파일 삭제
```
- classic 설치 안내의 Windows: Nmake(Visual Studio) 필요. OpenMP 는 Intel® Fortran 필요. MPI 는 Intel® MPI library.

Windows OpenMP의 Intel 한정은 classic 설치 안내로 구분한다. 41.51 공개 시점의 Git CMake도 GNU Windows 설정과 OpenMP Fortran 탐색을 포함했다. (`7ee8981:src/CMakeLists.txt:40` `if( WIN32 AND ${CMAKE_Fortran_COMPILER_VERSION} VERSION_GREATER_EQUAL 7 )`; `7ee8981:src/CMakeLists.txt:67` `find_package( OpenMP REQUIRED COMPONENTS Fortran )`; R7:N-006.)
- `make ser/omp/mpi` 중 **하나를 반드시 `make config` 1회로 선행**.

### 4.1 OpenMP vs MPI (node5, node7)
- **OpenMP**: 컴파일러 directive, shared-memory(laptop multi-core). 적은 thread 수에서 좋은 성능.
- **MPI**: 독립 프로세서 + interconnect(Linux cluster). MPICH/OpenMPI. **큰 시뮬레이션에서만** 유리(통신시간 ≪ 계산시간). [swan-parallel-implementation](../source-analysis/swan-parallel-implementation.md) 의 빌드 측 대응.
- F2003 stream I/O + F2008 OS command line 두 statement 사용(41.41+) — gfortran·Intel® Fortran 지원.

## 5. switch.pl — 소스 전처리 스위치 (node10) ★

```
perl switch.pl [-dos] [-unix] [-f95] [-jac] [-mpi] [-metis] [-cray] [-sgi]
               [-cvis] [-timg] [-matl4] [-impi] [-adcirc] [-netcdf] *.ftn
```
문서의 열 설명은 식별 접두부의 위치에 관한 느슨한 표기이다. 구현은 행 첫머리에서 !METIS 등 해당 표식 전체를 제거한다. (swanimp PDF 18쪽 / 인쇄 12쪽: `first 3 or 4 columns`; `switch.pl:101` `if ($met=~/TRUE/) {$newline=~s/^!METIS//;}`; R7:N-007.) [10-13 전수 검증 정정]

| 옵션 | 효과 |
|---|---|
| `-dos`/`-unix` | `!DOS`/`!UNIX` 제거 (OCPINI in ocpids.ftn, TXPBLA in swanser.ftn). `-unix`는 ftn→f, ftn90→f90 자동 변환. 41.51 공개 코드도 TABC를 CHAR(9)로 설정한다. (`src/ocpids.ftn:193` `TABC = CHAR(9)`; R7:I-015.) |
| `-f95` | CPU_TIME 행의 전처리 활성화에는 -timg와 -f95가 모두 필요하다. (`src/swanser.ftn:5852` `!TIMG!F95      CALL CPU_TIME (TIMER)`; swanimp PDF 19–20쪽 / 인쇄 13–14쪽; R7:N-008.) |
| `-jac` | **block Jacobi** (`!JAC` 제거, `!WFR` 유지). swanimp 원문은 `this option must be followed by the next option -mpi`이다. 현행 switch.pl은 두 옵션의 순서를 강제하지 않는다. (swanimp PDF 19쪽 / 인쇄 13쪽; `switch.pl:23` `if ($ARGV[0]=~/-jac/) {$jac="TRUE";shift;}`; `switch.pl:25` `if ($ARGV[0]=~/-mpi/) {$mpi="TRUE";shift;}`; R7:N-009.) |
| (기본) | **block wavefront**(`!WFR` 자동 제거) — 수렴특성 보존 |
| `-mpi` | `!MPI` 제거 (swanparll.ftn, swancom1.ftn, swmod1.ftn) |
| `-metis` | `!METIS` 제거 (unstructured mesh partition) |
| `-cray`/`-sgi` | `!/Cray`/`!/SGI` — 256자 초과 line RECL OPEN (OCPINI, FOR in ocpmix.ftn) |
| `-cvis` | `!CVIS` — Compaq Visual Fortran MPI 의 SHARED OPEN(Windows 다중 executable 파일열기 문제) |
| `-timg` | `!TIMG` — wall-clock/CPU timing 을 PRINT 파일에 출력 |
| `-matl4` | `!MatL4` — Level 4 MAT-File(IBM Power6 등 1-byte record 미지원). 기본은 `!MatL5`(Level 5, MATLAB 5+) |
| `-impi` | `!/impi` — `USE MPI` 미지원 컴파일러용 module MPI(swmod1.ftn) |
| `-adcirc` | `!ADC` 제거(coupled ADCIRC+SWAN). standalone 은 `!NADC` 제거 |
| `-netcdf` | `!NCF` 제거 |

예: Linux cluster + Intel® + MPI:
```
perl switch.pl -unix -f95 -mpi *.ftn *.ftn90
```
> **block Jacobi vs block wavefront** (node10 verbatim): Jacobi = subdomain interface 를 explicit 처리(높은 병렬성, 수렴특성 저하 가능). wavefront = 순차 알고리즘 연산순서 보존(수렴특성 유지, serial start-up/shut-down 으로 병렬효율 다소 저하). → 비/준정상엔 Jacobi, 그 외엔 wavefront 권장. ([swan-parallel-implementation](../source-analysis/swan-parallel-implementation.md) / [swan-tech-ch7-parallel](swan-tech-ch7-parallel.md) §7.2 와 정합)

## 6. 수동 컴파일·링크 (node11)

- F90 컴파일러 필수(F77 불가). MPI 시 `mpif90`(Intel® 은 `mpiifx`).
- ANSI F90 준수, **예외: 19 continuation line 한계 위반**(현존 컴파일러 문제없음).
- INTEGER/REAL/LOGICAL 에 동일 byte 할당 확인(보통 4 byte; 슈퍼컴은 8 — REAL 8 + INTEGER 4 면 오작동).
- binary MATLAB(unformatted) record length 1-byte 옵션: Intel® `/assume:byterecl`(Win) 또는 `-assume byterecl`(Linux).
- **module 선컴파일 목록** (node11, SwanSpectPart 확장자 정정): `swmod1.f, swmod2.f` → `SwanSpectPart.f` → `m_constants/m_fileio/serv_xnl4v5/mod_xnl4v5.f90` → `SwanGriddata/Gridobjects/Compdata.f90` → `SwanParallel.f90` → `SdsBabanin.f90` → `SwanIEM.f90` → `SwanBraggScat.f90` → `SwanQCM.f90`.

원본은 SwanSpectPart.ftn이다. UNIX 전처리 결과는 SwanSpectPart.f이다. 문서의 SwanSpectPart.f90은 확장자 오기이다. (swanimp PDF 21쪽 / 인쇄 15쪽: `SwanSpectPart.f90`; `src/srclist.cmake:4` `${SRC}/SwanSpectPart.${EXTF}`; `switch.pl:63` `$ext = ($file =~ m/ftn90/) ? "f90" : "f";`; R7:N-011.)
```
mpif90 <modules> ocp*.f swan*.f Swan*.f90 -o swan.exe
```
링크는 옵션/공유라이브러리(math, NAG) 없이. executable 은 `swan.exe` 로 rename 권장.

## 7. MPI / Metis / netCDF (node12-14)

- **MPI** (node12): Linux 는 설치 전제. Windows 는 Intel® MPI(oneAPI HPC Toolkit). `macros.inc` 에서 `INCS_MPI`/`LIBS_MPI` 비우고 `F90_MPI` 의 `ifx`→`mpiifx` 후 `make mpi`.
- **Metis** (node13): SWAN **41.45A+**. unstructured mesh 분할(distributed-memory). **multilevel k-way method**. MPI 필요. metis.h 의 `IDXTYPEWIDTH`·`REALTYPEWIDTH`=32, GKlib 필요, **Metis 5.2.1** 테스트됨. `macros.inc` 에 `METISROOT` 정의 후 `make mpi`.
- **netCDF** (node14): SWAN **40.91A+**. spectra·map 의 netCDF 출력. netCDF **4.5.x+** + Fortran interface enable. `macros.inc` 에 `NETCDFROOT` 정의.

## 8. CMake build (node15-18) — since 41.41 ★ 신규

Git 배포의 CMake 최소 버전은 2026-01-30에 3.12에서 3.20으로 바뀌었다. (`acb58b3:CMakeLists.txt:6` `cmake_minimum_required( VERSION 3.20 )`; swanimp PDF 24쪽 / 인쇄 18쪽: `CMake 3.12+`; R7:N-012.)

cross-platform. **현재 Git 코드의 최소 버전은 CMake 3.20**. generator 로 **Ninja**(GNU make 와 유사, 더 빠름) 권장.

```
git clone https://gitlab.tudelft.nl/citg/wavemodels/swan.git && cd swan
mkdir build && cd build         # out-of-source build (오브젝트·실행 파일은 build 아래)
cmake .. -G Ninja               # ./swan/CMakeLists.txt + ./swan/src/CMakeLists.txt
cmake --build .
cmake --install .               # UNIX 기본 $HOME/wavemodels/swan; Windows 기본 %LOCALAPPDATA%/Programs/wavemodels/swan
cmake --install . --prefix /your/dir
```
설치 후 `/bin`(executable) `/lib` `/mod` `/doc`(pdf) `/tools` `/misc`(machinefile, swan.edt) 생성.

전처리한 Fortran 파일은 src에 생성한다. (`src/CMakeLists.txt:35–36` `execute_process( COMMAND ${PERL_EXECUTABLE} ${CMAKE_SOURCE_DIR}/switch.pl ${SWITCHES} ${SRC}/*.ftn ${SRC}/*.ftn90 )`; R7:N-013.)

기본 설치 경로는 2026-01-30에 사용자 폴더로 바뀌었다. UNIX 기본값은 $HOME/wavemodels/swan이다. Windows 기본값은 %LOCALAPPDATA%/Programs/wavemodels/swan이다. (`acb58b3:CMakeLists.txt:13` `set( CMAKE_INSTALL_PREFIX "$ENV{HOME}/wavemodels/swan" CACHE STRING "" )`; `acb58b3:CMakeLists.txt:10` `cmake_path( SET LOCALSWAN $ENV{LOCALAPPDATA}/Programs/wavemodels/swan )`; R7:N-014.)

### 8.1 `-D` 옵션 (node17)
| option | default |
|---|---|
| `CMAKE_INSTALL_PREFIX` | UNIX `$HOME/wavemodels/swan`; Windows `%LOCALAPPDATA%/Programs/wavemodels/swan` |
| `CMAKE_PREFIX_PATH` | empty |
| `CMAKE_Fortran_COMPILER` | CMake 결정 |
| `MPI` / `OPENMP` / `METIS` / `NETCDF` | **OFF** |
| `JAC` / `FFRO` | **OFF** (`CMakeLists.txt:42–47` `option( JAC "" OFF )`, `option( FFRO "" OFF )`; R7:N-015) |
| `CMAKE_VERBOSE_MAKEFILE` | OFF |

예: `cmake .. -GNinja -DNETCDF=ON -DMPI=ON`. netCDF/Metis custom 경로는 `export NetCDF_ROOT=…`/`Metis_ROOT=…` 또는 `-DCMAKE_PREFIX_PATH=…`(세미콜론 구분). clean: `cmake -P clobber.cmake` (node18).

JAC를 선택하면 MPI를 켠다. OPENMP와 MPI를 함께 선택하면 CMake가 중단한다. (`src/CMakeLists.txt:18` `set( MPI ON )`; `src/CMakeLists.txt:72` `if( OPENMP AND MPI )`; `src/CMakeLists.txt:71–75` `message( FATAL_ERROR "-- Cannot use both OpenMP and MPI" )`; R7:N-015.) [10-13 전수 검증 정정]

## 9. swaninit — 사용자 초기화 파일 (node19) ★

첫 실행 시 생성. 해당 디렉토리 run 에만 적용. **현행 version = 4**. 필드:

| 필드 | 기본/의미 |
|---|---|
| version | **4** (유효성 검증) |
| institute | `Delft University of Technology` (변경 가능) |
| command file ref/name | 3 / `INPUT` |
| print file ref/name | 4 / `PRINT` |
| test file ref/name | 4 / (= print) |
| screen ref | 6 (abnormal end 시 진단용) |
| highest file ref | 99999 |
| comment id | `$` (VAX 등 충돌 시 `!`) |
| TAB char | [TAB] 키 |
| dir sep char | `\` → `/` (OS별 치환) |
| time coding option | **1** (default) |
| processor speed ×N | 100 (heterogeneous machine 부하분배) |

- **time coding option** (node19 verbatim): 1 `19870530.153000`(ISO, 권장·millennium 문제없음) / 2 `30-May-87 15:30:00` / 3 `05/30/87 15:30:00` / 4 `15:30:00` / 5 `87/05/30 15:30:00` / 6 `8705301530`(WAM). (`../raw/manuals/website/online_doc/swanimp/node19.html:115–125`.) [10-13 전수 검증 정정]

노트의 1911–2010 범위는 swanimp 원문에도 있는 오기이다. 41.51 공개 코드도 형식 2·3·5·6의 두 자리 연도를 1930–2029로 해석한다. 형식 4는 날짜 성분을 0으로 둔다. (swanimp PDF 28쪽 / 인쇄 22쪽; `src/ocpids.ftn:494` `INTEGER :: JUMPYEAR = 30     ! Used in interpretation of 2-digit year code`; `43e9bbb:src/ocpids.ftn:506` `        IF (DTTIME(1).LT.JUMPYEAR) THEN                                   40.89 30.70`; `43e9bbb:src/ocpids.ftn:507` `          DTTIME(1) = 2000 + DTTIME(1)                                    30.70`; `43e9bbb:src/ocpids.ftn:509` `          DTTIME(1) = 1900 + DTTIME(1)`; `43e9bbb:src/ocpids.ftn:530` `          DTTIME(II) = 0`; R7:N-016.)
- processor speed: % of 100. 예 1.5배 빠른 노드 = `150`/`100` → 구조 격자의 1000 active point 를 600/400 자동 분배(MPI 부하균형, [swan-tech-ch7-parallel](swan-tech-ch7-parallel.md) §7.1 load balancing 의 사용자측).

150:100에 따른 600:400 예시는 구조 격자의 활성점 분할에 해당한다. 현재 Metis 경로의 목표 가중치는 모든 프로세서에 동일하다. (swanimp PDF 29쪽 / 인쇄 23쪽; `src/swanparll.ftn:2263–2294` `IWORK(2,I) = (NACTP*ICNT)/SUM(IWEIG) - NPCUM`; `src/SwanParallel.ftn90:481–483` `tpwgts = 1./real(np)`; R7:N-017.)

## 10. Run instructions (node20)

명령 파일(`.swn`) 완성 후 실행. `swan.edt`는 편집용 구문표이다. 이를 숨은 개발용 명령까지 포함하는 전수 명세로 읽지 않는다. (swanimp PDF 31쪽 / 인쇄 25쪽: `complete set of commands`; `src/swanpre1.ftn:637–642` `!     COTE [cotes]         (NOT documented)`와 `IF (KEYWIS ('COTE')) THEN`; R7:N-018.)
```
swanrun filename [nprocs]                   # Windows .bat (default nprocs=1)
./swanrun -input filename [-omp n | -mpi n]  # UNIX (chmod +rx 선행)
./swanrun -input f31har01 -omp 4 > swanout & # 예
```
- PATH 예시는 swan.exe가 그 디렉터리에 있을 때 유효하다. CMake로 설치한 실행 파일은 설치 위치의 bin에 있다. 래퍼에는 -omp n을 전달한다. UNIX 래퍼는 기존 OMP_NUM_THREADS 값을 1로 덮어쓴다. (swanimp PDF 32–33쪽 / 인쇄 26–27쪽; `src/CMakeLists.txt:124` `install( TARGETS ${EXE} swan${VERSION} RUNTIME DESTINATION bin LIBRARY DESTINATION lib ARCHIVE DESTINATION lib )`; `bin/swanrun:10` `export OMP_NUM_THREADS=1`; `bin/swanrun:84–86` `if [ $npomp -gt 1 ]; then`, `export OMP_NUM_THREADS=$npomp`; R7:N-019·I-049.)
- UNIX 래퍼는 MPI 프로세스 수가 1보다 클 때 machinefile을 전달한다. Windows 래퍼는 이 파일을 전달하지 않는다. 콜론 뒤 수는 요청한 MPI 프로세스 배치 수이다. (swanimp PDF 33쪽 / 인쇄 27쪽; `bin/swanrun:92–96` `if [ $npmpi -gt 1 ]; then`, `mpirun -np $npmpi -machinefile machinefile swan.exe`; `bin/swanrun.bat:34–39` `mpiexec -n %nprocs% swan.exe`; R7:N-020.)
- 출력: `PRINT`(MPI 면 `PRINT-001`…), table/spectra/block(사용자 이름), `Errfile`(에러 시만 생성), `ERRPTS`(비수렴 등 grid-point). hotfile 다중→단일 병합 `hcat.exe`(swanhcat.ftn, 40.51A+, `hcat.nml`).
- pre-built Windows 는 Intel® Fortran Classic + DLL → **Intel® Fortran Runtime 설치 필요**.

## 11. Testing SWAN (node21)

패키지 = `swan.exe` + `swan.edt` + `swanrun(.bat)`. 사이트의 test 입출력(`.swn` command, `.bot` bottom 등)으로 구성 테스트. **결과는 마지막 자리까지 동일할 필요 없음**.

50 MB 이상은 시험 사례의 권장 메모리이다. 원문은 현실적인 응용에 100–500 MB가 필요할 수 있다고 적는다. 1차원 계산은 대체로 5 MB 미만이라는 안내이다. 이 숫자를 코드가 보장하는 고정 메모리 요구량으로 쓰지 않는다. (swanimp PDF 35쪽 / 인쇄 29쪽; R7:N-021.)

## 12. 연결

- [swan-documentation-stack](swan-documentation-stack.md) — 4 docs TOC (본 노트가 swanimp 의 deep 화)
- [swan-programming-rules](swan-programming-rules.md) — swanpgr (코드 스타일; switch/ANSI F90 한계 cross-ref)
- [swan-source-coverage-audit](../source-analysis/swan-source-coverage-audit.md) / [swan-foundation](../source-analysis/swan-foundation.md) — §2 source file map 의 실제 분석
- [swan-parallel-implementation](../source-analysis/swan-parallel-implementation.md) / [swan-tech-ch7-parallel](swan-tech-ch7-parallel.md) — §5 OpenMP/MPI + §5 block Jacobi/wavefront + §9 load balancing
- 공식: http://www.swan.tudelft.nl, GitLab https://gitlab.tudelft.nl/citg/wavemodels/swan

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치 (swanpgr v1.3, 2006-03-22). 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb (2026-07-13 patch B).

표의 원문 인용과 AI 결론은 [R7 §5](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론)에서 옮겼다. 기존 노트 인용의 줄 번호는 이번 반영 전 HEAD 기준이다. [10-13 전수 검증 보완]

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R7:I-003 | 배포 지원·저작권·제공 시험 | swanimp PDF 8·10–11쪽, 인쇄 2·4–5쪽: `Delft University of Technology will not support modified versions of SWAN.` | `README.md:35` `The SWAN software can be used freely under the terms of the [GNU General Public License]` | H 코드 대조 대상 아님 | 지원 정책·재배포 조건·다운로드 안내는 실행 코드와 대조하는 명제가 아니다. |
| R7:I-008 | 지원 플랫폼 표·병렬 효율 | swanimp PDF 16–17쪽, 인쇄 10–11쪽: `supported (and tested)`; `The performance is good for a limited number of threads.` | `src/CMakeLists.txt:42` `if( CMAKE_Fortran_COMPILER_ID MATCHES "GNU" )` | H 코드 대조 대상 아님 | 플랫폼별 시험 이력과 성능 권고는 조건부 경험 주장이다. 현재 컴파일러 분기는 R-004에서 별도로 대조한다. |
| R7:I-013 | Perl 최소 버전 | swanimp PDF 16쪽, 인쇄 10쪽: `at least 5.0.0 or higher` | `CMakeLists.txt:67` `find_package( Perl REQUIRED )` | H 코드 대조 대상 아님 | Perl 5.0.0 이상은 사용자가 갖춰야 하는 설치 전제이다. `find_package( Perl REQUIRED )`는 Perl 존재를 검사하고 버전 하한은 검사하지 않는다. 문서의 설치 전제를 자동 검사한다고 읽을 근거가 없으므로 문서 누락으로 판정하지 않는다. |
| R7:I-015 | -dos·-unix | swanimp PDF 18–19쪽, 인쇄 12–13쪽: `DIRCH1, DIRCH2 ... TABC ... ITABVL` | `switch.pl:91` `if ($dos=~/TRUE/) {$newline=~s/^!DOS//;}`; 92행 `if ($unx=~/TRUE/) {$newline=~s/^!UNIX//;}`; `src/ocpids.ftn:193` `TABC = CHAR(9)`; 이력: `7ee8981:src/ocpids.ftn:193` `TABC = CHAR(9)                                                    40.69` | B 문서 오기 | 41.51 공개 코드도 TABC를 CHAR(9)로 설정한다. TABC까지 -dos·-unix가 선택한다는 설명은 같은 판의 코드와 다르다. |
| R7:I-016 | -f95와 -timg | swanimp PDF 19–20쪽, 인쇄 13–14쪽: `activate the CPU TIME statement`; `remove the switch !TIMG` | `src/swanser.ftn:5852` `!TIMG!F95      CALL CPU_TIME (TIMER)`; `switch.pl:84` `if ($tim=~/TRUE/) {$newline=~s/^!TIMG//;}`; `switch.pl:90` `if ($f95=~/TRUE/) {$newline=~s/^!F95//;}` | C 문서 누락 | swanimp PDF 19쪽은 -f95와 TEST itest=1을 설명한다. PDF 20쪽은 -timg를 제거하지 않으면 시간을 수집·출력하지 않는다고 적는다. 중첩된 `!TIMG!F95` 행을 활성화하려면 `-timg -f95`가 모두 필요하다. C는 두 스위치의 중첩 해제 순서를 직접 설명하지 않은 부분에 한정한다. |
| R7:I-022 | 수동 컴파일·수치형 크기·연속행 | swanimp PDF 20–21쪽, 인쇄 14–15쪽: `cannot be compiled with a Fortran 77 compiler`; `same amount of memory for all INTEGERS, REAL and LOGICALS`; `limit of 19 continuation lines is violated` | `CMakeLists.txt:17` `project( SWAN Fortran )`; `src/CMakeLists.txt:46` `set( CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fallow-argument-mismatch" )` | H 코드 대조 대상 아님 | 컴파일러 규격과 INTEGER·REAL·LOGICAL의 저장 크기는 설치 제약이다. CMake는 Fortran 프로젝트를 구성한다. 연속행 예외는 같은 매뉴얼 PDF 21쪽에 명시되어 있다. 대표 선언의 연결행은 P-008에서 대조한다. |
| R7:I-024 | 모듈 선행 목록 | swanimp PDF 21쪽, 인쇄 15쪽: `SwanSpectPart.f90`; `SwanIEM.f90`; swanimp PDF 10쪽, 인쇄 4쪽: `SwanSpectPart.ftn` | `src/srclist.cmake:4` `${SRC}/SwanSpectPart.${EXTF}`; 13행 `${SRC}/SwanIEM.f90`; `switch.pl:63` `$ext = ($file =~ m/ftn90/) ? "f90" : "f";` | B 문서 오기 | 같은 문서의 material 목록은 `SwanSpectPart.ftn`으로 적는다. `switch.pl`은 -unix에서 이 파일을 `.f`로 변환한다. PDF 21쪽의 `SwanSpectPart.f90`은 그 목록 및 코드와 다른 확장자 오기이다. |
| R7:I-025 | 라이브러리 없는 링크 | swanimp PDF 21쪽, 인쇄 15쪽: `Linking should be done without any options nor using shared libraries`; 같은 쪽 예시: `mpif90 <list of modules> ocp*.f swan*.f Swan*.f90 -o swan.exe`; PDF 22쪽 §3.2.4–3.2.6은 MPI·Metis·netCDF 설치를 설명한다. | `src/CMakeLists.txt:108` `target_link_libraries( swan${VERSION} PUBLIC NetCDF::NetCDF_Fortran )`; 120행 `target_link_libraries( ${EXE} swan${VERSION} ${MPI_Fortran_LIBRARIES} )` | F 표기 차이 | 문장은 math·NAG 같은 별도 라이브러리 옵션을 쓰지 않는 수동 링크 예시와 함께 제시된다. 같은 매뉴얼은 MPI·Metis·netCDF 선택 빌드의 외부 라이브러리를 별도로 요구한다. 모든 빌드가 라이브러리 없이 링크된다는 뜻으로 확장하지 않는다. 링크 옵션 생략과 선택 라이브러리 의존성을 구분하는 F로 낮춘다. |
| R7:I-029 | netCDF 버전·Fortran 인터페이스 | swanimp PDF 22쪽, 인쇄 16쪽: `netCDF 4.5.x or greater`; `The Fortran interface must have been enabled` | `CMakeLists.txt:77` `find_package( NetCDF REQUIRED COMPONENTS Fortran )` | H 코드 대조 대상 아님 | netCDF 4.5.x 이상과 Fortran 인터페이스는 사용자가 준비할 설치 전제이다. CMake의 이 호출은 Fortran 구성 요소를 요구하지만 버전 하한을 전달하지 않는다. 문서가 버전 자동 검사를 약속하지 않으므로 문서 누락으로 판정하지 않는다. |
| R7:I-030 | CMake 최소 버전 | swanimp PDF 24쪽, 인쇄 18쪽: `CMake 3.12+` | `CMakeLists.txt:6` `cmake_minimum_required( VERSION 3.20 )`; 이력: `7ee8981:CMakeLists.txt:6` `cmake_minimum_required( VERSION 3.12 )`; `acb58b3:CMakeLists.txt:6` `cmake_minimum_required( VERSION 3.20 )`; 변경·대조 커밋: `acb58b3 2026-01-30 small updates (300126)` | A 판 차이 | Git 배포의 CMake 최소 버전은 2026-01-30에 3.12에서 3.20으로 바뀌었다. git 판정 근거는 `acb58b3`(2026-01-30)이다. |
| R7:I-032 | out-of-source 설명 | swanimp PDF 24쪽, 인쇄 18쪽: `build files will not be created in the /swan/src directory` | `CMakeLists.txt:53` `set( SRC ${CMAKE_SOURCE_DIR}/src )`; `src/CMakeLists.txt:36` `execute_process( COMMAND ${PERL_EXECUTABLE} ${CMAKE_SOURCE_DIR}/switch.pl ${SWITCHES} ${SRC}/*.ftn ${SRC}/*.ftn90 )`; `switch.pl:64` `$outfile = join(".",$tempf,$ext);`; `switch.pl:73–77`은 변환 출력 파일을 `open(OUTFILE,">".$outfile);`로 연다. | F 표기 차이 | 문서는 CMake의 build 디렉터리를 설명한다. 전처리된 Fortran 소스는 `set( SRC ${CMAKE_SOURCE_DIR}/src )`와 원본 파일명을 사용하여 src에 생성한다. 문서의 `build files`를 모든 생성 파일로 확장한 B 판정을 F로 낮춘다. 생성 소스와 CMake 빌드 산출물의 위치를 구분한다. |
| R7:I-033 | 기본 설치 경로 | swanimp PDF 25쪽, 인쇄 19쪽: `/usr/local/swan`; `C:\PROGRAM FILES\swan` | `CMakeLists.txt:10` `cmake_path( SET LOCALSWAN $ENV{LOCALAPPDATA}/Programs/wavemodels/swan )`; 13행 `set( CMAKE_INSTALL_PREFIX "$ENV{HOME}/wavemodels/swan" CACHE STRING "" )`; 이력: `7ee8981:CMakeLists.txt:10` `set( CMAKE_INSTALL_PREFIX "C:/Program Files/swan" CACHE STRING "" )`; `7ee8981:CMakeLists.txt:12` `set( CMAKE_INSTALL_PREFIX "/usr/local/swan" CACHE STRING "" )`; `acb58b3:CMakeLists.txt:10` `cmake_path( SET LOCALSWAN $ENV{LOCALAPPDATA}/Programs/wavemodels/swan )`; `acb58b3:CMakeLists.txt:11` `set( CMAKE_INSTALL_PREFIX "${LOCALSWAN}" CACHE STRING "" )`; `acb58b3:CMakeLists.txt:13` `set( CMAKE_INSTALL_PREFIX "$ENV{HOME}/wavemodels/swan" CACHE STRING "" )`; 변경·대조 커밋: `acb58b3 2026-01-30 small updates (300126)` | A 판 차이 | 기본 설치 경로는 2026-01-30에 사용자 폴더로 바뀌었다. UNIX 기본값은 $HOME/wavemodels/swan이다. Windows 기본값은 %LOCALAPPDATA%/Programs/wavemodels/swan이다. git 판정 근거는 `acb58b3`(2026-01-30)이다. |
| R7:I-043 | 두 자리 연도 유효 범위 | swanimp PDF 28쪽, 인쇄 22쪽: `January 1, 1911 and December 31, 2010 (both inclusive)` | `src/ocpids.ftn:494` `INTEGER :: JUMPYEAR = 30     ! Used in interpretation of 2-digit year code`; 506행 `IF (DTTIME(1).LT.JUMPYEAR) THEN`; 507행 `DTTIME(1) = 2000 + DTTIME(1)`; 이력: `7ee8981:src/ocpids.ftn:494` `INTEGER :: JUMPYEAR = 30     ! Used in interpretation of 2-digit year code`; `src/ocpids.ftn:519–546`은 형식 3·5·6에도 같은 분기를 적용하며 형식 4는 날짜를 0으로 둔다. | B 문서 오기 | 41.51 공개 코드도 두 자리 연도의 분기값으로 30을 사용한다. 형식 2·3·5·6의 연도 범위는 1930–2029이다. 1911–2010이라는 문서 범위는 같은 판의 코드와 다르다. swanimp PDF 28쪽 이미지의 1911–2010 표기를 확인했다. |
| R7:I-045 | Windows 사전 빌드·시험 메모리·동일 끝자리 불요 | swanimp PDF 31·35쪽, 인쇄 25·29쪽: `linked to DLL libraries`; `at least 50 MBytes`; `need not to be identical up to the last digit` | `README.md:245` `1. **serial**: for computers using one processor (recommended for small tests)` | H 코드 대조 대상 아님 | Windows 사전 빌드의 DLL 구성은 배포 환경 설명이다. 50 MBytes 이상은 제공 시험에 대한 권고이다. 마지막 자리까지 일치할 필요가 없다는 문장은 결과 비교 지침이다. 세 문장을 현재 소스의 메모리 보장이나 수치 동등성 주장으로 바꾸지 않는다. |
| R7:I-048 | 환경 변수의 관리자 권한 | swanimp PDF 32쪽, 인쇄 26쪽: `you must be an administrator in order to modify an environment variable` | `README.md:134` `(These directories allow app installation without requiring administrator rights.) Instead, you may install SWAN in any other user-defined directory, as follows` | H 코드 대조 대상 아님 | 운영체제의 환경 변수 편집 권한에 관한 안내이다. SWAN 코드의 요구 조건으로 쓰지 않는다. |
| R7:I-049 | OMP_NUM_THREADS | swanimp PDF 32–33쪽, 인쇄 26–27쪽: `export OMP_NUM_THREADS=4`; `the UNIX script will set OMP NUM THREADS to n`; swanimp PDF 33쪽: `default: n = 1` | `bin/swanrun:10` `export OMP_NUM_THREADS=1`; 85행 `export OMP_NUM_THREADS=$npomp` | C 문서 누락 | swanimp는 `-omp n`의 설정과 생략 시 기본값 1을 적는다. Unix 래퍼는 시작할 때 기존 `OMP_NUM_THREADS`도 1로 덮어쓴다. C는 외부 환경 값까지 덮어쓰는 초기화 설명이 없는 부분에 한정한다. 1보다 큰 스레드 수를 래퍼에 전달하려면 `-omp n`을 사용한다. |
| R7:I-052 | 실행 권한·리다이렉션·백그라운드·공유 실행 파일 | swanimp PDF 32–33쪽, 인쇄 26–27쪽: `chmod +rx ./swanrun`; `Use an ampersand`; `placing it in a shared directory` | `bin/swanrun:93` `mpirun -np $npmpi -machinefile machinefile swan.exe` | H 코드 대조 대상 아님 | chmod·리다이렉션·백그라운드 실행·공유 실행 파일은 쉘과 MPI 환경의 사용 절차이다. `swanrun`의 MPI 호출은 이 절차를 사용하는 래퍼 경로의 근거이다. 권한 정책과 배치 환경 자체는 모델 계산 코드 대조 대상이 아니다. |
| R7:I-053 | machinefile | swanimp PDF 33쪽, 인쇄 27쪽: `one node per line`; `node2:2`; `a space should be used instead of a colon`; 같은 쪽: `may also need a machinefile` | `bin/swanrun:93` `mpirun -np $npmpi -machinefile machinefile swan.exe`; `bin/swanrun.bat:39` `mpiexec -n %nprocs% swan.exe` | C 문서 누락 | swanimp의 `may also need a machinefile`은 조건부 안내이다. Unix 래퍼는 `-machinefile machinefile`을 전달한다. Windows 래퍼의 `mpiexec -n %nprocs% swan.exe`에는 이 인자가 없다. C는 Windows용 파일 구문을 안내하면서 제공 배치 파일에는 전달 절차가 없다는 부분에 한정한다. |
| R7:I-056 | swan.edt의 역할·파일 목록 | swanimp PDF 31·35쪽, 인쇄 25·29쪽: `contains the complete set of commands`; `a command file (swan.edt)`; `../raw/manuals/website/online_doc/swanimp/node20.html:76–78`; `../raw/manuals/website/online_doc/swanimp/node21.html:42–43`; `../raw/manuals/website/online_doc/swanuse/node47.html:52–57` `the edit file`; `../raw/manuals/website/online_doc/swanuse/node49.html:53` | `misc/swan.edt:1` `!   PROJECT  'name'  'nr'`; 345행 `!   STOP` | F 표기 차이 | swanimp node21은 swan.edt를 command file이라 부르지만 swanimp node20·swanuse node47·node49는 편집용 구문표로 설명한다. 코드 파일은 전 행이 주석이다. |
| R7:I-057 | 삭제된 소스 파일 | swanimp PDF 9쪽, 인쇄 3쪽: `SwanThreadBounds.ftn90` | `git log -- src/SwanThreadBounds.ftn90`: `0dabfa4`(2026-07-13)에서 삭제. `src/SwanCompUnstruc.ftn90:823` `! loop over a fixed number of sweeps through grid`; 이력: `7ee8981:src/SwanThreadBounds.ftn90:1` `subroutine SwanThreadBounds ( nwetp, ivlow, ivup, tlist, n )`; `git show 0dabfa4 -- src/SwanThreadBounds.ftn90`은 `deleted file mode 100644`이다. `src/SwanCompUnstruc.ftn90:839–849`은 !GRAPH·!FXFRO에 따른 front 목록 선택이다. 변경·대조 커밋: `0dabfa4 2026-07-13 updated src (patch B)` | A 판 차이 | patch B는 SwanThreadBounds.ftn90을 삭제했다. 현재 비정렬 계산은 front 목록을 직접 순회한다. git 판정 근거는 `0dabfa4`(2026-07-13)이다. |
| R7:I-058 | 배포 목록의 두 coupler 파일 | swanimp PDF 10쪽, 인쇄 4쪽: `couple2adcirc.ftn90`; `swan2coh.ftn90` | `switch.pl:97` `if ($adc=~/TRUE/) {$newline=~s/^!ADC//;}`; 99행 `if ($coh=~/TRUE/) {$newline=~s/^!COH//;}`; git 전체 이력의 두 파일 경로 검색은 0커밋이다. `2980d1a:switch.pl:95`에도 !ADC 치환만 있다. [확정 검색 근거](../../../_staging/recovery/compare/SWAN-git-verify-D.md). | D 문서에만 있음 | couple2adcirc.ftn90과 swan2coh.ftn90은 조사한 Git 배포에 없다. 전처리 스위치의 존재는 두 coupler 파일의 배포 근거가 아니다. swanimp PDF 8–10쪽의 목록은 tarball 목록이므로 이 판정을 tarball 자체의 파일 부재로 확대하지 않는다. |
| R7:I-059 | material 목록의 SwanIEM 누락 | swanimp PDF 8–10쪽, 인쇄 2–4쪽: `The source tarball swan4151.tar.gz ... consists of the following files`; PDF 21쪽, 인쇄 15쪽: `SwanIEM.f90` | `src/srclist.cmake:13` `${SRC}/SwanIEM.f90` | C 문서 누락 | C는 swanimp PDF 8–10쪽의 material 목록에 한정한다. 같은 매뉴얼 PDF 21쪽의 모듈 컴파일 목록과 Git `srclist.cmake`에는 SwanIEM이 있다. SWAN 문서 전체에 설명이 없다는 뜻이 아니다. |
| R7:R-003 | ANSI Fortran90만의 이식성 설명 | swanimp PDF 15쪽 및 `../raw/manuals/website/online_doc/swanimp/node5.html:49–53`은 Fortran 2003 stream·Fortran 2008 명령 실행 예외를 명시한다. | `README.md:63` `Due to the use of ANSI standard Fortran90 the SWAN source code can be ported to various architectures (e.g., Windows, Linux, macOS and Unix-like systems).`; `src/swanser.ftn:7397` `CALL EXECUTE_COMMAND_LINE('mkdir '//TRIM(PATH), EXITSTAT=ESTAT,` | C 문서 누락 | README의 ANSI Fortran90 설명에는 두 예외가 없다. 구현 매뉴얼에는 예외가 있다. C는 README에 한정하며 SWAN 문서 전체의 누락으로 확대하지 않는다. |
| R7:R-006 | out-of-source 문장 |  | `README.md:88` ``This step is required to perform an out-of-source build with CMake, that is, build files will not be created in the `/swan/src` directory.``; `src/CMakeLists.txt:36` `execute_process( COMMAND ${PERL_EXECUTABLE} ${CMAKE_SOURCE_DIR}/switch.pl ${SWITCHES} ${SRC}/*.ftn ${SRC}/*.ftn90 )`; `switch.pl:73–77`은 변환 출력 파일을 `open(OUTFILE,">".$outfile);`로 연다. | F 표기 차이 | 문서는 CMake의 build 디렉터리를 설명한다. 전처리된 Fortran 소스는 `set( SRC ${CMAKE_SOURCE_DIR}/src )`와 원본 파일명을 사용하여 src에 생성한다. 문서의 `build files`를 모든 생성 파일로 확장한 B 판정을 F로 낮춘다. 생성 소스와 CMake 빌드 산출물의 위치를 구분한다. |
| R7:R-007 | 설치 경로 본문·표 |  | `README.md:133` ``The default install directory is `$HOME/wavemodels/swan` (Unix-like operating systems, including macOS) or `%LocalAppData%\Programs\wavemodels\swan` (Windows).``; 166행 `../wavemodels/swan`; `CMakeLists.txt:13` `set( CMAKE_INSTALL_PREFIX "$ENV{HOME}/wavemodels/swan" CACHE STRING "" )` | B 문서 오기 | 본문은 맞는다. 표의 상대경로를 문자 그대로 쓰면 기본값과 같지 않다. OS별 절대경로로 표를 고쳐야 한다. |
| R7:R-010 | mpirun의 n 의미 |  | `README.md:266` `mpirun -np <n> swan.exe`; 269행 ``with `<n>` the number of desired nodes.``; `bin/swanrun:93` `mpirun -np $npmpi -machinefile machinefile swan.exe`; `misc/machinefile:4` `# after the node name to indicate how many processes to launch` | B 문서 오기 | n은 MPI 프로세스 수이다. 노드 수와 구분해야 한다. 한 노드에 여러 프로세스를 배치할 수 있다. |
| R7:C-001 | README에 없는 CMake 옵션 |  | README 옵션 표(`README.md:164–173`)와 swanimp PDF 25쪽(인쇄 19쪽)에는 JAC·FFRO가 없다. swanimp PDF 19쪽은 별도의 `-jac` 전처리 옵션을 설명한다.; `CMakeLists.txt:42–47` `option( JAC "" OFF )`, `option( FFRO "" OFF )` | C 문서 누락 | CMake의 JAC·FFRO 옵션은 기본값이 OFF이다. 문서에 있는 `-jac` 스위치 설명과 CMake 옵션 표의 누락을 구분한다. |
| R7:C-002 | OpenMP와 MPI의 동시 선택 거부 | swanimp PDF 25쪽의 MPI·OPENMP 옵션 표에는 동시 선택 시의 구성 중단 조건이 없다. | `src/CMakeLists.txt:17–19,71–75` `set( MPI ON )`, `if( OPENMP AND MPI )`, `message( FATAL_ERROR "-- Cannot use both OpenMP and MPI" )` | C 문서 누락 | OPENMP와 MPI가 함께 참이면 구성을 중단한다. JAC는 18행 `set( MPI ON )`으로 MPI를 켠다. |
| R7:C-003 | Metis 선택의 MPI 의존성 미검사 | swanimp PDF 22쪽(인쇄 16쪽), `../raw/manuals/website/online_doc/swanimp/node13.html:48–51`은 `an MPI implementation is still required`라고 적는다. CMake가 MPI 옵션을 켜거나 의존성을 검사하는지는 적지 않는다. | `src/CMakeLists.txt:17–24` `if( JAC )`, `set( MPI ON )`, `if( METIS )`, `list( APPEND SWITCHES -metis )` | C 문서 누락 | Metis의 MPI 요구는 문서에 있다. METIS만 선택해도 CMake는 -metis를 추가한다. 이 분기는 JAC 분기와 달리 MPI를 자동으로 켜지 않는다. C는 이 옵션 처리 차이의 설명 누락으로 한정한다. |
| R7:C-004 | 비 GNU MPI의 호환 모듈 스위치 | swanimp PDF 20쪽(인쇄 14쪽)은 USE MPI를 지원하지 않는 컴파일러의 -impi를 설명한다. CMake가 GNU 여부만으로 이를 선택하는 규칙은 적지 않는다. | `src/CMakeLists.txt:9–14` `if( MPI OR JAC )`, `if( CMAKE_Fortran_COMPILER_ID MATCHES "GNU" )`, `list( APPEND SWITCHES -impi -mpi )` | C 문서 누락 | MPI 또는 JAC를 선택하면 GNU 이외 컴파일러에 -impi와 -mpi를 함께 추가한다. 문서의 USE MPI 호환성 설명과 이 CMake 선택 규칙을 구분한다. |
| R7:C-005 | 빌드 유형 강제 | swanimp PDF 24–26쪽의 CMake 설정 절에는 CMAKE_BUILD_TYPE을 None으로 강제하는 설명이 없다. | `CMakeLists.txt:23` `set( CMAKE_BUILD_TYPE None CACHE STRING "" FORCE )` | C 문서 누락 | 사용자가 지정한 CMAKE_BUILD_TYPE도 None으로 다시 저장한다. |
| R7:C-006 | 컴파일러 기본 플래그 덮어쓰기 | swanimp PDF 24–26쪽은 컴파일러 지정 방법을 설명한다. CMAKE_Fortran_FLAGS 캐시를 FORCE로 다시 쓰는 조건은 적지 않는다. | `src/CMakeLists.txt:42–66` `set( CMAKE_Fortran_FLAGS "-O -w -fno-second-underscore -ffree-line-length-none" CACHE STRING "" FORCE )` | C 문서 누락 | GNU·Intel·PGI·Fujitsu·XL 분기는 CACHE FORCE를 쓴다. 사용자가 넘긴 CMAKE_Fortran_FLAGS를 보존하는 방식이 아니다. |
| R7:C-007 | GNU 버전별 호환 플래그 | swanimp의 CMake 절에는 GNU 버전별 조건이 없다. 공개 patch 41.51.A:123은 classic FLAGS_MSC의 -fallow-argument-mismatch를 별도로 기록한다. | `src/CMakeLists.txt:45–49` `if( ${CMAKE_Fortran_COMPILER_VERSION} VERSION_GREATER_EQUAL 10 )`, `set( CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fallow-argument-mismatch" )`, `if( WIN32 AND ${CMAKE_Fortran_COMPILER_VERSION} VERSION_GREATER_EQUAL 7 )`, `set( CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fdec" )` | C 문서 누락 | CMake는 GNU 10 이상에서 -fallow-argument-mismatch를 추가한다. Windows의 GNU 7 이상에서는 -fdec도 추가한다. C는 이 버전·운영체제 조건의 설명 누락으로 한정한다. |
| R7:C-008 | 전처리 결과의 반환 코드 미검사 | swanimp PDF 24–26쪽의 CMake 절에는 switch.pl 실행 결과의 오류 처리 규칙이 없다. | `src/CMakeLists.txt:35–39` `execute_process( COMMAND ${PERL_EXECUTABLE} ${CMAKE_SOURCE_DIR}/switch.pl ${SWITCHES} ${SRC}/*.ftn ${SRC}/*.ftn90 )` | C 문서 누락 | execute_process에는 RESULT_VARIABLE이나 COMMAND_ERROR_IS_FATAL 설정이 없다. Perl 발견 실패에 대한 38행 FATAL_ERROR와 구분한다. |
| R7:C-009 | 생성 소스의 위치와 재생성 조건 | swanimp PDF 20쪽과 `../raw/manuals/website/online_doc/swanimp/node10.html:141–142`는 -unix의 확장자 변경을 설명한다. 출력 파일의 존재·수정시각으로 재생성을 결정하는 규칙은 적지 않는다. | `switch.pl:62–74` `$outfile = join(".",$tempf,$ext);`, `if (   (! -e $outfile)`, `\|\| (-M $file < -M $outfile) ) #.ftn file recently modified` | C 문서 누락 | 생성 소스는 원본과 같은 경로에 놓인다. 출력이 없거나 원본이 더 새로울 때만 다시 쓴다. 확장자 변경은 문서에 있다. 스위치 변경 자체가 재생성 조건이 아니라는 설명은 없다. |
| R7:C-010 | 알 수 없는 전처리 인자 | swanimp PDF 18–20쪽은 지원하는 옵션을 나열한다. 알 수 없는 하이픈 인자의 처리 규칙은 적지 않는다. | `switch.pl:19–37` `while ( $ARGV[0]=~/-.*/ )` | C 문서 누락 | 21–37행의 알려진 인자만 shift한다. 하이픈을 포함하지만 어느 분기에도 맞지 않는 첫 인자는 while 조건을 계속 만족한다. 이 판단은 제어 흐름 판독 결과이다. |
| R7:C-011 | ESMF의 배타 조합 | 네 매뉴얼 판독 기록과 웹 문서의 -esmf·-adcirc·-metis 검색에서 ESMF 배타 조합의 설명은 없다. | `switch.pl:41–47` `if ($esmf=~/TRUE/ && $adc=~/TRUE/)`, `die "$0: -esmf and -adcirc is not supported.\n";`, `if ($esmf=~/TRUE/ && $met=~/TRUE/)`, `die "$0: -esmf and -metis is not supported.\n";` | C 문서 누락 | ESMF와 ADCIRC를 함께 선택하면 종료한다. 47행은 ESMF와 Metis의 동시 선택도 거부한다. |
| R7:C-012 | 겹친 전처리 표식의 처리 순서 | swanimp PDF 18–20쪽은 각 표식의 제거를 설명한다. 겹친 표식의 처리 순서는 적지 않는다. | `switch.pl:81–105` `# ESMF must be processed first`, `if ($esmf=~/TRUE/) {$newline=~s/^!ESMF//;}`; `src/swanser.ftn:5852` `!TIMG!F95      CALL CPU_TIME (TIMER)` | C 문서 누락 | ESMF 표식을 먼저 처리한다. 뒤에 남은 다른 표식은 84–105행에서 순서대로 처리한다. 선택하지 않은 다른 표식이 남으면 그 행은 계속 주석이다. |
| R7:C-013 | 병렬 라이브러리 검색 캐시 정리 | swanimp PDF 25쪽의 병렬 옵션 표에는 다른 병렬 방식의 탐색 캐시를 지우는 규칙이 없다. | `src/CMakeLists.txt:81–94` `unset( MPI_Fortran_FOUND CACHE )`, `unset( OpenMP_Fortran_FLAGS CACHE )` | C 문서 누락 | OpenMP 경로는 MPI 검색 캐시를 지운다. MPI 경로는 OpenMP_Fortran_FLAGS 캐시를 지운다. 직렬 경로는 두 종류의 캐시를 지운다. |
| R7:C-014 | OpenMP 환경 변수 초기화 | swanimp PDF 32–33쪽과 `../raw/manuals/website/online_doc/swanimp/node20.html:172–184`는 -omp n의 환경 변수 설정과 생략값 n=1을 설명한다. 기존 환경 값을 래퍼 시작 때 덮어쓰는 동작은 적지 않는다. | `bin/swanrun:7–10,84–85` `export OMP_NUM_THREADS=1`, `if [ $npomp -gt 1 ]; then`, `export OMP_NUM_THREADS=$npomp` | C 문서 누락 | -omp n의 설정과 생략값 1은 문서에 있다. UNIX 래퍼는 시작할 때 기존 OMP_NUM_THREADS도 1로 덮어쓴다. n이 1보다 클 때만 실행 직전에 다시 설정한다. |
| R7:C-015 | UNIX 실행 인자의 짝·입력 경로 | swanimp PDF 33쪽은 입력 파일명과 -omp·-mpi 구문을 설명한다. 남은 인자가 하나일 때와 디렉터리 접두어의 처리 규칙은 적지 않는다. | `bin/swanrun:16–27` `while [ $# -ge 2 ]`, ``-input) input=`basename $2 .swn`;;`` | C 문서 누락 | 인자가 두 개 이상 남은 동안만 파싱한다. 홀로 남은 인자는 처리하지 않는다. 19행의 basename은 입력 디렉터리와 .swn 접미사를 제거한다. |
| R7:C-016 | 알 수 없는 실행 인자의 종료 상태 | swanimp 제5장 실행 안내에는 잘못된 인자와 입력 이름 누락의 종료 상태 차이가 없다. | `bin/swanrun:22–25,34–40` `exit ;;`, `exit 1` | C 문서 누락 | 알 수 없는 인자는 사용법을 출력하고 인자 없는 exit로 끝낸다. 입력 이름 누락은 40행 `exit 1`로 끝낸다. |
| R7:C-017 | MPI 실행기 탐색 조건 | swanimp PDF 32쪽은 MPI 실행기의 PATH 설정을 설명한다. 래퍼가 mpirun을 일반 파일 여부로 찾는 조건은 적지 않는다. | `bin/swanrun:47–54`의 IFS 설정과 PATH 반복; `if test -f $dir/mpirun; then`. | C 문서 누락 | PATH를 분리하려고 IFS에 콜론을 추가한다. mpirun을 일반 파일 여부로 검사한다. 실행 권한 검사는 이 조건에 없다. |
| R7:C-019 | 현재 디렉터리 실행 파일 우선 | swanimp PDF 32쪽은 PATH에 실행 파일 디렉터리를 추가하라고 한다. 현재 디렉터리를 먼저 탐색하는 래퍼 규칙은 적지 않는다. | `bin/swanrun:78–80` `PATH=.:$PATH`, `type swan.exe` | C 문서 누락 | 현재 디렉터리를 PATH 앞에 둔다. 80행 type은 실행 파일 탐색 결과를 출력한다. |
| R7:C-020 | MPI 탐지 후 로컬 심볼릭 링크 | 공개 patch 41.51.A:366–368,390–391에 심볼릭 링크 생성·정리 문맥이 있다. swanimp 제5장에는 MPI 실행기를 발견하면 단일 프로세스에서도 링크 분기에 들어가는 조건이 없다. | `bin/swanrun:47–54,87–95,129–130` `elif [ $npmpi -gt 1 -o ! -z "$mpi" ]; then`, ``ln -s `which swan.exe` swan.exe`` | C 문서 누락 | mpirun을 발견하고 OpenMP 분기를 선택하지 않으면 프로세스 수가 1이어도 링크 분기에 들어갈 수 있다. 로컬 swan.exe가 없으면 링크를 만든다. 정리는 이번 호출이 만든 링크에 한정한다. C는 단일 프로세스에서 이 분기에 들어가는 조건의 설명 누락이다. |
| R7:C-021 | 두 병렬 실행 인자의 우선순위 | swanimp PDF 33쪽(인쇄 27쪽), `../raw/manuals/website/online_doc/swanimp/node20.html:163–184`의 구문은 `./swanrun -input filename [-omp n \| -mpi n]`이다. | `bin/swanrun:84–100` `if [ $npomp -gt 1 ]; then`, `elif [ $npmpi -gt 1 -o ! -z "$mpi" ]; then`, `if [ $npmpi -gt 1 ]; then` | H 코드 대조 대상 아님 | 문서는 -omp와 -mpi를 택일로 제시한다. 두 값을 모두 1보다 크게 주는 조합은 문서 구문 밖이다. 이 조합에서 코드는 OpenMP 실행을 먼저 선택하고 npmpi로 결과 정리를 선택한다. 이 동작을 문서가 지원하는 조합의 누락으로 판정하지 않는다. |
| R7:C-023 | UNIX 결과 정리와 종료 상태 | swanimp PDF 31·33쪽은 명령 파일을 INPUT으로 복사하고 PRINT 결과의 이름을 바꾸는 절차를 설명한다. 모델 종료 상태의 전달 규칙은 적지 않는다. | `bin/swanrun:81–136` `cp $input.swn INPUT`, `rm -f INPUT` | C 문서 누락 | INPUT 복사와 결과 이름 변경은 문서에 있다. 래퍼는 실행 명령의 종료 상태를 별도 변수에 저장하거나 그 상태로 종료하지 않는다. C는 이 종료 상태 처리와 실행 후 INPUT 삭제의 설명 누락으로 한정한다. |
| R7:C-024 | Windows 실패 후 정리 생략 | swanimp 제5장은 실행 후 PRINT 결과 복사를 설명한다. Windows 실행 실패 때 정리를 건너뛰는 조건은 적지 않는다. | `bin/swanrun.bat:34–49,75–83` `if errorlevel 1 goto END`, `del INPUT` | C 문서 누락 | 실행 명령이 실패 상태를 반환하면 결과 이름 변경과 79행의 INPUT 삭제를 건너뛴다. |
| R7:C-025 | Windows 프로세스 수 상한 검사 위치 | swanimp PDF 33쪽의 nprocs 설명에는 999 상한 검사의 위치와 PRINT-001 조건이 없다. | `bin/swanrun.bat:39,49–62` `mpiexec -n %nprocs% swan.exe`, `if not exist PRINT-001 goto OK5`, `if %nprocs% GTR 999 goto ERR` | C 문서 누락 | 39행 mpiexec 실행 후 PRINT 파일을 정리하는 단계에서 999 초과 여부를 검사한다. 49행은 PRINT-001이 없으면 이 검사도 건너뛴다. |
| R7:C-026 | Windows MPI 오류 파일 정리 | swanimp PDF 34쪽과 `../raw/manuals/website/online_doc/swanimp/node20.html:224–226`은 MPI 오류 파일이 여러 개일 수 있다고 적는다. Windows 래퍼의 노드별 오류 파일 이름 변경 범위는 적지 않는다. | `bin/swanrun.bat:75–78` `if exist Errfile copy Errfile %inputfile%.erf >> nul`; `bin/swanrun:108–109` `if [ -r Errfile-$inode ]; then`, `mv Errfile-$inode $input.erf-$inode` | C 문서 누락 | Windows 래퍼는 Errfile만 복사한다. UNIX 래퍼 108–109행의 Errfile-노드번호 처리에 대응하는 반복문이 없다. |
| R7:C-028 | 운영체제 스위치와 생성 확장자 | swanimp PDF 18–20쪽, `../raw/manuals/website/online_doc/swanimp/node10.html:54–61,141–142`는 -dos/-unix의 표식 제거와 -unix의 확장자 변경을 이미 설명한다. | `switch.pl:60–74,91–92` `if ($unx=~/TRUE/)`, `$ext = ($file =~ m/ftn90/) ? "f90" : "f";`, `$ext = ($file =~ m/ftn90/) ? "f90" : "for";`, `if ($dos=~/TRUE/) {$newline=~s/^!DOS//;}`, `if ($unx=~/TRUE/) {$newline=~s/^!UNIX//;}` | C 문서 누락 | swanimp node10은 -dos/-unix의 표식 제거와 -unix의 확장자 변경을 적는다. -unix와 -dos를 동시에 지정할 때 UNIX 분기가 확장자를 정하는 규칙은 적지 않는다. 둘 다 없을 때 .ftn에서 .for를 생성하면서 !DOS를 제거하지 않는 동작도 적지 않는다. |
| R7:N-001 | 문서 판과 코드 판 | `swan-implementation-manual.md:5` `external_source: "swanimp (SWAN Implementation Manual, Cycle III version 41.51, SWAN team 2026-03-13). Chapters 1 Introduction(material) / 2 Patch files / 3 Installation(classic GNU make + switch.pl + MPI/Metis/netCDF + CMake) / 4 swaninit / 5 Run / 6 Testing. 공식: http://www.swan.tudelft.nl + GitLab https://gitlab.tudelft.nl/citg/wavemodels/swan."` | `src/swanmain.ftn:968` `CALL BUGFIX ('B')`; 이력 대조: `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:src/swanmain.ftn:964` `      VERNUM = 41.51`; `7ee8981:src/swanmain.ftn:966` `!      CALL BUGFIX ('A')`; `7ee8981:src/swanmain.ftn:967` `!      CALL BUGFIX ('B')`; `c6d3136 2026-03-13 updated src (patch A)`; `c6d3136:src/swanmain.ftn:967` `      CALL BUGFIX ('A')`; `0dabfa4 2026-07-13 updated src (patch B)`; `43e9bbb:src/swanmain.ftn:965` `      VERNUM = 41.51`; `43e9bbb:src/swanmain.ftn:967` `      CALL BUGFIX ('A')`; `43e9bbb:src/swanmain.ftn:968` `      CALL BUGFIX ('B')` | A 판 차이 | 노트의 문서 기준판은 41.51이다. 코드 검증 기준은 43e9bbb의 41.51AB이다. 문서 판독 날짜와 patch 적용 판을 구분한다. git 판정 근거는 `c6d3136`(2026-03-13)·`0dabfa4`(2026-07-13)이다. |
| R7:N-002 | SwanThreadBounds 목록 | `swan-implementation-manual.md:45` ``\| unstructured grids (routines) \| `SwanReadGrid/ReadADCGrid/ReadTriangleGrid/ReadEasymeshGrid`, `SwanInitCompGrid`, `SwanCheckGrid`, `SwanCreateEdges`, `SwanGridTopology/Vert/Cell/Face`, `SwanPrintGridInfo`, `SwanFindPoint`, `SwanPointinMesh`, `SwanBpntlist`, `SwanPrepComp`, `SwanVertlist`, `SwanCompUnstruc`, `SwanDispParm`, `SwanPropvelX/S`, `SwanSweepSel`, `SwanTranspAc/X`, `SwanGradDepthorK`, `SwanGradVel`, `SwanDiffPar`, `SwanGSECorr`, `SwanInterpolatePoint/Ac/Output`, `SwanConvAccur`, `SwanConvStopc`, `SwanThreadBounds`, `SwanFindObstacles`, `SwanCrossObstacle`, `SwanComputeForce` (.ftn90) \|`` | `src/SwanCompUnstruc.ftn90:823` `! loop over a fixed number of sweeps through grid`; 이력 대조: `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:src/SwanThreadBounds.ftn90:1` `subroutine SwanThreadBounds ( nwetp, ivlow, ivup, tlist, n )`; `0dabfa4 2026-07-13 updated src (patch B)`; `git show 0dabfa4 -- src/SwanThreadBounds.ftn90` 원문 `deleted file mode 100644`; `43e9bbb:src/SwanCompUnstruc.ftn90:848` `!GRAPH                ivert = flist(kvert,swpdir)`; `43e9bbb:src/SwanCompUnstruc.ftn90:849` `!FXFRO                ivert = vlist(kvert,swpdir)` | A 판 차이 | SwanThreadBounds는 41.51 공개 코드에 있던 파일이다. patch B는 이 파일을 삭제했다. 노트의 현재 소스 목록에서 삭제 사실을 구분한다. git 판정 근거는 `0dabfa4`(2026-07-13)이다. |
| R7:N-003 | classic 부속 파일 | `swan-implementation-manual.md:61` ``- 부속 파일: `INSTALL.README`, `Makefile`, `macros.inc`, `which.cmd`, `platform.pl`, `switch.pl`, `SWANRUN.README`, `swanrun`/`swanrun.bat`, `machinefile`, `swanhcat.ftn`+`hcat.nml`(hotfile 병합), `swan.edt`(edit file), `plotunswan.m`/`plotgrid.m`(unstructured Matlab).`` | `Makefile:44` `cd build && cmake $(CURDIR) $(CMAKE_FLAGS)`; 이력 대조: `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:README.md:74` `$ cmake .. -G Ninja`; `acb58b3 2026-01-30 small updates (300126)`; `43e9bbb:Makefile:42` `config: clobber`; Git 이력의 `Makefile` 추가는 classic 파일의 교체 이력이 아니다. | C 문서 누락 | INSTALL.README·macros.inc·which.cmd·platform.pl은 classic tarball 목록으로 한정한다. 41.51 공개 시점의 Git 배포도 CMake를 사용했다. 현재 Git Makefile은 뒤에 추가한 CMake 래퍼이다. |
| R7:N-005 | make config와 실행 target | `swan-implementation-manual.md:76` `make config        # macros.inc 생성 (1회, 필수 선행)` | `Makefile:42` `config: clobber`; 이력 대조: `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:README.md:74` `$ cmake .. -G Ninja`; `acb58b3 2026-01-30 small updates (300126)`; `43e9bbb:Makefile:42` `config: clobber`; Git 이력의 `Makefile` 추가는 classic 파일의 교체 이력이 아니다. | C 문서 누락 | macros.inc를 만드는 make config와 make ser·make omp·make mpi는 classic 절차이다. 현재 Git make config는 build를 다시 만드는 래퍼이다. 이 배포 범위 구분은 41.51 공개 코드에도 필요했다. |
| R7:N-006 | Windows OpenMP의 Intel 한정 | `swan-implementation-manual.md:83` `- Windows: Nmake(Visual Studio) 필요. OpenMP 는 Intel® Fortran 필요. MPI 는 Intel® MPI library.` | `src/CMakeLists.txt:75` `find_package( OpenMP REQUIRED COMPONENTS Fortran )`; 이력 대조: `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:src/CMakeLists.txt:40` `  if( WIN32 AND ${CMAKE_Fortran_COMPILER_VERSION} VERSION_GREATER_EQUAL 7 )`; `7ee8981:src/CMakeLists.txt:41` `    set( CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fdec" )`; `7ee8981:src/CMakeLists.txt:67` `  find_package( OpenMP REQUIRED COMPONENTS Fortran )`; `43e9bbb:src/CMakeLists.txt:75` `  find_package( OpenMP REQUIRED COMPONENTS Fortran )`; `43e9bbb:src/CMakeLists.txt:48` `  if( WIN32 AND ${CMAKE_Fortran_COMPILER_VERSION} VERSION_GREATER_EQUAL 7 )`; `43e9bbb:src/CMakeLists.txt:49` `    set( CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fdec" )` | C 문서 누락 | Windows OpenMP의 Intel 한정은 classic 설치 안내로 구분한다. 41.51 공개 시점의 Git CMake도 GNU Windows 설정과 OpenMP Fortran 탐색을 포함했다. |
| R7:N-007 | 전처리 표식 열 | `swan-implementation-manual.md:97` `` `!` + prefix 로 시작하는 컬럼 1-4 의 switch 를 제거하여 활성화: ``; swanimp PDF 18쪽(인쇄 12쪽), `../raw/manuals/website/online_doc/swanimp/node10.html:47–52`은 식별 접두부의 위치를 `first 3 or 4 columns`로 설명한다. | `switch.pl:84–105`의 행 첫머리 치환. 101행 `if ($met=~/TRUE/) {$newline=~s/^!METIS//;}`. | F 표기 차이 | 문서의 열 설명은 식별 접두부의 위치에 관한 느슨한 표기이다. 노트를 제거 길이가 4열로 고정된다는 주장으로 읽지 않는다. 구현은 행 첫머리에서 !METIS 등 해당 표식 전체를 제거한다고 설명한다. [10-13 전수 검증 정정] |
| R7:N-008 | CPU_TIME 활성 조건 | `swan-implementation-manual.md:102` ``\| `-f95` \| SWTSTA/SWTSTO 의 `CPU_TIME` 활성(`!F95`). 상세 timing (command `TEST itest=1`) \|``; 같은 노트 109행과 swanimp PDF 19–20쪽(인쇄 13–14쪽), `../raw/manuals/website/online_doc/swanimp/node10.html:66–70,111–113`은 -f95와 -timg를 각각 설명한다. | `src/swanser.ftn:5852` `!TIMG!F95      CALL CPU_TIME (TIMER)`; `switch.pl:84,90`은 !TIMG 뒤에 !F95를 치환한다. | C 문서 누락 | 문서에는 -f95와 -timg의 개별 설명이 있다. C는 노트의 -f95 행에 중첩 표식의 결합 조건이 빠진 범위로 한정한다. CPU_TIME 행의 전처리 활성화에는 -timg와 -f95가 모두 필요하다. |
| R7:N-009 | Jacobi와 MPI 순서 번역 | `swan-implementation-manual.md:103` ``\| `-jac` \| **block Jacobi**(`!JAC` 제거, `!WFR` 유지). 비/준정상 simulation 권장. **반드시 `-mpi` 뒤에** \|``; swanimp PDF 19쪽(인쇄 13쪽), 쪽 이미지 `swanimp-19.png`, `../raw/manuals/website/online_doc/swanimp/node10.html:87–91`. | `switch.pl:19–38`의 while 반복과 개별 if 판독; 23행 `if ($ARGV[0]=~/-jac/) {$jac="TRUE";shift;}`, 25행 `if ($ARGV[0]=~/-mpi/) {$mpi="TRUE";shift;}`. | B 문서 오기 | swanimp 원문은 `this option must be followed by the next option -mpi`이다. 노트의 ‘반드시 -mpi 뒤에’는 순서를 반대로 옮겼다. 현행 switch.pl은 두 옵션의 순서를 강제하지 않는다. |
| R7:N-010 | wavefront 권고 조건 | `swan-implementation-manual.md:104` ``\| (기본) \| **block wavefront**(`!WFR` 자동 제거) — 수렴특성 보존(non-stationary 권장) \|``; swanimp PDF 19쪽(인쇄 13쪽), 쪽 이미지 `swanimp-19.png`, `../raw/manuals/website/online_doc/swanimp/node10.html:72–91`. | `switch.pl:85–86` `if ($jac=~/TRUE/) {$newline=~s/^!JAC//;}`와 `else              {$newline=~s/^!WFR//;}`. | B 문서 오기 | 기본값은 block wavefront이다. 원문은 비정상·준정상 계산에 block Jacobi를 권고한다. 노트의 wavefront 설명에서 non-stationary 권장이라는 괄호를 제거한다. |
| R7:N-011 | 분할 모듈 확장자 | `swan-implementation-manual.md:127` ``- **module 선컴파일 순서** (node11 verbatim): `swmod1.f, swmod2.f` → `SwanSpectPart.f90` → `m_constants/m_fileio/serv_xnl4v5/mod_xnl4v5.f90` → `SwanGriddata/Gridobjects/Compdata.f90` → `SwanParallel.f90` → `SdsBabanin.f90` → `SwanIEM.f90` → `SwanBraggScat.f90` → `SwanQCM.f90`.``; swanimp PDF 21쪽(인쇄 15쪽), `../raw/manuals/website/online_doc/swanimp/node11.html:89`도 `SwanSpectPart.f90`이라고 적는다. | `src/srclist.cmake:4` `${SRC}/SwanSpectPart.${EXTF}`; `CMakeLists.txt:35–39`의 UNIX EXTF=f; `switch.pl:60–69`의 .ftn 확장자 변환; 원본 파일 `src/SwanSpectPart.ftn`. | B 문서 오기 | 노트는 원문의 SwanSpectPart.f90을 그대로 옮겼다. 이 확장자는 구현 매뉴얼의 모듈 컴파일 목록에도 있는 오기이다. 원본은 SwanSpectPart.ftn이다. UNIX 전처리 결과는 SwanSpectPart.f이다. |
| R7:N-012 | CMake 최소 버전 | `swan-implementation-manual.md:141` `cross-platform. **CMake 3.12+** 권장. generator 로 **Ninja**(GNU make 와 유사, 더 빠름) 권장.` | `CMakeLists.txt:6` `cmake_minimum_required( VERSION 3.20 )`; 이력 대조: `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:CMakeLists.txt:6` `cmake_minimum_required( VERSION 3.12 )`; `acb58b3 2026-01-30 small updates (300126)`; `acb58b3:CMakeLists.txt:6` `cmake_minimum_required( VERSION 3.20 )`; `43e9bbb:CMakeLists.txt:6` `cmake_minimum_required( VERSION 3.20 )` | A 판 차이 | Git 배포의 CMake 최소 버전은 2026-01-30에 3.12에서 3.20으로 바뀌었다. git 판정 근거는 `acb58b3`(2026-01-30)이다. |
| R7:N-013 | src 비오염 설명 | `swan-implementation-manual.md:145` `mkdir build && cd build         # out-of-source build (src 비오염)`; swanimp PDF 24쪽(인쇄 18쪽)은 오브젝트·실행 파일을 소스와 다른 디렉터리에 두는 out-of-source build를 설명한다. | `CMakeLists.txt:50–61`의 BIN·LIB·MOD 및 `set( SRC ${CMAKE_SOURCE_DIR}/src )`; `src/CMakeLists.txt:35–36` `execute_process( COMMAND ${PERL_EXECUTABLE} ${CMAKE_SOURCE_DIR}/switch.pl ${SWITCHES} ${SRC}/*.ftn ${SRC}/*.ftn90 )`; `switch.pl:62–77`은 입력 파일 경로에서 출력 파일명을 정한다. | B 문서 오기 | 오브젝트·실행 파일을 build 아래에 두는 원문 설명은 유지한다. 노트가 덧붙인 ‘src 비오염’은 고친다. 전처리한 Fortran 파일은 src에 생성한다. |
| R7:N-014 | 기본 설치 경로 | `swan-implementation-manual.md:148` `cmake --install .               # 기본 /usr/local/swan (Win: C:\PROGRAM FILES\swan)` | `CMakeLists.txt:13` `set( CMAKE_INSTALL_PREFIX "$ENV{HOME}/wavemodels/swan" CACHE STRING "" )`; 이력 대조: `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:CMakeLists.txt:10` `  set( CMAKE_INSTALL_PREFIX "C:/Program Files/swan" CACHE STRING "" )`; `7ee8981:CMakeLists.txt:12` `  set( CMAKE_INSTALL_PREFIX "/usr/local/swan" CACHE STRING "" )`; `acb58b3 2026-01-30 small updates (300126)`; `acb58b3:CMakeLists.txt:10` `  cmake_path( SET LOCALSWAN $ENV{LOCALAPPDATA}/Programs/wavemodels/swan )`; `acb58b3:CMakeLists.txt:11` `  set( CMAKE_INSTALL_PREFIX "${LOCALSWAN}" CACHE STRING "" )`; `acb58b3:CMakeLists.txt:13` `  set( CMAKE_INSTALL_PREFIX "$ENV{HOME}/wavemodels/swan" CACHE STRING "" )` | A 판 차이 | 기본 설치 경로는 2026-01-30에 사용자 폴더로 바뀌었다. UNIX 기본값은 $HOME/wavemodels/swan이다. Windows 기본값은 %LOCALAPPDATA%/Programs/wavemodels/swan이다. git 판정 근거는 `acb58b3`(2026-01-30)이다. |
| R7:N-015 | CMake 옵션 누락 | `swan-implementation-manual.md:159` ``\| `MPI` / `OPENMP` / `METIS` / `NETCDF` \| **OFF** \|``; swanimp PDF 25쪽(인쇄 19쪽)의 옵션 표와 `README.md:164–180`도 MPI·OPENMP·METIS·NETCDF만 열거한다. | `CMakeLists.txt:42–47`의 JAC·FFRO 기본값 OFF; `src/CMakeLists.txt:17–20` `if( JAC )`, `set( MPI ON )`; 26–28행 FFRO→-fixfront; 71–79행 `if( OPENMP AND MPI )`와 중단 메시지. | C 문서 누락 | Jacobi 병렬 방식 자체는 swanimp에 설명되어 있다. C는 CMake 옵션 목록에서 JAC·FFRO가 빠진 범위로 한정한다. 두 기본값은 OFF이다. JAC를 선택하면 MPI를 켠다. OPENMP와 MPI를 함께 선택하면 CMake가 중단한다. |
| R7:N-016 | 두 자리 연도 | `swan-implementation-manual.md:183` ``- **time coding option** (node19 verbatim): 1 `19870530.153000`(ISO, 권장·millennium 문제없음) / 2 `30-May-87 15:30:00` / 3 `05/30/87` / 4 `15:30:00` / 5 `87/05/30` / 6 `8705301530`(WAM). **ISO 외 옵션은 유효범위 1911-01-01 ~ 2010-12-31**.``; swanimp PDF 28쪽(인쇄 22쪽), 쪽 이미지 `swanimp-28.png`도 ISO 이외 옵션에 1911–2010을 적는다. | `src/ocpids.ftn:494` `INTEGER :: JUMPYEAR = 30     ! Used in interpretation of 2-digit year code`; 이력 대조: `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:src/ocpids.ftn:494` `      INTEGER :: JUMPYEAR = 30     ! Used in interpretation of 2-digit year code`; `43e9bbb:src/ocpids.ftn:494` `      INTEGER :: JUMPYEAR = 30     ! Used in interpretation of 2-digit year code`; `43e9bbb:src/ocpids.ftn:506` `        IF (DTTIME(1).LT.JUMPYEAR) THEN                                   40.89 30.70`; `43e9bbb:src/ocpids.ftn:507` `          DTTIME(1) = 2000 + DTTIME(1)                                    30.70`; `43e9bbb:src/ocpids.ftn:509` `          DTTIME(1) = 1900 + DTTIME(1)`; `43e9bbb:src/ocpids.ftn:527` `      ELSE IF (IOPT.EQ.4) THEN`; `43e9bbb:src/ocpids.ftn:528` `        READ (TIMSTR, '(I2,2(1X,I2))', ERR=98) (DTTIME(II), II=4,6)`; `43e9bbb:src/ocpids.ftn:529` `        DO 40 II = 1, 3`; `43e9bbb:src/ocpids.ftn:530` `          DTTIME(II) = 0` | B 문서 오기 | 노트의 1911–2010 범위는 swanimp 원문에도 있는 오기이다. 41.51 공개 코드도 형식 2·3·5·6의 두 자리 연도를 1930–2029로 해석한다. 형식 4는 날짜 성분을 0으로 둔다. ISO 이외의 모든 형식에 1911–2010 범위를 적용한 문장을 고친다. |
| R7:N-017 | 프로세서 속도 예시의 격자 조건 | `swan-implementation-manual.md:184` ``- processor speed: % of 100. 예 1.5배 빠른 노드 = `150`/`100` → 1000 active point 를 600/400 자동 분배(MPI 부하균형, [swan-tech-ch7-parallel](swan-tech-ch7-parallel.md) §7.1 load balancing 의 사용자측).``; swanimp PDF 29쪽(인쇄 23쪽), 쪽 이미지 `swanimp-29.png`의 150·100 및 1000→600·400 예시. | `src/swanparll.ftn:2263–2294`의 구조 격자 활성점 집계와 `IWORK(2,I) = (NACTP*ICNT)/SUM(IWEIG) - NPCUM`; `src/SwanParallel.ftn90:481–483`의 Metis 목표 가중치 `tpwgts = 1./real(np)`. | C 문서 누락 | 150:100에 따른 600:400 예시는 구조 격자의 활성점 분할에 해당한다. 현재 Metis 경로의 목표 가중치는 모든 프로세서에 동일하다. 노트에 격자 조건을 추가한다. |
| R7:N-018 | 편집 파일의 전체 명령 주장 | `swan-implementation-manual.md:188` ``명령 파일(`.swn`) 완성 후 실행. `swan.edt` = 전체 command set template.``; swanimp PDF 31쪽(인쇄 25쪽), `../raw/manuals/website/online_doc/swanimp/node20.html:76–78`도 편집을 돕는 `complete set of commands`라고 표현한다. | `misc/swan.edt:1` `!   PROJECT  'name'  'nr'`; 해당 파일에 COTE 일치 없음. `src/swanpre1.ftn:637–642`은 `!     COTE [cotes]         (NOT documented)`와 `IF (KEYWIS ('COTE')) THEN`을 둔다. | C 문서 누락 | 노트의 ‘전체 command set’은 원문의 편집 보조 설명을 옮긴 것이다. 이를 숨은 개발용 명령까지 포함하는 전수 명세로 읽지 않는다. C는 편집용 구문표라는 범위 설명을 보완하는 판정이다. |
| R7:N-019 | PATH와 OpenMP 환경 예시 | `swan-implementation-manual.md:194` ``- `PATH` 에 swan.exe 디렉토리 추가: `export PATH=${PATH}:/usr/local/swan` (csh: `setenv`). OpenMP: `export OMP_NUM_THREADS=4`.``; swanimp PDF 32–33쪽(인쇄 26–27쪽), `../raw/manuals/website/online_doc/swanimp/node20.html:103–139,163–184`은 실행 파일 위치라는 PATH 예시 조건과 -omp n을 적는다. | `src/CMakeLists.txt:124,130–132`의 bin 설치; `bin/swanrun:10` `export OMP_NUM_THREADS=1`; 20행 -omp 판독; 84–86행 `if [ $npomp -gt 1 ]; then`과 `export OMP_NUM_THREADS=$npomp`. | C 문서 누락 | PATH 예시는 swan.exe가 그 디렉터리에 있을 때 유효하다. CMake로 설치한 실행 파일은 설치 위치의 bin에 있다. 외부 OMP_NUM_THREADS 설정과 UNIX 래퍼 호출 조건을 구분한다. 래퍼에는 -omp n을 전달한다. C는 노트의 예시에 이 조건이 빠진 범위로 한정한다. |
| R7:N-020 | machinefile의 Windows 조건 | `swan-implementation-manual.md:195` ``- MPI run 은 `mpirun`/`mpiexec`. machinefile 1 노드/line, `node7:4`(콜론=core 수; Windows 는 space). swan.exe 를 모든 노드 공유.``; swanimp PDF 33쪽(인쇄 27쪽), `../raw/manuals/website/online_doc/swanimp/node20.html:194–208`은 machinefile의 MPI 프로세스 배치 예시를 설명한다. | `bin/swanrun:92–96`은 `if [ $npmpi -gt 1 ]; then`에서 `mpirun -np $npmpi -machinefile machinefile swan.exe`; `bin/swanrun.bat:34–39`은 `mpiexec -n %nprocs% swan.exe`. | C 문서 누락 | UNIX 래퍼는 MPI 프로세스 수가 1보다 클 때 machinefile을 전달한다. Windows 래퍼는 이 파일을 전달하지 않는다. 문서의 machinefile 형식 안내를 두 래퍼의 동일한 자동 동작으로 확대하지 않는다. 콜론 뒤 수는 요청한 MPI 프로세스 배치 수이다. |
| R7:N-021 | 검증·메모리 권고 | `swan-implementation-manual.md:201` ``패키지 = `swan.exe` + `swan.edt` + `swanrun(.bat)`. 사이트의 test 입출력(`.swn` command, `.bot` bottom 등)으로 구성 테스트. **결과는 마지막 자리까지 동일할 필요 없음**. 메모리 권장: test ≥ 50 MB, 현실 case 100-500 MB, 1D < 5 MB.``; swanimp PDF 35쪽(인쇄 29쪽), 쪽 이미지 `swanimp-35.png`의 시험·메모리 안내. | `README.md:245` `1. **serial**: for computers using one processor (recommended for small tests)` | H 코드 대조 대상 아님 | 50 MB 이상은 시험 사례의 권장 메모리이다. 원문은 현실적인 응용에 100–500 MB가 필요할 수 있다고 적는다. 1차원 계산은 대체로 5 MB 미만이라는 안내이다. 이 숫자를 코드가 보장하는 고정 메모리 요구량으로 쓰지 않는다. |
| R7:N-035 | 노트의 coupler 파일 목록 | `swan-implementation-manual.md:48` `couple2adcirc.ftn90` `swan2coh.ftn90` | `switch.pl:97` `if ($adc=~/TRUE/) {$newline=~s/^!ADC//;}`; 이력 대조: `couple[ _-]?2[ _-]?adcirc\|swan[ _-]?2[ _-]?coh`: 0행; `couple[ _-]?2[ _-]?adcirc\|swan[ _-]?2[ _-]?coh\|coupl(e\|ing).{0,24}(adcirc\|coh)`: 9행; `!ADC\|!COH`: 2행. `git rev-list --objects`로 얻은 조사 범위의 경로 목록에서도 두 파일명의 일치는 0건이다.; 41.45부터 `43e9bbb`까지 `-S 'couple2adcirc'`, `-S 'swan2coh'` 및 두 이름의 철자 변형 `-G '[Cc][Oo][Uu][Pp][Ll][Ee][ _-]?2[ _-]?[Aa][Dd][Cc][Ii][Rr][Cc]\|[Ss][Ww][Aa][Nn][ _-]?2[ _-]?[Cc][Oo][Hh]'`은 각각 0커밋이다. 2980d1a:switch.pl:97 `if ($coh=~/TRUE/) {$newline=~s/^!COH//;}`. 43e9bbb:switch.pl:99 `if ($coh=~/TRUE/) {$newline=~s/^!COH//;}`. 43e9bbb:src/srclist.cmake:1 `set( swan_src`. | D 문서에만 있음 | 현재 Git 배포의 파일 목록에서 couple2adcirc.ftn90과 swan2coh.ftn90을 제외한다. 매뉴얼의 목록을 인용할 때에는 두 파일이 조사한 Git 배포에 없다고 명시한다. |
